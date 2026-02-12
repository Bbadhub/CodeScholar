# Feasibility Study on MHEV Application for Motorbikes: Components Sizing, Strategy Optimization through Dynamic Programming and Analysis of Possible Benefits

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/vehicles6030068` |
| Full Paper | [https://doi.org/10.3390/vehicles6030068](https://doi.org/10.3390/vehicles6030068) |
| Source | [https://journalclub.io/episodes/feasibility-study-on-mhev-application-for-motorbikes-components-sizing-strategy-optimization-through-dynamic-programming-and-analysis-of-possible-benefits](https://journalclub.io/episodes/feasibility-study-on-mhev-application-for-motorbikes-components-sizing-strategy-optimization-through-dynamic-programming-and-analysis-of-possible-benefits) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `7fa92afb-7001-47c2-888a-f91861461f8c` |

## Classification

- **Problem Type:** energy management optimization for hybrid vehicles
- **Domain:** Machine Learning & AI
- **Sub-domain:** Dynamic Programming for Energy Management
- **Technique:** Dynamic Programming (DP)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

This paper presents a feasibility study on the application of mild hybrid electric vehicle (MHEV) technology for motorcycles, focusing on component sizing and strategy optimization using dynamic programming. Engineers should care because it provides a systematic approach to reducing fuel consumption and CO2 emissions in motorcycles, which is increasingly important due to regulatory pressures.

## Key Contribution

**The development of a dynamic programming-based optimization strategy for MHEV architecture in motorcycles to minimize fuel consumption.**

## Problem

The need to reduce CO2 emissions from motorcycles while maintaining performance and managing costs and space constraints.

## Method

**Approach:** The method involves simulating a motorcycle's performance under a homologation cycle and optimizing the power unit's usage strategy through dynamic programming. The optimization focuses on minimizing fuel consumption while considering various configurations of hybridization ratios.

**Algorithm:**

1. 1. Define the state of the system and control variables.
2. 2. Discretize the dynamical system representing the motorcycle.
3. 3. Compute instantaneous costs associated with control actions.
4. 4. Calculate total costs backward from the final timestep to the initial one.
5. 5. Apply Bellman's principle to find the optimized path for minimizing costs.

**Input:** Motorcycle specifications, hybridization ratios, and homologation cycle parameters.

**Output:** Optimized power-split strategy and estimated fuel consumption reduction.

**Key Parameters:**

- `hybridization_ratio: varies (specific values not stated)`
- `nominal_voltage: 48 V`
- `target_capacity: 500 kJ to 4000 kJ`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** World Motorcycle Test Cycle (WMTC)

**Results:**

- fuel consumption reduction
- CO2 emissions reduction

**Compared against:** Standard internal combustion engine (ICE) motorcycle

**Improvement:** Significant reduction in fuel consumption compared to baseline ICE.

## Implementation Guide

**Data Structures:** 1D model of the motorcycle, state variable for energy management

**Dependencies:** Dynamic programming libraries, Simulation tools for vehicle dynamics

**Core Operation:**

```python
for each timestep: calculate torque output; optimize power-split using DP; minimize fuel consumption.
```

**Watch Out For:**

- Ensure accurate modeling of the ICE efficiency maps.
- Consider the impact of electrical component losses in final analysis.
- Be aware of the limitations of the DP approach for real-time applications.

## Use This When

- Designing hybrid powertrains for motorcycles.
- Evaluating fuel consumption reduction strategies.
- Optimizing energy management systems in vehicles.

## Don't Use When

- Real-time applications requiring immediate decision-making.
- When the complexity of the model needs to be minimized.

## Key Concepts

mild-hybrid technology, dynamic programming, energy management, kinetic energy recovery, load-point shifting

## Connects To

- Energy management strategies in hybrid vehicles
- Dynamic programming applications in control systems
- Modeling of vehicle dynamics

## Prerequisites

- Understanding of hybrid vehicle architectures
- Familiarity with dynamic programming techniques
- Knowledge of energy management systems

## Limitations

- Not suitable for real-time optimization due to computational complexity.
- Assumes a predefined mission profile for optimization.
- Does not account for efficiency losses in electric components in initial analysis.

## Open Questions

- How to effectively integrate real-time optimization techniques with DP?
- What are the long-term impacts of hybridization on motorcycle performance and maintenance?

## Abstract

About a month ago, on September 7th, Héctor Garzó rounded the final turn at San Marino, crossed the finish line, and became the 2024 MotoE World Champion. He wasn’t riding any normal motorcycle. He was riding a fully-electric Ducati superbike, with a top speed of about 171 miles per hour. In fact, everyone in that race was riding a Ducati, because the storied Italian manufacturer has signed a deal to be the exclusive provider of electric motorcycles for the entire field through 2026. You see, Ducati is going long on electric motorcycles, and doing everything they can to push the technology (and the acceptance of it) to higher and higher levels. So far, they haven’t seen much success. The MotoE race where Garzo was crowned champion was streamed live on Youtube. As of this writing, the video only has about 11,000 views. Total. For a world championship.
