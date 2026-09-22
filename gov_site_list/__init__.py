"""gov-site-list: 中国政府网站 URL 清单（静态数据）。

包含中央机构、省级政府、垂直部委的首页与通知/政策栏目 URL。
数据以 JSONL 格式存储，每行一个 JSON 对象。
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterator

__version__ = "0.1.0"

_DATA_DIR = Path(__file__).resolve().parent / "data"


def data_dir() -> Path:
    """返回数据文件所在目录。"""
    return _DATA_DIR


def load_jsonl(rel_path: str) -> Iterator[dict]:
    """按相对路径加载 JSONL 文件，逐行 yield dict。

    rel_path 相对于 data/ 目录，例如 "homepages/central.jsonl"。
    """
    p = _DATA_DIR / rel_path
    if not p.exists():
        raise FileNotFoundError(f"数据文件不存在: {p}")
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def list_jsonl_files() -> list[str]:
    """列出 data/ 下所有 .jsonl 文件（相对路径）。"""
    return sorted(str(p.relative_to(_DATA_DIR)) for p in _DATA_DIR.rglob("*.jsonl"))


def load_homepages() -> list[dict]:
    """加载所有政府网站首页（中央 + 省级）。"""
    rows = []
    for name in ("central.jsonl", "provincial.jsonl"):
        rows.extend(load_jsonl(f"homepages/{name}"))
    return rows


def load_notice_columns() -> list[dict]:
    """加载所有通知/政策栏目（中央 + 部委 + 省级）。"""
    rows = []
    for p in sorted(_DATA_DIR.glob("notice_columns/**/*.jsonl")):
        rel = str(p.relative_to(_DATA_DIR))
        rows.extend(load_jsonl(rel))
    return rows


def load_rss_feeds() -> list[dict]:
    """加载 RSS 订阅地址。"""
    return list(load_jsonl("rss_feeds/rss.jsonl"))


__all__ = [
    "__version__",
    "data_dir",
    "load_jsonl",
    "list_jsonl_files",
    "load_homepages",
    "load_notice_columns",
    "load_rss_feeds",
]
