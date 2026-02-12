# Semisolid Extrusion Additive Manufacturing

*Also known as: 3D Printing of Semisolid Formulations*

**This technique allows for the creation of custom-dosed tablets using a 3D printer to extrude semisolid formulations.**

**Category:** additive_manufacturing  
**Maturity:** emerging

## How It Works

Semisolid extrusion additive manufacturing involves preparing a semisolid formulation of a drug, such as metoprolol tartrate, and loading it into a 3D printer. The printer then extrudes the formulation according to specified dosage parameters, allowing for the production of tablets tailored to individual patient needs. Once printed, the tablets are allowed to solidify before packaging for distribution.

## Algorithm

**Input:** Semisolid formulation of metoprolol tartrate and dosage parameters.

**Output:** Custom-dosed metoprolol tartrate tablets.

**Steps:**

1. 1. Prepare the semisolid formulation of metoprolol tartrate.
2. 2. Load the formulation into the 3D printer.
3. 3. Set the desired dosage parameters for the patient.
4. 4. Initiate the printing process to create the custom tablet.
5. 5. Allow the tablet to solidify and package for distribution.

**Core Operation:** `output = custom tablet based on dosage parameters`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `extrusion_speed` | 5 mm/s | Affects the rate at which the formulation is extruded, influencing tablet consistency. |
| `temperature` | 60°C | Impacts the viscosity of the semisolid formulation, affecting extrusion quality. |
| `tablet_weight` | 100 mg | Determines the final weight of the tablet, which is crucial for dosage accuracy. |

## Complexity

- **Time:** O(n) where n is the number of tablets printed
- **Space:** O(1) for the formulation storage
- **In practice:** Real-world performance can vary based on printer capabilities and formulation properties.

## Implementation

```python
def print_tablet(formulation: Semisolid, dosage: float) -> Tablet:
    load_printer(formulation)
    set_dosage_parameters(dosage)
    start_printing()
    solidify_tablet()
    return packaged_tablet
```

## Common Mistakes

- Not calibrating the printer for different formulations.
- Ignoring the impact of temperature on formulation viscosity.
- Failing to validate dosage accuracy post-printing.

## Use When

- Developing personalized medication solutions for pediatric patients.
- Creating custom dosages for patients with specific health conditions.
- Implementing on-demand medication manufacturing in clinical settings.

## Avoid When

- Standard dosages are sufficient and available.
- High-volume production of uniform tablets is required.
- Regulatory approval for 3D printed medications is not established.

## Tradeoffs

**Strengths:**

- Allows for personalized medication tailored to individual patient needs.
- Reduces the need for off-label dosing.
- Improves medication adherence through custom dosages.

**Weaknesses:**

- Not suitable for high-volume production.
- Regulatory hurdles for 3D printed medications.
- Potential variability in tablet quality.

**Compared To:**

- **vs Traditional Tablet Manufacturing:** Use semisolid extrusion for personalized solutions; use traditional methods for mass production.

## Connects To

- 3D Printing
- Personalized Medicine
- Pharmaceutical Manufacturing
- Additive Manufacturing Techniques

## Evidence (Papers)

- **Off-the-shelf medication transformed: Custom-dosed metoprolol tartrate tablets via semisolid extrusion additive manufacturing and the perception of this technique in a hospital context** [8 citations] - [DOI](https://doi.org/10.1016/j.ijpx.2024.100277)
