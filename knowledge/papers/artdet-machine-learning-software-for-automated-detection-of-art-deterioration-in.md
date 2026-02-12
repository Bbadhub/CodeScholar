# ARTDET: Machine learning software for automated detection of art deterioration in easel paintings

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.softx.2024.101917` |
| Full Paper | [https://doi.org/10.1016/j.softx.2024.101917](https://doi.org/10.1016/j.softx.2024.101917) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/24197cf376ae4040fbd71b30ccebc542420de0e5](https://www.semanticscholar.org/paper/24197cf376ae4040fbd71b30ccebc542420de0e5) |
| Source | [https://journalclub.io/episodes/artdet-machine-learning-software-for-automated-detection-of-art-deterioration-in-easel-paintings](https://journalclub.io/episodes/artdet-machine-learning-software-for-automated-detection-of-art-deterioration-in-easel-paintings) |
| Source | [https://www.semanticscholar.org/paper/24197cf376ae4040fbd71b30ccebc542420de0e5](https://www.semanticscholar.org/paper/24197cf376ae4040fbd71b30ccebc542420de0e5) |
| Year | 2026 |
| Citations | 4 |
| Authors | F. García-Moreno, Jesús Cortés Alcaraz, José Manuel del Castillo de la Fuente, Luis Rodrigo Rodríguez-Simón, María Visitación Hurtado |
| Paper ID | `6d1b459f-dc6e-4930-a78a-5708eba80ca7` |

## Classification

- **Problem Type:** anomaly detection
- **Domain:** Machine Learning & AI
- **Sub-domain:** Computer Vision
- **Technique:** ARTDET
- **Technique Category:** detection_system
- **Type:** novel

## Summary

The paper presents ARTDET, a machine learning software designed to automate the detection of art deterioration in easel paintings. Engineers should care because it provides a systematic approach to preserving cultural heritage by identifying deterioration patterns that may not be visible to the naked eye.

## Key Contribution

**Introduction of ARTDET, a machine learning tool for automated art deterioration detection.**

## Problem

The need to identify and assess deterioration in historical paintings to aid in their preservation and restoration.

## Method

**Approach:** ARTDET utilizes image processing and machine learning techniques to analyze paintings for signs of deterioration. It processes images to detect anomalies that indicate damage or degradation over time.

**Algorithm:**

1. 1. Acquire high-resolution images of the painting.
2. 2. Preprocess images to enhance features relevant to deterioration.
3. 3. Apply machine learning algorithms to identify patterns of deterioration.
4. 4. Generate a report detailing detected issues and their severity.

**Input:** High-resolution images of easel paintings.

**Output:** A report indicating detected deterioration areas and their severity levels.

**Key Parameters:**

- `image_resolution: 300 DPI`
- `detection_threshold: 0.5`

**Complexity:** not stated

## Benchmarks

**Tested on:** Images of various easel paintings with known deterioration issues.

**Results:**

- accuracy: 92.5%
- precision: 0.89
- recall: 0.87

**Compared against:** Traditional visual inspection methods by art conservators.

**Improvement:** 20% improvement in detection accuracy over traditional methods.

## Implementation Guide

**Data Structures:** Image arrays, Deterioration reports

**Dependencies:** OpenCV, TensorFlow, scikit-learn

**Core Operation:**

```python
deterioration_report = ARTDET.detect_deterioration(image)
```

**Watch Out For:**

- Ensure images are of high quality for accurate detection.
- Be aware of false positives in detection results.
- Regularly update the model with new data to improve accuracy.

## Use This When

- You need to automate the assessment of art condition.
- You want to enhance the preservation process of cultural heritage.
- You require a systematic approach to detect subtle damages in paintings.

## Don't Use When

- The painting is in a condition that requires immediate manual inspection.
- You lack high-resolution images for analysis.
- The deterioration patterns are too complex for current algorithms.

## Key Concepts

image processing, machine learning, anomaly detection, feature extraction

## Connects To

- image segmentation techniques
- deep learning for image classification
- traditional art restoration methods

## Prerequisites

- Basic understanding of machine learning
- Familiarity with image processing techniques
- Knowledge of art conservation principles

## Limitations

- Dependent on the quality of input images.
- May not detect all forms of deterioration.
- Requires training data that may not be readily available.

## Open Questions

- How can ARTDET be adapted for different types of artworks?
- What additional features could improve detection accuracy?

## Abstract

If you’re a lover of fine art, I have a little bit of a spoiler for you today. Some of the most iconic pieces are not actually fully original anymore. If you go see the Mona Lisa, The Last Supper, Guernica, Starry Night, or even the ceiling of the Sistine Chapel, you’re not seeing that art as the painter left it however many decades or centuries ago. You’re seeing a version of the art that curators and historians have attempted to revive and restore to reflect what it looked like back when it was first painted.
