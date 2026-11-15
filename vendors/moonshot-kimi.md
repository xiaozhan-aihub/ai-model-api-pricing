# 月之暗面 Kimi API 价格与调用：Kimi K2、K3

> Moonshot AI (Kimi) API pricing on XiaoZhan AIhub: 5 models (Kimi K2 and K3). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 月之暗面 Kimi 模型共 5 个（对话大模型 5 个），一把 `sk-gpushare-` 密钥全都能调：对话模型用 OpenAI SDK 改个 `base_url` 即可。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [大模型 API 价格对比](../pricing/llm-api.md) · [官网厂商页](https://model.dflop.top/vendors/moonshot)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [Kimi K2.5](#kimi-k2.5) | `kimi-k2.5` | 对话大模型 | 输入 ¥4.044 / 输出 ¥16.85 每百万 token | 256K | — |
| [Kimi K2.6](#kimi-k2.6) | `kimi-k2.6` | 对话大模型 | 输入 ¥4.044 / 输出 ¥16.85 每百万 token | 256K | — |
| [Kimi K2.7 Code](#kimi-k2.7-code) | `kimi-k2.7-code` | 对话大模型 | 输入 ¥4.044 / 输出 ¥16.85 每百万 token | 256K | — |
| [Kimi K3](#kimi-k3) | `kimi-k3` | 对话大模型 | 输入 ¥20 / 输出 ¥100 每百万 token | 256K | — |
| [Kimi K3 1013](#kimi-k3-1013) | `kimi-k3-1013` | 对话大模型 | 输入 ¥15 / 输出 ¥75 每百万 token | 256K | 7.5 折 |

## 各模型详情

<a id="kimi-k2.5"></a>

### Kimi K2.5

调用 ID `kimi-k2.5` · 对话大模型 · 上架 2025-11-01

Moonshot Kimi K2.5,256K 上下文,带 prompt cache。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 242.64 积分 ≈ ¥4.044 ≈ $0.6 |
| 输出 · 每百万 token | 1011 积分 ≈ ¥16.85 ≈ $2.5 |
| 缓存命中输入 · 每百万 token | 40.44 积分 ≈ ¥0.674 ≈ $0.1 |

- 上下文 256K token，最大输出 256K token
- 能力：工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式、开源权重
- 接口：OpenAI Chat Completions `POST /v1/chat/completions`
- 模型页：[model.dflop.top/models/kimi-k2.5](https://model.dflop.top/models/kimi-k2.5) · [English](https://model.dflop.top/en/models/kimi-k2.5) · [Markdown](https://model.dflop.top/models/kimi-k2.5.md)

> Moonshot Kimi K2.5. 256K context, with prompt caching.

<a id="kimi-k2.6"></a>

### Kimi K2.6

调用 ID `kimi-k2.6` · 对话大模型 · 上架 2026-01-15

Moonshot Kimi K2.6,256K 上下文。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 242.64 积分 ≈ ¥4.044 ≈ $0.6 |
| 输出 · 每百万 token | 1011 积分 ≈ ¥16.85 ≈ $2.5 |
| 缓存命中输入 · 每百万 token | 40.44 积分 ≈ ¥0.674 ≈ $0.1 |

- 上下文 256K token，最大输出 256K token
- 能力：工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式、开源权重
- 接口：OpenAI Chat Completions `POST /v1/chat/completions`
- 模型页：[model.dflop.top/models/kimi-k2.6](https://model.dflop.top/models/kimi-k2.6) · [English](https://model.dflop.top/en/models/kimi-k2.6) · [Markdown](https://model.dflop.top/models/kimi-k2.6.md)

> Moonshot Kimi K2.6. 256K context.

<a id="kimi-k2.7-code"></a>

### Kimi K2.7 Code

调用 ID `kimi-k2.7-code` · 对话大模型 · 上架 2026-06-15

Moonshot Kimi K2.7 代码特化版,256K 上下文。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 242.64 积分 ≈ ¥4.044 ≈ $0.6 |
| 输出 · 每百万 token | 1011 积分 ≈ ¥16.85 ≈ $2.5 |
| 缓存命中输入 · 每百万 token | 40.44 积分 ≈ ¥0.674 ≈ $0.1 |

- 上下文 256K token，最大输出 256K token
- 能力：工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式、开源权重
- 接口：OpenAI Chat Completions `POST /v1/chat/completions`
- 模型页：[model.dflop.top/models/kimi-k2.7-code](https://model.dflop.top/models/kimi-k2.7-code) · [English](https://model.dflop.top/en/models/kimi-k2.7-code) · [Markdown](https://model.dflop.top/models/kimi-k2.7-code.md)

> Moonshot Kimi K2.7, the coding-specialised version. 256K context.

<a id="kimi-k3"></a>

### Kimi K3

调用 ID `kimi-k3` · 对话大模型 · 上架 2026-07-24

Moonshot Kimi K3,256K 上下文,带 prompt cache。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 1200 积分 ≈ ¥20 ≈ $2.967 |
| 输出 · 每百万 token | 6000 积分 ≈ ¥100 ≈ $14.84 |
| 缓存命中输入 · 每百万 token | 120 积分 ≈ ¥2 ≈ $0.2967 |

- 上下文 256K token，最大输出 256K token
- 能力：工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式、开源权重
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/kimi-k3](https://model.dflop.top/models/kimi-k3) · [English](https://model.dflop.top/en/models/kimi-k3) · [Markdown](https://model.dflop.top/models/kimi-k3.md)

> Moonshot Kimi K3. 256K context, with prompt caching.

<a id="kimi-k3-1013"></a>

### Kimi K3 1013

调用 ID `kimi-k3-1013` · 对话大模型 · 上架 2026-10-14

Moonshot Kimi K3 独立线路,256K 上下文,带 prompt cache。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 900 积分 ≈ ¥15 ≈ $2.226 | 1200 积分 ≈ ¥20 ≈ $2.967 |
| 输出 · 每百万 token | 4500 积分 ≈ ¥75 ≈ $11.13 | 6000 积分 ≈ ¥100 ≈ $14.84 |
| 缓存命中输入 · 每百万 token | 90 积分 ≈ ¥1.5 ≈ $0.2226 | 120 积分 ≈ ¥2 ≈ $0.2967 |

现在是限时 7.5 折。

- 上下文 256K token，最大输出 256K token
- 能力：工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式、开源权重
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · Anthropic Messages `POST /v1/messages`
- 模型页：[model.dflop.top/models/kimi-k3-1013](https://model.dflop.top/models/kimi-k3-1013) · [English](https://model.dflop.top/en/models/kimi-k3-1013) · [Markdown](https://model.dflop.top/models/kimi-k3-1013.md)

> Moonshot Kimi K3 on a separate line. 256K context, with prompt caching.

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

对话（Kimi K3）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="kimi-k3",
    messages=[{"role": "user", "content": "用三句话介绍一下你自己"}],
)
print(resp.choices[0].message.content)
```

## English

5 Moonshot AI (Kimi) models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (Kimi K2 and K3). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: chat models through the OpenAI SDK at `https://api.dflop.top/v1`.

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
