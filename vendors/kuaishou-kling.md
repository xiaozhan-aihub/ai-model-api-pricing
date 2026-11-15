# 快手 可灵 API 价格与调用：可灵 Kling 视频与图像

> Kuaishou (Kling) API pricing on XiaoZhan AIhub: 7 models (Kling video and image). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 快手 可灵 模型共 7 个（图像生成 2 个，视频生成 5 个），一把 `sk-gpushare-` 密钥全都能调：生图走 OpenAI Images 接口，视频是提交任务再轮询结果。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [AI 生图 API 价格对比](../pricing/image-generation-api.md) · [AI 视频生成 API 价格对比](../pricing/video-generation-api.md) · [官网厂商页](https://model.dflop.top/vendors/kuaishou)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [可灵图像 3.0](#tvod-kling-image-3.0) | `tvod-kling-image-3.0` | 图像生成 | ¥0.337 / 张 | — | — |
| [可灵图像 3.0 Omni](#tvod-kling-image-3.0-omni) | `tvod-kling-image-3.0-omni` | 图像生成 | ¥0.4044 / 张 | — | — |
| [可灵 3.0](#tvod-kling-video-3.0) | `tvod-kling-video-3.0` | 视频生成 | ¥0.5392 / 秒 | — | — |
| [可灵 3.0 Omni](#tvod-kling-video-3.0-omni) | `tvod-kling-video-3.0-omni` | 视频生成 | ¥0.5392 / 秒 | — | — |
| [可灵 4.0](#tvod-kling-video-4.0) | `tvod-kling-video-4.0` | 视频生成 | ¥1.14 / 秒 | — | 9.5 折 |
| [可灵 4.0 Omni](#tvod-kling-video-4.0-omni) | `tvod-kling-video-4.0-omni` | 视频生成 | ¥1.14 / 秒 | — | 9.5 折 |
| [可灵 O1](#tvod-kling-video-o1) | `tvod-kling-video-o1` | 视频生成 | ¥0.337 / 秒 | — | — |

## 各模型详情

<a id="tvod-kling-image-3.0"></a>

### 可灵图像 3.0

调用 ID `tvod-kling-image-3.0` · 图像生成 · 上架 2026-06-26

快手可灵图像 3.0。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 20.22 积分 ≈ ¥0.337 ≈ $0.05 |

- 尺寸：尺寸档 1K / 2K / 4K，尺寸下限约 1920×1920
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 9 张、图生图最多 50 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/tvod-kling-image-3.0](https://model.dflop.top/models/tvod-kling-image-3.0) · [English](https://model.dflop.top/en/models/tvod-kling-image-3.0) · [Markdown](https://model.dflop.top/models/tvod-kling-image-3.0.md)

> Kuaishou Kling image 3.0.

<a id="tvod-kling-image-3.0-omni"></a>

### 可灵图像 3.0 Omni

调用 ID `tvod-kling-image-3.0-omni` · 图像生成 · 上架 2026-06-26

快手可灵图像 3.0 Omni(全能版)。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 24.26 积分 ≈ ¥0.4044 ≈ $0.06 |

- 尺寸：尺寸档 1K / 2K / 4K，尺寸下限约 1920×1920
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 9 张、图生图最多 50 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/tvod-kling-image-3.0-omni](https://model.dflop.top/models/tvod-kling-image-3.0-omni) · [English](https://model.dflop.top/en/models/tvod-kling-image-3.0-omni) · [Markdown](https://model.dflop.top/models/tvod-kling-image-3.0-omni.md)

> Kuaishou Kling image 3.0 Omni.

<a id="tvod-kling-video-3.0"></a>

### 可灵 3.0

调用 ID `tvod-kling-video-3.0` · 视频生成 · 上架 2026-06-26

快手可灵 视频生成(异步任务)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 32.35 积分 ≈ ¥0.5392 ≈ $0.08 |

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p / 4k
- 时长：3–15 秒
- 画幅：16:9 / 9:16 / 1:1
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-kling-video-3.0](https://model.dflop.top/models/tvod-kling-video-3.0) · [English](https://model.dflop.top/en/models/tvod-kling-video-3.0) · [Markdown](https://model.dflop.top/models/tvod-kling-video-3.0.md)

> Kuaishou Kling video generation (asynchronous task).

<a id="tvod-kling-video-3.0-omni"></a>

### 可灵 3.0 Omni

调用 ID `tvod-kling-video-3.0-omni` · 视频生成 · 上架 2026-06-26

快手可灵 视频生成(异步任务)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 32.35 积分 ≈ ¥0.5392 ≈ $0.08 |

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p / 4k
- 时长：3–15 秒
- 画幅：16:9 / 9:16 / 1:1
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-kling-video-3.0-omni](https://model.dflop.top/models/tvod-kling-video-3.0-omni) · [English](https://model.dflop.top/en/models/tvod-kling-video-3.0-omni) · [Markdown](https://model.dflop.top/models/tvod-kling-video-3.0-omni.md)

> Kuaishou Kling video generation (asynchronous task).

<a id="tvod-kling-video-4.0"></a>

### 可灵 4.0

调用 ID `tvod-kling-video-4.0` · 视频生成 · 上架 2026-10-24

快手可灵 4.0 视频生成(异步任务)。3-30 秒整数时长,720P / 1080P / 2K / 4K,画幅 16:9 / 9:16 / 1:1 / 21:9,成片自带原生音频。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 68.4 积分 ≈ ¥1.14 ≈ $0.1691 | 72 积分 ≈ ¥1.2 ≈ $0.178 |

现在是限时 9.5 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p / 2k / 4k
- 时长：3–30 秒
- 画幅：16:9 / 9:16 / 1:1 / 21:9
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-kling-video-4.0](https://model.dflop.top/models/tvod-kling-video-4.0) · [English](https://model.dflop.top/en/models/tvod-kling-video-4.0) · [Markdown](https://model.dflop.top/models/tvod-kling-video-4.0.md)

> Kuaishou Kling 4.0 video generation (asynchronous task). Integer durations of 3-30 seconds, 720P / 1080P / 2K / 4K, aspect ratios 16:9 / 9:16 / 1:1 / 21:9, with native audio.

<a id="tvod-kling-video-4.0-omni"></a>

### 可灵 4.0 Omni

调用 ID `tvod-kling-video-4.0-omni` · 视频生成 · 上架 2026-10-24

快手可灵 4.0 Omni 视频生成(异步任务),支持多图参考。3-30 秒整数时长,720P / 1080P / 2K / 4K,画幅 16:9 / 9:16 / 1:1 / 21:9,成片自带原生音频。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 68.4 积分 ≈ ¥1.14 ≈ $0.1691 | 72 积分 ≈ ¥1.2 ≈ $0.178 |

现在是限时 9.5 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p / 2k / 4k
- 时长：3–30 秒
- 画幅：16:9 / 9:16 / 1:1 / 21:9
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-kling-video-4.0-omni](https://model.dflop.top/models/tvod-kling-video-4.0-omni) · [English](https://model.dflop.top/en/models/tvod-kling-video-4.0-omni) · [Markdown](https://model.dflop.top/models/tvod-kling-video-4.0-omni.md)

> Kuaishou Kling 4.0 Omni video generation (asynchronous task) with multi-image reference. Integer durations of 3-30 seconds, 720P / 1080P / 2K / 4K, aspect ratios 16:9 / 9:16 / 1:1 / 21:9, with native audio.

<a id="tvod-kling-video-o1"></a>

### 可灵 O1

调用 ID `tvod-kling-video-o1` · 视频生成 · 上架 2026-06-26

快手可灵 视频生成(异步任务)。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 20.22 积分 ≈ ¥0.337 ≈ $0.05 |

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p
- 时长：3–15 秒
- 画幅：16:9 / 9:16 / 1:1
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-kling-video-o1](https://model.dflop.top/models/tvod-kling-video-o1) · [English](https://model.dflop.top/en/models/tvod-kling-video-o1) · [Markdown](https://model.dflop.top/models/tvod-kling-video-o1.md)

> Kuaishou Kling video generation (asynchronous task).

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

生图（可灵图像 3.0）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"], timeout=300)

result = client.images.generate(
    model="tvod-kling-image-3.0",
    prompt="一只在竹林里喝茶的熊猫，水彩风格",
    size="2048x2048",
)
print(result.data[0].url)  # 临时链接（约 24 小时），请转存
```

视频（可灵 3.0）：

```python
import os, time, uuid
import requests

BASE = "https://api.dflop.top/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"}

r = requests.post(
    f"{BASE}/videos/generations",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},  # 重试用同一把键，不会重复扣费
    json={
        "model": "tvod-kling-video-3.0",
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

7 Kuaishou (Kling) models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (Kling video and image). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: image models through the OpenAI Images API (`/v1/images/generations`); video models as asynchronous tasks (`/v1/videos/generations`).

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
