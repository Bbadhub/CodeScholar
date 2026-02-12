# Urban sentiment mapping using language and vision models in spatial analysis

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fcomp.2025.1504523` |
| Full Paper | [https://doi.org/10.3389/fcomp.2025.1504523](https://doi.org/10.3389/fcomp.2025.1504523) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/a19889c15678c3afc68052fe1befa437ec355e0e](https://www.semanticscholar.org/paper/a19889c15678c3afc68052fe1befa437ec355e0e) |
| Source | [https://journalclub.io/episodes/urban-sentiment-mapping-using-language-and-vision-models-in-spatial-analysis](https://journalclub.io/episodes/urban-sentiment-mapping-using-language-and-vision-models-in-spatial-analysis) |
| Source | [https://www.semanticscholar.org/paper/a19889c15678c3afc68052fe1befa437ec355e0e](https://www.semanticscholar.org/paper/a19889c15678c3afc68052fe1befa437ec355e0e) |
| Year | 2026 |
| Citations | 9 |
| Authors | Jayedi Aman, T. Matisziw |
| Paper ID | `71259531-c1af-4271-a474-8a7ca6bedb74` |

## Classification

- **Problem Type:** Sentiment analysis in urban environments
- **Domain:** Machine Learning & AI
- **Sub-domain:** Sentiment analysis, Urban studies
- **Technique:** BERT, PSPNet, Mask R-CNN
- **Technique Category:** neural_architecture
- **Type:** adaptation

## Summary

The paper presents a two-phase computational framework for urban sentiment mapping that combines language and vision models to analyze public sentiment based on social media data and street view imagery. Engineers should care because this approach provides a scalable and efficient method to understand urban environments and their emotional impacts, which can inform urban planning and design.

## Key Contribution

**Integration of NLP and computer vision techniques to analyze urban sentiment through social media and street view imagery.**

## Problem

City planners struggle to understand public sentiment about urban environments due to limitations of traditional methods like surveys and interviews.

## Method

**Approach:** The method consists of two phases: first, sentiment inference using a BERT-based model to analyze geotagged social media posts; second, urban context inference using computer vision models like PSPNet and Mask R-CNN to analyze street view imagery for urban design features.

**Algorithm:**

1. 1. Collect geotagged social media posts from platforms like Instagram.
2. 2. Use BERT to analyze captions and extract sentiment scores.
3. 3. Retrieve street view images corresponding to the locations of the posts.
4. 4. Apply PSPNet and Mask R-CNN to segment and classify urban features from the images.
5. 5. Integrate sentiment scores with urban design features.
6. 6. Perform statistical analysis to evaluate relationships between sentiment and urban features.

**Input:** Geotagged social media posts (captions) and street view images.

**Output:** Sentiment scores linked to urban design features, visualized sentiment patterns.

**Key Parameters:**

- `BERT model: pre-trained on social media data`
- `PSPNet: for semantic segmentation of urban features`
- `Mask R-CNN: for object detection in street view images`

**Complexity:** Not stated

## Benchmarks

**Tested on:** 63,861 Instagram posts (filtered to 47,107 for analysis), Google Street View images

**Results:**

- Sentiment classification: Positive (1) or Negative (0)
- Correlation and regression analyses for sentiment-urban feature relationships

**Compared against:** Traditional survey methods for sentiment analysis

**Improvement:** Not stated

## Implementation Guide

**Data Structures:** DataFrame for storing social media posts and sentiment scores, Image arrays for street view images

**Dependencies:** Hugging Face Transformers for BERT, OpenCV for image processing, TensorFlow or PyTorch for model training, Google API for retrieving street view images

**Core Operation:**

```python
sentiment_scores = BERT.analyze(captions); urban_features = PSPNet.analyze(street_view_images); integrate(sentiment_scores, urban_features)
```

**Watch Out For:**

- Ensure geotagged data is accurate and comprehensive.
- Watch out for biases in social media data.
- Consider the computational resources needed for model training.

## Use This When

- You need to analyze public sentiment about urban spaces using social media data.
- You want to correlate emotional responses with urban design features.
- You are working on urban planning projects that require data-driven insights.

## Don't Use When

- You have limited access to social media data.
- You require real-time sentiment analysis.
- You are focusing on non-urban sentiment analysis.

## Key Concepts

Sentiment analysis, Urban design features, Natural language processing, Computer vision, Geospatial analysis, Social media data

## Connects To

- Sentiment analysis frameworks
- Geospatial data analysis tools
- Urban planning software
- Computer vision techniques for urban studies

## Prerequisites

- Understanding of natural language processing
- Familiarity with computer vision techniques
- Knowledge of urban design principles

## Limitations

- Dependent on the availability of geotagged social media data.
- May not capture sentiments from non-digital demographics.
- Limited to the quality of the models used for sentiment and feature extraction.

## Open Questions

- How can this framework be adapted for real-time sentiment analysis?
- What are the implications of sentiment analysis on urban policy-making?

## Abstract

City planners have always struggled with understanding how people feel about their environments. Sure, there are surveys, interviews, and field observations, but these methods often fall short. They’re slow, limited in scope, and often fail to reflect the everyday experiences of real people across a city. There have been attempts to close this gap in the past. But their methods often relied on small datasets, simplistic tools, and manual analysis. The result is a blurry picture that lacks fine-grained emotional detail. That’s exactly what researchers are trying to solve. For this they designed a two-phase system: Phase 1: They used a large language model to analyze Instagram captions and determine the corresponding sentiment within that area. Phase 2: They used computer vision tools to analyze the corresponding street view imagery around each post. That way, they could directly correlate how people felt with what those places actually looked like.
