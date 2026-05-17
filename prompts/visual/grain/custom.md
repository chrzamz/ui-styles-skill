# Custom Prompt

## 中文版本 (zh-CN)

你现在是一位精通噪点质感与胶片美学设计的资深 UI 设计师兼前端工程师。请为我创建一个带有电影胶片噪点质感的网页，要求如下：

### 核心视觉特征
- **噪点纹理**：在背景与卡片上叠加低透明度噪点纹理，模拟胶片颗粒感
- **复古配色**：使用低饱和度的暖色调（米黄、棕褐、淡橙）或冷色调（灰蓝、青灰）
- **柔和对比**：避免高对比度，营造柔和、怀旧的视觉体验
- **纸质质感**：卡片与元素带有类似纸张或老照片的质感

### 噪点实现技术
- **CSS 噪点**：使用 background: url('data:image/svg+xml,<svg>...')创建SVG噪点纹理
- **伪元素叠加**：使用 ::before 或 ::after 伪元素叠加噪点层，设置 pointer-events: none
- **Canvas 噪点**：使用 Canvas 动态生成噪点纹理，并通过 toDataURL() 转为背景图
- **透明度控制**：噪点层透明度设置在 0.03-0.15 之间，避免过于明显

### 页面结构
1. **Hero 区域**：大标题，背景为浅色 + 细微噪点，营造老照片感
2. **卡片/按钮示例**：3-4 个卡片，每个卡片背景叠加噪点纹理，展示不同配色
3. **图文分栏**：一侧文字，一侧图片（带噪点边框或叠加层），图文搭配呈现
4. **装饰元素**：页面边缘可有老旧纸张的撕裂边缘或磨损效果

### 配色方案
- **暖色调**：米黄（#f5f1e8, #faf6ed）、棕褐（#d4c5b9, #c9b8a8）、淡橙（#f4e1d2）
- **冷色调**：灰蓝（#d5dce0, #c8d0d4）、青灰（#cad5d8, #b8c5c9）、淡绿（#e0e8d8）
- **文字色**：深灰（#3a3d40, #4a4d50）、深褐（#5a4a3a），避免纯黑
- **强调色**：低饱和度橙（#e8b389）、棕红（#c9887a），用于 CTA 按钮

### 噪点纹理生成
**SVG 噪点**（轻量级方案）：
```html
<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>
  <filter id='noise'>
    <feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' />
  </filter>
  <rect width='100%' height='100%' filter='url(#noise)' />
</svg>
```

**Canvas 噪点**（动态方案）：
```javascript
const canvas = document.createElement('canvas');
canvas.width = 300;
canvas.height = 300;
const ctx = canvas.getContext('2d');
const imageData = ctx.createImageData(300, 300);
for (let i = 0; i < imageData.data.length; i += 4) {
  const noise = Math.random() * 255;
  imageData.data[i] = imageData.data[i+1] = imageData.data[i+2] = noise;
  imageData.data[i+3] = 255;
}
ctx.putImageData(imageData, 0, 0);
const noiseURL = canvas.toDataURL();
```

### 噪点应用方式
- **背景噪点**：页面底色叠加大面积噪点层（opacity: 0.05-0.1）
- **卡片噪点**：卡片背景叠加噪点层（opacity: 0.08-0.12），增强质感
- **图片噪点**：图片上叠加噪点层（使用 mix-blend-mode: multiply），模拟老照片
- **边框噪点**：边框使用噪点纹理而非纯色，增强复古感

### 动画与交互
- **静态优先**：噪点纹理通常为静态，避免动态噪点影响性能
- **动态噪点**（可选）：使用 Canvas 动画每帧生成新噪点，模拟胶片播放（需谨慎使用）
- **hover 效果**：卡片 hover 时噪点透明度略微增加或减少，营造微妙变化
- **淡入淡出**：页面元素淡入时噪点同步出现，增强整体感

### 文字排版
- **字体选择**：使用衬线字体（如 Georgia, Times New Roman）或复古等宽字体
- **字号**：标题 32-48px，正文 16-18px，不宜过小
- **行高**：1.7-1.9，营造舒适的阅读体验
- **字重**：400-600，避免过细或过粗

### 性能优化
- **静态噪点**：使用预生成的噪点图片或 SVG data-url，避免实时生成
- **CSS 背景复用**：噪点纹理定义为 CSS 变量，在多个元素中复用
- **透明度控制**：噪点透明度尽量低（≤ 0.15），减少视觉干扰与渲染负担
- **避免过大图片**：噪点纹理尺寸控制在 300x300px 以内，通过 repeat 平铺

### 技术要点
- 使用 CSS 变量定义噪点纹理（--grain-texture）和配色（--grain-bg, --grain-text）
- 使用 ::before 伪元素叠加噪点层，设置 pointer-events: none 避免遮挡交互
- 使用 mix-blend-mode: multiply 或 overlay 融合噪点与背景色
- 可选：使用 Canvas 实时生成噪点纹理，实现动态噪点效果

### 情感与氛围
- **怀旧感**：噪点纹理模拟胶片照片或老电影的颗粒感
- **温暖柔和**：低饱和度配色、柔和对比营造温馨氛围
- **质感真实**：纸质或胶片质感增强视觉真实感
- **时光感**：噪点与复古配色传达时光流逝的美感

### 输出要求
请生成完整的 HTML 结构与内联样式，确保：
- 代码清晰注释，说明噪点纹理的生成与应用方式
- 噪点纹理与配色使用 CSS 变量，便于调整
- 噪点透明度适中，不影响内容可读性
- 页面传达出复古、质感、怀旧的胶片美学氛围


---

## English Version (en-US)

You are a senior UI designer and frontend engineer specializing in grain texture and film aesthetics. Create a webpage with cinematic film grain texture with the following requirements:

### Core Visual Characteristics
- **Grain Texture**: Overlay low-opacity grain texture on backgrounds and cards simulating film grain
- **Vintage Palette**: Use low-saturation warm tones (beige, sepia, pale orange) or cool tones (gray-blue, cyan-gray)
- **Soft Contrast**: Avoid high contrast, creating soft, nostalgic visual experience
- **Paper Texture**: Cards and elements have paper-like or old photo texture

### Grain Implementation Techniques
- **CSS Grain**: Use background: url('data:image/svg+xml,<svg>...') to create SVG grain texture
- **Pseudo-Element Overlay**: Use ::before or ::after pseudo-elements to overlay grain layer with pointer-events: none
- **Canvas Grain**: Use Canvas to dynamically generate grain texture and convert to background via toDataURL()
- **Opacity Control**: Set grain layer opacity between 0.03-0.15 to avoid being too obvious

### Page Structure
1. **Hero Section**: Large headline with light background + subtle grain creating old photo feel
2. **Card/Button Examples**: 3-4 cards each with grain texture overlay on background showing different color schemes
3. **Text-Image Split**: Text on one side, image on other (with grain border or overlay), text-image pairing
4. **Decorative Elements**: Page edges may have torn paper edges or worn effects

### Color Scheme
- **Warm Tones**: Beige (#f5f1e8, #faf6ed), sepia (#d4c5b9, #c9b8a8), pale orange (#f4e1d2)
- **Cool Tones**: Gray-blue (#d5dce0, #c8d0d4), cyan-gray (#cad5d8, #b8c5c9), pale green (#e0e8d8)
- **Text Colors**: Dark gray (#3a3d40, #4a4d50), dark brown (#5a4a3a), avoid pure black
- **Accent Colors**: Low-saturation orange (#e8b389), brownish-red (#c9887a) for CTA buttons

### Grain Texture Generation
**SVG Grain** (lightweight solution):
```html
<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>
  <filter id='noise'>
    <feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' />
  </filter>
  <rect width='100%' height='100%' filter='url(#noise)' />
</svg>
```

**Canvas Grain** (dynamic solution):
```javascript
const canvas = document.createElement('canvas');
canvas.width = 300;
canvas.height = 300;
const ctx = canvas.getContext('2d');
const imageData = ctx.createImageData(300, 300);
for (let i = 0; i < imageData.data.length; i += 4) {
  const noise = Math.random() * 255;
  imageData.data[i] = imageData.data[i+1] = imageData.data[i+2] = noise;
  imageData.data[i+3] = 255;
}
ctx.putImageData(imageData, 0, 0);
const noiseURL = canvas.toDataURL();
```

### Grain Application Methods
- **Background Grain**: Page base color overlays large grain layer (opacity: 0.05-0.1)
- **Card Grain**: Card backgrounds overlay grain layer (opacity: 0.08-0.12) enhancing texture
- **Image Grain**: Images overlay grain layer (using mix-blend-mode: multiply) simulating old photos
- **Border Grain**: Borders use grain texture rather than solid color enhancing vintage feel

### Animation & Interaction
- **Static Priority**: Grain texture usually static, avoid dynamic grain affecting performance
- **Dynamic Grain** (optional): Use Canvas animation to generate new grain each frame simulating film playback (use cautiously)
- **Hover Effect**: Card hover slightly increases or decreases grain opacity creating subtle changes
- **Fade In/Out**: Elements fade in with grain appearing simultaneously enhancing unity

### Typography
- **Font Choice**: Use serif fonts (like Georgia, Times New Roman) or vintage monospace fonts
- **Font Size**: Headlines 32-48px, body 16-18px, not too small
- **Line Height**: 1.7-1.9 creating comfortable reading experience
- **Font Weight**: 400-600, avoid too thin or too thick

### Performance Optimization
- **Static Grain**: Use pre-generated grain images or SVG data-url avoiding real-time generation
- **CSS Background Reuse**: Define grain texture as CSS variable reusing across multiple elements
- **Opacity Control**: Keep grain opacity low (≤ 0.15) reducing visual interference and rendering burden
- **Avoid Large Images**: Control grain texture size within 300x300px, tile via repeat

### Technical Points
- Use CSS variables to define grain texture (--grain-texture) and color scheme (--grain-bg, --grain-text)
- Use ::before pseudo-element to overlay grain layer with pointer-events: none avoiding interaction blocking
- Use mix-blend-mode: multiply or overlay to blend grain with background color
- Optional: Use Canvas to generate grain texture in real-time for dynamic grain effects

### Emotion & Atmosphere
- **Nostalgic Feel**: Grain texture simulates film photo or old movie grain
- **Warm Soft**: Low-saturation colors, soft contrast creating cozy atmosphere
- **Textural Realism**: Paper or film texture enhances visual authenticity
- **Time Sense**: Grain and vintage colors convey beauty of time passage

### Output Requirements
Generate complete HTML structure with inline styles ensuring:
- Clear code comments explaining grain texture generation and application methods
- Grain texture and colors use CSS variables for adjustment
- Grain opacity moderate not affecting content readability
- Page conveys vintage, textural, nostalgic film aesthetic atmosphere
