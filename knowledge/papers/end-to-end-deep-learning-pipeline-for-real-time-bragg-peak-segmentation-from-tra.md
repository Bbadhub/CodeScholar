# End-to-end deep learning pipeline for real-time Bragg peak segmentation: from training to large-scale deployment

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fhpcp.2025.1536471` |
| Full Paper | [https://doi.org/10.3389/fhpcp.2025.1536471](https://doi.org/10.3389/fhpcp.2025.1536471) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/2eef2d593cdea51a8fe677156e0e13e27bfa5ed7](https://www.semanticscholar.org/paper/2eef2d593cdea51a8fe677156e0e13e27bfa5ed7) |
| Source | [https://journalclub.io/episodes/end-to-end-deep-learning-pipeline-for-real-time-bragg-peak-segmentation-from-training-to-large-scale-deployment](https://journalclub.io/episodes/end-to-end-deep-learning-pipeline-for-real-time-bragg-peak-segmentation-from-training-to-large-scale-deployment) |
| Source | [https://www.semanticscholar.org/paper/2eef2d593cdea51a8fe677156e0e13e27bfa5ed7](https://www.semanticscholar.org/paper/2eef2d593cdea51a8fe677156e0e13e27bfa5ed7) |
| Year | 2026 |
| Citations | 6 |
| Authors | Cong Wang, Valerio Mariani, Frédéric Poitevin, Matthew Avaylon, Jana Thayer |
| Paper ID | `aaa13763-698d-4681-b59d-66f243451d28` |

## Classification

- **Problem Type:** real-time peak segmentation in X-ray crystallography
- **Domain:** Machine Learning & AI
- **Sub-domain:** Deep Learning in Crystallography
- **Technique:** PeakNet
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents an end-to-end deep learning pipeline for real-time Bragg peak segmentation, addressing the challenges of high-throughput X-ray crystallography at XFEL facilities. Engineers should care because this system automates peak detection, significantly improving processing speed and accuracy compared to traditional methods.

## Key Contribution

**An integrated deep learning pipeline that combines automated dataset generation, scalable model architecture, and a decoupled producer-consumer architecture for efficient peak segmentation.**

## Problem

The need for efficient Bragg peak detection in high-throughput XFEL facilities producing millions of images per second.

## Method

**Approach:** The method utilizes a data engine for automated dataset generation, a modular architecture for scalable model training, and a producer-consumer architecture for efficient inference. This allows for real-time processing of large volumes of data without manual parameter tuning.

**Algorithm:**

1. 1. Collect diﬀraction patterns using established peak finding algorithms.
2. 2. Generate training data through a peak matching algorithm.
3. 3. Train a deep learning model using a modular architecture.
4. 4. Deploy the model in a producer-consumer architecture for inference.
5. 5. Validate and refine the model using continuous data feedback.

**Input:** Diﬀraction patterns in HDF5 format.

**Output:** Segmentation masks indicating Bragg peak locations.

**Key Parameters:**

- `learning_rate: 3e-4`
- `batch_size: 1 (gradient accumulation every 20 iterations)`
- `alpha_peak: 0.75`
- `alpha_background: 0.25`
- `gamma: 2`
- `threshold for reduced chi-square: not specified`

**Complexity:** Not stated

## Benchmarks

**Tested on:** PeakNet-20k dataset of ∼20,000 diﬀraction patterns

**Results:**

- indexing yield: 37.5%
- hit rate: 50.02%
- indexing rate: 72.73%

**Compared against:** Expert-tuned traditional methods achieving indexing yield of 36.38%

**Improvement:** 1.12% improvement in indexing yield over expert-tuned methods

## Implementation Guide

**Data Structures:** HDF5 files for input data, binary masks for output labels

**Dependencies:** Ray Core for distributed processing, lmfit for peak fitting, PyTorch for model training

**Core Operation:**

```python
def process_images(images): for img in images: mask = model.predict(img) save_to_hdf5(mask)
```

**Watch Out For:**

- Ensure proper data normalization for input images.
- Monitor GPU utilization to avoid bottlenecks during inference.
- Be aware of the need for iterative dataset curation for model improvement.

## Use This When

- You need to process large volumes of X-ray diﬀraction data in real-time.
- You want to automate peak detection without manual parameter tuning.
- You require a scalable solution for deploying machine learning models in edge environments.

## Don't Use When

- You are working with low-throughput data where traditional methods suffice.
- You have limited computational resources for model training and inference.
- You need a solution that does not require continuous model improvement.

## Key Concepts

Bragg peak detection, neural networks, data engine, model distillation, producer-consumer architecture, focal loss, feature pyramid networks

## Connects To

- BraggNet
- BraggNN
- Cheetah
- DIALS
- Psocake

## Prerequisites

- Understanding of deep learning frameworks
- Familiarity with X-ray crystallography
- Knowledge of distributed computing

## Limitations

- Requires significant computational resources for training
- Performance may vary with different experimental conditions
- Further optimization needed for MHz-scale operations

## Open Questions

- How can the pipeline be optimized for even higher throughput?
- What additional features can be integrated for improved accuracy?

## Abstract

This story takes place at what is called an XFEL facility. In an XFEL (which stands for X-ray Free Electron Laser) lab, researchers regularly fire ultrafast, high-intensity X-ray pulses at microscopic crystals to determine their atomic structure. A core part of that process is, as I mentioned, Bragg Peak detection. A Bragg Peak is a bright spot in a diffraction pattern. It’s formed when X-rays scatter off a crystal’s atomic lattice and interfere constructively at specific angles, in accordance with something called Bragg’s Law (thus the name). These peaks hold the key to determining a crystal’s atomic structure because their positions and intensities reveal how X-rays interact with the crystal at the atomic level. A modern XFEL can produce up to a million images per second, and they all need Bragg Peak detection run on them. But there's the problem: it can't handle that kind of speed and scale. Why? Well, existing
