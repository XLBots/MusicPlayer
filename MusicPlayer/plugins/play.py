# Copyright © 2023-2024 by piroxpower@Github, < https://github.com/piroxpower >.
#
# This file is part of < https://github.com/Team-Deadly/MusicUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Deadly/MusicUserbot/blob/main/LICENSE >
#
# All rights reserved ®.

import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from youtubesearchpython import VideosSearch

import time
from datetime import datetime
from pyrogram import filters
from .import userbot, command, MusicPlayer as Music
from ..core.queue import QUEUE, add_queue, get_queue
from ..core.Youtube import *


@userbot.on_message(command("play")) 
async def play(client, m: Message):
    replied = m.reply_to_message
    chat_id = m.chat.id
    m.chat.title
    if replied:
        if replied.audio or replied.voice:
            await m.delete()
            huehue = await replied.reply("**✧ Processing...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:35] + "..."
                else:
                    songname = replied.audio.file_name[:35] + "..."
                duration = convert_seconds(replied.audio.duration)
            elif replied.voice:
                songname = "Voice Note"
                duration = convert_seconds(replied.voice.duration)
            if chat_id in QUEUE:
                pos = add_queue(chat_id, songname, dl, link, "Audio", 0)
                await huehue.delete()
                await m.reply_to_message.delete()
                await m.reply_text(f"*➕ {songname} Added To Queue At {pos} On Request of {m.from_user.mention}*")
            else:
                await Music.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                    ),
                    stream_type=StreamType().pulse_stream,
                )
                add_queue(chat_id, songname, dl, link, "Audio", 0)
                await huehue.delete()
                await m.reply_to_message.delete()
                await m.reply_text(f"▶ Now Playing {songname} On Request Of {m.from_user.mention}")

    else:
        if len(m.command) < 2:
            await m.reply("Reply to Audio Files or give something to play")
        else:
            await m.delete()
            huehue = await m.reply("**✧ Searching!**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await huehue.edit("**Failed To Process Query!**")
            else:
                songname = search[0]
                url = search[1]
                duration = search[2]
                hm, ytlink = await ytdl(url)
                if hm == 0:
                    await huehue.edit(f"**YouTube Failed To Process Query!**")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await huehue.delete()
                        await m.reply_to_message.delete()
                        await m.reply_text(f"*➕ {songname} Added To Queue At {pos} On Request of {m.from_user.mention}*") 
                    else:
                        try:
                            await Music.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                ),
                                stream_type=StreamType().pulse_stream,
                            )
                            add_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await huehue.delete()
                            await m.reply_to_message.delete()
                            await m.reply_text(f"▶ Now Playing {songname} On Request Of {m.from_user.mention} ✨")
                        except Exception as ep:
                            await huehue.edit(f"`{ep}`")



