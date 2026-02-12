# Location Privacy Protection for the Internet of Things with Edge Computing Based on Clustering K-Anonymity

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/s24186153` |
| Full Paper | [https://doi.org/10.3390/s24186153](https://doi.org/10.3390/s24186153) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/c83b3c8953d28c6d461295108e552ac16c592171](https://www.semanticscholar.org/paper/c83b3c8953d28c6d461295108e552ac16c592171) |
| Source | [https://journalclub.io/episodes/location-privacy-protection-for-the-internet-of-things-with-edge-computing-based-on-clustering-k-anonymity](https://journalclub.io/episodes/location-privacy-protection-for-the-internet-of-things-with-edge-computing-based-on-clustering-k-anonymity) |
| Source | [https://www.semanticscholar.org/paper/c83b3c8953d28c6d461295108e552ac16c592171](https://www.semanticscholar.org/paper/c83b3c8953d28c6d461295108e552ac16c592171) |
| Year | 2026 |
| Citations | 2 |
| Authors | Nanlan Jiang, Yinan Zhai, Yujun Wang, Xuesong Yin, Sai Yang, Pingping Xu |
| Paper ID | `18aba8c5-6774-46aa-afe4-6b6cea3fee45` |

## Classification

- **Problem Type:** location privacy protection
- **Domain:** Cybersecurity
- **Sub-domain:** Location Privacy Protection
- **Technique:** Clustering K-anonymity Algorithm (CKA)
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

The paper presents a novel Clustering K-anonymity Algorithm (CKA) designed to enhance location privacy protection for IoT devices utilizing edge computing. This approach is significant for engineers as it addresses vulnerabilities in traditional K-anonymity methods, particularly against narrow-region attacks, by effectively obscuring user locations through clustering and the use of virtual nodes.

## Key Contribution

**Introduction of the Clustering K-anonymity Algorithm (CKA) that improves location privacy security in IoT environments with edge computing.**

## Problem

The increasing number of IoT devices and their sensitive location data necessitates robust privacy protection mechanisms during communication processes.

## Method

**Approach:** CKA utilizes clustering to enhance location privacy by dividing the communication region into zones and incorporating both real and virtual locations in requests. This method confuses eavesdroppers and improves the probability of successful information transmission.

**Algorithm:**

1. Monitor broadcasts from head nodes to determine if the node should act as a normal node or head node.
2. If acting as a head node, divide the surrounding region into N zones and form clusters.
3. Include at least one real or virtual location from each cluster in the request to the service provider.
4. Generate virtual nodes if the number of real nodes in a cluster is below a threshold.
5. Broadcast the confirmation with all selected locations and send the request to the service provider.

**Input:** Parameters K (degree of anonymity), N (number of clusters), γ (weight parameter), and τ (time interval).

**Output:** Responses from normal nodes, confirmation, and service requests sent to the service provider.

**Key Parameters:**

- `K: degree of anonymity (e.g., K = 8)`
- `N: number of clusters (e.g., N = 4)`
- `γ: weight parameter (e.g., γ = 1.5)`
- `τ: time interval`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Simulated environment in a 100 m × 100 m region with various node densities.

**Results:**

- Eavesdropping probability, successful information transmission probability.

**Compared against:** Traditional K-anonymity algorithms.

**Improvement:** CKA significantly reduces the probability of eavesdroppers revealing location information compared to traditional methods.

## Implementation Guide

**Data Structures:** Clusters of nodes, virtual nodes, communication requests.

**Dependencies:** MATLAB for simulation and performance evaluation.

**Core Operation:**

```python
if lτ = 0 then broadcast notice; for each zone i do generate virtual nodes if needed; send request to service provider.
```

**Watch Out For:**

- Ensure the number of real nodes does not exceed the defined limits.
- Monitor the communication range to maintain privacy effectively.
- Adjust parameters N and γ to balance security and efficiency.

## Use This When

- Building IoT applications that require location-based services with privacy considerations.
- Developing systems that need to protect sensitive location data from potential eavesdroppers.
- Implementing edge computing solutions where location privacy is a concern.

## Don't Use When

- The application does not involve sensitive location data.
- Low latency is critical and cannot be compromised for privacy.
- The system architecture does not support clustering or edge computing.

## Key Concepts

K-anonymity, clustering, location-based services, edge computing, virtual nodes, eavesdropping attacks

## Connects To

- K-anonymity algorithms
- Differential privacy
- Location-based services
- Edge computing frameworks

## Prerequisites

- Understanding of K-anonymity
- Familiarity with clustering techniques
- Knowledge of IoT architecture

## Limitations

- Performance may degrade with a high number of clusters if not managed properly.
- The algorithm's effectiveness is dependent on the density of nodes in the region.
- Virtual nodes may introduce overhead in communication efficiency.

## Open Questions

- How to optimize the clustering process for dynamic environments?
- What are the implications of varying node densities on privacy protection?

## Abstract

The past decade has seen nothing short of a revolution in privacy protection. From GDPR in Europe to CCPA in California, to third-party cookie restrictions built into iOS, and stronger browser defaults around HTTPS. Compared to the wild-west days of the early and mid-2000s, the internet consumer today has far more protections and avenues for recourse than ever before. The operators of web applications, mobile apps, APIs, newsletters, and other internet services are governed by strict compliance regimes that dictate what they can and can’t do with your personal information. Importantly, these regimes also specify how they must care for, handle, and protect your personal data—securing it from bad actors, encrypting it, and ensuring its safety.
