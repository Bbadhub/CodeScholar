# Federated Learning

*Also known as: FL*

**Federated Learning enables collaborative model training across institutions without sharing their private data.**

**Category:** optimization_algorithm  
**Maturity:** proven (widely used in production)

## How It Works

Federated Learning allows multiple institutions to collaboratively train a machine learning model while keeping their data localized. Each institution trains the model on its own dataset and only shares the model updates with a central server. The server aggregates these updates to improve a global model, which is then redistributed for further training. This process continues iteratively until the model converges.

## Algorithm

**Input:** Local datasets from each institution.

**Output:** A global model that reflects the knowledge from all institutions without accessing their raw data.

**Steps:**

1. 1. Initialize a global model.
2. 2. Distribute the global model to all participating institutions.
3. 3. Each institution trains the model on its local dataset.
4. 4. Institutions send model updates (not raw data) back to a central server.
5. 5. The server aggregates the updates to improve the global model.
6. 6. Repeat steps 2-5 until convergence.

**Core Operation:** `global_model = aggregate(local_updates)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `number_of_rounds` | 10 | More rounds can lead to better convergence but increase computation time. |
| `local_epochs` | 5 | Increasing local epochs can improve local model accuracy but may slow down the overall process. |
| `learning_rate` | 0.01 | A higher learning rate can speed up convergence but may lead to instability. |

## Complexity

- **Time:** O(n * m * r)
- **Space:** O(m)
- **In practice:** The time complexity depends on the number of institutions (n), the size of local datasets (m), and the number of training rounds (r).

## Implementation

```python
def federated_learning(local_datasets: List[Dataset], rounds: int = 10, local_epochs: int = 5, learning_rate: float = 0.01) -> GlobalModel:
    global_model = initialize_global_model()
    for round in range(rounds):
        local_updates = []
        for dataset in local_datasets:
            local_model = train_local_model(global_model, dataset, local_epochs, learning_rate)
            local_updates.append(local_model)
        global_model = aggregate(local_updates)
    return global_model
```

## Common Mistakes

- Not properly aggregating model updates, leading to suboptimal global models.
- Ignoring data heterogeneity across institutions, which can affect model performance.
- Underestimating the communication costs between institutions and the central server.

## Use When

- You need to train models across multiple institutions without sharing data.
- Fairness in model performance across different demographic groups is a priority.
- You are dealing with sensitive data that cannot leave its original location.

## Avoid When

- Data can be centralized without privacy concerns.
- The institutions have similar data distributions.
- Real-time model updates are required.

## Tradeoffs

**Strengths:**

- Preserves data privacy by keeping data localized.
- Enables collaboration across institutions without data sharing.
- Can improve fairness in model performance across diverse datasets.

**Weaknesses:**

- Communication overhead can be significant.
- Model convergence may be slower compared to centralized training.
- Requires careful handling of data heterogeneity.

**Compared To:**

- **vs Centralized Learning:** Use Federated Learning when data privacy is a concern; otherwise, centralized learning may be more efficient.

## Connects To

- Differential Privacy
- Transfer Learning
- Multi-Task Learning
- Distributed Learning

## Evidence (Papers)

- **Fairness in Federated Learning: Trends, Challenges, and Opportunities** [3 citations] - [DOI](https://doi.org/10.1002/aisy.202400836)
