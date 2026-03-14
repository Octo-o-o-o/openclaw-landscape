> https://github.com/kevin-liu-robot/EQtreader

# EQtreader (54 stars)

## Problem & Solution

Quantitative trading systems need to integrate market data retrieval, trade execution, position management, and other modules, with high manual development costs and error-prone processes. This project provides a quantitative trading Skill for OpenClaw based on open-source libraries like easyquotation, easytrader, and easyquant, supporting automated trading via the Tonghuashun client and multi-source market data retrieval.

## Key Features

- **Trading Client Integration** — Connects to the Tonghuashun client (`xiadan.exe`) via easytrader, supporting order placement, position queries, and balance checks
- **Multi-Source Market Data** — Integrates Sina and Tencent market APIs, supporting real-time quotes, top gainers/losers rankings, and block trade data
- **32-Bit Python Compatibility** — Provides Anaconda virtual environment configuration for Tonghuashun client's 32-bit limitation
- **OCR Recognition Support** — Integrates pytesseract and pyperclip for CAPTCHA recognition and clipboard filling
- **Remote Deployment Guide** — Provides remote server deployment considerations (screensaver off, desktop active, code disconnect handling)
- **Data Source Extensions** — Integrates TuShare, Waizao.com, and other third-party data platforms for historical and fundamental data

<!-- lastCommit: 2266016 -->
