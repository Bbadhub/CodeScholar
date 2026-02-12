# Reconstructing unreadable QR codes: a deep learning based super resolution strategy

## Access

| Field | Value |
|-------|-------|
| DOI | `10.7717/peerj-cs.2841` |
| Full Paper | [https://doi.org/10.7717/peerj-cs.2841](https://doi.org/10.7717/peerj-cs.2841) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/5ad0bc5d9fc50f5ecb05faea5ca77051fcc85175](https://www.semanticscholar.org/paper/5ad0bc5d9fc50f5ecb05faea5ca77051fcc85175) |
| Source | [https://journalclub.io/episodes/reconstructing-unreadable-qr-codes-a-deep-learning-based-super-resolution-strategy](https://journalclub.io/episodes/reconstructing-unreadable-qr-codes-a-deep-learning-based-super-resolution-strategy) |
| Source | [https://www.semanticscholar.org/paper/5ad0bc5d9fc50f5ecb05faea5ca77051fcc85175](https://www.semanticscholar.org/paper/5ad0bc5d9fc50f5ecb05faea5ca77051fcc85175) |
| Year | 2026 |
| Citations | 2 |
| Authors | Yasin Sancar |
| Paper ID | `361b2c7b-f337-410c-bb77-2696a19e74a0` |

## Classification

- **Problem Type:** image enhancement, QR code reconstruction
- **Domain:** Computer Vision
- **Sub-domain:** Super-resolution techniques
- **Technique:** Enhanced Deep Super Resolution (EDSR), Very Deep Super Resolution (VDSR), Efficient Sub-Pixel Convolutional Network (ESPCN), Super Resolution Convolutional Neural Network (SRCNN)
- **Technique Category:** neural_architecture
- **Type:** comparison

## Summary

This paper presents a deep learning-based super-resolution strategy to reconstruct unreadable QR codes, demonstrating that super-resolution models can effectively improve the readability of degraded QR codes. Engineers should care because this approach can enhance QR code scanning reliability in real-world applications where traditional methods fail.

## Key Contribution

**A comparative analysis of four super-resolution models (EDSR, VDSR, ESPCN, SRCNN) for enhancing the readability of low-resolution QR codes.**

## Problem

The work addresses the issue of unreadable QR codes due to low resolution, misalignment, and other distortions caused by scanning devices.

## Method

**Approach:** The method involves applying four different super-resolution models to enhance the quality of unreadable QR codes. Each model processes the input images to reconstruct higher-resolution versions that can be decoded successfully.

**Algorithm:**

1. 1. Input the low-resolution QR code image.
2. 2. Preprocess the image (if necessary) to fit model input requirements.
3. 3. Pass the image through the selected super-resolution model (EDSR, VDSR, ESPCN, or SRCNN).
4. 4. Obtain the enhanced image output.
5. 5. Decode the enhanced QR code using a QR code detection library.
6. 6. Evaluate the success of decoding.

**Input:** Low-resolution QR code images in JPG format.

**Output:** Enhanced QR code images that are more readable and can be decoded.

**Key Parameters:**

- `learning_rate: 0.0001`
- `early_stopping_patience: 5`
- `reduce_lr_factor: 0.1`
- `lower_bound_learning_rate: 0.000001`

**Complexity:** Not stated

## Benchmarks

**Tested on:** 4,593 unreadable real-world scanned QR codes, 2,899 simulated unreadable QR codes, 16,000 computer-generated QR codes for training

**Results:**

- Success rates of decoding: EDSR (4,261), VDSR (4,229), ESPCN (4,255), SRCNN (4,042)

**Compared against:** OpenCV QRCodeDetector, WeChatQRCodeDetector

**Improvement:** Super-resolution models significantly improved QR code readability compared to traditional methods.

## Implementation Guide

**Data Structures:** Image arrays for input and output, Model architecture definitions for each super-resolution technique

**Dependencies:** TensorFlow or PyTorch for model implementation, OpenCV for QR code detection

**Core Operation:**

```python
output_image = super_resolution_model(input_image)
```

**Watch Out For:**

- Ensure the input images are preprocessed correctly for the models.
- Monitor for overfitting during training with EarlyStopping.
- Adjust learning rates appropriately to avoid convergence issues.

## Use This When

- You need to recover unreadable QR codes from low-quality scans.
- You are working with QR codes in commercial applications where reliability is critical.
- You want to enhance QR code scanning in environments with poor lighting or low contrast.

## Don't Use When

- The QR codes are already of high quality and easily readable.
- You require real-time processing with minimal computational resources.
- The application does not involve QR codes.

## Key Concepts

super-resolution, deep learning, image enhancement, QR code detection

## Connects To

- Image processing techniques
- Convolutional Neural Networks (CNNs)
- Generative Adversarial Networks (GANs)

## Prerequisites

- Understanding of deep learning concepts
- Familiarity with image processing techniques
- Knowledge of QR code structure and encoding

## Limitations

- Performance may vary based on the quality of the input images.
- Models may require significant computational resources for training.
- Not all QR codes may be recoverable, especially if severely damaged.

## Open Questions

- How can these models be optimized for real-time applications?
- What additional techniques can be combined with super-resolution for better performance?

## Abstract

Today’s paper focuses not on better code generation, or improvements to physical printing, but on the computational recovery of unreadable QR codes, after the damage is done. The authors ask a series of questions: When a QR code scan fails, can we use deep learning-based super-resolution to reconstruct a version of the image that can be decoded? And if so, which model works best, under which conditions, and with what tradeoffs? These questions aren’t new. But the experimental setup in this paper is different from most prior work. Instead of just generating synthetic low-res QR codes and testing on them, the authors collected over four thousand real-world scanned QR codes that had failed to decode in the wild. These aren’t academic edge cases; they are representative of the actual failure points in deployed systems. The authors also included an additional ~3,000 simulated QR codes that couldn’t be read by either OpenCV’s traditional
