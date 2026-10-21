# Preview and verify the actual design

## Before implementing the whole product

Make the first sample representative of the user's task: a compact table/filter/editor for an operations tool; a typography/product/story section for a marketing site; artwork, catalog navigation and a readable detail block for an anime community. Abstract swatches help show color and material, but do not prove a usable interface.

When comparing alternatives, keep text, data, component set and viewport constant. Explain the meaningful tradeoff and recommend one. Build with the existing app if practical; otherwise a small self-contained HTML sample can demonstrate art direction. Label a standalone mockup as a mockup, not as completed application integration. Use local assets or appropriate licensed assets and preserve attribution.

If the user has asked to build directly, do not turn sample selection into a mandatory approval gate. Pick the best-supported direction, implement the slice, and allow corrections before expanding. If the user specifically asks to choose first, present the previews and wait for that choice.

## Check what changed

Use the available browser and rendering tools. Check the actual DOM/interaction when relevant; a screenshot alone cannot prove keyboard behavior or readable error announcements.

| Concern | Representative check |
|---|---|
| Product fit | Can the intended user find and complete the main action? |
| Identity | Are the selected typography, spacing, shape and imagery visible? |
| Consistency | Do new components reuse the same semantic roles and patterns? |
| States | Exercise applicable focus/pressed/disabled/pending/invalid/empty/error states |
| Content | Long Chinese/English labels, real numbers, empty and crowded data |
| Size | Needed wide and narrow layouts; navigation and dialogs remain usable |
| Accessibility | Keyboard order/focus, meaningful labels, contrast, non-color cues |
| Motion | Respect reduced-motion needs; avoid depending on animation for meaning |

For a tiny spacing change, check the affected component and layout; do not rebuild a full test suite. For a new theme or shared token, include consumers with different states and sizes. Keep evaluation proportional to impact.

Report verified observations and untested gaps separately. No browser available means render/interaction checks are pending, not passed. Do not use the agent's own aesthetic score as acceptance evidence. Ask for the user's visual preference when that is the actual decision; use observable checks for implementation quality.
