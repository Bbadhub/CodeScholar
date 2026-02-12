# Embodied climate impacts in urban development: a neighborhood case study

## Access

| Field | Value |
|-------|-------|
| DOI | `10.5334/bc.478` |
| Full Paper | [https://doi.org/10.5334/bc.478](https://doi.org/10.5334/bc.478) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/123285f9af605610aa9d2eb70d86dd38916b65b7](https://www.semanticscholar.org/paper/123285f9af605610aa9d2eb70d86dd38916b65b7) |
| Source | [https://journalclub.io/episodes/embodied-climate-impacts-in-urban-development-a-neighborhood-case-study](https://journalclub.io/episodes/embodied-climate-impacts-in-urban-development-a-neighborhood-case-study) |
| Source | [https://www.semanticscholar.org/paper/123285f9af605610aa9d2eb70d86dd38916b65b7](https://www.semanticscholar.org/paper/123285f9af605610aa9d2eb70d86dd38916b65b7) |
| Year | 2026 |
| Citations | 2 |
| Authors | Simon Sjökvist, N. Francart, M. Balouktsi, H. Birgisdóttir |
| Paper ID | `71935759-aec6-49a7-a586-843d53a0d57e` |

## Classification

- **Problem Type:** life-cycle assessment of embodied carbon emissions
- **Domain:** Optimization & Operations Research
- **Sub-domain:** Sustainability assessment
- **Technique:** Life-Cycle Assessment (LCA)
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

The paper conducts a comprehensive life-cycle assessment of a newly developed neighborhood in Copenhagen, quantifying embodied CO2 equivalent emissions from buildings, infrastructure, landscape, and major earthworks. Engineers should care because it provides a framework for assessing the environmental impact of urban development, which is increasingly critical in sustainable design.

## Key Contribution

**A novel methodology for quantifying embodied carbon emissions in urban development projects.**

## Problem

The need to understand the carbon footprint of urban development to inform sustainable building practices.

## Method

**Approach:** The method involves collecting data on materials, construction processes, and energy use throughout the life cycle of the neighborhood. This data is then analyzed to calculate the total embodied CO2 emissions associated with the project.

**Algorithm:**

1. 1. Define the scope of the assessment including boundaries and functional units.
2. 2. Collect data on materials used, construction methods, and energy consumption.
3. 3. Calculate the carbon emissions associated with each material and process.
4. 4. Aggregate the emissions data to obtain total embodied CO2 emissions.
5. 5. Analyze results to identify key areas for improvement.

**Input:** Data on materials, construction processes, and energy use.

**Output:** Total embodied CO2 equivalent emissions for the neighborhood.

**Key Parameters:**

- `material_emission_factor: varies by material type`
- `construction_energy_use: specific to construction methods`

**Complexity:** not stated

## Benchmarks

**Tested on:** Data from the Copenhagen neighborhood case study

**Results:**

- embodied CO2 emissions: specific values not stated

**Compared against:** Previous assessments of similar urban developments

**Improvement:** not stated

## Implementation Guide

**Data Structures:** Database for material properties, Data collection forms for construction processes

**Dependencies:** LCA software tools, Environmental impact databases

**Core Operation:**

```python
total_emissions = sum(material_emission * quantity for each material)
```

**Watch Out For:**

- Ensure accurate data collection to avoid underestimating emissions.
- Consider regional variations in material emissions.

## Use This When

- Assessing the environmental impact of new urban developments.
- Designing sustainable building practices.
- Evaluating compliance with carbon reduction targets.

## Don't Use When

- The project scope does not include carbon emissions assessment.
- Data on materials and processes is unavailable.

## Key Concepts

life-cycle assessment, embodied carbon, urban development, sustainability metrics

## Connects To

- Sustainable building design
- Environmental impact assessment
- Carbon footprint analysis

## Prerequisites

- Understanding of life-cycle assessment principles
- Knowledge of carbon accounting methods

## Limitations

- Data availability may limit assessment accuracy
- Focus on embodied carbon may overlook operational emissions

## Open Questions

- How to standardize LCA methodologies across different regions?
- What are the long-term impacts of embodied carbon on climate change?

## Abstract

Just how much carbon are we talking? And how bad is this problem exactly? That’s what the authors of today’s paper intend to find out. In this study they’re conducting a comprehensive life-cycle assessment of a newly developed neighborhood in Copenhagen, quantifying embodied CO2 equivalent emissions from buildings, infrastructure, landscape, and major earthworks.
