# Enabling per-file data recovery from ransomware attacks via file system forensics and flash translation layer data extraction

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s42400-024-00287-9` |
| Full Paper | [https://doi.org/10.1186/s42400-024-00287-9](https://doi.org/10.1186/s42400-024-00287-9) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/32811b74e7323799aec3119af7b72da007a83964](https://www.semanticscholar.org/paper/32811b74e7323799aec3119af7b72da007a83964) |
| Source | [https://journalclub.io/episodes/enabling-per-file-data-recovery-from-ransomware-attacks-via-file-system-forensics-and-flash-translation-layer-data-extraction](https://journalclub.io/episodes/enabling-per-file-data-recovery-from-ransomware-attacks-via-file-system-forensics-and-flash-translation-layer-data-extraction) |
| Source | [https://www.semanticscholar.org/paper/32811b74e7323799aec3119af7b72da007a83964](https://www.semanticscholar.org/paper/32811b74e7323799aec3119af7b72da007a83964) |
| Year | 2026 |
| Citations | 3 |
| Authors | Josh Dafoe, Niusen Chen, Bo Chen, Zhenlin Wang |
| Paper ID | `7a61c5a9-f51d-4616-b00d-48edacf3dd31` |

## Classification

- **Problem Type:** data recovery from ransomware attacks
- **Domain:** Cybersecurity
- **Sub-domain:** File system forensics, Flash translation layer
- **Technique:** FFRecovery
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents FFRecovery, a novel ransomware defense strategy that enables fine-grained per-file data recovery from ransomware attacks by leveraging file system forensics and flash translation layer data extraction. Engineers should care because it addresses the limitations of existing recovery solutions by allowing users to selectively recover critical files instead of restoring entire disks.

## Key Contribution

**FFRecovery is the first cross-layer data recovery design against ransomware that collaborates multiple layers of a storage system for file-driven recovery.**

## Problem

The increasing prevalence of ransomware attacks that encrypt user files necessitates effective recovery solutions that do not require paying ransoms.

## Method

**Approach:** FFRecovery restores corrupted files by first recovering the file system metadata using file system forensics, then extracting the original file data from the flash memory using raw data extraction techniques, and finally assembling the metadata and data to restore the file. It incorporates a garbage collection delay and freeze mechanism to prevent data loss during recovery.

**Algorithm:**

1. 1. Detect ransomware and stop its execution.
2. 2. Identify the files that need recovery based on user input.
3. 3. Restore the file system metadata using forensic analysis.
4. 4. Extract the original file data from the flash memory.
5. 5. Re-map the logical disk locations to the physical flash memory locations.
6. 6. Assemble the restored metadata and data into a recoverable file.
7. 7. Present the recovered files to the user.

**Input:** User input specifying which files to recover, and the flash memory data.

**Output:** Restored files in their original state.

**Key Parameters:**

- `garbage_collection_delay: configurable (not specified)`
- `freeze_mechanism: enabled (default)`
- `file_system_type: EXT3, EXT4, NTFS, FAT32, exFAT (based on user environment)`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Real-world ransomware samples from 54 families

**Results:**

- Recovery rate: not specified
- Storage cost: negligible
- Performance impact: negligible

**Compared against:** Existing ransomware recovery solutions like CLDSafe, RockFS, PayBreak

**Improvement:** FFRecovery allows for fine-grained recovery, which is a significant improvement over existing solutions that require full disk restoration.

## Implementation Guide

**Data Structures:** File system metadata structures (inodes, directory entries), Mapping tables for logical to physical address translation

**Dependencies:** File system libraries, Flash memory access libraries, Ransomware detection tools

**Core Operation:**

```python
def recover_file(file_id): restore_metadata(file_id); data = extract_raw_data(file_id); return assemble_file(metadata, data)
```

**Watch Out For:**

- Ensure the garbage collection mechanism is properly configured to prevent data loss.
- Be aware of the specific file system type being used for accurate metadata restoration.
- Monitor the performance impact during recovery operations.

## Use This When

- You need to recover specific files after a ransomware attack.
- You want to minimize downtime by selectively restoring critical files.
- You are working with flash memory storage systems.

## Don't Use When

- The ransomware operates with root privileges.
- You have a reliable off-site backup solution.
- The storage medium is not flash-based.

## Key Concepts

file system forensics, flash translation layer, out-of-place updates, ransomware detection, data extraction, metadata restoration

## Connects To

- File system recovery techniques
- Data backup solutions
- Ransomware detection algorithms

## Prerequisites

- Understanding of file system structures
- Knowledge of flash memory operations
- Familiarity with ransomware behavior

## Limitations

- Only applicable to user-space ransomware
- Dependent on the integrity of the flash memory
- May not recover files if garbage collection has occurred

## Open Questions

- How to enhance recovery for root-level ransomware?
- What additional optimizations can be made for performance?

## Abstract

User-space ransomware works within the permissions granted to standard user accounts. This means it cannot modify system-level configurations or access kernel data. This also means, critically, that if you have backups or restore-points in protected areas that require administrator privileges, those are also safe. What the ransomware can do is encrypt most user files, as these are typically within the permissions of a standard account. Root-privileged ransomware, on the other hand, is significantly harder to detect and mitigate. Root-level ransomware can disable security tools, encrypt backups, and render entire systems inoperable. Today we're looking at a paper that presents a new mitigation option for user-space ransomware only. It won't really apply to anything operating with root privileges.
