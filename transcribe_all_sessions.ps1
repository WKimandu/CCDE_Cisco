# PowerShell script to transcribe all Cisco Live session videos
Write-Host "Transcribing all Cisco Live session videos..." -ForegroundColor Green

# Activate the conda environment
conda activate CCDE_Cisco

# Run the whisper transcription script for all videos
Write-Host "Starting transcription of all MP4 files..." -ForegroundColor Cyan
python whisper_transcribe.py --all --output_dir transcripts

Write-Host "Transcription complete! Check the transcripts directory for results." -ForegroundColor Green
Read-Host -Prompt "Press Enter to exit" 