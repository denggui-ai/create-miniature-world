# 安装与更新

仓库、Skill目录和调用标识统一为 `create-miniature-world`。项目展示名是「微缩摄影 Skill · Miniature World」；当前核心的界面配置仍显示「微缩造景」，是同一个Skill。以下沿用已核对的宿主入口，实际加载与生图能力仍需本机确认。

## 获取项目

当前仓库已公开，可以直接克隆或下载ZIP。在本机终端执行：

```bash
git clone https://github.com/denggui-ai/create-miniature-world.git
cd create-miniature-world
```

也可在仓库的 Code 菜单选择 Download ZIP，解压后打开项目。下载或打开仓库不等于安装Skill。唯一安装源是 `skills/create-miniature-world/`，不要把整个仓库复制成一个Skill。

## Codex

在本机Codex打开项目，将这段话交给它：

> 请阅读 docs/INSTALL.md 和 docs/LOCAL_TEST.md。检查是否已有 create-miniature-world 技能，若有则比较版本，不直接覆盖。将 skills/create-miniature-world 安装到本项目的 .agents/skills/create-miniature-world。核对三个核心文件与源目录一致，并在新任务中确认实际加载路径。分别报告能否读本地图、把图传入生图工具、生图、编辑和保存；先不生图，不安装依赖或接入付费服务。

默认建议项目级安装 `.agents/skills/create-miniature-world/`，只在该项目使用。明确需要全局使用时，可选择用户级 `~/.agents/skills/create-miniature-world/`。两者选择其一；遇到云端或旧版同名Skill，确认实际加载的是哪一份。

安装并确认加载后，上传商品照片，发送：

上传的照片和生成提示会交给当前宿主及其图像工具处理；仅上传有权使用、可交给这些服务的内容。本介绍页本身不接收照片或执行生图。

> 使用 $create-miniature-world，把这张商品图做成微缩摄影。先给三个有明显区别的创意，不要立即生图。

支持技能选择的界面中，也可选择当前显示的「微缩造景」。

## Claude Code

在Claude Code打开项目，发送：

> 请阅读 docs/INSTALL.md 和 docs/LOCAL_TEST.md。检查本项目 .claude/skills/create-miniature-world 是否已有技能，若有则比较版本，不直接覆盖。将完整的 skills/create-miniature-world 复制到该目录，核对源与安装副本一致。在新会话确认技能可发现，并分别报告读图、参考图输入、生图、编辑和保存能力；先不生图，不安装依赖或接入付费服务。

默认项目级目录为 `.claude/skills/create-miniature-world/`；明确需要全局使用时，可选择 `~/.claude/skills/create-miniature-world/`。保留同一份源文件，`agents/openai.yaml`为Codex界面配置，不需要为Claude另写创作方法。

安装后上传商品照片，发送：

```text
/create-miniature-world 把这张商品图做成微缩摄影。先给三个有明显区别的创意，不要立即生图。
```

普通Claude网页聊天上传文件，不等于完成Claude Code本机安装。

## 确认安装成功

目录存在不代表加载成功。确认实际加载的 `SKILL.md`、`references/creative-relations.md` 和 `agents/openai.yaml` 与本包一致；然后按[本机验收](LOCAL_TEST.md)完成先看方案、一次出图和一次反馈修改。

Skill不附带生图模型、API密钥或额度。没有生图工具时，可以策划并输出提示词；能够读商品图不代表生图工具能接收该图。工具不足时记录具体阻塞，可由用户在现有图像工具中生成后交回审图，不能记为本机自动生图通过。

## 更新

先检查项目是否有自己的修改。无本地改动时可以 `git pull --ff-only` 更新源码；有改动或分支分歧时先让开发助手比较并处理，不强制覆盖。ZIP用户先下载到新目录再比较。

拉取源码不会自动更新安装副本。比较唯一源目录 `skills/create-miniature-world/` 与实际安装目录，保留自己的改动后再同步，打开新任务确认加载版本。输出保存在项目 `outputs/`，原商品图不要覆盖。

入口资料：[OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills)、[Claude Code Skills](https://code.claude.com/docs/en/skills)。安装路径沿用2026-10-05的文档核对记录，不代表本包已完成两个宿主的本机生图验收。
