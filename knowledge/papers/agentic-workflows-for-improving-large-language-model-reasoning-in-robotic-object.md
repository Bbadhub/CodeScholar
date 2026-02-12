# Agentic Workflows for Improving Large Language Model Reasoning in Robotic Object-Centered Planning

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/robotics14030024` |
| Full Paper | [https://doi.org/10.3390/robotics14030024](https://doi.org/10.3390/robotics14030024) |
| Source | [https://journalclub.io/episodes/agentic-workflows-for-improving-large-language-model-reasoning-in-robotic-object-centered-planning](https://journalclub.io/episodes/agentic-workflows-for-improving-large-language-model-reasoning-in-robotic-object-centered-planning) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `d6496498-3802-4b18-a5bb-9d7bd2199143` |

## Classification

- **Problem Type:** object-centered planning
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Robotic Planning with LLMs
- **Technique:** Agentic Workflows
- **Technique Category:** framework
- **Type:** novel

## Summary

This paper presents agentic workflows to enhance the reasoning capabilities of Large Language Models (LLMs) in robotic object-centered planning, addressing the limitations of single-step LLM prompts that struggle with complex queries. Engineers should care because these workflows improve response quality and reliability in robotic applications, particularly in environments requiring nuanced understanding and reasoning.

## Key Contribution

**The introduction of three agentic workflows—Self-Reflection, Multi-Agent Reflection, and LLM Ensemble—to improve LLM reasoning in robotic planning tasks.**

## Problem

The challenge of accurately identifying relevant objects in a robotic environment based on natural language queries, especially when queries introduce ambiguity or require reasoning about object functions.

## Method

**Approach:** The method involves integrating LLMs with structured workflows that guide the model's output through iterative feedback and refinement. This allows for improved reasoning and reduced hallucinations in responses.

**Algorithm:**

1. 1. Input a semantic map and a natural language query to the LLM.
2. 2. Generate an initial response listing relevant objects.
3. 3. Apply the Self-Reflection workflow to evaluate the response based on correctness, relevance, and clarity.
4. 4. Generate feedback and refine the initial response based on this feedback.
5. 5. Optionally repeat the reflection and refinement steps for improved accuracy.

**Input:** A semantic map in JSON format and a natural language query.

**Output:** A ranked list of relevant object identifiers from the semantic map.

**Key Parameters:**

- `max_iterations: 5`
- `feedback_threshold: 0.8`

**Complexity:** Not stated

## Benchmarks

**Tested on:** ScanNet, SceneNN

**Results:**

- object retrieval performance: average improvement of 10% over baseline

**Compared against:** Single-step LLM prompt approach

**Improvement:** 10% improvement for Self-Reflection, 9.67% for Multi-Agent Reflection, and 4.67% for LLM Ensemble.

## Implementation Guide

**Data Structures:** JSON representation of semantic maps, Lists for storing object identifiers

**Dependencies:** Transformers library for LLMs, Voxeland for semantic map generation

**Core Operation:**

```python
response = LLM(semantic_map, query); feedback = LLM(reflect_prompt, response); refined_response = LLM(refine_prompt, response, feedback);
```

**Watch Out For:**

- Ensure the semantic map is correctly formatted in JSON.
- Monitor the number of iterations to avoid excessive processing time.
- Be cautious of LLM hallucinations even after refinement.

## Use This When

- You need to improve the accuracy of object identification in robotic systems.
- Your application involves complex queries that require reasoning about object functions.
- You want to mitigate hallucinations in LLM outputs for robotic tasks.

## Don't Use When

- The task requires real-time responses with minimal processing time.
- The environment is static and does not require complex reasoning.
- You have a limited computational budget that cannot support multiple LLMs.

## Key Concepts

semantic maps, LLM reasoning, reflection, multi-agent systems, object-centered planning, feedback loops

## Connects To

- Chain-of-Thought prompting
- Tool Use workflows
- Multi-Agent frameworks

## Prerequisites

- Understanding of LLMs and their limitations.
- Familiarity with semantic mapping techniques.
- Knowledge of robotic planning concepts.

## Limitations

- Performance degrades with larger semantic maps due to context length saturation.
- Requires significant computational resources for multiple LLMs.
- Still prone to hallucinations despite refinements.

## Open Questions

- How can these workflows be adapted for real-time applications?
- What are the best practices for integrating external resources into agentic workflows?

## Abstract

In this paper, the baseline approach that they’re comparing against uses a single-step LLM prompt. It includes the full semantic map in JSON format and a natural language query, and it returns a ranked list of object identifiers. In practice, this approach works fine on simple queries, especially those that require direct string matches or category lookups. But its performance drops quickly when the query introduces ambiguity, requires reasoning about object function, or includes negative logic. Since it’s a single-step there’s no iterative feedback, no correction step, and no filtering mechanism beyond what the LLM does implicitly. As the map size increases, performance actually degrades further. This is due to context length saturation and the LLM's tendency to focus on early or late parts of the prompt, ignoring the middle. This is (more or less) the core technical limitation that the authors are trying to solve. The challenge is
