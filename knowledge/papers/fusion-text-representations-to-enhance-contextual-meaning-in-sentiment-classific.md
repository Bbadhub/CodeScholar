# Fusion Text Representations to Enhance Contextual Meaning in Sentiment Classification

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/app142210420` |
| Full Paper | [https://doi.org/10.3390/app142210420](https://doi.org/10.3390/app142210420) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/6cde2f782c513f4b405d58d4061961d3b32b0610](https://www.semanticscholar.org/paper/6cde2f782c513f4b405d58d4061961d3b32b0610) |
| Source | [https://journalclub.io/episodes/fusion-text-representations-to-enhance-contextual-meaning-in-sentiment-classification](https://journalclub.io/episodes/fusion-text-representations-to-enhance-contextual-meaning-in-sentiment-classification) |
| Source | [https://www.semanticscholar.org/paper/6cde2f782c513f4b405d58d4061961d3b32b0610](https://www.semanticscholar.org/paper/6cde2f782c513f4b405d58d4061961d3b32b0610) |
| Year | 2026 |
| Citations | 1 |
| Authors | K. Trisna, Jinjie Huang, Hengyu Liang, Eddy Muntina Dharma |
| Paper ID | `c6de7e34-98b3-4d84-bfcc-cb6b24f05a02` |

## Classification

- **Problem Type:** sentiment classification
- **Domain:** Natural Language Processing
- **Sub-domain:** Sentiment Analysis
- **Technique:** GloWord_biGRU
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents GloWord_biGRU, a novel sentiment classification model that enhances contextual understanding by fusing GloVe and Word2Vec embeddings. Engineers should care because it automates sentiment analysis for large datasets, improving efficiency and accuracy in processing user-generated content.

## Key Contribution

**Introduction of GloWord_biGRU, a fusion text representation model that combines GloVe and Word2Vec embeddings for improved sentiment classification.**

## Problem

The need to classify large volumes of user comments and reviews as positive or negative in online platforms like YouTube.

## Method

**Approach:** GloWord_biGRU combines GloVe and Word2Vec embeddings to create richer word representations, which are then processed by a biGRU for sentiment classification. This approach leverages both local and global context to improve classification accuracy.

**Algorithm:**

1. 1. Pre-process the text data to remove noise and irrelevant characters.
2. 2. Generate word embeddings using GloVe and Word2Vec.
3. 3. Concatenate the embeddings from GloVe and Word2Vec.
4. 4. Feed the concatenated embeddings into a biGRU layer.
5. 5. Apply Global Max Pooling to the output of the biGRU.
6. 6. Use dropout layers for regularization.
7. 7. Pass the result through dense layers to produce the final output.

**Input:** Text data consisting of user comments or reviews.

**Output:** A boolean indicating sentiment: True for positive comments, False for negative comments.

**Key Parameters:**

- `embedding_dimension: d (not specified)`
- `dropout_rate: 0.5 (common practice)`
- `number_of_units_in_biGRU: not specified`

**Complexity:** not stated

## Benchmarks

**Tested on:** IMDB dataset

**Results:**

- F1 score: 90.21%

**Compared against:** Traditional machine learning models like Naïve Bayes, SVM, and Decision Trees.

**Improvement:** Achieved superior performance compared to traditional models.

## Implementation Guide

**Data Structures:** Embedding matrix for GloVe, Embedding matrix for Word2Vec, Concatenated embedding matrix

**Dependencies:** GloVe library, Word2Vec library, Deep learning framework (e.g., TensorFlow, PyTorch)

**Core Operation:**

```python
embeddings = concatenate(GloVe(w), Word2Vec(w)); output = biGRU(embeddings)
```

**Watch Out For:**

- Ensure proper pre-processing of text to avoid noise affecting results.
- Monitor for overfitting, especially with smaller datasets.
- Adjust the embedding dimension based on the vocabulary size.

## Use This When

- You need to classify large volumes of text data quickly and accurately.
- You want to leverage both local and global context in text analysis.
- You are working on sentiment analysis for user-generated content.

## Don't Use When

- The dataset is too small to benefit from deep learning models.
- You require real-time processing with minimal computational resources.
- You are dealing with highly specialized vocabulary that may not be captured by general embeddings.

## Key Concepts

word embedding, deep learning, biGRU, sentiment classification

## Connects To

- Word2Vec
- GloVe
- biGRU
- LSTM
- CNN

## Prerequisites

- Understanding of word embeddings
- Familiarity with RNN architectures
- Knowledge of sentiment analysis techniques

## Limitations

- Performance may degrade with highly specialized or domain-specific language.
- Requires significant computational resources for training on large datasets.
- May struggle with sarcasm or nuanced sentiments.

## Open Questions

- How can the model be adapted for languages other than English?
- What improvements can be made to handle sarcasm and irony in sentiment classification?

## Abstract

This paper is about a great piece of software with a terrible name. It’s called GloWord_biGRU. At a high-level this research is all about sentiment classification. It’s about building a tool that can classify user-comments, posts, and other freeform text as either positive or negative. Imagine that you work at a place like Youtube. You have lots of videos, people can thumb-up or thumb-down them to indicate if they like it, but they can also leave a comment. One popular video could have hundreds of thousands of comments, far too many for a team-member to review. But you do want to review those comments somehow. You want to feed the overall sentiment of each comment back into the system as if it was a thumbs-up or thumbs-down. So, you have a bunch of text, and you need to convert each blob into a boolean. True if it’s a positive comment, false if it’s negative. And of course you need to do this at scale, as quickly and cost-efficiently as possible. What do you do?
