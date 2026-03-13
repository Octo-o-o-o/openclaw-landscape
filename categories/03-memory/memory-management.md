> https://github.com/jzOcb/memory-management

# openclaw-memory-management (29 stars)

## Problem & Solution

The more memories an AI Agent accumulates, the "dumber" it gets -- excessive context token consumption leads to slower responses and higher costs. This project, based on @ohxiyu's P0/P1/P2 priority system, uses automatic archiving and tiered memory management to reduce token usage by 78% (from 6,618 to 1,488) while maintaining memory accuracy and accessibility.

## Key Features

- **Three-Tier Priority System** -- P0 (core identity, never expires), P1 (active projects, 90-day TTL), P2 (temporary memories, 30-day TTL)
- **Automatic Archiving Mechanism** -- Cron jobs automatically migrate expired memories to the archive directory, keeping hot memory files lean (<= 200 lines)
- **Structured Lessons Storage** -- Stores lessons learned in JSONL format, supporting semantic search instead of full loading
- **Core Principles Compression** -- Compresses 17 scattered rules into 5 core principles (AGENTS.md), with the rest stored in a searchable lessons library
- **Dry Run Mode** -- Provides `--dry-run` and `--stats` parameters for previewing archiving operations and running statistical analysis
- **Multiple Integration Methods** -- Supports OpenClaw Skill, Claude Code rule files, and other integration approaches

<!-- lastCommit: 6a7050b -->
