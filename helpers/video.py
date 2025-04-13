import os
import subprocess
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import JoinGroupCall
from pyrogram.raw.types import InputPhoneCall
from pyrogram.raw.types import DataJSON

# For Pyrogram v2.x+ (new import locations)
try:
    from pyrogram.types import AudioParameters, VideoParameters
    from pyrogram.types import InputAudioStream, InputVideoStream
except ImportError:
    # Fallback for older versions
    from pyrogram.types import (
        AudioParameters,
        VideoParameters,
        InputAudioStream,
        InputVideoStream
    )

async def play_telegram_video(client: Client, message: Message):
    try:
        # 1. Check if replied to a video
        if not message.reply_to_message or not message.reply_to_message.video:
            await message.reply("❌ Please reply to a video with /play")
            return

        # 2. Download the video
        await message.reply("⬇️ Downloading video...")
        video_path = await message.reply_to_message.download()
        
        # 3. Convert streams
        raw_audio = "stream_audio.raw"
        subprocess.run([
            'ffmpeg', '-i', video_path,
            '-f', 's16le', '-ac', '2', '-ar', '48000', 
            '-acodec', 'pcm_s16le', raw_audio
        ], check=True)

        # 4. Join and stream
        chat = await client.get_chat(message.chat.id)
        
        await client.start_group_call(
            chat.id,
            InputAudioStream(
                raw_audio,
                parameters=AudioParameters(
                    bitrate=48000,
                )
            )
        )
        
        await message.reply("▶️ Now playing in voice chat!")
        
    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")
    finally:
        # Cleanup
        for f in [video_path, raw_audio]:
            if os.path.exists(f):
                os.remove(f)
