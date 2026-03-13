# Gen-Verse/OpenClaw-RL

## 基本信息

- **GitHub Stars**: 1,311
- **项目地址**: https://github.com/Gen-Verse/OpenClaw-RL
- **博客页面**: https://yinjjiew.github.io/projects/openclawrl
- **最新版本**: v1 (2026/2/26)
- **开源协议**: MIT
- **技术栈**: Python 3.12, CUDA 12.9, Slime RL Framework, SGLang, OpenClaw

## 问题与解决方案

### 核心问题
传统 AI Agent 系统面临的训练困境：
1. **数据收集成本高**: 需要预先收集大量标注数据集
2. **批量训练模式**: 集中式批处理训练，无法实时优化
3. **个性化不足**: 通用模型难以适应个人使用习惯
4. **反馈信号稀疏**: 缺乏有效的训练信号提取机制
5. **生产部署割裂**: 训练和服务是两个独立系统

### 解决方案
OpenClaw-RL 提出了一个**完全异步的强化学习框架**，通过日常对话自动训练个性化 Agent：

**核心创新**:
- **零 API Key**: 完全自托管，无需外部 API
- **完全异步**: 4 组件独立运行（Agent 服务、Rollout 收集、PRM 评判、策略训练）
- **对话即训练**: 拦截实时多轮对话，自动转换为训练信号
- **后台优化**: 模型在服务请求的同时后台训练，不中断使用
- **个性化**: 根据用户反馈持续优化，越用越懂你

**Slogan**: "Train a personalized agent simply by talking to it."

## 核心架构

### 系统架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                    OpenClaw-RL 异步架构                          │
│                                                                 │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────┐  │
│  │   OpenClaw   │─────►│  RL Server   │◄─────│   用户对话   │  │
│  │   Gateway    │ API  │  (FastAPI)   │ WS   │              │  │
│  └──────────────┘      └──────┬───────┘      └──────────────┘  │
│                               │                                 │
│                               │ 异步提交                         │
│                               ▼                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              4 组件异步循环                                │  │
│  │                                                            │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │  │
│  │  │ Agent 服务  │  │   Rollout   │  │  PRM 评判   │       │  │
│  │  │  (SGLang)   │  │   收集器    │  │ (多数投票)  │       │  │
│  │  │  2 GPUs     │  │  2 GPUs     │  │  2 GPUs     │       │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘       │  │
│  │                                                            │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │           策略训练 (GRPO/OPD)                        │  │  │
│  │  │           4 GPUs                                     │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 技术架构

**1. RL Server (FastAPI)**
```python
# openclaw_api_server.py
# 职责：
# - 作为 OpenAI 兼容 API 代理
# - 拦截多轮对话
# - 分类 main-line vs. side 消息
# - 触发 PRM 评判
# - 提交训练样本
```

**2. Rollout 收集器**
```python
# openclaw_rollout.py
# 职责：
# - 异步收集对话轨迹
# - 桥接 API Server ↔ SLIME Trainer
# - 管理 session 状态
# - 保证 at-least-one 样本
```

**3. PRM 评判器**
```
# 职责：
# - 基于 next-state 评分
# - 多数投票（m 次独立评估）
# - 输出 +1 (good) / -1 (bad) / 0 (neutral)
# - 异步并发评估
```

**4. 策略训练器 (Slime)**
```
# 职责：
# - PPO-style 策略梯度
# - GRPO 优势估计
# - 权重更新和检查点保存
# - 训练期间暂停提交
```

### 数据流

```
用户消息 → API Server → 策略模型 (SGLang) → 响应 + log_probs
                ↓
         等待 next-state
                ↓
         PRM 评判 (m 次投票) → 标量奖励 r
                ↓
         Rollout 收集器 → 训练样本
                ↓
         SLIME Trainer → 策略更新
                ↓
         新权重 → SGLang 重载
```

### 会话管理

**消息分类**:
- **Main-line**: 可训练的主线对话（用户请求 → Agent 响应）
- **Side**: 不可训练的旁路消息（系统提示、元对话）

**At-least-one 保证**:
- 每个 session 至少贡献 1 个有效训练样本
- 最后一轮默认排除（无 next-state），除非是唯一一轮

**Session 追踪**:
- 多轮对话按 session_id 分组
- 保持轮次顺序
- 支持并发 session

## 关键特性

### 1. 两种学习范式

#### Binary RL (GRPO)
**信号类型**: 评价性（好/坏）
**优势计算**: 序列级标量
**反馈类型**: 隐式反馈（点赞/点踩、环境成功/失败）
**信号密度**: 所有评分轮次

**算法**:
```
优势估计 (GRPO):
A_t = r, ∀t ∈ response tokens

策略梯度损失 (PPO-style):
ρ_t = π_θ(a_t | s_t) / π_old(a_t | s_t)
L_pg = -E_t[min(ρ_t A_t, clip(ρ_t, 1-ε, 1+ε_high) · A_t)]

总损失:
L = L_pg + β_KL · L_KL
```

**参数**:
- ε = 0.2 (clip 下界)
- ε_high = 0.28 (clip 上界)
- β_KL = 0.02
- β_ent = 0 (禁用熵奖励)

**启动**:
```bash
cd slime
bash ../openclaw-rl/run_qwen3_4b_openclaw_rl.sh
```

#### On-Policy Distillation (OPD)
**信号类型**: 方向性
**优势计算**: Token 级方向性
**反馈类型**: 显式纠正（"你应该先检查文件"）
**信号密度**: 仅接受 hint 的轮次

**算法**:
```
Hindsight Hint 提取:
1. 判断 (response, next_state) 是否有用
2. m 次投票，每次返回 +1/-1 和可选 hint
3. 选择最长的非平凡正向 hint
4. 如果没有，丢弃样本

Token 级 OPD:
A_t = log π_teacher(a_t | s + hint) - log π_θ(a_t | s)

训练损失:
L = L_pg + β_KL · L_KL
```

**启动**:
```bash
cd slime
bash ../openclaw-opd/run_qwen3_4b_openclaw_opd.sh
```

#### Top-K Logits Distillation (SDFT/SDPO-style)
**扩展**: 蒸馏 teacher top-K 分布而非单 token

**算法**:
```
Teacher 查询: input_top_logprobs (K tokens per position)
存储字段: teacher_topk_log_probs [T,K], teacher_topk_indices [T,K]

损失 (Reverse KL over K+1 bins):
D_KL(π_θ^{K+1} || π_teacher^{K+1}) = Σ π_θ^(k) (log π_θ^(k) - log π_teacher^(k))

Tail bin:
log p_tail = log(1 - exp(logsumexp(log p_1, ..., log p_K)))
```

**启动**:
```bash
cd slime
bash ../openclaw-opd/run_qwen3_4b_openclaw_opd_topk.sh
```

**关键参数**:
```bash
--loss-type custom_loss \
--custom-loss-function-path topk_distillation_loss.topk_distillation_loss_function \
--distill-topk 50 \
--disable-compute-advantages-and-returns \
--entropy-coef 0.00
```

### 2. 完全异步架构

**4 组件独立循环**:
- Agent 服务: 持续响应请求
- Rollout 收集: 后台收集轨迹
- PRM 评判: 并发评估质量
- 策略训练: 异步更新权重

**无阻塞设计**:
- 模型服务不等待训练
- 训练不阻塞新对话
- PRM 评估与对话并发

**优雅权重更新**:
- 提交在更新期间暂停
- 更新完成后恢复
- 无数据损坏

### 3. 自托管和隐私

**完全本地**:
- 模型、PRM、训练全在本地
- 对话数据不离开系统
- 零外部 API Key

**硬件要求**:
- 默认: 8× GPUs
- 可配置: `NUM_GPUS`, `ACTOR_GPUS`, `ROLLOUT_GPUS`, `PRM_GPUS`
- 软件: CUDA 12.9, Python 3.12

### 4. 自动训练信号提取

**消息分类**:
- 自动识别 main-line vs. side
- 无需手动标注

**Next-state 信号**:
- 下一条用户/环境消息作为自然"next state"
- PRM 基于 next-state 评分

**多数投票**:
- m 次独立 PRM 评估
- 鲁棒性评分

### 5. 生产工程特性

**Session 感知训练**:
- 多轮对话按 session 追踪
- 保持轮次顺序

**At-least-one 保证**:
- 每个 session 至少 1 个有效样本

**Hint 质量过滤 (OPD)**:
- 仅选择最长、最有信息量的 hint
- 丢弃平凡 hint

**Teacher log-prob 优化 (OPD)**:
- 仅计算响应后缀 log-probs
- 减少峰值内存

**记录和调试**:
- 所有对话和 PRM 评估记录到 JSONL
- 便于分析和复现

### 6. 方法对比

| 维度 | Binary RL | OPD | Combined |
|---|---|---|---|
| 信号类型 | 评价性 (好/坏) | 方向性 | 评价性 + 方向性 |
| 优势 | 序列级标量 | Token 级方向性 | 混合序列和 token 级 |
| 密度 | 所有评分轮次 | 仅 hint 接受轮次 | 所有评分轮次 |
| 反馈类型 | 用户/环境 | 显式纠正 | 隐式和显式反馈 |
| 信号丰富度 | 每样本 1 标量 | 每 token 1 值 | 每 token 1 值 |

### 7. 配置灵活性

**环境变量**:
```bash
NUM_GPUS=8              # 总 GPU 数
ACTOR_GPUS=4            # 训练 actor GPU
ROLLOUT_GPUS=2          # Rollout GPU
PRM_GPUS=2              # PRM GPU
HF_CKPT=path/to/model   # 基础模型路径
PRM_MODEL_PATH=path     # 奖励模型路径
SAVE_CKPT=path          # 保存路径
SGLANG_API_KEY=key      # API Key
```

### 8. OpenClaw 集成

**配置示例**:
```json
{
  "models": {
    "providers": {
      "qwen": {
        "baseUrl": "http://<HOST_IP>:30000/v1",
        "apiKey": "apiKey",
        "api": "openai-completions",
        "models": [
          {
            "id": "qwen3-4b",
            "name": "Qwen3 4B",
            "reasoning": true,
            "input": ["text"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 32768,
            "maxTokens": 8192
          }
        ]
      }
    }
  }
}
```

**工作流**:
1. 启动 RL Server: `bash run_qwen3_4b_openclaw_rl.sh`
2. 配置 OpenClaw 指向 RL Server
3. 开始对话，系统自动训练
# apps/api/services/agent_learning.py
class AgentLearningService:
    """类似 OpenClaw-RL 的异步学习服务"""

    async def start_learning_session(self, workspace_id: str, agent_id: str):
        """启动学习会话"""
        session = LearningSession(
            workspace_id=workspace_id,
            agent_id=agent_id,
            mode="async"  # 异步模式
        )
        await self._spawn_rollout_collector(session)
        await self._spawn_reward_evaluator(session)
        return session

    async def collect_feedback(self, session_id: str, interaction: Interaction):
        """收集用户交互反馈（类似 next-state 信号）"""
        # 用户点赞/点踩
        # Config 部署成功/失败
        # Runbook 执行结果
        pass

    async def train_policy(self, session_id: str):
        """后台训练策略（不阻塞服务）"""
        pass
```

### 2. 对话即训练的反馈机制
**借鉴点**: 从日常对话自动提取训练信号

**应用场景**:
- ClawButler Web 的用户反馈（👍/👎）
- Config Safety 部署后的成功/失败信号
- Template 部署的兼容性检查结果

**实现建议**:
```python
# apps/api/models/feedback_signal.py
class FeedbackSignal(Base):
    __tablename__ = "feedback_signals"

    id = Column(UUID, primary_key=True)
    session_id = Column(UUID)
    turn_index = Column(Integer)
    signal_type = Column(Enum("thumbs_up", "thumbs_down", "deployment_success", "deployment_failure"))
    next_state = Column(JSON)  # 类似 OpenClaw-RL 的 next-state
    reward_score = Column(Float)  # PRM 评分
    created_at = Column(DateTime)

# apps/api/services/feedback_learning.py
class FeedbackLearningService:
    async def process_user_feedback(self, interaction_id: str, feedback: str):
        """处理用户反馈，转换为训练信号"""
        # 类似 OpenClaw-RL 的 PRM 评判
        reward = await self._evaluate_with_prm(interaction, feedback)
        await self._submit_training_sample(interaction, reward)
```

### 3. 多数投票的鲁棒评分
**借鉴点**: PRM 多次独立评估 + 多数投票

**应用场景**:
- Config Safety 的语义 diff 质量评估
- Template 兼容性检查的多维度验证
- Runbook 执行结果的多指标评分

**实现建议**:
```python
# apps/api/services/quality_evaluation.py
class QualityEvaluationService:
    async def evaluate_config_diff(self, diff: ConfigDiff, m: int = 5) -> float:
        """类似 OpenClaw-RL 的多数投票评分"""
        votes = await asyncio.gather(*[
            self._single_evaluation(diff) for _ in range(m)
        ])
        # votes: [+1, +1, -1, +1, 0] → 多数投票 → +1
        return self._majority_vote(votes)

    def _majority_vote(self, votes: List[int]) -> int:
        """多数投票"""
        from collections import Counter
        return Counter(votes).most_common(1)[0][0]
```

### 4. Hindsight Hint 提取（OPD 模式）
**借鉴点**: 从事后反馈提取改进建议

**应用场景**:
- Config Safety 部署失败后的根因分析
- Template 部署错误的修复建议
- Runbook 执行失败的优化提示

**实现建议**:
```python
# apps/api/services/hindsight_learning.py
class HindsightLearningService:
    async def extract_hint_from_failure(self, deployment_id: str) -> Optional[str]:
        """类似 OpenClaw-RL OPD 的 hint 提取"""
        deployment = await self._get_deployment(deployment_id)
        if deployment.status != "failed":
            return None

        # 多次 LLM 调用提取 hint
        hints = await asyncio.gather(*[
            self._llm_extract_hint(deployment) for _ in range(5)
        ])

        # 选择最长的非平凡 hint
        valid_hints = [h for h in hints if len(h) > 20]  # 过滤平凡 hint
        return max(valid_hints, key=len) if valid_hints else None

    async def apply_hint_to_next_deployment(self, hint: str, template_id: str):
        """将 hint 应用到下次部署"""
        # 类似 OPD 的 teacher signal
        pass
```

### 5. 异步组件架构
**借鉴点**: 4 组件独立循环的设计

**应用场景**:
- ClawButler 的 Runbook 调度器（异步执行）
- Config Safety 的 drift 检测（后台扫描）
- Federation 的 A2A 调用（异步路由）

**实现建议**:
```python
# apps/api/services/async_orchestrator.py
class AsyncOrchestrator:
    """类似 OpenClaw-RL 的异步编排器"""

    def __init__(self):
        self.runbook_executor = RunbookExecutor()  # 类似 Agent 服务
        self.drift_detector = DriftDetector()      # 类似 Rollout 收集
        self.quality_evaluator = QualityEvaluator()  # 类似 PRM 评判
        self.policy_trainer = PolicyTrainer()      # 类似策略训练

    async def start_all(self):
        """启动所有异步循环"""
        await asyncio.gather(
            self.runbook_executor.run(),
            self.drift_detector.run(),
            self.quality_evaluator.run(),
            self.policy_trainer.run()
        )
```

### 6. Session 感知的状态管理
**借鉴点**: 多轮对话的 session 追踪

**应用场景**:
- ClawButler 的多步 Runbook 执行追踪
- Config Safety 的多版本快照链
- Template 部署的多阶段状态

**实现建议**:
```python
# apps/api/models/execution_session.py
class ExecutionSession(Base):
    __tablename__ = "execution_sessions"

    id = Column(UUID, primary_key=True)
    runbook_id = Column(UUID, ForeignKey("runbooks.id"))
    turns = relationship("ExecutionTurn", order_by="ExecutionTurn.turn_index")

class ExecutionTurn(Base):
    __tablename__ = "execution_turns"

    id = Column(UUID, primary_key=True)
    session_id = Column(UUID, ForeignKey("execution_sessions.id"))
    turn_index = Column(Integer)
    step_name = Column(String)
    status = Column(Enum("pending", "running", "completed", "failed"))
    next_state = Column(JSON)  # 类似 OpenClaw-RL 的 next-state
    reward_score = Column(Float)
```

### 7. At-least-one 保证机制
**借鉴点**: 每个 session 至少贡献 1 个有效样本

**应用场景**:
- ClawButler 的 Runbook 执行至少记录 1 个有效事件
- Config Safety 快照至少保留 1 个有效版本
- Template 部署至少生成 1 个有效交付物

**实现建议**:
```python
# apps/api/services/execution_tracker.py
class ExecutionTracker:
    async def ensure_at_least_one_event(self, session_id: str):
        """类似 OpenClaw-RL 的 at-least-one 保证"""
        events = await self._get_session_events(session_id)
        if len(events) == 0:
            # 创建一个默认事件
            await self._create_default_event(session_id)
        elif len(events) == 1 and events[0].is_last_turn:
            # 如果只有最后一轮，也要保留
            events[0].loss_mask = 1
```

### 8. 自托管和隐私优先
**借鉴点**: 完全本地化的训练和推理

**应用场景**:
- ClawButler 的私有化部署
- 企业内网的 Agent 训练
- 敏感数据的本地处理

**实现建议**:
```yaml
# docker-compose.learning.yml
services:
  clawbutler-learning-server:
    image: clawbutler/learning-server
    environment:
      - MODE=self_hosted  # 自托管模式
      - NO_EXTERNAL_API=true  # 禁用外部 API
      - LOCAL_MODEL_PATH=/models/qwen3-4b
    volumes:
      - ./models:/models
      - ./training_data:/data
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 8  # 类似 OpenClaw-RL 的 8 GPU 配置
```

### 9. 记录和可观测性
**借鉴点**: 所有对话和评估记录到 JSONL

**应用场景**:
- ClawButler 的审计日志
- Runbook 执行轨迹
- Config Safety 变更历史

**实现建议**:
```python
# apps/api/services/audit_logger.py
class AuditLogger:
    """类似 OpenClaw-RL 的 JSONL 记录"""

    async def log_interaction(self, interaction: Interaction):
        """记录交互到 JSONL"""
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "session_id": interaction.session_id,
            "turn_index": interaction.turn_index,
            "user_message": interaction.user_message,
            "agent_response": interaction.agent_response,
            "reward_score": interaction.reward_score,
            "next_state": interaction.next_state
        }
        async with aiofiles.open("audit.jsonl", "a") as f:
            await f.write(json.dumps(log_entry) + "\n")
```

### 10. 两阶段 Roadmap 策略
**借鉴点**: Track 1（小规模个性化）+ Track 2（大规模通用）

**应用场景**:
- ClawButler 的产品演进策略
- Track 1: Workspace 级个性化 Agent
- Track 2: 跨 Workspace 的通用 Agent 优化

**实现建议**:
```python
# docs/roadmap/learning-roadmap.md
"""
## Track 1 — Workspace 级个性化 Agent
✅ 异步学习框架
✅ 用户反馈收集
⬜ 多模态反馈（文本 + 操作日志）
⬜ 跨 Agent 知识迁移

## Track 2 — 跨 Workspace 通用优化
✅ 可扩展训练基础设施
⬜ 联邦学习支持
⬜ 云端训练服务
"""
```

## 总结

OpenClaw-RL 提供了一个突破性的 Agent 训练范式，其核心价值在于：

1. **完全异步**: 4 组件独立循环，无阻塞设计
2. **对话即训练**: 从日常对话自动提取训练信号
3. **个性化**: 根据用户反馈持续优化
4. **自托管**: 完全本地化，零外部 API
5. **生产就绪**: Session 感知、at-least-one 保证、优雅权重更新

对 ClawButler 而言，可以借鉴其异步学习架构、反馈信号提取机制、多数投票评分，构建 Workspace 级个性化 Agent 训练系统，结合 ClawButler 的 Config Safety 和 Runbook 特性，实现"越用越懂你"的智能控制平面。
