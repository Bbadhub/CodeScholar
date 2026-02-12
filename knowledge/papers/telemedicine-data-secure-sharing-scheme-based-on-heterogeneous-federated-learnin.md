# Telemedicine data secure sharing scheme based on heterogeneous federated learning

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s42400-024-00250-8` |
| Full Paper | [https://doi.org/10.1186/s42400-024-00250-8](https://doi.org/10.1186/s42400-024-00250-8) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/2e8485271e5e782a3c6a936fd9e46d4c03131762](https://www.semanticscholar.org/paper/2e8485271e5e782a3c6a936fd9e46d4c03131762) |
| Source | [https://journalclub.io/episodes/telemedicine-data-secure-sharing-scheme-based-on-heterogeneous-federated-learning](https://journalclub.io/episodes/telemedicine-data-secure-sharing-scheme-based-on-heterogeneous-federated-learning) |
| Source | [https://www.semanticscholar.org/paper/2e8485271e5e782a3c6a936fd9e46d4c03131762](https://www.semanticscholar.org/paper/2e8485271e5e782a3c6a936fd9e46d4c03131762) |
| Year | 2026 |
| Citations | 3 |
| Authors | Nansen Wang, Jianing Zhang, Ju Huang, Wei Ou, Wenbao Han, Qionglu Zhang |
| Paper ID | `0accbb41-7037-4a3a-82a0-4464f878ed31` |

## Classification

- **Problem Type:** Federated learning for medical data sharing
- **Domain:** Cybersecurity
- **Sub-domain:** Federated Learning
- **Technique:** Heterogeneous Federated Learning with SM9 Threshold Identity Authentication
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a telemedicine data secure-sharing scheme utilizing heterogeneous federated learning to enhance medical data privacy and accessibility. Engineers should care because this approach addresses critical challenges in data sharing and privacy in telemedicine, especially in resource-constrained environments.

## Key Contribution

**A novel heterogeneous federated learning framework with model alignment and an SM9 threshold identity authentication scheme for secure telemedicine data sharing.**

## Problem

The need for secure and efficient sharing of telemedicine data among various healthcare providers while maintaining patient privacy.

## Method

**Approach:** The method involves a heterogeneous federated learning framework that aggregates local models from various healthcare institutions into a global model while ensuring data privacy through an SM9 threshold identity authentication scheme. This allows institutions with different resources to contribute effectively to the federated learning process.

**Algorithm:**

1. 1. Each healthcare institution trains its local model using its medical data.
2. 2. Local models are sent to the parameter server (PS) for aggregation.
3. 3. The PS performs global aggregation using a model alignment algorithm.
4. 4. The aggregated model is sent back to the institutions for further local training.
5. 5. The SM9 threshold signature algorithm is used to authenticate participants and secure data transmission.
6. 6. Repeat the process for multiple training rounds.

**Input:** Local medical data from participating healthcare institutions.

**Output:** A global model that incorporates knowledge from all local models while maintaining data privacy.

**Key Parameters:**

- `number_of_participants: variable`
- `local_training_rounds: variable`
- `threshold_for_SM9: variable`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** COVID-19 Radiography, Medical MNIST Database

**Results:**

- Performance cost: minimal
- Data heterogeneity resistance: effective

**Compared against:** Four representative works in heterogeneous federated learning

**Improvement:** The proposed scheme effectively resists the impact of data heterogeneity and resource constraints with almost no performance cost.

## Implementation Guide

**Data Structures:** Local model structures for each institution, Global model structure, Mapping matrix for model positions

**Dependencies:** Federated learning libraries, Cryptographic libraries for SM9

**Core Operation:**

```python
for each institution: local_train(data); send_model_to_PS(); PS.aggregate_models(); return global_model;
```

**Watch Out For:**

- Ensure proper implementation of the SM9 threshold signature to avoid unauthorized access.
- Monitor the communication channels to prevent eavesdropping attacks.
- Be aware of the resource constraints of participating institutions.

## Use This When

- You need to share medical data securely among multiple healthcare providers.
- You are working in a resource-constrained environment and need to implement federated learning.
- You require a solution that ensures patient data privacy during model training.

## Don't Use When

- You have a centralized data storage solution that does not require federated learning.
- The participating institutions have uniform data and resource capabilities.
- You need real-time data access without privacy concerns.

## Key Concepts

Federated Learning, Data Privacy, Threshold Signature, Model Aggregation, Telemedicine

## Connects To

- Federated Averaging (FedAvg)
- Heterogeneous Model Aggregation Techniques
- Threshold Cryptography
- Secure Multi-Party Computation

## Prerequisites

- Understanding of federated learning concepts
- Knowledge of cryptographic algorithms, specifically threshold signatures
- Familiarity with telemedicine data privacy regulations

## Limitations

- Performance may vary based on the heterogeneity of data across institutions.
- Requires a robust infrastructure for secure communication.
- Potentially high complexity in managing diverse model architectures.

## Open Questions

- How to further optimize the aggregation process for even larger datasets?
- What additional security measures can be implemented to enhance data protection?

## Abstract

A couple of months ago, <a href="https://www.tiktok.com/@jessicawetz6/video/7399423920828468485" target="_blank">a video</a> went viral on TikTok of a patient named Jessica explaining the lengths she has to go to just to get her various medical providers on the same page. Jessica carries a huge binder to her medical appointments, and from the sounds of it, that binder contains virtually every x-ray, procedure, medication, lab result, and exam they've ever had. It includes everything that any doctor who has seen them has ever documented, prescribed, ordered, or said about Jessica. Some people might watch that video and think: Why on earth is Jessica doing this? Why is this necessary? But for the millions of people who have watched and rewatched this video, for the numerous people in the comments who have asked Jessica how to structure their own patient binder, what information to include, and whether to use a cover page, Jessica really strikes a chord.
