# Well-Being of the Baltic Herring and Bycatch Fish Species from FAO Major Fishing Areas 27 According to Microplastic Pollution

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/ani15162381` |
| Full Paper | [https://doi.org/10.3390/ani15162381](https://doi.org/10.3390/ani15162381) |
| Source | [https://journalclub.io/episodes/well-being-of-the-baltic-herring-and-bycatch-fish-species-from-fao-major-fishing-areas-27-according-to-microplastic-pollution](https://journalclub.io/episodes/well-being-of-the-baltic-herring-and-bycatch-fish-species-from-fao-major-fishing-areas-27-according-to-microplastic-pollution) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `e991e7b0-18ce-441a-aa42-12c025e5fca0` |

## Classification

- **Problem Type:** Environmental monitoring and assessment of pollution impact on aquatic life.
- **Domain:** Environmental Science
- **Sub-domain:** Marine Pollution Assessment
- **Technique:** Microplastic Analysis and Health Indices Assessment
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

The study investigates the impact of microplastic pollution on the well-being of Baltic herring and bycatch fish species by analyzing their biological tissues and the presence of microplastics. Engineers should care because this research provides insights into environmental monitoring and assessment techniques that can be applied to other ecosystems affected by pollution.

## Key Contribution

**Introduction of novel health indices (GILSI and GITI) for assessing fish well-being in relation to microplastic pollution.**

## Problem

The increasing presence of microplastics in marine environments poses a significant threat to fish health and ecosystem stability.

## Method

**Approach:** The method involves dissolving fish tissues using potassium hydroxide to isolate microplastics, followed by filtration and manual identification of plastic particles. Health indices are calculated to assess the well-being of fish species based on their biometric data and microplastic content.

**Algorithm:**

1. 1. Collect fish samples and measure total body length and mass.
2. 2. Dissect organs (gills, liver, gastrointestinal tract) and weigh them.
3. 3. Digest organs in 10% potassium hydroxide to isolate microplastics.
4. 4. Filter the digested samples through a fine mesh filter.
5. 5. Identify and categorize microplastics based on size, shape, and color.
6. 6. Calculate health indices (K, HSI, GILSI, GITI) using the specified formulas.
7. 7. Perform statistical analysis and principal component analysis (PCA) to assess relationships.

**Input:** Fish samples (gills, liver, gastrointestinal tract) and their biometric measurements.

**Output:** Quantified microplastic presence and calculated health indices for each fish species.

**Key Parameters:**

- `potassium_hydroxide_concentration: 10%`
- `K_factor_formula: K = (total fish weight [g] × 100)/(total fish length [cm]³)`
- `HSI_formula: HSI = liver weight [g]/total fish weight [g]`
- `GILSI_formula: GILSI = gills weight [g]/total fish weight [g]`
- `GITI_formula: GITI = gastrointestinal tract weight [g]/total fish weight [g]`

**Complexity:** not stated

## Benchmarks

**Tested on:** Fish samples from the southern and central Baltic Sea, including Baltic herring, sprat, cod, flounder, long-spined bullhead, and lumpfish.

**Results:**

- Microplastic abundance per fish, health indices (K, HSI, GILSI, GITI) values.

**Compared against:** Previous studies on fish health without microplastic analysis.

**Improvement:** Introduced new health indices (GILSI and GITI) for a more comprehensive evaluation of fish health.

## Implementation Guide

**Data Structures:** Arrays for storing fish biometric data and microplastic counts., Dictionaries for mapping health indices.

**Dependencies:** Statistical analysis software (e.g., R, Python libraries for PCA)., Laboratory equipment for microplastic analysis.

**Core Operation:**

```python
for each fish in fish_samples: calculate_health_indices(fish); analyze_microplastics(fish.organs)
```

**Watch Out For:**

- Ensure proper contamination prevention during sample processing.
- Be aware of the limitations of microplastic identification methods.
- Standardize health indices across species for accurate comparisons.

## Use This When

- Assessing the impact of pollution on aquatic ecosystems.
- Developing monitoring protocols for microplastic contamination in marine life.
- Evaluating fish health in relation to environmental stressors.

## Don't Use When

- When studying freshwater species not affected by microplastics.
- In environments where microplastics are not a concern.
- For species that do not have established health indices.

## Key Concepts

microplastics, fish health indices, environmental monitoring, biometric analysis, principal component analysis

## Connects To

- Environmental Toxicology
- Marine Biology
- Pollution Assessment Techniques

## Prerequisites

- Understanding of fish biology and ecology
- Knowledge of statistical analysis methods
- Familiarity with microplastic pollution issues

## Limitations

- The method relies on manual identification of microplastics, which can be time-consuming.
- Potential for variability in health indices due to species differences.
- Limited to the specific fish species studied and may not generalize to others.

## Open Questions

- What are the long-term effects of microplastic ingestion on fish populations?
- How can these health indices be adapted for other aquatic species?

## Abstract

They needed to dissolve the fish’s biological tissues while preserving the plastic particles. They used a potassium hydroxide solution for that, a strong base that breaks down proteins and other organic compounds but leaves synthetic polymers intact. Once that was over, they sent the samples through an extremely fine mesh filter, then dug into the process of identifying the plastic bits. This is, oddly enough, largely a manual process, tiny piece by tiny piece.
