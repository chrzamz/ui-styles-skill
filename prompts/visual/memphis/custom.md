# Custom Prompt: Memphis Design（孟菲斯设计）

## 中文版本 (zh-CN)

### 1. 设计哲学与核心原则

**Memphis Design（孟菲斯设计）**诞生于 1980 年代的意大利，是一场反对现代主义极简美学的设计运动。这种风格以**狂野的几何形状、高饱和撞色、大胆的图形对比和反功能主义态度**为特征，旨在打破传统设计规则，创造充满活力、趣味和反叛精神的视觉体验。

**设计原则**：
- **反极简主义**：拥抱视觉噪点，拒绝"少即是多"
- **几何狂欢**：大量使用圆形、三角形、方形、波浪线等基本几何元素
- **撞色美学**：高饱和对比色自由组合，无视传统配色规则
- **图形优先**：形状本身即内容，装饰性图形与功能性内容同等重要
- **复古未来感**：80 年代 MTV、霓虹灯、电子游戏厅的视觉语言

### 2. 核心设计要求

#### 2.1 孟菲斯配色系统（Memphis Color Palette）

Memphis 的配色系统以**极端饱和度、强烈对比度**为核心，模拟 80 年代电子显示器和印刷海报的视觉冲击力。

**主色调（Primary Colors）**：
- **亮黄（Bright Yellow）**：`#FFD700` - 背景主色、强调色
- **品红（Magenta）**：`#FF00FF` - 标题、图形
- **青色（Cyan）**：`#00FFFF` - 背景、装饰
- **亮红（Bright Red）**：`#FF0000` - 按钮、强调
- **纯黑（Pure Black）**：`#000000` - 边框、文字、阴影
- **纯白（Pure White）**：`#FFFFFF` - 背景、对比

**次要色（Secondary Colors）**：
- **亮绿（Lime Green）**：`#00FF00`
- **橙色（Orange）**：`#FF8C00`
- **蓝色（Blue）**：`#0000FF`
- **粉红（Pink）**：`#FFB6C1`

**配色规则**：
```css
/* Memphis 配色不遵循传统和谐理论，而是追求最大视觉冲击 */

/* 彩虹渐变导航栏 */
background: linear-gradient(90deg, #FFD700 0%, #FF00FF 50%, #00FFFF 100%);

/* 对比撞色背景 */
background: #FFD700; /* 亮黄 */
color: #000000; /* 纯黑 */

/* 三色条纹装饰 */
background: repeating-linear-gradient(
  90deg,
  #FFD700 0px, #FFD700 20px,
  #000000 20px, #000000 22px,
  #FF00FF 22px, #FF00FF 42px,
  #000000 42px, #000000 44px
);
```

**完整 CSS 变量定义**：
```css
:root {
  /* 主色调 */
  --memphis-yellow: #FFD700;
  --memphis-magenta: #FF00FF;
  --memphis-cyan: #00FFFF;
  --memphis-red: #FF0000;
  --memphis-black: #000000;
  --memphis-white: #FFFFFF;

  /* 次要色 */
  --memphis-lime: #00FF00;
  --memphis-orange: #FF8C00;
  --memphis-blue: #0000FF;
  --memphis-pink: #FFB6C1;

  /* 边框粗细 */
  --memphis-border-thin: 3px;
  --memphis-border-medium: 4px;
  --memphis-border-thick: 6px;
  --memphis-border-ultra: 8px;

  /* 硬阴影 */
  --memphis-shadow-sm: 3px 3px 0 var(--memphis-black);
  --memphis-shadow-md: 5px 5px 0 var(--memphis-black);
  --memphis-shadow-lg: 7px 7px 0 var(--memphis-black);
  --memphis-shadow-xl: 10px 10px 0 var(--memphis-black);

  /* 字体 */
  --memphis-font: 'Arial Black', 'Arial', 'Helvetica Neue', sans-serif;
}
```

#### 2.2 几何形状系统（Geometric Shape System）

Memphis 的灵魂在于**基本几何形状的自由组合**，每个形状都带有**粗黑边框**和**随机倾斜角度**。

**基础形状**：

```css
/* 圆形（Circle） */
.memphis-circle {
  width: 150px;
  height: 150px;
  background-color: var(--memphis-yellow);
  border: 6px solid var(--memphis-black);
  border-radius: 50%;
  position: absolute;
  animation: memphisFloat 6s ease-in-out infinite;
}

/* 方形（Square） */
.memphis-square {
  width: 150px;
  height: 150px;
  background-color: var(--memphis-red);
  border: 6px solid var(--memphis-black);
  transform: rotate(25deg);
  box-shadow: var(--memphis-shadow-lg);
  position: absolute;
}

/* 三角形（Triangle） */
.memphis-triangle {
  width: 0;
  height: 0;
  border-left: 80px solid transparent;
  border-right: 80px solid transparent;
  border-bottom: 140px solid var(--memphis-magenta);
  position: absolute;
  transform: rotate(-20deg);
  filter: drop-shadow(6px 6px 0 var(--memphis-black));
}

/* 菱形（Diamond） */
.memphis-diamond {
  width: 120px;
  height: 120px;
  background-color: var(--memphis-cyan);
  border: 5px solid var(--memphis-black);
  transform: rotate(45deg);
  box-shadow: var(--memphis-shadow-md);
  position: absolute;
}

/* 半圆（Semicircle） */
.memphis-semicircle {
  width: 100px;
  height: 50px;
  background-color: var(--memphis-orange);
  border: 4px solid var(--memphis-black);
  border-radius: 100px 100px 0 0;
  border-bottom: none;
  position: absolute;
}

/* 波浪线（Wavy Line） */
.memphis-wave {
  width: 200px;
  height: 50px;
  background-image: url("data:image/svg+xml,%3Csvg width='200' height='50' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 25 Q 25 0, 50 25 T 100 25 T 150 25 T 200 25' stroke='%23000000' stroke-width='5' fill='none'/%3E%3C/svg%3E");
  position: absolute;
}

/* 锯齿线（Zigzag） */
.memphis-zigzag {
  width: 200px;
  height: 4px;
  background: repeating-linear-gradient(
    90deg,
    var(--memphis-black) 0px, var(--memphis-black) 10px,
    transparent 10px, transparent 20px
  );
  position: absolute;
}

/* 圆点阵列（Dot Pattern） */
.memphis-dots {
  width: 300px;
  height: 50px;
  background-image: radial-gradient(
    circle,
    var(--memphis-black) 4px,
    transparent 4px
  );
  background-size: 20px 20px;
  position: absolute;
}
```

**浮动动画**：
```css
@keyframes memphisFloat {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-30px) rotate(10deg);
  }
}

@keyframes memphisRotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@keyframes memphisShake {
  0%, 100% {
    transform: translateX(0);
  }
  25% {
    transform: translateX(-5px) rotate(-2deg);
  }
  75% {
    transform: translateX(5px) rotate(2deg);
  }
}
```

#### 2.3 粗黑边框系统（Bold Black Border System）

Memphis 的所有元素都必须带有**极粗的纯黑边框**，这是风格的视觉锚点。

```css
/* 标准边框 */
.memphis-border-standard {
  border: 4px solid var(--memphis-black);
}

/* 超粗边框 */
.memphis-border-thick {
  border: 8px solid var(--memphis-black);
}

/* 不对称边框（制造手绘感） */
.memphis-border-asymmetric {
  border-top: 6px solid var(--memphis-black);
  border-right: 4px solid var(--memphis-black);
  border-bottom: 8px solid var(--memphis-black);
  border-left: 5px solid var(--memphis-black);
}

/* 双层边框 */
.memphis-border-double {
  border: 4px solid var(--memphis-black);
  outline: 4px solid var(--memphis-yellow);
  outline-offset: 4px;
}

/* 虚线边框（模拟手绘） */
.memphis-border-dashed {
  border: 4px dashed var(--memphis-black);
}
```

#### 2.4 硬阴影系统（Hard Shadow System）

Memphis 使用**无模糊的硬边阴影**（`box-shadow` 不带 blur），创造强烈的图层感。

```css
/* 小阴影 */
.memphis-shadow-sm {
  box-shadow: 3px 3px 0 var(--memphis-black);
}

/* 中阴影 */
.memphis-shadow-md {
  box-shadow: 5px 5px 0 var(--memphis-black);
}

/* 大阴影 */
.memphis-shadow-lg {
  box-shadow: 7px 7px 0 var(--memphis-black);
}

/* 超大阴影 */
.memphis-shadow-xl {
  box-shadow: 10px 10px 0 var(--memphis-black);
}

/* 彩色阴影（制造 3D 效果） */
.memphis-shadow-color {
  box-shadow:
    4px 4px 0 var(--memphis-magenta),
    8px 8px 0 var(--memphis-cyan),
    12px 12px 0 var(--memphis-black);
}

/* 反向阴影（左上角） */
.memphis-shadow-reverse {
  box-shadow: -5px -5px 0 var(--memphis-black);
}

/* 多方向阴影 */
.memphis-shadow-multi {
  box-shadow:
    5px 5px 0 var(--memphis-black),
    -5px -5px 0 var(--memphis-yellow);
}
```

#### 2.5 夸张字体系统（Exaggerated Typography）

Memphis 的文字必须**粗壮、倾斜、带多重阴影**，模拟 80 年代海报字体。

```css
/* 超粗标题 */
.memphis-title-hero {
  font-family: var(--memphis-font);
  font-size: 120px;
  font-weight: 900;
  line-height: 1;
  color: var(--memphis-yellow);
  text-shadow:
    6px 6px 0 var(--memphis-black),
    -3px -3px 0 var(--memphis-magenta);
  transform: rotate(-3deg);
}

/* 主标题 */
.memphis-title-main {
  font-family: var(--memphis-font);
  font-size: 60px;
  font-weight: 900;
  color: var(--memphis-red);
  text-shadow:
    4px 4px 0 var(--memphis-black),
    -2px -2px 0 var(--memphis-white);
  transform: rotate(2deg);
}

/* 次标题 */
.memphis-title-sub {
  font-family: var(--memphis-font);
  font-size: 36px;
  font-weight: 900;
  color: var(--memphis-black);
  text-shadow:
    3px 3px 0 var(--memphis-yellow),
    -2px -2px 0 var(--memphis-cyan);
  transform: skew(-5deg);
}

/* 强调文字 */
.memphis-text-accent {
  font-size: 48px;
  font-weight: 900;
  color: var(--memphis-magenta);
  text-shadow: 4px 4px 0 var(--memphis-black);
  animation: memphisPulse 2s infinite;
}

/* 正文文字 */
.memphis-text-body {
  font-family: var(--memphis-font);
  font-size: 18px;
  font-weight: 900;
  color: var(--memphis-black);
  text-transform: uppercase;
  letter-spacing: 2px;
}

/* 脉动动画 */
@keyframes memphisPulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
}
```

#### 2.6 按钮系统（Button System）

Memphis 按钮必须**大胆、倾斜、带硬阴影**，悬停时产生**强烈的空间位移**。

```css
/* 主按钮 */
.memphis-btn-primary {
  padding: 16px 40px;
  font-family: var(--memphis-font);
  font-size: 18px;
  font-weight: 900;
  text-transform: uppercase;
  color: var(--memphis-white);
  background-color: var(--memphis-red);
  border: 4px solid var(--memphis-black);
  cursor: pointer;
  transform: rotate(-3deg);
  box-shadow: 5px 5px 0 var(--memphis-black);
  transition: all 0.3s ease;
}

.memphis-btn-primary:hover {
  background-color: var(--memphis-magenta);
  transform: rotate(-3deg) translateY(-3px);
  box-shadow: 7px 7px 0 var(--memphis-black);
}

.memphis-btn-primary:active {
  transform: rotate(-3deg) translateY(0);
  box-shadow: 3px 3px 0 var(--memphis-black);
}

/* 次要按钮 */
.memphis-btn-secondary {
  padding: 14px 35px;
  font-family: var(--memphis-font);
  font-size: 16px;
  font-weight: 900;
  text-transform: uppercase;
  color: var(--memphis-black);
  background-color: var(--memphis-yellow);
  border: 3px solid var(--memphis-black);
  cursor: pointer;
  transform: skew(-10deg);
  box-shadow: 4px 4px 0 var(--memphis-black);
  transition: all 0.3s ease;
}

.memphis-btn-secondary:hover {
  background-color: var(--memphis-cyan);
  transform: skew(-10deg) translateY(-2px);
  box-shadow: 6px 6px 0 var(--memphis-black);
}

/* 轮廓按钮 */
.memphis-btn-outline {
  padding: 14px 35px;
  font-family: var(--memphis-font);
  font-size: 16px;
  font-weight: 900;
  text-transform: uppercase;
  color: var(--memphis-black);
  background-color: var(--memphis-white);
  border: 4px solid var(--memphis-black);
  cursor: pointer;
  transform: rotate(2deg);
  box-shadow: 4px 4px 0 var(--memphis-black);
  transition: all 0.3s ease;
}

.memphis-btn-outline:hover {
  background-color: var(--memphis-yellow);
  transform: rotate(2deg) translateX(-3px) translateY(-3px);
  box-shadow: 7px 7px 0 var(--memphis-black);
}

/* 图标按钮 */
.memphis-btn-icon {
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--memphis-magenta);
  border: 4px solid var(--memphis-black);
  border-radius: 50%;
  cursor: pointer;
  transform: rotate(15deg);
  box-shadow: 4px 4px 0 var(--memphis-black);
  transition: all 0.3s ease;
}

.memphis-btn-icon:hover {
  background-color: var(--memphis-cyan);
  transform: rotate(15deg) scale(1.1);
  box-shadow: 6px 6px 0 var(--memphis-black);
}
```

#### 2.7 卡片系统（Card System）

Memphis 卡片使用**倾斜布局、撞色背景、粗边框和几何装饰**。

```css
/* 基础卡片 */
.memphis-card {
  position: relative;
  background-color: var(--memphis-white);
  border: 5px solid var(--memphis-black);
  padding: 30px;
  transform: rotate(-2deg);
  box-shadow: 8px 8px 0 var(--memphis-black);
  overflow: hidden;
  transition: all 0.3s ease;
}

.memphis-card:hover {
  transform: rotate(-2deg) translateY(-5px);
  box-shadow: 12px 12px 0 var(--memphis-black);
}

/* 卡片装饰圆点 */
.memphis-card::before {
  content: '';
  position: absolute;
  top: 10px;
  right: 10px;
  width: 30px;
  height: 30px;
  background-color: var(--memphis-yellow);
  border: 3px solid var(--memphis-black);
  border-radius: 50%;
}

/* 卡片装饰三角 */
.memphis-card::after {
  content: '';
  position: absolute;
  bottom: 10px;
  left: 10px;
  width: 0;
  height: 0;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
  border-bottom: 35px solid var(--memphis-magenta);
  filter: drop-shadow(2px 2px 0 var(--memphis-black));
}

/* 彩色背景卡片 */
.memphis-card-color {
  background: linear-gradient(135deg, var(--memphis-cyan) 0%, var(--memphis-yellow) 100%);
  border: 6px solid var(--memphis-black);
  padding: 35px;
  transform: rotate(1deg);
  box-shadow: 10px 10px 0 var(--memphis-black);
}

/* 条纹背景卡片 */
.memphis-card-striped {
  background: repeating-linear-gradient(
    45deg,
    var(--memphis-yellow),
    var(--memphis-yellow) 10px,
    var(--memphis-magenta) 10px,
    var(--memphis-magenta) 20px
  );
  border: 6px solid var(--memphis-black);
  padding: 35px;
  transform: skew(-3deg);
}

/* 卡片标题 */
.memphis-card-title {
  font-family: var(--memphis-font);
  font-size: 32px;
  font-weight: 900;
  color: var(--memphis-black);
  text-transform: uppercase;
  margin-bottom: 15px;
  text-shadow: 2px 2px 0 var(--memphis-yellow);
}

/* 卡片内容 */
.memphis-card-content {
  font-family: Arial, sans-serif;
  font-size: 16px;
  font-weight: 700;
  color: var(--memphis-black);
  line-height: 1.6;
}
```

#### 2.8 导航系统（Navigation System）

Memphis 导航栏使用**彩虹渐变背景、倾斜链接和条纹装饰**。

```css
/* 导航栏 */
.memphis-nav {
  position: sticky;
  top: 0;
  background: linear-gradient(90deg,
    var(--memphis-yellow) 0%,
    var(--memphis-magenta) 50%,
    var(--memphis-cyan) 100%
  );
  border-bottom: 8px solid var(--memphis-black);
  z-index: 1000;
  padding: 20px 0;
}

/* 导航容器 */
.memphis-nav-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Logo */
.memphis-logo {
  display: flex;
  align-items: center;
  gap: 15px;
}

/* Logo 图形 */
.memphis-logo-shape {
  width: 50px;
  height: 50px;
  background-color: var(--memphis-red);
  border: 4px solid var(--memphis-black);
  transform: rotate(45deg);
  box-shadow: 4px 4px 0 var(--memphis-black);
}

/* Logo 文字 */
.memphis-logo-text {
  font-family: var(--memphis-font);
  font-size: 24px;
  font-weight: 900;
  color: var(--memphis-black);
  text-shadow: 3px 3px 0 var(--memphis-white);
}

/* 导航链接容器 */
.memphis-nav-links {
  display: flex;
  gap: 30px;
}

/* 导航链接 */
.memphis-nav-link {
  font-family: var(--memphis-font);
  font-size: 16px;
  font-weight: 900;
  color: var(--memphis-black);
  text-decoration: none;
  text-transform: uppercase;
  padding: 10px 20px;
  border: 3px solid var(--memphis-black);
  background-color: var(--memphis-white);
  transform: skew(-10deg);
  transition: all 0.3s ease;
}

.memphis-nav-link:hover {
  background-color: var(--memphis-yellow);
  transform: skew(-10deg) translateY(-2px);
  box-shadow: 3px 3px 0 var(--memphis-black);
}

/* 导航按钮 */
.memphis-nav-btn {
  padding: 12px 30px;
  font-family: var(--memphis-font);
  font-size: 16px;
  font-weight: 900;
  text-transform: uppercase;
  color: var(--memphis-white);
  background-color: var(--memphis-red);
  border: 4px solid var(--memphis-black);
  cursor: pointer;
  transform: rotate(-3deg);
  box-shadow: 5px 5px 0 var(--memphis-black);
  transition: all 0.3s ease;
}

.memphis-nav-btn:hover {
  background-color: var(--memphis-magenta);
  transform: rotate(-3deg) translateY(-3px);
  box-shadow: 7px 7px 0 var(--memphis-black);
}

/* 导航装饰条纹 */
.memphis-nav-decoration {
  height: 8px;
  background: repeating-linear-gradient(
    90deg,
    var(--memphis-yellow) 0px, var(--memphis-yellow) 20px,
    var(--memphis-black) 20px, var(--memphis-black) 22px,
    var(--memphis-magenta) 22px, var(--memphis-magenta) 42px,
    var(--memphis-black) 42px, var(--memphis-black) 44px
  );
}
```

### 3. Tailwind CSS 配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        memphis: {
          yellow: '#FFD700',
          magenta: '#FF00FF',
          cyan: '#00FFFF',
          red: '#FF0000',
          black: '#000000',
          white: '#FFFFFF',
          lime: '#00FF00',
          orange: '#FF8C00',
          blue: '#0000FF',
          pink: '#FFB6C1',
        },
      },
      fontFamily: {
        memphis: ['Arial Black', 'Arial', 'Helvetica Neue', 'sans-serif'],
      },
      boxShadow: {
        'memphis-sm': '3px 3px 0 #000000',
        'memphis-md': '5px 5px 0 #000000',
        'memphis-lg': '7px 7px 0 #000000',
        'memphis-xl': '10px 10px 0 #000000',
        'memphis-color': '4px 4px 0 #FF00FF, 8px 8px 0 #00FFFF, 12px 12px 0 #000000',
      },
      borderWidth: {
        'memphis': '4px',
        'memphis-thick': '6px',
        'memphis-ultra': '8px',
      },
      animation: {
        'memphis-float': 'memphisFloat 6s ease-in-out infinite',
        'memphis-pulse': 'memphisPulse 2s infinite',
        'memphis-shake': 'memphisShake 1s infinite',
        'memphis-rotate': 'memphisRotate 10s linear infinite',
      },
      keyframes: {
        memphisFloat: {
          '0%, 100%': { transform: 'translateY(0) rotate(0deg)' },
          '50%': { transform: 'translateY(-30px) rotate(10deg)' },
        },
        memphisPulse: {
          '0%, 100%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(1.1)' },
        },
        memphisShake: {
          '0%, 100%': { transform: 'translateX(0)' },
          '25%': { transform: 'translateX(-5px) rotate(-2deg)' },
          '75%': { transform: 'translateX(5px) rotate(2deg)' },
        },
        memphisRotate: {
          from: { transform: 'rotate(0deg)' },
          to: { transform: 'rotate(360deg)' },
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
<section class="relative min-h-screen bg-memphis-cyan overflow-hidden py-20">
  <!-- 背景几何装饰 -->
  <div class="absolute inset-0 overflow-hidden">
    <div class="memphis-circle absolute top-[10%] left-[5%]"></div>
    <div class="memphis-square absolute bottom-[15%] left-[15%]"></div>
    <div class="memphis-triangle absolute top-[20%] right-[10%]"></div>
    <div class="memphis-dots absolute bottom-[10%] left-[50%]"></div>
  </div>

  <!-- 主内容 -->
  <div class="relative z-10 text-center px-8">
    <div class="memphis-title-hero mb-8">
      MEMPHIS
    </div>
    <div class="memphis-title-main mb-12">
      80s DESIGN REVOLUTION
    </div>
    <p class="memphis-text-body max-w-2xl mx-auto mb-12">
      BOLD SHAPES • BRIGHT COLORS • PURE ENERGY
    </p>
    <div class="flex gap-6 justify-center flex-wrap">
      <button class="memphis-btn-primary">
        GET STARTED
      </button>
      <button class="memphis-btn-secondary">
        LEARN MORE
      </button>
    </div>
  </div>
</section>

<!-- 卡片网格 -->
<section class="py-20 px-8 bg-memphis-white">
  <div class="max-w-6xl mx-auto">
    <h2 class="memphis-title-main text-center mb-16">
      OUR FEATURES
    </h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
      <div class="memphis-card">
        <h3 class="memphis-card-title">WILD</h3>
        <p class="memphis-card-content">
          Break all the rules with bold geometric shapes and crazy colors.
        </p>
      </div>
      <div class="memphis-card-color">
        <h3 class="memphis-card-title">LOUD</h3>
        <p class="memphis-card-content">
          Turn up the volume with high-saturation palette and strong contrast.
        </p>
      </div>
      <div class="memphis-card-striped">
        <h3 class="memphis-card-title">FUN</h3>
        <p class="memphis-card-content">
          Celebrate the playful spirit of 80s pop culture and MTV aesthetics.
        </p>
      </div>
    </div>
  </div>
</section>
```


---

## English Version (en-US)

### 1. Design Philosophy & Core Principles

**Memphis Design** emerged in 1980s Italy as a rebellious movement against modernist minimalism. This style is characterized by **wild geometric shapes, high-saturation color clashes, bold graphic contrasts, and an anti-functionalist attitude**, aiming to break traditional design rules and create vibrant, playful, and rebellious visual experiences.

**Design Principles**:
- **Anti-Minimalism**: Embrace visual noise, reject "less is more"
- **Geometric Carnival**: Extensive use of circles, triangles, squares, and wavy lines
- **Color Clashes**: High-saturation contrasting colors freely combined
- **Graphics First**: Shapes themselves are content; decorative graphics equal functional content
- **Retro Futurism**: 80s MTV, neon lights, and arcade visual language

### 2. Core Design Requirements

#### 2.1 Memphis Color Palette System

The Memphis color system centers on **extreme saturation and strong contrasts**, simulating the visual impact of 80s electronic displays and printed posters.

**Primary Colors**:
- **Bright Yellow**: `#FFD700` - Background, emphasis
- **Magenta**: `#FF00FF` - Titles, graphics
- **Cyan**: `#00FFFF` - Backgrounds, decoration
- **Bright Red**: `#FF0000` - Buttons, emphasis
- **Pure Black**: `#000000` - Borders, text, shadows
- **Pure White**: `#FFFFFF` - Backgrounds, contrast

**Secondary Colors**:
- **Lime Green**: `#00FF00`
- **Orange**: `#FF8C00`
- **Blue**: `#0000FF`
- **Pink**: `#FFB6C1`

**Color Rules**:
```css
/* Memphis colors don't follow traditional harmony; they pursue maximum visual impact */

/* Rainbow gradient navigation */
background: linear-gradient(90deg, #FFD700 0%, #FF00FF 50%, #00FFFF 100%);

/* Contrasting background */
background: #FFD700; /* Bright yellow */
color: #000000; /* Pure black */

/* Three-color stripe decoration */
background: repeating-linear-gradient(
  90deg,
  #FFD700 0px, #FFD700 20px,
  #000000 20px, #000000 22px,
  #FF00FF 22px, #FF00FF 42px,
  #000000 42px, #000000 44px
);
```

**Complete CSS Variables**:
```css
:root {
  /* Primary Colors */
  --memphis-yellow: #FFD700;
  --memphis-magenta: #FF00FF;
  --memphis-cyan: #00FFFF;
  --memphis-red: #FF0000;
  --memphis-black: #000000;
  --memphis-white: #FFFFFF;

  /* Secondary Colors */
  --memphis-lime: #00FF00;
  --memphis-orange: #FF8C00;
  --memphis-blue: #0000FF;
  --memphis-pink: #FFB6C1;

  /* Border Widths */
  --memphis-border-thin: 3px;
  --memphis-border-medium: 4px;
  --memphis-border-thick: 6px;
  --memphis-border-ultra: 8px;

  /* Hard Shadows */
  --memphis-shadow-sm: 3px 3px 0 var(--memphis-black);
  --memphis-shadow-md: 5px 5px 0 var(--memphis-black);
  --memphis-shadow-lg: 7px 7px 0 var(--memphis-black);
  --memphis-shadow-xl: 10px 10px 0 var(--memphis-black);

  /* Font */
  --memphis-font: 'Arial Black', 'Arial', 'Helvetica Neue', sans-serif;
}
```

### 3. Tailwind CSS Configuration

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        memphis: {
          yellow: '#FFD700',
          magenta: '#FF00FF',
          cyan: '#00FFFF',
          red: '#FF0000',
          black: '#000000',
          white: '#FFFFFF',
          lime: '#00FF00',
          orange: '#FF8C00',
          blue: '#0000FF',
          pink: '#FFB6C1',
        },
      },
      fontFamily: {
        memphis: ['Arial Black', 'Arial', 'Helvetica Neue', 'sans-serif'],
      },
      boxShadow: {
        'memphis-sm': '3px 3px 0 #000000',
        'memphis-md': '5px 5px 0 #000000',
        'memphis-lg': '7px 7px 0 #000000',
        'memphis-xl': '10px 10px 0 #000000',
      },
      borderWidth: {
        'memphis': '4px',
        'memphis-thick': '6px',
        'memphis-ultra': '8px',
      },
      animation: {
        'memphis-float': 'memphisFloat 6s ease-in-out infinite',
        'memphis-pulse': 'memphisPulse 2s infinite',
      },
      keyframes: {
        memphisFloat: {
          '0%, 100%': { transform: 'translateY(0) rotate(0deg)' },
          '50%': { transform: 'translateY(-30px) rotate(10deg)' },
        },
        memphisPulse: {
          '0%, 100%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(1.1)' },
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
<section class="relative min-h-screen bg-memphis-cyan overflow-hidden py-20">
  <!-- Background geometric decorations -->
  <div class="absolute inset-0 overflow-hidden">
    <div class="memphis-circle absolute top-[10%] left-[5%]"></div>
    <div class="memphis-square absolute bottom-[15%] left-[15%]"></div>
    <div class="memphis-triangle absolute top-[20%] right-[10%]"></div>
  </div>

  <!-- Main content -->
  <div class="relative z-10 text-center px-8">
    <div class="memphis-title-hero mb-8">
      MEMPHIS
    </div>
    <div class="memphis-title-main mb-12">
      80s DESIGN REVOLUTION
    </div>
    <div class="flex gap-6 justify-center">
      <button class="memphis-btn-primary">
        GET STARTED
      </button>
      <button class="memphis-btn-secondary">
        LEARN MORE
      </button>
    </div>
  </div>
</section>
```

**Advanced Design Techniques**

**Geometric Pattern Systems**:
- Create reusable pattern components using CSS shapes and clip-path
- Implement pattern variations by rotating and scaling base shapes
- Use CSS grid to create structured pattern layouts with controlled randomness
- Apply patterns as background layers with controlled opacity (15-35%)
- Consider using SVG patterns for more complex shapes and better scaling

**Color Harmony Strategies**:
- Establish a primary color (e.g., hot pink #ff006e) and derive complementary colors
- Use color theory: split-complementary, triadic, or tetradic schemes
- Maintain consistent color temperature (warm Memphis vs cool Memphis variants)
- Apply 80-20 rule: 80% neutral space, 20% bold colors for impact
- Test color combinations against white, black, and gray backgrounds

**Layering & Depth**:
- Use z-index strategically to create visual hierarchy (shapes: 1, content: 10, overlays: 20)
- Implement drop shadows with offset but no blur for flat aesthetic
- Stack geometric shapes at different angles for dynamic composition
- Create depth through color contrast rather than gradients or shadows
- Position patterns and shapes to frame important content

**Typography in Memphis Style**:
- Mix geometric sans-serif (Futura, Montserrat) with playful display fonts
- Use bold weights (700-900) for headlines to compete with geometric shapes
- Apply uppercase for emphasis and to match geometric aesthetic
- Implement text as shapes: outline text, rotated text, text on paths
- Maintain readability by ensuring sufficient contrast between text and backgrounds

**Animation & Interaction**:
- Create bouncy, playful animations using cubic-bezier easing (e.g., cubic-bezier(0.68, -0.55, 0.265, 1.55))
- Implement shape morphing on hover using border-radius transitions
- Add rotation and scale transforms for interactive elements (5-15 degrees rotation)
- Use staggered animations (100-200ms delays) when revealing multiple elements
- Keep animation duration short and snappy (200-400ms) to match energetic aesthetic

**Responsive Strategies**:
- On mobile: Reduce pattern density, stack elements vertically, simplify geometric backgrounds
- Tablet: Maintain most visual effects but reduce overlay complexity
- Desktop: Full Memphis experience with all patterns, shapes, and interactive elements
- Ensure patterns and shapes don't overwhelm content on smaller screens
