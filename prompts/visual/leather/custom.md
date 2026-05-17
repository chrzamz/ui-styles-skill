# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名擅长材质表现的资深 UI 设计师兼前端工程师，请生成一个与当前「皮革质感（Leather Texture）」展示界面风格高度接近的深色皮革风格 UI。
请使用 TailwindCSS 创建一个深色皮革质感风格的界面，通过径向渐变、噪点纹理、缝线和金属细节营造厚重而奢华的视觉体验。

**核心设计要求**

1. **皮革背景质感系统**
   - 使用多层径向渐变营造中心略亮、边缘较暗的皮面效果：
     ```css
     .leather-bg {
       background:
         radial-gradient(ellipse at top, #4b3621 0%, #2b1c12 45%, #120b07 100%),
         radial-gradient(circle at bottom left, #3b2718 0%, transparent 55%),
         radial-gradient(circle at bottom right, #3b2718 0%, transparent 55%);
       background-color: #120b07;
     }
     ```
   - 颜色区间：深棕 (#3b2718, #4b3621) 到接近黑色 (#120b07)。
   - 亮暗对比要明显，但避免纯黑，保持细节空间。

2. **噪点与纹理叠加**
   - 使用 CSS 滤镜或 SVG 噪点模拟皮革纤维：
     ```css
     .leather-texture {
       position: relative;
       overflow: hidden;
     }

     .leather-texture::before {
       content: '';
       position: absolute;
       inset: 0;
       background-image:
         radial-gradient(circle at 0 0, rgba(255,255,255,0.06) 0, transparent 40%),
         radial-gradient(circle at 100% 0, rgba(0,0,0,0.4) 0, transparent 55%),
         radial-gradient(circle at 0 100%, rgba(0,0,0,0.3) 0, transparent 55%);
       mix-blend-mode: multiply;
       opacity: 0.7;
       pointer-events: none;
     }
     ```
   - 可以叠加 `filter: contrast(1.05) brightness(1.05);` 让纹理更清晰。
   - 避免颗粒过大，以细密、柔和为主。

3. **内外阴影与压痕**
   - 外阴影用于模拟皮革面板浮在背景上：
     ```css
     .leather-panel {
       box-shadow:
         0 18px 40px rgba(0, 0, 0, 0.6),
         0 0 0 1px rgba(0, 0, 0, 0.8);
     }
     ```
   - 内阴影用于卡槽、按键、表盘等凹陷区域：
     ```css
     .leather-inset {
       box-shadow:
         inset 0 2px 4px rgba(255, 255, 255, 0.04),
         inset 0 -4px 10px rgba(0, 0, 0, 0.8);
     }
     ```
   - 建议同时组合 2–3 层阴影，营造厚度与压痕。

4. **缝线与边缘细节**
   - 使用虚线边框或重复线性渐变模拟缝线：
     ```css
     .leather-stitch {
       position: relative;
       border-radius: 18px;
       padding: 1px;
       background:
         linear-gradient(#2b1c12, #2b1c12) padding-box,
         linear-gradient(135deg, #e2c9a0, #8a5a32) border-box;
     }

     .leather-stitch::before {
       content: '';
       position: absolute;
       inset: 10px;
       border-radius: 14px;
       border: 1px dashed rgba(226, 201, 160, 0.8);
       box-shadow:
         0 1px 0 rgba(255, 255, 255, 0.2),
         0 -1px 0 rgba(0, 0, 0, 0.6);
       pointer-events: none;
     }
     ```
   - 缝线颜色接近浅棕或麻色 (#e2c9a0)，不使用纯白或高饱和色。
   - 线距适中（8–12px），避免过密显得凌乱。

5. **金属配件与点缀**
   - 金属旋钮、角保护、螺丝等使用金属渐变：
     ```css
     .leather-metal {
       background: radial-gradient(circle at 30% 30%, #ffffff 0%, #d4c6a8 25%, #8f7248 55%, #3c2b1b 100%);
       box-shadow:
         0 1px 0 rgba(255, 255, 255, 0.5),
         0 4px 10px rgba(0, 0, 0, 0.8);
       border-radius: 999px;
     }
     ```
   - 金属色建议选用暖金、古铜而非冷银，强化复古奢华感。
   - 适量加入小型高光点，模拟反射。

6. **按键与控件形态**
   - 按钮使用略圆的矩形或圆形，带明显压痕反馈：
     ```css
     .leather-button {
       background: radial-gradient(circle at 30% 20%, #5a4028 0%, #2b1c12 60%, #120b07 100%);
       border-radius: 999px;
       padding: 10px 22px;
       color: #f5e2c4;
       letter-spacing: 0.04em;
       text-transform: uppercase;
       box-shadow:
         0 10px 20px rgba(0, 0, 0, 0.7),
         inset 0 1px 0 rgba(255, 255, 255, 0.12);
       transition: all 0.18s ease-out;
     }

     .leather-button:hover {
       filter: brightness(1.06);
       box-shadow:
         0 14px 30px rgba(0, 0, 0, 0.85),
         inset 0 1px 0 rgba(255, 255, 255, 0.2);
     }

     .leather-button:active {
       transform: translateY(2px);
       box-shadow:
         0 4px 10px rgba(0, 0, 0, 0.7),
         inset 0 3px 6px rgba(0, 0, 0, 0.8);
       filter: brightness(0.96);
     }
     ```
   - 旋钮和开关可以参考模拟设备：带刻度、指示线和内发光指示灯。

7. **整体布局与节奏**
   - 面板通常为少数几个大区块，而非大量小卡片，强化"设备面板"感。
   - 间距建议基于 8px 系统：16/24/32px 作为主要间距。
   - 动效节奏控制在 150–220ms，缓和但有重量感。

**配色方案（深色皮革）**

主色调：
- 深棕皮革：#4b3621, #3b2718, #2b1c12
- 深黑棕：#120b07, #0b0705

点缀色：
- 暖金金属：#d4c6a8, #b08a5a, #8f7248
- 指示灯：#eab308（琥珀）, #22c55e（绿色）, #f97316（橙色）

中性色：
- 高光线：rgba(255, 255, 255, 0.12-0.26)
- 阴影：rgba(0, 0, 0, 0.6-0.9)

**关键 CSS 类示例**

```css
/* 皮革背景容器 */
.leather-shell {
  @apply min-h-screen flex items-center justify-center bg-neutral-950 text-neutral-50;
}

.leather-panel {
  background:
    radial-gradient(ellipse at top, #4b3621 0%, #2b1c12 45%, #120b07 100%);
  border-radius: 24px;
  padding: 32px 40px;
  box-shadow:
    0 24px 60px rgba(0, 0, 0, 0.85),
    0 0 0 1px rgba(0, 0, 0, 0.9);
  position: relative;
  overflow: hidden;
}

/* 缝线边框 */
.leather-panel::before {
  content: '';
  position: absolute;
  inset: 14px;
  border-radius: 18px;
  border: 1px dashed rgba(226, 201, 160, 0.75);
  box-shadow:
    0 1px 0 rgba(255, 255, 255, 0.18),
    0 -1px 0 rgba(0, 0, 0, 0.8);
  pointer-events: none;
}

/* 标签与小牌匾 */
.leather-tag {
  background: linear-gradient(180deg, #3b2718 0%, #1f140d 100%);
  border-radius: 999px;
  padding: 6px 14px;
  font-size: 0.75rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #f5e2c4;
  box-shadow:
    0 4px 12px rgba(0, 0, 0, 0.7),
    inset 0 1px 0 rgba(255, 255, 255, 0.15);
}
```

**间距与字体系统（建议）**

- 基础间距单位：8px
- 内边距层级：12px / 16px / 24px / 32px / 40px
- 标题字体：衬线或几何无衬线，32–40px，字重 500–700
- 正文字体：14–16px，行高 1.6–1.8，字重 400–500
- 标签文字使用全大写与增加字距，强调器材铭牌感。

**重要提示**
- 保持整体亮度偏低，让高光和金属细节成为视觉焦点。
- 确保文字对比度符合 WCAG AA，避免深棕背景上使用过暗的文字色。
- 纹理要细腻不重复，避免"平铺纹理图"带来的廉价感。
- 控件数量不宜过多，优先展示少量关键控制区。
- 避免高饱和荧光色与强烈霓虹效果，以免破坏皮革的沉稳感。
- 在 Tailwind 中，优先使用 `bg-[radial-gradient(...)]`、`shadow-[...]` 等自定义类封装复杂细节。


---

## English Version (en-US)

You are now a senior UI designer and front-end engineer specialising in material rendering. Please generate a dark leather texture UI that closely matches the current "Leather Texture" preview.
Create a dark leather-style interface using TailwindCSS, combining radial gradients, noise textures, stitching and warm metal accents to deliver a heavy, luxurious look.

**Core Design Requirements**

1. **Leather Background Texture System**
   - Use layered radial gradients to create a slightly brighter center and darker edges:
     ```css
     .leather-bg {
       background:
         radial-gradient(ellipse at top, #4b3621 0%, #2b1c12 45%, #120b07 100%),
         radial-gradient(circle at bottom left, #3b2718 0%, transparent 55%),
         radial-gradient(circle at bottom right, #3b2718 0%, transparent 55%);
       background-color: #120b07;
     }
     ```
   - Color range: deep browns (#3b2718, #4b3621) down to near-black (#120b07).
   - Maintain strong contrast without using pure black so surface details remain visible.

2. **Noise and Grain Overlays**
   - Simulate leather grain and subtle creases with layered noise:
     ```css
     .leather-texture {
       position: relative;
       overflow: hidden;
     }

     .leather-texture::before {
       content: '';
       position: absolute;
       inset: 0;
       background-image:
         radial-gradient(circle at 0 0, rgba(255,255,255,0.06) 0, transparent 40%),
         radial-gradient(circle at 100% 0, rgba(0,0,0,0.4) 0, transparent 55%),
         radial-gradient(circle at 0 100%, rgba(0,0,0,0.3) 0, transparent 55%);
       mix-blend-mode: multiply;
       opacity: 0.7;
       pointer-events: none;
     }
     ```
   - Optionally add `filter: contrast(1.05) brightness(1.05);` to make texture clearer.
   - Keep noise fine and soft; avoid large, harsh speckles.

3. **Inner/Outer Shadows and Impressions**
   - Use outer shadows to float panels above the leather background:
     ```css
     .leather-panel {
       box-shadow:
         0 18px 40px rgba(0, 0, 0, 0.6),
         0 0 0 1px rgba(0, 0, 0, 0.8);
     }
     ```
   - Use inner shadows for recessed slots, gauges and button wells:
     ```css
     .leather-inset {
       box-shadow:
         inset 0 2px 4px rgba(255, 255, 255, 0.04),
         inset 0 -4px 10px rgba(0, 0, 0, 0.8);
     }
     ```
   - Combining 2–3 layers of shadow per element is common to achieve depth.

4. **Stitching and Edge Details**
   - Use dashed borders or layered gradients to simulate stitched seams:
     ```css
     .leather-stitch {
       position: relative;
       border-radius: 18px;
       padding: 1px;
       background:
         linear-gradient(#2b1c12, #2b1c12) padding-box,
         linear-gradient(135deg, #e2c9a0, #8a5a32) border-box;
     }

     .leather-stitch::before {
       content: '';
       position: absolute;
       inset: 10px;
       border-radius: 14px;
       border: 1px dashed rgba(226, 201, 160, 0.8);
       box-shadow:
         0 1px 0 rgba(255, 255, 255, 0.2),
         0 -1px 0 rgba(0, 0, 0, 0.6);
       pointer-events: none;
     }
     ```
   - Stitching colors should stay near warm thread tones (#e2c9a0) rather than pure white or neon.
   - Keep spacing between stitches around 8–12px to avoid visual noise.

5. **Metal Hardware and Accents**
   - Represent knobs, corners and screws with warm metal gradients:
     ```css
     .leather-metal {
       background: radial-gradient(circle at 30% 30%, #ffffff 0%, #d4c6a8 25%, #8f7248 55%, #3c2b1b 100%);
       box-shadow:
         0 1px 0 rgba(255, 255, 255, 0.5),
         0 4px 10px rgba(0, 0, 0, 0.8);
       border-radius: 999px;
     }
     ```
   - Prefer warm gold and aged brass over cold silver to reinforce a heritage luxury mood.
   - Add small specular highlights to suggest reflections.

6. **Buttons and Controls**
   - Buttons should feel weighty and slightly domed, with clear pressed states:
     ```css
     .leather-button {
       background: radial-gradient(circle at 30% 20%, #5a4028 0%, #2b1c12 60%, #120b07 100%);
       border-radius: 999px;
       padding: 10px 22px;
       color: #f5e2c4;
       letter-spacing: 0.04em;
       text-transform: uppercase;
       box-shadow:
         0 10px 20px rgba(0, 0, 0, 0.7),
         inset 0 1px 0 rgba(255, 255, 255, 0.12);
       transition: all 0.18s ease-out;
     }

     .leather-button:hover {
       filter: brightness(1.06);
       box-shadow:
         0 14px 30px rgba(0, 0, 0, 0.85),
         inset 0 1px 0 rgba(255, 255, 255, 0.2);
     }

     .leather-button:active {
       transform: translateY(2px);
       box-shadow:
         0 4px 10px rgba(0, 0, 0, 0.7),
         inset 0 3px 6px rgba(0, 0, 0, 0.8);
       filter: brightness(0.96);
     }
     ```
   - For knobs and toggles, include tick marks, indicator lines and small LEDs to reinforce the "hardware panel" metaphor.

7. **Layout and Rhythm**
   - Use a few large panels rather than many small cards to feel like a single device.
   - Base spacing on an 8px grid: 16/24/32px as the main gaps and padding.
   - Keep animation timings around 150–220ms with easing that feels heavy and deliberate rather than springy.

**Color Scheme (Dark Leather)**

Primary colors:
- Deep leather browns: #4b3621, #3b2718, #2b1c12
- Near-black browns: #120b07, #0b0705

Accent colors:
- Warm metal: #d4c6a8, #b08a5a, #8f7248
- Indicator LEDs: #eab308 (amber), #22c55e (green), #f97316 (orange)

Neutrals:
- Highlights: rgba(255, 255, 255, 0.12-0.26)
- Shadows: rgba(0, 0, 0, 0.6-0.9)

**Key CSS Class Examples**

```css
/* Leather background shell */
.leather-shell {
  @apply min-h-screen flex items-center justify-center bg-neutral-950 text-neutral-50;
}

.leather-panel {
  background:
    radial-gradient(ellipse at top, #4b3621 0%, #2b1c12 45%, #120b07 100%);
  border-radius: 24px;
  padding: 32px 40px;
  box-shadow:
    0 24px 60px rgba(0, 0, 0, 0.85),
    0 0 0 1px rgba(0, 0, 0, 0.9);
  position: relative;
  overflow: hidden;
}

/* Stitched border */
.leather-panel::before {
  content: '';
  position: absolute;
  inset: 14px;
  border-radius: 18px;
  border: 1px dashed rgba(226, 201, 160, 0.75);
  box-shadow:
    0 1px 0 rgba(255, 255, 255, 0.18),
    0 -1px 0 rgba(0, 0, 0, 0.8);
  pointer-events: none;
}

/* Label plate */
.leather-tag {
  background: linear-gradient(180deg, #3b2718 0%, #1f140d 100%);
  border-radius: 999px;
  padding: 6px 14px;
  font-size: 0.75rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #f5e2c4;
  box-shadow:
    0 4px 12px rgba(0, 0, 0, 0.7),
    inset 0 1px 0 rgba(255, 255, 255, 0.15);
}
```

**Spacing and Typography System (Recommended)**

- Base spacing unit: 8px.
- Padding levels: 12px / 16px / 24px / 32px / 40px.
- Heading type: serif or geometric sans-serif, 32–40px, weight 500–700.
- Body type: 14–16px, line-height 1.6–1.8, weight 400–500.
- Labels use uppercase with expanded tracking to resemble nameplates and instrument labels.

**Important Notes**
- Keep global brightness low so leather and metal highlights become focal points.
- Ensure text contrast meets WCAG AA, avoiding overly dark text on deep brown backgrounds.
- Texture should feel fine and non-repeating; avoid obvious tiled bitmaps.
- Limit the number of controls on screen; highlight a few key groups instead of dense dashboards.
- Avoid neon and highly saturated colors that would break the sober, premium mood.
- In Tailwind, prefer encapsulating complex details in utilities like `bg-[radial-gradient(...)]` and `shadow-[...]` for reuse.
