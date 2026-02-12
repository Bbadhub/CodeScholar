# Text Mining for Crime Classification

*Also known as: Crime Text Classification, Narrative Crime Analysis*

**This technique classifies types of crime using narrative text extracted from court documents.**

**Category:** machine_learning  
**Maturity:** proven (widely used in production)

## How It Works

The technique involves extracting narrative sections from public court documents, particularly those containing police report excerpts. After preprocessing the text data, it is labeled according to crime types. A machine learning model is then trained on this labeled dataset to classify new documents based on their narratives.

## Algorithm

**Input:** Public court documents containing narrative text.

**Output:** Classified crime types for each document.

**Steps:**

1. 1. Collect public court documents.
2. 2. Extract narrative sections that likely contain police report excerpts.
3. 3. Preprocess the text data (cleaning, tokenization, etc.).
4. 4. Label the data based on crime types.
5. 5. Train a machine learning model on the labeled dataset.
6. 6. Evaluate the model's performance on a test set.
7. 7. Use the model for classifying new court documents.

**Core Operation:** `output = classify(narrative_text)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `n_estimators` | 100 | Increasing this value can improve model performance but may increase training time. |
| `max_depth` | 10 | Higher values can lead to overfitting, while lower values may underfit the data. |
| `learning_rate` | 0.01 | A lower learning rate may improve convergence but requires more training iterations. |

## Complexity

- **Time:** Not explicitly stated
- **Space:** Not explicitly stated
- **In practice:** Performance may vary based on the size and quality of the dataset.

## Implementation

```python
def classify_crime(narrative: str) -> str:
    # Step 1: Preprocess the narrative
    cleaned_text = preprocess(narrative)
    # Step 2: Use the trained model to predict crime type
    crime_type = model.predict(cleaned_text)
    return crime_type
```

## Common Mistakes

- Neglecting to preprocess the text data adequately.
- Using a small or biased dataset for training.
- Failing to evaluate the model's performance properly.

## Use When

- You need to classify crime types from narrative text.
- Access to police reports is restricted.
- Working with unstructured text data from legal documents.

## Avoid When

- The dataset lacks relevant narrative text.
- Real-time classification is required.
- High accuracy is critical and cannot be compromised.

## Tradeoffs

**Strengths:**

- Can handle unstructured text data effectively.
- Improves classification accuracy over traditional methods.
- Utilizes existing public documents for training.

**Weaknesses:**

- Dependent on the quality of the narrative text.
- May not perform well with limited or irrelevant data.
- Not suitable for real-time applications.

**Compared To:**

- **vs Traditional keyword-based classification methods:** Use text mining for better accuracy and handling of complex narratives.

## Connects To

- Natural Language Processing (NLP)
- Machine Learning for Text Classification
- Information Retrieval
- Sentiment Analysis

## Evidence (Papers)

- **Text mining and machine learning for crime classification: using unstructured narrative court documents in police academic** [1 citations] - [DOI](https://doi.org/10.1080/23311916.2024.2359850)
