# A Comparison Between Single-Stage and Two-Stage 3D Tracking Algorithms for Greenhouse Robotics

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/s24227332` |
| Full Paper | [https://doi.org/10.3390/s24227332](https://doi.org/10.3390/s24227332) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/31cd6ed21f1d34f8f9793b47b8886bedb90eaf34](https://www.semanticscholar.org/paper/31cd6ed21f1d34f8f9793b47b8886bedb90eaf34) |
| Source | [https://journalclub.io/episodes/a-comparison-between-single-stage-and-two-stage-3d-tracking-algorithms-for-greenhouse-robotics](https://journalclub.io/episodes/a-comparison-between-single-stage-and-two-stage-3d-tracking-algorithms-for-greenhouse-robotics) |
| Source | [https://www.semanticscholar.org/paper/31cd6ed21f1d34f8f9793b47b8886bedb90eaf34](https://www.semanticscholar.org/paper/31cd6ed21f1d34f8f9793b47b8886bedb90eaf34) |
| Year | 2026 |
| Citations | 1 |
| Authors | David Rapado Rincon, A. K. Burusa, Eldert J. van Henten, Gert Kootstra |
| Paper ID | `f62c7d65-090c-4734-aac6-5301b57b889d` |

## Classification

- **Problem Type:** multi-object tracking
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Multi-Object Tracking
- **Technique:** MOT-DETR
- **Technique Category:** neural_architecture
- **Type:** comparison

## Summary

This paper compares two multi-object tracking (MOT) algorithms, 3D-SORT (a two-stage method) and MOT-DETR (a single-stage method), in the context of greenhouse robotics for tomato harvesting. The findings indicate that while 3D-SORT excels in object detection, MOT-DETR consistently outperforms it in overall tracking accuracy, particularly in complex scenarios with occlusions.

## Key Contribution

**The demonstration that single-stage MOT algorithms can outperform two-stage methods in tracking accuracy despite lower detection performance in complex environments.**

## Problem

The need for accurate detection and localization of tomatoes in a greenhouse environment for robotic harvesting amidst occlusions and varying viewpoints.

## Method

**Approach:** MOT-DETR processes color images and 3D point clouds simultaneously to detect objects and extract re-ID features in a single network inference. 3D-SORT first detects objects using a YOLOv8 network and then associates detected objects with previous detections using a Kalman filter.

**Algorithm:**

1. 1. For MOT-DETR, input a color image and point cloud.
2. 2. Extract features using ResNet34 for both inputs.
3. 3. Pass features to a transformer encoder-decoder.
4. 4. Predict bounding boxes and re-ID features.
5. 5. Use a Hungarian algorithm for data association.
6. 6. For 3D-SORT, detect objects using YOLOv8.
7. 7. Filter point cloud based on detected bounding boxes.
8. 8. Estimate 3D positions and perform data association using the Hungarian algorithm.

**Input:** Color images (960x540 pixels) and corresponding 3D point clouds.

**Output:** Detected object bounding boxes, classes, and re-ID features.

**Key Parameters:**

- `learning_rate: not stated`
- `number_of_training_images: 50,000 for MOT-DETR`
- `image_dimensions: 960x540`

**Complexity:** not stated

## Benchmarks

**Tested on:** Custom dataset from a tomato greenhouse with 5400 viewpoints

**Results:**

- HOTA: 71.66 (MOT-DETR, AP sequence)
- DetA: 79.89 (3D-SORT, AP sequence)
- AssA: 78.58 (MOT-DETR, AP sequence)
- LocA: 80.16 (MOT-DETR, AP sequence)
- MOTA: 88.09 (MOT-DETR, AP sequence)
- IDSW: 4.2 (MOT-DETR, AP sequence)

**Compared against:** 3D-SORT

**Improvement:** MOT-DETR outperformed 3D-SORT in tracking accuracy across all tests.

## Implementation Guide

**Data Structures:** Color images, 3D point clouds, Bounding boxes, Tracking IDs

**Dependencies:** YOLOv8, ResNet34, Transformer architecture

**Core Operation:**

```python
features = extract_features(image, point_cloud); predictions = transformer(features); associations = hungarian_algorithm(predictions);
```

**Watch Out For:**

- Ensure sufficient training data for MOT-DETR to avoid underfitting.
- Monitor occlusion levels in the environment to optimize tracking performance.
- Carefully tune the parameters of the Hungarian algorithm for optimal data association.

## Use This When

- Tracking multiple objects in complex environments with occlusions.
- Implementing robotic systems for agricultural applications.
- Needing a single-stage tracking solution that balances accuracy and complexity.

## Don't Use When

- High object detection accuracy is critical and must be prioritized.
- Limited training data is available for model training.
- Real-time processing with minimal computational resources is required.

## Key Concepts

multi-object tracking, active perception, Kalman filter, Hungarian algorithm, deep learning, transformers

## Connects To

- YOLOv8 for object detection
- Kalman filtering for state estimation
- FairMOT for comparison of tracking methods

## Prerequisites

- Understanding of multi-object tracking concepts
- Familiarity with deep learning frameworks
- Knowledge of Kalman filters and data association techniques

## Limitations

- MOT-DETR requires significantly more training data than two-stage methods.
- Performance may degrade in extremely cluttered environments.
- Complexity of implementation may be higher for single-stage methods.

## Open Questions

- How can the performance of single-stage methods be improved with less training data?
- What are the best practices for integrating active perception in various robotic applications?

## Abstract

Real-world farming isn’t as neat and simple as a library of images. Nature is unpredictable. No amount of training data will account for variables like lighting, position, and bunch size. These variations make it much harder for AI to identify the tomatoes accurately 100% of the time. And when you factor in the complexity of the plant’s structure into the mix, things get even messier. This is where Multi-Object Tracking (MOT) technology comes in. It’s a set of algorithms designed to track multiple objects while they, or the camera, are in motion. In MOT systems this is known as re-identification. Think of the technology that allows commentators to track each player on a football field during a game. While the human eye perceives this as smooth tracking, it’s actually a series of frames fed into an algorithm, along with their corresponding location within three-dimensional space. This 3D space is what’s known
