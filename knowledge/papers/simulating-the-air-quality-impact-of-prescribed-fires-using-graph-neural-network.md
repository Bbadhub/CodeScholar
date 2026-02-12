# Simulating the air quality impact of prescribed fires using graph neural network-based PM2.5 forecasts

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1017/eds.2025.4` |
| Full Paper | [https://doi.org/10.1017/eds.2025.4](https://doi.org/10.1017/eds.2025.4) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/98ebfd5a037f595834d5cbf7c14031644a782e64](https://www.semanticscholar.org/paper/98ebfd5a037f595834d5cbf7c14031644a782e64) |
| Source | [https://journalclub.io/episodes/simulating-the-air-quality-impact-of-prescribed-fires-using-graph-neural-network-based-pm25-forecasts](https://journalclub.io/episodes/simulating-the-air-quality-impact-of-prescribed-fires-using-graph-neural-network-based-pm25-forecasts) |
| Source | [https://www.semanticscholar.org/paper/98ebfd5a037f595834d5cbf7c14031644a782e64](https://www.semanticscholar.org/paper/98ebfd5a037f595834d5cbf7c14031644a782e64) |
| Year | 2026 |
| Citations | 1 |
| Authors | Kyleen Liao, Jatan Buch, Kara D. Lamb, Pierre Gentine |
| Paper ID | `f0797628-592e-4f18-85a7-3aebeff01604` |

## Classification

- **Problem Type:** air quality forecasting
- **Domain:** Machine Learning & AI
- **Sub-domain:** Graph Neural Networks
- **Technique:** PM2.5-GNN
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a spatio-temporal graph neural network (GNN)-based model for forecasting PM2.5 concentrations in California, specifically focusing on the air quality impact of prescribed fires. Engineers should care because this model provides a novel approach to predict air quality impacts, which is crucial for effective fire management and public health.

## Key Contribution

**Introduction of a GNN-based framework for forecasting PM2.5 concentrations from prescribed fires, enabling better air quality management.**

## Problem

The need for accurate forecasting of PM2.5 concentrations resulting from prescribed fires to minimize health risks and optimize fire management strategies.

## Method

**Approach:** The PM2.5-GNN model predicts PM2.5 concentrations using a two-step approach: first, it forecasts total PM2.5 concentrations, and second, it estimates the contributions from ambient sources. The model integrates meteorological and fire-related data to enhance prediction accuracy.

**Algorithm:**

1. 1. Collect PM2.5, meteorological, and fire data.
2. 2. Train the PM2.5-GNN model using historical PM2.5 observations.
3. 3. Predict total PM2.5 concentrations using the trained model.
4. 4. Train a second PM2.5-GNN model to predict ambient PM2.5 concentrations.
5. 5. Subtract ambient PM2.5 predictions from total PM2.5 predictions to estimate fire-specific PM2.5 contributions.
6. 6. Simulate prescribed fires and input data into the PM2.5-GNN model to forecast air quality impact.

**Input:** PM2.5 concentrations, meteorological data (wind speed, temperature, precipitation), fire data (fire radiative power, number of fires).

**Output:** Predicted PM2.5 concentrations at specified sensor locations.

**Key Parameters:**

- `learning_rate: 0.001`
- `number_of_epochs: 100`
- `batch_size: 32`
- `window_size: 240 hours for historical data`
- `prediction_window: 48 hours into the future`

**Complexity:** not stated

## Benchmarks

**Tested on:** PM2.5 data from 112 sensor locations in California, meteorological data from ERA5, fire data from VIIRS

**Results:**

- MAE: 5.23 μg/m3
- RMSE: 6.72 μg/m3

**Compared against:** Random Forest (RF), Long Short-Term Memory (LSTM), Multilayer Perceptron (MLP)

**Improvement:** The PM2.5-GNN model outperformed baseline models with lower MAE and RMSE values.

## Implementation Guide

**Data Structures:** Graph structure for PM2.5 monitors, Feature vectors for nodes and edges

**Dependencies:** TensorFlow or PyTorch for model training, NumPy for data manipulation, Pandas for data handling

**Core Operation:**

```python
predictions = PM2.5_GNN(train_data, test_data)
```

**Watch Out For:**

- Ensure data is preprocessed correctly to handle missing values.
- Be cautious of overfitting with complex models.
- Monitor for prediction accuracy drop at higher PM2.5 concentrations.

## Use This When

- You need to forecast air quality impacts from prescribed fires.
- You require real-time PM2.5 predictions for emergency management.
- You want to analyze the trade-offs of prescribed fire implementation.

## Don't Use When

- You have access to high-resolution PM2.5 data without the need for modeling.
- You require predictions in a different geographical region not covered by the model.
- You need a simpler model without the complexity of GNNs.

## Key Concepts

Graph Neural Networks, PM2.5 Forecasting, Fire Emissions, Air Quality Management

## Connects To

- Gated Recurrent Units (GRU)
- Random Forests
- LSTM
- Chemical Transport Models (CTMs)

## Prerequisites

- Understanding of Graph Neural Networks
- Knowledge of PM2.5 and air quality metrics
- Familiarity with meteorological data

## Limitations

- Model performance may degrade during extreme fire events.
- Requires substantial historical data for training.
- Limited to the geographical scope of California.

## Open Questions

- How can the model be adapted for real-time deployment?
- What additional data sources could improve prediction accuracy?

## Abstract

Every year, California faces an impossible choice: burn now or burn later. Controlled burns reduce fuel loads and prevent megafires, but they also release something called PM2.5 into the atmosphere. These are fine particles of soot, ash, and other airborne pollutants that can travel hundreds of miles, and stay suspended in the air for days. And they’re not benign, they can cause respiratory illness and cardiovascular disease, and pose other serious health risks.
