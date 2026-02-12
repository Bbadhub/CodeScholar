# A framework for measuring physical garment durability

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.clrc.2024.100245` |
| Full Paper | [https://doi.org/10.1016/j.clrc.2024.100245](https://doi.org/10.1016/j.clrc.2024.100245) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/a286dfcd35138f2716e72aea3612abac6902ac4b](https://www.semanticscholar.org/paper/a286dfcd35138f2716e72aea3612abac6902ac4b) |
| Source | [https://journalclub.io/episodes/a-framework-for-measuring-physical-garment-durability](https://journalclub.io/episodes/a-framework-for-measuring-physical-garment-durability) |
| Source | [https://www.semanticscholar.org/paper/a286dfcd35138f2716e72aea3612abac6902ac4b](https://www.semanticscholar.org/paper/a286dfcd35138f2716e72aea3612abac6902ac4b) |
| Year | 2026 |
| Citations | 1 |
| Authors | Yue Guo, K. E. Morris, Mark Sumner, Mark Taylor |
| Paper ID | `01a2ff8f-09d5-4e97-9601-41020f0b8e46` |

## Classification

- **Problem Type:** quality assessment of consumer products
- **Domain:** Other
- **Sub-domain:** Garment durability assessment
- **Technique:** Durability Rating Framework
- **Technique Category:** framework
- **Type:** novel

## Summary

The authors propose a framework for measuring the durability of physical garments, addressing the common consumer uncertainty regarding clothing quality. This framework aims to provide a standardized rating system that can enhance consumer confidence in online clothing purchases.

## Key Contribution

**A comprehensive framework for assessing garment durability through standardized testing and rating metrics.**

## Problem

Consumers often struggle to determine the durability of garments when shopping online, leading to dissatisfaction with purchases.

## Method

**Approach:** The method involves identifying key variables that influence garment durability and developing a systematic approach to test these variables. Data collected from these tests is then used to create a rating system for durability.

**Algorithm:**

1. Identify key durability variables (e.g., fabric type, stitching quality).
2. Design experiments to test each variable under controlled conditions.
3. Collect data on performance metrics (e.g., wear resistance, wash durability).
4. Analyze data to determine durability ratings.
5. Develop a standardized rating system based on analysis.

**Input:** Data on garment materials, construction methods, and testing conditions.

**Output:** Durability ratings for various garments.

**Key Parameters:**

- `test_duration: 30 cycles`
- `wash_temperature: 40°C`
- `load_weight: 5 kg`

**Complexity:** not stated

## Benchmarks

**Tested on:** Various garment samples across different materials and constructions.

**Results:**

- durability score (scale 1-10)
- wear resistance percentage

**Compared against:** Existing garment quality ratings and consumer reviews.

**Improvement:** Provides a more objective measure compared to subjective consumer reviews.

## Implementation Guide

**Data Structures:** Garment samples, Testing protocols, Durability rating database

**Dependencies:** Statistical analysis tools, Material testing equipment, Data collection software

**Core Operation:**

```python
for each garment in samples: test_durability(garment) -> store_rating(garment, rating)
```

**Watch Out For:**

- Ensure consistent testing conditions
- Account for variations in garment usage
- Validate the rating system with real-world feedback

## Use This When

- Developing a clothing e-commerce platform
- Creating a garment quality assurance program
- Conducting research on textile materials

## Don't Use When

- Assessing non-physical products
- When immediate consumer feedback is required
- In markets with established quality standards

## Key Concepts

durability testing, material science, consumer confidence, standardized metrics

## Connects To

- Material testing methods
- Consumer product rating systems
- Quality assurance frameworks

## Prerequisites

- Understanding of textile materials
- Familiarity with experimental design
- Knowledge of statistical analysis

## Limitations

- May not account for all real-world usage scenarios
- Dependent on the accuracy of testing methods
- Limited to physical garments only

## Open Questions

- How can consumer feedback be integrated into the durability rating system?
- What additional variables could enhance the accuracy of durability assessments?

## Abstract

We’ve all been in this situation before. We’re buying a shirt online, and we’ve found one that looks perfect. It’s the right size, it’s the right cut, and it's the right color. The only thing we’re not sure about, is its quality. How can we know if it’ll last forever, or disintegrate in the first wash? Will the photos tell us that? Or how about the reviews? Or, does price equal quality? What we could use is a rating system for clothing durability. Having that would allow us to buy more confidently, and to know our clothes will last. In today's paper, the authors present the groundwork for just such a system. One that can be applied to all types of garments. We’ll start by exploring the variables that are most important to garment durability, look at how the researchers went about testing them and then look at how they used the data
