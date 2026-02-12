# Designing Microservices Using AI: A Systematic Literature Review

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/software4010006` |
| Full Paper | [https://doi.org/10.3390/software4010006](https://doi.org/10.3390/software4010006) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/e25d7ec31406f6108633ff159a935e6fb64d19c1](https://www.semanticscholar.org/paper/e25d7ec31406f6108633ff159a935e6fb64d19c1) |
| Source | [https://journalclub.io/episodes/designing-microservices-using-ai-a-systematic-literature-review](https://journalclub.io/episodes/designing-microservices-using-ai-a-systematic-literature-review) |
| Source | [https://www.semanticscholar.org/paper/e25d7ec31406f6108633ff159a935e6fb64d19c1](https://www.semanticscholar.org/paper/e25d7ec31406f6108633ff159a935e6fb64d19c1) |
| Year | 2026 |
| Citations | 9 |
| Authors | Daniel Narváez, Nicolas Battaglia, Alejandro Fernández, Gustavo Rossi |
| Paper ID | `be867612-aec7-4d9b-a9a8-014f957d9922` |

## Classification

- **Problem Type:** microservices design
- **Domain:** Software Engineering
- **Sub-domain:** Microservices Architecture
- **Technique:** AI-driven tools for microservices design
- **Technique Category:** framework
- **Type:** adaptation

## Summary

This paper presents a systematic literature review on the application of AI techniques in the design of microservices, highlighting how AI can automate and enhance service decomposition, decision-making, and architectural validation. Engineers should care because it provides insights into optimizing microservices design, addressing challenges like service boundaries and inter-service communication using AI.

## Key Contribution

**The review identifies key AI methods used in microservices design and highlights the challenges and benefits of integrating AI into the design process.**

## Problem

The need for scalable and modular software systems has led to challenges in designing microservices architectures, particularly in service decomposition and maintaining data consistency.

## Method

**Approach:** The method involves using AI techniques such as machine learning and natural language processing to automate the design of microservices. This includes analyzing requirements and user stories to identify service boundaries and optimize architectural decisions.

**Algorithm:**

1. 1. Gather design artifacts such as textual requirements and UML diagrams.
2. 2. Apply NLP techniques to analyze unstructured data and identify key entities.
3. 3. Use clustering algorithms (e.g., k-means) to group related functionalities.
4. 4. Define service boundaries based on the analysis.
5. 5. Validate architectural decisions using AI-driven tools.

**Input:** Design artifacts including textual requirements, user stories, UML diagrams, and source code.

**Output:** Optimized microservices architecture with defined service boundaries and improved design decisions.

**Key Parameters:**

- `clustering_algorithm: k-means`
- `NLP_tool: SEMGROMI`
- `service_boundary_definition: based on semantic similarity`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Studies published between 2018 and 2024 focusing on AI in microservices design.

**Results:**

- Percentage of studies using AI techniques: 100%
- Percentage using ML techniques: 53.5%
- Percentage using NLP: 32.6%

**Compared against:** Traditional microservices design methodologies without AI.

**Improvement:** AI techniques reported to enhance service decomposition and decision-making, but specific numerical improvements not stated.

## Implementation Guide

**Data Structures:** Service definitions, User story clusters, Design artifacts

**Dependencies:** NLP libraries (e.g., NLTK, SpaCy), Machine learning frameworks (e.g., Scikit-learn, TensorFlow)

**Core Operation:**

```python
services = cluster(user_stories); boundaries = define_boundaries(services); validate(architecture);
```

**Watch Out For:**

- Ensure clarity in user stories to avoid ambiguous service boundaries.
- Carefully calibrate clustering parameters to achieve meaningful segmentation.
- Monitor for data consistency issues during service interactions.

## Use This When

- Designing new microservices from scratch in complex domains.
- Automating service identification and decomposition tasks.
- Improving architectural validation processes using AI.

## Don't Use When

- Working with well-defined monolithic systems that do not require decomposition.
- When the team lacks expertise in AI techniques.
- In scenarios where regulatory compliance is critical and AI methods have not been validated.

## Key Concepts

service decomposition, AI-driven decision-making, natural language processing, machine learning, microservices architecture, performance optimization

## Connects To

- Domain-Driven Design (DDD)
- Microservices Performance Optimization
- AI in Software Engineering

## Prerequisites

- Understanding of microservices architecture
- Familiarity with AI techniques
- Knowledge of software design principles

## Limitations

- Challenges in handling distributed transactions remain.
- AI techniques depend heavily on the quality of input data.
- Limited empirical studies assessing the practical impact of AI-driven methods.

## Open Questions

- What are the best practices for integrating AI into existing microservices architectures?
- How can AI techniques be validated in real-world scenarios to ensure compliance and security?

## Abstract

The age of “Vibe Coding” has arrived. Whether we like it or not. If you’re unfamiliar with that term, consider yourself fortunate to be so insulated from programmer meme culture. It’s a term that held virtually no meaning a few years ago, and today is a common expression. So what does it mean? Vibe Coding is a verb, It’s the act of using LLMs and other A.I.-powered code-completion tools less like they’re a helper, and more like they’re the lead dev. It’s almost an inversion of control: you’re no longer using the A.I. when you get stuck, you’re using it all the time, by default. And it’s only when something doesn’t work as expected, or the system needs direction or course-correction, that you need to step in and help. The first few times I heard the term it was used in a derogatory way; saying someone was “vibe coding” their product was not a compliment. But in less than a year, that connotation has shifted, hard. Recently, even Garry Tan, the
