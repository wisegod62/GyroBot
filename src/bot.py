import discord

from discord.ext import commands

from src.config import DISCORD_TOKEN
from src.database.database import engine, Base
from src.database.models import Profile

Base.metadata.create_all(bind=engine)


class GyroBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.default())

    async def setup_hook(self):

        await self.load_extension("src.cogs.profiles")

        await self.load_extension("src.cogs.journal")

        await self.load_extension("src.cogs.practice")

        await self.load_extension("src.cogs.flags")

        commands = await self.tree.sync()

        print(f"Synced {len(commands)} commands")
        for command in commands:
            print(f" - {command.name}")

    async def on_ready(self):

        print(f"Logged in as {self.user}")


bot = GyroBot()

bot.run(DISCORD_TOKEN)
