# Custom Prompt

## 中文版本 (zh-CN)

你现在是一位精通粒子动画与视觉效果的资深 UI 设计师兼前端工程师。请为我创建一个以漂浮粒子为核心视觉元素的网页，要求如下：

### 核心视觉特征
- **深色科技背景**：使用深蓝黑（#0a0e1a, #0f1419）或纯黑背景，营造深邃的科技氛围
- **漂浮粒子层**：背景中布满小型圆点或发光点，缓慢随机漂移，模拟星空或数据流效果
- **粒子连线**：当粒子距离接近时，使用细线连接（Canvas 或 SVG），形成动态网络结构
- **前景内容清晰**：粒子作为背景装饰，不干扰前景文字与内容的阅读

### 粒子系统设计
- **粒子数量**：根据屏幕尺寸生成 50-150 个粒子，移动设备减少至 30-80 个以优化性能
- **粒子大小**：1-4px 的圆形粒子，部分粒子稍大（5-6px）作为视觉焦点
- **粒子颜色**：半透明白色（rgba(255,255,255,0.3-0.7)）、淡蓝（rgba(100,200,255,0.4)）、青绿（rgba(100,255,200,0.3)）
- **粒子运动**：每个粒子以不同速度缓慢移动（0.2-1 像素/帧），方向随机或沿特定方向漂移

### 粒子连线算法
- **距离检测**：计算每个粒子与其他粒子的距离，当距离 < 120-150px 时绘制连线
- **连线样式**：使用细线（0.5-1px）连接，颜色与粒子相同但透明度更低（opacity: 0.2-0.4）
- **连线动画**：连线的透明度根据粒子距离动态变化（距离越近透明度越高）
- **连线限制**：每个粒子最多连接 3-5 条线，避免过密影响视觉效果

### 页面结构
1. **Hero 区域**：大标题与副标题，背景粒子缓慢漂移，文字清晰可读
2. **指标卡片**：展示关键数据的半透明卡片（如在线用户数、数据流量），边缘可有微光效果
3. **图表或控件区**：数据可视化图表或交互控件，粒子作为装饰背景
4. **日志列表或信息流**：文字列表区域，背景粒子低频漂移，不干扰阅读

### 粒子动画实现
- **Canvas 渲染**：使用 Canvas 2D API 绘制粒子与连线，性能最佳
- **requestAnimationFrame**：使用 RAF 驱动动画循环，确保流畅的 60fps
- **粒子更新逻辑**：每帧更新粒子位置（x += vx, y += vy），检测边界并反弹或环绕
- **鼠标交互**（可选）：鼠标接近时粒子被吸引或排斥，增强互动性

### 视觉层次
- **粒子在最底层**：使用 z-index: 0 或 position: fixed 确保粒子位于所有内容下方
- **半透明遮罩**：在粒子层与内容层之间添加 rgba(10,14,26,0.8) 遮罩，降低粒子干扰
- **前景内容突出**：文字与卡片使用高对比度颜色（白色、浅蓝），确保清晰可读

### 性能优化
- **Canvas 尺寸优化**：Canvas 分辨率可降至实际显示尺寸的 75%，使用 CSS 缩放至 100%
- **粒子数量自适应**：根据设备性能（通过 navigator.hardwareConcurrency 或窗口尺寸）动态调整粒子数量
- **连线距离限制**：仅计算附近粒子的距离（使用空间分区算法如 Quadtree），避免 O(n²) 复杂度
- **requestIdleCallback**：在空闲时预计算粒子轨迹，减少实时计算负担

### 粒子变体效果
- **发光粒子**：部分粒子添加 shadowBlur 效果，使其看起来发光
- **脉冲粒子**：部分粒子的透明度或大小周期性变化（使用 sin 函数），模拟呼吸效果
- **粒子爆发**：用户点击页面时，从点击位置爆发出 10-20 个短寿命粒子，快速扩散后消失
- **粒子轨迹**：部分粒子留下淡淡的轨迹线（通过不完全清除 Canvas 实现）

### 颜色对比与可读性
- **文字颜色**：使用高亮白色（#f0f4ff）或浅蓝白色（#e0e8ff），确保与深色背景对比度 ≥ 7:1
- **卡片背景**：使用半透明深色卡片（rgba(20,30,50,0.8)），模糊背景粒子，提升内容可读性
- **粒子透明度控制**：粒子透明度不超过 0.7，避免过于抢眼

### 技术要点
- 使用 Canvas API 的 arc() 绘制圆形粒子，lineTo() 绘制连线
- 使用 requestAnimationFrame 驱动动画，避免使用 setInterval
- 考虑使用 OffscreenCanvas 或 Web Workers 进行粒子计算，释放主线程
- 可选：使用 WebGL（如 Three.js 的 Points）实现更高性能的粒子系统

### 交互设计
- **鼠标跟随**：鼠标移动时，附近粒子被吸引或排斥，形成动态交互
- **点击涟漪**：点击页面时产生粒子涟漪效果，从点击位置向外扩散
- **滚动视差**：滚动页面时粒子层以不同速度移动，增强景深感

### 输出要求
请生成完整的 HTML 结构与内联样式，确保：
- 代码清晰注释，说明粒子生成、移动、连线逻辑
- 粒子参数（数量、大小、速度、连线距离）使用常量定义，便于调整
- Canvas 渲染逻辑高效，避免不必要的重绘
- 粒子动画流畅自然，不产生卡顿或闪烁


---

## English Version (en-US)

You are a senior UI designer and frontend engineer specializing in particle animations and visual effects. Create a webpage with floating particles as the core visual element with the following requirements:

### Core Visual Characteristics
- **Dark Tech Background**: Use deep blue-black (#0a0e1a, #0f1419) or pure black backgrounds to create deep tech atmosphere
- **Floating Particle Layer**: Background filled with small dots or glowing points slowly drifting randomly, simulating starfield or data flow effects
- **Particle Connections**: When particles are close, connect them with thin lines (Canvas or SVG) forming dynamic network structures
- **Clear Foreground Content**: Particles serve as background decoration without interfering with foreground text and content readability

### Particle System Design
- **Particle Count**: Generate 50-150 particles based on screen size, reduce to 30-80 on mobile devices for performance
- **Particle Size**: 1-4px circular particles, some slightly larger (5-6px) as visual focal points
- **Particle Colors**: Semi-transparent white (rgba(255,255,255,0.3-0.7)), light blue (rgba(100,200,255,0.4)), cyan-green (rgba(100,255,200,0.3))
- **Particle Motion**: Each particle moves slowly at different speeds (0.2-1 pixel/frame), random direction or drifting along specific direction

### Particle Connection Algorithm
- **Distance Detection**: Calculate distance between each particle and others, draw connections when distance < 120-150px
- **Connection Style**: Use thin lines (0.5-1px) to connect, same color as particles but lower opacity (opacity: 0.2-0.4)
- **Connection Animation**: Line opacity dynamically changes based on particle distance (closer = higher opacity)
- **Connection Limit**: Each particle connects maximum 3-5 lines to avoid excessive density affecting visual

### Page Structure
1. **Hero Section**: Large title and subtitle with slowly drifting background particles, text clearly readable
2. **Metric Cards**: Semi-transparent cards displaying key data (online users, data traffic), edges may have micro-glow effect
3. **Chart or Control Area**: Data visualization charts or interactive controls with particles as decorative background
4. **Log List or Info Stream**: Text list area with low-frequency drifting background particles not interfering with reading

### Particle Animation Implementation
- **Canvas Rendering**: Use Canvas 2D API to draw particles and connections for best performance
- **requestAnimationFrame**: Use RAF to drive animation loop ensuring smooth 60fps
- **Particle Update Logic**: Update particle position each frame (x += vx, y += vy), detect boundaries and bounce or wrap around
- **Mouse Interaction** (optional): Particles attracted or repelled when mouse approaches, enhancing interactivity

### Visual Hierarchy
- **Particles at Bottom Layer**: Use z-index: 0 or position: fixed to ensure particles below all content
- **Semi-Transparent Overlay**: Add rgba(10,14,26,0.8) overlay between particle layer and content layer to reduce particle interference
- **Foreground Content Prominence**: Text and cards use high-contrast colors (white, light blue) ensuring clear readability

### Performance Optimization
- **Canvas Size Optimization**: Canvas resolution can be reduced to 75% of actual display size, scale to 100% using CSS
- **Adaptive Particle Count**: Dynamically adjust particle count based on device performance (via navigator.hardwareConcurrency or window size)
- **Connection Distance Limit**: Only calculate distance for nearby particles (use spatial partitioning like Quadtree) avoiding O(n²) complexity
- **requestIdleCallback**: Pre-calculate particle trajectories during idle time reducing real-time computation burden

### Particle Variant Effects
- **Glowing Particles**: Some particles add shadowBlur effect making them appear glowing
- **Pulsing Particles**: Some particles' opacity or size changes periodically (using sin function) simulating breathing effect
- **Particle Burst**: User click produces 10-20 short-lived particles from click position, rapidly dispersing then disappearing
- **Particle Trails**: Some particles leave faint trail lines (by not completely clearing Canvas)

### Color Contrast & Readability
- **Text Colors**: Use bright white (#f0f4ff) or light blue-white (#e0e8ff) ensuring contrast ratio ≥ 7:1 with dark background
- **Card Background**: Use semi-transparent dark cards (rgba(20,30,50,0.8)) blurring background particles improving content readability
- **Particle Opacity Control**: Particle opacity doesn't exceed 0.7 to avoid being too eye-catching

### Technical Points
- Use Canvas API's arc() to draw circular particles, lineTo() to draw connections
- Use requestAnimationFrame to drive animations, avoid setInterval
- Consider using OffscreenCanvas or Web Workers for particle computation, freeing main thread
- Optional: Use WebGL (like Three.js Points) for higher performance particle system

### Interaction Design
- **Mouse Following**: When mouse moves, nearby particles attracted or repelled forming dynamic interaction
- **Click Ripple**: Click produces particle ripple effect radiating outward from click position
- **Scroll Parallax**: Particle layer moves at different speed when scrolling, enhancing depth perception

### Output Requirements
Generate complete HTML structure with inline styles ensuring:
- Clear code comments explaining particle generation, movement, connection logic
- Particle parameters (count, size, speed, connection distance) defined as constants for easy adjustment
- Canvas rendering logic efficient, avoiding unnecessary redraws
- Particle animations smooth and natural without stuttering or flashing
