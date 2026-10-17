# 安装与更新

先选择安装来源，再选择宿主。仓库、Skill目录和调用标识都是 `create-miniature-world`；下载仓库不会自动安装Skill。

## 选择安装来源

| 来源 | 适用情况 | 注意事项 |
| --- | --- | --- |
| [正式 v0.1.0 安装包](https://github.com/denggui-ai/create-miniature-world/releases/tag/v0.1.0) | 需要固定版本时优先使用 | 下载ZIP和SHA-256文件，按[离线指南](USER-GUIDE.html#install)核验后安装。 |
| 公开仓库 main | 跟进公开文档与教程 | 以v0.1.0为基础，仅修正默认张数矛盾；正式安装包未更新，其他开发运行修订未同步。 |

公开 main 与 v0.1.0 的 Codex 界面显示名都是「微缩造景」；仓库标题「微缩摄影 Skill」是项目介绍，调用标识始终为 `create-miniature-world`。若界面显示其他名称，先核对实际加载来源。开发运行修订未包含在本页安装步骤中。

安装时只复制 `skills/create-miniature-world/` 中的11个运行文件：入口、界面配置、4份参考文档、人偶参考说明和3张照片、后期脚本。源侧 `evals/`、`CHANGELOG.md` 不属于安装范围；不要把整个仓库复制成一个Skill。

已验证同一台Mac上Codex项目级及默认用户级安装、升级、回退和卸载；Claude仅文件级生命周期及既有方案输出。新机器、跨系统、其他用户级位置和Claude新会话仍需分别验证，见[带日期的验证记录](VALIDATION.md)。

[English installation and first-use guide](GETTING_STARTED.en.md)。

## 获取项目

当前仓库已公开，可以直接克隆或下载ZIP。在本机终端执行：

```bash
git clone https://github.com/denggui-ai/create-miniature-world.git
cd create-miniature-world
```

也可在仓库的 Code 菜单选择 Download ZIP，解压后打开项目。下载或打开仓库不等于安装Skill。唯一安装源是 `skills/create-miniature-world/`，不要把整个仓库复制成一个Skill。

## 安装前先检查同名副本

检查所选宿主的项目级和用户级目录，并确认实际发现列表；目录存在、失效符号链接或同名技能已从别处发现时，先记录来源与差异，不覆盖或自动移动。验证用户级安装应使用没有项目级同名副本的独立项目，防止把项目副本的加载误当成用户级成功。已有安装需要更新时，先完整备份到技能发现目录之外。

## 终端直接安装（macOS / Linux，首次项目级安装）

从上述公开仓库或正式包获取文件，在解压/克隆后的仓库根目录运行。需要 Python 3 标准库，无需安装额外依赖。下方默认安装 Codex；Claude Code 用户只将 `host` 改为 `"claude"`，不要两个范围一起安装。

脚本先检查该宿主常见的项目级和用户级同名位置，目录或失效链接存在时均停止；安装目录及其父目录也不能是链接。如果你配置过其他技能搜索位置，先核对宿主实际发现列表。已有安装请转到[更新](#更新)，完整备份并比较，勿删除旧目录来绕过检查。

```bash
python3 - <<'PYINSTALL'
from pathlib import Path
import hashlib
import shutil

host = "codex"  # Claude Code 用户改成 "claude"
name = "create-miniature-world"
if host not in ("codex", "claude"):
    raise SystemExit("host 只能是 codex 或 claude")
roots = [".agents/skills", ".codex/skills"] if host == "codex" else [".claude/skills"]
target = Path(roots[0]) / name
for root in roots:
    for base in (Path.cwd(), Path.home()):
        existing = base / root / name
        if existing.exists() or existing.is_symlink():
            raise SystemExit(f"发现同名目录或链接，停止安装：{existing}")
for parent in target.parents:
    if parent.is_symlink():
        raise SystemExit(f"安装父目录是链接，停止安装：{parent}")
source = Path("skills") / name
ignored = {"evals", "CHANGELOG.md", "__pycache__", ".DS_Store"}
entries = [p for p in source.rglob("*") if not ignored.intersection(p.relative_to(source).parts)]
if not source.is_dir() or source.is_symlink() or any(p.is_symlink() for p in entries):
    raise SystemExit("安装源缺失或含链接，停止安装")
files = [p for p in entries if p.is_file()]
if len(files) != 11:
    raise SystemExit("所选公开版本应有11个运行文件，请先核对安装源")
shutil.copytree(source, target, ignore=shutil.ignore_patterns(*ignored))
for original in files:
    copied = target / original.relative_to(source)
    if hashlib.sha256(original.read_bytes()).digest() != hashlib.sha256(copied.read_bytes()).digest():
        raise SystemExit(f"文件校验未通过：{copied}；先停止，不覆盖重装")
print(f"已复制并核对11个运行文件：{target}；请在新会话确认实际加载路径。")
PYINSTALL
```

以上只复制文件并核对摘要，不启动宿主、不调用模型或生图。打开新会话，先确认实际加载的入口路径，再按下方文字请求试用；文件复制成功不等于宿主加载成功。Windows 安装命令未验证，不直接套用这段命令。

## Codex

在本机Codex打开项目，将这段话交给它：

> 请阅读 docs/INSTALL.md 和 docs/LOCAL_TEST.md。检查是否已有 create-miniature-world 技能，若有则比较版本，不直接覆盖。按v0.1.0的11个运行文件范围，将 skills/create-miniature-world 安装到本项目的 .agents/skills/create-miniature-world，排除源侧evals/CHANGELOG。已有版本先完整备份。核对全部运行文件的SHA-256与源目录一致，并在新任务中确认实际加载路径。分别报告能否读本地图、把图传入生图工具、生图、编辑和保存；先不生图，不安装依赖或接入付费服务。

默认建议项目级安装 `.agents/skills/create-miniature-world/`，只在该项目使用。明确需要全局使用时，可选择用户级 `~/.agents/skills/create-miniature-world/`。两者选择其一；遇到云端或旧版同名Skill，确认实际加载的是哪一份。

安装并确认加载后，上传商品照片，发送：

上传的照片和生成提示会交给当前宿主及其图像工具处理；仅上传有权使用、可交给这些服务的内容。本介绍页本身不接收照片或执行生图。

> 使用 $create-miniature-world，把这张商品图做成微缩摄影。先给三个有明显区别的方案并推荐一个，不要生图。

支持技能选择的 Codex 界面中，公开版显示为「微缩造景」。先看文字方案，选定后明确说「按方案1生成一张，保留商品外观」；公开 main 默认推荐案、次选案各一张，只要一张时请明确指定。v0.1.0 安装包仍有历史矛盾，使用它时明确指定张数。生成与编辑需要实际工具，不承诺未发布的 A/B 选择和诊断流程。

## Claude Code

在Claude Code打开项目，发送：

> 请阅读 docs/INSTALL.md 和 docs/LOCAL_TEST.md。检查本项目 .claude/skills/create-miniature-world 是否已有技能，若有则比较版本，不直接覆盖。已有版本先完整备份；按v0.1.0的11个运行文件范围将 skills/create-miniature-world 复制到该目录，排除源侧evals/CHANGELOG，逐文件核对SHA-256一致。在新会话确认技能可发现，并分别报告读图、参考图输入、生图、编辑和保存能力；先不生图，不安装依赖或接入付费服务。

默认项目级目录为 `.claude/skills/create-miniature-world/`；明确需要全局使用时，可选择 `~/.claude/skills/create-miniature-world/`。保留同一份源文件，`agents/openai.yaml`为Codex界面配置，不需要为Claude另写创作方法。

安装后上传商品照片，发送：

```text
/create-miniature-world 把这张商品图做成微缩摄影。先给三个有明显区别的方案并推荐一个，不要生图。
```

已测 Claude Code 宿主没有内置生图，方案与提示词可在你已有的图像工具使用，再把成图带回评审；不自动接新服务。普通Claude网页聊天上传文件，不等于完成Claude Code本机安装。

## 确认安装成功

目录存在不代表加载成功。核对实际安装的全部11个运行文件与本包一致，并在新会话确认实际读取项目安装入口和参考文件；先用“先给三个方案，不要生图”做文字验证。文字加载通过不等于生图通过。只有用户授权图像调用且工具能力具备时，才按[本机验收](LOCAL_TEST.md)追加参考图生成和指定编辑；不为检查安装自动消耗图像额度。

Skill不附带生图模型、API密钥或额度。没有生图工具时，可以策划并输出提示词；能够读商品图不代表生图工具能接收该图。工具不足时记录具体阻塞，可由用户在现有图像工具中生成后交回审图，不能记为本机自动生图通过。

## 更新

先检查项目是否有自己的修改。无本地改动时可以 `git pull --ff-only` 更新源码；有改动或分支分歧时先让开发助手比较并处理，不强制覆盖。ZIP用户先下载到新目录再比较。

拉取源码不会自动更新安装副本。比较唯一源目录 `skills/create-miniature-world/` 与实际安装目录，保留自己的改动后再同步，打开新任务确认加载版本。输出保存在项目 `outputs/`，原商品图不要覆盖。

## 回退与卸载

2026-10-17已在同一台Mac的独立项目中验证Codex项目级完整生命周期：正式v0.1.0→冻结开发候选→完整回退→卸载，每次切换均核对实际发现/读取；现有安装未动。Claude仅文件级流程通过。另一次同日验证已完成默认用户级位置的公开rc2→v0.1.0→回退→卸载，并恢复现有环境；新机器、跨系统、其他用户级位置与Claude新会话仍未验证。详见[项目级记录](VALIDATION.md#2026-10-17本机独立项目的安装升级回退与卸载)与[用户级记录](VALIDATION.md#2026-10-17本机用户级生命周期验证公开版本)。

更新前完整备份实际安装目录，包括自己添加的文件；备份放在 `.agents/skills/`、`.claude/skills/` 等技能发现目录之外，避免同时发现新旧两份同名技能。准备并核对新副本后再切换，不能靠覆盖复制保证旧文件已移除。

需要回退时，先保留当前安装的完整备份，再恢复更新前的完整目录。逐文件核对恢复结果，在新会话确认实际加载路径、入口和关键参考文件的摘要；界面名称相同不代表版本相同。备份中的本地修改应一并恢复，不能仅拿发布包覆盖后就称回退完成。

卸载时只移除选定范围内的 `create-miniature-world` 安装目录，保留必要备份。不要删除整个 `.agents/skills/` 或 `.claude/skills/`，也不要删除商品原照、`outputs/` 或其他技能。之后在新会话核对该范围已不再发现它；若别处仍有同名安装，报告实际路径，不自动删除。旧会话已加载的上下文不作为卸载是否生效的判据。

入口资料：[OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills)、[Claude Code Skills](https://code.claude.com/docs/en/skills)。安装路径沿用2026-10-05的文档核对记录，文档核对本身不代替实际运行：Codex生成/编辑/保存有已有证据，新会话安装加载已验证；Claude Code仅声明已有方案输出与本轮文件核对，未声明其内置生图通过。
