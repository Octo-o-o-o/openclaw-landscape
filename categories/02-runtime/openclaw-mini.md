> https://github.com/voocel/openclaw-mini

# OpenClaw Mini (555 stars)

## Problem & Solution

OpenClaw Mini addresses the pain point of "high learning barrier for OpenClaw architecture." By distilling core designs from 430K lines of code, it provides a minimal implementation (three-layer separation: core layer + extension layer + engineering layer) to help developers understand production-grade Agent system design: dual-loop + EventStream event flow, session persistence (JSONL), context management (pruning + summary compaction), long-term memory, skills system, proactive wake-up, multi-provider adaptation (22+ providers), and more — not just a simple Agent Loop.

## Key Features

- **Three-layer Architecture Separation** — Core layer (Agent Loop/EventStream/Session/Context/Tools/Provider, required for any Agent), Extension layer (Memory/Skills/Heartbeat, OpenClaw-specific), Engineering layer (Session Key/Tool Policy/Command Queue, production-grade safeguards)
- **Dual-loop + EventStream** — Outer loop (follow-up loop, handles end_turn/tool_use continuation) + Inner loop (tool execution + steering injection), returns EventStream (18 typed events, async push-pull)
- **Session Persistence (JSONL)** — Session module manages JSONL history, supporting load, append, and prune operations
- **Context Management Trio** — Loader (on-demand loading of bootstrap files like AGENTS.md), Pruning (three-tier progressive pruning: tool_result -> assistant -> keep recent), Compaction (adaptive chunked summary compression)
- **Long-term Memory + Skills System + Proactive Wake-up** — Memory (keyword retrieval + time decay), Skills (SKILL.md frontmatter + trigger word matching), Heartbeat (wake request merging + runner scheduling)
- **Multi-Provider Adaptation** — Based on pi-ai, supports Anthropic/OpenAI/Google/Groq and 22+ other providers
- **Engineering Layer Safeguards** — Session Key (multi-agent session key normalization), Tool Policy (three-level access control), Command Queue (concurrent lane control), Tool Result Guard (auto-fills missing tool_result), Context Window Guard (context window overflow protection)

<!-- lastCommit: 662d02c -->
