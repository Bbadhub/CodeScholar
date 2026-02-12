# PM2.5-GNN

**PM2.5-GNN predicts PM2.5 concentrations using a graph neural network approach, integrating meteorological and fire-related data.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

The PM2.5-GNN model operates in two main steps. First, it forecasts total PM2.5 concentrations by training on historical data, incorporating meteorological and fire data. Second, it estimates the contributions of ambient sources to isolate the impact of prescribed fires on air quality.

## Algorithm

**Input:** PM2.5 concentrations, meteorological data (wind speed, temperature, precipitation), fire data (fire radiative power, number of fires)

**Output:** Predicted PM2.5 concentrations at specified sensor locations

**Steps:**

1. 1. Collect PM2.5, meteorological, and fire data.
2. 2. Train the PM2.5-GNN model using historical PM2.5 observations.
3. 3. Predict total PM2.5 concentrations using the trained model.
4. 4. Train a second PM2.5-GNN model to predict ambient PM2.5 concentrations.
5. 5. Subtract ambient PM2.5 predictions from total PM2.5 predictions to estimate fire-specific PM2.5 contributions.
6. 6. Simulate prescribed fires and input data into the PM2.5-GNN model to forecast air quality impact.

**Core Operation:** `output = total_PM2.5 - ambient_PM2.5`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.001 | Affects the speed of convergence during training. |
| `number_of_epochs` | 100 | Determines how many times the model will see the training data. |
| `batch_size` | 32 | Influences the stability of the training process. |
| `window_size` | 240 hours | Defines the historical data range used for predictions. |
| `prediction_window` | 48 hours | Specifies how far into the future predictions are made. |

## Complexity

- **Time:** Not explicitly stated
- **Space:** Not explicitly stated
- **In practice:** Performance may vary based on the size of the input data and model architecture.

## Implementation

```python
def pm25_gnn_predict(data: Dict[str, Any]) -> np.ndarray:
    # Step 1: Collect data
    pm25_data = data['pm25']
    met_data = data['meteorological']
    fire_data = data['fire']
    
    # Step 2: Train the model (pseudo)
    model = train_pm25_gnn(pm25_data, met_data, fire_data)
    
    # Step 3: Predict total PM2.5
    total_pm25 = model.predict(pm25_data)
    
    # Step 4: Train ambient model
    ambient_model = train_pm25_gnn_ambient(pm25_data, met_data)
    
    # Step 5: Predict ambient PM2.5
    ambient_pm25 = ambient_model.predict(pm25_data)
    
    # Step 6: Calculate fire-specific PM2.5
    fire_pm25 = total_pm25 - ambient_pm25
    return fire_pm25
```

## Common Mistakes

- Neglecting to preprocess the input data properly.
- Overfitting the model by using too many epochs.
- Failing to validate the model on unseen data.

## Use When

- You need to forecast air quality impacts from prescribed fires.
- You require real-time PM2.5 predictions for emergency management.
- You want to analyze the trade-offs of prescribed fire implementation.

## Avoid When

- You have access to high-resolution PM2.5 data without the need for modeling.
- You require predictions in a different geographical region not covered by the model.
- You need a simpler model without the complexity of GNNs.

## Tradeoffs

**Strengths:**

- Integrates multiple data sources for improved accuracy.
- Outperforms traditional models like Random Forest and LSTM.
- Provides insights into the impact of prescribed fires on air quality.

**Weaknesses:**

- Requires significant computational resources for training.
- Complexity may deter users needing simpler solutions.
- Performance heavily depends on the quality of input data.

**Compared To:**

- **vs Random Forest:** Use PM2.5-GNN for better accuracy with complex data relationships.
- **vs LSTM:** Choose PM2.5-GNN for spatial data integration.

## Connects To

- Graph Neural Networks (GNN)
- Air Quality Modeling
- Time Series Forecasting
- Environmental Data Analysis

## Evidence (Papers)

- **Simulating the air quality impact of prescribed fires using graph neural network-based PM2.5 forecasts** [1 citations] - [DOI](https://doi.org/10.1017/eds.2025.4)
