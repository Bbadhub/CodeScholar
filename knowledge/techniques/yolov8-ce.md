# YOLOv8-CE

*Also known as: You Only Look Once version 8 with Coordinate Attention*

**YOLOv8-CE is a real-time object detection model optimized for detecting small traffic signs in autonomous vehicles.**

**Category:** neural_architecture  
**Maturity:** proven

## How It Works

YOLOv8-CE enhances the YOLOv8 architecture by integrating Coordinate Attention to improve localization and using EIoU for better regression accuracy. It processes input images through data augmentation techniques and extracts features using a backbone network. The model employs a decoupled head for classification and detection, and utilizes Focal Loss to effectively handle sample difficulty, particularly for small objects.

## Algorithm

**Input:** 640x640 pixel images of traffic signs

**Output:** Predicted bounding boxes and class labels for detected traffic signs

**Steps:**

1. 1. Input images are processed using data augmentation techniques like Mosaic and MixUp.
2. 2. The backbone network extracts features using Conv, C2f, and SPPF modules.
3. 3. Coordinate Attention is applied to enhance localization capabilities.
4. 4. The neck fuses features at different scales using FPN and PANet.
5. 5. The head uses a decoupled structure for classification and detection.
6. 6. The EIoU loss function is used for regression.
7. 7. The model is trained and evaluated on the CCTSDB dataset.

**Core Operation:** `output = predicted bounding boxes and class labels`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.01 | Higher values may lead to faster convergence but risk overshooting minima. |
| `batch_size` | 16 | Larger batch sizes can stabilize training but require more memory. |
| `weight_decay` | 0.0005 | Increases regularization to prevent overfitting. |
| `epochs` | 300 | More epochs can improve accuracy but may lead to overfitting. |

## Complexity

- **Time:** O(n)
- **Space:** O(n)
- **In practice:** Real-world performance is optimized for real-time applications with an inference time of 96 ms.

## Implementation

```python
def yolo_v8_ce(input_image: np.ndarray) -> Tuple[np.ndarray, List[str]]:
    # Step 1: Data augmentation
    augmented_image = data_augmentation(input_image)
    # Step 2: Feature extraction
    features = backbone_network(augmented_image)
    # Step 3: Apply Coordinate Attention
    localized_features = coordinate_attention(features)
    # Step 4: Feature fusion
    fused_features = feature_fusion(localized_features)
    # Step 5: Detection head
    predictions = detection_head(fused_features)
    return predictions.bounding_boxes, predictions.class_labels
```

## Common Mistakes

- Neglecting data augmentation, which can lead to poor performance on small objects.
- Using inappropriate learning rates that can cause instability in training.
- Failing to properly tune the EIoU loss function for regression tasks.

## Use When

- You need to detect small objects in real-time.
- You are working on an autonomous vehicle project.
- You require a model that performs well under varying environmental conditions.

## Avoid When

- You have access to high-end computing resources and can afford larger models.
- The application does not require real-time performance.
- You are working with very large images that exceed the model's input size.

## Tradeoffs

**Strengths:**

- High accuracy in detecting small traffic signs.
- Real-time performance suitable for autonomous applications.
- Robustness to varying environmental conditions.

**Weaknesses:**

- May not perform as well on larger objects.
- Requires careful tuning of hyperparameters.
- Limited to the input size of 640x640 pixels.

**Compared To:**

- **vs YOLOv8:** YOLOv8-CE is preferable for small object detection, while YOLOv8 may be better for larger objects.

## Connects To

- YOLOv8
- Focal Loss
- Coordinate Attention
- EIoU
- Feature Pyramid Networks (FPN)
- Path Aggregation Network (PANet)

## Evidence (Papers)

- **A YOLOv8-CE-based real-time traffic sign detection and identification method for autonomous vehicles** [2 citations] - [DOI](https://doi.org/10.48130/dts-0024-0009)
