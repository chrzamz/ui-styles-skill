# Enter early across agents

Checked against official documentation on 2026-10-21. Host versions and policy can change loading behavior. These are integration instructions, not a promise that a prompt enforces compliance.

## Two layers

1. Install the skill in a location the host discovers. Its description covers building demos, pages, themes and selecting UI libraries, not just requests containing the word “style”.
2. Put a short rule in the consumer project's instruction file, pointing to its actual visual standard. This is what keeps later sessions aligned even when a skill is not selected.

Codex uses skill descriptions for implicit selection and reads applicable `AGENTS.md` before work. Local skill locations currently include project/user `.agents/skills`. Claude Code uses `.claude/skills` and `CLAUDE.md`; recent versions also read `AGENTS.md` under documented conditions. A `CLAUDE.md` import of `@AGENTS.md` provides a bridge when needed. Do not assume that an arbitrary `DESIGN.md` filename is automatically loaded by every agent.

## A consumer-project rule

Adapt the path to the existing standard. Keep the rule short:

```markdown
## Product UI
Before building or visually changing a page, demo, component, interaction state,
theme, or UI-library choice, read design/visual-system.md and its linked theme
sources. Use the installed ui-styles skill when available. Preserve the chosen
visual system and component library; extend missing states consistently. If no
direction exists, establish a justified first slice before styling the rest.
Backend-only and nonvisual fixes do not require a design workflow.
```

The [link helper](../scripts/link_project.py) inserts/updates only its marked block in the target project's `AGENTS.md`; it can add a `CLAUDE.md` import. It preserves unrelated text, refuses malformed markers and symlinked instruction files, and requires the visual document to exist inside the chosen project. It previews by default:

```sh
python3 <skill-root>/scripts/link_project.py --project /path/to/product --design design/visual-system.md --claude
python3 <skill-root>/scripts/link_project.py --project /path/to/product --design design/visual-system.md --claude --write
```

Use `--write` within an authorized project setup or implementation. Do not introduce a new approval step for an already authorized reversible setup. If the project already has an equivalent rule or uses different scoped instruction files, edit those minimally instead of duplicating them. Read subdirectory rules too.

For another agent, use its documented project-rule entrypoint to link the same standard. Verify a fresh session can identify the standard and use it for a small UI change. Do not claim cross-agent behavior from file creation alone.

## Starting every new project

A user who explicitly wants this workflow as their general UI preference may add an equivalent conditional rule to their host's user instructions. Avoid brand values in global instructions; keep those project-local or in selected profiles. Installing this repository does not silently edit user instructions. Without a project or user entrypoint, first-use activation remains metadata-based and may be missed; explicit invocation is the fallback.

## Bundled creator discovery

The main skill can read `skills/ui-style-creator/SKILL.md` directly. Do not assume that putting a skill inside another skill registers a separate command. To expose it independently, copy that complete, self-contained folder into a host's project or user skills directory as `ui-style-creator`. Preserve any existing installation; do not merge two versions without inspecting them.

## Sources

- [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills)
- [Codex project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code shared instructions and imports](https://code.claude.com/docs/en/memory#share-one-file-with-other-coding-tools)
