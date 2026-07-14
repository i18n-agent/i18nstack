# i18nstack

[![skills.sh](https://skills.sh/b/i18n-agent/i18nstack)](https://skills.sh/i18n-agent/i18nstack)

**i18nstack turns AI coding agents into a full localization team: format engineer, QA tester, release gate, and 46 native-quality translators.**

Three battle-tested CLI tools, five workflow slash commands, and 46 language-specific translation skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Grok](https://github.com/xai-org/grok-cli), and [Codex](https://github.com/openai/codex), installed with one command.

## Install

### skills.sh (any supported agent)

Install all 55 skills via [skills.sh](https://skills.sh/) / [vercel-labs/skills](https://github.com/vercel-labs/skills):

```bash
npx skills add i18n-agent/i18nstack -g -y
```

Install a subset:

```bash
npx skills add i18n-agent/i18nstack -g -y --skill localize-ja --skill i18n-validate
```

List available skills without installing:

```bash
npx skills add i18n-agent/i18nstack --list
```

skills.sh installs skill definitions only. For the CLI tools (`i18n-convert`, `i18n-pseudo`, `i18n-validate`) and slash commands (`/i18n-wrap`, `/i18n-review`, …), run setup after cloning:

```bash
git clone --depth 1 https://github.com/i18n-agent/i18nstack.git ~/.claude/skills/i18nstack && ~/.claude/skills/i18nstack/setup
```

### Direct install (recommended)

**Claude Code**

```bash
git clone --depth 1 https://github.com/i18n-agent/i18nstack.git ~/.claude/skills/i18nstack && ~/.claude/skills/i18nstack/setup
```

**Grok**

```bash
git clone --depth 1 https://github.com/i18n-agent/i18nstack.git ~/.grok/skills/i18nstack && ~/.grok/skills/i18nstack/setup
```

**Codex**

```bash
git clone --depth 1 https://github.com/i18n-agent/i18nstack.git ~/.codex/i18nstack && ~/.codex/i18nstack/setup
```

That's it. The setup script installs the CLI tools (npm, with Homebrew fallback) and registers every skill and slash command with your agent. Clone into any supported location — setup registers **all installed agents** (Claude Code, Grok, Codex) when their config directories exist.

Codex uses a different skill format than Claude/Grok: setup writes adapter skills to `~/.agents/skills/` and slash prompts to `~/.codex/prompts/`, each pointing back to the native i18nstack source files.

## What's inside

### CLI tools (installed globally)

| Tool | Role | What it does |
|------|------|--------------|
| [`i18n-convert`](https://github.com/i18n-agent/i18n-convert) | Format engineer | Convert localization files between 32 formats: JSON, i18next, Flutter ARB, Android XML, iOS .strings/String Catalog, XLIFF, PO, YAML, RESX, CSV, Excel, and more. Warns before lossy conversions. |
| [`i18n-pseudo`](https://github.com/i18n-agent/i18n-pseudo) | QA tester | Pseudo-translate locale files to expose hardcoded strings, text overflow, encoding bugs, and RTL breakage before you pay for real translations. 7 strategies, 5 presets. |
| [`i18n-validate`](https://github.com/i18n-agent/i18n-validate) | Release gate | Validate translation files for missing keys, placeholder drift, malformed plurals, and untranslated values. CI-ready with JUnit/JSON output and meaningful exit codes. |

### Slash commands

| Command | What it does |
|---------|--------------|
| `/i18n-wrap [path] [--framework=...]` | Scan code for hardcoded user-facing strings and wrap them with the right i18n function (next-intl, react-i18next, vue-i18n, angular, svelte, python, ruby, flutter, ios, android). Updates locale files and validates. |
| `/i18n-review [path] [--framework=...]` | Read-only audit of existing i18n wrapping: over/under-wrapping, split sentences, hardcoded values, quality issues. |
| `/i18n-validate [path]` | Run validation and FIX every finding — placeholder drift, plural forms, missing keys (translated properly, never English filler) — looping until it passes. |
| `/i18n-convert <file> --to <format>` | Safe conversion workflow: resolve the format slug, dry-run for data-loss warnings, convert, verify key counts round-trip. |
| `/i18n-pseudo <files> [--preset=...]` | Generate pseudo locales, wire them into the app as a test locale, and hunt down the hardcoded strings and layout bugs they expose. |

### Translation skills (46 languages)

Each `localize-XX` skill is distilled from production translation prompts and enforces native-writer rules: formality registers, particle selection, plural systems, script conventions, and false-friend avoidance.

Arabic (ar), Bulgarian (bg), Bengali (bn), Catalan (ca), Czech (cs), Welsh (cy), Danish (da), German (de), Greek (el), Spanish (es), Estonian (et), Persian (fa), Finnish (fi), French (fr), Irish (ga), Hebrew (he), Hindi (hi), Croatian (hr), Hungarian (hu), Indonesian (id), Icelandic (is), Italian (it), Japanese (ja), Korean (ko), Lithuanian (lt), Latvian (lv), Malay (ms), Maltese (mt), Dutch (nl), Norwegian (no), Polish (pl), Portuguese (pt), Romanian (ro), Russian (ru), Slovak (sk), Slovenian (sl), Serbian (sr), Swedish (sv), Swahili (sw), Thai (th), Tagalog (tl), Turkish (tr), Ukrainian (uk), Urdu (ur), Vietnamese (vi), Chinese (zh)

## How it works

Clone into `~/.claude/skills/i18nstack`, `~/.grok/skills/i18nstack`, or `~/.codex/i18nstack`. Setup symlinks each skill directory into Claude/Grok and writes Codex adapter skills. A single `git pull` updates everything.

```
~/.claude/skills/  (or ~/.grok/skills/)
├── i18nstack/          ← this repo
├── i18n-convert  →  i18nstack/i18n-convert
├── localize-ja   →  i18nstack/localize-ja
└── ... (46 localize skills)

~/.claude/commands/  (symlinks)
~/.grok/commands/    (Grok-native copies with tool-mapping header)

~/.agents/skills/    (Codex adapter dirs: SKILL.md + agents/openai.yaml)
~/.codex/prompts/    (Codex slash prompts for /i18n-wrap, /i18n-validate, …)
```

## The workflow

Ship a new locale end to end:

1. **Convert** your source file into whatever format the project needs:
   ```bash
   i18n-convert en.json --to android-xml -o strings.xml
   ```
2. **Pseudo-translate** to prove every string goes through the i18n layer:
   ```bash
   i18n-pseudo en.json --preset layout -o pseudo/
   ```
   Load it as a fake locale, screenshot the app: un-bracketed English = hardcoded string.
3. **Translate** with Claude Code using the matching skill: "translate messages/en.json to Japanese" triggers `localize-ja` and its native-writer rules.
4. **Validate** before shipping:
   ```bash
   i18n-validate ./locales --strict
   ```

## Updating

```bash
cd ~/.claude/skills/i18nstack && git pull && ./setup
```

## Uninstalling

```bash
# Claude Code
cd ~/.claude/skills && find . -maxdepth 1 -type l -lname 'i18nstack/*' -delete && rm -rf i18nstack
cd ~/.claude/commands && find . -maxdepth 1 -type l -lname '*skills/i18nstack/*' -delete

# Grok (only removes files installed by i18nstack setup)
cd ~/.grok/skills && find . -maxdepth 1 -type l -lname 'i18nstack/*' -delete && rm -rf i18nstack
cd ~/.grok/commands && for f in i18n-wrap.md i18n-review.md i18n-validate.md i18n-convert.md i18n-pseudo.md; do
  [ -f "$f" ] && grep -q 'i18nstack `setup`' "$f" 2>/dev/null && rm -f "$f"
done
```

CLI tools: `npm uninstall -g @i18n-agent/i18n-convert @i18n-agent/i18n-pseudo @i18n-agent/i18n-validate`

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Grok](https://github.com/xai-org/grok-cli), or [Codex](https://github.com/openai/codex)
- Node.js/npm (or Homebrew) for the CLI tools

## License

MIT
