# PowerShell script to transcribe Cisco Live session videos
Write-Host "Transcribing Cisco Live session videos..." -ForegroundColor Green

# Activate the conda environment
conda activate CCDE_Cisco

# Run the whisper transcription script
Write-Host "Starting transcription of BRKDCN-2673.mp4..." -ForegroundColor Cyan
python whisper_transcribe.py --videos BRKDCN-2673.mp4 --output_dir transcripts

Write-Host "Transcription complete! Check the transcripts directory for results." -ForegroundColor Green
Read-Host -Prompt "Press Enter to exit" 
