import discord


class ProfileEditModal(discord.ui.Modal):
    def __init__(self, profile_service, user_id, profile, fields):
        super().__init__(title="Edit Profile")

        self.profile_service = profile_service
        self.user_id = user_id
        self.fields = fields

        self.inputs = {}

        for field in fields:
            if field == "card_color":
                default = f"#{profile.card_color:06X}"
            else:
                default = str(getattr(profile, field))
            input_box = discord.ui.TextInput(
                label=field.replace("_", " ").title(),
                default=default,
                required=False,
                style=(
                    discord.TextStyle.paragraph
                    if field in ["bio", "interests"]
                    else discord.TextStyle.short
                ),
            )

            self.inputs[field] = input_box

            self.add_item(input_box)

    async def on_submit(self, interaction):

        for field, input_box in self.inputs.items():
            value = input_box.value

            if field == "card_color":
                value = self.profile_service.parse_color(value)

            self.profile_service.update_field(self.user_id, field, value)

        await interaction.response.send_message("Profile updated.", ephemeral=True)
