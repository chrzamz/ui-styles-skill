# Custom Prompt

## 中文版本 (zh-CN)

你现在是一位精通 Liminal Space（阈限空间）美学设计的资深 UI 设计师兼前端工程师。请为我创建一个充满空旷感、诡异宁静与似曾相识感的网页，要求如下：

### 核心视觉特征
- **极简留白**：大面积留白，内容稀疏分布，营造空旷寂静的氛围
- **低饱和配色**：使用低饱和度的米黄（#f0ece2）、灰蓝（#d0d5dd）、淡绿（#e0e8d0）、灰紫（#d8d0e0），避免鲜艳色彩
- **柔和光线**：模拟荧光灯或柔和日光的效果，使用 linear-gradient 制造光带或雾感
- **空间透视**：使用透视（perspective）与变换（transform）营造深度感与空间感

### 阈限空间元素
- **走廊与过渡空间**：使用线性透视创建走廊、楼梯、长廊等过渡空间视觉
- **空无一人**：画面中没有人物，仅有空荡的场景与结构
- **荧光灯光带**：使用渐变色块模拟荧光灯光带（linear-gradient，黄白色 + box-shadow）
- **几何线条**：简洁的几何线条与边框，避免过多装饰

### 视觉氛围营造
- **雾气与模糊**：部分区域使用 filter: blur(2-5px) 或半透明白色遮罩，营造雾气感
- **低对比度**：文字与背景对比度适中（不过高也不过低），维持在 4.5:1 至 7:1 之间
- **渐变光线**：背景使用垂直或水平渐变，模拟光线从一侧照入的效果
- **阴影柔和**：所有阴影使用大范围模糊、低透明度，避免锐利边缘

### 页面结构
1. **Hero 区域**：简洁大标题，周围大量留白，背景可有柔和光带或雾感渐变
2. **叙事段落**：2-3 个简短的文字段落，间距宽松，字号适中，行高 1.8-2.0
3. **展示卡片**：1-3 个极简卡片，边框细线，内部留白充足，背景半透明或纯色
4. **CTA 按钮**：低调的按钮设计，边框细线，hover 时轻微变色，无强烈动画

### 动画与交互
- **缓慢淡入**：页面元素缓慢淡入（animation: fadeIn 2-3s ease-out），营造时间停滞感
- **微动画**：元素 hover 时仅有轻微的 transform: translateY(-2px)，无剧烈动作
- **无跳跃**：避免突兀的动画或闪烁，所有过渡使用 1-2s 的缓慢 transition
- **静默感**：动画节奏极慢，营造静止、诡异的氛围

### 配色方案
- **主色调**：米黄白（#f5f1e8, #faf8f3），灰蓝（#d5dce0, #e0e5ea），淡绿（#e8f0e0）
- **辅助色**：浅灰（#c0c5ca），淡紫灰（#d5d0dd），象牙白（#fffef8）
- **文字色**：深灰（#3a3d40, #4a4d50），避免纯黑，确保柔和感
- **强调色**：极少使用，仅在 CTA 按钮处使用低饱和度的青灰（#8a9da8）或淡蓝（#a0b5c0）

### 光线效果实现
- **荧光灯光带**：使用 linear-gradient(90deg, rgba(255,255,240,0) 0%, rgba(255,255,240,0.8) 50%, rgba(255,255,240,0) 100%) 创建水平光带
- **天花板光源**：在页面顶部添加半透明白色渐变条，模拟顶部光源（linear-gradient(180deg, rgba(255,255,255,0.3) 0%, transparent 20%)）
- **雾气层**：使用 ::before 伪元素叠加 rgba(255,255,255,0.1-0.2) 半透明层，营造雾感

### 空间透视技巧
- **透视走廊**：使用 perspective: 1000px 与 rotateY/rotateX 创建走廊或长廊的透视效果
- **渐小元素**：远处元素使用较小尺寸与较低透明度，营造距离感
- **网格地板**（可选）：使用 repeating-linear-gradient 创建渐隐的网格地板效果

### 文字排版
- **字体选择**：使用无衬线字体（如 Inter, Helvetica），字重适中（400-500），避免粗体
- **行高**：1.8-2.0，营造舒适的阅读节奏与空间感
- **字号**：标题 32-48px，正文 16-18px，不宜过大
- **间距**：段落间距 32-48px，营造留白与隔离感

### 性能优化
- **简化元素**：保持页面元素数量少，避免过多 DOM 节点
- **静态渐变**：大部分效果使用静态 CSS 渐变，减少动画计算
- **GPU 加速**：透视与变换使用 transform3d 启用硬件加速

### 技术要点
- 使用 CSS 变量定义配色（--liminal-bg, --liminal-text, --liminal-light）
- 使用 filter: blur() 与 opacity 营造雾感与距离感
- 使用 @media (prefers-reduced-motion) 为敏感用户提供无动画版本
- 可选：使用 Canvas 绘制动态雾气或光线效果

### 情感与氛围
- **似曾相识**：场景似曾相识但又陌生，营造 déjà vu 感
- **寂静与空旷**：大量留白，稀疏内容，营造无人的寂静感
- **诡异宁静**：柔和但略显诡异的光线与配色，营造不安的宁静
- **时间停滞**：缓慢的动画与淡入效果，营造时间静止的感觉

### 输出要求
请生成完整的 HTML 结构与内联样式，确保：
- 代码清晰注释，说明阈限空间美学的实现手法
- 配色与光线效果使用 CSS 变量，便于调整
- 动画缓慢柔和，无突兀的跳跃或闪烁
- 页面传达出空旷、寂静、诡异的阈限空间氛围


---

## English Version (en-US)

You are a senior UI designer and frontend engineer specializing in Liminal Space aesthetics. Create a webpage filled with spaciousness, eerie quietness, and déjà vu sensations with the following requirements:

### Core Visual Characteristics
- **Extreme Whitespace**: Large areas of whitespace with sparse content distribution creating empty, silent atmosphere
- **Low-Saturation Palette**: Use low-saturation beige (#f0ece2), gray-blue (#d0d5dd), pale green (#e0e8d0), gray-purple (#d8d0e0), avoid vibrant colors
- **Soft Lighting**: Simulate fluorescent or soft daylight effects using linear-gradient to create light bars or fog feel
- **Spatial Perspective**: Use perspective and transform to create depth and spatial sense

### Liminal Space Elements
- **Corridors & Transitional Spaces**: Use linear perspective to create corridors, stairways, hallways and other transitional space visuals
- **Absence of People**: No human figures in scenes, only empty structures and spaces
- **Fluorescent Light Bars**: Use gradient blocks to simulate fluorescent light bars (linear-gradient with yellowish-white + box-shadow)
- **Geometric Lines**: Clean geometric lines and borders, avoid excessive decoration

### Visual Atmosphere Creation
- **Fog & Blur**: Some areas use filter: blur(2-5px) or semi-transparent white overlay to create fog feel
- **Low Contrast**: Text-to-background contrast moderate (not too high or low), maintain between 4.5:1 and 7:1
- **Gradient Lighting**: Background uses vertical or horizontal gradients simulating light entering from one side
- **Soft Shadows**: All shadows use wide blur range and low opacity, avoid sharp edges

### Page Structure
1. **Hero Section**: Simple large headline with abundant surrounding whitespace, background may have soft light bars or fog-feel gradients
2. **Narrative Paragraphs**: 2-3 short text paragraphs with loose spacing, moderate font size, line-height 1.8-2.0
3. **Display Cards**: 1-3 minimalist cards with thin borders, ample internal whitespace, semi-transparent or solid backgrounds
4. **CTA Buttons**: Understated button design with thin borders, subtle color change on hover, no strong animations

### Animation & Interaction
- **Slow Fade-In**: Page elements slowly fade in (animation: fadeIn 2-3s ease-out) creating time-freeze sensation
- **Micro-Animations**: Elements only have slight transform: translateY(-2px) on hover, no dramatic actions
- **No Jumping**: Avoid abrupt animations or flashing, all transitions use 1-2s slow transition
- **Silent Feel**: Animation rhythm extremely slow, creating still, eerie atmosphere

### Color Scheme
- **Primary Tones**: Beige-white (#f5f1e8, #faf8f3), gray-blue (#d5dce0, #e0e5ea), pale green (#e8f0e0)
- **Secondary Colors**: Light gray (#c0c5ca), pale purple-gray (#d5d0dd), ivory (#fffef8)
- **Text Colors**: Dark gray (#3a3d40, #4a4d50), avoid pure black for softer feel
- **Accent Colors**: Rarely used, only on CTA buttons using low-saturation cyan-gray (#8a9da8) or pale blue (#a0b5c0)

### Lighting Effect Implementation
- **Fluorescent Light Bars**: Use linear-gradient(90deg, rgba(255,255,240,0) 0%, rgba(255,255,240,0.8) 50%, rgba(255,255,240,0) 100%) to create horizontal light bars
- **Ceiling Light Source**: Add semi-transparent white gradient strip at page top simulating overhead lighting (linear-gradient(180deg, rgba(255,255,255,0.3) 0%, transparent 20%))
- **Fog Layer**: Use ::before pseudo-element to overlay rgba(255,255,255,0.1-0.2) semi-transparent layer for fog feel

### Spatial Perspective Techniques
- **Perspective Corridor**: Use perspective: 1000px with rotateY/rotateX to create corridor or hallway perspective effects
- **Diminishing Elements**: Distant elements use smaller sizes and lower opacity creating distance sensation
- **Grid Floor** (optional): Use repeating-linear-gradient to create fading grid floor effect

### Typography
- **Font Choice**: Use sans-serif fonts (like Inter, Helvetica), moderate weight (400-500), avoid bold
- **Line Height**: 1.8-2.0 creating comfortable reading rhythm and spaciousness
- **Font Size**: Headlines 32-48px, body 16-18px, not too large
- **Spacing**: Paragraph spacing 32-48px creating whitespace and isolation feel

### Performance Optimization
- **Simplified Elements**: Keep page element count low, avoid excessive DOM nodes
- **Static Gradients**: Most effects use static CSS gradients reducing animation computation
- **GPU Acceleration**: Perspective and transforms use transform3d for hardware acceleration

### Technical Points
- Use CSS variables to define color scheme (--liminal-bg, --liminal-text, --liminal-light)
- Use filter: blur() and opacity to create fog and distance sensation
- Use @media (prefers-reduced-motion) to provide animation-free version for sensitive users
- Optional: Use Canvas to draw dynamic fog or lighting effects

### Emotion & Atmosphere
- **Déjà Vu**: Scenes feel familiar yet strange creating déjà vu sensation
- **Silence & Emptiness**: Abundant whitespace, sparse content creating unpopulated silence
- **Eerie Quietness**: Soft but slightly eerie lighting and colors creating unsettling calm
- **Time Freeze**: Slow animations and fade-ins creating time-stopped feeling

### Output Requirements
Generate complete HTML structure with inline styles ensuring:
- Clear code comments explaining liminal space aesthetic implementation techniques
- Color schemes and lighting effects use CSS variables for adjustment
- Animations slow and gentle without abrupt jumps or flashing
- Page conveys empty, silent, eerie liminal space atmosphere
