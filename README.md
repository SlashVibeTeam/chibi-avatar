<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="showcase/logo-dark.png">
  <img src="showcase/logo-light.png" alt="Chibi Avatar" width="340">
</picture>

English · [简体中文](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Images: CC BY-NC 4.0](https://img.shields.io/badge/images-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-8A2BE2.svg)](skills/chibi-avatar/SKILL.md)
[![Works with Codex](https://img.shields.io/badge/works%20with-Codex-black.svg)](#requirements)

<img src="showcase/team-row.png" alt="Chibi desk avatars" width="100%">

</div>

<!--
When the public-figure examples are ready, put the images in showcase/examples/, uncomment this block and match the file names.

## Examples

<div align="center">

| <img src="showcase/examples/altman.png" width="220"> | <img src="showcase/examples/dalio.png" width="220"> | <img src="showcase/examples/musk.png" width="220"> |
|:---:|:---:|:---:|
| Sam Altman | Ray Dalio | Elon Musk |

<sub>Unofficial fan illustrations. Not affiliated with or endorsed by the people shown.</sub>

</div>
-->

## What is this

Chibi Avatar is a skill for AI agents. Upload a photo of a person and it draws a big-head, small-body chibi working at a desk, keeping the hairstyle, skin tone, glasses and outfit from the photo.

Make one of yourself, your teammates, or a public figure you like.

## Quick start

**1. Download**

```bash
git clone https://github.com/SlashVibeTeam/chibi-avatar.git
```

**2. Install into Codex**

```bash
mkdir -p ~/.codex/skills && cp -R chibi-avatar/skills/chibi-avatar ~/.codex/skills/
```

**3. Start a new conversation, upload a photo, and type**

```
Use $chibi-avatar to make a chibi avatar from my photo.
```

## Features

| | |
|---|---|
| **One person per image** | A standalone square avatar, about 1024 × 1024 |
| **Keeps your look** | Hairstyle, hair color, skin tone, glasses, accessories and outfit follow the photo |
| **Three scenes** | Wooden desk at home (default) · office workstation · cushion at a low table |
| **Optional extras** | 1–3 desk items · a pet (from a second photo) · transparent background |
| **Self-check** | Checks the face, hands, desk perspective and proportions, and fixes only what's wrong |

Every avatar has a small [SlashVibe](https://github.com/SlashVibeTeam) device on the desk. It's a fixed part of this style.

## More ways to use it

| You want | Say |
|---|---|
| Specific features | `Use $chibi-avatar. Keep my black glasses, home desk, a small coffee cup on the desk.` |
| Add a pet | `Use $chibi-avatar. The first photo is me, the second is my cat. Put the cat beside the desk.` |
| Transparent background | `Use $chibi-avatar. Full-body avatar at an office desk, transparent background.` |
| Edit an existing image | `Only change the cat's eyes to yellow-green. Keep everything else.` |

See [examples](skills/chibi-avatar/references/examples.md) (in Chinese) for more.

## Requirements

Images come from your AI tool's **built-in image generation**. No extra API key is needed.

| Tool | Generates the image directly? |
|---|---|
| **Codex** | ✅ Yes, recommended |
| Other AI tools with built-in image generation and skill support | ✅ Yes |
| **Claude Code** | ⚠️ No. It has no built-in image generation yet, so it gives you the prompt and the list of reference images to use in another image tool |

<details>
<summary>Install in Claude Code</summary>

```bash
mkdir -p ~/.claude/skills && cp -R chibi-avatar/skills/chibi-avatar ~/.claude/skills/
```

Use `/chibi-avatar` instead of `$chibi-avatar`.

</details>

<details>
<summary>Build the prompt without an AI agent</summary>

The repo includes a prompt builder that uses only the Python standard library, with no network and no uploads:

```bash
python3 skills/chibi-avatar/scripts/build_prompt.py --photo ~/me.jpg --scene home
```

Use the resulting prompt and reference image paths in any image tool that accepts reference images. `--scene` can be `home`, `office` or `floor`.

</details>

## Structure

```
skills/chibi-avatar/
├── SKILL.md            # main skill instructions
├── assets/             # style reference, product shape and scale references
├── references/         # style checklist, usage examples
├── scripts/            # prompt builder
└── agents/             # Codex UI config
```

## Credits

Illustration style and skill design: **[Sherry](https://github.com/SherryLi8)** @ [SlashVibe](https://github.com/SlashVibeTeam)

## Disclaimer

- Avatars of public figures made with this skill, including any in this repo, are unofficial fan illustrations. They are not affiliated with or endorsed by the people shown.
- Only use photos you have the right to use. Ask before making an avatar of someone else.

## License

- Code and text (`SKILL.md`, `references/`, `scripts/`, `agents/`, etc.): [MIT](LICENSE)
- Images (`assets/`, `showcase/`): [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). You may use and adapt them with attribution, but not commercially.
