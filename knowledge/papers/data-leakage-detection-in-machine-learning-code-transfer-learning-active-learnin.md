# Data leakage detection in machine learning code: transfer learning, active learning, or low-shot prompting?

## Access

| Field | Value |
|-------|-------|
| DOI | `10.7717/peerj-cs.2730` |
| Full Paper | [https://doi.org/10.7717/peerj-cs.2730](https://doi.org/10.7717/peerj-cs.2730) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/3aa9944282b0345bf2ccf23e6ef8d02c38c23ddf](https://www.semanticscholar.org/paper/3aa9944282b0345bf2ccf23e6ef8d02c38c23ddf) |
| Source | [https://journalclub.io/episodes/data-leakage-detection-in-machine-learning-code-transfer-learning-active-learning-or-low-shot-prompting](https://journalclub.io/episodes/data-leakage-detection-in-machine-learning-code-transfer-learning-active-learning-or-low-shot-prompting) |
| Source | [https://www.semanticscholar.org/paper/3aa9944282b0345bf2ccf23e6ef8d02c38c23ddf](https://www.semanticscholar.org/paper/3aa9944282b0345bf2ccf23e6ef8d02c38c23ddf) |
| Year | 2026 |
| Citations | 3 |
| Authors | Nouf Alturayeif, Jameleddine Hassine |
| Paper ID | `2f89d54f-5458-4e8c-a2da-346b504b5882` |

## Classification

- **Problem Type:** data leakage detection
- **Domain:** Software Engineering
- **Sub-domain:** Machine Learning Code Quality
- **Technique:** Transfer Learning, Active Learning, Low-shot Prompting
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents methods for detecting data leakage in machine learning code using transfer learning, active learning, and low-shot prompting. Engineers should care because data leakage can lead to misleading performance metrics, and the proposed methods can automate the detection process, improving code quality and reliability.

## Key Contribution

**Introduction of ML-based approaches for detecting data leakage in ML code using limited annotated datasets.**

## Problem

Data leakage occurs when information from the test set inadvertently influences the training process, leading to inflated performance metrics that do not generalize well to new data.

## Method

**Approach:** The method involves training models using transfer learning, active learning, and low-shot prompting to detect data leakage in ML code. The models are trained on a dataset of code snippets labeled for data leakage.

**Algorithm:**

1. 1. Collect and annotate a dataset of Python ML code snippets.
2. 2. Identify types of data leakage (overlap, multi-test, preprocessing).
3. 3. Map leakage types to ML pipeline phases.
4. 4. Filter code snippets to include only those associated with potential leakage.
5. 5. Train models using transfer learning, active learning, or low-shot prompting.
6. 6. Evaluate model performance using metrics like F2-score.

**Input:** Python code snippets labeled as having data leakage or not.

**Output:** Predictions indicating whether a code snippet contains data leakage.

**Key Parameters:**

- `learning_rate: 0.001`
- `number_of_samples: 698 (after active learning)`
- `dataset_size: 1,904 samples`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Custom dataset of 1,904 labeled Python code snippets

**Results:**

- F2-score: 0.72
- Precision and Recall (not specified)

**Compared against:** Manual detection methods, code analysis approaches

**Improvement:** Active learning reduced the number of needed annotated samples from 1,523 to 698.

## Implementation Guide

**Data Structures:** Dataset of labeled code snippets, Mapping table for leakage types

**Dependencies:** CodeBERT, GPT, Python libraries for ML

**Core Operation:**

```python
model.train(data) # Train model on filtered code snippets
```

**Watch Out For:**

- Ensure proper labeling of data to avoid false positives.
- Be cautious of the imbalance in the dataset.
- Monitor model performance to avoid overfitting.

## Use This When

- You need to automate the detection of data leakage in ML code.
- You have limited annotated datasets for training models.
- You want to improve the quality of ML code in production.

## Don't Use When

- You have a large annotated dataset available for training.
- You require real-time detection with minimal latency.
- You are working in a domain where data leakage is not a concern.

## Key Concepts

data leakage, transfer learning, active learning, low-shot prompting

## Connects To

- CodeBERT
- GPT
- Static code analysis
- Dynamic code analysis

## Prerequisites

- Understanding of ML code quality issues
- Familiarity with transfer learning techniques
- Knowledge of active learning strategies

## Limitations

- Performance may vary based on the quality of the labeled dataset.
- May not generalize well to all types of data leakage.
- Requires careful tuning of parameters for optimal performance.

## Open Questions

- How can these methods be adapted for other programming languages?
- What additional features could improve the detection of complex data leakage scenarios?

## Abstract

Data leakage occurs during training, when information that should be unavailable to the model inadvertently influences its learning process. Think of it as contamination. Your testing/evaluation data somehow got into the training data. As you can guess, this can lead to overly optimistic performance metrics that do not translate into real-world effectiveness. This issue is particularly insidious because it masquerades as a highly successful model, with impressive training and validation results that collapse once the model is deployed. The problem is not that the model has failed to learn meaningful patterns, but rather that it has learned patterns it should never have had access to in the first place. As a result, the model does not actually generalize but instead exploits unintended shortcuts in the data. So how does this happen? There are several ways, and they stem from flaws in your data pipeline
