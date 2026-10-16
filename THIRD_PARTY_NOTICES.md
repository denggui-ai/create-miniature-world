# 素材来源与许可

本页说明仓库中图片与第三方名称的来源、许可和用途。[MIT 许可证](LICENSE) 只覆盖本项目自行编写的代码和文档，**不覆盖下列图片**，也不覆盖链接指向的作品、照片和品牌标识。本项目没有为任何图片提供额外的商用、修改或再分发许可。权利人如有异议，请通过仓库 Issue 联系，确认后移除。

## 第三方照片

| 文件 | 作者与来源 | 许可 | 用途 |
| --- | --- | --- | --- |
| `examples/clothespin-public-domain.jpg` | Eloquence，2004，[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Clothespin.jpg) | 公有领域（作者释出） | 本机验收与木夹教程的商品输入 |
| `examples/paperclip-pd-scan.jpeg` | Hephaestos，[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Paperclip.jpeg) | 公有领域（作者释出） | 回形针试验的商品输入 |
| `examples/grater-reference-20261013.jpg` | Ben Dalton / noii，2009，[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Grater_(3792844780).jpg) | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/)，署名“Grater — Ben Dalton / noii, CC BY 2.0, via Wikimedia Commons” | 刨丝器真实参考验证的商品输入 |

以上照片原样收录，仅重命名；本项目不对其重新授权或附加限制。

## 项目作者拍摄的照片

| 文件 | 说明 | 许可 |
| --- | --- | --- |
| `skills/create-miniature-world/assets/figure-refs/` 三张 | 项目作者 denggui-ai 拍摄的 1:87（HO）手工涂装塑料人偶，已去除元数据，不含包装、logo、条码 | 仅这三张照片采用 CC BY-NC 4.0，署名“1:87 (HO) hand-painted plastic model figures. Photos by denggui-ai (project author).”；不授予人偶造型本身的任何权利 |
| `examples/remote-reference-20261014.jpg` | 遥控器实拍原照，已无损转正并移除 EXIF | 未附加许可，仅供本项目展示 |
| `examples/orange-reference-20261015.jpg` | 橘子实拍原照，无 EXIF、GPS | 未附加许可，仅供本项目展示 |

## AI 生成的示例图

`examples/` 下其余 PNG，以及 `site/hero-comb.png`、`site/cover.png` 和 `site/img/` 下的压缩版，都是本项目用 AI 图像工具生成或编辑的输出。逐文件的输入、尺寸和 SHA-256 见 [examples/SELECTED.md](examples/SELECTED.md)、[examples/CASES.md](examples/CASES.md) 和各教程页。

- 这些图片不纳入 MIT，仅供本项目展示和教学，不提供额外复用许可。
- 生成时用到的输入分三类：只有物品名称或文字；上面列出的第三方或作者照片；以及少量网上公开的官方商品页或人偶厂商照片。最后一类只作为生成参考，**原图不随仓库分发**。
- 成图不是官方商品照片或人偶厂商照片，不代表任何品牌或厂商的合作、背书或真品证明，也不保证商品外观、型号或 1:87 比例精确。
- AI 生成的文字、刻度和标识可能有错，见各案例说明。

<a id="paper-cup-tutorial-source"></a>

### 纸杯教程（2026-10-06）

`examples/paper-cup-train-depot-20261006.png`、`paper-cup-circus-20261006.png`、`paper-cup-theatre-20261006.png`：只凭“纸杯”名称生成，无商品参考图，每案一次、未修图，1086×1448。三张均作为有问题的教学对照，不是成功验收。说明见[纸杯入门教程](docs/QUICK_START.md)。

```text
8450a47d77eb51f969e898e212205eb2e468c7c5cb624f38d6b2566ddb539060  examples/paper-cup-train-depot-20261006.png
f423079d57dbb74861e61b27565e7ea37d798a9b37e8f7440bcac26c6c43d5f1  examples/paper-cup-circus-20261006.png
78943b0a1f05866861ce1664e92a03e929890d689723a6e64fa5576e298d17c0  examples/paper-cup-theatre-20261006.png
```

<a id="soap-skating-tutorial-source"></a>

### 香皂教程（2026-10-06）

`examples/pears-soap-skating-v1-20261006.png`（初稿）与 `-v2-`（一次编辑）：生成参考为 [Pears 官方产品页](https://www.pearspuresince1807.com/us/en/p/pears-pure-gentle-with-glycerin-mint-extracts-extracts-bar-soap-3-53oz.html/00850022820427)，官方照片不随仓库分发。生成后才发现田中达也《[Soap Skating](https://miniature-calendar.com/200911)》是同类先例，本项目不主张该机制为独创。

```text
798346189faaf83ebf183ef1decb09f8fcb5f7d8e52c72805f7f5202cf2bc2bb  examples/pears-soap-skating-v1-20261006.png
a7c88da784f0c8cddbd31d7dd886f56f9debad7449cbdcfebc0c4c7b6062b403  examples/pears-soap-skating-v2-20261006.png
```

<a id="sticky-roller-tutorial-source"></a>

### 粘毛滚筒教程（2026-10-06）

`examples/muji-sticky-roller-v1-20261006.png`（初稿）与 `-v2-`（一次缩人编辑）：生成参考为 [MUJI Lint Roller 官方产品页](https://www.muji.us/collections/cleaning-tools/products/lint-roller-ma0dpa1a)，并用了人偶厂商照片作造型参考；两类参考原图都不随仓库分发。商品识别和比例未通过，作为能力边界对照。

```text
8d635fe619a33ad515d648b2a6def8ca3e595a29b3e7f9abcab164c333758cf5  examples/muji-sticky-roller-v1-20261006.png
0d3b81bd799b196babf477d1d4a1f45f3e76e59c1d479d163e75b7c64c0575ad  examples/muji-sticky-roller-v2-20261006.png
```

### 木夹教程（2026-10-09）

`examples/clothespin-diving-v1-20261009.png`（初图）与 `-v2-`（按“人再小一半”的一次编辑）：输入为上方公有领域木夹照片，无品牌商品、无人偶照片。提示词见 `examples/prompts/`。

```text
9061053f5fddb448320139ac7d59511795f1bee9a659ac932c9aeaff108bf6fa  examples/clothespin-diving-v1-20261009.png
b8f6bddf2fbad05b89ee17bd7f691754ccc1c3b68c5c4cd7e33619a2f912070a  examples/clothespin-diving-v2-20261009.png
```

<a id="2026-10-12新测试案例"></a>

### 2026-10-12 名称测试（8 张）

眼镜、马克杯、订书机、卷尺 8 张，只凭物品名称或文字生成，无商品输入图。眼镜与马克杯 4 张用了人偶厂商官方照片作造型参考，原图不随仓库分发。逐文件说明见 [SELECTED.md](examples/SELECTED.md#2026-10-12-新测试案例8-张)。

### 真实参考验证（2026-10-13 起）

- 刨丝器：`examples/grater-*-original-20261013.png` 由 AI 生成，输入为上方 CC BY 2.0 刨丝器照片和包内人偶照片；`*-finish-*` 为本机脚本加颗粒的另存版。详见[刨丝器对照](examples/GRATER_VALIDATION_20261013.md)。
- 遥控器：`examples/remote-*-finish-20261014.png`，输入为遥控器原照和包内人偶照片，详见[实测记录](examples/REMOTE_CONTROL_TEST_20261014.md)。

<a id="2026-10-15橘子教程"></a>

### 橘子教程（2026-10-15）

`examples/orange-a-initial-20261015.png`、`orange-b-initial-20261015.png`（各一次生成）与 `orange-a-edited-20261015.png`（一次编辑）：输入为橘子原照和包内弯腰人偶照片。详见[教程](site/orange.html)。

## 名称与创作启发

本项目受田中达也（Tatsuya Tanaka）MINIATURE CALENDAR 的见立创作启发。田中达也、Preiser 及各商品品牌名称仅用于说明启发来源、造型参考或商品类别，不代表官方产品、合作或背书。方法说明是本项目对公开作品画面的分析，不是作者本人的创作自述。

- 此前公开的 `examples/tape-runner-learning-replica-20261008.png`（参照田中达也《[Tape Runner](https://miniature-calendar.com/240821)》的 AI 学习复刻）已于 2026-10-17 出于对原作权利的审慎主动移除；本项目今后不公开对特定作品的复刻。[作品解读](docs/ARTWORK_INTERPRETATION.md)只做文字分析并链接原作。
- 田中达也官网的 [ABOUT 页](https://miniature-calendar.com/about/) 允许为介绍作者而引用图片并要求署名，禁止热链和其他再分发；本仓库不收录田中原作图片，只链接官方页面。
- Preiser 官网的 [Impressum](https://www.preiserfiguren.de/showpage.php?Impressum&SiteID=26) 规定其图片仅限私人、非商业用途；本仓库不收录 Preiser 官方照片。
- 官方来源索引见 `skills/create-miniature-world/references/creative-relations.md`。

你自己添加的商品图和人偶照片不属于本仓库内容，请按各自的权利条件使用。
