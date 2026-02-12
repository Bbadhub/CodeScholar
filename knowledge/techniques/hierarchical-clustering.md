# Hierarchical Clustering

*Also known as: Agglomerative Clustering*

**Hierarchical clustering groups data points into a tree of clusters based on their similarities.**

**Category:** clustering_algorithm  
**Maturity:** proven

## How It Works

Hierarchical clustering starts with each data point as its own cluster and iteratively merges the closest clusters based on a similarity measure. This process continues until all data points are combined into a single cluster or until a specified number of clusters is reached. The result is a dendrogram that illustrates the arrangement of clusters and their relationships.

## Algorithm

**Input:** A dataset containing individual health literacy responses from the HLQ.

**Output:** A hierarchical structure of clusters representing different health literacy profiles.

**Steps:**

1. Start with each observation as a separate cluster.
2. Calculate the similarity between all clusters.
3. Identify the two most similar clusters.
4. Merge these clusters into a new cluster.
5. Repeat the process until all observations are in one cluster.

**Core Operation:** `similarity = distance(clusterA, clusterB)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `similarity_threshold` | 0.5 | Adjusting this value changes the sensitivity of cluster merging. |
| `max_clusters` | 10 | Limits the number of clusters formed, affecting granularity. |

## Complexity

- **Time:** O(n²)
- **Space:** O(n)
- **In practice:** While computationally intensive for large datasets, it provides a comprehensive view of data relationships.

## Implementation

```python
def hierarchical_clustering(data: List[List[float]], similarity_threshold: float, max_clusters: int) -> List[List[int]]:
    clusters = [[i] for i in range(len(data))]
    while len(clusters) > 1:
        # Calculate similarities
        # Find two closest clusters
        # Merge clusters
        pass
    return clusters
```

## Common Mistakes

- Not normalizing data before clustering.
- Choosing an inappropriate similarity measure.
- Failing to visualize the dendrogram for interpretation.

## Use When

- You need to group individuals based on similar characteristics.
- You want to analyze survey data for patterns.
- You are working on public health interventions.

## Avoid When

- The dataset is too small for meaningful clustering.
- You require real-time clustering updates.
- Data is highly dimensional without proper preprocessing.

## Tradeoffs

**Strengths:**

- Produces a comprehensive hierarchical structure.
- No need to specify the number of clusters in advance.
- Can reveal nested clusters.

**Weaknesses:**

- Computationally expensive for large datasets.
- Sensitive to noise and outliers.
- Difficult to interpret results without visualization.

**Compared To:**

- **vs K-means clustering:** Use K-means for larger datasets with a known number of clusters; use hierarchical clustering for detailed relationships.

## Connects To

- K-means Clustering
- DBSCAN
- Principal Component Analysis
- Agglomerative Clustering

## Evidence (Papers)

- **Health literacy profiling: a snapshot of Tasmania’s challenges and strengths using five domains of the health literacy questionnaire (HLQ)** [4 citations] - [DOI](https://doi.org/10.1080/28355245.2024.2410201)
