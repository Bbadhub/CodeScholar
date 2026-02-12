# Genome editing for sustainable agriculture in Peru: advances, potential applications and regulation

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fgeed.2025.1611040` |
| Full Paper | [https://doi.org/10.3389/fgeed.2025.1611040](https://doi.org/10.3389/fgeed.2025.1611040) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/3e5a1dbce71bdcda0b7cf5a1d2b805101cd542bb](https://www.semanticscholar.org/paper/3e5a1dbce71bdcda0b7cf5a1d2b805101cd542bb) |
| Source | [https://journalclub.io/episodes/genome-editing-for-sustainable-agriculture-in-peru-advances-potential-applications-and-regulation](https://journalclub.io/episodes/genome-editing-for-sustainable-agriculture-in-peru-advances-potential-applications-and-regulation) |
| Source | [https://www.semanticscholar.org/paper/3e5a1dbce71bdcda0b7cf5a1d2b805101cd542bb](https://www.semanticscholar.org/paper/3e5a1dbce71bdcda0b7cf5a1d2b805101cd542bb) |
| Year | 2026 |
| Citations | 3 |
| Authors | M. Mestanza, Ángel David Hernández-Amasifuen, Alexandra Jherina Pineda-Lázaro, Dennis Eriksson, J. Guerrero-Abad |
| Paper ID | `07f8a413-7b56-4df3-8a2d-2121adcc094b` |

## Classification

- **Problem Type:** genome editing for agricultural improvement
- **Domain:** Bioinformatics & Health
- **Sub-domain:** Genome editing technologies
- **Technique:** CRISPR/Cas
- **Technique Category:** framework
- **Type:** novel

## Summary

This paper reviews the advances and potential applications of CRISPR/Cas genome editing technologies in sustainable agriculture in Peru, emphasizing transgene-free methodologies that can enhance crop resilience and nutritional value. Engineers should care because these techniques can lead to significant improvements in agricultural productivity while adhering to regulatory constraints.

## Key Contribution

**The introduction of transgene-free CRISPR/Cas methodologies for genome editing in crops to enhance resilience and nutritional quality without integrating foreign DNA.**

## Problem

Peruvian agriculture faces challenges such as biotic and abiotic stress, which threaten food security and crop yields.

## Method

**Approach:** CRISPR/Cas technology allows precise editing of specific genes in crops by utilizing ribonucleoprotein (RNP) complexes or tRNA-like sequence (TLS) motifs to deliver editing components without integrating foreign DNA. This enables targeted mutations that improve traits such as stress tolerance and nutritional content.

**Algorithm:**

1. 1. Design sgRNA targeting the specific gene of interest.
2. 2. Assemble RNP complex with Cas9 protein and sgRNA.
3. 3. Introduce RNP complex into plant cells via protoplast transformation or other delivery methods.
4. 4. Allow the CRISPR/Cas system to induce a double-strand break at the target site.
5. 5. Activate DNA repair pathways (NHEJ or HDR) to achieve desired genetic modifications.
6. 6. Regenerate whole plants from edited cells.
7. 7. Screen for successful edits and evaluate phenotypic traits.

**Input:** Plant protoplasts or tissues, sgRNA, Cas9 protein, and delivery method (e.g., RNP complex).

**Output:** Edited plant lines with specific genetic modifications.

**Key Parameters:**

- `RNP_complex_concentration: 1-10 µM`
- `sgRNA_length: 20-24 nucleotides`
- `transfection_time: 24-48 hours`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Rice, maize, potato, tomato, and other staple crops

**Results:**

- Yield improvement: up to 11.1%
- Disease resistance: enhanced immune responses
- Nutritional content: increased lysine and carotenoid levels

**Compared against:** Traditional breeding methods, previous gene editing techniques (ZFNs, TALENs)

**Improvement:** Significant yield and trait improvements over traditional methods, specific values not stated.

## Implementation Guide

**Data Structures:** Ribonucleoprotein complexes, sgRNA sequences, Cas9 protein

**Dependencies:** CRISPR/Cas libraries, Plant transformation protocols, Gene editing software for sgRNA design

**Core Operation:**

```python
def edit_gene(target_gene): create_RNP(target_gene); deliver_RNP(); monitor_editing();
```

**Watch Out For:**

- Ensure sgRNA specificity to avoid off-target effects.
- Optimize delivery methods for different crop types.
- Monitor for somaclonal variations in regenerated plants.

## Use This When

- Developing crops with enhanced resistance to drought and pests.
- Seeking to improve nutritional content of staple crops.
- Working within regulatory frameworks that restrict transgenic crops.

## Don't Use When

- Crops that are highly recalcitrant to transformation.
- When rapid integration of transgenes is required.
- In environments where traditional breeding is more effective.

## Key Concepts

CRISPR/Cas, gene editing, transgene-free, ribonucleoprotein, tRNA-like sequence, agricultural biotechnology

## Connects To

- Zinc Finger Nucleases (ZFNs)
- Transcription Activator-Like Effector Nucleases (TALENs)
- Base editing technologies
- Plant breeding techniques
- Agroecological practices

## Prerequisites

- Basic understanding of molecular biology and genetics.
- Familiarity with plant tissue culture techniques.
- Knowledge of CRISPR/Cas technology.

## Limitations

- Regulatory constraints on genetically modified organisms.
- Technical challenges in transforming recalcitrant crops.
- Potential for off-target effects in genome editing.

## Open Questions

- What are the long-term ecological impacts of CRISPR-edited crops?
- How can regulatory frameworks adapt to new biotechnological advancements?

## Abstract

The power of CRISPR lies in what happens next. The cell responds to the break by activating one of two natural DNA repair pathways: non-homologous end joining (NHEJ) or homology-directed repair (HDR). NHEJ is error-prone and often results in small insertions or deletions, which can knock out a gene by disrupting its reading frame. HDR, on the other hand, uses a repair template to precisely modify the DNA sequence, enabling the introduction of specific mutations or corrections. In agricultural applications, this allows scientists to disable susceptibility genes, enhance stress tolerance, modify metabolic pathways, or improve nutritional content, without inserting foreign DNA. This is what sets CRISPR apart from traditional GMOs. Transgenic approaches typically involve inserting an entire gene (often from a different species) into the host genome, and this insertion is usually random. By contrast, CRISPR targets specific sites, enabling precise control over both the location and nature of the genetic change. CRISPR edits can be achieved using transgene-free methods. Instead of integrating editing machinery into the genome, researchers can introduce ribonucleoprotein (RNP) complexes directly into plant cells. These RNPs perform the edit and then degrade, leaving no foreign genetic material behind.
