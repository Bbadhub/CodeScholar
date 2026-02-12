# Domain knowledge-based deterministic graph traversal method for white blood cell classification

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1088/2632-2153/adb126` |
| Full Paper | [https://doi.org/10.1088/2632-2153/adb126](https://doi.org/10.1088/2632-2153/adb126) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/8cfbcd9f23df736b5f652dca75f87abccf1d6b09](https://www.semanticscholar.org/paper/8cfbcd9f23df736b5f652dca75f87abccf1d6b09) |
| Source | [https://journalclub.io/episodes/domain-knowledge-based-deterministic-graph-traversal-method-for-white-blood-cell-classification](https://journalclub.io/episodes/domain-knowledge-based-deterministic-graph-traversal-method-for-white-blood-cell-classification) |
| Source | [https://www.semanticscholar.org/paper/8cfbcd9f23df736b5f652dca75f87abccf1d6b09](https://www.semanticscholar.org/paper/8cfbcd9f23df736b5f652dca75f87abccf1d6b09) |
| Year | 2026 |
| Citations | 1 |
| Authors | Jeneessha P, Vinoth Kumar Balasubramanian |
| Paper ID | `7fc4df35-73c7-459f-bb0b-b53d5ac1db20` |

## Classification

- **Problem Type:** classification
- **Domain:** Machine Learning & AI
- **Sub-domain:** Graph-based classification methods
- **Technique:** Deterministic Graph Traversal Method
- **Technique Category:** classification_model
- **Type:** novel

## Summary

The authors propose a deterministic graph traversal method for classifying white blood cells (WBCs) using domain knowledge, achieving high accuracy without relying heavily on traditional deep learning models. This approach is significant for engineers as it offers a novel alternative to complex architectures commonly used in computer vision tasks.

## Key Contribution

**A novel deterministic graph traversal method for WBC classification based on domain knowledge.**

## Problem

The need for efficient and accurate classification of white blood cells to assess human health and identify medical conditions.

## Method

**Approach:** The method constructs a directed graph with WBC classes as nodes and morphological connections as edges. A deterministic traversal is performed based on a Boolean feature vector generated from WBC images to classify them.

**Algorithm:**

1. 1. Input a whole-blood smear image.
2. 2. Preprocess the image to segment the WBC.
3. 3. Use a CNN model to generate a Boolean feature vector from the segmented WBC image.
4. 4. Construct a directed graph with WBC classes as nodes and morphological connections as edges.
5. 5. Perform a deterministic traversal on the graph using the Boolean feature vector.
6. 6. Identify the WBC class based on the traversal result.

**Input:** Whole-blood smear images containing WBCs.

**Output:** Class label of the identified WBC.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 32`
- `epochs: 30`
- `dropout_rate: 0.25`

**Complexity:** not stated

## Benchmarks

**Tested on:** Blood Cell Count and Detection (BCCD), LISC

**Results:**

- BCCD - accuracy: 99.13%, precision: 99.25%, recall: 99.25%, F1: 99.25%
- LISC - accuracy: 97.05%, precision: 97.04%, recall: 96.93%, F1: 96.94%

**Compared against:** Traditional deep learning models for WBC classification

**Improvement:** Achieved higher accuracy with less architectural complexity compared to traditional models.

## Implementation Guide

**Data Structures:** Directed graph structure, Boolean feature vectors

**Dependencies:** TensorFlow, Keras, OpenCV, PyTorch

**Core Operation:**

```python
classify_wbc(image): preprocess(image) -> feature_vector = generate_feature_vector(image) -> class_label = traverse_graph(feature_vector)
```

**Watch Out For:**

- Ensure proper segmentation of WBCs to avoid misclassification.
- The quality of the Boolean feature vector directly impacts classification accuracy.
- Watch for potential infinite loops during graph traversal.

## Use This When

- You need a lightweight classifier for WBC classification.
- You want to reduce dependency on deep learning models for specific applications.
- You have domain knowledge about the classification task that can be encoded in a graph.

## Don't Use When

- You require real-time processing with high computational resources.
- You have access to large, high-quality datasets suitable for deep learning models.
- You need to classify images with complex features that are not well represented by the proposed method.

## Key Concepts

deterministic traversal, graph-based classification, Boolean feature vectors, WBC morphology

## Connects To

- Graph Neural Networks
- Knowledge Graphs
- Traditional Machine Learning Classifiers

## Prerequisites

- Basic understanding of graph theory
- Familiarity with CNNs
- Knowledge of WBC morphology

## Limitations

- May not generalize well to datasets with different imaging conditions.
- Performance heavily relies on the quality of the Boolean feature vectors.
- Limited to the morphological features encoded in the graph.

## Open Questions

- How can this method be adapted for other types of cell classification?
- What improvements can be made to the graph traversal algorithm for efficiency?

## Abstract

Geesh...is every computer vision paper just another deep learning classifier? It can certainly seem that way. There are so many projects built on top of Yolo, ResNet, and VGG that it can be tempting to believe that that’s all there is...that there’s nothing else going on in that field. So today, we’re going to look at something different. A computer-vision problem that’s being solved in a way that we rarely see. Instead of a normal deep-learning classifier, the authors built a system that performs a deterministic traversal through a directed graph in order to arrive at a class label. Why? Because it turns out that traditional CV models are not a panacea. They have a number of drawbacks that make them less suitable for specific applications. In today’s episode we’re going to talk about how most CV models work, why they’re not ideal for certain use-cases, how this alternative method is better suited, and then how
