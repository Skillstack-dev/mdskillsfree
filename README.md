# 🧠 Free MDSkills

> The open collection of free agent skills for [mdskill.dev](https://mdskill.dev)

Skills are modular knowledge files that give your AI coding agent new capabilities — instantly. Drop one in, and your agent knows how to do something it didn't before. Think of them as plugins for your AI.

Works with **Claude Code**, **Cursor**, **GitHub Copilot**, **Cline**, **Windsurf**, and any agent that reads local context files.

---

## Install a Skill in 3 Steps

```bash
# 1. Install the CLI (requires Node.js 20+)
npm install -g mdskill

# 2. Sign in
mdskill login

# 3. Add a skill to your project
mdskill add <skill-name>
```

The skill lands in `.skills/` inside your project — ready for your agent to read.

---

## Useful Commands

| Command | What it does |
|---|---|
| `mdskill list` | Browse all available skills |
| `mdskill search <query>` | Find skills by keyword |
| `mdskill add <slug>` | Install a skill into your project |
| `mdskill info <slug>` | View details and audit status for a skill |

---

## Every Skill is Security Audited

Before any skill appears on the [mdskill.dev](https://mdskill.dev) leaderboard, it goes through an automated security review:

- 🔑 **Secrets scan** — flags tokens, API keys, and credentials
- 🛡️ **Prompt injection scan** — detects instruction overrides and jailbreak patterns
- 🔗 **URL safety scan** — checks for suspicious links and redirects
- 📄 **Content integrity scan** — catches oversized files and obfuscated content

Audit status is visible on every skill's page at mdskill.dev.

---

## All skills here are free

No subscription needed. Sign in once, install anything in this repo.

👉 [Browse the directory at mdskill.dev](https://mdskill.dev)

---

## License

MIT
