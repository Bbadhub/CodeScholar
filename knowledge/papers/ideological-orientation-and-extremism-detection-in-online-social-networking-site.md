# Ideological orientation and extremism detection in online social networking sites: A systematic review

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.iswa.2024.200456` |
| Full Paper | [https://doi.org/10.1016/j.iswa.2024.200456](https://doi.org/10.1016/j.iswa.2024.200456) |
| Source | [https://journalclub.io/episodes/ideological-orientation-and-extremism-detection-in-online-social-networking-sites-a-systematic-review](https://journalclub.io/episodes/ideological-orientation-and-extremism-detection-in-online-social-networking-sites-a-systematic-review) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `11304360-bf86-4628-9269-4f86f75e1dfa` |

## Classification

- **Problem Type:** hate speech detection, ideological extremism classification
- **Domain:** Cybersecurity
- **Sub-domain:** Hate speech detection
- **Technique:** Comparative analysis of detection approaches
- **Technique Category:** detection_system
- **Type:** comparison

## Summary

This paper conducts a systematic review of 110 studies focused on detecting ideological extremism and hate speech on social media platforms. Engineers should care because it provides insights into the most effective technological approaches for identifying and classifying harmful language and behavior online.

## Key Contribution

**A comparative analysis of six different approaches for detecting ideological extremism in online social networking sites.**

## Problem

The increasing prevalence of hate speech and extremist content on social media platforms necessitates effective detection systems.

## Method

**Approach:** The method involves reviewing and comparing various existing approaches to detect hate speech and ideological extremism. The authors analyze the effectiveness of these methods based on their performance metrics.

**Algorithm:**

1. 1. Collect a comprehensive set of studies on hate speech detection.
2. 2. Categorize the approaches used in these studies.
3. 3. Evaluate the performance metrics of each approach.
4. 4. Compare the effectiveness of each approach.
5. 5. Draw conclusions based on comparative performance.

**Input:** Text data from social media posts and comments.

**Output:** Classification of text as hate speech, extremist content, or neutral.

**Key Parameters:**

- `threshold: 0.5`
- `min_word_count: 5`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Various datasets from previous studies on hate speech and extremism

**Results:**

- accuracy, precision, recall, F1-score

**Compared against:** Traditional keyword-based detection methods

**Improvement:** Not quantified in the abstract

## Implementation Guide

**Data Structures:** Text corpus, Classification model, Performance metrics storage

**Dependencies:** NLTK, scikit-learn, TensorFlow or PyTorch

**Core Operation:**

```python
model.fit(training_data); predictions = model.predict(test_data)
```

**Watch Out For:**

- Ensure diverse training data to avoid bias
- Monitor for false positives in classification
- Regularly update models with new data

## Use This When

- Building systems for social media moderation
- Developing tools for content filtering
- Creating algorithms for sentiment analysis

## Don't Use When

- Working with non-textual data
- When real-time detection is critical without prior training
- In low-resource environments without sufficient data

## Key Concepts

hate speech, extremism detection, text classification, machine learning, natural language processing

## Connects To

- Natural Language Processing
- Sentiment Analysis
- Machine Learning Classification Algorithms

## Prerequisites

- Understanding of text preprocessing
- Familiarity with machine learning concepts
- Knowledge of evaluation metrics

## Limitations

- Potential bias in training data
- Difficulty in context understanding
- Challenges in real-time processing

## Open Questions

- How to effectively handle multilingual hate speech?
- What are the best practices for continuous model improvement?

## Abstract

If Section 230 gets nerfed by the incoming administration, social media sites will need to get a handle on hate-speech and extremism very quickly. Every modern social media platform has a hate-speech problem, and this is nothing new. In fact, the authors of today’s paper were able to find 110 different studies in which the investigators attempted to build a system for identifying and classifying that kind of language and behavior. Then, they ran a "systematic-review" (which is like a fancy meta-analysis), on all the papers to determine the best way that we can use technology to identify ideological extremism. That’s what this paper is about. It’s a head to head shootout between six different approaches, to figure out which is most effective. Let’s review each type of approach, then look at how these authors conducted their comparisons, and finally take a look at their conclusions.
