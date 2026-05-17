# Custom Prompt

## 中文版本 (zh-CN)

设计 3D 立方体/等距界面，使用 CSS 3D 变换创造空间深度与立体视觉效果。

**核心视觉特征**：
- CSS 3D 透视：使用 perspective (800-1200px) 创建透视空间
- 立方体变换：transform: rotateX(20deg) rotateY(-15deg) rotateZ(0deg) 创造立体角度
- 等距投影：45度角倾斜，配合 scale(1, 0.866) 模拟等距视图
- 分层堆叠：使用 translateZ() 创建不同深度的元素层次
- 旋转动画：@keyframes 在 X、Y、Z 轴上旋转立方体（6-12秒循环）
- 阴影投射：box-shadow 模拟光源投影，配合 transform 同步移动

**色彩系统**：
- 背景主题：
  - 深色科技：#0a0a0a → #1a1a2e 渐变，配合星空或网格
  - 宇宙主题：深紫 (#1a0b2e) → 深蓝 (#0f1729) 径向渐变
  - 赛博朋克：暗紫 (#0d0221) + 霓虹点缀
- 立方体配色：
  - 上表面：较亮色（#4a5568, #667eea）表现光照面
  - 左侧面：中等色（#2d3748, #4c51bf）
  - 右侧面：较暗色（#1a202c, #3730a3）表现阴影面
  - 边缘线：亮色描边（#60a5fa, #a78bfa）增强立体感
- 重点色：电蓝 (#0ea5e9), 紫色 (#a855f7), 青色 (#06b6d4)
- 文字对比：纯白 (#fff) 或淡紫 (#e9d5ff) 保证可读性

**3D 技术实现**：
- 父容器设置：
  ```css
  perspective: 1000px;
  perspective-origin: center center;
  ```
- 立方体构建：
  - 6个面分别使用 div，定位 absolute
  - 使用 transform 将每个面旋转到对应位置
  - 前面：translateZ(100px)
  - 后面：rotateY(180deg) translateZ(100px)
  - 左面：rotateY(-90deg) translateZ(100px)
  - 右面：rotateY(90deg) translateZ(100px)
  - 上面：rotateX(90deg) translateZ(100px)
  - 下面：rotateX(-90deg) translateZ(100px)
- 等距效果：
  - 使用 rotateX(35.264deg) rotateZ(-45deg) 创建等距视角
  - 配合 transform-style: preserve-3d 保持 3D 空间
- 硬件加速：transform: translateZ(0) 开启 GPU 加速

**布局与组件**：
- Hero 区域：中心放置大型旋转立方体，两侧配文字说明
- 立方体展示区：3-6个不同大小和旋转速度的立方体网格排列
- 等距卡片：使用等距投影样式的功能卡片，hover 时浮起
- 信息卡片：带有 3D 效果的扁平卡片，轻微倾斜角度
- CTA 按钮：立体按钮效果，hover 时 translateZ 增加深度
- 数据可视化：3D 柱状图或层叠图表

**动画与交互**：
- 连续旋转：
  ```css
  @keyframes rotate3d {
    from { transform: rotateX(20deg) rotateY(0deg); }
    to { transform: rotateX(20deg) rotateY(360deg); }
  }
  animation: rotate3d 10s linear infinite;
  ```
- 悬停效果：
  - 旋转暂停：animation-play-state: paused
  - 深度增加：translateZ(50px)
  - 发光效果：box-shadow 强度增加
- 交错动画：使用 animation-delay 让不同立方体错开启动时间
- 视差滚动：背景立方体慢速滚动，前景立方体快速滚动
- 鼠标跟踪：使用 JS 监听 mousemove，根据鼠标位置调整 rotateX/Y

**光照与阴影**：
- 顶部光源：上表面最亮，使用浅色
- 侧面渐变：左侧较亮，右侧较暗，模拟斜向光源
- 投影阴影：
  ```css
  box-shadow:
    20px 30px 60px rgba(0,0,0,0.6),
    inset -5px -5px 10px rgba(0,0,0,0.3);
  ```
- 边缘高光：使用 border 或 box-shadow 创建亮色边缘线
- 环境光：整体使用低饱和度背景色模拟环境光反射

**可读性保障**：
- 文字叠层：3D 元素作为背景装饰，文字内容在 2D 平面上
- 高对比文字：纯白或高亮色，避免放在旋转元素上
- 静态内容区：重要信息放在无 3D 变换的区域
- 阴影衬底：文字添加 text-shadow: 0 2px 8px rgba(0,0,0,0.8)
- 避免过度旋转：主要内容区域倾斜角度控制在 15-25 度以内

**等距网格系统**：
- 网格角度：使用 transform: rotateX(60deg) rotateZ(-45deg) 创建等距网格
- 网格间距：统一使用 30-40px 间距保持视觉一致性
- 层级堆叠：使用 z-index 配合 translateZ 控制元素前后关系
- 点击热区：为等距元素提供足够大的点击区域（至少 44x44px）
- 伪 3D 图标：使用多层叠加创建伪 3D 图标效果

**性能优化**：
- 减少 DOM 节点：每个立方体使用最少的 div 数量（可用 CSS 伪元素优化）
- will-change: transform 提示浏览器优化
- 降低动画复杂度：移动端减少旋转轴数量（仅 Y 轴旋转）
- 使用 CSS 变量：动态计算旋转角度，避免 JS 频繁操作
- 懒加载：非可视区域的 3D 元素暂停动画

**响应式策略**：
- 移动端：
  - 减少立方体数量（6个 → 3个）
  - 简化动画（禁用复杂旋转）
  - 降低透视深度（1000px → 600px）
  - 静态等距视图代替旋转动画
- 平板端：
  - 保留主要立方体动画
  - 简化背景装饰元素
  - 使用较小的 perspective 值
- 桌面端：
  - 完整 3D 效果 + 复杂动画
  - 鼠标交互增强
  - 视差滚动效果

**典型应用场景**：
- 科技产品展示：3D 产品模型、设备展示、硬件介绍
- 区块链/加密货币：立方体代表区块，旋转展示数据流动
- 游戏/娱乐：游戏元素展示、等距关卡预览、立体界面
- 建筑/设计：等距建筑图、室内设计展示、空间规划
- 教育/科普：3D 模型展示、分子结构、几何教学
- 创意作品集：独特的项目展示方式，吸引注意力


---

## English Version (en-US)

Design 3D cube/isometric interfaces using CSS 3D transforms to create spatial depth and stereoscopic visual effects.

**Core Visual Characteristics**:
- CSS 3D perspective: Use perspective (800-1200px) to create perspective space
- Cube transforms: transform: rotateX(20deg) rotateY(-15deg) rotateZ(0deg) creates 3D angles
- Isometric projection: 45-degree tilt with scale(1, 0.866) to simulate isometric view
- Layered stacking: Use translateZ() to create different depth element layers
- Rotation animation: @keyframes rotating cubes on X, Y, Z axes (6-12 second loops)
- Cast shadows: box-shadow simulates light source projection, moves synchronously with transform

**Color System**:
- Background themes:
  - Dark tech: #0a0a0a → #1a1a2e gradient with starry sky or grid
  - Cosmic theme: Deep purple (#1a0b2e) → deep blue (#0f1729) radial gradient
  - Cyberpunk: Dark purple (#0d0221) + neon accents
- Cube coloring:
  - Top surface: Brighter colors (#4a5568, #667eea) representing lit surface
  - Left surface: Medium colors (#2d3748, #4c51bf)
  - Right surface: Darker colors (#1a202c, #3730a3) representing shadowed surface
  - Edge lines: Bright strokes (#60a5fa, #a78bfa) enhance 3D feel
- Accent colors: Electric blue (#0ea5e9), purple (#a855f7), cyan (#06b6d4)
- Text contrast: Pure white (#fff) or light lavender (#e9d5ff) for readability

**3D Technical Implementation**:
- Parent container setup:
  ```css
  perspective: 1000px;
  perspective-origin: center center;
  ```
- Cube construction:
  - 6 faces each using div, positioned absolute
  - Use transform to rotate each face to corresponding position
  - Front: translateZ(100px)
  - Back: rotateY(180deg) translateZ(100px)
  - Left: rotateY(-90deg) translateZ(100px)
  - Right: rotateY(90deg) translateZ(100px)
  - Top: rotateX(90deg) translateZ(100px)
  - Bottom: rotateX(-90deg) translateZ(100px)
- Isometric effect:
  - Use rotateX(35.264deg) rotateZ(-45deg) to create isometric view
  - With transform-style: preserve-3d to maintain 3D space
- Hardware acceleration: transform: translateZ(0) enables GPU acceleration

**Layout & Components**:
- Hero section: Large rotating cube centered with text explanations on sides
- Cube showcase area: Grid of 3-6 cubes with different sizes and rotation speeds
- Isometric cards: Feature cards with isometric projection style, lift on hover
- Info cards: Flat cards with 3D effects and slight tilt angle
- CTA buttons: 3D button effect, increase depth with translateZ on hover
- Data visualization: 3D bar charts or layered charts

**Animation & Interaction**:
- Continuous rotation:
  ```css
  @keyframes rotate3d {
    from { transform: rotateX(20deg) rotateY(0deg); }
    to { transform: rotateX(20deg) rotateY(360deg); }
  }
  animation: rotate3d 10s linear infinite;
  ```
- Hover effects:
  - Pause rotation: animation-play-state: paused
  - Increase depth: translateZ(50px)
  - Glow effect: Increase box-shadow intensity
- Staggered animation: Use animation-delay to offset cube start times
- Parallax scrolling: Background cubes scroll slowly, foreground cubes scroll fast
- Mouse tracking: Use JS to listen for mousemove, adjust rotateX/Y based on mouse position

**Lighting & Shadows**:
- Top light source: Top surface brightest using light colors
- Side gradients: Left side brighter, right side darker, simulating angled light source
- Cast shadows:
  ```css
  box-shadow:
    20px 30px 60px rgba(0,0,0,0.6),
    inset -5px -5px 10px rgba(0,0,0,0.3);
  ```
- Edge highlights: Use border or box-shadow to create bright edge lines
- Ambient light: Overall use low saturation background colors to simulate ambient light reflection

**Readability Safeguards**:
- Text layering: 3D elements as background decoration, text content on 2D plane
- High contrast text: Pure white or bright colors, avoid placing on rotating elements
- Static content areas: Important information in areas without 3D transforms
- Shadow backing: Text with text-shadow: 0 2px 8px rgba(0,0,0,0.8)
- Avoid excessive rotation: Main content area tilt angle within 15-25 degrees

**Isometric Grid System**:
- Grid angle: Use transform: rotateX(60deg) rotateZ(-45deg) to create isometric grid
- Grid spacing: Uniformly use 30-40px spacing to maintain visual consistency
- Layer stacking: Use z-index with translateZ to control element front-back relationships
- Click targets: Provide sufficiently large click areas for isometric elements (at least 44x44px)
- Pseudo 3D icons: Use multi-layer overlay to create pseudo 3D icon effects

**Performance Optimization**:
- Reduce DOM nodes: Use minimum div count per cube (can optimize with CSS pseudo-elements)
- will-change: transform hints browser to optimize
- Reduce animation complexity: Mobile reduces rotation axes (Y-axis only)
- Use CSS variables: Dynamically calculate rotation angles, avoid frequent JS operations
- Lazy loading: Pause animations for 3D elements outside viewport

**Responsive Strategy**:
- Mobile:
  - Reduce cube count (6 → 3)
  - Simplify animations (disable complex rotations)
  - Lower perspective depth (1000px → 600px)
  - Static isometric view instead of rotation animation
- Tablet:
  - Retain main cube animations
  - Simplify background decorative elements
  - Use smaller perspective values
- Desktop:
  - Full 3D effects + complex animations
  - Enhanced mouse interactions
  - Parallax scrolling effects

**Typical Use Cases**:
- Tech product showcase: 3D product models, device displays, hardware introductions
- Blockchain/cryptocurrency: Cubes representing blocks, rotating to show data flow
- Gaming/entertainment: Game element displays, isometric level previews, stereoscopic interfaces
- Architecture/design: Isometric building diagrams, interior design displays, space planning
- Education/science: 3D model displays, molecular structures, geometry teaching
- Creative portfolios: Unique project presentation methods to attract attention
