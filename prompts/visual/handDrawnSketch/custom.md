# Custom Prompt

## 中文版本 (zh-CN)

请使用 TailwindCSS 创建一个手绘涂鸦风格的界面，通过手写字体、SVG 滤镜和随性线条创造温暖亲切的视觉体验。

**核心设计要求**

1. **手写字体系统**
   - 主标题字体：Caveat（支持粗细 400-700）
     \`\`\`css
     @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&display=swap');

     .hand-title {
       font-family: 'Caveat', cursive;
       font-size: 48px;
       font-weight: 700;
       letter-spacing: 0.02em;
     }
     \`\`\`

   - 正文字体：Patrick Hand（更易读）
     \`\`\`css
     @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');

     .hand-text {
       font-family: 'Patrick Hand', cursive;
       font-size: 16px;
       line-height: 1.6;
     }
     \`\`\`

   - 装饰字体：Reenie Beanie（更随性）
     \`\`\`css
     @import url('https://fonts.googleapis.com/css2?family=Reenie+Beanie&display=swap');

     .hand-casual {
       font-family: 'Reenie Beanie', cursive;
       font-size: 20px;
     }
     \`\`\`

2. **SVG 手绘滤镜效果**
   - 使用 feTurbulence + feDisplacementMap 创造手绘抖动感
   - 滤镜强度：scale 1.0-2.0（数值越大越明显）
   - 基础频率：baseFrequency 0.03-0.08
   - 示例：
     \`\`\`html
     <svg style="position: absolute; width: 0; height: 0;">
       <defs>
         <filter id="sketch-roughen">
           <feTurbulence type="turbulence" baseFrequency="0.05" numOctaves="2" result="turbulence"/>
           <feDisplacementMap in2="turbulence" in="SourceGraphic" scale="1.5" xChannelSelector="R" yChannelSelector="G"/>
         </filter>
       </defs>
     </svg>

     <div style="filter: url(#sketch-roughen);">
       <!-- 应用手绘滤镜的内容 -->
     </div>
     \`\`\`

   - 性能提示：仅对关键元素应用滤镜，避免全局使用

3. **粘贴便签设计**
   - 经典便签颜色：
     \`\`\`css
     .sticky-note-yellow {
       background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
     }

     .sticky-note-pink {
       background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%);
     }

     .sticky-note-blue {
       background: linear-gradient(135deg, #e1f5fe 0%, #b3e5fc 100%);
     }

     .sticky-note-green {
       background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
     }
     \`\`\`

   - 便签立体效果：
     \`\`\`css
     .sticky-note {
       box-shadow:
         0 4px 6px rgba(0, 0, 0, 0.1),
         0 1px 3px rgba(0, 0, 0, 0.08);
       transform: rotate(-2deg);  /* 随机旋转角度 -3deg ~ 3deg */
       transition: all 0.3s ease;
     }

     .sticky-note:hover {
       transform: rotate(0deg) scale(1.05);
       box-shadow:
         0 10px 20px rgba(0, 0, 0, 0.15),
         0 3px 6px rgba(0, 0, 0, 0.1);
       z-index: 10;
     }
     \`\`\`

4. **Grid 纸背景效果**
   - 使用 repeating-linear-gradient 创造网格纸
   - 网格间距：20px（推荐）
   - 示例：
     \`\`\`css
     .grid-paper-bg {
       background:
         repeating-linear-gradient(
           0deg,
           #f8f9fa 0px,
           #f8f9fa 1px,
           transparent 1px,
           transparent 20px
         ),
         repeating-linear-gradient(
           90deg,
           #f8f9fa 0px,
           #f8f9fa 1px,
           transparent 1px,
           transparent 20px
         ),
         #ffffff;
     }
     \`\`\`

   - 点阵纸背景：
     \`\`\`css
     .dot-paper-bg {
       background-image: radial-gradient(circle, #d0d0d0 1px, transparent 1px);
       background-size: 20px 20px;
       background-color: #ffffff;
     }
     \`\`\`

5. **手绘边框和线条**
   - 使用 border-image 或 SVG path 创造不规则边框
   - 虚线手绘效果：
     \`\`\`css
     .sketch-border {
       border: 2px dashed #2c3e50;
       border-radius: 4px;
       filter: url(#sketch-roughen);
     }
     \`\`\`

   - 波浪线分隔：
     \`\`\`html
     <svg width="100%" height="20">
       <path d="M 0 10 Q 10 5, 20 10 T 40 10 T 60 10 T 80 10 T 100 10"
             stroke="#2c3e50" stroke-width="2" fill="none"
             filter="url(#sketch-roughen)"/>
     </svg>
     \`\`\`

6. **手绘图标和箭头**
   - 使用 SVG path 绘制不规则形状
   - 示例（手绘勾选框）：
     \`\`\`html
     <svg width="24" height="24" viewBox="0 0 24 24">
       <defs>
         <filter id="icon-sketch">
           <feTurbulence baseFrequency="0.08" numOctaves="1"/>
           <feDisplacementMap in="SourceGraphic" scale="1.2"/>
         </filter>
       </defs>
       <path d="M 4 12 L 9 17 L 20 6"
             stroke="#2c3e50" stroke-width="2.5"
             fill="none" stroke-linecap="round"
             filter="url(#icon-sketch)"/>
     </svg>
     \`\`\`

7. **柔和动画效果**
   - 避免生硬的过渡，使用弹性缓动
   - 推荐 easing：cubic-bezier(0.68, -0.55, 0.265, 1.55)
   - 示例：
     \`\`\`css
     .sketch-animate {
       transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
     }

     .sketch-animate:hover {
       transform: scale(1.05) rotate(2deg);
     }
     \`\`\`

**配色方案（温暖友好）**

主色调（粘贴便签色系）：
- 黄色便签：#fff9c4, #fff59d, #fff176
- 粉色便签：#fce4ec, #f8bbd0, #f48fb1
- 蓝色便签：#e1f5fe, #b3e5fc, #81d4fa
- 绿色便签：#e8f5e9, #c8e6c9, #a5d6a7

文字色彩：
- 主要文字：#2c3e50（深蓝灰）
- 次要文字：#34495e（中蓝灰）
- 装饰文字：#7f8c8d（浅灰）

手绘线条：
- 黑色线条：#23303d
- 深灰线条：#4a5568
- 装饰线条：#a0aec0

背景色：
- 纸质背景：#ffffff, #fefefe, #fcfcfc
- 网格线条：#f8f9fa, #e9ecef

**关键 CSS 类示例**

\`\`\`css
/* 手绘卡片 */
.sketch-card {
  background: #ffffff;
  border: 2px solid #2c3e50;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 4px 4px 0 rgba(0, 0, 0, 0.1);
  filter: url(#sketch-roughen);
  font-family: 'Patrick Hand', cursive;
  transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.sketch-card:hover {
  transform: translateY(-4px) rotate(1deg);
  box-shadow: 6px 6px 0 rgba(0, 0, 0, 0.15);
}

/* 手绘按钮 */
.sketch-button {
  background: #fff176;
  border: 2px solid #2c3e50;
  border-radius: 12px;
  padding: 12px 24px;
  font-family: 'Caveat', cursive;
  font-size: 20px;
  font-weight: 700;
  color: #2c3e50;
  cursor: pointer;
  filter: url(#sketch-roughen);
  transition: all 0.3s ease;
  box-shadow: 3px 3px 0 rgba(0, 0, 0, 0.1);
}

.sketch-button:hover {
  background: #fff59d;
  transform: translate(-2px, -2px);
  box-shadow: 5px 5px 0 rgba(0, 0, 0, 0.15);
}

.sketch-button:active {
  transform: translate(1px, 1px);
  box-shadow: 2px 2px 0 rgba(0, 0, 0, 0.1);
}

/* 手绘输入框 */
.sketch-input {
  background: #ffffff;
  border: 2px dashed #4a5568;
  border-radius: 8px;
  padding: 12px 16px;
  font-family: 'Patrick Hand', cursive;
  font-size: 16px;
  color: #2c3e50;
  filter: url(#sketch-roughen);
  transition: all 0.3s ease;
}

.sketch-input:focus {
  outline: none;
  border-color: #2c3e50;
  border-style: solid;
  box-shadow: 0 0 0 4px rgba(44, 62, 80, 0.1);
}

.sketch-input::placeholder {
  color: #7f8c8d;
  font-style: italic;
}

/* 便签容器 */
.sticky-notes-container {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  perspective: 1000px;
}

.sticky-note {
  width: 200px;
  min-height: 200px;
  padding: 20px;
  border-radius: 2px;
  box-shadow:
    0 4px 6px rgba(0, 0, 0, 0.1),
    0 1px 3px rgba(0, 0, 0, 0.08);
  font-family: 'Patrick Hand', cursive;
  transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  cursor: pointer;
  position: relative;
}

/* 添加随机旋转 */
.sticky-note:nth-child(3n+1) {
  transform: rotate(-2deg);
}

.sticky-note:nth-child(3n+2) {
  transform: rotate(1deg);
}

.sticky-note:nth-child(3n) {
  transform: rotate(-1deg);
}

.sticky-note:hover {
  transform: rotate(0deg) scale(1.05);
  box-shadow:
    0 10px 20px rgba(0, 0, 0, 0.15),
    0 3px 6px rgba(0, 0, 0, 0.1);
  z-index: 10;
}

/* 网格纸容器 */
.grid-paper-container {
  background:
    repeating-linear-gradient(
      0deg,
      #f8f9fa 0px,
      #f8f9fa 1px,
      transparent 1px,
      transparent 20px
    ),
    repeating-linear-gradient(
      90deg,
      #f8f9fa 0px,
      #f8f9fa 1px,
      transparent 1px,
      transparent 20px
    ),
    #ffffff;
  padding: 48px;
  min-height: 100vh;
}
\`\`\`

**Tailwind CSS 配置**

如使用 Tailwind CSS，添加以下配置：

\`\`\`javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        caveat: ['Caveat', 'cursive'],
        patrick: ['Patrick Hand', 'cursive'],
        reenie: ['Reenie Beanie', 'cursive'],
      },
      colors: {
        'sticky-yellow': {
          light: '#fff9c4',
          DEFAULT: '#fff59d',
          dark: '#fff176',
        },
        'sticky-pink': {
          light: '#fce4ec',
          DEFAULT: '#f8bbd0',
          dark: '#f48fb1',
        },
        'sticky-blue': {
          light: '#e1f5fe',
          DEFAULT: '#b3e5fc',
          dark: '#81d4fa',
        },
        'sticky-green': {
          light: '#e8f5e9',
          DEFAULT: '#c8e6c9',
          dark: '#a5d6a7',
        },
        'sketch-text': {
          primary: '#2c3e50',
          secondary: '#34495e',
          muted: '#7f8c8d',
        },
      },
      boxShadow: {
        'sketch': '4px 4px 0 rgba(0, 0, 0, 0.1)',
        'sketch-lg': '6px 6px 0 rgba(0, 0, 0, 0.15)',
        'sticky': '0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08)',
        'sticky-hover': '0 10px 20px rgba(0, 0, 0, 0.15), 0 3px 6px rgba(0, 0, 0, 0.1)',
      },
    },
  },
}
\`\`\`

Tailwind 类示例：
\`\`\`html
<div class="font-patrick text-sketch-text-primary bg-white border-2 border-sketch-text-primary rounded-lg p-6 shadow-sketch hover:shadow-sketch-lg transition-all duration-300">
  <!-- 手绘卡片内容 -->
</div>

<button class="font-caveat text-xl font-bold bg-sticky-yellow border-2 border-sketch-text-primary rounded-xl px-6 py-3 shadow-sketch hover:shadow-sketch-lg active:shadow-none transition-all">
  Get Started
</button>
\`\`\`

**重要提示**
- 手写字体适合标题和短文本，长文本可读性较差
- SVG 滤镜会影响性能，避免在大量元素上同时使用
- 粘贴便签效果适合卡片式布局，不适合密集信息展示
- 旋转角度建议 -3deg ~ 3deg 之间，避免过于夸张
- Grid 纸背景适合浅色内容，深色内容需调整网格颜色
- 手绘风格适合创意、友好、非正式的项目
- 配色以柔和的粉彩色为主，避免高饱和度色彩
- 使用弹性缓动函数增强手绘的俏皮感
- 边框粗细建议 2px-3px，避免过细或过粗
- 阴影使用硬边阴影（offset shadow）而非模糊阴影


---

## English Version (en-US)

Please create a Hand-Drawn Sketch style interface using TailwindCSS, creating a warm and approachable visual experience through handwritten fonts, SVG filters, and casual lines.

**Core Design Requirements**

1. **Handwritten Font System**
   - Title font: Caveat (supports weights 400-700)
     \`\`\`css
     @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&display=swap');

     .hand-title {
       font-family: 'Caveat', cursive;
       font-size: 48px;
       font-weight: 700;
       letter-spacing: 0.02em;
     }
     \`\`\`

   - Body font: Patrick Hand (more readable)
     \`\`\`css
     @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');

     .hand-text {
       font-family: 'Patrick Hand', cursive;
       font-size: 16px;
       line-height: 1.6;
     }
     \`\`\`

   - Decorative font: Reenie Beanie (more casual)
     \`\`\`css
     @import url('https://fonts.googleapis.com/css2?family=Reenie+Beanie&display=swap');

     .hand-casual {
       font-family: 'Reenie Beanie', cursive;
       font-size: 20px;
     }
     \`\`\`

2. **SVG Hand-Drawn Filter Effects**
   - Use feTurbulence + feDisplacementMap to create hand-drawn wobble effect
   - Filter strength: scale 1.0-2.0 (higher values = more pronounced)
   - Base frequency: baseFrequency 0.03-0.08
   - Example:
     \`\`\`html
     <svg style="position: absolute; width: 0; height: 0;">
       <defs>
         <filter id="sketch-roughen">
           <feTurbulence type="turbulence" baseFrequency="0.05" numOctaves="2" result="turbulence"/>
           <feDisplacementMap in2="turbulence" in="SourceGraphic" scale="1.5" xChannelSelector="R" yChannelSelector="G"/>
         </filter>
       </defs>
     </svg>

     <div style="filter: url(#sketch-roughen);">
       <!-- Content with hand-drawn filter applied -->
     </div>
     \`\`\`

   - Performance tip: Apply filters only to key elements, avoid global usage

3. **Sticky Note Design**
   - Classic sticky note colors:
     \`\`\`css
     .sticky-note-yellow {
       background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
     }

     .sticky-note-pink {
       background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%);
     }

     .sticky-note-blue {
       background: linear-gradient(135deg, #e1f5fe 0%, #b3e5fc 100%);
     }

     .sticky-note-green {
       background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
     }
     \`\`\`

   - Sticky note 3D effect:
     \`\`\`css
     .sticky-note {
       box-shadow:
         0 4px 6px rgba(0, 0, 0, 0.1),
         0 1px 3px rgba(0, 0, 0, 0.08);
       transform: rotate(-2deg);  /* Random rotation -3deg ~ 3deg */
       transition: all 0.3s ease;
     }

     .sticky-note:hover {
       transform: rotate(0deg) scale(1.05);
       box-shadow:
         0 10px 20px rgba(0, 0, 0, 0.15),
         0 3px 6px rgba(0, 0, 0, 0.1);
       z-index: 10;
     }
     \`\`\`

4. **Grid Paper Background Effect**
   - Use repeating-linear-gradient to create grid paper
   - Grid spacing: 20px (recommended)
   - Example:
     \`\`\`css
     .grid-paper-bg {
       background:
         repeating-linear-gradient(
           0deg,
           #f8f9fa 0px,
           #f8f9fa 1px,
           transparent 1px,
           transparent 20px
         ),
         repeating-linear-gradient(
           90deg,
           #f8f9fa 0px,
           #f8f9fa 1px,
           transparent 1px,
           transparent 20px
         ),
         #ffffff;
     }
     \`\`\`

   - Dot grid background:
     \`\`\`css
     .dot-paper-bg {
       background-image: radial-gradient(circle, #d0d0d0 1px, transparent 1px);
       background-size: 20px 20px;
       background-color: #ffffff;
     }
     \`\`\`

5. **Hand-Drawn Borders and Lines**
   - Use border-image or SVG path to create irregular borders
   - Dashed hand-drawn effect:
     \`\`\`css
     .sketch-border {
       border: 2px dashed #2c3e50;
       border-radius: 4px;
       filter: url(#sketch-roughen);
     }
     \`\`\`

   - Wavy line divider:
     \`\`\`html
     <svg width="100%" height="20">
       <path d="M 0 10 Q 10 5, 20 10 T 40 10 T 60 10 T 80 10 T 100 10"
             stroke="#2c3e50" stroke-width="2" fill="none"
             filter="url(#sketch-roughen)"/>
     </svg>
     \`\`\`

6. **Hand-Drawn Icons and Arrows**
   - Use SVG path to draw irregular shapes
   - Example (hand-drawn checkbox):
     \`\`\`html
     <svg width="24" height="24" viewBox="0 0 24 24">
       <defs>
         <filter id="icon-sketch">
           <feTurbulence baseFrequency="0.08" numOctaves="1"/>
           <feDisplacementMap in="SourceGraphic" scale="1.2"/>
         </filter>
       </defs>
       <path d="M 4 12 L 9 17 L 20 6"
             stroke="#2c3e50" stroke-width="2.5"
             fill="none" stroke-linecap="round"
             filter="url(#icon-sketch)"/>
     </svg>
     \`\`\`

7. **Smooth Animation Effects**
   - Avoid rigid transitions, use elastic easing
   - Recommended easing: cubic-bezier(0.68, -0.55, 0.265, 1.55)
   - Example:
     \`\`\`css
     .sketch-animate {
       transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
     }

     .sketch-animate:hover {
       transform: scale(1.05) rotate(2deg);
     }
     \`\`\`

**Color Scheme (Warm and Friendly)**

Primary colors (sticky note colors):
- Yellow notes: #fff9c4, #fff59d, #fff176
- Pink notes: #fce4ec, #f8bbd0, #f48fb1
- Blue notes: #e1f5fe, #b3e5fc, #81d4fa
- Green notes: #e8f5e9, #c8e6c9, #a5d6a7

Text colors:
- Primary text: #2c3e50 (dark blue-gray)
- Secondary text: #34495e (medium blue-gray)
- Decorative text: #7f8c8d (light gray)

Hand-drawn lines:
- Black lines: #23303d
- Dark gray lines: #4a5568
- Decorative lines: #a0aec0

Background colors:
- Paper background: #ffffff, #fefefe, #fcfcfc
- Grid lines: #f8f9fa, #e9ecef

**Key CSS Class Examples**

\`\`\`css
/* Sketch Card */
.sketch-card {
  background: #ffffff;
  border: 2px solid #2c3e50;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 4px 4px 0 rgba(0, 0, 0, 0.1);
  filter: url(#sketch-roughen);
  font-family: 'Patrick Hand', cursive;
  transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.sketch-card:hover {
  transform: translateY(-4px) rotate(1deg);
  box-shadow: 6px 6px 0 rgba(0, 0, 0, 0.15);
}

/* Sketch Button */
.sketch-button {
  background: #fff176;
  border: 2px solid #2c3e50;
  border-radius: 12px;
  padding: 12px 24px;
  font-family: 'Caveat', cursive;
  font-size: 20px;
  font-weight: 700;
  color: #2c3e50;
  cursor: pointer;
  filter: url(#sketch-roughen);
  transition: all 0.3s ease;
  box-shadow: 3px 3px 0 rgba(0, 0, 0, 0.1);
}

.sketch-button:hover {
  background: #fff59d;
  transform: translate(-2px, -2px);
  box-shadow: 5px 5px 0 rgba(0, 0, 0, 0.15);
}

.sketch-button:active {
  transform: translate(1px, 1px);
  box-shadow: 2px 2px 0 rgba(0, 0, 0, 0.1);
}

/* Sketch Input */
.sketch-input {
  background: #ffffff;
  border: 2px dashed #4a5568;
  border-radius: 8px;
  padding: 12px 16px;
  font-family: 'Patrick Hand', cursive;
  font-size: 16px;
  color: #2c3e50;
  filter: url(#sketch-roughen);
  transition: all 0.3s ease;
}

.sketch-input:focus {
  outline: none;
  border-color: #2c3e50;
  border-style: solid;
  box-shadow: 0 0 0 4px rgba(44, 62, 80, 0.1);
}

.sketch-input::placeholder {
  color: #7f8c8d;
  font-style: italic;
}

/* Sticky Notes Container */
.sticky-notes-container {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  perspective: 1000px;
}

.sticky-note {
  width: 200px;
  min-height: 200px;
  padding: 20px;
  border-radius: 2px;
  box-shadow:
    0 4px 6px rgba(0, 0, 0, 0.1),
    0 1px 3px rgba(0, 0, 0, 0.08);
  font-family: 'Patrick Hand', cursive;
  transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  cursor: pointer;
  position: relative;
}

/* Add random rotation */
.sticky-note:nth-child(3n+1) {
  transform: rotate(-2deg);
}

.sticky-note:nth-child(3n+2) {
  transform: rotate(1deg);
}

.sticky-note:nth-child(3n) {
  transform: rotate(-1deg);
}

.sticky-note:hover {
  transform: rotate(0deg) scale(1.05);
  box-shadow:
    0 10px 20px rgba(0, 0, 0, 0.15),
    0 3px 6px rgba(0, 0, 0, 0.1);
  z-index: 10;
}

/* Grid Paper Container */
.grid-paper-container {
  background:
    repeating-linear-gradient(
      0deg,
      #f8f9fa 0px,
      #f8f9fa 1px,
      transparent 1px,
      transparent 20px
    ),
    repeating-linear-gradient(
      90deg,
      #f8f9fa 0px,
      #f8f9fa 1px,
      transparent 1px,
      transparent 20px
    ),
    #ffffff;
  padding: 48px;
  min-height: 100vh;
}
\`\`\`

**Tailwind CSS Configuration**

If using Tailwind CSS, add the following configuration:

\`\`\`javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        caveat: ['Caveat', 'cursive'],
        patrick: ['Patrick Hand', 'cursive'],
        reenie: ['Reenie Beanie', 'cursive'],
      },
      colors: {
        'sticky-yellow': {
          light: '#fff9c4',
          DEFAULT: '#fff59d',
          dark: '#fff176',
        },
        'sticky-pink': {
          light: '#fce4ec',
          DEFAULT: '#f8bbd0',
          dark: '#f48fb1',
        },
        'sticky-blue': {
          light: '#e1f5fe',
          DEFAULT: '#b3e5fc',
          dark: '#81d4fa',
        },
        'sticky-green': {
          light: '#e8f5e9',
          DEFAULT: '#c8e6c9',
          dark: '#a5d6a7',
        },
        'sketch-text': {
          primary: '#2c3e50',
          secondary: '#34495e',
          muted: '#7f8c8d',
        },
      },
      boxShadow: {
        'sketch': '4px 4px 0 rgba(0, 0, 0, 0.1)',
        'sketch-lg': '6px 6px 0 rgba(0, 0, 0, 0.15)',
        'sticky': '0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08)',
        'sticky-hover': '0 10px 20px rgba(0, 0, 0, 0.15), 0 3px 6px rgba(0, 0, 0, 0.1)',
      },
    },
  },
}
\`\`\`

Tailwind class example:
\`\`\`html
<div class="font-patrick text-sketch-text-primary bg-white border-2 border-sketch-text-primary rounded-lg p-6 shadow-sketch hover:shadow-sketch-lg transition-all duration-300">
  <!-- Sketch card content -->
</div>

<button class="font-caveat text-xl font-bold bg-sticky-yellow border-2 border-sketch-text-primary rounded-xl px-6 py-3 shadow-sketch hover:shadow-sketch-lg active:shadow-none transition-all">
  Get Started
</button>
\`\`\`

**Important Notes**
- Handwritten fonts are best for titles and short text, less readable for long content
- SVG filters impact performance, avoid using on many elements simultaneously
- Sticky note effects work best for card layouts, not suitable for dense information
- Rotation angles recommended between -3deg ~ 3deg, avoid exaggeration
- Grid paper backgrounds work best with light content, adjust grid color for dark content
- Hand-drawn style suits creative, friendly, informal projects
- Use soft pastel colors, avoid high saturation
- Use elastic easing functions to enhance playful feeling
-- Border thickness recommended 2px-3px, avoid too thin or thick
-- Use hard-edge shadows (offset shadows) rather than blurred shadows
