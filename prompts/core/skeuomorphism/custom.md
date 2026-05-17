# Custom Prompt

## 中文版本 (zh-CN)

此模板用于指导 AI 生成高质量的拟物化（Skeuomorphism）风格界面。

### 核心指令
**"请使用 TailwindCSS 创建一个拟物化（Skeuomorphism）风格的界面，模拟真实世界的材质和物理特性。"**

### 1. 核心设计要求 (Core Design Requirements)

拟物化设计的精髓在于对光影、材质纹理和物理体积的极致模拟。以下是构建此风格必须遵循的 7 个核心要求：

#### 1.1 多层阴影系统 (Multi-layer Shadow System)
真实的物体不会只有一层简单的阴影。需要通过组合多层 `box-shadow` 来模拟主光源投射的阴影（Drop Shadow）、环境光遮蔽（Ambient Occlusion）以及边缘的高光反射（Specular Highlight）。

*   **光源设定**：通常设定在左上角（135度），导致高光在左上，阴影在右下。
*   **混合模式**：深色阴影建议使用 `multiply` 混合模式的模拟色，高光建议使用 `screen` 或 `overlay`。

```css
/* Tailwind 任意值示例 - 复杂按钮阴影 */
.shadow-skeuo {
  box-shadow:
    /* 外部深色投射阴影 (右下) */
    6px 6px 12px 0px rgba(0, 0, 0, 0.25),
    /* 外部环境光阴影 (紧贴) */
    2px 2px 4px 0px rgba(0, 0, 0, 0.15),
    /* 外部高光反射 (左上) */
    -6px -6px 12px 0px rgba(255, 255, 255, 0.1),
    /* 内部高光 (营造边缘倒角感) */
    inset 1px 1px 0px 0px rgba(255, 255, 255, 0.2),
    /* 内部反光 (营造体积感) */
    inset -1px -1px 0px 0px rgba(0, 0, 0, 0.1);
}
```

#### 1.2 渐变模拟材质光泽 (Gradient Material Simulation)
拒绝纯色背景。现实世界的材质表面总是因为曲率变化而呈现微妙的渐变。

*   **金属质感**：使用对角线线性渐变，模拟金属拉丝或光泽漫反射。
*   **皮革/木纹**：使用深色系的细微径向渐变，中心稍亮，边缘稍暗，模拟老化或光照集中效果。

```css
/* 金属拉丝银色表面 */
.bg-metal-gradient {
  background: linear-gradient(
    135deg,
    #e0e0e0 0%,
    #f5f5f5 50%,
    #d4d4d4 51%,
    #c0c0c0 100%
  );
}

/* 深空灰磨砂金属 */
.bg-dark-metal {
  background: linear-gradient(
    145deg,
    #3a4b5f 0%,
    #2c3e50 100%
  );
}

/* 木纹表面 */
.bg-wood {
  background: linear-gradient(
    180deg,
    #8b4513 0%,
    #654321 100%
  );
}

/* 皮革质感 */
.bg-leather {
  background: linear-gradient(
    180deg,
    #4a3c31 0%,
    #2c2117 100%
  );
}
```

#### 1.3 立体边框效果 (3D Border Effects)
边框不是简单的描边，而是表现物体厚度的关键。通过分别控制上下左右边框的颜色，可以模拟出凸起或凹陷的棱角。

*   **凸起物体**：上/左边框亮（受光面），下/右边框暗（背光面）。
*   **凹陷物体（如输入框）**：上/左边框暗（内部阴影投射），下/右边框亮（底部边缘反光）。

```css
/* 凸起边框效果 */
.border-raised {
  border-top: 1px solid rgba(255, 255, 255, 0.4);
  border-left: 1px solid rgba(255, 255, 255, 0.4);
  border-bottom: 1px solid rgba(0, 0, 0, 0.3);
  border-right: 1px solid rgba(0, 0, 0, 0.3);
}

/* 凹陷边框效果 */
.border-recessed {
  border-top: 2px solid rgba(0, 0, 0, 0.4);
  border-left: 2px solid rgba(0, 0, 0, 0.4);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  border-right: 1px solid rgba(255, 255, 255, 0.1);
}
```

#### 1.4 物理反馈交互 (Physical Feedback Interactions)
交互不仅仅是颜色变化，更是物理位置和状态的改变。

*   **按下状态（Active）**：凸起的按钮被按下时，阴影范围应缩小（离地面更近），内容向右下方位移（1px-2px），并可能出现内阴影（变为凹陷状态）。
*   **悬停状态（Hover）**：亮度略微提升，阴影可能略微扩散（物体浮起）。

```css
/* 按钮默认状态 */
.skeuo-interactive {
  transform: translateY(0);
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
  transition: all 0.15s ease;
}

/* 悬停状态 */
.skeuo-interactive:hover {
  filter: brightness(110%);
  box-shadow: 0 6px 12px rgba(0,0,0,0.35);
}

/* 按钮点击物理位移 */
.skeuo-interactive:active {
  transform: translateY(2px) translateX(1px);
  box-shadow:
    inset 2px 2px 5px rgba(0,0,0,0.3),
    inset -2px -2px 5px rgba(255,255,255,0.1);
  filter: brightness(90%);
}
```

#### 1.5 文字质感效果 (Text Texture Effects)
文字应该看起来像是雕刻在材质上，或者像是贴在上面的金属铭牌。

*   **雕刻文字（Letterpress）**：文字颜色深于背景，下方有浅色投影（模拟凹槽底部高光），上方有深色投影（模拟凹槽顶部阴影）。
*   **凸起文字（Embossed）**：文字颜色浅于背景，下方有深色投影。

```css
/* 雕刻文字效果 */
.text-engraved {
  color: rgba(0, 0, 0, 0.6);
  text-shadow:
    0px 1px 1px rgba(255, 255, 255, 0.3), /* 底部高光 */
    0px -1px 0px rgba(0, 0, 0, 0.5);      /* 顶部内阴影 */
}

/* 凸起文字效果 */
.text-embossed {
  color: rgba(255, 255, 255, 0.9);
  text-shadow:
    0 1px 0 rgba(255,255,255,0.8),
    0 2px 3px rgba(0,0,0,0.3);
}

/* 发光文字效果 */
.text-glow {
  text-shadow:
    0 0 10px rgba(98, 110, 234, 0.8),
    0 0 20px rgba(98, 110, 234, 0.5);
}
```

#### 1.6 材质纹理叠加 (Material Texture Overlays)
过于光滑的表面会显得像塑料（除非是玻璃）。需要叠加噪点或纹理来增加真实感。

*   **噪点（Noise）**：使用 SVG 或 base64 噪点图片作为背景遮罩。
*   **皮革/织物**：使用细微的平铺纹理图案。

```css
/* 噪点纹理叠加类 */
.texture-noise {
  position: relative;
}
.texture-noise::before {
  content: "";
  position: absolute;
  inset: 0;
  opacity: 0.05;
  background-image: url("data:image/svg+xml,..."); /* 噪点SVG */
  pointer-events: none;
  mix-blend-mode: overlay;
}

/* 金属拉丝纹理 */
.texture-brushed::after {
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    90deg,
    transparent,
    transparent 1px,
    rgba(255,255,255,0.02) 1px,
    rgba(255,255,255,0.02) 2px
  );
  pointer-events: none;
}
```

#### 1.7 光影动态效果 (Dynamic Lighting)
如果可能，通过简单的 CSS 动画模拟光源的微小移动或金属光泽的流转，增加"活"的感觉。

```css
/* 模拟金属光泽流转 */
@keyframes sheen {
  0% { background-position: 0% 50%; }
  100% { background-position: 100% 50%; }
}
.metal-sheen:hover {
  background: linear-gradient(120deg, transparent 30%, rgba(255,255,255,0.4) 50%, transparent 70%);
  background-size: 200% 100%;
  animation: sheen 1s linear;
}

/* 光环扩散效果 */
@keyframes glow-pulse {
  0%, 100% { box-shadow: 0 0 10px rgba(102,126,234,0.3); }
  50% { box-shadow: 0 0 20px rgba(102,126,234,0.6); }
}
.glow-pulse {
  animation: glow-pulse 2s ease-in-out infinite;
}
```

### 2. 完整配色方案 (Color Palette)

请在 Tailwind 配置中注册以下颜色，以确保设计的一致性。

#### 基础材质色 (Materials)
*   **深灰金属 (Metal Base)**: `#2c3e50` (主色调), `#34495e` (亮部), `#4a5568` (环境色)
*   **深棕木纹 (Wood Base)**: `#4a3c31` (主色调), `#654321` (亮部), `#8b4513` (纹理色)
*   **深蓝玻璃 (Glass Base)**: `#1e3a5f` (主色调), `#2c5282` (透光色)

#### 光影功能色 (Lighting)
*   **高光 (Highlight)**:
    *   强高光: `#ffffff`
    *   金属高光: `#c0c0c0`
    *   柔和高光: `rgba(255, 255, 255, 0.5)`
*   **阴影 (Shadow)**:
    *   深部阴影: `rgba(0, 0, 0, 0.5)`
    *   环境阴影: `rgba(0, 0, 0, 0.3)`

#### 交互点缀色 (Accents)
*   **指示灯蓝 (Indicator Blue)**: `#667eea` (常态), `#7f9cf5` (发光态)
*   **琥珀金 (Amber Gold)**: `#f59e0b` (警告/高亮), `#fbbf24` (金属铭牌色)
*   **警示红 (Alert Red)**: `#e53e3e` (开关/错误)

### 3. 关键 CSS 类实现 (Key Component Implementations)

以下是基于 Tailwind CSS 的 5 个核心组件实现示例。

#### 3.1 拟物化按钮 (.skeuo-button)
*一个带有明显厚度和点击反馈的金属质感按钮。*

```html
<button class="
  relative overflow-hidden px-8 py-4 rounded-lg font-bold tracking-wider text-gray-200 uppercase
  /* 基础渐变背景 */
  bg-gradient-to-b from-[#34495e] to-[#2c3e50]
  /* 边框高光与阴影 */
  border-t border-l border-white/10 border-b border-r border-black/40
  /* 复杂外阴影 */
  shadow-[6px_6px_12px_rgba(0,0,0,0.4),-4px_-4px_10px_rgba(255,255,255,0.05)]
  /* 交互状态：Hover */
  hover:brightness-110 hover:shadow-[8px_8px_16px_rgba(0,0,0,0.45),-6px_-6px_14px_rgba(255,255,255,0.08)]
  /* 交互状态：Active (按下) */
  active:translate-y-[2px] active:translate-x-[1px]
  active:shadow-[inset_4px_4px_8px_rgba(0,0,0,0.5),inset_-4px_-4px_8px_rgba(255,255,255,0.05)]
  active:border-t-black/30 active:border-b-white/10
  transition-all duration-150 ease-out
">
  <!-- 内部文字雕刻效果 -->
  <span class="drop-shadow-[0_1px_1px_rgba(0,0,0,0.8)] text-shadow-[0_-1px_0_rgba(0,0,0,1)]">
    Execute
  </span>
</button>
```

#### 3.2 拟物化卡片 (.skeuo-card)
*作为内容容器，模拟放置在桌面上的实体面板，具有柔和的边缘和纹理。*

```html
<div class="
  relative p-6 rounded-xl
  /* 深色哑光金属背景 */
  bg-[#2c3e50]
  /* 噪点纹理叠加 (假设已配置texture-noise) */
  texture-noise
  /* 混合边框：顶部亮线，底部暗线 */
  ring-1 ring-white/5 ring-inset
  /* 深度阴影 */
  shadow-[10px_10px_20px_rgba(0,0,0,0.5),-8px_-8px_16px_rgba(255,255,255,0.03)]
">
  <!-- 卡片顶部的凹槽标题栏 -->
  <div class="
    -mx-2 -mt-2 mb-4 py-2 px-4 rounded bg-black/20
    border-b border-white/5 shadow-[inset_0_2px_4px_rgba(0,0,0,0.3)]
  ">
    <h3 class="text-gray-400 text-sm font-bold uppercase tracking-widest drop-shadow-md">
      System Control
    </h3>
  </div>
  <!-- 卡片内容 -->
  <div class="text-gray-300">
    Content goes here...
  </div>
</div>
```

#### 3.3 拟物化输入框 (.skeuo-input)
*模拟嵌入面板内部的凹槽显示屏或输入区域。*

```html
<div class="relative group">
  <input type="text" placeholder="Enter command..." class="
    w-full px-5 py-3 rounded-lg outline-none
    /* 深色凹陷背景 */
    bg-[#1a2634] text-gray-200
    /* 强烈的内阴影模拟凹陷深度 */
    shadow-[inset_4px_4px_10px_rgba(0,0,0,0.6),inset_-2px_-2px_6px_rgba(255,255,255,0.05)]
    /* 边框处理：底部反光，顶部阴影 */
    border-b border-white/10 border-t border-black/50 border-x border-black/30
    /* 占位符样式 */
    placeholder-gray-600
    /* 聚焦状态：内发光 */
    focus:shadow-[inset_2px_2px_5px_rgba(0,0,0,0.7),0_0_10px_rgba(102,126,234,0.3)]
    focus:text-blue-200
    transition-all duration-200
  " />
</div>
```

#### 3.4 拟物化开关 (.skeuo-switch)
*一个真实的物理拨动开关，具有清晰的开/关状态和机械感。*

```html
<!-- 开关底座 -->
<label class="
  relative inline-flex items-center cursor-pointer
  w-20 h-10 rounded-full
  /* 凹陷底座轨道 */
  bg-[#1a2634]
  shadow-[inset_3px_3px_6px_rgba(0,0,0,0.6),inset_-1px_-1px_2px_rgba(255,255,255,0.05)]
  border border-black/20
">
  <input type="checkbox" class="sr-only peer">

  <!-- 拨杆 (Thumb) -->
  <div class="
    absolute left-1 top-1 w-8 h-8 rounded-full
    /* 拨杆材质：凸起的金属/塑料球体 */
    bg-gradient-to-br from-[#4a5568] to-[#2d3748]
    /* 拨杆立体感 */
    shadow-[2px_2px_5px_rgba(0,0,0,0.5),inset_2px_2px_4px_rgba(255,255,255,0.2)]
    border border-t-white/10 border-b-black/40
    /* 状态过渡 */
    transition-all duration-300 ease-[cubic-bezier(0.68,-0.55,0.27,1.55)]
    /* 选中状态位置与样式 */
    peer-checked:translate-x-10
    peer-checked:bg-gradient-to-br peer-checked:from-[#667eea] peer-checked:to-[#5a67d8]
    peer-checked:shadow-[0_0_15px_rgba(102,126,234,0.6),2px_2px_5px_rgba(0,0,0,0.4)]
  ">
    <!-- 拨杆上的防滑纹理细节 -->
    <div class="absolute inset-0 flex items-center justify-center gap-[2px] opacity-30">
        <div class="w-[1px] h-4 bg-black/50"></div>
        <div class="w-[1px] h-4 bg-black/50"></div>
        <div class="w-[1px] h-4 bg-black/50"></div>
    </div>
  </div>
</label>
```

#### 3.5 拟物化面板 (.skeuo-panel)
*多层级的大型控制面板，包含螺丝钉装饰。*

```html
<div class="
  relative rounded-2xl p-8
  /* 面板主材质 */
  bg-[#2c3e50]
  /* 边缘高光倒角 */
  border-t-2 border-l border-white/10 border-b-4 border-r-2 border-black/50
  /* 巨大的投影，使其看起来浮在背景之上 */
  shadow-[20px_20px_60px_rgba(0,0,0,0.6),-10px_-10px_30px_rgba(255,255,255,0.05)]
">
  <!-- 装饰性螺丝钉 (四角) -->
  <div class="absolute top-4 left-4 w-3 h-3 rounded-full bg-gray-400 shadow-[inset_1px_1px_2px_rgba(0,0,0,0.8),1px_1px_0_rgba(255,255,255,0.2)] flex items-center justify-center">
    <div class="w-full h-[1px] bg-gray-600 rotate-45"></div>
    <div class="w-full h-[1px] bg-gray-600 -rotate-45"></div>
  </div>
  <div class="absolute top-4 right-4 w-3 h-3 rounded-full bg-gray-400 shadow-[inset_1px_1px_2px_rgba(0,0,0,0.8),1px_1px_0_rgba(255,255,255,0.2)] flex items-center justify-center">
    <div class="w-full h-[1px] bg-gray-600 rotate-12"></div> <!-- 随机角度 -->
    <div class="w-full h-[1px] bg-gray-600 -rotate-[78deg]"></div>
  </div>

  <!-- 面板内容区域 -->
  <div class="h-full w-full bg-[#243342] rounded-lg shadow-[inset_2px_2px_8px_rgba(0,0,0,0.4)] border border-white/5 p-4">
    <!-- Content -->
  </div>
</div>
```

### 4. Tailwind CSS 配置 (Configuration)

在 `tailwind.config.js` 中扩展以下配置以支持复杂的拟物化效果。

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        skeuo: {
          dark: '#2c3e50',
          darker: '#1a2634',
          light: '#34495e',
          highlight: 'rgba(255, 255, 255, 0.1)',
          shadow: 'rgba(0, 0, 0, 0.4)',
          accent: '#667eea',
          gold: '#f59e0b',
        }
      },
      boxShadow: {
        'skeuo-raised': '6px 6px 12px 0px rgba(0, 0, 0, 0.3), -4px -4px 10px 0px rgba(255, 255, 255, 0.05)',
        'skeuo-recessed': 'inset 4px 4px 8px 0px rgba(0, 0, 0, 0.4), inset -3px -3px 6px 0px rgba(255, 255, 255, 0.05)',
        'skeuo-flat': '2px 2px 5px 0px rgba(0, 0, 0, 0.2), -1px -1px 2px 0px rgba(255, 255, 255, 0.05)',
      },
      backgroundImage: {
        'metal-brushed': "linear-gradient(135deg, #34495e 0%, #2c3e50 100%)",
        'noise': "url('/path/to/noise.png')", // 需要准备噪点素材
      }
    }
  }
}
```

### 5. 重要提示 (Important Tips)

1.  **拒绝纯黑和纯白**：在拟物化风格中，几乎不使用 `#000` 或 `#fff` 作为背景色。使用深灰、深蓝或米色作为基础，纯色仅用于极亮的高光点。
2.  **光源一致性**：必须严格遵守光源方向（通常是左上角）。如果一个按钮的阴影在右下，那么所有元素的阴影都必须在右下，凹陷元素的内阴影则相反（左上深，右下亮）。
3.  **对比度控制**：拟物化界面由于包含大量阴影和渐变，容易导致视觉杂乱。务必保持文本与背景的足够对比度，必要时给文字加外发光或投影以提升可读性。
4.  **圆角处理**：圆角（Border Radius）越明显，物体的实体感越强。避免使用直角，那看起来像平面设计。
5.  **细节决定成败**：添加细微的杂色（Noise）、划痕纹理、螺丝钉、接缝线等细节，能极大提升真实感。
6.  **物理动效**：所有的过渡动画都应该是线性的或缓出的（ease-out），模拟物体在物理世界中的惯性。不要使用瞬间变化的动画。
7.  **层级观念**：始终思考 Z 轴。背景是地基，面板是地板，卡片是桌子，按钮是桌上的物体。层级越高，投影越扩散。
8.  **排版留白**：由于拟物化元素视觉比重很大（Heavy），需要比扁平化设计更多的留白来呼吸，否则界面会显得非常拥挤压抑。

---

## English Version (en-US)

This template is designed to guide AI in generating high-quality Skeuomorphism style interfaces.

### Core Instruction
**"Please create a Skeuomorphism style interface using TailwindCSS, simulating real-world materials and physical properties."**

### 1. Core Design Requirements

The essence of Skeuomorphism lies in the extreme simulation of light, shadow, material texture, and physical volume. The following 7 core requirements must be adhered to when building this style:

#### 1.1 Multi-layer Shadow System
Real objects never have just a single layer of simple shadow. You need to combine multiple `box-shadow` layers to simulate the Drop Shadow cast by the main light source, Ambient Occlusion, and the Specular Highlight on the edges.

*   **Light Source**: Usually set at the top-left (135 degrees), resulting in highlights on the top-left and shadows on the bottom-right.
*   **Blending Modes**: It is recommended to use `multiply` mode for dark shadows and `screen` or `overlay` for highlights.

```css
/* Tailwind Arbitrary Value Example - Complex Button Shadow */
.shadow-skeuo {
  box-shadow:
    /* External Dark Drop Shadow (Bottom Right) */
    6px 6px 12px 0px rgba(0, 0, 0, 0.25),
    /* External Ambient Shadow (Close) */
    2px 2px 4px 0px rgba(0, 0, 0, 0.15),
    /* External Highlight Reflection (Top Left) */
    -6px -6px 12px 0px rgba(255, 255, 255, 0.1),
    /* Internal Highlight (Creates Bevel Feel) */
    inset 1px 1px 0px 0px rgba(255, 255, 255, 0.2),
    /* Internal Reflection (Creates Volume) */
    inset -1px -1px 0px 0px rgba(0, 0, 0, 0.1);
}
```

#### 1.2 Gradient Material Simulation
Avoid solid background colors. Surfaces in the real world always show subtle gradients due to curvature changes.

*   **Metal Texture**: Use diagonal linear gradients to simulate brushed metal or diffuse light reflection.
*   **Leather/Wood**: Use subtle radial gradients in dark tones, lighter in the center and darker at the edges, to simulate aging or focused lighting.

```css
/* Brushed Silver Metal Surface */
.bg-metal-gradient {
  background: linear-gradient(
    135deg,
    #e0e0e0 0%,
    #f5f5f5 50%,
    #d4d4d4 51%,
    #c0c0c0 100%
  );
}

/* Deep Space Grey Matte Metal */
.bg-dark-metal {
  background: linear-gradient(
    145deg,
    #3a4b5f 0%,
    #2c3e50 100%
  );
}

/* Wood Surface */
.bg-wood {
  background: linear-gradient(
    180deg,
    #8b4513 0%,
    #654321 100%
  );
}

/* Leather Texture */
.bg-leather {
  background: linear-gradient(
    180deg,
    #4a3c31 0%,
    #2c2117 100%
  );
}
```

#### 1.3 3D Border Effects
Borders are not just simple strokes; they are key to expressing object thickness. By controlling the colors of the top, bottom, left, and right borders separately, you can simulate raised or recessed edges.

*   **Raised Object**: Top/Left borders are light (lit side), Bottom/Right borders are dark (shadow side).
*   **Recessed Object (e.g., Input)**: Top/Left borders are dark (internal shadow cast), Bottom/Right borders are light (bottom edge reflection).

```css
/* Raised Border Effect */
.border-raised {
  border-top: 1px solid rgba(255, 255, 255, 0.4);
  border-left: 1px solid rgba(255, 255, 255, 0.4);
  border-bottom: 1px solid rgba(0, 0, 0, 0.3);
  border-right: 1px solid rgba(0, 0, 0, 0.3);
}

/* Recessed Border Effect */
.border-recessed {
  border-top: 2px solid rgba(0, 0, 0, 0.4);
  border-left: 2px solid rgba(0, 0, 0, 0.4);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  border-right: 1px solid rgba(255, 255, 255, 0.1);
}
```

#### 1.4 Physical Feedback Interactions
Interaction is not just a change in color, but a change in physical position and state.

*   **Active State (Pressed)**: When a raised button is pressed, the shadow range should decrease (closer to the surface), the content shifts to the bottom-right (1px-2px), and an inner shadow may appear (becoming recessed).
*   **Hover State**: Brightness increases slightly, and shadows may diffuse slightly (object lifts up).

```css
/* Button Default State */
.skeuo-interactive {
  transform: translateY(0);
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
  transition: all 0.15s ease;
}

/* Hover State */
.skeuo-interactive:hover {
  filter: brightness(110%);
  box-shadow: 0 6px 12px rgba(0,0,0,0.35);
}

/* Button Click Physical Displacement */
.skeuo-interactive:active {
  transform: translateY(2px) translateX(1px);
  box-shadow:
    inset 2px 2px 5px rgba(0,0,0,0.3),
    inset -2px -2px 5px rgba(255,255,255,0.1);
  filter: brightness(90%);
}
```

#### 1.5 Text Texture Effects
Text should look like it is engraved into the material or like a metal plate attached to it.

*   **Letterpress (Engraved)**: Text color is darker than the background, with a light shadow below (simulating the highlight at the bottom of the groove) and a dark shadow above (simulating the shadow at the top of the groove).
*   **Embossed (Raised)**: Text color is lighter than the background, with a dark shadow below.

```css
/* Engraved Text Effect */
.text-engraved {
  color: rgba(0, 0, 0, 0.6);
  text-shadow:
    0px 1px 1px rgba(255, 255, 255, 0.3), /* Bottom Highlight */
    0px -1px 0px rgba(0, 0, 0, 0.5);      /* Top Inner Shadow */
}

/* Embossed Text Effect */
.text-embossed {
  color: rgba(255, 255, 255, 0.9);
  text-shadow:
    0 1px 0 rgba(255,255,255,0.8),
    0 2px 3px rgba(0,0,0,0.3);
}

/* Glowing Text Effect */
.text-glow {
  text-shadow:
    0 0 10px rgba(98, 110, 234, 0.8),
    0 0 20px rgba(98, 110, 234, 0.5);
}
```

#### 1.6 Material Texture Overlays
Surfaces that are too smooth look like plastic (unless it's glass). You need to overlay noise or textures to add realism.

*   **Noise**: Use an SVG or base64 noise image as a background mask.
*   **Leather/Fabric**: Use subtle tiling texture patterns.

```css
/* Noise Texture Overlay Class */
.texture-noise {
  position: relative;
}
.texture-noise::before {
  content: "";
  position: absolute;
  inset: 0;
  opacity: 0.05;
  background-image: url("data:image/svg+xml,..."); /* Noise SVG */
  pointer-events: none;
  mix-blend-mode: overlay;
}

/* Brushed Metal Texture */
.texture-brushed::after {
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    90deg,
    transparent,
    transparent 1px,
    rgba(255,255,255,0.02) 1px,
    rgba(255,255,255,0.02) 2px
  );
  pointer-events: none;
}
```

#### 1.7 Dynamic Lighting Effects
If possible, use simple CSS animations to simulate the slight movement of a light source or the shifting sheen on metal, adding a sense of "life".

```css
/* Simulating Metal Sheen Flow */
@keyframes sheen {
  0% { background-position: 0% 50%; }
  100% { background-position: 100% 50%; }
}
.metal-sheen:hover {
  background: linear-gradient(120deg, transparent 30%, rgba(255,255,255,0.4) 50%, transparent 70%);
  background-size: 200% 100%;
  animation: sheen 1s linear;
}

/* Glow Pulse Effect */
@keyframes glow-pulse {
  0%, 100% { box-shadow: 0 0 10px rgba(102,126,234,0.3); }
  50% { box-shadow: 0 0 20px rgba(102,126,234,0.6); }
}
.glow-pulse {
  animation: glow-pulse 2s ease-in-out infinite;
}
```

### 2. Complete Color Palette

Please register the following colors in your Tailwind configuration to ensure design consistency.

#### Material Bases
*   **Metal Base**: `#2c3e50` (Main), `#34495e` (Light), `#4a5568` (Ambient)
*   **Wood Base**: `#4a3c31` (Main), `#654321` (Light), `#8b4513` (Texture)
*   **Glass Base**: `#1e3a5f` (Main), `#2c5282` (Translucent)

#### Lighting & Shadows
*   **Highlight**:
    *   Strong Highlight: `#ffffff`
    *   Metal Highlight: `#c0c0c0`
    *   Soft Highlight: `rgba(255, 255, 255, 0.5)`
*   **Shadow**:
    *   Deep Shadow: `rgba(0, 0, 0, 0.5)`
    *   Ambient Shadow: `rgba(0, 0, 0, 0.3)`

#### Interaction Accents
*   **Indicator Blue**: `#667eea` (Normal), `#7f9cf5` (Glowing)
*   **Amber Gold**: `#f59e0b` (Warning/Highlight), `#fbbf24` (Plate Color)
*   **Alert Red**: `#e53e3e` (Switch/Error)

### 3. Key Component Implementations

Here are 5 core component implementation examples based on Tailwind CSS.

#### 3.1 Skeuomorphic Button (.skeuo-button)
*A metal-textured button with distinct thickness and click feedback.*

```html
<button class="
  relative overflow-hidden px-8 py-4 rounded-lg font-bold tracking-wider text-gray-200 uppercase
  /* Base Gradient Background */
  bg-gradient-to-b from-[#34495e] to-[#2c3e50]
  /* Border Highlights & Shadows */
  border-t border-l border-white/10 border-b border-r border-black/40
  /* Complex Drop Shadows */
  shadow-[6px_6px_12px_rgba(0,0,0,0.4),-4px_-4px_10px_rgba(255,255,255,0.05)]
  /* Interaction State: Hover */
  hover:brightness-110 hover:shadow-[8px_8px_16px_rgba(0,0,0,0.45),-6px_-6px_14px_rgba(255,255,255,0.08)]
  /* Interaction State: Active (Pressed) */
  active:translate-y-[2px] active:translate-x-[1px]
  active:shadow-[inset_4px_4px_8px_rgba(0,0,0,0.5),inset_-4px_-4px_8px_rgba(255,255,255,0.05)]
  active:border-t-black/30 active:border-b-white/10
  transition-all duration-150 ease-out
">
  <!-- Internal Text Engraving Effect -->
  <span class="drop-shadow-[0_1px_1px_rgba(0,0,0,0.8)] text-shadow-[0_-1px_0_rgba(0,0,0,1)]">
    Execute
  </span>
</button>
```

#### 3.2 Skeuomorphic Card (.skeuo-card)
*A content container simulating a physical panel placed on a desk, with soft edges and texture.*

```html
<div class="
  relative p-6 rounded-xl
  /* Dark Matte Metal Background */
  bg-[#2c3e50]
  /* Noise Texture Overlay (Assume texture-noise is configured) */
  texture-noise
  /* Mixed Border: Light top line, dark bottom line */
  ring-1 ring-white/5 ring-inset
  /* Deep Shadow */
  shadow-[10px_10px_20px_rgba(0,0,0,0.5),-8px_-8px_16px_rgba(255,255,255,0.03)]
">
  <!-- Recessed Title Bar at the top of the card -->
  <div class="
    -mx-2 -mt-2 mb-4 py-2 px-4 rounded bg-black/20
    border-b border-white/5 shadow-[inset_0_2px_4px_rgba(0,0,0,0.3)]
  ">
    <h3 class="text-gray-400 text-sm font-bold uppercase tracking-widest drop-shadow-md">
      System Control
    </h3>
  </div>
  <!-- Card Content -->
  <div class="text-gray-300">
    Content goes here...
  </div>
</div>
```

#### 3.3 Skeuomorphic Input (.skeuo-input)
*Simulating a recessed display screen or input area embedded within a panel.*

```html
<div class="relative group">
  <input type="text" placeholder="Enter command..." class="
    w-full px-5 py-3 rounded-lg outline-none
    /* Dark Recessed Background */
    bg-[#1a2634] text-gray-200
    /* Strong Inner Shadow Simulating Depth */
    shadow-[inset_4px_4px_10px_rgba(0,0,0,0.6),inset_-2px_-2px_6px_rgba(255,255,255,0.05)]
    /* Border Treatment: Bottom reflection, Top shadow */
    border-b border-white/10 border-t border-black/50 border-x border-black/30
    /* Placeholder Styling */
    placeholder-gray-600
    /* Focus State: Inner Glow */
    focus:shadow-[inset_2px_2px_5px_rgba(0,0,0,0.7),0_0_10px_rgba(102,126,234,0.3)]
    focus:text-blue-200
    transition-all duration-200
  " />
</div>
```

#### 3.4 Skeuomorphic Switch (.skeuo-switch)
*A realistic physical toggle switch with clear on/off states and mechanical feel.*

```html
<!-- Switch Base -->
<label class="
  relative inline-flex items-center cursor-pointer
  w-20 h-10 rounded-full
  /* Recessed Base Track */
  bg-[#1a2634]
  shadow-[inset_3px_3px_6px_rgba(0,0,0,0.6),inset_-1px_-1px_2px_rgba(255,255,255,0.05)]
  border border-black/20
">
  <input type="checkbox" class="sr-only peer">

  <!-- Toggle Thumb -->
  <div class="
    absolute left-1 top-1 w-8 h-8 rounded-full
    /* Thumb Material: Raised Metal/Plastic Sphere */
    bg-gradient-to-br from-[#4a5568] to-[#2d3748]
    /* Thumb 3D Feel */
    shadow-[2px_2px_5px_rgba(0,0,0,0.5),inset_2px_2px_4px_rgba(255,255,255,0.2)]
    border border-t-white/10 border-b-black/40
    /* State Transition */
    transition-all duration-300 ease-[cubic-bezier(0.68,-0.55,0.27,1.55)]
    /* Checked State Position & Style */
    peer-checked:translate-x-10
    peer-checked:bg-gradient-to-br peer-checked:from-[#667eea] peer-checked:to-[#5a67d8]
    peer-checked:shadow-[0_0_15px_rgba(102,126,234,0.6),2px_2px_5px_rgba(0,0,0,0.4)]
  ">
    <!-- Grip Texture Details on Thumb -->
    <div class="absolute inset-0 flex items-center justify-center gap-[2px] opacity-30">
        <div class="w-[1px] h-4 bg-black/50"></div>
        <div class="w-[1px] h-4 bg-black/50"></div>
        <div class="w-[1px] h-4 bg-black/50"></div>
    </div>
  </div>
</label>
```

#### 3.5 Skeuomorphic Panel (.skeuo-panel)
*A large-scale control panel with multi-level depth, featuring decorative screws.*

```html
<div class="
  relative rounded-2xl p-8
  /* Panel Main Material */
  bg-[#2c3e50]
  /* Edge Highlight Bevel */
  border-t-2 border-l border-white/10 border-b-4 border-r-2 border-black/50
  /* Massive Drop Shadow, making it float above background */
  shadow-[20px_20px_60px_rgba(0,0,0,0.6),-10px_-10px_30px_rgba(255,255,255,0.05)]
">
  <!-- Decorative Screws (Corners) -->
  <div class="absolute top-4 left-4 w-3 h-3 rounded-full bg-gray-400 shadow-[inset_1px_1px_2px_rgba(0,0,0,0.8),1px_1px_0_rgba(255,255,255,0.2)] flex items-center justify-center">
    <div class="w-full h-[1px] bg-gray-600 rotate-45"></div>
    <div class="w-full h-[1px] bg-gray-600 -rotate-45"></div>
  </div>
  <div class="absolute top-4 right-4 w-3 h-3 rounded-full bg-gray-400 shadow-[inset_1px_1px_2px_rgba(0,0,0,0.8),1px_1px_0_rgba(255,255,255,0.2)] flex items-center justify-center">
    <div class="w-full h-[1px] bg-gray-600 rotate-12"></div> <!-- Random Angle -->
    <div class="w-full h-[1px] bg-gray-600 -rotate-[78deg]"></div>
  </div>

  <!-- Panel Content Area -->
  <div class="h-full w-full bg-[#243342] rounded-lg shadow-[inset_2px_2px_8px_rgba(0,0,0,0.4)] border border-white/5 p-4">
    <!-- Content -->
  </div>
</div>
```

### 4. Tailwind CSS Configuration

Extend the following configuration in `tailwind.config.js` to support complex skeuomorphic effects.

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        skeuo: {
          dark: '#2c3e50',
          darker: '#1a2634',
          light: '#34495e',
          highlight: 'rgba(255, 255, 255, 0.1)',
          shadow: 'rgba(0, 0, 0, 0.4)',
          accent: '#667eea',
          gold: '#f59e0b',
        }
      },
      boxShadow: {
        'skeuo-raised': '6px 6px 12px 0px rgba(0, 0, 0, 0.3), -4px -4px 10px 0px rgba(255, 255, 255, 0.05)',
        'skeuo-recessed': 'inset 4px 4px 8px 0px rgba(0, 0, 0, 0.4), inset -3px -3px 6px 0px rgba(255, 255, 255, 0.05)',
        'skeuo-flat': '2px 2px 5px 0px rgba(0, 0, 0, 0.2), -1px -1px 2px 0px rgba(255, 255, 255, 0.05)',
      },
      backgroundImage: {
        'metal-brushed': "linear-gradient(135deg, #34495e 0%, #2c3e50 100%)",
        'noise': "url('/path/to/noise.png')", // Noise asset required
      }
    }
  }
}
```

### 5. Important Tips

1.  **Avoid Pure Black and White**: In Skeuomorphism, `#000` or `#fff` are rarely used as background colors. Use dark gray, dark blue, or beige as bases, reserving pure colors for extreme highlights only.
2.  **Lighting Consistency**: You must strictly adhere to the light source direction (usually top-left). If a button's shadow is on the bottom-right, all elements must cast shadows to the bottom-right, and recessed elements must have opposite inner shadows (top-left dark, bottom-right light).
3.  **Contrast Control**: Skeuomorphic interfaces can easily become visually cluttered due to the abundance of shadows and gradients. Ensure sufficient contrast between text and background, adding an outer glow or drop shadow to text if necessary to improve readability.
4.  **Rounded Corners**: The more distinct the border radius, the stronger the sense of physical solidity. Avoid sharp right angles, as they look like flat design.
5.  **Details Matter**: Adding subtle noise, scratch textures, screws, and seam lines can significantly enhance realism.
6.  **Physical Motion**: All transition animations should be linear or ease-out, simulating the inertia of objects in the physical world. Do not use instant changes.
7.  **Hierarchy**: Always think in terms of the Z-axis. The background is the foundation, the panel is the floor, the card is the table, and the button is the object on the table. The higher the level, the more diffused the shadow.
8.  **Whitespace**: Since skeuomorphic elements carry a heavy visual weight, they require more whitespace to breathe compared to flat design; otherwise, the interface will feel very cramped and oppressive.
