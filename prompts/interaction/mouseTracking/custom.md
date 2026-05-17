# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名非常熟悉「滑鼠追踪 / Mouse Tracking」交互模式的资深 UI 设计师兼前端工程师，需要为一个全新的「Mouse Tracking Interaction Playground」页面编写一段可以直接复制给 LLM 使用的完整 Prompt。

你的任务：让 LLM 生成一个与当前 Mouse Tracking 全屏示例界面交互风格高度一致的 HTML 完整页面。页面在布局结构、色彩方向、3D 视差卡片、滑鼠追踪统计信息与粒子尾迹效果上，要与现有 Demo 非常接近，但文案内容、场景设定和具体模块名称都可以替换。

【使用场景设定】
- 场景：一个交互设计团队或前端组件库的「互动动效实验室」，专门用于展示滑鼠追踪效果、3D 视差卡片和光标粒子轨迹。
- 用户：前端工程师、互动设计师、产品经理，以及任何想测试 Mouse Tracking 交互感觉的设计/开发人员。
- 目标：在一个全屏页面中，将「滑鼠追踪全息卡片」作为主角，同时辅助以说明文案和坐标数据显示，使用户既能感受炫酷效果，又能理解交互结构和参数。
- 氛围：安静、深色、高科技、略带科幻感，像是未来 UI Playground，而不是传统企业后台。

【整体页面结构要求】
请引导 LLM 生成一个包含以下结构的完整页面（使用语义化标签与 TailwindCSS 风格类名）：

1. 背景层（Background）
   - 使用 <main> 或包裹容器作为页面根节点，背景为从深灰到纯黑的渐变（例如 from-gray-900 via-black to-gray-900）。
   - 背景中可以加入「粒子画布」层，用于绘制光标粒子尾迹（通过 <canvas> 或绝对定位的容器实现），该层应位于最底层并禁止鼠标事件（pointer-events: none）。
   - 背景整体应传达一种安静的宇宙或数据空间感，为中央主卡片提供对比。

2. 顶部/中部标题区（Intro / Heading）
   - 在视口中居中堆叠一个内容容器，内部顶部为标题与说明文。
   - 标题示例（可自定义）：例如「Mouse Tracking Effects」「Cursor Reactive UI」「Hologram Interaction Lab」，采用较大字号（如 text-5xl / text-7xl）与渐变文字填充（蓝色到紫色的线性渐变，并通过 text-transparent + background-clip 技巧描述）。
   - 副标题用浅灰色文本简要说明：例如「Move your mouse to explore 3D parallax cards and glowing particle trails」，字号略小，可使用 text-gray-400。

3. 核心 Mouse Tracking 卡片区（Core Tracking Card）
   - 在标题下方居中放置一个主要「追踪卡片」容器，与当前 Demo 保持类似结构：
     - 外层容器负责 perspective 与整体旋转（如使用 CSS 变量 --rotate-x / --rotate-y 控制）。
     - 内部为一张较大的矩形卡片，背景为半透明深灰（接近 #111827）配合少量玻璃模糊效果（backdrop-blur），边框为蓝色或紫色发光描边。
     - 卡片边缘外圈有一层柔和的发光边框（Glow），在 hover 时增强亮度；平时则较为克制。
   - 卡片内部至少包含以下内容区块：
     1. 顶部徽章（Badge）
        - 使用「Interactive」「Real-time」「3D Parallax」之类的文案，搭配一个会缓慢脉动的小圆点，代表系统在线。
        - 徽章背景为半透明蓝色矩形，边框轻微发光，文字颜色为浅蓝。
     2. 标题与说明（Card Title & Description）
        - 使用富有未来感或概念感的标题，如「Future Tech」「Live Cursor Field」「Holographic Panel」等。
        - 下方用一两行说明文字概括交互体验，例如「Experience immersive 3D parallax interaction based on cursor position」。
     3. 滑鼠坐标/状态面板（Mouse Stats）
        - 通过两到三个「统计小卡」展示当前鼠标相对于卡片的 X 轴 / Y 轴位置、距离中心的偏移程度等。
        - 每个小卡包含「大号数值」和「小号标签」，例如「240 / X Axis」「120 / Y Axis」，使用等宽字体，强化技术感。
     4. 主调用按钮（Call-to-Action Button）
        - 一个发光的按钮，如「Explore More」「Enable Playground」「Open Docs」等。
        - 按钮使用空心描边 + 内部渐变光晕，hover 时背景略亮、发光增强。

4. 交互行为（Mouse Tracking 交互细节）
   - 卡片需要对鼠标位置产生 3D 视差响应：
     - 根据鼠标在卡片容器中的坐标（相对宽高的比例），计算垂直/水平旋转角度（如最大 ±15 度）。
     - 将计算结果映射到 CSS transform: rotateX / rotateY 上，使卡片在鼠标移动时产生轻微倾斜。
     - 鼠标离开卡片区域时，卡片需平滑返回初始状态（旋转角度回归 0）。
   - 卡片内发光层（Glow）可根据鼠标位置改变偏移方向或亮度，让用户感觉光源跟随指针。
   - 页面文案应明确提示用户「Move your mouse」「Hover to explore」，使交互意图清晰。

5. 粒子尾迹效果（Cursor Particle Trail）
   - 在页面全局监听鼠标移动事件，生成带有寿命与透明度递减的「粒子」：
     - 每个粒子包含：初始位置（接近光标）、随机速度向量、大小、颜色（可以用 HSL 在蓝色与紫色区间内变化）、不透明度。
     - 动画步骤中更新位置、缩小大小、降低透明度，当粒子过小或完全透明时移除。
  - 使用 <canvas> 或绝对定位层配合 requestAnimationFrame 连续绘制粒子，营造「光标拖尾」与「光晕爆点」效果。
   - 注意描述：粒子动画要柔和、半透明，避免遮挡主内容；在移动端或小屏幕可以自动关闭此效果以提升性能。

【色彩与视觉语言】
1. 背景与主色：
   - 背景基调为深色（灰黑到纯黑的渐变），中间可带少量蓝紫光晕，模拟宇宙或数据流场。
   - 主要强调色：浅蓝 (#60A5FA)、紫色 (#A78BFA)，适度搭配青色 (#22D3EE) 作为点缀。
2. 光效与阴影：
   - 标题文字可使用渐变填充与强烈光晕；卡片边缘与按钮可使用外发光阴影，强调科技感。
   - 光效需要相对集中在核心卡片与粒子轨迹上，其余区域保持克制，避免过度花哨。

【交互节奏与性能考量】
1. 动画节奏：
   - 卡片旋转与光晕变化的过渡时间控制在 120–220ms 之间，使用 ease-out 或 ease-in-out。
   - 粒子尾迹的生命周期约 0.6–1.2 秒，形成柔和拖尾而非烟火式爆炸。
2. 响应式策略：
   - 桌面端保留完整 3D 视差与粒子尾迹效果。
   - 平板端可在减少粒子数量的前提下保留主要交互。
   - 移动端可以关闭或弱化 3D 倾斜与粒子（例如固定角度、隐藏 canvas），以确保流畅。

【输出技术要求】
- 最终输出必须是完整 HTML5 文档（包含 <!DOCTYPE html>、<html>、<head>、<body>），不输出任何解说文字。
- 使用语义化标签：<main> 作为页面主体，内部再使用 <section> 分隔标题区与互动区；如有需要，可加上 <header>、<footer>。
- 布局与间距使用 TailwindCSS 风格的原子类（如 min-h-screen、flex、items-center、justify-center、p-8、text-5xl、md:text-7xl、bg-gradient-to-br 等），搭配少量语义化自定义类（如 int-tracking-card、int-card-glow、int-tech-stats）。
- 与滑鼠追踪、粒子效果相关的 JS 代码应直接写在 <script> 标签中，不依赖外部框架；但请在 Prompt 中强调「可以使用原生 JS 事件与 requestAnimationFrame 动画」。
- 通篇要强调：区域结构、色彩语言与互动模式需要让人一眼就能辨认为 Mouse Tracking Interaction 系列的同源变体，而不只是随意的鼠标事件示范。


---

## English Version (en-US)

You are a senior UI designer and front-end engineer who specializes in mouse-tracking and cursor-reactive interfaces. Your task is to write a complete instruction that another LLM can use to generate a full HTML page called “Mouse Tracking Interaction Playground”.

Goal: the generated page must look and feel like a sibling of the existing Mouse Tracking full-page demo (3D parallax card + coordinate readout + glowing particle trail), while using different copy, labels and scenario. The structure, color direction and interaction patterns should remain strongly recognizable.

[Scenario]
- Context: an “Interaction Lab” or “Motion Playground” where designers and developers explore mouse-tracking effects, 3D parallax cards and cursor trails.
- Audience: front-end engineers, interaction designers and product people who care about motion behavior.
- Purpose: place a single hero card and its tracking behavior at the center of the page, with clear messaging and simple real-time metrics that reveal how the interaction works.

[Layout Requirements]
Instruct the LLM to output a complete HTML5 document with the following sections (using semantic elements and Tailwind-like utility classes):

1. Background Layer
   - Use a full-viewport container (e.g., <main>) with a dark gradient background (from gray-900 through black back to gray-900).
   - Add a particle layer (preferably a <canvas> or absolutely positioned overlay) for cursor trails. It must sit behind other content and ignore pointer events.

2. Heading / Intro
   - Center a content column that first shows a large headline, then a short description.
   - The headline might read “Mouse Tracking Effects”, “Cursor Reactive UI”, or “Hologram Interaction Lab” and should use a blue-to-purple gradient fill applied to the text.
   - The subtitle, in muted gray text, briefly invites the user to move their mouse and observe 3D parallax and particle trails.

3. Core Mouse Tracking Card
   - Below the heading, in the center, place a “tracking card” container:
     - The outer wrapper provides perspective and stores rotation values (e.g., via CSS variables).
     - Inside, a medium-large rectangular card with:
       - A translucent dark background (glass-like panel with blur).
       - A thin neon border (blue/purple) and a subtle inner shadow.
       - A glow halo that becomes stronger when the card is hovered.
   - Inside the card, include:
     - A badge row with a small pulsing dot and a label such as “Interactive”, “Live Cursor Field” or “Real-time Tracking”.
     - A title like “Future Tech” or “Holographic Panel” and a one-sentence description of the effect.
     - A stats block that displays at least two values (e.g., X Axis, Y Axis) updated in real time based on cursor position relative to the card.
     - A primary CTA button (“Explore More”, “Open Playground Docs”, etc.) styled as a neon-outlined button with an inner glow layer.

4. Interaction Details
   - Describe how the card should respond to pointer movement:
     - Listen for mousemove events over the card’s container.
     - Compute the cursor’s position relative to the card’s width and height.
     - Map those normalized values to rotation angles for rotateX and rotateY (for example, within ±15 degrees).
     - Apply these values via CSS transforms so that the card tilts in the direction of the cursor, with a smooth, continuous parallax effect.
     - When the pointer leaves the card, smoothly animate rotation back to neutral.
   - The glow layer can shift or brighten slightly based on cursor position or proximity to the card center, reinforcing the holographic feel.

5. Cursor Particle Trail
   - Globally listen to mousemove events.
   - For each event (or every few events), spawn a small group of particles near the cursor position with:
     - Randomized velocity, initial size, hue (within a blue–purple range) and opacity.
     - An update loop that moves them outward, gradually reduces size and fades opacity.
   - Use requestAnimationFrame to continuously clear and redraw particles on the canvas, creating a smooth glowing trail behind the cursor.
   - Mention that on small screens or low-power devices, this effect can be disabled or reduced to protect performance.

[Color & Visual Language]
- Global background: deep gray to black gradient; no bright flat areas.
- Accent palette:
  - Soft blue (#60A5FA), purple (#A78BFA) and optional cyan (#22D3EE) as the main neon tones.
- Apply these colors to the headline gradient, card borders, glow effects, and stats numbers.
- Shadows and glows should be focused around the hero card and particles, leaving other areas darker and calmer.

[Motion & Performance]
- Card rotation and glow transitions should be short (around 120–220ms) and use easing (ease-out / ease-in-out).
- Particle lifetimes around 0.6–1.2s to create a soft trail, not a fireworks explosion.
- Responsive behavior:
  - Desktop: full parallax and particle effects.
  - Tablet: keep parallax but consider fewer particles.
  - Mobile: simplify—e.g., disable rotation and canvas trail, keeping only a static but glowing card.

[Output Requirements]
- Output a complete HTML5 document only (<!DOCTYPE html>, <html>, <head>, <body>).
- Use semantic elements: <main> as the core container, <section> for the hero area and card, optional <header>/<footer> if needed.
- Use TailwindCSS-like utilities for layout and spacing (min-h-screen, flex, items-center, justify-center, p-8, text-5xl, md:text-7xl, bg-gradient-to-br, etc.), plus a small set of semantic custom class names (int-tracking-card, int-card-glow, int-tech-stats, etc.).
- Use plain JavaScript in a <script> tag for mouse tracking and particle animation (no external frameworks).
- Make clear in the overall Prompt that the new layout must feel unmistakably like a variation of the existing Mouse Tracking Interaction page: same family of colors, same 3D parallax behavior, same style of coordinate readouts and glowing cursor trail, but with fresh copy and slightly different composition.
