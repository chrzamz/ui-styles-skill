# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名资深 UI 设计师兼前端工程师，请生成一个与当前「Retro OS」核心样式卡展示界面风格高度接近的 1990 年代桌面操作系统风格 UI。
要求：保持 Windows 95/98 风格窗口、任务栏、开始菜单和 CRT 显示器质感，只允许替换窗口标题、图标与具体内容，不改变整体窗口布局与配色体系。输出使用语义化 HTML 结构和 TailwindCSS 风格原子类（或等价工具类方案）。

【使用场景】
- 怀旧主题网站、复古游戏平台、技术博客的「虚拟桌面」式首页
- 模拟器、系统工具、个人作品集的操作系统主题界面
- 需要传达 90 年代个人电脑审美与趣味感的交互场景

【整体布局结构】
1. 桌面背景
   - 使用经典青绿色 (#008080) 或纯色渐变作为全屏背景，可加入少量像素化图标。
   - 保持背景简洁，突出前景窗口。
2. 主窗口
   - 居中或略偏上的主应用窗口，包含标题栏、菜单区和内容区。
   - 标题栏使用深蓝色 (#000080) 背景 + 白色文字，左侧带应用图标，右侧为最小化 / 最大化 / 关闭按钮。
3. 任务栏与开始菜单
   - 底部使用灰色任务栏 (#C0C0C0)，左侧放置「Start」按钮，右侧可包含时间或系统托盘区域。
   - 可设计多个小窗口 / 对话框叠加在桌面上，但层级关系要清晰。

【色彩与材质】
1. 经典配色
   - 桌面背景：Teal 青色 #008080 或类似。
   - 窗口背景：浅灰色 #C0C0C0。
   - 标题栏：深蓝 #000080（活动窗口）、深灰蓝用于非活动窗口。
   - 边框与线条：使用深浅不同的灰色组合，模拟 3D 边框。
2. 材质与像素感
   - 保持纯平色块与清晰像素边缘，不使用现代渐变或柔光阴影。
   - 图标与按钮使用低分辨率像素图或像素风矢量图。

【3D 边框与交互细节】
1. 窗口与按钮边框采用「上亮下暗」和「上暗下亮」组合，模拟凸起 / 凹陷效果。
2. 按钮默认为凸起状态，按下时边框反转为凹陷（例如 border-style 从 outset 换成 inset）。
3. 输入框、列表与滚动条同样使用 2px 边框和内凹效果，统一视觉语言。

【交互与动效】
1. Hover
   - 鼠标悬停在按钮上时仅改变背景色或边框色，尽量模仿原生 OS 交互。
2. Active
   - 点击时按钮应立即呈现凹陷态，释放后恢复凸起。
3. 动画
   - 基本不使用复杂动画，只在必要时使用极短的淡入淡出或位移（100–150ms），保持操作系统原始感觉。

【输出要求】
- 使用语义化 HTML 构建桌面、任务栏、窗口等层级结构。
- 使用 TailwindCSS 风格原子类描述布局（绝对定位 / flex）、层级（z-index）和颜色。
- 生成结果必须保留「Teal 桌面背景 + 灰色 3D 窗口 + 蓝色标题栏 + 底部任务栏」这些关键特征，让人一眼看出是 90 年代 Retro OS 风格。


---

## English Version (en-US)

You are a senior UI designer and front-end engineer. Generate a 1990s desktop operating-system style interface that looks very close to the current “Retro OS” core style card demo.
Keep Windows 95/98-style windows, taskbar, Start button and CRT-like visual feel as the main traits. You may change window titles, icons and content, but you should not change the overall window layout or color system. Output semantic HTML and TailwindCSS-style utility classes (or an equivalent utility-first system).

[Usage scenario]
- Virtual desktop style homepages for nostalgic websites, retro game portals or tech blogs
- OS-themed UIs for emulators, tools or personal portfolios
- Interfaces that need to express 1990s personal computer aesthetics and playful nostalgia

[Layout structure]
1. Desktop background
   - Use a full-screen teal (#008080) or similar solid / simple gradient background with a few desktop icons.
   - Keep the background simple so foreground windows stand out.
2. Main window
   - A central or slightly elevated primary application window with title bar, menu area and content pane.
   - Title bar uses deep blue (#000080) with white text; left side shows an app icon, right side has minimize / maximize / close buttons.
3. Taskbar and Start menu
   - A gray taskbar (#C0C0C0) at the bottom, with a “Start” button on the left and optional clock / tray area on the right.
   - Optionally include additional small windows or dialogs stacked on the desktop, but maintain clear visual hierarchy.

[Color and materials]
1. Classic palette
   - Desktop: teal #008080 or related hues.
   - Window backgrounds: light grey #C0C0C0.
   - Active title bar: navy #000080; inactive bars can use darker greys.
   - Borders and separators: combinations of light and dark greys to form 3D edges.
2. Pixel feel
   - Use sharp solid color blocks and crisp pixel edges; avoid modern gradients and soft glows.
   - Icons and buttons should look pixelated or low-resolution, matching the period.

[3D borders and micro-interactions]
1. Use “light top / dark bottom” and the reverse combinations for raised vs sunken surfaces.
2. Buttons are raised by default; when pressed, their border inverts to look inset (similar to switching from outset to inset style).
3. Inputs, lists and scrollbars use 2px borders and inset effects to maintain a unified visual language.

[Interaction and motion]
1. Hover
   - On hover, change button background or border color only, mimicking native OS hover if present.
2. Active
   - On click, buttons should immediately appear sunken, then return to raised state when released.
3. Animation
   - Avoid complex animations; limit transitions to very short fades or position changes (around 100–150ms) so the UI feels like a real 90s OS.

[Output requirements]
- Use semantic HTML to represent desktop, taskbar and window hierarchy.
- Use Tailwind-style utilities for layout (absolute positioning / flex), z-index layering and colors.
- The generated UI must preserve “teal desktop + grey 3D windows + blue title bar + bottom taskbar” as key cues so it is instantly recognizable as a 90s Retro OS variant.
