# A YOLOv8-CE-based real-time traffic sign detection and identification method for autonomous vehicles

## Access

| Field | Value |
|-------|-------|
| DOI | `10.48130/dts-0024-0009` |
| Full Paper | [https://doi.org/10.48130/dts-0024-0009](https://doi.org/10.48130/dts-0024-0009) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/03c47dc0471020cf8efb21fd9343456c9cff22fc](https://www.semanticscholar.org/paper/03c47dc0471020cf8efb21fd9343456c9cff22fc) |
| Source | [https://journalclub.io/episodes/a-yolov8-ce-based-real-time-traffic-sign-detection-and-identification-method-for-autonomous-vehicles](https://journalclub.io/episodes/a-yolov8-ce-based-real-time-traffic-sign-detection-and-identification-method-for-autonomous-vehicles) |
| Source | [https://www.semanticscholar.org/paper/03c47dc0471020cf8efb21fd9343456c9cff22fc](https://www.semanticscholar.org/paper/03c47dc0471020cf8efb21fd9343456c9cff22fc) |
| Year | 2026 |
| Citations | 2 |
| Authors | Yuechen Luo, Yusheng Ci, Hexin Zhang, Lina Wu |
| Paper ID | `8c1991f8-0dad-4023-ae23-0679897bdcaa` |

## Classification

- **Problem Type:** object detection
- **Domain:** Machine Learning & AI
- **Sub-domain:** Object Detection
- **Technique:** YOLOv8-CE
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents an improved YOLOv8 model, named YOLOv8-CE, for real-time traffic sign detection and identification in autonomous vehicles. It enhances detection accuracy and speed under various environmental conditions, making it suitable for deployment on low-end embedded platforms like the Jetson Nano.

## Key Contribution

**Introduction of Coordinate Attention and EIoU loss function to enhance the YOLOv8 model for better traffic sign detection performance.**

## Problem

The challenge of accurately detecting and identifying traffic signs in real-time under varying environmental conditions.

## Method

**Approach:** The YOLOv8-CE model integrates Coordinate Attention into the backbone for improved localization and EIoU for enhanced regression accuracy. It employs Focal Loss to balance sample difficulty, leading to better performance in detecting small traffic signs.

**Algorithm:**

1. 1. Input images are processed using data augmentation techniques like Mosaic and MixUp.
2. 2. The backbone network extracts features using Conv, C2f, and SPPF modules.
3. 3. Coordinate Attention is applied to enhance localization capabilities.
4. 4. The neck fuses features at different scales using FPN and PANet.
5. 5. The head uses a decoupled structure for classification and detection.
6. 6. The EIoU loss function is used for regression.
7. 7. The model is trained and evaluated on the CCTSDB dataset.

**Input:** 640x640 pixel images of traffic signs.

**Output:** Predicted bounding boxes and class labels for detected traffic signs.

**Key Parameters:**

- `learning_rate: 0.01`
- `batch_size: 16`
- `weight_decay: 0.0005`
- `epochs: 300`

**Complexity:** not stated

## Benchmarks

**Tested on:** CCTSDB dataset

**Results:**

- mAP: 86.1%
- Inference Time: 96 ms

**Compared against:** YOLOv8n, Raspberry Pi 4B

**Improvement:** 2.8% improvement in mAP over YOLOv8.

## Implementation Guide

**Data Structures:** Tensor for image data, Arrays for bounding box coordinates

**Dependencies:** PyTorch, CUDA, TensorRT

**Core Operation:**

```python
model.predict(image) returns bounding boxes and class labels.
```

**Watch Out For:**

- Ensure input images are correctly resized to 640x640.
- Monitor the inference time on embedded devices to ensure real-time performance.
- Adjust learning rate and batch size based on available hardware.

## Use This When

- You need to detect small objects in real-time.
- You are working on an autonomous vehicle project.
- You require a model that performs well under varying environmental conditions.

## Don't Use When

- You have access to high-end computing resources and can afford larger models.
- The application does not require real-time performance.
- You are working with very large images that exceed the model's input size.

## Key Concepts

Coordinate Attention, EIoU, Focal Loss, YOLOv8, real-time detection, traffic sign identification

## Connects To

- YOLOv8
- Focal Loss
- EIoU
- Coordinate Attention
- TensorRT

## Prerequisites

- Understanding of convolutional neural networks
- Familiarity with object detection algorithms
- Knowledge of loss functions in deep learning

## Limitations

- Performance may degrade in extremely adverse weather conditions
- Model size and complexity may limit deployment on very low-end devices
- Requires careful tuning of hyperparameters for optimal performance

## Open Questions

- How can the model be further optimized for even lower latency?
- What additional data augmentation techniques could improve robustness?

## Abstract

Previous generations of traffic sign detection methods, especially those relying on traditional machine vision techniques like color thresholding or shape analysis, fail almost completely under variable real-world conditions. Even modern deep learning models struggle. When the environment degrades, or when the signs are too small relative to the input resolution, detection confidence collapses. Worse, the latency of a full YOLOv8 pipeline, even in its smallest variant, is often outside the margin of what is acceptable on a low-end embedded platform without heavy optimization. All of this creates a hard technical bottleneck. You need a model that can not just classify but also localize small objects precisely and do it fast. You need robustness across weather, lighting, and motion artifacts. And you need to achieve all of that without blowing through your compute or energy budgets. Enter YOLOv8n. "n" stands for "nano". It is the smallest
