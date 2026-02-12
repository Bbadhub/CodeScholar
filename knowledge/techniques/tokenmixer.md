# TokenMixer

**TokenMixer is a hybrid architecture that combines CNNs and Vision Transformers for efficient classification of histopathology images.**

**Category:** neural_architecture  
**Maturity:** proven (widely used in production)

## How It Works

TokenMixer processes histopathology images by first extracting features using convolutional layers. It then tokenizes these features and passes them through a Vision Transformer (ViT) for enhanced classification accuracy. This method is particularly effective for tasks like breast cancer diagnosis, where both feature extraction and classification are critical.

## Algorithm

**Input:** Histopathology images resized to 224x224 pixels.

**Output:** Predictions for binary (Benign/Malignant) and multi-class (eight tumor subtypes) classification.

**Steps:**

1. 1. Preprocess histopathology images by resizing to 224x224 pixels.
2. 2. Split data into training, validation, and test sets.
3. 3. Use data augmentation techniques such as rotation and zoom.
4. 4. Extract features using TokenLearner and ConvMixer.
5. 5. Combine features in TokenMixer and pass through ViT for classification.
6. 6. Output predictions for binary and multi-class classification.

**Core Operation:** `output = ViT(TokenMixer(features))`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `patch_size` | 14x14 | Changing this affects the granularity of feature extraction. |
| `number_of_layers` | 8 | Increasing layers can improve accuracy but may increase computation. |
| `learning_rate` | not stated | Affects convergence speed and model performance. |
| `batch_size` | not stated | Impacts training stability and resource usage. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance may vary based on dataset size and model configuration.

## Implementation

```python
def token_mixer_model(input_image: np.ndarray) -> np.ndarray:
    resized_image = preprocess(input_image)
    features = extract_features(resized_image)
    combined_features = combine_features(features)
    predictions = classify_with_vit(combined_features)
    return predictions
```

## Common Mistakes

- Neglecting proper data augmentation, which can lead to overfitting.
- Using inappropriate patch sizes that do not suit the image characteristics.
- Failing to split data correctly into training, validation, and test sets.

## Use When

- You need to classify histopathology images for breast cancer diagnosis.
- You want to reduce computational resources while maintaining high accuracy.
- You are working with limited training data and need an efficient model.

## Avoid When

- You require real-time processing with extremely low latency.
- You have access to abundant computational resources and prefer using pure ViTs or CNNs.
- You are dealing with non-image data.

## Tradeoffs

**Strengths:**

- High accuracy in classifying histopathology images.
- Efficient use of computational resources compared to pure ViTs.
- Effective for limited training data scenarios.

**Weaknesses:**

- Not suitable for real-time applications due to decision time.
- May require tuning of multiple hyperparameters.
- Performance can degrade with non-image data.

**Compared To:**

- **vs ViT:** Use TokenMixer when computational resources are limited; use ViT for maximum accuracy with ample resources.

## Connects To

- Convolutional Neural Networks (CNNs)
- Vision Transformers (ViTs)
- Data Augmentation Techniques
- Feature Extraction Methods

## Evidence (Papers)

- **Advancing breast cancer diagnosis: token vision transformers for faster and accurate classification of histopathology images** [11 citations] - [DOI](https://doi.org/10.1186/s42492-024-00181-8)
