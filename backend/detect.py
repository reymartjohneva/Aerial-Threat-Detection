"""
YOLOv8 Object Detection Backend
Handles video processing and real-time object detection
"""

import cv2
import torch
from ultralytics import YOLO
import numpy as np
from pathlib import Path
import json
import base64
from datetime import datetime

class ObjectDetector:
    def __init__(self, model_path='models/yolov8s.pt', conf_threshold=0.5):
        """
        Initialize the object detector
        
        Args:
            model_path: Path to YOLOv8 model file
            conf_threshold: Confidence threshold for detections
        """
        self.model_path = model_path
        self.conf_threshold = conf_threshold
        self.model = None
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        
        # Custom class names for aerial detection
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
        
        # Class-specific colors (BGR format)
        self.colors = {
            'Soldier': (0, 0, 255),      # Red
            'Civilian': (0, 255, 0),     # Green
            'Person': (255, 165, 0),     # Blue
            'Vehicle': (0, 165, 255),    # Orange
            'Drone': (255, 0, 255),      # Magenta
            'Aircraft': (255, 255, 0),   # Cyan
            'Weapon': (0, 0, 128),       # Dark Red
            'Unknown': (255, 255, 255)   # White
        }
        
        self.load_model()
    
    def load_model(self):
        """Load the YOLOv8 model"""
        try:
            print(f"Loading model from {self.model_path}")
            print(f"Using device: {self.device}")
            
            self.model = YOLO(self.model_path)
            self.model.to(self.device)
            
            print("Model loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    
    def draw_detections(self, frame, detections):
        """
        Draw bounding boxes and labels on frame
        
        Args:
            frame: Input frame
            detections: Detection results
            
        Returns:
            Annotated frame
        """
        annotated_frame = frame.copy()
        
        for det in detections:
            x1, y1, x2, y2 = map(int, det['bbox'])
            class_name = det['class']
            confidence = det['confidence']
            
            # Get color based on class name
            color = self.colors.get(class_name, self.colors['Unknown'])
            
            # Draw bounding box with thickness based on importance
            thickness = 3 if class_name in ['Soldier', 'Civilian'] else 2
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, thickness)
            
            # Prepare label text
            label = f"{class_name} {confidence:.0%}"
            
            # Get text size for background
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.6
            font_thickness = 2
            (text_width, text_height), baseline = cv2.getTextSize(label, font, font_scale, font_thickness)
            
            # Calculate label position (above the box)
            label_y = y1 - 10 if y1 - 10 > text_height else y1 + text_height + 10
            
            # Draw semi-transparent background for label
            overlay = annotated_frame.copy()
            cv2.rectangle(overlay, 
                         (x1, label_y - text_height - 8),
                         (x1 + text_width + 10, label_y + baseline + 2),
                         color, -1)
            
            # Blend the overlay with the original frame for transparency
            alpha = 0.8
            cv2.addWeighted(overlay, alpha, annotated_frame, 1 - alpha, 0, annotated_frame)
            
            # Draw black outline for text (for better visibility)
            cv2.putText(annotated_frame, label,
                       (x1 + 5, label_y),
                       font, font_scale, (0, 0, 0), font_thickness + 2, cv2.LINE_AA)
            
            # Draw white text on top
            cv2.putText(annotated_frame, label,
                       (x1 + 5, label_y),
                       font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)
            
            # Add a small icon/indicator for quick identification
            if class_name == 'Soldier':
                # Draw small circle in top-right corner of box
                cv2.circle(annotated_frame, (x2 - 10, y1 + 10), 6, color, -1)
                cv2.circle(annotated_frame, (x2 - 10, y1 + 10), 6, (255, 255, 255), 1)
            elif class_name == 'Civilian':
                # Draw small square in top-right corner of box
                cv2.rectangle(annotated_frame, (x2 - 16, y1 + 4), (x2 - 4, y1 + 16), color, -1)
                cv2.rectangle(annotated_frame, (x2 - 16, y1 + 4), (x2 - 4, y1 + 16), (255, 255, 255), 1)
        
        return annotated_frame
    
    def detect_frame(self, frame):
        """
        Perform detection on a single frame
        
        Args:
            frame: Input frame (numpy array)
            
        Returns:
            dict: Detection results and annotated frame
        """
        if self.model is None:
            return None
        
        # Perform inference
        results = self.model(frame, conf=self.conf_threshold, verbose=False)
        
        detections = []
        
        # Process results
        for result in results:
            boxes = result.boxes
            
            for box in boxes:
                # Extract box coordinates
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                
                # Get class and confidence
                cls = int(box.cls[0].cpu().numpy())
                conf = float(box.conf[0].cpu().numpy())
                
                # Get class name (use custom names or default)
                if hasattr(result, 'names'):
                    class_name = result.names[cls]
                else:
                    class_name = self.class_names.get(cls, 'Unknown')
                
                detection = {
                    'bbox': [float(x1), float(y1), float(x2), float(y2)],
                    'class': class_name,
                    'class_id': cls,
                    'confidence': conf
                }
                
                detections.append(detection)
        
        # Draw detections on frame
        annotated_frame = self.draw_detections(frame, detections)
        
        return {
            'detections': detections,
            'frame': annotated_frame,
            'count': len(detections),
            'timestamp': datetime.now().isoformat()
        }
    
    def process_video(self, video_path, output_path=None, frame_skip=1):
        """
        Process entire video file
        
        Args:
            video_path: Path to input video
            output_path: Path to save output video (optional)
            frame_skip: Process every nth frame for speed
            
        Yields:
            Detection results for each processed frame
        """
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            raise ValueError(f"Cannot open video: {video_path}")
        
        # Get video properties
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # Initialize video writer if output path provided
        writer = None
        if output_path:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        frame_count = 0
        processed_count = 0
        
        try:
            while cap.isOpened():
                ret, frame = cap.read()
                
                if not ret:
                    break
                
                frame_count += 1
                
                # Skip frames for performance
                if frame_count % frame_skip != 0:
                    continue
                
                # Detect objects
                result = self.detect_frame(frame)
                
                if result:
                    processed_count += 1
                    result['frame_number'] = frame_count
                    result['total_frames'] = total_frames
                    result['progress'] = (frame_count / total_frames) * 100
                    
                    # Write annotated frame
                    if writer:
                        writer.write(result['frame'])
                    
                    yield result
        
        finally:
            cap.release()
            if writer:
                writer.release()
    
    def frame_to_base64(self, frame):
        """Convert frame to base64 for transmission"""
        _, buffer = cv2.imencode('.jpg', frame)
        return base64.b64encode(buffer).decode('utf-8')


if __name__ == '__main__':
    # Test the detector
    detector = ObjectDetector()
    
    print("\nObject Detector initialized successfully!")
    print(f"Device: {detector.device}")
    print(f"Model: {detector.model_path}")
    print(f"Ready for detection...")
