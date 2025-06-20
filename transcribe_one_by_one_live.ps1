# PowerShell script to transcribe Cisco Live session videos one by one with live output
Write-Host "Transcribing Cisco Live session videos one by one (with live progress)..." -ForegroundColor Green

# Activate the conda environment
conda activate CCDE_Cisco

# Get all MP4 files in the current directory
$videoFiles = Get-ChildItem -Filter "*.mp4" | Select-Object -ExpandProperty Name

Write-Host "Found $($videoFiles.Count) video files to transcribe" -ForegroundColor Cyan

# Process each video file one by one
foreach ($video in $videoFiles) {
    Write-Host "Starting transcription of $video..." -ForegroundColor Yellow
    
    # Run the live_whisper.py script for this video 
    # This shows real-time progress during transcription
    python live_whisper.py $video --output_dir transcripts --model large
    
    Write-Host "Completed transcription of $video" -ForegroundColor Green
    Write-Host "-----------------------------------------------------" -ForegroundColor DarkGray
    
    # Ask if user wants to continue to the next video
    $continue = Read-Host -Prompt "Continue to the next video? (Y/N)"
    if ($continue -ne "Y" -and $continue -ne "y") {
        Write-Host "Transcription process paused. Run the script again to continue with remaining videos." -ForegroundColor Yellow
        break
    }
}

Write-Host "All requested transcriptions complete! Check the transcripts directory for results." -ForegroundColor Green
Read-Host -Prompt "Press Enter to exit" 