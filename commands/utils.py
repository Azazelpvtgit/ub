from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from helpers.decorators import sudo_only

def register_handlers(app: Client):
    @app.on_message(filters.command("sudolist"))
    @sudo_only
    async def sudolist(client: Client, message: Message):
        sudo_list = "\n".join(str(user_id) for user_id in Config.SUDO_USERS)
        await message.reply(f"**Sudo Users List:**\n{sudo_list}")
