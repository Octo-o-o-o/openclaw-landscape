> https://github.com/codesfly/openclaw-memory-final

# openclaw-memory-final (94 stars)

## Problem & Solution

Production AI memory systems need to handle incremental updates, deduplication, stability monitoring, and cost control -- pure LLM memory extraction alone is insufficient for 24/7 operation. memory-final provides a production-oriented memory architecture: daily incremental distillation + weekly refinement + idempotent deduplication + watchdog daemon + QMD indexing + context budget control, ensuring memory system reliability and cost manageability.

## Key Features

- **Layered Memory Pipeline** -- Short-term workbench (CURRENT_STATE) + daily incremental distillation (memory/YYYY-MM-DD.md) + weekly refinement (MEMORY.md + weekly report archiving)
- **Sub-Agent Task Card Index** -- Execution results from isolated sessions are written as task cards to `memory/tasks/YYYY-MM-DD.md`, with task card lookup before semantic search
- **Idempotent Capture** -- Message fingerprint cursor (`processed-sessions.json`) to avoid duplicate processing
- **Low-Noise Alerting** -- Alerts only after 2 consecutive anomalies, filtering out sporadic failures
- **Cost-Aware Indexing** -- Daily runs only `qmd update` (BM25), weekly runs `qmd update && qmd embed` (vectorization)
- **Context Budget Control** -- Hard limits on per-file and total injected memory character counts to prevent token overflow
- **Dynamic Profile Injection** -- Loads minimal context packages based on profile (main/ops/btc/quant)
- **Conflict Detection** -- Scans for routing/rule drift before persisting memory changes
- **Retrieval Watchdog + Nightly Maintenance** -- 30-minute health checks + daily 03:20 `qmd update` / conditional `embed`
