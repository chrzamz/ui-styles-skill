# A project-owned visual standard

The standard belongs to the product, travels with its repository and can be read by any agent. No Claude Design workspace or proprietary export is required. A file guides an agent; it does not mechanically enforce design quality.

## Files and authority

First inspect existing documents and theme code. Keep the current canonical path if it already serves this purpose. Do not replace an architectural `DESIGN.md` with a visual document merely because the name matches.

For a new system, the small default is:

```text
design/visual-system.md   # product decisions, component/state behavior, evidence
design/tokens.json        # optional: authoritative structured values
src/.../theme.*          # library adapter, following the existing stack
AGENTS.md                # short instruction to read the actual standard
CLAUDE.md                # host bridge when needed, not a copy of the standard
```

One Markdown file is enough for a small demo. Add JSON when code generation or shared values benefit. Existing CSS variables or a library theme can remain authoritative; the document should link to those values instead of duplicating them. The exporter requires explicit resolved values, so an existing theme with aliases must be resolved/adapted deliberately rather than silently flattened into a second source.

## What to retain

- Product users, key tasks and visual goals, with one reason for the chosen direction.
- Framework/library and version from the project; which components are reused and any gaps.
- Font families including Chinese/non-Latin fallback, type hierarchy, spacing, density, shape, elevation, imagery and motion intent.
- Semantic color roles rather than just a palette: action, error, warning, focus and muted content are distinct decisions.
- Relevant component/state combinations: a button's disabled state differs from a text field's invalid state. Do not assume every component has every state.
- Responsive behavior, long labels and realistic empty/error/loading data.
- Source/reference attribution, inferred decisions and unresolved questions.
- Actual implementation and verification evidence; small dated decision notes for material changes.

Use the [template](../assets/visual-system.template.md) as a starting point and remove irrelevant sections. Do not leave placeholders in a delivered standard. A family such as Swiss Design describes a broad tradition; a concrete palette and exact spacing are this project's choices, not universal requirements of that tradition.

## Token interchange used by the starter exporter

`schemaVersion: 1` is this repository's small interchange format, **not a claim of DTCG compatibility**. All listed light-mode color roles and numeric groups are required by the starter exporter; dark mode is optional and, when supplied, has the same roles. If the project needs aliases, multiple brands, component-specific tokens or other color formats, preserve its native representation and write the appropriate adapter instead of distorting the design to fit this subset.

| Field | Meaning |
|---|---|
| `name` | Selected project/profile name |
| `modes.light`, optional `modes.dark` | `background`, `surface`, `text`, `mutedText`, `border`, `primary`, `onPrimary`, `success`, `warning`, `danger`, `focus` |
| `typography` | `fontFamily`, `fontSize` in px, unitless `lineHeight` |
| `shape` | `borderRadius` in px |
| `spacing` | `unit` in px |
| `control` | `height` in px |
| `motion` | `duration` in ms, `reducedMotion` boolean |

See [a complete example](../examples/industrial-light.tokens.json) and [adapter constraints](theme-adapters.md). The example is a test/reference fixture, not the default palette for new projects. Do not manufacture values without a selected direction. Additional states and component decisions remain in the standard and the library's theme/component layer; a base token export cannot replace them.

## Reuse and change

Project standards apply to their documented surface. A personal profile is an optional recipe; selecting it copies or adapts a snapshot into the project so another developer or agent does not need the creator's home directory. Record profile name/version/source, then keep project overrides local. New personal-profile versions do not silently restyle existing products.

For a theme change, inspect consumers and update the values, mapping, representative preview and standard together. For a narrow UI fix, retain the selected system and change only what is needed. Avoid adding new colors, libraries or layout conventions to hide a component-level problem.
