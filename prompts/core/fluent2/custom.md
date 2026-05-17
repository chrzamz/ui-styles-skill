# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名资深 UI 设计师兼前端工程师，请生成一个与当前「Fluent Design 2.0」核心样式卡展示界面风格高度接近的 Fluent 2 风格 UI。
要求：保持整体视觉气质（浅色渐变背景 + 亚克力卡片 + Fluent 蓝）与光影 / 圆角语言基本一致，只允许替换文案、图标和具体模块内容。输出使用语义化 HTML 结构和 TailwindCSS 风格的原子类（或等价的工具类方案）。

【使用场景】
- 场景：Windows 11 风格的轻量信息面板 / 控制面板（如：小仪表板、状态总览卡片）。
- 用户：日常使用桌面应用或 Web 控制台的知识型工作者。
- 目标：在一个紧凑的卡片中展示标题、副标题、状态信息（进度条）和两枚主要操作按钮。

【整体布局结构（参考当前 demo 卡片）】
1. 外层容器
   - 居中展示卡片，周围留有充足空白。
   - 最外层背景使用浅色斜向渐变，例如：from-gray-50 via-slate-50 to-slate-100。
2. 主卡片（Fluent 2 卡片）
   - 最大宽度约 320–400px，左右留出固定内边距（如 p-6）。
   - 卡片内部划分为三部分：
     - 头部：图标方块 + 标题文本。
     - 内容区：说明文字 + 进度条。
     - 底部：两枚操作按钮（主按钮 + 次按钮）。
3. 头部区域
   - 左侧方形图标容器：40x40 像素左右，使用品牌蓝背景 + 白色图标。
   - 右侧为标题文字，字号中等，字体加粗。
4. 内容区
   - 一行说明文字，描述当前状态（例如 “Windows 11 Acrylic Material”）。
   - 一条水平进度条（高度较细），填充为从 Fluent 蓝到浅青色的线性渐变。
5. 底部操作区
   - 两枚按钮水平并排，主按钮使用品牌色填充，次按钮使用浅灰背景。

【色彩与材质】
1. 背景与卡片
   - 页面背景：柔和浅色渐变，如 #f5f7fa → #e8ebf0。
   - 卡片背景：使用半透明浅灰 + 模糊的亚克力材质：
     - background: rgba(243,243,243,0.7)
     - backdrop-filter: blur(30px) saturate(180%);
2. 品牌与强调色
   - Fluent 蓝：#0078D4 作为主按钮和图标底色。
   - 渐变进度条：从 #0078D4 过渡到 #50E6FF。
3. 文本颜色
   - 标题：#242424 深灰。
   - 正文：#605E5C 中灰。

【圆角、阴影与 Fluent 2 光影语言】
1. 圆角系统
   - 卡片与图标容器统一使用 8px 圆角。
   - 按钮使用 4–6px 圆角，保持柔和但不过度圆润。
2. 阴影与高光
   - 卡片阴影：类似 box-shadow: 0 4px 8px rgba(0,0,0,0.12)，营造轻微悬浮感。
   - hover 时阴影加深为 0 8px 16px rgba(0,0,0,0.14)，同时可以略微上移 4px。
3. 边框与描边光
   - 卡片可使用一层细边框 + 外圈渐变描边高光（如当前 demo 中的 ::before 渐变边缘）。

【动效与交互反馈】
1. 动效曲线
   - 所有 hover / active / 宽度变化使用 Fluent 曲线：
     - cubic-bezier(0.4, 0, 0.2, 1) 或 (0.25, 0.46, 0.45, 0.94)，时长 150–300ms。
2. 悬停效果
   - 卡片 hover：轻微上移 + 阴影加深 + 描边高光显现。
   - 主按钮 hover：背景色稍微加深，增加轻微阴影。
   - 次按钮 hover：浅灰背景略微加深，增加轻微阴影。
3. 进度条动画
   - 进度条宽度变化应使用平滑过渡（例如 500ms），避免瞬间跳变。

【输出要求】
- 使用语义化 HTML：外层容器 + 卡片 + header / main / footer 层次清晰。
- 使用 TailwindCSS 原子类描述布局、间距、对齐和颜色（若使用原生 CSS，可在类名中体现语义）。
- 生成的 UI 在「浅色渐变背景 + 亚克力卡片 + Fluent 蓝按钮 + 进度条 + 双按钮布局」这些关键特征上，应与当前 Fluent 2 样式卡的 demo 界面高度接近。


---

## English Version (en-US)

You are a senior UI designer and front-end engineer. Generate a Fluent Design 2 style UI that looks very close to the current “Fluent Design 2.0” core style card demo.
Keep the overall visual character (light gradient background, acrylic card, Fluent blue accents), light and shadow language and rounded corner system essentially unchanged. You may replace text, icons and specific module content, but not the global composition or Fluent 2 visual style. Output semantic HTML and TailwindCSS-style utility classes (or an equivalent utility-first system).

[Usage scenario]
- Context: Windows 11 style lightweight information or control panel (for example a small dashboard or status overview card).
- Users: knowledge workers using desktop apps or web consoles.
- Goal: show a compact summary card with title, subtitle, status information (progress bar) and two main action buttons.

[Layout]
1. Center the card within a full-page light diagonal gradient background, leaving generous whitespace around it.
2. Main card with maximum width around the current demo (roughly 320–400 pixels) and comfortable padding; internally it is divided into:
   - Header row with square icon container on the left and title text on the right.
   - Content row with one line of descriptive text and a thin horizontal progress bar.
   - Footer row with two horizontally aligned buttons (primary and secondary).
3. Icon container is a small square filled with Fluent blue and a simple white glyph; the title text sits to the right with medium size and strong weight.

[Visual style]
1. Page background uses a very soft light gradient (for example from grey to slate tones) to create depth without distraction.
2. Card background is a semi-transparent light grey acrylic surface with noticeable blur and saturation, plus a subtle inner highlight.
3. Use Fluent blue as the main accent for icons, primary button and part of the progress bar; extend to a lighter aqua tint at the end of the bar.
4. Text colors are dark grey for titles and medium grey for body copy so readability stays high on light surfaces.

[Corners, shadows and lighting]
1. Use consistent 8px corner radius on card and icon container; use slightly smaller radii (around 4–6px) on buttons.
2. Cards have a soft shadow that suggests light elevation; on hover, increase shadow and slightly shift the card upward to reinforce depth.
3. Optionally add a subtle outer gradient border or glow around the card, similar to the current demo’s highlight edge.

[Interaction]
1. All hover and active transitions follow Fluent motion curves with durations around 150–300ms.
2. On hover, the card lifts slightly, its shadow deepens and edge highlight becomes more visible; primary button darkens a bit and may gain a slight shadow, while the secondary button’s light grey background deepens subtly.
3. Progress bar width changes should animate smoothly (for example around 500ms) rather than jumping instantly.

[Output requirements]
- Use semantic HTML: outer container, card, and header/main/footer-like inner structure.
- Use Tailwind-style utility classes to describe layout, spacing, alignment and colors; if using plain CSS, ensure class names remain semantic.
- The generated UI must preserve the recognisable traits of the current Fluent 2 core demo: light gradient background, acrylic card, Fluent blue accents, a progress bar and dual-button footer layout.
