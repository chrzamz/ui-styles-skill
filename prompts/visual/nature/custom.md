# Custom Prompt

## 中文版本 (zh-CN)

# Nature Elements（自然元素视觉效果）家族完整设计指南

请使用 TailwindCSS 和原生 CSS 创建自然元素风格的界面，通过模拟极光、波浪、粒子、液体和烟雾等自然现象，实现流动、有机、飘渺的视觉效果。

## 一、Aurora（极光）设计规范

**核心理念**：流动渐变 + 水平移动 + 模糊融合


### 1.1 渐变带设计

\`\`\`css
.aurora-wave {
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(0, 255, 200, 0.4) 25%,
    rgba(100, 200, 255, 0.4) 50%,
    rgba(200, 100, 255, 0.4) 75%,
    transparent 100%
  );
  filter: blur(40px);
  animation: auroraFlow 20s ease-in-out infinite;
}

@keyframes auroraFlow {
  0%, 100% { transform: translateX(-50%) scaleY(1); opacity: 0.5; }
  50% { transform: translateX(50%) scaleY(1.2); opacity: 0.8; }
}
\`\`\`

### 1.2 关键设计要点

- **多色渐变**：使用 3-5 种颜色过渡（青色、蓝色、紫色、绿色）
- **模糊处理**：filter: blur(30px-50px) 创造柔和边缘
- **水平流动**：translateX(-50% → 50%) 模拟极光漂移
- **垂直拉伸**：scaleY(1 → 1.2) 增加动态感
- **透明度变化**：opacity: 0.4 → 0.8 模拟亮度波动

### 1.3 适用场景

- 页面顶部装饰
- 科幻主题背景
- 加载动画
- Hero section 氛围渲染

## 二、Wave（波浪）设计规范

**核心理念**：SVG 路径动画 + 贝塞尔曲线 + 多层叠加


### 2.1 SVG 波浪路径

\`\`\`html
<svg viewBox="0 0 1200 200" class="wave-svg">
  <path d="M0,100 Q300,50 600,100 T1200,100 V200 H0 Z" class="wave-path" />
</svg>
\`\`\`

\`\`\`css
.wave-svg {
  width: 100%;
  height: auto;
  position: absolute;
  bottom: 0;
}

.wave-path {
  fill: rgba(100, 200, 255, 0.3);
  animation: waveMove 8s ease-in-out infinite;
}

@keyframes waveMove {
  0%, 100% { d: path("M0,100 Q300,50 600,100 T1200,100 V200 H0 Z"); }
  50% { d: path("M0,100 Q300,150 600,100 T1200,100 V200 H0 Z"); }
}
\`\`\`

### 2.2 CSS clip-path 替代方案

\`\`\`css
.wave-css {
  background: linear-gradient(180deg, transparent 0%, rgba(100, 200, 255, 0.3) 100%);
  clip-path: polygon(
    0% 50%, 10% 40%, 20% 50%, 30% 45%, 40% 50%,
    50% 40%, 60% 50%, 70% 45%, 80% 50%, 90% 40%,
    100% 50%, 100% 100%, 0% 100%
  );
}
\`\`\`

### 2.3 关键设计要点

- **贝塞尔曲线**：Q (二次) 或 C (三次) 创造平滑波峰
- **多层波浪**：3 层不同透明度和速度
- **颜色选择**：蓝色系 (#64c8ff, #4ca3d8, #357abd)
- **动画节奏**：6-10s ease-in-out 模拟海浪节奏


### 2.4 适用场景

- 页面底部装饰
- 水主题界面
- 分隔区域
- 滚动触发动画

## 三、Particle（粒子系统）设计规范

**核心理念**：多粒子 + 随机运动 + 发光效果

### 3.1 粒子元素设计

\`\`\`css
.particle {
  width: 4px;
  height: 4px;
  background: rgba(100, 200, 255, 0.8);
  border-radius: 50%;
  box-shadow: 0 0 10px rgba(100, 200, 255, 0.8);
  position: absolute;
}

.particle-1 {
  top: 10%;
  left: 20%;
  animation: particleFloat 8s ease-in-out infinite;
}

@keyframes particleFloat {
  0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.8; }
  25% { transform: translate(50px, -50px) scale(1.2); opacity: 1; }
  50% { transform: translate(-30px, -80px) scale(0.8); opacity: 0.6; }
  75% { transform: translate(70px, -40px) scale(1.1); opacity: 0.9; }
}
\`\`\`

### 3.2 关键设计要点

- **小圆点**：4-6px，border-radius: 50%
- **发光效果**：box-shadow: 0 0 10px 同色
- **随机位置**：top/left 使用百分比分散
- **浮动动画**：translate + scale + opacity 组合
- **多种颜色**：蓝色、紫色、青色、橙色混合


### 3.3 批量生成技巧

\`\`\`javascript
// 动态生成 8-12 个粒子
for (let i = 0; i < 10; i++) {
  const particle = document.createElement('div');
  particle.className = 'particle';
  particle.style.top = (Math.random() * 100) + '%';
  particle.style.left = (Math.random() * 100) + '%';
  particle.style.animationDelay = (Math.random() * 5) + 's';
  particle.style.animationDuration = (6 + Math.random() * 8) + 's';
  container.appendChild(particle);
}
\`\`\`

### 3.4 适用场景

- 科技感背景
- 星空效果
- 魔法/能量视觉
- 装饰性动态元素

## 四、Liquid（液体流动）设计规范

**核心理念**：变形动画 + 径向渐变 + 模糊融合

### 4.1 液体 Blob 设计

\`\`\`css
.liquid-blob {
  width: 400px;
  height: 400px;
  background: radial-gradient(
    circle,
    rgba(255, 255, 255, 0.5) 0%,
    rgba(255, 255, 255, 0.2) 50%,
    transparent 100%
  );
  border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
  filter: blur(20px);
  animation: liquidMorph 10s ease-in-out infinite;
}

@keyframes liquidMorph {
  0%, 100% {
    border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
    transform: translate(0, 0) rotate(0deg) scale(1);
  }
  25% {
    border-radius: 60% 40% 50% 50% / 30% 60% 40% 70%;
    transform: translate(30px, -30px) rotate(90deg) scale(1.1);
  }
  50% {
    border-radius: 50% 50% 30% 70% / 50% 50% 50% 50%;
    transform: translate(-20px, 40px) rotate(180deg) scale(0.9);
  }
  75% {
    border-radius: 70% 30% 50% 50% / 60% 40% 60% 40%;
    transform: translate(40px, 20px) rotate(270deg) scale(1.05);
  }
}
\`\`\`

### 4.2 关键设计要点

- **复杂圆角**：8 个百分比值创造有机形状
- **径向渐变**：从中心到边缘透明
- **模糊融合**：filter: blur(20px-40px)
- **变形 + 旋转**：同时改变 border-radius、translate、rotate
- **双 Blob 叠加**：2-3 个不同速度的 blob 叠加

### 4.3 适用场景

- 流体背景
- 有机形态界面
- 动态装饰元素
- 现代感 Hero section

## 五、Smoke（烟雾效果）设计规范

**核心理念**：径向渐变 + 极致模糊 + 缓慢上升 + 逐渐消散

### 5.1 烟雾层设计

\`\`\`css
.smoke-layer {
  width: 300px;
  height: 400px;
  background: radial-gradient(
    ellipse at center,
    rgba(255, 255, 255, 0.3) 0%,
    rgba(200, 200, 255, 0.15) 30%,
    rgba(150, 150, 200, 0.08) 60%,
    transparent 100%
  );
  border-radius: 50%;
  filter: blur(40px);
  position: absolute;
  opacity: 0.6;
  animation: smokeRise 15s ease-in-out infinite;
}

@keyframes smokeRise {
  0% {
    transform: translate(0, 0) scale(1) rotate(0deg);
    opacity: 0.4;
  }
  25% {
    transform: translate(-30px, -100px) scale(1.2) rotate(45deg);
    opacity: 0.7;
  }
  50% {
    transform: translate(20px, -200px) scale(1.4) rotate(90deg);
    opacity: 0.5;
  }
  75% {
    transform: translate(-40px, -300px) scale(1.6) rotate(135deg);
    opacity: 0.3;
  }
  100% {
    transform: translate(0, -400px) scale(1.8) rotate(180deg);
    opacity: 0;
  }
}
\`\`\`

### 5.2 关键设计要点

- **椭圆形状**：width/height 不同值 + border-radius: 50%
- **极致模糊**：filter: blur(40px-60px)
- **上升动画**：translateY(-400px) 模拟上升
- **缩放变化**：scale(1 → 1.8) 模拟扩散
- **旋转**：rotate(0 → 180deg) 增加自然感
- **透明度消散**：opacity: 0.6 → 0
- **多层烟雾**：4 层不同速度和延迟

### 5.3 颜色变体

\`\`\`css
/* 白色烟雾 */
background: radial-gradient(ellipse, rgba(255, 255, 255, 0.3) 0%, transparent 70%);

/* 彩色烟雾（紫色）*/
background: radial-gradient(ellipse, rgba(200, 150, 255, 0.25) 0%, transparent 70%);

/* 彩色烟雾（青色）*/
background: radial-gradient(ellipse, rgba(100, 255, 200, 0.3) 0%, transparent 70%);
\`\`\`

### 5.4 适用场景

- 神秘氛围渲染
- 背景装饰
- 魔法效果
- 飘渺主题界面

## 六、配色方案

### 6.1 极光色系

\`\`\`css
--aurora-cyan: #00ffc8;
--aurora-blue: #64c8ff;
--aurora-purple: #c864ff;
--aurora-green: #00ff80;
\`\`\`

### 6.2 海洋色系（波浪）

\`\`\`css
--ocean-light: #64c8ff;
--ocean-medium: #4ca3d8;
--ocean-deep: #357abd;
--ocean-dark: #1e4d7a;
\`\`\`

### 6.3 粒子色系

\`\`\`css
--particle-blue: rgba(100, 200, 255, 0.8);
--particle-purple: rgba(200, 100, 255, 0.8);
--particle-cyan: rgba(100, 255, 200, 0.8);
--particle-orange: rgba(255, 150, 100, 0.8);
\`\`\`

### 6.4 液体色系

\`\`\`css
--liquid-primary: rgba(102, 126, 234, 0.5);
--liquid-secondary: rgba(118, 75, 162, 0.5);
--liquid-highlight: rgba(255, 255, 255, 0.5);
\`\`\`

### 6.5 烟雾色系

\`\`\`css
--smoke-white: rgba(255, 255, 255, 0.3);
--smoke-blue: rgba(200, 200, 255, 0.15);
--smoke-gray: rgba(150, 150, 200, 0.08);
\`\`\`

## 七、关键 CSS 技术详解

### 7.1 filter: blur() 使用规范

\`\`\`css
/* 轻微模糊（粒子）*/
filter: blur(10px);

/* 中度模糊（液体）*/
filter: blur(20px);

/* 强模糊（极光、烟雾）*/
filter: blur(40px);

/* 极致模糊（大面积烟雾）*/
filter: blur(60px);
\`\`\`

**性能优化**：
- 避免对大量元素同时使用高 blur 值
- 使用 will-change: filter; 提升性能
- 考虑使用 transform: translateZ(0); 启用硬件加速

### 7.2 border-radius 变形技术

\`\`\`css
/* 基础形态 */
border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;

/* 解析：前 4 个值控制水平半径，后 4 个值控制垂直半径 */
/* 水平：左上 40%，右上 60%，右下 70%，左下 30% */
/* 垂直：左上 40%，右上 50%，右下 60%，左下 50% */

/* 动态变化示例 */
@keyframes morph {
  0% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; }
  50% { border-radius: 60% 40% 50% 50% / 30% 60% 40% 70%; }
  100% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; }
}
\`\`\`

### 7.3 SVG 路径动画

\`\`\`html
<svg viewBox="0 0 1200 200">
  <path d="M0,100 Q300,50 600,100 T1200,100 V200 H0 Z" />
</svg>
\`\`\`

**路径命令解析**：
- M0,100：移动到起点 (0, 100)
- Q300,50 600,100：二次贝塞尔曲线，控制点 (300,50)，终点 (600,100)
- T1200,100：平滑二次贝塞尔，终点 (1200,100)
- V200：垂直线到 y=200
- H0：水平线到 x=0
- Z：闭合路径

### 7.4 动画时序控制

\`\`\`css
/* 基础延迟 */
animation-delay: 2s;

/* 随机延迟（JavaScript）*/
element.style.animationDelay = \`\${Math.random() * 5}s\`;

/* 错开动画（多元素）*/
.particle:nth-child(1) { animation-delay: 0s; }
.particle:nth-child(2) { animation-delay: 1s; }
.particle:nth-child(3) { animation-delay: 2s; }

/* 或使用 calc */
.particle:nth-child(n) {
  animation-delay: calc(var(--n) * 0.5s);
}
\`\`\`

## 八、组合使用示例

### 8.1 完整自然主题 Hero Section

\`\`\`html
<div class="nature-hero">
  <!-- 极光背景 -->
  <div class="aurora-layer"></div>
  
  <!-- 粒子系统 -->
  <div class="particle-container">
    <div class="particle"></div>
    <!-- 8-12 个粒子 -->
  </div>
  
  <!-- 液体装饰 -->
  <div class="liquid-blob"></div>
  
  <!-- 内容 -->
  <div class="hero-content">
    <h1>Embrace Nature</h1>
    <p>Experience the beauty of natural elements</p>
  </div>
  
  <!-- 波浪底部 -->
  <svg class="wave-bottom">
    <path d="M0,100 Q300,50 600,100 T1200,100 V200 H0 Z" />
  </svg>
</div>
\`\`\`

### 8.2 样式整合

\`\`\`css
.nature-hero {
  min-height: 100vh;
  background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.aurora-layer {
  position: absolute;
  top: 0;
  width: 200%;
  height: 200px;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(0, 255, 200, 0.3) 25%,
    rgba(100, 200, 255, 0.3) 50%,
    rgba(200, 100, 255, 0.3) 75%,
    transparent 100%
  );
  filter: blur(40px);
  animation: auroraFlow 20s ease-in-out infinite;
}

.particle-container {
  position: absolute;
  width: 100%;
  height: 100%;
}

.liquid-blob {
  position: absolute;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
  border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
  filter: blur(30px);
  top: 50%;
  right: 10%;
  animation: liquidMorph 12s ease-in-out infinite;
}

.hero-content {
  position: relative;
  z-index: 10;
  text-align: center;
  color: white;
}

.wave-bottom {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 150px;
}
\`\`\`

## 九、性能优化建议

### 9.1 减少 blur 使用

- 限制同时使用 blur 的元素数量（建议 ≤ 5 个）
- 使用 will-change: filter; 提升性能
- 考虑在低端设备禁用 blur

### 9.2 动画优化

\`\`\`css
/* 使用 transform 代替 top/left */
/* ❌ 不推荐 */
@keyframes bad {
  to { top: 100px; left: 200px; }
}

/* ✅ 推荐 */
@keyframes good {
  to { transform: translate(200px, 100px); }
}

/* 添加硬件加速 */
.optimized {
  transform: translateZ(0);
  will-change: transform;
}
\`\`\`

### 9.3 减少重绘

- 避免频繁改变 border-radius
- 使用 opacity 而非 visibility
- 使用 transform: scale() 而非 width/height

## 十、响应式设计

### 10.1 移动端适配

\`\`\`css
@media (max-width: 768px) {
  /* 减少粒子数量 */
  .particle:nth-child(n+5) { display: none; }
  
  /* 缩小元素尺寸 */
  .liquid-blob { width: 250px; height: 250px; }
  .smoke-layer { width: 200px; height: 300px; }
  
  /* 降低模糊强度 */
  .aurora-layer { filter: blur(25px); }
  .liquid-blob { filter: blur(15px); }
  
  /* 减慢动画速度节省性能 */
  .particle { animation-duration: 12s !important; }
}

@media (prefers-reduced-motion: reduce) {
  /* 尊重用户偏好设置 */
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
\`\`\`

### 10.2 平板适配

\`\`\`css
@media (min-width: 769px) and (max-width: 1024px) {
  .liquid-blob { width: 300px; height: 300px; }
  .smoke-layer { width: 250px; height: 350px; }
  .particle-container .particle:nth-child(n+8) { display: none; }
}
\`\`\`

## 十一、浏览器兼容性

### 11.1 必要的前缀

\`\`\`css
.nature-element {
  -webkit-filter: blur(20px);
  filter: blur(20px);
  
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}
\`\`\`

### 11.2 降级方案

\`\`\`css
/* 不支持 blur 的浏览器 */
@supports not (filter: blur(10px)) {
  .liquid-blob {
    opacity: 0.5;
    /* 使用静态渐变代替 */
  }
}
\`\`\`

## 十二、重要提示

1. **性能优先**：限制同时使用 blur 的元素数量，建议不超过 5 个
2. **移动端优化**：在移动设备上减少粒子数量、降低模糊强度
3. **硬件加速**：使用 transform: translateZ(0) 和 will-change 提升性能
4. **动画错开**：通过 animation-delay 让多个元素错开，避免同时启动
5. **颜色和谐**：使用蓝色、青色、紫色系保持自然感
6. **SVG 优先**：波浪效果优先使用 SVG path，更平滑且性能更好
7. **多层叠加**：通过 2-4 层不同透明度的元素叠加增加深度感
8. **尊重用户偏好**：使用 prefers-reduced-motion 媒体查询
9. **渐进增强**：在不支持 filter 的浏览器提供降级方案
10. **测试实际效果**：在真实设备上测试性能，根据需要调整参数


---

## English Version (en-US)

# Nature Elements Visual Effects Family - Complete Design Guide

Please create nature-inspired interfaces using TailwindCSS and native CSS, simulating natural phenomena like aurora, waves, particles, liquid, and smoke to achieve flowing, organic, ethereal visual effects.

## I. Aurora Design Specifications

**Core Concept**: Flowing gradients + Horizontal movement + Blur blending

### 1.1 Gradient Band Design

\`\`\`css
.aurora-wave {
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(0, 255, 200, 0.4) 25%,
    rgba(100, 200, 255, 0.4) 50%,
    rgba(200, 100, 255, 0.4) 75%,
    transparent 100%
  );
  filter: blur(40px);
  animation: auroraFlow 20s ease-in-out infinite;
}

@keyframes auroraFlow {
  0%, 100% { transform: translateX(-50%) scaleY(1); opacity: 0.5; }
  50% { transform: translateX(50%) scaleY(1.2); opacity: 0.8; }
}
\`\`\`

### 1.2 Key Design Points

- **Multi-color gradient**: Use 3-5 color transitions (cyan, blue, purple, green)
- **Blur processing**: filter: blur(30px-50px) creates soft edges
- **Horizontal flow**: translateX(-50% → 50%) simulates aurora drift
- **Vertical stretch**: scaleY(1 → 1.2) adds dynamic feel
- **Opacity variation**: opacity: 0.4 → 0.8 simulates brightness fluctuation

### 1.3 Use Cases

- Page header decoration, sci-fi themed backgrounds, loading animations, Hero section atmosphere

## II. Wave Design Specifications

**Core Concept**: SVG path animation + Bézier curves + Multi-layer overlay

### 2.1 SVG Wave Path

\`\`\`html
<svg viewBox="0 0 1200 200" class="wave-svg">
  <path d="M0,100 Q300,50 600,100 T1200,100 V200 H0 Z" class="wave-path" />
</svg>
\`\`\`

### 2.2 Key Points

- **Bézier curves**: Q (quadratic) or C (cubic) creates smooth peaks
- **Multi-layer**: 3 layers with different opacity and speeds
- **Color palette**: Blue tones (#64c8ff, #4ca3d8, #357abd)
- **Animation rhythm**: 6-10s ease-in-out mimics wave rhythm

## III. Particle System Specifications

**Core Concept**: Multi-particles + Random motion + Glow effect

### 3.1 Particle Element Design

\`\`\`css
.particle {
  width: 4px;
  height: 4px;
  background: rgba(100, 200, 255, 0.8);
  border-radius: 50%;
  box-shadow: 0 0 10px rgba(100, 200, 255, 0.8);
  animation: particleFloat 8s ease-in-out infinite;
}

@keyframes particleFloat {
  0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.8; }
  25% { transform: translate(50px, -50px) scale(1.2); opacity: 1; }
  50% { transform: translate(-30px, -80px) scale(0.8); opacity: 0.6; }
  75% { transform: translate(70px, -40px) scale(1.1); opacity: 0.9; }
}
\`\`\`

### 3.2 Key Points

- Small dots: 4-6px with border-radius: 50%
- Glow: box-shadow matching color
- Random positions using percentages
- Floating animation with translate + scale + opacity


## IV. Liquid Motion Specifications

**Core Concept**: Morphing animation + Radial gradient + Blur blending

### 4.1 Liquid Blob Design

\`\`\`css
.liquid-blob {
  width: 400px;
  height: 400px;
  background: radial-gradient(
    circle,
    rgba(255, 255, 255, 0.5) 0%,
    rgba(255, 255, 255, 0.2) 50%,
    transparent 100%
  );
  border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
  filter: blur(20px);
  animation: liquidMorph 10s ease-in-out infinite;
}

@keyframes liquidMorph {
  0%, 100% {
    border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
    transform: translate(0, 0) rotate(0deg) scale(1);
  }
  25% {
    border-radius: 60% 40% 50% 50% / 30% 60% 40% 70%;
    transform: translate(30px, -30px) rotate(90deg) scale(1.1);
  }
  50% {
    border-radius: 50% 50% 30% 70% / 50% 50% 50% 50%;
    transform: translate(-20px, 40px) rotate(180deg) scale(0.9);
  }
  75% {
    border-radius: 70% 30% 50% 50% / 60% 40% 60% 40%;
    transform: translate(40px, 20px) rotate(270deg) scale(1.05);
  }
}
\`\`\`

### 4.2 Key Points

- Complex border-radius: 8 percentage values create organic shapes
- Radial gradient: Center to edge transparency
- Blur blending: filter: blur(20px-40px)
- Morph + rotate: Simultaneously change border-radius, translate, rotate
- Dual blob overlay: 2-3 blobs with different speeds

## V. Smoke Effect Specifications

**Core Concept**: Radial gradient + Extreme blur + Slow rise + Gradual dissipation

### 5.1 Smoke Layer Design

\`\`\`css
.smoke-layer {
  width: 300px;
  height: 400px;
  background: radial-gradient(
    ellipse at center,
    rgba(255, 255, 255, 0.3) 0%,
    rgba(200, 200, 255, 0.15) 30%,
    rgba(150, 150, 200, 0.08) 60%,
    transparent 100%
  );
  border-radius: 50%;
  filter: blur(40px);
  animation: smokeRise 15s ease-in-out infinite;
}

@keyframes smokeRise {
  0% { transform: translate(0, 0) scale(1) rotate(0deg); opacity: 0.4; }
  25% { transform: translate(-30px, -100px) scale(1.2) rotate(45deg); opacity: 0.7; }
  50% { transform: translate(20px, -200px) scale(1.4) rotate(90deg); opacity: 0.5; }
  75% { transform: translate(-40px, -300px) scale(1.6) rotate(135deg); opacity: 0.3; }
  100% { transform: translate(0, -400px) scale(1.8) rotate(180deg); opacity: 0; }
}
\`\`\`

### 5.2 Key Points

- Ellipse shape: Different width/height + border-radius: 50%
- Extreme blur: filter: blur(40px-60px)
- Rising animation: translateY(-400px) simulates ascent
- Scale change: scale(1 → 1.8) simulates diffusion
- Rotation: rotate(0 → 180deg) adds natural feel
- Opacity fade: opacity: 0.6 → 0
- Multi-layer: 4 layers with different speeds and delays

## VI. Color Schemes

### Aurora Colors
\`\`\`css
--aurora-cyan: #00ffc8;
--aurora-blue: #64c8ff;
--aurora-purple: #c864ff;
--aurora-green: #00ff80;
\`\`\`

### Ocean Colors (Waves)
\`\`\`css
--ocean-light: #64c8ff;
--ocean-medium: #4ca3d8;
--ocean-deep: #357abd;
--ocean-dark: #1e4d7a;
\`\`\`

### Particle Colors
\`\`\`css
--particle-blue: rgba(100, 200, 255, 0.8);
--particle-purple: rgba(200, 100, 255, 0.8);
--particle-cyan: rgba(100, 255, 200, 0.8);
--particle-orange: rgba(255, 150, 100, 0.8);
\`\`\`

## VII. Key CSS Techniques


### 7.1 filter: blur() Usage

\`\`\`css
filter: blur(10px);  /* Light blur (particles) */
filter: blur(20px);  /* Medium blur (liquid) */
filter: blur(40px);  /* Strong blur (aurora, smoke) */
filter: blur(60px);  /* Extreme blur (large smoke areas) */
\`\`\`

**Performance**: Use will-change: filter; and transform: translateZ(0); for optimization

### 7.2 border-radius Morphing

\`\`\`css
/* Basic form */
border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;

/* Explanation: First 4 values control horizontal radius, last 4 control vertical radius */
/* Horizontal: top-left 40%, top-right 60%, bottom-right 70%, bottom-left 30% */
/* Vertical: top-left 40%, top-right 50%, bottom-right 60%, bottom-left 50% */
\`\`\`

### 7.3 SVG Path Animation

\`\`\`html
<svg viewBox="0 0 1200 200">
  <path d="M0,100 Q300,50 600,100 T1200,100 V200 H0 Z" />
</svg>
\`\`\`

**Path Commands**:
- M0,100: Move to start point
- Q300,50 600,100: Quadratic Bézier curve
- T1200,100: Smooth quadratic Bézier
- V200: Vertical line to y=200
- H0: Horizontal line to x=0
- Z: Close path

## VIII. Performance Optimization

### 8.1 Reduce blur Usage

- Limit simultaneous blur elements (≤ 5 recommended)
- Use will-change: filter; for better performance
- Consider disabling blur on low-end devices

### 8.2 Animation Optimization

\`\`\`css
/* Use transform instead of top/left */
/* ❌ Not recommended */
@keyframes bad { to { top: 100px; left: 200px; } }

/* ✅ Recommended */
@keyframes good { to { transform: translate(200px, 100px); } }

/* Add hardware acceleration */
.optimized {
  transform: translateZ(0);
  will-change: transform;
}
\`\`\`

## IX. Responsive Design

### 9.1 Mobile Adaptation

\`\`\`css
@media (max-width: 768px) {
  .particle:nth-child(n+5) { display: none; }  /* Reduce particles */
  .liquid-blob { width: 250px; height: 250px; }  /* Smaller size */
  .aurora-layer { filter: blur(25px); }  /* Reduce blur intensity */
  .particle { animation-duration: 12s !important; }  /* Slower animations */
}

@media (prefers-reduced-motion: reduce) {
  /* Respect user preferences */
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
\`\`\`

## X. Important Notes

1. **Performance first**: Limit simultaneous blur elements (≤ 5 recommended)
2. **Mobile optimization**: Reduce particle count and blur intensity on mobile
3. **Hardware acceleration**: Use transform: translateZ(0) and will-change
4. **Stagger animations**: Use animation-delay to prevent simultaneous starts
5. **Color harmony**: Use blue, cyan, purple tones for natural feel
6. **SVG priority**: Use SVG paths for waves - smoother and better performance
7. **Multi-layer**: Stack 2-4 layers with different opacity for depth
8. **Respect preferences**: Use prefers-reduced-motion media query
9. **Progressive enhancement**: Provide fallbacks for unsupported browsers
10. **Test real devices**: Test performance on actual devices and adjust accordingly
