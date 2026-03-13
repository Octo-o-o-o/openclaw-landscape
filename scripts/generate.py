#!/usr/bin/env python3
"""Generate all Markdown files from data/projects.json.

Usage:
    python scripts/generate.py
"""

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "projects.json"
CATEGORIES_DIR = ROOT / "categories"

CATEGORY_ORDER = [
    "official",
    "runtime",
    "memory",
    "security",
    "dashboard-and-monitoring",
    "deployment",
    "china-ecosystem",
    "skills-and-resources",
    "protocols",
    "ops",
    "voice",
    "routing-and-cost",
    "orchestration",
    "clients",
    "other",
]

CATEGORY_META = {
    "official": {
        "name_en": "Official",
        "name_zh": "官方项目",
        "desc_en": "Projects maintained by the OpenClaw organization.",
        "desc_zh": "OpenClaw 官方组织维护的项目。",
        "emoji": "",
    },
    "runtime": {
        "name_en": "Alternative Runtimes",
        "name_zh": "替代实现 / 运行时",
        "desc_en": "Alternative implementations and runtimes compatible with the OpenClaw ecosystem.",
        "desc_zh": "与 OpenClaw 生态兼容的替代实现和运行时。",
        "emoji": "",
    },
    "memory": {
        "name_en": "Memory Systems",
        "name_zh": "记忆系统",
        "desc_en": "Memory management, persistence, and retrieval systems for AI agents.",
        "desc_zh": "AI Agent 的记忆管理、持久化和检索系统。",
        "emoji": "",
    },
    "security": {
        "name_en": "Security Tools",
        "name_zh": "安全工具",
        "desc_en": "Security scanning, auditing, and hardening tools for agent deployments.",
        "desc_zh": "Agent 部署的安全扫描、审计和加固工具。",
        "emoji": "",
    },
    "dashboard-and-monitoring": {
        "name_en": "Dashboards & Monitoring",
        "name_zh": "仪表板 / 监控",
        "desc_en": "Web dashboards, monitoring tools, and observability platforms.",
        "desc_zh": "Web 仪表板、监控工具和可观测性平台。",
        "emoji": "",
    },
    "deployment": {
        "name_en": "Deployment Tools",
        "name_zh": "部署工具",
        "desc_en": "Docker, Helm, installers, and other deployment solutions.",
        "desc_zh": "Docker、Helm、安装程序及其他部署方案。",
        "emoji": "",
    },
    "china-ecosystem": {
        "name_en": "China Ecosystem",
        "name_zh": "中国生态",
        "desc_en": "Chinese-language resources, IM integrations (Feishu, DingTalk, WeChat), and localized tools.",
        "desc_zh": "中文资源、IM 集成（飞书、钉钉、企业微信）及本地化工具。",
        "emoji": "",
    },
    "skills-and-resources": {
        "name_en": "Skills & Resources",
        "name_zh": "技能 / 模板 / 资源",
        "desc_en": "Curated skill collections, templates, tutorials, and community resources.",
        "desc_zh": "技能集合、模板、教程及社区资源。",
        "emoji": "",
    },
    "protocols": {
        "name_en": "Protocols (A2A / MCP / ACP)",
        "name_zh": "协议（A2A / MCP / ACP）",
        "desc_en": "Agent-to-Agent, Model Context Protocol, and Agent Communication Protocol implementations.",
        "desc_zh": "Agent 间通信、模型上下文协议和 Agent 通信协议的实现。",
        "emoji": "",
    },
    "ops": {
        "name_en": "Ops Tools",
        "name_zh": "运维工具",
        "desc_en": "Backup, health monitoring, runbook automation, and operational tooling.",
        "desc_zh": "备份、健康监控、运维手册自动化及运维工具。",
        "emoji": "",
    },
    "voice": {
        "name_en": "Voice",
        "name_zh": "语音",
        "desc_en": "Voice interfaces and speech integration for agents.",
        "desc_zh": "Agent 的语音接口和语音集成。",
        "emoji": "",
    },
    "routing-and-cost": {
        "name_en": "LLM Routing & Cost Optimization",
        "name_zh": "LLM 路由 / 成本优化",
        "desc_en": "Smart model routing, token optimization, and cost management.",
        "desc_zh": "智能模型路由、Token 优化和成本管理。",
        "emoji": "",
    },
    "orchestration": {
        "name_en": "Multi-Agent Orchestration",
        "name_zh": "多 Agent 编排",
        "desc_en": "Frameworks for coordinating multiple agents, workflows, and agent teams.",
        "desc_zh": "多 Agent 协调、工作流和 Agent 团队编排框架。",
        "emoji": "",
    },
    "clients": {
        "name_en": "Desktop & Mobile Clients",
        "name_zh": "桌面 / 移动客户端",
        "desc_en": "Desktop apps, mobile apps, and terminal clients.",
        "desc_zh": "桌面应用、移动应用和终端客户端。",
        "emoji": "",
    },
    "other": {
        "name_en": "Other",
        "name_zh": "其他",
        "desc_en": "Projects that don't fit neatly into other categories.",
        "desc_zh": "未归入其他分类的项目。",
        "emoji": "",
    },
}


def format_stars(n: int) -> str:
    if n >= 1000:
        return f"{n / 1000:.1f}k".rstrip("0").rstrip(".")  + "k" if n < 10000 else f"{n / 1000:.0f}k"
    return str(n)


def format_stars_display(n: int) -> str:
    """Format with comma separators."""
    return f"{n:,}"


def generate_category_page(cat: str, projects: list[dict]) -> str:
    meta = CATEGORY_META[cat]
    lines = [
        f"# {meta['name_en']}",
        "",
        f"> {meta['desc_en']}",
        f"> {meta['desc_zh']}",
        "",
        f"**{len(projects)} projects** | [Back to overview](../README.md)",
        "",
        "---",
        "",
    ]

    for p in projects:
        stars = format_stars_display(p["stars"])
        meta_parts = [f"Stars: {stars}"]
        if p.get("language"):
            meta_parts.append(p["language"])
        if p.get("license"):
            meta_parts.append(p["license"])

        lines.append(f"### {p['name']}")
        lines.append("")
        lines.append(f"[{p['repo']}](https://github.com/{p['repo']}) | {' | '.join(meta_parts)}")
        lines.append(f"Researched: {p['last_researched']} | Updated: {p['last_updated']}")
        lines.append("")

        if p.get("description"):
            lines.append(p["description"])
            lines.append("")

        if p.get("features"):
            lines.append(f"**Features:** {', '.join(p['features'])}")
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def generate_readme(projects: list[dict]) -> str:
    total = len(projects)
    cats_count = {}
    for p in projects:
        cats_count[p["category"]] = cats_count.get(p["category"], 0) + 1

    total_stars = sum(p["stars"] for p in projects)

    lines = [
        "# OpenClaw Landscape",
        "",
        f"A structured directory of **{total} projects** across **{len(CATEGORY_ORDER)} categories** in the OpenClaw ecosystem.",
        "",
        f"Total stars tracked: **{format_stars_display(total_stars)}**",
        "",
        "---",
        "",
        "## Categories",
        "",
        "| Category | Projects | Top Project |",
        "|----------|----------|-------------|",
    ]

    for cat in CATEGORY_ORDER:
        meta = CATEGORY_META[cat]
        count = cats_count.get(cat, 0)
        # Find top project
        cat_projects = [p for p in projects if p["category"] == cat]
        top = cat_projects[0] if cat_projects else None
        top_str = f"[{top['name']}](https://github.com/{top['repo']}) ({format_stars_display(top['stars'])})" if top else "-"
        lines.append(f"| [{meta['name_en']}](categories/{cat}.md) | {count} | {top_str} |")

    lines.extend([
        "",
        "---",
        "",
        "## Top 20 by Stars",
        "",
        "| # | Project | Stars | Category |",
        "|---|---------|-------|----------|",
    ])

    sorted_by_stars = sorted(projects, key=lambda p: -p["stars"])
    for i, p in enumerate(sorted_by_stars[:20], 1):
        cat_meta = CATEGORY_META.get(p["category"], {})
        cat_name = cat_meta.get("name_en", p["category"])
        lines.append(
            f"| {i} | [{p['name']}](https://github.com/{p['repo']}) | {format_stars_display(p['stars'])} | {cat_name} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## How to Use This Directory",
        "",
        "Browse by category above, or check the [full project list in JSON](data/projects.json) for programmatic access.",
        "",
        "## Contributing",
        "",
        "Know a project that should be listed? [Open a PR](CONTRIBUTING.md) or [create an issue](https://github.com/Octo-o-o-o/openclaw-landscape/issues/new).",
        "",
        "## Update Log",
        "",
        "This directory is updated daily via GitHub Actions. Stars and project status are refreshed automatically.",
        "",
        "See [update-log.md](update-log.md) for the full changelog.",
        "",
        "---",
        "",
        "*This directory started as internal research for [ClawButler](https://github.com/Octo-o-o-o/clawbutler), an open-source Agent control plane. We figured the community might find it useful too, so here it is. PRs welcome.*",
        "",
    ])

    return "\n".join(lines)


def generate_readme_zh(projects: list[dict]) -> str:
    total = len(projects)
    cats_count = {}
    for p in projects:
        cats_count[p["category"]] = cats_count.get(p["category"], 0) + 1

    total_stars = sum(p["stars"] for p in projects)

    lines = [
        "# OpenClaw Landscape",
        "",
        f"OpenClaw 生态项目全景目录 — **{total} 个项目**，横跨 **{len(CATEGORY_ORDER)} 个分类**。",
        "",
        f"追踪总星数：**{format_stars_display(total_stars)}**",
        "",
        "[English](README.md) | 中文",
        "",
        "---",
        "",
        "## 分类",
        "",
        "| 分类 | 项目数 | 热门项目 |",
        "|------|--------|---------|",
    ]

    for cat in CATEGORY_ORDER:
        meta = CATEGORY_META[cat]
        count = cats_count.get(cat, 0)
        cat_projects = [p for p in projects if p["category"] == cat]
        top = cat_projects[0] if cat_projects else None
        top_str = f"[{top['name']}](https://github.com/{top['repo']}) ({format_stars_display(top['stars'])})" if top else "-"
        lines.append(f"| [{meta['name_zh']}](categories/{cat}.md) | {count} | {top_str} |")

    lines.extend([
        "",
        "---",
        "",
        "## Stars Top 20",
        "",
        "| # | 项目 | Stars | 分类 |",
        "|---|------|-------|------|",
    ])

    sorted_by_stars = sorted(projects, key=lambda p: -p["stars"])
    for i, p in enumerate(sorted_by_stars[:20], 1):
        cat_meta = CATEGORY_META.get(p["category"], {})
        cat_name = cat_meta.get("name_zh", p["category"])
        lines.append(
            f"| {i} | [{p['name']}](https://github.com/{p['repo']}) | {format_stars_display(p['stars'])} | {cat_name} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 如何使用",
        "",
        "按上方分类浏览，或查看 [projects.json](data/projects.json) 获取结构化数据。",
        "",
        "## 贡献",
        "",
        "知道应该收录的项目？[提交 PR](CONTRIBUTING.md) 或 [创建 Issue](https://github.com/Octo-o-o-o/openclaw-landscape/issues/new)。",
        "",
        "## 更新日志",
        "",
        "本目录通过 GitHub Actions 每日自动更新。Stars 和项目状态会自动刷新。",
        "",
        "查看 [update-log.md](update-log.md) 获取完整变更记录。",
        "",
        "---",
        "",
        "*本目录源自 [ClawButler](https://github.com/Octo-o-o-o/clawbutler)（开源 Agent 控制面）的内部调研。觉得对社区有用，就开放出来了。欢迎 PR。*",
        "",
    ])

    return "\n".join(lines)


def main():
    projects = json.loads(DATA_PATH.read_text())
    print(f"Loaded {len(projects)} projects")

    # Generate category pages
    CATEGORIES_DIR.mkdir(exist_ok=True)
    for cat in CATEGORY_ORDER:
        cat_projects = [p for p in projects if p["category"] == cat]
        if not cat_projects:
            continue
        content = generate_category_page(cat, cat_projects)
        out = CATEGORIES_DIR / f"{cat}.md"
        out.write_text(content)
        print(f"  {cat}.md ({len(cat_projects)} projects)")

    # Generate READMEs
    readme = generate_readme(projects)
    (ROOT / "README.md").write_text(readme)
    print("  README.md")

    readme_zh = generate_readme_zh(projects)
    (ROOT / "README.zh-CN.md").write_text(readme_zh)
    print("  README.zh-CN.md")

    print("Done!")


if __name__ == "__main__":
    main()
