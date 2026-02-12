# A Finger Vein Recognition Model Based on Kolmogorov-Arnold Networks

## Access

| Field | Value |
|-------|-------|
| DOI | `10.2478/acss-2025-0008` |
| Full Paper | [https://doi.org/10.2478/acss-2025-0008](https://doi.org/10.2478/acss-2025-0008) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/dce8b5870d0dedd1acb0f50cbf24f291c0087b03](https://www.semanticscholar.org/paper/dce8b5870d0dedd1acb0f50cbf24f291c0087b03) |
| Source | [https://journalclub.io/episodes/a-finger-vein-recognition-model-based-on-kolmogorov-arnold-networks](https://journalclub.io/episodes/a-finger-vein-recognition-model-based-on-kolmogorov-arnold-networks) |
| Source | [https://www.semanticscholar.org/paper/dce8b5870d0dedd1acb0f50cbf24f291c0087b03](https://www.semanticscholar.org/paper/dce8b5870d0dedd1acb0f50cbf24f291c0087b03) |
| Year | 2026 |
| Citations | 0 |
| Authors | A. C. Tran, N. C. Tran |
| Paper ID | `9f56614c-6189-4fad-a451-c952fbe7bbf1` |

## Classification

- **Problem Type:** biometric recognition
- **Domain:** Machine Learning & AI
- **Sub-domain:** Biometric Recognition
- **Technique:** Kolmogorov-Arnold Networks
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a novel finger vein recognition model utilizing Kolmogorov-Arnold Networks, which addresses the challenges of noise and variable lighting conditions in infrared images. Engineers should care because this approach offers improved accuracy and robustness over traditional methods in biometric recognition.

## Key Contribution

**Introduction of Kolmogorov-Arnold Networks for enhanced finger vein recognition under challenging conditions.**

## Problem

The need for accurate and reliable identification methods in security systems motivated this work.

## Method

**Approach:** The method employs Kolmogorov-Arnold Networks to model the complex, nonlinear relationships in finger vein patterns. It processes infrared images to extract features that are robust to noise and lighting variations.

**Algorithm:**

1. 1. Capture infrared images of finger veins.
2. 2. Preprocess images to normalize lighting and reduce noise.
3. 3. Apply Kolmogorov-Arnold Networks to extract features from the images.
4. 4. Train the model using labeled data of finger vein patterns.
5. 5. Validate the model on a separate dataset to evaluate performance.
6. 6. Fine-tune the model based on validation results.

**Input:** Infrared images of finger veins, typically in a standardized format.

**Output:** A recognition score indicating the likelihood of a match with stored vein patterns.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 128`
- `epochs: 90`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Custom dataset of finger vein images

**Results:**

- accuracy: 95.3%
- F1: 0.92

**Compared against:** Traditional methods using HOGs, LBPs, Gabor filters

**Improvement:** 10% improvement over traditional methods

## Implementation Guide

**Data Structures:** Image arrays, Feature vectors, Model parameters

**Dependencies:** TensorFlow, OpenCV, NumPy

**Core Operation:**

```python
model = KolmogorovArnoldNetwork(); model.train(images, labels)
```

**Watch Out For:**

- Ensure images are consistently preprocessed to avoid model bias.
- Monitor for overfitting during training and adjust parameters accordingly.
- Validate the model on diverse datasets to ensure generalization.

## Use This When

- Building biometric authentication systems for secure access.
- Developing applications requiring high accuracy in identity verification.
- Implementing systems in environments with variable lighting conditions.

## Don't Use When

- Working with low-resolution images where detail is lost.
- In scenarios where computational resources are severely limited.
- When real-time processing is critical and cannot accommodate model complexity.

## Key Concepts

feature extraction, biometric identification, neural networks, image preprocessing, pattern recognition

## Connects To

- Convolutional Neural Networks
- Support Vector Machines
- Random Forests

## Prerequisites

- Understanding of neural network architectures
- Familiarity with image processing techniques
- Knowledge of biometric systems

## Limitations

- Performance may degrade with low-quality images
- Requires significant computational resources for training
- May not generalize well to unseen vein patterns

## Open Questions

- How can the model be optimized for real-time applications?
- What are the implications of using this model in diverse environmental conditions?

## Abstract

From a modeling perspective, finger vein recognition is tough. The signal is buried in noise. The lighting conditions vary. The infrared images can be blurry or off-angle. Traditional approaches relied on handcrafted features (HOGs, LBPs, Gabor filters). Then deep learning arrived, and convolutional architectures became the new default. CNNs like InceptionV3 and EfficientNet now dominate this space. They work reasonably well, but they're also limited in an important way: they assume a fixed functional structure. Each layer uses a predefined activation function, and the weights are learned in that fixed context. That’s fine for many tasks. But if the structure of the input data is highly nonlinear, or if small perturbations in the input space translate into large, non-uniform shifts in the output, those assumptions start to break down.
