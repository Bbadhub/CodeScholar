# Study of Code Smells: A Review and Research Agenda

## Access

| Field | Value |
|-------|-------|
| DOI | `10.33889/IJMEMS.2024.9.3.025` |
| Full Paper | [https://doi.org/10.33889/IJMEMS.2024.9.3.025](https://doi.org/10.33889/IJMEMS.2024.9.3.025) |
| Source | [https://journalclub.io/episodes/study-of-code-smells-a-review-and-research-agenda](https://journalclub.io/episodes/study-of-code-smells-a-review-and-research-agenda) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `60a9c9c5-41f5-4460-a6b2-e15ab98321f3` |

## Classification

- **Problem Type:** Code smell detection
- **Domain:** Software Engineering
- **Sub-domain:** Code Quality Analysis
- **Technique:** Random Forest, JRip
- **Technique Category:** machine_learning_algorithm
- **Type:** comparison

## Summary

This paper reviews the landscape of code smells, categorizing them and analyzing various detection tools and algorithms used in the literature from 2009 to 2022. It highlights the prevalence of certain smells and the effectiveness of machine learning techniques in detecting them, which is crucial for software engineers aiming to improve code quality and maintainability.

## Key Contribution

**A comprehensive review of code smells and the effectiveness of detection techniques, particularly machine learning algorithms.**

## Problem

Code smells are design defects that degrade software quality without causing immediate failures, leading to increased maintenance costs.

## Method

**Approach:** The method involves a systematic literature review of studies on code smells, categorizing them into machine learning and non-machine learning techniques. It analyzes the effectiveness of various algorithms and tools used for detection.

**Algorithm:**

1. 1. Conduct a literature search on code smells from recognized databases.
2. 2. Filter studies based on inclusion and exclusion criteria.
3. 3. Assess the quality of selected studies using a scoring system.
4. 4. Categorize the studies into machine learning and non-machine learning techniques.
5. 5. Analyze the effectiveness of different algorithms and tools.
6. 6. Summarize findings and identify gaps for future research.

**Input:** Research studies on code smells published between 2009 and 2022.

**Output:** A categorized summary of code smells, detection techniques, and their effectiveness.

**Key Parameters:**

- `quality_score_threshold: 5`
- `study_period: 2009-2022`

**Complexity:** not stated

## Benchmarks

**Tested on:** Various datasets used in the studies reviewed, primarily focusing on Java code.

**Results:**

- Detection accuracy, precision, recall, F1-score for machine learning techniques.

**Compared against:** Previous studies on code smell detection using heuristic or metric strategies.

**Improvement:** Machine learning techniques showed improved detection capabilities compared to traditional methods, but specific percentage improvements were not stated.

## Implementation Guide

**Data Structures:** Data structures for storing code metrics and smell classifications.

**Dependencies:** Machine learning libraries (e.g., scikit-learn for Random Forest), code analysis tools (e.g., SonarQube).

**Core Operation:**

```python
for each file in codebase: detect_smells(file) -> report_smells(file)
```

**Watch Out For:**

- Ensure the quality of the dataset used for training machine learning models.
- Be aware of the limitations of detection tools and their context of use.

## Use This When

- You need to identify and refactor code smells in a large codebase.
- You are developing or enhancing tools for code quality analysis.
- You want to apply machine learning techniques to software engineering problems.

## Don't Use When

- The codebase is small and manageable without automated tools.
- You are working in a domain where code smells are not applicable.

## Key Concepts

Code smells, Machine learning, Refactoring, Technical debt, Software maintainability, Detection tools, Empirical studies

## Connects To

- Static code analysis tools
- Refactoring techniques
- Software quality metrics

## Prerequisites

- Understanding of software design principles.
- Familiarity with machine learning concepts.
- Knowledge of code quality metrics.

## Limitations

- The review may not cover all recent studies beyond 2022.
- Machine learning techniques require quality datasets for effective training.
- Detection tools may have varying effectiveness based on the programming language.

## Open Questions

- What are the long-term impacts of code smells on software maintainability?
- How can machine learning techniques be further improved for better detection of code smells?

## Abstract

Bucket 1 is the Bloaters. These arise when something in your codebase has grown too large to handle gracefully. These smells don’t immediately break your system but instead slowly erode its maintainability. Examples include the “Long Method”, where a single function becomes a sprawling labyrinth of logic. And the “Large Class”, which is stuffed with so many responsibilities it’s hard to tell what its primary purpose is. Another classic bloater is the “Long Parameter List”, which is a sign of poor abstraction, and requires the caller to juggle too many pieces of data at once. Left unchecked, bloaters bog down your code, making it harder to navigate, extend, or debug. Bucket 2, the Object-Orientation Abusers, is all about misusing or misunderstanding fundamental principles of OOP. This bucket includes
