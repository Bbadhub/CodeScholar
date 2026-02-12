# A comparative study of neural network pruning strategies for industrial applications

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fcomp.2025.1563942` |
| Full Paper | [https://doi.org/10.3389/fcomp.2025.1563942](https://doi.org/10.3389/fcomp.2025.1563942) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/1376fd37d4d882a4abc83f0ad15ec45efc397dcb](https://www.semanticscholar.org/paper/1376fd37d4d882a4abc83f0ad15ec45efc397dcb) |
| Source | [https://journalclub.io/episodes/a-comparative-study-of-neural-network-pruning-strategies-for-industrial-applications](https://journalclub.io/episodes/a-comparative-study-of-neural-network-pruning-strategies-for-industrial-applications) |
| Source | [https://www.semanticscholar.org/paper/1376fd37d4d882a4abc83f0ad15ec45efc397dcb](https://www.semanticscholar.org/paper/1376fd37d4d882a4abc83f0ad15ec45efc397dcb) |
| Year | 2026 |
| Citations | 1 |
| Authors | Amirhossein Douzandeh Zenoozi, L. Erhan, A. Liotta, Lucia Cavallaro |
| Paper ID | `ff66e6af-249b-49a1-a305-0212717c6b20` |

## Classification

- **Problem Type:** model compression and optimization
- **Domain:** Machine Learning & AI
- **Sub-domain:** Neural Network Pruning
- **Technique:** Neural Network Pruning
- **Technique Category:** optimization_algorithm
- **Type:** comparison

## Summary

This paper presents a comparative study of various neural network pruning strategies aimed at optimizing models for industrial applications, particularly in resource-constrained environments. Engineers should care because the findings demonstrate that pruning techniques can significantly reduce model size and energy consumption while maintaining accuracy, making them suitable for deployment on edge devices.

## Key Contribution

**The introduction of a systematic comparison of Pre-Training, In-Training, Post-Training, and SET pruning methods applied to VGG16 and ResNet18 architectures for industrial applications.**

## Problem

The need to deploy deep learning models on resource-constrained edge devices in industrial settings motivated this work.

## Method

**Approach:** The method involves applying different pruning strategies to neural networks to reduce the number of active weights, thereby creating sparser models. These strategies include Pre-Training, In-Training, Post-Training, and SET, each with distinct mechanisms for identifying and removing less important connections.

**Algorithm:**

1. 1. Initialize the neural network with dense weights.
2. 2. Apply the chosen pruning method (Pre-Training, In-Training, Post-Training, or SET).
3. 3. For Pre-Training, calculate L1 norms and prune the weakest connections before training.
4. 4. For In-Training, prune the weakest connections after each epoch and replace them with random connections.
5. 5. For Post-Training, prune the weakest connections after the model has been fully trained.
6. 6. For SET, initialize using the Erdös-Rényi model and dynamically adjust connections during training.
7. 7. Evaluate the model's performance based on accuracy, inference time, and energy consumption.

**Input:** Training data in the form of labeled images for classification or anomaly detection tasks.

**Output:** A pruned neural network model with reduced size and optimized performance metrics.

**Key Parameters:**

- `sparsity_level: 50% for convolutional layers, 80% for linear layers`
- `epochs: variable depending on training setup`
- `learning_rate: not specified`

**Complexity:** Not stated

## Benchmarks

**Tested on:** BloodMNIST, VisA, MVTec 3D Object Classification

**Results:**

- accuracy: VGG16 (Dense: 94.85%, Sparse: 92.4%), ResNet18 (Dense: 91.93%, Sparse: 92.3%)
- inference time: not specified
- energy consumption: not specified

**Compared against:** Dense VGG16 and ResNet18 models

**Improvement:** Achieved comparable accuracy levels with reduced inference time and energy consumption.

## Implementation Guide

**Data Structures:** Neural network layers (convolutional and linear), Weight matrices

**Dependencies:** PyTorch, TensorFlow

**Core Operation:**

```python
model = initialize_model(); prune_model(model, method='SET'); train_model(model, data)
```

**Watch Out For:**

- Ensure the chosen pruning method aligns with the specific application requirements.
- Monitor the model's performance closely after pruning to avoid overfitting.
- Consider the trade-off between sparsity and accuracy during the pruning process.

## Use This When

- Deploying deep learning models on edge devices with limited computational resources.
- Needing to reduce model size without significantly impacting accuracy.
- Optimizing energy consumption in industrial applications.

## Don't Use When

- Working with high-performance computing resources where model size is not a concern.
- When maximum accuracy is prioritized over model efficiency.
- In scenarios where real-time adaptability of the model is critical.

## Key Concepts

sparsity, L1 norm, Erdös-Rényi model, dynamic pruning, energy efficiency, edge computing

## Connects To

- L1 regularization
- Dropout techniques
- Model quantization

## Prerequisites

- Understanding of neural network architectures
- Familiarity with pruning techniques
- Knowledge of model evaluation metrics

## Limitations

- Pruning may lead to loss of important connections if not carefully managed.
- Some methods may require retraining the model, increasing overall training time.
- Performance may vary significantly based on the chosen pruning strategy.

## Open Questions

- How do different pruning methods impact the long-term performance of models in dynamic environments?
- What are the best practices for selecting the optimal sparsity level for various applications?

## Abstract

Pre-Training Pruning: This is what you’d expect if you’ve worked with static pruning or tried L1-based compression in PyTorch or TensorFlow. The model starts with a dense set of weights, then the weakest ones (measured using the L1 norm) are zeroed out before training begins. In their setup, this means computing the L1 magnitude of each connection in a layer, ranking them, and dropping the bottom X percent to hit a predefined sparsity level. It’s simple and deterministic. But once you kill a connection, it’s gone for good. You’re locking the sparsity structure in place before the model has had a chance to learn which pathways might end up being important. That tradeoff: less training overhead, but no flexibility, is a recurring theme across the other methods as well. In-Training Pruning: This method is more dynamic. The pruning process runs every epoch. After each round of backpropagation, the algorithm identifies the
