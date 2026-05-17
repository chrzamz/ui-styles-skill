# Custom Prompt - Ink Wash Style

## 中文版本 (zh-CN)

你现在是一名资深 UI 设计师兼前端工程师，请生成一个与当前「Ink Wash（水墨）」样式卡展示界面风格高度接近的水墨风格 UI。

要求：保持整体视觉气质（宣纸白背景 + 墨色层次 + 书法字体 + 印章装饰 + 留白意境）与笔墨语言基本一致，只允许替换文案、图标和具体模块内容。输出使用语义化 HTML 结构和 TailwindCSS 风格的原子类（或等价的工具类方案）。

### 使用场景

- **场景**：文化艺术展览、茶道品牌、养生健康、诗词文学等需要传达东方美学与文化底蕴的产品
- **用户**：对传统文化有认同感的知识人群、艺术爱好者、文化从业者
- **目标**：在一个优雅的页面中展示品牌理念、作品展示、联系方式，营造宁静、诗意、深邃的氛围

### 整体布局结构

1. **外层容器**
   - 使用宣纸白（#F8F5F0）作为主背景色，叠加细腻的纸张纹理
   - 整体布局采用不对称构图，大量留白，营造呼吸感

2. **页面章节**
   - Hero 区域：大标题使用草书，副标题使用行书，周围留白充足
   - 内容区域：多个独立章节，每个章节有独立的主题和意境
   - 装饰元素：水墨山水、印章、毛笔笔触等点缀其间

3. **导航系统**
   - 侧边固定导航，使用竖排文字，中英双语
   - 当前章节用朱红色（印章红）高亮，其他章节半透明

### 书法字体系统（核心）

**Google Fonts 引入方式**：

```html
<!-- HTML 格式 -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Liu+Jian+Mao+Cao&family=Ma+Shan+Zheng&family=Zhi+Mang+Xing&family=ZCOOL+XiaoWei&family=ZCOOL+KuaiLe&family=Noto+Serif+SC:wght@300;700&display=swap" rel="stylesheet">
```

```jsx
// JSX/React 格式（推荐）
<>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
  <link href="https://fonts.googleapis.com/css2?family=Liu+Jian+Mao+Cao&family=Ma+Shan+Zheng&family=Zhi+Mang+Xing&family=ZCOOL+XiaoWei&family=ZCOOL+KuaiLe&family=Noto+Serif+SC:wght@300;700&display=swap" rel="stylesheet" />

  <style>{`
    /* 字体类定义 */
    .font-calligraphy-草 { font-family: 'Liu Jian Mao Cao', cursive; }
    .font-calligraphy-行 { font-family: 'Ma Shan Zheng', cursive; }
    .font-calligraphy-行草 { font-family: 'Zhi Mang Xing', cursive; }
    .font-body-楷 { font-family: 'ZCOOL XiaoWei', serif; }
    .font-seal { font-family: 'ZCOOL KuaiLe', cursive; }

    /* 竖排文字 */
    .vertical-text {
      writing-mode: vertical-rl;
      text-orientation: mixed;
    }
  `}</style>

  <div>{/* 页面内容 */}</div>
</>
```

**字体家族详解**：

1. **刘建毛草** - 草书（大标题）
   - 特点：笔势飞扬、气势磅礴
   - 示例：`<h1 className="font-calligraphy-草 text-8xl">水墨意境</h1>`

2. **马善政** - 行书（副标题、导航）
   - 特点：流畅端正、易读性强
   - 示例：`<h2 className="font-calligraphy-行 text-5xl">艺术致理</h2>`

3. **智蟒行** - 行草（诗句、装饰）
   - 特点：潇洒飘逸、富有韵律
   - 示例：`<p className="vertical-text font-calligraphy-行草 text-4xl">虚实相生 · 无画处皆成妙境</p>`

4. **站酷小薇** - 楷书（正文）
   - 特点：工整清秀、舒适阅读
   - 示例：`<p className="font-body-楷 text-2xl leading-relaxed">气韵乃水墨之魂...</p>`

5. **站酷快乐体** - 印章字体
   - 特点：方正厚重、篆刻风格
   - 示例：用于 Seal 组件内的竖排文字

**竖排文字实现**：
```css
.vertical-text {
  writing-mode: vertical-rl;
  text-orientation: mixed;
}
```

### 色彩与材质

1. **背景与纸张**
   - 页面背景：宣纸白 #F8F5F0，叠加细腻纹理
   - 区域变化：象牙白 #FFFFF0、米色 #FAF0E6 用于不同章节
   - 纹理：`url("https://www.transparenttextures.com/patterns/p6.png")`

2. **墨色系统（墨分五色）**
   - 焦墨：#1a1a1a - 最深的标题文字
   - 浓墨：#333333 - 主要文字
   - 重墨：#666666 - 次要内容
   - 淡墨：#999999 - 辅助说明
   - 清墨：#cccccc - 装饰线条

3. **点缀色彩**
   - 印章红：#C41E3A（朱红）- 强调、导航高亮、印章底色
   - 金色：#D4AF37 - 高端装饰、副标题点缀
   - 青绿：#2E8B57 - 山水点缀（可选）

### 视觉元素与装饰

1. **印章组件**
   - 方形或圆形，尺寸 40px～80px
   - 底色：印章红 #C41E3A
   - 文字：竖排、白色、站酷快乐体
   - 阴影：`inset 0 0 15px rgba(0,0,0,0.3)`
   - 轻微旋转：`transform: rotate(±3deg)`

2. **毛笔笔触（SVG）**
   - 使用 SVG filter 的 feTurbulence 模拟毛笔纹理
   - 笔画边缘不规则，带有自然的虚实变化

3. **水墨晕染**
   - 使用 feGaussianBlur + feColorMatrix 制作墨晕效果
   - 不透明度：0.3～0.6

4. **远山背景**
   - 使用 clip-path 和渐变创建山形
   - 多层叠加，透明度递减，模拟远近层次

### 留白与间距

- **章节间距**：py-48（约 192px）
- **段落间距**：mb-32（约 128px）
- **元素间距**：gap-12～gap-20（48px～80px）
- **整体原则**：画面中至少 40% 为留白区域

### 动效与交互

1. **动效曲线**
   - 墨迹晕染：`cubic-bezier(0.19, 1, 0.22, 1)`，2～3秒
   - 元素淡入：`ease-out`，2～4秒
   - 悬停反馈：`duration-700`～`duration-1000`

2. **特殊交互**
   - 点击墨滴效果：从点击位置扩散的墨晕动画
   - 滚动视差：章节切换时轻微的透明度变化
   - 印章悬停：旋转归正（从倾斜到水平）

3. **导航反馈**
   - 当前章节：朱红色高亮 + 下划线
   - 其他章节：淡墨色半透明
   - 英文小标签淡入淡出

### 输出要求

- 使用语义化 HTML：section、header、nav、main、footer 层次清晰
- 使用 TailwindCSS 原子类描述布局、间距、对齐和颜色
- **必须包含完整的字体引入代码**（`<link>` 标签或 CSS `@import`）
- 生成的 UI 在「宣纸背景 + 墨色层次 + 书法字体 + 印章装饰 + 留白意境」这些关键特征上，应与当前水墨样式卡的 demo 界面高度接近

---

## English Version (en-US)

You are a senior UI designer and front-end engineer. Generate an Ink Wash style UI that closely matches the current "Ink Wash" style card demo.

Keep the overall visual character (Xuan paper white background, ink gradation, calligraphy fonts, seal decorations, meaningful whitespace) and brush-ink language essentially unchanged. You may replace text, icons and specific module content, but not the global composition or Ink Wash visual style. Output semantic HTML and TailwindCSS-style utility classes (or an equivalent utility-first system).

### Usage Scenario

- **Context**: Cultural art exhibitions, tea ceremony brands, wellness & health, poetry & literature platforms that need to convey Eastern aesthetics and cultural depth
- **Users**: Knowledge workers and art enthusiasts with appreciation for traditional culture
- **Goal**: Display brand philosophy, artwork showcase, and contact information in an elegant page that creates a tranquil, poetic, and profound atmosphere

### Layout Structure

1. **Outer Container**
   - Use Xuan paper white (#F8F5F0) as main background with delicate paper texture overlay
   - Adopt asymmetric composition with generous whitespace for breathing room

2. **Page Sections**
   - Hero area: Cursive headings, running script subtitles, abundant surrounding whitespace
   - Content areas: Multiple independent sections, each with its own theme and mood
   - Decorative elements: Ink landscapes, seals, brush strokes scattered throughout

3. **Navigation System**
   - Fixed sidebar navigation with vertical text, bilingual labels
   - Current section highlighted in vermilion red, others semi-transparent

### Calligraphy Font System (Core)

**Google Fonts Integration**:

```html
<!-- HTML Format -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Liu+Jian+Mao+Cao&family=Ma+Shan+Zheng&family=Zhi+Mang+Xing&family=ZCOOL+XiaoWei&family=ZCOOL+KuaiLe&family=Noto+Serif+SC:wght@300;700&display=swap" rel="stylesheet">
```

```jsx
// JSX/React Format (Recommended)
<>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
  <link href="https://fonts.googleapis.com/css2?family=Liu+Jian+Mao+Cao&family=Ma+Shan+Zheng&family=Zhi+Mang+Xing&family=ZCOOL+XiaoWei&family=ZCOOL+KuaiLe&family=Noto+Serif+SC:wght@300;700&display=swap" rel="stylesheet" />

  <style>{`
    /* Font class definitions */
    .font-calligraphy-草 { font-family: 'Liu Jian Mao Cao', cursive; }
    .font-calligraphy-行 { font-family: 'Ma Shan Zheng', cursive; }
    .font-calligraphy-行草 { font-family: 'Zhi Mang Xing', cursive; }
    .font-body-楷 { font-family: 'ZCOOL XiaoWei', serif; }
    .font-seal { font-family: 'ZCOOL KuaiLe', cursive; }

    /* Vertical text */
    .vertical-text {
      writing-mode: vertical-rl;
      text-orientation: mixed;
    }
  `}</style>

  <div>{/* Page content */}</div>
</>
```

**Font Family Details**:

1. **Liu Jian Mao Cao (刘建毛草)** - Cursive Script (草书)
   - Usage: Main titles like "水墨意境"
   - Style: Free-flowing, bold, imposing
   - CSS: `.font-calligraphy-草 { font-family: 'Liu Jian Mao Cao', cursive; }`
   - Sizes: text-[13vw] or text-6xl to text-8xl
   - Example: `<h1 className="font-calligraphy-草 text-[13vw]">水墨意境</h1>`

2. **Ma Shan Zheng (马善政)** - Running Script (行书)
   - Usage: Subtitles, section headers, navigation
   - Style: Smooth, balanced, readable
   - CSS: `.font-calligraphy-行 { font-family: 'Ma Shan Zheng', cursive; }`
   - Sizes: text-3xl to text-7xl
   - Example: `<h2 className="font-calligraphy-行 text-5xl">艺术致理</h2>`

3. **Zhi Mang Xing (智蟒行)** - Semi-Cursive (行草)
   - Usage: Poetry, decorative text, side inscriptions
   - Style: Connected, elegant, rhythmic
   - CSS: `.font-calligraphy-行草 { font-family: 'Zhi Mang Xing', cursive; }`
   - Sizes: text-2xl to text-4xl
   - Example: `<div className="vertical-text font-calligraphy-行草 text-4xl">虚实相生 · 无画处皆成妙境</div>`

4. **ZCOOL XiaoWei (站酷小薇)** - Regular Script (楷书)
   - Usage: Body text, descriptions
   - Style: Neat, standard, comfortable reading
   - CSS: `.font-body-楷 { font-family: 'ZCOOL XiaoWei', serif; }`
   - Sizes: text-xl to text-3xl
   - Example: `<p className="font-body-楷 text-2xl">气韵乃水墨之魂...</p>`

5. **ZCOOL KuaiLe (站酷快乐体)** - Seal Script
   - Usage: Seal component text
   - Style: Square, heavy, engraving-like
   - CSS: `.font-seal { font-family: 'ZCOOL KuaiLe', cursive; }`
   - Used in Seal component with vertical text orientation

6. **Noto Serif SC (思源宋体)** - Serif
   - Usage: English headings, captions
   - Weights: 300, 700

### Colors and Materials

1. **Backgrounds**:
   - Xuan paper white: #F8F5F0
   - Ivory: #FFFFF0
   - Beige: #FAF0E6
   - Texture: `url("https://www.transparenttextures.com/patterns/p6.png")`

2. **Ink System (Five Shades)**:
   - Burnt ink: #1a1a1a (darkest titles)
   - Dense ink: #333333 (main text)
   - Heavy ink: #666666 (secondary content)
   - Light ink: #999999 (helper text)
   - Clear ink: #cccccc (decorative lines)

3. **Accent Colors**:
   - Seal red: #C41E3A (emphasis, navigation, seal backgrounds)
   - Gold: #D4AF37 (premium decorations)
   - Blue-green: #2E8B57 (landscape accents, optional)

### Visual Elements

1. **Seal Components**
   - Square or round, 40-80px
   - Background: #C41E3A (seal red)
   - Text: Vertical, white, ZCOOL KuaiLe font
   - Shadow: `inset 0 0 15px rgba(0,0,0,0.3)`
   - Slight rotation: `transform: rotate(±3deg)`

2. **Brush Strokes (SVG)**
   - Use feTurbulence filter for brush texture
   - Irregular edges with natural variation

3. **Ink Wash Effects**
   - feGaussianBlur + feColorMatrix
   - Opacity: 0.3-0.6

4. **Mountain Backgrounds**
   - clip-path with gradients
   - Layered with decreasing opacity
   - Increasing blur for depth

### Spacing & Whitespace

- Section spacing: py-48 (~192px)
- Paragraph spacing: mb-32 (~128px)
- Element gaps: gap-12 to gap-20 (48-80px)
- Overall: At least 40% whitespace

### Animations & Interactions

1. **Animation Curves**
   - Ink bleed: `cubic-bezier(0.19, 1, 0.22, 1)`, 2-3s
   - Fade in: `ease-out`, 2-4s
   - Hover: `duration-700` to `duration-1000`

2. **Special Interactions**
   - Click ink drop effect spreading from interaction point
   - Scroll parallax with opacity changes
   - Seal hover: Rotate to horizontal from tilted

3. **Navigation Feedback**
   - Current section: Vermilion highlight + underline
   - Other sections: Light ink semi-transparent
   - English labels fade in/out

### Output Requirements

- Use semantic HTML: section, header, nav, main, footer with clear hierarchy
- Use TailwindCSS utility classes for layout, spacing, alignment, colors
- **Must include complete font loading code** (`<link>` tags or CSS `@import`)
- Generated UI must preserve key traits: paper background, ink gradation, calligraphy fonts, seal decorations, meaningful whitespace

---
