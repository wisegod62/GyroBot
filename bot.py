#!/usr/bin/env python3

import json
import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from pride_data import GENDERS, SEXUALITIES, PRONOUNS, QUEER_HISTORY, FLAGS


load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
PROFILE_FILE = "user_profiles.json"

# Load saved profiles on startup, or create an empty dictionary
if os.path.exists(PROFILE_FILE):
    with open(PROFILE_FILE, "r") as f:
        user_profiles = json.load(f)
else:
    user_profiles = {}

def save_profiles():
    """Helper to write profile data to the disk safely."""
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

# --- AUTOCOMPLETE HELPERS ---


async def gender_autocomplete(
    interaction: discord.Interaction, current: str
) -> list[app_commands.Choice[str]]:
    return [
        app_commands.Choice(name=g.title(), value=g)
        for g in GENDERS.keys()
        if current.lower() in g.lower()
    ][:25]


async def sexuality_autocomplete(
    interaction: discord.Interaction, current: str
) -> list[app_commands.Choice[str]]:
    return [
        app_commands.Choice(name=s.title(), value=s)
        for s in SEXUALITIES.keys()
        if current.lower() in s.lower()
    ][:25]

async def pronouns_autocomplete(
    interaction: discord.Interaction, current: str
) -> list[app_commands.Choice[str]]:
    return [
        app_commands.Choice(name=p.title(), value=p)
        for p in PRONOUNS.keys()
        if current.lower() in p.lower()
    ][:25]

async def queer_history_autocomplete(
    interaction: discord.Interaction, current: str
) -> list[app_commands.Choice[str]]:
    return [
        app_commands.Choice(name=q.title(), value=q)
        for q in QUEER_HISTORY.keys()
        if current.lower() in q.lower()
    ][:25]

from PIL import Image, ImageDraw
import io

async def flag_autocomplete(
    interaction: discord.Interaction, current: str
) -> list[app_commands.Choice[str]]:
    return [
        app_commands.Choice(name=f.title(), value=f)
        for f in FLAGS.keys()
        if current.lower() in f.lower()
    ][:25]

from PIL import Image, ImageDraw
import io



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


# --- LOOKUPS ---

@bot.tree.command(
    name="gender", description="Look up an LGBTQ+ gender identity"
)
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


@bot.tree.command(
    name="queer_history", description="Look up an LGBTQ+ historical figure"
)
@app_commands.autocomplete(queer_history=queer_history_autocomplete)
async def queer_history_lookup(interaction: discord.Interaction, queer_history: str):
    term = queer_history.strip()
    if term in QUEER_HISTORY:
        data = QUEER_HISTORY[term]
        embed = discord.Embed(
            title=f"🍎 Queer Historical Figure: {queer_history.title()}",
            description=data["definition"],
            color=data.get("color", 0x9B59B6),
        )
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(
            f"❌ `{queer_history}` not found in database.", ephemeral=True
        )

@bot.tree.command(
    name="flag",
    description="Look up a pride flag"
)
@app_commands.autocomplete(flag=flag_autocomplete)
async def flag_lookup(interaction: discord.Interaction, flag: str):
    term = flag.lower().strip()

    if term not in FLAGS:
        await interaction.response.send_message(
            f"❌ `{flag}` not found in database.",
            ephemeral=True
        )
        return

    data = FLAGS[term]

    # Generate image
    image_buffer = generate_flag(data["colors"])
    file = discord.File(image_buffer, filename="flag.png")

    # Build embed
    embed = discord.Embed(
        title=f"🏳️ {flag.title()} Flag",
        description=data.get("description", "No description available."),
        color=0x9B59B6
    )

    embed.set_image(url="attachment://flag.png")

    await interaction.response.send_message(
        embed=embed,
        file=file
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
    
    saved_gender = profile.get("gender", "").lower()

    if "card_color" in profile:
        embed_color = profile["card_color"]
    elif saved_gender in GENDERS:
        embed_color = GENDERS[saved_gender]["color"]
    else:
        embed_color = 0x9B59B6
    
    embed = discord.Embed(
        title=f"📛 {target_user.display_name}'s Pride Card", color=embed_color
    )
    embed.set_thumbnail(url=target_user.display_avatar.url)
    embed.add_field(
        name="🗣️ Pronouns", value=profile.get("pronouns", "Not Set"), inline=False
    )
    embed.add_field(
        name="✨ Gender Identity",
        value=profile.get("gender", "Not Set").title(),
        inline=True,
    )
    embed.add_field(
        name="🌈 Orientation",
        value=profile.get("sexuality", "Not Set").title(),
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
    color="Hex color, e.g. #FF69B4",
)
@app_commands.autocomplete(
    gender=gender_autocomplete,
    sexuality=sexuality_autocomplete,
    pronouns=pronouns_autocomplete
)
async def update_profile(
    interaction: discord.Interaction,
    pronouns: str = None,
    gender: str = None,
    sexuality: str = None,
    color: str = None,
):
    user_id = str(interaction.user.id)

    if user_id not in user_profiles:
        user_profiles[user_id] = {
            "username": interaction.user.name,
            "pronouns": "Not Set",
            "gender": "Not Set",
            "sexuality": "Not Set",
            "card_color": 0x9B59B6,
        }

    user_profiles[user_id]["username"] = interaction.user.name

    if pronouns:
        user_profiles[user_id]["pronouns"] = pronouns

    if gender:
        user_profiles[user_id]["gender"] = gender.lower()

    if sexuality:
        user_profiles[user_id]["sexuality"] = sexuality.lower()

    if color:
        try:
            user_profiles[user_id]["card_color"] = int(
                color.replace("#", ""), 16
            )
        except ValueError:
            await interaction.response.send_message(
                "Invalid color. Use a hex code like #FF69B4.",
                ephemeral=True,
            )
            return

    save_profiles()

    await interaction.response.send_message(
        "✅ Your identity profile card has been successfully updated!",
        ephemeral=True,
    )

# Start the bot
bot.run(DISCORD_BOT_TOKEN)

