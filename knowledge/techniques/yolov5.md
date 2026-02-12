# YOLOv5

*Also known as: You Only Look Once version 5*

**YOLOv5 is a real-time object detection model that identifies and classifies objects in images efficiently.**

**Category:** neural_architecture  
**Maturity:** proven

## How It Works

YOLOv5 processes images through a single neural network that divides the image into a grid and predicts bounding boxes and class probabilities for each grid cell. It uses a series of convolutional layers to extract features from the image and applies non-maximum suppression to filter out overlapping boxes. This allows for fast and accurate detection of multiple objects in a single pass.

## Algorithm

**Input:** Raw image data in various formats (e.g., fits, JPEG)

**Output:** Classified images with bounding boxes indicating detected objects

**Steps:**

1. Load the input image data.
2. Resize the image to the required dimensions (e.g., 640x480 pixels).
3. Pass the image through the YOLOv5 model to predict bounding boxes and class probabilities.
4. Apply non-maximum suppression to eliminate redundant boxes.
5. Output the classified images with detected objects.

**Core Operation:** `output = sigmoid(predictions) · (bounding boxes + class probabilities)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `image_size` | 640x480 | Changing the size affects detection accuracy and processing speed. |
| `threshold_value` | adaptive thresholding method | Altering this value can change the sensitivity of detection. |
| `kernel_size` | 4x4 | Modifying kernel size impacts the morphological operations applied to the image. |

## Complexity

- **Time:** O(n)
- **Space:** O(n)
- **In practice:** Real-world performance can vary based on hardware and image complexity.

## Implementation

```python
def detect_objects(image: np.ndarray) -> List[DetectedObject]:
    resized_image = resize(image, (640, 480))
    predictions = yolo_model.predict(resized_image)
    boxes = non_max_suppression(predictions)
    return boxes
```

## Common Mistakes

- Not resizing images to the expected input size.
- Ignoring the need for non-maximum suppression, leading to multiple overlapping detections.
- Failing to preprocess images correctly, which can affect detection accuracy.

## Use When

- You need to analyze large volumes of astronomical image data.
- Real-time detection of phenomena in remote sensing applications is required.
- You want to leverage cloud computing for scalable image processing.

## Avoid When

- You require on-premises processing due to data privacy concerns.
- The image data is too small to justify cloud computing costs.
- You need a solution that does not rely on external cloud services.

## Tradeoffs

**Strengths:**

- High speed and efficiency for real-time applications.
- Ability to detect multiple objects in a single image.
- Scalable through cloud computing resources.

**Weaknesses:**

- Dependent on cloud infrastructure, which may raise privacy concerns.
- Performance can degrade with very small or very large objects.
- Requires significant computational resources for training.

**Compared To:**

- **vs Traditional image analysis methods:** YOLOv5 is faster and more effective for complex scenes.

## Connects To

- OpenCV for image processing
- AWS Lambda for serverless architecture
- Non-maximum suppression techniques
- Other YOLO versions (e.g., YOLOv4, YOLOv3)

## Evidence (Papers)

- **A serverless computing architecture for Martian aurora detection with the Emirates Mars Mission** - [DOI](https://doi.org/10.1038/s41598-024-53492-4)
