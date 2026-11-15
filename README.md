# 小战AIhub 模型目录与价格（开放数据）· XiaoZhan AIhub model catalogue (open data)

[小战AIhub](https://model.dflop.top) 上全部可调用模型的目录与价格，每天从平台自动同步一次。按 **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** 授权：可以自由使用、转载、改编，包括商用和用于 AI 训练，请注明来源「小战AIhub」并附链接 <https://model.dflop.top/models>。

[English](#english)

| 文件 | 内容 |
|---|---|
| [`data/models.json`](data/models.json) | 完整数据：模型、价格（积分、≈人民币、≈美元）、能力、上下文、发布与更新日期，带许可证与来源说明 |
| [`data/models.csv`](data/models.csv) | 同一份数据的表格版（价格写人民币与美元） |

源地址（实时）：<https://model.dflop.top/data/models.json>、<https://model.dflop.top/data/models.csv>。这里是每天的快照，提交历史就是价格与上下架的变化记录。

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

平台按积分计费；`cny` / `usd` 是按平台公布的汇率换算的参考值（文件里的 `currency` 一节写着换算比例）。

## 怎么用这些模型

一把 `sk-gpushare-` 密钥，用 OpenAI / Anthropic / Gemini SDK 都能调。示例：[xiaozhan-aihub/api-examples](https://github.com/xiaozhan-aihub/api-examples)，文档：[model.dflop.top/docs](https://model.dflop.top/docs)。

---

## English

The catalogue and prices of every model callable on [XiaoZhan AIhub](https://model.dflop.top/en), synced from the platform once a day. Licensed **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**: free to use, share and adapt, commercially and for AI training; please credit "XiaoZhan AIhub" with a link to <https://model.dflop.top/models>.

- `data/models.json`: models, prices (platform credits, ≈CNY, ≈USD), capabilities, context window, release and update dates, plus the licence and source.
- `data/models.csv`: the same rows as a table (prices in CNY and USD).
- Live sources: <https://model.dflop.top/data/models.json> and <https://model.dflop.top/data/models.csv>. The commit history of this repository is the record of price and listing changes.

`price` is the price charged now (promotions included); `list_price` and `promotion_factor` give the regular price. `updated_at` is when the model's public details (price, name, description, capabilities) last changed.

To call these models with the OpenAI, Anthropic or Gemini SDKs, see [xiaozhan-aihub/api-examples](https://github.com/xiaozhan-aihub/api-examples) and the [docs](https://model.dflop.top/en/docs).
