# Custom Prompt: Sci-Fi HUD（科幻擡头显示）

## 中文版本 (zh-CN)

### 1. 设计哲学与核心原则

**Sci-Fi HUD（科幻擡头显示）**风格源自电影、游戏中的未来科技界面，特别是星际飞船、机甲驾驶舱、战术指挥中心的全息显示系统。这种风格的核心在于**信息即界面**，所有 UI 元素都以**发光的几何图形、透明面板、实时数据流**的形式呈现，营造"正在操作高科技设备"的沉浸感。

**设计原则**：
- **深空背景**：使用极深的蓝灰色背景，模拟太空环境或暗色指挥室
- **发光几何**：所有元素使用青色/蓝绿色发光边框，创造全息投影感
- **信息密集**：界面承载大量实时数据，但通过分层和模块化保持可读性
- **实时动态**：雷达扫描、数据流滚动、状态脉冲等动效传递"系统运行中"的感觉
- **半透明材质**：面板使用玻璃态效果（glassmorphism）+模糊背景

### 2. 核心设计要求

#### 2.1 深空配色系统（Deep Space Color Palette）

Sci-Fi HUD 的配色系统以**极深的冷色调背景**和**高亮青色发光**为核心，模拟太空舰桥环境。

**主色调（Primary Colors）**：
- **深海军蓝（Deep Navy）**：`#020617` - 主背景
- **深蓝灰（Dark Slate）**：`#0f172a` - 面板背景
- **深石板（Darker Slate）**：`#1e293b` - 卡片背景

**HUD 发光色（HUD Accent Colors）**：
- **主青色（Primary Cyan）**：`#06B6D4` - 主要边框、按钮
- **亮蓝（Bright Blue）**：`#0EA5E9` - 强调色、扫描线
- **霓虹青（Neon Cyan）**：`#22D3EE` - 高亮、雷达扫描

**状态色（Status Colors）**：
- **成功绿（Success Green）**：`#22C55E`, `#10B981` - 系统正常、连接成功
- **警告橙（Warning Orange）**：`#F97316`, `#FB923C` - 警告状态
- **警告黄（Alert Yellow）**：`#EAB308`, `#FBBF24` - 注意事项
- **危险红（Danger Red）**：`#EF4444`, `#DC2626` - 紧急状态、错误
- **离线灰（Offline Gray）**：`#6B7280`, `#4B5563` - 禁用、离线

**文本色（Text Colors）**：
- **主文本（Primary Text）**：`#E5F2FF` - 标题、重要文字
- **次文本（Secondary Text）**：`#94A3B8` - 正文、标签
- **辅助文本（Helper Text）**：`#6B7280` - 说明文字、时间戳

**完整 CSS 变量定义**：
```css
:root {
  /* 背景色 */
  --hud-bg-deep: #020617;
  --hud-bg-dark: #0f172a;
  --hud-bg-panel: #1e293b;
  --hud-bg-card: rgba(15, 23, 42, 0.85);

  /* HUD 发光色 */
  --hud-cyan: #06B6D4;
  --hud-cyan-bright: #0EA5E9;
  --hud-cyan-neon: #22D3EE;

  /* 状态色 */
  --hud-success: #22C55E;
  --hud-success-bright: #10B981;
  --hud-warning: #F97316;
  --hud-alert: #EAB308;
  --hud-danger: #EF4444;
  --hud-danger-dark: #DC2626;
  --hud-offline: #6B7280;

  /* 文本色 */
  --hud-text-primary: #E5F2FF;
  --hud-text-secondary: #94A3B8;
  --hud-text-helper: #6B7280;

  /* 发光效果 */
  --hud-glow-cyan: 0 0 20px rgba(6, 182, 212, 0.5);
  --hud-glow-cyan-strong: 0 0 30px rgba(34, 211, 238, 0.7);
  --hud-glow-green: 0 0 20px rgba(34, 197, 94, 0.5);
  --hud-glow-red: 0 0 20px rgba(239, 68, 68, 0.5);

  /* 边框 */
  --hud-border-thin: 1px;
  --hud-border-medium: 2px;
  --hud-border-thick: 3px;

  /* 圆角 */
  --hud-radius-sm: 4px;
  --hud-radius-md: 8px;
  --hud-radius-lg: 12px;

  /* 字体 */
  --hud-font: 'Orbitron', 'Rajdhani', 'Exo 2', 'Roboto Mono', monospace;
}
```

#### 2.2 半透明玻璃面板系统（Translucent Glass Panel System）

所有 HUD 面板使用**半透明背景 + 模糊效果 + 发光边框**，模拟全息投影或强化玻璃。

```css
/* 基础 HUD 面板 */
.hud-panel {
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(6, 182, 212, 0.3);
  border-radius: var(--hud-radius-md);
  padding: 1.5rem;
  box-shadow:
    0 4px 24px rgba(0, 0, 0, 0.4),
    inset 0 1px 0 rgba(148, 163, 184, 0.1);
  transition: all 0.3s ease;
}

.hud-panel:hover {
  border-color: rgba(6, 182, 212, 0.6);
  box-shadow:
    0 6px 32px rgba(0, 0, 0, 0.5),
    var(--hud-glow-cyan);
  transform: translateY(-2px);
}

/* 强调面板（带角标） */
.hud-panel-accent {
  position: relative;
  background: rgba(15, 23, 42, 0.9);
  border: 2px solid var(--hud-cyan);
  box-shadow:
    0 8px 40px rgba(6, 182, 212, 0.2),
    var(--hud-glow-cyan);
}

/* L 型角标 */
.hud-panel-accent::before,
.hud-panel-accent::after {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  border: 2px solid var(--hud-cyan-neon);
}

.hud-panel-accent::before {
  top: -2px;
  left: -2px;
  border-right: none;
  border-bottom: none;
}

.hud-panel-accent::after {
  bottom: -2px;
  right: -2px;
  border-left: none;
  border-top: none;
}

/* 切角面板 */
.hud-panel-clipped {
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(6, 182, 212, 0.3);
  clip-path: polygon(
    0 12px, 12px 0,
    calc(100% - 12px) 0, 100% 12px,
    100% calc(100% - 12px), calc(100% - 12px) 100%,
    12px 100%, 0 calc(100% - 12px)
  );
  padding: 1.5rem;
}

/* 扫描线背景 */
.hud-panel-scanline {
  position: relative;
  overflow: hidden;
}

.hud-panel-scanline::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 100%;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(148, 163, 184, 0.03) 2px,
    rgba(148, 163, 184, 0.03) 4px
  );
  pointer-events: none;
}
```

#### 2.3 雷达扫描系统（Radar Scanning System）

雷达是 Sci-Fi HUD 的标志性元素，包含**同心圆网格、旋转扫描扇、目标光点**。

```css
/* 雷达容器 */
.hud-radar-container {
  position: relative;
  width: 400px;
  height: 400px;
  background: radial-gradient(
    circle,
    rgba(6, 182, 212, 0.05) 0%,
    transparent 70%
  );
  border-radius: 50%;
  overflow: hidden;
}

/* 雷达 SVG */
.hud-radar-svg {
  width: 100%;
  height: 100%;
}

/* 雷达扫描扇动画 */
.hud-radar-sweep {
  transform-origin: 50% 50%;
  animation: radarSweep 6s linear infinite;
}

@keyframes radarSweep {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* 雷达中心脉冲 */
.hud-radar-center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 12px;
  height: 12px;
}

.hud-radar-pulse {
  width: 100%;
  height: 100%;
  background: var(--hud-cyan-neon);
  border-radius: 50%;
  box-shadow: var(--hud-glow-cyan-strong);
  animation: radarPulse 2s ease-in-out infinite;
}

@keyframes radarPulse {
  0%, 100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.5);
    opacity: 0.5;
  }
}

/* 目标光点 */
.hud-blip {
  animation: blipPulse 1.5s ease-in-out infinite;
}

@keyframes blipPulse {
  0%, 100% {
    opacity: 1;
    r: 4;
  }
  50% {
    opacity: 0.6;
    r: 6;
  }
}

/* 雷达网格线 */
.hud-radar-grid {
  stroke: rgba(14, 165, 233, 0.2);
  stroke-width: 1;
  fill: none;
}
```

#### 2.4 数据流与日志系统（Data Stream & Log System）

实时滚动的数据日志是 HUD 的关键元素，显示系统状态和事件。

```css
/* 数据流容器 */
.hud-data-stream {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  max-height: 400px;
  overflow-y: auto;
  padding-right: 0.5rem;
  font-family: 'Roboto Mono', monospace;
  font-size: 0.875rem;
}

/* 隐藏滚动条但保持功能 */
.hud-data-stream::-webkit-scrollbar {
  width: 4px;
}

.hud-data-stream::-webkit-scrollbar-track {
  background: rgba(15, 23, 42, 0.5);
}

.hud-data-stream::-webkit-scrollbar-thumb {
  background: rgba(6, 182, 212, 0.3);
  border-radius: 2px;
}

.hud-data-stream::-webkit-scrollbar-thumb:hover {
  background: rgba(6, 182, 212, 0.5);
}

/* 数据行 */
.hud-data-line {
  display: flex;
  gap: 0.75rem;
  padding: 0.5rem;
  background: rgba(30, 41, 59, 0.3);
  border-left: 2px solid rgba(148, 163, 184, 0.2);
  color: var(--hud-text-secondary);
  transition: all 0.2s ease;
  animation: dataLineSlideIn 0.3s ease-out;
}

@keyframes dataLineSlideIn {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.hud-data-line:hover {
  background: rgba(30, 41, 59, 0.5);
  border-left-color: var(--hud-cyan);
}

/* 数据时间戳 */
.hud-data-timestamp {
  color: var(--hud-cyan);
  font-weight: 600;
  min-width: 70px;
  flex-shrink: 0;
}

/* 数据文本 */
.hud-data-text {
  color: var(--hud-text-secondary);
  flex: 1;
}

/* 成功状态行 */
.hud-data-success {
  border-left-color: var(--hud-success);
}

.hud-data-success .hud-data-text {
  color: var(--hud-success);
}

/* 警告状态行 */
.hud-data-warning {
  border-left-color: var(--hud-warning);
}

.hud-data-warning .hud-data-text {
  color: var(--hud-warning);
}

/* 错误状态行 */
.hud-data-error {
  border-left-color: var(--hud-danger);
  background: rgba(239, 68, 68, 0.1);
}

.hud-data-error .hud-data-text {
  color: var(--hud-danger);
}
```

#### 2.5 状态指示器系统（Status Indicator System）

状态指示器使用**发光圆点**和**脉冲动画**显示系统状态。

```css
/* 基础状态指示器 */
.hud-status-indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  position: relative;
  animation: statusPulse 2s ease-in-out infinite;
}

/* 在线状态（绿色） */
.hud-status-online {
  background: var(--hud-success);
  box-shadow:
    0 0 10px var(--hud-success),
    0 0 20px rgba(34, 197, 94, 0.5);
}

/* 警告状态（橙色） */
.hud-status-warning {
  background: var(--hud-warning);
  box-shadow:
    0 0 10px var(--hud-warning),
    0 0 20px rgba(249, 115, 22, 0.5);
}

/* 危险状态（红色） */
.hud-status-danger {
  background: var(--hud-danger);
  box-shadow:
    0 0 10px var(--hud-danger),
    0 0 20px rgba(239, 68, 68, 0.5);
  animation: statusPulseFast 1s ease-in-out infinite;
}

/* 离线状态（灰色） */
.hud-status-offline {
  background: var(--hud-offline);
  box-shadow: none;
  animation: none;
}

/* 状态脉冲动画 */
@keyframes statusPulse {
  0%, 100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.2);
    opacity: 0.8;
  }
}

@keyframes statusPulseFast {
  0%, 100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.3);
    opacity: 0.6;
  }
}

/* 状态标签 */
.hud-status-label {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--hud-text-secondary);
}
```

#### 2.6 进度条与资源指示器（Progress Bars & Resource Indicators）

使用**渐变填充**和**发光效果**显示资源状态。

```css
/* 进度条容器 */
.hud-bar {
  position: relative;
  width: 100%;
  height: 8px;
  background: rgba(30, 41, 59, 0.5);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 4px;
  overflow: hidden;
}

/* 进度条填充 */
.hud-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--hud-cyan), var(--hud-cyan-bright));
  box-shadow: 0 0 10px currentColor;
  transition: width 0.5s ease-out;
  position: relative;
}

/* 进度条发光动画 */
.hud-bar-fill::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.4),
    transparent
  );
  animation: barShine 2s ease-in-out infinite;
}

@keyframes barShine {
  to {
    left: 100%;
  }
}

/* 不同状态的进度条 */
.hud-bar-blue {
  --hud-bar-color: var(--hud-cyan);
  background: linear-gradient(90deg, #0EA5E9, #06B6D4);
}

.hud-bar-cyan {
  --hud-bar-color: var(--hud-cyan-neon);
  background: linear-gradient(90deg, #22D3EE, #0EA5E9);
}

.hud-bar-green {
  --hud-bar-color: var(--hud-success);
  background: linear-gradient(90deg, #10B981, #22C55E);
}

.hud-bar-yellow {
  --hud-bar-color: var(--hud-alert);
  background: linear-gradient(90deg, #FBBF24, #EAB308);
}

.hud-bar-orange {
  --hud-bar-color: var(--hud-warning);
  background: linear-gradient(90deg, #FB923C, #F97316);
}

.hud-bar-red {
  --hud-bar-color: var(--hud-danger);
  background: linear-gradient(90deg, #DC2626, #EF4444);
}

/* 资源指标容器 */
.hud-metric {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: 1rem;
  background: rgba(30, 41, 59, 0.3);
  border: 1px solid rgba(148, 163, 184, 0.1);
  border-radius: var(--hud-radius-sm);
}

/* 指标头部 */
.hud-metric-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.hud-metric-label {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--hud-text-secondary);
}

.hud-metric-value {
  font-size: 1.125rem;
  font-weight: 700;
  color: var(--hud-cyan-bright);
  font-family: 'Roboto Mono', monospace;
}
```

#### 2.7 HUD 按钮系统（HUD Button System）

HUD 按钮使用**发光边框**和**几何图标**，悬停时增强发光。

```css
/* 基础 HUD 按钮 */
.hud-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(6, 182, 212, 0.4);
  border-radius: var(--hud-radius-sm);
  color: var(--hud-cyan);
  font-family: var(--hud-font);
  font-size: 0.875rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.hud-btn::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    135deg,
    transparent,
    rgba(6, 182, 212, 0.1),
    transparent
  );
  transform: translateX(-100%);
  transition: transform 0.5s ease;
}

.hud-btn:hover {
  border-color: var(--hud-cyan);
  box-shadow: var(--hud-glow-cyan);
  transform: translateY(-2px);
}

.hud-btn:hover::before {
  transform: translateX(100%);
}

.hud-btn:active {
  transform: translateY(0) scale(0.98);
  box-shadow:
    0 0 10px rgba(6, 182, 212, 0.3),
    inset 0 2px 8px rgba(0, 0, 0, 0.3);
}

/* 激活状态按钮 */
.hud-btn-active {
  background: rgba(6, 182, 212, 0.2);
  border-color: var(--hud-cyan-neon);
  color: var(--hud-cyan-neon);
  box-shadow: var(--hud-glow-cyan);
}

/* 危险按钮 */
.hud-btn-danger {
  border-color: rgba(239, 68, 68, 0.4);
  color: var(--hud-danger);
}

.hud-btn-danger:hover {
  border-color: var(--hud-danger);
  box-shadow: var(--hud-glow-red);
}

/* 成功按钮 */
.hud-btn-success {
  border-color: rgba(34, 197, 94, 0.4);
  color: var(--hud-success);
}

.hud-btn-success:hover {
  border-color: var(--hud-success);
  box-shadow: var(--hud-glow-green);
}

/* 按钮图标 */
.hud-btn-icon {
  font-size: 1.125rem;
}

/* 按钮标签 */
.hud-btn-label {
  font-size: 0.75rem;
}
```

#### 2.8 顶部状态栏系统（Top Status Bar System）

顶部状态栏显示**系统名称、时间、全局状态**。

```css
/* 状态栏 */
.hud-status-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: rgba(2, 6, 23, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(6, 182, 212, 0.3);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2rem;
  z-index: 1000;
}

/* Logo 区域 */
.hud-logo {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.hud-logo-icon {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  font-weight: 900;
  color: var(--hud-cyan-neon);
  background: rgba(6, 182, 212, 0.1);
  border: 2px solid var(--hud-cyan);
  border-radius: 4px;
  box-shadow: var(--hud-glow-cyan);
}

.hud-logo-text {
  font-family: var(--hud-font);
  font-size: 1.125rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--hud-text-primary);
}

/* 时间显示 */
.hud-status-time {
  font-family: 'Roboto Mono', monospace;
  font-size: 1rem;
  font-weight: 600;
  color: var(--hud-cyan);
  padding: 0.5rem 1rem;
  background: rgba(6, 182, 212, 0.1);
  border: 1px solid rgba(6, 182, 212, 0.3);
  border-radius: 4px;
}

/* 状态右侧 */
.hud-status-right {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
```

### 3. Tailwind CSS 配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        hud: {
          'bg-deep': '#020617',
          'bg-dark': '#0f172a',
          'bg-panel': '#1e293b',
          'cyan': '#06B6D4',
          'cyan-bright': '#0EA5E9',
          'cyan-neon': '#22D3EE',
          'success': '#22C55E',
          'warning': '#F97316',
          'alert': '#EAB308',
          'danger': '#EF4444',
          'offline': '#6B7280',
        },
      },
      fontFamily: {
        hud: ['Orbitron', 'Rajdhani', 'Exo 2', 'Roboto Mono', 'monospace'],
        mono: ['Roboto Mono', 'Courier New', 'monospace'],
      },
      backdropBlur: {
        'hud': '16px',
      },
      boxShadow: {
        'hud-glow': '0 0 20px rgba(6, 182, 212, 0.5)',
        'hud-glow-strong': '0 0 30px rgba(34, 211, 238, 0.7)',
        'hud-panel': '0 4px 24px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(148, 163, 184, 0.1)',
      },
      animation: {
        'radar-sweep': 'radarSweep 6s linear infinite',
        'radar-pulse': 'radarPulse 2s ease-in-out infinite',
        'status-pulse': 'statusPulse 2s ease-in-out infinite',
        'bar-shine': 'barShine 2s ease-in-out infinite',
        'data-slide-in': 'dataLineSlideIn 0.3s ease-out',
      },
      keyframes: {
        radarSweep: {
          from: { transform: 'rotate(0deg)' },
          to: { transform: 'rotate(360deg)' },
        },
        radarPulse: {
          '0%, 100%': { transform: 'scale(1)', opacity: '1' },
          '50%': { transform: 'scale(1.5)', opacity: '0.5' },
        },
        statusPulse: {
          '0%, 100%': { transform: 'scale(1)', opacity: '1' },
          '50%': { transform: 'scale(1.2)', opacity: '0.8' },
        },
        barShine: {
          to: { left: '100%' },
        },
        dataLineSlideIn: {
          from: { opacity: '0', transform: 'translateX(-10px)' },
          to: { opacity: '1', transform: 'translateX(0)' },
        },
      },
    },
  },
  plugins: [],
};
```

### 4. 使用示例

```html
<!-- HUD 仪表板 -->
<div class="min-h-screen bg-gradient-to-br from-hud-bg-deep via-hud-bg-dark to-hud-bg-deep">
  <!-- 顶部状态栏 -->
  <div class="hud-status-bar">
    <div class="hud-logo">
      <div class="hud-logo-icon">HUD</div>
      <span class="hud-logo-text">NEXUS SYSTEM</span>
    </div>
    <div class="hud-status-time">12:34:56 UTC</div>
    <div class="hud-status-right">
      <div class="hud-status-indicator hud-status-online"></div>
      <span class="hud-status-label">ONLINE</span>
    </div>
  </div>

  <!-- 主内容区 -->
  <main class="max-w-7xl mx-auto px-8 py-24">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <!-- 左侧：系统状态 -->
      <div class="hud-panel">
        <div class="flex justify-between items-center mb-6">
          <h3 class="text-lg font-bold text-hud-text-primary uppercase tracking-wider">
            SYSTEM STATUS
          </h3>
          <div class="hud-status-indicator hud-status-online"></div>
        </div>

        <!-- 资源指标 -->
        <div class="space-y-4">
          <div class="hud-metric">
            <div class="hud-metric-header">
              <span class="hud-metric-label">POWER CORE</span>
              <span class="hud-metric-value">92%</span>
            </div>
            <div class="hud-bar">
              <div class="hud-bar-fill hud-bar-blue" style="width: 92%"></div>
            </div>
          </div>

          <div class="hud-metric">
            <div class="hud-metric-header">
              <span class="hud-metric-label">SHIELD</span>
              <span class="hud-metric-value">78%</span>
            </div>
            <div class="hud-bar">
              <div class="hud-bar-fill hud-bar-cyan" style="width: 78%"></div>
            </div>
          </div>

          <div class="hud-metric">
            <div class="hud-metric-header">
              <span class="hud-metric-label">SYSTEMS</span>
              <span class="hud-metric-value">100%</span>
            </div>
            <div class="hud-bar">
              <div class="hud-bar-fill hud-bar-green" style="width: 100%"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- 右侧：数据流 -->
      <div class="hud-panel">
        <h3 class="text-lg font-bold text-hud-text-primary uppercase tracking-wider mb-6">
          DATA STREAM
        </h3>
        <div class="hud-data-stream">
          <div class="hud-data-line">
            <span class="hud-data-timestamp">12:34:56</span>
            <span class="hud-data-text">System initialized</span>
          </div>
          <div class="hud-data-line hud-data-success">
            <span class="hud-data-timestamp">12:34:58</span>
            <span class="hud-data-text">Connection established</span>
          </div>
          <div class="hud-data-line hud-data-warning">
            <span class="hud-data-timestamp">12:35:00</span>
            <span class="hud-data-text">3 objects detected</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 底部控制栏 -->
    <div class="flex justify-center gap-4 mt-8">
      <button class="hud-btn hud-btn-active">
        <span class="hud-btn-icon">◆</span>
        <span class="hud-btn-label">SCAN</span>
      </button>
      <button class="hud-btn">
        <span class="hud-btn-icon">▲</span>
        <span class="hud-btn-label">NAV</span>
      </button>
      <button class="hud-btn">
        <span class="hud-btn-icon">●</span>
        <span class="hud-btn-label">TARGET</span>
      </button>
    </div>
  </main>
</div>
```


---

## English Version (en-US)

### 1. Design Philosophy & Core Principles

**Sci-Fi HUD (Heads-Up Display)** style originates from futuristic interfaces in films and games, particularly holographic displays in starship cockpits, mech control systems, and tactical command centers. The core philosophy is **information as interface**, where all UI elements are presented as **glowing geometric shapes, transparent panels, and real-time data streams**, creating an immersive "operating high-tech equipment" experience.

**Design Principles**:
- **Deep Space Background**: Ultra-dark blue-gray backgrounds simulating space or command room environments
- **Glowing Geometry**: All elements use cyan/teal glowing borders for holographic projection feel
- **Information Density**: Interfaces carry large amounts of real-time data, maintained readable through layering and modularization
- **Real-time Dynamics**: Radar scans, data streams, status pulses convey "system is running" feeling
- **Translucent Materials**: Panels use glassmorphism effects with blurred backgrounds

### 2. Core Design Requirements

[继续英文版本的详细内容...]

**Advanced Implementation Details**

**Performance Optimization Strategies**:
- Use CSS containment (`contain: layout style paint`) on independent sections to improve rendering performance
- Implement lazy loading for images and heavy content below the fold using Intersection Observer API
- Utilize `will-change` property judiciously on elements that will animate (remove after animation completes)
- Minimize layout thrashing by batching DOM reads and writes
- Use requestAnimationFrame for smooth JavaScript animations at 60fps
- Consider using CSS custom properties for dynamic values instead of inline styles

**Responsive Design Patterns**:
- Mobile (< 640px): Stack all elements vertically, simplify animations, reduce visual effects by 40-50%
- Tablet (640-1024px): Use 2-column layouts where appropriate, maintain moderate visual effects
- Desktop (≥ 1024px): Full visual experience with all effects, animations, and interactive elements
- Implement fluid typography using clamp() for seamless scaling across breakpoints
- Test on actual devices, not just browser resize, to catch touch and performance issues

**Accessibility Standards**:
- Ensure WCAG 2.1 Level AA compliance minimum (4.5:1 contrast for text, 3:1 for UI components)
- Implement keyboard navigation for all interactive elements with visible focus indicators (3px+ outline)
- Provide skip links to main content for screen reader users
- Add appropriate ARIA labels, roles, and states for complex interactive components
- Respect user preferences: prefers-reduced-motion, prefers-color-scheme, prefers-contrast
- Test with actual assistive technologies (NVDA, JAWS, VoiceOver) not just automated tools
- Ensure all images have descriptive alt text and decorative images use alt=""

**Browser Compatibility & Fallbacks**:
- Test across Chrome, Firefox, Safari, and Edge for visual consistency
- Provide fallback styles for CSS features with limited support (backdrop-filter, scroll-timeline)
- Use feature detection (@supports) to progressively enhance
- Implement polyfills for critical features in older browsers if necessary
- Test on both desktop and mobile browsers as rendering may differ
- Ensure graceful degradation: site remains functional even without advanced CSS features

**Code Quality & Maintainability**:
- Use CSS custom properties (variables) for consistent theming and easy maintenance
- Organize styles with clear naming conventions (BEM, utility-first, or custom methodology)
- Comment complex CSS techniques for future maintainability
- Extract repeated patterns into reusable utility classes
- Keep specificity low to avoid cascading issues
- Validate HTML and CSS to catch errors early

**Sci-Fi HUD Advanced Techniques**

**Holographic UI Elements**:
- Create semi-transparent panels using rgba backgrounds with backdrop-filter blur
- Implement animated scan lines moving vertically or horizontally across panels
- Add holographic flicker using subtle opacity keyframe animations (0.9-1.0 range)
- Use gradient borders that animate position to simulate energy flow
- Apply chromatic aberration on edges using box-shadow in cyan and magenta

**Data Visualization Components**:
- Design circular progress indicators using conic-gradient or SVG stroke-dasharray
- Implement bar graphs with animated fills using CSS transitions or GSAP
- Create radar/sonar displays with rotating sweep animation
- Add network topology diagrams with animated connection lines
- Design numerical counters with digital/segmented display aesthetics

**Angular Geometry & Layout**:
- Use clip-path polygon to create cut-corner panels and angular shapes
- Implement diagonal lines and chevron patterns for directional emphasis
- Create hexagonal or octagonal containers instead of rectangular
- Apply skew transforms for italic/slanted panel aesthetics
- Design corner brackets and frame elements using positioned pseudo-elements

**Glow & Luminance Effects**:
- Layer multiple box-shadows for intense outer glow (3-5 layers recommended)
- Use drop-shadow filter on SVG elements for cohesive glow across shapes
- Implement pulsing glow animation using shadow spread-radius changes
- Apply inner glow using inset box-shadow for button active states
- Create light trail effects using gradient with animated background-position

**HUD Typography System**:
- Primary: Monospace fonts (JetBrains Mono, Space Mono) for data displays
- Secondary: Geometric sans-serif (Rajdhani, Orbitron, Saira) for labels
- Use uppercase with increased letter-spacing (0.1-0.15em) for tactical feel
- Apply subtle text glow using text-shadow for readability on dark backgrounds
- Implement animated number counting effects for live data updates

**Status & Alert System**:
- Green: Optimal/online status (#00ff88, #22ff66)
- Yellow/Amber: Warning states (#ffaa00, #ffcc00)
- Red: Critical alerts (#ff0055, #ff1744)
- Blue/Cyan: Information and data (#00ddff, #33ccff)
- Use blinking animations for urgent alerts (1-2s interval)
- Combine color with icons and text to avoid color-only communication

**Animation Timing & Rhythm**:
- Fast transitions for user interactions (150-250ms) to feel responsive
- Medium speed for data updates and state changes (400-600ms)
- Slow animations for ambient effects (2-8s) like scan lines or glows
- Use cubic-bezier easing for mechanical precision: cubic-bezier(0.4, 0, 0.2, 1)
- Stagger animations with 50-150ms delays for sequential reveal effects

**Responsive HUD Design**:
- Mobile: Simplify layout to single column, reduce glow effects, enlarge touch targets
- Tablet: Use 2-column grid, maintain moderate visual effects
- Desktop: Full multi-panel HUD experience with maximum visual fidelity
- Scale HUD elements proportionally to maintain aspect ratios
- Hide or collapse less critical data panels on smaller screens

**Performance Considerations**:
- Limit active glow effects to 10-15 elements maximum on screen
- Use CSS transforms and opacity for animations (GPU accelerated)
- Implement intersection observer to only animate visible HUD elements
- Reduce animation frame rate on mobile to 30fps if needed
- Use CSS containment on independent HUD panels
- Debounce data update animations to avoid excessive re-rendering

**Accessibility Requirements**:
- Ensure text contrast meets WCAG AA even with glow effects (4.5:1 minimum)
- Provide alternative visualization modes without complex animations
- Add keyboard shortcuts for quick HUD panel navigation
- Implement screen reader announcements for data updates using ARIA live regions
- Ensure focus indicators remain visible on glowing backgrounds
- Respect prefers-reduced-motion preference by disabling decorative animations
