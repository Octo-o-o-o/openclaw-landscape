# openclaw/skills

## 基本信息

- **GitHub 仓库**: https://github.com/openclaw/skills
- **Stars**: 2,524
- **创建时间**: 2026-01-06
- **最后更新**: 2026-03-11
- **主要语言**: Python
- **仓库大小**: 367,017 KB (约 358 MB)
- **Topics**: archive, backup, clawhub, openclaw, skill
- **技能数量**: 1,000+ 个技能（持续增长）

## 问题与解决方案

### 核心问题

openclaw/skills 仓库解决的是 **技能注册中心的持久化备份和历史存档** 问题：

1. **数据持久性**：ClawHub 作为在线服务，需要一个可靠的备份机制，防止数据丢失
2. **历史追溯**：需要保留所有技能的所有版本，包括已删除或标记为恶意的技能，用于安全分析和审计
3. **离线访问**：开发者和研究人员需要能够离线访问技能库，进行批量分析或研究
4. **透明度**：公开的 Git 仓库提供了完全透明的技能发布历史，任何人都可以审查
5. **灾难恢复**：如果 ClawHub 服务出现故障，可以从 GitHub 仓库恢复所有数据

### 解决方案

openclaw/skills 仓库作为 **ClawHub 的官方备份存档**，具备以下特点：

- **自动化备份**：通过 GitHub App 集成，ClawHub 上的每次技能发布/更新都会自动同步到此仓库
- **完整版本历史**：每个技能的所有版本都被保留，包括软删除的版本
- **结构化存储**：
  - 每个技能一个目录（以用户名命名）
  - 每个版本一个子目录（以版本号或标识符命名）
  - 包含 `SKILL.md` 和 `_meta.json`（版本元数据）
- **安全分析语料库**：保留可疑/恶意技能用于进一步分析，帮助改进安全检测算法
- **只读存档**：用户应优先使用 ClawHub 网站或 CLI 下载技能，此仓库仅作为历史存档

## 核心架构

### 仓库结构

```
openclaw/skills/
├── README.md
├── LICENSE
└── skills/
    ├── 00xmorty/
    │   └── conatus/
    │       ├── SKILL.md
    │       └── _meta.json
    ├── 04551lh/
    ├── 0731coderlee-sudo/
    ├── ...
    └── [1000+ 用户目录]/
```

### 目录命名规则

- **一级目录**：用户名（GitHub handle）
  - 例如：`00xmorty`、`steipete`、`anthropic`
- **二级目录**：技能 slug 或版本标识符
  - 例如：`conatus`、`my-skill-v1.0.0`
- **文件**：
  - `SKILL.md`：技能的主文档（必需）
  - `_meta.json`：版本元数据（可选，由备份系统生成）
  - 其他支持文件（脚本、配置、示例等）

### 备份机制

根据 ClawHub 的文档（`docs/github-import.md`、`githubBackups.ts`），备份流程如下：

1. **触发条件**：
   - 用户在 ClawHub 上发布新技能版本
   - 用户更新现有技能
   - 管理员手动触发备份

2. **GitHub App 集成**：
   - ClawHub 使用 GitHub App 认证
   - 拥有 `openclaw/skills` 仓库的写权限
   - 通过 GitHub API 创建/更新文件

3. **备份内容**：
   - 技能的所有文本文件（从 Convex `_storage` 下载）
   - 版本元数据（`_meta.json`）：
     - 版本号、发布时间、变更日志
     - 作者信息、标签
     - 文件列表和哈希值

4. **冲突处理**：
   - 如果目标路径已存在，使用版本号后缀避免覆盖
   - 保留所有历史版本

5. **恶意技能处理**：
   - 即使技能被标记为恶意或软删除，仍然保留在仓库中
   - 用于安全研究和改进检测算法
   - README 中明确警告用户谨慎使用

### 数据流

```
用户 → ClawHub Web/CLI
         ↓ (发布技能)
    Convex 数据库 + 文件存储
         ↓ (触发备份)
    GitHub App (认证)
         ↓ (API 调用)
    openclaw/skills 仓库
         ↓ (Git commit)
    公开的 GitHub 存档
```

## 关键特性

### 1. 完整的版本历史

- **所有版本保留**：每个技能的每个版本都被备份
- **软删除版本**：即使用户在 ClawHub 上删除了某个版本，仓库中仍然保留
- **变更追踪**：通过 Git 历史可以追踪技能的演变过程

### 2. 安全分析语料库

- **恶意技能存档**：
  - 被标记为 `suspicious` 或 `malicious` 的技能仍然保留
  - 用于训练和改进安全检测模型
  - 帮助研究人员分析攻击模式

- **免责声明**：
  - README 明确警告："there may be suspicious or malicious skills within this repo"
  - 建议用户仅使用 ClawHub 网站下载技能
  - 将此仓库视为历史存档而非分发渠道

### 3. 离线访问

- **克隆仓库**：
  ```bash
  git clone https://github.com/openclaw/skills.git
  cd skills/skills
  ```

- **批量分析**：
  - 研究人员可以批量分析所有技能
  - 统计技能的依赖、工具使用、代码模式
  - 构建技能推荐系统

- **离线搜索**：
  - 使用 `grep`、`rg` 等工具搜索技能内容
  - 不依赖 ClawHub 的在线服务

### 4. 透明度与审计

- **公开的 Git 历史**：
  - 任何人都可以查看技能的发布历史
  - 可以追踪谁在何时发布了什么

- **社区监督**：
  - 社区成员可以审查技能内容
  - 发现问题可以在 ClawHub 上举报

### 5. 灾难恢复

- **数据冗余**：
  - ClawHub 的 Convex 数据库 + GitHub 仓库双重备份
  - 即使 ClawHub 服务中断，数据仍然安全

- **恢复流程**：
  - 从 GitHub 仓库克隆所有技能
  - 解析 `_meta.json` 重建数据库
  - 重新生成 embeddings 和索引
# apps/api/services/git_backup.py
import asyncio
from github import Github
from sqlalchemy.ext.asyncio import AsyncSession

class GitBackupService:
    def __init__(self, github_token: str, repo_name: str):
        self.github = Github(github_token)
        self.repo = self.github.get_repo(repo_name)

    async def backup_agent_config(
        self,
        agent_id: str,
        config: dict,
        version: str,
        author: str,
        changelog: str
    ):
        """备份 Agent 配置到 GitHub"""
        path = f"agents/{agent_id}/{version}/config.yaml"
        content = yaml.dump(config)
        message = f"Backup agent {agent_id} v{version}\n\n{changelog}"

        try:
            self.repo.create_file(
                path=path,
                message=message,
                content=content,
                branch="main"
            )
        except GithubException as e:
            if e.status == 422:  # File already exists
                # Use version suffix to avoid conflict
                path = f"agents/{agent_id}/{version}-{int(time.time())}/config.yaml"
                self.repo.create_file(path, message, content, branch="main")
            else:
                raise
```

#### 9.2 从 Git 恢复配置

```python
# apps/api/services/git_restore.py
class GitRestoreService:
    async def restore_agent_config(
        self,
        agent_id: str,
        version: str,
        db: AsyncSession
    ):
        """从 GitHub 恢复 Agent 配置"""
        path = f"agents/{agent_id}/{version}/config.yaml"

        try:
            file_content = self.repo.get_contents(path)
            config = yaml.safe_load(file_content.decoded_content)

            # 恢复到数据库
            agent = await db.get(Agent, agent_id)
            agent.config = config
            agent.version = version
            await db.commit()

            return agent
        except GithubException as e:
            if e.status == 404:
                raise ValueError(f"Config not found: {path}")
            raise
```

#### 9.3 审计日志 Git 归档

```python
# apps/api/services/audit_archive.py
class AuditArchiveService:
    async def archive_daily_logs(self, date: datetime.date):
        """每日归档审计日志到 Git"""
        logs = await self.fetch_audit_logs(date)

        # 序列化为 JSON
        content = json.dumps(logs, indent=2, ensure_ascii=False)

        # 提交到 Git
        path = f"audit-logs/{date.year}/{date.month:02d}/{date.day:02d}.json"
        message = f"Archive audit logs for {date}"

        self.repo.create_file(
            path=path,
            message=message,
            content=content,
            branch="main"
        )
```

---

## 总结

openclaw/skills 仓库是 ClawHub 的关键基础设施，提供了：

1. **持久化备份**：所有技能的所有版本都被安全备份
2. **历史存档**：包括已删除和恶意技能，用于安全研究
3. **离线访问**：研究人员和开发者可以离线分析技能库
4. **透明度**：公开的 Git 历史提供完全透明的审计日志
5. **灾难恢复**：作为 ClawHub 的冗余备份，确保数据安全

对于 ClawButler 而言，openclaw/skills 提供了一个成熟的参考实现，展示了如何：

- 将关键数据备份到 Git 仓库
- 实现 GitOps 工作流
- 保留完整的审计日志
- 支持离线部署和边缘场景
- 满足合规和法律要求
- 构建安全分析语料库

ClawButler 可以借鉴这些设计，为 Agent 配置、模板、Runbook、审计日志等关键数据建立 Git-based 的备份和版本控制机制，进一步增强系统的可靠性、透明度和合规性。
