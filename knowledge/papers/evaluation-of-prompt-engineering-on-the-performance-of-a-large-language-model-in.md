# Evaluation of Prompt Engineering on the Performance of a Large Language Model in Document Information Extraction

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/electronics14112145` |
| Full Paper | [https://doi.org/10.3390/electronics14112145](https://doi.org/10.3390/electronics14112145) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/90ee82527d6979dda97370f90b1c14764d4c8f37](https://www.semanticscholar.org/paper/90ee82527d6979dda97370f90b1c14764d4c8f37) |
| Source | [https://journalclub.io/episodes/evaluation-of-prompt-engineering-on-the-performance-of-a-large-language-model-in-document-information-extraction](https://journalclub.io/episodes/evaluation-of-prompt-engineering-on-the-performance-of-a-large-language-model-in-document-information-extraction) |
| Source | [https://www.semanticscholar.org/paper/90ee82527d6979dda97370f90b1c14764d4c8f37](https://www.semanticscholar.org/paper/90ee82527d6979dda97370f90b1c14764d4c8f37) |
| Year | 2026 |
| Citations | 4 |
| Authors | Lun-Chi Chen, Hsin-Tzu Weng, M. Pardeshi, Chien-Ming Chen, Ruey-Kai Sheu, Kai-Chih Pai |
| Paper ID | `a08aeeed-0594-4a0a-b22b-e00c92ed432e` |

## Classification

- **Problem Type:** document information extraction
- **Domain:** Machine Learning & AI
- **Sub-domain:** Prompt Engineering, Document Processing
- **Technique:** Applied Key Information Extraction (KIE)
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a prompt-based key information extraction (KIE) pipeline that integrates large language models (LLMs) with Amazon Textract for efficient document information extraction from heterogeneous formats like invoices. Engineers should care because it offers a low-cost, high-accuracy solution for automating data extraction, which is crucial for processing large volumes of documents in real-world applications.

## Key Contribution

**A novel applied KIE pipeline that combines OCR with LLMs to automate and enhance document information extraction accuracy.**

## Problem

The need to automate the extraction of key information from diverse and unstructured document formats, such as invoices, which are challenging to process manually.

## Method

**Approach:** The method utilizes Amazon Textract for initial OCR processing to extract text and layout data from documents. This data is then structured using user-defined prompts and processed through an LLM to produce a final structured JSON output.

**Algorithm:**

1. Input a PDF document and prompt instruction.
2. Use Amazon Textract to extract textual and structural data.
3. Create a configuration table for field schema, unit definitions, and special formats.
4. Process the OCR-extracted content with a user-defined prompt to structure the data.
5. Feed the structured prompt into an LLM for final JSON output.
6. Implement a rule-based post-processing module for specific fields.
7. Filter results and calculate confidence scores.
8. Handle user queries to extract targeted information.

**Input:** PDF document containing heterogeneous data (e.g., invoices).

**Output:** Structured JSON output containing extracted key information.

**Key Parameters:**

- `OCR tool: Amazon Textract`
- `Anonymization package: anonymizedf (version 1.0.1)`
- `Field schema: user-defined`
- `Confidence score calculation: predefined formula`

**Complexity:** not stated

## Benchmarks

**Tested on:** SROIE dataset, Invoice dataset from a Taiwanese shipping company

**Results:**

- average precision: 95.5% on SROIE
- document information extraction accuracy: 91.5% on SROIE
- average precision: 97.15% on Taiwanese invoice dataset
- document information extraction accuracy: 85.29% on Taiwanese invoice dataset

**Compared against:** Standard OCR methods, NER-based methods

**Improvement:** Significant improvement in accuracy compared to traditional methods.

## Implementation Guide

**Data Structures:** JSON for structured output, Configuration table for field definitions

**Dependencies:** Amazon Textract, Python package: anonymizedf

**Core Operation:**

```python
output_json = LLM.process(prompt + OCR_output)
```

**Watch Out For:**

- Ensure proper configuration of field schemas to match document formats.
- Handle OCR noise effectively to improve extraction accuracy.
- Be cautious with sensitive data and ensure anonymization is applied.

## Use This When

- You need to automate data extraction from invoices or receipts.
- You are dealing with heterogeneous document formats.
- You require high accuracy in information extraction with minimal training data.

## Don't Use When

- You have a fixed format for all documents.
- You require real-time processing without any preprocessing.
- You need to extract information from highly structured documents.

## Key Concepts

prompt engineering, key information extraction, Optical Character Recognition, large language models, data normalization, JSON structuring

## Connects To

- Optical Character Recognition (OCR)
- Natural Language Processing (NLP)
- Data Normalization Techniques
- Large Language Models (LLMs)
- Information Retrieval Systems

## Prerequisites

- Understanding of OCR technologies
- Familiarity with JSON data structures
- Knowledge of prompt engineering techniques

## Limitations

- Performance may degrade with highly noisy or poorly formatted documents.
- Requires initial setup and configuration for different document types.
- May not perform well with documents that have fixed formats.

## Open Questions

- How can the system be adapted for real-time processing?
- What additional features can enhance the robustness of the extraction process?

## Abstract

Data extraction seems easy and straightforward, until you try it at scale. Because it’s only at scale that all the corner cases and variations, and version-changes and schema updates start to reveal themselves. For example: imagine that your task is to build a system that can pull data from a pile of invoices. But that pile is heterogenous, no two invoices are exactly alike. At the bottom of one invoice it says “Amount Due” The bottom of another says “Total”. A third says “Final Cost - Unpaid” at the top, and the fourth just has an unlabeled line item below a table.
