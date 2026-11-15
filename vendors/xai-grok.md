# xAI Grok API 价格与调用：Grok 对话、Grok Imagine 图像与视频

> xAI (Grok) API pricing on XiaoZhan AIhub: 7 models (Grok chat and Grok Imagine image and video). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 xAI Grok 模型共 7 个（对话大模型 3 个，图像生成 2 个，视频生成 2 个），一把 `sk-gpushare-` 密钥全都能调：对话模型用 OpenAI SDK 改个 `base_url` 即可，生图走 OpenAI Images 接口，视频是提交任务再轮询结果。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [大模型 API 价格对比](../pricing/llm-api.md) · [AI 生图 API 价格对比](../pricing/image-generation-api.md) · [AI 视频生成 API 价格对比](../pricing/video-generation-api.md) · [官网厂商页](https://model.dflop.top/vendors/xai)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [Grok 4.5](#grok-4.5) | `grok-4.5` | 对话大模型 | 输入 ¥4.044 / 输出 ¥12.13 每百万 token | 500K | 3 折 |
| [Grok 4.6](#grok-4.6) | `grok-4.6` | 对话大模型 | 输入 ¥4.044 / 输出 ¥12.13 每百万 token | 500K | 3 折 |
| [Grok 4.7](#grok-4.7) | `grok-4.7` | 对话大模型 | 输入 ¥4.044 / 输出 ¥12.13 每百万 token | 500K | 3 折 |
| [Grok Imagine (Image · Quality)](#grok-imagine-image-quality) | `grok-imagine-image-quality` | 图像生成 | ¥0.3 / 张 | — | — |
| [Grok Imagine (Image)](#grok-imagine-image) | `grok-imagine-image` | 图像生成 | ¥0.3 / 张 | — | — |
| [Grok Imagine Video](#grok-imagine-video) | `grok-imagine-video` | 视频生成 | ¥0.1 / 秒 | — | — |
| [Grok Imagine Video 1.5](#grok-imagine-video-1.5-preview) | `grok-imagine-video-1.5-preview` | 视频生成 | ¥0.1 / 秒 | — | — |

## 各模型详情

<a id="grok-4.5"></a>

### Grok 4.5

调用 ID `grok-4.5` · 对话大模型 · 上架 2026-07-09

xAI Grok 4.5 旗舰, 500K 上下文, 推理+多模态, 可在 playground 中直接生成视频..

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 242.64 积分 ≈ ¥4.044 ≈ $0.6 | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 727.92 积分 ≈ ¥12.13 ≈ $1.8 | 2426.4 积分 ≈ ¥40.44 ≈ $6 |
| 缓存命中输入 · 每百万 token | 36.4 积分 ≈ ¥0.6066 ≈ $0.09 | 121.32 积分 ≈ ¥2.022 ≈ $0.3 |

现在是限时 3 折。

- 上下文 500K token，最大输出 128K token
- 能力：读图、读视频、工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/grok-4.5](https://model.dflop.top/models/grok-4.5) · [English](https://model.dflop.top/en/models/grok-4.5) · [Markdown](https://model.dflop.top/models/grok-4.5.md)

> xAI Grok 4.5 flagship. 500K context, reasoning and multimodal input, and video generation right in the playground.

<a id="grok-4.6"></a>

### Grok 4.6

调用 ID `grok-4.6` · 对话大模型 · 上架 2026-08-12

xAI Grok 4.6 最新旗舰, 500K 上下文, 推理+多模态, 可在 playground 中直接生成视频.

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 242.64 积分 ≈ ¥4.044 ≈ $0.6 | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 727.92 积分 ≈ ¥12.13 ≈ $1.8 | 2426.4 积分 ≈ ¥40.44 ≈ $6 |
| 缓存命中输入 · 每百万 token | 60.66 积分 ≈ ¥1.011 ≈ $0.15 | 202.2 积分 ≈ ¥3.37 ≈ $0.5 |

现在是限时 3 折。

- 上下文 500K token，最大输出 128K token
- 能力：读图、读视频、工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/grok-4.6](https://model.dflop.top/models/grok-4.6) · [English](https://model.dflop.top/en/models/grok-4.6) · [Markdown](https://model.dflop.top/models/grok-4.6.md)

> xAI Grok 4.6 flagship. 500K context, reasoning and multimodal input, and video generation right in the playground.

<a id="grok-4.7"></a>

### Grok 4.7

调用 ID `grok-4.7` · 对话大模型 · 上架 2026-09-21

xAI Grok 4.7 最新旗舰, 500K 上下文, 推理 + 读图 + 读视频, 可在 playground 中直接生成视频.

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 242.64 积分 ≈ ¥4.044 ≈ $0.6 | 808.8 积分 ≈ ¥13.48 ≈ $2 |
| 输出 · 每百万 token | 727.92 积分 ≈ ¥12.13 ≈ $1.8 | 2426.4 积分 ≈ ¥40.44 ≈ $6 |
| 缓存命中输入 · 每百万 token | 60.66 积分 ≈ ¥1.011 ≈ $0.15 | 202.2 积分 ≈ ¥3.37 ≈ $0.5 |

现在是限时 3 折。

- 上下文 500K token，最大输出 128K token
- 能力：读图、读视频、工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/grok-4.7](https://model.dflop.top/models/grok-4.7) · [English](https://model.dflop.top/en/models/grok-4.7) · [Markdown](https://model.dflop.top/models/grok-4.7.md)

> xAI Grok 4.7, the latest flagship. 500K context, reasoning, image and video understanding, and video generation right in the playground.

<a id="grok-imagine-image-quality"></a>

### Grok Imagine (Image · Quality)

调用 ID `grok-imagine-image-quality` · 图像生成 · 上架 2025-01-01

xAI Grok Imagine 图片生成 (高质量). /v1/images/generations.

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 18 积分 ≈ ¥0.3 ≈ $0.04451 |

- 尺寸：尺寸档 1K / 2K / 4K，尺寸下限约 1920×1920
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 9 张、图生图最多 50 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/grok-imagine-image-quality](https://model.dflop.top/models/grok-imagine-image-quality) · [English](https://model.dflop.top/en/models/grok-imagine-image-quality) · [Markdown](https://model.dflop.top/models/grok-imagine-image-quality.md)

> xAI Grok Imagine image generation (high quality). /v1/images/generations.

<a id="grok-imagine-image"></a>

### Grok Imagine (Image)

调用 ID `grok-imagine-image` · 图像生成 · 上架 2025-01-01

xAI Grok Imagine 图片生成 (标准). /v1/images/generations.

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 18 积分 ≈ ¥0.3 ≈ $0.04451 |

- 尺寸：尺寸档 1K / 2K / 4K，尺寸下限约 1920×1920
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 9 张、图生图最多 50 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/grok-imagine-image](https://model.dflop.top/models/grok-imagine-image) · [English](https://model.dflop.top/en/models/grok-imagine-image) · [Markdown](https://model.dflop.top/models/grok-imagine-image.md)

> xAI Grok Imagine image generation (standard). /v1/images/generations.

<a id="grok-imagine-video"></a>

### Grok Imagine Video

调用 ID `grok-imagine-video` · 视频生成 · 上架 2025-01-01

xAI Grok Imagine 文生视频 (异步任务).

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 6 积分 ≈ ¥0.1 ≈ $0.01484 |

- 生成方式：文生视频、图生视频、参考图/视频生视频
- 分辨率：720p（默认） / 1080p
- 时长：1–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 3:2 / 2:3
- 参考素材：图片最多 7 张、视频 1 段
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/grok-imagine-video](https://model.dflop.top/models/grok-imagine-video) · [English](https://model.dflop.top/en/models/grok-imagine-video) · [Markdown](https://model.dflop.top/models/grok-imagine-video.md)

> xAI Grok Imagine text-to-video (asynchronous task).

<a id="grok-imagine-video-1.5-preview"></a>

### Grok Imagine Video 1.5

调用 ID `grok-imagine-video-1.5-preview` · 视频生成 · 上架 2025-01-01

xAI Grok Imagine 1.5 视频生成 (异步任务, 支持文生 / 图生 / 多图参考).

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 6 积分 ≈ ¥0.1 ≈ $0.01484 |

- 生成方式：文生视频、图生视频、参考图/视频生视频
- 分辨率：720p（默认） / 1080p
- 时长：1–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 3:2 / 2:3
- 参考素材：图片最多 7 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/grok-imagine-video-1.5-preview](https://model.dflop.top/models/grok-imagine-video-1.5-preview) · [English](https://model.dflop.top/en/models/grok-imagine-video-1.5-preview) · [Markdown](https://model.dflop.top/models/grok-imagine-video-1.5-preview.md)

> xAI Grok Imagine 1.5 video generation (asynchronous task; text-to-video, image-to-video and multi-image reference).

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

对话（Grok 4.7）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="grok-4.7",
    messages=[{"role": "user", "content": "用三句话介绍一下你自己"}],
)
print(resp.choices[0].message.content)
```

生图（Grok Imagine (Image)）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"], timeout=300)

result = client.images.generate(
    model="grok-imagine-image",
    prompt="一只在竹林里喝茶的熊猫，水彩风格",
    size="2048x2048",
)
print(result.data[0].url)  # 临时链接（约 24 小时），请转存
```

视频（Grok Imagine Video）：

```python
import os, time, uuid
import requests

BASE = "https://api.dflop.top/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"}

r = requests.post(
    f"{BASE}/videos/generations",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},  # 重试用同一把键，不会重复扣费
    json={
        "model": "grok-imagine-video",
        "content": [{"type": "text", "text": "海边日落，无人机航拍视角"}],
        "duration": 5,
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

7 xAI (Grok) models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (Grok chat and Grok Imagine image and video). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: chat models through the OpenAI SDK at `https://api.dflop.top/v1`; image models through the OpenAI Images API (`/v1/images/generations`); video models as asynchronous tasks (`/v1/videos/generations`).

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
