# The JavaScript Package Selection Task: A Comparative Experiment Using an LLM-based Approach

## Access

| Field | Value |
|-------|-------|
| DOI | `10.19153/cleiej.27.2.4` |
| Full Paper | [https://doi.org/10.19153/cleiej.27.2.4](https://doi.org/10.19153/cleiej.27.2.4) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/dda6cccf266c5e0043720fd6f360ba102853044f](https://www.semanticscholar.org/paper/dda6cccf266c5e0043720fd6f360ba102853044f) |
| Source | [https://journalclub.io/episodes/the-javascript-package-selection-task-a-comparative-experiment-using-an-llm-based-approach](https://journalclub.io/episodes/the-javascript-package-selection-task-a-comparative-experiment-using-an-llm-based-approach) |
| Source | [https://www.semanticscholar.org/paper/dda6cccf266c5e0043720fd6f360ba102853044f](https://www.semanticscholar.org/paper/dda6cccf266c5e0043720fd6f360ba102853044f) |
| Year | 2026 |
| Citations | 4 |
| Authors | J. A. D. Pace, Antonela Tommasel, H. Vázquez |
| Paper ID | `d9b29852-b241-4c3a-8a73-279ddf2c4a7b` |

## Classification

- **Problem Type:** package selection
- **Domain:** Software Engineering
- **Sub-domain:** Recommender Systems
- **Technique:** Retrieval Augmented Generation (RAG)
- **Technique Category:** framework
- **Type:** novel

## Summary

This paper presents a Retrieval Augmented Generation (RAG) architecture that enhances the AIDT recommender system for selecting JavaScript packages. It combines machine learning techniques with large language models (LLMs) to improve the relevance and explainability of package recommendations, addressing the challenges developers face in package selection.

## Key Contribution

**The introduction of a RAG architecture that integrates LLMs for improved package selection and explanation capabilities.**

## Problem

Developers struggle to find relevant JavaScript packages due to ineffective search results from package managers and search engines.

## Method

**Approach:** The RAG architecture retrieves relevant JavaScript packages based on a developer's query and re-ranks them using an LLM. It combines results from multiple sources and provides explanations for the recommendations.

**Algorithm:**

1. 1. Receive a developer's query.
2. 2. Perform semantic search on a knowledge repository to retrieve candidate packages.
3. 3. Re-rank the retrieved packages using a learning-to-rank model.
4. 4. Generate an enriched prompt for the LLM with the top-k packages.
5. 5. Synthesize a response using the LLM.

**Input:** A natural language query expressing a technology need.

**Output:** A ranked list of recommended JavaScript packages with explanations.

**Key Parameters:**

- `top_k: 5`
- `embedding_dimension: 768`
- `learning_rate: 0.001`

**Complexity:** O(n log n) time for ranking, O(n) space.

## Benchmarks

**Tested on:** 4600 curated JavaScript packages from GitHub

**Results:**

- precision: 20% improvement over NPM
- MAP: not stated
- nDCG: not stated

**Compared against:** AIDT, human rankings

**Improvement:** RAG achieved performance comparable to AIDT with better explainability.

## Implementation Guide

**Data Structures:** Knowledge repository for JavaScript packages, Ranking model for package features

**Dependencies:** Transformers library for LLMs, Semantic search library

**Core Operation:**

```python
results = RAG(query); return results
```

**Watch Out For:**

- Ensure the knowledge repository is up-to-date.
- Be cautious of LLM hallucinations in package recommendations.
- Fine-tune the learning-to-rank model for best results.

## Use This When

- You need to recommend JavaScript packages based on developer queries.
- You want to improve the explainability of package recommendations.
- You are facing challenges with traditional search engines returning irrelevant results.

## Don't Use When

- The task requires real-time package recommendations without any prior data.
- You have a very small dataset of packages to work with.
- The application context is not related to JavaScript.

## Key Concepts

RAG architecture, LLM integration, semantic search, learning-to-rank, explainable recommendations

## Connects To

- AIDT
- ChatGPT
- Cohere
- Llama2
- learning-to-rank algorithms

## Prerequisites

- Understanding of recommender systems
- Familiarity with LLMs
- Knowledge of JavaScript package ecosystem

## Limitations

- RAG performance may vary with different LLMs
- Dependency on the quality of the knowledge repository
- Potential for LLMs to produce irrelevant recommendations

## Open Questions

- How can RAG be further optimized for real-time applications?
- What additional features can improve the ranking accuracy?

## Abstract

NPM is a fantastic package manager in a number of ways, but it's really bad at search. To be fair, every other package manager is bad at it too: PIP, Crates, Maven, Homebrew, RPM, etc. They all struggle to give meaningful search-results for a query. When you have a problem that you need a library to solve, your chances of finding a relevant package might hinge on your ability to guess what that package might be named. The search-bar in NPM returns such irrelevant results, that you'll likely spend your day jumping from search engines, to Github, to blog posts, to youtube videos, to forum discussions. You'll go back and forth to NPM over and over again, trying out different packages to see what fits. You'll spend time reading their docs, checking their Github issues, checking if they're stable, well maintained and recently updated. It’s a pain, to say the least. I’ve always thought that non-programmers would be shocked to see how much of a Software Engineers day is spent trying to find and use new packages. Out of exasperation, many developers just choose the most popular package that seems like it might possibly do the job. Not the package best suited to the problem, not the package with highest test coverage, not the package with the best documentation, or the lowest number of open issues, just the one with the most impressive download graph.
