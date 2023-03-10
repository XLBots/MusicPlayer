
import asyncio
import importlib
import sys

from pyrogram import idle

import config
from MusicPlayer import LOGGER, Userbot, MusicPlayer
from MusicPlayer.plugins import ALL_MODULES

loop = asyncio.get_event_loop_policy().get_event_loop()


async def init():
    if (
        not config.STRING_SESSION        
    ):
        LOGGER("MusicPlayer").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    await Userbot.start()
    for all_module in ALL_MODULES:
        importlib.import_module("MusicPlayer.plugins" + all_module)
    LOGGER("MusicPlayer.plugins").info(
        "Successfully Imported Modules "
    )
    await MusicPlayer.start()
    LOGGER("MusicPlayer").info("Music Userbot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("MusicPlayer").info("Stopping XL Music Userbot! GoodBye")
