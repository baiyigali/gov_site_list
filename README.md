# gov-site-list

中国政府网站（中央 + 省级 + 垂直部委）的 **首页与通知/政策栏目 URL 清单**，Python 包形式发布，一行 `pip install` 就能用。

这个仓库只做一件事：**维护一份政府网站地址列表**。不存正文、不做处理逻辑，就是一堆 `.jsonl` 文件，每行一个 JSON 对象，人工维护，Git 管理。

## 安装

```bash
pip install gov-site-list
```

## 使用

```python
import gov_site_list as g

# 所有政府网站首页（中央 + 省级）
homepages = g.load_homepages()

# 所有通知/政策栏目（中央 + 部委 + 省级）
notice_columns = g.load_notice_columns()

# RSS 地址
rss = g.load_rss_feeds()

# 按路径加载单个 JSONL 文件
rows = list(g.load_jsonl("notice_columns/ministries/miit.jsonl"))

# 列出所有数据文件
files = g.list_jsonl_files()

# 数据目录
data_dir = g.data_dir()
```

## 数据规模

- **首页**：75 条（中央机构 + 31 个省级）
- **通知/政策栏目**：136 条（中央 + 42 个部委 + 31 个省级）

## 目录结构

```
gov-site-list/
├── gov_site_list/                  # Python 包
│   ├── __init__.py                 # 读取 API
│   ├── py.typed
│   └── data/                       # 数据文件（JSONL）
│       ├── homepages/              # 政府网站首页
│       ├── notice_columns/         # 通知/政策栏目
│       │   ├── central_gov.jsonl
│       │   ├── ministries/          # 各部委，一部一个文件
│       │   └── provinces/          # 各省级，一省一个文件
│       └── rss_feeds/              # RSS 地址
│
├── .github/workflows/publish.yml   # 发布到 PyPI
├── pyproject.toml                  # 包配置
└── docs/images/                    # README 用图
```

## 文件格式

所有数据文件都是 **JSONL**（每行一个 JSON 对象，UTF-8，不含注释）。

### 首页

```json
{"name": "工业和信息化部", "url": "https://www.miit.gov.cn", "category": "国务院组成部门"}
{"name": "北京市人民政府", "url": "https://www.beijing.gov.cn", "region": "北京"}
```

### 通知/政策栏目

```json
{"site": "工业和信息化部", "column": "政策文件", "url": "https://www.miit.gov.cn/zwgk/zcwj/", "encoding": "utf-8", "rss": null}
```

| 字段 | 说明 |
|---|---|
| `site` | 站点/机构名称 |
| `column` | 栏目名称 |
| `url` | 栏目页 URL |
| `encoding` | 页面编码，多数 `utf-8` |
| `rss` | 该栏目 RSS 地址，没有则为 `null` |

## 维护方式

- 改完对应 JSONL 文件，commit 后 push 到 `main` 会自动发到 TestPyPI 验证。
- 打 tag `v*` 会自动发到正式 PyPI。
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
