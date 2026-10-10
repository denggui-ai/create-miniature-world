# 田中达也按物件类型蒸馏 · 成果快照（2026-10-10）

本目录是研究成果的**可跟踪快照**，供接手者阅读与复跑；运行时的工作目录在本机 `outputs/tanaka-catalog/`（.gitignore 内，含官网目录快照 posts.json／posts.tsv、逐篇分类 full/classified.json、三模型原始输出等，不随仓库分发；图片从未入库）。文内引用的 `outputs/...` 路径均指该本机目录。

## 文件
| 文件 | 内容 | 对应交接步骤 |
|---|---|---|
| `model-bench.md` | 60 篇样本 × 3 个 Codex 模型分类基准、全量运行实录、质量偏移证据 | 第 1 步 |
| `by-object-summary.md` | 5171 篇按主物件归类的摘要（1284 类、计数口径、待定 780 篇） | 第 1 步 |
| `shape-watchlist.md` | 五类形状（螺旋／链条／网格／球体／透明容器）对应物件类与每类 6 件看图清单（含原图 URL） | 第 2 步 |
| `five-shapes-from-catalog.md` | 30 件实看条目：画面观察／作者文字／推断，五节规律，文本分类纠错 | 第 2 步 |
| `product-type-to-approach.md` | 产品类型→田中做法→本项目模板→词典行，可信度 ★☆○（v1，已被 v2 取代，留作追溯） | 第 3 步 |
| `distillation-logic-audit-fable.md` | Fable 子代理独立审计原文＋逐条回应（裁决"修正后继续"） | 审计 |
| `scene-first-dictionary.md` | 场景优先词典 v2.1（L3，含第二批更新）：场景主键、尺度区间、可动等级、n／独立物件、状态规则、负例库、商品反查索引 | 审计修正 |
| `product-type-to-approach-v2.md` | 查表 v2（L4）：按可动等级 0/1/2 过滤，电商主类覆盖 | 审计修正 |
| `validation-protocol-v2.md` | 验证协议 v2：G1 flash 方案审→G2 flash 看图盲读→G3 Owner 盲判；入词典门槛 | 审计修正 |
| `l2-coding-template.md` | 逐张编码模板：A 读法槽位／B 拍摄／C 盲读提示／D 分歧处理／E 汇总 | 第二批起 |
| `batch2-coding.md` | 第二批 30 张逐张编码（unresolved 780 篇按年分层抽样）＋与 flash 盲读的一致率 | 第二批 |
| `batch2-agreement.tsv` | 第二批逐张 read_as／moment 两编码者对照与场景行归属 | 第二批 |
| `scripts/` | 抽样、跑分类、比对、归并汇总、看图清单（watchlist 第一批／watchlist2 第二批）、存档、看图盲读脚本（Codex CLI effort low；DeepSeek flash） | 复跑 |

脚本按相对路径找数据，复跑前须放回原位：bench 组→`outputs/tanaka-catalog/bench/`，run_full/aggregate/watchlist/watchlist2→`outputs/tanaka-catalog/full/`，fetch_archive→`outputs/tanaka-archive/`，ds_vision→`outputs/validation/`，run_blind.sh/ready.sh/prompt-c.txt→`outputs/validation/batch2/`。

## 结论摘要
- 模型：gpt-5.6-terra 质量最好，gpt-6-astra 偏保守可互校，gpt-6-luna 不合格（不写"无法判断"、编抽象类）。
- 文本分类有天花板：2012–2014 年说明多为对白，约 15% 篇目要看图；两模型交叉后仍 780 篇待定。件数是下限。
- 形状名不是读法入口：30 件里螺纹／网眼／透明度只有 6 件参与；入口是**摆法 × 切法 × 数量**（平放／竖放／横放；整只／切片／楔块；单个／一堆／散开）。
- 最可复刻的两条：凹格＝池／坑（华夫饼→冰格、蛋托）；浅圆容器＝赛场／浴池（蒸笼、盃、盖）。
- 第二批（780 篇待定项按年抽 30）：Claude 与 flash read_as 一致 26/30、moment 21/30；五类形状规律可检验的 14 次中 13 次符合（透明容器有 1 个反例，螺旋未出现）；词典升候选 3 行（下雪、划艇限等级 2、新建楼房；水面三件合并后又拆回假设）。

## 边界
- 未改 Skill。★ 读法要先过"新物件二选一（带条目 vs 不带）"再由 Owner 授权写入 `references/creative-relations.md`；○ 行只是文本线索，不得入词典。
- 版权归田中达也；目录与原图仅作私有研究索引，不公开、不再分发。
