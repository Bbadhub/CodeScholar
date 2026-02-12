"""
Test suite for import_existing_papers.py
Following TDD approach - write tests FIRST
"""

import json
import pytest
from pathlib import Path
import sys
import uuid

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from import_existing_papers import (
    load_metadata,
    convert_to_unified_format,
    find_pdf_path,
    generate_uuid,
    save_unified_library
)


class TestImportPapers:
    """Test suite for paper import functionality"""

    @pytest.fixture
    def sample_journal_club_paper(self):
        """Sample Journal Club paper structure"""
        return {
            "url": "https://journalclub.io/episodes/test-paper",
            "title": "Test Paper on Optimization Algorithms",
            "doi": "10.1234/test.5678",
            "doi_url": "https://doi.org/10.1234/test.5678",
            "description": "This is a test paper about optimization.",
            "slug": "test-paper-optimization",
            "scraped_at": "2026-01-20T01:53:38.627890"
        }

    @pytest.fixture
    def sample_metadata_list(self, sample_journal_club_paper):
        """Sample metadata.json structure"""
        return [sample_journal_club_paper]

    def test_load_metadata_success(self, tmp_path):
        """Test loading metadata.json successfully"""
        # Arrange
        metadata_file = tmp_path / "metadata.json"
        test_data = [{"title": "Test"}]
        metadata_file.write_text(json.dumps(test_data))

        # Act
        result = load_metadata(str(metadata_file))

        # Assert
        assert result == test_data
        assert len(result) == 1

    def test_load_metadata_file_not_found(self):
        """Test handling missing metadata.json"""
        with pytest.raises(FileNotFoundError):
            load_metadata("nonexistent.json")

    def test_convert_to_unified_format(self, sample_journal_club_paper):
        """Test conversion to unified format"""
        # Act
        result = convert_to_unified_format(sample_journal_club_paper)

        # Assert - Check required fields
        assert "id" in result
        assert result["title"] == "Test Paper on Optimization Algorithms"
        assert result["abstract"] == "This is a test paper about optimization."

        # Check identifiers
        assert result["identifiers"]["doi"] == "10.1234/test.5678"
        assert result["identifiers"]["journalclub_slug"] == "test-paper-optimization"

        # Check sources array
        assert len(result["sources"]) == 1
        assert result["sources"][0]["source"] == "journalclub"
        assert result["sources"][0]["url"] == "https://journalclub.io/episodes/test-paper"

        # Check metadata
        assert "year" in result["metadata"]
        assert result["metadata"]["year"] == 2026

        # Check files (metadata-only architecture)
        assert "pdf_url" in result["files"]
        assert result["files"]["pdf_url"] == "https://doi.org/10.1234/test.5678"
        assert "downloaded" in result["files"]
        assert result["files"]["downloaded"] is False
        assert result["files"]["local_path"] is None

        # Check analysis structure
        assert result["analysis"]["theories"] == []
        assert result["analysis"]["embedding"] is None
        assert result["analysis"]["relevant_to"] == []

    def test_convert_handles_missing_doi(self):
        """Test conversion handles papers without DOI"""
        # Arrange
        paper_no_doi = {
            "url": "https://journalclub.io/episodes/no-doi",
            "title": "Paper Without DOI",
            "doi": None,
            "doi_url": None,
            "description": "Test paper without DOI",
            "slug": "paper-no-doi",
            "scraped_at": "2026-01-20T01:53:38.627890"
        }

        # Act
        result = convert_to_unified_format(paper_no_doi)

        # Assert
        assert result["identifiers"]["doi"] is None
        assert "id" in result  # Should still have UUID

    def test_generate_uuid_is_unique(self):
        """Test UUID generation is unique"""
        # Act
        uuid1 = generate_uuid()
        uuid2 = generate_uuid()

        # Assert
        assert uuid1 != uuid2
        assert len(uuid1) == 36  # Standard UUID format

    def test_find_pdf_path_exists(self, tmp_path):
        """Test finding PDF when it exists"""
        # Arrange
        pdf_dir = tmp_path / "pdfs"
        pdf_dir.mkdir()
        test_pdf = pdf_dir / "test-slug.pdf"
        test_pdf.write_text("fake pdf content")

        # Act
        result = find_pdf_path("test-slug", str(pdf_dir))

        # Assert
        assert result is not None
        assert "test-slug.pdf" in result

    def test_find_pdf_path_not_found(self, tmp_path):
        """Test finding PDF when it doesn't exist"""
        # Arrange
        pdf_dir = tmp_path / "pdfs"
        pdf_dir.mkdir()

        # Act
        result = find_pdf_path("nonexistent-slug", str(pdf_dir))

        # Assert
        assert result is None

    def test_save_unified_library(self, tmp_path, sample_metadata_list):
        """Test saving unified library to JSON"""
        # Arrange
        output_file = tmp_path / "unified_library.json"
        converted_papers = [convert_to_unified_format(p) for p in sample_metadata_list]

        # Act
        save_unified_library(converted_papers, str(output_file))

        # Assert
        assert output_file.exists()

        # Load and verify
        with open(output_file) as f:
            loaded = json.load(f)

        assert len(loaded) == 1
        assert loaded[0]["title"] == "Test Paper on Optimization Algorithms"

    def test_preserves_all_original_data(self, sample_journal_club_paper):
        """Test that no data is lost from original metadata.json"""
        # Act
        result = convert_to_unified_format(sample_journal_club_paper)

        # Assert - All original data preserved in sources
        source = result["sources"][0]
        assert source["url"] == sample_journal_club_paper["url"]
        assert source["doi_url"] == sample_journal_club_paper["doi_url"]
        assert source["description"] == sample_journal_club_paper["description"]
        assert source["discovered_at"] == sample_journal_club_paper["scraped_at"]

    def test_validates_output_schema(self, sample_journal_club_paper):
        """Test output matches expected schema"""
        # Act
        result = convert_to_unified_format(sample_journal_club_paper)

        # Assert - Schema validation
        required_fields = ["id", "title", "abstract", "identifiers", "sources", "metadata", "files", "analysis"]
        for field in required_fields:
            assert field in result, f"Missing required field: {field}"

        # Identifiers schema
        assert "doi" in result["identifiers"]
        assert "journalclub_slug" in result["identifiers"]

        # Sources schema
        assert isinstance(result["sources"], list)
        assert len(result["sources"]) > 0
        assert "source" in result["sources"][0]
        assert "url" in result["sources"][0]

        # Analysis schema
        assert isinstance(result["analysis"]["theories"], list)
        assert isinstance(result["analysis"]["relevant_to"], list)
