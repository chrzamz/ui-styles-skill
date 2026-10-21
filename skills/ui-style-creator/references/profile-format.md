# Local style profile

A profile is a reusable recipe, not an automatically enforced user preference. Its directory contains:

```text
<slug>/
  profile.json
  DESIGN.md
  tokens.json     # optional until exact values have been chosen
```

`profile.json` uses `schemaVersion: 1`, a profile revision `version` starting at `1`, a lowercase hyphenated `name`, `scope` (`project` or `user`), a short `description`, and a portable `source` description or public URL. Increment `version` when intentionally editing a saved recipe. The helper does not store source file paths. A project's active specification should record the selected profile and its version; updating a recipe does not automatically update its consumers.

## Visual specification

Write only the decisions that affect implementation. Extend an existing specification rather than duplicating it. Include:

- Product tasks, audience, information density and the intended visual character.
- Source references and which facts were observed versus inferred or proposed.
- Typography including language coverage and fallbacks; color roles; spacing, shape, hierarchy and motion.
- Library/framework decisions and why its existing components meet the product's needs.
- Required component states and content cases for the actual product.
- Responsive behavior and keyboard/focus/reduced-motion expectations.
- Stable style features, allowed variations, and decisions still awaiting validation.

Keep real interactions and business states distinct from decoration. For example, an anime community can have expressive art and typography while retaining conventional readable form fields and menus. Avoid deriving semantics such as success, warning and error solely from the accent color.

For a form, define applicable default, hover, focus-visible, active, disabled, invalid, loading and success appearances; not every component needs every state. Include empty results, long text and interrupted/loading data where relevant. Use the library's proven interaction behavior when it exists, and specify visual adaptations rather than inventing replacement controls. A screenshot only establishes the states it shows.

## Portable token contract, version 1

The optional token file must be a JSON object with these fields. Exact values come from the selected design; this format supplies no default palette. Version 1 rejects unknown keys at every level so a saved profile follows the same structure as the theme exporter. Keep additional component-state decisions in the specification or the project's native theme.

| Field | Type and meaning |
|---|---|
| `schemaVersion` | Integer `1` |
| `name` | Nonempty design name |
| `modes.light` | Required color-role object |
| `modes.dark` | Optional complete color-role object; omit if dark mode has not been designed |
| `typography.fontFamily` | Nonempty CSS font stack |
| `typography.fontSize` | Positive number, px |
| `typography.lineHeight` | Positive unitless number |
| `shape.borderRadius` | Nonnegative number, px |
| `spacing.unit` | Positive number, px |
| `control.height` | Positive number, px |
| `motion.duration` | Nonnegative number, ms |
| `motion.reducedMotion` | Boolean |

Each mode contains nonempty CSS color strings for `background`, `surface`, `text`, `mutedText`, `border`, `primary`, `onPrimary`, `success`, `warning`, `danger`, and `focus`. The creation helper validates this structure; the chosen library adapter must additionally validate whether it can represent the color syntax and values. Saving the profile is not a contrast or accessibility check.

This small shared contract covers common base theme values. Keep component-specific states, unusual palettes, image treatment and typography hierarchies in the specification and the project's real theme configuration. Do not claim this token file alone is a complete design system or that every library has an equivalent token for every field.

## Scope and activation

Project profiles live at `<project>/.ui-styles/profiles/<slug>/`. User profiles live at `${XDG_CONFIG_HOME:-~/.config}/ui-styles/profiles/<slug>/`. The name is 1–64 lowercase ASCII letters/digits separated by single hyphens; path separators and dot segments are invalid.

Selecting a profile copies/adapts its decisions into the active project specification and token file. Reuse an existing `DESIGN.md` or equivalent when present; otherwise use `design/visual-system.md` and `design/tokens.json`. Reference this active specification from the host's project instruction entrypoint. The helper intentionally does not write `AGENTS.md`, `CLAUDE.md`, global configuration, or an active theme: those edits require awareness of the project's existing conventions and requested scope.
