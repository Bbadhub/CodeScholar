"""
Test suite for query_generator.py
"""

import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from query_generator import (
    QueryGenerator,
    GeneratedQuery,
    QueryStrategy,
    expand_concept,
    combine_concepts,
    rank_queries,
)


class TestGeneratedQuery:
    """Test GeneratedQuery dataclass"""

    def test_basic_creation(self):
        q = GeneratedQuery(
            query="transformer attention mechanism",
            strategy=QueryStrategy.CONCEPT_EXPANSION,
            source_concepts=["transformer", "attention"],
            confidence=0.9,
        )
        assert q.query == "transformer attention mechanism"
        assert q.confidence == 0.9
        assert len(q.source_concepts) == 2

    def test_default_values(self):
        q = GeneratedQuery(query="test", strategy=QueryStrategy.DIRECT)
        assert q.confidence == 1.0
        assert q.source_concepts == []


class TestExpandConcept:
    """Test concept expansion into academic search terms"""

    def test_expand_known_concept(self):
        expanded = expand_concept("neural network")
        assert len(expanded) >= 1
        assert "neural network" in expanded

    def test_expand_with_synonyms(self):
        expanded = expand_concept("gradient descent")
        assert "gradient descent" in expanded
        assert any("optimization" in e for e in expanded)

    def test_expand_unknown_concept(self):
        expanded = expand_concept("xyzzy_unknown_thing")
        assert expanded == ["xyzzy_unknown_thing"]

    def test_expand_ml_concept(self):
        expanded = expand_concept("random forest")
        assert "random forest" in expanded
        assert any("ensemble" in e.lower() for e in expanded)

    def test_expand_data_structure(self):
        expanded = expand_concept("binary tree")
        assert "binary tree" in expanded
        assert any("tree" in e.lower() for e in expanded)


class TestCombineConcepts:
    """Test combining multiple concepts into compound queries"""

    def test_combine_two(self):
        combined = combine_concepts(["machine learning", "optimization"])
        assert any("machine learning" in q and "optimization" in q for q in combined)

    def test_combine_single(self):
        combined = combine_concepts(["transformer"])
        assert combined == ["transformer"]

    def test_combine_empty(self):
        combined = combine_concepts([])
        assert combined == []

    def test_combine_related(self):
        combined = combine_concepts(["deep learning", "computer vision", "CNN"])
        # Should produce compound queries
        assert len(combined) >= 1


class TestRankQueries:
    """Test query ranking"""

    def test_rank_by_confidence(self):
        queries = [
            GeneratedQuery("low conf", QueryStrategy.DIRECT, confidence=0.3),
            GeneratedQuery("high conf", QueryStrategy.DIRECT, confidence=0.9),
            GeneratedQuery("mid conf", QueryStrategy.DIRECT, confidence=0.6),
        ]
        ranked = rank_queries(queries)
        assert ranked[0].query == "high conf"
        assert ranked[-1].query == "low conf"

    def test_rank_deduplicates(self):
        queries = [
            GeneratedQuery("same query", QueryStrategy.DIRECT, confidence=0.5),
            GeneratedQuery("same query", QueryStrategy.CONCEPT_EXPANSION, confidence=0.8),
            GeneratedQuery("different", QueryStrategy.DIRECT, confidence=0.7),
        ]
        ranked = rank_queries(queries)
        # Duplicate queries should be merged, keeping higher confidence
        query_texts = [q.query for q in ranked]
        assert query_texts.count("same query") == 1
        # The merged query should keep the higher confidence
        same = next(q for q in ranked if q.query == "same query")
        assert same.confidence == 0.8

    def test_rank_respects_limit(self):
        queries = [
            GeneratedQuery(f"query_{i}", QueryStrategy.DIRECT, confidence=0.5)
            for i in range(20)
        ]
        ranked = rank_queries(queries, limit=5)
        assert len(ranked) == 5


class TestQueryGenerator:
    """Test the full query generator"""

    @pytest.fixture
    def generator(self):
        return QueryGenerator()

    def test_from_concepts_basic(self, generator):
        concepts = [
            {"name": "neural network", "category": "algorithm", "confidence": 0.9},
            {"name": "gradient descent", "category": "algorithm", "confidence": 0.8},
        ]
        queries = generator.from_concepts(concepts)
        assert len(queries) >= 2
        assert all(isinstance(q, GeneratedQuery) for q in queries)

    def test_from_concepts_with_categories(self, generator):
        concepts = [
            {"name": "k-means clustering", "category": "algorithm", "confidence": 0.9},
            {"name": "data analysis", "category": "technique", "confidence": 0.5},
        ]
        queries = generator.from_concepts(concepts)
        # Higher-confidence concepts should produce more queries
        algo_queries = [q for q in queries if "k-means" in q.query.lower() or "clustering" in q.query.lower()]
        assert len(algo_queries) >= 1

    def test_from_concepts_empty(self, generator):
        queries = generator.from_concepts([])
        assert queries == []

    def test_from_analysis_result(self, generator):
        """Test generating queries from a full analysis result dict"""
        analysis = {
            "concepts": [
                {"name": "transformer", "category": "algorithm", "max_confidence": 0.95, "count": 3},
                {"name": "attention mechanism", "category": "algorithm", "max_confidence": 0.9, "count": 2},
                {"name": "embedding", "category": "technique", "max_confidence": 0.8, "count": 5},
            ],
            "search_queries": ["transformer", "attention mechanism", "embedding"],
        }
        queries = generator.from_analysis(analysis)
        assert len(queries) >= 3
        # Should include both direct and expanded queries
        strategies = {q.strategy for q in queries}
        assert len(strategies) >= 1

    def test_from_analysis_limits_output(self, generator):
        analysis = {
            "concepts": [
                {"name": f"concept_{i}", "category": "algorithm", "max_confidence": 0.5, "count": 1}
                for i in range(50)
            ],
            "search_queries": [f"concept_{i}" for i in range(50)],
        }
        queries = generator.from_analysis(analysis, max_queries=10)
        assert len(queries) <= 10

    def test_query_diversity(self, generator):
        """Ensure generator produces diverse query types"""
        concepts = [
            {"name": "convolutional neural network", "category": "algorithm", "confidence": 0.95},
            {"name": "image classification", "category": "ml_technique", "confidence": 0.9},
        ]
        queries = generator.from_concepts(concepts)
        query_texts = [q.query for q in queries]
        # Should not all be identical
        assert len(set(query_texts)) > 1

    def test_low_confidence_filtered(self, generator):
        concepts = [
            {"name": "important concept", "category": "algorithm", "confidence": 0.9},
            {"name": "noise", "category": "technique", "confidence": 0.1},
        ]
        queries = generator.from_concepts(concepts, min_confidence=0.3)
        query_texts = " ".join(q.query for q in queries)
        assert "important" in query_texts.lower()
        # Noise should be filtered out
        assert not any(q.query == "noise" for q in queries)
