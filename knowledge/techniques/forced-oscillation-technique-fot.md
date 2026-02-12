# Forced Oscillation Technique (FOT)

**FOT measures respiratory impedance using external oscillatory signals during normal breathing.**

**Category:** medical_diagnostic_technique  
**Maturity:** proven (widely used in production)

## How It Works

The Forced Oscillation Technique employs external pulse vibrations to assess the flow response of the respiratory tract. By analyzing how the respiratory system reacts to these oscillations, it quantifies respiratory impedance, which is broken down into resistance and reactance at various frequencies. This method is particularly useful for monitoring lung function in patients who cannot perform standard spirometry tests.

## Algorithm

**Input:** Normal breathing data from patients with Hermansky-Pudlak Syndrome.

**Output:** Values of respiratory resistance (Rrs) and reactance (Xrs) at frequencies of 5, 11, and 19 Hz.

**Steps:**

1. 1. Set up the Resmon™Pro V3 device for FOT measurements.
2. 2. Instruct the patient to breathe normally while the device emits oscillatory signals.
3. 3. Measure the flow response of the respiratory tract to the oscillations.
4. 4. Calculate Rrs and Xrs from the measured flow and pressure data.
5. 5. Analyze the results to assess the severity of pulmonary fibrosis.

**Core Operation:** `Zrs = Rrs + jXrs`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `frequency` | 5 Hz, 11 Hz, 19 Hz | Changing frequency can affect the sensitivity of the impedance measurements. |
| `device` | Resmon™Pro V3 | Different devices may yield varying accuracy and reliability. |

## Complexity

- **Time:** O(n) where n is the number of measurements taken
- **Space:** O(1) for storing impedance values
- **In practice:** Real-world performance may vary based on patient cooperation and device calibration.

## Implementation

```python
def forced_oscillation_measurement(patient_data: List[float]) -> Tuple[float, float]:
    # Step 1: Set up device
    device = ResmonPro()
    # Step 2: Instruct patient
    instruct_patient_to_breathe_normally()
    # Step 3: Measure flow response
    flow_response = device.measure_flow()
    # Step 4: Calculate Rrs and Xrs
    Rrs, Xrs = calculate_impedance(flow_response)
    return Rrs, Xrs
```

## Common Mistakes

- Not calibrating the device properly before measurements.
- Failing to instruct patients clearly, leading to inconsistent breathing patterns.
- Overlooking the importance of selecting appropriate frequencies for measurement.

## Use When

- Monitoring patients with Hermansky-Pudlak Syndrome for pulmonary fibrosis.
- Assessing lung function in patients unable to perform standard spirometry.
- Early detection of lung function deterioration in interstitial lung diseases.

## Avoid When

- Patients with normal lung function without risk factors for pulmonary fibrosis.
- In cases where spirometry can be performed reliably.
- When immediate invasive diagnostic procedures are required.

## Tradeoffs

**Strengths:**

- Non-invasive and easy to perform.
- Can detect changes in lung function earlier than standard spirometry.
- Useful for patients who cannot perform traditional lung function tests.

**Weaknesses:**

- Requires specialized equipment that may not be widely available.
- Interpretation of results can be complex.
- Less effective in patients with normal lung function.

**Compared To:**

- **vs Standard Spirometry:** Use FOT when patients cannot perform spirometry; otherwise, spirometry is preferred.

## Connects To

- Spirometry
- Lung Function Testing
- Pulmonary Rehabilitation
- Respiratory Impedance Measurement

## Evidence (Papers)

- **Application of Forced Oscillation Technique in Assessing Pulmonary Fibrosis in Hermansky-Pudlak Syndrome** - [DOI](https://doi.org/10.3390/arm92060040)
