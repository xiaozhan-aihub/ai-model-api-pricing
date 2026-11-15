# OpenAI API 价格与调用：GPT 对话模型、GPT-Image 生图

> OpenAI API pricing on XiaoZhan AIhub: 25 models (GPT chat models and GPT-Image). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 OpenAI 模型共 25 个（对话大模型 17 个，图像生成 8 个），一把 `sk-gpushare-` 密钥全都能调：对话模型用 OpenAI SDK 改个 `base_url` 即可，生图走 OpenAI Images 接口。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [大模型 API 价格对比](../pricing/llm-api.md) · [AI 生图 API 价格对比](../pricing/image-generation-api.md) · [官网厂商页](https://model.dflop.top/vendors/openai)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [Codex Auto Review](#codex-auto-review) | `codex-auto-review` | 对话大模型 | 输入 ¥0.4044 / 输出 ¥2.426 每百万 token | 272K | 3 折 |
| [GPT-5.6 Luna](#gpt-5.6-luna) | `gpt-5.6-luna` | 对话大模型 | 输入 ¥0.4044 / 输出 ¥2.426 每百万 token | 1M | 3 折 |
| [GPT-5.6 Luna-bd](#gpt-5.6-luna-bd) | `gpt-5.6-luna-bd` | 对话大模型 | 输入 ¥1.348 / 输出 ¥8.088 每百万 token | 1.05M | — |
| [GPT-5.6 Sol](#gpt-5.6-sol) | `gpt-5.6-sol` | 对话大模型 | 输入 ¥10.11 / 输出 ¥60.66 每百万 token | 1M | 3 折 |
| [GPT-5.6 Sol-bd](#gpt-5.6-sol-bd) | `gpt-5.6-sol-bd` | 对话大模型 | 输入 ¥26.96 / 输出 ¥134.8 每百万 token | 1.05M | — |
| [GPT-5.6 Terra](#gpt-5.6-terra) | `gpt-5.6-terra` | 对话大模型 | 输入 ¥10.11 / 输出 ¥60.66 每百万 token | 1M | 3 折 |
| [GPT-5.6 Terra-bd](#gpt-5.6-terra-bd) | `gpt-5.6-terra-bd` | 对话大模型 | 输入 ¥13.48 / 输出 ¥80.88 每百万 token | 1.05M | — |
| [GPT-6](#gpt-6) | `gpt-6` | 对话大模型 | 输入 ¥20.22 / 输出 ¥101.1 每百万 token | 1.05M | 3 折 |
| [GPT-6 Astra](#gpt-6-astra) | `gpt-6-astra` | 对话大模型 | 输入 ¥20.22 / 输出 ¥101.1 每百万 token | 1.05M | 3 折 |
| [GPT-6 Astra-bd](#gpt-6-astra-bd) | `gpt-6-astra-bd` | 对话大模型 | 输入 ¥67.4 / 输出 ¥337 每百万 token | 1.05M | — |
| [GPT-6 Luna](#gpt-6-luna) | `gpt-6-luna` | 对话大模型 | 输入 ¥0.2022 / 输出 ¥1.011 每百万 token | 1.05M | 3 折 |
| [GPT-6 Luna-bd](#gpt-6-luna-bd) | `gpt-6-luna-bd` | 对话大模型 | 输入 ¥0.674 / 输出 ¥3.37 每百万 token | 1.05M | — |
| [GPT-6 Sol](#gpt-6-sol) | `gpt-6-sol` | 对话大模型 | 输入 ¥4.044 / 输出 ¥20.22 每百万 token | 1.05M | 3 折 |
| [GPT-6 Sol-bd](#gpt-6-sol-bd) | `gpt-6-sol-bd` | 对话大模型 | 输入 ¥13.48 / 输出 ¥67.4 每百万 token | 1.05M | — |
| [GPT-6.1 Sol](#gpt-6.1-sol) | `gpt-6.1-sol` | 对话大模型 | 输入 ¥4.044 / 输出 ¥20.22 每百万 token | 1.05M | 3 折 |
| [GPT-6.1 Sol-bd](#gpt-6.1-sol-bd) | `gpt-6.1-sol-bd` | 对话大模型 | 输入 ¥13.48 / 输出 ¥67.4 每百万 token | 1.05M | — |
| [GPT-6.1 Terra](#gpt-6.1-terra) | `gpt-6.1-terra` | 对话大模型 | 输入 ¥2.022 / 输出 ¥10.11 每百万 token | 1.05M | 3 折 |
| [GPT-Image 2](#gpt-image-2) | `gpt-image-2` | 图像生成 | ¥0.3 / 张 | — | — |
| [GPT-Image 2-bd](#gpt-image-2-bd) | `gpt-image-2-bd` | 图像生成 | ¥1.138 / 张 | — | — |
| [GPT-Image 2.5 Flare](#gpt-image-2.5-flare) | `gpt-image-2.5-flare` | 图像生成 | ¥0.3 / 张 | — | — |
| [GPT-Image 2.5 Flare-bd](#gpt-image-2.5-flare-bd) | `gpt-image-2.5-flare-bd` | 图像生成 | ¥1.138 / 张 | — | — |
| [GPT-Image 2.5 Sunburst](#gpt-image-2.5-sunburst) | `gpt-image-2.5-sunburst` | 图像生成 | ¥0.3 / 张 | — | — |
| [GPT-Image 2.5 Sunburst-bd](#gpt-image-2.5-sunburst-bd) | `gpt-image-2.5-sunburst-bd` | 图像生成 | ¥1.138 / 张 | — | — |
| [GPT-Image 2.6 Flare](#gpt-image-2.6-flare) | `gpt-image-2.6-flare` | 图像生成 | ¥1.422 / 张 | — | — |
| [GPT-Image 2.6 Sunburst](#gpt-image-2.6-sunburst) | `gpt-image-2.6-sunburst` | 图像生成 | ¥1.422 / 张 | — | — |

## 各模型详情

<a id="codex-auto-review"></a>

### Codex Auto Review

调用 ID `codex-auto-review` · 对话大模型 · 上架 2026-09-09

Codex「帮我批准」(Approve for me)背后的审批复核模型 —— 内核对每个有风险的动作先问它一次安全与否,只有判危险才打断用户。官方标记为内部模型;上下文 272K,工具 / 读图 / 联网 / 出图全套就绪。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 24.26 积分 ≈ ¥0.4044 ≈ $0.06 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |
| 输出 · 每百万 token | 145.58 积分 ≈ ¥2.426 ≈ $0.36 | 485.28 积分 ≈ ¥8.088 ≈ $1.2 |
| 缓存命中输入 · 每百万 token | 2.426 积分 ≈ ¥0.04044 ≈ $0.006 | 8.088 积分 ≈ ¥0.1348 ≈ $0.02 |
| 出图 · 每张 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 3 折。

- 上下文 272K token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式、出图
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/codex-auto-review](https://model.dflop.top/models/codex-auto-review) · [English](https://model.dflop.top/en/models/codex-auto-review) · [Markdown](https://model.dflop.top/models/codex-auto-review.md)

> The review model behind Codex's "Approve for me": the kernel asks it whether each risky action is safe and only interrupts you when it judges an action dangerous. Officially marked as an internal model; 272K context, with tools, image input, web search and image generation ready to use.

<a id="gpt-5.6-luna"></a>

### GPT-5.6 Luna

调用 ID `gpt-5.6-luna` · 对话大模型 · 上架 2026-07-10

OpenAI GPT-5.6 系列前沿模型(Luna 档),1M 上下文。Reasoning effort 可调,Web 搜索 / 图像生成全套就绪。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 24.26 积分 ≈ ¥0.4044 ≈ $0.06 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |
| 输出 · 每百万 token | 145.58 积分 ≈ ¥2.426 ≈ $0.36 | 485.28 积分 ≈ ¥8.088 ≈ $1.2 |
| 缓存命中输入 · 每百万 token | 2.426 积分 ≈ ¥0.04044 ≈ $0.006 | 8.088 积分 ≈ ¥0.1348 ≈ $0.02 |
| 出图 · 每张 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 3 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式、出图
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-5.6-luna](https://model.dflop.top/models/gpt-5.6-luna) · [English](https://model.dflop.top/en/models/gpt-5.6-luna) · [Markdown](https://model.dflop.top/models/gpt-5.6-luna.md)

> OpenAI GPT-5.6 frontier model (Luna tier). 1M context, adjustable reasoning effort, with web search and image generation ready to use.

<a id="gpt-5.6-luna-bd"></a>

### GPT-5.6 Luna-bd

调用 ID `gpt-5.6-luna-bd` · 对话大模型 · 上架 2026-10-26

OpenAI GPT-5.6 系列 Luna 档(bd 线路),1.05M 上下文,按 OpenAI 官方价计费。推理强度可调,支持联网搜索、读图、文件输入与工具调用;超长 prompt 另有分档价。OpenAI Chat / Responses 双协议。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |
| 输出 · 每百万 token | 485.28 积分 ≈ ¥8.088 ≈ $1.2 |
| 缓存命中输入 · 每百万 token | 8.088 积分 ≈ ¥0.1348 ≈ $0.02 |

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-5.6-luna-bd](https://model.dflop.top/models/gpt-5.6-luna-bd) · [English](https://model.dflop.top/en/models/gpt-5.6-luna-bd) · [Markdown](https://model.dflop.top/models/gpt-5.6-luna-bd.md)

> OpenAI GPT-5.6 Luna tier (bd line). 1.05M context, billed at OpenAI's list price. Adjustable reasoning effort; web search, image input, file input and tool calling; very long prompts are priced in a separate tier. OpenAI Chat and Responses protocols.

<a id="gpt-5.6-sol"></a>

### GPT-5.6 Sol

调用 ID `gpt-5.6-sol` · 对话大模型 · 上架 2026-07-10

OpenAI GPT-5.6 系列前沿模型(Sol 档),1M 上下文。Reasoning effort 可调,Web 搜索 / 图像生成全套就绪。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 606.6 积分 ≈ ¥10.11 ≈ $1.5 | 2022 积分 ≈ ¥33.7 ≈ $5 |
| 输出 · 每百万 token | 3639.6 积分 ≈ ¥60.66 ≈ $9 | 12132 积分 ≈ ¥202.2 ≈ $30 |
| 缓存命中输入 · 每百万 token | 60.66 积分 ≈ ¥1.011 ≈ $0.15 | 202.2 积分 ≈ ¥3.37 ≈ $0.5 |
| 出图 · 每张 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 3 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式、出图
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-5.6-sol](https://model.dflop.top/models/gpt-5.6-sol) · [English](https://model.dflop.top/en/models/gpt-5.6-sol) · [Markdown](https://model.dflop.top/models/gpt-5.6-sol.md)

> OpenAI GPT-5.6 frontier model (Sol tier). 1M context, adjustable reasoning effort, with web search and image generation ready to use.

<a id="gpt-5.6-sol-bd"></a>

### GPT-5.6 Sol-bd

调用 ID `gpt-5.6-sol-bd` · 对话大模型 · 上架 2026-10-26

OpenAI GPT-5.6 系列 Sol 档(bd 线路),1.05M 上下文,按 OpenAI 官方价计费。推理强度可调,支持联网搜索、读图、文件输入与工具调用;超长 prompt 另有分档价。OpenAI Chat / Responses 双协议。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 1617.6 积分 ≈ ¥26.96 ≈ $4 |
| 输出 · 每百万 token | 8088 积分 ≈ ¥134.8 ≈ $20 |
| 缓存命中输入 · 每百万 token | 161.76 积分 ≈ ¥2.696 ≈ $0.4 |

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-5.6-sol-bd](https://model.dflop.top/models/gpt-5.6-sol-bd) · [English](https://model.dflop.top/en/models/gpt-5.6-sol-bd) · [Markdown](https://model.dflop.top/models/gpt-5.6-sol-bd.md)

> OpenAI GPT-5.6 Sol tier (bd line). 1.05M context, billed at OpenAI's list price. Adjustable reasoning effort; web search, image input, file input and tool calling; very long prompts are priced in a separate tier. OpenAI Chat and Responses protocols.

<a id="gpt-5.6-terra"></a>

### GPT-5.6 Terra

调用 ID `gpt-5.6-terra` · 对话大模型 · 上架 2026-07-10

OpenAI GPT-5.6 系列前沿模型(Terra 档),1M 上下文。Reasoning effort 可调,Web 搜索 / 图像生成全套就绪。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 606.6 积分 ≈ ¥10.11 ≈ $1.5 | 2022 积分 ≈ ¥33.7 ≈ $5 |
| 输出 · 每百万 token | 3639.6 积分 ≈ ¥60.66 ≈ $9 | 12132 积分 ≈ ¥202.2 ≈ $30 |
| 缓存命中输入 · 每百万 token | 60.66 积分 ≈ ¥1.011 ≈ $0.15 | 202.2 积分 ≈ ¥3.37 ≈ $0.5 |
| 出图 · 每张 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 3 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式、出图
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-5.6-terra](https://model.dflop.top/models/gpt-5.6-terra) · [English](https://model.dflop.top/en/models/gpt-5.6-terra) · [Markdown](https://model.dflop.top/models/gpt-5.6-terra.md)

> OpenAI GPT-5.6 frontier model (Terra tier). 1M context, adjustable reasoning effort, with web search and image generation ready to use.

<a id="gpt-5.6-terra-bd"></a>

### GPT-5.6 Terra-bd

调用 ID `gpt-5.6-terra-bd` · 对话大模型 · 上架 2026-10-26

OpenAI GPT-5.6 系列 Terra 档(bd 线路),1.05M 上下文,按 OpenAI 官方价计费。推理强度可调,支持联网搜索、读图、文件输入与工具调用;超长 prompt 另有分档价。OpenAI Chat / Responses 双协议。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 4852.8 积分 ≈ ¥80.88 ≈ $12 |
| 缓存命中输入 · 每百万 token | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-5.6-terra-bd](https://model.dflop.top/models/gpt-5.6-terra-bd) · [English](https://model.dflop.top/en/models/gpt-5.6-terra-bd) · [Markdown](https://model.dflop.top/models/gpt-5.6-terra-bd.md)

> OpenAI GPT-5.6 Terra tier (bd line). 1.05M context, billed at OpenAI's list price. Adjustable reasoning effort; web search, image input, file input and tool calling; very long prompts are priced in a separate tier. OpenAI Chat and Responses protocols.

<a id="gpt-6"></a>

### GPT-6

调用 ID `gpt-6` · 对话大模型 · 上架 2026-09-07

OpenAI GPT-6 系列旗舰,1.05M 上下文。Reasoning effort 可调,Web 搜索 / 图像生成全套就绪;超长 prompt 另有分档价。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 1213.2 积分 ≈ ¥20.22 ≈ $3 | 4044 积分 ≈ ¥67.4 ≈ $10 |
| 输出 · 每百万 token | 6066 积分 ≈ ¥101.1 ≈ $15 | 20220 积分 ≈ ¥337 ≈ $50 |
| 缓存命中输入 · 每百万 token | 121.32 积分 ≈ ¥2.022 ≈ $0.3 | 404.4 积分 ≈ ¥6.74 ≈ $1 |
| 出图 · 每张 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 3 折。

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式、出图
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-6](https://model.dflop.top/models/gpt-6) · [English](https://model.dflop.top/en/models/gpt-6) · [Markdown](https://model.dflop.top/models/gpt-6.md)

> OpenAI GPT-6 flagship. 1.05M context, adjustable reasoning effort, with web search and image generation ready to use; very long prompts are priced in a separate tier.

<a id="gpt-6-astra"></a>

### GPT-6 Astra

调用 ID `gpt-6-astra` · 对话大模型 · 上架 2026-09-03

OpenAI GPT-6 系列旗舰(Astra 档),1.05M 上下文。Reasoning effort 可调,Web 搜索 / 图像生成全套就绪;超长 prompt 另有分档价。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 1213.2 积分 ≈ ¥20.22 ≈ $3 | 4044 积分 ≈ ¥67.4 ≈ $10 |
| 输出 · 每百万 token | 6066 积分 ≈ ¥101.1 ≈ $15 | 20220 积分 ≈ ¥337 ≈ $50 |
| 缓存命中输入 · 每百万 token | 121.32 积分 ≈ ¥2.022 ≈ $0.3 | 404.4 积分 ≈ ¥6.74 ≈ $1 |
| 出图 · 每张 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 3 折。

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式、出图
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-6-astra](https://model.dflop.top/models/gpt-6-astra) · [English](https://model.dflop.top/en/models/gpt-6-astra) · [Markdown](https://model.dflop.top/models/gpt-6-astra.md)

> OpenAI GPT-6 flagship (Astra tier). 1.05M context, adjustable reasoning effort, with web search and image generation ready to use; very long prompts are priced in a separate tier.

<a id="gpt-6-astra-bd"></a>

### GPT-6 Astra-bd

调用 ID `gpt-6-astra-bd` · 对话大模型 · 上架 2026-10-26

OpenAI GPT-6 系列旗舰 Astra 档(bd 线路),1.05M 上下文,按 OpenAI 官方价计费。推理强度可调,支持联网搜索、读图、文件输入与工具调用;超长 prompt 另有分档价。OpenAI Chat / Responses 双协议。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 4044 积分 ≈ ¥67.4 ≈ $10 |
| 输出 · 每百万 token | 20220 积分 ≈ ¥337 ≈ $50 |
| 缓存命中输入 · 每百万 token | 404.4 积分 ≈ ¥6.74 ≈ $1 |

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-6-astra-bd](https://model.dflop.top/models/gpt-6-astra-bd) · [English](https://model.dflop.top/en/models/gpt-6-astra-bd) · [Markdown](https://model.dflop.top/models/gpt-6-astra-bd.md)

> OpenAI GPT-6 flagship Astra tier (bd line). 1.05M context, billed at OpenAI's list price. Adjustable reasoning effort; web search, image input, file input and tool calling; very long prompts are priced in a separate tier. OpenAI Chat and Responses protocols.

<a id="gpt-6-luna"></a>

### GPT-6 Luna

调用 ID `gpt-6-luna` · 对话大模型 · 上架 2026-09-22

OpenAI GPT-6 系列 Luna 档,全系最省、面向高并发的专注型任务,1.05M 上下文。Reasoning effort 可调,Web 搜索 / 图像生成全套就绪;超长 prompt 另有分档价。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 12.13 积分 ≈ ¥0.2022 ≈ $0.03 | 40.44 积分 ≈ ¥0.674 ≈ $0.1 |
| 输出 · 每百万 token | 60.66 积分 ≈ ¥1.011 ≈ $0.15 | 202.2 积分 ≈ ¥3.37 ≈ $0.5 |
| 缓存命中输入 · 每百万 token | 1.213 积分 ≈ ¥0.02022 ≈ $0.003 | 4.044 积分 ≈ ¥0.0674 ≈ $0.01 |
| 出图 · 每张 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 3 折。

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式、出图
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-6-luna](https://model.dflop.top/models/gpt-6-luna) · [English](https://model.dflop.top/en/models/gpt-6-luna) · [Markdown](https://model.dflop.top/models/gpt-6-luna.md)

> OpenAI GPT-6 Luna tier, the most economical of the series, for focused high-concurrency tasks. 1.05M context, adjustable reasoning effort, with web search and image generation ready to use; very long prompts are priced in a separate tier.

<a id="gpt-6-luna-bd"></a>

### GPT-6 Luna-bd

调用 ID `gpt-6-luna-bd` · 对话大模型 · 上架 2026-10-26

OpenAI GPT-6 系列 Luna 档,全系最省(bd 线路),1.05M 上下文,按 OpenAI 官方价计费。推理强度可调,支持联网搜索、读图、文件输入与工具调用;超长 prompt 另有分档价。OpenAI Chat / Responses 双协议。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 40.44 积分 ≈ ¥0.674 ≈ $0.1 |
| 输出 · 每百万 token | 202.2 积分 ≈ ¥3.37 ≈ $0.5 |
| 缓存命中输入 · 每百万 token | 4.044 积分 ≈ ¥0.0674 ≈ $0.01 |

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-6-luna-bd](https://model.dflop.top/models/gpt-6-luna-bd) · [English](https://model.dflop.top/en/models/gpt-6-luna-bd) · [Markdown](https://model.dflop.top/models/gpt-6-luna-bd.md)

> OpenAI GPT-6 Luna tier, the most economical of the series (bd line). 1.05M context, billed at OpenAI's list price. Adjustable reasoning effort; web search, image input, file input and tool calling; very long prompts are priced in a separate tier. OpenAI Chat and Responses protocols.

<a id="gpt-6-sol"></a>

### GPT-6 Sol

调用 ID `gpt-6-sol` · 对话大模型 · 上架 2026-09-22

OpenAI GPT-6 系列 Sol 档,面向复杂编码与智能体工作流,1.05M 上下文。Reasoning effort 可调,Web 搜索 / 图像生成全套就绪;超长 prompt 另有分档价。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 242.64 积分 ≈ ¥4.044 ≈ $0.6 | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 1213.2 积分 ≈ ¥20.22 ≈ $3 | 4044 积分 ≈ ¥67.4 ≈ $10 |
| 缓存命中输入 · 每百万 token | 24.26 积分 ≈ ¥0.4044 ≈ $0.06 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |
| 出图 · 每张 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 3 折。

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式、出图
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-6-sol](https://model.dflop.top/models/gpt-6-sol) · [English](https://model.dflop.top/en/models/gpt-6-sol) · [Markdown](https://model.dflop.top/models/gpt-6-sol.md)

> OpenAI GPT-6 Sol tier, for complex coding and agent workflows. 1.05M context, adjustable reasoning effort, with web search and image generation ready to use; very long prompts are priced in a separate tier.

<a id="gpt-6-sol-bd"></a>

### GPT-6 Sol-bd

调用 ID `gpt-6-sol-bd` · 对话大模型 · 上架 2026-10-26

OpenAI GPT-6 系列 Sol 档,面向复杂编码与智能体工作流(bd 线路),1.05M 上下文,按 OpenAI 官方价计费。推理强度可调,支持联网搜索、读图、文件输入与工具调用;超长 prompt 另有分档价。OpenAI Chat / Responses 双协议。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 4044 积分 ≈ ¥67.4 ≈ $10 |
| 缓存命中输入 · 每百万 token | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-6-sol-bd](https://model.dflop.top/models/gpt-6-sol-bd) · [English](https://model.dflop.top/en/models/gpt-6-sol-bd) · [Markdown](https://model.dflop.top/models/gpt-6-sol-bd.md)

> OpenAI GPT-6 Sol tier, for complex coding and agent workflows (bd line). 1.05M context, billed at OpenAI's list price. Adjustable reasoning effort; web search, image input, file input and tool calling; very long prompts are priced in a separate tier. OpenAI Chat and Responses protocols.

<a id="gpt-6.1-sol"></a>

### GPT-6.1 Sol

调用 ID `gpt-6.1-sol` · 对话大模型 · 上架 2026-09-29

OpenAI GPT-6.1 Sol,以低于 GPT-6 Astra 的价格提供接近 Astra 的复杂编码、电脑操作与专业工作能力,1.05M 上下文。Reasoning effort 可调,Web 搜索 / 图像生成全套就绪;超长 prompt 另有分档价。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 242.64 积分 ≈ ¥4.044 ≈ $0.6 | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 1213.2 积分 ≈ ¥20.22 ≈ $3 | 4044 积分 ≈ ¥67.4 ≈ $10 |
| 缓存命中输入 · 每百万 token | 12.13 积分 ≈ ¥0.2022 ≈ $0.03 | 40.44 积分 ≈ ¥0.674 ≈ $0.1 |
| 出图 · 每张 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 3 折。

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式、出图
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-6.1-sol](https://model.dflop.top/models/gpt-6.1-sol) · [English](https://model.dflop.top/en/models/gpt-6.1-sol) · [Markdown](https://model.dflop.top/models/gpt-6.1-sol.md)

> OpenAI GPT-6.1 Sol: close to GPT-6 Astra on complex coding, computer use and professional work at a lower price. 1.05M context, adjustable reasoning effort, with web search and image generation ready to use; very long prompts are priced in a separate tier.

<a id="gpt-6.1-sol-bd"></a>

### GPT-6.1 Sol-bd

调用 ID `gpt-6.1-sol-bd` · 对话大模型 · 上架 2026-10-26

OpenAI GPT-6.1 Sol(bd 线路),1.05M 上下文,按 OpenAI 官方价计费。推理强度可调,支持联网搜索、读图、文件输入与工具调用;超长 prompt 另有分档价。OpenAI Chat / Responses 双协议。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 4044 积分 ≈ ¥67.4 ≈ $10 |
| 缓存命中输入 · 每百万 token | 40.44 积分 ≈ ¥0.674 ≈ $0.1 |

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-6.1-sol-bd](https://model.dflop.top/models/gpt-6.1-sol-bd) · [English](https://model.dflop.top/en/models/gpt-6.1-sol-bd) · [Markdown](https://model.dflop.top/models/gpt-6.1-sol-bd.md)

> OpenAI GPT-6.1 Sol (bd line). 1.05M context, billed at OpenAI's list price. Adjustable reasoning effort; web search, image input, file input and tool calling; very long prompts are priced in a separate tier. OpenAI Chat and Responses protocols.

<a id="gpt-6.1-terra"></a>

### GPT-6.1 Terra

调用 ID `gpt-6.1-terra` · 对话大模型 · 上架 2026-10-26

OpenAI GPT-6.1 Terra,快速高效的新一代模型,擅长视觉推理、精确的电脑操作与清晰自然的写作,1.05M 上下文。Reasoning effort 可调,Web 搜索 / 图像生成全套就绪;超长 prompt 另有分档价。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 121.32 积分 ≈ ¥2.022 ≈ $0.3 | 404.4 积分 ≈ ¥6.74 ≈ $1 |
| 输出 · 每百万 token | 606.6 积分 ≈ ¥10.11 ≈ $1.5 | 2022 积分 ≈ ¥33.7 ≈ $5 |
| 缓存命中输入 · 每百万 token | 6.066 积分 ≈ ¥0.1011 ≈ $0.015 | 20.22 积分 ≈ ¥0.337 ≈ $0.05 |
| 出图 · 每张 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 3 折。

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、文件输入、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式、出图
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/gpt-6.1-terra](https://model.dflop.top/models/gpt-6.1-terra) · [English](https://model.dflop.top/en/models/gpt-6.1-terra) · [Markdown](https://model.dflop.top/models/gpt-6.1-terra.md)

> OpenAI GPT-6.1 Terra, a fast and efficient new-generation model, strong at visual reasoning, precise computer use and clear, natural writing. 1.05M context, adjustable reasoning effort, with web search and image generation ready to use; very long prompts are priced in a separate tier.

<a id="gpt-image-2"></a>

### GPT-Image 2

调用 ID `gpt-image-2` · 图像生成 · 上架 2026-07-08

OpenAI GPT-Image 2 独立出图。文生图 / 参考图改图,任意比例与自定义尺寸。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 18 积分 ≈ ¥0.3 ≈ $0.04451 |

- 尺寸：尺寸档 1K / 2K / 4K，不读 `size`，画面比例写在提示词里
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 图生图最多 16 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/gpt-image-2](https://model.dflop.top/models/gpt-image-2) · [English](https://model.dflop.top/en/models/gpt-image-2) · [Markdown](https://model.dflop.top/models/gpt-image-2.md)

> OpenAI GPT-Image 2 standalone image generation. Text-to-image and reference-image editing at any aspect ratio and custom sizes.

<a id="gpt-image-2-bd"></a>

### GPT-Image 2-bd

调用 ID `gpt-image-2-bd` · 图像生成 · 上架 2026-10-26

OpenAI GPT-Image 2(bd 线路)。文生图 / 参考图改图 / 局部重绘,支持自定义尺寸与画质,按 OpenAI 官方 token 价计费。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 68.26 积分 ≈ ¥1.138 ≈ $0.1688 |

- 尺寸：尺寸档 1K / 2K / 4K，默认 `1024x1024`
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 自动
- 图生图最多 16 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/gpt-image-2-bd](https://model.dflop.top/models/gpt-image-2-bd) · [English](https://model.dflop.top/en/models/gpt-image-2-bd) · [Markdown](https://model.dflop.top/models/gpt-image-2-bd.md)

> OpenAI GPT-Image 2 (bd line). Text-to-image, reference-image editing and inpainting, with custom sizes and quality, billed at OpenAI's official token prices.

<a id="gpt-image-2.5-flare"></a>

### GPT-Image 2.5 Flare

调用 ID `gpt-image-2.5-flare` · 图像生成 · 上架 2026-09-08

OpenAI GPT-Image 2.5 速度档。文生图 / 参考图改图 / 草图转成品,单张出图。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 18 积分 ≈ ¥0.3 ≈ $0.04451 |

- 尺寸：尺寸档 1K / 2K / 4K，不读 `size`，画面比例写在提示词里
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 图生图最多 16 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/gpt-image-2.5-flare](https://model.dflop.top/models/gpt-image-2.5-flare) · [English](https://model.dflop.top/en/models/gpt-image-2.5-flare) · [Markdown](https://model.dflop.top/models/gpt-image-2.5-flare.md)

> OpenAI GPT-Image 2.5, speed tier. Text-to-image, reference-image editing and sketch-to-finished-image, one image per request.

<a id="gpt-image-2.5-flare-bd"></a>

### GPT-Image 2.5 Flare-bd

调用 ID `gpt-image-2.5-flare-bd` · 图像生成 · 上架 2026-10-26

OpenAI GPT-Image 2.5 速度档(bd 线路)。文生图 / 参考图改图 / 局部重绘,支持自定义尺寸与画质,按 OpenAI 官方 token 价计费。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 68.26 积分 ≈ ¥1.138 ≈ $0.1688 |

- 尺寸：尺寸档 1K / 2K / 4K，默认 `1024x1024`
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 自动
- 图生图最多 16 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/gpt-image-2.5-flare-bd](https://model.dflop.top/models/gpt-image-2.5-flare-bd) · [English](https://model.dflop.top/en/models/gpt-image-2.5-flare-bd) · [Markdown](https://model.dflop.top/models/gpt-image-2.5-flare-bd.md)

> OpenAI GPT-Image 2.5 speed tier (bd line). Text-to-image, reference-image editing and inpainting, with custom sizes and quality, billed at OpenAI's official token prices.

<a id="gpt-image-2.5-sunburst"></a>

### GPT-Image 2.5 Sunburst

调用 ID `gpt-image-2.5-sunburst` · 图像生成 · 上架 2026-09-08

OpenAI GPT-Image 2.5 精修档。编辑精度与参考图主体保持更强,适合草图转成品与改图。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 18 积分 ≈ ¥0.3 ≈ $0.04451 |

- 尺寸：尺寸档 1K / 2K / 4K，不读 `size`，画面比例写在提示词里
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 图生图最多 16 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/gpt-image-2.5-sunburst](https://model.dflop.top/models/gpt-image-2.5-sunburst) · [English](https://model.dflop.top/en/models/gpt-image-2.5-sunburst) · [Markdown](https://model.dflop.top/models/gpt-image-2.5-sunburst.md)

> OpenAI GPT-Image 2.5, refinement tier. Stronger editing precision and subject consistency with reference images; suited to sketch-to-finished-image and edits.

<a id="gpt-image-2.5-sunburst-bd"></a>

### GPT-Image 2.5 Sunburst-bd

调用 ID `gpt-image-2.5-sunburst-bd` · 图像生成 · 上架 2026-10-26

OpenAI GPT-Image 2.5 精修档(bd 线路)。文生图 / 参考图改图 / 局部重绘,支持自定义尺寸与画质,按 OpenAI 官方 token 价计费。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 68.26 积分 ≈ ¥1.138 ≈ $0.1688 |

- 尺寸：尺寸档 1K / 2K / 4K，默认 `1024x1024`
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 自动
- 图生图最多 16 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/gpt-image-2.5-sunburst-bd](https://model.dflop.top/models/gpt-image-2.5-sunburst-bd) · [English](https://model.dflop.top/en/models/gpt-image-2.5-sunburst-bd) · [Markdown](https://model.dflop.top/models/gpt-image-2.5-sunburst-bd.md)

> OpenAI GPT-Image 2.5 refinement tier (bd line). Text-to-image, reference-image editing and inpainting, with custom sizes and quality, billed at OpenAI's official token prices.

<a id="gpt-image-2.6-flare"></a>

### GPT-Image 2.6 Flare

调用 ID `gpt-image-2.6-flare` · 图像生成 · 上架 2026-11-04

OpenAI GPT-Image 2.6 速度档。文生图 / 参考图改图,还能生成 GIF 动图;按 OpenAI 官方 token 价计费。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 85.33 积分 ≈ ¥1.422 ≈ $0.211 |

- 尺寸：尺寸档 1K / 2K / 4K，默认 `1024x1024`
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 自动
- 图生图最多 9 张参考图、能生成 GIF 动图（9 / 12 / 16 帧）
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/gpt-image-2.6-flare](https://model.dflop.top/models/gpt-image-2.6-flare) · [English](https://model.dflop.top/en/models/gpt-image-2.6-flare) · [Markdown](https://model.dflop.top/models/gpt-image-2.6-flare.md)

> OpenAI GPT-Image 2.6, speed tier. Text-to-image and reference-image editing, and it can make animated GIFs; billed at OpenAI's official token prices.

<a id="gpt-image-2.6-sunburst"></a>

### GPT-Image 2.6 Sunburst

调用 ID `gpt-image-2.6-sunburst` · 图像生成 · 上架 2026-11-04

OpenAI GPT-Image 2.6 精修档。细节与参考图主体保持更强,同样能生成 GIF 动图;按 OpenAI 官方 token 价计费。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 85.33 积分 ≈ ¥1.422 ≈ $0.211 |

- 尺寸：尺寸档 1K / 2K / 4K，默认 `1024x1024`
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 自动
- 图生图最多 9 张参考图、能生成 GIF 动图（9 / 12 / 16 帧）
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/gpt-image-2.6-sunburst](https://model.dflop.top/models/gpt-image-2.6-sunburst) · [English](https://model.dflop.top/en/models/gpt-image-2.6-sunburst) · [Markdown](https://model.dflop.top/models/gpt-image-2.6-sunburst.md)

> OpenAI GPT-Image 2.6, refinement tier. Better detail and subject consistency with reference images, and it can also make animated GIFs; billed at OpenAI's official token prices.

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

对话（GPT-6 Luna）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="gpt-6-luna",
    messages=[{"role": "user", "content": "用三句话介绍一下你自己"}],
)
print(resp.choices[0].message.content)
```

生图（GPT-Image 2）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"], timeout=300)

result = client.images.generate(
    model="gpt-image-2",
    prompt="一只在竹林里喝茶的熊猫，水彩风格，画面比例 1:1",  # 这个模型不读 size，比例写在提示词里
)
print(result.data[0].url)  # 临时链接（约 24 小时），请转存
```

## English

25 OpenAI models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (GPT chat models and GPT-Image). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: chat models through the OpenAI SDK at `https://api.dflop.top/v1`; image models through the OpenAI Images API (`/v1/images/generations`).

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
