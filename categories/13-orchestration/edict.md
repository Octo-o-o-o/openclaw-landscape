> https://github.com/cft0808/edict

# Edict (7,637 stars)

## Problem & Solution

Existing Multi-Agent frameworks (CrewAI/AutoGen) allow Agents to collaborate freely but lack quality review and observability, producing unreliable output with no intervention mechanism. Edict restructures Agent collaboration architecture using China's Tang Dynasty "Three Departments and Six Ministries" system: Crown Prince for message routing, Zhongshu (Central Secretariat) for planning, Menxia (Chancellery) for review and rejection, Shangshu (Department of State Affairs) for dispatch, and Six Ministries for parallel execution — enforcing quality gates + real-time dashboards + complete audit trails.

## Key Features

- **Twelve-Ministry Agent Architecture** — Crown Prince (message routing) + Three Departments (Zhongshu for planning / Menxia for review / Shangshu for dispatch) + Seven Ministries (Revenue, Rites, War, Justice, Works, Personnel + Morning Court Official) for specialized execution, with strict permission matrices controlling message flow
- **Menxia Mandatory Review** — Zhongshu's plans must pass Menxia's quality inspection; non-compliant plans are directly rejected and sent back for rework, creating institutional quality gates (missing in CrewAI/AutoGen)
- **Military Command Center Real-Time Dashboard** — React 18 frontend + Python stdlib backend (zero dependencies), real-time display of task flow, Agent status, heartbeat monitoring, and execution timeline
- **Hot-Swap Model Configuration** — One-click LLM switching, Skill management, and complete archive viewing within the dashboard, no service restart required
- **Feishu Integration** — Create tasks via Feishu commands, auto-report upon completion; aggregated news push
- **Docker One-Click Experience** — `docker run -p 7891:7891 cft0808/edict` launches a complete dashboard with pre-loaded simulation data
