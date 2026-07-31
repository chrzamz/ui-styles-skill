# ui-styles-skill

[简体中文](./README.md) | [English](./README.en.md)

> An offline, ready-to-use UI style library for Claude Code, covering **79 design style families with bilingual prompts (zh-CN / en-US)**. It gives Claude a stronger visual vocabulary when generating frontend UI.

<p align="center">
  <img src="./demo/demo-terminal.gif" alt="ui-styles-skill demo — Claude reads catalog, recommends styles, applies Swiss Design to a project" width="880">
</p>

<p align="center">
  <img alt="styles" src="https://img.shields.io/badge/styles-79-blueviolet">
  <img alt="languages" src="https://img.shields.io/badge/i18n-zh--CN%20%7C%20en--US-brightgreen">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-blue">
  <img alt="claude code" src="https://img.shields.io/badge/Claude%20Code-Skill-orange">
</p>

---

## ✨ What is this?

`ui-styles-skill` packages 79 UI style prompts from the upstream open-source project [TonnyWong1052/UI-Prompt](https://github.com/TonnyWong1052/UI-Prompt) as an offline Claude Code Skill. Once installed, you can ask Claude:

- "I'm building a developer tool website. Recommend three suitable UI styles."
- "Create a login page in the claymorphism style."
- "What's the difference between synthwave and vaporwave?"
- "Try a more retro style."

Claude reads the local catalog, selects suitable candidates, loads the relevant prompt on demand, and generates code according to that style's visual guidelines. The entire workflow runs locally without network requests or browsing an external style library.

## 📦 Installation

### Global installation (recommended)

```bash
git clone https://github.com/chrzamz/ui-styles-skill.git ~/.claude/skills/ui-styles
```

### Project-level installation

```bash
git clone https://github.com/chrzamz/ui-styles-skill.git .claude/skills/ui-styles
```

After installation, enter the following in any Claude Code session:

```text
/ui-styles Recommend styles for a SaaS dashboard
```

You can also trigger the Skill using natural language because its description includes relevant trigger phrases:

> "I need a UI style for a developer tool."

## 🎨 Style catalog overview

| Category | Count | Representative styles |
|---|---:|---|
| `core` | 9 | flatDesign · minimalism · brutalism · memphis · skeuomorphism · materialDesign · fluent2 |
| `visual` | 53 | claymorphism · glassmorphism · neoBrutalism · vaporwave · y2k · bentoGrids · auroraGlass · holographicFoil · sciFiHud · wabiSabi · biophilic · blueprint · popArt … |
| `retro` | 15 | synthwave · arcadeCRT · artDeco · bauhaus · darkAcademia · filmNoir · midCenturyModern · newspaper · retroOS · steampunk · swissDesign · vhsAesthetic |
| `layout` | 1 | magazine |
| `interaction` | 1 | mouseTracking |

> The catalog contains **79 families**. Nine provide only `style.md` for helping the model understand the style and do not include a `custom.md` prompt for direct code generation.

## 🚀 Usage examples

### 1. Ask Claude to recommend styles

> **You:** I'm building a website for an AI coding assistant. Can you recommend three UI styles?
>
> **Claude:** *(reads the catalog and matches tags related to developer tools, minimalism, and technology)*
> 1. **Minimalism** — Generous whitespace keeps the product itself in focus
> 2. **Blueprint** — An engineering-drawing aesthetic with a distinctive technical character
> 3. **Bento Grids** — A modular layout well suited to presenting multiple product features

### 2. Ask Claude to generate code in a style

> **You:** Create a pricing page in the Claymorphism style.
>
> **Claude:** *(reads `prompts/visual/claymorphism/custom.md`, applies its instructions, and outputs HTML, CSS, or React code that follows the style guidelines)*

### 3. Browse or compare styles

> **You:** What's the difference between synthwave and vaporwave?
>
> **Claude:** *(reads and compares the `style.md` sections for both styles)*

## 📂 Project structure

```text
ui-styles-skill/
├── SKILL.md              # Claude Code Skill entry point and workflow
├── catalog.json          # Index of all 79 styles: ID, category, tags, and prompt paths
└── prompts/
    ├── core/
    │   └── <familyId>/
    │       ├── style.md  # Style definition: visual principles, materials, interaction, and mood
    │       └── custom.md # Generative prompt for producing code in the selected style
    ├── visual/
    ├── retro/
    ├── layout/
    └── interaction/
```

Each `style.md` and `custom.md` file contains **zh-CN** and **en-US** sections. Claude selects the appropriate language based on the project context.

## 🧭 Style selection guide

| Use case | Recommended directions |
|---|---|
| B2B tools / SaaS / dashboards | minimalism · flatDesign · fluent2 · bentoGrids · swissDesign |
| Developer tools / technical blogs | minimalism · monochrome · blueprint · retroOS · vhsAesthetic |
| Creative portfolios / designer websites | brutalism · neoBrutalism · memphis · claymorphism · holographicFoil · antiDesign |
| Marketing landing pages / brand websites | gradients · glassmorphism · 3dElements · auroraGlass · bentoGrids |
| Games / entertainment / music | synthwave · vaporwave · neonCyberpunk · retroFuturism · y2k · sciFiHud |
| Retro / nostalgic / editorial | midCenturyModern · swissDesign · newspaper · artDeco · darkAcademia · wabiSabi |
| Nature / wellness / lifestyle | biophilic · organic · natural · scandi · wabiSabi · solarpunk |
| Children / education / cute themes | kawaiiMinimal · claymorphism · paperCutout · handDrawnSketch · comicBook |

## 🤝 Contributing

Contributions are welcome in the following areas:

- **Add a style** — Provide bilingual `style.md` and `custom.md` files and register the style in `catalog.json`
- **Improve an existing prompt** — Make its style description more accurate and easier for the model to follow
- **Add the nine missing `custom.md` files** — See families whose `prompts.custom` value is `null` in the catalog
- **Add trigger scenarios to `SKILL.md`** — Help Claude match requests to styles more effectively
- **Internationalization** — The project currently supports zh-CN and en-US; Japanese, Korean, and other translations are welcome

Please open an issue to align on direction before submitting a pull request. Keep `catalog.json` synchronized with the prompt directory structure in every contribution.

## 📜 Upstream source and acknowledgements

All 79 style prompts in this project come from the upstream open-source project **[TonnyWong1052/UI-Prompt](https://github.com/TonnyWong1052/UI-Prompt)**, which provides the complete design documentation, an online browsing interface, and continuously updated prompt source files. This repository:

1. Organizes the upstream prompts into a directory structure compatible with Claude Code Skills
2. Provides the `catalog.json` index for lower-cost style selection
3. Defines the triggering and output workflow in `SKILL.md`

See [ATTRIBUTION.md](./ATTRIBUTION.md) for details. If this project is useful to you, please also star the upstream repository.

## 📄 License

[MIT](./LICENSE) © 2026 chrzamz

The upstream prompt content remains copyrighted by its original author and is distributed according to the upstream project's terms.
