# Aerial Object Detection System

> AI-powered desktop application for detecting and classifying people and objects in aerial footage using YOLOv8

An intelligent computer vision system built with YOLOv8, PyTorch, Flask, and Electron that analyzes aerial imagery to identify and classify soldiers, civilians, and other objects with real-time processing and visual annotations.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Node](https://img.shields.io/badge/node-14%2B-green)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange)

## 🎯 Features

- 🤖 **YOLOv8 Object Detection** - State-of-the-art deep learning model for accurate object detection
- 🎥 **Video & Image Processing** - Supports MP4, AVI, MOV, MKV, WebM videos and JPG, PNG, BMP images
- 🎨 **Smart Visual Annotations** - Color-coded bounding boxes with semi-transparent labels
  - 🔴 **Soldiers** - Red boxes with circle indicators
  - 🟢 **Civilians** - Green boxes with square indicators
  - 🟡 **Other Objects** - Yellow/Orange boxes for vehicles, drones, etc.
- 📊 **Real-time Dashboard** - Live progress monitoring with detection statistics
- 👥 **Classification Analytics** - Automatic categorization and counting by object type
- 💾 **Export Results** - Download processed videos/images with all annotations
- ⚡ **GPU Acceleration** - CUDA support for 10x faster processing
- 🖥️ **Cross-platform** - Works on Windows, macOS, and Linux
- 🎛️ **Configurable Processing** - Adjustable frame skip and confidence thresholds

## 📋 Prerequisites

### System Requirements
- **Node.js** v14 or higher
- **Python** 3.8 - 3.11 (3.10 recommended)
- **pip** (Python package manager)
- **Git** (for cloning repository)

### Optional
- **CUDA-compatible GPU** for faster processing (NVIDIA GPU with CUDA support)

## 🛠️ Technology Stack

### Backend
- **Python 3.8-3.11** - Core programming language
- **YOLOv8 (Ultralytics)** - Object detection model
- **PyTorch** - Deep learning framework
- **OpenCV** - Computer vision library
- **Flask** - REST API server
- **Flask-CORS** - Cross-origin resource sharing

### Frontend
- **Electron** - Desktop application framework
- **HTML5/CSS3** - User interface
- **JavaScript (ES6+)** - Frontend logic
- **Fetch API** - Backend communication

### Model
- **YOLOv8** - You Only Look Once v8
- Supports custom trained models
- Pre-trained COCO weights available

## 🚀 Installation

### Quick Setup (Recommended)

**Windows:**
```bash
# Clone the repository
git clone https://github.com/reymartjohneva/Aerial-Threat-Detection.git
cd Aerial-Threat-Detection

# Run automated setup
setup.bat
```

**Linux/Mac:**
```bash
# Clone the repository
git clone https://github.com/reymartjohneva/Aerial-Threat-Detection.git
cd Aerial-Threat-Detection

# Make setup script executable and run
chmod +x setup.sh
./setup.sh
```

### Manual Installation

### 1. Clone the Repository
```bash
git clone https://github.com/reymartjohneva/Aerial-Object-Detection.git
cd Aerial-Object-Detection
```

### 2. Install Node.js Dependencies
```bash
npm install
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

**Note:** This will install PyTorch, YOLOv8 (ultralytics), OpenCV, Flask, and other required packages.

### 4. Add Your YOLOv8 Model

Place your trained model in the `models/` directory:

- Copy your `model.pt` or `yolov8s.pt` file to `models/`
- If no model is found, YOLOv8s will be auto-downloaded on first run

```bash
# Example: Copy your trained model
copy path\to\your\model.pt models\model.pt
```

## 🎮 Running the Application

### Method 1: Start Both Services Separately (Recommended)

**Terminal 1 - Start Python Backend:**
```bash
python backend/server.py
```

**Terminal 2 - Start Electron App:**
```bash
npm start
```

### Method 2: Quick Start (Development)
```bash
npm run dev
```

The application will open automatically, and you can access:
- **Electron App**: Desktop window
- **Backend API**: http://localhost:5000

## 📖 Usage Guide

### Starting the Application

**Option 1: Quick Start (Windows)**
```bash
start.bat
```

**Option 2: Quick Start (Linux/Mac)**
```bash
chmod +x start.sh
./start.sh
```

**Option 3: Manual Start**
```bash
# Terminal 1 - Backend
python backend/server.py

# Terminal 2 - Frontend
npm start
```

### Using the Detection System

### 1. **Select Input Type**
   - Toggle between **Video** or **Image** mode
   - Each mode supports different file formats

### 2. **Upload File**
   - **Video**: Click "Select Video" or drag & drop
     - Supported: MP4, AVI, MOV, MKV, WebM
   - **Image**: Click "Select Image" or drag & drop
     - Supported: JPG, JPEG, PNG, BMP, TIFF, WebP

### 3. **Configure Processing** (Video only)
   - **Frame Skip**: Process every Nth frame for faster results
     - Every frame: Highest accuracy, slowest
     - Every 3rd frame: Balanced (recommended)
     - Every 5th frame: Fastest, lower accuracy

### 4. **Start Detection**
   - Click "🚀 Start Detection"
   - Monitor progress bar and statistics
   - View real-time counts:
     - Total Detections
     - Soldiers (red)
     - Civilians (green)
     - Other Objects (yellow)

### 5. **Review Results**
   - **Images**: View annotated image immediately
   - **Videos**: Wait for processing to complete
   - Check detection counts and classifications

### 6. **Export Results**
   - Click "⬇️ Download Result"
   - Processed files include:
     - Color-coded bounding boxes
     - Classification labels
     - Confidence percentages
     - Visual indicators (circles for soldiers, squares for civilians)

## 🎨 Detection Visualization

The system uses an advanced visualization scheme:

- **Bounding Boxes**: Color-coded by classification
  - Red: Soldiers
  - Green: Civilians
  - Blue/Orange/Magenta: Other objects (vehicles, drones, etc.)

- **Labels**: Semi-transparent backgrounds with white text
  - Format: "ClassName Confidence%"
  - Example: "Soldier 95%"
  - Black outline for visibility on any background

- **Visual Indicators**: Quick identification markers
  - Circle (●) in top-right: Soldier
  - Square (■) in top-right: Civilian

### 1. **Upload Video**
   - Click "Select Video" or drag & drop a video file
   - Supported formats: MP4, AVI, MOV, MKV, WebM

### 2. **Configure Processing**
   - Choose frame skip option (process every Nth frame for speed)
   - Default: Every 3rd frame (good balance)

### 3. **Start Detection**
   - Click "🚀 Start Detection"
   - Monitor real-time progress and statistics
   - View detection counts by threat level

### 4. **Review Results**
   - View total detections and threat breakdown
   - Download processed video with bounding boxes
   - Check detailed logs for frame-by-frame analysis

### 5. **Export & Share**
   - Download annotated video
   - Save detection reports
   - Share results via Google Drive or GitHub

## 🏗️ Project Structure

```
Aerial-Threat-Detection/
├── backend/
│   ├── detect.py              # YOLOv8 ObjectDetector class
│   ├── server.py              # Flask REST API server
│   └── __pycache__/           # Python cache files
├── models/
│   ├── yolov8s.pt             # YOLOv8 small model (auto-downloaded)
│   └── README.md              # Model documentation
├── uploads/                    # Uploaded files (auto-created)
│   └── README.md
├── outputs/                    # Processed results (auto-created)
│   └── README.md
├── tests/
│   └── test_detection.py      # Unit tests
├── detection.html             # Main detection interface
├── detection.js               # Frontend detection logic
├── index.html                 # Alternative monitoring interface
├── main.js                    # Electron main process
├── renderer.js                # Electron renderer process
├── styles.css                 # All application styling
├── package.json               # Node.js dependencies
├── requirements.txt           # Python dependencies
├── setup.bat                  # Windows setup script
├── setup.sh                   # Linux/Mac setup script
├── start.bat                  # Windows start script
├── start.sh                   # Linux/Mac start script
├── README.md                  # This file
├── QUICKSTART.md              # Quick start guide
├── DEPLOYMENT.md              # Deployment instructions
├── GETTING_STARTED.md         # Beginner's guide
├── IMPLEMENTATION_SUMMARY.md  # Technical implementation
└── PROJECT_REPORT.md          # Project documentation
```

### Key Components

**Backend (`backend/`)**
- `detect.py`: Core detection engine with ObjectDetector class
  - Model loading and initialization
  - Frame-by-frame detection
  - Bounding box visualization
  - Video processing pipeline
- `server.py`: Flask API providing REST endpoints
  - File upload handling
  - Job queue management
  - Real-time status updates

**Frontend**
- `detection.html`: Modern UI with file upload and results display
- `detection.js`: Client-side logic for API communication
- `styles.css`: Responsive styling with gradient backgrounds

**Electron**
- `main.js`: Desktop window management
- `renderer.js`: Browser-to-Node.js bridge

## 🏗️ Project Structure

```
Aerial-Threat-Detection/
├── backend/
│   ├── detect.py           # YOLOv8 detection engine
│   └── server.py           # Flask API server
├── models/
│   ├── model.pt            # Your trained model (place here)
│   └── README.md           # Model instructions
├── uploads/                # Uploaded videos (auto-created)
├── outputs/                # Processed videos (auto-created)
├── index.html              # Original monitoring interface
├── detection.html          # AI detection interface
├── detection.js            # Frontend detection logic
├── main.js                 # Electron main process
├── renderer.js             # Original renderer
├── styles.css              # All styling
├── package.json            # Node dependencies
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 API Endpoints

The Flask backend provides these REST API endpoints:

### Health Check
```http
GET /api/health
```
Returns server status, model loaded status, and device (CPU/CUDA).

**Response:**
```json
{
  "status": "running",
  "model_loaded": true,
  "device": "cuda"
}
```

### Upload File
```http
POST /api/upload
Content-Type: multipart/form-data

Fields:
  - video: File (for videos)
  - image: File (for images)
```

**Response:**
```json
{
  "success": true,
  "filename": "example.mp4",
  "filepath": "uploads/example.mp4",
  "file_type": "video",
  "message": "Video uploaded successfully"
}
```

### Detect Objects in Video
```http
POST /api/detect/video
Content-Type: application/json

Body:
{
  "filename": "example.mp4",
  "frame_skip": 3
}
```

**Response:**
```json
{
  "success": true,
  "job_id": "example_mp4",
  "message": "Video processing started"
}
```

### Detect Objects in Image
```http
POST /api/detect/image
Content-Type: application/json

Body:
{
  "filename": "example.jpg"
}
```

**Response:**
```json
{
  "detections": [...],
  "frame_base64": "base64_encoded_image",
  "count": 5,
  "output_file": "detected_example.jpg",
  "timestamp": "2025-12-03T10:30:00"
}
```

### Check Processing Status
```http
GET /api/status/{job_id}
```

**Response:**
```json
{
  "status": "processing",
  "progress": 45.5,
  "detections": [...],
  "output_file": "detected_example.mp4"
}
```

### Download Processed File
```http
GET /api/download/{filename}
```
Returns the processed file as a downloadable attachment.

### List Available Models
```http
GET /api/models
```

**Response:**
```json
{
  "models": [
    {
      "name": "yolov8s.pt",
      "path": "models/yolov8s.pt",
      "size": 25000000
    }
  ]
}
```

### Detect Single Frame
```http
POST /api/detect/frame
Content-Type: multipart/form-data

Fields:
  - frame: File (image file)
```

## 🔧 API Endpoints

The Flask backend provides these REST API endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Check server and model status |
| `/api/upload` | POST | Upload video file |
| `/api/detect/video` | POST | Start video processing |
| `/api/status/<job_id>` | GET | Check processing status |
| `/api/download/<filename>` | GET | Download processed video |
| `/api/models` | GET | List available models |
| `/api/detect/frame` | POST | Detect objects in single frame |

## 🎨 Customization

### Custom Class Names

Edit `backend/detect.py` to match your trained model classes:

```python
self.class_names = {
    0: 'Person',
    1: 'Soldier',
    2: 'Civilian',
    3: 'Vehicle',
    4: 'Drone',
    5: 'Aircraft',
    6: 'Weapon',
    7: 'Unknown'
}
```

### Custom Colors

Modify the color scheme in `backend/detect.py`:

```python
self.colors = {
    'Soldier': (0, 0, 255),      # Red (BGR format)
    'Civilian': (0, 255, 0),     # Green
    'Person': (255, 165, 0),     # Blue
    'Vehicle': (0, 165, 255),    # Orange
    'Drone': (255, 0, 255),      # Magenta
    'Aircraft': (255, 255, 0),   # Cyan
    'Weapon': (0, 0, 128),       # Dark Red
    'Unknown': (255, 255, 255)   # White
}
```

### Detection Confidence Threshold

Adjust detection sensitivity in `backend/detect.py`:

```python
def __init__(self, model_path='models/yolov8s.pt', conf_threshold=0.5):
    # conf_threshold range: 0.0 - 1.0
    # Lower value = more detections (less confident)
    # Higher value = fewer detections (more confident)
    # Recommended: 0.3 - 0.7
```

### Frame Processing Speed

Balance speed vs accuracy in the UI or programmatically:

```python
# In server.py or when calling process_video
frame_skip = 1  # Process every frame (slowest, most accurate)
frame_skip = 3  # Process every 3rd frame (recommended)
frame_skip = 5  # Process every 5th frame (fastest)
```

### Label Appearance

Customize label transparency and text in `backend/detect.py`:

```python
# Label background transparency
alpha = 0.8  # Range: 0.0 (transparent) to 1.0 (opaque)

# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
font_thickness = 2
```

## 🎨 Customization

### Custom Class Names

Edit `backend/detect.py` to match your trained model classes:

```python
self.class_names = {
    0: 'Person',
    1: 'Soldier',
    2: 'Civilian',
    3: 'Vehicle',
    4: 'Drone',
    5: 'Aircraft',
    6: 'Weapon',
    7: 'Unknown'
}
```

### Detection Confidence Threshold

Adjust detection sensitivity in `backend/detect.py`:
    'Soldier': 'high',
    'Weapon': 'high',
    'Drone': 'medium',
    'Aircraft': 'medium',
    'Vehicle': 'medium',
    'Person': 'low',
    'Civilian': 'low',
}
```

### Confidence Threshold

Adjust detection sensitivity in `backend/detect.py`:

```python
def __init__(self, model_path='models/yolov8s.pt', conf_threshold=0.5):
    # Lower value = more detections (less confident)
    # Higher value = fewer detections (more confident)
```

## 🧪 Testing with Sample Videos

1. Find drone footage samples online (YouTube, Pexels, etc.)
2. Upload through the application interface
3. Review detection results

**Recommended Test Videos:**
- Aerial city footage
- Crowd monitoring
- Traffic surveillance
- Military simulation footage

## 📊 Performance Optimization

### For Faster Processing ⚡

1. **Use GPU (CUDA)**
   - 10-50x faster than CPU
   - Requires NVIDIA GPU with CUDA support
   - Install CUDA-enabled PyTorch

2. **Increase Frame Skip**
   ```python
   frame_skip = 5  # Process every 5th frame
   # Trade-off: May miss fast-moving objects
   ```

3. **Use Smaller Model**
   - YOLOv8n (nano): Fastest, less accurate
   - YOLOv8s (small): Balanced (default)
   - YOLOv8m (medium): Slower, more accurate
   - YOLOv8l (large): Slowest, most accurate

4. **Reduce Video Resolution**
   - 720p recommended for speed
   - 1080p for better accuracy
   - 4K only if necessary

5. **Optimize Confidence Threshold**
   ```python
   conf_threshold = 0.6  # Higher = fewer detections = faster
   ```

### For Better Accuracy 🎯

1. **Process Every Frame**
   ```python
   frame_skip = 1  # No frame skipping
   ```

2. **Use Larger Model**
   ```python
   model_path = 'models/yolov8l.pt'  # Large model
   ```

3. **Higher Resolution Videos**
   - Minimum 720p recommended
   - 1080p optimal

4. **Lower Confidence Threshold**
   ```python
   conf_threshold = 0.3  # Catch more potential detections
   ```

5. **Custom Trained Model**
   - Train on your specific use case
   - Fine-tune on similar aerial footage

### Performance Benchmarks

| Configuration | Device | FPS | Accuracy |
|--------------|--------|-----|----------|
| YOLOv8n + GPU | RTX 3060 | ~45 | Good |
| YOLOv8s + GPU | RTX 3060 | ~30 | Better |
| YOLOv8m + GPU | RTX 3060 | ~20 | Best |
| YOLOv8s + CPU | i7-10700K | ~5 | Better |
| YOLOv8n + CPU | i7-10700K | ~8 | Good |

*Note: FPS varies based on video resolution and frame skip settings*

## 📊 Performance Optimization

### For Faster Processing:
- Use GPU (CUDA) if available
- Increase frame skip (e.g., every 5th frame)
- Use smaller model (YOLOv8n/s instead of m/l/x)
- Lower resolution videos

### For Better Accuracy:
- Process every frame (frame_skip=1)
- Use larger model (YOLOv8m/l/x)
- Higher resolution videos
- Lower confidence threshold

## 🐛 Troubleshooting

### Common Issues and Solutions

#### Backend Server Won't Start

**Issue**: `ModuleNotFoundError` or `ImportError`

```bash
# Solution 1: Check Python version (must be 3.8-3.11)
python --version

# Solution 2: Reinstall all dependencies
pip install -r requirements.txt --upgrade

# Solution 3: Install specific packages
pip install ultralytics torch opencv-python flask flask-cors
```

**Issue**: Port already in use

```bash
# Find process using port 5000
netstat -ano | findstr :5000  # Windows
lsof -i :5000                  # Linux/Mac

# Kill the process or change port in backend/server.py
app.run(host='0.0.0.0', port=5001, debug=True)

# Update API_BASE in detection.js
const API_BASE = 'http://localhost:5001/api';
```

#### Model Not Loading

```bash
# Verify model file exists
dir models\        # Windows
ls -la models/     # Linux/Mac

# Download YOLOv8 model manually
python -c "from ultralytics import YOLO; YOLO('yolov8s.pt')"

# Move to models directory
move yolov8s.pt models\     # Windows
mv yolov8s.pt models/       # Linux/Mac
```

#### CUDA/GPU Issues

```bash
# Check if CUDA is available
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"

# If False, install CPU-only PyTorch
pip uninstall torch torchvision
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Or install CUDA-enabled PyTorch
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

#### Frontend Not Connecting to Backend

```bash
# Test backend directly
curl http://localhost:5000/api/health

# Or in browser
http://localhost:5000/api/health

# Check CORS settings in backend/server.py
CORS(app)  # Should be enabled

# Check console for errors (F12 in browser)
```

#### Electron Won't Start

```bash
# Reinstall Node dependencies
rm -rf node_modules package-lock.json  # Linux/Mac
rd /s /q node_modules                  # Windows
del package-lock.json                   # Windows

npm install

# Clear Electron cache
npm run clean
```

#### Video Processing Stuck

1. Check if backend is still running
2. Look at backend terminal for errors
3. Verify video file is not corrupted
4. Try with a smaller video file first
5. Reduce frame skip to increase speed

#### Poor Detection Accuracy

1. Lower confidence threshold (e.g., 0.3)
2. Use a larger model (yolov8m.pt or yolov8l.pt)
3. Process every frame instead of skipping
4. Ensure good video quality (720p minimum)
5. Train a custom model on your specific data

## 🐛 Troubleshooting

### Python Server Won't Start
```bash
# Check Python version (needs 3.8-3.11)
python --version

# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Model Not Loading
```bash
# Verify model file exists
dir models\

# Check backend logs for errors
python backend\server.py
```

### CUDA/GPU Issues
```bash
# Check PyTorch CUDA availability
python -c "import torch; print(torch.cuda.is_available())"

# Install CPU-only version if needed
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### Port Already in Use
```bash
# Change port in backend/server.py (last line)
app.run(host='0.0.0.0', port=5001, debug=True)

# Update API_BASE in detection.js
const API_BASE = 'http://localhost:5001/api';
```

## 📝 Development Roadmap

### Completed ✅
- [x] YOLOv8 integration and model loading
- [x] Video and image upload support
- [x] Real-time progress monitoring
- [x] Multi-class object detection
- [x] Classification-based counting (Soldiers, Civilians, Others)
- [x] Color-coded bounding box visualization
- [x] Semi-transparent labels with confidence scores
- [x] Visual indicators (shapes) for quick identification
- [x] Export processed videos and images
- [x] REST API with comprehensive endpoints
- [x] Cross-platform desktop application (Electron)
- [x] GPU acceleration support (CUDA)
- [x] Configurable frame skip for performance
- [x] Adjustable confidence thresholds
- [x] Drag-and-drop file upload
- [x] File type toggle (Video/Image)

### In Progress 🚧
- [ ] Enhanced error handling and validation
- [ ] Batch processing for multiple files
- [ ] Detection history and session management

### Planned 📋
- [ ] **Live Camera Support**: Real-time detection from webcam or IP cameras
- [ ] **Stream Processing**: Analyze RTSP/RTMP video streams
- [ ] **Multiple Model Comparison**: Side-by-side comparison of different models
- [ ] **Custom Training Pipeline**: Train models on custom datasets
- [ ] **Advanced Analytics**: Heatmaps, tracking, and trajectory analysis
- [ ] **Export Formats**: JSON, CSV, XML detection reports
- [ ] **Cloud Deployment**: Docker containers and cloud hosting
- [ ] **Mobile App**: iOS and Android companion apps
- [ ] **Database Integration**: Store detection history in SQLite/PostgreSQL
- [ ] **User Authentication**: Multi-user support with login system
- [ ] **Notification System**: Alerts for specific detection events
- [ ] **Video Timeline**: Scrubber to navigate detection results
- [ ] **Object Tracking**: Track objects across frames
- [ ] **Zone-based Detection**: Define areas of interest
- [ ] **Performance Metrics**: FPS, latency, and accuracy tracking

## 📝 Development Roadmap

- [x] YOLOv8 integration
- [x] Video upload and processing
- [x] Real-time progress monitoring
- [x] Object classification (Soldier/Civilian)
- [x] Live preview during processing
- [x] Image and video support
- [x] Export processed videos
- [ ] Live camera/stream support
- [ ] Multiple model comparison
- [ ] Custom training pipeline
- [ ] Cloud deployment option
- [ ] Mobile app version

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### How to Contribute

1. **Fork the Repository**
   ```bash
   # Click the 'Fork' button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Aerial-Threat-Detection.git
   cd Aerial-Threat-Detection
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

4. **Make Your Changes**
   - Write clean, documented code
   - Follow existing code style
   - Add comments where necessary
   - Update README if adding features

5. **Test Your Changes**
   ```bash
   # Run the application
   python backend/server.py
   npm start
   
   # Test detection functionality
   python tests/test_detection.py
   ```

6. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   # or
   git commit -m "Fix: Brief description of the bug fix"
   ```

7. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your feature branch
   - Describe your changes in detail

### Contribution Guidelines

- **Code Quality**: Follow PEP 8 for Python, ESLint for JavaScript
- **Documentation**: Update README.md and inline comments
- **Testing**: Ensure your code doesn't break existing functionality
- **Commits**: Use clear, descriptive commit messages
- **Issues**: Check existing issues before creating new ones

### Areas for Contribution

- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🎨 UI/UX enhancements
- ⚡ Performance optimizations
- 🧪 Test coverage
- 🌐 Translations

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ❌ Liability
- ❌ Warranty

## 👨‍💻 Author

**Reymart John Eva**
- GitHub: [@reymartjohneva](https://github.com/reymartjohneva)
- Repository: [Aerial-Threat-Detection](https://github.com/reymartjohneva/Aerial-Threat-Detection)

## 🙏 Acknowledgments

This project was made possible by these amazing open-source projects:

- **[Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)** - State-of-the-art object detection
- **[PyTorch](https://pytorch.org/)** - Deep learning framework
- **[Electron](https://www.electronjs.org/)** - Cross-platform desktop apps
- **[Flask](https://flask.palletsprojects.com/)** - Lightweight web framework
- **[OpenCV](https://opencv.org/)** - Computer vision library
- **[Node.js](https://nodejs.org/)** - JavaScript runtime

Special thanks to the open-source community for continuous inspiration and support.

## 📚 References

### Documentation
- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [Electron Documentation](https://www.electronjs.org/docs/latest)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenCV Python Documentation](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

### Research Papers
- [YOLOv8: Ultralytics](https://github.com/ultralytics/ultralytics)
- [You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640)

### Tutorials
- [Custom YOLOv8 Training](https://docs.ultralytics.com/modes/train/)
- [Flask REST API Development](https://flask.palletsprojects.com/en/2.3.x/quickstart/)
- [Electron App Development](https://www.electronjs.org/docs/latest/tutorial/tutorial-prerequisites)

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/reymartjohneva/Aerial-Threat-Detection?style=social)
![GitHub forks](https://img.shields.io/github/forks/reymartjohneva/Aerial-Threat-Detection?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/reymartjohneva/Aerial-Threat-Detection?style=social)

## ⚠️ Disclaimer

This application is designed for **educational and research purposes only**. 

- Ensure you have proper authorization before analyzing any surveillance footage
- Respect privacy laws and regulations in your jurisdiction
- The classification results (Soldier/Civilian) are AI predictions and should not be used for critical decision-making without human verification
- Users are responsible for compliance with local laws regarding AI, surveillance, and data privacy
- This tool should not be used for illegal surveillance or unauthorized monitoring

## 📞 Support

If you encounter any issues or have questions:

1. **Check Documentation**: Read this README and other docs thoroughly
2. **Search Issues**: Look for similar issues on GitHub
3. **Create an Issue**: [Open a new issue](https://github.com/reymartjohneva/Aerial-Threat-Detection/issues) with:
   - Detailed description
   - Steps to reproduce
   - System information
   - Error messages/screenshots
4. **Community**: Join discussions in the Issues section

---

**Made with ❤️ by Reymart John Eva**

*Star ⭐ this repository if you find it helpful!*
