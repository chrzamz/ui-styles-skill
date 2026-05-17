# Custom Prompt

## 中文版本 (zh-CN)

你现在是一位精通 Solarpunk（太阳朋克 / 生态未来主义）美学设计的资深 UI 设计师兼前端工程师。请为我创建一个充满绿色科技、可持续发展与乐观未来感的网页，要求如下：

### 核心视觉特征
- **明亮的绿色系**：使用阳光黄（#ffd93d, #ffe066）、草木绿（#6bc46d, #4caf50）、天空蓝（#5dade2, #85c1e9）
- **科技与自然融合**：玻璃态、金属质感与植物插画、藤蔓图案结合
- **乐观积极**：明亮配色、开放布局，传达希望与可持续发展理念
- **能源流动**：使用光束、粒子、流线展示能源流动与循环

### 页面结构
1. **Hero 区域**：大标题 + 太阳能板、风力发电机等插画元素，背景有流动的能量粒子
2. **特性卡片**：3-4 个卡片展示可持续科技特性，配有植物与科技图标
3. **能源流示意图**：光束或粒子动画展示能源从太阳能板流向城市建筑
4. **可持续指标卡**：显示碳减排、清洁能源比例等环保数据
5. **CTA 按钮**：明亮的绿色或黄色按钮，hover 时有光芒扩散效果

### 配色方案
- **主色调**：阳光黄（#ffd93d, #f9ca24），草绿（#6bc46d, #4caf50），天蓝（#5dade2）
- **辅助色**：薄荷绿（#55efc4），橙色（#fab1a0），淡紫（#a29bfe）
- **中性色**：浅灰（#dfe6e9），白色（#ffffff），深灰（#2d3436）
- **金属感**：使用银色（#ecf0f1）、浅金（#f8d59e）营造科技感

### 装饰元素
- **植物插画**：藤蔓、叶子、树木的扁平化插画，使用 SVG 绘制
- **能源光束**：使用 linear-gradient 创建从太阳/风车向建筑流动的光束
- **粒子效果**：浮动的发光粒子，代表清洁能源或数据流动
- **玻璃态卡片**：半透明白色卡片，背景模糊（backdrop-filter: blur），边缘细光晕

### 动画与交互
- **光束流动**：使用 animation: energyFlow 配合 background-position 实现光束流动（5-8s 循环）
- **粒子漂移**：小型圆形粒子缓慢上升或漂移，使用 opacity 动画模拟闪烁
- **植物生长**：SVG 植物元素使用 stroke-dasharray + animation 实现生长动画
- **hover 发光**：按钮或卡片 hover 时边缘发光增强（box-shadow 增大）

### 能源流可视化
- **太阳光束**：从页面顶部太阳图标发出向下的光束（linear-gradient，黄色 → 透明）
- **能量粒子**：使用 Canvas 或 CSS 创建浮动的发光点，沿光束路径移动
- **流动路径**：使用虚线或光点链展示能源从源头到终端的流动路径

### 文字排版
- **字体**：现代无衬线字体（如 Montserrat, Raleway），字重 500-700
- **标题**：大而醒目（48-64px），使用黄色或绿色
- **正文**：16-18px，深灰色（#2d3436），确保清晰可读
- **标签**：12-14px，使用品牌色（绿/黄）作为强调

### 技术要点
- 使用 CSS 变量定义 Solarpunk 配色（--solar-yellow, --eco-green, --sky-blue）
- 使用 @keyframes 定义 energyFlow, particleRise, plantGrow 等动画
- 使用 SVG 绘制插画元素（植物、太阳能板、风车）
- 可选：使用 Canvas 实现更复杂的粒子与能源流效果

### 情感与氛围
- **乐观积极**：明亮色彩、开放布局传达希望与活力
- **科技感**：玻璃态、光束、粒子营造现代科技氛围
- **可持续性**：绿色、植物元素强调生态与环保
- **未来感**：流动的能源、动态效果展示未来科技愿景

### 输出要求
请生成完整的 HTML 结构与内联样式，确保：
- 代码清晰注释，说明 Solarpunk 美学的实现手法
- 配色与动画参数使用 CSS 变量，便于调整
- 动画流畅自然，传达能源流动与生命力
- 页面传达出乐观、可持续、科技与自然融合的 Solarpunk 氛围


---

## English Version (en-US)

You are a senior UI designer and frontend engineer specializing in Solarpunk (eco-futurism) aesthetics. Create a webpage filled with green technology, sustainability, and optimistic future feel with the following requirements:

### Core Visual Characteristics
- **Bright Green Palette**: Use sunny yellow (#ffd93d, #ffe066), grass green (#6bc46d, #4caf50), sky blue (#5dade2, #85c1e9)
- **Tech & Nature Fusion**: Glass-morphic, metallic textures combined with plant illustrations and vine patterns
- **Optimistic Positive**: Bright colors, open layouts conveying hope and sustainable development
- **Energy Flow**: Use beams, particles, streamlines to show energy flow and cycles

### Page Structure
1. **Hero Section**: Large headline + solar panel, wind turbine illustrations with flowing energy particles in background
2. **Feature Cards**: 3-4 cards showcasing sustainable tech features with plant and tech icons
3. **Energy Flow Diagram**: Beam or particle animations showing energy flow from solar panels to city buildings
4. **Sustainability Metric Cards**: Display carbon reduction, clean energy percentage, and other eco-data
5. **CTA Buttons**: Bright green or yellow buttons with glow diffusion effect on hover

### Color Scheme
- **Primary Tones**: Sunny yellow (#ffd93d, #f9ca24), grass green (#6bc46d, #4caf50), sky blue (#5dade2)
- **Secondary Colors**: Mint green (#55efc4), orange (#fab1a0), pale purple (#a29bfe)
- **Neutrals**: Light gray (#dfe6e9), white (#ffffff), dark gray (#2d3436)
- **Metallic**: Use silver (#ecf0f1), light gold (#f8d59e) for tech feel

### Decorative Elements
- **Plant Illustrations**: Vines, leaves, trees in flat illustration style using SVG
- **Energy Beams**: Use linear-gradient to create beams flowing from sun/windmills to buildings
- **Particle Effects**: Floating glowing particles representing clean energy or data flow
- **Glass-morphic Cards**: Semi-transparent white cards with blurred backgrounds (backdrop-filter: blur), thin edge glow

### Animation & Interaction
- **Beam Flow**: Use animation: energyFlow with background-position for beam movement (5-8s loop)
- **Particle Drift**: Small circular particles slowly rise or drift using opacity animation to simulate twinkling
- **Plant Growth**: SVG plant elements use stroke-dasharray + animation for growth effect
- **Hover Glow**: Buttons or cards enhance edge glow on hover (box-shadow increases)

### Energy Flow Visualization
- **Solar Beams**: Beams emanating downward from sun icon at top (linear-gradient, yellow → transparent)
- **Energy Particles**: Use Canvas or CSS to create floating glowing dots moving along beam paths
- **Flow Paths**: Use dashed lines or light dot chains showing energy flow from source to endpoint

### Typography
- **Font**: Modern sans-serif (like Montserrat, Raleway) with weight 500-700
- **Headlines**: Large and prominent (48-64px) using yellow or green
- **Body**: 16-18px, dark gray (#2d3436) ensuring clear readability
- **Labels**: 12-14px using brand colors (green/yellow) for emphasis

### Technical Points
- Use CSS variables to define Solarpunk palette (--solar-yellow, --eco-green, --sky-blue)
- Define energyFlow, particleRise, plantGrow animations with @keyframes
- Use SVG to draw illustration elements (plants, solar panels, windmills)
- Optional: Use Canvas for more complex particle and energy flow effects

### Emotion & Atmosphere
- **Optimistic Positive**: Bright colors, open layout convey hope and vitality
- **Tech Feel**: Glass-morphic, beams, particles create modern tech atmosphere
- **Sustainability**: Green, plant elements emphasize ecology and environment
- **Future Vision**: Flowing energy, dynamic effects showcase future technology vision

### Output Requirements
Generate complete HTML structure with inline styles ensuring:
- Clear code comments explaining Solarpunk aesthetic implementation
- Color and animation parameters use CSS variables for adjustment
- Animations smooth and natural conveying energy flow and vitality
- Page conveys optimistic, sustainable, tech-nature-fusion Solarpunk atmosphere
