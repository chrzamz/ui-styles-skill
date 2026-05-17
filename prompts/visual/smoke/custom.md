# Custom Prompt

## 中文版本 (zh-CN)

请使用 TailwindCSS 创建一个充满神秘氛围的烟雾效果页面，通过飘渺的雾带、光斑和柔和的粒子营造沉浸式视觉体验。

**烟雾风格核心特征**：

**色彩与氛围**：
- 主背景色：深色调（#0F172A, #1E1B4B, #1F2937）营造暗场
- 烟雾颜色：半透明白烟（rgba(255, 255, 255, 0.05-0.15)）
- 冷色烟雾：淡蓝雾（rgba(147, 197, 253, 0.1)）、青绿雾（rgba(34, 211, 238, 0.08)）
- 暖色烟雾：淡紫雾（rgba(196, 181, 253, 0.1)）、玫瑰雾（rgba(251, 207, 232, 0.08)）
- 光斑点缀：柔和的白色/蓝色光晕（blur 效果）
- 文字高对比：使用纯白（#FFFFFF）或浅灰（#F3F4F6）确保可读性

**烟雾形态与纹理**：
- 飘带状烟雾：使用波浪曲线（`border-radius: 50%`）+ 高斯模糊（`filter: blur(40px-80px)`）
- 云朵状烟雾：多个圆形重叠（不同大小和透明度）形成聚合效果
- 条纹雾带：横向或斜向的半透明条带，使用渐变（`linear-gradient`）
- 粒子雾：小圆点（2-8px）随机散布，透明度 0.05-0.2
- 光束穿透：纵向的光柱效果，使用垂直渐变 + 高模糊
- 边缘扩散：烟雾边界使用渐变透明度（0% → 100%）实现自然消散

**运动与动画**：
- 缓慢飘移：使用 `@keyframes` 实现水平或垂直移动
  - 动画时长：20-40 秒（极慢速度）
  - 缓动函数：`ease-in-out`（平滑往复运动）
- 呼吸效果：烟雾的 `opacity` 和 `scale` 缓慢变化（0.8 ↔ 1.2）
- 旋转漂移：某些烟雾元素缓慢旋转（360 度 / 60 秒）
- 错位动画：多层烟雾以不同速度移动，营造景深感
- 光斑闪烁：光点的 `opacity` 0.3 ↔ 0.8 缓慢变化（5-10 秒周期）
- 视差滚动：滚动时烟雾层以不同速度移动

**层次与深度**：
- 前景烟雾：高透明度（0.02-0.08），大模糊半径（60-100px），快速移动
- 中景烟雾：中透明度（0.08-0.15），中模糊半径（40-60px），中速移动
- 背景烟雾：低透明度（0.15-0.25），小模糊半径（20-40px），慢速移动
- 光斑层：位于烟雾之上，透明度 0.1-0.3，大模糊（80-120px）
- 内容层：最高 z-index，确保文字和按钮清晰可见

**页面结构要求**：

1. **Hero 区域**：
   - 全屏高度（`h-screen`）深色背景
   - 标题：超大字号（text-6xl 或 text-7xl），纯白色，字重 700-900
   - 副标题：中等字号（text-xl），浅灰色（text-gray-300）
   - 3-5 层烟雾叠加：
     - 底层：大范围淡蓝雾带，横向飘动
     - 中层：2-3 个云朵状烟团，缓慢旋转
     - 顶层：细小粒子雾，快速飘移
   - CTA 按钮：半透明白色边框（`border-2 border-white/30`），悬停时边框变实
   - 光斑装饰：2-3 个柔和光晕，位于标题周围

2. **特性卡片区（3-4 个卡片）**：
   - 卡片背景：深色半透明（`bg-slate-800/40`）+ 模糊背景（`backdrop-blur-md`）
   - 卡片边框：1px 浅色边框（`border border-white/10`）
   - 卡片内烟雾：每张卡片底部或顶部添加淡雾装饰
   - 图标：线性图标，白色或淡蓝色
   - 标题：白色，字重 600
   - 描述：浅灰色（text-gray-400）
   - 悬停效果：卡片上升 + 边框亮度增强 + 内部雾气加深

3. **CTA 行动召唤区**：
   - 标题：大字号，纯白色
   - 背景：深色 + 横向雾带（从左至右缓慢移动）
   - 烟雾效果：2-3 条宽雾带（高度 100-200px），透明度 0.1，模糊 60px
   - 按钮：实心白色按钮 + 半透明烟雾包围效果
   - 光斑：按钮周围添加柔和光晕

4. **日志/列表区域**：
   - 列表容器：半透明深色背景（`bg-slate-900/60`）
   - 列表项：每项间隔添加细雾条（高度 1-2px，透明度 0.05）
   - 列表项悬停：背景微亮 + 左侧雾气显现
   - 滚动条：半透明样式，与整体烟雾风格一致
   - 背景装饰：垂直光束效果（从上至下渐变消失）

5. **页脚区域**：
   - 背景：深色渐变（从深灰到纯黑）
   - 顶部雾气：浓密的横向雾带，模糊 80px
   - 内容：两列或三列布局，文字浅灰色
   - 底部烟雾：细小粒子雾，缓慢上升动画

**关键 CSS 技术实现**：

1. **烟雾元素基础样式**：
```css
.smoke-layer {
  position: absolute;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
  filter: blur(60px);
  opacity: 0.8;
  animation: drift 30s ease-in-out infinite;
}

@keyframes drift {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(100px, -50px); }
}
```

2. **光斑效果**：
```css
.glow-orb {
  position: absolute;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(147,197,253,0.3) 0%, transparent 70%);
  filter: blur(100px);
  animation: pulse 8s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.3; transform: scale(1); }
  50% { opacity: 0.6; transform: scale(1.2); }
}
```

3. **粒子雾**：
```css
.fog-particle {
  position: absolute;
  width: 4px;
  height: 4px;
  background: rgba(255,255,255,0.15);
  border-radius: 50%;
  filter: blur(2px);
  animation: float 20s linear infinite;
}

@keyframes float {
  0% { transform: translateY(0) translateX(0); opacity: 0; }
  50% { opacity: 0.15; }
  100% { transform: translateY(-100vh) translateX(50px); opacity: 0; }
}
```

**响应式考虑**：
- 移动端：减少烟雾层数（2-3 层），降低模糊半径（30-50px）
- 移动端：禁用复杂动画或使用简化版（使用 `@media (prefers-reduced-motion)`）
- 移动端：减少粒子数量，避免性能问题
- 平板：中等烟雾密度，保持主要动画效果
- 桌面：完整烟雾效果，多层叠加 + 视差滚动

**性能优化**：
- 使用 `will-change: transform, opacity` 提示浏览器优化动画
- 烟雾元素使用 `transform` 和 `opacity` 动画（避免 `left`/`top`）
- 限制模糊元素数量（最多 8-10 个）
- 使用 CSS 变量动态控制烟雾透明度和速度
- 在低性能设备上禁用烟雾动画（使用 `matchMedia` 检测）

**可访问性**：
- 确保文字与烟雾背景对比度 ≥ 4.5:1（WCAG AA）
- 提供"减少动画"选项，遵循 `prefers-reduced-motion`
- 烟雾装饰使用 `aria-hidden="true"`，不干扰屏幕阅读器
- 所有交互元素（按钮、链接）有明确的焦点指示器

**配色方案示例**：
- 方案 1（冷色神秘）：背景 #0F172A + 白烟 rgba(255,255,255,0.1) + 蓝光 rgba(147,197,253,0.3)
- 方案 2（紫色梦幻）：背景 #1E1B4B + 紫烟 rgba(196,181,253,0.12) + 粉光 rgba(251,207,232,0.2)
- 方案 3（青绿科技）：背景 #134E4A + 青烟 rgba(34,211,238,0.1) + 绿光 rgba(74,222,128,0.25)


---

## English Version (en-US)

Create a mysterious smoke-effect page using TailwindCSS, establishing an immersive visual experience through ethereal mist bands, light orbs, and soft particles.

**Smoke Style Core Characteristics**:

**Colors & Atmosphere**:
- Main background: Dark tones (#0F172A, #1E1B4B, #1F2937) for dark stage
- Smoke colors: Semi-transparent white smoke (rgba(255, 255, 255, 0.05-0.15))
- Cool smoke: Light blue mist (rgba(147, 197, 253, 0.1)), cyan mist (rgba(34, 211, 238, 0.08))
- Warm smoke: Light purple mist (rgba(196, 181, 253, 0.1)), rose mist (rgba(251, 207, 232, 0.08))
- Light orb accents: Soft white/blue glows (blur effects)
- High-contrast text: Pure white (#FFFFFF) or light gray (#F3F4F6) for readability

**Smoke Forms & Textures**:
- Ribbon smoke: Wavy curves (`border-radius: 50%`) + Gaussian blur (`filter: blur(40px-80px)`)
- Cloud smoke: Multiple overlapping circles (different sizes and opacities) forming aggregate effect
- Stripe mist bands: Horizontal or diagonal semi-transparent bands using gradients (`linear-gradient`)
- Particle fog: Small dots (2-8px) randomly scattered, opacity 0.05-0.2
- Beam penetration: Vertical light column effects using vertical gradients + high blur
- Edge diffusion: Smoke boundaries use gradient transparency (0% → 100%) for natural dissipation

**Movement & Animation**:
- Slow drift: Use `@keyframes` for horizontal or vertical movement
  - Animation duration: 20-40 seconds (extremely slow)
  - Easing function: `ease-in-out` (smooth reciprocal motion)
- Breathing effect: Smoke `opacity` and `scale` slowly change (0.8 ↔ 1.2)
- Rotation drift: Some smoke elements slowly rotate (360° / 60 seconds)
- Misaligned animation: Multiple smoke layers move at different speeds, creating depth
- Light orb flicker: Light dot `opacity` 0.3 ↔ 0.8 slowly changes (5-10 second cycle)
- Parallax scrolling: Smoke layers move at different speeds when scrolling

**Hierarchy & Depth**:
- Foreground smoke: High transparency (0.02-0.08), large blur radius (60-100px), fast movement
- Midground smoke: Medium transparency (0.08-0.15), medium blur radius (40-60px), medium speed
- Background smoke: Low transparency (0.15-0.25), small blur radius (20-40px), slow movement
- Light orb layer: Above smoke, opacity 0.1-0.3, large blur (80-120px)
- Content layer: Highest z-index, ensuring text and buttons are clearly visible

**Page Structure Requirements**:

1. **Hero Section**:
   - Full-screen height (`h-screen`) dark background
   - Title: Extra large font (text-6xl or text-7xl), pure white, weight 700-900
   - Subtitle: Medium font (text-xl), light gray (text-gray-300)
   - 3-5 smoke layers overlaid:
     - Bottom: Large light blue mist band, horizontal drift
     - Middle: 2-3 cloud-shaped smoke masses, slow rotation
     - Top: Fine particle fog, fast drift
   - CTA button: Semi-transparent white border (`border-2 border-white/30`), border solidifies on hover
   - Light orb decoration: 2-3 soft glows around title

2. **Feature Card Area (3-4 cards)**:
   - Card background: Dark semi-transparent (`bg-slate-800/40`) + blur background (`backdrop-blur-md`)
   - Card border: 1px light border (`border border-white/10`)
   - Card smoke: Add light mist decoration at bottom or top of each card
   - Icons: Linear icons, white or light blue
   - Title: White, weight 600
   - Description: Light gray (text-gray-400)
   - Hover effect: Card rises + border brightness increases + internal mist deepens

3. **CTA Call-to-Action Area**:
   - Title: Large font, pure white
   - Background: Dark + horizontal mist bands (slowly moving left to right)
   - Smoke effect: 2-3 wide mist bands (height 100-200px), opacity 0.1, blur 60px
   - Button: Solid white button + semi-transparent smoke surrounding effect
   - Light orbs: Soft glows around button

4. **Log/List Area**:
   - List container: Semi-transparent dark background (`bg-slate-900/60`)
   - List items: Add fine mist strips between items (height 1-2px, opacity 0.05)
   - List item hover: Background slightly brighter + left mist appears
   - Scrollbar: Semi-transparent style, consistent with overall smoke aesthetic
   - Background decoration: Vertical beam effect (gradient fade from top to bottom)

5. **Footer Area**:
   - Background: Dark gradient (from deep gray to pure black)
   - Top mist: Dense horizontal mist band, blur 80px
   - Content: Two or three-column layout, text light gray
   - Bottom smoke: Fine particle fog, slow upward animation

**Key CSS Implementation Techniques**:

1. **Smoke Element Base Styles**:
```css
.smoke-layer {
  position: absolute;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
  filter: blur(60px);
  opacity: 0.8;
  animation: drift 30s ease-in-out infinite;
}

@keyframes drift {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(100px, -50px); }
}
```

2. **Light Orb Effect**:
```css
.glow-orb {
  position: absolute;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(147,197,253,0.3) 0%, transparent 70%);
  filter: blur(100px);
  animation: pulse 8s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.3; transform: scale(1); }
  50% { opacity: 0.6; transform: scale(1.2); }
}
```

3. **Particle Fog**:
```css
.fog-particle {
  position: absolute;
  width: 4px;
  height: 4px;
  background: rgba(255,255,255,0.15);
  border-radius: 50%;
  filter: blur(2px);
  animation: float 20s linear infinite;
}

@keyframes float {
  0% { transform: translateY(0) translateX(0); opacity: 0; }
  50% { opacity: 0.15; }
  100% { transform: translateY(-100vh) translateX(50px); opacity: 0; }
}
```

**Responsive Considerations**:
- Mobile: Reduce smoke layer count (2-3 layers), lower blur radius (30-50px)
- Mobile: Disable complex animations or use simplified versions (use `@media (prefers-reduced-motion)`)
- Mobile: Reduce particle count to avoid performance issues
- Tablet: Medium smoke density, maintain main animation effects
- Desktop: Full smoke effects, multi-layer overlay + parallax scrolling

**Performance Optimization**:
- Use `will-change: transform, opacity` to hint browser for animation optimization
- Smoke elements use `transform` and `opacity` animations (avoid `left`/`top`)
- Limit blurred element count (maximum 8-10 elements)
- Use CSS variables to dynamically control smoke opacity and speed
- Disable smoke animations on low-performance devices (use `matchMedia` detection)

**Accessibility**:
- Ensure text-to-smoke background contrast ratio ≥ 4.5:1 (WCAG AA)
- Provide "reduce animation" option, respect `prefers-reduced-motion`
- Smoke decorations use `aria-hidden="true"`, don't interfere with screen readers
- All interactive elements (buttons, links) have clear focus indicators

**Color Scheme Examples**:
- Scheme 1 (Cool Mystery): Background #0F172A + white smoke rgba(255,255,255,0.1) + blue light rgba(147,197,253,0.3)
- Scheme 2 (Purple Dream): Background #1E1B4B + purple smoke rgba(196,181,253,0.12) + pink light rgba(251,207,232,0.2)
- Scheme 3 (Cyan Tech): Background #134E4A + cyan smoke rgba(34,211,238,0.1) + green light rgba(74,222,128,0.25)
