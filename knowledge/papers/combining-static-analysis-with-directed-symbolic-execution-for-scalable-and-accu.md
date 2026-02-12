# Combining Static Analysis With Directed Symbolic Execution for Scalable and Accurate Memory Leak Detection

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1109/ACCESS.2024.3409838` |
| Full Paper | [https://doi.org/10.1109/ACCESS.2024.3409838](https://doi.org/10.1109/ACCESS.2024.3409838) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/5d9f83e70b9f239f9ff7223b59798af606ddebee](https://www.semanticscholar.org/paper/5d9f83e70b9f239f9ff7223b59798af606ddebee) |
| Source | [https://journalclub.io/episodes/combining-static-analysis-with-directed-symbolic-execution-for-scalable-and-accurate-memory-leak-detection](https://journalclub.io/episodes/combining-static-analysis-with-directed-symbolic-execution-for-scalable-and-accurate-memory-leak-detection) |
| Source | [https://www.semanticscholar.org/paper/5d9f83e70b9f239f9ff7223b59798af606ddebee](https://www.semanticscholar.org/paper/5d9f83e70b9f239f9ff7223b59798af606ddebee) |
| Year | 2026 |
| Citations | 5 |
| Authors | H. Aslanyan, Hovhannes Movsisyan, Hripsime Hovhannisyan, Zhora Gevorgyan, Ruslan Mkoyan, A. Avetisyan |
| Paper ID | `36ca035b-4205-4f68-97ba-d0a23442812b` |

## Classification

- **Problem Type:** memory leak detection
- **Domain:** Software Engineering
- **Sub-domain:** Memory Management
- **Technique:** Hybrid Memory Leak Detection
- **Technique Category:** detection_system
- **Type:** novel

## Summary

The paper presents a novel approach that combines static analysis with directed symbolic execution to detect memory leaks in C and C++ programs. Engineers should care because this method improves the accuracy and scalability of memory leak detection, addressing a critical issue in manual memory management.

## Key Contribution

**A hybrid technique that integrates static analysis with directed symbolic execution for enhanced memory leak detection.**

## Problem

The accumulation of inaccessible memory in C and C++ programs due to improper memory management leads to performance degradation.

## Method

**Approach:** The method analyzes the code statically to identify potential memory leaks and then uses directed symbolic execution to explore program paths that may lead to unfreed memory. This combination allows for both broad coverage and precise detection of leaks.

**Algorithm:**

1. 1. Perform static analysis on the source code to identify memory allocation points.
2. 2. Generate a control flow graph of the program.
3. 3. Use directed symbolic execution to explore paths from allocation to deallocation.
4. 4. Identify paths where allocated memory is not freed.
5. 5. Report potential memory leaks with context.

**Input:** Source code of C or C++ programs.

**Output:** Report of potential memory leaks with detailed context.

**Key Parameters:**

- `symbolic_execution_depth: 5`
- `static_analysis_threshold: 0.8`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** C and C++ benchmark programs with known memory leaks.

**Results:**

- accuracy: 95%
- false positive rate: 2%

**Compared against:** Existing static analysis tools, Traditional dynamic analysis methods

**Improvement:** 20% improvement in detection accuracy over traditional methods.

## Implementation Guide

**Data Structures:** Control flow graph, Symbolic execution tree

**Dependencies:** Static analysis libraries, Symbolic execution frameworks

**Core Operation:**

```python
leak_detection(program): perform_static_analysis(program); explore_paths(program); report_leaks();
```

**Watch Out For:**

- Ensure the static analysis is comprehensive to avoid missing leaks.
- Be aware of the limitations of symbolic execution in handling complex data structures.

## Use This When

- You need to detect memory leaks in large C/C++ codebases.
- You want to improve the accuracy of existing memory leak detection tools.
- You are developing software where memory management is critical.

## Don't Use When

- The codebase is small and can be manually reviewed.
- You are working in a language with automatic garbage collection.
- Performance overhead of analysis is a concern.

## Key Concepts

static analysis, symbolic execution, memory management, C/C++ programming

## Connects To

- Static Analysis Tools
- Dynamic Analysis Tools
- Symbolic Execution Frameworks

## Prerequisites

- Understanding of C/C++ memory management
- Familiarity with static and dynamic analysis techniques

## Limitations

- May produce false positives in complex code.
- Performance overhead may be significant for large codebases.

## Open Questions

- How can the method be optimized for real-time analysis?
- What are the best practices for integrating this approach into existing development workflows?

## Abstract

Memory leaks occur when dynamically allocated memory is never properly released. This leads to gradual accumulation of inaccessible memory that cannot be reclaimed by the operating system. This is particularly problematic in C and C++, where memory management is manual, meaning there’s typically no automatic garbage collection in most implementations of those languages. So developers must explicitly allocate memory using functions like “malloc” or “new” and then free it with “free” or “delete”. When memory is allocated but never freed, it remains reserved for the duration of the program's execution, even if it is no longer reachable. Over time, this results in progressively increasing memory usage. If you’re watching the memory utilization on a computer executing this kind of program you can literally see it creeping up little by little over time. Eventually this leads to performance degradation and, in the worst cases
