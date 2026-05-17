# Custom Prompt

## 中文版本 (zh-CN)

你现在是一位精通色彩渐变设计的资深 UI 设计师兼前端工程师。请为我创建一个以大面积渐变为核心视觉元素的网页，要求如下：

### 核心视觉特征
- **大胆的渐变背景**：使用全屏或大面积线性/径向/锥形渐变作为主视觉，不限于单一方向
- **丰富的配色方案**：至少使用 3-5 种颜色的渐变，色彩过渡自然流畅
- **渐变类型多样性**：展示 linear-gradient、radial-gradient、conic-gradient、mesh-gradient（如果支持）等多种渐变形式
- **色彩情感表达**：通过渐变配色传达特定情感（温暖、冷静、活力、优雅等）

### 渐变技术实现
- **线性渐变**：使用 linear-gradient(角度, 色1, 色2, 色3) 创建方向性渐变，角度可为 45deg、135deg、180deg 等
- **径向渐变**：使用 radial-gradient(circle at 位置, 色1, 色2) 创建从中心向外扩散的渐变
- **锥形渐变**：使用 conic-gradient(from 角度 at 位置, 色1, 色2, 色3) 创建圆锥形渐变效果
- **多层叠加**：使用多个渐变层叠加（background: gradient1, gradient2），配合 opacity 和 mix-blend-mode 产生复杂效果

### 配色策略
- **单色渐变**：同一色相的不同明度/饱和度渐变（如浅蓝 → 深蓝 → 极深蓝）
- **邻近色渐变**：色环上相邻颜色的渐变（如橙 → 黄 → 绿，或蓝 → 紫 → 粉）
- **互补色渐变**：对比强烈的互补色渐变（如蓝 → 橙，或紫 → 黄），中间可加入过渡色
- **Aurora 极光配色**：多彩极光效果（粉 → 紫 → 蓝 → 青 → 绿），使用高饱和度色彩
- **Sunset 日落配色**：温暖日落效果（深蓝 → 紫 → 橙 → 黄 → 浅黄），模拟天空色彩变化

### 页面结构
1. **Hero 区域**：全屏大型渐变背景，标题文字使用半透明白色或深色确保可读性
2. **渐变示例网格**：展示 6-9 个不同的渐变样本卡片，每个卡片展示一种渐变配色或方向
3. **渐变参数说明**：在每个示例下方标注渐变参数（角度、颜色值、类型），方便理解
4. **内容分栏**：使用渐变背景的卡片展示文字内容，确保文字与渐变对比度充足
5. **CTA 按钮**：按钮本身使用渐变填充，hover 时渐变方向反转或颜色加深

### 渐变动画效果
- **色彩流动**：使用 animation: gradientShift 配合 background-position 或 background-size 制造渐变缓慢移动效果
- **渐变旋转**：conic-gradient 配合 animation: rotate 实现圆锥渐变旋转效果
- **色彩变换**：使用 @keyframes 改变渐变色彩值，实现渐变配色动态变化（需谨慎使用，可能影响性能）
- **hover 渐变**：按钮或卡片 hover 时渐变角度或颜色发生变化，使用 transition: background 0.5s ease

### 对比度与可读性
- **文字颜色选择**：在浅色渐变上使用深色文字，在深色渐变上使用浅色文字，确保对比度 ≥ 4.5:1
- **半透明遮罩**：在渐变背景上叠加 rgba(0,0,0,0.2-0.5) 遮罩层，降低背景干扰，提升文字可读性
- **渐变方向控制**：确保文字区域的渐变过渡不会造成部分文字不可读（避免中间恰好是中灰色）

### 性能优化
- **避免复杂动画渐变**：使用 transform 和 opacity 实现动画，而非直接改变 background-image 属性
- **使用 will-change**：为动画渐变元素添加 will-change: transform，启用 GPU 加速
- **限制渐变层数**：单个元素的叠加渐变不超过 3 层，避免过度计算
- **静态渐变优先**：大部分渐变使用静态背景，仅关键元素使用动画渐变

### 技术要点
- 使用 CSS 自定义属性定义渐变配色（--gradient-1, --gradient-2）便于全局调整
- 使用 @keyframes 定义 gradientShift, gradientRotate 等动画
- 考虑使用 CSS Houdini Paint API（如 @property）实现更平滑的渐变动画过渡
- 可选：使用 Canvas 或 SVG 绘制更复杂的 mesh gradient 效果

### 渐变最佳实践
- **色彩数量**：单个渐变使用 2-5 种颜色为宜，过多会显得杂乱
- **色彩位置**：合理分配色标位置（如 0%, 30%, 70%, 100%），避免过于均匀导致失去重点
- **渐变角度**：常用角度为 45deg、135deg、180deg，或根据页面布局选择最佳方向
- **渐变应用**：背景、按钮、卡片边框、文字颜色（text via background-clip）、装饰元素等

### 输出要求
请生成完整的 HTML 结构与内联样式，确保：
- 代码清晰注释，标注每个渐变的类型与配色方案
- 所有渐变配色使用 CSS 变量定义，便于调整
- 包含至少 6 种不同的渐变效果示例（线性、径向、锥形，不同配色）
- 渐变过渡自然，色彩搭配和谐，符合视觉美学


---

## English Version (en-US)

You are a senior UI designer and frontend engineer specializing in color gradient design. Create a webpage with large-scale gradients as the core visual element with the following requirements:

### Core Visual Characteristics
- **Bold Gradient Backgrounds**: Use full-screen or large-area linear/radial/conic gradients as main visuals, not limited to single direction
- **Rich Color Schemes**: Use at least 3-5 colors in gradients with natural, smooth transitions
- **Gradient Type Diversity**: Showcase multiple gradient forms including linear-gradient, radial-gradient, conic-gradient, mesh-gradient (if supported)
- **Color Emotional Expression**: Convey specific emotions through gradient color schemes (warm, calm, energetic, elegant, etc.)

### Gradient Technical Implementation
- **Linear Gradients**: Use linear-gradient(angle, color1, color2, color3) to create directional gradients with angles like 45deg, 135deg, 180deg
- **Radial Gradients**: Use radial-gradient(circle at position, color1, color2) to create center-outward diffusion gradients
- **Conic Gradients**: Use conic-gradient(from angle at position, color1, color2, color3) to create conical gradient effects
- **Multi-Layer Overlay**: Stack multiple gradient layers (background: gradient1, gradient2) with opacity and mix-blend-mode for complex effects

### Color Palette Strategies
- **Monochromatic Gradients**: Different lightness/saturation gradients of same hue (light blue → deep blue → ultra deep blue)
- **Analogous Color Gradients**: Adjacent colors on color wheel gradients (orange → yellow → green, or blue → purple → pink)
- **Complementary Color Gradients**: High-contrast complementary color gradients (blue → orange, or purple → yellow) with intermediate transition colors
- **Aurora Palette**: Multi-color aurora effect (pink → purple → blue → cyan → green) using high-saturation colors
- **Sunset Palette**: Warm sunset effect (deep blue → purple → orange → yellow → light yellow) simulating sky color changes

### Page Structure
1. **Hero Section**: Full-screen large gradient background with semi-transparent white or dark text ensuring readability
2. **Gradient Sample Grid**: Display 6-9 different gradient sample cards, each showing one gradient color scheme or direction
3. **Gradient Parameter Labels**: Mark gradient parameters (angle, color values, type) below each example for understanding
4. **Content Columns**: Use gradient background cards to display text content, ensuring sufficient text-to-gradient contrast
5. **CTA Buttons**: Buttons filled with gradients, hover reverses gradient direction or deepens colors

### Gradient Animation Effects
- **Color Flow**: Use animation: gradientShift with background-position or background-size to create slow gradient movement
- **Gradient Rotation**: Conic-gradient with animation: rotate to achieve conical gradient rotation
- **Color Transformation**: Use @keyframes to change gradient color values for dynamic color scheme changes (use cautiously, may affect performance)
- **Hover Gradient**: Button or card hover changes gradient angle or colors using transition: background 0.5s ease

### Contrast & Readability
- **Text Color Selection**: Use dark text on light gradients, light text on dark gradients, ensuring contrast ≥ 4.5:1
- **Semi-Transparent Overlay**: Add rgba(0,0,0,0.2-0.5) overlay on gradient backgrounds to reduce interference and improve text readability
- **Gradient Direction Control**: Ensure gradient transitions in text areas don't cause partial text unreadability (avoid mid-gray in middle)

### Performance Optimization
- **Avoid Complex Animated Gradients**: Use transform and opacity for animations rather than directly changing background-image property
- **Use will-change**: Add will-change: transform to animated gradient elements for GPU acceleration
- **Limit Gradient Layers**: Single element overlay gradients shouldn't exceed 3 layers to avoid excessive computation
- **Static Gradients First**: Most gradients use static backgrounds, only key elements use animated gradients

### Technical Points
- Use CSS custom properties to define gradient color schemes (--gradient-1, --gradient-2) for global adjustment
- Define gradientShift, gradientRotate animations with @keyframes
- Consider using CSS Houdini Paint API (like @property) for smoother gradient animation transitions
- Optional: Use Canvas or SVG to draw more complex mesh gradient effects

### Gradient Best Practices
- **Color Count**: Single gradient should use 2-5 colors, too many appears cluttered
- **Color Positions**: Reasonably distribute color stop positions (e.g., 0%, 30%, 70%, 100%), avoid too uniform distribution losing focus
- **Gradient Angles**: Common angles are 45deg, 135deg, 180deg, or choose best direction based on page layout
- **Gradient Applications**: Backgrounds, buttons, card borders, text colors (via background-clip), decorative elements, etc.

### Output Requirements
Generate complete HTML structure with inline styles ensuring:
- Clear code comments marking each gradient's type and color scheme
- All gradient color schemes defined using CSS variables for adjustment
- Include at least 6 different gradient effect examples (linear, radial, conic, various color schemes)
- Natural gradient transitions with harmonious color combinations conforming to visual aesthetics
