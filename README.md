# ui-styles-skill

[简体中文](./README.md) | [English](./README.en.md)

一个参与产品制作的设计师 Skill：理解项目、推荐视觉方向和组件库、做预览、保存项目视觉规范，并在后续页面与交互状态中保持一致。面向独立开发者，以及没有设计或开发背景、通过 Agent 制作产品的人。

内置 **79 条中英双语风格记录**，支持自定义风格、项目视觉规范和组件库主题适配。风格资料离线可用；库的版本核验、在线参考和安装依赖按实际任务使用网络。

> 原有终端演示展示的是早期“推荐风格 → 应用 prompt”流程；新增工作流及工具以本文和 SKILL.md 为准。
>
> ![原有推荐演示](./demo/demo-terminal.gif)

## 它如何参与制作

你可以直接说：

- “帮我做一个订单管理后台，适合业务员用，表格和表单比较多。”
- “做一个动漫收藏网站，我不懂设计，你帮我推荐并做出效果。”
- “给这个产品做个 demo，先沿用现有品牌和组件。”
- “用现有 Semi Design 实现这套视觉，补齐加载、错误和禁用状态。”
- “把我选定的风格存成个人配方，以后其他项目也能选用。”
- “继续做设置页，保持和前面一致。”

Skill 在第一个带样式的页面、demo 或组件库选择之前参与。它先读取已有项目，给出有理由的推荐；需要比较时展示少量候选。用户要求直接制作时先做代表性页面，避免反复问设计术语。

选库依据任务、技术栈、组件覆盖和定制成本。后台可比较 Ant Design、Semi、MUI、Arco 等；内容/营销页可以使用更轻的组件；动漫产品的艺术方向与基础交互库分别决定。保留合适的现有库，优先复用成熟能力。没有固定默认配色，也不默认安装 shadcn/ui 或禁止它。

## 跨 Agent 的项目视觉标准

默认成果可以是：

```text
design/visual-system.md   # 受众、方向、组件库、布局、状态与验证记录
design/tokens.json        # 需要结构化复用时才创建
src/.../theme.*          # 按实际项目生成/适配的主题实现
AGENTS.md                # 指向视觉标准的简短入口
CLAUDE.md                # 需要时导入共享入口
```

已有 `DESIGN.md` 或主题文件时继续使用，避免两套规范。Markdown 保存意图和行为，tokens/现有主题保存权威数值；后续页面读取同一份约定。规范包括适用的 hover、focus、disabled、loading、error、empty、selected 等状态，而不仅是主色和圆角。

这套文件可随项目被不同 Agent 读取，无需依赖 Claude Design。**自动发现不是强制执行**：skill 描述帮助首轮触发，项目规则负责后续持续介入，实际页面检查证明执行效果。宿主配置仍可能限制加载。

详见 [项目规范](references/project-standard.md)、[跨 Agent 接入](references/agent-integration.md)、[预览与验收](references/visual-review.md)。

## 安装

保留原有 Claude Code 安装方式；Codex 使用当前官方文档列出的 `.agents/skills`。选择需要的宿主和范围，不要覆盖已有安装。

```sh
# Claude Code，用户级
git clone https://github.com/chrzamz/ui-styles-skill.git ~/.claude/skills/ui-styles

# Codex，用户级
git clone https://github.com/chrzamz/ui-styles-skill.git ~/.agents/skills/ui-styles
```

项目级分别放在项目的 `.claude/skills/ui-styles` 或 `.agents/skills/ui-styles`。其他支持 Agent Skills 的工具按其发现路径安装。

可以明确调用 Claude Code 的 `/ui-styles` 或 Codex 的 `$ui-styles`。自然语言也能触发，但是否自动调用由宿主和模型决定。希望从每个项目第一步都参与时，按[接入说明](references/agent-integration.md)设置条件式项目/用户规则；安装不会偷偷修改全局配置。

已有视觉规范后，可让 Agent 使用项目接入工具。默认仅预览，加 `--write` 才写入：

```sh
python3 <skill-root>/scripts/link_project.py --project /path/to/product --design design/visual-system.md --claude
```

## 自定义风格：ui-style-creator

主 Skill 能直接读取内置的 [ui-style-creator](skills/ui-style-creator/SKILL.md)。它把用户想法、现有项目或参考图整理成可复用的风格配方。

- **项目级**：`<project>/.ui-styles/profiles/<name>/`
- **用户级**：`${XDG_CONFIG_HOME:-~/.config}/ui-styles/profiles/<name>/`
- 内容包括视觉规范、元数据和可选 tokens；保存已确定的内容，不自动套默认色板。
- 用户级配方只在被项目选用时生效；项目保留本地副本，更新配方不会悄悄修改旧项目。

需要独立命令时，将整个 `skills/ui-style-creator/` 文件夹安装到宿主的技能目录。不要假定嵌套文件夹会自动注册第二个命令。

## 组件库主题导出

附带 Python 3.9+ 标准库工具，支持 CSS、Ant Design、MUI、Semi 的**基础主题映射**。使用项目确认的值，先查实际库版本，再接入并验证。其他库由 Agent 按对应版本的官方 API 适配。

```sh
python3 <skill-root>/scripts/export_theme.py design/tokens.json --library antd --output src/theme.ts
```

只创建新文件，不覆盖已有主题。Semi 输出语义 CSS 变量；其状态色阶等仍需补齐。Ant/MUI 的派生状态也需在真实组件中检查。导出成功不等于全状态或无障碍验收通过。参见 [格式、映射和限制](references/theme-adapters.md)。

## 仓库内容

| 路径 | 用途 |
|---|---|
| `SKILL.md` | 主设计工作流与触发边界 |
| `catalog.json`、`prompts/` | 79 条风格资料，70 份 custom prompt |
| `references/` | 项目规范、Agent 接入、选库、适配与视觉检查 |
| `assets/visual-system.template.md` | 项目视觉规范模板 |
| `examples/` | token 示例，用于说明和测试，不是默认主题 |
| `skills/ui-style-creator/` | 可独立使用的自定义风格技能 |
| `scripts/` | 项目规则接入与基础主题导出 |
| `tests/`、`evals/` | 工具行为测试与真实任务评估场景 |

资料存在重复/近似风格和不完整 tags，79 表示记录数；推荐时结合描述与实际内容。没有 custom 的风格仍可由 Agent 提炼后实现。演示页布局作为参考，实际页面结构由产品任务决定。

## 开发与验证

```sh
python3 -B -m unittest discover -s tests -v
```

脚本测试验证文件边界和 token 映射；技能行为用 [评估场景](evals/scenarios.md)检查。[2026-10-21 验证记录](evals/results-2026-10-21.json)包含实际库集成与一次独立页面制作测试。真实宿主自动触发、其他库版本和用户视觉接受度仍需独立验证。

欢迎围绕真实使用失败改进工作流、状态覆盖、适配器和案例，帮助更多使用者完成产品的设计与制作。

## 协议

[MIT](./LICENSE) © 2026 chrzamz。
