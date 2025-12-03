"""
Model Setup Helper Script
Downloads YOLOv8 model if not present and verifies setup
"""

import os
import sys
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and 8 <= version.minor <= 11:
        print("✓ Python version is compatible")
        return True
    else:
        print("✗ Python version must be 3.8-3.11")
        print("  Current version:", f"{version.major}.{version.minor}.{version.micro}")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = {
        'torch': 'PyTorch',
        'ultralytics': 'YOLOv8',
        'cv2': 'OpenCV',
        'flask': 'Flask',
        'numpy': 'NumPy'
    }
    
    missing = []
    
    for package, name in required_packages.items():
        try:
            if package == 'cv2':
                __import__('cv2')
            else:
                __import__(package)
            print(f"✓ {name} is installed")
        except ImportError:
            print(f"✗ {name} is NOT installed")
            missing.append(package)
    
    return missing

def check_model_file():
    """Check if model file exists"""
    model_dir = Path('models')
    model_files = ['model.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt']
    
    found_models = []
    for model_file in model_files:
        model_path = model_dir / model_file
        if model_path.exists():
            size = model_path.stat().st_size / (1024 * 1024)  # Size in MB
            print(f"✓ Found model: {model_file} ({size:.1f} MB)")
            found_models.append(model_file)
    
    if not found_models:
        print("⚠ No model files found in models/ directory")
        print("\nOptions:")
        print("1. Copy your trained model.pt to models/")
        print("2. Run this script to download YOLOv8s (recommended)")
        print("3. The backend will auto-download on first run")
        return None
    
    return found_models[0]

def download_yolov8_model():
    """Download YOLOv8 model"""
    try:
        from ultralytics import YOLO
        
        print("\nDownloading YOLOv8s model...")
        print("This may take a few minutes...")
        
        model = YOLO('yolov8s.pt')
        
        # Move to models directory
        import shutil
        source = 'yolov8s.pt'
        dest = 'models/yolov8s.pt'
        
        if os.path.exists(source):
            shutil.move(source, dest)
            print(f"✓ Model downloaded and saved to {dest}")
            return True
        else:
            print("✓ Model downloaded (already in cache)")
            return True
            
    except Exception as e:
        print(f"✗ Error downloading model: {e}")
        return False

def setup_directories():
    """Create necessary directories"""
    dirs = ['models', 'uploads', 'outputs', 'backend', 'tests']
    
    for dir_name in dirs:
        dir_path = Path(dir_name)
        if not dir_path.exists():
            dir_path.mkdir(parents=True)
            print(f"✓ Created directory: {dir_name}")
        else:
            print(f"✓ Directory exists: {dir_name}")

def main():
    """Main setup function"""
    print("=" * 60)
    print("Aerial Threat Detection - Model Setup")
    print("=" * 60)
    print()
    
    # Check Python version
    print("Step 1: Checking Python version...")
    if not check_python_version():
        print("\nPlease install a compatible Python version (3.8-3.11)")
        return 1
    print()
    
    # Check dependencies
    print("Step 2: Checking dependencies...")
    missing = check_dependencies()
    if missing:
        print(f"\n⚠ Missing packages: {', '.join(missing)}")
        print("\nPlease install missing packages:")
        print("pip install -r requirements.txt")
        return 1
    print()
    
    # Setup directories
    print("Step 3: Setting up directories...")
    setup_directories()
    print()
    
    # Check model
    print("Step 4: Checking for model files...")
    model = check_model_file()
    
    if not model:
        print("\nWould you like to download YOLOv8s model? (y/n): ", end='')
        choice = input().lower()
        
        if choice == 'y':
            if download_yolov8_model():
                print("\n✓ Model setup complete!")
            else:
                print("\n✗ Model download failed")
                print("You can manually place your model.pt file in models/")
                return 1
        else:
            print("\nPlease place your model.pt file in the models/ directory")
            print("The system will auto-download YOLOv8s on first run if no model is found")
    else:
        print(f"\n✓ Using model: {model}")
    
    print("\n" + "=" * 60)
    print("Setup Complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Start the backend server: python backend/server.py")
    print("2. Start the Electron app: npm start")
    print("\nOr use the quick start scripts:")
    print("  Windows: start.bat")
    print("  Linux/Mac: ./start.sh")
    print()
    
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nError during setup: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
