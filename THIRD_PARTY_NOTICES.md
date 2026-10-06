# 素材与授权范围

状态更新（2026-10-06）：用户已明确确认公开现有仓库与GitHub Pages。下文「本轮仅私有同步」等为历史收录阶段，不再描述当前可见性。公开操作不改变图片许可范围，也不补齐缺失的历史输入；MIT仍仅覆盖有权许可的代码与自编文档。

## 包内素材

`examples/clothespin-public-domain.jpg`：Eloquence，2004，原文件名 Clothespin.jpg。

- 来源：https://commons.wikimedia.org/wiki/File:Clothespin.jpg
- 原图：https://upload.wikimedia.org/wikipedia/commons/0/0e/Clothespin.jpg
- 来源页标明由作者释入公有领域（Public domain）；2026-10-05已核对。
- 本包原字节复制，仅重命名，未改图。它不是本项目原创，也不是已确认品牌型号的商品图。
- 此照片不通过本项目MIT重新授予或限制权利。

## 当前未附带的素材与后续收录

历史私人试验用过 Preiser 官方人偶照片、田中达也作品原图及相应AI学习复刻；公开包不携带这些文件。现有原文件未因本次打包被删除。参考文档保留官方作品页及目录来源，公开可访问不等于本项目获得再分发或训练授权。

2026-10-05曾在私有开发阶段恢复六组历史案例及AI人偶诊断图，见 examples/CASES.md 和 examples/FIGURE_REFERENCES.md。现已随仓库公开；除已匹配记录外，部分完整参考输入仍未知，因此不将这些图片自动归入MIT或宣称全部已适合公开分发。公开展示不能代替按实际输入和用途逐项核对；当前缺口与复用状态见下方逐文件清单。独立策划的AI成图、作者原作与学习复刻分别标记；不能仅因使用AI生成，就推定实际输入及输出的全部用途均获许可。文档中的认可与失败状态是项目历史记录摘要，不能替代读者自己的视觉验收。

人偶实物公开销售不等于厂商或商家的产品照片可自由再分发。自摄或已获相应用途许可的参考图可以收录；其他图片按来源条款和具体用途判断，不作一律禁用。私有仓库与公开发布分开处理，私有可见性本身不产生素材授权。精选图片需单独注明来源和使用条件，不自动归入项目MIT许可证。

Preiser官网Impressum的Urheberrecht段说明：下载与复制仅允许私人、非商业用途；超出著作权法允许范围的复制、改编、传播与利用，需要相应作者或制作者的书面同意。因此品牌推荐、署名和目录可下载本身，不等于获得将官方照片随Skill公开分发的许可。可保留官网链接、产品信息及自己的观察；本轮未取得额外图片分发授权。来源：https://www.preiserfiguren.de/showpage.php?Impressum&SiteID=26 （2026-10-05核对）。

本地用户另行添加的产品图和人偶照片不属于公开源代码；请按各自权利条件使用，不将其自动提交到仓库。生成结果的使用条件另按实际输入、工具和用途判断。

## 名称与研究来源

本项目致敬田中达也的见立创作，并将MINIATURE CALENDAR明确列为创作启发。田中达也及Preiser名称用于说明研究来源或造型目标，不代表官方产品、合作或背书。方法研究是对可见作品关系的分析，不是作者本人公开确认的完整创作过程。致敬和署名不替代图片许可。

田中达也官网ABOUT的Notice允许为介绍作者与MINIATURE CALENDAR而在文章中引用图片，要求署名，禁止图片热链，并限制其他未经授权的再分发与二次使用。研究介绍中的引用与把图片作为可安装Skill素材分发是不同用途，不能直接推定后一用途获准。来源：https://miniature-calendar.com/about/ （2026-10-05核对）。

官方来源索引见 `skills/create-miniature-world/references/creative-relations.md`。MIT仅覆盖本项目有权许可的自行编写内容，不覆盖这些链接指向的作品、照片和品牌标识。

## 本次新增图片的具体来源

- `examples/paperclip-pd-scan.jpeg`：Hephaestos，来源 https://commons.wikimedia.org/wiki/File:Paperclip.jpeg 。2026-10-04历史sources.json记录PD-user公有领域；2026-10-05本地审计重新打开来源页，仍标明作者释入公有领域。文件从试验档案原字节恢复。它不是项目原创，不通过MIT重新许可。
- 九张PNG均为项目历史AI输出，原名与校验值见CASES.md；生成方式标记不等于完整输入与所有用途已核清。其中 `ai-figure-diagnostic.png` 不是官方Preiser产品照片。
- 木梳关联输入为用户提供的商品页面截图；本轮实际看过但没有把整张页面截图打包，商家摄影、品牌标识及网页内容的权利不由本项目授予。
- 本批不含田中达也原作和Preiser官方人偶照片。未确定对应关系的作者复刻不作为“本项目独立成功案例”补入。

## 产品代表图增补（2026-10-05）

新增选图与历史原件SHA-256逐一匹配，映射见examples/SELECTED.md。18组主案例和G45详情补充均是本项目历史AI输出；保留部分完整输入、实物人偶参考及公开用途仍待核实的边界，不自动用MIT许可这些图片。此为2026-10-05公开前的选图收录记录；当时仅同步私有仓库，后续已公开，未发布正式 Release。

## 公开图片逐文件清单（2026-10-06发布稿）

覆盖原30张公开图片与本次批准新增的1张纸胶带v2，共31张发布候选图片，首页所用资产列在前五行。原30张文件已在公开仓库展示，新增纸胶带v2已获采用授权、当前待终检发布。文件公开可访问只说明已展示；不等于本项目能够授权商业使用、修改或再分发。表中「未提供额外复用授权」记录项目目前未授予的范围，不替代适用法律或原权利人的授权。AI 输出标记不构成商用许可结论。未核清的证据继续保留待核，图片不因本次审计删除或替换。

首页三案的优先缺口：木梳缺完整实际生成输入及商品截图权利链；笔记本缺对应调用和人偶参考用途授权；薯片缺完整输入与生成工具/用途记录。首屏及封面还依赖设计参考图，其原始出处与复用许可待核。下一次补证应对应具体文件，不用统一的「AI生成」说明覆盖这些差异。

| 公开文件 | 已知来源 / 证据 | 当前许可状态 | 本项目是否提供图片复用授权 |
| --- | --- | --- | --- |
| `site/hero-comb.png` | 项目 AI 展示适配；依据木梳案例与选定设计稿，见 [site/README.md](site/README.md) | 原案例及设计稿权利链未完整核清；不纳入 MIT | 未提供额外复用授权 |
| `examples/comb-farm.png` | 项目历史 AI 输出 G23，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md)；商品页面截图仅为关联输入候选 | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/notebook-bike-rack.png` | 项目历史 AI 输出 G30，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md)；历史方法记录提及成人实物参考，完整调用未恢复 | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/potato-chip-harvest.png` | 项目历史 AI 输出 G68，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `site/cover.png` | 项目 AI 展示适配；依据木梳案例与选定设计稿，见 [site/README.md](site/README.md) | 原案例及设计稿权利链未完整核清；不纳入 MIT | 未提供额外复用授权 |
| `docs/design-reference.png` | 用户选定的设计参考图，见 [开发交接](docs/DEVELOPMENT_HANDOFF.md)；原作者/原始出处未记录 | 作者、输入链与分发/复用许可待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/ai-figure-diagnostic.png` | 项目历史 AI 输出，原名及 SHA-256 见 [CASES.md](examples/CASES.md)；AI 人偶诊断，非官方实物照片 | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/binder-clip-climbing.png` | 项目历史 AI 输出 G64，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/citrus-tea-loading.png` | 项目历史 AI 输出 G58，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/clear-tape-concert.png` | 项目历史 AI 输出 G54，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/clothespin-public-domain.jpg` | Eloquence，2004；[Commons 来源页](https://commons.wikimedia.org/wiki/File:Clothespin.jpg) | 来源页 Public domain；2026-10-05复核 | 依据原作者公有领域声明；非本项目再许可 |
| `examples/correction-tape-cinema-alternative.png` | 项目历史 AI 输出 G45，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/correction-tape-hiking.png` | 项目历史 AI 输出 G52，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/glasses-roof-repair.png` | 项目历史 AI 输出 G05，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/glue-stick-summit.png` | 项目历史 AI 输出 G50，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/grater-climbing.png` | 项目历史 AI 输出 G15，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/mug-rain-shelter.png` | 项目历史 AI 输出 G19，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/notebook-bike-parking.png` | 项目历史 AI 输出，原名及 SHA-256 见 [CASES.md](examples/CASES.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/packing-tape-road.png` | 项目历史 AI 输出 G12，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/paper-tape-road-roller-v2.png` | 2026-10-06纸胶带试验AI输出，一次修正v2；原名、尺寸与SHA-256见[SELECTED.md](examples/SELECTED.md)。参考造型非认证Preiser型号，精确1:87未验证；非官方实物照片 | 用户已批准本项目公开展示；不纳入MIT，不将参考照片许可外推至成图全部用途 | 未提供额外复用授权 |
| `examples/paperclip-diving-before.png` | 项目历史 AI 输出，原名及 SHA-256 见 [CASES.md](examples/CASES.md)；公有领域回形针输入与试验1-2已配对，完整用途权利仍不能据此推定 | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/paperclip-paper-after.png` | 项目历史 AI 输出 G46，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/paperclip-pd-scan.jpeg` | Hephaestos，2004；[Commons 来源页](https://commons.wikimedia.org/wiki/File:Paperclip.jpeg) | 来源页 Public domain；2026-10-05复核 | 依据原作者公有领域声明；非本项目再许可 |
| `examples/pencil-road.png` | 项目历史 AI 输出 G56，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/ruler-finish-line.png` | 项目历史 AI 输出，原名及 SHA-256 见 [CASES.md](examples/CASES.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/scissors-rink-a.png` | 项目历史 AI 输出，原名及 SHA-256 见 [CASES.md](examples/CASES.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/scissors-rink-b.png` | 项目历史 AI 输出，原名及 SHA-256 见 [CASES.md](examples/CASES.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/sponge-climbing.png` | 项目历史 AI 输出 G70，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/stapler-concert.png` | 项目历史 AI 输出 G65，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/tape-measure-jump.png` | 项目历史 AI 输出 G60，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |
| `examples/zipper-canal.png` | 项目历史 AI 输出 G69，原名及 SHA-256 见 [SELECTED.md](examples/SELECTED.md) | 完整输入与公开复用权利待核；不纳入 MIT | 未提供额外复用授权 |

上述发布稿仅纳入用户明确批准采用的纸胶带v2，其他本机验证图与纸胶带对照保存在被忽略的outputs；下方纸杯图另列为获用户批准公开的教程示例。该发布稿只收录v2成图，不附带第三方参考照片；公开采用不等于额外商用或再分发承诺。轻量实验安装包不含任何图片，案例仅提供在线浏览链接。

<a id="paper-cup-tutorial-source"></a>

## 教程图片（2026-10-06）

以下3张为用户于2026-10-06批准公开的教程图片，与上方31张合计34张公开资产，不加入18图精选。主展示选择为A的“隧道口／列车出洞”入口联想，B、C保留教学对照。公开展示授权不代表SKU保真、精确比例或额外商用许可。

三案从普通物品名称出发，没有商品参考图；每案生成一次、没有修图，均为1086×1448。本轮从各自原Library条目取回并实际看图，按原字节复制；原文件名与下表相同。原Library身份和取回记录只保留在本机忽略目录。[纸杯入门教程](docs/QUICK_START.md)记录文字预选、成图比较与推荐理由。

| 教程文件 | 已知来源 / 可见限制 | 当前许可与采用状态 | 本项目是否提供图片复用授权 |
| --- | --- | --- | --- |
| `examples/paper-cup-train-depot-20261006.png` | A纸杯隧道口／列车出洞联想，2026-10-06 AI输出。原提示用“tunnel”且保留封底，曾收窄称车库；现采用入口联想，不宣称贯通。未修图，杯口下缘连接被遮挡 | 用户选择为教程主展示，已批准本项目公开展示；非SKU或比例验收；不纳入MIT | 未提供额外复用授权 |
| `examples/paper-cup-circus-20261006.png` | B马戏帐篷，2026-10-06 AI输出。入场动作可读；切门、布帘与旗帜为新增，亦可读成剧场入口 | 已批准公开作教学对照；未记录单独质量认可或SKU保真；不纳入MIT | 未提供额外复用授权 |
| `examples/paper-cup-theatre-20261006.png` | C音乐厅，2026-10-06 AI输出。木阶梯座席、舞台重构杯内空间，纸杯偏容器；不据此断言杯壁被切坏，部分脚部支撑不清 | 已批准公开作教学对照，主展示选择已改为A；非SKU或比例验收；不纳入MIT | 未提供额外复用授权 |

SHA-256：

```text
8450a47d77eb51f969e898e212205eb2e468c7c5cb624f38d6b2566ddb539060  examples/paper-cup-train-depot-20261006.png
f423079d57dbb74861e61b27565e7ea37d798a9b37e8f7440bcac26c6c43d5f1  examples/paper-cup-circus-20261006.png
78943b0a1f05866861ce1664e92a03e929890d689723a6e64fa5576e298d17c0  examples/paper-cup-theatre-20261006.png
```
