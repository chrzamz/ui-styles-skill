# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名擅长排版系统与版面结构的资深 UI 设计师兼前端工程师，请生成一个与当前「报纸排版（Newspaper Typography）」家族展示界面风格高度接近的报纸风格 UI。
请使用 TailwindCSS 创建一个 Newspaper Typography 风格的界面，通过报头（Masthead）、首字下沉、多栏排版和细致的规则线来重现传统印刷媒体在网页中的阅读体验。

**核心设计要求**

1. **报纸标题栏（Masthead 系统）**
   - 使用大字号全大写衬线字体、极宽字距，强调品牌名称：
     \`\`\`css
     .newspaper-masthead {
       font-size: clamp(2.5rem, 6vw, 4.5rem);
       font-weight: 900;
       letter-spacing: 0.2em;
       text-transform: uppercase;
       text-align: center;
       border-top: 4px solid #000000;
       border-bottom: 4px solid #000000;
       padding: 1.25rem 0;
       font-family: 'Georgia', 'Times New Roman', 'Merriweather', serif;
     }
     \`\`\`
   - 可在报头上方增加版次与价格信息条（vol / price bar），字重较轻：
     \`\`\`css
     .newspaper-topbar {
       display: flex;
       justify-content: space-between;
       font-size: 0.875rem;
       color: #6B7280;
       margin-bottom: 0.5rem;
     }
     \`\`\`

2. **首字下沉（Drop Cap 系统）**
   - 首字母放大 3–5 倍，与正文共享同一行，制造传统印刷开头效果：
     \`\`\`css
     .drop-cap-paragraph {
       font-size: 0.9375rem;  /* 15px */
       line-height: 1.6;
       text-align: justify;
     }

     .drop-cap-paragraph::first-letter {
       float: left;
       font-size: 4.5rem;
       line-height: 0.85;
       font-weight: 900;
       margin-right: 0.2rem;
       margin-top: 0.1rem;
       color: #1E3A8A;
     }
     \`\`\`
   - 亦可使用带边框的强调版本：
     \`\`\`css
     .drop-cap-framed::first-letter {
       float: left;
       font-size: 3.5rem;
       line-height: 1;
       font-weight: 900;
       padding: 0.35rem 0.5rem;
       margin-right: 0.5rem;
       background: #1E3A8A;
       color: #FFFFFF;
       border: 3px solid #000000;
     }
     \`\`\`

3. **多栏布局（Multi-column Layout）**
   - 使用 CSS columns 或 grid 模拟 2–3 栏报纸内文：
     \`\`\`css
     .newspaper-columns {
       column-count: 3;
       column-gap: 2rem;                 /* 32px */
       column-rule: 1px solid #E5E7EB;   /* 栏间分隔线 */
       font-size: 0.9375rem;
       line-height: 1.6;
       text-align: justify;
     }

     .newspaper-columns p {
       margin-bottom: 1rem;
       break-inside: avoid;              /* 避免段落断裂 */
     }

     @media (max-width: 1024px) {
       .newspaper-columns { column-count: 2; }
     }

     @media (max-width: 768px) {
       .newspaper-columns { column-count: 1; }
     }
     \`\`\`

4. **标题层级与副标（Typographic Hierarchy）**
   - 为不同层级的标题定义清晰规则：
     \`\`\`css
     .headline-main {
       font-size: clamp(1.75rem, 3vw, 2.5rem);
       font-weight: 900;
       line-height: 1.2;
       color: #1E3A8A;
       border-bottom: 3px solid #1E3A8A;
       padding-bottom: 0.5rem;
       margin-bottom: 0.75rem;
     }

     .headline-section {
       font-size: 1.125rem;
       font-weight: 700;
       margin-bottom: 0.5rem;
       color: #111827;
     }

     .byline {
       font-size: 0.875rem;
       font-style: italic;
       color: #6B7280;
       margin-bottom: 0.75rem;
     }
     \`\`\`

5. **经典规则线与栏目盒（Rules & Boxes）**
   - 利用双线、点线强化分区与层次：
     \`\`\`css
     .section-divider {
       border-top: 3px double #000000;
       margin: 2rem 0;
     }

     .dotted-divider {
       border-bottom: 1px dotted #D1D5DB;
       margin: 1rem 0;
     }
     \`\`\`
   - 侧栏资讯盒（如「Inside Today」）：
     \`\`\`css
     .sidebar-box {
       border: 2px solid #1E3A8A;
       padding: 1rem;
       background: #F9FAFB;
     }

     .sidebar-title {
       font-size: 1.125rem;
       font-weight: 700;
       color: #1E3A8A;
       border-bottom: 2px solid #1E3A8A;
       padding-bottom: 0.5rem;
       margin-bottom: 0.75rem;
     }

     .sidebar-item {
       display: flex;
       justify-content: space-between;
       font-size: 0.875rem;
       padding: 0.4rem 0;
       border-bottom: 1px dotted #D1D5DB;
     }

     .sidebar-item:last-child {
       border-bottom: none;
     }
     \`\`\`

6. **页面布局与版心（Page Layout & Grid）**
   - 整体页面应有「纸张边距 + 版心」的结构，而不是满版卡片：
     \`\`\`css
     .newspaper-shell {
       min-height: 100vh;
       background: #E5E7EB;
       display: flex;
       align-items: flex-start;
       justify-content: center;
       padding: 2rem 1rem;
     }

     .newspaper-page {
       max-width: 1200px;
       width: 100%;
       margin: 0 auto;
       padding: 2rem;
       background: #FFFFFF;
       box-shadow: 0 0 30px rgba(0, 0, 0, 0.08);
       font-family: 'Georgia', 'Times New Roman', 'Merriweather', serif;
     }

     .newspaper-layout {
       display: grid;
       grid-template-columns: minmax(0, 2.5fr) minmax(0, 1fr);
       gap: 2rem;
       margin-top: 2rem;
     }

     @media (max-width: 1024px) {
       .newspaper-layout {
         grid-template-columns: 1fr;
       }
     }
     \`\`\`

7. **尾栏、次要文章与脚注区（Secondary Stories & Footer）**
   - 在页面底部使用 2–3 栏次要文章，配合双线或细线区隔：
     \`\`\`css
     .newspaper-secondary {
       display: grid;
       grid-template-columns: repeat(3, minmax(0, 1fr));
       gap: 2rem;
       padding-top: 2rem;
       border-top: 3px double #1E3A8A;
       margin-top: 2rem;
     }

     .secondary-article {
       font-size: 0.875rem;
       line-height: 1.6;
       text-align: justify;
     }

     .secondary-headline {
       font-size: 1.125rem;
       font-weight: 700;
       margin-bottom: 0.75rem;
       color: #1E3A8A;
       border-bottom: 2px solid #1E3A8A;
       padding-bottom: 0.25rem;
     }
     \`\`\`

**配色方案（经典报纸色系）**

主色调：
- 深蓝强调色：#1E3A8A, #2563EB
- 标题黑：#1F2937, #111827
- 正文灰：#374151, #4B5563

中性色与辅助色：
- 日期/说明灰：#6B7280, #9CA3AF
- 分隔线灰：#D1D5DB, #E5E7EB

背景色：
- 纸张米白：#FAF8F5, #F9FAFB
- 版心白：#FFFFFF
- 外围灰背景（页面衬底）：#E5E7EB

**关键 CSS 类示例**

\`\`\`css
/* 页面外壳（灰背景 + 居中纸张） */
.newspaper-shell {
  min-height: 100vh;
  background: #E5E7EB;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 2rem 1rem;
}

.newspaper-page {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding: 2rem;
  background: #FFFFFF;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.08);
  font-family: 'Georgia', 'Times New Roman', 'Merriweather', serif;
}

/* 报头区 */
.newspaper-header {
  border-top: 4px solid #000000;
  border-bottom: 4px solid #000000;
  padding: 1.25rem 0;
  margin-bottom: 2rem;
  text-align: center;
}

.newspaper-title {
  font-size: clamp(2.25rem, 5vw, 3.5rem);
  font-weight: 900;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #1E3A8A;
}

.newspaper-subtitle {
  font-size: 0.875rem;
  font-style: italic;
  color: #6B7280;
  margin-top: 0.5rem;
}

/* 主故事区 + 侧栏 */
.newspaper-layout {
  display: grid;
  grid-template-columns: minmax(0, 2.5fr) minmax(0, 1fr);
  gap: 2rem;
}

.newspaper-main-story {
  border-right: 2px solid #1E3A8A;
  padding-right: 2rem;
}

.newspaper-main-headline {
  font-size: clamp(1.75rem, 3vw, 2.5rem);
  font-weight: 900;
  line-height: 1.2;
  color: #1E3A8A;
  border-bottom: 3px solid #1E3A8A;
  padding-bottom: 0.5rem;
  margin-bottom: 0.75rem;
}

.newspaper-lead {
  font-size: 1.0625rem;
  font-weight: 500;
  margin-bottom: 1.5rem;
  line-height: 1.7;
}

.newspaper-columns-3 {
  column-count: 3;
  column-gap: 1.5rem;
  column-rule: 1px solid #E5E7EB;
  font-size: 0.9375rem;
  text-align: justify;
}
\`\`\`

**间距与字体系统（建议）**

- 基础间距单位：4px 或 8px，正文段落间距 16px。
- 报头与版心四周外边距：24–32px。
- 标题层级：
  - 报头：40–56px，字重 900，全大写。
  - 主标题：24–32px，字重 800–900。
  - 小标题：18–20px，字重 600–700。
- 正文字号：14–16px，行高 1.6–1.8。
- 装饰文字（Caption / Footer）：12–13px，行高 1.4–1.6。

**重要提示**
- 必须使用语义化 HTML 结构（header / main / article / aside / footer），避免仅用 <div> 堆叠。
- 正文对比度需达到 WCAG AA（正文灰 vs 米白背景 > 7:1），确保长文阅读舒适。
- 勿使用高饱和亮色区块或霓虹色，将主视觉重点放在排版与文字层次。
- 多栏布局下要避免图片或段落在栏内被任意分割，可使用 \`break-inside: avoid\`。
- Hover 动效需克制，主要用于连结下划线、颜色细微变化，不要让整个版面大幅位移或放大。
- 在 TailwindCSS 中，将重复的报头、栏宽、分隔线样式封装为自定义 utilities 或组件，方便跨页重用。


---

## English Version (en-US)

You are now a senior UI designer and front-end engineer specialising in editorial layout systems. Please generate a UI in the Newspaper Typography family that closely matches the current core “Newspaper Typography” style card.
Create a newspaper-style interface using TailwindCSS, combining masthead, drop caps, multi-column body text and classic rules to recreate a print-like reading experience on the web.

**Core Design Requirements**

1. **Masthead System**
   - Use uppercase serif type, very wide tracking and heavy weight for the newspaper name:
     \`\`\`css
     .newspaper-masthead {
       font-size: clamp(2.5rem, 6vw, 4.5rem);
       font-weight: 900;
       letter-spacing: 0.2em;
       text-transform: uppercase;
       text-align: center;
       border-top: 4px solid #000000;
       border-bottom: 4px solid #000000;
       padding: 1.25rem 0;
       font-family: 'Georgia', 'Times New Roman', 'Merriweather', serif;
     }
     \`\`\`
   - Add a compact top bar for volume/issue and price:
     \`\`\`css
     .newspaper-topbar {
       display: flex;
       justify-content: space-between;
       font-size: 0.875rem;
       color: #6B7280;
       margin-bottom: 0.5rem;
     }
     \`\`\`

2. **Drop Cap System**
   - The first letter of the leading paragraph should span 3–5 lines and share the same baseline as the body:
     \`\`\`css
     .drop-cap-paragraph {
       font-size: 0.9375rem;  /* 15px */
       line-height: 1.6;
       text-align: justify;
     }

     .drop-cap-paragraph::first-letter {
       float: left;
       font-size: 4.5rem;
       line-height: 0.85;
       font-weight: 900;
       margin-right: 0.2rem;
       margin-top: 0.1rem;
       color: #1E3A8A;
     }
     \`\`\`
   - Optionally, provide a framed drop cap variant for feature stories:
     \`\`\`css
     .drop-cap-framed::first-letter {
       float: left;
       font-size: 3.5rem;
       line-height: 1;
       font-weight: 900;
       padding: 0.35rem 0.5rem;
       margin-right: 0.5rem;
       background: #1E3A8A;
       color: #FFFFFF;
       border: 3px solid #000000;
     }
     \`\`\`

3. **Multi-column Layout**
   - Implement 2–3 column layouts for dense editorial content:
     \`\`\`css
     .newspaper-columns {
       column-count: 3;
       column-gap: 2rem;                 /* 32px */
       column-rule: 1px solid #E5E7EB;
       font-size: 0.9375rem;
       line-height: 1.6;
       text-align: justify;
     }

     .newspaper-columns p {
       margin-bottom: 1rem;
       break-inside: avoid;              /* Avoid awkward breaks */
     }

     @media (max-width: 1024px) {
       .newspaper-columns { column-count: 2; }
     }

     @media (max-width: 768px) {
       .newspaper-columns { column-count: 1; }
     }
     \`\`\`

4. **Typographic Hierarchy**
   - Define clear headline, subheadline and byline styles:
     \`\`\`css
     .headline-main {
       font-size: clamp(1.75rem, 3vw, 2.5rem);
       font-weight: 900;
       line-height: 1.2;
       color: #1E3A8A;
       border-bottom: 3px solid #1E3A8A;
       padding-bottom: 0.5rem;
       margin-bottom: 0.75rem;
     }

     .headline-section {
       font-size: 1.125rem;
       font-weight: 700;
       margin-bottom: 0.5rem;
       color: #111827;
     }

     .byline {
       font-size: 0.875rem;
       font-style: italic;
       color: #6B7280;
       margin-bottom: 0.75rem;
     }
     \`\`\`

5. **Rules and Sidebar Boxes**
   - Use classic rules to separate sections:
     \`\`\`css
     .section-divider {
       border-top: 3px double #000000;
       margin: 2rem 0;
     }

     .dotted-divider {
       border-bottom: 1px dotted #D1D5DB;
       margin: 1rem 0;
     }
     \`\`\`
   - Sidebar information such as “Inside Today” or “Market Watch”:
     \`\`\`css
     .sidebar-box {
       border: 2px solid #1E3A8A;
       padding: 1rem;
       background: #F9FAFB;
     }

     .sidebar-title {
       font-size: 1.125rem;
       font-weight: 700;
       color: #1E3A8A;
       border-bottom: 2px solid #1E3A8A;
       padding-bottom: 0.5rem;
       margin-bottom: 0.75rem;
     }

     .sidebar-item {
       display: flex;
       justify-content: space-between;
       font-size: 0.875rem;
       padding: 0.4rem 0;
       border-bottom: 1px dotted #D1D5DB;
     }

     .sidebar-item:last-child {
       border-bottom: none;
     }
     \`\`\`

6. **Page Layout and Grid**
   - The page should feel like a physical sheet with margins and a clear “body” area:
     \`\`\`css
     .newspaper-shell {
       min-height: 100vh;
       background: #E5E7EB;
       display: flex;
       align-items: flex-start;
       justify-content: center;
       padding: 2rem 1rem;
     }

     .newspaper-page {
       max-width: 1200px;
       width: 100%;
       margin: 0 auto;
       padding: 2rem;
       background: #FFFFFF;
       box-shadow: 0 0 30px rgba(0, 0, 0, 0.08);
       font-family: 'Georgia', 'Times New Roman', 'Merriweather', serif;
     }

     .newspaper-layout {
       display: grid;
       grid-template-columns: minmax(0, 2.5fr) minmax(0, 1fr);
       gap: 2rem;
       margin-top: 2rem;
     }

     @media (max-width: 1024px) {
       .newspaper-layout {
         grid-template-columns: 1fr;
       }
     }
     \`\`\`

7. **Secondary Stories and Footer**
   - Use a 2–3 column secondary section for shorter articles at the bottom:
     \`\`\`css
     .newspaper-secondary {
       display: grid;
       grid-template-columns: repeat(3, minmax(0, 1fr));
       gap: 2rem;
       padding-top: 2rem;
       border-top: 3px double #1E3A8A;
       margin-top: 2rem;
     }

     .secondary-article {
       font-size: 0.875rem;
       line-height: 1.6;
       text-align: justify;
     }

     .secondary-headline {
       font-size: 1.125rem;
       font-weight: 700;
       margin-bottom: 0.75rem;
       color: #1E3A8A;
       border-bottom: 2px solid #1E3A8A;
       padding-bottom: 0.25rem;
     }
     \`\`\`

**Color Scheme (Classic Newspaper)**

Primary colors:
- Deep blue accent: #1E3A8A, #2563EB
- Heading black: #1F2937, #111827
- Body gray: #374151, #4B5563

Neutrals and supporting tones:
- Caption gray: #6B7280, #9CA3AF
- Rule gray: #D1D5DB, #E5E7EB

Backgrounds:
- Paper cream: #FAF8F5, #F9FAFB
- Page white: #FFFFFF
- Outer shell gray: #E5E7EB

**Key CSS Class Examples**

\`\`\`css
/* Outer shell and page container */
.newspaper-shell {
  min-height: 100vh;
  background: #E5E7EB;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 2rem 1rem;
}

.newspaper-page {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding: 2rem;
  background: #FFFFFF;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.08);
  font-family: 'Georgia', 'Times New Roman', 'Merriweather', serif;
}

/* Header / Masthead */
.newspaper-header {
  border-top: 4px solid #000000;
  border-bottom: 4px solid #000000;
  padding: 1.25rem 0;
  margin-bottom: 2rem;
  text-align: center;
}

.newspaper-title {
  font-size: clamp(2.25rem, 5vw, 3.5rem);
  font-weight: 900;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #1E3A8A;
}

.newspaper-subtitle {
  font-size: 0.875rem;
  font-style: italic;
  color: #6B7280;
  margin-top: 0.5rem;
}

/* Layout grid */
.newspaper-layout {
  display: grid;
  grid-template-columns: minmax(0, 2.5fr) minmax(0, 1fr);
  gap: 2rem;
}

.newspaper-main-story {
  border-right: 2px solid #1E3A8A;
  padding-right: 2rem;
}

.newspaper-main-headline {
  font-size: clamp(1.75rem, 3vw, 2.5rem);
  font-weight: 900;
  line-height: 1.2;
  color: #1E3A8A;
  border-bottom: 3px solid #1E3A8A;
  padding-bottom: 0.5rem;
  margin-bottom: 0.75rem;
}

.newspaper-lead {
  font-size: 1.0625rem;
  font-weight: 500;
  margin-bottom: 1.5rem;
  line-height: 1.7;
}

.newspaper-columns-3 {
  column-count: 3;
  column-gap: 1.5rem;
  column-rule: 1px solid #E5E7EB;
  font-size: 0.9375rem;
  text-align: justify;
}
\`\`\`

**Spacing and Typography System (Recommended)**

- Base spacing unit: 4–8px; paragraphs typically use 16px bottom margin.
- Outer margins and page padding: 24–32px around the page content.
- Hierarchy:
  - Masthead: 40–56px, weight 900, uppercase serif.
  - Main headlines: 24–32px, weight 800–900.
  - Section headlines: 18–20px, weight 600–700.
  - Body: 14–16px, line-height 1.6–1.8.
  - Captions and footer: 12–13px, line-height 1.4–1.6.

**Important Notes**
- Always use semantic HTML (header / main / article / aside / footer); avoid flat <div> only layouts.
- Ensure body text contrast against the cream background meets WCAG AA (ratio > 7:1).
- Avoid bright, saturated brand colors; the focus should stay on typography and structure, not on flashy UI chrome.
- When using multi-column layouts, prevent headings or images from being split with \`break-inside: avoid\`.
- Hover effects should be subtle and text-focused (underlines, small color shifts), not heavy motion or scaling.
- In TailwindCSS, encapsulate repeated masthead, column and rule patterns into reusable utilities or components so entire sections can be regenerated consistently by the LLM.
