# ui-styles-skill

[简体中文](./README.md) | [English](./README.en.md)

> Offline UI style library for Claude Code — **79 design styles × bilingual prompts (zh-CN / en-US)**, packaged as a [Claude Code Skill](https://docs.claude.com/en/docs/claude-code/skills).
>
> 一个开箱即用的离线 UI 风格库 Skill，覆盖 79 个设计风格家族、中英双语 prompt，让 Claude 在生成前端 UI 时有"审美"。

<p align="center">
  <img src="./demo/demo-terminal.gif" alt="ui-styles-skill demo — Claude reads catalog, recommends styles, applies Swiss Design to a project" width="880">
</p>

<p align="center">
  <img alt="styles" src="https://img.shields.io/badge/styles-79-blueviolet">
  <img alt="languages" src="https://img.shields.io/badge/i18n-zh--CN%20%7C%20en--US-brightgreen">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-blue">
  <img alt="claude code" src="https://img.shields.io/badge/Claude%20Code-Skill-orange">
</p>

---

## ✨ 这是什么

`ui-styles-skill` 把上游开源项目 [TonnyWong1052/UI-Prompt](https://github.com/TonnyWong1052/UI-Prompt) 的 79 个 UI 风格 prompt 离线封装为一个 Claude Code Skill。装上之后，你可以这样和 Claude 对话：

- 「我在做一个开发者工具站点，推荐 3 个合适的 UI 风格」
- 「用 claymorphism 风格帮我生成一个登录页」
- 「synthwave 和 vaporwave 有什么区别？」
- 「换个更复古的风格试试」

Claude 会读取本地 catalog、筛选候选、按需加载对应风格的 prompt，最后用该风格的视觉规范生成代码 —— 全程零网络请求、零 token 消耗在浏览风格库上。

## 📦 安装

### 全局安装（推荐）

```bash
git clone https://github.com/chrzamz/ui-styles-skill.git ~/.claude/skills/ui-styles
```

### 项目级安装

```bash
git clone https://github.com/chrzamz/ui-styles-skill.git .claude/skills/ui-styles
```

安装后在任意 Claude Code 会话里输入：

```
/ui-styles 推荐适合 SaaS 后台的风格
```

或直接用自然语言触发（Skill 描述里已声明触发词）：

> 「我要给开发者工具选个 UI 风格」

## 🎨 风格目录概览

| Category | 数量 | 代表风格 |
|---|---:|---|
| `core` | 9 | flatDesign · minimalism · brutalism · memphis · skeuomorphism · materialDesign · fluent2 |
| `visual` | 53 | claymorphism · glassmorphism · neoBrutalism · vaporwave · y2k · bentoGrids · auroraGlass · holographicFoil · sciFiHud · wabiSabi · biophilic · blueprint · popArt … |
| `retro` | 15 | synthwave · arcadeCRT · artDeco · bauhaus · darkAcademia · filmNoir · midCenturyModern · newspaper · retroOS · steampunk · swissDesign · vhsAesthetic |
| `layout` | 1 | magazine |
| `interaction` | 1 | mouseTracking |

> 共 **79 个 family**；其中 9 个仅提供 `style.md`（用于让模型理解风格），无可直接生成代码的 `custom.md`。

## 🚀 使用示例

### 1. 让 Claude 推荐风格

> **You:** 我在做一个 AI 编程助手的官网，能不能推荐 3 个 UI 风格？
>
> **Claude:** *(读取 catalog → 按 tags 匹配 dev-tool / minimal / tech 调性)*
> 1. **Minimalism** — 极简留白，让产品本身成为视觉焦点
> 2. **Blueprint** — 工程蓝图美学，技术感强、辨识度高
> 3. **Bento Grids** — 苹果发布会同款，适合展示多个功能模块

### 2. 让 Claude 按风格生成代码

> **You:** 用 Claymorphism 风格给我做一个 Pricing 页面
>
> **Claude:** *(读取 `prompts/visual/claymorphism/custom.md` → 注入到系统指令 → 输出符合风格规范的 HTML/CSS/React)*

### 3. 浏览/对比

> **You:** synthwave 和 vaporwave 有啥区别？
>
> **Claude:** *(分别读取两个风格的 `style.md` 段落对比)*

## 📂 项目结构

```
ui-styles-skill/
├── SKILL.md              # Claude Code Skill 入口（含触发词、工作流程）
├── catalog.json          # 全部 79 个风格的轻量索引（id / 分类 / tags / prompt 路径）
└── prompts/
    ├── core/
    │   └── <familyId>/
    │       ├── style.md  # 风格定义：视觉理念、材质、交互、氛围（"是什么"）
    │       └── custom.md # 可直接喂给模型的生成式 prompt（"按这个生成代码"）
    ├── visual/
    ├── retro/
    ├── layout/
    └── interaction/
```

每个风格的 `style.md` / `custom.md` 都包含 **zh-CN** 和 **en-US** 两段；Claude 会根据项目语境自动选择。

## 🧭 风格选择启发式

| 场景 | 推荐方向 |
|---|---|
| B 端工具 / SaaS / 数据看板 | minimalism · flatDesign · fluent2 · bentoGrids · swissDesign |
| 开发者工具 / 技术博客 | minimalism · monochrome · blueprint · retroOS · vhsAesthetic |
| 创意作品集 / 设计师官网 | brutalism · neoBrutalism · memphis · claymorphism · holographicFoil · antiDesign |
| 营销落地页 / 品牌站 | gradients · glassmorphism · 3dElements · auroraGlass · bentoGrids |
| 游戏 / 娱乐 / 音乐 | synthwave · vaporwave · neonCyberpunk · retroFuturism · y2k · sciFiHud |
| 复古 / 怀旧 / 文艺 | midCenturyModern · swissDesign · newspaper · artDeco · darkAcademia · wabiSabi |
| 自然 / 健康 / 生活方式 | biophilic · organic · natural · scandi · wabiSabi · solarpunk |
| 儿童 / 教育 / 萌系 | kawaiiMinimal · claymorphism · paperCutout · handDrawnSketch · comicBook |

## 🤝 贡献

欢迎以下几类 PR：

- **新增风格** — 提供 `style.md` + `custom.md`（双语），并在 `catalog.json` 注册
- **润色现有 prompt** — 让风格描述更准确、更易被模型理解
- **补充 9 个缺失的 `custom.md`** — 见 catalog 中 `prompts.custom = null` 的 family
- **新增触发场景到 SKILL.md** — 让 Claude 更聪明地匹配
- **i18n** — 当前是 zh-CN / en-US，欢迎补 ja / ko 等

贡献前请先开 issue 对齐方向。提交时请保持 catalog.json 与目录结构同步。

## 📜 上游来源与致谢

本项目的 79 个风格 prompt 全部来自上游开源项目 **[TonnyWong1052/UI-Prompt](https://github.com/TonnyWong1052/UI-Prompt)** —— 那里有完整的设计文档、在线浏览界面和持续更新的 prompt 源文件。本仓库的工作是：

1. 将上游 prompt 整理为符合 Claude Code Skill 规范的目录结构
2. 编写 catalog.json 索引，让模型可低成本筛选
3. 撰写 SKILL.md 工作流程，约束模型的触发与输出行为

详见 [ATTRIBUTION.md](./ATTRIBUTION.md)。如果你觉得这个项目有用，**请同时给上游仓库点 star**。

## 📄 License

[MIT](./LICENSE) © 2026 chrzamz

上游 prompt 内容版权归原作者所有，遵循上游项目协议。
