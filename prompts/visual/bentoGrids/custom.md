# Custom Prompt

## 中文版本 (zh-CN)

设计 Bento Grid 布局界面，受日式便当盒启发的不对称网格卡片系统，创造现代仪表板风格。

**核心视觉特征**：
- 不对称网格：卡片大小不一，占据 1x1、2x1、1x2、2x2 等不同网格单元
- 紧密排列：卡片之间间距统一（通常 16-24px），无浪费空间
- 圆角一致：所有卡片使用相同圆角（通常 12-16px），创造统一感
- 高对比度：主要卡片使用品牌色或深色突出，次要卡片使用中性色
- 功能分区：每个卡片代表独立功能模块（统计、图表、快捷操作等）
- 响应式重排：移动端自动转为单列，平板端 2 列，桌面端 3-4 列

**色彩系统**：
- 背景色：
  - 浅色主题：#f5f5f7, #fafafa, #f9fafb（淡灰色背景）
  - 深色主题：#0a0a0a, #1a1a1a, #212121（深灰色背景）
- 卡片配色：
  - 主卡片：品牌色背景（#3b82f6, #8b5cf6, #ec4899）+ 白色文字
  - 次卡片：白色/深灰（#fff or #2a2a2a）+ 深色/浅色文字
  - 中性卡片：浅灰/中灰（#f5f5f5 or #3a3a3a）
  - 强调卡片：渐变背景或图片背景
- 边框与分割线：
  - 浅色模式：#e5e5e5 或 rgba(0,0,0,0.1)
  - 深色模式：#333 或 rgba(255,255,255,0.1)
- 文字颜色：
  - 浅色模式：标题 #1a1a1a，正文 #4a4a4a
  - 深色模式：标题 #f5f5f5，正文 #a0a0a0

**网格系统技术实现**：
- CSS Grid 布局：
  ```css
  .bento-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    padding: 20px;
  }
  ```
- 跨列跨行：
  ```css
  .card-large {
    grid-column: span 2;
    grid-row: span 2;
  }
  .card-wide {
    grid-column: span 2;
    grid-row: span 1;
  }
  .card-tall {
    grid-column: span 1;
    grid-row: span 2;
  }
  ```
- 自适应列数：
  - 桌面端（> 1280px）：4 列，grid-template-columns: repeat(4, 1fr)
  - 平板端（768-1280px）：2-3 列
  - 移动端（< 768px）：1 列
- 最小卡片高度：min-height: 200px，确保内容不拥挤

**布局与组件**：
- Hero 卡片（2x2 或 2x1）：
  - 主推荐内容，占据最大空间
  - 背景使用品牌色渐变或高质量图片
  - 包含标题、描述、CTA 按钮
- 统计卡片（1x1）：
  - 显示关键指标（用户数、收入、增长率等）
  - 大数字 + 小标签 + 趋势图标
  - 简洁设计，突出数字
- 图表卡片（2x1 或 1x2）：
  - 内嵌迷你图表（折线图、柱状图、饼图）
  - 标题 + 图表 + 简短说明
- 快捷操作卡片（1x1）：
  - 图标 + 标签
  - 悬停时显示更多信息
  - 点击触发相应功能
- 内容预览卡片（1x1 或 2x1）：
  - 缩略图 + 标题 + 简短描述
  - 用于展示文章、产品、项目等
- 导航卡片：顶部固定或侧边栏，不占网格空间

**卡片设计规范**：
- 统一圆角：border-radius: 12-16px
- 统一阴影：
  - 浅色模式：box-shadow: 0 2px 8px rgba(0,0,0,0.08)
  - 深色模式：box-shadow: 0 2px 8px rgba(0,0,0,0.4)
- 内边距：padding: 20-32px（根据卡片大小调整）
- 卡片头部：标题 + 图标/操作按钮
- 卡片主体：内容区域，可滚动
- 卡片底部（可选）：操作按钮或链接

**动画与交互**：
- 悬停效果：
  - transform: translateY(-4px)（轻微浮起）
  - box-shadow 强度增加
  - 过渡时间 200-300ms
- 加载动画：
  - 卡片依次淡入，stagger delay 80-120ms
  - 使用 Intersection Observer 实现滚动加载
- 拖拽排序：
  - 允许用户自定义卡片位置
  - 使用 HTML5 Drag & Drop API 或库（如 react-grid-layout）
- 展开/折叠：
  - 点击卡片展开查看详细内容
  - 使用 modal 或原地展开

**响应式策略**：
- 移动端（< 768px）：
  - 单列布局，所有卡片 1x1
  - 主卡片放在顶部
  - 减少卡片内边距（16-20px）
  - 简化图表和内容
- 平板端（768-1024px）：
  - 2 列布局
  - 主卡片 2x2 或 2x1
  - 次要卡片 1x1 或 2x1
- 桌面端（1024-1440px）：
  - 3 列布局
  - 灵活使用 1x1、2x1、1x2、2x2 组合
- 超宽屏（> 1440px）：
  - 4 列布局
  - 更多空间展示更多卡片

**内容层次与视觉流**：
- 主要卡片：使用品牌色或图片背景，位于左上或中心
- 次要卡片：白色/深灰背景，环绕主卡片
- 信息密度：避免卡片过于拥挤，留白充足
- 视觉权重：通过大小、颜色、位置引导视线流动
- F 型阅读模式：重要内容放在左上和顶部

**性能优化**：
- 虚拟滚动：大量卡片时使用虚拟滚动（如 react-window）
- 懒加载：图片和图表按需加载
- CSS Grid 优化：使用 subgrid（支持的浏览器）减少嵌套
- 减少 DOM 节点：合并不必要的包裹元素
- GPU 加速：transform 属性触发硬件加速

**典型应用场景**：
- 仪表板/控制面板：展示业务数据、系统状态、关键指标
- 项目管理工具：任务卡片、看板视图、团队协作
- CMS 后台：内容管理、媒体库、设置面板
- 个人中心：用户资料、活动历史、偏好设置
- 作品集网站：项目展示、技能卡片、联系方式
- SaaS 产品：功能模块、快捷入口、通知中心
- 新闻/博客首页：文章预览、分类导航、热门推荐

**设计最佳实践**：
- 保持一致性：圆角、间距、阴影、字体统一
- 避免过度拥挤：卡片之间保持足够间距（16-24px）
- 突出重点：使用颜色、大小、位置强调主要内容
- 功能清晰：每个卡片代表单一功能，避免混杂
- 可扫描性：用户应能快速浏览并找到目标信息
- 无障碍性：键盘导航、屏幕阅读器支持、足够的颜色对比度


---

## English Version (en-US)

Design Bento Grid layout interfaces inspired by Japanese bento boxes - asymmetric grid card systems creating modern dashboard styles.

**Core Visual Characteristics**:
- Asymmetric grid: Cards of varying sizes occupying 1x1, 2x1, 1x2, 2x2 grid units
- Tight arrangement: Uniform spacing between cards (typically 16-24px) with no wasted space
- Consistent rounded corners: All cards use same border-radius (typically 12-16px) for unity
- High contrast: Primary cards use brand colors or dark tones, secondary cards use neutral colors
- Functional zones: Each card represents independent functional module (statistics, charts, quick actions, etc.)
- Responsive reflow: Mobile auto-converts to single column, tablet 2 columns, desktop 3-4 columns

**Color System**:
- Background colors:
  - Light theme: #f5f5f7, #fafafa, #f9fafb (light gray background)
  - Dark theme: #0a0a0a, #1a1a1a, #212121 (dark gray background)
- Card coloring:
  - Primary cards: Brand color backgrounds (#3b82f6, #8b5cf6, #ec4899) + white text
  - Secondary cards: White/dark gray (#fff or #2a2a2a) + dark/light text
  - Neutral cards: Light/medium gray (#f5f5f5 or #3a3a3a)
  - Emphasis cards: Gradient backgrounds or image backgrounds
- Borders & dividers:
  - Light mode: #e5e5e5 or rgba(0,0,0,0.1)
  - Dark mode: #333 or rgba(255,255,255,0.1)
- Text colors:
  - Light mode: Headings #1a1a1a, body #4a4a4a
  - Dark mode: Headings #f5f5f5, body #a0a0a0

**Grid System Technical Implementation**:
- CSS Grid layout:
  ```css
  .bento-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    padding: 20px;
  }
  ```
- Spanning columns/rows:
  ```css
  .card-large {
    grid-column: span 2;
    grid-row: span 2;
  }
  .card-wide {
    grid-column: span 2;
    grid-row: span 1;
  }
  .card-tall {
    grid-column: span 1;
    grid-row: span 2;
  }
  ```
- Adaptive column count:
  - Desktop (> 1280px): 4 columns, grid-template-columns: repeat(4, 1fr)
  - Tablet (768-1280px): 2-3 columns
  - Mobile (< 768px): 1 column
- Minimum card height: min-height: 200px to ensure content isn't cramped

**Layout & Components**:
- Hero card (2x2 or 2x1):
  - Main featured content occupying largest space
  - Background uses brand color gradient or high-quality image
  - Contains title, description, CTA button
- Statistics cards (1x1):
  - Display key metrics (user count, revenue, growth rate, etc.)
  - Large number + small label + trend icon
  - Simple design highlighting numbers
- Chart cards (2x1 or 1x2):
  - Embedded mini charts (line, bar, pie charts)
  - Title + chart + brief description
- Quick action cards (1x1):
  - Icon + label
  - Show more info on hover
  - Click to trigger corresponding function
- Content preview cards (1x1 or 2x1):
  - Thumbnail + title + brief description
  - Display articles, products, projects, etc.
- Navigation cards: Top fixed or sidebar, not occupying grid space

**Card Design Standards**:
- Uniform corners: border-radius: 12-16px
- Uniform shadows:
  - Light mode: box-shadow: 0 2px 8px rgba(0,0,0,0.08)
  - Dark mode: box-shadow: 0 2px 8px rgba(0,0,0,0.4)
- Internal padding: padding: 20-32px (adjusted by card size)
- Card header: Title + icon/action buttons
- Card body: Content area, scrollable
- Card footer (optional): Action buttons or links

**Animation & Interaction**:
- Hover effects:
  - transform: translateY(-4px) (slight lift)
  - Increased box-shadow intensity
  - 200-300ms transition
- Loading animation:
  - Cards fade in sequentially with stagger delay 80-120ms
  - Use Intersection Observer for scroll loading
- Drag & drop sorting:
  - Allow users to customize card positions
  - Use HTML5 Drag & Drop API or libraries (like react-grid-layout)
- Expand/collapse:
  - Click card to expand and view detailed content
  - Use modal or in-place expansion

**Responsive Strategy**:
- Mobile (< 768px):
  - Single column layout, all cards 1x1
  - Main card at top
  - Reduced card padding (16-20px)
  - Simplified charts and content
- Tablet (768-1024px):
  - 2 column layout
  - Main card 2x2 or 2x1
  - Secondary cards 1x1 or 2x1
- Desktop (1024-1440px):
  - 3 column layout
  - Flexible use of 1x1, 2x1, 1x2, 2x2 combinations
- Ultra-wide (> 1440px):
  - 4 column layout
  - More space for more cards

**Content Hierarchy & Visual Flow**:
- Primary cards: Use brand colors or image backgrounds, positioned top-left or center
- Secondary cards: White/dark gray backgrounds surrounding main card
- Information density: Avoid overcrowded cards, ample whitespace
- Visual weight: Guide eye flow through size, color, position
- F-shaped reading pattern: Important content in top-left and top area

**Performance Optimization**:
- Virtual scrolling: Use virtual scrolling for many cards (like react-window)
- Lazy loading: Load images and charts on demand
- CSS Grid optimization: Use subgrid (supported browsers) to reduce nesting
- Reduce DOM nodes: Merge unnecessary wrapper elements
- GPU acceleration: Transform properties trigger hardware acceleration

**Typical Use Cases**:
- Dashboards/control panels: Display business data, system status, key metrics
- Project management tools: Task cards, kanban views, team collaboration
- CMS backends: Content management, media libraries, settings panels
- User centers: User profiles, activity history, preference settings
- Portfolio websites: Project showcases, skill cards, contact info
- SaaS products: Feature modules, quick access, notification center
- News/blog homepages: Article previews, category navigation, popular recommendations

**Design Best Practices**:
- Maintain consistency: Uniform corners, spacing, shadows, fonts
- Avoid overcrowding: Maintain sufficient spacing between cards (16-24px)
- Highlight priorities: Use color, size, position to emphasize main content
- Clear functionality: Each card represents single function, avoid mixing
- Scannability: Users should quickly browse and find target information
- Accessibility: Keyboard navigation, screen reader support, sufficient color contrast
