> https://github.com/8421bit/MiniClaw

# MiniClaw (63 stars)

## Problem & Solution

Traditional AI Copilots (such as Claude Desktop, Cursor) lack cross-session memory and proactive awareness — each conversation starts from a blank slate. MiniClaw builds a "nervous system" for IDE-based AI copilots via the MCP protocol, giving them workspace awareness, secure execution, cross-session memory, and autonomous evolution capabilities, upgrading them from "chatbots" to "digital life embryos."

## Key Features

- **Zero-Install Deployment** — Run directly via `npx -y github:8421bit/miniclaw` with no need for git clone or manual dependency installation
- **Global Awareness Engine** — Automatically identifies project type, Git status, and tech stack, injecting context (e.g., `Project: my-app | Git: feature/login | Stack: TypeScript, React`)
- **Adaptive Context Engine (ACE)** — Dynamically adjusts persona modes based on time of day and task type (morning briefing, nighttime memory consolidation, minimal mode when coding, full persona mode for casual chat)
- **Emotion State System** — Maintains four-dimensional emotions (alertness/mood/curiosity/confidence) that influence behavior patterns (conservative when high alertness + low mood, exploratory when high curiosity + positive mood)
- **Pain Memory Mechanism** — Learns from failures to form protective instincts (7-day half-life; triggers avoidance behavior when weight exceeds threshold)
- **Proactive Exploration** — Detects repetitive workflows (3+ occurrences) and automatically proposes Skill creation, records new tools to TOOLS.md, senses emotional fluctuations to update user model
