# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名非常熟悉「Liquid Motion 深海科技仪表盘」风格的资深 UI 设计师兼前端工程师，需要为一个全新页面生成一套与当前预览 /styles/preview/visual-nature-liquid（LiquidFullPage）在「背景动画结构」上高度一致的 UI。

你的重点任务：请完整复刻当前模板中所有背景动画层（至少 8 层），并在新页面的 HTML/CSS 中保留相同的 class 名称与动画逻辑，只替换文案、业务数据和部分布局结构。下面给出当前模板使用的完整背景动画代码，请严格按照这些层级来设计和生成新的页面。

【背景动画总览】
- LAYER 1：Deep Ocean Current（深海洋流 blob，30s 循环）
- LAYER 2：Mid-Layer Water Mass（中层水体 blob，20s 循环）
- LAYER 3：Surface Surge（表层浪涌 blob，12s 循环）
- LAYER 4：Rising Bubbles（上升气泡粒子）
- LAYER 5：Bioluminescent Plankton（发光浮游生物）
- LAYER 6：Light Refraction Beams（光线折射光束）
- LAYER 7：Auto Ripples（自动扩散水波纹）
- LAYER 8：Seaweed Sway（摇曳的海草 silohuette）

你生成的新页面必须至少保留这 8 层中的核心层级（1~5 必须保留，6~8 可在性能允许时保留），并使用与下方一致或等价的 CSS 动画结构。

【基础容器与页面背景】
请使用一个顶层容器 .liquid-page 包住所有背景层与内容层：

.liquid-page {
  min-height: 100vh;
  background: linear-gradient(180deg, #020617 0%, #0a192f 50%, #112240 100%);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: #e2e8f0;
  position: relative;
  overflow-x: hidden;
}

【LAYER 1：Deep Ocean Current（深海洋流 blob，30s）】
@keyframes deepOceanCurrent {
  0%, 100% {
    transform: translate(0, 0) rotate(0deg) scale(1);
    border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
  }
  20% {
    transform: translate(150px, -100px) rotate(72deg) scale(1.3);
    border-radius: 60% 40% 30% 70% / 50% 60% 50% 40%;
  }
  40% {
    transform: translate(-80px, 120px) rotate(144deg) scale(0.8);
    border-radius: 30% 70% 60% 40% / 60% 40% 50% 60%;
  }
  60% {
    transform: translate(200px, 80px) rotate(216deg) scale(1.2);
    border-radius: 70% 30% 40% 60% / 40% 60% 70% 30%;
  }
  80% {
    transform: translate(-120px, -60px) rotate(288deg) scale(0.9);
    border-radius: 50% 50% 60% 40% / 55% 45% 55% 45%;
  }
}

.ocean-blob-deep {
  position: absolute;
  width: 800px;
  height: 800px;
  background: radial-gradient(circle, rgba(0, 229, 255, 0.15) 0%, rgba(100, 255, 218, 0.08) 50%, transparent 70%);
  filter: blur(80px);
  animation: deepOceanCurrent 30s ease-in-out infinite;
  will-change: transform, border-radius;
  pointer-events: none;
  z-index: 0;
}

.ocean-blob-deep-1 {
  top: -20%;
  left: -10%;
  animation-delay: 0s;
}

.ocean-blob-deep-2 {
  bottom: -30%;
  right: -15%;
  animation-delay: -15s;
  background: radial-gradient(circle, rgba(100, 255, 218, 0.12) 0%, rgba(0, 229, 255, 0.06) 50%, transparent 70%);
}

【LAYER 2：Mid-Layer Water Mass（中层水体 blob，20s）】
@keyframes midLayerFlow {
  0%, 100% {
    transform: translate(0, 0) rotate(0deg) scale(1);
    border-radius: 50% 50% 40% 60% / 60% 40% 60% 40%;
  }
  25% {
    transform: translate(100px, -80px) rotate(90deg) scale(1.15);
    border-radius: 40% 60% 50% 50% / 50% 50% 50% 50%;
  }
  50% {
    transform: translate(-60px, 100px) rotate(180deg) scale(0.85);
    border-radius: 60% 40% 60% 40% / 40% 60% 40% 60%;
  }
  75% {
    transform: translate(80px, 40px) rotate(270deg) scale(1.1);
    border-radius: 45% 55% 55% 45% / 55% 45% 55% 45%;
  }
}

.ocean-blob-mid {
  position: absolute;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(0, 229, 255, 0.2) 0%, rgba(100, 255, 218, 0.1) 60%, transparent 80%);
  filter: blur(60px);
  animation: midLayerFlow 20s ease-in-out infinite;
  will-change: transform, border-radius;
  pointer-events: none;
  z-index: 0;
}

.ocean-blob-mid-1 {
  top: 20%;
  left: 30%;
  animation-delay: -5s;
}

.ocean-blob-mid-2 {
  top: 50%;
  right: 20%;
  animation-delay: -10s;
}

.ocean-blob-mid-3 {
  bottom: 20%;
  left: 10%;
  animation-delay: -15s;
}

【LAYER 3：Surface Surge（表层浪涌 blob，12s）】
@keyframes surfaceSurge {
  0%, 100% {
    transform: translate(0, 0) rotate(0deg) scale(1);
    border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
  }
  33% {
    transform: translate(120px, -60px) rotate(120deg) scale(1.25);
    border-radius: 70% 30% 30% 70% / 70% 70% 30% 30%;
  }
  66% {
    transform: translate(-80px, 80px) rotate(240deg) scale(0.75);
    border-radius: 50% 50% 50% 50% / 50% 50% 50% 50%;
  }
}

.ocean-blob-surface {
  position: absolute;
  width: 350px;
  height: 350px;
  background: radial-gradient(circle, rgba(0, 229, 255, 0.25) 0%, rgba(100, 255, 218, 0.15) 50%, transparent 70%);
  filter: blur(40px);
  animation: surfaceSurge 12s ease-in-out infinite;
  will-change: transform, border-radius;
  pointer-events: none;
  z-index: 0;
}

.ocean-blob-surface-1 {
  top: 10%;
  right: 30%;
  animation-delay: -3s;
}

.ocean-blob-surface-2 {
  bottom: 30%;
  left: 40%;
  animation-delay: -6s;
}

【LAYER 4：Rising Bubbles（上升气泡粒子）】
@keyframes bubbleRise {
  0% {
    transform: translateY(100vh) translateX(0) scale(0.3);
    opacity: 0;
  }
  10% {
    opacity: 0.8;
  }
  50% {
    transform: translateY(50vh) translateX(var(--bubble-drift, 20px)) scale(0.6);
  }
  90% {
    opacity: 0.4;
  }
  100% {
    transform: translateY(-10vh) translateX(calc(var(--bubble-drift, 20px) * -1)) scale(1);
    opacity: 0;
  }
}

.bubble {
  position: absolute;
  width: var(--bubble-size, 10px);
  height: var(--bubble-size, 10px);
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.8), rgba(0, 229, 255, 0.3));
  border-radius: 50%;
  animation: bubbleRise var(--bubble-duration, 8s) ease-in-out infinite;
  animation-delay: var(--bubble-delay, 0s);
  will-change: transform, opacity;
  pointer-events: none;
  z-index: 1;
}

【LAYER 5：Bioluminescent Plankton（发光浮游生物）】
@keyframes planktonGlow {
  0%, 100% {
    opacity: 0.2;
    transform: translate(0, 0) scale(0.8);
    filter: blur(1px);
  }
  25% {
    opacity: 0.5;
    transform: translate(30px, -20px) scale(1.1);
    filter: blur(0px);
    box-shadow: 0 0 20px #00e5ff, 0 0 40px #64ffda;
  }
  50% {
    opacity: 0.3;
    transform: translate(-25px, 35px) scale(0.9);
    filter: blur(2px);
  }
  75% {
    opacity: 0.95;
    transform: translate(40px, 15px) scale(1.2);
    filter: blur(0px);
    box-shadow: 0 0 25px #00e5ff, 0 0 50px #64ffda;
  }
}

.plankton {
  position: absolute;
  width: var(--plankton-size, 4px);
  height: var(--plankton-size, 4px);
  background: #00e5ff;
  border-radius: 50%;
  animation: planktonGlow var(--plankton-duration, 15s) ease-in-out infinite;
  animation-delay: var(--plankton-delay, 0s);
  will-change: transform, opacity, filter;
  pointer-events: none;
  z-index: 1;
}

【LAYER 6：Light Refraction Beams（光线折射光束）】
@keyframes lightBeam {
  0%, 100% {
    opacity: 0.2;
    transform: translateY(0) scaleY(1) skewX(0deg);
  }
  25% {
    opacity: 0.5;
    transform: translateY(30px) scaleY(1.1) skewX(2deg);
  }
  50% {
    opacity: 0.3;
    transform: translateY(10px) scaleY(0.95) skewX(-1deg);
  }
  75% {
    opacity: 0.6;
    transform: translateY(40px) scaleY(1.15) skewX(3deg);
  }
}

.light-beam {
  position: absolute;
  top: 0;
  width: var(--beam-width, 100px);
  height: 100%;
  background: linear-gradient(180deg,
    rgba(255, 255, 255, 0.15) 0%,
    rgba(0, 229, 255, 0.08) 30%,
    rgba(100, 255, 218, 0.03) 70%,
    transparent 100%
  );
  filter: blur(20px);
  animation: lightBeam var(--beam-duration, 25s) ease-in-out infinite;
  animation-delay: var(--beam-delay, 0s);
  will-change: transform, opacity;
  pointer-events: none;
  z-index: 0;
}

【LAYER 7：Auto Ripples（自动水波纹）】
@keyframes autoRipple {
  0%, 100% {
    transform: scale(0);
    opacity: 0.4;
  }
  50% {
    transform: scale(2);
    opacity: 0;
  }
}

.auto-ripple {
  position: absolute;
  width: 150px;
  height: 150px;
  border: 1px solid rgba(100, 255, 218, 0.3);
  border-radius: 50%;
  animation: autoRipple 10s ease-in-out infinite;
  will-change: transform, opacity;
  pointer-events: none;
  z-index: 0;
}

【LAYER 8：Seaweed Sway（海草摇曳）】
@keyframes seaweedSway {
  0%, 100% {
    transform: rotate(-5deg) scaleY(1);
  }
  25% {
    transform: rotate(3deg) scaleY(1.02);
  }
  50% {
    transform: rotate(-8deg) scaleY(0.98);
  }
  75% {
    transform: rotate(6deg) scaleY(1.01);
  }
}

.seaweed {
  position: absolute;
  bottom: 0;
  width: var(--seaweed-width, 20px);
  height: var(--seaweed-height, 150px);
  background: linear-gradient(180deg, rgba(100, 255, 218, 0.4) 0%, rgba(0, 229, 255, 0.2) 100%);
  border-radius: 50% 50% 0 0;
  transform-origin: bottom center;
  animation: seaweedSway var(--seaweed-duration, 18s) ease-in-out infinite;
  animation-delay: var(--seaweed-delay, 0s);
  will-change: transform;
  pointer-events: none;
  z-index: 1;
}

【输出与约束要求】
- 生成的新 HTML 页面必须：
  - 使用 .liquid-page 容器和上述所有背景层 class 名称（可以增减元素数量，但不要完全删除某一层的存在）；
  - 保留「多层液体 blob + 气泡 + 发光粒子 + 光束 + 水波纹 + 海草」的整体视觉结构；
  - 内容层（.ocean-content 及内部卡片/按钮）可以改成新的业务场景，但仍然使用玻璃态卡片、液体进度条和发光按钮等元素。
- 你输出的内容只需要给出完整的 HTML 结构（包括这些背景层节点与内容层），不需要再解释原理。CSS 可以通过上述代码片段推导或复用。


---

## English Version (en-US)

You are rebuilding a new page while keeping the same 8-layer Liquid Motion background stack described above.
- Preserve class names and animation logic for .liquid-page and all ocean layers (blob/bubbles/plankton/light-beam/ripple/seaweed); change only copy, data, and layout.
- Keep at least layers 1–5; include 6–8 when performance allows, and use glass cards, liquid progress bars, and glowing CTAs in the content area.
- Output full HTML with these background nodes and content; CSS can reuse or extend the provided snippets—no extra explanation is needed.

---
