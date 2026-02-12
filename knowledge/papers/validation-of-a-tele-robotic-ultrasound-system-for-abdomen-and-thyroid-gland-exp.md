# Validation of a tele-robotic ultrasound system for abdomen and thyroid gland explorations: a comparison with standard ultrasound

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s13089-025-00408-6` |
| Full Paper | [https://doi.org/10.1186/s13089-025-00408-6](https://doi.org/10.1186/s13089-025-00408-6) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/02dc225c4e92aec853b32767ee4199b106f3bdbb](https://www.semanticscholar.org/paper/02dc225c4e92aec853b32767ee4199b106f3bdbb) |
| Source | [https://journalclub.io/episodes/validation-of-a-tele-robotic-ultrasound-system-for-abdomen-and-thyroid-gland-explorations-a-comparison-with-standard-ultrasound](https://journalclub.io/episodes/validation-of-a-tele-robotic-ultrasound-system-for-abdomen-and-thyroid-gland-explorations-a-comparison-with-standard-ultrasound) |
| Source | [https://www.semanticscholar.org/paper/02dc225c4e92aec853b32767ee4199b106f3bdbb](https://www.semanticscholar.org/paper/02dc225c4e92aec853b32767ee4199b106f3bdbb) |
| Year | 2026 |
| Citations | 4 |
| Authors | A. Antolín, N. Roson, Marina Planes, Mar Castillo, Anna Alberti, Manuel Escobar |
| Paper ID | `11b5689a-3fed-426e-989e-28814e2d2c3f` |

## Classification

- **Problem Type:** medical imaging, telemedicine
- **Domain:** Medical Imaging
- **Sub-domain:** Tele-robotic Ultrasound Systems
- **Technique:** Tele-robotic Ultrasound System
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper validates a 5G-based tele-robotic ultrasound system for abdominal and thyroid gland assessments, demonstrating comparable performance to standard ultrasound techniques. Engineers should care because this technology addresses the shortage of radiologists and improves access to ultrasound services in remote areas.

## Key Contribution

**Validation of a tele-robotic ultrasound system achieving performance parity with standard ultrasound.**

## Problem

The global shortage of radiologists and limited access to ultrasound services in rural areas necessitates innovative solutions for medical imaging.

## Method

**Approach:** The tele-robotic ultrasound system allows remote operation of ultrasound examinations via a robotic arm controlled over a 5G network. The system includes real-time image display and audiovisual communication to facilitate the examination process.

**Algorithm:**

1. 1. Patient is positioned appropriately for the ultrasound examination.
2. 2. The radiologist remotely controls the robotic arm using a console.
3. 3. The robotic arm applies ultrasound probes to the patient's body.
4. 4. Ultrasound images are captured and displayed in real-time.
5. 5. The radiologist communicates with an assistant at the patient site for support.
6. 6. The examination is completed, and findings are recorded.

**Input:** Patient demographic data, ultrasound examination requests, and real-time imaging data.

**Output:** Ultrasound images and diagnostic findings.

**Key Parameters:**

- `robotic_arm_force_range: 3-40 N`
- `minimum_training_patients: 20 for abdominal US`

**Complexity:** not stated

## Benchmarks

**Tested on:** 64 participants (23 male, 41 female) undergoing abdominal and thyroid gland ultrasound examinations.

**Results:**

- mean exploration time for abdominal US: 18.33 ± 6.26 min
- mean exploration time for thyroid US: 4.64 ± 0.97 min

**Compared against:** Standard ultrasound system (Aplio i700 model)

**Improvement:** No statistical differences in performance metrics between tele-robotic and standard ultrasound after training.

## Implementation Guide

**Data Structures:** Patient records database, Ultrasound imaging data storage

**Dependencies:** 5G network infrastructure, robotic control software, ultrasound imaging software

**Core Operation:**

```python
control_robotic_arm(position, pressure); capture_ultrasound_image(); display_image();
```

**Watch Out For:**

- Ensure stable 5G connection to avoid latency issues.
- Train assistants adequately to support the examination process.
- Monitor patient comfort and safety during robotic operations.

## Use This When

- Access to radiologists is limited due to geographic constraints.
- There is a need for remote medical examinations in rural areas.
- A rapid deployment of ultrasound services is required.

## Don't Use When

- High precision imaging is critical and cannot be compromised.
- Patients have severe mobility issues that prevent proper positioning.
- The technology is not yet validated for specific medical conditions.

## Key Concepts

telemedicine, robotic systems, medical imaging, patient satisfaction, learning curve, 5G technology

## Connects To

- Telemedicine frameworks
- Robotic surgery systems
- Remote patient monitoring technologies

## Prerequisites

- Understanding of ultrasound imaging principles
- Familiarity with telecommunication technologies
- Knowledge of robotic control systems

## Limitations

- Dependent on reliable 5G network availability.
- Potential for reduced image quality compared to traditional methods.
- Requires trained personnel for both remote and patient-side operations.

## Open Questions

- What are the long-term effects of using tele-robotic systems on patient outcomes?
- How can the learning curve be further reduced for new operators?

## Abstract

An in-person ultrasound involves a patient lying in various positions to optimally target the organs or body region to be screened. The sonographer holds a transducer, a device that looks like a cross between a universal TV remote and a grocery store check out scanner. The transducer makes contact with the skin, and sends the soundwaves into the body, where they bounce off soft tissues. The echo bounces back and is received by the transducer, which sends that information back to a computer to generate the images. A gel is applied to the region of the body that the scanner will touch to allow smooth movement of the transducer along the skin, and to eliminate any air pockets (between the skin and the device) that might interfere with the sound waves. Some scans can be as short as five minutes, while others can last thirty minutes. That's a lot of time to be in intimate proximity with anyone, let alone someone
