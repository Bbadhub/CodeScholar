# Comparative evaluation of encoding techniques for workflow process remaining time prediction for cloud applications

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s13677-025-00763-8` |
| Full Paper | [https://doi.org/10.1186/s13677-025-00763-8](https://doi.org/10.1186/s13677-025-00763-8) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/4d493205a1d9b056fbfc182b4467afa2ddc68148](https://www.semanticscholar.org/paper/4d493205a1d9b056fbfc182b4467afa2ddc68148) |
| Source | [https://journalclub.io/episodes/comparative-evaluation-of-encoding-techniques-for-workflow-process-remaining-time-prediction-for-cloud-applications](https://journalclub.io/episodes/comparative-evaluation-of-encoding-techniques-for-workflow-process-remaining-time-prediction-for-cloud-applications) |
| Source | [https://www.semanticscholar.org/paper/4d493205a1d9b056fbfc182b4467afa2ddc68148](https://www.semanticscholar.org/paper/4d493205a1d9b056fbfc182b4467afa2ddc68148) |
| Year | 2026 |
| Citations | 2 |
| Authors | Cong Liu, Wenjuan Liu, Na Guo, Rongjia Song, Yan Gu, Long Cheng |
| Paper ID | `75bc9710-d4a6-4ef5-8e5a-6f055865be9d` |

## Classification

- **Problem Type:** remaining time prediction
- **Domain:** Machine Learning & AI
- **Sub-domain:** Predictive Process Monitoring
- **Technique:** GloVe, One-Hot, Skip-Gram, CBOW, FastText
- **Technique Category:** encoding_technique
- **Type:** comparison

## Summary

This paper evaluates five event encoding techniques combined with nine deep learning models to predict the remaining time of workflow processes in cloud applications. Engineers should care because the choice of encoding technique significantly impacts prediction accuracy, which is crucial for optimizing resource allocation in cloud environments.

## Key Contribution

**The paper provides a comprehensive empirical evaluation of event encoding techniques and their effects on workflow process remaining time prediction accuracy.**

## Problem

The need to accurately predict the remaining execution time of cloud-based workflow processes to improve response times and resource allocation.

## Method

**Approach:** The method involves encoding workflow events into numerical vectors using various techniques, which are then fed into deep learning models to predict the remaining time of process instances. The evaluation compares the effectiveness of these encoding techniques across multiple models.

**Algorithm:**

1. 1. Collect event logs from workflow processes.
2. 2. Apply one of the five encoding techniques (One-Hot, Skip-Gram, CBOW, FastText, GloVe) to convert events into vectors.
3. 3. Construct a dataset from the event logs based on trace prefixes.
4. 4. Train a deep learning model (LSTM, GRU, QRNN) using the encoded vectors.
5. 5. Predict the remaining time for ongoing process instances using the trained model.
6. 6. Evaluate the prediction accuracy against real-world data.

**Input:** Event logs containing sequences of workflow events.

**Output:** Predicted remaining time for workflow processes.

**Key Parameters:**

- `N (number of discrete classifications): 10`
- `Context window size for CBOW: 2`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Eight real-world event logs were used for evaluation.

**Results:**

- Prediction accuracy was measured, with GloVe showing superior results.

**Compared against:** Traditional model-based approaches and other encoding techniques.

**Improvement:** GloVe consistently yielded better prediction accuracy compared to other encoding techniques.

## Implementation Guide

**Data Structures:** Event logs as sequences of tuples (caseid, activity, time, attributes), Vectors for encoded events

**Dependencies:** Pytorch for model implementation

**Core Operation:**

```python
encoded_events = encode(event_logs, technique='GloVe'); predictions = model.predict(encoded_events)
```

**Watch Out For:**

- Ensure the encoding technique matches the characteristics of your data.
- Be cautious of overfitting with complex models on small datasets.
- Monitor for computational overhead when using deep learning models.

## Use This When

- You need to predict the remaining time of cloud-based workflows.
- You are evaluating different encoding techniques for event data.
- You want to optimize resource allocation in cloud applications.

## Don't Use When

- You have a small dataset where complex models may overfit.
- You require real-time predictions with minimal computational overhead.
- You are working with non-sequential data.

## Key Concepts

event encoding, deep learning, workflow prediction, process mining, LSTM, GRU, QRNN

## Connects To

- LSTM
- GRU
- QRNN
- Word2Vec
- FastText

## Prerequisites

- Understanding of event logs
- Familiarity with deep learning models
- Knowledge of encoding techniques

## Limitations

- The effectiveness of encoding techniques may vary based on the specific characteristics of the event logs.
- Complex models may require significant computational resources.
- The approach may not generalize well to all types of workflows.

## Open Questions

- How can encoding techniques be further optimized for different types of workflows?
- What are the implications of privacy concerns in cross-organizational data sharing?

## Abstract

The authors are surveying the available options and benchmarking them against each other. They evaluated five different event encoding techniques, and combined them with nine deep learning models. Their goal wasn’t to invent another model, but to find out which representations of workflow events actually lead to the most accurate time predictions.
