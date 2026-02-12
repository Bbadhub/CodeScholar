# The Kernel Density Estimation Technique for Spatio-Temporal Distribution and Mapping of Rain Heights over South Africa: The Effects on Rain-Induced Attenuation

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/atmos15111354` |
| Full Paper | [https://doi.org/10.3390/atmos15111354](https://doi.org/10.3390/atmos15111354) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/bae45165a99e54a42c41c1a6c55ae1db4e470539](https://www.semanticscholar.org/paper/bae45165a99e54a42c41c1a6c55ae1db4e470539) |
| Source | [https://journalclub.io/episodes/the-kernel-density-estimation-technique-for-spatio-temporal-distribution-and-mapping-of-rain-heights-over-south-africa-the-effects-on-rain-induced-attenuation](https://journalclub.io/episodes/the-kernel-density-estimation-technique-for-spatio-temporal-distribution-and-mapping-of-rain-heights-over-south-africa-the-effects-on-rain-induced-attenuation) |
| Source | [https://www.semanticscholar.org/paper/bae45165a99e54a42c41c1a6c55ae1db4e470539](https://www.semanticscholar.org/paper/bae45165a99e54a42c41c1a6c55ae1db4e470539) |
| Year | 2026 |
| Citations | 8 |
| Authors | Y. B. Lawal, P. Owolawi, Chunling Tu, E. V. van Wyk, J. S. Ojo |
| Paper ID | `034d9a5c-cae1-42ed-99c1-42ad036ecb2f` |

## Classification

- **Problem Type:** spatio-temporal distribution estimation
- **Domain:** Optimization & Operations Research
- **Sub-domain:** Meteorological data analysis
- **Technique:** Kernel Density Estimation (KDE)
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

The paper presents a Kernel Density Estimation (KDE) technique to estimate the spatio-temporal distribution of rain heights across South Africa, which is crucial for understanding rain-induced attenuation on communication systems. Engineers should care because accurate rain height predictions can optimize network performance in regions affected by high rain attenuation.

## Key Contribution

**Introduction of a KDE-based method for estimating seasonal rain heights and its impact on rain-induced attenuation in communication systems.**

## Problem

The need to accurately predict rain heights to mitigate rain-induced attenuation effects on communication links operating above 10 GHz.

## Method

**Approach:** The method uses atmospheric temperature and geopotential height data to estimate rain heights using KDE. It applies different kernel functions to model the probability density function of rain heights and identifies the optimal kernel for accurate estimation.

**Algorithm:**

1. 1. Collect atmospheric temperature and geopotential height data from the Copernicus Climate Data Store.
2. 2. Compute the zero-degree isotherm height (ZDIH) from the data.
3. 3. Calculate daily rain heights using the formula hr = ho + 0.36 (km).
4. 4. Apply KDE using various kernel functions (Gaussian, Epanechnikov, Triangular, Rectangular) to estimate the probability density function of rain heights.
5. 5. Optimize the bandwidth for each kernel to minimize Integrated Squared Errors (ISE).
6. 6. Validate the estimated rain heights against measured data.
7. 7. Generate contour maps of seasonal rain heights.

**Input:** Atmospheric temperature and geopotential height data at multiple pressure levels.

**Output:** Estimated seasonal rain heights and contour maps showing spatial distribution.

**Key Parameters:**

- `bandwidth: optimized per kernel`
- `sample_size: m (number of observations)`
- `standard_deviation: σ (calculated from data)`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Atmospheric temperature and geopotential height data from Copernicus Climate Data Store, Measured rain height data from nine stations in South Africa

**Results:**

- Correlation coefficient: 0.997
- Maximum percentage difference: 5.3%

**Compared against:** International Telecommunication Union (ITU) recommended rain heights

**Improvement:** Significantly improved accuracy in estimating rain heights compared to ITU recommendations.

## Implementation Guide

**Data Structures:** Arrays for storing atmospheric data, Data frames for managing seasonal rain height estimates

**Dependencies:** NumPy for numerical computations, SciPy for statistical functions, Pandas for data manipulation, Matplotlib for plotting contour maps

**Core Operation:**

```python
rain_heights = KDE(data) # Apply KDE to atmospheric data to estimate rain heights
```

**Watch Out For:**

- Ensure the bandwidth is optimized for each kernel to avoid over-smoothing.
- Validate the KDE results against measured data to ensure reliability.
- Consider seasonal variations when interpreting results.

## Use This When

- You need to estimate rain heights for communication network planning.
- You are working in regions with high rain-induced signal attenuation.
- You require seasonal variations in rain height for meteorological studies.

## Don't Use When

- You have access to localized radar data that provides accurate rain height measurements.
- You need real-time rain height data for immediate decision-making.
- The computational resources are limited for processing large datasets.

## Key Concepts

Kernel Density Estimation, Probability Density Function, Rain Height Estimation, Rain-Induced Attenuation

## Connects To

- Gaussian Mixture Models
- Statistical Analysis Techniques
- Machine Learning for Rainfall Prediction

## Prerequisites

- Understanding of probability density functions
- Familiarity with kernel methods
- Basic knowledge of atmospheric science

## Limitations

- Dependent on the quality of input atmospheric data.
- May not perform well in regions with sparse data.
- Assumes that the underlying distribution can be modeled by the chosen kernels.

## Open Questions

- How can machine learning techniques further enhance rain height estimation?
- What are the implications of localized climate changes on rain height distributions?

## Abstract

We have to start with a Probability Density Function (PDF). Not to be confused with a Probability Distribution Function, which would show us a distribution (the probability of all possible values a random variable can have). A Probability Density Function shows us the likelihood of a variable having a value within a specific range of values, like rain height measurements through the summer. A higher density of rain height measurements that fall in the specific range, the more likely it is that rain will fall in that range in the future. The Density function is the one that we are interested in today. The function is the equation that data is fed into to calculate the probability spread. The visual expression of this function is a line graph with a parabolic arc. Let's use the famous bell shaped curve as an example. The middle of the curve represents the highest density of data points. The X axis is the
