# Head in the game: the impact of cognitive abilities on performance of National Football League quarterbacks

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fpsyg.2025.1540498` |
| Full Paper | [https://doi.org/10.3389/fpsyg.2025.1540498](https://doi.org/10.3389/fpsyg.2025.1540498) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/17c43a18beb8a9fdbe1760a9a351f0da3395f67d](https://www.semanticscholar.org/paper/17c43a18beb8a9fdbe1760a9a351f0da3395f67d) |
| Source | [https://journalclub.io/episodes/head-in-the-game-the-impact-of-cognitive-abilities-on-performance-of-national-football-league-quarterbacks](https://journalclub.io/episodes/head-in-the-game-the-impact-of-cognitive-abilities-on-performance-of-national-football-league-quarterbacks) |
| Source | [https://www.semanticscholar.org/paper/17c43a18beb8a9fdbe1760a9a351f0da3395f67d](https://www.semanticscholar.org/paper/17c43a18beb8a9fdbe1760a9a351f0da3395f67d) |
| Year | 2026 |
| Citations | 1 |
| Authors | R. T. Boone, Nicholas S Zambrotta, Andrew M. Manocchio, James K Bowman, D. Corrado, Alan Hartley |
| Paper ID | `194865a7-7b8d-4af5-88d0-7214d3eb2a7f` |

## Classification

- **Problem Type:** predictive modeling for athlete performance
- **Domain:** Machine Learning & AI
- **Sub-domain:** Sports Analytics
- **Technique:** Athletic Intelligence Quotient (AIQ)
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This study investigates the impact of cognitive abilities, measured by the Athletic Intelligence Quotient (AIQ), on the performance of NFL quarterbacks. Engineers should care because understanding these cognitive metrics can inform the development of predictive models for athlete performance in sports analytics.

## Key Contribution

**The study demonstrates that cognitive abilities, particularly Reaction Time, significantly predict NFL quarterback performance metrics beyond traditional draft pick evaluations.**

## Problem

The work is motivated by the need to improve recruitment and performance prediction of NFL quarterbacks using cognitive assessments.

## Method

**Approach:** The AIQ assesses cognitive abilities relevant to athletic performance through a series of subtests. The results are then correlated with performance metrics to evaluate predictive power.

**Algorithm:**

1. 1. Administer the AIQ to NFL quarterback draftees.
2. 2. Collect performance metrics from NFL games.
3. 3. Perform regression analysis to evaluate the relationship between AIQ subscales and performance metrics.
4. 4. Control for draft pick in the analysis.
5. 5. Report significant predictors and their contributions to performance variance.

**Input:** AIQ scores from cognitive assessments and NFL performance metrics (e.g., passing yards, QB rating).

**Output:** Regression coefficients indicating the predictive power of cognitive abilities on quarterback performance.

**Key Parameters:**

- `AIQ subscales: Reaction Time, Visual Spatial Processing, Decision Making, Learning Efficiency`
- `Draft Pick: categorical variable representing player selection order`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Performance metrics from 42 NFL quarterbacks over multiple seasons (2018-2021)

**Results:**

- Career Approximate Value (CAV)
- Quarterback Rating (QBR)
- Passing Yards per Game
- Rushing Yards per Game

**Compared against:** Draft Pick evaluations

**Improvement:** Reaction Time explained an additional 13% of variance in CAV and 8% in QBR after controlling for Draft Pick.

## Implementation Guide

**Data Structures:** DataFrame for AIQ scores and performance metrics, Regression model structure for analysis

**Dependencies:** Pandas for data manipulation, Statsmodels or Scikit-learn for regression analysis

**Core Operation:**

```python
model = sm.OLS(y, X).fit()  # where y is performance metric and X includes AIQ scores and draft pick
```

**Watch Out For:**

- Ensure data is de-identified to protect player privacy.
- Control for confounding variables like draft pick to avoid biased results.

## Use This When

- Developing predictive models for athlete performance based on cognitive assessments.
- Evaluating quarterback prospects for NFL teams using cognitive metrics.
- Integrating cognitive data into sports analytics platforms.

## Don't Use When

- When focusing solely on physical performance metrics without cognitive considerations.
- In contexts where cognitive assessments are not feasible or acceptable.

## Key Concepts

Cognitive abilities, Athletic Intelligence Quotient, Predictive modeling, Regression analysis, Performance metrics

## Connects To

- Machine Learning models
- Statistical analysis techniques
- Sports performance analytics frameworks

## Prerequisites

- Understanding of regression analysis
- Familiarity with cognitive assessment methods
- Knowledge of sports performance metrics

## Limitations

- Small sample size of 42 quarterbacks
- Potential biases in cognitive assessments
- Generalizability to other positions not established

## Open Questions

- How do cognitive abilities interact with physical skills in other sports?
- What are the long-term impacts of cognitive training on athlete performance?

## Abstract

We’re releasing this episode on Thanksgiving for a reason. You’re probably going to be spending several hours this evening stuck in front of a TV watching the game, and listening to your brother-in-law and your cousin drone on about football stuff.
