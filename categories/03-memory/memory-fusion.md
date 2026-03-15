> https://github.com/dztabel-happy/openclaw-memory-fusion

# openclaw-memory-fusion (120 stars)

## Problem & Solution

OpenClaw's memory capability relies on the model voluntarily writing to memory -- smart models will proactively memorize but most models are inconsistent, and critical context is easily lost after session compaction. memory-fusion uses a three-layer cron (hourly/daily/weekly) for system-level automatic extraction/distillation/consolidation, turning "important conversations into retrievable knowledge" into an operationally manageable process, achieving "never forget."

## Key Features

- **Three-Layer Cron Architecture** -- L1 hourly (micro-sync, 5 times/day), L2 daily (23:30 canonical + A' rolling 7-day window), L3 weekly (00:20 gate, category governance + promotion)
- **Incremental Cursor Mechanism** -- Reads `~/.openclaw/agents/<agent>/sessions/*.jsonl` by byte offset, no loss and no duplication, tolerant of half-line JSON
- **Anti-Recursion Hard Constraint** -- Cron prompts start with `[cron:`, scanner ignores cron sessions and notification text; validation: running hourly repeatedly should converge to `events: 0`
- **High Signal-to-Noise Input** -- Extracts only `role=user` (intent/decisions/preferences) and `role=assistant` (final conclusions), skipping tool calls and tool echoes
- **A' Rolling Zone** -- Daily maintains `MEMORY.md#Recent Important Updates (Rolling 7 Days)` (<= 30 entries), weekly promotes long-term valid content to formal categories
- **Operations-Ready Design** -- Lock mechanism (prevents concurrent overwrites) + weekly gate (at least one success per week) + Telegram notification panel (unified `events/updated/coverage` format)

<!-- lastCommit: 2282706fed1a4a62b037e75079df3ffa12c16715 -->
