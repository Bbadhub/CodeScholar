# Energy-aware operation of HPC systems in Germany

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fhpcp.2025.1520207` |
| Full Paper | [https://doi.org/10.3389/fhpcp.2025.1520207](https://doi.org/10.3389/fhpcp.2025.1520207) |
| Source | [https://journalclub.io/episodes/energy-aware-operation-of-hpc-systems-in-germany](https://journalclub.io/episodes/energy-aware-operation-of-hpc-systems-in-germany) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `201b0e6c-c99d-4cc9-9adb-fe50ce20c6e0` |

## Classification

- **Problem Type:** energy efficiency optimization in high-performance computing
- **Domain:** Computer Science
- **Sub-domain:** High-Performance Computing (HPC)
- **Technique:** Energy-aware scheduling and dynamic power management
- **Technique Category:** optimization_algorithm
- **Type:** adaptation

## Summary

The paper discusses strategies and innovations for enhancing energy efficiency in high-performance computing (HPC) systems in Germany, addressing the significant power demands of these facilities. Engineers should care because implementing these strategies can lead to substantial cost savings and align with sustainability goals.

## Key Contribution

**The paper provides a comprehensive overview of state-of-the-art energy efficiency techniques and their implementation in German HPC centers.**

## Problem

The increasing demand for computational capacity in HPC systems leads to unsustainable energy consumption and costs.

## Method

**Approach:** The method involves implementing energy-efficient hardware architectures, advanced monitoring infrastructures, and dynamic power management strategies. These techniques aim to optimize the energy consumption of HPC systems while maintaining high performance.

**Algorithm:**

1. 1. Assess current energy consumption and performance metrics of HPC systems.
2. 2. Implement energy-aware scheduling to prioritize jobs based on their power draw.
3. 3. Utilize dynamic power management to adjust power consumption based on workload demands.
4. 4. Monitor energy usage continuously and adjust strategies as needed.
5. 5. Evaluate the impact of changes on performance and energy efficiency.

**Input:** Data on current energy consumption, job performance metrics, and workload characteristics.

**Output:** Optimized scheduling of jobs and reduced energy consumption in HPC systems.

**Key Parameters:**

- `PUE (Power Usage Efficiency): target < 1.3 by 2030`
- `Energy reuse: 10% for new data centers by 2026, increasing to 20% by 2028`

**Complexity:** not stated

## Benchmarks

**Tested on:** Data from various German HPC centers including DKRZ, FAU, HLRS, JSC, KIT, LRZ, MPCDF, TUD

**Results:**

- PUE: < 1.3
- Energy reuse: 10%-20% depending on the year of operation

**Compared against:** Previous energy consumption metrics from the same HPC centers

**Improvement:** Significant reduction in operational costs through energy efficiency measures.

## Implementation Guide

**Data Structures:** Job scheduling queue, Energy consumption logs, Performance metrics database

**Dependencies:** Monitoring tools for energy consumption, Dynamic power management software

**Core Operation:**

```python
while jobs remain in queue: schedule based on energy efficiency metrics
```

**Watch Out For:**

- Ensure compatibility of cooling systems with existing infrastructure.
- Monitor for unexpected increases in energy consumption during peak loads.
- Regularly update energy efficiency metrics to reflect current performance.

## Use This When

- You need to reduce operational costs in HPC systems.
- You are required to comply with energy efficiency regulations.
- You want to implement sustainable practices in data centers.

## Don't Use When

- The HPC workload is not sensitive to energy consumption.
- You are operating in a low-cost energy environment.
- The infrastructure is not capable of supporting advanced cooling solutions.

## Key Concepts

energy efficiency, dynamic power management, energy-aware scheduling, liquid cooling, monitoring infrastructures, HPC architectures

## Connects To

- Power Usage Effectiveness (PUE)
- Dynamic Voltage and Frequency Scaling (DVFS)
- Green computing practices

## Prerequisites

- Understanding of HPC system architectures
- Knowledge of energy consumption metrics
- Familiarity with scheduling algorithms

## Limitations

- High initial investment for new cooling systems.
- Potential performance trade-offs when prioritizing energy efficiency.
- Dependence on the availability of renewable energy sources.

## Open Questions

- How can energy efficiency measures be standardized across different HPC centers?
- What are the long-term impacts of energy-aware scheduling on job performance?

## Abstract

HPC engineers aren’t like most devs. They work in an environment that is decidedly...weird. It’s an environment where languages like Fortran abound (and are actually quite popular). An environment where batch jobs can queue for days, where computers are cooled by water instead of fans, where performance is measured in teraflops, storage is measured in exabytes, networking speeds are faster than most SSDs, and job failures can be caused by cosmic rays flipping bits. HPC is just a whole other universe. And it’s a universe that uses an almost unbelievable amount of power.High-performance computing centers are among the most power-hungry facilities in the world. A single supercomputing installation can draw upwards of 20 megawatts of juice. That’s an amount comparable to the total electricity consumption of a small city. The JUPITER system planned for Germany is expected to require an amount of power roughly
