# 微缩摄影 Skill · Miniature World

**让日常物件，成为有故事的小世界。**

给 Codex 与 Claude Code 用的 AI 微缩摄影 Skill：从物件的形状、纹理和结构里找联想，先把画面想清楚，再生成。受田中达也（Tatsuya Tanaka）的「见立 / mitate」启发。

[介绍页](https://denggui-ai.github.io/create-miniature-world/site/) · [案例图库](https://denggui-ai.github.io/create-miniature-world/site/gallery.html) · [安装说明](docs/INSTALL.md) · [下载最新版](https://github.com/denggui-ai/create-miniature-world/releases/latest) · [English](README.en.md) · [日本語](README.ja.md)

| 回形针 · 跨栏赛 | 刨丝器 · 果岭推杆 | 剪刀 · 柄环接力 |
| --- | --- | --- |
| <img src="examples/paperclip-hurdles-20261020.png" width="260" alt="三枚立起的回形针成了跨栏，小跑者腾空跨栏"> | <img src="examples/grater-golf-20261020.png" width="260" alt="仰放的刨丝器大孔面成了高尔夫果岭，球手推杆进洞"> | <img src="examples/scissors-handle-relay-20261021.png" width="260" alt="剪刀黑色柄环成了环形跑道，小跑者接力"> |
| 跨栏决赛，领跑的已经腾空过栏。 | 球手正在推杆，球童在一旁看。 | 柄环跑道上的接力赛，冲向终点。 |

AI 生成，每张只生成 1 次。创作过程见[案例记录](examples/PICTURE_CARD_CASES_20261021.md)；更多看[案例图库](https://denggui-ai.github.io/create-miniature-world/site/gallery.html)。

## 从第一个文字方案开始

先准备 Codex 或 Claude Code。这个项目是给 Agent 读取的创作 Skill，介绍页用于看案例，不是在线生图工具。**没有照片也能试用；先看方案不会调用生图工具。**

**1. 安装到你使用的一个宿主**

从[最新版 Release](https://github.com/denggui-ai/create-miniature-world/releases/latest)下载附带的 Skill 安装包与校验文件，按[安装说明](docs/INSTALL.md)核验并解压。找到包含 `SKILL.md` 的 `create-miniature-world` 文件夹；源码中的对应位置是 `skills/create-miniature-world/`。

| 你使用的宿主 | 首次项目级安装位置 | 详细步骤 |
| --- | --- | --- |
| Codex | `你的项目/.agents/skills/create-miniature-world/` | [Codex 安装](docs/INSTALL.md#codex) |
| Claude Code | `你的项目/.claude/skills/create-miniature-world/` | [Claude Code 安装](docs/INSTALL.md#claude-code) |

只选你使用的一行，完整安装 Skill 文件夹，不要只复制 `SKILL.md` 或整个仓库。已有同名副本时先[备份与比较](docs/INSTALL.md#更新)，不要直接覆盖。打开新会话，确认宿主实际加载了这份 Skill；文件复制成功不等于已加载。

**2. 不用照片，先复制一句话**

| 环境 | 发送 |
| --- | --- |
| Claude Code | `/create-miniature-world 用一个普通马克杯设计微缩摄影。先给我两个文字方案，不要生成图片。` |
| Codex | `使用 $create-miniature-world，用一个普通马克杯设计微缩摄影。先给我两个文字方案，不要生成图片。` |

你应该先看到文字方案：马克杯的哪部分变成什么、谁在做什么、相机从哪里看。此时还没有成图。若没加载 Skill，回到[安装检查](docs/INSTALL.md#确认安装成功)；若先出了图，记录问题并反馈。

**3. 选一个方案，再生成一张**

有可用生图工具时，发送「按方案1生成一张」。没有生图工具时，发送「只给方案1的完整生图提示词，不要生成」，拿到你已有的图像工具中使用。之后可以换成自己的商品照片，并明确要保留的外观。

生成和编辑取决于当前宿主实际提供的图像工具；并非每个 Codex 或 Claude Code 环境都能出图。本项目不附带模型、API 密钥或生图额度。已有验证范围见[记录](docs/VALIDATION.md)。

做完后，用一句话描述“这是什么场景”，再决定是否修改。愿意分享试用结果，可以填[首次体验反馈](https://github.com/denggui-ai/create-miniature-world/issues/new?template=first_use.md)；卡在安装或没有生图工具也欢迎记录。

## 你可以怎样和它沟通

| 你说什么 | 它会怎样做 |
| --- | --- |
| 创意你来定，直接做一张 | 读物件、比较候选后自己选案，工具可用时生成 |
| 先看方案，不要生图 | 只用文字讲清每个方案：相机放在哪、谁在做什么、物件的哪个部分成了什么，等你选 |
| 只给我生图提示词 | 只输出文字，不调用生图 |
| 用我这张实物照直接改 | 照片贴近桌面、物件拍得够大、背景干净时，保留原照，只添加小人和道具 |
| 人物再小一些 | 调整人物及相关道具比例，保护商品 |
| 没看懂这个故事 | 回查物件联系、人物动作和空间关系，必要时换情境 |

有商品照片时默认保护它的可见外观；只有名称时自由创作。画幅默认方幅，你指定的比例优先。每个方案一张首图；编辑只在你点名的那张上做、至多一次；失败不重试、不自动追加。

## 它怎么想创意

先把画面想清楚再动手：相机放在哪，什么显得巨大，小人有多小（比如“人高约等于一个孔”），物件的哪个部分成了什么，正在发生什么事。想不出来时，它会翻 20 张田中达也作品的文字案例卡找同类，借想法，不抄画面。

出图有两种方式：只有物件名称时，整张画面直接生成；有一张贴近桌面、物件拍得够大的实物照时，保留原照，只在上面添加小人和道具。成图后它只问你一句“这是什么场景”，你一眼读出的故事就是检验。

## 更多案例与教程

- [马克杯 · 咖啡渍跑道](https://denggui-ai.github.io/create-miniature-world/site/coffee-ring.html)：只有物件名称，怎样变成一个故事
- [橘子实拍 → 行星考察](site/orange.html)：比较两个创意，再用一次编辑缩小人物
- [遥控器原照 → 两张成图](https://denggui-ai.github.io/create-miniature-world/site/remote-control.html)：上传一张实拍照片，变成两个小世界
- [冰格与榨汁器的两次完整取舍](examples/PLANNING_PHOTOGRAPHY_CASES_20261019.md)：候选、机位与布光怎样决定
- [纸巾雪坡、铅笔桥与木夹跳台](docs/SECONDARY_CREATION.md)：从材质、组合和姿态出发
- [作品解读：胶带座为什么能成为跑步机？](docs/ARTWORK_INTERPRETATION.md)：只做文字分析，链接官方原作
- [纸杯三案复盘：怎样看图选案](docs/QUICK_START.md) · [全部案例与复盘](examples/README.md)

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

想介绍或收录这个项目？这里有[中英文项目简介、案例入口与收录说明](docs/SHARING.md)。
