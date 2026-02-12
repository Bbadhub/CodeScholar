"""
CodeScholar Smart Query Generator
Converts code analysis concepts into optimized academic search queries.

Strategies:
  1. Direct concept query (highest precision)
  2. Concept expansion with synonyms/related terms
  3. Compound queries combining related concepts
  4. Category-boosted queries (algorithm vs technique)
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum


class QueryStrategy(Enum):
    """Strategy used to generate a query"""
    DIRECT = "direct"
    CONCEPT_EXPANSION = "concept_expansion"
    COMPOUND = "compound"
    CATEGORY_BOOST = "category_boost"


@dataclass
class GeneratedQuery:
    """A generated search query with metadata"""
    query: str
    strategy: QueryStrategy
    source_concepts: List[str] = field(default_factory=list)
    confidence: float = 1.0


# Concept expansion mappings: concept -> related academic terms
CONCEPT_EXPANSIONS = {
    # ML/AI
    "neural network": ["neural network", "deep learning architecture", "artificial neural network"],
    "deep learning": ["deep learning", "neural network", "representation learning"],
    "machine learning": ["machine learning", "statistical learning", "predictive modeling"],
    "gradient descent": ["gradient descent", "stochastic optimization", "optimization algorithm"],
    "backpropagation": ["backpropagation", "gradient computation", "neural network training"],
    "attention mechanism": ["attention mechanism", "self-attention", "transformer attention"],
    "transformer": ["transformer", "attention mechanism", "sequence-to-sequence model"],
    "convolutional neural network": ["convolutional neural network", "CNN", "image feature learning"],
    "recurrent neural network": ["recurrent neural network", "RNN", "sequence modeling"],
    "generative adversarial network": ["generative adversarial network", "GAN", "generative model"],
    "autoencoder": ["autoencoder", "variational autoencoder", "representation learning"],
    "reinforcement learning": ["reinforcement learning", "reward optimization", "policy gradient"],
    "random forest": ["random forest", "ensemble learning", "decision tree ensemble"],
    "gradient boosting": ["gradient boosting", "ensemble learning", "boosted trees"],
    "support vector machine": ["support vector machine", "SVM", "kernel method"],
    "decision tree": ["decision tree", "tree-based model", "interpretable classification"],
    "naive bayes": ["naive bayes", "probabilistic classifier", "bayesian classification"],
    "k-nearest neighbors": ["k-nearest neighbors", "KNN", "instance-based learning"],
    "k-means clustering": ["k-means clustering", "centroid-based clustering", "unsupervised learning"],
    "DBSCAN clustering": ["DBSCAN", "density-based clustering", "spatial clustering"],
    "dimensionality reduction": ["dimensionality reduction", "PCA", "feature extraction"],
    "embedding": ["embedding", "vector representation", "distributed representation"],
    "word embedding": ["word embedding", "word2vec", "distributional semantics"],
    "sentence embedding": ["sentence embedding", "sentence representation", "text encoding"],
    # NLP
    "natural language processing": ["natural language processing", "NLP", "computational linguistics"],
    "topic modeling": ["topic modeling", "latent dirichlet allocation", "document clustering"],
    "large language model": ["large language model", "LLM", "language generation"],
    # Computer vision
    "computer vision": ["computer vision", "image analysis", "visual recognition"],
    "image processing": ["image processing", "digital image analysis", "visual computing"],
    # Algorithms
    "sorting algorithm": ["sorting algorithm", "comparison sort", "computational complexity"],
    "binary search": ["binary search", "search algorithm", "divide and conquer"],
    "dynamic programming": ["dynamic programming", "optimal substructure", "memoization"],
    "shortest path algorithm": ["shortest path", "graph algorithm", "Dijkstra"],
    "breadth-first search": ["breadth-first search", "BFS", "graph traversal"],
    "depth-first search": ["depth-first search", "DFS", "graph traversal"],
    "A* search": ["A* search", "heuristic search", "pathfinding algorithm"],
    "topological sort": ["topological sort", "directed acyclic graph", "dependency ordering"],
    "minimum spanning tree": ["minimum spanning tree", "MST", "graph algorithm"],
    # Data structures
    "binary tree": ["binary tree", "tree data structure", "balanced tree"],
    "hash table": ["hash table", "hash map", "associative array"],
    "linked list": ["linked list", "dynamic data structure", "sequential access"],
    "trie": ["trie", "prefix tree", "string data structure"],
    "priority queue": ["priority queue", "heap data structure", "scheduling algorithm"],
    "graph": ["graph data structure", "graph algorithm", "network analysis"],
    # Optimization
    "genetic algorithm": ["genetic algorithm", "evolutionary computation", "metaheuristic"],
    "simulated annealing": ["simulated annealing", "metaheuristic optimization", "stochastic optimization"],
    "particle swarm optimization": ["particle swarm optimization", "swarm intelligence", "metaheuristic"],
    "linear programming": ["linear programming", "mathematical optimization", "simplex method"],
    "hyperparameter optimization": ["hyperparameter optimization", "AutoML", "model selection"],
    # Statistics
    "bayesian inference": ["bayesian inference", "posterior estimation", "probabilistic modeling"],
    "Monte Carlo method": ["Monte Carlo", "stochastic simulation", "sampling method"],
    "Markov model": ["Markov model", "hidden Markov model", "stochastic process"],
    "hypothesis testing": ["hypothesis testing", "statistical significance", "p-value"],
    "statistical modeling": ["statistical modeling", "regression analysis", "inference"],
    # Security
    "encryption": ["encryption", "cryptographic algorithm", "data protection"],
    "hashing": ["hash function", "cryptographic hash", "message digest"],
    "authentication": ["authentication", "access control", "identity verification"],
    "cryptography": ["cryptography", "cipher", "encryption scheme"],
    # Distributed systems
    "distributed computing": ["distributed computing", "parallel processing", "distributed algorithm"],
    # Design patterns
    "singleton pattern": ["singleton pattern", "creational design pattern"],
    "factory pattern": ["factory pattern", "creational design pattern", "object creation"],
    "observer pattern": ["observer pattern", "event-driven architecture", "publish-subscribe"],
    "strategy pattern": ["strategy pattern", "behavioral design pattern"],
    "decorator pattern": ["decorator pattern", "structural design pattern"],
    # Misc
    "vector database": ["vector database", "similarity search", "approximate nearest neighbor"],
    "similarity search": ["similarity search", "nearest neighbor", "vector retrieval"],
    "regularization": ["regularization", "overfitting prevention", "model generalization"],
    "loss function": ["loss function", "objective function", "cost function"],
}

# Category weights for query generation
CATEGORY_WEIGHTS = {
    "algorithm": 1.0,
    "ml_technique": 0.95,
    "data_structure": 0.85,
    "technique": 0.7,
    "design_pattern": 0.6,
    "framework": 0.4,
}


def expand_concept(concept: str) -> List[str]:
    """
    Expand a concept into related academic search terms.

    Returns list of expanded terms, always including the original.
    """
    key = concept.lower().strip()
    if key in CONCEPT_EXPANSIONS:
        return CONCEPT_EXPANSIONS[key]
    return [concept]


def combine_concepts(concepts: List[str]) -> List[str]:
    """
    Combine multiple concepts into compound search queries.

    Generates meaningful pairwise combinations for related concepts.
    """
    if len(concepts) == 0:
        return []
    if len(concepts) == 1:
        return concepts

    combined = []
    # Generate pairwise combinations (limited to avoid explosion)
    for i in range(min(len(concepts), 5)):
        for j in range(i + 1, min(len(concepts), 5)):
            combined.append(f"{concepts[i]} {concepts[j]}")

    return combined


def rank_queries(
    queries: List[GeneratedQuery],
    limit: int = 20
) -> List[GeneratedQuery]:
    """
    Rank and deduplicate queries by confidence.

    Merges duplicate query texts, keeping the highest confidence.
    """
    # Deduplicate by query text, keeping highest confidence
    seen: Dict[str, GeneratedQuery] = {}
    for q in queries:
        key = q.query.lower().strip()
        if key not in seen or q.confidence > seen[key].confidence:
            seen[key] = q

    # Sort by confidence descending
    ranked = sorted(seen.values(), key=lambda q: q.confidence, reverse=True)

    return ranked[:limit]


class QueryGenerator:
    """
    Generates optimized academic search queries from code analysis concepts.
    """

    def from_concepts(
        self,
        concepts: List[Dict],
        min_confidence: float = 0.2,
        max_queries: int = 20
    ) -> List[GeneratedQuery]:
        """
        Generate queries from a list of concept dicts.

        Args:
            concepts: List of {name, category, confidence} dicts
            min_confidence: Minimum concept confidence to include
            max_queries: Maximum queries to return

        Returns:
            Ranked list of GeneratedQuery objects
        """
        if not concepts:
            return []

        all_queries = []

        for concept in concepts:
            name = concept.get("name", "")
            category = concept.get("category", "technique")
            confidence = concept.get("confidence", concept.get("max_confidence", 0.5))

            if confidence < min_confidence or not name:
                continue

            # Apply category weight
            cat_weight = CATEGORY_WEIGHTS.get(category, 0.5)
            adjusted_confidence = confidence * cat_weight

            # Strategy 1: Direct query
            all_queries.append(GeneratedQuery(
                query=name,
                strategy=QueryStrategy.DIRECT,
                source_concepts=[name],
                confidence=adjusted_confidence,
            ))

            # Strategy 2: Concept expansion (for higher confidence concepts)
            if confidence >= 0.5:
                expanded = expand_concept(name)
                for term in expanded:
                    if term.lower() != name.lower():
                        all_queries.append(GeneratedQuery(
                            query=term,
                            strategy=QueryStrategy.CONCEPT_EXPANSION,
                            source_concepts=[name],
                            confidence=adjusted_confidence * 0.85,
                        ))

        # Strategy 3: Compound queries from high-confidence concepts
        high_conf = [
            c["name"] for c in concepts
            if c.get("confidence", c.get("max_confidence", 0)) >= 0.7
        ]
        if len(high_conf) >= 2:
            compounds = combine_concepts(high_conf)
            for compound in compounds:
                all_queries.append(GeneratedQuery(
                    query=compound,
                    strategy=QueryStrategy.COMPOUND,
                    source_concepts=compound.split(" ", 1),
                    confidence=0.7,
                ))

        return rank_queries(all_queries, limit=max_queries)

    def from_analysis(
        self,
        analysis: Dict,
        max_queries: int = 20,
        min_confidence: float = 0.2
    ) -> List[GeneratedQuery]:
        """
        Generate queries from a full analysis result (from concept_extractor aggregate).

        Args:
            analysis: Dict with 'concepts' and optionally 'search_queries'
            max_queries: Maximum queries to return
            min_confidence: Minimum confidence threshold

        Returns:
            Ranked list of GeneratedQuery objects
        """
        concepts = analysis.get("concepts", [])
        return self.from_concepts(
            concepts,
            min_confidence=min_confidence,
            max_queries=max_queries,
        )
