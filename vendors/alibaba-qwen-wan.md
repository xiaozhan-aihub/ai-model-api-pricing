# 阿里巴巴 通义 API 价格与调用：通义千问 Qwen、Qwen Image、通义万相 Wan 视频、快乐马视频

> Alibaba (Qwen, Wan) API pricing on XiaoZhan AIhub: 9 models (Qwen, Qwen Image, Wan video and HappyHorse video). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 阿里巴巴 通义 模型共 9 个（对话大模型 2 个，图像生成 2 个，视频生成 5 个），一把 `sk-gpushare-` 密钥全都能调：对话模型用 OpenAI SDK 改个 `base_url` 即可，生图走 OpenAI Images 接口，视频是提交任务再轮询结果。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [大模型 API 价格对比](../pricing/llm-api.md) · [AI 生图 API 价格对比](../pricing/image-generation-api.md) · [AI 视频生成 API 价格对比](../pricing/video-generation-api.md) · [官网厂商页](https://model.dflop.top/vendors/alibaba)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [Qwen3.8-Max-cjx](#qwen3.8-max-cjx) | `qwen3.8-max-cjx` | 对话大模型 | 输入 ¥8.4 / 输出 ¥25.2 每百万 token | 1M | 7 折 |
| [Qwen3.8-Omni-Flash](#qwen3.8-omni-flash) | `qwen3.8-omni-flash` | 对话大模型 | 输入 ¥0.8 / 输出 ¥2.7 每百万 token | 1M | — |
| [Qwen Image 3.0](#qwen-image-3.0) | `qwen-image-3.0` | 图像生成 | ¥0.18 / 张 | — | — |
| [Qwen Image 3.0 Pro](#qwen-image-3.0-pro) | `qwen-image-3.0-pro` | 图像生成 | ¥0.25 / 张 | — | — |
| [万相 3.0 视频生成](#wan3.0-video) | `wan3.0-video` | 视频生成 | ¥1.08 / 秒 | — | 9 折 |
| [万相 3.0 视频生成 Prime](#wan3.0-video-prime) | `wan3.0-video-prime` | 视频生成 | ¥1.62 / 秒 | — | 9 折 |
| [快乐马 1.1 全能参考](#happyhorse-1.1-r2v) | `happyhorse-1.1-r2v` | 视频生成 | ¥1.2 / 秒 | — | — |
| [快乐马 1.1 图生视频](#happyhorse-1.1-i2v) | `happyhorse-1.1-i2v` | 视频生成 | ¥1.2 / 秒 | — | — |
| [快乐马 1.1 文生视频](#happyhorse-1.1-t2v) | `happyhorse-1.1-t2v` | 视频生成 | ¥1.2 / 秒 | — | — |

## 各模型详情

<a id="qwen3.8-max-cjx"></a>

### Qwen3.8-Max-cjx

调用 ID `qwen3.8-max-cjx` · 对话大模型 · 上架 2026-08-03

通义千问 Qwen3.8-Max(cjx 线路)—— 1M 上下文,默认思考,支持读图与工具调用,按阿里云百炼官方价计费。OpenAI Chat / Responses 双协议。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 输入 · 每百万 token | 504 积分 ≈ ¥8.4 ≈ $1.246 | 720 积分 ≈ ¥12 ≈ $1.78 |
| 输出 · 每百万 token | 1512 积分 ≈ ¥25.2 ≈ $3.739 | 2160 积分 ≈ ¥36 ≈ $5.341 |
| 缓存命中输入 · 每百万 token | 63 积分 ≈ ¥1.05 ≈ $0.1558 | 90 积分 ≈ ¥1.5 ≈ $0.2226 |

现在是限时 7 折。

- 上下文 1M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/qwen3.8-max-cjx](https://model.dflop.top/models/qwen3.8-max-cjx) · [English](https://model.dflop.top/en/models/qwen3.8-max-cjx) · [Markdown](https://model.dflop.top/models/qwen3.8-max-cjx.md)

> Alibaba Qwen3.8-Max (cjx line). 1M context, thinking on by default, image input and tool calling, billed at Alibaba Cloud Model Studio's list price. OpenAI Chat and Responses protocols.

<a id="qwen3.8-omni-flash"></a>

### Qwen3.8-Omni-Flash

调用 ID `qwen3.8-omni-flash` · 对话大模型 · 上架 2026-09-09

通义千问 Qwen3.8-Omni-Flash —— 原生全模态 Flash 档,1M 上下文,可直接输入文本/图像/音频/视频并按统一的一口价计费,带思考链路。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 48 积分 ≈ ¥0.8 ≈ $0.1187 |
| 输出 · 每百万 token | 162 积分 ≈ ¥2.7 ≈ $0.4006 |
| 缓存命中输入 · 每百万 token | 6 积分 ≈ ¥0.1 ≈ $0.01484 |

- 上下文 1M token，最大输出 32K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh）、JSON 模式、前缀续写
- 接口：OpenAI Chat Completions `POST /v1/chat/completions`
- 模型页：[model.dflop.top/models/qwen3.8-omni-flash](https://model.dflop.top/models/qwen3.8-omni-flash) · [English](https://model.dflop.top/en/models/qwen3.8-omni-flash) · [Markdown](https://model.dflop.top/models/qwen3.8-omni-flash.md)

> Alibaba Qwen3.8-Omni-Flash: the natively omni-modal Flash tier with 1M context. Takes text, images, audio and video directly at one flat price, with a thinking chain.

<a id="qwen-image-3.0"></a>

### Qwen Image 3.0

调用 ID `qwen-image-3.0` · 图像生成 · 上架 2026-09-04

阿里通义千问 Qwen Image 3.0 图像生成(同步)。文生图 / 图生图(参考图改图),尺寸 512×512 ~ 2560×2560 任意长宽,单次最多 6 张。1K/2K 同价。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 10.8 积分 ≈ ¥0.18 ≈ $0.02671 |

- 尺寸：尺寸档 1K / 2K / 4K，尺寸下限约 1920×1920
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 9 张、图生图最多 50 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/qwen-image-3.0](https://model.dflop.top/models/qwen-image-3.0) · [English](https://model.dflop.top/en/models/qwen-image-3.0) · [Markdown](https://model.dflop.top/models/qwen-image-3.0.md)

> Alibaba Qwen Image 3.0 image generation (synchronous). Text-to-image and image-to-image (reference-image editing), any size from 512×512 to 2560×2560, up to 6 images per request. 1K and 2K cost the same.

<a id="qwen-image-3.0-pro"></a>

### Qwen Image 3.0 Pro

调用 ID `qwen-image-3.0-pro` · 图像生成 · 上架 2026-09-04

阿里通义千问 Qwen Image 3.0 Pro 图像生成(同步),复杂版式与文字渲染更强。文生图 / 图生图,单次最多 6 张。按输出总像素分 1K / 2K 两档计价。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 15 积分 ≈ ¥0.25 ≈ $0.03709 |

- 尺寸：尺寸档 1K / 2K / 4K，尺寸下限约 1920×1920
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 9 张、图生图最多 50 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/qwen-image-3.0-pro](https://model.dflop.top/models/qwen-image-3.0-pro) · [English](https://model.dflop.top/en/models/qwen-image-3.0-pro) · [Markdown](https://model.dflop.top/models/qwen-image-3.0-pro.md)

> Alibaba Qwen Image 3.0 Pro image generation (synchronous), stronger at complex layouts and text rendering. Text-to-image and image-to-image, up to 6 images per request, priced in two tiers (1K / 2K) by total output pixels.

<a id="wan3.0-video"></a>

### 万相 3.0 视频生成

调用 ID `wan3.0-video` · 视频生成 · 上架 2026-09-04

通义万相 3.0 视频生成(异步任务),2-30 秒,480P/720P/1080P,30fps,支持 16:9/9:16/1:1/4:3/3:4/adaptive。单卡双态:带首帧参考图时自动转为图生视频(同价)。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 64.8 积分 ≈ ¥1.08 ≈ $0.1602 | 72 积分 ≈ ¥1.2 ≈ $0.178 |

现在是限时 9 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：480p / 720p（默认） / 1080p
- 时长：2–30 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 10 张、视频 5 段、音频 5 段
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/wan3.0-video](https://model.dflop.top/models/wan3.0-video) · [English](https://model.dflop.top/en/models/wan3.0-video) · [Markdown](https://model.dflop.top/models/wan3.0-video.md)

> Alibaba Wan 3.0 video generation (asynchronous task): 2-30 seconds, 480P / 720P / 1080P, 30 fps, 16:9 / 9:16 / 1:1 / 4:3 / 3:4 / adaptive. One card, two modes: with a first-frame reference image it becomes image-to-video automatically (same price).

<a id="wan3.0-video-prime"></a>

### 万相 3.0 视频生成 Prime

调用 ID `wan3.0-video-prime` · 视频生成 · 上架 2026-09-04

通义万相 3.0 视频生成 Prime 加速版(异步任务),与标准版同能力但出片显著更快。2-30 秒,480P/720P/1080P,30fps,支持 16:9/9:16/1:1/4:3/3:4/adaptive。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 97.2 积分 ≈ ¥1.62 ≈ $0.2404 | 108 积分 ≈ ¥1.8 ≈ $0.2671 |

现在是限时 9 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：480p / 720p（默认） / 1080p
- 时长：2–30 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 10 张、视频 5 段、音频 5 段
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/wan3.0-video-prime](https://model.dflop.top/models/wan3.0-video-prime) · [English](https://model.dflop.top/en/models/wan3.0-video-prime) · [Markdown](https://model.dflop.top/models/wan3.0-video-prime.md)

> Alibaba Wan 3.0 video generation, Prime accelerated version (asynchronous task): the same capabilities as the standard version with noticeably faster output. 2-30 seconds, 480P / 720P / 1080P, 30 fps, 16:9 / 9:16 / 1:1 / 4:3 / 3:4 / adaptive.

<a id="happyhorse-1.1-r2v"></a>

### 快乐马 1.1 全能参考

调用 ID `happyhorse-1.1-r2v` · 视频生成 · 上架 2026-08-25

通义万相系 快乐马 1.1 多图参考生视频(异步任务),1~9 张参考图,提示词以 character1/2/3 指代,3-15 秒,720P/1080P。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 72 积分 ≈ ¥1.2 ≈ $0.178 |

- 生成方式：图生视频、参考图/视频生视频
- 需要传参考图（首帧或参考图）
- 分辨率：720p（默认） / 1080p
- 时长：3–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9
- 参考素材：图片最多 9 张
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/happyhorse-1.1-r2v](https://model.dflop.top/models/happyhorse-1.1-r2v) · [English](https://model.dflop.top/en/models/happyhorse-1.1-r2v) · [Markdown](https://model.dflop.top/models/happyhorse-1.1-r2v.md)

> Happy Horse 1.1 (Wan family) multi-reference image-to-video (asynchronous task): 1-9 reference images, referred to as character1/2/3 in the prompt, 3-15 seconds, 720P / 1080P.

<a id="happyhorse-1.1-i2v"></a>

### 快乐马 1.1 图生视频

调用 ID `happyhorse-1.1-i2v` · 视频生成 · 上架 2026-08-25

通义万相系 快乐马 1.1 首帧图生视频(异步任务),3-15 秒,720P/1080P。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 72 积分 ≈ ¥1.2 ≈ $0.178 |

- 生成方式：图生视频
- 需要传参考图（首帧或参考图）
- 分辨率：720p（默认） / 1080p
- 时长：3–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/happyhorse-1.1-i2v](https://model.dflop.top/models/happyhorse-1.1-i2v) · [English](https://model.dflop.top/en/models/happyhorse-1.1-i2v) · [Markdown](https://model.dflop.top/models/happyhorse-1.1-i2v.md)

> Happy Horse 1.1 (Wan family) first-frame image-to-video (asynchronous task): 3-15 seconds, 720P / 1080P.

<a id="happyhorse-1.1-t2v"></a>

### 快乐马 1.1 文生视频

调用 ID `happyhorse-1.1-t2v` · 视频生成 · 上架 2026-08-25

通义万相系 快乐马 1.1 文生视频(异步任务),3-15 秒,720P/1080P,支持 16:9/9:16/1:1/4:3/3:4/4:5/5:4/21:9/9:21。带首帧图时自动升级为图生视频(同价)。相比 1.0 动态更连贯、主体更稳、质感更真。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 72 积分 ≈ ¥1.2 ≈ $0.178 |

- 生成方式：文生视频、图生视频
- 分辨率：720p（默认） / 1080p
- 时长：3–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/happyhorse-1.1-t2v](https://model.dflop.top/models/happyhorse-1.1-t2v) · [English](https://model.dflop.top/en/models/happyhorse-1.1-t2v) · [Markdown](https://model.dflop.top/models/happyhorse-1.1-t2v.md)

> Happy Horse 1.1 (Wan family) text-to-video (asynchronous task): 3-15 seconds, 720P / 1080P, 16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 4:5 / 5:4 / 21:9 / 9:21. With a first-frame image it becomes image-to-video automatically (same price). Smoother motion, steadier subjects and more realistic texture than 1.0.

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

对话（Qwen3.8-Omni-Flash）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="qwen3.8-omni-flash",
    messages=[{"role": "user", "content": "用三句话介绍一下你自己"}],
)
print(resp.choices[0].message.content)
```

生图（Qwen Image 3.0）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"], timeout=300)

result = client.images.generate(
    model="qwen-image-3.0",
    prompt="一只在竹林里喝茶的熊猫，水彩风格",
    size="2048x2048",
)
print(result.data[0].url)  # 临时链接（约 24 小时），请转存
```

视频（万相 3.0 视频生成）：

```python
import os, time, uuid
import requests

BASE = "https://api.dflop.top/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"}

r = requests.post(
    f"{BASE}/videos/generations",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},  # 重试用同一把键，不会重复扣费
    json={
        "model": "wan3.0-video",
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

9 Alibaba (Qwen, Wan) models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (Qwen, Qwen Image, Wan video and HappyHorse video). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: chat models through the OpenAI SDK at `https://api.dflop.top/v1`; image models through the OpenAI Images API (`/v1/images/generations`); video models as asynchronous tasks (`/v1/videos/generations`).

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
