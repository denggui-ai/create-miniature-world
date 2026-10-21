# Miniature World · Miniature Photography Skill

**Turn everyday objects into small worlds with a story.**

An Agent Skill for Codex and Claude Code. It looks for connections in an object's shape, texture and structure, writes the idea as one picture card, then generates the image with the image tools your host already has. Inspired by Tatsuya Tanaka (田中達也) and his 見立 / mitate approach: seeing everyday objects as something else.

[Website](https://denggui-ai.github.io/create-miniature-world/site/) · [Gallery](https://denggui-ai.github.io/create-miniature-world/site/gallery.html) · [English guide](docs/GETTING_STARTED.en.md) · [Download latest](https://github.com/denggui-ai/create-miniature-world/releases/latest) · [中文](README.md) · [日本語](README.ja.md)

| Notebook → bicycle rack | Potato chip → harvest field | Mug → coffee-ring race track |
| --- | --- | --- |
| <img src="examples/notebook-bike-rack.png" width="260" alt="Notebook binding rings become a miniature bicycle rack"> | <img src="examples/potato-chip-harvest.png" width="260" alt="Golden potato chip ridges become a miniature harvest field"> | <img src="examples/mug-coffee-ring-track-20261012.png" width="260" alt="A coffee ring left by a mug becomes a running track for children"> |

AI-generated examples showing the creative direction; product fidelity and known flaws are listed in the [case notes](examples/SELECTED.md) (Chinese).

## Start in 30 seconds

**1. Install** (first install only, when the target folder does not exist yet; if a copy is already installed, back it up and compare first, see [installation](docs/INSTALL.md))

```bash
git clone https://github.com/denggui-ai/create-miniature-world.git
# Claude Code: copy into your project
mkdir -p your-project/.claude/skills && cp -R create-miniature-world/skills/create-miniature-world your-project/.claude/skills/
# Codex: use .agents/skills instead
mkdir -p your-project/.agents/skills && cp -R create-miniature-world/skills/create-miniature-world your-project/.agents/skills/
```

Install only the `skills/create-miniature-world/` folder, not the whole repository.

**2. Open a fresh session and send a product photo with one line** (an object name alone also works)

| Host | Send |
| --- | --- |
| Claude Code | `/create-miniature-world Use this product photo. Show the picture cards first. Do not generate images yet.` |
| Codex | `Use $create-miniature-world with this product photo. Show the picture cards first. Do not generate images yet.` |

**3. Pick a card**, say "Generate card 1, keep the product's appearance", then ask for one focused change after you see the image.

Generation and editing use your host's own image tools. Built-in generation works in Codex/ChatGPT; the tested Claude Code host has none, so it returns cards and prompts you can run in an image tool you already have, then bring back for review. No model, API key or image credits are bundled.

## How to talk to it

| You say | It does |
| --- | --- |
| You choose the idea, make one | Reads the object, compares candidates, picks one and generates when a tool is available |
| Show the picture cards first | Text only: where the camera is, what is huge, who is small, which part becomes what, what is happening |
| Just give me the prompt | Text only, no generation |
| Edit my real photo | First checks whether it can serve as a base (camera near and low, object large in frame, clean surface, soft light); if so, only figures and props are added |
| Make the people smaller | Rescales figures and their props, protecting the product |
| I don't get the story | Rechecks the object link, the action and the spatial relationships; changes the situation if needed |

With a product photo, its visible appearance is protected by default; with only a name, the design is free. Square frame by default; any ratio you specify takes priority. One first image per idea; at most one edit, only on the image you name; no retries or automatic extra images.

## One picture card, two making routes

Planning and shooting are one picture card: where the camera is and what it sees; what is huge; who is small and which part a person is as tall as; which part of the object becomes what and why it reads that way from this camera; what is happening; what is left out. When ideas run short, the skill looks through 20 text-only case cards of Tanaka's works for a similar one and borrows the mechanism, not figure counts, props or titles.

| | Direct generation | Edit the real photo |
| --- | --- | --- |
| When | Only an object name, or the photo cannot serve as a base | A photo that passes as a base |
| Object | Redrawn by the generator; parts and holes may change | Original photo kept; only figures and props are added |
| Review | Two questions first: what is happening; does it look like tiny people in a giant object's world | Also checks the object was not altered |

## More examples and tutorials

- [English first-use guide](docs/GETTING_STARTED.en.md#follow-the-examples), which introduces the case tutorials
- [Orange photo → planet survey](site/orange.html): two concepts, then one edit to shrink the figures (Chinese)
- [Remote control photo → two results](examples/REMOTE_CONTROL_TEST_20261014.md): a real product reference and its fidelity limits (Chinese)
- [All cases and reviews](examples/README.md) (Chinese)

## Requirements and limits

- **Works best** with objects whose outline, texture, structure or opening suggests something else; a product photo helps. Success is not guaranteed by category, and the product's structure is not changed for the story.
- **Product fidelity**: lettering, parts and proportions can still come out wrong, especially with direct generation. An appealing idea is not an exact SKU match.
- **Figures**: scale follows the relationship between a person and a part of the object, not millimetres. Three bundled figure photos are style references only ([notes and license](skills/create-miniature-world/assets/figure-refs/README.md), CC BY-NC 4.0).
- **Local finishing** runs only on request and needs Python 3, Pillow and NumPy; otherwise the original is delivered.
- **What has been verified** for each version is in the [release notes](https://github.com/denggui-ai/create-miniature-world/releases) and the [validation log](docs/VALIDATION.md) (Chinese). Other machines, other platforms and implicit desktop triggering are unverified; no stable success rate is claimed.

## Inspiration and materials

With appreciation for [Tatsuya Tanaka / MINIATURE CALENDAR](https://miniature-calendar.com/about/) and the possibilities of mitate. This project's method is its own synthesis of visual study and experiments, not the artist's published workflow; the case cards contain text and links to the artist's own article pages only, with no copied images. [Preiser](https://www.preiserfiguren.de/) is a useful official reference for figures and poses.

This is an independent project, with no official affiliation or endorsement from the artist, MINIATURE CALENDAR, Preiser or the product brands shown in examples. Code and original text use the [MIT license](LICENSE); images and third-party materials are not automatically covered, see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Versions, feedback and maintenance

The current version, archive, SHA-256 and release notes are on [Releases](https://github.com/denggui-ai/create-miniature-world/releases/latest). Report problems with the [issue template](https://github.com/denggui-ai/create-miniature-world/issues/new?template=bug_report.md): host, loaded version, input, expected and actual result; share only images you may share and never credentials. Maintainers see [MAINTAINING.md](docs/MAINTAINING.md); the only source is `skills/create-miniature-world/`, and installed folders are copies.
