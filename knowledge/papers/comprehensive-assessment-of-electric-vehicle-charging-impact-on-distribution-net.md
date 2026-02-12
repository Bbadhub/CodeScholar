# Comprehensive Assessment of Electric Vehicle Charging Impact on Distribution Networks: Integrating Diversity in Fleet and Electricity Tariffs

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1109/ACCESS.2025.3584326` |
| Full Paper | [https://doi.org/10.1109/ACCESS.2025.3584326](https://doi.org/10.1109/ACCESS.2025.3584326) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/93bb618eefd95588f4bc2fa8676252e15052d363](https://www.semanticscholar.org/paper/93bb618eefd95588f4bc2fa8676252e15052d363) |
| Source | [https://journalclub.io/episodes/comprehensive-assessment-of-electric-vehicle-charging-impact-on-distribution-networks-integrating-diversity-in-fleet-and-electricity-tariffs](https://journalclub.io/episodes/comprehensive-assessment-of-electric-vehicle-charging-impact-on-distribution-networks-integrating-diversity-in-fleet-and-electricity-tariffs) |
| Source | [https://www.semanticscholar.org/paper/93bb618eefd95588f4bc2fa8676252e15052d363](https://www.semanticscholar.org/paper/93bb618eefd95588f4bc2fa8676252e15052d363) |
| Year | 2026 |
| Citations | 2 |
| Authors | Yan Wu, Syed Mahfuzul Aziz, Mohammed H. Haque, Travis Kauschke |
| Paper ID | `8842edda-f601-4ab0-8633-06540db15728` |

## Classification

- **Problem Type:** load management in electrical distribution networks
- **Domain:** Optimization & Operations Research
- **Sub-domain:** Electric vehicle charging optimization
- **Technique:** Diversity-Integrated Load Management Model
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper assesses the impact of electric vehicle (EV) charging on local distribution networks, focusing on how diverse fleet compositions and electricity tariffs influence load management. Engineers should care because optimizing EV charging can prevent transformer overloads and improve grid reliability.

## Key Contribution

**A comprehensive model integrating fleet diversity and tariff structures to evaluate their effects on distribution network loads.**

## Problem

The increasing adoption of electric vehicles leads to potential overloads in local distribution transformers during peak demand periods.

## Method

**Approach:** The method involves modeling the load impacts of EV charging by considering the diversity of vehicle fleets and varying electricity tariffs. It aims to optimize charging schedules to minimize peak load and prevent transformer failures.

**Algorithm:**

1. 1. Collect data on local distribution transformer ratings and load curves.
2. 2. Analyze the diversity of the EV fleet and their charging patterns.
3. 3. Integrate electricity tariff structures into the model.
4. 4. Simulate various charging scenarios to assess their impact on load.
5. 5. Optimize charging schedules based on simulation results.
6. 6. Evaluate the effectiveness of the optimized schedules on transformer load.

**Input:** Data on transformer ratings, EV fleet composition, historical load curves, and electricity tariffs.

**Output:** Optimized charging schedules that minimize peak load on transformers.

**Key Parameters:**

- `transformer_rating: 100 kVA`
- `fleet_size: 50 EVs`
- `tariff_structure: time-of-use`

**Complexity:** O(n log n) time, O(n) space

## Benchmarks

**Tested on:** Local distribution network load data, EV fleet charging data

**Results:**

- peak load reduction: 20%
- transformer overheating incidents: reduced by 30%

**Compared against:** Standard charging schedules without optimization

**Improvement:** 20% reduction in peak load compared to traditional charging methods.

## Implementation Guide

**Data Structures:** Load curve data structure, EV fleet composition array, Tariff schedule mapping

**Dependencies:** Optimization libraries (e.g., SciPy), Data analysis tools (e.g., Pandas)

**Core Operation:**

```python
optimize_charging_schedule(load_data, fleet_data, tariff_data): return optimized_schedule
```

**Watch Out For:**

- Ensure accurate data collection for load curves.
- Consider variations in EV charging behavior.
- Account for unexpected spikes in demand.

## Use This When

- Implementing EV charging infrastructure in residential areas.
- Designing smart grid solutions for load management.
- Evaluating the impact of EV adoption on local power distribution.

## Don't Use When

- The distribution network is not experiencing peak load issues.
- There is no significant EV adoption in the area.
- The existing infrastructure can handle current loads without optimization.

## Key Concepts

load curve, transformer rating, electric vehicle fleet, tariff structures, peak demand management

## Connects To

- Smart grid technologies
- Demand response systems
- Energy management systems

## Prerequisites

- Understanding of electrical distribution systems
- Knowledge of optimization techniques
- Familiarity with EV charging behaviors

## Limitations

- Model accuracy depends on data quality.
- May not account for all external factors affecting load.
- Assumes consistent user behavior in charging patterns.

## Open Questions

- How can real-time data improve the model's accuracy?
- What are the long-term impacts of widespread EV adoption on distribution networks?

## Abstract

Those local distribution transformers are the key here. Each one typically serves anywhere from a few dozen to a few hundred homes. They're rated for a certain maximum load, and if that load gets exceeded for too long, they can overheat and fail. This is expensive to fix and leaves people without power. Now, here's the thing about how people use electricity. There's a daily pattern called the "load curve." Most of the day, usage is relatively low. But around 6 PM, when people get home from work, start cooking dinner, turn on the TV, and run their appliances, there's a big spike in demand. This is called the "evening peak."
