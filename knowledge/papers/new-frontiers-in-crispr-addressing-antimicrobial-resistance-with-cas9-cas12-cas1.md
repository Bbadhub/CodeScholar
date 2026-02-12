# New frontiers in CRISPR: Addressing antimicrobial resistance with Cas9, Cas12, Cas13, and Cas14

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.heliyon.2025.e42013` |
| Full Paper | [https://doi.org/10.1016/j.heliyon.2025.e42013](https://doi.org/10.1016/j.heliyon.2025.e42013) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/d0474ff5c244df5cb7a15dcf1931ec66c4e70fb3](https://www.semanticscholar.org/paper/d0474ff5c244df5cb7a15dcf1931ec66c4e70fb3) |
| Source | [https://journalclub.io/episodes/new-frontiers-in-crispr-addressing-antimicrobial-resistance-with-cas9-cas12-cas13-and-cas14](https://journalclub.io/episodes/new-frontiers-in-crispr-addressing-antimicrobial-resistance-with-cas9-cas12-cas13-and-cas14) |
| Source | [https://www.semanticscholar.org/paper/d0474ff5c244df5cb7a15dcf1931ec66c4e70fb3](https://www.semanticscholar.org/paper/d0474ff5c244df5cb7a15dcf1931ec66c4e70fb3) |
| Year | 2026 |
| Citations | 33 |
| Authors | A. S. A. Ali Agha, A. Al-Samydai, Talal Aburjai |
| Paper ID | `772efdf9-0d94-4fae-ac2b-bbee789f5165` |

## Classification

- **Problem Type:** gene therapy for antimicrobial resistance
- **Domain:** Bioinformatics & Health
- **Sub-domain:** CRISPR technologies
- **Technique:** CRISPR-Cas systems (Cas9, Cas12, Cas13, Cas14)
- **Technique Category:** genetic_modification_tool
- **Type:** adaptation

## Summary

This paper reviews the applications of CRISPR technologies (Cas9, Cas12, Cas13, and Cas14) in combating antimicrobial resistance by modifying the genes of superbugs to enhance their susceptibility to antibiotics. Engineers should care because this approach presents a novel alternative to traditional antibiotics in addressing the growing threat of superbugs.

## Key Contribution

**The paper provides a comprehensive overview of CRISPR applications in gene therapy for antimicrobial resistance.**

## Problem

The work is motivated by the urgent need to find alternatives to antibiotics due to the rise of superbugs resistant to all known medications.

## Method

**Approach:** The method involves using CRISPR systems to target and modify specific genes in superbugs, making them more susceptible to existing antibiotics. This gene editing can potentially reverse antibiotic resistance mechanisms in these pathogens.

**Algorithm:**

1. Identify the target gene associated with antibiotic resistance in the superbug.
2. Design a specific guide RNA (gRNA) to direct the CRISPR system to the target gene.
3. Introduce the CRISPR-Cas complex into the bacterial cells.
4. Allow the CRISPR system to bind to the target gene and induce a double-strand break.
5. Utilize the cell's repair mechanisms to introduce a modification that disrupts the resistance gene.
6. Test the modified bacteria for susceptibility to antibiotics.

**Input:** Bacterial strains exhibiting antibiotic resistance, designed gRNA sequences.

**Output:** Modified bacterial strains with altered susceptibility to antibiotics.

**Key Parameters:**

- `gRNA_length: 20-25 nucleotides`
- `Cas protein concentration: 100-500 ng/µL`
- `transfection efficiency: >70%`

**Complexity:** not stated

## Benchmarks

**Tested on:** Clinical strains of superbugs, laboratory-generated resistant strains

**Results:**

- susceptibility to antibiotics, gene modification efficiency

**Compared against:** Standard antibiotic treatments, previous gene editing techniques

**Improvement:** Potentially significant reduction in resistance, specific values not stated.

## Implementation Guide

**Data Structures:** gRNA sequences, Cas protein complexes, bacterial plasmids

**Dependencies:** CRISPR libraries, gene editing software, molecular biology tools

**Core Operation:**

```python
modify_bacteria(target_gene, gRNA): introduce_Cas_complex(gRNA) -> induce_double_strand_break() -> repair_with_modification()
```

**Watch Out For:**

- Ensure gRNA specificity to avoid off-target effects.
- Optimize delivery methods for CRISPR components.
- Monitor for potential horizontal gene transfer.

## Use This When

- Developing new gene therapies for antibiotic-resistant infections.
- Researching alternative treatments for superbugs.
- Exploring genetic modification techniques in microbiology.

## Don't Use When

- Working with non-bacterial pathogens.
- When ethical concerns about gene editing are paramount.
- In environments where CRISPR technology is restricted or banned.

## Key Concepts

CRISPR, gene editing, antimicrobial resistance, superbugs, Cas proteins

## Connects To

- Gene therapy techniques
- Antibiotic susceptibility testing
- Synthetic biology applications

## Prerequisites

- Basic understanding of molecular biology
- Familiarity with CRISPR technology
- Knowledge of bacterial genetics

## Limitations

- Potential off-target effects leading to unintended mutations.
- Ethical concerns surrounding gene editing in pathogens.
- Regulatory hurdles for clinical applications.

## Open Questions

- What are the long-term effects of CRISPR modifications on bacterial populations?
- How can CRISPR be integrated into existing antibiotic treatment protocols?

## Abstract

We are running low on solutions to combat superbugs. Rather than sticking with antibiotics, we’re starting to turn our gaze towards gene therapies. To this end, the authors of this paper have reviewed the latest applications of CRISPR: Clustered Regularly Interspaced Short Palindromic Repeats. They’re looking specifically at how it can be used to modify the genes of superbugs and make them more susceptible to antibiotics. Today on Journal Club, we will be talking about antimicrobial resistance (AMR), what CRISPR is, and why CRISPR could be the ultimate weapon in this battle. In 2016, a 70-year-old from Nevada died in the hospital, overcome by an infection from the bacteria Klebsiella pneumoniae. Why is this significant? The specific strain of Klebsiella had evolved into a superbug. It had developed resistance to all the antibiotics available in the United States. This means that no known medication was capable of
