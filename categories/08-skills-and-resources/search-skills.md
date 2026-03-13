> https://github.com/blessonism/search-skills

# blessonism/openclaw-search-skills (232 stars)

## Problem & Solution

General-purpose search engines (Google/Bing) cannot meet Agents' deep research needs, lacking precise retrieval capabilities for academic papers, patents, code repositories, and other vertical domains. This project provides 10+ specialized search skills (arXiv, Google Scholar, GitHub, patent databases, etc.), giving Agents multi-source, structured deep search capabilities.

## Key Features

- **Vertical search coverage** — Supports academic papers (arXiv, Google Scholar, PubMed), code repositories (GitHub, GitLab), patents (USPTO, EPO), and technical documentation (Stack Overflow, MDN)
- **Structured output** — Each search result includes title, abstract, authors, citation count, publication date, DOI/URL, and other complete metadata for downstream Agent processing
- **Advanced filtering** — Supports precise filtering by time range, citation count threshold, programming language, license type, and other criteria
- **Batch retrieval** — Supports querying multiple data sources at once with automatic deduplication, sorting, and comprehensive report generation
- **Citation tracking** — Automatically extracts paper citation relationships to build knowledge graphs, supporting "follow-the-thread" deep research
- **OpenClaw native integration** — Each search skill is independently packaged as a SKILL.md and can be installed on demand (e.g., `npx sundial-hub add arxiv-search`)
