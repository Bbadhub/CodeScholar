# Hybrid Euclidean Distance with Large Language Models (HED-LM)

**HED-LM optimizes example selection for few-shot learning by combining Euclidean distance filtering with contextual evaluation from large language models.**

**Category:** optimization_algorithm  
**Maturity:** emerging

## How It Works

HED-LM begins by preprocessing sensor data to extract relevant features. It then filters examples based on numerical similarity using Euclidean distance. Afterward, large language models assess the contextual relevance of the selected examples. Finally, the technique constructs prompts for classification based on the re-ranked examples, enhancing the model's performance in few-shot scenarios.

## Algorithm

**Input:** Accelerometer data represented as 1D vectors of 180 values per instance.

**Output:** Predicted labels for fatigue or non-fatigue based on selected examples.

**Steps:**

1. 1. Acquire accelerometer data and assign labels (fatigue/non-fatigue).
2. 2. Preprocess data: segment signals, apply low-pass filtering, and normalize.
3. 3. Extract features from preprocessed signals to form structured representations.
4. 4. Filter examples using Euclidean distance to find numerically similar instances.
5. 5. Score selected examples using LLMs for contextual relevance.
6. 6. Re-rank examples based on scores and construct prompts.
7. 7. Use the constructed prompts for classification of new inputs.

**Core Operation:** `output = classify(prompts)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `fcutoff` | 30 Hz | Affects the filtering of high-frequency noise in the sensor data. |
| `sampling_frequency` | 256 Hz | Determines the resolution of the accelerometer data. |
| `window_size` | 60 samples | Defines the segment length for feature extraction. |
| `feature_vector_dimension` | 30 | Controls the number of features extracted per segment. |

## Complexity

- **Time:** Not explicitly stated
- **Space:** Not explicitly stated
- **In practice:** Performance may vary based on the size of the dataset and the complexity of the LLM used.

## Implementation

```python
def hed_lm_classification(data: List[float]) -> str:
    # Step 1: Preprocess data
    preprocessed_data = preprocess(data)
    # Step 2: Extract features
    features = extract_features(preprocessed_data)
    # Step 3: Filter examples
    similar_examples = filter_by_distance(features)
    # Step 4: Score examples with LLM
    scores = score_with_llm(similar_examples)
    # Step 5: Construct prompts
    prompts = construct_prompts(scores)
    # Step 6: Classify
    return classify(prompts)
```

## Common Mistakes

- Neglecting to properly preprocess the sensor data, leading to poor feature extraction.
- Using inappropriate parameters for filtering, which can reduce the quality of selected examples.
- Over-relying on LLM scores without considering the numerical similarity aspect.

## Use When

- You have limited labeled data for sensor-based classification tasks.
- You need to improve model performance in high-variability environments.
- You require a robust example selection strategy for nuanced classification problems.

## Avoid When

- You have a large labeled dataset available for training.
- The task does not involve sensor data or few-shot learning.
- Real-time processing is critical and computational resources are limited.

## Tradeoffs

**Strengths:**

- Improves classification performance in few-shot scenarios.
- Combines numerical and contextual evaluation for better example selection.
- Effective in high-variability environments.

**Weaknesses:**

- May not perform well with large labeled datasets.
- Computationally intensive due to LLM usage.
- Requires careful tuning of parameters for optimal performance.

**Compared To:**

- **vs Distance-only filtering:** Use HED-LM when contextual relevance is crucial for classification.

## Connects To

- Few-shot learning
- Sensor data classification
- Feature extraction techniques
- Large language models

## Evidence (Papers)

- **Few-Shot Optimization for Sensor Data Using Large Language Models: A Case Study on Fatigue Detection** - [DOI](https://doi.org/10.3390/s25113324)
