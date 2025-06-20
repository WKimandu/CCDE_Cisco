import os
import sys
import subprocess
import argparse
import time
from pathlib import Path


def check_ffmpeg():
    """Check if ffmpeg is installed."""
    try:
        subprocess.check_output(["ffmpeg", "-version"],
                                stderr=subprocess.STDOUT)
        print("✓ ffmpeg is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ ffmpeg not found in PATH")
        try:
            print("Attempting to install ffmpeg using conda...")
            subprocess.check_call(["conda", "install", "-y", "ffmpeg"])
            print("✓ ffmpeg installed successfully using conda")
            return True
        except:
            print("Could not install ffmpeg automatically.")
            print("Please install it manually and add it to your PATH.")
            return False


def run_with_live_output(video_path, output_dir="transcripts", model="large"):
    """Run the Whisper CLI command with live output."""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get the base name of the video file without extension
    video_name = os.path.basename(video_path).rsplit('.', 1)[0]

    # Output paths
    txt_output = os.path.join(output_dir, f"{video_name}.txt")
    tsv_output = os.path.join(output_dir, f"{video_name}.tsv")
    vtt_output = os.path.join(output_dir, f"{video_name}.vtt")

    print(f"\n{'='*80}")
    print(f"Starting transcription of {video_path}")
    print(f"Model: {model}")
    print(f"Output directory: {output_dir}")
    print(f"{'='*80}\n")

    # Build the Whisper command
    cmd = [
        "whisper",
        video_path,
        "--model", model,
        "--output_dir", output_dir,
        "--verbose", "True",
        "--task", "transcribe",
        "--language", "en",
        # Generate all formats (txt, vtt, srt, tsv, json)
        "--output_format", "all"
    ]

    print("Running command:", " ".join(cmd))
    print(f"\n{'='*80}")
    print("Transcription Progress (this may take a while):")
    print(f"{'='*80}\n")

    # Run the process with live output
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1
    )

    # Print output in real-time
    segment_count = 0
    for line in process.stdout:
        line = line.strip()
        print(line)

        # Count segments processed
        if "[segment]" in line:
            segment_count += 1
            print(f"Progress: {segment_count} segments processed")

    # Wait for the process to complete
    process.wait()

    # Check if the output files were created
    files_created = []
    for ext in ["txt", "vtt", "srt", "tsv", "json"]:
        file_path = os.path.join(output_dir, f"{video_name}.{ext}")
        if os.path.exists(file_path):
            files_created.append(file_path)

    print(f"\n{'='*80}")
    print(f"Transcription completed with exit code: {process.returncode}")
    print(f"{'='*80}\n")

    if files_created:
        print("Files created:")
        for file in files_created:
            print(f" - {file} ({os.path.getsize(file) / 1024:.2f} KB)")
    else:
        print("No output files were created. Check for errors above.")

    # If txt file wasn't created but tsv exists, convert tsv to txt
    if not os.path.exists(txt_output) and os.path.exists(tsv_output):
        print("\nGenerating text file from TSV data...")
        try:
            with open(tsv_output, 'r', encoding='utf-8') as tsv_file:
                lines = tsv_file.readlines()[1:]  # Skip header

            with open(txt_output, 'w', encoding='utf-8') as txt_file:
                for line in lines:
                    parts = line.split('\t')
                    if len(parts) >= 3:
                        txt_file.write(parts[2] + ' ')

            print(
                f"Created text file: {txt_output} ({os.path.getsize(txt_output) / 1024:.2f} KB)")
        except Exception as e:
            print(f"Error creating text file: {str(e)}")


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe videos using Whisper with live output")
    parser.add_argument("video", help="Path to the video file to transcribe")
    parser.add_argument("--output_dir", default="transcripts",
                        help="Output directory for transcripts")
    parser.add_argument("--model", default="large",
                        choices=["tiny", "base", "small", "medium", "large"],
                        help="Whisper model size to use")

    args = parser.parse_args()

    if not check_ffmpeg():
        print("Please install ffmpeg and add it to your PATH, then try again.")
        return

    # Get absolute path to the video
    video_path = os.path.abspath(args.video)

    if not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}")
        return

    run_with_live_output(video_path, args.output_dir, args.model)


if __name__ == "__main__":
    main()
