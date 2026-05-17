# Custom Prompt

## 中文版本 (zh-CN)

设计生成艺术（Generative Art）风格界面，使用算法驱动的视觉元素创造独特动态美学。

**核心视觉特征**：算法生成的图案背景、程序化噪点/粒子效果、几何线条/曲线动画、数学美感的抽象图形、颜色循环变化、实时生成动态效果。

**技术实现**：使用 Canvas API 或 SVG 绘制生成图案、Perlin noise 创建有机纹理、粒子系统模拟动态效果、递归算法生成分形图案、随机化参数创造独特性、requestAnimationFrame 实现流畅动画。

**核心算法**：
- Perlin/Simplex noise：有机流动纹理
- Particle systems：粒子轨迹和爆发效果
- L-systems：植物/分形生长模式
- Voronoi diagrams：细胞状分割图案
- Flow fields：流体动力学模拟
- Fractal trees：递归分形树

**色彩系统**：使用算法生成色彩方案（HSL color space 循环）、渐变映射 noise 值到颜色、动态 hue rotation、可自定义调色板（单色、互补色、类比色、三色）。

**布局与组件**：
- Hero 区域：全屏生成艺术背景，前景简洁内容
- 控制面板：滑块调整参数（速度、密度、颜色、复杂度）
- 缩略图网格：展示不同生成结果
- 实时预览：参数变化时即时更新
- 保存/分享：导出为图片或分享 seed 值

**交互设计**：
- 鼠标移动：影响粒子流动方向或图案变形
- 点击：触发新图案生成或颜色变化
- 滚动：驱动动画进度或参数渐变
- 参数滑块：实时调整生成算法参数
- 随机按钮：生成全新随机图案
- 重置按钮：恢复默认参数

**性能优化**：
- 使用 Web Workers 处理复杂计算
- requestAnimationFrame 代替 setInterval
- Canvas offscreen rendering 减少重绘
- 降低移动端粒子数量和复杂度
- 使用 OffscreenCanvas（支持的浏览器）
- 暂停不可见标签页的动画

**控制参数示例**：
- 粒子数量：100-5000
- 速度：0.1-5.0
- 噪点强度：0-1
- 色相旋转：0-360deg
- 线条粗细：1-10px
- 透明度：0.1-1.0
- 帧率：30-60 FPS

**典型应用**：
- 创意工作室：展示技术和艺术能力
- 数字艺术平台：生成式 NFT、艺术创作工具
- 音乐可视化：实时响应音频的视觉效果
- 数据可视化：将数据映射为艺术图案
- 游戏背景：程序化生成游戏场景
- 冥想/放松应用：缓慢变化的抽象图案
- 品牌动态背景：独特的视觉识别

**最佳实践**：
- 提供 "暂停" 选项节省性能
- 允许用户保存喜欢的图案（seed 值）
- 提供预设参数组合快速切换
- 确保生成结果有一定重复性（使用 seed）
- 在生成过程显示进度指示
- 支持键盘快捷键（空格暂停、R 随机、S 保存）
- 遵守 prefers-reduced-motion 媒体查询


---

## English Version (en-US)

Design generative art style interfaces using algorithm-driven visual elements to create unique dynamic aesthetics.

**Core Visual Characteristics**: Algorithmically generated pattern backgrounds, procedural noise/particle effects, geometric line/curve animations, mathematical abstract forms, color cycling, real-time generative dynamic effects.

**Technical Implementation**: Use Canvas API or SVG for pattern drawing, Perlin noise for organic textures, particle systems for dynamic effects, recursive algorithms for fractal patterns, randomized parameters for uniqueness, requestAnimationFrame for smooth animation.

**Core Algorithms**:
- Perlin/Simplex noise: Organic flowing textures
- Particle systems: Particle trails and burst effects
- L-systems: Plant/fractal growth patterns
- Voronoi diagrams: Cellular division patterns
- Flow fields: Fluid dynamics simulation
- Fractal trees: Recursive fractal trees

**Color System**: Use algorithms to generate color schemes (HSL color space cycling), gradient mapping noise values to colors, dynamic hue rotation, customizable palettes (monochrome, complementary, analogous, triadic).

**Layout & Components**:
- Hero area: Fullscreen generative art background with minimal foreground content
- Control panel: Sliders to adjust parameters (speed, density, color, complexity)
- Thumbnail grid: Display different generation results
- Live preview: Instant updates on parameter changes
- Save/share: Export as image or share seed value

**Interaction Design**:
- Mouse movement: Influences particle flow direction or pattern deformation
- Click: Triggers new pattern generation or color change
- Scroll: Drives animation progress or parameter gradients
- Parameter sliders: Real-time adjustment of generation algorithm parameters
- Random button: Generate entirely new random pattern
- Reset button: Restore default parameters

**Performance Optimization**:
- Use Web Workers for complex calculations
- requestAnimationFrame instead of setInterval
- Canvas offscreen rendering to reduce repaints
- Reduce particle count and complexity on mobile
- Use OffscreenCanvas (supported browsers)
- Pause animations in invisible tabs

**Control Parameter Examples**:
- Particle count: 100-5000
- Speed: 0.1-5.0
- Noise intensity: 0-1
- Hue rotation: 0-360deg
- Line thickness: 1-10px
- Opacity: 0.1-1.0
- Frame rate: 30-60 FPS

**Typical Applications**:
- Creative studios: Showcase technical and artistic capabilities
- Digital art platforms: Generative NFTs, art creation tools
- Music visualization: Real-time audio-responsive visuals
- Data visualization: Map data to artistic patterns
- Game backgrounds: Procedurally generated game scenes
- Meditation/relaxation apps: Slowly changing abstract patterns
- Brand dynamic backgrounds: Unique visual identity

**Best Practices**:
- Provide "pause" option to save performance
- Allow users to save favorite patterns (seed values)
- Offer preset parameter combinations for quick switching
- Ensure reproducible generation results (use seed)
- Display progress indicator during generation
- Support keyboard shortcuts (space pause, R random, S save)
- Respect prefers-reduced-motion media query
