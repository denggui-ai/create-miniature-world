# 田中达也作品图片私有存档（研究用）

## 治理规则
- **用途**：仅供本项目私有研究（创意读法与拍摄手法分析）。版权归田中达也（MINIATURE CALENDAR / Tatsuya Tanaka）。
- **不分发**：不上传 GitHub、不打包分享、不进任何公开或半公开位置；不作为训练数据，不用于生成图的参考图输入。
- **位置**：`outputs/tanaka-archive/`，受仓库根 `.gitignore` 的 `outputs/` 规则覆盖；本目录另有 `.gitignore` 兜底（`*`）。
- **命名**：`images/<YYYY>/<slug>.jpg` 为每篇第一张；多图篇目第 n 张为 `<slug>-n.jpg`。slug 即官网六位日期，可直接对应 `tanaka-catalog/posts.tsv` 和 `by-object.json`。
- **清单**：`manifest.tsv`（slug / date / idx / url / file / bytes / sha256 / status）是唯一事实来源；status 非 `ok` 的行可重跑脚本补取。
- **获取方式**：`fetch_archive.py`，公开 URL，单线程，每 0.6 s 一请求，失败重试 3 次；可断点续跑。默认只取每篇第一张（`--all` 取全部）。
- **引用方式**：分析文档只写 slug（如 `150820`），不复制图片到文档目录；要看图就按 slug 打开本目录文件。
- **删除**：Owner 决定不再研究时整目录删除即可，仓库无任何引用依赖。

## 规模（2026-10-10 估算）
日更作品 5221 篇，图片共 7228 张；第一张合计约 1.3 GB，全部约 1.8 GB。
