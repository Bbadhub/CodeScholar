"""
Test suite for dedup_engine.py
"""

import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from dedup_engine import (
    DeduplicationEngine,
    normalize_doi,
    normalize_title,
    levenshtein_distance,
    title_similarity,
    DeduplicationResult
)


class TestNormalization:
    """Test normalization functions"""

    def test_normalize_doi_basic(self):
        assert normalize_doi("10.1234/test.5678") == "10.1234/test.5678"

    def test_normalize_doi_url(self):
        assert normalize_doi("https://doi.org/10.1234/test.5678") == "10.1234/test.5678"

    def test_normalize_doi_dx_url(self):
        assert normalize_doi("https://dx.doi.org/10.1234/test.5678") == "10.1234/test.5678"

    def test_normalize_doi_case(self):
        assert normalize_doi("10.1234/TEST.5678") == "10.1234/test.5678"

    def test_normalize_doi_none(self):
        assert normalize_doi(None) is None

    def test_normalize_doi_empty(self):
        assert normalize_doi("") is None

    def test_normalize_title_basic(self):
        assert normalize_title("Machine Learning") == "machine learning"

    def test_normalize_title_punctuation(self):
        assert normalize_title("A Novel Approach: Using ML!") == "a novel approach using ml"

    def test_normalize_title_whitespace(self):
        assert normalize_title("  Machine   Learning  ") == "machine learning"

    def test_normalize_title_none(self):
        assert normalize_title(None) == ""


class TestLevenshteinDistance:
    """Test edit distance calculation"""

    def test_identical(self):
        assert levenshtein_distance("hello", "hello") == 0

    def test_one_edit(self):
        assert levenshtein_distance("hello", "hallo") == 1

    def test_completely_different(self):
        assert levenshtein_distance("abc", "xyz") == 3

    def test_empty_string(self):
        assert levenshtein_distance("", "hello") == 5

    def test_both_empty(self):
        assert levenshtein_distance("", "") == 0


class TestTitleSimilarity:
    """Test title similarity scoring"""

    def test_identical_titles(self):
        assert title_similarity("Machine Learning", "Machine Learning") == 1.0

    def test_case_insensitive(self):
        assert title_similarity("Machine Learning", "machine learning") == 1.0

    def test_similar_titles(self):
        sim = title_similarity(
            "A Novel Approach to Machine Learning",
            "A Novel Approach to Machine Learing"  # typo
        )
        assert sim > 0.9

    def test_different_titles(self):
        sim = title_similarity(
            "Machine Learning for Image Recognition",
            "Quantum Computing in Financial Markets"
        )
        assert sim < 0.5

    def test_empty_title(self):
        assert title_similarity("", "Machine Learning") == 0.0


class TestDeduplicationEngine:
    """Test deduplication engine"""

    @pytest.fixture
    def engine(self):
        """Create engine with sample library"""
        engine = DeduplicationEngine()
        papers = [
            {
                "id": "paper-1",
                "title": "Deep Learning for Computer Vision",
                "identifiers": {
                    "doi": "10.1234/dl.cv.2024",
                    "arxiv_id": "2401.12345",
                    "semantic_scholar_id": "abc123"
                }
            },
            {
                "id": "paper-2",
                "title": "Natural Language Processing with Transformers",
                "identifiers": {
                    "doi": "10.5678/nlp.trans.2024",
                    "arxiv_id": None,
                    "semantic_scholar_id": "def456"
                }
            },
            {
                "id": "paper-3",
                "title": "Graph Neural Networks for Social Analysis",
                "identifiers": {
                    "doi": None,
                    "arxiv_id": "2402.67890",
                    "semantic_scholar_id": None
                }
            }
        ]
        engine.build_index(papers)
        return engine

    def test_detect_doi_duplicate(self, engine):
        """Test DOI-based duplicate detection"""
        new_paper = {
            "title": "Some Other Title",
            "identifiers": {"doi": "10.1234/dl.cv.2024"}
        }
        result = engine.check_duplicate(new_paper)

        assert result.is_duplicate is True
        assert result.match_type == "doi"
        assert result.confidence == 1.0
        assert result.matched_paper_id == "paper-1"

    def test_detect_doi_url_duplicate(self, engine):
        """Test DOI URL normalization"""
        new_paper = {
            "title": "Some Title",
            "identifiers": {"doi": "https://doi.org/10.1234/dl.cv.2024"}
        }
        result = engine.check_duplicate(new_paper)

        assert result.is_duplicate is True
        assert result.match_type == "doi"

    def test_detect_arxiv_duplicate(self, engine):
        """Test arXiv ID-based duplicate detection"""
        new_paper = {
            "title": "Different Title",
            "identifiers": {"arxiv_id": "2401.12345"}
        }
        result = engine.check_duplicate(new_paper)

        assert result.is_duplicate is True
        assert result.match_type == "arxiv_id"
        assert result.matched_paper_id == "paper-1"

    def test_detect_s2_duplicate(self, engine):
        """Test Semantic Scholar ID duplicate detection"""
        new_paper = {
            "title": "Yet Another Title",
            "identifiers": {"semantic_scholar_id": "def456"}
        }
        result = engine.check_duplicate(new_paper)

        assert result.is_duplicate is True
        assert result.match_type == "s2_id"
        assert result.matched_paper_id == "paper-2"

    def test_detect_title_duplicate(self, engine):
        """Test title-based fuzzy duplicate detection"""
        new_paper = {
            "title": "Deep Learning for Computer Vision",
            "identifiers": {}
        }
        result = engine.check_duplicate(new_paper)

        assert result.is_duplicate is True
        assert result.match_type == "title"
        assert result.confidence >= 0.95

    def test_detect_title_fuzzy_match(self, engine):
        """Test fuzzy title matching with minor differences"""
        new_paper = {
            "title": "Deep Learning for Computer Vison",  # typo
            "identifiers": {}
        }
        result = engine.check_duplicate(new_paper)

        assert result.is_duplicate is True
        assert result.match_type == "title"
        assert result.confidence >= 0.9

    def test_no_duplicate(self, engine):
        """Test unique paper detection"""
        new_paper = {
            "title": "Quantum Computing Applications in Finance",
            "identifiers": {"doi": "10.9999/unique.paper"}
        }
        result = engine.check_duplicate(new_paper)

        assert result.is_duplicate is False

    def test_batch_dedup(self, engine):
        """Test batch deduplication"""
        new_papers = [
            # Duplicate by DOI
            {"title": "Paper A", "identifiers": {"doi": "10.1234/dl.cv.2024"}},
            # Unique
            {"title": "Unique Paper About Robotics", "identifiers": {"doi": "10.9999/unique"}},
            # Duplicate by title
            {"title": "Natural Language Processing with Transformers", "identifiers": {}},
            # Unique
            {"title": "Blockchain for Supply Chain", "identifiers": {"doi": "10.8888/blockchain"}},
        ]

        unique, duplicates = engine.deduplicate_batch(new_papers)

        assert len(unique) == 2
        assert len(duplicates) == 2
        assert unique[0]["title"] == "Unique Paper About Robotics"
        assert unique[1]["title"] == "Blockchain for Supply Chain"

    def test_batch_dedup_within_batch(self, engine):
        """Test deduplication within the same batch"""
        new_papers = [
            {"title": "New Unique Paper", "identifiers": {"doi": "10.1111/new.1"}},
            {"title": "Another Paper", "identifiers": {"doi": "10.2222/new.2"}},
            {"title": "New Unique Paper", "identifiers": {"doi": "10.1111/new.1"}},  # Same DOI
        ]

        unique, duplicates = engine.deduplicate_batch(new_papers)

        assert len(unique) == 2
        assert len(duplicates) == 1
        assert duplicates[0]["match_type"] == "doi_within_batch"

    def test_build_index_counts(self, engine):
        """Test that indexes are built correctly"""
        assert len(engine.doi_index) == 2  # paper-1 and paper-2 have DOIs
        assert len(engine.arxiv_index) == 2  # paper-1 and paper-3 have arXiv IDs
        assert len(engine.s2_index) == 2  # paper-1 and paper-2 have S2 IDs
        assert len(engine.title_index) == 3  # All papers have titles

    def test_empty_paper(self, engine):
        """Test with paper with no identifiers"""
        new_paper = {
            "title": "Completely New and Unique Research",
            "identifiers": {}
        }
        result = engine.check_duplicate(new_paper)

        assert result.is_duplicate is False
