@echo off
echo Testing whisper installation...

REM Set the correct environment paths
set CONDA_PATH=C:\ProgramData\anaconda3
set CONDA_ENV=CCDE_Cisco
set ENV_PATH=C:\Users\kiman\.conda\envs\CCDE_Cisco

echo Setting up environment path: %ENV_PATH%

REM Properly activate the conda environment
call %CONDA_PATH%\Scripts\activate.bat %CONDA_ENV%
if %ERRORLEVEL% NEQ 0 (
    echo Failed to activate conda environment %CONDA_ENV%
    echo Trying alternate activation method...
    call conda activate %CONDA_ENV%
)

REM Verify we're in the correct environment
echo Current Python Path: 
where python
echo.

REM Verify whisper is installed
echo Checking if whisper is installed:
%ENV_PATH%\python.exe -c "import whisper; print(f'Whisper is installed! Version: {whisper.__version__}')"
if %ERRORLEVEL% NEQ 0 (
    echo Whisper module not found or could not be imported.
    echo Attempting to install whisper...
    %ENV_PATH%\python.exe -m pip install openai-whisper
    echo Checking whisper installation again:
    %ENV_PATH%\python.exe -c "import whisper; print(f'Whisper is installed! Version: {whisper.__version__}')"
)

REM List available whisper help info
echo.
echo Checking whisper CLI functionality:
%ENV_PATH%\python.exe -m whisper --help

echo.
echo Test complete.
pause 