"""
Test script for YOLOv8 detection
Verifies model loading and basic inference
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from detect import ThreatDetector
import cv2
import numpy as np

def test_model_loading():
    """Test if model loads successfully"""
    print("\n" + "="*60)
    print("TEST 1: Model Loading")
    print("="*60)
    
    try:
        detector = ThreatDetector()
        print("✓ Model loaded successfully")
        print(f"  Device: {detector.device}")
        print(f"  Model path: {detector.model_path}")
        return True
    except Exception as e:
        print(f"✗ Model loading failed: {e}")
        return False

def test_single_frame_detection():
    """Test detection on a single synthetic frame"""
    print("\n" + "="*60)
    print("TEST 2: Single Frame Detection")
    print("="*60)
    
    try:
        detector = ThreatDetector()
        
        # Create a test frame (random image)
        test_frame = np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)
        
        # Add some simple shapes to detect
        cv2.rectangle(test_frame, (100, 100), (200, 200), (255, 0, 0), -1)
        cv2.circle(test_frame, (400, 400), 50, (0, 255, 0), -1)
        
        result = detector.detect_frame(test_frame)
        
        if result:
            print("✓ Detection successful")
            print(f"  Detections count: {result['count']}")
            print(f"  Timestamp: {result['timestamp']}")
            return True
        else:
            print("✗ Detection returned None")
            return False
            
    except Exception as e:
        print(f"✗ Detection failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_class_names():
    """Test custom class names configuration"""
    print("\n" + "="*60)
    print("TEST 3: Class Names Configuration")
    print("="*60)
    
    try:
        detector = ThreatDetector()
        
        print("✓ Custom class names loaded:")
        for cls_id, cls_name in detector.class_names.items():
            print(f"  {cls_id}: {cls_name}")
        
        return True
    except Exception as e:
        print(f"✗ Class names test failed: {e}")
        return False

def test_threat_levels():
    """Test threat level mapping"""
    print("\n" + "="*60)
    print("TEST 4: Threat Level Mapping")
    print("="*60)
    
    try:
        detector = ThreatDetector()
        
        test_classes = ['Soldier', 'Civilian', 'Drone', 'Unknown']
        
        print("✓ Threat level mapping:")
        for cls_name in test_classes:
            level = detector.get_threat_level(cls_name)
            print(f"  {cls_name:15} -> {level}")
        
        return True
    except Exception as e:
        print(f"✗ Threat level test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("YOLOv8 Detection System - Test Suite")
    print("="*60)
    
    tests = [
        test_model_loading,
        test_single_frame_detection,
        test_class_names,
        test_threat_levels
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"\n✗ Test failed with exception: {e}")
            results.append(False)
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    print(f"Failed: {total - passed}/{total}")
    
    if passed == total:
        print("\n✓ ALL TESTS PASSED!")
        return 0
    else:
        print("\n✗ SOME TESTS FAILED")
        return 1

if __name__ == '__main__':
    sys.exit(main())
