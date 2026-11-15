# AI 生图 API 价格对比：GPT-Image、Seedream、Nano Banana、可灵、Qwen Image、Grok Imagine（23 个模型）

> Image generation API pricing comparison: 23 models (GPT-Image, Seedream, Nano Banana, Kling, Qwen Image, Grok Imagine) through one API. Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上全部 23 个图像生成模型的 API 价格，按每张价格从低到高排列。文生图和图生图（参考图改图）都走 OpenAI Images 形状的接口 `POST /v1/images/generations`，按张计费。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部类别](../README.md) · [`models.json`](../data/models.json)

## 价格表（每张从低到高）

| # | 模型 | 调用 ID | 厂商 | ¥ / 张 | $ / 张 | 尺寸档 | 单次最多 | 参考图 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [Qwen Image 3.0](../vendors/alibaba-qwen-wan.md#qwen-image-3.0) | `qwen-image-3.0` | 阿里巴巴 通义 | ¥0.18 | $0.02671 | 1K / 2K / 4K | 9 | 50 | 最小约 1920² |
| 2 | [Seedream 4.0](../vendors/bytedance-seedance-seedream.md#doubao-seedream-4-0-250828) | `doubao-seedream-4-0-250828` | 字节跳动 豆包 | ¥0.18 | $0.02671 | 1K / 2K / 4K | 15 | 14 | — |
| 3 | [Seedream 5.0](../vendors/bytedance-seedance-seedream.md#doubao-seedream-5-0-260128) | `doubao-seedream-5-0-260128` | 字节跳动 豆包 | ¥0.198 | $0.02938 | 2K / 4K | 15 | 14 | 最小约 1920² |
| 4 | [Seedream 4.5](../vendors/bytedance-seedance-seedream.md#doubao-seedream-4-5-251128) | `doubao-seedream-4-5-251128` | 字节跳动 豆包 | ¥0.225 | $0.03338 | 2K / 4K | 15 | 14 | 最小约 1920² |
| 5 | [Qwen Image 3.0 Pro](../vendors/alibaba-qwen-wan.md#qwen-image-3.0-pro) | `qwen-image-3.0-pro` | 阿里巴巴 通义 | ¥0.25 | $0.03709 | 1K / 2K / 4K | 9 | 50 | 最小约 1920² |
| 6 | [Seedream 5.0 Pro](../vendors/bytedance-seedance-seedream.md#doubao-seedream-5-0-pro-260628) | `doubao-seedream-5-0-pro-260628` | 字节跳动 豆包 | ¥0.27 | $0.04006 | 1K / 2K | 1 | 10 | — |
| 7 | [GPT-Image 2](../vendors/openai.md#gpt-image-2) | `gpt-image-2` | OpenAI | ¥0.3 | $0.04451 | 1K / 2K / 4K | 1 | 16 | 比例写进提示词 |
| 8 | [GPT-Image 2.5 Flare](../vendors/openai.md#gpt-image-2.5-flare) | `gpt-image-2.5-flare` | OpenAI | ¥0.3 | $0.04451 | 1K / 2K / 4K | 1 | 16 | 比例写进提示词 |
| 9 | [GPT-Image 2.5 Sunburst](../vendors/openai.md#gpt-image-2.5-sunburst) | `gpt-image-2.5-sunburst` | OpenAI | ¥0.3 | $0.04451 | 1K / 2K / 4K | 1 | 16 | 比例写进提示词 |
| 10 | [Grok Imagine (Image · Quality)](../vendors/xai-grok.md#grok-imagine-image-quality) | `grok-imagine-image-quality` | xAI Grok | ¥0.3 | $0.04451 | 1K / 2K / 4K | 9 | 50 | 最小约 1920² |
| 11 | [Grok Imagine (Image)](../vendors/xai-grok.md#grok-imagine-image) | `grok-imagine-image` | xAI Grok | ¥0.3 | $0.04451 | 1K / 2K / 4K | 9 | 50 | 最小约 1920² |
| 12 | [Nano Banana](../vendors/google-gemini-veo-nano-banana.md#nano-banana) | `nano-banana` | Google | ¥0.3 | $0.04451 | 1K / 2K / 4K | 9 | 3 | 最小约 1920² |
| 13 | [Nano Banana 2](../vendors/google-gemini-veo-nano-banana.md#nano-banana-2) | `nano-banana-2` | Google | ¥0.3 | $0.04451 | 1K / 2K / 4K | 9 | 14 | 最小约 1920² |
| 14 | [Nano Banana 2.1](../vendors/google-gemini-veo-nano-banana.md#nano-banana-2.1) | `nano-banana-2.1` | Google | ¥0.3 | $0.04451 | 1K / 2K / 4K | 9 | 14 | 最小约 1920² |
| 15 | [Nano Banana Pro](../vendors/google-gemini-veo-nano-banana.md#nano-banana-pro) | `nano-banana-pro` | Google | ¥0.3 | $0.04451 | 1K / 2K / 4K | 9 | 14 | 最小约 1920² |
| 16 | [可灵图像 3.0](../vendors/kuaishou-kling.md#tvod-kling-image-3.0) | `tvod-kling-image-3.0` | 快手 可灵 | ¥0.337 | $0.05 | 1K / 2K / 4K | 9 | 50 | 最小约 1920² |
| 17 | [可灵图像 3.0 Omni](../vendors/kuaishou-kling.md#tvod-kling-image-3.0-omni) | `tvod-kling-image-3.0-omni` | 快手 可灵 | ¥0.4044 | $0.06 | 1K / 2K / 4K | 9 | 50 | 最小约 1920² |
| 18 | [xiaozhanimage](../vendors/xiaozhan-platform.md#xiaozhanimage) | `xiaozhanimage` | 小战AIhub 自有能力 | ¥0.5 | $0.07418 | 1K / 2K / 4K | 1 | 9 | — |
| 19 | [GPT-Image 2-bd](../vendors/openai.md#gpt-image-2-bd) | `gpt-image-2-bd` | OpenAI | ¥1.138 | $0.1688 | 1K / 2K / 4K | 1 | 16 | — |
| 20 | [GPT-Image 2.5 Flare-bd](../vendors/openai.md#gpt-image-2.5-flare-bd) | `gpt-image-2.5-flare-bd` | OpenAI | ¥1.138 | $0.1688 | 1K / 2K / 4K | 1 | 16 | — |
| 21 | [GPT-Image 2.5 Sunburst-bd](../vendors/openai.md#gpt-image-2.5-sunburst-bd) | `gpt-image-2.5-sunburst-bd` | OpenAI | ¥1.138 | $0.1688 | 1K / 2K / 4K | 1 | 16 | — |
| 22 | [GPT-Image 2.6 Flare](../vendors/openai.md#gpt-image-2.6-flare) | `gpt-image-2.6-flare` | OpenAI | ¥1.422 | $0.211 | 1K / 2K / 4K | 1 | 9 | GIF 动图 |
| 23 | [GPT-Image 2.6 Sunburst](../vendors/openai.md#gpt-image-2.6-sunburst) | `gpt-image-2.6-sunburst` | OpenAI | ¥1.422 | $0.211 | 1K / 2K / 4K | 1 | 9 | GIF 动图 |

部分模型按 token 计费（如 GPT-Image 2.6），表里是平台目录上的每张参考价，实际按尺寸和画质结算。

## 怎么调用

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

文生图：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"], timeout=300)

result = client.images.generate(
    model="gpt-image-2",
    prompt="一只在竹林里喝茶的熊猫，水彩风格，画面比例 1:1",  # 这个模型不读 size，比例写在提示词里
)
print(result.data[0].url)  # 临时链接（约 24 小时），请转存
```

图生图（参考图改图）：同一个接口加 `image`（公网 URL 或 `data:` URI），或用 `client.images.edit` 直接上传本地文件：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"], timeout=300)

result = client.images.edit(
    model="gpt-image-2",
    image=open("original.png", "rb"),
    prompt="把沙发改成蓝色，其余保持不变",
)
print(result.data[0].url)
```

GIF 动图（GPT-Image 2.6 Flare、GPT-Image 2.6 Sunburst）：`output_format` 传 `gif`：

```bash
curl https://api.dflop.top/v1/images/generations \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  --max-time 300 \
  -d '{"model": "gpt-image-2.6-flare", "prompt": "一只卡通小猫挥手打招呼，循环动画，纯色背景", "output_format": "gif", "size": "512x512", "frame_count": 9, "frame_duration_ms": 200}'
```

## 常见问题

**哪个生图 API 最便宜？** 按每张价格，这份目录里最便宜的三个：[Qwen Image 3.0](../vendors/alibaba-qwen-wan.md#qwen-image-3.0)，¥0.18 / 张；[Seedream 4.0](../vendors/bytedance-seedance-seedream.md#doubao-seedream-4-0-250828)，¥0.18 / 张；[Seedream 5.0](../vendors/bytedance-seedance-seedream.md#doubao-seedream-5-0-260128)，¥0.198 / 张。

**都能出 4K 吗？** 23 个里有 22 个支持 4K；不支持的是 [Seedream 5.0 Pro](../vendors/bytedance-seedance-seedream.md#doubao-seedream-5-0-pro-260628)。

**能生成 GIF 动图吗？** 能，[GPT-Image 2.6 Flare](../vendors/openai.md#gpt-image-2.6-flare)、[GPT-Image 2.6 Sunburst](../vendors/openai.md#gpt-image-2.6-sunburst) 支持，见上面的示例。

**返回的图片链接能用多久？** 是临时链接（约 24 小时），拿到后请下载转存。

**为什么要把超时设长？** 部分模型（如 GPT-Image）一张图要 30 秒到 3 分钟，客户端超时请设 300 秒以上，或者在请求里加 `"async": true` 改成提交 + 轮询。

完整参数见 [图像 API 文档](https://model.dflop.top/docs/reference/media-apis) 和 [图生图指南](https://model.dflop.top/docs/guides/image-editing)。

## English

Per-image API prices of all 23 image generation models on [XiaoZhan AIhub](https://model.dflop.top/en/models), cheapest first. Text-to-image and image editing use the OpenAI Images API shape (`POST https://api.dflop.top/v1/images/generations`, or `/v1/images/edits` for file uploads), billed per image. Cheapest: Qwen Image 3.0, Seedream 4.0 and Seedream 5.0. Animated GIF output: GPT-Image 2.6 Flare and GPT-Image 2.6 Sunburst.

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
