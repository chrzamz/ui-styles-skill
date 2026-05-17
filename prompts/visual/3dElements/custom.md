# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名专注于 3D 网页体验的资深 UI 设计师兼前端工程师，请根据当前「STUDIO 3D 创意工作室」示例页的视觉特征，生成一个风格高度相似的全屏主页。你必须保留「3D 浮动立方体 Hero」「可翻转的统计卡片」「3D 轮播作品区」「服务 Tab 模块」「团队卡片 + Modal」「FAQ 手风琴」等结构逻辑，但允许替换文案和具体内容。生成结果应让人一眼认出这是同一个 3D Elements 设计体系下的创意工作室主页变体。

【使用场景】
- 品牌类型：以 3D 视觉、沉浸式网页为卖点的创意工作室或数位代理；
- 用户目标：快速了解该工作室的能力、代表作品、服务范围和核心团队，并有明显的联络/咨询入口；
- 设备假设：以桌面端为主，移动端需要保留纵向滚动和基本 3D 效果（可适当减弱复杂动画）。

【整体布局结构】
1. 固定顶部导航（Header）
   - 半透明玻璃导航条，背景为白色或浅色透明叠加到彩色渐变上，带轻微模糊和 1px 亮边；
   - 左侧是 STUDIO 3D 风格 Logo：大写粗体渐变文字，略微 rotateY，Hover 时左右轻微摆动；
   - 右侧导航链接（Home / Portfolio / Services / Team / Contact），文字为白色或浅色，Hover 时向 Z 轴方向擡起 10px，底部出现亮线；
   - 右侧一个「Contact」或「Start a Project」圆角按钮，背景为粉 → 橙或蓝 → 紫渐变，Hover 时上移并增强阴影。

2. Hero 区（3D 浮动立方体）
   - 页面首屏中心为标题区 + 3 组浮动立方体：
     - 标题文案如「Creative 3D Studio」或同类两行主标题，使用极粗白字 + 投影，整体向前突出（translateZ）；
     - 副标题简短说明工作室擅长「3D web design / immersive interfaces / interactive dashboards」；
     - CTA 按钮区包括主按钮（View Portfolio）与次按钮（Book a Call），都具备 3D 阴影与 hover 放大效果；
   - 右侧或背景区域排列 2–3 组不同大小的立方体：使用 preserve-3d、six faces、渐变色面与阴影，整体缓慢旋转，不同立方体有不同的轨迹与速度。

3. Stats Dashboard（统计卡片）
   - 下一屏为 2×2 或 1×4 的统计网格，Card 采用「可翻转」结构：
     - 正面：大号数字（项目数量、客户数量、获奖数量、满意度等）+ 描述标签；
     - 背面：一段更具体的说明；
   - 整个卡片使用 transform-style: preserve-3d 构建，Hover 或点击时绕 Y 轴旋转 180° 显示背面；
   - 背景可为深色玻璃容器，有轻微光带或渐变叠加，强化「仪表盘面板」感觉。

4. 3D Carousel（作品轮播）
   - 使用水平方向的 3D 卡片轮播展示 3–5 个代表项目；
   - 每张卡片包含：顶部大图（可用渐变块代替示意）、项目名称、简短说明；
   - 卡片在轮播轨道中以不同的 translateZ 和 scale 表示前后关系，当前卡片更大、更亮，其他卡片略微后退并降低透明度；
   - 左右两侧使用半透明圆形按钮控制轮播，Hover 时按钮向前浮出。

5. Services Tabs（服务选项卡）
   - 服务区采用 Tab 切换形式（例如 Design / Development / Animation）；
   - 顶部为 3 个按钮式 Tab，具有立体边框和底部阴影，当前 Tab 向前突出，其余略退后；
   - 下方内容面板为「悬浮的 3D 服务卡片」，内含 Emoji/Icon、标题、服务说明，每个面板切换时可伴随轻微淡入与上浮动效。

6. Team + Modal（团队 & 弹窗）
   - 使用 3–4 张团队卡片，每张卡片包含圆形或方形 Avatar（彩色渐变背景 + 首字母）、姓名、职位；
   - Hover 时卡片倾斜并拉长阴影，点击则打开中央的模态框，展示详细简介（名称、角色、项目经验、技能等）；
   - 模态框本身采用玻璃 + 3D 边框样式，带入场缩放和阴影变化。

7. FAQ 手风琴
   - 列出 3–5 个常见问题，每一项是带有 3D 边缘和阴影的折叠卡片；
   - Header 部分包括问题标题与 +/− 图标，点击时展开内容并更新图标；
   - 展开动画为 max-height 过渡 + 轻微位移，让整个区块视觉上像「展开的立体牌」。

【色彩与光影】
1. 背景：使用蓝→紫→粉的对角线渐变或深色渐变，配合轻微噪点或网格；
2. 前景：使用冷色系渐变块（蓝、紫、青）和暖色点缀（粉、橙），在重要区域叠加发光阴影；
3. 阴影：多用软阴影 + 轻微色偏（例如蓝色阴影），在 3D 元素上强化浮空感。

【交互与动效】
1. 尽量使用 CSS 动画和 transition 表达旋转、翻转和浮动，不依赖 JS 动画库；
2. Hover 与 Active 态要清晰地区分可交互元素，避免纯装饰动画抢走注意力；
3. 动画节奏统一控制在 0.3–0.8 秒区间，Hero 背景立方体可以更慢。

【输出要求】
- 使用语义化 HTML（header/nav/main/section/footer 等），结合合理的 class 名称（可接近 Tailwind 风格但不强制）；
- 不引入外部脚本库（如 Three.js）和大型 UI 框架，仅用 HTML + CSS 实现上述 3D 效果和交互；
- 结构中必须包含：Hero（带 3D 立方体）、Stats 卡片、Carousel、Services Tabs、Team + Modal、FAQ，模块名称可以调整但职能相似；
- 整体视觉必须与当前 STUDIO 3D 示例高度一致：强烈的渐变背景、玻璃卡片、3D 阴影和漂浮立方体，同时保持文字可读和交互清晰。


---

## English Version (en-US)

You are a senior UI designer and front-end engineer focused on 3D web experiences. Based on the existing “STUDIO 3D” creative studio page, generate a full-page landing layout with the same design language. You must preserve the structural logic—3D floating cubes in the hero, flippable stats cards, 3D carousel, services tabs, team cards with modal, and FAQ accordion—while allowing text and details to change. The result should look like a sibling homepage in the same 3D Elements design system.

[Use Case]
- Brand: A creative studio or digital agency specialising in 3D web, immersive interfaces and interactive dashboards;
- User goals: Understand capabilities, representative projects, service offerings and core team, with obvious entry points for contact or project brief;
- Devices: Desktop first, but the page should still work on mobile via vertical scroll with simplified 3D effects.

[Layout Structure]
1. Fixed Glass Header
   - A sticky, glassy navigation bar with a faint blur and subtle light border over the gradient background;
   - Left: a STUDIO 3D logo rendered as bold gradient text with a slight rotateY tilt and hover wobble;
   - Right: navigation links (Home / Portfolio / Services / Team / Contact) that lift along the Z-axis on hover and draw a bright underline;
   - A pill-shaped CTA button (“Contact” or “Start a Project”) with pink→orange or blue→purple gradient, heavy shadow and hover lift.

2. Hero with Floating Cubes
   - Centered hero block combining headline, subheading and CTAs with a cluster of 3D cubes;
   - Headline (e.g. “Creative 3D Studio”) uses oversized white type, strong drop shadow and a Z-translation so it appears closer to the viewer;
   - Subheading briefly states what the studio does (3D web design, immersive products, etc.);
   - Two main buttons (“View Portfolio”, “Book a Call”) behave like physical chips with depth and hover scaling;
   - Around the hero, 2–3 cube clusters built from six faces each, using gradients and CSS 3D transforms to slowly rotate along multiple axes.

3. Stats Dashboard
   - Below the hero, a grid of 4 cards summarising metrics (projects, clients, awards, satisfaction);
   - Each card uses a 3D flip pattern: front shows the metric number and label, back shows a short explanatory sentence;
   - Cards sit on a dark glass surface, with layered shadows that intensify on hover and a smooth 180deg rotation on the Y-axis.

4. 3D Carousel of Projects
   - A horizontally scrolling track of project cards, each composed of an image block, project title and short description;
   - Cards are arranged with different translateZ/scale values to simulate depth; the active card is larger, brighter and closer;
   - Left/right arrow buttons appear as floating discs with subtle glow, moving forward on hover.

5. Services Tabs
   - A 3-tab switcher for services such as Design / Development / Animation;
   - Tab buttons themselves are 3D pills with shadows and perspective; the active tab is pushed toward the viewer;
   - Each tab panel presents a 3D service card with icon, title and paragraph text, transitioning in with a gentle fade and upward movement.

6. Team Section with Modal
   - A responsive grid of team cards, each containing a gradient avatar tile, name and role;
   - Hover effects tilt the cards and strengthen shadows; clicking a card opens a central glass modal with extended bio text;
   - The modal uses a frosted background, depth shadow and entrance animation that scales from the center while fading in.

7. FAQ Accordion
   - A list of 3–5 questions styled as thick, 3D-edged panels;
   - Clicking a header toggles the expanded content, rotates the +/− icon and animates max-height and padding to feel like the card “unfolds”;

[Color & Lighting]
- Background: rich diagonal gradients (blue→purple→pink) or dark space-like transitions with subtle noise or grid lines;
- Foreground: cool gradients (blues, purples, cyans) with warm accents (pinks, oranges) on key CTAs and highlights;
- Shadows: layered, sometimes tinted shadows that enhance the sense of floating depth.

[Interaction & Motion]
- Prefer CSS transitions and keyframes over JavaScript animation libraries;
- Hover and active states must make interactive elements unmistakable while keeping decorative animations calm and predictable;
- Use consistent timing (around 0.3–0.8s) across lifts, flips and movements to maintain a coherent sense of mass.

[Output Requirements]
- Use semantic HTML (header, nav, main, section, footer, etc.) and meaningful class names (utility-like or BEM-style);
- Do not import external JS libraries or heavy UI frameworks; implement all 3D effects and interactions with HTML + CSS (and minimal vanilla JS only for tabs/accordion/modal state);
- Include the following modules in some form: Hero with 3D cubes, Stats cards, Project carousel, Services tabs, Team cards with modal, FAQ accordion;
- The generated page should be instantly recognisable as belonging to the same 3D Elements creative studio family: dramatic gradients, glassy cards, deep shadows and floating cubes, while still keeping text legible and navigation clear.
