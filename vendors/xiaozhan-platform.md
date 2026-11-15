# 小战AIhub自有模型与能力：xiaozhanAI、数字人、智能剪辑、语音合成、声音克隆

> XiaoZhan AIhub platform services API pricing on XiaoZhan AIhub: 7 models (xiaozhanAI, digital humans, smart clip editing, text-to-speech and voice cloning). Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上可调用的 小战AIhub 自有能力 模型共 7 个（对话大模型 1 个，图像生成 1 个，视频生成 3 个，音乐与语音 2 个），一把 `sk-gpushare-` 密钥全都能调：对话模型用 OpenAI SDK 改个 `base_url` 即可，生图走 OpenAI Images 接口，视频是提交任务再轮询结果，音乐和语音各有专门的接口。下面是每个模型的价格、参数和接口。

平台按积分计费，60 积分 = ¥1，约 404.4 积分 = $1；表里的 ¥ / $ 是按这个比例换算的参考价。

数据更新于 2026-11-14 · [全部厂商](../README.md) · [大模型 API 价格对比](../pricing/llm-api.md) · [AI 生图 API 价格对比](../pricing/image-generation-api.md) · [AI 视频生成 API 价格对比](../pricing/video-generation-api.md) · [AI 音乐生成与语音合成 API](../pricing/music-and-speech-api.md)

## 模型一览

| 模型 | 调用 ID | 类别 | 现价 | 上下文 | 折扣 |
|---|---|---|---|---|---|
| [xiaozhanAI](#xiaozhanAI) | `xiaozhanAI` | 对话大模型 | 输入 ¥2.022 / 输出 ¥10.11 每百万 token | 1.05M | — |
| [xiaozhanimage](#xiaozhanimage) | `xiaozhanimage` | 图像生成 | ¥0.5 / 张 | — | — |
| [创建数字人形象](#dh-avatar-create) | `dh-avatar-create` | 视频生成 | 价格见模型页 | — | — |
| [数字人视频](#dh-avatar) | `dh-avatar` | 视频生成 | ¥0.06 / 秒 | — | — |
| [智能剪辑](#clip-compose) | `clip-compose` | 视频生成 | ¥1.5 / 次 | — | — |
| [声音克隆 · 创建音色](#voice-clone-pro) | `voice-clone-pro` | 音乐与语音 | 按次计费 | — | — |
| [语音合成](#voice-tts-pro) | `voice-tts-pro` | 音乐与语音 | 按字符计费 | — | — |

## 各模型详情

<a id="xiaozhanAI"></a>

### xiaozhanAI

调用 ID `xiaozhanAI` · 对话大模型 · 上架 2026-10-11

xiaozhanAI 旗舰对话模型,1.05M 上下文,OpenAI 官方 API 直连,默认走官方 Fast 加速档。支持联网搜索、生成图片、工具调用与读图,推理强度可调,超长 prompt 另有分档价;还能用云沙箱写代码生成 Word / Excel / PPT / PDF 文件 —— 本站 AI 对话里直接用,API 用 /v1/responses 的 shell / code_interpreter 工具 + /v1/containers 取文件。

| 计价项 | 价格 |
|---|---|
| 输入 · 每百万 token | 121.32 积分 ≈ ¥2.022 ≈ $0.3 |
| 输出 · 每百万 token | 606.6 积分 ≈ ¥10.11 ≈ $1.5 |
| 缓存命中输入 · 每百万 token | 12.13 积分 ≈ ¥0.2022 ≈ $0.03 |
| 出图 · 每张 | 170.66 积分 ≈ ¥2.844 ≈ $0.422 |

- 上下文 1.05M token，最大输出 128K token
- 能力：读图、工具调用、思考模式（推理强度 low / medium / high / xhigh / max）、联网搜索、JSON 模式、出图
- 接口：OpenAI Chat Completions `POST /v1/chat/completions` · OpenAI Responses `POST /v1/responses`
- 模型页：[model.dflop.top/models/xiaozhanAI](https://model.dflop.top/models/xiaozhanAI) · [English](https://model.dflop.top/en/models/xiaozhanAI) · [Markdown](https://model.dflop.top/models/xiaozhanAI.md)

> xiaozhanAI flagship chat model. 1.05M context, connected directly to the official OpenAI API, on the official Fast tier by default. Web search, image generation, tool calling and image input, with adjustable reasoning effort; very long prompts are priced in a separate tier. It can also write code in a cloud sandbox to produce Word, Excel, PowerPoint and PDF files: use it directly in AI Chat on this site, or over the API with the shell / code_interpreter tools of /v1/responses and /v1/containers to fetch the files.

<a id="xiaozhanimage"></a>

### xiaozhanimage

调用 ID `xiaozhanimage` · 图像生成 · 上架 2026-10-12

xiaozhanimage 图片模型,OpenAI 官方 API 直连。文生图 / 参考图改图 / 局部重绘,按张计费,每张固定价。

| 计价项 | 价格 |
|---|---|
| 出图 · 每张 | 30 积分 ≈ ¥0.5 ≈ $0.07418 |

- 尺寸：尺寸档 1K / 2K / 4K，默认 `1024x1024`
- 比例：1:1 / 2:3 / 3:2 / 9:16 / 16:9 / 3:4 / 4:3 / 自动
- 图生图最多 9 张参考图
- 接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）
- 模型页：[model.dflop.top/models/xiaozhanimage](https://model.dflop.top/models/xiaozhanimage) · [English](https://model.dflop.top/en/models/xiaozhanimage) · [Markdown](https://model.dflop.top/models/xiaozhanimage.md)

> xiaozhanimage image model, connected directly to the official OpenAI API. Text-to-image, reference-image editing and inpainting, billed per image at a fixed price.

<a id="dh-avatar-create"></a>

### 创建数字人形象

调用 ID `dh-avatar-create` · 视频生成 · 上架 2026-07-24

创建数字人形象:上传一张照片或一段视频 → 克隆出可复用的专属数字人形象(异步任务),之后可反复驱动出片。

计费：价格见模型页。

- 上传一张照片或一段视频，创建可反复使用的数字人形象
- 接口：`POST /v1/videos/avatars`，用法见[数字人 / 剪辑 API](https://model.dflop.top/docs/reference/digital-human-apis)
- 模型页：[model.dflop.top/models/dh-avatar-create](https://model.dflop.top/models/dh-avatar-create) · [English](https://model.dflop.top/en/models/dh-avatar-create) · [Markdown](https://model.dflop.top/models/dh-avatar-create.md)

> Create a digital-human avatar: upload a photo or a video to clone a reusable avatar of your own (asynchronous task), then drive it again and again.

<a id="dh-avatar"></a>

### 数字人视频

调用 ID `dh-avatar` · 视频生成 · 上架 2026-07-24

数字人视频:选一个数字人形象 + 一段驱动音频(或文字驱动)→ 开口说话的数字人视频(异步任务)。按视频时长计费。

| 计价项 | 价格 |
|---|---|
| 视频 · 每秒 | 3.6 积分 ≈ ¥0.06 ≈ $0.008902 |

- 数字人形象 + 驱动音频（或文字 + 音色）→ 开口说话的视频
- 接口：`POST /v1/videos/generations`（异步任务），用法见[数字人 / 剪辑 API](https://model.dflop.top/docs/reference/digital-human-apis)
- 模型页：[model.dflop.top/models/dh-avatar](https://model.dflop.top/models/dh-avatar) · [English](https://model.dflop.top/en/models/dh-avatar) · [Markdown](https://model.dflop.top/models/dh-avatar.md)

> Digital-human video: pick a digital-human avatar and a driving audio clip (or text) to get a talking avatar video (asynchronous task). Billed by video length.

<a id="clip-compose"></a>

### 智能剪辑

调用 ID `clip-compose` · 视频生成 · 上架 2026-09-25

智能剪辑:口播视频 + 可编辑字幕 + 模板 / 背景音乐 / 标题 / 名片 / 画中画 → 包装好的成片(异步任务)。按次计费。

| 计价项 | 价格 |
|---|---|
| 任务 · 每次 | 90 积分 ≈ ¥1.5 ≈ $0.2226 |

- 口播视频 → 带字幕特效、标题、模板、背景音乐的成片
- 接口：`POST /v1/videos/generations`（异步任务），用法见[数字人 / 剪辑 API](https://model.dflop.top/docs/reference/digital-human-apis)
- 模型页：[model.dflop.top/models/clip-compose](https://model.dflop.top/models/clip-compose) · [English](https://model.dflop.top/en/models/clip-compose) · [Markdown](https://model.dflop.top/models/clip-compose.md)

> Smart editing: a talking-head video with editable subtitles plus a template, background music, title, name card and picture-in-picture gives a packaged finished video (asynchronous task). Billed per job.

<a id="voice-clone-pro"></a>

### 声音克隆 · 创建音色

调用 ID `voice-clone-pro` · 音乐与语音 · 上架 2026-07-24

声音克隆:上传/录制一段本人(或已授权)语音,克隆出可复用的专属音色,用于语音合成与数字人配音。

计费：按次计费，价格见模型页。

- 上传一段本人（或已获授权）的语音，克隆出可复用的音色，用于语音合成和数字人配音
- 接口：`POST /v1/audio/voices`
- 模型页：[model.dflop.top/models/voice-clone-pro](https://model.dflop.top/models/voice-clone-pro) · [English](https://model.dflop.top/en/models/voice-clone-pro) · [Markdown](https://model.dflop.top/models/voice-clone-pro.md)

> Voice cloning: upload or record your own (or an authorised) voice to clone a reusable voice of your own for speech synthesis and avatar voice-overs.

<a id="voice-tts-pro"></a>

### 语音合成

调用 ID `voice-tts-pro` · 音乐与语音 · 上架 2026-07-24

语音合成:输入文字,用平台公共音色或已克隆的专属音色朗读,生成可下载音频(MP3),自动进入「我的配音」历史。

计费：按字符计费，价格见模型页。

- 文本转语音（MP3），可用平台公共音色或自己克隆的音色
- 接口：`POST /v1/audio/speech`（OpenAI SDK 的 `audio.speech.create` 可直接用）
- 模型页：[model.dflop.top/models/voice-tts-pro](https://model.dflop.top/models/voice-tts-pro) · [English](https://model.dflop.top/en/models/voice-tts-pro) · [Markdown](https://model.dflop.top/models/voice-tts-pro.md)

> Speech synthesis: read text aloud with the platform's public voices or a voice you cloned, producing downloadable audio (MP3) that is saved to My Voice-overs.

## 调用示例

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

对话（xiaozhanAI）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="xiaozhanAI",
    messages=[{"role": "user", "content": "用三句话介绍一下你自己"}],
)
print(resp.choices[0].message.content)
```

生图（xiaozhanimage）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"], timeout=300)

result = client.images.generate(
    model="xiaozhanimage",
    prompt="一只在竹林里喝茶的熊猫，水彩风格",
    size="1024x1024",
)
print(result.data[0].url)  # 临时链接（约 24 小时），请转存
```

视频（创建数字人形象）：

```python
import os, time, uuid
import requests

BASE = "https://api.dflop.top/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"}

r = requests.post(
    f"{BASE}/videos/generations",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},  # 重试用同一把键，不会重复扣费
    json={
        "model": "dh-avatar-create",
        "content": [{"type": "text", "text": "海边日落，无人机航拍视角"}],
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

语音合成（语音合成）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

speech = client.audio.speech.create(model="voice-tts-pro", voice="alloy", input="你好，欢迎使用语音合成。")
speech.write_to_file("hello.mp3")  # voice 可换成 GET /v1/audio/voices 里的音色 id
```

## English

7 XiaoZhan AIhub platform services models are available through [XiaoZhan AIhub](https://model.dflop.top/en/models) (xiaozhanAI, digital humans, smart clip editing, text-to-speech and voice cloning). Each section above lists the call id, the price charged now in platform credits, CNY and USD, and the supported endpoints. One `sk-gpushare-` key covers them all: chat models through the OpenAI SDK at `https://api.dflop.top/v1`; image models through the OpenAI Images API (`/v1/images/generations`); video models as asynchronous tasks (`/v1/videos/generations`); music and speech through `/v1/music/generations` and `/v1/audio/speech`.

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
