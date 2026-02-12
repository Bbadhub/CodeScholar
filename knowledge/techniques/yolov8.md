# YOLOv8

*Also known as: You Only Look Once version 8*

**YOLOv8 is a lightweight object detection algorithm optimized for real-time performance on low-powered hardware.**

**Category:** neural_architecture  
**Maturity:** proven (widely used in production)

## How It Works

YOLOv8 adapts the YOLO architecture to reduce computational requirements while maintaining detection accuracy. It processes live video feeds to detect and track moving targets in real-time. The model is initialized with lightweight configurations, allowing it to operate efficiently on devices with limited resources.

## Algorithm

**Input:** Live video feed from cameras.

**Output:** Detected targets with their positions and actions, along with trigger signals.

**Steps:**

1. 1. Initialize the YOLOv8 model with lightweight configurations.
2. 2. Capture live video feed from the camera.
3. 3. Preprocess the video frames for input into the model.
4. 4. Run the model on each frame to detect moving targets.
5. 5. Post-process the detection results to filter and trigger actions.
6. 6. Send triggers to the system based on detected actions.

**Core Operation:** `output = detect(targets, frames)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `input_size` | 640x640 | Changing this affects the model's ability to detect smaller objects. |
| `confidence_threshold` | 0.5 | Lowering this may increase false positives. |
| `nms_threshold` | 0.4 | Adjusting this changes how overlapping detections are handled. |

## Complexity

- **Time:** O(n)
- **Space:** O(1)
- **In practice:** Inference time is approximately 30ms per frame, making it suitable for real-time applications.

## Implementation

```python
def yolo_v8_detection(video_feed: str) -> List[DetectedObject]:
    model = initialize_yolo_v8(lightweight=True)
    for frame in capture_video(video_feed):
        preprocessed_frame = preprocess(frame)
        detections = model.detect(preprocessed_frame)
        filtered_detections = post_process(detections)
        trigger_actions(filtered_detections)
    return filtered_detections
```

## Common Mistakes

- Neglecting to optimize input size for specific hardware capabilities.
- Setting the confidence threshold too low, leading to excessive false positives.
- Failing to properly preprocess video frames before feeding them into the model.

## Use When

- You need to deploy a detection system on low-powered hardware.
- Real-time processing of video feeds is required.
- You want to minimize latency in detection tasks.

## Avoid When

- High accuracy is critical and resources are not constrained.
- You need to process large volumes of data in the cloud.
- The application requires complex scene understanding beyond simple detection.

## Tradeoffs

**Strengths:**

- Optimized for real-time performance on low-powered devices.
- Improved mAP by 10% over previous YOLO versions.
- Lightweight architecture reduces computational load.

**Weaknesses:**

- May not achieve the same accuracy as heavier models on complex tasks.
- Limited capability for detailed scene understanding.
- Performance may degrade with high-resolution inputs.

**Compared To:**

- **vs YOLOv5:** Use YOLOv8 for lower latency and resource-constrained environments; use YOLOv5 for higher accuracy when resources allow.

## Connects To

- YOLOv5
- YOLOv7
- SSD (Single Shot MultiBox Detector)
- Faster R-CNN
- MobileNet

## Evidence (Papers)

- **Application of Lightweight Target Detection Algorithm Based on YOLOv8 for Police Intelligent Moving Targets** - [DOI](https://doi.org/10.1049/cdt2/9984821)
