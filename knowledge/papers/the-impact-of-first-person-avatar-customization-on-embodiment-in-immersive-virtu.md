# The impact of first-person avatar customization on embodiment in immersive virtual reality

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/frvir.2024.1436752` |
| Full Paper | [https://doi.org/10.3389/frvir.2024.1436752](https://doi.org/10.3389/frvir.2024.1436752) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/c65a5dc8b077c7c16c459b1aba70c92c20368c63](https://www.semanticscholar.org/paper/c65a5dc8b077c7c16c459b1aba70c92c20368c63) |
| Source | [https://journalclub.io/episodes/the-impact-of-first-person-avatar-customization-on-embodiment-in-immersive-virtual-reality](https://journalclub.io/episodes/the-impact-of-first-person-avatar-customization-on-embodiment-in-immersive-virtual-reality) |
| Source | [https://www.semanticscholar.org/paper/c65a5dc8b077c7c16c459b1aba70c92c20368c63](https://www.semanticscholar.org/paper/c65a5dc8b077c7c16c459b1aba70c92c20368c63) |
| Year | 2026 |
| Citations | 10 |
| Authors | Mar González-Franco, Anthony Steed, Christopher C. Berger, Ana Tajadura-Jiménez |
| Paper ID | `447af409-8949-40e4-8a4b-f82ea2387daa` |

## Classification

- **Problem Type:** embodiment in virtual reality
- **Domain:** Human-Computer Interaction
- **Sub-domain:** Virtual Reality and Avatar Customization
- **Technique:** First-Person Avatar Customization
- **Technique Category:** framework
- **Type:** novel

## Summary

This paper investigates the impact of first-person avatar customization on the sense of embodiment in immersive virtual reality (VR) and its potential to reduce implicit biases towards larger-sized individuals. Engineers should care because the findings suggest that first-person customization can enhance user experience and promote social change through VR applications.

## Key Contribution

**The introduction of a first-person avatar customization mechanism that enhances embodiment and reduces implicit bias compared to third-person customization.**

## Problem

The need to enhance user experience and reduce implicit biases in virtual environments through effective avatar customization.

## Method

**Approach:** Participants customize their avatars from a first-person perspective by grabbing and pulling their avatar to resize it, as opposed to using sliders in a third-person perspective. This method is hypothesized to increase the sense of embodiment and reduce biases.

**Algorithm:**

1. 1. User dons VR headset and controllers.
2. 2. User selects avatar customization mode (first-person or third-person).
3. 3. In first-person mode, user grabs their avatar and pulls to resize it.
4. 4. In third-person mode, user adjusts sliders to modify avatar size.
5. 5. User engages in a game to enhance embodiment.
6. 6. User completes questionnaires to assess embodiment and implicit bias.

**Input:** User's interactions with the avatar (grabbing and pulling or slider adjustments), and the avatar's blend shape parameters.

**Output:** Customized avatar with modified embodiment levels and implicit bias measurements.

**Key Parameters:**

- `upper_body_size: [0, 1]`
- `lower_body_size: [0, 1]`

**Complexity:** not stated

## Benchmarks

**Tested on:** Implicit Association Test (IAT) results from participants' responses.

**Results:**

- Embodiment scores from questionnaires, implicit bias scores from IAT.

**Compared against:** Third-person avatar customization results.

**Improvement:** First-person customization led to higher embodiment scores and reduced implicit bias compared to third-person customization.

## Implementation Guide

**Data Structures:** Avatar model with blend shapes for size adjustments., User input handling for VR controllers.

**Dependencies:** Unity3D, HTC VIVE SDK, Final IK animation system

**Core Operation:**

```python
if user_mode == 'first_person': grab_avatar(); else: adjust_sliders();
```

**Watch Out For:**

- Ensure accurate tracking of user movements to avoid disembodiment.
- Balance avatar customization options to prevent overwhelming users.
- Test for user comfort with avatar sizes to avoid negative experiences.

## Use This When

- Developing VR applications focused on user representation and identity.
- Creating training simulations that require high levels of user engagement.
- Designing social VR platforms that aim to reduce biases.

## Don't Use When

- The application does not require a strong sense of presence or embodiment.
- The target audience is not engaged in social interactions.
- Customization complexity is not feasible for the intended user base.

## Key Concepts

embodiment, avatar customization, implicit bias, virtual reality, user agency

## Connects To

- Avatar representation techniques
- Bias reduction strategies
- User experience design in VR

## Prerequisites

- Understanding of VR development
- Familiarity with user experience principles
- Knowledge of implicit bias concepts

## Limitations

- Limited to male participants in the study
- Results may not generalize across different demographics
- Customization may not be suitable for all VR applications

## Open Questions

- How can this approach be adapted for diverse user populations?
- What long-term effects does embodiment have on user behavior outside of VR?

## Abstract

In the world of virtual reality, developers and designers care a lot about something called "embodiment". Embodiment is the feeling or sensation that you’re "in" the character/avatar that you're playing. You are the avatar. You have agency, you have ownership. You have what’s referred to as "visual-motor congruence", and you feel accurately represented by the avatar in the virtual universe. Remember that scene in the Matrix when Neo wants to learn Kung Fu? They plug him into the simulation, and suddenly he’s in a room with Morpheus training and fighting. Well, in that moment Neo knows that what he's experiencing is a simulation, but that's counteracted by the fact that he has “high embodiment” in his avatar. It’s not his actual body, but in a way, it is. He’s not really in that room, but in a way, he is. That's embodiment.
