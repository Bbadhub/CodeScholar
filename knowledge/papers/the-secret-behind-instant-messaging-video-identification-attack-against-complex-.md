# The secret behind instant messaging: video identification attack against complex protocols

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s42400-024-00300-1` |
| Full Paper | [https://doi.org/10.1186/s42400-024-00300-1](https://doi.org/10.1186/s42400-024-00300-1) |
| Source | [https://journalclub.io/episodes/the-secret-behind-instant-messaging-video-identification-attack-against-complex-protocols](https://journalclub.io/episodes/the-secret-behind-instant-messaging-video-identification-attack-against-complex-protocols) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `4dcb96be-0f12-4dd9-aa44-61a41abc8d83` |

## Classification

- **Problem Type:** video identification in encrypted traffic
- **Domain:** Cybersecurity
- **Sub-domain:** Video identification and traffic analysis
- **Technique:** Video Fingerprint Matching Framework
- **Technique Category:** detection_system
- **Type:** novel

## Summary

The paper presents a framework for identifying video content transmitted via Instant Messaging (IM) software by extracting unique transmission fingerprints from encrypted video traffic. This is crucial for understanding user privacy risks associated with video sharing in IM applications.

## Key Contribution

**A general video identification framework for IM software that achieves high accuracy in identifying video content from encrypted traffic.**

## Problem

The need to identify video content shared through IM software, which poses privacy risks due to the potential for unauthorized access to user preferences.

## Method

**Approach:** The method involves constructing separate fingerprint databases for ciphertext and plaintext videos, extracting transmission fingerprints from captured traffic, and matching these fingerprints against the databases to identify video content.

**Algorithm:**

1. 1. Capture network traffic from IM software.
2. 2. Preprocess the traffic to filter out non-video data.
3. 3. Extract transmission fingerprints based on the video transmission protocol.
4. 4. Match the extracted fingerprints with the video fingerprint database.
5. 5. Identify the video content based on the best match.

**Input:** Captured network traffic containing video data.

**Output:** Identified video content from the IM software.

**Key Parameters:**

- `HTTPheaderlen: length of the HTTP header`
- `NGQUIC: number of GQUIC packets used for video transmission`
- `diﬀGQUIC: extra data introduced by the GQUIC protocol`
- `plainGQUIC: plaintext control information from GQUIC header`
- `opaqueGQUIC: undisclosed ciphertext control information (estimated as 17 bytes)`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Traffic data from WeChat and WhatsApp

**Results:**

- accuracy: 98.05% for GQUIC, 99.49% for HTTPS, 100% for plaintext

**Compared against:** Existing methods for video identification in DASH streams

**Improvement:** Outperformed existing methods for video identification.

## Implementation Guide

**Data Structures:** Fingerprint databases for ciphertext and plaintext videos, Traffic flow data structures

**Dependencies:** Network traffic analysis tools, Data processing libraries

**Core Operation:**

```python
def identify_video(traffic): preprocess_traffic(traffic); fingerprint = extract_fingerprint(traffic); return match_fingerprint(fingerprint)
```

**Watch Out For:**

- Ensure accurate filtering of non-video traffic to avoid noise.
- Understand the specific transmission protocol used by the IM software.
- Be aware of variations in video size due to padding in ciphertext.

## Use This When

- You need to identify video content shared via IM software.
- You are concerned about user privacy and data leakage in video sharing.
- You want to analyze encrypted traffic for security assessments.

## Don't Use When

- The video transmission protocol is well-documented and standardized.
- You require real-time video identification with minimal processing.
- The dataset of videos is too large for fingerprint matching to be effective.

## Key Concepts

video fingerprint, transmission fingerprint, ciphertext traffic, plaintext traffic, GQUIC protocol, HTTPS protocol

## Connects To

- Deep Packet Inspection
- Traffic Analysis Techniques
- Machine Learning for Traffic Classification

## Prerequisites

- Understanding of network protocols
- Knowledge of encryption methods
- Familiarity with traffic analysis techniques

## Limitations

- Dependent on the specific characteristics of the transmission protocol.
- May not generalize well to all IM software due to proprietary protocols.
- Requires a well-constructed fingerprint database for accurate identification.

## Open Questions

- How can this method be adapted for real-time video identification?
- What additional features could improve identification accuracy across diverse protocols?

## Abstract

This is where side-channel attacks come into play. Instead of breaking the encryption directly, these attacks analyze the patterns and characteristics of encrypted traffic to infer what's happening underneath. In the case of video streaming platforms like YouTube or Netflix, researchers have already shown that you can identify which videos people are watching by analyzing encrypted traffic patterns. These platforms use something called DASH (Dynamic Adaptive Streaming over HTTP), which breaks videos into segments and transmits them at variable bitrates. Each video has a unique "fingerprint" based on how these segments are sized and sequenced. So even when they’re encrypted, you can still see the size and timing patterns of the data chunks, and that's enough to identify specific videos.
