# Interpretable and efficient data-driven discovery and control of distributed systems

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1017/dce.2025.10027` |
| Full Paper | [https://doi.org/10.1017/dce.2025.10027](https://doi.org/10.1017/dce.2025.10027) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/c4afec07162a7a857a1ad05397d56c6a677f4b00](https://www.semanticscholar.org/paper/c4afec07162a7a857a1ad05397d56c6a677f4b00) |
| Source | [https://journalclub.io/episodes/interpretable-and-efficient-data-driven-discovery-and-control-of-distributed-systems](https://journalclub.io/episodes/interpretable-and-efficient-data-driven-discovery-and-control-of-distributed-systems) |
| Source | [https://www.semanticscholar.org/paper/c4afec07162a7a857a1ad05397d56c6a677f4b00](https://www.semanticscholar.org/paper/c4afec07162a7a857a1ad05397d56c6a677f4b00) |
| Year | 2026 |
| Citations | 2 |
| Authors | Florian Wolf, Nicolò Botteghi, Urban Fasel, Andrea Manzoni |
| Paper ID | `13491fb3-ee1f-49c6-b6a2-23960b2b7d38` |

## Classification

- **Problem Type:** control of nonlinear distributed systems
- **Domain:** Machine Learning & AI
- **Sub-domain:** Reinforcement Learning, Control Theory
- **Technique:** AE+SINDy-C
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a novel data-efficient and interpretable control framework for distributed systems governed by partial differential equations (PDEs) using a combination of autoencoders and sparse identification of nonlinear dynamics. Engineers should care because this approach significantly reduces the need for extensive simulations while providing interpretable models for complex systems.

## Key Contribution

**Introduction of the AE+SINDy-C framework that combines autoencoders with sparse identification for efficient control of PDEs.**

## Problem

The work addresses the challenge of controlling complex physical systems described by PDEs, which often exhibit nonlinear dynamics and require low-latency feedback control.

## Method

**Approach:** The AE+SINDy-C framework uses autoencoders to reduce the dimensionality of the state and action spaces, allowing for the application of Sparse Identification of Nonlinear Dynamics with Control (SINDy-C) in a latent space. This enables efficient learning and control of PDEs with fewer interactions with the environment.

**Algorithm:**

1. 1. Encode the observed state and control input using separate encoder networks.
2. 2. Apply the SINDy-C algorithm in the latent space to predict the next state.
3. 3. Decode the predicted state back to the observation space.
4. 4. Compute the reconstruction loss and SINDy loss.
5. 5. Optimize the model parameters to minimize the combined loss.

**Input:** Current state and control input, both represented in high-dimensional space.

**Output:** Predicted next state in the observation space.

**Key Parameters:**

- `NLat_x: latent dimension for state representation`
- `NLat_u: latent dimension for control representation`
- `λ1, λ2, λ3: regularization parameters for SINDy loss`

**Complexity:** Not stated

## Benchmarks

**Tested on:** 1D Burgers equation, 2D Navier–Stokes equations

**Results:**

- sample efficiency
- stability
- interpretability

**Compared against:** model-free baseline algorithm

**Improvement:** Significantly improved sample efficiency and stability compared to the baseline.

## Implementation Guide

**Data Structures:** Neural network models for encoders and decoders, Sparse dictionary for SINDy

**Dependencies:** PyTorch, PySINDy

**Core Operation:**

```python
z_x = encoder(state); z_u = encoder(control); next_state = SINDy_C(z_x, z_u); output = decoder(next_state)
```

**Watch Out For:**

- Ensure the latent dimensions are appropriately set based on prior knowledge or data-driven tuning.
- Watch for overfitting when using sparse regularization.
- Monitor the stability of the learned dynamics model during training.

## Use This When

- Controlling high-dimensional nonlinear systems with limited data.
- Needing interpretable models for safety-critical applications.
- Reducing the computational cost of simulations in control tasks.

## Don't Use When

- The system dynamics are fully observable and low-dimensional.
- Real-time performance is critical and cannot accommodate the training time.
- The application does not require interpretability.

## Key Concepts

autoencoder, sparse identification, reinforcement learning, partial differential equations

## Connects To

- Model-based reinforcement learning
- Sparse Identification of Nonlinear Dynamics (SINDy)
- Autoencoder frameworks for dimensionality reduction

## Prerequisites

- Understanding of reinforcement learning concepts
- Familiarity with partial differential equations
- Knowledge of dimensionality reduction techniques

## Limitations

- Scalability issues with very high-dimensional systems.
- Dependence on the quality of the training data.
- Potential challenges in tuning hyperparameters for optimal performance.

## Open Questions

- How can the framework be adapted for real-time applications?
- What are the best practices for tuning latent dimensions in various applications?

## Abstract

When we talk about “physical systems”, we’re talking about real-life processes that move, flow, heat up, vibrate, or deform. Air flowing through a duct. Water moving down a channel. Heat spreading through a battery pack, etc. These systems are not just collections of parts, the components are interdependent and causally linked.
