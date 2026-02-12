# SpeckleNN

**SpeckleNN is a neural network optimized for real-time classification of X-ray single-particle imaging data.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

SpeckleNN is designed to classify speckle patterns from X-ray detectors efficiently. The model is optimized to reduce its parameters significantly while maintaining high accuracy. It leverages FPGA hardware for deployment, allowing for low latency and reduced power consumption during inference.

## Algorithm

**Input:** Speckle patterns from X-ray detectors (data type: images, shape: variable)

**Output:** Real-time classification results indicating the presence of single-particle hits (data type: labels, shape: variable)

**Steps:**

1. Define the original SpeckleNN architecture with approximately 5.6 million parameters.
2. Optimize the model to reduce parameters to 64.6K while maintaining at least 90% accuracy.
3. Implement the optimized model on the KCU1500 FPGA board using the SLAC Neural Network Library (SNL).
4. Evaluate performance based on resource utilization, power consumption, and inference latency.
5. Compare FPGA performance against a GPU implementation.

**Core Operation:** `output = classification(SpeckleNN(input))`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | not stated | affects convergence speed and model performance |
| `parameter_count` | 64.6K | reducing parameters may impact accuracy |
| `latency` | 45.015 microseconds | lower latency improves real-time performance |
| `power_consumption` | 9.4W | lower power consumption is critical for embedded systems |

## Complexity

- **Time:** not stated
- **Space:** not stated
- **In practice:** The model is optimized for FPGA deployment, which may not translate directly to other hardware.

## Implementation

```python
def speckle_nn(input: np.ndarray) -> np.ndarray:
    # Load optimized model parameters
    model = load_model('optimized_speckle_nn')
    # Perform classification
    output = model.predict(input)
    return output
```

## Common Mistakes

- Neglecting to optimize the model for the specific FPGA architecture.
- Overlooking the trade-off between model size and accuracy.
- Failing to evaluate power consumption during deployment.

## Use When

- You need to perform real-time classification of high-throughput data from X-ray detectors.
- You are working in environments where power consumption is critical.
- You require rapid deployment of machine learning models that may need frequent updates.

## Avoid When

- You have access to abundant computational resources and can afford higher latency.
- You require extremely high accuracy beyond 90% and cannot compromise on model size.
- You are working with datasets that do not fit the few-shot learning paradigm.

## Tradeoffs

**Strengths:**

- High efficiency in real-time classification tasks.
- Significant reduction in power consumption compared to GPU implementations.
- Fast inference times suitable for high-throughput environments.

**Weaknesses:**

- Limited to approximately 90% accuracy, which may not be sufficient for all applications.
- Requires careful optimization for FPGA deployment.
- Not suitable for datasets outside the few-shot learning paradigm.

**Compared To:**

- **vs GPU-based neural networks:** Use SpeckleNN for lower power and latency; use GPU for higher accuracy and flexibility.

## Connects To

- FPGA optimization techniques
- Real-time machine learning
- X-ray imaging analysis
- Low-power neural networks

## Evidence (Papers)

- **FPGA-accelerated SpeckleNN with SNL for real-time X-ray single-particle imaging** - [DOI](https://doi.org/10.3389/fhpcp.2025.1520151)
