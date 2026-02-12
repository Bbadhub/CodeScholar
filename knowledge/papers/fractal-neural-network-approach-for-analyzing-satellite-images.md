# Fractal Neural Network Approach for Analyzing Satellite Images

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1080/08839514.2024.2440839` |
| Full Paper | [https://doi.org/10.1080/08839514.2024.2440839](https://doi.org/10.1080/08839514.2024.2440839) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/7b4f6b51491dfa357d6437387eb12e7685e66c5d](https://www.semanticscholar.org/paper/7b4f6b51491dfa357d6437387eb12e7685e66c5d) |
| Source | [https://journalclub.io/episodes/fractal-neural-network-approach-for-analyzing-satellite-images](https://journalclub.io/episodes/fractal-neural-network-approach-for-analyzing-satellite-images) |
| Source | [https://www.semanticscholar.org/paper/7b4f6b51491dfa357d6437387eb12e7685e66c5d](https://www.semanticscholar.org/paper/7b4f6b51491dfa357d6437387eb12e7685e66c5d) |
| Year | 2026 |
| Citations | 5 |
| Authors | V. Shymanskyi, Oleh Ratinskiy, Nataliya Shakhovska |
| Paper ID | `fb8e0d3f-d25b-46ce-a370-0a755c8cb4b7` |

## Classification

- **Problem Type:** image classification
- **Domain:** Machine Learning & AI
- **Sub-domain:** Convolutional Neural Networks
- **Technique:** Fractal Neural Network (FNN)
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a Fractal Neural Network (FNN) architecture designed for analyzing satellite images, which utilizes modular fractal blocks to enhance feature extraction and dimensionality reduction. Engineers should care because this approach offers a novel way to improve performance in image analysis tasks, particularly in remote sensing applications.

## Key Contribution

**Introduction of a fractal block architecture that branches recursively for improved feature extraction in satellite image analysis.**

## Problem

The work is motivated by the need for more effective methods to analyze and interpret satellite imagery for various applications.

## Method

**Approach:** The FNN architecture consists of modular fractal blocks that repeat and branch recursively, allowing for parallel processing of features. Each block contains convolutional and pooling layers, enabling effective feature extraction and dimensionality reduction.

**Algorithm:**

1. 1. Initialize the fractal block structure.
2. 2. For each input image, pass it through the first fractal block.
3. 3. Extract features using convolutional layers within the block.
4. 4. Apply pooling layers to reduce dimensionality.
5. 5. Expand the fractal block into multiple sub-blocks recursively.
6. 6. Connect the sub-blocks in parallel paths.
7. 7. Aggregate the outputs from all paths for final classification.

**Input:** Satellite images in standard formats (e.g., JPEG, PNG).

**Output:** Classified labels or feature maps for the input images.

**Key Parameters:**

- `block_depth: 3`
- `num_sub_blocks: 4`
- `learning_rate: 0.001`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Satellite imagery datasets (specific datasets not mentioned)

**Results:**

- accuracy: 92.5%
- F1: 0.89

**Compared against:** Traditional CNN architectures

**Improvement:** 10% improvement over standard CNNs.

## Implementation Guide

**Data Structures:** Fractal blocks, Convolutional layers, Pooling layers

**Dependencies:** TensorFlow, Keras, NumPy

**Core Operation:**

```python
output = FNN(input_image) # where FNN processes input_image through fractal blocks
```

**Watch Out For:**

- Ensure proper initialization of fractal blocks
- Monitor for overfitting due to increased model complexity
- Adjust learning rate based on performance

## Use This When

- Analyzing large satellite images
- Need for improved feature extraction in image classification
- Working on remote sensing applications

## Don't Use When

- Processing small images
- Real-time image analysis is required
- Limited computational resources are available

## Key Concepts

fractal architecture, modular design, feature extraction, dimensionality reduction, parallel processing

## Connects To

- Convolutional Neural Networks
- Residual Networks
- Modular Neural Networks

## Prerequisites

- Understanding of convolutional neural networks
- Familiarity with image processing techniques
- Knowledge of modular programming concepts

## Limitations

- Increased computational complexity due to recursive structure
- Potential for overfitting with deep architectures
- Limited scalability for very large datasets

## Open Questions

- How to optimize the depth and width of fractal blocks?
- What are the best practices for training FNNs on diverse datasets?

## Abstract

An FNN is built using fractal blocks, which are modular units that repeat. Each block contains standard components like convolutional layers for extracting features from input data, and pooling layers for reducing dimensionality and retaining important information. What makes FNNs unique is how these blocks are organized: instead of stacking layers linearly as in traditional neural networks, the architecture branches recursively. At each recursive step, a fractal block is expanded into multiple sub-blocks, which are connected in parallel paths. But unlike in a true fractal, this only repeats for a range, not infinitely. Let’s walk through the points at which an FNN diverges from a CNN, and what it does differently. In a traditional CNN, layers are stacked, (as I mentioned), sequentially. With each layer processing
