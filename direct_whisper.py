import os
import sys
import subprocess
import argparse


def check_dependencies():
    """Check if ffmpeg is installed and whisper is available."""
    # Check for whisper
    try:
        import whisper
        print("✓ Whisper is installed")
    except ImportError:
        print("Installing Whisper...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "openai-whisper"])
        print("✓ Whisper installed successfully")

    # Check for ffmpeg
    try:
        subprocess.check_output(["ffmpeg", "-version"],
                                stderr=subprocess.STDOUT)
        print("✓ ffmpeg is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ ffmpeg not found in PATH")
        try:
            # Try to install ffmpeg using conda
            print("Attempting to install ffmpeg using conda...")
            subprocess.check_call(["conda", "install", "-y", "ffmpeg"])
            print("✓ ffmpeg installed successfully using conda")
            return True
        except:
            print("Could not install ffmpeg. Please install it manually:")
            print(
                "1. Download ffmpeg from https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip")
            print("2. Extract the zip file")
            print("3. Add the bin folder to your PATH")
            return False


def transcribe_video(video_path, output_dir="transcripts", model_size="large"):
    """Transcribe a video file using Whisper with word-level timestamps."""
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
        return

    print(f"Transcribing {video_name} using {model_size} model...")

    # Load model
    model = whisper.load_model(model_size)

    # Transcribe with word-level timestamps
    options = {
        "task": "transcribe",
        "language": "en",  # Set to English
        "word_timestamps": True  # Enable word-level timestamps
    }

    result = model.transcribe(video_path, **options)

    # Save text transcript
    with open(txt_output, "w", encoding="utf-8") as f:
        f.write(result["text"])

    # Save timestamps (TSV format)
    with open(tsv_output, "w", encoding="utf-8") as f:
        f.write("start\tend\ttext\n")

        # Write segments with timestamps
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]
            f.write(f"{start}\t{end}\t{text}\n")

        # If word-level timestamps are available, write those too
        if "words" in result:
            f.write("\n# Word-level timestamps\n")
            f.write("start\tend\tword\n")
            for segment in result["segments"]:
                if "words" in segment:
                    for word_data in segment["words"]:
                        start = word_data["start"]
                        end = word_data["end"]
                        word = word_data["word"]
                        f.write(f"{start}\t{end}\t{word}\n")

    print(f"Completed transcription of {video_name}")
    print(f"Text saved to: {txt_output}")
    print(f"Timestamps saved to: {tsv_output}")


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe videos using Whisper with word-level timestamps")
    parser.add_argument("video", help="Path to the video file to transcribe")
    parser.add_argument("--output_dir", default="transcripts",
                        help="Output directory for transcripts")
    parser.add_argument("--model", default="large", choices=["tiny", "base", "small", "medium", "large"],
                        help="Whisper model size to use")

    args = parser.parse_args()

    # Check for dependencies
    if not check_dependencies():
        print("Please install the required dependencies and try again.")
        return

    # Transcribe the video
    transcribe_video(args.video, args.output_dir, args.model)


if __name__ == "__main__":
    main()
