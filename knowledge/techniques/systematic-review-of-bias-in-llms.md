# Systematic Review of Bias in LLMs

*Also known as: Systematic Review of Demographic Biases in Large Language Models*

**This technique systematically reviews literature to evaluate and address demographic biases in large language models (LLMs) in medical contexts.**

**Category:** statistical_method  
**Maturity:** established

## How It Works

The technique involves defining criteria for including studies that assess demographic biases in LLMs. It conducts a comprehensive literature search, screens relevant studies, and extracts data on bias types and mitigation strategies. The quality of the studies is assessed, and findings are synthesized to provide a comprehensive overview of bias in medical LLMs.

## Algorithm

**Input:** Peer-reviewed studies evaluating demographic biases in LLMs applied to medical tasks.

**Output:** A comprehensive overview of bias types, measurement methods, and mitigation strategies in medical LLMs.

**Steps:**

1. 1. Define inclusion criteria for studies evaluating demographic biases in LLMs.
2. 2. Conduct a literature search across multiple databases from January 2018 to July 2024.
3. 3. Screen titles and abstracts for relevance using Rayyan software.
4. 4. Extract data from included studies regarding bias types and mitigation strategies.
5. 5. Assess the quality of studies using JBI Critical Appraisal Tools.
6. 6. Synthesize findings narratively and categorize by bias type and mitigation method.

**Core Operation:** `output = comprehensive overview of bias types + measurement methods + mitigation strategies`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `search_date_range` | January 2018 - July 2024 | Defines the temporal scope of the literature review. |
| `included_studies` | 24 | Indicates the number of studies reviewed for bias evaluation. |
| `bias_types` | gender, racial, ethnic, age, disability, socioeconomic | Specifies the types of demographic biases assessed. |

## Complexity

- **Time:** O(n log n) for sorting and screening studies
- **Space:** O(n) for storing study data
- **In practice:** The complexity is primarily dependent on the number of studies reviewed and the depth of analysis.

## Implementation

```python
def systematic_review_bias(input_data: List[Study]) -> Overview:
    # Step 1: Define inclusion criteria
    # Step 2: Conduct literature search
    # Step 3: Screen studies
    # Step 4: Extract data
    # Step 5: Assess quality
    # Step 6: Synthesize findings
    return overview
```

## Common Mistakes

- Neglecting to define clear inclusion criteria for studies.
- Overlooking the quality assessment of included studies.
- Failing to categorize biases effectively during synthesis.

## Use When

- Developing AI applications in healthcare that utilize LLMs.
- Evaluating existing LLMs for bias before deployment in clinical settings.
- Implementing mitigation strategies to reduce bias in AI outputs.

## Avoid When

- Working with LLMs in non-medical domains where bias is less critical.
- When the application context does not involve demographic considerations.

## Tradeoffs

**Strengths:**

- Provides a comprehensive overview of existing biases.
- Identifies effective mitigation strategies.
- Supports informed decision-making in AI deployment.

**Weaknesses:**

- Time-consuming due to extensive literature review.
- May not capture all emerging biases if studies are limited.
- Dependent on the quality of included studies.

**Compared To:**

- **vs Ad-hoc bias evaluation:** Use systematic review for a thorough understanding; ad-hoc methods may miss critical insights.

## Connects To

- Bias detection algorithms
- Fairness in AI
- Ethical AI frameworks
- Meta-analysis techniques

## Evidence (Papers)

- **Evaluating and addressing demographic disparities in medical large language models: a systematic review** [43 citations] - [DOI](https://doi.org/10.1186/s12939-025-02419-0)
