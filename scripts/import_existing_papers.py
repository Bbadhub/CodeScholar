"""
Import existing Journal Club papers to unified format
Architecture: Metadata + Abstract Only (no PDF storage)

Converts metadata.json (443 papers) to unified format for CodeScholar.
Saves 1.2 GB by storing only metadata + abstracts, accessing PDFs via DOI on-demand.
"""

import json
import uuid
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


def generate_uuid() -> str:
    """Generate unique UUID for paper"""
    return str(uuid.uuid4())


def extract_year(scraped_at: str) -> int:
    """Extract year from scraped_at timestamp"""
    try:
        dt = datetime.fromisoformat(scraped_at.replace('Z', '+00:00'))
        return dt.year
    except Exception:
        return datetime.now().year


def find_pdf_path(slug: str, pdf_dir: str = "pdfs") -> Optional[str]:
    """
    Check if PDF exists for this paper
    NOTE: With metadata-only approach, this is just for validation
    We won't actually store PDFs long-term
    """
    pdf_path = Path(pdf_dir) / f"{slug}.pdf"
    return str(pdf_path) if pdf_path.exists() else None


def convert_to_unified_format(paper: Dict) -> Dict:
    """
    Convert Journal Club paper to unified CodeScholar format

    Architecture Decision: Metadata + Abstract Only
    - Store: title, abstract, DOI, metadata
    - Don't store: PDF files locally
    - Access: Full papers via DOI link on-demand
    - Savings: 1.2 GB (40x space reduction)
    """
    return {
        # Unique identifier
        "id": generate_uuid(),

        # Core content (sufficient for semantic search)
        "title": paper["title"],
        "abstract": paper.get("description", ""),  # Journal Club descriptions as abstracts
        "authors": [],  # Will be enriched from Semantic Scholar in IMPORT-002

        # Identifiers (DOI provides permanent access to full paper)
        "identifiers": {
            "doi": paper.get("doi"),
            "doi_url": paper.get("doi_url"),  # Direct link to full PDF
            "journalclub_slug": paper["slug"],
            "semantic_scholar_id": None,  # Will be added in IMPORT-002
            "arxiv_id": None
        },

        # Multiple sources (paper may appear in Journal Club + arXiv + Semantic Scholar)
        "sources": [{
            "source": "journalclub",
            "url": paper["url"],
            "doi_url": paper.get("doi_url"),
            "description": paper.get("description"),
            "discovered_at": paper["scraped_at"]
        }],

        # Metadata
        "metadata": {
            "published_date": None,  # Will be enriched from Semantic Scholar
            "year": extract_year(paper["scraped_at"]),
            "citation_count": None,  # Will be added in IMPORT-002
            "categories": []  # Will be added for arXiv papers
        },

        # Files (no local storage, only links)
        "files": {
            "pdf_url": paper.get("doi_url"),  # Link to full paper (not local path)
            "downloaded": False,  # We don't download PDFs locally
            "local_path": None  # No local storage
        },

        # Analysis (will be populated in later tasks)
        "analysis": {
            "theories": [],  # Extracted in THEORY-001
            "embedding": None,  # Generated in IMPORT-003 (from abstract)
            "relevant_to": [],  # Linked in LINK-001
            "applicability_scores": {}  # Calculated in LINK-001
        }
    }


def load_metadata(metadata_file: str = "metadata.json") -> List[Dict]:
    """Load existing Journal Club metadata.json"""
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Metadata file not found: {metadata_file}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {metadata_file}: {e}")


def save_unified_library(papers: List[Dict], output_file: str = "unified_library.json"):
    """Save unified library to JSON"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(papers, f, indent=2, ensure_ascii=False)
        print(f"[OK] Saved {len(papers)} papers to {output_file}")
    except Exception as e:
        raise IOError(f"Failed to save unified library: {e}")


def validate_output(papers: List[Dict]) -> Dict:
    """Validate converted papers and generate report"""
    report = {
        "total_papers": len(papers),
        "with_doi": sum(1 for p in papers if p["identifiers"]["doi"]),
        "with_abstract": sum(1 for p in papers if p["abstract"]),
        "unique_ids": len(set(p["id"] for p in papers)),
        "schema_valid": True
    }

    # Validate schema
    required_fields = ["id", "title", "abstract", "identifiers", "sources", "metadata", "files", "analysis"]
    for paper in papers:
        for field in required_fields:
            if field not in paper:
                report["schema_valid"] = False
                print(f"[ERROR] Missing field '{field}' in paper: {paper.get('title', 'Unknown')}")

    return report


def main():
    """Main import workflow"""
    print("=" * 60)
    print("CodeScholar Paper Import")
    print("Architecture: Metadata + Abstract Only")
    print("=" * 60)

    # Step 1: Load existing Journal Club metadata
    print("\n[1/4] Loading metadata.json...")
    try:
        metadata = load_metadata("metadata.json")
        print(f"[OK] Loaded {len(metadata)} papers from Journal Club")
    except Exception as e:
        print(f"[ERROR] Error loading metadata: {e}")
        return

    # Step 2: Convert to unified format
    print("\n[2/4] Converting to unified format...")
    unified_papers = []
    errors = 0

    for i, paper in enumerate(metadata, 1):
        try:
            converted = convert_to_unified_format(paper)
            unified_papers.append(converted)

            if i % 50 == 0:
                print(f"   Processed {i}/{len(metadata)} papers...")
        except Exception as e:
            errors += 1
            print(f"[ERROR] Error converting paper {i}: {e}")
            # Continue processing other papers

    print(f"[OK] Converted {len(unified_papers)} papers ({errors} errors)")

    # Step 3: Validate output
    print("\n[3/4] Validating output...")
    report = validate_output(unified_papers)

    print(f"   Total papers: {report['total_papers']}")
    print(f"   With DOI: {report['with_doi']}")
    print(f"   With abstract: {report['with_abstract']}")
    print(f"   Unique IDs: {report['unique_ids']}")
    print(f"   Schema valid: {'[OK]' if report['schema_valid'] else '[ERROR]'}")

    if report['unique_ids'] != report['total_papers']:
        print("[WARNING]  Warning: Duplicate IDs detected!")

    # Step 4: Save unified library
    print("\n[4/4] Saving unified library...")
    try:
        save_unified_library(unified_papers, "unified_library.json")

        # Calculate space savings
        import os
        json_size = os.path.getsize("unified_library.json") / (1024 * 1024)  # MB
        print(f"\n[INFO] Space Analysis:")
        print(f"   Unified library: {json_size:.2f} MB")
        print(f"   vs. Original PDFs: 1,200 MB")
        print(f"   Space saved: {1200 - json_size:.2f} MB ({(1200 - json_size) / 1200 * 100:.1f}%)")
        print(f"\n[TIP] PDFs accessible via DOI links on-demand")

    except Exception as e:
        print(f"[ERROR] Error saving: {e}")
        return

    print("\n" + "=" * 60)
    print("[OK] Import Complete!")
    print("=" * 60)
    print(f"\nNext steps:")
    print(f"1. Run IMPORT-002 to enhance with Semantic Scholar data")
    print(f"2. Run IMPORT-003 to generate abstract embeddings")
    print(f"3. Run IMPORT-004 to add to Qdrant vector database")


if __name__ == "__main__":
    main()
