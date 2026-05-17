# Custom Prompt

## 中文版本 (zh-CN)

请使用 TailwindCSS 创建一个沉浸式的街机 CRT（阴极射线管）风格界面组件。该界面应唤起 80-90 年代街机游戏厅的复古氛围，包含扫描线、屏幕曲率、霓虹辉光、像素化字体以及 RGB 色差故障效果。

**核心设计要求**

1. **CRT 扫描线与荧光屏纹理**
   - 在所有内容之上覆盖一层扫描线和微小的网格纹理，模拟真实的物理屏幕像素点
   - 扫描线间距：4px，使用半透明黑色
   - 示例：
     ```css
     .scanlines {
       background: linear-gradient(
         to bottom,
         rgba(255, 255, 255, 0),
         rgba(255, 255, 255, 0) 50%,
         rgba(0, 0, 0, 0.2) 50%,
         rgba(0, 0, 0, 0.2)
       );
       background-size: 100% 4px;
       pointer-events: none;
       position: absolute;
       inset: 0;
       z-index: 50;
     }
     ```

2. **屏幕发光与晕影效果**
   - 通过内阴影模拟 CRT 显示器的曲面玻璃反光和四角变暗的晕影效果
   - 使用径向渐变增加立体感
   - 示例：
     ```css
     .crt-vignette {
       box-shadow: inset 0 0 100px rgba(0, 0, 0, 0.9);
       background: radial-gradient(
         circle,
         rgba(18, 16, 16, 0) 60%,
         rgba(0, 0, 0, 0.4) 100%
       );
       position: absolute;
       inset: 0;
       pointer-events: none;
       z-index: 40;
     }
     ```

3. **文本辉光与溢出效果**
   - 所有高亮文本和 UI 元素必须带有特定颜色的多层 `text-shadow`
   - 模拟电子束激发荧光粉产生的晕光
   - 示例：
     ```css
     .neon-text-glow {
       text-shadow:
         0 0 2px #fff,
         0 0 5px #00ffff,
         0 0 10px #00ffff,
         0 0 20px #00ffff,
         0 0 40px #00ffff;
     }

     .neon-pink-glow {
       text-shadow:
         0 0 2px #fff,
         0 0 5px #ff00ff,
         0 0 10px #ff00ff,
         0 0 20px #ff00ff;
     }

     .neon-green-glow {
       text-shadow:
         0 0 2px #fff,
         0 0 5px #39ff14,
         0 0 10px #39ff14,
         0 0 20px #39ff14;
     }
     ```

4. **RGB 色差故障效果**
   - 为标题或强调元素添加轻微的红蓝色彩偏移
   - 模拟显示器信号不稳定的故障美学
   - 示例：
     ```css
     .rgb-glitch {
       position: relative;
       text-shadow:
         2px 0 rgba(255, 0, 0, 0.7),
         -2px 0 rgba(0, 0, 255, 0.7);
     }

     @keyframes glitch-skew {
       0%, 100% { transform: skewX(0deg); }
       20% { transform: skewX(-0.5deg); }
       40% { transform: skewX(0.5deg); }
       60% { transform: skewX(-0.3deg); }
       80% { transform: skewX(0.3deg); }
     }

     .rgb-glitch-animated {
       animation: glitch-skew 3s infinite linear alternate-reverse;
     }
     ```

5. **屏幕闪烁动画**
   - 整个屏幕或特定旧化元素应具有极轻微的透明度或亮度闪烁动画
   - 模拟 60Hz 显示器的微闪
   - 示例：
     ```css
     @keyframes screen-flicker {
       0% { opacity: 0.98; }
       5% { opacity: 0.95; }
       10% { opacity: 0.99; }
       15% { opacity: 0.97; }
       100% { opacity: 0.98; }
     }

     .flicker-effect {
       animation: screen-flicker 0.15s infinite;
     }

     /* 游标闪烁 */
     @keyframes cursor-blink {
       0%, 100% { opacity: 1; }
       50% { opacity: 0; }
     }

     .cursor-blink {
       animation: cursor-blink 1s steps(1) infinite;
     }
     ```

6. **像素化边框与字体**
   - 完全摒弃圆角（或仅使用极其夸张的圆角模拟显像管物理外壳）
   - UI 元素应使用双线或块状边框
   - 示例：
     ```css
     .pixel-border {
       border: 4px solid #39ff14;
       border-style: double;
       image-rendering: pixelated;
     }

     .pixel-box-shadow {
       box-shadow:
         4px 0 0 #39ff14,
         -4px 0 0 #39ff14,
         0 4px 0 #39ff14,
         0 -4px 0 #39ff14;
     }

     /* 模拟像素字体渲染 */
     .pixel-font {
       font-family: 'VT323', 'Press Start 2P', 'Courier New', monospace;
       image-rendering: pixelated;
       -webkit-font-smoothing: none;
       -moz-osx-font-smoothing: grayscale;
     }
     ```

7. **霓虹边框发光**
   - 使用多层 box-shadow 创造霓虹灯管效果
   - 内外发光组合增加深度感
   - 示例：
     ```css
     .neon-border {
       border: 2px solid #00ffff;
       box-shadow:
         0 0 5px #00ffff,
         0 0 10px #00ffff,
         0 0 20px #00ffff,
         inset 0 0 5px rgba(0, 255, 255, 0.2);
     }

     .neon-border-pink {
       border: 2px solid #ff00ff;
       box-shadow:
         0 0 5px #ff00ff,
         0 0 10px #ff00ff,
         0 0 20px #ff00ff,
         inset 0 0 5px rgba(255, 0, 255, 0.2);
     }
     ```

**配色方案（街机霓虹）**

背景色：
- 深空黑（屏幕关闭/深处）: #050505
- 显像管灰（屏幕底色）: #111111, #0a0a0a
- 扫描线暗部: rgba(0, 0, 0, 0.2-0.3)

主色调（霓虹色）：
- 赛博青（文本/边框）: #00FFFF, #00e5e5
- 激光粉（强调/动作）: #FF00FF, #e500e5
- 荧光绿（成功/数据）: #39FF14, #32e512
- 霓虹橙: #FF6600, #ff8533

功能色：
- 警告黄: #FFFF00, #e5e500
- 系统红（错误/高危）: #FF2A2A, #ff4444
- 纯白（极高亮光芯）: #FFFFFF
- 暗灰（次要文字）: #888888, #666666

**关键 CSS 类示例**

```css
/* 街机主容器 */
.arcade-container {
  position: relative;
  overflow: hidden;
  background: #111111;
  font-family: 'VT323', 'Courier New', monospace;
  color: #00ffff;
  border-radius: 20px;
  box-shadow:
    0 0 0 10px #222,
    0 0 0 20px #111,
    0 0 50px rgba(0, 255, 255, 0.2);
}

/* 复古像素按钮 */
.btn-retro {
  position: relative;
  padding: 12px 32px;
  background: transparent;
  border: 4px solid #ff00ff;
  color: #ff00ff;
  font-family: 'VT323', monospace;
  font-size: 18px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  cursor: pointer;
  text-shadow: 0 0 8px rgba(255, 0, 255, 0.8);
  box-shadow:
    0 0 10px rgba(255, 0, 255, 0.4),
    inset 0 0 10px rgba(255, 0, 255, 0.2);
  transition: all 0.1s ease;
}

.btn-retro:hover {
  background: #ff00ff;
  color: #000000;
  border-color: #ff00ff;
  text-shadow: none;
  box-shadow: 0 0 30px rgba(255, 0, 255, 0.8);
}

.btn-retro:active {
  transform: scale(0.95);
  box-shadow: 0 0 15px rgba(255, 0, 255, 0.6);
}

/* INSERT COIN 按钮（特殊动画） */
.btn-insert-coin {
  animation: coin-pulse 1.5s ease-in-out infinite;
}

@keyframes coin-pulse {
  0%, 100% {
    box-shadow: 0 0 10px rgba(255, 255, 0, 0.4);
    border-color: #ffff00;
  }
  50% {
    box-shadow: 0 0 30px rgba(255, 255, 0, 0.8);
    border-color: #ffffff;
  }
}

/* 系统状态面板 */
.panel-hud {
  border: 2px solid #39ff14;
  background: rgba(57, 255, 20, 0.05);
  padding: 16px;
  position: relative;
}

.panel-hud::before {
  content: "SYSTEM_READY";
  position: absolute;
  top: -10px;
  left: 16px;
  background: #111111;
  padding: 0 8px;
  font-size: 12px;
  color: #39ff14;
  font-weight: bold;
  letter-spacing: 0.1em;
}

/* 加载条动画 */
.loader-scan {
  width: 100%;
  height: 16px;
  border: 2px solid #ffff00;
  padding: 2px;
  background: #111111;
}

.loader-fill {
  height: 100%;
  background: #ffff00;
  box-shadow: 0 0 10px #ffff00;
  animation: load-progress 2s steps(10) infinite;
}

@keyframes load-progress {
  0% { width: 0%; }
  100% { width: 100%; }
}

/* 计分板显示 */
.scoreboard {
  font-family: 'VT323', monospace;
  font-size: 48px;
  color: #ffff00;
  text-shadow:
    0 0 5px #ffff00,
    0 0 10px #ffff00,
    0 0 20px #ff6600;
  letter-spacing: 0.1em;
}

/* 终端输入框 */
.terminal-input {
  background: #050505;
  border: 2px solid #00ffff;
  color: #00ffff;
  font-family: 'VT323', monospace;
  padding: 8px 12px;
  box-shadow: inset 0 0 10px rgba(0, 255, 255, 0.1);
}

.terminal-input:focus {
  outline: none;
  border-color: #ffffff;
  box-shadow:
    0 0 10px rgba(0, 255, 255, 0.5),
    inset 0 0 10px rgba(0, 255, 255, 0.2);
}

.terminal-input::placeholder {
  color: #00ffff;
  opacity: 0.5;
}
```

**Tailwind CSS 配置**

如使用 Tailwind CSS，添加以下配置：

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        'arcade': ['VT323', 'Press Start 2P', 'Courier New', 'monospace'],
      },
      colors: {
        'crt-black': '#050505',
        'crt-gray': '#111111',
        'neon-cyan': '#00ffff',
        'neon-pink': '#ff00ff',
        'neon-green': '#39ff14',
        'neon-yellow': '#ffff00',
        'neon-orange': '#ff6600',
        'neon-red': '#ff2a2a',
      },
      boxShadow: {
        'neon-cyan': '0 0 10px #00ffff, 0 0 20px #00ffff',
        'neon-pink': '0 0 10px #ff00ff, 0 0 20px #ff00ff',
        'neon-green': '0 0 10px #39ff14, 0 0 20px #39ff14',
      },
      animation: {
        'flicker': 'screen-flicker 0.15s infinite',
        'cursor-blink': 'cursor-blink 1s steps(1) infinite',
        'coin-pulse': 'coin-pulse 1.5s ease-in-out infinite',
      },
    },
  },
}
```

**重要提示**

- 字体选择：优先使用等宽字体（如 'VT323', 'Press Start 2P', 'Courier New'）
- 图像处理：所有图片应使用 `mix-blend-mode: screen` 或 `overlay` 融入 CRT 背景
- 交互反馈：所有点击和悬停都应有即时的、高对比度的颜色反转或亮度爆发
- 滚动条：自定义滚动条样式，使其看起来像粗大的滑块或完全隐藏
- Z-Index 管理：确保扫描线和晕影图层始终处于最顶层且具有 `pointer-events: none`
- 性能优化：大量的 `box-shadow` 和 `text-shadow` 可能影响渲染性能，适度使用 `will-change`
- 无障碍性：由于包含闪烁和高对比度色彩，请提供「减少动效」的开关
- 布局结构：布局应倾向于网格化（Grid），模拟早期 GUI 的刚性结构


---

## English Version (en-US)

Please use TailwindCSS to create an immersive Arcade CRT (Cathode Ray Tube) style interface component. The interface should evoke the retro atmosphere of 80s-90s arcade halls, featuring scanlines, screen curvature, neon glow, pixelated fonts, and RGB chromatic aberration effects.

**Core Design Requirements**

1. **CRT Scanlines & Phosphor Mesh**
   - Overlay all content with scanlines and tiny mesh texture to simulate real physical screen pixels
   - Scanline spacing: 4px, using semi-transparent black
   - Example:
     ```css
     .scanlines {
       background: linear-gradient(
         to bottom,
         rgba(255, 255, 255, 0),
         rgba(255, 255, 255, 0) 50%,
         rgba(0, 0, 0, 0.2) 50%,
         rgba(0, 0, 0, 0.2)
       );
       background-size: 100% 4px;
       pointer-events: none;
       position: absolute;
       inset: 0;
       z-index: 50;
     }
     ```

2. **Screen Glow & Vignette Effect**
   - Simulate CRT monitor's curved glass reflection and darkened corners using inner shadows
   - Use radial gradients to add depth
   - Example:
     ```css
     .crt-vignette {
       box-shadow: inset 0 0 100px rgba(0, 0, 0, 0.9);
       background: radial-gradient(
         circle,
         rgba(18, 16, 16, 0) 60%,
         rgba(0, 0, 0, 0.4) 100%
       );
       position: absolute;
       inset: 0;
       pointer-events: none;
       z-index: 40;
     }
     ```

3. **Text Bloom & Bleed Effect**
   - All highlighted text and UI elements must have multi-layer `text-shadow` with specific colors
   - Simulate the halo produced by electron beams exciting phosphor
   - Example:
     ```css
     .neon-text-glow {
       text-shadow:
         0 0 2px #fff,
         0 0 5px #00ffff,
         0 0 10px #00ffff,
         0 0 20px #00ffff,
         0 0 40px #00ffff;
     }

     .neon-pink-glow {
       text-shadow:
         0 0 2px #fff,
         0 0 5px #ff00ff,
         0 0 10px #ff00ff,
         0 0 20px #ff00ff;
     }

     .neon-green-glow {
       text-shadow:
         0 0 2px #fff,
         0 0 5px #39ff14,
         0 0 10px #39ff14,
         0 0 20px #39ff14;
     }
     ```

4. **RGB Split / Chromatic Aberration**
   - Add slight red-blue color offsets to titles or emphasized elements
   - Simulate the glitch aesthetic of unstable monitor signals
   - Example:
     ```css
     .rgb-glitch {
       position: relative;
       text-shadow:
         2px 0 rgba(255, 0, 0, 0.7),
         -2px 0 rgba(0, 0, 255, 0.7);
     }

     @keyframes glitch-skew {
       0%, 100% { transform: skewX(0deg); }
       20% { transform: skewX(-0.5deg); }
       40% { transform: skewX(0.5deg); }
       60% { transform: skewX(-0.3deg); }
       80% { transform: skewX(0.3deg); }
     }

     .rgb-glitch-animated {
       animation: glitch-skew 3s infinite linear alternate-reverse;
     }
     ```

5. **Screen Flicker Animation**
   - The entire screen or specific aged elements should have very slight opacity or brightness flicker
   - Simulate 60Hz monitor micro-flicker
   - Example:
     ```css
     @keyframes screen-flicker {
       0% { opacity: 0.98; }
       5% { opacity: 0.95; }
       10% { opacity: 0.99; }
       15% { opacity: 0.97; }
       100% { opacity: 0.98; }
     }

     .flicker-effect {
       animation: screen-flicker 0.15s infinite;
     }

     /* Cursor blink */
     @keyframes cursor-blink {
       0%, 100% { opacity: 1; }
       50% { opacity: 0; }
     }

     .cursor-blink {
       animation: cursor-blink 1s steps(1) infinite;
     }
     ```

6. **Pixel Borders & Typography**
   - Completely abandon rounded corners (or use exaggerated ones to simulate physical monitor casing)
   - UI elements should use double lines or blocky borders
   - Example:
     ```css
     .pixel-border {
       border: 4px solid #39ff14;
       border-style: double;
       image-rendering: pixelated;
     }

     .pixel-box-shadow {
       box-shadow:
         4px 0 0 #39ff14,
         -4px 0 0 #39ff14,
         0 4px 0 #39ff14,
         0 -4px 0 #39ff14;
     }

     /* Pixel font rendering */
     .pixel-font {
       font-family: 'VT323', 'Press Start 2P', 'Courier New', monospace;
       image-rendering: pixelated;
       -webkit-font-smoothing: none;
       -moz-osx-font-smoothing: grayscale;
     }
     ```

7. **Neon Border Glow**
   - Use multi-layer box-shadow to create neon tube effect
   - Combine inner and outer glow for depth
   - Example:
     ```css
     .neon-border {
       border: 2px solid #00ffff;
       box-shadow:
         0 0 5px #00ffff,
         0 0 10px #00ffff,
         0 0 20px #00ffff,
         inset 0 0 5px rgba(0, 255, 255, 0.2);
     }

     .neon-border-pink {
       border: 2px solid #ff00ff;
       box-shadow:
         0 0 5px #ff00ff,
         0 0 10px #ff00ff,
         0 0 20px #ff00ff,
         inset 0 0 5px rgba(255, 0, 255, 0.2);
     }
     ```

**Color Scheme (Arcade Neon)**

Backgrounds:
- Deep Space Black (Screen Off/Deep): #050505
- CRT Tube Grey (Screen Base): #111111, #0a0a0a
- Scanline Dark: rgba(0, 0, 0, 0.2-0.3)

Primary Colors (Neon):
- Cyber Cyan (Text/Borders): #00FFFF, #00e5e5
- Hot Pink (Emphasis/Action): #FF00FF, #e500e5
- Matrix Green (Success/Data): #39FF14, #32e512
- Neon Orange: #FF6600, #ff8533

Functional Colors:
- Warning Yellow: #FFFF00, #e5e500
- System Red (Error/High Risk): #FF2A2A, #ff4444
- Pure White (Extreme Highlight): #FFFFFF
- Dark Gray (Secondary Text): #888888, #666666

**Key CSS Class Examples**

```css
/* Arcade Main Container */
.arcade-container {
  position: relative;
  overflow: hidden;
  background: #111111;
  font-family: 'VT323', 'Courier New', monospace;
  color: #00ffff;
  border-radius: 20px;
  box-shadow:
    0 0 0 10px #222,
    0 0 0 20px #111,
    0 0 50px rgba(0, 255, 255, 0.2);
}

/* Retro Pixel Button */
.btn-retro {
  position: relative;
  padding: 12px 32px;
  background: transparent;
  border: 4px solid #ff00ff;
  color: #ff00ff;
  font-family: 'VT323', monospace;
  font-size: 18px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  cursor: pointer;
  text-shadow: 0 0 8px rgba(255, 0, 255, 0.8);
  box-shadow:
    0 0 10px rgba(255, 0, 255, 0.4),
    inset 0 0 10px rgba(255, 0, 255, 0.2);
  transition: all 0.1s ease;
}

.btn-retro:hover {
  background: #ff00ff;
  color: #000000;
  border-color: #ff00ff;
  text-shadow: none;
  box-shadow: 0 0 30px rgba(255, 0, 255, 0.8);
}

.btn-retro:active {
  transform: scale(0.95);
  box-shadow: 0 0 15px rgba(255, 0, 255, 0.6);
}

/* INSERT COIN Button (Special Animation) */
.btn-insert-coin {
  animation: coin-pulse 1.5s ease-in-out infinite;
}

@keyframes coin-pulse {
  0%, 100% {
    box-shadow: 0 0 10px rgba(255, 255, 0, 0.4);
    border-color: #ffff00;
  }
  50% {
    box-shadow: 0 0 30px rgba(255, 255, 0, 0.8);
    border-color: #ffffff;
  }
}

/* Status Panel */
.panel-hud {
  border: 2px solid #39ff14;
  background: rgba(57, 255, 20, 0.05);
  padding: 16px;
  position: relative;
}

.panel-hud::before {
  content: "SYSTEM_READY";
  position: absolute;
  top: -10px;
  left: 16px;
  background: #111111;
  padding: 0 8px;
  font-size: 12px;
  color: #39ff14;
  font-weight: bold;
  letter-spacing: 0.1em;
}

/* Loading Bar Animation */
.loader-scan {
  width: 100%;
  height: 16px;
  border: 2px solid #ffff00;
  padding: 2px;
  background: #111111;
}

.loader-fill {
  height: 100%;
  background: #ffff00;
  box-shadow: 0 0 10px #ffff00;
  animation: load-progress 2s steps(10) infinite;
}

@keyframes load-progress {
  0% { width: 0%; }
  100% { width: 100%; }
}

/* Scoreboard Display */
.scoreboard {
  font-family: 'VT323', monospace;
  font-size: 48px;
  color: #ffff00;
  text-shadow:
    0 0 5px #ffff00,
    0 0 10px #ffff00,
    0 0 20px #ff6600;
  letter-spacing: 0.1em;
}

/* Terminal Input */
.terminal-input {
  background: #050505;
  border: 2px solid #00ffff;
  color: #00ffff;
  font-family: 'VT323', monospace;
  padding: 8px 12px;
  box-shadow: inset 0 0 10px rgba(0, 255, 255, 0.1);
}

.terminal-input:focus {
  outline: none;
  border-color: #ffffff;
  box-shadow:
    0 0 10px rgba(0, 255, 255, 0.5),
    inset 0 0 10px rgba(0, 255, 255, 0.2);
}

.terminal-input::placeholder {
  color: #00ffff;
  opacity: 0.5;
}
```

**Tailwind CSS Configuration**

If using Tailwind CSS, add the following configuration:

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        'arcade': ['VT323', 'Press Start 2P', 'Courier New', 'monospace'],
      },
      colors: {
        'crt-black': '#050505',
        'crt-gray': '#111111',
        'neon-cyan': '#00ffff',
        'neon-pink': '#ff00ff',
        'neon-green': '#39ff14',
        'neon-yellow': '#ffff00',
        'neon-orange': '#ff6600',
        'neon-red': '#ff2a2a',
      },
      boxShadow: {
        'neon-cyan': '0 0 10px #00ffff, 0 0 20px #00ffff',
        'neon-pink': '0 0 10px #ff00ff, 0 0 20px #ff00ff',
        'neon-green': '0 0 10px #39ff14, 0 0 20px #39ff14',
      },
      animation: {
        'flicker': 'screen-flicker 0.15s infinite',
        'cursor-blink': 'cursor-blink 1s steps(1) infinite',
        'coin-pulse': 'coin-pulse 1.5s ease-in-out infinite',
      },
    },
  },
}
```

**Important Notes**

- Font Selection: Prioritize monospaced fonts (e.g., 'VT323', 'Press Start 2P', 'Courier New')
- Image Blending: All images should use `mix-blend-mode: screen` or `overlay` to blend into CRT background
- Interaction Feedback: All clicks and hovers should have immediate, high-contrast color inversion or brightness bursts
- Scrollbars: Customize scrollbars to look like chunky sliders or hide them completely
- Z-Index Management: Ensure scanlines and vignette layers are always at top z-index with `pointer-events: none`
- Performance: Heavy use of `box-shadow` and `text-shadow` may affect rendering; use `will-change` moderately
- Accessibility: Due to flickering and high-contrast colors, provide a "Reduced Motion" toggle
- Grid Layout: Layouts should lean towards Grid systems, simulating the rigid structure of early GUIs
