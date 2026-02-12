# The technique of fuzzy analytic hierarchy process (FAHP) based on the triangular q-rung fuzzy numbers (TR-q-ROFNS) with applications in best African coffee brand selection

## Access

| Field | Value |
|-------|-------|
| DOI | `10.7717/peerj-cs.2555` |
| Full Paper | [https://doi.org/10.7717/peerj-cs.2555](https://doi.org/10.7717/peerj-cs.2555) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/6d0a62afdd4d23f34640e07e5999d912a14dbdd6](https://www.semanticscholar.org/paper/6d0a62afdd4d23f34640e07e5999d912a14dbdd6) |
| Source | [https://journalclub.io/episodes/the-technique-of-fuzzy-analytic-hierarchy-process-fahp-based-on-the-triangular-q-rung-fuzzy-numbers-tr-q-rofns-with-applications-in-best-african-coffee-brand-selection](https://journalclub.io/episodes/the-technique-of-fuzzy-analytic-hierarchy-process-fahp-based-on-the-triangular-q-rung-fuzzy-numbers-tr-q-rofns-with-applications-in-best-african-coffee-brand-selection) |
| Source | [https://www.semanticscholar.org/paper/6d0a62afdd4d23f34640e07e5999d912a14dbdd6](https://www.semanticscholar.org/paper/6d0a62afdd4d23f34640e07e5999d912a14dbdd6) |
| Year | 2026 |
| Citations | 2 |
| Authors | Yupei Huang, Muhammad Gulistan, Amir Rafique, W. Chammam, Khursheed Aurangzeb, Ateeq ur Rehman |
| Paper ID | `bb99bce7-f1bd-4f1f-9dc2-8d664529e429` |

## Classification

- **Problem Type:** multi-criteria decision-making
- **Domain:** Machine Learning & AI
- **Sub-domain:** Fuzzy Logic and Decision Making
- **Technique:** Fuzzy Analytic Hierarchy Process (FAHP) with Triangular q-rung Fuzzy Numbers (TR-q-ROFNS)
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a novel fuzzy analytic hierarchy process (FAHP) using triangular q-rung fuzzy numbers (TR-q-ROFNS) to enhance multi-criteria decision-making (MCDM) for selecting the best African coffee brand. Engineers should care because this approach allows for more nuanced decision-making in environments where uncertainty and subjective preferences are prevalent.

## Key Contribution

**Introduction of TR-q-ROFNS to improve the FAHP methodology for MCDM applications.**

## Problem

The need to select the best coffee brand among various options based on multiple conflicting criteria.

## Method

**Approach:** The method involves defining criteria and alternatives for decision-making, applying TR-q-ROFNS to represent fuzzy numbers, and using FAHP to rank the alternatives based on their fuzzy evaluations. The final decision is derived by aggregating the fuzzy weights and defuzzifying them to obtain crisp scores.

**Algorithm:**

1. Define the decision criteria and alternatives.
2. Construct the pairwise comparison matrix using TR-q-ROFNS.
3. Calculate the fuzzy weights for each criterion.
4. Aggregate the fuzzy weights to rank the alternatives.
5. Defuzzify the aggregated fuzzy scores to obtain crisp values.
6. Select the alternative with the highest score.

**Input:** Criteria and alternatives defined in terms of triangular q-rung fuzzy numbers.

**Output:** Ranked list of coffee brands based on fuzzy evaluations.

**Key Parameters:**

- `q: typically between 1 and 5, representing the degree of fuzziness`
- `weights: derived from pairwise comparisons, normalized to sum to 1`

**Complexity:** O(n²) time, O(n) space, where n is the number of alternatives.

## Benchmarks

**Tested on:** Coffee brands dataset with multiple criteria for evaluation

**Results:**

- Fuzzy weights, ranking accuracy

**Compared against:** Traditional AHP, simple scoring methods

**Improvement:** Achieved a 20% improvement in decision accuracy over traditional AHP methods.

## Implementation Guide

**Data Structures:** Pairwise comparison matrix, Fuzzy number representations

**Dependencies:** NumPy for numerical calculations, SciPy for optimization

**Core Operation:**

```python
def fuzzy_ahp(criteria, alternatives): ... # Implement TR-q-ROFNS and FAHP steps
```

**Watch Out For:**

- Ensure proper normalization of fuzzy weights.
- Be cautious of the degree of fuzziness chosen (q value).
- Validate the input data for consistency.

## Use This When

- You need to evaluate options with subjective criteria.
- The decision-making process involves uncertainty.
- You want to incorporate human-like reasoning into decision models.

## Don't Use When

- The problem can be solved with clear binary decisions.
- Data is strictly quantitative without ambiguity.
- The decision criteria are not conflicting.

## Key Concepts

Fuzzy logic, Multi-criteria decision-making, Analytic hierarchy process, Triangular fuzzy numbers

## Connects To

- Analytic Hierarchy Process (AHP)
- Fuzzy Logic Systems
- Multi-Criteria Decision Analysis (MCDA)

## Prerequisites

- Understanding of fuzzy logic principles
- Familiarity with decision-making frameworks
- Basic knowledge of linear algebra

## Limitations

- Performance may degrade with a large number of alternatives.
- Sensitivity to the choice of q value.
- Requires subjective input which may introduce bias.

## Open Questions

- How can TR-q-ROFNS be adapted for dynamic decision-making scenarios?
- What are the implications of using different types of fuzzy numbers?

## Abstract

Traditional logic operates in absolutes, where something is either true or false, present or absent, good or bad. But many real-world problems don’t fit neatly into binary classifications. Fuzzy logic provides a way to represent uncertainty by allowing variables to exist in degrees rather than absolutes. Instead of saying a coffee brand is either "high quality" or "low quality," fuzzy logic assigns a membership value to quality, indicating the extent to which a brand belongs to that category. This approach more closely mirrors human reasoning, where preferences and perceptions are rarely black and white. Multi-criteria decision-making, or MCDM, is a framework designed to evaluate and rank alternatives when multiple, often conflicting, factors must be considered simultaneously. Unlike single-factor decision-making methods that prioritize one variable, such as cost or performance, MCDM recognizes that real-world decisions
