# A virtual reality intervention to reduce death anxiety and stress in adults: examining the effect of a near-death experience simulation

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/frvir.2025.1644131` |
| Full Paper | [https://doi.org/10.3389/frvir.2025.1644131](https://doi.org/10.3389/frvir.2025.1644131) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/53166e5c698d4ff9f98d0d10e8bfabfaca2ce463](https://www.semanticscholar.org/paper/53166e5c698d4ff9f98d0d10e8bfabfaca2ce463) |
| Source | [https://journalclub.io/episodes/a-virtual-reality-intervention-to-reduce-death-anxiety-and-stress-in-adults-examining-the-effect-of-a-near-death-experience-simulation](https://journalclub.io/episodes/a-virtual-reality-intervention-to-reduce-death-anxiety-and-stress-in-adults-examining-the-effect-of-a-near-death-experience-simulation) |
| Source | [https://www.semanticscholar.org/paper/53166e5c698d4ff9f98d0d10e8bfabfaca2ce463](https://www.semanticscholar.org/paper/53166e5c698d4ff9f98d0d10e8bfabfaca2ce463) |
| Year | 2026 |
| Citations | 0 |
| Authors | Parya Khandan, Benjamin Ennemoser, Ryan D. Foster, Logan Dubose, Zhipeng Lu |
| Paper ID | `c0b595fc-ed97-4751-98a6-d5e3fa681b52` |

## Classification

- **Problem Type:** psychological intervention for anxiety reduction
- **Domain:** Human-Computer Interaction
- **Sub-domain:** Virtual Reality Therapy
- **Technique:** VR NDE Simulation
- **Technique Category:** framework
- **Type:** novel

## Summary

This paper presents a virtual reality (VR) intervention designed to reduce death anxiety (DA) and stress in adults through a near-death experience (NDE) simulation. Engineers should care because it demonstrates a novel application of VR technology in psychological interventions, potentially offering a scalable solution for mental health challenges.

## Key Contribution

**The introduction of an immersive VR NDE simulation as an effective intervention for reducing death anxiety and stress in adults.**

## Problem

The work addresses the significant psychological challenges posed by death anxiety and stress, which negatively impact health and wellbeing.

## Method

**Approach:** The method involves participants experiencing a first-person VR simulation of a near-death experience, which includes immersive scenes commonly reported in NDEs. Participants complete pre- and post-intervention questionnaires to assess changes in death anxiety and stress levels.

**Algorithm:**

1. 1. Recruit participants aged 18 and older.
2. 2. Administer pre-intervention questionnaires measuring death anxiety and perceived stress.
3. 3. Participants engage in an 11-minute VR NDE simulation using Oculus Quest 2.
4. 4. Administer post-intervention questionnaires to measure changes in death anxiety and stress.
5. 5. Analyze data using statistical methods to compare pre- and post-intervention scores.

**Input:** Participants' responses to pre-intervention questionnaires measuring death anxiety and perceived stress.

**Output:** Post-intervention scores on death anxiety and perceived stress, along with qualitative feedback on the VR experience.

**Key Parameters:**

- `simulation_duration: 11 minutes`
- `sample_size: 61 participants`
- `questionnaire_items: PSQ (30 items), DAS (15 items)`

**Complexity:** not stated

## Benchmarks

**Tested on:** Pre- and post-intervention questionnaire responses from 61 participants.

**Results:**

- Death Anxiety (DA) scores: pre-intervention mean = 8.57, post-intervention mean = 7.00
- Perceived Stress scores: pre-intervention mean = 0.469, post-intervention mean = 0.396

**Compared against:** Pre-intervention scores for DA and perceived stress.

**Improvement:** Significant reduction in DA (Δmean = 1.566, p < 0.001) and perceived stress (Δmean = 0.073, p = 0.002).

## Implementation Guide

**Data Structures:** Participant data records, Questionnaire response arrays

**Dependencies:** Oculus Quest 2 SDK, Statistical analysis software (e.g., SPSS)

**Core Operation:**

```python
def run_vr_experience(participant): administer_pre_questionnaire(participant); launch_vr_simulation(); administer_post_questionnaire(participant);
```

**Watch Out For:**

- Ensure participants are screened for comfort with VR and death-related topics.
- Monitor for adverse reactions during the VR experience.
- Provide clear instructions on using VR equipment.

## Use This When

- Developing VR applications for mental health interventions.
- Addressing anxiety related to mortality in therapeutic settings.
- Creating immersive experiences for psychological exposure therapy.

## Don't Use When

- Participants have severe mental health conditions that may be exacerbated by VR experiences.
- The target population is not comfortable with death-related topics.
- High levels of pre-existing death anxiety may lead to adverse effects.

## Key Concepts

virtual reality, death anxiety, stress reduction, near-death experience, psychological interventions, immersive technology

## Connects To

- Exposure therapy techniques
- Other VR-based therapeutic interventions
- Cognitive Behavioral Therapy (CBT) methods

## Prerequisites

- Understanding of VR technology and its applications in therapy.
- Knowledge of psychological principles related to anxiety and stress.
- Familiarity with statistical analysis methods for intervention studies.

## Limitations

- Potential for increased anxiety in a subset of participants (26.7% experienced increased DA).
- Sample may not represent broader populations due to self-selection bias.
- Limited generalizability due to the homogeneous sample of university students.

## Open Questions

- What are the effects of simulating negative or hellish NDEs in VR?
- How can VR NDE simulations be personalized to enhance effectiveness?

## Abstract

Now, if it were any other fear, exposure therapy might be an option. You gradually and safely expose someone to the thing they're afraid of. It works really well for most anxieties. Afraid of spiders? We can show you pictures of them, then put you in a room with a spider in a jar, and eventually work up to holding one.
