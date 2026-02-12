# Adversarial disentanglement by backpropagation with physics-informed variational autoencoder

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1017/dce.2025.10028` |
| Full Paper | [https://doi.org/10.1017/dce.2025.10028](https://doi.org/10.1017/dce.2025.10028) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/1ea4961563c60e51e2291f73888934f2d85c3151](https://www.semanticscholar.org/paper/1ea4961563c60e51e2291f73888934f2d85c3151) |
| Source | [https://journalclub.io/episodes/adversarial-disentanglement-by-backpropagation-with-physics-informed-variational-autoencoder](https://journalclub.io/episodes/adversarial-disentanglement-by-backpropagation-with-physics-informed-variational-autoencoder) |
| Source | [https://www.semanticscholar.org/paper/1ea4961563c60e51e2291f73888934f2d85c3151](https://www.semanticscholar.org/paper/1ea4961563c60e51e2291f73888934f2d85c3151) |
| Year | 2026 |
| Citations | 1 |
| Authors | Ioannis Koune, Alice Cicirello |
| Paper ID | `46511d07-e34f-4c8a-8207-8171a77d0246` |

## Classification

- **Problem Type:** disentangled representation learning
- **Domain:** Machine Learning & AI
- **Sub-domain:** Physics-informed machine learning
- **Technique:** Physics-informed Variational Autoencoder
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a physics-informed variational autoencoder (VAE) that integrates physics-based models with data-driven approaches to improve the interpretability and performance of structural health monitoring systems. This method allows for the disentanglement of known physics from confounding influences, making it particularly valuable for engineers working with complex physical systems.

## Key Contribution

**A novel architecture for a physics-informed variational autoencoder that preserves the interpretability of latent variables while accounting for confounding influences through adversarial training.**

## Problem

The challenge of accurately inferring the behavior of engineering systems under the influence of multiple confounding factors and limited data.

## Method

**Approach:** The proposed method uses a VAE architecture that splits the latent space into physics-based and data-driven components. The encoder captures the known physics while the decoder integrates both components, constrained by an adversarial objective to maintain interpretability.

**Algorithm:**

1. 1. Define the physics-based model and collect response measurements, domain, and class variables.
2. 2. Partition the latent space into physically meaningful variables and data-driven variables.
3. 3. Train the encoder to map inputs to a posterior distribution over latent variables.
4. 4. Train the decoder to reconstruct the response while integrating both physics-based and data-driven components.
5. 5. Apply adversarial training to constrain the data-driven components and maintain the interpretability of the physics-based variables.
6. 6. Evaluate the model on new measurements to infer latent variables and predict domain and class variables.

**Input:** Response measurements, domain variables, and class variables.

**Output:** Disentangled latent variables representing the physics, domain, and class influences, along with reconstructed response measurements.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 64`
- `number_of_epochs: 100`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Synthetic case studies relevant to engineering structures

**Results:**

- Reconstruction accuracy, uncertainty quantification

**Compared against:** Fully data-driven approaches

**Improvement:** Demonstrated improved performance in damage identification tasks compared to fully data-driven models.

## Implementation Guide

**Data Structures:** Latent variable representations, Neural network architectures for encoder and decoder

**Dependencies:** TensorFlow or PyTorch for neural network implementation, NumPy for numerical operations

**Core Operation:**

```python
encoder_output = encoder(input_data); reconstructed_output = decoder(encoder_output);
```

**Watch Out For:**

- Ensure the adversarial training is properly balanced to avoid overfitting to the data-driven component.
- Monitor the interpretability of the latent variables during training to ensure they remain physically meaningful.
- Be cautious of the trade-off between model complexity and generalization performance.

## Use This When

- You need to model complex physical systems with limited data.
- You want to integrate domain knowledge with machine learning for better interpretability.
- You are dealing with confounding influences in your measurements.

## Don't Use When

- You have abundant high-quality data that can be modeled purely with data-driven approaches.
- The physical model is well-defined and does not require adjustments based on data.
- You need real-time predictions without the overhead of complex model training.

## Key Concepts

disentangled representations, adversarial training, variational inference, structural health monitoring

## Connects To

- Variational Autoencoders (VAE)
- Generative Adversarial Networks (GAN)
- Physics-informed Neural Networks (PINN)

## Prerequisites

- Understanding of variational inference and autoencoders.
- Familiarity with physics-based modeling.
- Knowledge of adversarial training techniques.

## Limitations

- Performance may degrade with highly noisy data.
- Requires careful tuning of adversarial constraints to maintain interpretability.
- Limited to scenarios where domain knowledge can be effectively integrated.

## Open Questions

- How can this approach be generalized to other domains beyond structural health monitoring?
- What are the best practices for tuning adversarial training parameters?

## Abstract

On November 7th, 1940, the Tacoma Narrows Bridge tore itself apart in the wind. Not because it was overloaded, and not because it was poorly built, but because the dominant physical mechanism driving its motion was misunderstood. Engineers had models for static loads and simple oscillations.
