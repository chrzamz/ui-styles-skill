# Custom Prompt

## 中文版本 (zh-CN)

你现在是一位精通柔和发光效果设计的资深 UI 设计师兼前端工程师。请为我创建一个充满温柔光芒与辐射感的网页，要求如下：

### 核心视觉特征
- **深色或半深色底**：使用深蓝灰（#0f1419, #1a1f2e）或深紫灰（#1c1a2e）作为背景，营造夜晚或黄昏氛围
- **发光配色**：柔和的蓝白光（#a0c4ff, #bfd7ff），暖金光（#ffd89b, #ffe5b4），淡紫光（#d4b5ff），薄荷绿光（#b4ffdb）
- **光芒辐射**：所有元素散发柔和光晕，而非锐利边界，使用多层 box-shadow 与 blur 实现
- **发光层次**：近距离元素发光更强，远处元素光芒更柔和，营造景深感

### 发光效果实现
- **文字发光**：标题使用 text-shadow: 0 0 20px rgba(255,255,255,0.8), 0 0 40px rgba(160,196,255,0.5)，制造柔和光晕
- **卡片发光**：卡片边缘使用 box-shadow: 0 0 15px 5px rgba(180,215,255,0.3), 0 0 30px 10px rgba(180,215,255,0.15)
- **按钮发光**：按钮使用 4-5 层 box-shadow，从内到外逐渐扩散，hover 时光芒范围扩大 2 倍
- **背景光斑**：页面背景添加 3-5 个大型半透明圆形光斑，使用 radial-gradient 与 filter: blur(80px)

### 发光颜色策略
- **主色光芒**：品牌主色（如蓝色）的发光使用同色系但透明度渐变（50% → 20% → 5%）
- **多色光斑**：背景光斑可使用不同颜色（蓝、紫、金），相互交叠产生柔和渐变效果
- **白光基底**：所有彩色光芒底层添加一层白光（rgba(255,255,255,0.1-0.3)），增强发光真实感

### 背景氛围层
- **漂浮光斑**：使用 position: absolute 创建 5-8 个不同大小的圆形光斑，缓慢移动（animation: floatGlow 20s infinite）
- **柔光渐变**：页面底色使用 linear-gradient 从深色过渡到略浅的色调，配合光斑营造光源感
- **微光粒子**（可选）：添加小型点状光粒子，使用 opacity 动画模拟闪烁（animation: twinkle 3s infinite）

### 页面结构
1. **Hero 区域**：大标题带强烈文字发光，副标题光芒较弱，背景有 2-3 个大型光斑
2. **特性卡片**：3-4 个半透明卡片，边缘柔和发光，内部内容清晰可读
3. **按钮组件**：主按钮实心发光（box-shadow 5 层），次要按钮仅边缘微光
4. **装饰光带**：页面边缘或分隔处添加柔和发光的线条或带状装饰

### 颜色对比与可读性
- **文字对比**：主要文字使用高亮浅色（#e8f0ff, #f0f4ff），确保与深色背景对比度 ≥ 7:1
- **发光不遮挡**：控制发光扩散范围（blur ≤ 30px），避免光芒过大影响文字阅读
- **层次分明**：前景元素发光更清晰，背景光斑高度模糊（blur 60-100px），拉开视觉层次

### 动画与交互
- **缓慢呼吸**：关键元素添加 animation: glowPulse 4s infinite，box-shadow 扩散范围与透明度循环变化
- **光芒跟随**：按钮 hover 时光芒向鼠标方向扩散，使用 transform: scale(1.1) + box-shadow 增强
- **淡入淡出**：页面加载时各元素依次淡入并"点亮"发光效果（animation: fadeInGlow 1s ease-out）

### 性能优化
- **模糊优化**：背景大型光斑使用 CSS filter: blur()，数量控制在 5 个以内
- **合并阴影**：单个元素的 box-shadow 层数不超过 5 层，避免过多计算
- **GPU 加速**：发光元素使用 transform: translateZ(0) 启用硬件加速
- **动画节制**：同时运行的发光动画不超过 10 个，其余使用 animation-delay 错开

### 技术要点
- 使用 CSS 变量定义发光配色（--glow-primary, --glow-secondary）与模糊参数（--glow-blur-sm, --glow-blur-lg）
- 使用 @keyframes 定义 glowPulse, floatGlow, fadeInGlow 等动画
- 考虑添加 @media (prefers-reduced-motion) 为用户提供静态发光版本
- 可选：使用 Canvas 绘制动态光粒子效果，提升视觉丰富度

### 输出要求
请生成完整的 HTML 结构与内联样式，确保：
- 代码清晰注释，标注发光效果的参数含义
- 所有发光色与模糊值使用 CSS 变量，便于全局调整
- 包含至少 4 种发光效果示例：文字发光、卡片发光、按钮发光、背景光斑
- 动画柔和自然，无突兀的闪烁或跳动


---

## English Version (en-US)

You are a senior UI designer and frontend engineer specializing in soft glow effects. Create a webpage filled with gentle luminescence and radiance with the following requirements:

### Core Visual Characteristics
- **Dark or Semi-Dark Base**: Use deep blue-gray (#0f1419, #1a1f2e) or deep purple-gray (#1c1a2e) backgrounds to create night or twilight atmosphere
- **Glow Palette**: Soft blue-white glow (#a0c4ff, #bfd7ff), warm gold glow (#ffd89b, #ffe5b4), light purple glow (#d4b5ff), mint green glow (#b4ffdb)
- **Light Emanation**: All elements emit soft halos rather than sharp edges, achieved through multi-layer box-shadow and blur
- **Glow Hierarchy**: Closer elements glow stronger, distant elements have softer glows, creating depth perception

### Glow Effect Implementation
- **Text Glow**: Headlines use text-shadow: 0 0 20px rgba(255,255,255,0.8), 0 0 40px rgba(160,196,255,0.5) for soft halos
- **Card Glow**: Card edges use box-shadow: 0 0 15px 5px rgba(180,215,255,0.3), 0 0 30px 10px rgba(180,215,255,0.15)
- **Button Glow**: Buttons use 4-5 box-shadow layers gradually diffusing outward, hover doubles glow range
- **Background Light Spots**: Page background adds 3-5 large semi-transparent circular light spots using radial-gradient with filter: blur(80px)

### Glow Color Strategy
- **Primary Color Glow**: Brand color (e.g., blue) glow uses same hue with opacity gradients (50% → 20% → 5%)
- **Multi-Color Spots**: Background light spots can use different colors (blue, purple, gold) overlapping for soft gradient effects
- **White Light Base**: All colored glows add underlying white light layer (rgba(255,255,255,0.1-0.3)) for realistic luminescence

### Background Atmosphere Layers
- **Floating Light Spots**: Use position: absolute to create 5-8 circular light spots of varying sizes, slowly moving (animation: floatGlow 20s infinite)
- **Soft Light Gradient**: Page base uses linear-gradient transitioning from dark to slightly lighter tones, coordinating with spots for light source feel
- **Micro Light Particles** (optional): Add small dot-shaped light particles using opacity animation to simulate twinkling (animation: twinkle 3s infinite)

### Page Structure
1. **Hero Section**: Large headline with strong text glow, subtitle with weaker glow, background has 2-3 large light spots
2. **Feature Cards**: 3-4 semi-transparent cards with soft edge glow, internal content clearly readable
3. **Button Components**: Primary buttons with solid glow (5-layer box-shadow), secondary buttons with edge micro-glow only
4. **Decorative Light Bands**: Add softly glowing lines or band decorations at page edges or separators

### Color Contrast & Readability
- **Text Contrast**: Primary text uses bright light colors (#e8f0ff, #f0f4ff) ensuring contrast ratio ≥ 7:1 with dark background
- **Glow Non-Obstruction**: Control glow diffusion range (blur ≤ 30px) to prevent excessive light from affecting text reading
- **Clear Hierarchy**: Foreground elements have clearer glow, background spots highly blurred (blur 60-100px), separating visual layers

### Animation & Interaction
- **Slow Breathing**: Key elements add animation: glowPulse 4s infinite, box-shadow diffusion range and opacity cycle
- **Glow Following**: Button hover makes glow expand toward mouse direction using transform: scale(1.1) + box-shadow enhancement
- **Fade In Out**: Page load makes elements sequentially fade in and "light up" glow effect (animation: fadeInGlow 1s ease-out)

### Performance Optimization
- **Blur Optimization**: Background large light spots use CSS filter: blur(), quantity controlled under 5
- **Shadow Consolidation**: Single element box-shadow layers don't exceed 5 to avoid excessive computation
- **GPU Acceleration**: Glowing elements use transform: translateZ(0) to enable hardware acceleration
- **Animation Restraint**: Simultaneously running glow animations don't exceed 10, others staggered with animation-delay

### Technical Points
- Use CSS variables to define glow palette (--glow-primary, --glow-secondary) and blur parameters (--glow-blur-sm, --glow-blur-lg)
- Define glowPulse, floatGlow, fadeInGlow animations with @keyframes
- Consider adding @media (prefers-reduced-motion) to provide static glow version for users
- Optional: Use Canvas to draw dynamic light particle effects for enhanced visual richness

### Output Requirements
Generate complete HTML structure with inline styles ensuring:
- Clear code comments marking glow effect parameter meanings
- All glow colors and blur values using CSS variables for global adjustment
- Include at least 4 glow effect examples: text glow, card glow, button glow, background light spots
- Smooth and natural animations without abrupt flashing or jumping
