# Claymorphism (黏土形态) - Custom Prompt

## 中文版本 (zh-CN)

### 设计概述
为产品生成 **Claymorphism（黏土形态）** 风格的界面设计。这是一种反扁平化的 3D 设计风格,通过模拟真实世界的黏土或橡皮泥质感,创造出柔软、蓬松、亲和的数字体验。每个 UI 元素都应该像是手工捏制的黏土物体,具有明显的厚度感、圆润的边缘和柔和的光影。

## 核心设计要求

### 1. 双层阴影系统（The Soul of Claymorphism）

**外部阴影（Drop Shadow）- 制造悬浮感**:
- 使用两层外部阴影叠加
- 第一层：深色大范围模糊,模拟遮挡阴影
- 第二层：浅色中等范围,模拟环境光反射

**内部阴影（Inner Shadow）- 创造厚度感**:
- 上方：浅色内阴影,模拟顶部高光
- 下方：深色内阴影,模拟底部遮挡
- 形成「凸起」的 3D 效果

**完整 CSS 实现**:
```css
.clay-card {
  background: linear-gradient(145deg, #ffb3d9, #ff8fb3);
  border-radius: 32px;
  padding: 2rem;

  /* 外部阴影 - 双层叠加 */
  box-shadow:
    /* 主阴影 - 深色大范围 */
    -6px -6px 20px rgba(255, 255, 255, 0.7),
    6px 6px 20px rgba(255, 143, 179, 0.4),
    /* 内部阴影 - 模拟厚度 */
    inset -3px -3px 8px rgba(255, 255, 255, 0.3),
    inset 3px 3px 8px rgba(255, 143, 179, 0.4);

  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.clay-card:hover {
  transform: translateY(-4px);

  /* hover 时阴影扩散,增强悬浮感 */
  box-shadow:
    -8px -8px 24px rgba(255, 255, 255, 0.8),
    8px 8px 24px rgba(255, 143, 179, 0.5),
    inset -3px -3px 8px rgba(255, 255, 255, 0.3),
    inset 3px 3px 8px rgba(255, 143, 179, 0.4);
}

.clay-card:active {
  transform: translateY(0);

  /* active 时阴影收缩,模拟被按下 */
  box-shadow:
    -3px -3px 10px rgba(255, 255, 255, 0.6),
    3px 3px 10px rgba(255, 143, 179, 0.3),
    /* 内部阴影加深 */
    inset -4px -4px 10px rgba(255, 255, 255, 0.2),
    inset 4px 4px 10px rgba(255, 143, 179, 0.5);
}
```

### 2. 极致圆润（Extreme Roundness）

**圆角策略**:
- 大型卡片/容器: `border-radius: 32px - 48px`
- 中型按钮: `border-radius: 24px - 32px`
- 小型标签/徽章: `border-radius: 16px - 24px`
- 图标容器: `border-radius: 50%` (完美圆形)
- 输入框: `border-radius: 20px - 28px`

**完整 CSS 实现**:
```css
/* 大型容器 */
.clay-container-large {
  border-radius: 48px;
  padding: 3rem;
}

/* 按钮组件 */
.clay-button {
  border-radius: 28px;
  padding: 1rem 2rem;
  font-size: 1rem;
  font-weight: 700;
  border: none;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* 胶囊按钮 */
.clay-button-pill {
  border-radius: 50px;
  padding: 0.875rem 2.5rem;
}

/* 圆形图标容器 */
.clay-icon-wrapper {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 输入框 */
.clay-input {
  border-radius: 24px;
  padding: 1rem 1.5rem;
  border: none;
  font-size: 1rem;
}

/* 标签 */
.clay-tag {
  border-radius: 20px;
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  display: inline-block;
}
```

### 3. 马卡龙色彩系统（Macaron Color Palette）

**色彩原则**:
- 高明度（Lightness > 70%）
- 低饱和度（Saturation 40-60%）
- 柔和的色调变化
- 背景色与主体色同色系但更浅

**完整色彩方案**:
```css
:root {
  /* 粉色系 - Pink Family */
  --clay-pink-light: #ffc8dd;
  --clay-pink-main: #ffb3d9;
  --clay-pink-medium: #ff99ac;
  --clay-pink-dark: #ff8fb3;
  --clay-pink-deep: #ff6a88;

  /* 蓝色系 - Blue Family */
  --clay-blue-light: #cae9ff;
  --clay-blue-main: #a2d2ff;
  --clay-blue-medium: #7eb8e0;
  --clay-blue-dark: #5a9fd4;

  /* 紫色系 - Purple Family */
  --clay-purple-light: #e4c1f9;
  --clay-purple-main: #d4a5f3;
  --clay-purple-medium: #c48ee8;
  --clay-purple-dark: #b377dc;

  /* 绿色系 - Green Family */
  --clay-green-light: #d8f3dc;
  --clay-green-main: #b7e4c7;
  --clay-green-medium: #95d5b2;
  --clay-green-dark: #74c69d;

  /* 黄色系 - Yellow Family */
  --clay-yellow-light: #fff4bd;
  --clay-yellow-main: #ffe6a7;
  --clay-yellow-medium: #ffd98e;
  --clay-yellow-dark: #ffcc77;

  /* 中性色 - Neutral */
  --clay-white: #ffffff;
  --clay-gray-light: #f8f9fa;
  --clay-gray-medium: #e9ecef;
  --clay-text-primary: #495057;
  --clay-text-secondary: #6c757d;

  /* 渐变背景 */
  --clay-gradient-warm: linear-gradient(135deg, #ffecd2 0%, #fcb69f 50%, #ffecd2 100%);
  --clay-gradient-cool: linear-gradient(135deg, #cae9ff 0%, #a2d2ff 50%, #cae9ff 100%);
  --clay-gradient-purple: linear-gradient(135deg, #e4c1f9 0%, #d4a5f3 50%, #e4c1f9 100%);
}

/* 配色示例 - 粉色主题 */
body.theme-pink {
  background: var(--clay-gradient-warm);
}

.clay-card-pink {
  background: linear-gradient(145deg, var(--clay-pink-light), var(--clay-pink-main));
}

.clay-button-pink {
  background: linear-gradient(145deg, var(--clay-pink-medium), var(--clay-pink-dark));
  color: var(--clay-white);
}

/* 配色示例 - 蓝色主题 */
body.theme-blue {
  background: var(--clay-gradient-cool);
}

.clay-card-blue {
  background: linear-gradient(145deg, var(--clay-blue-light), var(--clay-blue-main));
}
```

### 4. 按钮设计（Button Components）

**按钮的物理反馈**:
- Idle: 正常悬浮状态
- Hover: 轻微上浮 + 阴影扩散
- Active: 按下效果 + 阴影收缩 + 内阴影加深
- 使用弹性动画曲线

**完整 CSS 实现**:
```css
/* 主要按钮 */
.clay-btn-primary {
  background: linear-gradient(145deg, #ff99ac, #ff6a88);
  color: #ffffff;
  padding: 1rem 2rem;
  border-radius: 28px;
  border: none;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);

  /* 双层外部阴影 + 内部阴影 */
  box-shadow:
    -4px -4px 12px rgba(255, 255, 255, 0.6),
    4px 4px 12px rgba(255, 106, 136, 0.4),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(255, 106, 136, 0.3);

  /* 弹性动画 */
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.clay-btn-primary:hover {
  transform: translateY(-3px);
  box-shadow:
    -6px -6px 16px rgba(255, 255, 255, 0.7),
    6px 6px 16px rgba(255, 106, 136, 0.5),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(255, 106, 136, 0.3);
}

.clay-btn-primary:active {
  transform: translateY(0);
  box-shadow:
    -2px -2px 8px rgba(255, 255, 255, 0.5),
    2px 2px 8px rgba(255, 106, 136, 0.3),
    /* 内阴影加深,模拟被压扁 */
    inset -3px -3px 6px rgba(255, 255, 255, 0.1),
    inset 3px 3px 6px rgba(255, 106, 136, 0.4);
}

/* 次要按钮 */
.clay-btn-secondary {
  background: linear-gradient(145deg, #ffc8dd, #ffafcc);
  color: #ff6a88;
  padding: 1rem 2rem;
  border-radius: 28px;
  border: none;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow:
    -4px -4px 12px rgba(255, 255, 255, 0.6),
    4px 4px 12px rgba(255, 175, 204, 0.4),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(255, 175, 204, 0.3);
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* 图标按钮 */
.clay-btn-icon {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: linear-gradient(145deg, #ffb3d9, #ff8fb3);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow:
    -4px -4px 12px rgba(255, 255, 255, 0.6),
    4px 4px 12px rgba(255, 143, 179, 0.4),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(255, 143, 179, 0.3);
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

### 5. 输入框与表单（Input and Form Elements）

**凹陷效果（Inset Style）**:
- 使用内阴影创造「挖出」的凹槽效果
- 背景色略深于容器
- 聚焦时内阴影加深 + 外发光

**完整 CSS 实现**:
```css
/* 文本输入框 */
.clay-input {
  width: 100%;
  padding: 1rem 1.5rem;
  border: none;
  border-radius: 24px;
  font-size: 1rem;
  font-weight: 500;
  color: #495057;

  /* 凹陷效果 - 反向内阴影 */
  background: linear-gradient(145deg, #f0e5f5, #e8d8f0);
  box-shadow:
    inset 3px 3px 8px rgba(200, 170, 220, 0.3),
    inset -3px -3px 8px rgba(255, 255, 255, 0.5);

  transition: all 0.3s ease;
}

.clay-input:focus {
  outline: none;

  /* 聚焦时内阴影加深 + 外发光 */
  box-shadow:
    inset 4px 4px 10px rgba(200, 170, 220, 0.4),
    inset -4px -4px 10px rgba(255, 255, 255, 0.6),
    0 0 0 4px rgba(212, 165, 243, 0.2);
}

.clay-input::placeholder {
  color: #adb5bd;
  font-weight: 400;
}

/* 文本区域 */
.clay-textarea {
  width: 100%;
  padding: 1rem 1.5rem;
  border: none;
  border-radius: 24px;
  font-size: 1rem;
  font-weight: 500;
  color: #495057;
  min-height: 120px;
  resize: vertical;
  font-family: inherit;
  line-height: 1.6;
  background: linear-gradient(145deg, #f0e5f5, #e8d8f0);
  box-shadow:
    inset 3px 3px 8px rgba(200, 170, 220, 0.3),
    inset -3px -3px 8px rgba(255, 255, 255, 0.5);
  transition: all 0.3s ease;
}

/* 复选框（Checkbox） */
.clay-checkbox-wrapper {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
}

.clay-checkbox {
  appearance: none;
  width: 28px;
  height: 28px;
  border-radius: 8px;
  background: linear-gradient(145deg, #ffc8dd, #ffafcc);
  box-shadow:
    -3px -3px 8px rgba(255, 255, 255, 0.6),
    3px 3px 8px rgba(255, 175, 204, 0.4),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(255, 175, 204, 0.3);
  cursor: pointer;
  position: relative;
  transition: all 0.3s ease;
}

.clay-checkbox:checked {
  background: linear-gradient(145deg, #ff99ac, #ff6a88);
  box-shadow:
    inset 3px 3px 8px rgba(255, 106, 136, 0.4),
    inset -3px -3px 8px rgba(255, 255, 255, 0.3);
}

.clay-checkbox:checked::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #ffffff;
  font-size: 16px;
  font-weight: 800;
}
```

### 6. 导航栏（Navigation Bar）

**设计特点**:
- 固定顶部或居中悬浮
- 使用胶囊形状
- 背景与页面色系一致但更鲜艳
- Logo 和连结使用文字阴影增强立体感

**完整 CSS 实现**:
```css
/* 悬浮导航栏 */
.clay-nav {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  padding: 1rem 2rem;
  background: linear-gradient(145deg, #ffb3ba, #ff8fab);
  border-radius: 50px;
  box-shadow:
    -6px -6px 16px rgba(255, 255, 255, 0.6),
    6px 6px 16px rgba(255, 143, 171, 0.4),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(255, 143, 171, 0.3);
}

.clay-nav-content {
  display: flex;
  align-items: center;
  gap: 3rem;
}

.clay-logo {
  font-size: 1.5rem;
  font-weight: 800;
  color: #ffffff;
  text-decoration: none;

  /* 文字阴影创造立体感 */
  text-shadow:
    2px 2px 4px rgba(255, 143, 171, 0.3),
    -1px -1px 2px rgba(255, 255, 255, 0.3);
}

.clay-nav-menu {
  display: flex;
  list-style: none;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.clay-nav-link {
  color: rgba(255, 255, 255, 0.85);
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.3s ease;
  text-shadow: 1px 1px 2px rgba(255, 143, 171, 0.2);
}

.clay-nav-link:hover,
.clay-nav-link.active {
  color: #ffffff;
  text-shadow:
    2px 2px 4px rgba(255, 143, 171, 0.4),
    -1px -1px 2px rgba(255, 255, 255, 0.4);
}
```

### 7. 进度条与滑块（Progress and Slider）

**设计特点**:
- 轨道使用凹陷效果
- 进度条/滑块使用凸起效果
- 动画流畅且有弹性

**完整 CSS 实现**:
```css
/* 进度条容器 */
.clay-progress-container {
  width: 100%;
  height: 16px;
  border-radius: 12px;
  background: linear-gradient(145deg, #e8d8f0, #f0e5f5);

  /* 凹陷效果 */
  box-shadow:
    inset 2px 2px 6px rgba(200, 170, 220, 0.3),
    inset -2px -2px 6px rgba(255, 255, 255, 0.5);

  overflow: hidden;
  position: relative;
}

/* 进度条 */
.clay-progress-bar {
  height: 100%;
  border-radius: 12px;
  background: linear-gradient(145deg, #d4a5f3, #c48ee8);

  /* 凸起效果 */
  box-shadow:
    -2px -2px 6px rgba(255, 255, 255, 0.6),
    2px 2px 6px rgba(196, 142, 232, 0.4),
    inset -1px -1px 3px rgba(255, 255, 255, 0.2),
    inset 1px 1px 3px rgba(196, 142, 232, 0.3);

  transition: width 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* 滑块容器 */
.clay-slider-container {
  width: 100%;
  position: relative;
}

.clay-slider-track {
  width: 100%;
  height: 12px;
  border-radius: 10px;
  background: linear-gradient(145deg, #e8d8f0, #f0e5f5);
  box-shadow:
    inset 2px 2px 6px rgba(200, 170, 220, 0.3),
    inset -2px -2px 6px rgba(255, 255, 255, 0.5);
}

.clay-slider-thumb {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(145deg, #d4a5f3, #c48ee8);
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  cursor: grab;

  box-shadow:
    -4px -4px 10px rgba(255, 255, 255, 0.6),
    4px 4px 10px rgba(196, 142, 232, 0.4),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(196, 142, 232, 0.3);

  transition: all 0.2s ease;
}

.clay-slider-thumb:hover {
  transform: translate(-50%, -50%) scale(1.1);
  box-shadow:
    -5px -5px 12px rgba(255, 255, 255, 0.7),
    5px 5px 12px rgba(196, 142, 232, 0.5),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(196, 142, 232, 0.3);
}

.clay-slider-thumb:active {
  cursor: grabbing;
  transform: translate(-50%, -50%) scale(0.95);
}
```

## 完整 Tailwind 配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        clay: {
          pink: {
            50: '#ffc8dd',
            100: '#ffb3d9',
            200: '#ff99ac',
            300: '#ff8fb3',
            400: '#ff6a88',
          },
          blue: {
            50: '#cae9ff',
            100: '#a2d2ff',
            200: '#7eb8e0',
            300: '#5a9fd4',
          },
          purple: {
            50: '#e4c1f9',
            100: '#d4a5f3',
            200: '#c48ee8',
            300: '#b377dc',
          },
          green: {
            50: '#d8f3dc',
            100: '#b7e4c7',
            200: '#95d5b2',
            300: '#74c69d',
          },
        },
      },
      borderRadius: {
        'clay-sm': '16px',
        'clay': '24px',
        'clay-lg': '32px',
        'clay-xl': '48px',
        'clay-full': '50px',
      },
      boxShadow: {
        'clay': '-4px -4px 12px rgba(255, 255, 255, 0.6), 4px 4px 12px rgba(255, 143, 179, 0.4), inset -2px -2px 4px rgba(255, 255, 255, 0.2), inset 2px 2px 4px rgba(255, 143, 179, 0.3)',
        'clay-hover': '-6px -6px 16px rgba(255, 255, 255, 0.7), 6px 6px 16px rgba(255, 143, 179, 0.5), inset -2px -2px 4px rgba(255, 255, 255, 0.2), inset 2px 2px 4px rgba(255, 143, 179, 0.3)',
        'clay-active': '-2px -2px 8px rgba(255, 255, 255, 0.5), 2px 2px 8px rgba(255, 143, 179, 0.3), inset -3px -3px 6px rgba(255, 255, 255, 0.1), inset 3px 3px 6px rgba(255, 143, 179, 0.4)',
        'clay-inset': 'inset 3px 3px 8px rgba(200, 170, 220, 0.3), inset -3px -3px 8px rgba(255, 255, 255, 0.5)',
      },
    },
  },
};
```

## 间距系统

```css
/* 推荐间距 */
--clay-space-xs: 0.5rem;    /* 8px */
--clay-space-sm: 1rem;      /* 16px */
--clay-space-md: 1.5rem;    /* 24px */
--clay-space-lg: 2rem;      /* 32px */
--clay-space-xl: 3rem;      /* 48px */
--clay-space-2xl: 4rem;     /* 64px */

/* 内边距 */
--clay-padding-btn: 1rem 2rem;
--clay-padding-card: 2rem;
--clay-padding-input: 1rem 1.5rem;
--clay-padding-nav: 1rem 2rem;
```

## 字体系统

```css
/* 推荐字体 */
font-family: 'Rounded Mplus 1c', 'Nunito', 'Quicksand', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

/* 字重 */
--clay-font-regular: 400;
--clay-font-medium: 500;
--clay-font-semibold: 600;
--clay-font-bold: 700;
--clay-font-extrabold: 800;

/* 字体大小 */
--clay-text-xs: 0.75rem;    /* 12px */
--clay-text-sm: 0.875rem;   /* 14px */
--clay-text-base: 1rem;     /* 16px */
--clay-text-lg: 1.125rem;   /* 18px */
--clay-text-xl: 1.25rem;    /* 20px */
--clay-text-2xl: 1.5rem;    /* 24px */
--clay-text-3xl: 2rem;      /* 32px */
```

## 阴影强度系统

```css
/* 阴影等级 */
--clay-shadow-sm: -3px -3px 8px rgba(255, 255, 255, 0.6), 3px 3px 8px rgba(255, 143, 179, 0.3);
--clay-shadow-md: -4px -4px 12px rgba(255, 255, 255, 0.6), 4px 4px 12px rgba(255, 143, 179, 0.4);
--clay-shadow-lg: -6px -6px 16px rgba(255, 255, 255, 0.7), 6px 6px 16px rgba(255, 143, 179, 0.5);
--clay-shadow-xl: -8px -8px 20px rgba(255, 255, 255, 0.8), 8px 8px 20px rgba(255, 143, 179, 0.6);

/* 内阴影 */
--clay-inset-sm: inset -2px -2px 4px rgba(255, 255, 255, 0.2), inset 2px 2px 4px rgba(255, 143, 179, 0.3);
--clay-inset-md: inset -3px -3px 6px rgba(255, 255, 255, 0.3), inset 3px 3px 6px rgba(255, 143, 179, 0.4);
--clay-inset-lg: inset -4px -4px 8px rgba(255, 255, 255, 0.4), inset 4px 4px 8px rgba(255, 143, 179, 0.5);
```

## 重要事项（Important Notes）

1. **哑光表面**: Claymorphism 不应有强烈的高光反射,避免使用 `glossy` 效果
2. **双层阴影必须**: 外部阴影 + 内部阴影缺一不可,这是 claymorphism 的灵魂
3. **柔和过渡**: 所有交互动画使用 `cubic-bezier(0.34, 1.56, 0.64, 1)` 创造弹性效果
4. **色彩一致性**: 背景色与主体色应在同一色系内,仅明度不同
5. **可访问性**: 确保文字对比度达到 WCAG AA 标准（至少 4.5:1）
6. **性能**: 避免过度使用阴影,单个元素阴影层数不超过 4 层
7. **响应式**: 移动端适当减小圆角和阴影强度

## 禁止事项（Things to Avoid）

❌ **不要使用锐利边角**: 避免 `border-radius < 16px`
❌ **不要使用高饱和度**: 避免饱和度 > 70% 的鲜艳色彩
❌ **不要使用扁平阴影**: `box-shadow: 0 2px 4px` 这种标准阴影不适用
❌ **不要忘记内阴影**: 仅有外部阴影无法实现 claymorphism 效果
❌ **不要使用渐变边框**: Claymorphism 不需要边框,厚度由阴影创造
❌ **不要过度动画**: 避免复杂的 3D 旋转或变形动画
❌ **不要使用深色背景**: Claymorphism 在深色模式下效果较差,建议仅用于浅色主题

---

## English Version (en-US)

### Design Overview
Generate **Claymorphism** style interface design for products. This is an anti-flat 3D design style that creates soft, fluffy, and approachable digital experiences by simulating the texture of real-world clay or play-doh. Every UI element should look like a handmade clay object with noticeable thickness, rounded edges, and soft lighting.

## Core Design Requirements

### 1. Dual Shadow System (The Soul of Claymorphism)

**Drop Shadow - Creating Levitation**:
- Use two-layer drop shadows stacked
- First layer: Deep dark with large blur, simulating occlusion shadow
- Second layer: Light with medium blur, simulating ambient light reflection

**Inner Shadow - Creating Thickness**:
- Top: Light inner shadow, simulating top highlight
- Bottom: Dark inner shadow, simulating bottom occlusion
- Forms a "raised" 3D effect

**Complete CSS Implementation**:
```css
.clay-card {
  background: linear-gradient(145deg, #ffb3d9, #ff8fb3);
  border-radius: 32px;
  padding: 2rem;

  /* Drop shadow - dual layer */
  box-shadow:
    /* Main shadow - dark large range */
    -6px -6px 20px rgba(255, 255, 255, 0.7),
    6px 6px 20px rgba(255, 143, 179, 0.4),
    /* Inner shadow - simulate thickness */
    inset -3px -3px 8px rgba(255, 255, 255, 0.3),
    inset 3px 3px 8px rgba(255, 143, 179, 0.4);

  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.clay-card:hover {
  transform: translateY(-4px);

  /* Shadow diffuses on hover, enhancing levitation */
  box-shadow:
    -8px -8px 24px rgba(255, 255, 255, 0.8),
    8px 8px 24px rgba(255, 143, 179, 0.5),
    inset -3px -3px 8px rgba(255, 255, 255, 0.3),
    inset 3px 3px 8px rgba(255, 143, 179, 0.4);
}

.clay-card:active {
  transform: translateY(0);

  /* Shadow contracts on active, simulating pressed down */
  box-shadow:
    -3px -3px 10px rgba(255, 255, 255, 0.6),
    3px 3px 10px rgba(255, 143, 179, 0.3),
    /* Inner shadow deepens */
    inset -4px -4px 10px rgba(255, 255, 255, 0.2),
    inset 4px 4px 10px rgba(255, 143, 179, 0.5);
}
```

### 2. Extreme Roundness

**Border Radius Strategy**:
- Large cards/containers: `border-radius: 32px - 48px`
- Medium buttons: `border-radius: 24px - 32px`
- Small tags/badges: `border-radius: 16px - 24px`
- Icon containers: `border-radius: 50%` (perfect circle)
- Input fields: `border-radius: 20px - 28px`

**Complete CSS Implementation**:
```css
/* Large container */
.clay-container-large {
  border-radius: 48px;
  padding: 3rem;
}

/* Button component */
.clay-button {
  border-radius: 28px;
  padding: 1rem 2rem;
  font-size: 1rem;
  font-weight: 700;
  border: none;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Pill button */
.clay-button-pill {
  border-radius: 50px;
  padding: 0.875rem 2.5rem;
}

/* Circular icon wrapper */
.clay-icon-wrapper {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Input field */
.clay-input {
  border-radius: 24px;
  padding: 1rem 1.5rem;
  border: none;
  font-size: 1rem;
}

/* Tag */
.clay-tag {
  border-radius: 20px;
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  display: inline-block;
}
```

### 3. Macaron Color System

**Color Principles**:
- High Lightness (Lightness > 70%)
- Low Saturation (Saturation 40-60%)
- Soft tone variations
- Background colors in the same family as main colors but lighter

**Complete Color Scheme**:
```css
:root {
  /* Pink Family */
  --clay-pink-light: #ffc8dd;
  --clay-pink-main: #ffb3d9;
  --clay-pink-medium: #ff99ac;
  --clay-pink-dark: #ff8fb3;
  --clay-pink-deep: #ff6a88;

  /* Blue Family */
  --clay-blue-light: #cae9ff;
  --clay-blue-main: #a2d2ff;
  --clay-blue-medium: #7eb8e0;
  --clay-blue-dark: #5a9fd4;

  /* Purple Family */
  --clay-purple-light: #e4c1f9;
  --clay-purple-main: #d4a5f3;
  --clay-purple-medium: #c48ee8;
  --clay-purple-dark: #b377dc;

  /* Green Family */
  --clay-green-light: #d8f3dc;
  --clay-green-main: #b7e4c7;
  --clay-green-medium: #95d5b2;
  --clay-green-dark: #74c69d;

  /* Yellow Family */
  --clay-yellow-light: #fff4bd;
  --clay-yellow-main: #ffe6a7;
  --clay-yellow-medium: #ffd98e;
  --clay-yellow-dark: #ffcc77;

  /* Neutral */
  --clay-white: #ffffff;
  --clay-gray-light: #f8f9fa;
  --clay-gray-medium: #e9ecef;
  --clay-text-primary: #495057;
  --clay-text-secondary: #6c757d;

  /* Gradient backgrounds */
  --clay-gradient-warm: linear-gradient(135deg, #ffecd2 0%, #fcb69f 50%, #ffecd2 100%);
  --clay-gradient-cool: linear-gradient(135deg, #cae9ff 0%, #a2d2ff 50%, #cae9ff 100%);
  --clay-gradient-purple: linear-gradient(135deg, #e4c1f9 0%, #d4a5f3 50%, #e4c1f9 100%);
}
```

### 4. Button Design

**Physical Feedback**:
- Idle: Normal levitated state
- Hover: Slight lift + shadow diffusion
- Active: Pressed effect + shadow contraction + inner shadow deepening
- Use elastic animation curves

**Complete CSS Implementation**:
```css
/* Primary button */
.clay-btn-primary {
  background: linear-gradient(145deg, #ff99ac, #ff6a88);
  color: #ffffff;
  padding: 1rem 2rem;
  border-radius: 28px;
  border: none;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);

  /* Dual drop shadow + inner shadow */
  box-shadow:
    -4px -4px 12px rgba(255, 255, 255, 0.6),
    4px 4px 12px rgba(255, 106, 136, 0.4),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(255, 106, 136, 0.3);

  /* Elastic animation */
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.clay-btn-primary:hover {
  transform: translateY(-3px);
  box-shadow:
    -6px -6px 16px rgba(255, 255, 255, 0.7),
    6px 6px 16px rgba(255, 106, 136, 0.5),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(255, 106, 136, 0.3);
}

.clay-btn-primary:active {
  transform: translateY(0);
  box-shadow:
    -2px -2px 8px rgba(255, 255, 255, 0.5),
    2px 2px 8px rgba(255, 106, 136, 0.3),
    /* Inner shadow deepens, simulating flattening */
    inset -3px -3px 6px rgba(255, 255, 255, 0.1),
    inset 3px 3px 6px rgba(255, 106, 136, 0.4);
}

/* Secondary button */
.clay-btn-secondary {
  background: linear-gradient(145deg, #ffc8dd, #ffafcc);
  color: #ff6a88;
  padding: 1rem 2rem;
  border-radius: 28px;
  border: none;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow:
    -4px -4px 12px rgba(255, 255, 255, 0.6),
    4px 4px 12px rgba(255, 175, 204, 0.4),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(255, 175, 204, 0.3);
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Icon button */
.clay-btn-icon {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: linear-gradient(145deg, #ffb3d9, #ff8fb3);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow:
    -4px -4px 12px rgba(255, 255, 255, 0.6),
    4px 4px 12px rgba(255, 143, 179, 0.4),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(255, 143, 179, 0.3);
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

### 5. Input and Form Elements

**Inset Style**:
- Use inner shadows to create "scooped out" groove effect
- Background slightly darker than container
- Inner shadow deepens + outer glow on focus

**Complete CSS Implementation**:
```css
/* Text input */
.clay-input {
  width: 100%;
  padding: 1rem 1.5rem;
  border: none;
  border-radius: 24px;
  font-size: 1rem;
  font-weight: 500;
  color: #495057;

  /* Inset effect - reversed inner shadow */
  background: linear-gradient(145deg, #f0e5f5, #e8d8f0);
  box-shadow:
    inset 3px 3px 8px rgba(200, 170, 220, 0.3),
    inset -3px -3px 8px rgba(255, 255, 255, 0.5);

  transition: all 0.3s ease;
}

.clay-input:focus {
  outline: none;

  /* Inner shadow deepens + outer glow on focus */
  box-shadow:
    inset 4px 4px 10px rgba(200, 170, 220, 0.4),
    inset -4px -4px 10px rgba(255, 255, 255, 0.6),
    0 0 0 4px rgba(212, 165, 243, 0.2);
}

/* Checkbox */
.clay-checkbox-wrapper {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
}

.clay-checkbox {
  appearance: none;
  width: 28px;
  height: 28px;
  border-radius: 8px;
  background: linear-gradient(145deg, #ffc8dd, #ffafcc);
  box-shadow:
    -3px -3px 8px rgba(255, 255, 255, 0.6),
    3px 3px 8px rgba(255, 175, 204, 0.4),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(255, 175, 204, 0.3);
  cursor: pointer;
  position: relative;
  transition: all 0.3s ease;
}

.clay-checkbox:checked {
  background: linear-gradient(145deg, #ff99ac, #ff6a88);
  box-shadow:
    inset 3px 3px 8px rgba(255, 106, 136, 0.4),
    inset -3px -3px 8px rgba(255, 255, 255, 0.3);
}

.clay-checkbox:checked::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #ffffff;
  font-size: 16px;
  font-weight: 800;
}
```

### 6. Navigation Bar

**Design Features**:
- Fixed top or center floating
- Capsule shape
- Background more vibrant than page colors
- Logo and links use text shadows for depth

**Complete CSS Implementation**:
```css
/* Floating navigation bar */
.clay-nav {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  padding: 1rem 2rem;
  background: linear-gradient(145deg, #ffb3ba, #ff8fab);
  border-radius: 50px;
  box-shadow:
    -6px -6px 16px rgba(255, 255, 255, 0.6),
    6px 6px 16px rgba(255, 143, 171, 0.4),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(255, 143, 171, 0.3);
}

.clay-nav-content {
  display: flex;
  align-items: center;
  gap: 3rem;
}

.clay-logo {
  font-size: 1.5rem;
  font-weight: 800;
  color: #ffffff;
  text-decoration: none;

  /* Text shadow creates depth */
  text-shadow:
    2px 2px 4px rgba(255, 143, 171, 0.3),
    -1px -1px 2px rgba(255, 255, 255, 0.3);
}

.clay-nav-menu {
  display: flex;
  list-style: none;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.clay-nav-link {
  color: rgba(255, 255, 255, 0.85);
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.3s ease;
  text-shadow: 1px 1px 2px rgba(255, 143, 171, 0.2);
}

.clay-nav-link:hover,
.clay-nav-link.active {
  color: #ffffff;
  text-shadow:
    2px 2px 4px rgba(255, 143, 171, 0.4),
    -1px -1px 2px rgba(255, 255, 255, 0.4);
}
```

### 7. Progress and Slider

**Design Features**:
- Track uses inset effect
- Progress bar/slider uses raised effect
- Smooth and elastic animations

**Complete CSS Implementation**:
```css
/* Progress container */
.clay-progress-container {
  width: 100%;
  height: 16px;
  border-radius: 12px;
  background: linear-gradient(145deg, #e8d8f0, #f0e5f5);

  /* Inset effect */
  box-shadow:
    inset 2px 2px 6px rgba(200, 170, 220, 0.3),
    inset -2px -2px 6px rgba(255, 255, 255, 0.5);

  overflow: hidden;
  position: relative;
}

/* Progress bar */
.clay-progress-bar {
  height: 100%;
  border-radius: 12px;
  background: linear-gradient(145deg, #d4a5f3, #c48ee8);

  /* Raised effect */
  box-shadow:
    -2px -2px 6px rgba(255, 255, 255, 0.6),
    2px 2px 6px rgba(196, 142, 232, 0.4),
    inset -1px -1px 3px rgba(255, 255, 255, 0.2),
    inset 1px 1px 3px rgba(196, 142, 232, 0.3);

  transition: width 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Slider container */
.clay-slider-container {
  width: 100%;
  position: relative;
}

.clay-slider-track {
  width: 100%;
  height: 12px;
  border-radius: 10px;
  background: linear-gradient(145deg, #e8d8f0, #f0e5f5);
  box-shadow:
    inset 2px 2px 6px rgba(200, 170, 220, 0.3),
    inset -2px -2px 6px rgba(255, 255, 255, 0.5);
}

.clay-slider-thumb {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(145deg, #d4a5f3, #c48ee8);
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  cursor: grab;

  box-shadow:
    -4px -4px 10px rgba(255, 255, 255, 0.6),
    4px 4px 10px rgba(196, 142, 232, 0.4),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(196, 142, 232, 0.3);

  transition: all 0.2s ease;
}

.clay-slider-thumb:hover {
  transform: translate(-50%, -50%) scale(1.1);
  box-shadow:
    -5px -5px 12px rgba(255, 255, 255, 0.7),
    5px 5px 12px rgba(196, 142, 232, 0.5),
    inset -2px -2px 4px rgba(255, 255, 255, 0.2),
    inset 2px 2px 4px rgba(196, 142, 232, 0.3);
}

.clay-slider-thumb:active {
  cursor: grabbing;
  transform: translate(-50%, -50%) scale(0.95);
}
```

## Complete Tailwind Configuration

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        clay: {
          pink: {
            50: '#ffc8dd',
            100: '#ffb3d9',
            200: '#ff99ac',
            300: '#ff8fb3',
            400: '#ff6a88',
          },
          blue: {
            50: '#cae9ff',
            100: '#a2d2ff',
            200: '#7eb8e0',
            300: '#5a9fd4',
          },
          purple: {
            50: '#e4c1f9',
            100: '#d4a5f3',
            200: '#c48ee8',
            300: '#b377dc',
          },
          green: {
            50: '#d8f3dc',
            100: '#b7e4c7',
            200: '#95d5b2',
            300: '#74c69d',
          },
        },
      },
      borderRadius: {
        'clay-sm': '16px',
        'clay': '24px',
        'clay-lg': '32px',
        'clay-xl': '48px',
        'clay-full': '50px',
      },
      boxShadow: {
        'clay': '-4px -4px 12px rgba(255, 255, 255, 0.6), 4px 4px 12px rgba(255, 143, 179, 0.4), inset -2px -2px 4px rgba(255, 255, 255, 0.2), inset 2px 2px 4px rgba(255, 143, 179, 0.3)',
        'clay-hover': '-6px -6px 16px rgba(255, 255, 255, 0.7), 6px 6px 16px rgba(255, 143, 179, 0.5), inset -2px -2px 4px rgba(255, 255, 255, 0.2), inset 2px 2px 4px rgba(255, 143, 179, 0.3)',
        'clay-active': '-2px -2px 8px rgba(255, 255, 255, 0.5), 2px 2px 8px rgba(255, 143, 179, 0.3), inset -3px -3px 6px rgba(255, 255, 255, 0.1), inset 3px 3px 6px rgba(255, 143, 179, 0.4)',
        'clay-inset': 'inset 3px 3px 8px rgba(200, 170, 220, 0.3), inset -3px -3px 8px rgba(255, 255, 255, 0.5)',
      },
    },
  },
};
```

## Spacing System

```css
/* Recommended spacing */
--clay-space-xs: 0.5rem;    /* 8px */
--clay-space-sm: 1rem;      /* 16px */
--clay-space-md: 1.5rem;    /* 24px */
--clay-space-lg: 2rem;      /* 32px */
--clay-space-xl: 3rem;      /* 48px */
--clay-space-2xl: 4rem;     /* 64px */

/* Padding */
--clay-padding-btn: 1rem 2rem;
--clay-padding-card: 2rem;
--clay-padding-input: 1rem 1.5rem;
--clay-padding-nav: 1rem 2rem;
```

## Typography System

```css
/* Recommended fonts */
font-family: 'Rounded Mplus 1c', 'Nunito', 'Quicksand', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

/* Font weights */
--clay-font-regular: 400;
--clay-font-medium: 500;
--clay-font-semibold: 600;
--clay-font-bold: 700;
--clay-font-extrabold: 800;

/* Font sizes */
--clay-text-xs: 0.75rem;    /* 12px */
--clay-text-sm: 0.875rem;   /* 14px */
--clay-text-base: 1rem;     /* 16px */
--clay-text-lg: 1.125rem;   /* 18px */
--clay-text-xl: 1.25rem;    /* 20px */
--clay-text-2xl: 1.5rem;    /* 24px */
--clay-text-3xl: 2rem;      /* 32px */
```

## Shadow Intensity System

```css
/* Shadow levels */
--clay-shadow-sm: -3px -3px 8px rgba(255, 255, 255, 0.6), 3px 3px 8px rgba(255, 143, 179, 0.3);
--clay-shadow-md: -4px -4px 12px rgba(255, 255, 255, 0.6), 4px 4px 12px rgba(255, 143, 179, 0.4);
--clay-shadow-lg: -6px -6px 16px rgba(255, 255, 255, 0.7), 6px 6px 16px rgba(255, 143, 179, 0.5);
--clay-shadow-xl: -8px -8px 20px rgba(255, 255, 255, 0.8), 8px 8px 20px rgba(255, 143, 179, 0.6);

/* Inner shadows */
--clay-inset-sm: inset -2px -2px 4px rgba(255, 255, 255, 0.2), inset 2px 2px 4px rgba(255, 143, 179, 0.3);
--clay-inset-md: inset -3px -3px 6px rgba(255, 255, 255, 0.3), inset 3px 3px 6px rgba(255, 143, 179, 0.4);
--clay-inset-lg: inset -4px -4px 8px rgba(255, 255, 255, 0.4), inset 4px 4px 8px rgba(255, 143, 179, 0.5);
```

## Important Notes

1. **Matte Surface**: Claymorphism should not have harsh specular highlights, avoid `glossy` effects
2. **Dual Shadows Required**: Drop shadow + inner shadow are both essential, this is the soul of claymorphism
3. **Soft Transitions**: Use `cubic-bezier(0.34, 1.56, 0.64, 1)` for elastic effects in all interactions
4. **Color Consistency**: Background and main colors should be in the same family, differing only in lightness
5. **Accessibility**: Ensure text contrast meets WCAG AA standard (at least 4.5:1)
6. **Performance**: Avoid excessive shadows, max 4 shadow layers per element
7. **Responsive**: Reduce border radius and shadow intensity on mobile

## Things to Avoid

❌ **Don't use sharp edges**: Avoid `border-radius < 16px`
❌ **Don't use high saturation**: Avoid colors with saturation > 70%
❌ **Don't use flat shadows**: Standard shadows like `box-shadow: 0 2px 4px` don't work
❌ **Don't forget inner shadows**: Drop shadow alone cannot achieve claymorphism effect
❌ **Don't use gradient borders**: Claymorphism doesn't need borders, thickness is created by shadows
❌ **Don't overdo animations**: Avoid complex 3D rotations or deformation animations
❌ **Don't use dark backgrounds**: Claymorphism works poorly in dark mode, recommend light themes only
