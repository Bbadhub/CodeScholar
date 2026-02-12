"""
Test suite for enhance_existing_papers.py
TDD approach - write tests FIRST
"""

import json
import pytest
from pathlib import Path
import sys
from unittest.mock import Mock, patch, AsyncMock
import asyncio

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from enhance_existing_papers import (
    query_semantic_scholar,
    enhance_paper,
    rate_limit,
    load_unified_library,
    save_enhanced_library
)


class TestEnhancePapers:
    """Test suite for Semantic Scholar enhancement"""

    @pytest.fixture
    def sample_unified_paper(self):
        """Sample paper from unified_library.json"""
        return {
            "id": "test-uuid-123",
            "title": "Test Paper on Optimization",
            "abstract": "This is a test abstract.",
            "authors": [],
            "identifiers": {
                "doi": "10.1234/test.5678",
                "doi_url": "https://doi.org/10.1234/test.5678",
                "journalclub_slug": "test-paper",
                "semantic_scholar_id": None,
                "arxiv_id": None
            },
            "sources": [{
                "source": "journalclub",
                "url": "https://journalclub.io/episodes/test",
                "discovered_at": "2026-01-20T01:53:38Z"
            }],
            "metadata": {
                "year": 2024,
                "citation_count": None,
                "published_date": None
            }
        }

    @pytest.fixture
    def mock_s2_response(self):
        """Mock Semantic Scholar API response"""
        return {
            "paperId": "abc123def456",
            "title": "Test Paper on Optimization",
            "abstract": "This is a test abstract.",
            "citationCount": 42,
            "authors": [
                {"name": "John Smith", "authorId": "12345"},
                {"name": "Jane Doe", "authorId": "67890"}
            ],
            "year": 2024,
            "publicationDate": "2024-03-15"
        }

    @pytest.mark.asyncio
    async def test_query_semantic_scholar_success(self, mock_s2_response):
        """Test querying Semantic Scholar API successfully"""
        with patch('aiohttp.ClientSession.get') as mock_get:
            # Setup mock response
            mock_resp = AsyncMock()
            mock_resp.status = 200
            mock_resp.json = AsyncMock(return_value=mock_s2_response)
            mock_get.return_value.__aenter__.return_value = mock_resp

            # Act
            result = await query_semantic_scholar("10.1234/test.5678")

            # Assert
            assert result is not None
            assert result["paperId"] == "abc123def456"
            assert result["citationCount"] == 42
            assert len(result["authors"]) == 2

    @pytest.mark.asyncio
    async def test_query_semantic_scholar_not_found(self):
        """Test handling DOI not found in Semantic Scholar"""
        with patch('aiohttp.ClientSession.get') as mock_get:
            # Setup mock 404 response
            mock_resp = AsyncMock()
            mock_resp.status = 404
            mock_get.return_value.__aenter__.return_value = mock_resp

            # Act
            result = await query_semantic_scholar("10.9999/notfound")

            # Assert
            assert result is None

    @pytest.mark.asyncio
    async def test_query_semantic_scholar_rate_limit(self):
        """Test handling rate limiting (429)"""
        with patch('aiohttp.ClientSession.get') as mock_get:
            # Setup mock 429 response
            mock_resp = AsyncMock()
            mock_resp.status = 429
            mock_get.return_value.__aenter__.return_value = mock_resp

            # Act
            result = await query_semantic_scholar("10.1234/test.5678")

            # Assert - Should return None after retries
            assert result is None

    @pytest.mark.asyncio
    async def test_enhance_paper_with_s2_data(self, sample_unified_paper, mock_s2_response):
        """Test enhancing paper with Semantic Scholar data"""
        with patch('enhance_existing_papers.query_semantic_scholar', return_value=mock_s2_response):
            # Act
            enhanced = await enhance_paper(sample_unified_paper)

            # Assert
            assert enhanced["metadata"]["citation_count"] == 42
            assert len(enhanced["authors"]) == 2
            assert enhanced["authors"][0] == "John Smith"
            assert enhanced["identifiers"]["semantic_scholar_id"] == "abc123def456"

            # Check new source added
            s2_sources = [s for s in enhanced["sources"] if s["source"] == "semantic_scholar"]
            assert len(s2_sources) == 1
            assert "abc123def456" in s2_sources[0]["url"]

    @pytest.mark.asyncio
    async def test_enhance_paper_without_doi(self, sample_unified_paper):
        """Test enhancing paper without DOI (skip enhancement)"""
        # Remove DOI
        sample_unified_paper["identifiers"]["doi"] = None

        # Act
        enhanced = await enhance_paper(sample_unified_paper)

        # Assert - Paper unchanged
        assert enhanced["metadata"]["citation_count"] is None
        assert len(enhanced["authors"]) == 0

    @pytest.mark.asyncio
    async def test_enhance_paper_s2_not_found(self, sample_unified_paper):
        """Test enhancing paper when not found in Semantic Scholar"""
        with patch('enhance_existing_papers.query_semantic_scholar', return_value=None):
            # Act
            enhanced = await enhance_paper(sample_unified_paper)

            # Assert - Paper unchanged
            assert enhanced["metadata"]["citation_count"] is None
            assert len(enhanced["authors"]) == 0

    def test_load_unified_library(self, tmp_path):
        """Test loading unified_library.json"""
        # Arrange
        library_file = tmp_path / "unified_library.json"
        test_data = [{"id": "test", "title": "Test"}]
        library_file.write_text(json.dumps(test_data))

        # Act
        result = load_unified_library(str(library_file))

        # Assert
        assert len(result) == 1
        assert result[0]["id"] == "test"

    def test_save_enhanced_library(self, tmp_path, sample_unified_paper):
        """Test saving enhanced library"""
        # Arrange
        output_file = tmp_path / "enhanced_library.json"
        papers = [sample_unified_paper]

        # Act
        save_enhanced_library(papers, str(output_file))

        # Assert
        assert output_file.exists()

        with open(output_file) as f:
            saved = json.load(f)

        assert len(saved) == 1
        assert saved[0]["id"] == "test-uuid-123"

    @pytest.mark.asyncio
    async def test_rate_limiting(self):
        """Test rate limiting doesn't exceed 100 req/sec"""
        import time

        # Act - Make 10 requests with rate limiting
        start = time.time()
        for i in range(10):
            await rate_limit()
        end = time.time()

        # Assert - Should take at least 0.1 seconds (10 requests * 0.01 sec)
        assert end - start >= 0.09  # Allow slight variance

    @pytest.mark.asyncio
    async def test_handles_network_timeout(self, sample_unified_paper):
        """Test handling network timeouts"""
        with patch('aiohttp.ClientSession.get', side_effect=asyncio.TimeoutError):
            # Act
            enhanced = await enhance_paper(sample_unified_paper)

            # Assert - Paper returned unchanged on timeout
            assert enhanced == sample_unified_paper

    @pytest.mark.asyncio
    async def test_preserves_existing_sources(self, sample_unified_paper, mock_s2_response):
        """Test that existing sources are preserved when adding S2 source"""
        with patch('enhance_existing_papers.query_semantic_scholar', return_value=mock_s2_response):
            # Act
            enhanced = await enhance_paper(sample_unified_paper)

            # Assert
            assert len(enhanced["sources"]) == 2  # Original + Semantic Scholar
            journalclub_sources = [s for s in enhanced["sources"] if s["source"] == "journalclub"]
            assert len(journalclub_sources) == 1
