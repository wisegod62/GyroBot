from discord.ext import commands
from discord import app_commands
import discord


class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="about", description="I yap about this bot")
    async def about(self, interaction):
        embed = discord.Embed(
            title="About GyroBot",
            description="A Discord bot for profiles and journaling",
            color=discord.Color.blue(),
        )
        embed.add_field(
            name="GitHub",
            value="[Repository](https://github.com/wisegod62/GyroBot)",
            inline=False,
        )
        embed.add_field(name="Version", value="0.2.0", inline=True)
        embed.add_field(name="Author", value="wisegod62", inline=True)
        embed.set_footer(text="Made with discord.py")

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(About(bot))
