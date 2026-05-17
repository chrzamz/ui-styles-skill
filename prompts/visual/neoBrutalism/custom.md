# Neo-Brutalism (新粗野主义) - Custom Prompt

## 中文版本 (zh-CN)

### 设计概述
为产品生成 **Neo-Brutalism（新粗野主义）** 风格的界面设计。这是一种反对过度装饰的设计运动，通过粗黑边框、高饱和度色块、硬阴影和零圆角，创造出原始、直接、毫不妥协的数字体验。每个元素都像是用记号笔和尺子在白纸上直接画出来的，拒绝任何视觉糖衣。

## 核心设计要求

### 1. 粗黑边框系统（Brutal Borders）

**边框原则**:
- 所有元素必须有明显的黑色边框
- 边框粗细：2-4px（标准）、6-8px（强调）
- 边框颜色：纯黑 `#000000` 或深灰 `#1a1a1a`
- 绝对禁止圆角：`border-radius: 0`

**完整 CSS 实现**:
```css
/* 标准容器边框 */
.brutal-card {
  background: #ffffff;
  border: 3px solid #000000;
  border-radius: 0;
  padding: 2rem;
  position: relative;
  transition: all 0.2s ease;
}

.brutal-card:hover {
  /* hover 时边框加粗 */
  border-width: 4px;
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0 #000000;
}

/* 强调边框（加粗版） */
.brutal-card-emphasis {
  background: #ffff00;
  border: 6px solid #000000;
  padding: 2.5rem;
  box-shadow: 8px 8px 0 #000000;
}

/* 嵌套边框效果 */
.brutal-card-nested {
  background: #ff0000;
  border: 4px solid #000000;
  padding: 0.5rem;
}

.brutal-card-nested .inner {
  background: #ffffff;
  border: 3px solid #000000;
  padding: 1.5rem;
}

/* 双色边框 */
.brutal-card-duotone {
  background: #00ff00;
  border: 4px solid #000000;
  box-shadow:
    0 0 0 8px #ffffff,
    0 0 0 12px #000000;
}
```

### 2. 硬阴影系统（Hard Shadows）

**阴影原则**:
- 完全没有模糊：`blur = 0`
- 明显的偏移量：通常 4-8px
- 纯色阴影：黑色或与主色相同
- 阴影始终朝向右下角

**完整 CSS 实现**:
```css
/* 标准硬阴影 */
.brutal-shadow {
  box-shadow: 4px 4px 0 #000000;
}

.brutal-shadow:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 #000000;
}

.brutal-shadow:active {
  transform: translate(2px, 2px);
  box-shadow: 2px 2px 0 #000000;
}

/* 大号硬阴影 */
.brutal-shadow-large {
  box-shadow: 8px 8px 0 #000000;
}

/* 彩色硬阴影 */
.brutal-shadow-color {
  background: #ff0000;
  border: 3px solid #000000;
  box-shadow: 6px 6px 0 #ffff00;
}

/* 多层硬阴影 */
.brutal-shadow-layered {
  background: #00ffff;
  border: 3px solid #000000;
  box-shadow:
    4px 4px 0 #000000,
    8px 8px 0 #ff00ff;
}

/* 内硬阴影（凹陷效果） */
.brutal-shadow-inset {
  background: #f0f0f0;
  border: 3px solid #000000;
  box-shadow: inset 4px 4px 0 #000000;
}
```

### 3. 高饱和度色彩系统（Candy Colors）

**色彩原则**:
- 使用纯色、高饱和度（100%）
- 避免渐变和半透明
- 黑白作为基础色
- 糖果色作为点缀

**完整色彩方案**:
```css
:root {
  /* 基础色 - Base Colors */
  --brutal-black: #000000;
  --brutal-white: #ffffff;
  --brutal-gray-dark: #1a1a1a;
  --brutal-gray-light: #e5e5e5;

  /* 糖果色 - Candy Colors (100% saturation) */
  --brutal-red: #ff0000;
  --brutal-blue: #0000ff;
  --brutal-green: #00ff00;
  --brutal-yellow: #ffff00;
  --brutal-cyan: #00ffff;
  --brutal-magenta: #ff00ff;
  --brutal-orange: #ff6600;
  --brutal-pink: #ff3399;
  --brutal-purple: #9900ff;

  /* 柔和糖果色（稍降饱和度至80%） */
  --brutal-red-soft: #ff4d4d;
  --brutal-blue-soft: #4d4dff;
  --brutal-green-soft: #4dff4d;
  --brutal-yellow-soft: #ffff4d;
  --brutal-orange-soft: #ff884d;
  --brutal-pink-soft: #ff66b3;
}

/* 配色示例 - 红黑主题 */
.theme-red {
  background: var(--brutal-red);
  border: 4px solid var(--brutal-black);
  color: var(--brutal-white);
}

/* 配色示例 - 黄黑主题 */
.theme-yellow {
  background: var(--brutal-yellow);
  border: 4px solid var(--brutal-black);
  color: var(--brutal-black);
}

/* 配色示例 - 多色块 */
.theme-multicolor {
  background: var(--brutal-white);
  border: 4px solid var(--brutal-black);
}

.theme-multicolor .block-1 {
  background: var(--brutal-cyan);
  border: 3px solid var(--brutal-black);
}

.theme-multicolor .block-2 {
  background: var(--brutal-magenta);
  border: 3px solid var(--brutal-black);
}

.theme-multicolor .block-3 {
  background: var(--brutal-yellow);
  border: 3px solid var(--brutal-black);
}
```

### 4. 按钮设计（Button Components）

**按钮的原始力量**:
- 全大写文字
- 粗黑边框
- 硬阴影
- 简单的 transform 动画

**完整 CSS 实现**:
```css
/* 主要按钮（红底黑字） */
.brutal-btn-primary {
  background: #ff0000;
  color: #000000;
  border: 3px solid #000000;
  padding: 1rem 2rem;
  font-size: 18px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  cursor: pointer;
  box-shadow: 4px 4px 0 #000000;
  transition: all 0.15s ease;
}

.brutal-btn-primary:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 #000000;
}

.brutal-btn-primary:active {
  transform: translate(2px, 2px);
  box-shadow: 2px 2px 0 #000000;
}

/* 次要按钮（白底黑框） */
.brutal-btn-secondary {
  background: #ffffff;
  color: #000000;
  border: 4px solid #000000;
  padding: 1rem 2rem;
  font-size: 18px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  cursor: pointer;
  box-shadow: 4px 4px 0 #000000;
  transition: all 0.15s ease;
}

.brutal-btn-secondary:hover {
  background: #000000;
  color: #ffffff;
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 #ff0000;
}

/* 大号按钮 */
.brutal-btn-large {
  padding: 1.5rem 3rem;
  font-size: 24px;
  border: 4px solid #000000;
  box-shadow: 8px 8px 0 #000000;
}

/* 图标按钮（方形） */
.brutal-btn-icon {
  width: 60px;
  height: 60px;
  background: #ffff00;
  border: 3px solid #000000;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  font-weight: 900;
  cursor: pointer;
  box-shadow: 4px 4px 0 #000000;
  transition: all 0.15s ease;
}

.brutal-btn-icon:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 #000000;
}

/* 禁用状态 */
.brutal-btn-disabled {
  background: #e5e5e5;
  color: #999999;
  border: 3px solid #999999;
  box-shadow: 4px 4px 0 #999999;
  cursor: not-allowed;
  opacity: 0.6;
}
```

### 5. 表单元素（Form Elements）

**表单的极简主义**:
- 粗黑边框
- 零圆角
- 全大写标签
- 聚焦时边框变红

**完整 CSS 实现**:
```css
/* 文本输入框 */
.brutal-input {
  width: 100%;
  padding: 1rem 1.5rem;
  background: #ffffff;
  border: 3px solid #000000;
  border-radius: 0;
  font-size: 16px;
  font-weight: 700;
  color: #000000;
  transition: all 0.2s ease;
}

.brutal-input:focus {
  outline: none;
  border-color: #ff0000;
  box-shadow: 4px 4px 0 #ff0000;
}

.brutal-input::placeholder {
  color: #999999;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* 文本区域 */
.brutal-textarea {
  width: 100%;
  padding: 1rem 1.5rem;
  background: #ffffff;
  border: 3px solid #000000;
  border-radius: 0;
  font-size: 16px;
  font-weight: 700;
  color: #000000;
  min-height: 150px;
  resize: vertical;
  font-family: inherit;
  line-height: 1.6;
  transition: all 0.2s ease;
}

.brutal-textarea:focus {
  outline: none;
  border-color: #ff0000;
  box-shadow: 4px 4px 0 #ff0000;
}

/* 标签 */
.brutal-label {
  display: block;
  font-size: 14px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #000000;
  margin-bottom: 0.5rem;
}

/* 复选框（自定义样式） */
.brutal-checkbox-wrapper {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  cursor: pointer;
}

.brutal-checkbox {
  appearance: none;
  width: 32px;
  height: 32px;
  background: #ffffff;
  border: 3px solid #000000;
  cursor: pointer;
  position: relative;
  transition: all 0.15s ease;
}

.brutal-checkbox:checked {
  background: #ff0000;
  box-shadow: inset 4px 4px 0 #000000;
}

.brutal-checkbox:checked::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #ffffff;
  font-size: 24px;
  font-weight: 900;
}

/* 下拉选择 */
.brutal-select {
  width: 100%;
  padding: 1rem 1.5rem;
  background: #ffffff;
  border: 3px solid #000000;
  border-radius: 0;
  font-size: 16px;
  font-weight: 700;
  color: #000000;
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M5 7L10 12L15 7' stroke='%23000000' stroke-width='3' stroke-linecap='square'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  padding-right: 3rem;
  transition: all 0.2s ease;
}

.brutal-select:focus {
  outline: none;
  border-color: #ff0000;
  box-shadow: 4px 4px 0 #ff0000;
}
```

### 6. 导航栏（Navigation Bar）

**导航的强势存在**:
- 固定顶部或底部
- 黑色背景 + 白色文字
- 红色底边或顶边强调
- 全大写链接

**完整 CSS 实现**:
```css
/* 固定导航栏 */
.brutal-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: #000000;
  color: #ffffff;
  padding: 2rem;
  border-bottom: 6px solid #ff0000;
}

.brutal-nav-content {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Logo */
.brutal-logo {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brutal-logo-icon {
  width: 60px;
  height: 60px;
  background: #ff0000;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  font-weight: 900;
  color: #000000;
}

.brutal-logo-text {
  font-size: 28px;
  font-weight: 900;
  letter-spacing: 2px;
  text-transform: uppercase;
}

/* 导航菜单 */
.brutal-nav-menu {
  display: flex;
  list-style: none;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.brutal-nav-link {
  color: #ffffff;
  text-decoration: none;
  font-weight: 700;
  font-size: 18px;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 0.5rem 1rem;
  border: 2px solid transparent;
  transition: all 0.15s ease;
}

.brutal-nav-link:hover {
  border: 2px solid #ffffff;
  background: #ff0000;
  color: #000000;
}

.brutal-nav-link.active {
  border: 2px solid #ff0000;
  background: #ff0000;
  color: #000000;
}

/* 搜索框 */
.brutal-nav-search {
  padding: 0.75rem 1rem;
  background: #000000;
  border: 2px solid #ffffff;
  color: #ffffff;
  font-weight: 700;
  text-transform: uppercase;
  width: 180px;
  font-size: 16px;
}

.brutal-nav-search:focus {
  outline: none;
  border-color: #ff0000;
}

/* 用户头像 */
.brutal-nav-avatar {
  width: 50px;
  height: 50px;
  background: #ffffff;
  color: #000000;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 18px;
}
```

### 7. 卡片网格（Bento Grid）

**Brutalist 网格系统**:
- 不规则布局
- 明显的边框分隔
- 不同尺寸的色块
- 轻微的旋转或位移

**完整 CSS 实现**:
```css
/* Bento 容器 */
.brutal-bento {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

/* 标准网格项 */
.brutal-bento-item {
  background: #ffffff;
  border: 4px solid #000000;
  padding: 2rem;
  box-shadow: 6px 6px 0 #000000;
  transition: all 0.2s ease;
}

.brutal-bento-item:hover {
  transform: translate(-3px, -3px) rotate(-1deg);
  box-shadow: 9px 9px 0 #000000;
}

/* 大型项（占 2 列） */
.brutal-bento-item-large {
  grid-column: span 2;
  background: #ffff00;
  border: 5px solid #000000;
  box-shadow: 8px 8px 0 #000000;
}

/* 特大项（占 2x2） */
.brutal-bento-item-xlarge {
  grid-column: span 2;
  grid-row: span 2;
  background: #ff0000;
  color: #ffffff;
  border: 6px solid #000000;
  box-shadow: 10px 10px 0 #000000;
}

/* 高项（占 2 行） */
.brutal-bento-item-tall {
  grid-row: span 2;
  background: #00ffff;
  border: 4px solid #000000;
}

/* 倾斜项 */
.brutal-bento-item-tilted {
  transform: rotate(-2deg);
  background: #ff00ff;
  border: 4px solid #000000;
  box-shadow: 8px 8px 0 #000000;
}

.brutal-bento-item-tilted:hover {
  transform: rotate(-1deg) translate(-2px, -2px);
  box-shadow: 10px 10px 0 #000000;
}

/* 响应式 */
@media (max-width: 1024px) {
  .brutal-bento {
    grid-template-columns: repeat(2, 1fr);
  }

  .brutal-bento-item-xlarge {
    grid-column: span 1;
    grid-row: span 1;
  }
}

@media (max-width: 768px) {
  .brutal-bento {
    grid-template-columns: 1fr;
  }

  .brutal-bento-item-large,
  .brutal-bento-item-tall {
    grid-column: span 1;
    grid-row: span 1;
  }
}
```

## 完整 Tailwind 配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        brutal: {
          black: '#000000',
          white: '#ffffff',
          gray: {
            dark: '#1a1a1a',
            light: '#e5e5e5',
          },
          red: '#ff0000',
          blue: '#0000ff',
          green: '#00ff00',
          yellow: '#ffff00',
          cyan: '#00ffff',
          magenta: '#ff00ff',
          orange: '#ff6600',
          pink: '#ff3399',
          purple: '#9900ff',
        },
      },
      borderWidth: {
        '3': '3px',
        '6': '6px',
        '8': '8px',
      },
      borderRadius: {
        'none': '0',
      },
      boxShadow: {
        'brutal-sm': '2px 2px 0 #000000',
        'brutal': '4px 4px 0 #000000',
        'brutal-md': '6px 6px 0 #000000',
        'brutal-lg': '8px 8px 0 #000000',
        'brutal-xl': '10px 10px 0 #000000',
        'brutal-red': '6px 6px 0 #ff0000',
        'brutal-yellow': '6px 6px 0 #ffff00',
        'brutal-inset': 'inset 4px 4px 0 #000000',
      },
      fontFamily: {
        'brutal': ['Arial', 'Helvetica', 'sans-serif'],
        'mono': ['Courier New', 'monospace'],
      },
    },
  },
};
```

## 间距系统

```css
/* 推荐间距 */
--brutal-space-xs: 0.5rem;     /* 8px */
--brutal-space-sm: 1rem;       /* 16px */
--brutal-space-md: 1.5rem;     /* 24px */
--brutal-space-lg: 2rem;       /* 32px */
--brutal-space-xl: 3rem;       /* 48px */
--brutal-space-2xl: 4rem;      /* 64px */

/* 内边距 */
--brutal-padding-btn: 1rem 2rem;
--brutal-padding-card: 2rem;
--brutal-padding-input: 1rem 1.5rem;
--brutal-padding-nav: 2rem;
```

## 字体系统

```css
/* 推荐字体 */
font-family: Arial, Helvetica, sans-serif;
/* 等宽字体（用于代码或强调） */
font-family: 'Courier New', Courier, monospace;

/* 字重 */
--brutal-font-regular: 400;
--brutal-font-bold: 700;
--brutal-font-black: 900;

/* 字体大小 */
--brutal-text-xs: 0.75rem;     /* 12px */
--brutal-text-sm: 0.875rem;    /* 14px */
--brutal-text-base: 1rem;      /* 16px */
--brutal-text-lg: 1.125rem;    /* 18px */
--brutal-text-xl: 1.25rem;     /* 20px */
--brutal-text-2xl: 1.5rem;     /* 24px */
--brutal-text-3xl: 2rem;       /* 32px */
--brutal-text-4xl: 3rem;       /* 48px */
--brutal-text-5xl: 4rem;       /* 64px */
--brutal-text-6xl: 6rem;       /* 96px */

/* 字母间距 */
--brutal-tracking-tight: -0.05em;
--brutal-tracking-normal: 0;
--brutal-tracking-wide: 0.05em;
--brutal-tracking-wider: 0.1em;
--brutal-tracking-widest: 0.2em;
```

## 边框系统

```css
/* 边框粗细 */
--brutal-border-thin: 2px;
--brutal-border-default: 3px;
--brutal-border-medium: 4px;
--brutal-border-thick: 6px;
--brutal-border-extra-thick: 8px;

/* 边框样式 */
--brutal-border-style: solid;
--brutal-border-color: #000000;
```

## 阴影系统

```css
/* 硬阴影等级 */
--brutal-shadow-xs: 2px 2px 0 #000000;
--brutal-shadow-sm: 3px 3px 0 #000000;
--brutal-shadow-md: 4px 4px 0 #000000;
--brutal-shadow-lg: 6px 6px 0 #000000;
--brutal-shadow-xl: 8px 8px 0 #000000;
--brutal-shadow-2xl: 10px 10px 0 #000000;

/* 彩色阴影 */
--brutal-shadow-red: 6px 6px 0 #ff0000;
--brutal-shadow-yellow: 6px 6px 0 #ffff00;
--brutal-shadow-cyan: 6px 6px 0 #00ffff;

/* 内阴影 */
--brutal-shadow-inset: inset 4px 4px 0 #000000;
```

## 重要事项（Important Notes）

1. **零圆角铁律**: 绝对禁止 `border-radius > 0`，所有元素必须是锐利的直角
2. **粗黑边框必须**: 每个可见元素都应有明显的黑色边框（2-8px）
3. **硬阴影唯一**: 阴影的 `blur` 值必须为 0，只能使用偏移量
4. **高饱和度**: 使用纯色或接近 100% 饱和度的颜色，避免灰调色彩
5. **全大写标题**: 重要文字使用全大写 + 加粗 + 字母间距
6. **极简动画**: 仅使用简单的 `transform` 和 `box-shadow` 变化，禁止复杂过渡
7. **可访问性**: 确保黑底白字或白底黑字的对比度足够（21:1）

## 禁止事项（Things to Avoid）

❌ **不要使用圆角**: `border-radius: 0` 是唯一选择
❌ **不要使用渐变**: 只能使用纯色填充，禁止 `linear-gradient` 或 `radial-gradient`
❌ **不要使用模糊阴影**: `box-shadow` 的第三个值必须为 0
❌ **不要使用半透明**: `rgba()` 的 alpha 值必须是 1.0（完全不透明）
❌ **不要使用柔和色**: 避免低饱和度的灰调色彩
❌ **不要使用衬线字体**: 只能使用无衬线字体（Arial, Helvetica）或等宽字体
❌ **不要过度动画**: 避免缓动函数、弹跳效果或复杂的关键帧动画
❌ **不要使用细边框**: 边框粗细不能小于 2px

---

## English Version (en-US)

### Design Overview
Generate **Neo-Brutalism** style interface design for products. This is a design movement that opposes over-decoration, creating raw, direct, and uncompromising digital experiences through thick black borders, high-saturation color blocks, hard shadows, and zero border radius. Every element looks like it was drawn directly on white paper with a marker and ruler, rejecting any visual sugar coating.

## Core Design Requirements

### 1. Brutal Borders System

**Border Principles**:
- All elements must have obvious black borders
- Border thickness: 2-4px (standard), 6-8px (emphasis)
- Border color: Pure black `#000000` or dark gray `#1a1a1a`
- Absolutely no rounded corners: `border-radius: 0`

**Complete CSS Implementation**:
```css
/* Standard container border */
.brutal-card {
  background: #ffffff;
  border: 3px solid #000000;
  border-radius: 0;
  padding: 2rem;
  position: relative;
  transition: all 0.2s ease;
}

.brutal-card:hover {
  /* Border thickens on hover */
  border-width: 4px;
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0 #000000;
}

/* Emphasis border (thicker) */
.brutal-card-emphasis {
  background: #ffff00;
  border: 6px solid #000000;
  padding: 2.5rem;
  box-shadow: 8px 8px 0 #000000;
}

/* Nested border effect */
.brutal-card-nested {
  background: #ff0000;
  border: 4px solid #000000;
  padding: 0.5rem;
}

.brutal-card-nested .inner {
  background: #ffffff;
  border: 3px solid #000000;
  padding: 1.5rem;
}

/* Duotone border */
.brutal-card-duotone {
  background: #00ff00;
  border: 4px solid #000000;
  box-shadow:
    0 0 0 8px #ffffff,
    0 0 0 12px #000000;
}
```

### 2. Hard Shadows System

**Shadow Principles**:
- Absolutely no blur: `blur = 0`
- Obvious offset: typically 4-8px
- Solid color shadows: black or matching primary color
- Shadows always toward bottom-right

**Complete CSS Implementation**:
```css
/* Standard hard shadow */
.brutal-shadow {
  box-shadow: 4px 4px 0 #000000;
}

.brutal-shadow:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 #000000;
}

.brutal-shadow:active {
  transform: translate(2px, 2px);
  box-shadow: 2px 2px 0 #000000;
}

/* Large hard shadow */
.brutal-shadow-large {
  box-shadow: 8px 8px 0 #000000;
}

/* Colored hard shadow */
.brutal-shadow-color {
  background: #ff0000;
  border: 3px solid #000000;
  box-shadow: 6px 6px 0 #ffff00;
}

/* Layered hard shadows */
.brutal-shadow-layered {
  background: #00ffff;
  border: 3px solid #000000;
  box-shadow:
    4px 4px 0 #000000,
    8px 8px 0 #ff00ff;
}

/* Inset hard shadow */
.brutal-shadow-inset {
  background: #f0f0f0;
  border: 3px solid #000000;
  box-shadow: inset 4px 4px 0 #000000;
}
```

### 3. High-Saturation Color System (Candy Colors)

**Color Principles**:
- Use pure, high-saturation colors (100%)
- Avoid gradients and transparency
- Black and white as base colors
- Candy colors as accents

**Complete Color Scheme**:
```css
:root {
  /* Base Colors */
  --brutal-black: #000000;
  --brutal-white: #ffffff;
  --brutal-gray-dark: #1a1a1a;
  --brutal-gray-light: #e5e5e5;

  /* Candy Colors (100% saturation) */
  --brutal-red: #ff0000;
  --brutal-blue: #0000ff;
  --brutal-green: #00ff00;
  --brutal-yellow: #ffff00;
  --brutal-cyan: #00ffff;
  --brutal-magenta: #ff00ff;
  --brutal-orange: #ff6600;
  --brutal-pink: #ff3399;
  --brutal-purple: #9900ff;

  /* Soft candy colors (80% saturation) */
  --brutal-red-soft: #ff4d4d;
  --brutal-blue-soft: #4d4dff;
  --brutal-green-soft: #4dff4d;
  --brutal-yellow-soft: #ffff4d;
  --brutal-orange-soft: #ff884d;
  --brutal-pink-soft: #ff66b3;
}
```

### 4. Button Design

**Button Raw Power**:
- All uppercase text
- Thick black borders
- Hard shadows
- Simple transform animations

**Complete CSS Implementation**:
```css
/* Primary button (red background, black text) */
.brutal-btn-primary {
  background: #ff0000;
  color: #000000;
  border: 3px solid #000000;
  padding: 1rem 2rem;
  font-size: 18px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  cursor: pointer;
  box-shadow: 4px 4px 0 #000000;
  transition: all 0.15s ease;
}

.brutal-btn-primary:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 #000000;
}

.brutal-btn-primary:active {
  transform: translate(2px, 2px);
  box-shadow: 2px 2px 0 #000000;
}

/* Secondary button (white background, black border) */
.brutal-btn-secondary {
  background: #ffffff;
  color: #000000;
  border: 4px solid #000000;
  padding: 1rem 2rem;
  font-size: 18px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  cursor: pointer;
  box-shadow: 4px 4px 0 #000000;
  transition: all 0.15s ease;
}

.brutal-btn-secondary:hover {
  background: #000000;
  color: #ffffff;
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 #ff0000;
}

/* Large button */
.brutal-btn-large {
  padding: 1.5rem 3rem;
  font-size: 24px;
  border: 4px solid #000000;
  box-shadow: 8px 8px 0 #000000;
}

/* Icon button (square) */
.brutal-btn-icon {
  width: 60px;
  height: 60px;
  background: #ffff00;
  border: 3px solid #000000;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  font-weight: 900;
  cursor: pointer;
  box-shadow: 4px 4px 0 #000000;
  transition: all 0.15s ease;
}

.brutal-btn-icon:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 #000000;
}

/* Disabled state */
.brutal-btn-disabled {
  background: #e5e5e5;
  color: #999999;
  border: 3px solid #999999;
  box-shadow: 4px 4px 0 #999999;
  cursor: not-allowed;
  opacity: 0.6;
}
```

### 5. Form Elements

**Form Minimalism**:
- Thick black borders
- Zero border radius
- All uppercase labels
- Red border on focus

**Complete CSS Implementation**:
```css
/* Text input */
.brutal-input {
  width: 100%;
  padding: 1rem 1.5rem;
  background: #ffffff;
  border: 3px solid #000000;
  border-radius: 0;
  font-size: 16px;
  font-weight: 700;
  color: #000000;
  transition: all 0.2s ease;
}

.brutal-input:focus {
  outline: none;
  border-color: #ff0000;
  box-shadow: 4px 4px 0 #ff0000;
}

.brutal-input::placeholder {
  color: #999999;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* Textarea */
.brutal-textarea {
  width: 100%;
  padding: 1rem 1.5rem;
  background: #ffffff;
  border: 3px solid #000000;
  border-radius: 0;
  font-size: 16px;
  font-weight: 700;
  color: #000000;
  min-height: 150px;
  resize: vertical;
  font-family: inherit;
  line-height: 1.6;
  transition: all 0.2s ease;
}

.brutal-textarea:focus {
  outline: none;
  border-color: #ff0000;
  box-shadow: 4px 4px 0 #ff0000;
}

/* Label */
.brutal-label {
  display: block;
  font-size: 14px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #000000;
  margin-bottom: 0.5rem;
}

/* Custom checkbox */
.brutal-checkbox-wrapper {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  cursor: pointer;
}

.brutal-checkbox {
  appearance: none;
  width: 32px;
  height: 32px;
  background: #ffffff;
  border: 3px solid #000000;
  cursor: pointer;
  position: relative;
  transition: all 0.15s ease;
}

.brutal-checkbox:checked {
  background: #ff0000;
  box-shadow: inset 4px 4px 0 #000000;
}

.brutal-checkbox:checked::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #ffffff;
  font-size: 24px;
  font-weight: 900;
}

/* Select dropdown */
.brutal-select {
  width: 100%;
  padding: 1rem 1.5rem;
  background: #ffffff;
  border: 3px solid #000000;
  border-radius: 0;
  font-size: 16px;
  font-weight: 700;
  color: #000000;
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M5 7L10 12L15 7' stroke='%23000000' stroke-width='3' stroke-linecap='square'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  padding-right: 3rem;
  transition: all 0.2s ease;
}

.brutal-select:focus {
  outline: none;
  border-color: #ff0000;
  box-shadow: 4px 4px 0 #ff0000;
}
```

### 6. Navigation Bar

**Navigation Presence**:
- Fixed top or bottom
- Black background + white text
- Red border emphasis
- All uppercase links

**Complete CSS Implementation**:
```css
/* Fixed navigation */
.brutal-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: #000000;
  color: #ffffff;
  padding: 2rem;
  border-bottom: 6px solid #ff0000;
}

.brutal-nav-content {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Logo */
.brutal-logo {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brutal-logo-icon {
  width: 60px;
  height: 60px;
  background: #ff0000;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  font-weight: 900;
  color: #000000;
}

.brutal-logo-text {
  font-size: 28px;
  font-weight: 900;
  letter-spacing: 2px;
  text-transform: uppercase;
}

/* Navigation menu */
.brutal-nav-menu {
  display: flex;
  list-style: none;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.brutal-nav-link {
  color: #ffffff;
  text-decoration: none;
  font-weight: 700;
  font-size: 18px;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 0.5rem 1rem;
  border: 2px solid transparent;
  transition: all 0.15s ease;
}

.brutal-nav-link:hover {
  border: 2px solid #ffffff;
  background: #ff0000;
  color: #000000;
}

.brutal-nav-link.active {
  border: 2px solid #ff0000;
  background: #ff0000;
  color: #000000;
}

/* Search input */
.brutal-nav-search {
  padding: 0.75rem 1rem;
  background: #000000;
  border: 2px solid #ffffff;
  color: #ffffff;
  font-weight: 700;
  text-transform: uppercase;
  width: 180px;
  font-size: 16px;
}

.brutal-nav-search:focus {
  outline: none;
  border-color: #ff0000;
}

/* User avatar */
.brutal-nav-avatar {
  width: 50px;
  height: 50px;
  background: #ffffff;
  color: #000000;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 18px;
}
```

### 7. Bento Grid

**Brutalist Grid System**:
- Irregular layout
- Obvious border separation
- Different sized color blocks
- Slight rotation or offset

**Complete CSS Implementation**:
```css
/* Bento container */
.brutal-bento {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

/* Standard grid item */
.brutal-bento-item {
  background: #ffffff;
  border: 4px solid #000000;
  padding: 2rem;
  box-shadow: 6px 6px 0 #000000;
  transition: all 0.2s ease;
}

.brutal-bento-item:hover {
  transform: translate(-3px, -3px) rotate(-1deg);
  box-shadow: 9px 9px 0 #000000;
}

/* Large item (2 columns) */
.brutal-bento-item-large {
  grid-column: span 2;
  background: #ffff00;
  border: 5px solid #000000;
  box-shadow: 8px 8px 0 #000000;
}

/* Extra large item (2x2) */
.brutal-bento-item-xlarge {
  grid-column: span 2;
  grid-row: span 2;
  background: #ff0000;
  color: #ffffff;
  border: 6px solid #000000;
  box-shadow: 10px 10px 0 #000000;
}

/* Tall item (2 rows) */
.brutal-bento-item-tall {
  grid-row: span 2;
  background: #00ffff;
  border: 4px solid #000000;
}

/* Tilted item */
.brutal-bento-item-tilted {
  transform: rotate(-2deg);
  background: #ff00ff;
  border: 4px solid #000000;
  box-shadow: 8px 8px 0 #000000;
}

.brutal-bento-item-tilted:hover {
  transform: rotate(-1deg) translate(-2px, -2px);
  box-shadow: 10px 10px 0 #000000;
}

/* Responsive */
@media (max-width: 1024px) {
  .brutal-bento {
    grid-template-columns: repeat(2, 1fr);
  }

  .brutal-bento-item-xlarge {
    grid-column: span 1;
    grid-row: span 1;
  }
}

@media (max-width: 768px) {
  .brutal-bento {
    grid-template-columns: 1fr;
  }

  .brutal-bento-item-large,
  .brutal-bento-item-tall {
    grid-column: span 1;
    grid-row: span 1;
  }
}
```

## Complete Tailwind Configuration

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        brutal: {
          black: '#000000',
          white: '#ffffff',
          gray: {
            dark: '#1a1a1a',
            light: '#e5e5e5',
          },
          red: '#ff0000',
          blue: '#0000ff',
          green: '#00ff00',
          yellow: '#ffff00',
          cyan: '#00ffff',
          magenta: '#ff00ff',
          orange: '#ff6600',
          pink: '#ff3399',
          purple: '#9900ff',
        },
      },
      borderWidth: {
        '3': '3px',
        '6': '6px',
        '8': '8px',
      },
      borderRadius: {
        'none': '0',
      },
      boxShadow: {
        'brutal-sm': '2px 2px 0 #000000',
        'brutal': '4px 4px 0 #000000',
        'brutal-md': '6px 6px 0 #000000',
        'brutal-lg': '8px 8px 0 #000000',
        'brutal-xl': '10px 10px 0 #000000',
        'brutal-red': '6px 6px 0 #ff0000',
        'brutal-yellow': '6px 6px 0 #ffff00',
        'brutal-inset': 'inset 4px 4px 0 #000000',
      },
      fontFamily: {
        'brutal': ['Arial', 'Helvetica', 'sans-serif'],
        'mono': ['Courier New', 'monospace'],
      },
    },
  },
};
```

## Spacing System

```css
/* Recommended spacing */
--brutal-space-xs: 0.5rem;     /* 8px */
--brutal-space-sm: 1rem;       /* 16px */
--brutal-space-md: 1.5rem;     /* 24px */
--brutal-space-lg: 2rem;       /* 32px */
--brutal-space-xl: 3rem;       /* 48px */
--brutal-space-2xl: 4rem;      /* 64px */

/* Padding */
--brutal-padding-btn: 1rem 2rem;
--brutal-padding-card: 2rem;
--brutal-padding-input: 1rem 1.5rem;
--brutal-padding-nav: 2rem;
```

## Typography System

```css
/* Recommended fonts */
font-family: Arial, Helvetica, sans-serif;
/* Monospace font (for code or emphasis) */
font-family: 'Courier New', Courier, monospace;

/* Font weights */
--brutal-font-regular: 400;
--brutal-font-bold: 700;
--brutal-font-black: 900;

/* Font sizes */
--brutal-text-xs: 0.75rem;     /* 12px */
--brutal-text-sm: 0.875rem;    /* 14px */
--brutal-text-base: 1rem;      /* 16px */
--brutal-text-lg: 1.125rem;    /* 18px */
--brutal-text-xl: 1.25rem;     /* 20px */
--brutal-text-2xl: 1.5rem;     /* 24px */
--brutal-text-3xl: 2rem;       /* 32px */
--brutal-text-4xl: 3rem;       /* 48px */
--brutal-text-5xl: 4rem;       /* 64px */
--brutal-text-6xl: 6rem;       /* 96px */

/* Letter spacing */
--brutal-tracking-tight: -0.05em;
--brutal-tracking-normal: 0;
--brutal-tracking-wide: 0.05em;
--brutal-tracking-wider: 0.1em;
--brutal-tracking-widest: 0.2em;
```

## Border System

```css
/* Border thickness */
--brutal-border-thin: 2px;
--brutal-border-default: 3px;
--brutal-border-medium: 4px;
--brutal-border-thick: 6px;
--brutal-border-extra-thick: 8px;

/* Border style */
--brutal-border-style: solid;
--brutal-border-color: #000000;
```

## Shadow System

```css
/* Hard shadow levels */
--brutal-shadow-xs: 2px 2px 0 #000000;
--brutal-shadow-sm: 3px 3px 0 #000000;
--brutal-shadow-md: 4px 4px 0 #000000;
--brutal-shadow-lg: 6px 6px 0 #000000;
--brutal-shadow-xl: 8px 8px 0 #000000;
--brutal-shadow-2xl: 10px 10px 0 #000000;

/* Colored shadows */
--brutal-shadow-red: 6px 6px 0 #ff0000;
--brutal-shadow-yellow: 6px 6px 0 #ffff00;
--brutal-shadow-cyan: 6px 6px 0 #00ffff;

/* Inset shadow */
--brutal-shadow-inset: inset 4px 4px 0 #000000;
```

## Important Notes

1. **Zero Border Radius Rule**: Absolutely no `border-radius > 0`, all elements must have sharp right angles
2. **Thick Black Borders Required**: Every visible element should have obvious black borders (2-8px)
3. **Hard Shadows Only**: Shadow `blur` value must be 0, only use offsets
4. **High Saturation**: Use pure colors or near 100% saturation, avoid muted colors
5. **All Caps Titles**: Important text uses all uppercase + bold + letter spacing
6. **Minimal Animation**: Only use simple `transform` and `box-shadow` changes, no complex transitions
7. **Accessibility**: Ensure sufficient contrast for black-on-white or white-on-black (21:1)

## Things to Avoid

❌ **Don't use rounded corners**: `border-radius: 0` is the only option
❌ **Don't use gradients**: Only solid color fills, no `linear-gradient` or `radial-gradient`
❌ **Don't use blurred shadows**: `box-shadow` third value must be 0
❌ **Don't use transparency**: `rgba()` alpha value must be 1.0 (fully opaque)
❌ **Don't use muted colors**: Avoid low-saturation gray-toned colors
❌ **Don't use serif fonts**: Only sans-serif (Arial, Helvetica) or monospace fonts
❌ **Don't over-animate**: Avoid easing functions, bounce effects, or complex keyframe animations
❌ **Don't use thin borders**: Border thickness cannot be less than 2px
