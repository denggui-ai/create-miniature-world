# Miniature World · Miniature Photography Skill

**Turn everyday objects into small worlds with a story.**

An Agent Skill for Codex and Claude Code that finds visual connections in an object's shape, texture and structure, plans a miniature scene, and uses available image tools to generate and revise it. Inspired by Tatsuya Tanaka (田中达也) and his 見立 / 见立 / mitate approach to miniature photography: seeing everyday objects as something else.

[View website](https://denggui-ai.github.io/create-miniature-world/site/) · [中文](README.md) · [English installation and first-use guide](docs/GETTING_STARTED.en.md) · [case gallery](https://denggui-ai.github.io/create-miniature-world/site/gallery.html) · [Case notes and sources](examples/SELECTED.md)

## See the idea

| Notebook → bicycle rack | Potato chip → harvest field |
| --- | --- |
| <img src="examples/notebook-bike-rack.png" width="300" alt="Notebook binding rings become a miniature bicycle rack"> | <img src="examples/potato-chip-harvest.png" width="300" alt="Golden potato chip ridges become a miniature harvest field"> |

The homepage retains the comb, notebook and potato chip displays and adds two reviewed grater images made from the same real product reference. The comb cover is an AI layout adaptation; the [original comb image](examples/comb-farm.png) is retained separately. The two images above are original AI-generated development examples. The historical selection keeps one representative image per product group; the recent grater comparison shows two photo styles. Limitations and evidence are recorded in the [case collection](examples/SELECTED.md) (Chinese). They are not proof of local-host compatibility or exact product fidelity.

## Getting started

Follow the [English guide](docs/GETTING_STARTED.en.md) for the published version: installation, a text-only first request, one selected image and feedback.

Clone this public repository, or download its ZIP from the Code menu; no repository access invitation is required. Open the project in your local host.

```bash
git clone https://github.com/denggui-ai/create-miniature-world.git
cd create-miniature-world
```

The only installable source directory is `skills/create-miniature-world/`. Check for an existing installation before copying; compare rather than overwrite it.

| Host | Suggested project-local destination | Invoke after confirming discovery |
| --- | --- | --- |
| Codex | `.agents/skills/create-miniature-world/` | `$create-miniature-world` |
| Claude Code | `.claude/skills/create-miniature-world/` | `/create-miniature-world` |

Use one installation scope and verify the actual loaded files in a fresh task. Public main and v0.1.3 use the display label `微缩摄影 Skill`; the invocation identifier is `create-miniature-world`. See the [English guide](docs/GETTING_STARTED.en.md) and [installation instructions](docs/INSTALL.md).

To install, ask your local host:

> Read docs/INSTALL.md. Install only the 11 runtime files from skills/create-miniature-world into the project-local directory for this host: .agents/skills/create-miniature-world for Codex, or .claude/skills/create-miniature-world for Claude Code. Exclude evals and CHANGELOG.md. If a directory or symlink already exists, compare and back it up before any replacement. Verify all copied SHA-256 values and confirm the actual loaded path in a fresh session. Report image reading, reference-image input, generation, editing and saving separately. Do not generate, install dependencies or connect a paid service during installation.

After loading, attach a product photo and ask. An object name also works. Your host and its image tool process the photo and prompt; upload only material you may share with those services. This project website does not receive photos or generate images.

| Host | First request |
| --- | --- |
| Codex | `Use $create-miniature-world with this product photo. Propose three distinct concepts and recommend one. Do not generate images yet.` |
| Claude Code | `/create-miniature-world Use this product photo. Propose three distinct concepts and recommend one. Do not generate images yet.` |

Public main and v0.1.3 include the revised creative, framing and delivery rules. First request text-only concepts, then select an image to generate.

Direct generation defaults to two valid, distinct concepts, one image each, labeled A/B. Produce one if only one concept works, the user specifies a concept or asks for one image. Text-only requests do not generate. Show initial images first; the entire round shares at most one edit after selection. Diagnose “neither” feedback before generating a newly requested direction. The tested Claude Code host has no built-in generation; use an image tool you already have and return results for review.

## Learn from the tutorials

Start with the [orange photo-to-scene tutorial](site/orange.html): two initial concepts, one edit to reduce the figures and rover, and the user’s feedback. Compare the source photo and results, including the remaining fidelity limits. The illustrated page is in Chinese; the [English first-use guide](docs/GETTING_STARTED.en.md#follow-the-examples) introduces the existing case tutorials.

## The method

- **Find a connection:** notice a feature worth seeing differently.
- **Build a situation:** make that connection visible through action or spatial relationships.
- **Compose the image:** keep the original object, its new role and the overall image readable.
- **Review the result:** assess story, appearance and product fidelity separately, using visible evidence and comparisons when needed.

A story can be a small everyday moment. It does not need conflict, and it does not have to demonstrate the product's normal function. The product itself must contribute to the idea.

## Two photo styles: Soft Studio / Photo-real light

| | Soft Studio (default) | Photo-real light |
| --- | --- | --- |
| When | You do not mention a style | You ask for a real-photo feel, light and shadow, natural light |
| Light | Start with soft light and adjust to the scene | Credible direction, reflections and shadows; fill is allowed when needed |
| Backdrop and camera | Clean support; choose viewpoint for the relationship | Choose backdrop, focal length and viewpoint; no fixed 100mm rule |
| Focus | Keep required relationships readable | Blur must preserve key figures, parts and markings |
| Figures | Scale and count follow visible parts and scene needs | Same evidence; no universal frame-height target |

"Soft Studio" (柔光棚拍) is the new name for the former "Tanaka-inspired" route. "田中风格", "田中达也风格" and "Tanaka-inspired" remain compatible aliases. The lighting and workflow are unchanged; the name implies no endorsement. Ideas, figure appearance and product-fidelity rules are the same in both styles. When Python 3, Pillow and NumPy are available, the skill also saves a lightly finished copy (fine grain, optional gentle focus falloff) and delivers it with the original.

## Version and validation

> **v0.1.3 creative and delivery maintenance release.** [Release and archive](https://github.com/denggui-ai/create-miniature-world/releases/tag/v0.1.3). This release relaxes fixed concept quotas, figure occupancy/count and camera rules, and separates concept drafts from final deliverables. One independent temporary CLI session explicitly read the installed skill and produced three concepts. The parent session generated five initial images across three products and edited the timer once. The timer concept received positive feedback; the user agreed with the egg-slicer delivery assessment. Strict product-detail fidelity remains unresolved. These are limited assisted trials, not a blind baseline comparison. See [validation](docs/VALIDATION.md).

New real-reference test: [a remote-control photo and two results](examples/REMOTE_CONTROL_TEST_20261014.md), [usage tutorial](site/remote-control.html), and [fidelity regressions](docs/REMOTE_CONTROL_REGRESSION.md) (Chinese). Both images use the default Soft Studio route. Added display symbols, redrawn details and contact issues are retained; strict detail fidelity did not pass. Permission to publish is separate from quality approval.

> **Version scope:** public main and v0.1.3 retain 11 runtime files. The Codex project install was checked; the Claude install was not updated or retested this round. Earlier versions remain available.

## Requirements and limits

Requires an image-reading host; generation, image references and editing each depend on tools actually available in that session. No model, credits, API keys or paid-service client are bundled. Each generated image is a separate opaque portrait image in a 3:4 ratio by default.

Product lettering, construction and figure appearance may still be wrong. Scale follows visible relationships and valid references, without a universal occupancy target. Close-ups alone cannot establish scale beside a product. Finishing preserves the original and follows supported EXIF/ICC handling. Desktop implicit discovery, other machines, cross-platform behavior and fresh Claude sessions remain unverified. A concept draft is not a final product image; recommend delivery counts from actual quality, without generating extra images to fill a quota.

## Inspiration and materials

With appreciation for [Tatsuya Tanaka / MINIATURE CALENDAR](https://miniature-calendar.com/about/) and the possibilities of mitate. This project's method is its own synthesis of visual study and experiments, not the artist's published workflow. [Preiser](https://www.preiserfiguren.de/) is a useful official reference for miniature figures and poses.

This is an independent project, with no official affiliation or endorsement from the artist, Preiser or the product brands shown in examples. Original project text and configuration use the [MIT license](LICENSE). Images and third-party materials are not automatically covered by MIT; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Cost and common questions

- **Does the skill include generation credits?** No model, API key or image allowance is bundled. Generation and editing use your existing host and image tool; their current account terms and limits apply.
- **What if Claude Code cannot generate images?** Get concepts and prompts, use an image tool you already have, then return the results for review. Installing this skill does not require a new paid service.
- **Why do results differ from the examples?** Generation varies. Text, texture, product parts and figure size can be wrong. Confirm the loaded source, then describe one focused change. An appealing idea does not establish exact product fidelity.
- **Are local finishing dependencies required?** Without Python 3, Pillow and NumPy, deliver the original image. Finishing and web compression do not guarantee preservation of content credentials or all metadata; consult the original and case notes together.
- **How do I report a problem?** Use the [issue template](https://github.com/denggui-ai/create-miniature-world/issues/new?template=bug_report.md), including the host, loaded version, minimal input, expected and actual result. Share only authorized material and omit credentials.

## Feedback and development

Report the host, loaded version, input, expected result and observed problem. Include an image only when you have permission to share it. Distinguish missing tools from unreadable stories, altered products and oversized figures; do not include secrets.

Maintainers see [MAINTAINING.md](docs/MAINTAINING.md). Keep one source in `skills/create-miniature-world/`; update installed copies deliberately. The repository and invocation identifier remain `create-miniature-world`.

<details>
<summary>Historical presentation cover</summary>

![Miniature World: everyday objects, unexpected stories.](site/cover.png)

*Historical candidate-stage cover with its original wording retained; the current version is the v0.1.3 release stated above.*

</details>
