# YOLOv8n (Nano) and YOLOv8m (Medium)

*Also known as: You Only Look Once version 8 Nano, You Only Look Once version 8 Medium*

**YOLOv8n and YOLOv8m are lightweight deep learning models designed for real-time object detection, particularly in resource-constrained environments.**

**Category:** neural_architecture  
**Maturity:** proven

## How It Works

YOLOv8n is a smaller version of the YOLOv8m model, trained using knowledge distillation. The larger YOLOv8m model acts as a teacher, providing soft targets to the smaller YOLOv8n student model. This approach allows the smaller model to achieve competitive accuracy while being suitable for deployment on edge devices like Raspberry Pi.

## Algorithm

**Input:** Images of fire and non-fire scenarios (e.g., forest, vehicle, industrial, accidental, residential fires).

**Output:** Real-time detection of fire incidents with accuracy metrics.

**Steps:**

1. 1. Collect a comprehensive dataset of fire images.
2. 2. Train the YOLOv8m model as the teacher model on the dataset.
3. 3. Use the trained YOLOv8m to generate soft targets for the YOLOv8n student model.
4. 4. Train the YOLOv8n model using the soft targets from the teacher model.
5. 5. Deploy the YOLOv8n model on a Raspberry Pi 5 microcontroller.
6. 6. Integrate the model with a drone for real-time fire detection.

**Core Operation:** `output = YOLOv8n(image)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.01 | Higher values may lead to faster convergence but risk overshooting minima. |
| `batch_size` | 32 | Larger batch sizes can stabilize training but require more memory. |
| `epochs` | 50 | More epochs can improve accuracy but may lead to overfitting. |
| `IoU` | 0.7 for YOLOv8, 0.8 for DETR | Higher IoU thresholds can reduce false positives but may miss some detections. |
| `weight_decay` | 0.0005 for YOLOv8, 1 × 10^-4 for DETR | Increased weight decay can help prevent overfitting. |

## Complexity

- **Time:** O(n)
- **Space:** O(m)
- **In practice:** Real-world performance is highly dependent on the hardware used for deployment.

## Implementation

```python
def train_yolo_nano(teacher_model: Model, dataset: Dataset) -> Model:
    # Step 1: Train teacher model
    teacher_model.train(dataset)
    # Step 2: Generate soft targets
    soft_targets = teacher_model.predict(dataset)
    # Step 3: Train student model
    student_model = YOLOv8n()
    student_model.train(soft_targets)
    return student_model
```

## Common Mistakes

- Not properly tuning the learning rate, leading to poor convergence.
- Ignoring the importance of data augmentation for better generalization.
- Failing to validate the model on a separate dataset, risking overfitting.

## Use When

- You need to implement a fire detection system in remote areas.
- You require a lightweight model for deployment on edge devices.
- Real-time processing of visual data is essential for your application.

## Avoid When

- High computational resources are available for processing.
- The application does not require real-time detection.
- The environment is not constrained by power or processing limitations.

## Tradeoffs

**Strengths:**

- Lightweight and suitable for edge devices.
- High detection accuracy in real-time applications.
- Effective knowledge distillation improves performance.

**Weaknesses:**

- May not perform as well as larger models in complex scenarios.
- Limited by the computational power of edge devices.
- Requires careful tuning of hyperparameters.

**Compared To:**

- **vs DETR:** Use YOLOv8n for real-time applications with limited resources; use DETR for tasks requiring higher accuracy and computational resources.

## Connects To

- Knowledge Distillation
- Object Detection
- Real-Time Processing
- Edge Computing
- Deep Learning Frameworks

## Evidence (Papers)

- **Real-Time Fire Detection: Integrating Lightweight Deep Learning Models on Drones with Edge Computing** - [DOI](https://doi.org/10.3390/drones8090483)
