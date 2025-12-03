# Quick Start Guide

## 🚀 Fast Setup (3 Steps)

### Step 1: Install Dependencies

**Windows:**
```bash
setup.bat
```

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

### Step 2: Add Your Model

Copy your trained `model.pt` file to the `models/` folder:
```bash
copy path\to\your\model.pt models\model.pt
```

Or the system will auto-download YOLOv8s on first run.

### Step 3: Run the Application

**Windows:**
```bash
start.bat
```

**Linux/Mac:**
```bash
chmod +x start.sh
./start.sh
```

## 📹 Using the App

1. **Upload File** - Click "Select Video" or "Select Image" or drag & drop
2. **Start Detection** - Click the "🚀 Start Detection" button
3. **Monitor Progress** - Watch real-time detection with live preview
4. **Download Results** - Get your processed video/image with bounding boxes showing Soldier/Civilian classification

## 🧪 Test the System

```bash
# Test if everything is working
python tests/test_detection.py
```

## ⚙️ Manual Setup (Alternative)

**Terminal 1 - Backend:**
```bash
python backend/server.py
```

**Terminal 2 - Frontend:**
```bash
npm start
```

## ❓ Common Issues

**Problem:** `Python not found`
- Install Python 3.8-3.11 from python.org

**Problem:** `Module not found`
- Run: `pip install -r requirements.txt`

**Problem:** `Server offline`
- Make sure Python backend is running
- Check: http://localhost:5000/api/health

**Problem:** `Model not loaded`
- Place model.pt in models/ folder
- Check models/README.md for instructions

## 📊 System Requirements

**Minimum:**
- 8GB RAM
- 4-core CPU
- 10GB disk space

**Recommended:**
- 16GB RAM
- NVIDIA GPU (RTX 3060+)
- 20GB disk space

## 🎯 Next Steps

1. Upload a test video (drone footage)
2. Review detection results
3. Adjust confidence threshold if needed
4. Export and share your results!

---

For detailed documentation, see [README.md](README.md)
