# 维护说明

本页面向想了解项目结构或参与维护的人。日常使用请看 [README](../README.md) 和 [安装说明](INSTALL.md)。

## 源码结构

- `skills/create-miniature-world/`：Skill 唯一源码。安装到 Codex 或 Claude Code 的目录只是运行副本，修改源码后再重新安装。
- `examples/`：样张原图、提示词和逐案说明。
- `site/`：GitHub Pages 介绍页，见 [site/README.md](../site/README.md)。
- `docs/`：安装、教程和验证记录。

仓库名、源目录和调用标识统一为 `create-miniature-world`。

## 发版

- 版本以 [GitHub Releases](https://github.com/denggui-ai/create-miniature-world/releases) 为准，每个版本附发布说明。
- 发版前确认：Skill 行为与 README、网站描述一致；至少一张真实参考样张在商品外观、故事、人物尺度和美感四方面看图通过；公开图片的来源与许可已写进 [素材说明](../THIRD_PARTY_NOTICES.md)。
- 验证方法见 [本机验收](LOCAL_TEST.md) 和 [验证记录](VALIDATION.md)。

## 反馈

请在 [Issues](https://github.com/denggui-ai/create-miniature-world/issues) 说明：宿主（Codex 或 Claude Code）、实际加载的版本、输入、期望结果和实际结果。只附有权分享的图片，不要贴账号信息或密钥。
