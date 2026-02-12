# Multinomial Logistic Regression (MLR)

**MLR is used to classify outcomes into multiple categories based on independent variables.**

**Category:** statistical_method  
**Maturity:** proven

## How It Works

Multinomial Logistic Regression extends binary logistic regression to handle multiple classes. It estimates the probabilities of different outcomes based on a set of independent variables. The model uses a softmax function to convert the linear combinations of the inputs into probabilities for each class, allowing for classification into more than two categories.

## Algorithm

**Input:** Data from IPO prospectuses including financial ratios and prospectus characteristics.

**Output:** Predicted class of IPO performance: BELOW AVERAGE (0), AVERAGE (1), ABOVE AVERAGE (2).

**Steps:**

1. 1. Collect and preprocess data from prospectuses.
2. 2. Split data into training (90%) and testing (10%) sets.
3. 3. Normalize the training data.
4. 4. Train the MLR model using the training data.
5. 5. Calculate class probabilities using the trained model.
6. 6. Assign labels based on a predetermined threshold.
7. 7. Evaluate model performance using metrics like accuracy, recall, precision, and F1 score.

**Core Operation:** `P(Y = k | X) = exp(β_k · X) / Σ(exp(β_j · X)) for all classes j`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.01 | Affects the speed of convergence during training. |
| `threshold` | 0.5 | Determines the cutoff for classifying probabilities into categories. |

## Complexity

- **Time:** O(n * k * m) where n is the number of samples, k is the number of classes, and m is the number of features.
- **Space:** O(k * m) for storing the model parameters.
- **In practice:** Real-world performance may vary based on the quality of input data and preprocessing steps.

## Implementation

```python
def train_mlr_model(data: np.ndarray, labels: np.ndarray) -> MLRModel:
    # Preprocess data
    normalized_data = normalize(data)
    # Split data
    train_data, test_data = split_data(normalized_data)
    # Train model
    model = MLRModel()
    model.fit(train_data, labels)
    return model
```

## Common Mistakes

- Not normalizing the input data before training.
- Using a threshold that does not reflect the distribution of classes.
- Overfitting the model by using too many features without regularization.

## Use When

- You need to predict the performance of IPOs based on financial data.
- You have access to detailed prospectus information for companies going public.
- You want to classify outcomes into multiple categories rather than binary.

## Avoid When

- The dataset is too small to train a reliable model.
- You require real-time predictions and cannot afford preprocessing time.
- The IPOs have unique characteristics that cannot be generalized.

## Tradeoffs

**Strengths:**

- Can handle multiple classes effectively.
- Provides probabilities for class membership.
- Relatively easy to interpret and implement.

**Weaknesses:**

- Assumes independence of features, which may not hold in practice.
- Can struggle with imbalanced datasets.
- Sensitive to outliers in the data.

**Compared To:**

- **vs Binary Logistic Regression:** Use MLR when dealing with more than two classes.
- **vs Random Forest:** Use Random Forest for better handling of non-linear relationships.

## Connects To

- Logistic Regression
- Softmax Regression
- Support Vector Machines
- Decision Trees

## Evidence (Papers)

- **Prediction of IPO performance from prospectus using multinomial logistic regression, a machine learning model** [1 citations] - [DOI](https://doi.org/10.3934/dsfe.2025006)
