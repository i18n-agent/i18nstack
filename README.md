# i18nstack

**i18nstack turns Claude Code into a full localization team: format engineer, QA tester, release gate, and 46 native-quality translators.**

Three battle-tested CLI tools, five workflow slash commands, and 46 language-specific translation skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), installed with one command.

## Install

```bash
git clone --depth 1 https://github.com/i18n-agent/i18nstack.git ~/.claude/skills/i18nstack && ~/.claude/skills/i18nstack/setup
```

That's it. The setup script installs the CLI tools (npm, with Homebrew fallback) and registers every skill with Claude Code.

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

The repo lives at `~/.claude/skills/i18nstack`. Setup symlinks each skill directory into `~/.claude/skills/`, so Claude Code discovers them automatically and a single `git pull` updates everything.

```
~/.claude/skills/
├── i18nstack/          ← this repo
├── i18n-convert  →  i18nstack/i18n-convert
├── i18n-pseudo   →  i18nstack/i18n-pseudo
├── i18n-validate →  i18nstack/i18n-validate
├── localize-ja   →  i18nstack/localize-ja
└── ... (46 localize skills)

~/.claude/commands/
├── i18n-wrap.md     →  ../skills/i18nstack/commands/i18n-wrap.md
├── i18n-review.md   →  ../skills/i18nstack/commands/i18n-review.md
├── i18n-validate.md →  ../skills/i18nstack/commands/i18n-validate.md
├── i18n-convert.md  →  ../skills/i18nstack/commands/i18n-convert.md
└── i18n-pseudo.md   →  ../skills/i18nstack/commands/i18n-pseudo.md
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
cd ~/.claude/skills && find . -maxdepth 1 -type l -lname 'i18nstack/*' -delete && rm -rf i18nstack
cd ~/.claude/commands && find . -maxdepth 1 -type l -lname '*skills/i18nstack/*' -delete
```

CLI tools: `npm uninstall -g @i18n-agent/i18n-convert @i18n-agent/i18n-pseudo @i18n-agent/i18n-validate`

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- Node.js/npm (or Homebrew) for the CLI tools

## License

MIT
