# Opportunities for retrieval and tool augmented large language models in scientific facilities

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1038/s41524-024-01423-2` |
| Full Paper | [https://doi.org/10.1038/s41524-024-01423-2](https://doi.org/10.1038/s41524-024-01423-2) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/0a42274653199306ddc9fa7d604ccbed58ad8254](https://www.semanticscholar.org/paper/0a42274653199306ddc9fa7d604ccbed58ad8254) |
| Source | [https://journalclub.io/episodes/opportunities-for-retrieval-and-tool-augmented-large-language-models-in-scientific-facilities](https://journalclub.io/episodes/opportunities-for-retrieval-and-tool-augmented-large-language-models-in-scientific-facilities) |
| Source | [https://www.semanticscholar.org/paper/0a42274653199306ddc9fa7d604ccbed58ad8254](https://www.semanticscholar.org/paper/0a42274653199306ddc9fa7d604ccbed58ad8254) |
| Year | 2026 |
| Citations | 42 |
| Authors | Michael H. Prince, Henry Chan, Aikaterini Vriza, Tao Zhou, V. Sastry, Yanqi Luo |
| Paper ID | `bf759451-0c00-4277-b066-8e5409181e42` |

## Classification

- **Problem Type:** AI-assisted experimental planning and operation in scientific facilities
- **Domain:** Machine Learning & AI
- **Sub-domain:** Large Language Models
- **Technique:** Context-Aware Language Model for Science (CALMS)
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents the Context-Aware Language Model for Science (CALMS), which leverages large language models (LLMs) to assist scientists in operating complex scientific instruments and conducting experiments. Engineers should care because CALMS can enhance experimental design and execution, making advanced scientific facilities more accessible and efficient.

## Key Contribution

**Introduction of CALMS, a framework that integrates LLMs with contextual information retrieval and tool usage for scientific experimentation.**

## Problem

The increasing complexity of scientific instruments and experiments makes it challenging for scientists to effectively design and operate experiments.

## Method

**Approach:** CALMS uses a large language model to retrieve relevant information from documentation and assist in instrument operation. It combines conversational memory, semantic search, and tool usage to provide contextual responses to user queries.

**Algorithm:**

1. 1. User inputs a query related to scientific experimentation.
2. 2. The LLM retrieves relevant context from a document store using semantic search.
3. 3. The LLM processes the query along with the retrieved context.
4. 4. If a tool is required, the LLM generates a tool call based on the user input.
5. 5. The tool executes the command and returns results to the LLM.
6. 6. The LLM formulates a response based on the tool output and context.
7. 7. The response is presented to the user.

**Input:** User queries related to scientific experiments and instrument operations.

**Output:** Responses that provide guidance on experimental design, instrument operation, or direct control of scientific tools.

**Key Parameters:**

- `context_window_size: 4096 or 16384 tokens`
- `temperature: 0.7 (for creativity in responses)`
- `top_k: 50 (to limit choices during generation)`
- `top_p: 0.9 (to focus on a subset of predictions)`

**Complexity:** Not stated

## Benchmarks

**Tested on:** User queries related to scientific facilities like APS, CNM, ALCF, CNMS

**Results:**

- relevance, absence of hallucination, completeness

**Compared against:** Responses from GPT-3.5 Turbo and Vicuna without context

**Improvement:** GPT-3.5 Turbo showed better completeness scores compared to Vicuna, with specific scores not quantified.

## Implementation Guide

**Data Structures:** Document store for context retrieval, Vector database for embeddings

**Dependencies:** OpenAI API for GPT-3.5, LangChain for structured input, HuggingFace Transformers for open-source models

**Core Operation:**

```python
response = CALMS(user_query, context_retrieval(document_store), tool_usage())
```

**Watch Out For:**

- Ensure the context provided is relevant to avoid hallucinations.
- Monitor the API call limits and costs associated with LLM usage.
- Be cautious of the LLM's inability to follow strict JSON syntax in tool calls.

## Use This When

- Designing experiments in complex scientific environments.
- Assisting new users in navigating scientific facilities.
- Automating instrument operations based on user queries.

## Don't Use When

- When high accuracy is critical and hallucination risks are unacceptable.
- For tasks requiring extensive domain-specific fine-tuning not covered by the LLM.

## Key Concepts

semantic search, contextual retrieval, tool usage, conversational memory, LLM integration

## Connects To

- OpenAI's GPT-3.5 Turbo
- Vicuna LLM
- HuggingFace Transformers
- LangChain framework
- Retrieval-Augmented Generation (RAG)

## Prerequisites

- Understanding of LLMs and their architectures.
- Familiarity with API integration and tool usage.
- Knowledge of semantic search techniques.

## Limitations

- LLMs may hallucinate answers without proper context.
- Performance may vary significantly between different LLMs.
- Open-source models may not consistently execute complex tool calls.

## Open Questions

- How can we further reduce hallucination rates in LLM responses?
- What additional tools can be integrated to enhance the CALMS framework?

## Abstract

In 1998, NASA launched the Mars Climate Orbiter. The spacecraft was designed to orbit Mars and relay vital atmospheric data back to Earth. For months, the orbiter traveled through space, with mission-control monitoring its progress and making minor adjustments as needed. Anticipation built as the team prepared for the critical moment when the orbiter would enter Mars' orbit. On the scheduled day, engineers gathered together, awaiting confirmation that the spacecraft had successfully positioned itself around Mars. Instead, they were met with an unsettling silence. Attempts to contact the orbiter failed, and it became clear that the Mars Climate Orbiter was lost, its mission ending abruptly as it vanished into the Martian atmosphere.
