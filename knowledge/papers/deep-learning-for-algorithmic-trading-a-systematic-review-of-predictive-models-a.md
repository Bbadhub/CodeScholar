# Deep learning for algorithmic trading: A systematic review of predictive models and optimization strategies

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.array.2025.100390` |
| Full Paper | [https://doi.org/10.1016/j.array.2025.100390](https://doi.org/10.1016/j.array.2025.100390) |
| Source | [https://journalclub.io/episodes/deep-learning-for-algorithmic-trading-a-systematic-review-of-predictive-models-and-optimization-strategies](https://journalclub.io/episodes/deep-learning-for-algorithmic-trading-a-systematic-review-of-predictive-models-and-optimization-strategies) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `b1918d99-7dd9-492f-b6bf-8d7ed5ae3d3d` |

## Classification

- **Problem Type:** predictive modeling for financial time series forecasting
- **Domain:** Machine Learning & AI
- **Sub-domain:** Time-series forecasting
- **Technique:** RNNs, LSTMs, CNNs, Autoencoders, GNNs, Transformers, Reinforcement Learning hybrids
- **Technique Category:** neural_architecture
- **Type:** comparison

## Summary

This paper systematically reviews various deep learning architectures used for algorithmic trading, highlighting their strengths and weaknesses in predictive modeling. Engineers should care because understanding these models can enhance trading strategies and improve decision-making in financial markets.

## Key Contribution

**A comprehensive review of deep learning architectures for algorithmic trading, detailing their application and performance trade-offs.**

## Problem

The need for accurate prediction models in algorithmic trading to make informed investment decisions.

## Method

**Approach:** The review categorizes various deep learning architectures based on their application in algorithmic trading. Each architecture is evaluated for its ability to capture temporal dependencies and handle market volatility.

**Algorithm:**

1. 1. Identify the trading task and data requirements.
2. 2. Select an appropriate deep learning architecture (e.g., RNN, LSTM).
3. 3. Preprocess the financial time series data.
4. 4. Train the model using historical data.
5. 5. Validate the model's performance on unseen data.
6. 6. Implement the model in a trading strategy.

**Input:** Historical financial time series data, including price, volume, and other relevant indicators.

**Output:** Predicted price movements or trading signals.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 32`
- `epochs: 100`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Historical stock price data, Forex data, Cryptocurrency data

**Results:**

- accuracy, precision, recall, F1-score

**Compared against:** Traditional statistical models (e.g., ARIMA), simpler machine learning models (e.g., decision trees)

**Improvement:** Varies by architecture; specific improvements not stated.

## Implementation Guide

**Data Structures:** Time series arrays, DataFrames for financial data

**Dependencies:** TensorFlow, Keras, PyTorch, NumPy, Pandas

**Core Operation:**

```python
model.fit(X_train, y_train); predictions = model.predict(X_test)
```

**Watch Out For:**

- Be cautious of overfitting on noisy data.
- Ensure proper data normalization before training.
- Monitor for vanishing gradients in RNNs.

## Use This When

- You need to predict stock prices based on historical data.
- You want to implement a trading strategy that adapts to market conditions.
- You are dealing with high-frequency trading data.

## Don't Use When

- The dataset is too small or lacks temporal structure.
- You require explainability in your trading decisions.
- Market conditions are highly unpredictable and volatile.

## Key Concepts

time-series forecasting, deep learning, financial modeling, predictive analytics, market volatility, overfitting, temporal dependencies

## Connects To

- ARIMA models
- Support Vector Machines
- Reinforcement Learning
- Feature engineering techniques
- Ensemble methods

## Prerequisites

- Understanding of neural networks
- Familiarity with time-series analysis
- Knowledge of financial markets

## Limitations

- Models may struggle with long-term dependencies.
- Performance can degrade in volatile markets.
- Requires large amounts of high-quality data.

## Open Questions

- How can we improve model robustness in unpredictable market conditions?
- What are the best practices for feature selection in financial time series?

## Abstract

The bulk of the models they reviewed fall into one of seven architecture classes: RNNs, LSTMs, CNNs, Autoencoders (including VAEs), GNNs, Transformers, and Reinforcement Learning hybrids. Each comes with tradeoffs, and each is being used in different ways depending on the specific prediction or trading task. I’ll walk through them in that order. RNNs are the most traditional approach for time-series forecasting. They operate by feeding the output from the previous timestep back into the model. This recurrent loop gives RNNs memory, which in principle allows them to capture temporal dependencies across financial time series. But in practice, vanilla RNNs degrade quickly when trying to model anything with long-term dependencies. They’re prone to vanishing gradients, they underperform in volatile markets, and they tend to overfit when the input data is noisy (which it usually is). A couple of studies cited in the review proposed RNN variants that
