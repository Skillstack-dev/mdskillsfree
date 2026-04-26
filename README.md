# mdskillsfree

> Free, open Claude skills you can install in one line.  
> Built for Claude Code and claude.ai users.  
> No config. No setup. Just better Claude behaviour — immediately.

---

## Install any skill

```bash
npx mdskill add token-optimizer
```

That's it. Claude Code picks it up automatically on next launch.

---

## Skills available

| Skill | What it does | Install |
|---|---|---|
| `token-optimizer` | Cuts Claude response bloat — no preambles, no over-explanation | `npx mdskill add token-optimizer` |

> More skills coming. [Browse the full catalogue at mdskill.dev →](http://mdskill.dev)

---

## What is a skill?

A skill is a markdown instruction file that changes how Claude behaves — permanently, across every conversation. You install it once, Claude reads it automatically, and your experience improves without you doing anything else.

Think of it as a persistent briefing note Claude always has in context.

```
Without skill                        With skill
─────────────────────────────────    ─────────────────────────────────
"Great question! Let me explain      "Canberra."
 the history of Australia's
 capital, which is actually
 Canberra and not Sydney as
 many people assume..."
```

---

## How to install manually

If you prefer not to use the CLI, you can install any skill by hand:

**1. Find the skill folder in this repo**

**2. Copy it to your Claude skills directory**

```bash
# Mac / Linux
cp -r token-optimizer ~/.claude/skills/

# Windows
xcopy token-optimizer %USERPROFILE%\.claude\skills\token-optimizer /E /I
```

**3. Restart Claude Code**

Claude picks it up automatically — no configuration needed.

---

## What mdskillsfree is

This repo is the **free, open layer** of [mdskill.dev](http://mdskill.dev).

Every skill here is:
- Free forever
- MIT licensed — use it in anything, commercial or not
- Community maintained — PRs welcome
- Verified to work with Claude Code and claude.ai

---

## Want more?

**[mdskill.dev](http://mdskill.dev)** is the full skills platform — search, browse, and install skills across every category. Productivity, coding, writing, research, and more.

Free skills live here. Everything else lives there.

---

## Contribute a skill

Have a skill that makes Claude better? Submit it here.

```
your-skill/
├── SKILL.md          ← required
├── scripts/          ← optional, executable helpers
└── references/       ← optional, reference docs
```

Open a PR. If it works and adds genuine value, it gets merged.

**Contribution guidelines:** Keep SKILL.md under 500 lines. No vendor lock-in. Must work on Claude Code and claude.ai. Tested before submitting.

---

## License

MIT — free to use, modify, distribute, commercially or otherwise.  
Credit appreciated, not required.

---

<div align="center">

**[Browse all skills at mdskill.dev →](http://mdskill.dev)**

*Free skills live here. The full catalogue lives there.*

</div>
