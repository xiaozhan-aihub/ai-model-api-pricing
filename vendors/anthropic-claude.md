# Anthropic Claude API 价格与调用：Claude Opus、Sonnet、Haiku

> Anthropic Claude API pricing on XiaoZhan AIhub: 14 models (Claude Opus, Sonnet and Haiku). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 Anthropic Claude 模型共 14 个（对话大模型 14 个），一把 `sk-gpushare-` 密钥全都能调：对话模型用 OpenAI SDK 改个 `base_url` 即可。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [大模型 API 价格对比](../pricing/llm-api.md) · [官网厂商页](https://model.dflop.top/vendors/anthropic)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [Claude Fable 5](#claude-fable-5) | `claude-fable-5` | 对话大模型 | 输入 ¥40.44 / 输出 ¥202.2 每百万 token | 200K | 6 折 |
| [Claude Fable 5.1](#claude-fable-5-1) | `claude-fable-5-1` | 对话大模型 | 输入 ¥40.44 / 输出 ¥202.2 每百万 token | 1M | 6 折 |
| [Claude Haiku 4.5](#claude-haiku-4-5-20251001) | `claude-haiku-4-5-20251001` | 对话大模型 | 输入 ¥4.044 / 输出 ¥20.22 每百万 token | 200K | 6 折 |
| [Claude Haiku 5.5](#claude-haiku-5-5) | `claude-haiku-5-5` | 对话大模型 | 输入 ¥0.4044 / 输出 ¥2.022 每百万 token | 1M | 6 折 |
| [Claude Opus 4.5](#claude-opus-4-5-20251101) | `claude-opus-4-5-20251101` | 对话大模型 | 输入 ¥20.22 / 输出 ¥101.1 每百万 token | 200K | 6 折 |
| [Claude Opus 4.6](#claude-opus-4-6) | `claude-opus-4-6` | 对话大模型 | 输入 ¥20.22 / 输出 ¥101.1 每百万 token | 1M | 6 折 |
| [Claude Opus 4.7](#claude-opus-4-7) | `claude-opus-4-7` | 对话大模型 | 输入 ¥20.22 / 输出 ¥101.1 每百万 token | 1M | 6 折 |
| [Claude Opus 4.8](#claude-opus-4-8) | `claude-opus-4-8` | 对话大模型 | 输入 ¥20.22 / 输出 ¥101.1 每百万 token | 1M | 6 折 |
| [Claude Opus 5](#claude-opus-5) | `claude-opus-5` | 对话大模型 | 输入 ¥20.22 / 输出 ¥101.1 每百万 token | 1M | 6 折 |
| [Claude Opus 5.5](#claude-opus-5-5) | `claude-opus-5-5` | 对话大模型 | 输入 ¥16.18 / 输出 ¥80.88 每百万 token | 1M | 6 折 |
| [Claude Sonnet 4.5](#claude-sonnet-4-5-20250929) | `claude-sonnet-4-5-20250929` | 对话大模型 | 输入 ¥12.13 / 输出 ¥60.66 每百万 token | 200K | 6 折 |
| [Claude Sonnet 4.6](#claude-sonnet-4-6) | `claude-sonnet-4-6` | 对话大模型 | 输入 ¥12.13 / 输出 ¥60.66 每百万 token | 1M | 6 折 |
| [Claude Sonnet 5](#claude-sonnet-5) | `claude-sonnet-5` | 对话大模型 | 输入 ¥8.088 / 输出 ¥40.44 每百万 token | 1M | 6 折 |
| [Claude Sonnet 5.5](#claude-sonnet-5-5) | `claude-sonnet-5-5` | 对话大模型 | 输入 ¥1.855 / 输出 ¥9.277 每百万 token | 1M | — |

## 各模型详情

<a id="claude-fable-5"></a>

### Claude Fable 5

调用 ID `claude-fable-5` · 对话大模型

Anthropic Fable 5,长篇写作 / 叙事向的 Claude 5 变体,200K 上下文。支持 OpenAI Chat / Anthropic Messages 双协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 2426.4 积分 ≈ ¥40.44 ≈ $6 | 4044 积分 ≈ ¥67.4 ≈ $10 |
| 输出 · 每百万 token | 12132 积分 ≈ ¥202.2 ≈ $30 | 20220 积分 ≈ ¥337 ≈ $50 |
| 缓存命中输入 · 每百万 token | 242.64 积分 ≈ ¥4.044 ≈ $0.6 | 404.4 积分 ≈ ¥6.74 ≈ $1 |

现在是限时 6 折。

- 上下文 200K token，最大输出 64K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-fable-5](https://model.dflop.top/models/claude-fable-5) · [English](https://model.dflop.top/en/models/claude-fable-5) · [Markdown](https://model.dflop.top/models/claude-fable-5.md)

> Anthropic Fable 5, a Claude 5 variant for long-form writing and storytelling. 200K context. Supports the OpenAI Chat and Anthropic Messages protocols.

<a id="claude-fable-5-1"></a>

### Claude Fable 5.1

调用 ID `claude-fable-5-1` · 对话大模型

Anthropic Fable 5.1,Anthropic 目前能力最强的通用模型,面向最高难度的推理与长程智能体任务,1M 上下文。支持 OpenAI Chat / Anthropic Messages 双协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 2426.4 积分 ≈ ¥40.44 ≈ $6 | 4044 积分 ≈ ¥67.4 ≈ $10 |
| 输出 · 每百万 token | 12132 积分 ≈ ¥202.2 ≈ $30 | 20220 积分 ≈ ¥337 ≈ $50 |
| 缓存命中输入 · 每百万 token | 60.66 积分 ≈ ¥1.011 ≈ $0.15 | 101.1 积分 ≈ ¥1.685 ≈ $0.25 |

现在是限时 6 折。

- 上下文 1M token，最大输出 64K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-fable-5-1](https://model.dflop.top/models/claude-fable-5-1) · [English](https://model.dflop.top/en/models/claude-fable-5-1) · [Markdown](https://model.dflop.top/models/claude-fable-5-1.md)

> Anthropic Fable 5.1, Anthropic's most capable general model, built for the hardest reasoning and long-horizon agent tasks. 1M context. Supports the OpenAI Chat and Anthropic Messages protocols.

<a id="claude-haiku-4-5-20251001"></a>

### Claude Haiku 4.5

调用 ID `claude-haiku-4-5-20251001` · 对话大模型 · 上架 2025-10-01

Anthropic Haiku 4.5,200K 上下文,最快最省的轻量级 Claude,适合高并发 / 低延迟场景。支持三协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 242.64 积分 ≈ ¥4.044 ≈ $0.6 | 404.4 积分 ≈ ¥6.74 ≈ $1 |
| 输出 · 每百万 token | 1213.2 积分 ≈ ¥20.22 ≈ $3 | 2022 积分 ≈ ¥33.7 ≈ $5 |
| 缓存命中输入 · 每百万 token | 24.26 积分 ≈ ¥0.4044 ≈ $0.06 | 40.44 积分 ≈ ¥0.674 ≈ $0.1 |

现在是限时 6 折。

- 上下文 200K token，最大输出 64K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-haiku-4-5-20251001](https://model.dflop.top/models/claude-haiku-4-5-20251001) · [English](https://model.dflop.top/en/models/claude-haiku-4-5-20251001) · [Markdown](https://model.dflop.top/models/claude-haiku-4-5-20251001.md)

> Anthropic Haiku 4.5. 200K context, the fastest and most economical Claude, for high-concurrency and low-latency workloads. Supports all three protocols.

<a id="claude-haiku-5-5"></a>

### Claude Haiku 5.5

调用 ID `claude-haiku-5-5` · 对话大模型

Anthropic Haiku 5.5,新一代轻量 Claude,1M 上下文,快而省,适合高并发、分类抽取与子任务。支持 OpenAI Chat / Anthropic Messages 双协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 24.26 积分 ≈ ¥0.4044 ≈ $0.06 | 40.44 积分 ≈ ¥0.674 ≈ $0.1 |
| 输出 · 每百万 token | 121.32 积分 ≈ ¥2.022 ≈ $0.3 | 202.2 积分 ≈ ¥3.37 ≈ $0.5 |
| 缓存命中输入 · 每百万 token | 2.426 积分 ≈ ¥0.04044 ≈ $0.006 | 4.044 积分 ≈ ¥0.0674 ≈ $0.01 |

现在是限时 6 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-haiku-5-5](https://model.dflop.top/models/claude-haiku-5-5) · [English](https://model.dflop.top/en/models/claude-haiku-5-5) · [Markdown](https://model.dflop.top/models/claude-haiku-5-5.md)

> Anthropic Haiku 5.5, the new lightweight Claude. 1M context, fast and economical; good for high concurrency, classification, extraction and sub-tasks. Supports the OpenAI Chat and Anthropic Messages protocols.

<a id="claude-opus-4-5-20251101"></a>

### Claude Opus 4.5

调用 ID `claude-opus-4-5-20251101` · 对话大模型 · 上架 2025-11-01

Anthropic Opus 4.5,200K 上下文,推理 / 编码 / 智能体任务。支持 OpenAI Chat / Anthropic Messages 双协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 1213.2 积分 ≈ ¥20.22 ≈ $3 | 2022 积分 ≈ ¥33.7 ≈ $5 |
| 输出 · 每百万 token | 6066 积分 ≈ ¥101.1 ≈ $15 | 10110 积分 ≈ ¥168.5 ≈ $25 |
| 缓存命中输入 · 每百万 token | 121.32 积分 ≈ ¥2.022 ≈ $0.3 | 202.2 积分 ≈ ¥3.37 ≈ $0.5 |

现在是限时 6 折。

- 上下文 200K token，最大输出 64K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-opus-4-5-20251101](https://model.dflop.top/models/claude-opus-4-5-20251101) · [English](https://model.dflop.top/en/models/claude-opus-4-5-20251101) · [Markdown](https://model.dflop.top/models/claude-opus-4-5-20251101.md)

> Anthropic Opus 4.5. 200K context, for reasoning, coding and agent tasks. Supports the OpenAI Chat and Anthropic Messages protocols.

<a id="claude-opus-4-6"></a>

### Claude Opus 4.6

调用 ID `claude-opus-4-6` · 对话大模型

Anthropic Opus 4.6,1M 上下文,推理 / 编码 / 多模态全能,适合最复杂任务。支持 OpenAI Chat / Anthropic Messages / OpenAI Responses 三协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 1213.2 积分 ≈ ¥20.22 ≈ $3 | 2022 积分 ≈ ¥33.7 ≈ $5 |
| 输出 · 每百万 token | 6066 积分 ≈ ¥101.1 ≈ $15 | 10110 积分 ≈ ¥168.5 ≈ $25 |
| 缓存命中输入 · 每百万 token | 121.32 积分 ≈ ¥2.022 ≈ $0.3 | 202.2 积分 ≈ ¥3.37 ≈ $0.5 |

现在是限时 6 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-opus-4-6](https://model.dflop.top/models/claude-opus-4-6) · [English](https://model.dflop.top/en/models/claude-opus-4-6) · [Markdown](https://model.dflop.top/models/claude-opus-4-6.md)

> Anthropic Opus 4.6. 1M context, an all-rounder for reasoning, coding and multimodal work, suited to the hardest tasks. Supports the OpenAI Chat, Anthropic Messages and OpenAI Responses protocols.

<a id="claude-opus-4-7"></a>

### Claude Opus 4.7

调用 ID `claude-opus-4-7` · 对话大模型

Anthropic Opus 4.7,1M 上下文,推理 / 编码 / 多模态全能。支持 OpenAI Chat / Anthropic Messages / OpenAI Responses 三协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 1213.2 积分 ≈ ¥20.22 ≈ $3 | 2022 积分 ≈ ¥33.7 ≈ $5 |
| 输出 · 每百万 token | 6066 积分 ≈ ¥101.1 ≈ $15 | 10110 积分 ≈ ¥168.5 ≈ $25 |
| 缓存命中输入 · 每百万 token | 121.32 积分 ≈ ¥2.022 ≈ $0.3 | 202.2 积分 ≈ ¥3.37 ≈ $0.5 |

现在是限时 6 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-opus-4-7](https://model.dflop.top/models/claude-opus-4-7) · [English](https://model.dflop.top/en/models/claude-opus-4-7) · [Markdown](https://model.dflop.top/models/claude-opus-4-7.md)

> Anthropic Opus 4.7. 1M context, an all-rounder for reasoning, coding and multimodal work. Supports the OpenAI Chat, Anthropic Messages and OpenAI Responses protocols.

<a id="claude-opus-4-8"></a>

### Claude Opus 4.8

调用 ID `claude-opus-4-8` · 对话大模型

Anthropic Opus 4.8,1M 上下文,当前最强 Opus,推理 / 编码 / 多模态全能,适合最复杂任务。支持三协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 1213.2 积分 ≈ ¥20.22 ≈ $3 | 2022 积分 ≈ ¥33.7 ≈ $5 |
| 输出 · 每百万 token | 6066 积分 ≈ ¥101.1 ≈ $15 | 10110 积分 ≈ ¥168.5 ≈ $25 |
| 缓存命中输入 · 每百万 token | 121.32 积分 ≈ ¥2.022 ≈ $0.3 | 202.2 积分 ≈ ¥3.37 ≈ $0.5 |

现在是限时 6 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-opus-4-8](https://model.dflop.top/models/claude-opus-4-8) · [English](https://model.dflop.top/en/models/claude-opus-4-8) · [Markdown](https://model.dflop.top/models/claude-opus-4-8.md)

> Anthropic Opus 4.8. 1M context, the strongest Opus to date, an all-rounder for reasoning, coding and multimodal work, suited to the hardest tasks. Supports all three protocols.

<a id="claude-opus-5"></a>

### Claude Opus 5

调用 ID `claude-opus-5` · 对话大模型

Anthropic Opus 5,新一代最强 Opus,1M 上下文,推理 / 编码 / 多模态全能,适合最复杂任务。支持 OpenAI Chat / Anthropic Messages 双协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 1213.2 积分 ≈ ¥20.22 ≈ $3 | 2022 积分 ≈ ¥33.7 ≈ $5 |
| 输出 · 每百万 token | 6066 积分 ≈ ¥101.1 ≈ $15 | 10110 积分 ≈ ¥168.5 ≈ $25 |
| 缓存命中输入 · 每百万 token | 121.32 积分 ≈ ¥2.022 ≈ $0.3 | 202.2 积分 ≈ ¥3.37 ≈ $0.5 |

现在是限时 6 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-opus-5](https://model.dflop.top/models/claude-opus-5) · [English](https://model.dflop.top/en/models/claude-opus-5) · [Markdown](https://model.dflop.top/models/claude-opus-5.md)

> Anthropic Opus 5, the new strongest Opus. 1M context, an all-rounder for reasoning, coding and multimodal work, suited to the hardest tasks. Supports the OpenAI Chat and Anthropic Messages protocols.

<a id="claude-opus-5-5"></a>

### Claude Opus 5.5

调用 ID `claude-opus-5-5` · 对话大模型

Anthropic Opus 5.5,Opus 5 的下一代,1M 上下文,长程智能体编码与知识工作更强。支持 OpenAI Chat / Anthropic Messages 双协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 970.56 积分 ≈ ¥16.18 ≈ $2.4 | 1617.6 积分 ≈ ¥26.96 ≈ $4 |
| 输出 · 每百万 token | 4852.8 积分 ≈ ¥80.88 ≈ $12 | 8088 积分 ≈ ¥134.8 ≈ $20 |
| 缓存命中输入 · 每百万 token | 48.53 积分 ≈ ¥0.8088 ≈ $0.12 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 6 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-opus-5-5](https://model.dflop.top/models/claude-opus-5-5) · [English](https://model.dflop.top/en/models/claude-opus-5-5) · [Markdown](https://model.dflop.top/models/claude-opus-5-5.md)

> Anthropic Opus 5.5, the successor to Opus 5. 1M context, stronger at long-horizon agentic coding and knowledge work. Supports the OpenAI Chat and Anthropic Messages protocols.

<a id="claude-sonnet-4-5-20250929"></a>

### Claude Sonnet 4.5

调用 ID `claude-sonnet-4-5-20250929` · 对话大模型 · 上架 2025-09-29

Anthropic Claude Sonnet 4.5,200K 上下文,推理 + 视觉 + 工具调用。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 727.92 积分 ≈ ¥12.13 ≈ $1.8 | 1213.2 积分 ≈ ¥20.22 ≈ $3 |
| 输出 · 每百万 token | 3639.6 积分 ≈ ¥60.66 ≈ $9 | 6066 积分 ≈ ¥101.1 ≈ $15 |
| 缓存命中输入 · 每百万 token | 72.79 积分 ≈ ¥1.213 ≈ $0.18 | 121.32 积分 ≈ ¥2.022 ≈ $0.3 |

现在是限时 6 折。

- 上下文 200K token，最大输出 64K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-sonnet-4-5-20250929](https://model.dflop.top/models/claude-sonnet-4-5-20250929) · [English](https://model.dflop.top/en/models/claude-sonnet-4-5-20250929) · [Markdown](https://model.dflop.top/models/claude-sonnet-4-5-20250929.md)

> Anthropic Claude Sonnet 4.5: 200K context, reasoning, vision and tool calling.

<a id="claude-sonnet-4-6"></a>

### Claude Sonnet 4.6

调用 ID `claude-sonnet-4-6` · 对话大模型

Anthropic Sonnet 4.6,1M 上下文,性价比首选,推理 + 编码均衡。Cache 命中输入价 1/10($0.30/M)。支持三协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 727.92 积分 ≈ ¥12.13 ≈ $1.8 | 1213.2 积分 ≈ ¥20.22 ≈ $3 |
| 输出 · 每百万 token | 3639.6 积分 ≈ ¥60.66 ≈ $9 | 6066 积分 ≈ ¥101.1 ≈ $15 |
| 缓存命中输入 · 每百万 token | 72.79 积分 ≈ ¥1.213 ≈ $0.18 | 121.32 积分 ≈ ¥2.022 ≈ $0.3 |

现在是限时 6 折。

- 上下文 1M token，最大输出 64K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-sonnet-4-6](https://model.dflop.top/models/claude-sonnet-4-6) · [English](https://model.dflop.top/en/models/claude-sonnet-4-6) · [Markdown](https://model.dflop.top/models/claude-sonnet-4-6.md)

> Anthropic Sonnet 4.6. 1M context, the best value, balanced between reasoning and coding. Cached input costs 1/10 of the input price. Supports all three protocols.

<a id="claude-sonnet-5"></a>

### Claude Sonnet 5

调用 ID `claude-sonnet-5` · 对话大模型

Anthropic Sonnet 5,新一代性价比旗舰,1M 上下文,推理 + 编码均衡。支持 OpenAI Chat / Anthropic Messages / OpenAI Responses 三协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 485.28 积分 ≈ ¥8.088 ≈ $1.2 | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 2426.4 积分 ≈ ¥40.44 ≈ $6 | 4044 积分 ≈ ¥67.4 ≈ $10 |
| 缓存命中输入 · 每百万 token | 48.53 积分 ≈ ¥0.8088 ≈ $0.12 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 6 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-sonnet-5](https://model.dflop.top/models/claude-sonnet-5) · [English](https://model.dflop.top/en/models/claude-sonnet-5) · [Markdown](https://model.dflop.top/models/claude-sonnet-5.md)

> Anthropic Sonnet 5, the new best-value flagship. 1M context, balanced between reasoning and coding. Supports the OpenAI Chat, Anthropic Messages and OpenAI Responses protocols.

<a id="claude-sonnet-5-5"></a>

### Claude Sonnet 5.5

调用 ID `claude-sonnet-5-5` · 对话大模型

Anthropic Sonnet 5.5,Sonnet 5 的下一代,1M 上下文,兼顾速度、成本与能力,擅长文档、代码与智能体任务。支持 OpenAI Chat / Anthropic Messages 双协议。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 111.32 积分 ≈ ¥1.855 ≈ $0.2753 |
| 输出 · 每百万 token | 556.62 积分 ≈ ¥9.277 ≈ $1.376 |
| 缓存命中输入 · 每百万 token | 5.581 积分 ≈ ¥0.09301 ≈ $0.0138 |

- 上下文 1M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/claude-sonnet-5-5](https://model.dflop.top/models/claude-sonnet-5-5) · [English](https://model.dflop.top/en/models/claude-sonnet-5-5) · [Markdown](https://model.dflop.top/models/claude-sonnet-5-5.md)

> Anthropic Sonnet 5.5, the successor to Sonnet 5. 1M context, balancing speed, cost and capability; strong at documents, code and agent tasks. Supports the OpenAI Chat and Anthropic Messages protocols.

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

对话（Claude Sonnet 5）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": "用三句话介绍一下你自己"}],
)
print(resp.choices[0].message.content)
```

用 Anthropic SDK（`base_url` 不带 `/v1`）：

```python
import os
from anthropic import Anthropic

client = Anthropic(base_url="https://api.dflop.top", api_key=os.environ["PLATFORM_API_KEY"])  # 不带 /v1

msg = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "你好"}],
)
print(msg.content[0].text)
```

## English

14 Anthropic Claude models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (Claude Opus, Sonnet and Haiku). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: chat models through the OpenAI SDK at `https://api.dflop.top/v1`.

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
