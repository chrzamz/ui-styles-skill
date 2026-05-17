# Custom Prompt

## 中文版本 (zh-CN)

你现在是一位精通 Soft UI（柔和 UI / 新拟态）设计的资深 UI 设计师兼前端工程师。请为我创建一个以柔和内外阴影为核心视觉元素的网页，要求如下：

### 核心视觉特征
- **浅色或低饱和底色**：使用浅灰（#e0e5ec, #f0f4f8）、淡蓝（#e8f0fe）、米色（#f5f1e8）作为背景
- **双向阴影**：元素使用内阴影（inset）与外阴影组合，营造轻微凸起或凹陷效果
- **大圆角**：按钮、卡片使用大圆角（border-radius: 16-32px），营造柔和感
- **低对比度**：元素与背景颜色接近，通过阴影区分层次

### Soft UI 实现技巧
- **凸起效果**：box-shadow: -5px -5px 10px rgba(255,255,255,0.8), 5px 5px 10px rgba(0,0,0,0.1)（左上亮，右下暗）
- **凹陷效果**：box-shadow: inset 2px 2px 5px rgba(0,0,0,0.1), inset -2px -2px 5px rgba(255,255,255,0.8)
- **按钮按下**：active 状态使用凹陷阴影，hover 状态阴影增强
- **颜色同步**：阴影颜色基于背景色，亮阴影使用白色，暗阴影使用背景色的暗版

### 页面结构
1. **Hero 区域**：大标题，背景为统一浅色，周围无明显边界
2. **设置面板示例**：切换开关、滑块、输入框，所有控件使用 Soft UI 凸起/凹陷效果
3. **KPI 指标卡**：3-4 个卡片展示数据，卡片微微凸起，数字清晰可读
4. **CTA 按钮**：大圆角按钮，默认凸起，hover 时阴影增强，active 时凹陷

### 配色方案
- **背景色**：浅灰（#e0e5ec），淡蓝灰（#e8ecf1），米白（#f5f1e8）
- **元素色**：与背景相近，略深或略浅 5-10% 的色调
- **文字色**：中灰（#6e7c87, #8a95a0），确保与背景对比度 ≥ 4.5:1
- **强调色**：低饱和度蓝（#7ba7d6）、绿（#8bc9a8）、橙（#e8b389），用于开关、进度条

### 交互状态
- **Default**：元素凸起，外阴影 + 浅色内反光
- **Hover**：阴影模糊范围增大，凸起感增强
- **Active**：阴影反转为凹陷效果，模拟按下
- **Disabled**：阴影减弱，元素颜色变淡

### 动画与交互
- **阴影过渡**：所有状态变化使用 transition: box-shadow 0.3s ease
- **轻微缩放**：hover 时 transform: scale(1.02)，增强交互反馈
- **柔和动画**：避免突兀的跳跃，所有动画使用 ease-in-out 曲线

### 文字排版
- **字体**：圆润的无衬线字体（如 Inter, Poppins），字重 400-600
- **字号**：标题 24-32px，正文 14-16px，控件标签 12-14px
- **颜色**：中灰色，避免纯黑，确保柔和感

### 技术要点
- 使用 CSS 变量定义阴影（--soft-shadow-light, --soft-shadow-dark）
- 使用 box-shadow 的多层叠加实现 Soft UI 效果
- 考虑暗色模式：深色底 + 深浅阴影组合

### 输出要求
请生成完整的 HTML 结构与内联样式，确保：
- 代码清晰注释，说明凸起/凹陷效果的实现
- 阴影参数使用 CSS 变量，便于调整
- 交互状态流畅自然，阴影过渡柔和


---

## English Version (en-US)

You are a senior UI designer and frontend engineer specializing in Soft UI (Neumorphism-lite) design. Create a webpage with soft inner/outer shadows as core visual elements with the following requirements:

### Core Visual Characteristics
- **Light or Low-Saturation Base**: Use light gray (#e0e5ec, #f0f4f8), pale blue (#e8f0fe), beige (#f5f1e8) backgrounds
- **Dual-Direction Shadows**: Elements use inset and outer shadows combined creating slight raised or recessed effects
- **Large Border-Radius**: Buttons, cards use large border-radius (16-32px) for softness
- **Low Contrast**: Elements similar color to background, differentiated by shadows

### Soft UI Implementation
- **Raised Effect**: box-shadow: -5px -5px 10px rgba(255,255,255,0.8), 5px 5px 10px rgba(0,0,0,0.1) (top-left bright, bottom-right dark)
- **Recessed Effect**: box-shadow: inset 2px 2px 5px rgba(0,0,0,0.1), inset -2px -2px 5px rgba(255,255,255,0.8)
- **Button Press**: active state uses recessed shadow, hover state enhances shadow
- **Color Sync**: Shadow colors based on background color, bright shadows use white, dark shadows use darker background version

### Page Structure
1. **Hero Section**: Large headline with uniform light background, no obvious boundaries
2. **Settings Panel Example**: Toggle switches, sliders, inputs, all controls use Soft UI raised/recessed effects
3. **KPI Cards**: 3-4 cards displaying data, cards slightly raised, numbers clearly readable
4. **CTA Buttons**: Large rounded buttons, default raised, shadow enhances on hover, recessed on active

### Color Scheme
- **Background**: Light gray (#e0e5ec), pale blue-gray (#e8ecf1), beige-white (#f5f1e8)
- **Element Colors**: Similar to background, slightly deeper or lighter 5-10% tone
- **Text Colors**: Mid-gray (#6e7c87, #8a95a0) ensuring contrast ≥ 4.5:1 with background
- **Accent Colors**: Low-saturation blue (#7ba7d6), green (#8bc9a8), orange (#e8b389) for switches, progress bars

### Interaction States
- **Default**: Element raised with outer shadow + light inner reflection
- **Hover**: Shadow blur range increases, raised feel enhances
- **Active**: Shadow inverts to recessed effect simulating press
- **Disabled**: Shadow weakens, element color fades

### Animation & Interaction
- **Shadow Transition**: All state changes use transition: box-shadow 0.3s ease
- **Slight Scale**: hover applies transform: scale(1.02) enhancing interaction feedback
- **Soft Animation**: Avoid abrupt jumps, all animations use ease-in-out curves

### Typography
- **Font**: Rounded sans-serif (like Inter, Poppins) with weight 400-600
- **Size**: Headings 24-32px, body 14-16px, control labels 12-14px
- **Color**: Mid-gray, avoid pure black for softness

### Technical Points
- Use CSS variables to define shadows (--soft-shadow-light, --soft-shadow-dark)
- Use multi-layer box-shadow stacking for Soft UI effects
- Consider dark mode: deep background + light/dark shadow combination

### Output Requirements
Generate complete HTML structure with inline styles ensuring:
- Clear code comments explaining raised/recessed effect implementation
- Shadow parameters use CSS variables for adjustment
- Interaction states smooth and natural with soft shadow transitions
