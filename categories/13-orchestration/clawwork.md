> https://github.com/HKUDS/ClawWork

# ClawWork: OpenClaw as Your AI Coworker

## Basic Info

- **Project URL**: https://github.com/HKUDS/ClawWork
- **Stars**: 6,988
- **Language**: Python
- **Created**: 2026-02-15
- **Last Updated**: 2026-03-11
- **Tagline**: $19K in 8 Hours -- AI Coworker for 44+ Professions

## Problem & Solution

### Core Problem

1. **The Gap from AI Assistant to AI Coworker**
   - Existing AI assistants can only handle simple conversations and task assistance, unable to create real economic value
   - Lack of verification mechanisms for AI's real working capabilities in production environments
   - Traditional technical benchmarks cannot measure AI's actual work quality, cost efficiency, and long-term viability

2. **Missing AI Economic Sustainability Verification**
   - The balance between AI model token costs and output value has not been sufficiently tested
   - Lack of AI decision-making assessment under real economic pressure
   - Unable to verify whether AI can achieve economic self-sufficiency in real work scenarios

3. **Difficulty in Cross-Profession AI Capability Assessment**
   - Lack of standardized task sets covering multiple economic sectors
   - Non-uniform quality assessment standards across different professions
   - Unable to horizontally compare different AI models' performance in professional work

### Solution

**ClawWork transforms AI assistants into true AI coworkers** through the following mechanisms:

1. **Real Professional Task System**
   - 220 real professional tasks based on the GDPVal dataset
   - Covering 44 economic sectors (manufacturing, finance, healthcare, legal, etc.)
   - Tasks require producing real deliverables (Word documents, Excel spreadsheets, PDF reports, etc.)

2. **Extreme Economic Pressure Testing**
   - Agent starts with only $10 in initial funds
   - Each LLM call costs token fees
   - Income comes solely from completing high-quality work tasks
   - A single mistake can lead to bankruptcy

3. **Strategic Work vs Learning Choices**
   - Agent faces daily decisions: work immediately to earn money vs invest in learning to improve future performance
   - Simulates real career development trade-offs

4. **Rigorous LLM Evaluation System**
   - Uses GPT-5.2 for quality scoring
   - Category-specific scoring criteria for 44 GDPVal sectors
   - Payment formula: `payment = quality_score x (estimated_hours x BLS_hourly_wage)`

## Core Architecture

### System Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    ClawWork Agent                          │
│                                                            │
│  Daily Loop:                                               │
│    1. Receive GDPVal task assignment                       │
│    2. Decide: work or learn?                               │
│    3. Execute (complete task / build knowledge base)        │
│    4. Earn income / deduct token costs                     │
│    5. Persist state & update dashboard                     │
└──────────────────────────────────────────────────────────┘
          │                           │
          ▼                           ▼
   ┌─────────────┐           ┌──────────────────┐
   │  8 Tools    │           │ Economic Tracker │
   │             │           │                  │
   │ • decide    │           │ • Balance        │
   │ • submit    │           │ • Token costs    │
   │ • learn     │           │ • Work income    │
   │ • status    │           │ • Survival tier  │
   │ • search    │           └──────────────────┘
   │ • create    │
   │ • execute   │
   │ • video     │
   └─────────────┘
          │
          ▼
   ┌──────────────────────────────────┐
   │   FastAPI + React Dashboard      │
   │   WebSocket real-time updates    │
   └──────────────────────────────────┘
```

### Tech Stack

- **Core Engine**: Python 3.10+
- **Agent Framework**: Based on Nanobot (lightweight AI coworker framework)
- **LLM Integration**: LangChain / LiteLLM (multi-model support)
- **Code Sandbox**: E2B (default) / BoxLite (experimental local backend)
- **Web Search**: Tavily (default) / Jina AI
- **Dashboard**: FastAPI + React + WebSocket
- **Document Generation**: python-docx, openpyxl, reportlab
- **Video Generation**: moviepy

### Directory Structure

```
ClawWork/
├── livebench/                    # Core economic engine
│   ├── agent/
│   │   ├── live_agent.py         # Main Agent orchestrator
│   │   ├── economic_tracker.py   # Balance, cost, income tracking
│   │   └── wrapup_workflow.py    # Task summary workflow
│   ├── work/
│   │   ├── task_manager.py       # GDPVal task loading & assignment
│   │   ├── evaluator.py          # Work evaluation interface
│   │   └── llm_evaluator.py      # LLM scoring implementation
│   ├── tools/
│   │   ├── direct_tools.py       # Core tools (decide, submit, learn, status)
│   │   └── productivity/         # Productivity tools (search, create, execute, video)
│   ├── api/
│   │   └── server.py             # FastAPI backend + WebSocket
│   ├── prompts/
│   │   └── live_agent_prompt.py  # System prompts
│   └── configs/                  # Agent configuration files
├── clawmode_integration/         # Nanobot integration layer
│   ├── agent_loop.py             # ClawWorkAgentLoop + /clawwork command
│   ├── task_classifier.py        # Profession classifier (40 categories)
│   ├── provider_wrapper.py       # TrackedProvider (cost interception)
│   ├── tools.py                  # ClawWork tool wrappers
│   └── cli.py                    # CLI entry point
├── eval/
│   ├── meta_prompts/             # Category evaluation criteria (44 professions)
│   └── generate_meta_prompts.py  # Meta-prompt generator
├── scripts/
│   ├── estimate_task_hours.py    # GPT task hour estimation
│   └── calculate_task_values.py  # BLS wage x hours = task value
└── frontend/                     # React dashboard
```

## Key Features

### 1. Real Professional Task System (GDPVal Benchmark)

**Dataset Scale**
- 220 real professional tasks
- 44 profession categories
- 4 major domains: Technology & Engineering, Business & Finance, Healthcare & Social Services, Legal & Operations

**Task Type Examples**

| Domain | Example Professions |
|------|---------|
| Manufacturing | Purchasing agents, production supervisors |
| Professional Services | Financial analysts, compliance officers |
| Information Technology | Computer and information systems managers |
| Finance & Insurance | Financial managers, auditors |
| Healthcare | Social workers, health administrators |
| Government | Police supervisors, administrative managers |
| Retail | Customer service representatives, counter clerks |
| Wholesale | Sales supervisors, purchasing agents |
| Real Estate | Property managers, appraisers |

**Payment System**
```
Payment = quality_score x (estimated_hours x BLS_hourly_wage)
```

- Task value range: $82.78 -- $5,004.00
- Average task value: $259.45
- Quality score range: 0.0 -- 1.0
- Total tasks: 220

### 2. Economic System

**Initial Conditions**
- Starting balance: $10 (intentionally tight)
- Token costs: automatically deducted after each LLM call
- API costs: Web search (Tavily $0.0008/call, Jina $0.05/1M tokens)

**Cost Tracking** (one record per task)
```json
{
  "task_id": "abc-123",
  "date": "2025-01-20",
  "llm_usage": {
    "total_input_tokens": 4500,
    "total_output_tokens": 900,
    "total_cost": 0.02025
  },
  "api_usage": {
    "search_api_cost": 0.0016
  },
  "cost_summary": {
    "total_cost": 0.02185
  },
  "balance_after": 1198.41
}
```

**Token Pricing** (configurable)
```json
"token_pricing": {
  "input_per_1m": 2.5,
  "output_per_1m": 10.0
}
```

### 3. Agent Toolset (8 Tools)

| Tool | Description |
|------|------|
| `decide_activity(activity, reasoning)` | Choose: `"work"` or `"learn"` |
| `submit_work(work_output, artifact_file_paths)` | Submit completed work for evaluation + payment |
| `learn(topic, knowledge)` | Save knowledge to persistent memory (minimum 200 characters) |
| `get_status()` | Check balance, costs, survival tier |
| `search_web(query, max_results)` | Web search via Tavily or Jina AI |
| `create_file(filename, content, file_type)` | Create .txt, .xlsx, .docx, .pdf documents |
| `execute_code_sandbox(code, language)` | Run Python in isolated sandbox (E2B default, BoxLite optional) |
| `create_video(slides_json, output_filename)` | Generate MP4 from text/image slides |

### 4. Nanobot Integration (ClawMode)

**Integration Architecture**
```
You (Telegram / Discord / CLI / ...)
  │
  ▼
nanobot gateway
  │
  ├── nanobot tools (file, shell, web, message, spawn, cron)
  ├── clawwork tools (get_status, decide_activity, submit_work, learn)
  ├── /clawwork command → TaskClassifier → paid task assignment
  └── TrackedProvider → deducts from agent balance on each LLM call
```

**Key Components**

1. **ClawWorkAgentLoop** (`agent_loop.py`)
   - Subclasses nanobot's `AgentLoop`
   - Intercepts `/clawwork` commands in `_process_message()`
   - Wraps each message with `start_task()` / `end_task()` for cost tracking
   - Appends cost footer to responses

2. **TaskClassifier** (`task_classifier.py`)
   - Classifies free-form instructions
   - Selects best match from 40 professions + hourly wages
   - Uses LLM (temp=0.3, JSON output) for classification
   - Fuzzy matching fallback (case-insensitive, substring matching)

3. **TrackedProvider** (`provider_wrapper.py`)
   - Wraps nanobot's LLM provider
   - Intercepts each `chat()` call and feeds token usage back to `EconomicTracker`
   - Uses litellm's actual token counts (not estimates)

**`/clawwork` Command**

Send `/clawwork <instruction>` from any connected channel to assign a paid task:

```
/clawwork Write a market analysis report for electric vehicles
```

The system will:
1. **Classify** the instruction — select the best profession from 40 categories (using BLS wage data) and estimate professional hours
2. **Calculate task value** — `hours x hourly_wage` (e.g., 2h x $44.96/hr = $89.92)
3. **Assign the task** to the agent with full context
4. **Evaluate** submitted work and pay proportionally to quality

### 5. Real-Time Dashboard

**Main Tab**
- Balance chart (real-time line graph)
- Activity distribution (work vs learning)
- Economic metrics: income, costs, net worth, survival status

**Work Tasks Tab**
- All assigned GDPVal tasks (sector & profession)
- Payment amounts and quality scores
- Full task prompts and submitted deliverables

**Learning Tab**
- Knowledge entries organized by topic
- Learning timeline
- Searchable knowledge base

### 6. Benchmark Metrics

| Metric | Description |
|------|------|
| **Survival Days** | How long the Agent remains solvent |
| **Final Balance** | Net economic outcome |
| **Total Work Income** | Total income from completed tasks |
| **Profit Margin** | `(income - costs) / costs` |
| **Work Quality** | Average quality score across tasks (0--1) |
| **Token Efficiency** | Income earned per dollar of token cost |
| **Activity Mix** | Percentage of work vs learning decisions |
| **Task Completion Rate** | Completed tasks / assigned tasks |

### 7. Leaderboard Performance

| Rank | Agent | Starting Funds | Balance | Income | Cost | Hourly Rate | Avg Quality |
|:----:|-------|--------:|--------:|-------:|-----:|---------:|------------:|
| 1 | **ATIC + Qwen3.5-Plus** | $10.00 | $19,915.68 | $19,914.38 | $8.70 | $2,285.31/hr | 61.6% |
| 2 | **Gemini 3.1 Pro Preview** | $10.00 | $15,661.71 | $15,757.48 | $105.76 | $1,287.47/hr | 43.3% |
| 3 | **Qwen3.5-Plus** | $10.00 | $15,268.13 | $15,264.92 | $6.78 | $1,390.42/hr | 41.6% |
| 4 | **GLM-4.7** | $10.00 | $11,497.05 | $11,503.49 | $16.44 | $877.80/hr | 40.6% |
| 5 | **ATIC-DEEPSEEK** | $10.00 | $10,877.01 | $10,870.52 | $3.52 | $2,579.16/hr | 66.8% |

**Key Findings**:
- Top Agents achieve $1,500+/hr equivalent wage — exceeding typical human white-collar productivity
- Best models earn $19K+ in 8 hours
- Huge cost efficiency variance: ATIC-DEEPSEEK costs only $3.52, while Gemini 3.1 Pro costs $105.76

<!-- lastCommit: 6a7050b -->
