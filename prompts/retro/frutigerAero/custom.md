# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名资深 UI 设计师兼前端工程师，请生成一个与当前「Frutiger Aero」核心样式卡展示界面风格高度接近的 Y2K 玻璃质感 UI。
要求：保持天空蓝渐变背景、半透明玻璃卡片、水滴气泡和流线圆角这些核心特征，只允许替换文案、图标与具体模块内容，不改变整体「清爽、梦幻、略带复古操作系统感」的视觉语言。输出使用语义化 HTML 结构和 TailwindCSS 风格原子类（或等价工具类方案）。

【使用场景】
- 具有 2000 年代气质的产品官网、工具仪表盘首页
- 怀旧 Windows Vista / 早期 Aero 主题的登陆界面
- 创意软件、效率工具、云服务的轻量信息面板

【整体布局结构】
1. 背景层
   - 使用大面积天空蓝 / 青蓝渐变背景，自上而下或对角线方向过渡。
   - 可以在远处加入柔和云朵、光晕或模糊景深元素，营造「在空中漂浮」的感觉。
2. 主玻璃卡片
   - 中央或略偏中的位置放置一块半透明玻璃卡片，用于承载标题、副标题和主要操作按钮。
   - 圆角较大（例如 20–32px），内边距充足，保持轻盈通透。
3. 装饰层
   - 周围散布 3–6 个大小不同的玻璃气泡 / 水滴，位置不必完全规则但需围绕主体区域。
   - 可加一条或几条弯曲的高光线条，暗示水波或光线流动。

【色彩与材质】
1. 颜色系统
   - 背景：从 #87CEEB（天空蓝）到 #5FB3CC（青蓝）或类似范围的冷色渐变。
   - 卡片：白色半透明背景（例如 rgba(255,255,255,0.3–0.4)），叠加轻微高光与内阴影。
   - 强调色：亮绿色 / 橙色可用作主按钮或状态标签点缀，但面积有限。
2. 材质表现
   - 玻璃态元素使用 blur、透明度与高光边界模拟折射感。
   - 气泡内部使用 radial-gradient 做出中心亮、边缘渐暗的水滴质感。

【光影与空间】
1. 所有前景元素（卡片、按钮、图标）在背景上有轻微投影，营造浮起的层次。
2. 可在整体增加非常轻的噪点纹理，让画面不至于过于塑料感。
3. 背景亮度自上而下略有变化，提高空间深度感。

【交互与动效】
1. Hover
   - 按钮在悬停时略微提亮并增加轻微阴影，不改变整体形状。
   - 气泡在悬停时可轻微放大 1.05 倍并提高亮度，像被光线照到。
2. 动效
   - 可为部分气泡添加缓慢上下漂浮或轻微缩放动画（周期 3–6 秒）。
   - 卡片出现时可以从轻微缩放 + 淡入的方式进入视图。

【输出要求】
- 使用语义化 HTML（main / section / header 等）组织内容结构。
- 使用 TailwindCSS 风格原子类实现布局（flex / grid）、间距与对齐。
- 生成结果必须保留「天空蓝渐变背景 + 半透明玻璃卡片 + 浮动气泡 + 大圆角」这些关键特征，让人一眼看出属于 Frutiger Aero / Y2K 玻璃风格。


---

## English Version (en-US)

You are a senior UI designer and front-end engineer. Generate a Frutiger Aero style interface that looks very close to the current “Frutiger Aero” core style card demo.
Keep the sky-blue gradient background, translucent glass card, floating water bubbles and large rounded corners as the main traits. You may change text, icons and module content, but you should not change the overall “fresh, dreamy, slightly nostalgic OS” visual language. Output semantic HTML and TailwindCSS-style utility classes (or an equivalent utility-first system).

[Usage scenario]
- Product marketing or dashboard home screens with a 2000s Aero feeling
- Nostalgic Windows Vista / early Aero themed landing experiences
- Creative tools, productivity apps or cloud services with light, uplifting visuals

[Layout structure]
1. Background layer
   - Use a large sky-blue to cyan gradient, either vertical or diagonal.
   - Optionally add soft clouds, halos or distant blurred shapes to suggest aerial depth.
2. Main glass card
   - Place a semi-transparent glass card in the center or slightly off-center to hold heading, subheading and main action button.
   - Use generous border-radius (around 20–32px) and internal padding so the card feels light and airy.
3. Decoration layer
   - Scatter a handful of glass bubbles / droplets around the main card, with varying sizes.
   - One or two curved light streaks can hint at flowing water or moving light.

[Color and materials]
1. Palette
   - Background: gradients around #87CEEB (sky blue) to #5FB3CC (cyan), or similar cool hues.
   - Card: white translucent surface (for example rgba(255,255,255,0.3–0.4)) with subtle highlights and inner shadows.
   - Accent: bright green or orange for primary buttons or status chips, used sparingly.
2. Material rendering
   - Glass elements combine blur, transparency and edge highlights to mimic refraction.
   - Bubbles use radial gradients with bright centers and darker rims to feel like liquid droplets.

[Light, depth and space]
1. Foreground elements (cards, buttons, icons) cast soft shadows on the gradient background.
2. Add a very light noise texture overall if needed so the scene does not look overly plastic.
3. Let the gradient brightness vary slightly from top to bottom to reinforce depth.

[Interaction and motion]
1. Hover
   - Buttons brighten a bit and gain a slight shadow on hover rather than changing shape.
   - Bubbles may scale up to about 1.05x and brighten slightly when hovered, as if catching more light.
2. Motion
   - Some bubbles can float gently up and down or pulse in size over 3–6 second cycles.
   - The main card can fade and scale in when entering the viewport.

[Output requirements]
- Use semantic HTML (main / section / header, etc.) for structure.
- Use Tailwind-style utility classes for layout, spacing and alignment.
- The generated UI must preserve “sky gradient + translucent glass card + floating bubbles + big rounded corners” so it is clearly a Frutiger Aero / Y2K glass variant at first glance.
