# Importing libraries and modules
import os # Allows interaction with the operating system
import discord # Provides methods to interact with the Discord API
from discord.ext import commands # Extends discord.py and allows creation and handling of commands
from discord import app_commands # Allows parameters to be used for slash-commands
from dotenv import load_dotenv # Allows the use of environment variables (this is what we'll use to manage our
                               # tokens and keys)

# Environment variables for tokens and other sensitive data
load_dotenv() # Loads and reads the .env file
TOKEN = os.getenv("DISCORD_TOKEN") # Reads and stores the Discord Token from the .env file

# Setup of intents. Intents are permissions the bot has on the server
intents = discord.Intents.default() # Intents can be set through this object
intents.message_content = True  # This intent allows you to read and handle messages from users

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents) # Creates a bot and uses the intents created earlier

# Bot ready-up code
@bot.event # Decorator
async def on_ready():
    await bot.tree.sync() # Syncs the commands with Discord so that they can be displayed
    print(f"{bot.user} is online!") # Appears when the bot comes online


# Run the bot
bot.run(TOKEN) # This code uses your bot's token to run the bot