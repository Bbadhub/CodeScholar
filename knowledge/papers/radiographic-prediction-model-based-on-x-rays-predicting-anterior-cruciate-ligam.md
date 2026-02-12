# Radiographic prediction model based on X-rays predicting anterior cruciate ligament function in patients with knee osteoarthritis

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s42492-025-00195-w` |
| Full Paper | [https://doi.org/10.1186/s42492-025-00195-w](https://doi.org/10.1186/s42492-025-00195-w) |
| Source | [https://journalclub.io/episodes/radiographic-prediction-model-based-on-x-rays-predicting-anterior-cruciate-ligament-function-in-patients-with-knee-osteoarthritis](https://journalclub.io/episodes/radiographic-prediction-model-based-on-x-rays-predicting-anterior-cruciate-ligament-function-in-patients-with-knee-osteoarthritis) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `afbe1a19-9638-4ea3-8b53-a80b593630a3` |

## Classification

- **Problem Type:** binary classification of ACL function (functional vs. dysfunctional)
- **Domain:** Bioinformatics & Health
- **Sub-domain:** Orthopedic Imaging
- **Technique:** Radiographic prediction model
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This paper presents a radiographic prediction model that utilizes X-ray images to assess the functional status of the anterior cruciate ligament (ACL) in patients with knee osteoarthritis (KOA). This model is crucial for guiding surgical decisions, particularly between unicompartmental knee arthroplasty (UKA) and total knee arthroplasty (TKA), based on whether the ACL is functionally competent.

## Key Contribution

**Development of a nomogram-based prediction model for ACL function using radiographic features from X-ray images in KOA patients.**

## Problem

The need for accurate assessment of ACL function in patients with knee osteoarthritis to inform surgical treatment decisions.

## Method

**Approach:** The method involves extracting specific radiographic features from X-ray images and using least absolute shrinkage and selection operator (LASSO) regression to identify significant predictors of ACL function. A logistic regression model is then constructed to predict ACL function, visualized through a nomogram.

**Algorithm:**

1. 1. Collect preoperative X-ray images from KOA patients.
2. 2. Extract relevant radiographic features (e.g., wear depth, tibial slope).
3. 3. Apply LASSO regression to select significant predictors.
4. 4. Use logistic regression to model the relationship between predictors and ACL function.
5. 5. Construct a nomogram to visualize the prediction model.
6. 6. Validate the model using ROC analysis and calibration curves.

**Input:** Preoperative X-ray images (anteroposterior, lateral, full-length lower limbs) of KOA patients.

**Output:** Probability of ACL function (functional or dysfunctional) represented in a nomogram.

**Key Parameters:**

- `lambda (LASSO regression): chosen to have one standard error`
- `cutoff values: position (anterior-middle), depth of wear (D2 > 1.40 mm), posterior tibial slope (PTS > 7.90°), static anterior tibial translation (SATT > 4.49 mm)`

**Complexity:** Not stated

## Benchmarks

**Tested on:** 272 KOA patients' X-ray images

**Results:**

- AUC: 0.831 (training), 0.907 (validation)
- Sensitivity: 88.4% (training), 86.1% (validation)
- Specificity: 63.8% (training), 82.2% (validation)

**Compared against:** Previous radiographic studies with smaller sample sizes

**Improvement:** Significant improvement in predictive accuracy over previous methods.

## Implementation Guide

**Data Structures:** X-ray image data, radiographic feature vectors

**Dependencies:** R (version 4.4), Picture Archiving and Communication System (PACS)

**Core Operation:**

```python
predicted_probability = 1 / (1 + exp(-(-11.985 + 0.967 * position + 1.420 * D2 + 0.833 * SATT + 0.688 * PTS)))
```

**Watch Out For:**

- Ensure accurate measurement of radiographic features to avoid misclassification.
- Be cautious of the sample size and validation cohort to ensure model reliability.
- Consider the limitations of the model when applying it to different patient populations.

## Use This When

- You need to assess ACL function in KOA patients preoperatively.
- You want to guide surgical decisions between UKA and TKA based on ACL viability.
- You are looking for a method to utilize X-ray images for functional assessments.

## Don't Use When

- You require direct visualization of ACL morphology.
- You are dealing with acute ACL injuries where MRI is more appropriate.
- You have a patient population outside of KOA with K-L grades III to IV.

## Key Concepts

LASSO regression, logistic regression, nomogram, radiographic features, ACL function prediction

## Connects To

- MRI assessment of ACL injuries
- other predictive modeling techniques
- radiographic analysis methods

## Prerequisites

- Understanding of radiographic imaging
- Basic knowledge of regression analysis
- Familiarity with clinical decision-making in orthopedic surgery

## Limitations

- Limited to patients with K-L grades III to IV.
- Does not directly visualize ACL morphology.
- Potential for misclassification based on radiographic interpretation.

## Open Questions

- How can this model be adapted for use in other populations or grades of KOA?
- What additional radiographic features could improve the predictive accuracy?

## Abstract

The ACL is often treated as a binary variable in surgical planning: either intact or torn. But in patients with end-stage knee osteoarthritis, that distinction isn't enough. What actually matters is whether the ligament is functionally competent. That is, can it still stabilize the tibia under load. And that’s not something most imaging tools are built to answer. MRI can show gross morphological changes, but its signal is confounded by degenerative remodeling, fluid artifacts, and partial volume effects. It can report a ligament as "torn" when it's merely degenerated, or as "intact" when it’s functionally lax. In other words, MRI is sensitive to structure, but not to performance. That matters because treatment decisions hinge on functional status. The clinical pathway diverges depending on whether the ACL is still doing its job. In particular, surgeons deciding between UKA and TKA need to know if the ACL is viable. UKA preserves both cruciate ligaments and requires an intact kinematic chain. If the ACL is compromised, UKA is contraindicated. In those cases, TKA is the default. Getting this wrong leads to failed implants, revisions, and poor outcomes.
