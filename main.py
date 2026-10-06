import yt_dlp
import os
import sys


# pyinstaller detection thingy
if getattr(sys, "frozen", False):
    # Running as an EXE
    base_path = os.path.dirname(sys.executable)
else:
    # normal python script
    base_path = os.path.dirname(os.path.abspath(__file__))


ffmpeg_path = os.path.join(base_path, "ffmpeg", "bin", "ffmpeg.exe")


if not os.path.exists(ffmpeg_path):
    print("ffmpeg not found :/")
    print("looking for:", ffmpeg_path)
    input("press enter to exit...")
    sys.exit(1)


url = input("enter url ")

options = {
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
    "ffmpeg_location": ffmpeg_path,
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])