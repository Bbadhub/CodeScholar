# Exploring cognitive presence patterns in GenAI-integrated six-hat thinking technique scaffolded discussion: an epistemic network analysis

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s41239-025-00545-x` |
| Full Paper | [https://doi.org/10.1186/s41239-025-00545-x](https://doi.org/10.1186/s41239-025-00545-x) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/a68d754303aaa7e94966302fddab7c6f068c58fb](https://www.semanticscholar.org/paper/a68d754303aaa7e94966302fddab7c6f068c58fb) |
| Source | [https://journalclub.io/episodes/exploring-cognitive-presence-patterns-in-genai-integrated-six-hat-thinking-technique-scaffolded-discussion-an-epistemic-network-analysis](https://journalclub.io/episodes/exploring-cognitive-presence-patterns-in-genai-integrated-six-hat-thinking-technique-scaffolded-discussion-an-epistemic-network-analysis) |
| Source | [https://www.semanticscholar.org/paper/a68d754303aaa7e94966302fddab7c6f068c58fb](https://www.semanticscholar.org/paper/a68d754303aaa7e94966302fddab7c6f068c58fb) |
| Year | 2026 |
| Citations | 3 |
| Authors | Manli Yu, Zhi Liu, Taotao Long, Dong Li, Lei Deng, Xiangyan Kong |
| Paper ID | `20f15501-7515-4e9b-af2c-bad82a684442` |

## Classification

- **Problem Type:** cognitive presence analysis in educational settings
- **Domain:** Education Technology
- **Sub-domain:** Cognitive Presence Analysis
- **Technique:** Epistemic Network Analysis (ENA)
- **Technique Category:** analysis_method
- **Type:** novel

## Summary

This study investigates the impact of Generative AI (GenAI) integrated with the six-hat thinking technique on cognitive presence patterns among pre-service teachers. It reveals that while GenAI can enhance cognitive presence, its effects vary significantly based on individual creativity levels, which is crucial for engineers developing educational tools.

## Key Contribution

**The study demonstrates that GenAI acts as a cognitive amplifier, enhancing cognitive presence in high-creativity individuals while potentially exacerbating achievement gaps in low-creativity individuals.**

## Problem

The research addresses the challenge of understanding how GenAI influences cognitive engagement and learning outcomes in educational contexts, particularly for pre-service teachers.

## Method

**Approach:** The method involves using the six-hat thinking technique to structure discussions among pre-service teachers, with some groups utilizing GenAI for information retrieval and problem-solving. Cognitive presence is then analyzed using ENA to visualize and explore cognitive engagement patterns.

**Algorithm:**

1. 1. Introduce participants to the six-hat thinking technique and GenAI tools.
2. 2. Conduct group discussions using the six-hat technique, integrating GenAI suggestions at appropriate stages.
3. 3. Collect discussion data from QQ over a 13-week period.
4. 4. Code the discussion posts according to cognitive presence levels: Triggering, Exploration, Integration, Resolution.
5. 5. Apply ENA to analyze co-occurrences of cognitive elements in the discussions.
6. 6. Visualize cognitive presence patterns using ENA.

**Input:** Discussion posts from QQ platform, creativity test scores.

**Output:** Cognitive presence patterns visualized as an epistemic network.

**Key Parameters:**

- `creativity_threshold: top 20% and bottom 20% based on TTCT and SCCT scores`
- `discussion_duration: 13 weeks`

**Complexity:** not stated

## Benchmarks

**Tested on:** Discussion posts from 108 pre-service teachers over 13 weeks

**Results:**

- Cognitive presence levels: Triggering, Exploration, Integration, Resolution; F1 score of cognitive presence classification: between 0.779 and 0.965

**Compared against:** Groups using six-hat technique without GenAI

**Improvement:** No statistically significant difference in cognitive presence patterns between groups using GenAI and those that did not.

## Implementation Guide

**Data Structures:** Discussion posts stored in a database, Cognitive presence coding scheme

**Dependencies:** Epistemic Network Analysis Webkit, Natural Language Processing libraries for text analysis

**Core Operation:**

```python
analyze_cognitive_presence(discussion_posts) -> ENA_visualization
```

**Watch Out For:**

- Ensure proper training on the six-hat technique to avoid confusion during discussions.
- Monitor for overreliance on GenAI to prevent diminished critical thinking.

## Use This When

- You want to enhance cognitive engagement in educational discussions.
- You need to analyze the impact of AI tools on learning outcomes.
- You are developing educational frameworks that integrate structured thinking techniques.

## Don't Use When

- The focus is solely on quantitative performance metrics without cognitive analysis.
- The educational context does not involve collaborative discussions.

## Key Concepts

Cognitive presence, Generative AI, Six-hat thinking, Epistemic Network Analysis, Creativity assessment

## Connects To

- Cognitive Load Theory
- Collaborative Learning Techniques
- AI in Education
- Critical Thinking Frameworks

## Prerequisites

- Understanding of cognitive presence theory
- Familiarity with the six-hat thinking technique
- Basic knowledge of Generative AI

## Limitations

- Findings may not generalize beyond the specific educational context studied.
- The impact of GenAI on cognitive presence may vary significantly among different student populations.

## Open Questions

- How can GenAI be effectively tailored to support low-creativity individuals?
- What additional scaffolding techniques can enhance cognitive presence in diverse learning environments?

## Abstract

We normally think about LLMs (and other AI tools) as equalizers and normalizers. They’re, ostensibly, supposed to help the lower-performing students raise their output to match the more talented kids. Right? Well, no. It doesn’t appear that way at all. This paper is arguing that the real effect is the opposite. Their data is showing that these tools are acting not as an equalizer, but as a cognitive amplifier. They don’t just make everything and everyone better. For each individual they make both your existing strengths and your existing weaknesses louder. Effectively exacerbating specific achievement gaps, not closing them.
