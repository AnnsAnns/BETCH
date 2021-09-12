# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import re
import discord
import BETCH
import asyncio
import random
import pickle
import aiohttp

from pprint import pprint as print # Replace with better printing function
from config import token
from discord.ext import commands
from dislash import InteractionClient, Option, OptionType
from data.legacy_errcodes import switch_known_errcode_ranges, switch_game_err

bot = commands.Bot(command_prefix=".")
inter_client = InteractionClient(bot, test_guilds=[335895133805477889, 364791892635811840])
regex_nor_err = re.compile(r"2\d{3}\-\d{4}")
usage_stats = {}
status_q = ("crashing Switches", "fatals around the world", "crying developers", "confused developers", 
            "homebrews crashing", "ko-fi.com/tomGER donations")
bot.remove_command("help")
desc_donation_link = "\n \n Please consider donating to keep the API running via https://ko-fi.com/tomger"
slash_reminder = " - Please start using the provided Slash commands (eg. /err)! Discord is phasing out the old system, see: https://github.com/tumGER/BETCH/issues/26"

async def c_status():
    await bot.wait_until_ready()
    while True:
        await bot.change_presence(activity=discord.Activity(name=f"{random.choice(status_q)} | .err", type=2), status=discord.Status.dnd)
        await asyncio.sleep(1800)
        
@bot.event
async def on_ready():
    members = 0
    
    for guild in bot.guilds:
        members += guild.member_count
        
    print(f"Started {bot.user.name} on {len(bot.guilds)} servers with {members} members!")
    
@inter_client.slash_command(description = "Searches for Switch error codes!", options = [Option("error_code", "Specify the error code. Supported formats: Hex (0x4a8) or String (2168-0002)", required=True)])
async def err(ctx, error_code: str):
    """Searches for Switch error codes!
        Usage: .serr/.nxerr/.err <Error Code>"""
    err = error_code # Legacy problem
        
    module_name = "Unknown Module"
    desc_name = " It seems like the error code is unknown! \n If you know the reason for the error code please either update https://switchbrew.org/wiki/Error_codes " \
                "or send a PR to https://github.com/tumGER/BETCH."

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
                            url="https://github.com/tumGER/BETCH",
                            description=f"{desc} {desc_donation_link}")
        embed.set_footer(text="Console: Nintendo Switch" + slash_reminder)
        embed.add_field(name="Game", value=game, inline=True)

        await ctx.send(embed=embed)
        return
    else:
        await ctx.send("Your error code seems to be in a wrong format.")
        return
    
    dec_err = f"{(module + 2000):04}-{desc:04}"

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://raw.githubusercontent.com/tumGER/BETCH/actions/api.json") as resp:
            response = await resp.json(content_type="text/plain")
    
    if str(module) in response.keys():
        if "name" in response[str(module)].keys() \
        and response[str(module)]["name"] != None:
            module_name = response[str(module)]["name"]
        else:
            module_name = "Unknown"
        desc_name = response[str(module)][str(desc)] if str(desc) in response[str(module)].keys() else "Unknown"
    else:
        module_name = "Unknown"
        desc_name = "Unknown"
        
    # Find the description #        
    if module in switch_known_errcode_ranges:
        for err_range in switch_known_errcode_ranges[module]:
            if desc >= err_range[0] and desc <= err_range[1]:
                desc_name = err_range[2]

    # Embed Creation #
    embed = discord.Embed(title=f"{dec_err} / {hex(errcode)}",
                        url="https://github.com/tumGER/BETCH",
                        description=f"{desc_name} {desc_donation_link}")
    embed.set_author(name="Error Code Bot",
                     icon_url="https://raw.githubusercontent.com/tumGER/Random-Stuff/c05959658d3ca0fb8d0a7d674062b2b845d88c3d/GBATemp%20Sign%20Meme/inkscape_hql9WK4JaJ.png")
    embed.add_field(name="Module",
                    value=f"{module_name} ({module})",
                    inline=True)
    embed.add_field(name="Description", value=desc, inline=True)
    embed.set_footer(text=f"Console: Nintendo Switch" + slash_reminder)
    await ctx.send(embed=embed)

@inter_client.slash_command(description = "Searches for informations related to the module", options = [Option("module", "Specify the module number. (1, 3, etc.)", required=True)])
async def module(ctx, module: str):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://raw.githubusercontent.com/tumGER/BETCH/actions/api.json") as resp:
            errcodes = await resp.json(content_type="text/plain")
    
    if not module.isdigit():
        for module_int in errcodes:
            if not "name" in errcodes[module_int]:
                continue
            
            if module.lower() in errcodes[module_int]["name"].lower():
                module = module_int
                break
    
    if not module in errcodes:
        await ctx.send("ERROR: There is no entry for that module!")
        return

    module_name = errcodes[module]["name"] if "name" in errcodes[module] else "Unknown"
    number_errors = len(errcodes[module])
    
    # Embed Creation #
    embed = discord.Embed(title=f"{module_name} ({module})",
                        url="https://github.com/tumGER/BETCH",
                        description=f"The module {module_name} ({module}) has {number_errors} registered errors. {desc_donation_link}")
    embed.set_author(name="Error Code Bot",
                     icon_url="https://raw.githubusercontent.com/tumGER/Random-Stuff/c05959658d3ca0fb8d0a7d674062b2b845d88c3d/GBATemp%20Sign%20Meme/inkscape_hql9WK4JaJ.png")
    embed.set_footer(text="Console: Nintendo Switch" + slash_reminder)
    await ctx.send(embed=embed)
    
###
# THIS SECTION EXISTS IN ORDER TO SUPPORT THE LEGACY CMD MESSAGE FORMAT
###

@bot.command(aliases=["err", "error", "nxerr", "serr"])
async def old_err(ctx, err_arg: str):
    await err(ctx, err_arg)

@bot.command(aliases=["module", "modules", "errmodule", "dec2module"])
async def old_module(ctx, module_arg: str):
    await module(ctx, module_arg)

@bot.command()
async def help(ctx):
    await ctx.send("Please start using Slash-commands. You can type either /err or /module to get more informations about both functions! \n"\
        "In the future this bot **will have to** drop the support for message-based commands because of a decision by Discord.\n"\
        "For more informations visit: <https://github.com/tumGER/BETCH/issues/26>")

@bot.event
async def on_command_error(ctx, error):
    print(f"Error: \"{str(error)}\" when someone typed \"{ctx.message.content}\"")

bot.loop.create_task(c_status())
bot.run(token)
