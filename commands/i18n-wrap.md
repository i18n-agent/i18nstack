---
description: "Scan and wrap hardcoded user-facing strings with i18n functions, framework-generic"
argument-hint: "[path] [--framework=next-intl|react-i18next|vue-i18n|angular|svelte|python|ruby|flutter|ios|android]"
allowed-tools: [Bash, Read, Edit, Write, Glob, Grep, LS, TodoWrite, MultiEdit, Agent]
---

<!-- ROLE: You are an i18n wrapping agent. You scan code, wrap hardcoded strings with framework-appropriate i18n functions, update locale files, and validate. -->

# i18n-wrap: $ARGUMENTS

<instructions priority="critical">

## DECISION RULE
If even ONE target language needs a different string, it MUST be wrapped.
When uncertain: wrap it. Over-wrapping = minor annoyance. Under-wrapping = broken UX.

## ANTI-PATTERNS (never do these)
- NEVER split sentences across keys (`t('greeting') + name` -- word order varies)
- NEVER wrap technical constants (API, PDF, USD, regex, CSS classes, env vars, console.log)
- NEVER guess framework -- ask user if ambiguous
- NEVER delete existing translations or overwrite them
- NEVER use `defaultValue` in t() calls
- NEVER transform t() output (`.toLowerCase()`, `.toUpperCase()`, `.trim()`, template casing) -- case rules differ by language (e.g. Turkish İ/i, German ß→SS); create a separate key instead
- NEVER interpolate count outside t() (`{n} {t('label')}`) -- bypasses plural handling ("1 languages"); use single key with ICU plurals: `t('label_count', {count: n})`

</instructions>

## Phase 1: DETECT (framework + i18n setup)

MUST detect before any changes:

| Detect | How |
|--------|-----|
| Framework | package.json, imports, config files |
| Translation fn | t(), $t(), _(), $localize, NSLocalizedString, getString |
| Locale files | Location + format (JSON/YAML/PO/XLIFF/ARB/.strings/.xml) |
| Key convention | dot.notation / nested / flat / prefixed |
| Source locale | en, en-US, etc. |
| Target locales | All configured locales |
| Plural format | ICU MessageFormat / suffix keys / pipe / YAML / stringsdict |

If ambiguous, ask user. Never guess.

## Phase 2: AUDIT (clean existing issues first)

**Use Agent tool (subagent_type: "research") to scan locale files in parallel -- one subagent per locale file checking for non-translatable keys.**

<non-translatable-keys>
Remove: empty values, space-only, emoji-only, number-only ("0","404"), single punctuation ("-","..."), pure HTML without text (`<br/>`), brand names ("GitHub"), technical acronyms identical across all langs ("API","PDF").

Unwrap: console/debug messages, technical IDs, CSS classes, HTML IDs, config values, env vars in t() calls.
</non-translatable-keys>

<false-positives>
These LOOK like constants but DO translate -- verify before removing:
"OK"(JP:了解), "Email"(CN:电子邮件), "N/A"(JP:該当なし), "Yes"/"No"(DE:Ja/Nein), "Home"/"Search"/"Login", single-word labels ("Name","Date","Status","All","None"), status words ("enabled","disabled","active","pending").
Decision: "Does this EXACT string work in ALL target languages?" If no or unsure, keep wrapped.
</false-positives>

Report audit results before proceeding.

## Phase 3: SCAN (find unwrapped strings)

**Use Agent tool (subagent_type: "research") for parallel scanning -- delegate one subagent per file type pattern (JSX/TSX, Python, Ruby, Swift/Kotlin).**

Each subagent should search its file type for:
1. Text content between tags: `>[^<{]*[A-Za-z]{2,}[^<{]*<`
2. Translatable attributes: `(placeholder|title|alt|aria-label|aria-description)="[^"]*[A-Za-z]{2,}[^"]*"`
3. Message/label assignments: `(message|label|text|title|description|placeholder|error|warning|success)\s*[:=]\s*["'][A-Za-z]`

**Glob exclusions (always):** `!**/node_modules/** !**/*.test.* !**/*.spec.* !**/__tests__/** !**/dist/** !**/build/** !**/.next/** !**/coverage/** !**/*.config.* !**/*.d.ts`

## Phase 4: CATEGORIZE (semantic key namespaces)

| Prefix | Content |
|--------|---------|
| `common.` | Shared buttons, labels, generic messages |
| `nav.` | Menu items, breadcrumbs, links |
| `auth.` | Login, register, password forms |
| `{feature}.form.` / `validation.` | Form labels, validation errors |
| `errors.` / `{feature}.errors.` | User-facing error messages |
| `{feature}.success.` / `notifications.` | Confirmations, toasts |
| `{pageName}.` | Page headings, descriptions, content |
| `meta.` | SEO titles, descriptions |
| Inline with parent | aria-labels near their component keys |

Same text + different context = different keys (e.g., `profile.buttons.save` vs `settings.buttons.save`).

## Phase 5: WRAP (apply i18n functions)

For each string: import hook/function if needed, initialize translator, replace hardcoded string, handle interpolation (`${name}` -> `t('key', {name})`), convert ternary plurals to ICU/framework format, replace manual date/number formatting with Intl formatters. Never break JSX structure.

## Phase 6: KEYS (update locale files)

1. Add new keys to source locale, maintaining structure/formatting/ordering
2. For target locales: add missing keys as `"[NEEDS_TRANSLATION] English text"`
3. NEVER remove existing keys or overwrite existing translations
4. Validate JSON/YAML is parseable after changes

## Phase 7: VALIDATE

**Use Agent tool (subagent_type: "research") to run validation checks in parallel:**
- Subagent 1: Build + lint (`pnpm build && pnpm lint` or framework equivalent)
- Subagent 2: Key parity check across all locales (count, missing, extra, placeholder match, plural categories)
- Subagent 3: Run test suite (update assertions for changed text, never delete tests)

## QUALITY CHECKLISTS

<over-wrapping>
MUST NOT wrap: technical acronyms (PDF/USB/WiFi/URL/API/SDK/JSON/CSV), brand names (GitHub/iPhone/Chrome), units/ISO codes (kg/km/MB/USD), log levels (DEBUG/INFO/ERROR), version strings (v2.1.0), regex/code/config, emoji-only, console.log/debug messages.
</over-wrapping>

<under-wrapping>
MUST wrap (commonly missed):
- Short labels: "OK"/"Cancel", "Yes"/"No", "Email"/"Name"/"Date"/"Status", "Home"/"Search"/"Login"/"Logout"
- Filter/select options: "N/A"/"None"/"All"/"Other"
- Status text: "enabled"/"disabled"/"active"/"pending"
- Form hints: "(optional)"/"(required)", "e.g."/"etc."
- Counter labels: "items"/"results"/"pages" (+ plural rules)
- Ordinals: "1st"/"2nd"/"3rd" (completely different per language)
- Aria-labels on icon buttons (close "x", add "+")
</under-wrapping>

<incomplete-strings>
MUST be single keys (never concatenate):
- Label + punctuation: colon INSIDE key (CJK uses fullwidth `：`)
- Greeting + name: use `t('greeting', {name})` (word order varies)
- Count + unit: single key with plurals (never `t('count') + t('items')`)
- Standalone connectors: "or"/"and" belong inside full sentence
- Error + message: use `t('errorMessage', {message})`
- Step progress: use `t('stepProgress', {step, total})`
</incomplete-strings>

<hardcoded-values>
MUST be parameters (never baked in):
File extensions -> `{formats}`, limits -> `{limit}`, counts -> `{count}` + plurals, emails/URLs -> `{email}`, versions -> `{version}`, lists -> `{languages}`, prices -> `{price}` + Intl.NumberFormat, dates -> `{date}` + Intl.DateTimeFormat, nav paths -> `{path}`.
Test: if it could change without a code deploy, it MUST be a `{parameter}`.
</hardcoded-values>

<punctuation>
Keep INSIDE translated strings (locale-sensitive):
Quotes: EN `"text"` / JP `「テキスト」` / CN `"文本"`.  Separators: use Intl.ListFormat.  Colons: EN `:` / CJK `：`.  Ellipsis: EN `...` / JP `…` / CN `……`.  Parens: EN `()` / CJK `（）`.
</punctuation>

## FRAMEWORK CHECKLISTS

| Framework | Import/Init | Plurals | Interpolation | Rich text/markup | Key notes |
|-----------|-------------|---------|---------------|-----------------|-----------|
| **next-intl** | `useTranslations(ns)` client, `await getTranslations(ns)` server | ICU: `{count, plural, one{#} other{#}}` | `t('key', {name})` | `t.rich('key', {bold: c=><b>{c}</b>})` | No defaultValue; NextIntlClientProvider needs `locale` prop; deep merge fallback in request.ts |
| **react-i18next** | `useTranslation(ns)` hook, `withTranslation` HOC | Suffix: `key_one`, `key_other` | `{{name}}` in JSON | `<Trans i18nKey="key">` | Configure fallback lang + language detector |
| **vue-i18n** | `$t()` template, `useI18n()` script setup | Pipe: `no items \| {n} item \| {n} items` | `$t('key', {name})` | `<i18n-t keypath="key">` | Configure `fallbackLocale`; lazy load for large apps |
| **Angular** | `i18n` attr, `$localize` in TS | ICU in templates | ICU expressions | `i18n` attribute | Extract with `ng extract-i18n`; XLIFF format; per-locale builds |
| **Svelte** | `$_('key')` / `$format('key')` | ICU MessageFormat | `$_('key', {values: {name}})` | N/A | `init()` with fallback; `waitLocale()` to prevent FOUC |
| **Python** | `_("str")` / `gettext("str")` | `ngettext("sg","pl",n)` | `_("Hi %(name)s") % {"name": n}` | `{% trans %}` / `{% blocktrans %}` | PO->MO compile; `pgettext` for context; no f-strings in gettext |
| **Ruby** | `t('key')` / `I18n.t('key')` | `count:` + zero/one/other YAML | `t('key', name: val)` | ERB: `<%= t('key') %>` | YAML in config/locales; lazy lookup `.key` in views |
| **Flutter** | `AppLocalizations.of(context)!.key` | ICU in ARB | ICU MessageFormat | N/A | ARB in lib/l10n; `flutter gen-l10n`; configure delegates+supportedLocales |
| **iOS** | `NSLocalizedString("key", comment:)` / `String(localized:)` | .stringsdict | `String.localizedStringWithFormat` | N/A | .strings in {locale}.lproj; XLIFF export; set CFBundleDevelopmentRegion |
| **Android** | `getString(R.string.key)` / `@string/key` XML | `<plurals>` element | `getString(R.string.key, arg)` %1$s | N/A | strings.xml in res/values-{locale}; `resConfigs` in build.gradle |

## REFERENCE TABLES

<plural-reference>

| Language | =0 | 1 | 2 | 5 | 21 | Forms |
|----------|-----|---|---|---|-----|-------|
| EN/DE/ES | other | one | other | other | other | one, other |
| FR/PT-BR | one | one | other | other | other | one, other (0+1=one) |
| JA/KO/ZH | other | other | other | other | other | other only |
| AR | zero | one | two | few | other | zero,one,two,few,many,other |
| RU/PL | other | one | other | many | one | one,few,many,other |

Test with: 0, 1, 2, 5, 21.
</plural-reference>

<expansion-reference>

| Language | Avg expansion | Notes |
|----------|--------------|-------|
| DE/RU | +30% (max +50%) | Flag tight layouts |
| FR | +20% (max +40%) | |
| ES/PT | +25% (max +40%) | |
| AR | +25% (max +50%) | + RTL |
| JA | -30% chars | Wider glyphs |
| ZH | -50% chars | Wider glyphs |
| KO | -20% chars | Wider glyphs |

</expansion-reference>

## OUTPUT FORMAT

```
i18n Wrap: {target}
========================================
Framework: {detected} | Locale: {format} | Source: {locale} | Targets: [{list}]

--- AUDIT ---
  Cleaned: {n} non-translatable keys | Unwrapped: {n} t() calls reverted

--- SCAN ---
  Files: {n} scanned | Strings: {n} found | Already wrapped: {n} | Newly wrapped: {n} | Skipped: {n}

--- KEYS ---
  {namespace}.*: {n} keys
  ...

--- LOCALE FILES ---
  {file}: +{n} keys
  Missing translations: {n} across {n} locales

--- VALIDATION ---
  Build: PASS/FAIL | Lint: PASS/FAIL | Tests: PASS/FAIL ({n} updated) | Key parity: PASS/FAIL | Plurals: PASS/FAIL

--- WARNINGS ---
  🔴 {critical issues}
  🟡 {quality concerns}
  🔵 {expansion risks, suggestions}

--- NEXT STEPS ---
  1. Send {n} keys for translation to {locales}
  2. Review flagged context-dependent strings
```

## PRINCIPLES
Detect don't assume. Audit first. Semantic keys. Full sentences never split. Named params `{name}` not `{0}`. Framework-native plurals. Key parity across locales. Non-destructive. Validate everything.
