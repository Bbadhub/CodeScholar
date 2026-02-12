# Explainable autoencoder for neutron star dense matter parameter estimation

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1088/2632-2153/add3bd` |
| Full Paper | [https://doi.org/10.1088/2632-2153/add3bd](https://doi.org/10.1088/2632-2153/add3bd) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/f9b3e92ee436d5b69e21edfa8c28c29c98c1b81d](https://www.semanticscholar.org/paper/f9b3e92ee436d5b69e21edfa8c28c29c98c1b81d) |
| Source | [https://journalclub.io/episodes/explainable-autoencoder-for-neutron-star-dense-matter-parameter-estimation](https://journalclub.io/episodes/explainable-autoencoder-for-neutron-star-dense-matter-parameter-estimation) |
| Source | [https://www.semanticscholar.org/paper/f9b3e92ee436d5b69e21edfa8c28c29c98c1b81d](https://www.semanticscholar.org/paper/f9b3e92ee436d5b69e21edfa8c28c29c98c1b81d) |
| Year | 2026 |
| Citations | 7 |
| Authors | Francesco Di Clemente, M. Scialpi, M. Bejger |
| Paper ID | `67f4d3ce-33e7-472b-861c-a9099ce6959a` |

## Classification

- **Problem Type:** parameter estimation
- **Domain:** Machine Learning & AI
- **Sub-domain:** Physics-informed neural networks
- **Technique:** Physics-informed autoencoder (PIA)
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a physics-informed autoencoder (PIA) designed to estimate the equation of state (EoS) parameters of neutron stars from observable quantities like mass, radius, and tidal deformability. This approach enhances interpretability and provides insights into the physical connections between EoS and observable properties, making it valuable for astrophysical research.

## Key Contribution

**Introduction of a physics-informed autoencoder that incorporates physical constraints into the latent space for improved interpretability in neutron star parameter estimation.**

## Problem

The challenge of accurately estimating the nuclear matter properties of neutron stars from observational data, particularly in the context of gravitational wave events.

## Method

**Approach:** The PIA encodes the EoS of neutron stars into an interpretable latent space using an autoencoder architecture. It incorporates additional loss functions that enforce physical relationships, allowing the model to learn a mapping between observables and microphysical parameters while maintaining interpretability.

**Algorithm:**

1. 1. Normalize the dataset of EoS parameters and neutron star observables.
2. 2. Initialize the encoder and decoder networks with fully connected layers.
3. 3. Define the loss function as a combination of reconstruction loss and physics-informed losses.
4. 4. Train the model using the ADAM optimizer with a learning rate of 0.001 and apply early stopping.
5. 5. Use Monte Carlo dropout during inference for uncertainty estimation.
6. 6. Evaluate the model's performance on test data.

**Input:** Pairs of data consisting of parameterized EoS and corresponding neutron star observables (mass, radius, tidal deformability).

**Output:** Reconstructed EoS parameters and insights into the physical connections between EoS and observable quantities.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: [4, 64]`
- `number_of_epochs: 2000`
- `dropout_rate: [0.1, 0.5]`
- `patience: [300, 400]`
- `n: [16, 128]`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Simulated neutron star parameters dataset ranging from 1000 to 30,000 instances.

**Results:**

- Reconstruction accuracy of mass, radius, and tidal deformability.

**Compared against:** Traditional black-box models without interpretability.

**Improvement:** Significant improvement in precision for reconstructing key physical quantities compared to traditional methods.

## Implementation Guide

**Data Structures:** Fully connected layers for encoder and decoder., Latent space representation.

**Dependencies:** TensorFlow or PyTorch for neural network implementation.

**Core Operation:**

```python
model.fit(X_train, y_train, epochs=2000, batch_size=64, callbacks=[early_stopping])
```

**Watch Out For:**

- Ensure proper normalization of input data to improve training stability.
- Monitor validation loss to prevent overfitting during training.
- Adjust learning rates dynamically to avoid local minima.

## Use This When

- You need to estimate neutron star parameters from observational data.
- Interpretability of machine learning models is critical for your application.
- You want to incorporate physical laws into your machine learning models.

## Don't Use When

- The problem domain does not require interpretability.
- You are working with data that does not relate to astrophysical phenomena.
- You need a fast, non-interpretative black-box model.

## Key Concepts

autoencoder, latent space, physics-informed neural networks, TOV equations, gravitational waves, interpretability

## Connects To

- Neural networks
- Physics-informed neural networks
- Autoencoders
- Gravitational wave analysis
- Astrophysical modeling

## Prerequisites

- Understanding of neural networks
- Familiarity with autoencoders
- Basic knowledge of astrophysics and neutron stars

## Limitations

- The model may not generalize well to neutron stars with complex EoS.
- Empirical relationships used may not hold in all astrophysical scenarios.
- The approach relies on the assumption that the TOV equations accurately describe neutron star behavior.

## Open Questions

- How can the model be adapted to incorporate more complex EoS considerations?
- What are the implications of using different empirical relationships in the loss function?

## Abstract

This is a well-known bottleneck in neutron star research. Gravitational wave events have opened up a new observational channel, but turning those observations into meaningful constraints on nuclear matter requires some way to navigate this problem. Traditional techniques approach this by sampling from parameterized equation-of-state families and running forward simulations, rejecting configurations that do not match observed data. That works, but it is slow, non-differentiable, and hard to scale. More recent approaches have turned to machine learning as a way to learn a fast, differentiable mapping between observables and microphysical parameters. But even there, most of the progress has been made with black-box models that offer little visibility into how their predictions are structured internally.
