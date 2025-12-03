# 🚀 Getting Started Checklist

Use this checklist to set up and run your Aerial Threat Detection System!

## ✅ Pre-Installation Checklist

- [ ] **Python 3.8-3.11 installed**
  ```bash
  python --version
  ```
  If not, download from: https://www.python.org/downloads/

- [ ] **Node.js v14+ installed**
  ```bash
  node --version
  ```
  If not, download from: https://nodejs.org/

- [ ] **Git installed** (for version control)
  ```bash
  git --version
  ```

## 📦 Installation Steps

### Step 1: Install Dependencies

- [ ] **Run setup script**
  ```bash
  # Windows
  setup.bat
  
  # Linux/Mac
  chmod +x setup.sh
  ./setup.sh
  ```

- [ ] **Verify Python packages installed**
  ```bash
  pip list | findstr torch
  pip list | findstr ultralytics
  pip list | findstr opencv
  pip list | findstr flask
  ```

- [ ] **Verify Node packages installed**
  ```bash
  npm list electron
  ```

### Step 2: Model Setup

- [ ] **Option A: Use your trained model**
  ```bash
  # Copy your model.pt to models/ folder
  copy path\to\your\model.pt models\model.pt
  ```

- [ ] **Option B: Auto-download YOLOv8**
  ```bash
  # Run model setup script
  python setup_model.py
  ```

- [ ] **Verify model exists**
  ```bash
  dir models\*.pt
  ```

### Step 3: Configuration (Optional)

- [ ] **Update class names** (if using custom model)
  - Edit: `backend/detect.py`
  - Update: `self.class_names` dictionary

- [ ] **Adjust confidence threshold**
  - Edit: `backend/detect.py`
  - Change: `conf_threshold=0.5` (line ~15)

- [ ] **Modify threat levels**
  - Edit: `backend/detect.py`
  - Update: `get_threat_level()` method

## 🎯 First Run

### Start the Application

- [ ] **Open TWO terminal windows**

- [ ] **Terminal 1: Start Python Backend**
  ```bash
  cd Aerial-Threat-Detection
  python backend/server.py
  ```
  Wait for: "Server starting on http://localhost:5000"

- [ ] **Terminal 2: Start Electron App**
  ```bash
  cd Aerial-Threat-Detection
  npm start
  ```
  Application window should open automatically

**OR use quick start:**
- [ ] **Windows:** Double-click `start.bat`
- [ ] **Linux/Mac:** Run `./start.sh`

### Verify Everything Works

- [ ] **Check server status**
  - Look for green "Server Online" indicator in app
  - Or visit: http://localhost:5000/api/health

- [ ] **Check model loaded**
  - Server status should show "Model: Loaded"
  - Check backend terminal for "Model loaded successfully!"

## 🎬 First Detection Test

### Upload and Process Video

- [ ] **Prepare test video**
  - Find any aerial footage (YouTube, sample videos, etc.)
  - Supported formats: MP4, AVI, MOV, MKV, WebM

- [ ] **Upload video**
  - Click "Select Video" or drag & drop
  - Verify file info appears

- [ ] **Configure processing**
  - Set frame skip: "Every 3rd Frame" (recommended)

- [ ] **Start detection**
  - Click "🚀 Start Detection"
  - Watch progress bar

- [ ] **Monitor results**
  - Check detection count updates
  - View threat level breakdown
  - Read activity log

- [ ] **Download results**
  - Click "⬇️ Download Processed Video"
  - Verify bounding boxes and labels

## 🧪 Testing

- [ ] **Run automated tests**
  ```bash
  python tests/test_detection.py
  ```
  All tests should pass ✓

- [ ] **Test with different videos**
  - [ ] Short video (<1 min)
  - [ ] Different resolution
  - [ ] Different format

- [ ] **Test frame skip options**
  - [ ] Every frame (slowest, most accurate)
  - [ ] Every 3rd frame (balanced)
  - [ ] Every 5th frame (fastest)

## 📊 Performance Check

- [ ] **Check processing speed**
  - Note: FPS in activity log
  - CPU: 5-8 FPS expected
  - GPU: 60+ FPS expected

- [ ] **Monitor resource usage**
  - [ ] RAM usage (<4GB normal)
  - [ ] CPU usage (varies)
  - [ ] GPU usage (if available)

- [ ] **Verify output quality**
  - [ ] Bounding boxes visible
  - [ ] Labels readable
  - [ ] Colors appropriate for threat level

## 📚 Documentation Review

- [ ] **Read QUICKSTART.md**
  - Fast reference guide

- [ ] **Skim README.md**
  - Comprehensive documentation
  - Troubleshooting section

- [ ] **Review PROJECT_REPORT.md**
  - Technical details
  - For presentations

- [ ] **Check DEPLOYMENT.md**
  - Deployment strategies
  - Presentation outline

## 🎯 Project Submission Prep

### For GitHub

- [ ] **Initialize git (if not done)**
  ```bash
  git init
  git add .
  git commit -m "Initial commit: AI-powered aerial threat detection"
  ```

- [ ] **Push to GitHub**
  ```bash
  git remote add origin https://github.com/reymartjohneva/Aerial-Threat-Detection.git
  git branch -M development
  git push -u origin development
  ```

- [ ] **Verify repository online**

### For Google Drive

- [ ] **Create distribution folder**
  - Copy application files
  - Include sample videos (input/output)
  - Add model.pt
  - Include documentation PDFs

- [ ] **Create shared link**

- [ ] **Test download and setup from Drive**

### For Presentation

- [ ] **Prepare slides**
  - Use DEPLOYMENT.md outline
  - Add screenshots from app
  - Include detection results

- [ ] **Prepare demo**
  - Test video ready
  - Application working
  - Results pre-generated (backup)

- [ ] **Practice presentation**
  - Technical explanation ready
  - Demo flow tested
  - Q&A preparation

## 🔧 Troubleshooting Checklist

### If Server Won't Start

- [ ] Check Python version (3.8-3.11)
- [ ] Reinstall requirements: `pip install -r requirements.txt`
- [ ] Check port 5000 not in use
- [ ] Review backend terminal for errors

### If Model Won't Load

- [ ] Verify model.pt exists in models/
- [ ] Check model file not corrupted
- [ ] Run: `python setup_model.py`
- [ ] Check backend logs for error details

### If Electron Won't Start

- [ ] Reinstall node modules: `npm install`
- [ ] Check Node.js version
- [ ] Clear npm cache: `npm cache clean --force`
- [ ] Check main.js for errors

### If Detection Fails

- [ ] Verify server is running
- [ ] Check video format supported
- [ ] Verify model loaded successfully
- [ ] Check activity log for errors
- [ ] Try smaller video file

## ✨ Optional Enhancements

- [ ] **Customize UI**
  - Modify styles.css
  - Update colors/fonts

- [ ] **Add custom classes**
  - Update detect.py class names
  - Retrain model with custom dataset

- [ ] **Optimize performance**
  - Enable GPU acceleration
  - Adjust frame skip
  - Use smaller model

- [ ] **Package application**
  - Install electron-builder
  - Create installer
  - Distribute to others

## 📝 Final Checklist Before Submission

- [ ] **Application works end-to-end**
  - Upload → Process → Download ✓

- [ ] **Documentation complete**
  - README.md ✓
  - PROJECT_REPORT.md ✓
  - Comments in code ✓

- [ ] **Sample results prepared**
  - Input video ✓
  - Output video with detections ✓
  - Screenshots ✓

- [ ] **Repository clean**
  - No unnecessary files
  - .gitignore configured
  - Good commit messages

- [ ] **Presentation ready**
  - Slides prepared ✓
  - Demo tested ✓
  - Backup plan ready ✓

---

## 🎉 You're Ready!

✅ All items checked? **Congratulations!**

Your Aerial Threat Detection System is:
- ✅ Fully functional
- ✅ Well documented
- ✅ Ready for submission
- ✅ Ready for presentation

**Next:** Start your presentation or submit your project!

**Questions?** Check the documentation files or open an issue on GitHub.

**Good luck! 🚀**
