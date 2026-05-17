# Custom Prompt

## 中文版本 (zh-CN)

请使用 TailwindCSS 创建一个大胆、反叛且打破常规的 Anti-Design（反设计）风格界面组件。该界面应故意摒弃传统 UI 的和谐感与栅格对齐，通过高饱和度色彩、夸张的粗黑边框、不规则的旋转排版以及强烈的视觉冲突，营造出一种原始、粗野主义（Brutalism）和具有讽刺意味的现代艺术美学。

**核心设计要求**

1. **极粗的硬边框**
   - 所有容器、图片和按钮必须拥有极粗的纯黑边框（4px 至 8px）
   - 完全放弃圆角（`border-radius: 0`），强调结构的原始感
   - 边框可以故意不均匀，增加粗野感
   - 示例：
     ```css
     .anti-border {
       border: 6px solid #000000;
       border-radius: 0px;
       /* 边框可以不均匀 */
       border-right-width: 8px;
       border-bottom-width: 8px;
     }

     .anti-border-thick {
       border: 8px solid #000000;
       outline: 4px solid #FF0000;
       outline-offset: -2px;
     }
     ```

2. **硬性偏移阴影**
   - 阴影绝对不能有模糊（Blur）效果
   - 使用纯黑色的硬性偏移，创造出贴纸或剪贴画的层次感
   - 偏移量建议：8px-16px
   - 示例：
     ```css
     .hard-shadow {
       box-shadow: 8px 8px 0px 0px #000000;
       transition: all 0.15s ease-out;
     }

     .hard-shadow:hover {
       box-shadow: 12px 12px 0px 0px #000000;
       transform: translate(-4px, -4px);
     }

     .hard-shadow:active {
       box-shadow: 4px 4px 0px 0px #000000;
       transform: translate(4px, 4px);
     }

     /* 彩色硬阴影变体 */
     .hard-shadow-yellow {
       box-shadow: 10px 10px 0px 0px #FFFF00;
     }

     .hard-shadow-red {
       box-shadow: 10px 10px 0px 0px #FF0000;
     }
     ```

3. **受控的混乱与旋转**
   - 关键元素（标题、卡片、徽章）应应用随机的轻微旋转（-6deg 到 6deg）
   - 打破水平线的单调，制造视觉噪音
   - 悬停时旋转角度变化，增加交互感
   - 示例：
     ```css
     .tilt-left {
       transform: rotate(-3deg);
     }

     .tilt-right {
       transform: rotate(2deg);
     }

     .tilt-random {
       transform: rotate(-1.5deg);
     }

     .tilt-hover {
       transition: transform 0.2s ease;
     }

     .tilt-hover:hover {
       transform: rotate(2deg) scale(1.05);
     }

     /* 使用 nth-child 实现多元素随机旋转 */
     .anti-grid > *:nth-child(odd) {
       transform: rotate(-2deg);
     }

     .anti-grid > *:nth-child(even) {
       transform: rotate(1.5deg);
     }

     .anti-grid > *:nth-child(3n) {
       transform: rotate(3deg);
     }
     ```

4. **重叠与错位布局**
   - 使用负边距（Negative Margin）或绝对定位让元素故意重叠
   - 制造拥挤和冲突感，打破传统的留白规则
   - 确保被覆盖的内容仍然可访问
   - 示例：
     ```css
     .forced-overlap {
       margin-top: -20px;
       margin-left: -15px;
       z-index: 10;
       position: relative;
       background-color: #ffffff;
     }

     .overlap-stack > *:nth-child(2) {
       margin-top: -30px;
       margin-left: 20px;
     }

     .overlap-stack > *:nth-child(3) {
       margin-top: -40px;
       margin-left: -10px;
     }

     .chaotic-position {
       position: absolute;
       top: 15%;
       right: -5%;
       transform: rotate(12deg);
     }
     ```

5. **原始排版系统**
   - 混合使用无衬线字体和等宽字体
   - 字号要有巨大的对比（极小说明文 vs 巨大标题）
   - 行高故意设置得非常紧凑
   - 示例：
     ```css
     .typography-clash {
       font-family: 'Courier New', monospace;
       letter-spacing: -2px;
       line-height: 0.9;
       text-transform: uppercase;
       font-weight: 900;
     }

     .anti-headline {
       font-size: 5rem;
       font-weight: 900;
       line-height: 0.85;
       letter-spacing: -0.05em;
       text-transform: uppercase;
     }

     .anti-small {
       font-size: 0.65rem;
       letter-spacing: 0.2em;
       text-transform: uppercase;
     }

     /* 混搭字体风格 */
     .font-mix {
       font-family: 'Times New Roman', serif;
     }

     .font-mix strong {
       font-family: 'Arial Black', sans-serif;
     }

     .font-mix em {
       font-family: 'Courier New', monospace;
       font-style: normal;
     }
     ```

6. **高对比度色块**
   - 背景和前景应使用纯度极高的颜色进行撞色
   - 避免渐变，避免透明度（除非用于特定的叠加效果）
   - 颜色碰撞是核心美学
   - 示例：
     ```css
     .color-block-yellow {
       background-color: #FFFF00;
       color: #0000FF;
       border: 4px solid #FF0000;
     }

     .color-block-blue {
       background-color: #0000FF;
       color: #FFFF00;
       border: 4px solid #000000;
     }

     .color-block-red {
       background-color: #FF0000;
       color: #FFFFFF;
       border: 4px solid #000000;
     }

     .color-block-green {
       background-color: #00FF00;
       color: #000000;
       border: 4px solid #FF00FF;
     }

     /* 分区域色块 */
     .anti-section:nth-child(odd) {
       background: #FFFFFF;
     }

     .anti-section:nth-child(even) {
       background: #FFFF00;
     }
     ```

7. **装饰性元素与图案**
   - 使用几何图案、条纹和噪点增加视觉复杂度
   - 添加「贴纸」风格的装饰元素
   - 示例：
     ```css
     /* 条纹背景 */
     .stripe-bg {
       background: repeating-linear-gradient(
         45deg,
         #000000,
         #000000 10px,
         #FFFF00 10px,
         #FFFF00 20px
       );
     }

     /* 点阵背景 */
     .dot-pattern {
       background-image: radial-gradient(#000000 2px, transparent 2px);
       background-size: 20px 20px;
       background-color: #FFFFFF;
     }

     /* 网格线背景 */
     .grid-lines {
       background-image:
         linear-gradient(#000000 1px, transparent 1px),
         linear-gradient(90deg, #000000 1px, transparent 1px);
       background-size: 40px 40px;
       background-color: #FFFFFF;
     }
     ```

**配色方案（高饱和度撞色）**

基础色：
- 纯黑（Brutal Black）: #000000
- 纯白（Paper White）: #FFFFFF

高亮色（RGB/CMY）：
- 警告红（Alert Red）: #FF0000
- 荧光绿（Terminal Green）: #00FF00
- 纯蓝（Link Blue）: #0000FF
- 荧光黄（Highlighter Yellow）: #FFFF00, #FFEB3B
- 品红（Magenta）: #FF00FF
- 青色（Cyan）: #00FFFF

背景推荐：
- 白纸风格: #FFFFFF
- 警示风格: #FFFF00
- 蓝屏风格: #0000FF

**关键 CSS 类示例**

```css
/* 反设计按钮 */
.btn-anti {
  background: #FF00FF;
  color: #000000;
  border: 6px solid #000000;
  padding: 16px 40px;
  font-family: 'Arial Black', sans-serif;
  font-size: 24px;
  font-weight: 900;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: 10px 10px 0px 0px #000000;
  transition: all 0.1s linear;
}

.btn-anti:hover {
  background: #00FF00;
  box-shadow: 15px 15px 0px 0px #000000;
  transform: translate(-5px, -5px) rotate(-1deg);
}

.btn-anti:active {
  background: #FF0000;
  color: #FFFFFF;
  box-shadow: 0px 0px 0px 0px #000000;
  transform: translate(10px, 10px);
}

/* 次要按钮 */
.btn-anti-secondary {
  background: #FFFFFF;
  color: #000000;
  border: 4px solid #000000;
  padding: 12px 32px;
  font-size: 18px;
  font-weight: 700;
  box-shadow: 6px 6px 0px 0px #FFFF00;
}

.btn-anti-secondary:hover {
  background: #FFFF00;
  box-shadow: 8px 8px 0px 0px #000000;
}

/* 残酷主义卡片 */
.card-brutal {
  position: relative;
  background: #FFFFFF;
  border: 5px solid #000000;
  padding: 24px;
  max-width: 400px;
  box-shadow: 12px 12px 0px 0px #FFEB3B;
  transform: rotate(1deg);
}

.card-brutal-header {
  background: #000000;
  color: #FFFFFF;
  padding: 8px 16px;
  margin: -24px -24px 16px -24px;
  border-bottom: 5px solid #000000;
  font-family: monospace;
  font-weight: bold;
  text-align: center;
}

.card-brutal:hover {
  box-shadow: 16px 16px 0px 0px #FF0000;
  transform: rotate(-1deg);
}

/* 跑马灯装饰 */
.marquee-container {
  width: 100%;
  overflow: hidden;
  border-top: 4px solid #000000;
  border-bottom: 4px solid #000000;
  background: #FFFF00;
  padding: 8px 0;
  white-space: nowrap;
}

.marquee-content {
  display: inline-block;
  animation: marquee-scroll 10s linear infinite;
  font-family: monospace;
  font-size: 1.5rem;
  font-weight: bold;
  padding-right: 50px;
}

@keyframes marquee-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* 装饰性贴纸 */
.sticker-badge {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 96px;
  height: 96px;
  background: #FF0000;
  color: #FFFFFF;
  border: 4px solid #000000;
  border-radius: 50%;
  font-weight: bold;
  font-size: 14px;
  text-transform: uppercase;
  transform: rotate(15deg);
  box-shadow: 4px 4px 0px rgba(0, 0, 0, 0.5);
  z-index: 20;
}

.sticker-badge:hover {
  background: #000000;
  color: #FF0000;
  transform: rotate(0deg) scale(1.1);
}

/* 星形贴纸 */
.sticker-star {
  position: absolute;
  width: 80px;
  height: 80px;
  background: #FFFF00;
  border: 3px solid #000000;
  clip-path: polygon(
    50% 0%, 61% 35%, 98% 35%, 68% 57%,
    79% 91%, 50% 70%, 21% 91%, 32% 57%,
    2% 35%, 39% 35%
  );
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 12px;
  transform: rotate(-10deg);
}

/* 输入框 */
.input-anti {
  background: #FFFFFF;
  border: 4px solid #000000;
  padding: 12px 16px;
  font-family: monospace;
  font-size: 16px;
  box-shadow: 4px 4px 0px 0px #000000;
}

.input-anti:focus {
  outline: none;
  border-color: #0000FF;
  box-shadow: 6px 6px 0px 0px #0000FF;
}

/* 导航栏 */
.nav-anti {
  background: linear-gradient(90deg, #FFFF00 0%, #FF00FF 50%, #00FFFF 100%);
  border-bottom: 6px solid #000000;
  padding: 16px 24px;
  transform: skewY(-1deg);
}

.nav-anti-link {
  background: #000000;
  color: #FFFFFF;
  padding: 8px 16px;
  border: 3px solid #FFFFFF;
  font-weight: bold;
  text-transform: uppercase;
  transform: rotate(-2deg);
  display: inline-block;
  margin: 0 8px;
}

.nav-anti-link:hover {
  background: #FF0000;
  transform: rotate(2deg) scale(1.1);
}
```

**Tailwind CSS 配置**

如使用 Tailwind CSS，添加以下配置：

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'anti-black': '#000000',
        'anti-white': '#FFFFFF',
        'anti-red': '#FF0000',
        'anti-green': '#00FF00',
        'anti-blue': '#0000FF',
        'anti-yellow': '#FFFF00',
        'anti-magenta': '#FF00FF',
        'anti-cyan': '#00FFFF',
      },
      boxShadow: {
        'hard': '8px 8px 0px 0px #000000',
        'hard-lg': '12px 12px 0px 0px #000000',
        'hard-xl': '16px 16px 0px 0px #000000',
        'hard-yellow': '10px 10px 0px 0px #FFFF00',
        'hard-red': '10px 10px 0px 0px #FF0000',
      },
      borderWidth: {
        '6': '6px',
        '8': '8px',
      },
      rotate: {
        '-3': '-3deg',
        '-2': '-2deg',
        '-1': '-1deg',
        '1': '1deg',
        '2': '2deg',
        '3': '3deg',
        '6': '6deg',
        '12': '12deg',
        '15': '15deg',
      },
      animation: {
        'marquee': 'marquee-scroll 10s linear infinite',
        'wiggle': 'wiggle 0.5s ease-in-out infinite',
      },
      keyframes: {
        'marquee-scroll': {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-50%)' },
        },
        'wiggle': {
          '0%, 100%': { transform: 'rotate(-3deg)' },
          '50%': { transform: 'rotate(3deg)' },
        },
      },
    },
  },
}
```

**重要提示**

- 拒绝平滑：所有 `transition` 应该是快速且线性的（linear），避免类似 iOS 的平滑阻尼感
- 图像处理：图片应该被强制调整大小（可能纵横比失真），或应用二值化滤镜，或直接加粗黑框
- 不要留白：Anti-Design 倾向于填满屏幕，或使用巨大的留白来嘲讽布局，不要让间距看起来「均匀」
- 系统字体：优先使用默认系统字体栈（sans-serif, serif, monospace），增加「未经设计」的原始感
- 装饰性元素：使用「X」符号的方框、巨大箭头、复古 Windows 95 风格图标或 ASCII 字符作为装饰
- 响应式：在移动端将混乱堆叠转换为垂直单栏，但保持粗边框和硬阴影特征
- 可访问性：虽然风格反叛，但确保文本与背景对比度符合 AA 标准
- Z-index 管理：由于大量使用重叠和绝对定位，仔细管理 `z-index` 防止按钮被遮挡


---

## English Version (en-US)

Please use TailwindCSS to create a bold, rebellious, and rule-breaking Anti-Design style interface component. The interface should intentionally discard traditional UI harmony and grid alignment, using high-saturation colors, exaggerated heavy black borders, irregular rotated layouts, and strong visual conflicts to create a primitive, Brutalist, and ironic modern art aesthetic.

**Core Design Requirements**

1. **Heavy Hard Borders**
   - All containers, images, and buttons must have extremely thick pure black borders (4px to 8px)
   - Completely abandon rounded corners (`border-radius: 0`) to emphasize structural primitive feel
   - Borders can be intentionally uneven to increase brutalist feel
   - Example:
     ```css
     .anti-border {
       border: 6px solid #000000;
       border-radius: 0px;
       /* Borders can be uneven */
       border-right-width: 8px;
       border-bottom-width: 8px;
     }

     .anti-border-thick {
       border: 8px solid #000000;
       outline: 4px solid #FF0000;
       outline-offset: -2px;
     }
     ```

2. **Hard Offset Shadows**
   - Shadows must absolutely not have any blur effect
   - Use pure black hard offsets to create sticker or collage-like layering
   - Recommended offset: 8px-16px
   - Example:
     ```css
     .hard-shadow {
       box-shadow: 8px 8px 0px 0px #000000;
       transition: all 0.15s ease-out;
     }

     .hard-shadow:hover {
       box-shadow: 12px 12px 0px 0px #000000;
       transform: translate(-4px, -4px);
     }

     .hard-shadow:active {
       box-shadow: 4px 4px 0px 0px #000000;
       transform: translate(4px, 4px);
     }

     /* Colored hard shadow variants */
     .hard-shadow-yellow {
       box-shadow: 10px 10px 0px 0px #FFFF00;
     }

     .hard-shadow-red {
       box-shadow: 10px 10px 0px 0px #FF0000;
     }
     ```

3. **Controlled Chaos & Rotation**
   - Key elements (headings, cards, badges) should apply random slight rotations (-6deg to 6deg)
   - Break the monotony of horizontal lines and create visual noise
   - Rotation angle changes on hover for interactive feel
   - Example:
     ```css
     .tilt-left {
       transform: rotate(-3deg);
     }

     .tilt-right {
       transform: rotate(2deg);
     }

     .tilt-random {
       transform: rotate(-1.5deg);
     }

     .tilt-hover {
       transition: transform 0.2s ease;
     }

     .tilt-hover:hover {
       transform: rotate(2deg) scale(1.05);
     }

     /* Use nth-child for random rotation on multiple elements */
     .anti-grid > *:nth-child(odd) {
       transform: rotate(-2deg);
     }

     .anti-grid > *:nth-child(even) {
       transform: rotate(1.5deg);
     }

     .anti-grid > *:nth-child(3n) {
       transform: rotate(3deg);
     }
     ```

4. **Overlapping & Misalignment**
   - Use negative margins or absolute positioning to force elements to overlap intentionally
   - Create a sense of crowding and conflict, breaking traditional whitespace rules
   - Ensure covered content remains accessible
   - Example:
     ```css
     .forced-overlap {
       margin-top: -20px;
       margin-left: -15px;
       z-index: 10;
       position: relative;
       background-color: #ffffff;
     }

     .overlap-stack > *:nth-child(2) {
       margin-top: -30px;
       margin-left: 20px;
     }

     .overlap-stack > *:nth-child(3) {
       margin-top: -40px;
       margin-left: -10px;
     }

     .chaotic-position {
       position: absolute;
       top: 15%;
       right: -5%;
       transform: rotate(12deg);
     }
     ```

5. **Raw Typography System**
   - Mix sans-serif fonts with monospace fonts
   - Use massive contrast in font sizes (tiny explanation text vs. gigantic headings)
   - Line height intentionally set very tight
   - Example:
     ```css
     .typography-clash {
       font-family: 'Courier New', monospace;
       letter-spacing: -2px;
       line-height: 0.9;
       text-transform: uppercase;
       font-weight: 900;
     }

     .anti-headline {
       font-size: 5rem;
       font-weight: 900;
       line-height: 0.85;
       letter-spacing: -0.05em;
       text-transform: uppercase;
     }

     .anti-small {
       font-size: 0.65rem;
       letter-spacing: 0.2em;
       text-transform: uppercase;
     }

     /* Mixed font styles */
     .font-mix {
       font-family: 'Times New Roman', serif;
     }

     .font-mix strong {
       font-family: 'Arial Black', sans-serif;
     }

     .font-mix em {
       font-family: 'Courier New', monospace;
       font-style: normal;
     }
     ```

6. **Bold Color Blocking**
   - Backgrounds and foregrounds should use extremely high-purity contrasting colors
   - Avoid gradients and transparency (unless for specific overlay effects)
   - Color collision is the core aesthetic
   - Example:
     ```css
     .color-block-yellow {
       background-color: #FFFF00;
       color: #0000FF;
       border: 4px solid #FF0000;
     }

     .color-block-blue {
       background-color: #0000FF;
       color: #FFFF00;
       border: 4px solid #000000;
     }

     .color-block-red {
       background-color: #FF0000;
       color: #FFFFFF;
       border: 4px solid #000000;
     }

     .color-block-green {
       background-color: #00FF00;
       color: #000000;
       border: 4px solid #FF00FF;
     }

     /* Sectioned color blocks */
     .anti-section:nth-child(odd) {
       background: #FFFFFF;
     }

     .anti-section:nth-child(even) {
       background: #FFFF00;
     }
     ```

7. **Decorative Elements & Patterns**
   - Use geometric patterns, stripes, and noise to increase visual complexity
   - Add "sticker" style decorative elements
   - Example:
     ```css
     /* Stripe background */
     .stripe-bg {
       background: repeating-linear-gradient(
         45deg,
         #000000,
         #000000 10px,
         #FFFF00 10px,
         #FFFF00 20px
       );
     }

     /* Dot pattern background */
     .dot-pattern {
       background-image: radial-gradient(#000000 2px, transparent 2px);
       background-size: 20px 20px;
       background-color: #FFFFFF;
     }

     /* Grid lines background */
     .grid-lines {
       background-image:
         linear-gradient(#000000 1px, transparent 1px),
         linear-gradient(90deg, #000000 1px, transparent 1px);
       background-size: 40px 40px;
       background-color: #FFFFFF;
     }
     ```

**Color Palette (High Saturation Clash)**

Base:
- Brutal Black: #000000
- Paper White: #FFFFFF

Accents (RGB/CMY):
- Alert Red: #FF0000
- Terminal Green: #00FF00
- Link Blue: #0000FF
- Highlighter Yellow: #FFFF00, #FFEB3B
- Magenta: #FF00FF
- Cyan: #00FFFF

Recommended Backgrounds:
- Paper style: #FFFFFF
- Warning style: #FFFF00
- Blue Screen style: #0000FF

**Key CSS Class Examples**

```css
/* Anti-Design Button */
.btn-anti {
  background: #FF00FF;
  color: #000000;
  border: 6px solid #000000;
  padding: 16px 40px;
  font-family: 'Arial Black', sans-serif;
  font-size: 24px;
  font-weight: 900;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: 10px 10px 0px 0px #000000;
  transition: all 0.1s linear;
}

.btn-anti:hover {
  background: #00FF00;
  box-shadow: 15px 15px 0px 0px #000000;
  transform: translate(-5px, -5px) rotate(-1deg);
}

.btn-anti:active {
  background: #FF0000;
  color: #FFFFFF;
  box-shadow: 0px 0px 0px 0px #000000;
  transform: translate(10px, 10px);
}

/* Secondary Button */
.btn-anti-secondary {
  background: #FFFFFF;
  color: #000000;
  border: 4px solid #000000;
  padding: 12px 32px;
  font-size: 18px;
  font-weight: 700;
  box-shadow: 6px 6px 0px 0px #FFFF00;
}

.btn-anti-secondary:hover {
  background: #FFFF00;
  box-shadow: 8px 8px 0px 0px #000000;
}

/* Brutalist Card */
.card-brutal {
  position: relative;
  background: #FFFFFF;
  border: 5px solid #000000;
  padding: 24px;
  max-width: 400px;
  box-shadow: 12px 12px 0px 0px #FFEB3B;
  transform: rotate(1deg);
}

.card-brutal-header {
  background: #000000;
  color: #FFFFFF;
  padding: 8px 16px;
  margin: -24px -24px 16px -24px;
  border-bottom: 5px solid #000000;
  font-family: monospace;
  font-weight: bold;
  text-align: center;
}

.card-brutal:hover {
  box-shadow: 16px 16px 0px 0px #FF0000;
  transform: rotate(-1deg);
}

/* Marquee Banner */
.marquee-container {
  width: 100%;
  overflow: hidden;
  border-top: 4px solid #000000;
  border-bottom: 4px solid #000000;
  background: #FFFF00;
  padding: 8px 0;
  white-space: nowrap;
}

.marquee-content {
  display: inline-block;
  animation: marquee-scroll 10s linear infinite;
  font-family: monospace;
  font-size: 1.5rem;
  font-weight: bold;
  padding-right: 50px;
}

@keyframes marquee-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* Sticker Badge */
.sticker-badge {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 96px;
  height: 96px;
  background: #FF0000;
  color: #FFFFFF;
  border: 4px solid #000000;
  border-radius: 50%;
  font-weight: bold;
  font-size: 14px;
  text-transform: uppercase;
  transform: rotate(15deg);
  box-shadow: 4px 4px 0px rgba(0, 0, 0, 0.5);
  z-index: 20;
}

.sticker-badge:hover {
  background: #000000;
  color: #FF0000;
  transform: rotate(0deg) scale(1.1);
}

/* Star Sticker */
.sticker-star {
  position: absolute;
  width: 80px;
  height: 80px;
  background: #FFFF00;
  border: 3px solid #000000;
  clip-path: polygon(
    50% 0%, 61% 35%, 98% 35%, 68% 57%,
    79% 91%, 50% 70%, 21% 91%, 32% 57%,
    2% 35%, 39% 35%
  );
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 12px;
  transform: rotate(-10deg);
}

/* Input Field */
.input-anti {
  background: #FFFFFF;
  border: 4px solid #000000;
  padding: 12px 16px;
  font-family: monospace;
  font-size: 16px;
  box-shadow: 4px 4px 0px 0px #000000;
}

.input-anti:focus {
  outline: none;
  border-color: #0000FF;
  box-shadow: 6px 6px 0px 0px #0000FF;
}

/* Navigation Bar */
.nav-anti {
  background: linear-gradient(90deg, #FFFF00 0%, #FF00FF 50%, #00FFFF 100%);
  border-bottom: 6px solid #000000;
  padding: 16px 24px;
  transform: skewY(-1deg);
}

.nav-anti-link {
  background: #000000;
  color: #FFFFFF;
  padding: 8px 16px;
  border: 3px solid #FFFFFF;
  font-weight: bold;
  text-transform: uppercase;
  transform: rotate(-2deg);
  display: inline-block;
  margin: 0 8px;
}

.nav-anti-link:hover {
  background: #FF0000;
  transform: rotate(2deg) scale(1.1);
}
```

**Tailwind CSS Configuration**

If using Tailwind CSS, add the following configuration:

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'anti-black': '#000000',
        'anti-white': '#FFFFFF',
        'anti-red': '#FF0000',
        'anti-green': '#00FF00',
        'anti-blue': '#0000FF',
        'anti-yellow': '#FFFF00',
        'anti-magenta': '#FF00FF',
        'anti-cyan': '#00FFFF',
      },
      boxShadow: {
        'hard': '8px 8px 0px 0px #000000',
        'hard-lg': '12px 12px 0px 0px #000000',
        'hard-xl': '16px 16px 0px 0px #000000',
        'hard-yellow': '10px 10px 0px 0px #FFFF00',
        'hard-red': '10px 10px 0px 0px #FF0000',
      },
      borderWidth: {
        '6': '6px',
        '8': '8px',
      },
      rotate: {
        '-3': '-3deg',
        '-2': '-2deg',
        '-1': '-1deg',
        '1': '1deg',
        '2': '2deg',
        '3': '3deg',
        '6': '6deg',
        '12': '12deg',
        '15': '15deg',
      },
      animation: {
        'marquee': 'marquee-scroll 10s linear infinite',
        'wiggle': 'wiggle 0.5s ease-in-out infinite',
      },
      keyframes: {
        'marquee-scroll': {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-50%)' },
        },
        'wiggle': {
          '0%, 100%': { transform: 'rotate(-3deg)' },
          '50%': { transform: 'rotate(3deg)' },
        },
      },
    },
  },
}
```

**Important Notes**

- Refuse Smoothness: All `transition` effects should be fast and linear, avoid smooth iOS-like damping feel
- Image Processing: Images should be forcibly resized (risking aspect ratio distortion), applied with Threshold filter, or framed with thick black borders
- No Balanced Whitespace: Anti-Design tends to fill the screen or use massive whitespace to mock layout, don't make spacing look "even"
- System Fonts: Prioritize default system font stacks (sans-serif, serif, monospace) for "undesigned" primitive feel
- Decorative Elements: Use boxes with "X" symbols, huge arrows, retro Windows 95 style icons, or ASCII characters as decoration
- Responsive: On mobile, convert chaotic stacking to vertical single-column, but maintain thick border and hard shadow characteristics
- Accessibility: Although the style is rebellious, ensure text-to-background contrast meets AA standards
- Z-index Management: Due to heavy use of overlapping and absolute positioning, manage `z-index` carefully to prevent buttons from being blocked
