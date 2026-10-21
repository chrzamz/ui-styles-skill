# ui-styles-skill

[简体中文](./README.md) | [English](./README.en.md)

A designer skill that participates in product development: understand the project, recommend visual directions and component libraries, build previews, save a project visual standard, and keep later pages and interaction states consistent. Built for independent makers and people who use agents without a design or development background.

Includes **79 bilingual style records**, custom-style creation, project visual standards and component-library theme adapters. The reference library works offline; current library documentation, online references and dependency installation use the network when needed.

> The existing terminal demo shows the earlier recommendation/prompt workflow. See the current SKILL.md for the expanded workflow.
>
> ![Original recommendation demo](./demo/demo-terminal.gif)

## How it participates

Ask naturally:

- “Build an order-management dashboard for operations staff, with dense tables and forms.”
- “Make an anime collection site. I don't know design; recommend a direction and show it.”
- “Create a product demo using our existing brand and components.”
- “Apply this direction using our Semi Design setup, including loading, error and disabled states.”
- “Save this selected style as a personal recipe for future projects.”
- “Continue with the settings page and keep it consistent.”

The skill enters before the first styled page, demo or UI-library decision. It inspects the project and explains a recommendation. When comparison helps, it shows a few alternatives. For a direct build request, it starts with a representative slice instead of blocking on a design questionnaire.

Library choices follow the actual tasks, framework, component coverage and customization cost. Data-heavy apps may compare Ant Design, Semi, MUI or Arco. Content sites may need lighter primitives. Anime art direction is separate from the behavior library. Suitable existing components take priority. There is no mandatory palette, default shadcn/ui installation, or blanket ban on it.

## A project visual standard across agents

A new project can retain:

```text
design/visual-system.md   # audience, direction, libraries, layout, states and evidence
design/tokens.json        # only when structured reuse helps
src/.../theme.*          # the implementation for the project's actual stack
AGENTS.md                # a short pointer to the visual standard
CLAUDE.md                # import the shared entrypoint when needed
```

Continue an existing authoritative `DESIGN.md` or theme instead of creating competing sources. Markdown captures intent and behavior; tokens or an existing theme own values. Cover applicable hover, focus, disabled, loading, error, empty and selected states, not just primary color and radius.

These files travel with the project and do not require Claude Design. **Automatic discovery is not enforcement**: metadata helps first-use activation, project rules guide later sessions, and real interface checks verify the result. Host configuration may still restrict loading.

See [project standards](references/project-standard.md), [agent integration](references/agent-integration.md) and [visual review](references/visual-review.md).

## Installation

Choose the host and scope you need. Preserve existing installations.

```sh
# Claude Code, user scope
git clone https://github.com/chrzamz/ui-styles-skill.git ~/.claude/skills/ui-styles

# Codex, user scope, following current documented discovery paths
git clone https://github.com/chrzamz/ui-styles-skill.git ~/.agents/skills/ui-styles
```

For project scope, use `.claude/skills/ui-styles` or `.agents/skills/ui-styles` inside the product repository. Other Agent Skills hosts use their own documented discovery paths.

Invoke `/ui-styles` in Claude Code or `$ui-styles` in Codex. Natural-language activation depends on the host/model. For early participation in every project, follow the conditional project/user-rule instructions in [agent integration](references/agent-integration.md). Installation does not silently change global configuration.

After a visual standard exists, the agent can link it into project instructions. This previews changes; add `--write` to apply:

```sh
python3 <skill-root>/scripts/link_project.py --project /path/to/product --design design/visual-system.md --claude
```

## Custom styles: ui-style-creator

The main skill can directly read the bundled [ui-style-creator](skills/ui-style-creator/SKILL.md). It turns ideas, references or an existing project into a reusable style profile.

- Project scope: `<project>/.ui-styles/profiles/<name>/`.
- User scope: `${XDG_CONFIG_HOME:-~/.config}/ui-styles/profiles/<name>/`.
- Profiles hold a design document, metadata and optional tokens, without an invented default palette.
- Personal profiles apply only when a project selects them. Keep a project-local snapshot; changing a personal profile does not silently restyle previous projects.

To expose a separate command, install the complete `skills/ui-style-creator/` folder in the host's skill directory. A nested skill folder is not assumed to register independently.

## Theme exports

A Python 3.9+ standard-library helper provides **base theme mappings** for CSS, Ant Design, MUI and Semi. Use selected project values, check the installed library version, integrate the output and verify real components. Other libraries require their documented version-specific adapters.

```sh
python3 <skill-root>/scripts/export_theme.py design/tokens.json --library antd --output src/theme.ts
```

The helper creates new files only. Semi uses semantic CSS variables and still needs state palette work. Ant/MUI derived states also require inspection. Successful export is not complete state coverage or accessibility acceptance. See [format, mappings and limits](references/theme-adapters.md).

## Repository

| Path | Purpose |
|---|---|
| `SKILL.md` | Main design workflow and activation boundaries |
| `catalog.json`, `prompts/` | 79 style records and 70 custom prompts |
| `references/` | Project standards, integration, library selection, adapters and review |
| `assets/visual-system.template.md` | Portable visual-standard template |
| `examples/` | Token example for explanation/testing, not a default theme |
| `skills/ui-style-creator/` | Self-contained custom-style skill |
| `scripts/` | Project instruction linking and theme export |
| `tests/`, `evals/` | Tool tests and realistic skill scenarios |

The catalog has related/duplicate styles and incomplete tags; 79 is a record count. Inspect descriptions and content. Missing custom prompts do not prevent a new adaptation. Demo layouts provide references; actual page structure follows the product's tasks.

## Development and validation

```sh
python3 -B -m unittest discover -s tests -v
```

Script tests check file boundaries and token mappings. Use [evaluation scenarios](evals/scenarios.md) for skill behavior. The [2026-10-21 validation record](evals/results-2026-10-21.json) covers real-library integration and one independent page-building task. Host activation, other library versions and user visual acceptance still require separate verification.

Contributions should address real usage failures, state coverage, adapters and examples, helping more people design and build their products.

## License

[MIT](./LICENSE) © 2026 chrzamz. See [ATTRIBUTION.md](./ATTRIBUTION.md) for third-party material provenance and rights notices.
