# Weighted Phase Lag Index (WPLI)

**WPLI is used to assess brain connectivity by analyzing EEG signals.**

**Category:** statistical_method  
**Maturity:** emerging

## How It Works

WPLI quantifies the phase synchronization between different EEG channels, providing insights into functional connectivity in the brain. It is particularly useful for analyzing brain activity in response to emotional stimuli. By comparing the phase differences of signals, WPLI helps identify how different brain regions communicate during specific tasks or emotional experiences.

## Algorithm

**Input:** EEG signals from participants, emotional response ratings from Likert scales.

**Output:** Analysis of emotional responses and brain connectivity metrics.

**Steps:**

1. 1. Select nostalgic and non-nostalgic stimuli based on participant feedback.
2. 2. Present stimuli through auditory, visual, and audiovisual channels.
3. 3. Record EEG data during stimulus presentation.
4. 4. Measure emotional responses using Likert scales.
5. 5. Preprocess EEG data (filtering, artifact removal).
6. 6. Calculate WPLI to assess functional connectivity.
7. 7. Analyze emotional response data using ANOVA.

**Core Operation:** `WPLI = |E[exp(j(φ1 - φ2))]| / (E[|exp(j(φ1 - φ2))|])^2`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `number_of_participants` | 38 | More participants can improve the reliability of results. |
| `stimulus_duration` | 30-40 seconds | Longer durations may enhance emotional engagement. |
| `EEG_channels` | 64 | More channels provide a finer resolution of brain connectivity. |
| `frequency_bands` | Delta (1-4 Hz), Theta (4-8 Hz), Alpha (8-13 Hz), Beta (13-30 Hz), Gamma (30-50 Hz) | Different bands can reveal various aspects of brain activity. |

## Complexity

- **Time:** O(n log n) for FFT calculations
- **Space:** O(n) for storing EEG data
- **In practice:** Real-world performance may vary based on preprocessing steps and the quality of EEG data.

## Implementation

```python
def calculate_wpli(eeg_data: List[List[float]]) -> List[float]:
    # Preprocess EEG data
    filtered_data = preprocess(eeg_data)
    # Calculate WPLI
    wpli_values = []
    for channel_pair in combinations(filtered_data, 2):
        wpli = compute_wpli(channel_pair)
        wpli_values.append(wpli)
    return wpli_values
```

## Common Mistakes

- Neglecting proper preprocessing of EEG data, leading to noise interference.
- Using inappropriate stimulus types that do not elicit emotional responses.
- Failing to account for individual differences in emotional engagement.

## Use When

- Designing applications that leverage nostalgia for emotional engagement.
- Creating therapeutic tools that utilize music and imagery for emotional well-being.
- Conducting research on emotional responses to multimedia stimuli.

## Avoid When

- The target audience has no emotional connection to the stimuli.
- The application requires real-time processing of emotional responses.
- The focus is solely on visual or auditory stimuli without integration.

## Tradeoffs

**Strengths:**

- Provides a robust measure of brain connectivity.
- Effective for analyzing emotional responses.
- Can be applied to various types of stimuli.

**Weaknesses:**

- Requires careful preprocessing of EEG data.
- May not be suitable for real-time applications.
- Interpretation of results can be complex.

**Compared To:**

- **vs Phase Locking Value (PLV):** Use WPLI for better noise resistance in EEG data.

## Connects To

- Phase Locking Value (PLV)
- Functional Connectivity Analysis
- EEG Signal Processing
- Emotional Response Measurement

## Evidence (Papers)

- **Harmonizing the past: EEG-based brain network unveil modality-specific mechanisms of nostalgia** - [DOI](https://doi.org/10.3389/fpsyg.2025.1517449)
