# Polymerase Chain Reaction (PCR)

*Also known as: PCR*

**PCR is a technique used to amplify specific DNA sequences for analysis and identification.**

**Category:** biological_method  
**Maturity:** proven

## How It Works

PCR works by repeatedly heating and cooling a mixture of DNA, primers, and polymerase to create copies of a specific DNA segment. The process involves denaturation, annealing, and extension phases, allowing for exponential amplification of the target DNA. This amplified DNA can then be sequenced to identify species or genetic variations.

## Algorithm

**Input:** Mosquito samples containing blood from vertebrates.

**Output:** Identified vertebrate species based on DNA sequencing.

**Steps:**

1. 1. Collect mosquitoes using light traps.
2. 2. Preserve collected mosquitoes for DNA extraction.
3. 3. Extract DNA from the blood meal of the mosquitoes.
4. 4. Amplify the extracted DNA using PCR.
5. 5. Sequence the amplified DNA.
6. 6. Compare the sequenced DNA against known vertebrate genomes.

**Core Operation:** `output = amplified DNA from original sample`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `primer_length` | 18-25 bp | Affects the specificity and efficiency of the amplification. |
| `number_of_cycles` | 25-35 | More cycles increase the amount of DNA but can also lead to non-specific amplification. |

## Complexity

- **Time:** O(n * c) where n is the length of the DNA and c is the number of cycles
- **Space:** O(n)
- **In practice:** PCR can be performed relatively quickly, typically within a few hours.

## Implementation

```python
def perform_pcr(samples: List[Sample]) -> List[IdentifiedSpecies]:
    extracted_dna = extract_dna(samples)
    amplified_dna = amplify_dna(extracted_dna)
    sequenced_data = sequence_dna(amplified_dna)
    identified_species = identify_species(sequenced_data)
    return identified_species
```

## Common Mistakes

- Using primers that are not specific to the target DNA.
- Not optimizing the number of cycles leading to non-specific amplification.
- Failing to properly extract DNA, resulting in low yield.

## Use When

- You need to monitor vertebrate diversity in a non-invasive manner.
- Traditional methods of biodiversity assessment are impractical.
- Rapid assessment of species presence is required.

## Avoid When

- High accuracy in species identification is critical and cannot tolerate errors.
- Resources for DNA sequencing are limited.
- The target species are not likely to be found in mosquito blood meals.

## Tradeoffs

**Strengths:**

- Non-invasive method for biodiversity assessment.
- Rapid results compared to traditional methods.
- Ability to detect a wide range of species from small samples.

**Weaknesses:**

- Potential for errors in species identification.
- Requires access to DNA sequencing technology.
- Not all species may be represented in mosquito blood meals.

**Compared To:**

- **vs Traditional trapping methods:** Use PCR when rapid assessment is needed; traditional methods are slower and more invasive.

## Connects To

- DNA sequencing
- Genetic barcoding
- Metagenomics
- Environmental DNA (eDNA) analysis

## Evidence (Papers)

- **Mosquito-derived ingested DNA as a tool for monitoring terrestrial vertebrates within a peri-urban environment** - [DOI](https://doi.org/10.1002/ecs2.70163)
