> https://github.com/BlockRunAI/ClawRouter

# ClawRouter (5,352 stars)

## Problem & Solution

OpenClaw sends all requests to the same model, wasting cost by invoking large models even for small tasks. ClawRouter is an Agent-native LLM router that uses a 15-dimension scoring algorithm to route requests to the most suitable model in <1ms, supporting 41+ models and using x402 protocol USDC non-custodial payments (Base/Solana), saving 74-100% in costs.

## Key Features

- **Local Routing Engine** — 15-dimension weighted scoring (complexity/reasoning needs/code generation, etc.), <1ms latency, zero external API calls, 100% local decision-making
- **Four Routing Strategies** — eco (cheapest) / auto (balanced, default) / premium (highest quality) / free (zero cost), switchable via `/model <profile>`
- **41+ Model Support** — Covers SIMPLE/MEDIUM/COMPLEX/REASONING four tiers; eco mode uses nvidia/gpt-oss-120b (free) for SIMPLE tasks
- **Image Generation Integration** — `/imagegen` command supports 5 models (nano-banana/banana-pro/dall-e-3/gpt-image/flux), priced $0.02-$0.10/image
- **x402 Non-Custodial Payments** — USDC Hackathon Agentic Commerce award winner, Base/Solana on-chain micropayments, users hold their own private keys, $5 supports thousands of requests
- **OpenClaw Plugin** — One-click install `curl -fsSL https://blockrun.ai/ClawRouter-update | bash`, automatically replaces the default model with `blockrun/auto`

<!-- lastCommit: 14c83c258cf9dcef8ce497701f45cc337a2c8595 -->
