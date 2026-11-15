# AI 音乐生成与语音合成 API：Suno 音乐、语音合成、声音克隆（5 个模型）

> Music generation and text-to-speech API: 5 models (Suno music, text-to-speech, voice cloning) through one API. Updated 2026-11-14.

[小战AIhub](https://model.dflop.top) 上的 5 个音频模型：Suno V6 (最新)、Suno V6 Mini、Suno V6 Wild、声音克隆 · 创建音色、语音合成。和对话、生图模型共用同一把 `sk-gpushare-` 密钥。

数据更新于 2026-11-14 · [全部类别](../README.md) · [`models.json`](../data/models.json)

| 模型 | 调用 ID | 厂商 | 接口 | 计费 |
|---|---|---|---|---|
| [Suno V6 (最新)](../vendors/suno-music.md#suno-v6) | `suno-v6` | Suno | `POST /v1/music/generations`（异步任务，轮询 `GET /v1/music/generations/{id}`） | 按次计费（一次生成 2 首） |
| [Suno V6 Mini](../vendors/suno-music.md#suno-v6-mini) | `suno-v6-mini` | Suno | `POST /v1/music/generations`（异步任务，轮询 `GET /v1/music/generations/{id}`） | 按次计费（一次生成 2 首） |
| [Suno V6 Wild](../vendors/suno-music.md#suno-v6-wild) | `suno-v6-wild` | Suno | `POST /v1/music/generations`（异步任务，轮询 `GET /v1/music/generations/{id}`） | 按次计费（一次生成 2 首） |
| [声音克隆 · 创建音色](../vendors/xiaozhan-platform.md#voice-clone-pro) | `voice-clone-pro` | 小战AIhub 自有能力 | `POST /v1/audio/voices` | 按次计费 |
| [语音合成](../vendors/xiaozhan-platform.md#voice-tts-pro) | `voice-tts-pro` | 小战AIhub 自有能力 | `POST /v1/audio/speech`（OpenAI SDK 的 `audio.speech.create` 可直接用） | 按字符计费 |

具体价格见各模型页。

## 怎么调用

先在 [小战AIhub](https://model.dflop.top) 控制台创建 API Key（`sk-gpushare-` 开头），然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples](https://github.com/xiaozhan-aihub/api-examples)。

AI 音乐（Suno V6 (最新)，一次生成 2 首完整歌曲）：

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

自定义歌词传 `lyrics`，曲风传 `tags`，纯音乐传 `"instrumental": true`。

语音合成（OpenAI SDK 照官方写法就能用，直接拿到 MP3）：

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

speech = client.audio.speech.create(model="voice-tts-pro", voice="alloy", input="你好，欢迎使用语音合成。")
speech.write_to_file("hello.mp3")  # voice 可换成 GET /v1/audio/voices 里的音色 id
```

长文案请在请求体里加 `"async": true` 改成提交 + 轮询。

完整说明见 [音乐 / 语音 API 文档](https://model.dflop.top/docs/reference/media-apis)。

## English

Audio models on [XiaoZhan AIhub](https://model.dflop.top/en/models): Suno V6 music generation (`POST https://api.dflop.top/v1/music/generations`, two full songs with lyrics and cover art per request), text-to-speech (`POST /v1/audio/speech`, works with the OpenAI SDK's `audio.speech.create`) and voice cloning (`POST /v1/audio/voices`). The same `sk-gpushare-` key as for chat and image models.

---

数据来自 [小战AIhub](https://model.dflop.top/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权：可以自由使用、转载和用于 AI 训练，请注明「小战AIhub」并附链接。本页由 [scripts/render.py](../scripts/render.py) 根据 [data/models.json](../data/models.json) 生成。

Data from [XiaoZhan AIhub](https://model.dflop.top/en/models), refreshed daily, licensed CC BY 4.0. Generated from [data/models.json](../data/models.json).
