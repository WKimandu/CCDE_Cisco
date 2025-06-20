@echo off
echo Transcribing Cisco Live session videos one by one with enhanced options...

REM Set the correct environment paths
set CONDA_PATH=C:\ProgramData\anaconda3
set CONDA_ENV=CCDE_Cisco
set ENV_PATH=C:\Users\kiman\.conda\envs\CCDE_Cisco

REM Set the correct output directory
set OUTPUT_DIR=transcripts
if exist "%OUTPUT_DIR%\%OUTPUT_DIR%" (
    echo Nested transcripts directory detected, using parent directory only...
    rmdir /s /q "%OUTPUT_DIR%\%OUTPUT_DIR%"
)

REM Enable delayed expansion for variables inside loops
setlocal enabledelayedexpansion

REM Set up logging
set LOG_FILE=transcription_log.txt
echo Transcription Log - Started at %date% %time% > %LOG_FILE%
echo ================================================== >> %LOG_FILE%

REM Properly activate the conda environment
call %CONDA_PATH%\Scripts\activate.bat %CONDA_ENV%
if %ERRORLEVEL% NEQ 0 (
    echo Failed to activate conda environment %CONDA_ENV%
    echo Failed to activate conda environment %CONDA_ENV% >> %LOG_FILE%
    echo Trying alternate activation method...
    echo Trying alternate activation method... >> %LOG_FILE%
    call conda activate %CONDA_ENV%
)

REM Verify we're in the correct environment
echo Current Python:
echo Current Python: >> %LOG_FILE%
where python
where python >> %LOG_FILE%
echo.
echo. >> %LOG_FILE%

REM Create a list of videos to transcribe
echo Scanning for MP4 files...
echo Scanning for MP4 files... >> %LOG_FILE%
dir /b *.mp4 > video_queue.txt

REM Count the videos
for /f %%a in ('type video_queue.txt ^| find /c /v ""') do set total=%%a
echo Found %total% videos to transcribe.
echo Found %total% videos to transcribe. >> %LOG_FILE%

REM Process each video
set current=0
for /f "tokens=*" %%a in (video_queue.txt) do (
    set /a current+=1
    echo.
    echo. >> %LOG_FILE%
    echo [!current!/%total%] Starting transcription of %%a...
    echo [!current!/%total%] Starting transcription of %%a... >> %LOG_FILE%
    echo Started at: %date% %time%
    echo Started at: %date% %time% >> %LOG_FILE%
    
    REM Check if transcript already exists
    set basename=%%~na
    if exist "%OUTPUT_DIR%\!basename!.txt" (
        echo Transcript for %%a already exists. Skipping...
        echo Transcript for %%a already exists. Skipping... >> %LOG_FILE%
    ) else (
        echo Processing %%a with enhanced options...
        echo Processing %%a with enhanced options... >> %LOG_FILE%
        
        REM Create output directory if it doesn't exist
        if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"
        
        REM Force CPU device to avoid CUDA errors and use absolute output dir path
        %ENV_PATH%\python.exe -m whisper "%%a" --task transcribe --word_timestamps True --output_format all --output_dir "%CD%\%OUTPUT_DIR%" --device cpu --model large --language en --fp16 False > whisper_temp_output.txt 2>&1
        type whisper_temp_output.txt
        type whisper_temp_output.txt >> %LOG_FILE%
        del whisper_temp_output.txt
        
        echo Completed transcription of %%a
        echo Completed transcription of %%a >> %LOG_FILE%
        echo Completed at: %date% %time%
        echo Completed at: %date% %time% >> %LOG_FILE%
        
        REM Check file sizes
        if exist "%OUTPUT_DIR%\!basename!.txt" (
            for %%f in ("%OUTPUT_DIR%\!basename!.txt") do set size=%%~zf
            echo TXT file size: !size! bytes
            echo TXT file size: !size! bytes >> %LOG_FILE%
        )
        if exist "%OUTPUT_DIR%\!basename!.vtt" (
            for %%f in ("%OUTPUT_DIR%\!basename!.vtt") do set size=%%~zf
            echo VTT file size: !size! bytes
            echo VTT file size: !size! bytes >> %LOG_FILE%
        )
        if exist "%OUTPUT_DIR%\!basename!.srt" (
            for %%f in ("%OUTPUT_DIR%\!basename!.srt") do set size=%%~zf
            echo SRT file size: !size! bytes
            echo SRT file size: !size! bytes >> %LOG_FILE%
        )
    )
    echo --------------------------------------------------
    echo -------------------------------------------------- >> %LOG_FILE%
)

REM Clean up
del video_queue.txt

echo All transcriptions complete! Check the transcripts directory for results.
echo All transcriptions complete! Check the transcripts directory for results. >> %LOG_FILE%
echo Transcription process finished at %date% %time%
echo Transcription process finished at %date% %time% >> %LOG_FILE%

endlocal
pause 