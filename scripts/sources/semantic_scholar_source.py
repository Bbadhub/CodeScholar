"""
Semantic Scholar Live Search Source
Search and discover papers from Semantic Scholar API

API: https://api.semanticscholar.org/graph/v1
Rate limit: 100 requests/second (public API)
"""

import asyncio
import aiohttp
from typing import Dict, List, Optional
from datetime import datetime
import time

# Configuration
S2_API_URL = "https://api.semanticscholar.org/graph/v1"
RATE_LIMIT_DELAY = 0.01  # 100 requests/second
TIMEOUT = 30
S2_FIELDS = "paperId,title,abstract,authors,year,citationCount,publicationDate,externalIds"

# Rate limiting
_last_request_time = 0


async def rate_limit():
    """Enforce Semantic Scholar rate limit"""
    global _last_request_time

    current_time = time.time()
    time_since_last = current_time - _last_request_time

    if time_since_last < RATE_LIMIT_DELAY:
        await asyncio.sleep(RATE_LIMIT_DELAY - time_since_last)

    _last_request_time = time.time()


async def search_semantic_scholar(
    query: str,
    max_results: int = 10,
    year: Optional[str] = None,
    fields_of_study: Optional[List[str]] = None
) -> List[Dict]:
    """
    Search Semantic Scholar for papers

    Args:
        query: Search query
        max_results: Maximum results (max 100)
        year: Year range filter (e.g., "2020-2024" or "2024")
        fields_of_study: Optional fields filter (e.g., ["Computer Science"])

    Returns:
        List of paper dicts in unified format
    """
    max_results = min(max_results, 100)

    params = {
        "query": query,
        "limit": max_results,
        "fields": S2_FIELDS
    }

    if year:
        params["year"] = year

    if fields_of_study:
        params["fieldsOfStudy"] = ",".join(fields_of_study)

    await rate_limit()

    try:
        async with aiohttp.ClientSession() as session:
            url = f"{S2_API_URL}/paper/search"
            async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=TIMEOUT)) as response:
                if response.status == 200:
                    data = await response.json()
                    return [parse_s2_paper(p) for p in data.get("data", []) if p]
                elif response.status == 429:
                    print("[WARNING] Semantic Scholar rate limited, waiting...")
                    await asyncio.sleep(2)
                    return []
                else:
                    print(f"[ERROR] S2 API returned status {response.status}")
                    return []

    except asyncio.TimeoutError:
        print(f"[ERROR] S2 API timeout for query: {query}")
        return []
    except Exception as e:
        print(f"[ERROR] S2 API error: {e}")
        return []


async def get_paper_recommendations(
    paper_id: str,
    max_results: int = 10
) -> List[Dict]:
    """
    Get paper recommendations based on a seed paper

    Args:
        paper_id: Semantic Scholar paper ID
        max_results: Maximum recommendations

    Returns:
        List of recommended paper dicts
    """
    await rate_limit()

    try:
        async with aiohttp.ClientSession() as session:
            url = f"{S2_API_URL}/recommendations/v1/papers/forpaper/{paper_id}"
            params = {"limit": max_results, "fields": S2_FIELDS}

            async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=TIMEOUT)) as response:
                if response.status == 200:
                    data = await response.json()
                    return [parse_s2_paper(p) for p in data.get("recommendedPapers", []) if p]
                else:
                    return []

    except Exception as e:
        print(f"[ERROR] S2 recommendations error: {e}")
        return []


def parse_s2_paper(paper_data: Dict) -> Dict:
    """
    Parse Semantic Scholar paper into unified format

    Args:
        paper_data: Raw S2 API response

    Returns:
        Unified format paper dict
    """
    # Extract authors
    authors = [a.get("name", "Unknown") for a in paper_data.get("authors", [])]

    # Extract external IDs
    external_ids = paper_data.get("externalIds", {}) or {}
    doi = external_ids.get("DOI")
    arxiv_id = external_ids.get("ArXiv")

    return {
        "title": paper_data.get("title", ""),
        "abstract": paper_data.get("abstract", ""),
        "authors": authors,
        "identifiers": {
            "semantic_scholar_id": paper_data.get("paperId"),
            "doi": doi,
            "doi_url": f"https://doi.org/{doi}" if doi else None,
            "arxiv_id": arxiv_id
        },
        "metadata": {
            "year": paper_data.get("year"),
            "citation_count": paper_data.get("citationCount"),
            "published_date": paper_data.get("publicationDate")
        },
        "sources": [{
            "source": "semantic_scholar",
            "url": f"https://www.semanticscholar.org/paper/{paper_data.get('paperId')}",
            "discovered_at": datetime.now().isoformat()
        }]
    }
