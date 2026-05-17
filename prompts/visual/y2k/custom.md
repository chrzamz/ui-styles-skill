# Custom Prompt: Y2K（千禧年风格）

## 中文版本 (zh-CN)

### 1. 设计哲学与核心原则

**Y2K（Year 2000）风格**是千禧年前后（1998-2004）流行的视觉美学，融合了**未来主义幻想、数字乐观主义和早期互联网文化**。这种风格以**镀铬金属质感、玻璃态透明、霓虹发光、像素字体和太空元素**为特征，表达了人类对新千年科技未来的憧憬。

**设计原则**：
- **数字乐观主义**：科技是酷炫的、友好的、充满希望的
- **玻璃态质感**：半透明、模糊背景、光泽反射
- **镀铬金属**：银色、彩虹色渐变、液态金属效果
- **霓虹发光**：青色、粉色、紫色的柔和光晕
- **太空主题**：星星、气泡、光束、全息效果

### 2. 核心设计要求

#### 2.1 玻璃态配色系统（Glassmorphic Color Palette）

Y2K 的配色系统以**高明度、中低饱和度**的未来感色彩为主，营造清新、科技、乐观的视觉氛围。

**主色调（Primary Colors）**：
- **青色（Cyan）**：`#06b6d4` - 主要强调色、按钮
- **天蓝（Sky Blue）**：`#0ea5e9` - 次要强调色
- **紫罗兰（Violet）**：`#8b5cf6` - 点缀色、装饰
- **粉红（Pink）**：`#ec4899` - 警示色、高亮

**浅色调（Light Tones）**：
- **冰蓝（Ice Blue）**：`#e0f2fe`
- **淡青（Light Cyan）**：`#cffafe`
- **薰衣草浅（Light Lavender）**：`#ede9fe`
- **淡粉（Light Pink）**：`#fce7f3`

**金属色（Metallic Colors）**：
- **银色（Silver）**：`#e5e7eb` - 边框、文字
- **镀铬渐变（Chrome Gradient）**：`linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- **彩虹金属（Rainbow Metal）**：`linear-gradient(135deg, #667eea, #764ba2, #f093fb, #4facfe)`

**中性色（Neutral Colors）**：
- **深灰文本（Text Dark）**：`#334155` - 主文本
- **中灰文本（Text Medium）**：`#64748b` - 次要文本
- **白色透明（White Alpha）**：`rgba(255, 255, 255, 0.7)` - 玻璃背景
- **纯白（Pure White）**：`#ffffff` - 高亮

**完整 CSS 变量定义**：
```css
:root {
  /* 主色调 */
  --y2k-cyan: #06b6d4;
  --y2k-sky: #0ea5e9;
  --y2k-violet: #8b5cf6;
  --y2k-pink: #ec4899;

  /* 浅色调 */
  --y2k-ice-blue: #e0f2fe;
  --y2k-light-cyan: #cffafe;
  --y2k-light-lavender: #ede9fe;
  --y2k-light-pink: #fce7f3;

  /* 金属色 */
  --y2k-silver: #e5e7eb;
  --y2k-chrome: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --y2k-rainbow: linear-gradient(135deg, #667eea, #764ba2, #f093fb, #4facfe);

  /* 中性色 */
  --y2k-text-dark: #334155;
  --y2k-text-medium: #64748b;
  --y2k-text-light: #94a3b8;
  --y2k-white: #ffffff;
  --y2k-white-alpha-70: rgba(255, 255, 255, 0.7);
  --y2k-white-alpha-50: rgba(255, 255, 255, 0.5);
  --y2k-white-alpha-30: rgba(255, 255, 255, 0.3);

  /* 玻璃态阴影 */
  --y2k-shadow-glass:
    0 8px 32px rgba(0, 0, 0, 0.05),
    inset 0 -2px 8px rgba(0, 0, 0, 0.02),
    inset 0 2px 8px rgba(255, 255, 255, 0.4);

  --y2k-shadow-glow-cyan:
    0 0 20px rgba(6, 182, 212, 0.3),
    0 0 40px rgba(6, 182, 212, 0.15);

  --y2k-shadow-glow-violet:
    0 0 20px rgba(139, 92, 246, 0.3),
    0 0 40px rgba(139, 92, 246, 0.15);

  /* 圆角 */
  --y2k-radius-sm: 12px;
  --y2k-radius-md: 20px;
  --y2k-radius-lg: 24px;
  --y2k-radius-full: 9999px;

  /* 模糊程度 */
  --y2k-blur-sm: 10px;
  --y2k-blur-md: 20px;
  --y2k-blur-lg: 40px;
}
```

#### 2.2 玻璃态效果系统（Glassmorphism System）

Y2K 风格的核心是**玻璃态设计**，通过 `backdrop-filter` 和多层阴影模拟玻璃的透明、模糊和光泽效果。

**标准玻璃卡片**：
```css
.y2k-glass-card {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: var(--y2k-radius-md);
  padding: 2rem;
  box-shadow: var(--y2k-shadow-glass);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.y2k-glass-card:hover {
  transform: translateY(-4px);
  box-shadow:
    0 12px 48px rgba(0, 0, 0, 0.08),
    inset 0 -2px 8px rgba(0, 0, 0, 0.02),
    inset 0 2px 8px rgba(255, 255, 255, 0.4);
}
```

**强化玻璃效果（更透明）**：
```css
.y2k-glass-intense {
  background: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(40px);
  -webkit-backdrop-filter: blur(40px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--y2k-radius-lg);
  box-shadow:
    0 8px 32px rgba(0, 0, 0, 0.04),
    inset 0 -4px 12px rgba(0, 0, 0, 0.03),
    inset 0 4px 12px rgba(255, 255, 255, 0.5);
}
```

**渐变边框玻璃卡片**：
```css
.y2k-glass-gradient-border {
  position: relative;
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(20px);
  border-radius: var(--y2k-radius-md);
  padding: 2rem;
  overflow: hidden;
}

.y2k-glass-gradient-border::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--y2k-radius-md);
  padding: 1px;
  background: var(--y2k-rainbow);
  -webkit-mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
}
```

**玻璃按钮**：
```css
.y2k-glass-button {
  padding: 0.75rem 2rem;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(10px);
  color: var(--y2k-cyan);
  font-weight: 600;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: var(--y2k-radius-full);
  cursor: pointer;
  box-shadow:
    0 4px 16px rgba(0, 0, 0, 0.05),
    inset 0 -2px 6px rgba(0, 0, 0, 0.02),
    inset 0 2px 6px rgba(255, 255, 255, 0.4);
  transition: all 0.3s ease;
}

.y2k-glass-button:hover {
  background: rgba(255, 255, 255, 0.8);
  transform: translateY(-2px);
  box-shadow:
    0 8px 24px rgba(0, 0, 0, 0.08),
    inset 0 -2px 6px rgba(0, 0, 0, 0.02),
    inset 0 2px 6px rgba(255, 255, 255, 0.4);
}
```

#### 2.3 镀铬渐变系统（Chrome Gradient System）

Y2K 的另一核心是**镀铬金属效果**，使用彩虹色渐变模拟液态金属的光泽。

**标准镀铬渐变**：
```css
.y2k-chrome-gradient {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 900;
}
```

**彩虹镀铬（多色渐变）**：
```css
.y2k-rainbow-chrome {
  background: linear-gradient(
    135deg,
    #667eea 0%,
    #764ba2 25%,
    #f093fb 50%,
    #4facfe 75%,
    #00f2fe 100%
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 900;
  animation: y2k-shimmer 3s linear infinite;
  background-size: 200% 200%;
}

@keyframes y2k-shimmer {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
```

**镀铬按钮（实心背景）**：
```css
.y2k-chrome-button {
  padding: 0.875rem 2.5rem;
  background: var(--y2k-chrome);
  color: white;
  font-weight: 700;
  border: none;
  border-radius: var(--y2k-radius-full);
  cursor: pointer;
  box-shadow:
    0 4px 16px rgba(102, 126, 234, 0.4),
    inset 0 -2px 8px rgba(0, 0, 0, 0.15),
    inset 0 2px 8px rgba(255, 255, 255, 0.3);
  transition: all 0.3s ease;
}

.y2k-chrome-button:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow:
    0 8px 32px rgba(102, 126, 234, 0.5),
    inset 0 -2px 8px rgba(0, 0, 0, 0.15),
    inset 0 2px 8px rgba(255, 255, 255, 0.3);
}

.y2k-chrome-button:active {
  transform: translateY(-1px) scale(0.98);
}
```

**金属边框**：
```css
.y2k-chrome-border {
  position: relative;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: var(--y2k-radius-md);
}

.y2k-chrome-border::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--y2k-radius-md);
  padding: 2px;
  background: var(--y2k-rainbow);
  -webkit-mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
}
```

#### 2.4 霓虹发光系统（Neon Glow System）

Y2K 风格使用**柔和的霓虹发光效果**，而非赛博朋克的强烈霓虹。

**青色发光**：
```css
.y2k-glow-cyan {
  box-shadow:
    0 0 20px rgba(6, 182, 212, 0.3),
    0 0 40px rgba(6, 182, 212, 0.15),
    0 4px 16px rgba(6, 182, 212, 0.2);
}

.y2k-glow-cyan:hover {
  box-shadow:
    0 0 30px rgba(6, 182, 212, 0.4),
    0 0 60px rgba(6, 182, 212, 0.2),
    0 8px 24px rgba(6, 182, 212, 0.3);
}
```

**紫色发光**：
```css
.y2k-glow-violet {
  box-shadow:
    0 0 20px rgba(139, 92, 246, 0.3),
    0 0 40px rgba(139, 92, 246, 0.15),
    0 4px 16px rgba(139, 92, 246, 0.2);
}
```

**发光文字**：
```css
.y2k-text-glow-cyan {
  color: var(--y2k-cyan);
  text-shadow:
    0 0 10px rgba(6, 182, 212, 0.5),
    0 0 20px rgba(6, 182, 212, 0.3),
    0 0 30px rgba(6, 182, 212, 0.15);
}

.y2k-text-glow-pink {
  color: var(--y2k-pink);
  text-shadow:
    0 0 10px rgba(236, 72, 153, 0.5),
    0 0 20px rgba(236, 72, 153, 0.3),
    0 0 30px rgba(236, 72, 153, 0.15);
}
```

**发光边框**：
```css
.y2k-border-glow {
  border: 2px solid rgba(6, 182, 212, 0.5);
  box-shadow:
    0 0 15px rgba(6, 182, 212, 0.2),
    inset 0 0 15px rgba(6, 182, 212, 0.1);
}
```

#### 2.5 气泡装饰系统（Bubble Decoration System）

Y2K 风格大量使用**半透明气泡**作为背景装饰，营造太空、水下的梦幻感。

**基础气泡**：
```css
.y2k-bubble {
  position: absolute;
  background: linear-gradient(
    135deg,
    rgba(6, 182, 212, 0.2) 0%,
    rgba(59, 130, 246, 0.15) 50%,
    rgba(16, 185, 129, 0.2) 100%
  );
  border-radius: 50%;
  backdrop-filter: blur(20px);
  border: 2px solid rgba(255, 255, 255, 0.4);
  box-shadow:
    0 8px 32px rgba(6, 182, 212, 0.15),
    inset 0 -4px 12px rgba(0, 0, 0, 0.05),
    inset 4px 4px 12px rgba(255, 255, 255, 0.5);
  animation: y2k-float 6s ease-in-out infinite;
  pointer-events: none;
}

@keyframes y2k-float {
  0%, 100% {
    transform: translateY(0) scale(1);
  }
  50% {
    transform: translateY(-20px) scale(1.05);
  }
}
```

**气泡尺寸变体**：
```css
.y2k-bubble-sm {
  width: 80px;
  height: 80px;
}

.y2k-bubble-md {
  width: 150px;
  height: 150px;
}

.y2k-bubble-lg {
  width: 250px;
  height: 250px;
}

.y2k-bubble-xl {
  width: 400px;
  height: 400px;
}
```

**多气泡布局示例**：
```css
.y2k-bubble-container {
  position: absolute;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
}

.y2k-bubble-1 {
  top: 10%;
  left: 5%;
  animation-delay: 0s;
}

.y2k-bubble-2 {
  top: 60%;
  left: 80%;
  animation-delay: 2s;
}

.y2k-bubble-3 {
  bottom: 10%;
  left: 50%;
  animation-delay: 4s;
}
```

#### 2.6 按钮系统（Button System）

Y2K 按钮结合**玻璃态、镀铬和发光效果**，营造未来感交互体验。

**主要按钮（青色渐变）**：
```css
.y2k-btn-primary {
  padding: 0.875rem 2.5rem;
  background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
  color: white;
  font-weight: 700;
  border: none;
  border-radius: var(--y2k-radius-full);
  cursor: pointer;
  box-shadow:
    0 4px 16px rgba(6, 182, 212, 0.3),
    inset 0 -2px 8px rgba(0, 0, 0, 0.1),
    inset 0 2px 8px rgba(255, 255, 255, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.y2k-btn-primary:hover {
  transform: translateY(-2px);
  box-shadow:
    0 8px 24px rgba(6, 182, 212, 0.4),
    0 0 20px rgba(6, 182, 212, 0.2),
    inset 0 -2px 8px rgba(0, 0, 0, 0.1),
    inset 0 2px 8px rgba(255, 255, 255, 0.3);
}

.y2k-btn-primary:active {
  transform: translateY(0);
  box-shadow:
    0 2px 8px rgba(6, 182, 212, 0.3),
    inset 0 -2px 8px rgba(0, 0, 0, 0.1),
    inset 0 2px 8px rgba(255, 255, 255, 0.3);
}
```

**次要按钮（玻璃态）**：
```css
.y2k-btn-secondary {
  padding: 0.875rem 2.5rem;
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  color: var(--y2k-cyan);
  font-weight: 700;
  border: 2px solid rgba(6, 182, 212, 0.3);
  border-radius: var(--y2k-radius-full);
  cursor: pointer;
  box-shadow:
    0 4px 12px rgba(0, 0, 0, 0.05),
    inset 0 -2px 6px rgba(0, 0, 0, 0.02),
    inset 0 2px 6px rgba(255, 255, 255, 0.4);
  transition: all 0.3s ease;
}

.y2k-btn-secondary:hover {
  background: rgba(255, 255, 255, 0.9);
  border-color: rgba(6, 182, 212, 0.5);
  transform: translateY(-2px);
  box-shadow:
    0 8px 20px rgba(0, 0, 0, 0.08),
    inset 0 -2px 6px rgba(0, 0, 0, 0.02),
    inset 0 2px 6px rgba(255, 255, 255, 0.4);
}
```

**镀铬按钮**：
```css
.y2k-btn-chrome {
  padding: 0.875rem 2.5rem;
  background: var(--y2k-rainbow);
  color: white;
  font-weight: 700;
  border: none;
  border-radius: var(--y2k-radius-full);
  cursor: pointer;
  box-shadow:
    0 4px 20px rgba(102, 126, 234, 0.4),
    inset 0 -2px 8px rgba(0, 0, 0, 0.15),
    inset 0 2px 8px rgba(255, 255, 255, 0.3);
  transition: all 0.3s ease;
  animation: y2k-shimmer 3s linear infinite;
  background-size: 200% 200%;
}

.y2k-btn-chrome:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow:
    0 8px 32px rgba(102, 126, 234, 0.5),
    0 0 25px rgba(102, 126, 234, 0.3),
    inset 0 -2px 8px rgba(0, 0, 0, 0.15),
    inset 0 2px 8px rgba(255, 255, 255, 0.3);
}
```

**图标按钮**：
```css
.y2k-btn-icon {
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  cursor: pointer;
  box-shadow:
    0 4px 12px rgba(0, 0, 0, 0.05),
    inset 0 -2px 6px rgba(0, 0, 0, 0.02),
    inset 0 2px 6px rgba(255, 255, 255, 0.4);
  transition: all 0.3s ease;
}

.y2k-btn-icon:hover {
  background: rgba(255, 255, 255, 0.9);
  transform: scale(1.1);
  box-shadow:
    0 6px 16px rgba(0, 0, 0, 0.08),
    inset 0 -2px 6px rgba(0, 0, 0, 0.02),
    inset 0 2px 6px rgba(255, 255, 255, 0.4);
}
```

#### 2.7 导航系统（Navigation System）

Y2K 导航使用**玻璃态背景、柔和阴影和流畅过渡**。

```css
.y2k-nav {
  position: sticky;
  top: 0;
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  z-index: 1000;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.y2k-nav-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.y2k-nav-logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-weight: 800;
  font-size: 1.5rem;
  background: var(--y2k-rainbow);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.y2k-nav-links {
  display: flex;
  gap: 2rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.y2k-nav-link {
  position: relative;
  color: var(--y2k-text-dark);
  text-decoration: none;
  font-weight: 600;
  padding: 0.5rem 1rem;
  border-radius: var(--y2k-radius-sm);
  transition: all 0.3s ease;
}

.y2k-nav-link:hover {
  color: var(--y2k-cyan);
  background: rgba(6, 182, 212, 0.1);
  transform: translateY(-2px);
}

.y2k-nav-link.active {
  color: var(--y2k-cyan);
  background: rgba(6, 182, 212, 0.15);
  box-shadow:
    0 0 15px rgba(6, 182, 212, 0.2),
    inset 0 0 10px rgba(6, 182, 212, 0.1);
}

.y2k-nav-link.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 2px;
  background: var(--y2k-cyan);
  border-radius: 2px;
  box-shadow: 0 0 8px rgba(6, 182, 212, 0.5);
}
```

#### 2.8 表单系统（Form System）

Y2K 表单元素使用**玻璃态输入框、发光边框和流畅反馈**。

```css
/* 文本输入框 */
.y2k-input {
  width: 100%;
  padding: 0.875rem 1.5rem;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: var(--y2k-radius-md);
  color: var(--y2k-text-dark);
  font-size: 1rem;
  box-shadow:
    0 2px 8px rgba(0, 0, 0, 0.03),
    inset 0 -1px 4px rgba(0, 0, 0, 0.02),
    inset 0 1px 4px rgba(255, 255, 255, 0.3);
  transition: all 0.3s ease;
}

.y2k-input::placeholder {
  color: var(--y2k-text-light);
}

.y2k-input:focus {
  outline: none;
  background: rgba(255, 255, 255, 0.8);
  border-color: rgba(6, 182, 212, 0.5);
  box-shadow:
    0 0 0 3px rgba(6, 182, 212, 0.1),
    0 4px 12px rgba(0, 0, 0, 0.05),
    inset 0 -1px 4px rgba(0, 0, 0, 0.02),
    inset 0 1px 4px rgba(255, 255, 255, 0.3);
}

/* 文本域 */
.y2k-textarea {
  width: 100%;
  min-height: 120px;
  padding: 1rem 1.5rem;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: var(--y2k-radius-md);
  color: var(--y2k-text-dark);
  font-size: 1rem;
  resize: vertical;
  transition: all 0.3s ease;
}

/* 复选框（自定义样式） */
.y2k-checkbox {
  appearance: none;
  width: 24px;
  height: 24px;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(10px);
  border: 2px solid rgba(6, 182, 212, 0.3);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  transition: all 0.3s ease;
}

.y2k-checkbox:checked {
  background: linear-gradient(135deg, #06b6d4, #0891b2);
  border-color: #06b6d4;
  box-shadow: 0 0 15px rgba(6, 182, 212, 0.3);
}

.y2k-checkbox:checked::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 14px;
  font-weight: bold;
}

/* 开关按钮 */
.y2k-switch {
  position: relative;
  width: 60px;
  height: 32px;
  background: rgba(226, 232, 240, 0.6);
  backdrop-filter: blur(10px);
  border-radius: var(--y2k-radius-full);
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.y2k-switch::after {
  content: '';
  position: absolute;
  top: 3px;
  left: 3px;
  width: 24px;
  height: 24px;
  background: white;
  border-radius: 50%;
  box-shadow:
    0 2px 8px rgba(0, 0, 0, 0.1),
    inset 0 -1px 3px rgba(0, 0, 0, 0.05),
    inset 0 1px 3px rgba(255, 255, 255, 0.5);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.y2k-switch.active {
  background: linear-gradient(135deg, #06b6d4, #0891b2);
  border-color: #06b6d4;
  box-shadow: 0 0 15px rgba(6, 182, 212, 0.2);
}

.y2k-switch.active::after {
  left: calc(100% - 27px);
}
```

### 3. Tailwind CSS 配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        y2k: {
          cyan: '#06b6d4',
          sky: '#0ea5e9',
          violet: '#8b5cf6',
          pink: '#ec4899',
          'ice-blue': '#e0f2fe',
          'light-cyan': '#cffafe',
          'light-lavender': '#ede9fe',
          'light-pink': '#fce7f3',
          silver: '#e5e7eb',
        },
      },
      borderRadius: {
        'y2k-sm': '12px',
        'y2k-md': '20px',
        'y2k-lg': '24px',
      },
      backdropBlur: {
        'y2k-sm': '10px',
        'y2k-md': '20px',
        'y2k-lg': '40px',
      },
      boxShadow: {
        'y2k-glass':
          '0 8px 32px rgba(0, 0, 0, 0.05), inset 0 -2px 8px rgba(0, 0, 0, 0.02), inset 0 2px 8px rgba(255, 255, 255, 0.4)',
        'y2k-glow-cyan':
          '0 0 20px rgba(6, 182, 212, 0.3), 0 0 40px rgba(6, 182, 212, 0.15)',
        'y2k-glow-violet':
          '0 0 20px rgba(139, 92, 246, 0.3), 0 0 40px rgba(139, 92, 246, 0.15)',
      },
      animation: {
        'y2k-float': 'y2kFloat 6s ease-in-out infinite',
        'y2k-shimmer': 'y2kShimmer 3s linear infinite',
      },
      keyframes: {
        y2kFloat: {
          '0%, 100%': { transform: 'translateY(0) scale(1)' },
          '50%': { transform: 'translateY(-20px) scale(1.05)' },
        },
        y2kShimmer: {
          '0%': { backgroundPosition: '0% 50%' },
          '50%': { backgroundPosition: '100% 50%' },
          '100%': { backgroundPosition: '0% 50%' },
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
<section class="relative min-h-screen bg-gradient-to-br from-cyan-50 via-blue-50 to-violet-50 overflow-hidden">
  <!-- 背景气泡装饰 -->
  <div class="absolute inset-0 overflow-hidden pointer-events-none">
    <div class="y2k-bubble y2k-bubble-lg absolute top-[10%] left-[5%]"></div>
    <div class="y2k-bubble y2k-bubble-md absolute top-[60%] right-[10%]" style="animation-delay: 2s"></div>
    <div class="y2k-bubble y2k-bubble-xl absolute bottom-[10%] left-[50%]" style="animation-delay: 4s"></div>
  </div>

  <!-- 主内容 -->
  <div class="relative z-10 max-w-6xl mx-auto px-8 py-20 text-center">
    <h1 class="text-7xl font-black mb-6 y2k-rainbow-chrome">
      Welcome to Y2K
    </h1>
    <p class="text-2xl text-slate-700 mb-12 max-w-3xl mx-auto">
      Experience the future of design with glassmorphic interfaces and chrome gradients
    </p>
    <div class="flex gap-6 justify-center flex-wrap">
      <button class="y2k-btn-primary">
        Get Started
      </button>
      <button class="y2k-btn-secondary">
        Learn More
      </button>
      <button class="y2k-btn-chrome">
        Try Demo
      </button>
    </div>
  </div>
</section>

<!-- 卡片网格 -->
<section class="py-20 px-8 bg-white">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-5xl font-black text-center mb-16 y2k-chrome-gradient">
      Our Features
    </h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="y2k-glass-card y2k-glow-cyan">
        <div class="text-6xl mb-4">✨</div>
        <h3 class="text-2xl font-bold text-slate-800 mb-3">Glassmorphism</h3>
        <p class="text-slate-600">
          Beautiful frosted glass effects with backdrop blur and transparency
        </p>
      </div>
      <div class="y2k-glass-card y2k-glow-violet">
        <div class="text-6xl mb-4">🌈</div>
        <h3 class="text-2xl font-bold text-slate-800 mb-3">Chrome Gradients</h3>
        <p class="text-slate-600">
          Liquid metal effects with rainbow color transitions
        </p>
      </div>
      <div class="y2k-glass-card">
        <div class="text-6xl mb-4">💫</div>
        <h3 class="text-2xl font-bold text-slate-800 mb-3">Neon Glow</h3>
        <p class="text-slate-600">
          Soft glowing effects that bring your UI to life
        </p>
      </div>
    </div>
  </div>
</section>
```


---

## English Version (en-US)

### 1. Design Philosophy & Core Principles

**Y2K (Year 2000) style** is a visual aesthetic popular around the millennium (1998-2004), blending **futuristic fantasy, digital optimism, and early internet culture**. This style is characterized by **chrome metallic textures, glass transparency, neon glows, pixel fonts, and space elements**, expressing humanity's aspirations for a technological future in the new millennium.

**Design Principles**:
- **Digital Optimism**: Technology is cool, friendly, and hopeful
- **Glassmorphism**: Semi-transparent, blurred backgrounds, glossy reflections
- **Chrome Metal**: Silver, rainbow gradients, liquid metal effects
- **Neon Glow**: Soft cyan, pink, and purple halos
- **Space Theme**: Stars, bubbles, light beams, holographic effects

### 2. Core Design Requirements

#### 2.1 Glassmorphic Color Palette System

The Y2K color system features **high-brightness, medium-to-low saturation** futuristic colors, creating a fresh, tech-forward, optimistic visual atmosphere.

**Primary Colors**:
- **Cyan**: `#06b6d4` - Primary emphasis, buttons
- **Sky Blue**: `#0ea5e9` - Secondary emphasis
- **Violet**: `#8b5cf6` - Accent, decoration
- **Pink**: `#ec4899` - Alerts, highlights

**Light Tones**:
- **Ice Blue**: `#e0f2fe`
- **Light Cyan**: `#cffafe`
- **Light Lavender**: `#ede9fe`
- **Light Pink**: `#fce7f3`

**Metallic Colors**:
- **Silver**: `#e5e7eb` - Borders, text
- **Chrome Gradient**: `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- **Rainbow Metal**: `linear-gradient(135deg, #667eea, #764ba2, #f093fb, #4facfe)`

**Complete CSS Variables**:
```css
:root {
  /* Primary Colors */
  --y2k-cyan: #06b6d4;
  --y2k-sky: #0ea5e9;
  --y2k-violet: #8b5cf6;
  --y2k-pink: #ec4899;

  /* Light Tones */
  --y2k-ice-blue: #e0f2fe;
  --y2k-light-cyan: #cffafe;
  --y2k-light-lavender: #ede9fe;
  --y2k-light-pink: #fce7f3;

  /* Metallic Colors */
  --y2k-silver: #e5e7eb;
  --y2k-chrome: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --y2k-rainbow: linear-gradient(135deg, #667eea, #764ba2, #f093fb, #4facfe);

  /* Shadows */
  --y2k-shadow-glass:
    0 8px 32px rgba(0, 0, 0, 0.05),
    inset 0 -2px 8px rgba(0, 0, 0, 0.02),
    inset 0 2px 8px rgba(255, 255, 255, 0.4);

  --y2k-shadow-glow-cyan:
    0 0 20px rgba(6, 182, 212, 0.3),
    0 0 40px rgba(6, 182, 212, 0.15);

  /* Border Radius */
  --y2k-radius-sm: 12px;
  --y2k-radius-md: 20px;
  --y2k-radius-lg: 24px;
  --y2k-radius-full: 9999px;

  /* Blur Levels */
  --y2k-blur-sm: 10px;
  --y2k-blur-md: 20px;
  --y2k-blur-lg: 40px;
}
```

### 3. Tailwind CSS Configuration

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        y2k: {
          cyan: '#06b6d4',
          sky: '#0ea5e9',
          violet: '#8b5cf6',
          pink: '#ec4899',
          'ice-blue': '#e0f2fe',
          'light-cyan': '#cffafe',
          silver: '#e5e7eb',
        },
      },
      borderRadius: {
        'y2k-sm': '12px',
        'y2k-md': '20px',
        'y2k-lg': '24px',
      },
      backdropBlur: {
        'y2k-sm': '10px',
        'y2k-md': '20px',
        'y2k-lg': '40px',
      },
      boxShadow: {
        'y2k-glass':
          '0 8px 32px rgba(0, 0, 0, 0.05), inset 0 -2px 8px rgba(0, 0, 0, 0.02), inset 0 2px 8px rgba(255, 255, 255, 0.4)',
        'y2k-glow-cyan':
          '0 0 20px rgba(6, 182, 212, 0.3), 0 0 40px rgba(6, 182, 212, 0.15)',
      },
      animation: {
        'y2k-float': 'y2kFloat 6s ease-in-out infinite',
        'y2k-shimmer': 'y2kShimmer 3s linear infinite',
      },
      keyframes: {
        y2kFloat: {
          '0%, 100%': { transform: 'translateY(0) scale(1)' },
          '50%': { transform: 'translateY(-20px) scale(1.05)' },
        },
        y2kShimmer: {
          '0%': { backgroundPosition: '0% 50%' },
          '50%': { backgroundPosition: '100% 50%' },
          '100%': { backgroundPosition: '0% 50%' },
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
<section class="relative min-h-screen bg-gradient-to-br from-cyan-50 via-blue-50 to-violet-50 overflow-hidden">
  <!-- Background bubble decorations -->
  <div class="absolute inset-0 overflow-hidden pointer-events-none">
    <div class="y2k-bubble y2k-bubble-lg absolute top-[10%] left-[5%]"></div>
    <div class="y2k-bubble y2k-bubble-md absolute top-[60%] right-[10%]" style="animation-delay: 2s"></div>
  </div>

  <!-- Main content -->
  <div class="relative z-10 max-w-6xl mx-auto px-8 py-20 text-center">
    <h1 class="text-7xl font-black mb-6 y2k-rainbow-chrome">
      Welcome to Y2K
    </h1>
    <p class="text-2xl text-slate-700 mb-12">
      Experience the future with glassmorphic design
    </p>
    <div class="flex gap-6 justify-center">
      <button class="y2k-btn-primary">Get Started</button>
      <button class="y2k-btn-secondary">Learn More</button>
    </div>
  </div>
</section>
```

**Advanced Y2K Design Techniques**

**Metallic & Chrome Effects**:
- Create realistic chrome using multi-stop gradients with sharp transitions
- Implement reflection effects using linear gradients at specific angles (135deg, 45deg)
- Use CSS filters (brightness, contrast) to enhance metallic appearance
- Apply subtle animations to simulate light reflecting off chrome surfaces
- Combine multiple gradient layers for complex metallic textures

**Futuristic UI Elements**:
- Design rounded buttons with glossy overlays using linear-gradient and inset shadows
- Create bubble-like elements with radial gradients and border-radius
- Implement translucent panels using rgba backgrounds with backdrop-filter blur
- Add digital/LCD-style counters and displays using monospace fonts
- Design futuristic progress bars with animated gradient fills

**Interactive Animations**:
- Implement hover effects with smooth color transitions (300-500ms)
- Add pulsing animations for call-to-action elements using keyframe animations
- Create bouncy interactions using cubic-bezier easing curves
- Apply entrance animations (slide-in, fade-in, scale-in) with staggered timing
- Use rotation and perspective transforms for 3D card flip effects

**Typography for Y2K**:
- Mix chunky display fonts (Impact, Bebas Neue) with futuristic sans-serif
- Apply text effects: outlines, shadows, gradients for dimensional text
- Use all-caps for emphasis and futuristic feel
- Implement animated text effects: gradient sweep, color cycling
- Maintain readability despite decorative effects (ensure 4.5:1 contrast minimum)

**Layout Patterns**:
- Create asymmetric grid layouts with overlapping elements
- Use rounded containers (border-radius: 24-40px) throughout
- Implement card-based designs with glossy overlays
- Add decorative geometric shapes as background elements
- Create visual hierarchy through size, color, and layering

**Performance Optimization**:
- Limit complex gradients and filters to key elements only
- Use CSS transforms instead of position changes for animations
- Implement intersection observer to animate only visible elements
- Optimize gradient definitions to use fewer color stops when possible
- Consider reducing effects on mobile devices for better performance

**Browser Compatibility**:
- Provide fallbacks for backdrop-filter (not supported in older browsers)
- Test chrome gradients across browsers as rendering may vary
- Use vendor prefixes for experimental CSS properties
- Ensure animations work smoothly in Safari, Chrome, and Firefox
- Provide static alternatives for browsers with limited CSS support
