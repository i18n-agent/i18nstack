---
description: "Review existing i18n-wrapped strings for quality issues, over/under-wrapping, split sentences, and hardcoded values"
argument-hint: "[path] [--framework=next-intl|react-i18next|vue-i18n|angular|svelte|python|ruby|flutter|ios|android]"
allowed-tools: [Bash, Read, Edit, Glob, Grep, LS, TodoWrite, Agent]
---

<!-- ROLE: You are an i18n review agent. You audit existing i18n wrapping for quality issues. This is a READ-ONLY audit -- report problems but do NOT apply fixes unless explicitly asked. -->

# i18n-review: $ARGUMENTS

<instructions priority="critical">

## MODE
Read-only audit. Report issues with file, line, current code, and suggested fix. Never modify code unless user explicitly asks.

## SEVERITY
- 🔴 **CRITICAL** -- Broken/wrong translations (split sentences, missing plurals, placeholder mismatches)
- 🟡 **WARNING** -- Quality/consistency degradation (over/under-wrapping, non-semantic keys)
- 🔵 **INFO** -- Improvement suggestions (expansion risks, naming conventions, key organization)

## DECISION RULE
If even ONE target language needs a different string, it MUST be wrapped.

## ANTI-PATTERNS
- NEVER auto-remove keys -- report only
- NEVER mark dynamic-key-covered keys as unused without noting the dynamic pattern
- NEVER flag false positives: "OK"/"Email"/"Yes"/"No" as button/form labels ARE translatable

</instructions>

## Phase 1: DETECT (framework + i18n setup)

| Detect | How |
|--------|-----|
| Framework | package.json, imports, config files |
| Translation fn | t(), $t(), _(), $localize, NSLocalizedString, getString |
| Locale files | Location + format (JSON/YAML/PO/XLIFF/ARB/.strings/.xml) |
| Key convention | dot.notation / nested / flat / prefixed |
| Source + target locales | All configured |
| Plural format | ICU / suffix / pipe / YAML / stringsdict |

## Phase 2-8: PARALLEL REVIEW

**Use Agent tool (subagent_type: "research") to run review phases in parallel. Launch up to 4 subagents simultaneously:**

**Subagent A: Over-wrapping + Under-wrapping scan**
**Subagent B: Split sentences + Hardcoded values scan**
**Subagent C: Locale file quality + Pluralization review**
**Subagent D: Unused keys analysis**

Then run text expansion review on the main thread (needs results from other phases).

---

### Subagent A: OVER-WRAPPING + UNDER-WRAPPING

<over-wrapping>
Scan all t()/equivalent calls. Flag any wrapping non-translatable content:
- Technical acronyms: PDF, USB, WiFi, URL, API, SDK, JSON, CSV
- Brand names: GitHub, iPhone, Chrome, Google
- Units/ISO codes: kg, km, MB, USD, US, JP
- Internal strings: log levels (DEBUG/INFO/ERROR), version strings, regex, code, config values
- Non-text: emoji-only, console/debug messages, tech IDs, CSS classes, HTML IDs, env vars

**But verify first -- these LOOK constant but DO translate:**
"OK"(JP:了解,CN:确定), "Email"(CN:电子邮件,JP:メール), "N/A"(JP:該当なし), "Yes"/"No"(DE:Ja/Nein), "Home"/"Search"/"Login", single-word labels, status words.
Litmus test: "Does this EXACT string work in ALL target languages?" If yes -> over-wrapped.
</over-wrapping>

<under-wrapping>
Scan source files for hardcoded user-facing strings NOT wrapped.

Search patterns per file type:
- JSX/TSX/Vue: tag content `>[^<{]*[A-Za-z]{2,}[^<{]*<`, translatable attrs (placeholder/title/alt/aria-label), message assignments
- Python: message/label assignments, Django templates without `{% trans %}`
- Ruby: ERB tag content, flash/render notice assignments
- Swift/Kotlin: Text/Label/title/message/hint assignments

Commonly missed: "OK"/"Cancel", "Yes"/"No", form labels ("Email"/"Name"/"Date"), nav items, filter options ("N/A"/"None"/"All"), status text, "(optional)"/"(required)", "e.g."/"etc.", counter labels (+ plurals), ordinals ("1st"/"2nd"), aria-labels on icon buttons.
</under-wrapping>

**Glob exclusions (always):** `!**/node_modules/** !**/*.test.* !**/*.spec.* !**/__tests__/** !**/dist/** !**/build/** !**/.next/** !**/coverage/** !**/*.config.* !**/*.d.ts`

---

### Subagent B: SPLIT SENTENCES + HARDCODED VALUES

<split-sentences>
The #1 i18n quality issue. Flag these concatenation anti-patterns:

| Pattern | Problem | Fix |
|---------|---------|-----|
| `t('label') + ':'` | CJK uses fullwidth `：` | Colon inside key |
| `t('label') + ' - ' + val` | Separator varies by locale | Single key |
| `t('greeting') + name` | Word order differs (JP: name first) | `t('greeting', {name})` |
| `t('count') + ' ' + t('items')` | Breaks word order | Single key + plurals |
| `t('or')` / `t('and')` standalone | Connectors inside full sentence | Merge into parent key |
| `t('error') + ': ' + msg` | Separator varies | `t('errorMessage', {message})` |
| `t('step') + n + '/' + total` | Format differs per locale | `t('stepProgress', {step, total})` |
| `t('label').toLowerCase()` | Case rules differ by language (Turkish İ/i, German ß→SS) | Separate key with correct casing |
| `{n} {t('label')}` (JSX) | Bypasses plural handling ("1 languages") | `t('label_count', {count: n})` with ICU plurals |

Search patterns:
```bash
rg -n 't\([^)]+\)\s*\+\s*["\x27`:}]'     # t() + string
rg -n '["\x27]\s*\+\s*t\('                 # string + t()
rg -n '`[^`]*\$\{t\('                      # template literal with t()
rg -n 't\([^)]+\).*t\([^)]+\)'             # multiple t() concatenated
```
</split-sentences>

<hardcoded-values>
Check locale files for values that should be parameters:

| Hardcoded | Should be | Format |
|-----------|-----------|--------|
| File extensions (".json") | `{formats}` | string |
| Limits ("10MB") | `{limit}` | string |
| Counts ("14 days") | `{count}` | + plurals |
| Emails/URLs | `{email}` / `{url}` | string |
| Version numbers | `{version}` | string |
| Lists ("English, French") | `{languages}` | Intl.ListFormat |
| Prices ("$9.99") | `{price}` | Intl.NumberFormat |
| Dates ("Jan 1, 2025") | `{date}` | Intl.DateTimeFormat |
| Nav paths ("Settings > Account") | Translate + locale separator | parameterize |

Test: if it could change without a code deploy, it MUST be a `{parameter}`.
</hardcoded-values>

---

### Subagent C: LOCALE FILE QUALITY + PLURALIZATION

<locale-quality>
**Non-translatable keys to flag:** empty, space-only, emoji-only, number-only ("0","404"), single punctuation, pure HTML without text, untranslatable brand names, technical acronyms.

**Key parity (per locale):** count vs source, missing keys, extra keys, placeholder name mismatches, plural category coverage.

**Key naming quality:** mixed conventions (camelCase/snake_case/dot.notation), non-semantic keys ("text1","label2","msg_3"), incorrect scope sharing.
</locale-quality>

<pluralization>
Flag broken plural patterns:
- Code ternaries: `count === 1 ? 'item' : 'items'` -- must use i18n plurals
- Manual concatenation: `count + ' item' + (count !== 1 ? 's' : '')` -- broken for non-EN
- Missing categories for target languages (Arabic needs 6 forms, Russian/Polish need 4)

| Language | =0 | 1 | 2 | 5 | 21 | Required forms |
|----------|-----|---|---|---|-----|----------------|
| EN/DE/ES | other | one | other | other | other | one, other |
| FR/PT-BR | one | one | other | other | other | one, other |
| JA/KO/ZH | other | other | other | other | other | other only |
| AR | zero | one | two | few | other | zero,one,two,few,many,other |
| RU/PL | other | one | other | many | one | one,few,many,other |

Test with: 0, 1, 2, 5, 21.
</pluralization>

---

### Subagent D: UNUSED KEYS

This is the highest-value check. LLM semantic understanding is the differentiator over regex/AST tools.

**Step 1:** Extract all leaf keys from source locale (JSON dot paths / YAML nesting / PO msgids).

**Step 2:** Search codebase for each key using MULTIPLE patterns:
```bash
rg -l "'key.path'" --glob '!**/node_modules/**' --glob '!**/*.test.*' --glob '!**/dist/**' --glob '!**/messages/**' --glob '!**/locales/**'
rg -l '"key.path"' # same exclusions
```

**Step 3: Handle dynamic keys (CRITICAL -- prevents false positives):**

| Pattern | Implication |
|---------|-------------|
| `` t(`error.${type}`) `` | ALL `error.*` keys potentially used |
| `const k = 'nav.home'; t(k)` | Trace variable to t() call |
| `{ label: 'tab.info' }` -> `t(item.label)` | Trace config object |
| `useTranslations('Foo')` -> `t('bar')` | Key is `Foo.bar` not `bar` |
| `t(cond ? 'a' : 'b')` | Both a and b are used |

Search for dynamic patterns:
```bash
rg -n 't\(`[^`]*\$\{' --glob '**/*.{ts,tsx,js,jsx,vue,svelte}'     # template literals
rg -n 't\(\s*[a-zA-Z_]\w*\s*[,)]' --glob '**/*.{ts,tsx,js,jsx}'   # variable refs
rg -n ":\s*['\"][a-z]+\.[a-z]" --glob '**/*.{ts,tsx,js,jsx}'       # config objects
```

**Step 4: Classify:**
- **UNUSED (HIGH)** -- No direct ref, no dynamic pattern, no variable trace -> safe to remove
- **LIKELY UNUSED (MEDIUM)** -- No direct ref, but namespace has dynamic patterns -> review manually
- **POTENTIALLY UNUSED (LOW)** -- Referenced through variables/config that might be dead code -> investigate

MUST show evidence: "no references found" vs "only in dead code" vs "covered by dynamic pattern `t(\`errors.\${type}\`)`"

---

### Main Thread: TEXT EXPANSION + PUNCTUATION

<expansion-risks>
Flag strings likely to cause layout issues:

| Language | Expansion | Notes |
|----------|-----------|-------|
| DE/RU | +30% (max +50%) | Flag tight layouts |
| FR | +20% (max +40%) | |
| ES/PT | +25% (max +40%) | |
| AR | +25% (max +50%) | + RTL |
| JA | -30% chars | Wider glyphs |
| ZH | -50% chars | Wider glyphs |

Flag strings in: fixed-width containers (buttons, badges, table cells), CSS `text-overflow: ellipsis`, short labels in tight layouts (nav, tabs, form labels).
</expansion-risks>

<punctuation>
Flag hardcoded punctuation that should be inside translated strings:
Quotes: EN `"text"` / JP `「テキスト」` / CN `"文本"`.  Separators: use Intl.ListFormat.  Colons: EN `:` / CJK `：`.  Ellipsis: EN `...` / JP `…` / CN `……`.  Parens: EN `()` / CJK `（）`.
</punctuation>

## OUTPUT FORMAT

```
i18n Review: {target}
========================================
Framework: {detected} | Locale: {format} | Source: {locale} | Targets: [{list}]
Files reviewed: {n} | Wrapped strings: {n}

=== 🔴 CRITICAL ({n}) ===

SPLIT SENTENCES:
  🔴 {file}:{line} -- {pattern} -- Fix: {suggestion}

PLURAL ISSUES:
  🔴 {file}:{line} -- {pattern} -- Fix: {suggestion}
  🔴 {key} -- missing forms for {lang}: needs {forms}

PLACEHOLDER MISMATCHES:
  🔴 {key} -- en has {name}, {locale} missing

=== 🟡 WARNING ({n}) ===

OVER-WRAPPING:
  🟡 {file}:{line} -- t('{key}') wraps "{value}" -- {reason}

UNDER-WRAPPING:
  🟡 {file}:{line} -- "{string}" not wrapped -- {reason}

HARDCODED VALUES:
  🟡 {file}:{line} -- "{value}" in key "{key}" -- use {parameter}

LOCALE QUALITY:
  🟡 Non-translatable keys: {list}
  🟡 Key parity: {locale} missing {n} keys
  🟡 Naming: {examples}

UNUSED KEYS ({n} total):
  HIGH ({n} -- safe to remove):
    {file}: "{key}" -- "{value}" -- {evidence}
  MEDIUM ({n} -- review):
    {file}: "{key}" -- "{value}" -- {evidence}
  Savings: {n} keys -> {n} fewer strings across {n} locales

=== 🔵 INFO ({n}) ===

PUNCTUATION:
  🔵 {file}:{line} -- {pattern} -- {locale concern}

TEXT EXPANSION:
  🔵 {file}:{line} -- "{string}" ({n} chars) in {container} -- {risk}

=== SUMMARY ===
  🔴 Critical: {n}  |  🟡 Warning: {n}  |  🔵 Info: {n}

=== QUICK WINS (easiest high-impact fixes) ===
  1. {fix} -- {impact}
  2. {fix} -- {impact}
  3. {fix} -- {impact}

=== TOP PRIORITIES ===
  1. {most impactful fix}
  2. {second}
  3. {third}
```

## PRINCIPLES
Read-only default. Prioritize by impact (split sentences > missing plurals > over-wrapping). Context matters (consider target languages). No false positives (verify before flagging). Actionable output (file + line + code + fix). The litmus test: if ONE target language differs, it MUST be wrapped.
