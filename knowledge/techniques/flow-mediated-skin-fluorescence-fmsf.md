# Flow Mediated Skin Fluorescence (FMSF)

**FMSF measures changes in NADH fluorescence in skin tissue to assess mitochondrial and vascular function.**

**Category:** biomedical_technique  
**Maturity:** proven (widely used in production)

## How It Works

The FMSF technique involves occluding blood flow in the brachial artery and measuring the fluorescence of NADH in the skin. After inducing ischemia, the changes in fluorescence are recorded to evaluate the ischemic and hyperemic responses. The analysis provides insights into mitochondrial and vascular health by deriving parameters such as flowmotion and hypoxia sensitivity.

## Algorithm

**Input:** NADH fluorescence data collected from skin tissue during various stages of blood flow occlusion and reperfusion.

**Output:** Parameters including baseline fluorescence (FLbase), ischemic response (IRmax), hyperemic response (HRmax), flowmotion (FM), and hypoxia sensitivity (HS).

**Steps:**

1. 1. Apply a cuff to occlude blood flow in the brachial artery.
2. 2. Measure NADH fluorescence at baseline for 3 minutes.
3. 3. Inflate the cuff to 60 mmHg above systolic blood pressure to induce ischemia.
4. 4. Record changes in NADH fluorescence during ischemia to determine ischemic response (IRmax).
5. 5. Release the cuff and measure the hyperemic response (HRmax) as NADH fluorescence decreases.
6. 6. Analyze the fluorescence signal to derive flowmotion (FM) and hypoxia sensitivity (HS).

**Core Operation:** `output = analyze(NADH fluorescence data)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `cuff_pressure` | 60 mmHg above systolic blood pressure | Affects the level of ischemia induced. |
| `sampling_frequency` | 25 Hz | Determines the temporal resolution of fluorescence measurements. |
| `measurement_duration` | 3 minutes for baseline | Influences the accuracy of baseline fluorescence readings. |

## Complexity

- **Time:** O(n) where n is the number of measurements taken during the procedure.
- **Space:** O(m) where m is the number of parameters derived from the fluorescence data.
- **In practice:** Real-world performance may vary based on patient conditions and equipment calibration.

## Implementation

```python
def fmsf_measurement(data: List[float]) -> Dict[str, float]:
    # Step 1: Apply cuff
    apply_cuff()
    # Step 2: Measure baseline
    baseline = measure_nadh(data)
    # Step 3: Induce ischemia
    induce_ischemia()
    # Step 4: Record ischemic response
    irmax = record_ischemic_response()
    # Step 5: Measure hyperemic response
    hrmax = measure_hyperemic_response()
    # Step 6: Analyze results
    return analyze_results(baseline, irmax, hrmax)
```

## Common Mistakes

- Neglecting to calibrate equipment before measurements.
- Failing to account for patient variability in skin fluorescence.
- Inadequate baseline measurement duration leading to inaccurate results.

## Use When

- Assessing patients for cardiovascular diseases or diabetes.
- Monitoring metabolic health in athletes.
- Evaluating microcirculatory dysfunction in chronic diseases.

## Avoid When

- When immediate results are required without setup time.
- In patients with skin conditions that may affect fluorescence measurements.

## Tradeoffs

**Strengths:**

- Non-invasive assessment of vascular and mitochondrial function.
- Provides real-time feedback on blood flow dynamics.
- Can differentiate between healthy and diseased states effectively.

**Weaknesses:**

- Requires specific equipment and setup time.
- Results can be influenced by external factors like skin conditions.
- May not provide immediate results.

**Compared To:**

- **vs Laser Doppler flowmetry:** FMSF provides more detailed metabolic insights compared to LDF.
- **vs Flow mediated dilation:** FMSF offers a broader assessment of both mitochondrial and vascular function.

## Connects To

- Laser Doppler flowmetry (LDF)
- Laser speckle contrast imaging (LSCI)
- Flow mediated dilation (FMD)
- Reactive hyperemia peripheral arterial tonometry (RH-PAT)

## Evidence (Papers)

- **Simultaneous assessment of mitochondrial and vascular function using the Flow Mediated Skin Fluorescence technique** [3 citations] - [DOI](https://doi.org/10.3389/fphys.2025.1509159)
