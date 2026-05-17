# Custom Prompt

## 中文版本 (zh-CN)

设计全息风格界面，创造未来科技感的虹彩投影美学。

**核心视觉特征**：
- 虹彩渐变：使用 linear-gradient 或 conic-gradient 创建彩虹光谱效果，角度在 45-135度之间
- 高光反射：模拟全息投影的镜面反射，使用 background: linear-gradient(135deg, transparent, rgba(255,255,255,0.4), transparent)
- 动态光效：hover 时渐变位置移动，使用 background-position 动画（3-5秒循环）
- 半透明层次：卡片背景使用 rgba 或 hsla，透明度 0.7-0.9
- 边缘光晕：使用 box-shadow 创建彩色外发光，如 0 0 20px rgba(147, 51, 234, 0.5)
- 全息贴纸：小标签或徽章使用完整虹彩效果，模拟真实全息贴纸

**色彩系统**：
- 基础背景：深色（#0a0a1f, #1a0b2e）或宇宙渐变（紫-蓝-品红）
- 虹彩配色：完整光谱 - 红(#ff0080) → 橙(#ff6b00) → 黄(#ffd700) → 绿(#00ff88) → 青(#00d4ff) → 蓝(#6366f1) → 紫(#a855f7)
- 重点色：亮洋红 (#f0f), 电紫 (#b0f), 霓虹蓝 (#0ff)
- 文字对比：纯白 (#fff) 或淡紫 (#e9d5ff) 保证可读性
- 渐变方向：对角线（135deg）或径向渐变创造投影立体感

**布局与组件**：
- Hero 区域：大标题使用渐变文字（background-clip: text），副标题纯白高对比
- 虹彩卡片：backdrop-filter: blur(10px) + 虹彩边框（border-image: linear-gradient）或 box-shadow
- 全息标签：小型彩色徽章，模拟防伪标签效果，配合 transform 轻微倾斜
- CTA 按钮：纯色虹彩渐变背景 + 白色文字，hover 时渐变动画
- 特性网格：3-4列卡片，每个卡片有不同角度的虹彩高光
- 数据展示：使用彩虹进度条或渐变图表

**动画与交互**：
- 虹彩流动：background-position 从 0% 0% 到 200% 200%，持续 4-6秒，linear 或 ease-in-out
- 旋转光效：@keyframes 旋转渐变角度（0deg → 360deg），应用在伪元素 ::before
- 悬停反射：hover 时 box-shadow 扩大，从 0 0 20px 到 0 0 40px
- 闪烁高光：使用 animation-delay 错开不同卡片的动画启动时间
- 视差层次：背景虹彩层固定（background-attachment: fixed），前景内容正常滚动

**技术实现要点**：
- 使用 CSS 自定义属性定义虹彩渐变：--holographic-gradient: linear-gradient(...)
- 伪元素 ::before/::after 创建多层光效叠加
- backdrop-filter 创造模糊透视效果（需配合半透明背景）
- transform: translateZ(0) 开启硬件加速，优化动画性能
- @supports 检测 backdrop-filter 支持，提供降级方案
- 使用 background-blend-mode 混合多层渐变（overlay, screen, color-dodge）

**可读性保障**：
- 文字区域：添加深色半透明背景（rgba(0,0,0,0.5)）作为衬底
- 描边文字：text-shadow: 0 0 10px rgba(0,0,0,0.8) 增强轮廓
- 分层设计：虹彩效果作为装饰层，内容区域使用纯色或半透明白色背景
- 对比检测：确保文字与背景对比度 ≥ 4.5:1（WCAG AA 标准）
- 避免过度：不要全页面都是虹彩，局部使用突出重点

**响应式策略**：
- 移动端：减少渐变复杂度（5色 → 3色），禁用部分动画节省性能
- 平板端：保留主要虹彩效果，简化背景动画
- 桌面端：完整虹彩效果 + 复杂动画
- 使用 @media (prefers-reduced-motion: reduce) 为运动敏感用户提供静态版本

**典型应用场景**：
- 科技产品着陆页：展示 AI、VR、区块链等前沿科技
- 数字艺术平台：NFT 市场、在线画廊、设计作品集
- 游戏/娱乐：赛博朋克主题、未来音乐节、电竞品牌
- 安全认证：会员卡、防伪标识、认证徽章
- 创意工作室：设计机构、动画团队、科技创业公司


---

## English Version (en-US)

Design holographic interfaces that create futuristic iridescent projection aesthetics.

**Core Visual Characteristics**:
- Iridescent gradients: Use linear-gradient or conic-gradient to create rainbow spectrum effects at 45-135 degree angles
- Highlight reflections: Simulate holographic projection mirror reflections with background: linear-gradient(135deg, transparent, rgba(255,255,255,0.4), transparent)
- Dynamic lighting: Animate gradient position on hover using background-position (3-5 second loops)
- Translucent layers: Card backgrounds use rgba or hsla with 0.7-0.9 opacity
- Edge glow: Use box-shadow to create colored outer glow, e.g. 0 0 20px rgba(147, 51, 234, 0.5)
- Holographic stickers: Small tags or badges with full iridescent effects simulating real holographic stickers

**Color System**:
- Base background: Dark tones (#0a0a1f, #1a0b2e) or cosmic gradients (purple-blue-magenta)
- Iridescent palette: Full spectrum - red(#ff0080) → orange(#ff6b00) → yellow(#ffd700) → green(#00ff88) → cyan(#00d4ff) → blue(#6366f1) → purple(#a855f7)
- Accent colors: Bright magenta (#f0f), electric purple (#b0f), neon cyan (#0ff)
- Text contrast: Pure white (#fff) or light lavender (#e9d5ff) for readability
- Gradient directions: Diagonal (135deg) or radial gradients to create projection depth

**Layout & Components**:
- Hero section: Large titles with gradient text (background-clip: text), subtitles in pure white for contrast
- Iridescent cards: backdrop-filter: blur(10px) + iridescent borders (border-image: linear-gradient) or box-shadow
- Holographic tags: Small colored badges simulating security label effects with slight transform tilt
- CTA buttons: Solid iridescent gradient background + white text, gradient animation on hover
- Feature grid: 3-4 column cards, each with different angle iridescent highlights
- Data display: Use rainbow progress bars or gradient charts

**Animation & Interaction**:
- Iridescent flow: background-position from 0% 0% to 200% 200%, 4-6 second duration, linear or ease-in-out
- Rotating light: @keyframes rotating gradient angle (0deg → 360deg), applied to ::before pseudo-element
- Hover reflection: box-shadow expands on hover from 0 0 20px to 0 0 40px
- Flickering highlights: Use animation-delay to stagger animation start times across cards
- Parallax layers: Background iridescent layer fixed (background-attachment: fixed), foreground content scrolls normally

**Technical Implementation**:
- Use CSS custom properties to define iridescent gradients: --holographic-gradient: linear-gradient(...)
- Pseudo-elements ::before/::after create layered light effects
- backdrop-filter creates blur perspective effects (requires semi-transparent background)
- transform: translateZ(0) enables hardware acceleration for animation performance
- @supports detects backdrop-filter support, provides fallback
- Use background-blend-mode to blend multiple gradient layers (overlay, screen, color-dodge)

**Readability Safeguards**:
- Text areas: Add dark semi-transparent background (rgba(0,0,0,0.5)) as backing
- Stroked text: text-shadow: 0 0 10px rgba(0,0,0,0.8) enhances outline
- Layered design: Iridescent effects as decorative layer, content areas use solid or semi-transparent white backgrounds
- Contrast checking: Ensure text-to-background contrast ≥ 4.5:1 (WCAG AA standard)
- Avoid overuse: Don't make entire page iridescent, use locally to highlight key areas

**Responsive Strategy**:
- Mobile: Reduce gradient complexity (5 colors → 3 colors), disable some animations to save performance
- Tablet: Retain main iridescent effects, simplify background animations
- Desktop: Full iridescent effects + complex animations
- Use @media (prefers-reduced-motion: reduce) to provide static version for motion-sensitive users

**Typical Use Cases**:
- Tech product landing pages: Showcasing AI, VR, blockchain and cutting-edge technologies
- Digital art platforms: NFT marketplaces, online galleries, design portfolios
- Gaming/entertainment: Cyberpunk themes, futuristic music festivals, esports brands
- Security authentication: Membership cards, anti-counterfeit labels, certification badges
- Creative studios: Design agencies, animation teams, tech startups
