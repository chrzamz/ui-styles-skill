# Custom Prompt: Wabi-Sabi（侘寂美学）

## 中文版本 (zh-CN)

### 1. 设计哲学与核心原则

**Wabi-Sabi（侘寂）**是源自日本禅宗的美学理念，强调**接受不完美、欣赏未完成、尊重无常**。在界面设计中，侘寂美学摒弃现代主义的完美主义追求，转而通过**低饱和度色彩、自然材质纹理、大量留白、手工痕迹**来传达一种**宁静、克制、时间沉淀**的气质。

**核心哲学**：
- **不完美之美（Imperfection）**：接受裂纹、褪色、磨损等自然痕迹，不追求机械的完美
- **简朴素雅（Simplicity）**：去除一切不必要的装饰，保留最本质的元素
- **自然时光（Transience）**：尊重材料的老化、风化，视时间流逝为美的一部分
- **内敛宁静（Quietness）**：避免强烈对比和夸张表达，营造冥想般的氛围
- **手作温度（Handmade）**：保留人工制作的不均匀感和独特性

**设计原则**：
- **色彩低饱和**：使用灰绿、灰褐、米白、炭黑等大地色系，饱和度 < 30%
- **留白充足**：内容占据页面比例 < 50%，让画面呼吸
- **纹理自然**：使用纸张、亚麻、黏土、石头等自然材质的轻微纹理
- **边缘柔和**：避免锐利的硬边，使用微圆角或不规则边缘
- **交互克制**：hover/active 变化极小（仅 2-5% 亮度变化），动画时长 300-500ms
- **字体优雅**：衬线体用于标题（Noto Serif、Crimson Text），无衬线体用于正文（Inter、Source Sans）

### 2. 核心设计要求

#### 2.1 低饱和色彩系统（Low-Saturation Color Palette）

侘寂风格的配色以**大地色系**为核心，所有颜色饱和度极低（< 30%），模拟泥土、石头、植物、纸张等自然材质。

**主色调（Primary Colors）**：
- **米白背景（Off-White）**：`#F5F3EF` - 页面主背景（温暖的米白）
- **次级背景（Secondary Background）**：`#E8E5DF` - 区块背景（浅灰褐）
- **深色背景（Darker Background）**：`#D5D0C8` - 深色区块

**文本色（Text Colors）**：
- **主文本（Primary Text）**：`#3A3731` - 标题、正文（深炭灰）
- **次文本（Secondary Text）**：`#7A7772` - 辅助文字、说明（中灰褐）
- **强调色（Accent）**：`#A89C94` - 链接、重点（灰褐）
- **黏土色（Clay）**：`#C9BDB1` - 装饰、分隔（浅黏土）

**材质色（Material Colors）**：
- **亚麻（Linen）**：`#E8E5DF` → `#D5CFC5` 渐变
- **黏土（Clay）**：`#C9BDB1` → `#B8ACA0` 渐变
- **石头（Stone）**：`#BFB5A9` → `#AEA498` 渐变
- **纸张（Paper）**：`#F5F3EF` → `#E8E5DF` 渐变

**完整 CSS 变量定义**：
```css
:root {
  /* 背景色 */
  --wabi-bg-primary: #F5F3EF;
  --wabi-bg-secondary: #E8E5DF;
  --wabi-bg-dark: #D5D0C8;

  /* 文本色 */
  --wabi-text-primary: #3A3731;
  --wabi-text-secondary: #7A7772;
  --wabi-text-helper: #A89C94;

  /* 强调色 */
  --wabi-accent: #A89C94;
  --wabi-clay: #C9BDB1;

  /* 材质色（用于渐变） */
  --wabi-linen-light: #E8E5DF;
  --wabi-linen-dark: #D5CFC5;
  --wabi-clay-light: #C9BDB1;
  --wabi-clay-dark: #B8ACA0;
  --wabi-stone-light: #BFB5A9;
  --wabi-stone-dark: #AEA498;
  --wabi-paper-light: #F5F3EF;
  --wabi-paper-dark: #E8E5DF;

  /* 边框 */
  --wabi-border: rgba(58, 55, 49, 0.08);
  --wabi-border-medium: rgba(58, 55, 49, 0.12);
  --wabi-border-dark: rgba(58, 55, 49, 0.15);

  /* 圆角 */
  --wabi-radius: 2px;

  /* 字体 */
  --wabi-font-serif: 'Noto Serif', 'Crimson Text', Georgia, serif;
  --wabi-font-sans: 'Inter', -apple-system, sans-serif;

  /* 阴影（极轻） */
  --wabi-shadow-sm: 0 10px 30px rgba(58, 55, 49, 0.06);
  --wabi-shadow-md: 0 20px 60px rgba(58, 55, 49, 0.08);
  --wabi-shadow-lg: 0 30px 80px rgba(58, 55, 49, 0.12);
}
```

#### 2.2 纹理叠加系统（Texture Overlay System）

侘寂风格使用**极低透明度的自然纹理**叠加在背景上，模拟纸张纤维、亚麻编织、黏土表面、石头裂纹等效果。

```css
/* 纸张纤维纹理（Paper Fiber） */
.wabi-texture-paper {
  position: relative;
  overflow: hidden;
}

.wabi-texture-paper::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(58, 55, 49, 0.02) 2px,
      rgba(58, 55, 49, 0.02) 4px
    );
  pointer-events: none;
  opacity: 0.5;
}

/* 亚麻编织纹理（Linen Weave） */
.wabi-texture-linen {
  position: relative;
  background:
    linear-gradient(90deg, transparent 1px, rgba(245, 243, 239, 0.5) 1px),
    linear-gradient(rgba(232, 229, 223, 1) 0%, rgba(213, 207, 197, 1) 100%);
  background-size: 3px 3px, 100% 100%;
}

/* 黏土表面纹理（Clay Surface） */
.wabi-texture-clay {
  background: radial-gradient(
    circle at 30% 40%,
    var(--wabi-clay-light) 0%,
    var(--wabi-clay-dark) 100%
  );
  box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* 石头裂纹纹理（Stone Cracks） */
.wabi-texture-stone {
  background:
    radial-gradient(
      circle at 20% 30%,
      transparent 5%,
      rgba(58, 55, 49, 0.05) 5%
    ),
    radial-gradient(
      circle at 70% 60%,
      transparent 3%,
      rgba(58, 55, 49, 0.03) 3%
    ),
    linear-gradient(
      var(--wabi-stone-light) 0%,
      var(--wabi-stone-dark) 100%
    );
}

/* 网格纹理（Grid Pattern） */
.wabi-texture-grid {
  position: relative;
}

.wabi-texture-grid::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    repeating-linear-gradient(
      90deg,
      transparent,
      transparent 2px,
      rgba(58, 55, 49, 0.02) 2px,
      rgba(58, 55, 49, 0.02) 4px
    ),
    repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(58, 55, 49, 0.02) 2px,
      rgba(58, 55, 49, 0.02) 4px
    );
  opacity: 0.5;
  pointer-events: none;
}

/* 斜纹纹理（Diagonal Pattern） */
.wabi-texture-diagonal {
  position: relative;
}

.wabi-texture-diagonal::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 10px,
      rgba(58, 55, 49, 0.02) 10px,
      rgba(58, 55, 49, 0.02) 20px
    );
  pointer-events: none;
}
```

#### 2.3 留白与间距系统（Whitespace & Spacing System）

侘寂风格强调**大量留白**，让页面元素有充足的呼吸空间。间距系统基于 **8px 基准**。

```css
:root {
  /* 间距比例 */
  --wabi-space-xs: 0.5rem;   /* 8px */
  --wabi-space-sm: 1rem;     /* 16px */
  --wabi-space-md: 1.5rem;   /* 24px */
  --wabi-space-lg: 2rem;     /* 32px */
  --wabi-space-xl: 3rem;     /* 48px */
  --wabi-space-2xl: 5rem;    /* 80px */
  --wabi-space-3xl: 8rem;    /* 128px */
  --wabi-space-4xl: 10rem;   /* 160px */

  /* 容器最大宽度 */
  --wabi-container-sm: 800px;    /* 小容器 */
  --wabi-container-md: 1200px;   /* 标准容器 */
  --wabi-container-lg: 1400px;   /* 大容器 */
}

/* 容器系统 */
.wabi-container {
  max-width: var(--wabi-container-md);
  margin: 0 auto;
  padding: 0 3rem;
}

.wabi-container-sm {
  max-width: var(--wabi-container-sm);
  margin: 0 auto;
  padding: 0 3rem;
}

.wabi-container-lg {
  max-width: var(--wabi-container-lg);
  margin: 0 auto;
  padding: 0 3rem;
}

/* 章节间距 */
.wabi-section {
  padding: var(--wabi-space-3xl) 0;
}

.wabi-section-lg {
  padding: var(--wabi-space-4xl) 0;
}

/* 内容留白 */
.wabi-content-space {
  margin-bottom: var(--wabi-space-2xl);
}
```

#### 2.4 不完美边缘系统（Imperfect Edges System）

侘寂风格接受**不完美的边缘**和**手工痕迹**，使用极小圆角或自然形状。

```css
/* 微圆角卡片 */
.wabi-card {
  background: var(--wabi-bg-primary);
  border-radius: var(--wabi-radius);
  padding: var(--wabi-space-xl);
  box-shadow: var(--wabi-shadow-md);
  border: 1px solid var(--wabi-border);
  transition: all 0.4s ease;
}

.wabi-card:hover {
  box-shadow: var(--wabi-shadow-lg);
  transform: translateY(-8px);
}

/* 不规则边缘（使用 filter） */
.wabi-card-organic {
  background: var(--wabi-bg-secondary);
  border-radius: var(--wabi-radius);
  padding: var(--wabi-space-xl);
  box-shadow: var(--wabi-shadow-md);
  filter: url('#wabi-organic-filter');
}

/* SVG 滤镜定义（在 HTML 中添加） */
<svg style="position: absolute; width: 0; height: 0;">
  <defs>
    <filter id="wabi-organic-filter">
      <feTurbulence
        type="fractalNoise"
        baseFrequency="0.01"
        numOctaves="2"
        result="noise" />
      <feDisplacementMap
        in="SourceGraphic"
        in2="noise"
        scale="2"
        xChannelSelector="R"
        yChannelSelector="G" />
    </filter>
  </defs>
</svg>

/* 手绘边框 */
.wabi-border-handdrawn {
  position: relative;
  padding: var(--wabi-space-lg);
}

.wabi-border-handdrawn::before {
  content: '';
  position: absolute;
  inset: -2px;
  border: 1px solid var(--wabi-text-secondary);
  border-radius: var(--wabi-radius);
  opacity: 0.3;
  transform: rotate(-0.5deg);
}

.wabi-border-handdrawn::after {
  content: '';
  position: absolute;
  inset: -4px;
  border: 1px solid var(--wabi-text-secondary);
  border-radius: var(--wabi-radius);
  opacity: 0.2;
  transform: rotate(0.5deg);
}

/* 印章式标签 */
.wabi-stamp {
  display: inline-block;
  padding: 0.5rem 1rem;
  border: 2px solid var(--wabi-text-primary);
  border-radius: 50%;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--wabi-text-primary);
  transform: rotate(-5deg);
  opacity: 0.8;
}
```

#### 2.5 极简交互系统（Minimal Interaction System）

侘寂风格的交互**极其克制**，hover 变化仅体现在**轻微的亮度调整**和**缓慢的过渡**。

```css
/* 基础链接 */
.wabi-link {
  color: var(--wabi-text-secondary);
  text-decoration: none;
  font-size: 0.9rem;
  letter-spacing: 0.05em;
  transition: color 0.4s ease;
  position: relative;
}

.wabi-link::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 1px;
  background: var(--wabi-text-primary);
  transition: width 0.4s ease;
}

.wabi-link:hover {
  color: var(--wabi-text-primary);
}

.wabi-link:hover::after {
  width: 100%;
}

/* 极简按钮 */
.wabi-btn {
  display: inline-block;
  padding: 1rem 3rem;
  border: 1px solid var(--wabi-text-primary);
  color: var(--wabi-text-primary);
  background: transparent;
  font-size: 0.9rem;
  letter-spacing: 0.1em;
  text-decoration: none;
  transition: all 0.4s ease;
  cursor: pointer;
}

.wabi-btn:hover {
  background: var(--wabi-text-primary);
  color: var(--wabi-bg-primary);
}

.wabi-btn:active {
  transform: scale(0.98);
  opacity: 0.9;
}

/* 图片悬停 */
.wabi-image-wrapper {
  position: relative;
  overflow: hidden;
  border-radius: var(--wabi-radius);
  background: var(--wabi-bg-primary);
  box-shadow: var(--wabi-shadow-md);
  transition: all 0.5s ease;
}

.wabi-image-wrapper:hover {
  transform: translateY(-8px);
  box-shadow: var(--wabi-shadow-lg);
}

.wabi-image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease, opacity 0.5s ease;
}

.wabi-image-wrapper:hover img {
  transform: scale(1.03);
  opacity: 0.95;
}
```

#### 2.6 字体系统（Typography System）

侘寂风格使用**衬线体**（Noto Serif、Crimson Text）表现优雅，**无衬线体**（Inter、Source Sans）保持简洁。

```css
/* 字体导入 */
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif:wght@300;400;600&family=Inter:wght@300;400;500&display=swap');

/* 标题字体系统 */
.wabi-title-xl {
  font-family: var(--wabi-font-serif);
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  font-weight: 300;
  color: var(--wabi-text-primary);
  line-height: 1.3;
  letter-spacing: 0.02em;
  margin-bottom: 1.5rem;
}

.wabi-title-lg {
  font-family: var(--wabi-font-serif);
  font-size: 2.5rem;
  font-weight: 400;
  color: var(--wabi-text-primary);
  line-height: 1.4;
  letter-spacing: 0.03em;
  margin-bottom: 2rem;
}

.wabi-title-md {
  font-family: var(--wabi-font-serif);
  font-size: 2rem;
  font-weight: 400;
  color: var(--wabi-text-primary);
  line-height: 1.4;
  letter-spacing: 0.05em;
  margin-bottom: 1.5rem;
}

.wabi-title-sm {
  font-family: var(--wabi-font-serif);
  font-size: 1.5rem;
  font-weight: 400;
  color: var(--wabi-text-primary);
  line-height: 1.5;
  letter-spacing: 0.03em;
  margin-bottom: 1rem;
}

/* 正文字体系统 */
.wabi-body-lg {
  font-family: var(--wabi-font-sans);
  font-size: 1.1rem;
  color: var(--wabi-text-secondary);
  line-height: 2;
  letter-spacing: 0.03em;
}

.wabi-body {
  font-family: var(--wabi-font-sans);
  font-size: 1rem;
  color: var(--wabi-text-secondary);
  line-height: 1.8;
  letter-spacing: 0.03em;
}

.wabi-body-sm {
  font-family: var(--wabi-font-sans);
  font-size: 0.9rem;
  color: var(--wabi-text-secondary);
  line-height: 1.7;
  letter-spacing: 0.05em;
}

/* 标签字体系统 */
.wabi-label {
  font-family: var(--wabi-font-sans);
  font-size: 0.75rem;
  color: var(--wabi-text-secondary);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

/* 引用 */
.wabi-quote {
  font-family: var(--wabi-font-serif);
  font-size: 1.5rem;
  font-weight: 300;
  font-style: italic;
  color: var(--wabi-text-primary);
  line-height: 1.8;
  letter-spacing: 0.02em;
  padding-left: 2rem;
  border-left: 2px solid var(--wabi-border-dark);
}
```

#### 2.7 自然阴影系统（Natural Shadow System）

侘寂风格的阴影**极其轻柔**，模拟自然光的柔和投射，避免强烈的对比。

```css
/* 阴影定义 */
:root {
  /* 极轻阴影 */
  --wabi-shadow-xs: 0 5px 15px rgba(58, 55, 49, 0.04);
  /* 轻阴影 */
  --wabi-shadow-sm: 0 10px 30px rgba(58, 55, 49, 0.06);
  /* 标准阴影 */
  --wabi-shadow-md: 0 20px 60px rgba(58, 55, 49, 0.08);
  /* 强阴影 */
  --wabi-shadow-lg: 0 30px 80px rgba(58, 55, 49, 0.12);
  /* 内阴影（凹陷） */
  --wabi-shadow-inset: inset 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* 卡片阴影 */
.wabi-card {
  box-shadow: var(--wabi-shadow-md);
}

.wabi-card:hover {
  box-shadow: var(--wabi-shadow-lg);
}

/* 浮动元素 */
.wabi-float {
  box-shadow: var(--wabi-shadow-sm);
  transition: all 0.4s ease;
}

.wabi-float:hover {
  box-shadow: var(--wabi-shadow-md);
  transform: translateY(-5px);
}

/* 凹陷效果（黏土表面） */
.wabi-inset {
  box-shadow: var(--wabi-shadow-inset);
}
```

#### 2.8 材质卡片系统（Material Card System）

侘寂风格使用**材质卡片**展示不同的自然纹理和质感。

```css
/* 基础材质卡片 */
.wabi-material-card {
  text-align: center;
  transition: transform 0.4s ease;
}

.wabi-material-swatch {
  width: 100%;
  aspect-ratio: 1;
  border-radius: var(--wabi-radius);
  margin-bottom: 1.5rem;
  box-shadow: var(--wabi-shadow-md);
  transition: transform 0.4s ease;
}

.wabi-material-card:hover .wabi-material-swatch {
  transform: translateY(-5px);
}

.wabi-material-name {
  font-family: var(--wabi-font-serif);
  font-size: 1.1rem;
  font-weight: 400;
  color: var(--wabi-text-primary);
  margin-bottom: 0.5rem;
  letter-spacing: 0.05em;
}

.wabi-material-desc {
  font-size: 0.85rem;
  color: var(--wabi-text-secondary);
  letter-spacing: 0.05em;
}

/* 材质样例组合 */
.wabi-material-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 3rem;
}

@media (max-width: 1024px) {
  .wabi-material-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
  }
}

@media (max-width: 768px) {
  .wabi-material-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}
```

### 3. Tailwind CSS 配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        wabi: {
          'bg-primary': '#F5F3EF',
          'bg-secondary': '#E8E5DF',
          'bg-dark': '#D5D0C8',
          'text-primary': '#3A3731',
          'text-secondary': '#7A7772',
          'text-helper': '#A89C94',
          'accent': '#A89C94',
          'clay': '#C9BDB1',
          'linen-light': '#E8E5DF',
          'linen-dark': '#D5CFC5',
          'clay-light': '#C9BDB1',
          'clay-dark': '#B8ACA0',
          'stone-light': '#BFB5A9',
          'stone-dark': '#AEA498',
          'paper-light': '#F5F3EF',
          'paper-dark': '#E8E5DF',
        },
      },
      fontFamily: {
        serif: ['Noto Serif', 'Crimson Text', 'Georgia', 'serif'],
        sans: ['Inter', '-apple-system', 'sans-serif'],
      },
      spacing: {
        'wabi-xs': '0.5rem',
        'wabi-sm': '1rem',
        'wabi-md': '1.5rem',
        'wabi-lg': '2rem',
        'wabi-xl': '3rem',
        'wabi-2xl': '5rem',
        'wabi-3xl': '8rem',
        'wabi-4xl': '10rem',
      },
      maxWidth: {
        'wabi-sm': '800px',
        'wabi-md': '1200px',
        'wabi-lg': '1400px',
      },
      boxShadow: {
        'wabi-xs': '0 5px 15px rgba(58, 55, 49, 0.04)',
        'wabi-sm': '0 10px 30px rgba(58, 55, 49, 0.06)',
        'wabi-md': '0 20px 60px rgba(58, 55, 49, 0.08)',
        'wabi-lg': '0 30px 80px rgba(58, 55, 49, 0.12)',
        'wabi-inset': 'inset 0 2px 10px rgba(0, 0, 0, 0.1)',
      },
      borderRadius: {
        'wabi': '2px',
      },
      transitionDuration: {
        'wabi': '400ms',
      },
      animation: {
        'wabi-fade-in': 'wabiFlowIn 1.5s ease-out',
        'wabi-scroll-pulse': 'scrollPulse 2s ease-in-out infinite',
      },
      keyframes: {
        wabiFlowIn: {
          from: {
            opacity: '0',
            transform: 'translateY(30px)',
          },
          to: {
            opacity: '1',
            transform: 'translateY(0)',
          },
        },
        scrollPulse: {
          '0%, 100%': {
            opacity: '0.3',
            transform: 'translateY(0)',
          },
          '50%': {
            opacity: '1',
            transform: 'translateY(10px)',
          },
        },
      },
    },
  },
  plugins: [],
};
```

### 4. 使用示例

```html
<!-- 侘寂风格页面 -->
<div class="min-h-screen bg-wabi-bg-primary">
  <!-- 导航栏 -->
  <nav class="fixed top-0 left-0 right-0 bg-wabi-bg-primary/95 backdrop-blur-sm border-b border-wabi-bg-dark z-50">
    <div class="wabi-container flex justify-between items-center py-6">
      <div class="wabi-title-sm mb-0">侘寂 Studio</div>
      <div class="flex gap-10">
        <a href="#" class="wabi-link">Works</a>
        <a href="#" class="wabi-link">About</a>
        <a href="#" class="wabi-link">Journal</a>
        <a href="#" class="wabi-link">Contact</a>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <section class="wabi-section-lg wabi-texture-grid mt-20">
    <div class="wabi-container-sm text-center animate-wabi-fade-in">
      <h1 class="wabi-title-xl">Finding Beauty in Imperfection</h1>
      <p class="wabi-body-lg">
        A visual journey through simplicity, transience, and natural elegance
      </p>
      <div class="flex flex-col items-center gap-4 mt-20 opacity-60">
        <span class="wabi-label">Scroll to explore</span>
        <div class="w-px h-10 bg-wabi-text-secondary animate-wabi-scroll-pulse"></div>
      </div>
    </div>
  </section>

  <!-- Philosophy Statement -->
  <section class="wabi-section">
    <div class="wabi-container">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-20 items-center">
        <div>
          <h2 class="wabi-title-lg">Wabi-Sabi</h2>
          <p class="wabi-body-lg">
            Embracing the imperfect, appreciating the incomplete, and honoring the impermanent.
            Our approach to visual storytelling reflects the Japanese aesthetic of finding profound
            beauty in simplicity and naturalness.
          </p>
        </div>
        <div>
          <div class="wabi-texture-clay aspect-[4/5] rounded-wabi shadow-wabi-md"></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Gallery Grid -->
  <section class="wabi-section bg-wabi-bg-secondary">
    <div class="wabi-container">
      <h2 class="wabi-title-md text-center mb-20">Selected Works</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12">
        <!-- Gallery Item 1 -->
        <div class="group">
          <div class="wabi-image-wrapper">
            <div class="wabi-texture-linen aspect-[4/5] flex items-center justify-center">
              <span class="wabi-label opacity-40">Ceramic Still Life</span>
            </div>
          </div>
          <div class="mt-6">
            <h3 class="wabi-title-sm mb-2">Earth & Form</h3>
            <p class="wabi-body-sm">Handcrafted pottery series</p>
          </div>
        </div>

        <!-- Gallery Item 2 -->
        <div class="group">
          <div class="wabi-image-wrapper">
            <div class="wabi-texture-stone aspect-[4/5] flex items-center justify-center">
              <span class="wabi-label opacity-40">Architectural Study</span>
            </div>
          </div>
          <div class="mt-6">
            <h3 class="wabi-title-sm mb-2">Light & Shadow</h3>
            <p class="wabi-body-sm">Minimalist architecture</p>
          </div>
        </div>

        <!-- Gallery Item 3 -->
        <div class="group">
          <div class="wabi-image-wrapper">
            <div class="wabi-texture-paper aspect-[4/5] flex items-center justify-center">
              <span class="wabi-label opacity-40">Textile Detail</span>
            </div>
          </div>
          <div class="mt-6">
            <h3 class="wabi-title-sm mb-2">Woven Textures</h3>
            <p class="wabi-body-sm">Natural linen collection</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Material Swatches -->
  <section class="wabi-section">
    <div class="wabi-container">
      <h2 class="wabi-title-md text-center mb-20">Material Palette</h2>
      <div class="wabi-material-grid">
        <div class="wabi-material-card">
          <div class="wabi-material-swatch wabi-texture-linen"></div>
          <h3 class="wabi-material-name">Linen</h3>
          <p class="wabi-material-desc">Natural woven texture</p>
        </div>
        <div class="wabi-material-card">
          <div class="wabi-material-swatch wabi-texture-clay"></div>
          <h3 class="wabi-material-name">Clay</h3>
          <p class="wabi-material-desc">Earthy ceramic finish</p>
        </div>
        <div class="wabi-material-card">
          <div class="wabi-material-swatch wabi-texture-stone"></div>
          <h3 class="wabi-material-name">Stone</h3>
          <p class="wabi-material-desc">Weathered surface</p>
        </div>
        <div class="wabi-material-card">
          <div class="wabi-material-swatch wabi-texture-paper"></div>
          <h3 class="wabi-material-name">Paper</h3>
          <p class="wabi-material-desc">Handmade washi</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section class="wabi-section-lg bg-wabi-bg-secondary text-center">
    <div class="wabi-container-sm">
      <h2 class="wabi-title-lg">Let's Create Together</h2>
      <p class="wabi-body-lg mb-12">
        For collaboration inquiries and project discussions
      </p>
      <a href="#" class="wabi-btn">Get in Touch</a>
    </div>
  </section>

  <!-- Footer -->
  <footer class="py-12 bg-wabi-bg-primary border-t border-wabi-bg-dark">
    <div class="wabi-container flex justify-between items-center">
      <p class="wabi-body-sm">&copy; 2025 Wabi-Sabi Studio. Embracing imperfection.</p>
      <div class="flex gap-8">
        <a href="#" class="wabi-link">Instagram</a>
        <a href="#" class="wabi-link">Behance</a>
        <a href="#" class="wabi-link">Email</a>
      </div>
    </div>
  </footer>
</div>
```


---

## English Version (en-US)

### 1. Design Philosophy & Core Principles

**Wabi-Sabi** is a Japanese aesthetic philosophy rooted in Zen Buddhism that emphasizes **accepting imperfection, appreciating incompleteness, and honoring impermanence**. In UI design, Wabi-Sabi rejects the perfectionism of modernism, instead conveying **serenity, restraint, and timeworn beauty** through **low-saturation colors, natural material textures, generous whitespace, and handmade traces**.

**Core Philosophy**:
- **Imperfection**: Accept cracks, fading, wear as natural marks, not pursuing mechanical perfection
- **Simplicity**: Remove all unnecessary decoration, retain only essential elements
- **Transience**: Respect aging and weathering of materials, view passage of time as part of beauty
- **Quietness**: Avoid strong contrasts and exaggerations, create meditative atmospheres
- **Handmade**: Preserve unevenness and uniqueness of manual craftsmanship

**Design Principles**:
- **Low-saturation colors**: Use gray-green, gray-brown, off-white, charcoal with saturation < 30%
- **Generous whitespace**: Content occupies < 50% of page area, let the design breathe
- **Natural textures**: Use subtle textures of paper, linen, clay, stone
- **Soft edges**: Avoid sharp hard edges, use micro-rounded or irregular edges
- **Restrained interaction**: Hover/active changes are minimal (only 2-5% brightness), animation 300-500ms
- **Elegant typography**: Serif for titles (Noto Serif, Crimson Text), sans-serif for body (Inter, Source Sans)

### 2. Core Design Requirements

[Continue with English translations of all sections above, maintaining the same structure and detail level...]

**Implementation Guidelines**

**Typography Best Practices**:
- Use serif fonts for headlines (Noto Serif CJK, Crimson Text, Lora) to convey elegance and tradition
- Body text should use humanist sans-serif (Inter, Source Sans Pro) for clarity at 16-18px
- Maintain generous line-height (1.7-2.0) for comfortable reading and visual breathing room
- Use subtle font-weight variations (400 for body, 500-600 for emphasis) instead of stark bold

**Color Application**:
- Limit palette to 3-4 earth tones plus neutrals to maintain harmony
- Use color sparingly - let natural tones and textures dominate
- Avoid pure white (#ffffff) - prefer warm whites (#faf8f5, #f5f3ef)
- Test colors under different lighting conditions to ensure they maintain their calming quality

**Layout & Spacing**:
- Use generous margins and padding (minimum 24px, ideally 40-60px on desktop)
- Maintain 40-60% whitespace ratio to content for visual breathing room
- Implement asymmetric layouts where appropriate to create organic flow
- Use fluid spacing with clamp() for responsive designs that maintain proportions

**Texture & Material**:
- Apply paper or linen textures at 2-5% opacity for subtle organic feel
- Use CSS filters sparingly - prefer natural color variations over heavy effects
- Implement subtle gradients (5-10% opacity difference) for depth
- Add grain or noise textures to backgrounds for handmade quality

**Responsive Behavior**:
- On mobile, increase text size slightly (18-20px body) for readability
- Maintain generous spacing even on small screens - reduce content, not white space
- Simplify animations or remove them entirely on mobile for serene experience
- Stack elements vertically with consistent rhythm (space-y-8 to space-y-12)
