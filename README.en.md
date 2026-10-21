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

Use one installation scope and verify the actual loaded files in a fresh task. Public main and v0.2.2 use the display label `微缩摄影 Skill`; the invocation identifier is `create-miniature-world`. See the [English guide](docs/GETTING_STARTED.en.md) and [installation instructions](docs/INSTALL.md).

To install, ask your local host:

> Read docs/INSTALL.md. Install only the 11 runtime files from skills/create-miniature-world into the project-local directory for this host: .agents/skills/create-miniature-world for Codex, or .claude/skills/create-miniature-world for Claude Code. Exclude evals and CHANGELOG.md. If a directory or symlink already exists, compare and back it up before any replacement. Verify all copied SHA-256 values and confirm the actual loaded path in a fresh session. Report image reading, reference-image input, generation, editing and saving separately. Do not generate, install dependencies or connect a paid service during installation.

After loading, attach a product photo and ask. An object name also works. Your host and its image tool process the photo and prompt; upload only material you may share with those services. This project website does not receive photos or generate images.

| Host | First request |
| --- | --- |
| Codex | `Use $create-miniature-world with this product photo. Show the picture cards first. Do not generate images yet.` |
| Claude Code | `/create-miniature-world Use this product photo. Show the picture cards first. Do not generate images yet.` |

Public main and v0.2.2 write planning and shooting as one picture card and produce through one of two routes. First request the picture cards, then select one to generate.

Direct generation defaults to two ideas, one image each. Produce one if only one idea works, the user specifies an idea or asks for one image. Text-only requests do not generate. One edit at most, only on the image the user names; no retries or automatic extra images. The tested Claude Code host has no built-in generation; use an image tool you already have and return results for review.

## Learn from the tutorials

Start with the [orange photo-to-scene tutorial](site/orange.html): two initial concepts, one edit to reduce the figures and rover, and the user’s feedback. Compare the source photo and results, including the remaining fidelity limits. The illustrated page is in Chinese; the [English first-use guide](docs/GETTING_STARTED.en.md#follow-the-examples) introduces the existing case tutorials.

## The method

- **Find a connection:** notice a feature worth seeing differently.
- **Build a situation:** make that connection visible through action or spatial relationships.
- **Compose the image:** keep the original object, its new role and the overall image readable.
- **Review the result:** assess story, appearance and product fidelity separately, using visible evidence and comparisons when needed.

A story can be a small everyday moment. It does not need conflict, and it does not have to demonstrate the product's normal function. The product itself must contribute to the idea.

## One picture card, two making routes

Planning and shooting are written as one picture card: where the camera is and which three things it sees; what is huge; who is small and which part a person is as tall as; which part of the object becomes what and why it reads that way from this camera; what is happening and where the joke is; what is left out. When ideas run short, the 20 text-only Tanaka case cards (links to the author site, no images) supply mechanisms to borrow, not figure counts, props or titles.

| | Direct generation | Edit the real photo |
| --- | --- | --- |
| When | Only an object name, or the photo cannot serve as a base | A photo that passes as a base (camera near and low, object filling the frame, clean surface, soft light) |
| Object | Redrawn by the generator; parts and holes may change | Original photo kept; only figures and props are added |
| Figures | Figure photo reference from the package, written as matte flat paint | Same, following the base photo's depth and perspective |
| Review | Two questions first: what is happening; does it look like tiny people in a giant object's world | Also check object retention by eye and pixel difference |

"Soft Studio" and "Photo-real light" are no longer route names since v0.2.0. A request for "Tanaka-inspired" work is designed through the picture card; the name implies no endorsement. The original image is delivered without finishing by default; local finishing runs only on request when Python 3, Pillow and NumPy are available.

## Version and validation

> **v0.2.2 case-card article links.** [Release and archive](https://github.com/denggui-ai/create-miniature-world/releases/tag/v0.2.2). v0.2.2 changes only references/tanaka-cases.md: the 20 Tanaka case-card links now point to the author's article pages (each page shows the original) instead of image files, matching the "official pages only" notice; card text and the other ten runtime files are unchanged, and all 20 pages were opened and checked. No image run in this release. See [release notes](docs/RELEASE_v0.2.2.md).

> **v0.2.1 typical-object gate and base admission.** [Release and archive](https://github.com/denggui-ai/create-miniature-world/releases/tag/v0.2.1). v0.2.1 corrects three rules against Tatsuya Tanaka's 2017 interview: the picture card gains a fourth gate (a typical object whose identity and real size read at a glance); base-photo admission changes from "object fills the frame" to "object is large in frame" (near end off-frame or close to the edge, margins allowed; a small centred object is still rejected); the off-white ground is described as a post-processed backdrop, and a crop tightened to the event may be delivered alongside the original. Three runtime files changed; the other eight match v0.2.0. Checked with a five-case text before/after comparison and one image run (two scissors images, read on first look as skiing and a relay race); test images are not published. No fresh host session, blind test or cross-machine verification; strict SKU fidelity, figure matching and stable success rates remain unverified. See [release notes](docs/RELEASE_v0.2.1.md).

> **v0.2.0 picture-card release.** [Release and archive](https://github.com/denggui-ai/create-miniature-world/releases/tag/v0.2.0). v0.2.0 writes planning and shooting as one picture card (where the camera is, what is huge, who is small, which parts become what, what is happening, what is left out); production takes one of two routes, direct generation or editing the real product photo; review answers two questions and lists three differences against a Tanaka original. All four reference documents are new, including 20 text-only Tanaka case cards (links to the author site, no images). One image per route was produced: the ice tray (edit route) was approved by the user on first read; the grater (direct route) remains a candidate; two further direct-route images read as their card events but were not judged. Those samples and the base photo are not published. Both local Codex and Claude project installs match source; one explicit Claude host load test was done; no Codex fresh session, blind test or cross-machine verification; strict SKU fidelity, figure matching and stable success rates remain unverified. See [release notes](docs/RELEASE_v0.2.0.md).

New real-reference test: [a remote-control photo and two results](examples/REMOTE_CONTROL_TEST_20261014.md), [usage tutorial](site/remote-control.html), and [fidelity regressions](docs/REMOTE_CONTROL_REGRESSION.md) (Chinese). Both images use the default Soft Studio route. Added display symbols, redrawn details and contact issues are retained; strict detail fidelity did not pass. Permission to publish is separate from quality approval.

> **Version scope:** v0.2.2 keeps 11 runtime files; one changed in this release. Both local Codex and Claude project installs match source; one explicit Claude host load test was done. v0.2.1, v0.2.0, v0.1.4 and earlier releases remain available.

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

*Historical candidate-stage cover with its original wording retained; the current version is the v0.2.2 release stated above.*

</details>
