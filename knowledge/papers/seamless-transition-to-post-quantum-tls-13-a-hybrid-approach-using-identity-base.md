# Seamless Transition to Post-Quantum TLS 1.3: A Hybrid Approach Using Identity-Based Encryption

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/s24227300` |
| Full Paper | [https://doi.org/10.3390/s24227300](https://doi.org/10.3390/s24227300) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/7934a9760e179a444a89b0d3bffd5091bb702991](https://www.semanticscholar.org/paper/7934a9760e179a444a89b0d3bffd5091bb702991) |
| Source | [https://journalclub.io/episodes/seamless-transition-to-post-quantum-tls-13-a-hybrid-approach-using-identity-based-encryption](https://journalclub.io/episodes/seamless-transition-to-post-quantum-tls-13-a-hybrid-approach-using-identity-based-encryption) |
| Source | [https://www.semanticscholar.org/paper/7934a9760e179a444a89b0d3bffd5091bb702991](https://www.semanticscholar.org/paper/7934a9760e179a444a89b0d3bffd5091bb702991) |
| Year | 2026 |
| Citations | 3 |
| Authors | T. Astrizi, Ricardo Custódio |
| Paper ID | `202efd76-fd4f-4f0a-aa1c-4b3288deb9e5` |

## Classification

- **Problem Type:** post-quantum cryptography for secure communication
- **Domain:** Cybersecurity
- **Sub-domain:** Post-Quantum Cryptography
- **Technique:** Hybrid KEMTLS with Identity-Based Encryption
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a hybrid approach to transition existing TLS 1.3 implementations to post-quantum security using Identity-Based Encryption (IBE). This method minimizes infrastructure changes, allowing for the reuse of existing keys and certificates, which is crucial for a seamless migration to post-quantum cryptography.

## Key Contribution

**Development of a hybrid KEMTLS variant that integrates classical public key infrastructure with identity-based encryption for post-quantum security in TLS communications.**

## Problem

The need to secure TLS communications against threats posed by quantum computers that can break current cryptographic algorithms.

## Method

**Approach:** The method combines classical public key algorithms with identity-based encryption to facilitate a transition to post-quantum security. It allows existing certificates to be used while integrating post-quantum operations through IBE, thus reducing the need for immediate updates from certificate authorities.

**Algorithm:**

1. 1. Generate a master public key (mpk) and master secret key (msk) using IDKEM.KeyGen.
2. 2. For each server, extract a secret key using IDKEM.Extract with the server's identity.
3. 3. Use the existing public key infrastructure for classical key encapsulation.
4. 4. For post-quantum operations, encapsulate keys using IDKEM.Encaps with the server's identity.
5. 5. Decapsulate keys using IDKEM.Decaps with the extracted secret key.
6. 6. Integrate the classical public key into the identity for revocation management.
7. 7. Implement the hybrid KEMTLS protocol for secure communication.

**Input:** Server's identity and existing public key infrastructure.

**Output:** Post-quantum secure communication using existing TLS certificates.

**Key Parameters:**

- `security_parameter: 1λ`
- `key_size: typical sizes for post-quantum keys not specified`
- `message_size: larger than classical TLS due to post-quantum keys`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Simulated network environments and real-world Internet configurations.

**Results:**

- Performance timings compared to existing TLS 1.3 implementations and KEMTLS.

**Compared against:** Existing TLS 1.3 implementations, KEMTLS.

**Improvement:** Timings remain competitive despite larger message sizes.

## Implementation Guide

**Data Structures:** Master public key (mpk), Master secret key (msk), Identity-based secret keys, Ciphertexts

**Dependencies:** Cryptographic libraries supporting IBE and KEMs.

**Core Operation:**

```python
mpk, msk = IDKEM.KeyGen(1λ); skid = IDKEM.Extract(msk, id); c, k = IDKEM.Encaps(mpk, id); k' = IDKEM.Decaps(skid, c)
```

**Watch Out For:**

- Ensure compatibility with existing certificate authorities.
- Manage revocation effectively to avoid domain-wide revocation issues.
- Monitor performance impacts due to larger message sizes.

## Use This When

- Transitioning existing TLS systems to be resistant to quantum attacks.
- Maintaining compatibility with current public key infrastructure during migration.
- Implementing a gradual upgrade path to post-quantum cryptography.

## Don't Use When

- Immediate full transition to post-quantum cryptography is feasible.
- Existing infrastructure cannot support hybrid approaches.
- Performance is a critical constraint and larger message sizes are unacceptable.

## Key Concepts

Identity-Based Encryption, Post-Quantum Cryptography, Key Encapsulation Mechanism, Hybrid Cryptography, Public Key Infrastructure, TLS 1.3

## Connects To

- KEMTLS
- Post-Quantum Key Exchange
- Identity-Based Cryptography
- Hybrid Cryptographic Protocols

## Prerequisites

- Understanding of TLS protocol and its security mechanisms.
- Familiarity with public key infrastructure.
- Knowledge of identity-based encryption concepts.

## Limitations

- Requires updates to certificate authorities to support post-quantum keys.
- Performance may be impacted due to larger message sizes.
- Complexity in managing the transition for smaller entities.

## Open Questions

- What are the long-term implications of maintaining a hybrid PKI?
- How can the transition to fully post-quantum systems be accelerated?

## Abstract

Today is a special episode of Journal Club. This is the first installment of a series I’m calling "Post Quantum Readiness". I’m going to sprinkle these episodes in every once in a while over the next year, or two, or however long they’re needed. While the goal of every Journal Club episode is to get you up to speed on some new research (and this episode is no exception in that regard), this "Post Quantum Readiness" series is going to be much more focused on practical advice. We’re going to be looking at research papers of course, but for this series we’re specifically trying to extract three things from them: 1. What you need to know now. 2. What you’ll need to know tomorrow. 3. Calls to action. Steps you can take immediately to start to get ahead of this.
