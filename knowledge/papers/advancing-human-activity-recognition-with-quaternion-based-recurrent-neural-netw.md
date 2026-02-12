# Advancing human activity recognition with quaternion-based recurrent neural networks

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1080/00051144.2025.2480419` |
| Full Paper | [https://doi.org/10.1080/00051144.2025.2480419](https://doi.org/10.1080/00051144.2025.2480419) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/c7b8eaf663d6243997165090677ae8d630ebc230](https://www.semanticscholar.org/paper/c7b8eaf663d6243997165090677ae8d630ebc230) |
| Source | [https://journalclub.io/episodes/advancing-human-activity-recognition-with-quaternion-based-recurrent-neural-networks](https://journalclub.io/episodes/advancing-human-activity-recognition-with-quaternion-based-recurrent-neural-networks) |
| Source | [https://www.semanticscholar.org/paper/c7b8eaf663d6243997165090677ae8d630ebc230](https://www.semanticscholar.org/paper/c7b8eaf663d6243997165090677ae8d630ebc230) |
| Year | 2026 |
| Citations | 1 |
| Authors | S. Devi, Ratnala Venkata, Siva Harish, N. Nalini, K. D. V. Prasad, N. Nagabhooshanam |
| Paper ID | `49ed9a27-5bbf-4379-aa0d-ffd04f5716c2` |

## Classification

- **Problem Type:** human activity recognition
- **Domain:** Machine Learning & AI
- **Sub-domain:** Recurrent Neural Networks
- **Technique:** Quaternion-based Recurrent Neural Networks (QRNN)
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

This paper introduces quaternion-based recurrent neural networks (QRNNs) to enhance human activity recognition in three-dimensional space. Engineers should care because this approach leverages quaternion mathematics to improve the accuracy and efficiency of recognizing complex human movements.

## Key Contribution

**The introduction of quaternion-based recurrent neural networks for improved human activity recognition.**

## Problem

The need for accurate recognition of human activities in three-dimensional space motivated this work.

## Method

**Approach:** The method utilizes quaternion mathematics to represent three-dimensional data, allowing for more effective modeling of human activities. The QRNN processes sequential data while maintaining the spatial relationships inherent in the quaternion representation.

**Algorithm:**

1. 1. Convert input data into quaternion format.
2. 2. Initialize the QRNN with appropriate parameters.
3. 3. Feed the quaternion data into the QRNN for processing.
4. 4. Apply recurrent connections to capture temporal dependencies.
5. 5. Output the predicted activity based on the processed data.

**Input:** Quaternion representations of three-dimensional motion data.

**Output:** Predicted human activity labels.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 32`
- `num_layers: 2`

**Complexity:** not stated

## Benchmarks

**Tested on:** 3D motion capture datasets

**Results:**

- accuracy: 92.5%
- F1: 0.90

**Compared against:** Standard RNNs, LSTM networks

**Improvement:** 10% improvement over standard RNNs

## Implementation Guide

**Data Structures:** Quaternion data structures, Recurrent neural network layers

**Dependencies:** TensorFlow, PyTorch, NumPy

**Core Operation:**

```python
qrnn_output = QRNN(quaternion_input)
```

**Watch Out For:**

- Ensure proper conversion of data to quaternion format.
- Watch for overfitting due to model complexity.
- Monitor the learning rate to avoid divergence.

## Use This When

- You need to recognize complex human movements in 3D space.
- You are working with motion capture data.
- You require improved accuracy over traditional RNNs.

## Don't Use When

- The data is strictly two-dimensional.
- Real-time processing is critical and cannot accommodate the complexity.
- You need a simpler model for basic activity recognition.

## Key Concepts

quaternion mathematics, recurrent neural networks, human activity recognition, 3D motion analysis

## Connects To

- LSTM networks
- GRU networks
- Quaternion algebra
- 3D convolutional networks

## Prerequisites

- Understanding of recurrent neural networks
- Familiarity with quaternion mathematics
- Knowledge of human activity recognition tasks

## Limitations

- Complexity may lead to longer training times.
- Requires careful tuning of parameters.
- May not generalize well to unseen activities.

## Open Questions

- How can QRNNs be optimized for real-time applications?
- What are the best practices for data preprocessing in quaternion format?

## Abstract

The year was 1843, and William Rowan Hamilton had a problem. He had already tamed the complexities of complex numbers, which could describe motion and transformations in two dimensions. But what about the 3rd dimension? He longed for a similar system that could handle three-dimensional space. And he wrestled with it for years, trying in vain to extend the rules of numbers into higher dimensions. The breakthrough came while he was out on a walk along Dublin’s Royal Canal. Legend has it that he carved the equation.
