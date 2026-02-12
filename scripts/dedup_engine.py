"""
CodeScholar Deduplication Engine
Prevents duplicate papers when aggregating from multiple sources.

Strategies:
  1. DOI exact match (highest confidence)
  2. arXiv ID exact match
  3. Semantic Scholar ID exact match
  4. Title fuzzy match (Levenshtein distance)
"""

import re
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass


@dataclass
class DeduplicationResult:
    """Result of deduplication check"""
    is_duplicate: bool
    match_type: Optional[str] = None  # "doi", "arxiv_id", "s2_id", "title"
    confidence: float = 0.0
    matched_paper_id: Optional[str] = None


def normalize_doi(doi: Optional[str]) -> Optional[str]:
    """Normalize DOI for comparison"""
    if not doi:
        return None
    # Lowercase, strip whitespace
    doi = doi.strip().lower()
    # Remove common DOI URL prefixes
    doi = re.sub(r'^https?://(?:dx\.)?doi\.org/', '', doi)
    return doi


def normalize_title(title: Optional[str]) -> str:
    """Normalize title for fuzzy matching"""
    if not title:
        return ""
    # Lowercase
    title = title.lower()
    # Remove punctuation
    title = re.sub(r'[^\w\s]', '', title)
    # Collapse whitespace
    title = re.sub(r'\s+', ' ', title).strip()
    return title


def levenshtein_distance(s1: str, s2: str) -> int:
    """Calculate Levenshtein edit distance between two strings"""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    prev_row = range(len(s2) + 1)

    for i, c1 in enumerate(s1):
        curr_row = [i + 1]
        for j, c2 in enumerate(s2):
            # Cost is 0 if characters match, 1 otherwise
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (c1 != c2)
            curr_row.append(min(insertions, deletions, substitutions))
        prev_row = curr_row

    return prev_row[-1]


def title_similarity(title1: str, title2: str) -> float:
    """
    Calculate title similarity score (0.0 to 1.0)

    Uses normalized Levenshtein distance
    """
    norm1 = normalize_title(title1)
    norm2 = normalize_title(title2)

    if not norm1 or not norm2:
        return 0.0

    if norm1 == norm2:
        return 1.0

    max_len = max(len(norm1), len(norm2))
    if max_len == 0:
        return 0.0

    distance = levenshtein_distance(norm1, norm2)
    return 1.0 - (distance / max_len)


class DeduplicationEngine:
    """
    Deduplication engine for paper library

    Maintains indexes for fast duplicate detection
    """

    def __init__(self):
        self.doi_index: Dict[str, str] = {}      # normalized_doi -> paper_id
        self.arxiv_index: Dict[str, str] = {}     # arxiv_id -> paper_id
        self.s2_index: Dict[str, str] = {}        # s2_id -> paper_id
        self.title_index: Dict[str, str] = {}     # normalized_title -> paper_id
        self.papers: Dict[str, Dict] = {}         # paper_id -> paper

    def build_index(self, papers: List[Dict]):
        """
        Build deduplication indexes from existing library

        Args:
            papers: List of papers in unified format
        """
        self.doi_index.clear()
        self.arxiv_index.clear()
        self.s2_index.clear()
        self.title_index.clear()
        self.papers.clear()

        for paper in papers:
            paper_id = paper.get("id", "")
            self.papers[paper_id] = paper

            # Index by DOI
            doi = normalize_doi(paper.get("identifiers", {}).get("doi"))
            if doi:
                self.doi_index[doi] = paper_id

            # Index by arXiv ID
            arxiv_id = paper.get("identifiers", {}).get("arxiv_id")
            if arxiv_id:
                self.arxiv_index[arxiv_id] = paper_id

            # Index by S2 ID
            s2_id = paper.get("identifiers", {}).get("semantic_scholar_id")
            if s2_id:
                self.s2_index[s2_id] = paper_id

            # Index by normalized title
            title = normalize_title(paper.get("title"))
            if title:
                self.title_index[title] = paper_id

    def check_duplicate(
        self,
        paper: Dict,
        title_threshold: float = 0.9
    ) -> DeduplicationResult:
        """
        Check if a paper is a duplicate of an existing paper

        Args:
            paper: Paper to check
            title_threshold: Minimum title similarity for fuzzy match (default: 0.9)

        Returns:
            DeduplicationResult with match info
        """
        identifiers = paper.get("identifiers", {})

        # Strategy 1: DOI exact match (highest confidence)
        doi = normalize_doi(identifiers.get("doi"))
        if doi and doi in self.doi_index:
            return DeduplicationResult(
                is_duplicate=True,
                match_type="doi",
                confidence=1.0,
                matched_paper_id=self.doi_index[doi]
            )

        # Strategy 2: arXiv ID exact match
        arxiv_id = identifiers.get("arxiv_id")
        if arxiv_id and arxiv_id in self.arxiv_index:
            return DeduplicationResult(
                is_duplicate=True,
                match_type="arxiv_id",
                confidence=1.0,
                matched_paper_id=self.arxiv_index[arxiv_id]
            )

        # Strategy 3: Semantic Scholar ID exact match
        s2_id = identifiers.get("semantic_scholar_id")
        if s2_id and s2_id in self.s2_index:
            return DeduplicationResult(
                is_duplicate=True,
                match_type="s2_id",
                confidence=1.0,
                matched_paper_id=self.s2_index[s2_id]
            )

        # Strategy 4: Title fuzzy match
        title = paper.get("title", "")
        if title:
            norm_title = normalize_title(title)

            # Exact normalized title match first
            if norm_title in self.title_index:
                return DeduplicationResult(
                    is_duplicate=True,
                    match_type="title",
                    confidence=0.95,
                    matched_paper_id=self.title_index[norm_title]
                )

            # Fuzzy title match
            best_similarity = 0.0
            best_match_id = None

            for existing_title, paper_id in self.title_index.items():
                similarity = title_similarity(title, existing_title)
                if similarity > best_similarity:
                    best_similarity = similarity
                    best_match_id = paper_id

            if best_similarity >= title_threshold:
                return DeduplicationResult(
                    is_duplicate=True,
                    match_type="title",
                    confidence=best_similarity,
                    matched_paper_id=best_match_id
                )

        # No duplicate found
        return DeduplicationResult(is_duplicate=False)

    def deduplicate_batch(
        self,
        new_papers: List[Dict],
        title_threshold: float = 0.9
    ) -> Tuple[List[Dict], List[Dict]]:
        """
        Deduplicate a batch of new papers against existing library

        Args:
            new_papers: New papers to check
            title_threshold: Title similarity threshold

        Returns:
            Tuple of (unique_papers, duplicate_papers)
        """
        unique = []
        duplicates = []

        # Also deduplicate within the batch itself
        batch_titles: Set[str] = set()
        batch_dois: Set[str] = set()

        for paper in new_papers:
            # Check against existing library
            result = self.check_duplicate(paper, title_threshold)

            if result.is_duplicate:
                duplicates.append({
                    "paper": paper,
                    "match_type": result.match_type,
                    "confidence": result.confidence,
                    "matched_paper_id": result.matched_paper_id
                })
                continue

            # Check against other papers in this batch
            doi = normalize_doi(paper.get("identifiers", {}).get("doi"))
            title = normalize_title(paper.get("title"))

            if doi and doi in batch_dois:
                duplicates.append({
                    "paper": paper,
                    "match_type": "doi_within_batch",
                    "confidence": 1.0
                })
                continue

            if title and title in batch_titles:
                duplicates.append({
                    "paper": paper,
                    "match_type": "title_within_batch",
                    "confidence": 0.95
                })
                continue

            # Paper is unique
            unique.append(paper)

            if doi:
                batch_dois.add(doi)
            if title:
                batch_titles.add(title)

        return unique, duplicates
