# Resampling Point Clouds Using Series of Local Triangulations

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/jimaging11020049` |
| Full Paper | [https://doi.org/10.3390/jimaging11020049](https://doi.org/10.3390/jimaging11020049) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/839b4a4a5862308f38b07eebadabae6f63ca869c](https://www.semanticscholar.org/paper/839b4a4a5862308f38b07eebadabae6f63ca869c) |
| Source | [https://journalclub.io/episodes/resampling-point-clouds-using-series-of-local-triangulations](https://journalclub.io/episodes/resampling-point-clouds-using-series-of-local-triangulations) |
| Source | [https://www.semanticscholar.org/paper/839b4a4a5862308f38b07eebadabae6f63ca869c](https://www.semanticscholar.org/paper/839b4a4a5862308f38b07eebadabae6f63ca869c) |
| Year | 2026 |
| Citations | 0 |
| Authors | Vijai Kumar Suriyababu, Cornelis Vuik, M. Möller |
| Paper ID | `d277676f-4b03-4456-a56e-359f1d445d37` |

## Classification

- **Problem Type:** point cloud resampling
- **Domain:** Computer Vision
- **Sub-domain:** Point Cloud Processing
- **Technique:** Series of Local Triangulations (SOLT)
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a novel algorithm called Series of Local Triangulations (SOLT) for resampling point clouds, which efficiently performs upsampling and downsampling while preserving geometry and topology. Engineers should care because this method integrates seamlessly into existing workflows and avoids the artifacts associated with traditional voxelization methods.

## Key Contribution

**A novel algorithm, SOLT, enabling efficient point-cloud upsampling and downsampling without artifacts or topology loss.**

## Problem

The need for algorithms optimized for point-cloud geometry representations in computer-aided engineering (CAE) simulations, particularly to avoid artifacts from voxel-based methods.

## Method

**Approach:** The SOLT algorithm constructs localized triangulations around individual points in a point cloud, using distance and geometric parameters to identify nearby points and compute a characteristic length scale. It merges local triangulations into a global mesh while ensuring topology preservation and avoiding artifacts.

**Algorithm:**

1. Initialize the point cloud.
2. For each point p in the point cloud, identify a local neighborhood S(p) using a distance threshold or tangent space coordinates.
3. Determine the characteristic length scale of S(p) as the distance to its farthest neighbor.
4. Adjust positions of excessively close points to prevent degeneracies.
5. Compute the local Delaunay triangulation of S(p).
6. Refine the triangulation to ensure it adheres to the Delaunay criterion.
7. Merge the local triangulations into a global mesh by eliminating duplicate vertices.

**Input:** Unoriented point cloud.

**Output:** Series of Local Triangulations (SOLT) representation.

**Key Parameters:**

- `search_radius (r): average point-to-point distance`
- `threshold (ϵ): tangent coordinate similarity threshold`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Waterloo Point Cloud Database, Thingi10k, SimJEB

**Results:**

- Chamfer Distance Loss: 0.1–0.3%
- Hausdorff Distance Loss: 0.22–1.25%
- Uniformity Index: 96–99%
- Volume Preservation Error: 1.5%
- Computational Time: 5.0–30.0 s
- Compression Ratio: 2:1–3.33:1

**Compared against:** Ball-Pivoting Algorithm (BPA), Poisson reconstruction

**Improvement:** SOLT is 62 times faster than BPA and 2.46 times faster than Poisson reconstruction while maintaining similar quality.

## Implementation Guide

**Data Structures:** Point cloud data structure, Triangle data structure for local triangulations

**Dependencies:** C++ standard libraries for data structures and algorithms

**Core Operation:**

```python
SOLT(point_cloud): for each point p in point_cloud: compute_local_triangulation(p); merge_triangulations();
```

**Watch Out For:**

- Ensure proper handling of degenerate cases in local neighborhoods.
- Adjust parameters based on point cloud density to avoid artifacts.

## Use This When

- You need to resample point clouds for CAE applications.
- You want to preserve geometry and topology in point cloud processing.
- You require a lightweight solution without reliance on pre-trained models.

## Don't Use When

- You need a method that requires surface normals.
- You are working with extremely noisy data where artifacts are tolerable.

## Key Concepts

Delaunay triangulation, point cloud, resampling, topology preservation, blue noise sampling, feature distance field

## Connects To

- Delaunay triangulation algorithms
- Voxelization techniques
- Machine learning methods for point cloud processing

## Prerequisites

- Understanding of triangulation methods
- Familiarity with point cloud data structures
- Basic knowledge of computational geometry

## Limitations

- Not optimized for extremely noisy point clouds.
- May require additional processing for feature preservation in complex geometries.

## Open Questions

- How can SOLT be adapted for real-time applications?
- What are the effects of varying point cloud densities on the performance of SOLT?

## Abstract

Delaunay triangulation constructs a set of triangles connecting the points in such a way that no point is unnecessarily enclosed within any triangle. This can be difficult to picture, so let’s take a moment to visualize it. You’ve got a 3D space, and a bunch of points floating in it. A Delaunay triangulation would try to connect these points with triangles in a way that avoids skinny or highly stretched triangles, instead favoring triangles that are as close to equilateral as possible. It doesn't add points that aren't there, and it doesn't move any of your existing points, it just figures out the way to connect the existing points such that it maximizes the minimum interior angle across all triangles. Remember that an equilateral triangle has the largest possible minimum-angle (in other words, its smallest angle is the largest it could be). As you would expect Delaunay triangulation is well-suited for
