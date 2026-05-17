# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名资深 UI 设计师兼前端工程师，请生成一个与当前「Swiss Design 瑞士设计」核心样式卡展示界面风格高度接近的 UI。
要求：保持严谨网格系统、极简二色配色（黑 / 白 + 瑞士红）和理性排版秩序，只允许替换文案与模块内容，不改变整体结构与排版逻辑。输出使用语义化 HTML 结构和 TailwindCSS 风格原子类（或等价工具类方案）。

【使用场景】
- 设计工作室 / 建筑事务所 / 艺术机构的官网或作品集列表页
- 现代主义主题专题页、展览介绍页
- 需要表达「理性、专业、秩序感」的品牌界面

【整体布局结构】
1. 网格基础
   - 使用明确的列系统（如 12 列网格）和固定的列间距（例如基于 8px 或 12px 的倍数）。
   - 所有文字块、图片块都对齐到网格，避免任意漂移。
2. 版面分区
   - 顶部为简洁的 Logo + 导航栏，通常左对齐 Logo，右侧为少量导航链接。
   - 中部为主视觉标题区，可以是大字号标题 + 少量说明文字。
   - 下方使用网格排列项目卡片 / 文案模块，形成清晰列表或分区。
3. 非对称平衡
   - 打破绝对左右对称，通过块状排布和留白形成平衡，而不是居中一切元素。

【色彩与材质】
1. 配色系统
   - 主要采用黑白二色：纯黑 #000000、纯白 #FFFFFF 作为主前景 / 背景色。
   - 瑞士红 #E30613 作为唯一大面积强调色，用于标题、标记条或关键按钮。
   - 若需要灰度，可使用少量浅灰（如 #E5E5E5）作为分隔线或辅助背景。
2. 质感与风格
   - 整体保持扁平、无阴影、无渐变、无纹理的现代主义平面设计。
   - 不使用拟物或玻璃效果，依靠排版与色块本身形成视觉张力。

【排版与网格】
1. 字体系统
   - 使用无衬线字体（如 Helvetica / Inter / SF Pro）作为主体字体。
   - 标题字号可在 48–72px 范围，正文在 14–16px，辅文更小。
2. 对齐与间距
   - 全局采用左对齐排版，避免居中对齐造成的摇摆感。
   - 使用统一的行距和段落间距（例如基于 8px 的倍数），让内容有明确节奏。

【交互与动效】
1. Hover
   - 按钮和链接在悬停时以线条变粗、下划线出现或背景块轻微变暗 / 变亮为主，避免夸张动效。
2. 动画
   - 若需要过渡，可使用非常克制的位移或淡入动画（150–250ms），保持「干净、理性」的视觉感受。

【输出要求】
- 使用语义化 HTML（header / nav / main / section / footer）组织内容。
- 使用 TailwindCSS 风格原子类实现网格（grid / flex）、间距和排版，并确保所有模块对齐到统一网格。
- 生成结果必须保留「严格网格 + 黑白 + 瑞士红 + 左对齐排版」这些关键特征，让人一眼看出是瑞士设计风格。


---

## English Version (en-US)

You are a senior UI designer and front-end engineer. Generate a Swiss Design style interface that looks very close to the current “Swiss Design” core style card demo.
Keep the strict grid system, minimal black/white + Swiss red palette and rational typographic order. You may change copy and module content, but you should not change the overall structure or typographic logic. Output semantic HTML and TailwindCSS-style utility classes (or an equivalent utility-first system).

[Usage scenario]
- Websites or portfolios for design studios, architecture offices or art institutions
- Modernist-themed campaign pages or exhibition intros
- Brand interfaces that must communicate rationality, professionalism and order

[Layout structure]
1. Grid foundation
   - Use a clear column system (for example a 12-column grid) with fixed gutters based on 8px or 12px increments.
   - All text blocks and images should align to this grid; avoid arbitrary offsets.
2. Page zones
   - Top area: simple logo plus navigation, typically left-aligned logo with a small set of links on the right.
   - Middle: a primary headline area with large type and a short supporting description.
   - Below: project cards or content modules arranged on the grid, forming clear lists or sections.
3. Balance
   - Break strict symmetry while preserving equilibrium using blocks of content and whitespace.

[Color and material]
- Black (#000000) and white (#FFFFFF) as primary foreground/background;
- Swiss red (#E30613) as the only strong accent color;
- Optional light grays (#E5E5E5, #808080) for dividers and subtle backgrounds;
- No gradients, no shadows, no textures; flat shapes and type create the visual impact.

[Typography]
- Sans-serif type (Helvetica / equivalent), 48–72px headlines, 14–16px body;
- Left-aligned text, tight but readable line-height and controlled spacing.

[Interaction]
- Hover states for links and buttons expressed through underlines or color changes;
- Very subtle transitions (150–250ms) for color/opacity only.

[Output]
- Use semantic HTML with Tailwind-like utility classes for grid, spacing and type;
- Preserve the key features “strict grid + black/white + Swiss red + left-aligned typography” so the result is immediately recognizable as Swiss Design.
