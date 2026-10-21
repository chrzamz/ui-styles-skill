# 项目 tokens 到组件库主题

视觉规范负责设计意图、布局、组件状态和可接受的变化；`tokens.json` 保存可确定的值，库主题文件实现这些值。沿用项目已有文件和命名，不再造另一份相互冲突的事实源。下面的最小格式是本 skill 的交换约定，不是 DTCG 标准，也不是完整设计系统。

## 最小输入格式（schemaVersion 1）

`tokens.json` 必须显式提供：

- `schemaVersion: 1`、非空 `name`。
- `modes.light`，可选完整 `modes.dark`。每个模式含 `background`、`surface`、`text`、`mutedText`、`border`、`primary`、`onPrimary`、`success`、`warning`、`danger`、`focus`。
- `typography: { fontFamily, fontSize, lineHeight }`，字号单位 px，行高是无单位倍数。
- `shape: { borderRadius }`（px）、`spacing: { unit }`（px）、`control: { height }`（px）。
- `motion: { duration, reducedMotion }`，时长 ms，布尔值表示是否响应系统减少动态效果偏好。

这些值应来自用户、已有规范或经过说明的设计提案。没有隐式色板；不要将示例当作所有项目的默认审美。只做浅色的产品不必强行补暗色。schema v1 拒绝未知键，完整状态规则保存在视觉规范/组件实现里。

CSS/Semi 导出接受 hex、安全的简单数字颜色函数和 `var(--name)`；复杂表达式应先解析成值。Ant Design/MUI 导出要求不透明 `#RGB`/`#RRGGBB`，避免将尚未解析的 CSS 变量或不兼容颜色空间交给库的运行时颜色算法。高级色彩/多色阶需求由 Agent 依据实际版本直接适配，不强行塞进这个小工具。

## 可执行导出

Python 3，无第三方依赖：

```sh
python3 <skill-root>/scripts/export_theme.py design/tokens.json --library css --output design/theme.css
python3 <skill-root>/scripts/export_theme.py design/tokens.json --library antd --output src/theme.ts
python3 <skill-root>/scripts/export_theme.py design/tokens.json --library mui --output src/theme.ts
python3 <skill-root>/scripts/export_theme.py design/tokens.json --library semi --output src/theme.css
```

只执行选中的一种。`--output` 只创建新文件，不覆盖文件或符号链接；父目录须已存在。省略时输出到 stdout。已有主题用正常编辑流程按差异合入，不用 shell 重定向覆盖。脚本不安装库、不改 provider，也不发布主题。

每次导出都向 stderr 报告尚待检查的范围。生成成功只证明完成了映射；必须把主题接入用户项目并检查真实页面。

## 映射与接入

| 导出器 | 输出与入口 | 覆盖范围与边界 |
|---|---|---|
| `css` | `--ui-*` 变量；暗色设在根元素 `data-ui-mode="dark"` | 保存全部基础值；现有组件需要实际引用变量。减少动态效果只改变时长变量，不能自动修改不使用它的动画 |
| `antd` | `getUiTheme(mode, prefersReducedMotion)` 返回 `ThemeConfig`，传给 `<ConfigProvider theme={...}>` | 品牌/语义色、背景、文字、边框、字体、字号、行高、圆角、尺寸单位、控件高度和中速动效；使用浅/暗算法生成派生状态，同时保留明确给定的主色/成功/警告/错误色，派生状态仍需检查 |
| `mui` | `createUiTheme(mode, prefersReducedMotion)`，传给 `<ThemeProvider theme={...}>` | palette、typography、shape、spacing、标准动效；Button/InputBase 最小高度，ButtonBase 键盘焦点。其余 slots、密度、CSS 动画和 ripple 另核实 |
| `semi` | 在库 CSS 后加载语义变量覆盖；暗色由 `body[theme-mode="dark"]` 控制 | **部分适配**：背景/文字/品牌/状态基础色、边框、焦点边框、小圆角。其余输入保留为 `--ui-*`，不代表 Semi 已消费 |

Ant Design 的静态 `message`/`Modal` 等调用可能不在 ConfigProvider 上下文内；按项目版本使用相应 hook 或 App 上下文。MUI 的 `CssBaseline` 按项目约定使用，不擅自替换全局 reset。两种 JS 导出器接收系统减少动态效果偏好作为参数，调用方用现有 SSR 安全方式读取；不要在模块顶层访问 `window`。缓存生成的主题，避免每次 render 重建。

**Semi 不能只覆盖一个 primary 就声称整套状态已适配。** 它的 hover、active、disabled、light 背景有各自变量，可能仍保留原色。按视觉规范补齐相关色阶，或使用 DSM/本地 SCSS 及官方构建插件配置。不要给 `--semi-blue-5` 一类 RGB 通道变量直接塞 hex；本脚本只覆盖完整 CSS 颜色的语义变量。`onPrimary` 没有被粗暴映射成全局 white，须按 Button 等具体组件处理。字体、尺寸、间距与动效也应通过实际 SCSS/组件接口实现。

## 状态与运行验收

选择一个主按钮、一个含错误提示的表单、一个数据/内容列表和一个弹窗，检查 default、hover、active、focus-visible、disabled、loading、selected、error、empty。检查文字/背景、焦点与状态对比，长中文、窄屏、弹出层主题归属及减少动态效果。暗色只有在提供和接入了暗色 tokens 时才测试并宣称支持。

状态允许沿用库的正确实现，但视觉上必须与项目规范一致。不能把“设置了 theme 对象”“CSS 文件生成了”当成验收通过。若版本 API 不匹配，修改适配层而不是要求用户升级整个项目。

## 核验依据与兼容性

2026-10-21 核对了当前官方文档与源文件：

- Ant Design 文档显示 **6.6.7**；采用自 5.x 引入的 ConfigProvider/token API，4.x Less 主题不兼容。参考：[主题与 Token API](https://ant.design/docs/react/customize-theme/)、[ThemeConfig 源码](https://github.com/ant-design/ant-design/blob/master/components/config-provider/context.ts)。
- MUI 当前文档显示 **9.5.0**；使用 `@mui/material/styles` 的 `createTheme` 基础 API，不假设项目已采用新版 CSS variables/colorSchemes。参考：[Theming](https://mui.com/material-ui/customization/theming/)、[Palette](https://mui.com/material-ui/customization/palette/)、[组件覆盖](https://mui.com/material-ui/customization/theme-components/)。
- Semi 使用 **2.x** 文档的语义 CSS 变量与暗色入口。参考：[定制主题](https://semi.design/zh-CN/advanced/customize-theme)、[暗色模式](https://semi.design/zh-CN/advanced/dark-mode)、[全局变量源码](https://github.com/DouyinFE/semi-design/blob/main/packages/semi-theme-default/scss/global.scss)。

同日完成临时项目集成验证：`antd 6.6.7`、`@mui/material 9.5.0`、`@douyinfe/semi-ui 2.104.0`、`react/react-dom 19.3.1`、`typescript 7.0.2`、`@emotion/react 11.14.0`、`@emotion/styled 11.14.1`，安装使用 `--ignore-scripts`。Ant/MUI 生成模块和 provider 接入通过严格类型检查（`skipLibCheck: true` 仅跳过上游声明内部检查），主题函数、明暗语义色、尺寸、减少动效及 provider 服务端渲染通过运行验证。Semi 导出的 11 个变量名均在安装包 CSS 中找到定义。过程中修正了 Ant 暗色算法二次变暗明确色值、以及中速时长覆盖减少动效结果的问题。

这不是浏览器视觉、交互或无障碍验收，也不代表所有历史版本均兼容。用户项目仍需按实际安装版本验证。其他库由 Agent 查该版本官方 API 后生成配置，不存在虚构的通用 token API。

基础测试无需 npm。需要复跑真实依赖回归时，先在临时目录安装上述依赖，再运行：

```sh
UI_STYLES_THEME_CHECK_NODE_MODULES=/absolute/temp/node_modules python3 -B -m unittest discover -s tests -p test_export_theme.py -v
```

测试会在另一个临时目录生成、编译和运行主题及 provider，不修改依赖目录或实际项目。未提供该变量时只跳过真实库回归，仍运行其余基础测试。
