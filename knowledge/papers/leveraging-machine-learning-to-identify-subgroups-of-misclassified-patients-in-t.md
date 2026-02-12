# Leveraging Machine Learning to Identify Subgroups of Misclassified Patients in the Emergency Department: Multicenter Proof-of-Concept Study

## Access

| Field | Value |
|-------|-------|
| DOI | `10.2196/56382` |
| Full Paper | [https://doi.org/10.2196/56382](https://doi.org/10.2196/56382) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/c54335c9a411ada37d9a60f7afcfec79015c7021](https://www.semanticscholar.org/paper/c54335c9a411ada37d9a60f7afcfec79015c7021) |
| Source | [https://journalclub.io/episodes/leveraging-machine-learning-to-identify-subgroups-of-misclassified-patients-in-the-emergency-department-multicenter-proof-of-concept-study](https://journalclub.io/episodes/leveraging-machine-learning-to-identify-subgroups-of-misclassified-patients-in-the-emergency-department-multicenter-proof-of-concept-study) |
| Source | [https://www.semanticscholar.org/paper/c54335c9a411ada37d9a60f7afcfec79015c7021](https://www.semanticscholar.org/paper/c54335c9a411ada37d9a60f7afcfec79015c7021) |
| Year | 2026 |
| Citations | 3 |
| Authors | S. Wyatt, Dagfinn Lunde Markussen, Mounir Haizoune, Anders Strand Vestbø, Y. Sima, Maria Ilene Sandboe |
| Paper ID | `4455a572-ae4d-49ee-832b-7f290edf9e52` |

## Classification

- **Problem Type:** classification
- **Domain:** Machine Learning & AI
- **Sub-domain:** Classification models in healthcare
- **Technique:** Random Forest, XGBoost
- **Technique Category:** classification_model
- **Type:** comparison

## Summary

This study demonstrates how machine learning can identify subgroups of patients who are misclassified in emergency department triage systems, aiming to reduce adverse outcomes from undertriage and optimize resource allocation. Engineers should care because this approach can enhance patient care and improve the efficiency of healthcare delivery systems.

## Key Contribution

**The use of machine learning to identify clinical features associated with triage misclassification in emergency departments.**

## Problem

The misclassification of patients in emergency departments can lead to inadequate care or resource wastage.

## Method

**Approach:** The method uses retrospective cohort data from two hospitals to train classification models that identify features associated with undertriage and overtriage. Machine learning algorithms, specifically Random Forest and XGBoost, are employed to capture nonlinear relationships and assess variable importance using SHAP values.

**Algorithm:**

1. 1. Collect retrospective cohort data from emergency departments.
2. 2. Define target variables for undertriage and overtriage.
3. 3. Preprocess data, including handling missing values and categorical data.
4. 4. Train Random Forest and XGBoost models on the dataset.
5. 5. Optimize model parameters using GridSearch.
6. 6. Evaluate model performance using ROC curves.
7. 7. Analyze feature importance using SHAP values.

**Input:** Patient records including triage score, age, sex, arrival time, clinical referral department, reason for emergency contact, discharge location, level of care, and time of death.

**Output:** Classification of patients into undertriaged or overtriaged categories.

**Key Parameters:**

- `class_weight: adjusted for unbalanced data`
- `SMOTE: applied for oversampling minority classes`
- `n_estimators: default values for Random Forest and XGBoost`
- `max_depth: tuned during GridSearch`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Bergen University Hospital: 205,488 patient records, Trondheim University Hospital: 304,997 patient records

**Results:**

- ROC AUC for Random Forest (Bergen): 0.79
- ROC AUC for XGBoost (Trondheim): 0.78

**Compared against:** Logistic Regression, Decision Tree Classifier

**Improvement:** Random Forest outperformed Logistic Regression with an AUC of 0.79 compared to 0.78.

## Implementation Guide

**Data Structures:** DataFrame for patient records, Dictionary for SHAP values

**Dependencies:** scikit-learn, XGBoost, pandas, numpy

**Core Operation:**

```python
model = RandomForestClassifier().fit(X_train, y_train)
```

**Watch Out For:**

- Ensure data is preprocessed correctly to handle missing values.
- Be cautious of overfitting when tuning model parameters.
- Monitor for class imbalance and apply SMOTE appropriately.

## Use This When

- You need to analyze patient data to improve triage accuracy.
- You want to identify factors contributing to misclassification in emergency departments.
- You are working on healthcare applications that require classification of patient urgency.

## Don't Use When

- Data availability is limited or lacks granularity.
- You require real-time triage decision-making without historical data.
- The problem does not involve classification or triage.

## Key Concepts

triage systems, machine learning, classification, SHAP values, undertriage, overtriage, feature importance

## Connects To

- Logistic Regression
- Decision Trees
- Support Vector Machines
- Neural Networks
- SHAP for interpretability

## Prerequisites

- Understanding of machine learning classification techniques.
- Familiarity with data preprocessing methods.
- Knowledge of healthcare data and triage systems.

## Limitations

- Data was collected from only two hospitals, limiting generalizability.
- Lack of detailed clinical parameters may affect model accuracy.
- Temporal changes in data collection methods may impact results.

## Open Questions

- How can this approach be adapted for real-time triage systems?
- What additional clinical parameters could improve model performance?

## Abstract

RETTS was developed in Sweden in the early 2000s, and is a structured and evidence-based triage model designed for high-resource healthcare settings. RETTS categorizes patients based on a combination of both vital signs and clinical symptoms. When they arrive at the ER, patients undergo an initial assessment of a few key physiological parameters (like heart rate, respiratory rate, blood pressure, oxygen saturation, and temperature). These values are then cross-referenced with a rubric called Emergency Symptoms and Signs (ESS). ESS provides guidelines for interpreting the clinical context of the patient's presentation. The system assigns patients into one of five urgency levels. Each urgency level is designated as a specific color, and is mapped to a recommended maximum waiting time. There is: Red (immediate care), Orange (20 minutes), Yellow
