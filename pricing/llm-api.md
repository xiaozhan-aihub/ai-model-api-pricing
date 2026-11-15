# 大模型 API 价格对比：GPT、Claude、Gemini、DeepSeek、Kimi、GLM、Qwen、Grok（56 个模型）

> LLM API pricing comparison: 56 models (GPT, Claude, Gemini, DeepSeek, Kimi, GLM, Qwen, Grok) through one API. Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上全部 56 个对话大模型的 API 价格，按输入价从低到高排列，来自 OpenAI、Anthropic Claude、Google、DeepSeek 深度求索、月之暗面 Kimi、智谱 GLM、阿里巴巴 通义、xAI Grok、MiniMax 海螺、小战AIhub 自有能力。一把 `sk-gpushare-` 密钥，OpenAI SDK 改个 `base_url` 就能调用下表任一模型。

价格是实际扣费的现价（含限时折扣），单位是每百万 token。平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部类别](../README.md) · [`models.json`](../data/models.json)

## 价格表（输入价从低到高）

| # | 模型 | 调用 ID | 厂商 | 上下文 | 输入 ¥ | 输出 ¥ | 输入 $ | 输出 $ | 折扣 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [GPT-6 Luna](../vendors/openai.md#gpt-6-luna) | `gpt-6-luna` | OpenAI | 1.05M | ¥0.2022 | ¥1.011 | $0.03 | $0.15 | 3 折 |
| 2 | [Claude Haiku 5.5](../vendors/anthropic-claude.md#claude-haiku-5-5) | `claude-haiku-5-5` | Anthropic Claude | 1M | ¥0.4044 | ¥2.022 | $0.06 | $0.3 | 6 折 |
| 3 | [Codex Auto Review](../vendors/openai.md#codex-auto-review) | `codex-auto-review` | OpenAI | 272K | ¥0.4044 | ¥2.426 | $0.06 | $0.36 | 3 折 |
| 4 | [GPT-5.6 Luna](../vendors/openai.md#gpt-5.6-luna) | `gpt-5.6-luna` | OpenAI | 1M | ¥0.4044 | ¥2.426 | $0.06 | $0.36 | 3 折 |
| 5 | [GLM-5.3-Flash](../vendors/zhipu-glm.md#glm-5.3-flash) | `glm-5.3-flash` | 智谱 GLM | 1M | ¥0.56 | ¥1.96 | $0.08309 | $0.2908 | 7 折 |
| 6 | [GPT-6 Luna-bd](../vendors/openai.md#gpt-6-luna-bd) | `gpt-6-luna-bd` | OpenAI | 1.05M | ¥0.674 | ¥3.37 | $0.1 | $0.5 | — |
| 7 | [GLM-5.3-Flash-1022](../vendors/zhipu-glm.md#glm-5.3-flash-1022) | `glm-5.3-flash-1022` | 智谱 GLM | 1M | ¥0.8 | ¥2.8 | $0.1187 | $0.4154 | — |
| 8 | [Qwen3.8-Omni-Flash](../vendors/alibaba-qwen-wan.md#qwen3.8-omni-flash) | `qwen3.8-omni-flash` | 阿里巴巴 通义 | 1M | ¥0.8 | ¥2.7 | $0.1187 | $0.4006 | — |
| 9 | [GPT-5.6 Luna-bd](../vendors/openai.md#gpt-5.6-luna-bd) | `gpt-5.6-luna-bd` | OpenAI | 1.05M | ¥1.348 | ¥8.088 | $0.2 | $1.2 | — |
| 10 | [DeepSeek V4 Flash](../vendors/deepseek.md#deepseek-v4-flash) | `deepseek-v4-flash` | DeepSeek 深度求索 | 1M | ¥1.4 | ¥5.6 | $0.2077 | $0.8309 | 7 折 |
| 11 | [DeepSeek V4.1 Flash](../vendors/deepseek.md#deepseek-v4.1-flash) | `deepseek-v4.1-flash` | DeepSeek 深度求索 | 1M | ¥1.4 | ¥5.6 | $0.2077 | $0.8309 | 7 折 |
| 12 | [Claude Sonnet 5.5](../vendors/anthropic-claude.md#claude-sonnet-5-5) | `claude-sonnet-5-5` | Anthropic Claude | 1M | ¥1.855 | ¥9.277 | $0.2753 | $1.376 | — |
| 13 | [GPT-6.1 Terra](../vendors/openai.md#gpt-6.1-terra) | `gpt-6.1-terra` | OpenAI | 1.05M | ¥2.022 | ¥10.11 | $0.3 | $1.5 | 3 折 |
| 14 | [MiniMax M2.7](../vendors/minimax-hailuo.md#MiniMax-M2.7) | `MiniMax-M2.7` | MiniMax 海螺 | 200K | ¥2.022 | ¥10.11 | $0.3 | $1.5 | — |
| 15 | [xiaozhanAI](../vendors/xiaozhan-platform.md#xiaozhanAI) | `xiaozhanAI` | 小战AIhub 自有能力 | 1.05M | ¥2.022 | ¥10.11 | $0.3 | $1.5 | — |
| 16 | [Gemini 3.8 Flash](../vendors/google-gemini-veo-nano-banana.md#gemini-3.8-flash) | `gemini-3.8-flash` | Google | 1M | ¥2.527 | ¥12.64 | $0.375 | $1.875 | 5 折 |
| 17 | [Claude Haiku 4.5](../vendors/anthropic-claude.md#claude-haiku-4-5-20251001) | `claude-haiku-4-5-20251001` | Anthropic Claude | 200K | ¥4.044 | ¥20.22 | $0.6 | $3 | 6 折 |
| 18 | [GPT-6 Sol](../vendors/openai.md#gpt-6-sol) | `gpt-6-sol` | OpenAI | 1.05M | ¥4.044 | ¥20.22 | $0.6 | $3 | 3 折 |
| 19 | [GPT-6.1 Sol](../vendors/openai.md#gpt-6.1-sol) | `gpt-6.1-sol` | OpenAI | 1.05M | ¥4.044 | ¥20.22 | $0.6 | $3 | 3 折 |
| 20 | [Grok 4.5](../vendors/xai-grok.md#grok-4.5) | `grok-4.5` | xAI Grok | 500K | ¥4.044 | ¥12.13 | $0.6 | $1.8 | 3 折 |
| 21 | [Grok 4.6](../vendors/xai-grok.md#grok-4.6) | `grok-4.6` | xAI Grok | 500K | ¥4.044 | ¥12.13 | $0.6 | $1.8 | 3 折 |
| 22 | [Grok 4.7](../vendors/xai-grok.md#grok-4.7) | `grok-4.7` | xAI Grok | 500K | ¥4.044 | ¥12.13 | $0.6 | $1.8 | 3 折 |
| 23 | [Kimi K2.5](../vendors/moonshot-kimi.md#kimi-k2.5) | `kimi-k2.5` | 月之暗面 Kimi | 256K | ¥4.044 | ¥16.85 | $0.6 | $2.5 | — |
| 24 | [Kimi K2.6](../vendors/moonshot-kimi.md#kimi-k2.6) | `kimi-k2.6` | 月之暗面 Kimi | 256K | ¥4.044 | ¥16.85 | $0.6 | $2.5 | — |
| 25 | [Kimi K2.7 Code](../vendors/moonshot-kimi.md#kimi-k2.7-code) | `kimi-k2.7-code` | 月之暗面 Kimi | 256K | ¥4.044 | ¥16.85 | $0.6 | $2.5 | — |
| 26 | [Gemini 3.8 Flash-nx](../vendors/google-gemini-veo-nano-banana.md#gemini-3.8-flash-nx) | `gemini-3.8-flash-nx` | Google | 1M | ¥5.055 | ¥25.27 | $0.75 | $3.75 | — |
| 27 | [GLM-5.3](../vendors/zhipu-glm.md#glm-5.3) | `glm-5.3` | 智谱 GLM | 1M | ¥5.6 | ¥19.6 | $0.8309 | $2.908 | 7 折 |
| 28 | [DeepSeek V4 Pro](../vendors/deepseek.md#deepseek-v4-pro) | `deepseek-v4-pro` | DeepSeek 深度求索 | 128K | ¥6.3 | ¥18.9 | $0.9347 | $2.804 | 7 折 |
| 29 | [Gemini 3.1 Pro](../vendors/google-gemini-veo-nano-banana.md#gemini-3.1-pro-low) | `gemini-3.1-pro-low` | Google | 2M | ¥6.74 | ¥40.44 | $1 | $6 | 5 折 |
| 30 | [Gemini 3.1 Pro Preview 1020](../vendors/google-gemini-veo-nano-banana.md#gemini-3.1-pro-preview-1020) | `gemini-3.1-pro-preview-1020` | Google | 1M | ¥6.74 | ¥40.44 | $1 | $6 | 5 折 |
| 31 | [Gemini 4 Argon](../vendors/google-gemini-veo-nano-banana.md#gemini-4-argon) | `gemini-4-argon` | Google | 1M | ¥6.74 | ¥33.7 | $1 | $5 | 5 折 |
| 32 | [GLM-5.3-1022](../vendors/zhipu-glm.md#glm-5.3-1022) | `glm-5.3-1022` | 智谱 GLM | 1M | ¥8 | ¥28 | $1.187 | $4.154 | — |
| 33 | [Claude Sonnet 5](../vendors/anthropic-claude.md#claude-sonnet-5) | `claude-sonnet-5` | Anthropic Claude | 1M | ¥8.088 | ¥40.44 | $1.2 | $6 | 6 折 |
| 34 | [Qwen3.8-Max-cjx](../vendors/alibaba-qwen-wan.md#qwen3.8-max-cjx) | `qwen3.8-max-cjx` | 阿里巴巴 通义 | 1M | ¥8.4 | ¥25.2 | $1.246 | $3.739 | 7 折 |
| 35 | [GPT-5.6 Sol](../vendors/openai.md#gpt-5.6-sol) | `gpt-5.6-sol` | OpenAI | 1M | ¥10.11 | ¥60.66 | $1.5 | $9 | 3 折 |
| 36 | [GPT-5.6 Terra](../vendors/openai.md#gpt-5.6-terra) | `gpt-5.6-terra` | OpenAI | 1M | ¥10.11 | ¥60.66 | $1.5 | $9 | 3 折 |
| 37 | [Claude Sonnet 4.5](../vendors/anthropic-claude.md#claude-sonnet-4-5-20250929) | `claude-sonnet-4-5-20250929` | Anthropic Claude | 200K | ¥12.13 | ¥60.66 | $1.8 | $9 | 6 折 |
| 38 | [Claude Sonnet 4.6](../vendors/anthropic-claude.md#claude-sonnet-4-6) | `claude-sonnet-4-6` | Anthropic Claude | 1M | ¥12.13 | ¥60.66 | $1.8 | $9 | 6 折 |
| 39 | [Gemini 4 Argon-nx](../vendors/google-gemini-veo-nano-banana.md#gemini-4-argon-nx) | `gemini-4-argon-nx` | Google | 1M | ¥13.48 | ¥67.4 | $2 | $10 | — |
| 40 | [GPT-5.6 Terra-bd](../vendors/openai.md#gpt-5.6-terra-bd) | `gpt-5.6-terra-bd` | OpenAI | 1.05M | ¥13.48 | ¥80.88 | $2 | $12 | — |
| 41 | [GPT-6 Sol-bd](../vendors/openai.md#gpt-6-sol-bd) | `gpt-6-sol-bd` | OpenAI | 1.05M | ¥13.48 | ¥67.4 | $2 | $10 | — |
| 42 | [GPT-6.1 Sol-bd](../vendors/openai.md#gpt-6.1-sol-bd) | `gpt-6.1-sol-bd` | OpenAI | 1.05M | ¥13.48 | ¥67.4 | $2 | $10 | — |
| 43 | [Kimi K3 1013](../vendors/moonshot-kimi.md#kimi-k3-1013) | `kimi-k3-1013` | 月之暗面 Kimi | 256K | ¥15 | ¥75 | $2.226 | $11.13 | 7.5 折 |
| 44 | [Claude Opus 5.5](../vendors/anthropic-claude.md#claude-opus-5-5) | `claude-opus-5-5` | Anthropic Claude | 1M | ¥16.18 | ¥80.88 | $2.4 | $12 | 6 折 |
| 45 | [Kimi K3](../vendors/moonshot-kimi.md#kimi-k3) | `kimi-k3` | 月之暗面 Kimi | 256K | ¥20 | ¥100 | $2.967 | $14.84 | — |
| 46 | [Claude Opus 4.5](../vendors/anthropic-claude.md#claude-opus-4-5-20251101) | `claude-opus-4-5-20251101` | Anthropic Claude | 200K | ¥20.22 | ¥101.1 | $3 | $15 | 6 折 |
| 47 | [Claude Opus 4.6](../vendors/anthropic-claude.md#claude-opus-4-6) | `claude-opus-4-6` | Anthropic Claude | 1M | ¥20.22 | ¥101.1 | $3 | $15 | 6 折 |
| 48 | [Claude Opus 4.7](../vendors/anthropic-claude.md#claude-opus-4-7) | `claude-opus-4-7` | Anthropic Claude | 1M | ¥20.22 | ¥101.1 | $3 | $15 | 6 折 |
| 49 | [Claude Opus 4.8](../vendors/anthropic-claude.md#claude-opus-4-8) | `claude-opus-4-8` | Anthropic Claude | 1M | ¥20.22 | ¥101.1 | $3 | $15 | 6 折 |
| 50 | [Claude Opus 5](../vendors/anthropic-claude.md#claude-opus-5) | `claude-opus-5` | Anthropic Claude | 1M | ¥20.22 | ¥101.1 | $3 | $15 | 6 折 |
| 51 | [GPT-6](../vendors/openai.md#gpt-6) | `gpt-6` | OpenAI | 1.05M | ¥20.22 | ¥101.1 | $3 | $15 | 3 折 |
| 52 | [GPT-6 Astra](../vendors/openai.md#gpt-6-astra) | `gpt-6-astra` | OpenAI | 1.05M | ¥20.22 | ¥101.1 | $3 | $15 | 3 折 |
| 53 | [GPT-5.6 Sol-bd](../vendors/openai.md#gpt-5.6-sol-bd) | `gpt-5.6-sol-bd` | OpenAI | 1.05M | ¥26.96 | ¥134.8 | $4 | $20 | — |
| 54 | [Claude Fable 5](../vendors/anthropic-claude.md#claude-fable-5) | `claude-fable-5` | Anthropic Claude | 200K | ¥40.44 | ¥202.2 | $6 | $30 | 6 折 |
| 55 | [Claude Fable 5.1](../vendors/anthropic-claude.md#claude-fable-5-1) | `claude-fable-5-1` | Anthropic Claude | 1M | ¥40.44 | ¥202.2 | $6 | $30 | 6 折 |
| 56 | [GPT-6 Astra-bd](../vendors/openai.md#gpt-6-astra-bd) | `gpt-6-astra-bd` | OpenAI | 1.05M | ¥67.4 | ¥337 | $10 | $50 | — |

缓存命中的输入另有更低的价格，见各模型的厂商页。

## 能力对照

| 模型 | 读图 | 工具调用 | 联网搜索 | 思考 | JSON | 出图 | 开源权重 | 接口 |
|---|---|---|---|---|---|---|---|---|
| [Codex Auto Review](../vendors/openai.md#codex-auto-review) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | OpenAI / Responses |
| [GPT-5.6 Luna](../vendors/openai.md#gpt-5.6-luna) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | OpenAI / Responses |
| [GPT-5.6 Luna-bd](../vendors/openai.md#gpt-5.6-luna-bd) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses |
| [GPT-5.6 Sol](../vendors/openai.md#gpt-5.6-sol) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | OpenAI / Responses |
| [GPT-5.6 Sol-bd](../vendors/openai.md#gpt-5.6-sol-bd) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses |
| [GPT-5.6 Terra](../vendors/openai.md#gpt-5.6-terra) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | OpenAI / Responses |
| [GPT-5.6 Terra-bd](../vendors/openai.md#gpt-5.6-terra-bd) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses |
| [GPT-6](../vendors/openai.md#gpt-6) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | OpenAI / Responses |
| [GPT-6 Astra](../vendors/openai.md#gpt-6-astra) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | OpenAI / Responses |
| [GPT-6 Astra-bd](../vendors/openai.md#gpt-6-astra-bd) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses |
| [GPT-6 Luna](../vendors/openai.md#gpt-6-luna) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | OpenAI / Responses |
| [GPT-6 Luna-bd](../vendors/openai.md#gpt-6-luna-bd) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses |
| [GPT-6 Sol](../vendors/openai.md#gpt-6-sol) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | OpenAI / Responses |
| [GPT-6 Sol-bd](../vendors/openai.md#gpt-6-sol-bd) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses |
| [GPT-6.1 Sol](../vendors/openai.md#gpt-6.1-sol) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | OpenAI / Responses |
| [GPT-6.1 Sol-bd](../vendors/openai.md#gpt-6.1-sol-bd) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses |
| [GPT-6.1 Terra](../vendors/openai.md#gpt-6.1-terra) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | OpenAI / Responses |
| [Claude Fable 5](../vendors/anthropic-claude.md#claude-fable-5) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Anthropic |
| [Claude Fable 5.1](../vendors/anthropic-claude.md#claude-fable-5-1) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Anthropic |
| [Claude Haiku 4.5](../vendors/anthropic-claude.md#claude-haiku-4-5-20251001) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses / Anthropic |
| [Claude Haiku 5.5](../vendors/anthropic-claude.md#claude-haiku-5-5) | ✓ | ✓ | — | ✓ | ✓ | — | — | OpenAI / Anthropic |
| [Claude Opus 4.5](../vendors/anthropic-claude.md#claude-opus-4-5-20251101) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Anthropic |
| [Claude Opus 4.6](../vendors/anthropic-claude.md#claude-opus-4-6) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses / Anthropic |
| [Claude Opus 4.7](../vendors/anthropic-claude.md#claude-opus-4-7) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses / Anthropic |
| [Claude Opus 4.8](../vendors/anthropic-claude.md#claude-opus-4-8) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses / Anthropic |
| [Claude Opus 5](../vendors/anthropic-claude.md#claude-opus-5) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Anthropic |
| [Claude Opus 5.5](../vendors/anthropic-claude.md#claude-opus-5-5) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Anthropic |
| [Claude Sonnet 4.5](../vendors/anthropic-claude.md#claude-sonnet-4-5-20250929) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Anthropic |
| [Claude Sonnet 4.6](../vendors/anthropic-claude.md#claude-sonnet-4-6) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses / Anthropic |
| [Claude Sonnet 5](../vendors/anthropic-claude.md#claude-sonnet-5) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Responses / Anthropic |
| [Claude Sonnet 5.5](../vendors/anthropic-claude.md#claude-sonnet-5-5) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Anthropic |
| [Gemini 3.1 Pro](../vendors/google-gemini-veo-nano-banana.md#gemini-3.1-pro-low) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Gemini |
| [Gemini 3.1 Pro Preview 1020](../vendors/google-gemini-veo-nano-banana.md#gemini-3.1-pro-preview-1020) | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | OpenAI / Gemini |
| [Gemini 3.8 Flash](../vendors/google-gemini-veo-nano-banana.md#gemini-3.8-flash) | ✓ | ✓ | — | ✓ | ✓ | — | — | OpenAI / Gemini |
| [Gemini 3.8 Flash-nx](../vendors/google-gemini-veo-nano-banana.md#gemini-3.8-flash-nx) | ✓ | ✓ | — | ✓ | ✓ | — | — | OpenAI / Gemini |
| [Gemini 4 Argon](../vendors/google-gemini-veo-nano-banana.md#gemini-4-argon) | ✓ | ✓ | — | ✓ | ✓ | — | — | OpenAI / Gemini |
| [Gemini 4 Argon-nx](../vendors/google-gemini-veo-nano-banana.md#gemini-4-argon-nx) | ✓ | ✓ | — | ✓ | ✓ | — | — | OpenAI / Gemini |
| [DeepSeek V4 Flash](../vendors/deepseek.md#deepseek-v4-flash) | — | ✓ | — | ✓ | ✓ | — | — | OpenAI |
| [DeepSeek V4 Pro](../vendors/deepseek.md#deepseek-v4-pro) | — | ✓ | — | ✓ | ✓ | — | — | OpenAI |
| [DeepSeek V4.1 Flash](../vendors/deepseek.md#deepseek-v4.1-flash) | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | OpenAI |
| [Kimi K2.5](../vendors/moonshot-kimi.md#kimi-k2.5) | — | ✓ | — | ✓ | ✓ | — | ✓ | OpenAI |
| [Kimi K2.6](../vendors/moonshot-kimi.md#kimi-k2.6) | — | ✓ | — | ✓ | ✓ | — | ✓ | OpenAI |
| [Kimi K2.7 Code](../vendors/moonshot-kimi.md#kimi-k2.7-code) | — | ✓ | — | ✓ | ✓ | — | ✓ | OpenAI |
| [Kimi K3](../vendors/moonshot-kimi.md#kimi-k3) | — | ✓ | — | ✓ | ✓ | — | ✓ | OpenAI / Anthropic |
| [Kimi K3 1013](../vendors/moonshot-kimi.md#kimi-k3-1013) | — | ✓ | — | ✓ | ✓ | — | ✓ | OpenAI / Anthropic |
| [GLM-5.3](../vendors/zhipu-glm.md#glm-5.3) | — | ✓ | — | ✓ | ✓ | — | ✓ | OpenAI |
| [GLM-5.3-1022](../vendors/zhipu-glm.md#glm-5.3-1022) | — | ✓ | — | ✓ | ✓ | — | ✓ | OpenAI / Responses / Anthropic |
| [GLM-5.3-Flash](../vendors/zhipu-glm.md#glm-5.3-flash) | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | OpenAI |
| [GLM-5.3-Flash-1022](../vendors/zhipu-glm.md#glm-5.3-flash-1022) | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | OpenAI / Responses / Anthropic |
| [Qwen3.8-Max-cjx](../vendors/alibaba-qwen-wan.md#qwen3.8-max-cjx) | ✓ | ✓ | — | ✓ | ✓ | — | — | OpenAI / Responses |
| [Qwen3.8-Omni-Flash](../vendors/alibaba-qwen-wan.md#qwen3.8-omni-flash) | ✓ | ✓ | — | ✓ | ✓ | — | — | OpenAI |
| [Grok 4.5](../vendors/xai-grok.md#grok-4.5) | ✓ | ✓ | — | ✓ | ✓ | — | — | OpenAI / Responses |
| [Grok 4.6](../vendors/xai-grok.md#grok-4.6) | ✓ | ✓ | — | ✓ | ✓ | — | — | OpenAI / Responses |
| [Grok 4.7](../vendors/xai-grok.md#grok-4.7) | ✓ | ✓ | — | ✓ | ✓ | — | — | OpenAI / Responses |
| [MiniMax M2.7](../vendors/minimax-hailuo.md#MiniMax-M2.7) | — | ✓ | — | — | ✓ | — | — | OpenAI |
| [xiaozhanAI](../vendors/xiaozhan-platform.md#xiaozhanAI) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | OpenAI / Responses |

「接口」列：OpenAI = `/v1/chat/completions`，Responses = `/v1/responses`，Anthropic = `/v1/messages`，Gemini = `/v1beta/models/{id}:generateContent`。

## 怎么调用

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

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

```bash
curl https://api.dflop.top/v1/chat/completions \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-6-luna", "messages": [{"role": "user", "content": "你好"}]}'
```

Claude 也可以用 Anthropic SDK（`base_url` 不带 `/v1`）：

```python
import os
from anthropic import Anthropic

client = Anthropic(base_url="https://api.dflop.top", api_key=os.environ["PLATFORM_API_KEY"])  # 不带 /v1

msg = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "你好"}],
)
print(msg.content[0].text)
```

Gemini 也可以用 Google Gen AI SDK：

```python
import os
from google import genai

client = genai.Client(
    api_key=os.environ["PLATFORM_API_KEY"],
    http_options={"base_url": "https://api.dflop.top", "api_version": "v1beta"},
)
resp = client.models.generate_content(model="gemini-3.8-flash", contents="你好")
print(resp.text)
```

## 常见问题

**哪个对话模型最便宜？** 按输入价，这份目录里最便宜的三个：[GPT-6 Luna](../vendors/openai.md#gpt-6-luna)，输入 ¥0.2022、输出 ¥1.011 / 百万 token；[Claude Haiku 5.5](../vendors/anthropic-claude.md#claude-haiku-5-5)，输入 ¥0.4044、输出 ¥2.022 / 百万 token；[Codex Auto Review](../vendors/openai.md#codex-auto-review)，输入 ¥0.4044、输出 ¥2.426 / 百万 token。

**哪个模型上下文最长？** [Gemini 3.1 Pro](../vendors/google-gemini-veo-nano-banana.md#gemini-3.1-pro-low)，2M token；1M 及以上的共 41 个。

**能用 Anthropic SDK 或 Gemini SDK 调用吗？** 能。Anthropic Messages 接口可调 18 个模型，Gemini 原生接口可调 6 个，OpenAI Responses 接口 30 个，OpenAI Chat Completions 接口全部 56 个。逐个模型见上面的「能力对照」，说明见 [兼容矩阵](https://model.dflop.top/docs/reference/compatibility-matrix)。

**价格多久更新？** 每天同步一次，实时价格见模型页。

## English

API prices of all 56 chat models on [XiaoZhan AIhub](https://model.dflop.top/en/models), sorted by input price per million tokens, with the price charged now (promotions included) in CNY and USD. Every model is reachable through the OpenAI-compatible endpoint `https://api.dflop.top/v1/chat/completions`; 18 also through the Anthropic Messages API and 6 through the Gemini API. The cheapest by input price: GPT-6 Luna, Claude Haiku 5.5 and Codex Auto Review. Longest context: Gemini 3.1 Pro (2M tokens).

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
