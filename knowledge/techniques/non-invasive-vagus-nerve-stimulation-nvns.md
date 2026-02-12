# Non-invasive Vagus Nerve Stimulation (nVNS)

**nVNS is a therapeutic technique that stimulates the vagus nerve to alleviate symptoms in patients with persistent post-concussion syndrome.**

**Category:** medical_therapy  
**Maturity:** proven (widely used in production)

## How It Works

nVNS employs a handheld device to stimulate the vagus nerve non-invasively, activating the cholinergic anti-inflammatory pathway. Patients use the device daily, applying it to the cervical pulse point for short sessions. The effectiveness of the treatment is evaluated through changes in symptom severity measured by the Neurobehavioral Symptom Inventory (NSI).

## Algorithm

**Input:** Patient symptom data collected via the Neurobehavioral Symptom Inventory (NSI).

**Output:** Change in NSI scores indicating symptom severity before and after nVNS treatment.

**Steps:**

1. 1. Patient completes baseline NSI assessment.
2. 2. Patient is prescribed gammaCore™ device for nVNS.
3. 3. Patient is trained to use the device over the cervical pulse point.
4. 4. Patient uses the device for 2 minutes, twice in the morning and twice in the evening.
5. 5. Follow-up NSI assessment is conducted approximately 112 days post-treatment initiation.
6. 6. Analyze changes in NSI scores to evaluate treatment efficacy.

**Core Operation:** `output = change in NSI scores before and after nVNS treatment`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `stimulation_duration` | 2 minutes | Longer durations may enhance efficacy but are not tested. |
| `stimulation_frequency` | 25 Hz | Higher frequencies may alter nerve response. |
| `intensity` | up to 60 milliamps | Increased intensity may improve stimulation but risks discomfort. |
| `voltage` | 24 volts | Higher voltage may enhance effectiveness but could lead to side effects. |
| `treatment_frequency` | 4 sessions per day | More frequent sessions may improve outcomes. |

## Complexity

- **Time:** O(1) for each treatment session
- **Space:** O(1) as it requires minimal data storage
- **In practice:** Real-world performance may vary based on patient compliance and device usage.

## Implementation

```python
def nVNS_treatment(patient_data: NSIData) -> NSIChange:
    baseline_scores = patient_data.get_baseline_scores()
    device = gammaCore()
    for session in range(4):
        device.stimulate(duration=2, frequency=25)
    follow_up_scores = patient_data.get_follow_up_scores()
    return analyze_scores(baseline_scores, follow_up_scores)
```

## Common Mistakes

- Failing to train patients properly on device usage.
- Not adhering to the prescribed treatment frequency.
- Ignoring contraindications that may lead to adverse effects.

## Use When

- Managing persistent post-concussion symptoms in patients with mTBI.
- Integrating adjunctive therapies into standard care for TBI.
- Seeking non-pharmacological interventions for symptom relief.

## Avoid When

- Patients have contraindications such as implanted pacemakers.
- Immediate acute care is required for severe TBI symptoms.
- Patients are not compliant with treatment protocols.

## Tradeoffs

**Strengths:**

- Non-invasive and easy to use.
- Can be integrated into existing treatment protocols.
- Potentially significant symptom relief for patients.

**Weaknesses:**

- Effectiveness may vary among individuals.
- Requires patient compliance for optimal results.
- Not suitable for all patients due to contraindications.

**Compared To:**

- **vs pharmacological treatments:** nVNS is preferred for patients seeking non-drug interventions.

## Connects To

- Transcutaneous Electrical Nerve Stimulation (TENS)
- Cognitive Behavioral Therapy (CBT)
- Physical Rehabilitation for TBI
- Biofeedback Techniques

## Evidence (Papers)

- **Non-invasive vagus nerve stimulation is associated with the reduction in persistent post-concussion symptoms: an observational study** - [DOI](https://doi.org/10.3389/fneur.2025.1642034)
