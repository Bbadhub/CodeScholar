# Covalent organic framework membrane with hourglass-shaped nanochannels for ultrafast desalination

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1038/s41467-025-63650-5` |
| Full Paper | [https://doi.org/10.1038/s41467-025-63650-5](https://doi.org/10.1038/s41467-025-63650-5) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/a3c080a3a1834d4f7bce7e9cb69a54bc7e033af1](https://www.semanticscholar.org/paper/a3c080a3a1834d4f7bce7e9cb69a54bc7e033af1) |
| Source | [https://journalclub.io/episodes/covalent-organic-framework-membrane-with-hourglass-shaped-nanochannels-for-ultrafast-desalination](https://journalclub.io/episodes/covalent-organic-framework-membrane-with-hourglass-shaped-nanochannels-for-ultrafast-desalination) |
| Source | [https://www.semanticscholar.org/paper/a3c080a3a1834d4f7bce7e9cb69a54bc7e033af1](https://www.semanticscholar.org/paper/a3c080a3a1834d4f7bce7e9cb69a54bc7e033af1) |
| Year | 2026 |
| Citations | 13 |
| Authors | Xiaocui Wei, Yanan Liu, Fu Zhao, Tingyuan Wang, Zongmei Li, Chunyang Fan |
| Paper ID | `4afe157e-433f-430b-b818-abe9c665e880` |

## Classification

- **Problem Type:** desalination
- **Domain:** Optimization & Operations Research
- **Sub-domain:** Membrane technology
- **Technique:** COF-CDN membrane
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a novel covalent organic framework (COF) membrane with hourglass-shaped nanochannels designed for ultrafast desalination, achieving high water flux and salt rejection. Engineers should care because this technology offers a promising solution to the global water shortage by enhancing desalination efficiency.

## Key Contribution

**Development of a COF membrane with hourglass-shaped nanochannels that significantly improves water permeability and ion rejection for desalination applications.**

## Problem

The increasing global water shortage necessitates efficient desalination technologies to convert seawater into potable water.

## Method

**Approach:** The COF-CDN membrane is fabricated by sequentially assembling amino-cyclodextrin nanoparticles onto the mouth of a COF membrane, creating hourglass-shaped nanochannels. These nanochannels feature a hydrophilic conical entrance and a hydrophobic spout, optimizing water transport and ion rejection.

**Algorithm:**

1. 1. Synthesize TpPa-SO3H COF nanosheets using 1,3,5-triformylphloroglucinol and 2,5-diaminobenzenesulfonic acid.
2. 2. Assemble COF nanosheets onto a Nylon substrate membrane.
3. 3. Install amino-cyclodextrin nanoparticles onto the mouth of the COF membrane via hydrogen bonding and electrostatic interactions.
4. 4. Characterize the membrane structure and properties using techniques like SEM, FT-IR, and NMR.
5. 5. Test desalination performance using a dead-end filtration cell at a constant pressure.

**Input:** Saltwater solutions with varying concentrations of salts (Li2SO4, Na2SO4, MgSO4, LiCl, NaCl, MgCl2).

**Output:** Desalinated water with high purity and reduced salt concentration.

**Key Parameters:**

- `water_flux: 98 L m–2 h–1`
- `Na2SO4_rejection: 94%`
- `NaCl_rejection: 92%`
- `operating_pressure: 2.0 bar`
- `membrane_thickness: ~1.26 ± 0.02 µm`

**Complexity:** not stated

## Benchmarks

**Tested on:** Saltwater solutions with various salts

**Results:**

- water flux: 98 L m–2 h–1
- Na2SO4 rejection: 94%
- NaCl rejection: 92%

**Compared against:** pristine COF membrane with water flux of 45 L m–2 h–1 and rejection of less than 40%

**Improvement:** High water flux and salt rejection significantly better than the pristine COF membrane.

## Implementation Guide

**Data Structures:** COF nanosheets, amino-cyclodextrin nanoparticles, Nylon substrate membrane

**Dependencies:** Synthesis equipment for COF and CDN, Characterization tools (SEM, FT-IR, NMR)

**Core Operation:**

```python
assemble_membrane(COF_nanosheets, CDN) -> test_performance(membrane, salt_solution)
```

**Watch Out For:**

- Ensure proper alignment of CDN to avoid defects in the membrane.
- Monitor pH levels during testing as they affect membrane performance.
- Be cautious of the membrane's stability under different chemical environments.

## Use This When

- You need to develop a high-performance desalination membrane.
- You are working on projects that require efficient water purification.
- You want to explore novel membrane technologies for chemical separations.

## Don't Use When

- The application requires membranes with high thermal stability beyond 250 °C.
- You need membranes that can operate effectively in extreme pH conditions without degradation.
- The project does not involve desalination or water purification.

## Key Concepts

covalent organic framework, hourglass-shaped nanochannels, desalination, pH-responsive membranes, ion rejection, water permeability, hydrophilic-hydrophobic interactions

## Connects To

- membrane filtration techniques
- nanoporous materials
- chemical separation processes

## Prerequisites

- Understanding of membrane technology
- Knowledge of polymer chemistry
- Familiarity with desalination processes

## Limitations

- Limited operational stability beyond 7 days
- Performance may vary with different salt types
- Requires careful pH management for optimal performance

## Open Questions

- How can the membrane be scaled for industrial applications?
- What are the long-term effects of fouling on membrane performance?

## Abstract

Desalination is actually a group of technologies, not just one thing. The most common approach is reverse osmosis. In this process, saltwater is forced through specialized membranes under high pressure. The membranes allow water molecules to pass through while blocking salt ions and other contaminants. Think of it as an extremely fine filter/strainer that can separate molecules based on their size and chemical properties.
