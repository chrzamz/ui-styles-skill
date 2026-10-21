# 组件库选型：先看产品需要什么

在新建页面、demo、产品原型或重做视觉时使用。已有项目先读依赖、组件封装、设计规范及可用的库专用 skill；不要因为模型熟悉某个库，就为它改技术栈。

## 用一个真实页面决定

提取用户的主要任务、内容密度、终端、技术栈、品牌要求和已有资产。例如后台是否需要树形权限、复杂表单、可编辑表格、日期区间和上传；内容站是否主要是文字、图片、搜索与订阅。用户不必会说设计术语。

优先沿用能满足需求的现有库。新项目给一个首选和最多两个备选，说明组件覆盖、视觉可塑性、无障碍/键盘行为、依赖与维护成本。用代表性页面检验关键能力，再决定是否引入；不要因为一个普通按钮同时安装多个完整组件库。

以下是起点，不是固定的行业配对，也不是下载量排行榜：

| 场景/约束 | 可考察的方向 | 必须核实的差异 |
|---|---|---|
| React 管理后台、复杂表单和数据操作 | Ant Design、Semi Design、Arco Design | 项目需要的表格、树、表单联动、国际化、密度与主题扩展是否覆盖；商业/高级组件是否另有条件 |
| React 通用产品、愿意采用 Material 语言 | MUI | Material 交互是否符合产品；MUI X 的具体功能、许可证和付费边界另查 |
| React 应用，需要较完整组件且强调可调主题 | Mantine、Chakra UI | 所需组件、框架/SSR 兼容、主题 API 的安装版本；不要把另一大版本示例混入项目 |
| 强品牌内容站、营销页、特殊视觉表达 | 现有轻量组件、原生 HTML/CSS，按需补 Radix 或 React Aria | 基础交互可复用，但信息结构、排版和品牌表达仍需设计；无样式不等于没有实现成本 |
| 希望组件代码归项目持有 | shadcn/ui 或已有本地组件 | 接受后续维护责任；检查 registry 与底层依赖；默认主题不是产品品牌 |
| Vue 管理产品 | Element Plus、Naive UI、Arco Design Vue | 以 Vue 版本及实际能力选择；不要为了 React 库迁移现有 Vue 项目 |
| 动漫、二次元、游戏社区 | 先按内容浏览/社区/交易/游戏交互选基础，再定角色、插画、字体、色板与动效 | 没有通用“二次元组件库”承诺。主题皮肤不能替代登录、弹窗、表单和键盘行为；核实素材授权 |

高辨识度页面仍可使用成熟组件。先用 token、组件主题接口、组合与少量外观扩展满足要求；只有某个必要交互或外观确实达不到时，才定制该部分，并保留键盘、焦点、ARIA 和状态行为。

## 推荐的交付格式

用用户能理解的语言说明：推荐什么、为什么适合当前任务、有什么代价、会复用哪些现成能力、需要自己做哪一小部分。记录框架及库的实际版本、选型理由、主题入口和状态验收范围。用户已选库时直接适配，除非发现具体不兼容问题。

“下载量高”只能是维护生态的一个线索。用户要求排名时，按当前 npm 包名、同一统计窗口查询，标注日期与数据源；不要把不同包拆分策略、历史安装量或 GitHub star 混为下载排名。不为一个推荐任务永久维护排行榜。

## 官方入口

选定候选后按安装版本查官方文档；这些入口用于核验，不要求每次把全部文档加载到上下文。

- [Ant Design](https://ant.design/docs/react/introduce/)、[Semi Design](https://semi.design/zh-CN/start/introduction)、[Arco React](https://arco.design/react/docs/start)
- [MUI](https://mui.com/material-ui/getting-started/)、[Mantine](https://mantine.dev/getting-started/)、[Chakra UI](https://chakra-ui.com/docs/get-started/installation)
- [Radix Primitives](https://www.radix-ui.com/primitives/docs/overview/introduction)、[React Aria](https://react-spectrum.adobe.com/react-aria/)、[shadcn/ui](https://ui.shadcn.com/docs)
- [Element Plus](https://element-plus.org/en-US/guide/design.html)、[Naive UI](https://www.naiveui.com/)、[Arco Vue](https://arco.design/vue/docs/start)

要生成主题，继续读 [theme-adapters.md](theme-adapters.md)。
