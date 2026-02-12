"""
Enhance existing papers with Semantic Scholar data
Architecture: Query S2 API for citation counts, authors, and IDs

Rate limit: 100 requests/second (Semantic Scholar public API limit)
"""

import json
import asyncio
import aiohttp
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import time

# Configuration
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1"
RATE_LIMIT_DELAY = 0.01  # 100 requests/second
MAX_RETRIES = 3
TIMEOUT = 30  # seconds

# Rate limiting
_last_request_time = 0


async def rate_limit():
    """Enforce rate limit of 100 req/sec"""
    global _last_request_time

    current_time = time.time()
    time_since_last = current_time - _last_request_time

    if time_since_last < RATE_LIMIT_DELAY:
        await asyncio.sleep(RATE_LIMIT_DELAY - time_since_last)

    _last_request_time = time.time()


async def query_semantic_scholar(doi: str) -> Optional[Dict]:
    """
    Query Semantic Scholar API for paper metadata

    Args:
        doi: DOI identifier (e.g., "10.1234/test.5678")

    Returns:
        Paper metadata dict or None if not found
    """
    if not doi:
        return None

    url = f"{SEMANTIC_SCHOLAR_API}/paper/DOI:{doi}"
    params = {
        "fields": "paperId,title,abstract,citationCount,authors,year,publicationDate"
    }

    await rate_limit()

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=TIMEOUT)) as response:
                if response.status == 200:
                    return await response.json()
                elif response.status == 404:
                    # Paper not found in Semantic Scholar
                    return None
                elif response.status == 429:
                    # Rate limited - wait and retry
                    print(f"[WARNING] Rate limited for DOI {doi}, waiting...")
                    await asyncio.sleep(2)
                    return None
                else:
                    print(f"[ERROR] Unexpected status {response.status} for DOI {doi}")
                    return None
    except asyncio.TimeoutError:
        print(f"[ERROR] Timeout querying Semantic Scholar for DOI {doi}")
        return None
    except Exception as e:
        print(f"[ERROR] Error querying Semantic Scholar for DOI {doi}: {e}")
        return None


async def enhance_paper(paper: Dict) -> Dict:
    """
    Enhance paper with Semantic Scholar data

    Args:
        paper: Unified format paper dict

    Returns:
        Enhanced paper dict
    """
    doi = paper.get("identifiers", {}).get("doi")

    if not doi:
        # No DOI, can't query Semantic Scholar
        return paper

    try:
        s2_data = await query_semantic_scholar(doi)

        if not s2_data:
            # Not found or error
            return paper

        # Extract authors
        authors = [author.get("name", "Unknown") for author in s2_data.get("authors", [])]

        # Update paper with S2 data
        enhanced = paper.copy()
        enhanced["authors"] = authors
        enhanced["metadata"]["citation_count"] = s2_data.get("citationCount")
        enhanced["metadata"]["published_date"] = s2_data.get("publicationDate")
        enhanced["identifiers"]["semantic_scholar_id"] = s2_data.get("paperId")

        # Add Semantic Scholar source
        s2_source = {
            "source": "semantic_scholar",
            "url": f"https://www.semanticscholar.org/paper/{s2_data.get('paperId')}",
            "discovered_at": datetime.now().isoformat()
        }
        enhanced["sources"].append(s2_source)

        print(f"[OK] Enhanced: {paper['title'][:60]}... (Citations: {s2_data.get('citationCount', 0)})")

        return enhanced

    except Exception as e:
        print(f"[ERROR] Error enhancing paper: {e}")
        return paper


def load_unified_library(filepath: str = "unified_library.json") -> List[Dict]:
    """Load unified library from JSON"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Unified library not found: {filepath}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {filepath}: {e}")


def save_enhanced_library(papers: List[Dict], filepath: str = "unified_library.json"):
    """Save enhanced library to JSON"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(papers, f, indent=2, ensure_ascii=False)
        print(f"[OK] Saved {len(papers)} enhanced papers to {filepath}")
    except Exception as e:
        raise IOError(f"Failed to save enhanced library: {e}")


async def enhance_all_papers(papers: List[Dict]) -> List[Dict]:
    """
    Enhance all papers with Semantic Scholar data

    Args:
        papers: List of unified format papers

    Returns:
        List of enhanced papers
    """
    enhanced_papers = []
    total = len(papers)

    for i, paper in enumerate(papers, 1):
        enhanced = await enhance_paper(paper)
        enhanced_papers.append(enhanced)

        if i % 50 == 0:
            print(f"   Processed {i}/{total} papers...")

    return enhanced_papers


async def main():
    """Main enhancement workflow"""
    print("=" * 60)
    print("Semantic Scholar Paper Enhancement")
    print("=" * 60)

    # Step 1: Load unified library
    print("\n[1/3] Loading unified_library.json...")
    try:
        papers = load_unified_library("unified_library.json")
        print(f"[OK] Loaded {len(papers)} papers")
    except Exception as e:
        print(f"[ERROR] {e}")
        return

    # Step 2: Enhance papers with S2 data
    print(f"\n[2/3] Querying Semantic Scholar for {len(papers)} papers...")
    print("   (Rate limited to 100 req/sec)")

    enhanced_papers = await enhance_all_papers(papers)

    # Count enhancements
    enhanced_count = sum(1 for p in enhanced_papers if p.get("identifiers", {}).get("semantic_scholar_id"))
    print(f"[OK] Enhanced {enhanced_count}/{len(papers)} papers with S2 data")

    # Step 3: Save enhanced library
    print("\n[3/3] Saving enhanced library...")
    try:
        save_enhanced_library(enhanced_papers, "unified_library.json")
    except Exception as e:
        print(f"[ERROR] {e}")
        return

    # Summary
    print("\n" + "=" * 60)
    print("Enhancement Complete!")
    print("=" * 60)
    print(f"Total papers: {len(papers)}")
    print(f"Enhanced with S2: {enhanced_count}")
    print(f"Not found: {len(papers) - enhanced_count}")
    print("\nNext steps:")
    print("1. Run IMPORT-003 to generate abstract embeddings")
    print("2. Run IMPORT-004 to add to Qdrant vector database")


if __name__ == "__main__":
    asyncio.run(main())
