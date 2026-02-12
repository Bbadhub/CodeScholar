# Time Series Forecasting Using Recurrent Neural Networks Based on Recurrent Sigmoid Piecewise Linear Neurons

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1080/08839514.2025.2490057` |
| Full Paper | [https://doi.org/10.1080/08839514.2025.2490057](https://doi.org/10.1080/08839514.2025.2490057) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/887c64d4cca0acb8533eaa72547599431f4e3920](https://www.semanticscholar.org/paper/887c64d4cca0acb8533eaa72547599431f4e3920) |
| Source | [https://journalclub.io/episodes/time-series-forecasting-using-recurrent-neural-networks-based-on-recurrent-sigmoid-piecewise-linear-neurons](https://journalclub.io/episodes/time-series-forecasting-using-recurrent-neural-networks-based-on-recurrent-sigmoid-piecewise-linear-neurons) |
| Source | [https://www.semanticscholar.org/paper/887c64d4cca0acb8533eaa72547599431f4e3920](https://www.semanticscholar.org/paper/887c64d4cca0acb8533eaa72547599431f4e3920) |
| Year | 2026 |
| Citations | 2 |
| Authors | V. Sineglazov, Vladyslav Horbatiuk |
| Paper ID | `d377f03b-6a18-4292-b5e8-e703617e82f4` |

## Classification

- **Problem Type:** time series forecasting
- **Domain:** Machine Learning & AI
- **Sub-domain:** Recurrent Neural Networks
- **Technique:** Recurrent Sigmoid Piecewise Linear (RSPL) neurons
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

This paper introduces a novel recurrent neuron architecture called Recurrent Sigmoid Piecewise Linear (RSPL) neurons, which aims to improve time series forecasting by providing better stability and lower error variance with fewer parameters compared to traditional RNN architectures like LSTM and GRU. Engineers should care because this approach could lead to more efficient models for time-dependent prediction tasks.

## Key Contribution

**The introduction of the Recurrent Sigmoid Piecewise Linear (RSPL) neuron architecture for time series forecasting.**

## Problem

The need for improved accuracy and efficiency in predicting time-dependent data.

## Method

**Approach:** The RSPL architecture modifies the traditional neuron structure by incorporating piecewise linear activation functions, allowing for better handling of non-linear relationships in time series data. This results in improved stability and reduced error variance while maintaining a lower number of parameters.

**Algorithm:**

1. 1. Initialize RSPL neuron parameters.
2. 2. Input time series data into the RSPL architecture.
3. 3. Compute the output using piecewise linear activation functions.
4. 4. Update weights based on the loss function using backpropagation.
5. 5. Repeat for multiple epochs until convergence.

**Input:** Time series data in a suitable format (e.g., normalized numerical values).

**Output:** Forecasted values for the time series.

**Key Parameters:**

- `learning_rate: 0.001`
- `num_epochs: 100`
- `batch_size: 32`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Standard time series datasets (specific datasets not mentioned)

**Results:**

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

**Compared against:** LSTM, GRU

**Improvement:** Demonstrated lower error variance compared to LSTM and GRU.

## Implementation Guide

**Data Structures:** Arrays for time series data, Matrices for weights

**Dependencies:** TensorFlow, Keras, NumPy

**Core Operation:**

```python
output = RSPL(input_data) # where RSPL is the custom neuron function
```

**Watch Out For:**

- Ensure proper normalization of input data.
- Monitor for overfitting during training.
- Adjust learning rate based on convergence behavior.

## Use This When

- You need to forecast time-dependent data with high accuracy.
- You want a model with fewer parameters for efficiency.
- You are facing stability issues with traditional RNN architectures.

## Don't Use When

- The dataset is small and does not require complex modeling.
- Real-time predictions are critical and require extremely low latency.
- You need to leverage existing LSTM or GRU architectures for compatibility.

## Key Concepts

RNN, LSTM, GRU, activation functions, time series, backpropagation, neural networks

## Connects To

- LSTM
- GRU
- Vanilla RNN
- Convolutional Neural Networks (for hybrid approaches)

## Prerequisites

- Understanding of neural networks
- Familiarity with time series analysis
- Knowledge of backpropagation

## Limitations

- Performance may vary with different types of time series data.
- Requires careful tuning of parameters for optimal results.
- Not yet widely adopted, may lack community support.

## Open Questions

- How does RSPL perform on diverse datasets compared to LSTM and GRU?
- Can RSPL be adapted for other types of neural network architectures?

## Abstract

Today we’re going to dig into one of those new advancements. A new recurrent neuron architecture designed specifically for this problem space: the Recurrent Sigmoid Piecewise Linear (RSPL) neuron. We’re going to walk through the core technical motivation behind it, the structural differences compared to LSTM and GRU neurons, and how it manages to deliver better stability and lower error variance with fewer parameters. We will step through the experimental setup that was used to benchmark RSPL against traditional recurrent cells and examine the results in detail. Let’s dive in. To date, the dominant technical paradigm for handling time-dependent prediction tasks has long been recurrent neural networks (RNNs), particularly variants like Long Short-Term Memory networks (LSTMs) and Gated Recurrent Units (GRUs). These latter two architectures were designed to address some of the shortcomings of vanilla RNNs, but they introduced problems of their
