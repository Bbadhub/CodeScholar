# Pattern-Based Feature Extraction for Improved Deep Learning in Financial Time Series Classification

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1109/ACCESS.2025.3584251` |
| Full Paper | [https://doi.org/10.1109/ACCESS.2025.3584251](https://doi.org/10.1109/ACCESS.2025.3584251) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/67a585dce49b930db49792f21da7c55482e200ea](https://www.semanticscholar.org/paper/67a585dce49b930db49792f21da7c55482e200ea) |
| Source | [https://journalclub.io/episodes/pattern-based-feature-extraction-for-improved-deep-learning-in-financial-time-series-classification](https://journalclub.io/episodes/pattern-based-feature-extraction-for-improved-deep-learning-in-financial-time-series-classification) |
| Source | [https://www.semanticscholar.org/paper/67a585dce49b930db49792f21da7c55482e200ea](https://www.semanticscholar.org/paper/67a585dce49b930db49792f21da7c55482e200ea) |
| Year | 2026 |
| Citations | 1 |
| Authors | Seyed Ali Hosseini, Francesco Grimaccia, A. Niccolai, Silvia Trimarchi |
| Paper ID | `b1a03ae4-8d2a-407a-8edc-f6df1311e763` |

## Classification

- **Problem Type:** time series classification
- **Domain:** Machine Learning & AI
- **Sub-domain:** Financial Time Series Analysis
- **Technique:** Pattern-Based Feature Extraction
- **Technique Category:** feature_extraction
- **Type:** novel

## Summary

The paper presents a method for extracting structured, geometry-aware features from financial time series data to improve deep learning models' performance in classification tasks. Engineers should care because this approach addresses the limitations of existing models that struggle with noisy and non-stationary data by providing contextually rich features.

## Key Contribution

**Introduction of a pattern-based feature extraction technique that enhances deep learning for financial time series classification.**

## Problem

Traders need to make directional calls based on noisy and non-stationary financial time series data, which traditional models struggle to interpret effectively.

## Method

**Approach:** The method extracts structured features from raw financial time series data by analyzing the geometric properties of price movements. This enables deep learning models to learn from meaningful patterns rather than noise.

**Algorithm:**

1. 1. Collect OHLCV (Open, High, Low, Close, Volume) data.
2. 2. Analyze price movements to identify geometric patterns.
3. 3. Extract features based on the identified patterns.
4. 4. Feed the extracted features into a deep learning model for classification.

**Input:** OHLCV time series data in a structured format.

**Output:** Structured features that represent geometric properties of price movements.

**Key Parameters:**

- `window_size: 30`
- `feature_count: 10`

**Complexity:** not stated

## Benchmarks

**Tested on:** Financial time series datasets from stock markets

**Results:**

- accuracy: not stated
- F1: not stated

**Compared against:** Traditional deep learning models like LSTM and GRU without feature extraction

**Improvement:** Significant improvement over baseline models, exact percentage not stated.

## Implementation Guide

**Data Structures:** DataFrame for OHLCV data, Arrays for extracted features

**Dependencies:** NumPy, Pandas, TensorFlow or PyTorch

**Core Operation:**

```python
features = extract_features(OHLCV_data); model.fit(features, labels)
```

**Watch Out For:**

- Ensure data is preprocessed correctly before feature extraction.
- Watch out for overfitting when using complex features.
- Validate the extracted features with domain experts.

## Use This When

- You need to classify financial time series data with high noise levels.
- Existing deep learning models are underperforming due to lack of structured features.
- You want to leverage geometric properties of price movements for better predictions.

## Don't Use When

- The dataset is small and lacks sufficient time series data.
- Real-time processing is required and feature extraction adds too much latency.
- The problem does not involve classification of time series data.

## Key Concepts

feature extraction, time series analysis, deep learning, geometric patterns

## Connects To

- LSTM
- GRU
- Feature Engineering
- Time Series Forecasting

## Prerequisites

- Understanding of time series data
- Familiarity with deep learning frameworks
- Knowledge of feature extraction techniques

## Limitations

- May not generalize well to all types of financial instruments.
- Requires sufficient historical data for effective feature extraction.
- Complexity of feature extraction may increase computational costs.

## Open Questions

- How can this feature extraction method be adapted for real-time trading systems?
- What other geometric properties could be explored for further improvements?

## Abstract

Time series data is inherently noisy, non-stationary, and locally unpredictable. But traders still need to make directional calls. So they turn to indicators like moving averages, Bollinger Bands, or MACD. And more recently, deep learning and sequence models like LSTM and GRU have been used to learn richer representations directly from the market data. This is a promising direction, for sure, but in practice these models often hit a wall. They’re handed data without context, and expected to find structure in patterns that were never explicitly described. OHLCV data captures price activity, but it doesn’t say much about how prices moved, what shapes they traced, how sharp the turns were, or how compressed the swings were. And when markets are moving fast, those shapes matter. Two 5% moves can have completely different meanings depending on how they got there. Without explicit signals to guide them, models end up modeling noise. What they’re missing is a mechanism for extracting structured, geometry-aware features from the raw price movements. Features that can compress complex temporal patterns into learnable signals.
