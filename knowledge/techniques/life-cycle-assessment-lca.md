# Life-Cycle Assessment (LCA)

*Also known as: LCA*

**LCA evaluates the environmental impacts associated with all stages of a product's life from cradle to grave.**

**Category:** environmental_analysis  
**Maturity:** established

## How It Works

LCA involves defining the scope of the assessment, collecting data on materials and processes, and calculating the total environmental impacts, particularly carbon emissions. The method aggregates emissions data to provide a comprehensive view of the embodied CO2 associated with a project. This analysis helps identify areas for improvement in sustainability practices.

## Algorithm

**Input:** Data on materials (types and quantities), construction processes, and energy use.

**Output:** Total embodied CO2 equivalent emissions for the neighborhood.

**Steps:**

1. 1. Define the scope of the assessment including boundaries and functional units.
2. 2. Collect data on materials used, construction methods, and energy consumption.
3. 3. Calculate the carbon emissions associated with each material and process.
4. 4. Aggregate the emissions data to obtain total embodied CO2 emissions.
5. 5. Analyze results to identify key areas for improvement.

**Core Operation:** `total_embodied_CO2 = sum(material_emission * quantity for each material)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `material_emission_factor` | varies by material type | Changing this affects the calculated emissions for each material. |
| `construction_energy_use` | specific to construction methods | Altering this impacts the overall energy consumption and emissions. |

## Complexity

- **Time:** O(n) where n is the number of materials and processes assessed
- **Space:** O(m) where m is the number of data points collected
- **In practice:** Real-world performance can vary based on data availability and accuracy.

## Implementation

```python
def life_cycle_assessment(materials: List[Material], processes: List[Process]) -> float:
    total_emissions = 0.0
    for material in materials:
        total_emissions += material.emission_factor * material.quantity
    return total_emissions
```

## Common Mistakes

- Neglecting to define clear boundaries for the assessment.
- Using outdated or inaccurate emission factors.
- Failing to include all relevant materials and processes.

## Use When

- Assessing the environmental impact of new urban developments.
- Designing sustainable building practices.
- Evaluating compliance with carbon reduction targets.

## Avoid When

- The project scope does not include carbon emissions assessment.
- Data on materials and processes is unavailable.

## Tradeoffs

**Strengths:**

- Provides a comprehensive view of environmental impacts.
- Helps identify opportunities for reducing carbon emissions.
- Supports compliance with sustainability regulations.

**Weaknesses:**

- Can be data-intensive and time-consuming.
- Results may vary significantly based on data quality.
- Requires expertise in environmental impact assessment.

**Compared To:**

- **vs Carbon Footprint Analysis:** Use LCA for a more comprehensive assessment including all life stages, while Carbon Footprint is more focused on direct emissions.

## Connects To

- Sustainability Assessment
- Environmental Impact Assessment
- Carbon Footprint Analysis
- Life Cycle Costing

## Evidence (Papers)

- **Embodied climate impacts in urban development: a neighborhood case study** [2 citations] - [DOI](https://doi.org/10.5334/bc.478)
