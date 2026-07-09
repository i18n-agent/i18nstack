---
name: i18nstack
description: |
  Complete i18n/localization toolkit for Claude Code. Use when doing ANY
  internationalization work: converting localization files between 32 formats
  (i18n-convert), pseudo-translating files to QA an i18n implementation
  (i18n-pseudo), validating translation files for missing keys / placeholder
  drift / plural errors (i18n-validate), or translating UI strings, marketing
  copy, and docs into 46 languages with native-quality rules (localize-*).
allowed-tools:
  - Bash
  - Read
---

# i18nstack: the i18n toolkit for Claude Code

Three CLI tools + 46 language-specific translation skills. Route any i18n task
to the right piece:

| Task | Use |
|------|-----|
| Convert a localization file to another format | `i18n-convert` CLI (see `i18n-convert` skill) |
| Generate pseudo-translations to test an i18n setup | `i18n-pseudo` CLI (see `i18n-pseudo` skill) |
| Check translation files for missing keys, placeholder drift, plural errors | `i18n-validate` CLI (see `i18n-validate` skill) |
| Translate text into language XX with native-quality rules | `localize-XX` skill (46 languages, e.g. `localize-ja`, `localize-de`) |
| Wrap hardcoded strings in code with i18n functions | `/i18n-wrap` command |
| Audit existing i18n wrapping for quality issues | `/i18n-review` command |
| Validate AND fix all findings until green | `/i18n-validate` command |
| Safe format conversion with data-loss checks | `/i18n-convert` command |
| Pseudo-locale QA sweep with fix-up | `/i18n-pseudo` command |

## Setup check (run BEFORE using any CLI)

```bash
for t in i18n-convert i18n-pseudo i18n-validate; do command -v $t >/dev/null || echo "MISSING: $t"; done
```

If anything is missing, run the stack's setup: `~/.claude/skills/i18nstack/setup`
(or `npm install -g @i18n-agent/<tool>`).

## Recommended workflow (new locale end to end)

1. **Convert** the source file into the target project's format if needed:
   `i18n-convert en.json --to android-xml -o strings.xml`
2. **Pseudo-translate** before paying for real translations to catch hardcoded
   strings, overflow, and encoding bugs:
   `i18n-pseudo en.json --preset layout -o pseudo/`
3. **Translate** using the matching `localize-XX` skill — it enforces
   native-writer rules (formality, particles, plurals, script conventions).
4. **Validate** the result before shipping:
   `i18n-validate ./locales --strict`

## Available localize skills (46)

ar bg bn ca cs cy da de el es et fa fi fr ga he hi hr hu id is it ja ko lt lv
ms mt nl no pl pt ro ru sk sl sr sv sw th tl tr uk ur vi zh

Each is a standalone skill (`localize-ja`, `localize-de`, …) distilled from
production translation prompts — invoke the one matching your target language.

## Updating

```bash
cd ~/.claude/skills/i18nstack && git pull && ./setup
```
