# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名资深 UI 设计师兼前端工程师，请生成一个与当前「Typography」核心样式卡展示界面风格高度接近的「排版驱动设计」风格 UI。
请使用 TailwindCSS 创建一个排版驱动设计风格的界面，**通过文字本身的视觉表现力传达信息**。

**核心设计要求**

1. **字体层级系统**
   - 主标题（H1）: \`text-5xl md:text-7xl font-black\` (48px-72px)
   - 副标题（H2）: \`text-3xl md:text-5xl font-bold\` (32px-48px)
   - 小标题（H3）: \`text-2xl md:text-3xl font-semibold\` (24px-32px)
   - 正文（Body）: \`text-base md:text-lg leading-relaxed\` (16px-18px, line-height: 1.75)
   - 辅助文字（Caption）: \`text-xs md:text-sm tracking-wider\` (12px-14px, letter-spacing: 0.05em)

2. **动态文字效果（Kinetic Typography）**
   - 使用 CSS 动画创建文字动态效果：
     \`\`\`css
     @keyframes text-pulse {
       0%, 100% { transform: scale(1); opacity: 1; }
       50% { transform: scale(1.1); opacity: 0.8; }
     }
     .kinetic-text {
       animation: text-pulse 2s ease-in-out infinite;
     }
     \`\`\`
   - 渐变文字效果：
     \`\`\`css
     .gradient-text {
       background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
       -webkit-background-clip: text;
       background-clip: text;
       -webkit-text-fill-color: transparent;
     }
     \`\`\`
   - 多层文字阴影营造发光效果：
     \`\`\`css
     .glow-text {
       text-shadow:
         0 0 10px rgba(102, 126, 234, 0.8),
         0 0 20px rgba(102, 126, 234, 0.6),
         0 0 40px rgba(102, 126, 234, 0.4);
     }
     \`\`\`

3. **编辑排版系统（Editorial Typography）**
   - 首字下沉效果：
     \`\`\`css
     .drop-cap::first-letter {
       float: left;
       font-size: 4em;
       line-height: 0.85;
       font-weight: 900;
       margin-right: 0.15rem;
       color: #1e3a8a;
     }
     \`\`\`
   - 多列布局（报纸风格）：
     \`\`\`css
     .newspaper-columns {
       column-count: 3;
       column-gap: 2rem;
       column-rule: 1px solid #e5e7eb;
       text-align: justify;
     }
     \`\`\`
   - 经典报纸分隔线：
     \`\`\`css
     .newspaper-divider {
       border-top: 3px double #000;
       border-bottom: 1px solid #000;
       padding: 1rem 0;
     }
     \`\`\`

4. **字体选择指南**
   - **衬线字体（Serif）** - 用于传统、权威、文学性内容：
     - Georgia, Times New Roman, Merriweather
     - TailwindCSS: \`font-serif\`
   - **无衬线字体（Sans-serif）** - 用于现代、简洁、科技感内容：
     - -apple-system, Helvetica, Inter, Poppins
     - TailwindCSS: \`font-sans\`
   - **等宽字体（Monospace）** - 用于代码、数据、技术内容：
     - Courier New, Monaco, Roboto Mono
     - TailwindCSS: \`font-mono\`

5. **排版节奏与间距**
   - 使用 8px 基础间距单位：\`space-y-8\` (32px), \`space-y-12\` (48px)
   - 段落间距：\`mb-6\` (24px) 或 \`mb-8\` (32px)
   - 行高（Leading）：
     - 标题：\`leading-tight\` (1.25) 或 \`leading-none\` (1)
     - 正文：\`leading-relaxed\` (1.625) 或 \`leading-loose\` (2)

6. **文字装饰与强调**
   - 文字描边效果：
     \`\`\`css
     .text-stroke {
       -webkit-text-stroke: 2px #000;
       -webkit-text-fill-color: transparent;
     }
     \`\`\`
   - 文字背景高亮：
     \`\`\`css
     .text-highlight {
       background: linear-gradient(180deg, transparent 50%, #fbbf24 50%);
       padding: 0 0.2em;
     }
     \`\`\`
   - 文字下划线动画：
     \`\`\`css
     .underline-animated {
       position: relative;
     }
     .underline-animated::after {
       content: '';
       position: absolute;
       bottom: 0;
       left: 0;
       width: 0;
       height: 2px;
       background: #3b82f6;
       transition: width 0.3s ease;
     }
     .underline-animated:hover::after {
       width: 100%;
     }
     \`\`\`

**配色方案**

**动态排版（Kinetic）配色：**
主色调（霓虹渐变）：
- 蓝紫色：#667eea, #764ba2
- 粉紫色：#ec4899, #8b5cf6
- 彩虹色：#3b82f6 (蓝), #ec4899 (粉), #fbbf24 (黄), #10b981 (绿)

背景与对比：
- 深色背景：#000000, #0f0f0f
- 高对比文字：#ffffff

**传统编辑（Editorial）配色：**
主色调（经典报纸）：
- 深蓝强调色：#1e3a8a, #1e40af
- 黑白基调：#000000, #ffffff
- 米白背景：#faf8f5, #f9fafb

中性色（灰度）：
- 标题黑：#1f2937, #111827
- 正文灰：#374151, #4b5563
- 辅助灰：#6b7280, #9ca3af

**关键 CSS 类示例**

\`\`\`css
/* 动态标题效果 */
.kinetic-heading {
  font-size: clamp(3rem, 10vw, 8rem);
  font-weight: 900;
  background: linear-gradient(45deg, #3b82f6, #ec4899, #fbbf24, #10b981);
  background-size: 300% 300%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradient-flow 3s ease infinite, text-float 2s ease-in-out infinite;
}

@keyframes gradient-flow {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

@keyframes text-float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

/* 打字机效果 */
.typewriter {
  display: inline-block;
  overflow: hidden;
  border-right: 2px solid #3b82f6;
  white-space: nowrap;
  animation: typing 3.5s steps(40, end), blink 0.75s step-end infinite;
}

@keyframes typing {
  from { width: 0; }
  to { width: 100%; }
}

@keyframes blink {
  0%, 50% { border-color: transparent; }
  51%, 100% { border-color: #3b82f6; }
}

/* 报纸标题栏（Masthead） */
.newspaper-masthead {
  font-size: clamp(2.5rem, 6vw, 5rem);
  font-weight: 900;
  text-align: center;
  letter-spacing: 0.2em;
  color: #1e3a8a;
  text-transform: uppercase;
  border-top: 4px solid #000;
  border-bottom: 4px solid #000;
  padding: 1.5rem 0;
  font-family: 'Georgia', 'Times New Roman', serif;
}

/* 首字下沉（Drop Cap） */
.editorial-dropcap::first-letter {
  float: left;
  font-size: 4.5rem;
  line-height: 0.85;
  font-weight: 900;
  color: #1e3a8a;
  margin-right: 0.15rem;
  margin-top: 0.1rem;
}

/* 分栏文字（Multi-column） */
.editorial-columns {
  column-count: 3;
  column-gap: 2rem;
  column-rule: 1px solid #e5e7eb;
  text-align: justify;
  font-size: 0.9375rem;
  line-height: 1.6;
}

.editorial-columns p {
  margin-bottom: 1rem;
  break-inside: avoid;
}
\`\`\`

**TailwindCSS 实用类组合**

**动态排版（Kinetic）：**
\`\`\`html
<!-- 主标题 -->
<h1 class="text-6xl md:text-8xl font-black bg-gradient-to-r from-blue-500 via-pink-500 to-yellow-500 bg-clip-text text-transparent animate-pulse">
  DYNAMIC TEXT
</h1>

<!-- 副标题（打字机效果） -->
<p class="text-xl md:text-2xl font-mono border-r-2 border-blue-500 pr-1 overflow-hidden whitespace-nowrap animate-typing">
  Next-Gen Typography Engine
</p>

<!-- 霓虹按钮 -->
<button class="px-8 py-4 text-lg font-bold bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl text-white shadow-lg shadow-blue-500/50 hover:shadow-xl hover:shadow-blue-500/70 hover:scale-105 transition-all">
  Get Started
</button>
\`\`\`

**传统编辑（Editorial）：**
\`\`\`html
<!-- 报纸标题栏 -->
<header class="border-t-4 border-b-4 border-black py-6 text-center">
  <h1 class="text-5xl md:text-7xl font-black tracking-[0.2em] text-blue-900 uppercase font-serif">
    THE DAILY CHRONICLE
  </h1>
  <p class="text-sm italic text-gray-600 mt-2">All The News Worth Reading</p>
  <p class="text-base text-gray-700 mt-3 pt-3 border-t border-gray-300">Monday, November 6, 2025</p>
</header>

<!-- 首字下沉文章 -->
<article class="prose prose-lg max-w-none">
  <p class="text-justify leading-relaxed">
    <span class="float-left text-7xl font-black leading-none mr-1 text-blue-900">I</span>
    n a groundbreaking development that is reshaping industries worldwide, technology companies have announced unprecedented innovations...
  </p>
</article>

<!-- 三栏布局 -->
<div class="columns-3 gap-8 column-rule column-rule-gray-300 text-justify text-sm leading-relaxed">
  <p>First column content...</p>
  <p>Second column content...</p>
  <p>Third column content...</p>
</div>
\`\`\`

**间距系统（8px 基础单位）**

- \`gap-2\` (8px) - 紧密间距
- \`gap-4\` (16px) - 小间距
- \`gap-6\` (24px) - 中间距
- \`gap-8\` (32px) - 标准间距
- \`gap-12\` (48px) - 大间距
- \`gap-16\` (64px) - 特大间距
- \`gap-24\` (96px) - 超大间距（章节分隔）

**重要提示**

1. **可读性优先**：
   - 正文行长度控制在 50-75 字符（约 600-800px）
   - 使用 \`max-w-prose\` 或 \`max-w-3xl\` 限制阅读宽度
   - 行高至少为字体大小的 1.5 倍（\`leading-normal\` 或更高）

2. **对比度要求**：
   - 正文文字与背景对比度至少 4.5:1（WCAG AA）
   - 大标题文字与背景对比度至少 3:1
   - 使用工具检查：https://webaim.org/resources/contrastchecker/

3. **响应式排版**：
   - 使用 \`clamp()\` 实现流畅字体缩放：\`font-size: clamp(1rem, 2.5vw, 1.5rem);\`
   - 移动端减少列数：\`md:columns-3\` → 小屏单列
   - 调整间距：\`space-y-6 md:space-y-12\`

4. **性能优化**：
   - 避免过度使用文字阴影和滤镜（影响渲染性能）
   - 动画优先使用 \`transform\` 和 \`opacity\`（硬件加速）
   - 使用 \`will-change: transform;\` 提示浏览器优化动画元素

5. **无障碍性（Accessibility）**：
   - 使用语义化 HTML（\`<h1>\`-\`<h6>\`, \`<p>\`, \`<article>\`）
   - 渐变文字需要设置 fallback 颜色
   - 支持 \`prefers-reduced-motion\` 媒体查询：
     \`\`\`css
     @media (prefers-reduced-motion: reduce) {
       * {
         animation-duration: 0.01ms !important;
         animation-iteration-count: 1 !important;
         transition-duration: 0.01ms !important;
       }
     }
     \`\`\`

6. **字体加载优化**：
   - 使用 \`font-display: swap;\` 避免 FOIT（Flash of Invisible Text）
   - 预加载关键字体：\`<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>\`
   - 优先使用系统字体栈减少加载时间


---

## English Version (en-US)

Please create a typography-driven design interface using TailwindCSS, where **the visual expressiveness of text itself conveys information**.

**Core Design Requirements**

1. **Font Hierarchy System**
   - Primary Heading (H1): \`text-5xl md:text-7xl font-black\` (48px-72px)
   - Secondary Heading (H2): \`text-3xl md:text-5xl font-bold\` (32px-48px)
   - Subheading (H3): \`text-2xl md:text-3xl font-semibold\` (24px-32px)
   - Body Text: \`text-base md:text-lg leading-relaxed\` (16px-18px, line-height: 1.75)
   - Caption Text: \`text-xs md:text-sm tracking-wider\` (12px-14px, letter-spacing: 0.05em)

2. **Kinetic Typography Effects**
   - Create dynamic text effects using CSS animations:
     \`\`\`css
     @keyframes text-pulse {
       0%, 100% { transform: scale(1); opacity: 1; }
       50% { transform: scale(1.1); opacity: 0.8; }
     }
     .kinetic-text {
       animation: text-pulse 2s ease-in-out infinite;
     }
     \`\`\`
   - Gradient text effects:
     \`\`\`css
     .gradient-text {
       background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
       -webkit-background-clip: text;
       background-clip: text;
       -webkit-text-fill-color: transparent;
     }
     \`\`\`
   - Multi-layer text shadows for glowing effects:
     \`\`\`css
     .glow-text {
       text-shadow:
         0 0 10px rgba(102, 126, 234, 0.8),
         0 0 20px rgba(102, 126, 234, 0.6),
         0 0 40px rgba(102, 126, 234, 0.4);
     }
     \`\`\`

3. **Editorial Typography System**
   - Drop cap effect:
     \`\`\`css
     .drop-cap::first-letter {
       float: left;
       font-size: 4em;
       line-height: 0.85;
       font-weight: 900;
       margin-right: 0.15rem;
       color: #1e3a8a;
     }
     \`\`\`
   - Multi-column layout (newspaper style):
     \`\`\`css
     .newspaper-columns {
       column-count: 3;
       column-gap: 2rem;
       column-rule: 1px solid #e5e7eb;
       text-align: justify;
     }
     \`\`\`
   - Classic newspaper divider:
     \`\`\`css
     .newspaper-divider {
       border-top: 3px double #000;
       border-bottom: 1px solid #000;
       padding: 1rem 0;
     }
     \`\`\`

4. **Font Selection Guide**
   - **Serif Fonts** - For traditional, authoritative, literary content:
     - Georgia, Times New Roman, Merriweather
     - TailwindCSS: \`font-serif\`
   - **Sans-serif Fonts** - For modern, clean, tech-focused content:
     - -apple-system, Helvetica, Inter, Poppins
     - TailwindCSS: \`font-sans\`
   - **Monospace Fonts** - For code, data, technical content:
     - Courier New, Monaco, Roboto Mono
     - TailwindCSS: \`font-mono\`

5. **Typographic Rhythm & Spacing**
   - Use 8px base spacing unit: \`space-y-8\` (32px), \`space-y-12\` (48px)
   - Paragraph spacing: \`mb-6\` (24px) or \`mb-8\` (32px)
   - Line height (Leading):
     - Headings: \`leading-tight\` (1.25) or \`leading-none\` (1)
     - Body text: \`leading-relaxed\` (1.625) or \`leading-loose\` (2)

6. **Text Decoration & Emphasis**
   - Text stroke effect:
     \`\`\`css
     .text-stroke {
       -webkit-text-stroke: 2px #000;
       -webkit-text-fill-color: transparent;
     }
     \`\`\`
   - Text background highlight:
     \`\`\`css
     .text-highlight {
       background: linear-gradient(180deg, transparent 50%, #fbbf24 50%);
       padding: 0 0.2em;
     }
     \`\`\`
   - Animated underline:
     \`\`\`css
     .underline-animated {
       position: relative;
     }
     .underline-animated::after {
       content: '';
       position: absolute;
       bottom: 0;
       left: 0;
       width: 0;
       height: 2px;
       background: #3b82f6;
       transition: width 0.3s ease;
     }
     .underline-animated:hover::after {
       width: 100%;
     }
     \`\`\`

**Color Schemes**

**Kinetic Typography Colors:**
Primary (Neon Gradients):
- Blue-Purple: #667eea, #764ba2
- Pink-Purple: #ec4899, #8b5cf6
- Rainbow: #3b82f6 (Blue), #ec4899 (Pink), #fbbf24 (Yellow), #10b981 (Green)

Background & Contrast:
- Dark backgrounds: #000000, #0f0f0f
- High contrast text: #ffffff

**Editorial Typography Colors:**
Primary (Classic Newspaper):
- Deep blue accent: #1e3a8a, #1e40af
- Black & white base: #000000, #ffffff
- Cream background: #faf8f5, #f9fafb

Neutral (Grayscale):
- Heading black: #1f2937, #111827
- Body gray: #374151, #4b5563
- Caption gray: #6b7280, #9ca3af

**Key CSS Class Examples**

\`\`\`css
/* Kinetic heading effect */
.kinetic-heading {
  font-size: clamp(3rem, 10vw, 8rem);
  font-weight: 900;
  background: linear-gradient(45deg, #3b82f6, #ec4899, #fbbf24, #10b981);
  background-size: 300% 300%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradient-flow 3s ease infinite, text-float 2s ease-in-out infinite;
}

@keyframes gradient-flow {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

@keyframes text-float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

/* Typewriter effect */
.typewriter {
  display: inline-block;
  overflow: hidden;
  border-right: 2px solid #3b82f6;
  white-space: nowrap;
  animation: typing 3.5s steps(40, end), blink 0.75s step-end infinite;
}

@keyframes typing {
  from { width: 0; }
  to { width: 100%; }
}

@keyframes blink {
  0%, 50% { border-color: transparent; }
  51%, 100% { border-color: #3b82f6; }
}

/* Newspaper masthead */
.newspaper-masthead {
  font-size: clamp(2.5rem, 6vw, 5rem);
  font-weight: 900;
  text-align: center;
  letter-spacing: 0.2em;
  color: #1e3a8a;
  text-transform: uppercase;
  border-top: 4px solid #000;
  border-bottom: 4px solid #000;
  padding: 1.5rem 0;
  font-family: 'Georgia', 'Times New Roman', serif;
}

/* Drop cap */
.editorial-dropcap::first-letter {
  float: left;
  font-size: 4.5rem;
  line-height: 0.85;
  font-weight: 900;
  color: #1e3a8a;
  margin-right: 0.15rem;
  margin-top: 0.1rem;
}

/* Multi-column text */
.editorial-columns {
  column-count: 3;
  column-gap: 2rem;
  column-rule: 1px solid #e5e7eb;
  text-align: justify;
  font-size: 0.9375rem;
  line-height: 1.6;
}

.editorial-columns p {
  margin-bottom: 1rem;
  break-inside: avoid;
}
\`\`\`

**TailwindCSS Utility Combinations**

**Kinetic Typography:**
\`\`\`html
<!-- Main heading -->
<h1 class="text-6xl md:text-8xl font-black bg-gradient-to-r from-blue-500 via-pink-500 to-yellow-500 bg-clip-text text-transparent animate-pulse">
  DYNAMIC TEXT
</h1>

<!-- Subtitle (typewriter effect) -->
<p class="text-xl md:text-2xl font-mono border-r-2 border-blue-500 pr-1 overflow-hidden whitespace-nowrap animate-typing">
  Next-Gen Typography Engine
</p>

<!-- Neon button -->
<button class="px-8 py-4 text-lg font-bold bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl text-white shadow-lg shadow-blue-500/50 hover:shadow-xl hover:shadow-blue-500/70 hover:scale-105 transition-all">
  Get Started
</button>
\`\`\`

**Editorial Typography:**
\`\`\`html
<!-- Newspaper masthead -->
<header class="border-t-4 border-b-4 border-black py-6 text-center">
  <h1 class="text-5xl md:text-7xl font-black tracking-[0.2em] text-blue-900 uppercase font-serif">
    THE DAILY CHRONICLE
  </h1>
  <p class="text-sm italic text-gray-600 mt-2">All The News Worth Reading</p>
  <p class="text-base text-gray-700 mt-3 pt-3 border-t border-gray-300">Monday, November 6, 2025</p>
</header>

<!-- Drop cap article -->
<article class="prose prose-lg max-w-none">
  <p class="text-justify leading-relaxed">
    <span class="float-left text-7xl font-black leading-none mr-1 text-blue-900">I</span>
    n a groundbreaking development that is reshaping industries worldwide, technology companies have announced unprecedented innovations...
  </p>
</article>

<!-- Three-column layout -->
<div class="columns-3 gap-8 column-rule column-rule-gray-300 text-justify text-sm leading-relaxed">
  <p>First column content...</p>
  <p>Second column content...</p>
  <p>Third column content...</p>
</div>
\`\`\`

**Spacing System (8px Base Unit)**

- \`gap-2\` (8px) - Tight spacing
- \`gap-4\` (16px) - Small spacing
- \`gap-6\` (24px) - Medium spacing
- \`gap-8\` (32px) - Standard spacing
- \`gap-12\` (48px) - Large spacing
- \`gap-16\` (64px) - Extra-large spacing
- \`gap-24\` (96px) - Section divider

**Important Notes**

1. **Readability First**:
   - Keep line length between 50-75 characters (~600-800px)
   - Use \`max-w-prose\` or \`max-w-3xl\` to limit reading width
   - Line height should be at least 1.5x font size (\`leading-normal\` or higher)

2. **Contrast Requirements**:
   - Body text vs background: minimum 4.5:1 (WCAG AA)
   - Large text vs background: minimum 3:1
   - Check with: https://webaim.org/resources/contrastchecker/

3. **Responsive Typography**:
   - Use \`clamp()\` for fluid font scaling: \`font-size: clamp(1rem, 2.5vw, 1.5rem);\`
   - Reduce columns on mobile: \`md:columns-3\` → single column on small screens
   - Adjust spacing: \`space-y-6 md:space-y-12\`

4. **Performance Optimization**:
   - Avoid excessive text-shadow and filters (impacts rendering)
   - Prefer \`transform\` and \`opacity\` for animations (hardware-accelerated)
   - Use \`will-change: transform;\` to hint browser about animated elements

5. **Accessibility**:
   - Use semantic HTML (\`<h1>\`-\`<h6>\`, \`<p>\`, \`<article>\`)
   - Provide fallback colors for gradient text
   - Support \`prefers-reduced-motion\` media query:
     \`\`\`css
     @media (prefers-reduced-motion: reduce) {
       * {
         animation-duration: 0.01ms !important;
         animation-iteration-count: 1 !important;
         transition-duration: 0.01ms !important;
       }
     }
     \`\`\`

6. **Font Loading Optimization**:
   - Use \`font-display: swap;\` to avoid FOIT (Flash of Invisible Text)
   - Preload critical fonts: \`<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>\`
   - Prefer system font stacks to reduce load time
