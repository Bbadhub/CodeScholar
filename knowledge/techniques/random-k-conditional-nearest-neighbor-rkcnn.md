# Random k Conditional Nearest Neighbor (RkCNN)

**RkCNN enhances classification accuracy by aggregating predictions from multiple kCNN classifiers built on random feature subsets.**

**Category:** ensemble_method  
**Maturity:** proven (widely used in production)

## How It Works

RkCNN constructs multiple kCNN classifiers using random subsets of features from the dataset. It evaluates the informativeness of each subset through a separation score. The top subsets are selected to build individual kCNN models, and their predictions are aggregated based on these scores to produce a final classification output.

## Algorithm

**Input:** Feature matrix X of size n x q, where n is the number of instances and q is the number of features.

**Output:** Predicted class probabilities for a new instance.

**Steps:**

1. 1. For each of the h random feature subsets, sample m features from the feature space.
2. 2. Calculate the separation score for each feature subset.
3. 3. Sort the separation scores in descending order.
4. 4. Select the top r feature subsets based on their separation scores.
5. 5. Construct a kCNN model for each of the top r subsets.
6. 6. Calculate the predicted probabilities for each class from each kCNN model.
7. 7. Aggregate the probabilities using weighted averaging based on the separation scores.

**Core Operation:** `output = weighted_average(predicted_probabilities from top r kCNN models)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `k` | 1 | A smaller k value increases sensitivity to local patterns. |
| `m` | 10-20 | Affects the diversity of feature subsets; too few may miss important features. |
| `r` | 200 | More subsets can improve robustness but increase computation. |
| `h` | >= r | More random subsets can enhance model performance but require more resources. |

## Complexity

- **Time:** Not explicitly stated.
- **Space:** Not explicitly stated.
- **In practice:** Performance may vary significantly based on the number of features and instances.

## Implementation

```python
def rkcnn(X: np.ndarray, k: int, m: int, r: int, h: int) -> np.ndarray:
    # Step 1: Initialize feature subsets
    subsets = sample_random_feature_subsets(X, h, m)
    # Step 2: Calculate separation scores
    scores = calculate_separation_scores(subsets)
    # Step 3: Select top r subsets
    top_subsets = select_top_subsets(subsets, scores, r)
    # Step 4: Construct kCNN models
    models = [construct_kcnn(subset, k) for subset in top_subsets]
    # Step 5: Aggregate predictions
    return aggregate_predictions(models, X)
```

## Common Mistakes

- Choosing too few features in each subset can lead to loss of important information.
- Not properly tuning the number of subsets can result in overfitting or underfitting.
- Ignoring the computational cost of building multiple models can lead to performance issues.

## Use When

- You have a high-dimensional dataset with many irrelevant features.
- You need to improve classification accuracy in noisy environments.
- You want to leverage ensemble methods for better model robustness.

## Avoid When

- The dataset has a low number of features and instances.
- Real-time classification is critical and computational resources are limited.
- You require a simple, interpretable model without ensemble complexity.

## Tradeoffs

**Strengths:**

- Improves classification accuracy in high-dimensional spaces.
- Robust to noise and irrelevant features.
- Utilizes ensemble learning principles for better generalization.

**Weaknesses:**

- Increased computational complexity due to multiple models.
- May be less interpretable than simpler models.
- Performance heavily depends on the choice of parameters.

**Compared To:**

- **vs Standard kNN:** Use RkCNN for better performance in high-dimensional datasets.
- **vs kCNN:** RkCNN provides enhanced accuracy by leveraging multiple feature subsets.

## Connects To

- k-Nearest Neighbors (kNN)
- Conditional Nearest Neighbors (kCNN)
- Ensemble Learning
- Feature Selection Techniques
- Random Forests

## Evidence (Papers)

- **Random k conditional nearest neighbor for high-dimensional data** [7 citations] - [DOI](https://doi.org/10.7717/peerj-cs.2497)
