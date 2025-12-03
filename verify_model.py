"""
Model Verification Script
Checks the trained YOLOv8 model's classes and configuration
"""

from ultralytics import YOLO
import torch

print("="*60)
print("YOLOv8 Model Verification")
print("="*60)

# Load the model
model_path = 'models/yolov8s.pt'
print(f"\nLoading model from: {model_path}")

try:
    model = YOLO(model_path)
    
    print(f"✓ Model loaded successfully!")
    print(f"\nDevice: {'CUDA (GPU)' if torch.cuda.is_available() else 'CPU'}")
    
    # Check if model has names attribute
    if hasattr(model, 'names'):
        print(f"\n{'='*60}")
        print(f"Model has {len(model.names)} classes:")
        print(f"{'='*60}")
        
        for idx, name in model.names.items():
            print(f"  Class {idx}: '{name}'")
        
        print(f"{'='*60}")
        
        # Verify it's the correct custom model
        class_names_lower = [name.lower() for name in model.names.values()]
        
        if 'civilian' in class_names_lower and 'soldier' in class_names_lower:
            print("\n✓ CORRECT: This is your custom-trained model!")
            print("  Contains: 'civilian' and 'soldier' classes")
        elif len(model.names) == 80:
            print("\n✗ WARNING: This appears to be the default COCO model (80 classes)")
            print("  You need to use your custom-trained model instead!")
        else:
            print(f"\n⚠ NOTICE: Model has {len(model.names)} classes")
            print("  Classes found:", ', '.join(class_names_lower))
    else:
        print("\n✗ ERROR: Model does not have class names")
    
    print(f"\n{'='*60}")
    print("Model Info:")
    print(f"{'='*60}")
    print(f"Model type: {model.task}")
    
except Exception as e:
    print(f"\n✗ ERROR loading model: {e}")

print("\n" + "="*60)
print("Verification Complete")
print("="*60)
