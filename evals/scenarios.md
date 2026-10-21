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
