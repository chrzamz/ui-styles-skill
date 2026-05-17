# Custom Prompt

## 中文版本 (zh-CN)

你现在是一位精通有机形状与自然流动设计的资深 UI 设计师兼前端工程师。请为我创建一个以柔和有机形状为核心视觉元素的网页，要求如下：

### 核心视觉特征
- **流动的有机形状**：使用 blob、不规则曲线、生物形态的形状作为装饰元素
- **自然配色**：柔和的绿色（#a8d5ba, #c8e6c9）、米黄（#f5e6d3）、浅蓝（#b3d9ff）、淡紫（#d5c6e0），避免锐利的纯色
- **柔和边界**：所有元素使用大圆角（border-radius: 24-48px）或不规则形状，避免直角
- **漂浮感**：使用阴影与渐变营造元素漂浮在背景之上的感觉

### 有机形状实现
- **SVG Blob 形状**：使用 SVG path 创建不规则有机形状，或使用 border-radius: 30% 60% 70% 40% / 60% 30% 70% 40% 创建变形圆
- **形状动画**：使用 @keyframes 缓慢改变 border-radius 值，使形状产生呼吸或形变效果（10-20s 循环）
- **形状叠加**：多个半透明有机形状叠加，使用 opacity: 0.1-0.3 和 mix-blend-mode: multiply/screen
- **背景装饰**：页面四角或边缘放置大型有机形状作为装饰，使用低饱和度渐变填充

### 页面结构
1. **Hero 区域**：大标题，背景有 2-3 个大型有机形状缓慢漂移或形变
2. **特性卡片**：3-4 个卡片，边角极度圆润（border-radius: 32px），边缘可有有机形状装饰
3. **图文分栏**：一侧文字，一侧有机形状装饰或插图，形状与文字区域自然融合
4. **CTA 按钮**：大圆角按钮（border-radius: 48px），hover 时轻微形变或阴影增强

### 配色策略
- **主色调**：柔和绿（#a8d5ba, #b8e6c9），米黄（#f5ead3, #fff8e7），浅蓝（#c8e0f4）
- **辅助色**：淡紫（#d5c6e0），粉橙（#ffd5c8），浅灰（#e8e8e8）
- **渐变配色**：使用多色柔和渐变（如绿 → 黄 → 橙），过渡自然，避免突变
- **自然感**：配色灵感来自自然界（植物、水、天空），使用低饱和度色彩

### 动画与交互
- **形状呼吸**：有机形状使用 animation: blobMorph 15-20s infinite ease-in-out，border-radius 值缓慢变化
- **漂浮动画**：装饰形状使用 animation: float 10s infinite ease-in-out，轻微上下漂移
- **hover 形变**：卡片或按钮 hover 时边角圆润度增加，使用 transition: border-radius 0.5s ease
- **滚动视差**：滚动时有机形状以不同速度移动，增强层次感

### 阴影与深度
- **柔和阴影**：使用 box-shadow: 0 10px 40px rgba(0,0,0,0.08)，模糊范围大，透明度低
- **多层阴影**：卡片使用 2-3 层阴影叠加，营造漂浮感（如 0 5px 15px rgba(), 0 15px 35px rgba()）
- **内阴影**：部分元素使用 inset shadow 增强深度感

### 文字排版
- **字体选择**：使用圆润的无衬线字体（如 Poppins, Quicksand, Nunito），字重 400-600
- **行高**：1.7-1.8，营造舒适的阅读体验
- **文字颜色**：深灰（#2d3436, #636e72），避免纯黑，确保柔和感

### 技术要点
- 使用 CSS 变量定义有机配色（--organic-green, --organic-beige）和圆角（--organic-radius）
- 使用 @keyframes 定义 blobMorph, float 等动画
- 使用 clip-path 或 SVG 创建更复杂的有机形状
- 可选：使用 Canvas 或 WebGL 实现流体模拟效果

### 输出要求
请生成完整的 HTML 结构与内联样式，确保：
- 代码清晰注释，说明有机形状的实现方式
- 配色与形状参数使用 CSS 变量，便于调整
- 动画柔和自然，营造流动、舒适的视觉体验


---

## English Version (en-US)

You are a senior UI designer and frontend engineer specializing in organic shapes and natural flow design. Create a webpage with soft organic shapes as core visual elements with the following requirements:

### Core Visual Characteristics
- **Flowing Organic Shapes**: Use blobs, irregular curves, biomorphic shapes as decorative elements
- **Natural Palette**: Soft greens (#a8d5ba, #c8e6c9), beige (#f5e6d3), light blue (#b3d9ff), pale purple (#d5c6e0), avoid sharp pure colors
- **Soft Boundaries**: All elements use large border-radius (24-48px) or irregular shapes, avoid right angles
- **Floating Feel**: Use shadows and gradients to create elements floating above background

### Organic Shape Implementation
- **SVG Blob Shapes**: Use SVG path to create irregular organic shapes, or use border-radius: 30% 60% 70% 40% / 60% 30% 70% 40% for morphed circles
- **Shape Animation**: Use @keyframes to slowly change border-radius values making shapes breathe or morph (10-20s loop)
- **Shape Overlay**: Multiple semi-transparent organic shapes overlay using opacity: 0.1-0.3 and mix-blend-mode: multiply/screen
- **Background Decoration**: Place large organic shapes at page corners or edges as decoration using low-saturation gradient fills

### Page Structure
1. **Hero Section**: Large headline with 2-3 large organic shapes slowly drifting or morphing in background
2. **Feature Cards**: 3-4 cards with extremely rounded corners (border-radius: 32px), edges may have organic shape decorations
3. **Text-Image Split**: Text on one side, organic shape decoration or illustration on other, shapes naturally blend with text area
4. **CTA Buttons**: Large rounded buttons (border-radius: 48px), slight morph or shadow enhancement on hover

### Color Strategy
- **Primary Tones**: Soft green (#a8d5ba, #b8e6c9), beige (#f5ead3, #fff8e7), light blue (#c8e0f4)
- **Secondary Colors**: Pale purple (#d5c6e0), pink-orange (#ffd5c8), light gray (#e8e8e8)
- **Gradient Colors**: Use multi-color soft gradients (like green → yellow → orange) with natural transitions, avoid abrupt changes
- **Natural Feel**: Color inspiration from nature (plants, water, sky) using low-saturation colors

### Animation & Interaction
- **Shape Breathing**: Organic shapes use animation: blobMorph 15-20s infinite ease-in-out with slowly changing border-radius values
- **Floating Animation**: Decorative shapes use animation: float 10s infinite ease-in-out with slight up-down drift
- **Hover Morph**: Cards or buttons increase corner roundness on hover using transition: border-radius 0.5s ease
- **Scroll Parallax**: Organic shapes move at different speeds when scrolling enhancing layering

### Shadow & Depth
- **Soft Shadows**: Use box-shadow: 0 10px 40px rgba(0,0,0,0.08) with large blur range and low opacity
- **Multi-Layer Shadows**: Cards use 2-3 stacked shadows creating floating feel (like 0 5px 15px rgba(), 0 15px 35px rgba())
- **Inset Shadow**: Some elements use inset shadow to enhance depth sensation

### Typography
- **Font Choice**: Use rounded sans-serif fonts (like Poppins, Quicksand, Nunito) with weight 400-600
- **Line Height**: 1.7-1.8 creating comfortable reading experience
- **Text Colors**: Dark gray (#2d3436, #636e72), avoid pure black ensuring softness

### Technical Points
- Use CSS variables to define organic palette (--organic-green, --organic-beige) and border-radius (--organic-radius)
- Define blobMorph, float animations with @keyframes
- Use clip-path or SVG to create more complex organic shapes
- Optional: Use Canvas or WebGL for fluid simulation effects

### Output Requirements
Generate complete HTML structure with inline styles ensuring:
- Clear code comments explaining organic shape implementation
- Color and shape parameters use CSS variables for adjustment
- Animations soft and natural creating flowing, comfortable visual experience
