# Attribution

## Upstream source

All 79 UI style prompt families bundled under `prompts/` are mirrored from:

> **TonnyWong1052/UI-Prompt** — https://github.com/TonnyWong1052/UI-Prompt

The original repository contains:

- The canonical `style.md` / `custom.md` source files for each style
- An online browser UI to preview each style
- Ongoing curation and additions

If you use this Skill in a project, please consider:

1. **Starring the upstream repository** to support the original author
2. **Linking to upstream** when you ship a product built with one of these styles
3. **Sending corrections / new styles upstream first** so the whole community benefits

## What this repository adds on top of upstream

This project packages the upstream reference material and adds a product-design
workflow for agents that support skills and project instructions:

| Component | Source | Notes |
|---|---|---|
| `prompts/<category>/<familyId>/style.md` | TonnyWong1052/UI-Prompt | Mirrored 1:1 |
| `prompts/<category>/<familyId>/custom.md` | TonnyWong1052/UI-Prompt | Mirrored 1:1 |
| `catalog.json` | This repo | Lightweight index — id / category / tags / prompt paths |
| `SKILL.md` / `references/` | This repo | Product-design workflow, library selection, portable standards and verification |
| `scripts/` / `assets/` / `examples/` | This repo | Project integration helpers, starter theme adapters and templates |
| `skills/ui-style-creator/` | This repo | Project/user custom-style profiles |
| `tests/` / `evals/` | This repo | Tool validation and behavioral evaluation scenarios |
| `README.md` / `README.en.md` / `LICENSE` / `ATTRIBUTION.md` | This repo | Open-source project documentation |

## Snapshot version

- Upstream snapshot taken: **2026-05** (see `catalog.json` → `version`)
- Total families: 79
- Families with both `style.md` and `custom.md`: 70
- Families with only `style.md`: 9 (no prepared code-generation prompt;
  an agent can still create and identify a new adaptation from the definition)

## License

- This repository's scaffolding (catalog, SKILL.md, README, etc.) is MIT licensed
  — see [LICENSE](./LICENSE).
- The mirrored prompt content under `prompts/` retains the copyright of the
  upstream authors and is redistributed under the terms of the upstream project's
  license. If you intend to use the prompts for commercial purposes, please
  verify the upstream license at the time of use.

## Resyncing with upstream

To pull in new styles or updates from upstream:

1. Diff the upstream prompt directories against this repo's `prompts/`
2. Apply additions / changes file-by-file
3. Regenerate or hand-edit `catalog.json` so the index stays in sync
4. Bump `catalog.json` → `version` and document the snapshot date here
