> https://github.com/NevaMind-AI/memU

# memU (12,811 stars)

## Problem & Solution
Addresses two core problems of 24/7 long-running Agents: context window bloat causing token cost explosion, and passive response modes being unable to proactively understand user intent. memU uses a filesystem-style memory architecture and proactive intent capture to enable Agents to run continuously at low cost, anticipating needs and taking proactive action even before the user issues a command.

## Core Architecture
- **Filesystem-Style Memory** -- Organizes memory as a hierarchical directory structure (preferences/relationships/knowledge/context), supporting navigation, mounting, cross-referencing, and export
- **Proactive Memory Lifecycle** -- The Main Agent handles user queries while the memU Bot monitors input/output in parallel, extracting insights, predicting intent, and executing proactive tasks
- **Continuous Sync Loop** -- Agent <--> memU Bot <--> DB three-way continuous synchronization, with memory updated in real-time and injected into the Agent context
- **Cost Optimization** -- Reduces long-running token costs to approximately 1/10 by caching insights and avoiding redundant LLM calls

## Key Features
- **Proactive Intent Capture** -- Continuously understands user goals, preferences, and context, anticipating needs without explicit instructions
- **Proactive Task Execution** -- Information recommendations (suggesting papers based on reading history), email management (auto-drafting replies and flagging priorities)
- **memU Bot** -- Enterprise-grade OpenClaw alternative, one-click installation (< 3 minutes), open-source and self-hostable
- **Memory as Filesystem** -- Navigate memory like browsing directories, load knowledge sources like mounting disks
- **Portability** -- Memory can be exported, backed up, and migrated, with support for cross-Agent sharing

<!-- lastCommit: 163d050299b77143226e9727f67d4826c9a69f92 -->
