---
description: "Pseudo-translate locale files to QA an i18n implementation, then hunt down the hardcoded strings and layout bugs it exposes"
argument-hint: "<files> [--preset=default|layout|charset|rtl|full] [-o output-dir]"
allowed-tools: [Bash, Read, Edit, Glob, Grep, TodoWrite]
---

# i18n-pseudo: $ARGUMENTS

Pseudo-translate the given locale file(s) with the `i18n-pseudo` CLI, wire the
result into the app as a test locale, and report what the test exposes.

## Step 1 — Setup check

```bash
command -v i18n-pseudo || npm install -g @i18n-agent/i18n-pseudo
```

## Step 2 — Pick the preset (if the user didn't)

| Situation | Preset |
|-----------|--------|
| Quick scan for untranslated/hardcoded strings | `default` |
| Target languages with long words (de, fi) / overflow worries | `layout` |
| CJK targets or font/encoding concerns | `charset` |
| Arabic/Hebrew support | `rtl` |
| Pre-release full sweep | `full` |

## Step 3 — Generate

```bash
i18n-pseudo <files> --preset <preset> -o <output-dir>
```

Default output dir: `pseudo/` next to the input. Never use `--in-place` on the
real reference locale unless the user explicitly asks; if they do, keep the
`.bak` files.

## Step 4 — Wire it up and inspect

- Register the pseudo output as a test locale in the project's i18n config
  (e.g. a `qps` or `en-XA` locale) so the app can actually render it.
- Verify placeholders survived: grep the pseudo output for the placeholder
  patterns present in the source (`{`, `{{`, `%s`, `${`); they must be intact.
- If the app can be run/screenshotted, render key screens in the pseudo
  locale: any text WITHOUT brackets/accents is a hardcoded string that bypassed
  the i18n layer.

## Step 5 — Fix or report

List every hardcoded string found with file:line. If the user asked for fixes,
wrap them (use `/i18n-wrap` for bulk wrapping); otherwise report the list and
the recommended next step.
