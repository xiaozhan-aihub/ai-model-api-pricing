# MiniMax 海螺 API 价格与调用：MiniMax 对话、海螺 H3 视频

> MiniMax (Hailuo) API pricing on XiaoZhan AIhub: 8 models (MiniMax chat and Hailuo H3 video). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 MiniMax 海螺 模型共 8 个（对话大模型 1 个，视频生成 7 个），一把 `sk-gpushare-` 密钥全都能调：对话模型用 OpenAI SDK 改个 `base_url` 即可，视频是提交任务再轮询结果。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [大模型 API 价格对比](../pricing/llm-api.md) · [AI 视频生成 API 价格对比](../pricing/video-generation-api.md) · [官网厂商页](https://model.dflop.top/vendors/minimax)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [MiniMax M2.7](#MiniMax-M2.7) | `MiniMax-M2.7` | 对话大模型 | 输入 ¥2.022 / 输出 ¥10.11 每百万 token | 200K | — |
| [海螺 H3](#minimax-h3) | `minimax-h3` | 视频生成 | ¥0.8 / 秒 | — | — |
| [海螺 H3 Max](#minimax-h3-max) | `minimax-h3-max` | 视频生成 | ¥0.5 / 秒 | — | — |
| [海螺 H3 tx](#minimax-h3-tx) | `minimax-h3-tx` | 视频生成 | ¥0.5 / 秒 | — | — |
| [海螺 H3 提速版 tx](#minimax-h3-fast-tx) | `minimax-h3-fast-tx` | 视频生成 | ¥0.4 / 秒 | — | — |
| [海螺 H3 提速版带IR tx](#minimax-h3-fast-ir-tx) | `minimax-h3-fast-ir-tx` | 视频生成 | ¥0.4 / 秒 | — | — |
| [海螺 H3 满血版 tx](#minimax-h3-medium-tx) | `minimax-h3-medium-tx` | 视频生成 | ¥0.5 / 秒 | — | — |
| [海螺 H3 满血版带IR tx](#minimax-h3-medium-ir-tx) | `minimax-h3-medium-ir-tx` | 视频生成 | ¥0.5 / 秒 | — | — |

## 各模型详情

<a id="MiniMax-M2.7"></a>

### MiniMax M2.7

调用 ID `MiniMax-M2.7` · 对话大模型 · 上架 2026-03-15

MiniMax M2.7,200K 上下文。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 121.32 积分 ≈ ¥2.022 ≈ $0.3 |
| 输出 · 每百万 token | 606.6 积分 ≈ ¥10.11 ≈ $1.5 |
| 缓存命中输入 · 每百万 token | 24.26 积分 ≈ ¥0.4044 ≈ $0.06 |

- 上下文 200K token，最大输出 192K token
- 能力：工具调用、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions`
- 模型页：[model.dflop.top/models/MiniMax-M2.7](https://model.dflop.top/models/MiniMax-M2.7) · [English](https://model.dflop.top/en/models/MiniMax-M2.7) · [Markdown](https://model.dflop.top/models/MiniMax-M2.7.md)

> MiniMax M2.7. 200K context.

<a id="minimax-h3"></a>

### 海螺 H3

调用 ID `minimax-h3` · 视频生成 · 上架 2026-09-24

MiniMax 海螺 H3 视频生成(异步任务),原生立体声音频。4-15 秒,768P / 2K,画幅 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive。支持文生视频、首帧 / 首尾帧图生视频、全能参考(参考图 ≤9 张、参考视频 ≤3 段、参考音频 ≤3 段)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 48 积分 ≈ ¥0.8 ≈ $0.1187 |

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：768p（默认） / 2k
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 9 张、视频 3 段、音频 3 段
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/minimax-h3](https://model.dflop.top/models/minimax-h3) · [English](https://model.dflop.top/en/models/minimax-h3) · [Markdown](https://model.dflop.top/models/minimax-h3.md)

> MiniMax Hailuo H3 video generation (asynchronous task) with native stereo audio. 4-15 seconds, 768P / 2K, aspect ratios 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive. Text-to-video, first-frame and first-and-last-frame image-to-video, and all-round reference (up to 9 reference images, 3 reference videos and 3 reference audio clips).

<a id="minimax-h3-max"></a>

### 海螺 H3 Max

调用 ID `minimax-h3-max` · 视频生成 · 上架 2026-09-24

MiniMax 海螺 H3 Max 极速视频生成(异步任务),原生立体声音频。5-15 秒,480P / 768P,画幅 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive。支持文生视频与首帧 / 首尾帧图生视频(不支持全能参考)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 30 积分 ≈ ¥0.5 ≈ $0.07418 |

- 生成方式：文生视频、图生视频、首尾帧
- 分辨率：480p（默认） / 768p
- 时长：5–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/minimax-h3-max](https://model.dflop.top/models/minimax-h3-max) · [English](https://model.dflop.top/en/models/minimax-h3-max) · [Markdown](https://model.dflop.top/models/minimax-h3-max.md)

> MiniMax Hailuo H3 Max, express video generation (asynchronous task) with native stereo audio. 5-15 seconds, 480P / 768P, aspect ratios 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive. Text-to-video and first-frame or first-and-last-frame image-to-video (no all-round reference).

<a id="minimax-h3-tx"></a>

### 海螺 H3 tx

调用 ID `minimax-h3-tx` · 视频生成 · 上架 2026-10-14

MiniMax 海螺 H3 视频生成(异步任务),原生音频可关闭。4-15 秒,768P / 720P,画幅 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive。支持文生视频、首帧 / 尾帧 / 首尾帧图生视频、全能参考(参考图 ≤9 张、参考视频 ≤3 段、参考音频 ≤3 段)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 30 积分 ≈ ¥0.5 ≈ $0.07418 |

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p / 768p（默认）
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 9 张、视频 3 段、音频 3 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/minimax-h3-tx](https://model.dflop.top/models/minimax-h3-tx) · [English](https://model.dflop.top/en/models/minimax-h3-tx) · [Markdown](https://model.dflop.top/models/minimax-h3-tx.md)

> MiniMax Hailuo H3 video generation (asynchronous task); native audio can be turned off. 4-15 seconds, 768P / 720P, aspect ratios 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive. Text-to-video, first-frame, last-frame and first-and-last-frame image-to-video, and all-round reference (up to 9 reference images, 3 reference videos and 3 reference audio clips).

<a id="minimax-h3-fast-tx"></a>

### 海螺 H3 提速版 tx

调用 ID `minimax-h3-fast-tx` · 视频生成 · 上架 2026-10-27

MiniMax 海螺 H3 视频生成(异步任务),原生音频可关闭。4-15 秒,768P / 720P / 480P,画幅 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive。支持文生视频、首帧 / 尾帧 / 首尾帧图生视频、全能参考(参考图 ≤9 张、参考视频 ≤3 段、参考音频 ≤3 段)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 24 积分 ≈ ¥0.4 ≈ $0.05935 |

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：480p / 720p / 768p（默认）
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 9 张、视频 3 段、音频 3 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/minimax-h3-fast-tx](https://model.dflop.top/models/minimax-h3-fast-tx) · [English](https://model.dflop.top/en/models/minimax-h3-fast-tx) · [Markdown](https://model.dflop.top/models/minimax-h3-fast-tx.md)

> MiniMax Hailuo H3 video generation (asynchronous task); native audio can be turned off. 4-15 seconds, 768P / 720P / 480P, aspect ratios 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive. Text-to-video, first-frame, last-frame and first-and-last-frame image-to-video, and all-round reference (up to 9 reference images, 3 reference videos and 3 reference audio clips).

<a id="minimax-h3-fast-ir-tx"></a>

### 海螺 H3 提速版带IR tx

调用 ID `minimax-h3-fast-ir-tx` · 视频生成 · 上架 2026-10-27

MiniMax 海螺 H3 视频生成(异步任务),原生音频可关闭。4-15 秒,768P / 720P / 480P,画幅 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive。支持文生视频、首帧 / 尾帧 / 首尾帧图生视频、全能参考(参考图 ≤9 张、参考视频 ≤3 段、参考音频 ≤3 段)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 24 积分 ≈ ¥0.4 ≈ $0.05935 |

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：480p / 720p / 768p（默认）
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 9 张、视频 3 段、音频 3 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/minimax-h3-fast-ir-tx](https://model.dflop.top/models/minimax-h3-fast-ir-tx) · [English](https://model.dflop.top/en/models/minimax-h3-fast-ir-tx) · [Markdown](https://model.dflop.top/models/minimax-h3-fast-ir-tx.md)

> MiniMax Hailuo H3 video generation (asynchronous task); native audio can be turned off. 4-15 seconds, 768P / 720P / 480P, aspect ratios 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive. Text-to-video, first-frame, last-frame and first-and-last-frame image-to-video, and all-round reference (up to 9 reference images, 3 reference videos and 3 reference audio clips).

<a id="minimax-h3-medium-tx"></a>

### 海螺 H3 满血版 tx

调用 ID `minimax-h3-medium-tx` · 视频生成 · 上架 2026-10-27

MiniMax 海螺 H3 视频生成(异步任务),原生音频可关闭。4-15 秒,768P / 720P,画幅 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive。支持文生视频、首帧 / 尾帧 / 首尾帧图生视频、全能参考(参考图 ≤9 张、参考视频 ≤3 段、参考音频 ≤3 段)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 30 积分 ≈ ¥0.5 ≈ $0.07418 |

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p / 768p（默认）
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 9 张、视频 3 段、音频 3 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/minimax-h3-medium-tx](https://model.dflop.top/models/minimax-h3-medium-tx) · [English](https://model.dflop.top/en/models/minimax-h3-medium-tx) · [Markdown](https://model.dflop.top/models/minimax-h3-medium-tx.md)

> MiniMax Hailuo H3 video generation (asynchronous task); native audio can be turned off. 4-15 seconds, 768P / 720P, aspect ratios 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive. Text-to-video, first-frame, last-frame and first-and-last-frame image-to-video, and all-round reference (up to 9 reference images, 3 reference videos and 3 reference audio clips).

<a id="minimax-h3-medium-ir-tx"></a>

### 海螺 H3 满血版带IR tx

调用 ID `minimax-h3-medium-ir-tx` · 视频生成 · 上架 2026-10-27

MiniMax 海螺 H3 视频生成(异步任务),原生音频可关闭。4-15 秒,768P / 720P,画幅 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive。支持文生视频、首帧 / 尾帧 / 首尾帧图生视频、全能参考(参考图 ≤9 张、参考视频 ≤3 段、参考音频 ≤3 段)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 30 积分 ≈ ¥0.5 ≈ $0.07418 |

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p / 768p（默认）
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 9 张、视频 3 段、音频 3 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/minimax-h3-medium-ir-tx](https://model.dflop.top/models/minimax-h3-medium-ir-tx) · [English](https://model.dflop.top/en/models/minimax-h3-medium-ir-tx) · [Markdown](https://model.dflop.top/models/minimax-h3-medium-ir-tx.md)

> MiniMax Hailuo H3 video generation (asynchronous task); native audio can be turned off. 4-15 seconds, 768P / 720P, aspect ratios 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive. Text-to-video, first-frame, last-frame and first-and-last-frame image-to-video, and all-round reference (up to 9 reference images, 3 reference videos and 3 reference audio clips).

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

对话（MiniMax M2.7）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="MiniMax-M2.7",
    messages=[{"role": "user", "content": "用三句话介绍一下你自己"}],
)
print(resp.choices[0].message.content)
```

视频（海螺 H3）：

```python
import os, time, uuid
import requests

BASE = "https://api.dflop.top/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"}

r = requests.post(
    f"{BASE}/videos/generations",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},  # 重试用同一把键，不会重复扣费
    json={
        "model": "minimax-h3",
        "content": [{"type": "text", "text": "海边日落，无人机航拍视角"}],
        "duration": 5,
        "resolution": "768p",
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

8 MiniMax (Hailuo) models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (MiniMax chat and Hailuo H3 video). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: chat models through the OpenAI SDK at `https://api.dflop.top/v1`; video models as asynchronous tasks (`/v1/videos/generations`).

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
