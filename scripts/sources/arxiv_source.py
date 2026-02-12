"""
arXiv Paper Source
Search and discover papers from arXiv API

API: https://export.arxiv.org/api/query
Rate limit: 3 seconds between requests (per arXiv guidelines)
"""

import asyncio
import aiohttp
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional
from datetime import datetime
import time
import re

# Configuration
ARXIV_API_URL = "https://export.arxiv.org/api/query"
RATE_LIMIT_DELAY = 3.0  # arXiv requires 3 sec between requests
MAX_RESULTS = 50

# arXiv Atom namespace
ATOM_NS = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"

# Rate limiting
_last_request_time = 0


async def rate_limit():
    """Enforce arXiv rate limit (3 sec between requests)"""
    global _last_request_time

    current_time = time.time()
    time_since_last = current_time - _last_request_time

    if time_since_last < RATE_LIMIT_DELAY:
        await asyncio.sleep(RATE_LIMIT_DELAY - time_since_last)

    _last_request_time = time.time()


async def search_arxiv(
    query: str,
    max_results: int = 10,
    sort_by: str = "relevance",
    categories: Optional[List[str]] = None
) -> List[Dict]:
    """
    Search arXiv for papers

    Args:
        query: Search query (supports arXiv query syntax)
        max_results: Maximum results to return (max 50)
        sort_by: Sort order - "relevance", "lastUpdatedDate", "submittedDate"
        categories: Optional arXiv category filter (e.g., ["cs.AI", "cs.LG"])

    Returns:
        List of paper dicts in unified format
    """
    max_results = min(max_results, MAX_RESULTS)

    # Build query
    search_query = query
    if categories:
        cat_filter = " OR ".join(f"cat:{cat}" for cat in categories)
        search_query = f"({query}) AND ({cat_filter})"

    # Map sort parameter
    sort_map = {
        "relevance": "relevance",
        "lastUpdatedDate": "lastUpdatedDate",
        "submittedDate": "submittedDate"
    }

    params = {
        "search_query": f"all:{search_query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": sort_map.get(sort_by, "relevance"),
        "sortOrder": "descending"
    }

    await rate_limit()

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(ARXIV_API_URL, params=params, timeout=aiohttp.ClientTimeout(total=30)) as response:
                if response.status != 200:
                    print(f"[ERROR] arXiv API returned status {response.status}")
                    return []

                xml_text = await response.text()
                return parse_arxiv_response(xml_text)

    except asyncio.TimeoutError:
        print(f"[ERROR] arXiv API timeout for query: {query}")
        return []
    except Exception as e:
        print(f"[ERROR] arXiv API error: {e}")
        return []


def parse_arxiv_response(xml_text: str) -> List[Dict]:
    """
    Parse arXiv Atom XML response

    Args:
        xml_text: Raw XML response

    Returns:
        List of paper dicts
    """
    papers = []

    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        print(f"[ERROR] Failed to parse arXiv XML: {e}")
        return []

    for entry in root.findall(f"{ATOM_NS}entry"):
        paper = parse_arxiv_entry(entry)
        if paper:
            papers.append(paper)

    return papers


def parse_arxiv_entry(entry) -> Optional[Dict]:
    """Parse a single arXiv entry into unified format"""
    try:
        # Extract basic fields
        title_elem = entry.find(f"{ATOM_NS}title")
        title = title_elem.text.strip().replace("\n", " ") if title_elem is not None and title_elem.text else ""

        summary_elem = entry.find(f"{ATOM_NS}summary")
        abstract = summary_elem.text.strip().replace("\n", " ") if summary_elem is not None and summary_elem.text else ""

        # Extract arXiv ID from entry id URL
        id_elem = entry.find(f"{ATOM_NS}id")
        arxiv_url = id_elem.text.strip() if id_elem is not None and id_elem.text else ""
        arxiv_id = extract_arxiv_id(arxiv_url)

        # Extract DOI if available
        doi_elem = entry.find(f"{ARXIV_NS}doi")
        doi = doi_elem.text.strip() if doi_elem is not None and doi_elem.text else None

        # Extract authors
        authors = []
        for author_elem in entry.findall(f"{ATOM_NS}author"):
            name_elem = author_elem.find(f"{ATOM_NS}name")
            if name_elem is not None and name_elem.text:
                authors.append(name_elem.text.strip())

        # Extract published date
        published_elem = entry.find(f"{ATOM_NS}published")
        published = published_elem.text.strip() if published_elem is not None and published_elem.text else None
        year = int(published[:4]) if published else None

        # Extract categories
        categories = []
        for cat_elem in entry.findall(f"{ATOM_NS}category"):
            term = cat_elem.get("term")
            if term:
                categories.append(term)

        # Extract PDF link
        pdf_url = None
        for link_elem in entry.findall(f"{ATOM_NS}link"):
            if link_elem.get("title") == "pdf":
                pdf_url = link_elem.get("href")
                break

        return {
            "title": title,
            "abstract": abstract,
            "authors": authors,
            "identifiers": {
                "arxiv_id": arxiv_id,
                "doi": doi,
                "doi_url": f"https://doi.org/{doi}" if doi else None
            },
            "metadata": {
                "year": year,
                "published_date": published,
                "categories": categories,
                "citation_count": None  # arXiv doesn't provide this
            },
            "sources": [{
                "source": "arxiv",
                "url": arxiv_url,
                "pdf_url": pdf_url,
                "discovered_at": datetime.now().isoformat()
            }]
        }

    except Exception as e:
        print(f"[ERROR] Failed to parse arXiv entry: {e}")
        return None


def extract_arxiv_id(url: str) -> Optional[str]:
    """Extract arXiv ID from URL"""
    if not url:
        return None

    # Match patterns like http://arxiv.org/abs/2301.12345v1
    match = re.search(r'arxiv\.org/abs/(.+?)(?:v\d+)?$', url)
    if match:
        return match.group(1)

    return None


# Common CS arXiv categories for CodeScholar
CS_CATEGORIES = [
    "cs.AI",   # Artificial Intelligence
    "cs.LG",   # Machine Learning
    "cs.CL",   # Computation and Language
    "cs.CV",   # Computer Vision
    "cs.DS",   # Data Structures and Algorithms
    "cs.SE",   # Software Engineering
    "cs.PL",   # Programming Languages
    "cs.DB",   # Databases
    "cs.CR",   # Cryptography and Security
    "cs.DC",   # Distributed Computing
    "cs.NE",   # Neural and Evolutionary Computing
    "cs.IR",   # Information Retrieval
    "cs.RO",   # Robotics
    "cs.SI",   # Social and Information Networks
    "stat.ML", # Machine Learning (Statistics)
]
