---
name: i18n-validate-workflow
description: "Validate translation files and FIX every problem found (missing keys, placeholder drift, plural errors), looping until validation passes"
---

# i18n-validate: $ARGUMENTS

Run the `i18n-validate` CLI on the given path (default: auto-detect the locales
directory — look for `locales/`, `messages/`, `i18n/`, `lang/`), then fix every
problem it reports. With `--no-fix`, stop after reporting.

## Step 1 — Setup check

```bash
command -v i18n-validate || npm install -g @i18n-agent/i18n-validate
```

## Step 2 — Validate (machine-readable)

```bash
i18n-validate <path> --format json [--ref <lang>] [--strict]
```

Exit 0 = clean: report "validation passed" and stop.
Exit 2 = bad arguments/config: fix the invocation, not the files.

## Step 3 — Fix findings (unless --no-fix)

Parse the JSON findings and fix in this priority order:

1. **parse-errors** — open the file, fix the syntax (trailing commas, encoding,
   malformed plural blocks). Never delete entries to make a file parse.
2. **placeholders** — make the translation's placeholders match the reference
   exactly (`{name}`, `{{count}}`, `%s`, `${var}`). Keep the translated text,
   correct only the placeholder tokens.
3. **plural-structure / plural-requirements** — add the CLDR-required plural
   forms for the target language (e.g. ru needs one/few/many/other). Translate
   each form properly; do not copy one form into all slots.
4. **missing-keys** — add the key with a real translation. If a `localize-XX`
   skill exists for the target language, apply its rules. Never insert the
   English value as filler and never invent placeholder text.
5. **extra-keys** — check git history/usage first (`grep -r` the key in the
   codebase). Only remove keys that are orphaned in the reference too;
   otherwise report them.
6. **empty-values / untranslated** (warnings) — translate them the same way as
   missing keys.

## Step 4 — Re-validate

Re-run Step 2 after fixing. Loop until exit 0 (max 3 rounds — if still failing,
report the stuck findings honestly instead of weakening the check).

## Rules

- NEVER skip checks (`--skip`) or drop `--strict` just to get a green exit.
- NEVER copy English into a translation slot to silence `missing-keys`.
- Preserve file formatting/key order; make minimal diffs.
- Summarize at the end: findings fixed per check type, files touched, final
  validation status.
