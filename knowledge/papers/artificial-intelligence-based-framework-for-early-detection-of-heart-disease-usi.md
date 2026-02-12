# Artificial intelligence-based framework for early detection of heart disease using enhanced multilayer perceptron

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/frai.2024.1539588` |
| Full Paper | [https://doi.org/10.3389/frai.2024.1539588](https://doi.org/10.3389/frai.2024.1539588) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/f66b6637ecdda53a856be9a0114bdf58d736ee5a](https://www.semanticscholar.org/paper/f66b6637ecdda53a856be9a0114bdf58d736ee5a) |
| Source | [https://journalclub.io/episodes/artificial-intelligence-based-framework-for-early-detection-of-heart-disease-using-enhanced-multilayer-perceptron](https://journalclub.io/episodes/artificial-intelligence-based-framework-for-early-detection-of-heart-disease-using-enhanced-multilayer-perceptron) |
| Source | [https://www.semanticscholar.org/paper/f66b6637ecdda53a856be9a0114bdf58d736ee5a](https://www.semanticscholar.org/paper/f66b6637ecdda53a856be9a0114bdf58d736ee5a) |
| Year | 2026 |
| Citations | 4 |
| Authors | Monir Abdullah |
| Paper ID | `5bedff60-0a8c-4283-9bd6-d5ded6a46b01` |

## Classification

- **Problem Type:** classification
- **Domain:** Machine Learning & AI
- **Sub-domain:** Multilayer Perceptron
- **Technique:** Enhanced Multilayer Perceptron (EMLP)
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents an Enhanced Multilayer Perceptron (EMLP) framework for the early detection of heart disease, achieving a 92% accuracy on the CDC cardiac disease dataset. Engineers should care because this framework offers a reliable machine learning approach to improve early diagnosis and patient outcomes in a critical health domain.

## Key Contribution

**Introduction of the Enhanced Multilayer Perceptron (EMLP) model with advanced techniques for improved predictive accuracy in heart disease detection.**

## Problem

The need for accurate and timely detection of heart disease to prevent severe health outcomes and improve patient survival rates.

## Method

**Approach:** The EMLP model enhances traditional MLP by incorporating optimized weight initialization, adaptive learning rates, and additional hidden layers for feature extraction. This allows the model to capture complex, non-linear relationships in the data effectively.

**Algorithm:**

1. 1. Preprocess the CDC dataset by converting categorical features to numerical values and scaling numerical features to a range of 0 to 1.
2. 2. Initialize the EMLP model with specified architecture (input layer, hidden layers, output layer).
3. 3. Train the model using the processed dataset with backpropagation and regularization techniques.
4. 4. Evaluate the model's performance using metrics such as accuracy, precision, F1-score, and recall.

**Input:** CDC cardiac disease dataset containing 17 attributes including categorical and numerical features.

**Output:** Predicted classification of heart disease presence or absence.

**Key Parameters:**

- `learning_rate: 0.01`
- `number_of_hidden_layers: 2`
- `number_of_perceptrons_in_first_hidden_layer: 68`
- `number_of_perceptrons_in_second_hidden_layer: 34`

**Complexity:** Not stated

## Benchmarks

**Tested on:** CDC cardiac disease dataset with 319,795 patients and 17 attributes.

**Results:**

- accuracy: 92%
- precision: not stated
- F1-score: not stated
- recall: not stated

**Compared against:** K-Nearest Neighbor (KNN), Naïve Bayes (NB), Random Forest (RF), Support Vector Machine (SVM), Decision Tree (DT), Multilayer Perceptron (MLP)

**Improvement:** EMLP achieved 92% accuracy, surpassing all traditional methods.

## Implementation Guide

**Data Structures:** DataFrame for dataset handling, Arrays for input features, Neural network architecture for EMLP

**Dependencies:** TensorFlow, Keras, NumPy, Pandas

**Core Operation:**

```python
model = EMLP(input_shape=(17,)); model.fit(X_train, y_train); predictions = model.predict(X_test)
```

**Watch Out For:**

- Ensure proper preprocessing of categorical features to avoid model errors.
- Monitor for overfitting, especially with complex models.
- Adjust learning rates and regularization parameters based on validation performance.

## Use This When

- You need to implement a machine learning model for early detection of heart disease.
- You are working with a dataset that includes both categorical and numerical features.
- You require a model that can handle complex, non-linear relationships in data.

## Don't Use When

- The dataset is small or lacks diversity.
- Real-time predictions are required with minimal computational resources.
- You need a model that is easily interpretable for clinical settings.

## Key Concepts

multilayer perceptron, feature extraction, weight initialization, adaptive learning rates, regularization techniques, cardiac disease detection, machine learning classification

## Connects To

- Multilayer Perceptron (MLP)
- K-Nearest Neighbor (KNN)
- Random Forest (RF)
- Support Vector Machine (SVM)
- Deep Learning Techniques
- Ensemble Learning Methods

## Prerequisites

- Understanding of neural networks
- Familiarity with machine learning classification techniques
- Knowledge of data preprocessing methods

## Limitations

- Model performance may degrade with imbalanced datasets.
- Requires careful tuning of hyperparameters for optimal performance.
- Complexity may lead to longer training times.

## Open Questions

- How can the EMLP model be adapted for real-time prediction?
- What additional features could improve the model's accuracy further?

## Abstract

A simple perceptron is the most basic type of artificial neural network. It consists of a single layer of neurons that directly map input features to an output. Each neuron in a perceptron receives multiple numerical inputs, applies a corresponding weight to each, sums the weighted inputs, and then passes the result through an activation function that produces an output. This is typically a step function that produces a binary output. This means a perceptron functions as a linear classifier, capable of distinguishing between two classes only if they are linearly separable (meaning they can be divided by a straight line or a hyperplane). While these are effective for simple classification problems like AND or OR logic gates, a single-layer perceptron fails to model more complex relationships where data points cannot be neatly separated by a single decision boundary. A multilayer perceptron (MLP) extends the capabilities of a simple perceptron by introducing one or more hidden layers between the input and output layers. These hidden layers contain
