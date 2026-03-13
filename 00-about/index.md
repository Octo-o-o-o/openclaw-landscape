# OpenClaw 生态项目研究索引

> 调研时间：2026-03-11
> > 总计调研：**128 个项目**（含排除项目清单 160+）

## 目录结构

```
├── 00-index.md                 # 本文件
├── 00-excluded-projects.md     # 已检查但不直接相关的项目
├── 01-official/   (7)           # OpenClaw 官方项目
├── 02-runtime/    (16)          # 替代实现/运行时
├── 03-memory/     (11)          # 记忆系统
├── 04-security/   (7)           # 安全工具
├── 05-dashboard-and-monitoring/  (16)          # 仪表板/监控
├── 06-deployment/     (6)           # 部署工具
├── 07-china-ecosystem/      (19)          # 中国生态
├── 08-skills-and-resources/     (14)          # 技能/模板/资源
├── 09-protocols/   (4)           # 协议（A2A/MCP/ACP）
├── 10-ops/        (3)           # 运维工具
├── 11-voice/      (2)           # 语音
├── 12-routing-and-cost/     (6)           # LLM 路由/成本优化
├── 13-orchestration/ (9)        # 多 Agent 编排
├── 14-clients/     (5)           # 桌面/移动客户端
└── 15-other/      (10)          # 其他
```

---

## A. OpenClaw 官方项目

| 项目 | Stars | 文件 |
|------|-------|------|
| openclaw/openclaw | 299,704 | [openclaw-core.md](../categories/01-official/openclaw-core.md) |
| openclaw/clawhub | 5,292 | [clawhub.md](../categories/01-official/clawhub.md) |
| openclaw/skills | 2,524 | [skills.md](../categories/01-official/skills.md) |
| openclaw/lobster | 795 | [lobster.md](../categories/01-official/lobster.md) |
| openclaw/acpx | 719 | [acpx.md](../categories/01-official/acpx.md) |
| openclaw/openclaw-ansible | 481 | [openclaw-ansible.md](../categories/01-official/openclaw-ansible.md) |
| 16 个小型项目 | <519 | [small-projects.md](../categories/01-official/small-projects.md) |

## B. 替代实现/运行时

| 项目 | Stars | 文件 |
|------|-------|------|
| zeroclaw-labs/zeroclaw | 25,853 | [zeroclaw.md](../categories/02-runtime/zeroclaw.md) |
| qwibitai/nanoclaw | 21,451 | [nanoclaw.md](../categories/02-runtime/nanoclaw.md) |
| cloudflare/moltworker | 9,558 | [moltworker.md](../categories/02-runtime/moltworker.md) |
| nearai/ironclaw | 9,101 | [ironclaw.md](../categories/02-runtime/ironclaw.md) |
| memovai/mimiclaw | 4,260 | [mimiclaw.md](../categories/02-runtime/mimiclaw.md) |
| moltis-org/moltis | 2,077 | [moltis.md](../categories/02-runtime/moltis.md) |
| tnm/zclaw | 1,873 | [zclaw.md](../categories/02-runtime/zclaw.md) |
| poco-ai/poco-claw | 1,131 | [poco-claw.md](../categories/02-runtime/poco-claw.md) |
| mosaxiv/clawlet | 657 | [clawlet.md](../categories/02-runtime/clawlet.md) |
| sachaa/openbrowserclaw | 558 | [openbrowserclaw.md](../categories/02-runtime/openbrowserclaw.md) |
| voocel/openclaw-mini | 555 | [openclaw-mini.md](../categories/02-runtime/openclaw-mini.md) |
| stellarlinkco/myclaw | 236 | [myclaw.md](../categories/02-runtime/myclaw.md) |
| clawdotnet/openclaw.net | 84 | [openclaw-net.md](../categories/02-runtime/openclaw-net.md) |
| opencrust-org/opencrust | 49 | [opencrust.md](../categories/02-runtime/opencrust.md) |
| harperaa/bastionclaw | 24 | [bastionclaw.md](../categories/02-runtime/bastionclaw.md) |
| creeper-scr/claw-kernel | 2 | [claw-kernel.md](../categories/02-runtime/claw-kernel.md) |

## C. 记忆系统

| 项目 | Stars | 文件 |
|------|-------|------|
| NevaMind-AI/memU | 12,811 | [memU.md](../categories/03-memory/memU.md) |
| EverMind-AI/EverMemOS | 2,520 | [evermemos.md](../categories/03-memory/evermemos.md) |
| CortexReach/memory-lancedb-pro | 2,030 | [memory-lancedb-pro.md](../categories/03-memory/memory-lancedb-pro.md) |
| supermemoryai/openclaw-supermemory | 579 | [supermemory.md](../categories/03-memory/supermemory.md) |
| oceanbase/powermem | 489 | [powermem.md](../categories/03-memory/powermem.md) |
| dztabel-happy/openclaw-memory-fusion | 106 | [memory-fusion.md](../categories/03-memory/memory-fusion.md) |
| codesfly/openclaw-memory-final | 94 | [memory-final.md](../categories/03-memory/memory-final.md) |
| ktao732084/memory-supersystem | 64 | [memory-supersystem.md](../categories/03-memory/memory-supersystem.md) |
| duxiaoxiong/memu-engine | 46 | [memu-engine.md](../categories/03-memory/memu-engine.md) |
| coolmanns/12layer-memory | 31 | [12layer-memory.md](../categories/03-memory/12layer-memory.md) |
| jzOcb/memory-management | 29 | [memory-management.md](../categories/03-memory/memory-management.md) |

## D. 安全工具

| 项目 | Stars | 文件 |
|------|-------|------|
| Tencent/AI-Infra-Guard | 3,124 | [ai-infra-guard.md](../categories/04-security/ai-infra-guard.md) |
| slowmist/security-practice-guide | 1,659 | [security-practice-guide.md](../categories/04-security/security-practice-guide.md) |
| prompt-security/clawsec | 709 | [clawsec.md](../categories/04-security/clawsec.md) |
| knownsec/openclaw-security | 55 | [knownsec-security.md](../categories/04-security/knownsec-security.md) |
| yi-john-huang/secure-stack | 47 | [secure-stack.md](../categories/04-security/secure-stack.md) |
| UseAI-pro/skills-security | 25 | [skills-security.md](../categories/04-security/skills-security.md) |
| davidcrowe/gatewaystack-governance | 5 | [gatewaystack-governance.md](../categories/04-security/gatewaystack-governance.md) |

## E. 仪表板/监控

| 项目 | Stars | 文件 |
|------|-------|------|
| ringhyacinth/Star-Office-UI | 4,092 | [star-office-ui.md](../categories/05-dashboard-and-monitoring/star-office-ui.md) |
| builderz-labs/mission-control | 2,069 | [mission-control-builderz.md](../categories/05-dashboard-and-monitoring/mission-control-builderz.md) |
| abhi1693/mission-control | 1,957 | [mission-control-abhi.md](../categories/05-dashboard-and-monitoring/mission-control-abhi.md) |
| grp06/openclaw-studio | 1,549 | [openclaw-studio.md](../categories/05-dashboard-and-monitoring/openclaw-studio.md) |
| crshdn/mission-control | 1,319 | [mission-control-crshdn.md](../categories/05-dashboard-and-monitoring/mission-control-crshdn.md) |
| crabwise-ai/crabwalk | 859 | [crabwalk.md](../categories/05-dashboard-and-monitoring/crabwalk.md) |
| Curbob/LobsterBoard | 815 | [lobsterboard.md](../categories/05-dashboard-and-monitoring/lobsterboard.md) |
| carlosazaustre/tenacitOS | 689 | [tenacitos.md](../categories/05-dashboard-and-monitoring/tenacitos.md) |
| tugcantopaloglu/dashboard | 418 | [openclaw-dashboard-tugcan.md](../categories/05-dashboard-and-monitoring/openclaw-dashboard-tugcan.md) |
| mudrii/dashboard | 261 | [openclaw-dashboard-mudrii.md](../categories/05-dashboard-and-monitoring/openclaw-dashboard-mudrii.md) |
| WW-AI-Lab/openclaw-office | 209 | [openclaw-office.md](../categories/05-dashboard-and-monitoring/openclaw-office.md) |
| daggerhashimoto/openclaw-nerve | 178 | [openclaw-nerve.md](../categories/05-dashboard-and-monitoring/openclaw-nerve.md) |
| madrzak/vidclaw | 139 | [vidclaw.md](../categories/05-dashboard-and-monitoring/vidclaw.md) |
| video-db/openclaw-monitoring | 15 | [openclaw-monitoring.md](../categories/05-dashboard-and-monitoring/openclaw-monitoring.md) |
| openclawq/clawmonitor | 32 | [clawmonitor.md](../categories/05-dashboard-and-monitoring/clawmonitor.md) |
| JiangAgentLabs/Agent-Control | 1 | [agent-control.md](../categories/05-dashboard-and-monitoring/agent-control.md) |

## F. 部署工具

| 项目 | Stars | 文件 |
|------|-------|------|
| phioranex/openclaw-docker | 528 | [phioranex-docker.md](../categories/06-deployment/phioranex-docker.md) |
| chrysb/alphaclaw | 481 | [alphaclaw.md](../categories/06-deployment/alphaclaw.md) |
| miaoxworld/OpenClawInstaller | 2,978 | [openclawinstaller.md](../categories/06-deployment/openclawinstaller.md) |
| coollabsio/openclaw | 287 | [coollabsio-openclaw.md](../categories/06-deployment/coollabsio-openclaw.md) |
| serhanekicii/openclaw-helm | 149 | [openclaw-helm.md](../categories/06-deployment/openclaw-helm.md) |
| tsconfigdotjson/lobsterd | 25 | [lobsterd.md](../categories/06-deployment/lobsterd.md) |

## G. 中国生态

| 项目 | Stars | 文件 |
|------|-------|------|
| m1heng/clawdbot-feishu | 4,189 | [clawdbot-feishu.md](../categories/07-china-ecosystem/clawdbot-feishu.md) |
| justlovemaki/docker-cn-im | 3,124 | [openclaw-docker-cn-im.md](../categories/07-china-ecosystem/openclaw-docker-cn-im.md) |
| 1186258278/ChineseTranslation | 2,934 | [openclaw-chinese-translation.md](../categories/07-china-ecosystem/openclaw-chinese-translation.md) |
| clawdbot-ai/awesome-skills-zh | 2,902 | [awesome-skills-zh.md](../categories/07-china-ecosystem/awesome-skills-zh.md) |
| BytePioneer-AI/openclaw-china | 2,790 | [openclaw-china.md](../categories/07-china-ecosystem/openclaw-china.md) |
| xianyu110/awesome-tutorial | 2,179 | [awesome-tutorial.md](../categories/07-china-ecosystem/awesome-tutorial.md) |
| mengjian-github/openclaw101 | 2,011 | [openclaw101.md](../categories/07-china-ecosystem/openclaw101.md) |
| DingTalk-Real-AI/connector | 1,603 | [dingtalk-connector.md](../categories/07-china-ecosystem/dingtalk-connector.md) |
| AlexAnys/awesome-usecases-zh | 1,553 | [awesome-usecases-zh.md](../categories/07-china-ecosystem/awesome-usecases-zh.md) |
| freestylefly/openclaw-wechat | 1,345 | [openclaw-wechat.md](../categories/07-china-ecosystem/openclaw-wechat.md) |
| soimy/channel-dingtalk | 1,267 | [openclaw-channel-dingtalk.md](../categories/07-china-ecosystem/openclaw-channel-dingtalk.md) |
| xianyu110/clawbot | 856 | [clawbot.md](../categories/07-china-ecosystem/clawbot.md) |
| yeuxuan/openclaw-docs | 533 | [openclaw-docs.md](../categories/07-china-ecosystem/openclaw-docs.md) |
| AlexAnys/openclaw-feishu | 522 | [openclaw-feishu.md](../categories/07-china-ecosystem/openclaw-feishu.md) |
| sunnoy/wecom-plugin | 433 | [wecom-plugin.md](../categories/07-china-ecosystem/wecom-plugin.md) |
| 11haonb/wecom-plugin | 95 | [wecom-plugin-2.md](../categories/07-china-ecosystem/wecom-plugin-2.md) |
| AIPMAndy/awesome-skills-CN | 51 | [awesome-skills-cn.md](../categories/07-china-ecosystem/awesome-skills-cn.md) |
| IanShaw027/wemp-operator | 46 | [wemp-operator.md](../categories/07-china-ecosystem/wemp-operator.md) |
| aliramw/dingtalk-ai-table | 46 | [dingtalk-ai-table.md](../categories/07-china-ecosystem/dingtalk-ai-table.md) |

## H. 技能/模板/资源

| 项目 | Stars | 文件 |
|------|-------|------|
| VoltAgent/awesome-skills | 34,631 | [awesome-skills-voltagent.md](../categories/08-skills-and-resources/awesome-skills-voltagent.md) |
| hesamsheikh/awesome-usecases | 23,013 | [awesome-usecases.md](../categories/08-skills-and-resources/awesome-usecases.md) |
| davepoon/buildwithclaude | 2,565 | [buildwithclaude.md](../categories/08-skills-and-resources/buildwithclaude.md) |
| SumeLabs/clawra | 2,008 | [clawra.md](../categories/08-skills-and-resources/clawra.md) |
| LeoYeAI/master-skills | 1,391 | [openclaw-master-skills.md](../categories/08-skills-and-resources/openclaw-master-skills.md) |
| SamurAIGPT/awesome-openclaw | 778 | [awesome-openclaw.md](../categories/08-skills-and-resources/awesome-openclaw.md) |
| unbrowse-ai/unbrowse | 485 | [unbrowse.md](../categories/08-skills-and-resources/unbrowse.md) |
| sundial-org/awesome-skills | 427 | [sundial-awesome-skills.md](../categories/08-skills-and-resources/sundial-awesome-skills.md) |
| ythx-101/x-tweet-fetcher | 407 | [x-tweet-fetcher.md](../categories/08-skills-and-resources/x-tweet-fetcher.md) |
| sharbelxyz/x-bookmarks | 241 | [x-bookmarks.md](../categories/08-skills-and-resources/x-bookmarks.md) |
| blessonism/search-skills | 232 | [search-skills.md](../categories/08-skills-and-resources/search-skills.md) |
| oh-ashen-one/reddit-growth | 109 | [reddit-growth.md](../categories/08-skills-and-resources/reddit-growth.md) |
| destinyfrancis/knowledge-distiller | 43 | [knowledge-distiller.md](../categories/08-skills-and-resources/knowledge-distiller.md) |
| pepicrft/plugin-vault | 41 | [plugin-vault.md](../categories/08-skills-and-resources/plugin-vault.md) |

## I. 协议（A2A / MCP / ACP）

| 项目 | Stars | 文件 |
|------|-------|------|
| win4r/a2a-gateway | 162 | [a2a-gateway.md](../categories/09-protocols/a2a-gateway.md) |
| 8421bit/MiniClaw | 63 | [miniclaw.md](../categories/09-protocols/miniclaw.md) |
| freema/openclaw-mcp | 60 | [openclaw-mcp.md](../categories/09-protocols/openclaw-mcp.md) |
| androidStern/mcp-adapter | 27 | [mcp-adapter.md](../categories/09-protocols/mcp-adapter.md) |

## J. 运维工具

| 项目 | Stars | 文件 |
|------|-------|------|
| LeoYeAI/openclaw-guardian | 938 | [openclaw-guardian.md](../categories/10-ops/openclaw-guardian.md) |
| LeoYeAI/openclaw-backup | 917 | [openclaw-backup.md](../categories/10-ops/openclaw-backup.md) |
| digitalknk/openclaw-runbook | 894 | [openclaw-runbook.md](../categories/10-ops/openclaw-runbook.md) |

## K. 语音

| 项目 | Stars | 文件 |
|------|-------|------|
| yuga-hashimoto/openclaw-assistant | 157 | [openclaw-assistant.md](../categories/11-voice/openclaw-assistant.md) |
| Purple-Horizons/openclaw-voice | 66 | [openclaw-voice.md](../categories/11-voice/openclaw-voice.md) |

## L. LLM 路由/成本优化

| 项目 | Stars | 文件 |
|------|-------|------|
| BlockRunAI/ClawRouter | 5,352 | [clawrouter.md](../categories/12-routing-and-cost/clawrouter.md) |
| mnfst/manifest | 3,733 | [manifest.md](../categories/12-routing-and-cost/manifest.md) |
| badrisnarayanan/antigravity | 3,107 | [antigravity-proxy.md](../categories/12-routing-and-cost/antigravity-proxy.md) |
| linuxhsj/zero-token | 1,450 | [openclaw-zero-token.md](../categories/12-routing-and-cost/openclaw-zero-token.md) |
| junhoyeo/tokscale | 1,090 | [tokscale.md](../categories/12-routing-and-cost/tokscale.md) |
| zscole/model-hierarchy-skill | 329 | [model-hierarchy-skill.md](../categories/12-routing-and-cost/model-hierarchy-skill.md) |

## M. 多 Agent 编排

| 项目 | Stars | 文件 |
|------|-------|------|
| RightNow-AI/openfang | 13,621 | [openfang.md](../categories/13-orchestration/openfang.md) |
| HKUDS/ClawWork | 6,988 | [clawwork.md](../categories/13-orchestration/clawwork.md) |
| cft0808/edict | 7,636 | [edict.md](../categories/13-orchestration/edict.md) |
| snarktank/antfarm | 2,104 | [antfarm.md](../categories/13-orchestration/antfarm.md) |
| heshengtao/super-agent-party | 1,834 | [super-agent-party.md](../categories/13-orchestration/super-agent-party.md) |
| alibaba/hiclaw | 1,537 | [hiclaw.md](../categories/13-orchestration/hiclaw.md) |
| Gen-Verse/OpenClaw-RL | 1,311 | [openclaw-rl.md](../categories/13-orchestration/openclaw-rl.md) |
| Arvincreator/project-golem | 270 | [project-golem.md](../categories/13-orchestration/project-golem.md) |
| Mayuqi-crypto/InterSystem | 50 | [intersystem.md](../categories/13-orchestration/intersystem.md) |
| trohitg/MachinaOS | 18 | [machinaos.md](../categories/13-orchestration/machinaos.md) |

## N. 桌面/移动客户端

| 项目 | Stars | 文件 |
|------|-------|------|
| ValueCell-ai/ClawX | 3,454 | [clawx.md](../categories/14-clients/clawx.md) |
| openakita/openakita | 1,114 | [openakita.md](../categories/14-clients/openakita.md) |
| mithun50/openclaw-termux | 563 | [openclaw-termux.md](../categories/14-clients/openclaw-termux.md) |
| rohanarun/phoneclaw | 392 | [phoneclaw.md](../categories/14-clients/phoneclaw.md) |
| zhixianio/botdrop-android | 303 | [botdrop-android.md](../categories/14-clients/botdrop-android.md) |

## O. 其他

| 项目 | Stars | 文件 |
|------|-------|------|
| HKUDS/nanobot | 32,020 | [nanobot.md](../categories/15-other/nanobot.md) |
| openimsdk/open-im-server | 15,775 | [openimsdk.md](../categories/15-other/openimsdk.md) |
| volcengine/OpenViking | 5,671 | [openviking.md](../categories/15-other/openviking.md) |
| ComposioHQ/secure-openclaw | 1,358 | [secure-openclaw.md](../categories/15-other/secure-openclaw.md) |
| 195440/nof1.ai | 569 | [nof1-ai.md](../categories/15-other/nof1-ai.md) |
| pjasicek/OpenClaw | 448 | [pjasicek-openclaw.md](../categories/15-other/pjasicek-openclaw.md) |
| kevin-liu-robot/EQtreader | 54 | [eqtreader.md](../categories/15-other/eqtreader.md) |
| ZiyaZhang/market-sentry | 31 | [market-sentry.md](../categories/15-other/market-sentry.md) |
| chenmuwen0930/snowtrace | 27 | [snowtrace.md](../categories/15-other/snowtrace.md) |

---

→ 已检查但不直接相关的项目：[00-excluded-projects.md](excluded-projects.md)（160+ 个）
