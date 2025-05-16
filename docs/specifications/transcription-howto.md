# Video Transcription System: Comprehensive Guide

## Overview

This guide explains how to use the video transcription system built for the CCDE & Cisco ACI Knowledge Base. The system uses OpenAI's Whisper model to transcribe video content (such as Cisco Live sessions) into searchable text that can be integrated into the knowledge base.

## Prerequisites

- Conda environment `CCDE_Cisco` (configured per environment.yml)
- Python 3.10+
- OpenAI Whisper
- FFmpeg (for audio extraction)
- Videos in MP4 format

## Quick Start Guide

### Method 1: One-Click Processing (Recommended for Beginners)

```powershell
# For Windows PowerShell (process all videos in current directory)
.\transcribe_all_sessions.ps1

# For Windows Command Prompt
transcribe_all_sessions.bat
```

### Method 2: Process Individual Files

```powershell
# For a specific video file
.\transcribe_session.ps1
# Edit the script first to specify your video filename
```

### Method 3: One-by-One with Interactive Control

```powershell
# Process files one by one with confirmation between each
.\transcribe_one_by_one.ps1

# Process with live progress feedback
.\transcribe_one_by_one_live.ps1
```

## Detailed Usage Instructions

### Testing Your Setup

Before starting batch processing, test your Whisper installation:

```powershell
.\test_whisper.bat
```

This script will:
1. Verify conda environment activation
2. Check if Whisper is installed, installing it if necessary
3. Test basic Whisper functionality

### Queue-Based Processing

For processing multiple files in sequence:

1. Create or modify `video_queue.txt` with one video filename per line:
   ```
   BRKDCN-2673.mp4
   CISCOU-2041.mp4
   DEVLIT-1860.mp4
   ```

2. Run the queue processor:
   ```powershell
   .\whisper_queue.bat
   ```

3. Monitor progress:
   - Check `transcription_log.txt` for detailed logs
   - Temporary output is shown in the console
   - Final transcripts are saved in the `transcripts/` directory

### Using the Python Transcription API Directly

For advanced users who want more control:

```bash
# Transcribe a specific file with custom options
python whisper_transcribe.py --videos BRKDCN-3615.mp4 --output_dir transcripts

# Transcribe all MP4 files in the current directory
python whisper_transcribe.py --all --output_dir transcripts

# Parallel processing (be aware of memory usage)
python whisper_transcribe.py --all --output_dir transcripts --max_workers 2
```

## Understanding the Output

Each transcribed video produces several files:

- `[filename].txt`: Plain text transcript of the entire video
- `[filename].tsv`: Transcript with timestamps in tab-separated format
- `[filename].vtt` (optional): WebVTT format for subtitles
- `[filename].srt` (optional): SubRip format for subtitles

Additionally, a `TRANSCRIPTS.md` index file is automatically generated in the transcripts directory.

## Integration with the Knowledge Base

### Adding Transcripts to the Knowledge Base

1. Complete the transcription of your videos
2. Place the transcript files in the `data/transcripts/` directory
3. Run the document processing pipeline:

```bash
python src/processing/run_processor.py --input data/transcripts --is_directory --output data/processed_index --custom_entities config/custom_entities.json
```

### Querying Transcribed Content

Once processed, you can query the knowledge base including transcript content:

```python
from src.examples.process_example import main as run_example
run_example()  # This will run a test query against your knowledge base
```

## Troubleshooting

### Common Issues

1. **Conda Environment Activation Fails**
   ```
   Problem: "Failed to activate conda environment CCDE_Cisco"
   Solution: Ensure the environment exists and try manual activation:
   conda activate CCDE_Cisco
   ```

2. **CUDA/GPU Errors**
   ```
   Problem: CUDA out of memory or related GPU errors
   Solution: Force CPU usage by adding --device cpu to Whisper commands
   ```

3. **Interrupted Transcription**
   ```
   Problem: Transcription stops in the middle of a file
   Solution: Check transcription_log.txt for errors; the queue processor 
   will automatically skip already processed files
   ```

4. **Memory Issues with Large Videos**
   ```
   Problem: System runs out of memory with long videos
   Solution: Use a smaller Whisper model:
   python whisper_transcribe.py --videos long_video.mp4 --model small
   ```

### Model Size Options

Whisper provides multiple model sizes to balance accuracy vs. resource usage:

| Model  | Memory Required | Accuracy  | Speed     | Recommended For                                |
| ------ | --------------- | --------- | --------- | ---------------------------------------------- |
| tiny   | ~1GB            | Low       | Fast      | Quick tests, resource-constrained environments |
| base   | ~1GB            | Basic     | Fast      | Simple content, clear speech                   |
| small  | ~2GB            | Good      | Medium    | Most Cisco Live sessions                       |
| medium | ~5GB            | Very good | Slow      | Technical content, default choice              |
| large  | ~10GB           | Excellent | Very slow | Critical content, heavy accents                |

## Advanced Configurations

### Custom Processing Scripts

You can create custom processing configurations by editing the batch or PowerShell scripts. Key parameters to consider:

- `--task`: Set to "transcribe" for standard transcription or "translate" for translation to English
- `--language`: Specify source language (e.g., "en" for English)
- `--word_timestamps`: Set to True for word-level timestamps
- `--output_format`: Choose from "txt", "vtt", "srt", "tsv", "json", or "all"
- `--model`: Choose model size (tiny, base, small, medium, large)

### Batch Processing Best Practices

1. **Organize videos in topic-specific folders** before processing
2. **Start with a small test set** before processing large collections
3. **Check transcript quality** periodically during batch processing
4. **Use the medium model for technical content** like Cisco Live sessions
5. **Schedule long-running jobs** during off-hours due to processing time
6. **Back up transcripts** regularly to prevent data loss

## Performance Expectations

Based on the medium Whisper model running on CPU:

- 30-minute video: ~15-30 minutes to transcribe
- 60-minute video: ~30-60 minutes to transcribe
- Full-day session: May take several hours

GPU acceleration can significantly improve these times if available.

## Integration with Documentation Workflow

After transcription, consider these next steps:

1. **Extract key concepts** from transcripts using the NER processor
2. **Add technical terms** discovered in transcripts to `custom_entities.json`
3. **Create topic summaries** based on transcript content
4. **Cross-reference** transcripts with official documentation
5. **Index transcripts** by topic, technology area, and certification relevance

## Maintenance and Updates

- Check periodically for Whisper updates: `pip install openai-whisper --upgrade`
- Keep FFmpeg updated for optimal media processing
- Review and clean the transcripts directory periodically
- Update the transcript index (`TRANSCRIPTS.md`) when adding new content

## Additional Resources

- [Whisper GitHub Repository](https://github.com/openai/whisper)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- Full documentation for the knowledge base is available in the [PRD document](product-requirements.md)

## Appendix: Script Reference

| Script                           | Description                         | Usage                                 |
| -------------------------------- | ----------------------------------- | ------------------------------------- |
| `test_whisper.bat`               | Tests Whisper installation          | `.\test_whisper.bat`                  |
| `transcribe_session.ps1`         | Transcribes a single video          | `.\transcribe_session.ps1`            |
| `transcribe_all_sessions.ps1`    | Transcribes all videos in directory | `.\transcribe_all_sessions.ps1`       |
| `transcribe_one_by_one.ps1`      | Interactive transcription           | `.\transcribe_one_by_one.ps1`         |
| `transcribe_one_by_one_live.ps1` | Interactive with progress           | `.\transcribe_one_by_one_live.ps1`    |
| `whisper_queue.bat`              | Processes videos in queue file      | `.\whisper_queue.bat`                 |
| `whisper_transcribe.py`          | Python API for direct access        | `python whisper_transcribe.py --help` |