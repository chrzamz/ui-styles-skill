# Custom Prompt

## 中文版本 (zh-CN)

你现在是一名资深 UI 设计师兼前端工程师，请生成一个与当前「扁平化（Flat Design）」核心样式卡展示界面风格高度接近的 Flat Design 风格 UI。
请使用 TailwindCSS 创建一个扁平化（Flat Design）风格的界面，使用纯色和简洁几何形状，完全去除阴影、渐变和纹理等装饰效果。

**核心设计要求**

1. **零装饰原则**
   - 完全移除阴影: box-shadow: none;
   - 禁用渐变: 仅使用纯色背景（background: #3498db;）
   - 无纹理效果: 保持纯色平面，不使用 background-image
   - 无边框或极简边框: border: none; 或 border: 1px solid #ecf0f1;

2. **纯色配色系统**
   - 主色使用纯色: background: #3498db;（不使用 rgba 或 gradient）
   - 高对比度配色: 白底黑字 (#ffffff + #2c3e50) 或深底白字 (#2c3e50 + #ffffff)
   - 色彩分块明确: 每个区域使用单一纯色，边界清晰
   - 颜色即层级: 通过颜色深浅区分重要性，而非阴影深度

3. **简洁几何形状**
   - 统一圆角: border-radius: 4px;（小圆角）或 8px（中圆角）
   - 矩形为主: 使用 <div> 矩形容器承载内容
   - 圆形图标: border-radius: 50%;（头像、按钮）
   - 直线分隔: border-bottom: 1px solid #ecf0f1;（替代阴影）

4. **视觉层次建立**
   - 颜色对比: 使用不同亮度的颜色区分层级（#3498db 主按钮 vs #95a5a6 次要按钮）
   - 尺寸对比: font-size: 24px（标题）vs 16px（正文）vs 14px（辅助文字）
   - 留白分隔: padding: 24px; margin: 16px;（用留白代替边框）
   - 排版层次: font-weight: 700（重要）vs 400（常规）vs 300（轻量）

5. **大胆色彩应用**
   - 鲜明主色: #3498db（蓝）, #e74c3c（红）, #2ecc71（绿）, #f39c12（黄）
   - 冷暖对比: 蓝色系（#3498db, #2980b9）vs 橙色系（#e67e22, #d35400）
   - 有限色板: 每个界面使用 2-4 种主要颜色
   - 中性色辅助: #ecf0f1（浅灰背景）, #2c3e50（深灰文字）

**配色方案（鲜明纯色）**

主色调：
- 蓝色: #3498db, #2980b9
- 红色: #e74c3c, #c0392b
- 绿色: #2ecc71, #27ae60
- 黄色: #f39c12, #f1c40f

中性色：
- 深灰: #2c3e50, #34495e
- 浅灰: #ecf0f1, #bdc3c7
- 纯白: #ffffff
- 纯黑: #000000

强调色：
- 紫色: #9b59b6, #8e44ad
- 橙色: #e67e22, #d35400
- 青色: #1abc9c, #16a085

**关键 CSS 类示例**

\`\`\`css
/* 扁平化按钮 */
.flat-button {
  background: #3498db;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  padding: 12px 24px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s ease;
  box-shadow: none; /* 关键：无阴影 */
}

.flat-button:hover {
  background: #2980b9; /* 仅改变颜色 */
}

.flat-button:active {
  background: #21618c; /* 按下时更深 */
}

/* 扁平化卡片 */
.flat-card {
  background: #ffffff;
  border: 1px solid #ecf0f1;
  border-radius: 8px;
  padding: 24px;
  box-shadow: none; /* 关键：无阴影 */
}

/* 扁平化导航栏 */
.flat-navbar {
  background: #2c3e50;
  color: #ffffff;
  padding: 16px 24px;
  border-bottom: 3px solid #3498db; /* 使用彩色边框代替阴影 */
}

/* 扁平化输入框 */
.flat-input {
  background: #ecf0f1;
  border: 2px solid #bdc3c7;
  border-radius: 4px;
  padding: 12px 16px;
  font-size: 16px;
  transition: border-color 0.2s ease;
  box-shadow: none;
}

.flat-input:focus {
  border-color: #3498db;
  outline: none;
}
\`\`\`

**图标系统**
- 使用线性图标（Feather Icons、Heroicons）
- 统一线宽: stroke-width: 2px;
- 单色填充: color: #3498db; 或 fill: #3498db;
- 尺寸统一: width: 24px; height: 24px;

**重要提示**
- 绝对不使用 box-shadow（扁平化的核心特征）
- 所有背景必须是纯色，不使用渐变
- 通过颜色对比和留白建立层次，而非视觉深度
- 保持高对比度，确保文字可读性（WCAG AA 标准）
- 交互反馈仅通过颜色变化，不使用阴影或位移


---

## English Version (en-US)

Please create a Flat Design style interface using TailwindCSS, with solid colors and simple geometric shapes, completely removing shadows, gradients, and textures.

**Core Design Requirements**

1. **Zero Decoration Principle**
   - Completely remove shadows: box-shadow: none;
   - No gradients: Use only solid colors (background: #3498db;)
   - No textures: Keep solid color planes, no background-image
   - No borders or minimal borders: border: none; or border: 1px solid #ecf0f1;

2. **Solid Color System**
   - Primary colors as solid: background: #3498db; (no rgba or gradient)
   - High contrast pairing: White bg + dark text (#ffffff + #2c3e50) or dark bg + white text
   - Clear color blocks: Each area uses single solid color with clear boundaries
   - Color as hierarchy: Use color depth for importance, not shadow depth

3. **Simple Geometric Shapes**
   - Unified border radius: border-radius: 4px; (small) or 8px (medium)
   - Rectangle dominant: Use <div> rectangular containers
   - Circular icons: border-radius: 50%; (avatars, buttons)
   - Straight dividers: border-bottom: 1px solid #ecf0f1; (replace shadows)

4. **Visual Hierarchy Establishment**
   - Color contrast: Different brightness for hierarchy (#3498db primary vs #95a5a6 secondary)
   - Size contrast: font-size: 24px (heading) vs 16px (body) vs 14px (auxiliary)
   - Whitespace separation: padding: 24px; margin: 16px; (replace borders)
   - Typography hierarchy: font-weight: 700 (important) vs 400 (regular) vs 300 (light)

5. **Bold Color Application**
   - Vivid primary colors: #3498db (blue), #e74c3c (red), #2ecc71 (green), #f39c12 (yellow)
   - Warm/cool contrast: Blue (#3498db, #2980b9) vs Orange (#e67e22, #d35400)
   - Limited palette: Use 2-4 main colors per interface
   - Neutral support: #ecf0f1 (light gray bg), #2c3e50 (dark gray text)

**Color Scheme (Vivid Solid Colors)**

Primary colors:
- Blue: #3498db, #2980b9
- Red: #e74c3c, #c0392b
- Green: #2ecc71, #27ae60
- Yellow: #f39c12, #f1c40f

Neutral colors:
- Dark gray: #2c3e50, #34495e
- Light gray: #ecf0f1, #bdc3c7
- Pure white: #ffffff
- Pure black: #000000

Accent colors:
- Purple: #9b59b6, #8e44ad
- Orange: #e67e22, #d35400
- Teal: #1abc9c, #16a085

**Key CSS Class Examples**

\`\`\`css
/* Flat Button */
.flat-button {
  background: #3498db;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  padding: 12px 24px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s ease;
  box-shadow: none; /* Key: no shadow */
}

.flat-button:hover {
  background: #2980b9; /* Only change color */
}

.flat-button:active {
  background: #21618c; /* Darker when pressed */
}

/* Flat Card */
.flat-card {
  background: #ffffff;
  border: 1px solid #ecf0f1;
  border-radius: 8px;
  padding: 24px;
  box-shadow: none; /* Key: no shadow */
}

/* Flat Navbar */
.flat-navbar {
  background: #2c3e50;
  color: #ffffff;
  padding: 16px 24px;
  border-bottom: 3px solid #3498db; /* Use colored border instead of shadow */
}

/* Flat Input */
.flat-input {
  background: #ecf0f1;
  border: 2px solid #bdc3c7;
  border-radius: 4px;
  padding: 12px 16px;
  font-size: 16px;
  transition: border-color 0.2s ease;
  box-shadow: none;
}

.flat-input:focus {
  border-color: #3498db;
  outline: none;
}
\`\`\`

**Icon System**
- Use linear icons (Feather Icons, Heroicons)
- Uniform stroke width: stroke-width: 2px;
- Single color fill: color: #3498db; or fill: #3498db;
- Uniform size: width: 24px; height: 24px;

**Important Notes**
- Absolutely no box-shadow (core characteristic of flat design)
- All backgrounds must be solid colors, no gradients
- Establish hierarchy through color contrast and whitespace, not visual depth
- Maintain high contrast for text readability (WCAG AA standard)
- Interaction feedback only through color changes, no shadows or translations
