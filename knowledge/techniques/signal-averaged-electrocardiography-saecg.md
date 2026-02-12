# Signal Averaged Electrocardiography (SAECG)

**SAECG is a non-invasive technique used to evaluate the risk of ventricular arrhythmias by analyzing late potentials in ECG waveforms.**

**Category:** diagnostic_method  
**Maturity:** proven

## How It Works

SAECG processes multiple ECG waveforms to detect late potentials that indicate abnormal ventricular conduction. It involves filtering the QRS complex to isolate these late potentials and measuring specific parameters. Based on these measurements, patients are classified into groups to assess their risk of ventricular arrhythmias and evaluate ventricular substrate characteristics.

## Algorithm

**Input:** ECG data from patients, specifically 12-lead ECG and SAECG recordings.

**Output:** Classification of patients into groups based on SAECG criteria and assessment of ventricular substrate characteristics.

**Steps:**

1. 1. Collect ECG data from patients.
2. 2. Apply filtering to the QRS complex to isolate late potentials.
3. 3. Measure the following parameters: filtered QRS duration, terminal QRS duration, and root mean square voltage of the last 40 ms.
4. 4. Classify patients into groups based on SAECG criteria.
5. 5. Compare ventricular substrate characteristics between groups.

**Core Operation:** `Classification based on filtered QRS duration, terminal QRS duration, and terminal QRS root mean square voltage.`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `filtered QRS duration` | ≥ 114 ms | Longer duration indicates higher risk of arrhythmias. |
| `terminal QRS duration` | ≥ 38 ms | Longer duration suggests abnormal conduction. |
| `terminal QRS root mean square voltage` | ≥ 20 mV | Lower voltage may indicate higher risk. |

## Complexity

- **Time:** O(n) where n is the number of ECG samples processed.
- **Space:** O(1) as it requires a fixed amount of space for parameters.
- **In practice:** Real-world performance can vary based on the quality of ECG data and patient conditions.

## Implementation

```python
def saecg_analysis(ecg_data: List[float]) -> Tuple[str, Dict[str, float]]:
    filtered_qrs_duration = filter_qrs(ecg_data)
    terminal_qrs_duration = measure_terminal_qrs(ecg_data)
    terminal_qrs_rms_voltage = measure_rms_voltage(ecg_data)
    classification = classify_patient(filtered_qrs_duration, terminal_qrs_duration, terminal_qrs_rms_voltage)
    return classification, {'filtered_qrs_duration': filtered_qrs_duration, 'terminal_qrs_duration': terminal_qrs_duration, 'terminal_qrs_rms_voltage': terminal_qrs_rms_voltage}
```

## Common Mistakes

- Not applying appropriate filtering to isolate late potentials.
- Misinterpreting the significance of measured parameters.
- Failing to classify patients correctly based on SAECG criteria.

## Use When

- You need a non-invasive method to assess arrhythmia risk in NICM patients.
- You want to predict the presence of arrhythmogenic substrates before invasive procedures.
- You are developing a diagnostic tool for cardiac health monitoring.

## Avoid When

- Patients have baseline ventricular conduction disturbances.
- You require immediate invasive intervention for arrhythmias.
- The patient has a known diagnosis of Arrhythmogenic Cardiomyopathy.

## Tradeoffs

**Strengths:**

- Non-invasive and safe for patients.
- Can predict arrhythmia risk before invasive procedures.
- Useful for monitoring cardiac health over time.

**Weaknesses:**

- May not be effective in patients with existing conduction disturbances.
- Requires high-quality ECG data for accurate results.
- Not suitable for immediate intervention scenarios.

**Compared To:**

- **vs Standard ECG:** SAECG provides more detailed analysis of late potentials compared to standard ECG.

## Connects To

- Electrocardiography (ECG)
- Cardiac MRI
- Electrophysiology studies
- Holter monitoring

## Evidence (Papers)

- **Signal-averaged electrocardiography as a noninvasive tool for evaluating the ventricular substrate in patients with nonischemic cardiomyopathy: reassessment of an old tool** [2 citations] - [DOI](https://doi.org/10.3389/fcvm.2024.1306055)
