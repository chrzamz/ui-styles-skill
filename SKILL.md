---
name: ui-styles
description: 离线 UI 风格库（79 个风格家族，中英双语 prompt）。当用户需要为项目选定视觉风格、生成 UI 设计 prompt、或询问某个具体设计风格（如 claymorphism / glassmorphism / neoBrutalism / vaporwave / synthwave / bento grids / minimalism 等）时使用。触发词：「UI 风格」「设计风格推荐」「UI prompt」「视觉风格」「换个风格」「这个项目用什么风格」。
---

# UI Styles Skill

离线封装自 https://github.com/TonnyWong1052/UI-Prompt 的 UI 风格 prompt 库，覆盖 5 大分类 79 个风格家族，中英双语。

## 数据结构

- `catalog.json` — 全部风格的轻量索引（id / 分类 / 名称 / 描述 / 标签 / prompt 路径）
- `prompts/<category>/<familyId>/`
  - `style.md` — 风格定义：视觉理念、材质质感、交互体验、整体氛围（适合让 AI 理解一个风格"是什么"）
  - `custom.md` — 可直接使用的生成式 prompt 模板（适合让 AI "按这个风格生成代码"）
- 5 个分类：`core`（核心设计系统）、`visual`（视觉效果）、`retro`（复古/年代）、`layout`（版式）、`interaction`（交互）

## 工作流程

### 触发方式

1. **推荐风格**：用户描述项目（"我在做一个 SaaS 后台"/"游戏官网"/"开发者工具"），让你挑风格
2. **直接命名**：用户点名一个风格（"用 claymorphism"/"给我 vaporwave"），让你产出 prompt
3. **对比/浏览**：用户问"有哪些风格"或"和 X 风格类似的有哪些"

### 执行步骤

**步骤 1 — 读 catalog**
```
Read <skill-root>/catalog.json
```
`<skill-root>` 是本 skill 的安装目录（通常 `~/.claude/skills/ui-styles/` 或项目内 `.claude/skills/ui-styles/`）。取出所有 family 的 `id / name / description / tags / category`，作为筛选基础。

**步骤 2 — 筛选 / 匹配**
- 若用户给项目上下文：根据项目调性（B 端工具 / C 端娱乐 / 数据展示 / 营销页 / 游戏 / 复古怀旧 / 极简专业 …）匹配 `tags` 和 `description`，输出 Top 3-5 候选，每个附一句话推荐理由
- 若用户点名风格：直接定位对应的 family（注意中英文名都可能匹配）
- 若用户要浏览：按 category 分组列出，避免一次倾倒太多

**步骤 3 — 加载详细 prompt（按需）**
- 用户确认要某个风格后，按 `catalog.json` 中 `prompts.custom` 或 `prompts.style` 路径读取 md 文件
- `custom.md` 优先用于"帮我生成 UI"场景
- `style.md` 优先用于"解释这个风格"或"提供给设计师参考"场景
- 默认输出中文（zh-CN 段落），若项目是英文项目或用户明确要英文则用 en-US

**步骤 4 — 输出**
- 把对应语言段落整段呈现给用户，可附简短说明
- 如果用户接下来要直接生成 UI 代码，用 prompt 作为系统指令，结合项目实际页面需求生成

## 风格分类速览

| Category | 数量 | 代表风格 |
|---|---|---|
| `core` | 9 | flatDesign / minimalism / brutalism / memphis / scrollNarrative / skeuomorphism / typography / fluent2 / materialDesign |
| `visual` | 50+ | claymorphism / glassmorphism / neoBrutalism / synthwave / vaporwave / y2k / gradients / 3dElements / bentoGrids / kawaiiMinimal / wabiSabi / industrial / biophilic / blueprint / popArt / sciFiHud … |
| `retro` | 15 | arcadeCRT / artDeco / bauhaus / darkAcademia / filmNoir / frutigerAero / midCenturyModern / newspaper / retroFuturism / retroOS / steampunk / swissDesign / synthwave / vhsAesthetic / digitalRetro |
| `layout` | 1 | magazine |
| `interaction` | 1 | mouseTracking |

## 推荐启发式

- **B 端工具 / SaaS / 数据看板** → minimalism, flatDesign, fluent2, bentoGrids, swissDesign, utilityFirst
- **开发者工具 / 技术博客** → minimalism, monochrome, blueprint, terminal-like (retroOS / vhsAesthetic)
- **创意作品集 / 设计师官网** → brutalism, neoBrutalism, memphis, claymorphism, holographicFoil, antiDesign
- **营销落地页 / 品牌站** → gradients, glassmorphism, 3dElements, auroraGlass, bentoGrids
- **游戏 / 娱乐 / 音乐** → synthwave, vaporwave, neonCyberpunk, retroFuturism, y2k, sciFiHud
- **复古 / 怀旧 / 文艺** → midCenturyModern, swissDesign, newspaper, artDeco, darkAcademia, wabiSabi, inkWash
- **自然 / 健康 / 生活方式** → biophilic, organic, natural, scandi, wabiSabi, solarpunk
- **儿童 / 教育 / 萌系** → kawaiiMinimal, claymorphism, paperCutout, handDrawnSketch, comicBook

## 注意事项

- catalog 和 prompt 内容都是从上游仓库 (TonnyWong1052/UI-Prompt) 镜像而来，是该项目的设计成果，引用时建议保留来源链接
- 79 个 family 中，9 个只有 `style.md` 没有 `custom.md`（catalog 中 `prompts.custom` 为 null），这些只能解释风格、不能直接生成代码
- 不要在响应中倾倒整个 catalog；先筛选、再按需读 prompt
- 如果用户问的风格不在 catalog 里，直接说不在并给出最接近的候选，不要编造
