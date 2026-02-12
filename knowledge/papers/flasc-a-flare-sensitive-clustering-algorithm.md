# FLASC: a flare-sensitive clustering algorithm

## Access

| Field | Value |
|-------|-------|
| DOI | `10.7717/peerj-cs.2792` |
| Full Paper | [https://doi.org/10.7717/peerj-cs.2792](https://doi.org/10.7717/peerj-cs.2792) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/23f29ea6929b154845c638a7d3ec6f4073166f57](https://www.semanticscholar.org/paper/23f29ea6929b154845c638a7d3ec6f4073166f57) |
| Source | [https://journalclub.io/episodes/flasc-a-flare-sensitive-clustering-algorithm](https://journalclub.io/episodes/flasc-a-flare-sensitive-clustering-algorithm) |
| Source | [https://www.semanticscholar.org/paper/23f29ea6929b154845c638a7d3ec6f4073166f57](https://www.semanticscholar.org/paper/23f29ea6929b154845c638a7d3ec6f4073166f57) |
| Year | 2026 |
| Citations | 5 |
| Authors | Daniël M. Bot, Jannes Peeters, J. Liesenborgs, Jan Aerts |
| Paper ID | `c4461ee6-6134-4768-a7ca-f5831b0168a2` |

## Classification

- **Problem Type:** density-based clustering with branch detection
- **Domain:** Machine Learning & AI
- **Sub-domain:** Clustering algorithms
- **Technique:** FLASC
- **Technique Category:** clustering_algorithm
- **Type:** novel

## Summary

FLASC is a novel clustering algorithm that identifies branching structures within clusters, allowing for the detection of meaningful subpopulations in data. Engineers should care because traditional clustering methods often fail to reveal these internal branches, which can lead to missed insights in various applications such as biology and customer behavior modeling.

## Key Contribution

**FLASC introduces a flare detection post-processing step to HDBSCAN*, enabling the identification of branches within clusters.**

## Problem

The inability of traditional clustering methods to detect branching structures within clusters can lead to the loss of critical information about subpopulations.

## Method

**Approach:** FLASC builds upon HDBSCAN* to detect branches within clusters by evaluating the connectivity of points based on eccentricity. It uses a post-processing step to identify connected components that represent branches.

**Algorithm:**

1. 1. Perform HDBSCAN* clustering on the dataset.
2. 2. For each selected cluster, calculate the centroid and eccentricity of each point.
3. 3. Construct the full and core approximation graphs based on mutual reachability distance.
4. 4. Identify eccentricity contour clusters by filtering points above a certain eccentricity threshold.
5. 5. Detect connected components in the approximation graphs to identify branches.

**Input:** A dataset suitable for density-based clustering, typically in the form of feature vectors.

**Output:** Clusters with identified branches represented as connected components.

**Key Parameters:**

- `min_cluster_size: 5`
- `min_samples: 10`
- `eccentricity_threshold: 0.5`

**Complexity:** O(N) for eccentricity computation, similar computational cost to HDBSCAN*.

## Benchmarks

**Tested on:** Synthetic datasets, Real-world datasets from biological and customer behavior domains

**Results:**

- Cluster stability
- Branch detection sensitivity

**Compared against:** HDBSCAN*, DBSCAN

**Improvement:** FLASC shows similar outputs to HDBSCAN* while providing additional insights into branching structures.

## Implementation Guide

**Data Structures:** Graph data structures for approximation graphs, Cluster membership arrays

**Dependencies:** hdbscan Python package, numpy, scipy

**Core Operation:**

```python
clusters = FLASC(data, min_cluster_size=5, eccentricity_threshold=0.5)
```

**Watch Out For:**

- Ensure proper tuning of min_cluster_size to avoid overfitting.
- Watch for noise in the data that may affect branch detection.
- Understand the implications of eccentricity thresholds on results.

## Use This When

- You need to analyze data with potential branching structures.
- Traditional clustering methods fail to reveal subpopulations.
- You are working with biological data or customer behavior modeling.

## Don't Use When

- The dataset is small and can be effectively clustered using simpler methods.
- You require strict convex cluster shapes.
- The computational cost is a critical constraint.

## Key Concepts

density-based clustering, branch detection, HDBSCAN*, eccentricity, connected components

## Connects To

- HDBSCAN*
- DBSCAN
- OPTICS
- Hierarchical clustering

## Prerequisites

- Understanding of density-based clustering
- Familiarity with graph theory
- Knowledge of clustering evaluation metrics

## Limitations

- May not perform well on datasets with uniform density.
- Sensitive to the choice of eccentricity threshold.
- Computational cost can increase with very large datasets.

## Open Questions

- How can FLASC be adapted for high-dimensional data?
- What are the best practices for parameter tuning in various domains?

## Abstract

If you have a cluster that internally branches, like a Y-shape or a starburst, traditional clustering methods will treat the entire structure as a single monolithic group. They will not tell you that some data points are headed down one evolutionary path while others are diverging down another. You can’t rely on density gaps to separate these subpopulations because the branches are connected by continuous paths of relatively high density. From the point of view of the clustering algorithm, it is just one big happy family. In practice, this is a real limitation. Branching structures inside clusters show up across a wide range of domains: in biological cell development, in customer behavior modeling, in physical system transitions, and in process drift analysis. If your clustering pipeline cannot detect internal branches, you are leaving valuable information on the table. You might miss critical subgroups, misinterpret the shape of your data
