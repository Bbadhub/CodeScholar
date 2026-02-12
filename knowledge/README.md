# CodeScholar Knowledge Base

A structured research knowledge base designed for AI agent consumption.
443 papers indexed across techniques, problems, and cross-domain connections.

## How To Use This

### "I have a problem to solve"
Start with **[Problems](problems/_index.md)** → find your problem type → see proven approaches with decision matrix.

### "I want to understand a technique"
Go to **[Techniques](techniques/_index.md)** → find the algorithm → get pseudocode, parameters, tradeoffs, and evidence.

### "I found interesting code and want the research behind it"
Search **[Papers](papers/)** → find papers by concept or domain → follow DOI links to full text.

### "I want to discover unexpected connections"
Check **[Connections](connections/connections.md)** → find techniques that bridge domains → apply solutions from other fields.

## Structure

```
knowledge/
├── problems/      ← START HERE: "I have this type of problem"
│   └── _index.md     Decision matrices, approach rankings
├── techniques/    ← REFERENCE: "How does this algorithm work?"
│   └── _index.md     Pseudocode, parameters, complexity, tradeoffs
├── papers/        ← EVIDENCE: "Show me the proof"
│   └── {slug}.md    DOIs, benchmarks, methodology, access links
└── connections/   ← DISCOVERY: "What else could work?"
    └── connections.md  Cross-domain bridges, concept co-occurrence
```

## Every Paper Includes

- **DOI and access URLs** for the full document
- Algorithm steps and pseudocode hints
- Key parameters with typical values
- Benchmarks: what was measured, against what, how much better
- "Use when" / "Don't use when" guidance
- Implementation gotchas
- Cross-references to related techniques

## Generated

Last updated: 2026-02-11
Model: GPT-4o for knowledge extraction
