# One-class classifiers

**One-class classifiers are used to identify anomalies by learning from normal operational data.**

**Category:** statistical_method  
**Maturity:** emerging

## How It Works

One-class classifiers are trained exclusively on normal data to model the expected behavior of a system. Once trained, they can evaluate new data points to determine if they deviate from this learned behavior, indicating potential anomalies. This approach is particularly useful in scenarios where labeled anomalous data is scarce or unavailable.

## Algorithm

**Input:** Normal operational data from robotic systems in a structured format.

**Output:** Anomaly detection results indicating whether the current operation is normal or anomalous.

**Steps:**

1. Collect normal operational data from the robotic system.
2. Preprocess the data to extract relevant features.
3. Train the one-class classifier using the preprocessed data.
4. Deploy the classifier to monitor real-time operations.
5. Detect anomalies by evaluating new data against the trained model.

**Core Operation:** `output = evaluate(new_data) against trained_model`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `feature_set` | [list of features] | Changing the feature set can improve or degrade the model's ability to detect anomalies. |
| `threshold` | 0.5 | Adjusting the threshold affects the sensitivity of anomaly detection. |

## Complexity

- **Time:** O(n)
- **Space:** O(m)
- **In practice:** Performance may vary based on the complexity of the feature set and the size of the training data.

## Implementation

```python
def train_one_class_classifier(data: List[float]) -> Model:
    # Preprocess data
    features = extract_features(data)
    model = OneClassClassifier()
    model.fit(features)
    return model

def detect_anomalies(model: Model, new_data: List[float]) -> List[bool]:
    features = extract_features(new_data)
    return model.predict(features)
```

## Common Mistakes

- Using a feature set that does not capture the essence of normal behavior.
- Failing to preprocess data adequately before training.
- Setting the threshold too low or too high, leading to false positives or negatives.

## Use When

- You need to monitor robotic systems for software anomalies.
- You have access to normal operational data for training.
- You require a method that does not rely on labeled anomalous data.

## Avoid When

- You have a highly dynamic environment with rapidly changing operational patterns.
- You need to detect known types of anomalies with labeled data.
- You require real-time processing with extremely low latency.

## Tradeoffs

**Strengths:**

- Effective in scenarios with limited labeled data.
- Can adapt to various types of normal behavior.
- Useful for continuous monitoring of systems.

**Weaknesses:**

- May struggle in highly dynamic environments.
- Performance heavily depends on the quality of normal data.
- Not suitable for detecting known anomalies with labeled data.

**Compared To:**

- **vs Supervised classification models:** Use one-class classifiers when labeled anomalous data is unavailable.

## Connects To

- Anomaly detection techniques
- Supervised learning methods
- Feature extraction methods
- Robotic system monitoring

## Evidence (Papers)

- **Detecting Software Anomalies in Robots by Means of One-class Classifiers** - [DOI](https://doi.org/10.1080/08839514.2025.2538459)
