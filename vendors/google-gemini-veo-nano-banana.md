# Google API 价格与调用：Gemini 对话、Nano Banana 生图、Veo 视频

> Google API pricing on XiaoZhan AIhub: 13 models (Gemini, Nano Banana image and Veo video). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 Google 模型共 13 个（对话大模型 6 个，图像生成 4 个，视频生成 3 个），一把 `sk-gpushare-` 密钥全都能调：对话模型用 OpenAI SDK 改个 `base_url` 即可，生图走 OpenAI Images 接口，视频是提交任务再轮询结果。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [大模型 API 价格对比](../pricing/llm-api.md) · [AI 生图 API 价格对比](../pricing/image-generation-api.md) · [AI 视频生成 API 价格对比](../pricing/video-generation-api.md) · [官网厂商页](https://model.dflop.top/vendors/google)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [Gemini 3.1 Pro](#gemini-3.1-pro-low) | `gemini-3.1-pro-low` | 对话大模型 | 输入 ¥6.74 / 输出 ¥40.44 每百万 token | 2M | 5 折 |
| [Gemini 3.1 Pro Preview 1020](#gemini-3.1-pro-preview-1020) | `gemini-3.1-pro-preview-1020` | 对话大模型 | 输入 ¥6.74 / 输出 ¥40.44 每百万 token | 1M | 5 折 |
| [Gemini 3.8 Flash](#gemini-3.8-flash) | `gemini-3.8-flash` | 对话大模型 | 输入 ¥2.527 / 输出 ¥12.64 每百万 token | 1M | 5 折 |
| [Gemini 3.8 Flash-nx](#gemini-3.8-flash-nx) | `gemini-3.8-flash-nx` | 对话大模型 | 输入 ¥5.055 / 输出 ¥25.27 每百万 token | 1M | — |
| [Gemini 4 Argon](#gemini-4-argon) | `gemini-4-argon` | 对话大模型 | 输入 ¥6.74 / 输出 ¥33.7 每百万 token | 1M | 5 折 |
| [Gemini 4 Argon-nx](#gemini-4-argon-nx) | `gemini-4-argon-nx` | 对话大模型 | 输入 ¥13.48 / 输出 ¥67.4 每百万 token | 1M | — |
| [Nano Banana](#nano-banana) | `nano-banana` | 图像生成 | ¥0.3 / 张 | — | — |
| [Nano Banana 2](#nano-banana-2) | `nano-banana-2` | 图像生成 | ¥0.3 / 张 | — | — |
| [Nano Banana 2.1](#nano-banana-2.1) | `nano-banana-2.1` | 图像生成 | ¥0.3 / 张 | — | — |
| [Nano Banana Pro](#nano-banana-pro) | `nano-banana-pro` | 图像生成 | ¥0.3 / 张 | — | — |
| [Veo 3.1](#tvod-veo-3.1) | `tvod-veo-3.1` | 视频生成 | ¥0.674 / 秒 | — | — |
| [Veo 3.1 Fast](#tvod-veo-3.1-fast) | `tvod-veo-3.1-fast` | 视频生成 | ¥0.8088 / 秒 | — | — |
| [Veo 3.1 Lite](#tvod-veo-3.1-lite) | `tvod-veo-3.1-lite` | 视频生成 | ¥0.5392 / 秒 | — | — |

## 各模型详情

<a id="gemini-3.1-pro-low"></a>

### Gemini 3.1 Pro

调用 ID `gemini-3.1-pro-low` · 对话大模型 · 上架 2026-02-01

Google Gemini 3.1 Pro,2M 超长上下文,旗舰推理 + 多模态。以 OpenAI 兼容协议供给。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 404.4 积分 ≈ ¥6.74 ≈ $1 | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 2426.4 积分 ≈ ¥40.44 ≈ $6 | 4852.8 积分 ≈ ¥80.88 ≈ $12 |
| 缓存命中输入 · 每百万 token | 40.44 积分 ≈ ¥0.674 ≈ $0.1 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 5 折。

- 上下文 2M token，最大输出 64K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Gemini generateContent `POST /v1beta/models/gemini-3.1-pro-low:generateContent`
- 模型页：[model.dflop.top/models/gemini-3.1-pro-low](https://model.dflop.top/models/gemini-3.1-pro-low) · [English](https://model.dflop.top/en/models/gemini-3.1-pro-low) · [Markdown](https://model.dflop.top/models/gemini-3.1-pro-low.md)

> Google Gemini 3.1 Pro. 2M context, flagship reasoning and multimodal. Served over the OpenAI-compatible protocol.

<a id="gemini-3.1-pro-preview-1020"></a>

### Gemini 3.1 Pro Preview 1020

调用 ID `gemini-3.1-pro-preview-1020` · 对话大模型 · 上架 2026-02-01

Google Gemini 3.1 Pro Preview(1020 线路),1M 上下文,默认带思考,支持 Google 搜索,按 Google 官方价计费,输入超过 20 万 token 按长上下文档。OpenAI 兼容 + Gemini 原生双协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 404.4 积分 ≈ ¥6.74 ≈ $1 | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 2426.4 积分 ≈ ¥40.44 ≈ $6 | 4852.8 积分 ≈ ¥80.88 ≈ $12 |
| 缓存命中输入 · 每百万 token | 40.44 积分 ≈ ¥0.674 ≈ $0.1 | 80.88 积分 ≈ ¥1.348 ≈ $0.2 |

现在是限时 5 折。

- 上下文 1M token，最大输出 64K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、联网搜索、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Gemini generateContent `POST /v1beta/models/gemini-3.1-pro-preview-1020:generateContent`
- 模型页：[model.dflop.top/models/gemini-3.1-pro-preview-1020](https://model.dflop.top/models/gemini-3.1-pro-preview-1020) · [English](https://model.dflop.top/en/models/gemini-3.1-pro-preview-1020) · [Markdown](https://model.dflop.top/models/gemini-3.1-pro-preview-1020.md)

> Google Gemini 3.1 Pro Preview (1020 line). 1M context, thinking on by default, Google Search supported, billed at Google's list price; inputs over 200K tokens use the long-context tier. OpenAI-compatible and native Gemini protocols.

<a id="gemini-3.8-flash"></a>

### Gemini 3.8 Flash

调用 ID `gemini-3.8-flash` · 对话大模型 · 上架 2026-09-02

Google Gemini 3.8 Flash,1M 上下文,当前最强的 Flash 档,面向长程编码与自主智能体,默认带思考。OpenAI 兼容 + Gemini 原生双协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 151.65 积分 ≈ ¥2.527 ≈ $0.375 | 303.3 积分 ≈ ¥5.055 ≈ $0.75 |
| 输出 · 每百万 token | 758.25 积分 ≈ ¥12.64 ≈ $1.875 | 1516.5 积分 ≈ ¥25.27 ≈ $3.75 |
| 缓存命中输入 · 每百万 token | 15.16 积分 ≈ ¥0.2527 ≈ $0.0375 | 30.33 积分 ≈ ¥0.5055 ≈ $0.075 |

现在是限时 5 折。

- 上下文 1M token，最大输出 64K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Gemini generateContent `POST /v1beta/models/gemini-3.8-flash:generateContent`
- 模型页：[model.dflop.top/models/gemini-3.8-flash](https://model.dflop.top/models/gemini-3.8-flash) · [English](https://model.dflop.top/en/models/gemini-3.8-flash) · [Markdown](https://model.dflop.top/models/gemini-3.8-flash.md)

> Google Gemini 3.8 Flash. 1M context, the strongest Flash tier to date, for long-horizon coding and autonomous agents, thinking on by default. OpenAI-compatible and native Gemini protocols.

<a id="gemini-3.8-flash-nx"></a>

### Gemini 3.8 Flash-nx

调用 ID `gemini-3.8-flash-nx` · 对话大模型 · 上架 2026-09-02

Google Gemini 3.8 Flash(nx 线路),1M 上下文,当前最强的 Flash 档,面向长程编码与自主智能体,默认带思考,按 Google 官方价计费。OpenAI 兼容 + Gemini 原生双协议。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 303.3 积分 ≈ ¥5.055 ≈ $0.75 |
| 输出 · 每百万 token | 1516.5 积分 ≈ ¥25.27 ≈ $3.75 |
| 缓存命中输入 · 每百万 token | 30.33 积分 ≈ ¥0.5055 ≈ $0.075 |

- 上下文 1M token，最大输出 64K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Gemini generateContent `POST /v1beta/models/gemini-3.8-flash-nx:generateContent`
- 模型页：[model.dflop.top/models/gemini-3.8-flash-nx](https://model.dflop.top/models/gemini-3.8-flash-nx) · [English](https://model.dflop.top/en/models/gemini-3.8-flash-nx) · [Markdown](https://model.dflop.top/models/gemini-3.8-flash-nx.md)

> Google Gemini 3.8 Flash (nx line). 1M context, the strongest Flash tier to date, for long-horizon coding and autonomous agents, thinking on by default, billed at Google's list price. OpenAI-compatible and native Gemini protocols.

<a id="gemini-4-argon"></a>

### Gemini 4 Argon

调用 ID `gemini-4-argon` · 对话大模型 · 上架 2026-10-13

Google Gemini 4 Argon,1M 上下文,Gemini 4 代旗舰推理模型,面向复杂编码、智能体、数学与科学任务,思考档位 low / medium(默认)/ high。OpenAI 兼容 + Gemini 原生双协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 404.4 积分 ≈ ¥6.74 ≈ $1 | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 2022 积分 ≈ ¥33.7 ≈ $5 | 4044 积分 ≈ ¥67.4 ≈ $10 |
| 缓存命中输入 · 每百万 token | 20.22 积分 ≈ ¥0.337 ≈ $0.05 | 40.44 积分 ≈ ¥0.674 ≈ $0.1 |

现在是限时 5 折。

- 上下文 1M token，最大输出 64K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Gemini generateContent `POST /v1beta/models/gemini-4-argon:generateContent`
- 模型页：[model.dflop.top/models/gemini-4-argon](https://model.dflop.top/models/gemini-4-argon) · [English](https://model.dflop.top/en/models/gemini-4-argon) · [Markdown](https://model.dflop.top/models/gemini-4-argon.md)

> Google Gemini 4 Argon. 1M context, the Gemini 4 flagship reasoning model for complex coding, agents, maths and science; thinking levels low, medium (default) and high. OpenAI-compatible and native Gemini protocols.

<a id="gemini-4-argon-nx"></a>

### Gemini 4 Argon-nx

调用 ID `gemini-4-argon-nx` · 对话大模型 · 上架 2026-10-13

Google Gemini 4 Argon(nx 线路),1M 上下文,Gemini 4 代旗舰推理模型,面向复杂编码、智能体、数学与科学任务,思考档位 low / medium(默认)/ high,按 Google 官方价计费。OpenAI 兼容 + Gemini 原生双协议。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 4044 积分 ≈ ¥67.4 ≈ $10 |
| 缓存命中输入 · 每百万 token | 40.44 积分 ≈ ¥0.674 ≈ $0.1 |

- 上下文 1M token，最大输出 64K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Gemini generateContent `POST /v1beta/models/gemini-4-argon-nx:generateContent`
- 模型页：[model.dflop.top/models/gemini-4-argon-nx](https://model.dflop.top/models/gemini-4-argon-nx) · [English](https://model.dflop.top/en/models/gemini-4-argon-nx) · [Markdown](https://model.dflop.top/models/gemini-4-argon-nx.md)

> Google Gemini 4 Argon (nx line). 1M context, the Gemini 4 flagship reasoning model for complex coding, agents, maths and science; thinking levels low, medium (default) and high; billed at Google's list price. OpenAI-compatible and native Gemini protocols.

<a id="nano-banana"></a>

### Nano Banana

调用 ID `nano-banana` · 图像生成 · 上架 2026-06-26

Google Gemini 2.5 Flash Image(Nano Banana)。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 18 积分 ≈ ¥0.3 ≈ $0.04451 |

- 尺寸：尺寸档 1K / 2K / 4K，尺寸下限约 1920×1920
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 9 张、图生图最多 3 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/nano-banana](https://model.dflop.top/models/nano-banana) · [English](https://model.dflop.top/en/models/nano-banana) · [Markdown](https://model.dflop.top/models/nano-banana.md)

> Google Gemini 2.5 Flash Image (Nano Banana).

<a id="nano-banana-2"></a>

### Nano Banana 2

调用 ID `nano-banana-2` · 图像生成 · 上架 2025-11-01

Google Gemini 3.1 Flash Image(Nano Banana 2)。文生图 / 图生图(参考图改图)。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 18 积分 ≈ ¥0.3 ≈ $0.04451 |

- 尺寸：尺寸档 1K / 2K / 4K，尺寸下限约 1920×1920
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 9 张、图生图最多 14 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/nano-banana-2](https://model.dflop.top/models/nano-banana-2) · [English](https://model.dflop.top/en/models/nano-banana-2) · [Markdown](https://model.dflop.top/models/nano-banana-2.md)

> Google Gemini 3.1 Flash Image (Nano Banana 2). Text-to-image and image-to-image (reference-image editing).

<a id="nano-banana-2.1"></a>

### Nano Banana 2.1

调用 ID `nano-banana-2.1` · 图像生成 · 上架 2026-10-06

Google Gemini Nano Banana 2.1(Nano Banana 2 的升级版)。文生图 / 图生图(参考图改图),支持 1K / 2K / 4K。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 18 积分 ≈ ¥0.3 ≈ $0.04451 |

- 尺寸：尺寸档 1K / 2K / 4K，尺寸下限约 1920×1920
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 9 张、图生图最多 14 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/nano-banana-2.1](https://model.dflop.top/models/nano-banana-2.1) · [English](https://model.dflop.top/en/models/nano-banana-2.1) · [Markdown](https://model.dflop.top/models/nano-banana-2.1.md)

> Google Gemini Nano Banana 2.1, the upgrade of Nano Banana 2. Text-to-image and image-to-image (reference-image editing) at 1K, 2K or 4K.

<a id="nano-banana-pro"></a>

### Nano Banana Pro

调用 ID `nano-banana-pro` · 图像生成 · 上架 2026-06-26

Google Gemini 3 Pro Image(Nano Banana Pro)。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 18 积分 ≈ ¥0.3 ≈ $0.04451 |

- 尺寸：尺寸档 1K / 2K / 4K，尺寸下限约 1920×1920
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 9 张、图生图最多 14 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/nano-banana-pro](https://model.dflop.top/models/nano-banana-pro) · [English](https://model.dflop.top/en/models/nano-banana-pro) · [Markdown](https://model.dflop.top/models/nano-banana-pro.md)

> Google Gemini 3 Pro Image (Nano Banana Pro).

<a id="tvod-veo-3.1"></a>

### Veo 3.1

调用 ID `tvod-veo-3.1` · 视频生成 · 上架 2026-06-26

Google Veo 视频生成(异步任务)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 40.44 积分 ≈ ¥0.674 ≈ $0.1 |

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p / 4k
- 时长：8 秒
- 画幅：16:9 / 9:16
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-veo-3.1](https://model.dflop.top/models/tvod-veo-3.1) · [English](https://model.dflop.top/en/models/tvod-veo-3.1) · [Markdown](https://model.dflop.top/models/tvod-veo-3.1.md)

> Google Veo video generation (asynchronous task).

<a id="tvod-veo-3.1-fast"></a>

### Veo 3.1 Fast

调用 ID `tvod-veo-3.1-fast` · 视频生成 · 上架 2026-06-26

Google Veo 视频生成(异步任务)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 48.53 积分 ≈ ¥0.8088 ≈ $0.12 |

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p
- 时长：8 秒
- 画幅：16:9 / 9:16
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-veo-3.1-fast](https://model.dflop.top/models/tvod-veo-3.1-fast) · [English](https://model.dflop.top/en/models/tvod-veo-3.1-fast) · [Markdown](https://model.dflop.top/models/tvod-veo-3.1-fast.md)

> Google Veo video generation (asynchronous task).

<a id="tvod-veo-3.1-lite"></a>

### Veo 3.1 Lite

调用 ID `tvod-veo-3.1-lite` · 视频生成 · 上架 2026-06-26

Google Veo 视频生成(异步任务)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 32.35 积分 ≈ ¥0.5392 ≈ $0.08 |

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p
- 时长：8 秒
- 画幅：16:9 / 9:16
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-veo-3.1-lite](https://model.dflop.top/models/tvod-veo-3.1-lite) · [English](https://model.dflop.top/en/models/tvod-veo-3.1-lite) · [Markdown](https://model.dflop.top/models/tvod-veo-3.1-lite.md)

> Google Veo video generation (asynchronous task).

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

对话（Gemini 3.8 Flash）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[{"role": "user", "content": "用三句话介绍一下你自己"}],
)
print(resp.choices[0].message.content)
```

用 Google Gen AI SDK（Gemini 原生协议）：

```python
import os
from google import genai

client = genai.Client(
    api_key=os.environ["PLATFORM_API_KEY"],
    http_options={"base_url": "https://api.dflop.top", "api_version": "v1beta"},
)
resp = client.models.generate_content(model="gemini-3.8-flash", contents="你好")
print(resp.text)
```

生图（Nano Banana Pro）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"], timeout=300)

result = client.images.generate(
    model="nano-banana-pro",
    prompt="一只在竹林里喝茶的熊猫，水彩风格",
    size="2048x2048",
)
print(result.data[0].url)  # 临时链接（约 24 小时），请转存
```

视频（Veo 3.1 Fast）：

```python
import os, time, uuid
import requests

BASE = "https://api.dflop.top/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"}

r = requests.post(
    f"{BASE}/videos/generations",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},  # 重试用同一把键，不会重复扣费
    json={
        "model": "tvod-veo-3.1-fast",
        "content": [{"type": "text", "text": "海边日落，无人机航拍视角"}],
        "duration": 8,
        "resolution": "720p",
        "ratio": "16:9",
    },
    timeout=60,
)
r.raise_for_status()
task = r.json()

while task["status"] not in ("succeeded", "failed", "expired", "cancelled"):
    time.sleep(10)  # 一般 1–5 分钟
    task = requests.get(f"{BASE}/videos/generations/{task['id']}", headers=HEADERS, timeout=30).json()

print(task.get("video_url") or task.get("error"))  # video_url 7 天有效，请转存
```

## English

13 Google models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (Gemini, Nano Banana image and Veo video). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: chat models through the OpenAI SDK at `https://api.dflop.top/v1`; image models through the OpenAI Images API (`/v1/images/generations`); video models as asynchronous tasks (`/v1/videos/generations`).

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
