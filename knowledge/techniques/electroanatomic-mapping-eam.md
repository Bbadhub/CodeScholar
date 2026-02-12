# Electroanatomic Mapping (EAM)

**Electroanatomic mapping is a technique used to assess the electrical activity of the heart to diagnose arrhythmogenic cardiomyopathy.**

**Category:** diagnostic_method  
**Maturity:** proven

## How It Works

Electroanatomic mapping utilizes a multielectrode catheter to collect electrophysiological data from the heart. It identifies areas of low-voltage and fractionated electrograms that indicate myocardial abnormalities. This information helps in diagnosing conditions like arrhythmogenic cardiomyopathy, particularly when traditional imaging methods are inconclusive.

## Algorithm

**Input:** Electrophysiological data from the heart, including voltage measurements from the mapping catheter.

**Output:** Identification of abnormal electrical substrates and potential diagnosis of arrhythmogenic cardiomyopathy.

**Steps:**

1. 1. Insert a multielectrode catheter into the heart.
2. 2. Perform endocardial high-density substrate bipolar voltage mapping.
3. 3. Identify areas with low-voltage and fractionated electrograms.
4. 4. Target specific PVC morphologies for ablation.
5. 5. Confirm findings with genetic testing if necessary.

**Core Operation:** `output = identify_low_voltage_areas(electrophysiological_data)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `bipolar voltage threshold` | <0.5 mV | Lowering the threshold increases sensitivity for detecting low-voltage areas. |
| `unipolar voltage threshold` | <0.5 mV | Lowering the threshold increases sensitivity for detecting low-voltage areas. |

## Complexity

- **Time:** O(n) where n is the number of data points collected
- **Space:** O(n) for storing the collected data
- **In practice:** Real-world performance can vary based on the quality of the catheter and the operator's experience.

## Implementation

```python
def electroanatomic_mapping(data: List[float]) -> List[Tuple[float, float]]:
    # Step 1: Insert multielectrode catheter
    # Step 2: Perform mapping
    low_voltage_areas = identify_low_voltage_areas(data)
    # Step 3: Target PVC morphologies
    return low_voltage_areas
```

## Common Mistakes

- Failing to properly calibrate the mapping catheter.
- Overlooking the importance of patient selection criteria.
- Not correlating findings with clinical symptoms.

## Use When

- Diagnosing patients with frequent PVCs and inconclusive imaging results.
- Assessing patients with suspected arrhythmogenic cardiomyopathy.
- Evaluating patients who have undergone previous catheter ablation without clear diagnosis.

## Avoid When

- When clear structural abnormalities are evident on imaging.
- In patients without significant arrhythmias or symptoms.

## Tradeoffs

**Strengths:**

- Increases sensitivity for detecting arrhythmogenic cardiomyopathy compared to imaging alone.
- Provides detailed mapping of electrical activity.
- Can guide targeted ablation procedures.

**Weaknesses:**

- Requires specialized equipment and training.
- Invasive procedure with associated risks.
- May not provide clear results in all patients.

**Compared To:**

- **vs Traditional imaging techniques (e.g., echocardiography, cardiac MRI):** Use EAM when imaging is inconclusive; imaging is better for structural abnormalities.

## Connects To

- Electrophysiological studies
- Catheter ablation techniques
- Cardiac MRI
- Echocardiography

## Evidence (Papers)

- **Case Report: Electroanatomic mapping as an early diagnostic tool in arrhythmogenic cardiomyopathy** - [DOI](https://doi.org/10.3389/fcvm.2024.1392186)
