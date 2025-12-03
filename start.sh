#!/bin/bash

echo "========================================"
echo "Starting Aerial Threat Detection System"
echo "========================================"
echo ""

echo "Starting Python Backend Server..."
python3 backend/server.py &
BACKEND_PID=$!

sleep 3

echo ""
echo "Starting Electron Application..."
npm start &
ELECTRON_PID=$!

echo ""
echo "========================================"
echo "Both services are running"
echo "========================================"
echo ""
echo "Python Backend PID: $BACKEND_PID"
echo "Electron App PID: $ELECTRON_PID"
echo ""
echo "Press Ctrl+C to stop both services"
echo ""

# Wait for user interrupt
trap "kill $BACKEND_PID $ELECTRON_PID; exit" INT
wait
