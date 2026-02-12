# Skyline query under multidimensional incomplete data based on classification tree

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s40537-024-00923-8` |
| Full Paper | [https://doi.org/10.1186/s40537-024-00923-8](https://doi.org/10.1186/s40537-024-00923-8) |
| Source | [https://journalclub.io/episodes/skyline-query-under-multidimensional-incomplete-data-based-on-classification-tree](https://journalclub.io/episodes/skyline-query-under-multidimensional-incomplete-data-based-on-classification-tree) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `4737c4b3-00b6-4949-933c-534a0120950b` |

## Classification

- **Problem Type:** skyline query on incomplete data
- **Domain:** Data Structures & Algorithms
- **Sub-domain:** Skyline queries, Classification trees
- **Technique:** Incomplete Data Weighted Classification Tree
- **Technique Category:** data_structure
- **Type:** novel

## Summary

The paper presents a method for executing skyline queries on multidimensional incomplete data using a classification tree, addressing inefficiencies in existing approaches. Engineers should care because this method improves query efficiency and accuracy by effectively handling missing data.

## Key Contribution

**Introduction of an incomplete data weighted classification tree and optimal virtual points for efficient skyline queries on incomplete data.**

## Problem

The prevalence of incomplete data in practical scenarios necessitates efficient skyline queries that can handle missing values without compromising performance.

## Method

**Approach:** The method involves constructing an incomplete data weighted classification tree that classifies tuples based on the presence or absence of attributes. Once classified, skyline queries are executed using optimal virtual points to minimize comparisons.

**Algorithm:**

1. 1. Select a training set from the incomplete dataset (70% of the data).
2. 2. Construct the incomplete data weighted classification tree by inserting tuples into the root node.
3. 3. For each dimension, assign weights based on missing values (0 for missing, 1 for present).
4. 4. Store dimension values in intermediate nodes and classify data into leaf nodes.
5. 5. Use horizontal indexing to export classified data into buckets.
6. 6. Execute skyline queries using optimal virtual points to filter out unnecessary comparisons.

**Input:** Multidimensional incomplete dataset O = {o1, o2, ..., on}, where each oi may have missing values.

**Output:** Classified tuples in buckets and the result of the skyline query.

**Key Parameters:**

- `training_set_size: 70% of the dataset`
- `weight_for_missing: 0`
- `weight_for_present: 1`

**Complexity:** O(2^d * n + d * 2^d log n) for tree construction, O(2^d * m + 3d * 2^d log m) for classification.

## Benchmarks

**Tested on:** Multidimensional incomplete datasets with various missing patterns.

**Results:**

- Query efficiency and accuracy of skyline results.

**Compared against:** Existing skyline query algorithms on complete data.

**Improvement:** Significant reduction in the number of comparisons and improved query efficiency.

## Implementation Guide

**Data Structures:** Incomplete data weighted classification tree, Buckets for classified data

**Dependencies:** Data processing libraries (e.g., NumPy, Pandas) for handling datasets

**Core Operation:**

```python
for each tuple in dataset: insert into classification_tree; classify based on weights; execute skyline_query using optimal_virtual_points.
```

**Watch Out For:**

- Ensure the training set is representative of the entire dataset to avoid bias.
- Carefully manage memory usage when handling large datasets.
- Optimize the horizontal indexing to improve retrieval times.

## Use This When

- Handling large datasets with significant missing values.
- Performing skyline queries in data mining applications.
- Optimizing query performance in geographic information systems.

## Don't Use When

- Working with complete datasets where missing data is not an issue.
- When real-time query performance is critical and cannot tolerate classification delays.
- In scenarios where data is highly dynamic and frequently changing.

## Key Concepts

Skyline queries, Incomplete data, Classification trees, Optimal virtual points, Data redundancy, Multi-objective optimization

## Connects To

- Decision trees
- Random forests
- Multi-objective optimization techniques
- Data imputation methods

## Prerequisites

- Understanding of skyline queries
- Familiarity with classification algorithms
- Knowledge of data structures

## Limitations

- Performance may degrade with extremely high-dimensional data.
- The method assumes a fixed percentage of missing data, which may not generalize well.
- Classification tree construction can be time-consuming for very large datasets.

## Open Questions

- How can the method be adapted for real-time data streams?
- What are the implications of varying missing data patterns on query performance?

## Abstract

The process begins by inserting each tuple into the tree. The root node contains all data tuples, and from there, branching occurs based on the presence or absence of attributes. Intermediate nodes store weight-based decisions rather than attribute values, ensuring that tuples with missing values are assigned correctly. The tree grows downward, with leaf nodes representing fully classified groups of tuples that share identical missingness patterns. Once classification is complete, the tree’s indexing mechanism ensures that data can be efficiently retrieved and processed. Since each leaf node corresponds to a distinct missing data pattern, skyline queries can be executed within each bucket separately, minimizing unnecessary dominance comparisons across tuples with incompatible attribute sets. One of the other key innovations here is the introduction of Optimal Virtual Points
