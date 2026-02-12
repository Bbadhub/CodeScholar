# National fisheries restricted areas: an alternative tool for the sustainable management of Black Sea vulnerable and economically important fish populations

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fmars.2025.1570936` |
| Full Paper | [https://doi.org/10.3389/fmars.2025.1570936](https://doi.org/10.3389/fmars.2025.1570936) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/f08a8e9af91fca90f8f5c1d0758af7d5f466aa69](https://www.semanticscholar.org/paper/f08a8e9af91fca90f8f5c1d0758af7d5f466aa69) |
| Source | [https://journalclub.io/episodes/national-fisheries-restricted-areas-an-alternative-tool-for-the-sustainable-management-of-black-sea-vulnerable-and-economically-important-fish-populations](https://journalclub.io/episodes/national-fisheries-restricted-areas-an-alternative-tool-for-the-sustainable-management-of-black-sea-vulnerable-and-economically-important-fish-populations) |
| Source | [https://www.semanticscholar.org/paper/f08a8e9af91fca90f8f5c1d0758af7d5f466aa69](https://www.semanticscholar.org/paper/f08a8e9af91fca90f8f5c1d0758af7d5f466aa69) |
| Year | 2026 |
| Citations | 2 |
| Authors | V. Niță, M. Nenciu, T. Begun, A. Teacă, M. Galațchi, C. Danilov |
| Paper ID | `55ac7d55-55fe-4746-ac29-284e4580ed39` |

## Classification

- **Problem Type:** spatial fisheries management
- **Domain:** Marine Biology & Ecology
- **Sub-domain:** Fisheries Management
- **Technique:** National Fisheries Restricted Areas (nFRAs)
- **Technique Category:** management_strategy
- **Type:** novel

## Summary

The paper proposes the establishment of national Fisheries Restricted Areas (nFRAs) as a tool for sustainable management of vulnerable fish populations in the Black Sea. This approach aims to enhance biodiversity conservation and improve local fisheries management by protecting critical habitats and reducing fishing pressure in specific areas.

## Key Contribution

**Identification and establishment of the first national Fisheries Restricted Area in the Black Sea to support both conservation and local fisheries.**

## Problem

Overexploitation of fish stocks in the Black Sea necessitates effective management strategies to protect vulnerable species and habitats.

## Method

**Approach:** The method involves identifying suitable areas for Fisheries Restricted Areas based on ecological and fisheries criteria. Data from various sources, including fish fauna inventories and macrozoobenthos sampling, are integrated to substantiate the establishment of nFRAs.

**Algorithm:**

1. 1. Collect data on fish species and macrozoobenthos in the target area.
2. 2. Analyze the spatial distribution of identified species and habitats.
3. 3. Evaluate ecological criteria such as species richness and habitat quality.
4. 4. Propose suitable areas for nFRAs based on the analysis.
5. 5. Conduct public consultations and finalize the nFRA establishment.
6. 6. Monitor the ecological and economic impacts post-establishment.

**Input:** Data on fish species, macrozoobenthos composition, fishing effort, and ecological assessments.

**Output:** Established Fisheries Restricted Areas that enhance biodiversity and support local fisheries.

**Key Parameters:**

- `depth_range: 40-50 meters`
- `area_size: 272.76 km²`

**Complexity:** not stated

## Benchmarks

**Tested on:** Macrozoobenthos samples from 43 stations, Ichthyological surveys from the northern Romanian coast

**Results:**

- species richness: 62 fish species identified
- macrozoobenthic density: 7,935 ind.m-2
- macrozoobenthic biomass: 396 g.m-2

**Compared against:** Existing Fisheries Restricted Areas in deeper waters (>1000m), Previous fish stock assessments in the Black Sea

**Improvement:** Establishment of nFRA is expected to lead to improved ecological status and fish population recovery.

## Implementation Guide

**Data Structures:** Spatial data for fish and benthic species distribution, Ecological assessment indices

**Dependencies:** Statistical analysis software (e.g., R, PRIMER), GIS tools for spatial analysis

**Core Operation:**

```python
identify_nFRA(area_data): analyze_species_distribution(area_data); propose_nFRA(location); conduct_public_consultation(); establish_nFRA();
```

**Watch Out For:**

- Ensure comprehensive data collection to support ecological assessments.
- Engage local communities early to avoid opposition.
- Monitor ecological changes post-establishment to assess effectiveness.

## Use This When

- Implementing fisheries management strategies in overexploited regions.
- Establishing conservation areas to protect vulnerable marine species.
- Integrating ecological data into fisheries policy decisions.

## Don't Use When

- In regions with sufficient existing marine protected areas.
- When local fishing communities oppose area restrictions.
- In areas where ecological data is insufficient for informed decision-making.

## Key Concepts

Fisheries Restricted Areas, Biodiversity Conservation, Essential Fish Habitats, Ecological Assessment, Participatory Approach

## Connects To

- Marine Protected Areas (MPAs)
- Ecosystem-Based Fisheries Management
- Biodiversity Assessment Frameworks

## Prerequisites

- Understanding of marine ecology and fisheries biology.
- Familiarity with spatial analysis techniques.
- Knowledge of local fisheries regulations.

## Limitations

- Limited effectiveness in deeper waters where fish populations are not present.
- Potential resistance from local fishing communities.
- Dependence on accurate ecological data for successful implementation.

## Open Questions

- What are the long-term ecological impacts of nFRAs on fish populations?
- How can stakeholder engagement be improved in the establishment of nFRAs?

## Abstract

According to the latest data from the General Fisheries Commission for the Mediterranean, over half of the fish stocks in the Mediterranean and Black Sea are currently overexploited. Despite a decade of conservation efforts, sustainable fisheries management remains challenging. Traditional Marine Protected Areas (MPAs) aren't always effective for both biodiversity conservation and fisheries management, so alternative approaches are needed. Now, you might be thinking, “doesn't the Black Sea already have fishing restrictions?” Well, yes and no. There's a large Fisheries Restricted Area covering 1.76 million square kilometers in the Mediterranean and Black Seas, but there's a critical problem: it only applies to waters deeper than 1,000 meters. This is completely irrelevant for the Black Sea, which below 200 meters becomes anoxic, meaning there’s no oxygen and thus it is essentially lifeless. All Black Sea fishing activity is
