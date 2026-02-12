# Deep learning and explainable AI for classification of potato leaf diseases

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/frai.2024.1449329` |
| Full Paper | [https://doi.org/10.3389/frai.2024.1449329](https://doi.org/10.3389/frai.2024.1449329) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/6a375ee3b9d37a38e5e230ddaf28cf6e3ef929fd](https://www.semanticscholar.org/paper/6a375ee3b9d37a38e5e230ddaf28cf6e3ef929fd) |
| Source | [https://journalclub.io/episodes/deep-learning-and-explainable-ai-for-classification-of-potato-leaf-diseases](https://journalclub.io/episodes/deep-learning-and-explainable-ai-for-classification-of-potato-leaf-diseases) |
| Source | [https://www.semanticscholar.org/paper/6a375ee3b9d37a38e5e230ddaf28cf6e3ef929fd](https://www.semanticscholar.org/paper/6a375ee3b9d37a38e5e230ddaf28cf6e3ef929fd) |
| Year | 2026 |
| Citations | 19 |
| Authors | Sarah M. Alhammad, D. S. Khafaga, W. M. El-Hady, Farid M. Samy, Khalid M. Hosny |
| Paper ID | `7c48570c-a379-4043-8d7e-ff15eaf34164` |

## Classification

- **Problem Type:** multi-class classification
- **Domain:** Machine Learning & AI
- **Sub-domain:** Deep Learning, Explainable AI
- **Technique:** VGG16 with Grad-CAM
- **Technique Category:** neural_architecture
- **Type:** adaptation

## Summary

This paper presents a deep learning model using transfer learning with VGG16 for classifying potato leaf diseases, achieving high accuracy and incorporating explainable AI techniques for interpretability. Engineers should care because it provides a practical solution for disease identification in agriculture, enhancing crop management.

## Key Contribution

**A transfer learning-based deep learning model combined with explainable AI techniques for potato leaf disease classification.**

## Problem

The need for accurate and timely identification of potato leaf diseases to prevent crop losses and ensure agricultural productivity.

## Method

**Approach:** The method utilizes a pre-trained VGG16 model, fine-tuning it for potato leaf disease classification. Grad-CAM is applied to provide visual explanations of the model's predictions.

**Algorithm:**

1. 1. Load the pre-trained VGG16 model without its classification layers.
2. 2. Freeze the convolutional layers to retain learned features.
3. 3. Add custom classification layers for three classes: early blight, late blight, and healthy.
4. 4. Apply dropout layers to prevent overfitting.
5. 5. Train the model using the potato leaf dataset.
6. 6. Use Grad-CAM to generate class activation maps for interpretability.

**Input:** Images of potato leaves resized to 224x224 pixels.

**Output:** Predicted class labels for potato leaf diseases and Grad-CAM visualizations.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 32`
- `epochs: 100`

**Complexity:** not stated

## Benchmarks

**Tested on:** PlantVillage dataset with 2,152 images

**Results:**

- validation accuracy: 97%
- testing accuracy: 98%
- precision: 98%
- recall: 98%
- F1-score: 98%

**Compared against:** Other deep learning models including AlexNet, GoogleNet, InceptionResNetV2

**Improvement:** The proposed model outperformed existing methods, achieving the highest accuracy.

## Implementation Guide

**Data Structures:** Image arrays, Class labels

**Dependencies:** TensorFlow, Keras

**Core Operation:**

```python
model.fit(training_data, training_labels, epochs=100, batch_size=32)
```

**Watch Out For:**

- Ensure the input images are correctly preprocessed to match VGG16 requirements.
- Monitor for overfitting and adjust dropout rates accordingly.
- Grad-CAM visualizations may vary based on the model architecture.

## Use This When

- You need to classify images of potato leaves for disease detection.
- You require a model that provides interpretability for its predictions.
- You have limited labeled data for training a deep learning model.

## Don't Use When

- You need real-time classification with very low latency.
- You have a very large dataset that can be trained from scratch.
- You require a model that does not need interpretability.

## Key Concepts

transfer learning, VGG16, Grad-CAM, explainable AI, multi-class classification

## Connects To

- Transfer learning
- Convolutional Neural Networks
- Explainable AI techniques

## Prerequisites

- Understanding of CNNs
- Familiarity with transfer learning
- Basic knowledge of explainable AI

## Limitations

- Model performance may degrade with highly complex images.
- Interpretability may be less clear with deeper models.
- Limited to the classes defined in the training dataset.

## Open Questions

- How can additional XAI methods improve model interpretability?
- What impact does dataset diversity have on model robustness?

## Abstract

As you would probably guess, they decided to use a convolutional neural network (CNN) as the classifier itself. This is a type of artificial neural network commonly optimized for analyzing visual data. Rather than train from scratch, they decided to use transfer learning, where a pre-trained CNN, specifically VGG16, was adapted to their new use-case. VGG16 is a well-established architecture originally trained on ImageNet. By leveraging the knowledge that’s already encoded in its convolutional layers, it can extract meaningful patterns from potato leaf images without requiring a vast dataset for training. All the researchers needed to do is replace the final classification layers of that model with custom layers suited for their specific classification task. To enhance interpretability, they incorporated Grad-CAM: Gradient-weighted Class Activation Mapping. This is a technique that
