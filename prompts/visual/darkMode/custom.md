# Custom Prompt

## 中文版本 (zh-CN)

设计专业深色模式界面，减少视觉疲劳，提供舒适的长时间阅读体验。

**核心设计原则**：
- 真黑与炭灰：纯黑 (#000) 仅用于 OLED 省电，一般使用 #0a0a0a, #121212, #1a1a1a 等深灰色
- 层级分离：通过不同深度的灰色创建视觉层次，避免使用鲜艳边框
- 降低对比度：白色文字使用 #e5e5e5 或 #d0d0d0，而非刺眼的 #fff
- 柔和阴影：使用 box-shadow 创建深色阴影，如 0 4px 12px rgba(0,0,0,0.5)
- 色彩去饱和：品牌色降低饱和度 20-30%，避免过于刺眼（如 #60a5fa 替代 #3b82f6）
- 避免纯白背景：卡片背景使用 #1e1e1e, #252525，而非 #fff

**色彩系统**：
- 背景层次：
  - 基础背景：#0a0a0a（页面底色）
  - 次级背景：#141414（侧边栏、面板）
  - 卡片背景：#1e1e1e（内容卡片）
  - 浮层背景：#282828（模态框、菜单）
- 文字颜色：
  - 主文字：#e5e5e5（正文内容）
  - 次要文字：#a0a0a0（辅助说明）
  - 禁用文字：#666666（不可用状态）
  - 高亮文字：#ffffff（需要强调的内容）
- 品牌色适配：
  - 蓝色：#60a5fa（原 #3b82f6 降低饱和度）
  - 绿色：#4ade80（原 #10b981 提高亮度）
  - 红色：#f87171（原 #ef4444 降低饱和度）
  - 黄色：#fbbf24（原 #f59e0b 避免太亮）
- 边框与分割线：
  - 细边框：#2a2a2a（1px 线条）
  - 强调边框：#3a3a3a（焦点状态）
  - 分割线：rgba(255,255,255,0.1)

**布局与组件**：
- 顶部导航：深灰背景（#141414）+ 轻微底部阴影，避免纯黑
- 侧边栏：比主区域稍深（#0f0f0f），使用内阴影分隔
- 内容卡片：#1e1e1e 背景 + 8-12px 圆角 + 深色阴影
- 表格设计：斑马纹使用 #1a1a1a 和 #202020 交替，边框 #2a2a2a
- 按钮状态：
  - 默认：#2a2a2a 背景 + #e5e5e5 文字
  - 悬停：#3a3a3a 背景 + 轻微外发光
  - 激活：品牌色背景（如 #60a5fa）+ #000 文字
  - 禁用：#1a1a1a 背景 + #666 文字
- 表单输入：
  - 背景：#1a1a1a
  - 边框：#2a2a2a（默认）→ #60a5fa（焦点）
  - 文字：#e5e5e5
  - 占位符：#666

**对比度与可读性**：
- 正文文字：至少 4.5:1 对比度（#e5e5e5 on #0a0a0a = 12.6:1）
- 大号文字：至少 3:1 对比度（18px+ 或 14px+ 粗体）
- UI 元素：至少 3:1 对比度（按钮、图标）
- 避免低对比度：#888 on #222 仅 3.3:1，不适合小字
- 测试工具：使用 WebAIM Contrast Checker 验证所有颜色组合

**焦点与交互状态**：
- 焦点指示器：2px 蓝色外边框 + 4px 偏移，确保键盘导航可见
- 悬停状态：背景颜色提亮 5-10%，添加微妙 transition（150-200ms）
- 激活状态：轻微 scale(0.98) 变换，模拟按压效果
- 选中状态：品牌色背景（如 #60a5fa）+ 深色文字（#000）
- 禁用状态：降低透明度至 0.5，cursor: not-allowed

**阴影系统**：
- 微阴影：0 1px 3px rgba(0,0,0,0.4)（轻微浮起）
- 小阴影：0 2px 8px rgba(0,0,0,0.5)（卡片）
- 中阴影：0 4px 12px rgba(0,0,0,0.6)（模态框）
- 大阴影：0 8px 24px rgba(0,0,0,0.7)（下拉菜单）
- 悬停增强：阴影扩散半径 +4px，透明度 +0.1

**图像与图标处理**：
- 图片滤镜：brightness(0.9) 降低亮度，避免刺眼
- 图标颜色：使用 #a0a0a0 或 #e5e5e5，避免纯白
- SVG 适配：通过 CSS filter 或 fill 属性调整颜色
- Logo 处理：深色背景版本使用浅色 Logo 变体
- 占位图：使用深灰色渐变（#1a1a1a → #2a2a2a）

**动画与过渡**：
- 颜色过渡：transition: background-color 200ms ease, color 200ms ease
- 阴影过渡：transition: box-shadow 300ms ease
- 避免闪烁：深色模式切换使用淡入淡出（300-500ms）
- 微交互：悬停时轻微 translateY(-2px) 提升效果
- 尊重用户偏好：@media (prefers-reduced-motion: reduce) 禁用动画

**响应式深色模式**：
- 系统自适应：@media (prefers-color-scheme: dark) 自动应用
- 手动切换：提供深色/浅色/自动三种模式选择
- 本地存储：localStorage.setItem('theme', 'dark') 保存用户偏好
- 无闪烁加载：在 <head> 中内联脚本预加载主题
- CSS 变量：使用 CSS 自定义属性方便主题切换

**特殊场景处理**：
- 代码编辑器：使用 VS Code Dark+ 或 Monokai 配色
- 数据可视化：使用高对比度色板，避免深色背景上的深色线条
- 图表颜色：提高饱和度和亮度，确保在深色背景上清晰
- 通知消息：成功/警告/错误使用去饱和色 + 深色背景
- 加载状态：使用骨架屏或 spinner，颜色匹配深色主题

**性能优化**：
- OLED 省电：使用更多 #000 纯黑背景，减少像素发光
- GPU 加速：transform: translateZ(0) 优化动画性能
- 减少重绘：避免频繁改变 box-shadow 和 background-color
- 图片优化：使用 WebP 格式，深色模式下降低图片亮度

**典型应用场景**：
- 生产力工具：代码编辑器、笔记应用、项目管理工具
- 内容平台：阅读应用、新闻网站、社交媒体
- 开发者工具：控制台、API 文档、管理后台
- 金融应用：股票交易、加密货币、数据监控面板
- 娱乐应用：视频平台、音乐播放器、游戏界面


---

## English Version (en-US)

Design professional dark mode interfaces that reduce visual fatigue and provide comfortable long-term reading experiences.

**Core Design Principles**:
- True black vs charcoal: Pure black (#000) only for OLED power saving, generally use deep grays like #0a0a0a, #121212, #1a1a1a
- Layer separation: Create visual hierarchy through different depths of gray, avoid vibrant borders
- Reduced contrast: White text uses #e5e5e5 or #d0d0d0 instead of harsh #fff
- Soft shadows: Use box-shadow to create dark shadows like 0 4px 12px rgba(0,0,0,0.5)
- Desaturated colors: Reduce brand color saturation by 20-30% to avoid being too harsh (e.g., #60a5fa instead of #3b82f6)
- Avoid pure white backgrounds: Card backgrounds use #1e1e1e, #252525 instead of #fff

**Color System**:
- Background hierarchy:
  - Base background: #0a0a0a (page base)
  - Secondary background: #141414 (sidebar, panels)
  - Card background: #1e1e1e (content cards)
  - Floating background: #282828 (modals, menus)
- Text colors:
  - Primary text: #e5e5e5 (body content)
  - Secondary text: #a0a0a0 (supporting text)
  - Disabled text: #666666 (unavailable states)
  - Highlight text: #ffffff (emphasized content)
- Brand color adaptation:
  - Blue: #60a5fa (desaturated from #3b82f6)
  - Green: #4ade80 (brightened from #10b981)
  - Red: #f87171 (desaturated from #ef4444)
  - Yellow: #fbbf24 (from #f59e0b to avoid being too bright)
- Borders & dividers:
  - Thin borders: #2a2a2a (1px lines)
  - Emphasis borders: #3a3a3a (focus states)
  - Dividers: rgba(255,255,255,0.1)

**Layout & Components**:
- Top navigation: Dark gray background (#141414) + subtle bottom shadow, avoid pure black
- Sidebar: Slightly darker than main area (#0f0f0f), use inner shadow for separation
- Content cards: #1e1e1e background + 8-12px border-radius + dark shadow
- Table design: Zebra stripes alternating between #1a1a1a and #202020, borders #2a2a2a
- Button states:
  - Default: #2a2a2a background + #e5e5e5 text
  - Hover: #3a3a3a background + subtle outer glow
  - Active: Brand color background (like #60a5fa) + #000 text
  - Disabled: #1a1a1a background + #666 text
- Form inputs:
  - Background: #1a1a1a
  - Border: #2a2a2a (default) → #60a5fa (focus)
  - Text: #e5e5e5
  - Placeholder: #666

**Contrast & Readability**:
- Body text: At least 4.5:1 contrast (#e5e5e5 on #0a0a0a = 12.6:1)
- Large text: At least 3:1 contrast (18px+ or 14px+ bold)
- UI elements: At least 3:1 contrast (buttons, icons)
- Avoid low contrast: #888 on #222 only 3.3:1, unsuitable for small text
- Testing tools: Use WebAIM Contrast Checker to verify all color combinations

**Focus & Interaction States**:
- Focus indicator: 2px blue outer border + 4px offset, ensure keyboard navigation visibility
- Hover state: Lighten background by 5-10%, add subtle transition (150-200ms)
- Active state: Slight scale(0.98) transform simulating press effect
- Selected state: Brand color background (like #60a5fa) + dark text (#000)
- Disabled state: Reduce opacity to 0.5, cursor: not-allowed

**Shadow System**:
- Micro shadow: 0 1px 3px rgba(0,0,0,0.4) (slight elevation)
- Small shadow: 0 2px 8px rgba(0,0,0,0.5) (cards)
- Medium shadow: 0 4px 12px rgba(0,0,0,0.6) (modals)
- Large shadow: 0 8px 24px rgba(0,0,0,0.7) (dropdowns)
- Hover enhancement: Shadow spread radius +4px, opacity +0.1

**Image & Icon Treatment**:
- Image filters: brightness(0.9) to reduce brightness, avoid harshness
- Icon colors: Use #a0a0a0 or #e5e5e5, avoid pure white
- SVG adaptation: Adjust colors via CSS filter or fill attribute
- Logo treatment: Use light logo variants for dark backgrounds
- Placeholder images: Use dark gray gradients (#1a1a1a → #2a2a2a)

**Animation & Transitions**:
- Color transitions: transition: background-color 200ms ease, color 200ms ease
- Shadow transitions: transition: box-shadow 300ms ease
- Avoid flickering: Dark mode toggle uses fade in/out (300-500ms)
- Micro-interactions: Slight translateY(-2px) on hover for lift effect
- Respect user preferences: @media (prefers-reduced-motion: reduce) disables animations

**Responsive Dark Mode**:
- System adaptive: @media (prefers-color-scheme: dark) auto-applies
- Manual toggle: Provide dark/light/auto three mode options
- Local storage: localStorage.setItem('theme', 'dark') saves user preference
- Flash-free loading: Inline script in <head> to preload theme
- CSS variables: Use CSS custom properties for easy theme switching

**Special Scenarios**:
- Code editors: Use VS Code Dark+ or Monokai color schemes
- Data visualization: Use high-contrast palettes, avoid dark lines on dark backgrounds
- Chart colors: Increase saturation and brightness for clarity on dark backgrounds
- Notifications: Success/warning/error use desaturated colors + dark backgrounds
- Loading states: Use skeleton screens or spinners matching dark theme

**Performance Optimization**:
- OLED power saving: Use more #000 pure black backgrounds to reduce pixel emission
- GPU acceleration: transform: translateZ(0) optimizes animation performance
- Reduce repaints: Avoid frequent changes to box-shadow and background-color
- Image optimization: Use WebP format, reduce image brightness in dark mode

**Typical Use Cases**:
- Productivity tools: Code editors, note apps, project management tools
- Content platforms: Reading apps, news sites, social media
- Developer tools: Consoles, API documentation, admin dashboards
- Financial apps: Stock trading, cryptocurrency, data monitoring dashboards
- Entertainment apps: Video platforms, music players, gaming interfaces
