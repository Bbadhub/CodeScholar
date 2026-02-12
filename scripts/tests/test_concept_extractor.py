"""
Test suite for concept_extractor.py
TDD approach for codebase analysis
"""

import pytest
from pathlib import Path
import sys
import tempfile
import os

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from analyzers.concept_extractor import (
    analyze_python_file,
    analyze_file,
    analyze_directory,
    analyze_with_regex,
    detect_language,
    aggregate_concepts,
    ExtractedConcept,
    AnalysisResult,
    PythonASTAnalyzer
)


class TestLanguageDetection:
    """Test file language detection"""

    def test_detect_python(self):
        assert detect_language("test.py") == "python"

    def test_detect_javascript(self):
        assert detect_language("test.js") == "javascript"

    def test_detect_typescript(self):
        assert detect_language("test.ts") == "typescript"

    def test_detect_tsx(self):
        assert detect_language("component.tsx") == "typescript"

    def test_detect_unknown(self):
        assert detect_language("test.txt") is None

    def test_detect_no_extension(self):
        assert detect_language("Makefile") is None


class TestPythonASTAnalysis:
    """Test Python AST-based concept extraction"""

    def test_extract_sklearn_import(self, tmp_path):
        """Test detecting scikit-learn imports"""
        code = """
import sklearn
from sklearn.ensemble import RandomForestClassifier
"""
        f = tmp_path / "ml_code.py"
        f.write_text(code)

        result = analyze_python_file(str(f))

        assert result.language == "python"
        assert any(c.name == "machine learning" for c in result.concepts)
        assert any(c.name == "random forest" for c in result.concepts)

    def test_extract_torch_import(self, tmp_path):
        """Test detecting PyTorch imports"""
        code = """
import torch
import torch.nn as nn
"""
        f = tmp_path / "deep_learning.py"
        f.write_text(code)

        result = analyze_python_file(str(f))

        assert any(c.name == "deep learning" for c in result.concepts)
        assert any(c.name == "neural network" for c in result.concepts)

    def test_extract_transformers_import(self, tmp_path):
        """Test detecting Hugging Face transformers"""
        code = """
from transformers import AutoTokenizer, AutoModel
"""
        f = tmp_path / "nlp.py"
        f.write_text(code)

        result = analyze_python_file(str(f))

        assert any(c.name == "transformer" for c in result.concepts)
        assert any(c.name == "attention mechanism" for c in result.concepts)

    def test_extract_function_names(self, tmp_path):
        """Test extracting concept from function names"""
        code = """
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
    return -1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    return quick_sort([x for x in arr[1:] if x < pivot]) + [pivot] + quick_sort([x for x in arr[1:] if x >= pivot])
"""
        f = tmp_path / "algorithms.py"
        f.write_text(code)

        result = analyze_python_file(str(f))

        assert any(c.name == "binary search" for c in result.concepts)
        assert any(c.name == "sorting algorithm" for c in result.concepts)
        assert "binary_search" in result.functions
        assert "quick_sort" in result.functions

    def test_extract_class_names(self, tmp_path):
        """Test extracting concepts from class names"""
        code = """
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class GeneticAlgorithm:
    def __init__(self, population_size):
        self.population_size = population_size
"""
        f = tmp_path / "structures.py"
        f.write_text(code)

        result = analyze_python_file(str(f))

        assert any(c.name == "binary tree" for c in result.concepts)
        assert any(c.name == "genetic algorithm" for c in result.concepts)
        assert "BinaryTree" in result.classes
        assert "GeneticAlgorithm" in result.classes

    def test_extract_multiple_imports(self, tmp_path):
        """Test multiple imports in one file"""
        code = """
import numpy as np
from scipy.optimize import minimize
from sklearn.cluster import KMeans
import networkx as nx
"""
        f = tmp_path / "multi.py"
        f.write_text(code)

        result = analyze_python_file(str(f))

        concept_names = [c.name for c in result.concepts]
        assert "numerical computing" in concept_names
        assert "optimization" in concept_names
        assert "clustering" in concept_names
        assert "graph algorithm" in concept_names

    def test_handles_syntax_error(self, tmp_path):
        """Test graceful handling of syntax errors"""
        code = "def broken(:\n    pass"
        f = tmp_path / "broken.py"
        f.write_text(code)

        result = analyze_python_file(str(f))

        # Should not crash - falls back to regex
        assert result is not None
        assert result.language == "python"

    def test_handles_missing_file(self):
        """Test handling of missing files"""
        result = analyze_python_file("/nonexistent/file.py")
        assert result is not None
        assert len(result.concepts) == 0

    def test_confidence_scores(self, tmp_path):
        """Test that confidence scores are reasonable"""
        code = """
from transformers import AutoModel  # High confidence
import numpy  # Lower confidence
"""
        f = tmp_path / "confidence.py"
        f.write_text(code)

        result = analyze_python_file(str(f))

        transformer_concept = next((c for c in result.concepts if c.name == "transformer"), None)
        numpy_concept = next((c for c in result.concepts if c.name == "numerical computing"), None)

        assert transformer_concept is not None
        assert numpy_concept is not None
        assert transformer_concept.confidence > numpy_concept.confidence

    def test_async_function_detection(self, tmp_path):
        """Test async function name analysis"""
        code = """
async def gradient_descent(params, learning_rate):
    pass
"""
        f = tmp_path / "async_ml.py"
        f.write_text(code)

        result = analyze_python_file(str(f))

        assert "gradient_descent" in result.functions
        assert any(c.name == "gradient descent" for c in result.concepts)


class TestRegexAnalysis:
    """Test regex-based analysis for JS/TS files"""

    def test_javascript_imports(self, tmp_path):
        """Test detecting JS imports"""
        code = """
import { NeuralNetwork } from './network';
const tf = require('tensorflow');

function binarySearch(arr, target) {
    let left = 0, right = arr.length - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) return mid;
    }
    return -1;
}
"""
        f = tmp_path / "algorithms.js"
        f.write_text(code)

        result = analyze_file(str(f))

        assert result is not None
        assert result.language == "javascript"
        assert any(c.name == "binary search" for c in result.concepts)

    def test_typescript_class(self, tmp_path):
        """Test detecting TS class patterns"""
        code = """
class ObserverPattern {
    private observers: Array<Observer> = [];

    subscribe(observer: Observer): void {
        this.observers.push(observer);
    }
}

class KMeansCluster {
    centroids: number[][];
}
"""
        f = tmp_path / "patterns.ts"
        f.write_text(code)

        result = analyze_file(str(f))

        assert result is not None
        assert any(c.name == "observer pattern" for c in result.concepts)
        assert any(c.name == "k-means clustering" for c in result.concepts)


class TestDirectoryAnalysis:
    """Test analyzing entire directories"""

    def test_analyze_directory(self, tmp_path):
        """Test analyzing a directory of files"""
        # Create test files
        (tmp_path / "ml.py").write_text("from sklearn.svm import SVC\n")
        (tmp_path / "algo.py").write_text("def binary_search(arr, t): pass\n")
        (tmp_path / "readme.txt").write_text("Not code")

        results = analyze_directory(str(tmp_path))

        assert len(results) >= 1  # At least one file with concepts
        all_concepts = [c.name for r in results for c in r.concepts]
        assert "support vector machine" in all_concepts

    def test_excludes_node_modules(self, tmp_path):
        """Test that node_modules is excluded"""
        nm = tmp_path / "node_modules" / "pkg"
        nm.mkdir(parents=True)
        (nm / "index.js").write_text("class NeuralNetwork {}")
        (tmp_path / "app.py").write_text("import sklearn\n")

        results = analyze_directory(str(tmp_path))

        # Should only find the app.py results, not node_modules
        files_analyzed = [Path(r.file_path) for r in results]
        assert not any("node_modules" in p.relative_to(tmp_path).parts for p in files_analyzed)

    def test_empty_directory(self, tmp_path):
        """Test analyzing empty directory"""
        results = analyze_directory(str(tmp_path))
        assert results == []


class TestAggregation:
    """Test concept aggregation across files"""

    def test_aggregate_concepts(self):
        """Test aggregating concepts from multiple results"""
        results = [
            AnalysisResult(
                file_path="a.py",
                language="python",
                concepts=[
                    ExtractedConcept("neural network", "algorithm", 0.9, "a.py", evidence="import torch.nn"),
                    ExtractedConcept("deep learning", "ml_technique", 0.9, "a.py", evidence="import torch")
                ]
            ),
            AnalysisResult(
                file_path="b.py",
                language="python",
                concepts=[
                    ExtractedConcept("neural network", "algorithm", 0.8, "b.py", evidence="class NeuralNetwork"),
                    ExtractedConcept("gradient descent", "algorithm", 0.8, "b.py", evidence="def gradient_descent")
                ]
            )
        ]

        aggregated = aggregate_concepts(results)

        assert aggregated["total_concepts"] == 3  # neural network, deep learning, gradient descent
        assert aggregated["total_files_analyzed"] == 2

        # Neural network should have count 2
        nn = next(c for c in aggregated["concepts"] if c["name"] == "neural network")
        assert nn["count"] == 2
        assert nn["max_confidence"] == 0.9
        assert len(nn["files"]) == 2

    def test_aggregate_generates_queries(self):
        """Test that aggregation generates search queries"""
        results = [
            AnalysisResult(
                file_path="test.py",
                language="python",
                concepts=[
                    ExtractedConcept("transformer", "algorithm", 0.95, "test.py"),
                    ExtractedConcept("attention mechanism", "algorithm", 0.9, "test.py"),
                ]
            )
        ]

        aggregated = aggregate_concepts(results)

        assert "search_queries" in aggregated
        assert len(aggregated["search_queries"]) > 0
        assert "transformer" in aggregated["search_queries"]

    def test_aggregate_categories(self):
        """Test category counting in aggregation"""
        results = [
            AnalysisResult(
                file_path="test.py",
                language="python",
                concepts=[
                    ExtractedConcept("binary tree", "data_structure", 0.9, "test.py"),
                    ExtractedConcept("hash table", "data_structure", 0.9, "test.py"),
                    ExtractedConcept("gradient descent", "algorithm", 0.8, "test.py"),
                ]
            )
        ]

        aggregated = aggregate_concepts(results)

        assert aggregated["categories"]["data_structure"] == 2
        assert aggregated["categories"]["algorithm"] == 1


class TestSearchQueryGeneration:
    """Test search query generation from analysis results"""

    def test_generate_queries_from_result(self, tmp_path):
        """Test generating search queries from analysis"""
        code = """
from transformers import AutoModel
import torch.nn as nn
from sklearn.cluster import KMeans
"""
        f = tmp_path / "ml_pipeline.py"
        f.write_text(code)

        result = analyze_python_file(str(f))
        queries = result.generate_search_queries()

        assert len(queries) > 0
        assert len(queries) <= 10  # Max 10 queries

    def test_queries_deduplication(self):
        """Test that search queries are deduplicated"""
        result = AnalysisResult(
            file_path="test.py",
            language="python",
            concepts=[
                ExtractedConcept("neural network", "algorithm", 0.9, "test.py"),
                ExtractedConcept("neural network", "algorithm", 0.8, "test.py"),
            ]
        )

        queries = result.generate_search_queries()

        assert queries.count("neural network") == 1

    def test_queries_sorted_by_confidence(self):
        """Test that queries are sorted by confidence"""
        result = AnalysisResult(
            file_path="test.py",
            language="python",
            concepts=[
                ExtractedConcept("numerical computing", "technique", 0.5, "test.py"),
                ExtractedConcept("transformer", "algorithm", 0.95, "test.py"),
                ExtractedConcept("deep learning", "ml_technique", 0.9, "test.py"),
            ]
        )

        queries = result.generate_search_queries()

        assert queries[0] == "transformer"  # Highest confidence first
