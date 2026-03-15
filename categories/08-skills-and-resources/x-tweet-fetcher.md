> https://github.com/ythx-101/x-tweet-fetcher

# ythx-101/x-tweet-fetcher (N/A stars)

## Problem & Solution

X/Twitter has shut down its free API, traditional scrapers are easily blocked, and browser automation solutions are fragile. This project uses a combined approach of zero-dependency HTTP requests (single tweets) + Camofox browser automation (comments/timelines/long-form articles), enabling tweet scraping without login or API keys, outputting structured JSON for direct Agent consumption.

## Key Features

- **Zero-config single tweet fetch** — One command to get tweet text, likes, retweets, views, and media URLs, requiring no dependencies or authentication
- **Advanced features (Camofox)** — Supports comment trees, user timelines (up to 200 tweets), X Articles long-form content, X Lists, and @mentions monitoring
- **Cross-platform content aggregation** — Integrates WeChat Official Account search (via Sogou), Weibo/Bilibili/CSDN scraping, and Google search (zero API key), covering both Chinese and English social media with one tool
- **Agent-friendly design** — All output is structured JSON, supports Python module import, exit codes adapted for cron (0=no new content, 1=new content)
- **User profiling** — Combines LLM analysis of user tweets to generate MBTI, Big Five personality traits, and topic graphs
- **Incremental monitoring mode** — The `--monitor` parameter supports scheduled checking for new @mentions, suitable for automated workflows

<!-- lastCommit: c7fad90 -->
