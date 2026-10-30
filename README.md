# Miniature World · 微缩摄影 Skill

**回形针是跨栏，刨丝器是果岭，日常物件里藏着一个小世界。**

给一个物件名，或上传一张商品照片，让 Codex / Claude Code 帮你构思有故事的微缩摄影：从物件的形状、纹理与结构出发，安排小人的动作、比例、机位和光线，再用当前环境的图像工具制作。

可以先选方案、直接创作，也可以只拿提示词。适合日常物件创意、商品微缩场景和见立摄影练习。

[介绍页](https://denggui-ai.github.io/create-miniature-world/site/) · [案例图库](https://denggui-ai.github.io/create-miniature-world/site/gallery.html) · [安装说明](docs/INSTALL.md) · [下载最新版](https://github.com/denggui-ai/create-miniature-world/releases/latest) · [English](README.en.md) · [日本語](README.ja.md)

| 回形针 · 跨栏赛 | 刨丝器 · 果岭推杆 | 剪刀 · 柄环接力 |
| --- | --- | --- |
| <img src="examples/paperclip-hurdles-20261020.png" width="260" alt="三枚立起的回形针成了跨栏，小跑者腾空跨栏"> | <img src="examples/grater-golf-20261020.png" width="260" alt="仰放的刨丝器大孔面成了高尔夫果岭，球手推杆进洞"> | <img src="examples/scissors-handle-relay-20261021.png" width="260" alt="剪刀黑色柄环成了环形跑道，小跑者接力"> |
| 跨栏决赛，领跑的已经腾空过栏。 | 球手正在推杆，球童在一旁看。 | 柄环跑道上的接力赛，冲向终点。 |

AI 生成，每张只生成 1 次。创作过程见[案例记录](examples/PICTURE_CARD_CASES_20261021.md)；更多看[案例图库](https://denggui-ai.github.io/create-miniature-world/site/gallery.html)。

## 从一件物品开始

| 你提供什么 | 可以怎样创作 |
| --- | --- |
| 一个物件名，如“马克杯” | 从轮廓、纹理或结构联想场景，先给方案，或直接生成 |
| 一张商品照片 | 以保留商品可见外观为目标，构思小人与物件的故事；照片适合作底图时，走实物照编辑路线 |
| 一个明确创意 | 按你指定的故事制作，不额外凑候选方案 |
| 只想要文字 | 交付方案或完整生图提示词，不调用图像工具 |

**核心是让物件本身成为场景。** 小人做什么、为什么在这里，都要和物件的可见结构有关。创意方法受田中达也（Tatsuya Tanaka）的「见立 / mitate」启发，详见[创作启发与致敬](#创作启发与致敬)。

## 安装与第一次创作

**1. 安装**（首次安装、目标目录还不存在时；已有同名 Skill 请先看[安装说明](docs/INSTALL.md)备份与比较）

先获取仓库：

```bash
git clone https://github.com/denggui-ai/create-miniature-world.git
```

进入你的目标项目，按所用宿主选择一个项目级目录：

| 宿主 | 安装位置 |
| --- | --- |
| Codex | `.agents/skills/create-miniature-world/` |
| Claude Code | `.claude/skills/create-miniature-world/` |

将仓库中的 `skills/create-miniature-world/` 完整复制到所选位置。**只安装这个 Skill 目录，别把整个仓库复制进去。** 首次安装脚本、更新与备份步骤见[安装说明](docs/INSTALL.md)；已有同名副本时先比较，不直接覆盖。

**2. 开一个新会话，发一张商品照片和一句话**（没有照片，只说物品名称也行）

| 环境 | 发送 |
| --- | --- |
| Claude Code | `/create-miniature-world 把这张商品图做成微缩摄影。先看方案，不要生图。` |
| Codex | `使用 $create-miniature-world，把这张商品图做成微缩摄影。先看方案，不要生图。` |

**3. 选一个方案**，说「按方案1生成一张，保留商品外观」，看图后再提一处修改。

**出图取决于宿主能力。** Codex 在图像工具可用时可直接生成或编辑；Claude Code 没有内置生图时，会交付方案和提示词，供你在已有图像工具中使用。本项目不附带模型、API 密钥或生图额度。

## 你可以怎样和它沟通

| 你说什么 | 它会怎样做 |
| --- | --- |
| 创意你来定，直接做一张 | 读物件、比较候选后自己选案，工具可用时生成 |
| 先看方案，不要生图 | 只用文字讲清每个方案：相机放在哪、谁在做什么、物件的哪个部分成了什么，等你选 |
| 只给我生图提示词 | 只输出文字，不调用生图 |
| 用我这张实物照直接改 | 照片贴近桌面、物件拍得够大、背景干净时，保留原照，只添加小人和道具 |
| 人物再小一些 | 调整人物及相关道具比例，保护商品 |
| 没看懂这个故事 | 回查物件联系、人物动作和空间关系，必要时换情境 |

有商品照片或指定商品时，默认以保护可见外观为目标；只有普通物件名称时自由创作。画幅默认方幅，你指定的比例优先。直接创作默认两个想法各出一张；指定创意、只要一张或仅成立一案时出一张。每个方案一张首图；编辑只在你点名的那张上做、至多一次；失败不重试、不自动追加。

## 它怎么想创意

先把画面想清楚再动手：相机放在哪，什么显得巨大，小人有多小（比如“人高约等于一个孔”），物件的哪个部分成了什么，正在发生什么事。想不出来时，它会翻 20 张田中达也作品的文字案例卡找同类，借想法，不抄画面。

出图有两种方式：只有物件名称时，整张画面直接生成；有一张贴近桌面、物件拍得够大的实物照时，保留原照，只在上面添加小人和道具。成图后它只问你一句“这是什么场景”，你一眼读出的故事就是检验。

## 更多案例与教程

- [马克杯 · 咖啡渍跑道](https://denggui-ai.github.io/create-miniature-world/site/coffee-ring.html)：只有物件名称，怎样变成一个故事
- [橘子实拍 → 行星考察](https://denggui-ai.github.io/create-miniature-world/site/orange.html)：比较两个创意，再用一次编辑缩小人物
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
