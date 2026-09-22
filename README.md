# gov-site-list

中国政府网站（中央 + 省级 + 垂直部委）的 **首页与通知/政策栏目 URL 清单**，纯文本静态数据。

这个仓库只做一件事：**维护一份政府网站地址列表**。不存正文、不做处理逻辑，就是一堆 `.jsonl` 文件，每行一个 JSON 对象，人工维护，Git 管理。

## 目录结构

```
gov-site-list/
├── homepages/                        # 政府网站首页
│   ├── all_gov_homepages.jsonl         # 全国 .gov.cn 全集（占位，待回填）
│   ├── central.jsonl                   # 中央政府及组成部门、直属机构首页
│   └── provincial.jsonl                # 31 个省级人民政府首页
│
├── notice_columns/                   # 通知/政策栏目页
│   ├── central_gov.jsonl               # 中国政府网栏目
│   ├── provinces/                    # 各省级政府栏目，一省一个文件
│   │   ├── beijing.jsonl
│   │   ├── shanghai.jsonl
│   │   └── ...
│   └── ministries/                   # 各部委栏目，一部一个文件
│       ├── miit.jsonl                  # 工业和信息化部
│       ├── pbc.jsonl                   # 中国人民银行
│       └── ...
│
├── rss_feeds/                        # RSS 地址
│   └── rss.jsonl
│
└── docs/images/                      # README 用图
```

## 文件格式

所有数据文件都是 **JSONL**（每行一个 JSON 对象，UTF-8，不含注释）。不同目录下的文件字段略有差异：

### `homepages/`

首页类文件，字段为 `name` / `url` / `category` 或 `region`：

```json
{"name": "工业和信息化部", "url": "https://www.miit.gov.cn", "category": "国务院组成部门"}
{"name": "北京市人民政府", "url": "https://www.beijing.gov.cn", "region": "北京"}
```

| 文件 | 额外字段 | 说明 |
|---|---|---|
| `central.jsonl` | `category` | 机构类别（国务院门户 / 组成部门 / 直属机构 / 部委管理国家局） |
| `provincial.jsonl` | `region` | 省级行政区简称 |
| `all_gov_homepages.jsonl` | — | 全国 `.gov.cn` 全集，目前为空占位。后续可从中国政府网"政府网站导航"、工信部域名备案数据或 GitHub 公开列表回填 |

### `notice_columns/`

栏目页文件，字段为 `site` / `column` / `url` / `encoding` / `rss`：

```json
{"site": "工业和信息化部", "column": "政策文件", "url": "https://www.miit.gov.cn/zwgk/zcwj/", "encoding": "utf-8", "rss": null}
```

| 字段 | 说明 |
|---|---|
| `site` | 站点/机构名称 |
| `column` | 栏目名称 |
| `url` | 栏目页 URL |
| `encoding` | 页面编码，多数 `utf-8`，老站点可能是 `gbk` |
| `rss` | 该栏目 RSS 地址，没有则为 `null` |

### `rss_feeds/`

RSS 地址单独记录，字段为 `site` / `column` / `rss`，目前为空，探测到后补。

## 维护方式

- 静态数据仓库，不需要 CI/CD，改完直接 commit。
- 新增或修改地址时，对应文件里加一行或改一行即可。
- 建议定期检查链接可用性，把失效、改版的地址修正过来。

## 技术交流

扫码添加微信，交流使用问题、定制与合作：

<p align="center">
  <img src="docs/images/wechat-contact-qr.jpg" alt="微信二维码" width="240" />
</p>

## 项目赞助

本项目由微信公众号 **「程序员白大力」** 提供赞助，感谢支持：

<p align="center">
  <img src="docs/images/wechat-official-account-qr.png" alt="程序员白大力公众号二维码" width="240" />
</p>

## License

MIT
