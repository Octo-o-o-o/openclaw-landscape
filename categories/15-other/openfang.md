> https://github.com/RightNow-AI/openfang

# OpenFang (13,622 stars)

## Problem & Solution

Traditional Agent frameworks are just Python wrappers around LLMs, requiring users to actively trigger them. OpenFang is an Agent operating system built from scratch in Rust, providing autonomous Agents (Hands) that work 24/7 on schedule — monitoring targets, generating leads, managing social media — with no human intervention required.

## Key Features

- **Hands Autonomous Capability Packs** — 7 pre-built Hands (Clip/Lead/Collector/Predictor/Researcher/Twitter/Browser), each containing a HAND.toml manifest, multi-stage system prompts (500+ word expert workflows), SKILL.md domain knowledge, and approval gates
- **Single Binary Deployment** — 137K LOC Rust code compiled to a ~32MB single file, 1,767+ tests passing, zero clippy warnings, one command launches the complete system
- **Scheduled Autonomous Execution** — Lead Hand automatically discovers potential customers daily, scores, deduplicates, and delivers CSV reports; Collector Hand continuously monitors targets and builds knowledge graphs
- **Safety Approval Mechanism** — Browser Hand requires mandatory human confirmation before any purchase; Twitter Hand queues all tweets for approval
- **FangHub Extension Ecosystem** — Users can define their own HAND.toml and publish to FangHub, similar to Docker Hub for Agent capabilities
- **Cross-Platform Support** — macOS/Linux/Windows one-click install script, Dashboard runs by default on localhost:4200
