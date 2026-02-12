# Applied Key Information Extraction (KIE)

**A method for automating the extraction of key information from heterogeneous documents using OCR and LLMs.**

**Category:** optimization_algorithm  
**Maturity:** proven (widely used in production)

## How It Works

Applied Key Information Extraction leverages Amazon Textract to perform initial OCR processing on documents, extracting both text and layout data. This extracted data is then structured using user-defined prompts and processed through a large language model (LLM) to produce a final structured JSON output. The technique includes a rule-based post-processing module to refine specific fields and calculate confidence scores for the extracted information.

## Algorithm

**Input:** PDF document containing heterogeneous data (e.g., invoices)

**Output:** Structured JSON output containing extracted key information

**Steps:**

1. Input a PDF document and prompt instruction.
2. Use Amazon Textract to extract textual and structural data.
3. Create a configuration table for field schema, unit definitions, and special formats.
4. Process the OCR-extracted content with a user-defined prompt to structure the data.
5. Feed the structured prompt into an LLM for final JSON output.
6. Implement a rule-based post-processing module for specific fields.
7. Filter results and calculate confidence scores.
8. Handle user queries to extract targeted information.

**Core Operation:** `output = structured_prompt(LLM(OCR_output))`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `OCR tool` | Amazon Textract | Changing the OCR tool may affect the accuracy of text extraction. |
| `Field schema` | user-defined | Modifying the schema can change the structure and relevance of the extracted data. |
| `Confidence score calculation` | predefined formula | Altering the formula can impact the reliability of the extracted information. |

## Complexity

- **Time:** Not explicitly stated
- **Space:** Not explicitly stated
- **In practice:** Performance may vary based on document complexity and the efficiency of the OCR tool.

## Implementation

```python
def extract_key_info(document: str, prompt: str) -> dict:
    ocr_data = amazon_textract(document)
    structured_data = structure_data(ocr_data, prompt)
    json_output = llm_process(structured_data)
    refined_output = post_process(json_output)
    return refined_output
```

## Common Mistakes

- Neglecting to define a clear field schema, leading to poor extraction results.
- Overlooking the importance of post-processing, which can refine the accuracy of extracted fields.
- Using an inappropriate OCR tool that does not suit the document type.

## Use When

- You need to automate data extraction from invoices or receipts.
- You are dealing with heterogeneous document formats.
- You require high accuracy in information extraction with minimal training data.

## Avoid When

- You have a fixed format for all documents.
- You require real-time processing without any preprocessing.
- You need to extract information from highly structured documents.

## Tradeoffs

**Strengths:**

- High accuracy in extracting information from diverse document types.
- Ability to handle unstructured data effectively.
- Minimal training data required for effective performance.

**Weaknesses:**

- Not suitable for fixed-format documents.
- Requires preprocessing, which may delay real-time applications.
- Performance can vary significantly based on the quality of the OCR tool.

**Compared To:**

- **vs Standard OCR methods:** Use KIE for better accuracy and structure in heterogeneous documents.
- **vs NER-based methods:** KIE is preferable when dealing with complex document layouts.

## Connects To

- Optical Character Recognition (OCR)
- Natural Language Processing (NLP)
- Named Entity Recognition (NER)
- Document Layout Analysis
- Data Annotation Techniques

## Evidence (Papers)

- **Evaluation of Prompt Engineering on the Performance of a Large Language Model in Document Information Extraction** [4 citations] - [DOI](https://doi.org/10.3390/electronics14112145)
