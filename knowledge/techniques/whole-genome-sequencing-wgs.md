# Whole-genome sequencing (WGS)

*Also known as: WGS, genome sequencing*

**Whole-genome sequencing (WGS) is a comprehensive method for analyzing the complete DNA sequence of an organism's genome.**

**Category:** genomic_analysis  
**Maturity:** proven (widely used in production)

## How It Works

Whole-genome sequencing involves collecting genomic data from a large cohort of participants, which is then integrated with phenotypic, environmental, and clinical information. This data is processed using variant calling tools to identify genetic variants associated with health outcomes. The findings can be utilized to support precision medicine by tailoring healthcare based on individual genetic profiles.

## Algorithm

**Input:** Genomic data from DNA samples, along with associated phenotypic, environmental, and clinical data.

**Output:** Identified genetic variants and their associations with health outcomes, along with insights for precision medicine.

**Steps:**

1. 1. Recruit a diverse cohort of participants.
2. 2. Collect genomic data using whole-genome sequencing.
3. 3. Gather comprehensive phenotypic and clinical data.
4. 4. Process genomic data using variant calling tools.
5. 5. Analyze data to identify genetic variants and their associations with health outcomes.
6. 6. Integrate findings into clinical practice for precision medicine.

**Core Operation:** `output = identified genetic variants + health outcome associations`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `sample_size` | 1,000,000 | Larger sample sizes improve the robustness of findings. |
| `WGS_depth` | 30x for general population, 60x for cancer patients | Higher depth increases the accuracy of variant detection. |

## Complexity

- **Time:** O(n log n) for processing genomic data
- **Space:** O(n) for storing genomic data
- **In practice:** Processing time and resource requirements can be significant, especially with large datasets.

## Implementation

```python
def whole_genome_sequencing(data: GenomicData, cohort: List[Participant]) -> VariantAnalysis:
    # Step 1: Recruit participants
    participants = recruit_participants(cohort)
    # Step 2: Collect genomic data
    genomic_data = collect_genomic_data(participants)
    # Step 3: Gather phenotypic data
    phenotypic_data = gather_phenotypic_data(participants)
    # Step 4: Process genomic data
    variants = process_genomic_data(genomic_data)
    # Step 5: Analyze data
    analysis_results = analyze_variants(variants, phenotypic_data)
    # Step 6: Integrate findings
    integrate_findings(analysis_results)
    return analysis_results
```

## Common Mistakes

- Underestimating the computational resources required for large-scale genomic data processing.
- Neglecting to integrate diverse datasets, which can lead to biased results.
- Failing to validate the findings with independent cohorts.

## Use When

- Building applications for precision medicine based on genomic data.
- Conducting large-scale genomic studies requiring integration of diverse datasets.
- Developing tools for variant calling and genomic data analysis.

## Avoid When

- Working with small datasets where traditional methods suffice.
- When computational resources are limited and cannot handle large-scale genomic data.

## Tradeoffs

**Strengths:**

- Provides comprehensive genomic data for precision medicine.
- Enables identification of genetic variants associated with health outcomes.
- Supports large-scale studies with diverse datasets.

**Weaknesses:**

- Requires significant computational resources and storage.
- Processing time can be lengthy for large datasets.
- Data integration can be complex and challenging.

**Compared To:**

- **vs Targeted sequencing:** Use WGS for comprehensive analysis; use targeted sequencing for specific genes.

## Connects To

- Variant calling
- Genomic data analysis
- Precision medicine
- Population genomics

## Evidence (Papers)

- **Lessons from national biobank projects utilizing whole-genome sequencing for population-scale genomics** - [DOI](https://doi.org/10.1186/s44342-025-00040-9)
