# Domain-informed CNN architectures

**This technique enhances CNN architectures by incorporating domain knowledge to improve the accuracy of predictions in specific applications, such as weather forecasting.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

Domain-informed CNN architectures leverage both coarse forecast data and domain-specific features to train a convolutional neural network. By integrating physical principles and local atmospheric conditions, the model learns to predict finer-scale patterns. This approach is particularly useful in scenarios where traditional methods fall short, allowing for more accurate localized predictions.

## Algorithm

**Input:** Coarse wind forecast data from NWP models and domain-specific features.

**Output:** High-resolution wind forecasts tailored to specific locations.

**Steps:**

1. 1. Gather coarse wind forecast data from numerical weather prediction (NWP) models.
2. 2. Integrate domain-specific features related to local geography and atmospheric conditions.
3. 3. Design and train a CNN architecture using the integrated data.
4. 4. Validate the model against high-resolution observational data.
5. 5. Use the trained model to generate downscaled wind forecasts.

**Core Operation:** `output = CNN(integrated_coarse_data, domain_features)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.001 | A higher learning rate may speed up training but risks overshooting the optimal solution. |
| `batch_size` | 32 | Larger batch sizes can stabilize training but may require more memory. |
| `num_epochs` | 100 | More epochs can improve accuracy but may lead to overfitting. |

## Complexity

- **Time:** O(n * m * k) where n is the number of training samples, m is the number of features, and k is the number of epochs.
- **Space:** O(m * p) where m is the number of features and p is the number of parameters in the model.
- **In practice:** The actual performance may vary based on the architecture and the size of the input data.

## Implementation

```python
def domain_informed_cnn(coarse_data: np.ndarray, domain_features: np.ndarray) -> np.ndarray:
    # Step 1: Integrate data
    integrated_data = integrate(coarse_data, domain_features)
    # Step 2: Define CNN model
    model = create_cnn_model()
    # Step 3: Train model
    model.fit(integrated_data)
    # Step 4: Generate forecasts
    forecasts = model.predict(integrated_data)
    return forecasts
```

## Common Mistakes

- Neglecting to properly preprocess the domain-specific features.
- Overfitting the model by using too many epochs without validation.
- Failing to validate against high-resolution observational data.

## Use When

- You need to improve local wind forecasts for renewable energy applications.
- You have access to both coarse NWP data and high-resolution observational data.
- You want to leverage domain knowledge in weather prediction.

## Avoid When

- You require real-time predictions without prior training.
- You have limited computational resources.
- You are working with non-weather-related forecasting tasks.

## Tradeoffs

**Strengths:**

- Improves accuracy of localized predictions.
- Utilizes domain knowledge for better feature representation.
- Can outperform traditional downscaling methods.

**Weaknesses:**

- Requires substantial computational resources for training.
- Dependent on the quality of both coarse and high-resolution data.
- May not generalize well to non-weather-related tasks.

**Compared To:**

- **vs Standard downscaling methods:** Use domain-informed CNNs for better accuracy in localized forecasts.
- **vs Other CNN architectures:** Use domain-informed CNNs when domain knowledge is available to enhance predictions.

## Connects To

- Convolutional Neural Networks (CNNs)
- Numerical Weather Prediction (NWP)
- Feature Engineering
- Data Preprocessing Techniques

## Evidence (Papers)

- **Domain-informed CNN architectures for downscaling regional wind forecasts** [1 citations] - [DOI](https://doi.org/10.1016/j.egyai.2025.100485)
