> https://github.com/BlockRunAI/ClawRouter

# ClawRouter (5,352 stars)

## 问题与解决方案

OpenClaw 将所有请求发送到同一模型，小任务也调用大模型导致成本浪费。ClawRouter 是 Agent 原生的 LLM 路由器，通过 15 维度评分算法在 <1ms 内将请求路由到最合适的模型，支持 41+ 模型，使用 x402 协议的 USDC 非托管支付（Base/Solana），节省 74-100% 成本。

## 关键特性

- **本地路由引擎** — 15 维度加权评分（复杂度/推理需求/代码生成等），<1ms 延迟，零外部 API 调用，100% 本地决策
- **四种路由策略** — eco（最便宜）/auto（平衡，默认）/premium（最高质量）/free（零成本），通过 `/model <profile>` 切换
- **41+ 模型支持** — 覆盖 SIMPLE/MEDIUM/COMPLEX/REASONING 四个层级，eco 模式下 SIMPLE 任务使用 nvidia/gpt-oss-120b（免费）
- **图像生成集成** — `/imagegen` 命令支持 5 个模型（nano-banana/banana-pro/dall-e-3/gpt-image/flux），价格 $0.02-$0.10/张
- **x402 非托管支付** — USDC Hackathon Agentic Commerce 获奖项目，Base/Solana 链上微支付，用户自持私钥，$5 可支持数千次请求
- **OpenClaw 插件** — 一键安装 `curl -fsSL https://blockrun.ai/ClawRouter-update | bash`，自动替换默认模型为 `blockrun/auto`

<!-- lastCommit: 699a190 -->
