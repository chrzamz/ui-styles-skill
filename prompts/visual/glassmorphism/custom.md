# Custom Prompt - Glassmorphism Style

## 中文版本 (zh-CN)

请使用 TailwindCSS 创建一个玻璃态（Glassmorphism）风格的界面，通过背景模糊、透明度和光影效果创造层次丰富、现代优雅的视觉体验。

**核心设计要求**

1. **背景模糊效果（Backdrop Blur）**
   - 使用 backdrop-filter 实现背景虚化
   - 模糊半径：10px（轻微）- 40px（强烈）
   - 必须添加 -webkit- 前缀确保 Safari 兼容性
   - 示例：
     ```css
     .glass-card {
       backdrop-filter: blur(20px);
       -webkit-backdrop-filter: blur(20px); /* Safari 兼容 */
     }

     /* 不同强度的模糊 */
     .glass-light { backdrop-filter: blur(10px); }
     .glass-medium { backdrop-filter: blur(20px); }
     .glass-strong { backdrop-filter: blur(40px); }
     ```

2. **透明度层级系统**
   - 使用 rgba 控制透明度，创建层次感
   - 透明度范围：0.05（极浅）- 0.2（较深）
   - 避免超过 0.3，否则失去玻璃质感
   - 示例：
     ```css
     /* 主要卡片 */
     .glass-primary {
       background: rgba(255, 255, 255, 0.1);
     }

     /* 次要卡片（更浅） */
     .glass-secondary {
       background: rgba(255, 255, 255, 0.05);
     }

     /* 强调卡片（略深） */
     .glass-emphasis {
       background: rgba(255, 255, 255, 0.15);
     }

     /* 黑色玻璃变体 */
     .glass-dark {
       background: rgba(0, 0, 0, 0.2);
     }
     ```

3. **边缘光晕和描边**
   - 使用半透明边框创建光感
   - 边框透明度：0.1 - 0.3
   - 边框宽度：1px（标准）到 2px（强调）
   - 示例：
     ```css
     .glass-border {
       border: 1px solid rgba(255, 255, 255, 0.18);
     }

     /* 渐变边框（高级技巧） */
     .glass-border-gradient {
       border: 1px solid transparent;
       background-image:
         linear-gradient(white, white),
         linear-gradient(135deg,
           rgba(255,255,255,0.3),
           rgba(255,255,255,0.1),
           rgba(255,255,255,0.2)
         );
       background-origin: border-box;
       background-clip: padding-box, border-box;
     }
     ```

4. **柔和阴影系统**
   - 使用低透明度阴影创造深度
   - 多层阴影叠加增强立体感
   - 示例：
     ```css
     .glass-shadow {
       box-shadow:
         0 8px 32px 0 rgba(31, 38, 135, 0.37),
         0 4px 16px 0 rgba(31, 38, 135, 0.2);
     }

     /* 悬停时加深阴影 */
     .glass-shadow:hover {
       box-shadow:
         0 12px 48px 0 rgba(31, 38, 135, 0.45),
         0 6px 24px 0 rgba(31, 38, 135, 0.3);
     }

     /* 轻微阴影（次要元素） */
     .glass-shadow-light {
       box-shadow: 0 4px 16px 0 rgba(31, 38, 135, 0.2);
     }
     ```

5. **渐变背景衬托**
   - 玻璃效果需要丰富背景衬托
   - 使用渐变或图像背景
   - 示例：
     ```css
     /* 经典紫色渐变 */
     .glass-bg-purple {
       background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
     }

     /* 多色渐变 */
     .glass-bg-rainbow {
       background: linear-gradient(135deg,
         #667eea 0%,
         #764ba2 50%,
         #f093fb 100%
       );
     }

     /* 动态渐变 */
     .glass-bg-animated {
       background: linear-gradient(
         135deg,
         #667eea,
         #764ba2,
         #f093fb,
         #4facfe
       );
       background-size: 400% 400%;
       animation: gradientShift 15s ease infinite;
     }

     @keyframes gradientShift {
       0%, 100% { background-position: 0% 50%; }
       50% { background-position: 100% 50%; }
     }
     ```

6. **圆角和形状**
   - 使用较大圆角保持柔和感
   - 圆角半径：12px（小）- 24px（大）
   - 示例：
     ```css
     .glass-rounded-sm { border-radius: 12px; }
     .glass-rounded-md { border-radius: 16px; }
     .glass-rounded-lg { border-radius: 20px; }
     .glass-rounded-xl { border-radius: 24px; }
     ```

7. **动态粒子背景（可选）**
   - 浮动的半透明圆形元素
   - 使用 CSS 动画创造流动感
   - 示例：
     ```css
     .particle {
       position: absolute;
       border-radius: 50%;
       background: linear-gradient(
         135deg,
         rgba(255, 255, 255, 0.2),
         rgba(255, 255, 255, 0.05)
       );
       animation: float-particle 20s ease-in-out infinite;
     }

     @keyframes float-particle {
       0%, 100% { transform: translate(0, 0) scale(1); }
       25% { transform: translate(30px, -40px) scale(1.1); }
       50% { transform: translate(-20px, -80px) scale(0.9); }
       75% { transform: translate(-40px, -40px) scale(1.05); }
     }
     ```

**配色方案（玻璃透明质感）**

主色调：
- 白色玻璃：rgba(255, 255, 255, 0.05-0.2)
- 边框高光：rgba(255, 255, 255, 0.1-0.3)
- 文字主色：#ffffff（白色，适用于深色背景）
- 文字次要：rgba(255, 255, 255, 0.7-0.9)

背景色（用于衬托）：
- 经典紫色渐变：#667eea → #764ba2
- 多色渐变：#667eea → #764ba2 → #f093fb
- 蓝紫渐变：#667eea → #764ba2 → #f093fb → #4facfe
- 深蓝：#1e3a8a → #1e40af
- 深紫：#5b21b6 → #7c3aed

阴影色：
- 柔和阴影：rgba(31, 38, 135, 0.2-0.45)
- 深色阴影：rgba(0, 0, 0, 0.1-0.3)

强调色：
- 霓虹蓝：#60a5fa
- 霓虹紫：#a78bfa
- 霓虹粉：#f472b6

**关键 CSS 类示例**

```css
/* 玻璃态卡片（标准） */
.glass-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  padding: 32px;
  transition: all 0.3s ease;
}

.glass-card:hover {
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 0 12px 48px 0 rgba(31, 38, 135, 0.45);
  transform: translateY(-4px);
}

/* 玻璃态按钮 */
.glass-button {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 12px 32px;
  color: #ffffff;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px 0 rgba(31, 38, 135, 0.2);
}

.glass-button:hover {
  background: rgba(255, 255, 255, 0.2);
  box-shadow: 0 6px 24px 0 rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
}

.glass-button:active {
  transform: translateY(0);
  box-shadow: 0 2px 8px 0 rgba(31, 38, 135, 0.2);
}

/* 玻璃态输入框 */
.glass-input {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 14px 18px;
  color: #ffffff;
  font-size: 16px;
  width: 100%;
  transition: all 0.3s ease;
}

.glass-input:focus {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.3);
  outline: none;
  box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.1);
}

.glass-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

/* 玻璃态导航栏 */
.glass-nav {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(40px);
  -webkit-backdrop-filter: blur(40px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 4px 16px 0 rgba(31, 38, 135, 0.2);
  position: sticky;
  top: 0;
  z-index: 100;
}

/* 玻璃态容器背景 */
.glass-container {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
  min-height: 100vh;
  padding: 48px;
  position: relative;
  overflow: hidden;
}

/* 玻璃态进度条 */
.glass-progress {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 24px;
  height: 8px;
  overflow: hidden;
}

.glass-progress-fill {
  background: linear-gradient(90deg, #60a5fa 0%, #a78bfa 100%);
  height: 100%;
  border-radius: 24px;
  box-shadow: 0 0 16px rgba(96, 165, 250, 0.5);
  transition: width 0.3s ease;
}

/* 玻璃态浮动按钮 */
.glass-fab {
  position: fixed;
  bottom: 32px;
  right: 32px;
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.glass-fab:hover {
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 0 12px 48px 0 rgba(31, 38, 135, 0.45);
  transform: scale(1.1);
}
```

**Tailwind CSS 配置**

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      backdropBlur: {
        xs: '2px',
        sm: '4px',
        md: '10px',
        lg: '20px',
        xl: '40px',
      },
      colors: {
        'glass-white': {
          5: 'rgba(255, 255, 255, 0.05)',
          10: 'rgba(255, 255, 255, 0.1)',
          15: 'rgba(255, 255, 255, 0.15)',
          20: 'rgba(255, 255, 255, 0.2)',
        },
      },
      boxShadow: {
        'glass': '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
        'glass-hover': '0 12px 48px 0 rgba(31, 38, 135, 0.45)',
      },
    },
  },
}
```

**Tailwind CSS 类示例**

```html
<!-- 玻璃态卡片 -->
<div class="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/[0.18] shadow-glass p-8 hover:bg-white/15 hover:shadow-glass-hover transition-all">
  <!-- 卡片内容 -->
</div>

<!-- 玻璃态按钮 -->
<button class="bg-white/10 backdrop-blur-md rounded-xl border border-white/20 px-8 py-3 text-white font-semibold shadow-[0_4px_16px_0_rgba(31,38,135,0.2)] hover:bg-white/20 hover:shadow-[0_6px_24px_0_rgba(255,255,255,0.3)] transition-all">
  Click Me
</button>

<!-- 玻璃态输入框 -->
<input type="text" placeholder="Search..." class="bg-white/5 backdrop-blur-md rounded-xl border border-white/10 px-5 py-3.5 text-white placeholder:text-white/50 focus:bg-white/10 focus:border-white/30 focus:ring-4 focus:ring-white/10 transition-all w-full">

<!-- 玻璃态导航栏 -->
<nav class="bg-white/[0.08] backdrop-blur-[40px] border-b border-white/15 shadow-[0_4px_16px_0_rgba(31,38,135,0.2)] sticky top-0 z-100">
  <!-- 导航内容 -->
</nav>
```

**间距系统（基于 8px）**

- xs: 8px (0.5rem)
- sm: 16px (1rem)
- md: 24px (1.5rem)
- lg: 32px (2rem)
- xl: 48px (3rem)
- 2xl: 64px (4rem)
- 3xl: 96px (6rem)

**字体大小系统**

标题：
- h1: 48px-72px (3rem-4.5rem), font-weight: 700-800
- h2: 36px-48px (2.25rem-3rem), font-weight: 700
- h3: 28px-36px (1.75rem-2.25rem), font-weight: 600-700
- h4: 24px-28px (1.5rem-1.75rem), font-weight: 600

正文：
- 大号：18px-20px (1.125rem-1.25rem)
- 标准：16px-18px (1rem-1.125rem)
- 小号：14px-16px (0.875rem-1rem)
- 极小：12px-14px (0.75rem-0.875rem)
- 行高：1.5-1.7

**模糊强度系统**

- 极轻：blur(5px) - 用于微妙效果
- 轻度：blur(10px) - 用于按钮、输入框
- 中度：blur(20px) - 用于卡片（最常用）
- 强烈：blur(30px) - 用于主要容器
- 极强：blur(40px) - 用于导航栏、模态框

**透明度层级系统**

- Level 1（最浅）：rgba(255, 255, 255, 0.05) - 次要元素
- Level 2：rgba(255, 255, 255, 0.08) - 导航栏
- Level 3：rgba(255, 255, 255, 0.1) - 标准卡片
- Level 4：rgba(255, 255, 255, 0.15) - 强调卡片
- Level 5（最深）：rgba(255, 255, 255, 0.2) - 悬停状态

**重要提示**

- **必须有深色或渐变背景衬托**，否则玻璃效果不明显
- **backdrop-filter 在 Safari 需要 -webkit- 前缀**，必须同时添加
- **透明度不宜过高**，避免超过 0.3，否则失去玻璃质感
- **边框透明度应低于背景透明度**，保持细腻的光感
- **使用较大圆角**（12px-24px），避免直角
- **阴影颜色使用低透明度黑色或蓝色**，不要使用彩色阴影
- **文字必须使用白色或浅色**，确保在深色背景上可读
- **避免使用纯黑或纯白背景**，使用渐变或图像
- **模糊半径不宜过大**，避免超过 40px
- **动画过渡时间建议 0.3s**，保持流畅感
- **hover 状态应提升透明度和阴影**，增强互动反馈
- **多层玻璃叠加时，每层透明度递减**
- **使用 position: sticky 时注意 z-index 层级**
- **移动端性能考虑**：过多 backdrop-filter 可能影响性能

**避免事项**

- ❌ 不要在浅色背景上使用玻璃效果
- ❌ 不要使用过高的透明度（超过 0.3）
- ❌ 不要使用模糊的阴影（使用清晰的多层阴影）
- ❌ 不要使用锐利的边角（使用圆角）
- ❌ 不要忽略 Safari 兼容性（必须加 -webkit- 前缀）
- ❌ 不要在文字上直接使用强模糊
- ❌ 不要过度嵌套玻璃元素（影响性能）
- ❌ 不要使用过暗的边框色
- ❌ 不要在玻璃元素内使用深色背景图
- ❌ 不要使用过多动态粒子（影响性能）
- ❌ 不要混用玻璃效果和其他重型效果（如大型阴影）
- ❌ 不要在小元素上使用强烈模糊

**性能优化建议**

- 限制 backdrop-filter 使用数量（建议不超过 10 个可见元素）
- 使用 will-change 属性预优化动画元素
- 移动端考虑降低模糊强度
- 使用 CSS containment 隔离重绘区域
- 避免在滚动容器内大量使用 backdrop-filter


---

## English Version (en-US)

Please create a Glassmorphism style interface using TailwindCSS, creating rich layered and modern elegant visual experiences through background blur, transparency, and lighting effects.

**Core Design Requirements**

1. **Backdrop Blur Effect**
   - Use backdrop-filter to achieve background blur
   - Blur radius: 10px (subtle) - 40px (strong)
   - Must add -webkit- prefix for Safari compatibility
   - Examples:
     ```css
     .glass-card {
       backdrop-filter: blur(20px);
       -webkit-backdrop-filter: blur(20px); /* Safari compatibility */
     }

     /* Different blur intensities */
     .glass-light { backdrop-filter: blur(10px); }
     .glass-medium { backdrop-filter: blur(20px); }
     .glass-strong { backdrop-filter: blur(40px); }
     ```

2. **Transparency Hierarchy System**
   - Use rgba to control transparency, creating depth
   - Transparency range: 0.05 (very light) - 0.2 (heavier)
   - Avoid exceeding 0.3 to maintain glass texture
   - Examples:
     ```css
     /* Primary card */
     .glass-primary {
       background: rgba(255, 255, 255, 0.1);
     }

     /* Secondary card (lighter) */
     .glass-secondary {
       background: rgba(255, 255, 255, 0.05);
     }

     /* Emphasis card (slightly darker) */
     .glass-emphasis {
       background: rgba(255, 255, 255, 0.15);
     }

     /* Dark glass variant */
     .glass-dark {
       background: rgba(0, 0, 0, 0.2);
     }
     ```

3. **Edge Glow and Borders**
   - Use semi-transparent borders to create light feel
   - Border transparency: 0.1 - 0.3
   - Border width: 1px (standard) to 2px (emphasis)
   - Examples:
     ```css
     .glass-border {
       border: 1px solid rgba(255, 255, 255, 0.18);
     }

     /* Gradient border (advanced technique) */
     .glass-border-gradient {
       border: 1px solid transparent;
       background-image:
         linear-gradient(white, white),
         linear-gradient(135deg,
           rgba(255,255,255,0.3),
           rgba(255,255,255,0.1),
           rgba(255,255,255,0.2)
         );
       background-origin: border-box;
       background-clip: padding-box, border-box;
     }
     ```

4. **Soft Shadow System**
   - Use low-opacity shadows to create depth
   - Layer multiple shadows for enhanced dimensionality
   - Examples:
     ```css
     .glass-shadow {
       box-shadow:
         0 8px 32px 0 rgba(31, 38, 135, 0.37),
         0 4px 16px 0 rgba(31, 38, 135, 0.2);
     }

     /* Deeper shadow on hover */
     .glass-shadow:hover {
       box-shadow:
         0 12px 48px 0 rgba(31, 38, 135, 0.45),
         0 6px 24px 0 rgba(31, 38, 135, 0.3);
     }

     /* Light shadow (secondary elements) */
     .glass-shadow-light {
       box-shadow: 0 4px 16px 0 rgba(31, 38, 135, 0.2);
     }
     ```

5. **Gradient Background Contrast**
   - Glass effect requires rich background for contrast
   - Use gradient or image backgrounds
   - Examples:
     ```css
     /* Classic purple gradient */
     .glass-bg-purple {
       background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
     }

     /* Multi-color gradient */
     .glass-bg-rainbow {
       background: linear-gradient(135deg,
         #667eea 0%,
         #764ba2 50%,
         #f093fb 100%
       );
     }

     /* Animated gradient */
     .glass-bg-animated {
       background: linear-gradient(
         135deg,
         #667eea,
         #764ba2,
         #f093fb,
         #4facfe
       );
       background-size: 400% 400%;
       animation: gradientShift 15s ease infinite;
     }

     @keyframes gradientShift {
       0%, 100% { background-position: 0% 50%; }
       50% { background-position: 100% 50%; }
     }
     ```

6. **Border Radius and Shapes**
   - Use larger border radius for soft feel
   - Radius range: 12px (small) - 24px (large)
   - Examples:
     ```css
     .glass-rounded-sm { border-radius: 12px; }
     .glass-rounded-md { border-radius: 16px; }
     .glass-rounded-lg { border-radius: 20px; }
     .glass-rounded-xl { border-radius: 24px; }
     ```

7. **Dynamic Particle Background (Optional)**
   - Floating semi-transparent circular elements
   - Use CSS animations for flow effect
   - Examples:
     ```css
     .particle {
       position: absolute;
       border-radius: 50%;
       background: linear-gradient(
         135deg,
         rgba(255, 255, 255, 0.2),
         rgba(255, 255, 255, 0.05)
       );
       animation: float-particle 20s ease-in-out infinite;
     }

     @keyframes float-particle {
       0%, 100% { transform: translate(0, 0) scale(1); }
       25% { transform: translate(30px, -40px) scale(1.1); }
       50% { transform: translate(-20px, -80px) scale(0.9); }
       75% { transform: translate(-40px, -40px) scale(1.05); }
     }
     ```

**Color Scheme (Glass Transparent Texture)**

Primary Colors:
- White glass: rgba(255, 255, 255, 0.05-0.2)
- Border highlight: rgba(255, 255, 255, 0.1-0.3)
- Text primary: #ffffff (white, for dark backgrounds)
- Text secondary: rgba(255, 255, 255, 0.7-0.9)

Background Colors (for contrast):
- Classic purple gradient: #667eea → #764ba2
- Multi-color gradient: #667eea → #764ba2 → #f093fb
- Blue-purple gradient: #667eea → #764ba2 → #f093fb → #4facfe
- Deep blue: #1e3a8a → #1e40af
- Deep purple: #5b21b6 → #7c3aed

Shadow Colors:
- Soft shadow: rgba(31, 38, 135, 0.2-0.45)
- Dark shadow: rgba(0, 0, 0, 0.1-0.3)

Accent Colors:
- Neon blue: #60a5fa
- Neon purple: #a78bfa
- Neon pink: #f472b6

**Key CSS Class Examples**

```css
/* Standard glass card */
.glass-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  padding: 32px;
  transition: all 0.3s ease;
}

.glass-card:hover {
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 0 12px 48px 0 rgba(31, 38, 135, 0.45);
  transform: translateY(-4px);
}

/* Glass button */
.glass-button {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 12px 32px;
  color: #ffffff;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px 0 rgba(31, 38, 135, 0.2);
}

.glass-button:hover {
  background: rgba(255, 255, 255, 0.2);
  box-shadow: 0 6px 24px 0 rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
}

.glass-button:active {
  transform: translateY(0);
  box-shadow: 0 2px 8px 0 rgba(31, 38, 135, 0.2);
}

/* Glass input */
.glass-input {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 14px 18px;
  color: #ffffff;
  font-size: 16px;
  width: 100%;
  transition: all 0.3s ease;
}

.glass-input:focus {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.3);
  outline: none;
  box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.1);
}

.glass-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

/* Glass navigation */
.glass-nav {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(40px);
  -webkit-backdrop-filter: blur(40px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 4px 16px 0 rgba(31, 38, 135, 0.2);
  position: sticky;
  top: 0;
  z-index: 100;
}

/* Glass container background */
.glass-container {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
  min-height: 100vh;
  padding: 48px;
  position: relative;
  overflow: hidden;
}

/* Glass progress bar */
.glass-progress {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 24px;
  height: 8px;
  overflow: hidden;
}

.glass-progress-fill {
  background: linear-gradient(90deg, #60a5fa 0%, #a78bfa 100%);
  height: 100%;
  border-radius: 24px;
  box-shadow: 0 0 16px rgba(96, 165, 250, 0.5);
  transition: width 0.3s ease;
}

/* Glass floating action button */
.glass-fab {
  position: fixed;
  bottom: 32px;
  right: 32px;
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.glass-fab:hover {
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 0 12px 48px 0 rgba(31, 38, 135, 0.45);
  transform: scale(1.1);
}
```

**Spacing System (Based on 8px)**

- xs: 8px (0.5rem)
- sm: 16px (1rem)
- md: 24px (1.5rem)
- lg: 32px (2rem)
- xl: 48px (3rem)
- 2xl: 64px (4rem)
- 3xl: 96px (6rem)

**Font Size System**

Headings:
- h1: 48px-72px (3rem-4.5rem), font-weight: 700-800
- h2: 36px-48px (2.25rem-3rem), font-weight: 700
- h3: 28px-36px (1.75rem-2.25rem), font-weight: 600-700
- h4: 24px-28px (1.5rem-1.75rem), font-weight: 600

Body:
- Large: 18px-20px (1.125rem-1.25rem)
- Standard: 16px-18px (1rem-1.125rem)
- Small: 14px-16px (0.875rem-1rem)
- Extra small: 12px-14px (0.75rem-0.875rem)
- Line height: 1.5-1.7

**Blur Intensity System**

- Extra light: blur(5px) - for subtle effects
- Light: blur(10px) - for buttons, inputs
- Medium: blur(20px) - for cards (most common)
- Strong: blur(30px) - for main containers
- Extra strong: blur(40px) - for navigation, modals

**Transparency Level System**

- Level 1 (lightest): rgba(255, 255, 255, 0.05) - secondary elements
- Level 2: rgba(255, 255, 255, 0.08) - navigation bar
- Level 3: rgba(255, 255, 255, 0.1) - standard cards
- Level 4: rgba(255, 255, 255, 0.15) - emphasis cards
- Level 5 (darkest): rgba(255, 255, 255, 0.2) - hover states

**Important Notes**

- **Must have dark or gradient background for contrast**, otherwise glass effect is not visible
- **backdrop-filter requires -webkit- prefix in Safari**, must add both
- **Transparency should not be too high**, avoid exceeding 0.3 to maintain glass texture
- **Border transparency should be lower than background transparency**, maintain delicate light feel
- **Use larger border radius** (12px-24px), avoid sharp corners
- **Shadow colors use low-opacity black or blue**, avoid colored shadows
- **Text must use white or light colors**, ensure readability on dark backgrounds
- **Avoid pure black or pure white backgrounds**, use gradients or images
- **Blur radius should not be too large**, avoid exceeding 40px
- **Animation transition time recommended 0.3s**, maintain smooth feel
- **Hover states should increase transparency and shadow**, enhance interactive feedback
- **When layering multiple glass elements, decrease transparency per layer**
- **When using position: sticky, pay attention to z-index hierarchy**
- **Mobile performance consideration**: too many backdrop-filters may affect performance

**Things to Avoid**

- ❌ Don't use glass effect on light backgrounds
- ❌ Don't use excessive transparency (over 0.3)
- ❌ Don't use blurred shadows (use crisp multi-layer shadows)
- ❌ Don't use sharp corners (use border radius)
- ❌ Don't ignore Safari compatibility (must add -webkit- prefix)
- ❌ Don't use strong blur directly on text
- ❌ Don't over-nest glass elements (affects performance)
- ❌ Don't use overly dark border colors
- ❌ Don't use dark background images inside glass elements
- ❌ Don't use too many dynamic particles (affects performance)
- ❌ Don't mix glass effects with other heavy effects (like large shadows)
- ❌ Don't use strong blur on small elements

**Performance Optimization Suggestions**

- Limit backdrop-filter usage (recommend no more than 10 visible elements)
- Use will-change property to pre-optimize animated elements
- Consider reducing blur intensity on mobile
- Use CSS containment to isolate repaint areas
- Avoid excessive use of backdrop-filter in scroll containers
