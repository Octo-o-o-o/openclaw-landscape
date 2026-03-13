> https://github.com/JiangAgentLabs/Agent-Control

# OpenClaw-Agent-Control (1 star)

## Problem & Solution

In multi-Agent operations scenarios, Agent states are scattered across logs and monitoring systems, making it costly to locate and handle issues. This project provides a risk-priority console that centralizes Agent observability and operational control decisions into a single interface, supporting real-time status monitoring, event timeline diagnostics, and one-click Skill deployment.

## Key Features

- **Risk-Priority View** — The main display area prioritizes stalled, blocked, and executing states, reducing MTTD
- **Clear Status Semantics** — Defines 5 standard states (idle, executing, waiting, stalled, blocked) to eliminate status ambiguity
- **Event Timeline** — Visualizes the state evolution of Agents and Sub-agents, supporting retrospective and root cause analysis
- **One-Click Skill Deployment** — Provides the `deploy_with_skill.sh` script to automatically launch the backend (FastAPI) and frontend (Next.js)
- **Lifecycle Management Scripts** — Encapsulates operational tasks including start, stop, restart, status check, and log viewing
- **Bilingual Documentation** — Provides documentation and tutorials in both Chinese and English, reducing onboarding costs for international teams
