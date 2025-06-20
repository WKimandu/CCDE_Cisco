# PowerShell script to show which videos still need to be transcribed
Write-Host "Checking which videos still need to be transcribed..." -ForegroundColor Green

# Get all MP4 files in the current directory
$videoFiles = Get-ChildItem -Filter "*.mp4" | Select-Object -ExpandProperty Name

# Get all transcript files
$transcriptFiles = Get-ChildItem -Path "transcripts" -Filter "*.txt" | 
                  Select-Object -ExpandProperty BaseName

Write-Host "`nFound $($videoFiles.Count) video files and $($transcriptFiles.Count) existing transcripts" -ForegroundColor Cyan

# Check which videos don't have transcripts yet
$pendingVideos = @()
$completedVideos = @()

foreach ($video in $videoFiles) {
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($video)
    
    if ($transcriptFiles -contains $baseName) {
        $completedVideos += $video
    } else {
        $pendingVideos += $video
    }
}

# Display results
Write-Host "`nCompleted Transcriptions ($($completedVideos.Count)):" -ForegroundColor Green
if ($completedVideos.Count -gt 0) {
    foreach ($video in $completedVideos) {
        Write-Host "  ✓ $video" -ForegroundColor DarkGreen
    }
} else {
    Write-Host "  No videos have been transcribed yet" -ForegroundColor DarkGray
}

Write-Host "`nPending Transcriptions ($($pendingVideos.Count)):" -ForegroundColor Yellow
if ($pendingVideos.Count -gt 0) {
    foreach ($video in $pendingVideos) {
        Write-Host "  ○ $video" -ForegroundColor DarkYellow
    }
    
    # Offer to transcribe pending videos
    Write-Host "`nWould you like to transcribe one of these videos now?" -ForegroundColor Cyan
    $transcribeNow = Read-Host -Prompt "Enter video number to transcribe (1-$($pendingVideos.Count)) or 'N' to cancel"
    
    if ($transcribeNow -match "^\d+$" -and [int]$transcribeNow -ge 1 -and [int]$transcribeNow -le $pendingVideos.Count) {
        $videoToTranscribe = $pendingVideos[[int]$transcribeNow-1]
        Write-Host "`nStarting transcription of $videoToTranscribe..." -ForegroundColor Yellow
        
        $transcribeMethod = Read-Host -Prompt "Use (1) direct_whisper or (2) live_whisper? Enter 1 or 2"
        
        if ($transcribeMethod -eq "1") {
            # Run direct_whisper.py
            python direct_whisper.py $videoToTranscribe --output_dir transcripts --model large
        } 
        elseif ($transcribeMethod -eq "2") {
            # Run live_whisper.py
            python live_whisper.py $videoToTranscribe --output_dir transcripts --model large
        }
        else {
            Write-Host "Invalid option. Exiting without transcribing." -ForegroundColor Red
        }
    }
    elseif ($transcribeNow -ne "N" -and $transcribeNow -ne "n") {
        Write-Host "Invalid option. No video will be transcribed." -ForegroundColor Red
    }
} else {
    Write-Host "  All videos have been transcribed!" -ForegroundColor Green
}

Write-Host "`nTo transcribe all pending videos at once, run:" -ForegroundColor Cyan
Write-Host "  .\transcribe_one_by_one.ps1" -ForegroundColor White
Write-Host "  or" -ForegroundColor Cyan
Write-Host "  .\transcribe_one_by_one_live.ps1" -ForegroundColor White

Read-Host -Prompt "`nPress Enter to exit" 