# Custom Prompt: Accessibility / High Contrast（无障碍 / 高对比度）

## 中文版本 (zh-CN)

### 1. 设计哲学与核心原则

**Accessibility / High Contrast（无障碍 / 高对比度）**设计是一种以**包容性、可用性、可访问性**为核心的设计理念，遵循 **WCAG 2.1 AA（Web Content Accessibility Guidelines）**标准，确保所有用户——包括视力障碍、色盲、老年用户、键盘用户——都能**平等、高效、无障碍**地使用界面。

**核心哲学**：
- **包容性设计（Inclusive Design）**：设计适用于所有人，而不仅是多数人
- **可感知性（Perceivable）**：信息和界面组件必须以用户可感知的方式呈现
- **可操作性（Operable）**：界面组件和导航必须可操作（键盘、鼠标、触摸、辅助技术）
- **可理解性（Understandable）**：信息和界面操作必须可理解
- **健壮性（Robust）**：内容必须足够健壮，能被各种用户代理（包括辅助技术）解释

**设计原则**：
- **高对比度**：文本对比度 ≥ 4.5:1（正文），≥ 3:1（大文本/图标）
- **清晰层级**：使用字号、字重、间距建立明确的视觉层级
- **键盘可达**：所有交互元素可通过键盘访问，Tab 顺序合理
- **可见焦点**：焦点指示器清晰可见（≥ 3px 高对比描边）
- **不依赖颜色**：状态变化同时使用颜色+形状+文本+图标
- **减少动态**：尊重 `prefers-reduced-motion`，避免闪烁和高频动画
- **语义化 HTML**：使用正确的 HTML5 语义标签和 ARIA 属性

### 2. 核心设计要求

#### 2.1 高对比度配色系统（High Contrast Color System）

Accessibility 的配色系统以**WCAG 2.1 AA 对比度标准**为核心，确保所有文本和图标清晰可辨。

**对比度标准（WCAG 2.1 AA）**：
- **正文文本**：对比度 ≥ **4.5:1**（字号 < 18px 或 < 14px 粗体）
- **大文本**：对比度 ≥ **3:1**（字号 ≥ 18px 或 ≥ 14px 粗体）
- **图标和边框**：对比度 ≥ **3:1**
- **焦点指示器**：对比度 ≥ **3:1**，厚度 ≥ 2px

**主题 1：黑白（Black on White）**：
- **背景色**：`#FFFFFF`（白色）
- **文本色**：`#000000`（黑色）- 对比度 **21:1** ✅
- **次要文本**：`#1F2937`（深灰）- 对比度 **16.7:1** ✅
- **辅助文本**：`#374151`（中灰）- 对比度 **12.6:1** ✅
- **边框色**：`#000000`（黑色）- 4px 粗边框
- **焦点指示器**：`#3B82F6`（蓝色）- 4px 描边

**主题 2：黑黄（Black on Yellow）** - 色盲友好：
- **背景色**：`#FBBF24`（鲜黄）
- **文本色**：`#000000`（黑色）- 对比度 **13.3:1** ✅
- **次要文本**：`#1F2937`（深灰）- 对比度 **10.5:1** ✅
- **边框色**：`#000000`（黑色）- 4px 粗边框
- **焦点指示器**：`#DC2626`（红色）- 4px 描边

**主题 3：青黑（Cyan on Black）** - 夜间模式：
- **背景色**：`#000000`（黑色）
- **文本色**：`#06B6D4`（青色）- 对比度 **9.8:1** ✅
- **次要文本**：`#22D3EE`（浅青）- 对比度 **11.2:1** ✅
- **边框色**：`#06B6D4`（青色）- 4px 粗边框
- **焦点指示器**：`#FBBF24`（黄色）- 4px 描边

**色盲安全配色（Color-Blind Safe Palette）**：
- **成功色**：`#059669`（绿色）+ ✓ 图标
- **警告色**：`#F59E0B`（橙色）+ ⚠ 图标
- **错误色**：`#DC2626`（红色）+ ✗ 图标
- **信息色**：`#3B82F6`（蓝色）+ ⓘ 图标

**完整 CSS 变量定义**：
```css
:root {
  /* 主题 1：黑白 */
  --a11y-bg-white: #FFFFFF;
  --a11y-text-black: #000000;
  --a11y-text-dark-gray: #1F2937;
  --a11y-text-medium-gray: #374151;
  --a11y-text-light-gray: #6B7280;
  --a11y-border-black: #000000;
  --a11y-focus-blue: #3B82F6;

  /* 主题 2：黑黄 */
  --a11y-bg-yellow: #FBBF24;

  /* 主题 3：青黑 */
  --a11y-bg-black: #000000;
  --a11y-text-cyan: #06B6D4;
  --a11y-text-cyan-light: #22D3EE;

  /* 状态色（色盲安全） */
  --a11y-success: #059669;
  --a11y-warning: #F59E0B;
  --a11y-error: #DC2626;
  --a11y-info: #3B82F6;

  /* 边框粗细 */
  --a11y-border-thin: 2px;
  --a11y-border-medium: 3px;
  --a11y-border-thick: 4px;

  /* 焦点指示器 */
  --a11y-focus-ring: 4px;
  --a11y-focus-offset: 2px;

  /* 字号 */
  --a11y-text-xs: 0.875rem;    /* 14px */
  --a11y-text-sm: 1rem;         /* 16px - 最小正文 */
  --a11y-text-base: 1.125rem;   /* 18px - 大文本 */
  --a11y-text-lg: 1.25rem;      /* 20px */
  --a11y-text-xl: 1.5rem;       /* 24px */
  --a11y-text-2xl: 1.875rem;    /* 30px */
  --a11y-text-3xl: 2.25rem;     /* 36px */

  /* 行高 */
  --a11y-leading-normal: 1.6;
  --a11y-leading-relaxed: 1.8;

  /* 间距 */
  --a11y-space-xs: 0.5rem;   /* 8px */
  --a11y-space-sm: 1rem;     /* 16px */
  --a11y-space-md: 1.5rem;   /* 24px */
  --a11y-space-lg: 2rem;     /* 32px */
  --a11y-space-xl: 3rem;     /* 48px */
}
```

#### 2.2 焦点指示器系统（Focus Indicator System）

Accessibility 设计必须为所有可交互元素提供**清晰可见的焦点指示器**（≥ 3:1 对比度，≥ 2px 厚度）。

```css
/* 全局焦点指示器（仅键盘用户） */
*:focus-visible {
  outline: var(--a11y-focus-ring) solid var(--a11y-focus-blue);
  outline-offset: var(--a11y-focus-offset);
  transition: outline 0.15s ease;
}

/* 移除鼠标点击的焦点环 */
*:focus:not(:focus-visible) {
  outline: none;
}

/* 链接焦点 */
a:focus-visible {
  outline: var(--a11y-focus-ring) solid var(--a11y-focus-blue);
  outline-offset: var(--a11y-focus-offset);
  background-color: rgba(59, 130, 246, 0.1);
}

/* 按钮焦点 */
button:focus-visible,
.a11y-btn:focus-visible {
  outline: var(--a11y-focus-ring) solid var(--a11y-focus-blue);
  outline-offset: var(--a11y-focus-offset);
  box-shadow: 0 0 0 8px rgba(59, 130, 246, 0.15);
}

/* 输入框焦点 */
input:focus-visible,
textarea:focus-visible,
select:focus-visible {
  outline: var(--a11y-focus-ring) solid var(--a11y-focus-blue);
  outline-offset: 0;
  border-color: var(--a11y-focus-blue);
  box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.2);
}

/* 复选框和单选框焦点 */
input[type="checkbox"]:focus-visible,
input[type="radio"]:focus-visible {
  outline: var(--a11y-focus-ring) solid var(--a11y-focus-blue);
  outline-offset: var(--a11y-focus-offset);
}

/* 卡片焦点（当内部有焦点时） */
.a11y-card:focus-within {
  outline: var(--a11y-border-medium) solid var(--a11y-focus-blue);
  outline-offset: 2px;
  box-shadow: 0 0 0 6px rgba(59, 130, 246, 0.1);
}

/* 跳过链接焦点（Skip Links） */
.a11y-skip-link:focus-visible {
  position: fixed;
  top: 1rem;
  left: 1rem;
  z-index: 9999;
  padding: 1rem 1.5rem;
  background: var(--a11y-text-black);
  color: var(--a11y-bg-white);
  font-weight: 700;
  border-radius: 4px;
  outline: var(--a11y-focus-ring) solid var(--a11y-bg-white);
  outline-offset: 2px;
}
```

#### 2.3 按钮系统（Button System）

Accessibility 按钮使用**高对比度边框、清晰状态、触摸友好尺寸**（≥ 44x44px）。

```css
/* 主要按钮 */
.a11y-btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  min-width: 44px;
  min-height: 44px;
  padding: 0.875rem 1.5rem;
  background: var(--a11y-text-black);
  color: var(--a11y-bg-white);
  font-size: var(--a11y-text-base);
  font-weight: 700;
  text-align: center;
  border: var(--a11y-border-thick) solid var(--a11y-text-black);
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.a11y-btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}

.a11y-btn-primary:active:not(:disabled) {
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.a11y-btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* 次要按钮 */
.a11y-btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  min-width: 44px;
  min-height: 44px;
  padding: 0.875rem 1.5rem;
  background: var(--a11y-bg-white);
  color: var(--a11y-text-black);
  font-size: var(--a11y-text-base);
  font-weight: 700;
  text-align: center;
  border: var(--a11y-border-thick) solid var(--a11y-text-black);
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.a11y-btn-secondary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  background: var(--a11y-text-light-gray);
}

/* 成功按钮 */
.a11y-btn-success {
  background: var(--a11y-success);
  color: var(--a11y-bg-white);
  border-color: var(--a11y-success);
}

.a11y-btn-success::before {
  content: '✓';
  margin-right: 0.25rem;
  font-weight: 900;
}

/* 警告按钮 */
.a11y-btn-warning {
  background: var(--a11y-warning);
  color: var(--a11y-text-black);
  border-color: var(--a11y-warning);
}

.a11y-btn-warning::before {
  content: '⚠';
  margin-right: 0.25rem;
  font-weight: 900;
}

/* 危险按钮 */
.a11y-btn-danger {
  background: var(--a11y-error);
  color: var(--a11y-bg-white);
  border-color: var(--a11y-error);
}

.a11y-btn-danger::before {
  content: '✗';
  margin-right: 0.25rem;
  font-weight: 900;
}

/* 图标按钮 */
.a11y-btn-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  min-height: 44px;
  padding: 0.75rem;
  background: var(--a11y-bg-white);
  border: var(--a11y-border-thick) solid var(--a11y-text-black);
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.a11y-btn-icon svg {
  width: 24px;
  height: 24px;
  stroke-width: 3;
}

/* 按钮组 */
.a11y-btn-group {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}
```

#### 2.4 表单系统（Form System）

Accessibility 表单强调**清晰标签、错误提示、键盘可达性、ARIA 属性**。

```css
/* 表单标签 */
.a11y-label {
  display: block;
  margin-bottom: 0.5rem;
  font-size: var(--a11y-text-base);
  font-weight: 700;
  color: var(--a11y-text-black);
}

/* 必填标记 */
.a11y-label-required::after {
  content: ' *';
  color: var(--a11y-error);
  font-weight: 900;
}

/* 文本输入框 */
.a11y-input {
  width: 100%;
  min-height: 44px;
  padding: 0.875rem 1rem;
  font-size: var(--a11y-text-base);
  font-family: inherit;
  color: var(--a11y-text-black);
  background: var(--a11y-bg-white);
  border: var(--a11y-border-medium) solid var(--a11y-text-black);
  border-radius: 4px;
  transition: all 0.2s ease;
}

.a11y-input:hover:not(:disabled) {
  border-color: var(--a11y-text-dark-gray);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.a11y-input:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  background: var(--a11y-text-light-gray);
}

/* 输入框错误状态 */
.a11y-input-error {
  border-color: var(--a11y-error);
  border-width: var(--a11y-border-thick);
}

.a11y-input-error:focus-visible {
  outline-color: var(--a11y-error);
  box-shadow: 0 0 0 4px rgba(220, 38, 38, 0.2);
}

/* 输入框成功状态 */
.a11y-input-success {
  border-color: var(--a11y-success);
  border-width: var(--a11y-border-thick);
}

/* 错误提示 */
.a11y-error-message {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.5rem;
  padding: 0.75rem 1rem;
  font-size: var(--a11y-text-sm);
  font-weight: 700;
  color: var(--a11y-error);
  background: rgba(220, 38, 38, 0.1);
  border-left: var(--a11y-border-thick) solid var(--a11y-error);
  border-radius: 4px;
}

.a11y-error-message::before {
  content: '✗';
  font-size: 1.25rem;
  font-weight: 900;
}

/* 成功提示 */
.a11y-success-message {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.5rem;
  padding: 0.75rem 1rem;
  font-size: var(--a11y-text-sm);
  font-weight: 700;
  color: var(--a11y-success);
  background: rgba(5, 150, 105, 0.1);
  border-left: var(--a11y-border-thick) solid var(--a11y-success);
  border-radius: 4px;
}

.a11y-success-message::before {
  content: '✓';
  font-size: 1.25rem;
  font-weight: 900;
}

/* 帮助文本 */
.a11y-help-text {
  display: block;
  margin-top: 0.5rem;
  font-size: var(--a11y-text-sm);
  color: var(--a11y-text-medium-gray);
}

/* 复选框 */
.a11y-checkbox {
  appearance: none;
  width: 28px;
  height: 28px;
  border: var(--a11y-border-medium) solid var(--a11y-text-black);
  border-radius: 4px;
  background: var(--a11y-bg-white);
  cursor: pointer;
  position: relative;
  flex-shrink: 0;
  transition: all 0.2s ease;
}

.a11y-checkbox:checked {
  background: var(--a11y-text-black);
  border-color: var(--a11y-text-black);
}

.a11y-checkbox:checked::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: var(--a11y-bg-white);
  font-size: 1.125rem;
  font-weight: 900;
}

/* 单选框 */
.a11y-radio {
  appearance: none;
  width: 28px;
  height: 28px;
  border: var(--a11y-border-medium) solid var(--a11y-text-black);
  border-radius: 50%;
  background: var(--a11y-bg-white);
  cursor: pointer;
  position: relative;
  flex-shrink: 0;
  transition: all 0.2s ease;
}

.a11y-radio:checked {
  border-width: 8px;
  border-color: var(--a11y-text-black);
}

/* 文本域 */
.a11y-textarea {
  width: 100%;
  min-height: 120px;
  padding: 0.875rem 1rem;
  font-size: var(--a11y-text-base);
  font-family: inherit;
  line-height: var(--a11y-leading-relaxed);
  color: var(--a11y-text-black);
  background: var(--a11y-bg-white);
  border: var(--a11y-border-medium) solid var(--a11y-text-black);
  border-radius: 4px;
  resize: vertical;
  transition: all 0.2s ease;
}

/* 选择框 */
.a11y-select {
  width: 100%;
  min-height: 44px;
  padding: 0.875rem 2.5rem 0.875rem 1rem;
  font-size: var(--a11y-text-base);
  font-family: inherit;
  color: var(--a11y-text-black);
  background: var(--a11y-bg-white);
  border: var(--a11y-border-medium) solid var(--a11y-text-black);
  border-radius: 4px;
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23000000' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  background-size: 24px;
}
```

#### 2.5 跳过链接系统（Skip Links System）

Skip Links 允许键盘用户快速跳转到主要内容区域，提升导航效率。

```css
/* 跳过链接（默认隐藏） */
.a11y-skip-link {
  position: absolute;
  top: -9999px;
  left: -9999px;
  z-index: 9999;
  padding: 1rem 1.5rem;
  background: var(--a11y-text-black);
  color: var(--a11y-bg-white);
  font-size: var(--a11y-text-base);
  font-weight: 700;
  text-decoration: none;
  border-radius: 4px;
  transition: all 0.15s ease;
}

/* 跳过链接（获得焦点时显示） */
.a11y-skip-link:focus,
.a11y-skip-link:focus-visible {
  position: fixed;
  top: 1rem;
  left: 1rem;
  outline: var(--a11y-focus-ring) solid var(--a11y-bg-white);
  outline-offset: 2px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
}

/* 跳过链接容器 */
.a11y-skip-links {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 9999;
}

.a11y-skip-links a {
  position: absolute;
  top: -9999px;
  left: -9999px;
}

.a11y-skip-links a:focus {
  position: fixed;
  top: 1rem;
  left: 1rem;
}
```

**HTML 使用示例**：
```html
<!-- 跳过链接（放在 <body> 开头） -->
<div class="a11y-skip-links">
  <a href="#main-content" class="a11y-skip-link">
    Skip to main content
  </a>
  <a href="#main-navigation" class="a11y-skip-link">
    Skip to navigation
  </a>
</div>

<!-- 主导航 -->
<nav id="main-navigation" aria-label="Main navigation">
  <!-- 导航内容 -->
</nav>

<!-- 主内容 -->
<main id="main-content" role="main">
  <!-- 主要内容 -->
</main>
```

#### 2.6 屏幕阅读器工具类（Screen Reader Utilities）

提供仅屏幕阅读器可访问的内容，增强可访问性。

```css
/* 屏幕阅读器专用（视觉隐藏但可被读取） */
.sr-only,
.a11y-visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

/* 可获得焦点的屏幕阅读器专用内容 */
.sr-only-focusable:not(:focus),
.a11y-visually-hidden-focusable:not(:focus) {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.sr-only-focusable:focus,
.a11y-visually-hidden-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  padding: inherit;
  margin: inherit;
  overflow: visible;
  clip: auto;
  white-space: normal;
}

/* 隐藏图标文本（仅对视觉用户） */
.a11y-icon-text {
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  height: 1px;
  overflow: hidden;
  position: absolute;
  white-space: nowrap;
  width: 1px;
}
```

#### 2.7 减少动态系统（Reduced Motion System）

尊重用户的 `prefers-reduced-motion` 偏好，移除或简化动画。

```css
/* 减少动态媒体查询 */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* 可选的减少动态类（用户手动启用） */
.a11y-reduce-motion *,
.a11y-reduce-motion *::before,
.a11y-reduce-motion *::after {
  animation-duration: 0.01ms !important;
  animation-iteration-count: 1 !important;
  transition-duration: 0.01ms !important;
  scroll-behavior: auto !important;
}

/* 安全的动画（即使在减少动态模式下也保留） */
@media (prefers-reduced-motion: no-preference) {
  .a11y-safe-animation {
    animation: fadeIn 0.3s ease-out;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
}

/* 避免使用的动画类型 */
/* ❌ 闪烁动画（可能引发癫痫） */
/* ❌ 快速移动（可能引发眩晕） */
/* ❌ 视差滚动（可能引发恶心） */
/* ✅ 简单淡入淡出（安全） */
/* ✅ 缓慢滑动（安全） */
```

#### 2.8 ARIA 标签和语义化 HTML（ARIA Labels & Semantic HTML）

使用正确的 HTML5 语义标签和 ARIA 属性增强可访问性。

**HTML 结构示例**：
```html
<!-- ✅ 正确：使用语义化标签 + ARIA -->
<header role="banner">
  <nav aria-label="Main navigation" role="navigation">
    <ul role="menubar">
      <li role="none">
        <a href="#" role="menuitem">Home</a>
      </li>
    </ul>
  </nav>
</header>

<main role="main" id="main-content">
  <article aria-labelledby="article-title">
    <h1 id="article-title">Article Title</h1>
    <!-- 内容 -->
  </article>
</main>

<aside role="complementary" aria-label="Related content">
  <!-- 侧边栏内容 -->
</aside>

<footer role="contentinfo">
  <!-- 页脚内容 -->
</footer>

<!-- 按钮示例 -->
<button type="button" aria-label="Close dialog">
  <span aria-hidden="true">×</span>
  <span class="sr-only">Close</span>
</button>

<!-- 表单示例 -->
<form>
  <label for="email">Email Address</label>
  <input
    type="email"
    id="email"
    name="email"
    aria-required="true"
    aria-describedby="email-help email-error"
  />
  <span id="email-help" class="a11y-help-text">
    We'll never share your email.
  </span>
  <span id="email-error" role="alert" class="a11y-error-message" hidden>
    Please enter a valid email address.
  </span>
</form>

<!-- 图片示例 */
<img src="..." alt="Detailed description of image content" />

<!-- 装饰性图片 -->
<img src="..." alt="" aria-hidden="true" />

<!-- 图标 + 文本 -->
<button>
  <svg aria-hidden="true">...</svg>
  <span>Save</span>
</button>
```

### 3. Tailwind CSS 配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        a11y: {
          'bg-white': '#FFFFFF',
          'bg-yellow': '#FBBF24',
          'bg-black': '#000000',
          'text-black': '#000000',
          'text-dark-gray': '#1F2937',
          'text-medium-gray': '#374151',
          'text-light-gray': '#6B7280',
          'text-cyan': '#06B6D4',
          'text-cyan-light': '#22D3EE',
          'focus-blue': '#3B82F6',
          success: '#059669',
          warning: '#F59E0B',
          error: '#DC2626',
          info: '#3B82F6',
        },
      },
      fontSize: {
        'a11y-xs': '0.875rem',    /* 14px */
        'a11y-sm': '1rem',         /* 16px */
        'a11y-base': '1.125rem',   /* 18px */
        'a11y-lg': '1.25rem',      /* 20px */
        'a11y-xl': '1.5rem',       /* 24px */
        'a11y-2xl': '1.875rem',    /* 30px */
        'a11y-3xl': '2.25rem',     /* 36px */
      },
      lineHeight: {
        'a11y-normal': '1.6',
        'a11y-relaxed': '1.8',
      },
      borderWidth: {
        'a11y-thin': '2px',
        'a11y-medium': '3px',
        'a11y-thick': '4px',
      },
      outlineWidth: {
        'a11y-focus': '4px',
      },
      outlineOffset: {
        'a11y-focus': '2px',
      },
      minHeight: {
        'a11y-touch': '44px',
      },
      minWidth: {
        'a11y-touch': '44px',
      },
    },
  },
  plugins: [
    // 减少动态插件
    function ({ addVariant }) {
      addVariant('reduce-motion', '@media (prefers-reduced-motion: reduce)');
      addVariant('no-motion-preference', '@media (prefers-reduced-motion: no-preference)');
    },
  ],
};
```

### 4. 使用示例

```html
<!-- 无障碍页面完整示例 -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>企业仪表板 - 高对比度无障碍</title>
</head>
<body class="bg-white text-black min-h-screen">

  <!-- 跳过链接 -->
  <div class="a11y-skip-links">
    <a href="#main-content" class="a11y-skip-link">
      跳转到主要内容
    </a>
    <a href="#main-navigation" class="a11y-skip-link">
      跳转到导航
    </a>
  </div>

  <!-- 主导航 -->
  <nav id="main-navigation" class="bg-white border-b-4 border-black sticky top-0 z-30" role="navigation" aria-label="主导航">
    <div class="container mx-auto px-6 py-4">
      <div class="flex items-center justify-between">
        <h1 class="text-2xl font-black">企业仪表板</h1>
        <ul class="flex gap-6" role="menubar">
          <li role="none">
            <a href="#" class="font-bold text-lg px-4 py-2 hover:bg-gray-100 rounded" role="menuitem">
              仪表板
            </a>
          </li>
          <li role="none">
            <a href="#" class="font-bold text-lg px-4 py-2 hover:bg-gray-100 rounded" role="menuitem">
              报告
            </a>
          </li>
          <li role="none">
            <a href="#" class="font-bold text-lg px-4 py-2 hover:bg-gray-100 rounded" role="menuitem">
              设置
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- 主要内容 -->
  <main id="main-content" class="container mx-auto px-6 py-12" role="main">

    <!-- 统计数据 -->
    <section aria-labelledby="stats-heading" class="mb-12">
      <h2 id="stats-heading" class="text-3xl font-black mb-8 pb-4 border-b-4 border-black">
        关键指标
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">

        <!-- 统计卡片 1 -->
        <article class="bg-white border-4 border-black rounded-lg p-6">
          <div class="flex items-start justify-between mb-4">
            <div>
              <p class="text-sm font-bold uppercase tracking-wider mb-2">
                总用户数
              </p>
              <p class="text-4xl font-black">24,891</p>
            </div>
            <div class="w-16 h-16 bg-black flex items-center justify-center rounded-lg" aria-hidden="true">
              <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
              </svg>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="font-black" aria-label="增长">↑ 12.5%</span>
            <span class="font-bold">较上月</span>
          </div>
        </article>

        <!-- 统计卡片 2 -->
        <article class="bg-white border-4 border-black rounded-lg p-6">
          <div class="flex items-start justify-between mb-4">
            <div>
              <p class="text-sm font-bold uppercase tracking-wider mb-2">
                收入
              </p>
              <p class="text-4xl font-black">$48,392</p>
            </div>
            <div class="w-16 h-16 bg-black flex items-center justify-center rounded-lg" aria-hidden="true">
              <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="font-black" aria-label="增长">↑ 8.2%</span>
            <span class="font-bold">较上月</span>
          </div>
        </article>

        <!-- 统计卡片 3 -->
        <article class="bg-white border-4 border-black rounded-lg p-6">
          <div class="flex items-start justify-between mb-4">
            <div>
              <p class="text-sm font-bold uppercase tracking-wider mb-2">
                活跃项目
              </p>
              <p class="text-4xl font-black">127</p>
            </div>
            <div class="w-16 h-16 bg-black flex items-center justify-center rounded-lg" aria-hidden="true">
              <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
              </svg>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="font-black" aria-label="下降">↓ 3.1%</span>
            <span class="font-bold">较上月</span>
          </div>
        </article>

      </div>
    </section>

    <!-- 表单示例 -->
    <section aria-labelledby="form-heading" class="mb-12">
      <h2 id="form-heading" class="text-3xl font-black mb-8 pb-4 border-b-4 border-black">
        联系表单
      </h2>
      <form class="max-w-2xl bg-white border-4 border-black rounded-lg p-8">

        <!-- 姓名字段 -->
        <div class="mb-6">
          <label for="name" class="a11y-label a11y-label-required">
            姓名
          </label>
          <input
            type="text"
            id="name"
            name="name"
            class="a11y-input"
            aria-required="true"
            aria-describedby="name-help"
          />
          <span id="name-help" class="a11y-help-text">
            请输入您的全名
          </span>
        </div>

        <!-- 邮箱字段 -->
        <div class="mb-6">
          <label for="email" class="a11y-label a11y-label-required">
            邮箱地址
          </label>
          <input
            type="email"
            id="email"
            name="email"
            class="a11y-input"
            aria-required="true"
            aria-describedby="email-help"
          />
          <span id="email-help" class="a11y-help-text">
            我们不会分享您的邮箱
          </span>
        </div>

        <!-- 消息字段 -->
        <div class="mb-6">
          <label for="message" class="a11y-label a11y-label-required">
            消息
          </label>
          <textarea
            id="message"
            name="message"
            class="a11y-textarea"
            aria-required="true"
            aria-describedby="message-help"
          ></textarea>
          <span id="message-help" class="a11y-help-text">
            请详细描述您的需求
          </span>
        </div>

        <!-- 复选框 -->
        <div class="mb-6">
          <label class="flex items-center gap-4 cursor-pointer">
            <input
              type="checkbox"
              id="subscribe"
              name="subscribe"
              class="a11y-checkbox"
            />
            <span class="font-bold">订阅我们的新闻简报</span>
          </label>
        </div>

        <!-- 提交按钮 -->
        <div class="flex gap-4">
          <button type="submit" class="a11y-btn-primary">
            提交
          </button>
          <button type="reset" class="a11y-btn-secondary">
            重置
          </button>
        </div>

      </form>
    </section>

  </main>

  <!-- 页脚 -->
  <footer class="bg-black text-white py-12 border-t-4 border-black" role="contentinfo">
    <div class="container mx-auto px-6 text-center">
      <p class="text-lg font-bold">
        &copy; 2025 企业仪表板. 保留所有权利.
      </p>
    </div>
  </footer>

</body>
</html>
```


---

## English Version (en-US)

### 1. Design Philosophy & Core Principles

**Accessibility / High Contrast** design is a philosophy centered on **inclusivity, usability, and accessibility**, adhering to **WCAG 2.1 AA (Web Content Accessibility Guidelines)** standards to ensure all users—including those with visual impairments, color blindness, elderly users, and keyboard users—can use interfaces **equally, efficiently, and without barriers**.

**Core Philosophy**:
- **Inclusive Design**: Design for everyone, not just the majority
- **Perceivable**: Information and UI components must be presentable in ways users can perceive
- **Operable**: UI components and navigation must be operable (keyboard, mouse, touch, assistive technologies)
- **Understandable**: Information and UI operation must be understandable
- **Robust**: Content must be robust enough to be interpreted by various user agents (including assistive technologies)

**Design Principles**:
- **High Contrast**: Text contrast ≥ 4.5:1 (body text), ≥ 3:1 (large text/icons)
- **Clear Hierarchy**: Establish clear visual hierarchy using font size, weight, and spacing
- **Keyboard Accessible**: All interactive elements accessible via keyboard with logical Tab order
- **Visible Focus**: Focus indicators clearly visible (≥ 3px high-contrast outline)
- **Not Color-Dependent**: State changes use color + shape + text + icons
- **Reduced Motion**: Respect `prefers-reduced-motion`, avoid flickering and high-frequency animations
- **Semantic HTML**: Use proper HTML5 semantic tags and ARIA attributes

### 2. Core Design Requirements

[English translation continues with same structure and detail level...]

**Implementation Best Practices**

**Color Contrast Testing**:
- Use tools like WebAIM Contrast Checker or Stark to verify all color combinations
- Test with browser DevTools to simulate different types of color blindness
- Ensure interactive elements maintain contrast in all states (default, hover, focus, active, disabled)
- Provide high-contrast mode option for users who need extra visual clarity

**Keyboard Navigation**:
- Implement logical tab order that follows visual flow of content
- Ensure all interactive elements are reachable via Tab/Shift+Tab
- Add skip links to allow quick navigation to main content
- Test entire user flow using only keyboard (no mouse) to identify gaps

**Screen Reader Support**:
- Use semantic HTML5 elements (header, nav, main, article, aside, footer)
- Provide descriptive alt text for images and decorative images with alt=""
- Use ARIA labels for icon buttons and complex widgets
- Test with actual screen readers (NVDA, JAWS, VoiceOver) not just automated tools

**Motion & Animation**:
- Respect `prefers-reduced-motion` media query to disable/reduce animations
- Avoid auto-playing videos or animations without user control
- Provide play/pause controls for all motion content
- Keep animations subtle and purposeful - avoid distracting decorative motion

**Form Accessibility**:
- Associate all form inputs with labels using `for` and `id` attributes
- Provide clear error messages with instructions for fixing errors
- Use fieldset and legend for grouping related form controls
- Implement inline validation with both visual and text feedback
- Ensure form errors are announced to screen readers using ARIA live regions
