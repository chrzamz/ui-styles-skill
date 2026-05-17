# Custom Prompt

## 中文版本 (zh-CN)

设计极光玻璃风格界面，将北极光色彩与玻璃态设计相结合，创造梦幻般的视觉体验。

**核心视觉特征**：
- 极光渐变：模拟北极光的流动色带，使用多色渐变（绿-蓝-紫-粉）
- 玻璃态卡片：半透明毛玻璃效果，使用 backdrop-filter: blur(10-20px)
- 流动动画：极光带横向或波浪状流动，持续 10-20秒循环
- 渐变边框：卡片边框使用极光色彩渐变，增强玻璃质感
- 光泽反射：使用伪元素 ::before 创建高光反射效果
- 深色背景：深蓝或深紫背景衬托极光和玻璃效果

**极光色彩系统**：
- 经典极光配色：
  - 主绿色：#00ff88, #10b981, #059669（极光绿）
  - 青蓝色：#00d4ff, #0ea5e9, #0284c7（冰蓝）
  - 紫色调：#a855f7, #9333ea, #7c3aed（神秘紫）
  - 粉色调：#f472b6, #ec4899, #db2777（极光粉）
- 背景色彩：
  - 主背景：#0a0a1f, #0f0f1e, #0d0221（深蓝黑）
  - 渐变背景：#0a0a1f → #1a0b2e → #0f1729（深蓝紫径向）
- 玻璃卡片：
  - 半透明背景：rgba(255,255,255,0.05-0.1)
  - 边框：rgba(255,255,255,0.2) 或极光渐变边框
  - 阴影：0 8px 32px rgba(0,0,0,0.4)
- 文字颜色：
  - 标题：#ffffff 或 #f0f0f0（纯白）
  - 正文：#e0e0e0 或 #d0d0d0（柔和白）
  - 强调：极光色（#00ff88, #00d4ff, #a855f7）

**极光带技术实现**：
- 横向流动极光：
  ```css
  background: linear-gradient(
    90deg,
    #00ff88 0%,
    #00d4ff 25%,
    #a855f7 50%,
    #f472b6 75%,
    #00ff88 100%
  );
  background-size: 200% 100%;
  animation: aurora-flow 15s linear infinite;

  @keyframes aurora-flow {
    0% { background-position: 0% 50%; }
    100% { background-position: 200% 50%; }
  }
  ```
- 波浪状极光：
  - 使用 border-radius 创建波浪形状
  - 配合 transform: scaleY() 增加波动感
  - 使用 filter: blur(40-80px) 创造柔和扩散效果
- 多层极光叠加：
  - 3-4层不同速度和方向的极光带
  - 使用 mix-blend-mode: screen 或 lighten 叠加
  - z-index 分层，创造深度感

**玻璃态卡片设计**：
- 毛玻璃效果：
  ```css
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(15px) saturate(150%);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
  ```
- 极光边框：
  ```css
  border-image: linear-gradient(
    135deg,
    #00ff88, #00d4ff, #a855f7, #f472b6
  ) 1;
  ```
- 高光反射：
  ```css
  .glass-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 40%;
    background: linear-gradient(
      180deg,
      rgba(255,255,255,0.15) 0%,
      transparent 100%
    );
    border-radius: inherit;
  }
  ```
- 卡片层次：使用 transform: translateZ() 创建浮起效果

**布局与组件**：
- Hero 区域：
  - 大标题使用极光渐变文字（background-clip: text）
  - 背景横向流动的极光带，覆盖整个视口
  - 副标题和 CTA 使用玻璃卡片包裹
- 功能卡片网格：
  - 2-3列玻璃卡片，每个卡片不同的边框渐变角度
  - 卡片内部：图标/插图 + 标题 + 描述 + 链接
  - hover 时卡片 backdrop-filter 强度增加
- 数据展示区：
  - 玻璃态数据条或进度条，填充部分使用极光渐变
  - 统计数字大字号显示，配合极光色高亮
- CTA 按钮：
  - 实心极光渐变背景按钮
  - 或玻璃态边框按钮，hover 时填充极光渐变
- 导航栏：顶部固定玻璃态导航，背景极光带缓慢流动

**动画与交互**：
- 极光流动：
  - 横向流动：background-position 从 0% 到 200%
  - 波浪起伏：transform: translateY() 上下波动
  - 色相旋转：filter: hue-rotate() 缓慢变化（0deg → 30deg）
- 卡片悬停：
  - backdrop-filter: blur(20px)（从 15px 增强）
  - transform: translateY(-4px) translateZ(20px)（浮起效果）
  - box-shadow 强度增加
  - 边框渐变动画（边框颜色流动）
- 加载动画：
  - 极光带从透明淡入（opacity 0 → 1）
  - 卡片依次淡入，stagger delay 100-150ms
- 鼠标视差：
  - 极光带跟随鼠标微微移动
  - 玻璃卡片有轻微的 3D 倾斜效果

**极光图案变化**：
- 水平极光：最常见，从左到右流动
- 垂直极光：从上到下流动，适合侧边栏
- 对角极光：45度或135度角，更具动感
- 辐射极光：从中心向外扩散，使用 radial-gradient
- 波浪极光：使用 SVG path 或 CSS clip-path 创建波浪形状

**可读性保障**：
- 文字背景衬底：重要文字区域添加深色半透明背景
- 高对比度文字：标题纯白（#fff），正文至少 #e0e0e0
- 文字描边：text-shadow: 0 2px 8px rgba(0,0,0,0.8) 增强轮廓
- 玻璃卡片不宜过于透明：alpha 至少 0.08，确保内容可读
- 极光作装饰：主要内容区域避免直接放在极光带上

**性能优化**：
- 极光带使用 CSS 渐变：避免大图片或视频背景
- will-change: background-position, transform 提示浏览器优化
- 减少 backdrop-filter 使用范围：仅在卡片上使用，避免全页面
- 移动端简化：
  - 极光带静态或减速（30s → 60s）
  - 减少模糊半径（15px → 10px）
  - 禁用鼠标视差效果
- 使用 transform 代替 top/left 动画

**响应式策略**：
- 移动端（< 768px）：
  - 极光带垂直或对角方向，更适合竖屏
  - 简化动画或使用静态极光
  - 卡片单列排列
  - backdrop-filter: blur(10px)（减少模糊）
- 平板端（768px - 1024px）：
  - 保留主要极光流动效果
  - 2列卡片布局
  - backdrop-filter: blur(15px)
- 桌面端（> 1024px）：
  - 完整极光效果 + 复杂动画
  - 3列卡片布局
  - backdrop-filter: blur(20px)
  - 鼠标交互增强

**典型应用场景**：
- 科技产品着陆页：展示前沿科技、AI、云服务
- 加密货币/区块链：神秘感与未来感结合
- 游戏/娱乐平台：奇幻主题、魔法风格、未来世界
- 设计/创意工作室：展现独特审美和创意能力
- 音乐平台：配合音乐专辑封面色彩的极光效果
- SaaS 产品：现代、高端、专业的品牌形象
- 科幻主题网站：太空、未来城市、赛博朋克

**极光色彩组合建议**：
- 经典北极光：绿(#00ff88) → 青(#00d4ff) → 紫(#a855f7)
- 梦幻极光：粉(#f472b6) → 紫(#a855f7) → 蓝(#3b82f6)
- 冷色极光：蓝(#0ea5e9) → 青(#06b6d4) → 紫(#8b5cf6)
- 暖色极光：橙(#f97316) → 粉(#ec4899) → 紫(#a855f7)
- 单色极光：使用同一色相的不同明度（如 3 种绿色）


---

## English Version (en-US)

Design aurora glass style interfaces that combine northern lights colors with glassmorphism design to create dreamlike visual experiences.

**Core Visual Characteristics**:
- Aurora gradients: Simulate northern lights flowing color bands using multi-color gradients (green-blue-purple-pink)
- Glass cards: Semi-transparent frosted glass effect using backdrop-filter: blur(10-20px)
- Flow animation: Aurora bands flow horizontally or in waves for 10-20 second loops
- Gradient borders: Card borders use aurora color gradients to enhance glass texture
- Glossy reflections: Use ::before pseudo-element to create highlight reflection effects
- Dark backgrounds: Deep blue or deep purple backgrounds accentuate aurora and glass effects

**Aurora Color System**:
- Classic aurora palette:
  - Primary green: #00ff88, #10b981, #059669 (aurora green)
  - Cyan-blue: #00d4ff, #0ea5e9, #0284c7 (ice blue)
  - Purple tones: #a855f7, #9333ea, #7c3aed (mysterious purple)
  - Pink tones: #f472b6, #ec4899, #db2777 (aurora pink)
- Background colors:
  - Primary background: #0a0a1f, #0f0f1e, #0d0221 (deep blue-black)
  - Gradient background: #0a0a1f → #1a0b2e → #0f1729 (deep blue-purple radial)
- Glass cards:
  - Semi-transparent background: rgba(255,255,255,0.05-0.1)
  - Border: rgba(255,255,255,0.2) or aurora gradient border
  - Shadow: 0 8px 32px rgba(0,0,0,0.4)
- Text colors:
  - Headings: #ffffff or #f0f0f0 (pure white)
  - Body: #e0e0e0 or #d0d0d0 (soft white)
  - Emphasis: Aurora colors (#00ff88, #00d4ff, #a855f7)

**Aurora Band Technical Implementation**:
- Horizontal flowing aurora:
  ```css
  background: linear-gradient(
    90deg,
    #00ff88 0%,
    #00d4ff 25%,
    #a855f7 50%,
    #f472b6 75%,
    #00ff88 100%
  );
  background-size: 200% 100%;
  animation: aurora-flow 15s linear infinite;

  @keyframes aurora-flow {
    0% { background-position: 0% 50%; }
    100% { background-position: 200% 50%; }
  }
  ```
- Wave-shaped aurora:
  - Use border-radius to create wave shapes
  - Combine with transform: scaleY() for wave motion
  - Use filter: blur(40-80px) for soft diffusion
- Multi-layer aurora stacking:
  - 3-4 layers with different speeds and directions
  - Use mix-blend-mode: screen or lighten for blending
  - z-index layering for depth

**Glass Card Design**:
- Frosted glass effect:
  ```css
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(15px) saturate(150%);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
  ```
- Aurora border:
  ```css
  border-image: linear-gradient(
    135deg,
    #00ff88, #00d4ff, #a855f7, #f472b6
  ) 1;
  ```
- Highlight reflection:
  ```css
  .glass-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 40%;
    background: linear-gradient(
      180deg,
      rgba(255,255,255,0.15) 0%,
      transparent 100%
    );
    border-radius: inherit;
  }
  ```
- Card hierarchy: Use transform: translateZ() for floating effect

**Layout & Components**:
- Hero section:
  - Large title with aurora gradient text (background-clip: text)
  - Horizontal flowing aurora bands covering viewport
  - Subtitle and CTA wrapped in glass cards
- Feature card grid:
  - 2-3 column glass cards with different border gradient angles
  - Card internals: icon/illustration + title + description + link
  - Increase backdrop-filter intensity on hover
- Data display:
  - Glass data bars or progress bars with aurora gradient fill
  - Large statistics numbers with aurora color highlights
- CTA buttons:
  - Solid aurora gradient background buttons
  - Or glass border buttons that fill with aurora gradient on hover
- Navigation: Top fixed glass navbar with slowly flowing aurora background

**Animation & Interaction**:
- Aurora flow:
  - Horizontal flow: background-position from 0% to 200%
  - Wave motion: transform: translateY() up and down
  - Hue rotation: filter: hue-rotate() slow change (0deg → 30deg)
- Card hover:
  - backdrop-filter: blur(20px) (enhanced from 15px)
  - transform: translateY(-4px) translateZ(20px) (lift effect)
  - Increase box-shadow intensity
  - Border gradient animation (border color flow)
- Loading animation:
  - Aurora bands fade in from transparent (opacity 0 → 1)
  - Cards fade in sequentially with stagger delay 100-150ms
- Mouse parallax:
  - Aurora bands follow mouse with slight movement
  - Glass cards have subtle 3D tilt effect

**Aurora Pattern Variations**:
- Horizontal aurora: Most common, flows left to right
- Vertical aurora: Top to bottom flow, suitable for sidebars
- Diagonal aurora: 45 or 135 degree angle, more dynamic
- Radial aurora: Expand from center outward using radial-gradient
- Wave aurora: Use SVG path or CSS clip-path for wave shapes

**Readability Safeguards**:
- Text background backing: Add dark semi-transparent background for important text areas
- High contrast text: Headings pure white (#fff), body at least #e0e0e0
- Text stroke: text-shadow: 0 2px 8px rgba(0,0,0,0.8) enhances outline
- Glass cards shouldn't be too transparent: Alpha at least 0.08 for content readability
- Aurora as decoration: Avoid placing main content directly on aurora bands

**Performance Optimization**:
- Aurora bands use CSS gradients: Avoid large images or video backgrounds
- will-change: background-position, transform hints browser optimization
- Limit backdrop-filter scope: Use only on cards, avoid full page
- Mobile simplification:
  - Static aurora or slowed (30s → 60s)
  - Reduce blur radius (15px → 10px)
  - Disable mouse parallax
- Use transform instead of top/left animations

**Responsive Strategy**:
- Mobile (< 768px):
  - Aurora bands vertical or diagonal for portrait screens
  - Simplify animations or use static aurora
  - Single column card layout
  - backdrop-filter: blur(10px) (reduced blur)
- Tablet (768px - 1024px):
  - Retain main aurora flow effects
  - 2 column card layout
  - backdrop-filter: blur(15px)
- Desktop (> 1024px):
  - Full aurora effects + complex animations
  - 3 column card layout
  - backdrop-filter: blur(20px)
  - Enhanced mouse interactions

**Typical Use Cases**:
- Tech product landing pages: Showcase cutting-edge tech, AI, cloud services
- Cryptocurrency/blockchain: Combine mystery with futurism
- Gaming/entertainment platforms: Fantasy themes, magic style, future worlds
- Design/creative studios: Showcase unique aesthetics and creative capabilities
- Music platforms: Aurora effects matching album cover colors
- SaaS products: Modern, premium, professional brand image
- Sci-fi themed websites: Space, future cities, cyberpunk

**Aurora Color Combination Suggestions**:
- Classic northern lights: Green(#00ff88) → cyan(#00d4ff) → purple(#a855f7)
- Dreamy aurora: Pink(#f472b6) → purple(#a855f7) → blue(#3b82f6)
- Cool aurora: Blue(#0ea5e9) → cyan(#06b6d4) → purple(#8b5cf6)
- Warm aurora: Orange(#f97316) → pink(#ec4899) → purple(#a855f7)
- Monochrome aurora: Use different luminosities of same hue (e.g., 3 shades of green)
