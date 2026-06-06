from discord.ext import commands
from discord import app_commands

import discord

from src.services.profile_service import ProfileService


class Profiles(commands.Cog):
    profile_group = app_commands.Group(name="profile", description="Profile commands")

    def __init__(self, bot):
        self.bot = bot
        self.profile_service = ProfileService()

    def build_embed(self, user, profile):

        embed = discord.Embed(
            title=f"{user.display_name}'s Profile", color=profile.card_color
        )

        embed.set_thumbnail(url=user.display_avatar.url)

        embed.add_field(
            name="Pronouns", value=profile.pronouns or "Not Set", inline=True
        )

        embed.add_field(name="Gender", value=profile.gender or "Not Set", inline=True)

        embed.add_field(
            name="Sexuality", value=profile.sexuality or "Not Set", inline=True
        )

        embed.add_field(name="Bio", value=profile.bio or "Not Set", inline=False)

        embed.add_field(
            name="Interests", value=profile.interests or "Not Set", inline=False
        )

        embed.add_field(name="Flag", value=profile.flag or "Not Set", inline=False)

        return embed

    async def update_profile_field(self, interaction, field: str, value: str):

        self.profile_service.update_field(interaction.user.id, field, value)

        await interaction.response.send_message(
            f"{field.title()} updated.", ephemeral=True
        )

    @profile_group.command(name="view", description="View your profile")
    async def view(self, interaction):

        profile = self.profile_service.get_or_create_profile(interaction.user.id)

        await interaction.response.send_message(
            embed=self.build_embed(interaction.user, profile)
        )

    @profile_group.command(name="pronouns", description="Set your pronouns")
    async def pronouns(self, interaction, pronouns: str):

        await self.update_profile_field(interaction, "pronouns", pronouns)

    @profile_group.command(name="bio", description="Set your bio")
    async def bio(self, interaction, bio: str):

        await self.update_profile_field(interaction, "bio", bio)

    @profile_group.command(name="gender", description="Set your gender")
    async def gender(self, interaction, gender: str):

        await self.update_profile_field(interaction, "gender", gender)

    @profile_group.command(name="sexuality", description="Set your sexuality")
    async def sexuality(self, interaction, sexuality: str):

        await self.update_profile_field(interaction, "sexuality", sexuality)

    @profile_group.command(name="interests", description="Set your interests")
    async def interests(self, interaction, interests: str):

        await self.update_profile_field(interaction, "interests", interests)


async def setup(bot):
    await bot.add_cog(Profiles(bot))
