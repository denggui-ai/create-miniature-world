# 已恢复的历史试验1-2

从项目档案 `miniature-stationery-trial-records.zip` 的 protocol.json、results.json、sources.json 提取。输出SHA-256与档案完全匹配，提示词原文保留；这不是重新运行。

- 条件：baseline，简洁创意提示；当时对照中的显示标签“回形针2”。不能把它误记为当前Skill生成。
- 输入：[paperclip-pd-scan.jpeg](paperclip-pd-scan.jpeg)，唯一商品事实参考；这次记录没有人偶参考。
- 输出：[paperclip-diving-before.png](paperclip-diving-before.png)，1086 × 1448。
- 开始UTC：2026-10-04T07:24:21.234Z；返回UTC：2026-10-04T07:27:22.262Z。
- 工具：内置imagegen，具体模型版本未公开；seed工具不提供；请求竖版3:4、不透明背景。
- 当时记录的Skill仓库提交：`afa41d865e46afefcc7fa88a1747e774aa03f303`，不能当作本GitHub仓库已有提交。
- 原冻结protocol SHA-256：`b9ba7d39c0bbb776c74d146e579b84ed4e80cb96d25f72e2db3a3a447932262d`。
- 反馈：用户对早期回形针对照说缺少参照、像水管，未指定1或2；没有单独确认本图的偏好。

## 实际提示词

```text
Create one original mitate miniature photograph inspired by Tatsuya Tanaka's playful reinterpretation of everyday objects. Make both the original stationery product and its new miniature-world role recognizable. Use the single attached image only as the factual product reference. Preserve its visible shape, proportions, components, open/closed state, materials, colors and original markings. Do not carve, cut, bend, melt, hollow, add parts to, or redesign the product. Props must sit beside or on existing accessible surfaces. Use a view supported by the reference. Hand-built tabletop photography with tactile materials, credible miniature scale, contact shadows and focus covering the important visual relationship. Keep the complete product recognizable in a single portrait 3:4 frame, opaque background. No collage, added title, captions, watermark, or new branding. Preserve the existing product markings; do not invent illegible small text.

Subject: the ONE silver metal Gem-style paperclip in the reference scan, with its exact narrow round wire, elongated nested bends, both offset open ends and open gaps. Do not turn the open wire path into a closed racetrack or add metal connectors. The scan's dark edge shading is not black paint.

Choose an imaginative, visually clear and witty miniature scene for this product yourself. Make the product's everyday features read as a different world.
```

## 输入来源

Hephaestos：[Wikimedia Commons / Paperclip.jpeg](https://commons.wikimedia.org/wiki/File:Paperclip.jpeg)。历史sources.json记录作者释入公有领域（PD-user），输入校验值为 `343791769692760793e72e7756d7423dfcb3c3d6566b9de25cc1cf4703ca724d`。本轮从档案原字节恢复并实际看图，未重新检索许可页；图为262×721扫描，不能支撑不可见侧面或精细材质重建。
