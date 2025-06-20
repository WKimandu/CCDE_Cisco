@echo off
echo Checking video files and transcripts...

REM Set the output directory
set OUTPUT_DIR=transcripts

REM Ensure output directory exists
if not exist "%OUTPUT_DIR%" (
    echo Creating transcripts directory...
    mkdir "%OUTPUT_DIR%"
)

REM List all mp4 files
echo.
echo Available MP4 files:
echo -------------------
dir /b *.mp4

REM Check each MP4 file
echo.
echo Checking MP4 file details:
echo ------------------------
for %%f in (*.mp4) do (
    echo File: %%f
    echo Size: %%~zf bytes
    if exist "%OUTPUT_DIR%\%%~nf.txt" (
        echo - Transcript exists: %OUTPUT_DIR%\%%~nf.txt
        for %%t in ("%OUTPUT_DIR%\%%~nf.txt") do echo   Size: %%~zt bytes
    ) else (
        echo - No transcript found for this file
    )
    echo.
)

REM Check output directory contents
echo.
echo Transcript directory contents:
echo ----------------------------
dir /b "%OUTPUT_DIR%"

echo.
echo Check complete.
pause 