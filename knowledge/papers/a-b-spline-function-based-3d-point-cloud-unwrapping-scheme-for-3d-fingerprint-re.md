# A B-Spline Function Based 3D Point Cloud Unwrapping Scheme for 3D Fingerprint Recognition and Identification

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1109/OJCS.2025.3559975` |
| Full Paper | [https://doi.org/10.1109/OJCS.2025.3559975](https://doi.org/10.1109/OJCS.2025.3559975) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/f0f8762d815b012e2c90abc0cf2bd69c669f0c93](https://www.semanticscholar.org/paper/f0f8762d815b012e2c90abc0cf2bd69c669f0c93) |
| Source | [https://journalclub.io/episodes/a-b-spline-function-based-3d-point-cloud-unwrapping-scheme-for-3d-fingerprint-recognition-and-identification](https://journalclub.io/episodes/a-b-spline-function-based-3d-point-cloud-unwrapping-scheme-for-3d-fingerprint-recognition-and-identification) |
| Source | [https://www.semanticscholar.org/paper/f0f8762d815b012e2c90abc0cf2bd69c669f0c93](https://www.semanticscholar.org/paper/f0f8762d815b012e2c90abc0cf2bd69c669f0c93) |
| Year | 2026 |
| Citations | 1 |
| Authors | Mohammad Mogharen Askarin, Jiankun Hu, Min Wang, Xuefei Yin, Xiuping Jia |
| Paper ID | `decf4251-59fa-4e06-9011-8dffe47e106f` |

## Classification

- **Problem Type:** 3D point cloud unwrapping for biometric recognition
- **Domain:** Computer Vision
- **Sub-domain:** 3D Shape Modeling
- **Technique:** B-spline Function Based Unwrapping
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

The paper presents a B-spline function based method for unwrapping 3D point clouds to enhance fingerprint recognition and identification. Engineers should care because this approach improves the accuracy of biometric systems by effectively modeling complex finger shapes.

## Key Contribution

**Introduction of a B-spline based unwrapping scheme for 3D fingerprint recognition.**

## Problem

The work addresses the challenge of accurately recognizing and identifying fingerprints from 3D point cloud data.

## Method

**Approach:** The method involves slicing the 3D point cloud of a fingerprint in the Y-direction and fitting a B-spline curve to the Z values of each slice. This curve serves as a local baseline to normalize the Z values of the points, effectively unwrapping the fingerprint shape.

**Algorithm:**

1. 1. Acquire 3D point cloud data of the fingerprint.
2. 2. Slice the point cloud in the Y-direction to create thin slices.
3. 3. For each slice, extract the Z values of the points.
4. 4. Fit a B-spline curve to the Z values of the slice.
5. 5. Subtract the fitted B-spline curve from the Z values of the points in the slice.
6. 6. Repeat for all slices to normalize the entire point cloud.

**Input:** 3D point cloud data of fingerprints in a structured format.

**Output:** Normalized 3D point cloud data with unwrapped fingerprint features.

**Key Parameters:**

- `spline_degree: 3`
- `number_of_knots: variable based on slice size`

**Complexity:** Not stated

## Benchmarks

**Tested on:** 3D fingerprint datasets (specific datasets not mentioned)

**Results:**

- recognition accuracy: not specified
- identification rate: not specified

**Compared against:** Traditional 3D fingerprint recognition methods

**Improvement:** Not specified

## Implementation Guide

**Data Structures:** 3D arrays for point cloud representation, Lists for storing B-spline coefficients

**Dependencies:** NumPy for numerical computations, SciPy for B-spline fitting

**Core Operation:**

```python
for each slice in point_cloud: fit_b_spline(slice.z_values); normalize(slice.z_values, b_spline)
```

**Watch Out For:**

- Ensure proper selection of knots for B-spline fitting
- Watch for overfitting with too many knots
- Consider computational efficiency for large datasets

## Use This When

- Developing a biometric system for fingerprint recognition
- Handling 3D point cloud data from fingerprint scanners
- Needing to model complex shapes accurately

## Don't Use When

- Working with 2D fingerprint data
- When real-time processing is critical
- If computational resources are severely limited

## Key Concepts

B-spline, 3D point cloud, biometric recognition, curve fitting

## Connects To

- Point cloud processing techniques
- B-spline curve fitting methods
- Biometric identification systems

## Prerequisites

- Understanding of 3D geometry
- Familiarity with B-spline concepts
- Knowledge of biometric recognition systems

## Limitations

- May not perform well with low-quality point clouds
- Dependent on the accuracy of initial point cloud acquisition
- Computationally intensive for large datasets

## Open Questions

- How to optimize the algorithm for real-time applications?
- Can this method be generalized to other biometric modalities?

## Abstract

What’s a B-spline? B-splines are piecewise polynomial functions that can flexibly approximate smooth curves by stitching together low-degree polynomials across defined intervals, controlled by a set of points called knots. Unlike simple polynomials, B-splines provide local control (adjusting one segment doesn’t distort the entire curve) which makes them ideal for modeling complex shapes like biometric surfaces. The process starts by slicing the point cloud in the Y-direction, which corresponds to the length of the finger. Each slice is one point thick. Within each slice, the Z values of the points (which represent height above the sensor plane) are fitted to a B-spline curve. Think of this like laying a flexible ruler across the surface of the slice. This curve becomes a smooth local baseline. Then, the algorithm subtracts the Z value of the curve from each point’s Z value, normalizing away the global shape of the finger while keeping the
