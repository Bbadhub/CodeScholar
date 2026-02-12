# Dynamic-budget superpixel active learning for semantic segmentation

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/frai.2024.1498956` |
| Full Paper | [https://doi.org/10.3389/frai.2024.1498956](https://doi.org/10.3389/frai.2024.1498956) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/ef53850caf152235baa119775d012aa765bbf2f8](https://www.semanticscholar.org/paper/ef53850caf152235baa119775d012aa765bbf2f8) |
| Source | [https://journalclub.io/episodes/dynamic-budget-superpixel-active-learning-for-semantic-segmentation](https://journalclub.io/episodes/dynamic-budget-superpixel-active-learning-for-semantic-segmentation) |
| Source | [https://www.semanticscholar.org/paper/ef53850caf152235baa119775d012aa765bbf2f8](https://www.semanticscholar.org/paper/ef53850caf152235baa119775d012aa765bbf2f8) |
| Year | 2026 |
| Citations | 1 |
| Authors | Yuemin Wang, Ian Stavness |
| Paper ID | `ab916f68-f71f-4241-87b7-5e5cb6c8d033` |

## Classification

- **Problem Type:** active learning for semantic segmentation
- **Domain:** Machine Learning & AI
- **Sub-domain:** Active Learning, Semantic Segmentation
- **Technique:** Dynamic-budget superpixel active learning
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a dynamic-budget superpixel active learning strategy for semantic segmentation that improves labeling efficiency by dynamically querying high-uncertainty superpixels in images. Engineers should care because this approach can significantly reduce labeling costs while enhancing model performance in tasks like agricultural weed detection and urban scene understanding.

## Key Contribution

**A novel dynamic-budget querying strategy that improves regional active learning algorithms for semantic segmentation tasks.**

## Problem

The need for efficient labeling in semantic segmentation tasks, particularly in specialized domains like precision agriculture, where labeling costs are high.

## Method

**Approach:** The method uses a dynamic-budget querying strategy to select the optimal number of high-uncertainty superpixels from images for labeling. It employs clustering to determine the most uncertain superpixels and aggregates pixel uncertainties to guide the labeling process.

**Algorithm:**

1. Initialize with a pool of unlabeled images and an empty active learning training set.
2. Randomly select a small batch of images for initial labeling.
3. Train the model on the labeled images until convergence.
4. In each active learning step, identify the images with the highest uncertainty.
5. For each selected image, determine the superpixels and their uncertainties.
6. Cluster superpixels into high- and low-uncertainty groups.
7. Label high-uncertainty superpixels manually and ignore low-uncertainty ones.
8. Update the training set and retrain the model.

**Input:** Unlabeled images from datasets (Nassar 2020 and Cityscapes).

**Output:** Partially labeled images with high-uncertainty superpixels labeled and low-uncertainty superpixels ignored.

**Key Parameters:**

- `initial_learning_rate: 1e-4`
- `dropout_rate: 0.5`
- `batch_size: 4 (Nassar), 5 (Cityscapes)`
- `number_of_epochs: 500`
- `step_size: 50 images for low-budget experiments`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Nassar 2020, Cityscapes

**Results:**

- mean Intersection over Union (mIoU)

**Compared against:** Static-budget querying, Random whole-image manual labels

**Improvement:** 5.6% mIoU improvement over static-budget querying on Nassar dataset, 2.4% mIoU improvement on Cityscapes.

## Implementation Guide

**Data Structures:** Image arrays, Superpixel representations, Uncertainty maps

**Dependencies:** TensorFlow or PyTorch for model training, scikit-image for superpixel segmentation

**Core Operation:**

```python
for each image in unlabeled_pool: query_high_uncertainty_superpixels(image); label_superpixels(high_uncertainty);
```

**Watch Out For:**

- Ensure the superpixel segmentation is appropriate for the image resolution.
- Monitor the balance of labeled classes to avoid over-representing dominant classes.
- Dynamic budgeting may require tuning based on dataset characteristics.

## Use This When

- You need to reduce labeling costs in semantic segmentation tasks.
- Working with imbalanced datasets where certain classes are underrepresented.
- You have a limited labeling budget but want to maximize model performance.

## Don't Use When

- The dataset is small and can be fully labeled without high costs.
- The task does not involve significant class imbalance.
- Real-time labeling is required and cannot accommodate the querying process.

## Key Concepts

active learning, semantic segmentation, superpixels, uncertainty sampling, dynamic-budget querying

## Connects To

- Uncertainty sampling
- Bayesian Active Learning by Disagreement (BALD)
- Superpixel segmentation algorithms

## Prerequisites

- Understanding of active learning concepts
- Familiarity with semantic segmentation techniques
- Knowledge of uncertainty estimation methods

## Limitations

- Performance may vary significantly with different superpixel sizes.
- Dynamic-budget querying may not be effective in datasets with uniform class distributions.
- Requires careful tuning of parameters for optimal performance.

## Open Questions

- How can this approach be generalized to other domains beyond semantic segmentation?
- What are the effects of different superpixel algorithms on the performance of the active learning strategy?

## Abstract

Imagine that you went out and bought a big jigsaw puzzle. You take it home, open the box, flip it over and dump all the thousands of little pieces on the table. What’s the next thing you do? Well, I’m no puzzle-master, but the next thing I’d do is categorize all the pieces. This is basically a “classification” task. I have to look at each one, and say “that one is sky, that’s grass, that’s a piece of a building, that’s a part of a car, that’s a part of an animal, that’s a texture, that’s a pattern” etc. If I was a computer-vision model, and I was looking at pixels instead of puzzle-pieces, then this task would be called “semantic segmentation”. In semantic segmentation, a model scans through an image and classifies each pixel into a predefined category. As it reaches each pixel, it analyzes its features, and determines its class based on learned patterns
