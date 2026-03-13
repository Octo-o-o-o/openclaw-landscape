# ClawWork: OpenClaw as Your AI Coworker

## 基本信息

- **项目地址**: https://github.com/HKUDS/ClawWork
- **Stars**: 6,988
- **语言**: Python
- **创建时间**: 2026-02-15
- **最后更新**: 2026-03-11
- **标语**: 💰 $19K in 8 Hours — AI Coworker for 44+ Professions

## 问题与解决方案

### 核心问题

1. **AI 助手到 AI 同事的进化鸿沟**
   - 现有 AI 助手只能完成简单对话和任务辅助，无法创造真实经济价值
   - 缺乏对 AI 在生产环境中真实工作能力的验证机制
   - 传统技术 Benchmark 无法衡量 AI 的实际工作质量、成本效率和长期生存能力

2. **AI 经济可持续性验证缺失**
   - AI 模型的 Token 成本与产出价值之间的平衡关系未被充分测试
   - 缺乏真实经济压力下的 AI 决策能力评估
   - 无法验证 AI 是否能在真实工作场景中实现经济自给自足

3. **跨职业 AI 能力评估困难**
   - 缺乏覆盖多个经济部门的标准化任务集
   - 不同职业的工作质量评估标准不统一
   - 无法横向比较不同 AI 模型在专业工作中的表现

### 解决方案

**ClawWork 将 AI 助手转变为真正的 AI 同事**，通过以下机制实现：

1. **真实职业任务系统**
   - 基于 GDPVal 数据集的 220 个真实专业任务
   - 覆盖 44 个经济部门（制造业、金融、医疗、法律等）
   - 任务需要产出真实交付物（Word 文档、Excel 表格、PDF 报告等）

2. **极端经济压力测试**
   - Agent 初始资金仅 $10
   - 每次 LLM 调用都需支付 Token 成本
   - 收入仅来自完成高质量工作任务
   - 一次失误可能导致破产

3. **战略性工作与学习选择**
   - Agent 每天面临决策：立即工作赚钱 vs 投资学习提升未来表现
   - 模拟真实职业发展中的权衡取舍

4. **严格的 LLM 评估系统**
   - 使用 GPT-5.2 进行质量评分
   - 针对 44 个 GDPVal 部门的分类评分标准
   - 支付公式：`payment = quality_score × (estimated_hours × BLS_hourly_wage)`

## 核心架构

### 系统架构

```
┌──────────────────────────────────────────────────────────┐
│                    ClawWork Agent                        │
│                                                          │
│  Daily Loop:                                             │
│    1. 接收 GDPVal 任务分配                                │
│    2. 决策：工作还是学习？                                │
│    3. 执行（完成任务 / 构建知识库）                        │
│    4. 赚取收入 / 扣除 Token 成本                          │
│    5. 持久化状态 & 更新仪表板                             │
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

### 技术栈

- **核心引擎**: Python 3.10+
- **Agent 框架**: 基于 Nanobot（轻量级 AI 同事框架）
- **LLM 集成**: LangChain / LiteLLM（支持多模型）
- **代码沙箱**: E2B（默认）/ BoxLite（实验性本地后端）
- **Web 搜索**: Tavily（默认）/ Jina AI
- **仪表板**: FastAPI + React + WebSocket
- **文档生成**: python-docx, openpyxl, reportlab
- **视频生成**: moviepy

### 目录结构

```
ClawWork/
├── livebench/                    # 核心经济引擎
│   ├── agent/
│   │   ├── live_agent.py         # 主 Agent 编排器
│   │   ├── economic_tracker.py   # 余额、成本、收入跟踪
│   │   └── wrapup_workflow.py    # 任务总结工作流
│   ├── work/
│   │   ├── task_manager.py       # GDPVal 任务加载与分配
│   │   ├── evaluator.py          # 工作评估接口
│   │   └── llm_evaluator.py      # LLM 评分实现
│   ├── tools/
│   │   ├── direct_tools.py       # 核心工具（decide, submit, learn, status）
│   │   └── productivity/         # 生产力工具（search, create, execute, video）
│   ├── api/
│   │   └── server.py             # FastAPI 后端 + WebSocket
│   ├── prompts/
│   │   └── live_agent_prompt.py  # 系统提示词
│   └── configs/                  # Agent 配置文件
├── clawmode_integration/         # Nanobot 集成层
│   ├── agent_loop.py             # ClawWorkAgentLoop + /clawwork 命令
│   ├── task_classifier.py        # 职业分类器（40 类别）
│   ├── provider_wrapper.py       # TrackedProvider（成本拦截）
│   ├── tools.py                  # ClawWork 工具封装
│   └── cli.py                    # CLI 入口
├── eval/
│   ├── meta_prompts/             # 分类评估标准（44 个职业）
│   └── generate_meta_prompts.py  # 元提示词生成器
├── scripts/
│   ├── estimate_task_hours.py    # GPT 任务工时估算
│   └── calculate_task_values.py  # BLS 工资 × 工时 = 任务价值
└── frontend/                     # React 仪表板
```

## 关键特性

### 1. 真实职业任务系统（GDPVal Benchmark）

**数据集规模**
- 220 个真实专业任务
- 44 个职业类别
- 4 大领域：技术与工程、商业与金融、医疗与社会服务、法律与运营

**任务类型示例**

| 领域 | 职业示例 |
|------|---------|
| 制造业 | 采购代理、生产主管 |
| 专业服务 | 金融分析师、合规官 |
| 信息技术 | 计算机与信息系统经理 |
| 金融保险 | 财务经理、审计师 |
| 医疗保健 | 社会工作者、健康管理员 |
| 政府 | 警察主管、行政经理 |
| 零售 | 客户服务代表、柜台职员 |
| 批发 | 销售主管、采购代理 |
| 房地产 | 物业经理、评估师 |

**支付系统**
```
Payment = quality_score × (estimated_hours × BLS_hourly_wage)
```

- 任务价值范围：$82.78 – $5,004.00
- 平均任务价值：$259.45
- 质量评分范围：0.0 – 1.0
- 总任务数：220

### 2. 经济系统

**初始条件**
- 初始余额：$10（设计上的紧张）
- Token 成本：每次 LLM 调用后自动扣除
- API 成本：Web 搜索（Tavily $0.0008/次，Jina $0.05/1M tokens）

**成本跟踪**（每任务一条记录）
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

**Token 定价**（可配置）
```json
"token_pricing": {
  "input_per_1m": 2.5,
  "output_per_1m": 10.0
}
```

### 3. Agent 工具集（8 个工具）

| 工具 | 描述 |
|------|------|
| `decide_activity(activity, reasoning)` | 选择：`"work"` 或 `"learn"` |
| `submit_work(work_output, artifact_file_paths)` | 提交完成的工作以进行评估 + 支付 |
| `learn(topic, knowledge)` | 保存知识到持久化记忆（最少 200 字符）|
| `get_status()` | 检查余额、成本、生存等级 |
| `search_web(query, max_results)` | 通过 Tavily 或 Jina AI 进行 Web 搜索 |
| `create_file(filename, content, file_type)` | 创建 .txt, .xlsx, .docx, .pdf 文档 |
| `execute_code_sandbox(code, language)` | 在隔离沙箱中运行 Python（E2B 默认，可选 BoxLite）|
| `create_video(slides_json, output_filename)` | 从文本/图像幻灯片生成 MP4 |

### 4. Nanobot 集成（ClawMode）

**集成架构**
```
You (Telegram / Discord / CLI / ...)
  │
  ▼
nanobot gateway
  │
  ├── nanobot tools (file, shell, web, message, spawn, cron)
  ├── clawwork tools (get_status, decide_activity, submit_work, learn)
  ├── /clawwork command → TaskClassifier → 付费任务分配
  └── TrackedProvider → 每次 LLM 调用从 agent 余额中扣除
```

**关键组件**

1. **ClawWorkAgentLoop** (`agent_loop.py`)
   - 子类化 nanobot 的 `AgentLoop`
   - 在 `_process_message()` 中拦截 `/clawwork` 命令
   - 用 `start_task()` / `end_task()` 包装每条消息以进行成本跟踪
   - 在响应中附加成本页脚

2. **TaskClassifier** (`task_classifier.py`)
   - 分类自由形式的指令
   - 从 40 个职业 + 时薪中选择最佳匹配
   - 使用 LLM（temp=0.3，JSON 输出）进行分类
   - 模糊匹配回退（不区分大小写，子串匹配）

3. **TrackedProvider** (`provider_wrapper.py`)
   - 包装 nanobot 的 LLM provider
   - 拦截每次 `chat()` 调用并将 token 使用情况反馈给 `EconomicTracker`
   - 使用 litellm 的实际 token 计数（非估算）

**`/clawwork` 命令**

从任何连接的频道发送 `/clawwork <instruction>` 以分配付费任务：

```
/clawwork 为电动汽车撰写市场分析报告
```

系统将：
1. **分类**指令 — 从 40 个类别中选择最佳职业（使用 BLS 工资数据）并估算专业工时
2. **计算任务价值** — `hours × hourly_wage`（例如 2h × $44.96/hr = $89.92）
3. **分配任务**给 agent，包含完整上下文
4. **评估**提交的工作并按质量比例支付

### 5. 实时仪表板

**主标签页**
- 余额图表（实时折线图）
- 活动分布（工作 vs 学习）
- 经济指标：收入、成本、净值、生存状态

**工作任务标签页**
- 所有分配的 GDPVal 任务（部门 & 职业）
- 支付金额和质量评分
- 完整任务提示和提交的交付物

**学习标签页**
- 按主题组织的知识条目
- 学习时间线
- 可搜索的知识库

### 6. Benchmark 指标

| 指标 | 描述 |
|------|------|
| **生存天数** | Agent 保持偿付能力的时间 |
| **最终余额** | 净经济结果 |
| **总工作收入** | 完成任务的总收入 |
| **利润率** | `(income - costs) / costs` |
| **工作质量** | 任务的平均质量评分（0–1）|
| **Token 效率** | 每美元 Token 成本赚取的收入 |
| **活动组合** | 工作 vs 学习决策的百分比 |
| **任务完成率** | 完成任务 / 分配任务 |

### 7. 排行榜表现

| 排名 | Agent | 起始资金 | 余额 | 收入 | 成本 | 时薪 | 平均质量 |
|:----:|-------|--------:|--------:|-------:|-----:|---------:|------------:|
| 🥇 | **ATIC + Qwen3.5-Plus** | $10.00 | $19,915.68 | $19,914.38 | $8.70 | $2,285.31/hr | 61.6% |
| 🥈 | **Gemini 3.1 Pro Preview** | $10.00 | $15,661.71 | $15,757.48 | $105.76 | $1,287.47/hr | 43.3% |
| 🥉 | **Qwen3.5-Plus** | $10.00 | $15,268.13 | $15,264.92 | $6.78 | $1,390.42/hr | 41.6% |
| 4 | **GLM-4.7** | $10.00 | $11,497.05 | $11,503.49 | $16.44 | $877.80/hr | 40.6% |
| 5 | **ATIC-DEEPSEEK** | $10.00 | $10,877.01 | $10,870.52 | $3.52 | $2,579.16/hr | 66.8% |

**关键发现**：
- 顶级 Agent 实现 $1,500+/hr 等效工资 — 超过典型人类白领生产力
- 最佳模型在 8 小时内赚取 $19K+
- 成本效率差异巨大：ATIC-DEEPSEEK 成本仅 $3.52，而 Gemini 3.1 Pro 成本 $105.76
# ClawButler 可以为每个 Agent 实例添加经济跟踪
class AgentEconomicTracker:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.token_costs = []
        self.task_revenues = []
        self.balance = initial_budget

    def track_llm_call(self, input_tokens, output_tokens, model):
        cost = calculate_cost(input_tokens, output_tokens, model)
        self.balance -= cost
        self.token_costs.append({
            "timestamp": now(),
            "cost": cost,
            "model": model
        })

    def track_task_completion(self, task_id, revenue, quality_score):
        self.balance += revenue
        self.task_revenues.append({
            "task_id": task_id,
            "revenue": revenue,
            "quality": quality_score
        })
```

### 2. 跨平台任务分类与路由

**借鉴点**：
- ClawWork 的 `TaskClassifier` 可以将自由形式的指令映射到 40 个职业类别
- ClawButler 可以使用类似机制将用户请求路由到最合适的 Agent 平台

**实施建议**：
```python
# ClawButler 的智能路由器
class AgentPlatformRouter:
    def __init__(self):
        self.platform_capabilities = {
            "openclaw": ["code", "web_search", "file_ops"],
            "dify": ["workflow", "knowledge_base"],
            "langgraph": ["complex_reasoning", "multi_step"],
            "custom": ["domain_specific"]
        }

    async def route_task(self, task_description: str) -> str:
        # 使用 LLM 分类任务类型
        task_type = await self.classify_task(task_description)

        # 根据能力匹配选择最佳平台
        best_platform = self.match_platform(task_type)

        return best_platform
```

### 3. 质量评估与支付系统

**借鉴点**：
- ClawWork 的 LLM 评估系统可以为 ClawButler 提供 Agent 输出质量验证
- 支付公式 `quality_score × estimated_value` 可用于企业 Agent 的绩效考核

**实施建议**：
```python
# ClawButler 的质量评估服务
class AgentQualityEvaluator:
    def __init__(self, evaluation_model: str):
        self.model = evaluation_model
        self.meta_prompts = load_meta_prompts()  # 从 ClawWork 借鉴

    async def evaluate_output(
        self,
        task_prompt: str,
        agent_output: str,
        category: str
    ) -> float:
        meta_prompt = self.meta_prompts[category]

        evaluation_prompt = f"""
        Task: {task_prompt}
        Output: {agent_output}

        {meta_prompt}

        Rate the quality from 0.0 to 1.0.
        """

        response = await self.llm.chat(evaluation_prompt)
        quality_score = parse_score(response)

        return quality_score
```

### 4. 多模型竞技场（Arena）

**借鉴点**：
- ClawWork 的排行榜机制可以为 ClawButler 提供跨平台 Agent 性能比较
- 企业客户可以看到不同 Agent 平台在相同任务上的表现差异

**实施建议**：
```python
# ClawButler 的 Agent Arena
class AgentArena:
    def __init__(self):
        self.leaderboard = []

    async def run_benchmark(self, task: Task, agents: List[Agent]):
        results = []

        for agent in agents:
            start_time = time.time()
            output = await agent.execute(task)
            duration = time.time() - start_time

            quality = await self.evaluator.evaluate(task, output)
            cost = agent.get_cost()

            results.append({
                "agent": agent.name,
                "platform": agent.platform,
                "quality": quality,
                "cost": cost,
                "duration": duration,
                "efficiency": quality / cost  # 质量/成本比
            })

        self.update_leaderboard(results)
        return results
```

### 5. 实时经济仪表板

**借鉴点**：
- ClawWork 的 WebSocket 实时仪表板可以为 ClawButler 提供 Agent 监控界面
- 企业客户可以实时查看 Agent 的成本、收入、任务完成情况

**实施建议**：
```typescript
// ClawButler 的实时仪表板组件
interface AgentMetrics {
  agentId: string;
  platform: string;
  balance: number;
  totalCost: number;
  totalRevenue: number;
  tasksCompleted: number;
  averageQuality: number;
  status: 'thriving' | 'stable' | 'struggling' | 'bankrupt';
}

function AgentDashboard() {
  const [metrics, setMetrics] = useState<AgentMetrics[]>([]);

  useEffect(() => {
    const ws = new WebSocket('ws://api.clawbutler.cc/ws/metrics');

    ws.onmessage = (event) => {
      const update = JSON.parse(event.data);
      setMetrics(prev => updateMetrics(prev, update));
    };

    return () => ws.close();
  }, []);

  return (
    <div>
      <BalanceChart data={metrics} />
      <TaskCompletionTable data={metrics} />
      <CostBreakdown data={metrics} />
    </div>
  );
}
```

### 6. MCP 和 A2A 协议集成

**借鉴点**：
- ClawWork 的工具系统（8 个工具）可以通过 MCP 协议暴露给其他 Agent
- ClawButler 可以将 ClawWork 的经济跟踪能力作为 MCP 服务提供

**实施建议**：
```python
# ClawButler 的 MCP 服务：经济跟踪
class EconomicTrackingMCPServer:
    def __init__(self):
        self.trackers = {}

    @mcp_tool
    async def track_cost(
        self,
        agent_id: str,
        input_tokens: int,
        output_tokens: int,
        model: str
    ):
        """Track LLM call cost for an agent"""
        tracker = self.get_tracker(agent_id)
        cost = calculate_cost(input_tokens, output_tokens, model)
        tracker.deduct(cost)

        return {
            "cost": cost,
            "balance": tracker.balance,
            "status": tracker.get_status()
        }

    @mcp_tool
    async def get_agent_status(self, agent_id: str):
        """Get economic status of an agent"""
        tracker = self.get_tracker(agent_id)
        return {
            "balance": tracker.balance,
            "total_cost": tracker.total_cost,
            "total_revenue": tracker.total_revenue,
            "profit_margin": tracker.profit_margin,
            "status": tracker.get_status()
        }
```

### 7. 知识管理系统

**借鉴点**：
- ClawWork 的 `learn()` 工具和知识库可以为 ClawButler 提供跨 Agent 的知识共享机制
- Agent 可以将学到的知识存储到 ClawButler 的统一知识库中

**实施建议**：
```python
# ClawButler 的统一知识库
class UnifiedKnowledgeBase:
    def __init__(self):
        self.knowledge_store = {}
        self.embeddings = EmbeddingModel()

    async def store_knowledge(
        self,
        agent_id: str,
        topic: str,
        content: str,
        metadata: dict
    ):
        """Store knowledge from any agent"""
        embedding = await self.embeddings.embed(content)

        self.knowledge_store[f"{agent_id}:{topic}"] = {
            "content": content,
            "embedding": embedding,
            "metadata": metadata,
            "timestamp": now()
        }

    async def retrieve_knowledge(
        self,
        query: str,
        agent_id: Optional[str] = None
    ) -> List[dict]:
        """Retrieve relevant knowledge for any agent"""
        query_embedding = await self.embeddings.embed(query)

        # 语义搜索
        results = self.semantic_search(query_embedding, agent_id)

        return results
```

### 8. 配置管理与多 Agent 支持

**借鉴点**：
- ClawWork 的配置系统支持多个 Agent 同时运行
- ClawButler 可以借鉴其配置结构来管理跨平台 Agent

**实施建议**：
```json
{
  "agents": [
    {
      "id": "openclaw-agent-1",
      "platform": "openclaw",
      "model": "gpt-4o",
      "enabled": true,
      "economic": {
        "initial_balance": 100.0,
        "token_pricing": {
          "input_per_1m": 2.5,
          "output_per_1m": 10.0
        }
      },
      "capabilities": ["code", "web_search", "file_ops"]
    },
    {
      "id": "dify-agent-1",
      "platform": "dify",
      "workflow_id": "wf-123",
      "enabled": true,
      "economic": {
        "initial_balance": 50.0
      },
      "capabilities": ["workflow", "knowledge_base"]
    }
  ],
  "federation": {
    "enabled": true,
    "peers": [
      {
        "peer_id": "remote-clawbutler-instance",
        "endpoint": "https://remote.clawbutler.cc"
      }
    ]
  }
}
```

### 总结

ClawWork 为 ClawButler 提供了以下核心价值：

1. **经济可持续性验证** — 为 Agent 控制平面添加成本跟踪和 ROI 分析能力
2. **智能任务路由** — 基于任务分类将请求路由到最合适的 Agent 平台
3. **质量评估系统** — 为跨平台 Agent 输出提供统一的质量评分标准
4. **性能比较机制** — 通过 Arena 模式比较不同平台 Agent 的表现
5. **实时监控仪表板** — 为企业客户提供 Agent 运营的可视化界面
6. **MCP 服务集成** — 将经济跟踪能力作为标准 MCP 服务暴露
7. **知识共享机制** — 构建跨 Agent 的统一知识库
8. **多 Agent 配置管理** — 支持异构 Agent 生态系统的统一配置

这些借鉴点与 ClawButler 的核心价值主张（统一身份、权限、协作路由、审计跟踪、成本跟踪）高度契合，可以显著增强 ClawButler 作为 Agent 控制平面的能力。
