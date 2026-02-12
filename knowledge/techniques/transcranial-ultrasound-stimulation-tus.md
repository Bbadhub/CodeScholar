# Transcranial Ultrasound Stimulation (TUS)

**TUS is a non-invasive technique that uses ultrasound waves to modulate neuronal activity in deep brain structures.**

**Category:** neuromodulation  
**Maturity:** emerging

## How It Works

TUS employs a 256-element transducer array to deliver focused ultrasound waves to specific brain regions. By adjusting parameters such as frequency and pulse duration, it can precisely modulate neuronal activity. Real-time fMRI monitoring allows researchers to observe the effects of stimulation and adjust parameters accordingly for optimal results.

## Algorithm

**Input:** Participant-specific anatomical data from CT scans and fMRI imaging.

**Output:** Modulated neuronal activity in targeted brain regions, observed through fMRI.

**Steps:**

1. 1. Position participant using a custom-designed stereotactic mask.
2. 2. Use low-dose CT scans to derive participant-specific skull and brain properties.
3. 3. Compute driving parameters for each transducer element using a full-wave acoustic model.
4. 4. Apply TUS to the target area with specified pulse parameters.
5. 5. Monitor brain activity using fMRI during and after stimulation.
6. 6. Adjust stimulation parameters in real-time based on feedback.

**Core Operation:** `output = modulated neuronal activity in targeted brain regions`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `frequency` | 555 kHz | Higher frequencies may enhance spatial resolution but could also increase tissue heating. |
| `target pressure` | 775 kPa | Increasing pressure may enhance stimulation effects but risks damaging tissue. |
| `pulse duration` | 300 ms | Longer pulse durations may lead to stronger modulation but could also cause discomfort. |
| `pulse interval` | 3 s | Shorter intervals may increase stimulation frequency but could lead to fatigue. |
| `theta burst stimulation duration` | 80 s | Longer durations may enhance cumulative effects but risk overstimulation. |
| `theta burst frequency` | 5 Hz | Higher frequencies may lead to more rapid modulation but could also reduce precision. |

## Complexity

- **Time:** O(n) where n is the number of transducer elements
- **Space:** O(m) where m is the size of the anatomical data
- **In practice:** Real-world performance may vary based on individual anatomical differences.

## Implementation

```python
def apply_tus(ct_data: CTData, fMRI_data: fMRIData) -> NeuronalActivity:
    position_participant(ct_data)
    derive_skull_properties(ct_data)
    compute_transducer_parameters()
    apply_ultrasound_stimulation()
    monitor_brain_activity(fMRI_data)
    adjust_parameters_real_time()
    return modulated_activity
```

## Common Mistakes

- Not accounting for individual anatomical variations in skull and brain structure.
- Using inappropriate stimulation parameters that do not match the target area.
- Failing to monitor real-time feedback during stimulation.

## Use When

- You need to target deep brain structures non-invasively.
- You want to study the effects of neuromodulation on brain function.
- You are developing therapies for neurological disorders.

## Avoid When

- You require immediate invasive intervention.
- You are targeting superficial cortical regions with high angles of incidence.

## Tradeoffs

**Strengths:**

- Non-invasive method for deep brain stimulation.
- High spatial precision targeting.
- Ability to monitor effects in real-time using fMRI.

**Weaknesses:**

- Limited to deep brain structures; less effective for superficial areas.
- Potential for discomfort or adverse effects if not properly calibrated.
- Requires sophisticated equipment and expertise.

**Compared To:**

- **vs Transcranial Magnetic Stimulation (TMS):** Use TUS for deeper brain structures; use TMS for superficial areas.

## Connects To

- Transcranial Magnetic Stimulation (TMS)
- Functional Magnetic Resonance Imaging (fMRI)
- Deep Brain Stimulation (DBS)
- Neurofeedback Techniques

## Evidence (Papers)

- **Ultrasound system for precise neuromodulation of human deep brain circuits** [25 citations] - [DOI](https://doi.org/10.1038/s41467-025-63020-1)
