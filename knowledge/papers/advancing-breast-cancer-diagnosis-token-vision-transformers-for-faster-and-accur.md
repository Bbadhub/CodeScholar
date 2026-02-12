# Advancing breast cancer diagnosis: token vision transformers for faster and accurate classification of histopathology images

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s42492-024-00181-8` |
| Full Paper | [https://doi.org/10.1186/s42492-024-00181-8](https://doi.org/10.1186/s42492-024-00181-8) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/1073fb3a183271055d065e7b5c8ceda700bdaa0d](https://www.semanticscholar.org/paper/1073fb3a183271055d065e7b5c8ceda700bdaa0d) |
| Source | [https://journalclub.io/episodes/advancing-breast-cancer-diagnosis-token-vision-transformers-for-faster-and-accurate-classification-of-histopathology-images](https://journalclub.io/episodes/advancing-breast-cancer-diagnosis-token-vision-transformers-for-faster-and-accurate-classification-of-histopathology-images) |
| Source | [https://www.semanticscholar.org/paper/1073fb3a183271055d065e7b5c8ceda700bdaa0d](https://www.semanticscholar.org/paper/1073fb3a183271055d065e7b5c8ceda700bdaa0d) |
| Year | 2026 |
| Citations | 11 |
| Authors | Mouhamed Laid Abimouloud, Khaled Bensid, Mohamed Elleuch, Mohamed Ben Ammar, M. Kherallah |
| Paper ID | `3d87935e-0954-4550-8f2d-3af0e995854a` |

## Classification

- **Problem Type:** multi-class classification
- **Domain:** Machine Learning & AI
- **Sub-domain:** Medical Image Analysis
- **Technique:** TokenMixer
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents the TokenMixer, a hybrid architecture combining convolutional neural networks (CNNs) and vision transformers (ViTs) to enhance the classification of breast cancer histopathology images. This approach aims to improve accuracy and reduce training time and computational resources, making it suitable for real-world medical applications.

## Key Contribution

**Introduction of the TokenMixer hybrid architecture that integrates CNNs and ViTs for efficient breast cancer classification.**

## Problem

The challenge of accurately classifying breast cancer subtypes from histopathology images due to the complexity and variability of the images.

## Method

**Approach:** The TokenMixer architecture utilizes a combination of CNNs for feature extraction and ViTs for classification. It tokenizes input patches using convolutional layers and processes them through an encoder transformer to enhance feature representation and classification accuracy.

**Algorithm:**

1. 1. Preprocess histopathology images by resizing to 224x224 pixels.
2. 2. Split data into training, validation, and test sets.
3. 3. Use data augmentation techniques such as rotation and zoom.
4. 4. Extract features using TokenLearner and ConvMixer.
5. 5. Combine features in TokenMixer and pass through ViT for classification.
6. 6. Output predictions for binary and multi-class classification.

**Input:** Histopathology images resized to 224x224 pixels.

**Output:** Predictions for binary (Benign/Malignant) and multi-class (eight tumor subtypes) classification.

**Key Parameters:**

- `patch_size: 14x14`
- `number_of_layers: 8`
- `learning_rate: not stated`
- `batch_size: not stated`

**Complexity:** Not stated

## Benchmarks

**Tested on:** BreakHis dataset

**Results:**

- accuracy (binary classification): 97.02%
- accuracy (multi-class classification): 93.29%
- decision time (binary classification): 391.71 s
- decision time (multi-class classification): 1173.56 s

**Compared against:** ViT-based models, other state-of-the-art methods

**Improvement:** Significant improvement over baseline models in terms of accuracy and decision time.

## Implementation Guide

**Data Structures:** Image tensors, Feature maps, Tokenized patches

**Dependencies:** TensorFlow or PyTorch, NumPy, OpenCV for image processing

**Core Operation:**

```python
model_output = TokenMixer(preprocess(image))
```

**Watch Out For:**

- Ensure images are correctly resized to avoid loss of important features.
- Monitor GPU memory usage during training to avoid out-of-memory errors.
- Data augmentation should be applied consistently across training and validation sets.

## Use This When

- You need to classify histopathology images for breast cancer diagnosis.
- You want to reduce computational resources while maintaining high accuracy.
- You are working with limited training data and need an efficient model.

## Don't Use When

- You require real-time processing with extremely low latency.
- You have access to abundant computational resources and prefer using pure ViTs or CNNs.
- You are dealing with non-image data.

## Key Concepts

Tokenization, Convolutional layers, Multi-head attention, Feature extraction, Hybrid architecture

## Connects To

- CNN architectures
- Vision Transformers
- ConvMixer
- TokenLearner

## Prerequisites

- Understanding of CNNs
- Familiarity with ViTs
- Basic knowledge of image preprocessing techniques

## Limitations

- Requires significant computational resources for training.
- Performance may vary with different histopathology image qualities.
- Not optimized for real-time applications.

## Open Questions

- How can the model be further optimized for lower computational costs?
- What other medical imaging tasks can benefit from the TokenMixer architecture?

## Abstract

The ViTs process images as a sequence of non-overlapping patches rather than pixel arrays. Unlike CNNs, which rely on local receptive fields and weight-sharing, ViTs divide an image up, and then convert the pieces into flattened feature vectors. These vectors are then passed through an embedding layer that encodes positional information to maintain spatial context. The core of the architecture is its multi-head self-attention mechanism, which allows the model to attend to different regions of the image simultaneously. Since it’s a transformer, it’s able to capture complex relationships between distant regions of the tissue sample that may not be immediately adjacent but are diagnostically significant. Each transformer layer applies self-attention operations followed by normalization and feed-forward layers to refine the feature representation.
