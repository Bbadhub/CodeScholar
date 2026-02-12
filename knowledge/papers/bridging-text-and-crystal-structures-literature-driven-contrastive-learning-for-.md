# Bridging text and crystal structures: literature driven contrastive learning for materials science

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1088/2632-2153/ade58c` |
| Full Paper | [https://doi.org/10.1088/2632-2153/ade58c](https://doi.org/10.1088/2632-2153/ade58c) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/e4bf557652145eff46eec6f4ad52170b829a56e0](https://www.semanticscholar.org/paper/e4bf557652145eff46eec6f4ad52170b829a56e0) |
| Source | [https://journalclub.io/episodes/bridging-text-and-crystal-structures-literature-driven-contrastive-learning-for-materials-science](https://journalclub.io/episodes/bridging-text-and-crystal-structures-literature-driven-contrastive-learning-for-materials-science) |
| Source | [https://www.semanticscholar.org/paper/e4bf557652145eff46eec6f4ad52170b829a56e0](https://www.semanticscholar.org/paper/e4bf557652145eff46eec6f4ad52170b829a56e0) |
| Year | 2026 |
| Citations | 1 |
| Authors | Yuta Suzuki, Tatsunori Taniai, Ryo Igarashi, Kotaro Saito, Naoya Chiba, Yoshitaka Ushiku |
| Paper ID | `51d391f8-96f2-4a7d-95a9-8263b42f80b7` |

## Classification

- **Problem Type:** crossmodal retrieval and embedding learning
- **Domain:** Machine Learning & AI
- **Sub-domain:** Materials Informatics
- **Technique:** Contrastive Language–Structure Pre-training (CLaSP)
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents Contrastive Language–Structure Pre-training (CLaSP), a novel approach for linking crystal structures with textual descriptions to enhance materials discovery. Engineers should care because this method enables intuitive retrieval of materials based on user-provided text queries, significantly speeding up the search for new superconductors and other materials.

## Key Contribution

**Introduction of CLaSP, a learning paradigm that constructs crossmodal embedding spaces between crystal structures and texts for enhanced materials retrieval.**

## Problem

The challenge of efficiently identifying and retrieving crystal structures associated with desired material properties from vast literature.

## Method

**Approach:** CLaSP uses a dataset of crystal structures paired with publication titles and abstracts to learn embeddings that capture similarities between structures and their properties. It employs a contrastive learning framework to align crystal and text embeddings, allowing for intuitive material retrieval based on textual queries.

**Algorithm:**

1. 1. Pre-train a crystal encoder using pairs of crystal structures and publication titles.
2. 2. Fine-tune the model using pairs of crystal structures and keywords generated from titles and abstracts.
3. 3. Transform crystal structures into embeddings using the crystal encoder.
4. 4. Transform paired caption texts into embeddings using the text encoder.
5. 5. Minimize the large margin cosine loss function to align embeddings.
6. 6. Retrieve candidate structures based on user-provided text queries.

**Input:** Crystal structures and their associated publication titles and abstracts.

**Output:** Embeddings of crystal structures and the ability to retrieve structures based on textual queries.

**Key Parameters:**

- `embedding_dimensionality: 768`
- `margin (m): [0, 0.3, 0.5]`
- `scaling hyperparameter (s): [1.0, 1.5, 2.0, 2.5, 3.0, 3.5]`

**Complexity:** not stated

## Benchmarks

**Tested on:** 406,048 crystal structures from the Crystallography Open Database (COD)

**Results:**

- ROC-AUC: average 0.7804 after fine-tuning
- Average Precision (AP): average 0.7743 after fine-tuning

**Compared against:** CMML (trained solely on crystal structure information)

**Improvement:** CLaSP outperformed the baseline CMML method in retrieval tasks.

## Implementation Guide

**Data Structures:** Embedding vectors for crystal structures and text descriptions.

**Dependencies:** SciBERT for text encoding, Llama 3 for keyword generation

**Core Operation:**

```python
crystal_embeddings = crystal_encoder(crystal_structures); text_embeddings = text_encoder(text_descriptions); loss = contrastive_loss(crystal_embeddings, text_embeddings)
```

**Watch Out For:**

- Ensure the dataset is large enough to capture diverse material properties.
- Carefully tune the margin and scaling hyperparameters for optimal performance.
- Monitor for overfitting during fine-tuning with limited positive samples.

## Use This When

- You need to retrieve materials based on high-level properties from unannotated datasets.
- You want to leverage existing literature to enhance materials discovery.
- You require a method to visualize and explore relationships between materials and their properties.

## Don't Use When

- You have a well-annotated dataset with specific property labels.
- You need real-time predictions for specific material properties.
- You are working in a domain where textual descriptions are not available.

## Key Concepts

contrastive learning, crossmodal embedding, materials informatics, semantic retrieval

## Connects To

- CLIP (Contrastive Language–Image Pre-Training)
- Graph Neural Networks (GNNs) for crystal structure modeling
- Self-supervised learning techniques

## Prerequisites

- Understanding of contrastive learning principles
- Familiarity with neural network architectures
- Knowledge of materials science and properties

## Limitations

- Dependent on the quality and relevance of the textual data used for training.
- May not generalize well to materials with no associated literature.
- Performance may vary with the complexity of the material properties.

## Open Questions

- How can the model be adapted for real-time property predictions?
- What additional features can enhance the interpretability of the embeddings?

## Abstract

You're part of a team that is hunting for a new superconductor. A material that is easy to synthesize, easy to stabilize, and can be used to carry current without resistance or enable next-generation electronics. Easier said than done. The hunt for such a structure (or in this case, crystal) can take weeks or months: not just in the lab, but in the literature. Every lead begins with a paper, and every paper references another. You find yourself combing through thousands of entries across databases and journals, trying to piece together which compounds have been tried, which ones worked, and which ones didn’t. It’s slow, repetitive detective work: scanning titles, abstracts, and datasets for clues about superconductivity.
