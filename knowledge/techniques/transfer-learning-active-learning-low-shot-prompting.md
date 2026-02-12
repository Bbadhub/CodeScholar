# Transfer Learning, Active Learning, Low-shot Prompting

*Also known as: Transfer Learning, Active Learning, Low-shot Learning*

**This technique automates the detection of data leakage in machine learning code using limited annotated datasets.**

**Category:** machine_learning_technique  
**Maturity:** proven (widely used in production)

## How It Works

The technique leverages transfer learning to adapt pre-trained models to new tasks, active learning to iteratively select the most informative samples for labeling, and low-shot prompting to effectively utilize few examples. By training on a dataset of labeled Python code snippets, the models learn to identify various types of data leakage. The approach is particularly useful when annotated data is scarce, allowing for efficient model training and improved detection capabilities.

## Algorithm

**Input:** Python code snippets labeled as having data leakage or not.

**Output:** Predictions indicating whether a code snippet contains data leakage.

**Steps:**

1. 1. Collect and annotate a dataset of Python ML code snippets.
2. 2. Identify types of data leakage (overlap, multi-test, preprocessing).
3. 3. Map leakage types to ML pipeline phases.
4. 4. Filter code snippets to include only those associated with potential leakage.
5. 5. Train models using transfer learning, active learning, or low-shot prompting.
6. 6. Evaluate model performance using metrics like F2-score.

**Core Operation:** `output = model.predict(code_snippet)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.001 | A lower learning rate may lead to more stable training but slower convergence. |
| `number_of_samples` | 698 (after active learning) | Reducing the number of samples can speed up training but may affect model accuracy. |
| `dataset_size` | 1,904 samples | Larger datasets generally improve model performance but require more resources. |

## Complexity

- **Time:** O(n log n) for active learning selection
- **Space:** O(n) for storing the dataset
- **In practice:** The complexity may vary based on the model architecture and the specific implementation.

## Implementation

```python
def detect_data_leakage(code_snippets: List[str]) -> List[bool]:
    model = load_pretrained_model()
    predictions = []
    for snippet in code_snippets:
        prediction = model.predict(snippet)
        predictions.append(prediction)
    return predictions
```

## Common Mistakes

- Neglecting to properly annotate the dataset, leading to poor model performance.
- Overfitting the model to a small number of examples.
- Failing to evaluate the model on a separate validation set.

## Use When

- You need to automate the detection of data leakage in ML code.
- You have limited annotated datasets for training models.
- You want to improve the quality of ML code in production.

## Avoid When

- You have a large annotated dataset available for training.
- You require real-time detection with minimal latency.
- You are working in a domain where data leakage is not a concern.

## Tradeoffs

**Strengths:**

- Reduces the need for large annotated datasets.
- Improves detection capabilities in scenarios with limited data.
- Can adapt to new types of data leakage with minimal retraining.

**Weaknesses:**

- May not perform well if the initial model is poorly chosen.
- Active learning can be resource-intensive.
- Low-shot prompting may lead to overfitting if not managed carefully.

**Compared To:**

- **vs Traditional Supervised Learning:** Use transfer learning when labeled data is scarce; traditional methods require more data.

## Connects To

- Supervised Learning
- Semi-supervised Learning
- Data Augmentation
- Model Fine-tuning

## Evidence (Papers)

- **Data leakage detection in machine learning code: transfer learning, active learning, or low-shot prompting?** [3 citations] - [DOI](https://doi.org/10.7717/peerj-cs.2730)
