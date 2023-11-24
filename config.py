# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "Your Api Id"))
API_HASH = os.environ.get("API_HASH", "Your Api Hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6702361035:AAFVM-QGYWFG5tvnbKcRyqlBdDucW5Al_KU")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "").split(",") if i.strip()] 
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Db Name")
DATABASE_URL = os.getenv("DATABASE_URL", "Mongodb url") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "Owner Id")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Updates Channel User name Without @") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "False"
