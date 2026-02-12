# Photograph-based machine learning approach for automated detection and differentiation of aerial blight disease in soybean crops

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s40537-025-01191-w` |
| Full Paper | [https://doi.org/10.1186/s40537-025-01191-w](https://doi.org/10.1186/s40537-025-01191-w) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/6559b69e45f120e5d8979c5ae0b70c385bd7ae26](https://www.semanticscholar.org/paper/6559b69e45f120e5d8979c5ae0b70c385bd7ae26) |
| Source | [https://journalclub.io/episodes/photograph-based-machine-learning-approach-for-automated-detection-and-differentiation-of-aerial-blight-disease-in-soybean-crops](https://journalclub.io/episodes/photograph-based-machine-learning-approach-for-automated-detection-and-differentiation-of-aerial-blight-disease-in-soybean-crops) |
| Source | [https://www.semanticscholar.org/paper/6559b69e45f120e5d8979c5ae0b70c385bd7ae26](https://www.semanticscholar.org/paper/6559b69e45f120e5d8979c5ae0b70c385bd7ae26) |
| Year | 2026 |
| Citations | 1 |
| Authors | Mukta Nainwal, Anurag Satpathi, Saqib Nizam Shamsi, Ali Salem, A. Nain, Dinesh Kumar Vishwakarma |
| Paper ID | `290ee3e4-5edd-4e72-9d05-62a6c2c2d8fa` |

## Classification

- **Problem Type:** multi-class classification
- **Domain:** Machine Learning & AI
- **Sub-domain:** Image Classification
- **Technique:** ResNet-34
- **Technique Category:** classification_model
- **Type:** comparison

## Summary

This paper presents a machine learning approach for the automated detection and differentiation of aerial blight disease in soybean crops using smartphone imagery. Engineers should care because it offers a scalable solution to a significant agricultural problem, enhancing crop management and minimizing yield losses.

## Key Contribution

**The study demonstrates the effectiveness of various machine learning algorithms, particularly ResNet-34 with data augmentation, achieving a classification accuracy of 95.64%.**

## Problem

The work is motivated by the need for timely identification and management of aerial blight disease in soybean crops to prevent substantial yield losses.

## Method

**Approach:** The method involves capturing images of soybean leaves, preprocessing them to remove noise, applying data augmentation techniques, and then classifying the images using various machine learning algorithms. The focus is on classifying diseases rather than segmenting lesions.

**Algorithm:**

1. 1. Capture images of soybean leaves using smartphones.
2. 2. Preprocess images to remove noise and enhance quality.
3. 3. Apply data augmentation techniques such as rotation, flipping, and zooming.
4. 4. Split the dataset into training (80%), validation (15%), and testing (5%) sets.
5. 5. Train various classifiers including Logistic Regression, SVM, VGG-16, ResNet-18, and ResNet-34.
6. 6. Evaluate model performance using the test set.
7. 7. Select the best-performing model based on accuracy.

**Input:** Images of soybean leaves categorized into eight classes: healthy leaves, bacterial pustules, insect attacked, multiple diseases leaf, rhizoctonia aerial blight, severe rhizoctonia aerial blight, viral diseases, and bacterial blight.

**Output:** Classified disease type for each input image.

**Key Parameters:**

- `image_size: 224x224 pixels (Logistic Regression, SVM, VGG-16)`
- `image_size: 299x299 pixels (ResNet-18)`
- `augmentation: random rotation, flipping, zooming (up to 10%)`

**Complexity:** not stated

## Benchmarks

**Tested on:** Images collected from soybean fields at Crop Research Centre, G.B. Pant University of Agriculture & Technology.

**Results:**

- accuracy: 95.64% (ResNet-34 with data augmentation)
- accuracy: 66.77% (Logistic Regression)

**Compared against:** Logistic Regression, Support Vector Machine (SVM), VGG-16, ResNet-18, ResNet-34

**Improvement:** ResNet-34 with data augmentation achieved a 28.87% improvement over Logistic Regression.

## Implementation Guide

**Data Structures:** Image arrays, Label arrays for classification

**Dependencies:** TensorFlow, Keras, OpenCV

**Core Operation:**

```python
model.fit(training_data, training_labels); predictions = model.predict(test_data)
```

**Watch Out For:**

- Ensure images are preprocessed to remove noise.
- Be cautious of class imbalance; it may affect model performance.
- Data augmentation should be carefully applied to avoid overfitting.

## Use This When

- You need to classify plant diseases from images.
- You have access to smartphone imagery for data collection.
- You are dealing with imbalanced datasets in agricultural applications.

## Don't Use When

- You require precise lesion segmentation rather than classification.
- You have limited computational resources for deep learning models.
- You need real-time processing capabilities.

## Key Concepts

data augmentation, image preprocessing, convolutional neural networks, classification algorithms, machine learning, disease detection, smartphone imaging

## Connects To

- Transfer Learning
- Image Segmentation
- Data Augmentation Techniques

## Prerequisites

- Understanding of machine learning concepts
- Familiarity with convolutional neural networks
- Basic knowledge of image processing

## Limitations

- The model may struggle with generalization across different environmental conditions.
- Dependency on high-quality images for accurate classification.
- Limited to the specific diseases and conditions studied.

## Open Questions

- How can the model be adapted for other crops and diseases?
- What additional features could improve classification accuracy?

## Abstract

The labels (for each category) were assigned manually. But to be clear, this is weakly labeled data with class boundaries that are inherently fuzzy. Some conditions, like insect damage versus early-stage Rhizoctonia, share a lot of features. Others, like the multi-disease class, are purposefully ambiguous. And that ambiguity carries through to training, so any model working on this dataset will have to deal with imprecision not just in the image quality, but in the ground truth itself. The dataset also reflects a natural class imbalance. Rhizoctonia is the dominant disease in the region and appears more frequently in the data than the others. Rarer classes like bacterial pustules and viral diseases have fewer examples. This imbalance is not corrected with oversampling or synthetic expansion at this stage. It is left intact during collection to reflect realistic deployment distributions.
