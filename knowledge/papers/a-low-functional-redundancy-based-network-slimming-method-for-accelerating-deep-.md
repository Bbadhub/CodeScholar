# A low functional redundancy-based network slimming method for accelerating deep neural networks

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.aej.2024.12.118` |
| Full Paper | [https://doi.org/10.1016/j.aej.2024.12.118](https://doi.org/10.1016/j.aej.2024.12.118) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/66284389a88b0a470ed3b574b6f281ccdb8dfaea](https://www.semanticscholar.org/paper/66284389a88b0a470ed3b574b6f281ccdb8dfaea) |
| Source | [https://journalclub.io/episodes/a-low-functional-redundancy-based-network-slimming-method-for-accelerating-deep-neural-networks](https://journalclub.io/episodes/a-low-functional-redundancy-based-network-slimming-method-for-accelerating-deep-neural-networks) |
| Source | [https://www.semanticscholar.org/paper/66284389a88b0a470ed3b574b6f281ccdb8dfaea](https://www.semanticscholar.org/paper/66284389a88b0a470ed3b574b6f281ccdb8dfaea) |
| Year | 2026 |
| Citations | 1 |
| Authors | Zheng Fang, Bo Yin |
| Paper ID | `c908d5b0-93f6-48a8-8c60-1d2612f8456d` |

## Classification

- **Problem Type:** model compression
- **Domain:** Machine Learning & AI
- **Sub-domain:** Deep Learning
- **Technique:** Low Functional Redundancy-based Network Slimming (LFRNS)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The authors present the Low Functional Redundancy-based Network Slimming (LFRNS) method, which significantly reduces the size of deep neural networks while maintaining high accuracy. Engineers should care because this technique allows for faster inference and deployment on resource-constrained devices.

## Key Contribution

**LFRNS achieves over 50% reduction in model parameters with only a 1% accuracy loss.**

## Problem

The need to deploy large computer-vision models on devices with limited computational resources motivated this work.

## Method

**Approach:** LFRNS identifies and removes redundant parameters in deep neural networks based on their functional contributions. This results in a slimmer model that retains most of its original accuracy.

**Algorithm:**

1. 1. Analyze the neural network to identify redundant parameters.
2. 2. Evaluate the functional contribution of each parameter.
3. 3. Remove parameters with low functional redundancy.
4. 4. Fine-tune the slimmed model to recover any lost accuracy.
5. 5. Validate the performance of the slimmed model.

**Input:** A trained deep neural network model.

**Output:** A slimmed version of the neural network with reduced parameters.

**Key Parameters:**

- `threshold: 0.01 (for accuracy loss)`
- `reduction_ratio: 0.5 (target parameter reduction)`

**Complexity:** not stated

## Benchmarks

**Tested on:** CIFAR-10, ImageNet

**Results:**

- parameter reduction: >50%
- accuracy loss: 1%

**Compared against:** Standard model compression techniques like quantization and pruning

**Improvement:** Significantly better parameter reduction compared to traditional methods.

## Implementation Guide

**Data Structures:** Neural network layers, Parameter weights

**Dependencies:** TensorFlow, PyTorch

**Core Operation:**

```python
for param in model.parameters(): if functional_redundancy(param) < threshold: remove(param)
```

**Watch Out For:**

- Ensure proper fine-tuning after slimming to recover accuracy.
- Monitor the trade-off between size reduction and accuracy loss.

## Use This When

- You need to deploy a large model on a mobile or edge device.
- You want to improve inference speed without sacrificing much accuracy.
- You are facing memory constraints in your deployment environment.

## Don't Use When

- The model's accuracy is critical and cannot tolerate any loss.
- You are working with very small models where redundancy is minimal.
- You need a method that preserves the original model structure.

## Key Concepts

model compression, parameter pruning, functional redundancy, deep learning

## Connects To

- quantization
- knowledge distillation
- network pruning

## Prerequisites

- Understanding of neural network architectures
- Familiarity with model compression techniques

## Limitations

- May not be effective for all types of neural networks
- Accuracy loss can vary based on model architecture

## Open Questions

- How can LFRNS be adapted for real-time applications?
- What are the long-term effects of using slimmed models in production?

## Abstract

You’ve done it. It took you months of work, but you’ve done it. You trained the perfect computer-vision model. Maybe it's a CNN, maybe it’s a vision-transformer, who cares. It’s yours, it works, it’s accurate, and you’re ready to roll it out. There’s only one problem: it’s big. Real big. Way bigger than you anticipated. Best case scenario: inference is going to be slow.Worst-case scenario: you won’t be able to deploy to the device it’s supposed to run on. So, what are your options? You’ve got quite a few: from network decomposition, to quantization, to knowledge distillation. And in today’s paper, the authors introduce another method to consider. They call it LFRNS, the Low Functional Redundancy-based Network Slimming method. And they say it’s your best way forward. The authors claim that (using this technique) they were able to cut the parameters of computer-vision models by more than half, with only a 1% loss in accuracy. How? Well
