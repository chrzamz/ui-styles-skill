# Behavioral evaluation scenarios

Run in an isolated temporary project with only the brief, appropriate raw files and the installed skill. Let a fresh agent choose its actions. Inspect artifacts and behavior, not just its explanation. Never mutate a real user profile in an evaluation; use a temporary HOME/XDG_CONFIG_HOME.

| Scenario | Raw request / fixture | Observable success |
|---|---|---|
| First demo, implicit trigger | “Build a small inventory demo for staff who use phones; I don't know design.” No prescribed UI library. | Relevant skill considered before styling; task-appropriate rationale; a working slice rather than a questionnaire; realistic content/state checks |
| Existing Ant Design product | package.json/lockfile, existing theme, a dense order table. “Add an edit form matching the product.” | Reads current theme; reuses controls; no extra UI system; matches focus/invalid/pending states; no global redesign |
| Anime content site | Existing Vue project and licensed artwork. “Make a collection page with character detail dialogs.” | Separates art direction from stack; preserves Vue; composes accessible existing dialogs; no unsupported claim about an anime-specific library |
| New personal profile | User-supplied design and tokens. “Save this as a personal style for future projects.” | Writes only chosen profile scope; preserves originals; no automatic changes to unrelated projects; local snapshot when adopted |
| Cross-agent continuation | Project visual document, theme and linked instructions. “Add settings page.” | Identifies the actual standard before styling and reuses its decisions; avoids re-selecting the system |
| State drift | A screenshot plus an implementation with mismatched disabled/error colors. | Distinguishes screenshot observations from unknown states; fixes actual states and checks interaction |
| Explanation only | “Compare Swiss and Memphis, no files needed.” | Explains using catalog/source material without creating project rules or artifacts |
| Negative control | “Fix this database migration's index name.” | Does not enter the design workflow or install UI dependencies |

Separate explicit skill tests from implicit routing tests. A test that tells the agent to read SKILL.md cannot prove automatic discovery. When measuring routing, expose only the normal metadata and include a negative control. Check fresh sessions in each supported host; agent instructions are guidance, not an enforced hook.

For theme exporters, separately compile/integrate the emitted output against the actual library version and render representative states. Passing Python tests proves neither browser behavior nor support for all library versions. Record the date, host, fixture, observed artifacts and unchecked limits for any published result.

## Requirements-to-design and reusable style cases

Use [trigger-cases.json](trigger-cases.json) for natural-language routing. It includes product creation, existing-page work, mobile forms, accepted requirements, PPT planning and custom brand direction, plus early discovery, copy-only changes, backend/UI logic fixes, color-data conversion and field-definition negatives. Evaluate the actual stage: naming a future visual product alone is not enough to start design.

For native Codex checks, start a fresh ephemeral session for each prompt, retain the ordinary installed skill catalog, and provide no instruction to select this skill. Use isolated local fixtures with no design-routing rule in AGENTS.md. Disable memory and delegation consistently when comparing versions so past tasks and child runs cannot supply the missing route. Record host/model/effort, skill hashes, prompts, fixture, CLI flags, and raw tool events. A successful read of the relevant SKILL.md before the first visual edit is routing evidence; a skill-name announcement alone is not. Mark timeouts inconclusive, not as negative controls passing.

A routing run may stop after a successful skill read; explicitly label it as activation-only rather than a completed design. Let stage-transition and custom-style cases finish to inspect their advice. Check that an accepted requirements list produces a concise optional next step, while a direct build does not add another approval gate. Inspect representative outputs and actual file changes separately before claiming design quality.

Profile lifecycle checks use only temporary project profiles: an accepted custom direction may prompt once to save; an explicit save/update proceeds without repeating that question; upgrades change the requested profile version and decision note, not unrelated profiles or projects. A company label does not imply a new global storage service.
