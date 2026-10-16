# 安装与更新

仓库、Skill目录和调用标识统一为 `create-miniature-world`。项目展示名是「微缩摄影 Skill · Miniature World」；当前开发源码的界面配置显示「微缩摄影 Skill」，正式包仍显示「微缩造景」，是同一个Skill。以下沿用已核对的宿主入口；新环境的实际加载与图像能力需分别确认。

当前版本为已正式发布的 **v0.1.0**，可从[Release页](https://github.com/denggui-ai/create-miniature-world/releases/tag/v0.1.0)获取专用ZIP和SHA-256校验文件；先按[离线指南](USER-GUIDE.html#install)核验，再安装。2026-10-14本项目两安装副本的11个运行文件已与源码/正式包一致，新Codex会话实际加载并完成文字验证；Claude Code本轮只核对文件，方案输出沿用2026-10-09验收。另一台新机或其他宿主仍需分别确认实际加载与工具能力。

v0.1.0安装范围为 `SKILL.md`、`agents/openai.yaml`、4份 `references/`、`assets/figure-refs/` 的说明及3张照片、`scripts/photo_finish.py`，共11个运行文件。专用包的 `skills/create-miniature-world/` 已按此范围整理；从开发源码安装时排除源侧 `evals/` 和 `CHANGELOG.md`。这些开发证据保留在源码，不复制到安装副本。

> **维护状态（2026-10-16核对）：** 本地源码已修改 A/B 流程、比例判断、人偶与后期；两个项目安装副本各11个运行文件均与当前源码一致。公开 main 的运行文本与正式 v0.1.0 包仍是维护前版本。上段“源码/正式包一致”是此前验证记录。安装时先确认所选来源，不把本地源码、公开主干与正式包当成同一版本。

| 对象 | 本次只读核对结果 |
| --- | --- |
| 本地源码 | 当前维护的唯一源 `skills/create-miniature-world/`。 |
| 两个项目安装副本 | Codex 与 Claude Code 各11个运行文件与当前源码逐字节一致；本次未安装或启动新会话。 |
| 公开 main | 本次核查提交为 `03ce0d4`；已核对的8个运行文本文件与 v0.1.0 标签一致，尚未包含本地 A/B 等维护修订。 |
| 正式 v0.1.0 | 远端仍为正式非草稿发布。现有本地下载ZIP的 SHA-256 与远端附件摘要一致；其11个运行文件中7个与当前源码不同，保持发布时快照。 |

[English installation and first-use guide](GETTING_STARTED.en.md)。本轮仅同步教程与文档，未同步Skill运行维护，也不更新Release。

## 获取项目

当前仓库已公开，可以直接克隆或下载ZIP。在本机终端执行：

```bash
git clone https://github.com/denggui-ai/create-miniature-world.git
cd create-miniature-world
```

也可在仓库的 Code 菜单选择 Download ZIP，解压后打开项目。下载或打开仓库不等于安装Skill。唯一安装源是 `skills/create-miniature-world/`，不要把整个仓库复制成一个Skill。

## Codex

在本机Codex打开项目，将这段话交给它：

> 请阅读 docs/INSTALL.md 和 docs/LOCAL_TEST.md。检查是否已有 create-miniature-world 技能，若有则比较版本，不直接覆盖。按v0.1.0的11个运行文件范围，将 skills/create-miniature-world 安装到本项目的 .agents/skills/create-miniature-world，排除源侧evals/CHANGELOG。已有版本先完整备份。核对全部运行文件的SHA-256与源目录一致，并在新任务中确认实际加载路径。分别报告能否读本地图、把图传入生图工具、生图、编辑和保存；先不生图，不安装依赖或接入付费服务。

默认建议项目级安装 `.agents/skills/create-miniature-world/`，只在该项目使用。明确需要全局使用时，可选择用户级 `~/.agents/skills/create-miniature-world/`。两者选择其一；遇到云端或旧版同名Skill，确认实际加载的是哪一份。

安装并确认加载后，上传商品照片，发送：

上传的照片和生成提示会交给当前宿主及其图像工具处理；仅上传有权使用、可交给这些服务的内容。本介绍页本身不接收照片或执行生图。

> 使用 $create-miniature-world，把这张商品图做成微缩摄影，创意由你决定，给我两个不同且成立的创意各一张。

支持技能选择的界面中，也可选择「微缩摄影 Skill」（正式包仍为「微缩造景」）。以下为当前开发源码的交互，正式 v0.1.0 和公开 main 尚未包含全部修订，使用前确认加载来源。开发版默认 A/B 各一张，指定创意先一张，只有一案成立不凑数；收到图后选一张或直接反馈，选后才编辑，整轮共享一次预算。两案都不喜欢时先诊断，明确要求新方向后再生成。加「先给三个方案，不要生图」可先看文字。

## Claude Code

在Claude Code打开项目，发送：

> 请阅读 docs/INSTALL.md 和 docs/LOCAL_TEST.md。检查本项目 .claude/skills/create-miniature-world 是否已有技能，若有则比较版本，不直接覆盖。已有版本先完整备份；按v0.1.0的11个运行文件范围将 skills/create-miniature-world 复制到该目录，排除源侧evals/CHANGELOG，逐文件核对SHA-256一致。在新会话确认技能可发现，并分别报告读图、参考图输入、生图、编辑和保存能力；先不生图，不安装依赖或接入付费服务。

默认项目级目录为 `.claude/skills/create-miniature-world/`；明确需要全局使用时，可选择 `~/.claude/skills/create-miniature-world/`。保留同一份源文件，`agents/openai.yaml`为Codex界面配置，不需要为Claude另写创作方法。

安装后上传商品照片，发送：

```text
/create-miniature-world 把这张商品图做成微缩摄影，给我两个不同且成立的创意；没有生图工具就给对应提示词。
```

已测 Claude Code 宿主没有内置生图，方案与提示词可在你已有的图像工具使用，再把成图带回评审；不自动接新服务。普通Claude网页聊天上传文件，不等于完成Claude Code本机安装。

## 确认安装成功

目录存在不代表加载成功。核对实际安装的全部11个运行文件与本包一致，并在新会话确认实际读取项目安装入口和参考文件；先用“先给三个方案，不要生图”做文字验证。文字加载通过不等于生图通过。只有用户授权图像调用且工具能力具备时，才按[本机验收](LOCAL_TEST.md)追加参考图生成和指定编辑；不为检查安装自动消耗图像额度。

Skill不附带生图模型、API密钥或额度。没有生图工具时，可以策划并输出提示词；能够读商品图不代表生图工具能接收该图。工具不足时记录具体阻塞，可由用户在现有图像工具中生成后交回审图，不能记为本机自动生图通过。

## 更新

先检查项目是否有自己的修改。无本地改动时可以 `git pull --ff-only` 更新源码；有改动或分支分歧时先让开发助手比较并处理，不强制覆盖。ZIP用户先下载到新目录再比较。

拉取源码不会自动更新安装副本。比较唯一源目录 `skills/create-miniature-world/` 与实际安装目录，保留自己的改动后再同步，打开新任务确认加载版本。输出保存在项目 `outputs/`，原商品图不要覆盖。

## 回退与卸载

2026-10-17已在同一台Mac的独立项目中验证Codex项目级完整生命周期：正式v0.1.0→冻结开发候选→完整回退→卸载，每次切换均核对实际发现/读取；现有安装未动。Claude仅文件级流程通过。此结论不覆盖用户级安装、新机器、跨系统或Claude新会话，详见[验证记录](VALIDATION.md#2026-10-17本机独立项目的安装升级回退与卸载)。

更新前完整备份实际安装目录，包括自己添加的文件；备份放在 `.agents/skills/`、`.claude/skills/` 等技能发现目录之外，避免同时发现新旧两份同名技能。准备并核对新副本后再切换，不能靠覆盖复制保证旧文件已移除。

需要回退时，先保留当前安装的完整备份，再恢复更新前的完整目录。逐文件核对恢复结果，在新会话确认实际加载路径、入口和关键参考文件的摘要；界面名称相同不代表版本相同。备份中的本地修改应一并恢复，不能仅拿发布包覆盖后就称回退完成。

卸载时只移除选定范围内的 `create-miniature-world` 安装目录，保留必要备份。不要删除整个 `.agents/skills/` 或 `.claude/skills/`，也不要删除商品原照、`outputs/` 或其他技能。之后在新会话核对该范围已不再发现它；若别处仍有同名安装，报告实际路径，不自动删除。旧会话已加载的上下文不作为卸载是否生效的判据。

入口资料：[OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills)、[Claude Code Skills](https://code.claude.com/docs/en/skills)。安装路径沿用2026-10-05的文档核对记录，文档核对本身不代替实际运行：Codex生成/编辑/保存有已有证据，新会话安装加载已验证；Claude Code仅声明已有方案输出与本轮文件核对，未声明其内置生图通过。
