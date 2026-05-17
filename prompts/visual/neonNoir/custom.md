# Custom Prompt

## 中文版本 (zh-CN)

请使用 TailwindCSS 创建一个 **Neon Noir（霓虹黑色电影）** 风格的界面，将赛博朋克霓虹灯与黑色电影的高对比光影结合起来，营造潮湿夜街、酒吧门口、音乐平台等场景氛围。

**核心设计要求**

1. **黑色电影式深色背景**
   - 使用接近纯黑的渐变背景：\`#050509 → #0a0a0a → #1a0a14\`
   - 可以叠加轻微雾气、暗角（vignette）与颗粒噪点，营造胶片质感
   - 示例：
     \`\`\`css
     .neon-noir-bg {
       background:
         radial-gradient(circle at top, #1a0a14 0%, #050509 40%, #000000 100%);
       color: #f9fafb;
     }

     .neon-noir-vignette::before {
       content: '';
       position: absolute;
       inset: 0;
       pointer-events: none;
       background:
         radial-gradient(circle at center,
           transparent 0%,
           transparent 45%,
           rgba(0, 0, 0, 0.75) 100%);
     }
     \`\`\`

2. **霓虹粉紫 + 高对比光晕**
   - 主色：霓虹红粉 \`#ff0055\`、霓虹粉紫 \`#ff00ff\`、霓虹紫 \`#b967ff\`
   - 背景多为暗红 / 酒红：\`#1a0a14\`、\`#140812\`
   - 文字与边框示例：
     \`\`\`css
     .neon-noir-pink {
       color: #ff0055;
       text-shadow:
         0 0 10px rgba(255, 0, 85, 0.9),
         0 0 25px rgba(255, 0, 85, 0.7),
         0 0 40px rgba(255, 0, 85, 0.5);
     }

     .neon-noir-purple {
       color: #b967ff;
       text-shadow:
         0 0 12px rgba(185, 103, 255, 0.9),
         0 0 24px rgba(185, 103, 255, 0.7);
     }

     .neon-noir-border {
       border: 1px solid rgba(255, 0, 85, 0.7);
       box-shadow:
         0 0 20px rgba(255, 0, 85, 0.6),
         0 0 40px rgba(255, 0, 85, 0.4);
     }
     \`\`\`

3. **霓虹招牌与标题字体**
   - 使用大写、宽字距标题：\`letter-spacing: 0.12em - 0.2em\`
   - 模拟霓虹招牌：多层 text-shadow + 闪烁动画
   - 示例：
     \`\`\`css
     .neon-noir-title {
       font-size: clamp(1.75rem, 3vw, 3rem);
       font-weight: 900;
       letter-spacing: 0.16em;
       color: #ff0055;
       text-transform: uppercase;
       text-shadow:
         0 0 10px rgba(255, 0, 85, 0.9),
         0 0 20px rgba(255, 0, 85, 0.8),
         0 0 40px rgba(255, 0, 85, 0.6);
       animation: neonNoirFlicker 4s ease-in-out infinite;
     }

     @keyframes neonNoirFlicker {
       0%, 100% { opacity: 1; }
       3%, 7%, 22%, 28% { opacity: 0.85; }
       5%, 24% { opacity: 0.4; }
     }
     \`\`\`

4. **雾气与光晕粒子**
   - 使用模糊圆形渐变作为「霓虹光晕」与「街头雾气」
   - 粒子随机漂浮，速度较慢（4–10 秒）以保持 Noir 气氛
   - 示例：
     \`\`\`css
     .neon-noir-fog {
       position: absolute;
       width: 200px;
       height: 200px;
       border-radius: 9999px;
       background: radial-gradient(circle,
         rgba(255, 0, 85, 0.25),
         transparent 70%);
       filter: blur(35px);
       animation: noirFogFloat 8s ease-in-out infinite;
     }

     @keyframes noirFogFloat {
       0%, 100% { transform: translate3d(0, 0, 0); opacity: 0.25; }
       50% { transform: translate3d(-12px, -18px, 0); opacity: 0.4; }
     }
     \`\`\`

5. **卡片与音乐平台模块**
   - 典型场景：音乐平台 / 夜店活动页面
   - 卡片设计：
     - 半透明深色背景：\`rgba(10, 10, 16, 0.8)\`
     - 霓虹边框 + 微弱内阴影
     - 卡片标题使用霓虹字体、描述文字保持偏灰色
   - 示例：
     \`\`\`css
     .neon-noir-card {
       background: rgba(10, 10, 16, 0.8);
       border-radius: 1rem;
       border: 1px solid rgba(185, 103, 255, 0.6);
       box-shadow:
         0 0 24px rgba(185, 103, 255, 0.4),
         0 20px 40px rgba(0, 0, 0, 0.7);
       padding: 1.25rem 1.5rem;
     }

     .neon-noir-card-title {
       font-weight: 700;
       color: #ff00ff;
       letter-spacing: 0.08em;
     }
     \`\`\`

6. **互动与按钮效果**
   - 按钮应具有「霓虹亮起」的悬停状态与轻微按压效果
   - 建议使用边框 + 透明背景组合
   - 示例：
     \`\`\`css
     .neon-noir-button {
       padding: 0.75rem 1.75rem;
       border-radius: 9999px;
       border: 1px solid rgba(255, 0, 85, 0.8);
       background: rgba(5, 5, 10, 0.8);
       color: #ff0055;
       font-weight: 600;
       letter-spacing: 0.08em;
       text-transform: uppercase;
       box-shadow:
         0 0 16px rgba(255, 0, 85, 0.5),
         0 8px 18px rgba(0, 0, 0, 0.8);
       transition: all 0.25s ease-out;
     }

     .neon-noir-button:hover {
       background: rgba(255, 0, 85, 0.1);
       box-shadow:
         0 0 26px rgba(255, 0, 85, 0.8),
         0 14px 28px rgba(0, 0, 0, 0.9);
       transform: translateY(-2px);
     }

     .neon-noir-button:active {
       transform: translateY(1px) scale(0.98);
       box-shadow:
         0 0 12px rgba(255, 0, 85, 0.6),
         0 6px 16px rgba(0, 0, 0, 0.9);
     }
     \`\`\`

**配色方案（Neon Noir）**

- 背景：\`#0a0a0a\`、\`#050509\`、\`#1a0a14\`
- 霓虹主色：\`#ff0055\`、\`#ff00ff\`、\`#b967ff\`
- 文本：\`#f9fafb\`（主文本）、\`#9ca3af\`（描述文字）

**重要提示**
- 需保持高对比：背景极暗、霓虹极亮
- 适量使用雾气与颗粒，避免画面过于干净
- 动画节奏偏慢、偶尔闪烁，模拟不稳定的霓虹灯
- 避免大面积纯白或高饱和其他颜色，以免破坏 Noir 氛围


---

## English Version (en-US)

Please create a **Neon Noir** style interface using TailwindCSS, combining cyberpunk neon lights with film noir high-contrast lighting to evoke rainy streets, bar entrances, and music/nightclub platforms.

**Core Design Requirements**

1. **Film Noir Dark Background**
   - Use near-black gradients: \`#050509 → #0a0a0a → #1a0a14\`
   - Add subtle fog, vignette, and grain to simulate analog film
   - Example:
     \`\`\`css
     .neon-noir-bg {
       background:
         radial-gradient(circle at top, #1a0a14 0%, #050509 40%, #000000 100%);
       color: #f9fafb;
     }

     .neon-noir-vignette::before {
       content: '';
       position: absolute;
       inset: 0;
       pointer-events: none;
       background:
         radial-gradient(circle at center,
           transparent 0%,
           transparent 45%,
           rgba(0, 0, 0, 0.75) 100%);
     }
     \`\`\`

2. **Neon Pink-Purple Glow**
   - Primary colors: \`#ff0055\`, \`#ff00ff\`, \`#b967ff\`
   - Background accent: dark red / wine tones \`#1a0a14\`, \`#140812\`
   - Example:
     \`\`\`css
     .neon-noir-pink {
       color: #ff0055;
       text-shadow:
         0 0 10px rgba(255, 0, 85, 0.9),
         0 0 25px rgba(255, 0, 85, 0.7),
         0 0 40px rgba(255, 0, 85, 0.5);
     }

     .neon-noir-purple {
       color: #b967ff;
       text-shadow:
         0 0 12px rgba(185, 103, 255, 0.9),
         0 0 24px rgba(185, 103, 255, 0.7);
     }

     .neon-noir-border {
       border: 1px solid rgba(255, 0, 85, 0.7);
       box-shadow:
         0 0 20px rgba(255, 0, 85, 0.6),
         0 0 40px rgba(255, 0, 85, 0.4);
     }
     \`\`\`

3. **Neon Sign Typography**
   - Use uppercase titles with wide letter-spacing: \`0.12em–0.2em\`
   - Simulate neon signage through multi-layer text-shadow and flicker
   - Example:
     \`\`\`css
     .neon-noir-title {
       font-size: clamp(1.75rem, 3vw, 3rem);
       font-weight: 900;
       letter-spacing: 0.16em;
       color: #ff0055;
       text-transform: uppercase;
       text-shadow:
         0 0 10px rgba(255, 0, 85, 0.9),
         0 0 20px rgba(255, 0, 85, 0.8),
         0 0 40px rgba(255, 0, 85, 0.6);
       animation: neonNoirFlicker 4s ease-in-out infinite;
     }
     \`\`\`

4. **Fog and Glow Particles**
   - Use blurred radial gradients as neon glow and street fog
   - Particles float slowly (4–10s) to keep the noir mood
   - Example:
     \`\`\`css
     .neon-noir-fog {
       position: absolute;
       width: 200px;
       height: 200px;
       border-radius: 9999px;
       background: radial-gradient(circle,
         rgba(255, 0, 85, 0.25),
         transparent 70%);
       filter: blur(35px);
       animation: noirFogFloat 8s ease-in-out infinite;
     }
     \`\`\`

5. **Cards and Music Platform Modules**
   - Typical use case: music platform / nightclub event page
   - Card design:
     - Semi-transparent dark surface: \`rgba(10, 10, 16, 0.8)\`
     - Neon borders with soft inner shadow
     - Titles in neon, descriptions in muted gray
   - Example:
     \`\`\`css
     .neon-noir-card {
       background: rgba(10, 10, 16, 0.8);
       border-radius: 1rem;
       border: 1px solid rgba(185, 103, 255, 0.6);
       box-shadow:
         0 0 24px rgba(185, 103, 255, 0.4),
         0 20px 40px rgba(0, 0, 0, 0.7);
       padding: 1.25rem 1.5rem;
     }

     .neon-noir-card-title {
       font-weight: 700;
       color: #ff00ff;
       letter-spacing: 0.08em;
     }
     \`\`\`

6. **Interactions and Buttons**
   - Buttons should feel like neon switches: glow on hover, slight press on active
   - Prefer outline + transparent background combinations
   - Example:
     \`\`\`css
     .neon-noir-button {
       padding: 0.75rem 1.75rem;
       border-radius: 9999px;
       border: 1px solid rgba(255, 0, 85, 0.8);
       background: rgba(5, 5, 10, 0.8);
       color: #ff0055;
       font-weight: 600;
       letter-spacing: 0.08em;
       text-transform: uppercase;
       box-shadow:
         0 0 16px rgba(255, 0, 85, 0.5),
         0 8px 18px rgba(0, 0, 0, 0.8);
       transition: all 0.25s ease-out;
     }
     \`\`\`

**Color Scheme (Neon Noir)**

- Background: \`#0a0a0a\`, \`#050509\`, \`#1a0a14\`
- Neon: \`#ff0055\`, \`#ff00ff\`, \`#b967ff\`
- Text: \`#f9fafb\` (primary), \`#9ca3af\` (secondary)

**Important Notes**
- Maintain strong contrast: very dark background, very bright neon
- Use fog and grain sparingly but visibly to avoid a too-clean digital look
- Animation tempo should be slow with occasional flicker to mimic unstable neon
- Avoid large bright white areas or non-neon saturated colors that break the noir mood

**Typography Recommendations**
- Headlines: Use bold sans-serif with tight tracking (e.g., Inter, Poppins) at 700-900 weight
- Body text: 16-18px with 1.6-1.8 line-height for readability on dark backgrounds
- Accent text: Use uppercase with letter-spacing of 0.08-0.12em for a dystopian feel
- Monospace: Use Space Mono or JetBrains Mono for code blocks or terminal-style elements

**Responsive Considerations**
- On mobile devices, reduce glow intensity (fewer shadow layers) to improve performance
- Stack cards vertically with consistent spacing (space-y-6 or space-y-8)
- Scale down font sizes appropriately (clamp values for fluid typography)
- Consider disabling complex animations on smaller screens using `@media (max-width: 768px)`

**Browser Support Notes**
- `backdrop-filter` requires `-webkit-` prefix for Safari compatibility
- Test neon glow effects across different browsers (may render differently in Firefox vs Chrome)
- Provide fallback backgrounds for older browsers that don't support `backdrop-filter`
- Use CSS custom properties (variables) for easy theme adjustments
