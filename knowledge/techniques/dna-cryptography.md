# DNA Cryptography

*Also known as: DNA-based encryption, Biological cryptography*

**DNA Cryptography encodes data into DNA sequences for secure and durable storage.**

**Category:** data_storage, cryptography  
**Maturity:** emerging

## How It Works

DNA Cryptography involves converting data into binary format and then encoding it into DNA sequences using a predefined mapping. The synthesized DNA can be stored in a suitable medium, and to retrieve the data, the stored DNA is sequenced and decoded back into its original binary format. This method leverages the high storage density and durability of DNA as a medium for data storage.

## Algorithm

**Input:** Data in binary format.

**Output:** Data retrieved in its original format.

**Steps:**

1. 1. Convert data into binary format.
2. 2. Encode binary data into DNA sequences using a predefined mapping.
3. 3. Synthesize the DNA sequences for storage.
4. 4. Store the synthesized DNA in a suitable medium.
5. 5. To retrieve, sequence the stored DNA.
6. 6. Decode the sequenced DNA back into binary format.

**Core Operation:** `output = decode(sequenced_DNA)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `encoding_scheme` | custom mapping | Affects how efficiently data is encoded into DNA. |
| `synthesis_cost` | variable based on technology | Higher costs may limit practical applications. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Real-world performance can vary significantly based on synthesis technology and data size.

## Implementation

```python
def dna_encrypt(data: bytes) -> str:
    binary_data = convert_to_binary(data)
    dna_sequence = encode_to_dna(binary_data)
    store_dna(dna_sequence)

def dna_decrypt(dna_sequence: str) -> bytes:
    sequenced_dna = sequence_dna(dna_sequence)
    return decode_from_binary(sequenced_dna)
```

## Common Mistakes

- Using an inefficient encoding scheme that increases data size.
- Not considering the cost of DNA synthesis in the overall budget.
- Overlooking the need for proper storage conditions for synthesized DNA.

## Use When

- You need a highly durable storage solution for large datasets.
- You are working on secure data transmission methods.
- You want to explore innovative data storage technologies.

## Avoid When

- You require immediate access to data with low latency.
- The cost of DNA synthesis is prohibitive for your application.
- You are dealing with small amounts of data that can be easily stored using traditional methods.

## Tradeoffs

**Strengths:**

- High storage density compared to traditional methods.
- Durability and longevity of DNA as a storage medium.
- Potential for secure data transmission.

**Weaknesses:**

- High cost of DNA synthesis.
- Complexity of encoding and decoding processes.
- Latency in data retrieval compared to electronic storage.

**Compared To:**

- **vs Traditional storage methods:** Use DNA Cryptography for long-term storage and security; use traditional methods for speed and cost-effectiveness.

## Connects To

- Data encoding techniques
- Cryptographic methods
- Biological data storage
- Synthetic biology applications

## Evidence (Papers)

- **A Review of DNA Cryptography** [7 citations] - [DOI](https://doi.org/10.34133/icomputing.0106)
