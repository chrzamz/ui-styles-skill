# Custom Prompt

## 中文版本 (zh-CN)

你现在是一位精通 Vaporwave（蒸汽波）美学设计的资深 UI 设计师兼前端工程师。请为我创建一个充满 80/90 年代怀旧感与赛博朋克风格的网页，要求如下：

### 核心视觉特征
- **粉紫青配色**：使用霓虹粉（#ff6ad5, #ff71ce）、电紫（#c774e8, #ad8ee6）、青色（#00d8ff, #72f1b8）组合
- **透视网格地面**：使用 repeating-linear-gradient 创建透视网格地面，模拟 80 年代电脑图形
- **渐变天空**：粉 → 紫 → 蓝的渐变背景，模拟日落或赛博天空
- **复古图标**：像素化图标、几何形状、80 年代计算机元素

### Vaporwave 标志元素
- **古希腊雕像**：大卫像、维纳斯等古典雕像的剪影或线描（使用 SVG 或 CSS）
- **棕榈树剪影**：黑色或深紫色棕榈树轮廓，营造热带夜晚氛围
- **几何形状**：三角形、方形、圆形的霓虹轮廓，漂浮在空间中
- **日本文字**：使用日文假名或汉字作为装饰元素（如「未来」「夢」）
- **Windows 95 元素**：复古窗口边框、像素化按钮、系统字体

### 背景实现
- **渐变天空**：`linear-gradient(180deg, #ff6ad5 0%, #c774e8 50%, #00d8ff 100%)`
- **透视网格**：使用 CSS 3D transform 创建透视网格地面，网格线为霓虹青色
- **太阳/月亮**：大型圆形渐变球体，模拟落日或升月（radial-gradient）

### 页面结构
1. **Hero 区域**：霓虹标题 + 雕像剪影 + 棕榈树，背景为渐变天空与透视网格
2. **特性卡片**：3-4 个玻璃态卡片，边框霓虹粉/青色，内部半透明
3. **播放列表/画廊区**：展示专辑封面或图片网格，使用霓虹边框
4. **装饰元素**：页面四角或边缘添加几何形状、日文文字装饰

### 配色方案
- **主色调**：霓虹粉（#ff6ad5, #ff71ce），电紫（#c774e8, #ad8ee6），青色（#00d8ff, #72f1b8）
- **辅助色**：霓虹黄（#fffd82, #fdff9a），深紫（#2b1055, #3d1766）
- **背景色**：深紫黑（#200f33, #1a0a2e），渐变天空（粉紫蓝）
- **文字色**：白色（#ffffff），霓虹粉（#ff71ce），青色（#00d8ff）

### 透视网格实现
```css
.perspective-grid {
  perspective: 400px;
  transform-style: preserve-3d;
}

.grid {
  background: repeating-linear-gradient(
    90deg,
    transparent,
    transparent 79px,
    #00d8ff 79px,
    #00d8ff 81px
  ),
  repeating-linear-gradient(
    180deg,
    transparent,
    transparent 79px,
    #00d8ff 79px,
    #00d8ff 81px
  );
  transform: rotateX(60deg);
  opacity: 0.6;
}
```

### 动画与交互
- **网格流动**：透视网格使用 animation: gridFlow 缓慢向后移动，模拟前进感
- **霓虹脉冲**：标题与边框使用 animation: neonPulse 2-3s infinite，透明度与阴影微幅变化
- **雕像漂浮**：雕像剪影轻微上下漂浮（animation: float 6s infinite ease-in-out）
- **hover 发光**：卡片或按钮 hover 时霓虹边框发光增强

### 文字排版
- **字体选择**：使用复古等宽字体（如 Courier New, VT323）或霓虹风格字体
- **标题**：大而醒目（60-80px），使用霓虹粉或青色，带 text-shadow 发光效果
- **正文**：16-18px，白色或浅粉色，确保可读性
- **装饰文字**：日文文字使用较大字号（24-32px），半透明（opacity: 0.3-0.5）

### 技术要点
- 使用 CSS 变量定义 Vaporwave 配色（--vaporwave-pink, --vaporwave-cyan, --vaporwave-purple）
- 使用 @keyframes 定义 gridFlow, neonPulse, float 等动画
- 使用 SVG 或 CSS clip-path 创建雕像与棕榈树剪影
- 可选：使用 Canvas 实现更复杂的粒子或星空效果

### 情感与氛围
- **怀旧感**：80/90 年代电脑图形、霓虹灯、复古元素
- **梦幻感**：粉紫渐变天空、漂浮元素、柔和光晕
- **赛博朋克**：霓虹色、网格地面、未来与复古交织
- **孤独美**：雕像、棕榈树、日落营造孤独但美丽的氛围

### 输出要求
请生成完整的 HTML 结构与内联样式，确保：
- 代码清晰注释，说明 Vaporwave 美学的实现手法
- 配色与动画参数使用 CSS 变量，便于调整
- 包含至少 4 种 Vaporwave 标志元素（雕像、棕榈树、网格、渐变天空）
- 动画流畅自然，传达出怀旧、梦幻、赛博的 Vaporwave 氛围


---

## English Version (en-US)

You are a senior UI designer and frontend engineer specializing in Vaporwave aesthetics. Create a webpage filled with 80s/90s nostalgia and cyberpunk style with the following requirements:

### Core Visual Characteristics
- **Pink-Purple-Cyan Palette**: Use neon pink (#ff6ad5, #ff71ce), electric purple (#c774e8, #ad8ee6), cyan (#00d8ff, #72f1b8) combinations
- **Perspective Grid Floor**: Use repeating-linear-gradient to create perspective grid floor simulating 80s computer graphics
- **Gradient Sky**: Pink → purple → blue gradient background simulating sunset or cyber sky
- **Retro Icons**: Pixelated icons, geometric shapes, 80s computer elements

### Vaporwave Signature Elements
- **Greek Statues**: Silhouettes or line drawings of David, Venus, etc. classical statues (using SVG or CSS)
- **Palm Tree Silhouettes**: Black or deep purple palm tree outlines creating tropical night atmosphere
- **Geometric Shapes**: Neon-outlined triangles, squares, circles floating in space
- **Japanese Text**: Use Japanese kana or kanji as decorative elements (like「未来」「夢」)
- **Windows 95 Elements**: Retro window borders, pixelated buttons, system fonts

### Background Implementation
- **Gradient Sky**: `linear-gradient(180deg, #ff6ad5 0%, #c774e8 50%, #00d8ff 100%)`
- **Perspective Grid**: Use CSS 3D transform to create perspective grid floor with neon cyan grid lines
- **Sun/Moon**: Large circular gradient sphere simulating sunset or moonrise (radial-gradient)

### Page Structure
1. **Hero Section**: Neon headline + statue silhouette + palm trees with gradient sky and perspective grid background
2. **Feature Cards**: 3-4 glass-morphic cards with neon pink/cyan borders, semi-transparent interior
3. **Playlist/Gallery Area**: Album cover or image grid display using neon borders
4. **Decorative Elements**: Geometric shapes, Japanese text decorations at page corners or edges

### Color Scheme
- **Primary Tones**: Neon pink (#ff6ad5, #ff71ce), electric purple (#c774e8, #ad8ee6), cyan (#00d8ff, #72f1b8)
- **Secondary Colors**: Neon yellow (#fffd82, #fdff9a), deep purple (#2b1055, #3d1766)
- **Background**: Deep purple-black (#200f33, #1a0a2e), gradient sky (pink-purple-blue)
- **Text Colors**: White (#ffffff), neon pink (#ff71ce), cyan (#00d8ff)

### Perspective Grid Implementation
```css
.perspective-grid {
  perspective: 400px;
  transform-style: preserve-3d;
}

.grid {
  background: repeating-linear-gradient(
    90deg,
    transparent,
    transparent 79px,
    #00d8ff 79px,
    #00d8ff 81px
  ),
  repeating-linear-gradient(
    180deg,
    transparent,
    transparent 79px,
    #00d8ff 79px,
    #00d8ff 81px
  );
  transform: rotateX(60deg);
  opacity: 0.6;
}
```

### Animation & Interaction
- **Grid Flow**: Perspective grid uses animation: gridFlow slowly moving backward simulating forward motion
- **Neon Pulse**: Headline and borders use animation: neonPulse 2-3s infinite with subtle opacity and shadow variations
- **Statue Float**: Statue silhouettes lightly float up and down (animation: float 6s infinite ease-in-out)
- **Hover Glow**: Card or button hover enhances neon border glow

### Typography
- **Font Choice**: Use retro monospace fonts (like Courier New, VT323) or neon-style fonts
- **Headlines**: Large and prominent (60-80px) using neon pink or cyan with text-shadow glow effect
- **Body**: 16-18px, white or light pink ensuring readability
- **Decorative Text**: Japanese text uses larger sizes (24-32px), semi-transparent (opacity: 0.3-0.5)

### Technical Points
- Use CSS variables to define Vaporwave palette (--vaporwave-pink, --vaporwave-cyan, --vaporwave-purple)
- Define gridFlow, neonPulse, float animations with @keyframes
- Use SVG or CSS clip-path to create statue and palm tree silhouettes
- Optional: Use Canvas for more complex particle or starfield effects

### Emotion & Atmosphere
- **Nostalgia**: 80s/90s computer graphics, neon lights, retro elements
- **Dreamlike**: Pink-purple gradient sky, floating elements, soft halos
- **Cyberpunk**: Neon colors, grid floor, future and retro intertwined
- **Lonely Beauty**: Statues, palm trees, sunset creating lonely but beautiful atmosphere

### Output Requirements
Generate complete HTML structure with inline styles ensuring:
- Clear code comments explaining Vaporwave aesthetic implementation
- Color and animation parameters use CSS variables for adjustment
- Include at least 4 Vaporwave signature elements (statue, palm tree, grid, gradient sky)
- Animations smooth and natural conveying nostalgic, dreamlike, cyber Vaporwave atmosphere
