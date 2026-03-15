> https://github.com/snarktank/antfarm

# Antfarm (2,104 stars)

## Problem & Solution
Antfarm addresses the complexity of OpenClaw Agent team collaboration. Traditional approaches require manually orchestrating multiple Agents, managing context passing, and tracking state. Antfarm provides a one-click-install multi-Agent workflow framework that uses YAML to define deterministic processes, enabling specialized Agent teams to automatically collaborate on complex tasks.

## Core Architecture
- **Ralph Loop Pattern** — Each Agent runs in an independent session, persisting memory via git history and progress files to avoid context window bloat
- **SQLite + Cron Orchestration** — No Redis/Kafka/container orchestration needed; Agents poll task queues via cron, claim steps, execute, and pass context
- **YAML Workflow Definition** — Declaratively define Agent roles, workspaces, validation criteria, and step dependencies
- **Auto-Retry and Escalation** — Failed steps automatically retry; after retry exhaustion, escalate to human intervention

## Key Features
- **3 Pre-built Workflows** — feature-dev (7 agents), security-audit (7 agents), bug-fix (6 agents)
- **Agent Cross-Verification** — Developers don't self-verify; independent verifiers check acceptance criteria
- **One-Click Install** — `curl | bash` install, auto-configures Agent workspaces, cron tasks, and permissions
- **Web Dashboard** — Real-time monitoring of run status, step progress, and Agent output
- **Security Review Mechanism** — Only installs workflows from the official repo; all community contributions undergo prompt injection review

<!-- lastCommit: a442ad7dcb8cf8746175cc4a2e2dcafd501156cf -->
