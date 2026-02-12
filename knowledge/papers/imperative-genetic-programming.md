# Imperative Genetic Programming

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/sym16091146` |
| Full Paper | [https://doi.org/10.3390/sym16091146](https://doi.org/10.3390/sym16091146) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/21a21eac173204f8f295cae31c4d120ec846d35a](https://www.semanticscholar.org/paper/21a21eac173204f8f295cae31c4d120ec846d35a) |
| Source | [https://journalclub.io/episodes/imperative-genetic-programming](https://journalclub.io/episodes/imperative-genetic-programming) |
| Source | [https://www.semanticscholar.org/paper/21a21eac173204f8f295cae31c4d120ec846d35a](https://www.semanticscholar.org/paper/21a21eac173204f8f295cae31c4d120ec846d35a) |
| Year | 2026 |
| Citations | 1 |
| Authors | I. Fajfar, Žiga Rojec, Á. Bürmen, M. Kunaver, T. Tuma, Sašo Tomažič |
| Paper ID | `dd2065dd-2b0b-48cd-a586-4638a66bf58d` |

## Classification

- **Problem Type:** program synthesis
- **Domain:** Software Engineering
- **Sub-domain:** Genetic Programming
- **Technique:** Imperative Genetic Programming
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper introduces Imperative Genetic Programming, a novel approach that combines tree and linear genetic programming paradigms to evolve syntactically correct Python programs from scratch. Engineers should care because this method addresses the limitations of existing genetic programming techniques and enables the evolution of more complex imperative programs.

## Key Contribution

**A new encoding scheme that merges tree and linear representations to generate imperative Python programs without prior knowledge of their structure.**

## Problem

The need to evolve real Turing-like imperative programs from scratch without a priori assumptions on the solution structure.

## Method

**Approach:** The method integrates tree and linear genetic programming paradigms to create a genotype that can evolve imperative programs. It uses a linear sequence of instructions with embedded expression trees to ensure syntactic correctness in generated Python code.

**Algorithm:**

1. Initialize population of random programs.
2. Evaluate fitness of each program using least squares method.
3. Select programs for genetic operations using linear ranking.
4. Perform crossover between selected programs based on a probability.
5. Mutate the offspring programs based on a mutation probability.
6. Calculate fitness for the new generation of programs.
7. Repeat for a set number of generations or until stopping criteria are met.

**Input:** Training data in the form of input/output pairs for the target program.

**Output:** Evolved Python programs that meet the specified output criteria.

**Key Parameters:**

- `population_size: 1000`
- `number_of_generations: 2000`
- `mutation_probability: 0.5`
- `line_crossover_probability: 0.3`
- `maximum_loop_iterations: 100`
- `maximum_if_nesting: 2`
- `maximum_loop_nesting: 1`
- `tree_generation_depth: 2`
- `tree_evaluation_depth: 3`
- `program_length: 15`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** 35 problems characterized by varying Halstead complexity metrics.

**Results:**

- fitness calculated using least squares method.

**Compared against:** Standard genetic programming techniques.

**Improvement:** Demonstrated more sophisticated strategies compared to brute-force solutions.

## Implementation Guide

**Data Structures:** List for storing population of programs, Tree structure for expressions, Dictionary for variable mappings

**Dependencies:** Python 3.x, NumPy for numerical operations

**Core Operation:**

```python
for each program in population: evaluate_fitness(program); select_parents(); crossover(); mutate();
```

**Watch Out For:**

- Ensure proper handling of indentation in generated Python code.
- Limit loop iterations to prevent infinite loops during evolution.
- Be cautious of bloat in expression trees; implement depth limits.

## Use This When

- You need to evolve complex imperative programs without prior knowledge of their structure.
- You want to explore the capabilities of genetic programming in generating real software.
- You are working on problems that require optimization of program logic.

## Don't Use When

- The problem domain is strictly functional programming.
- You require deterministic program generation without evolutionary processes.
- The computational resources are severely limited.

## Key Concepts

genetic programming, imperative programming, evolutionary algorithms, program synthesis, fitness evaluation, crossover, mutation

## Connects To

- Evolutionary algorithms
- Tree-based genetic programming
- Linear genetic programming
- Program synthesis techniques

## Prerequisites

- Understanding of genetic algorithms
- Familiarity with Python programming
- Basic knowledge of evolutionary computation

## Limitations

- Limited to evolving imperative programs; may not generalize to functional programming.
- Performance may vary based on the complexity of the target program.
- Potential for code bloat if not managed properly.

## Open Questions

- How can the approach be adapted for functional programming paradigms?
- What are the implications of using different programming languages for evolution?

## Abstract

In 1948, less than 90 years after Darwin published "On the Origin of Species", Alan Turing applied the concept of natural selection to Computer Science. In an unpublished essay titled “Intelligent Machinery,” he wrote: “There is the genetical or evolutionary search by which a combination of genes is looked for, the criterion being the survival value.” This line appears to be the first mention by any person, anywhere, of what is now referred to as an evolutionary algorithm. And now, 76 years later, this niche concept which has existed on the fringes of computer science for decades, is poised to finally have its time in the spotlight. Specifically, one technique within this field: Genetic Programming is coming to the forefront. Why? Because the same hardware advances, the same distributed systems and cloud computing advances that have enabled the proliferation of LLMs can also enable the widespread adoption of Genetic Programming.
