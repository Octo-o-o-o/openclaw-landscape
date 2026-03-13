> https://github.com/unbrowse-ai/unbrowse

# Unbrowse (485 stars)

## 问题与解决方案
Agent 访问网站时需要手动编写 API 调用代码，效率低且难以复用。Unbrowse 通过捕获浏览器网络流量，自动逆向工程出网站底层的真实 API 端点，并将学习到的 API 合约存储到共享市场中，实现"一个 Agent 学习一次，后续 Agent 直接复用"的快速路径，速度提升 100 倍，成本降低 80%。

## 关键特性
- 自动发现网站底层 API（捕获网络流量 + 逆向工程）
- 共享市场（一个 Agent 学习，所有 Agent 复用）
- 意图解析管道（路由缓存 → 市场搜索 → 实时捕获 → DOM 回退）
- 技能生命周期管理（active/deprecated/disabled）
- 后台验证循环（每 6 小时执行安全 GET 端点，检测失败和 Schema 漂移）
- 本地执行（凭证留在本地，仅发布学习到的 API 合约）

<!-- lastCommit: 6a7050b -->
