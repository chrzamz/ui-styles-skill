# Custom Prompt

## 中文版本 (zh-CN)

请使用 TailwindCSS 创建一个光影艺术风格的界面，通过发光、阴影和光晕效果创造视觉焦点和氛围。

**核心设计要求**

1. **霓虹灯光（Neon Lights）**
   - 多层 text-shadow：0 0 5px, 0 0 10px, 0 0 20px, 0 0 40px, 0 0 80px, 0 0 120px
   - 高饱和色彩：#00f3ff (蓝), #ff006e (粉), #39ff14 (绿)
   - 闪烁动画：
     \`\`\`css
     @keyframes flicker {
       0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; }
       20%, 24%, 55% { opacity: 0.7; }
     }
     \`\`\`
   - 深色背景：#0a0a0a

2. **环境光（Ambient Lighting）**
   - 径向渐变光晕：\`radial-gradient(circle, color 0%, transparent 70%)\`
   - 大范围模糊：\`filter: blur(60px)\`
   - 低透明度：opacity: 0.6-0.8
   - 缓慢浮动动画

3. **发光效果（Glow Effect）**
   - 三层 box-shadow：
     \`\`\`css
     box-shadow:
       0 0 10px rgba(59, 130, 246, 0.5),
       0 0 20px rgba(59, 130, 246, 0.3),
       0 0 40px rgba(59, 130, 246, 0.2);
     \`\`\`
   - 脉动动画改变阴影范围
   - 悬停增强效果

4. **背光效果（Backlight）**
   - 伪元素旋转渐变边框：
     \`\`\`css
     .backlight::before {
       content: "";
       position: absolute;
       top: -2px; left: -2px; right: -2px; bottom: -2px;
       background: linear-gradient(45deg, transparent 30%, #3b82f6 50%, transparent 70%);
       animation: rotate 4s linear infinite;
       z-index: -1;
     }
     \`\`\`
   - Z-index 分层
   - 轮廓发光

5. **聚光灯（Spotlight）**
   - 径向聚焦光：\`radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%)\`
   - 动态移动动画
   - 多光源叠加

**配色方案（光影色彩）**

霓虹系：
- 电蓝：#00f3ff, #00a8ff
- 荧光粉：#ff006e, #d90056
- 荧光绿：#39ff14, #2bcc0f

发光系：
- 蓝光：#3b82f6 (rgba 透明度变化)
- 紫光：#a855f7 (rgba 透明度变化)
- 橙光：#f97316 (rgba 透明度变化)

环境光：
- 紫蓝：#667eea
- 粉色：#f093fb
- 青色：#4facfe

**关键 CSS 类示例**

\`\`\`css
/* 霓虹文字 */
.neon-text {
  color: #00f3ff;
  font-size: 64px;
  font-weight: 900;
  text-shadow:
    0 0 5px #00f3ff,
    0 0 10px #00f3ff,
    0 0 20px #00f3ff,
    0 0 40px #00a8ff,
    0 0 80px #00a8ff,
    0 0 120px #00a8ff;
  animation: flicker 3s infinite;
}

@keyframes flicker {
  0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; }
  20%, 24%, 55% { opacity: 0.7; }
}

/* 环境光球 */
.ambient-orb {
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, #667eea 0%, transparent 70%);
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.6;
  animation: ambientFloat 8s ease-in-out infinite;
}

@keyframes ambientFloat {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(30px, -30px); opacity: 0.8; }
}

/* 发光按钮 */
.glow-button {
  background: #1e3a8a;
  color: white;
  padding: 20px 40px;
  border: none;
  border-radius: 12px;
  box-shadow:
    0 0 10px rgba(59, 130, 246, 0.5),
    0 0 20px rgba(59, 130, 246, 0.3),
    0 0 40px rgba(59, 130, 246, 0.2);
  animation: pulse 2s ease-in-out infinite;
  cursor: pointer;
}

.glow-button:hover {
  box-shadow:
    0 0 20px rgba(59, 130, 246, 0.8),
    0 0 40px rgba(59, 130, 246, 0.6),
    0 0 80px rgba(59, 130, 246, 0.4);
  transform: translateY(-5px);
}

@keyframes pulse {
  0%, 100% {
    box-shadow:
      0 0 10px rgba(59, 130, 246, 0.5),
      0 0 20px rgba(59, 130, 246, 0.3),
      0 0 40px rgba(59, 130, 246, 0.2);
  }
  50% {
    box-shadow:
      0 0 15px rgba(59, 130, 246, 0.6),
      0 0 30px rgba(59, 130, 246, 0.4),
      0 0 60px rgba(59, 130, 246, 0.3);
  }
}

/* 背光卡片 */
.backlight-card {
  position: relative;
  background: rgba(20, 20, 20, 0.8);
  border-radius: 20px;
  padding: 32px;
  overflow: hidden;
}

.backlight-card::before {
  content: "";
  position: absolute;
  top: -2px; left: -2px; right: -2px; bottom: -2px;
  background: linear-gradient(45deg, transparent 30%, #3b82f6 50%, transparent 70%);
  border-radius: 20px;
  z-index: -1;
  animation: rotate 4s linear infinite;
}

@keyframes rotate {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* 聚光灯 */
.spotlight {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.3) 0%, rgba(255, 255, 255, 0.1) 40%, transparent 70%);
  border-radius: 50%;
  position: absolute;
  animation: spotlightMove 8s ease-in-out infinite;
}

@keyframes spotlightMove {
  0%, 100% { transform: translate(0, 0) scale(1); }
  25% { transform: translate(50px, -30px) scale(1.1); }
  50% { transform: translate(-30px, 50px) scale(0.9); }
  75% { transform: translate(40px, 40px) scale(1.05); }
}
\`\`\`

**重要提示**
- text-shadow 和 box-shadow 层数建议 3-6 层
- 霓虹效果需要深色背景（#000-#1a1a1a）
- 环境光使用 filter: blur() 创造柔和感
- 动画速度建议 2s-8s，避免过快
- 透明度递减创造深度感


---

## English Version (en-US)

Please create a Light Art style interface using TailwindCSS, creating visual focus and atmosphere through glow, shadow, and halo effects.

**Core Design Requirements**

1. **Neon Lights**
   - Multi-layer text-shadow: 0 0 5px, 0 0 10px, 0 0 20px, 0 0 40px, 0 0 80px, 0 0 120px
   - High saturation colors: #00f3ff (blue), #ff006e (pink), #39ff14 (green)
   - Flicker animation:
     \`\`\`css
     @keyframes flicker {
       0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; }
       20%, 24%, 55% { opacity: 0.7; }
     }
     \`\`\`
   - Dark background: #0a0a0a

2. **Ambient Lighting**
   - Radial gradient halo: \`radial-gradient(circle, color 0%, transparent 70%)\`
   - Large blur: \`filter: blur(60px)\`
   - Low opacity: 0.6-0.8
   - Slow floating animation

3. **Glow Effect**
   - Three-layer box-shadow:
     \`\`\`css
     box-shadow:
       0 0 10px rgba(59, 130, 246, 0.5),
       0 0 20px rgba(59, 130, 246, 0.3),
       0 0 40px rgba(59, 130, 246, 0.2);
     \`\`\`
   - Pulse animation changes shadow range
   - Hover enhancement

4. **Backlight Effect**
   - Pseudo-element rotating gradient border:
     \`\`\`css
     .backlight::before {
       content: "";
       position: absolute;
       top: -2px; left: -2px; right: -2px; bottom: -2px;
       background: linear-gradient(45deg, transparent 30%, #3b82f6 50%, transparent 70%);
       animation: rotate 4s linear infinite;
       z-index: -1;
     }
     \`\`\`
   - Z-index layering
   - Rim glow

5. **Spotlight**
   - Radial focused light: \`radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%)\`
   - Dynamic movement animation
   - Multiple light source overlay

**Color Scheme (Light Colors)**

Neon series:
- Electric blue: #00f3ff, #00a8ff
- Fluorescent pink: #ff006e, #d90056
- Fluorescent green: #39ff14, #2bcc0f

Glow series:
- Blue glow: #3b82f6 (rgba opacity variations)
- Purple glow: #a855f7 (rgba opacity variations)
- Orange glow: #f97316 (rgba opacity variations)

Ambient light:
- Purple-blue: #667eea
- Pink: #f093fb
- Cyan: #4facfe

**Key CSS Class Examples**

\`\`\`css
/* Neon Text */
.neon-text {
  color: #00f3ff;
  font-size: 64px;
  font-weight: 900;
  text-shadow:
    0 0 5px #00f3ff,
    0 0 10px #00f3ff,
    0 0 20px #00f3ff,
    0 0 40px #00a8ff,
    0 0 80px #00a8ff,
    0 0 120px #00a8ff;
  animation: flicker 3s infinite;
}

@keyframes flicker {
  0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; }
  20%, 24%, 55% { opacity: 0.7; }
}

/* Ambient Orb */
.ambient-orb {
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, #667eea 0%, transparent 70%);
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.6;
  animation: ambientFloat 8s ease-in-out infinite;
}

@keyframes ambientFloat {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(30px, -30px); opacity: 0.8; }
}

/* Glow Button */
.glow-button {
  background: #1e3a8a;
  color: white;
  padding: 20px 40px;
  border: none;
  border-radius: 12px;
  box-shadow:
    0 0 10px rgba(59, 130, 246, 0.5),
    0 0 20px rgba(59, 130, 246, 0.3),
    0 0 40px rgba(59, 130, 246, 0.2);
  animation: pulse 2s ease-in-out infinite;
  cursor: pointer;
}

.glow-button:hover {
  box-shadow:
    0 0 20px rgba(59, 130, 246, 0.8),
    0 0 40px rgba(59, 130, 246, 0.6),
    0 0 80px rgba(59, 130, 246, 0.4);
  transform: translateY(-5px);
}

@keyframes pulse {
  0%, 100% {
    box-shadow:
      0 0 10px rgba(59, 130, 246, 0.5),
      0 0 20px rgba(59, 130, 246, 0.3),
      0 0 40px rgba(59, 130, 246, 0.2);
  }
  50% {
    box-shadow:
      0 0 15px rgba(59, 130, 246, 0.6),
      0 0 30px rgba(59, 130, 246, 0.4),
      0 0 60px rgba(59, 130, 246, 0.3);
  }
}

/* Backlight Card */
.backlight-card {
  position: relative;
  background: rgba(20, 20, 20, 0.8);
  border-radius: 20px;
  padding: 32px;
  overflow: hidden;
}

.backlight-card::before {
  content: "";
  position: absolute;
  top: -2px; left: -2px; right: -2px; bottom: -2px;
  background: linear-gradient(45deg, transparent 30%, #3b82f6 50%, transparent 70%);
  border-radius: 20px;
  z-index: -1;
  animation: rotate 4s linear infinite;
}

@keyframes rotate {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Spotlight */
.spotlight {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.3) 0%, rgba(255, 255, 255, 0.1) 40%, transparent 70%);
  border-radius: 50%;
  position: absolute;
  animation: spotlightMove 8s ease-in-out infinite;
}

@keyframes spotlightMove {
  0%, 100% { transform: translate(0, 0) scale(1); }
  25% { transform: translate(50px, -30px) scale(1.1); }
  50% { transform: translate(-30px, 50px) scale(0.9); }
  75% { transform: translate(40px, 40px) scale(1.05); }
}
\`\`\`

**Important Notes**
- text-shadow and box-shadow layers recommended: 3-6 layers
- Neon effects require dark background (#000-#1a1a1a)
- Ambient light uses filter: blur() for softness
- Animation speed recommended: 2s-8s, avoid too fast
- Decreasing opacity creates depth

**Implementation Best Practices**

**Performance Considerations**:
- Limit the number of simultaneous blur filters (max 5-8 active filters) as they are computationally expensive
- Use CSS `will-change: transform, opacity` for animated light elements
- Consider reducing animation complexity on mobile devices using media queries
- Test performance on mid-range devices to ensure smooth 60fps animations

**Browser Compatibility**:
- CSS filters (blur, brightness) are well-supported in modern browsers
- Provide fallback colors for older browsers that don't support advanced shadow effects
- Test glow effects across browsers as rendering may vary (especially Safari vs Chrome)
- Use `-webkit-backdrop-filter` prefix for Safari support

**Accessibility & UX**:
- Ensure text contrast meets WCAG AA standards even with glow effects (minimum 4.5:1 ratio)
- Provide `prefers-reduced-motion` alternatives for users sensitive to animations
- Avoid overly bright glows that could cause eye strain in dark environments
- Test light effects with colorblind users to ensure visual hierarchy remains clear
- Ensure all interactive elements have clear hover and focus states beyond just glow changes
