# 给Codex与Claude的开发交接

## 当前状态（2026-10-09）

- 2026-10-09 已在 `f521e28` 创建 pre-release `v0.1.0-rc2`（[Release 页](https://github.com/denggui-ai/create-miniature-world/releases/tag/v0.1.0-rc2)）；版本仍为实验候选，site 页保留 noindex，正式版 v0.1.0 未发布。
- 唯一核心源 `skills/create-miniature-world/`；项目 Codex 安装副本 `.agents/skills/` 与 Claude Code 安装副本 `.claude/skills/` 三文件均与源码逐字节一致（两目录均被 .gitignore 覆盖）。
- 2026-10-09 完成一次全项目独立审计（报告在本机 `outputs/claude-project-audit-20261009/report/`，私有目录，不随仓库分发）。当日据此改动：reference 加牙刷对照 6 行（`709edeb`）；SKILL.md 三句（`f063453` 提示约 200 词、保留项肯定句、道具风格词；`cfc7c8c` 自动修正只限结构性错误、小商品改按人物占商品长度描述）；木夹跳台教程（`f27879e`）。
- E1 画面安排对照（6 图、3 次二选一）：牙刷选 A、毛巾选 B、笔袋都不好。"摆放优先"作为通则不成立，选情境段未改。
- 2026-10-10 创意策划根因分析（本机 `outputs/claude-project-audit-20261009/report/CREATIVE_PLANNING_ANALYSIS.md`，四次用户二选一实验 22 图）：根因是选情境段只写了"小人借用物件"一种见立模式；剪刀借用模式 0/6、变身模式 3/3。据此 Owner 授权改 SKILL.md 两处：选情境段第 6 句改为"三候选里至少一条走变身……其余候选走借用……"；出图段背景句改为"默认纯色卡纸，实景只在用户要求时使用"（用户指出田中用卡纸不用实景，五件剪刀原作核实）。两处安装副本已同步（SHA-256 `389e1880…`）。
- 2026-10-10 第二次改动（实验五、六后，Owner 授权）：选情境段加推荐依据"推荐案选不听解释、第一眼就能懂小人在干什么、物件是什么或成了什么的那条，要先理解一个机制才懂的放在次选"；默认改为推荐案与次选案各生成一张交用户挑选（六次实验策划端自荐命中 6/13）；看图段预算句同步改为两张初始生成、修正仍至多一次。安装副本已同步（SHA-256 `709af2f6…`）。
- 2026-10-10 第三次改动（实验七后，Owner 授权）：reference 新增"形状词典"节（13 类形状特征→读法／日常事／再加的一样东西／来源／备注，替换原六行关系表），SKILL 选情境段末改为"选案前先拆形状特征查词典"。证据：长尾夹二选一，带词典一路自荐中、认可 2 张，不带一路自荐不中、认可 1 张；词典全文与本项目裁决在本机 `outputs/claude-project-audit-20261009/research/shape-reading-dictionary.md`。安装副本已同步（SKILL `4586757a…`、reference `74289307…`）。未验证：哪些物件该推荐变身案、哪些该推荐借用案；策划端自荐排序仍不可靠；本 Skill 无 evals/CHANGELOG，改动记录以本条和分析报告为准。
- 2026-10-10 第四次改动（Owner 逐条授权，研究线第三会话）：reference 形状词典"单个环／圆筒／筒腔"行删去"街机"读法与来源 210822（分析报告 §17）；SKILL 生图能力段加"田中达也原作图片只用于读法比对，不作为生图参考图传入，用户提供时说明原因"。安装副本已同步（SKILL `20c6f911…`、reference `f472882a…`）；quick_validate 通过；check_skill_standard --strict 仍报既有缺口（无 evals、无 CHANGELOG、DoD 不清），本次未补。未改动："多件并置"行仍引 210822 作"街机厅"，不在本次授权内，待核查原图。
- 2026-10-10 田中达也按物件类型蒸馏（研究，未改 Skill）：官网 5906 篇目录快照→Codex gpt-5.6-terra 文本分类 5171 篇（1284 类，计 4441 篇，待定 780 篇；三模型基准与全量质量偏移见报告）→五类形状各看 6 件原图→产品类型查表草案。成果快照在 [docs/research/tanaka-distillation/](research/tanaka-distillation/README.md)；原始目录、逐篇分类与图片只在本机 `outputs/tanaka-catalog/`，不入库。同日 Fable 独立审计后重排为场景优先词典 v2、查表 v2（商品可动等级 0/1/2 过滤）与验证协议 v2（G1 DeepSeek flash 方案审→G2 flash 看图盲读→G3 Owner 盲判；入词典门槛 n≥3、独立物件≥2、G2 通过、Owner 授权）；DeepSeek MCP `deepseek_chat` 已加 `image_path` 看图（claude-tools `eb9a6d7`）；作品图片按 Owner 授权私有存档于本机 `outputs/tanaka-archive/`（不分发、不上传），已取 117 张暂停。待 Owner 逐次授权：形状词典 B 行删"街机／210822"；写入"田中作品图片不作生图参考图"边界。五类形状规律目前为假设，复现前不入 Skill。 同日第二批 30 张（从 780 篇待定项按年抽，Claude＋flash 双编码）：五类规律可检验 14 次 13 次符合；词典 v2.1 升候选 3 行（水面行合并后拆回假设），见 [batch2-coding.md](research/tanaka-distillation/batch2-coding.md)；仍未改 Skill。
- 验证状态（差分）：

| 项 | 状态 | 证据 |
| --- | --- | --- |
| Codex/ChatGPT：参考图生成 + 用户点名的一次编辑 + 保存 | 已跑通 | [LOCAL_TEST 结果表](LOCAL_TEST.md)、[LOCAL_AUDIT](LOCAL_AUDIT_2026-10-05.md)、`examples/clothespin-diving-*` |
| Claude Code：安装、自动发现、方案输出 | 已验收（2026-10-09，项目级 `.claude/skills/` 安装；新会话显式调用读图并出三方案，未生图）；该宿主无内置生图，出图需人工接力；冷启动自然语言触发未单测 | [LOCAL_TEST 结果表](LOCAL_TEST.md) |
| 任一样张的严格商品保真 | 未通过 | 各案记录与 THIRD_PARTY_NOTICES |
| 自动化视觉测试 | 不存在；历史脚本只查结构与链接 | — |

- 挂起、不排期：Claude Code 冷启动自然语言触发单测；正式 Release（条件见 [PUBLISH](PUBLISH.md)）；解除 noindex 前的手机真机检查；学习复刻 230808／170704／130724、OXO v2、香皂加人等待用户评价；精确 Preiser 型号与物理比例认证不做。
- 已结束、不重开：木梳 10-06 迁移、胶带穿环、杯沿跑圈、MUJI／U 款滚筒重生、热水袋、笔袋货船概念、背景／承托面实验。
- 2026-10-05 至 10-08 的发布、研究、案例轮次与网站设计决策已原样移至 [DEVELOPMENT_HANDOFF_HISTORY.md](DEVELOPMENT_HANDOFF_HISTORY.md)，只作追溯，不是新指令。

<a id="项目规划唯一当前待办入口"></a>

## 项目规划（唯一当前待办入口）

按 2026-10-09 审计给出的顺序：文档收口（已完成）→ Claude Code 安装验证（已完成，方案输出层面）→ Release 决定（已决定：保持 rc2，发 pre-release；正式版待四维全过样张）。不扩大研究、不加规则、不建测试平台。创意方法的改动只在有用户二选一证据时进行（E1／E3 的做法）。

## 阅读顺序与修改位置

1. [README.md](../README.md)：范围、使用方式和素材边界。
2. [SKILL.md](../skills/create-miniature-world/SKILL.md)：当前实际流程。
3. [创意关系参考](../skills/create-miniature-world/references/creative-relations.md)：已有方法、反例、来源和迁移限制；接手时读一遍，日常执行按需读相关段。
4. [VALIDATION.md](VALIDATION.md)、[LOCAL_TEST.md](LOCAL_TEST.md)：已做什么、下一步怎么验收。
5. [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md)：素材分发边界；发布前再读[PUBLISH.md](PUBLISH.md)。

只在 `skills/create-miniature-world/` 修改核心。`CLAUDE.md`是开发交接入口，不要把其开发流程塞进每次生图提示。没有构建项目或依赖安装步骤；当前不需要搭建服务、数据库、状态机、测试平台或新插件。

## Claude接手与Skill安装是两件事

Codex先读根目录AGENTS.md，其安装与调用按README执行。两种宿主都使用同一份核心源；本节只说明Claude的入口差异，后续的证据边界和首轮任务对两者都适用。

Claude Code可以先直接阅读这些文件开展开发，不必先安装Skill。需要测试自动发现与调用时，再把完整 `skills/create-miniature-world/` 复制到本项目的 `.claude/skills/create-miniature-world/`；已有同名目录或链接先比较，不覆盖。选择项目级安装可避免影响其他项目。若用户明确希望全局使用，官方用户级路径为 `~/.claude/skills/create-miniature-world/`。

Claude Code的调用形式是 `/create-miniature-world`，不是Codex示例中的 `$create-miniature-world`。`agents/openai.yaml`保留给Codex，不需要为Claude另写一份创作方法；实际能力和权限以Claude会话为准。安装后比对源与运行副本，并确认确实加载了本包；不能仅凭目录存在就判安装发现成功。

以上位置与调用形式来自[Claude Code官方Skills文档](https://code.claude.com/docs/en/skills)，项目入口方式参考[官方CLAUDE.md文档](https://code.claude.com/docs/en/memory)，2026-10-05核对。官方文档核对不代表本包已完成Claude实际运行验证。

如果用的是普通Claude聊天界面，可提供这些文档和图片做分析；不要把上传资料等同于本机安装或源码修改。要继续改项目文件与验证本机流程，使用能访问项目目录的开发环境。

## 先核对工具，再决定怎样测试

分别确认：读取本地商品图、把图片实际传入生图工具、生成、编辑指定成图、查看结果、保存文件。Claude接手代码不会自动获得原ChatGPT会话的图片工具、额度、登录状态或历史附件。

| 实际能力 | 本轮能做什么 | 不能据此宣称什么 |
| --- | --- | --- |
| 读图与文字策划 | 识别商品、三选案、输出提示词、审查用户返回的图片 | 已生图或完成端到端自动化 |
| 只有文字生图 | 用户明确接受时可做自由创作概念；严格商品保真任务先保留方案 | 商品参考图已输入或准确恢复标签 |
| 支持参考图的生成 | 生成商品方案并看图判断；记录实际输入 | 已具备编辑能力或所有商品均保真 |
| 参考图生成、编辑和结果保存均可用 | 按LOCAL_TEST跑一次完整闭环 | 成图必然好看、故事必然被看懂 |

没有合适的图像工具时，继续做方案和提示词即可。可以由用户在现有生图工具里生成并将结果交回审图；记录为人工接力，不记为本机自动生图通过。不要为通过验收擅自接付费API、账号或浏览器。若后续决定新增图像执行渠道，只围绕实际需要做最小连接，不先造通用适配层。

## 必须继承的反馈与判断边界

- 回形针曾被误认成水管：先保住物件识别线索，再判断故事；后续图获认可不等于所有回形针题材通过。
- 修正带放映曾有空间位置错误：题材逻辑通顺仍需核查真实画面中的朝向、接触、路径和承托。
- 人偶多次偏大、像玩偶：需要同时检查雕塑造型、人物相对商品的大小及景别。拉远不等于相对缩小；品牌词不能代替实物参考。1:64是项目规划值，不是作者或Preiser的统一比例。
- 便利贴需要仍像纸叠，盖被关系要在图中显现；认可的复刻不证明独立联想有效。
- 剪刀冰场被用户否定；眼镜镜片是用户提出的候选，并未因此验证。斜面不必硬套滑冰，先回到物件结构重新选情境。
- 用户说“不错”“有意思”只支持对应样张或创意；不自动代表商品标签、尺寸、型号与其他画面细节通过。

更完整的历史边界见参考文件与[案例摘要](../examples/README.md)。这里是交接摘要，不是本轮实际看图结论。

## 给接手开发者的启动指令

> 先读AGENTS.md（Claude读CLAUDE.md）及本页「当前状态」，核对 HEAD、安装副本哈希与实际工具能力，再按「项目规划」接续。保持一份核心源、保留原件，不安装新依赖或接付费服务，不因接手自动提交或发布。历史轮次见 DEVELOPMENT_HANDOFF_HISTORY.md，不重开。

