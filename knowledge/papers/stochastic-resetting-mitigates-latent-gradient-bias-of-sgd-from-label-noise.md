# Stochastic resetting mitigates latent gradient bias of SGD from label noise

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1088/2632-2153/adbc46` |
| Full Paper | [https://doi.org/10.1088/2632-2153/adbc46](https://doi.org/10.1088/2632-2153/adbc46) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/99636d0325cee7685e122fae4d03769c9a589258](https://www.semanticscholar.org/paper/99636d0325cee7685e122fae4d03769c9a589258) |
| Source | [https://journalclub.io/episodes/stochastic-resetting-mitigates-latent-gradient-bias-of-sgd-from-label-noise](https://journalclub.io/episodes/stochastic-resetting-mitigates-latent-gradient-bias-of-sgd-from-label-noise) |
| Source | [https://www.semanticscholar.org/paper/99636d0325cee7685e122fae4d03769c9a589258](https://www.semanticscholar.org/paper/99636d0325cee7685e122fae4d03769c9a589258) |
| Year | 2026 |
| Citations | 5 |
| Authors | Youngkyoung Bae, Yeongwoo Song, Hawoong Jeong |
| Paper ID | `bdce1aa7-fe05-4a80-9c6a-20bafec64add` |

## Classification

- **Problem Type:** supervised learning with noisy labels
- **Domain:** Machine Learning & AI
- **Sub-domain:** Deep Learning
- **Technique:** Stochastic Resetting
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper demonstrates that applying stochastic resetting during the training of deep neural networks (DNNs) can significantly improve generalization performance in the presence of noisy labels. This method helps mitigate the latent gradient bias introduced by label noise, which often leads to overfitting.

## Key Contribution

**Introduction of stochastic resetting to SGD to counteract latent gradient bias from noisy labels in DNN training.**

## Problem

The work addresses the issue of overfitting in DNNs caused by noisy labels in training datasets, which can lead to poor generalization on unseen data.

## Method

**Approach:** The method integrates stochastic resetting into the SGD process by allowing the model parameters to reset to a checkpoint with a certain probability during training. This helps to avoid overfitting to corrupted data by revisiting earlier, potentially more accurate model states.

**Algorithm:**

1. Initialize model parameters θ0 and set iteration t = 0.
2. For each iteration t, sample a mini-batch Bt from the corrupted training set.
3. Update parameters θt using the SGD update rule.
4. With probability r, reset θt to a checkpoint θc.
5. Evaluate the model on the validation set and update the best checkpoint θbest if necessary.
6. If no improvement is seen for T iterations, update the checkpoint θc to θbest.

**Input:** Corrupted training set ˜Dtr, validation set Dval, reset probability r, threshold T.

**Output:** Updated model parameters θ after training.

**Key Parameters:**

- `learning_rate: 0.01`
- `reset_probability: r (0 < r < 1)`
- `threshold: T (e.g., 1000 iterations)`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** ciFAIR-10, CIFAR-10, CIFAR-100, CIFAR-10N, CIFAR-100N, ANIMAL-10N

**Results:**

- accuracy: improved test accuracy compared to baseline
- validation loss: reduced relative difference in validation loss

**Compared against:** SGD without resetting

**Improvement:** Significant improvements in generalization performance, with specific metrics not quantified in the abstract.

## Implementation Guide

**Data Structures:** Model parameters θ, Mini-batch Bt, Checkpoint θc, Best checkpoint θbest

**Dependencies:** Deep learning framework (e.g., TensorFlow, PyTorch), Statistical libraries for analysis

**Core Operation:**

```python
if rand(0,1) < r: θt = θc
```

**Watch Out For:**

- Choosing the right checkpoint to reset to is crucial for effectiveness.
- Setting the reset probability too high may lead to excessive resets.
- Monitoring validation loss is essential to determine when to update checkpoints.

## Use This When

- Training DNNs on datasets with known label noise.
- Seeking to improve generalization performance in supervised learning tasks.
- Experiencing overfitting issues during model training.

## Don't Use When

- The dataset is clean and free from label noise.
- Real-time training is required without interruptions.
- The computational resources are extremely limited.

## Key Concepts

stochastic gradient descent, latent gradient bias, overfitting, checkpointing, noisy labels, statistical physics

## Connects To

- Early stopping methods
- Co-teaching
- SELFIE
- Robust early learning

## Prerequisites

- Understanding of stochastic gradient descent.
- Familiarity with deep learning architectures.
- Knowledge of overfitting and regularization techniques.

## Limitations

- Performance may degrade if the reset probability is not optimally tuned.
- Not all datasets may benefit from stochastic resetting.
- The method may require additional computational overhead.

## Open Questions

- How does the optimal reset probability vary across different datasets?
- Can stochastic resetting be effectively combined with other noise-handling techniques?

## Abstract

Consider training a language model on a corpus where shorter sentences are overrepresented. If the model updates its parameters using mini-batches drawn randomly from the full dataset, shorter and syntactically simpler examples will dominate the early gradient estimates. These examples might favor certain token predictions or structural patterns that are not representative of the broader language distribution. As a result, the model parameters will be nudged in directions that overfit these simpler forms. This doesn’t just introduce noise, it creates a directional bias in the gradient field, pulling the optimization process toward a region that minimizes loss on an unbalanced subset of the data. Even as training continues and more varied examples appear, the model may be stuck in a basin shaped by these early biases. This phenomenon, while hard to detect in raw training curves, has been observed in practice in domains like
