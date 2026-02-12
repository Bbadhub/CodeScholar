# YOLOx

*Also known as: You Only Look Once X*

**YOLOx is a one-stage object detection model that predicts bounding boxes and classifications in a single pass, optimized for speed and efficiency.**

**Category:** neural_architecture  
**Maturity:** proven

## How It Works

YOLOx utilizes a backbone network called CSPDarkNet to extract features from input video frames. It aggregates space-time features from consecutive frames to enhance detection accuracy. The model predicts bounding boxes and class labels in one pass, allowing for fast inference speeds. Additionally, it reuses results from previous frames to improve detection performance in video streams.

## Algorithm

**Input:** Video frames in RGB format (e.g., 640x640 pixels).

**Output:** Detected objects with bounding boxes and class labels.

**Steps:**

1. Input video frames into the YOLOx model.
2. Extract features using the CSPDarkNet backbone.
3. Aggregate space-time features from consecutive frames.
4. Predict bounding boxes and classifications in one pass.
5. Reuse results from previous frames to improve detection.
6. Output detected objects with bounding boxes and class labels.

**Core Operation:** `output = predict(bounding_boxes, class_labels)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `input_size` | 640x640 | Changing this affects the model's ability to detect objects at different scales. |
| `confidence_threshold` | 0.5 | Higher values reduce false positives but may miss some detections. |
| `nms_threshold` | 0.4 | Adjusting this affects how overlapping bounding boxes are handled. |

## Complexity

- **Time:** O(n)
- **Space:** O(n)
- **In practice:** YOLOx is designed for real-time applications, achieving 30 FPS on benchmark datasets.

## Implementation

```python
def yolo_x_detect(frames: List[np.ndarray]) -> List[Tuple[np.ndarray, str]]:
    # Load YOLOx model
    model = load_yolox_model()
    results = []
    for frame in frames:
        features = model.extract_features(frame)
        detections = model.predict(features)
        results.append(detections)
    return results
```

## Common Mistakes

- Not adjusting the input size for specific use cases.
- Ignoring the impact of confidence and NMS thresholds on results.
- Failing to preprocess video frames correctly before input.

## Use When

- You need fast object detection in video streams.
- Real-time applications require efficient processing.
- You want to detect objects under varying motion conditions.

## Avoid When

- High accuracy is prioritized over speed.
- The application involves complex scene understanding.
- You need to detect small objects in high-density scenes.

## Tradeoffs

**Strengths:**

- Fast inference speeds suitable for real-time applications.
- Single-pass detection simplifies the processing pipeline.
- Effective in aggregating features from video frames.

**Weaknesses:**

- May sacrifice accuracy for speed in complex scenes.
- Less effective at detecting small objects in dense environments.
- Requires careful tuning of parameters for optimal performance.

**Compared To:**

- **vs Faster R-CNN:** Use YOLOx for speed; use Faster R-CNN for higher accuracy.
- **vs SSD:** YOLOx offers better speed improvements over SSD in video applications.

## Connects To

- Faster R-CNN
- Single Shot MultiBox Detector (SSD)
- Object Detection
- Real-time Video Processing
- Deep Learning for Computer Vision

## Evidence (Papers)

- **Video object detection via space–time feature aggregation and result reuse** - [DOI](https://doi.org/10.1049/ipr2.13179)
