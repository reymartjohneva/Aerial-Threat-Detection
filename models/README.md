# YOLOv8 Models Directory

Place your trained YOLOv8 model files here.

## Supported Models

- `model.pt` - Your custom trained model for aerial threat detection
- `yolov8s.pt` - YOLOv8 Small model (will be downloaded automatically if not present)
- `yolov8m.pt` - YOLOv8 Medium model
- `yolov8l.pt` - YOLOv8 Large model
- `yolov8x.pt` - YOLOv8 Extra Large model

## Instructions

1. **For your custom trained model:**
   - Copy your `model.pt` file to this directory
   - The backend will automatically detect and load it

2. **For pre-trained YOLOv8 models:**
   - The system will auto-download YOLOv8s on first run if no model is found
   - Or manually download from: https://github.com/ultralytics/assets/releases

## Model Priority

The backend will look for models in this order:
1. `model.pt` (your custom model)
2. `yolov8s.pt` (small model)
3. Auto-download `yolov8s.pt` if none found

## Custom Classes

If your model is trained with custom classes (e.g., Soldier, Civilian), make sure to update the class names in `backend/detect.py`:

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
