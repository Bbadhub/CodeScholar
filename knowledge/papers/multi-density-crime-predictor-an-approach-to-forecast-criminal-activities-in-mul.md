# Multi-density crime predictor: an approach to forecast criminal activities in multi-density crime hotspots

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s40537-024-00935-4` |
| Full Paper | [https://doi.org/10.1186/s40537-024-00935-4](https://doi.org/10.1186/s40537-024-00935-4) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/342ec46dfefbf443f9baa03a45b512ab5cfb86fc](https://www.semanticscholar.org/paper/342ec46dfefbf443f9baa03a45b512ab5cfb86fc) |
| Source | [https://journalclub.io/episodes/multi-density-crime-predictor-an-approach-to-forecast-criminal-activities-in-multi-density-crime-hotspots](https://journalclub.io/episodes/multi-density-crime-predictor-an-approach-to-forecast-criminal-activities-in-multi-density-crime-hotspots) |
| Source | [https://www.semanticscholar.org/paper/342ec46dfefbf443f9baa03a45b512ab5cfb86fc](https://www.semanticscholar.org/paper/342ec46dfefbf443f9baa03a45b512ab5cfb86fc) |
| Year | 2026 |
| Citations | 20 |
| Authors | Eugenio Cesario, Paolo Lindia, Andrea Vinci |
| Paper ID | `bad41bab-371b-4d52-9ca0-a10187f4d183` |

## Classification

- **Problem Type:** crime forecasting and hotspot detection
- **Domain:** Machine Learning & AI
- **Sub-domain:** Crime data analysis
- **Technique:** MD-CrimePredictor
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents the MD-CrimePredictor, a method for forecasting criminal activities in urban environments by detecting multi-density crime hotspots and applying regression models like SARIMA and LSTM. Engineers should care because this approach leverages spatio-temporal crime data to improve resource allocation and crime prevention strategies.

## Key Contribution

**Introduction of a multi-density clustering approach combined with regression models for effective crime forecasting.**

## Problem

The uneven distribution of crime in urban areas necessitates effective prediction models to allocate police resources efficiently.

## Method

**Approach:** MD-CrimePredictor detects multi-density crime hotspots using a clustering algorithm and then applies SARIMA and LSTM models to forecast crime trends in those hotspots. The method automatically computes densities and shapes of detected regions without predefined divisions.

**Algorithm:**

1. 1. Gather spatio-temporal crime data.
2. 2. Apply multi-density clustering algorithm (CHD) to detect crime hotspots.
3. 3. For each hotspot, analyze data to discover a specific regressive model.
4. 4. Train SARIMA and LSTM models on the data from each hotspot.
5. 5. Evaluate the performance of both models using error measures.
6. 6. Ensemble the models if beneficial for improved accuracy.

**Input:** Spatio-temporal crime data (e.g., location, time, type of crime).

**Output:** Forecasted number of crimes in each detected hotspot over specified time horizons.

**Key Parameters:**

- `SARIMA parameters: p, d, q (not specified in detail)`
- `LSTM parameters: number of layers, number of units per layer (not specified in detail)`
- `Clustering parameters: density thresholds (not specified in detail)`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Chicago crime data spanning 19 years with over two million crime events.

**Results:**

- Accuracy of crime forecasting (exact values not specified).

**Compared against:** Traditional density-based clustering methods like DBSCAN.

**Improvement:** Higher accuracy of SARIMA over LSTM, specific percentage improvement not stated.

## Implementation Guide

**Data Structures:** DataFrame for crime data, List for detected hotspots

**Dependencies:** Pandas for data manipulation, Statsmodels for SARIMA, TensorFlow/Keras for LSTM

**Core Operation:**

```python
crime_forecast = MD_CrimePredictor(crime_data).predict()
```

**Watch Out For:**

- Ensure the crime data is preprocessed correctly for time series analysis.
- Parameter tuning for SARIMA and LSTM is crucial for accuracy.
- Multi-density clustering may require careful selection of parameters to avoid noise.

## Use This When

- You need to predict crime trends in urban areas with varying crime densities.
- You have access to extensive historical crime data.
- You want to improve police resource allocation based on predictive analytics.

## Don't Use When

- The crime data is sparse or lacks temporal resolution.
- You require real-time predictions without historical data.
- The urban environment does not exhibit multi-density characteristics.

## Key Concepts

multi-density clustering, SARIMA, LSTM, crime hotspots, spatio-temporal analysis, regression models

## Connects To

- ARIMA
- DBSCAN
- K-means clustering
- LSTM
- crime data mining

## Prerequisites

- Understanding of time series analysis
- Familiarity with clustering algorithms
- Knowledge of regression techniques

## Limitations

- Performance may degrade with insufficient or noisy data.
- Requires significant computational resources for large datasets.
- The effectiveness of the model is contingent on the quality of input data.

## Open Questions

- How can the model be adapted for real-time crime prediction?
- What additional features could enhance the accuracy of crime forecasts?

## Abstract

They decided to use a combination of two different technologies: SARIMA and LSTM. They would build, train, and test both independently, and then consider if they should be ensembled together. Let's learn a little bit more about these two model types. SARIMA, or Seasonal AutoRegressive Integrated Moving Average, is an extension of the ARIMA model that has been modified to handle seasonal time series data. The AutoRegressive (AR) component models a time series as a linear combination of its past values, using lagged observations as predictors. The Integrated (I) component applies differencing to remove trends and make the series stationary. The Moving Average (MA) component captures dependencies on past forecast errors, adjusting predictions based on previously observed deviations. SARIMA extends this by adding seasonal autoregressive (SAR), seasonal moving average (SMA), and
