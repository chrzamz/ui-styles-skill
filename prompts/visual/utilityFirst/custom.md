# Custom Prompt

## 中文版本 (zh-CN)

你现在是一位精通 Utility-First（实用优先 / 原子化）设计方法论的资深 UI 设计师兼前端工程师。请为我创建一个展示原子类系统与设计令牌的示例网页，要求如下：

### 核心理念
- **原子化类名**：展示 Tailwind CSS 式的实用类（如 `px-4`, `text-lg`, `bg-blue-500`）应用效果
- **设计令牌展示**：清晰展示颜色、间距、字号、圆角等设计令牌系统
- **一致性**：通过统一的设计令牌确保UI一致性
- **极简中性**：使用中性色系 + 单一品牌色，避免过度装饰

### 页面结构
1. **导航栏**：展示实用类应用（padding, flex, gap 等）
2. **组件网格**：4x4 网格展示不同组件（按钮、输入框、标签、警示条）
3. **设计令牌表**：表格形式展示颜色系统、间距尺度、字号尺度
4. **排版尺度说明**：展示从 xs 到 5xl 的字号阶梯

### 配色策略
- **中性色阶**：灰色 50-950 九级色阶（#fafafa, #f5f5f5, ..., #0a0a0a）
- **品牌色**：单一品牌色（如蓝色）的 50-950 九级色阶
- **语义色**：成功绿、警告黄、错误红、信息蓝，各 3-5 级深浅
- **极简呈现**：大面积白/灰背景，色彩仅用于强调

### 组件展示网格
- **按钮变体**：主按钮、次要按钮、轮廓按钮、文本按钮、禁用状态
- **输入框状态**：默认、聚焦、填充、错误、禁用
- **标签 Tag**：不同颜色与尺寸的标签（xs, sm, md, lg）
- **警示条 Alert**：success, warning, error, info 四种类型
- **表格 Table**：展示数据表格的样式

### 设计令牌系统
- **间距尺度**：0, 0.5 (2px), 1 (4px), 2 (8px), 3 (12px), 4 (16px), 6 (24px), 8 (32px), 12 (48px), 16 (64px)
- **字号尺度**：xs (12px), sm (14px), base (16px), lg (18px), xl (20px), 2xl (24px), 3xl (30px), 4xl (36px), 5xl (48px)
- **圆角尺度**：none, sm (2px), default (4px), md (6px), lg (8px), xl (12px), 2xl (16px), 3xl (24px), full (9999px)
- **阴影尺度**：sm, default, md, lg, xl, 2xl, inner

### 文字排版
- **字体**：系统无衬线字体栈（-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, ...）
- **字重**：100 (thin), 300 (light), 400 (normal), 500 (medium), 600 (semibold), 700 (bold), 900 (black)
- **行高**：tight (1.25), normal (1.5), relaxed (1.625), loose (2)
- **字间距**：tighter, tight, normal, wide, wider, widest

### 表格展示设计令牌
创建表格展示各类令牌：

**颜色表**（每行一个颜色，展示 9 个色阶）：
```
| 颜色名     | 50      | 100     | ... | 900     |
|-----------|---------|---------|-----|---------|
| Gray      | #fafafa | #f5f5f5 | ... | #0a0a0a |
| Blue      | #eff6ff | #dbeafe | ... | #1e3a8a |
```

**间距表**：
```
| 名称 | 值    | 实际像素 |
|------|-------|----------|
| 0    | 0     | 0px      |
| 1    | 0.25rem | 4px   |
| 2    | 0.5rem  | 8px   |
```

### 实用类命名规范
- **间距**：`p-4` (padding), `m-2` (margin), `px-6` (padding-left-right), `mt-8` (margin-top)
- **布局**：`flex`, `grid`, `justify-center`, `items-center`, `gap-4`
- **字号**：`text-xs`, `text-sm`, `text-base`, `text-lg`
- **字重**：`font-thin`, `font-normal`, `font-bold`
- **颜色**：`text-gray-900`, `bg-blue-500`, `border-red-600`
- **圆角**：`rounded-sm`, `rounded-md`, `rounded-lg`, `rounded-full`

### 技术要点
- 使用 CSS 变量定义所有设计令牌（--spacing-1, --color-blue-500, --text-lg）
- 使用实用类而非自定义类名（如使用 `flex items-center gap-4` 而非 `.my-custom-flex-container`）
- 展示令牌如何在不同组件中复用，确保一致性

### 输出要求
请生成完整的 HTML 结构与内联样式，确保：
- 代码清晰注释，说明实用类与设计令牌的应用
- 所有令牌使用 CSS 变量定义，便于全局调整
- 展示至少 12 种不同的组件与样式组合
- 页面传达出系统化、可扩展、一致的设计系统理念


---

## English Version (en-US)

You are a senior UI designer and frontend engineer specializing in Utility-First (Atomic CSS) design methodology. Create a sample webpage showcasing atomic class system and design tokens with the following requirements:

### Core Philosophy
- **Atomic Classnames**: Showcase Tailwind CSS-style utility classes (like `px-4`, `text-lg`, `bg-blue-500`) in action
- **Design Token Display**: Clearly present color, spacing, font-size, border-radius design token systems
- **Consistency**: Ensure UI consistency through unified design tokens
- **Minimal Neutral**: Use neutral color scheme + single brand color, avoid excessive decoration

### Page Structure
1. **Navigation**: Demonstrate utility class application (padding, flex, gap, etc.)
2. **Component Grid**: 4x4 grid displaying different components (buttons, inputs, tags, alerts)
3. **Design Token Table**: Table format showing color system, spacing scale, font-size scale
4. **Typography Scale Description**: Show font-size ladder from xs to 5xl

### Color Strategy
- **Neutral Scale**: Gray 50-950 nine-level scale (#fafafa, #f5f5f5, ..., #0a0a0a)
- **Brand Color**: Single brand color (e.g., blue) with 50-950 nine-level scale
- **Semantic Colors**: Success green, warning yellow, error red, info blue, each with 3-5 shades
- **Minimal Presentation**: Large areas of white/gray background, color only for emphasis

### Component Display Grid
- **Button Variants**: Primary, secondary, outline, text, disabled states
- **Input States**: Default, focused, filled, error, disabled
- **Tags**: Different colors and sizes (xs, sm, md, lg)
- **Alerts**: Success, warning, error, info four types
- **Table**: Data table styling

### Design Token System
- **Spacing Scale**: 0, 0.5 (2px), 1 (4px), 2 (8px), 3 (12px), 4 (16px), 6 (24px), 8 (32px), 12 (48px), 16 (64px)
- **Font-Size Scale**: xs (12px), sm (14px), base (16px), lg (18px), xl (20px), 2xl (24px), 3xl (30px), 4xl (36px), 5xl (48px)
- **Border-Radius Scale**: none, sm (2px), default (4px), md (6px), lg (8px), xl (12px), 2xl (16px), 3xl (24px), full (9999px)
- **Shadow Scale**: sm, default, md, lg, xl, 2xl, inner

### Typography
- **Font**: System sans-serif stack (-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, ...)
- **Weight**: 100 (thin), 300 (light), 400 (normal), 500 (medium), 600 (semibold), 700 (bold), 900 (black)
- **Line-Height**: tight (1.25), normal (1.5), relaxed (1.625), loose (2)
- **Letter-Spacing**: tighter, tight, normal, wide, wider, widest

### Table Display Design Tokens
Create tables displaying various tokens:

**Color Table** (each row one color, showing 9 shades):
```
| Color Name | 50      | 100     | ... | 900     |
|------------|---------|---------|-----|---------|
| Gray       | #fafafa | #f5f5f5 | ... | #0a0a0a |
| Blue       | #eff6ff | #dbeafe | ... | #1e3a8a |
```

**Spacing Table**:
```
| Name | Value   | Pixels |
|------|---------|--------|
| 0    | 0       | 0px    |
| 1    | 0.25rem | 4px    |
| 2    | 0.5rem  | 8px    |
```

### Utility Class Naming Convention
- **Spacing**: `p-4` (padding), `m-2` (margin), `px-6` (padding-left-right), `mt-8` (margin-top)
- **Layout**: `flex`, `grid`, `justify-center`, `items-center`, `gap-4`
- **Font-Size**: `text-xs`, `text-sm`, `text-base`, `text-lg`
- **Font-Weight**: `font-thin`, `font-normal`, `font-bold`
- **Color**: `text-gray-900`, `bg-blue-500`, `border-red-600`
- **Border-Radius**: `rounded-sm`, `rounded-md`, `rounded-lg`, `rounded-full`

### Technical Points
- Use CSS variables to define all design tokens (--spacing-1, --color-blue-500, --text-lg)
- Use utility classes rather than custom class names (e.g., use `flex items-center gap-4` instead of `.my-custom-flex-container`)
- Show how tokens reuse across components ensuring consistency

### Output Requirements
Generate complete HTML structure with inline styles ensuring:
- Clear code comments explaining utility class and design token application
- All tokens defined using CSS variables for global adjustment
- Display at least 12 different component and style combinations
- Page conveys systematic, scalable, consistent design system philosophy
