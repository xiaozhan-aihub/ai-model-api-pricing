# 字节跳动 豆包 API 价格与调用：Seedance 视频、Seedream 生图

> ByteDance (Doubao) API pricing on XiaoZhan AIhub: 13 models (Seedance video and Seedream image). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 字节跳动 豆包 模型共 13 个（图像生成 4 个，视频生成 9 个），一把 `sk-gpushare-` 密钥全都能调：生图走 OpenAI Images 接口，视频是提交任务再轮询结果。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [AI 生图 API 价格对比](../pricing/image-generation-api.md) · [AI 视频生成 API 价格对比](../pricing/video-generation-api.md) · [官网厂商页](https://model.dflop.top/vendors/bytedance)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [Seedream 4.0](#doubao-seedream-4-0-250828) | `doubao-seedream-4-0-250828` | 图像生成 | ¥0.18 / 张 | — | — |
| [Seedream 4.5](#doubao-seedream-4-5-251128) | `doubao-seedream-4-5-251128` | 图像生成 | ¥0.225 / 张 | — | — |
| [Seedream 5.0](#doubao-seedream-5-0-260128) | `doubao-seedream-5-0-260128` | 图像生成 | ¥0.198 / 张 | — | — |
| [Seedream 5.0 Pro](#doubao-seedream-5-0-pro-260628) | `doubao-seedream-5-0-pro-260628` | 图像生成 | ¥0.27 / 张 | — | — |
| [Seedance 2.0](#doubao-seedance-2.0) | `doubao-seedance-2.0` | 视频生成 | ¥2.231 / 秒 | — | 9 折 |
| [Seedance 2.0 Fast](#doubao-seedance-2.0-fast) | `doubao-seedance-2.0-fast` | 视频生成 | ¥0.7193 / 秒 | — | 9 折 |
| [Seedance 2.0 Fast Lite](#doubao-seedance-2.0-fast-lite) | `doubao-seedance-2.0-fast-lite` | 视频生成 | ¥0.6394 / 秒 | — | 8 折 |
| [Seedance 2.0 Lite](#doubao-seedance-2.0-lite) | `doubao-seedance-2.0-lite` | 视频生成 | ¥0.7949 / 秒 | — | 8 折 |
| [Seedance 2.0 Mini](#doubao-seedance-2.0-mini) | `doubao-seedance-2.0-mini` | 视频生成 | ¥0.4471 / 秒 | — | 9 折 |
| [Seedance 2.0 Mini Lite](#doubao-seedance-2.0-mini-lite) | `doubao-seedance-2.0-mini-lite` | 视频生成 | ¥0.3974 / 秒 | — | 8 折 |
| [Seedance 2.0 YD](#seedance2.0-yd) | `seedance2.0-yd` | 视频生成 | ¥1.983 / 秒 | — | 8 折 |
| [Seedance 2.5](#doubao-seedance-2.5) | `doubao-seedance-2.5` | 视频生成 | ¥3.368 / 秒 | — | 9 折 |
| [Seedance 2.5 Lite](#doubao-seedance-2.5-lite) | `doubao-seedance-2.5-lite` | 视频生成 | ¥1.21 / 秒 | — | 8 折 |

## 各模型详情

<a id="doubao-seedream-4-0-250828"></a>

### Seedream 4.0

调用 ID `doubao-seedream-4-0-250828` · 图像生成 · 上架 2025-08-28

字节跳动 Seedream 4.0,图片生成模型(经典档)。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 10.8 积分 ≈ ¥0.18 ≈ $0.02671 |

- 尺寸：尺寸档 1K / 2K / 4K，默认 `1024x1024`，尺寸下限约 960×960
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 15 张、图生图最多 14 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/doubao-seedream-4-0-250828](https://model.dflop.top/models/doubao-seedream-4-0-250828) · [English](https://model.dflop.top/en/models/doubao-seedream-4-0-250828) · [Markdown](https://model.dflop.top/models/doubao-seedream-4-0-250828.md)

> ByteDance Seedream 4.0 image generation (classic tier).

<a id="doubao-seedream-4-5-251128"></a>

### Seedream 4.5

调用 ID `doubao-seedream-4-5-251128` · 图像生成 · 上架 2025-11-28

字节跳动 Seedream 4.5,图片生成模型。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 13.5 积分 ≈ ¥0.225 ≈ $0.03338 |

- 尺寸：尺寸档 2K / 4K，默认 `2048x2048`，尺寸下限约 1920×1920
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 15 张、图生图最多 14 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/doubao-seedream-4-5-251128](https://model.dflop.top/models/doubao-seedream-4-5-251128) · [English](https://model.dflop.top/en/models/doubao-seedream-4-5-251128) · [Markdown](https://model.dflop.top/models/doubao-seedream-4-5-251128.md)

> ByteDance Seedream 4.5 image generation.

<a id="doubao-seedream-5-0-260128"></a>

### Seedream 5.0

调用 ID `doubao-seedream-5-0-260128` · 图像生成 · 上架 2026-01-28

字节跳动 Seedream 5.0,图片生成旗舰。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 11.88 积分 ≈ ¥0.198 ≈ $0.02938 |

- 尺寸：尺寸档 2K / 4K，默认 `2048x2048`，尺寸下限约 1920×1920
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 单次最多 15 张、图生图最多 14 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/doubao-seedream-5-0-260128](https://model.dflop.top/models/doubao-seedream-5-0-260128) · [English](https://model.dflop.top/en/models/doubao-seedream-5-0-260128) · [Markdown](https://model.dflop.top/models/doubao-seedream-5-0-260128.md)

> ByteDance Seedream 5.0, the image generation flagship.

<a id="doubao-seedream-5-0-pro-260628"></a>

### Seedream 5.0 Pro

调用 ID `doubao-seedream-5-0-pro-260628` · 图像生成 · 上架 2026-06-28

字节跳动 Seedream 5.0 Pro,图片生成旗舰增强档;参考图输入按张另计。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 16.2 积分 ≈ ¥0.27 ≈ $0.04006 |

- 尺寸：尺寸档 1K / 2K，默认 `1536x1536`，尺寸下限约 960×960
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 21:9 / 自动
- 图生图最多 10 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/doubao-seedream-5-0-pro-260628](https://model.dflop.top/models/doubao-seedream-5-0-pro-260628) · [English](https://model.dflop.top/en/models/doubao-seedream-5-0-pro-260628) · [Markdown](https://model.dflop.top/models/doubao-seedream-5-0-pro-260628.md)

> ByteDance Seedream 5.0 Pro, the enhanced image generation flagship; reference images are billed per image.

<a id="doubao-seedance-2.0"></a>

### Seedance 2.0

调用 ID `doubao-seedance-2.0` · 视频生成 · 上架 2026-01-28

字节跳动 Seedance 2.0,视频生成旗舰(异步任务)。支持文生视频、图生视频与多模态参考;480p/720p/1080p/4K,4-15 秒,24fps。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 133.84 积分 ≈ ¥2.231 ≈ $0.331 | 148.72 积分 ≈ ¥2.479 ≈ $0.3677 |

现在是限时 9 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：480p / 720p（默认） / 1080p / 4k
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 9 张、视频 3 段、音频 3 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/doubao-seedance-2.0](https://model.dflop.top/models/doubao-seedance-2.0) · [English](https://model.dflop.top/en/models/doubao-seedance-2.0) · [Markdown](https://model.dflop.top/models/doubao-seedance-2.0.md)

> ByteDance Seedance 2.0, the video generation flagship (asynchronous task). Text-to-video, image-to-video and multimodal reference; 480p / 720p / 1080p / 4K, 4-15 seconds, 24 fps.

<a id="doubao-seedance-2.0-fast"></a>

### Seedance 2.0 Fast

调用 ID `doubao-seedance-2.0-fast` · 视频生成 · 上架 2026-01-28

字节跳动 Seedance 2.0 Fast,低延迟视频生成快速档(异步任务)。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 43.16 积分 ≈ ¥0.7193 ≈ $0.1067 | 47.95 积分 ≈ ¥0.7992 ≈ $0.1186 |

现在是限时 9 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：480p / 720p（默认）
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 9 张、视频 3 段、音频 3 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/doubao-seedance-2.0-fast](https://model.dflop.top/models/doubao-seedance-2.0-fast) · [English](https://model.dflop.top/en/models/doubao-seedance-2.0-fast) · [Markdown](https://model.dflop.top/models/doubao-seedance-2.0-fast.md)

> ByteDance Seedance 2.0 Fast, the low-latency video generation tier (asynchronous task).

<a id="doubao-seedance-2.0-fast-lite"></a>

### Seedance 2.0 Fast Lite

调用 ID `doubao-seedance-2.0-fast-lite` · 视频生成 · 上架 2026-08-12

字节跳动 Seedance 2.0 极速轻量档,低延迟 + 高性价比(异步任务)。支持文生视频、图生视频与多模态参考;720p,4-15 秒,24fps。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 38.36 积分 ≈ ¥0.6394 ≈ $0.09486 | 47.95 积分 ≈ ¥0.7992 ≈ $0.1186 |

现在是限时 8 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认）
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 9 张、视频 3 段、音频 3 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/doubao-seedance-2.0-fast-lite](https://model.dflop.top/models/doubao-seedance-2.0-fast-lite) · [English](https://model.dflop.top/en/models/doubao-seedance-2.0-fast-lite) · [Markdown](https://model.dflop.top/models/doubao-seedance-2.0-fast-lite.md)

> ByteDance Seedance 2.0 fast lite tier: low latency and high value (asynchronous task). Text-to-video, image-to-video and multimodal reference; 720p, 4-15 seconds, 24 fps.

<a id="doubao-seedance-2.0-lite"></a>

### Seedance 2.0 Lite

调用 ID `doubao-seedance-2.0-lite` · 视频生成 · 上架 2026-08-12

字节跳动 Seedance 2.0 轻量档,高性价比出片(异步任务)。支持文生视频、图生视频与多模态参考;720p/1080p,4-15 秒,24fps。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 47.69 积分 ≈ ¥0.7949 ≈ $0.1179 | 59.62 积分 ≈ ¥0.9936 ≈ $0.1474 |

现在是限时 8 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 9 张、视频 3 段、音频 3 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/doubao-seedance-2.0-lite](https://model.dflop.top/models/doubao-seedance-2.0-lite) · [English](https://model.dflop.top/en/models/doubao-seedance-2.0-lite) · [Markdown](https://model.dflop.top/models/doubao-seedance-2.0-lite.md)

> ByteDance Seedance 2.0 lite tier, high-value output (asynchronous task). Text-to-video, image-to-video and multimodal reference; 720p / 1080p, 4-15 seconds, 24 fps.

<a id="doubao-seedance-2.0-mini"></a>

### Seedance 2.0 Mini

调用 ID `doubao-seedance-2.0-mini` · 视频生成 · 上架 2026-06-16

字节跳动 Seedance 2.0 Mini,轻量高性价比视频生成档(异步任务)。支持文生视频、图生视频与多模态参考;480p/720p,4-15 秒,24fps。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 26.83 积分 ≈ ¥0.4471 ≈ $0.06634 | 29.81 积分 ≈ ¥0.4968 ≈ $0.07371 |

现在是限时 9 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：480p / 720p（默认）
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 9 张、视频 3 段、音频 3 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/doubao-seedance-2.0-mini](https://model.dflop.top/models/doubao-seedance-2.0-mini) · [English](https://model.dflop.top/en/models/doubao-seedance-2.0-mini) · [Markdown](https://model.dflop.top/models/doubao-seedance-2.0-mini.md)

> ByteDance Seedance 2.0 Mini, a light, high-value video generation tier (asynchronous task). Text-to-video, image-to-video and multimodal reference; 480p / 720p, 4-15 seconds, 24 fps.

<a id="doubao-seedance-2.0-mini-lite"></a>

### Seedance 2.0 Mini Lite

调用 ID `doubao-seedance-2.0-mini-lite` · 视频生成 · 上架 2026-08-12

字节跳动 Seedance 2.0 Mini 轻量档,轻量场景最低成本出片(异步任务)。支持文生视频、图生视频与多模态参考;720p,4-15 秒,24fps。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 23.85 积分 ≈ ¥0.3974 ≈ $0.05897 | 29.81 积分 ≈ ¥0.4968 ≈ $0.07371 |

现在是限时 8 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认）
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 9 张、视频 3 段、音频 3 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/doubao-seedance-2.0-mini-lite](https://model.dflop.top/models/doubao-seedance-2.0-mini-lite) · [English](https://model.dflop.top/en/models/doubao-seedance-2.0-mini-lite) · [Markdown](https://model.dflop.top/models/doubao-seedance-2.0-mini-lite.md)

> ByteDance Seedance 2.0 Mini lite tier, the lowest cost for light scenarios (asynchronous task). Text-to-video, image-to-video and multimodal reference; 720p, 4-15 seconds, 24 fps.

<a id="seedance2.0-yd"></a>

### Seedance 2.0 YD

调用 ID `seedance2.0-yd` · 视频生成 · 上架 2026-10-10

字节跳动 Seedance 2.0 独立通道(异步任务)。支持文生视频与多模态参考(参考图 ≤9 张,可加参考音频 ≤3 段,role 分别为 reference_image / reference_audio);不支持首帧 / 首尾帧与参考视频。须写文字提示词,并指定 resolution(480p / 720p / 1080p)、具体 ratio(16:9 / 4:3 / 1:1 / 3:4 / 9:16 / 21:9,不支持 adaptive)与整数 duration(4-15 秒),24fps。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 118.97 积分 ≈ ¥1.983 ≈ $0.2942 | 148.72 积分 ≈ ¥2.479 ≈ $0.3677 |

现在是限时 8 折。

- 生成方式：文生视频、参考图/视频生视频
- 分辨率：480p / 720p（默认） / 1080p
- 时长：4–15 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9
- 参考素材：图片最多 9 张、音频 3 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/seedance2.0-yd](https://model.dflop.top/models/seedance2.0-yd) · [English](https://model.dflop.top/en/models/seedance2.0-yd) · [Markdown](https://model.dflop.top/models/seedance2.0-yd.md)

> ByteDance Seedance 2.0 on a separate channel (asynchronous task). Text-to-video and multimodal reference (up to 9 reference images and up to 3 reference audio clips, with roles reference_image / reference_audio); no first frame, first-and-last frame or reference video. A text prompt is required, along with resolution (480p / 720p / 1080p), a specific ratio (16:9 / 4:3 / 1:1 / 3:4 / 9:16 / 21:9; adaptive is not supported) and an integer duration (4-15 seconds), 24 fps.

<a id="doubao-seedance-2.5"></a>

### Seedance 2.5

调用 ID `doubao-seedance-2.5` · 视频生成 · 上架 2026-06-28

字节跳动 Seedance 2.5,视频生成新旗舰(异步任务)。支持文生视频、图生视频首帧/首尾帧,以及图片(≤30 张)/视频/音频的多模态参考与组合参考;可生成有声视频。480p/720p/1080p,4-30 秒,24fps,画幅 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 202.08 积分 ≈ ¥3.368 ≈ $0.4997 | 224.53 积分 ≈ ¥3.742 ≈ $0.5552 |

现在是限时 9 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：480p / 720p（默认） / 1080p
- 时长：4–30 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 30 张、视频 10 段、音频 10 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/doubao-seedance-2.5](https://model.dflop.top/models/doubao-seedance-2.5) · [English](https://model.dflop.top/en/models/doubao-seedance-2.5) · [Markdown](https://model.dflop.top/models/doubao-seedance-2.5.md)

> ByteDance Seedance 2.5, the new video generation flagship (asynchronous task). Text-to-video, image-to-video with a first frame or first and last frames, and multimodal or combined reference with images (up to 30), video and audio; can generate video with sound. 480p / 720p / 1080p, 4-30 seconds, 24 fps, aspect ratios 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16.

<a id="doubao-seedance-2.5-lite"></a>

### Seedance 2.5 Lite

调用 ID `doubao-seedance-2.5-lite` · 视频生成 · 上架 2026-08-12

字节跳动 Seedance 2.5 轻量档,高性价比出片(异步任务)。支持文生视频、图生视频首帧/首尾帧,以及图片(≤30 张)/视频/音频的多模态参考与组合参考;可生成有声视频。720p/1080p,4-30 秒,24fps,画幅 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16。

| 计价项 | 现价（实际扣费） | 原价 |
|---|---|---|
| 视频 · 每秒 | 72.58 积分 ≈ ¥1.21 ≈ $0.1795 | 90.72 积分 ≈ ¥1.512 ≈ $0.2243 |

现在是限时 8 折。

- 生成方式：文生视频、图生视频、首尾帧、参考图/视频生视频
- 分辨率：720p（默认） / 1080p
- 时长：4–30 秒
- 画幅：16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 / 自适应
- 参考素材：图片最多 30 张、视频 10 段、音频 10 段
- 可生成带声音的视频（可开关）
- 接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）
- 模型页：[model.dflop.top/models/doubao-seedance-2.5-lite](https://model.dflop.top/models/doubao-seedance-2.5-lite) · [English](https://model.dflop.top/en/models/doubao-seedance-2.5-lite) · [Markdown](https://model.dflop.top/models/doubao-seedance-2.5-lite.md)

> ByteDance Seedance 2.5 lite tier, high-value output (asynchronous task). Text-to-video, image-to-video with a first frame or first and last frames, and multimodal or combined reference with images (up to 30), video and audio; can generate video with sound. 720p / 1080p, 4-30 seconds, 24 fps, aspect ratios 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16.

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

生图（Seedream 5.0）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"], timeout=300)

result = client.images.generate(
    model="doubao-seedream-5-0-260128",
    prompt="一只在竹林里喝茶的熊猫，水彩风格",
    size="2048x2048",
)
print(result.data[0].url)  # 临时链接（约 24 小时），请转存
```

视频（Seedance 2.0）：

```python
import os, time, uuid
import requests

BASE = "https://api.dflop.top/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"}

r = requests.post(
    f"{BASE}/videos/generations",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},  # 重试用同一把键，不会重复扣费
    json={
        "model": "doubao-seedance-2.0",
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

13 ByteDance (Doubao) models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (Seedance video and Seedream image). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: image models through the OpenAI Images API (`/v1/images/generations`); video models as asynchronous tasks (`/v1/videos/generations`).

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
