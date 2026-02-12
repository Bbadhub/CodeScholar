# Quotient Network-A Network Similar to ResNet but Learning Quotients

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/a17110521` |
| Full Paper | [https://doi.org/10.3390/a17110521](https://doi.org/10.3390/a17110521) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/df4c6863883d12d11cea4686bfd845df0d496107](https://www.semanticscholar.org/paper/df4c6863883d12d11cea4686bfd845df0d496107) |
| Source | [https://journalclub.io/episodes/quotient-network-a-network-similar-to-resnet-but-learning-quotients](https://journalclub.io/episodes/quotient-network-a-network-similar-to-resnet-but-learning-quotients) |
| Source | [https://www.semanticscholar.org/paper/df4c6863883d12d11cea4686bfd845df0d496107](https://www.semanticscholar.org/paper/df4c6863883d12d11cea4686bfd845df0d496107) |
| Year | 2026 |
| Citations | 1 |
| Authors | Peng Hui, Jiamuyang Zhao, Changxin Li, Qingzhen Zhu |
| Paper ID | `c31a5479-a67b-422d-861e-561634667f15` |

## Classification

- **Problem Type:** image classification
- **Domain:** Machine Learning & AI
- **Sub-domain:** Convolutional Neural Networks
- **Technique:** Quotient Network
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper introduces the Quotient Network, a novel variant of ResNet that learns by calculating the quotients between features instead of differences, addressing key limitations of ResNet. This approach allows for better utilization of feature size information and improves performance without increasing the number of parameters.

## Key Contribution

**The introduction of the Quotient Network, which learns the quotient of target features over existing features, enhancing the learning process in deep networks.**

## Problem

The work is motivated by the need to improve the learning efficiency and performance of deep convolutional neural networks, particularly ResNet, in image classification tasks.

## Method

**Approach:** The Quotient Network modifies the learning goal from learning the difference between features to learning the quotient of features. This is achieved by multiplying the old features by the learned quotient, allowing for better representation of feature relationships.

**Algorithm:**

1. 1. Initialize the network with the same architecture as ResNet.
2. 2. Replace residual modules with quotient modules that compute the quotient of new and old features.
3. 3. Apply a specially designed activation function to ensure values remain within a suitable range.
4. 4. Perform point-to-point multiplication of the old features by the learned quotient.
5. 5. Train the network using stochastic gradient descent with specified parameters.
6. 6. Validate and test the network on benchmark datasets.

**Input:** 32x32 RGB images from datasets like CIFAR10, CIFAR100, and SVHN.

**Output:** Predicted class probabilities for the input images.

**Key Parameters:**

- `learning_rate: 0.1 (initial), reduced by a factor of 10 at epochs 92 and 136`
- `batch_size: 128`
- `α values for activation function: 1.8 (44 layers), 1.7 (56 layers), 1.5 (110 layers)`

**Complexity:** not stated

## Benchmarks

**Tested on:** CIFAR10, CIFAR100, SVHN

**Results:**

- CIFAR10 accuracy: 92.78% (44 layers), 93.1% (56 layers), 93.44% (110 layers)
- SVHN accuracy: 96.17% (44 layers), 96.20% (56 layers), 96.12% (110 layers)
- CIFAR100 accuracy: 73.25% (44 layers), 73.53% (56 layers), 73.00% (110 layers)

**Compared against:** ResNet of corresponding layers

**Improvement:** 6% improvement in accuracy over ResNet in optimal results.

## Implementation Guide

**Data Structures:** Convolutional layers, Activation functions, Feature maps

**Dependencies:** TensorFlow or PyTorch for neural network implementation

**Core Operation:**

```python
output = H(x) * activate(x) where activate(x) = sigmoid(x - ln(α - 1)) * α
```

**Watch Out For:**

- Ensure the activation function is globally differentiable and bounded.
- Monitor for gradient explosion during training.
- Adjust α based on the number of layers to optimize performance.

## Use This When

- You need to improve the performance of deep CNNs for image classification tasks.
- You want to leverage the advantages of ResNet while addressing its limitations.
- You are working with datasets similar to CIFAR10, CIFAR100, or SVHN.

## Don't Use When

- You require a method that significantly reduces computational complexity.
- You are working with very small datasets where overfitting is a concern.
- You need a solution that does not involve modifying existing architectures.

## Key Concepts

quotient learning, residual learning, convolutional neural network, image classification, activation function design

## Connects To

- ResNet
- DenseNet
- Attention Mechanisms
- SENet

## Prerequisites

- Understanding of convolutional neural networks
- Familiarity with residual learning
- Knowledge of activation functions

## Limitations

- Increased computation time compared to ResNet due to point-by-point multiplication.
- Potential for gradient explosion if activation functions are not properly designed.
- Performance may vary based on the choice of activation function.

## Open Questions

- How can the Quotient Network be adapted for other types of data beyond image classification?
- What are the implications of using different activation functions on the performance of the Quotient Network?

## Abstract

In today’s paper, the authors propose a new concept: a new variant of ResNet that overcomes two key issues with that methodology. They’re calling their concept a “Quotient Network”. Where ResNet learns in part by calculating differences between old and new features, the Quotient Network learns by calculating the quotients between them instead. So rather than subtraction they’re doing division. Now, that probably makes no intuitive sense to you right now, and that’s ok. We’re about to change that.
