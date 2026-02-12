# SN-Comparator

**SN-Comparator is a tool for visualizing and comparing the agreement of multiple text embedding models in similarity calculations.**

**Category:** visualization_tool  
**Maturity:** emerging

## How It Works

SN-Comparator constructs similarity networks from various text embedding models to assess their agreement on text similarity. It processes text documents to generate embeddings, builds similarity networks based on these embeddings, and analyzes the networks for model agreement. The results are visualized to help users understand the continuous similarity distribution captured by different models.

## Algorithm

**Input:** Text documents in various formats (e.g., abstracts, news articles, question pairs).

**Output:** Visual representation of similarity networks and model agreement metrics.

**Steps:**

1. 1. Select multiple text embedding models (e.g., USE, BERT, SPECTER).
2. 2. Process the text documents to generate embeddings using the selected models.
3. 3. Construct similarity networks based on the embeddings.
4. 4. Analyze the networks to assess the level of agreement/disagreement between models.
5. 5. Visualize the results using the SN-Comparator tool.

**Core Operation:** `Not applicable (focuses on network visualization rather than a specific equation).`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `embedding_model` | USE, BERT, SPECTER | Different models may yield varying levels of agreement. |
| `data_set` | IEEE VIS abstracts, CNN news articles, Quora question pairs | The choice of dataset influences the similarity results and model performance. |

## Complexity

- **Time:** Not stated.
- **Space:** Not stated.
- **In practice:** Performance may vary based on the number of models and size of the dataset.

## Implementation

```python
def sn_comparator(models: List[str], documents: List[str]) -> Visualization:
    embeddings = [generate_embedding(model, documents) for model in models]
    similarity_networks = [construct_similarity_network(embedding) for embedding in embeddings]
    agreement_metrics = analyze_agreement(similarity_networks)
    return visualize_results(agreement_metrics)
```

## Common Mistakes

- Not selecting a diverse range of embedding models.
- Overlooking the importance of dataset choice on results.
- Failing to properly interpret the visualized agreement metrics.

## Use When

- You need to compare multiple text embedding models for similarity.
- You want to visualize the agreement/disagreement of models in text similarity tasks.
- You are working on applications like recommender systems or plagiarism detection.

## Avoid When

- You require a single definitive similarity score for text pairs.
- Your application does not involve comparing multiple models.

## Tradeoffs

**Strengths:**

- Provides a visual representation of model agreement.
- Facilitates comparison across multiple embedding models.
- Helps identify discrepancies in similarity calculations.

**Weaknesses:**

- Does not provide a single similarity score.
- May require significant computational resources for large datasets.
- Interpretation of visual results can be subjective.

**Compared To:**

- **vs Traditional similarity scoring methods:** Use SN-Comparator for model comparison; use traditional methods for definitive scores.

## Connects To

- Text embedding models (e.g., BERT, USE)
- Similarity metrics (e.g., cosine similarity)
- Visual analytics tools
- Recommender systems
- Plagiarism detection systems

## Evidence (Papers)

- **Using similarity network analysis to improve text similarity calculations** - [DOI](https://doi.org/10.1007/s41109-025-00699-7)
