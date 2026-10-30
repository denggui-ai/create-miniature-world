# 介绍页

[在线查看介绍页](https://denggui-ai.github.io/create-miniature-world/site/) · [浏览案例图库](https://denggui-ai.github.io/create-miniature-world/site/gallery.html)

静态网页，没有构建步骤和后台服务。GitHub Pages 从 main 分支根目录发布，根目录 `index.html` 跳转到默认英文 `site/`。语言入口：英文 `site/`（兼容 `site/en/`）、中文 `site/zh/`、日文 `site/ja/`；三语主页显式互链，中文图库和教程在外语入口中标注语言。

## 在本机查看

下载完整仓库后，用浏览器打开 `site/index.html`，并保留相邻的 `examples/` 目录。页面可以放大案例图、切换和复制宿主指令；网页本身不生图。

## README 首页入口

README 横幅和文字首页链接均按语言落到对应主页。各语言横幅独立保存，不能复用带另一语言文案的图片。变更后需核对图片内文字、href、语言切换、canonical / hreflang 与社交元信息。

## 图片

- 网页显示 `site/img/` 下的 WebP 压缩版；"查看原图"链接指向 `examples/` 下的原始 PNG/JPG。
- `hero-comb.png` 和 `cover.png` 是由木梳案例生成的 AI 展示适配图，不是商品保真测试。`cover.png` 图内的"实验候选版"是历史文字，见 `cover.html`。
- 新增网页图片时，同时生成 `site/img/*.webp`，并修改 `src` 和 `data-image`。

来源与许可见 [素材说明](../THIRD_PARTY_NOTICES.md)。

## 搜索与分享

已公开的介绍、图库和教程入口列于 [sitemap.xml](../sitemap.xml)。地图不包含历史封面或尚未公开的本地页面；更新公开页面清单时同步维护。页面元信息与站点地图不保证被搜索引擎收录，也不代表已向搜索服务提交。
