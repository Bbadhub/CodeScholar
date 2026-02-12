#!/usr/bin/env python3
"""
CodeScholar Knowledge Base Generator - Multi-Pass Pipeline

Transforms raw paper metadata into a 3-layer knowledge architecture
designed for AI agent consumption via MCP wiki:

  Layer 1: PROBLEMS   → "I have this kind of problem" → decision matrix
  Layer 2: TECHNIQUES → "Here's how to solve it" → algorithm + pseudocode + proof
  Layer 3: PAPERS     → "Here's the evidence" → DOI + benchmarks + methodology

Pass 1: Extract deep knowledge from each paper (GPT-4)
Pass 2: Cluster papers → generate technique cards
Pass 3: Cluster techniques → generate problem entry points
Pass 4: Map cross-domain connections for emergent discovery

Usage:
  python scripts/generate_knowledge_base.py                    # full run
  python scripts/generate_knowledge_base.py --limit 10         # test
  python scripts/generate_knowledge_base.py --skip-existing    # resume
  python scripts/generate_knowledge_base.py --pass 1           # single pass
"""

import json
import os
import sys
import re
import argparse
import time
from pathlib import Path
from collections import defaultdict
from typing import Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from openai import OpenAI
except ImportError:
    print("ERROR: pip install openai")
    sys.exit(1)

try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False
    print("WARNING: pymupdf not installed. Install with: pip install pymupdf")
    print("  PDF reading disabled - will use abstracts only.\n")


def safe_print(msg: str):
    """Print with fallback for Windows cp1252 encoding issues."""
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode('ascii', errors='replace').decode('ascii'))


def extract_pdf_text(pdf_path: str, max_pages: int = 15, max_chars: int = 30000) -> str:
    """Extract text from a PDF file using PyMuPDF.

    Returns the first max_chars characters from up to max_pages pages.
    Focuses on methodology, results, and algorithm sections.
    """
    if not HAS_PYMUPDF:
        return ""
    try:
        doc = fitz.open(pdf_path)
        pages_text = []
        total_chars = 0
        for i in range(min(max_pages, len(doc))):
            text = doc[i].get_text()
            # Clean up common PDF artifacts
            text = text.replace('\x00', '').replace('\ufb01', 'fi').replace('\ufb02', 'fl')
            text = text.replace('\ufb03', 'ffi').replace('\ufb04', 'ffl')
            pages_text.append(text)
            total_chars += len(text)
            if total_chars >= max_chars:
                break
        doc.close()
        full_text = "\n\n".join(pages_text)
        return full_text[:max_chars]
    except Exception as e:
        print(f"    [WARN] PDF read failed: {e}")
        return ""


def find_pdf_for_paper(paper: dict, pdfs_dir: str) -> str:
    """Find the PDF file matching a paper, if it exists."""
    if not pdfs_dir or not os.path.isdir(pdfs_dir):
        return ""
    # The PDF filenames are slugified versions of the title
    title = paper.get("title", "")
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'\s+', '-', slug.strip())

    # Try full slug match first (no truncation)
    candidate = os.path.join(pdfs_dir, slug + '.pdf')
    if os.path.exists(candidate):
        return candidate

    # Try truncated slug (80 chars)
    candidate = os.path.join(pdfs_dir, slug[:80] + '.pdf')
    if os.path.exists(candidate):
        return candidate

    # Try partial match - find PDFs that share a long prefix
    try:
        pdf_files = [f for f in os.listdir(pdfs_dir) if f.endswith('.pdf')]
        slug_words = slug.split('-')[:6]  # First 6 words
        prefix = '-'.join(slug_words)
        for pdf_file in pdf_files:
            if pdf_file.startswith(prefix):
                return os.path.join(pdfs_dir, pdf_file)
    except Exception:
        pass

    return ""


# ============================================================
# PASS 1: Deep Paper Extraction
# ============================================================

PAPER_SYSTEM_PROMPT = """You are a senior research engineer extracting implementable knowledge from academic papers. Your audience is software engineers who need to BUILD things based on this research.

You MUST respond with valid JSON only. No markdown, no explanation.

Extract EVERYTHING an engineer needs to evaluate and implement this paper's approach:

{
  "summary": "2-3 sentences. What did they build/prove and why should an engineer care?",
  "key_contribution": "One sentence: the single most important technical contribution.",

  "problem_type": "What class of problem does this solve? Use standard CS terminology. Examples: 'multi-objective optimization', 'sequence classification', 'object detection', 'anomaly detection', 'task scheduling', 'code generation', 'malware detection'. Be specific.",
  "problem_description": "One sentence: what real-world problem motivated this work?",

  "domain": "Primary domain: Machine Learning & AI, Computer Vision, Natural Language Processing, Robotics & Control Systems, Software Engineering, Data Structures & Algorithms, Cybersecurity, Networking & Distributed Systems, Bioinformatics & Health, Optimization & Operations Research, Signal Processing & IoT, Human-Computer Interaction, Quantum Computing, Other",
  "sub_domain": "Specific sub-field (e.g., 'Transformer architectures', 'Container orchestration')",

  "technique_name": "The main technique/algorithm proposed or used. Use canonical name if it exists (e.g., 'NSGA-II', 'BERT', 'Random Forest'). If novel, give the paper's name for it.",
  "technique_category": "Broad category: optimization_algorithm, neural_architecture, statistical_method, data_structure, search_algorithm, scheduling_algorithm, classification_model, detection_system, framework, protocol, other",
  "technique_type": "novel (new method), adaptation (existing method applied to new domain), comparison (survey/benchmark), hybrid (combines existing methods)",

  "method": {
    "approach": "2-3 sentences: How does the method work at a high level?",
    "algorithm_steps": ["Step-by-step algorithm in plain English, like pseudocode. 3-8 steps."],
    "input": "What data/format goes in?",
    "output": "What comes out?",
    "key_parameters": ["List tunable parameters with typical values, e.g., 'learning_rate: 0.001', 'population_size: 100'"],
    "complexity": "Time and space complexity if inferrable, e.g., 'O(n² log n) time, O(n) space'. Say 'not stated' if unclear."
  },

  "benchmarks": {
    "datasets": ["What data was it tested on?"],
    "metrics": ["What was measured? Include values if stated, e.g., 'accuracy: 94.2%', 'F1: 0.87'"],
    "baselines": ["What was it compared against?"],
    "improvement": "How much better than baselines? e.g., '15% improvement over standard GA'"
  },

  "concepts": ["4-8 key technical concepts, 1-4 words each"],

  "use_this_when": ["2-4 specific scenarios where an engineer should reach for this approach"],
  "dont_use_when": ["1-3 scenarios where this approach is a bad fit"],

  "implementation_guide": {
    "data_structures": ["Key data structures needed"],
    "dependencies": ["Libraries, frameworks, or tools needed"],
    "pseudocode_hint": "1-3 lines of pseudocode showing the core operation. Use Python-like syntax.",
    "gotchas": ["2-4 common pitfalls or things to watch out for"]
  },

  "connects_to": ["3-6 related techniques, algorithms, or concepts this links to. Include both prerequisites and extensions."],
  "prerequisites": ["2-4 concepts someone should understand first"],
  "limitations": ["2-4 limitations or constraints of this approach"],
  "open_questions": ["1-2 unsolved problems or future work directions"]
}"""


def extract_paper_knowledge(client: OpenAI, paper: dict, model: str = "gpt-4o",
                            pdf_text: str = "") -> dict:
    """Pass 1: Extract deep structured knowledge from a paper.

    If pdf_text is provided, includes the full paper text for richer extraction.
    Falls back to abstract-only when no PDF is available.
    """
    title = paper.get("title", "")
    abstract = paper.get("abstract", "")
    authors = ", ".join((paper.get("authors") or [])[:5])
    year = paper.get("metadata", {}).get("year", "")
    citations = paper.get("metadata", {}).get("citation_count", 0)

    if pdf_text:
        user_prompt = f"""Paper Title: {title}
Authors: {authors}
Year: {year}
Citations: {citations or 'unknown'}

Abstract:
{abstract}

Full Paper Text (first ~30k chars):
{pdf_text}

You have the FULL PAPER TEXT above. Extract deep implementable knowledge including specific algorithm details, equations, parameter values, and benchmark numbers directly from the paper. Respond with JSON only."""
    else:
        user_prompt = f"""Paper Title: {title}
Authors: {authors}
Year: {year}
Citations: {citations or 'unknown'}

Abstract:
{abstract}

Extract deep implementable knowledge. Respond with JSON only."""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": PAPER_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
            max_tokens=3000 if pdf_text else 2000,
            response_format={"type": "json_object"},
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"  [ERROR] Extraction failed for '{title[:50]}': {e}")
        return None


def paper_to_markdown(paper: dict, k: dict) -> str:
    """Render a paper card as markdown."""
    title = paper.get("title", "Untitled")
    doi = paper.get("identifiers", {}).get("doi", "")
    doi_url = paper.get("identifiers", {}).get("doi_url", "")
    s2_id = paper.get("identifiers", {}).get("semantic_scholar_id", "")
    year = paper.get("metadata", {}).get("year", "")
    citations = paper.get("metadata", {}).get("citation_count", 0)
    authors = paper.get("authors", [])
    abstract = paper.get("abstract", "")
    paper_id = paper.get("id", "")
    sources = paper.get("sources", [])

    lines = [f"# {title}\n"]

    # Access block - DOIs front and center
    lines.append("## Access\n")
    lines.append("| Field | Value |")
    lines.append("|-------|-------|")
    if doi:
        lines.append(f"| DOI | `{doi}` |")
    if doi_url:
        lines.append(f"| Full Paper | [{doi_url}]({doi_url}) |")
    if s2_id:
        s2_url = f"https://www.semanticscholar.org/paper/{s2_id}"
        lines.append(f"| Semantic Scholar | [{s2_url}]({s2_url}) |")
    for s in sources:
        if s.get("url"):
            lines.append(f"| Source | [{s['url']}]({s['url']}) |")
    lines.append(f"| Year | {year or 'unknown'} |")
    lines.append(f"| Citations | {citations or 0} |")
    lines.append(f"| Authors | {', '.join(authors[:6])} |")
    lines.append(f"| Paper ID | `{paper_id}` |")
    lines.append("")

    # Classification
    lines.append("## Classification\n")
    lines.append(f"- **Problem Type:** {k.get('problem_type', 'unknown')}")
    lines.append(f"- **Domain:** {k.get('domain', 'unknown')}")
    lines.append(f"- **Sub-domain:** {k.get('sub_domain', '')}")
    lines.append(f"- **Technique:** {k.get('technique_name', 'unknown')}")
    lines.append(f"- **Technique Category:** {k.get('technique_category', '')}")
    lines.append(f"- **Type:** {k.get('technique_type', '')}")
    lines.append("")

    # Summary
    if k.get("summary"):
        lines.append("## Summary\n")
        lines.append(k["summary"])
        lines.append("")

    if k.get("key_contribution"):
        lines.append("## Key Contribution\n")
        lines.append(f"**{k['key_contribution']}**")
        lines.append("")

    if k.get("problem_description"):
        lines.append("## Problem\n")
        lines.append(k["problem_description"])
        lines.append("")

    # Method - the core value
    method = k.get("method", {})
    if method:
        lines.append("## Method\n")
        if method.get("approach"):
            lines.append(f"**Approach:** {method['approach']}\n")
        if method.get("algorithm_steps"):
            lines.append("**Algorithm:**\n")
            for i, step in enumerate(method["algorithm_steps"], 1):
                lines.append(f"{i}. {step}")
            lines.append("")
        if method.get("input"):
            lines.append(f"**Input:** {method['input']}\n")
        if method.get("output"):
            lines.append(f"**Output:** {method['output']}\n")
        if method.get("key_parameters"):
            lines.append("**Key Parameters:**\n")
            for p in method["key_parameters"]:
                lines.append(f"- `{p}`")
            lines.append("")
        if method.get("complexity"):
            lines.append(f"**Complexity:** {method['complexity']}\n")

    # Benchmarks
    bench = k.get("benchmarks", {})
    if bench and any(bench.values()):
        lines.append("## Benchmarks\n")
        if bench.get("datasets"):
            lines.append(f"**Tested on:** {', '.join(bench['datasets'])}\n")
        if bench.get("metrics"):
            lines.append("**Results:**\n")
            for m in bench["metrics"]:
                lines.append(f"- {m}")
            lines.append("")
        if bench.get("baselines"):
            lines.append(f"**Compared against:** {', '.join(bench['baselines'])}\n")
        if bench.get("improvement"):
            lines.append(f"**Improvement:** {bench['improvement']}\n")

    # Implementation guide
    impl = k.get("implementation_guide", {})
    if impl:
        lines.append("## Implementation Guide\n")
        if impl.get("data_structures"):
            lines.append(f"**Data Structures:** {', '.join(impl['data_structures'])}\n")
        if impl.get("dependencies"):
            lines.append(f"**Dependencies:** {', '.join(impl['dependencies'])}\n")
        if impl.get("pseudocode_hint"):
            lines.append("**Core Operation:**\n")
            lines.append(f"```python\n{impl['pseudocode_hint']}\n```\n")
        if impl.get("gotchas"):
            lines.append("**Watch Out For:**\n")
            for g in impl["gotchas"]:
                lines.append(f"- {g}")
            lines.append("")

    # When to use / not use
    if k.get("use_this_when"):
        lines.append("## Use This When\n")
        for s in k["use_this_when"]:
            lines.append(f"- {s}")
        lines.append("")

    if k.get("dont_use_when"):
        lines.append("## Don't Use When\n")
        for s in k["dont_use_when"]:
            lines.append(f"- {s}")
        lines.append("")

    # Concepts and connections
    if k.get("concepts"):
        lines.append("## Key Concepts\n")
        lines.append(", ".join(k["concepts"]))
        lines.append("")

    if k.get("connects_to"):
        lines.append("## Connects To\n")
        for c in k["connects_to"]:
            lines.append(f"- {c}")
        lines.append("")

    if k.get("prerequisites"):
        lines.append("## Prerequisites\n")
        for p in k["prerequisites"]:
            lines.append(f"- {p}")
        lines.append("")

    if k.get("limitations"):
        lines.append("## Limitations\n")
        for lim in k["limitations"]:
            lines.append(f"- {lim}")
        lines.append("")

    if k.get("open_questions"):
        lines.append("## Open Questions\n")
        for q in k["open_questions"]:
            lines.append(f"- {q}")
        lines.append("")

    # Full abstract
    if abstract:
        lines.append("## Abstract\n")
        lines.append(abstract)
        lines.append("")

    return "\n".join(lines)


# ============================================================
# PASS 2: Generate Technique Cards
# ============================================================

TECHNIQUE_SYSTEM_PROMPT = """You are synthesizing knowledge from multiple academic papers into a single TECHNIQUE REFERENCE CARD for software engineers.

Given a technique name and summaries from papers that use/describe it, produce a definitive reference card.

Respond with valid JSON only:

{
  "technique_name": "Canonical name of the technique",
  "aliases": ["Other names this is known by"],
  "category": "optimization_algorithm, neural_architecture, statistical_method, etc.",
  "one_liner": "One sentence: what this technique does.",

  "how_it_works": "3-5 sentence explanation a senior engineer would understand. No unnecessary jargon.",

  "algorithm": {
    "steps": ["Step-by-step algorithm, 4-10 steps, in plain English pseudocode"],
    "core_equation": "The key equation or operation in LaTeX-free notation (e.g., 'output = softmax(Q·K^T / sqrt(d)) · V')",
    "input_format": "What goes in (data types, shapes)",
    "output_format": "What comes out"
  },

  "parameters": [
    {"name": "param_name", "typical_value": "value or range", "effect": "what happens when you change it"}
  ],

  "complexity": {
    "time": "Big-O time complexity",
    "space": "Big-O space complexity",
    "practical_note": "Real-world performance note"
  },

  "use_when": ["3-5 specific scenarios"],
  "avoid_when": ["2-3 anti-patterns"],

  "implementation_skeleton": "10-20 lines of Python pseudocode showing the core implementation. Include type hints.",

  "common_mistakes": ["3-5 pitfalls engineers hit when implementing this"],

  "tradeoffs": {
    "strengths": ["3-4 strengths"],
    "weaknesses": ["3-4 weaknesses"],
    "compared_to": [{"technique": "name", "verdict": "when to use one vs the other"}]
  },

  "connects_to": ["4-8 related techniques (prerequisites, extensions, alternatives)"],

  "maturity": "established (textbook), proven (widely used in production), emerging (recent research), experimental (limited validation)"
}"""


def generate_technique_card(client: OpenAI, technique_name: str,
                            paper_summaries: list, model: str = "gpt-4o") -> dict:
    """Pass 2: Synthesize papers into a technique reference card."""
    papers_text = ""
    for ps in paper_summaries[:8]:  # Limit context
        papers_text += f"\n---\nPaper: {ps['title']}\n"
        papers_text += f"Citations: {ps.get('citations', 0)}\n"
        papers_text += f"Method: {json.dumps(ps.get('method', {}), indent=2)}\n"
        papers_text += f"Benchmarks: {json.dumps(ps.get('benchmarks', {}), indent=2)}\n"
        papers_text += f"Use when: {ps.get('use_this_when', [])}\n"
        papers_text += f"Don't use when: {ps.get('dont_use_when', [])}\n"

    user_prompt = f"""Technique: {technique_name}
Number of papers covering this technique: {len(paper_summaries)}

Paper summaries:
{papers_text}

Synthesize these papers into a single definitive technique reference card. Respond with JSON only."""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": TECHNIQUE_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
            max_tokens=2500,
            response_format={"type": "json_object"},
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"  [ERROR] Technique card failed for '{technique_name}': {e}")
        return None


def technique_to_markdown(tech: dict, citing_papers: list) -> str:
    """Render a technique card as markdown."""
    name = tech.get("technique_name", "Unknown")
    lines = [f"# {name}\n"]

    if tech.get("aliases"):
        lines.append(f"*Also known as: {', '.join(tech['aliases'])}*\n")

    if tech.get("one_liner"):
        lines.append(f"**{tech['one_liner']}**\n")

    lines.append(f"**Category:** {tech.get('category', 'unknown')}  ")
    lines.append(f"**Maturity:** {tech.get('maturity', 'unknown')}\n")

    # How it works
    if tech.get("how_it_works"):
        lines.append("## How It Works\n")
        lines.append(tech["how_it_works"])
        lines.append("")

    # Algorithm
    alg = tech.get("algorithm", {})
    if alg:
        lines.append("## Algorithm\n")
        if alg.get("input_format"):
            lines.append(f"**Input:** {alg['input_format']}\n")
        if alg.get("output_format"):
            lines.append(f"**Output:** {alg['output_format']}\n")
        if alg.get("steps"):
            lines.append("**Steps:**\n")
            for i, step in enumerate(alg["steps"], 1):
                lines.append(f"{i}. {step}")
            lines.append("")
        if alg.get("core_equation"):
            lines.append(f"**Core Operation:** `{alg['core_equation']}`\n")

    # Parameters
    params = tech.get("parameters", [])
    if params:
        lines.append("## Parameters\n")
        lines.append("| Parameter | Typical Value | Effect |")
        lines.append("|-----------|--------------|--------|")
        for p in params:
            lines.append(f"| `{p.get('name', '')}` | {p.get('typical_value', '')} | {p.get('effect', '')} |")
        lines.append("")

    # Complexity
    comp = tech.get("complexity", {})
    if comp:
        lines.append("## Complexity\n")
        if comp.get("time"):
            lines.append(f"- **Time:** {comp['time']}")
        if comp.get("space"):
            lines.append(f"- **Space:** {comp['space']}")
        if comp.get("practical_note"):
            lines.append(f"- **In practice:** {comp['practical_note']}")
        lines.append("")

    # Implementation skeleton
    if tech.get("implementation_skeleton"):
        lines.append("## Implementation\n")
        lines.append(f"```python\n{tech['implementation_skeleton']}\n```\n")

    # Common mistakes
    if tech.get("common_mistakes"):
        lines.append("## Common Mistakes\n")
        for m in tech["common_mistakes"]:
            lines.append(f"- {m}")
        lines.append("")

    # When to use / avoid
    if tech.get("use_when"):
        lines.append("## Use When\n")
        for s in tech["use_when"]:
            lines.append(f"- {s}")
        lines.append("")

    if tech.get("avoid_when"):
        lines.append("## Avoid When\n")
        for s in tech["avoid_when"]:
            lines.append(f"- {s}")
        lines.append("")

    # Tradeoffs
    tradeoffs = tech.get("tradeoffs", {})
    if tradeoffs:
        lines.append("## Tradeoffs\n")
        if tradeoffs.get("strengths"):
            lines.append("**Strengths:**\n")
            for s in tradeoffs["strengths"]:
                lines.append(f"- {s}")
            lines.append("")
        if tradeoffs.get("weaknesses"):
            lines.append("**Weaknesses:**\n")
            for w in tradeoffs["weaknesses"]:
                lines.append(f"- {w}")
            lines.append("")
        if tradeoffs.get("compared_to"):
            lines.append("**Compared To:**\n")
            for c in tradeoffs["compared_to"]:
                lines.append(f"- **vs {c.get('technique', '')}:** {c.get('verdict', '')}")
            lines.append("")

    # Connections
    if tech.get("connects_to"):
        lines.append("## Connects To\n")
        for c in tech["connects_to"]:
            lines.append(f"- {c}")
        lines.append("")

    # Citing papers (evidence)
    if citing_papers:
        lines.append("## Evidence (Papers)\n")
        for p in citing_papers:
            doi_link = f" - [DOI]({p['doi_url']})" if p.get("doi_url") else ""
            cite_str = f" [{p.get('citations', 0)} citations]" if p.get("citations") else ""
            lines.append(f"- **{p['title']}**{cite_str}{doi_link}")
        lines.append("")

    return "\n".join(lines)


# ============================================================
# PASS 3: Generate Problem Entry Points
# ============================================================

PROBLEM_SYSTEM_PROMPT = """You are creating a PROBLEM ENTRY POINT document for software engineers. Given a problem type and the techniques that have been applied to it (with evidence from papers), create a decision guide.

Respond with valid JSON only:

{
  "problem_name": "Canonical name for this problem type",
  "description": "2-3 sentences explaining the problem in plain English.",
  "you_have_this_if": ["3-5 indicators that an engineer has this type of problem"],

  "approaches": [
    {
      "technique": "technique name",
      "best_for": "when this approach is the best choice",
      "paper_count": 0,
      "max_citations": 0,
      "key_tradeoff": "one-sentence tradeoff summary"
    }
  ],

  "decision_matrix": [
    {
      "technique": "name",
      "speed": "fast/medium/slow",
      "memory": "low/medium/high",
      "accuracy": "low/medium/high",
      "ease_of_implementation": "easy/medium/hard",
      "best_when": "one-sentence scenario"
    }
  ],

  "start_here": "The recommended first approach for most cases, with reasoning.",
  "related_problems": ["2-4 related problem types to also consider"]
}"""


def generate_problem_card(client: OpenAI, problem_type: str,
                          technique_summaries: list, model: str = "gpt-4o") -> dict:
    """Pass 3: Generate a problem entry point with decision matrix."""
    tech_text = ""
    for ts in technique_summaries[:10]:
        tech_text += f"\n---\nTechnique: {ts['technique_name']}\n"
        tech_text += f"Papers: {ts['paper_count']}\n"
        tech_text += f"Max citations: {ts.get('max_citations', 0)}\n"
        tech_text += f"Use when: {ts.get('use_when', [])}\n"
        tech_text += f"Category: {ts.get('category', '')}\n"

    user_prompt = f"""Problem Type: {problem_type}
Number of techniques applied to this problem: {len(technique_summaries)}

Techniques:
{tech_text}

Create a problem entry point with decision matrix. Respond with JSON only."""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": PROBLEM_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
            max_tokens=2000,
            response_format={"type": "json_object"},
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"  [ERROR] Problem card failed for '{problem_type}': {e}")
        return None


def problem_to_markdown(prob: dict, techniques: list) -> str:
    """Render a problem entry point as markdown."""
    name = prob.get("problem_name", "Unknown Problem")
    lines = [f"# Problem: {name}\n"]

    if prob.get("description"):
        lines.append(prob["description"])
        lines.append("")

    if prob.get("you_have_this_if"):
        lines.append("## You Have This Problem If\n")
        for indicator in prob["you_have_this_if"]:
            lines.append(f"- {indicator}")
        lines.append("")

    if prob.get("start_here"):
        lines.append("## Start Here\n")
        lines.append(f"**{prob['start_here']}**")
        lines.append("")

    # Decision matrix
    dm = prob.get("decision_matrix", [])
    if dm:
        lines.append("## Decision Matrix\n")
        lines.append("| Technique | Speed | Memory | Accuracy | Ease | Best When |")
        lines.append("|-----------|-------|--------|----------|------|-----------|")
        for row in dm:
            lines.append(
                f"| **{row.get('technique', '')}** "
                f"| {row.get('speed', '')} "
                f"| {row.get('memory', '')} "
                f"| {row.get('accuracy', '')} "
                f"| {row.get('ease_of_implementation', '')} "
                f"| {row.get('best_when', '')} |"
            )
        lines.append("")

    # Approaches detail
    approaches = prob.get("approaches", [])
    if approaches:
        lines.append("## Approaches\n")
        for a in approaches:
            lines.append(f"### {a.get('technique', 'Unknown')}\n")
            if a.get("best_for"):
                lines.append(f"**Best for:** {a['best_for']}\n")
            if a.get("key_tradeoff"):
                lines.append(f"**Tradeoff:** {a['key_tradeoff']}\n")
            lines.append(f"*{a.get('paper_count', 0)} papers, up to {a.get('max_citations', 0)} citations*\n")

    if prob.get("related_problems"):
        lines.append("## Related Problems\n")
        for rp in prob["related_problems"]:
            lines.append(f"- {rp}")
        lines.append("")

    return "\n".join(lines)


# ============================================================
# PASS 4: Cross-Domain Connection Map
# ============================================================

def generate_connection_map(all_knowledge: list, output_dir: Path):
    """Pass 4: Find techniques that bridge domains."""
    # Build: technique → set of domains it appears in
    technique_domains = defaultdict(lambda: {"domains": set(), "papers": []})

    for item in all_knowledge:
        k = item.get("knowledge") or {}
        paper = item["paper"]
        tech = k.get("technique_name", "").lower().strip()
        domain = k.get("domain", "Other")
        if tech:
            technique_domains[tech]["domains"].add(domain)
            technique_domains[tech]["papers"].append({
                "title": paper.get("title", ""),
                "domain": domain,
                "doi_url": paper.get("identifiers", {}).get("doi_url", ""),
            })

    # Find cross-domain bridges (technique appears in 2+ domains)
    bridges = {}
    for tech, data in technique_domains.items():
        if len(data["domains"]) >= 2:
            bridges[tech] = {
                "domains": sorted(data["domains"]),
                "papers": data["papers"]
            }

    # Also build concept co-occurrence
    concept_pairs = defaultdict(int)
    for item in all_knowledge:
        k = item.get("knowledge") or {}
        concepts = [c.lower().strip() for c in k.get("concepts", [])]
        for i, c1 in enumerate(concepts):
            for c2 in concepts[i + 1:]:
                pair = tuple(sorted([c1, c2]))
                concept_pairs[pair] += 1

    # Top co-occurring concepts
    top_pairs = sorted(concept_pairs.items(), key=lambda x: x[1], reverse=True)[:50]

    # Write connection map
    lines = ["# Cross-Domain Connections\n"]
    lines.append("Techniques and concepts that bridge multiple research domains. ")
    lines.append("These are high-value connections: a solution proven in one domain ")
    lines.append("may solve your problem in a different domain.\n")

    if bridges:
        lines.append("## Bridging Techniques\n")
        lines.append("These techniques appear across multiple domains:\n")
        for tech, data in sorted(bridges.items(), key=lambda x: len(x[1]["domains"]), reverse=True):
            lines.append(f"### {tech.title()}\n")
            lines.append(f"**Spans {len(data['domains'])} domains:** {', '.join(data['domains'])}\n")
            lines.append("**Evidence:**\n")
            for p in data["papers"][:5]:
                doi_link = f" - [DOI]({p['doi_url']})" if p.get("doi_url") else ""
                lines.append(f"- [{p['domain']}] {p['title']}{doi_link}")
            lines.append("")

    if top_pairs:
        lines.append("## Frequently Co-Occurring Concepts\n")
        lines.append("Concepts that appear together across multiple papers:\n")
        lines.append("| Concept A | Concept B | Papers |")
        lines.append("|-----------|-----------|--------|")
        for (c1, c2), count in top_pairs:
            if count >= 2:
                lines.append(f"| {c1} | {c2} | {count} |")
        lines.append("")

    (output_dir / "connections.md").write_text("\n".join(lines), encoding="utf-8")

    # Machine-readable JSON
    conn_json = {
        "bridges": {k: {"domains": list(v["domains"]), "paper_count": len(v["papers"])}
                    for k, v in bridges.items()},
        "concept_pairs": {f"{c1}|{c2}": count for (c1, c2), count in top_pairs if count >= 2}
    }
    (output_dir / "connections.json").write_text(
        json.dumps(conn_json, indent=2), encoding="utf-8"
    )
    print(f"  Connections: {len(bridges)} bridging techniques, {sum(1 for _, c in top_pairs if c >= 2)} concept pairs")


# ============================================================
# Utility functions
# ============================================================

def sanitize_filename(text: str) -> str:
    """Convert text to a safe filename slug."""
    clean = re.sub(r'[^\w\s-]', '', text.lower())
    clean = re.sub(r'\s+', '-', clean.strip())
    return clean[:80]


# ============================================================
# Main pipeline
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="CodeScholar Knowledge Base Generator")
    parser.add_argument("--library", default=None, help="Path to unified_library.json")
    parser.add_argument("--output", default=None, help="Output directory")
    parser.add_argument("--limit", type=int, default=0, help="Process only N papers")
    parser.add_argument("--skip-existing", action="store_true", help="Skip papers with existing cards")
    parser.add_argument("--model", default="gpt-4o", help="OpenAI model (gpt-4o recommended)")
    parser.add_argument("--delay", type=float, default=0.3, help="Delay between API calls")
    parser.add_argument("--pass", dest="run_pass", type=int, default=0,
                        help="Run only specific pass (1-4). 0 = all passes")
    parser.add_argument("--min-papers-for-technique", type=int, default=1,
                        help="Min papers to generate a technique card (default: 1)")
    parser.add_argument("--min-techniques-for-problem", type=int, default=1,
                        help="Min techniques to generate a problem card (default: 1)")
    parser.add_argument("--pdfs-dir", default="",
                        help="Directory containing PDF files for full-text extraction")
    parser.add_argument("--concurrency", type=int, default=5,
                        help="Number of concurrent API calls (default: 5)")
    args = parser.parse_args()

    # Paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    library_path = Path(args.library) if args.library else repo_root / "data" / "unified_library.json"
    output_root = Path(args.output) if args.output else repo_root / "knowledge"

    papers_dir = output_root / "papers"
    techniques_dir = output_root / "techniques"
    problems_dir = output_root / "problems"
    connections_dir = output_root / "connections"

    for d in [papers_dir, techniques_dir, problems_dir, connections_dir]:
        d.mkdir(parents=True, exist_ok=True)

    # API key
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not set")
        sys.exit(1)
    client = OpenAI(api_key=api_key)

    # Load library
    print(f"Loading library from {library_path}...")
    with open(library_path, encoding="utf-8") as f:
        all_papers = json.load(f)
    print(f"  Loaded {len(all_papers)} papers")
    if args.limit:
        all_papers = all_papers[:args.limit]
        print(f"  Limited to {args.limit} papers")

    run_all = args.run_pass == 0

    # PDF directory
    pdfs_dir = args.pdfs_dir
    if pdfs_dir and os.path.isdir(pdfs_dir):
        pdf_count = len([f for f in os.listdir(pdfs_dir) if f.endswith('.pdf')])
        print(f"  PDF directory: {pdfs_dir} ({pdf_count} PDFs)")
    elif pdfs_dir:
        print(f"  WARNING: PDF directory not found: {pdfs_dir}")
        pdfs_dir = ""

    # ========================================
    # PASS 1: Paper Knowledge Extraction
    # ========================================
    all_knowledge = []

    if run_all or args.run_pass == 1:
        print(f"\n{'='*60}")
        print("PASS 1: Extracting paper knowledge")
        print(f"{'='*60}")
        processed = 0
        skipped = 0
        errors = 0
        pdf_hits = 0

        # First, load existing and build work queue
        work_queue = []
        for i, paper in enumerate(all_papers):
            title = paper.get("title", "Untitled")
            filename = sanitize_filename(title)
            json_path = papers_dir / f"{filename}.json"

            if args.skip_existing and json_path.exists():
                skipped += 1
                with open(json_path, encoding="utf-8") as f:
                    knowledge = json.load(f)
                all_knowledge.append({"paper": paper, "knowledge": knowledge})
                continue

            # Pre-read PDF text (fast, local I/O)
            pdf_text = ""
            if pdfs_dir:
                pdf_path = find_pdf_for_paper(paper, pdfs_dir)
                if pdf_path:
                    pdf_text = extract_pdf_text(pdf_path)
                    if pdf_text:
                        pdf_hits += 1

            work_queue.append((i, paper, filename, pdf_text))

        if skipped:
            print(f"  Skipped {skipped} existing cards")
        print(f"  Processing {len(work_queue)} papers ({pdf_hits} with PDFs) using {args.concurrency} threads...")

        def process_paper(item):
            """Process a single paper - called from thread pool."""
            idx, paper, filename, pdf_text = item
            title = paper.get("title", "Untitled")
            source_tag = "[PDF]" if pdf_text else "[abs]"
            knowledge = extract_paper_knowledge(client, paper, model=args.model, pdf_text=pdf_text)
            return idx, paper, filename, knowledge, source_tag, title

        # Process concurrently
        completed = 0
        total = len(work_queue)
        with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            futures = {executor.submit(process_paper, item): item for item in work_queue}
            for future in as_completed(futures):
                idx, paper, filename, knowledge, source_tag, title = future.result()
                completed += 1

                if knowledge:
                    md_content = paper_to_markdown(paper, knowledge)
                    (papers_dir / f"{filename}.md").write_text(md_content, encoding="utf-8")
                    (papers_dir / f"{filename}.json").write_text(
                        json.dumps(knowledge, indent=2), encoding="utf-8"
                    )
                    all_knowledge.append({"paper": paper, "knowledge": knowledge})
                    processed += 1
                    safe_print(f"  [{completed}/{total}] {source_tag} {title[:55]}...")
                else:
                    errors += 1
                    safe_print(f"  [{completed}/{total}] [ERR] {title[:55]}")

        print(f"\n  Pass 1 complete: {processed} generated ({pdf_hits} from PDFs), {skipped} existing, {errors} errors")

    # Load existing knowledge for passes 2-4 if we skipped pass 1
    if not all_knowledge and (run_all or args.run_pass >= 2):
        print("  Loading existing paper knowledge...")
        for json_file in papers_dir.glob("*.json"):
            with open(json_file, encoding="utf-8") as f:
                knowledge = json.load(f)
            # Find matching paper
            tech_name = knowledge.get("technique_name", "")
            for paper in all_papers:
                fn = sanitize_filename(paper.get("title", ""))
                if fn == json_file.stem:
                    all_knowledge.append({"paper": paper, "knowledge": knowledge})
                    break
        print(f"  Loaded {len(all_knowledge)} paper knowledge cards")

    # ========================================
    # PASS 2: Technique Card Generation
    # ========================================
    technique_data = {}

    if (run_all or args.run_pass == 2) and all_knowledge:
        print(f"\n{'='*60}")
        print("PASS 2: Generating technique cards")
        print(f"{'='*60}")

        # Cluster papers by technique
        technique_clusters = defaultdict(list)
        for item in all_knowledge:
            k = item.get("knowledge") or {}
            tech = k.get("technique_name", "").strip()
            if tech:
                technique_clusters[tech].append({
                    "title": item["paper"].get("title", ""),
                    "citations": item["paper"].get("metadata", {}).get("citation_count", 0),
                    "doi_url": item["paper"].get("identifiers", {}).get("doi_url", ""),
                    "method": k.get("method", {}),
                    "benchmarks": k.get("benchmarks", {}),
                    "use_this_when": k.get("use_this_when", []),
                    "dont_use_when": k.get("dont_use_when", []),
                    "problem_type": k.get("problem_type", ""),
                    "domain": k.get("domain", ""),
                })

        # Filter by minimum papers
        eligible = {t: p for t, p in technique_clusters.items()
                    if len(p) >= args.min_papers_for_technique}
        print(f"  {len(eligible)} techniques with >= {args.min_papers_for_technique} paper(s)")

        generated = 0
        for tech_name, papers in eligible.items():
            filename = sanitize_filename(tech_name)
            json_path = techniques_dir / f"{filename}.json"

            if args.skip_existing and json_path.exists():
                with open(json_path, encoding="utf-8") as f:
                    tech_card = json.load(f)
            else:
                safe_print(f"  Generating: {tech_name} ({len(papers)} papers)...")
                tech_card = generate_technique_card(client, tech_name, papers, model=args.model)
                if args.delay > 0:
                    time.sleep(args.delay)

            if tech_card:
                # Save JSON and markdown
                json_path.write_text(json.dumps(tech_card, indent=2), encoding="utf-8")
                md_content = technique_to_markdown(tech_card, papers)
                (techniques_dir / f"{filename}.md").write_text(md_content, encoding="utf-8")
                technique_data[tech_name] = {
                    **tech_card,
                    "paper_count": len(papers),
                    "max_citations": max((p.get("citations") or 0) for p in papers),
                    "problem_types": list(set(p.get("problem_type", "") for p in papers if p.get("problem_type"))),
                    "citing_papers": papers,
                }
                generated += 1

        # Technique index
        lines = ["# Technique Reference\n"]
        lines.append(f"*{len(technique_data)} techniques extracted from {len(all_knowledge)} papers*\n")
        for tech_name in sorted(technique_data.keys()):
            td = technique_data[tech_name]
            slug = sanitize_filename(tech_name)
            one_liner = td.get("one_liner", "")
            lines.append(f"- **[{tech_name}]({slug}.md)** - {one_liner}")
        (techniques_dir / "_index.md").write_text("\n".join(lines), encoding="utf-8")

        print(f"\n  Pass 2 complete: {generated} technique cards")

    # ========================================
    # PASS 3: Problem Entry Points
    # ========================================
    if (run_all or args.run_pass == 3) and all_knowledge:
        print(f"\n{'='*60}")
        print("PASS 3: Generating problem entry points")
        print(f"{'='*60}")

        # Cluster techniques by problem type
        problem_clusters = defaultdict(list)
        for item in all_knowledge:
            k = item.get("knowledge") or {}
            prob = k.get("problem_type", "").strip()
            tech = k.get("technique_name", "").strip()
            if prob and tech:
                # Deduplicate technique per problem
                existing = [t for t in problem_clusters[prob] if t["technique_name"] == tech]
                if existing:
                    existing[0]["paper_count"] += 1
                    existing[0]["max_citations"] = max(
                        existing[0]["max_citations"],
                        item["paper"].get("metadata", {}).get("citation_count", 0) or 0
                    )
                else:
                    problem_clusters[prob].append({
                        "technique_name": tech,
                        "paper_count": 1,
                        "max_citations": item["paper"].get("metadata", {}).get("citation_count", 0) or 0,
                        "use_when": k.get("use_this_when", []),
                        "category": k.get("technique_category", ""),
                    })

        eligible = {p: t for p, t in problem_clusters.items()
                    if len(t) >= args.min_techniques_for_problem}
        print(f"  {len(eligible)} problem types with >= {args.min_techniques_for_problem} technique(s)")

        generated = 0
        for problem_type, techniques in eligible.items():
            filename = sanitize_filename(problem_type)
            json_path = problems_dir / f"{filename}.json"

            if args.skip_existing and json_path.exists():
                continue

            safe_print(f"  Generating: {problem_type} ({len(techniques)} techniques)...")
            prob_card = generate_problem_card(client, problem_type, techniques, model=args.model)

            if prob_card:
                json_path.write_text(json.dumps(prob_card, indent=2), encoding="utf-8")
                md_content = problem_to_markdown(prob_card, techniques)
                (problems_dir / f"{filename}.md").write_text(md_content, encoding="utf-8")
                generated += 1

            if args.delay > 0:
                time.sleep(args.delay)

        # Problem index
        lines = ["# Problem Types\n"]
        lines.append("Start here when you have a problem to solve. Find your problem type,\n")
        lines.append("then see which techniques have been proven to work.\n")
        for prob_type in sorted(eligible.keys()):
            slug = sanitize_filename(prob_type)
            tech_count = len(eligible[prob_type])
            lines.append(f"- **[{prob_type}]({slug}.md)** ({tech_count} techniques)")
        (problems_dir / "_index.md").write_text("\n".join(lines), encoding="utf-8")

        print(f"\n  Pass 3 complete: {generated} problem entry points")

    # ========================================
    # PASS 4: Cross-Domain Connections
    # ========================================
    if (run_all or args.run_pass == 4) and all_knowledge:
        print(f"\n{'='*60}")
        print("PASS 4: Mapping cross-domain connections")
        print(f"{'='*60}")
        generate_connection_map(all_knowledge, connections_dir)

    # ========================================
    # Master README
    # ========================================
    paper_count = len(list(papers_dir.glob("*.md")))
    tech_count = len(list(techniques_dir.glob("*.md"))) - 1  # minus _index.md
    prob_count = len(list(problems_dir.glob("*.md"))) - 1

    readme = f"""# CodeScholar Knowledge Base

A structured research knowledge base designed for AI agent consumption.
{paper_count} papers indexed across techniques, problems, and cross-domain connections.

## How To Use This

### "I have a problem to solve"
Start with **[Problems]({problems_dir.name}/_index.md)** → find your problem type → see proven approaches with decision matrix.

### "I want to understand a technique"
Go to **[Techniques]({techniques_dir.name}/_index.md)** → find the algorithm → get pseudocode, parameters, tradeoffs, and evidence.

### "I found interesting code and want the research behind it"
Search **[Papers]({papers_dir.name}/)** → find papers by concept or domain → follow DOI links to full text.

### "I want to discover unexpected connections"
Check **[Connections]({connections_dir.name}/connections.md)** → find techniques that bridge domains → apply solutions from other fields.

## Structure

```
knowledge/
├── problems/      ← START HERE: "I have this type of problem"
│   └── _index.md     Decision matrices, approach rankings
├── techniques/    ← REFERENCE: "How does this algorithm work?"
│   └── _index.md     Pseudocode, parameters, complexity, tradeoffs
├── papers/        ← EVIDENCE: "Show me the proof"
│   └── {{slug}}.md    DOIs, benchmarks, methodology, access links
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

Last updated: {time.strftime('%Y-%m-%d')}
Model: GPT-4o for knowledge extraction
"""
    (output_root / "README.md").write_text(readme, encoding="utf-8")

    print(f"\n{'='*60}")
    print("Knowledge Base Generation Complete")
    print(f"{'='*60}")
    print(f"Papers:      {paper_count}")
    print(f"Techniques:  {max(tech_count, 0)}")
    print(f"Problems:    {max(prob_count, 0)}")
    print(f"Output:      {output_root}")


if __name__ == "__main__":
    main()
