import os
import subprocess
from pyrogram import Client
from pyrogram.types import Message, InputAudioStream, InputVideoStream
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import JoinGroupCall

async def play_telegram_video(client: Client, message: Message):
    try:
        # 1. Check if replied to a video
        if not message.reply_to_message or not message.reply_to_message.video:
            await message.reply("❌ Please reply to a video with /play")
            return

        # 2. Download the video
        await message.reply("⬇️ Downloading video...")
        video_path = await message.reply_to_message.download()
        
        # 3. Convert for Telegram Voice Chat
        raw_audio = "stream_audio.raw"
        raw_video = "stream_video.raw"
        
        # Extract audio stream
        subprocess.run([
            'ffmpeg', '-i', video_path,
            '-f', 's16le', '-ac', '2', '-ar', '48000', '-acodec', 'pcm_s16le', raw_audio
        ], check=True)
        
        # Extract video stream (optional)
        subprocess.run([
            'ffmpeg', '-i', video_path,
            '-f', 'rawvideo', '-pix_fmt', 'yuv420p', '-vf', 'scale=640:360', raw_video
        ], check=True)

        # 4. Join and stream
        chat = await client.get_chat(message.chat.id)
        peer = await client.resolve_peer(chat.id)
        
        await client.send(
            JoinGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash
                ),
                muted=False,
                video_stopped=False
            )
        )
        
        # Start streaming (audio only for reliability)
        await client.start_group_call(
            message.chat.id,
            InputAudioStream(
                raw_audio,
                parameters=AudioParameters(
                    bitrate=48000,
                )
            )
            # Uncomment for video:
            # InputVideoStream(
            #     raw_video,
            #     parameters=VideoParameters(
            #         width=640,
            #         height=360,
            #         frame_rate=30
            #     )
            # )
        )
        
        await message.reply("▶️ Now playing video in VC!")
        
    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")
    finally:
        # Cleanup
        for f in [video_path, raw_audio, raw_video]:
            if os.path.exists(f):
                os.remove(f)
