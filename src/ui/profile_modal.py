import discord


class ProfileModal(discord.ui.Modal, title="Edit Profile"):
    def __init__(self, profile_service, user_id, profile):
        super().__init__()

        self.profile_service = profile_service
        self.user_id = user_id

        self.pronouns = discord.ui.TextInput(
            label="Pronouns", default=profile.pronouns, required=False, max_length=50
        )

        self.gender = discord.ui.TextInput(
            label="Gender", default=profile.gender, required=False, max_length=50
        )

        self.sexuality = discord.ui.TextInput(
            label="Sexuality", default=profile.sexuality, required=False, max_length=50
        )

        self.interests = discord.ui.TextInput(
            label="Interests", default=profile.interests, required=False, max_length=200
        )

        self.bio = discord.ui.TextInput(
            label="Bio",
            default=profile.bio,
            required=False,
            style=discord.TextStyle.paragraph,
            max_length=500,
        )

        self.add_item(self.pronouns)
        self.add_item(self.gender)
        self.add_item(self.sexuality)
        self.add_item(self.interests)
        self.add_item(self.bio)

    async def on_submit(self, interaction: discord.Interaction):

        self.profile_service.update_field(self.user_id, "pronouns", str(self.pronouns))

        self.profile_service.update_field(self.user_id, "gender", str(self.gender))

        self.profile_service.update_field(
            self.user_id, "sexuality", str(self.sexuality)
        )

        self.profile_service.update_field(
            self.user_id, "interests", str(self.interests)
        )

        self.profile_service.update_field(self.user_id, "bio", str(self.bio))

        await interaction.response.send_message("Profile updated.", ephemeral=True)
