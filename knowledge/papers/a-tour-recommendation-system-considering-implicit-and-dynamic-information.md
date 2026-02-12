# A Tour Recommendation System Considering Implicit and Dynamic Information

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/app14209271` |
| Full Paper | [https://doi.org/10.3390/app14209271](https://doi.org/10.3390/app14209271) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/508927f0a4b349901e6238cc523db6228ccd51fa](https://www.semanticscholar.org/paper/508927f0a4b349901e6238cc523db6228ccd51fa) |
| Source | [https://journalclub.io/episodes/a-tour-recommendation-system-considering-implicit-and-dynamic-information](https://journalclub.io/episodes/a-tour-recommendation-system-considering-implicit-and-dynamic-information) |
| Source | [https://www.semanticscholar.org/paper/508927f0a4b349901e6238cc523db6228ccd51fa](https://www.semanticscholar.org/paper/508927f0a4b349901e6238cc523db6228ccd51fa) |
| Year | 2026 |
| Citations | 8 |
| Authors | Chieh-Yuan Tsai, Kai-Wen Chuang, Hen-Yi Jen, Hao Huang |
| Paper ID | `0fb3523d-25bb-4eb1-a057-9c2dc84e3b8f` |

## Classification

- **Problem Type:** personalized itinerary recommendation
- **Domain:** Software Engineering
- **Sub-domain:** Recommendation Systems
- **Technique:** Tour Recommendation System
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a novel tour recommendation system that utilizes implicit and dynamic information from social media to provide personalized itinerary suggestions for tourists. Engineers should care because this system enhances user satisfaction by considering user preferences, dynamic staying times, and visiting sequences, leading to more accurate recommendations.

## Key Contribution

**The introduction of a tour recommendation system that leverages implicit features from textual descriptions of Points-of-Interest (POIs) and dynamic staying time predictions using Non-negative Matrix Factorization (NMF).**

## Problem

The challenge of creating practical and personalized tour itineraries for tourists who prefer self-guided tours over traditional package itineraries.

## Method

**Approach:** The method involves extracting implicit features from POI textual descriptions, clustering users based on their visiting sequences, predicting dynamic staying times using NMF, and generating personalized itineraries based on user preferences and time constraints.

**Algorithm:**

1. 1. Collect photo records with GPS coordinates and timestamps.
2. 2. Assign the nearest POI to each photo record based on GPS location.
3. 3. Extract implicit features from POI textual descriptions using TF-IDF and Autoencoder.
4. 4. Transform visiting sequences into implicit vectors and cluster users using K-Means based on cosine similarity.
5. 5. Evaluate user preferences for each POI based on historical visit data.
6. 6. Predict dynamic staying times for users at different POIs using NMF.
7. 7. Generate the personalized itinerary with the highest preference score and longest remaining time.

**Input:** User's previous visiting sequence, request, and time limitation.

**Output:** Personalized itinerary with the highest preference score and longest remaining time.

**Key Parameters:**

- `wpop: weight of popularity, e.g., 0.5`
- `watt: weight of attraction, e.g., 0.5`
- `k: number of nearest neighbors for user-based preference calculation, e.g., 5`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Social media photo dataset with GPS coordinates and timestamps

**Results:**

- Accuracy, Precision, Recall, F1-score

**Compared against:** State-of-the-art next POI recommendation methods

**Improvement:** Outperforms state-of-the-art methods across four commonly used evaluation metrics.

## Implementation Guide

**Data Structures:** User check-in records, POI feature vectors, User clusters

**Dependencies:** Libraries for NMF, K-Means clustering, and text processing (e.g., scikit-learn, pandas, numpy)

**Core Operation:**

```python
for each user in users: assign_POI(user.photo); extract_features(POI); cluster_users(users); generate_itinerary(user);
```

**Watch Out For:**

- Ensure the textual descriptions of POIs are comprehensive for accurate feature extraction.
- Be cautious with the choice of k in K-Means clustering to avoid overfitting.
- Dynamic staying time predictions require sufficient historical data to be effective.

## Use This When

- You need to create a personalized itinerary for tourists based on their preferences.
- You want to utilize social media data to enhance recommendation accuracy.
- You need to account for varying staying times at different POIs.

## Don't Use When

- The dataset lacks sufficient social media photo records.
- You require a simple recommendation system without dynamic factors.
- The user base is too small to form meaningful clusters.

## Key Concepts

Implicit features, Dynamic staying time, User clustering, Personalized recommendations

## Connects To

- Collaborative filtering techniques
- Graph-based recommendation systems
- Reinforcement learning for dynamic recommendations

## Prerequisites

- Understanding of recommendation system principles
- Familiarity with clustering algorithms
- Knowledge of text processing techniques

## Limitations

- Dependent on the quality and quantity of social media data.
- May not perform well with sparse user data.
- Dynamic staying time predictions may not be accurate without sufficient historical data.

## Open Questions

- How can the system be adapted for different cultural contexts in tourism?
- What additional data sources could further enhance recommendation accuracy?

## Abstract

When I go on vacation, I like to do: nothing. I want to fly to wherever I’m going, sleep all day, chill all night, lay around the room, lay around the pool, order room service, be a sloth. For me, the idea of having to wake up early, put on actual clothes, and go do something sounds completely insane. Why anyone would jam-pack their vacation time with an itinerary full of stuff they have to do is beyond me. That just sounds like work.
