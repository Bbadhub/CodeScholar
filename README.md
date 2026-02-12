# CodeScholar

Context-aware academic research MCP server. Analyzes codebases and links them to relevant academic papers using hybrid vector + text search.

## Features

- **7 MCP Tools**: search_papers, get_paper_details, find_related_papers, get_library_stats, analyze_code, discover_papers, link_papers_to_code
- **Hybrid Search**: Vectra vector DB (local, no Docker) + text keyword matching
- **Code Analysis**: AST-based concept extraction for Python, JS, TypeScript
- **Applicability Scoring**: 4-component weighted scoring (concept overlap, text relevance, recency, citations)
- **External Discovery**: Search arXiv and Semantic Scholar for new papers

## Quick Start

```bash
# Install Node.js dependencies
npm install

# Install Python dependencies
pip install -r requirements.txt

# Place your unified_library.json in data/
mkdir data
cp /path/to/unified_library.json data/

# Build vector search index (optional, requires OPENAI_API_KEY for embeddings)
node build-vectra-index.js

# Start the MCP server
npm start
```

## MCP Configuration

Add to your Claude Code `.mcp.json`:

```json
{
  "mcpServers": {
    "codescholar": {
      "command": "node",
      "args": ["/path/to/CodeScholar/server.js"],
      "env": {
        "OPENAI_API_KEY": "your-key-here"
      }
    }
  }
}
```

## Architecture

```
CodeScholar/
├── server.js                 # MCP server (7 tools)
├── build-vectra-index.js     # One-time index builder
├── config.json               # Server configuration
├── data/                     # Paper library (gitignored)
│   └── unified_library.json
├── vectra-index/             # Vector search index (gitignored)
├── scripts/
│   ├── query_generator.py        # Smart query generation
│   ├── applicability_scorer.py   # Paper relevance scoring
│   ├── generate_embeddings.py    # OpenAI embedding generation
│   ├── analyzers/
│   │   └── concept_extractor.py  # AST-based code analysis
│   ├── sources/
│   │   ├── arxiv_source.py       # arXiv API integration
│   │   └── semantic_scholar_source.py
│   └── tests/                    # Test suites (135 tests)
└── requirements.txt
```

## Search Modes

| Mode | Requirements | Performance |
|------|-------------|-------------|
| Text only | Just `unified_library.json` | Fast, keyword-based |
| Hybrid | + Vectra index + OPENAI_API_KEY | Best results, semantic + keyword |

## License

MIT
