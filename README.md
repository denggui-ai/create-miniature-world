# 微缩摄影 Skill · Miniature World

**让日常物件，成为有故事的小世界。**

给 Codex 与 Claude Code 用的 AI 微缩摄影 Skill：从物件的形状、纹理和结构里找联想，把它写成一张图卡，再生成画面。受田中达也（Tatsuya Tanaka）的「见立 / mitate」启发。

[介绍页](https://denggui-ai.github.io/create-miniature-world/site/) · [案例图库](https://denggui-ai.github.io/create-miniature-world/site/gallery.html) · [安装说明](docs/INSTALL.md) · [下载最新版](https://github.com/denggui-ai/create-miniature-world/releases/latest) · [English](README.en.md) · [日本語](README.ja.md)

| 笔记本 · 装订圈停车架 | 薯片 · 波纹秋收 | 马克杯 · 咖啡渍跑道 |
| --- | --- | --- |
| <img src="examples/notebook-bike-rack.png" width="260" alt="笔记本装订圈成为微缩自行车停车架"> | <img src="examples/potato-chip-harvest.png" width="260" alt="薯片的金色波纹成为微型收割机作业的田垄"> | <img src="examples/mug-coffee-ring-track-20261012.png" width="260" alt="杯底留下的咖啡渍圈成为孩子们赛跑的跑道"> |
| 装订圈成了停放自行车的车架。 | 金黄的波纹成了秋收的田垄。 | 一圈咖啡渍成了运动会跑道。[看教程](https://denggui-ai.github.io/create-miniature-world/site/coffee-ring.html) |

以上为 AI 成图，展示创意方向；商品保真与已知不足见[案例说明](examples/SELECTED.md)。

## 30 秒开始

**1. 安装**（首次安装、目标目录还不存在时；已有同名 Skill 请先看[安装说明](docs/INSTALL.md)备份与比较）

```bash
git clone https://github.com/denggui-ai/create-miniature-world.git
# Claude Code：复制到你的项目
mkdir -p 你的项目/.claude/skills && cp -R create-miniature-world/skills/create-miniature-world 你的项目/.claude/skills/
# Codex：改用 .agents/skills
mkdir -p 你的项目/.agents/skills && cp -R create-miniature-world/skills/create-miniature-world 你的项目/.agents/skills/
```

只装 `skills/create-miniature-world/` 这一个目录，不要把整个仓库当成 Skill。

**2. 开一个新会话，发一张商品照片和一句话**（没有照片，只说物品名称也行）

| 环境 | 发送 |
| --- | --- |
| Claude Code | `/create-miniature-world 把这张商品图做成微缩摄影。先看方案，不要生图。` |
| Codex | `使用 $create-miniature-world，把这张商品图做成微缩摄影。先看方案，不要生图。` |

**3. 选一个方案**，说「按方案1生成一张，保留商品外观」，看图后再提一处修改。

生图和编辑用的是你所在环境自带的图像工具。Codex/ChatGPT 内置生图已跑通；已测的 Claude Code 环境没有内置生图，会给出方案与提示词，由你拿到已有的图像工具生成后带回来评。本项目不附带模型、API 密钥或生图额度。

## 你可以怎样和它沟通

| 你说什么 | 它会怎样做 |
| --- | --- |
| 创意你来定，直接做一张 | 读物件、比较候选后自己选案，工具可用时生成 |
| 先看方案，不要生图 | 只交图卡（相机在哪、什么巨大、谁小、哪些部位成了什么、发生什么事），等你选 |
| 只给我生图提示词 | 只输出文字，不调用生图 |
| 用我这张实物照直接改 | 先判它能否当底图（机位近而低、物件在画中大、承托面干净、柔光）；能就只添加小人与配件，物件保留 |
| 人物再小一些 | 调整人物及相关道具比例，保护商品 |
| 没看懂这个故事 | 回查物件联系、人物动作和空间关系，必要时换情境 |

有商品照片时默认保护它的可见外观；只有名称时自由创作。画幅默认方幅，你指定的比例优先。每个方案一张首图；编辑只在你点名的那张上做、至多一次；失败不重试、不自动追加。

## 一张图卡，两条制作路线

策划和拍摄写成一张图卡：相机在哪、看见什么；什么巨大；谁小、人高约等于哪个部件；物件哪个部位成了什么、从这个机位凭什么像；正在发生什么事；不加什么。想不出来时，Skill 会在 20 张田中作品的文字案例卡里找同类，借想法的机制，不抄人数、配件和标题。

| | 直接生成 | 编辑实物照 |
| --- | --- | --- |
| 什么时候用 | 只有物件名，或实物照不能当底图 | 有一张能当底图的实物照 |
| 物件 | 由生成器重绘，部件与孔形可能变 | 原照保留，只添加小人与配件 |
| 看图 | 先答两问：在发生什么事；像不像小人在巨大物件的世界里 | 另核对物件有没有被改 |

## 更多案例与教程

- [马克杯 · 咖啡渍跑道](https://denggui-ai.github.io/create-miniature-world/site/coffee-ring.html)：只有物件名称，怎样变成一个故事
- [橘子实拍 → 行星考察](site/orange.html)：比较两个创意，再用一次编辑缩小人物
- [遥控器原照 → 两张成图](examples/REMOTE_CONTROL_TEST_20261014.md)：真实商品参考与保真问题
- [冰格与榨汁器的两次完整取舍](examples/PLANNING_PHOTOGRAPHY_CASES_20261019.md)：候选、机位与布光怎样决定
- [纸巾雪坡、铅笔桥与木夹跳台](docs/SECONDARY_CREATION.md)：从材质、组合和姿态出发
- [作品解读：胶带座为什么能成为跑步机？](docs/ARTWORK_INTERPRETATION.md)：只做文字分析，链接官方原作
- [纸杯入门教程](docs/QUICK_START.md) · [全部案例与复盘](examples/README.md)

## 适用条件与限制

- **适合**从可见的轮廓、纹理、结构或开合关系中找联想的物件；商品照片优先。不能只按「文具」「食品」等品类保证成功，也不会为了故事凭空改变商品结构。
- **商品保真**：标签、文字、部件和尺寸仍可能生成错误，直接生成时尤其明显。创意得到认可，不代表精确还原了某款商品。
- **微缩人偶**：大小按人物与物件部件的关系判断，不猜毫米。包内三张人偶实拍只作造型与涂装参考（[说明与许可](skills/create-miniature-world/assets/figure-refs/README.md)，CC BY-NC 4.0）。
- **本机后期**：只在你点名时做，需要 Python 3、Pillow、NumPy；缺依赖时交原图。
- **已验证与未验证**：每个版本测了什么、没测什么，写在[发布说明](https://github.com/denggui-ai/create-miniature-world/releases)与[验证记录](docs/VALIDATION.md)里。换电脑、跨系统、桌面端自动触发尚未验证，也不宣称稳定成功率。

## 创作启发与致敬

致敬微缩摄影家、见立作家**田中达也**。他的 [MINIATURE CALENDAR](https://miniature-calendar.com/about/) 启发我们重新看见日常物件。本项目把作品学习和自己的试验整理成方法，这些步骤不是作者本人公布的工作流程；案例卡只有文字与作者官网文章页链接，不收录、不转存任何原作图片。人物动作和模型造型可参考 [Preiser 官网](https://www.preiserfiguren.de/)。

本项目与田中达也、MINIATURE CALENDAR、Preiser 及样张中的商品品牌无官方合作或背书关系。代码与自编文档采用 [MIT 许可证](LICENSE)；案例图和第三方素材不自动适用 MIT，见[素材说明](THIRD_PARTY_NOTICES.md)。

## 版本、反馈与维护

当前版本见 [Releases](https://github.com/denggui-ai/create-miniature-world/releases/latest)（含安装包、SHA-256 与发布说明）；需要离线阅读时用[离线用户指南](docs/USER-GUIDE.html)，首次运行可用[本机验收](docs/LOCAL_TEST.md)确认实际能力。

遇到问题请用[反馈模板](https://github.com/denggui-ai/create-miniature-world/issues/new?template=bug_report.md)，写明用的是 Codex 还是 Claude Code、加载的版本、输入、期望与实际结果；只附有权分享的图片，不要贴账号或密钥。维护者见[维护说明](docs/MAINTAINING.md)。核心只维护 `skills/create-miniature-world/` 一份源，安装目录是运行副本。
