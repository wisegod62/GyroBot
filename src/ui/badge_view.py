import discord

from src.constants.badges import BADGES


class BadgeSelect(discord.ui.Select):
    def __init__(self, profile_service, user_id, profile):
        self.profile_service = profile_service
        self.user_id = user_id

        current_badges = []

        if profile.badges:
            current_badges = profile.badges.split(",")

        options = []

        for badge_name, badge_display in BADGES.items():
            options.append(
                discord.SelectOption(
                    label=badge_name,
                    description=badge_display,
                    default=badge_name in current_badges,
                )
            )

        super().__init__(
            placeholder="Choose your badges",
            min_values=0,
            max_values=len(options),
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):

        badges = ",".join(self.values)

        self.profile_service.update_field(self.user_id, "badges", badges)

        await interaction.response.send_message("Badges updated.", ephemeral=True)


class BadgeView(discord.ui.View):
    def __init__(self, profile_service, user_id, profile):
        super().__init__()

        self.add_item(BadgeSelect(profile_service, user_id, profile))
