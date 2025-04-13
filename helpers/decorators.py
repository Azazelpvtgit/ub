from pyrogram import filters
from pyrogram.types import Message
from config import Config
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid

def sudo_only(func):
    async def wrapper(client, message: Message):
        if message.from_user.id in Config.SUDO_USERS:
            await func(client, message)
        else:
            await message.reply("🚫 You are not authorized to use this command")
    return wrapper
