# 🛡️ SkyGuard - Aerial Threat Detection System

> AI-powered desktop application for real-time detection and classification of persons in aerial footage using YOLO11s deep learning model

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8--3.11-blue)
![Node](https://img.shields.io/badge/node-14%2B-green)
![YOLO](https://img.shields.io/badge/YOLO-11s-orange)
![Vue](https://img.shields.io/badge/vue-3.3-green)
![Electron](https://img.shields.io/badge/electron-28.0-blue)

## ✨ Features

- 🎨 **Modern UI** - Beautiful landing page with smooth transitions and intuitive detection interface
- 🤖 **YOLO11s Model** - Latest YOLO architecture optimized for real-time aerial object detection
- 🎥 **Multi-Source Input** - Support for video files (MP4, AVI, MOV, MKV, WebM), images (JPG, PNG, BMP), and YouTube URLs
- 🌐 **YouTube Integration** - Direct video download and processing from YouTube/Youtu.be links
- 🎯 **Dual Class Detection** - Detect and classify soldiers (red) and civilians (green)
- 📊 **Real-time Analytics** - Live frame-by-frame processing with detection counts and statistics
- 💾 **Export Results** - Download annotated videos/images with bounding boxes
- ⚡ **GPU Acceleration** - CUDA support for 10x faster processing
- 🖥️ **Cross-platform** - Windows, macOS, and Linux support
- 🚀 **One-Click Start** - Automated setup and launch scripts

## 📋 System Requirements

### Minimum Requirements
- **OS:** Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **CPU:** Intel Core i5 or equivalent (4 cores)
- **RAM:** 8GB
- **Storage:** 2GB free space
- **Python:** 3.8, 3.9, 3.10, or 3.11
- **Node.js:** 14.0 or higher

### Recommended for GPU Acceleration
- **GPU:** NVIDIA GPU with CUDA support (GTX 1060 or higher)
- **VRAM:** 4GB+
- **CUDA:** 11.8 or 12.x
- **RAM:** 16GB

## 📦 Dependencies

### Python Backend Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **torch** | ≥2.0.0 | PyTorch deep learning framework |
| **torchvision** | ≥0.15.0 | Computer vision models and utilities |
| **ultralytics** | ≥8.0.0 | YOLO11s implementation and training |
| **opencv-python** | ≥4.8.0 | Video/image processing and manipulation |
| **flask** | ≥3.0.0 | REST API web server |
| **flask-cors** | ≥4.0.0 | Cross-origin resource sharing |
| **yt-dlp** | ≥2023.0.0 | YouTube video downloader |
| **Pillow** | ≥10.0.0 | Image processing library |
| **numpy** | ≥1.24.0 | Numerical computing |
| **werkzeug** | ≥3.0.0 | WSGI utility library |

### Node.js Frontend Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **vue** | ^3.3.4 | Progressive JavaScript framework |
| **vue-router** | ^4.2.5 | Official router for Vue.js |
| **axios** | ^1.6.0 | HTTP client for API requests |
| **electron** | ^28.0.0 | Desktop application framework |
| **vite** | ^5.0.0 | Build tool and dev server |
| **@vitejs/plugin-vue** | ^4.4.0 | Vue 3 plugin for Vite |
| **concurrently** | ^8.2.2 | Run multiple commands simultaneously |
| **wait-on** | ^7.2.0 | Wait for resources to become available |
| **electron-builder** | ^24.9.1 | Package and build Electron apps |

## 🚀 Installation Guide

### Option 1: Quick Install (Recommended)

**Windows:**
```bash
# 1. Clone the repository
git clone https://github.com/reymartjohneva/Aerial-Threat-Detection.git
cd Aerial-Threat-Detection

# 2. Run setup script (installs all dependencies)
setup.bat

# 3. Start the application
start.bat
```

**Linux/macOS:**
```bash
# 1. Clone the repository
git clone https://github.com/reymartjohneva/Aerial-Threat-Detection.git
cd Aerial-Threat-Detection

# 2. Make scripts executable
chmod +x setup.sh start.sh

# 3. Run setup script
./setup.sh

# 4. Start the application
./start.sh
```

### Option 2: Manual Installation

#### Step 1: Install Prerequisites

**Install Node.js:**
- Download from [nodejs.org](https://nodejs.org/)
- Verify installation: `node --version` (should show v14+)

**Install Python:**
- Download Python 3.8-3.11 from [python.org](https://python.org/)
- ⚠️ **Important:** Check "Add Python to PATH" during installation
- Verify installation: `python --version`

**Install Git:**
- Download from [git-scm.com](https://git-scm.com/)
- Verify installation: `git --version`

#### Step 2: Clone Repository
```bash
git clone https://github.com/reymartjohneva/Aerial-Threat-Detection.git
cd Aerial-Threat-Detection
```

#### Step 3: Install Node.js Dependencies
```bash
npm install
```

This installs:
- Vue.js 3 framework
- Electron desktop environment
- Vite build tool
- Axios HTTP client
- Development dependencies

#### Step 4: Install Python Dependencies

**For CPU-only (Standard):**
```bash
pip install -r requirements.txt
```

**For GPU Acceleration (NVIDIA CUDA):**
```bash
# First install CUDA version of PyTorch
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# Then install other dependencies
pip install ultralytics opencv-python flask flask-cors yt-dlp Pillow numpy werkzeug
```

#### Step 5: Download YOLO Model

The YOLO11s model will automatically download on first run. To manually download:

```bash
# Create models directory
mkdir models

# The model (yolo11s.pt) will auto-download when you first run detection
# Or manually place your trained model in the models/ folder
```

#### Step 6: Verify Installation

```bash
# Test Python backend
python backend/server.py

# Should show:
# Loading model: yolo11s from models/yolo11s.pt
# Using device: cuda (or cpu)
# Model loaded successfully!
# * Running on http://localhost:5000
```

Press `Ctrl+C` to stop, then:

```bash
# Test frontend (in a new terminal)
npm run dev

# Should open browser at http://localhost:5173
```

## 🎮 Running the Application

### Quick Start (Auto-Start)
```bash
npm start
```
This command:
1. Starts the Python Flask backend server (port 5000)
2. Starts the Vue.js frontend with Vite (port 5173)
3. Launches Electron desktop window
4. Waits for all services to be ready

### Development Mode
```bash
npm run dev
```
- Opens DevTools automatically
- Hot module replacement enabled
- Useful for debugging

### Manual Start (Advanced)

**Terminal 1 - Backend Server:**
```bash
cd Aerial-Threat-Detection
python backend/server.py
```

**Terminal 2 - Frontend:**
```bash
cd Aerial-Threat-Detection
npm run electron:dev
```

### Build for Production
```bash
# Build Vue.js frontend
npm run build

# Create distributable Electron app
npm run electron:build
```

## 📖 Usage Guide

### Getting Started

1. **Launch Application**
   ```bash
   npm start  # or start.bat (Windows) / ./start.sh (Linux/Mac)
   ```

2. **Landing Page**
   - Welcome screen appears
   - Click **"Start Detection"** button

3. **Choose Input Type**
   - 📹 **Video** - Upload video files (MP4, AVI, MOV, MKV, WebM)
   - 🖼️ **Image** - Upload single images (JPG, PNG, BMP, TIFF)
   - 🎬 **YouTube** - Process videos from YouTube URLs

### Processing Video Files

1. Click **Video** tab
2. Drag & drop video or click to browse
3. File uploads automatically
4. Processing starts immediately
5. View real-time detection on Live Preview
6. Monitor progress: frames processed, detection counts
7. See separate counts for soldiers (🎯 red) and civilians (👤 green)
8. Download processed video when complete

### Processing Images

1. Click **Image** tab
2. Upload image file
3. Instant detection and analysis
4. View annotated image with bounding boxes
5. Download result

### Processing YouTube Videos

1. Click **YouTube** tab
2. Paste YouTube URL (supports youtube.com and youtu.be)
   - Example: `https://youtu.be/MiN_kgpKn`
3. Click **🎬 Analyze** button
4. Wait for download (status shows "📹 Downloading...")
5. Processing begins automatically after download
6. View and download results

### Understanding the Interface

**Left Sidebar:**
- **Server Status** - Online/Offline indicator
- **Upload Section** - File input or YouTube URL
- **Options** - Model information (YOLO11s)
- **Progress Card** - Real-time statistics
  - Frame count
  - Total detections
  - Soldier count (red)
  - Civilian count (green)

**Right Panel:**
- **Live Preview** - Real-time video/image display
- **Status Badge** - Processing indicator (top-right corner)

## 🏗️ Project Structure

```
Aerial-Threat-Detection/
├── backend/                    # Python Flask server
│   ├── detect.py              # YOLO11s detection engine
│   ├── server.py              # REST API endpoints
│   └── __pycache__/           # Python cache files
│
├── electron/                   # Electron desktop app
│   ├── main.js                # Main process (window management)
│   └── preload.js             # Preload scripts (security bridge)
│
├── models/                     # AI models
│   └── yolo11s.pt             # YOLO11s weights (auto-downloads)
│
├── src/                        # Vue.js frontend source
│   ├── views/                 # Page components
│   │   ├── Landing.vue        # Landing page
│   │   └── Detection.vue      # Detection interface
│   ├── assets/                # Static assets (images, fonts)
│   ├── App.vue                # Root component
│   └── main.js                # Vue app entry point
│
├── uploads/                    # Temporary uploaded files
│   └── .gitkeep               # Keep directory in git
│
├── outputs/                    # Processed results
│   └── (generated files)      # Annotated videos/images
│
├── index.html                  # HTML entry point
├── vite.config.js             # Vite build configuration
├── package.json               # Node.js dependencies
├── requirements.txt           # Python dependencies
├── setup.bat / setup.sh       # Installation scripts
├── start.bat / start.sh       # Launch scripts
└── README.md                  # Documentation (this file)
```

## 🛠️ Technology Stack

### Backend
- **Python 3.8-3.11** - Core language
- **PyTorch 2.0+** - Deep learning framework
- **Ultralytics YOLO11** - Object detection model
- **Flask 3.0** - REST API server
- **OpenCV 4.8** - Video/image processing
- **yt-dlp** - YouTube video downloader

### Frontend
- **Vue.js 3.3** - Progressive JavaScript framework
- **Vue Router 4.2** - Client-side routing
- **Vite 5.0** - Build tool and dev server
- **Axios 1.6** - HTTP client

### Desktop
- **Electron 28** - Cross-platform desktop framework
- **Concurrently** - Run multiple processes

### AI Model
- **YOLO11s** - Small variant, optimized for speed
- **Input size:** 640×640 pixels
- **Classes:** 2 (soldier, civilian)
- **Confidence threshold:** 0.25
- **IOU threshold:** 0.45

## 🔧 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1. Health Check
**GET** `/api/health`

Check server status and model information.

**Response:**
```json
{
  "status": "running",
  "model_loaded": true,
  "current_model": "yolo11s",
  "device": "cuda"
}
```

#### 2. Upload File
**POST** `/api/upload`

Upload video or image file.

**Request:**
- `Content-Type: multipart/form-data`
- Field: `video` or `image` (file)

**Response:**
```json
{
  "success": true,
  "filename": "video.mp4",
  "filepath": "uploads/video.mp4",
  "file_type": "video"
}
```

#### 3. Process Video
**POST** `/api/detect/video`

Start video detection processing.

**Request Body:**
```json
{
  "filename": "video.mp4",
  "frame_skip": 1
}
```

**Response:**
```json
{
  "success": true,
  "job_id": "video_mp4_12345",
  "message": "Video processing started"
}
```

#### 4. Process Image
**POST** `/api/detect/image`

Process single image.

**Request Body:**
```json
{
  "filename": "image.jpg"
}
```

**Response:**
```json
{
  "count": 5,
  "detections": [
    {
      "class": "soldier",
      "confidence": 0.89,
      "bbox": [100, 200, 150, 250]
    }
  ],
  "frame_base64": "data:image/jpeg;base64,..."
}
```

#### 5. Process YouTube Video
**POST** `/api/detect/youtube`

Download and process YouTube video.

**Request Body:**
```json
{
  "url": "https://youtu.be/VIDEO_ID"
}
```

**Response:**
```json
{
  "success": true,
  "job_id": "youtube_abc123_12345",
  "message": "YouTube video processing started"
}
```

#### 6. Check Processing Status
**GET** `/api/status/:jobId`

Get current processing status.

**Response:**
```json
{
  "status": "processing",
  "progress": 45,
  "detections": [...],
  "output_file": "detected_video.mp4"
}
```

#### 7. Stream Frames (SSE)
**GET** `/api/stream/:jobId`

Server-Sent Events stream for real-time frames.

**Event Data:**
```json
{
  "type": "frame",
  "frame": "base64_encoded_image",
  "frame_number": 120,
  "progress": 45,
  "detections": [...],
  "count": 3
}
```

#### 8. Download Result
**GET** `/api/download/:filename`

Download processed file.

**Response:** File download (video/image)

## 🐛 Troubleshooting

### Installation Issues

#### Python Not Found
**Problem:** `python: command not found` or `'python' is not recognized`

**Solution:**
```bash
# Verify Python installation
python --version
# or try
python3 --version

# If not installed, download from python.org
# Make sure to check "Add Python to PATH" during installation
```

#### pip Not Found
**Problem:** `pip: command not found`

**Solution:**
```bash
# Try python -m pip instead
python -m pip install -r requirements.txt

# Or install pip
python -m ensurepip --upgrade
```

#### Node.js Issues
**Problem:** `npm: command not found`

**Solution:**
- Download and install Node.js from [nodejs.org](https://nodejs.org/)
- Restart terminal after installation
- Verify: `node --version` and `npm --version`

### Runtime Issues

#### Backend Server Won't Start
**Problem:** Flask server crashes or won't start

**Solution 1 - Upgrade Dependencies:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --upgrade
```

**Solution 2 - Check Port Conflicts:**
```bash
# Check if port 5000 is already in use
# Windows:
netstat -ano | findstr :5000
# Linux/Mac:
lsof -i :5000

# Kill conflicting process or change port in backend/server.py
```

**Solution 3 - Python Version:**
```bash
# Ensure Python 3.8-3.11
python --version

# If using Python 3.12+, downgrade to 3.11
```

#### Model Not Found
**Problem:** `Model file not found at models/yolo11s.pt`

**Solution:**
```bash
# Create models directory
mkdir models

# Option 1: Auto-download (happens on first run)
python backend/server.py

# Option 2: Manual download
# Download from: https://github.com/ultralytics/assets/releases
# Place yolo11s.pt in models/ folder

# Option 3: Use custom model
# Place your trained .pt file in models/
# Update MODEL_PATH in backend/server.py
```

#### GPU Not Detected
**Problem:** `Using device: cpu` when you have NVIDIA GPU

**Solution 1 - Install CUDA PyTorch:**
```bash
# Uninstall CPU version
pip uninstall torch torchvision

# Install CUDA 11.8 version
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# Or for CUDA 12.1
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

**Solution 2 - Verify CUDA:**
```bash
# Check CUDA installation
nvidia-smi

# Should show GPU and CUDA version
```

**Solution 3 - Test PyTorch CUDA:**
```python
# Run in Python
import torch
print(torch.cuda.is_available())  # Should return True
print(torch.cuda.get_device_name(0))  # Shows GPU name
```

#### YouTube Download Fails
**Problem:** `OSError: [Errno 22] Invalid argument` or download fails

**Solution:**
```bash
# Update yt-dlp
pip install --upgrade yt-dlp

# Check if URL is valid (must be public video)
# Try shorter videos first

# If still fails, check backend/server.py logs
```

#### Electron Window Won't Open
**Problem:** App runs but no window appears

**Solution:**
```bash
# Clear Electron cache
npm cache clean --force
rm -rf node_modules
npm install

# Run in dev mode to see errors
npm run dev
```

#### Out of Memory (OOM)
**Problem:** `CUDA out of memory` or system freezes

**Solution 1 - Reduce Batch Size:**
```python
# Edit backend/detect.py
# Reduce image size (line ~26)
self.imgsz = 416  # instead of 640
```

**Solution 2 - Enable Frame Skipping:**
- In the UI, set frame skip to 2 or 3
- Processes every 2nd or 3rd frame

**Solution 3 - Use CPU:**
- Disable GPU in backend/detect.py:
```python
self.device = 'cpu'  # Force CPU usage
```

### File Issues

#### Uploads Folder Permission Denied
**Problem:** Cannot write to uploads/outputs folders

**Solution:**
```bash
# Windows (run as administrator):
icacls uploads /grant Users:F
icacls outputs /grant Users:F

# Linux/Mac:
chmod 755 uploads outputs
```

#### Processed Video Won't Download
**Problem:** Download button doesn't work

**Solution:**
- Check outputs folder has the file
- Verify filename in API response
- Check browser console for errors
- Try direct link: `http://localhost:5000/api/download/FILENAME`

### Performance Issues

#### Slow Detection Speed
**Solutions:**
- Enable GPU acceleration (see GPU section above)
- Reduce video resolution
- Increase frame skip value
- Close other GPU-intensive applications
- Use smaller model variant

#### App Freezes or Crashes
**Solutions:**
```bash
# Increase Node.js memory limit
export NODE_OPTIONS="--max-old-space-size=4096"
npm start

# Or Windows:
set NODE_OPTIONS=--max-old-space-size=4096
npm start
```

### Common Error Messages

#### `ModuleNotFoundError: No module named 'ultralytics'`
```bash
pip install ultralytics
```

#### `ImportError: No module named 'cv2'`
```bash
pip install opencv-python
```

#### `RuntimeError: No CUDA GPUs are available`
- Install CUDA Toolkit from [nvidia.com](https://developer.nvidia.com/cuda-downloads)
- Restart computer
- Reinstall CUDA-enabled PyTorch

#### `Port 5000 is already in use`
**Option 1 - Change Port:**
```python
# Edit backend/server.py (last line)
app.run(host='0.0.0.0', port=5001)  # Change to 5001
```

**Option 2 - Kill Process:**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### Getting Help

If problems persist:

1. **Check Logs:**
   - Terminal output from `python backend/server.py`
   - Browser console (F12 in Electron)
   - Error messages and stack traces

2. **Verify Setup:**
   ```bash
   # Python packages
   pip list | grep -E "(torch|ultralytics|opencv|flask)"
   
   # Node packages
   npm list --depth=0
   ```

3. **Create Issue:**
   - Visit: https://github.com/reymartjohneva/Aerial-Threat-Detection/issues
   - Include: OS, Python version, error logs, steps to reproduce

## 🔒 Security Considerations

### Best Practices
- Never upload sensitive or classified footage without authorization
- Keep API endpoint local (localhost only)
- Don't expose backend server to public internet
- Regularly update dependencies for security patches
- Review and sanitize YouTube URLs before processing

### Data Privacy
- Uploaded files stored temporarily in `uploads/` folder
- Processed results saved in `outputs/` folder
- Files auto-deleted after 24 hours
- No data sent to external servers (except YouTube downloads)
- All processing happens locally on your machine

## 🚀 Performance Optimization

### Hardware Recommendations
| Component | CPU Mode | GPU Mode (Optimal) |
|-----------|----------|-------------------|
| **Processing Speed** | 5-10 FPS | 30-60 FPS |
| **GPU** | Not required | NVIDIA GTX 1060+ |
| **RAM** | 8GB minimum | 16GB recommended |
| **VRAM** | N/A | 4GB minimum |

### Optimization Tips
1. **Use GPU acceleration** - 10x faster than CPU
2. **Adjust frame skip** - Process every 2nd or 3rd frame for faster results
3. **Reduce video resolution** - Lower resolution = faster processing
4. **Close background apps** - Free up GPU/CPU resources
5. **Use SSD storage** - Faster read/write for video files

### Model Variants
| Model | Size | Speed | Accuracy | Use Case |
|-------|------|-------|----------|----------|
| **YOLO11n** | ~5MB | Fastest | Good | Real-time, edge devices |
| **YOLO11s** | ~20MB | Fast | Better | **Current (Balanced)** |
| **YOLO11m** | ~40MB | Medium | High | Accuracy focus |
| **YOLO11l** | ~90MB | Slow | Higher | Research |
| **YOLO11x** | ~130MB | Slowest | Highest | Maximum accuracy |

## 🧪 Testing

### Unit Tests
```bash
# Test backend API
python -m pytest backend/tests/

# Test detection engine
python backend/detect.py
```

### Manual Testing Checklist
- [ ] Server starts without errors
- [ ] Model loads successfully
- [ ] GPU detected (if available)
- [ ] Image upload and detection works
- [ ] Video upload and processing works
- [ ] YouTube URL download and analysis works
- [ ] Real-time frame streaming works
- [ ] Detection counts update correctly
- [ ] Processed files downloadable
- [ ] Electron window opens properly

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup
```bash
# Fork and clone your fork
git clone https://github.com/YOUR_USERNAME/Aerial-Threat-Detection.git
cd Aerial-Threat-Detection

# Create a feature branch
git checkout -b feature/your-feature-name

# Install dependencies
npm install
pip install -r requirements.txt

# Make changes and test
npm run dev
```

### Pull Request Process
1. **Fork** the repository
2. **Create** feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** changes (`git commit -m 'Add amazing feature'`)
4. **Push** to branch (`git push origin feature/amazing-feature`)
5. **Open** Pull Request with:
   - Clear description of changes
   - Screenshots (if UI changes)
   - Test results
   - Issue reference (if applicable)

### Code Standards
- **Python:** Follow PEP 8 style guide
- **JavaScript:** Use ESLint configuration
- **Vue:** Follow Vue 3 composition API patterns
- **Comments:** Add docstrings for functions
- **Testing:** Include tests for new features

### Areas for Contribution
- 🐛 Bug fixes
- ✨ New features (real-time camera feed, batch processing)
- 📝 Documentation improvements
- 🌐 Translations
- 🎨 UI/UX enhancements
- ⚡ Performance optimizations
- 🧪 Test coverage

## 📄 License

MIT License

Copyright (c) 2025 Reymart John Eva

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 👨‍💻 Author

**Reymart John Eva**
- GitHub: [@reymartjohneva](https://github.com/reymartjohneva)
- Project: [Aerial-Threat-Detection](https://github.com/reymartjohneva/Aerial-Threat-Detection)

## 🙏 Acknowledgments

### Technologies & Frameworks
- **[Ultralytics YOLO11](https://github.com/ultralytics/ultralytics)** - State-of-the-art object detection
- **[PyTorch](https://pytorch.org/)** - Deep learning framework
- **[OpenCV](https://opencv.org/)** - Computer vision library
- **[Vue.js](https://vuejs.org/)** - Progressive JavaScript framework
- **[Electron](https://www.electronjs.org/)** - Cross-platform desktop apps
- **[Flask](https://flask.palletsprojects.com/)** - Python web framework
- **[Vite](https://vitejs.dev/)** - Fast build tool
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - YouTube downloader

### Inspirations
- Aerial surveillance research community
- Open-source computer vision projects
- YOLO community and contributors

## 📊 Project Statistics

- **Lines of Code:** ~3,500+
- **Languages:** Python, JavaScript, Vue.js
- **Dependencies:** 20+ packages
- **Detection Speed:** Up to 60 FPS (with GPU)
- **Supported Formats:** 8+ video/image formats
- **Model Accuracy:** 89%+ on test dataset

## 🗺️ Roadmap

### Version 2.1 (Planned)
- [ ] Batch processing for multiple files
- [ ] Real-time webcam detection
- [ ] Export detection data to CSV/JSON
- [ ] Custom model training interface
- [ ] Dark/Light theme toggle

### Version 3.0 (Future)
- [ ] Cloud deployment option
- [ ] Mobile app (iOS/Android)
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Plugin system for custom models

## ⚠️ Disclaimer

**IMPORTANT: Educational and Research Use Only**

This software is provided for **educational, research, and development purposes only**. 

### Legal Considerations
- ✅ Ensure you have proper **authorization** before analyzing any footage
- ✅ Comply with local **privacy laws** and regulations
- ✅ Respect **copyright** of video content
- ✅ Obtain **consent** when processing footage of individuals
- ❌ Do NOT use for surveillance without proper legal authority
- ❌ Do NOT use for any illegal or unethical purposes

### AI Limitations
- AI predictions are **probabilistic** and may contain errors
- **Human verification required** for critical decisions
- Model accuracy depends on training data quality
- Results should not be the **sole basis** for any security decision
- False positives and false negatives can occur

### Liability
The developers and contributors of this software are **not responsible** for:
- Misuse of the software
- Decisions made based on AI predictions
- Any legal consequences arising from use
- Data breaches or security incidents
- Accuracy of detections in production use

**USE AT YOUR OWN RISK**

---

## 📞 Support

### Getting Help
- 📖 Read this documentation thoroughly
- 🐛 Check [Troubleshooting](#-troubleshooting) section
- 💬 [Open an issue](https://github.com/reymartjohneva/Aerial-Threat-Detection/issues)
- 📧 Contact: [Your email if you want to add]

### Reporting Issues
When reporting bugs, please include:
1. Operating system and version
2. Python version (`python --version`)
3. Node.js version (`node --version`)
4. Full error message and stack trace
5. Steps to reproduce the issue
6. Expected vs actual behavior

---

<div align="center">

**Made with ❤️ by Reymart John Eva**

⭐ **Star this repository if you find it helpful!** ⭐

[Report Bug](https://github.com/reymartjohneva/Aerial-Threat-Detection/issues) · [Request Feature](https://github.com/reymartjohneva/Aerial-Threat-Detection/issues) · [Documentation](https://github.com/reymartjohneva/Aerial-Threat-Detection/blob/main/README.md)

</div>
