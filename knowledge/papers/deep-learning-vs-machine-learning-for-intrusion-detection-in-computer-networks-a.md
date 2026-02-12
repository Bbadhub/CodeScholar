# Deep Learning vs. Machine Learning for Intrusion Detection in Computer Networks: A Comparative Study

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/app15041903` |
| Full Paper | [https://doi.org/10.3390/app15041903](https://doi.org/10.3390/app15041903) |
| Source | [https://journalclub.io/episodes/deep-learning-vs-machine-learning-for-intrusion-detection-in-computer-networks-a-comparative-study](https://journalclub.io/episodes/deep-learning-vs-machine-learning-for-intrusion-detection-in-computer-networks-a-comparative-study) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `7ead89e7-d392-42dd-8c89-767afeb8d9b5` |

## Classification

- **Problem Type:** intrusion detection
- **Domain:** Cybersecurity
- **Sub-domain:** Intrusion Detection Systems
- **Technique:** Convolutional Neural Network (CNN), Long Short-Term Memory (LSTM), Random Forest
- **Technique Category:** neural_architecture
- **Type:** comparison

## Summary

This study compares deep learning models with traditional machine learning algorithms for intrusion detection in computer networks. Engineers should care because deep learning approaches, particularly CNN and LSTM, show significant promise in detecting novel attack patterns that traditional systems may miss.

## Key Contribution

**The application of deep learning models, particularly CNN and LSTM, significantly enhances the accuracy of intrusion detection systems compared to traditional machine learning methods.**

## Problem

The increasing sophistication of cyber threats necessitates more effective intrusion detection systems capable of identifying novel attack patterns.

## Method

**Approach:** The method involves training various deep learning models (CNN, LSTM) and traditional machine learning algorithms (logistic regression, random forest) on network traffic data. The models are evaluated based on their ability to detect intrusions, with a focus on accuracy and false positive rates.

**Algorithm:**

1. 1. Preprocess the CICIDS2017 dataset by handling missing values and removing duplicates.
2. 2. Consolidate similar attack labels to reduce classification complexity.
3. 3. Apply SMOTE to balance the dataset and generate synthetic samples for underrepresented classes.
4. 4. Scale features using StandardScaler to ensure equal contribution to distance calculations.
5. 5. Train multiple models (CNN, LSTM, random forest, etc.) using the preprocessed data.
6. 6. Optimize hyperparameters using random search.
7. 7. Evaluate model performance using metrics such as accuracy and F1 score.

**Input:** CICIDS2017 dataset containing network traffic data with various features.

**Output:** Classification results indicating whether network traffic is normal or malicious.

**Key Parameters:**

- `learning_rate: not stated`
- `number_of_epochs: not stated`
- `batch_size: not stated`
- `SMOTE_ratio: not stated`

**Complexity:** not stated

## Benchmarks

**Tested on:** CICIDS2017

**Results:**

- accuracy: 98% for CNN and LSTM, 99.9% for Random Forest

**Compared against:** traditional machine learning algorithms (logistic regression, naive Bayes, random forest, K-nearest neighbors, decision trees)

**Improvement:** Deep learning models outperform traditional methods, with random forest achieving the highest accuracy at 99.9%.

## Implementation Guide

**Data Structures:** DataFrame for dataset handling, Arrays for model input

**Dependencies:** TensorFlow/Keras for deep learning models, Scikit-learn for traditional ML models and preprocessing

**Core Operation:**

```python
model.fit(X_train, y_train) # Train model on preprocessed data
```

**Watch Out For:**

- Ensure proper handling of class imbalance to avoid biased models.
- Monitor for overfitting during training, especially with deep learning models.
- Optimize hyperparameters effectively to improve model performance.

## Use This When

- You need to detect novel attack patterns in network traffic.
- You are dealing with imbalanced datasets in intrusion detection.
- You require high accuracy in classifying network traffic as normal or malicious.

## Don't Use When

- You have limited computational resources for model training.
- The dataset is small and does not require complex models.
- Real-time processing is critical and deep learning models introduce unacceptable latency.

## Key Concepts

deep learning, machine learning, intrusion detection, SMOTE, feature engineering, hyperparameter tuning

## Connects To

- Random Forest
- Support Vector Machines
- K-Nearest Neighbors
- Logistic Regression
- Hybrid models combining ML and DL

## Prerequisites

- Understanding of machine learning concepts
- Familiarity with deep learning frameworks
- Knowledge of network traffic analysis

## Limitations

- Deep learning models may require significant computational resources.
- Interpretability of deep learning models can be challenging.
- Performance may vary based on the quality of the training data.

## Open Questions

- How can deep learning models be made more interpretable in intrusion detection?
- What are the best practices for deploying these models in real-time environments?

## Abstract

Traditional rule-based systems are only good at checking for the threats they've seen before. Check for someone pinging this port in this specific way. Look out for URLs that embed would-be SQL injections in the query string, etc. But what happens when the attacker does something new? When the behavior simply doesn’t look like anything the system has been built to detect. This is the challenge being tackled in today's paper. The authors are trying to determine if deep-learning models might be the answer here. Is it possible that they’ll be able to pick up the slack, and detect novel attack patterns that rule-based systems might have missed? On today’s episode we’ll walk through how they conducted their analysis, and the results they obtained
