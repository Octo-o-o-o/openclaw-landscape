> https://github.com/zscole/model-hierarchy-skill

# model-hierarchy-skill (331 stars)

## Problem & Solution

AI Agents default to routing all tasks to expensive models (e.g., Claude Opus at $15-75/M tokens), but 80% of tasks are routine operations (file reading, status checks, formatting) that can be handled by cheaper models ($0.14/M tokens). model-hierarchy-skill achieves cost-optimized routing through task complexity classification, reducing costs by approximately 10x while maintaining quality.

## Key Features

- **Three-Tier Model Hierarchy** — ROUTINE (80%, $0.14-0.50/M) / MODERATE (15%, $1-5/M) / COMPLEX (5%, $10-75/M)
- **Task Classification Rules** — File operations/queries/formatting route to cheap models; code generation/summarization route to mid-tier models; debugging/architecture design route to premium models
- **Cross-Platform Adaptation** — Provides OpenClaw SKILL.md, Claude Code/Codex project instructions, and generic Agent system integration examples
- **Cost Estimation Tool** — Monthly cost comparison based on 100K tokens/day (pure Opus $225 vs tiered $19)
- **pytest Test Suite** — `tests/test_classification.py` + `scenarios.json` for validating classification accuracy
- **Sub-Agent Default Strategy** — Recommends sub-Agents default to cheap models, upgrading only when tasks fail

<!-- lastCommit: 9095f8303847a60de9f564659e561f3f6fd0cdc4 -->
