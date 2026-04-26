markdown# 🧠 Free MDSkills

A curated collection of free, open-source agent skills for [mdskill.dev](https://mdskill.dev) — the open directory of AI agent skills.

Skills in this repo are automatically discovered, audited, and listed on the mdskill.dev leaderboard. Anyone can install them for free using the `mdskill` CLI.

---

## What Are Skills?

Skills are modular knowledge files that give AI coding agents procedural superpowers.

Each skill is a single `SKILL.md` file — a structured Markdown document your agent reads as context before tackling a task. Think of them as plugins: drop one in, and your agent instantly knows how to do something new.

Skills work with any agent that reads local context files — including:
- Claude Code
- Cursor
- GitHub Copilot
- Cline
- Windsurf
- And more

---

## How mdskill.dev Works

The mdskill ecosystem has four parts that work together:
GitHub Repos             mdskill.dev               Your Project
(SKILL.md files)  ──→   Scraper + Index  ──→  CLI  ──→  .skills/ folder

### 1. Indexer (Scraper)
A daily pipeline crawls GitHub for repositories containing `SKILL.md` files. It checks curated publishers as well as repos tagged with topics like `skill`, `agent`, `claude`, `llm`, `copilot`, and `mcp`.

Before indexing, every repo must pass a qualification gate:
- At least one `SKILL.md` with valid frontmatter (`name` + `description`)
- The repo description or topics contain at least one relevant keyword
- ≥ 5 GitHub stars (for non-curated sources)
- Repo is at least 7 days old
- LLM confidence scoring ≥ 80 for immediate indexing (60–79 goes to manual review)

### 2. Security Audit
After indexing, every skill is scanned by four automated auditors before appearing on the leaderboard:
- **Secrets scanner** — detects tokens, API keys, passwords, connection strings
- **Prompt injection scanner** — detects instruction overrides, jailbreaks, exfiltration patterns
- **URL safety scanner** — flags suspicious domains, shorteners, IP-based URLs
- **Content integrity scanner** — checks for oversized files, null bytes, link farms, base64 bloat

Audit status is visible on each skill's detail page at `mdskill.dev`.

### 3. Backend API
The API serves skill content, validates CLI API keys, and checks subscriptions. Skills marked `public` are free — no subscription needed.

### 4. CLI
The `mdskill` CLI lets you install skills directly into your project with one command.

---

## Using Skills — CLI Quickstart

### Install the CLI

```bash
npm install -g mdskill
```

> Requires Node.js 20 or higher.

### Sign in

```bash
mdskill login
```

Opens a browser flow and saves your API key locally. Required for all skill installs.

### Browse available skills

```bash
mdskill list
```

### Search by keyword

```bash
mdskill search <query>
```

Minimum 2 characters. Returns matching skills with name, type, and description.

### Install a skill

```bash
mdskill add <owner/skill-name>
```

The skill is written to `.skills/<owner>/<skill-name>/SKILL.md` inside your project. The `.skills/` directory is automatically added to `.gitignore` so skill files aren't committed.

### Other commands

| Command | Description |
|---|---|
| `mdskill login` | Sign in via browser and save API key |
| `mdskill logout` | Sign out and remove local API key |
| `mdskill whoami` | Show the currently signed-in user |
| `mdskill list` | List all available skills |
| `mdskill search <query>` | Search skills by keyword |
| `mdskill add <slug>` | Install a skill into your project |
| `mdskill info <slug>` | Show metadata for a specific skill |

---

## Skill Types

| Type | Cost | Who can install |
|---|---|---|
| **Public** | Free | All signed-in users |
| **Premium** | Subscription required | Active subscribers |

All skills in this repository are **public** — free for anyone to install after login.

Run `mdskill info <slug>` to confirm a skill's type before installing.

---

## How Skills Are Ranked

The leaderboard at [mdskill.dev](https://mdskill.dev) ranks skills by **install count** — drawn from anonymous telemetry collected when `mdskill add` runs. No personal data or usage patterns are tracked. Only which skills are installed and how often.

---

## Skill File Format

Each skill is a single Markdown file named `SKILL.md` with a YAML frontmatter block at the top.

### Required frontmatter

```markdown
---
name: your-skill-name
description: A short description of what this skill teaches the agent to do.
license: MIT
---

# Your Skill Title

The body of your skill goes here. Write it as clear instructions the AI agent
will read as context when performing the task this skill covers.

## When to use this skill
Explain the situations where this skill should be applied.

## Steps
1. Step one
2. Step two
3. Step three
```

### Frontmatter fields

| Field | Required | Notes |
|---|---|---|
| `name` | ✅ Yes | Unique identifier. Use `kebab-case`. |
| `description` | ✅ Yes | One line. Shown in `mdskill list` and search results. |
| `license` | Recommended | e.g. `MIT`, `Apache-2.0` |

### File location

Skills are discovered by path. Place your `SKILL.md` files as:
your-repo/
skill-name/
SKILL.md

Or at the root:
your-repo/
SKILL.md

Multiple skills per repo are supported — one `SKILL.md` per subdirectory.

---

## Contributing a Free Skill

Want your skill listed on mdskill.dev?

### Option 1 — Submit to this repo
1. Fork this repository
2. Create a folder with your skill name: `skills/<your-skill-name>/`
3. Add a `SKILL.md` inside it with valid frontmatter
4. Open a Pull Request

Skills merged here are automatically picked up by the next daily indexer run.

### Option 2 — Publish your own repo
Publish a GitHub repo with `SKILL.md` files and tag it with the topic `agent-skills`. The daily scraper will discover it automatically if it meets the qualification criteria (see [How mdskill.dev Works](#how-mdskilldev-works) above).

---

## Qualification Criteria for Auto-Discovery

If you're publishing skills in your own repo and want them auto-indexed:

- ✅ At least one `SKILL.md` with `name` and `description` in frontmatter
- ✅ Repo description or topics include: `skill`, `agent`, `ai`, `claude`, `llm`, `copilot`, or `mcp`
- ✅ At least **5 GitHub stars**
- ✅ Repo is at least **7 days old**

Repos with LLM confidence score ≥ 80 are indexed immediately. Scores of 60–79 go to manual review.

---

## Links

- 🌐 Directory: [mdskill.dev](https://mdskill.dev)
- 📖 Docs: [mdskill.dev/docs](https://mdskill.dev/docs)
- ⌨️ CLI Reference: [mdskill.dev/docs/cli](https://mdskill.dev/docs/cli)
- 💎 Premium: [mdskill.dev/upgrade](https://mdskill.dev/upgrade)

---

## License

MIT
