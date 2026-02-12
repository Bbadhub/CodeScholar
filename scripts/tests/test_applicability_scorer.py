"""
Test suite for applicability_scorer.py
"""

import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from applicability_scorer import (
    ApplicabilityScorer,
    ScoredPaper,
    concept_overlap_score,
    text_relevance_score,
    recency_score,
    citation_score,
)


class TestConceptOverlapScore:
    """Test concept overlap between code and paper"""

    def test_full_overlap(self):
        code_concepts = {"neural network", "deep learning", "backpropagation"}
        paper_text = "This paper presents a neural network with deep learning and backpropagation"
        score = concept_overlap_score(code_concepts, paper_text)
        assert score >= 0.8

    def test_partial_overlap(self):
        code_concepts = {"neural network", "deep learning", "sorting algorithm"}
        paper_text = "A neural network architecture for image classification"
        score = concept_overlap_score(code_concepts, paper_text)
        assert 0.2 < score < 0.8

    def test_no_overlap(self):
        code_concepts = {"binary tree", "sorting algorithm"}
        paper_text = "Analyzing protein folding mechanisms in biology"
        score = concept_overlap_score(code_concepts, paper_text)
        assert score < 0.2

    def test_empty_concepts(self):
        score = concept_overlap_score(set(), "some paper text")
        assert score == 0.0

    def test_empty_text(self):
        score = concept_overlap_score({"neural network"}, "")
        assert score == 0.0


class TestTextRelevanceScore:
    """Test text-based relevance scoring"""

    def test_high_relevance(self):
        query = "transformer attention mechanism"
        title = "Attention Is All You Need: The Transformer Architecture"
        abstract = "We propose a new architecture based solely on attention mechanisms"
        score = text_relevance_score(query, title, abstract)
        assert score >= 0.5

    def test_title_match_beats_abstract(self):
        query = "gradient descent optimization"
        title1 = "Gradient Descent Optimization Methods"
        abstract1 = "A review of various methods."
        title2 = "Random Paper Title"
        abstract2 = "This discusses gradient descent optimization in detail."

        score1 = text_relevance_score(query, title1, abstract1)
        score2 = text_relevance_score(query, title2, abstract2)
        # Title match should score higher
        assert score1 > score2

    def test_no_relevance(self):
        query = "quantum computing"
        title = "Cooking Recipes from Around the World"
        abstract = "A collection of traditional recipes."
        score = text_relevance_score(query, title, abstract)
        assert score < 0.2

    def test_empty_query(self):
        score = text_relevance_score("", "Some Title", "Some abstract")
        assert score == 0.0


class TestRecencyScore:
    """Test publication recency scoring"""

    def test_recent_paper(self):
        score = recency_score(2025)
        assert score >= 0.8

    def test_older_paper(self):
        score = recency_score(2010)
        assert score < 0.5

    def test_very_old_paper(self):
        score = recency_score(1990)
        assert score < 0.3

    def test_none_year(self):
        score = recency_score(None)
        assert score == 0.5  # neutral score

    def test_future_year(self):
        score = recency_score(2027)
        assert score >= 0.9


class TestCitationScore:
    """Test citation impact scoring"""

    def test_high_citations(self):
        score = citation_score(5000)
        assert score >= 0.8

    def test_moderate_citations(self):
        score = citation_score(50)
        assert 0.3 < score < 0.8

    def test_zero_citations(self):
        score = citation_score(0)
        assert score == 0.0

    def test_none_citations(self):
        score = citation_score(None)
        assert score == 0.0


class TestApplicabilityScorer:
    """Test the full applicability scorer"""

    @pytest.fixture
    def scorer(self):
        return ApplicabilityScorer()

    @pytest.fixture
    def sample_papers(self):
        return [
            {
                "id": "paper-1",
                "title": "Deep Learning for Computer Vision",
                "abstract": "We present a convolutional neural network architecture for image classification using deep learning techniques with attention mechanisms.",
                "metadata": {"year": 2024, "citation_count": 150},
                "identifiers": {"doi": "10.1234/dl.cv"},
            },
            {
                "id": "paper-2",
                "title": "Sorting Algorithms: A Comprehensive Survey",
                "abstract": "This survey covers quicksort, mergesort, heapsort and their computational complexity analysis.",
                "metadata": {"year": 2020, "citation_count": 30},
                "identifiers": {"doi": "10.1234/sort"},
            },
            {
                "id": "paper-3",
                "title": "Transformer Models for Natural Language Processing",
                "abstract": "We introduce a transformer-based model using self-attention for text classification and generation.",
                "metadata": {"year": 2023, "citation_count": 500},
                "identifiers": {"doi": "10.1234/nlp"},
            },
            {
                "id": "paper-4",
                "title": "Marine Biology and Ocean Currents",
                "abstract": "A study of marine ecosystems and their relationship to ocean temperature changes.",
                "metadata": {"year": 2024, "citation_count": 10},
                "identifiers": {"doi": "10.1234/bio"},
            },
        ]

    def test_score_paper_relevant(self, scorer, sample_papers):
        code_concepts = {"neural network", "deep learning", "attention mechanism"}
        result = scorer.score_paper(sample_papers[0], code_concepts, "deep learning neural network")
        assert isinstance(result, ScoredPaper)
        assert result.total_score > 0.5
        assert result.paper_id == "paper-1"

    def test_score_paper_irrelevant(self, scorer, sample_papers):
        code_concepts = {"neural network", "deep learning"}
        result = scorer.score_paper(sample_papers[3], code_concepts, "deep learning neural network")
        assert result.total_score < 0.3

    def test_score_batch(self, scorer, sample_papers):
        code_concepts = {"neural network", "deep learning", "attention mechanism", "transformer"}
        query = "deep learning transformer attention"
        results = scorer.score_batch(sample_papers, code_concepts, query)

        assert len(results) == 4
        # Results should be sorted by score descending
        assert results[0].total_score >= results[1].total_score
        # Top 2 should be the highly relevant ML papers (paper-1 and paper-3)
        top_ids = {r.paper_id for r in results[:2]}
        assert "paper-1" in top_ids
        assert "paper-3" in top_ids

    def test_score_batch_with_threshold(self, scorer, sample_papers):
        code_concepts = {"neural network", "deep learning"}
        query = "deep learning neural network"
        results = scorer.score_batch(
            sample_papers, code_concepts, query, min_score=0.3
        )
        # Biology paper should be filtered out
        ids = {r.paper_id for r in results}
        assert "paper-4" not in ids

    def test_score_breakdown(self, scorer, sample_papers):
        code_concepts = {"transformer", "attention mechanism"}
        result = scorer.score_paper(sample_papers[2], code_concepts, "transformer attention")
        # Score breakdown should have individual components
        assert "concept_overlap" in result.breakdown
        assert "text_relevance" in result.breakdown
        assert "recency" in result.breakdown
        assert "citation_impact" in result.breakdown
        # All components should be between 0 and 1
        for key, val in result.breakdown.items():
            assert 0.0 <= val <= 1.0, f"{key} = {val} out of range"

    def test_custom_weights(self):
        scorer = ApplicabilityScorer(weights={
            "concept_overlap": 0.8,
            "text_relevance": 0.1,
            "recency": 0.05,
            "citation_impact": 0.05,
        })
        # Weights should sum to 1.0
        assert abs(sum(scorer.weights.values()) - 1.0) < 0.01
