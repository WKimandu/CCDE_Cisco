@echo off
echo Running enhanced whisper transcription...

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

REM Create output directory if it doesn't exist
if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

REM Properly activate the conda environment
call %CONDA_PATH%\Scripts\activate.bat %CONDA_ENV%
if %ERRORLEVEL% NEQ 0 (
    echo Failed to activate conda environment %CONDA_ENV%
    echo Trying alternate activation method...
    call conda activate %CONDA_ENV%
)

REM Verify we're in the correct environment
echo Current Python: 
where python
echo.

REM Check if video file was provided
if "%1"=="" (
    echo No video specified, using default BRKDCN-3615.mp4
    set VIDEO=BRKDCN-3615.mp4
) else (
    set VIDEO=%1
)

REM Check if the video exists
if not exist %VIDEO% (
    echo Error: Video file %VIDEO% not found!
    exit /b 1
)

echo Transcribing %VIDEO% using whisper with enhanced options...

REM Enhanced whisper call with word timestamps and multiple output formats
REM Force CPU device to avoid CUDA errors and use absolute output dir path
%ENV_PATH%\python.exe -m whisper %VIDEO% --task transcribe --word_timestamps True --output_format all --output_dir "%CD%\%OUTPUT_DIR%" --device cpu --model large --language en --fp16 False

echo Transcription complete! Check the %OUTPUT_DIR% directory for results. 