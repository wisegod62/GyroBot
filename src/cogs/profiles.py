from discord.ext import commands
from discord import app_commands

import discord

from src.services.profile_service import ProfileService
from src.ui.profile_modal import ProfileEditModal
from src.ui.badge_view import BadgeView

from src.constants.badges import BADGES, SELECTABLE_BADGES


class Profiles(commands.Cog):
    profile_group = app_commands.Group(name="profile", description="Profile commands")
    edit_group = app_commands.Group(name="edit", description="Edit your profile")

    profile_group.add_command(edit_group)

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

        if profile.badges:
            selected = profile.badges.split(",") if profile.badges else []

            display_badges = [
                BADGES.get(badge.strip(), badge.strip()) for badge in selected
            ]

            embed.add_field(
                name="Badges",
                value="\n".join(display_badges) if display_badges else "None",
                inline=False,
            )

        return embed

    async def update_profile_field(self, interaction, field: str, value: str):

        self.profile_service.update_field(interaction.user.id, field, value)

        await interaction.response.send_message(
            f"{field.title()} updated.", ephemeral=True
        )

    @profile_group.command(name="view", description="View a profile")
    async def view(self, interaction, member: discord.Member | None = None):
        target = member or interaction.user

        profile = self.profile_service.get_or_create_profile(target.id)
        self.profile_service.check_automatic_badges(target)
        profile = self.profile_service.get_or_create_profile(target.id)

        await interaction.response.send_message(embed=self.build_embed(target, profile))

    @edit_group.command(name="identity", description="Edit identity information")
    async def identity(self, interaction):
        profile = self.profile_service.get_or_create_profile(interaction.user.id)

        await interaction.response.send_modal(
            ProfileEditModal(
                self.profile_service,
                interaction.user.id,
                profile,
                ["pronouns", "gender", "sexuality"],
            )
        )

    @edit_group.command(name="about", description="Edit bio and interests")
    async def about(self, interaction):
        profile = self.profile_service.get_or_create_profile(interaction.user.id)

        await interaction.response.send_modal(
            ProfileEditModal(
                self.profile_service,
                interaction.user.id,
                profile,
                ["bio", "interests"],
            )
        )

    @edit_group.command(name="appearance", description="Edit profile appearance")
    async def appearance(self, interaction):
        profile = self.profile_service.get_or_create_profile(interaction.user.id)

        await interaction.response.send_modal(
            ProfileEditModal(
                self.profile_service,
                interaction.user.id,
                profile,
                ["card_color"],
            )
        )

    @edit_group.command(name="badges", description="Edit your badges")
    async def badges(self, interaction):

        profile = self.profile_service.get_or_create_profile(interaction.user.id)

        await interaction.response.send_message(
            "Choose your badges:",
            view=BadgeView(self.profile_service, interaction.user.id, profile),
            ephemeral=True,
        )


async def setup(bot):
    await bot.add_cog(Profiles(bot))
