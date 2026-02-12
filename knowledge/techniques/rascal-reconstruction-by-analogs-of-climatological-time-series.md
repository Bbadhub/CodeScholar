# RASCAL (Reconstruction by AnalogS of ClimatologicAL time series)

**RASCAL reconstructs climatological time series by leveraging analog days with similar atmospheric conditions.**

**Category:** statistical_method  
**Maturity:** emerging

## How It Works

RASCAL identifies historical days that share similar large-scale atmospheric conditions to the target day. It preprocesses observational and reanalysis data, selects relevant predictor variables, and applies Principal Component Analysis (PCA) to reduce dimensionality. By finding and averaging the most relevant analog days, it reconstructs the target climatological time series, potentially applying bias reduction techniques for improved accuracy.

## Algorithm

**Input:** Homogeneous time series of observational data and reanalysis dataset covering the reconstruction period.

**Output:** Reconstructed climatological time series with statistical properties resembling observations.

**Steps:**

1. 1. Preprocess observational and reanalysis data.
2. 2. Select predictor variables based on atmospheric dynamics.
3. 3. Perform PCA on the predictor field to obtain principal components.
4. 4. Identify N historical days with similar predictors to the target day.
5. 5. Use weighted averaging of the analogs to reconstruct the target day.
6. 6. Apply bias reduction techniques if necessary.
7. 7. Evaluate the reconstruction performance using skill metrics.

**Core Operation:** `output = weighted_average(analog_days)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `pool_size` | 10 | Increasing this value may improve reconstruction accuracy by providing more analogs. |
| `vw_size` | 1 | Excluding more days may reduce noise but could also limit the analog pool. |
| `N` | 5 | More principal components can capture more variance but may lead to overfitting. |
| `scaling` | 0-2 | Different scaling options can affect the PCA results and subsequent analog selection. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance may vary based on the density of input data and the number of analogs considered.

## Implementation

```python
def rascal_reconstruction(observational_data: np.ndarray, reanalysis_data: np.ndarray, pool_size: int, vw_size: int, N: int, scaling: int) -> np.ndarray:
    # Step 1: Preprocess data
    # Step 2: Select predictor variables
    # Step 3: Perform PCA
    # Step 4: Identify analog days
    # Step 5: Weighted averaging
    # Step 6: Apply bias reduction
    # Step 7: Evaluate performance
    return reconstructed_series
```

## Common Mistakes

- Neglecting to preprocess data adequately, leading to poor analog selection.
- Choosing an inappropriate pool size that either overfits or underfits the data.
- Failing to evaluate the reconstruction performance, resulting in unvalidated results.

## Use When

- You need to reconstruct missing climate data in regions with limited observations.
- You are working on climate variability analyses in mountainous or urbanized areas.
- You want to extend short-term climate forecasts using historical data.

## Avoid When

- You have a dense network of reliable in situ observations.
- You require real-time weather predictions.
- You are working in regions with significant land use changes affecting data homogeneity.

## Tradeoffs

**Strengths:**

- Effectively reconstructs missing climate data in sparse regions.
- Utilizes historical data to improve short-term forecasts.
- Combines analog methods with PCA for better accuracy.

**Weaknesses:**

- Performance can degrade in areas with significant land use changes.
- Not suitable for real-time predictions.
- Requires careful selection of parameters for optimal results.

**Compared To:**

- **vs Traditional interpolation methods:** RASCAL is preferable when historical analogs provide better context for reconstruction.

## Connects To

- Principal Component Analysis (PCA)
- Time Series Analysis
- Analog Methods in Meteorology
- Statistical Downscaling Techniques

## Evidence (Papers)

- **RASCAL v1.0: an open-source tool for climatological time series reconstruction and extension** - [DOI](https://doi.org/10.5194/gmd-17-7245-2024)
