---
name: localize-sk
description: "Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Slovak (sk). Slovak is NOT Czech — enforces Slovak-specific vocabulary (súbor not soubor, používateľ not uživatel, zložka/priečinok not složka, nastavenia not nastavení, prehliadač not prohlížeč), 6-case grammar (vocative merged into nominative — unlike Croatian/Russian), 3-gender system with masculine animate/inanimate split, ICU one/few/many/other plurals (1/2-4/fractions/0+5+), standard past participle endings (vybraný not dialectal vybratý), rhythmic law (rytmický zákon — no consecutive long syllables), Slovak diacritics (ľ ĺ ŕ ô ä unique to Slovak), Vy/ty formality (Vy capitalized), impersonal voice for status messages (Počíta sa..., NOT first-person Počítam...), gerundive stiffness avoidance (na organizáciu not na organizovanie), and EUR currency with `1 234,56 €` formatting."
---

# Translate to Slovak (sk) — High-Fidelity Skill

## Scope & Variants

Slovak is a single standard target — Modern Standard Slovak (spisovná slovenčina). No regional split for product UI:

| Locale | Notes |
|--------|-------|
| `sk` / `sk-SK` | Standard Slovak (Slovakia). Default and only target. |

**Practical reality:** Slovak translation has one target. The most important quality concern is **disambiguating from Czech**, which is structurally similar but lexically distinct.

### Slovak vs Czech — distinct West Slavic languages, often confused

Slovak and Czech are mutually intelligible (especially in writing) but they are **separate languages** with distinct vocabulary, distinct alphabets, and distinct grammar in places. AI translators sometimes mix them. Key distinguishing features:

**Slovak has 5 letters Czech doesn't:**

| Slovak | Used for | Czech equivalent |
|--------|----------|-------------------|
| **ľ** | soft L | doesn't exist (Czech uses `l` or `lj` constructions) |
| **ĺ** | long syllabic L | doesn't exist |
| **ŕ** | long syllabic R | doesn't exist |
| **ô** | /u̯o/ diphthong | doesn't exist |
| **ä** | open `a` (rare) | doesn't exist |

**Czech has 3 letters Slovak doesn't:** `ě`, `ř`, `ů`. Any of these appearing in Slovak text means a Czech word leaked in.

**Common Slovak vs Czech vocabulary** (the surface markers a translation must NOT mix):

| English | ✓ Slovak | ✗ Czech (do NOT use in sk) |
|---------|----------|-----------------------------|
| file | súbor | soubor |
| folder | zložka / priečinok | složka |
| user | používateľ | uživatel |
| settings | nastavenia | nastavení |
| browser | prehliadač | prohlížeč |
| computer | počítač | počítač (same) |
| now | teraz | nyní (or teď) |
| where | kde | kde (same) |
| but | ale | ale (same) |
| because | pretože | protože |
| yes | áno | ano (no diacritic) |
| no | nie | ne |
| good | dobrý | dobrý (same) |
| month | mesiac | měsíc (with ě) |
| year | rok | rok (same) |
| Monday | pondelok | pondělí (with ě) |
| Tuesday | utorok | úterý |
| only | len / iba | jen / pouze |
| also | tiež / aj | také / taky |
| can / be able | môcť | moci / moct |
| want | chcieť | chtít |
| see | vidieť | vidět (with ě) |
| do | robiť | dělat (with ě) |
| big | veľký | velký (no ľ — Czech has no soft L) |

**If a Slovak translation contains `soubor`, `uživatel`, `nastavení`, `prohlížeč`, `nyní`, `protože`, `měsíc`, `pondělí`, `dělat`, `vidět`, or any of the letters `ě ř ů`** — IT'S WRONG (Czech leaked in). Fix to the Slovak equivalents.

---

## Register Auto-Detection (Apply Before Translating)

Slovak has a strong T-V distinction (Vy/ty). Auto-detect from source:

| Source signal | Target register |
|---------------|-----------------|
| Casual / conversational / personal (`Hey!`, contractions, emoji, marketing voice, gaming) | **Informal (ty)** — `ty` lowercase, 2nd-person sg. verb endings (`-š`: môžeš, vidíš), familiar imperative (singular: vyber, klikni, otvor). |
| Neutral product UI / docs / consumer software (DEFAULT) | **Formal (Vy)** — `Vy` capitalized for direct address, 2nd-person pl. verb endings (`-te`: môžete, vidíte), polite imperative (`-te/-ite`: vyberte, kliknite, otvorte). Possessive `Váš / Vaša / Vaše` capitalized. |
| Legal / banking / government / enterprise | **Formal (Vy) elevated** — same `Vy` form but full constructions, no contractions, prefer reflexive impersonal (`Vykonáva sa`), native vocabulary over loanwords. |

**Hard rule: never mix levels in one text.** A string with `Môžete zmeniť` (formal verb) and `tvoje nastavenia` (informal possessive) is broken.

**Capitalization rule for Vy:** `Vy / Váš / Vaša / Vaše / Vaši / Vám / Vás` are capitalized in direct second-person address.

**Default for software UI: Vy (formal)** unless brand voice is explicitly youth/casual.

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. Slovak identity — NOT Czech (severity 2.5)

Documented above. Check for Czech letters (`ě ř ů`) and Czech vocabulary in your translation.

### 2. Word integrity — verb prefixes NEVER split (severity 3.0)

Slovak verbs with prefixes are **single words**. Splitting them is a critical error.

| ✗ Wrong (split) | ✓ Correct (joined) |
|-----------------|---------------------|
| `pre vesti` | **`previesť`** (to transfer / translate) |
| `iz vesti` | **`izvesti`** is not even Slovak — but `vyviesť` (to lead out) is ONE word |
| `vy konať` | **`vykonať`** (to execute) |
| `na hrať` | **`nahrať`** (to upload / record) |
| `pre nášať` | **`prenášať`** (to transfer) |
| `od oslať` | **`odoslať`** (to send out) |
| `pri jať` | **`prijať`** (to accept) |
| `roz počať` | **`rozpočítať`** is a different verb; `začať` (to begin) doesn't have a prefix to split |

**Reflexive `sa / si` is SEPARATE clitic** — not attached to verb in writing. `prihlásiť sa`, `registrovať sa`, `zaoberať sa`. Writing `prihlásiťsa` is wrong.

### 3. Standard past participle endings -ný/-ná/-né (severity 2.0)

Slovak uses **standard literary participles** ending in `-ný / -ná / -né` (not dialectal `-tý / -tá / -té`). This is a specific Slovak-internal quality concern.

| ✗ Dialectal / colloquial | ✓ Standard literary |
|--------------------------|---------------------|
| vybratý | **vybraný** |
| vybratá | **vybraná** |
| vybraté | **vybrané** |
| vybratých (gen.pl.) | **vybraných** |
| vybratí (masc.anim.pl.) | **vybraní** |

Same applies to other `vy-` and similar prefixed verbs. Default to the `-ný / -ná / -né` form for written Slovak.

### 4. Rhythmic law (Rytmický zákon) (severity 1.5)

Slovak avoids **two consecutive long syllables** in a single word. When a suffix would create a second long syllable after a long stem, the suffix shortens.

| ✗ Wrong (two long syllables) | ✓ Correct (rhythmic-shortened) |
|------------------------------|-------------------------------|
| **krásný** | **krásny** (the second `ý` shortens to `y` because `á` is already long) |
| **vážný** | **vážny** |
| **múdrý** | **múdry** |
| **gazdovských** (if both were long, would shorten) | (depends on context) |

The rule has exceptions (foreign words, some morphological positions), but the general principle: after a syllable with `á / é / í / ó / ú / ý / ä / ô / ia / ie / iu`, the next syllable's vowel shortens.

**Practical impact in UI:** mostly affects adjective endings and some noun declensions. Words borrowed from English with long vowels (`báza`, `online`) follow modified rules. When in doubt, look up the word in *Krátky slovník slovenského jazyka*.

### 5. Six-case system (NOT seven) (severity 2.5)

Slovak uses **6 cases** — vocative is **merged into nominative** (different from Croatian/Serbian/Ukrainian/Russian which use 7).

| Case | Question | Use | Example (m.anim. "používateľ") | Example (f. "aplikácia") |
|------|----------|-----|-------------------------------|--------------------------|
| Nominatív (NOM) | kto? čo? | Subject (and direct address — no separate vocative) | používateľ | aplikácia |
| Genitív (GEN) | koho? čoho? | Possession, "of", absence, 5+ count | používateľa | aplikácie |
| Datív (DAT) | komu? čomu? | Indirect object, "to" | používateľovi | aplikácii |
| Akuzatív (ACC) | koho? čo? | Direct object | používateľa (animate=GEN) / súbor (inanimate=NOM) | aplikáciu |
| Lokál (LOK) | o kom? o čom? | Location (always w/ prep) | o používateľovi | o aplikácii |
| Inštrumentál (INS) | s kým? čím? | "With", means | s používateľom | s aplikáciou |

**Critical: animate masculine accusative = genitive form.** `vidím používateľa`, NOT `vidím používateľ`.

**Direct address uses nominative**, NOT a separate vocative case (unlike Ukrainian's `Олександре!` or Czech's `Olego!`). For Slovak: `Ahoj, Alexander!` (NOT `Alexandere!`).

### 6. Preposition + governed case (severity 2.5)

| Preposition | Case | Example |
|-------------|------|---------|
| v / vo (in/into) | LOK / ACC | v systéme / do systému |
| na (on/onto) | LOK / ACC | na obrazovke / na obrazovku |
| s / so (with) | INS | s používateľom |
| bez (without) | GEN | bez chýb |
| pre (for) | ACC | pre používateľa |
| od (from) | GEN | od používateľa |
| do (until/to) | GEN | do konca |
| o (about) | LOK | o používateľovi |
| za (per / behind) | ACC / INS | za súbor (per file) / za stolom (behind table) |
| pred (before) | INS | pred uložením |
| po (after) | LOK | po prihlásení |
| medzi (between) | INS / ACC | medzi súbormi |
| k / ku (to/toward) | DAT | k používateľovi |

**"per" in Slovak:** use `za + ACC` for rate (`za súbor`), `na + ACC` for distribution (`na používateľa`), `denne` for "per day".

**Cost expressions:** prefer `pre + ACC` over `za + ACC` for describing costs that apply to a quantity (`cena pre 3 jazyky` = price for 3 languages). `za` is OK for exchange/rate (`za súbor`).

### 7. Verb-governed case (severity 2.0)

| Verb | Governs | Example |
|------|---------|---------|
| pomáhať (help) | **dative** | pomáhať **používateľovi** |
| ďakovať (thank) | dative | ďakujem **Vám** |
| riadiť sa (be guided by) | **instrumental** | riadiť sa **pravidlami** |
| zaoberať sa (deal with) | instrumental | zaoberať sa **systémom** |
| dosiahnuť (achieve) | **genitive OR accusative** | dosiahnuť **výsledok** / **výsledku** |
| zbaviť sa (get rid of) | genitive | zbaviť sa **chyby** |
| potrebovať (need) | accusative | potrebovať **pomoc** |

### 8. Relative pronoun agreement (ktorý / ktorá / ktoré / ktorí) (severity 2.5)

The relative pronoun MUST agree with its antecedent in gender and number:

| Antecedent | Pronoun |
|------------|---------|
| Masc. sg. (`systém`) | **ktorý** |
| Fem. sg. (`aplikácia`) | **ktorá** |
| Neut. sg. (`nastavenie`) | **ktoré** |
| Masc. anim. pl. (`používatelia`) | **ktorí** |
| Other pl. (fem. / neut. / masc. inanim.) | **ktoré** |

### 9. ICU plurals — one / few / many / other (1 / 2-4 / fractions / 0+5+) (severity 2.5)

Slovak's ICU plural categories differ slightly from other Slavic languages:

```icu
{count, plural,
  one {# súbor}
  few {# súbory}
  many {# súboru}
  other {# súborov}
}
```

**CLDR plural category boundaries:**

| Category | Rule | Examples | Noun form |
|----------|------|----------|-----------|
| `one` | n = 1 | 1 | **NOM singular** (súbor) |
| `few` | n ∈ {2, 3, 4} | 2, 3, 4 | **NOM plural** (súbory) |
| `many` | n is a fraction | 2.5, 1.5 | **GEN singular** (súboru) |
| `other` | n = 0 OR n ≥ 5 | 0, 5, 6, 10, 100 | **GEN plural** (súborov) |

**Note vs other Slavic:** Slovak's `many` is for **fractions only** (decimals), not 11-14 like Russian/Ukrainian/Croatian. Slovak uses `other` for everything ≥ 5 and 0.

### 10. Numeral-noun agreement (severity 2.0)

| Count | Pattern | Example |
|-------|---------|---------|
| 1 | NOM sg | 1 súbor |
| 2, 3, 4 | NOM pl (GEN pl for masc. animate) | 2 súbory, 3 systémy; but `2 používatelia` (NOM pl. for masc.anim.) |
| 5+ | GEN pl | 5 súborov, 10 používateľov |
| 0 | GEN pl | 0 súborov |
| Fractions | GEN sg | 2,5 súboru |

### 11. Three-gender adjective agreement with masc. animate/inanimate split (severity 2.0)

Slovak distinguishes **masculine animate** vs **masculine inanimate** (matters for accusative case):

| Gender | Example | Adjective NOM sg. |
|--------|---------|-------------------|
| Masc. animate (humans, named animals) | používateľ, programátor | nový používateľ |
| Masc. inanimate (objects, abstracts) | súbor, systém, počítač | nový súbor |
| Feminine (-a ending) | aplikácia, mapa | nová aplikácia |
| Neuter (-o / -e / -ie ending) | nastavenie, okno | nové nastavenie |

Wrong gender adjective is auto-fail: `nová systém` ✗, `nový aplikácia` ✗, `nová nastavenie` ✗.

### 12. Past-tense gender agreement (severity 1.5)

| Subject | L-participle | Example |
|---------|--------------|---------|
| m. sg. | -l | on pracoval |
| f. sg. | -la | ona pracovala |
| n. sg. | -lo | ono pracovalo |
| m. pl. (anim.) | -li | oni pracovali |
| f. pl. | -li | (modern Slovak uses -li for both m.pl. and f.pl.) |
| n. pl. | -li / -ly | one pracovali |

### 13. Verb-construction integrity — no stacked finite verbs (severity 2.0)

English `-ing` (gerund as adverbial) MUST be rendered with **prechodník** (Slovak's verbal adverb in `-ac/-iac/-úc`) or restructure, NOT a second finite clause. Slovak's prechodník is more archaic/literary than Russian/Ukrainian's equivalent — often better to use `pri + verbal noun`:

| ✗ Stacked finite | ✓ Verbal adverb / pri + noun | English |
|------------------|------------------------------|---------|
| `Strávil som 6 rokov staval som biznis` | **`Strávil som 6 rokov budovaním biznisu`** | I spent 6 years building the business |
| `Pracoval som kým som písal správu` | **`Pracoval som pri písaní správy`** / **`píšuc správu`** (literary) | I worked while writing the report |

### 14. Diacritics — preserve (severity 2.0)

Slovak uses: `á ä č ď é í ĺ ľ ň ó ô ŕ š ť ú ý ž`. Stripping or replacing any (especially `ľ`, `ô`, `ä` which are unique to Slovak) is a critical readability failure.

| ✗ Stripped | ✓ Correct |
|------------|-----------|
| pouzivatel | **používateľ** |
| dalsi | **ďalší** |
| nacitavanie | **načítavanie** |
| platba | **platba** ✓ (no diacritics needed here, just an example) |

---

## Pronouns and Possessives

### Personal pronouns

| English | Slovak | Notes |
|---------|--------|-------|
| I | ja | |
| you (sg. informal) | ty | |
| you (sg./pl. formal — capitalize) | Vy | Always capitalized in direct address |
| you (pl. informal) | vy | lowercase when truly plural informal |
| he | on | |
| she | ona | |
| it | ono | |
| we | my | |
| they (masc.anim.) | oni | |
| they (other) | ony | |

### Possessive pronouns

| Person | m. sg. | f. sg. | n. sg. |
|--------|--------|--------|--------|
| môj (my) | môj | moja | moje |
| tvoj (your sg.) | tvoj | tvoja | tvoje |
| **Váš (your formal — capitalize)** | **Váš** | **Vaša** | **Vaše** |
| jeho (his — invariable) | jeho | jeho | jeho |
| jej (her — invariable) | jej | jej | jej |
| svoj (reflexive — own) | svoj | svoja | svoje |
| náš (our) | náš | naša | naše |
| ich (their — invariable) | ich | ich | ich |

**Reflexive `svoj`** is required when possessor = subject of same clause.

---

## UI Conventions

### Buttons — INFINITIVE or formal imperative (Vy-form)

Slovak platform UIs (Windows SK, Chrome SK, macOS SK) use **infinitive** for buttons OR **Vy-imperative** depending on the brand. Both are acceptable; pick one and stay consistent.

| English | ✓ Infinitive (platform default) | ✓ Vy-imperative (alternative) |
|---------|--------------------------------|-------------------------------|
| Save | **Uložiť** | **Uložte** |
| Cancel | **Zrušiť** / **Storno** | **Zrušte** |
| Delete | **Zmazať** / **Odstrániť** | **Zmažte** / **Odstráňte** |
| Send | **Odoslať** | **Odošlite** |
| Edit | **Upraviť** | **Upravte** |
| Search | **Hľadať** | **Hľadajte** |
| Confirm | **Potvrdiť** | **Potvrďte** |
| Continue | **Pokračovať** | **Pokračujte** |
| Submit | **Odoslať** | **Odošlite** |
| Sign in / Log in | **Prihlásiť sa** | **Prihláste sa** |
| Sign out | **Odhlásiť sa** | **Odhláste sa** |
| Sign up | **Zaregistrovať sa** | **Zaregistrujte sa** |
| Next | **Ďalej** / **Nasledujúce** | (same) |
| Back | **Späť** | (same) |
| Done | **Hotovo** / **Dokončené** | (same) |
| OK | **OK** / **V poriadku** | (same) |
| Close | **Zavrieť** | **Zavrite** |
| Upload | **Nahrať** | **Nahrajte** |
| Download | **Stiahnuť** | **Stiahnite** |
| Refresh | **Obnoviť** | **Obnovte** |
| Settings | **Nastavenia** | (same) |
| Apply | **Použiť** | **Použite** |
| Reset | **Obnoviť pôvodné** / **Resetovať** | — |
| Select all | **Vybrať všetko** | **Vyberte všetko** |
| Add more | **Pridať ďalšie** (NOT `Pridať viac`) | **Pridajte ďalšie** |

### Status messages — three distinct patterns

**Ongoing (in-flight)** → **imperfective reflexive (sa)** or **Prebieha + verbal noun** (NEVER first-person)

| English | ✓ Slovak |
|---------|----------|
| Loading… | **Načítava sa…** / **Prebieha načítavanie…** |
| Saving… | **Ukladá sa…** / **Prebieha ukladanie…** |
| Sending… | **Odosiela sa…** / **Prebieha odosielanie…** |
| Processing… | **Spracováva sa…** / **Prebieha spracovanie…** |
| Connecting… | **Pripája sa…** / **Prebieha pripájanie…** |
| Searching… | **Hľadá sa…** / **Prebieha vyhľadávanie…** |
| Translating… | **Prekladá sa…** / **Prebieha preklad…** |
| Please wait | **Počkajte, prosím** / **Prosím počkajte** |

**Critical impersonal voice rule:** NEVER use first-person (`Počítam…`, `Analyzujem…`, `Spracovávam…`) — sounds awkward. Always impersonal.

**Completed** → **Neuter perfective participle** (impersonal completion)

| English | ✓ Slovak |
|---------|----------|
| Saved | **Uložené** |
| Done | **Hotovo** / **Dokončené** |
| Translation complete | **Preložené** / **Preklad dokončený** |
| File uploaded | **Súbor nahraný** / **Nahraté** |
| Sent | **Odoslané** |
| Payment successful | **Platba úspešná** / **Zaplatené** |

**Failed** → **`Nepodarilo sa` + infinitive** OR **`Chyba` + GEN of verbal noun**

| English | ✓ Slovak |
|---------|----------|
| Save failed | **Nepodarilo sa uložiť** / **Chyba ukladania** |
| Upload failed | **Nepodarilo sa nahrať** / **Chyba nahrávania** |
| Translation failed | **Nepodarilo sa preložiť** / **Chyba prekladu** |
| File not found | **Súbor sa nenašiel** / **Súbor nenájdený** |

NEVER use:
- ✗ `Preklad zlyhal` (too informal/slangy)
- ✗ `Uloženie neúspešné` (calque)

### Empty states — `Žiadne X` / `Nie je vybrané`

| ✗ Verbose / bare | ✓ Concise |
|------------------|-----------|
| Prázdne | **Žiadne výsledky** / **Žiadne nájdené položky** |
| Nič tu | **Žiadne súbory** / **Žiadne dostupné údaje** |
| Bez údajov | **Žiadne dostupné údaje** |

### Drag-and-drop

- drag → **potiahnite** (Vy) / **potiahni** (ty)
- drop → **pustite** (Vy) / **pusti** (ty)
- Combined: **`Potiahnite súbory sem`** (Drag files here).

### File picker — `Vybrať` not `Prehľadávať`

Standard in Chrome SK / Windows SK:

| ✗ Older / navigation | ✓ Modern / action-oriented |
|----------------------|----------------------------|
| Prehľadávať súbory | **Vybrať súbory** |
| Prehľadávať súbor | **Vybrať súbor** |
| kliknite pre prehľadávanie | **kliknite pre výber** |

### Quantity expressions

| ✗ Calque | ✓ Native |
|----------|----------|
| 25+ jazykov | **viac ako 25 jazykov** |
| +{count} viac | **a {count} ďalších** / **ešte {count}** |

`Pridať viac` ✗ → `Pridať ďalšie` ✓ (idiomatic).

### Error messages — what + next step

| ✗ Bare | ✓ With next step |
|--------|------------------|
| Súbor sa nenašiel. | **Súbor sa nenašiel. Skontrolujte cestu.** |
| Chyba siete. | **Chyba siete. Skúste znova.** |
| Neplatný e-mail. | **E-mailová adresa je neplatná. Skontrolujte formát.** |

### UI labels — prefer international standards

| ✗ Over-translated | ✓ International standard |
|-------------------|--------------------------|
| Rada: (advice) | **Tip:** |
| Poznámka: | **Tip:** / **Info:** |

`Tip:` is widely recognized in Slovak software (Windows, macOS, browsers).

### Gerundive stiffness — prefer noun forms

Slovak verbal nouns ending in `-nie/-tie` can sound stiff/bureaucratic. Prefer concrete noun forms or restructured phrases:

| ✗ Gerundive (stiff) | ✓ Noun / alternative (natural) |
|---------------------|--------------------------------|
| na organizovanie | **na organizáciu** |
| pre ukladanie | **na uloženie** |
| k zobrazovaniu | **na zobrazenie** |
| pri nastavovaní | **pri nastavení** |
| po dokončení analyzovania | **po analýze** |

**Exception:** some gerundives are natural for ongoing processes (`nahrávanie`, `sťahovanie` are fine).

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Slovak | Notes |
|------|--------|-------|
| Question mark | `?` | Same as English |
| Comma | `,` | Different conjunction rules |
| Period | `.` | Same |
| Colon | `:` | Same |
| Quotation marks | **`„…"`** primary (low-9 / high-9), **`‚…'`** nested | Slovak typography standard |
| Em-dash | `—` | Used for parenthetical breaks |

### Comma rules

| Rule | Example |
|------|---------|
| **NO comma** before `a` (and) | Vyberte súbor **a** kliknite. |
| **NO comma** before `i` (and, archaic) | — |
| **NO comma** before `alebo / či` (or) | Vyberte súbor **alebo** zložku. |
| **Comma** before `že` (that, subordinating) | Vidím, **že** súbor je otvorený. |
| **Comma** before `ktorý / ktorá / ktoré` (relative) | Súbor, **ktorý** ste vybrali… |
| **Comma** before `aby` (in order to) | Kliknite, **aby** ste pokračovali. |
| **Comma** before `ak` (if) | Uložte, **ak** chcete. |
| **Comma** before `pretože` (because) | Zrušené, **pretože** zlyhalo. |
| **Comma** before `ale` (but) | Rýchlo, **ale** efektívne. |

### Numbers

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **space** | 1 234 567 |
| Decimal separator | **comma (,)** | 3,14 / 99,99 |
| Negative | `-25` | |
| Percent | `25 %` (with space typical) | |

### Dates

| Format | Example | Use |
|--------|---------|-----|
| D. M. YYYY | **15. 1. 2024** | Default — note spaces around periods |
| D. mesiac YYYY | **15. januára 2024** | Long-form prose (month in genitive!) |
| YYYY-MM-DD | 2024-01-15 | Technical/API only |

**Slovak month names (lowercase, declines!):**

| Nominative | Genitive (used in dates) |
|------------|---------------------------|
| január | januára |
| február | februára |
| marec | marca |
| apríl | apríla |
| máj | mája |
| jún | júna |
| júl | júla |
| august | augusta |
| september | septembra |
| október | októbra |
| november | novembra |
| december | decembra |

**Critical: in long-form dates, month is in genitive** — `15. januára 2024`. The digit-only form uses periods with spaces: `15. 1. 2024`.

**Weekdays (lowercase):** pondelok, utorok, streda, štvrtok, piatok, sobota, nedeľa.

Week starts **Monday**.

### Time

- 24-hour preferred: `14:30` or `14.30` (period acceptable as separator).
- 12-hour rarely used.

### Currency — Euro (EUR / €)

| Format | Pattern | Example |
|--------|---------|---------|
| Symbol after amount with space | `€` | **99,99 €** |
| ISO code | EUR | **99,99 EUR** |

Slovakia adopted the euro on 1 January 2009 (currency previously was the Slovak koruna `Sk`).

---

## Terminology — preferred Slovak terms

| English | ✓ Slovak preferred | ✗ Avoid |
|---------|---------------------|---------|
| user | **používateľ** | user, uživatel (Czech) |
| account | účet / konto | accounting |
| password | heslo | password |
| settings | **nastavenia** | setingy, nastavení (Czech) |
| dashboard | hlavný panel / nástenka | dashboard |
| email | e-mail / elektronická pošta | mejl |
| link | odkaz | link |
| website | webová stránka / stránka | website |
| folder | **zložka** / **priečinok** | folder, složka (Czech) |
| file | **súbor** | fajl, soubor (Czech) |
| device | zariadenie | device |
| phone | telefón / mobil | — |
| computer | počítač | komputer |
| application / app | aplikácia | — |
| update (v.) | aktualizovať | apdejtovať |
| save | uložiť | sejvovať |
| delete | zmazať / odstrániť | deletovať |
| upload | **nahrať** | uploadovať |
| download | **stiahnuť** | downloadovať |
| sign in / log in | prihlásiť sa | logovať sa |
| sign up | zaregistrovať sa | — |
| search | hľadať | search |
| click | kliknúť / stlačiť | — |
| share | zdieľať | šerovať |
| profile | profil | — |
| notifications | upozornenia / notifikácie | — |
| privacy | súkromie | — |
| terms | podmienky | — |
| support | podpora | — |
| help | pomoc | — |
| feedback | spätná väzba | — |
| menu | menu / ponuka | — |
| home | domov / domovská stránka | — |
| **browser** | **prehliadač** | browser, prohlížeč (Czech) |
| **detect (v.)** | **rozpoznať** / **zistiť** | detegovať, detektovať |
| **analyze** | analyzovať / rozobrať | — |
| **optimize** | optimalizovať / zlepšiť | — |
| **generate** | vytvoriť / vygenerovať | — |
| **validate** | overiť / skontrolovať | validovať |
| build (software) | vytvoriť / zostaviť | budovať (= construction) |
| deploy | nasadiť / publikovať | deployovať |
| pipeline (CI/CD) | pipeline (keep) | — |
| commit (git) | commit (keep) | — |
| merge (git) | zlúčiť / merge | — |
| repository | repozitár | — |
| sync | synchronizovať | — |
| API | API (keep — Latin always) | — |

### Tech identifiers — keep in Latin script

Inside Slovak text (which uses Latin alphabet anyway), these stay exactly as-is:
- Git, GitHub, GitLab, Docker, npm, pip
- HTTP, REST, GraphQL, OAuth, JWT
- JSON, XML, YAML, CSV, PDF
- Brand names: Google, Microsoft, Apple, iPhone, Android
- Commands, paths, URLs, code snippets
- Placeholders `{variableName}`, `{{count}}`, `<tag>`

---

## False Friends — Critical

| Slovak word | Actually means | NOT this | Correct for the English |
|-------------|----------------|----------|--------------------------|
| **vzrušený** | aroused (sexual) / excited (in tense context) | "excited (looking forward)" | "excited" → **teším sa** / **som nadšený** |
| aktuálny | current / topical | "actual" | "actual" → **skutočný** / **reálny** |
| realizovať | to implement / carry out | "to realize (understand)" | "realize" → **uvedomiť si** |
| eventuálne | possibly / perhaps | "eventually" | "eventually" → **nakoniec** / **napokon** |
| kontrolovať | to check / verify | "to control (manage)" | "control" → **riadiť** / **ovládať** |
| sympatický | likeable / pleasant | "sympathetic (compassionate)" | "sympathetic" → **súcitný** |

---

## Calque / Anti-Pattern List

| ✗ Calque | ✓ Native Slovak | Reason |
|----------|------------------|--------|
| robiť zmysel | **dávať zmysel** / **mať zmysel** | "Makes sense" calque |
| na konci dňa | **nakoniec** / **v konečnom dôsledku** | "At the end of the day" calque |
| vziať miesto | **konať sa** / **uskutočniť sa** | "Take place" calque |
| založený na | **na základe** | "Based on" calque |
| v poriadku, aby | **aby** | "In order to" calque |
| na dennej báze | **denne** / **každý deň** | "On a daily basis" calque |
| v zmysle | **pokiaľ ide o** / **ohľadom** | "In terms of" calque (when overused) |
| **Auto-rozpoznané** | **Automaticky rozpoznané** | "Auto-X" — use full adverb |
| **Auto-uložené** | **Automaticky uložené** | "Auto-X" |
| **Auto-oprava** | **Automatická oprava** | Use full adjective |
| **Auto-dopĺňanie** | **Automatické dopĺňanie** | Use full adjective (neuter) |
| **Preložené výsledky** (header) | **Výsledky prekladu** | English Past-Participle + Noun → Slovak Noun + Genitive of verbal noun |
| **Nahrané súbory** (header) | **Súbory na nahranie** | Same pattern for actionable context |
| **Vybrané možnosti** (header) | **Výber možností** | Use noun form |
| **opcia jazyka** (N + N) | **jazykové možnosti** / **výber jazyka** | Use adj+N or genitive |
| **projekt mapa** | **mapa projektu** / **projektová mapa** | Use genitive or adjective |
| **používateľ nastavenia** | **používateľské nastavenia** / **nastavenia používateľa** | Use adj or genitive |
| **Nulový výpadok** / **Nula chýb** | **Bez výpadkov** / **Bez chýb** | "Zero X" marketing calque |
| **na organizovanie** | **na organizáciu** | Gerundive stiffness |
| **pre ukladanie** | **na uloženie** | Gerundive stiffness |
| **AI-poháňaný** | **založený na AI** / **s využitím AI** | "X-powered" calque |
| **dátovo-orientovaný** | **založený na dátach** / **dátami riadený** | "X-driven" calque |
| **per súbor** | **za súbor** | "per X" calque |
| **per user** | **na používateľa** | "per X" calque |
| **per day** | **denne** / **za deň** | "per X" calque |
| **Preklad zlyhal** | **Nepodarilo sa preložiť** / **Chyba prekladu** | Slangy → impersonal failure |
| **Uloženie neúspešné** | **Nepodarilo sa uložiť** / **Chyba ukladania** | Calque → impersonal |
| **Súbor sa uložil** | **Uložené** / **Súbor uložený** | Reflexive past → impersonal participle |
| **Prekliči vyber všetkého** | **Prekliči vse** / wait, that's Slovenian | (For Slovak: `Zrušiť výber všetkého` → `Zrušiť všetko`) |
| **Pridať viac** | **Pridať ďalšie** | "Add more" — use idiomatic `ďalšie` |
| **Spojené štáty americké** (UI) | **USA** | UI short form |
| **vybratý / vybratá / vybraté** | **vybraný / vybraná / vybrané** | Dialectal → standard literary participle |
| **detegovať** | **rozpoznať** / **zistiť** | Latinized verb → native |
| **validovať** | **overiť** / **skontrolovať** | Latinized verb → native |
| **Rada:** (label) | **Tip:** | International standard preferred |

---

## Self-Check Checklist (Run Before Returning Output)

### Slovak identity (auto-fail on miss)

- [ ] **No Czech letters**: no `ě ř ů` in the text.
- [ ] **No Czech vocabulary**: no `soubor, uživatel, nastavení, prohlížeč, nyní, protože, měsíc, pondělí, dělat, vidět`.
- [ ] **Slovak letters present where required**: `ľ ĺ ŕ ô ä` (e.g., `používateľ`, `ďalší`, `pôvodný`).

### Accuracy

- [ ] **Word integrity** — prefixes joined (`previesť`, `vykonať`, `nahrať`, `prijať`). Reflexive `sa/si` separate (`prihlásiť sa`).
- [ ] **Standard participles** `-ný/-ná/-né`, NOT dialectal `-tý/-tá/-té` (`vybraný` not `vybratý`).
- [ ] **Rhythmic law** — no two consecutive long syllables (`krásny` not `krásný`).
- [ ] **Six-case system** correct (NO vocative — direct address uses nominative).
- [ ] **Animate masc. accusative = genitive** (`vidím používateľa`).
- [ ] **Verb-governed case**: pomáhať+DAT, zaoberať sa+INS, dosiahnuť+GEN/ACC.
- [ ] **Relative pronoun agreement** (ktorý/ktorá/ktoré/ktorí).
- [ ] **Gender agreement** + masc. animate/inanimate distinction.
- [ ] **ICU plurals**: `one / few / many / other` (1 / 2-4 / fractions / 0+5+). Note: `many` is for fractions, NOT 11-14.
- [ ] **Numeral-noun**: 1=NOM.sg, 2-4=NOM.pl, 5+=GEN.pl, fractions=GEN.sg.
- [ ] **Verb aspect** correct.
- [ ] **No stacked finite verbs** from English -ing — use `pri + verbal noun` or prechodník.
- [ ] **Placeholders preserved**.
- [ ] **Latin tech identifiers** intact.
- [ ] **Numbers**: comma decimal (3,14), space thousands (1 234), `€` after amount.
- [ ] **Dates**: `15. 1. 2024` (with spaces!) or `15. januára 2024` (month in genitive).
- [ ] **Time**: 24-hour.
- [ ] **per**: `za + ACC` for rate, `na + ACC` for distribution, `pre + ACC` for cost contexts.

### Register

- [ ] **Vy/ty chosen and applied consistently**.
- [ ] **`Vy/Váš/Vaša/Vaše` capitalized** in direct address.

### UI conventions

- [ ] Buttons use **infinitive** (`Uložiť`, `Zrušiť`) OR Vy-imperative (`Uložte`, `Zrušte`) — pick one per project.
- [ ] Reflexive `sa` present where required (`prihlásiť sa`, `zaregistrovať sa`).
- [ ] Status ongoing: **reflexive `sa`** (`Ukladá sa…`) or `Prebieha + verbal noun` — NEVER first-person (`Počítam…` ✗).
- [ ] Status completed: **neuter perfective participle** (`Uložené`, `Preložené`).
- [ ] Status failed: **`Nepodarilo sa + infinitive`** OR **`Chyba + GEN`**.
- [ ] Empty state: `Žiadne + GEN` or `Nie je vybrané/nájdené`.
- [ ] File picker: `Vybrať`, not `Prehľadávať`.
- [ ] Drag-drop: `Potiahnite` + `Pustite`.
- [ ] Quantity: `viac ako 25`, `ešte {count}`, NOT `25+`, `+{count}`.
- [ ] UI hint label: `Tip:` not `Rada:`.
- [ ] Error messages include next step.

### Naturalness

- [ ] No English calques (`robiť zmysel`, `na konci dňa`, `založený na`, `na dennej báze`, `vziať miesto`).
- [ ] **Past-Participle + Noun headers** → **Noun + Genitive of verbal noun** (`Výsledky prekladu`).
- [ ] **Auto-X prefix** → full adverb (`Automaticky rozpoznané`).
- [ ] **Gerundive stiffness avoided** (`na organizáciu` not `na organizovanie`).
- [ ] **N+N compounds** → adj+N or genitive.
- [ ] **No verbose collocations** (`provést zlepšenie` → `zlepšiť`).
- [ ] **No false friends**: `vzrušený ≠ excited (looking forward)`, `aktuálny ≠ actual`, `realizovať ≠ realize`, `eventuálne ≠ eventually`.
- [ ] **Native verbs over Latinized**: `rozpoznať` not `detegovať`, `overiť` not `validovať`, `vytvoriť` not `generovať`.
- [ ] **Slovak month names in genitive** in date prose (`15. januára 2024`).
- [ ] `„…"` Slovak quotation marks (low-9/high-9).

---

## Worked Example — Standard sk formal UI

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** neutral product UI → **Vy (formal)**, infinitive/imperative buttons.

**Translation:**

> Vitajte späť! Máte 3 nové súbory vo svojom účte. Kliknite na **Pokračovať**, aby ste ich skontrolovali, alebo na **Zrušiť**, aby ste zostali tu. Ukladajú sa Vaše zmeny…

**Why this works:**
- `Vitajte späť` — Vy-form greeting (formal plural participle).
- `Máte` — Vy-form verb.
- `3 nové súbory` — `3` triggers `few` (NOM pl); `súbor` is masc. inanim.; `nové` is masc. inanim. pl. adjective.
- `vo svojom účte` — `v/vo` + LOK; `účte` masc. LOK sg.; `svojom` reflexive possessive.
- Buttons: `Pokračovať`, `Zrušiť` (infinitive).
- `aby ste ich skontrolovali / aby ste zostali` — `aby + past tense (conditional)` construction (correct Slovak — NOT `aby kontrolujete`).
- Status: `Ukladajú sa Vaše zmeny…` — imperfective reflexive (impersonal). `Vaše zmeny` are plural noun, so reflexive verb is plural.
- No comma before `alebo` ✓.
- Comma before `aby` ✓.
- No Czech vocabulary.

---

## Worked Example — Dates and currency

**Source:** Last login: January 15, 2024 at 2:30 PM. Subscription: €99.99/month.

**Translation:**

> Posledné prihlásenie: 15. januára 2024 o 14:30. Predplatné: 99,99 € mesačne.

(Long-form date with month in genitive; `o 14:30` for time; `99,99 €` for euro; `mesačne` is more natural than `pre mesiac`.)

---

## Worked Example — ICU plurals

**Source:**

```icu
You have {count, plural, one {# new message} other {# new messages}}.
```

**Translation (full Slovak four-category expansion):**

```icu
Máte {count, plural,
  one {# novú správu}
  few {# nové správy}
  many {# novej správy}
  other {# nových správ}
}.
```

Notes:
- `one`: `1 novú správu` — ACC sg fem (object of `Máte`).
- `few` (2-4): `2 nové správy` — NOM pl fem.
- `many` (fractions): `2,5 novej správy` — GEN sg fem.
- `other` (5+, 0): `5 nových správ` — GEN pl fem.

---

## Worked Example — Status messages

| State | English | ✓ Slovak |
|-------|---------|----------|
| Ongoing | Saving… | **Ukladá sa…** (NOT `Ukladám…` first-person) |
| Completed | Saved | **Uložené** (NOT `Súbor sa uložil` reflexive past) |
| Failed | Save failed | **Nepodarilo sa uložiť** / **Chyba ukladania** (NOT `Uloženie zlyhalo` slangy or `Uloženie neúspešné` calque) |

---

## When in Doubt

1. **Default to sk, Vy (formal), Slovak identity (NOT Czech), infinitive buttons, standard `-ný` participles.**
2. If you see Czech letters (`ě ř ů`) → **strip and convert** to Slovak forms.
3. If you see Czech vocabulary (`soubor`, `uživatel`, `nastavení`, `prohlížeč`) → **fix to Slovak** (`súbor`, `používateľ`, `nastavenia`, `prehliadač`).
4. If a participle is `vybratý / vybratá / vybraté` → **switch to standard literary** `vybraný / vybraná / vybrané`.
5. If a verb prefix has a space (`pre vesti`) → **join it**: `previesť`.
6. If `sa` is attached to a verb (`prihlásiťsa`) → **separate it**: `prihlásiť sa`.
7. If you used `vzrušený` for "excited" → **fix to `teším sa` / `nadšený`**.
8. If you wrote `Súbor sa uložil` → **use impersonal `Uložené`**.
9. If you wrote `Preklad zlyhal` → **use `Nepodarilo sa preložiť` / `Chyba prekladu`**.
10. If you used first-person status (`Počítam…`) → **switch to impersonal `Počíta sa…` / `Prebieha výpočet…`**.
11. If you used `na organizovanie` / `pre ukladanie` (stiff gerundive) → **switch to noun form** `na organizáciu` / `na uloženie`.
12. If a date is `15. január 2024` → **fix month to genitive**: `15. januára 2024`.
13. If you used `Auto-` prefix → **expand to `Automaticky`**.
14. If a Latinized verb (`detegovať`, `validovať`, `generovať`) feels off → **try native** (`rozpoznať`, `overiť`, `vytvoriť`).
15. If currency is `Sk` → **fix to `€` / `EUR`** (Slovakia adopted euro 2009).
