> https://github.com/ZiyaZhang/market-sentry

# market-sentry (31 stars)

## Problem & Solution

Investors need to simultaneously monitor multiple asset classes including A-shares, US stocks, and cryptocurrencies. Manually tracking anomalies and generating daily reports is time-consuming and prone to omissions. This Skill provides unified multi-market monitoring with real-time anomaly detection (price thresholds, Z-score statistical anomalies, volume surges), daily briefing generation, and Feishu push notifications. The EvidencePack mechanism ensures data auditability.

## Key Features

- **Multi-Market Support** — A-shares (K-lines, institutional capital flows, volume ratio, announcements, sector data), US stocks (quotes, news, SEC filings), cryptocurrencies (price, volume, on-chain data)
- **Three-Layer Anomaly Detection** — Price threshold (e.g., >2% move in 5 minutes), Z-score statistical anomalies, volume surges
- **Narrative-Style Briefings** — Generates natural language daily reports (similar to research notes) rather than simple data listings
- **Feishu Dual-Mode Push** — Mode A (App bot direct messages), Mode B (Webhook rich interactive cards, recommended)
- **EvidencePack Audit** — Each briefing generates a JSON evidence pack containing all raw API responses to prevent hallucinations
- **Silent Monitoring Mode** — Only pushes alerts on anomalies, stays silent during normal periods to reduce noise

<!-- lastCommit: 2d64c82 -->
