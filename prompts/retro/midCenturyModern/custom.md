# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名资深 UI 设计师兼前端工程师,请生成一个与当前「Mid-Century Modern」核心样式卡展示界面风格高度接近的中世纪现代主义 UI。要求:结合 1950-60 年代的设计美学(有机几何、温暖木质色调、星爆图案)与现代 Web 布局,只允许替换文案和具体模块内容,不改变核心构图与配色气质。输出使用语义化 HTML 结构和 TailwindCSS 风格原子类(或等价工具类方案)。

【使用场景】
- 家居设计展示页、家具品牌官网、设计工作室作品集
- 时尚品牌、创意展览或艺术画廊的展示页面
- 需要呈现「复古优雅/温暖现代/有机美学」氛围的界面

【整体布局结构】
1. 背景与氛围
   - 使用温暖的米色、柔和白色作为主背景,营造开放通透的空间感
   - 可添加细微的纹理或渐变,模拟自然光线感
   - 底部或侧面可使用木质色调的装饰条,增加层次感

2. 主内容区域
   - 中央设置大标题区(粗体无衬线字体),下方为副标题和主行动按钮
   - 左右可放置特性卡片、产品展示或时间轴,布局采用非对称但平衡的设计
   - 充足的留白和呼吸空间,避免拥挤感

3. 装饰元素
   - 使用有机几何形状(圆形、椭圆)作为背景装饰
   - 星爆图案、抽象几何图案(三角形、平行四边形)作为视觉锚点
   - 细线条分隔,保持简洁优雅

【色彩与材质】
1. 主色系统
   - 主色调:温暖米色(#f5e6d3)、柔和白色(#fff)、深棕色(#2c2416)
   - 强调色:橙红色(#d97642)、芥末黄(#d4a574)、橄榄绿(#4a7c59)
   - 木质色:胡桃木(#6b5d4f)、柚木(#8b7355)
   - 辅助色:灰蓝色(#7d9ba8)、珊瑚粉(#e57a77)

2. 材质表现
   - 温暖的木质纹理,光滑的表面和哑光质感
   - 软阴影,避免过重的投影
   - 自然光线感,营造温暖友好的氛围

【排版系统】
1. 字体选择
   - 主标题:Futura、Century Gothic、Avenir 等无衬线字体
   - 正文:同系列字体或 Inter、SF Pro 等现代无衬线字体
   - 小标签:全大写字母,增加字距(letter-spacing: 2-3px)

2. 层次结构
   - H1:48-64px,粗体,行高 1.1-1.2
   - H2:32-40px,粗体,行高 1.2-1.3
   - H3:24-28px,中粗,行高 1.3-1.4
   - 正文:16-18px,常规,行高 1.6-1.8
   - 标签:12-14px,全大写,字距 2-3px

【组件与元素】
1. 按钮设计
   - 扁平化设计,无圆角或轻微圆角(2-4px)
   - 强调色背景(橙红色、芥末黄),白色文字
   - 悬停时轻微上移(translateY(-2px))和阴影增强
   - 全大写文字,字距 2px

2. 卡片设计
   - 白色或浅米色背景
   - 左侧彩色边框(4px)作为强调
   - 软阴影(0 4px 15px rgba(0,0,0,0.1))
   - 充足的内边距(padding: 30-40px)

3. 图标与装饰
   - 简洁的线条图标,笔触宽度 2px
   - 星爆图案作为装饰元素
   - 几何图形(圆形、三角形)作为背景点缀

【动效与交互】
1. 过渡动画
   - 平滑自然的过渡(transition: all 0.3s ease)
   - 轻微的悬停效果(transform: translateY(-2px))
   - 简洁的淡入淡出(opacity 变化)

2. 交互反馈
   - 清晰的视觉反馈,颜色轻微加深或变亮
   - 按钮悬停时阴影增强
   - 链接悬停时下划线或颜色变化

【布局要点】
1. 网格系统
   - 12 列或 24 列模块化网格
   - 栅格间距 20-30px
   - 响应式断点:sm(640px)、md(768px)、lg(1024px)、xl(1280px)

2. 空间运用
   - 充足的上下边距(section padding: 80-120px 0)
   - 元素间距(margin-bottom: 40-60px)
   - 非对称但平衡的布局,避免完全居中

3. 响应式设计
   - 移动端采用单列布局
   - 平板端 2 列布局
   - 桌面端 3-4 列布局或非对称网格

【氛围与调性】
- 温暖、友好、乐观的视觉氛围
- 平衡复古与现代感,既有怀旧情怀又不失当代审美
- 强调功能性和实用性,形式追随功能
- 体现战后时代的乐观主义和对美好生活的向往

---

## English Version (en-US)

You are a senior UI designer and front-end engineer. Please generate a Mid-Century Modern UI that closely matches the core style card display interface aesthetic. Requirements: Combine 1950s-60s design aesthetics (organic geometry, warm wood tones, starburst patterns) with modern Web layouts. Only replace copy and specific module content without changing the core composition and color palette. Output semantic HTML structure with TailwindCSS-style atomic classes (or equivalent utility class approach).

【Use Cases】
- Home design showcase pages, furniture brand websites, design studio portfolios
- Fashion brands, creative exhibitions, or art gallery display pages
- Interfaces requiring a "retro elegance/warm modern/organic aesthetic" atmosphere

【Overall Layout Structure】
1. Background & Atmosphere
   - Use warm beige, soft white as main background to create an open, airy spatial feel
   - Add subtle textures or gradients to simulate natural lighting
   - Bottom or side can use wood-toned decorative strips to add depth

2. Main Content Area
   - Central title area (bold sans-serif font), with subtitle and primary action button below
   - Left and right feature cards, product displays, or timelines with asymmetric yet balanced layouts
   - Ample whitespace and breathing room, avoiding crowding

3. Decorative Elements
   - Use organic geometric shapes (circles, ovals) as background decorations
   - Starburst patterns, abstract geometric patterns (triangles, parallelograms) as visual anchors
   - Thin line separators to maintain clean elegance

【Colors & Materials】
1. Color System
   - Primary: Warm beige (#f5e6d3), soft white (#fff), deep brown (#2c2416)
   - Accent: Orange-red (#d97642), mustard yellow (#d4a574), olive green (#4a7c59)
   - Wood tones: Walnut (#6b5d4f), teak (#8b7355)
   - Secondary: Gray-blue (#7d9ba8), coral pink (#e57a77)

2. Material Expression
   - Warm wood textures, smooth surfaces, and matte finishes
   - Soft shadows, avoid heavy drop shadows
   - Natural light sensation, creating a warm, friendly atmosphere

【Typography System】
1. Font Selection
   - Main titles: Futura, Century Gothic, Avenir, or similar sans-serif fonts
   - Body text: Same font family or modern sans-serif like Inter, SF Pro
   - Small labels: All-caps with increased letter spacing (letter-spacing: 2-3px)

2. Hierarchy
   - H1: 48-64px, bold, line-height 1.1-1.2
   - H2: 32-40px, bold, line-height 1.2-1.3
   - H3: 24-28px, semi-bold, line-height 1.3-1.4
   - Body: 16-18px, regular, line-height 1.6-1.8
   - Labels: 12-14px, all-caps, letter-spacing 2-3px

【Components & Elements】
1. Button Design
   - Flat design with no border-radius or slight radius (2-4px)
   - Accent color background (orange-red, mustard yellow), white text
   - Hover: slight upward movement (translateY(-2px)) and enhanced shadow
   - All-caps text with 2px letter spacing

2. Card Design
   - White or light beige background
   - Left colored border (4px) for emphasis
   - Soft shadow (0 4px 15px rgba(0,0,0,0.1))
   - Generous padding (30-40px)

3. Icons & Decorations
   - Simple line icons with 2px stroke width
   - Starburst patterns as decorative elements
   - Geometric shapes (circles, triangles) as background accents

【Animation & Interaction】
1. Transitions
   - Smooth, natural transitions (transition: all 0.3s ease)
   - Subtle hover effects (transform: translateY(-2px))
   - Simple fade in/out (opacity changes)

2. Interaction Feedback
   - Clear visual feedback with slight color darkening or brightening
   - Enhanced shadow on button hover
   - Underline or color change on link hover

【Layout Principles】
1. Grid System
   - 12 or 24 column modular grid
   - Grid gap 20-30px
   - Responsive breakpoints: sm(640px), md(768px), lg(1024px), xl(1280px)

2. Spacing
   - Generous vertical margins (section padding: 80-120px 0)
   - Element spacing (margin-bottom: 40-60px)
   - Asymmetric yet balanced layouts, avoid full centering

3. Responsive Design
   - Mobile: single column layout
   - Tablet: 2 column layout
   - Desktop: 3-4 column layout or asymmetric grid

【Atmosphere & Tone】
- Warm, friendly, optimistic visual atmosphere
- Balance retro and modern aesthetics, combining nostalgic charm with contemporary appeal
- Emphasize functionality and practicality, form follows function
- Reflect post-war optimism and aspiration for better living
