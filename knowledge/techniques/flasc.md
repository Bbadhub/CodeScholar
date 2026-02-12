# FLASC

**FLASC is a flare-sensitive clustering algorithm that detects branching structures within clusters.**

**Category:** clustering_algorithm  
**Maturity:** emerging

## How It Works

FLASC enhances the HDBSCAN* clustering algorithm by focusing on the eccentricity of points to identify branches within clusters. It first performs clustering and then calculates the eccentricity of each point. Using this information, it constructs graphs to filter and detect connected components that represent branches, providing deeper insights into the data structure.

## Algorithm

**Input:** A dataset suitable for density-based clustering, typically in the form of feature vectors.

**Output:** Clusters with identified branches represented as connected components.

**Steps:**

1. 1. Perform HDBSCAN* clustering on the dataset.
2. 2. For each selected cluster, calculate the centroid and eccentricity of each point.
3. 3. Construct the full and core approximation graphs based on mutual reachability distance.
4. 4. Identify eccentricity contour clusters by filtering points above a certain eccentricity threshold.
5. 5. Detect connected components in the approximation graphs to identify branches.

**Core Operation:** `output = connected_components(graph) based on eccentricity filtering`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `min_cluster_size` | 5 | Increases the minimum size of clusters to be considered. |
| `min_samples` | 10 | Sets the minimum number of samples in a neighborhood for a point to be considered a core point. |
| `eccentricity_threshold` | 0.5 | Filters points based on their eccentricity to identify significant branches. |

## Complexity

- **Time:** O(N) for eccentricity computation, similar computational cost to HDBSCAN*.
- **Space:** O(N) for storing the graph structures.
- **In practice:** FLASC is efficient for large datasets but may be computationally intensive for very high-dimensional data.

## Implementation

```python
def flasc_clustering(data: List[float], min_cluster_size: int = 5, min_samples: int = 10, eccentricity_threshold: float = 0.5) -> List[Cluster]:
    clusters = hdbscan_clustering(data, min_cluster_size, min_samples)
    for cluster in clusters:
        eccentricities = calculate_eccentricity(cluster)
        graph = construct_graph(cluster, eccentricities)
        branches = detect_connected_components(graph, eccentricity_threshold)
    return branches
```

## Common Mistakes

- Neglecting to properly set the eccentricity threshold, leading to missed branches.
- Using FLASC on datasets that are too small for its complexity.
- Failing to preprocess data adequately before clustering.

## Use When

- You need to analyze data with potential branching structures.
- Traditional clustering methods fail to reveal subpopulations.
- You are working with biological data or customer behavior modeling.

## Avoid When

- The dataset is small and can be effectively clustered using simpler methods.
- You require strict convex cluster shapes.
- The computational cost is a critical constraint.

## Tradeoffs

**Strengths:**

- Effectively identifies branching structures in complex datasets.
- Provides more insights compared to traditional clustering methods.
- Robust to noise and outliers due to its density-based nature.

**Weaknesses:**

- Higher computational cost compared to simpler clustering algorithms.
- May require careful tuning of parameters for optimal performance.
- Not suitable for datasets with strict convex cluster shapes.

**Compared To:**

- **vs HDBSCAN*:** Use FLASC when branching structures are expected; otherwise, HDBSCAN* may suffice.
- **vs DBSCAN:** FLASC is preferred for complex datasets with potential branches, while DBSCAN is simpler and faster for well-defined clusters.

## Connects To

- HDBSCAN*
- DBSCAN
- Density-Based Clustering
- Graph-Based Clustering
- Eccentricity Analysis

## Evidence (Papers)

- **FLASC: a flare-sensitive clustering algorithm** [5 citations] - [DOI](https://doi.org/10.7717/peerj-cs.2792)
