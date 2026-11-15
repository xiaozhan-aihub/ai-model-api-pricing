# AI 大模型 API 价格表（每日更新）· AI model API pricing

[小战AIhub](https://model.dflop.top) 上全部 124 款可调用模型的 API 价格、上下文和能力：GPT、Claude、Gemini、DeepSeek、Kimi、GLM、通义千问 Qwen、Grok 等对话大模型，GPT-Image、Seedream、Nano Banana、可灵、Qwen Image 等生图模型，Seedance、Veo、可灵 Kling、Vidu、海螺、通义万相等视频模型，以及 Suno 音乐和语音合成。每天从平台自动同步，按 CC BY 4.0 开放，可以自由使用（包括商用和 AI 训练）。

Prices, context windows and capabilities of all 124 AI models callable through [XiaoZhan AIhub](https://model.dflop.top/en): chat models (GPT, Claude, Gemini, DeepSeek, Kimi, GLM, Qwen, Grok), image models (GPT-Image, Seedream, Nano Banana, Kling, Qwen Image), video models (Seedance, Veo, Kling, Vidu, Hailuo, Wan) and Suno music. Synced from the platform every day; open data under CC BY 4.0. [English](#english)

共 124 个模型：对话大模型 56 个，图像生成 23 个，视频生成 40 个，音乐与语音 5 个；数据更新于 2026-11-14（UTC）。

- 按类别：[大模型 API 价格对比](pricing/llm-api.md) · [AI 生图 API 价格对比](pricing/image-generation-api.md) · [AI 视频生成 API 价格对比](pricing/video-generation-api.md) · [AI 音乐生成与语音合成 API](pricing/music-and-speech-api.md)
- 按厂商：[OpenAI](vendors/openai.md) · [Anthropic Claude](vendors/anthropic-claude.md) · [Google](vendors/google-gemini-veo-nano-banana.md) · [DeepSeek 深度求索](vendors/deepseek.md) · [月之暗面 Kimi](vendors/moonshot-kimi.md) · [智谱 GLM](vendors/zhipu-glm.md) · [阿里巴巴 通义](vendors/alibaba-qwen-wan.md) · [xAI Grok](vendors/xai-grok.md) · [MiniMax 海螺](vendors/minimax-hailuo.md) · [字节跳动 豆包](vendors/bytedance-seedance-seedream.md) · [快手 可灵](vendors/kuaishou-kling.md) · [生数科技 Vidu](vendors/shengshu-vidu.md) · [Suno](vendors/suno-music.md) · [小战AIhub 自有能力](vendors/xiaozhan-platform.md)
- 数据文件：[`data/models.json`](data/models.json) · [`data/models.csv`](data/models.csv) · [Hugging Face](https://huggingface.co/datasets/xiaozhan-aihub/ai-model-api-pricing)
- 怎么调用：[接入示例](https://github.com/xiaozhan-aihub/api-examples) · [文档](https://model.dflop.top/docs)

价格是实际扣费的**现价**（含限时折扣），点模型名看原价、能力和调用示例。平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

## 对话大模型（56）

价格单位：每百万 token。

| 模型 | 调用 ID | 厂商 | 上下文 | 输入 ¥ | 输出 ¥ | 输入 $ | 输出 $ | 折扣 |
|---|---|---|---|---|---|---|---|---|
| [Codex Auto Review](vendors/openai.md#codex-auto-review) | `codex-auto-review` | OpenAI | 272K | ¥0.4044 | ¥2.426 | $0.06 | $0.36 | 3 折 |
| [GPT-5.6 Luna](vendors/openai.md#gpt-5.6-luna) | `gpt-5.6-luna` | OpenAI | 1M | ¥0.4044 | ¥2.426 | $0.06 | $0.36 | 3 折 |
| [GPT-5.6 Luna-bd](vendors/openai.md#gpt-5.6-luna-bd) | `gpt-5.6-luna-bd` | OpenAI | 1.05M | ¥1.348 | ¥8.088 | $0.2 | $1.2 | — |
| [GPT-5.6 Sol](vendors/openai.md#gpt-5.6-sol) | `gpt-5.6-sol` | OpenAI | 1M | ¥10.11 | ¥60.66 | $1.5 | $9 | 3 折 |
| [GPT-5.6 Sol-bd](vendors/openai.md#gpt-5.6-sol-bd) | `gpt-5.6-sol-bd` | OpenAI | 1.05M | ¥26.96 | ¥134.8 | $4 | $20 | — |
| [GPT-5.6 Terra](vendors/openai.md#gpt-5.6-terra) | `gpt-5.6-terra` | OpenAI | 1M | ¥10.11 | ¥60.66 | $1.5 | $9 | 3 折 |
| [GPT-5.6 Terra-bd](vendors/openai.md#gpt-5.6-terra-bd) | `gpt-5.6-terra-bd` | OpenAI | 1.05M | ¥13.48 | ¥80.88 | $2 | $12 | — |
| [GPT-6](vendors/openai.md#gpt-6) | `gpt-6` | OpenAI | 1.05M | ¥20.22 | ¥101.1 | $3 | $15 | 3 折 |
| [GPT-6 Astra](vendors/openai.md#gpt-6-astra) | `gpt-6-astra` | OpenAI | 1.05M | ¥20.22 | ¥101.1 | $3 | $15 | 3 折 |
| [GPT-6 Astra-bd](vendors/openai.md#gpt-6-astra-bd) | `gpt-6-astra-bd` | OpenAI | 1.05M | ¥67.4 | ¥337 | $10 | $50 | — |
| [GPT-6 Luna](vendors/openai.md#gpt-6-luna) | `gpt-6-luna` | OpenAI | 1.05M | ¥0.2022 | ¥1.011 | $0.03 | $0.15 | 3 折 |
| [GPT-6 Luna-bd](vendors/openai.md#gpt-6-luna-bd) | `gpt-6-luna-bd` | OpenAI | 1.05M | ¥0.674 | ¥3.37 | $0.1 | $0.5 | — |
| [GPT-6 Sol](vendors/openai.md#gpt-6-sol) | `gpt-6-sol` | OpenAI | 1.05M | ¥4.044 | ¥20.22 | $0.6 | $3 | 3 折 |
| [GPT-6 Sol-bd](vendors/openai.md#gpt-6-sol-bd) | `gpt-6-sol-bd` | OpenAI | 1.05M | ¥13.48 | ¥67.4 | $2 | $10 | — |
| [GPT-6.1 Sol](vendors/openai.md#gpt-6.1-sol) | `gpt-6.1-sol` | OpenAI | 1.05M | ¥4.044 | ¥20.22 | $0.6 | $3 | 3 折 |
| [GPT-6.1 Sol-bd](vendors/openai.md#gpt-6.1-sol-bd) | `gpt-6.1-sol-bd` | OpenAI | 1.05M | ¥13.48 | ¥67.4 | $2 | $10 | — |
| [GPT-6.1 Terra](vendors/openai.md#gpt-6.1-terra) | `gpt-6.1-terra` | OpenAI | 1.05M | ¥2.022 | ¥10.11 | $0.3 | $1.5 | 3 折 |
| [Claude Fable 5](vendors/anthropic-claude.md#claude-fable-5) | `claude-fable-5` | Anthropic Claude | 200K | ¥40.44 | ¥202.2 | $6 | $30 | 6 折 |
| [Claude Fable 5.1](vendors/anthropic-claude.md#claude-fable-5-1) | `claude-fable-5-1` | Anthropic Claude | 1M | ¥40.44 | ¥202.2 | $6 | $30 | 6 折 |
| [Claude Haiku 4.5](vendors/anthropic-claude.md#claude-haiku-4-5-20251001) | `claude-haiku-4-5-20251001` | Anthropic Claude | 200K | ¥4.044 | ¥20.22 | $0.6 | $3 | 6 折 |
| [Claude Haiku 5.5](vendors/anthropic-claude.md#claude-haiku-5-5) | `claude-haiku-5-5` | Anthropic Claude | 1M | ¥0.4044 | ¥2.022 | $0.06 | $0.3 | 6 折 |
| [Claude Opus 4.5](vendors/anthropic-claude.md#claude-opus-4-5-20251101) | `claude-opus-4-5-20251101` | Anthropic Claude | 200K | ¥20.22 | ¥101.1 | $3 | $15 | 6 折 |
| [Claude Opus 4.6](vendors/anthropic-claude.md#claude-opus-4-6) | `claude-opus-4-6` | Anthropic Claude | 1M | ¥20.22 | ¥101.1 | $3 | $15 | 6 折 |
| [Claude Opus 4.7](vendors/anthropic-claude.md#claude-opus-4-7) | `claude-opus-4-7` | Anthropic Claude | 1M | ¥20.22 | ¥101.1 | $3 | $15 | 6 折 |
| [Claude Opus 4.8](vendors/anthropic-claude.md#claude-opus-4-8) | `claude-opus-4-8` | Anthropic Claude | 1M | ¥20.22 | ¥101.1 | $3 | $15 | 6 折 |
| [Claude Opus 5](vendors/anthropic-claude.md#claude-opus-5) | `claude-opus-5` | Anthropic Claude | 1M | ¥20.22 | ¥101.1 | $3 | $15 | 6 折 |
| [Claude Opus 5.5](vendors/anthropic-claude.md#claude-opus-5-5) | `claude-opus-5-5` | Anthropic Claude | 1M | ¥16.18 | ¥80.88 | $2.4 | $12 | 6 折 |
| [Claude Sonnet 4.5](vendors/anthropic-claude.md#claude-sonnet-4-5-20250929) | `claude-sonnet-4-5-20250929` | Anthropic Claude | 200K | ¥12.13 | ¥60.66 | $1.8 | $9 | 6 折 |
| [Claude Sonnet 4.6](vendors/anthropic-claude.md#claude-sonnet-4-6) | `claude-sonnet-4-6` | Anthropic Claude | 1M | ¥12.13 | ¥60.66 | $1.8 | $9 | 6 折 |
| [Claude Sonnet 5](vendors/anthropic-claude.md#claude-sonnet-5) | `claude-sonnet-5` | Anthropic Claude | 1M | ¥8.088 | ¥40.44 | $1.2 | $6 | 6 折 |
| [Claude Sonnet 5.5](vendors/anthropic-claude.md#claude-sonnet-5-5) | `claude-sonnet-5-5` | Anthropic Claude | 1M | ¥1.855 | ¥9.277 | $0.2753 | $1.376 | — |
| [Gemini 3.1 Pro](vendors/google-gemini-veo-nano-banana.md#gemini-3.1-pro-low) | `gemini-3.1-pro-low` | Google | 2M | ¥6.74 | ¥40.44 | $1 | $6 | 5 折 |
| [Gemini 3.1 Pro Preview 1020](vendors/google-gemini-veo-nano-banana.md#gemini-3.1-pro-preview-1020) | `gemini-3.1-pro-preview-1020` | Google | 1M | ¥6.74 | ¥40.44 | $1 | $6 | 5 折 |
| [Gemini 3.8 Flash](vendors/google-gemini-veo-nano-banana.md#gemini-3.8-flash) | `gemini-3.8-flash` | Google | 1M | ¥2.527 | ¥12.64 | $0.375 | $1.875 | 5 折 |
| [Gemini 3.8 Flash-nx](vendors/google-gemini-veo-nano-banana.md#gemini-3.8-flash-nx) | `gemini-3.8-flash-nx` | Google | 1M | ¥5.055 | ¥25.27 | $0.75 | $3.75 | — |
| [Gemini 4 Argon](vendors/google-gemini-veo-nano-banana.md#gemini-4-argon) | `gemini-4-argon` | Google | 1M | ¥6.74 | ¥33.7 | $1 | $5 | 5 折 |
| [Gemini 4 Argon-nx](vendors/google-gemini-veo-nano-banana.md#gemini-4-argon-nx) | `gemini-4-argon-nx` | Google | 1M | ¥13.48 | ¥67.4 | $2 | $10 | — |
| [DeepSeek V4 Flash](vendors/deepseek.md#deepseek-v4-flash) | `deepseek-v4-flash` | DeepSeek 深度求索 | 1M | ¥1.4 | ¥5.6 | $0.2077 | $0.8309 | 7 折 |
| [DeepSeek V4 Pro](vendors/deepseek.md#deepseek-v4-pro) | `deepseek-v4-pro` | DeepSeek 深度求索 | 128K | ¥6.3 | ¥18.9 | $0.9347 | $2.804 | 7 折 |
| [DeepSeek V4.1 Flash](vendors/deepseek.md#deepseek-v4.1-flash) | `deepseek-v4.1-flash` | DeepSeek 深度求索 | 1M | ¥1.4 | ¥5.6 | $0.2077 | $0.8309 | 7 折 |
| [Kimi K2.5](vendors/moonshot-kimi.md#kimi-k2.5) | `kimi-k2.5` | 月之暗面 Kimi | 256K | ¥4.044 | ¥16.85 | $0.6 | $2.5 | — |
| [Kimi K2.6](vendors/moonshot-kimi.md#kimi-k2.6) | `kimi-k2.6` | 月之暗面 Kimi | 256K | ¥4.044 | ¥16.85 | $0.6 | $2.5 | — |
| [Kimi K2.7 Code](vendors/moonshot-kimi.md#kimi-k2.7-code) | `kimi-k2.7-code` | 月之暗面 Kimi | 256K | ¥4.044 | ¥16.85 | $0.6 | $2.5 | — |
| [Kimi K3](vendors/moonshot-kimi.md#kimi-k3) | `kimi-k3` | 月之暗面 Kimi | 256K | ¥20 | ¥100 | $2.967 | $14.84 | — |
| [Kimi K3 1013](vendors/moonshot-kimi.md#kimi-k3-1013) | `kimi-k3-1013` | 月之暗面 Kimi | 256K | ¥15 | ¥75 | $2.226 | $11.13 | 7.5 折 |
| [GLM-5.3](vendors/zhipu-glm.md#glm-5.3) | `glm-5.3` | 智谱 GLM | 1M | ¥5.6 | ¥19.6 | $0.8309 | $2.908 | 7 折 |
| [GLM-5.3-1022](vendors/zhipu-glm.md#glm-5.3-1022) | `glm-5.3-1022` | 智谱 GLM | 1M | ¥8 | ¥28 | $1.187 | $4.154 | — |
| [GLM-5.3-Flash](vendors/zhipu-glm.md#glm-5.3-flash) | `glm-5.3-flash` | 智谱 GLM | 1M | ¥0.56 | ¥1.96 | $0.08309 | $0.2908 | 7 折 |
| [GLM-5.3-Flash-1022](vendors/zhipu-glm.md#glm-5.3-flash-1022) | `glm-5.3-flash-1022` | 智谱 GLM | 1M | ¥0.8 | ¥2.8 | $0.1187 | $0.4154 | — |
| [Qwen3.8-Max-cjx](vendors/alibaba-qwen-wan.md#qwen3.8-max-cjx) | `qwen3.8-max-cjx` | 阿里巴巴 通义 | 1M | ¥8.4 | ¥25.2 | $1.246 | $3.739 | 7 折 |
| [Qwen3.8-Omni-Flash](vendors/alibaba-qwen-wan.md#qwen3.8-omni-flash) | `qwen3.8-omni-flash` | 阿里巴巴 通义 | 1M | ¥0.8 | ¥2.7 | $0.1187 | $0.4006 | — |
| [Grok 4.5](vendors/xai-grok.md#grok-4.5) | `grok-4.5` | xAI Grok | 500K | ¥4.044 | ¥12.13 | $0.6 | $1.8 | 3 折 |
| [Grok 4.6](vendors/xai-grok.md#grok-4.6) | `grok-4.6` | xAI Grok | 500K | ¥4.044 | ¥12.13 | $0.6 | $1.8 | 3 折 |
| [Grok 4.7](vendors/xai-grok.md#grok-4.7) | `grok-4.7` | xAI Grok | 500K | ¥4.044 | ¥12.13 | $0.6 | $1.8 | 3 折 |
| [MiniMax M2.7](vendors/minimax-hailuo.md#MiniMax-M2.7) | `MiniMax-M2.7` | MiniMax 海螺 | 200K | ¥2.022 | ¥10.11 | $0.3 | $1.5 | — |
| [xiaozhanAI](vendors/xiaozhan-platform.md#xiaozhanAI) | `xiaozhanAI` | 小战AIhub 自有能力 | 1.05M | ¥2.022 | ¥10.11 | $0.3 | $1.5 | — |

## 图像生成（23）

| 模型 | 调用 ID | 厂商 | 价格 ¥ | 价格 $ | 折扣 |
|---|---|---|---|---|---|
| [GPT-Image 2](vendors/openai.md#gpt-image-2) | `gpt-image-2` | OpenAI | ¥0.3 / 张 | $0.04451 / 张 | — |
| [GPT-Image 2-bd](vendors/openai.md#gpt-image-2-bd) | `gpt-image-2-bd` | OpenAI | ¥1.138 / 张 | $0.1688 / 张 | — |
| [GPT-Image 2.5 Flare](vendors/openai.md#gpt-image-2.5-flare) | `gpt-image-2.5-flare` | OpenAI | ¥0.3 / 张 | $0.04451 / 张 | — |
| [GPT-Image 2.5 Flare-bd](vendors/openai.md#gpt-image-2.5-flare-bd) | `gpt-image-2.5-flare-bd` | OpenAI | ¥1.138 / 张 | $0.1688 / 张 | — |
| [GPT-Image 2.5 Sunburst](vendors/openai.md#gpt-image-2.5-sunburst) | `gpt-image-2.5-sunburst` | OpenAI | ¥0.3 / 张 | $0.04451 / 张 | — |
| [GPT-Image 2.5 Sunburst-bd](vendors/openai.md#gpt-image-2.5-sunburst-bd) | `gpt-image-2.5-sunburst-bd` | OpenAI | ¥1.138 / 张 | $0.1688 / 张 | — |
| [GPT-Image 2.6 Flare](vendors/openai.md#gpt-image-2.6-flare) | `gpt-image-2.6-flare` | OpenAI | ¥1.422 / 张 | $0.211 / 张 | — |
| [GPT-Image 2.6 Sunburst](vendors/openai.md#gpt-image-2.6-sunburst) | `gpt-image-2.6-sunburst` | OpenAI | ¥1.422 / 张 | $0.211 / 张 | — |
| [Nano Banana](vendors/google-gemini-veo-nano-banana.md#nano-banana) | `nano-banana` | Google | ¥0.3 / 张 | $0.04451 / 张 | — |
| [Nano Banana 2](vendors/google-gemini-veo-nano-banana.md#nano-banana-2) | `nano-banana-2` | Google | ¥0.3 / 张 | $0.04451 / 张 | — |
| [Nano Banana 2.1](vendors/google-gemini-veo-nano-banana.md#nano-banana-2.1) | `nano-banana-2.1` | Google | ¥0.3 / 张 | $0.04451 / 张 | — |
| [Nano Banana Pro](vendors/google-gemini-veo-nano-banana.md#nano-banana-pro) | `nano-banana-pro` | Google | ¥0.3 / 张 | $0.04451 / 张 | — |
| [Qwen Image 3.0](vendors/alibaba-qwen-wan.md#qwen-image-3.0) | `qwen-image-3.0` | 阿里巴巴 通义 | ¥0.18 / 张 | $0.02671 / 张 | — |
| [Qwen Image 3.0 Pro](vendors/alibaba-qwen-wan.md#qwen-image-3.0-pro) | `qwen-image-3.0-pro` | 阿里巴巴 通义 | ¥0.25 / 张 | $0.03709 / 张 | — |
| [Grok Imagine (Image · Quality)](vendors/xai-grok.md#grok-imagine-image-quality) | `grok-imagine-image-quality` | xAI Grok | ¥0.3 / 张 | $0.04451 / 张 | — |
| [Grok Imagine (Image)](vendors/xai-grok.md#grok-imagine-image) | `grok-imagine-image` | xAI Grok | ¥0.3 / 张 | $0.04451 / 张 | — |
| [Seedream 4.0](vendors/bytedance-seedance-seedream.md#doubao-seedream-4-0-250828) | `doubao-seedream-4-0-250828` | 字节跳动 豆包 | ¥0.18 / 张 | $0.02671 / 张 | — |
| [Seedream 4.5](vendors/bytedance-seedance-seedream.md#doubao-seedream-4-5-251128) | `doubao-seedream-4-5-251128` | 字节跳动 豆包 | ¥0.225 / 张 | $0.03338 / 张 | — |
| [Seedream 5.0](vendors/bytedance-seedance-seedream.md#doubao-seedream-5-0-260128) | `doubao-seedream-5-0-260128` | 字节跳动 豆包 | ¥0.198 / 张 | $0.02938 / 张 | — |
| [Seedream 5.0 Pro](vendors/bytedance-seedance-seedream.md#doubao-seedream-5-0-pro-260628) | `doubao-seedream-5-0-pro-260628` | 字节跳动 豆包 | ¥0.27 / 张 | $0.04006 / 张 | — |
| [可灵图像 3.0](vendors/kuaishou-kling.md#tvod-kling-image-3.0) | `tvod-kling-image-3.0` | 快手 可灵 | ¥0.337 / 张 | $0.05 / 张 | — |
| [可灵图像 3.0 Omni](vendors/kuaishou-kling.md#tvod-kling-image-3.0-omni) | `tvod-kling-image-3.0-omni` | 快手 可灵 | ¥0.4044 / 张 | $0.06 / 张 | — |
| [xiaozhanimage](vendors/xiaozhan-platform.md#xiaozhanimage) | `xiaozhanimage` | 小战AIhub 自有能力 | ¥0.5 / 张 | $0.07418 / 张 | — |

## 视频生成（40）

视频按秒计价的是平台目录上的标价；多数视频模型按分辨率分档，具体见模型页。

| 模型 | 调用 ID | 厂商 | 价格 ¥ | 价格 $ | 折扣 |
|---|---|---|---|---|---|
| [Veo 3.1](vendors/google-gemini-veo-nano-banana.md#tvod-veo-3.1) | `tvod-veo-3.1` | Google | ¥0.674 / 秒 | $0.1 / 秒 | — |
| [Veo 3.1 Fast](vendors/google-gemini-veo-nano-banana.md#tvod-veo-3.1-fast) | `tvod-veo-3.1-fast` | Google | ¥0.8088 / 秒 | $0.12 / 秒 | — |
| [Veo 3.1 Lite](vendors/google-gemini-veo-nano-banana.md#tvod-veo-3.1-lite) | `tvod-veo-3.1-lite` | Google | ¥0.5392 / 秒 | $0.08 / 秒 | — |
| [万相 3.0 视频生成](vendors/alibaba-qwen-wan.md#wan3.0-video) | `wan3.0-video` | 阿里巴巴 通义 | ¥1.08 / 秒 | $0.1602 / 秒 | 9 折 |
| [万相 3.0 视频生成 Prime](vendors/alibaba-qwen-wan.md#wan3.0-video-prime) | `wan3.0-video-prime` | 阿里巴巴 通义 | ¥1.62 / 秒 | $0.2404 / 秒 | 9 折 |
| [快乐马 1.1 全能参考](vendors/alibaba-qwen-wan.md#happyhorse-1.1-r2v) | `happyhorse-1.1-r2v` | 阿里巴巴 通义 | ¥1.2 / 秒 | $0.178 / 秒 | — |
| [快乐马 1.1 图生视频](vendors/alibaba-qwen-wan.md#happyhorse-1.1-i2v) | `happyhorse-1.1-i2v` | 阿里巴巴 通义 | ¥1.2 / 秒 | $0.178 / 秒 | — |
| [快乐马 1.1 文生视频](vendors/alibaba-qwen-wan.md#happyhorse-1.1-t2v) | `happyhorse-1.1-t2v` | 阿里巴巴 通义 | ¥1.2 / 秒 | $0.178 / 秒 | — |
| [Grok Imagine Video](vendors/xai-grok.md#grok-imagine-video) | `grok-imagine-video` | xAI Grok | ¥0.1 / 秒 | $0.01484 / 秒 | — |
| [Grok Imagine Video 1.5](vendors/xai-grok.md#grok-imagine-video-1.5-preview) | `grok-imagine-video-1.5-preview` | xAI Grok | ¥0.1 / 秒 | $0.01484 / 秒 | — |
| [海螺 H3](vendors/minimax-hailuo.md#minimax-h3) | `minimax-h3` | MiniMax 海螺 | ¥0.8 / 秒 | $0.1187 / 秒 | — |
| [海螺 H3 Max](vendors/minimax-hailuo.md#minimax-h3-max) | `minimax-h3-max` | MiniMax 海螺 | ¥0.5 / 秒 | $0.07418 / 秒 | — |
| [海螺 H3 tx](vendors/minimax-hailuo.md#minimax-h3-tx) | `minimax-h3-tx` | MiniMax 海螺 | ¥0.5 / 秒 | $0.07418 / 秒 | — |
| [海螺 H3 提速版 tx](vendors/minimax-hailuo.md#minimax-h3-fast-tx) | `minimax-h3-fast-tx` | MiniMax 海螺 | ¥0.4 / 秒 | $0.05935 / 秒 | — |
| [海螺 H3 提速版带IR tx](vendors/minimax-hailuo.md#minimax-h3-fast-ir-tx) | `minimax-h3-fast-ir-tx` | MiniMax 海螺 | ¥0.4 / 秒 | $0.05935 / 秒 | — |
| [海螺 H3 满血版 tx](vendors/minimax-hailuo.md#minimax-h3-medium-tx) | `minimax-h3-medium-tx` | MiniMax 海螺 | ¥0.5 / 秒 | $0.07418 / 秒 | — |
| [海螺 H3 满血版带IR tx](vendors/minimax-hailuo.md#minimax-h3-medium-ir-tx) | `minimax-h3-medium-ir-tx` | MiniMax 海螺 | ¥0.5 / 秒 | $0.07418 / 秒 | — |
| [Seedance 2.0](vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0) | `doubao-seedance-2.0` | 字节跳动 豆包 | ¥2.231 / 秒 | $0.331 / 秒 | 9 折 |
| [Seedance 2.0 Fast](vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-fast) | `doubao-seedance-2.0-fast` | 字节跳动 豆包 | ¥0.7193 / 秒 | $0.1067 / 秒 | 9 折 |
| [Seedance 2.0 Fast Lite](vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-fast-lite) | `doubao-seedance-2.0-fast-lite` | 字节跳动 豆包 | ¥0.6394 / 秒 | $0.09486 / 秒 | 8 折 |
| [Seedance 2.0 Lite](vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-lite) | `doubao-seedance-2.0-lite` | 字节跳动 豆包 | ¥0.7949 / 秒 | $0.1179 / 秒 | 8 折 |
| [Seedance 2.0 Mini](vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-mini) | `doubao-seedance-2.0-mini` | 字节跳动 豆包 | ¥0.4471 / 秒 | $0.06634 / 秒 | 9 折 |
| [Seedance 2.0 Mini Lite](vendors/bytedance-seedance-seedream.md#doubao-seedance-2.0-mini-lite) | `doubao-seedance-2.0-mini-lite` | 字节跳动 豆包 | ¥0.3974 / 秒 | $0.05897 / 秒 | 8 折 |
| [Seedance 2.0 YD](vendors/bytedance-seedance-seedream.md#seedance2.0-yd) | `seedance2.0-yd` | 字节跳动 豆包 | ¥1.983 / 秒 | $0.2942 / 秒 | 8 折 |
| [Seedance 2.5](vendors/bytedance-seedance-seedream.md#doubao-seedance-2.5) | `doubao-seedance-2.5` | 字节跳动 豆包 | ¥3.368 / 秒 | $0.4997 / 秒 | 9 折 |
| [Seedance 2.5 Lite](vendors/bytedance-seedance-seedream.md#doubao-seedance-2.5-lite) | `doubao-seedance-2.5-lite` | 字节跳动 豆包 | ¥1.21 / 秒 | $0.1795 / 秒 | 8 折 |
| [可灵 3.0](vendors/kuaishou-kling.md#tvod-kling-video-3.0) | `tvod-kling-video-3.0` | 快手 可灵 | ¥0.5392 / 秒 | $0.08 / 秒 | — |
| [可灵 3.0 Omni](vendors/kuaishou-kling.md#tvod-kling-video-3.0-omni) | `tvod-kling-video-3.0-omni` | 快手 可灵 | ¥0.5392 / 秒 | $0.08 / 秒 | — |
| [可灵 4.0](vendors/kuaishou-kling.md#tvod-kling-video-4.0) | `tvod-kling-video-4.0` | 快手 可灵 | ¥1.14 / 秒 | $0.1691 / 秒 | 9.5 折 |
| [可灵 4.0 Omni](vendors/kuaishou-kling.md#tvod-kling-video-4.0-omni) | `tvod-kling-video-4.0-omni` | 快手 可灵 | ¥1.14 / 秒 | $0.1691 / 秒 | 9.5 折 |
| [可灵 O1](vendors/kuaishou-kling.md#tvod-kling-video-o1) | `tvod-kling-video-o1` | 快手 可灵 | ¥0.337 / 秒 | $0.05 / 秒 | — |
| [Vidu Q3](vendors/shengshu-vidu.md#tvod-vidu-video-q3) | `tvod-vidu-video-q3` | 生数科技 Vidu | ¥0.3774 / 秒 | $0.056 / 秒 | 8 折 |
| [Vidu Q3 Mix](vendors/shengshu-vidu.md#tvod-vidu-video-q3-mix) | `tvod-vidu-video-q3-mix` | 生数科技 Vidu | ¥0.3774 / 秒 | $0.056 / 秒 | 8 折 |
| [Vidu Q3 Pro](vendors/shengshu-vidu.md#tvod-vidu-video-q3-pro) | `tvod-vidu-video-q3-pro` | 生数科技 Vidu | ¥0.3774 / 秒 | $0.056 / 秒 | 8 折 |
| [Vidu Q3 Turbo](vendors/shengshu-vidu.md#tvod-vidu-video-q3-turbo) | `tvod-vidu-video-q3-turbo` | 生数科技 Vidu | ¥0.3774 / 秒 | $0.056 / 秒 | 8 折 |
| [Vidu Q3 广告版](vendors/shengshu-vidu.md#tvod-vidu-video-q3-ad) | `tvod-vidu-video-q3-ad` | 生数科技 Vidu | ¥0.3774 / 秒 | $0.056 / 秒 | 8 折 |
| [Vidu Q3 短剧版](vendors/shengshu-vidu.md#tvod-vidu-video-q3-drama) | `tvod-vidu-video-q3-drama` | 生数科技 Vidu | ¥0.3774 / 秒 | $0.056 / 秒 | 8 折 |
| [创建数字人形象](vendors/xiaozhan-platform.md#dh-avatar-create) | `dh-avatar-create` | 小战AIhub 自有能力 | 价格见模型页 | — | — |
| [数字人视频](vendors/xiaozhan-platform.md#dh-avatar) | `dh-avatar` | 小战AIhub 自有能力 | ¥0.06 / 秒 | $0.008902 / 秒 | — |
| [智能剪辑](vendors/xiaozhan-platform.md#clip-compose) | `clip-compose` | 小战AIhub 自有能力 | ¥1.5 / 次 | $0.2226 / 次 | — |

## 音乐与语音（5）

| 模型 | 调用 ID | 厂商 | 价格 ¥ | 价格 $ | 折扣 |
|---|---|---|---|---|---|
| [Suno V6 (最新)](vendors/suno-music.md#suno-v6) | `suno-v6` | Suno | 按次计费（一次生成 2 首） | — | — |
| [Suno V6 Mini](vendors/suno-music.md#suno-v6-mini) | `suno-v6-mini` | Suno | 按次计费（一次生成 2 首） | — | — |
| [Suno V6 Wild](vendors/suno-music.md#suno-v6-wild) | `suno-v6-wild` | Suno | 按次计费（一次生成 2 首） | — | — |
| [声音克隆 · 创建音色](vendors/xiaozhan-platform.md#voice-clone-pro) | `voice-clone-pro` | 小战AIhub 自有能力 | 按次计费 | — | — |
| [语音合成](vendors/xiaozhan-platform.md#voice-tts-pro) | `voice-tts-pro` | 小战AIhub 自有能力 | 按字符计费 | — | — |

## 数据文件

| 文件 | 内容 |
|---|---|
| [`data/models.json`](data/models.json) | 完整数据：调用 ID、名称、厂商、类别、上下文、最大输出、能力、现价与原价（积分、≈人民币、≈美元）、上架与更新日期、模型页链接、许可证 |
| [`data/models.csv`](data/models.csv) | 同一份数据的表格版（价格写人民币和美元） |

实时源：<https://model.dflop.top/data/models.json>、<https://model.dflop.top/data/models.csv>。这里是每天的快照，提交历史就是价格和上下架的变化记录。Hugging Face 镜像：[xiaozhan-aihub/ai-model-api-pricing](https://huggingface.co/datasets/xiaozhan-aihub/ai-model-api-pricing)（`load_dataset("xiaozhan-aihub/ai-model-api-pricing")`）。

## 字段（models.json 里的每个模型）

| 字段 | 说明 |
|---|---|
| `id` | 调用时 `model` 填的值 |
| `name`、`vendor`、`category`（text / image / video / audio）、`category_label` | 名称、厂商、类别 |
| `context_window`、`max_output_tokens` | 上下文窗口、最大输出 token |
| `capabilities` | 能力，如 Image input、Tool calling、Thinking mode、Web search |
| `price` | **现价**（实际扣费，含限时折扣）：每个计价项给 `credits`（平台积分）、`cny`、`usd` |
| `list_price`、`promotion_factor` | 原价与折扣系数（没有折扣时与现价相同） |
| `released_at`、`updated_at` | 上架日期；价格、名称、描述、能力最后一次变化的时间 |
| `url` | 模型详情页 |

## 怎么调用这些模型

一把 `sk-gpushare-` 密钥，OpenAI SDK 把 `base_url` 换成 `https://api.dflop.top/v1`，`model` 填上面的调用 ID 就行；Anthropic SDK 和 Google Gemini SDK 也能直接用。先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="gpt-6-luna",
    messages=[{"role": "user", "content": "用三句话介绍一下你自己"}],
)
print(resp.choices[0].message.content)
```

生图、视频、音乐、语音的接口和示例见各类别页，以及 [api-examples](https://github.com/xiaozhan-aihub/api-examples)。

## 常见问题

**小战AIhub是什么？** 多协议大模型 API 网关与 AI 创作平台（[model.dflop.top](https://model.dflop.top)）：一把 `sk-gpushare-` 密钥，用 OpenAI / Anthropic / Gemini SDK 调用 124 款对话、图像、视频、音乐与语音模型。

**价格多久更新？** 这个仓库每天 02:17（UTC）从平台同步一次，有变化才提交；要看实时价格，打开 [模型广场](https://model.dflop.top/models) 或 [`/data/models.json`](https://model.dflop.top/data/models.json)。

**现价和原价有什么区别？** 现价是现在实际扣费的价格，已经算上限时折扣；原价见 `list_price`，折扣系数见 `promotion_factor`。

**这些数据可以商用或拿去训练模型吗？** 可以。按 CC BY 4.0 授权，注明来源「小战AIhub」并附链接即可。

## English

This repository mirrors the open model catalogue of [XiaoZhan AIhub](https://model.dflop.top/en), a multi-protocol AI model gateway: one `sk-gpushare-` key lets the OpenAI, Anthropic and Google Gemini SDKs call all 124 models listed above. The tables show the price charged now, promotions included, in CNY and USD (converted from platform credits); follow a model name for its list price, capabilities and a code sample.

- By category: [LLM API pricing comparison](pricing/llm-api.md) · [Image generation API pricing comparison](pricing/image-generation-api.md) · [Video generation API pricing comparison](pricing/video-generation-api.md) · [Music generation and text-to-speech API](pricing/music-and-speech-api.md)
- Data: [`data/models.json`](data/models.json), [`data/models.csv`](data/models.csv), also on [Hugging Face](https://huggingface.co/datasets/xiaozhan-aihub/ai-model-api-pricing). Live sources: <https://model.dflop.top/data/models.json>.
- Calling the models: [api-examples](https://github.com/xiaozhan-aihub/api-examples) and the [documentation](https://model.dflop.top/en/docs).
- Licence: CC BY 4.0. Free to use, share and adapt, commercially and for AI training; please credit "XiaoZhan AIhub" with a link to <https://model.dflop.top/models>. The commit history is the record of price and listing changes.

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](scripts/render.py) 根据 [data/models.json](data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](data/models.json).
