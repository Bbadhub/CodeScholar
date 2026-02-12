# A leave-one-out algorithm for contribution analysis in component network meta-analysis

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s12874-025-02619-w` |
| Full Paper | [https://doi.org/10.1186/s12874-025-02619-w](https://doi.org/10.1186/s12874-025-02619-w) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/2cd5d9ab7fbc610dab18fcfa7d3515b8ee757ccd](https://www.semanticscholar.org/paper/2cd5d9ab7fbc610dab18fcfa7d3515b8ee757ccd) |
| Source | [https://journalclub.io/episodes/a-leave-one-out-algorithm-for-contribution-analysis-in-component-network-meta-analysis](https://journalclub.io/episodes/a-leave-one-out-algorithm-for-contribution-analysis-in-component-network-meta-analysis) |
| Source | [https://www.semanticscholar.org/paper/2cd5d9ab7fbc610dab18fcfa7d3515b8ee757ccd](https://www.semanticscholar.org/paper/2cd5d9ab7fbc610dab18fcfa7d3515b8ee757ccd) |
| Year | 2026 |
| Citations | 3 |
| Authors | Yunhe Mao, Yiwen Shen, Qinbo Yang, Qingyang Shi, Sheyu Li |
| Paper ID | `e7713d1c-6f79-4fa7-9a25-632895eb9b0d` |

## Classification

- **Problem Type:** component network meta-analysis
- **Domain:** Bioinformatics & Health
- **Sub-domain:** Meta-analysis methodologies
- **Technique:** Leave-one-out algorithm
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

The paper presents a leave-one-out algorithm for contribution analysis in component network meta-analysis (CNMA), which quantifies the impact of individual comparisons on the precision of component effect estimates. This method enhances the interpretability of CNMA results, making it crucial for engineers working with complex intervention analyses.

## Key Contribution

**A robust, variance-based framework for quantifying the contribution of constituent direct comparisons to component effect estimates in CNMA.**

## Problem

The need to disentangle individual component effects from multicomponent treatments in evidence synthesis.

## Method

**Approach:** The method iteratively excludes each constituent comparison from the network, recomputes the variances of all component effects, and quantifies the precision leverage of each comparison based on the induced variance inflation. Contributions are assigned via a normalized matrix.

**Algorithm:**

1. 1. Conduct a CNMA for the full network to estimate all component effects and their variances.
2. 2. For each direct comparison, conduct a CNMA without that comparison and recompute all component effects and their variances.
3. 3. Calculate precision leverage for each comparison based on the change in variance when excluded.
4. 4. Normalize the precision leverage values to create a contribution matrix.

**Input:** Data representing treatment comparisons and their effects, structured in a network format.

**Output:** A normalized contribution matrix indicating the percentage contribution of each comparison to the precision of component estimates.

**Key Parameters:**

- `n: number of distinct components`
- `k: number of edges (comparisons)`
- `Vfull,j: variance of component effect estimates from full network`
- `V−i,j: variance of component effect estimates after excluding comparison i`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Real-world dataset with 66 comparisons across 21 components related to exercise modalities on lean mass proportion in adults with obesity.

**Results:**

- Pearson correlation (r): 1.00
- Explained variance (R²): 0.99
- Mean absolute error (MAE): 0.084

**Compared against:** Traditional network meta-analysis methods

**Improvement:** The leave-one-out algorithm provides a more precise quantification of contributions compared to traditional methods.

## Implementation Guide

**Data Structures:** Network representation of treatments and comparisons, Matrix for storing variances and contributions

**Dependencies:** R programming language, netmeta package (version 3.2-0)

**Core Operation:**

```python
for each comparison in network: exclude comparison, recompute variances, calculate precision leverage
```

**Watch Out For:**

- Ensure that the network is sufficiently connected to avoid unidentifiability.
- Be cautious of the assumptions of linear additivity.
- Check for sufficient contrasts in the design matrix to disentangle effects.

## Use This When

- You need to analyze the contribution of individual treatment comparisons in complex interventions.
- You are working with multicomponent treatment data and need to disentangle effects.
- You require a robust method to enhance the interpretability of CNMA results.

## Don't Use When

- The treatment comparisons do not exhibit overlapping components.
- You are dealing with simple pairwise meta-analysis without complex interactions.
- The assumptions of linear additivity and identifiability are violated.

## Key Concepts

Component network meta-analysis, Precision leverage, Variance inflation, Contribution matrix

## Connects To

- Network meta-analysis
- Bayesian meta-analysis
- Hierarchical models

## Prerequisites

- Understanding of meta-analysis methodologies
- Familiarity with statistical variance concepts
- Knowledge of R programming

## Limitations

- Assumes linear additivity of treatment effects.
- Requires identifiable component effects in the full network.
- May not perform well in sparse networks.

## Open Questions

- How to extend the method for non-linear interactions between components?
- What are the implications of violating the assumptions of linear additivity?

## Abstract

Welcome to the messy world of component network meta-analysis. In traditional network meta-analysis (NMA), you're comparing complete treatments against each other. But component network meta-analysis (CNMA) is different because you’re figuring out individual contributions, and that is mathematically brutal. In regular NMA, you can trace evidence paths through a network of studies. You can say, "Study X compared Treatment 1 to Treatment 2, and Study Y compared Treatment 2 to Treatment 3, so we can make indirect comparisons between Treatment 1 and Treatment 3." It's like connecting dots on a map. But in CNMA, those clean pathways disappear. When treatments share overlapping components, it gets messier, and blurrier, because you get what the authors call "latent connections" between treatments. A comparison between "A+B" and "A+C" tells you something about the difference between components B and C, even though no study directly compared B to C. And these implicit comparisons (this extra, cloudy set of information) make it very difficult to trace where a given outcome is actually coming from.
