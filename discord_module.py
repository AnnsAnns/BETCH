import re
import discord

from discord.ext import commands
from discord.ext.commands import Cog

import BETCH
import data.legacy_errcodes

class Err(Cog):
    """Everything related to Nintendo 3DS, Wii U and Switch error codes"""

    def __init__(self, bot):
        self.bot = bot
        self.regex_nor_err = re.compile(r'2\d{3}\-\d{4}')
        BETCH.scrap()
        self.errcodes = BETCH.load()

    @commands.command(aliases=["error", "nxerr", "serr"])
    async def err(self, ctx, err: str):
        """Searches for Switch error codes!
            Usage: .serr/.nxerr/.err <Error Code>"""
        errcodes = self.errcodes
        module_name = "Unknown"
        desc_name = "Unknown"

        if err.startswith("0x"):
            err = err[2:]
            errcode = int(err, 16)
            module = errcode & 0x1FF
            desc = (errcode >> 9) & 0x3FFF
        
        elif self.regex_nor_err.match(err):
            module = int(err[0:4]) - 2000
            desc = int(err[5:9])
            errcode = (desc << 9) + module

        elif err in data.legacy_errcodes.switch_game_err: # Special handling
            game, desc = data.legacy_errcodes.switch_game_err[err].split(":")

            embed = discord.Embed(title=err,
                                  url=self.rickroll,
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

        elif module in data.legacy_errcodes.switch_known_errcode_ranges:
            for err_range in data.legacy_errcodes.switch_known_errcode_ranges[module]:
                if desc >= err_range[0] and desc <= err_range[1]:
                    desc_name = err_range[2]

        elif dec_err in data.legacy_errcodes.switch_support_page:
            desc_name = data.legacy_errcodes.switch_support_page[dec_err]

        elif errcode in data.legacy_errcodes.special_err:
            desc_name = data.legacy_errcodes.special_err[errcode]

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
        
def setup(bot):
    bot.add_cog(Err(bot))
