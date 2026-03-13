> https://github.com/chenmuwen0930/snowtrace

# openclaw-skill-snowtrace (27 stars)

## Problem & Solution

Investors need to manually browse the Xueqiu (Snowball) platform to track KOL updates and watchlist stock quotes, with information scattered and time-consuming to gather. This Skill uses Playwright + stealth to bypass Xueqiu's WAF, automatically scraping top influencer original posts and watchlist real-time quotes, generating five-section investment analysis reports (KOL opinion summary -> Market overview -> Correlation analysis -> Investment recommendations -> Disclaimer).

## Key Features

- **Anti-Crawler Bypass** — Uses Playwright + stealth plugin to bypass Alibaba Cloud WAF, supports main domain dynamic scraping
- **Multi-Market Support** — Supports A-shares, Hong Kong stocks, and US stocks for watchlist management and real-time quote retrieval
- **Portfolio P&L Calculation** — Optional local portfolio configuration (`portfolio.json`) with automatic P&L and return rate calculation
- **Structured Output** — Generates standardized five-section investment analysis reports, easy for Agents to understand and users to read
- **Hybrid Scraping Strategy** — KOL updates and watchlist use browser context (with cookies); individual stock quotes use curl (no WAF)
- **Environment Variable Configuration** — Manages Xueqiu login credentials via the `XQ_A_TOKEN` environment variable, avoiding hardcoding
