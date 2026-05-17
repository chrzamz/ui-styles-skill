# demo.tape — terminal portion of ui-styles-skill demo gif
#
# Re-enacts a real session (metal-powder-site, 2026-05-16):
#   user asks Claude to pick a UI style for a B2B metal-powder site
#   Claude reads catalog.json, recommends 3 candidates, user picks Swiss Design,
#   Claude reads prompts/retro/swissDesign/custom.md, then rewrites the page.
#
# Run:   vhs demo/demo.tape          (outputs demo/demo-terminal.gif)
# Deps:  brew install vhs

Output demo/demo-terminal.gif

# ── canvas ───────────────────────────────────────────────
Set FontSize 18
Set Width  1280
Set Height 760
Set Padding 24
Set TypingSpeed 35ms
Set Theme "Catppuccin Mocha"
Set Shell "zsh"

# ── 0. project cwd  ──────────────────────────────────────
Hide
Type "cd ~/Workspace/Projects/metal-powder-site && clear"
Enter
Sleep 400ms
Show

# ── 1. launch Claude Code  ───────────────────────────────
Type "claude"
Sleep 400ms
Enter
Sleep 1.2s

# fake the Claude Code banner so we don't need the real CLI
Hide
Type "clear && printf '\\033[38;5;208m ██████ ██       █████  ██    ██ ██████  ███████\\n██      ██      ██   ██ ██    ██ ██   ██ ██\\n██      ██      ███████ ██    ██ ██   ██ █████\\n██      ██      ██   ██ ██    ██ ██   ██ ██\\n ██████ ███████ ██   ██  ██████  ██████  ███████\\033[0m\\n\\n   Claude Code · ui-styles skill loaded · 79 styles\\n\\n'"
Enter
Sleep 200ms
Show
Sleep 1s

# ── 2. user prompt #1 ────────────────────────────────────
Type@40ms "> 网站类型你帮我选择一个合适的设计风格"
Sleep 400ms
Enter
Sleep 1s

# ── 3. simulated Claude turn #1 ──────────────────────────
Hide
Type "printf '\\033[38;5;245m● Read(~/.claude/skills/ui-styles/SKILL.md)\\033[0m\\n  \\033[2m└ 4.9 KB · catalog index 79 families\\033[0m\\n\\n'"
Enter
Sleep 600ms
Type "printf '\\033[38;5;245m● Read(~/.claude/skills/ui-styles/catalog.json)\\033[0m\\n  \\033[2m└ 116 KB · core(9) visual(53) retro(15) layout(1) interaction(1)\\033[0m\\n\\n'"
Enter
Sleep 900ms
Show
Sleep 200ms

Type@5ms "● 三个方向，按契合度排序（B2B 不锈钢粉末，PM/MIM/滤芯客户）："
Enter
Sleep 300ms
Type@5ms ""
Enter
Type@5ms "  1. Industrial Editorial Minimalism  ★ 推荐"
Enter
Type@5ms "     黑白灰 + 金属冷色 · 大字号无衬线 · Bento 规格表"
Enter
Sleep 250ms
Type@5ms "  2. Swiss Design                     ★ 推荐"
Enter
Type@5ms "     国际主义网格 · Helvetica/Akzidenz · 信息即设计"
Enter
Sleep 250ms
Type@5ms "  3. Material / Texture-Forward"
Enter
Type@5ms "     SEM 微观照为视觉锚 · 图主文辅"
Enter
Sleep 1.4s

# ── 4. user prompt #2 ────────────────────────────────────
Type@40ms "> 选择 swiss design 这个方案如何？"
Sleep 400ms
Enter
Sleep 900ms

# ── 5. simulated Claude turn #2 ──────────────────────────
Hide
Type "printf '\\033[38;5;245m● Read(prompts/retro/swissDesign/style.md)\\033[0m\\n  \\033[2m└ visual philosophy · typography · grid · color\\033[0m\\n\\n'"
Enter
Sleep 600ms
Type "printf '\\033[38;5;245m● Read(prompts/retro/swissDesign/custom.md)\\033[0m\\n  \\033[2m└ ready-to-use generation prompt (zh-CN + en-US)\\033[0m\\n\\n'"
Enter
Sleep 900ms
Show

Type@5ms "● 评估：非常合适 ★★★★★"
Enter
Sleep 250ms
Type@5ms ""
Enter
Type@5ms "  · 理性、客观、精确 — 让参数说话，契合工程师采购心智"
Enter
Sleep 200ms
Type@5ms "  · 网格系统天然适合粒度表 / 化学成分 / 应用矩阵"
Enter
Sleep 200ms
Type@5ms "  · Helvetica + 大量留白 — 国际客户=严肃工业供应商"
Enter
Sleep 200ms
Type@5ms "  · 国际同行参照：Höganäs / Sandvik Osprey / BASF"
Enter
Sleep 800ms

# ── 6. apply to project ──────────────────────────────────
Type@40ms "> 用 Swiss 重写 globals.css 并加一个 /preview 测试页"
Sleep 300ms
Enter
Sleep 700ms

Hide
Type "printf '\\033[38;5;245m● Write(src/app/globals.css)\\033[0m\\n  \\033[2m└ tokens: ink #0A0A0A · accent #D72027 · radius 0\\033[0m\\n'"
Enter
Sleep 500ms
Type "printf '\\033[38;5;245m● Write(src/app/[locale]/preview/page.tsx)\\033[0m\\n  \\033[2m└ 6 sections · hero · spec strip · process · table\\033[0m\\n'"
Enter
Sleep 500ms
Type "printf '\\033[38;5;245m● Bash(npm run dev)\\033[0m\\n  \\033[2m└ ▲ Next.js 16  -  http://localhost:3002\\033[0m\\n\\n'"
Enter
Show
Sleep 600ms

Type@5ms "● 跑通了 → http://localhost:3002/preview"
Enter
Sleep 2s

# ── 7. end card  ─────────────────────────────────────────
Hide
Type "clear"
Enter
Type "printf '\\n\\n   \\033[1mui-styles-skill\\033[0m\\n   79 styles · bilingual · offline · one prompt\\n\\n   github.com/chrzamz/ui-styles-skill\\n\\n'"
Enter
Show
Sleep 2.5s
