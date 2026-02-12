# Leveraging Google Earth Engine and Machine Learning to Estimate Evapotranspiration in a Commercial Forest Plantation

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/rs16152726` |
| Full Paper | [https://doi.org/10.3390/rs16152726](https://doi.org/10.3390/rs16152726) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/a59c20fdccc0fbba8d66d17943494ea2fd7e1913](https://www.semanticscholar.org/paper/a59c20fdccc0fbba8d66d17943494ea2fd7e1913) |
| Source | [https://journalclub.io/episodes/leveraging-google-earth-engine-and-machine-learning-to-estimate-evapotranspiration-in-a-commercial-forest-plantation](https://journalclub.io/episodes/leveraging-google-earth-engine-and-machine-learning-to-estimate-evapotranspiration-in-a-commercial-forest-plantation) |
| Source | [https://www.semanticscholar.org/paper/a59c20fdccc0fbba8d66d17943494ea2fd7e1913](https://www.semanticscholar.org/paper/a59c20fdccc0fbba8d66d17943494ea2fd7e1913) |
| Year | 2026 |
| Citations | 3 |
| Authors | S. Gokool, R. Kunz, A. Clulow, Michele Toucher |
| Paper ID | `4e24bb9c-93c9-4ac6-9bd8-9dab80402c33` |

## Classification

- **Problem Type:** evapotranspiration estimation
- **Domain:** Machine Learning & AI
- **Sub-domain:** Remote Sensing and Environmental Modeling
- **Technique:** Ensemble Machine Learning Model (EMLM)
- **Technique Category:** classification_model
- **Type:** novel

## Summary

This study developed a method to estimate evapotranspiration (ET) in commercial forest plantations using satellite-derived leaf area index (LAI) and machine learning techniques. Engineers should care because this approach leverages Google Earth Engine for efficient data processing and can improve water resource management in forestry.

## Key Contribution

**An ensemble machine learning model was proposed to estimate crop coefficients (Kc) from satellite-derived LAI, which was then used to estimate ET.**

## Problem

Accurate estimation of water use in commercial afforestation is crucial for sustainable timber production and water resource management.

## Method

**Approach:** The method uses satellite-derived LAI to estimate crop coefficients (Kc) through machine learning models. The best-performing model is then used to estimate daily evapotranspiration (ETa) based on in situ measurements of reference evapotranspiration (ETo).

**Algorithm:**

1. 1. Acquire satellite-derived LAI data from MODIS using Google Earth Engine.
2. 2. Collect in situ measurements of ET and ETo.
3. 3. Calculate Kc using the formula Kc = ETa / ETo.
4. 4. Train various machine learning models (GLM, CART, kNN, RF, SVM) to predict Kc from LAI.
5. 5. Use k-fold cross-validation to validate model performance.
6. 6. Select the best-performing model (EMLM) to generate monthly Kc estimates.
7. 7. Estimate daily ETa using the formula ETa = Kc * ETo.

**Input:** Satellite-derived LAI data and in situ measurements of ETo and ET.

**Output:** Estimated daily evapotranspiration (ETa) values.

**Key Parameters:**

- `LAI: derived from MODIS product (MCD15A3H V6)`
- `ETo: calculated using FAO56 method`
- `Kc: capped at 1.3 for humid environments`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** MODIS LAI product (MCD15A3H V6), in situ ET and ETo measurements

**Results:**

- RMSE for Kc: 0.05
- R2 for Kc: 0.68
- RMSE for ETa: 0.51 mm d−1
- R2 for ETa: 0.90

**Compared against:** Traditional Kc estimation methods based on FAO56

**Improvement:** The EMLM showed a 1.00% underestimation of ETa compared to in situ measurements.

## Implementation Guide

**Data Structures:** Data frames for LAI, Kc, and ETa time series

**Dependencies:** Google Earth Engine API, R statistical software, caret and caretEnsemble packages

**Core Operation:**

```python
Kc_est = train_model(LAI_data, ET_data); ETa = Kc_est * ETo;
```

**Watch Out For:**

- Ensure LAI data is free from cloud contamination.
- Kc values should be capped appropriately.
- Model performance may vary seasonally.

## Use This When

- Estimating water use in commercial forestry.
- Needing to leverage satellite data for environmental modeling.
- Working in regions with limited in situ data.

## Don't Use When

- Data is heavily cloud-contaminated and not filtered.
- High spatial heterogeneity in vegetation characteristics exists.
- Water stress conditions are prevalent and not accounted for.

## Key Concepts

evapotranspiration, leaf area index, crop coefficient, machine learning, remote sensing, Google Earth Engine

## Connects To

- FAO56 method for ET estimation
- MODIS satellite data processing
- Other machine learning algorithms for environmental data

## Prerequisites

- Understanding of evapotranspiration concepts
- Familiarity with machine learning techniques
- Knowledge of remote sensing data processing

## Limitations

- Site-specific nature of Kc estimates may limit transferability.
- Potential inaccuracies in satellite-derived LAI due to cloud cover.
- Kc estimates may not account for soil water availability.

## Open Questions

- How can the model be adapted for different vegetation types?
- What additional variables could improve Kc estimation accuracy?

## Abstract

You've probably heard of both deforestation and reforestation. But what on earth is afforestation? Afforestation is the process of planting and growing trees where none originally grew (or they haven’t grown in a long time). Afforestation is not replanting a recently-cut forest, it’s creating a forest where there was previously grassland, desert, or even ice, for example. Though it sounds a bit odd, afforestation is a key practice in sustainable timber production. Rather than chopping down existing forests, a company will grow a brand new forest, chop it down, and repeat. But, this technique does have its drawbacks. Commercial afforestation is extremely water-hungry. And as a result, many countries regulate it tightly. In South Africa, where today’s research takes place, you can’t grow a new forest without first being issued a water license. The licenses are granted based on the government's statistical models that show how that proposed crop would affect the overall energy balance, environment and water table. In order to create those models, the government needs to know a key metric for the species of tree you want to grow: Evapotranspiration (ET).
