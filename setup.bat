@echo off
echo ========================================
echo Aerial Threat Detection - Quick Start
echo ========================================
echo.

echo Step 1: Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8-3.11 from https://www.python.org/
    pause
    exit /b 1
)

echo.
echo Step 2: Checking Node.js installation...
node --version
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

echo.
echo Step 3: Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Step 4: Installing Node.js dependencies...
call npm install

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo To run the application:
echo 1. In one terminal: python backend\server.py
echo 2. In another terminal: npm start
echo.
echo Or simply run: start.bat
echo.
pause
