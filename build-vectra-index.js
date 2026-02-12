#!/usr/bin/env node

/**
 * Build Vectra index from unified_library.json embeddings
 *
 * Reads papers with pre-computed embeddings and inserts them into
 * a local Vectra index for fast cosine similarity search.
 *
 * Usage: node build-vectra-index.js
 */

import { LocalIndex } from 'vectra';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const config = JSON.parse(
  await fs.readFile(path.join(__dirname, 'config.json'), 'utf8')
);

const LIBRARY_PATH = path.resolve(__dirname, config.library.path);
const INDEX_PATH = path.join(__dirname, 'vectra-index');

async function main() {
  console.log('=' .repeat(60));
  console.log('Building Vectra Index from Paper Embeddings');
  console.log('=' .repeat(60));

  // Load library
  console.log('\n[1/3] Loading unified_library.json...');
  const data = await fs.readFile(LIBRARY_PATH, 'utf8');
  const papers = JSON.parse(data);
  console.log(`  Loaded ${papers.length} papers`);

  const withEmbeddings = papers.filter(p => p.analysis?.embedding?.length > 0);
  console.log(`  Papers with embeddings: ${withEmbeddings.length}/${papers.length}`);

  if (withEmbeddings.length === 0) {
    console.log('\n[ERROR] No papers with embeddings. Run generate_embeddings.py first.');
    process.exit(1);
  }

  // Create Vectra index
  console.log('\n[2/3] Creating Vectra index...');
  const index = new LocalIndex(INDEX_PATH);

  if (await index.isIndexCreated()) {
    console.log('  Deleting existing index...');
    await index.deleteIndex();
  }

  await index.createIndex({
    version: 1,
    metadata_config: {
      // Fields kept in index.json for fast filtering
      indexed: ['year', 'citation_count']
    }
  });
  console.log(`  Index created at: ${INDEX_PATH}`);

  // Insert papers
  console.log(`\n[3/3] Inserting ${withEmbeddings.length} papers...`);
  let inserted = 0;
  let errors = 0;

  for (const paper of withEmbeddings) {
    try {
      await index.insertItem({
        id: paper.id,
        vector: paper.analysis.embedding,
        metadata: {
          paper_id: paper.id,
          title: paper.title || '',
          abstract: (paper.abstract || '').substring(0, 500),
          authors: (paper.authors || []).slice(0, 5).join(', '),
          year: paper.metadata?.year || null,
          citation_count: paper.metadata?.citation_count || 0,
          doi: paper.identifiers?.doi || null,
          doi_url: paper.identifiers?.doi_url || null,
        }
      });
      inserted++;

      if (inserted % 50 === 0) {
        console.log(`  Inserted ${inserted}/${withEmbeddings.length}...`);
      }
    } catch (err) {
      errors++;
      if (errors <= 3) {
        console.log(`  [WARN] Failed to insert ${paper.id}: ${err.message}`);
      }
    }
  }

  console.log('\n' + '=' .repeat(60));
  console.log('Vectra Index Build Complete');
  console.log('=' .repeat(60));
  console.log(`Papers inserted: ${inserted}`);
  console.log(`Errors: ${errors}`);
  console.log(`Index path: ${INDEX_PATH}`);
  console.log(`\nThe MCP server will auto-detect this index on startup.`);
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
