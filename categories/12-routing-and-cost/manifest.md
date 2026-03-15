> https://github.com/mnfst/manifest

# Manifest (3,733 stars)

## Problem & Solution

OpenClaw sends all requests to the same model, wasting cost by invoking large models even for small tasks. Manifest is an OpenClaw plugin that uses a 23-dimension scoring algorithm to route requests to the most suitable model in <2ms, saving up to 70% in costs. It offers both Cloud and Local deployment modes — Local mode keeps all data on-device, while Cloud mode only transmits OpenTelemetry metadata (no message content).

## Key Features

- **23-Dimension Routing Algorithm** — Evaluates requests and routes to the most suitable model in <2ms, more granular than ClawRouter's 15 dimensions
- **Cloud/Local Dual Mode** — Cloud mode provides cross-device dashboard access + multi-Agent connectivity; Local mode stores data entirely locally (http://127.0.0.1:2099)
- **OTLP Native Support** — Standard OpenTelemetry ingestion (traces/metrics/logs), integrable with existing observability stacks
- **Zero-Code Installation** — OpenClaw plugin one-click install, no code modifications needed, automatically intercepts requests and routes them
- **Privacy-First Architecture** — Cloud mode's blind proxy is physically unable to read prompts (fundamentally different from "trust us" services); Local mode data never leaves the device
- **Anonymous Product Analytics** — Only collects hashed machine ID, OS platform, package version, and event name; can be disabled via `MANIFEST_TELEMETRY_OPTOUT=1` or config file

<!-- lastCommit: 1820c5f6bc0462c12fcfa3dac2660795fdabc093 -->
