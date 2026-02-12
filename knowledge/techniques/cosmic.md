# COSMIC

**COSMIC is a machine learning algorithm designed for identifying and estimating the richness of galaxy clusters from astronomical data.**

**Category:** machine_learning_algorithm  
**Maturity:** emerging

## How It Works

COSMIC operates in two main steps. First, it uses an XGBoost classifier to identify Brightest Cluster Galaxies (BCGs) based on photometric and spectroscopic features. Second, it generates a smoothed optical map around each identified BCG and employs a deep neural network to estimate the richness of the galaxy cluster.

## Algorithm

**Input:** Photometric and spectroscopic data of galaxies, including r-band magnitude, colors, and photometric redshifts.

**Output:** Identified BCGs and estimated richness of galaxy clusters.

**Steps:**

1. Step 1: Use XGBoost to classify galaxies as BCG-like based on features such as r-band magnitude and colors.
2. Step 2: Generate a smoothed optical map (SOM) around each BCG.
3. Step 3: Use a pretrained ResNet-34 model to estimate cluster richness from the smoothed optical map.

**Core Operation:** `output = XGBoost(photometric_features) → BCGs; richness = ResNet-34(smoothed_optical_map)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.1 | A lower learning rate may improve accuracy but increase training time. |
| `max_depth` | 6 | Increasing max depth can lead to overfitting. |
| `n_estimators` | 100 | More estimators can improve performance but increase computation. |
| `sigma` | 0.05 | Adjusting sigma affects the degree of Gaussian smoothing applied. |

## Complexity

- **Time:** Not explicitly stated.
- **Space:** Not explicitly stated.
- **In practice:** Performance may vary based on dataset size and feature complexity.

## Implementation

```python
def cosmic_algorithm(data: pd.DataFrame) -> Tuple[List[BCG], List[float]]:
    bcs = xgboost_classifier(data)
    smoothed_maps = generate_smoothed_maps(bcs)
    richness = estimate_richness(smoothed_maps)
    return bcs, richness
```

## Common Mistakes

- Neglecting to preprocess input data properly before feeding it to the model.
- Overfitting the XGBoost model by using too many estimators or too high max depth.
- Failing to validate the model on a separate test set to ensure generalization.

## Use When

- You need to catalog galaxy clusters from large astronomical datasets.
- You want to improve the accuracy of galaxy cluster detection in optical surveys.
- You are working with data from upcoming large-scale astronomical surveys.

## Avoid When

- You have a small dataset that does not require machine learning.
- You need real-time processing with minimal computational resources.
- You are focused on non-optical methods of galaxy cluster detection.

## Tradeoffs

**Strengths:**

- High accuracy in identifying BCGs and estimating cluster richness.
- Utilizes advanced machine learning techniques for improved performance.
- Can handle large datasets effectively.

**Weaknesses:**

- Requires significant computational resources for training.
- Not suitable for small datasets or real-time applications.
- Performance may degrade if the input data is not representative.

**Compared To:**

- **vs Traditional cluster detection algorithms:** COSMIC generally provides better completeness and purity.

## Connects To

- XGBoost
- Deep Learning (ResNet)
- Photometric Redshift Estimation
- Galaxy Cluster Analysis

## Evidence (Papers)

- **COSMIC: A Galaxy Cluster-Finding Algorithm Using Machine Learning** - [DOI](https://doi.org/10.3847/1538-4365/ad8bbd)
