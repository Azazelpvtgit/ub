from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
import os

def register_handlers(app: Client):
    @app.on_message(filters.command("addsudo") & filters.user(Config.OWNER_ID))
    async def addsudo(client: Client, message: Message):
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        elif len(message.command) > 1:
            try:
                user_id = int(message.command[1])
            except ValueError:
                await message.reply("Invalid user ID format")
                return
        else:
            await message.reply("Reply to a user or provide user ID")
            return
        
        Config.SUDO_USERS.add(user_id)
        with open(Config.SUDO_USERS_FILE, 'a') as f:
            f.write(f"{user_id}\n")
        
        await message.reply(f"User {user_id} added to sudo list")

    @app.on_message(filters.command("rmsudo") & filters.user(Config.OWNER_ID))
    async def rmsudo(client: Client, message: Message):
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        elif len(message.command) > 1:
            try:
                user_id = int(message.command[1])
            except ValueError:
                await message.reply("Invalid user ID format")
                return
        else:
            await message.reply("Reply to a user or provide user ID")
            return
        
        if user_id in Config.SUDO_USERS:
            Config.SUDO_USERS.remove(user_id)
            # Rewrite the entire file to remove the user
            with open(Config.SUDO_USERS_FILE, 'w') as f:
                for uid in Config.SUDO_USERS:
                    f.write(f"{uid}\n")
            await message.reply(f"User {user_id} removed from sudo list")
        else:
            await message.reply("User is not in sudo list")
