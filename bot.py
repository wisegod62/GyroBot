#!/usr/bin/env python3

import json
import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from pride_data import GENDERS, SEXUALITIES

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
PROFILE_FILE = "user_profiles.json"

if os.path.exists(PROFILE_FILE):
    with open(PROFILE_FILE, "r") as f:
        user_profiles = json.load(f)
else:
    user_profiles = {}


def save_profiles():
    with open(PROFILE_FILE, "w") as f:
        json.dump(user_profiles, f, indent=4)


class MyBot(discord.Client):

    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(f"Failed to sync commands: {e}")


bot = MyBot()


# --- MODAL FOR CUSTOM IDENTITY ---

class CustomIdentityModal(discord.ui.Modal, title="Custom Identity"):
    identity_input = discord.ui.TextInput(
        label="Your custom identity",
        placeholder="e.g., genderqueer, demisexual, etc.",
        required=True,
        max_length=100,
    )
    color_input = discord.ui.TextInput(
        label="Color (hex code, optional)",
        placeholder="e.g., FF00FF (leave blank for default)",
        required=False,
        max_length=6,
    )

    def __init__(self, identity_type: str):
        super().__init__()
        self.identity_type = identity_type  # "gender" or "sexuality"

    async def on_submit(self, interaction: discord.Interaction):
        identity_text = self.identity_input.value.strip().lower()
        color_text = self.color_input.value.strip()

        # Default color (purple for gender, green for sexuality)
        color = 0x9B59B6 if self.identity_type == "gender" else 0x2ECC71
        if color_text:
            try:
                color = int(color_text, 16)
            except ValueError:
                await interaction.response.send_message(
                    "❌ Invalid hex color code. Using default color.",
                    ephemeral=True,
                )

        user_id = str(interaction.user.id)
        if user_id not in user_profiles:
            user_profiles[user_id] = {
                "pronouns": "Not Set",
                "gender": "Not Set",
                "sexuality": "Not Set",
            }

        # Store custom identities with a marker
        if self.identity_type == "gender":
            user_profiles[user_id]["gender"] = f"custom:{identity_text}:{color:06X}"
        else:
            user_profiles[user_id]["sexuality"] = f"custom:{identity_text}:{color:06X}"

        save_profiles()
        await interaction.response.send_message(
            f"✅ Your custom {self.identity_type} identity has been saved!",
            ephemeral=True,
        )


# --- AUTOCOMPLETE HELPERS ---

async def gender_autocomplete(
    interaction: discord.Interaction, current: str
) -> list[app_commands.Choice[str]]:
    choices = [
        app_commands.Choice(name=g.title(), value=g) for g in GENDERS.keys()
        if current.lower() in g
    ]
    # Add "Custom" at the top if it matches
    if "custom".startswith(current.lower()):
        choices.insert(0, app_commands.Choice(name="Custom", value="__custom__"))
    return choices[:25]


async def sexuality_autocomplete(
    interaction: discord.Interaction, current: str
) -> list[app_commands.Choice[str]]:
    choices = [
        app_commands.Choice(name=s.title(), value=s) for s in SEXUALITIES.keys()
        if current.lower() in s
    ]
    # Add "Custom" at the top if it matches
    if "custom".startswith(current.lower()):
        choices.insert(0, app_commands.Choice(name="Custom", value="__custom__"))
    return choices[:25]


# --- HELPER TO PARSE CUSTOM IDENTITIES ---

def parse_custom_identity(value: str):
    """Parse custom identity string. Returns (display_name, color) or (None, None) if not custom."""
    if value.startswith("custom:"):
        parts = value.split(":")
        if len(parts) >= 3:
            display_name = parts[1]
            try:
                color = int(parts[2], 16)
                return display_name, color
            except ValueError:
                return parts[1], 0x9B59B6
    return None, None


# --- EXISTING COMMAND ---

@bot.tree.command(
    name="transphobia", description="What is it? Run the command to see!"
)
async def transphobia(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Transphobia or transmisia is set of deeply rooted negative beliefs about gender nonconforming people. "
        "It manifests as stigmatizing or denying the identities (including pronouns) of trans, nonbinary and "
        "otherwise gender nonconforming people. (Sources: Planned Parenthood, PFLAG)"
    )


# --- GENDER & SEXUALITY LOOKUPS ---

@bot.tree.command(name="gender", description="Look up an LGBTQ+ gender identity")
@app_commands.autocomplete(identity=gender_autocomplete)
async def gender_lookup(interaction: discord.Interaction, identity: str):
    term = identity.lower().strip()
    if term in GENDERS:
        data = GENDERS[term]
        embed = discord.Embed(
            title=f"✨ Gender Identity: {identity.title()}",
            description=data["definition"],
            color=data["color"],
        )
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(
            f"❌ `{identity}` not found in database.", ephemeral=True
        )


@bot.tree.command(
    name="sexuality", description="Look up an LGBTQ+ sexual or romantic orientation"
)
@app_commands.autocomplete(orientation=sexuality_autocomplete)
async def sexuality_lookup(interaction: discord.Interaction, orientation: str):
    term = orientation.lower().strip()
    if term in SEXUALITIES:
        data = SEXUALITIES[term]
        embed = discord.Embed(
            title=f"🌈 Sexuality Orientation: {orientation.title()}",
            description=data["definition"],
            color=data["color"],
        )
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(
            f"❌ `{orientation}` not found in database.", ephemeral=True
        )


# --- IDENTITY PROFILE SYSTEM ---

@bot.tree.command(
    name="profile", description="View your identity card or another user's card"
)
@app_commands.describe(user="The user whose profile you want to view")
async def view_profile(interaction: discord.Interaction, user: discord.User = None):
    target_user = user or interaction.user
    user_id = str(target_user.id)

    if user_id not in user_profiles:
        description = (
            f"This user hasn't set up their profile cards yet.\nUse `/profile_update` to get started!"
            if user
            else "You haven't set up your profile card yet!\nUse `/profile_update` to add your identities."
        )
        await interaction.response.send_message(
            description, ephemeral=True if not user else False
        )
        return

    profile = user_profiles[user_id]

    # Determine embed color from gender
    embed_color = 0x9B59B6
    saved_gender = profile.get("gender", "").lower()
    
    # Check if custom gender
    custom_name, custom_color = parse_custom_identity(saved_gender)
    if custom_name:
        embed_color = custom_color
        gender_display = custom_name.title()
    elif saved_gender in GENDERS:
        embed_color = GENDERS[saved_gender]["color"]
        gender_display = saved_gender.title()
    else:
        gender_display = "Not Set"

    # Handle sexuality display
    saved_sexuality = profile.get("sexuality", "").lower()
    custom_name, _ = parse_custom_identity(saved_sexuality)
    if custom_name:
        sexuality_display = custom_name.title()
    elif saved_sexuality in SEXUALITIES:
        sexuality_display = saved_sexuality.title()
    else:
        sexuality_display = "Not Set"

    embed = discord.Embed(
        title=f"📛 {target_user.display_name}'s Pride Card", color=embed_color
    )
    embed.set_thumbnail(url=target_user.display_avatar.url)
    embed.add_field(
        name="🗣️ Pronouns", value=profile.get("pronouns", "Not Set"), inline=False
    )
    embed.add_field(
        name="✨ Gender Identity",
        value=gender_display,
        inline=True,
    )
    embed.add_field(
        name="🌈 Orientation",
        value=sexuality_display,
        inline=True,
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(
    name="profile_update",
    description="Set up or edit your saved identities and pronouns",
)
@app_commands.describe(
    pronouns="Example: they/them, she/her",
    gender="Your gender identity",
    sexuality="Your sexual/romantic orientation",
)
@app_commands.autocomplete(
    gender=gender_autocomplete, sexuality=sexuality_autocomplete
)
async def update_profile(
    interaction: discord.Interaction,
    pronouns: str = None,
    gender: str = None,
    sexuality: str = None,
):
    user_id = str(interaction.user.id)

    if user_id not in user_profiles:
        user_profiles[user_id] = {
            "pronouns": "Not Set",
            "gender": "Not Set",
            "sexuality": "Not Set",
        }

    if pronouns:
        user_profiles[user_id]["pronouns"] = pronouns

    # Handle gender
    if gender:
        if gender == "__custom__":
            await interaction.response.send_modal(CustomIdentityModal("gender"))
            return
        else:
            user_profiles[user_id]["gender"] = gender.lower()

    # Handle sexuality
    if sexuality:
        if sexuality == "__custom__":
            await interaction.response.send_modal(CustomIdentityModal("sexuality"))
            return
        else:
            user_profiles[user_id]["sexuality"] = sexuality.lower()

    save_profiles()
    await interaction.response.send_message(
        "✅ Your identity profile card has been successfully updated!",
        ephemeral=True,
    )


# Start the bot
bot.run(DISCORD_BOT_TOKEN)
