---
name: localize-bg
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Bulgarian (български / Bǎlgarski) for Bulgaria. Bulgarian is South Slavic, written in Cyrillic, and closest to Macedonian (~70% mutually intelligible) — but it is the ONE Slavic language that LOST its case system entirely (no nominative/genitive/dative/accusative declension on nouns; prepositions + word order do the case work — this is THE defining feature versus Russian, Polish, Czech, Serbian). Other distinctive features: SUFFIXED definite article appended to the noun (момче → момчето, книга → книгата, село → селото — severity 2.5), 3 genders (мъжки masc / женски fem / среден neut) visible via adjective + article suffixes, 4 evidentiality moods in verbs (indicative / renarrative / dubitative / admirative — uniquely Slavic, encodes whether the speaker witnessed the event), ANALYTIC future formed with `ще` + present (ще пиша = I will write, NOT a synthetic future like Russian буду), ICU plurals one/other (case-less, so simpler than Russian's one/few/many/other), Bulgarian Cyrillic alphabet (uses ъ \"ер голям\" heavily; NO Russian ы; NO ё; preserves щ), MASCULINE COUNT FORM after numbers 2+ (два файла NOT два файлове), Вие/ти formality with Вие capitalized when addressing one person formally, perfective/imperfective verb aspect (shared with Slavic but combined with analytic structure), German-style „...\" quotation marks, DD.MM.YYYY dates, 1 234,56 number format (space thousands, comma decimal — European), BGN лв currency with planned EUR adoption on 2026-01-01, NO comma before и/или (and/or) but mandatory comma before че/ако/защото/който (subordinators), Latin-script tech identifiers (Git, API, JSON, URL, npm) preserved inside Cyrillic text, and rejection of anglicisms (юзър, линк, даунлоуд, дашборд → потребител, връзка, сваляне, табло). Bulgarian is NOT Russian and NOT Serbian."
---

# Localize: Bulgarian (bg → български)

Distilled from the production Bulgarian translation rules. Follow these rules verbatim — they are model-agnostic and produce consistent native-quality Bulgarian output for UI, marketing, docs, error messages, blog posts, and email.

## Mindset

> Вие сте изключително взискателен български писател, който мрази неестествените български конструкции, като буквални преводи от английски или неловки формулировки.

Reject literal English calques and word-stacking calques. Bulgarian looks Slavic on the surface (Cyrillic, gender, aspect) but is structurally unique among Slavic languages — it lost cases, gained a postposed article, and built an analytic future and renarrative mood system. Russian-style declension does NOT apply. Serbian-style word order does NOT apply. Bulgarian patterns its own way.

## Scope & Variants

| Variant | Used for | Default? |
|---------|----------|----------|
| **bg / bg-BG** | Standard Bulgarian for Bulgaria (the only official variant) | YES — there is no regional fragmentation comparable to es-ES/es-419 or pt-BR/pt-PT |

There is no `bg-MK` (Macedonia uses Macedonian, a separate standard despite ~70% mutual intelligibility). There is no Latin-script standard for Bulgarian. **Bulgarian is always Cyrillic.**

Transliteration (the official 2009 Bulgarian Transliteration Act maps Cyrillic to Latin: София → Sofia, Пловдив → Plovdiv) exists only for passport/road-sign use — NEVER for translating UI or marketing copy. If asked to render Bulgarian in Latin script, push back; it is wrong.

## Identity Guardrail — Bulgarian is NOT Russian, NOT Serbian, NOT Macedonian

Bulgarian belongs to the **South Slavic** branch with Macedonian, Serbian, Croatian, Slovenian. Closest sibling: **Macedonian (~70% mutually intelligible)**. Despite shared Cyrillic alphabet with Russian, Bulgarian is structurally and lexically distinct.

### Bulgarian vs Russian (DO NOT mix)

| Feature | Russian | **Bulgarian** |
|---------|---------|---------------|
| Case system | 6 cases (nom/gen/dat/acc/instr/prep) — heavy declension | **NONE** (lost entirely — only vestigial vocative remains: Иване!, Боже!) |
| Definite article | None (definiteness from context) | **Suffixed to noun**: момчето, книгата, селото |
| Future tense | Synthetic with `буду` + infinitive (я буду писать) | **Analytic with `ще` + present**: ще пиша |
| Plural categories (ICU) | `one / few / many / other` (4) | **`one / other` (2)** — because case-less |
| Letter ы | Used (мы, ты, был) | **NOT used** — Bulgarian has no ы |
| Letter ё | Used (всё, ёлка) | **NOT used** — Bulgarian has no ё |
| Letter ъ | Hard-sign only (объект, съезд — rare, silent) | **Vowel "er goljam"** — used heavily as full vowel: България, ъгъл, път, въпрос |
| Letter щ | Pronounced [ʂtɕ] in Russian | **Pronounced [ʃt] in Bulgarian**: щастие [shtastie] |
| Renarrative mood | None | **Present** — Той писал писмо (reported, unwitnessed) vs Той пише писмо (witnessed) |
| Word for "I am" | я (nom) + verb | **аз съм** (always with copula) |
| "yes" | да | **да** (same) — BUT Bulgarian famously NODS for NO and SHAKES for YES (cultural, not linguistic) |
| Word for "thank you" | спасибо | **благодаря / мерси** |

### Bulgarian vs Serbian (DO NOT mix)

| Feature | Serbian | **Bulgarian** |
|---------|---------|---------------|
| Case system | 7 cases (full Slavic declension) | **NONE** |
| Script | Cyrillic OR Latin (equal) | **Cyrillic ONLY** |
| Definite article | None | **Suffixed** (момчето) |
| Letter ћ / ђ | Used (ћирилица, ђак) | **NOT used** |
| "the boy" | дечак (no article) | **момчето** |

### Bulgarian vs Macedonian (closest sibling)

- Macedonian uses THREE definite articles (-от proximal, -ов near, -он distal); Bulgarian uses ONE.
- Macedonian: дома (home), Bulgarian: вкъщи
- Macedonian uses ќ and ѓ; Bulgarian uses щ and дж.
- Stress in Macedonian is fixed antepenultimate; Bulgarian stress is mobile.

If user-supplied Bulgarian text contains ы, ё, ћ, ђ, ќ, ѓ, or any suffixed article variant beyond -ът/-ят/-та/-то/-те → flag as wrong language.

## Register — Вие (formal) vs ти (informal)

Default to **Вие** (formal, ALWAYS capitalized when addressing one person: Вие / Ваш / Ваша / Ваше / Ваши / Вам / Вас) for B2B, government, banking, healthcare, enterprise SaaS, and most software UI. Use **ти** only for explicitly consumer-casual contexts (gaming, social, lifestyle, kids, dating).

**NEVER mix Вие/ти within a file.** This is the single most common Bulgarian localization error.

### Capitalization rule (CRITICAL)
- **Вие, Ваш, Ваша, Ваше, Ваши, Вам, Вас** — ALL capitalized when addressing ONE person formally (politeness convention identical to Russian Вы).
- **вие** lowercase = "you all" (plural, addressing multiple people, no formality marker).
- **ти, твой, твоя, твое, твои** — always lowercase.

| Wrong | Correct | Why |
|-------|---------|-----|
| `можете да промените настройките + Кликни тук` | **`Можете да промените настройките. Кликнете тук.`** | Mixed formal verb + informal imperative |
| `Качете своите файлове + Прегледай файловете` | **`Качете Вашите файлове` + `Прегледайте файловете`** | Mixed possessive + imperative formality |
| `Въведете вашия имейл` (lowercase вашия in formal) | **`Въведете Вашия имейл`** | Formal Вашия must be capitalized |
| `Изпратете ни Вашите въпроси` (in informal context) | **`Изпратете ни своите въпроси`** or switch entire text to ти | Don't mix |

### Register auto-detection (run before translating)

If user has NOT specified Вие or ти, infer from source:

**Formal source signals → output Вие**
- Hedging modals: "please", "kindly", "we recommend", "could you"
- Passive / impersonal: "users are advised", "it is recommended"
- No contractions: "do not", "cannot", "we will"
- Domains: legal, financial, healthcare, regulatory, enterprise B2B, government, banking, insurance
- Third-person distance: "the user must"
- Brand voice: bank, B2B SaaS, healthcare, legal tech
- No exclamations or emojis

**Informal source signals → output ти**
- Contractions: "don't", "you'll", "it's"
- Casual greetings: "hey", "hi there", "yo", "hi 👋"
- Emoji (🎉 😎 🚀 ✨), exclamations, slang
- Consumer apps: gaming, social, lifestyle, dating, fitness, kids

**Ambiguous → default to Вие.** Bulgarian B2B reads ти as disrespectful.

### Verb endings by register

| Concept | Formal (Вие) | Informal (ти) |
|---------|--------------|----------------|
| 2nd person sg present | можете, кликнете, променете (-те ending) | можеш, кликнеш, промениш (-ш ending) |
| Imperative | Натиснете, Изберете, Въведете (-ете/-ите) | Натисни, Избери, Въведи (no -те) |
| Possessive | Ваш / Ваша / Ваше / Ваши (capitalized) | твой / твоя / твое / твои |

## Critical Hard Rules

These are the highest-severity rules — they produce immediately-detectable unnaturalness if violated.

### A. NO grammatical cases — analytic restructuring (severity 3.0 — defining feature)

Bulgarian is **the only Slavic language that lost its case system.** Where Russian uses 6 case endings, Bulgarian uses **prepositions + suffixed article + word order**.

| Russian (with case) | **Bulgarian (no case)** | English |
|---------------------|--------------------------|---------|
| книга пользователя (gen.sg) | **книгата на потребителя** | the user's book |
| с пользователем (instr.sg) | **с потребителя** | with the user |
| без файла (gen.sg) | **без файла** (looks like gen but is JUST `без` + base noun + article) | without the file |
| в системе (prep.sg) | **в системата** | in the system |
| о файле (prep.sg) | **за файла** | about the file |
| помогать пользователю (dat.sg) | **помагам на потребителя** | help the user |
| на сервер (acc) / на сервере (prep) | **на сървъра** (same form for both motion and location) | on/to the server |

**RULE**: Never decline Bulgarian nouns. Possession = `на` + noun (на потребителя = of the user). Direction/location = `в / на / към / от / за` + noun. Means = `с / чрез` + noun.

Only vestigial form: **vocative** — direct address. `Иване!` (Ivan!), `Боже!` (God!), `братко!` (brother!), `майко!` (mother!). Used in fixed expressions and emotional appeals. **Do NOT use vocative in UI** — it sounds dramatic. Use base form: `Иван, моля...`.

| Wrong | Correct | Why |
|-------|---------|-----|
| `на системата данни` | **`данните на системата`** | Bulgarian uses NOUN + на + NOUN, not stacked nouns |
| `проект папка` (Russian/English style) | **`папка на проекта` / `проектна папка`** | Use `на` + noun OR adjective form |
| `потребител настройки` | **`настройки на потребителя` / `потребителски настройки`** | No noun-stacking |
| `с новия потребителя` (declining for instrumental) | **`с новия потребител`** | No instrumental case — `с` + base form |

### B. Suffixed definite article (severity 2.5 — uniquely Bulgarian)

Bulgarian articles **attach to the END** of the noun (or first adjective of a noun phrase). There are five forms:

| Gender / number | Article suffix | Example |
|-----------------|---------------|---------|
| Masculine SUBJECT (nominative position) | **-ът / -ят** | файл**ът**, потребител**ят**, ден**ят** |
| Masculine OBJECT (any other position) | **-а / -я** | файл**а**, потребител**я**, ден**я** |
| Feminine | **-та** | книга**та**, систем**ата**, страница**та** |
| Neuter | **-то** | момче**то**, село**то**, приложение**то** |
| Plural (all genders) | **-те** (or **-та** for neuter -е/-о plurals) | файлове**те**, книги**те**, момчета**та** |

**The masculine subject/object distinction (full vs short article)** is unique to Bulgarian and one of the hardest rules even for natives.

- Use **-ът / -ят** when the noun is the SUBJECT of the sentence (i.e., performs the action).
- Use **-а / -я** EVERYWHERE ELSE (after preposition, as direct object, as predicate).

| Wrong | Correct | Why |
|-------|---------|-----|
| `файла е качен` | **`файлът е качен`** | Subject → -ът |
| `Отворете файлът` | **`Отворете файла`** | Object of отворете → -а |
| `Запазете файлът` | **`Запазете файла`** | Object → -а |
| `Файлът е свален в папка` | **`Файлът е свален в папката`** | Feminine takes -та always |
| `новия файл е` (subject) | **`новият файл е`** | Article attaches to adjective; subject form -ят |
| `отворете новият файл` (object) | **`отворете новия файл`** | Object position → -я (short) |
| `отворете приложениято` | **`отворете приложението`** | Neuter takes -то NOT -ято |
| `книгита` | **`книгата`** | Feminine = -та |

### C. Gender agreement — 3 genders (severity 2.5)

Bulgarian has 3 genders, determined by noun ending:
- **Masculine (мъжки)**: ends in CONSONANT (стол, компютър, файл, потребител, сървър, проект, документ, имейл)
- **Feminine (женски)**: ends in **-а / -я** (система, програма, папка, страница, връзка, грешка, версия, настройка)
- **Neuter (среден)**: ends in **-о / -е** (приложение, съобщение, име, поле, число, устройство, уведомление, разрешение)

### Adjective agreement table

| Gender | Indefinite | Definite (subj if masc) | Definite (obj if masc) | Plural |
|--------|-----------|-------------------------|-----------------------|--------|
| Masc | нов | новият | новия | — |
| Fem | нова | новата | новата | — |
| Neut | ново | новото | новото | — |
| Plural | нови | новите | новите | новите |

| Wrong | Correct | Why |
|-------|---------|-----|
| `нова компютър` | **`нов компютър`** | компютър masculine |
| `нов система` | **`нова система`** | система feminine |
| `нова приложение` | **`ново приложение`** | приложение neuter |
| `бърз връзка` | **`бърза връзка`** | връзка feminine |
| `голям база данни` | **`голяма база данни`** | база feminine |
| `невалидна файл` | **`невалиден файл`** | файл masculine |
| `важен приложение` | **`важно приложение`** | приложение neuter |
| `загубена контекст` | **`загубен контекст`** | контекст masculine |
| `несъответстващо терминология` | **`несъответстваща терминология`** | терминология feminine |

### D. Past participle gender agreement (severity 2.0)

Past participles MUST agree with subject in gender:
- Masculine: **-л** (влязъл, качил, преведен — short form)
- Feminine: **-ла** (влязла, качила, преведена)
- Neuter: **-ло** (влязло, качило, преведено)
- Plural: **-ли** (влезли, качили, преведени)

| Wrong | Correct |
|-------|---------|
| `тя е влязъл` | **`тя е влязла`** |
| `то е влязъл` | **`то е влязло`** |
| `файлът е качена` (masc subject) | **`файлът е качен`** |
| `системата е готов` (fem subject) | **`системата е готова`** |
| `приложението е завършен` (neut subject) | **`приложението е завършено`** |
| `файловете е готов` (plural) | **`файловете са готови`** |

For UI strings where gender is unknown, use **neuter perfective participle** as impersonal: `Запазено`, `Заредено`, `Изтрито`, `Преведено`.

### E. Count form — masculine after numbers (severity 2.0)

Masculine nouns take a special **count form** after numbers (2+). Feminine and neuter nouns use normal plural.

| Wrong | Correct | Why |
|-------|---------|-----|
| `два файлове` | **`два файла`** | Masc count form after 2-4 |
| `три файлове` | **`три файла`** | Count form after 2-4 |
| `пет файлове` | **`пет файла`** | Count form ALSO after 5+ in Bulgarian (unlike Russian which uses gen.pl) |
| `два компютъра` | **`два компютъра`** | Correct count form |
| `три потребителя` | **`трима потребители`** | PEOPLE use the special **counting numeral form** for males: двама, трима, четирима, петима, шестима + normal plural |
| `пет момчета` | **`пет момчета`** | Neuter normal plural |
| `две системи` | **`две системи`** | Feminine normal plural |

**Counting humans (males or mixed):** use special numeral forms — двама, трима, четирима, петима, шестима, седмина, осмина — plus NORMAL plural (NOT count form).
- двама потребители (NOT двама потребителя)
- трима администратори

### F. ICU plurals — `one / other` ONLY (severity 2.0)

Bulgarian uses only TWO ICU plural categories (unlike Russian's four). Because Bulgarian lost cases, the count form difference (2-4 vs 5+) does NOT show up in ICU.

```icu
{count, plural,
  one {# файл}            // 1 — singular base
  other {# файла}}        // 0, 2, 3, 4, 5, 22, 100 — count form (for masculine)
```

| Wrong | Correct |
|-------|---------|
| `{count, plural, one {# файл} few {# файла} many {# файлове} other {# файла}}` (Russian-style 4 categories) | **`{count, plural, one {# файл} other {# файла}}`** |
| `{count, plural, one {# файл} other {# файлове}}` (no count form) | **`{count, plural, one {# файл} other {# файла}}`** |
| `{count, plural, one {# минута} other {# минути}}` | (correct — feminine, normal plural) |
| `{count, plural, one {# съобщение} other {# съобщения}}` | (correct — neuter, normal plural) |

Patterns by gender:

```icu
// Masculine (uses count form in `other`):
{n, plural, one {# файл} other {# файла}}
{n, plural, one {# потребител} other {# потребители}}    // -ел/-ер/-ор take normal plural in count too
{n, plural, one {# документ} other {# документа}}
{n, plural, one {# проект} other {# проекта}}

// Feminine (normal plural in `other`):
{n, plural, one {# минута} other {# минути}}
{n, plural, one {# секунда} other {# секунди}}
{n, plural, one {# страница} other {# страници}}
{n, plural, one {# грешка} other {# грешки}}

// Neuter (normal plural in `other`):
{n, plural, one {# съобщение} other {# съобщения}}
{n, plural, one {# приложение} other {# приложения}}
{n, plural, one {# устройство} other {# устройства}}
```

### G. Future tense — analytic `ще` + present (severity 2.0)

Bulgarian forms the future **analytically** by placing the invariant particle **`ще`** before the present-tense verb. There is no synthetic future like Russian буду.

| English | Wrong | Correct |
|---------|-------|---------|
| I will write | `пиша ще` / `буду писать` (Russian) | **`ще пиша`** |
| You (formal) will receive a confirmation | `ще получите потвърждение` | (correct) |
| We will save the file | `сме запазим файла` | **`ще запазим файла`** |
| The file will be saved | `ще бъде запазено` | (correct — passive future) |
| It will not work | `ще не работи` | **`няма да работи`** (negation uses `няма да` + present) |

**Negative future:** `няма да` + present (NOT `не ще` — archaic). `Няма да работи. Няма да отворя файла.`

### H. Verb aspect — perfective vs imperfective (severity 2.0)

Like other Slavic languages, every Bulgarian verb pair encodes whether action is **completed (perfective)** or **ongoing/repeated (imperfective)**.

| Aspect | Use for | UI examples |
|--------|---------|-------------|
| **Perfective** | Single completed action, buttons, result-focused | запазя, изтрия, отворя, кача, сваля, преведа, изпратя |
| **Imperfective** | Ongoing, in-progress, repeated, status spinners | запазвам / запазване, изтривам, отварям, качвам / качване |

**Buttons → imperative perfective (singular or plural depending on register).**
**Status (ongoing) → verbal noun (-не) OR reflexive imperfective (се + 3sg).**
**Completion (done) → neuter perfective participle.**
**Failure → "Неуспешно/Неуспешен" + noun OR "Грешка при" + verbal noun.**

| Wrong | Correct | Why |
|-------|---------|-----|
| `Заредено...` (as spinner) | **`Зареждане...`** | Perfective = completed; for ongoing use verbal noun |
| `Запазено...` (as spinner) | **`Запазване...`** | Verbal noun for ongoing |
| `Файлът е зареден` (as spinner) | **`Файлът се зарежда...`** | Reflexive imperfective for ongoing |
| `Преводът завърши` (as confirmation) | **`Преводът е завършен`** / **`Преведено`** | Perfective participle |
| `Файлът се запази` (as confirmation) | **`Файлът е запазен`** / **`Запазено`** | Perfective participle |
| `Преводът се провали` (failure) | **`Неуспешен превод`** / **`Грешка при превода`** | Standard error pattern |
| `Зареждането се провали` | **`Неуспешно зареждане`** / **`Грешка при зареждането`** | Same pattern |

### I. Word integrity — never split verb prefixes (severity 3.0)

Bulgarian verb prefixes (по-, пре-, из-, на-, до-, под-, у-, въз-, раз-) are part of the verb. NEVER split.

| Wrong (split) | Correct (joined) |
|---------------|-------------------|
| `по строя` | **`построя`** |
| `пре веда` | **`преведа`** |
| `из пълня` | **`изпълня`** |
| `до бавя` | **`добавя`** |
| `на тисна` | **`натисна`** |
| `у даля` | **`удаля`** |

Exception: `не` (negation) stays separate from verbs (`не запазих, не работи`) but attaches to adjectives/participles (`невалиден, неактивен, неуспешен, незавършен`).

## UI Conventions

### Buttons — imperative (matches register)

For Bulgarian, **buttons use IMPERATIVE form** (not infinitive like Russian). This applies to buttons, tab labels, navigation items, and ALL clickable elements.

| Action | Formal (Вие) | Informal (ти) |
|--------|--------------|----------------|
| Save | **Запазете** / **Запази** (also acceptable: verbal noun `Запазване`) | **Запази** |
| Delete | **Изтрийте** / **Изтрий** | **Изтрий** |
| Open | **Отворете** / **Отвори** | **Отвори** |
| Close | **Затворете** | **Затвори** |
| Cancel | **Отмени** / **Отмяна** | **Отмени** |
| Submit | **Изпратете** | **Изпрати** |
| Log in | **Вход** / **Влезте** | **Влез** |
| Log out | **Изход** / **Излезте** | **Излез** |
| Create | **Създайте** / **Създай** | **Създай** |
| Continue | **Продължете** / **Продължи** | **Продължи** |

Verbal noun (Запазване, Изтриване, Качване) is acceptable as an alternative to imperative — common for menu items.

| Wrong | Correct |
|-------|---------|
| `Да запазиш` (subjunctive/infinitive) | **`Запази` / `Запазване`** |
| `Натискане` (action noun used as button) | **`Натисни` / `Натиснете`** |
| `Качване на файлове` (as tab inviting action) | **`Качете файлове`** |

### Status messages — verbal noun + ellipsis (ongoing)

| Wrong | Correct | Why |
|-------|---------|-----|
| `Заредено...` (ongoing) | **`Зареждане...`** | Verbal noun for ongoing |
| `Запазено...` (ongoing) | **`Запазване...`** | Verbal noun for ongoing |
| `Преведено...` (ongoing) | **`Превеждане...`** | Verbal noun |
| `Файлът е зареден` (as spinner) | **`Файлът се зарежда...`** | Reflexive imperfective |
| `Изчислявам...` (first-person) | **`Изчисляване...`** / **`Изчислява се...`** | Impersonal, NEVER 1st person |

### Completion messages — neuter perfective participle

| Wrong | Correct |
|-------|---------|
| `Плащането успя` (past tense narrative) | **`Плащането е успешно`** / **`Платено`** |
| `Зареждането завърши` | **`Заредено`** / **`Зареждането е завършено`** |
| `Файлът се запази` | **`Файлът е запазен`** / **`Запазено`** |
| `Превода е готово` (gender mismatch) | **`Преводът е готов`** (masc) / **`Преведено`** (impersonal) |
| `Ваши файлове са успешно качени!` (verbose) | **`Файловете са качени`** / **`Качено`** |

Drop verbose "успешно" — completion implies success. Drop exclamation marks unless source clearly warrants them.

### Failure messages — "Неуспешно/Неуспешен" + noun OR "Грешка при" + verbal noun

| Wrong | Correct |
|-------|---------|
| `Преводът се провали` | **`Неуспешен превод`** / **`Грешка при превода`** |
| `Зареждането се провали` | **`Неуспешно зареждане`** / **`Грешка при зареждането`** |
| `Запазването не успя` | **`Неуспешно запазване`** / **`Грешка при запазването`** |
| `Качването фейлд` (anglicism) | **`Неуспешно качване`** |

Pattern: `Неуспешно/Неуспешен/Неуспешна` + gender-agreeing noun, OR `Грешка при` + verbal noun in definite form.

### Empty state messages — "Няма X" with gender agreement

| Wrong | Correct |
|-------|---------|
| `Празно` (bare) | **`Няма резултати`** / **`Няма намерени елементи`** |
| `Нищо тук` (vague) | **`Няма файлове`** / **`Няма налични данни`** |
| `Без данни` (bare) | **`Няма налични данни`** |
| `Списъкът е празно` (gender mismatch) | **`Списъкът е празен`** (masc adj) |
| `Няма намерен файлове` (number mismatch) | **`Няма намерени файлове`** (plural participle) |

Pattern: **`Няма`** + (optional past participle) + noun. The verb `няма` is invariant for negation of existence.

### Drag and drop — Bulgarian-native verbs

| English | Bulgarian | Notes |
|---------|-----------|-------|
| drag | **плъзнете** (formal) / **плъзни** (informal) | NOT `дръгнете` (anglicism) |
| drop | **пуснете** (formal) / **пусни** (informal) | NOT `освободете` (= liberate) |
| release | **пуснете** | Same verb |
| drag-and-drop | **плъзнете и пуснете** | Unified phrase |
| browse files (picker) | **изберете файлове** | NOT `прегледайте/разгледайте файлове` |

| Wrong | Correct |
|-------|---------|
| `Дръгнете файловете` (anglicism) | **`Плъзнете файловете`** |
| `Освободете тук` (= liberate here) | **`Пуснете тук`** |
| `Прегледайте файлове` (= preview/view) | **`Изберете файлове`** |
| `Разгледайте файлове` (= browse-look-around) | **`Изберете файлове`** |
| `кликнете за преглед` (file picker context) | **`кликнете за избор`** |

### Other UI patterns

| Wrong | Correct | Why |
|-------|---------|-----|
| `пер файл` (per file) | **`за файл`** / **`на файл`** | Bulgarian preposition |
| `25+ езика` | **`повече от 25 езика`** | Quantity expression |
| `+{count} повече` | **`и {count} други`** / **`още {count}`** | Bulgarian "N more" |
| `Добави повече` (literal "more") | **`Добави още`** | Idiom: още = more (incremental) |
| `Покажи повече` | **`Покажи още`** | Same idiom |
| `Файлът не е намерен.` (bare) | **`Файлът не е намерен. Проверете пътя.`** | Errors should include next steps |
| `Алтернативно` (bare adjective as menu) | **`Алтернативно разпознаване`** | Complete noun phrase |
| `Автоматично` (bare) | **`Автоматичен режим`** | Complete noun phrase |
| `Преференция за език` (calque) | **`Предпочитан език`** / **`Избор на език`** | Idiomatic |

### Validation messages — distinct verb moods

| Type | Mood | Example |
|------|------|---------|
| Field validation | indicative | `Това поле е задължително` / `Невалиден формат` |
| Action instruction | imperative | `Въведете валидна стойност` / `Изберете поне един език` |
| State description | impersonal | `Не може да се свърже` / `Възникна грешка` |

Drop calques: `Полето отсъства` (calque of "field missing") → `Това поле е задължително`.

## Punctuation, Numbers, Dates, Currency

| Item | Bulgarian |
|------|-----------|
| Decimal separator | **`,`** (comma) |
| Thousands separator | **` `** (space, ideally NBSP) |
| Example number | **`1 234,56`** |
| Currency (current) | **`1 234,56 лв.`** (Bulgarian lev, BGN) — amount + space + лв. |
| Currency (from 2026-01-01) | **`1 234,56 €`** — Bulgaria adopts euro on 2026-01-01 (currently in dual-display transition period) |
| Date | **`15.01.2024`** (DD.MM.YYYY, period separators) or **`15 януари 2024 г.`** (with `г.` = "of the year") |
| Time | **`14:30 часа`** or just **`14:30`** (24-hour, no AM/PM) |
| Primary quotation marks | **`„text"`** (German-style, low-9 opening + curly-right closing) |
| Nested quotation marks | **`«text»`** or **`'text'`** |
| Em-dash | **`—`** with spaces — used in copular sentences |
| Ellipsis | **`…`** (single character preferred) |

### Currency transition note (2026)

Bulgaria adopted the euro on **2026-01-01**. As of today, copy may still reference BGN (лв.) for legacy contracts, but new product copy should default to **€**. For dual-display during transition: `99,99 лв. (≈ 51,13 €)`. After 2026-01-01, prefer EUR only.

| Wrong | Correct |
|-------|---------|
| `"кнопка"` (English quotes) | **`„бутон"`** |
| `«кнопка»` (Russian-style chevrons) | **`„бутон"`** (Bulgarian uses German-style) |
| `1,234.56` (US format) | **`1 234,56`** |
| `01/15/2024` | **`15.01.2024`** |
| `2:30 PM` | **`14:30`** |
| `$99` | **`99,99 лв.`** (pre-2026) / **`99,99 €`** (post-2026) |

### Em-dash in copular sentences

Bulgarian uses `—` (with spaces) where English uses "is", especially in definitional / equational sentences:

| Bulgarian | English |
|-----------|---------|
| София — столицата на България. | Sofia is the capital of Bulgaria. |
| Това — нашият приоритет. | This is our priority. |
| OneSky — платформа за превод. | OneSky is a translation platform. |

In ordinary copular sentences, the verb **съм/е/са** appears (Bulgarian, unlike Russian, REQUIRES copula in present tense): `Файлът е готов. Системата е активна.`

## Comma Rules — differ from English

| Before | Comma? |
|--------|--------|
| **и / или / нито** (coordinating) | **NO comma** |
| **но / а / обаче / ала** (contrasting) | **Comma required** |
| **че / който / която / което / където / когато / ако / защото / тъй като** (subordinating) | **Comma required ALWAYS** |
| **за да** (in order to) | **Comma required** |
| Parenthetical phrases (например, обаче, освен това) | **Surround with commas** |

| Wrong | Correct | Why |
|-------|---------|-----|
| `Изберете файл, или папка` | **`Изберете файл или папка`** | No comma before или |
| `Запазете, и затворете` | **`Запазете и затворете`** | No comma before и |
| `Плъзнете тук, или кликнете` | **`Плъзнете тук или кликнете`** | No comma before или |
| `Виждам че файлът е отворен` | **`Виждам, че файлът е отворен`** | Comma required before че |
| `Файлът който избрахте` | **`Файлът, който избрахте`** | Comma required before който |
| `Кликнете тук ако искате да продължите` | **`Кликнете тук, ако искате да продължите`** | Comma required before ако |
| `Кликнете за да продължите` | **`Кликнете, за да продължите`** | Comma required before за да |
| `Не кликнете а плъзнете` | **`Не кликнете, а плъзнете`** | Comma required before а (contrasting) |
| `Това е просто но ефективно` | **`Това е просто, но ефективно`** | Comma required before но |

## Terminology

### Native vs loanword — prefer Bulgarian

| Anglicism (avoid) | Bulgarian native |
|--------------------|-------------------|
| юзър | **потребител** |
| линк | **връзка** |
| даунлоуд | **сваляне** / **изтегляне** |
| ъплоуд | **качване** |
| сетинги | **настройки** |
| дашборд | **табло** / **контролен панел** |
| фийдбек | **обратна връзка** / **отзив** |
| таргет | **цел** |
| репорт | **доклад** / **отчет** |
| чекване (verb anglicism) | **проверка** / **проверявам** |
| делитване | **изтриване** |
| мерджване | **сливане** / **обединяване** |
| ъпдейтване | **актуализиране** / **обновяване** |
| ънинсталиране (anglicism) | **деинсталиране** |

### Established loanwords (accepted)

These are normalized in modern Bulgarian and acceptable in any register:
- **браузър** (browser)
- **файл** (file)
- **сървър** (server)
- **сайт** (website)
- **акаунт** (account) — though `регистрация` / `потребителски профил` is more formal
- **чат** (chat)
- **интерфейс** (interface)
- **имейл** (email) — though `електронна поща` is the formal Bulgarian
- **компютър** (computer)
- **онлайн** / **офлайн**
- **софтуер** / **хардуер**

### Preferred UI terms (standardized)

| English | Bulgarian preferred |
|---------|----------------------|
| click | **натиснете** (preferred) / **кликнете** (acceptable) |
| settings | **настройки** |
| dashboard | **табло** / **контролен панел** |
| user | **потребител** |
| delete | **изтрий** / **изтриване** |
| save | **запази** / **запазване** |
| upload | **качване** |
| download | **сваляне** / **изтегляне** |
| log in | **вход** / **влизане** |
| log out | **изход** / **излизане** |
| file | **файл** |
| folder | **папка** |
| search | **търсене** |
| send | **изпращане** / **изпрати** |
| receive | **получаване** / **получи** |
| password | **парола** |
| username | **потребителско име** |
| confirm | **потвърди** / **потвърждение** |

### Gender of common IT nouns (memorize)

| Masculine (он) | Feminine (тя) | Neuter (то) |
|----------------|----------------|--------------|
| **файл** | **система** | **приложение** |
| **сайт** | **папка** | **съобщение** |
| **сървър** | **страница** | **име** |
| **браузър** | **връзка** | **поле** |
| **компютър** | **версия** | **устройство** |
| **потребител** | **програма** | **уведомление** |
| **документ** | **настройка** | **разрешение** |
| **проект** | **грешка** | **число** |
| **акаунт** | **парола** | **значение** |
| **сервиз** | **подписка** | **състояние** |
| **отчет** | **операция** | **завършване** |
| **доклад** | **корзина** (rare; → кошница) | **запазване** |
| **запис** | **функция** | **зареждане** |
| **резултат** | **мрежа** | **изтриване** |
| **имейл** | **база (данни)** | **търсене** |

### Acronym gender

| Acronym | Expansion | Gender |
|---------|-----------|--------|
| **ИИ** | Изкуствен интелект | masculine |
| **API** | (foreign) | masculine |
| **URL** | (foreign) | masculine |
| **PDF** | (foreign) | masculine |
| **САЩ** | Съединени американски щати | masc plural (treated plural) |
| **ЕС** | Европейски съюз | masculine |
| **ООН** | Организация на обединените нации | feminine |
| **БНБ** | Българска народна банка | feminine |

### Technical identifiers — KEEP LATIN (critical)

Technical identifiers, API names, code, framework names MUST stay in Latin script even inside Cyrillic text. NEVER transliterate.

| Wrong (transliterated) | Correct |
|------------------------|---------|
| `Гит хранилище` | **`Git хранилище`** |
| `АПИ ключ` | **`API ключ`** |
| `ДЖЕЙСЪН формат` | **`JSON формат`** |
| `УРЛ адрес` | **`URL адрес`** |
| `нпм пакет` | **`npm пакет`** |
| `НоудДжес` | **`Node.js`** |
| `Реакт компонент` | **`React компонент`** |

**Always keep Latin:** Git, GitHub, GitLab, npm, Node.js, React, Vue, Angular, Next.js, Docker, Kubernetes, API, URL, HTTP, HTTPS, JSON, XML, CSS, HTML, SQL, OAuth, JWT, REST, GraphQL, WebSocket, IDE, CLI, GUI, MVP, SaaS, PaaS, IaaS, SDK, SLA, KPI, CRM, ERP.

## Calque / Anti-Pattern Blocklist

### Word-for-word calques

| Wrong (literal English) | Correct (idiomatic Bulgarian) |
|--------------------------|-------------------------------|
| `направи смисъл` (makes sense) | **`има смисъл`** / **`логично е`** |
| `в края на деня` (at the end of the day) | **`в крайна сметка`** / **`накрая`** |
| `вземи място` (take place) | **`проведе се`** / **`състоя се`** |
| `базиран на` (based on) | **`на основата на`** / **`въз основа на`** |
| `в ред да` (in order to) | **`за да`** |
| `на дневна основа` (on a daily basis) | **`ежедневно`** / **`всеки ден`** |
| `на седмична основа` | **`ежеседмично`** / **`всяка седмица`** |
| `по отношение на` (in terms of, overused) | **`относно`** / **`за`** |
| `аз съм развълнуван` (I'm excited — `развълнуван` has sexual connotation) | **`очаквам с нетърпение`** / **`радвам се на`** |
| `Файлът не може да бъде намерен` (passive calque) | **`Файлът не е намерен`** |
| `Получете преведено за минути` ("Get X done") | **`Превод за минути`** / **`Преведете за минути`** |
| `Дръжте проектите си синхронизирани` | **`Поддържайте синхронизация на проектите`** |
| `Направете работния си процес по-бърз` | **`Ускорете работния си процес`** |
| `направи подобрение` | **`подобри`** |
| `осъществя избор` | **`избера`** |

### False friends

| Bulgarian word | Actually means | NOT the English |
|----------------|----------------|-----------------|
| **актуален** | current / relevant / topical | NOT "actual" — use **действителен** for "actual" |
| **реализирам** | to implement / accomplish | NOT "realize (understand)" — use **осъзнавам** |
| **развълнуван** | aroused (often sexual connotation) | NOT "excited (eager)" — use **в очакване** / **с нетърпение** |
| **симпатия** | liking / fondness | NOT "sympathy (condolence)" — use **съчувствие** |
| **фабрика** | factory (manufacturing) | NOT "fabric" — use **плат** |
| **магазин** | store / shop | NOT "magazine" — use **списание** |
| **резюме** | CV / summary | for verb "resume", use **продължи** |
| **акуратен** | neat / careful | NOT "accurate" — use **точен** |
| **репетиция** | rehearsal | NOT "repetition" — use **повторение** |
| **прогресивен** | progressive (political) | for "gradual" use **постепенен** |
| **симулирам** | simulate / fake | for software, **моделирам** is more precise |

### Header participle calques

English UI headers often use "Past Participle + Noun" pattern (e.g., "Translated Results"). This is a calque trap — Bulgarian prefers "Noun + preposition + verbal noun".

| English | Calque (WRONG) | Natural Bulgarian (CORRECT) |
|---------|----------------|------------------------------|
| Translated Results | Преведени резултати | **Резултати от превода** |
| Updated Settings | Актуализирани настройки | **Настройки за актуализация** / **Промени в настройките** |
| Imported Files | Импортирани файлове | **Файлове за импорт** / **Импортирано** |
| Deleted Items | Изтрити елементи | **Елементи за изтриване** / **Изтрито** |
| Downloaded Reports | Свалени отчети | **Свалени отчети** (this works) / **Отчети за сваляне** (better for "to-be-downloaded") |

### Abbreviated prefix calques

English uses `Auto-X` abbreviated prefixes. Bulgarian should use FULL adverb/adjective forms.

| Wrong | Correct |
|-------|---------|
| `Авто-разпознато` / `Авто-детектирано` | **`Автоматично разпознато`** |
| `Авто-запазено` | **`Автоматично запазено`** |
| `Авто-корекция` | **`Автоматична корекция`** |
| `Авто-попълване` | **`Автоматично попълване`** |
| `Авто-генерирано` | **`Автоматично генерирано`** / **`Автоматично създадено`** |

### Compound adjective calques

| English pattern | Wrong (calque) | Correct (Bulgarian) |
|-----------------|----------------|---------------------|
| AI-powered | `ИИ-задвижван` / `ИИ-управляван` | **`на базата на ИИ`** / **`с използване на ИИ`** / **`интелигентен`** |
| user-friendly | `потребителско-приятелски` | **`лесен за използване`** / **`удобен`** / **`интуитивен`** |
| cloud-based | `облачно-базиран` | **`в облака`** / **`облачен`** / **`базиран в облака`** |
| context-aware | `контекстно-осъзнат` | **`отчитащ контекста`** / **`контекстуален`** |
| data-driven | `данни-управляван` | **`основан на данни`** / **`базиран на данни`** |

### Structural calques

| Wrong (English subject-first passive) | Correct (Bulgarian verb-first / impersonal) |
|--------------------------------------|---------------------------------------------|
| `[Subject] е необходим за [Purpose]` | **`Необходим е [Subject] за [Purpose]`** / **`Нужен е [Subject]`** |
| `Сесия е изтекла` | **`Сесията изтече`** / **`Изтекла сесия`** |

### Marketing "Zero X" calques

| Wrong | Correct |
|-------|---------|
| `Нулево време на престой` | **`Без престой`** / **`Непрекъсната работа`** |
| `Нулеви грешки` | **`Без грешки`** / **`Никакви грешки`** |
| `Нулеви обвързвания` | **`Без ангажименти`** |
| `Нулева поддръжка` | **`Не изисква поддръжка`** |

### Proper-noun calques

| Wrong (in UI) | Correct |
|---------------|---------|
| `Съединените американски щати` | **`САЩ`** |
| `Обединеното кралство на Великобритания и Северна Ирландия` | **`Великобритания`** / **`Обединеното кралство`** |
| `Федерална република Германия` | **`Германия`** |

### Idiom calques

| Wrong (literal) | Natural Bulgarian |
|-----------------|-------------------|
| Break a leg (literal) | **Успех!** / **На добър час!** |
| Piece of cake (literal) | **Лесно като фасул** / **Детска игра** |
| It's raining cats and dogs | **Вали като из ведро** |
| At the end of the day | **В крайна сметка** / **Накрая** |
| Hit the nail on the head | **Удари точно в десятката** |

### Word-sense disambiguation (polysemy)

| English (context) | Wrong (first dictionary meaning) | Correct (contextual) |
|--------------------|-----------------------------------|------------------------|
| bank (river) | **банка** (= financial) | **бряг** |
| light (weight) | **светлина** (= illumination) | **лек** |
| current (electric) | **текущ** (= present) | **ток** |
| run (execute) | **бягам** (= physical) | **изпълни** / **стартирай** |
| save (file) | **спаси** (= rescue) | **запази** |
| save (rescue) | **запази** (= preserve file) | **спаси** |
| copy (marketing text) | **копие** (= duplicate) | **текст** / **рекламен текст** |
| bug (software) | **буболечка** (= insect) | **грешка** / **бъг** |
| scale (zoom) | **везни** (= weighing) | **мащаб** / **мащабиране** |
| architecture (software) | **архитектура (на сграда)** | **архитектура (на системата/софтуера)** |
| pipeline (CI/CD) | **тръбопровод** (= plumbing) | **пайплайн** / **поток** |

## Self-Check Checklist (run before finalizing)

### Critical accuracy (must all pass)
- [ ] **NO grammatical case declensions** on nouns (Bulgarian is case-less — use prepositions instead)
- [ ] **Suffixed definite article** correct: -ът/-ят (masc subj), -а/-я (masc obj), -та (fem), -то (neut), -те (pl)
- [ ] **Masculine subject vs object article** distinction (файлът е качен / отворете файла)
- [ ] **Gender agreement** correct on adjectives (нов файл / нова система / ново приложение)
- [ ] **Past participle gender agreement** (влязъл / влязла / влязло / влезли)
- [ ] **Count form** after numbers for masculine (два файла, NOT два файлове) — also пет файла, NOT пет файлове
- [ ] **Human counting numerals** (двама, трима, четирима, петима) for males + normal plural
- [ ] **ICU plurals**: `one / other` ONLY (Bulgarian uses 2 categories, NOT Russian's 4)
- [ ] **Future tense**: `ще` + present (NOT синтетичен with буду); negative future `няма да` + present
- [ ] **Verb aspect** correct (perfective for completed, imperfective for ongoing)
- [ ] **Вие/ти consistent** throughout (Вие always capitalized; matched possessives + imperatives)
- [ ] **Word integrity** — no split prefixes (`построя` NOT `по строя`)
- [ ] **Copula `е/съм/са` present** in copular sentences (Файлът е готов, NOT *Файлът готов)
- [ ] **Technical identifiers stay Latin** (`Git`, `API`, `JSON`, `npm`, `Node.js` — never transliterated)
- [ ] All `{variables}` and ICU intact
- [ ] **Domain terminology** uses IT meaning (architecture=software, pipeline=CI/CD, bug=software defect)

### Naturalness
- [ ] **Buttons in imperative** matching register (Запазете formal, Запази informal) — verbal noun acceptable (Запазване)
- [ ] **Status (ongoing)** uses verbal noun + ellipsis (`Зареждане...`, `Запазване...`) — NEVER perfective
- [ ] **Completion** uses neuter perfective participle (`Запазено`, `Преведено`) or `е + participle` (`Файлът е запазен`)
- [ ] **Failure** uses `Неуспешно/Неуспешен` + noun OR `Грешка при` + verbal noun
- [ ] **Empty state** uses `Няма X` (NOT bare `Празно` or `Без данни`)
- [ ] **Drag-drop verbs** correct (`плъзнете / пуснете`, NOT `дръгнете / освободете`)
- [ ] **File picker** uses `Изберете` (NOT `Прегледайте` / `Разгледайте`)
- [ ] **`„text"` German-style quotes** — NOT English `"..."` or Russian `«...»`
- [ ] **Em-dash** with spaces for copular sentences (София — столицата)
- [ ] **Comma rules**: comma before `че/който/ако/защото/за да`; NO comma before `и/или`
- [ ] **No verbed anglicisms** (`изтрий` NOT `делитни`; `провери` NOT `чекни`; `актуализирай` NOT `ъпдейтни`)
- [ ] **Native preferred over loan** for non-established (`потребител` NOT `юзър`; `връзка` NOT `линк`; `сваляне` NOT `даунлоуд`)
- [ ] **No noun-stacking calques** (`папка на проекта` NOT `проект папка`)
- [ ] **No hyphenated `Авто-X`** — use full `Автоматично` / `Автоматичен` / `Автоматична`
- [ ] **No header participle calques** (`Резултати от превода` NOT `Преведени резултати`)
- [ ] **Marketing zero**: `Без X` (NOT `Нулево X`)
- [ ] **Compound adjectives natural** (`лесен за използване`, `на базата на ИИ`)
- [ ] **No false friends** in wrong sense (актуален ≠ actual, реализирам ≠ realize, развълнуван has sexual connotation)
- [ ] **Currency**: pre-2026 `99,99 лв.`, post-2026 `99,99 €`; **date** `15.01.2024`; **numbers** `1 234,56`
- [ ] **Quantity**: `повече от 25 езика` not `25+ езика`; `още {count}` not `+{count} повече`
- [ ] **Idiom button** "more": `Добави още` / `Покажи още` (NOT `Добави повече`)

## Worked Examples

### Example 1 — File upload welcome (formal)

**Source (en):** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

**Bulgarian (Вие, formal):**

Добре дошли! Моля, изберете Вашия файл за качване. Поддържаме повече от 25 формата и го превеждаме на 5 езика за {seconds} {seconds, plural, one {секунда} other {секунди}}. Не се притеснявайте — можете да отмените операцията по всяко време.

**Errors this catches:**
- `25+ формата` → `повече от 25 формата` (Bulgarian quantity)
- `за 5 езика` (calque "for") → `на 5 езика` (translating INTO languages takes `на`)
- `{seconds} секунди` without ICU → `{seconds, plural, one {секунда} other {секунди}}`
- `Не се вълнувайте` (sounds erotic) → `Не се притеснявайте`
- `Кенселирайте` (anglicism) → `отменете`

### Example 2 — Button labels (formal)

| English | Bulgarian (formal) |
|---------|---------------------|
| Save | Запазете / Запазване |
| Delete | Изтрийте / Изтриване |
| Cancel | Отмяна / Отменете |
| Submit | Изпратете |
| Continue | Продължете |
| Log out | Изход / Излезте |
| Create new file | Създайте нов файл |
| Upload files | Качете файлове |

### Example 3 — Status messages

| English | Bulgarian |
|---------|-----------|
| Loading... | **Зареждане...** (NOT `Заредено...`) |
| Saving... | **Запазване...** |
| Translating... | **Превеждане...** |
| Uploading file... | **Файлът се качва...** / **Качване на файла...** |
| File saved | **Файлът е запазен** / **Запазено** |
| Translation complete | **Преводът е завършен** / **Преведено** |
| Upload failed | **Неуспешно качване** / **Грешка при качването** |
| No results | **Няма резултати** |
| No files yet | **Все още няма файлове** |
| No data available | **Няма налични данни** |

### Example 4 — ICU plural for masculine

```icu
You have {count, plural,
  one {# unread message}
  other {# unread messages}
}.
```

**Bulgarian (неуter `съобщение`):**

```icu
Имате {count, plural,
  one {# непрочетено съобщение}
  other {# непрочетени съобщения}
}.
```

### Example 5 — ICU plural for masculine with count form

```icu
{count, plural,
  one {# file}
  other {# files}
}
```

**Bulgarian (мъжки `файл` — count form in `other`):**

```icu
{count, plural,
  one {# файл}
  other {# файла}
}
```

NOT `# файлове` — masculine takes count form after numbers (2+ → `файла`, NOT `файлове`).

### Example 6 — Email confirmation (formal)

**Source (en):** "Hi! Your translation order has been processed. We'll send you the result within 24 hours. If you have any questions, feel free to contact our support team."

**Bulgarian (formal):**

Здравейте! Поръчката Ви за превод е обработена. Ще Ви изпратим резултата в рамките на 24 часа. Ако имате въпроси, можете да се свържете с екипа ни за поддръжка.

**Errors this catches:**
- `Здрасти!` (informal) → `Здравейте!` (matches formal register of business email)
- `Е обработена твоята поръчка` (mixed register) → `Поръчката Ви е обработена` (Ви capitalized)
- `ще изпратим резултата за 24 часа` (calque "for") → `в рамките на 24 часа` (idiomatic time-frame)
- `чувствайте се свободни да...` (calque "feel free") → `можете да се свържете` (direct)

### Example 7 — Error message with next steps

**Source:** "File not found."

**Wrong (bare):** Файлът не е намерен.
**Correct:** **Файлът не е намерен. Проверете пътя или опитайте отново.**

Error messages should include WHAT happened AND WHAT TO DO.

### Example 8 — Marketing headline

**Source:** "Translate 32 file formats with zero downtime."

**Wrong:** Преведете 32 файлови формата с нулево време на престой.
**Correct:** **Преведете 32 файлови формата без престой.**

(`Без X` over `Нулево X` marketing calque.)

### Example 9 — Subordinate clause with comma

**Source:** "Click here if you want to continue."

**Wrong:** Кликнете тук ако искате да продължите.
**Correct:** **Кликнете тук, ако искате да продължите.**

(Mandatory comma before `ако`.)

### Example 10 — Drag and drop UI

**Source:** "Drag and drop your files here, or click to browse."

**Wrong:** Дръгнете и освободете Вашите файлове тук, или кликнете за разглеждане.
**Correct:** **Плъзнете и пуснете Вашите файлове тук или кликнете за избор.**

- `дръгнете` (anglicism) → `плъзнете`
- `освободете` (= liberate) → `пуснете`
- comma before или removed
- `разглеждане` (= sightseeing) → `избор` (for file picker)

### Example 11 — Future tense and negation

**Source:** "We will save your changes. The file will not be lost."

**Wrong:** Ние сме запазим Вашите промени. Файлът ще не бъде загубен.
**Correct:** **Ще запазим Вашите промени. Файлът няма да бъде загубен.**

- `ще` + present, NOT `сме` + present
- negative future = `няма да` + present, NOT `ще не` + present

### Example 12 — Suffixed article on adjective

**Source:** "The new file is uploaded."

**Wrong:** Новия файл е качен.
**Wrong:** Нов файла е качен.
**Correct:** **Новият файл е качен.** (subject position → -ят on adjective)

Compare with object: "Open the new file" → **Отворете новия файл** (object → short -я).

## When in Doubt

1. **If unsure about formality → use Вие.** Bulgarian B2B and most software UI defaults to Вие. Ти reads as disrespectful in any professional context.
2. **If unsure about article** (full -ът vs short -а) → ask: is this noun the SUBJECT (performing the verb)? If yes → -ът. Otherwise → -а.
3. **If unsure about count form** → check noun gender. Masculine after 2+ → count form (-а, NOT -ове). Feminine + neuter → normal plural.
4. **If unsure about case** → don't decline. Bulgarian has no cases. Use a preposition (на, в, с, за, от, при) + base noun form.
5. **If unsure about an anglicism** → use the Bulgarian native. Bulgarian language purism is moderate (browser → браузър is fine), but verb anglicisms (`делитни, чекни, ъпдейтни`) are rejected.
6. **If unsure about a participle agreement** → use neuter impersonal (`Запазено`, `Преведено`, `Изтрито`) — works in any UI context.
7. **If unsure about currency** → use лв. for pre-2026 contexts, € for post-2026. Bulgaria adopted the euro on 2026-01-01.
8. **If unsure about quote style** → `„text"` German-style. NEVER Russian `«...»` or English `"..."`.
9. **If you see ы, ё, ћ, ђ, ќ, or ѓ in supposed-Bulgarian source** → flag it; it is wrong language (Russian, Serbian, or Macedonian).
10. **If asked to render Bulgarian in Latin script** → push back. Bulgarian is Cyrillic-only. The 2009 transliteration standard exists for passports and road signs, not for UI/marketing.
