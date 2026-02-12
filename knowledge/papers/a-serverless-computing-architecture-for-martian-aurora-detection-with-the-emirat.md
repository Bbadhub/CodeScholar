# A serverless computing architecture for Martian aurora detection with the Emirates Mars Mission

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1038/s41598-024-53492-4` |
| Full Paper | [https://doi.org/10.1038/s41598-024-53492-4](https://doi.org/10.1038/s41598-024-53492-4) |
| Source | [https://journalclub.io/episodes/a-serverless-computing-architecture-for-martian-aurora-detection-with-the-emirates-mars-mission](https://journalclub.io/episodes/a-serverless-computing-architecture-for-martian-aurora-detection-with-the-emirates-mars-mission) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `ac5a739a-64b6-41d5-b7d1-f171029a9cee` |

## Classification

- **Problem Type:** image classification, object detection, remote sensing
- **Domain:** Machine Learning & AI
- **Sub-domain:** Computer Vision
- **Technique:** YOLOv5
- **Technique Category:** classification_model
- **Type:** novel

## Summary

The authors developed a serverless computing architecture for detecting Martian auroras using image analysis techniques. This system leverages cloud computing resources to efficiently process and analyze high volumes of image data from the Emirates Mars Mission, making it a valuable tool for planetary science.

## Key Contribution

**A novel serverless architecture for real-time detection and analysis of Martian auroras using AWS services and OpenCV.**

## Problem

The need for automated detection and analysis of Martian auroras to enhance understanding of the Martian atmosphere.

## Method

**Approach:** The method involves a serverless architecture utilizing AWS Lambda for preprocessing and classification of images. It employs OpenCV for image processing and YOLOv5 for object detection to identify Martian auroras.

**Algorithm:**

1. Open the raw data file using fits.open() to generate initial images.
2. Resize images to a uniform dimension of 640x480 pixels.
3. Crop images to focus on the Martian sphere.
4. Isolate the Martian sphere and create a binary image for edge detection.
5. Enhance edges and classify images using YOLOv5.

**Input:** Raw image data in emm_emu_l2b format.

**Output:** Classified images indicating the presence of Martian auroras.

**Key Parameters:**

- `image_size: 640x480`
- `threshold_value: adaptive thresholding method`
- `kernel_size: 4x4 for morphological operations`

**Complexity:** not stated

## Benchmarks

**Tested on:** 200 images from the Emirates Mars Mission

**Results:**

- accuracy: 100% for detecting Mars
- processing time: not stated

**Compared against:** Traditional image analysis methods

**Improvement:** Significantly faster and more cost-effective than traditional methods.

## Implementation Guide

**Data Structures:** Image arrays, Binary masks, S3 storage buckets

**Dependencies:** AWS Lambda, AWS S3, OpenCV, YOLOv5, Matplotlib, Astropy

**Core Operation:**

```python
def lambda_handler(event): process_images(event['data'])
```

**Watch Out For:**

- Ensure images are normalized to the same size before processing.
- Monitor AWS Lambda execution time to avoid unexpected costs.
- Handle potential errors in image data formats gracefully.

## Use This When

- You need to analyze large volumes of astronomical image data.
- Real-time detection of phenomena in remote sensing applications is required.
- You want to leverage cloud computing for scalable image processing.

## Don't Use When

- You require on-premises processing due to data privacy concerns.
- The image data is too small to justify cloud computing costs.
- You need a solution that does not rely on external cloud services.

## Key Concepts

serverless computing, image preprocessing, object detection, cloud architecture

## Connects To

- OpenCV for image processing
- AWS SageMaker for machine learning
- Cloud computing paradigms

## Prerequisites

- Understanding of cloud computing concepts
- Familiarity with image processing techniques
- Knowledge of machine learning frameworks

## Limitations

- Dependent on cloud service availability and costs.
- Requires internet access for data processing.
- Performance may vary based on image data quality.

## Open Questions

- How can the architecture be optimized for even larger datasets?
- What additional features can be integrated for enhanced analysis?

## Abstract

In this paper, the authors develop a detection and analysis framework, specifically geared at Martian aurora observation. An aurora is a natural light display in a planet's atmosphere, caused by charged particles colliding with atmospheric gases and emitting light. If you've heard of the Aurora Borealis (aka the "Northern Lights"), here on earth, that's probably the most famous example. The authors' system would allow users to identify auroras, classify their types, and analyze their properties. Let’s see what they built and how they built it. At a high level, their system is a data-driven image analysis pipeline. Rather than manually
