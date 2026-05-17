# Custom Prompt

## 中文版本 (zh-CN)

设计氛围光效界面，通过柔和的渐变光球和环境光晕创造沉浸式视觉体验。

**核心视觉特征**：
- 大尺寸光球：使用径向渐变创建 400-800px 的柔光球体
- 模糊扩散：filter: blur(80-150px) 创造光晕效果
- 多层叠加：3-5个不同颜色和大小的光球叠加，使用 mix-blend-mode
- 缓慢流动：光球位置慢速动画移动，创造呼吸感（15-30秒循环）
- 低对比度：整体色彩柔和，避免刺眼的高饱和度色
- 前景清晰：内容卡片与背景光分离，保持可读性

**色彩系统**：
- 背景底色：
  - 深色主题：#050505, #0a0a1a, #0d0d1d（纯黑或深蓝黑）
  - 暖色主题：#1a1612, #1a1410（深棕褐色）
- 光球色彩：
  - 冷色调：深蓝 (#1e3a8a), 紫色 (#5b21b6), 青色 (#0e7490)
  - 暖色调：橙色 (#c2410c), 粉色 (#be185d), 黄色 (#ca8a04)
  - 中性调：灰蓝 (#334155), 灰紫 (#4c1d95)
- 前景卡片：
  - 半透明背景：rgba(255,255,255,0.05) 或 rgba(0,0,0,0.3)
  - 模糊玻璃：backdrop-filter: blur(10px)
  - 边框光晕：border: 1px solid rgba(255,255,255,0.1)
- 文字颜色：
  - 标题：#f5f5f5 或 #e0e0e0（柔和白）
  - 正文：#d0d0d0 或 #b0b0b0（降低对比度）
  - 强调：与光球相呼应的品牌色

**光球技术实现**：
- 径向渐变光球：
  ```css
  background: radial-gradient(
    circle at center,
    rgba(147, 51, 234, 0.3) 0%,
    rgba(79, 70, 229, 0.2) 30%,
    transparent 70%
  );
  ```
- 多层叠加：
  ```css
  .light-orb-1 { mix-blend-mode: screen; }
  .light-orb-2 { mix-blend-mode: color-dodge; }
  .light-orb-3 { mix-blend-mode: lighten; }
  ```
- 模糊扩散：filter: blur(100px) saturate(1.5)
- 绝对定位：position: absolute，z-index: -1 置于背景层

**布局与组件**：
- Hero 区域：大标题居中，背景 2-3个大光球缓慢移动
- 特性卡片：
  - 半透明玻璃卡片，悬浮于光球之上
  - 使用 backdrop-filter: blur(10px) 模糊背景
  - 卡片内容高对比度，确保可读性
- 网格布局：2-3列卡片，每列错位排列增加层次感
- 统计数据：大数字 + 小标签，配合微弱光晕背景
- CTA 按钮：柔和渐变背景，hover 时增加光晕强度
- 导航栏：顶部固定，半透明背景 + 模糊效果

**动画与交互**：
- 光球流动动画：
  ```css
  @keyframes float {
    0%, 100% { transform: translate(0, 0); }
    50% { transform: translate(100px, -80px); }
  }
  animation: float 25s ease-in-out infinite;
  ```
- 呼吸效果：光球大小缓慢放大缩小（scale 0.9 ↔ 1.1）
- 色相旋转：使用 filter: hue-rotate() 让光球颜色缓慢变化
- 鼠标视差：光球跟随鼠标微微移动（transform: translate）
- 卡片悬停：hover 时 backdrop-filter 强度增加，阴影增强
- 淡入效果：页面加载时光球从透明淡入（opacity 0 → 1，2-3秒）

**光晕分层系统**：
- 背景层（z-index: -2）：最大最模糊的光球，作为环境光
- 中间层（z-index: -1）：中等大小光球，提供主要色彩
- 前景层（z-index: 0）：内容卡片和文字
- 装饰层（z-index: 1）：小型光点或星点装饰

**可读性保障**：
- 内容区域背景：添加深色半透明遮罩（rgba(0,0,0,0.4)）
- 文字区域分离：重要文字远离最亮的光球中心
- 高对比文字：标题使用 #fff，正文至少 #d0d0d0
- 文字阴影：text-shadow: 0 2px 12px rgba(0,0,0,0.8) 增强辨识度
- 模糊玻璃卡片：使用 backdrop-filter 让背景光柔化，不影响卡片内文字

**光球配置建议**：
- 主光球：600-800px，位置偏左上或右上，颜色为主题色
- 辅助光球1：400-600px，位置相反对角，颜色为互补色
- 辅助光球2：300-500px，位置页面中下部，颜色为中性色
- 光球不要过多：最多 3-4个，避免视觉混乱
- 光球位置：至少 30-40% 在视口外，创造无限延伸感

**性能优化**：
- 使用 CSS 渐变而非图片：减少资源加载
- will-change: transform, filter 提示浏览器优化
- 减少模糊半径：移动端使用 blur(60px) 代替 blur(120px)
- 降低动画复杂度：移动端减少光球数量（3个 → 2个）
- 使用 transform 代替 top/left：避免触发 layout reflow
- 懒加载：仅在视口内的光球启用动画

**响应式策略**：
- 移动端（< 768px）：
  - 光球数量：3个 → 2个
  - 模糊半径：120px → 60px
  - 光球大小：600px → 400px
  - 禁用鼠标视差效果
  - 简化动画（仅位置移动，无大小变化）
- 平板端（768px - 1024px）：
  - 保留主要光球效果
  - 轻度简化动画
  - 光球大小：600-700px
- 桌面端（> 1024px）：
  - 完整光球效果
  - 复杂动画 + 鼠标交互
  - 光球大小：700-800px

**色彩搭配建议**：
- 科技感：深蓝 (#1e40af) + 紫色 (#7c3aed) + 青色 (#06b6d4)
- 温暖感：橙色 (#ea580c) + 粉色 (#db2777) + 黄色 (#eab308)
- 神秘感：深紫 (#581c87) + 深粉 (#831843) + 深蓝 (#1e3a8a)
- 自然感：深绿 (#15803d) + 青色 (#0e7490) + 黄绿 (#65a30d)
- 单色调：使用同一色相的不同明度（如 3 种深度的蓝色）

**典型应用场景**：
- 产品着陆页：营造高端科技感，突出产品特性
- 创意工作室：展示创意和设计能力，吸引客户
- SaaS 平台：创造现代、专业的品牌形象
- 音乐/娱乐：配合内容主题的氛围光（如专辑封面色）
- 冥想/健康：使用柔和色彩创造放松氛围
- 暗色主题应用：提供舒适的夜间浏览体验


---

## English Version (en-US)

Design ambient lighting interfaces that create immersive visual experiences through soft gradient light orbs and environmental glow.

**Core Visual Characteristics**:
- Large light orbs: Use radial gradients to create 400-800px soft light spheres
- Blur diffusion: filter: blur(80-150px) creates halo effects
- Multi-layer overlay: 3-5 light orbs of different colors and sizes stacked using mix-blend-mode
- Slow flow: Light orb positions animate slowly, creating breathing effect (15-30 second loops)
- Low contrast: Overall soft colors, avoid harsh high saturation
- Clear foreground: Content cards separated from background lights for readability

**Color System**:
- Background base:
  - Dark theme: #050505, #0a0a1a, #0d0d1d (pure black or deep blue-black)
  - Warm theme: #1a1612, #1a1410 (deep brown)
- Light orb colors:
  - Cool tones: Deep blue (#1e3a8a), purple (#5b21b6), cyan (#0e7490)
  - Warm tones: Orange (#c2410c), pink (#be185d), yellow (#ca8a04)
  - Neutral tones: Gray-blue (#334155), gray-purple (#4c1d95)
- Foreground cards:
  - Semi-transparent background: rgba(255,255,255,0.05) or rgba(0,0,0,0.3)
  - Blur glass: backdrop-filter: blur(10px)
  - Border glow: border: 1px solid rgba(255,255,255,0.1)
- Text colors:
  - Headings: #f5f5f5 or #e0e0e0 (soft white)
  - Body: #d0d0d0 or #b0b0b0 (reduced contrast)
  - Emphasis: Brand colors echoing the light orbs

**Light Orb Technical Implementation**:
- Radial gradient orbs:
  ```css
  background: radial-gradient(
    circle at center,
    rgba(147, 51, 234, 0.3) 0%,
    rgba(79, 70, 229, 0.2) 30%,
    transparent 70%
  );
  ```
- Multi-layer stacking:
  ```css
  .light-orb-1 { mix-blend-mode: screen; }
  .light-orb-2 { mix-blend-mode: color-dodge; }
  .light-orb-3 { mix-blend-mode: lighten; }
  ```
- Blur diffusion: filter: blur(100px) saturate(1.5)
- Absolute positioning: position: absolute, z-index: -1 in background layer

**Layout & Components**:
- Hero section: Large centered title with 2-3 large orbs moving slowly in background
- Feature cards:
  - Semi-transparent glass cards floating above orbs
  - Use backdrop-filter: blur(10px) to blur background
  - Card content high contrast for readability
- Grid layout: 2-3 column cards with staggered arrangement for depth
- Statistics: Large numbers + small labels with subtle glow backgrounds
- CTA buttons: Soft gradient backgrounds, increase glow intensity on hover
- Navigation bar: Top fixed with semi-transparent background + blur effect

**Animation & Interaction**:
- Orb floating animation:
  ```css
  @keyframes float {
    0%, 100% { transform: translate(0, 0); }
    50% { transform: translate(100px, -80px); }
  }
  animation: float 25s ease-in-out infinite;
  ```
- Breathing effect: Orb size slowly scales (scale 0.9 ↔ 1.1)
- Hue rotation: Use filter: hue-rotate() for slowly changing orb colors
- Mouse parallax: Orbs follow mouse with slight movement (transform: translate)
- Card hover: Increase backdrop-filter intensity on hover, enhance shadow
- Fade-in effect: Orbs fade from transparent on page load (opacity 0 → 1, 2-3 seconds)

**Glow Layering System**:
- Background layer (z-index: -2): Largest, most blurred orbs as ambient light
- Middle layer (z-index: -1): Medium-sized orbs providing main colors
- Foreground layer (z-index: 0): Content cards and text
- Decoration layer (z-index: 1): Small light points or star decorations

**Readability Safeguards**:
- Content area backgrounds: Add dark semi-transparent overlay (rgba(0,0,0,0.4))
- Text area separation: Keep important text away from brightest orb centers
- High contrast text: Headings use #fff, body at least #d0d0d0
- Text shadows: text-shadow: 0 2px 12px rgba(0,0,0,0.8) enhances legibility
- Blur glass cards: Use backdrop-filter to soften background light without affecting card text

**Orb Configuration Suggestions**:
- Main orb: 600-800px, positioned top-left or top-right, theme color
- Support orb 1: 400-600px, opposite diagonal position, complementary color
- Support orb 2: 300-500px, lower-middle page position, neutral color
- Limit orb count: Maximum 3-4 orbs to avoid visual clutter
- Orb positioning: At least 30-40% outside viewport to create infinite extension

**Performance Optimization**:
- Use CSS gradients instead of images: Reduce resource loading
- will-change: transform, filter hints browser optimization
- Reduce blur radius: Mobile uses blur(60px) instead of blur(120px)
- Reduce animation complexity: Mobile reduces orb count (3 → 2)
- Use transform instead of top/left: Avoid triggering layout reflow
- Lazy loading: Enable animations only for orbs in viewport

**Responsive Strategy**:
- Mobile (< 768px):
  - Orb count: 3 → 2
  - Blur radius: 120px → 60px
  - Orb size: 600px → 400px
  - Disable mouse parallax
  - Simplify animations (position only, no size changes)
- Tablet (768px - 1024px):
  - Retain main orb effects
  - Slightly simplified animations
  - Orb size: 600-700px
- Desktop (> 1024px):
  - Full orb effects
  - Complex animations + mouse interactions
  - Orb size: 700-800px

**Color Pairing Suggestions**:
- Tech feel: Deep blue (#1e40af) + purple (#7c3aed) + cyan (#06b6d4)
- Warm feel: Orange (#ea580c) + pink (#db2777) + yellow (#eab308)
- Mysterious: Deep purple (#581c87) + deep pink (#831843) + deep blue (#1e3a8a)
- Natural: Deep green (#15803d) + cyan (#0e7490) + yellow-green (#65a30d)
- Monochromatic: Use different luminosities of same hue (e.g., 3 shades of blue)

**Typical Use Cases**:
- Product landing pages: Create premium tech feel, highlight product features
- Creative studios: Showcase creativity and design capabilities, attract clients
- SaaS platforms: Create modern, professional brand image
- Music/entertainment: Ambient lighting matching content themes (album cover colors)
- Meditation/wellness: Use soft colors to create relaxing atmosphere
- Dark theme apps: Provide comfortable nighttime browsing experience
