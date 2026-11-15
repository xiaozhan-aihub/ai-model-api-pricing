# AI 视频生成 API 价格对比：Seedance、Veo、可灵 Kling、Vidu、海螺 Hailuo、通义万相 Wan、Grok Imagine（40 个模型）

> Video generation API pricing comparison: 40 models (Seedance, Veo, Kling, Vidu, Hailuo, Wan, Grok Imagine) through one API. Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上全部 40 个视频生成模型的 API 价格和参数，按每秒价格从低到高排列。文生视频、图生视频、首尾帧和参考生视频都走同一个异步接口 `POST /v1/videos/generations`：提交任务，再轮询结果。

价格是平台模型目录上的每秒标价（含限时折扣）。多数视频模型按分辨率分档，Seedance 系列按 token 计费，实际扣费以模型页和[计费说明](https://model.dflop.top/docs/reference/media-apis)为准。平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部类别](../README.md) · [`models.json`](../data/models.json)

## 价格表（每秒从低到高）

| # | 模型 | 调用 ID | 厂商 | ¥ | $ | 生成方式 | 分辨率 | 时长 | 声音 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [Grok Imagine Video](../vendors/xai-grok.md#grok-imagine-video) | `grok-imagine-video` | xAI Grok | ¥0.1 / 秒 | $0.01484 / 秒 | 文生视频、图生视频、参考图/视频生视频 | 720p / 1080p | 1–15 秒 | — |
| 2 | [Grok Imagine Video 1.5](../vendors/xai-grok.md#grok-imagine-video-1.5-preview) | `grok-imagine-video-1.5-preview` | xAI Grok | ¥0.1 / 秒 | $0.01484 / 秒 | 文生视频、图生视频、参考图/视频生视频 | 720p / 1080p | 1–15 秒 | — |
| 3 | [可灵 O1](../vendors/kuaishou-kling.md#tvod-kling-video-o1) | `tvod-kling-video-o1` | 快手 可灵 | ¥0.337 / 秒 | $0.05 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p | 3–15 秒 | — |
| 4 | [Vidu Q3](../vendors/shengshu-vidu.md#tvod-vidu-video-q3) | `tvod-vidu-video-q3` | 生数科技 Vidu | ¥0.3774 / 秒 | $0.056 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p / 4k | 1–10 秒 | — |
| 5 | [Vidu Q3 Mix](../vendors/shengshu-vidu.md#tvod-vidu-video-q3-mix) | `tvod-vidu-video-q3-mix` | 生数科技 Vidu | ¥0.3774 / 秒 | $0.056 / 秒 | — | — | — | — |
| 6 | [Vidu Q3 Pro](../vendors/shengshu-vidu.md#tvod-vidu-video-q3-pro) | `tvod-vidu-video-q3-pro` | 生数科技 Vidu | ¥0.3774 / 秒 | $0.056 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p / 4k | 1–10 秒 | — |
| 7 | [Vidu Q3 Turbo](../vendors/shengshu-vidu.md#tvod-vidu-video-q3-turbo) | `tvod-vidu-video-q3-turbo` | 生数科技 Vidu | ¥0.3774 / 秒 | $0.056 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p | 1–10 秒 | — |
| 8 | [Vidu Q3 广告版](../vendors/shengshu-vidu.md#tvod-vidu-video-q3-ad) | `tvod-vidu-video-q3-ad` | 生数科技 Vidu | ¥0.3774 / 秒 | $0.056 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p / 4k | 1–10 秒 | — |
| 9 | [Vidu Q3 短剧版](../vendors/shengshu-vidu.md#tvod-vidu-video-q3-drama) | `tvod-vidu-video-q3-drama` | 生数科技 Vidu | ¥0.3774 / 秒 | $0.056 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p / 4k | 1–10 秒 | — |
| 10 | [Seedance 2.0 Mini Lite](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-mini-lite) | `doubao-seedance-2.0-mini-lite` | 字节跳动 豆包 | ¥0.3974 / 秒 | $0.05897 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p | 4–15 秒 | 可选 |
| 11 | [海螺 H3 提速版 tx](../vendors/minimax-hailuo.md#minimax-h3-fast-tx) | `minimax-h3-fast-tx` | MiniMax 海螺 | ¥0.4 / 秒 | $0.05935 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 480p / 720p / 768p | 4–15 秒 | 可选 |
| 12 | [海螺 H3 提速版带IR tx](../vendors/minimax-hailuo.md#minimax-h3-fast-ir-tx) | `minimax-h3-fast-ir-tx` | MiniMax 海螺 | ¥0.4 / 秒 | $0.05935 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 480p / 720p / 768p | 4–15 秒 | 可选 |
| 13 | [Seedance 2.0 Mini](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-mini) | `doubao-seedance-2.0-mini` | 字节跳动 豆包 | ¥0.4471 / 秒 | $0.06634 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 480p / 720p | 4–15 秒 | 可选 |
| 14 | [海螺 H3 Max](../vendors/minimax-hailuo.md#minimax-h3-max) | `minimax-h3-max` | MiniMax 海螺 | ¥0.5 / 秒 | $0.07418 / 秒 | 文生视频、图生视频、首尾帧 | 480p / 768p | 5–15 秒 | — |
| 15 | [海螺 H3 tx](../vendors/minimax-hailuo.md#minimax-h3-tx) | `minimax-h3-tx` | MiniMax 海螺 | ¥0.5 / 秒 | $0.07418 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 768p | 4–15 秒 | 可选 |
| 16 | [海螺 H3 满血版 tx](../vendors/minimax-hailuo.md#minimax-h3-medium-tx) | `minimax-h3-medium-tx` | MiniMax 海螺 | ¥0.5 / 秒 | $0.07418 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 768p | 4–15 秒 | 可选 |
| 17 | [海螺 H3 满血版带IR tx](../vendors/minimax-hailuo.md#minimax-h3-medium-ir-tx) | `minimax-h3-medium-ir-tx` | MiniMax 海螺 | ¥0.5 / 秒 | $0.07418 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 768p | 4–15 秒 | 可选 |
| 18 | [Veo 3.1 Lite](../vendors/google-gemini-veo-nano-banana.md#tvod-veo-3.1-lite) | `tvod-veo-3.1-lite` | Google | ¥0.5392 / 秒 | $0.08 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p | 8 秒 | — |
| 19 | [可灵 3.0](../vendors/kuaishou-kling.md#tvod-kling-video-3.0) | `tvod-kling-video-3.0` | 快手 可灵 | ¥0.5392 / 秒 | $0.08 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p / 4k | 3–15 秒 | — |
| 20 | [可灵 3.0 Omni](../vendors/kuaishou-kling.md#tvod-kling-video-3.0-omni) | `tvod-kling-video-3.0-omni` | 快手 可灵 | ¥0.5392 / 秒 | $0.08 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p / 4k | 3–15 秒 | — |
| 21 | [Seedance 2.0 Fast Lite](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-fast-lite) | `doubao-seedance-2.0-fast-lite` | 字节跳动 豆包 | ¥0.6394 / 秒 | $0.09486 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p | 4–15 秒 | 可选 |
| 22 | [Veo 3.1](../vendors/google-gemini-veo-nano-banana.md#tvod-veo-3.1) | `tvod-veo-3.1` | Google | ¥0.674 / 秒 | $0.1 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p / 4k | 8 秒 | — |
| 23 | [Seedance 2.0 Fast](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-fast) | `doubao-seedance-2.0-fast` | 字节跳动 豆包 | ¥0.7193 / 秒 | $0.1067 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 480p / 720p | 4–15 秒 | 可选 |
| 24 | [Seedance 2.0 Lite](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-lite) | `doubao-seedance-2.0-lite` | 字节跳动 豆包 | ¥0.7949 / 秒 | $0.1179 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p | 4–15 秒 | 可选 |
| 25 | [海螺 H3](../vendors/minimax-hailuo.md#minimax-h3) | `minimax-h3` | MiniMax 海螺 | ¥0.8 / 秒 | $0.1187 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 768p / 2k | 4–15 秒 | — |
| 26 | [Veo 3.1 Fast](../vendors/google-gemini-veo-nano-banana.md#tvod-veo-3.1-fast) | `tvod-veo-3.1-fast` | Google | ¥0.8088 / 秒 | $0.12 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p | 8 秒 | — |
| 27 | [万相 3.0 视频生成](../vendors/alibaba-qwen-wan.md#wan3.0-video) | `wan3.0-video` | 阿里巴巴 通义 | ¥1.08 / 秒 | $0.1602 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 480p / 720p / 1080p | 2–30 秒 | — |
| 28 | [可灵 4.0](../vendors/kuaishou-kling.md#tvod-kling-video-4.0) | `tvod-kling-video-4.0` | 快手 可灵 | ¥1.14 / 秒 | $0.1691 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p / 2k / 4k | 3–30 秒 | — |
| 29 | [可灵 4.0 Omni](../vendors/kuaishou-kling.md#tvod-kling-video-4.0-omni) | `tvod-kling-video-4.0-omni` | 快手 可灵 | ¥1.14 / 秒 | $0.1691 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p / 2k / 4k | 3–30 秒 | — |
| 30 | [快乐马 1.1 全能参考](../vendors/alibaba-qwen-wan.md#happyhorse-1.1-r2v) | `happyhorse-1.1-r2v` | 阿里巴巴 通义 | ¥1.2 / 秒 | $0.178 / 秒 | 图生视频、参考图/视频生视频 | 720p / 1080p | 3–15 秒 | — |
| 31 | [快乐马 1.1 图生视频](../vendors/alibaba-qwen-wan.md#happyhorse-1.1-i2v) | `happyhorse-1.1-i2v` | 阿里巴巴 通义 | ¥1.2 / 秒 | $0.178 / 秒 | 图生视频 | 720p / 1080p | 3–15 秒 | — |
| 32 | [快乐马 1.1 文生视频](../vendors/alibaba-qwen-wan.md#happyhorse-1.1-t2v) | `happyhorse-1.1-t2v` | 阿里巴巴 通义 | ¥1.2 / 秒 | $0.178 / 秒 | 文生视频、图生视频 | 720p / 1080p | 3–15 秒 | — |
| 33 | [Seedance 2.5 Lite](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.5-lite) | `doubao-seedance-2.5-lite` | 字节跳动 豆包 | ¥1.21 / 秒 | $0.1795 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 720p / 1080p | 4–30 秒 | 可选 |
| 34 | [万相 3.0 视频生成 Prime](../vendors/alibaba-qwen-wan.md#wan3.0-video-prime) | `wan3.0-video-prime` | 阿里巴巴 通义 | ¥1.62 / 秒 | $0.2404 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 480p / 720p / 1080p | 2–30 秒 | — |
| 35 | [Seedance 2.0 YD](../vendors/bytedance-seedance-seedream.md#seedance2.0-yd) | `seedance2.0-yd` | 字节跳动 豆包 | ¥1.983 / 秒 | $0.2942 / 秒 | 文生视频、参考图/视频生视频 | 480p / 720p / 1080p | 4–15 秒 | 可选 |
| 36 | [Seedance 2.0](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0) | `doubao-seedance-2.0` | 字节跳动 豆包 | ¥2.231 / 秒 | $0.331 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 480p / 720p / 1080p / 4k | 4–15 秒 | 可选 |
| 37 | [Seedance 2.5](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.5) | `doubao-seedance-2.5` | 字节跳动 豆包 | ¥3.368 / 秒 | $0.4997 / 秒 | 文生视频、图生视频、首尾帧、参考图/视频生视频 | 480p / 720p / 1080p | 4–30 秒 | 可选 |
| 38 | [创建数字人形象](../vendors/xiaozhan-platform.md#dh-avatar-create) | `dh-avatar-create` | 小战AIhub 自有能力 | 见模型页 | — | — | — | — | — |
| 39 | [数字人视频](../vendors/xiaozhan-platform.md#dh-avatar) | `dh-avatar` | 小战AIhub 自有能力 | ¥0.06 / 秒 | $0.008902 / 秒 | 数字人口播 | — | — | 有 |
| 40 | [智能剪辑](../vendors/xiaozhan-platform.md#clip-compose) | `clip-compose` | 小战AIhub 自有能力 | ¥1.5 / 次 | $0.2226 / 次 | 智能剪辑 | — | — | 有 |

数字人和智能剪辑排在最后，它们是成片工具，不是通用视频模型。

## 怎么调用

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

文生视频（提交 + 轮询）：

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

图生视频：在 `content` 里加一张首帧图（公网 URL）：

```json
{
  "model": "doubao-seedance-2.0",
  "content": [
    {
      "type": "text",
      "text": "海边日落，无人机航拍视角"
    },
    {
      "type": "image_url",
      "image_url": {
        "url": "https://example.com/first-frame.jpg"
      }
    }
  ],
  "duration": 5,
  "resolution": "720p"
}
```

参数（分辨率、时长、画幅）按模型不同，见上表和各模型的厂商页；不支持的取值会直接返回 400，不扣费。带 `Idempotency-Key` 重试不会重复扣费；不想轮询可以传 `callback_url`。

## 常见问题

**哪个视频生成 API 最便宜？** 按每秒标价，这份目录里最便宜的三个：[Grok Imagine Video](../vendors/xai-grok.md#grok-imagine-video)，¥0.1 / 秒；[Grok Imagine Video 1.5](../vendors/xai-grok.md#grok-imagine-video-1.5-preview)，¥0.1 / 秒；[可灵 O1](../vendors/kuaishou-kling.md#tvod-kling-video-o1)，¥0.337 / 秒。

**单条视频最长多少秒？** 30 秒：[Seedance 2.5](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.5)、[Seedance 2.5 Lite](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.5-lite)、[万相 3.0 视频生成](../vendors/alibaba-qwen-wan.md#wan3.0-video)、[万相 3.0 视频生成 Prime](../vendors/alibaba-qwen-wan.md#wan3.0-video-prime)、[可灵 4.0](../vendors/kuaishou-kling.md#tvod-kling-video-4.0)、[可灵 4.0 Omni](../vendors/kuaishou-kling.md#tvod-kling-video-4.0-omni)。

**哪些模型能出 4K？** [Seedance 2.0](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0)、[Veo 3.1](../vendors/google-gemini-veo-nano-banana.md#tvod-veo-3.1)、[Vidu Q3](../vendors/shengshu-vidu.md#tvod-vidu-video-q3)、[Vidu Q3 Pro](../vendors/shengshu-vidu.md#tvod-vidu-video-q3-pro)、[Vidu Q3 广告版](../vendors/shengshu-vidu.md#tvod-vidu-video-q3-ad)、[Vidu Q3 短剧版](../vendors/shengshu-vidu.md#tvod-vidu-video-q3-drama)、[可灵 3.0](../vendors/kuaishou-kling.md#tvod-kling-video-3.0)、[可灵 3.0 Omni](../vendors/kuaishou-kling.md#tvod-kling-video-3.0-omni)、[可灵 4.0](../vendors/kuaishou-kling.md#tvod-kling-video-4.0)、[可灵 4.0 Omni](../vendors/kuaishou-kling.md#tvod-kling-video-4.0-omni)。

**能生成带声音的视频吗？** 能，[Seedance 2.0](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0)、[Seedance 2.0 Fast](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-fast)、[Seedance 2.0 Fast Lite](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-fast-lite)、[Seedance 2.0 Lite](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-lite)、[Seedance 2.0 Mini](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-mini)、[Seedance 2.0 Mini Lite](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-mini-lite)、[Seedance 2.0 YD](../vendors/bytedance-seedance-seedream.md#seedance2.0-yd)、[Seedance 2.5](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.5)、[Seedance 2.5 Lite](../vendors/bytedance-seedance-seedream.md#doubao-seedance-2.5-lite)、[海螺 H3 tx](../vendors/minimax-hailuo.md#minimax-h3-tx)、[海螺 H3 提速版 tx](../vendors/minimax-hailuo.md#minimax-h3-fast-tx)、[海螺 H3 提速版带IR tx](../vendors/minimax-hailuo.md#minimax-h3-fast-ir-tx)、[海螺 H3 满血版 tx](../vendors/minimax-hailuo.md#minimax-h3-medium-tx)、[海螺 H3 满血版带IR tx](../vendors/minimax-hailuo.md#minimax-h3-medium-ir-tx) 可以选择生成声音。

**生成要多久？结果能保存多久？** 一般 1–5 分钟；成片的 `video_url` 7 天有效，请下载转存。

## English

Prices and parameters of all 40 video generation models on [XiaoZhan AIhub](https://model.dflop.top/en/models): Seedance, Veo, Kling, Vidu, Hailuo, Wan, Grok Imagine and more. Text-to-video, image-to-video, first-and-last-frame and reference-to-video all use one asynchronous endpoint, `POST https://api.dflop.top/v1/videos/generations`, then poll `GET /v1/videos/generations/{id}`. Prices are the catalogue's per-second list (promotions included); most models are tiered by resolution. Cheapest per second: Grok Imagine Video, Grok Imagine Video 1.5 and 可灵 O1.

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
