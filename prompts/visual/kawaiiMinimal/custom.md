# Custom Prompt: Kawaii Minimal（可爱极简）

## 中文版本 (zh-CN)

### 1. 设计哲学与核心原则

Kawaii Minimal（可爱极简）是一种将**日式可爱文化（Kawaii）**与**极简主义设计**相结合的视觉风格。这种风格的核心在于：在保持界面简洁、信息层级清晰的前提下，通过**糖果色渐变、超大圆角、表情化图标和轻盈动效**来营造温暖、治愈、充满亲和力的用户体验。

**设计原则**：
- **简洁为基**：界面布局保持极简结构，模块数量适中，避免视觉过载
- **色彩点缀**：使用糖果色仅作为点缀，大面积保持柔和浅色背景
- **圆润柔软**：所有元素采用超大圆角（20-30px），按钮为胶囊形（9999px）
- **情感化设计**：通过表情图标、可爱插图和俏皮文案传递温暖情绪
- **轻盈互动**：动效偏向弹跳、浮动感，避免生硬的线性过渡

### 2. 核心设计要求

#### 2.1 糖果色配色系统（Candy Color Palette）

Kawaii Minimal 的配色系统以**高明度、中饱和度**的糖果色为主，营造甜美但不刺眼的视觉效果。

**主色调（Primary Colors）**：
- **蜜桃粉（Peach Pink）**：`#FFB6D9` - 主要按钮、强调色
- **薰衣草紫（Lavender Purple）**：`#E6D5FF` - 次要按钮、标签
- **薄荷绿（Mint Green）**：`#D4F1D4` - 成功状态、积极反馈
- **奶油黄（Cream Yellow）**：`#FFF9E6` - 提示信息、高亮

**浅色调（Light Tones）**：
- **樱花粉浅（Light Pink）**：`#FFDBE9`
- **薰衣草浅（Light Lavender）**：`#F5EDFF`
- **薄荷绿浅（Light Mint）**：`#E8F8E8`
- **奶油白（Creamy White）**：`#FFF9F5`

**中性色（Neutral Colors）**：
- **深灰文本（Text Dark）**：`#333333` - 标题文本
- **中灰文本（Text Medium）**：`#666666` - 正文文本
- **浅灰背景（Background Light）**：`#F8F9FA` - 卡片背景
- **纯白（Pure White）**：`#FFFFFF` - 主背景

**渐变配色（Gradient Schemes）**：
```css
/* 粉紫渐变（主要按钮） */
background: linear-gradient(135deg, #FFB6D9 0%, #E6D5FF 100%);

/* 粉绿渐变（标题文字） */
background: linear-gradient(135deg, #FFB6D9 0%, #D4F1D4 100%);

/* 三色彩虹渐变（导航栏） */
background: linear-gradient(135deg, #FFB6D9 0%, #E6D5FF 50%, #D4F1D4 100%);

/* 柔和背景渐变 */
background: linear-gradient(180deg, #FFFFFF 0%, #FFF9F5 100%);
```

**完整 CSS 变量定义**：
```css
:root {
  /* 主色调 */
  --kawaii-pink: #FFB6D9;
  --kawaii-pink-light: #FFDBE9;
  --kawaii-purple: #E6D5FF;
  --kawaii-purple-light: #F5EDFF;
  --kawaii-green: #D4F1D4;
  --kawaii-green-light: #E8F8E8;
  --kawaii-yellow: #FFF9E6;

  /* 中性色 */
  --kawaii-text-dark: #333333;
  --kawaii-text-medium: #666666;
  --kawaii-text-light: #999999;
  --kawaii-bg-white: #FFFFFF;
  --kawaii-bg-cream: #FFF9F5;
  --kawaii-bg-gray: #F8F9FA;

  /* 渐变 */
  --kawaii-gradient-primary: linear-gradient(135deg, #FFB6D9, #E6D5FF);
  --kawaii-gradient-secondary: linear-gradient(135deg, #FFB6D9, #D4F1D4);
  --kawaii-gradient-rainbow: linear-gradient(135deg, #FFB6D9 0%, #E6D5FF 50%, #D4F1D4 100%);

  /* 阴影 */
  --kawaii-shadow-sm: 0 4px 12px rgba(255, 182, 217, 0.15);
  --kawaii-shadow-md: 0 8px 20px rgba(255, 182, 217, 0.25);
  --kawaii-shadow-lg: 0 12px 32px rgba(255, 182, 217, 0.35);

  /* 圆角 */
  --kawaii-radius-sm: 16px;
  --kawaii-radius-md: 24px;
  --kawaii-radius-lg: 32px;
  --kawaii-radius-full: 9999px;
}
```

#### 2.2 超大圆角系统（Hyper Rounded Corners）

Kawaii Minimal 的标志性特征之一是**极端的圆角设计**，所有矩形元素都拥有超大圆角，营造柔软、亲和的视觉感受。

**圆角等级**：
- **小圆角（Small）**：`16px` - 标签、徽章
- **中圆角（Medium）**：`24px` - 输入框、卡片
- **大圆角（Large）**：`30-32px` - 主要卡片、模态框
- **胶囊形（Pill）**：`9999px / 50%` - 所有按钮

**CSS 实现**：
```css
/* 卡片圆角 */
.kawaii-card {
  background: var(--kawaii-bg-white);
  border-radius: var(--kawaii-radius-lg); /* 32px */
  padding: 2rem;
  box-shadow: var(--kawaii-shadow-md);
  border: 2px solid transparent;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* 渐变边框卡片 */
.kawaii-card-gradient-border {
  position: relative;
  background: var(--kawaii-bg-white);
  border-radius: var(--kawaii-radius-lg);
  padding: 2rem;
}

.kawaii-card-gradient-border::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--kawaii-radius-lg);
  padding: 2px;
  background: var(--kawaii-gradient-rainbow);
  -webkit-mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
}

/* 输入框圆角 */
.kawaii-input {
  background: var(--kawaii-bg-cream);
  border: 2px solid var(--kawaii-pink-light);
  border-radius: var(--kawaii-radius-md); /* 24px */
  padding: 0.875rem 1.5rem;
  font-size: 1rem;
  color: var(--kawaii-text-dark);
  transition: all 0.3s ease;
}

.kawaii-input:focus {
  outline: none;
  border-color: var(--kawaii-pink);
  box-shadow: 0 0 0 4px rgba(255, 182, 217, 0.2);
  transform: translateY(-2px);
}

/* 标签圆角 */
.kawaii-tag {
  display: inline-flex;
  align-items: center;
  padding: 0.5rem 1rem;
  background: var(--kawaii-purple-light);
  color: var(--kawaii-text-dark);
  border-radius: var(--kawaii-radius-sm); /* 16px */
  font-size: 0.875rem;
  font-weight: 600;
}
```

#### 2.3 胶囊按钮系统（Pill Button System）

所有按钮必须采用**完全圆形的胶囊设计**（`border-radius: 9999px`），并配合**糖果色渐变背景**和**弹跳动效**。

**按钮变体**：

```css
/* 基础按钮样式 */
.kawaii-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.875rem 2rem;
  border: none;
  border-radius: var(--kawaii-radius-full); /* 9999px */
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  position: relative;
  overflow: hidden;
}

/* 主要按钮（粉紫渐变） */
.kawaii-btn-primary {
  background: var(--kawaii-gradient-primary);
  color: var(--kawaii-text-dark);
  box-shadow: var(--kawaii-shadow-sm);
}

.kawaii-btn-primary:hover {
  transform: translateY(-4px);
  box-shadow: var(--kawaii-shadow-md);
  animation: kawaiiBounce 0.6s ease-in-out;
}

.kawaii-btn-primary:active {
  transform: translateY(-2px);
  box-shadow: var(--kawaii-shadow-sm);
}

/* 次要按钮（白底粉边） */
.kawaii-btn-secondary {
  background: var(--kawaii-bg-white);
  color: var(--kawaii-text-dark);
  border: 2px solid var(--kawaii-pink);
  box-shadow: 0 4px 12px rgba(255, 182, 217, 0.15);
}

.kawaii-btn-secondary:hover {
  background: var(--kawaii-pink-light);
  transform: translateY(-4px);
  box-shadow: var(--kawaii-shadow-md);
}

/* 轮廓按钮（渐变边框） */
.kawaii-btn-outline {
  background: transparent;
  color: var(--kawaii-text-dark);
  position: relative;
  border: 2px solid transparent;
  background-clip: padding-box;
}

.kawaii-btn-outline::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--kawaii-radius-full);
  padding: 2px;
  background: var(--kawaii-gradient-primary);
  -webkit-mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
}

/* 大尺寸按钮 */
.kawaii-btn-large {
  padding: 1.125rem 2.5rem;
  font-size: 1.125rem;
}

/* 小尺寸按钮 */
.kawaii-btn-small {
  padding: 0.625rem 1.5rem;
  font-size: 0.875rem;
}

/* 图标按钮 */
.kawaii-btn-icon {
  width: 48px;
  height: 48px;
  padding: 0;
  border-radius: 50%;
  background: var(--kawaii-gradient-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--kawaii-shadow-sm);
}

.kawaii-btn-icon:hover {
  transform: scale(1.1) rotate(5deg);
  box-shadow: var(--kawaii-shadow-md);
}
```

**弹跳动画**：
```css
@keyframes kawaiiBounce {
  0%, 100% {
    transform: translateY(-4px);
  }
  50% {
    transform: translateY(-12px);
  }
}

/* 持续弹跳（用于图标） */
@keyframes kawaiiBounceLoop {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-8px);
  }
}

.kawaii-bounce-icon {
  animation: kawaiiBounceLoop 2s ease-in-out infinite;
}
```

#### 2.4 柔和阴影系统（Soft Shadow System）

Kawaii Minimal 的阴影必须非常**轻盈、柔和**，使用**粉色调阴影**而非传统的黑灰色阴影，营造温暖的悬浮感。

```css
/* 基础阴影等级 */
.kawaii-shadow-xs {
  box-shadow: 0 2px 8px rgba(255, 182, 217, 0.1);
}

.kawaii-shadow-sm {
  box-shadow: 0 4px 12px rgba(255, 182, 217, 0.15);
}

.kawaii-shadow-md {
  box-shadow: 0 8px 20px rgba(255, 182, 217, 0.25);
}

.kawaii-shadow-lg {
  box-shadow: 0 12px 32px rgba(255, 182, 217, 0.35);
}

.kawaii-shadow-xl {
  box-shadow: 0 20px 48px rgba(255, 182, 217, 0.4);
}

/* 多层阴影（增强深度） */
.kawaii-shadow-layered {
  box-shadow:
    0 4px 12px rgba(255, 182, 217, 0.2),
    0 8px 24px rgba(230, 213, 255, 0.15),
    0 16px 48px rgba(212, 241, 212, 0.1);
}

/* 内阴影（凹陷效果） */
.kawaii-shadow-inset {
  box-shadow:
    inset 0 2px 8px rgba(255, 182, 217, 0.15),
    inset 0 4px 12px rgba(230, 213, 255, 0.1);
}

/* 发光阴影（强调状态） */
.kawaii-shadow-glow {
  box-shadow:
    0 0 20px rgba(255, 182, 217, 0.4),
    0 0 40px rgba(230, 213, 255, 0.2);
}
```

#### 2.5 表单元素设计（Form Elements）

表单元素保持**简洁、柔和、易用**的原则，使用大圆角和轻盈的交互反馈。

```css
/* 文本输入框 */
.kawaii-input-text {
  width: 100%;
  background: var(--kawaii-bg-cream);
  border: 2px solid var(--kawaii-pink-light);
  border-radius: var(--kawaii-radius-md);
  padding: 0.875rem 1.5rem;
  font-size: 1rem;
  color: var(--kawaii-text-dark);
  transition: all 0.3s ease;
}

.kawaii-input-text::placeholder {
  color: var(--kawaii-text-light);
}

.kawaii-input-text:focus {
  outline: none;
  border-color: var(--kawaii-pink);
  background: var(--kawaii-bg-white);
  box-shadow: 0 0 0 4px rgba(255, 182, 217, 0.2);
  transform: translateY(-2px);
}

/* 文本域 */
.kawaii-textarea {
  width: 100%;
  min-height: 120px;
  background: var(--kawaii-bg-cream);
  border: 2px solid var(--kawaii-pink-light);
  border-radius: var(--kawaii-radius-md);
  padding: 1rem 1.5rem;
  font-size: 1rem;
  color: var(--kawaii-text-dark);
  resize: vertical;
  transition: all 0.3s ease;
}

/* 复选框（自定义样式） */
.kawaii-checkbox {
  appearance: none;
  width: 24px;
  height: 24px;
  border: 2px solid var(--kawaii-pink);
  border-radius: 8px;
  background: var(--kawaii-bg-white);
  cursor: pointer;
  position: relative;
  transition: all 0.3s ease;
}

.kawaii-checkbox:checked {
  background: var(--kawaii-gradient-primary);
  border-color: var(--kawaii-pink);
}

.kawaii-checkbox:checked::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 14px;
  font-weight: bold;
}

.kawaii-checkbox:hover {
  transform: scale(1.1);
  box-shadow: 0 0 12px rgba(255, 182, 217, 0.3);
}

/* 单选框 */
.kawaii-radio {
  appearance: none;
  width: 24px;
  height: 24px;
  border: 2px solid var(--kawaii-pink);
  border-radius: 50%;
  background: var(--kawaii-bg-white);
  cursor: pointer;
  position: relative;
  transition: all 0.3s ease;
}

.kawaii-radio:checked {
  border-color: var(--kawaii-pink);
}

.kawaii-radio:checked::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--kawaii-gradient-primary);
}

/* 开关按钮 */
.kawaii-switch {
  position: relative;
  width: 60px;
  height: 32px;
  background: var(--kawaii-bg-gray);
  border-radius: var(--kawaii-radius-full);
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid var(--kawaii-pink-light);
}

.kawaii-switch::after {
  content: '';
  position: absolute;
  top: 3px;
  left: 3px;
  width: 22px;
  height: 22px;
  background: white;
  border-radius: 50%;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.kawaii-switch.active {
  background: var(--kawaii-gradient-primary);
  border-color: var(--kawaii-pink);
}

.kawaii-switch.active::after {
  left: calc(100% - 25px);
}

/* 下拉选择框 */
.kawaii-select {
  width: 100%;
  background: var(--kawaii-bg-cream);
  border: 2px solid var(--kawaii-pink-light);
  border-radius: var(--kawaii-radius-md);
  padding: 0.875rem 1.5rem;
  font-size: 1rem;
  color: var(--kawaii-text-dark);
  cursor: pointer;
  transition: all 0.3s ease;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg width='12' height='8' viewBox='0 0 12 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1L6 6L11 1' stroke='%23FFB6D9' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1.5rem center;
  padding-right: 3rem;
}

.kawaii-select:focus {
  outline: none;
  border-color: var(--kawaii-pink);
  background: var(--kawaii-bg-white);
  box-shadow: 0 0 0 4px rgba(255, 182, 217, 0.2);
}
```

#### 2.6 导航系统（Navigation System）

导航栏使用**彩虹渐变背景**和**胶囊形链接**，营造活泼友好的第一印象。

```css
/* 顶部导航栏 */
.kawaii-nav {
  background: var(--kawaii-gradient-rainbow);
  padding: 1rem 0;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 4px 12px rgba(255, 182, 217, 0.2);
  backdrop-filter: blur(10px);
}

.kawaii-nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Logo */
.kawaii-nav-logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-weight: 700;
  font-size: 1.25rem;
  color: var(--kawaii-text-dark);
  text-decoration: none;
}

.kawaii-logo-icon {
  animation: kawaiiBounceLoop 2s ease-in-out infinite;
  filter: drop-shadow(0 4px 8px rgba(230, 213, 255, 0.3));
}

/* 导航菜单 */
.kawaii-nav-menu {
  display: flex;
  gap: 1.5rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.kawaii-nav-link {
  color: var(--kawaii-text-dark);
  text-decoration: none;
  font-weight: 500;
  padding: 0.5rem 1.25rem;
  border-radius: var(--kawaii-radius-full);
  transition: all 0.3s ease;
  position: relative;
}

.kawaii-nav-link:hover {
  background: rgba(255, 255, 255, 0.6);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 182, 217, 0.2);
}

.kawaii-nav-link.active {
  background: white;
  box-shadow: 0 4px 12px rgba(255, 182, 217, 0.25);
}

/* 移动端菜单按钮 */
.kawaii-menu-toggle {
  display: none;
  width: 40px;
  height: 40px;
  background: white;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(255, 182, 217, 0.2);
  transition: all 0.3s ease;
}

.kawaii-menu-toggle:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 16px rgba(255, 182, 217, 0.3);
}

@media (max-width: 768px) {
  .kawaii-nav-menu {
    display: none;
  }

  .kawaii-menu-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
```

#### 2.7 卡片网格系统（Card Grid System）

使用**响应式网格布局**和**悬浮效果**展示内容卡片。

```css
/* 卡片网格容器 */
.kawaii-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  padding: 2rem 0;
}

/* 基础卡片 */
.kawaii-card-base {
  background: var(--kawaii-bg-white);
  border-radius: var(--kawaii-radius-lg);
  padding: 2rem;
  box-shadow: var(--kawaii-shadow-sm);
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  cursor: pointer;
}

.kawaii-card-base:hover {
  transform: translateY(-8px);
  box-shadow: var(--kawaii-shadow-md);
}

/* 图片卡片 */
.kawaii-card-image {
  background: var(--kawaii-bg-white);
  border-radius: var(--kawaii-radius-lg);
  overflow: hidden;
  box-shadow: var(--kawaii-shadow-sm);
  transition: all 0.3s ease;
}

.kawaii-card-image:hover {
  transform: translateY(-12px);
  box-shadow: var(--kawaii-shadow-lg);
}

.kawaii-card-image-wrapper {
  width: 100%;
  aspect-ratio: 16/10;
  overflow: hidden;
}

.kawaii-card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.kawaii-card-image:hover img {
  transform: scale(1.1);
}

.kawaii-card-content {
  padding: 1.5rem;
}

.kawaii-card-title {
  font-size: 1.375rem;
  font-weight: 700;
  color: var(--kawaii-text-dark);
  margin-bottom: 0.5rem;
}

.kawaii-card-description {
  color: var(--kawaii-text-medium);
  font-size: 1rem;
  line-height: 1.6;
}
```

### 3. Tailwind CSS 配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        kawaii: {
          pink: '#FFB6D9',
          'pink-light': '#FFDBE9',
          purple: '#E6D5FF',
          'purple-light': '#F5EDFF',
          green: '#D4F1D4',
          'green-light': '#E8F8E8',
          yellow: '#FFF9E6',
          cream: '#FFF9F5',
        },
      },
      borderRadius: {
        'kawaii-sm': '16px',
        'kawaii-md': '24px',
        'kawaii-lg': '32px',
      },
      boxShadow: {
        'kawaii-xs': '0 2px 8px rgba(255, 182, 217, 0.1)',
        'kawaii-sm': '0 4px 12px rgba(255, 182, 217, 0.15)',
        'kawaii-md': '0 8px 20px rgba(255, 182, 217, 0.25)',
        'kawaii-lg': '0 12px 32px rgba(255, 182, 217, 0.35)',
        'kawaii-xl': '0 20px 48px rgba(255, 182, 217, 0.4)',
      },
      animation: {
        'kawaii-bounce': 'kawaiiBounce 0.6s ease-in-out',
        'kawaii-bounce-loop': 'kawaiiBounceLoop 2s ease-in-out infinite',
      },
      keyframes: {
        kawaiiBounce: {
          '0%, 100%': { transform: 'translateY(-4px)' },
          '50%': { transform: 'translateY(-12px)' },
        },
        kawaiiBounceLoop: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-8px)' },
        },
      },
    },
  },
  plugins: [],
};
```

### 4. 使用示例

```html
<!-- Hero 区块 -->
<section class="py-20 px-8 bg-gradient-to-b from-white to-kawaii-cream">
  <div class="max-w-4xl mx-auto text-center">
    <div class="text-6xl mb-6 animate-kawaii-bounce-loop">
      👋
    </div>
    <h1 class="text-5xl font-extrabold mb-4 bg-gradient-to-r from-kawaii-pink to-kawaii-purple bg-clip-text text-transparent">
      欢迎来到可爱世界
    </h1>
    <p class="text-xl text-gray-600 mb-8">
      让界面变得更温暖、更友好
    </p>
    <div class="flex gap-4 justify-center flex-wrap">
      <button class="kawaii-btn kawaii-btn-primary kawaii-btn-large">
        开始探索
      </button>
      <button class="kawaii-btn kawaii-btn-secondary kawaii-btn-large">
        了解更多
      </button>
    </div>
  </div>
</section>

<!-- 卡片网格 -->
<section class="py-16 px-8">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-4xl font-extrabold text-center mb-12 bg-gradient-to-r from-kawaii-pink to-kawaii-green bg-clip-text text-transparent">
      我们的特色
    </h2>
    <div class="kawaii-grid">
      <div class="kawaii-card-base">
        <div class="text-5xl mb-4 animate-kawaii-bounce-loop">🎨</div>
        <h3 class="text-2xl font-bold mb-2">糖果色彩</h3>
        <p class="text-gray-600">温暖治愈的色彩系统</p>
      </div>
      <div class="kawaii-card-base">
        <div class="text-5xl mb-4 animate-kawaii-bounce-loop" style="animation-delay: 0.2s">💫</div>
        <h3 class="text-2xl font-bold mb-2">柔软圆角</h3>
        <p class="text-gray-600">亲和友好的视觉体验</p>
      </div>
      <div class="kawaii-card-base">
        <div class="text-5xl mb-4 animate-kawaii-bounce-loop" style="animation-delay: 0.4s">✨</div>
        <h3 class="text-2xl font-bold mb-2">轻盈动效</h3>
        <p class="text-gray-600">弹跳活泼的交互反馈</p>
      </div>
    </div>
  </div>
</section>
```


---

## English Version (en-US)

### 1. Design Philosophy & Core Principles

**Kawaii Minimal** is a visual style that combines **Japanese Kawaii culture** with **minimalist design principles**. The core philosophy is to create warm, healing, and approachable user experiences through **candy color gradients, hyper-rounded corners, expressive icons, and light animations** while maintaining clear information hierarchy and clean layouts.

**Design Principles**:
- **Simplicity First**: Maintain minimal layout structure with moderate module count
- **Color Accents**: Use candy colors as accents, keep large areas in soft pastel backgrounds
- **Rounded & Soft**: Apply hyper-rounded corners (20-30px) to all elements, pill-shaped buttons (9999px)
- **Emotional Design**: Convey warmth through emoji icons, cute illustrations, and playful copy
- **Light Interactions**: Prefer bouncy, floating animations over harsh linear transitions

### 2. Core Design Requirements

#### 2.1 Candy Color Palette System

The Kawaii Minimal color system features **high-brightness, medium-saturation** candy colors to create a sweet but not overwhelming visual effect.

**Primary Colors**:
- **Peach Pink**: `#FFB6D9` - Primary buttons, emphasis
- **Lavender Purple**: `#E6D5FF` - Secondary buttons, tags
- **Mint Green**: `#D4F1D4` - Success states, positive feedback
- **Cream Yellow**: `#FFF9E6` - Alerts, highlights

**Light Tones**:
- **Light Pink**: `#FFDBE9`
- **Light Lavender**: `#F5EDFF`
- **Light Mint**: `#E8F8E8`
- **Creamy White**: `#FFF9F5`

**Neutral Colors**:
- **Text Dark**: `#333333` - Headings
- **Text Medium**: `#666666` - Body text
- **Background Light**: `#F8F9FA` - Card backgrounds
- **Pure White**: `#FFFFFF` - Main background

**Gradient Schemes**:
```css
/* Pink-Purple Gradient (Primary Buttons) */
background: linear-gradient(135deg, #FFB6D9 0%, #E6D5FF 100%);

/* Pink-Green Gradient (Headings) */
background: linear-gradient(135deg, #FFB6D9 0%, #D4F1D4 100%);

/* Rainbow Gradient (Navigation) */
background: linear-gradient(135deg, #FFB6D9 0%, #E6D5FF 50%, #D4F1D4 100%);

/* Soft Background Gradient */
background: linear-gradient(180deg, #FFFFFF 0%, #FFF9F5 100%);
```

**Complete CSS Variables**:
```css
:root {
  /* Primary Colors */
  --kawaii-pink: #FFB6D9;
  --kawaii-pink-light: #FFDBE9;
  --kawaii-purple: #E6D5FF;
  --kawaii-purple-light: #F5EDFF;
  --kawaii-green: #D4F1D4;
  --kawaii-green-light: #E8F8E8;
  --kawaii-yellow: #FFF9E6;

  /* Neutral Colors */
  --kawaii-text-dark: #333333;
  --kawaii-text-medium: #666666;
  --kawaii-text-light: #999999;
  --kawaii-bg-white: #FFFFFF;
  --kawaii-bg-cream: #FFF9F5;
  --kawaii-bg-gray: #F8F9FA;

  /* Gradients */
  --kawaii-gradient-primary: linear-gradient(135deg, #FFB6D9, #E6D5FF);
  --kawaii-gradient-secondary: linear-gradient(135deg, #FFB6D9, #D4F1D4);
  --kawaii-gradient-rainbow: linear-gradient(135deg, #FFB6D9 0%, #E6D5FF 50%, #D4F1D4 100%);

  /* Shadows */
  --kawaii-shadow-sm: 0 4px 12px rgba(255, 182, 217, 0.15);
  --kawaii-shadow-md: 0 8px 20px rgba(255, 182, 217, 0.25);
  --kawaii-shadow-lg: 0 12px 32px rgba(255, 182, 217, 0.35);

  /* Border Radius */
  --kawaii-radius-sm: 16px;
  --kawaii-radius-md: 24px;
  --kawaii-radius-lg: 32px;
  --kawaii-radius-full: 9999px;
}
```

#### 2.2 Hyper-Rounded Corner System

One of the signature features of Kawaii Minimal is **extreme rounded corners** on all rectangular elements, creating a soft, approachable visual feel.

**Border Radius Levels**:
- **Small**: `16px` - Tags, badges
- **Medium**: `24px` - Input fields, cards
- **Large**: `30-32px` - Main cards, modals
- **Pill**: `9999px / 50%` - All buttons

**CSS Implementation**:
```css
/* Card Rounded Corners */
.kawaii-card {
  background: var(--kawaii-bg-white);
  border-radius: var(--kawaii-radius-lg); /* 32px */
  padding: 2rem;
  box-shadow: var(--kawaii-shadow-md);
  border: 2px solid transparent;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Gradient Border Card */
.kawaii-card-gradient-border {
  position: relative;
  background: var(--kawaii-bg-white);
  border-radius: var(--kawaii-radius-lg);
  padding: 2rem;
}

.kawaii-card-gradient-border::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--kawaii-radius-lg);
  padding: 2px;
  background: var(--kawaii-gradient-rainbow);
  -webkit-mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
}

/* Input Field Rounded Corners */
.kawaii-input {
  background: var(--kawaii-bg-cream);
  border: 2px solid var(--kawaii-pink-light);
  border-radius: var(--kawaii-radius-md); /* 24px */
  padding: 0.875rem 1.5rem;
  font-size: 1rem;
  color: var(--kawaii-text-dark);
  transition: all 0.3s ease;
}

.kawaii-input:focus {
  outline: none;
  border-color: var(--kawaii-pink);
  box-shadow: 0 0 0 4px rgba(255, 182, 217, 0.2);
  transform: translateY(-2px);
}

/* Tag Rounded Corners */
.kawaii-tag {
  display: inline-flex;
  align-items: center;
  padding: 0.5rem 1rem;
  background: var(--kawaii-purple-light);
  color: var(--kawaii-text-dark);
  border-radius: var(--kawaii-radius-sm); /* 16px */
  font-size: 0.875rem;
  font-weight: 600;
}
```

#### 2.3 Pill Button System

All buttons must adopt **fully rounded pill design** (`border-radius: 9999px`) combined with **candy color gradient backgrounds** and **bounce animations**.

**Button Variants**:

```css
/* Base Button Style */
.kawaii-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.875rem 2rem;
  border: none;
  border-radius: var(--kawaii-radius-full); /* 9999px */
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  position: relative;
  overflow: hidden;
}

/* Primary Button (Pink-Purple Gradient) */
.kawaii-btn-primary {
  background: var(--kawaii-gradient-primary);
  color: var(--kawaii-text-dark);
  box-shadow: var(--kawaii-shadow-sm);
}

.kawaii-btn-primary:hover {
  transform: translateY(-4px);
  box-shadow: var(--kawaii-shadow-md);
  animation: kawaiiBounce 0.6s ease-in-out;
}

.kawaii-btn-primary:active {
  transform: translateY(-2px);
  box-shadow: var(--kawaii-shadow-sm);
}

/* Secondary Button (White with Pink Border) */
.kawaii-btn-secondary {
  background: var(--kawaii-bg-white);
  color: var(--kawaii-text-dark);
  border: 2px solid var(--kawaii-pink);
  box-shadow: 0 4px 12px rgba(255, 182, 217, 0.15);
}

.kawaii-btn-secondary:hover {
  background: var(--kawaii-pink-light);
  transform: translateY(-4px);
  box-shadow: var(--kawaii-shadow-md);
}
```

**Bounce Animation**:
```css
@keyframes kawaiiBounce {
  0%, 100% {
    transform: translateY(-4px);
  }
  50% {
    transform: translateY(-12px);
  }
}

/* Continuous Bounce (for icons) */
@keyframes kawaiiBounceLoop {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-8px);
  }
}

.kawaii-bounce-icon {
  animation: kawaiiBounceLoop 2s ease-in-out infinite;
}
```

### 3. Tailwind CSS Configuration

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        kawaii: {
          pink: '#FFB6D9',
          'pink-light': '#FFDBE9',
          purple: '#E6D5FF',
          'purple-light': '#F5EDFF',
          green: '#D4F1D4',
          'green-light': '#E8F8E8',
          yellow: '#FFF9E6',
          cream: '#FFF9F5',
        },
      },
      borderRadius: {
        'kawaii-sm': '16px',
        'kawaii-md': '24px',
        'kawaii-lg': '32px',
      },
      boxShadow: {
        'kawaii-xs': '0 2px 8px rgba(255, 182, 217, 0.1)',
        'kawaii-sm': '0 4px 12px rgba(255, 182, 217, 0.15)',
        'kawaii-md': '0 8px 20px rgba(255, 182, 217, 0.25)',
        'kawaii-lg': '0 12px 32px rgba(255, 182, 217, 0.35)',
        'kawaii-xl': '0 20px 48px rgba(255, 182, 217, 0.4)',
      },
      animation: {
        'kawaii-bounce': 'kawaiiBounce 0.6s ease-in-out',
        'kawaii-bounce-loop': 'kawaiiBounceLoop 2s ease-in-out infinite',
      },
      keyframes: {
        kawaiiBounce: {
          '0%, 100%': { transform: 'translateY(-4px)' },
          '50%': { transform: 'translateY(-12px)' },
        },
        kawaiiBounceLoop: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-8px)' },
        },
      },
    },
  },
  plugins: [],
};
```

### 4. Usage Examples

```html
<!-- Hero Section -->
<section class="py-20 px-8 bg-gradient-to-b from-white to-kawaii-cream">
  <div class="max-w-4xl mx-auto text-center">
    <div class="text-6xl mb-6 animate-kawaii-bounce-loop">
      👋
    </div>
    <h1 class="text-5xl font-extrabold mb-4 bg-gradient-to-r from-kawaii-pink to-kawaii-purple bg-clip-text text-transparent">
      Welcome to Kawaii World
    </h1>
    <p class="text-xl text-gray-600 mb-8">
      Making interfaces warmer and friendlier
    </p>
    <div class="flex gap-4 justify-center flex-wrap">
      <button class="kawaii-btn kawaii-btn-primary kawaii-btn-large">
        Start Exploring
      </button>
      <button class="kawaii-btn kawaii-btn-secondary kawaii-btn-large">
        Learn More
      </button>
    </div>
  </div>
</section>

<!-- Card Grid -->
<section class="py-16 px-8">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-4xl font-extrabold text-center mb-12 bg-gradient-to-r from-kawaii-pink to-kawaii-green bg-clip-text text-transparent">
      Our Features
    </h2>
    <div class="kawaii-grid">
      <div class="kawaii-card-base">
        <div class="text-5xl mb-4 animate-kawaii-bounce-loop">🎨</div>
        <h3 class="text-2xl font-bold mb-2">Candy Colors</h3>
        <p class="text-gray-600">Warm and healing color system</p>
      </div>
      <div class="kawaii-card-base">
        <div class="text-5xl mb-4 animate-kawaii-bounce-loop" style="animation-delay: 0.2s">💫</div>
        <h3 class="text-2xl font-bold mb-2">Soft Corners</h3>
        <p class="text-gray-600">Friendly visual experience</p>
      </div>
      <div class="kawaii-card-base">
        <div class="text-5xl mb-4 animate-kawaii-bounce-loop" style="animation-delay: 0.4s">✨</div>
        <h3 class="text-2xl font-bold mb-2">Light Animations</h3>
        <p class="text-gray-600">Bouncy interactive feedback</p>
      </div>
    </div>
  </div>
</section>
```
