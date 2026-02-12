# Bioethanol production from concentration fruit wastes juice using bakery yeast

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1007/s40243-024-00283-6` |
| Full Paper | [https://doi.org/10.1007/s40243-024-00283-6](https://doi.org/10.1007/s40243-024-00283-6) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/061ea1ab6414e986337699b80cbe2396c9bbe556](https://www.semanticscholar.org/paper/061ea1ab6414e986337699b80cbe2396c9bbe556) |
| Source | [https://journalclub.io/episodes/bioethanol-production-from-concentration-fruit-wastes-juice-using-bakery-yeast](https://journalclub.io/episodes/bioethanol-production-from-concentration-fruit-wastes-juice-using-bakery-yeast) |
| Source | [https://www.semanticscholar.org/paper/061ea1ab6414e986337699b80cbe2396c9bbe556](https://www.semanticscholar.org/paper/061ea1ab6414e986337699b80cbe2396c9bbe556) |
| Year | 2026 |
| Citations | 5 |
| Authors | L. Mtashobya, Shedrack Thomas Mgeni, J. Emmanuel |
| Paper ID | `b752cf6c-fa79-4056-8493-a3e2ff668457` |

## Classification

- **Problem Type:** biofuel production
- **Domain:** Bioinformatics & Health
- **Sub-domain:** Bioethanol production
- **Technique:** Fermentation and Distillation of Fruit Waste Juices
- **Technique Category:** framework
- **Type:** novel

## Summary

This study demonstrates the production of bioethanol from fruit waste juices using bakery yeast, highlighting a sustainable method for waste management and renewable energy generation. Engineers should care because this approach can contribute to reducing environmental impacts and provide an alternative energy source.

## Key Contribution

**The study presents a method for producing high-quality bioethanol from fruit waste juices through fermentation and distillation processes.**

## Problem

The increasing global consumption of fruits leads to significant fruit waste, which poses environmental challenges and opportunities for conversion into biofuels.

## Method

**Approach:** The method involves extracting juice from fruit wastes, fermenting it with bakery yeast to convert sugars into bioethanol, and then distilling the fermented product to increase alcohol content. Re-distillation is performed to enhance the purity of the bioethanol.

**Algorithm:**

1. 1. Collect and wash fruit wastes (pineapple, mango, watermelon, pawpaw).
2. 2. Chop the fruit wastes and extract juice using a blender.
3. 3. Measure total soluble solids (TSS), pH, and specific gravity of the juice.
4. 4. Ferment the juice with 200g of bakery yeast in a sealed container at room temperature.
5. 5. Monitor fermentation parameters (alcohol content, pH, TSS) at 24-hour intervals.
6. 6. Distill the fermented broth at 78°C to collect bioethanol.
7. 7. Re-distill the collected bioethanol to improve purity.

**Input:** Juice extracted from a mixture of fruit wastes (pineapple, mango, watermelon, pawpaw).

**Output:** Bioethanol with varying alcohol content (initially 30%, improved to 88% after re-distillation).

**Key Parameters:**

- `yeast_amount: 200g`
- `distillation_temperature: 78°C`
- `initial_alcohol_content: 30%`
- `final_alcohol_content: 88%`

**Complexity:** not stated

## Benchmarks

**Tested on:** Fruit waste juices from pineapple, mango, watermelon, and pawpaw.

**Results:**

- Alcohol content: 30% (initial), 88% (after re-distillation)

**Compared against:** Fermented juice without yeast produced 20% alcohol.

**Improvement:** Bioethanol yield improved from 20% to 30% with yeast and further to 88% after re-distillation.

## Implementation Guide

**Data Structures:** Containers for fermentation, Distillation apparatus

**Dependencies:** Bakery yeast (Saccharomyces cerevisiae), Blender for juice extraction, Distillation equipment

**Core Operation:**

```python
ferment(juice, yeast_amount) -> distill(finished_product) -> re_distill()
```

**Watch Out For:**

- Ensure proper sealing of fermentation containers to prevent contamination.
- Monitor fermentation conditions closely to avoid spoilage.
- Control temperature accurately during distillation to prevent loss of bioethanol.

## Use This When

- You need to convert organic waste into renewable energy.
- You are looking for sustainable methods to manage fruit waste.
- You want to produce biofuels with high alcohol content.

## Don't Use When

- The fruit waste is not suitable for fermentation.
- You require immediate energy production without processing time.
- You need a method that does not involve biological processes.

## Key Concepts

Fermentation, Distillation, Bioethanol, Fruit waste management

## Connects To

- Fermentation techniques
- Biofuel production methods
- Waste-to-energy technologies

## Prerequisites

- Understanding of fermentation processes
- Knowledge of distillation techniques

## Limitations

- Dependent on the availability of fruit waste.
- Requires specific conditions for optimal fermentation.
- Potential variability in bioethanol yield based on fruit type.

## Open Questions

- How can the yeast-fruit waste juice ratio be optimized for higher yields?
- What enzymes can be utilized to expedite carbohydrate breakdown in fruit wastes?

## Abstract

In 1896, Henry Ford created the "quadricycle". It was a tiny, skeletal car, about the size of a go-kart. And interestingly, his team engineered it not to run on gasoline, but on pure ethanol. Why? Because back then, gasoline was not an obvious choice. It was dirty and expensive, and hard to find. We take gasoline-infrastructure (like fueling stations and refineries) for granted today, but back then there was very little of that.
