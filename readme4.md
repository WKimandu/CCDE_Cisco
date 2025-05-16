# Cisco Live Session Transcription

This document explains how to use the Whisper transcription tools to convert Cisco Live session videos to text.

## Prerequisites

1. Make sure you have the necessary dependencies installed:
   ```
   pip install -r requirements.txt
   ```

2. The script requires OpenAI's Whisper, which will be installed automatically if not present.

## Transcription Instructions

### Using the Python Script

#### Transcribing a Single Video

To transcribe a specific video (e.g., BRKDCN-3615.mp4):

```bash
python whisper_transcribe.py --videos BRKDCN-3615.mp4 --output_dir transcripts
```

#### Transcribing Multiple Videos

To transcribe multiple specific videos:

```bash
python whisper_transcribe.py --videos BRKDCN-3615.mp4 DEVNET-2473.mp4 --output_dir transcripts
```

#### Transcribing All Videos

To transcribe all MP4 files in the current directory:

```bash
python whisper_transcribe.py --all --output_dir transcripts
```

#### Parallel Processing

To transcribe multiple videos in parallel (e.g., using 2 workers):

```bash
python whisper_transcribe.py --all --max_workers 2 --output_dir transcripts
```

### Using Whisper CLI Directly (Recommended)

For more control over the transcription process, you can use the Whisper CLI directly:

```bash
whisper --task transcribe --word_timestamps True --output_format tsv --output_dir ./transcripts --device cpu --model large --language en BRKDCN-3615.mp4
```

This command provides:
- Word-level timestamps (`--word_timestamps True`)
- TSV output format with timestamps (`--output_format tsv`)
- Uses the CPU for processing (`--device cpu`)
- Uses the large model for better accuracy (`--model large`)
- Specifies English language (`--language en`)

## Output Format

The script creates two files for each transcribed video:
1. **[video_name].txt** - Contains the full transcript text
2. **[video_name].tsv** - Contains timestamps for each segment

A `TRANSCRIPTS.md` index file is also created in the output directory, cataloging all available transcripts.

## Notes

- The Python script uses the "medium" model by default for a good balance of accuracy and speed
- The direct CLI command uses the "large" model for better accuracy
- Previously transcribed videos will be skipped if they already have both .txt and .tsv files
- Transcription can be memory and CPU intensive, especially for longer videos
- Use the CPU option if you encounter GPU memory issues 