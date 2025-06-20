#!/usr/bin/env python3
import sys
import os
from yt_dlp import YoutubeDL


def download_video(url, output_path="C:\\Users\\kiman\\Documents\\GitHub\\YoutubeTranscribe"):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save with title
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',  # Merge audio and video into mp4
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {url}")
            ydl.download([url])
            print("Download complete!")
            return True
    except Exception as e:
        print("An error occurred while downloading:")
        print(e)
        return False


def download_from_file(file_path, output_path="C:\\Users\\kiman\\Documents\\GitHub\\YoutubeTranscribe"):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]

    total_urls = len(urls)
    successful = 0

    print(f"Found {total_urls} URLs in the file.")

    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{total_urls}] Processing URL: {url}")
        if download_video(url, output_path):
            successful += 1

    print(
        f"\nDownload summary: {successful} of {total_urls} videos downloaded successfully.")


def main():
    if len(sys.argv) > 1:
        # If file path is provided as an argument
        file_path = sys.argv[1]
        download_from_file(file_path)
    else:
        # Ask for URL or file
        choice = input(
            "Enter '1' to download a single video or '2' to download from a file: ")

        if choice == '1':
            url = input("Enter YouTube URL: ")
            download_video(url)
        elif choice == '2':
            file_path = input(
                "Enter path to file containing URLs (default: youtube_urls.txt): ") or "youtube_urls.txt"
            download_from_file(file_path)
        else:
            print("Invalid choice. Exiting.")


if __name__ == '__main__':
    main()
