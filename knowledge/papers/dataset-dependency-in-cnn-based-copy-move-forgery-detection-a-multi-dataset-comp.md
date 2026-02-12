# Dataset Dependency in CNN-Based Copy-Move Forgery Detection: A Multi-Dataset Comparative Analysis

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/make7020054` |
| Full Paper | [https://doi.org/10.3390/make7020054](https://doi.org/10.3390/make7020054) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/2cdf178f05b12b7e8b12012d8006a2915620cae2](https://www.semanticscholar.org/paper/2cdf178f05b12b7e8b12012d8006a2915620cae2) |
| Source | [https://journalclub.io/episodes/dataset-dependency-in-cnn-based-copy-move-forgery-detection-a-multi-dataset-comparative-analysis](https://journalclub.io/episodes/dataset-dependency-in-cnn-based-copy-move-forgery-detection-a-multi-dataset-comparative-analysis) |
| Source | [https://www.semanticscholar.org/paper/2cdf178f05b12b7e8b12012d8006a2915620cae2](https://www.semanticscholar.org/paper/2cdf178f05b12b7e8b12012d8006a2915620cae2) |
| Year | 2026 |
| Citations | 12 |
| Authors | Potito Valle Dell’Olmo, Oleksandr Kuznetsov, Emanuele Frontoni, M. Arnesano, Christian Napoli, Cristian Randieri |
| Paper ID | `2d891b0e-22a5-4caa-8784-7ea079926392` |

## Classification

- **Problem Type:** copy-move forgery detection
- **Domain:** Computer Vision
- **Sub-domain:** Image Forensics
- **Technique:** CNN-based Copy-Move Forgery Detection
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

This paper presents a comparative analysis of a CNN-based approach for copy-move forgery detection across three datasets, highlighting the significant impact of dataset characteristics on model performance. Engineers should care because understanding these dependencies can lead to more robust and generalizable detection systems.

## Key Contribution

**A systematic evaluation of CNN performance in copy-move forgery detection across multiple datasets, revealing the influence of dataset characteristics on accuracy.**

## Problem

The need to detect manipulated images in various contexts, such as journalism and legal proceedings, where image integrity is crucial.

## Method

**Approach:** The method uses a convolutional neural network (CNN) to classify images as authentic or tampered. The CNN architecture consists of multiple convolutional layers followed by pooling and a dense output layer, designed to capture hierarchical features.

**Algorithm:**

1. 1. Input image is resized to 224x224 pixels.
2. 2. Pass the image through six convolutional layers with increasing filter counts (16, 32, 64, 128, 256, 512).
3. 3. Apply max-pooling after each convolutional layer with a pool size of 2x2.
4. 4. Use a global average pooling layer to reduce feature maps to single values.
5. 5. Pass the output to a dense layer with softmax activation for binary classification.

**Input:** Images resized to 224x224 pixels with pixel values normalized to [0, 1].

**Output:** Probability distributions between the classes: authentic images or tampered images.

**Key Parameters:**

- `learning_rate: 0.001 (reduced to 0.0005 in experiments)`
- `batch_size: 32`
- `L2_regularization_lambda: 0.0005`
- `dropout_rate: 0.10-0.15`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** CoMoFoD, Coverage, CASIA v2

**Results:**

- accuracy: 95.90% on CoMoFoD, 27.50% on Coverage

**Compared against:** Traditional block-matching algorithms, keypoint analysis

**Improvement:** Up to 2.5% accuracy increase on CASIA v2 with regularization techniques.

## Implementation Guide

**Data Structures:** Image arrays, CNN model architecture

**Dependencies:** TensorFlow or PyTorch for CNN implementation

**Core Operation:**

```python
model.fit(train_images, train_labels, epochs=100, batch_size=32)
```

**Watch Out For:**

- Ensure proper dataset balancing to avoid bias.
- Monitor for overfitting by comparing training and validation metrics.
- Adjust learning rates and regularization parameters based on dataset characteristics.

## Use This When

- You need to detect manipulated images in digital forensics.
- You are working with datasets of varying sizes and characteristics.
- You want to implement a CNN for binary image classification tasks.

## Don't Use When

- You have a very small dataset (e.g., less than 200 images).
- You require real-time processing with minimal computational resources.
- You are dealing with highly complex transformations that CNNs struggle to detect.

## Key Concepts

copy-move forgery, convolutional neural networks, data augmentation, regularization techniques, dataset dependency, image forensics

## Connects To

- Traditional block-matching algorithms
- Data augmentation techniques
- Other CNN architectures for image classification

## Prerequisites

- Understanding of CNN architectures
- Familiarity with image preprocessing techniques
- Knowledge of binary classification metrics

## Limitations

- Performance varies significantly across different datasets.
- Smaller datasets may lead to overfitting.
- Complex transformations can still evade detection.

## Open Questions

- How can CNNs be adapted to improve generalizability across diverse datasets?
- What additional regularization techniques could enhance performance on small datasets?

## Abstract

Block-matching works by dividing the image into overlapping blocks or segments, typically of a fixed size, and scanning for duplicated blocks across the image. The similarity between blocks is measured using the sum of squared differences (SSD) or normalized cross-correlation (NCC). For this technique, the chosen block size is everything. Large blocks might overlook small duplications, while smaller blocks can become computationally expensive and may lead to higher false-positive rates due to image noise or slight variations. Block-matching works a lot of the time, but it struggles with forgeries that involve complex transformations like scaling, rotation, or distortion, as these transformations disrupt the block uniformity that this technique relies upon.
