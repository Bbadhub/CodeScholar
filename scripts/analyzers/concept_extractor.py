"""
CodeScholar Concept Extractor
Analyzes source code to extract algorithms, techniques, and research concepts.

Supported languages: Python (AST), JavaScript/TypeScript (regex)
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Set, Optional
from dataclasses import dataclass, field


@dataclass
class ExtractedConcept:
    """A concept extracted from code"""
    name: str
    category: str  # algorithm, data_structure, ml_technique, design_pattern, etc.
    confidence: float  # 0.0 to 1.0
    source_file: str
    source_line: Optional[int] = None
    evidence: str = ""  # The code/import that triggered detection


@dataclass
class AnalysisResult:
    """Result of analyzing a file or directory"""
    file_path: str
    language: str
    concepts: List[ExtractedConcept] = field(default_factory=list)
    imports: List[str] = field(default_factory=list)
    functions: List[str] = field(default_factory=list)
    classes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "file_path": self.file_path,
            "language": self.language,
            "concepts": [
                {
                    "name": c.name,
                    "category": c.category,
                    "confidence": c.confidence,
                    "source_line": c.source_line,
                    "evidence": c.evidence
                }
                for c in self.concepts
            ],
            "imports": self.imports,
            "functions": self.functions,
            "classes": self.classes,
            "search_queries": self.generate_search_queries()
        }

    def generate_search_queries(self) -> List[str]:
        """Generate paper search queries from extracted concepts"""
        queries = []
        seen = set()

        for concept in sorted(self.concepts, key=lambda c: c.confidence, reverse=True):
            query = concept.name.lower()
            if query not in seen:
                queries.append(query)
                seen.add(query)

        return queries[:10]  # Top 10 most relevant queries


# Import-to-concept mappings
PYTHON_IMPORT_CONCEPTS = {
    # ML/AI frameworks
    "sklearn": [("machine learning", "ml_technique", 0.9)],
    "sklearn.ensemble": [("random forest", "algorithm", 0.9), ("gradient boosting", "algorithm", 0.8)],
    "sklearn.svm": [("support vector machine", "algorithm", 0.9)],
    "sklearn.cluster": [("clustering", "algorithm", 0.9)],
    "sklearn.neural_network": [("neural network", "algorithm", 0.9)],
    "sklearn.decomposition": [("dimensionality reduction", "algorithm", 0.8), ("PCA", "algorithm", 0.9)],
    "sklearn.tree": [("decision tree", "algorithm", 0.9)],
    "sklearn.linear_model": [("linear regression", "algorithm", 0.8)],
    "sklearn.naive_bayes": [("naive bayes", "algorithm", 0.9)],
    "sklearn.neighbors": [("k-nearest neighbors", "algorithm", 0.9)],
    "torch": [("deep learning", "ml_technique", 0.9), ("PyTorch", "framework", 0.9)],
    "torch.nn": [("neural network", "algorithm", 0.9)],
    "torch.optim": [("optimization", "ml_technique", 0.8)],
    "tensorflow": [("deep learning", "ml_technique", 0.9), ("TensorFlow", "framework", 0.9)],
    "keras": [("deep learning", "ml_technique", 0.8)],
    "transformers": [("transformer", "algorithm", 0.95), ("attention mechanism", "algorithm", 0.9)],
    "xgboost": [("gradient boosting", "algorithm", 0.95)],
    "lightgbm": [("gradient boosting", "algorithm", 0.9)],
    "catboost": [("gradient boosting", "algorithm", 0.9)],
    # NLP
    "nltk": [("natural language processing", "ml_technique", 0.9)],
    "spacy": [("natural language processing", "ml_technique", 0.9)],
    "gensim": [("word embedding", "algorithm", 0.9), ("topic modeling", "algorithm", 0.8)],
    "sentence_transformers": [("sentence embedding", "algorithm", 0.9)],
    # Computer vision
    "cv2": [("computer vision", "ml_technique", 0.9)],
    "PIL": [("image processing", "ml_technique", 0.7)],
    "torchvision": [("computer vision", "ml_technique", 0.9)],
    # Data science
    "numpy": [("numerical computing", "technique", 0.5)],
    "pandas": [("data analysis", "technique", 0.5)],
    "scipy": [("scientific computing", "technique", 0.6)],
    "scipy.optimize": [("optimization", "algorithm", 0.8)],
    "scipy.signal": [("signal processing", "algorithm", 0.8)],
    "scipy.stats": [("statistical analysis", "technique", 0.7)],
    "statsmodels": [("statistical modeling", "technique", 0.8)],
    # Graphs
    "networkx": [("graph algorithm", "algorithm", 0.8), ("network analysis", "technique", 0.8)],
    "igraph": [("graph algorithm", "algorithm", 0.8)],
    # Reinforcement learning
    "gym": [("reinforcement learning", "ml_technique", 0.9)],
    "stable_baselines3": [("reinforcement learning", "ml_technique", 0.95)],
    # Optimization
    "optuna": [("hyperparameter optimization", "technique", 0.9)],
    "deap": [("genetic algorithm", "algorithm", 0.9), ("evolutionary computation", "technique", 0.9)],
    "pyswarms": [("particle swarm optimization", "algorithm", 0.95)],
    # Bayesian
    "pymc": [("bayesian inference", "technique", 0.9)],
    "pyro": [("probabilistic programming", "technique", 0.9)],
    # Cryptography
    "cryptography": [("cryptography", "technique", 0.8)],
    "hashlib": [("hashing", "algorithm", 0.6)],
    # Distributed systems
    "celery": [("distributed computing", "technique", 0.7)],
    "dask": [("distributed computing", "technique", 0.8)],
    "ray": [("distributed computing", "technique", 0.8)],
    # Web scraping / data collection
    "scrapy": [("web scraping", "technique", 0.6)],
    "beautifulsoup4": [("web scraping", "technique", 0.5)],
    # Embeddings / vector databases
    "qdrant_client": [("vector database", "technique", 0.8), ("similarity search", "algorithm", 0.8)],
    "chromadb": [("vector database", "technique", 0.8)],
    "pinecone": [("vector database", "technique", 0.8)],
    "openai": [("large language model", "ml_technique", 0.7)],
    "anthropic": [("large language model", "ml_technique", 0.7)],
}

# Function/class name patterns that indicate concepts
CODE_PATTERNS = [
    # Sorting algorithms
    (r"(?:quick|merge|heap|bubble|insertion|selection|radix|bucket)_?sort", "sorting algorithm", "algorithm", 0.9),
    (r"binary[_\s]?[Ss]earch|bisect", "binary search", "algorithm", 0.9),
    # Data structures
    (r"(?:linked_?list|LinkedList)", "linked list", "data_structure", 0.9),
    (r"(?:binary_?tree|BinaryTree|BST|RedBlack|AVL)", "binary tree", "data_structure", 0.9),
    (r"(?:hash_?map|HashMap|hash_?table|HashTable)", "hash table", "data_structure", 0.9),
    (r"(?:priority_?queue|PriorityQueue|heap|MinHeap|MaxHeap)", "priority queue", "data_structure", 0.9),
    (r"(?:trie|Trie|prefix_?tree)", "trie", "data_structure", 0.9),
    (r"(?:graph|Graph|adjacency)", "graph", "data_structure", 0.7),
    (r"(?:stack|Stack|LIFO)", "stack", "data_structure", 0.6),
    (r"(?:queue|Queue|FIFO|deque)", "queue", "data_structure", 0.6),
    # Graph algorithms
    (r"(?:dijkstra|bellman.ford|floyd.warshall)", "shortest path algorithm", "algorithm", 0.95),
    (r"(?:breadth.first|BFS|bfs)", "breadth-first search", "algorithm", 0.9),
    (r"(?:depth.first|DFS|dfs)", "depth-first search", "algorithm", 0.9),
    (r"(?:kruskal|prim).*(?:spanning|mst)", "minimum spanning tree", "algorithm", 0.9),
    (r"(?:topological.sort|topological_sort)", "topological sort", "algorithm", 0.9),
    (r"(?:a_star|astar|A\*)", "A* search", "algorithm", 0.9),
    # Dynamic programming
    (r"(?:dynamic_?prog|dp_|memoiz|memo_)", "dynamic programming", "algorithm", 0.85),
    (r"(?:knapsack|Knapsack)", "knapsack problem", "algorithm", 0.9),
    (r"(?:lcs|longest_common)", "longest common subsequence", "algorithm", 0.9),
    # ML techniques
    (r"(?:gradient_?descent|SGD|Adam|learning_rate)", "gradient descent", "algorithm", 0.8),
    (r"(?:backprop|backward|autograd)", "backpropagation", "algorithm", 0.8),
    (r"(?:attention|self_attention|multi_head)", "attention mechanism", "algorithm", 0.9),
    (r"(?:conv2d|Conv2d|convolution|CNN)", "convolutional neural network", "algorithm", 0.9),
    (r"(?:LSTM|lstm|GRU|gru|recurrent)", "recurrent neural network", "algorithm", 0.9),
    (r"(?:GAN|gan|generator.*discriminator|adversarial)", "generative adversarial network", "algorithm", 0.9),
    (r"(?:autoencoder|VAE|variational)", "autoencoder", "algorithm", 0.9),
    (r"(?:dropout|batch_?norm|layer_?norm)", "regularization", "technique", 0.7),
    (r"(?:cross_entropy|mse_loss|loss_function)", "loss function", "technique", 0.7),
    (r"(?:embedding|Embedding|word2vec|Word2Vec)", "embedding", "technique", 0.8),
    (r"(?:k_means|kmeans|KMeans)", "k-means clustering", "algorithm", 0.9),
    (r"(?:dbscan|DBSCAN)", "DBSCAN clustering", "algorithm", 0.9),
    # Optimization
    (r"(?:simulated_?annealing|SimulatedAnnealing)", "simulated annealing", "algorithm", 0.95),
    (r"(?:genetic_?algorithm|GeneticAlgorithm|crossover.*mutation)", "genetic algorithm", "algorithm", 0.9),
    (r"(?:particle_?swarm|PSO)", "particle swarm optimization", "algorithm", 0.95),
    (r"(?:ant_?colony|ACO)", "ant colony optimization", "algorithm", 0.95),
    (r"(?:linear_?program|LP|simplex)", "linear programming", "algorithm", 0.8),
    # Statistics
    (r"(?:bayesian|bayes|posterior|prior|likelihood)", "bayesian inference", "technique", 0.8),
    (r"(?:monte_?carlo|MonteCarlo|MCMC)", "Monte Carlo method", "algorithm", 0.9),
    (r"(?:markov|Markov|HMM|hidden_markov)", "Markov model", "algorithm", 0.9),
    (r"(?:hypothesis_test|t_test|chi_square|p_value)", "hypothesis testing", "technique", 0.8),
    # Security
    (r"(?:encrypt|decrypt|cipher|AES|RSA)", "encryption", "technique", 0.8),
    (r"(?:hash|SHA|MD5|bcrypt|pbkdf)", "hashing", "technique", 0.7),
    (r"(?:jwt|JWT|token|OAuth|oauth)", "authentication", "technique", 0.6),
    # Design patterns
    (r"(?:singleton|Singleton)", "singleton pattern", "design_pattern", 0.8),
    (r"(?:factory|Factory|AbstractFactory)", "factory pattern", "design_pattern", 0.8),
    (r"(?:observer|Observer|EventEmitter|pubsub)", "observer pattern", "design_pattern", 0.8),
    (r"(?:strategy|Strategy).*(?:pattern|Pattern)", "strategy pattern", "design_pattern", 0.8),
    (r"(?:decorator|Decorator).*(?:pattern|wrap)", "decorator pattern", "design_pattern", 0.7),
]


class PythonASTAnalyzer(ast.NodeVisitor):
    """Analyze Python files using AST parsing"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.imports: List[str] = []
        self.functions: List[str] = []
        self.classes: List[str] = []
        self.concepts: List[ExtractedConcept] = []

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append(alias.name)
            self._check_import_concepts(alias.name, node.lineno)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module:
            self.imports.append(node.module)
            self._check_import_concepts(node.module, node.lineno)
            for alias in node.names:
                full_import = f"{node.module}.{alias.name}"
                self._check_import_concepts(full_import, node.lineno)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.functions.append(node.name)
        self._check_name_patterns(node.name, node.lineno)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.functions.append(node.name)
        self._check_name_patterns(node.name, node.lineno)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.classes.append(node.name)
        self._check_name_patterns(node.name, node.lineno)

        # Check base classes
        for base in node.bases:
            if isinstance(base, ast.Name):
                self._check_name_patterns(base.id, node.lineno)
            elif isinstance(base, ast.Attribute):
                self._check_name_patterns(base.attr, node.lineno)

        self.generic_visit(node)

    def _check_import_concepts(self, import_name: str, line: int):
        """Check if import maps to known concepts"""
        # Check exact match first, then prefix matches
        for key, concepts in PYTHON_IMPORT_CONCEPTS.items():
            if import_name == key or import_name.startswith(key + "."):
                for name, category, confidence in concepts:
                    self.concepts.append(ExtractedConcept(
                        name=name,
                        category=category,
                        confidence=confidence,
                        source_file=self.file_path,
                        source_line=line,
                        evidence=f"import {import_name}"
                    ))

    def _check_name_patterns(self, name: str, line: int):
        """Check function/class names against known patterns"""
        for pattern, concept_name, category, confidence in CODE_PATTERNS:
            if re.search(pattern, name, re.IGNORECASE):
                self.concepts.append(ExtractedConcept(
                    name=concept_name,
                    category=category,
                    confidence=confidence,
                    source_file=self.file_path,
                    source_line=line,
                    evidence=f"name: {name}"
                ))


def analyze_python_file(file_path: str) -> AnalysisResult:
    """Analyze a Python file using AST"""
    result = AnalysisResult(file_path=file_path, language="python")

    try:
        source = Path(file_path).read_text(encoding='utf-8')
    except (FileNotFoundError, UnicodeDecodeError) as e:
        return result

    try:
        tree = ast.parse(source)
        analyzer = PythonASTAnalyzer(file_path)
        analyzer.visit(tree)

        result.imports = analyzer.imports
        result.functions = analyzer.functions
        result.classes = analyzer.classes
        result.concepts = analyzer.concepts
    except SyntaxError:
        # Fall back to regex-based analysis
        result = analyze_with_regex(file_path, source, "python")

    # Also scan full source text for patterns in comments/strings
    _scan_source_text(source, file_path, result)

    return result


def analyze_with_regex(file_path: str, source: str, language: str) -> AnalysisResult:
    """Regex-based analysis for any language"""
    result = AnalysisResult(file_path=file_path, language=language)

    # Extract imports
    if language in ("javascript", "typescript"):
        for match in re.finditer(r"(?:import|require)\s*\(?['\"]([^'\"]+)['\"]", source):
            result.imports.append(match.group(1))
    elif language == "python":
        for match in re.finditer(r"(?:import|from)\s+([\w.]+)", source):
            result.imports.append(match.group(1))

    # Extract function names
    if language in ("javascript", "typescript"):
        for match in re.finditer(r"(?:function|const|let|var)\s+(\w+)\s*(?:=\s*(?:async\s+)?(?:\([^)]*\)|[\w]+)\s*=>|\()", source):
            result.functions.append(match.group(1))
    elif language == "python":
        for match in re.finditer(r"def\s+(\w+)\s*\(", source):
            result.functions.append(match.group(1))

    # Extract class names
    for match in re.finditer(r"class\s+(\w+)", source):
        result.classes.append(match.group(1))

    # Check patterns against all names
    all_names = result.imports + result.functions + result.classes
    for name in all_names:
        for pattern, concept_name, category, confidence in CODE_PATTERNS:
            if re.search(pattern, name, re.IGNORECASE):
                result.concepts.append(ExtractedConcept(
                    name=concept_name,
                    category=category,
                    confidence=confidence,
                    source_file=file_path,
                    evidence=f"name: {name}"
                ))

    # Scan source text
    _scan_source_text(source, file_path, result)

    return result


def _scan_source_text(source: str, file_path: str, result: AnalysisResult):
    """Scan source text for concept patterns in comments and strings"""
    for pattern, concept_name, category, confidence in CODE_PATTERNS:
        for match in re.finditer(pattern, source, re.IGNORECASE):
            # Check if this concept is already found
            if not any(c.name == concept_name for c in result.concepts):
                # Lower confidence for text matches vs AST matches
                result.concepts.append(ExtractedConcept(
                    name=concept_name,
                    category=category,
                    confidence=confidence * 0.7,  # Lower confidence for text matches
                    source_file=file_path,
                    evidence=f"text match: {match.group(0)}"
                ))


def detect_language(file_path: str) -> Optional[str]:
    """Detect programming language from file extension"""
    ext_map = {
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".jsx": "javascript",
        ".tsx": "typescript",
        ".java": "java",
        ".go": "go",
        ".rs": "rust",
        ".cpp": "cpp",
        ".c": "c",
        ".rb": "ruby",
        ".php": "php",
    }
    ext = Path(file_path).suffix.lower()
    return ext_map.get(ext)


def analyze_file(file_path: str) -> Optional[AnalysisResult]:
    """Analyze a single file"""
    language = detect_language(file_path)
    if not language:
        return None

    if language == "python":
        return analyze_python_file(file_path)
    else:
        try:
            source = Path(file_path).read_text(encoding='utf-8')
        except (FileNotFoundError, UnicodeDecodeError):
            return None
        return analyze_with_regex(file_path, source, language)


def analyze_directory(
    directory: str,
    extensions: Optional[List[str]] = None,
    exclude_dirs: Optional[List[str]] = None
) -> List[AnalysisResult]:
    """
    Analyze all code files in a directory

    Args:
        directory: Path to directory
        extensions: File extensions to include (default: all supported)
        exclude_dirs: Directories to exclude (default: common non-code dirs)

    Returns:
        List of analysis results
    """
    if extensions is None:
        extensions = [".py", ".js", ".ts", ".jsx", ".tsx"]

    if exclude_dirs is None:
        exclude_dirs = [
            "node_modules", ".git", "__pycache__", ".venv", "venv",
            "dist", "build", ".tox", ".pytest_cache", ".mypy_cache",
            "env", ".env", "site-packages"
        ]

    results = []
    dir_path = Path(directory)

    for file_path in dir_path.rglob("*"):
        # Skip excluded directories (use relative path for reliable matching)
        try:
            rel_parts = file_path.relative_to(dir_path).parts
        except ValueError:
            continue
        if any(excl in rel_parts for excl in exclude_dirs):
            continue

        # Only process matching extensions
        if file_path.suffix.lower() not in extensions:
            continue

        if file_path.is_file():
            result = analyze_file(str(file_path))
            if result and result.concepts:
                results.append(result)

    return results


def aggregate_concepts(results: List[AnalysisResult]) -> Dict:
    """
    Aggregate concepts across multiple files

    Returns:
        Dict with aggregated concepts, queries, and file mappings
    """
    concept_counts: Dict[str, Dict] = {}

    for result in results:
        for concept in result.concepts:
            key = concept.name.lower()
            if key not in concept_counts:
                concept_counts[key] = {
                    "name": concept.name,
                    "category": concept.category,
                    "count": 0,
                    "max_confidence": 0,
                    "files": set(),
                    "evidence": []
                }

            concept_counts[key]["count"] += 1
            concept_counts[key]["max_confidence"] = max(
                concept_counts[key]["max_confidence"],
                concept.confidence
            )
            concept_counts[key]["files"].add(concept.source_file)
            if len(concept_counts[key]["evidence"]) < 3:
                concept_counts[key]["evidence"].append(concept.evidence)

    # Sort by combined score (count * confidence)
    sorted_concepts = sorted(
        concept_counts.values(),
        key=lambda c: c["count"] * c["max_confidence"],
        reverse=True
    )

    # Convert sets to lists for JSON serialization
    for concept in sorted_concepts:
        concept["files"] = list(concept["files"])

    # Generate search queries
    queries = [c["name"] for c in sorted_concepts[:15]]

    return {
        "total_concepts": len(sorted_concepts),
        "total_files_analyzed": len(results),
        "concepts": sorted_concepts,
        "search_queries": queries,
        "categories": _count_categories(sorted_concepts)
    }


def _count_categories(concepts: List[Dict]) -> Dict[str, int]:
    """Count concepts by category"""
    categories = {}
    for concept in concepts:
        cat = concept["category"]
        categories[cat] = categories.get(cat, 0) + 1
    return categories
