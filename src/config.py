import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv(
	"DISCORD_BOT_TOKEN"
)

DATABASE_URL = "sqlite:///GyroBot.db"
