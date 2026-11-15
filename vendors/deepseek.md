# DeepSeek 深度求索 API 价格与调用：DeepSeek V4 系列

> DeepSeek API pricing on XiaoZhan AIhub: 3 models (the DeepSeek V4 series). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 DeepSeek 深度求索 模型共 3 个（对话大模型 3 个），一把 `sk-gpushare-` 密钥全都能调：对话模型用 OpenAI SDK 改个 `base_url` 即可。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [大模型 API 价格对比](../pricing/llm-api.md) · [官网厂商页](https://model.dflop.top/vendors/deepseek)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [DeepSeek V4 Flash](#deepseek-v4-flash) | `deepseek-v4-flash` | 对话大模型 | 输入 ¥1.4 / 输出 ¥5.6 每百万 token | 1M | 7 折 |
| [DeepSeek V4 Pro](#deepseek-v4-pro) | `deepseek-v4-pro` | 对话大模型 | 输入 ¥6.3 / 输出 ¥18.9 每百万 token | 128K | 7 折 |
| [DeepSeek V4.1 Flash](#deepseek-v4.1-flash) | `deepseek-v4.1-flash` | 对话大模型 | 输入 ¥1.4 / 输出 ¥5.6 每百万 token | 1M | 7 折 |

## 各模型详情

<a id="deepseek-v4-flash"></a>

### DeepSeek V4 Flash

调用 ID `deepseek-v4-flash` · 对话大模型 · 上架 2026-03-01

DeepSeek V4 Flash — 1M 上下文,默认思考(reasoning_content 流)。按 DeepSeek 官方峰谷价计费(北京时间工作日 9:00-12:00、14:00-18:00 为原价,其余时段含周末与法定节假日半价)。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 84 积分 ≈ ¥1.4 ≈ $0.2077 | 120 积分 ≈ ¥2 ≈ $0.2967 |
| 输出 · 每百万 token | 336 积分 ≈ ¥5.6 ≈ $0.8309 | 480 积分 ≈ ¥8 ≈ $1.187 |
| 缓存命中输入 · 每百万 token | 1.68 积分 ≈ ¥0.028 ≈ $0.004154 | 2.4 积分 ≈ ¥0.04 ≈ $0.005935 |

现在是限时 7 折。

- 上下文 1M token，最大输出 128K token
- 能力：工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式、前缀续写
- 接口：OpenAI Chat Completions `POST /v1/chat/completions`
- 模型页：[model.dflop.top/models/deepseek-v4-flash](https://model.dflop.top/models/deepseek-v4-flash) · [English](https://model.dflop.top/en/models/deepseek-v4-flash) · [Markdown](https://model.dflop.top/models/deepseek-v4-flash.md)

> DeepSeek V4 Flash. 1M context, thinking on by default (reasoning_content stream). Billed at DeepSeek's official peak / off-peak prices: full price on weekdays 9:00-12:00 and 14:00-18:00 Beijing time, half price at all other times, including weekends and public holidays.

<a id="deepseek-v4-pro"></a>

### DeepSeek V4 Pro

调用 ID `deepseek-v4-pro` · 对话大模型 · 上架 2026-03-01

DeepSeek V4 Pro — 128K 上下文,reasoning_content 流。按 DeepSeek 官方峰谷价计费(北京时间工作日 9:00-12:00、14:00-18:00 为原价,其余时段含周末与法定节假日半价)。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 378 积分 ≈ ¥6.3 ≈ $0.9347 | 540 积分 ≈ ¥9 ≈ $1.335 |
| 输出 · 每百万 token | 1134 积分 ≈ ¥18.9 ≈ $2.804 | 1620 积分 ≈ ¥27 ≈ $4.006 |
| 缓存命中输入 · 每百万 token | 12.6 积分 ≈ ¥0.21 ≈ $0.03116 | 18 积分 ≈ ¥0.3 ≈ $0.04451 |

现在是限时 7 折。

- 上下文 128K token，最大输出 128K token
- 能力：工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式、前缀续写
- 接口：OpenAI Chat Completions `POST /v1/chat/completions`
- 模型页：[model.dflop.top/models/deepseek-v4-pro](https://model.dflop.top/models/deepseek-v4-pro) · [English](https://model.dflop.top/en/models/deepseek-v4-pro) · [Markdown](https://model.dflop.top/models/deepseek-v4-pro.md)

> DeepSeek V4 Pro. 128K context, reasoning_content stream. Billed at DeepSeek's official peak / off-peak prices: full price on weekdays 9:00-12:00 and 14:00-18:00 Beijing time, half price at all other times, including weekends and public holidays.

<a id="deepseek-v4.1-flash"></a>

### DeepSeek V4.1 Flash

调用 ID `deepseek-v4.1-flash` · 对话大模型 · 上架 2026-09-10

DeepSeek V4.1 Flash —— 552B 参数 MoE(Causal-Encoder-Decoder 非对称结构),原生多模态视觉理解,1M 上下文 / 最大输出 384K,默认思考模式,官方直连。按 DeepSeek 官方峰谷价计费(北京时间工作日 9:00-12:00、14:00-18:00 为原价,其余时段含周末与法定节假日半价)。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 84 积分 ≈ ¥1.4 ≈ $0.2077 | 120 积分 ≈ ¥2 ≈ $0.2967 |
| 输出 · 每百万 token | 336 积分 ≈ ¥5.6 ≈ $0.8309 | 480 积分 ≈ ¥8 ≈ $1.187 |
| 缓存命中输入 · 每百万 token | 1.68 积分 ≈ ¥0.028 ≈ $0.004154 | 2.4 积分 ≈ ¥0.04 ≈ $0.005935 |

现在是限时 7 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式、前缀续写、开源权重
- 接口：OpenAI Chat Completions `POST /v1/chat/completions`
- 模型页：[model.dflop.top/models/deepseek-v4.1-flash](https://model.dflop.top/models/deepseek-v4.1-flash) · [English](https://model.dflop.top/en/models/deepseek-v4.1-flash) · [Markdown](https://model.dflop.top/models/deepseek-v4.1-flash.md)

> DeepSeek V4.1 Flash: a 552B-parameter MoE (asymmetric causal encoder-decoder) with native multimodal vision, 1M context and up to 384K output, thinking mode on by default, connected to DeepSeek directly. Billed at DeepSeek's official peak / off-peak prices: full price on weekdays 9:00-12:00 and 14:00-18:00 Beijing time, half price at all other times, including weekends and public holidays.

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

对话（DeepSeek V4.1 Flash）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="deepseek-v4.1-flash",
    messages=[{"role": "user", "content": "用三句话介绍一下你自己"}],
)
print(resp.choices[0].message.content)
```

## English

3 DeepSeek models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (the DeepSeek V4 series). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: chat models through the OpenAI SDK at `https://api.dflop.top/v1`.

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
