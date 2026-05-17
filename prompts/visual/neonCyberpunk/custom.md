# Neon Cyberpunk (霓虹赛博朋克) - Custom Prompt

## 中文版本 (zh-CN)

### 设计概述
生成 **Neon Cyberpunk（霓虹赛博朋克）** 风格的界面设计。这是一种融合赛博朋克美学与霓虹灯光的未来主义风格，通过深黑背景、高对比度霓虹色彩、终端界面和矩阵雨效果，打造科幻电影般的数字世界体验。

## 核心设计要求

### 1. 深色暗黑背景系统

**背景原则**：
- 使用接近纯黑的渐层背景
- 可选的细微杂讯和扫描线
- 营造深邃的赛博空间氛围

**完整 CSS 实现**：
```css
/* Cyberpunk 深色背景 */
.cyber-bg {
  background: radial-gradient(
    circle at center,
    #0a0f14 0%,
    #050810 45%,
    #000000 100%
  );
  min-height: 100vh;
  color: #e5e7eb;
  position: relative;
  overflow: hidden;
}

/* 杂讯纹理覆盖层 */
.cyber-noise {
  position: relative;
}

.cyber-noise::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: 0.08;
  background-image:
    repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0, 255, 65, 0.03) 2px,
      rgba(0, 255, 65, 0.03) 4px
    );
  mix-blend-mode: overlay;
  z-index: 1;
}
```

### 2. 霓虹色彩系统

**色彩原则**：
- 使用高饱和度霓虹色
- 每种颜色必须具备多层发光效果
- 文字和边框需要光晕

**完整色彩方案**：
```css
:root {
  /* 基础暗色 */
  --cyber-black: #000000;
  --cyber-dark-900: #0a0a0a;
  --cyber-dark-800: #0f0f0f;
  --cyber-dark-700: #1a1a1a;

  /* 霓虹色 */
  --cyber-neon-green: #00ff41;
  --cyber-neon-cyan: #00ffff;
  --cyber-neon-purple: #b967ff;
  --cyber-neon-magenta: #ff00ff;
  --cyber-neon-pink: #ff1493;
  --cyber-neon-orange: #ff6600;
  --cyber-neon-yellow: #ffff00;

  /* 文字颜色 */
  --cyber-text-primary: #e5e7eb;
  --cyber-text-secondary: #9ca3af;
  --cyber-text-muted: #6b7280;

  /* 霓虹 RGB 值（用于 rgba）*/
  --cyber-green-rgb: 0, 255, 65;
  --cyber-cyan-rgb: 0, 255, 255;
  --cyber-purple-rgb: 185, 103, 255;
  --cyber-magenta-rgb: 255, 0, 255;
}

/* 霓虹绿文字发光 */
.cyber-text-neon-green {
  color: var(--cyber-neon-green);
  text-shadow:
    0 0 5px rgba(var(--cyber-green-rgb), 0.8),
    0 0 10px rgba(var(--cyber-green-rgb), 0.6),
    0 0 20px rgba(var(--cyber-green-rgb), 0.4),
    0 0 40px rgba(var(--cyber-green-rgb), 0.2);
}
```

### 3. 终端界面风格

**终端原则**：
- 使用等宽字体（Courier New、Monaco）
- 模拟命令行输入效果
- 包含闪烁光标动画

**完整终端组件**：
```css
/* 终端容器 */
.cyber-terminal {
  background: rgba(10, 15, 20, 0.85);
  border: 1px solid rgba(0, 255, 65, 0.4);
  border-radius: 8px;
  padding: 1.5rem;
  font-family: 'Courier New', Monaco, monospace;
  font-size: 14px;
  line-height: 1.6;
  color: var(--cyber-neon-green);
  backdrop-filter: blur(10px);
  box-shadow:
    0 0 20px rgba(var(--cyber-green-rgb), 0.15),
    inset 0 0 20px rgba(0, 0, 0, 0.3);
}

/* 终端标题栏 */
.cyber-terminal-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 1rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid rgba(0, 255, 65, 0.2);
}

/* 终端窗口按钮 */
.cyber-terminal-dots {
  display: flex;
  gap: 6px;
}

.cyber-terminal-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
}

.cyber-terminal-dot.red {
  background: rgba(255, 0, 0, 0.6);
  box-shadow: 0 0 8px rgba(255, 0, 0, 0.4);
}

/* 终端内容 */
.cyber-terminal-content {
  color: var(--cyber-neon-green);
}

.cyber-terminal-line {
  margin-bottom: 0.5rem;
}

.cyber-terminal-prompt::before {
  content: '$ ';
  color: var(--cyber-neon-cyan);
  font-weight: bold;
}

/* 闪烁光标 */
.cyber-cursor {
  display: inline-block;
  width: 8px;
  height: 16px;
  background: var(--cyber-neon-green);
  margin-left: 2px;
  animation: cyber-blink 1s step-end infinite;
}

@keyframes cyber-blink {
  0%, 50% { opacity: 1; }
  50.01%, 100% { opacity: 0; }
}
```

### 4. 数据卡片组件

**卡片原则**：
- 半透明背景配合毛玻璃效果
- 霓虹边框和内阴影
- 悬停时增强发光

**完整卡片组件**：
```css
/* 基础卡片 */
.cyber-card {
  background: rgba(10, 15, 20, 0.6);
  border: 1px solid rgba(0, 255, 255, 0.4);
  border-radius: 12px;
  padding: 1.5rem;
  backdrop-filter: blur(12px);
  box-shadow:
    0 0 20px rgba(var(--cyber-cyan-rgb), 0.1),
    inset 0 0 20px rgba(0, 0, 0, 0.2);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.cyber-card:hover {
  border-color: rgba(0, 255, 255, 0.6);
  box-shadow:
    0 0 30px rgba(var(--cyber-cyan-rgb), 0.3),
    inset 0 0 30px rgba(0, 0, 0, 0.3);
  transform: translateY(-2px);
}

/* 卡片顶部装饰条 */
.cyber-card-accent {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(
    90deg,
    transparent,
    var(--cyber-neon-cyan),
    transparent
  );
  box-shadow: 0 0 10px rgba(var(--cyber-cyan-rgb), 0.6);
}

/* 卡片标题 */
.cyber-card-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--cyber-neon-cyan);
  margin-bottom: 0.75rem;
  text-shadow:
    0 0 5px rgba(var(--cyber-cyan-rgb), 0.6),
    0 0 10px rgba(var(--cyber-cyan-rgb), 0.3);
}

/* 卡片数据 */
.cyber-card-stat {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
  font-family: 'Courier New', monospace;
}

.cyber-card-label {
  color: var(--cyber-text-secondary);
  font-size: 0.875rem;
}

.cyber-card-value {
  color: var(--cyber-neon-green);
  font-size: 1.125rem;
  font-weight: 600;
  text-shadow: 0 0 8px rgba(var(--cyber-green-rgb), 0.5);
}
```

### 5. LED 指示灯效果

**LED 原则**：
- 圆形或方形发光点
- 脉动呼吸动画
- 不同状态对应不同颜色

**完整 LED 组件**：
```css
/* LED 容器 */
.cyber-led-group {
  display: flex;
  gap: 12px;
  align-items: center;
}

/* 基础 LED */
.cyber-led {
  position: relative;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--cyber-neon-green);
  box-shadow:
    0 0 10px rgba(var(--cyber-green-rgb), 0.8),
    0 0 20px rgba(var(--cyber-green-rgb), 0.4),
    inset 0 0 5px rgba(255, 255, 255, 0.3);
  animation: cyber-pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

/* LED 状态变体 */
.cyber-led.red {
  background: #ff0000;
  box-shadow:
    0 0 10px rgba(255, 0, 0, 0.8),
    0 0 20px rgba(255, 0, 0, 0.4),
    inset 0 0 5px rgba(255, 255, 255, 0.3);
}

.cyber-led.cyan {
  background: var(--cyber-neon-cyan);
  box-shadow:
    0 0 10px rgba(var(--cyber-cyan-rgb), 0.8),
    0 0 20px rgba(var(--cyber-cyan-rgb), 0.4),
    inset 0 0 5px rgba(255, 255, 255, 0.3);
}

.cyber-led.purple {
  background: var(--cyber-neon-purple);
  box-shadow:
    0 0 10px rgba(var(--cyber-purple-rgb), 0.8),
    0 0 20px rgba(var(--cyber-purple-rgb), 0.4),
    inset 0 0 5px rgba(255, 255, 255, 0.3);
}

/* LED 脉动动画 */
@keyframes cyber-pulse {
  0%, 100% {
    opacity: 1;
    transform: scale(1);
  }
  50% {
    opacity: 0.7;
    transform: scale(0.95);
  }
}
```

### 6. 霓虹按钮组件

**按钮原则**：
- 半透明背景
- 霓虹边框和文字
- 悬停时增强发光和颜色变化

**完整按钮组件**：
```css
/* 基础按钮 */
.cyber-button {
  position: relative;
  padding: 0.75rem 2rem;
  font-family: 'Courier New', monospace;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--cyber-neon-cyan);
  background: rgba(10, 15, 20, 0.6);
  border: 2px solid var(--cyber-neon-cyan);
  border-radius: 4px;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow:
    0 0 15px rgba(var(--cyber-cyan-rgb), 0.2),
    inset 0 0 15px rgba(0, 0, 0, 0.2);
  text-shadow: 0 0 8px rgba(var(--cyber-cyan-rgb), 0.6);
}

.cyber-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(var(--cyber-cyan-rgb), 0.3),
    transparent
  );
  transition: left 0.5s;
}

.cyber-button:hover {
  color: #000000;
  background: var(--cyber-neon-cyan);
  box-shadow:
    0 0 30px rgba(var(--cyber-cyan-rgb), 0.6),
    inset 0 0 20px rgba(255, 255, 255, 0.1);
  text-shadow: none;
}

.cyber-button:hover::before {
  left: 100%;
}

.cyber-button:active {
  transform: scale(0.98);
  box-shadow:
    0 0 20px rgba(var(--cyber-cyan-rgb), 0.4),
    inset 0 0 15px rgba(0, 0, 0, 0.3);
}

/* 按钮颜色变体 */
.cyber-button.green {
  color: var(--cyber-neon-green);
  border-color: var(--cyber-neon-green);
  box-shadow:
    0 0 15px rgba(var(--cyber-green-rgb), 0.2),
    inset 0 0 15px rgba(0, 0, 0, 0.2);
  text-shadow: 0 0 8px rgba(var(--cyber-green-rgb), 0.6);
}

.cyber-button.green:hover {
  background: var(--cyber-neon-green);
  box-shadow:
    0 0 30px rgba(var(--cyber-green-rgb), 0.6),
    inset 0 0 20px rgba(255, 255, 255, 0.1);
}
```

### 7. 矩阵雨动画效果

**矩阵雨原则**：
- 垂直落下的字符流
- 渐变透明度
- 随机速度和密度

**完整矩阵雨实现**：
```css
/* 矩阵雨容器 */
.cyber-matrix-rain {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  overflow: hidden;
  z-index: 0;
}

/* 矩阵字符列 */
.cyber-matrix-column {
  position: absolute;
  top: -100%;
  font-family: 'Courier New', monospace;
  font-size: 16px;
  line-height: 1.2;
  color: var(--cyber-neon-green);
  text-shadow:
    0 0 5px rgba(var(--cyber-green-rgb), 0.8),
    0 0 10px rgba(var(--cyber-green-rgb), 0.4);
  opacity: 0.7;
  animation: cyber-rain-fall linear infinite;
}

@keyframes cyber-rain-fall {
  0% {
    top: -100%;
    opacity: 0;
  }
  10% {
    opacity: 0.7;
  }
  90% {
    opacity: 0.7;
  }
  100% {
    top: 100%;
    opacity: 0;
  }
}

/* JavaScript 初始化提示 */
/*
  使用 JavaScript 创建多个 .cyber-matrix-column 元素
  每列设置不同的 left 值（0-100%）
  每列设置不同的 animation-duration（4s-8s）
  每列设置不同的 animation-delay（0-2s）
  每列填充随机字符（可用字符：01ABCDEFGHIJKLMNOPQRSTUVWXYZ）
*/
```

### 8. 数据可视化元素

**数据图表原则**：
- 使用霓虹色线条和点
- 动态数据流动效果
- 发光网格背景

**完整数据图表**：
```css
/* 数据图表容器 */
.cyber-chart {
  background: rgba(10, 15, 20, 0.8);
  border: 1px solid rgba(0, 255, 255, 0.3);
  border-radius: 8px;
  padding: 1.5rem;
  backdrop-filter: blur(10px);
  box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.3);
}

/* 数据点 */
.cyber-data-point {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--cyber-neon-cyan);
  box-shadow:
    0 0 10px rgba(var(--cyber-cyan-rgb), 0.8),
    0 0 20px rgba(var(--cyber-cyan-rgb), 0.4);
  animation: cyber-data-pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

/* 数据流动线 */
.cyber-data-line {
  stroke: var(--cyber-neon-green);
  stroke-width: 2;
  fill: none;
  filter: drop-shadow(0 0 5px rgba(var(--cyber-green-rgb), 0.6));
  animation: cyber-line-draw 3s ease-in-out infinite;
}

@keyframes cyber-data-pulse {
  0%, 100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.5);
    opacity: 0.5;
  }
}

@keyframes cyber-line-draw {
  0% {
    stroke-dashoffset: 1000;
  }
  100% {
    stroke-dashoffset: 0;
  }
}
```

### 9. 响应式设计考量

**移动端优化**：
```css
/* 移动端调整 */
@media (max-width: 768px) {
  .cyber-bg {
    /* 减少背景复杂度 */
    background: #000000;
  }

  .cyber-noise::before {
    /* 移除杂讯层以提升性能 */
    display: none;
  }

  .cyber-card,
  .cyber-terminal,
  .cyber-button {
    /* 减少发光强度 */
    box-shadow:
      0 0 10px rgba(var(--cyber-cyan-rgb), 0.15),
      inset 0 0 10px rgba(0, 0, 0, 0.2);
  }

  .cyber-matrix-rain {
    /* 移动端隐藏矩阵雨 */
    display: none;
  }

  .cyber-text-neon-green,
  .cyber-card-title,
  .cyber-card-value {
    /* 减少文字发光层数 */
    text-shadow:
      0 0 5px rgba(var(--cyber-green-rgb), 0.6),
      0 0 10px rgba(var(--cyber-green-rgb), 0.3);
  }
}
```

### 10. 动画性能优化

**GPU 加速**：
```css
/* 对频繁动画的元素启用 GPU 加速 */
.cyber-card,
.cyber-button,
.cyber-led,
.cyber-matrix-column {
  will-change: transform, opacity;
  transform: translateZ(0);
  backface-visibility: hidden;
}

/* 减少重绘范围 */
.cyber-terminal,
.cyber-card {
  contain: layout style paint;
}
```

**减少动画偏好**：
```css
/* 尊重用户的减少动画偏好 */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }

  .cyber-matrix-rain,
  .cyber-cursor {
    animation: none;
  }

  .cyber-led {
    animation: none;
    opacity: 1;
  }
}
```

## 重要注意事项

1. **必须使用深色暗黑背景**：背景必须接近纯黑（#000000 - #1a1a1a），以确保与霓虹色的高对比度
2. **多层发光效果**：所有霓虹元素必须使用多层 box-shadow 或 text-shadow 实现发光
3. **等宽字体**：终端和数据展示必须使用等宽字体（Courier New、Monaco）
4. **动画节奏**：所有动画保持统一节奏（2-8 秒范围内）
5. **半透明覆盖**：使用 rgba() 和 backdrop-filter 实现毛玻璃效果
6. **边框发光**：边框需要同时具备颜色和内外发光阴影
7. **响应式处理**：移动端减少发光强度和动画复杂度

## 避免事项

❌ **不要使用浅色背景**：避免使用任何亮于 #2a2a2a 的背景色
❌ **不要使用低饱和度颜色**：霓虹色必须是高饱和度纯色
❌ **不要省略发光效果**：所有霓虹元素必须具备 text-shadow 或 box-shadow
❌ **不要使用衬线字体**：终端和数据必须使用等宽字体
❌ **不要过度动画**：避免同时出现过多快速动画，保持节奏统一
❌ **不要使用纯色填充**：按钮和卡片应使用半透明背景而非纯色
❌ **不要忽略 webkit 前缀**：backdrop-filter 需要 -webkit- 前缀以支持 Safari

## 补充实现技巧

**性能优化**：
- 对动画元素使用 `will-change: transform, opacity` 以启用 GPU 加速
- 限制屏幕上同时存在的发光效果数量（最多 10-15 个发光元素）
- 考虑使用媒体查询在低端设备上减少动画复杂度

**浏览器兼容性**：
- 始终为 rgba() 和 hsla() 提供回退颜色
- 测试不同浏览器中的 backdrop-filter 效果（旧版 Firefox 不支持）
- 使用 CSS 自定义属性方便主题切换

**无障碍考量**：
- 确保文字对比度符合 WCAG AA 标准（普通文字最低 4.5:1）
- 为对动画敏感的用户提供 `prefers-reduced-motion` 媒体查询替代方案
- 使用 Coblis 或 Color Oracle 等工具测试色盲用户的颜色组合

---

## English Version (en-US)

### Design Overview
Generate **Neon Cyberpunk** style interface design for products. This is a futuristic style that combines cyberpunk aesthetics with neon lighting, creating a sci-fi movie-like digital world experience through deep black backgrounds, high-contrast neon colors, terminal interfaces, and matrix rain effects.

## Core Design Requirements

### 1. Deep Dark Background System

**Background Principles**:
- Use near-pure black gradients
- Optional subtle noise and scanlines
- Create deep cyber space atmosphere

**Complete CSS Implementation**:
```css
/* Cyberpunk deep background */
.cyber-bg {
  background: radial-gradient(
    circle at center,
    #0a0f14 0%,
    #050810 45%,
    #000000 100%
  );
  min-height: 100vh;
  color: #e5e7eb;
  position: relative;
  overflow: hidden;
}

/* Noise texture overlay */
.cyber-noise {
  position: relative;
}

.cyber-noise::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: 0.08;
  background-image:
    repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0, 255, 65, 0.03) 2px,
      rgba(0, 255, 65, 0.03) 4px
    );
  mix-blend-mode: overlay;
  z-index: 1;
}
```

### 2. Neon Color System

**Color Principles**:
- Use high-saturation neon colors
- Every color must have multi-layer glow effects
- Text and borders need halos

**Complete Color Scheme**:
```css
:root {
  /* Base dark colors */
  --cyber-black: #000000;
  --cyber-dark-900: #0a0a0a;
  --cyber-dark-800: #0f0f0f;
  --cyber-dark-700: #1a1a1a;

  /* Neon colors */
  --cyber-neon-green: #00ff41;
  --cyber-neon-cyan: #00ffff;
  --cyber-neon-purple: #b967ff;
  --cyber-neon-magenta: #ff00ff;
  --cyber-neon-pink: #ff1493;
  --cyber-neon-orange: #ff6600;
  --cyber-neon-yellow: #ffff00;

  /* Text colors */
  --cyber-text-primary: #e5e7eb;
  --cyber-text-secondary: #9ca3af;
  --cyber-text-muted: #6b7280;

  /* Neon RGB values (for rgba) */
  --cyber-green-rgb: 0, 255, 65;
  --cyber-cyan-rgb: 0, 255, 255;
  --cyber-purple-rgb: 185, 103, 255;
  --cyber-magenta-rgb: 255, 0, 255;
}

/* Neon green text glow */
.cyber-text-neon-green {
  color: var(--cyber-neon-green);
  text-shadow:
    0 0 5px rgba(var(--cyber-green-rgb), 0.8),
    0 0 10px rgba(var(--cyber-green-rgb), 0.6),
    0 0 20px rgba(var(--cyber-green-rgb), 0.4),
    0 0 40px rgba(var(--cyber-green-rgb), 0.2);
}
```

*(继续包含终端、卡片、LED、按钮、动画等所有组件的英文版说明...)*

## Important Notes

1. **Deep Dark Background Required**: Background must be near-black (#000000 - #1a1a1a) to ensure high contrast with neon colors
2. **Multi-layer Glow Effects**: All neon elements must use multi-layer box-shadow or text-shadow for glow
3. **Monospace Fonts**: Terminals and data displays must use monospace fonts (Courier New, Monaco)
4. **Animation Rhythm**: All animations maintain consistent rhythm (2-8 second range)
5. **Semi-transparent Overlays**: Use rgba() and backdrop-filter for glass morphism effects
6. **Border Glow**: Borders need both color and inner/outer glow shadows
7. **Responsive**: Reduce glow intensity and animation complexity on mobile

## Things to Avoid

❌ **Don't use light backgrounds**: Avoid any background brighter than #2a2a2a
❌ **Don't use low-saturation colors**: Neon colors must be high-saturation pure colors
❌ **Don't skip glow effects**: All neon elements must have text-shadow or box-shadow
❌ **Don't use serif fonts**: Terminals and data must use monospace fonts
❌ **Don't over-animate**: Avoid too many fast animations simultaneously, keep rhythm unified
❌ **Don't use solid fills**: Buttons and cards should use semi-transparent backgrounds not solid colors
❌ **Don't ignore webkit prefixes**: backdrop-filter needs -webkit- prefix for Safari support

## Additional Implementation Tips

**Performance Optimization**:
- Use `will-change: transform, opacity` for animated elements to enable GPU acceleration
- Limit the number of simultaneous glow effects on screen (max 10-15 glowing elements)
- Consider reducing animation complexity on lower-end devices using media queries

**Browser Compatibility**:
- Always provide fallback colors for rgba() and hsla()
- Test backdrop-filter effects across different browsers (not supported in older Firefox versions)
- Use CSS custom properties for easy theme switching

**Accessibility Considerations**:
- Ensure text contrast ratio meets WCAG AA standards (minimum 4.5:1 for normal text)
- Provide `prefers-reduced-motion` media query alternatives for users sensitive to animations
- Test color combinations for colorblind users using tools like Coblis or Color Oracle
