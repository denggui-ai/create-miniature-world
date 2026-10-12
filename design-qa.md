# 独立介绍页检查

final result: partial — live c94665f columns passed cloud checks; aligned grid and AI tape v2 approved for adoption; independent final review and new-layout browser checks pending

日期：2026-10-05。用户指出此前左右分栏封面偏离设计，要求以docs/design-reference.png为准恢复连续背景、宋体大标题、斜向大木梳与双列案例。后续新增参考裁光独立介绍页的信息组织。

## 当前实现

- index.html / style.css：导航与首屏共享摄影背景，真实HTML文字和按钮叠放；下方笔记本与薯片双列，共三个案例；修正带保留在完整案例集。手机顺序展示。
- hero-comb.png：无字AI展示适配背景；cover.png：带字README展示封面，均1340×1174。
- 原始案例仍来自examples，首屏按钮打开原始木梳案例；新图不替代历史证据。
- 安装区区分尚未安装/已经安装，链接安装指南并提供两宿主的复制指令。
- 参考页https://denggui-ai.github.io/threadtruth-studio/已通过浏览器实际查看并截图，借鉴作品展示到安装入口的组织方式，未复制其媒体。

## 已检查

- 两张新生成的展示素材已实际查看：暖色背景连续，字图无硬分栏，封面宋体标题及状态文字可读。它们不是网页渲染截图。
- 本地路径、锚点、HTML图像尺寸与标签结构；JavaScript语法。
- 首屏放大按钮无子图片，JS已使用data-alt与可选图片回退，避免原querySelector('img').alt空引用错误。
- 当前导出入口已禁用旧排版操作，避免运行旧脚本覆盖已选封面。
- Skill核心和examples原始图片保持不变。

## 历史本地预览阻塞（2026-10-05，公开前）

预览入口此前多次返回net::ERR_BLOCKED_BY_CLIENT，未因公开参考页能访问而宣称本地预览恢复。没有新版网页截图、控制台检查或交互通过记录。

1. 桌面与390px手机：字体回退、文字/人物遮挡、首屏高度、横向溢出、双列案例节奏。
2. 三图放大/关闭/Escape，宿主切换，复制成功与手动回退，安装导航与键盘焦点。
3. 背景图上的文字实际对比度必须看渲染结果；纯色对比度计算不代表摄影背景验收。

该阶段独立页尚未公开部署；后续公开及桌面实测已替代这一状态，见下一节。该阶段未新增 Skill 本机生图/编辑验收。

## 公开页面实测（2026-10-05，用户确认公开后）

实测网址：https://denggui-ai.github.io/create-miniature-world/site/ 。GitHub Pages显示live，浏览器实际打开成功。桌面首屏暖色背景、宋体标题、木梳主体已截图观察；使用区布局可读。三个案例均能打开对应弹窗，关闭按钮和Escape可退出；开始使用锚点和Claude指令切换正常。复制按钮显示成功；独立剪贴板读取未获得对应内容，因此不将跨通道剪贴板核验记为通过。现有日志中的错误来自浏览器扩展，不能当作本站脚本错误。

以上替代此前无法访问网页的blocked状态。手机390px、其他字体环境与复制失败回退仍待实际检查，不因上线宣称全部QA通过。Skill核心未修改。

## 候选发布前记录（2026-10-05）

安装入口使用现有主按钮样式，复制按钮移除外跳箭头，上传处增加数据流提醒。新增18组站内图库，首页全案例入口转站内，connection补笔记本关系图；保留木梳首屏、三精选、核心及原图。

静态路径/锚点、18图尺寸/lazy、手机单列CSS、共享脚本空节点保护及关闭后的焦点逻辑检查通过；实际桌面/手机视觉、导航、复制、全部大图、Escape/Tab焦点及溢出仍待浏览器验收。此前DOM或截图只支持对应旧状态，不能记为新图库通过。

用户已批准更新公开实验候选和Pages后继续云端验收。两页noindex保留，不创建正式Release。测试范围与未通过项见[审计记录](docs/LOCAL_AUDIT_2026-10-05.md)；部署结果以GitHub Pages对应提交的构建记录为准。本机操作日志及机器状态不纳入公开记录。

## 最新复核（2026-10-06，c94665f）

图库原比例布局已随提交[`c94665f`](https://github.com/denggui-ai/create-miniature-world/commit/c94665f9ccb305d144d21188d9816fb7966cbebb)上线，[Pages运行](https://github.com/denggui-ai/create-miniature-world/actions/runs/37390715136)结果为success，部署SHA与该提交一致；线上CSS哈希已核对。可直接访问[首页](https://denggui-ai.github.io/create-miniature-world/site/)与[18组图库](https://denggui-ai.github.io/create-miniature-world/site/gallery.html)。

按主任务移交的云浏览器实测结果归档：1180px、852px、500px视口分别为三列、二列、单列，18张图、放大关闭及焦点检查通过，首页无退化。500px云端视口不等于375–390px真机验证；真机和慢网尚未测试。本次为结果归档，未在本地重跑浏览器，也不扩大为完整剪贴板、全部键盘操作或Skill质量验收通过。

noindex继续保留；网页部署与上述视觉通过不代表Skill本机兼容性、商品保真或素材许可已全部通过。

## 当前本地网格发布稿（待独立终检）

2026-10-06用户已批准采用纸胶带压路机v2，并完成等宽逐行网格后发布实验候选。当前本地稿统一3:4完整展示，保留现代浏览器五条共享行轨道，以及不支持subgrid时的普通文档流回退；窄屏单列。18张展示图由17张历史案例和1张新增AI示意组成，新图以日期标识，旧G12图片、编号和来源记录保留。新图仅为参考造型生成示意，非认证Preiser型号，未验证精确1:87，也不宣称已表现清楚“压平翘边”。当前尚未提交或上线，等待独立终检后提交推送；线上仍为c94665f，其既有验收不代表新网格通过。保留experimental/noindex，不创建正式Release。
