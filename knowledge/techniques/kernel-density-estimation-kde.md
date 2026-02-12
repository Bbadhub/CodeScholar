# Kernel Density Estimation (KDE)

*Also known as: KDE*

**KDE is a non-parametric way to estimate the probability density function of a random variable.**

**Category:** statistical_method  
**Maturity:** proven (widely used in production)

## How It Works

KDE uses a set of data points to create a smooth estimate of the probability density function. It applies a kernel function to each data point, which contributes to the overall density estimate. The choice of kernel and the bandwidth parameter significantly influence the smoothness and accuracy of the resulting density estimate.

## Algorithm

**Input:** Atmospheric temperature and geopotential height data at multiple pressure levels.

**Output:** Estimated seasonal rain heights and contour maps showing spatial distribution.

**Steps:**

1. 1. Collect atmospheric temperature and geopotential height data.
2. 2. Compute the zero-degree isotherm height (ZDIH) from the data.
3. 3. Calculate daily rain heights using the formula hr = ho + 0.36 (km).
4. 4. Apply KDE using various kernel functions (Gaussian, Epanechnikov, Triangular, Rectangular) to estimate the probability density function of rain heights.
5. 5. Optimize the bandwidth for each kernel to minimize Integrated Squared Errors (ISE).
6. 6. Validate the estimated rain heights against measured data.
7. 7. Generate contour maps of seasonal rain heights.

**Core Operation:** `output = sum(kernel(x - xi) for all xi) / (n * bandwidth)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `bandwidth` | optimized per kernel | Affects the smoothness of the density estimate. |
| `sample_size` | m (number of observations) | More observations can lead to a more accurate estimate. |
| `standard_deviation` | σ (calculated from data) | Influences the shape of the kernel function. |

## Complexity

- **Time:** O(n^2) in naive implementations, can be improved with optimized algorithms.
- **Space:** O(n)
- **In practice:** Performance can vary based on the choice of kernel and bandwidth.

## Implementation

```python
def kernel_density_estimation(data: List[float], bandwidth: float) -> List[float]:
    # Initialize density array
    density = []
    for x in range(min(data), max(data)):
        # Calculate density for each point
        density.append(sum(kernel(x - xi) for xi in data) / (len(data) * bandwidth))
    return density
```

## Common Mistakes

- Choosing an inappropriate kernel function for the data distribution.
- Not optimizing the bandwidth, leading to over-smoothing or under-smoothing.
- Ignoring the impact of sample size on the density estimate.

## Use When

- You need to estimate rain heights for communication network planning.
- You are working in regions with high rain-induced signal attenuation.
- You require seasonal variations in rain height for meteorological studies.

## Avoid When

- You have access to localized radar data that provides accurate rain height measurements.
- You need real-time rain height data for immediate decision-making.
- The computational resources are limited for processing large datasets.

## Tradeoffs

**Strengths:**

- Provides a smooth estimate of the probability density function.
- Flexible with different kernel functions.
- Non-parametric, making it applicable to various data distributions.

**Weaknesses:**

- Computationally intensive for large datasets.
- Sensitive to the choice of bandwidth.
- Can produce misleading results if the data is sparse.

**Compared To:**

- **vs Histogram:** KDE provides a smoother estimate compared to histograms, which can be too coarse.

## Connects To

- Gaussian Mixture Models
- Support Vector Machines
- Principal Component Analysis
- Regression Analysis

## Evidence (Papers)

- **The Kernel Density Estimation Technique for Spatio-Temporal Distribution and Mapping of Rain Heights over South Africa: The Effects on Rain-Induced Attenuation** [8 citations] - [DOI](https://doi.org/10.3390/atmos15111354)
