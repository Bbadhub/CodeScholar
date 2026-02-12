# Dynamic-budget superpixel active learning

**This technique optimizes the labeling process in semantic segmentation by selectively querying high-uncertainty superpixels for manual labeling.**

**Category:** active_learning, semantic_segmentation  
**Maturity:** emerging

## How It Works

Dynamic-budget superpixel active learning employs a querying strategy that focuses on selecting superpixels with the highest uncertainty from unlabeled images. It begins with a pool of unlabeled images and iteratively trains a model on labeled data. In each iteration, it identifies superpixels, clusters them based on uncertainty, and labels only those with high uncertainty, thereby optimizing the labeling budget while improving model performance.

## Algorithm

**Input:** Unlabeled images from datasets (e.g., Nassar 2020 and Cityscapes)

**Output:** Partially labeled images with high-uncertainty superpixels labeled and low-uncertainty superpixels ignored.

**Steps:**

1. Initialize with a pool of unlabeled images and an empty active learning training set.
2. Randomly select a small batch of images for initial labeling.
3. Train the model on the labeled images until convergence.
4. In each active learning step, identify the images with the highest uncertainty.
5. For each selected image, determine the superpixels and their uncertainties.
6. Cluster superpixels into high- and low-uncertainty groups.
7. Label high-uncertainty superpixels manually and ignore low-uncertainty ones.
8. Update the training set and retrain the model.

**Core Operation:** `output = label(high_uncertainty_superpixels) + ignore(low_uncertainty_superpixels)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `initial_learning_rate` | 1e-4 | Affects the speed of convergence during training. |
| `dropout_rate` | 0.5 | Controls overfitting by randomly dropping units during training. |
| `batch_size` | 4 (Nassar), 5 (Cityscapes) | Impacts the stability of training and memory usage. |
| `number_of_epochs` | 500 | Determines how long the model is trained. |
| `step_size` | 50 images | Defines the frequency of querying in low-budget experiments. |

## Complexity

- **Time:** Not explicitly stated.
- **Space:** Not explicitly stated.
- **In practice:** Performance may vary based on dataset size and complexity.

## Implementation

```python
def dynamic_budget_active_learning(images: List[Image], budget: int) -> List[LabeledImage]:
    labeled_images = []
    initial_labels = random_initial_labels(images)
    model = train_model(initial_labels)
    while budget > 0:
        uncertainties = calculate_uncertainties(images)
        high_uncertainty_superpixels = select_high_uncertainty_superpixels(uncertainties)
        new_labels = manual_label(high_uncertainty_superpixels)
        labeled_images.extend(new_labels)
        budget -= len(new_labels)
        model = retrain_model(model, labeled_images)
    return labeled_images
```

## Common Mistakes

- Failing to properly cluster superpixels, leading to ineffective labeling.
- Overlooking the importance of uncertainty estimation in the selection process.
- Not adjusting the budget based on the dataset's characteristics.

## Use When

- You need to reduce labeling costs in semantic segmentation tasks.
- Working with imbalanced datasets where certain classes are underrepresented.
- You have a limited labeling budget but want to maximize model performance.

## Avoid When

- The dataset is small and can be fully labeled without high costs.
- The task does not involve significant class imbalance.
- Real-time labeling is required and cannot accommodate the querying process.

## Tradeoffs

**Strengths:**

- Reduces labeling costs by focusing on high-uncertainty areas.
- Improves model performance through targeted labeling.
- Adapts to varying labeling budgets dynamically.

**Weaknesses:**

- May require more computational resources for uncertainty estimation.
- Not suitable for small datasets where full labeling is feasible.
- Can be time-consuming due to the iterative querying process.

**Compared To:**

- **vs Static-budget querying:** Dynamic-budget is preferable when dealing with uncertainty and budget constraints.
- **vs Random whole-image manual labels:** Dynamic-budget is more efficient in maximizing model performance.

## Connects To

- Active Learning
- Semantic Segmentation
- Uncertainty Estimation
- Superpixel Segmentation

## Evidence (Papers)

- **Dynamic-budget superpixel active learning for semantic segmentation** [1 citations] - [DOI](https://doi.org/10.3389/frai.2024.1498956)
