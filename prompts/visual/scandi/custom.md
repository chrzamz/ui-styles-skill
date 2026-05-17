# Custom Prompt - Scandi

## 中文版本 (zh-CN)

### 设计哲学与核心原则

你现在是一名北欧（Scandinavian）极简风格的资深 UI 设计师。Scandi 设计的核心理念是"**简化、明亮、功能至上**"——崇尚自然光线、原始材料（木材、棉麻）与空无之美。整个界面应该像一间通风明亮的北欧公寓：干净、整齐、有节奏感，且有一点温暖的人文气息。

**核心设计原则**：
- 大量留白和浅灰背景（通常 85-95% 的屏幕面积是白色或很浅的灰绿）
- 极简数量的柔和彩色点缀（绿色、蓝色、暖黄、木色），单纯用于功能标记或状态指示
- 工整的栅格布局、清晰的分组和大气的间距
- 轻盈的阴影（几乎感受不到立体感），柔和的圆角
- 优雅的极简图标和精选的一两款 sans-serif 字体

**设计态度**：用户不应该被界面"催促"或"轰炸"，反而应该感受到一种宁静、理性的陪伴感。界面应该像一支深呼吸——不张扬，但让人舒适。

### 八大核心设计要求

#### 1. 色彩与材质系统

**色彩定义**：
```css
/* 北欧极简色板 */
:root {
  /* 背景与中性色 */
  --scandi-white: #FFFFFF;           /* 纯白：卡片、文本背景 */
  --scandi-bg-light: #F9FAFB;        /* 浅灰：主容器背景 */
  --scandi-bg-medium: #F3F4F6;       /* 中灰：分组背景、禁用态 */
  --scandi-bg-dark: #E5E7EB;         /* 深灰：边框、分割线 */

  /* 文本色 */
  --scandi-text-primary: #1F2937;    /* 深灰：正文、标题 */
  --scandi-text-secondary: #6B7280;  /* 中灰：辅助文本、描述 */
  --scandi-text-tertiary: #9CA3AF;   /* 浅灰：标签、占位文本 */

  /* 自然彩色点 - 少量且柔和 */
  --scandi-green: #10B981;           /* 翠绿：完成、成功状态（自然、平和） */
  --scandi-green-light: #D1FAE5;     /* 浅绿：绿色背景、高亮 */
  --scandi-blue: #3B82F6;            /* 天蓝：信息、链接（清爽、信任） */
  --scandi-blue-light: #DBEAFE;      /* 浅蓝：蓝色背景 */
  --scandi-amber: #F59E0B;           /* 琥珀金：警告、提醒（温暖、警惕） */
  --scandi-amber-light: #FEF3C7;     /* 浅金：金色背景 */
  --scandi-wood: #8B7E74;            /* 木色：强调色、图标（温暖、自然） */
  --scandi-sage: #A5B5AB;            /* 鼠尾草绿：柔和强调 */

  /* 阴影 */
  --scandi-shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.05);
  --scandi-shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.08);
  --scandi-shadow-md: 0 4px 8px rgba(0, 0, 0, 0.1);
  --scandi-shadow-lg: 0 8px 16px rgba(0, 0, 0, 0.08);
}
```

**材质质感**：
- **卡片表面**：white背景 + 轻阴影（shadow-sm）+ 小圆角（rounded-lg），像薄纸或细木板
- **背景**：浅灰色（bg-gray-50 或 bg-blue-50），均匀无纹理，光线充足
- **边框**：极淡灰色（border-gray-200），宽度仅 1px，几乎察觉不到，仅用于必要的分组边界
- **阴影**：扩散柔和，不追求深度感，如 `box-shadow: 0 2px 4px rgba(0,0,0,0.08)`

#### 2. 排版与字体系统

**字体选择**：
```css
:root {
  --scandi-font-sans: 'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
  --scandi-font-serif: 'Crimson Text', 'Georgia', serif; /* 可选：标题 */
}

/* 排版规模 */
body {
  font-family: var(--scandi-font-sans);
  font-size: 16px;        /* 基础字号 */
  line-height: 1.5;       /* 行高 */
  color: var(--scandi-text-primary);
  -webkit-font-smoothing: antialiased;
}

h1 { font-size: 32px; font-weight: 500; line-height: 1.2; letter-spacing: -0.02em; }
h2 { font-size: 24px; font-weight: 500; line-height: 1.3; letter-spacing: -0.01em; }
h3 { font-size: 18px; font-weight: 500; line-height: 1.4; }
h4 { font-size: 16px; font-weight: 600; line-height: 1.4; }

p { font-size: 16px; font-weight: 400; line-height: 1.6; letter-spacing: 0; }
.text-small { font-size: 14px; font-weight: 400; line-height: 1.5; }
.text-tiny { font-size: 12px; font-weight: 500; line-height: 1.4; letter-spacing: 0.02em; }

/* 标题特殊处理：light weight + tracking */
h1, h2, h3 {
  font-weight: 300;       /* 极轻的字重，显得优雅 */
  letter-spacing: -0.02em;
  color: var(--scandi-text-primary);
}

/* 强调与链接 */
strong { font-weight: 600; }
a { color: var(--scandi-blue); text-decoration: none; }
a:hover { text-decoration: underline; }
```

**排版习惯**：
- 优先使用 font-weight: 300/400（Light/Regular），避免 Bold
- 充足的行高（1.5-1.6），增加阅读舒适度
- 大标题用 light weight 显得优雅、空间感强
- 段落文本保持 16px，最小不低于 14px

#### 3. 间距与布局栅格

**间距系统**：
```css
:root {
  /* 基础间距单位：4px */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;
  --space-3xl: 64px;

  /* 标准容器宽度 */
  --container-sm: 384px;  /* 小屏 */
  --container-md: 640px;  /* 中屏 */
  --container-lg: 1000px; /* 大屏 */

  /* 圆角 */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
}

/* 主容器 */
.container {
  max-width: var(--container-md);
  margin: 0 auto;
  padding: var(--space-md);
  background: var(--scandi-bg-light);
}

/* 卡片与区块间距 */
.card {
  background: var(--scandi-white);
  padding: var(--space-lg);
  border-radius: var(--radius-lg);
  border: 1px solid var(--scandi-bg-dark);
  margin-bottom: var(--space-md);
  box-shadow: var(--scandi-shadow-sm);
}

/* 栅格 */
.grid {
  display: grid;
  gap: var(--space-md);
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}

.grid-2 {
  grid-template-columns: repeat(2, 1fr);
}

@media (max-width: 640px) {
  .grid-2 { grid-template-columns: 1fr; }
}

/* 垂直堆叠 */
.stack { display: flex; flex-direction: column; gap: var(--space-md); }
.stack-xs { gap: var(--space-xs); }
.stack-sm { gap: var(--space-sm); }
.stack-lg { gap: var(--space-lg); }

/* 水平排列 */
.hstack { display: flex; align-items: center; gap: var(--space-md); }
.hstack-sm { gap: var(--space-sm); }
```

#### 4. 组件设计：按钮系统

**按钮样式**：
```css
/* 主按钮：纯色填充 + 轻阴影 */
.btn-primary {
  background: var(--scandi-blue);
  color: white;
  padding: 10px 24px;
  border-radius: var(--radius-lg);
  font-size: 14px;
  font-weight: 500;
  border: none;
  cursor: pointer;
  box-shadow: var(--scandi-shadow-sm);
  transition: all 200ms ease;
}

.btn-primary:hover {
  background: #2563EB; /* 稍深的蓝 */
  box-shadow: var(--scandi-shadow-md);
  transform: translateY(-2px);
}

.btn-primary:active {
  transform: translateY(0);
  box-shadow: var(--scandi-shadow-xs);
}

/* 次按钮：白底 + 灰边 */
.btn-secondary {
  background: var(--scandi-white);
  color: var(--scandi-text-primary);
  padding: 10px 24px;
  border-radius: var(--radius-lg);
  font-size: 14px;
  font-weight: 500;
  border: 1px solid var(--scandi-bg-dark);
  cursor: pointer;
  transition: all 200ms ease;
}

.btn-secondary:hover {
  background: var(--scandi-bg-light);
  border-color: var(--scandi-blue);
  color: var(--scandi-blue);
}

/* 成功按钮 */
.btn-success {
  background: var(--scandi-green);
  color: white;
  padding: 10px 24px;
  border-radius: var(--radius-lg);
  font-size: 14px;
  font-weight: 500;
  border: none;
  cursor: pointer;
  box-shadow: var(--scandi-shadow-sm);
  transition: all 200ms ease;
}

.btn-success:hover {
  background: #059669;
  box-shadow: var(--scandi-shadow-md);
}

/* 圆形小按钮 - 适合 icon */
.btn-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--scandi-bg-light);
  border: 1px solid var(--scandi-bg-dark);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 200ms ease;
  color: var(--scandi-text-secondary);
}

.btn-icon:hover {
  background: var(--scandi-white);
  border-color: var(--scandi-blue);
  color: var(--scandi-blue);
}

/* 禁用态 */
button:disabled,
.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

#### 5. 组件设计：卡片与容器

**卡片系统**：
```css
/* 标准卡片 */
.card {
  background: var(--scandi-white);
  border: 1px solid var(--scandi-bg-dark);
  border-radius: var(--radius-lg);
  padding: var(--space-lg);
  box-shadow: var(--scandi-shadow-sm);
  transition: all 200ms ease;
}

.card:hover {
  box-shadow: var(--scandi-shadow-md);
  border-color: var(--scandi-sage);
}

/* 卡片头 */
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-md);
  padding-bottom: var(--space-md);
  border-bottom: 1px solid var(--scandi-bg-dark);
}

.card-title {
  font-size: 18px;
  font-weight: 500;
  color: var(--scandi-text-primary);
}

/* 卡片内容区 */
.card-body {
  color: var(--scandi-text-primary);
  line-height: 1.6;
}

/* 卡片底部动作区 */
.card-footer {
  display: flex;
  gap: var(--space-md);
  margin-top: var(--space-lg);
  padding-top: var(--space-md);
  border-top: 1px solid var(--scandi-bg-dark);
}

/* 浮动卡片 - 用于强调内容 */
.card-floating {
  position: absolute;
  bottom: var(--space-lg);
  right: var(--space-lg);
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(0, 0, 0, 0.08);
  padding: var(--space-md);
  border-radius: var(--radius-lg);
  box-shadow: var(--scandi-shadow-lg);
}

/* 不同背景的卡片 */
.card-accent-green {
  background: var(--scandi-green-light);
  border-color: var(--scandi-green);
}

.card-accent-blue {
  background: var(--scandi-blue-light);
  border-color: var(--scandi-blue);
}

.card-accent-amber {
  background: var(--scandi-amber-light);
  border-color: var(--scandi-amber);
}
```

#### 6. 组件设计：表单与输入

**表单元素**：
```css
/* 输入框 */
input[type="text"],
input[type="email"],
input[type="password"],
textarea,
select {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid var(--scandi-bg-dark);
  border-radius: var(--radius-md);
  background: var(--scandi-white);
  font-size: 14px;
  color: var(--scandi-text-primary);
  font-family: inherit;
  transition: all 200ms ease;
}

input[type="text"]:focus,
input[type="email"]:focus,
input[type="password"]:focus,
textarea:focus,
select:focus {
  outline: none;
  border-color: var(--scandi-blue);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
  background: var(--scandi-white);
}

/* 标签 */
label {
  display: block;
  margin-bottom: var(--space-sm);
  font-size: 14px;
  font-weight: 500;
  color: var(--scandi-text-primary);
}

/* 帮助文本 */
.input-help {
  font-size: 12px;
  color: var(--scandi-text-tertiary);
  margin-top: var(--space-xs);
}

/* 错误状态 */
.input-error {
  border-color: #EF4444;
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
}

.error-text {
  color: #EF4444;
  font-size: 12px;
  margin-top: var(--space-xs);
}

/* 成功状态 */
.input-success {
  border-color: var(--scandi-green);
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

/* Checkbox & Radio */
input[type="checkbox"],
input[type="radio"] {
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: var(--scandi-blue);
}

.checkbox-group,
.radio-group {
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
}

.checkbox-item,
.radio-item {
  display: flex;
  align-items: center;
  gap: var(--space-sm);
  cursor: pointer;
}

.checkbox-item label,
.radio-item label {
  margin-bottom: 0;
  cursor: pointer;
}
```

#### 7. 交互动效与微动画

**交互规则**：
```css
/* 全局过渡 */
* {
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1); /* ease-in-out */
}

/* Hover 动效：轻微背景提亮 + 阴影增强 */
.interactive {
  transition: background-color 150ms ease,
              box-shadow 150ms ease,
              border-color 150ms ease;
}

.interactive:hover {
  background-color: var(--scandi-bg-light);
  box-shadow: var(--scandi-shadow-md);
}

/* 焦点态：蓝色边框 */
.interactive:focus-visible {
  outline: 2px solid var(--scandi-blue);
  outline-offset: 4px;
}

/* 按钮按压反馈 */
button:active {
  transform: scale(0.98);
}

/* 链接下划线动效 */
a {
  position: relative;
  text-decoration: none;
  color: var(--scandi-blue);
}

a::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0%;
  height: 2px;
  background: var(--scandi-blue);
  transition: width 200ms ease;
}

a:hover::after {
  width: 100%;
}

/* 加载动画 */
@keyframes scandi-spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.spinner {
  width: 24px;
  height: 24px;
  border: 2px solid var(--scandi-bg-dark);
  border-top-color: var(--scandi-blue);
  border-radius: 50%;
  animation: scandi-spin 0.6s linear infinite;
}

/* Fade In */
@keyframes scandi-fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}

.fade-in {
  animation: scandi-fade-in 300ms ease;
}

/* Slide In from left */
@keyframes scandi-slide-in-left {
  from {
    opacity: 0;
    transform: translateX(-16px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.slide-in-left {
  animation: scandi-slide-in-left 300ms ease;
}

/* 减少动效 - 辅助功能 */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

#### 8. 响应式设计与暗色模式

**响应式布局**：
```css
/* 手机 */
@media (max-width: 640px) {
  :root {
    font-size: 14px;
  }

  .container {
    padding: var(--space-md);
  }

  h1 { font-size: 24px; }
  h2 { font-size: 18px; }

  .grid-2,
  .grid {
    grid-template-columns: 1fr;
  }

  .hide-mobile {
    display: none;
  }
}

/* 平板 */
@media (min-width: 641px) and (max-width: 1024px) {
  .grid-2 {
    grid-template-columns: repeat(2, 1fr);
  }

  .hide-tablet {
    display: none;
  }
}

/* 桌面 */
@media (min-width: 1025px) {
  .container {
    max-width: var(--container-lg);
  }

  .hide-desktop {
    display: none;
  }
}

/* 暗色模式 - 可选 */
@media (prefers-color-scheme: dark) {
  :root {
    --scandi-white: #1F2937;
    --scandi-bg-light: #111827;
    --scandi-bg-medium: #1F2937;
    --scandi-bg-dark: #374151;
    --scandi-text-primary: #F3F4F6;
    --scandi-text-secondary: #D1D5DB;
    --scandi-text-tertiary: #9CA3AF;
  }
}
```

### Tailwind CSS 配置

在项目的 `tailwind.config.js` 中扩展主题配置，完整支持 Scandi 设计系统：

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        'scandi': {
          'white': '#FFFFFF',
          'bg-light': '#F9FAFB',
          'bg-medium': '#F3F4F6',
          'bg-dark': '#E5E7EB',
          'text': '#1F2937',
          'text-secondary': '#6B7280',
          'text-tertiary': '#9CA3AF',
          'green': '#10B981',
          'green-light': '#D1FAE5',
          'blue': '#3B82F6',
          'blue-light': '#DBEAFE',
          'amber': '#F59E0B',
          'amber-light': '#FEF3C7',
          'wood': '#8B7E74',
          'sage': '#A5B5AB',
        }
      },
      spacing: {
        'xs': '4px',
        'sm': '8px',
        'md': '16px',
        'lg': '24px',
        'xl': '32px',
        '2xl': '48px',
        '3xl': '64px',
      },
      boxShadow: {
        'scandi-xs': '0 1px 2px rgba(0, 0, 0, 0.05)',
        'scandi-sm': '0 2px 4px rgba(0, 0, 0, 0.08)',
        'scandi-md': '0 4px 8px rgba(0, 0, 0, 0.1)',
        'scandi-lg': '0 8px 16px rgba(0, 0, 0, 0.08)',
      },
      borderRadius: {
        'scandi-sm': '4px',
        'scandi-md': '8px',
        'scandi-lg': '12px',
        'scandi-xl': '16px',
      },
      fontFamily: {
        'scandi': ['"Inter"', '"Segoe UI"', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
      },
    },
  },
}
```

### 使用示例

#### 完整的个人仪表板演示

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>北欧极简仪表板</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    :root {
      --scandi-blue: #3B82F6;
      --scandi-green: #10B981;
      --scandi-amber: #F59E0B;
      --scandi-text: #1F2937;
      --scandi-secondary: #6B7280;
    }

    body {
      background-color: #F9FAFB;
      font-family: 'Inter', sans-serif;
      color: var(--scandi-text);
    }

    .card {
      background: white;
      border: 1px solid #E5E7EB;
      border-radius: 12px;
      padding: 24px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
      transition: all 200ms ease;
    }

    .card:hover {
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      border-color: #A5B5AB;
    }
  </style>
</head>
<body>
  <div class="min-h-screen p-8">
    <div class="max-w-6xl mx-auto">
      <!-- Header -->
      <div class="mb-12">
        <h1 class="text-4xl font-light text-gray-800 mb-2">我的仪表板</h1>
        <p class="text-gray-500">今日一览，任务管理与进度追踪</p>
      </div>

      <!-- 统计卡片网格 -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <!-- 完成任务 -->
        <div class="card">
          <div class="flex items-start justify-between mb-4">
            <h3 class="text-sm font-medium text-gray-500">今日完成</h3>
            <span class="text-2xl">✓</span>
          </div>
          <p class="text-3xl font-light text-gray-800">8/12</p>
          <p class="text-xs text-gray-400 mt-2">较昨日增加 2 项</p>
          <div class="mt-4 bg-gray-100 rounded-full h-2">
            <div class="bg-green-500 h-2 rounded-full" style="width: 66%;"></div>
          </div>
        </div>

        <!-- 日程安排 -->
        <div class="card">
          <div class="flex items-start justify-between mb-4">
            <h3 class="text-sm font-medium text-gray-500">日程安排</h3>
            <span class="text-2xl">📅</span>
          </div>
          <p class="text-3xl font-light text-gray-800">3</p>
          <p class="text-xs text-gray-400 mt-2">今日待处理</p>
          <div class="mt-4 flex gap-2">
            <span class="inline-block px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs">会议 10:00</span>
          </div>
        </div>

        <!-- 周进度 -->
        <div class="card">
          <div class="flex items-start justify-between mb-4">
            <h3 class="text-sm font-medium text-gray-500">本周进度</h3>
            <span class="text-2xl">📊</span>
          </div>
          <p class="text-3xl font-light text-gray-800">45%</p>
          <p class="text-xs text-gray-400 mt-2">预计周五完成</p>
          <div class="mt-4 bg-gray-100 rounded-full h-2">
            <div class="bg-amber-500 h-2 rounded-full" style="width: 45%;"></div>
          </div>
        </div>
      </div>

      <!-- 任务列表 -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <!-- 待办列表 -->
        <div class="card">
          <h2 class="text-xl font-light text-gray-800 mb-6 pb-4 border-b border-gray-200">
            待办事项
          </h2>
          <div class="space-y-3">
            <div class="flex items-center gap-3 p-3 bg-gray-50 rounded-lg hover:bg-white transition">
              <input type="checkbox" class="w-5 h-5" />
              <span class="text-gray-700">完成项目文档</span>
              <span class="ml-auto text-xs text-amber-600 bg-amber-50 px-2 py-1 rounded">紧急</span>
            </div>
            <div class="flex items-center gap-3 p-3 bg-gray-50 rounded-lg hover:bg-white transition">
              <input type="checkbox" class="w-5 h-5" />
              <span class="text-gray-700">代码审查</span>
              <span class="ml-auto text-xs text-blue-600 bg-blue-50 px-2 py-1 rounded">进行中</span>
            </div>
            <div class="flex items-center gap-3 p-3 bg-gray-50 rounded-lg hover:bg-white transition">
              <input type="checkbox" class="w-5 h-5" checked />
              <span class="text-gray-400 line-through">邮件回复</span>
              <span class="ml-auto text-xs text-green-600 bg-green-50 px-2 py-1 rounded">已完成</span>
            </div>
          </div>
          <button class="mt-6 w-full py-2 px-4 bg-blue-500 text-white rounded-lg font-medium hover:bg-blue-600 transition">
            新增任务
          </button>
        </div>

        <!-- 最近活动 -->
        <div class="card">
          <h2 class="text-xl font-light text-gray-800 mb-6 pb-4 border-b border-gray-200">
            最近活动
          </h2>
          <div class="space-y-4">
            <div class="flex gap-4">
              <div class="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center text-green-600 flex-shrink-0">
                ✓
              </div>
              <div>
                <p class="text-sm font-medium text-gray-800">任务完成</p>
                <p class="text-xs text-gray-500">设计评审 · 今天 14:30</p>
              </div>
            </div>
            <div class="flex gap-4">
              <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 flex-shrink-0">
                ◆
              </div>
              <div>
                <p class="text-sm font-medium text-gray-800">会议邀请</p>
                <p class="text-xs text-gray-500">站会 · 明天 10:00</p>
              </div>
            </div>
            <div class="flex gap-4">
              <div class="w-10 h-10 rounded-full bg-amber-100 flex items-center justify-center text-amber-600 flex-shrink-0">
                !
              </div>
              <div>
                <p class="text-sm font-medium text-gray-800">提醒</p>
                <p class="text-xs text-gray-500">代码审查截止 · 今天 17:00</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
```

---

## English Version (en-US)

### Design Philosophy & Core Principles

You are now a senior UI designer specializing in Scandinavian minimalism. The core principle of Scandi design is **"Simplify, Brighten, Function First"**—celebrating natural light, raw materials (wood, linen) and the beauty of emptiness. The entire interface should feel like a well-lit Scandinavian apartment: clean, organized, rhythmic, and quietly warm.

**Core Design Principles**:
- Large amounts of white space and pale gray backgrounds (typically 85-95% of screen area)
- Minimal muted color accents (greens, blues, warm yellows, wood tones) for functional status only
- Orderly grid layouts, clear grouping and generous spacing
- Light, diffused shadows (barely noticeable depth), soft rounded corners
- Elegant minimal icons and one or two carefully chosen sans-serif typefaces

**Design Attitude**: Users should not feel "rushed" or "bombarded" by the interface. Instead, they should sense calm, rational accompaniment. The interface should feel like a deep breath—unassuming yet deeply comfortable.

### 8 Core Design Requirements

**[1. Color & Material System]**
- **Primary Colors**: White (#FFFFFF), Light Gray (#F9FAFB), Medium Gray (#F3F4F6), Dark Gray (#E5E7EB)
- **Text Colors**: Primary (#1F2937), Secondary (#6B7280), Tertiary (#9CA3AF)
- **Accent Colors**: Green (#10B981), Blue (#3B82F6), Amber (#F59E0B), Wood (#8B7E74), Sage (#A5B5AB)
- **Shadows**: Soft and diffused (0 2px 4px rgba(0,0,0,0.08) to 0 8px 16px rgba(0,0,0,0.08))
- **Material Feel**: Paper-like or thin wood surfaces, no strong highlights or thick shadows

**[2. Typography System]**
- **Primary Font**: Inter, Segoe UI, sans-serif (clean, minimal)
- **Hierarchy**: H1 (32px, weight 300), H2 (24px, weight 300), Body (16px, weight 400)
- **Line Height**: 1.5-1.6 for comfort and readability
- **Letter Spacing**: Slightly negative (-0.02em) for tight, elegant headers
- **Weight Preference**: Light (300) and Regular (400), avoid Bold for minimalist feel

**[3. Spacing & Layout Grid]**
- **Base Unit**: 4px (xs: 4px, sm: 8px, md: 16px, lg: 24px, xl: 32px)
- **Grid**: Auto-fit with minmax(280px, 1fr) or explicit 2-column layout
- **Rounded Corners**: 4px, 8px, 12px, 16px (never sharp corners)
- **Padding**: Cards use 24px, containers use 16px
- **Gap**: Components separated by 16px horizontally, 24px vertically

**[4. Button System]**
- **Primary Button**: Solid color fill (blue), light shadow, rounded 12px
- **Secondary Button**: White background + subtle gray border, no shadow
- **Success Button**: Green background with white text
- **Icon Button**: 40x40px, circular, gray background with border
- **Hover State**: Deeper color, enhanced shadow, subtle lift (translateY -2px)
- **Active State**: Scale back to normal, reduced shadow

**[5. Card & Container Components]**
- **Standard Card**: White background + 1px border (#E5E7EB) + small shadow, rounded 12px
- **Card Hover**: Shadow increases, border tint towards sage green
- **Card Header**: 18px title, bottom border, margin-bottom 16px
- **Floating Card**: Positioned absolutely, semi-transparent white with backdrop blur
- **Accent Cards**: Light colored backgrounds (green, blue, amber) with matching borders

**[6. Form Elements]**
- **Input Fields**: 10px vertical padding, 12px horizontal, 1px subtle border, rounded 8px
- **Focus State**: Blue border + light blue halo (0 0 0 3px rgba(59,130,246,0.1))
- **Labels**: 14px, font-weight 500, below or above input
- **Error State**: Red border + red text + help text below
- **Success State**: Green border + green halo
- **Checkbox/Radio**: Native styling with blue accent color (accent-color: #3B82F6)

**[7. Micro-interactions & Animations]**
- **Transition Duration**: 150-200ms for all interactive states
- **Easing**: cubic-bezier(0.4, 0, 0.2, 1) (ease-in-out)
- **Hover Feedback**: Subtle background lift + shadow increase (no dramatic transforms)
- **Focus Indicator**: 2px solid blue outline with 4px offset
- **Loading Spinner**: 24px circular rotation, blue top border
- **Fade In/Slide In**: 300ms animations for content appearance
- **Respect prefers-reduced-motion**: Disable animations for users who prefer it

**[8. Responsive & Dark Mode]**
- **Mobile (< 640px)**: Single column layouts, smaller font sizes (14px base)
- **Tablet (641px-1024px)**: 2-column grids where applicable
- **Desktop (> 1024px)**: Full width with 1000px max-width container
- **Dark Mode**: Invert backgrounds and text, maintain color relationships
- **Flexible Typography**: Use clamp() for responsive font sizes

### Tailwind CSS Configuration

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        'scandi': {
          'white': '#FFFFFF',
          'bg': '#F9FAFB',
          'text': '#1F2937',
          'text-secondary': '#6B7280',
          'green': '#10B981',
          'blue': '#3B82F6',
          'amber': '#F59E0B',
          'wood': '#8B7E74',
        }
      },
      spacing: { 'xs': '4px', 'sm': '8px', 'md': '16px', 'lg': '24px', 'xl': '32px' },
      boxShadow: {
        'scandi-sm': '0 2px 4px rgba(0, 0, 0, 0.08)',
        'scandi-md': '0 4px 8px rgba(0, 0, 0, 0.1)',
      },
    },
  },
}
```

### Usage Example

A Scandinavian personal dashboard featuring task overview, daily schedule, progress tracking, to-do list with status tags (urgent/in-progress/completed), and recent activity feed. All components use subtle shadows, light typography, generous spacing, and muted color accents. The overall feel is calm, unobtrusive, and functionally clear.
