"""
CodeScholar Applicability Scorer
Scores how relevant a paper is to specific code concepts.

Components:
  1. Concept overlap - how many code concepts appear in paper
  2. Text relevance - keyword matching in title/abstract
  3. Recency - newer papers score higher
  4. Citation impact - highly-cited papers score higher
"""

import math
import re
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
from datetime import datetime


CURRENT_YEAR = datetime.now().year

# Default scoring weights
DEFAULT_WEIGHTS = {
    "concept_overlap": 0.40,
    "text_relevance": 0.30,
    "recency": 0.15,
    "citation_impact": 0.15,
}


@dataclass
class ScoredPaper:
    """A paper with applicability scores"""
    paper_id: str
    title: str
    total_score: float
    breakdown: Dict[str, float] = field(default_factory=dict)
    matched_concepts: List[str] = field(default_factory=list)


def concept_overlap_score(code_concepts: Set[str], paper_text: str) -> float:
    """
    Score concept overlap between code concepts and paper text.

    Args:
        code_concepts: Set of concept strings from code analysis
        paper_text: Combined title + abstract text from paper

    Returns:
        Score from 0.0 to 1.0
    """
    if not code_concepts or not paper_text:
        return 0.0

    text_lower = paper_text.lower()
    matched = 0

    for concept in code_concepts:
        if concept.lower() in text_lower:
            matched += 1

    return matched / len(code_concepts)


def text_relevance_score(query: str, title: str, abstract: str) -> float:
    """
    Score text relevance of a paper to a search query.

    Title matches weighted 3x, abstract matches weighted 1x.

    Args:
        query: Search query string
        title: Paper title
        abstract: Paper abstract

    Returns:
        Score from 0.0 to 1.0
    """
    if not query:
        return 0.0

    terms = [t.lower() for t in query.split() if len(t) > 2]
    if not terms:
        return 0.0

    title_lower = (title or "").lower()
    abstract_lower = (abstract or "").lower()

    title_matches = sum(1 for t in terms if t in title_lower)
    abstract_matches = sum(1 for t in terms if t in abstract_lower)

    # Title match weighted 3x
    weighted = (title_matches * 3 + abstract_matches) / (len(terms) * 4)

    # Bonus for exact phrase match in title
    if query.lower() in title_lower:
        weighted = min(weighted + 0.2, 1.0)

    return min(weighted, 1.0)


def recency_score(year: Optional[int]) -> float:
    """
    Score paper recency (newer = higher).

    Uses exponential decay: score = e^(-0.05 * age)

    Args:
        year: Publication year

    Returns:
        Score from 0.0 to 1.0 (0.5 for unknown year)
    """
    if year is None:
        return 0.5

    age = max(CURRENT_YEAR - year, 0)
    return math.exp(-0.05 * age)


def citation_score(citations: Optional[int]) -> float:
    """
    Score citation impact using logarithmic scaling.

    score = log10(citations + 1) / log10(10001)

    Args:
        citations: Citation count

    Returns:
        Score from 0.0 to 1.0
    """
    if not citations:
        return 0.0

    # Logarithmic scale: 1 citation = 0.0, 10000+ = 1.0
    return min(math.log10(citations + 1) / math.log10(10001), 1.0)


class ApplicabilityScorer:
    """
    Scores paper relevance to code concepts.
    """

    def __init__(self, weights: Optional[Dict[str, float]] = None):
        self.weights = weights or DEFAULT_WEIGHTS.copy()

    def score_paper(
        self,
        paper: Dict,
        code_concepts: Set[str],
        query: str,
    ) -> ScoredPaper:
        """
        Score a single paper's applicability.

        Args:
            paper: Paper dict with title, abstract, metadata
            code_concepts: Set of concepts extracted from code
            query: Search query that found this paper

        Returns:
            ScoredPaper with total score and breakdown
        """
        title = paper.get("title", "")
        abstract = paper.get("abstract", "")
        paper_text = f"{title} {abstract}"
        year = paper.get("metadata", {}).get("year")
        citations = paper.get("metadata", {}).get("citation_count")

        # Calculate component scores
        overlap = concept_overlap_score(code_concepts, paper_text)
        text_rel = text_relevance_score(query, title, abstract)
        recency = recency_score(year)
        citation = citation_score(citations)

        breakdown = {
            "concept_overlap": round(overlap, 4),
            "text_relevance": round(text_rel, 4),
            "recency": round(recency, 4),
            "citation_impact": round(citation, 4),
        }

        # Weighted total
        total = (
            self.weights["concept_overlap"] * overlap
            + self.weights["text_relevance"] * text_rel
            + self.weights["recency"] * recency
            + self.weights["citation_impact"] * citation
        )

        # Find matched concepts
        text_lower = paper_text.lower()
        matched = [c for c in code_concepts if c.lower() in text_lower]

        return ScoredPaper(
            paper_id=paper.get("id", ""),
            title=title,
            total_score=round(total, 4),
            breakdown=breakdown,
            matched_concepts=matched,
        )

    def score_batch(
        self,
        papers: List[Dict],
        code_concepts: Set[str],
        query: str,
        min_score: float = 0.0,
    ) -> List[ScoredPaper]:
        """
        Score and rank a batch of papers.

        Args:
            papers: List of paper dicts
            code_concepts: Concepts from code analysis
            query: Search query
            min_score: Minimum score threshold

        Returns:
            Sorted list of ScoredPaper (highest first), filtered by min_score
        """
        scored = []
        for paper in papers:
            result = self.score_paper(paper, code_concepts, query)
            if result.total_score >= min_score:
                scored.append(result)

        scored.sort(key=lambda s: s.total_score, reverse=True)
        return scored
