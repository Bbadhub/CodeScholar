# Ensemble Machine Learning Model (EMLM)

**EMLM combines multiple machine learning models to improve the accuracy of predictions in environmental modeling.**

**Category:** neural_architecture  
**Maturity:** proven (widely used in production)

## How It Works

EMLM leverages satellite-derived data and in situ measurements to estimate crop coefficients and daily evapotranspiration. It trains various machine learning models, such as GLM, CART, kNN, RF, and SVM, to predict crop coefficients from satellite data. The best-performing model is selected through k-fold cross-validation and used to generate estimates of evapotranspiration.

## Algorithm

**Input:** Satellite-derived LAI data and in situ measurements of ETo and ET.

**Output:** Estimated daily evapotranspiration (ETa) values.

**Steps:**

1. 1. Acquire satellite-derived LAI data from MODIS using Google Earth Engine.
2. 2. Collect in situ measurements of ET and ETo.
3. 3. Calculate Kc using the formula Kc = ETa / ETo.
4. 4. Train various machine learning models (GLM, CART, kNN, RF, SVM) to predict Kc from LAI.
5. 5. Use k-fold cross-validation to validate model performance.
6. 6. Select the best-performing model (EMLM) to generate monthly Kc estimates.
7. 7. Estimate daily ETa using the formula ETa = Kc * ETo.

**Core Operation:** `ETa = Kc * ETo`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `LAI` | derived from MODIS product (MCD15A3H V6) | Affects the accuracy of Kc estimation. |
| `ETo` | calculated using FAO56 method | Influences the final ETa estimation. |
| `Kc` | capped at 1.3 for humid environments | Limits the maximum crop coefficient value. |

## Complexity

- **Time:** O(n log n) for model training, where n is the number of data points.
- **Space:** O(m) where m is the number of models in the ensemble.
- **In practice:** Performance may vary based on the quality of input data and model selection.

## Implementation

```python
def ensemble_model(lai_data: List[float], eto_data: List[float]) -> List[float]:
    # Step 1: Train models
    models = train_models(lai_data, eto_data)
    # Step 2: Validate models
    best_model = select_best_model(models)
    # Step 3: Estimate Kc
    kc_estimates = best_model.predict(lai_data)
    # Step 4: Calculate ETa
    eta_estimates = [kc * eto for kc in kc_estimates]
    return eta_estimates
```

## Common Mistakes

- Neglecting to filter cloud-contaminated satellite data.
- Using inappropriate models for the data characteristics.
- Failing to validate model performance adequately.

## Use When

- Estimating water use in commercial forestry.
- Needing to leverage satellite data for environmental modeling.
- Working in regions with limited in situ data.

## Avoid When

- Data is heavily cloud-contaminated and not filtered.
- High spatial heterogeneity in vegetation characteristics exists.
- Water stress conditions are prevalent and not accounted for.

## Tradeoffs

**Strengths:**

- Improves prediction accuracy by combining multiple models.
- Utilizes satellite data, reducing the need for extensive in situ measurements.
- Adaptable to various environmental conditions.

**Weaknesses:**

- Complexity in model selection and validation.
- Potential overfitting if not properly validated.
- Requires high-quality input data for optimal performance.

**Compared To:**

- **vs Traditional Kc estimation methods:** EMLM generally provides more accurate estimates due to its data-driven approach.

## Connects To

- Random Forests
- Support Vector Machines
- k-Nearest Neighbors
- Generalized Linear Models
- Cross-Validation Techniques

## Evidence (Papers)

- **Leveraging Google Earth Engine and Machine Learning to Estimate Evapotranspiration in a Commercial Forest Plantation** [3 citations] - [DOI](https://doi.org/10.3390/rs16152726)
