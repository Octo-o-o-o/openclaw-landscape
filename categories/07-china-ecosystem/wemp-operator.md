> https://github.com/IanShaw027/wemp-operator

# wemp-operator (54 stars)

## Problem & Solution

Operating a WeChat Official Account requires manual hot topic collection, data analysis, and comment management, involving repetitive labor with low efficiency. wemp-operator automates the entire workflow of content collection, data analysis, and engagement management through 70 WeChat Official Account API integrations + 20+ data sources (Hacker News/V2EX, etc.) + AI-powered smart replies, supporting natural language interaction (e.g., "help me collect today's AI hot topics").

## Key Features

- **Three core workflows** — Content collection (AI expands keywords -> select data sources -> collect hot topics -> filter output), Data analysis (fetch statistics -> calculate metrics -> generate insights -> output reports -> push notifications), Engagement management (check comments -> AI generates reply suggestions -> user confirms -> execute reply/feature)
- **70 API integrations** — Complete coverage of WeChat Official Account APIs with no additional dependencies (material management, user management, message management, data statistics, etc.)
- **20+ data sources** — Supports hot topic collection from tech communities including Hacker News, V2EX, GitHub Trending, Reddit, Product Hunt, and more
- **Natural language triggers** — Through the OpenClaw Skill mechanism, users simply say "generate the official account daily report" to trigger, no need to memorize commands
- **AI-powered smart replies** — Automatically detects new comments and generates reply suggestions; users confirm before execution (supports batch featuring)
- **ClawHub one-click install** — `openclaw skill install IanShaw027/wemp-operator` for deployment; configuration requires only AppID/AppSecret

<!-- lastCommit: 7574534715edf5423b258beb12a2dc63372f8c2a -->
