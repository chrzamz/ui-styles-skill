# Custom Prompt

## 中文版本 (zh-CN)

请使用 TailwindCSS 创建一个「滚动叙事 Scroll Narrative」页面，让用户在滚动中体验分镜式故事与可视化重点。

**核心设计要求**

1. **封面 Hero（层叠视差）**
   - 前景：标题 40-64px、子标题 18-22px、主次 CTA（主色填充 + 反色描边）。
   - 背景：2-3 层视差渐变/网格，速度 0.3x/0.6x/1x。
   - 参考 CSS：
     ```css
     .scroll-hero { position: relative; min-height: 80vh; }
     .scroll-hero::before { content: ""; position: absolute; inset: -10% 0 0; background: radial-gradient(circle at 20% 30%, #5eead4 0%, transparent 40%), radial-gradient(circle at 80% 40%, #60a5fa 0%, transparent 35%); filter: blur(40px); transform: translateY(-6vh); }
     .scroll-hero .cta-primary { @apply bg-indigo-500 text-white rounded-full px-6 py-3 shadow-[0_10px_40px_rgba(76,106,255,0.35)]; }
     .scroll-hero .cta-secondary { @apply border border-white/40 text-white/90 rounded-full px-5 py-2; }
     ```

2. **节奏分镜 (3-5 段)**
   - 每段：章节编号 + 标题 28-34px + 2-3 行正文 + 深链按钮。
   - 左文右图或左右交错；图可用插画/数据卡片。
   - 滚动动画：`translate-y-10` → `translate-y-0` 与淡入，duration 500-700ms，stagger 120ms。
   - 参考 CSS：
     ```css
     .story-step { @apply grid grid-cols-1 lg:grid-cols-2 gap-10 items-center; }
     .story-step[data-active="true"] { @apply translate-y-0 opacity-100; transition: all 0.6s ease; }
     .story-step[data-active="false"] { @apply translate-y-8 opacity-0; }
     ```

3. **Sticky / Pinned 关键信息**
   - 右侧或左侧保留「摘要/进度」栏，滚动时保持视口内。
   - 包含章节导航点、当前章节标题、操作按钮。
   - 参考 CSS：
     ```css
     .sticky-nav { position: sticky; top: 96px; }
     .progress-rail { @apply relative h-full w-[2px] bg-white/10; }
     .progress-dot { @apply w-3 h-3 rounded-full bg-sky-400 shadow-[0_0_0_6px_rgba(125,211,252,0.18)]; }
     ```

4. **可视化/媒体插入**
   - 支持图表、视频或 3D 截图，统一留 16-24px 内边距，圆角 20px。
   - 为视频/图表添加遮罩渐变，避免与文本冲突。
   - 参考 CSS：
     ```css
     .media-card { @apply relative rounded-2xl overflow-hidden bg-slate-900/60 border border-white/10 shadow-[0_20px_80px_rgba(0,0,0,0.35)]; }
     .media-card::after { content:""; @apply absolute inset-0 bg-gradient-to-t from-slate-950/50 to-transparent; }
     ```

5. **滚动引导与分隔**
   - 在段落之间加入「轻分隔」：细线 + 小徽章文本。
   - 在首屏底部放置「Scroll 提示」动画 (chevron+dot)。

6. **响应式与降级**
   - <768px：禁用重度视差，改用静态渐变；图文改为上下排。
   - 控制阴影/模糊强度，移动端减半，确保性能。

7. **交互与可访问性**
   - 所有 CTA 有 `:hover` 提升亮度与轻微擡升，`:focus-visible` 外框。
   - 对比度 >= 4.5:1；文本行高 1.6-1.8，字距 0.01-0.04em。

**配色方案（夜空霓虹）**

主色调：
- 靛蓝高光：#6366f1, #4f46e5
- 青绿流光：#22d3ee, #5eead4
- 玫红点缀：#f472b6, #fb7185

中性色/功能色：
- 背景：#0b1020, #0f172a, #111827
- 文本：#e5e7eb, #cbd5e1
- 分隔/描边：rgba(255,255,255,0.08-0.16)

**关键 CSS 类示例**

```css
.scroll-shell { @apply min-h-screen bg-[#0b1020] text-slate-100 overflow-hidden; }
.scroll-grid { @apply max-w-6xl mx-auto px-6 lg:px-10 py-16 lg:py-24; }
.chapter-badge { @apply inline-flex items-center gap-2 text-xs uppercase tracking-[0.2em] text-sky-200 bg-white/5 border border-white/10 rounded-full px-3 py-1; }
.cta-ghost { @apply inline-flex items-center gap-2 text-sky-100 border border-sky-200/40 rounded-full px-4 py-2 hover:border-sky-200/70 hover:bg-sky-200/10 transition; }
.scrim { background: radial-gradient(circle at 30% 20%, rgba(94,234,212,0.25), transparent 40%), radial-gradient(circle at 70% 10%, rgba(99,102,241,0.25), transparent 45%); filter: blur(32px); }
```

**版式与节奏**
- 基线网格：8px；段落间距 48-72px；段落内行距 20-28px。
- 标题层级：H1 48-64px / H2 32-40px / H3 22-26px；字体粗细 600-800。
- 容器宽度：1200-1280px；行宽 58-72 字符。

**重要提示**
- sticky 区域预留 top = header 高度 + 24px。
- 视差层控制 transform: translateY(-10vh~-4vh)，避免过度眩晕。
- 移动端关闭 heavy blur（>20px）与大阴影。
- CTA 最多两个，保持层级明确。
- 确保滚动驱动动画可被关闭（尊重 prefers-reduced-motion）。


---

## English Version (en-US)

Create a “Scroll Narrative” page in TailwindCSS so users experience storyboard-like beats while scrolling.

**Core Design Requirements**

1. **Parallax Hero**
   - Foreground: headline 40–64px, subhead 18–22px, primary/secondary CTAs.
   - Background: 2–3 parallax gradient/grid layers at 0.3x/0.6x/1x speeds.
   - Sample CSS:
     ```css
     .scroll-hero { position: relative; min-height: 80vh; }
     .scroll-hero::before { content: ""; position: absolute; inset: -10% 0 0; background: radial-gradient(circle at 20% 30%, #5eead4 0%, transparent 40%), radial-gradient(circle at 80% 40%, #60a5fa 0%, transparent 35%); filter: blur(40px); transform: translateY(-6vh); }
     .scroll-hero .cta-primary { @apply bg-indigo-500 text-white rounded-full px-6 py-3 shadow-[0_10px_40px_rgba(76,106,255,0.35)]; }
     .scroll-hero .cta-secondary { @apply border border-white/40 text-white/90 rounded-full px-5 py-2; }
     ```

2. **Story Beats (3–5)**
   - Each beat: chapter badge, 28–34px title, 2–3 lines of body, deep-link CTA.
   - Alternate left/right layouts; pair with illustration/data card.
   - Scroll animation: fade + translate-y, 500–700ms, stagger 120ms.

3. **Sticky Summary / Progress**
   - Keep a pinned rail with chapter dots, active label, actions.
   - Use sticky top 96px; highlight active node.

4. **Media Blocks**
   - Video/chart blocks with 16–24px padding, 20px radius, gradient scrim overlay.
   - Keep contrast between text and media.

5. **Scroll Cues & Dividers**
   - Add light separators between beats and an animated “Scroll” cue at fold.

6. **Responsive & Performance**
   - Mobile: disable heavy parallax, reduce blur/shadow, stack content vertically.
   - Prefer GPU-friendly transforms; avoid massive box-shadows.

7. **Interaction & A11y**
   - Clear hover/focus states; focus-visible outline.
   - Contrast ≥ 4.5:1; line-height 1.6–1.8; letter-spacing 0.01–0.04em.

**Color System (Night Neon)**
- Primary: #6366f1, #4f46e5, #22d3ee, #5eead4, #f472b6
- Base: #0b1020, #0f172a, #111827; Text: #e5e7eb, #cbd5e1; Border: rgba(255,255,255,0.08-0.16)

**Key CSS Classes**
```css
.scroll-shell { @apply min-h-screen bg-[#0b1020] text-slate-100 overflow-hidden; }
.scroll-grid { @apply max-w-6xl mx-auto px-6 lg:px-10 py-16 lg:py-24; }
.chapter-badge { @apply inline-flex items-center gap-2 text-xs uppercase tracking-[0.2em] text-sky-200 bg-white/5 border border-white/10 rounded-full px-3 py-1; }
.cta-ghost { @apply inline-flex items-center gap-2 text-sky-100 border border-sky-200/40 rounded-full px-4 py-2 hover:border-sky-200/70 hover:bg-sky-200/10 transition; }
.scrim { background: radial-gradient(circle at 30% 20%, rgba(94,234,212,0.25), transparent 40%), radial-gradient(circle at 70% 10%, rgba(99,102,241,0.25), transparent 45%); filter: blur(32px); }
```

**Layout & Rhythm**
- 8px spacing grid; 48–72px beat spacing; 20–28px paragraph spacing.
- Headings: H1 48–64px / H2 32–40px / H3 22–26px; weight 600–800.
- Container 1200–1280px; line length 58–72 characters.

**Important Notes**
- Reserve sticky offset = header height + 24px.
- Parallax offsets between -10vh and -4vh; reduce on mobile.
- Disable heavy blur/shadow on small screens; honor prefers-reduced-motion.
- Limit CTAs to two levels; keep hierarchy clear.
- Ensure media overlays keep text legible.
