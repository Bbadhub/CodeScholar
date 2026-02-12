# Using similarity network analysis to improve text similarity calculations

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1007/s41109-025-00699-7` |
| Full Paper | [https://doi.org/10.1007/s41109-025-00699-7](https://doi.org/10.1007/s41109-025-00699-7) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/2de88c3439e84ed45691d28ef9081e1c93552f38](https://www.semanticscholar.org/paper/2de88c3439e84ed45691d28ef9081e1c93552f38) |
| Source | [https://journalclub.io/episodes/using-similarity-network-analysis-to-improve-text-similarity-calculations](https://journalclub.io/episodes/using-similarity-network-analysis-to-improve-text-similarity-calculations) |
| Source | [https://www.semanticscholar.org/paper/2de88c3439e84ed45691d28ef9081e1c93552f38](https://www.semanticscholar.org/paper/2de88c3439e84ed45691d28ef9081e1c93552f38) |
| Year | 2026 |
| Citations | 0 |
| Authors | D. Witschard, Kostiantyn Kucher, Ilir Jusufi, A. Kerren |
| Paper ID | `38b63553-bf08-4d45-9d3f-03823eac60e1` |

## Classification

- **Problem Type:** text similarity calculation
- **Domain:** Natural Language Processing
- **Sub-domain:** Text similarity analysis
- **Technique:** SN-Comparator
- **Technique Category:** framework
- **Type:** novel

## Summary

This paper presents a novel methodology for improving text similarity calculations through similarity network analysis, enabling better understanding of model agreement and disagreement in semantic similarity. Engineers should care because it provides a systematic approach to evaluate and compare different text embedding models, enhancing applications like recommender systems and plagiarism detection.

## Key Contribution

**A novel and generic way to compare the level of model agreement based on similarity networks.**

## Problem

The challenge of accurately comparing text documents for similarity, which is crucial for applications like recommender systems and plagiarism detection.

## Method

**Approach:** The method involves constructing similarity networks from different text embedding models and comparing them to assess model agreement. It utilizes visual analytics to help users understand the continuous similarity distribution captured by various models.

**Algorithm:**

1. 1. Select multiple text embedding models (e.g., USE, BERT, SPECTER).
2. 2. Process the text documents to generate embeddings using the selected models.
3. 3. Construct similarity networks based on the embeddings.
4. 4. Analyze the networks to assess the level of agreement/disagreement between models.
5. 5. Visualize the results using the SN-Comparator tool.

**Input:** Text documents in various formats (e.g., abstracts, news articles, question pairs).

**Output:** Visual representation of similarity networks and model agreement metrics.

**Key Parameters:**

- `embedding_model: USE, BERT, SPECTER`
- `data_set: IEEE VIS abstracts, CNN news articles, Quora question pairs`

**Complexity:** Not stated

## Benchmarks

**Tested on:** IEEE VIS conference abstracts (3,500 documents), CNN news articles (4,000 documents), Quora question pairs dataset (1,250 similar, 1,250 dissimilar)

**Results:**

- Model agreement metrics (specific values not stated)

**Compared against:** Existing methods for text similarity calculations (not explicitly named)

**Improvement:** Demonstrated low levels of model agreement, indicating the need for the proposed methodology.

## Implementation Guide

**Data Structures:** Similarity networks (graph structures), Embedding vectors (numpy arrays or similar)

**Dependencies:** TensorFlow or PyTorch (for model embeddings), NetworkX (for similarity network construction), Matplotlib or similar (for visualization)

**Core Operation:**

```python
similarity_network = construct_similarity_network(embeddings); visualize(similarity_network)
```

**Watch Out For:**

- Ensure embeddings are generated consistently across models.
- Be cautious of the subjective nature of similarity calculations.

## Use This When

- You need to compare multiple text embedding models for similarity.
- You want to visualize the agreement/disagreement of models in text similarity tasks.
- You are working on applications like recommender systems or plagiarism detection.

## Don't Use When

- You require a single definitive similarity score for text pairs.
- Your application does not involve comparing multiple models.

## Key Concepts

similarity networks, text embeddings, semantic similarity, visual analytics, model comparison

## Connects To

- BERT
- Universal Sentence Encoder
- SPECTER
- embComp
- Embedding Comparator

## Prerequisites

- Understanding of text embeddings
- Familiarity with similarity metrics
- Basic knowledge of visual analytics

## Limitations

- The methodology may not yield a definitive 'best' model.
- Subjectivity in similarity calculations can affect outcomes.
- Performance may vary based on the choice of embedding models.

## Open Questions

- How can this methodology be adapted for other types of data beyond text?
- What additional metrics can be developed to better quantify model agreement?

## Abstract

The Universal Sentence Encoder provides a strong baseline with its ability to encode sentences into fixed-length embeddings. This makes it particularly effective for capturing semantic similarity in a scalable way. USE is available in two versions: one based on a deep averaging network (DAN), and another using a Transformer architecture. They’re both designed to produce sentence embeddings that capture semantic content effectively. Regardless of the version you use, its architecture facilitates efficient processing of large volumes of text while ensuring that resultant embeddings retain contextually relevant semantic features. BERT offers heightened sensitivity to context through a bidirectional training mechanism. By pre-training transformers on a large corpus and fine-tuning them on downstream tasks, BERT generates contextual embeddings that reflect more nuanced semantic relationships. This model is particularly adept at understanding the meaning of words in context, producing embeddings that reveal intricate semantic connections between phrases and sentences.
