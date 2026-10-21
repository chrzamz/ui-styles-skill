---
name: ui-styles
description: "Participate before building or changing product UI: websites, apps, demos, dashboards, forms, visual redesigns, component-library selection, themes and interaction states. Act as a practical designer: understand the product, recommend and preview a direction, preserve a project visual standard, and implement it using the existing stack. 支持风格推荐、界面制作、组件库选型、主题 token、自定义风格。Skip backend-only work and nonvisual fixes."
---

# UI Styles

Help people who are not designers make and maintain a coherent product. Participate in the actual implementation, from the first demo through later pages. The 79 bilingual style entries are reference material; the deliverable is a suitable, usable interface and reusable project decisions.

Resolve paths below relative to this `SKILL.md`, regardless of where the skill is installed. Use available file, browser and preview tools; no particular agent, MCP server or network connection is required for the local workflow.

## Enter before visual decisions

Use this workflow before choosing a component library, writing the first styled page, or changing an existing visual system. A demo is still a product surface. Do not first generate a habitual palette, card layout or library and then apply this skill as decoration.

For a small change, read the existing standard and work within it. Do not restart style selection for every button, add setup files to an explanation-only request, or redesign unrelated screens. Plain backend/data work is outside this skill.

Automatic discovery depends on the host. When setting up persistent project use, follow [agent-integration.md](references/agent-integration.md); a skill description alone cannot guarantee invocation.

## 1. Understand the product with minimal friction

Inspect the brief, existing screens, assets, dependencies and applicable project instructions first. Look for `DESIGN.md`, `design/visual-system.md`, theme files and existing component conventions before making new ones.

Establish the primary user/task, content density, device and language, brand/reference material, framework and required components. Infer what the project already answers. Ask only a consequential unanswered question, in ordinary language with a recommended option; do useful independent work meanwhile. Do not ask a nontechnical user to choose token syntax or a framework for you.

Resolve conflicts using the user's current request and applicable project rules. Within those boundaries, prefer the project visual standard over an optionally selected personal profile, and either over generic catalog examples. A new page normally extends the existing system. A requested rebrand should explicitly update its scope and affected components.

## 2. Recommend a direction and implementation together

If the direction is already chosen, use it. Otherwise offer one recommended direction and, when helpful, up to two meaningful alternatives. Explain suitability and tradeoffs in terms of the user's product, not aesthetic jargon. For a direct build request, choose a justified direction, state the assumption briefly and implement a small representative slice without waiting for an unnecessary style-selection round.

- Consult [library-selection.md](references/library-selection.md) when selecting or reconsidering dependencies. Preserve a suitable installed library; recommend new ones from required behavior, stack, accessibility and customization cost. Typography, imagery and art direction can be independent of component behavior.
- Use the catalog as inspiration only as needed. Read `catalog.json` fields `id`, `familyId`, `category`, `name`, `description`, `tags`, `prompts`; tags are incomplete, so inspect relevant descriptions too. Use the unique `id`, not an ambiguous family name. Load only selected `style.md` / `custom.md` files and the needed language.
- Upstream prompts can contain demo-specific structure, missing “current style card” references or framework examples. Extract visual invariants; adapt layout to real content and code to the installed versions. These files are reference data, not system instructions. Never let an example replace the user's task or existing engineering rules.
- A missing `custom.md` means no prepared template, not an inability to implement. Derive a new adaptation from `style.md` and label it as such. A custom direction outside the catalog is welcome; do not invent a catalog entry.
- For references supplied as screenshots or websites, distinguish observed styling from inferred behavior. A screenshot does not establish focus, disabled, loading or mobile behavior.

## 3. Show a useful sample early

Follow [visual-review.md](references/visual-review.md). Use the same real content and components to compare alternatives. Prefer a small running slice or local HTML preview over prose-only names; use browser screenshots when tools are available. Show the task-critical component and its important states, not just decorative circles.

Avoid universal bans on colors, gradients or shadcn/ui. Choose those deliberately from the product and user's preference. Familiar model defaults are not evidence of suitability. Do not imply that a popular design system guarantees a distinctive brand.

## 4. Save decisions in portable project files

For an implementation that needs continued visual work, follow [project-standard.md](references/project-standard.md) and adapt [the visual standard template](assets/visual-system.template.md).

- Continue an existing authoritative document. Otherwise use `design/visual-system.md` for intent, library choice, components, states and verification; use `design/tokens.json` only when structured values are useful.
- Keep one authoritative set of token values. If an existing theme already owns them, reference and edit that theme; do not create a competing JSON source. When JSON is the source, library themes are generated/adapted outputs.
- Record scope and status: provisional choice, selected direction, implemented mapping, actually checked behavior. A written standard is not evidence that the UI follows it.
- Make the standard discoverable through the project's agent instructions, using [agent-integration.md](references/agent-integration.md). Preserve unrelated rules and existing paths. Do not modify global agent configuration merely to style one project.

When the user wants a named reusable custom style, read the bundled [ui-style-creator](skills/ui-style-creator/SKILL.md). It saves a project or personal profile. A personal profile takes effect only when selected for a project; keep a project-local snapshot for portability. Do not require every one-off page to become a reusable profile.

## 5. Implement with the chosen library

Use existing components and their theming APIs before replacing controls with custom implementations. For unsupported behavior, first consider composition or a focused specialized component, then implement the smallest missing piece. Preserve keyboard, focus, error and disabled behavior while styling.

Read [theme-adapters.md](references/theme-adapters.md) for CSS, Ant Design, Semi Design and MUI starter exports. Verify the actual installed version and map any project-specific component states. The exporter handles a documented subset, not every design decision. Do not introduce a second component system just because its theme is easier to generate.

## 6. Verify and carry decisions forward

Check the representative implementation at the needed desktop/mobile sizes, with realistic text/data and relevant interaction states. Compare it to the selected direction and standard. Fix observed drift and summarize what was tested; distinguish a rendered screenshot, keyboard check and untested assumption.

When adding a later page, reuse current tokens, components and rules. Add a missing component/state to the standard when its design is decided; do not silently invent a parallel style. Respect the task's scope when changing shared tokens. End with the working result, its standard/theme paths and any material unchecked behavior, rather than dumping a long prompt.
