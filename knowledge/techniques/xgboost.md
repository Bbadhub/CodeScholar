# XGBoost

*Also known as: Extreme Gradient Boosting*

**XGBoost is an efficient and scalable implementation of gradient boosting framework designed for speed and performance.**

**Category:** optimization_algorithm  
**Maturity:** proven (widely used in production)

## How It Works

XGBoost builds an ensemble of decision trees in a sequential manner, where each new tree corrects the errors made by the previous ones. It uses a gradient descent algorithm to minimize the loss function, which allows it to optimize both the model's accuracy and computational efficiency. Additionally, it includes regularization techniques to prevent overfitting and improve generalization.

## Algorithm

**Input:** Data frame with features and target variable, typically numerical and categorical data.

**Output:** Predicted values based on the input features.

**Steps:**

1. 1. Initialize predictions with a constant value.
2. 2. For each boosting round, compute the gradient and hessian of the loss function.
3. 3. Fit a decision tree to the computed gradients.
4. 4. Update the predictions by adding the new tree's predictions scaled by a learning rate.
5. 5. Repeat steps 2-4 for a specified number of rounds or until convergence.

**Core Operation:** `output = previous_output + learning_rate * new_tree_prediction`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.1 | Lower values make the model more robust but require more trees. |
| `max_depth` | 6 | Increased depth allows the model to capture more complex patterns but risks overfitting. |
| `n_estimators` | 100 | More estimators can improve accuracy but increase computation time. |

## Complexity

- **Time:** O(n log n)
- **Space:** O(n)
- **In practice:** XGBoost is optimized for speed and can handle large datasets efficiently.

## Implementation

```python
def xgboost_model(X: pd.DataFrame, y: pd.Series) -> np.ndarray:
    model = XGBRegressor(learning_rate=0.1, max_depth=6, n_estimators=100)
    model.fit(X, y)
    predictions = model.predict(X)
    return predictions
```

## Common Mistakes

- Neglecting to tune hyperparameters, which can lead to suboptimal performance.
- Using too many trees without proper regularization, resulting in overfitting.
- Failing to preprocess data correctly, especially handling missing values.

## Use When

- You need to predict rental prices based on property features.
- You want to analyze the impact of immunological markers on health outcomes.
- You are developing a user-friendly platform for tenants and landlords.
- You need to predict cardiovascular aging in elderly patients.
- You are working in a market with limited prediction tools.

## Avoid When

- You require real-time predictions with minimal data.
- You have a small dataset with fewer than 50 samples.
- You need a model that interprets results in a straightforward manner.

## Tradeoffs

**Strengths:**

- High predictive accuracy and performance.
- Handles missing data well.
- Supports parallel processing for faster training.

**Weaknesses:**

- Can be complex to tune due to many hyperparameters.
- Less interpretable than simpler models like linear regression.
- May require more computational resources than simpler algorithms.

**Compared To:**

- **vs Random Forest:** Use XGBoost for better performance on structured data, but Random Forest is easier to interpret.
- **vs Linear Regression:** Use XGBoost for non-linear relationships, but Linear Regression is simpler and faster for linear data.

## Connects To

- Gradient Boosting
- Random Forest
- LightGBM
- CatBoost
- Support Vector Regression

## Evidence (Papers)

- **Smart Renting: Harnessing Urban Data with Statistical and Machine Learning Methods for Predicting Property Rental Prices from a Tenant’s Perspective** - [DOI](https://doi.org/10.3390/stats8010012)
- **A Predictive Model of Cardiovascular Aging by Clinical and Immunological Markers Using Machine Learning** [4 citations] - [DOI](https://doi.org/10.3390/diagnostics15070850)
