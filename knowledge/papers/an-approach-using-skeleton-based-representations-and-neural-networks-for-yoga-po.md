# An Approach using Skeleton-based Representations and Neural Networks for Yoga Pose Recognition

## Access

| Field | Value |
|-------|-------|
| DOI | `10.2478/acss-2025-0009` |
| Full Paper | [https://doi.org/10.2478/acss-2025-0009](https://doi.org/10.2478/acss-2025-0009) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/4836ca255f6ac1a54906435b1179c9a3ed2f54f5](https://www.semanticscholar.org/paper/4836ca255f6ac1a54906435b1179c9a3ed2f54f5) |
| Source | [https://journalclub.io/episodes/an-approach-using-skeleton-based-representations-and-neural-networks-for-yoga-pose-recognition](https://journalclub.io/episodes/an-approach-using-skeleton-based-representations-and-neural-networks-for-yoga-pose-recognition) |
| Source | [https://www.semanticscholar.org/paper/4836ca255f6ac1a54906435b1179c9a3ed2f54f5](https://www.semanticscholar.org/paper/4836ca255f6ac1a54906435b1179c9a3ed2f54f5) |
| Year | 2026 |
| Citations | 0 |
| Authors | H. T. Nguyen, Nguyen Nhat Truong, L. Pham, Ngoc Huynh Pham |
| Paper ID | `82d3abfb-608b-41d9-a329-245c9f735ac9` |

## Classification

- **Problem Type:** pose recognition
- **Domain:** Machine Learning & AI
- **Sub-domain:** Pose Recognition
- **Technique:** FNN1D and Conv1D
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a method for recognizing yoga poses using skeleton-based representations extracted from images via the MoveNet model, achieving high accuracy with neural networks. Engineers should care because this approach can be implemented to create smart virtual trainers for yoga practice, enhancing user experience and safety.

## Key Contribution

**The integration of MoveNet for skeleton extraction and the development of FNN1D and Conv1D models for yoga pose classification.**

## Problem

The need for accurate yoga pose recognition to prevent injuries and enhance the effectiveness of home workouts.

## Method

**Approach:** The method uses MoveNet to extract skeletal keypoints from images, which are then fed into either a Feedforward Neural Network (FNN) or a Convolutional Neural Network (CNN) for classification of yoga poses. The models are trained on a dataset of skeletal representations to achieve high accuracy.

**Algorithm:**

1. 1. Collect images of yoga poses.
2. 2. Use MoveNet to extract skeletal keypoints from images.
3. 3. Preprocess the keypoints into a feature vector.
4. 4. Train the FNN1D or Conv1D model using the feature vectors.
5. 5. Evaluate the model's performance using metrics like accuracy, precision, recall, and F1-score.
6. 6. Deploy the model in a web application for real-time yoga pose recognition.

**Input:** Images of yoga poses in .jpg or .png format, which are converted to skeletal data.

**Output:** Predicted yoga pose labels corresponding to the input images.

**Key Parameters:**

- `learning_rate: 0.0005`
- `batch_size: 32`
- `epochs: 80`
- `dropout_rate: 0.2`

**Complexity:** not stated

## Benchmarks

**Tested on:** Custom dataset of 3939 images of 10 yoga poses

**Results:**

- Accuracy: 97.68% for FNN1D, 98.13% for Conv1D
- Precision, Recall, F1-score (exact values not stated)

**Compared against:** Previous models using different architectures like VGG16, ResNet

**Improvement:** Conv1D model achieved 0.98135 accuracy, outperforming baseline models.

## Implementation Guide

**Data Structures:** 1D arrays for skeletal keypoints, CSV files for storing extracted features

**Dependencies:** TensorFlow, Flask, HTML/CSS/JavaScript for web interface

**Core Operation:**

```python
skeleton_data = MoveNet(image); pose = Conv1D(skeleton_data)
```

**Watch Out For:**

- Ensure images are clear and contain detectable skeletons.
- Monitor for overfitting during model training.
- Optimize the model for different hardware capabilities.

## Use This When

- Building applications for yoga pose recognition.
- Creating virtual trainers for fitness applications.
- Developing systems that require real-time human pose analysis.

## Don't Use When

- Working with non-human poses or actions.
- When RGB image data is preferred over skeletal data.
- In scenarios requiring 3D pose recognition.

## Key Concepts

skeleton extraction, pose recognition, neural networks, MoveNet, FNN, CNN, data preprocessing

## Connects To

- PoseNet
- OpenPose
- 3D CNN architectures
- Transfer Learning techniques

## Prerequisites

- Understanding of neural networks
- Familiarity with image processing
- Knowledge of web development

## Limitations

- Dependent on the quality of input images
- Limited to the poses included in the training dataset
- May require significant computational resources for real-time processing

## Open Questions

- How can the model be adapted for more complex yoga poses?
- What additional features could enhance user interaction in the application?

## Abstract

Their pipeline begins with a clear decision: strip away everything that doesn’t help the model reason about human pose. That means discarding RGB pixel information and focusing solely on skeletal keypoints. To do that, the authors rely on MoveNet, a real-time pose estimation model developed by Google Research. It detects 17 anatomical landmarks per frame, each consisting of x and y coordinates, along with a confidence score. These keypoints correspond to major joints like the wrists, elbows, shoulders, hips, knees, and ankles.
