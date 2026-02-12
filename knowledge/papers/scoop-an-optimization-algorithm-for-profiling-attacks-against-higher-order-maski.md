# Scoop: An Optimization Algorithm for Profiling Attacks against Higher-Order Masking

## Access

| Field | Value |
|-------|-------|
| DOI | `10.46586/tches.v2025.i3.56-80` |
| Full Paper | [https://doi.org/10.46586/tches.v2025.i3.56-80](https://doi.org/10.46586/tches.v2025.i3.56-80) |
| Source | [https://journalclub.io/episodes/scoop-an-optimization-algorithm-for-profiling-attacks-against-higher-order-masking](https://journalclub.io/episodes/scoop-an-optimization-algorithm-for-profiling-attacks-against-higher-order-masking) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `5161515f-8b94-46bc-9cd7-3b7096c5e706` |

## Classification

- **Problem Type:** profiling attacks against higher-order masking
- **Domain:** Cybersecurity
- **Sub-domain:** Side-channel Analysis
- **Technique:** Scoop
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper introduces Scoop, a novel optimization algorithm designed to enhance deep learning profiling attacks against higher-order masking schemes. It addresses the plateau effect that hampers optimization in this context, making it crucial for engineers working on side-channel analysis and cryptographic security.

## Key Contribution

**Scoop combines second-order optimization with sparse mirror descent to effectively reduce the plateau effect in deep learning profiling attacks.**

## Problem

The work is motivated by the need to improve the efficiency of deep learning-based side-channel attacks, which suffer from optimization challenges due to masking schemes.

## Method

**Approach:** Scoop utilizes second-order derivatives of the loss function to navigate the loss landscape more effectively, reducing the impact of low-gradient areas. It also incorporates sparse mirror descent to leverage the intrinsic sparsity of information in side-channel attack traces.

**Algorithm:**

1. Initialize model parameters using a distribution (e.g., Kaiming uniform).
2. Compute the loss function based on the model's predictions.
3. Calculate the gradient and Hessian of the loss function.
4. Update model parameters using the second-order optimization rule.
5. Incorporate sparse mirror descent to enhance performance.
6. Repeat until convergence or a set number of iterations.

**Input:** Training data consisting of traces and corresponding secret values.

**Output:** Trained model parameters that minimize the loss function.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 32`
- `number_of_iterations: 1000`

**Complexity:** Not stated

## Benchmarks

**Tested on:** ASCADv1, ASCADv2

**Results:**

- number of traces required to retrieve the key
- perceived information
- training cost
- plateau length

**Compared against:** Standard SGD, Adam

**Improvement:** Scoop reduces the plateau length by a factor of up to 5 for a masking order of 3 and higher.

## Implementation Guide

**Data Structures:** Neural network model, Loss function representation, Gradient and Hessian matrices

**Dependencies:** TensorFlow, PyTorch, NumPy

**Core Operation:**

```python
for each iteration: update_parameters = parameters - learning_rate * inverse(Hessian) * gradient
```

**Watch Out For:**

- Ensure proper initialization to avoid saddle points.
- Monitor learning rate to prevent divergence.
- Validate the model on multiple datasets to ensure robustness.

## Use This When

- You need to optimize deep learning models for profiling attacks against cryptographic implementations.
- You are facing challenges with the plateau effect in optimization during training.
- You require a more efficient method for training models on small datasets typical in side-channel analysis.

## Don't Use When

- The problem does not involve deep learning or profiling attacks.
- You are working with large-scale datasets where traditional optimization methods suffice.
- The application does not require handling of higher-order masking schemes.

## Key Concepts

plateau effect, second-order optimization, sparse mirror descent, deep learning, profiling attacks

## Connects To

- SGD
- Adam
- Newton's method
- Sparse mirror descent
- Deep learning architectures

## Prerequisites

- Understanding of deep learning optimization
- Familiarity with side-channel attacks
- Knowledge of gradient descent methods

## Limitations

- Performance may vary with different masking orders.
- Requires careful tuning of hyperparameters.
- Not applicable to all types of machine learning problems.

## Open Questions

- How can Scoop be adapted for real-time applications?
- What are the implications of using Scoop in different cryptographic contexts?

## Abstract

The authors of this paper argue that the plateau isn’t just an incidental nuisance. It’s a structural weakness in the optimization process. Standard methods like SGD and Adam aren’t built for the geometry of this problem. So the authors introduce something called Scoop, a new optimizer tailored specifically for this attack setting. On today’s episode, we’ll start by unpacking the plateau effect a bit more, and explore why it gets worse as masking order increases. Then we’ll walk through the core design of Scoop, including its use of second-order curvature, sparse mirror descent, and a new variant of the Hutchinson estimator. Let’s dive in.
