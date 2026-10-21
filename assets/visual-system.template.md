# Product visual standard

Replace the guidance below with project decisions; remove irrelevant sections. Do not treat the sample token fixture as a default theme.

## Product and scope

State who uses the product, their main task, relevant devices/languages, surfaces covered and the selected direction. Give the reason in product terms. Distinguish a provisional first slice from a user-selected system.

## Implementation and source of truth

Record the framework and component-library versions actually installed, the canonical token/theme paths, reused primitives and any required custom components. Identify the source file to edit and any derived files to regenerate.

## Visual decisions

Document typography and fallback, semantic colors, spacing/density, grid/layout behavior, shape/elevation, imagery and motion. Reference authoritative values in code or tokens instead of keeping duplicate numerical tables. Describe which traits stay stable and which layouts adapt to content.

## Components and states

Replace this starter matrix with the components present in the product. For each applicable state, specify both appearance and behavior; mark remaining design decisions explicitly.

| Component | Applicable states | Design and behavior |
|---|---|---|
| Button/link | default, hover, keyboard focus, pressed, disabled, pending | focus visibility; pending label; prevent duplicate action |
| Input/select | empty, filled, focus, invalid, disabled, read-only | label/help/error placement; preserve entered value |
| List/table | loading, empty, populated, partial/error, selected | layout stability; retry action; long content handling |
| Dialog/menu | open, close, focus, invalid action | keyboard navigation; return focus; overflow behavior |

## Responsive and accessible behavior

Describe layout changes based on real content widths, readable text, keyboard/focus order, contrast checks, non-color status cues and reduced-motion behavior. Include dark mode only if required by the product. Record how Chinese/English text expansion, long names and dense data should behave.

## References and provenance

Link original references or profiles. Separate observed screenshot characteristics, designed extrapolations and behavior verified in a running interface. Do not copy third-party branding or imply a reference site's licensing is known without checking.

## Implementation evidence and changes

Record which representative page and component states were implemented, which viewport/input checks actually ran, results and remaining gaps. For later material changes, record the reason and affected surfaces. Do not label untested design intentions as passed checks.
