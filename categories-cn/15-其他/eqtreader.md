> https://github.com/kevin-liu-robot/EQtreader

# EQtreader (54 stars)

## 问题与解决方案

量化交易系统需要集成行情数据获取、交易执行、持仓管理等多个模块，手动开发成本高且容易出错。该项目基于 easyquotation、easytrader、easyquant 等开源库，为 OpenClaw 提供量化交易 Skill，支持同花顺客户端自动化交易和多数据源行情获取。

## 关键特性

- **交易客户端集成** — 通过 easytrader 连接同花顺客户端（`xiadan.exe`），支持下单、查询持仓、查询余额等操作
- **多数据源行情** — 集成新浪、腾讯行情接口，支持实时行情、涨跌幅排行、龙虎榜等数据获取
- **32 位 Python 兼容** — 针对同花顺客户端的 32 位限制，提供 Anaconda 虚拟环境配置方案
- **OCR 识别支持** — 集成 pytesseract 和 pyperclip，支持验证码识别和剪切板填充
- **远程部署指南** — 提供远程服务器部署注意事项（屏保关闭、桌面保持、代码断开连接）
- **数据源扩展** — 集成 TuShare、歪枣网等第三方数据平台，支持历史数据和基本面数据获取

<!-- lastCommit: 6a7050b -->
