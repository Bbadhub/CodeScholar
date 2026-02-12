# Electronic nose and machine learning for modern meat inspection

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s40537-025-01151-4` |
| Full Paper | [https://doi.org/10.1186/s40537-025-01151-4](https://doi.org/10.1186/s40537-025-01151-4) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/40eb18f41f08c2244da1da35ee2bad0694634f94](https://www.semanticscholar.org/paper/40eb18f41f08c2244da1da35ee2bad0694634f94) |
| Source | [https://journalclub.io/episodes/electronic-nose-and-machine-learning-for-modern-meat-inspection](https://journalclub.io/episodes/electronic-nose-and-machine-learning-for-modern-meat-inspection) |
| Source | [https://www.semanticscholar.org/paper/40eb18f41f08c2244da1da35ee2bad0694634f94](https://www.semanticscholar.org/paper/40eb18f41f08c2244da1da35ee2bad0694634f94) |
| Year | 2026 |
| Citations | 11 |
| Authors | I. Shtepliuk, G. Domènech-Gil, Viktor Almqvist, A. Kautto, I. Vågsholm, Sofia Boqvist |
| Paper ID | `d39f94eb-c596-4028-907c-cb82064fa252` |

## Classification

- **Problem Type:** anomaly detection
- **Domain:** Machine Learning & AI
- **Sub-domain:** Odor detection
- **Technique:** Optimizable Ensemble model
- **Technique Category:** classification_model
- **Type:** novel

## Summary

The authors developed a novel method using an electronic nose combined with machine learning to detect urine-related odor signatures in raw pig meat, aiming for high accuracy and real-time results. This approach could potentially replace human sensory judgment in meat inspection, enhancing food safety and quality control.

## Key Contribution

**Integration of a metal-oxide gas sensor array with a machine learning classification pipeline for meat inspection.**

## Problem

The need for reliable detection of chemical contaminants, specifically urine-related odors, in pig meat to ensure food safety.

## Method

**Approach:** The method employs a metal-oxide gas sensor array to capture volatile organic compounds (VOCs) from meat samples. The sensor data is processed to extract features, which are then used to train a machine learning model that classifies the samples as fresh or urine-contaminated.

**Algorithm:**

1. 1. Collect meat samples and prepare them for analysis.
2. 2. Use the electronic nose to measure VOC emissions from the samples.
3. 3. Normalize and smooth the raw sensor signals.
4. 4. Extract 60 features from the processed signals.
5. 5. Split the dataset into training and test sets.
6. 6. Train the machine learning model using the training set.
7. 7. Evaluate the model's performance using the test set.

**Input:** 60 extracted features from the sensor data.

**Output:** Classification labels indicating whether the meat is fresh or urine-contaminated.

**Key Parameters:**

- `sensor_count: 32`
- `feature_count: 60`
- `training_set_size: variable based on dataset split`

**Complexity:** not stated

## Benchmarks

**Tested on:** 100 pig meat samples from a slaughterhouse

**Results:**

- sensitivity: 96.5%
- specificity: 95.3%
- accuracy: 93.5%
- Kappa: 0.926

**Compared against:** Traditional sensory evaluation methods

**Improvement:** Significantly higher accuracy and reliability compared to traditional methods.

## Implementation Guide

**Data Structures:** Feature vectors for each meat sample, Sensor response data

**Dependencies:** MATLAB for data processing and model training

**Core Operation:**

```python
model.predict(feature_vector) # Classifies the meat sample based on extracted features.
```

**Watch Out For:**

- Ensure consistent sample preparation to avoid variability.
- Monitor sensor calibration regularly for accurate readings.
- Be aware of regulatory compliance when implementing in real-world settings.

## Use This When

- You need to automate meat inspection processes.
- Real-time detection of chemical contaminants is required.
- Objective assessment of meat quality is necessary.

## Don't Use When

- The regulatory environment does not permit the use of AI in food safety.
- High specificity for individual VOCs is required rather than general odor detection.
- Resources for implementing sensor technology are limited.

## Key Concepts

electronic nose, volatile organic compounds, machine learning, feature extraction, classification, food safety

## Connects To

- Random Forest
- Convolutional Neural Networks
- Gated Recurrent Units
- k-nearest neighbour
- Support Vector Machines

## Prerequisites

- Understanding of machine learning principles
- Familiarity with sensor technology
- Knowledge of data preprocessing techniques

## Limitations

- Dependent on the quality of sensor data
- May not detect all types of contaminants
- Regulatory hurdles in implementation

## Open Questions

- How can this method be adapted for other types of meat?
- What are the long-term effects of using this technology in commercial settings?

## Abstract

In this paper the authors are trying something different. They’re taking a commercially available metal-oxide gas sensor array (the "electronic nose”) and combining it with a classification pipeline built from 60 extracted signal features and a high-performing ensemble model. Their goal is to detect the presence of urine-related odor signatures in raw pig meat, with high accuracy, in real time, without human sensory judgment. In other words, they’re proposing a digital protocol that could “smell” a piece of pork, and tell you if it’s contaminated with urine. If it works well enough, it could, in theory, eventually replace (or at least augment) the nose of a human inspector. Let’s flush out more of the technical problem-space, then explore what the authors built, how it works, and whether or not it is effective. There are a number of current lab-based methods to analyze odor. This includes gas chromatography-mass spectrometry (GC-MS), surface
