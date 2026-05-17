# Custom Prompt

## 中文版本 (zh-CN)

请使用 TailwindCSS 创建一个充满活力的 Memphis 风格页面，完整展现 1980 年代 Memphis 设计运动的精髓。

**Memphis 风格核心特征**：

**色彩系统**：
- 使用高饱和度、高对比度的大胆色块组合
- 主色调：亮黄（#FFD700）、电蓝（#0066FF）、热粉（#FF1493）、翠绿（#00FF7F）、橙红（#FF4500）
- 次要色彩：紫罗兰（#9370DB）、青绿（#00CED1）、柠檬黄（#FFF44F）
- 避免使用柔和过渡色，强调色彩碰撞与冲突美学
- 背景可以是纯白或浅灰，让彩色元素充分跳跃

**几何形状元素**：
- 大量使用基础几何图形：圆形、三角形、正方形、矩形
- 添加不规则几何：梯形、平行四边形、不对称多边形
- 重复使用波浪线、锯齿线、波点阵列作为装饰元素
- 使用细线条（1-3px）勾勒形状轮廓，创造手绘感
- 图形间可以重叠、旋转、错位，营造俏皮动感

**纹理与图案**：
- 波点（Dots）：使用不同大小的圆点密集排列或随机散布
- 细线纹理：平行细线、交叉斜线、网格线（1-2px 宽度）
- 波浪曲线：流动的 S 形曲线、螺旋线、随机弯曲线条
- 条纹图案：宽窄不一的彩色条纹，可以斜向或竖向排列
- Memphis 经典符号：眼睛、嘴唇、闪电、星星等抽象符号

**排版设计**：
- 标题字体：使用粗体几何无衬线字体（如 Futura、Helvetica Black）
- 字体大小：大胆使用超大标题（48px-96px），制造视觉冲击
- 文字颜色：使用对比强烈的配色，文字本身也可以是彩色的
- 字母间距：可以适度增加，营造松散俏皮感
- 倾斜与旋转：部分文字可以旋转 5-15 度，增加动态
- 文字描边：使用 2-3px 的黑色或彩色描边，增强辨识度

**布局构成**：
- 非对称布局：避免传统的居中对齐，使用不规则的元素分布
- 留白与密集对比：某些区域密集填充图案，某些区域保持留白
- Z 轴层次：通过颜色块的叠加和错位营造深度感
- 模块化分隔：用粗线条（4-8px）或彩色色块分隔不同内容区域
- 网格基础：虽然看似随意，但底层遵循网格系统（12 列）

**交互元素设计**：
- 按钮：使用几何形状（圆角矩形、圆形、斜切角），添加粗边框（3-4px）
- 按钮悬停：颜色反转、形状微旋转（2-5 度）、阴影增强
- 卡片：每张卡片可以使用不同的背景图案和边框颜色
- 卡片边框：使用双色或三色边框，宽度 4-6px
- 图标：线性风格图标，可以填充彩色或保持纯线条
- 链接：下划线可以是波浪形或锯齿形，颜色鲜艳

**页面结构要求**：

1. **Hero 区域**：
   - 超大标题，字体粗黑，颜色鲜艳（使用 2-3 种颜色组合）
   - 背景使用几何图形拼贴：圆形、三角形、矩形随机分布
   - 添加细线纹理或波点图案作为背景装饰
   - CTA 按钮使用不规则形状（斜切角或倾斜）

2. **特性/服务卡片组（3-4 个）**：
   - 每张卡片使用不同的底色和边框颜色
   - 卡片内部添加几何装饰图形（角落的三角形、圆形点缀）
   - 图标使用线性风格，可以填充对比色
   - 卡片标题使用大字号，描述文字保持可读性
   - 卡片间距不均等，营造错落感

3. **图文分栏展示区（左右布局）**：
   - 图片区域：使用彩色边框（宽 6-8px），边框可以是多色拼接
   - 图片装饰：在图片周围添加几何图形（三角形、圆形）作为点缀
   - 文字区域：标题大胆，使用彩色背景块突出重点段落
   - 分隔线：使用波浪线或锯齿线分隔段落

4. **列表/网格展示区**：
   - 使用不规则网格布局（2-3 列，行高不一）
   - 每个列表项添加彩色图标或数字标记
   - 背景可以是条纹、波点或几何图案的组合
   - 列表项边框使用多色组合（红-蓝-黄三色边框）

5. **CTA 行动召唤区**：
   - 大面积彩色背景（使用主色调之一）
   - 背景叠加几何图案（半透明的圆形、三角形）
   - 超大标题，使用对比色或白色
   - 多个按钮并列，每个按钮颜色不同
   - 添加抽象装饰元素（波浪线、星星、闪电）

**细节实现要点**：
- 使用 CSS `transform: rotate()` 实现元素倾斜（-8deg 到 8deg）
- 使用 `background-image: repeating-linear-gradient()` 创建条纹和细线纹理
- 使用伪元素 `::before` 和 `::after` 添加装饰性几何图形
- 利用 `box-shadow` 创建多层彩色阴影效果（堆叠 2-3 层不同颜色）
- 使用 `clip-path` 创建不规则形状（斜切角、梯形）
- 添加微动画：悬停时的旋转（rotate）、缩放（scale）效果

**配色方案示例**：
- 方案 1（热情活力）：#FF1493 (热粉) + #FFD700 (亮黄) + #00CED1 (青绿) + #FF4500 (橙红)
- 方案 2（复古俏皮）：#9370DB (紫罗兰) + #00FF7F (翠绿) + #FF6347 (番茄红) + #1E90FF (道奇蓝)
- 方案 3（电子感）：#0066FF (电蓝) + #FFFF00 (纯黄) + #FF1493 (品红) + #00FF00 (荧光绿)

**响应式考虑**：
- 移动端：减少几何装饰元素密度，保持主要色块和纹理
- 移动端：卡片改为单列堆叠，保留边框和图案特征
- 移动端：标题字号适度缩小（32px-48px），但仍保持大胆
- 平板端：两列布局，几何元素适度缩放

**避免事项**：
- 不要使用柔和渐变或模糊效果（Memphis 风格强调清晰边界）
- 不要过度使用阴影营造立体感（Memphis 更偏向平面设计）
- 不要使用传统对称布局（Memphis 强调打破规则）
- 不要使用低饱和度或莫兰迪色系（Memphis 需要高饱和度）


---

## English Version (en-US)

Create a vibrant Memphis-style page using TailwindCSS that fully embodies the essence of the 1980s Memphis Design Movement.

**Memphis Style Core Characteristics**:

**Color System**:
- Use bold, high-saturation, high-contrast color block combinations
- Primary colors: Bright Yellow (#FFD700), Electric Blue (#0066FF), Hot Pink (#FF1493), Turquoise (#00FF7F), Orange Red (#FF4500)
- Secondary colors: Purple (#9370DB), Cyan (#00CED1), Lemon Yellow (#FFF44F)
- Avoid soft transitions; emphasize color clashes and conflicting aesthetics
- Background can be pure white or light gray to let colorful elements pop

**Geometric Shape Elements**:
- Extensive use of basic geometric shapes: circles, triangles, squares, rectangles
- Add irregular geometry: trapezoids, parallelograms, asymmetric polygons
- Repeatedly use wavy lines, zigzag lines, dot arrays as decorative elements
- Use thin lines (1-3px) to outline shapes, creating a hand-drawn feel
- Shapes can overlap, rotate, and misalign to create playful dynamics

**Textures & Patterns**:
- Dots: Arrange circles of different sizes densely or scatter randomly
- Fine line textures: parallel lines, cross-hatching, grid lines (1-2px width)
- Wave curves: flowing S-curves, spirals, random curved lines
- Stripe patterns: colorful stripes of varying widths, diagonal or vertical
- Memphis classic symbols: eyes, lips, lightning bolts, stars, abstract symbols

**Typography Design**:
- Heading fonts: Use bold geometric sans-serif fonts (like Futura, Helvetica Black)
- Font sizes: Boldly use oversized headlines (48px-96px) for visual impact
- Text colors: Use strongly contrasting colors; text itself can be multicolored
- Letter spacing: Can be moderately increased for a loose, playful feel
- Tilt & rotation: Some text can rotate 5-15 degrees for dynamism
- Text stroke: Use 2-3px black or colored strokes to enhance readability

**Layout Composition**:
- Asymmetric layouts: Avoid traditional center alignment, use irregular element distribution
- Whitespace vs. density contrast: Some areas densely filled with patterns, others maintain whitespace
- Z-axis hierarchy: Create depth through color block overlays and misalignments
- Modular separation: Use thick lines (4-8px) or colored blocks to separate content areas
- Grid foundation: Though seemingly random, follow an underlying grid system (12-column)

**Interactive Element Design**:
- Buttons: Use geometric shapes (rounded rectangles, circles, chamfered corners), add thick borders (3-4px)
- Button hover: Color inversion, slight shape rotation (2-5 degrees), enhanced shadow
- Cards: Each card can use different background patterns and border colors
- Card borders: Use two-color or three-color borders, width 4-6px
- Icons: Linear style icons, can be filled with colors or remain pure linework
- Links: Underlines can be wavy or zigzag, colors vibrant

**Page Structure Requirements**:

1. **Hero Section**:
   - Oversized headline, bold font, vibrant colors (use 2-3 color combinations)
   - Background uses geometric collage: circles, triangles, rectangles randomly distributed
   - Add fine line textures or dot patterns as background decoration
   - CTA button uses irregular shapes (chamfered or tilted)

2. **Feature/Service Card Group (3-4 cards)**:
   - Each card uses different background and border colors
   - Add geometric decorative shapes inside cards (corner triangles, circle accents)
   - Icons use linear style, can be filled with contrasting colors
   - Card titles use large font sizes, description text maintains readability
   - Unequal card spacing creates staggered feel

3. **Image-Text Split Display Area (left-right layout)**:
   - Image area: Use colorful borders (6-8px wide), borders can be multi-color spliced
   - Image decoration: Add geometric shapes (triangles, circles) around images as accents
   - Text area: Bold headlines, use colored background blocks to highlight key paragraphs
   - Dividers: Use wavy or zigzag lines to separate paragraphs

4. **List/Grid Display Area**:
   - Use irregular grid layout (2-3 columns, varying row heights)
   - Add colorful icons or numeric markers to each list item
   - Background can be combination of stripes, dots, or geometric patterns
   - List item borders use multi-color combinations (red-blue-yellow tricolor borders)

5. **CTA Call-to-Action Area**:
   - Large area colorful background (use one of primary colors)
   - Background overlaid with geometric patterns (semi-transparent circles, triangles)
   - Oversized headline, use contrasting color or white
   - Multiple buttons side by side, each different color
   - Add abstract decorative elements (wavy lines, stars, lightning)

**Implementation Details**:
- Use CSS `transform: rotate()` for element tilt (-8deg to 8deg)
- Use `background-image: repeating-linear-gradient()` to create stripes and fine line textures
- Use pseudo-elements `::before` and `::after` to add decorative geometric shapes
- Utilize `box-shadow` to create multi-layered colored shadow effects (stack 2-3 different colors)
- Use `clip-path` to create irregular shapes (chamfered corners, trapezoids)
- Add micro-animations: rotation (rotate) and scaling (scale) effects on hover

**Color Scheme Examples**:
- Scheme 1 (Hot Energy): #FF1493 (Hot Pink) + #FFD700 (Bright Yellow) + #00CED1 (Cyan) + #FF4500 (Orange Red)
- Scheme 2 (Retro Playful): #9370DB (Purple) + #00FF7F (Spring Green) + #FF6347 (Tomato) + #1E90FF (Dodger Blue)
- Scheme 3 (Electronic): #0066FF (Electric Blue) + #FFFF00 (Pure Yellow) + #FF1493 (Magenta) + #00FF00 (Lime Green)

**Responsive Considerations**:
- Mobile: Reduce density of geometric decorative elements, maintain main color blocks and textures
- Mobile: Cards stack in single column, retain border and pattern characteristics
- Mobile: Headline font size moderately reduced (32px-48px) but still bold
- Tablet: Two-column layout, geometric elements moderately scaled

**Things to Avoid**:
- Don't use soft gradients or blur effects (Memphis emphasizes clear boundaries)
- Don't overuse shadows for depth (Memphis leans toward flat design)
- Don't use traditional symmetric layouts (Memphis emphasizes breaking rules)
- Don't use low saturation or muted color palettes (Memphis needs high saturation)
