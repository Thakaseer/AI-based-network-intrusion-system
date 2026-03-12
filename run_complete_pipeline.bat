@echo off
REM Complete AI-NIDS Execution Pipeline
REM Runs: Data Load -> Process -> Train -> Test -> Display Results

cd /d "%~dp0"

echo.
echo ============================================================
echo  AI Network Intrusion Detection System
echo  Complete Execution Pipeline
echo ============================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo [1/5] Checking dependencies...
pip show pandas >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
)
echo OK: Dependencies ready

echo.
echo [2/5] Executing complete pipeline...
echo This will take a few minutes...
echo.

python execute_pipeline.py
if errorlevel 1 (
    echo Error: Pipeline execution failed
    pause
    exit /b 1
)

echo.
echo [3/5] Pipeline completed successfully!
echo.

:menu
echo.
echo ============================================================
echo  What would you like to do next?
echo ============================================================
echo.
echo 1. View Results in Web Dashboard (Recommended)
echo 2. View Results in Console
echo 3. View Results File
echo 4. Exit
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Starting web server at http://localhost:5000
    echo Press Ctrl+C to stop
    echo.
    python detect.py --mode api
    goto menu
)

if "%choice%"=="2" (
    echo.
    echo Showing test results...
    echo.
    python detect.py --mode demo
    goto menu
)

if "%choice%"=="3" (
    echo.
    echo Opening results file...
    for /f "tokens=*" %%A in ('powershell -NoProfile -Command "Get-ChildItem logs\execution_results*.json -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1 -ExpandProperty FullName"') do (
        start notepad "%%A"
    )
    goto menu
)

if "%choice%"=="4" (
    echo Goodbye!
    exit /b 0
)

echo Invalid choice. Please try again.
goto menu
