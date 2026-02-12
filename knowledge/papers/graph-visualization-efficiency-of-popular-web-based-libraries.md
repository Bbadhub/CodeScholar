# Graph visualization efficiency of popular web-based libraries

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s42492-025-00193-y` |
| Full Paper | [https://doi.org/10.1186/s42492-025-00193-y](https://doi.org/10.1186/s42492-025-00193-y) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/ffd0c5ed32d2230253b9f09cb4a88985e6b2e0b0](https://www.semanticscholar.org/paper/ffd0c5ed32d2230253b9f09cb4a88985e6b2e0b0) |
| Source | [https://journalclub.io/episodes/graph-visualization-efficiency-of-popular-web-based-libraries](https://journalclub.io/episodes/graph-visualization-efficiency-of-popular-web-based-libraries) |
| Source | [https://www.semanticscholar.org/paper/ffd0c5ed32d2230253b9f09cb4a88985e6b2e0b0](https://www.semanticscholar.org/paper/ffd0c5ed32d2230253b9f09cb4a88985e6b2e0b0) |
| Year | 2026 |
| Citations | 2 |
| Authors | Xin Zhao, Xuan Wang, Xianzhe Zou, Huiming Liang, Genghuai Bai, Ning Zhang |
| Paper ID | `2970d40c-4a30-4229-bd15-300d6f358606` |

## Classification

- **Problem Type:** graph visualization performance evaluation
- **Domain:** Software Engineering
- **Sub-domain:** Graph Visualization Libraries
- **Technique:** Empirical performance evaluation of graph visualization libraries
- **Technique Category:** benchmarking_method
- **Type:** comparison

## Summary

This paper evaluates the performance of popular web-based graph visualization libraries, specifically D3.js, ECharts.js, and G6.js, to determine their efficiency in handling large graph datasets. Engineers should care because the findings provide empirical guidelines for selecting the appropriate library based on specific efficiency requirements for graph visualizations.

## Key Contribution

**A systematic evaluation of web-based graph visualization libraries with application-oriented guidelines for selecting libraries based on efficiency requirements.**

## Problem

The need for efficient graph visualization tools that can handle large datasets without performance degradation motivated this work.

## Method

**Approach:** The method involves a controlled experiment where various web-based graph visualization libraries are tested against a set of graph datasets. The performance is measured in terms of time cost and frame rate for generating visualizations.

**Algorithm:**

1. Select popular web-based graph visualization libraries (D3.js, ECharts.js, G6.js).
2. Choose rendering methods (SVG, Canvas, WebGL) for each library.
3. Prepare graph datasets with varying node scales (100 to 200k) and edge-to-node ratios (1 to 10).
4. Visualize each dataset using each library three times and record the time cost and frame rate.
5. Analyze the results to identify performance trends and create guidelines.

**Input:** Graph datasets with node scales from 100 to 200k and edge-to-node ratios from 1 to 10.

**Output:** Time costs and frame rates for visualizing each dataset using the libraries.

**Key Parameters:**

- `node_scale: 100 to 200k`
- `edge_to_node_ratio: 1 to 10`
- `layout_iterations: 200`

**Complexity:** Not stated

## Benchmarks

**Tested on:** 481 graph datasets covering node scales from 100 to 200k and edge-to-node ratios from 1 to 10.

**Results:**

- Time cost: average time taken to visualize datasets.
- Frame rate: number of visualization images displayed per second.

**Compared against:** D3-SVG, D3-Canvas, D3-WebGL, ECharts-SVG, ECharts-Canvas, G6-SVG, G6-Canvas.

**Improvement:** The paper provides specific performance metrics but does not quantify improvements over baselines.

## Implementation Guide

**Data Structures:** Graph datasets represented as adjacency lists or matrices.

**Dependencies:** D3.js, ECharts.js, G6.js, and their respective rendering libraries.

**Core Operation:**

```python
for library in libraries: for dataset in datasets: visualize(dataset, library)
```

**Watch Out For:**

- Ensure the dataset size is within the library's handling capacity.
- Be aware of the rendering method's limitations on interactivity.
- Performance may vary significantly based on the graph's structure.

## Use This When

- You need to visualize large graph datasets efficiently.
- You want to compare the performance of different graph visualization libraries.
- You require guidelines for selecting a library based on specific efficiency needs.

## Don't Use When

- You are working with small datasets where performance is not a concern.
- You need highly customized visualizations that require low-level library access.

## Key Concepts

Graph Layout Algorithms, Rendering Methods, Time Cost, Frame Rate, Node-Link Diagrams, Web-Based Visualization

## Connects To

- Force-directed algorithms
- SVG rendering
- Canvas rendering
- WebGL rendering
- Data visualization best practices

## Prerequisites

- Understanding of graph theory and visualization techniques.
- Familiarity with JavaScript and web-based libraries.
- Knowledge of performance metrics in software engineering.

## Limitations

- Performance results may vary across different hardware setups.
- The study does not cover all possible graph visualization libraries.
- Guidelines are based on specific datasets and may not generalize.

## Open Questions

- How do different graph structures affect performance across libraries?
- What are the implications of using newer rendering technologies?

## Abstract

On today’s episode, we’re taking a deeper look at performance unpredictability in graph visualization tools. We’ll follow along with the authors of this paper as they design a shootout between several different popular libraries, to determine which ones are (and are not) built for scale. We’ll see how they set up their benchmarking framework, how they ran their tests, and what results they obtained. Let’s dive in. In principle, modern web-based libraries like D3.js, ECharts.js, and G6.js make graph visualization accessible. They abstract away layout algorithms, handle DOM updates, and offer high-level APIs to plot diagrams with minimal boilerplate. But under the hood, they’re a bit of a rat’s nest. They wrap a tangle of layout routines, physics simulations, and rendering methods (SVG, Canvas, WebGL) that each scale in very different ways. The result is that, for many developers, these libraries have trouble scaling. When you outgrow the size and
