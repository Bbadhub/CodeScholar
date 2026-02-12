# COSMIC: A Galaxy Cluster-Finding Algorithm Using Machine Learning

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3847/1538-4365/ad8bbd` |
| Full Paper | [https://doi.org/10.3847/1538-4365/ad8bbd](https://doi.org/10.3847/1538-4365/ad8bbd) |
| Source | [https://journalclub.io/episodes/cosmic-a-galaxy-cluster-finding-algorithm-using-machine-learning](https://journalclub.io/episodes/cosmic-a-galaxy-cluster-finding-algorithm-using-machine-learning) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `240b13af-1dc2-4ebe-a5e3-7b917abcbdbd` |

## Classification

- **Problem Type:** galaxy cluster detection
- **Domain:** Machine Learning & AI
- **Sub-domain:** Galaxy cluster detection
- **Technique:** COSMIC
- **Technique Category:** framework
- **Type:** novel

## Summary

The COSMIC algorithm utilizes machine learning techniques to efficiently detect galaxy clusters by identifying the brightest cluster galaxies and estimating cluster richness. Engineers should care because it addresses the challenge of cataloging vast amounts of astronomical data, improving the completeness and accuracy of galaxy cluster detection.

## Key Contribution

**COSMIC introduces a two-step machine learning approach for galaxy cluster detection, combining XGBoost for BCG classification and a deep neural network for richness estimation.**

## Problem

The need to catalog and classify galaxy clusters in the universe as telescopes collect increasingly large datasets.

## Method

**Approach:** COSMIC operates in two main steps: first, it uses an XGBoost classifier to identify BCG-like galaxies from photometric and spectroscopic data. Second, it employs a deep neural network to estimate cluster richness based on the smoothed optical map around each identified BCG.

**Algorithm:**

1. Step 1: Use XGBoost to classify galaxies as BCG-like based on features such as r-band magnitude and colors.
2. Step 2: Generate a smoothed optical map (SOM) around each BCG and use a pretrained ResNet-34 model to estimate cluster richness.

**Input:** Photometric and spectroscopic data of galaxies, including r-band magnitude, colors, and photometric redshifts.

**Output:** Identified BCGs and estimated richness of galaxy clusters.

**Key Parameters:**

- `learning_rate: 0.1`
- `max_depth: 6`
- `n_estimators: 100`
- `sigma: 0.05 (for Gaussian smoothing)`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Sloan Digital Sky Survey (SDSS), WHL galaxy cluster catalog

**Results:**

- accuracy: 90.2%
- recall: 93.4%
- AUC: 0.9618

**Compared against:** Traditional cluster detection algorithms

**Improvement:** COSMIC shows improved completeness and purity compared to traditional methods.

## Implementation Guide

**Data Structures:** DataFrame for galaxy features, Image matrix for SOM

**Dependencies:** XGBoost, PyTorch, NumPy, Pandas

**Core Operation:**

```python
bcg_probabilities = XGBoost.predict(galaxy_features); richness = ResNet34.predict(SOM)
```

**Watch Out For:**

- Ensure proper preprocessing of photometric data to avoid misclassification.
- Watch out for overfitting in the BCG classifier; use cross-validation.
- Be cautious with the choice of hyperparameters for the neural network.

## Use This When

- You need to catalog galaxy clusters from large astronomical datasets.
- You want to improve the accuracy of galaxy cluster detection in optical surveys.
- You are working with data from upcoming large-scale astronomical surveys.

## Don't Use When

- You have a small dataset that does not require machine learning.
- You need real-time processing with minimal computational resources.
- You are focused on non-optical methods of galaxy cluster detection.

## Key Concepts

XGBoost, Deep Neural Networks, Richness Estimation, SOM, BCG Classification

## Connects To

- Convolutional Neural Networks
- Transfer Learning
- Optical Imaging Techniques

## Prerequisites

- Understanding of machine learning concepts
- Familiarity with astronomical data
- Knowledge of deep learning frameworks

## Limitations

- Requires high-quality photometric and spectroscopic data.
- Performance may degrade with clusters lacking distinctive features.
- Not optimized for real-time processing.

## Open Questions

- How can COSMIC be adapted for other astronomical phenomena?
- What improvements can be made to enhance the algorithm's robustness against data noise?

## Abstract

Astronomers have been cataloging the universe for centuries. First by hand, then by film, and now with optical detector arrays. Why? Because the first step to understanding the cosmos is counting and classifying what’s in it. But cataloging isn’t as easy as it might sound. As telescopes grow more sensitive, they’re able to see more of the universe and collect more data. And as the data gets bigger, making sense of all of it gets harder. The sheer number of individual light sources turns cataloging from a counting problem, into a massive pattern-recognition problem.
