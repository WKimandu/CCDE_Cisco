@echo off
echo Transcribing Cisco Live session videos...

REM Activate the conda environment
call conda activate CCDE_Cisco

REM Run the whisper transcription script
python whisper_transcribe.py --videos BRKDCN-3615.mp4 --output_dir transcripts

echo Transcription complete! Check the transcripts directory for results.
pause 