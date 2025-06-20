import os
import subprocess
import argparse
from pathlib import Path
import concurrent.futures
import tqdm


def check_whisper_installed():
    """Check if Whisper is installed and install if not."""
    try:
        import whisper
        return True
    except ImportError:
        print("Whisper not found. Installing...")
        subprocess.check_call(["pip", "install", "openai-whisper"])
        return True


def get_video_files(directory="."):
    """Get all MP4 files in the specified directory."""
    video_files = []
    for file in Path(directory).glob("*.mp4"):
        video_files.append(str(file))
    return video_files


def transcribe_video(video_path, output_dir="transcripts"):
    """Transcribe a video file using Whisper."""
    import whisper

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get the base name of the video file without extension
    video_name = os.path.basename(video_path).rsplit('.', 1)[0]

    # Output paths
    txt_output = os.path.join(output_dir, f"{video_name}.txt")
    tsv_output = os.path.join(output_dir, f"{video_name}.tsv")

    # Check if the transcript already exists
    if os.path.exists(txt_output) and os.path.exists(tsv_output):
        print(f"Transcript for {video_name} already exists. Skipping...")
        return video_name

    print(f"Transcribing {video_name}...")

    # Load model
    # Options: tiny, base, small, medium, large
    model = whisper.load_model("medium")

    # Transcribe
    result = model.transcribe(video_path)

    # Save text transcript
    with open(txt_output, "w", encoding="utf-8") as f:
        f.write(result["text"])

    # Save timestamps (TSV format)
    with open(tsv_output, "w", encoding="utf-8") as f:
        f.write("start\tend\ttext\n")
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]
            f.write(f"{start}\t{end}\t{text}\n")

    print(f"Completed transcription of {video_name}")
    return video_name


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe MP4 videos using Whisper")
    parser.add_argument("--videos", nargs="+",
                        help="Specific video files to transcribe")
    parser.add_argument("--all", action="store_true",
                        help="Transcribe all MP4 files in the current directory")
    parser.add_argument("--output_dir", default="transcripts",
                        help="Output directory for transcripts")
    parser.add_argument("--max_workers", type=int, default=1,
                        help="Maximum number of parallel transcriptions")

    args = parser.parse_args()

    # Check if Whisper is installed
    if not check_whisper_installed():
        print("Failed to install Whisper. Exiting.")
        return

    videos_to_transcribe = []

    if args.videos:
        # Process specific videos
        for video in args.videos:
            if os.path.exists(video) and video.endswith(".mp4"):
                videos_to_transcribe.append(video)
            else:
                print(
                    f"Warning: {video} is not a valid MP4 file or does not exist")
    elif args.all:
        # Process all videos in the current directory
        videos_to_transcribe = get_video_files()
    else:
        print("Please specify videos to transcribe using --videos or --all")
        return

    if not videos_to_transcribe:
        print("No valid videos to transcribe.")
        return

    print(f"Found {len(videos_to_transcribe)} videos to transcribe")

    # Create a progress bar
    with tqdm.tqdm(total=len(videos_to_transcribe)) as pbar:
        # Use ThreadPoolExecutor for parallel processing if requested
        if args.max_workers > 1:
            with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as executor:
                futures = []
                for video in videos_to_transcribe:
                    future = executor.submit(
                        transcribe_video, video, args.output_dir)
                    futures.append(future)

                for future in concurrent.futures.as_completed(futures):
                    video_name = future.result()
                    pbar.update(1)
        else:
            # Process sequentially
            for video in videos_to_transcribe:
                transcribe_video(video, args.output_dir)
                pbar.update(1)

    print("Transcription complete!")

    # Generate Markdown index of transcripts
    generate_transcript_index(args.output_dir)


def generate_transcript_index(output_dir="transcripts"):
    """Generate a Markdown index of all transcripts."""
    index_path = os.path.join(output_dir, "TRANSCRIPTS.md")

    # Get all transcript files
    txt_files = sorted(Path(output_dir).glob("*.txt"))

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("# Cisco Live Session Transcripts\n\n")
        f.write("This document catalogs all transcribed Cisco Live sessions.\n\n")
        f.write("| Session ID | Transcript | Timestamps |\n")
        f.write("|------------|------------|------------|\n")

        for txt_file in txt_files:
            session_id = txt_file.stem
            tsv_file = txt_file.with_suffix(".tsv")

            if tsv_file.exists():
                f.write(
                    f"| {session_id} | [{session_id}.txt]({session_id}.txt) | [{session_id}.tsv]({session_id}.tsv) |\n")

    print(f"Generated transcript index at {index_path}")


if __name__ == "__main__":
    main()
