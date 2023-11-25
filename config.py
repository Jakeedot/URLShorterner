# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "23959532"))
API_HASH = os.environ.get("API_HASH", "cb371d8744f6f852dd4b9c43e01349f9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6932675345:AAGro8kHiSn6GNCvmnO_aUHhr9NwQUGMDgE")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "").split(",") if i.strip()] 
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Hs534415:<H79090@kumar>@cluster0.nagkto0.mongodb.net/") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "-1001906223425"))
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1993185966"))
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "layersyetem") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "False"
