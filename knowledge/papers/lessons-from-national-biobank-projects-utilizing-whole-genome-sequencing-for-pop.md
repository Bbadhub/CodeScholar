# Lessons from national biobank projects utilizing whole-genome sequencing for population-scale genomics

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s44342-025-00040-9` |
| Full Paper | [https://doi.org/10.1186/s44342-025-00040-9](https://doi.org/10.1186/s44342-025-00040-9) |
| Source | [https://journalclub.io/episodes/lessons-from-national-biobank-projects-utilizing-whole-genome-sequencing-for-population-scale-genomics](https://journalclub.io/episodes/lessons-from-national-biobank-projects-utilizing-whole-genome-sequencing-for-population-scale-genomics) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `8cfd49ae-1c06-493b-ada2-76fbf8197042` |

## Classification

- **Problem Type:** population-scale genomics
- **Domain:** Bioinformatics & Health
- **Sub-domain:** Population genomics
- **Technique:** Whole-genome sequencing (WGS)
- **Technique Category:** data_analysis
- **Type:** adaptation

## Summary

The paper reviews national biobank projects utilizing whole-genome sequencing (WGS) to enhance understanding of human genetic variation and its implications for health. Engineers should care because these projects leverage advanced technologies and methodologies that can inform the development of precision medicine and improve healthcare delivery.

## Key Contribution

**The synthesis of methodologies and technological advancements in national biobank projects that utilize WGS for population-scale genomics.**

## Problem

The need to understand human genetic variation and its relationship to health and disease across diverse populations.

## Method

**Approach:** National biobank projects collect genomic data from large cohorts, integrating it with phenotypic, environmental, and clinical information. This holistic approach enables the identification of genetic variants associated with health outcomes and supports precision medicine.

**Algorithm:**

1. 1. Recruit a diverse cohort of participants.
2. 2. Collect genomic data using whole-genome sequencing.
3. 3. Gather comprehensive phenotypic and clinical data.
4. 4. Process genomic data using variant calling tools.
5. 5. Analyze data to identify genetic variants and their associations with health outcomes.
6. 6. Integrate findings into clinical practice for precision medicine.

**Input:** Genomic data from participants, including DNA samples and associated phenotypic, environmental, and clinical data.

**Output:** Identified genetic variants and their associations with health outcomes, along with insights for precision medicine.

**Key Parameters:**

- `sample_size: 1,000,000 (target for NPBBD-Korea)`
- `WGS_depth: 30x for general population, 60x for cancer patients`

**Complexity:** not stated

## Benchmarks

**Tested on:** UK Biobank: 500,000 participants, All of Us Research Program: 1,000,000 participants (target), BioBank Japan: 200,000 participants

**Results:**

- number of SNPs: 1.1 billion in UK Biobank
- WGS data for 490,640 participants in UK Biobank

**Compared against:** GATK for variant calling, DRAGEN for accelerated processing

**Improvement:** DRAGEN significantly reduces processing time compared to GATK.

## Implementation Guide

**Data Structures:** BAM/CRAM for alignment data, VCF for variant calls, Sparse VCF for large datasets

**Dependencies:** Genome Analysis Toolkit (GATK), DRAGEN, DeepVariant, cloud computing platforms (e.g., AWS, Google Cloud)

**Core Operation:**

```python
def analyze_genomic_data(samples): process_samples(samples); call_variants(samples); integrate_data(samples)
```

**Watch Out For:**

- Ensure data privacy and ethical considerations are addressed.
- Be aware of the computational intensity of variant calling methods.
- Manage data storage efficiently to handle large genomic datasets.

## Use This When

- Building applications for precision medicine based on genomic data.
- Conducting large-scale genomic studies requiring integration of diverse datasets.
- Developing tools for variant calling and genomic data analysis.

## Don't Use When

- Working with small datasets where traditional methods suffice.
- When computational resources are limited and cannot handle large-scale genomic data.

## Key Concepts

whole-genome sequencing, biobank, precision medicine, variant calling, multi-omics integration, population genetics

## Connects To

- Variant calling algorithms (GATK, DRAGEN)
- Multi-omics integration techniques
- Cloud-based genomic data analysis frameworks

## Prerequisites

- Understanding of genomic data formats (BAM, VCF)
- Familiarity with bioinformatics tools for data analysis
- Knowledge of precision medicine principles

## Limitations

- High computational costs associated with large-scale genomic analysis.
- Potential biases in genomic data representation across populations.
- Challenges in integrating genomic data with clinical practice.

## Open Questions

- How to effectively integrate genomic data into routine clinical workflows?
- What are the best practices for ensuring data privacy in genomic studies?

## Abstract

In 2003, after 13 laborious years (and even more including its conception) the Human Genome Project declared that the first human genome was sequenced (well 92% of it, but that is pretty complete all things considered). Today, a mere 20 years later, genome sequencing can be done in well under a day. This leap in technology has allowed us to scale up genomic studies to unprecedented levels. Now the real question stands, what can be done with this incredible technology to improve our lives? Well, in terms of medicine, quite a lot! As genomics technology gets cheaper, better, and faster, it has allowed nations to apply whole-genome sequencing (WGS) to very large projects. These are called national biobank projects. They are collecting hundreds-of-thousands to millions of samples in order to expand our understanding of human genetic information and how it relates to our health. National biobank projects are special because they work to
