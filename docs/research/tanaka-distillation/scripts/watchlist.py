#!/usr/bin/env python3
"""Build ../shape-watchlist.md: for the five Owner-named shape classes, the
object classes (curated by Claude from by-object.json) and <=6 posts each to
open by URL for step 2. Images are referenced, never downloaded into the repo.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATALOG = HERE.parent
bo = json.load((CATALOG / "by-object.json").open(encoding="utf-8"))["by_object"]
cls = {it["slug"]: it for it in json.load((HERE / "classified.json").open(encoding="utf-8"))["items"]}
posts = {p["slug"]: p for p in json.load((CATALOG / "posts.json").open(encoding="utf-8")) if isinstance(p, dict) and "slug" in p}

# Claude's curation: keyword hits minus noise (口罩/罐头/易拉罐 are not transparent; 陀螺/钻石 are not spirals)
SHAPES = {
    "螺旋": ["螺丝", "螺栓", "螺母", "弹簧", "蚊香", "卷尺", "开瓶器", "通心粉", "螺丝刀"],
    "链条": ["拉链", "链条", "绳子", "挂锁", "门锁", "书签绳", "跳绳"],
    "网格": ["华夫饼", "键盘", "咖啡滤杯", "蒸笼", "篮子", "筛子", "沥水篮", "铁丝网", "网球拍", "蜘蛛网", "编织物", "游戏棋盘"],
    "球体": ["鸡蛋", "西瓜", "洋葱", "橙子", "珍珠", "气球", "章鱼烧", "高尔夫球", "樱桃", "栗子", "葡萄", "弹珠", "地球仪", "乒乓球拍", "网球", "足球"],
    "透明容器": ["杯子", "玻璃杯", "酒杯", "啤酒杯", "灯泡", "保鲜盒", "塑料瓶", "喷雾瓶", "瓶子", "水壶", "烧杯", "奶瓶", "汽水瓶", "花瓶"],
}
PER_SHAPE = 6


def pick(slugs, k):
    """Prefer high confidence, spread across years."""
    hi = sorted((s for s in slugs if cls[s]["confidence"] == "high"), key=lambda s: s)
    rest = sorted((s for s in slugs if cls[s]["confidence"] != "high"), key=lambda s: s)
    pool = hi + rest
    if len(pool) <= k:
        return pool
    step = len(pool) / k
    return [pool[int(i * step)] for i in range(k)]


def img(slug):
    p = posts.get(slug) or {}
    im = p.get("images") or p.get("image") or []
    if isinstance(im, str):
        im = [im]
    return im[0] if im else ""


out = ["# 五类形状 · 第 2 步看图清单（由 by-object.json 人工筛出；图片按 URL 打开，不入仓库）\n"]
out.append("件数 = 文本分类 high+medium；每类另列未计的 low。每类挑 ≤6 件，优先 high、跨年份。\n")
for shape, classes in SHAPES.items():
    rows = [(c, bo[c]) for c in classes if c in bo]
    total = sum(b["count"] for _, b in rows)
    out.append(f"## {shape}（{len(rows)} 个物件类，{total} 件）\n")
    out.append("| 物件 | 件数 | low 未计 | 常见读成 |")
    out.append("|---|---|---|---|")
    for c, b in rows:
        out.append(f"| {c} | {b['count']} | {b['low_not_counted']} | {'、'.join(b['read_as_top'][:4])} |")
    all_slugs = [s for _, b in rows for s in b["slugs"]]
    # allocate picks proportionally but at least 1 from the top class
    picks = []
    for c, b in rows:
        if len(picks) >= PER_SHAPE:
            break
        share = max(1, round(PER_SHAPE * b["count"] / max(total, 1)))
        picks.extend((c, s) for s in pick(b["slugs"], share))
    picks = picks[:PER_SHAPE]
    out.append(f"\n看图 {len(picks)} 件：\n")
    out.append("| slug | 物件 | 标题 | 说明 | 文本读成 | 图 |")
    out.append("|---|---|---|---|---|---|")
    for c, s in picks:
        it = cls[s]
        p = posts.get(s, {})
        cap = (p.get("caption") or "").replace("|", "｜").replace("\n", " ")[:60]
        out.append(f"| {s} | {c} | {it['title']} | {cap} | {it.get('read_as','')} | {img(s)} |")
    out.append("")
(CATALOG / "shape-watchlist.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("written", CATALOG / "shape-watchlist.md")
