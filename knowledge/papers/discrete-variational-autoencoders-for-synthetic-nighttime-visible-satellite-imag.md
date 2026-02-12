# Discrete variational autoencoders for synthetic nighttime visible satellite imagery

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1017/eds.2025.10015` |
| Full Paper | [https://doi.org/10.1017/eds.2025.10015](https://doi.org/10.1017/eds.2025.10015) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/31ff2ea751ebbe76af738e8bb7b17c449ed891d4](https://www.semanticscholar.org/paper/31ff2ea751ebbe76af738e8bb7b17c449ed891d4) |
| Source | [https://journalclub.io/episodes/discrete-variational-autoencoders-for-synthetic-nighttime-visible-satellite-imagery](https://journalclub.io/episodes/discrete-variational-autoencoders-for-synthetic-nighttime-visible-satellite-imagery) |
| Source | [https://www.semanticscholar.org/paper/31ff2ea751ebbe76af738e8bb7b17c449ed891d4](https://www.semanticscholar.org/paper/31ff2ea751ebbe76af738e8bb7b17c449ed891d4) |
| Year | 2026 |
| Citations | 0 |
| Authors | Mickell D. Als, David Tomarov, Steve M. Easterbrook |
| Paper ID | `b0951623-a499-48e1-9a62-61a3464fb072` |

## Classification

- **Problem Type:** image-to-image translation
- **Domain:** Machine Learning & AI
- **Sub-domain:** Generative Models
- **Technique:** Vector Quantized Variational Autoencoder (VQVAE)
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

This paper presents a discrete variational autoencoder (VQVAE) method for generating synthetic nighttime visible satellite imagery from infrared data, addressing the limitation of visible satellite imagery availability during nighttime. Engineers should care because this approach enhances weather forecasting capabilities and provides a modular framework for meteorological data processing.

## Key Contribution

**Introduction of a VQVAE method for generating high-quality synthetic nighttime visible satellite imagery without relying on U-Net architectures.**

## Problem

The work is motivated by the need for accurate low-level cloud tracking and weather prediction using visible satellite imagery, which is limited during nighttime.

## Method

**Approach:** The method uses a VQVAE to compress high-dimensional infrared satellite data into a discrete latent space, which is then used to generate synthetic visible imagery. The model is trained adversarially with a GAN framework to enhance the realism of the generated images.

**Algorithm:**

1. 1. Preprocess the input infrared satellite images into a suitable format.
2. 2. Pass the images through the encoder to obtain a latent representation.
3. 3. Quantize the latent representation using a predefined codebook.
4. 4. Decode the quantized representation to reconstruct the visible imagery.
5. 5. Train the model using a combination of reconstruction loss and GAN loss.

**Input:** Three selected LWIR bands from the ABI satellite data.

**Output:** Synthetic RGB images representing nighttime visible satellite imagery.

**Key Parameters:**

- `learning_rate: 4.5e-6`
- `codebook_size: 2048 or 4096`
- `embedding_dimension: 256`
- `discriminator_loss_weight: 0.2`
- `number_of_residual_blocks: 3`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Geostationary Operational Environmental Satellite (GOES) West Advanced Baseline Imager (ABI) data

**Results:**

- LPIPS: 0.251 (Dim = 4, Land/Ocean)
- PSNR: 21.788 (Dim = 4, Land/Ocean)
- RMSE: 0.084 (Dim = 4, Land/Ocean)
- SSIM: 0.637 (Dim = 4, Land/Ocean)

**Compared against:** Pix2Pix (Yao et al. 2024): PSNR = 28.3, U-Net: SSIM = 0.85

**Improvement:** Performance metrics show significant improvements over traditional methods like Pix2Pix and U-Net.

## Implementation Guide

**Data Structures:** NumPy arrays for image data, Latent codebook for VQVAE

**Dependencies:** TensorFlow or PyTorch for deep learning, NumPy for data manipulation

**Core Operation:**

```python
output_image = decoder(quantizer(encoder(input_image))
```

**Watch Out For:**

- Ensure proper normalization of input data.
- Watch for color inversion artifacts in generated images.
- Be cautious with the choice of codebook size as it affects performance.

## Use This When

- You need to generate synthetic satellite imagery for nighttime conditions.
- You want to improve weather forecasting models with enhanced data.
- You are working on projects involving satellite image processing.

## Don't Use When

- You require real-time processing of visible imagery.
- You have limited computational resources for training complex models.
- You need a model that explicitly maintains spatial correspondence.

## Key Concepts

Variational Autoencoders, Generative Adversarial Networks, Image-to-Image Translation, Latent Space Representation

## Connects To

- Pix2Pix
- U-Net
- Conditional Generative Adversarial Networks
- Multi-layer Perceptrons

## Prerequisites

- Understanding of deep learning frameworks
- Familiarity with variational autoencoders
- Knowledge of image processing techniques

## Limitations

- Model may not generalize well to unseen atmospheric conditions.
- Potential for color inversion in generated outputs.
- Requires substantial computational resources for training.

## Open Questions

- How can physically-informed representations improve model performance?
- What are the implications of using a shared latent space across different tasks?

## Abstract

Let’s say you’re trying to build a model that can forecast the weather. You want it to be accurate, reliable, consistent, scalable, and able to predict weather patterns anywhere on earth. Where would you like to get your data from? Ground readings? Weather stations? Radar networks? No.
