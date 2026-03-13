> https://github.com/unbrowse-ai/unbrowse

# Unbrowse (485 stars)

## Problem & Solution
When Agents access websites, they need to manually write API call code, which is inefficient and hard to reuse. Unbrowse captures browser network traffic to automatically reverse-engineer the real underlying API endpoints of websites, and stores the learned API contracts in a shared marketplace, achieving a "one Agent learns once, all subsequent Agents reuse directly" fast path — 100x faster and 80% cheaper.

## Key Features
- Automatic discovery of website underlying APIs (network traffic capture + reverse engineering)
- Shared marketplace (one Agent learns, all Agents reuse)
- Intent resolution pipeline (route cache -> marketplace search -> live capture -> DOM fallback)
- Skill lifecycle management (active/deprecated/disabled)
- Background validation loop (executes safe GET endpoints every 6 hours, detecting failures and schema drift)
- Local execution (credentials stay local; only learned API contracts are published)

<!-- lastCommit: 6a7050b -->
