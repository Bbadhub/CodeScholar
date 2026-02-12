# Series of Local Triangulations (SOLT)

**SOLT is a method for resampling point clouds by constructing localized triangulations around individual points.**

**Category:** mesh_generation  
**Maturity:** emerging

## How It Works

The SOLT algorithm identifies local neighborhoods around points in a point cloud and computes a characteristic length scale for triangulation. It constructs local Delaunay triangulations, refines them to meet the Delaunay criterion, and merges these local triangulations into a global mesh. This process preserves the topology of the original point cloud while avoiding artifacts.

## Algorithm

**Input:** Unoriented point cloud (N x 3 array of points)

**Output:** Series of Local Triangulations (mesh representation)

**Steps:**

1. Initialize the point cloud.
2. For each point p in the point cloud, identify a local neighborhood S(p) using a distance threshold or tangent space coordinates.
3. Determine the characteristic length scale of S(p) as the distance to its farthest neighbor.
4. Adjust positions of excessively close points to prevent degeneracies.
5. Compute the local Delaunay triangulation of S(p).
6. Refine the triangulation to ensure it adheres to the Delaunay criterion.
7. Merge the local triangulations into a global mesh by eliminating duplicate vertices.

**Core Operation:** `output = merge(local triangulations)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `search_radius (r)` | average point-to-point distance | Affects the size of the local neighborhood. |
| `threshold (ε)` | tangent coordinate similarity threshold | Controls the similarity required for points to be considered in the same local triangulation. |

## Complexity

- **Time:** Not explicitly stated.
- **Space:** Not explicitly stated.
- **In practice:** Performance may vary based on point cloud density and distribution.

## Implementation

```python
def SOLT(point_cloud: np.ndarray) -> Mesh:
    # Initialize the point cloud
    for p in point_cloud:
        S_p = find_local_neighborhood(p)
        characteristic_length = compute_length_scale(S_p)
        adjust_close_points(S_p)
        local_triangulation = compute_delaunay(S_p)
        refine_triangulation(local_triangulation)
        merge_into_global_mesh(local_triangulation)
    return global_mesh
```

## Common Mistakes

- Neglecting to adjust positions of excessively close points, leading to degeneracies.
- Using an inappropriate search radius that either includes too many or too few points.
- Failing to refine the triangulation, resulting in non-Delaunay artifacts.

## Use When

- You need to resample point clouds for CAE applications.
- You want to preserve geometry and topology in point cloud processing.
- You require a lightweight solution without reliance on pre-trained models.

## Avoid When

- You need a method that requires surface normals.
- You are working with extremely noisy data where artifacts are tolerable.

## Tradeoffs

**Strengths:**

- Preserves geometry and topology effectively.
- Fast performance compared to traditional methods like BPA and Poisson reconstruction.
- Lightweight and does not require pre-trained models.

**Weaknesses:**

- May struggle with extremely noisy data.
- Not suitable for applications requiring surface normals.
- Performance can vary with point cloud density.

**Compared To:**

- **vs Ball-Pivoting Algorithm (BPA):** Use SOLT for faster performance and topology preservation.
- **vs Poisson reconstruction:** SOLT is preferable for speed while maintaining quality.

## Connects To

- Delaunay triangulation
- Point cloud processing
- Mesh generation
- Surface reconstruction

## Evidence (Papers)

- **Resampling Point Clouds Using Series of Local Triangulations** - [DOI](https://doi.org/10.3390/jimaging11020049)
