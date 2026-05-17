# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名擅长 Soft UI / Neumorphism 风格的资深 UI 设计师兼前端工程师，需要为一个新的「Soft UI 控制台」编写一段可以直接复制给 LLM 使用的完整 Prompt。

目标：在不复制现有 Demo 文案和业务内容的前提下，让 LLM 生成一个与当前 Soft UI 全页预览（light/dark）在风格上高度一致的仪表盘界面。这个界面必须让人一眼看出是同一体系的 Soft UI：柔和圆角、外凸与内凹阴影、略带磨砂的背景、克制的色彩和舒适的层次。

【整体风格约束】
- 全局采用 Soft UI / Neumorphism 语言：卡片和按钮看起来像从背景表面「压出」或「浮起」，而不是传统的纯扁平或高对比玻璃态。
- 使用圆角较大的组件（如 rounded-2xl / rounded-3xl），阴影柔和、模糊半径大、透明度低，不允许出现生硬和锐利的阴影。
- 颜色体系以低饱和的浅色背景 + 深浅灰度文本为主，可以搭配少量主色（例如柔和的蓝色或紫色），但主色也必须偏柔和，不要霓虹。
- 所有边角和分割线尽量避免纯黑边框，改用「亮边 + 暗边」的光影组合表达层次。

【页面场景设定】
- 新页面的名字可以是 “Soft Studio Dashboard” 或类似的创意工作台，面向设计师、产品人或创作者。
- 用户在这里浏览今日任务、正在进行的项目、简单的统计数据、快速操作区和一个轻量消息/活动流。
- 界面必须支持长时间使用，视觉氛围偏「安静、温和、细腻」，而不是强烈刺激或高对比。

【布局结构要求】
1. 顶部导航栏（Top Bar）
   - 使用浅色背景（例如 #e5ecf5 / #e2e8f0 / #1f2937 的极浅版本）并应用轻微内凹或外凸效果。
   - 左侧放置品牌标识（圆角矩形 + 内阴影 + 简洁图形），右侧放导航链接和用户区（头像 + 名称 + 状态）。
   - 导航项之间用适度间距和浅色分隔符区分，不使用粗边框或强烈下划线。

2. 主内容区域（Main Content）
   - 页面主体使用 max-w-6xl 或 max-w-7xl 水平居中，保持左右留白。
   - 上方区域：一块主控卡片，显示欢迎文案、当前日期/时间、一个主要 CTA 按钮和少量统计信息。
   - 中部区域：2～3 列卡片网格，包含：
     - 项目概览卡片（项目数量、完成率、小型进度条）。
     - 模块化统计卡片（如「本周完成」「待处理请求」等）。
     - 快速操作卡片（创建新项目、打开模板库等）。
   - 下方区域：左右两列布局，左列为任务列表或时间线，右列为活动流或提醒列表，卡片之间使用 consistent gap-6 / gap-8。

3. 侧边/辅助区域（可选）
   - 可以在右侧或底部增加一个窄区域，用 Soft UI 卡片呈现简化日历、番茄钟、状态指示器或主题切换组件。

【色彩与背景】
1. Light 模式建议
   - 背景颜色使用接近 iOS 风格的淡灰或淡蓝灰，如 #e5ecf5、#e2e8f0、#edf2f7 等，配合渐变（from-slate-50 via-slate-100 to-slate-200）。
   - 卡片底色略浅于背景或稍微更亮，例如 #f5f7fb、#f9fafb，通过阴影凸显层次而非靠深色块。
   - 主色可以选用柔和蓝（#4f46e5、#6366f1 的低透明版本）或淡紫（#a855f7 的淡色），用在按钮填充或图标背景。

2. Dark 模式延伸（可选说明）
   - 使用偏蓝灰的深色背景，如 #0f172a、#111827、#1f2933，卡片则使用略浅的板岩灰。
   - 阴影需重新调整：外凸效果通过浅色高光边 + 深色内阴影表达，而不是纯黑阴影。

【Soft UI 阴影与边框设计】
- 对于「外凸」卡片：
  - 使用双向阴影：一侧为深色阴影（如 rgba(15,23,42,0.35)），另一侧为浅色高光（如 rgba(255,255,255,0.9)）。
  - Tailwind 示例可组合：shadow-[8px_8px_24px_rgba(15,23,42,0.25)] 与伪元素/边框模拟高光。
- 对于「内凹」元素（如开关、输入框、数值槽）：
  - 内部使用 inset 阴影：inset 3px 3px 6px rgba(15,23,42,0.25), inset -3px -3px 6px rgba(255,255,255,0.8)。
  - 圆角较大（rounded-full 或 rounded-2xl），让内凹效果更柔软。
- 任何阴影变化都要细腻：避免过于浓重的黑色阴影（如 rgba(0,0,0,0.7)），而应使用偏蓝灰或偏暖灰。

【交互与动效】
- Hover 状态：
  - 卡片在 hover 时可以稍微擡高（translate-y-[-2px] / scale-105），阴影变得稍强，但不要出现生硬的跳动。
  - 按钮 hover 时使用亮度提升和轻微阴影变化，而不是改变色相。
- Active 状态：
  - 按钮按下时可模拟内凹：shadow 减弱并加入少量 inset 阴影，整体略微下沉 1～2px。
- Transition 设计：
  - 统一使用 200～250ms 的过渡时间，easing 使用 ease-out 或 ease-in-out。
  - 禁止使用巨大旋转、弹簧动画等破坏 Soft UI 气质的动效。

【排版与图标】
- 字体选择：
  - 使用现代无衬线字体作为基础，例如系统预设或 Tailwind 默认（Inter 类），透过不同字重营造层次。
  - 标题（如 h1/h2）字重可用 700–800，文字颜色用深灰（#111827 / #0f172a），正文用中灰（#4b5563 / #6b7280）。
- 图标风格：
  - 图标本身保持线性或半填充样式，配合柔和渐变或 Soft UI icon 容器（圆形/圆角矩形背景 + 双向阴影）。

【输出技术要求】
- 使用完整 HTML 结构（<header>、<nav>、<main>、<section>、<aside>、<footer>），并用 TailwindCSS 风格原子类控制布局和间距（如 flex、grid、gap-6、px-6、py-4、rounded-3xl、shadow-*、bg-slate-*、text-slate-*）。
- 不输出解说文字或注释，只输出最终 HTML。
- 结构上必须包含：顶部导航、Hero 区、统计卡片网格、主内容 + 侧栏、（可选）底部区域。
- 视觉上必须清晰传达 Soft UI / Neumorphism 特色：柔和圆角、内外阴影、低饱和度背景、细腻光影，而不是单纯平面扁平化卡片。


---

## English Version (en-US)

You are a senior UI designer and front-end engineer specializing in Soft UI / Neumorphism. Your task is to write a complete, copy-paste-ready instruction for an LLM to generate a full-page Soft UI dashboard.

Goal: Produce a new dashboard page that clearly looks like a sibling of the existing Soft UI previews (light and dark variants). The layout, colors, shadows, and overall atmosphere should all communicate Soft UI: soft rounded corners, subtle extruded surfaces, gentle gradients, and calm, low-saturation tones.

[Global Style Constraints]
- The entire interface uses Neumorphic surfaces: cards and controls appear to be molded from the same base material as the background, either pressed in or raised out.
- Corners are generous (rounded-2xl / rounded-3xl), and shadows are soft with large blur radii and low opacity.
- The color palette is built from light grays and tinted neutrals for backgrounds, with deep gray text and a single soft accent color (blue or purple) for emphasis.
- Edges and separations rely more on paired light/dark shadows than on hard black borders.

[Scenario]
- The page is a “Soft Studio Dashboard” for a creative or product team.
- Users arrive here to monitor key metrics, review current projects, see a list of tasks, and access quick shortcuts.
- The mood is calm, polished, and slightly tactile—more like a modern mobile OS home screen than a dense admin panel.

[Layout]
1. Top Navigation
   - A sticky bar with a light, slightly textured background and minimal elevation.
   - Left: compact logo inside a Soft UI icon container (rounded shape with inner or outer shadow) plus product name.
   - Center: navigation links spaced evenly, using medium-weight typography.
   - Right: notification icon and user profile summary in a small Soft UI pill or rounded container.

2. Hero
   - A prominent Soft UI card near the top acting as a welcome and primary call-to-action area.
   - Contains a strong headline, a short description, and two buttons:
     - Primary: filled pill with accent color and Soft UI shadow.
     - Secondary: outlined or ghost-style Soft UI button.

3. Statistics Grid
   - 3–4 cards in a responsive grid, each a Soft UI tile with icon, metric, and label.
   - Icons sit inside circular or rounded rectangles with inner shadows, suggesting pressed-in controls.

4. Main Content & Sidebar
   - Two-column layout on larger screens, collapsing to a single column on mobile.
   - Main column: project list, kanban-style overview, or timeline.
   - Sidebar: small Soft UI widgets such as a mini calendar, quick actions, or a simple focus timer.

5. Footer (optional)
   - A simple, low-contrast footer with a very light top border shadow and small, muted text.

[Color & Shadows]
- Suggest a grayscale and accent palette (light slates and neutrals, plus one accent) and clearly state that saturation should remain moderate.
- Describe typical outer shadow combinations (e.g., dark shadow bottom-right, light highlight top-left) and typical inner shadow combinations for pressed controls.
- Stress that shadows should feel soft and pillow-like, not harsh or photographic.

[Typography]
- Use a modern sans-serif type system with clear hierarchy: bold, large headings; regular-weight body text; smaller, muted labels.
- Align text left in most content areas to keep the design feeling grounded and functional.

[Interaction & Motion]
- Hover: slight scale-up, position shift, or shadow strengthening—no large rotations or color flashes.
- Active: slight inset motion and reduced outer shadow to simulate pressing into a soft surface.
- Motion timing: 180–240ms with ease-out or ease-in-out curves; no bouncy elastic effects.

[Output Requirements]
- Output only HTML with TailwindCSS-style utility classes for layout and Soft UI styling (e.g., flex, grid, gap-6, rounded-3xl, shadow-*, bg-slate-*, text-slate-*).
- Do not output commentary or explanations.
- The final result must be a complete, self-contained page with navigation, hero, metrics, main content, and secondary panels, and it must immediately read as a Soft UI / Neumorphism interface.
