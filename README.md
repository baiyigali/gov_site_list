# gov-site-list

中国政府网站（中央 + 省级 + 垂直部委）的 **通知/政策栏目 URL 清单**，纯文本静态数据，供政务监测爬虫消费。

这个仓库只做一件事：**维护"该抓哪些页面"的地址列表**。不存正文、不做抓取逻辑、不写代码——就是一堆 `.txt` 文件，每行一个 JSON 对象，人工维护，Git 管理。

## 目录结构

```
gov-site-list/
├── homepages/                        # 第一层：政府网站首页
│   ├── all_gov_homepages.txt         # 全国 .gov.cn 全集（占位，待回填）
│   ├── central.txt                   # 中央政府及组成部门、直属机构首页
│   └── provincial.txt                # 31 个省级人民政府首页
│
├── notice_columns/                   # 第二层：实际要监测的通知/政策栏目页
│   ├── central_gov.txt               # 中国政府网栏目
│   ├── provinces/                    # 各省级政府栏目，一省一个文件
│   │   ├── beijing.txt
│   │   ├── shanghai.txt
│   │   └── ...
│   └── ministries/                   # 各部委栏目，一部一个文件
│       ├── miit.txt                  # 工信部
│       ├── pbc.txt                   # 央行
│       └── ...
│
├── rss_feeds/                        # 第三层：有 RSS 的栏目单独记录
│   └── rss.txt
│
└── docs/images/                      # README 用图
```

## 文件格式

所有数据文件都是 **JSONL**（每行一个 JSON 对象），注释行以 `#` 开头，方便人工直接编辑：

```json
{"site": "工业和信息化部", "column": "政策文件", "url": "https://www.miit.gov.cn/zwgk/zcwj/", "encoding": "utf-8", "rss": null}
```

字段说明：

| 字段 | 说明 |
|---|---|
| `site` | 站点/机构名称 |
| `column` | 栏目名称 |
| `url` | 栏目列表页 URL（实际要抓的地址） |
| `encoding` | 页面编码，多数 `utf-8`，老站点可能是 `gbk` |
| `rss` | 该栏目 RSS 地址，没有则为 `null` |

## 维护方式

- 这是静态数据仓库，**不需要 CI/CD**，改完直接 commit。
- 新增/修改栏目 URL 时，对应文件里加一行或改一行即可。
- 建议每周跑一次健康检查：遍历 `notice_columns/` 下所有 URL，HEAD 请求一遍，把 404、超时、重定向的列出来人工修。
- `homepages/` 是全集参考，`notice_columns/` 是抓取器真正消费的内容。以后扩到市县级，从 `all_gov_homepages.txt` 里挑。

## 配套项目

本仓库只维护地址列表。实际的抓取、去重、正文提取、推送通知，由另一个独立仓库消费本仓库的数据完成。两边解耦：改 URL 不用动代码，改抓取逻辑不用动清单。

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
