# Employing deep learning in crisis management and decision making through prediction using time series data in Mosul Dam Northern Iraq

## Access

| Field | Value |
|-------|-------|
| DOI | `10.7717/peerj-cs.2416` |
| Full Paper | [https://doi.org/10.7717/peerj-cs.2416](https://doi.org/10.7717/peerj-cs.2416) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/a77013dfd231339f5d02104084897567ae8450ee](https://www.semanticscholar.org/paper/a77013dfd231339f5d02104084897567ae8450ee) |
| Source | [https://journalclub.io/episodes/employing-deep-learning-in-crisis-management-and-decision-making-through-prediction-using-time-series-data-in-mosul-dam-northern-iraq](https://journalclub.io/episodes/employing-deep-learning-in-crisis-management-and-decision-making-through-prediction-using-time-series-data-in-mosul-dam-northern-iraq) |
| Source | [https://www.semanticscholar.org/paper/a77013dfd231339f5d02104084897567ae8450ee](https://www.semanticscholar.org/paper/a77013dfd231339f5d02104084897567ae8450ee) |
| Year | 2026 |
| Citations | 2 |
| Authors | Khalid MK Khafaji, Bassem Ben Hamed |
| Paper ID | `7a102569-f5fc-4640-a544-a1ab3d91251f` |

## Classification

- **Problem Type:** time series prediction
- **Domain:** Machine Learning & AI
- **Sub-domain:** Deep Learning, Time Series Analysis
- **Technique:** CNN-LSTM
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a deep learning approach to predict water levels in the Mosul Dam to enhance crisis management and decision-making in the event of potential dam failure. Engineers should care because this method can significantly improve early warning systems for flood risks, potentially saving lives and resources.

## Key Contribution

**The introduction of a hybrid CNN-LSTM model that outperforms traditional models in predicting water levels with high accuracy.**

## Problem

The Mosul Dam is at risk of collapse, which could lead to catastrophic flooding in the surrounding areas.

## Method

**Approach:** The method utilizes historical water level data to train deep learning models that predict future water levels. It generates time series data for 14 days to forecast the next 7 days, allowing for proactive crisis management.

**Algorithm:**

1. 1. Collect historical water level data from 1993 to 2006.
2. 2. Preprocess the data to remove noise and scale values between -1 and 1.
3. 3. Split the data into training (80%), validation (10%), and testing (10%) sets.
4. 4. Train multiple deep learning models (DNN, CNN, CNN-LSTM, etc.) on the training set.
5. 5. Evaluate model performance on the validation set and select the best-performing model.
6. 6. Use the selected model to predict water levels for the next 7 days based on the last 14 days of data.
7. 7. Generate alerts based on predicted water levels.

**Input:** Historical water level data (daily readings) for the Mosul Dam.

**Output:** Predicted water levels for the next 7 days.

**Key Parameters:**

- `n-steps: 14`
- `n-horizon: 7`
- `learning_rate: 3e-4`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Historical water level data from the Mosul Dam (1993-2006)

**Results:**

- MAE: 0.087153
- Loss: 0.00067

**Compared against:** CNN-LSTM model

**Improvement:** The hybrid CNN-LSTM model showed superior performance compared to the baseline models.

## Implementation Guide

**Data Structures:** DataFrame for time series data, Arrays for model inputs and outputs

**Dependencies:** TensorFlow, Keras, NumPy, Pandas

**Core Operation:**

```python
model.fit(X_train, y_train); predictions = model.predict(X_test)
```

**Watch Out For:**

- Ensure data is cleaned and scaled appropriately.
- Monitor for overfitting during training.
- Validate model performance with unseen data.

## Use This When

- You need to predict time series data for critical infrastructure.
- You want to implement an early warning system for flood risks.
- You are working on crisis management solutions involving water resources.

## Don't Use When

- The dataset is too small or lacks historical data.
- Real-time predictions are required without historical context.
- The problem does not involve time series data.

## Key Concepts

Deep Learning, Time Series Prediction, Crisis Management, Flood Prediction, Neural Networks

## Connects To

- LSTM
- CNN
- RNN
- Time Series Analysis
- Anomaly Detection

## Prerequisites

- Understanding of neural networks
- Familiarity with time series data
- Knowledge of deep learning frameworks

## Limitations

- Dependent on the quality and quantity of historical data.
- May not generalize well to different geographical regions or dam types.
- Requires significant computational resources for training.

## Open Questions

- How can the model be adapted for real-time predictions?
- What additional features could improve prediction accuracy?

## Abstract

Late on the night of March 12, 1928, the St. Francis Dam, a crucial piece of Los Angeles’s water infrastructure, failed without warning. Built just a few years earlier, the dam had been a symbol of progress, an ambitious project to secure water for a growing city. But at 11:57 p.m., a crack turned into a rupture, and within seconds, the dam broke apart, releasing billions of gallons of water into the San Francisquito Canyon. A wall of water, over 100 feet high, surged downstream, taking homes, farms, and hundreds of lives with it. By the time it reached the Pacific Ocean, over 50 miles away, the flood had left a trail of destruction across the valley.
