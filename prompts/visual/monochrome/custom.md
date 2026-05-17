# Custom Prompt: Monochrome（单色/黑白设计）

## 中文版本 (zh-CN)

### 1. 设计哲学与核心原则

**Monochrome（单色设计）**是一种仅使用**黑、白、灰**三个颜色维度的极简主义设计风格。这种风格的核心在于**用明度对比代替色相对比**，通过**严谨的排版、精确的网格、充足的留白**来构建信息层级，传递理性、专业、冷静的气质。

**设计原则**：
- **色彩极简**：严格限制在黑白灰色阶，不引入任何饱和色
- **对比为王**：用明度差异创造视觉层级，确保可读性
- **排版主导**：字重、字号、字距成为主要的设计语言
- **网格严谨**：所有间距对齐到 4px 或 8px 基准网格
- **留白充足**：让空白空间本身成为设计元素

### 2. 核心设计要求

#### 2.1 黑白灰配色系统（Grayscale Color Palette）

Monochrome 的配色系统是一套**精心校准的灰阶体系**，从纯白到纯黑分为多个等级，每个等级都有明确的用途。

**完整灰阶定义**：

```css
:root {
  /* 纯白（Pure White） */
  --mono-white: #FFFFFF;

  /* 极浅灰（Extra Light Gray）- 页面背景 */
  --mono-gray-50: #F9FAFB;
  --mono-gray-100: #F3F4F6;

  /* 浅灰（Light Gray）- 卡片背景、分隔线 */
  --mono-gray-200: #E5E7EB;
  --mono-gray-300: #D1D5DB;

  /* 中灰（Medium Gray）- 次要边框、辅助文字 */
  --mono-gray-400: #9CA3AF;
  --mono-gray-500: #6B7280;

  /* 深灰（Dark Gray）- 正文文字、重要元素 */
  --mono-gray-600: #4B5563;
  --mono-gray-700: #374151;

  /* 极深灰（Extra Dark Gray）- 标题、强调文字 */
  --mono-gray-800: #1F2937;
  --mono-gray-900: #111827;

  /* 纯黑（Pure Black） */
  --mono-black: #000000;
}
```

**配色规则**：

```css
/* 背景色规则 */
.mono-bg-page {
  background: var(--mono-gray-50); /* 页面主背景 */
}

.mono-bg-section {
  background: var(--mono-gray-100); /* 区块背景 */
}

.mono-bg-card {
  background: var(--mono-white); /* 卡片背景 */
}

.mono-bg-dark {
  background: linear-gradient(135deg, var(--mono-black), var(--mono-gray-800)); /* 深色 Hero 背景 */
}

/* 文本色规则 */
.mono-text-primary {
  color: var(--mono-black); /* 主标题 */
}

.mono-text-heading {
  color: var(--mono-gray-900); /* 次标题 */
}

.mono-text-body {
  color: var(--mono-gray-700); /* 正文 */
}

.mono-text-secondary {
  color: var(--mono-gray-600); /* 次要文字 */
}

.mono-text-muted {
  color: var(--mono-gray-500); /* 辅助文字 */
}

.mono-text-placeholder {
  color: var(--mono-gray-400); /* 占位文字 */
}

/* 边框色规则 */
.mono-border-light {
  border-color: var(--mono-gray-200); /* 浅边框 */
}

.mono-border-medium {
  border-color: var(--mono-gray-300); /* 中等边框 */
}

.mono-border-dark {
  border-color: var(--mono-gray-400); /* 深边框 */
}

.mono-border-strong {
  border-color: var(--mono-black); /* 强调边框 */
}
```

**对比度标准**：
- **主标题 vs 背景**：对比度 ≥ 7:1（WCAG AAA）
- **正文 vs 背景**：对比度 ≥ 4.5:1（WCAG AA）
- **辅助文字 vs 背景**：对比度 ≥ 3:1

#### 2.2 字体排版系统（Typography System）

Monochrome 设计中，**排版即设计**。通过字重、字号、行高、字距的精确控制创造视觉层级。

**字体族定义**：
```css
:root {
  /* 主字体：无衬线字体（适合屏幕阅读） */
  --mono-font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', sans-serif;

  /* 等宽字体：代码、数字 */
  --mono-font-mono: 'SF Mono', 'Monaco', 'Inconsolata', 'Fira Code', 'Courier New', monospace;

  /* 字重 */
  --mono-weight-regular: 400;
  --mono-weight-medium: 500;
  --mono-weight-semibold: 600;
  --mono-weight-bold: 700;
  --mono-weight-extrabold: 800;
  --mono-weight-black: 900;
}
```

**字体等级系统**：

```css
/* 超大标题（Hero Title） */
.mono-text-hero {
  font-family: var(--mono-font-sans);
  font-size: 3rem; /* 48px */
  font-weight: var(--mono-weight-black); /* 900 */
  line-height: 1.1;
  letter-spacing: -0.02em; /* 紧凑字距 */
  color: var(--mono-black);
}

/* 主标题（Main Heading） */
.mono-text-h1 {
  font-family: var(--mono-font-sans);
  font-size: 2.25rem; /* 36px */
  font-weight: var(--mono-weight-extrabold); /* 800 */
  line-height: 1.2;
  letter-spacing: -0.01em;
  color: var(--mono-gray-900);
}

/* 次标题（Sub Heading） */
.mono-text-h2 {
  font-family: var(--mono-font-sans);
  font-size: 1.875rem; /* 30px */
  font-weight: var(--mono-weight-bold); /* 700 */
  line-height: 1.25;
  letter-spacing: -0.01em;
  color: var(--mono-gray-900);
}

/* 小标题（Section Title） */
.mono-text-h3 {
  font-family: var(--mono-font-sans);
  font-size: 1.5rem; /* 24px */
  font-weight: var(--mono-weight-bold); /* 700 */
  line-height: 1.3;
  letter-spacing: 0;
  color: var(--mono-gray-900);
}

/* 卡片标题（Card Title） */
.mono-text-h4 {
  font-family: var(--mono-font-sans);
  font-size: 1.125rem; /* 18px */
  font-weight: var(--mono-weight-semibold); /* 600 */
  line-height: 1.4;
  color: var(--mono-gray-900);
}

/* 大正文（Large Body） */
.mono-text-lg {
  font-family: var(--mono-font-sans);
  font-size: 1.125rem; /* 18px */
  font-weight: var(--mono-weight-regular); /* 400 */
  line-height: 1.6;
  color: var(--mono-gray-700);
}

/* 标准正文（Base Body） */
.mono-text-base {
  font-family: var(--mono-font-sans);
  font-size: 1rem; /* 16px */
  font-weight: var(--mono-weight-regular); /* 400 */
  line-height: 1.5;
  color: var(--mono-gray-700);
}

/* 小文字（Small Text） */
.mono-text-sm {
  font-family: var(--mono-font-sans);
  font-size: 0.875rem; /* 14px */
  font-weight: var(--mono-weight-medium); /* 500 */
  line-height: 1.4;
  color: var(--mono-gray-600);
}

/* 极小文字（Extra Small） */
.mono-text-xs {
  font-family: var(--mono-font-sans);
  font-size: 0.75rem; /* 12px */
  font-weight: var(--mono-weight-medium); /* 500 */
  line-height: 1.3;
  color: var(--mono-gray-500);
}

/* 数字（Numeric） */
.mono-text-numeric {
  font-family: var(--mono-font-mono);
  font-size: 2.25rem; /* 36px */
  font-weight: var(--mono-weight-black); /* 900 */
  line-height: 1;
  color: var(--mono-black);
  font-feature-settings: 'tnum'; /* 等宽数字 */
}
```

#### 2.3 间距网格系统（Spacing Grid System）

所有间距严格对齐到 **4px 基准网格**，确保视觉一致性。

```css
:root {
  /* 间距等级（基于 4px） */
  --mono-space-0: 0;
  --mono-space-1: 0.25rem; /* 4px */
  --mono-space-2: 0.5rem;  /* 8px */
  --mono-space-3: 0.75rem; /* 12px */
  --mono-space-4: 1rem;    /* 16px */
  --mono-space-5: 1.25rem; /* 20px */
  --mono-space-6: 1.5rem;  /* 24px */
  --mono-space-8: 2rem;    /* 32px */
  --mono-space-10: 2.5rem; /* 40px */
  --mono-space-12: 3rem;   /* 48px */
  --mono-space-16: 4rem;   /* 64px */
  --mono-space-20: 5rem;   /* 80px */
  --mono-space-24: 6rem;   /* 96px */

  /* 圆角（基于 4px） */
  --mono-radius-sm: 0.25rem; /* 4px */
  --mono-radius-md: 0.5rem;  /* 8px */
  --mono-radius-lg: 0.75rem; /* 12px */
  --mono-radius-xl: 1rem;    /* 16px */
  --mono-radius-2xl: 1.5rem; /* 24px */
  --mono-radius-full: 9999px;
}
```

**间距使用规则**：
```css
/* 卡片内边距 */
.mono-card-padding {
  padding: var(--mono-space-6); /* 24px */
}

/* 区块间距 */
.mono-section-spacing {
  margin-bottom: var(--mono-space-12); /* 48px */
}

/* 元素间隙 */
.mono-gap-sm { gap: var(--mono-space-2); } /* 8px */
.mono-gap-md { gap: var(--mono-space-4); } /* 16px */
.mono-gap-lg { gap: var(--mono-space-6); } /* 24px */
```

#### 2.4 卡片与容器系统（Card & Container System）

卡片使用**白色背景、浅灰边框、柔和阴影**，悬停时增强阴影。

```css
/* 基础卡片 */
.mono-card {
  background: var(--mono-white);
  border: 1px solid var(--mono-gray-200);
  border-radius: var(--mono-radius-xl); /* 16px */
  padding: var(--mono-space-6); /* 24px */
  box-shadow:
    0 1px 3px rgba(0, 0, 0, 0.05),
    0 1px 2px rgba(0, 0, 0, 0.06);
  transition: all 0.2s ease-out;
}

.mono-card:hover {
  border-color: var(--mono-gray-300);
  box-shadow:
    0 10px 20px rgba(0, 0, 0, 0.08),
    0 4px 8px rgba(0, 0, 0, 0.06);
  transform: translateY(-2px);
}

/* 统计卡片 */
.mono-stat-card {
  background: var(--mono-white);
  border: 1px solid var(--mono-gray-200);
  border-radius: var(--mono-radius-xl);
  padding: var(--mono-space-6);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.mono-stat-card:hover {
  box-shadow:
    0 20px 40px rgba(0, 0, 0, 0.1),
    0 8px 16px rgba(0, 0, 0, 0.08);
  transform: translateY(-4px);
}

/* 卡片图标容器 */
.mono-card-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--mono-black), var(--mono-gray-700));
  border-radius: var(--mono-radius-lg); /* 12px */
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--mono-white);
}

/* 卡片徽章 */
.mono-card-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.5rem;
  background: var(--mono-black);
  color: var(--mono-white);
  font-size: 0.75rem;
  font-weight: var(--mono-weight-bold);
  border-radius: var(--mono-radius-sm);
}

/* 容器 */
.mono-container {
  max-width: 1280px;
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--mono-space-6);
  padding-right: var(--mono-space-6);
}

.mono-container-sm {
  max-width: 640px;
}

.mono-container-md {
  max-width: 768px;
}

.mono-container-lg {
  max-width: 1024px;
}

.mono-container-xl {
  max-width: 1280px;
}
```

#### 2.5 按钮系统（Button System）

按钮使用**黑白反转**或**边框轮廓**，悬停时调整灰度。

```css
/* 主按钮（黑底白字） */
.mono-btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.5rem;
  background: var(--mono-black);
  color: var(--mono-white);
  font-family: var(--mono-font-sans);
  font-size: 0.875rem;
  font-weight: var(--mono-weight-bold);
  border: none;
  border-radius: var(--mono-radius-lg);
  cursor: pointer;
  transition: all 0.2s ease-out;
}

.mono-btn-primary:hover {
  background: var(--mono-gray-800);
  transform: translateY(-1px);
  box-shadow:
    0 4px 12px rgba(0, 0, 0, 0.15),
    0 2px 4px rgba(0, 0, 0, 0.12);
}

.mono-btn-primary:active {
  transform: translateY(0);
  box-shadow:
    0 2px 4px rgba(0, 0, 0, 0.12),
    0 1px 2px rgba(0, 0, 0, 0.08);
}

/* 次要按钮（白底黑字） */
.mono-btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.5rem;
  background: var(--mono-white);
  color: var(--mono-black);
  font-family: var(--mono-font-sans);
  font-size: 0.875rem;
  font-weight: var(--mono-weight-bold);
  border: 2px solid var(--mono-black);
  border-radius: var(--mono-radius-lg);
  cursor: pointer;
  transition: all 0.2s ease-out;
}

.mono-btn-secondary:hover {
  background: var(--mono-gray-100);
  transform: translateY(-1px);
}

.mono-btn-secondary:active {
  transform: translateY(0);
  background: var(--mono-gray-200);
}

/* 轮廓按钮（透明底） */
.mono-btn-outline {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.5rem;
  background: transparent;
  color: var(--mono-gray-700);
  font-family: var(--mono-font-sans);
  font-size: 0.875rem;
  font-weight: var(--mono-weight-semibold);
  border: 1px solid var(--mono-gray-300);
  border-radius: var(--mono-radius-lg);
  cursor: pointer;
  transition: all 0.2s ease-out;
}

.mono-btn-outline:hover {
  border-color: var(--mono-gray-400);
  background: var(--mono-gray-50);
  color: var(--mono-black);
}

/* 幽灵按钮（深色背景用） */
.mono-btn-ghost {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.5rem;
  background: transparent;
  color: var(--mono-white);
  font-family: var(--mono-font-sans);
  font-size: 0.875rem;
  font-weight: var(--mono-weight-semibold);
  border: 2px solid var(--mono-white);
  border-radius: var(--mono-radius-lg);
  cursor: pointer;
  transition: all 0.3s ease-out;
}

.mono-btn-ghost:hover {
  background: var(--mono-white);
  color: var(--mono-black);
}

/* 按钮尺寸 */
.mono-btn-sm {
  padding: 0.5rem 1rem;
  font-size: 0.8125rem;
}

.mono-btn-lg {
  padding: 1rem 2rem;
  font-size: 1rem;
}
```

#### 2.6 表单元素系统（Form Elements）

表单使用**浅灰背景、细边框**，聚焦时边框加深。

```css
/* 文本输入框 */
.mono-input {
  width: 100%;
  padding: 0.75rem 1rem;
  background: var(--mono-gray-50);
  border: 1px solid var(--mono-gray-300);
  border-radius: var(--mono-radius-md);
  font-family: var(--mono-font-sans);
  font-size: 0.875rem;
  color: var(--mono-gray-900);
  transition: all 0.2s ease-out;
}

.mono-input::placeholder {
  color: var(--mono-gray-400);
}

.mono-input:focus {
  outline: none;
  background: var(--mono-white);
  border-color: var(--mono-black);
  box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.05);
}

.mono-input:disabled {
  background: var(--mono-gray-100);
  color: var(--mono-gray-500);
  cursor: not-allowed;
}

/* 文本域 */
.mono-textarea {
  width: 100%;
  min-height: 120px;
  padding: 0.75rem 1rem;
  background: var(--mono-gray-50);
  border: 1px solid var(--mono-gray-300);
  border-radius: var(--mono-radius-md);
  font-family: var(--mono-font-sans);
  font-size: 0.875rem;
  color: var(--mono-gray-900);
  resize: vertical;
  transition: all 0.2s ease-out;
}

.mono-textarea:focus {
  outline: none;
  background: var(--mono-white);
  border-color: var(--mono-black);
  box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.05);
}

/* 下拉选择 */
.mono-select {
  width: 100%;
  padding: 0.75rem 1rem;
  background: var(--mono-gray-50);
  border: 1px solid var(--mono-gray-300);
  border-radius: var(--mono-radius-md);
  font-family: var(--mono-font-sans);
  font-size: 0.875rem;
  color: var(--mono-gray-900);
  cursor: pointer;
  transition: all 0.2s ease-out;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg width='12' height='8' viewBox='0 0 12 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1L6 6L11 1' stroke='%234B5563' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  padding-right: 3rem;
}

.mono-select:focus {
  outline: none;
  background-color: var(--mono-white);
  border-color: var(--mono-black);
  box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.05);
}

/* 复选框 */
.mono-checkbox {
  appearance: none;
  width: 20px;
  height: 20px;
  border: 2px solid var(--mono-gray-300);
  border-radius: var(--mono-radius-sm);
  background: var(--mono-white);
  cursor: pointer;
  transition: all 0.2s ease-out;
  position: relative;
}

.mono-checkbox:checked {
  background: var(--mono-black);
  border-color: var(--mono-black);
}

.mono-checkbox:checked::after {
  content: '';
  position: absolute;
  top: 2px;
  left: 6px;
  width: 4px;
  height: 8px;
  border: solid var(--mono-white);
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.mono-checkbox:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.1);
}
```

#### 2.7 导航系统（Navigation System）

导航使用**白底、细分隔线**，链接悬停时加深。

```css
/* 顶部导航栏 */
.mono-nav {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: var(--mono-white);
  border-bottom: 1px solid var(--mono-gray-200);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.mono-nav-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 1rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Logo */
.mono-logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
}

.mono-logo-icon {
  width: 40px;
  height: 40px;
  background: var(--mono-black);
  border-radius: var(--mono-radius-lg);
  display: flex;
  align-items: center;
  justify-content: center;
}

.mono-logo-text {
  font-size: 1.25rem;
  font-weight: var(--mono-weight-black);
  letter-spacing: -0.01em;
  color: var(--mono-black);
}

/* 导航链接 */
.mono-nav-links {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.mono-nav-link {
  font-size: 0.875rem;
  font-weight: var(--mono-weight-medium);
  color: var(--mono-gray-600);
  text-decoration: none;
  transition: color 0.2s ease-out;
}

.mono-nav-link:hover {
  color: var(--mono-black);
}

.mono-nav-link.active {
  font-weight: var(--mono-weight-semibold);
  color: var(--mono-black);
}

/* 用户区域 */
.mono-nav-user {
  display: flex;
  align-items: center;
  gap: 1rem;
}

/* 通知图标 */
.mono-nav-notification {
  position: relative;
  padding: 0.5rem;
  border-radius: var(--mono-radius-lg);
  cursor: pointer;
  transition: background 0.2s ease-out;
}

.mono-nav-notification:hover {
  background: var(--mono-gray-100);
}

.mono-nav-notification-dot {
  position: absolute;
  top: 0.25rem;
  right: 0.25rem;
  width: 8px;
  height: 8px;
  background: var(--mono-black);
  border-radius: 50%;
}

/* 用户头像 */
.mono-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--mono-gray-400), var(--mono-gray-600));
  border: 2px solid var(--mono-white);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
```

#### 2.8 深色 Hero 区系统（Dark Hero Section）

Hero 区使用**黑到深灰的渐变**，前景为纯白文字。

```css
/* Hero 区 */
.mono-hero {
  background: linear-gradient(135deg, var(--mono-black), var(--mono-gray-800), var(--mono-black));
  color: var(--mono-white);
  padding: 4rem 1.5rem;
}

.mono-hero-container {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 4rem;
}

/* Hero 标题 */
.mono-hero-title {
  font-size: 3rem;
  font-weight: var(--mono-weight-black);
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: var(--mono-white);
  margin-bottom: 1rem;
}

/* Hero 描述 */
.mono-hero-description {
  font-size: 1.125rem;
  line-height: 1.6;
  color: var(--mono-gray-300);
  margin-bottom: 1.5rem;
  max-width: 600px;
}

/* Hero 按钮组 */
.mono-hero-actions {
  display: flex;
  gap: 1rem;
}

/* Hero 视觉元素 */
.mono-hero-visual {
  width: 256px;
  height: 256px;
  position: relative;
}

.mono-hero-visual-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(107, 114, 128, 0.1));
  border-radius: 1.5rem;
  transform: rotate(6deg);
}

.mono-hero-visual-fg {
  position: absolute;
  inset: 1rem;
  background: linear-gradient(135deg, var(--mono-gray-300), var(--mono-gray-500));
  border-radius: 1rem;
  transform: rotate(-3deg);
  display: flex;
  align-items: center;
  justify-content: center;
}
```

### 3. Tailwind CSS 配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        mono: {
          white: '#FFFFFF',
          black: '#000000',
          gray: {
            50: '#F9FAFB',
            100: '#F3F4F6',
            200: '#E5E7EB',
            300: '#D1D5DB',
            400: '#9CA3AF',
            500: '#6B7280',
            600: '#4B5563',
            700: '#374151',
            800: '#1F2937',
            900: '#111827',
          },
        },
      },
      fontFamily: {
        sans: ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
        mono: ['SF Mono', 'Monaco', 'Inconsolata', 'Fira Code', 'Courier New', 'monospace'],
      },
      fontWeight: {
        regular: '400',
        medium: '500',
        semibold: '600',
        bold: '700',
        extrabold: '800',
        black: '900',
      },
      spacing: {
        // 基于 4px 网格
        '1': '0.25rem',  // 4px
        '2': '0.5rem',   // 8px
        '3': '0.75rem',  // 12px
        '4': '1rem',     // 16px
        '5': '1.25rem',  // 20px
        '6': '1.5rem',   // 24px
        '8': '2rem',     // 32px
        '10': '2.5rem',  // 40px
        '12': '3rem',    // 48px
        '16': '4rem',    // 64px
        '20': '5rem',    // 80px
        '24': '6rem',    // 96px
      },
      borderRadius: {
        'sm': '0.25rem',  // 4px
        'md': '0.5rem',   // 8px
        'lg': '0.75rem',  // 12px
        'xl': '1rem',     // 16px
        '2xl': '1.5rem',  // 24px
        'full': '9999px',
      },
      boxShadow: {
        'mono-sm': '0 1px 3px rgba(0, 0, 0, 0.05), 0 1px 2px rgba(0, 0, 0, 0.06)',
        'mono-md': '0 4px 8px rgba(0, 0, 0, 0.06), 0 2px 4px rgba(0, 0, 0, 0.08)',
        'mono-lg': '0 10px 20px rgba(0, 0, 0, 0.08), 0 4px 8px rgba(0, 0, 0, 0.06)',
        'mono-xl': '0 20px 40px rgba(0, 0, 0, 0.1), 0 8px 16px rgba(0, 0, 0, 0.08)',
      },
    },
  },
  plugins: [],
};
```

### 4. 使用示例

```html
<!-- Monochrome 仪表板 -->
<div class="min-h-screen bg-mono-gray-50">
  <!-- 顶部导航 -->
  <nav class="mono-nav">
    <div class="mono-nav-container">
      <a href="#" class="mono-logo">
        <div class="mono-logo-icon">
          <div class="w-6 h-6 border-2 border-white rounded"></div>
        </div>
        <span class="mono-logo-text">MONOCHROME</span>
      </a>

      <div class="mono-nav-links">
        <a href="#" class="mono-nav-link active">Dashboard</a>
        <a href="#" class="mono-nav-link">Projects</a>
        <a href="#" class="mono-nav-link">Analytics</a>
        <a href="#" class="mono-nav-link">Settings</a>
      </div>

      <div class="mono-nav-user">
        <button class="mono-nav-notification">
          <svg class="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path>
          </svg>
          <span class="mono-nav-notification-dot"></span>
        </button>
        <div class="mono-avatar"></div>
      </div>
    </div>
  </nav>

  <!-- Hero 区 -->
  <section class="mono-hero">
    <div class="mono-hero-container">
      <div>
        <h1 class="mono-hero-title">Welcome Back</h1>
        <p class="mono-hero-description">
          Your workspace is ready. Track your projects, manage your team, and stay productive.
        </p>
        <div class="mono-hero-actions">
          <button class="mono-btn-primary">Create Project</button>
          <button class="mono-btn-ghost">View Reports</button>
        </div>
      </div>
      <div class="mono-hero-visual">
        <div class="mono-hero-visual-bg"></div>
        <div class="mono-hero-visual-fg">
          <!-- Chart Icon -->
        </div>
      </div>
    </div>
  </section>

  <!-- 统计卡片 -->
  <section class="py-12 -mt-8">
    <div class="mono-container">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="mono-stat-card">
          <div class="flex items-start justify-between mb-4">
            <div class="mono-card-icon">
              <!-- Icon SVG -->
            </div>
            <span class="mono-card-badge">+12%</span>
          </div>
          <div class="mono-text-numeric">24</div>
          <div class="mono-text-sm text-mono-gray-600">Active Projects</div>
        </div>

        <!-- 更多统计卡片... -->
      </div>
    </div>
  </section>
</div>
```


---

## English Version (en-US)

### 1. Design Philosophy & Core Principles

**Monochrome Design** is a minimalist style that exclusively uses **black, white, and gray**. The core philosophy is to **replace hue contrast with value contrast**, building information hierarchy through **rigorous typography, precise grid systems, and generous whitespace**, conveying rationality, professionalism, and calm confidence.

**Design Principles**:
- **Color Minimalism**: Strictly limited to grayscale, no saturated colors
- **Contrast as King**: Create visual hierarchy through value differences
- **Typography-Led**: Font weight, size, and spacing become the primary design language
- **Strict Grid**: All spacing aligns to 4px or 8px baseline grid
- **Generous Whitespace**: Let negative space itself become a design element

[English version continues with similar detailed content...]

**Implementation Best Practices**

**Layout & Composition**:
- Use CSS Grid for precise alignment and structured layouts (grid-template-columns: repeat(12, 1fr))
- Implement asymmetric balance: pair large elements with smaller complementary pieces
- Apply golden ratio (1.618) for proportional spacing and element sizing
- Create visual focal points using size contrast, color contrast, and positioning
- Maintain consistent margins and padding rhythm using 8px or 12px base unit
- Use max-width containers (max-w-6xl to max-w-7xl) for optimal reading line length

**Typography Excellence**:
- Establish clear type scale with sufficient size differentiation between levels (1.25-1.5 ratio)
- Apply proper line-height for optimal readability: 1.4-1.6 for headings, 1.6-1.8 for body
- Use appropriate font weights: avoid single-weight designs, vary from 300-700+
- Implement responsive typography with clamp() for fluid scaling across viewports
- Maintain optimal line length: 60-75 characters for body text, shorter for headings
- Pair fonts thoughtfully: maximum 2-3 font families, ensure visual harmony

**Color Theory Application**:
- Define primary, secondary, and accent colors with clear purpose and hierarchy
- Create tints and shades for each main color (5-7 variations: 100, 200, 300... 900)
- Ensure sufficient contrast ratios: 4.5:1 for text, 3:1 for UI components (WCAG AA)
- Apply 60-30-10 rule: 60% dominant color, 30% secondary, 10% accent
- Test color combinations for accessibility with colorblind simulation tools
- Use color psychology: warm colors for energy/action, cool colors for calm/trust

**Interactive States & Feedback**:
- Implement clear visual feedback for all interactive elements (hover, active, focus, disabled)
- Use multi-property transitions for smooth state changes: color, transform, shadow simultaneously
- Apply appropriate timing: quick for buttons (200-300ms), slower for complex reveals (400-600ms)
- Provide loading states for asynchronous actions with spinners or skeleton screens
- Use micro-interactions to delight users: subtle bounces, ripples, or morphs on interaction
- Ensure disabled states are visually distinct but maintain sufficient contrast

**Animation Principles**:
- Follow Disney's 12 principles of animation: ease-in, ease-out, anticipation, follow-through
- Use spring-based physics for natural, organic motion feel
- Implement easing curves that match content: bounce for playful, ease-out for professional
- Stagger animations when revealing multiple elements (50-150ms delays)
- Respect animation budgets: limit simultaneous animations to 5-8 elements
- Provide prefers-reduced-motion alternatives: instant transitions or simple fades

**Performance Optimization**:
- Use CSS transforms and opacity for animations (GPU accelerated properties)
- Implement lazy loading for images and components below the fold
- Apply code splitting to load features on demand, reducing initial bundle size
- Optimize images: compress, use appropriate formats (WebP, AVIF), responsive srcset
- Minimize DOM depth and complexity to improve rendering performance
- Use CSS containment for independent sections to isolate rendering work
- Implement virtual scrolling for long lists to render only visible items

**Cross-Browser Compatibility**:
- Test across Chrome, Firefox, Safari, Edge for consistent experience
- Provide fallbacks for modern CSS features (backdrop-filter, scroll-snap)
- Use autoprefixer or PostCSS to automatically add vendor prefixes
- Implement feature detection with @supports for progressive enhancement
- Ensure touch interactions work correctly on mobile browsers
- Test on actual devices, not just emulators, for real-world validation

**Accessibility Compliance**:
- Meet WCAG 2.1 Level AA standards minimum, aim for AAA where feasible
- Ensure keyboard navigation works for all functionality with visible focus states
- Provide sufficient color contrast for all text and interactive elements
- Add appropriate ARIA attributes: labels, roles, states, live regions
- Include skip links for keyboard users to bypass repetitive navigation
- Test with screen readers (NVDA, JAWS, VoiceOver) for actual user experience
- Provide text alternatives for all non-text content (images, icons, charts)
- Ensure forms have proper labels, error messages, and help text
- Respect user preferences: reduced motion, high contrast, color schemes
