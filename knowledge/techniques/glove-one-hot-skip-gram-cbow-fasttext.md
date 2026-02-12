# GloVe

*Also known as: Global Vectors for Word Representation*

**GloVe is a vector space model for word representation that captures semantic relationships between words based on their co-occurrence in a corpus.**

**Category:** neural_architecture  
**Maturity:** proven

## How It Works

GloVe constructs word embeddings by leveraging global word co-occurrence statistics from a corpus. It creates a matrix of word co-occurrences and then factorizes this matrix to produce dense vector representations for each word. The resulting vectors capture semantic meanings, allowing for effective comparisons and predictions based on the relationships between words.

## Algorithm

**Input:** Event logs containing sequences of workflow events.

**Output:** Predicted remaining time for workflow processes.

**Steps:**

1. 1. Collect event logs from workflow processes.
2. 2. Create a co-occurrence matrix from the corpus of text.
3. 3. Factorize the co-occurrence matrix to generate word vectors.
4. 4. Normalize the vectors to ensure they represent semantic similarities.
5. 5. Use the vectors in downstream tasks such as prediction or classification.

**Core Operation:** `cost = sum((X_ij - V_i^T V_j)^2)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `N (number of discrete classifications)` | 10 | Increases the granularity of classification. |
| `Context window size for CBOW` | 2 | Affects the amount of context considered for word embeddings. |

## Complexity

- **Time:** O(V^2)
- **Space:** O(V^2)
- **In practice:** Real-world performance can vary based on the size of the corpus and the number of unique words.

## Implementation

```python
def glove_embedding(event_logs: List[str]) -> Dict[str, np.ndarray]:
    co_occurrence_matrix = create_co_occurrence_matrix(event_logs)
    word_vectors = factorize_matrix(co_occurrence_matrix)
    return word_vectors
```

## Common Mistakes

- Not normalizing the vectors, leading to skewed results.
- Using too small a context window, missing important relationships.
- Overfitting the model on small datasets.

## Use When

- You need to predict the remaining time of cloud-based workflows.
- You are evaluating different encoding techniques for event data.
- You want to optimize resource allocation in cloud applications.

## Avoid When

- You have a small dataset where complex models may overfit.
- You require real-time predictions with minimal computational overhead.
- You are working with non-sequential data.

## Tradeoffs

**Strengths:**

- Captures semantic relationships effectively.
- Generates dense representations that reduce dimensionality.
- Improves prediction accuracy in various tasks.

**Weaknesses:**

- Requires a large corpus for effective training.
- Can be computationally intensive.
- Not suitable for real-time applications.

**Compared To:**

- **vs Word2Vec:** Use GloVe for global co-occurrence information; use Word2Vec for local context.

## Connects To

- Word2Vec
- FastText
- Skip-Gram
- CBOW
- One-Hot Encoding

## Evidence (Papers)

- **Comparative evaluation of encoding techniques for workflow process remaining time prediction for cloud applications** [2 citations] - [DOI](https://doi.org/10.1186/s13677-025-00763-8)
