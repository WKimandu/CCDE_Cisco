# Video Transcription System

This folder contains transcripts of video content related to CCDE certification and Cisco ACI technologies. The transcription system uses Whisper to convert video/audio content to searchable text.

## Transcription Workflow

1. Videos are downloaded using `yt_dwnld.py` or collected from official sources
2. Audio is extracted from the videos
3. Whisper processes the audio and generates text transcripts
4. Transcripts are saved in the `transcripts/` directory with standardized naming

## How to Use the Transcription Scripts

### For a Single Video

```powershell
.\transcribe_session.ps1 -VideoPath "path\to\video.mp4"
```

### For All Videos in a Queue

1. Add video paths to `video_queue.txt`, one per line
2. Run the batch transcription script:

```powershell
.\transcribe_all_sessions.ps1
```

## Transcript Naming Convention

Transcripts follow this naming convention:
`[Original_Video_Name]_transcript.txt`

## File Structure

- `transcripts/`: Contains all generated transcripts
- `video_queue.txt`: List of videos pending transcription
- `transcription_log.txt`: Log of transcription activities
- `whisper_temp_output.txt`: Temporary output during processing

## Dependencies

- Python 3.8+
- Whisper
- ffmpeg (for audio extraction) 