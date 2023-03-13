import time
from datetime import datetime
from pyrogram import filters
from ..import userbot, command

@userbot.on_message(command("ping") & filter.group) 
async def _ping(_, message: Message):
    """Ping command for user id"""
    await message.delete() 
    start = time.time()
    semx = await message.reply_text("•••••")
    delta_ping = time.time() - start
    await semx.edit(f"**[MusicPlayer]**\n\n• **Ping**: `{delta_ping * 1000:.3f} ms`\n**• , disable_web_page_preview=True) 
