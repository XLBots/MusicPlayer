import os 
import logging
from pyrogram import Client
from pyrogram import filters

PREFIX = "."

# Command Handler
command = partial(filters.command, prefixes=PREFIX)

print("[xl] Starting Deployment!")

CHATS = []

OWNER_ID = config.OWNER_ID

print("[XL] Booting Clients 🎶")

Userbot = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
MusicPlayer = pytgcalls(Userbot) 

print("[XL] Processing To __main__.py") 
