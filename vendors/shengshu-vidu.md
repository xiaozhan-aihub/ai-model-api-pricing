# 生数科技 Vidu API 价格与调用：Vidu Q3 视频

> ShengShu (Vidu) API pricing on XiaoZhan AIhub: 6 models (Vidu Q3 video). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 生数科技 Vidu 模型共 6 个（视频生成 6 个），一把 `sk-gpushare-` 密钥全都能调：视频是提交任务再轮询结果。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [AI 视频生成 API 价格对比](../pricing/video-generation-api.md) · [官网厂商页](https://model.dflop.top/vendors/shengshu)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [Vidu Q3](#tvod-vidu-video-q3) | `tvod-vidu-video-q3` | 视频生成 | ¥0.3774 / 秒 | — | 8 折 |
| [Vidu Q3 Mix](#tvod-vidu-video-q3-mix) | `tvod-vidu-video-q3-mix` | 视频生成 | ¥0.3774 / 秒 | — | 8 折 |
| [Vidu Q3 Pro](#tvod-vidu-video-q3-pro) | `tvod-vidu-video-q3-pro` | 视频生成 | ¥0.3774 / 秒 | — | 8 折 |
| [Vidu Q3 Turbo](#tvod-vidu-video-q3-turbo) | `tvod-vidu-video-q3-turbo` | 视频生成 | ¥0.3774 / 秒 | — | 8 折 |
| [Vidu Q3 广告版](#tvod-vidu-video-q3-ad) | `tvod-vidu-video-q3-ad` | 视频生成 | ¥0.3774 / 秒 | — | 8 折 |
| [Vidu Q3 短剧版](#tvod-vidu-video-q3-drama) | `tvod-vidu-video-q3-drama` | 视频生成 | ¥0.3774 / 秒 | — | 8 折 |

## 各模型详情

<a id="tvod-vidu-video-q3"></a>

### Vidu Q3

调用 ID `tvod-vidu-video-q3` · 视频生成 · 上架 2026-06-26

生数 Vidu 视频生成(异步任务)。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 22.65 积分 ≈ ¥0.3774 ≈ $0.056 | 28.31 积分 ≈ ¥0.4718 ≈ $0.07 |

现在是限时 8 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p / 4k
- 时长：1–10 秒
- 画幅：16:9 / 9:16 / 1:1
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-vidu-video-q3](https://model.dflop.top/models/tvod-vidu-video-q3) · [English](https://model.dflop.top/en/models/tvod-vidu-video-q3) · [Markdown](https://model.dflop.top/models/tvod-vidu-video-q3.md)

> Shengshu Vidu video generation (asynchronous task).

<a id="tvod-vidu-video-q3-mix"></a>

### Vidu Q3 Mix

调用 ID `tvod-vidu-video-q3-mix` · 视频生成 · 上架 2026-06-26

生数 Vidu 视频生成(异步任务)。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 22.65 积分 ≈ ¥0.3774 ≈ $0.056 | 28.31 积分 ≈ ¥0.4718 ≈ $0.07 |

现在是限时 8 折。

- 模型页：[model.dflop.top/models/tvod-vidu-video-q3-mix](https://model.dflop.top/models/tvod-vidu-video-q3-mix) · [English](https://model.dflop.top/en/models/tvod-vidu-video-q3-mix) · [Markdown](https://model.dflop.top/models/tvod-vidu-video-q3-mix.md)

> Shengshu Vidu video generation (asynchronous task).

<a id="tvod-vidu-video-q3-pro"></a>

### Vidu Q3 Pro

调用 ID `tvod-vidu-video-q3-pro` · 视频生成 · 上架 2026-06-26

生数 Vidu 视频生成(异步任务)。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 22.65 积分 ≈ ¥0.3774 ≈ $0.056 | 28.31 积分 ≈ ¥0.4718 ≈ $0.07 |

现在是限时 8 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p / 4k
- 时长：1–10 秒
- 画幅：16:9 / 9:16 / 1:1
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-vidu-video-q3-pro](https://model.dflop.top/models/tvod-vidu-video-q3-pro) · [English](https://model.dflop.top/en/models/tvod-vidu-video-q3-pro) · [Markdown](https://model.dflop.top/models/tvod-vidu-video-q3-pro.md)

> Shengshu Vidu video generation (asynchronous task).

<a id="tvod-vidu-video-q3-turbo"></a>

### Vidu Q3 Turbo

调用 ID `tvod-vidu-video-q3-turbo` · 视频生成 · 上架 2026-06-26

生数 Vidu 视频生成(异步任务)。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 22.65 积分 ≈ ¥0.3774 ≈ $0.056 | 28.31 积分 ≈ ¥0.4718 ≈ $0.07 |

现在是限时 8 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p
- 时长：1–10 秒
- 画幅：16:9 / 9:16 / 1:1
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-vidu-video-q3-turbo](https://model.dflop.top/models/tvod-vidu-video-q3-turbo) · [English](https://model.dflop.top/en/models/tvod-vidu-video-q3-turbo) · [Markdown](https://model.dflop.top/models/tvod-vidu-video-q3-turbo.md)

> Shengshu Vidu video generation (asynchronous task).

<a id="tvod-vidu-video-q3-ad"></a>

### Vidu Q3 广告版

调用 ID `tvod-vidu-video-q3-ad` · 视频生成 · 上架 2026-06-26

生数 Vidu 视频生成(异步任务)。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 22.65 积分 ≈ ¥0.3774 ≈ $0.056 | 28.31 积分 ≈ ¥0.4718 ≈ $0.07 |

现在是限时 8 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p / 4k
- 时长：1–10 秒
- 画幅：16:9 / 9:16 / 1:1
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-vidu-video-q3-ad](https://model.dflop.top/models/tvod-vidu-video-q3-ad) · [English](https://model.dflop.top/en/models/tvod-vidu-video-q3-ad) · [Markdown](https://model.dflop.top/models/tvod-vidu-video-q3-ad.md)

> Shengshu Vidu video generation (asynchronous task).

<a id="tvod-vidu-video-q3-drama"></a>

### Vidu Q3 短剧版

调用 ID `tvod-vidu-video-q3-drama` · 视频生成 · 上架 2026-06-26

生数 Vidu 视频生成(异步任务)。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 22.65 积分 ≈ ¥0.3774 ≈ $0.056 | 28.31 积分 ≈ ¥0.4718 ≈ $0.07 |

现在是限时 8 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p / 4k
- 时长：1–10 秒
- 画幅：16:9 / 9:16 / 1:1
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/tvod-vidu-video-q3-drama](https://model.dflop.top/models/tvod-vidu-video-q3-drama) · [English](https://model.dflop.top/en/models/tvod-vidu-video-q3-drama) · [Markdown](https://model.dflop.top/models/tvod-vidu-video-q3-drama.md)

> Shengshu Vidu video generation (asynchronous task).

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

视频（Vidu Q3）：

```python
import os, time, uuid
import requests

BASE = "https://api.dflop.top/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"}

r = requests.post(
    f"{BASE}/videos/generations",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},  # 重试用同一把键，不会重复扣费
    json={
        "model": "tvod-vidu-video-q3",
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

6 ShengShu (Vidu) models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (Vidu Q3 video). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: video models as asynchronous tasks (`/v1/videos/generations`).

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
