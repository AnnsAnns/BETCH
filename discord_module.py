import re
import discord
import BETCH
import asyncio
from pprint import pprint as print # Replace with better printing function
import random

from discord.ext import commands
from data.legacy_errcodes import *

bot = commands.Bot(command_prefix=".")
regex_nor_err = re.compile(r"2\d{3}\-\d{4}")
errcodes = {}
errcodes = BETCH.scrap()
status_q = ("crashing Switches", "fatals around the world", "crying developers", "confused developers", 
            "homebrews crashing", "atmosphere silent updates", "jakibaki cleaning sysmodule ram", "#support")

async def error_updater():
    global errcodes
    while True:
        await asyncio.sleep(21600)
        errcodes = BETCH.scrap()

async def c_status():
    await bot.wait_until_ready()
    while True:
        await bot.change_presence(activity=discord.Activity(name=f"{random.choice(status_q)} | .err"), status=discord.Status.dnd)
        await asyncio.sleep(1800)
        
@bot.event
async def on_ready():
    print(f"Started on {str(len(bot.guilds))} servers:")
    for guild in bot.guilds:
        print(f"{guild.name}")
                
@bot.command(aliases=["error", "nxerr", "serr"])
async def err(ctx, err: str):
    """Searches for Switch error codes!
        Usage: .serr/.nxerr/.err <Error Code>"""
    module_name = "Unknown Module"
    desc_name = " It seems like the error code is unknown! \n If you know the reason for the error code please either update https://switchbrew.org/wiki/Error_codes " \
                "or send a PR to https://github.com/AtlasNX/BETCH."

    if err.startswith("0x"):
        err = err[2:]
        errcode = int(err, 16)
        module = errcode & 0x1FF
        desc = (errcode >> 9) & 0x3FFF
    
    elif regex_nor_err.match(err):
        module = int(err[0:4]) - 2000
        desc = int(err[5:9])
        errcode = (desc << 9) + module

    elif err in switch_game_err: # Special handling
        game, desc = switch_game_err[err].split(":")

        embed = discord.Embed(title=err,
                            url="https://github.com/AtlasNX/BETCH",
                            description=desc)
        embed.set_footer(text="Console: Nintendo Switch")
        embed.add_field(name="Game", value=game, inline=True)

        await ctx.send(embed=embed)
    
    else:
        await ctx.send("Your error code seems to be in a wrong format.")
    
    dec_err = f"{(module + 2000):04}-{desc:04}"

    # Find the module name #
    if module in errcodes:
        module_name = errcodes[module]["name"]
    
    # Find the description #        
    if module in switch_known_errcode_ranges:
        for err_range in switch_known_errcode_ranges[module]:
            if desc >= err_range[0] and desc <= err_range[1]:
                desc_name = err_range[2]

    elif errcode in special_err:
        desc_name = special_err[errcode]

    elif dec_err in switch_support_page:
        desc_name = switch_support_page[dec_err]
    
    elif errcode in fs_err:
        desc_name = fs_err[errcode]
        
    # Always overwrite even if already found #    
    if module in errcodes:
        if desc in errcodes[module]:
            desc_name = errcodes[module][desc]
            
    if module in fatal_err:
        if desc in fatal_err[module]:
            desc_name = fatal_err[module][desc]

    # Embed Creation #
    embed = discord.Embed(title=f"{dec_err} / {hex(errcode)}",
                        url="https://github.com/AtlasNX/BETCH",
                        description=desc_name)
    embed.set_author(name="Team AtlasNX Error Code Bot",
                     icon_url="https://raw.githubusercontent.com/AtlasNX/Kosmos/4231e4e1a594b7196f3b4f1a4f65c1591085fa0b/Resources/Icons/atlasnx_trans.png")
    embed.add_field(name="Module",
                    value=f"{module_name} ({module})",
                    inline=True)
    embed.add_field(name="Description", value=desc, inline=True)
    embed.set_footer(text=f"Console: Nintendo Switch")
    await ctx.send(embed=embed)

@bot.command(aliases=["error2hex", "e2h", "err2hex", "err2hax"])
async def errortohex(ctx, err: str):
    if regex_nor_err.match(err):
        module = int(err[0:4]) - 2000
        desc = int(err[5:9])
        errcode = (desc << 9) + module
        
        await ctx.send(f"{err} equals {hex(errcode)}")
    else:
        await ctx.send("The error code you have entered doesn't seem to be correct")

@bot.command(aliases=["hex2err", "h2e", "hax2err"])
async def hextoerror(ctx, err: str):
    if err.startswith("0x"):
        err = err[2:]
        errcode = int(err, 16)
        module = errcode & 0x1FF
        desc = (errcode >> 9) & 0x3FFF
        dec_err = f"{(module + 2000):04}-{desc:04}"
        
        await ctx.send(f"{hex(err)} equals {dec_err}")
    else:
        await ctx.send("The error code you have entered doesn't seem to be correct")

bot.loop.create_task(c_status())
bot.loop.create_task(error_updater())
bot.run("TOKEN")
