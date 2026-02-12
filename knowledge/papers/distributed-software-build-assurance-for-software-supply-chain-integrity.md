# Distributed Software Build Assurance for Software Supply Chain Integrity

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/app14209262` |
| Full Paper | [https://doi.org/10.3390/app14209262](https://doi.org/10.3390/app14209262) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/86b3b2ffe5efc327e1d9f953bc20a4b8d498e279](https://www.semanticscholar.org/paper/86b3b2ffe5efc327e1d9f953bc20a4b8d498e279) |
| Source | [https://journalclub.io/episodes/distributed-software-build-assurance-for-software-supply-chain-integrity](https://journalclub.io/episodes/distributed-software-build-assurance-for-software-supply-chain-integrity) |
| Source | [https://www.semanticscholar.org/paper/86b3b2ffe5efc327e1d9f953bc20a4b8d498e279](https://www.semanticscholar.org/paper/86b3b2ffe5efc327e1d9f953bc20a4b8d498e279) |
| Year | 2026 |
| Citations | 1 |
| Authors | Ken Lew, Arijet Sarker, Simeon Wuthier, Jinoh Kim, Jong-Hoi Kim, Sang-Yoon Chang |
| Paper ID | `11200eec-31bb-4e47-8ff8-4d86836da5f6` |

## Classification

- **Problem Type:** software supply chain integrity verification
- **Domain:** Cybersecurity
- **Sub-domain:** Software Supply Chain Security
- **Technique:** Distributed Software Build Assurance
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a distributed software build assurance scheme that detects modifications in the software supply chain, enhancing security against malicious injections. Engineers should care because it leverages blockchain technology to provide a decentralized verification process, significantly improving efficiency and integrity in software builds.

## Key Contribution

**A distributed software build assurance scheme utilizing blockchain to verify software integrity across the supply chain.**

## Problem

The need to secure software development against malicious modifications and injections throughout the software supply chain.

## Method

**Approach:** The method uses reproducible builds and a software bill of materials (SBOM) to ensure the integrity of software artifacts. It generates a proof based on the software artifacts and compares it with a reference proof stored on a blockchain.

**Algorithm:**

1. 1. User downloads source code (s) and dependencies.
2. 2. User compiles the source code to generate build output (b) and SBOM documentation (d).
3. 3. User constructs a Merkle tree using s, b, and d to generate proof (p).
4. 4. User retrieves reference proof (p') from the blockchain.
5. 5. User compares p with p'.
6. 6. If p equals p', the software artifacts are verified as unmodified.

**Input:** Source code files (s), build output (b), SBOM documentation (d)

**Output:** Proof of integrity (p) for the software artifacts

**Key Parameters:**

- `hash_function: SHA-256`
- `Merkle_tree: constructed from s, b, d`
- `blockchain: permissioned with proof-of-authority consensus`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Ethereum software (Archanes v1.13.4)

**Results:**

- verification time: approximately 1 second overhead
- performance gain: 2-3 orders of magnitude quicker than centralized server

**Compared against:** Centralized server approach for software build assurance

**Improvement:** Significant performance gains over centralized server approaches

## Implementation Guide

**Data Structures:** Merkle tree, blockchain ledger

**Dependencies:** Ethereum Smart Contract, cryptographic libraries for SHA-256

**Core Operation:**

```python
proof = MerkleTree(hash(s), hash(b), hash(d))
```

**Watch Out For:**

- Ensure reproducible builds are supported in your environment.
- Watch for discrepancies in software artifacts across different machines.
- Be aware of the overhead introduced by proof generation.

## Use This When

- You need to verify the integrity of software builds in a decentralized manner.
- You are working with open-source software projects that require assurance against malicious modifications.
- You want to implement a secure software supply chain process.

## Don't Use When

- The software artifacts are not reproducible across different environments.
- You require real-time verification with a centralized authority.
- The overhead of generating proofs is unacceptable for your application.

## Key Concepts

blockchain, Merkle tree, reproducible build, software bill of materials, cryptographic hash function

## Connects To

- reproducible builds
- software bill of materials
- blockchain technology
- cryptographic hash functions

## Prerequisites

- Understanding of blockchain technology
- Knowledge of cryptographic hash functions
- Familiarity with software build processes

## Limitations

- Requires reproducible builds to function effectively.
- Performance may vary based on blockchain network conditions.
- Not suitable for environments without consistent build conditions.

## Open Questions

- How can this approach be generalized to other software applications?
- What are the implications of using different consensus protocols on performance?

## Abstract

In May 2021, the White House issued Executive Order 14028, the "Executive Order on Improving the Nation’s Cybersecurity". This order, among other things, directed NIST (the National Institute of Standards and Technology) to develop best-practices around software supply-chain security. Before we go on, I want to disambiguate that phrase. We are not talking about supply-chain software security. That is the security of the software that manages a business' supply chain. No. We’re talking about software supply-chain security: the security of the supply chain of the software we build.
