# Reliever Reliance Test (RRT)

**The RRT evaluates patients' reliance on short-acting beta-agonists (SABA) and provides personalized feedback to improve asthma management.**

**Category:** healthcare_assessment  
**Maturity:** emerging

## How It Works

The RRT uses the SABA Reliance Questionnaire (SRQ) to assess how much patients depend on SABA for asthma control. Patients complete the questionnaire online, which consists of five items scored on a Likert scale. Based on their responses, the tool classifies their risk of over-reliance on SABA and offers tailored feedback and recommendations to encourage better asthma management discussions with healthcare professionals.

## Algorithm

**Input:** Responses to the SABA Reliance Questionnaire (SRQ), which includes 5 items scored on a Likert scale.

**Output:** Risk classification (low, medium, high) and personalized feedback regarding SABA use.

**Steps:**

1. 1. Patient completes the RRT online.
2. 2. Calculate the SRQ score based on responses to 5 items.
3. 3. Classify the risk of SABA over-reliance as low, medium, or high based on the SRQ score.
4. 4. Provide personalized feedback and recommendations based on the risk classification.
5. 5. Encourage patients to discuss their treatment with healthcare professionals.

**Core Operation:** `Risk classification = classify(SRQ score)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `SRQ items` | 5-item scale | Affects the accuracy of the risk classification. |
| `Risk classification thresholds` | low (<10), medium (11-17), high (18-25) | Determines how patients are categorized based on their reliance on SABA. |

## Complexity

- **Time:** O(1) for scoring and classification
- **Space:** O(1) for storing responses and classifications
- **In practice:** The method is straightforward and quick, requiring minimal computational resources.

## Implementation

```python
def reliever_reliance_test(responses: List[int]) -> Tuple[str, str]:
    srq_score = sum(responses)
    risk_classification = classify(srq_score)
    feedback = generate_feedback(risk_classification)
    return risk_classification, feedback
```

## Common Mistakes

- Failing to ensure patients understand the questionnaire items.
- Not providing adequate follow-up after risk classification.
- Overlooking the importance of digital literacy for online completion.

## Use When

- Patients exhibit high reliance on SABA for asthma management.
- There is a need to educate patients about the risks of SABA overuse.
- Healthcare professionals want to facilitate discussions about asthma treatment options.

## Avoid When

- Patients are already well-controlled on their asthma treatment.
- Patients have limited access to alternative asthma treatments.
- Patients are not digitally literate and cannot complete the RRT online.

## Tradeoffs

**Strengths:**

- Provides personalized feedback to patients.
- Encourages proactive discussions about asthma management.
- Simple and quick to implement.

**Weaknesses:**

- Relies on patients' self-reporting, which may be biased.
- May not be suitable for all patient demographics.
- Limited effectiveness if patients are not engaged.

**Compared To:**

- **vs traditional asthma management assessments:** RRT offers a more interactive and personalized approach.

## Connects To

- SABA Reliance Questionnaire (SRQ)
- Asthma management plans
- Patient education tools
- Digital health interventions

## Evidence (Papers)

- **The Reliever Reliance Test: evaluating a new tool to address SABA over-reliance** - [DOI](https://doi.org/10.1038/s41533-024-00389-4)
