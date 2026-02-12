# Evaluating and addressing demographic disparities in medical large language models: a systematic review

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s12939-025-02419-0` |
| Full Paper | [https://doi.org/10.1186/s12939-025-02419-0](https://doi.org/10.1186/s12939-025-02419-0) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/9c3a4973299038c66dfe7df6ee028018a55ace5e](https://www.semanticscholar.org/paper/9c3a4973299038c66dfe7df6ee028018a55ace5e) |
| Source | [https://journalclub.io/episodes/evaluating-and-addressing-demographic-disparities-in-medical-large-language-models-a-systematic-review](https://journalclub.io/episodes/evaluating-and-addressing-demographic-disparities-in-medical-large-language-models-a-systematic-review) |
| Source | [https://www.semanticscholar.org/paper/9c3a4973299038c66dfe7df6ee028018a55ace5e](https://www.semanticscholar.org/paper/9c3a4973299038c66dfe7df6ee028018a55ace5e) |
| Year | 2026 |
| Citations | 43 |
| Authors | Mahmud Omar, Vera Sorin, R. Agbareia, Donald U. Apakama, A. Soroush, A. Sakhuja |
| Paper ID | `63dcb385-a434-488c-ae20-b7984d027f05` |

## Classification

- **Problem Type:** bias detection in machine learning models
- **Domain:** Machine Learning & AI
- **Sub-domain:** Natural Language Processing
- **Technique:** Systematic Review of Bias in LLMs
- **Technique Category:** statistical_method
- **Type:** comparison

## Summary

This paper systematically reviews demographic biases in large language models (LLMs) used in healthcare, identifying prevalent bias types and evaluating mitigation strategies. Engineers should care because understanding and addressing these biases is crucial for developing fair AI systems that impact medical decision-making.

## Key Contribution

**The identification and analysis of demographic biases in medical LLMs, along with proposed mitigation strategies such as prompt engineering and debiasing algorithms.**

## Problem

The work is motivated by the need to understand how biases in LLMs can lead to unequal outcomes in clinical practice, particularly affecting underrepresented demographic groups.

## Method

**Approach:** The method involves a systematic review of existing literature on demographic biases in LLMs, focusing on studies that evaluate these biases in medical contexts. The review synthesizes findings on bias types, measurement methods, and mitigation strategies.

**Algorithm:**

1. 1. Define inclusion criteria for studies evaluating demographic biases in LLMs.
2. 2. Conduct a literature search across multiple databases from January 2018 to July 2024.
3. 3. Screen titles and abstracts for relevance using Rayyan software.
4. 4. Extract data from included studies regarding bias types and mitigation strategies.
5. 5. Assess the quality of studies using JBI Critical Appraisal Tools.
6. 6. Synthesize findings narratively and categorize by bias type and mitigation method.

**Input:** Peer-reviewed studies evaluating demographic biases in LLMs applied to medical tasks.

**Output:** A comprehensive overview of bias types, measurement methods, and mitigation strategies in medical LLMs.

**Key Parameters:**

- `search_date_range: January 2018 - July 2024`
- `included_studies: 24`
- `bias_types: gender, racial, ethnic, age, disability, socioeconomic`

**Complexity:** not stated

## Benchmarks

**Tested on:** Studies published between 2021 and 2024 from various countries including the USA, Germany, Netherlands, Spain, and Turkey.

**Results:**

- Bias detection rates: 91.7% of studies identified biases.
- Gender bias reported in 93.7% of studies focused on gender.
- Racial/ethnic bias observed in 90.9% of studies focused on race.

**Compared against:** Previous studies on bias in LLMs without systematic review.

**Improvement:** Mitigation strategies showed improved fairness, with 6 out of 7 studies reporting reduced disparities.

## Implementation Guide

**Data Structures:** Data extraction forms for systematic review., Quality assessment checklists.

**Dependencies:** Rayyan software for study screening., JBI Critical Appraisal Tools for quality assessment.

**Core Operation:**

```python
def systematic_review(): search_studies(); screen_titles(); extract_data(); assess_quality(); synthesize_results()
```

**Watch Out For:**

- Ensure comprehensive search strategy to avoid missing relevant studies.
- Be aware of potential publication bias affecting the results.
- Consider the context of bias when interpreting findings.

## Use This When

- Developing AI applications in healthcare that utilize LLMs.
- Evaluating existing LLMs for bias before deployment in clinical settings.
- Implementing mitigation strategies to reduce bias in AI outputs.

## Don't Use When

- Working with LLMs in non-medical domains where bias is less critical.
- When the application context does not involve demographic considerations.

## Key Concepts

demographic bias, large language models, mitigation strategies, prompt engineering, debiasing algorithms, systematic review, healthcare applications

## Connects To

- Bias detection algorithms
- Fairness in AI
- Ethical AI development
- Prompt engineering techniques
- Debiasing methods in NLP

## Prerequisites

- Understanding of machine learning and NLP concepts.
- Familiarity with systematic review methodologies.
- Knowledge of bias and fairness in AI.

## Limitations

- Limited to peer-reviewed studies, potentially excluding relevant grey literature.
- Focus on specific demographic factors may overlook intersectional biases.
- Mitigation strategies are still developing and may not be universally effective.

## Open Questions

- How can bias mitigation strategies be standardized across different LLM applications?
- What are the long-term impacts of bias in LLMs on healthcare outcomes?

## Abstract

On today’s episode we are going to talk about bias in Large Language Models (LLMs) used in medicine. In this paper, the authors conducted a systematic review of LLMs to see if they contained biases and which were most prevalent. We will first briefly talk about how these LLMs are being used in medicine and what seems promising about them. Next, we will dive into what human bias in medicine is, and how it can manifest in a Machine Learning model. We will then explore how the authors used the PRISMA guidelines and JBI Critical Appraisal Tools, and what they found. Last, we will mention some mitigation tools that can help reduce bias in AI. It seems like everywhere you look there is a new AI tool promising to make your life better and easier. It’s no different for healthcare professionals. Healthcare systems tend to be low on resources, with overworked doctors and nurses being the norm. In terms of time, well, speeding up
