# Mass spectrometry imaging as a promising analytical technique for herbal medicines: an updated review

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fphar.2024.1442870` |
| Full Paper | [https://doi.org/10.3389/fphar.2024.1442870](https://doi.org/10.3389/fphar.2024.1442870) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/1c4ee9f3b105f3778a7424dade4a8857f9567817](https://www.semanticscholar.org/paper/1c4ee9f3b105f3778a7424dade4a8857f9567817) |
| Source | [https://journalclub.io/episodes/mass-spectrometry-imaging-as-a-promising-analytical-technique-for-herbal-medicines-an-updated-review](https://journalclub.io/episodes/mass-spectrometry-imaging-as-a-promising-analytical-technique-for-herbal-medicines-an-updated-review) |
| Source | [https://www.semanticscholar.org/paper/1c4ee9f3b105f3778a7424dade4a8857f9567817](https://www.semanticscholar.org/paper/1c4ee9f3b105f3778a7424dade4a8857f9567817) |
| Year | 2026 |
| Citations | 1 |
| Authors | Jinying Zhang, Zhiguo Mao, Ding Zhang, Lin Guo, Hui Zhao, Mingsan Miao |
| Paper ID | `f304d04a-9c55-496d-b655-5f16f9a9cec1` |

## Classification

- **Problem Type:** analytical chemistry, spatial metabolomics
- **Domain:** Bioinformatics & Health
- **Sub-domain:** Mass Spectrometry Imaging
- **Technique:** Mass Spectrometry Imaging (MSI)
- **Technique Category:** analytical_method
- **Type:** adaptation

## Summary

The paper reviews the application of Mass Spectrometry Imaging (MSI) techniques in analyzing herbal medicines, highlighting their ability to visualize the spatial distribution of bioactive compounds. Engineers should care because MSI can significantly enhance quality control and understanding of herbal medicine mechanisms, leading to safer and more effective products.

## Key Contribution

**The integration of MSI techniques for comprehensive spatial analysis of herbal medicine metabolites without complex sample pretreatment.**

## Problem

The complexity of herbal medicines and their metabolites makes it challenging to identify specific actions and ensure quality control.

## Method

**Approach:** MSI combines mass spectrometry with imaging techniques to visualize the spatial distribution of metabolites in herbal medicines. It allows for simultaneous qualitative and quantitative analysis without the need for complex sample preparation.

**Algorithm:**

1. 1. Prepare the sample by slicing it into thin sections.
2. 2. Select an appropriate ionization method (SIMS, MALDI, or DESI).
3. 3. Apply the ionization source to the sample to generate ions.
4. 4. Analyze the ions using a mass analyzer to obtain mass spectra.
5. 5. Map the spatial distribution of the detected ions to create an image.
6. 6. Use software to extract and visualize the data.

**Input:** Thin sections of herbal medicine samples.

**Output:** Spatial distribution images of metabolites and their concentrations.

**Key Parameters:**

- `spatial_resolution: 1-100 μm (depending on the ionization method)`
- `matrix_selection: varies by method (e.g., organic acids for MALDI)`
- `ionization_environment: high vacuum for SIMS and MALDI, ambient for DESI`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Herbal medicine samples including Salvia miltiorrhiza, Coptis chinensis, and Cordyceps sinensis

**Results:**

- spatial resolution: 1-100 μm
- sensitivity: high
- throughput: high

**Compared against:** Traditional analytical methods like LC-MS and GC-MS

**Improvement:** MSI provides higher spatial resolution and sensitivity compared to traditional methods.

## Implementation Guide

**Data Structures:** Mass spectra data arrays, Spatial coordinate mapping arrays

**Dependencies:** Mass spectrometry equipment, Imaging software for data visualization

**Core Operation:**

```python
for each pixel in sample: generate_ions(pixel) -> analyze_ions() -> map_distribution()
```

**Watch Out For:**

- Ensure proper sample preparation to avoid loss of volatile compounds.
- Select the appropriate ionization method based on the sample type.
- Be aware of matrix effects that can interfere with ionization efficiency.

## Use This When

- You need to visualize the spatial distribution of metabolites in herbal medicines.
- You want to improve quality control processes for herbal products.
- You are exploring the pharmacological mechanisms of herbal compounds.

## Don't Use When

- You require a simple qualitative analysis without spatial information.
- The sample is highly unstable and cannot withstand the ionization process.
- You need results in a very short time frame with minimal setup.

## Key Concepts

mass spectrometry, spatial distribution, metabolomics, bioactive compounds, quality control, herbal medicines, ionization techniques, chemical analysis

## Connects To

- Liquid Chromatography-Mass Spectrometry (LC-MS)
- Gas Chromatography-Mass Spectrometry (GC-MS)
- Nuclear Magnetic Resonance (NMR)
- Metabolomics
- Pharmacognosy

## Prerequisites

- Basic understanding of mass spectrometry principles.
- Familiarity with herbal medicine composition.
- Knowledge of spatial analysis techniques.

## Limitations

- High cost of equipment and maintenance.
- Complex sample preparation for some ionization methods.
- Potential matrix effects affecting ionization efficiency.

## Open Questions

- What are the best practices for optimizing matrix selection in MSI?
- How can MSI be further integrated with other analytical techniques for enhanced results?

## Abstract

Herbal medicines often have many bioactive compounds, working simultaneously on many different parts of the body, making it difficult for researchers to identify the actions of specific molecules. Mass Spectrometry Imaging (MSI) techniques have provided a visual window into the molecular realm of herbal medicines, enabling researchers to identify locations of useful compounds and observe the chemical mechanisms of pathology. Molecular level imagining can greatly improve the quality control of the herbal medicine landscape by helping to standardize cultivation and processing methods, ensuring safe and reliable medicines for all. In this episode of Journal Club, we’ll explore the three major methods of MSI, present how researchers use MSI techniques in herbal medicine analysis, and see how they can be applied to quality control improvement. But first, let’s start things off by looking at how herbal medicines work.
