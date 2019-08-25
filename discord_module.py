import re
import discord
import BETCH
import asyncio

from discord.ext import commands
from data.legacy_errcodes import *

bot = commands.Bot(command_prefix=".")
regex_nor_err = re.compile(r"2\d{3}\-\d{4}")

async def error_updater():
    global errcodes
    while True:
        errcodes = await BETCH.scrap()
        await asyncio.time.sleep(21600)

@bot.command(aliases=["error", "nxerr", "serr"])
async def err(self, ctx, err: str):
    """Searches for Switch error codes!
        Usage: .serr/.nxerr/.err <Error Code>"""
    errcodes = errcodes
    module_name = "Unknown"
    desc_name = "Unknown"

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
        embed.set_footer(text="Console: Switch")
        embed.add_field(name="Game", value=game, inline=True)

        await ctx.send(embed=embed)
    
    else:
        ctx.send("Your error code seems to be in a wrong format.")
    
    dec_err = f"{(module + 2000):04}-{desc:04}"

    # Find the module name #
    if module in errcodes:
        module_name = errcodes[module]["name"]
    
    # Find the description #
    if desc in errcodes[module]:
        desc_name = errcodes[module][desc]

    elif module in switch_known_errcode_ranges:
        for err_range in switch_known_errcode_ranges[module]:
            if desc >= err_range[0] and desc <= err_range[1]:
                desc_name = err_range[2]

    elif dec_err in switch_support_page:
        desc_name = switch_support_page[dec_err]

    elif errcode in special_err:
        desc_name = special_err[errcode]

    # Embed Creation #
    embed = discord.Embed(title=f"{dec_err} / {hex(errcode)}",
                        url="https://github.com/AtlasNX/BETCH",
                        description=desc_name)
    embed.add_field(name="Module",
                    value=f"{module_name} ({module})",
                    inline=True)
    embed.add_field(name="Description", value=desc, inline=True)
    embed.set_footer(text=f"Brought to you by AtlasNX | Console: Nintendo",
                    icon_url="https://github.com/AtlasNX/Kosmos/blob/4231e4e1a594b7196f3b4f1a4f65c1591085fa0b/Resources/Icons/atlasnx_trans.png")
    ctx.send(embed=embed)
    
bot.loop.create_task(error_updater())   
bot.run("TOKEN")
