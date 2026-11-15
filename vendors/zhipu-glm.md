# 智谱 GLM API 价格与调用：GLM-5.3 系列

> Zhipu AI (GLM) API pricing on XiaoZhan AIhub: 4 models (the GLM-5.3 series). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 智谱 GLM 模型共 4 个（对话大模型 4 个），一把 `sk-gpushare-` 密钥全都能调：对话模型用 OpenAI SDK 改个 `base_url` 即可。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [大模型 API 价格对比](../pricing/llm-api.md) · [官网厂商页](https://model.dflop.top/vendors/zhipu)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [GLM-5.3](#glm-5.3) | `glm-5.3` | 对话大模型 | 输入 ¥5.6 / 输出 ¥19.6 每百万 token | 1M | 7 折 |
| [GLM-5.3-1022](#glm-5.3-1022) | `glm-5.3-1022` | 对话大模型 | 输入 ¥8 / 输出 ¥28 每百万 token | 1M | — |
| [GLM-5.3-Flash](#glm-5.3-flash) | `glm-5.3-flash` | 对话大模型 | 输入 ¥0.56 / 输出 ¥1.96 每百万 token | 1M | 7 折 |
| [GLM-5.3-Flash-1022](#glm-5.3-flash-1022) | `glm-5.3-flash-1022` | 对话大模型 | 输入 ¥0.8 / 输出 ¥2.8 每百万 token | 1M | — |

## 各模型详情

<a id="glm-5.3"></a>

### GLM-5.3

调用 ID `glm-5.3` · 对话大模型 · 上架 2026-08-23

智谱 GLM-5.3 —— 1000K 上下文,带思考链路。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 336 积分 ≈ ¥5.6 ≈ $0.8309 | 480 积分 ≈ ¥8 ≈ $1.187 |
| 输出 · 每百万 token | 1176 积分 ≈ ¥19.6 ≈ $2.908 | 1680 积分 ≈ ¥28 ≈ $4.154 |
| 缓存命中输入 · 每百万 token | 84 积分 ≈ ¥1.4 ≈ $0.2077 | 120 积分 ≈ ¥2 ≈ $0.2967 |

现在是限时 7 折。

- 上下文 1M token，最大输出 32K token
- 能力：工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式、开源权重
- 接口：OpenAI Chat Completions `POST /v1/chat/completions`
- 模型页：[model.dflop.top/models/glm-5.3](https://model.dflop.top/models/glm-5.3) · [English](https://model.dflop.top/en/models/glm-5.3) · [Markdown](https://model.dflop.top/models/glm-5.3.md)

> Zhipu GLM-5.3: 1M context, with a thinking chain.

<a id="glm-5.3-1022"></a>

### GLM-5.3-1022

调用 ID `glm-5.3-1022` · 对话大模型 · 上架 2026-08-23

智谱 GLM-5.3(1022 线路)—— 1M 上下文,带思考链路(不可关闭),支持工具调用,纯文本输入,按智谱官方价计费。OpenAI Chat / Responses / Anthropic Messages 三协议。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 480 积分 ≈ ¥8 ≈ $1.187 |
| 输出 · 每百万 token | 1680 积分 ≈ ¥28 ≈ $4.154 |
| 缓存命中输入 · 每百万 token | 120 积分 ≈ ¥2 ≈ $0.2967 |

- 上下文 1M token，最大输出 128K token
- 能力：工具调用、思考模式（推理强度 low / high / max）、JSON 模式、开源权重
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/glm-5.3-1022](https://model.dflop.top/models/glm-5.3-1022) · [English](https://model.dflop.top/en/models/glm-5.3-1022) · [Markdown](https://model.dflop.top/models/glm-5.3-1022.md)

> Zhipu GLM-5.3 (1022 line): 1M context, with a thinking chain that cannot be turned off, tool calling and text-only input, billed at Zhipu's list price. OpenAI Chat, Responses and Anthropic Messages protocols.

<a id="glm-5.3-flash"></a>

### GLM-5.3-Flash

调用 ID `glm-5.3-flash` · 对话大模型 · 上架 2026-08-26

智谱 GLM-5.3-Flash —— GLM-5 系列首个原生多模态模型,1M 上下文 / 128K 最大输出,支持图片、视频、文件输入,带思考链路。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 33.6 积分 ≈ ¥0.56 ≈ $0.08309 | 48 积分 ≈ ¥0.8 ≈ $0.1187 |
| 输出 · 每百万 token | 117.6 积分 ≈ ¥1.96 ≈ $0.2908 | 168 积分 ≈ ¥2.8 ≈ $0.4154 |
| 缓存命中输入 · 每百万 token | 9.66 积分 ≈ ¥0.161 ≈ $0.02389 | 13.8 积分 ≈ ¥0.23 ≈ $0.03413 |

现在是限时 7 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / high / max）、JSON 模式、开源权重
- 接口：OpenAI Chat Completions `POST /v1/chat/completions`
- 模型页：[model.dflop.top/models/glm-5.3-flash](https://model.dflop.top/models/glm-5.3-flash) · [English](https://model.dflop.top/en/models/glm-5.3-flash) · [Markdown](https://model.dflop.top/models/glm-5.3-flash.md)

> Zhipu GLM-5.3-Flash: the first natively multimodal model of the GLM-5 series, 1M context and up to 128K output, with image, video and file input and a thinking chain.

<a id="glm-5.3-flash-1022"></a>

### GLM-5.3-Flash-1022

调用 ID `glm-5.3-flash-1022` · 对话大模型 · 上架 2026-08-26

智谱 GLM-5.3-Flash(1022 线路)—— 原生多模态,1M 上下文,带思考链路(不可关闭),支持图片输入与工具调用,按智谱官方标准价计费。OpenAI Chat / Responses / Anthropic Messages 三协议。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 48 积分 ≈ ¥0.8 ≈ $0.1187 |
| 输出 · 每百万 token | 168 积分 ≈ ¥2.8 ≈ $0.4154 |
| 缓存命中输入 · 每百万 token | 13.8 积分 ≈ ¥0.23 ≈ $0.03413 |

- 上下文 1M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / high / max）、JSON 模式、开源权重
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/glm-5.3-flash-1022](https://model.dflop.top/models/glm-5.3-flash-1022) · [English](https://model.dflop.top/en/models/glm-5.3-flash-1022) · [Markdown](https://model.dflop.top/models/glm-5.3-flash-1022.md)

> Zhipu GLM-5.3-Flash (1022 line): natively multimodal, 1M context, with a thinking chain that cannot be turned off, image input and tool calling, billed at Zhipu's standard list price. OpenAI Chat, Responses and Anthropic Messages protocols.

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

对话（GLM-5.3）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="glm-5.3",
    messages=[{"role": "user", "content": "用三句话介绍一下你自己"}],
)
print(resp.choices[0].message.content)
```

## English

4 Zhipu AI (GLM) models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (the GLM-5.3 series). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: chat models through the OpenAI SDK at `https://api.dflop.top/v1`.

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
