# A Review of DNA Cryptography

## Access

| Field | Value |
|-------|-------|
| DOI | `10.34133/icomputing.0106` |
| Full Paper | [https://doi.org/10.34133/icomputing.0106](https://doi.org/10.34133/icomputing.0106) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/0322703282a6c94f61b98512c19b4ba82e65e50b](https://www.semanticscholar.org/paper/0322703282a6c94f61b98512c19b4ba82e65e50b) |
| Source | [https://journalclub.io/episodes/a-review-of-dna-cryptography](https://journalclub.io/episodes/a-review-of-dna-cryptography) |
| Source | [https://www.semanticscholar.org/paper/0322703282a6c94f61b98512c19b4ba82e65e50b](https://www.semanticscholar.org/paper/0322703282a6c94f61b98512c19b4ba82e65e50b) |
| Year | 2026 |
| Citations | 7 |
| Authors | Ling Chu, Yanqing Su, Xiangyu Yao, Peng Xu, Wenbin Liu |
| Paper ID | `7c0d7c36-2909-4348-ac73-1cf743b4b03e` |

## Classification

- **Problem Type:** data storage and encryption
- **Domain:** Bioinformatics & Health
- **Sub-domain:** DNA data storage and cryptography
- **Technique:** DNA Cryptography
- **Technique Category:** framework
- **Type:** novel

## Summary

This paper reviews the potential of DNA as a medium for cryptography and information storage, highlighting its efficiency and durability compared to traditional storage methods. Engineers should care because leveraging DNA for data storage could revolutionize how we handle large amounts of information securely and sustainably.

## Key Contribution

**The paper provides a comprehensive overview of DNA cryptography techniques and their implications for future data storage solutions.**

## Problem

The need for more efficient and durable data storage solutions motivated this work.

## Method

**Approach:** The method involves encoding data into DNA sequences, which can then be synthesized and stored. The retrieval process requires sequencing the DNA to decode the information back into its original format.

**Algorithm:**

1. 1. Convert data into binary format.
2. 2. Encode binary data into DNA sequences using a predefined mapping.
3. 3. Synthesize the DNA sequences for storage.
4. 4. Store the synthesized DNA in a suitable medium.
5. 5. To retrieve, sequence the stored DNA.
6. 6. Decode the sequenced DNA back into binary format.

**Input:** Data in binary format.

**Output:** Data retrieved in its original format.

**Key Parameters:**

- `encoding_scheme: custom mapping`
- `synthesis_cost: variable based on technology`

**Complexity:** not stated

## Benchmarks

**Tested on:** Various datasets for testing DNA storage capacity and retrieval accuracy.

**Results:**

- storage density, retrieval accuracy, cost of synthesis

**Compared against:** Traditional storage methods like hard drives and flash drives.

**Improvement:** Significant improvements in storage density and durability compared to traditional methods.

## Implementation Guide

**Data Structures:** Binary trees for encoding schemes, DNA sequence representations

**Dependencies:** DNA synthesis tools, Sequencing technologies, Data encoding libraries

**Core Operation:**

```python
data = encode_to_dna(input_data); store_dna(data); retrieved_data = decode_from_dna(retrieve_dna());
```

**Watch Out For:**

- Ensure the encoding scheme is efficient to minimize synthesis costs.
- Be aware of the limitations of current sequencing technologies.
- Consider the environmental conditions for DNA storage.

## Use This When

- You need a highly durable storage solution for large datasets.
- You are working on secure data transmission methods.
- You want to explore innovative data storage technologies.

## Don't Use When

- You require immediate access to data with low latency.
- The cost of DNA synthesis is prohibitive for your application.
- You are dealing with small amounts of data that can be easily stored using traditional methods.

## Key Concepts

DNA sequencing, data encoding, information storage, cryptography, synthesis techniques

## Connects To

- Cryptographic algorithms
- Data compression techniques
- Biological data storage methods

## Prerequisites

- Understanding of DNA structure and encoding
- Familiarity with cryptographic principles
- Knowledge of data storage technologies

## Limitations

- High cost of DNA synthesis and sequencing
- Current technology limitations in speed and efficiency
- Potential degradation of DNA over time

## Open Questions

- How can we reduce the cost of DNA synthesis?
- What are the best practices for long-term DNA storage?

## Abstract

DNA is unbelievably compact and efficient at storing and encoding information. As a medium, it can be stored without electricity (in dry pellet form or dissolved in a solution), for thousands and thousands of years. We’ve understood how DNA stores information since Watson & Crick discovered the double-helix in the ‘50s. But until recently we’ve only been able to marvel at that storage mechanism from afar. We haven’t been able to use DNA to store information ourselves. The storage mechanisms we’ve come-up with instead are, well…way worse. Hard drives, flash drives, magnetic tape, CDs, floppy disks, etc, don’t come anywhere close to DNA’s efficiency or durability. In order to use DNA as a storage medium, we’d need to be able to read and write DNA. That is “sequence” and "synthesize" it. Both of these processes have historically been cost prohibitive, but that’s changing
