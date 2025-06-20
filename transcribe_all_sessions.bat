@echo off
echo Transcribing all Cisco Live session videos...

REM Activate the conda environment
call conda activate CCDE_Cisco

REM Run the whisper transcription script for all videos
python whisper_transcribe.py --all --output_dir transcripts

echo Transcription complete! Check the transcripts directory for results.
pause 