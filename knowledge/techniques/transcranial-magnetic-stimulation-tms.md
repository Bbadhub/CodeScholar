# Transcranial Magnetic Stimulation (TMS)

*Also known as: TMS*

**TMS is a non-invasive method used to stimulate neural activity in the brain using magnetic fields.**

**Category:** neural_stimulation  
**Maturity:** proven (widely used in production)

## How It Works

TMS involves placing a magnetic coil on the scalp, which generates brief magnetic pulses that induce electrical currents in the brain. This stimulation can enhance or inhibit neuronal activity, depending on the frequency and duration of the pulses. It is particularly useful for modulating brain regions associated with specific functions, such as reward processing in opioid users.

## Algorithm

**Input:** Data on opioid users' brain activity and reward response metrics.

**Output:** Normalized anterior midcingulate response to reward in opioid users.

**Steps:**

1. 1. Identify opioid users with blunted anterior midcingulate response.
2. 2. Prepare TMS equipment and set parameters for stimulation.
3. 3. Apply TMS to the prefrontal cortex at specified intervals.
4. 4. Measure anterior midcingulate response to reward stimuli pre- and post-TMS.
5. 5. Analyze changes in neural response to determine normalization.

**Core Operation:** `output = stimulation of prefrontal cortex using magnetic pulses`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `stimulation_frequency` | 10 Hz | Higher frequencies may enhance stimulation effects. |
| `stimulation_duration` | 20 minutes | Longer durations may lead to more significant changes in neural response. |

## Complexity

- **Time:** O(1) for each stimulation session
- **Space:** O(n) for storing brain activity data
- **In practice:** Real-world performance can vary based on individual brain responses and equipment calibration.

## Implementation

```python
def apply_tms(subject_data: List[float], frequency: float, duration: int) -> List[float]:
    # Prepare TMS equipment
    # Apply TMS to the prefrontal cortex
    # Measure response
    return normalized_response
```

## Common Mistakes

- Not properly calibrating the TMS equipment before use.
- Failing to assess contraindications in patients.
- Ignoring individual variability in brain response to TMS.

## Use When

- Developing interventions for opioid addiction
- Researching brain stimulation techniques
- Exploring reward processing in addiction

## Avoid When

- Working with non-addicted populations
- When TMS is contraindicated
- In cases of severe psychiatric disorders without prior assessment

## Tradeoffs

**Strengths:**

- Non-invasive and relatively safe.
- Can target specific brain regions.
- Potential to restore normal function in addiction.

**Weaknesses:**

- Effectiveness can vary widely among individuals.
- Requires specialized equipment and training.
- Not suitable for all patient populations.

**Compared To:**

- **vs Electroconvulsive Therapy (ECT):** Use TMS for non-invasive treatment; ECT for severe cases.

## Connects To

- Neurofeedback
- Functional Magnetic Resonance Imaging (fMRI)
- Cognitive Behavioral Therapy (CBT)
- Deep Brain Stimulation (DBS)

## Evidence (Papers)

- **Blunted anterior midcingulate response to reward in opioid users is normalized by prefrontal transcranial magnetic stimulation** - [DOI](https://doi.org/10.1016/j.eswa.2022.117725)
