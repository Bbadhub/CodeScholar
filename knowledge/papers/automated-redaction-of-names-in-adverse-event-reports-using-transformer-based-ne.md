# Automated redaction of names in adverse event reports using transformer-based neural networks

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s12911-024-02785-9` |
| Full Paper | [https://doi.org/10.1186/s12911-024-02785-9](https://doi.org/10.1186/s12911-024-02785-9) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/a0a0b8fe023a352208e63aec946a1ea9e9b3bcf4](https://www.semanticscholar.org/paper/a0a0b8fe023a352208e63aec946a1ea9e9b3bcf4) |
| Source | [https://journalclub.io/episodes/automated-redaction-of-names-in-adverse-event-reports-using-transformer-based-neural-networks](https://journalclub.io/episodes/automated-redaction-of-names-in-adverse-event-reports-using-transformer-based-neural-networks) |
| Source | [https://www.semanticscholar.org/paper/a0a0b8fe023a352208e63aec946a1ea9e9b3bcf4](https://www.semanticscholar.org/paper/a0a0b8fe023a352208e63aec946a1ea9e9b3bcf4) |
| Year | 2026 |
| Citations | 2 |
| Authors | Eva-Lisa Meldau, Shachi Bista, Carlos Melgarejo-González, G. N. Norén |
| Paper ID | `cde8b5ea-7d27-474d-bb67-44d803939844` |

## Classification

- **Problem Type:** Named Entity Recognition (NER) for de-identification
- **Domain:** Natural Language Processing
- **Sub-domain:** Transformer architectures
- **Technique:** BERT (Bidirectional Encoder Representations from Transformers)
- **Technique Category:** neural_architecture
- **Type:** adaptation

## Summary

The paper presents a method for automated redaction of personal names in adverse event reports using a fine-tuned BERT model. This is crucial for maintaining patient privacy while allowing organizations to share sensitive data, particularly in pharmacovigilance contexts.

## Key Contribution

**Development of a fine-tuned BERT model for effective name redaction in clinical narratives.**

## Problem

The need to protect patient privacy in narrative reports while sharing data for pharmacovigilance.

## Method

**Approach:** The method fine-tunes a BERT model to classify tokens in narratives as either NAME or NON-NAME. It combines this with a rule-based classifier to improve performance on specific patterns.

**Algorithm:**

1. 1. Collect and preprocess training data from Yellow Card and i2b2 datasets.
2. 2. Fine-tune the BERT model on the combined training set.
3. 3. Implement a binary classification for each token in the narratives.
4. 4. Use a rule-based classifier to identify common patterns.
5. 5. Evaluate the model on a separate test set.
6. 6. Analyze performance metrics including precision, recall, and false positive rates.

**Input:** Narrative text from adverse event reports.

**Output:** Redacted text with names replaced by asterisks.

**Key Parameters:**

- `learning_rate: 1e-5`
- `epochs: 5`
- `classification_threshold: 0.9`

**Complexity:** Not stated

## Benchmarks

**Tested on:** UK Yellow Card scheme narratives, i2b2 2014 de-identification challenge dataset

**Results:**

- Recall: 87% (overall), 94% (long tokens >3 characters)
- Precision: 55% (overall), 58% (long tokens >3 characters)
- False positive rate: 0.05%

**Compared against:** Rule-based classifier, BERT model without fine-tuning on Yellow Card data

**Improvement:** Recall improved from 66% to 87% when fine-tuning on Yellow Card data.

## Implementation Guide

**Data Structures:** Text corpus for training, Tokenized input sequences

**Dependencies:** TensorFlow (version 2.7.0), Hugging Face Transformers (version 4.12.3)

**Core Operation:**

```python
model.predict(tokenized_input) to classify tokens as NAME or NON-NAME.
```

**Watch Out For:**

- Ensure the training data is representative of the target domain.
- Monitor for overfitting during fine-tuning.
- Adjust classification threshold based on validation performance.

## Use This When

- You need to redact names in clinical narratives.
- You are working with sensitive patient data that requires de-identification.
- You want to maintain clinical context while anonymizing reports.

## Don't Use When

- The dataset has a high prevalence of names that are not well-represented in training data.
- Real-time processing is required with very low latency.
- You need 100% precision in name redaction.

## Key Concepts

de-identification, NLP, transformer models, BERT, token classification, medical eponyms, active learning

## Connects To

- Conditional Random Fields for NER
- Active learning techniques
- Rule-based de-identification methods

## Prerequisites

- Understanding of transformer models
- Familiarity with NLP tasks
- Knowledge of medical terminology and eponyms

## Limitations

- Performance may vary with the complexity of names.
- May not generalize well to other domains without retraining.
- False positives can mask clinically relevant information.

## Open Questions

- How can the model be adapted for other languages?
- What are the impacts of redaction on downstream NLP tasks?

## Abstract

Imagine you’re writing a function called “redact_names”. It takes one parameter, a string. Your function needs to accept the string, replace any names with a series of asterisks, and return the string. It needs to handle all the corner-cases I mentioned above (full names, partials names, and initials). But remember, people’s names may have any kind of capitalization or no capitalization at all. They may be one word, or one letter, or a series of words and letters. A name could be two words, or three, or four or more. There may even be standalone sentences that contain nothing but a name. And in other cases there may not be any names in the passage at all. Think that’s not complicated enough? It gets worse. Medical writing is often chock-full of what are called “medical eponyms”
