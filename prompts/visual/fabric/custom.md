# Custom Prompt

## 中文版本 (zh-CN)

设计织物质感（Fabric Texture）风格界面，使用布料纹理创造温暖手工艺感。

**核心视觉特征**：亚麻/帆布纹理背景、柔和自然阴影、缝线风格边框、编织图案装饰、温暖大地色调、手工艺品质感。

**色彩系统**：温暖中性色（米色#f5f5dc, 亚麻色#faf0e6, 卡其色#f0e68c, 浅褐#d2b48c）、深棕色文字（#3e2723, #4e342e）、柔和点缀色（铁锈红#b7410e, 橄榄绿#808000, 靛蓝#4b0082）。

**纹理实现**：
```css
/* 亚麻纹理 */
.fabric-bg {
  background-image:
    linear-gradient(90deg, rgba(0,0,0,.03) 1px, transparent 1px),
    linear-gradient(rgba(0,0,0,.03) 1px, transparent 1px);
  background-size: 20px 20px;
  background-color: #faf0e6;
}

/* 缝线边框 */
.stitched-border {
  border: 2px dashed #8b4513;
  border-radius: 8px;
  box-shadow: 0 0 0 4px #faf0e6, 0 0 0 5px #8b4513;
}
```

**布局与组件**：卡片使用缝线边框、按钮模拟布料质感、标题使用手写字体、图标线描风格、纹理背景不要过于强烈、保持充足留白营造手工质感。

**动画**：柔和过渡（300-500ms ease-in-out）、悬停时轻微浮起、避免过于光滑的动画（保持手工感）。

**典型应用**：手工艺品商店、时尚/服装品牌、家居/室内设计、文创产品、烘焙/咖啡店、复古风格博客。


---

## English Version (en-US)

Design fabric texture style interfaces using cloth textures to create warm handcrafted feel.

**Core Visual Characteristics**: Linen/canvas texture backgrounds, soft natural shadows, stitched-style borders, woven pattern decorations, warm earth tone palette, handcrafted quality.

**Color System**: Warm neutrals (beige#f5f5dc, linen#faf0e6, khaki#f0e68c, tan#d2b48c), deep brown text (#3e2723, #4e342e), soft accent colors (rust red#b7410e, olive green#808000, indigo#4b0082).

**Texture Implementation**:
```css
/* Linen texture */
.fabric-bg {
  background-image:
    linear-gradient(90deg, rgba(0,0,0,.03) 1px, transparent 1px),
    linear-gradient(rgba(0,0,0,.03) 1px, transparent 1px);
  background-size: 20px 20px;
  background-color: #faf0e6;
}

/* Stitched border */
.stitched-border {
  border: 2px dashed #8b4513;
  border-radius: 8px;
  box-shadow: 0 0 0 4px #faf0e6, 0 0 0 5px #8b4513;
}
```

**Layout & Components**: Cards with stitched borders, buttons simulating fabric texture, titles in handwritten fonts, line-drawn icons, texture backgrounds not too intense, ample whitespace for handcrafted feel.

**Animation**: Soft transitions (300-500ms ease-in-out), slight lift on hover, avoid overly smooth animations (maintain handcrafted feel).

**Typical Applications**: Handcraft stores, fashion/clothing brands, home/interior design, cultural creative products, bakery/coffee shops, vintage style blogs.
