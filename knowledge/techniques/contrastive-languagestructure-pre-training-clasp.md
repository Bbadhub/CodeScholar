# Contrastive Language–Structure Pre-training (CLaSP)

**CLaSP learns embeddings that align crystal structures with their textual descriptions for material retrieval.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

CLaSP utilizes a dataset of crystal structures paired with publication titles and abstracts to create embeddings that capture the relationships between materials and their properties. It employs a contrastive learning framework to align these crystal and text embeddings, allowing for intuitive retrieval of materials based on textual queries. The model is pre-trained on crystal structures and fine-tuned with keywords from literature to enhance its performance in material discovery.

## Algorithm

**Input:** Crystal structures and their associated publication titles and abstracts.

**Output:** Embeddings of crystal structures and the ability to retrieve structures based on textual queries.

**Steps:**

1. 1. Pre-train a crystal encoder using pairs of crystal structures and publication titles.
2. 2. Fine-tune the model using pairs of crystal structures and keywords generated from titles and abstracts.
3. 3. Transform crystal structures into embeddings using the crystal encoder.
4. 4. Transform paired caption texts into embeddings using the text encoder.
5. 5. Minimize the large margin cosine loss function to align embeddings.
6. 6. Retrieve candidate structures based on user-provided text queries.

**Core Operation:** `loss = max(0, margin - cosine_similarity(embedding_crystal, embedding_text))`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `embedding_dimensionality` | 768 | Higher dimensions may capture more complex relationships but increase computational cost. |
| `margin (m)` | [0, 0.3, 0.5] | Adjusting the margin affects the separation of positive and negative pairs in the embedding space. |
| `scaling hyperparameter (s)` | [1.0, 1.5, 2.0, 2.5, 3.0, 3.5] | Scaling can influence the sensitivity of the cosine similarity loss. |

## Complexity

- **Time:** O(n log n) for retrieval tasks
- **Space:** O(n) for storing embeddings
- **In practice:** Performance may vary based on dataset size and embedding dimensionality.

## Implementation

```python
def clasp_model(crystal_data: List[Crystal], text_data: List[str]) -> Embeddings:
    # Step 1: Pre-train crystal encoder
    crystal_embeddings = pretrain_crystal_encoder(crystal_data)
    # Step 2: Fine-tune with text
    text_embeddings = fine_tune_with_text(crystal_embeddings, text_data)
    # Step 3: Minimize loss
    loss = compute_loss(crystal_embeddings, text_embeddings)
    return crystal_embeddings, text_embeddings
```

## Common Mistakes

- Neglecting to properly preprocess text data before embedding.
- Using inappropriate margin values that do not reflect the dataset's distribution.
- Failing to validate the model on a separate test set after fine-tuning.

## Use When

- You need to retrieve materials based on high-level properties from unannotated datasets.
- You want to leverage existing literature to enhance materials discovery.
- You require a method to visualize and explore relationships between materials and their properties.

## Avoid When

- You have a well-annotated dataset with specific property labels.
- You need real-time predictions for specific material properties.
- You are working in a domain where textual descriptions are not available.

## Tradeoffs

**Strengths:**

- Effectively captures relationships between materials and their textual descriptions.
- Enhances material retrieval from unannotated datasets.
- Utilizes existing literature to improve model performance.

**Weaknesses:**

- Requires a substantial amount of paired data for effective training.
- Performance may degrade in domains without rich textual descriptions.
- Not suitable for real-time predictions.

**Compared To:**

- **vs CMML:** CLaSP outperforms CMML in retrieval tasks by leveraging textual information.

## Connects To

- Contrastive Learning
- Natural Language Processing
- Graph Neural Networks
- Material Property Prediction

## Evidence (Papers)

- **Bridging text and crystal structures: literature driven contrastive learning for materials science** [1 citations] - [DOI](https://doi.org/10.1088/2632-2153/ade58c)
