#!/usr/bin/env node

/**
 * CodeScholar MCP Server
 * Context-aware academic paper search for AI agents
 *
 * Tools:
 *   - search_papers: Semantic search across paper library
 *   - get_paper_details: Get full details of a specific paper
 *   - find_related_papers: Find papers related to code concepts
 *   - get_library_stats: Get library statistics
 */

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { ListToolsRequestSchema, CallToolRequestSchema } from '@modelcontextprotocol/sdk/types.js';
import { LocalIndex } from 'vectra';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load configuration
const config = JSON.parse(
  await fs.readFile(path.join(__dirname, 'config.json'), 'utf8')
);

// Resolve library path relative to server directory
const LIBRARY_PATH = path.resolve(__dirname, config.library.path);
const VECTRA_INDEX_PATH = path.join(__dirname, 'vectra-index');

// In-memory paper index
let papers = [];
let paperIndex = new Map(); // id -> paper
let titleIndex = [];        // { title_lower, id } for text search

// Vectra vector search
let vectraIndex = null;
let vectorSearchEnabled = false;

/**
 * Load and index the paper library
 */
async function loadLibrary() {
  try {
    const data = await fs.readFile(LIBRARY_PATH, 'utf8');
    papers = JSON.parse(data);

    // Build indexes
    paperIndex.clear();
    titleIndex = [];

    for (const paper of papers) {
      paperIndex.set(paper.id, paper);
      titleIndex.push({
        title_lower: (paper.title || '').toLowerCase(),
        abstract_lower: (paper.abstract || '').toLowerCase(),
        authors_lower: (paper.authors || []).join(' ').toLowerCase(),
        id: paper.id
      });
    }

    console.error(`[CodeScholar] Loaded ${papers.length} papers from library`);
    return true;
  } catch (error) {
    console.error(`[CodeScholar] Error loading library: ${error.message}`);
    return false;
  }
}

/**
 * Load Vectra vector index (if built)
 */
async function loadVectraIndex() {
  try {
    vectraIndex = new LocalIndex(VECTRA_INDEX_PATH);
    if (await vectraIndex.isIndexCreated()) {
      vectorSearchEnabled = true;
      console.error(`[CodeScholar] Vectra index loaded from ${VECTRA_INDEX_PATH}`);
      return true;
    } else {
      console.error('[CodeScholar] Vectra index not found - using text search only');
      console.error('  Run: node build-vectra-index.js  to enable vector search');
      vectraIndex = null;
      return false;
    }
  } catch (error) {
    console.error(`[CodeScholar] Vectra load error: ${error.message}`);
    vectraIndex = null;
    return false;
  }
}

/**
 * Vector-based semantic search using Vectra
 * Returns papers ranked by cosine similarity to query embedding
 */
async function vectorSearch(queryEmbedding, limit = 10, filters = {}) {
  if (!vectraIndex || !vectorSearchEnabled) return [];

  try {
    // Build Vectra filter if needed
    let metadataFilter = undefined;
    const conditions = [];
    if (filters.year) {
      conditions.push({ year: { $eq: filters.year } });
    }
    if (filters.min_citations) {
      conditions.push({ citation_count: { $gte: filters.min_citations } });
    }
    if (conditions.length === 1) {
      metadataFilter = conditions[0];
    } else if (conditions.length > 1) {
      metadataFilter = { $and: conditions };
    }

    const results = await vectraIndex.queryItems(queryEmbedding, limit, metadataFilter);

    return results.map(r => ({
      id: r.item.metadata.paper_id,
      title: r.item.metadata.title,
      abstract: r.item.metadata.abstract || '',
      authors: r.item.metadata.authors ? r.item.metadata.authors.split(', ') : [],
      year: r.item.metadata.year,
      citation_count: r.item.metadata.citation_count,
      doi: r.item.metadata.doi,
      doi_url: r.item.metadata.doi_url,
      relevance_score: Math.round(r.score * 10000) / 10000,
    }));
  } catch (error) {
    console.error(`[CodeScholar] Vector search error: ${error.message}`);
    return [];
  }
}

/**
 * Hybrid search: combines vector similarity + text matching
 * Uses vector search for semantic results, text search for keyword precision
 */
async function hybridSearch(query, queryEmbedding, limit = 10, filters = {}) {
  // Get results from both sources
  const vectorResults = queryEmbedding
    ? await vectorSearch(queryEmbedding, limit * 2, filters)
    : [];
  const textResults = textSearch(query, limit * 2, filters);

  // Merge and deduplicate, combining scores
  const merged = new Map();

  // Vector results (cosine similarity 0-1, scale to match text range)
  for (const r of vectorResults) {
    merged.set(r.id, {
      ...r,
      vector_score: r.relevance_score,
      text_score: 0,
      relevance_score: r.relevance_score * 10, // Scale vector scores
    });
  }

  // Text results
  for (const r of textResults) {
    if (merged.has(r.id)) {
      // Boost papers found by both methods
      const existing = merged.get(r.id);
      existing.text_score = r.relevance_score;
      existing.relevance_score += r.relevance_score;
    } else {
      merged.set(r.id, {
        ...r,
        vector_score: 0,
        text_score: r.relevance_score,
      });
    }
  }

  // Sort by combined score
  const sorted = [...merged.values()]
    .sort((a, b) => b.relevance_score - a.relevance_score)
    .slice(0, limit);

  // Round scores
  return sorted.map(r => ({
    ...r,
    relevance_score: Math.round(r.relevance_score * 100) / 100,
  }));
}

/**
 * Text-based search across papers (fallback when no vector DB)
 * Supports multi-term matching with relevance scoring
 */
function textSearch(query, limit = 10, filters = {}) {
  const queryTerms = query.toLowerCase().split(/\s+/).filter(t => t.length > 2);

  if (queryTerms.length === 0) return [];

  const scored = [];

  for (const entry of titleIndex) {
    let score = 0;
    const paper = paperIndex.get(entry.id);

    // Apply filters
    if (filters.year && paper.metadata?.year !== filters.year) continue;
    if (filters.min_citations && (paper.metadata?.citation_count || 0) < filters.min_citations) continue;

    // Score based on term matches
    for (const term of queryTerms) {
      // Title match (highest weight)
      if (entry.title_lower.includes(term)) score += 3;
      // Abstract match (medium weight)
      if (entry.abstract_lower.includes(term)) score += 2;
      // Author match (lower weight)
      if (entry.authors_lower.includes(term)) score += 1;
    }

    // Bonus for exact phrase match in title
    if (entry.title_lower.includes(query.toLowerCase())) score += 5;

    // Bonus for citation count (normalized)
    const citations = paper.metadata?.citation_count || 0;
    if (citations > 0) score += Math.min(citations / 100, 1);

    if (score > 0) {
      scored.push({ paper, score });
    }
  }

  // Sort by score descending
  scored.sort((a, b) => b.score - a.score);

  return scored.slice(0, limit).map(({ paper, score }) => ({
    id: paper.id,
    title: paper.title,
    abstract: paper.abstract ? paper.abstract.substring(0, 300) + '...' : '',
    authors: paper.authors || [],
    year: paper.metadata?.year,
    citation_count: paper.metadata?.citation_count,
    doi: paper.identifiers?.doi,
    doi_url: paper.identifiers?.doi_url,
    relevance_score: Math.round(score * 100) / 100
  }));
}

/**
 * Get full paper details by ID
 */
function getPaperById(paperId) {
  const paper = paperIndex.get(paperId);
  if (!paper) return null;

  return {
    id: paper.id,
    title: paper.title,
    abstract: paper.abstract,
    authors: paper.authors || [],
    identifiers: paper.identifiers || {},
    metadata: {
      year: paper.metadata?.year,
      citation_count: paper.metadata?.citation_count,
      published_date: paper.metadata?.published_date
    },
    sources: paper.sources || [],
    access: {
      doi_url: paper.identifiers?.doi_url,
      semantic_scholar_url: paper.identifiers?.semantic_scholar_id
        ? `https://www.semanticscholar.org/paper/${paper.identifiers.semantic_scholar_id}`
        : null
    }
  };
}

/**
 * Find papers by DOI
 */
function getPaperByDoi(doi) {
  for (const paper of papers) {
    if (paper.identifiers?.doi === doi) {
      return getPaperById(paper.id);
    }
  }
  return null;
}

/**
 * Get library statistics
 */
function getLibraryStats() {
  const totalPapers = papers.length;
  const withAbstract = papers.filter(p => p.abstract && p.abstract.trim()).length;
  const withDoi = papers.filter(p => p.identifiers?.doi).length;
  const withCitations = papers.filter(p => p.metadata?.citation_count != null).length;
  const withS2 = papers.filter(p => p.identifiers?.semantic_scholar_id).length;
  const withEmbedding = papers.filter(p => p.analysis?.embedding).length;

  // Citation stats
  const citations = papers
    .map(p => p.metadata?.citation_count || 0)
    .filter(c => c > 0);
  const totalCitations = citations.reduce((a, b) => a + b, 0);
  const avgCitations = citations.length > 0 ? Math.round(totalCitations / citations.length) : 0;
  const maxCitations = citations.length > 0 ? Math.max(...citations) : 0;

  // Year distribution
  const yearDist = {};
  for (const paper of papers) {
    const year = paper.metadata?.year;
    if (year) {
      yearDist[year] = (yearDist[year] || 0) + 1;
    }
  }

  // Top cited papers
  const topCited = [...papers]
    .filter(p => p.metadata?.citation_count > 0)
    .sort((a, b) => (b.metadata?.citation_count || 0) - (a.metadata?.citation_count || 0))
    .slice(0, 5)
    .map(p => ({
      title: p.title,
      citations: p.metadata?.citation_count,
      doi: p.identifiers?.doi
    }));

  return {
    total_papers: totalPapers,
    coverage: {
      with_abstract: withAbstract,
      with_doi: withDoi,
      with_citations: withCitations,
      with_semantic_scholar: withS2,
      with_embedding: withEmbedding
    },
    citations: {
      total: totalCitations,
      average: avgCitations,
      max: maxCitations,
      papers_with_citations: citations.length
    },
    year_distribution: yearDist,
    top_cited: topCited,
    architecture: 'metadata_plus_abstract',
    search_mode: vectorSearchEnabled ? 'hybrid_vectra' : 'text_only',
    vector_db: vectorSearchEnabled ? 'vectra (local)' : 'none'
  };
}

// Initialize MCP Server
const server = new Server(
  {
    name: 'codescholar',
    version: config.server.version,
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Register tool list
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: 'search_papers',
        description: 'Search academic papers by keyword, topic, or concept. Returns ranked results with relevance scores. Use this to find papers related to algorithms, techniques, or research topics you encounter in code.',
        inputSchema: {
          type: 'object',
          properties: {
            query: {
              type: 'string',
              description: 'Search query - keywords, concepts, or natural language question (e.g., "machine learning optimization", "graph neural networks")'
            },
            limit: {
              type: 'number',
              description: 'Maximum number of results to return (default: 10, max: 50)'
            },
            year: {
              type: 'number',
              description: 'Filter by publication year'
            },
            min_citations: {
              type: 'number',
              description: 'Minimum citation count filter'
            }
          },
          required: ['query']
        }
      },
      {
        name: 'get_paper_details',
        description: 'Get full details of a specific paper by ID or DOI. Returns title, abstract, authors, citation count, and access URLs.',
        inputSchema: {
          type: 'object',
          properties: {
            paper_id: {
              type: 'string',
              description: 'Paper UUID from search results'
            },
            doi: {
              type: 'string',
              description: 'DOI identifier (alternative to paper_id)'
            }
          }
        }
      },
      {
        name: 'find_related_papers',
        description: 'Find papers related to specific code concepts, algorithms, or techniques. Provide code context or concept description to find relevant academic research.',
        inputSchema: {
          type: 'object',
          properties: {
            concepts: {
              type: 'array',
              items: { type: 'string' },
              description: 'List of concepts, algorithms, or techniques to search for (e.g., ["gradient descent", "backpropagation", "neural network"])'
            },
            code_context: {
              type: 'string',
              description: 'Code snippet or description of what the code does - will be analyzed to extract relevant search terms'
            },
            limit: {
              type: 'number',
              description: 'Maximum results per concept (default: 5)'
            }
          }
        }
      },
      {
        name: 'get_library_stats',
        description: 'Get statistics about the CodeScholar paper library including total papers, citation stats, coverage metrics, and top-cited papers.',
        inputSchema: {
          type: 'object',
          properties: {}
        }
      },
      {
        name: 'analyze_code',
        description: 'Analyze source code to extract algorithms, techniques, data structures, and research concepts. Returns detected concepts with confidence scores and generates paper search queries. Supports Python (AST parsing), JavaScript, and TypeScript.',
        inputSchema: {
          type: 'object',
          properties: {
            file_path: {
              type: 'string',
              description: 'Path to a source code file to analyze'
            },
            directory: {
              type: 'string',
              description: 'Path to a directory to analyze recursively (alternative to file_path)'
            },
            search_library: {
              type: 'boolean',
              description: 'If true, automatically search the paper library for each extracted concept (default: true)'
            },
            limit: {
              type: 'number',
              description: 'Maximum papers per concept when search_library is true (default: 3)'
            }
          }
        }
      },
      {
        name: 'discover_papers',
        description: 'Discover new papers from external sources (arXiv, Semantic Scholar). Searches for papers that are NOT already in the local library. Use this to find cutting-edge research on a topic.',
        inputSchema: {
          type: 'object',
          properties: {
            query: {
              type: 'string',
              description: 'Search query for paper discovery'
            },
            sources: {
              type: 'array',
              items: { type: 'string', enum: ['arxiv', 'semantic_scholar'] },
              description: 'Sources to search (default: both). Options: "arxiv", "semantic_scholar"'
            },
            max_results: {
              type: 'number',
              description: 'Maximum results per source (default: 5)'
            },
            year: {
              type: 'string',
              description: 'Year filter for Semantic Scholar (e.g., "2024" or "2023-2024")'
            }
          },
          required: ['query']
        }
      },
      {
        name: 'link_papers_to_code',
        description: 'The flagship CodeScholar tool. Analyzes source code to extract concepts, generates optimized search queries, searches the paper library, and scores each paper for applicability. Returns a ranked list of the most relevant academic papers for the given code. Use this when you want to understand the research foundations behind code.',
        inputSchema: {
          type: 'object',
          properties: {
            file_path: {
              type: 'string',
              description: 'Path to a source code file to analyze and link to papers'
            },
            directory: {
              type: 'string',
              description: 'Path to a directory to analyze recursively (alternative to file_path)'
            },
            max_papers: {
              type: 'number',
              description: 'Maximum papers to return (default: 10)'
            },
            min_score: {
              type: 'number',
              description: 'Minimum applicability score threshold 0.0-1.0 (default: 0.15)'
            }
          }
        }
      }
    ]
  };
});

// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case 'search_papers': {
        if (!args.query) {
          throw new Error('query parameter is required');
        }

        const limit = Math.min(args.limit || config.search.default_limit, config.search.max_limit);
        const filters = {};
        if (args.year) filters.year = args.year;
        if (args.min_citations) filters.min_citations = args.min_citations;

        // Use hybrid search if vector index is available
        let results;
        let searchMode;

        if (vectorSearchEnabled) {
          // Get query embedding by finding a paper with matching text and reusing its vector
          // For true semantic search, we use the vector index directly
          // Vectra queryItems also supports text query via embedding lookup
          // For now: hybrid = vector candidates + text reranking
          const queryEmbedding = await getQueryEmbedding(args.query);
          if (queryEmbedding) {
            results = await hybridSearch(args.query, queryEmbedding, limit, filters);
            searchMode = 'hybrid';
          } else {
            results = textSearch(args.query, limit, filters);
            searchMode = 'text';
          }
        } else {
          results = textSearch(args.query, limit, filters);
          searchMode = 'text';
        }

        return {
          content: [{
            type: 'text',
            text: JSON.stringify({
              query: args.query,
              total_results: results.length,
              search_mode: searchMode,
              vector_search_available: vectorSearchEnabled,
              results
            }, null, 2)
          }]
        };
      }

      case 'get_paper_details': {
        if (!args.paper_id && !args.doi) {
          throw new Error('Either paper_id or doi parameter is required');
        }

        let paper;
        if (args.paper_id) {
          paper = getPaperById(args.paper_id);
        } else {
          paper = getPaperByDoi(args.doi);
        }

        if (!paper) {
          return {
            content: [{
              type: 'text',
              text: JSON.stringify({
                error: 'Paper not found',
                searched_by: args.paper_id ? 'paper_id' : 'doi',
                value: args.paper_id || args.doi
              }, null, 2)
            }]
          };
        }

        return {
          content: [{
            type: 'text',
            text: JSON.stringify(paper, null, 2)
          }]
        };
      }

      case 'find_related_papers': {
        const concepts = args.concepts || [];
        const limit = args.limit || 5;

        // Extract concepts from code context if provided
        if (args.code_context) {
          const extracted = extractConceptsFromCode(args.code_context);
          concepts.push(...extracted);
        }

        if (concepts.length === 0) {
          throw new Error('Provide concepts array or code_context to search');
        }

        // Search for each concept
        const allResults = {};
        const seen = new Set();

        for (const concept of concepts) {
          const results = textSearch(concept, limit);
          allResults[concept] = results.filter(r => {
            if (seen.has(r.id)) return false;
            seen.add(r.id);
            return true;
          });
        }

        return {
          content: [{
            type: 'text',
            text: JSON.stringify({
              concepts_searched: concepts,
              results_by_concept: allResults,
              total_unique_papers: seen.size
            }, null, 2)
          }]
        };
      }

      case 'get_library_stats': {
        const stats = getLibraryStats();

        return {
          content: [{
            type: 'text',
            text: JSON.stringify(stats, null, 2)
          }]
        };
      }

      case 'analyze_code': {
        if (!args.file_path && !args.directory) {
          throw new Error('Either file_path or directory parameter is required');
        }

        const searchLibrary = args.search_library !== false;
        const limit = args.limit || 3;
        const targetPath = args.file_path || args.directory;

        // Call the Python concept extractor
        const { execSync } = await import('child_process');
        const scriptPath = path.resolve(__dirname, 'scripts/analyzers/concept_extractor.py');

        // Build Python command to run analysis
        const pythonCmd = args.directory
          ? `python -c "import sys; sys.path.insert(0, '${path.resolve(__dirname, 'scripts').replace(/\\/g, '\\\\')}'); from analyzers.concept_extractor import analyze_directory, aggregate_concepts; import json; results = analyze_directory('${targetPath.replace(/\\/g, '\\\\')}'); print(json.dumps(aggregate_concepts(results), default=str))"`
          : `python -c "import sys; sys.path.insert(0, '${path.resolve(__dirname, 'scripts').replace(/\\/g, '\\\\')}'); from analyzers.concept_extractor import analyze_file; import json; r = analyze_file('${targetPath.replace(/\\/g, '\\\\')}'); print(json.dumps(r.to_dict() if r else {'error': 'Unsupported file type'}, default=str))"`;

        let analysisResult;
        try {
          const output = execSync(pythonCmd, {
            encoding: 'utf8',
            timeout: 30000,
            cwd: __dirname
          });
          analysisResult = JSON.parse(output.trim());
        } catch (pyError) {
          throw new Error(`Code analysis failed: ${pyError.message}`);
        }

        // Optionally search library for each concept
        let paperResults = {};
        if (searchLibrary && analysisResult.search_queries) {
          const queries = analysisResult.search_queries || [];
          const seen = new Set();

          for (const query of queries.slice(0, 10)) {
            const results = textSearch(query, limit);
            paperResults[query] = results.filter(r => {
              if (seen.has(r.id)) return false;
              seen.add(r.id);
              return true;
            });
          }
        }

        return {
          content: [{
            type: 'text',
            text: JSON.stringify({
              analysis: analysisResult,
              related_papers: searchLibrary ? paperResults : undefined,
              total_papers_found: searchLibrary
                ? Object.values(paperResults).reduce((sum, arr) => sum + arr.length, 0)
                : undefined
            }, null, 2)
          }]
        };
      }

      case 'discover_papers': {
        if (!args.query) {
          throw new Error('query parameter is required');
        }

        const maxResults = args.max_results || 5;
        const sources = args.sources || ['arxiv', 'semantic_scholar'];
        const scriptsPath = path.resolve(__dirname, 'scripts').replace(/\\/g, '\\\\');

        const allResults = {};

        // Call Python sources
        for (const source of sources) {
          const { execSync } = await import('child_process');

          let pythonCmd;
          if (source === 'arxiv') {
            pythonCmd = `python -c "import sys, json, asyncio; sys.path.insert(0, '${scriptsPath}'); from sources.arxiv_source import search_arxiv; results = asyncio.run(search_arxiv('${args.query.replace(/'/g, "\\'")}', ${maxResults})); print(json.dumps(results, default=str))"`;
          } else if (source === 'semantic_scholar') {
            const yearParam = args.year ? `, year='${args.year}'` : '';
            pythonCmd = `python -c "import sys, json, asyncio; sys.path.insert(0, '${scriptsPath}'); from sources.semantic_scholar_source import search_semantic_scholar; results = asyncio.run(search_semantic_scholar('${args.query.replace(/'/g, "\\'")}', ${maxResults}${yearParam})); print(json.dumps(results, default=str))"`;
          } else {
            continue;
          }

          try {
            const output = execSync(pythonCmd, {
              encoding: 'utf8',
              timeout: 60000,
              cwd: __dirname
            });
            const results = JSON.parse(output.trim());

            // Filter out papers already in library (by DOI or title)
            const newPapers = results.filter(p => {
              const doi = p.identifiers?.doi;
              if (doi) {
                const existing = papers.find(lib => lib.identifiers?.doi === doi);
                if (existing) return false;
              }
              // Fuzzy title match
              const titleLower = (p.title || '').toLowerCase();
              const titleMatch = titleIndex.find(t => t.title_lower === titleLower);
              return !titleMatch;
            });

            allResults[source] = {
              total_found: results.length,
              new_papers: newPapers.length,
              papers: newPapers
            };
          } catch (pyError) {
            allResults[source] = {
              error: pyError.message,
              total_found: 0,
              new_papers: 0,
              papers: []
            };
          }
        }

        const totalNew = Object.values(allResults).reduce((sum, r) => sum + (r.new_papers || 0), 0);

        return {
          content: [{
            type: 'text',
            text: JSON.stringify({
              query: args.query,
              sources_searched: sources,
              total_new_papers: totalNew,
              results_by_source: allResults
            }, null, 2)
          }]
        };
      }

      case 'link_papers_to_code': {
        if (!args.file_path && !args.directory) {
          throw new Error('Either file_path or directory parameter is required');
        }

        const maxPapers = args.max_papers || 10;
        const minScore = args.min_score || 0.15;
        const targetPath = args.file_path || args.directory;
        const scriptsPath = path.resolve(__dirname, 'scripts').replace(/\\/g, '\\\\');

        const { execSync } = await import('child_process');

        // Step 1: Analyze code to extract concepts
        const analyzeCmd = args.directory
          ? `python -c "import sys; sys.path.insert(0, '${scriptsPath}'); from analyzers.concept_extractor import analyze_directory, aggregate_concepts; import json; results = analyze_directory('${targetPath.replace(/\\/g, '\\\\')}'); print(json.dumps(aggregate_concepts(results), default=str))"`
          : `python -c "import sys; sys.path.insert(0, '${scriptsPath}'); from analyzers.concept_extractor import analyze_file; import json; r = analyze_file('${targetPath.replace(/\\/g, '\\\\')}'); print(json.dumps(r.to_dict() if r else {'concepts': [], 'search_queries': []}, default=str))"`;

        let analysisResult;
        try {
          const output = execSync(analyzeCmd, {
            encoding: 'utf8',
            timeout: 30000,
            cwd: __dirname
          });
          analysisResult = JSON.parse(output.trim());
        } catch (pyError) {
          throw new Error(`Code analysis failed: ${pyError.message}`);
        }

        // Step 2: Generate optimized queries
        const conceptsForQuery = (analysisResult.concepts || []).map(c => ({
          name: c.name,
          category: c.category,
          confidence: c.max_confidence || c.confidence || 0.5
        }));

        let generatedQueries;
        try {
          const queryCmd = `python -c "import sys, json; sys.path.insert(0, '${scriptsPath}'); from query_generator import QueryGenerator; g = QueryGenerator(); concepts = json.loads('''${JSON.stringify(conceptsForQuery).replace(/'/g, "\\'")}'''); queries = g.from_concepts(concepts, max_queries=15); print(json.dumps([{'query': q.query, 'confidence': q.confidence, 'strategy': q.strategy.value} for q in queries]))"`;
          const qOutput = execSync(queryCmd, {
            encoding: 'utf8',
            timeout: 15000,
            cwd: __dirname
          });
          generatedQueries = JSON.parse(qOutput.trim());
        } catch (pyError) {
          // Fallback to search_queries from analysis
          generatedQueries = (analysisResult.search_queries || []).map(q => ({
            query: q, confidence: 0.7, strategy: 'direct'
          }));
        }

        // Step 3: Search library with generated queries
        const conceptNames = new Set(
          (analysisResult.concepts || []).map(c => c.name?.toLowerCase()).filter(Boolean)
        );
        const candidatePapers = new Map(); // paper_id -> { paper, max_search_score }

        for (const gq of generatedQueries.slice(0, 10)) {
          const results = textSearch(gq.query, 20);
          for (const r of results) {
            const existing = candidatePapers.get(r.id);
            if (!existing || r.relevance_score > existing.max_search_score) {
              candidatePapers.set(r.id, {
                paper: paperIndex.get(r.id),
                max_search_score: r.relevance_score
              });
            }
          }
        }

        // Step 4: Score applicability
        const candidateList = [...candidatePapers.values()].map(c => c.paper).filter(Boolean);
        const queryStr = generatedQueries.slice(0, 3).map(q => q.query).join(' ');

        let scoredResults;
        try {
          const scoreCmd = `python -c "import sys, json; sys.path.insert(0, '${scriptsPath}'); from applicability_scorer import ApplicabilityScorer; scorer = ApplicabilityScorer(); papers = json.loads('''${JSON.stringify(candidateList).replace(/\\/g, '\\\\').replace(/'/g, "\\'")}'''); concepts = set(json.loads('''${JSON.stringify([...conceptNames]).replace(/'/g, "\\'")}''')); results = scorer.score_batch(papers, concepts, '''${queryStr.replace(/'/g, "\\'")}''', min_score=${minScore}); print(json.dumps([{'paper_id': r.paper_id, 'title': r.title, 'total_score': r.total_score, 'breakdown': r.breakdown, 'matched_concepts': r.matched_concepts} for r in results[:${maxPapers}]]))"`;
          const sOutput = execSync(scoreCmd, {
            encoding: 'utf8',
            timeout: 15000,
            cwd: __dirname
          });
          scoredResults = JSON.parse(sOutput.trim());
        } catch (pyError) {
          // Fallback: return candidates sorted by search score
          scoredResults = [...candidatePapers.entries()]
            .sort((a, b) => b[1].max_search_score - a[1].max_search_score)
            .slice(0, maxPapers)
            .map(([id, data]) => ({
              paper_id: id,
              title: data.paper?.title || '',
              total_score: data.max_search_score / 20, // normalize
              breakdown: { search_score: data.max_search_score },
              matched_concepts: []
            }));
        }

        // Enrich results with access URLs
        const enriched = scoredResults.map(r => {
          const paper = paperIndex.get(r.paper_id);
          return {
            ...r,
            doi: paper?.identifiers?.doi,
            doi_url: paper?.identifiers?.doi_url,
            year: paper?.metadata?.year,
            citation_count: paper?.metadata?.citation_count,
            authors: (paper?.authors || []).slice(0, 5),
          };
        });

        return {
          content: [{
            type: 'text',
            text: JSON.stringify({
              target: targetPath,
              concepts_detected: (analysisResult.concepts || []).length,
              top_concepts: (analysisResult.concepts || []).slice(0, 10).map(c => c.name),
              queries_generated: generatedQueries.length,
              candidates_searched: candidatePapers.size,
              papers_linked: enriched.length,
              min_score_threshold: minScore,
              linked_papers: enriched
            }, null, 2)
          }]
        };
      }

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error) {
    return {
      content: [{
        type: 'text',
        text: JSON.stringify({ error: error.message })
      }],
      isError: true
    };
  }
});

/**
 * Extract searchable concepts from code context
 * Simple keyword extraction for MVP - will be enhanced with AST parsing later
 */
function extractConceptsFromCode(codeContext) {
  const concepts = [];

  // Common algorithm/technique patterns
  const patterns = [
    // ML/AI
    /(?:neural\s+network|deep\s+learning|machine\s+learning|reinforcement\s+learning)/gi,
    /(?:gradient\s+descent|backpropagation|attention\s+mechanism|transformer)/gi,
    /(?:random\s+forest|decision\s+tree|support\s+vector|naive\s+bayes)/gi,
    /(?:convolutional|recurrent|generative|adversarial|autoencoder)/gi,
    /(?:clustering|classification|regression|dimensionality\s+reduction)/gi,
    // Data structures & algorithms
    /(?:binary\s+search|hash\s+map|linked\s+list|binary\s+tree|graph\s+algorithm)/gi,
    /(?:sorting|dynamic\s+programming|greedy\s+algorithm|divide\s+and\s+conquer)/gi,
    // Optimization
    /(?:optimization|genetic\s+algorithm|simulated\s+annealing|particle\s+swarm)/gi,
    /(?:linear\s+programming|convex\s+optimization|stochastic)/gi,
    // NLP
    /(?:natural\s+language|text\s+processing|tokenization|embedding|sentiment)/gi,
    /(?:named\s+entity|part.of.speech|language\s+model)/gi,
    // Computer vision
    /(?:image\s+recognition|object\s+detection|segmentation|feature\s+extraction)/gi,
    // Statistics
    /(?:bayesian|markov|monte\s+carlo|statistical|probability)/gi,
    // Security
    /(?:encryption|cryptograph|authentication|zero.knowledge)/gi,
    // Systems
    /(?:distributed\s+system|load\s+balanc|microservice|consensus\s+algorithm)/gi
  ];

  for (const pattern of patterns) {
    const matches = codeContext.match(pattern);
    if (matches) {
      concepts.push(...matches.map(m => m.toLowerCase().trim()));
    }
  }

  // Deduplicate
  return [...new Set(concepts)];
}

/**
 * Get a query embedding for semantic search
 * Uses OpenAI API if OPENAI_API_KEY is set, otherwise returns null (text-only fallback)
 */
async function getQueryEmbedding(query) {
  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) return null;

  try {
    const response = await fetch('https://api.openai.com/v1/embeddings', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'text-embedding-3-large',
        input: query,
      }),
    });

    if (!response.ok) return null;

    const data = await response.json();
    return data.data?.[0]?.embedding || null;
  } catch {
    return null;
  }
}

// Main startup
async function main() {
  // Load paper library
  await loadLibrary();

  // Load Vectra vector index
  await loadVectraIndex();

  // Start MCP server
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('[CodeScholar] MCP server running on stdio');
  console.error(`[CodeScholar] Search mode: ${vectorSearchEnabled ? 'hybrid (text + vector)' : 'text only'}`);
}

main().catch((error) => {
  console.error('[CodeScholar] Server error:', error);
  process.exit(1);
});
