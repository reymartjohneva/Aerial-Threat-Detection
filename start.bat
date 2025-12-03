@echo off
echo ========================================
echo Starting Aerial Threat Detection System
echo ========================================
echo.

echo Starting Python Backend Server...
start "Python Backend" cmd /k "python backend\server.py"

timeout /t 3 /nobreak >nul

echo.
echo Starting Electron Application...
start "Electron App" cmd /k "npm start"

echo.
echo ========================================
echo Both services are starting...
echo ========================================
echo.
echo Python Backend: http://localhost:5000
echo Electron App: Will open automatically
echo.
echo Press any key to close this window...
pause >nul
