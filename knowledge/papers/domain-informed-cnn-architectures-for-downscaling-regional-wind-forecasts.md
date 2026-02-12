# Domain-informed CNN architectures for downscaling regional wind forecasts

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.egyai.2025.100485` |
| Full Paper | [https://doi.org/10.1016/j.egyai.2025.100485](https://doi.org/10.1016/j.egyai.2025.100485) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/981b3c4b68a15e40ad80a208f46e99191455240f](https://www.semanticscholar.org/paper/981b3c4b68a15e40ad80a208f46e99191455240f) |
| Source | [https://journalclub.io/episodes/domain-informed-cnn-architectures-for-downscaling-regional-wind-forecasts](https://journalclub.io/episodes/domain-informed-cnn-architectures-for-downscaling-regional-wind-forecasts) |
| Source | [https://www.semanticscholar.org/paper/981b3c4b68a15e40ad80a208f46e99191455240f](https://www.semanticscholar.org/paper/981b3c4b68a15e40ad80a208f46e99191455240f) |
| Year | 2026 |
| Citations | 1 |
| Authors | Alexander M. Campbell, S. Warder, B. Bhaskaran, M. Piggott |
| Paper ID | `89897645-8338-4641-beff-ac6743c06f70` |

## Classification

- **Problem Type:** downscaling regional weather forecasts
- **Domain:** Machine Learning & AI
- **Sub-domain:** Convolutional Neural Networks (CNNs)
- **Technique:** Domain-informed CNN architectures
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents domain-informed CNN architectures designed to enhance the downscaling of regional wind forecasts from coarse Numerical Weather Prediction (NWP) models. Engineers should care because this approach enables more accurate local wind predictions crucial for applications like wind energy generation.

## Key Contribution

**Introduction of domain-informed CNN architectures specifically tailored for downscaling wind forecasts.**

## Problem

The need for high-resolution wind forecasts around specific locations, such as wind turbines, which are not adequately captured by coarse global NWP models.

## Method

**Approach:** The method utilizes CNN architectures that incorporate domain knowledge to improve the accuracy of downscaled wind forecasts. By integrating physical principles and local atmospheric conditions, the model learns to predict finer-scale wind patterns.

**Algorithm:**

1. 1. Gather coarse wind forecast data from NWP models.
2. 2. Integrate domain-specific features related to local geography and atmospheric conditions.
3. 3. Design and train a CNN architecture using the integrated data.
4. 4. Validate the model against high-resolution observational data.
5. 5. Use the trained model to generate downscaled wind forecasts.

**Input:** Coarse wind forecast data from NWP models and domain-specific features.

**Output:** High-resolution wind forecasts tailored to specific locations.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 32`
- `num_epochs: 100`

**Complexity:** Not stated

## Benchmarks

**Tested on:** High-resolution observational wind data, Coarse NWP model outputs

**Results:**

- accuracy: not stated
- mean absolute error: not stated

**Compared against:** Standard downscaling methods, Other CNN architectures

**Improvement:** Not stated

## Implementation Guide

**Data Structures:** Numpy arrays for data handling, TensorFlow or PyTorch for model building

**Dependencies:** TensorFlow, Keras, NumPy, Pandas

**Core Operation:**

```python
model.fit(X_train, y_train, epochs=num_epochs, batch_size=batch_size)
```

**Watch Out For:**

- Ensure proper integration of domain features.
- Monitor for overfitting due to high model complexity.
- Validate against diverse geographical conditions.

## Use This When

- You need to improve local wind forecasts for renewable energy applications.
- You have access to both coarse NWP data and high-resolution observational data.
- You want to leverage domain knowledge in weather prediction.

## Don't Use When

- You require real-time predictions without prior training.
- You have limited computational resources.
- You are working with non-weather-related forecasting tasks.

## Key Concepts

Convolutional Neural Networks, Numerical Weather Prediction, Downscaling, Domain knowledge integration

## Connects To

- Deep learning for time series forecasting
- Spatial data analysis
- Geographical information systems

## Prerequisites

- Understanding of CNN architectures
- Familiarity with weather forecasting principles
- Knowledge of downscaling techniques

## Limitations

- Dependent on the quality of input NWP data.
- May require significant computational resources for training.
- Performance may vary based on geographical diversity.

## Open Questions

- How can the model be adapted for other meteorological variables?
- What are the implications of using different CNN architectures for this task?

## Abstract

In weather forecasting, the foundation of the field is something called Numerical Weather Prediction, or NWP. NWP simulates the evolution of the atmosphere over time, using the laws of physics; that is: fluid dynamics, thermodynamics, and radiation models. It takes in the current state of the atmosphere from observations, then integrates the equations forward to produce future states. NWP is the global standard for everything from hurricane prediction to daily weather apps, and it’s only possible by way of massive supercomputers that crunch through billions of variables across global grids, all day long. But there’s a tradeoff inherent in these systems. The finer the spatial resolution, the more compute it takes to run. Because of this, global NWP models are typically limited to grid resolutions around 10 to 30 kilometers. That’s pretty coarse. You can’t resolve wind patterns around mountain ridges, or the land-sea gradients that matter in coastal areas. And you definitely can’t resolve wind flows at the scale of individual wind turbines. If you need to predict the unique weather that is only occurring around a specific set of turbines, you need another option.
