# Optimized Edge-Cloud System for Activity Monitoring Using Knowledge Distillation

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/electronics13234786` |
| Full Paper | [https://doi.org/10.3390/electronics13234786](https://doi.org/10.3390/electronics13234786) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/955ac4e036489f5a32d0905d03482225ef390ffd](https://www.semanticscholar.org/paper/955ac4e036489f5a32d0905d03482225ef390ffd) |
| Source | [https://journalclub.io/episodes/optimized-edge-cloud-system-for-activity-monitoring-using-knowledge-distillation](https://journalclub.io/episodes/optimized-edge-cloud-system-for-activity-monitoring-using-knowledge-distillation) |
| Source | [https://www.semanticscholar.org/paper/955ac4e036489f5a32d0905d03482225ef390ffd](https://www.semanticscholar.org/paper/955ac4e036489f5a32d0905d03482225ef390ffd) |
| Year | 2026 |
| Citations | 2 |
| Authors | Daniel Deniz, Eduardo Ros, E.M. Ortigosa, Francisco Barranco |
| Paper ID | `37a3a8b1-e69e-4738-af66-15aabe11275f` |

## Classification

- **Problem Type:** human activity recognition
- **Domain:** Machine Learning & AI
- **Sub-domain:** Deep Learning, Activity Recognition
- **Technique:** Knowledge Distillation
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents an optimized edge-cloud system for indoor activity monitoring using knowledge distillation to deploy lightweight models on resource-constrained edge devices. Engineers should care because this approach enhances action recognition performance while minimizing resource usage, making it suitable for real-time applications in healthcare settings.

## Key Contribution

**The optimization of deep learning models via knowledge distillation for efficient edge processing in resource-limited environments.**

## Problem

The need for efficient monitoring of residents in long-term care facilities to improve safety and response times in critical situations like falls.

## Method

**Approach:** The method involves training a complex teacher model to learn from video data and then transferring its knowledge to a simpler student model using knowledge distillation. This allows the student model to achieve high accuracy while being computationally efficient for deployment on edge devices.

**Algorithm:**

1. 1. Prepare the dataset with augmented input data.
2. 2. Train the teacher model on the full-resolution data.
3. 3. Train the student model on downsampled data.
4. 4. Compute the distillation loss using Kullback–Leibler divergence.
5. 5. Compute the cross-entropy loss for the student model.
6. 6. Combine the losses to form the global loss and backpropagate.

**Input:** Video streams of indoor activities, augmented with operations like random rotation, resizing, or cropping.

**Output:** Predictions of actions performed by individuals in the video streams.

**Key Parameters:**

- `temperature: τ ∈ [1, 9]`
- `distillation weight: λ = 0.1`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Indoor Action Dataset

**Results:**

- Recognition performance improvement: up to 8%

**Compared against:** S3DG Distilled Network

**Improvement:** Achieved real-time performance for action recognition at up to 250 fps.

## Implementation Guide

**Data Structures:** Video streams, Model architectures (Teacher and Student)

**Dependencies:** TensorFlow or PyTorch for model training, ThingsBoard for QRM tool

**Core Operation:**

```python
student_model.train(data) with loss = (1 - λ) * KL_divergence(teacher_output, student_output) + λ * cross_entropy(student_output, true_labels)
```

**Watch Out For:**

- Ensure the teacher model is well-trained before distillation.
- Monitor the temperature parameter closely for optimal performance.
- Be aware of the trade-off between input resolution and model accuracy.

## Use This When

- Deploying AI models on resource-constrained edge devices.
- Real-time monitoring of activities in healthcare settings.
- Optimizing deep learning models for efficiency without significant accuracy loss.

## Don't Use When

- High computational resources are available for model training and inference.
- The application does not require real-time processing.
- The dataset is not suitable for knowledge distillation techniques.

## Key Concepts

Knowledge Distillation, Edge Computing, Deep Learning, Activity Recognition, Quality and Resource Management

## Connects To

- Model Compression Techniques
- Real-time Video Processing
- Distributed Systems for Edge Computing

## Prerequisites

- Understanding of deep learning architectures.
- Familiarity with knowledge distillation concepts.
- Experience with edge computing frameworks.

## Limitations

- Performance may degrade if the student model is too simplified.
- Requires careful tuning of parameters for optimal results.
- Limited to scenarios where real-time processing is critical.

## Open Questions

- How can the approach be adapted for different types of actions or environments?
- What are the implications of using different architectures for the teacher model?

## Abstract

The complexity came mostly in step 2: Getting low-power edge nodes to run lightweight models. Deploying models on edge devices like NVIDIA Jetson Nano, which have limited GPU cores and memory, is challenging. Modern deep learning and CV architectures often involve millions or even billions of parameters, and they need to perform 3D convolutional operations to extract spatial and temporal features from video frames. This is necessary for accurate action recognition, but it requires substantial memory and processing capabilities. To make this possible in a resource-constrained environment, the authors applied Knowledge Distillation, a model compression technique that creates smaller, more efficient models while preserving much of the predictive accuracy of larger, more complex models. In this process
