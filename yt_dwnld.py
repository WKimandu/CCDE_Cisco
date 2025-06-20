#!/usr/bin/env python3
import sys
from pytube import YouTube

def download_video(url, output_path="."):
try:
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
print(f"Downloading: {yt.title}")
stream.download(output_path=output_path)
print("Download complete!")
except Exception as e:
print("An error occurred:", e)

def main():
if len(sys.argv) < 2:
print("Usage: python download_video.py <YouTube URL> [output_path]")
sys.exit(1)
url = sys.argv[1]
# Use the provided output path if supplied, otherwise use the current directory
output_path = sys.argv[2] if len(sys.argv) > 2 else "."
download_video(url, output_path)

if name == 'main': main()