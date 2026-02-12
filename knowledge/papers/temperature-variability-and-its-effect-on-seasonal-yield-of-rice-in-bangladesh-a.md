# Temperature variability and its effect on seasonal yield of rice in Bangladesh: a long-term trend assessment

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1080/23311932.2024.2447903` |
| Full Paper | [https://doi.org/10.1080/23311932.2024.2447903](https://doi.org/10.1080/23311932.2024.2447903) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/c7a081bddf078962fcb4af326c90e4ce9bc4b7ad](https://www.semanticscholar.org/paper/c7a081bddf078962fcb4af326c90e4ce9bc4b7ad) |
| Source | [https://journalclub.io/episodes/temperature-variability-and-its-effect-on-seasonal-yield-of-rice-in-bangladesh-a-long-term-trend-assessment](https://journalclub.io/episodes/temperature-variability-and-its-effect-on-seasonal-yield-of-rice-in-bangladesh-a-long-term-trend-assessment) |
| Source | [https://www.semanticscholar.org/paper/c7a081bddf078962fcb4af326c90e4ce9bc4b7ad](https://www.semanticscholar.org/paper/c7a081bddf078962fcb4af326c90e4ce9bc4b7ad) |
| Year | 2026 |
| Citations | 10 |
| Authors | Md Abdullah Al Mamun, Md Abdur Rouf Sarkar, M. Sarker, Andrew M. McKenzie, S. Nihad, Md Arafat Hossain |
| Paper ID | `5142bcd5-7ed3-4008-81ea-f1e4c76e0120` |

## Classification

- **Problem Type:** time series analysis
- **Domain:** Data Structures & Algorithms
- **Sub-domain:** Statistical analysis
- **Technique:** Man-Kendall Test, Wavelet Coherence
- **Technique Category:** statistical_method
- **Type:** adaptation

## Summary

This paper analyzes the impact of temperature variability on rice yields in Bangladesh, utilizing statistical methods to uncover trends in climate data. Engineers should care because the findings can inform agricultural strategies to mitigate the effects of climate change on crop production.

## Key Contribution

**The application of statistical analysis methods to assess the relationship between temperature variability and rice yield trends over time.**

## Problem

The real-world problem motivating this work is the need to adapt agricultural practices in response to climate change effects on crop yields.

## Method

**Approach:** The method involves analyzing daily temperature data to identify trends and their effects on rice yields. Statistical techniques like the Man-Kendall Test and Wavelet Coherence are employed to uncover relationships between temperature fluctuations and crop growth.

**Algorithm:**

1. 1. Collect daily temperature data and rice yield data over a long-term period.
2. 2. Apply descriptive statistics to summarize the data.
3. 3. Use the Man-Kendall Test to identify trends in temperature data.
4. 4. Apply Wavelet Coherence to analyze the relationship between temperature variability and rice yields.
5. 5. Interpret the results to understand the impact of temperature on crop growth.

**Input:** Daily temperature data and rice yield data.

**Output:** Statistical trends and insights on the relationship between temperature variability and rice yields.

**Key Parameters:**

- `significance_level: 0.05`
- `window_size: 30 days`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Daily temperature records and rice yield data from Bangladesh

**Results:**

- trend significance: p-value
- coherence: correlation coefficient

**Compared against:** Previous agricultural yield models not accounting for temperature variability

**Improvement:** Quantitative improvement not stated, but insights lead to better yield predictions.

## Implementation Guide

**Data Structures:** DataFrames for storing temperature and yield data, Arrays for statistical calculations

**Dependencies:** pandas, numpy, scipy, statsmodels

**Core Operation:**

```python
results = man_kendall_test(temperature_data); coherence = wavelet_coherence(temperature_data, yield_data)
```

**Watch Out For:**

- Ensure data quality and completeness
- Select appropriate window sizes for Wavelet analysis
- Interpret p-values correctly in the context of agricultural decisions

## Use This When

- Analyzing the impact of climate variables on agricultural yields
- Developing predictive models for crop production
- Implementing data-driven agricultural strategies

## Don't Use When

- Data is not available or insufficient
- The relationship between variables is already well understood
- Short-term analysis is required

## Key Concepts

temperature variability, rice yield, statistical analysis, climate change, time series, Man-Kendall Test, Wavelet Coherence

## Connects To

- Time series forecasting
- Climate impact modeling
- Agricultural yield prediction

## Prerequisites

- Basic statistics
- Understanding of time series analysis
- Familiarity with agricultural practices

## Limitations

- Results may not generalize to other crops or regions
- Dependence on the quality of historical data
- Potential for confounding variables not accounted for

## Open Questions

- How do other climate factors interact with temperature to affect yields?
- What are the long-term implications of these trends for agricultural policy?

## Abstract

Our paper today looks at how one country, Bangladesh, is using data-science to avoid repeating the mistakes of the past. This research is part of a larger initiative they’re using to equip the agricultural sector with the statistical and computational tools they need to adapt their growing strategies to climate change. In this paper they explore the relationship of temperature to rice yields. The authors use statistical analysis methods to discover trends hidden in daily temperature data over time, and show how they impact crop growth. We’re going to walk through how exactly they’re doing that. We’ll look at descriptive statistics, the Man-Kendall Test, and Wavelet Coherence. We’ll show how these researchers use those tools to get a multifaceted understanding of the variables that are critical to drought intervention. When it established itself as an independent
