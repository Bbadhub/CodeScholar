# Data-driven analysis of hysteresis and stability in perovskite solar cells using machine learning

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.egyai.2025.100503` |
| Full Paper | [https://doi.org/10.1016/j.egyai.2025.100503](https://doi.org/10.1016/j.egyai.2025.100503) |
| Source | [https://journalclub.io/episodes/data-driven-analysis-of-hysteresis-and-stability-in-perovskite-solar-cells-using-machine-learning](https://journalclub.io/episodes/data-driven-analysis-of-hysteresis-and-stability-in-perovskite-solar-cells-using-machine-learning) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `8a75ca7d-566e-4cc4-96dd-95df81d6b8a9` |

## Classification

- **Problem Type:** anomaly detection
- **Domain:** Machine Learning & AI
- **Sub-domain:** Data-driven analysis
- **Technique:** Machine Learning for Hysteresis Analysis
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This paper presents a machine learning approach to analyze hysteresis and stability in perovskite solar cells (PSCs) by evaluating their JV curves. Engineers should care because understanding and mitigating hysteresis can lead to more reliable performance metrics for solar cells, ultimately improving their efficiency and market viability.

## Key Contribution

**A novel machine learning framework for analyzing hysteresis in JV curves of perovskite solar cells.**

## Problem

The real-world problem is the inconsistent performance of perovskite solar cells due to hysteresis in their JV curves.

## Method

**Approach:** The method involves collecting JV curve data from PSCs and applying machine learning algorithms to identify patterns and anomalies related to hysteresis. This analysis helps in understanding the stability of the solar cells under different measurement conditions.

**Algorithm:**

1. 1. Collect JV curve data from perovskite solar cells under various voltage sweeps.
2. 2. Preprocess the data to normalize and clean it.
3. 3. Apply machine learning algorithms to model the relationship between voltage sweep direction and resulting current density.
4. 4. Analyze the model outputs to identify hysteresis patterns.
5. 5. Validate the model using additional datasets.
6. 6. Use insights to improve PSC design and measurement protocols.

**Input:** JV curve data from perovskite solar cells, including voltage and current density measurements.

**Output:** Insights into hysteresis behavior and stability metrics of PSCs.

**Key Parameters:**

- `sweep_speed: 0.1 V/s`
- `data_samples: 1000`

**Complexity:** not stated

## Benchmarks

**Tested on:** JV curve datasets from various perovskite solar cell experiments

**Results:**

- hysteresis magnitude, stability index

**Compared against:** Traditional analysis methods without machine learning

**Improvement:** Significant reduction in hysteresis identification time compared to traditional methods.

## Implementation Guide

**Data Structures:** DataFrame for storing JV curve data, Model object for machine learning algorithms

**Dependencies:** pandas, scikit-learn, numpy

**Core Operation:**

```python
model.fit(jv_data) # Train model on JV curve data
```

**Watch Out For:**

- Ensure data is properly normalized before analysis
- Be cautious of overfitting the model to specific datasets
- Validate results with independent datasets

## Use This When

- Analyzing performance inconsistencies in solar cells
- Improving the design of photovoltaic devices
- Conducting research on solar energy technologies

## Don't Use When

- Working with non-hysteretic solar cell technologies
- When real-time analysis is required without prior data collection
- In scenarios where data is scarce or unreliable

## Key Concepts

hysteresis, JV curve, perovskite solar cells, machine learning, data analysis

## Connects To

- Anomaly detection algorithms
- Time series analysis
- Statistical modeling techniques

## Prerequisites

- Understanding of machine learning concepts
- Familiarity with photovoltaic technologies
- Knowledge of data preprocessing techniques

## Limitations

- Requires a substantial amount of high-quality data
- May not generalize well to all types of solar cells
- Performance heavily depends on the choice of machine learning model

## Open Questions

- How can this approach be adapted for real-time monitoring?
- What additional factors contribute to hysteresis in other photovoltaic technologies?

## Abstract

To evaluate performance of a PSC, or any other photovoltaic, you measure a device’s JV curve, which is short for current-density-versus-voltage. This curve is produced by sweeping an external voltage across the device and measuring the resulting current density under illumination. This gives you the short-circuit current, open-circuit voltage, fill factor, and ultimately, power conversion efficiency. In an ideal situation (on a perfect device), the JV curve is stable and consistent regardless of how you measure it. But that’s not the case with PSC. They exhibit a phenomenon called hysteresis, where the shape of the JV curve depends on the direction or speed of the voltage sweep you perform. So, if you measure the curve from the bottom to the top, that is: from 0 to the open-circuit voltage (this is called a “forward scan”), you’ll get one reading. If you then measure it again the opposite way, from the top to the bottom (this is called a “backward scan”) you’ll get a different reading. This mismatch is hysteresis.
