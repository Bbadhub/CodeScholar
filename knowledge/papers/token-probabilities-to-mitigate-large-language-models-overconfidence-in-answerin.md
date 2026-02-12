# Token Probabilities to Mitigate Large Language Models Overconfidence in Answering Medical Questions: Quantitative Study

## Access

| Field | Value |
|-------|-------|
| DOI | `10.2196/64348` |
| Full Paper | [https://doi.org/10.2196/64348](https://doi.org/10.2196/64348) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/0c46669b7eb300b4c2e4ce637c8d59177d7a5ead](https://www.semanticscholar.org/paper/0c46669b7eb300b4c2e4ce637c8d59177d7a5ead) |
| Source | [https://journalclub.io/episodes/token-probabilities-to-mitigate-large-language-models-overconfidence-in-answering-medical-questions-quantitative-study](https://journalclub.io/episodes/token-probabilities-to-mitigate-large-language-models-overconfidence-in-answering-medical-questions-quantitative-study) |
| Source | [https://www.semanticscholar.org/paper/0c46669b7eb300b4c2e4ce637c8d59177d7a5ead](https://www.semanticscholar.org/paper/0c46669b7eb300b4c2e4ce637c8d59177d7a5ead) |
| Year | 2026 |
| Citations | 8 |
| Authors | Raphaël Bentegeac, Bastien Le Guellec, G. Kuchcinski, Philippe Amouyel, A. Hamroun |
| Paper ID | `86690ff7-37b3-4497-859e-572ea2d2adab` |

## Classification

- **Problem Type:** confidence estimation in natural language processing
- **Domain:** Natural Language Processing
- **Sub-domain:** Large Language Models
- **Technique:** Token Probability Analysis
- **Technique Category:** statistical_method
- **Type:** comparison

## Summary

This study evaluates the predictive capabilities of token probabilities versus expressed confidence in large language models (LLMs) when answering medical questions. Engineers should care because it provides insights into improving the reliability of chatbot responses in clinical settings by leveraging internal probability metrics.

## Key Contribution

**Token probabilities significantly outperform expressed confidence in predicting the accuracy of LLM responses to medical questions.**

## Problem

The overconfidence of chatbots in providing medical answers can lead to misinformation and potential health risks.

## Method

**Approach:** The method involves prompting various LLMs to answer medical questions while extracting both their expressed confidence and the token probabilities of their responses. The predictive performance of these metrics is then evaluated against actual response accuracy.

**Algorithm:**

1. Select a set of LLMs that provide access to internal probabilities.
2. Prompt each model with a medical question and request a confidence rating.
3. Extract the token probability for the chosen answer from the model's output.
4. Evaluate the accuracy of the model's response.
5. Compare the predictive performance of expressed confidence and token probabilities using statistical metrics.

**Input:** Medical questions from datasets such as the USMLE MedQA database.

**Output:** Predicted accuracy of responses based on token probabilities and expressed confidence.

**Key Parameters:**

- `temperature: 0 (to mitigate variability)`
- `prompting_strategy: vanilla prompting`
- `confidence_scale: 0 to 100`

**Complexity:** Not stated

## Benchmarks

**Tested on:** USMLE MedQA (n=2522), MedMCQA (n=2797), MedQA Mainland China (n=3413), MedQA Taiwan (n=2808), FrMedMCQA (n=1079)

**Results:**

- accuracy: ranged from 56.5% (Phi-3-Mini) to 89% (GPT-4o)
- AUROC for expressed confidence: ranged from 0.52 (Phi-3-Mini) to 0.68 (GPT-4o)
- AUROC for token probability: ranged from 0.71 (Phi-3-Mini) to 0.87 (GPT-4o)

**Compared against:** Expressed confidence levels of the models, Previous studies on confidence estimation

**Improvement:** Token probabilities showed a marked improvement over expressed confidence, with AUROCs significantly higher (all P<.001).

## Implementation Guide

**Data Structures:** Data structures to store model responses and their corresponding probabilities., Statistical data structures for performance evaluation.

**Dependencies:** OpenAI API for accessing GPT models, Microsoft Azure API for accessing other models, Statistical libraries in R and Python for analysis

**Core Operation:**

```python
response = model.predict(question); confidence = model.get_confidence(); token_prob = model.get_token_probability(response); evaluate_accuracy(response, correct_answer)
```

**Watch Out For:**

- Ensure models used provide access to log probabilities.
- Be cautious of overconfidence in smaller models.
- Sensitivity analyses may yield varying results based on prompting strategies.

## Use This When

- Building medical chatbots that require reliable confidence estimation.
- Evaluating the performance of LLMs in clinical settings.
- Improving decision-making processes in healthcare applications.

## Don't Use When

- The application does not require high-stakes decision-making.
- When using models that do not provide access to internal probabilities.
- In scenarios where expressed confidence is sufficient.

## Key Concepts

token probabilities, expressed confidence, receiver operating characteristic, calibration error, Brier score, sensitivity analysis

## Connects To

- Confidence calibration techniques
- Other metrics for evaluating model performance
- Statistical methods for predictive analysis

## Prerequisites

- Understanding of LLMs and their architectures.
- Familiarity with statistical evaluation metrics.
- Knowledge of natural language processing techniques.

## Limitations

- Models may still exhibit overconfidence despite using token probabilities.
- Performance may vary across different languages and datasets.
- Limited generalizability to non-medical domains.

## Open Questions

- How can token probabilities be further refined for better calibration?
- What are the implications of these findings for non-medical applications of LLMs?

## Abstract

When an LLM generates a response, they're not just spitting out words. Under the hood, they're running a process that assigns probabilities to every possible word or symbol that they might produce next. So when you give it a multiple-choice question, the model has to choose between specific answer tokens. The internal probability it assigns to its chosen answer is a window into how certain the model actually is, based on its training and the patterns it learned. But here's the issue: this internal mathematical certainty is actually completely separate from what the model says about its own confidence when asked. In this study they’re comparing and contrasting two things: how confident the model truly is vs how confident it says that it is. That was why they needed to stick with models that provided access to their internal probability calculations. Without that, they wouldn’t be able to make those comparisons.
