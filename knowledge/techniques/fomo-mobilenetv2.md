# FOMO (MobileNetV2)

**FOMO utilizes MobileNetV2 for real-time object shape recognition in bionic prostheses.**

**Category:** neural_architecture  
**Maturity:** proven

## How It Works

FOMO employs a MobileNetV2 neural network to classify images of objects captured by a camera. The system processes these images to identify shapes such as spherical, rectangular, or cylindrical. It then correlates the identified shapes with myographic signals to determine the appropriate grip type for a bionic hand prosthesis, enabling real-time interaction with the environment.

## Algorithm

**Input:** Digital images of objects (240x240 pixels)

**Output:** Identified object shape, grip type, coordinates of the object, and dimensions in the X and Y planes.

**Steps:**

1. 1. Capture images of objects using the ESP32-CAM.
2. 2. Preprocess images to standardize size and format.
3. 3. Feed images into the MobileNetV2 neural network.
4. 4. Classify the object shape into predefined categories (spherical, rectangular, cylindrical).
5. 5. Analyze myographic signals to determine user intent.
6. 6. Match identified shape with appropriate grip type.
7. 7. Execute grip type based on the classification results.

**Core Operation:** `output = MobileNetV2(image)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.005 | A higher learning rate may speed up training but risk overshooting the optimal solution. |
| `epochs` | 30 | More epochs can improve accuracy but may lead to overfitting. |
| `width_factor (kw)` | 0.35 | Adjusting this affects the model's complexity and performance. |
| `image_size` | 240x240 pixels | Changing image size can impact processing time and accuracy. |

## Complexity

- **Time:** O(n)
- **Space:** O(m)
- **In practice:** Processing time is approximately 2 ms per image.

## Implementation

```python
def fomo_classification(image: np.ndarray) -> Tuple[str, str, Tuple[float, float]]:
    processed_image = preprocess(image)
    shape = MobileNetV2(processed_image)
    grip_type = determine_grip(shape)
    coordinates = get_coordinates(image)
    return shape, grip_type, coordinates
```

## Common Mistakes

- Neglecting to preprocess images correctly, leading to poor classification.
- Using an inappropriate learning rate that affects model convergence.
- Overfitting the model by training for too many epochs without validation.

## Use When

- Developing low-cost bionic prostheses that require object shape recognition.
- Integrating machine learning for real-time object identification in prosthetic devices.
- Enhancing user experience in prosthetics through improved grip type accuracy.

## Avoid When

- High precision is required beyond the capabilities of the proposed method.
- Complex object shapes that exceed the training dataset's scope.
- When additional computational resources are available for more complex algorithms.

## Tradeoffs

**Strengths:**

- Fast processing time suitable for real-time applications.
- Lightweight model architecture allows deployment on low-cost hardware.
- Good accuracy for predefined object shapes.

**Weaknesses:**

- Limited to specific object shapes defined in the training dataset.
- May not perform well with complex or irregular shapes.
- Requires careful tuning of parameters for optimal performance.

**Compared To:**

- **vs YOLOv5:** Use YOLOv5 for more complex object detection tasks requiring higher precision.
- **vs Deep SORT:** Use Deep SORT for tracking multiple objects in video streams.

## Connects To

- Transfer Learning
- Image Preprocessing Techniques
- Myoelectric Control Systems
- Real-time Object Detection Algorithms

## Evidence (Papers)

- **Spatial identification of manipulable objects for a bionic hand prosthesis** - [DOI](https://doi.org/10.35784/acs_6867)
