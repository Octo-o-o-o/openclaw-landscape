> https://github.com/duxiaoxiong/memu-engine

# memu-engine-for-OpenClaw (46 stars)

## Problem & Solution

OpenClaw's single `memu.db` storage causes multi-Agent memory mixing, ambiguous cross-Agent retrieval rules, and inability to isolate shared documents from private memories. v0.3.1 introduces per-agent memory layout (independent DB per Agent) + explicit shared storage (`memory/shared/memu.db`) + configurable retrieval strategies (`searchableStores`), achieving memory isolation, shared document separation, and explicit cross-Agent retrieval control.

## Key Features

- **Per-Agent Memory Layout** -- Each Agent writes to an independent DB (`memory/<agent>/memu.db`), with default memory isolation to prevent cross-Agent contamination
- **Explicit Shared Storage** -- Shared documents are stored in `memory/shared/memu.db`, with cross-Agent retrieval permissions controlled via `agentSettings.searchableStores`
- **Unified Runtime Layout** -- All data is centralized under `~/.openclaw/memUdata/` (conversations/resources/memory/state) for easy backup, migration, and cleanup
- **Automatic Upgrade Migration** -- Automatically migrates from the v0.2.6 single-DB layout to the v0.3.1 per-agent layout with backup-first behavior
- **MemU Extraction Pipeline** -- Based on the upstream MemU project, extracts profiles/events/knowledge/skills/behavior signals from conversation logs and Markdown documents
- **Zero-Dependency Startup** -- Automatically bootstraps an isolated Python environment (`python/.venv`) via `uv sync`, installing locked dependencies from `python/uv.lock`

<!-- lastCommit: 6a7050b -->
