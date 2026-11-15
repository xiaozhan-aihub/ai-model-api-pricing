# Suno API 价格与调用：Suno V6 AI 音乐

> Suno API pricing on XiaoZhan AIhub: 3 models (Suno V6 music). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 Suno 模型共 3 个（音乐与语音 3 个），一把 `sk-gpushare-` 密钥全都能调：音乐和语音各有专门的接口。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [AI 音乐生成与语音合成 API](../pricing/music-and-speech-api.md) · [官网厂商页](https://model.dflop.top/vendors/suno)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [Suno V6 (最新)](#suno-v6) | `suno-v6` | 音乐与语音 | 按次计费（一次生成 2 首） | — | — |
| [Suno V6 Mini](#suno-v6-mini) | `suno-v6-mini` | 音乐与语音 | 按次计费（一次生成 2 首） | — | — |
| [Suno V6 Wild](#suno-v6-wild) | `suno-v6-wild` | 音乐与语音 | 按次计费（一次生成 2 首） | — | — |

## 各模型详情

<a id="suno-v6"></a>

### Suno V6 (最新)

调用 ID `suno-v6` · 音乐与语音 · 上架 2026-11-12

Suno AI 音乐生成 V6 旗舰引擎,稳定、精致,各类曲风都拿得住。一次生成 2 首完整歌曲(含歌词与封面);支持灵感模式(一句描述成歌)与自定义歌词/曲风/纯音乐。POST /v1/music/generations 异步任务。

计费：按次计费（一次生成 2 首），价格见模型页。

- 一次生成 2 首完整歌曲（含歌词与封面），支持一句话描述成歌、自定义歌词、曲风与纯音乐
- 接口：`POST /v1/music/generations`（异步任务，轮询 `GET /v1/music/generations/{id}`）
- 模型页：[model.dflop.top/models/suno-v6](https://model.dflop.top/models/suno-v6) · [English](https://model.dflop.top/en/models/suno-v6) · [Markdown](https://model.dflop.top/models/suno-v6.md)

> Suno AI music generation, the V6 flagship engine: stable, polished and at home in any genre. Two complete songs per request (with lyrics and cover art); inspiration mode (a one-line description becomes a song) or custom lyrics, style and instrumentals. POST /v1/music/generations, asynchronous task.

<a id="suno-v6-mini"></a>

### Suno V6 Mini

调用 ID `suno-v6-mini` · 音乐与语音 · 上架 2026-11-12

Suno AI 音乐生成 V6 Mini 引擎,更快、更省,适合先打个样。一次生成 2 首完整歌曲(含歌词与封面);支持灵感模式(一句描述成歌)与自定义歌词/曲风/纯音乐。POST /v1/music/generations 异步任务。

计费：按次计费（一次生成 2 首），价格见模型页。

- 一次生成 2 首完整歌曲（含歌词与封面），支持一句话描述成歌、自定义歌词、曲风与纯音乐
- 接口：`POST /v1/music/generations`（异步任务，轮询 `GET /v1/music/generations/{id}`）
- 模型页：[model.dflop.top/models/suno-v6-mini](https://model.dflop.top/models/suno-v6-mini) · [English](https://model.dflop.top/en/models/suno-v6-mini) · [Markdown](https://model.dflop.top/models/suno-v6-mini.md)

> Suno AI music generation, V6 Mini engine: faster and cheaper, good for a first draft. Two complete songs per request (with lyrics and cover art); inspiration mode (a one-line description becomes a song) or custom lyrics, style and instrumentals. POST /v1/music/generations, asynchronous task.

<a id="suno-v6-wild"></a>

### Suno V6 Wild

调用 ID `suno-v6-wild` · 音乐与语音 · 上架 2026-11-12

Suno AI 音乐生成 V6 Wild 引擎,更大胆、更多变,适合探索意料之外的效果。一次生成 2 首完整歌曲(含歌词与封面);支持灵感模式(一句描述成歌)与自定义歌词/曲风/纯音乐。POST /v1/music/generations 异步任务。

计费：按次计费（一次生成 2 首），价格见模型页。

- 一次生成 2 首完整歌曲（含歌词与封面），支持一句话描述成歌、自定义歌词、曲风与纯音乐
- 接口：`POST /v1/music/generations`（异步任务，轮询 `GET /v1/music/generations/{id}`）
- 模型页：[model.dflop.top/models/suno-v6-wild](https://model.dflop.top/models/suno-v6-wild) · [English](https://model.dflop.top/en/models/suno-v6-wild) · [Markdown](https://model.dflop.top/models/suno-v6-wild.md)

> Suno AI music generation, V6 Wild engine: bolder and more varied, for exploring unexpected results. Two complete songs per request (with lyrics and cover art); inspiration mode (a one-line description becomes a song) or custom lyrics, style and instrumentals. POST /v1/music/generations, asynchronous task.

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

音乐（Suno V6 (最新)）：

```python
import os, time, uuid
import requests

BASE = "https://api.dflop.top/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"}

r = requests.post(
    f"{BASE}/music/generations",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},
    json={"model": "suno-v6", "prompt": "一首关于夏天海边散步的轻快中文流行歌"},
    timeout=60,
)
r.raise_for_status()
task = r.json()

while task["status"] not in ("succeeded", "failed", "expired", "cancelled"):
    time.sleep(15)  # 一般 2–4 分钟
    task = requests.get(f"{BASE}/music/generations/{task['id']}", headers=HEADERS, timeout=30).json()

for track in task.get("tracks", []):  # 一次 2 首
    print(track["title"], track["audio_url"])
```

## English

3 Suno models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (Suno V6 music). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: music and speech through `/v1/music/generations` and `/v1/audio/speech`.

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
