# Frequency-Informed Transformer (FiT)

**FiT is a neural network architecture that leverages frequency domain analysis for enhanced leak detection in water pipelines.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

FiT converts vibration signals from sensors into the frequency domain using Fast Fourier Transform (FFT). It then extracts amplitude features and applies a self-attention mechanism to identify critical frequency bands relevant for leak detection. Finally, these features are processed through a multi-layer perceptron (MLP) to classify the presence and type of leaks.

## Algorithm

**Input:** Vibration sensor data in time-domain format.

**Output:** Leak detection status (leak/no leak) and leak type classification.

**Steps:**

1. Collect vibration data from sensors.
2. Apply Fast Fourier Transform (FFT) to convert time-domain signals to frequency-domain.
3. Extract amplitude features from the FFT output.
4. Use self-attention to identify and prioritize critical frequency bands.
5. Feed the processed features into a multi-layer perceptron (MLP) for classification.
6. Output the prediction of leak presence and type.

**Core Operation:** `output = MLP(features)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.0005 | Affects the speed of convergence during training. |
| `batch_size` | 120 | Impacts the stability of the training process. |
| `weight_decay` | 0.0002 | Helps prevent overfitting. |
| `epochs` | 40 | Determines how many times the model will see the training data. |
| `number_of_attention_heads` | 4 | Influences the model's ability to focus on different parts of the input. |
| `MLP_projection_dimension` | 4 | Defines the output dimensionality of the MLP. |
| `number_of_attention_modules` | 8 | Affects the model's capacity to learn complex patterns. |

## Complexity

- **Time:** O(N log N)
- **Space:** Not stated for the overall model.
- **In practice:** FFT is efficient for processing large datasets, but overall model complexity may vary based on architecture.

## Implementation

```python
def fit_model(data: np.ndarray) -> Tuple[str, str]:
    fft_output = apply_fft(data)
    features = extract_amplitude_features(fft_output)
    critical_bands = self_attention(features)
    prediction = mlp_classifier(critical_bands)
    return prediction['status'], prediction['type']
```

## Common Mistakes

- Neglecting to preprocess the vibration data adequately.
- Overfitting the model by using too many epochs.
- Failing to tune the hyperparameters effectively.

## Use When

- Real-time monitoring of water pipelines is required.
- High accuracy in leak detection is critical.
- Automated feature selection is needed to reduce manual tuning.

## Avoid When

- The environment has minimal noise and stable conditions.
- Cost constraints limit the use of advanced models.
- Real-time processing is not a priority.

## Tradeoffs

**Strengths:**

- Achieves high accuracy in leak detection.
- Automates feature selection, reducing manual effort.
- Fast response time suitable for real-time applications.

**Weaknesses:**

- May require significant computational resources.
- Not ideal for environments with minimal noise.
- Complexity may lead to longer training times.

**Compared To:**

- **vs Traditional Machine Learning Models:** Use FiT for higher accuracy and automated feature selection.

## Connects To

- Fast Fourier Transform (FFT)
- Self-Attention Mechanisms
- Multi-Layer Perceptron (MLP)
- Real-Time Data Processing Techniques
- Anomaly Detection Algorithms

## Evidence (Papers)

- **Frequency-informed transformer for real-time water pipeline leak detection** - [DOI](https://doi.org/10.1007/s43684-025-00094-0)
