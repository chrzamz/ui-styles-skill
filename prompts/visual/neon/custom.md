# Custom Prompt

## 中文版本 (zh-CN)

你现在是一位精通霓虹光效设计的资深 UI 设计师兼前端工程师。请为我创建一个充满霓虹夜景氛围的网页，要求如下：

### 核心视觉特征
- **深色底色**：使用极深的蓝黑色或纯黑背景（#000000, #0a0a0f, #050510），营造夜晚都市氛围
- **霓虹配色**：电光蓝（#00e5ff, #0ff），洋红/品红（#ff00ff, #f0f），荧光绿（#00ff41, #39ff14），霓虹紫（#bf00ff）
- **发光描边**：所有重要元素（标题、卡片、按钮）使用多层 text-shadow 或 box-shadow 模拟霓虹管发光效果
- **光晕扩散**：使用 filter: blur() 与半透明色层叠加，制造光线在雾气中散射的效果

### 发光效果实现
- **文字霓虹**：大标题使用 text-shadow: 0 0 10px, 0 0 20px, 0 0 30px 三层叠加，颜色由浓到淡
- **边框霓虹**：卡片与按钮使用 box-shadow: 0 0 5px, 0 0 10px, 0 0 20px, inset 0 0 10px 内外发光
- **动态闪烁**：关键元素添加 animation: neonFlicker 实现霓虹灯管偶尔闪烁效果（opacity 0.8-1）
- **悬停增强**：hover 状态下增强发光强度，blur 值增大 50%，阴影层数增加

### 背景氛围层
- **雨夜反光**（可选）：添加细微竖条纹动画模拟雨滴，使用 linear-gradient 与 animation: rainDrop
- **光栅网格**（可选）：使用 repeating-linear-gradient 创建赛博朋克风格的背景网格，颜色使用低透明度霓虹色
- **光束扫描**（可选）：添加从左至右或从上至下缓慢移动的半透明光束，使用 background: linear-gradient + animation: scan

### 页面结构
1. **Hero 区域**：超大霓虹标题（60-80px），副标题使用较弱的发光效果，背景可有扫描光束
2. **特性卡片**：3-4 个玻璃态卡片，边框霓虹发光，内部内容使用浅色文字（#e0e0ff）
3. **按钮组件**：主按钮使用实心霓虹色 + 强发光，次要按钮仅边框发光
4. **装饰元素**：页面四角或侧边添加霓虹线条装饰，使用 border 或 SVG 绘制

### 颜色对比与可读性
- **文字颜色**：主要文字使用浅蓝白色（#e0e8ff, #c0d0ff），确保在深色底上清晰可读
- **对比度控制**：确保正文文字与背景对比度达到 WCAG AA 标准（至少 4.5:1）
- **发光不过度**：控制发光范围，避免过度模糊影响文字辨识度

### 动画与交互
- **缓慢脉冲**：标题文字或主 CTA 按钮添加 animation: neonPulse 2s infinite，opacity 与 shadow 微幅变化
- **闪烁效果**：10% 概率触发的快速闪烁（200ms），模拟霓虹灯管不稳定
- **悬停发光**：所有可交互元素 hover 时发光强度提升 1.5-2 倍，transition: all 0.3s ease

### 性能优化
- **减少模糊层**：每个元素的 box-shadow 层数控制在 3-5 层，避免过多影响渲染性能
- **GPU 加速**：使用 transform: translateZ(0) 或 will-change: transform 开启硬件加速
- **动画节制**：避免同时运行超过 8 个动画元素，使用 animation-delay 错开时间

### 技术要点
- 使用 CSS 自定义属性（--neon-blue, --neon-pink）管理霓虹配色
- 使用 @keyframes 定义 neonPulse, neonFlicker, neonScan 等动画
- 考虑添加 prefers-reduced-motion 媒体查询，为不适应闪烁的用户禁用动画
- 可选：使用 Canvas 或 WebGL 实现更复杂的霓虹灯管效果

### 输出要求
请生成完整的 HTML 结构与内联样式，确保：
- 代码结构清晰，注释说明关键发光效果
- 所有霓虹色使用 CSS 变量定义，便于调整
- 包含至少 3 种不同的霓虹发光效果示例（文字、边框、背景）
- 动画流畅自然，不产生刺眼的闪烁


---

## English Version (en-US)

You are a senior UI designer and frontend engineer specializing in neon light effects. Create a neon night-themed webpage with the following requirements:

### Core Visual Characteristics
- **Dark Base**: Use deep blue-black or pure black backgrounds (#000000, #0a0a0f, #050510) to create a night cityscape atmosphere
- **Neon Palette**: Electric blue (#00e5ff, #0ff), magenta/fuchsia (#ff00ff, #f0f), fluorescent green (#00ff41, #39ff14), neon purple (#bf00ff)
- **Glowing Outlines**: All key elements (titles, cards, buttons) use multi-layer text-shadow or box-shadow to simulate neon tube glow
- **Light Diffusion**: Use filter: blur() with semi-transparent color overlays to create light scattering through fog

### Glow Effect Implementation
- **Text Neon**: Large headlines use text-shadow: 0 0 10px, 0 0 20px, 0 0 30px with three stacked layers, colors fading from intense to light
- **Border Neon**: Cards and buttons use box-shadow: 0 0 5px, 0 0 10px, 0 0 20px, inset 0 0 10px for inner and outer glow
- **Dynamic Flicker**: Key elements add animation: neonFlicker to simulate occasional neon tube flickering (opacity 0.8-1)
- **Hover Enhancement**: Hover state increases glow intensity, blur values increase by 50%, shadow layers multiply

### Background Atmosphere Layers
- **Rain Reflection** (optional): Add subtle vertical stripe animation simulating rain drops using linear-gradient with animation: rainDrop
- **Grid Raster** (optional): Use repeating-linear-gradient to create cyberpunk-style background grid with low-opacity neon colors
- **Scanning Beams** (optional): Add slow-moving semi-transparent beams from left-to-right or top-to-bottom using background: linear-gradient + animation: scan

### Page Structure
1. **Hero Section**: Oversized neon headline (60-80px), subtitle with weaker glow effect, background may have scanning beams
2. **Feature Cards**: 3-4 glass-morphic cards with neon glowing borders, internal content uses light text (#e0e0ff)
3. **Button Components**: Primary buttons use solid neon colors + strong glow, secondary buttons with border glow only
4. **Decorative Elements**: Add neon line decorations at page corners or sides using border or SVG

### Color Contrast & Readability
- **Text Colors**: Primary text uses light blue-white (#e0e8ff, #c0d0ff) ensuring clear readability on dark backgrounds
- **Contrast Control**: Ensure body text-to-background contrast meets WCAG AA standards (at least 4.5:1)
- **Glow Moderation**: Control glow range to avoid excessive blur affecting text legibility

### Animation & Interaction
- **Slow Pulse**: Title text or main CTA buttons add animation: neonPulse 2s infinite with subtle opacity and shadow variations
- **Flicker Effect**: 10% probability triggered quick flicker (200ms) simulating unstable neon tubes
- **Hover Glow**: All interactive elements increase glow intensity 1.5-2x on hover with transition: all 0.3s ease

### Performance Optimization
- **Reduce Blur Layers**: Control box-shadow layers to 3-5 per element to avoid rendering performance impact
- **GPU Acceleration**: Use transform: translateZ(0) or will-change: transform to enable hardware acceleration
- **Animation Restraint**: Avoid running more than 8 animated elements simultaneously, use animation-delay to stagger timing

### Technical Points
- Use CSS custom properties (--neon-blue, --neon-pink) to manage neon palette
- Define neonPulse, neonFlicker, neonScan animations with @keyframes
- Consider adding prefers-reduced-motion media query to disable animations for users sensitive to flashing
- Optional: Use Canvas or WebGL for more complex neon tube effects

### Output Requirements
Generate complete HTML structure with inline styles ensuring:
- Clear code structure with comments explaining key glow effects
- All neon colors defined using CSS variables for easy adjustment
- Include at least 3 different neon glow effect examples (text, border, background)
- Smooth and natural animations without jarring flashing
