# Encrypted Search Method for Cloud Computing Data Under Attack Based on TF-IDF and Apriori Algorithm

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1080/08839514.2024.2449303` |
| Full Paper | [https://doi.org/10.1080/08839514.2024.2449303](https://doi.org/10.1080/08839514.2024.2449303) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/b6829996c53214fcd3f4cf349b3438eda9b5db00](https://www.semanticscholar.org/paper/b6829996c53214fcd3f4cf349b3438eda9b5db00) |
| Source | [https://journalclub.io/episodes/encrypted-search-method-for-cloud-computing-data-under-attack-based-on-tf-idf-and-apriori-algorithm](https://journalclub.io/episodes/encrypted-search-method-for-cloud-computing-data-under-attack-based-on-tf-idf-and-apriori-algorithm) |
| Source | [https://www.semanticscholar.org/paper/b6829996c53214fcd3f4cf349b3438eda9b5db00](https://www.semanticscholar.org/paper/b6829996c53214fcd3f4cf349b3438eda9b5db00) |
| Year | 2026 |
| Citations | 0 |
| Authors | Demei Mao, Mingzhu Wang |
| Paper ID | `5f984071-711c-4a8b-8c17-90576e1cdd43` |

## Classification

- **Problem Type:** encrypted search in cloud computing
- **Domain:** Cybersecurity
- **Sub-domain:** Encrypted search methods
- **Technique:** Hybrid Encrypted Search Framework
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a hybrid encrypted search framework that integrates an improved TF-IDF weighting scheme with semantic keyword expansion via the Apriori algorithm. Engineers should care because this approach allows for secure, ranked multi-keyword searches in cloud environments while maintaining data confidentiality.

## Key Contribution

**A novel hybrid framework for encrypted search that combines TF-IDF and Apriori for enhanced search capabilities in cloud computing.**

## Problem

The need for secure and efficient multi-keyword search methods in cloud environments where data confidentiality is critical.

## Method

**Approach:** The method utilizes an improved TF-IDF weighting scheme to rank keywords while employing the Apriori algorithm for semantic keyword expansion. This combination allows for efficient multi-keyword searches without decrypting the data, ensuring confidentiality and high recall.

**Algorithm:**

1. 1. Input encrypted data and keywords.
2. 2. Apply TF-IDF weighting to the keywords.
3. 3. Use the Apriori algorithm to expand keywords semantically.
4. 4. Generate obscured keyword indices to resist attacks.
5. 5. Perform the search on the encrypted data using the obscured indices.
6. 6. Return ranked results based on the TF-IDF scores.

**Input:** Encrypted data and a set of keywords.

**Output:** Ranked list of search results based on the input keywords.

**Key Parameters:**

- `tfidf_weighting_scheme: improved version`
- `apriori_min_support: 0.5`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Synthetic datasets simulating cloud storage scenarios.

**Results:**

- Recall: high
- Precision: high
- Search time: efficient

**Compared against:** Standard TF-IDF search methods, Existing encrypted search frameworks

**Improvement:** Significant improvement in recall and efficiency compared to baseline methods.

## Implementation Guide

**Data Structures:** Encrypted data structures, Keyword index structures

**Dependencies:** Cryptography libraries, Data processing frameworks

**Core Operation:**

```python
results = search(encrypted_data, keywords) using TF-IDF and Apriori
```

**Watch Out For:**

- Ensure proper handling of encrypted data formats.
- Be cautious of the computational overhead introduced by encryption.
- Test the system thoroughly to validate search accuracy.

## Use This When

- You need to perform secure searches on sensitive data in the cloud.
- High recall in search results is a priority.
- You want to maintain data confidentiality while allowing multi-keyword searches.

## Don't Use When

- The search does not require encryption.
- Performance is more critical than security.
- The dataset is small and can be handled without encryption.

## Key Concepts

TF-IDF, Apriori algorithm, encrypted search, semantic expansion

## Connects To

- TF-IDF
- Apriori algorithm
- Homomorphic encryption
- Secure multi-party computation

## Prerequisites

- Understanding of encryption techniques
- Familiarity with TF-IDF
- Knowledge of data mining algorithms

## Limitations

- Performance may degrade with very large datasets.
- Complexity of keyword expansion may increase search time.
- Requires careful tuning of parameters for optimal results.

## Open Questions

- How can the framework be adapted for dynamic datasets?
- What are the implications of different encryption methods on search efficiency?

## Abstract

The authors propose a hybrid encrypted search framework that combines an improved TF-IDF weighting scheme with semantic keyword expansion using the Apriori algorithm. They introduce two methods, MKSE and SEMSS, that not only preserve data confidentiality in the cloud but also enable ranked, multi-keyword search with high recall and efficient performance. On today’s episode, we’ll walk through the core architecture of these methods, examine how they obscure keyword indices to resist attacks, and explore how semantic expansion boosts search completeness, without ever decrypting the data.
