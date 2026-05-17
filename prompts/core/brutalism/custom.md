# Custom Prompt

## 中文版本 (zh-CN)

请使用 TailwindCSS 创建一个「粗野主义」风格页面，保持黑白高对比、粗描边、硬阴影和不完全对齐的排版。包含：海报式 Hero、醒目标语、Bento 卡组/信息块、CTA，以及列表或表格区。排版使用粗体/等宽、紧字距大写，留白可不均衡，允许轻微错位形成张力。

Design a Brutalism page in TailwindCSS that feels raw, loud, and functional. Use extreme black/white contrast, thick borders (2–4px), hard drop-shadows, and deliberate misalignment. Typography should be bold or monospace, uppercase with tight or even negative tracking. Let whitespace be uneven and allow slight offsets to create visual tension rather than polish.

**Layout & Flow**
- Hero as a poster: massive headline (48–72px), blocky subhead, and one primary CTA plus a secondary text link. Background can be pure white or black; overlay a single geometric band or halftone pattern—avoid gradients.
- Below hero, build a Bento/info grid (2–3 rows) with oversized labels, chunky icons, and asymmetric gutters. Cards may vary in height; permit overlap using negative margins.
- Add a “Facts or List” strip: bullets or a mini table with heavy rules and alternating background stripes.
- Close with a bold CTA bar spanning the width; include contact/social tags in uppercase.

**Color & Surface**
- Base palette: #000000 and #ffffff; optionally one accent (safety yellow #facc15 or warning red #ef4444) used sparingly for badges/CTAs only.
- Backgrounds stay flat; no gradients, no glass. Borders are visible: `border-4 border-black` or inverse. Shadows are short and hard (e.g., `shadow-[8px_8px_0_0_#000]`).
- Accept visible grid lines and alignment “errors” (e.g., 4–12px offsets) as part of the aesthetic.

**Typography**
- Use heavy sans or mono: `font-black tracking-tight uppercase`. Pair with monospace for codes/prices.
- Headlines: 48–72px; body: 15–16px; line-height 1.4–1.5. Avoid soft rounded fonts.
- Allow intentional widows/orphans if they create tension, but keep readability.

**Components**
- Buttons: rectangular, no radius (`rounded-none`), thick stroke, high-contrast hover (invert fg/bg). Active state can nudge 2px down with a reduced shadow.
- Badges/labels: pill-free; use square edges and boxed backgrounds. Consider checkerboard or diagonal stripe fills for emphasis.
- Lists/tables: thick row dividers, zebra stripes (black/white), uppercase headers. Keep numeric columns monospace.
- Media: if using images, frame them with borders and captions; allow slight rotation (1–3deg) to break alignment.

**Motion & Interaction**
- Keep motion minimal and snappy (120–180ms). Hover can invert colors or jump shadow. No easing that feels “cute”; use linear/ease-out.
- Allow micro “jitter” on hover for accent items, but disable on `prefers-reduced-motion`.

**Accessibility**
- Ensure contrast ≥ 4.5:1; avoid gray-on-gray. Provide focus rings in pure black or accent color with 2–3px thickness.
- Do not rely on color alone; use text labels and icons. Maintain logical tab order despite visual misalignment.

**Copy Tone**
- Direct, declarative, sometimes confrontational: “BREAK THE GRID”, “NO FLUFF”, “ACT NOW”.
- Keep CTAs short: “START”, “BUY”, “CONTACT”.

**Tailwind Hints (no code required)**
- Utilities to lean on: `border-4`, `shadow-[8px_8px_0_0_#000]`, `-rotate-1`, `tracking-tight uppercase`, `bg-black text-white` (invert for sections), `grid gap-6 md:grid-cols-3` with mixed row spans.
- Use custom classes for stripe/checker backgrounds (`bg-[repeating-linear-gradient(...)]`) and chunky outlines.

---

## English Version (en-US)

Design a Brutalism page in TailwindCSS that feels raw, loud, and functional. Use extreme black/white contrast, thick borders (2–4px), hard drop-shadows, and deliberate misalignment. Typography should be bold or monospace, uppercase with tight or even negative tracking. Let whitespace be uneven and allow slight offsets to create visual tension rather than polish.

**Layout & Flow**
- Hero as a poster: massive headline (48–72px), blocky subhead, and one primary CTA plus a secondary text link. Background can be pure white or black; overlay a single geometric band or halftone pattern—avoid gradients.
- Below hero, build a Bento/info grid (2–3 rows) with oversized labels, chunky icons, and asymmetric gutters. Cards may vary in height; permit overlap using negative margins.
- Add a “Facts or List” strip: bullets or a mini table with heavy rules and alternating background stripes.
- Close with a bold CTA bar spanning the width; include contact/social tags in uppercase.

**Color & Surface**
- Base palette: #000000 and #ffffff; optionally one accent (safety yellow #facc15 or warning red #ef4444) used sparingly for badges/CTAs only.
- Backgrounds stay flat; no gradients, no glass. Borders are visible: `border-4 border-black` or inverse. Shadows are short and hard (e.g., `shadow-[8px_8px_0_0_#000]`).
- Accept visible grid lines and alignment “errors” (e.g., 4–12px offsets) as part of the aesthetic.

**Typography**
- Use heavy sans or mono: `font-black tracking-tight uppercase`. Pair with monospace for codes/prices.
- Headlines: 48–72px; body: 15–16px; line-height 1.4–1.5. Avoid soft rounded fonts.
- Allow intentional widows/orphans if they create tension, but keep readability.

**Components**
- Buttons: rectangular, no radius (`rounded-none`), thick stroke, high-contrast hover (invert fg/bg). Active state can nudge 2px down with a reduced shadow.
- Badges/labels: pill-free; use square edges and boxed backgrounds. Consider checkerboard or diagonal stripe fills for emphasis.
- Lists/tables: thick row dividers, zebra stripes (black/white), uppercase headers. Keep numeric columns monospace.
- Media: if using images, frame them with borders and captions; allow slight rotation (1–3deg) to break alignment.

**Motion & Interaction**
- Keep motion minimal and snappy (120–180ms). Hover can invert colors or jump shadow. No easing that feels “cute”; use linear/ease-out.
- Allow micro “jitter” on hover for accent items, but disable on `prefers-reduced-motion`.

**Accessibility**
- Ensure contrast ≥ 4.5:1; avoid gray-on-gray. Provide focus rings in pure black or accent color with 2–3px thickness.
- Do not rely on color alone; use text labels and icons. Maintain logical tab order despite visual misalignment.

**Copy Tone**
- Direct, declarative, sometimes confrontational: “BREAK THE GRID”, “NO FLUFF”, “ACT NOW”.
- Keep CTAs short: “START”, “BUY”, “CONTACT”.

**Tailwind Hints (no code required)**
- Utilities to lean on: `border-4`, `shadow-[8px_8px_0_0_#000]`, `-rotate-1`, `tracking-tight uppercase`, `bg-black text-white` (invert for sections), `grid gap-6 md:grid-cols-3` with mixed row spans.
- Use custom classes for stripe/checker backgrounds (`bg-[repeating-linear-gradient(...)]`) and chunky outlines.
