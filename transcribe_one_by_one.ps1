# PowerShell script to transcribe Cisco Live session videos one by one
Write-Host "Transcribing Cisco Live session videos one by one..." -ForegroundColor Green

# Activate the conda environment
conda activate CCDE_Cisco

# Get all MP4 files in the current directory
$videoFiles = Get-ChildItem -Filter "*.mp4" | Select-Object -ExpandProperty Name

Write-Host "Found $($videoFiles.Count) video files to transcribe" -ForegroundColor Cyan

# Process each video file one by one
foreach ($video in $videoFiles) {
    Write-Host "Starting transcription of $video..." -ForegroundColor Yellow
    
    # Run the direct_whisper.py script for this video 
    # Using the large model for better accuracy
    python direct_whisper.py $video --output_dir transcripts --model large
    
    Write-Host "Completed transcription of $video" -ForegroundColor Green
    Write-Host "-----------------------------------------------------" -ForegroundColor DarkGray
}

Write-Host "All transcriptions complete! Check the transcripts directory for results." -ForegroundColor Green
Read-Host -Prompt "Press Enter to exit" 