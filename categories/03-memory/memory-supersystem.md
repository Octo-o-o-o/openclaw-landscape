> https://github.com/ktao732084/memory-supersystem

# openclaw_memory_supersystem-v1.0 (64 stars)

## Problem & Solution

OpenClaw's MEMORY.md mechanism suffers from a "brute force overload" problem: as conversations grow longer, retrieval returns large volumes of 80%-relevant but useless information, consuming 3,000-8,000 tokens with only 60% precision. Inspired by neuroscience, this project builds a three-layer memory architecture (working memory / long-term memory / event log) + 7-stage consolidation + Fact/Belief/Summary classification, reducing token consumption to < 2,000 (down 60-75%) and improving retrieval precision to 90% (up 50%).

## Key Features

- **Three-Layer Storage Architecture** -- Working memory (SQLite hot storage), long-term memory (JSONL cold storage), event log (raw conversations), simulating the human brain's short-term / long-term memory separation
- **7-Stage Memory Consolidation** -- Noise filtering -> entity recognition -> conflict detection -> memory operations (ADD/UPDATE/DELETE/NOOP) -> confidence scoring -> classification (Fact/Belief/Summary) -> automatic decay
- **Hybrid Retrieval Engine** -- Keyword (BM25) + vector (GGUF local model) + shard indexing + multi-level caching, supporting temporal queries ("what the user mentioned about X last week")
- **Memory Operator** -- 92.9% accuracy CRUD operator with conflict resolution protocol (soft demotion instead of hard deletion) and false memory filtering
- **Temporal Engine** -- TemporalQueryEngine + FactEvolutionTracker + EvidenceTracker for tracking fact evolution and evidence chains
- **QMD Semantic Search Integration** -- Supports `qmd_search` + `router_search` hybrid retrieval, Mini-Consolidate daytime lightweight checks + pending.jsonl buffer

<!-- lastCommit: 6a7050b -->
