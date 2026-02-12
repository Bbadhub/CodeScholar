# 4D trajectory lightweight prediction algorithm based on knowledge distillation technique

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fnbot.2025.1643919` |
| Full Paper | [https://doi.org/10.3389/fnbot.2025.1643919](https://doi.org/10.3389/fnbot.2025.1643919) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/5f45508729c06cca215d69c7f8e2819edef31736](https://www.semanticscholar.org/paper/5f45508729c06cca215d69c7f8e2819edef31736) |
| Source | [https://journalclub.io/episodes/4d-trajectory-lightweight-prediction-algorithm-based-on-knowledge-distillation-technique](https://journalclub.io/episodes/4d-trajectory-lightweight-prediction-algorithm-based-on-knowledge-distillation-technique) |
| Source | [https://www.semanticscholar.org/paper/5f45508729c06cca215d69c7f8e2819edef31736](https://www.semanticscholar.org/paper/5f45508729c06cca215d69c7f8e2819edef31736) |
| Year | 2026 |
| Citations | 0 |
| Authors | Weizhen Tang, Jie Dai, Zhousheng Huang, Boyang Hao, Weizheng Xie |
| Paper ID | `f02dc869-688a-42b4-9c9d-389eacf51e5d` |

## Classification

- **Problem Type:** 4D trajectory prediction
- **Domain:** Machine Learning & AI
- **Sub-domain:** Trajectory Prediction
- **Technique:** RCBAM–TCN–LSTM
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a lightweight 4D trajectory prediction algorithm using a hybrid RCBAM–TCN–LSTM architecture enhanced by knowledge distillation. This approach is crucial for real-time air traffic management, addressing the growing computational demands of trajectory prediction as air traffic density increases.

## Key Contribution

**A hybrid RCBAM–TCN–LSTM model that utilizes knowledge distillation to improve prediction accuracy while reducing computational complexity.**

## Problem

The need for accurate and efficient prediction of aircraft trajectories in increasingly congested airspace.

## Method

**Approach:** The method combines a teacher model (RCBAM) for feature extraction with a student model (TCN-LSTM) for temporal modeling. Knowledge distillation is employed to transfer knowledge from the teacher to the student, improving the student's performance on trajectory prediction tasks.

**Algorithm:**

1. 1. Preprocess historical ADS-B trajectory data.
2. 2. Train the teacher model (RCBAM) to extract high-dimensional spatial features.
3. 3. Train the student model (TCN-LSTM) using both soft labels from the teacher and hard labels from actual observations.
4. 4. Use the knowledge distillation mechanism to optimize the student model's performance.
5. 5. Evaluate the model on multi-step prediction tasks.

**Input:** Historical ADS-B trajectory data, including sampling time, position, altitude, speed, flight number, heading, climb or descent rate.

**Output:** Predicted future trajectory points in 4D (longitude, latitude, altitude, time).

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 32`
- `num_epochs: 100`
- `window_size: 10`
- `H (prediction horizon): 5`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Historical ADS-B trajectory data from Zhuhai Jinwan Airport

**Results:**

- MAE, RMSE, MAPE, R²

**Compared against:** Original RCBAM model, TCN-LSTM model

**Improvement:** Achieved average reductions of 40%-60% in MAE, RMSE, and MAPE compared to baseline models, while improving R² by 4%-6%.

## Implementation Guide

**Data Structures:** DataFrame for trajectory data, Tensor for model inputs

**Dependencies:** TensorFlow or PyTorch, NumPy, Pandas

**Core Operation:**

```python
model.train(input_data, labels) # Train the TCN-LSTM model with knowledge distillation
```

**Watch Out For:**

- Ensure proper preprocessing of trajectory data to avoid missing values.
- Monitor for overfitting during training, especially with complex models.
- Adjust the learning rate based on model performance during training.

## Use This When

- You need to predict aircraft trajectories in real-time for air traffic management.
- You require a lightweight model that can run on standard CPUs or embedded devices.
- You want to improve prediction accuracy while reducing computational costs.

## Don't Use When

- You have a small dataset that does not require complex modeling.
- You need a model with very high interpretability.
- You are working in a domain where real-time predictions are not critical.

## Key Concepts

knowledge distillation, 4D trajectory prediction, spatiotemporal modeling, deep learning, LSTM, TCN, feature extraction

## Connects To

- LSTM
- Temporal Convolutional Networks
- Residual Networks
- Knowledge Distillation
- Attention Mechanisms

## Prerequisites

- Understanding of deep learning concepts
- Familiarity with LSTM and CNN architectures
- Knowledge of trajectory prediction problems

## Limitations

- Model performance may degrade with insufficient training data.
- Real-time performance may vary based on hardware capabilities.
- The model may not generalize well to trajectories outside the training dataset.

## Open Questions

- How can the model be adapted for different types of trajectory data?
- What are the implications of using this model in diverse air traffic scenarios?

## Abstract

What do air traffic control systems do, exactly? Well, broadly, their mandate is to route planes around each other safely. In practice, this often means needing to not-only plot where a plane is, but predict where it’s going to be, and when it’s going to get there. This is inherently a 4D trajectory prediction problem. The four dimensions being longitude, latitude, altitude, and time. And as air traffic density continues to grow worldwide, the computational demands of this kind of real-time prediction are pushing existing systems to their breaking point.
