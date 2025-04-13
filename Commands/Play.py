from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from helpers.decorators import sudo_only
from helpers.video import play_video, pause_stream, resume_stream, stop_stream

def register_handlers(app: Client):
    @app.on_message(filters.command("play") & filters.reply)
    @sudo_only
    async def play_command(client: Client, message: Message):
        replied = message.reply_to_message
        if replied.video or replied.audio:
            chat_id = message.chat.id
            await message.reply("Joining video chat...")
            await play_video(client, chat_id, replied)
        else:
            await message.reply("Please reply to a video or audio file with /play")

    @app.on_message(filters.command("pause"))
    @sudo_only
    async def pause_command(client: Client, message: Message):
        chat_id = message.chat.id
        await pause_stream(client, chat_id)
        await message.reply("⏸️ Playback paused")

    @app.on_message(filters.command("resume"))
    @sudo_only
    async def resume_command(client: Client, message: Message):
        chat_id = message.chat.id
        await resume_stream(client, chat_id)
        await message.reply("▶️ Playback resumed")

    @app.on_message(filters.command("end"))
    @sudo_only
    async def end_command(client: Client, message: Message):
        chat_id = message.chat.id
        await stop_stream(client, chat_id)
        await message.reply("⏹️ Playback ended")
