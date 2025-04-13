from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
import os
from commands import (
    play,
    sudo,
    utils
)

# Create session directory if it doesn't exist
if not os.path.exists("sessions"):
    os.makedirs("sessions")

app = Client(
    Config.SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    workdir="sessions"  # Store session files in a dedicated directory
)

# Load sudo users from file at startup
if os.path.exists(Config.SUDO_USERS_FILE):
    with open(Config.SUDO_USERS_FILE, 'r') as f:
        Config.SUDO_USERS.update(int(line.strip()) for line in f if line.strip())

@app.on_message(filters.command("ping"))
async def ping(client: Client, message: Message):
    if message.from_user.id in Config.SUDO_USERS:
        await message.reply("Hello master! I'm alive and working fine.")

# Register command handlers
play.register_handlers(app)
sudo.register_handlers(app)
utils.register_handlers(app)

if __name__ == "__main__":
    app.run()
