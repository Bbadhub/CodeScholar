# RASCAL v1.0: an open-source tool for climatological time series reconstruction and extension

## Access

| Field | Value |
|-------|-------|
| DOI | `10.5194/gmd-17-7245-2024` |
| Full Paper | [https://doi.org/10.5194/gmd-17-7245-2024](https://doi.org/10.5194/gmd-17-7245-2024) |
| Source | [https://journalclub.io/episodes/rascal-v10-an-open-source-tool-for-climatological-time-series-reconstruction-and-extension](https://journalclub.io/episodes/rascal-v10-an-open-source-tool-for-climatological-time-series-reconstruction-and-extension) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `a3a2f3d3-d650-4766-a8ea-58ca056ad88f` |

## Classification

- **Problem Type:** empirical statistical downscaling
- **Domain:** Machine Learning & AI
- **Sub-domain:** Climatological time series reconstruction
- **Technique:** RASCAL (Reconstruction by AnalogS of ClimatologicAL time series)
- **Technique Category:** framework
- **Type:** novel

## Summary

RASCAL v1.0 is an open-source Python tool designed for the reconstruction and extension of climatological time series, particularly in areas with limited observational data. It employs an analog method combined with principal component analysis (PCA) to link large-scale circulation patterns with local atmospheric features, making it valuable for climate research in regions with significant local effects.

## Key Contribution

**Introduction of RASCAL, an open-source tool that utilizes an analog method for climatological time series reconstruction and extension.**

## Problem

The decline in in situ meteorological observations poses risks of losing critical climate data, especially in regions with complex local effects.

## Method

**Approach:** RASCAL uses an analog method to identify historical days with similar large-scale atmospheric conditions and predicts local weather patterns based on these analogs. It combines this approach with PCA to reduce dimensionality and improve the selection of analog days.

**Algorithm:**

1. 1. Preprocess observational and reanalysis data.
2. 2. Select predictor variables based on atmospheric dynamics.
3. 3. Perform PCA on the predictor field to obtain principal components.
4. 4. Identify N historical days with similar predictors to the target day.
5. 5. Use weighted averaging of the analogs to reconstruct the target day.
6. 6. Apply bias reduction techniques if necessary.
7. 7. Evaluate the reconstruction performance using skill metrics.

**Input:** Homogeneous time series of observational data and reanalysis dataset covering the reconstruction period.

**Output:** Reconstructed climatological time series with statistical properties resembling observations.

**Key Parameters:**

- `pool_size: number of analog days to consider (e.g., 10)`
- `vw_size: number of days to exclude from the pool (e.g., 1)`
- `N: number of principal components to use (e.g., 5)`
- `scaling: scaling option for PCA (0: unscaled, 1: unit variance, 2: eigenvalue scaled)`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Central Spain mountainous and urbanized areas

**Results:**

- R2, standard deviation, bias

**Compared against:** ERA20C, ERA20CM reanalysis

**Improvement:** RASCAL outperformed ERA20C and ERA20CM in terms of R2, standard deviation, and bias.

## Implementation Guide

**Data Structures:** Station class for observational data, Predictor class for predictor variables, Analogs class for analog selection, RSkill class for evaluation metrics

**Dependencies:** Python, NumPy, xarray, EOFs library

**Core Operation:**

```python
reconstructed_series = RASCAL.predictor.predict(target_day)
```

**Watch Out For:**

- Ensure the observational data is homogeneous and of sufficient length.
- Select predictor variables carefully to maintain strong relationships with the predictand.
- Be cautious of changes in land use that may affect data quality.

## Use This When

- You need to reconstruct missing climate data in regions with limited observations.
- You are working on climate variability analyses in mountainous or urbanized areas.
- You want to extend short-term climate forecasts using historical data.

## Don't Use When

- You have a dense network of reliable in situ observations.
- You require real-time weather predictions.
- You are working in regions with significant land use changes affecting data homogeneity.

## Key Concepts

analog method, principal component analysis, empirical downscaling, climatological time series

## Connects To

- pyESD (empirical downscaling library)
- PCA techniques
- analog weather generators

## Prerequisites

- Understanding of statistical methods
- Familiarity with climate data
- Knowledge of PCA

## Limitations

- Requires long-term observational data for effective training
- Sensitive to changes in land use
- Cannot replicate unobserved events

## Open Questions

- How can RASCAL be adapted for real-time applications?
- What improvements can be made to enhance the accuracy of analog selections?

## Abstract

Today, November 11th 2024, marks the first day of COP29, the 29th meeting of the Conference of the Parties. COP was created by the UNFCCC, the United Nations Framework Convention on Climate Change, to bring countries together to negotiate and set international climate action goals. COP29 is happening in Baku, Azerbaijan, and will last nearly two weeks. During this time, member countries will set their climate change policies for
