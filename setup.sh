#!/bin/bash

echo "========================================"
echo "Aerial Threat Detection - Quick Start"
echo "========================================"
echo ""

echo "Step 1: Checking Python installation..."
python3 --version
if [ $? -ne 0 ]; then
    echo "ERROR: Python is not installed or not in PATH"
    echo "Please install Python 3.8-3.11"
    exit 1
fi

echo ""
echo "Step 2: Checking Node.js installation..."
node --version
if [ $? -ne 0 ]; then
    echo "ERROR: Node.js is not installed or not in PATH"
    echo "Please install Node.js from https://nodejs.org/"
    exit 1
fi

echo ""
echo "Step 3: Installing Python dependencies..."
pip3 install -r requirements.txt

echo ""
echo "Step 4: Installing Node.js dependencies..."
npm install

echo ""
echo "========================================"
echo "Installation Complete!"
echo "========================================"
echo ""
echo "To run the application:"
echo "1. In one terminal: python3 backend/server.py"
echo "2. In another terminal: npm start"
echo ""
echo "Or simply run: ./start.sh"
echo ""
