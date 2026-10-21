# Miniature World: installation, first image and examples

This guide covers public main and v0.2.2. It turns an everyday object into a tiny story world: paper clips become hurdles, a scissor handle becomes a relay track. It pictures the shot first, then either generates the whole image or adds figures to your own product photo.

## Choose your source

Start with the [English README](../README.en.md). The public repository is [denggui-ai/create-miniature-world](https://github.com/denggui-ai/create-miniature-world). Download and extract its Code → Download ZIP archive, or use the existing clone instructions:

```bash
git clone https://github.com/denggui-ai/create-miniature-world.git
cd create-miniature-world
```

For the released snapshot, use the dedicated ZIP and SHA-256 file attached to [v0.2.2](https://github.com/denggui-ai/create-miniature-world/releases/tag/v0.2.2). Verify the archive against its accompanying checksum before installing. Public main and v0.2.2 include the picture card with four gates, the two making routes and the two-question review. Keep the selected source identifiable; downloading a repository does not install a skill.

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

Public main and the release archive use the Codex display label `微缩摄影 Skill`. The project title is Miniature Photography Skill; the directory and invocation identifier remain `create-miniature-world`. If another label appears, verify the loaded path and version.

## Make your first request

Attach a clear product photo, or start with an object name. In Codex:

> Use $create-miniature-world with this product photo. Show the picture cards first. Do not generate images yet. Please respond in English.

In Claude Code:

> /create-miniature-world Use this product photo. Show the picture cards first. Do not generate images yet. Please respond in English.

With a product photo, the skill protects the visible product appearance by default. With only an ordinary object name, it uses free creation and does not promise to reproduce a particular product. State any features that must remain unchanged. Photos and prompts are processed by your host and its image tool; upload only material you may share with them. The project website displays examples and instructions.

After selecting a card, ask “Generate one image from card 1; preserve the product.” Direct generation defaults to two ideas, one image each. Produce one when only one idea works or an idea/count is specified. One edit at most, only on the image you name; no retries or automatic extra images.

For a text-only start:

> Use $create-miniature-world with an ordinary paper cup. Show the picture cards first. Do not generate yet. Please respond in English.

Use the Claude invocation instead when working in Claude Code. You can also request prompts only. The tested Claude Code environment has no built-in generation: use an image tool you already have, then return the results for review. Reading a photo does not prove that a generation tool can receive it.

## Select, review and refine

Review four things separately: whether the story is readable, whether the visible product is preserved, whether the figures feel tiny beside it, and whether the whole image looks good. Recognition of a clever idea does not establish exact SKU fidelity.

After selection, request one focused change and state what to preserve:

> Keep this image's story, product and composition. Make the people and their related props smaller together, and preserve their contact with the product.

Request one focused edit at a time and review the result before continuing. Editing requires a tool that can edit the selected image; a new text-only generation is not evidence of a faithful edit. If the story does not work, request text-only diagnosis before authorizing more images.

Images default to a square frame; any ratio you specify takes priority. The skill plans the camera, scale and scene for each idea. Figures should feel like tiny painted plastic models beside a giant object; each plan says which part a person is as tall as. Local finishing runs only on request and needs Python 3, Pillow and NumPy; otherwise the original is delivered. Save results under `outputs/` without overwriting inputs.

## Follow the examples

The [online gallery](https://denggui-ai.github.io/create-miniature-world/site/gallery.html) has more than 30 works plus step-by-step tutorials. Captions and detailed records are mainly in Chinese; this table is an English route through them.

| Entry | What to learn | Note |
| --- | --- | --- |
| [Grater reference comparison](../examples/GRATER_VALIDATION_20261013.md) | One real grater photo, two cheese-snow scenes in soft indoor light and warm side light. | The user compared both with the original photo and approved appearance, story, figure size and look. |
| [Paper-cup review](QUICK_START.md) | A cup as a tunnel mouth, a circus tent or a concert hall: how to judge which story comes from the cup itself. | An early (v0.1) comparison; for first use, pick one idea and ask for one image. |
| [Secondary creation](../site/secondary-creation.html) | Tissue becomes a ski slope, a pencil bridges a notebook, a clothespin becomes a diving platform. | Each case shows its input, the image and the feedback. |
| [Coffee-ring track](../site/coffee-ring.html) | A mug's coffee ring becomes a running track: children race, grandma cheers. | Made from the object name only, no product photo. |
| [Remote-control tutorial](../site/remote-control.html) | One photo of an old remote control becomes two tiny worlds: a cooling crew and an eco-mode roundabout. | Compare each result with the original photo to see what to fix next. |

For provenance and known issues, use [selected cases](../examples/SELECTED.md), the [case index](../examples/README.md) and [material notices](../THIRD_PARTY_NOTICES.md). Original text/configuration use MIT; images are not automatically MIT. The three bundled author-shot figure-reference photos use CC BY-NC 4.0 for those photos only.

## Update and report problems

For a repository with no local changes, the documented update command is `git pull --ff-only`. If you have local changes or branch differences, compare first. ZIP users should extract to a new directory. Updating source does not automatically update an installed copy; compare and preserve your changes before synchronizing, then verify loading in a fresh session.

When reporting a problem, include the host, actual loaded version/path, input, expected result and observed issue. Distinguish unavailable tools, an unclear story, an altered product and oversized figures. Do not include account secrets.

Codex on the tested Mac has evidence for reference-image generation, requested editing and saving. Claude Code has installation/planning evidence, with no built-in generation in the tested environment. On 2026-10-17, project-local Codex installation, upgrade to a frozen development candidate, rollback and uninstall passed in an independent project on the same Mac, including fresh-session file reads and post-uninstall discovery. A separate default user-wide run also passed using published rc2 → v0.1.0 → rc2 → uninstall; fresh sessions read the actual user-wide files from a neutral project. Existing project installs remained unchanged, and all files in the three inspected user-skill roots matched their initial hashes after cleanup, including restoration of temporary host-managed system-file refreshes. Claude passed filesystem operations only. Another machine, cross-system compatibility, other user-wide locations and Claude's fresh-session lifecycle remain unverified. The [installation guide](INSTALL.md) and [validation records](VALIDATION.md) retain the detailed dated evidence.
