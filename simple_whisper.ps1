# Simple PowerShell script to call whisper directly
Write-Host "Running simple whisper transcription..." -ForegroundColor Green

# Activate the conda environment
conda activate CCDE_Cisco

# Get the video from command line or use default
param (
    [string]$video = "BRKDCN-3615.mp4"
)

# Check if the video exists
if (-not (Test-Path $video)) {
    Write-Host "Error: Video file $video not found!" -ForegroundColor Red
    exit 1
}

Write-Host "Transcribing $video using whisper CLI..." -ForegroundColor Yellow

# Direct call to whisper CLI
whisper $video --model large --output_dir transcripts --language en

Write-Host "Transcription complete! Check the transcripts directory for results." -ForegroundColor Green 