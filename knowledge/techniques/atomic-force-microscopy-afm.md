# Atomic Force Microscopy (AFM)

**AFM is a high-resolution imaging technique used to characterize the surface properties of materials at the nanoscale.**

**Category:** measurement_technique  
**Maturity:** proven

## How It Works

AFM employs a cantilever with a sharp tip that scans the surface of a sample. As the tip moves across the surface, it measures the forces between the tip and the sample, allowing for the creation of detailed topographical maps. This technique is particularly effective for characterizing micro- and nanoplastics, providing quantitative data on their mechanical properties.

## Algorithm

**Input:** Sample containing micro- and nanoplastics mounted on an AFM stage.

**Output:** Topographical maps and quantitative mechanical properties of the micro- and nanoplastics.

**Steps:**

1. 1. Prepare the sample containing micro- and nanoplastics.
2. 2. Mount the sample on the AFM stage.
3. 3. Use the AFM cantilever to scan the sample surface.
4. 4. Measure the forces between the tip and the sample.
5. 5. Generate topographical maps and analyze mechanical properties.
6. 6. Compare results with known standards for validation.

**Core Operation:** `output = topographical map + mechanical properties`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `scan_speed` | 1 Hz | Higher speeds may reduce resolution. |
| `tip_radius` | 10 nm | Smaller tip radius allows for higher resolution imaging. |
| `force_setpoint` | 0.5 nN | Adjusting the force can affect the interaction with the sample surface. |

## Complexity

- **Time:** O(n^2) for scanning a surface of size n x n
- **Space:** O(n^2) for storing topographical data
- **In practice:** Real-world performance can vary based on sample type and AFM settings.

## Implementation

```python
def perform_afm_analysis(sample: Sample) -> Tuple[TopographicalMap, MechanicalProperties]:
    mount_sample(sample)
    scan_surface()
    forces = measure_forces()
    topographical_map = generate_topographical_map(forces)
    mechanical_properties = analyze_mechanical_properties()
    return topographical_map, mechanical_properties
```

## Common Mistakes

- Not properly calibrating the AFM before use.
- Using a tip that is too large for the desired resolution.
- Failing to account for environmental factors that can affect measurements.

## Use When

- You need to characterize micro- and nanoplastics in environmental samples.
- Existing spectroscopic techniques fail to provide accurate measurements.
- High-resolution topographical data is required.

## Avoid When

- The sample contains larger particles that do not require nanomechanical characterization.
- Cost and complexity of AFM setup are prohibitive.
- Rapid screening of large sample sizes is needed.

## Tradeoffs

**Strengths:**

- High-resolution imaging capabilities.
- Ability to measure mechanical properties at the nanoscale.
- Versatile for various types of samples.

**Weaknesses:**

- High cost and complexity of setup.
- Limited throughput for large sample sizes.
- Sensitivity to environmental conditions.

**Compared To:**

- **vs Raman spectroscopy:** Use AFM for high-resolution topographical data; use Raman for chemical composition analysis.
- **vs Fourier Transform Infrared Spectroscopy:** AFM is better for mechanical characterization; FTIR is better for molecular identification.

## Connects To

- Scanning Tunneling Microscopy (STM)
- Raman Spectroscopy
- Fourier Transform Infrared Spectroscopy
- Laser Direct Infrared

## Evidence (Papers)

- **Atomic Force Microscopy (AFM) nanomechanical characterization of micro- and nanoplastics to support environmental investigations in groundwater** [11 citations] - [DOI](https://doi.org/10.1016/j.emcon.2025.100478)
