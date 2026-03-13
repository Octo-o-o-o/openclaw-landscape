> https://github.com/Gen-Verse/OpenClaw-RL

# Gen-Verse/OpenClaw-RL

## Basic Info

- **GitHub Stars**: 1,311
- **Project URL**: https://github.com/Gen-Verse/OpenClaw-RL
- **Blog Page**: https://yinjjiew.github.io/projects/openclawrl
- **Latest Version**: v1 (2026/2/26)
- **License**: MIT
- **Tech Stack**: Python 3.12, CUDA 12.9, Slime RL Framework, SGLang, OpenClaw

## Problem & Solution

### Core Problem
Challenges facing traditional AI Agent system training:
1. **High data collection cost**: Requires pre-collecting large labeled datasets
2. **Batch training mode**: Centralized batch processing training, unable to optimize in real time
3. **Insufficient personalization**: Generic models struggle to adapt to individual usage habits
4. **Sparse feedback signals**: Lack of effective training signal extraction mechanisms
5. **Production deployment disconnect**: Training and serving are two separate systems

### Solution
OpenClaw-RL proposes a **fully asynchronous reinforcement learning framework** that automatically trains personalized Agents through daily conversations:

**Core Innovations**:
- **Zero API Keys**: Fully self-hosted, no external APIs needed
- **Fully Asynchronous**: 4 components run independently (Agent serving, Rollout collection, PRM judging, Policy training)
- **Conversation as Training**: Intercepts real-time multi-turn conversations and automatically converts them to training signals
- **Background Optimization**: Model trains in the background while serving requests, without interrupting usage
- **Personalization**: Continuously optimizes based on user feedback, becoming smarter over time

**Slogan**: "Train a personalized agent simply by talking to it."

## Core Architecture

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    OpenClaw-RL Async Architecture                 │
│                                                                   │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────┐   │
│  │   OpenClaw   │─────►│  RL Server   │◄─────│     User     │   │
│  │   Gateway    │ API  │  (FastAPI)   │ WS   │ Conversations│   │
│  └──────────────┘      └──────┬───────┘      └──────────────┘   │
│                               │                                   │
│                               │ Async submit                      │
│                               ▼                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              4-Component Async Loop                        │   │
│  │                                                            │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │   │
│  │  │Agent Serving│  │   Rollout   │  │ PRM Judging │       │   │
│  │  │  (SGLang)   │  │  Collector  │  │(Majority Vote)│      │   │
│  │  │  2 GPUs     │  │  2 GPUs     │  │  2 GPUs     │       │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘       │   │
│  │                                                            │   │
│  │  ┌─────────────────────────────────────────────────────┐  │   │
│  │  │           Policy Training (GRPO/OPD)                 │  │   │
│  │  │           4 GPUs                                     │  │   │
│  │  └─────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### Technical Architecture

**1. RL Server (FastAPI)**
```python
# openclaw_api_server.py
# Responsibilities:
# - Acts as OpenAI-compatible API proxy
# - Intercepts multi-turn conversations
# - Classifies main-line vs. side messages
# - Triggers PRM judging
# - Submits training samples
```

**2. Rollout Collector**
```python
# openclaw_rollout.py
# Responsibilities:
# - Asynchronously collects conversation trajectories
# - Bridges API Server <-> SLIME Trainer
# - Manages session state
# - Guarantees at-least-one sample
```

**3. PRM Judge**
```
# Responsibilities:
# - Next-state-based scoring
# - Majority voting (m independent evaluations)
# - Outputs +1 (good) / -1 (bad) / 0 (neutral)
# - Asynchronous concurrent evaluation
```

**4. Policy Trainer (Slime)**
```
# Responsibilities:
# - PPO-style policy gradient
# - GRPO advantage estimation
# - Weight updates and checkpoint saving
# - Pauses submissions during training
```

### Data Flow

```
User message → API Server → Policy Model (SGLang) → Response + log_probs
                ↓
         Wait for next-state
                ↓
         PRM Judging (m votes) → scalar reward r
                ↓
         Rollout Collector → training sample
                ↓
         SLIME Trainer → policy update
                ↓
         New weights → SGLang reload
```

### Session Management

**Message Classification**:
- **Main-line**: Trainable main dialogue (user request -> Agent response)
- **Side**: Non-trainable side messages (system prompts, meta-dialogue)

**At-least-one Guarantee**:
- Each session contributes at least 1 valid training sample
- The last turn is excluded by default (no next-state), unless it's the only turn

**Session Tracking**:
- Multi-turn conversations grouped by session_id
- Maintains turn order
- Supports concurrent sessions

## Key Features

### 1. Two Learning Paradigms

#### Binary RL (GRPO)
**Signal Type**: Evaluative (good/bad)
**Advantage Computation**: Sequence-level scalar
**Feedback Type**: Implicit feedback (thumbs up/down, environment success/failure)
**Signal Density**: All scored turns

**Algorithm**:
```
Advantage Estimation (GRPO):
A_t = r, for all t in response tokens

Policy Gradient Loss (PPO-style):
rho_t = pi_theta(a_t | s_t) / pi_old(a_t | s_t)
L_pg = -E_t[min(rho_t A_t, clip(rho_t, 1-eps, 1+eps_high) * A_t)]

Total Loss:
L = L_pg + beta_KL * L_KL
```

**Parameters**:
- eps = 0.2 (clip lower bound)
- eps_high = 0.28 (clip upper bound)
- beta_KL = 0.02
- beta_ent = 0 (entropy bonus disabled)

**Launch**:
```bash
cd slime
bash ../openclaw-rl/run_qwen3_4b_openclaw_rl.sh
```

#### On-Policy Distillation (OPD)
**Signal Type**: Directional
**Advantage Computation**: Token-level directional
**Feedback Type**: Explicit correction ("you should check the file first")
**Signal Density**: Only turns with accepted hints

**Algorithm**:
```
Hindsight Hint Extraction:
1. Judge whether (response, next_state) is useful
2. m votes, each returning +1/-1 and optional hint
3. Select the longest non-trivial positive hint
4. If none, discard sample

Token-level OPD:
A_t = log pi_teacher(a_t | s + hint) - log pi_theta(a_t | s)

Training Loss:
L = L_pg + beta_KL * L_KL
```

**Launch**:
```bash
cd slime
bash ../openclaw-opd/run_qwen3_4b_openclaw_opd.sh
```

#### Top-K Logits Distillation (SDFT/SDPO-style)
**Extension**: Distills teacher top-K distribution rather than single tokens

**Algorithm**:
```
Teacher Query: input_top_logprobs (K tokens per position)
Storage Fields: teacher_topk_log_probs [T,K], teacher_topk_indices [T,K]

Loss (Reverse KL over K+1 bins):
D_KL(pi_theta^{K+1} || pi_teacher^{K+1}) = sum pi_theta^(k) (log pi_theta^(k) - log pi_teacher^(k))

Tail bin:
log p_tail = log(1 - exp(logsumexp(log p_1, ..., log p_K)))
```

**Launch**:
```bash
cd slime
bash ../openclaw-opd/run_qwen3_4b_openclaw_opd_topk.sh
```

**Key Parameters**:
```bash
--loss-type custom_loss \
--custom-loss-function-path topk_distillation_loss.topk_distillation_loss_function \
--distill-topk 50 \
--disable-compute-advantages-and-returns \
--entropy-coef 0.00
```

### 2. Fully Asynchronous Architecture

**4 Components with Independent Loops**:
- Agent serving: Continuously responds to requests
- Rollout collection: Background trajectory gathering
- PRM judging: Concurrent quality evaluation
- Policy training: Asynchronous weight updates

**Non-Blocking Design**:
- Model serving doesn't wait for training
- Training doesn't block new conversations
- PRM evaluation runs concurrently with conversations

**Graceful Weight Updates**:
- Submissions pause during updates
- Resumes after update completion
- No data corruption

### 3. Self-Hosting and Privacy

**Fully Local**:
- Model, PRM, training all run locally
- Conversation data never leaves the system
- Zero external API Keys

**Hardware Requirements**:
- Default: 8x GPUs
- Configurable: `NUM_GPUS`, `ACTOR_GPUS`, `ROLLOUT_GPUS`, `PRM_GPUS`
- Software: CUDA 12.9, Python 3.12

### 4. Automatic Training Signal Extraction

**Message Classification**:
- Automatically identifies main-line vs. side
- No manual labeling required

**Next-State Signals**:
- Next user/environment message serves as natural "next state"
- PRM scores based on next-state

**Majority Voting**:
- m independent PRM evaluations
- Robust scoring

### 5. Production Engineering Features

**Session-Aware Training**:
- Multi-turn conversations tracked by session
- Maintains turn order

**At-least-one Guarantee**:
- Each session yields at least 1 valid sample

**Hint Quality Filtering (OPD)**:
- Only selects the longest, most informative hints
- Discards trivial hints

**Teacher Log-Prob Optimization (OPD)**:
- Only computes log-probs for response suffixes
- Reduces peak memory

**Logging and Debugging**:
- All conversations and PRM evaluations logged to JSONL
- Easy to analyze and reproduce

### 6. Method Comparison

| Dimension | Binary RL | OPD | Combined |
|---|---|---|---|
| Signal type | Evaluative (good/bad) | Directional | Evaluative + Directional |
| Advantage | Sequence-level scalar | Token-level directional | Hybrid sequence and token-level |
| Density | All scored turns | Only hint-accepted turns | All scored turns |
| Feedback type | User/environment | Explicit correction | Implicit and explicit feedback |
| Signal richness | 1 scalar per sample | 1 value per token | 1 value per token |

### 7. Configuration Flexibility

**Environment Variables**:
```bash
NUM_GPUS=8              # Total GPUs
ACTOR_GPUS=4            # Training actor GPUs
ROLLOUT_GPUS=2          # Rollout GPUs
PRM_GPUS=2              # PRM GPUs
HF_CKPT=path/to/model   # Base model path
PRM_MODEL_PATH=path     # Reward model path
SAVE_CKPT=path          # Save path
SGLANG_API_KEY=key      # API Key
```

### 8. OpenClaw Integration

**Configuration Example**:
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

**Workflow**:
1. Start RL Server: `bash run_qwen3_4b_openclaw_rl.sh`
2. Configure OpenClaw to point to the RL Server
3. Start conversations; the system trains automatically

## Summary

OpenClaw-RL provides a breakthrough Agent training paradigm. Its core value lies in:

1. **Fully asynchronous**: 4 components with independent loops, non-blocking design
2. **Conversation as training**: Automatically extracts training signals from daily conversations
3. **Personalization**: Continuously optimizes based on user feedback
4. **Self-hosted**: Fully local, zero external APIs
5. **Production-ready**: Session-aware, at-least-one guarantee, graceful weight updates

<!-- lastCommit: 6a7050b -->
