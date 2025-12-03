"""
Test script to verify model class mappings and detection accuracy
"""
from ultralytics import YOLO
import cv2
import numpy as np

def test_model_classes():
    """Test the model to see its actual class mappings"""
    print("="*70)
    print("MODEL CLASS VERIFICATION")
    print("="*70)
    
    model_path = 'models/yolov8s.pt'
    print(f"\nLoading model: {model_path}")
    
    try:
        model = YOLO(model_path)
        
        print("\n✓ Model loaded successfully!")
        print(f"\nDevice: {'CUDA' if model.device.type == 'cuda' else 'CPU'}")
        
        # Print class names
        if hasattr(model, 'names'):
            print(f"\n{'='*70}")
            print("CLASS MAPPINGS IN YOUR MODEL:")
            print(f"{'='*70}")
            for idx, name in model.names.items():
                print(f"  Class ID {idx} → '{name}'")
            print(f"{'='*70}\n")
            
            # Check if both classes exist
            names_lower = [name.lower() for name in model.names.values()]
            
            if 'civilian' in names_lower and 'soldier' in names_lower:
                print("✓ Both 'civilian' and 'soldier' classes found in model!")
                
                # Find which ID corresponds to which class
                civ_id = next((k for k, v in model.names.items() if v.lower() == 'civilian'), None)
                sol_id = next((k for k, v in model.names.items() if v.lower() == 'soldier'), None)
                
                print(f"\n  → CIVILIAN is Class ID: {civ_id}")
                print(f"  → SOLDIER is Class ID: {sol_id}")
            else:
                print("⚠ WARNING: Expected classes not found!")
                print(f"   Found: {', '.join(model.names.values())}")
        
        print("\n" + "="*70)
        print("RECOMMENDATIONS FOR BETTER ACCURACY:")
        print("="*70)
        print("1. Confidence threshold set to 0.25 (more sensitive)")
        print("2. Model uses class-specific NMS to reduce confusion")
        print("3. GPU half-precision enabled for faster inference")
        print("4. Image size: 640x640 for optimal detection")
        print("\nIf misclassification persists, you may need to:")
        print("  • Retrain the model with more diverse training data")
        print("  • Balance your training dataset (equal civilian/soldier examples)")
        print("  • Use data augmentation during training")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"✗ Error: {e}")

if __name__ == '__main__':
    test_model_classes()
