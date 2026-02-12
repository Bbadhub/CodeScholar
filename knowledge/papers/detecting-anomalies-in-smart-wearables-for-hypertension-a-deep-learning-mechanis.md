# Detecting anomalies in smart wearables for hypertension: a deep learning mechanism

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fpubh.2024.1426168` |
| Full Paper | [https://doi.org/10.3389/fpubh.2024.1426168](https://doi.org/10.3389/fpubh.2024.1426168) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/0cdc75fa9e09d0aef36e7d20c7081cf0c71f29f1](https://www.semanticscholar.org/paper/0cdc75fa9e09d0aef36e7d20c7081cf0c71f29f1) |
| Source | [https://journalclub.io/episodes/detecting-anomalies-in-smart-wearables-for-hypertension-a-deep-learning-mechanism](https://journalclub.io/episodes/detecting-anomalies-in-smart-wearables-for-hypertension-a-deep-learning-mechanism) |
| Source | [https://www.semanticscholar.org/paper/0cdc75fa9e09d0aef36e7d20c7081cf0c71f29f1](https://www.semanticscholar.org/paper/0cdc75fa9e09d0aef36e7d20c7081cf0c71f29f1) |
| Year | 2026 |
| Citations | 10 |
| Authors | C. Kishor Kumar Reddy, Vijaya Sindhoori Kaza, R. Madana Mohana, M. Alhameed, Fathe Jeribi, Shadab Alam |
| Paper ID | `8f19af3c-6aba-4caf-a10f-0ac0f6c42b23` |

## Classification

- **Problem Type:** anomaly detection
- **Domain:** Machine Learning & AI
- **Sub-domain:** Deep Learning for Health Monitoring
- **Technique:** ResNet-LSTM
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a deep learning mechanism using a novel ResNet-LSTM architecture to detect anomalies in physiological signals from smart wearables for hypertension monitoring. Engineers should care because this approach enhances real-time health monitoring, crucial for managing cardiovascular diseases.

## Key Contribution

**Introduction of a ResNet-LSTM architecture for anomaly detection in smart wearables monitoring blood pressure.**

## Problem

The need for accurate and timely detection of anomalies in blood pressure monitoring using smart wearables to manage hypertension.

## Method

**Approach:** The ResNet-LSTM architecture combines feature extraction capabilities of ResNet with the sequential data processing of LSTM to predict blood pressure from ECG and PPG signals. This integration allows for improved accuracy in detecting anomalies in real-time monitoring.

**Algorithm:**

1. 1. Collect physiological signals (ECG and PPG) from wearable devices.
2. 2. Preprocess the signals to remove noise and artifacts.
3. 3. Feed the preprocessed signals into the ResNet component for feature extraction.
4. 4. Pass the extracted features to the LSTM component to capture temporal dependencies.
5. 5. Output predictions for blood pressure and detect anomalies based on deviations from expected patterns.
6. 6. Validate the model using Leave-One-Out cross-validation.
7. 7. Analyze errors using MAE and RMSE metrics.

**Input:** Physiological signals (ECG and PPG) from smart wearables.

**Output:** Predicted blood pressure values and detected anomalies.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 32`
- `epochs: 100`
- `FLOPs: ~4,375`

**Complexity:** not stated

## Benchmarks

**Tested on:** Physiological signals dataset including ECG and PPG data

**Results:**

- MAE: 6.2 mmHg
- RMSE: 8.9 mmHg

**Compared against:** Standard machine learning models for BP prediction

**Improvement:** Superior performance compared to baseline models.

## Implementation Guide

**Data Structures:** Time series data structures for ECG and PPG signals, Neural network layers for ResNet and LSTM

**Dependencies:** TensorFlow or PyTorch for deep learning, NumPy for numerical operations, Pandas for data manipulation

**Core Operation:**

```python
model.fit(X_train, y_train); predictions = model.predict(X_test); anomalies = detect_anomalies(predictions)
```

**Watch Out For:**

- Ensure proper preprocessing of input signals to remove noise.
- Monitor for overfitting during training with validation datasets.
- Adjust learning rates based on model performance.

## Use This When

- You need to implement real-time monitoring systems for hypertension using wearables.
- You require accurate anomaly detection in physiological signals.
- You are developing applications for continuous health monitoring in remote areas.

## Don't Use When

- You have limited computational resources for model training.
- You need a simple model without deep learning complexities.
- You are working with non-sequential data.

## Key Concepts

deep learning, anomaly detection, smart wearables, blood pressure monitoring, ResNet, LSTM

## Connects To

- Convolutional Neural Networks (CNNs)
- Long Short-Term Memory (LSTM)
- Autoencoders for anomaly detection

## Prerequisites

- Understanding of deep learning frameworks
- Knowledge of time-series data processing
- Familiarity with physiological signal characteristics

## Limitations

- Higher computational cost due to complex architecture.
- Requires large datasets for effective training.
- Sensitivity to noise in physiological signals.

## Open Questions

- How can the model be optimized for lower computational resources?
- What additional physiological signals could enhance anomaly detection accuracy?

## Abstract

The Download Festival is a yearly rock and metal gathering in Leicestershire, England. Bands from around the world come out to play for tens of thousands. And some of those bands are a bit…raucous. Let’s just say that mosh-pits aren’t exactly unheard-of at this festival. And the vast majority of the time, that’s no problem. But a couple of years ago those mosh-pits became a big problem…for the local police. Why?
