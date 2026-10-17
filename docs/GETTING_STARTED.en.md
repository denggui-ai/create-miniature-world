# Miniature World: installation, first image and examples

This guide covers public main and the v0.1.0 runtime: installation, a text-only first request, one selected image, feedback and examples. Unpublished A/B and figure-maintenance rules are not part of these instructions; the release archive remains unchanged.

## Choose your source

Start with the [English README](../README.en.md). The public repository is [denggui-ai/create-miniature-world](https://github.com/denggui-ai/create-miniature-world). Download and extract its Code → Download ZIP archive, or use the existing clone instructions:

```bash
git clone https://github.com/denggui-ai/create-miniature-world.git
cd create-miniature-world
```

For the released snapshot, use the dedicated ZIP and SHA-256 file attached to [v0.1.0](https://github.com/denggui-ai/create-miniature-world/releases/tag/v0.1.0). Verify the archive against its accompanying checksum before installing. Public main includes the default image-count fix and Soft Studio naming update in the v0.1.0 runtime; the release archive is unchanged. Keep the selected source identifiable; downloading a repository does not install a skill.

## Install for your host

For a direct terminal installation on macOS/Linux, use the [checked copy-and-hash steps](INSTALL.md#终端直接安装macos--linux首次项目级安装). The default is Codex; change `host` to `"claude"` for Claude Code. Existing directories or symlinks stop the command. Windows commands have not been verified.

The source is `skills/create-miniature-world/`. Install the 11 runtime files: `SKILL.md`, `agents/openai.yaml`, four reference documents, the figure-reference README and its three photos, and `scripts/photo_finish.py`. Exclude development `evals/` and `CHANGELOG.md`.

| Host | Suggested project-local destination | Invocation |
| --- | --- | --- |
| Codex | `.agents/skills/create-miniature-world/` | `$create-miniature-world` |
| Claude Code | `.claude/skills/create-miniature-world/` | `/create-miniature-world` |

Ask your local host:

> Read docs/INSTALL.md and docs/LOCAL_TEST.md. Check for an existing create-miniature-world directory or symlink before installing. Compare it with the source I selected; back it up before any replacement. Install only the 11 runtime files from skills/create-miniature-world into this host's project-local skill directory. Exclude evals and CHANGELOG.md. Verify every copied file's SHA-256 against that source. In a fresh session, confirm the actual loaded path. Report image reading, reference-image input, generation, editing and saving separately. Do not generate images, install dependencies or connect a paid service during installation.

Choose one installation scope. If you explicitly need user-wide installation, the documented alternatives are `~/.agents/skills/create-miniature-world/` for Codex and `~/.claude/skills/create-miniature-world/` for Claude Code. An existing directory alone does not prove discovery. In the fresh session, first request three concepts without generation to confirm loading.

Public main and the release archive use the Codex display label `微缩造景`. The project title is Miniature Photography Skill; the directory and invocation identifier remain `create-miniature-world`. If another label appears, verify the loaded path and version.

## Make your first request

Attach a clear product photo, or start with an object name. In Codex:

> Use $create-miniature-world with this product photo. Propose three distinct concepts and recommend one. Do not generate images yet. Please respond in English.

In Claude Code:

> /create-miniature-world Use this product photo. Propose three distinct concepts and recommend one. Do not generate images yet. Please respond in English.

With a product photo, the skill protects the visible product appearance by default. With only an ordinary object name, it uses free creation and does not promise to reproduce a particular product. State any features that must remain unchanged. Photos and prompts are processed by your host and its image tool; upload only material you may share with them. The project website displays examples and instructions.

After selecting a concept, ask “Generate one image using concept 1; preserve the product.” Public main defaults to one image per recommended and runner-up concept; an explicit one-image request overrides that default. The unchanged v0.1.0 archive retains conflicting wording, so specify the count when using it. A/B selection and diagnosis changes in development are not promised by this guide.

For a text-only start:

> Use $create-miniature-world with an ordinary paper cup. Propose three concepts and recommend one. Do not generate yet. Please respond in English.

Use the Claude invocation instead when working in Claude Code. You can also request prompts only. The tested Claude Code environment has no built-in generation: use an image tool you already have, then return the results for review. Reading a photo does not prove that a generation tool can receive it.

## Select, review and refine

Review four things separately: whether the story is readable, whether the visible product is preserved, whether the figures feel tiny beside it, and whether the whole image looks good. Recognition of a clever idea does not establish exact SKU fidelity.

After selection, request one focused change and state what to preserve:

> Keep this image's story, product and composition. Make the people and their related props smaller together, and preserve their contact with the product.

Request one focused edit at a time and review the result before continuing. Editing requires a tool that can edit the selected image; a new text-only generation is not evidence of a faithful edit. If the story does not work, request text-only diagnosis before authorizing more images.

Images default to separate opaque portrait images in a 3:4 ratio. The default route is Soft Studio (柔光棚拍), the former Tanaka-inspired route; the old Chinese and English names remain compatible aliases. The v0.1.0 archive retains the old name. Ask for a real-photo feel, natural light, or light and shadow to select the Photo-real light route. Figures should feel like tiny painted plastic models beside a giant object; a frame-height percentage alone does not establish correct scale. Optional local finishing needs Python 3, Pillow and NumPy; without them, deliver the original. Save results under `outputs/` without overwriting inputs.

## Follow the examples

The [online gallery](https://denggui-ai.github.io/create-miniature-world/site/gallery.html) has 28 case cards: two reviewed real-reference results, eight object-name tests and eighteen historical representative images. Tutorial images are counted separately. Gallery captions and detailed source records remain mainly in Chinese; this draft provides an English route through them.

| Entry | What to learn | Evidence limit |
| --- | --- | --- |
| [Grater reference comparison](../examples/GRATER_VALIDATION_20261013.md) | Compare the same real product photo in the Soft Studio and Photo-real light routes. | The user approved both samples for visible appearance, story, figure scale and aesthetics. Hidden details, exact SKU and microscopic pattern accuracy are not certified. |
| [Paper-cup first steps](QUICK_START.md) | Compare a cup opening used as a train entrance, a circus entrance and an inner theatre; then inspect actual images. | This historical tutorial generated three concepts with permission. None became a complete success example: the train/cup-bottom logic remained unresolved, while other concepts depended on added scenery. For first use, select a concept and explicitly request one image. |
| [Secondary creation](../site/secondary-creation.html) | Follow tissue snow, a notebook-and-pencil bridge and a clothespin diving platform from object relationships to images and feedback. | Preserve each case's actual inputs, edits and limitations; these are examples, not a cross-product success rate. |
| [Coffee-ring track](../site/gallery.html) | See how an object's usage trace supplies the story: a mug's coffee ring becomes a running track. | Object-name input; no product-photo Before. Some runners are not exactly on the ring. |
| [Remote-control tutorial](../site/remote-control.html) | Compare a real reference photo, two results, screen symbols, button shapes and figure contact. | Strict detail fidelity did not pass. Permission to publish is separate from quality approval. |

For provenance and known issues, use [selected cases](../examples/SELECTED.md), the [case index](../examples/README.md) and [material notices](../THIRD_PARTY_NOTICES.md). Original text/configuration use MIT; images are not automatically MIT. The three bundled author-shot figure-reference photos use CC BY-NC 4.0 for those photos only.

## Update and report problems

For a repository with no local changes, the documented update command is `git pull --ff-only`. If you have local changes or branch differences, compare first. ZIP users should extract to a new directory. Updating source does not automatically update an installed copy; compare and preserve your changes before synchronizing, then verify loading in a fresh session.

When reporting a problem, include the host, actual loaded version/path, input, expected result and observed issue. Distinguish unavailable tools, an unclear story, an altered product and oversized figures. Do not include account secrets.

Codex on the tested Mac has evidence for reference-image generation, requested editing and saving. Claude Code has installation/planning evidence, with no built-in generation in the tested environment. On 2026-10-17, project-local Codex installation, upgrade to a frozen development candidate, rollback and uninstall passed in an independent project on the same Mac, including fresh-session file reads and post-uninstall discovery. A separate default user-wide run also passed using published rc2 → v0.1.0 → rc2 → uninstall; fresh sessions read the actual user-wide files from a neutral project. Existing project installs remained unchanged, and all files in the three inspected user-skill roots matched their initial hashes after cleanup, including restoration of temporary host-managed system-file refreshes. Claude passed filesystem operations only. Another machine, cross-system compatibility, other user-wide locations and Claude's fresh-session lifecycle remain unverified. The [installation guide](INSTALL.md) and [validation records](VALIDATION.md) retain the detailed dated evidence.
