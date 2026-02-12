"""
Generate embeddings for paper abstracts using OpenAI API
Architecture: Embed abstracts for semantic search

Model: text-embedding-3-large (3072 dimensions)
Rate limit: 3000 RPM (50 requests/second)
Cost: ~$0.13 per 1M tokens
"""

import json
import asyncio
import openai
from pathlib import Path
from typing import Dict, List, Optional
import time
import os

# Configuration
EMBEDDING_MODEL = "text-embedding-3-large"
EMBEDDING_DIMENSIONS = 3072
RATE_LIMIT_DELAY = 0.02  # 50 requests/second (3000 RPM)
BATCH_SIZE = 50  # Process in batches for progress tracking


class OpenAIEmbedder:
    """OpenAI embedding generator with rate limiting"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize OpenAI embedder

        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key required (set OPENAI_API_KEY env var)")

        self.client = openai.AsyncOpenAI(api_key=self.api_key)
        self._last_request_time = 0

    async def rate_limit(self):
        """Enforce rate limit of 50 req/sec (3000 RPM)"""
        current_time = time.time()
        time_since_last = current_time - self._last_request_time

        if time_since_last < RATE_LIMIT_DELAY:
            await asyncio.sleep(RATE_LIMIT_DELAY - time_since_last)

        self._last_request_time = time.time()

    async def generate_embedding(self, text: str) -> Optional[List[float]]:
        """
        Generate embedding for text using OpenAI API

        Args:
            text: Text to embed

        Returns:
            Embedding vector (3072 dimensions) or None if error
        """
        if not text or not text.strip():
            return None

        await self.rate_limit()

        try:
            response = await self.client.embeddings.create(
                model=EMBEDDING_MODEL,
                input=text,
                encoding_format="float"
            )

            return response.data[0].embedding

        except TimeoutError:
            print(f"[ERROR] Timeout generating embedding")
            return None
        except Exception as e:
            print(f"[ERROR] Error generating embedding: {e}")
            return None

    async def embed_paper(self, paper: Dict) -> Dict:
        """
        Embed paper abstract

        Args:
            paper: Unified format paper dict

        Returns:
            Paper with embedding in analysis.embedding field
        """
        abstract = paper.get("abstract", "").strip()

        if not abstract:
            # No abstract, can't embed
            return paper

        try:
            embedding = await self.generate_embedding(abstract)

            if embedding:
                # Update paper with embedding
                embedded = paper.copy()
                embedded["analysis"]["embedding"] = embedding

                print(f"[OK] Embedded: {paper['title'][:60]}... ({len(abstract)} chars)")

                return embedded
            else:
                return paper

        except Exception as e:
            print(f"[ERROR] Error embedding paper: {e}")
            return paper


def load_library(filepath: str = "unified_library.json") -> List[Dict]:
    """Load unified library from JSON"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Library file not found: {filepath}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {filepath}: {e}")


def save_library(papers: List[Dict], filepath: str = "unified_library.json"):
    """Save library with embeddings to JSON"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(papers, f, indent=2, ensure_ascii=False)
        print(f"[OK] Saved {len(papers)} papers with embeddings to {filepath}")
    except Exception as e:
        raise IOError(f"Failed to save library: {e}")


def calculate_embedding_stats(papers: List[Dict]) -> Dict:
    """
    Calculate embedding coverage statistics

    Args:
        papers: List of papers

    Returns:
        Stats dict with total, embedded, not_embedded, coverage
    """
    total = len(papers)
    embedded = sum(1 for p in papers if p.get("analysis", {}).get("embedding"))
    not_embedded = total - embedded
    coverage = (embedded / total * 100) if total > 0 else 0

    return {
        "total_papers": total,
        "embedded": embedded,
        "not_embedded": not_embedded,
        "embedding_coverage": round(coverage, 1)
    }


async def embed_all_papers(embedder: OpenAIEmbedder, papers: List[Dict]) -> List[Dict]:
    """
    Embed all papers with progress tracking

    Args:
        embedder: OpenAIEmbedder instance
        papers: List of papers to embed

    Returns:
        List of papers with embeddings
    """
    embedded_papers = []
    total = len(papers)

    for i, paper in enumerate(papers, 1):
        embedded = await embedder.embed_paper(paper)
        embedded_papers.append(embedded)

        if i % BATCH_SIZE == 0:
            print(f"   Processed {i}/{total} papers...")

    return embedded_papers


async def main():
    """Main embedding generation workflow"""
    print("=" * 60)
    print("Paper Abstract Embedding Generation")
    print("=" * 60)

    # Step 1: Initialize OpenAI embedder
    print("\n[1/4] Initializing OpenAI embedder...")
    try:
        embedder = OpenAIEmbedder()
        print(f"[OK] Using model: {EMBEDDING_MODEL}")
        print(f"   Dimensions: {EMBEDDING_DIMENSIONS}")
        print(f"   Rate limit: 50 req/sec (3000 RPM)")
    except ValueError as e:
        print(f"[ERROR] {e}")
        print("\nSet OPENAI_API_KEY environment variable:")
        print("   export OPENAI_API_KEY='your-api-key'  (Linux/Mac)")
        print("   set OPENAI_API_KEY=your-api-key       (Windows)")
        return

    # Step 2: Load unified library
    print("\n[2/4] Loading unified_library.json...")
    try:
        papers = load_library("unified_library.json")
        print(f"[OK] Loaded {len(papers)} papers")
    except Exception as e:
        print(f"[ERROR] {e}")
        return

    # Step 3: Generate embeddings
    print(f"\n[3/4] Generating embeddings for {len(papers)} papers...")
    print("   (This will take ~9 minutes at 50 req/sec)")

    embedded_papers = await embed_all_papers(embedder, papers)

    # Calculate stats
    stats = calculate_embedding_stats(embedded_papers)
    print(f"[OK] Generated embeddings: {stats['embedded']}/{stats['total_papers']}")
    print(f"   Coverage: {stats['embedding_coverage']}%")

    # Step 4: Save library with embeddings
    print("\n[4/4] Saving library with embeddings...")
    try:
        save_library(embedded_papers, "unified_library.json")

        # Calculate file size
        import os
        file_size_mb = os.path.getsize("unified_library.json") / (1024 * 1024)
        print(f"\n[INFO] File size: {file_size_mb:.2f} MB")

    except Exception as e:
        print(f"[ERROR] {e}")
        return

    # Summary
    print("\n" + "=" * 60)
    print("Embedding Generation Complete!")
    print("=" * 60)
    print(f"Total papers: {stats['total_papers']}")
    print(f"Embedded: {stats['embedded']}")
    print(f"Not embedded: {stats['not_embedded']}")
    print(f"Coverage: {stats['embedding_coverage']}%")
    print("\nNext steps:")
    print("1. Run IMPORT-004 to add papers to Qdrant vector database")
    print("2. Run MCP-001 to setup CodeScholar MCP server")


if __name__ == "__main__":
    asyncio.run(main())
