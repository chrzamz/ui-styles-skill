# Custom Prompt

## 中文版本 (zh-CN)

设计双色调（Duotone）风格界面，使用两种主色创造高对比度的大胆视觉效果。

**核心视觉特征**：仅用两种主色+中性色、高对比度视觉冲击、图片应用双色滤镜、大胆的色块分割、扁平化设计风格、强烈的品牌识别度。

**色彩系统**：选择两种高对比度颜色作为主色（如蓝#3b82f6+橙#f97316，紫#a855f7+黄#eab308，红#ef4444+青#06b6d4）。中性色用于文字和背景（白色#fff，深灰#1a1a1a）。图片使用 CSS filter 或 mix-blend-mode 应用双色效果。

**技术实现**：
```css
/* 双色图片效果 */
.duotone-image {
  filter: grayscale(100%) contrast(1.2);
  mix-blend-mode: multiply;
  background: linear-gradient(to right, #3b82f6, #f97316);
}
```

**布局与组件**：Hero 区域大面积使用主色1、次要区域使用主色2、交替色块分割页面、按钮和 CTA 使用对比色、图标和插画采用双色设计、文字保持中性色确保可读性。

**动画**：颜色切换动画（hover 时主色1 ↔ 主色2）、滑动时渐变位置变化、简洁快速过渡（200-300ms）。

**典型应用**：音乐/娱乐品牌、运动品牌、青年文化产品、艺术/设计作品集、活动/音乐节海报风格网站。


---

## English Version (en-US)

Design duotone style interfaces using two primary colors to create high-contrast bold visual effects.

**Core Visual Characteristics**: Only two primary colors + neutrals, high-contrast visual impact, duotone filters on images, bold color blocking, flat design style, strong brand recognition.

**Color System**: Choose two high-contrast colors as primaries (e.g., blue#3b82f6+orange#f97316, purple#a855f7+yellow#eab308, red#ef4444+cyan#06b6d4). Neutrals for text and backgrounds (white#fff, dark gray#1a1a1a). Images use CSS filter or mix-blend-mode for duotone effects.

**Technical Implementation**:
```css
/* Duotone image effect */
.duotone-image {
  filter: grayscale(100%) contrast(1.2);
  mix-blend-mode: multiply;
  background: linear-gradient(to right, #3b82f6, #f97316);
}
```

**Layout & Components**: Hero section with large primary color 1 area, secondary sections use primary color 2, alternating color blocks divide page, buttons and CTAs use contrast color, icons and illustrations in duotone design, text remains neutral for readability.

**Animation**: Color switching animations (hover primary 1 ↔ primary 2), gradient position changes on scroll, clean fast transitions (200-300ms).

**Typical Applications**: Music/entertainment brands, sports brands, youth culture products, art/design portfolios, event/festival poster-style websites.
