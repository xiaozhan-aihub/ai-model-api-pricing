#!/usr/bin/env python3
"""Render this repository's pages from the open data (run by the daily sync workflow).

    python3 scripts/render.py --catalog /tmp/catalog.json

Reads data/models.json (the open data, CC BY 4.0) and the platform's public model
catalogue (https://api.dflop.top/api/v1/models/public: descriptions, supported
protocols, image and video parameters), and writes:

    README.md                      every model with its price, by category
    pricing/*.md                   one comparison page per category
    vendors/*.md                   one page per vendor, a section per model
    build/hf/README.md             the Hugging Face dataset card (not committed)

The output depends only on the data, so a day without changes makes no commit.
Edit the wording here, not in the generated files.
"""

import argparse
import json
import math
import os
import re
import sys

SITE = "https://model.dflop.top"
API = "https://api.dflop.top"
GH_ORG = "https://github.com/xiaozhan-aihub"
REPO = "ai-model-api-pricing"
GH_REPO = f"{GH_ORG}/{REPO}"
GH_BLOB = f"{GH_REPO}/blob/main"
GH_EXAMPLES = f"{GH_ORG}/api-examples"
HF_ID = f"xiaozhan-aihub/{REPO}"
HF_URL = f"https://huggingface.co/datasets/{HF_ID}"
BRAND = "小战AIhub"
BRAND_EN = "XiaoZhan AIhub"
DOCS = f"{SITE}/docs"
DOCS_EN = f"{SITE}/en/docs"

# Words that must never reach these public pages. A catalogue description containing
# one is dropped (the rest of the model's section still renders).
BANNED = ["百度", "baidu", "文心", "千帆", "翻墙", "科学上网", "免翻", "国内直连", "国内可用", "国内访问"]

CATS = {
    "text": {
        "zh": "对话大模型", "en": "Chat models (LLM)", "file": "pricing/llm-api.md",
        "title": "大模型 API 价格对比", "title_en": "LLM API pricing comparison",
    },
    "image": {
        "zh": "图像生成", "en": "Image generation", "file": "pricing/image-generation-api.md",
        "title": "AI 生图 API 价格对比", "title_en": "Image generation API pricing comparison",
    },
    "video": {
        "zh": "视频生成", "en": "Video generation", "file": "pricing/video-generation-api.md",
        "title": "AI 视频生成 API 价格对比", "title_en": "Video generation API pricing comparison",
    },
    "audio": {
        "zh": "音乐与语音", "en": "Music and speech", "file": "pricing/music-and-speech-api.md",
        "title": "AI 音乐生成与语音合成 API", "title_en": "Music generation and text-to-speech API",
    },
}

# key, Chinese name, English name, page slug, what it makes (zh), what it makes (en)
VENDORS = [
    ("openai", "OpenAI", "OpenAI", "openai", "GPT 对话模型、GPT-Image 生图", "GPT chat models and GPT-Image"),
    ("anthropic", "Anthropic Claude", "Anthropic Claude", "anthropic-claude", "Claude Opus、Sonnet、Haiku", "Claude Opus, Sonnet and Haiku"),
    ("google", "Google", "Google", "google-gemini-veo-nano-banana", "Gemini 对话、Nano Banana 生图、Veo 视频", "Gemini, Nano Banana image and Veo video"),
    ("deepseek", "DeepSeek 深度求索", "DeepSeek", "deepseek", "DeepSeek V4 系列", "the DeepSeek V4 series"),
    ("moonshot", "月之暗面 Kimi", "Moonshot AI (Kimi)", "moonshot-kimi", "Kimi K2、K3", "Kimi K2 and K3"),
    ("zhipu", "智谱 GLM", "Zhipu AI (GLM)", "zhipu-glm", "GLM-5.3 系列", "the GLM-5.3 series"),
    ("alibaba", "阿里巴巴 通义", "Alibaba (Qwen, Wan)", "alibaba-qwen-wan", "通义千问 Qwen、Qwen Image、通义万相 Wan 视频、快乐马视频", "Qwen, Qwen Image, Wan video and HappyHorse video"),
    ("xai", "xAI Grok", "xAI (Grok)", "xai-grok", "Grok 对话、Grok Imagine 图像与视频", "Grok chat and Grok Imagine image and video"),
    ("minimax", "MiniMax 海螺", "MiniMax (Hailuo)", "minimax-hailuo", "MiniMax 对话、海螺 H3 视频", "MiniMax chat and Hailuo H3 video"),
    ("bytedance", "字节跳动 豆包", "ByteDance (Doubao)", "bytedance-seedance-seedream", "Seedance 视频、Seedream 生图", "Seedance video and Seedream image"),
    ("kuaishou", "快手 可灵", "Kuaishou (Kling)", "kuaishou-kling", "可灵 Kling 视频与图像", "Kling video and image"),
    ("shengshu", "生数科技 Vidu", "ShengShu (Vidu)", "shengshu-vidu", "Vidu Q3 视频", "Vidu Q3 video"),
    ("suno", "Suno", "Suno", "suno-music", "Suno V6 AI 音乐", "Suno V6 music"),
    ("other", "小战AIhub 自有能力", "XiaoZhan AIhub platform services", "xiaozhan-platform", "xiaozhanAI、数字人、智能剪辑、语音合成、声音克隆", "xiaozhanAI, digital humans, smart clip editing, text-to-speech and voice cloning"),
]
VENDOR = {v[0]: v for v in VENDORS}
SITE_VENDOR_PAGES = {v[0] for v in VENDORS} - {"other"}

# Models used in the code examples, first one present wins.
REPS = {
    "text": ["gpt-6-luna", "claude-sonnet-5", "gemini-3.8-flash", "deepseek-v4.1-flash", "kimi-k3", "glm-5.3",
             "qwen3.8-omni-flash", "grok-4.7", "MiniMax-M2.7", "xiaozhanAI"],
    "image": ["gpt-image-2", "doubao-seedream-5-0-260128", "nano-banana-pro", "qwen-image-3.0", "tvod-kling-image-3.0",
              "grok-imagine-image", "xiaozhanimage"],
    "video": ["doubao-seedance-2.0", "tvod-veo-3.1-fast", "tvod-kling-video-3.0", "tvod-vidu-video-q3", "minimax-h3",
              "wan3.0-video", "grok-imagine-video"],
    "audio": ["suno-v6", "voice-tts-pro"],
}

CAPS_ZH = {
    "Image input": "读图", "Video input": "读视频", "Tool calling": "工具调用", "Thinking mode": "思考模式",
    "Web search": "联网搜索", "JSON mode": "JSON 模式", "Image generation": "出图", "Open weights": "开源权重",
    "Prefix completion": "前缀续写",
}
PROTO = {
    "openai_chat": ("OpenAI Chat Completions", "POST /v1/chat/completions"),
    "openai_responses": ("OpenAI Responses", "POST /v1/responses"),
    "anthropic_messages": ("Anthropic Messages", "POST /v1/messages"),
    "gemini_native": ("Gemini generateContent", "POST /v1beta/models/{id}:generateContent"),
}
PROTO_ORDER = ["openai_chat", "openai_responses", "anthropic_messages", "gemini_native"]
MODES_ZH = {"t2v": "文生视频", "i2v": "图生视频", "flf": "首尾帧", "r2v": "参考图/视频生视频"}
MODES_EN = {"t2v": "text-to-video", "i2v": "image-to-video", "flf": "first and last frame", "r2v": "reference-to-video"}
PRICE_KEYS = {
    # key: (zh label, en label, zh unit, en unit)
    "input_per_1m_tokens": ("输入", "Input", "百万 token", "1M tokens"),
    "output_per_1m_tokens": ("输出", "Output", "百万 token", "1M tokens"),
    "cached_input_per_1m_tokens": ("缓存命中输入", "Cached input", "百万 token", "1M tokens"),
    "per_image": ("出图", "Image", "张", "image"),
    "per_video_second": ("视频", "Video", "秒", "second"),
    "per_video_task": ("任务", "Task", "次", "task"),
}
FAMILY_DOCS = f"{DOCS}/reference/digital-human-apis"
HOW_ZH = {
    "text": "对话模型用 OpenAI SDK 改个 `base_url` 即可",
    "image": "生图走 OpenAI Images 接口",
    "video": "视频是提交任务再轮询结果",
    "audio": "音乐和语音各有专门的接口",
}
HOW_EN = {
    "text": "chat models through the OpenAI SDK at `https://api.dflop.top/v1`",
    "image": "image models through the OpenAI Images API (`/v1/images/generations`)",
    "video": "video models as asynchronous tasks (`/v1/videos/generations`)",
    "audio": "music and speech through `/v1/music/generations` and `/v1/audio/speech`",
}


# ---------------------------------------------------------------- formatting


def fnum(v):
    """Short, stable number: 33.7, 8.088, 0.4044, 0.04044."""
    if v is None:
        return None
    if v == 0:
        return "0"
    if v >= 10:
        s = f"{v:.2f}"
    elif v >= 1:
        s = f"{v:.3f}"
    else:
        s = f"{v:.{max(0, 3 - int(math.floor(math.log10(abs(v)))))}f}"
    return s.rstrip("0").rstrip(".") if "." in s else s


def cny(p):
    return f"¥{fnum(p['cny'])}" if p and p.get("cny") is not None else "—"


def usd(p):
    return f"${fnum(p['usd'])}" if p and p.get("usd") is not None else "—"


def triple(p):
    if not p:
        return "—"
    parts = []
    if p.get("credits") is not None:
        parts.append(f"{fnum(p['credits'])} 积分")
    if p.get("cny") is not None:
        parts.append(f"¥{fnum(p['cny'])}")
    if p.get("usd") is not None:
        parts.append(f"${fnum(p['usd'])}")
    return " ≈ ".join(parts) if parts else "—"


def ctx(n):
    if not n:
        return "—"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.2f}".rstrip("0").rstrip(".") + "M"
    if n % 1000 == 0:
        return f"{n // 1000}K"
    if n % 1024 == 0:
        return f"{n // 1024}K"
    return f"{n / 1000:.1f}".rstrip("0").rstrip(".") + "K"


def off_zh(pf):
    return f"{pf * 10:g} 折" if pf else ""


def off_en(pf):
    return f"{round((1 - pf) * 100)}% off" if pf else ""


def cell(v):
    return str(v if v not in (None, "") else "—").replace("|", "\\|").replace("\n", " ")


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def natkey(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


def clean(text):
    if not text:
        return ""
    t = " ".join(str(text).split())
    low = t.lower()
    return "" if any(w.lower() in low for w in BANNED) else t


def join_zh(items):
    return "、".join(items)


def join_en(items):
    items = list(items)
    if len(items) <= 1:
        return "".join(items)
    return ", ".join(items[:-1]) + " and " + items[-1]


# ---------------------------------------------------------------- data


class Catalog:
    def __init__(self, data, catalog):
        self.doc = data
        self.models = data["models"]
        cat = catalog.get("models") if isinstance(catalog, dict) else catalog
        self.cat = {m["id"]: m for m in (cat or []) if isinstance(m, dict) and m.get("id")}
        self.by_id = {m["id"]: m for m in self.models}
        cur = data.get("currency") or {}
        self.per_cny = cur.get("credits_per_cny")
        self.per_usd = cur.get("credits_per_usd")
        self.updated = (data.get("updated_at") or "")[:10]

    def c(self, m):
        return self.cat.get(m["id"]) or {}

    def caps(self, m, kind):
        return ((self.c(m).get("caps") or {}).get(kind)) or {}

    def desc(self, m, lang="zh"):
        c = self.c(m)
        if lang == "en":
            return clean(((c.get("description_i18n") or {}).get("en")) or "")
        return clean(c.get("description") or "")

    def in_cat(self, cat):
        return [m for m in self.models if m.get("category") == cat]

    def vendors(self):
        present = {m.get("vendor") or "other" for m in self.models}
        known = [v[0] for v in VENDORS if v[0] in present]
        return known + sorted(present - set(known))

    def of_vendor(self, key):
        return sorted((m for m in self.models if (m.get("vendor") or "other") == key), key=order_key)

    def rep(self, cat, pool=None):
        pool = pool if pool is not None else self.in_cat(cat)
        ids = {m["id"] for m in pool}
        for mid in REPS.get(cat, []):
            if mid in ids:
                return self.by_id[mid]
        for m in sorted(pool, key=order_key):
            if cat == "video":
                v = self.caps(m, "video")
                if v.get("family") not in (None, "generic") or "ref_image" in (v.get("requires") or []):
                    continue
            return m
        return None


CAT_ORDER = {k: i for i, k in enumerate(["text", "image", "video", "audio"])}
VENDOR_ORDER = {v[0]: i for i, v in enumerate(VENDORS)}


def order_key(m):
    return (CAT_ORDER.get(m.get("category"), 9), natkey(m.get("name") or m["id"]), m["id"])


def table_key(m):
    """Tables: by vendor (the order of VENDORS), then by name."""
    return (VENDOR_ORDER.get(m.get("vendor") or "other", 99), m.get("vendor") or "", natkey(m.get("name") or m["id"]), m["id"])


def top3_zh(items):
    return "：" + "；".join(items) + "。"


def vinfo(key):
    v = VENDOR.get(key)
    if v:
        return {"key": key, "zh": v[1], "en": v[2], "slug": v[3], "what": v[4], "what_en": v[5]}
    return {"key": key, "zh": key, "en": key, "slug": key, "what": "", "what_en": ""}


def vendor_link(key, base=""):
    v = vinfo(key)
    return f"[{v['zh']}]({base}vendors/{v['slug']}.md)"


def model_link(m, base=""):
    v = vinfo(m.get("vendor") or "other")
    return f"[{m['name']}]({base}vendors/{v['slug']}.md#{m['id']})"


def price(m, key, which="price"):
    return ((m.get(which) or {}).get(key)) or None


def en_url(m):
    u = m.get("url") or ""
    return u.replace(SITE + "/", SITE + "/en/", 1) if u.startswith(SITE + "/") else u


# ---------------------------------------------------------------- code samples


def code(lang, body):
    return f"```{lang}\n{body.strip()}\n```"


def py_chat(mid):
    return code("python", f'''
import os
from openai import OpenAI

client = OpenAI(base_url="{API}/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="{mid}",
    messages=[{{"role": "user", "content": "用三句话介绍一下你自己"}}],
)
print(resp.choices[0].message.content)
''')


def curl_chat(mid):
    return code("bash", f'''
curl {API}/v1/chat/completions \\
  -H "Authorization: Bearer $PLATFORM_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{{"model": "{mid}", "messages": [{{"role": "user", "content": "你好"}}]}}'
''')


def py_anthropic(mid):
    return code("python", f'''
import os
from anthropic import Anthropic

client = Anthropic(base_url="{API}", api_key=os.environ["PLATFORM_API_KEY"])  # 不带 /v1

msg = client.messages.create(
    model="{mid}",
    max_tokens=1024,
    messages=[{{"role": "user", "content": "你好"}}],
)
print(msg.content[0].text)
''')


def py_gemini(mid):
    return code("python", f'''
import os
from google import genai

client = genai.Client(
    api_key=os.environ["PLATFORM_API_KEY"],
    http_options={{"base_url": "{API}", "api_version": "v1beta"}},
)
resp = client.models.generate_content(model="{mid}", contents="你好")
print(resp.text)
''')


def image_args(cat, m):
    img = cat.caps(m, "image")
    size = img.get("size") or {}
    prompt = "一只在竹林里喝茶的熊猫，水彩风格"
    if size.get("mode") == "prompt_ratio":
        return prompt + "，画面比例 1:1", None
    if size.get("default_size"):
        return prompt, size["default_size"]
    if (size.get("min_pixels") or 0) > 1024 * 1024:
        return prompt, "2048x2048"
    return prompt, "1024x1024"


def py_image(cat, m):
    prompt, size = image_args(cat, m)
    size_line = f'\n    size="{size}",' if size else ""
    note = "  # 这个模型不读 size，比例写在提示词里" if not size else ""
    return code("python", f'''
import os
from openai import OpenAI

client = OpenAI(base_url="{API}/v1", api_key=os.environ["PLATFORM_API_KEY"], timeout=300)

result = client.images.generate(
    model="{m["id"]}",
    prompt="{prompt}",{note}{size_line}
)
print(result.data[0].url)  # 临时链接（约 24 小时），请转存
''')


def video_body(cat, m, image=False):
    v = cat.caps(m, "video")
    body = {"model": m["id"], "content": [{"type": "text", "text": "海边日落，无人机航拍视角"}]}
    if image:
        body["content"].append({"type": "image_url", "image_url": {"url": "https://example.com/first-frame.jpg"}})
    d = v.get("duration") or {}
    if d.get("values"):
        body["duration"] = d["values"][0]
    elif d.get("max"):
        lo, hi = d.get("min") or 1, d["max"]
        body["duration"] = min(max(5, lo), hi)
    if v.get("default_resolution"):
        body["resolution"] = v["default_resolution"]
    ratios = v.get("ratios") or []
    if ratios and not image:
        body["ratio"] = "16:9" if "16:9" in ratios else ratios[0]
    return body


def py_dict(d, indent=4):
    """A dict literal with one key per line and compact values (strings, numbers, lists of dicts)."""
    pad = " " * indent
    lines = ["{"] + [f'{pad}    {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)},' for k, v in d.items()] + [pad + "}"]
    return "\n".join(lines)


def py_video(cat, m, image=False):
    body = py_dict(video_body(cat, m, image))
    return code("python", f'''
import os, time, uuid
import requests

BASE = "{API}/v1"
HEADERS = {{"Authorization": f"Bearer {{os.environ['PLATFORM_API_KEY']}}"}}

r = requests.post(
    f"{{BASE}}/videos/generations",
    headers={{**HEADERS, "Idempotency-Key": str(uuid.uuid4())}},  # 重试用同一把键，不会重复扣费
    json={body},
    timeout=60,
)
r.raise_for_status()
task = r.json()

while task["status"] not in ("succeeded", "failed", "expired", "cancelled"):
    time.sleep(10)  # 一般 1–5 分钟
    task = requests.get(f"{{BASE}}/videos/generations/{{task['id']}}", headers=HEADERS, timeout=30).json()

print(task.get("video_url") or task.get("error"))  # video_url 7 天有效，请转存
''')


def py_music(mid):
    return code("python", f'''
import os, time, uuid
import requests

BASE = "{API}/v1"
HEADERS = {{"Authorization": f"Bearer {{os.environ['PLATFORM_API_KEY']}}"}}

r = requests.post(
    f"{{BASE}}/music/generations",
    headers={{**HEADERS, "Idempotency-Key": str(uuid.uuid4())}},
    json={{"model": "{mid}", "prompt": "一首关于夏天海边散步的轻快中文流行歌"}},
    timeout=60,
)
r.raise_for_status()
task = r.json()

while task["status"] not in ("succeeded", "failed", "expired", "cancelled"):
    time.sleep(15)  # 一般 2–4 分钟
    task = requests.get(f"{{BASE}}/music/generations/{{task['id']}}", headers=HEADERS, timeout=30).json()

for track in task.get("tracks", []):  # 一次 2 首
    print(track["title"], track["audio_url"])
''')


def py_tts(mid):
    return code("python", f'''
import os
from openai import OpenAI

client = OpenAI(base_url="{API}/v1", api_key=os.environ["PLATFORM_API_KEY"])

speech = client.audio.speech.create(model="{mid}", voice="alloy", input="你好，欢迎使用语音合成。")
speech.write_to_file("hello.mp3")  # voice 可换成 GET /v1/audio/voices 里的音色 id
''')


def setup_line():
    return (f"先在 [{BRAND}]({SITE}) 控制台创建 API Key（`sk-gpushare-` 开头），"
            f"然后 `export PLATFORM_API_KEY=sk-gpushare-...`。更多示例：[api-examples]({GH_EXAMPLES})。")


# ---------------------------------------------------------------- model facts


def price_rows(m):
    """[(label, now, list)] for every price item of a model."""
    now, lst = m.get("price") or {}, m.get("list_price") or {}
    rows = []
    for key in list(PRICE_KEYS) + sorted(set(now) - set(PRICE_KEYS)):
        if key not in now:
            continue
        zh, _en, unit, _ = PRICE_KEYS.get(key, (key, key, "", ""))
        label = f"{zh} · 每{unit}" if unit else zh
        rows.append((label, triple(now.get(key)), triple(lst.get(key)) if lst.get(key) else "—"))
    return rows


def chat_lines(cat, m):
    ch = cat.caps(m, "chat")
    c = cat.c(m)
    caps = [CAPS_ZH.get(x, x) for x in (m.get("capabilities") or [])]
    if ch.get("file_input") and "文件输入" not in caps:
        caps.insert(1, "文件输入")
    efforts = ((ch.get("reasoning") or {}).get("efforts")) or []
    if efforts and "思考模式" in caps:
        caps[caps.index("思考模式")] = f"思考模式（推理强度 {' / '.join(efforts)}）"
    lines = []
    if m.get("context_window"):
        mo = f"，最大输出 {ctx(m['max_output_tokens'])} token" if m.get("max_output_tokens") else ""
        lines.append(f"上下文 {ctx(m['context_window'])} token{mo}")
    if caps:
        lines.append("能力：" + join_zh(caps))
    protos = [p for p in PROTO_ORDER if p in (c.get("supported_protocols") or [])]
    if protos:
        lines.append("接口：" + " · ".join(
            f"{PROTO[p][0]} `{PROTO[p][1].replace('{id}', m['id'])}`" for p in protos))
    return lines


def image_lines(cat, m):
    img = cat.caps(m, "image")
    if not img:
        return []
    size = img.get("size") or {}
    lines = []
    bits = []
    if size.get("tiers"):
        bits.append("尺寸档 " + " / ".join(size["tiers"]))
    if size.get("mode") == "prompt_ratio":
        bits.append("不读 `size`，画面比例写在提示词里")
    elif size.get("default_size"):
        bits.append(f"默认 `{size['default_size']}`")
    if size.get("min_pixels"):
        side = int(math.sqrt(size["min_pixels"]))
        bits.append(f"尺寸下限约 {side}×{side}")
    if bits:
        lines.append("尺寸：" + "，".join(bits))
    if img.get("ratios"):
        lines.append("比例：" + " / ".join(r if r != "auto" else "自动" for r in img["ratios"]))
    more = []
    if (img.get("max_outputs") or 0) > 1:
        more.append(f"单次最多 {img['max_outputs']} 张")
    if img.get("max_refs"):
        more.append(f"图生图最多 {img['max_refs']} 张参考图")
    if img.get("gif"):
        g = img["gif"]
        fc = " / ".join(str(x) for x in g.get("frame_counts") or [])
        more.append("能生成 GIF 动图" + (f"（{fc} 帧）" if fc else ""))
    if more:
        lines.append(join_zh(more))
    lines.append("接口：`POST /v1/images/generations`（文生图、图生图），`POST /v1/images/edits`（上传图片改图）")
    return lines


def video_lines(cat, m):
    v = cat.caps(m, "video")
    if not v:
        return []
    fam = v.get("family")
    if fam == "avatar":
        return ["数字人形象 + 驱动音频（或文字 + 音色）→ 开口说话的视频",
                f"接口：`POST /v1/videos/generations`（异步任务），用法见[数字人 / 剪辑 API]({FAMILY_DOCS})"]
    if fam == "clip_compose":
        return ["口播视频 → 带字幕特效、标题、模板、背景音乐的成片",
                f"接口：`POST /v1/videos/generations`（异步任务），用法见[数字人 / 剪辑 API]({FAMILY_DOCS})"]
    lines = []
    modes = [MODES_ZH[k] for k in ("t2v", "i2v", "flf", "r2v") if (v.get("modes") or {}).get(k)]
    if modes:
        lines.append("生成方式：" + join_zh(modes))
    if "ref_image" in (v.get("requires") or []):
        lines.append("需要传参考图（首帧或参考图）")
    res = v.get("resolutions") or []
    if res:
        dr = v.get("default_resolution")
        lines.append("分辨率：" + " / ".join(f"{r}（默认）" if r == dr else r for r in res))
    d = v.get("duration") or {}
    if d.get("values"):
        lines.append("时长：" + " / ".join(str(x) for x in d["values"]) + " 秒")
    elif d.get("max"):
        lines.append(f"时长：{d.get('min') or 1}–{d['max']} 秒")
    if v.get("ratios"):
        lines.append("画幅：" + " / ".join(r if r != "adaptive" else "自适应" for r in v["ratios"]))
    refs = v.get("refs") or {}
    rb = []
    if refs.get("images"):
        rb.append(f"图片最多 {refs['images']} 张")
    if refs.get("videos"):
        rb.append(f"视频 {refs['videos']} 段")
    if refs.get("audios"):
        rb.append(f"音频 {refs['audios']} 段")
    if rb and (v.get("modes") or {}).get("r2v"):
        lines.append("参考素材：" + "、".join(rb))
    if v.get("audio") == "toggle":
        lines.append("可生成带声音的视频（可开关）")
    elif v.get("audio") == "always":
        lines.append("成片带声音")
    lines.append("接口：`POST /v1/videos/generations`（异步任务，轮询 `GET /v1/videos/generations/{id}`）")
    return lines


def audio_lines(cat, m):
    ep = cat.c(m).get("endpoint_type")
    if ep == "music_generations":
        return ["一次生成 2 首完整歌曲（含歌词与封面），支持一句话描述成歌、自定义歌词、曲风与纯音乐",
                "接口：`POST /v1/music/generations`（异步任务，轮询 `GET /v1/music/generations/{id}`）"]
    if ep == "tts_synthesize":
        return ["文本转语音（MP3），可用平台公共音色或自己克隆的音色",
                "接口：`POST /v1/audio/speech`（OpenAI SDK 的 `audio.speech.create` 可直接用）"]
    if ep == "voice_clone":
        return ["上传一段本人（或已获授权）的语音，克隆出可复用的音色，用于语音合成和数字人配音",
                "接口：`POST /v1/audio/voices`"]
    if ep == "avatar_create":
        return ["上传一张照片或一段视频，创建可反复使用的数字人形象",
                f"接口：`POST /v1/videos/avatars`，用法见[数字人 / 剪辑 API]({FAMILY_DOCS})"]
    return []


def billing_note(cat, m):
    bf = cat.c(m).get("billing_features") or []
    if "music" in bf:
        return "按次计费（一次生成 2 首），价格见模型页"
    if "tts_char" in bf:
        return "按字符计费，价格见模型页"
    if "voice_clone" in bf:
        return "按次计费，价格见模型页"
    if "avatar" in bf:
        return "价格见模型页"
    return "价格见模型页"


def model_section(cat, m):
    out = [f'<a id="{m["id"]}"></a>', "", f"### {m['name']}", ""]
    head = [f"调用 ID `{m['id']}`", CATS.get(m.get("category"), {}).get("zh") or m.get("category_label") or ""]
    if m.get("released_at"):
        head.append(f"上架 {m['released_at']}")
    out.append(" · ".join(h for h in head if h))
    out.append("")
    d = cat.desc(m)
    if d:
        out += [d, ""]
    rows = price_rows(m)
    if rows:
        has_list = bool(m.get("promotion_factor"))
        if has_list:
            out.append(table(["计价项", "现价（实际扣费）", "原价"], rows))
        else:
            out.append(table(["计价项", "价格"], [(a, b) for a, b, _ in rows]))
        if has_list:
            out += ["", f"现在是限时 {off_zh(m['promotion_factor'])}。"]
        out.append("")
    else:
        out += [f"计费：{billing_note(cat, m)}。", ""]
    k = m.get("category")
    lines = chat_lines(cat, m) if k == "text" else image_lines(cat, m) if k == "image" else \
        video_lines(cat, m) if k == "video" else audio_lines(cat, m)
    if k == "video" and not cat.caps(m, "video") and m["id"] == "dh-avatar-create":
        lines = audio_lines(cat, m)
    if cat.c(m).get("endpoint_type") == "avatar_create":
        lines = audio_lines(cat, m)
    lines.append(f"模型页：[{m['url'].replace('https://', '')}]({m['url']}) · [English]({en_url(m)}) · [Markdown]({m['url']}.md)")
    out += [f"- {x}" for x in lines]
    de = cat.desc(m, "en")
    if de:
        out += ["", f"> {de}"]
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------- pages


def footer(base=""):
    return "\n".join([
        "---",
        "",
        f"数据来自 [{BRAND}]({SITE}/models)，每天自动更新，按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权："
        f"可以自由使用、转载和用于 AI 训练，请注明「{BRAND}」并附链接。"
        f"本页由 [scripts/render.py]({base}scripts/render.py) 根据 [data/models.json]({base}data/models.json) 生成。",
        "",
        f"Data from [{BRAND_EN}]({SITE}/en/models), refreshed daily, licensed CC BY 4.0. "
        f"Generated from [data/models.json]({base}data/models.json).",
        "",
    ])


def rate_line(cat):
    if cat.per_cny and cat.per_usd:
        return (f"平台按积分计费，{fnum(cat.per_cny)} 积分 = ¥1，约 {fnum(cat.per_usd)} 积分 = $1；"
                "表里的 ¥ / $ 是按这个比例换算的参考价。")
    return "平台按积分计费，表里的 ¥ / $ 是换算的参考价。"


def text_rows(cat, models, base, with_rank=False):
    rows = []
    for i, m in enumerate(models, 1):
        r = [model_link(m, base), f"`{m['id']}`", vinfo(m.get("vendor") or "other")["zh"], ctx(m.get("context_window")),
             cny(price(m, "input_per_1m_tokens")), cny(price(m, "output_per_1m_tokens")),
             usd(price(m, "input_per_1m_tokens")), usd(price(m, "output_per_1m_tokens")),
             off_zh(m.get("promotion_factor")) or "—"]
        rows.append(([i] if with_rank else []) + r)
    return rows


def media_unit(m):
    p = m.get("price") or {}
    for key, unit in (("per_image", "张"), ("per_video_second", "秒"), ("per_video_task", "次")):
        if key in p:
            return key, unit
    return None, None


def media_rows(cat, models, base, with_rank=False):
    rows = []
    for i, m in enumerate(models, 1):
        key, unit = media_unit(m)
        p = price(m, key) if key else None
        r = [model_link(m, base), f"`{m['id']}`", vinfo(m.get("vendor") or "other")["zh"],
             f"{cny(p)} / {unit}" if p else billing_note(cat, m).replace("，价格见模型页", ""),
             f"{usd(p)} / {unit}" if p else "—",
             off_zh(m.get("promotion_factor")) or "—"]
        rows.append(([i] if with_rank else []) + r)
    return rows


def sort_by(models, key):
    def k(m):
        p = price(m, key)
        return (0 if p else 1, p["cny"] if p else 0, natkey(m["name"]), m["id"])
    return sorted(models, key=k)


def overview(cat, base=""):
    counts = {k: len(cat.in_cat(k)) for k in CATS}
    parts = [f"{CATS[k]['zh']} {n} 个" for k, n in counts.items() if n]
    return f"共 {len(cat.models)} 个模型：" + "，".join(parts) + f"；数据更新于 {cat.updated}（UTC）。"


def readme(cat):
    n = len(cat.models)
    v_links = " · ".join(vendor_link(k) for k in cat.vendors())
    c_links = " · ".join(f"[{CATS[k]['title']}]({CATS[k]['file']})" for k in CATS if cat.in_cat(k))
    out = [
        f"# AI 大模型 API 价格表（每日更新）· AI model API pricing",
        "",
        f"[{BRAND}]({SITE}) 上全部 {n} 款可调用模型的 API 价格、上下文和能力：GPT、Claude、Gemini、DeepSeek、Kimi、GLM、"
        "通义千问 Qwen、Grok 等对话大模型，GPT-Image、Seedream、Nano Banana、可灵、Qwen Image 等生图模型，"
        "Seedance、Veo、可灵 Kling、Vidu、海螺、通义万相等视频模型，以及 Suno 音乐和语音合成。"
        "每天从平台自动同步，按 CC BY 4.0 开放，可以自由使用（包括商用和 AI 训练）。",
        "",
        f"Prices, context windows and capabilities of all {n} AI models callable through [{BRAND_EN}]({SITE}/en): "
        "chat models (GPT, Claude, Gemini, DeepSeek, Kimi, GLM, Qwen, Grok), image models (GPT-Image, Seedream, "
        "Nano Banana, Kling, Qwen Image), video models (Seedance, Veo, Kling, Vidu, Hailuo, Wan) and Suno music. "
        "Synced from the platform every day; open data under CC BY 4.0. [English](#english)",
        "",
        overview(cat),
        "",
        f"- 按类别：{c_links}",
        f"- 按厂商：{v_links}",
        f"- 数据文件：[`data/models.json`](data/models.json) · [`data/models.csv`](data/models.csv) · "
        f"[Hugging Face]({HF_URL})",
        f"- 怎么调用：[接入示例]({GH_EXAMPLES}) · [文档]({DOCS})",
        "",
        "价格是实际扣费的**现价**（含限时折扣），点模型名看原价、能力和调用示例。" + rate_line(cat),
        "",
    ]
    text = sorted(cat.in_cat("text"), key=table_key)
    if text:
        out += [f"## {CATS['text']['zh']}（{len(text)}）", "",
                "价格单位：每百万 token。", "",
                table(["模型", "调用 ID", "厂商", "上下文", "输入 ¥", "输出 ¥", "输入 $", "输出 $", "折扣"],
                      text_rows(cat, text, "")), ""]
    for k in ("image", "video", "audio"):
        ms = sorted(cat.in_cat(k), key=table_key)
        if not ms:
            continue
        out += [f"## {CATS[k]['zh']}（{len(ms)}）", ""]
        if k == "video":
            out += ["视频按秒计价的是平台目录上的标价；多数视频模型按分辨率分档，具体见模型页。", ""]
        out += [table(["模型", "调用 ID", "厂商", "价格 ¥", "价格 $", "折扣"], media_rows(cat, ms, "")), ""]
    out += [
        "## 数据文件",
        "",
        table(["文件", "内容"], [
            ("[`data/models.json`](data/models.json)",
             "完整数据：调用 ID、名称、厂商、类别、上下文、最大输出、能力、现价与原价（积分、≈人民币、≈美元）、上架与更新日期、模型页链接、许可证"),
            ("[`data/models.csv`](data/models.csv)", "同一份数据的表格版（价格写人民币和美元）"),
        ]),
        "",
        f"实时源：<{SITE}/data/models.json>、<{SITE}/data/models.csv>。这里是每天的快照，提交历史就是价格和上下架的变化记录。"
        f"Hugging Face 镜像：[{HF_ID}]({HF_URL})（`load_dataset(\"{HF_ID}\")`）。",
        "",
        "## 字段（models.json 里的每个模型）",
        "",
        table(["字段", "说明"], [
            ("`id`", "调用时 `model` 填的值"),
            ("`name`、`vendor`、`category`（text / image / video / audio）、`category_label`", "名称、厂商、类别"),
            ("`context_window`、`max_output_tokens`", "上下文窗口、最大输出 token"),
            ("`capabilities`", "能力，如 Image input、Tool calling、Thinking mode、Web search"),
            ("`price`", "**现价**（实际扣费，含限时折扣）：每个计价项给 `credits`（平台积分）、`cny`、`usd`"),
            ("`list_price`、`promotion_factor`", "原价与折扣系数（没有折扣时与现价相同）"),
            ("`released_at`、`updated_at`", "上架日期；价格、名称、描述、能力最后一次变化的时间"),
            ("`url`", "模型详情页"),
        ]),
        "",
        "## 怎么调用这些模型",
        "",
        "一把 `sk-gpushare-` 密钥，OpenAI SDK 把 `base_url` 换成 `https://api.dflop.top/v1`，`model` 填上面的调用 ID 就行；"
        "Anthropic SDK 和 Google Gemini SDK 也能直接用。" + setup_line(),
        "",
        py_chat("gpt-6-luna"),
        "",
        f"生图、视频、音乐、语音的接口和示例见各类别页，以及 [api-examples]({GH_EXAMPLES})。",
        "",
        "## 常见问题",
        "",
        f"**{BRAND}是什么？** 多协议大模型 API 网关与 AI 创作平台（[{SITE.replace('https://', '')}]({SITE})）："
        f"一把 `sk-gpushare-` 密钥，用 OpenAI / Anthropic / Gemini SDK 调用 {n} 款对话、图像、视频、音乐与语音模型。",
        "",
        "**价格多久更新？** 这个仓库每天 02:17（UTC）从平台同步一次，有变化才提交；"
        f"要看实时价格，打开 [模型广场]({SITE}/models) 或 [`/data/models.json`]({SITE}/data/models.json)。",
        "",
        "**现价和原价有什么区别？** 现价是现在实际扣费的价格，已经算上限时折扣；原价见 `list_price`，折扣系数见 `promotion_factor`。",
        "",
        "**这些数据可以商用或拿去训练模型吗？** 可以。按 CC BY 4.0 授权，注明来源「小战AIhub」并附链接即可。",
        "",
        "## English",
        "",
        f"This repository mirrors the open model catalogue of [{BRAND_EN}]({SITE}/en), a multi-protocol AI model "
        f"gateway: one `sk-gpushare-` key lets the OpenAI, Anthropic and Google Gemini SDKs call all {n} models listed "
        "above. The tables show the price charged now, promotions included, in CNY and USD (converted from platform "
        "credits); follow a model name for its list price, capabilities and a code sample.",
        "",
        f"- By category: " + " · ".join(f"[{CATS[k]['title_en']}]({CATS[k]['file']})" for k in CATS if cat.in_cat(k)),
        f"- Data: [`data/models.json`](data/models.json), [`data/models.csv`](data/models.csv), "
        f"also on [Hugging Face]({HF_URL}). Live sources: <{SITE}/data/models.json>.",
        f"- Calling the models: [api-examples]({GH_EXAMPLES}) and the [documentation]({DOCS_EN}).",
        "- Licence: CC BY 4.0. Free to use, share and adapt, commercially and for AI training; please credit "
        f"\"{BRAND_EN}\" with a link to <{SITE}/models>. The commit history is the record of price and listing changes.",
        "",
        footer(),
    ]
    return "\n".join(out)


def page_head(cat, k, names_zh, names_en):
    ms = cat.in_cat(k)
    c = CATS[k]
    return [
        f"# {c['title']}：{names_zh}（{len(ms)} 个模型）",
        "",
        f"> {c['title_en']}: {len(ms)} models ({names_en}) through one API. Updated {cat.updated}.",
        "",
    ]


def text_page(cat):
    ms = cat.in_cat("text")
    by_in = sort_by(ms, "input_per_1m_tokens")
    base = "../"
    vendors = [vinfo(k) for k in cat.vendors() if any((m.get("vendor") or "other") == k for m in ms)]
    rep = cat.rep("text")
    longest = sorted((m for m in ms if m.get("context_window")), key=lambda m: (-m["context_window"], natkey(m["name"])))
    big = [m for m in longest if m["context_window"] >= 1_000_000]
    anth = [m for m in ms if "anthropic_messages" in (cat.c(m).get("supported_protocols") or [])]
    gem = [m for m in ms if "gemini_native" in (cat.c(m).get("supported_protocols") or [])]
    resp = [m for m in ms if "openai_responses" in (cat.c(m).get("supported_protocols") or [])]
    out = page_head(cat, "text", "GPT、Claude、Gemini、DeepSeek、Kimi、GLM、Qwen、Grok",
                    "GPT, Claude, Gemini, DeepSeek, Kimi, GLM, Qwen, Grok")
    out += [
        f"[{BRAND}]({SITE}) 上全部 {len(ms)} 个对话大模型的 API 价格，按输入价从低到高排列，来自 "
        f"{join_zh(v['zh'] for v in vendors)}。一把 `sk-gpushare-` 密钥，OpenAI SDK 改个 `base_url` 就能调用下表任一模型。",
        "",
        "价格是实际扣费的现价（含限时折扣），单位是每百万 token。" + rate_line(cat),
        "",
        f"数据更新于 {cat.updated} · [全部类别]({base}README.md) · [`models.json`]({base}data/models.json)",
        "",
        "## 价格表（输入价从低到高）",
        "",
        table(["#", "模型", "调用 ID", "厂商", "上下文", "输入 ¥", "输出 ¥", "输入 $", "输出 $", "折扣"],
              text_rows(cat, by_in, base, True)),
        "",
        "缓存命中的输入另有更低的价格，见各模型的厂商页。",
        "",
        "## 能力对照",
        "",
    ]
    rows = []
    for m in sorted(ms, key=table_key):
        caps = set(m.get("capabilities") or [])
        protos = [p for p in PROTO_ORDER if p in (cat.c(m).get("supported_protocols") or [])]
        mark = lambda b: "✓" if b else ""
        rows.append([model_link(m, base), mark("Image input" in caps), mark("Tool calling" in caps),
                     mark("Web search" in caps), mark("Thinking mode" in caps), mark("JSON mode" in caps),
                     mark("Image generation" in caps), mark("Open weights" in caps),
                     " / ".join({"openai_chat": "OpenAI", "openai_responses": "Responses",
                                 "anthropic_messages": "Anthropic", "gemini_native": "Gemini"}[p] for p in protos) or "OpenAI"])
    out += [table(["模型", "读图", "工具调用", "联网搜索", "思考", "JSON", "出图", "开源权重", "接口"], rows), "",
            "「接口」列：OpenAI = `/v1/chat/completions`，Responses = `/v1/responses`，Anthropic = `/v1/messages`，"
            "Gemini = `/v1beta/models/{id}:generateContent`。", ""]
    out += ["## 怎么调用", "", setup_line(), "", py_chat(rep["id"] if rep else "gpt-6-luna"), "", curl_chat(rep["id"] if rep else "gpt-6-luna"), ""]
    claude = next((m for m in anth if (m.get("vendor") == "anthropic")), None)
    gm = next((m for m in gem if m.get("vendor") == "google"), None)
    if claude:
        out += ["Claude 也可以用 Anthropic SDK（`base_url` 不带 `/v1`）：", "", py_anthropic(cat.rep("text", [m for m in ms if m.get("vendor") == "anthropic"])["id"]), ""]
    if gm:
        out += ["Gemini 也可以用 Google Gen AI SDK：", "", py_gemini(cat.rep("text", [m for m in ms if m.get("vendor") == "google"])["id"]), ""]
    cheapest = [m for m in by_in if price(m, "input_per_1m_tokens")][:3]
    out += ["## 常见问题", ""]
    if cheapest:
        out += ["**哪个对话模型最便宜？** 按输入价，这份目录里最便宜的三个" + top3_zh(
            f"{model_link(m, base)}，输入 {cny(price(m, 'input_per_1m_tokens'))}、输出 {cny(price(m, 'output_per_1m_tokens'))} / 百万 token"
            for m in cheapest), ""]
    if longest:
        top = longest[0]
        out += [f"**哪个模型上下文最长？** {model_link(top, base)}，{ctx(top['context_window'])} token；"
                f"1M 及以上的共 {len(big)} 个。", ""]
    out += [f"**能用 Anthropic SDK 或 Gemini SDK 调用吗？** 能。Anthropic Messages 接口可调 {len(anth)} 个模型，"
            f"Gemini 原生接口可调 {len(gem)} 个，OpenAI Responses 接口 {len(resp)} 个，OpenAI Chat Completions 接口全部 {len(ms)} 个。"
            f"逐个模型见上面的「能力对照」，说明见 [兼容矩阵]({DOCS}/reference/compatibility-matrix)。", ""]
    out += ["**价格多久更新？** 每天同步一次，实时价格见模型页。", ""]
    out += ["## English", "",
            f"API prices of all {len(ms)} chat models on [{BRAND_EN}]({SITE}/en/models), sorted by input price per "
            "million tokens, with the price charged now (promotions included) in CNY and USD. Every model is reachable "
            "through the OpenAI-compatible endpoint `https://api.dflop.top/v1/chat/completions`; "
            f"{len(anth)} also through the Anthropic Messages API and {len(gem)} through the Gemini API. "
            + (f"The cheapest by input price: {join_en(m['name'] for m in cheapest)}. " if cheapest else "")
            + (f"Longest context: {longest[0]['name']} ({ctx(longest[0]['context_window'])} tokens)." if longest else ""), "",
            footer(base)]
    return "\n".join(out)


def image_page(cat):
    ms = cat.in_cat("image")
    base = "../"
    srt = sort_by(ms, "per_image")
    rep = cat.rep("image")
    rows = []
    for i, m in enumerate(srt, 1):
        img = cat.caps(m, "image")
        size = img.get("size") or {}
        notes = []
        if size.get("mode") == "prompt_ratio":
            notes.append("比例写进提示词")
        if img.get("gif"):
            notes.append("GIF 动图")
        if size.get("min_pixels") and size["min_pixels"] > 1024 * 1024:
            notes.append(f"最小约 {int(math.sqrt(size['min_pixels']))}²")
        p = price(m, "per_image")
        rows.append([i, model_link(m, base), f"`{m['id']}`", vinfo(m.get("vendor") or "other")["zh"],
                     cny(p), usd(p), " / ".join(size.get("tiers") or []) or "—",
                     img.get("max_outputs") or "—", img.get("max_refs") or "—", "，".join(notes) or "—"])
    gif = [m for m in ms if cat.caps(m, "image").get("gif")]
    k4 = [m for m in ms if "4K" in ((cat.caps(m, "image").get("size") or {}).get("tiers") or [])]
    cheapest = [m for m in srt if price(m, "per_image")][:3]
    out = page_head(cat, "image", "GPT-Image、Seedream、Nano Banana、可灵、Qwen Image、Grok Imagine",
                    "GPT-Image, Seedream, Nano Banana, Kling, Qwen Image, Grok Imagine")
    out += [
        f"[{BRAND}]({SITE}) 上全部 {len(ms)} 个图像生成模型的 API 价格，按每张价格从低到高排列。"
        "文生图和图生图（参考图改图）都走 OpenAI Images 形状的接口 `POST /v1/images/generations`，按张计费。",
        "",
        rate_line(cat),
        "",
        f"数据更新于 {cat.updated} · [全部类别]({base}README.md) · [`models.json`]({base}data/models.json)",
        "",
        "## 价格表（每张从低到高）",
        "",
        table(["#", "模型", "调用 ID", "厂商", "¥ / 张", "$ / 张", "尺寸档", "单次最多", "参考图", "备注"], rows),
        "",
        "部分模型按 token 计费（如 GPT-Image 2.6），表里是平台目录上的每张参考价，实际按尺寸和画质结算。",
        "",
        "## 怎么调用",
        "",
        setup_line(),
        "",
    ]
    if rep:
        out += ["文生图：", "", py_image(cat, rep), ""]
    out += ["图生图（参考图改图）：同一个接口加 `image`（公网 URL 或 `data:` URI），或用 `client.images.edit` 直接上传本地文件：", "",
            code("python", f'''
import os
from openai import OpenAI

client = OpenAI(base_url="{API}/v1", api_key=os.environ["PLATFORM_API_KEY"], timeout=300)

result = client.images.edit(
    model="{rep['id'] if rep else 'gpt-image-2'}",
    image=open("original.png", "rb"),
    prompt="把沙发改成蓝色，其余保持不变",
)
print(result.data[0].url)
'''), ""]
    if gif:
        g = gif[0]
        out += [f"GIF 动图（{join_zh(m['name'] for m in gif)}）：`output_format` 传 `gif`：", "",
                code("bash", f'''
curl {API}/v1/images/generations \\
  -H "Authorization: Bearer $PLATFORM_API_KEY" \\
  -H "Content-Type: application/json" \\
  --max-time 300 \\
  -d '{{"model": "{g['id']}", "prompt": "一只卡通小猫挥手打招呼，循环动画，纯色背景", "output_format": "gif", "size": "512x512", "frame_count": 9, "frame_duration_ms": 200}}'
'''), ""]
    out += ["## 常见问题", ""]
    if cheapest:
        out += ["**哪个生图 API 最便宜？** 按每张价格，这份目录里最便宜的三个" + top3_zh(
            f"{model_link(m, base)}，{cny(price(m, 'per_image'))} / 张" for m in cheapest), ""]
    no4k = [m for m in ms if m not in k4]
    if k4 and no4k:
        out += [f"**都能出 4K 吗？** {len(ms)} 个里有 {len(k4)} 个支持 4K；不支持的是 "
                f"{join_zh(model_link(m, base) for m in sorted(no4k, key=table_key))}。", ""]
    if gif:
        out += [f"**能生成 GIF 动图吗？** 能，{join_zh(model_link(m, base) for m in gif)} 支持，见上面的示例。", ""]
    out += ["**返回的图片链接能用多久？** 是临时链接（约 24 小时），拿到后请下载转存。", "",
            "**为什么要把超时设长？** 部分模型（如 GPT-Image）一张图要 30 秒到 3 分钟，客户端超时请设 300 秒以上，"
            "或者在请求里加 `\"async\": true` 改成提交 + 轮询。", "",
            f"完整参数见 [图像 API 文档]({DOCS}/reference/media-apis) 和 [图生图指南]({DOCS}/guides/image-editing)。", ""]
    out += ["## English", "",
            f"Per-image API prices of all {len(ms)} image generation models on [{BRAND_EN}]({SITE}/en/models), "
            "cheapest first. Text-to-image and image editing use the OpenAI Images API shape "
            "(`POST https://api.dflop.top/v1/images/generations`, or `/v1/images/edits` for file uploads), billed per image. "
            + (f"Cheapest: {join_en(m['name'] for m in cheapest)}. " if cheapest else "")
            + (f"Animated GIF output: {join_en(m['name'] for m in gif)}." if gif else ""), "",
            footer(base)]
    return "\n".join(out)


def video_page(cat):
    ms = cat.in_cat("video")
    base = "../"
    generic = lambda m: cat.caps(m, "video").get("family") in (None, "generic")
    srt = sort_by([m for m in ms if generic(m)], "per_video_second") + \
        sorted([m for m in ms if not generic(m)], key=table_key)
    rep = cat.rep("video")
    rows = []
    for i, m in enumerate(srt, 1):
        v = cat.caps(m, "video")
        key, unit = media_unit(m)
        p = price(m, key) if key else None
        modes = [MODES_ZH[x] for x in ("t2v", "i2v", "flf", "r2v") if (v.get("modes") or {}).get(x)]
        d = v.get("duration") or {}
        dur = (" / ".join(str(x) for x in d["values"]) + " 秒") if d.get("values") else \
            (f"{d.get('min') or 1}–{d['max']} 秒" if d.get("max") else "—")
        fam = v.get("family")
        if fam == "avatar":
            modes = ["数字人口播"]
        elif fam == "clip_compose":
            modes = ["智能剪辑"]
        audio = {"toggle": "可选", "always": "有"}.get(v.get("audio"), "—")
        rows.append([i, model_link(m, base), f"`{m['id']}`", vinfo(m.get("vendor") or "other")["zh"],
                     f"{cny(p)} / {unit}" if p else "见模型页", f"{usd(p)} / {unit}" if p else "—",
                     "、".join(modes) or "—", " / ".join(v.get("resolutions") or []) or "—", dur, audio])
    per_sec = [m for m in srt if price(m, "per_video_second") and cat.caps(m, "video").get("family") in (None, "generic")]
    longest = sorted((m for m in ms if (cat.caps(m, "video").get("duration") or {}).get("max")),
                     key=lambda m: (-(cat.caps(m, "video")["duration"]["max"]), natkey(m["name"])))
    k4 = [m for m in ms if "4k" in (cat.caps(m, "video").get("resolutions") or [])]
    sound = [m for m in ms if cat.caps(m, "video").get("audio") == "toggle"]
    out = page_head(cat, "video", "Seedance、Veo、可灵 Kling、Vidu、海螺 Hailuo、通义万相 Wan、Grok Imagine",
                    "Seedance, Veo, Kling, Vidu, Hailuo, Wan, Grok Imagine")
    out += [
        f"[{BRAND}]({SITE}) 上全部 {len(ms)} 个视频生成模型的 API 价格和参数，按每秒价格从低到高排列。"
        "文生视频、图生视频、首尾帧和参考生视频都走同一个异步接口 `POST /v1/videos/generations`：提交任务，再轮询结果。",
        "",
        "价格是平台模型目录上的每秒标价（含限时折扣）。多数视频模型按分辨率分档，Seedance 系列按 token 计费，"
        f"实际扣费以模型页和[计费说明]({DOCS}/reference/media-apis)为准。" + rate_line(cat),
        "",
        f"数据更新于 {cat.updated} · [全部类别]({base}README.md) · [`models.json`]({base}data/models.json)",
        "",
        "## 价格表（每秒从低到高）",
        "",
        table(["#", "模型", "调用 ID", "厂商", "¥", "$", "生成方式", "分辨率", "时长", "声音"], rows),
        "",
        "数字人和智能剪辑排在最后，它们是成片工具，不是通用视频模型。",
        "",
        "## 怎么调用",
        "",
        setup_line(),
        "",
    ]
    if rep:
        out += ["文生视频（提交 + 轮询）：", "", py_video(cat, rep), "",
                "图生视频：在 `content` 里加一张首帧图（公网 URL）：", "",
                code("json", json.dumps(video_body(cat, rep, image=True), ensure_ascii=False, indent=2)), ""]
    out += ["参数（分辨率、时长、画幅）按模型不同，见上表和各模型的厂商页；不支持的取值会直接返回 400，不扣费。"
            "带 `Idempotency-Key` 重试不会重复扣费；不想轮询可以传 `callback_url`。", ""]
    out += ["## 常见问题", ""]
    if per_sec:
        cheap = per_sec[:3]
        out += ["**哪个视频生成 API 最便宜？** 按每秒标价，这份目录里最便宜的三个" + top3_zh(
            f"{model_link(m, base)}，{cny(price(m, 'per_video_second'))} / 秒" for m in cheap), ""]
    if longest:
        mx = cat.caps(longest[0], "video")["duration"]["max"]
        top = [m for m in longest if cat.caps(m, "video")["duration"]["max"] == mx]
        out += [f"**单条视频最长多少秒？** {mx} 秒：{join_zh(model_link(m, base) for m in top)}。", ""]
    if k4:
        out += [f"**哪些模型能出 4K？** {join_zh(model_link(m, base) for m in sorted(k4, key=order_key))}。", ""]
    if sound:
        out += [f"**能生成带声音的视频吗？** 能，{join_zh(model_link(m, base) for m in sorted(sound, key=order_key))} 可以选择生成声音。", ""]
    out += ["**生成要多久？结果能保存多久？** 一般 1–5 分钟；成片的 `video_url` 7 天有效，请下载转存。", ""]
    out += ["## English", "",
            f"Prices and parameters of all {len(ms)} video generation models on [{BRAND_EN}]({SITE}/en/models): "
            "Seedance, Veo, Kling, Vidu, Hailuo, Wan, Grok Imagine and more. Text-to-video, image-to-video, "
            "first-and-last-frame and reference-to-video all use one asynchronous endpoint, "
            "`POST https://api.dflop.top/v1/videos/generations`, then poll `GET /v1/videos/generations/{id}`. "
            "Prices are the catalogue's per-second list (promotions included); most models are tiered by resolution. "
            + (f"Cheapest per second: {join_en(m['name'] for m in per_sec[:3])}." if per_sec else ""), "",
            footer(base)]
    return "\n".join(out)


def audio_page(cat):
    ms = sorted(cat.in_cat("audio"), key=order_key)
    base = "../"
    rows = [[model_link(m, base), f"`{m['id']}`", vinfo(m.get("vendor") or "other")["zh"],
             next((x.replace("接口：", "") for x in audio_lines(cat, m) if x.startswith("接口：")), "—"),
             billing_note(cat, m).replace("，价格见模型页", "")] for m in ms]
    music = next((m for m in ms if cat.c(m).get("endpoint_type") == "music_generations"), None)
    tts = next((m for m in ms if cat.c(m).get("endpoint_type") == "tts_synthesize"), None)
    names = join_zh(m["name"] for m in ms)
    out = page_head(cat, "audio", "Suno 音乐、语音合成、声音克隆", "Suno music, text-to-speech, voice cloning")
    out += [
        f"[{BRAND}]({SITE}) 上的 {len(ms)} 个音频模型：{names}。和对话、生图模型共用同一把 `sk-gpushare-` 密钥。",
        "",
        f"数据更新于 {cat.updated} · [全部类别]({base}README.md) · [`models.json`]({base}data/models.json)",
        "",
        table(["模型", "调用 ID", "厂商", "接口", "计费"], rows),
        "",
        "具体价格见各模型页。",
        "",
        "## 怎么调用",
        "",
        setup_line(),
        "",
    ]
    if music:
        out += [f"AI 音乐（{music['name']}，一次生成 2 首完整歌曲）：", "", py_music(music["id"]), "",
                "自定义歌词传 `lyrics`，曲风传 `tags`，纯音乐传 `\"instrumental\": true`。", ""]
    if tts:
        out += ["语音合成（OpenAI SDK 照官方写法就能用，直接拿到 MP3）：", "", py_tts(tts["id"]), "",
                "长文案请在请求体里加 `\"async\": true` 改成提交 + 轮询。", ""]
    out += [f"完整说明见 [音乐 / 语音 API 文档]({DOCS}/reference/media-apis)。", "",
            "## English", "",
            f"Audio models on [{BRAND_EN}]({SITE}/en/models): Suno V6 music generation "
            "(`POST https://api.dflop.top/v1/music/generations`, two full songs with lyrics and cover art per request), "
            "text-to-speech (`POST /v1/audio/speech`, works with the OpenAI SDK's `audio.speech.create`) and voice cloning "
            "(`POST /v1/audio/voices`). The same `sk-gpushare-` key as for chat and image models.", "",
            footer(base)]
    return "\n".join(out)


def vendor_page(cat, key):
    v = vinfo(key)
    ms = cat.of_vendor(key)
    base = "../"
    cats = [k for k in CATS if any(m.get("category") == k for m in ms)]
    count = "，".join(f"{CATS[k]['zh']} {sum(1 for m in ms if m.get('category') == k)} 个" for k in cats)
    title_zh = f"{v['zh']} API 价格与调用" if key != "other" else f"{BRAND}自有模型与能力"
    out = [
        f"# {title_zh}：{v['what']}",
        "",
        f"> {v['en']} API pricing on {BRAND_EN}: {len(ms)} models ({v['what_en']}). Updated {cat.updated}.",
        "",
        f"[{BRAND}]({SITE}) 上可调用的 {v['zh']} 模型共 {len(ms)} 个（{count}），一把 `sk-gpushare-` 密钥全都能调：" +
        "，".join(HOW_ZH[k] for k in cats if k in HOW_ZH) + "。下面是每个模型的价格、参数和接口。",
        "",
        rate_line(cat),
        "",
        f"数据更新于 {cat.updated} · [全部厂商]({base}README.md) · " +
        " · ".join(f"[{CATS[k]['title']}]({base}{CATS[k]['file']})" for k in cats) +
        (f" · [官网厂商页]({SITE}/vendors/{key})" if key in SITE_VENDOR_PAGES else ""),
        "",
        "## 模型一览",
        "",
    ]
    rows = []
    for m in ms:
        k = m.get("category")
        if k == "text":
            p = f"输入 {cny(price(m, 'input_per_1m_tokens'))} / 输出 {cny(price(m, 'output_per_1m_tokens'))} 每百万 token"
        else:
            pk, unit = media_unit(m)
            p = f"{cny(price(m, pk))} / {unit}" if pk else billing_note(cat, m).replace("，价格见模型页", "")
        rows.append([f"[{m['name']}](#{m['id']})", f"`{m['id']}`", CATS.get(k, {}).get("zh", k), p,
                     ctx(m.get("context_window")) if k == "text" else "—", off_zh(m.get("promotion_factor")) or "—"])
    out += [table(["模型", "调用 ID", "类别", "现价", "上下文", "折扣"], rows), "", "## 各模型详情", ""]
    for m in ms:
        out.append(model_section(cat, m))
    out += ["## 调用示例", "", setup_line(), ""]
    for k in cats:
        pool = [m for m in ms if m.get("category") == k]
        rep = cat.rep(k, pool)
        if not rep:
            continue
        if k == "text":
            out += [f"对话（{rep['name']}）：", "", py_chat(rep["id"]), ""]
            protos = cat.c(rep).get("supported_protocols") or []
            if key == "anthropic" and "anthropic_messages" in protos:
                out += ["用 Anthropic SDK（`base_url` 不带 `/v1`）：", "", py_anthropic(rep["id"]), ""]
            if key == "google" and "gemini_native" in protos:
                out += ["用 Google Gen AI SDK（Gemini 原生协议）：", "", py_gemini(rep["id"]), ""]
        elif k == "image":
            out += [f"生图（{rep['name']}）：", "", py_image(cat, rep), ""]
        elif k == "video":
            vv = cat.caps(rep, "video")
            if vv.get("family") in (None, "generic") and "ref_image" not in (vv.get("requires") or []):
                out += [f"视频（{rep['name']}）：", "", py_video(cat, rep), ""]
            else:
                out += [f"数字人与智能剪辑的完整流程见 [数字人 / 剪辑 API]({FAMILY_DOCS})。", ""]
        elif k == "audio":
            ep = cat.c(rep).get("endpoint_type")
            if ep == "music_generations":
                out += [f"音乐（{rep['name']}）：", "", py_music(rep["id"]), ""]
            elif ep == "tts_synthesize":
                out += [f"语音合成（{rep['name']}）：", "", py_tts(rep["id"]), ""]
    out += ["## English", "",
            f"{len(ms)} {v['en']} models are available through [{BRAND_EN}]({SITE}/en/models) ({v['what_en']}). "
            "Each section above lists the call id, the price charged now in platform credits, CNY and USD, and "
            "the supported endpoints. One `sk-gpushare-` key covers them all: " +
            "; ".join(HOW_EN[k] for k in cats if k in HOW_EN) + ".", "",
            footer(base)]
    return "\n".join(out)


def hf_card(cat):
    n = len(cat.models)
    tags = ["llm", "llm-api", "api-pricing", "ai-pricing", "model-catalog", "openai-compatible", "ai-gateway",
            "text-to-image", "text-to-video", "image-generation", "video-generation", "gpt", "claude", "gemini",
            "deepseek", "qwen", "kimi", "glm", "seedance", "kling", "veo", "suno", "chinese"]
    yaml = "\n".join([
        "---",
        "license: cc-by-4.0",
        "language:",
        "- zh",
        "- en",
        "pretty_name: AI Model API Pricing (XiaoZhan AIhub)",
        "tags:",
        *[f"- {t}" for t in tags],
        "size_categories:",
        "- n<1K",
        "configs:",
        "- config_name: default",
        "  data_files:",
        "  - split: train",
        "    path: data/models.csv",
        "---",
    ])
    def gh(path):
        return f"{GH_BLOB}/{path}"
    def link(m):
        v = vinfo(m.get("vendor") or "other")
        return f"[{m['name']}]({gh('vendors/' + v['slug'] + '.md')}#{m['id']})"
    text = sorted(cat.in_cat("text"), key=table_key)
    out = [
        yaml,
        "",
        f"# AI 大模型 API 价格数据集 · AI Model API Pricing",
        "",
        f"[{BRAND}]({SITE}) 上全部 {n} 款可调用模型的 API 价格、上下文和能力，每天自动更新："
        "GPT、Claude、Gemini、DeepSeek、Kimi、GLM、Qwen、Grok 对话大模型，GPT-Image、Seedream、Nano Banana、可灵生图模型，"
        "Seedance、Veo、可灵、Vidu、海螺、万相视频模型，以及 Suno 音乐和语音合成。CC BY 4.0，可商用，可用于 AI 训练。",
        "",
        f"Daily-updated API prices, context windows and capabilities of the {n} AI models callable through "
        f"[{BRAND_EN}]({SITE}/en), an OpenAI-compatible multi-model API gateway: chat models (GPT, Claude, Gemini, "
        "DeepSeek, Kimi, GLM, Qwen, Grok), image models (GPT-Image, Seedream, Nano Banana, Kling), video models "
        "(Seedance, Veo, Kling, Vidu, Hailuo, Wan) and Suno music. Licensed CC BY 4.0.",
        "",
        overview(cat),
        "",
        "## 用法 · Usage",
        "",
        code("python", f'''
from datasets import load_dataset

ds = load_dataset("{HF_ID}", split="train")
print(ds[0]["id"], ds[0]["input_cny_per_1m_tokens"])
'''),
        "",
        code("python", f'''
import pandas as pd

df = pd.read_csv("hf://datasets/{HF_ID}/data/models.csv")
print(df[df.category == "video"].sort_values("cny_per_video_second").head(10))
'''),
        "",
        code("sql", f"-- DuckDB\nSELECT id, name, input_usd_per_1m_tokens, output_usd_per_1m_tokens\n"
                    f"FROM 'hf://datasets/{HF_ID}/data/models.csv'\nWHERE category = 'text'\nORDER BY input_usd_per_1m_tokens;"),
        "",
        "## 文件 · Files",
        "",
        table(["文件 File", "内容 Contents"], [
            ("`data/models.csv`", "一行一个模型：价格（¥ / $）、上下文、能力、日期、链接（数据查看器用的就是它）。One row per model."),
            ("`data/models.json`", "完整数据：现价与原价（积分、≈¥、≈$），带许可证与来源说明。Full data with list prices, licence and source."),
        ]),
        "",
        f"源地址 Live source: <{SITE}/data/models.json>. 同步自 Synced from GitHub [xiaozhan-aihub/{REPO}]({GH_REPO})"
        "（提交历史就是价格变化记录 · the commit history records every price change）。",
        "",
        "## 对话大模型价格 · Chat model prices",
        "",
        "每百万 token 的现价（含限时折扣）。Price per million tokens charged now, promotions included.",
        "",
        table(["模型 Model", "调用 ID", "上下文 Context", "输入 ¥", "输出 ¥", "Input $", "Output $"],
              [[link(m), f"`{m['id']}`", ctx(m.get("context_window")), cny(price(m, "input_per_1m_tokens")),
                cny(price(m, "output_per_1m_tokens")), usd(price(m, "input_per_1m_tokens")),
                usd(price(m, "output_per_1m_tokens"))] for m in text]),
        "",
    ]
    for k, title in (("image", "生图模型价格 · Image model prices"), ("video", "视频模型价格 · Video model prices")):
        ms = sorted(cat.in_cat(k), key=table_key)
        if not ms:
            continue
        rows = []
        for m in ms:
            key, unit = media_unit(m)
            p = price(m, key) if key else None
            rows.append([link(m), f"`{m['id']}`", vinfo(m.get("vendor") or "other")["en"],
                         f"{cny(p)} / {unit}" if p else "—", f"{usd(p)}" if p else "—"])
        out += [f"## {title}", "", table(["模型 Model", "调用 ID", "Vendor", "¥", "$"], rows), ""]
    out += [
        f"更多对比（按价格排序、能力、参数、调用示例）：[大模型]({gh(CATS['text']['file'])}) · "
        f"[生图]({gh(CATS['image']['file'])}) · [视频]({gh(CATS['video']['file'])}) · "
        f"[音乐与语音]({gh(CATS['audio']['file'])})。",
        "",
        "## 字段 · Fields (models.csv)",
        "",
        table(["字段 Field", "说明 Description"], [
            ("`id`", "调用时 `model` 填的值 · the model id to call"),
            ("`name`, `vendor`, `category`", "名称、厂商、类别（text / image / video / audio）"),
            ("`context_window`, `max_output_tokens`", "上下文、最大输出 token"),
            ("`input_cny_per_1m_tokens`, `output_cny_per_1m_tokens`, `cached_input_cny_per_1m_tokens`", "对话模型现价（¥ / 百万 token）"),
            ("`input_usd_per_1m_tokens`, `output_usd_per_1m_tokens`", "同上（$）"),
            ("`cny_per_image`, `cny_per_video_second`, `cny_per_video_task`", "生图、视频的现价（¥）"),
            ("`list_input_cny_per_1m_tokens`, `list_output_cny_per_1m_tokens`, `promotion_factor`", "原价与折扣系数"),
            ("`capabilities`", "能力（分号分隔）"),
            ("`released_at`, `updated_at`, `url`", "上架日期、最后变化时间、模型页"),
        ]),
        "",
        "## 怎么调用这些模型 · Calling the models",
        "",
        "一把 `sk-gpushare-` 密钥，OpenAI SDK 的 `base_url` 换成 `https://api.dflop.top/v1`，`model` 填 `id`。"
        "One key, the OpenAI SDK with `base_url=\"https://api.dflop.top/v1\"`, and the `id` column as `model`:",
        "",
        py_chat("gpt-6-luna"),
        "",
        f"更多示例 More examples: [github.com/xiaozhan-aihub/api-examples]({GH_EXAMPLES}) · 文档 Docs: [{DOCS.replace('https://', '')}]({DOCS})",
        "",
        "## 许可与引用 · Licence and citation",
        "",
        f"CC BY 4.0：可以自由使用、转载和改编，包括商用和 AI 训练；请注明来源「{BRAND}」并附链接 <{SITE}/models>。"
        f"Free to use, share and adapt, commercially and for AI training; please credit \"{BRAND_EN}\" with a link.",
        "",
        code("bibtex", f'''
@misc{{xiaozhan_aihub_model_pricing,
  title        = {{AI Model API Pricing}},
  author       = {{{{XiaoZhan AIhub}}}},
  howpublished = {{\\url{{{HF_URL}}}}},
  note         = {{Daily snapshot of {SITE}/data/models.json, CC BY 4.0}}
}}
'''),
        "",
    ]
    return "\n".join(out)


# ---------------------------------------------------------------- main


def write(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    text = text.rstrip() + "\n"
    old = None
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            old = f.read()
    if old != text:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    return old != text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/models.json")
    ap.add_argument("--catalog", required=True, help="saved copy of /api/v1/models/public")
    ap.add_argument("--out", default=".")
    args = ap.parse_args()

    with open(args.data, encoding="utf-8") as f:
        data = json.load(f)
    with open(args.catalog, encoding="utf-8") as f:
        catalog = json.load(f)
    cat = Catalog(data, catalog)
    if not cat.models:
        sys.exit("no models in the data: nothing rendered")
    missing = [m["id"] for m in cat.models if m["id"] not in cat.cat]
    if len(missing) > len(cat.models) // 2:
        sys.exit(f"the catalogue lacks {len(missing)} of {len(cat.models)} models: nothing rendered")

    pages = {"README.md": readme(cat)}
    makers = {"text": text_page, "image": image_page, "video": video_page, "audio": audio_page}
    for k, make in makers.items():
        if cat.in_cat(k):
            pages[CATS[k]["file"]] = make(cat)
    for key in cat.vendors():
        pages[f"vendors/{vinfo(key)['slug']}.md"] = vendor_page(cat, key)
    pages["build/hf/README.md"] = hf_card(cat)

    for path, text in pages.items():
        low = text.lower()
        bad = [w for w in BANNED if w.lower() in low]
        if bad:
            sys.exit(f"{path} contains {bad}: nothing written")

    # Pages of vendors or categories that disappeared from the data.
    keep = {os.path.normpath(p) for p in pages}
    for d in ("vendors", "pricing"):
        full = os.path.join(args.out, d)
        if os.path.isdir(full):
            for name in os.listdir(full):
                rel = os.path.normpath(os.path.join(d, name))
                if name.endswith(".md") and rel not in keep:
                    os.remove(os.path.join(full, name))
                    print(f"removed {rel}")

    changed = [p for p, t in pages.items() if write(os.path.join(args.out, p), t)]
    print(f"rendered {len(pages)} pages for {len(cat.models)} models"
          + (f" ({len(missing)} without catalogue details)" if missing else "")
          + (f"; changed: {', '.join(changed)}" if changed else "; no change"))


if __name__ == "__main__":
    main()
