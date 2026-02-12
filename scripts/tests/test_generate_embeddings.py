"""
Test suite for generate_embeddings.py
TDD approach - write tests FIRST
"""

import json
import pytest
from pathlib import Path
import sys
from unittest.mock import Mock, patch, AsyncMock
import numpy as np

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from generate_embeddings import (
    OpenAIEmbedder,
    load_library,
    save_library,
    calculate_embedding_stats
)


class TestGenerateEmbeddings:
    """Test suite for embedding generation"""

    @pytest.fixture
    def sample_paper(self):
        """Sample paper from unified_library.json"""
        return {
            "id": "test-uuid-123",
            "title": "Test Paper on Machine Learning",
            "abstract": "This paper presents a novel approach to machine learning using neural networks.",
            "authors": ["John Smith", "Jane Doe"],
            "identifiers": {
                "doi": "10.1234/test.5678",
                "semantic_scholar_id": "abc123"
            },
            "metadata": {
                "year": 2024,
                "citation_count": 42
            },
            "analysis": {
                "embedding": None,
                "theories": [],
                "relevant_to": []
            }
        }

    @pytest.fixture
    def mock_embedding_response(self):
        """Mock OpenAI embedding API response"""
        return {
            "data": [
                {
                    "embedding": list(np.random.rand(3072)),  # text-embedding-3-large dimension
                    "index": 0
                }
            ],
            "model": "text-embedding-3-large",
            "usage": {
                "prompt_tokens": 20,
                "total_tokens": 20
            }
        }

    @pytest.mark.asyncio
    async def test_generate_embedding_success(self, mock_embedding_response):
        """Test generating embedding from text"""
        with patch('generate_embeddings.openai.AsyncOpenAI') as mock_openai:
            # Setup mock
            mock_client = AsyncMock()
            mock_embeddings = AsyncMock()
            mock_embeddings.create = AsyncMock(return_value=type('Response', (), {'data': [type('Data', (), {'embedding': mock_embedding_response['data'][0]['embedding']})()]})())
            mock_client.embeddings = mock_embeddings
            mock_openai.return_value = mock_client

            # Act
            embedder = OpenAIEmbedder(api_key="test-key")
            embedding = await embedder.generate_embedding("Test text")

            # Assert
            assert embedding is not None
            assert len(embedding) == 3072  # text-embedding-3-large dimension
            assert isinstance(embedding, list)
            assert all(isinstance(x, float) for x in embedding)

    @pytest.mark.asyncio
    async def test_generate_embedding_empty_text(self):
        """Test handling empty text"""
        embedder = OpenAIEmbedder(api_key="test-key")

        embedding = await embedder.generate_embedding("")

        assert embedding is None

    @pytest.mark.asyncio
    async def test_embed_paper_with_abstract(self, sample_paper):
        """Test embedding paper with abstract"""
        embedder = OpenAIEmbedder(api_key="test-key")

        # Mock the generate_embedding method
        mock_embedding = list(np.random.rand(3072))
        with patch.object(embedder, 'generate_embedding', return_value=mock_embedding):
            # Act
            embedded = await embedder.embed_paper(sample_paper)

            # Assert
            assert embedded["analysis"]["embedding"] is not None
            assert len(embedded["analysis"]["embedding"]) == 3072
            assert embedded["id"] == sample_paper["id"]  # Preserved original data

    @pytest.mark.asyncio
    async def test_embed_paper_without_abstract(self, sample_paper):
        """Test embedding paper without abstract (skip)"""
        sample_paper["abstract"] = ""

        embedder = OpenAIEmbedder(api_key="test-key")
        embedded = await embedder.embed_paper(sample_paper)

        # Assert - Paper unchanged
        assert embedded["analysis"]["embedding"] is None

    @pytest.mark.asyncio
    async def test_rate_limiting(self):
        """Test rate limiting (3000 RPM = 50 RPS)"""
        import time

        embedder = OpenAIEmbedder(api_key="test-key")

        # Act - Make 5 requests with rate limiting
        start = time.time()
        for i in range(5):
            await embedder.rate_limit()
        end = time.time()

        # Assert - Should take at least 0.08 seconds (5 requests * 0.02 sec)
        assert end - start >= 0.08  # Allow slight variance

    def test_load_library(self, tmp_path):
        """Test loading unified library"""
        # Arrange
        library_file = tmp_path / "unified_library.json"
        test_data = [{"id": "test", "title": "Test"}]
        library_file.write_text(json.dumps(test_data))

        # Act
        result = load_library(str(library_file))

        # Assert
        assert len(result) == 1
        assert result[0]["id"] == "test"

    def test_save_library(self, tmp_path, sample_paper):
        """Test saving library with embeddings"""
        # Arrange
        output_file = tmp_path / "embedded_library.json"
        papers = [sample_paper]

        # Act
        save_library(papers, str(output_file))

        # Assert
        assert output_file.exists()

        with open(output_file) as f:
            saved = json.load(f)

        assert len(saved) == 1
        assert saved[0]["id"] == "test-uuid-123"

    def test_calculate_embedding_stats(self, sample_paper):
        """Test calculating embedding statistics"""
        # Arrange
        sample_paper["analysis"]["embedding"] = list(np.random.rand(3072))
        papers = [sample_paper, sample_paper.copy()]

        # Act
        stats = calculate_embedding_stats(papers)

        # Assert
        assert stats["total_papers"] == 2
        assert stats["embedded"] == 2
        assert stats["not_embedded"] == 0
        assert stats["embedding_coverage"] == 100.0

    def test_calculate_stats_partial_coverage(self, sample_paper):
        """Test stats with partial embedding coverage"""
        import copy

        # Arrange - Use deep copy to avoid shared nested dicts
        paper_with_embedding = copy.deepcopy(sample_paper)
        paper_with_embedding["analysis"]["embedding"] = list(np.random.rand(3072))

        paper_without_embedding = copy.deepcopy(sample_paper)
        paper_without_embedding["analysis"]["embedding"] = None

        papers = [paper_with_embedding, paper_without_embedding]

        # Act
        stats = calculate_embedding_stats(papers)

        # Assert
        assert stats["total_papers"] == 2
        assert stats["embedded"] == 1
        assert stats["not_embedded"] == 1
        assert stats["embedding_coverage"] == 50.0

    @pytest.mark.asyncio
    async def test_handles_api_timeout(self, sample_paper):
        """Test handling API timeouts"""
        embedder = OpenAIEmbedder(api_key="test-key")

        # Mock generate_embedding to raise TimeoutError
        with patch.object(embedder, 'generate_embedding', side_effect=TimeoutError):
            # Act
            embedded = await embedder.embed_paper(sample_paper)

            # Assert - Paper returned unchanged on timeout
            assert embedded["analysis"]["embedding"] is None

    @pytest.mark.asyncio
    async def test_preserves_existing_data(self, sample_paper):
        """Test that existing paper data is preserved"""
        embedder = OpenAIEmbedder(api_key="test-key")

        # Mock the generate_embedding method
        mock_embedding = list(np.random.rand(3072))
        with patch.object(embedder, 'generate_embedding', return_value=mock_embedding):
            # Act
            embedded = await embedder.embed_paper(sample_paper)

            # Assert - All original data preserved
            assert embedded["title"] == sample_paper["title"]
            assert embedded["abstract"] == sample_paper["abstract"]
            assert embedded["authors"] == sample_paper["authors"]
            assert embedded["identifiers"] == sample_paper["identifiers"]
            assert embedded["metadata"] == sample_paper["metadata"]
