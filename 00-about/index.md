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
| openclaw/openclaw | 299,704 | [openclaw-core.md](../categories-cn/01-官方项目/openclaw-core.md) |
| openclaw/clawhub | 5,292 | [clawhub.md](../categories-cn/01-官方项目/clawhub.md) |
| openclaw/skills | 2,524 | [skills.md](../categories-cn/01-官方项目/skills.md) |
| openclaw/lobster | 795 | [lobster.md](../categories-cn/01-官方项目/lobster.md) |
| openclaw/acpx | 719 | [acpx.md](../categories-cn/01-官方项目/acpx.md) |
| openclaw/openclaw-ansible | 481 | [openclaw-ansible.md](../categories-cn/01-官方项目/openclaw-ansible.md) |
| 16 个小型项目 | <519 | [small-projects.md](../categories-cn/01-官方项目/small-projects.md) |

## B. 替代实现/运行时

| 项目 | Stars | 文件 |
|------|-------|------|
| zeroclaw-labs/zeroclaw | 25,853 | [zeroclaw.md](../categories-cn/02-替代实现与运行时/zeroclaw.md) |
| qwibitai/nanoclaw | 21,451 | [nanoclaw.md](../categories-cn/02-替代实现与运行时/nanoclaw.md) |
| cloudflare/moltworker | 9,558 | [moltworker.md](../categories-cn/02-替代实现与运行时/moltworker.md) |
| nearai/ironclaw | 9,101 | [ironclaw.md](../categories-cn/02-替代实现与运行时/ironclaw.md) |
| memovai/mimiclaw | 4,260 | [mimiclaw.md](../categories-cn/02-替代实现与运行时/mimiclaw.md) |
| moltis-org/moltis | 2,077 | [moltis.md](../categories-cn/02-替代实现与运行时/moltis.md) |
| tnm/zclaw | 1,873 | [zclaw.md](../categories-cn/02-替代实现与运行时/zclaw.md) |
| poco-ai/poco-claw | 1,131 | [poco-claw.md](../categories-cn/02-替代实现与运行时/poco-claw.md) |
| mosaxiv/clawlet | 657 | [clawlet.md](../categories-cn/02-替代实现与运行时/clawlet.md) |
| sachaa/openbrowserclaw | 558 | [openbrowserclaw.md](../categories-cn/02-替代实现与运行时/openbrowserclaw.md) |
| voocel/openclaw-mini | 555 | [openclaw-mini.md](../categories-cn/02-替代实现与运行时/openclaw-mini.md) |
| stellarlinkco/myclaw | 236 | [myclaw.md](../categories-cn/02-替代实现与运行时/myclaw.md) |
| clawdotnet/openclaw.net | 84 | [openclaw-net.md](../categories-cn/02-替代实现与运行时/openclaw-net.md) |
| opencrust-org/opencrust | 49 | [opencrust.md](../categories-cn/02-替代实现与运行时/opencrust.md) |
| harperaa/bastionclaw | 24 | [bastionclaw.md](../categories-cn/02-替代实现与运行时/bastionclaw.md) |
| creeper-scr/claw-kernel | 2 | [claw-kernel.md](../categories-cn/02-替代实现与运行时/claw-kernel.md) |

## C. 记忆系统

| 项目 | Stars | 文件 |
|------|-------|------|
| NevaMind-AI/memU | 12,811 | [memU.md](../categories-cn/03-记忆系统/memU.md) |
| EverMind-AI/EverMemOS | 2,520 | [evermemos.md](../categories-cn/03-记忆系统/evermemos.md) |
| CortexReach/memory-lancedb-pro | 2,030 | [memory-lancedb-pro.md](../categories-cn/03-记忆系统/memory-lancedb-pro.md) |
| supermemoryai/openclaw-supermemory | 579 | [supermemory.md](../categories-cn/03-记忆系统/supermemory.md) |
| oceanbase/powermem | 489 | [powermem.md](../categories-cn/03-记忆系统/powermem.md) |
| dztabel-happy/openclaw-memory-fusion | 106 | [memory-fusion.md](../categories-cn/03-记忆系统/memory-fusion.md) |
| codesfly/openclaw-memory-final | 94 | [memory-final.md](../categories-cn/03-记忆系统/memory-final.md) |
| ktao732084/memory-supersystem | 64 | [memory-supersystem.md](../categories-cn/03-记忆系统/memory-supersystem.md) |
| duxiaoxiong/memu-engine | 46 | [memu-engine.md](../categories-cn/03-记忆系统/memu-engine.md) |
| coolmanns/12layer-memory | 31 | [12layer-memory.md](../categories-cn/03-记忆系统/12layer-memory.md) |
| jzOcb/memory-management | 29 | [memory-management.md](../categories-cn/03-记忆系统/memory-management.md) |

## D. 安全工具

| 项目 | Stars | 文件 |
|------|-------|------|
| Tencent/AI-Infra-Guard | 3,124 | [ai-infra-guard.md](../categories-cn/04-安全工具/ai-infra-guard.md) |
| slowmist/security-practice-guide | 1,659 | [security-practice-guide.md](../categories-cn/04-安全工具/security-practice-guide.md) |
| prompt-security/clawsec | 709 | [clawsec.md](../categories-cn/04-安全工具/clawsec.md) |
| knownsec/openclaw-security | 55 | [knownsec-security.md](../categories-cn/04-安全工具/knownsec-security.md) |
| yi-john-huang/secure-stack | 47 | [secure-stack.md](../categories-cn/04-安全工具/secure-stack.md) |
| UseAI-pro/skills-security | 25 | [skills-security.md](../categories-cn/04-安全工具/skills-security.md) |
| davidcrowe/gatewaystack-governance | 5 | [gatewaystack-governance.md](../categories-cn/04-安全工具/gatewaystack-governance.md) |

## E. 仪表板/监控

| 项目 | Stars | 文件 |
|------|-------|------|
| ringhyacinth/Star-Office-UI | 4,092 | [star-office-ui.md](../categories-cn/05-仪表板与监控/star-office-ui.md) |
| builderz-labs/mission-control | 2,069 | [mission-control-builderz.md](../categories-cn/05-仪表板与监控/mission-control-builderz.md) |
| abhi1693/mission-control | 1,957 | [mission-control-abhi.md](../categories-cn/05-仪表板与监控/mission-control-abhi.md) |
| grp06/openclaw-studio | 1,549 | [openclaw-studio.md](../categories-cn/05-仪表板与监控/openclaw-studio.md) |
| crshdn/mission-control | 1,319 | [mission-control-crshdn.md](../categories-cn/05-仪表板与监控/mission-control-crshdn.md) |
| crabwise-ai/crabwalk | 859 | [crabwalk.md](../categories-cn/05-仪表板与监控/crabwalk.md) |
| Curbob/LobsterBoard | 815 | [lobsterboard.md](../categories-cn/05-仪表板与监控/lobsterboard.md) |
| carlosazaustre/tenacitOS | 689 | [tenacitos.md](../categories-cn/05-仪表板与监控/tenacitos.md) |
| tugcantopaloglu/dashboard | 418 | [openclaw-dashboard-tugcan.md](../categories-cn/05-仪表板与监控/openclaw-dashboard-tugcan.md) |
| mudrii/dashboard | 261 | [openclaw-dashboard-mudrii.md](../categories-cn/05-仪表板与监控/openclaw-dashboard-mudrii.md) |
| WW-AI-Lab/openclaw-office | 209 | [openclaw-office.md](../categories-cn/05-仪表板与监控/openclaw-office.md) |
| daggerhashimoto/openclaw-nerve | 178 | [openclaw-nerve.md](../categories-cn/05-仪表板与监控/openclaw-nerve.md) |
| madrzak/vidclaw | 139 | [vidclaw.md](../categories-cn/05-仪表板与监控/vidclaw.md) |
| video-db/openclaw-monitoring | 15 | [openclaw-monitoring.md](../categories-cn/05-仪表板与监控/openclaw-monitoring.md) |
| openclawq/clawmonitor | 32 | [clawmonitor.md](../categories-cn/05-仪表板与监控/clawmonitor.md) |
| JiangAgentLabs/Agent-Control | 1 | [agent-control.md](../categories-cn/05-仪表板与监控/agent-control.md) |

## F. 部署工具

| 项目 | Stars | 文件 |
|------|-------|------|
| phioranex/openclaw-docker | 528 | [phioranex-docker.md](../categories-cn/06-部署工具/phioranex-docker.md) |
| chrysb/alphaclaw | 481 | [alphaclaw.md](../categories-cn/06-部署工具/alphaclaw.md) |
| miaoxworld/OpenClawInstaller | 2,978 | [openclawinstaller.md](../categories-cn/06-部署工具/openclawinstaller.md) |
| coollabsio/openclaw | 287 | [coollabsio-openclaw.md](../categories-cn/06-部署工具/coollabsio-openclaw.md) |
| serhanekicii/openclaw-helm | 149 | [openclaw-helm.md](../categories-cn/06-部署工具/openclaw-helm.md) |
| tsconfigdotjson/lobsterd | 25 | [lobsterd.md](../categories-cn/06-部署工具/lobsterd.md) |

## G. 中国生态

| 项目 | Stars | 文件 |
|------|-------|------|
| m1heng/clawdbot-feishu | 4,189 | [clawdbot-feishu.md](../categories-cn/07-中国生态/clawdbot-feishu.md) |
| justlovemaki/docker-cn-im | 3,124 | [openclaw-docker-cn-im.md](../categories-cn/07-中国生态/openclaw-docker-cn-im.md) |
| 1186258278/ChineseTranslation | 2,934 | [openclaw-chinese-translation.md](../categories-cn/07-中国生态/openclaw-chinese-translation.md) |
| clawdbot-ai/awesome-skills-zh | 2,902 | [awesome-skills-zh.md](../categories-cn/07-中国生态/awesome-skills-zh.md) |
| BytePioneer-AI/openclaw-china | 2,790 | [openclaw-china.md](../categories-cn/07-中国生态/openclaw-china.md) |
| xianyu110/awesome-tutorial | 2,179 | [awesome-tutorial.md](../categories-cn/07-中国生态/awesome-tutorial.md) |
| mengjian-github/openclaw101 | 2,011 | [openclaw101.md](../categories-cn/07-中国生态/openclaw101.md) |
| DingTalk-Real-AI/connector | 1,603 | [dingtalk-connector.md](../categories-cn/07-中国生态/dingtalk-connector.md) |
| AlexAnys/awesome-usecases-zh | 1,553 | [awesome-usecases-zh.md](../categories-cn/07-中国生态/awesome-usecases-zh.md) |
| freestylefly/openclaw-wechat | 1,345 | [openclaw-wechat.md](../categories-cn/07-中国生态/openclaw-wechat.md) |
| soimy/channel-dingtalk | 1,267 | [openclaw-channel-dingtalk.md](../categories-cn/07-中国生态/openclaw-channel-dingtalk.md) |
| xianyu110/clawbot | 856 | [clawbot.md](../categories-cn/07-中国生态/clawbot.md) |
| yeuxuan/openclaw-docs | 533 | [openclaw-docs.md](../categories-cn/07-中国生态/openclaw-docs.md) |
| AlexAnys/openclaw-feishu | 522 | [openclaw-feishu.md](../categories-cn/07-中国生态/openclaw-feishu.md) |
| sunnoy/wecom-plugin | 433 | [wecom-plugin.md](../categories-cn/07-中国生态/wecom-plugin.md) |
| 11haonb/wecom-plugin | 95 | [wecom-plugin-2.md](../categories-cn/07-中国生态/wecom-plugin-2.md) |
| AIPMAndy/awesome-skills-CN | 51 | [awesome-skills-cn.md](../categories-cn/07-中国生态/awesome-skills-cn.md) |
| IanShaw027/wemp-operator | 46 | [wemp-operator.md](../categories-cn/07-中国生态/wemp-operator.md) |
| aliramw/dingtalk-ai-table | 46 | [dingtalk-ai-table.md](../categories-cn/07-中国生态/dingtalk-ai-table.md) |

## H. 技能/模板/资源

| 项目 | Stars | 文件 |
|------|-------|------|
| VoltAgent/awesome-skills | 34,631 | [awesome-skills-voltagent.md](../categories-cn/08-技能模板与资源/awesome-skills-voltagent.md) |
| hesamsheikh/awesome-usecases | 23,013 | [awesome-usecases.md](../categories-cn/08-技能模板与资源/awesome-usecases.md) |
| davepoon/buildwithclaude | 2,565 | [buildwithclaude.md](../categories-cn/08-技能模板与资源/buildwithclaude.md) |
| SumeLabs/clawra | 2,008 | [clawra.md](../categories-cn/08-技能模板与资源/clawra.md) |
| LeoYeAI/master-skills | 1,391 | [openclaw-master-skills.md](../categories-cn/08-技能模板与资源/openclaw-master-skills.md) |
| SamurAIGPT/awesome-openclaw | 778 | [awesome-openclaw.md](../categories-cn/08-技能模板与资源/awesome-openclaw.md) |
| unbrowse-ai/unbrowse | 485 | [unbrowse.md](../categories-cn/08-技能模板与资源/unbrowse.md) |
| sundial-org/awesome-skills | 427 | [sundial-awesome-skills.md](../categories-cn/08-技能模板与资源/sundial-awesome-skills.md) |
| ythx-101/x-tweet-fetcher | 407 | [x-tweet-fetcher.md](../categories-cn/08-技能模板与资源/x-tweet-fetcher.md) |
| sharbelxyz/x-bookmarks | 241 | [x-bookmarks.md](../categories-cn/08-技能模板与资源/x-bookmarks.md) |
| blessonism/search-skills | 232 | [search-skills.md](../categories-cn/08-技能模板与资源/search-skills.md) |
| oh-ashen-one/reddit-growth | 109 | [reddit-growth.md](../categories-cn/08-技能模板与资源/reddit-growth.md) |
| destinyfrancis/knowledge-distiller | 43 | [knowledge-distiller.md](../categories-cn/08-技能模板与资源/knowledge-distiller.md) |
| pepicrft/plugin-vault | 41 | [plugin-vault.md](../categories-cn/08-技能模板与资源/plugin-vault.md) |

## I. 协议（A2A / MCP / ACP）

| 项目 | Stars | 文件 |
|------|-------|------|
| win4r/a2a-gateway | 162 | [a2a-gateway.md](../categories-cn/09-协议/a2a-gateway.md) |
| 8421bit/MiniClaw | 63 | [miniclaw.md](../categories-cn/09-协议/miniclaw.md) |
| freema/openclaw-mcp | 60 | [openclaw-mcp.md](../categories-cn/09-协议/openclaw-mcp.md) |
| androidStern/mcp-adapter | 27 | [mcp-adapter.md](../categories-cn/09-协议/mcp-adapter.md) |

## J. 运维工具

| 项目 | Stars | 文件 |
|------|-------|------|
| LeoYeAI/openclaw-guardian | 938 | [openclaw-guardian.md](../categories-cn/10-运维工具/openclaw-guardian.md) |
| LeoYeAI/openclaw-backup | 917 | [openclaw-backup.md](../categories-cn/10-运维工具/openclaw-backup.md) |
| digitalknk/openclaw-runbook | 894 | [openclaw-runbook.md](../categories-cn/10-运维工具/openclaw-runbook.md) |

## K. 语音

| 项目 | Stars | 文件 |
|------|-------|------|
| yuga-hashimoto/openclaw-assistant | 157 | [openclaw-assistant.md](../categories-cn/11-语音/openclaw-assistant.md) |
| Purple-Horizons/openclaw-voice | 66 | [openclaw-voice.md](../categories-cn/11-语音/openclaw-voice.md) |

## L. LLM 路由/成本优化

| 项目 | Stars | 文件 |
|------|-------|------|
| BlockRunAI/ClawRouter | 5,352 | [clawrouter.md](../categories-cn/12-路由与成本优化/clawrouter.md) |
| mnfst/manifest | 3,733 | [manifest.md](../categories-cn/12-路由与成本优化/manifest.md) |
| badrisnarayanan/antigravity | 3,107 | [antigravity-proxy.md](../categories-cn/12-路由与成本优化/antigravity-proxy.md) |
| linuxhsj/zero-token | 1,450 | [openclaw-zero-token.md](../categories-cn/12-路由与成本优化/openclaw-zero-token.md) |
| junhoyeo/tokscale | 1,090 | [tokscale.md](../categories-cn/12-路由与成本优化/tokscale.md) |
| zscole/model-hierarchy-skill | 329 | [model-hierarchy-skill.md](../categories-cn/12-路由与成本优化/model-hierarchy-skill.md) |

## M. 多 Agent 编排

| 项目 | Stars | 文件 |
|------|-------|------|
| RightNow-AI/openfang | 13,621 | [openfang.md](../categories-cn/13-多Agent编排/openfang.md) |
| HKUDS/ClawWork | 6,988 | [clawwork.md](../categories-cn/13-多Agent编排/clawwork.md) |
| cft0808/edict | 7,636 | [edict.md](../categories-cn/13-多Agent编排/edict.md) |
| snarktank/antfarm | 2,104 | [antfarm.md](../categories-cn/13-多Agent编排/antfarm.md) |
| heshengtao/super-agent-party | 1,834 | [super-agent-party.md](../categories-cn/13-多Agent编排/super-agent-party.md) |
| alibaba/hiclaw | 1,537 | [hiclaw.md](../categories-cn/13-多Agent编排/hiclaw.md) |
| Gen-Verse/OpenClaw-RL | 1,311 | [openclaw-rl.md](../categories-cn/13-多Agent编排/openclaw-rl.md) |
| Arvincreator/project-golem | 270 | [project-golem.md](../categories-cn/13-多Agent编排/project-golem.md) |
| Mayuqi-crypto/InterSystem | 50 | [intersystem.md](../categories-cn/13-多Agent编排/intersystem.md) |
| trohitg/MachinaOS | 18 | [machinaos.md](../categories-cn/13-多Agent编排/machinaos.md) |

## N. 桌面/移动客户端

| 项目 | Stars | 文件 |
|------|-------|------|
| ValueCell-ai/ClawX | 3,454 | [clawx.md](../categories-cn/14-桌面与移动客户端/clawx.md) |
| openakita/openakita | 1,114 | [openakita.md](../categories-cn/14-桌面与移动客户端/openakita.md) |
| mithun50/openclaw-termux | 563 | [openclaw-termux.md](../categories-cn/14-桌面与移动客户端/openclaw-termux.md) |
| rohanarun/phoneclaw | 392 | [phoneclaw.md](../categories-cn/14-桌面与移动客户端/phoneclaw.md) |
| zhixianio/botdrop-android | 303 | [botdrop-android.md](../categories-cn/14-桌面与移动客户端/botdrop-android.md) |

## O. 其他

| 项目 | Stars | 文件 |
|------|-------|------|
| HKUDS/nanobot | 32,020 | [nanobot.md](../categories-cn/15-其他/nanobot.md) |
| openimsdk/open-im-server | 15,775 | [openimsdk.md](../categories-cn/15-其他/openimsdk.md) |
| volcengine/OpenViking | 5,671 | [openviking.md](../categories-cn/15-其他/openviking.md) |
| ComposioHQ/secure-openclaw | 1,358 | [secure-openclaw.md](../categories-cn/15-其他/secure-openclaw.md) |
| 195440/nof1.ai | 569 | [nof1-ai.md](../categories-cn/15-其他/nof1-ai.md) |
| pjasicek/OpenClaw | 448 | [pjasicek-openclaw.md](../categories-cn/15-其他/pjasicek-openclaw.md) |
| kevin-liu-robot/EQtreader | 54 | [eqtreader.md](../categories-cn/15-其他/eqtreader.md) |
| ZiyaZhang/market-sentry | 31 | [market-sentry.md](../categories-cn/15-其他/market-sentry.md) |
| chenmuwen0930/snowtrace | 27 | [snowtrace.md](../categories-cn/15-其他/snowtrace.md) |

---

→ 已检查但不直接相关的项目：[00-excluded-projects.md](excluded-projects.md)（160+ 个）
