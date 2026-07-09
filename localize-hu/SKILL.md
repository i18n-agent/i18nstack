---
name: localize-hu
description: Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Hungarian (Magyar) for Hungary. Hungarian is a Finno-Ugric (NOT Indo-European) agglutinative language with NO grammatical gender, 18 cases as suffixes, strict vowel harmony (front e/é/i/ö/ő/ü/ű vs back a/á/o/ó/u/ú), definite vs indefinite verb conjugation (mentjük a fájlt vs mentünk egy fájlt — the single hardest Hungarian feature), Ön/te formality (Ön = 3rd-person verb, NOT 2nd-person like Sie/du), separable verbal prefixes (meg-/el-/le-/fel-/be-/ki- that move with negation: Ne mentse el), focus-position word order (the word BEFORE the verb is emphasized), SINGULAR noun after numbers (öt fájl NOT öt fájlok — even in ICU other branch), adjective loanword adaptation (global → globális, digital → digitális — MANDATORY), native verb preference (kattintani not klikkelni, letölteni not downloadolni), Hungarian quotes „...", YYYY. MM. DD. dates with periods, Forint currency (1 234 Ft, NO decimals, NOT in eurozone), NOUN-form buttons (Mentés, Törlés — UNIQUE among languages, not infinitive), and the rejection of suffixes-on-placeholders ({name}-nak → restructure to "A következő felhasználónak: {name}").
---

# Localize: Hungarian (hu → Magyar)

You are translating source text into Hungarian for Hungary. This skill captures grammar, register, UI conventions, formatting, and Hungarian-specific failure modes derived from a production translation prompt.

## Scope & Variants

**One standard:**
- **hu-HU** — Hungarian as used in Hungary. Official language of Hungary and a recognized minority language in Slovakia, Romania, Serbia, Ukraine, Austria, Slovenia, and Croatia.

No widely-distinguished variants in software localization. Hungarian outside Hungary (Transylvania, Vojvodina) uses the same standard, possibly with some lexical differences not relevant to UI.

**Native name:** Magyar nyelv (the language); magyarul (the adverb "in Hungarian"). Use "magyar" for the language in UI.

**Identity guardrail:**
- Hungarian is **Finno-Ugric (Uralic), NOT Indo-European**. Closest living relatives are Khanty and Mansi (both in Russia). Among modern European languages, only Finnish and Estonian are distant cousins.
- Do NOT translate Hungarian by analogy with Slavic, Germanic, or Romance languages. Hungarian:
  - Has NO grammatical gender
  - Uses **suffixes** (not separate words) for cases, possession, plurals, and even articles in compound contexts
  - **Singular noun after numbers** (unlike all neighboring Indo-European languages)
  - Definite/indefinite verb conjugation (a feature shared only with some Uralic languages)
- Hungarian is **NOT Finnish**. Same family, but unintelligible to each other and developed independently for 4000+ years.

## Register

**Default level: FORMAL (Ön-form)** for software UI, errors, documentation, marketing. Like German Sie/du.

| | Ön (formal) | Te (informal) |
|---|---|---|
| Pronoun | Ön | te |
| Verb form | **3rd person singular** (Ön ment, Ön kattint) | 2nd person singular (te mentsz, te kattintasz) |
| Imperative | Mentse, Kattintson | Mentsd, Kattints |
| Possessive | az Ön + noun | suffix on noun (-d, -od, -ad, -ed) |

**The critical insight:** Hungarian formal Ön uses **3rd-person verbs** (like Spanish usted, but unlike German Sie). Mixing them is severity 2.5.

**Examples:**
- ❌ Ön mentsz (2nd person verb with Ön) → ✅ Ön ment
- ❌ Az Ön fiókja + Kattints ide (Ön possessive + te imperative) → ✅ Az Ön fiókja. Kattintson ide.
- ❌ Töltse fel az Ön fájljait + Töltsd fel a fájljaidat (mixed)

`Maga` is a third formality level (semi-formal) — can sound condescending in some contexts. Avoid in UI unless explicitly required.

**Within a file, ONE register only.** Mixing Ön and te in possessives, verbs, or imperatives is always wrong.

## Critical Hard Rules

### Vowel Harmony (severity 2.0)

**Every suffix in Hungarian must match the vowel type of the stem.** This is non-negotiable.

| Stem vowels | Type | Suffix form |
|---|---|---|
| **Back** (a, á, o, ó, u, ú) | back | -ban, -ba, -ról, -nak, -hoz |
| **Front unrounded** (e, é, i, í) | front | -ben, -be, -ről, -nek, -hez |
| **Front rounded** (ö, ő, ü, ű) | front-rounded | -ben, -be, -ről, -nek, -höz |

Examples:
- ❌ rendszer**ban** → ✅ rendszer**ben** (rendszer is front)
- ❌ fájl**ben** → ✅ fájl**ban** (fájl is back)
- ❌ tükör**ban** → ✅ tükör**ben** (tükör is front-rounded)
- ❌ ház**ben** → ✅ ház**ban** (ház is back)

Some stems mix vowels — they default based on the LAST vowel or follow established convention. Look up unfamiliar words.

### Definite vs Indefinite Verb Conjugation (severity 2.5 — THE hardest Hungarian rule)

Hungarian verbs have **two parallel conjugation paradigms** depending on the definiteness of the direct object. This is rare across world languages and absent from English entirely.

| Object type | Conjugation | Example |
|---|---|---|
| Definite (a/az + noun, proper noun, pronoun) | **definite** | Mentjük **a** fájlt (we save THE file) |
| Indefinite (egy + noun, no article, bare quantifier) | **indefinite** | Mentünk **egy** fájlt (we save A file) |
| No object | indefinite | Mentünk (we save) |

**Personal endings differ:**

| Person | Indefinite | Definite |
|---|---|---|
| én (I) | -ok/-ek/-ök | -om/-em/-öm |
| te (you sg) | -sz | -od/-ed/-öd |
| ő/Ön | -∅ (bare stem) | -ja/-i |
| mi (we) | -unk/-ünk | -juk/-jük |
| ti (you pl) | -tok/-tek/-tök | -játok/-itek |
| ők (they) | -nak/-nek | -ják/-ik |

Examples:
- ❌ Mentünk a fájlt (indefinite verb + definite object) → ✅ **Mentjük** a fájlt
- ❌ Mentjük egy fájlt (definite verb + indefinite object) → ✅ **Mentünk** egy fájlt

When in doubt: definite article `a/az` before the object = use definite conjugation. `egy` (a/an) or no article = use indefinite. Pronouns (azt, ezt) and proper nouns trigger definite.

### Suffixes Attach Directly (severity 1.5)

Hungarian suffixes attach to the stem with NO spaces and NO hyphens.

- ❌ fájl-ban → ✅ **fájlban**
- ❌ fájl ban → ✅ **fájlban**
- ❌ a fájl-ról → ✅ **a fájlról**

**Placeholders are the trap.** `{name}-nak` is wrong because:
1. Hyphen before the suffix is incorrect Hungarian punctuation
2. The suffix depends on the placeholder's vowels, which you don't know at translation time

**Restructure to avoid suffixes on placeholders:**
- ❌ "{name}-nak küldve" (case on placeholder)
- ✅ "**A következő felhasználónak: {name}**" (suffix on a known word, placeholder follows)
- ✅ "**Címzett: {name}**" (label-style, no suffix)

### Singular Noun After Numbers (severity 2.0)

**Hungarian numbers take a SINGULAR noun**, unlike English and most other languages. This includes ICU plural `other`.

- ❌ öt fájl**ok** (five files-plural) → ✅ **öt fájl** (five file-singular)
- ❌ három felhasználó**k** → ✅ **három felhasználó**
- ❌ sok fájl**ok** → ✅ **sok fájl** (sok = many)
- ❌ 25 nyelv**ek** → ✅ **25 nyelv**

ICU pattern (Hungarian has only `one` and `other`, both SINGULAR):
```icu
{count, plural,
  one {# fájl}
  other {# fájl}
}
```

Plural forms `fájlok / felhasználók / nyelvek` are used ONLY when the quantity is non-numeric (collective) — e.g., "A fájlok elérhetők" (the files are available). NEVER after a number.

### Verbal Prefixes (Igekötő) (severity 1.5)

Hungarian verbs often have separable prefixes that change meaning:

| Prefix | Meaning | Example |
|---|---|---|
| meg- | completion/perfectivity | megment (save fully) |
| el- | away from | elmegy (go away), elment (saved) |
| le- | down | letölt (download) |
| fel- | up | feltölt (upload), feléleszt (revive) |
| be- | in | bejelentkezik (log in) |
| ki- | out | kijelentkezik (log out), kinyit (open) |
| át- | through, across | átküld (forward) |
| vissza- | back | visszavon (revert), visszaad (return) |

**Prefix position rules:**

| Construction | Position | Example |
|---|---|---|
| Affirmative statement | prefix + verb | "Elmentem a fájlt" / "Bejelentkezett" |
| **Negation** | verb + prefix (SEPARATED) | "Ne mentse **el**!" / "Nem jelentkezett **be**" |
| Yes/no question | prefix + verb (often) | "Elmentette?" / "Bejelentkezett?" |
| Focus on another word | verb + prefix | "A FÁJLT mentem el" (it's the file I saved) |

- ❌ Nem **el**ment a fájl (prefix before negated verb) → ✅ Nem ment **el** a fájl
- ❌ Ne **el**mentse → ✅ Ne mentse **el**
- ❌ Meg nem ment → ✅ Nem ment **meg**

### 18-Case Suffix System (severity 2.0)

Hungarian has 18 cases, all marked by suffixes (which obey vowel harmony). The most common in UI:

| Suffix | Case | Meaning | Example |
|---|---|---|---|
| -∅ (no suffix) | nominative | subject | a fájl |
| -t | accusative | direct object | a fájl**t** |
| -nak/-nek | dative | to/for whom | a felhasználó**nak** |
| -ban/-ben | inessive | **in** (location) | a fájl**ban** |
| -ba/-be | illative | **into** (motion) | a fájl**ba** |
| -ból/-ből | elative | **out of** | a fájl**ból** |
| -ra/-re | sublative | **onto** | a képernyő**re** |
| -on/-en/-ön | superessive | **on** (location) | a képernyő**n** |
| -ról/-ről | delative | about / off | a fájl**ról** |
| -nál/-nél | adessive | at (location) | a felhasználó**nál** |
| -hoz/-hez/-höz | allative | toward | a felhasználó**hoz** |
| -tól/-től | ablative | away from | a rendszer**től** |
| -val/-vel | instrumental | with | a fájl**lal** (consonant doubles) |
| -ként | essive-modal | as/like (rate) | nyelv**enként** (per language) |

**The location/motion contrast is critical:**
- ❌ fájl**ban** (when meaning "into the file") → ✅ fájl**ba**
- ❌ rendszer**ből** (when meaning "into the system") → ✅ rendszer**be**
- ❌ fájl**ról** (when meaning "at the file") → ✅ fájl**nál**

### Verb-Governed Case (severity 2.0)

Specific verbs require specific case suffixes for their complements:

| Verb | Required case | Example |
|---|---|---|
| segít (help) | dative -nak/-nek | segít a felhasználó**nak** ❌ segít a felhasználó**t** |
| bízik (trust) | inessive -ban/-ben | bízik a rendszer**ben** ❌ bízik a rendszer**t** |
| függ (depend) | ablative -tól/-től | függ a beállítások**tól** ❌ függ a beállítások**nak** |
| gondoskodik (take care) | delative -ról/-ről | gondoskodik a biztonság**ról** ❌ gondoskodik a biztonság |
| keres (search) | accusative -t | keres**i** a fájl**t** |
| emlékszik (remember) | sublative -ra/-re | emlékszik a felhasználó**ra** |

### Existential Sentences Need a Predicate (severity 1.5)

Hungarian noun phrases cannot stand alone as complete sentences — they need an existential verb `van` (is/exists) or `található` (located).

- ❌ "A csapatodban # meglévő névtér" (just a noun phrase) → ✅ "A csapatodban # meglévő névtér **van**"
- ❌ "# elem a listában" → ✅ "# elem **van** a listában" / "A listában # elem **található**"
- ❌ "Nincs hiba" (this IS fine — `nincs` is the negative existential)

### Adjective Loanword Adaptation (severity 1.5 — CRITICAL for adjectives)

**Hungarian systematically adapts English adjectives** with characteristic suffixes (-ális, -ikus, -iv). Using the raw English form when an adapted form exists is a quality failure.

| English | Wrong (raw) | Correct (adapted) |
|---|---|---|
| global | global | **globális** |
| digital | digital | **digitális** |
| special | special | **speciális** |
| professional | professional | **professzionális** |
| normal | normal | **normális** |
| optimal | optimal | **optimális** |
| critical | critical | **kritikus** |
| analytical | analytical | **analitikus** |
| active | active | **aktív** |
| effective | effective | **effektív** |
| creative | creative | **kreatív** |

**Pattern recognition:** English -al / -ic / -ive → Hungarian -ális / -ikus / -ív (plus vowel harmony adjustments).

Raw English adjectives are tolerated ONLY when no Hungarian-adapted form exists (e.g., proprietary tech terms).

### Native Verb Preference (severity 1.5)

Hungarian rejects most -ol/-olni anglicism verbs in favor of native Hungarian equivalents:

| Wrong (anglicism) | Correct (native) | Meaning |
|---|---|---|
| klikkelni | **kattintani** | to click |
| downloadolni / daunlódolni | **letölteni** | to download |
| uploadolni / ápplódolni | **feltölteni** | to upload |
| szelektálni | **kiválasztani** | to select |
| deletálni | **törölni** | to delete |
| editálni | **szerkeszteni** | to edit |
| login-olni | **bejelentkezni** | to log in |
| save-olni | **menteni** | to save |

(Compare: noun loanwords like `email`, `online`, `wifi` are fully accepted because they have no native equivalent.)

## UI Conventions

### Button Labels — NOUN FORM (UNIQUE to Hungarian)

Hungarian buttons use the **deverbal noun** (action noun), NOT the infinitive or imperative. This is the opposite of most European languages.

| Wrong (infinitive) | Wrong (informal imperative) | Correct (noun) |
|---|---|---|
| Menteni | Mented | **Mentés** (Save) |
| Törölni | Töröld | **Törlés** (Delete) |
| Mégse-mondani | Mondd vissza | **Mégse** (Cancel) |
| Feltölteni | Töltsd fel | **Feltöltés** (Upload) |
| Letölteni | Töltsd le | **Letöltés** (Download) |
| Kiválasztani | Válaszd ki | **Kiválasztás** (Select) |
| Szerkeszteni | Szerkeszd | **Szerkesztés** (Edit) |
| Bejelentkezni | Jelentkezz be | **Bejelentkezés** (Log in) |

(Formal imperative `Mentse / Töröljön` is acceptable in some contexts — confirmation dialogs, system messages — but `Mentés` is the default in most UIs.)

### Status Messages — NOUN + Ellipsis

```
✅ Mentés...         (Saving...)
✅ Betöltés...       (Loading...)
✅ Feldolgozás...    (Processing...)
✅ Mentés folyamatban...  (Saving in progress...)
❌ Mentve (past participle "saved")
❌ Ment (bare 3rd person verb)
```

### Drag-and-Drop Vocabulary

- **húzd** = drag (imperative singular informal — used because gestures are immediate/casual)
- **engedd el** / **ejtsd** = drop / release
- ❌ Draggold / Droppolj (anglicism imperatives) — **wrong**

```
✅ Húzd ide a fájlokat
✅ Húzd és engedd el a feltöltéshez
❌ Draggold a fájlt ide
❌ Droppolj ide
```

### Error Messages — Direct Predicate

Hungarian error patterns are concrete and predicative, not nominalized:

- ❌ "Error: X" (English calque)
- ❌ "Hiba történt a fájl mentésekor" (verbose nominal)
- ✅ "**A fájl nem található. Ellenőrizze az elérési utat.**" (direct predicate + actionable advice)
- ✅ "**Nem sikerült menteni a fájlt.**" (Not succeeded + infinitive)

## Punctuation, Numbers, Dates, Currency

### Quotation Marks
- **Hungarian uses German-style low-high quotes: `„..."`**
- Secondary: `»...«` or `'...'`
- ❌ "English quotes" → ✅ „Magyar idézőjelek"

### Numbers
- Decimal separator: **comma** (1**,**5)
- Thousands separator: **space** (1 234,56) — or no separator for 4-digit numbers
- ❌ 1,234.56 → ✅ 1 234,56

### Dates — YYYY. MM. DD. (with periods)
- **Numeric**: `2024. 01. 15.` — periods AFTER each component, including the last
- **Long form**: "2024. január 15." (month name lowercase + day number + period)
- The period after the day is mandatory in formal writing.
- ❌ 15/01/2024 → ✅ 2024. 01. 15.
- ❌ 01/15/2024 (US format) → ✅ 2024. 01. 15.

### Time
- 24-hour: `14:30` or `14.30` (both acceptable, colon more modern)
- Word form: `14 óra 30 perc` or `fél három` (half past two)

### Currency: HUF Forint (NOT in eurozone)
- **Hungary uses the forint (Ft).** Hungary has NOT adopted the euro.
- Format: `1 234 Ft` — symbol AFTER amount, space thousands, **NO decimals** (forints aren't subdivided in practice)
- Older symbol HUF is used in financial documents; Ft in UI.
- ❌ 1,234.56 Ft → ✅ 1 234 Ft
- ❌ 99,99 Ft → ✅ 100 Ft (round to whole forints)

### Comma Rules

**NO comma before coordinating conjunctions** (vagy, és, meg, s):
- ❌ "Húzd a fájlokat ide, vagy kattints" → ✅ "Húzd a fájlokat ide vagy kattints"
- ❌ "Mentsd, és zárd be" → ✅ "Mentsd és zárd be"
- Exception: comma DOES precede `de`, `hanem`, `viszont` (but)

**ALWAYS comma before subordinating conjunctions:**
- hogy (that): "Látom, hogy működik"
- amely / ami (which): "A fájl, amelyet választottál"
- ha (if): "Kattints ide, ha folytatni szeretnéd"
- mert / mivel (because): "Nem működik, mert a fájl hiányzik"
- amikor (when): "Értesít, amikor kész"

## Word Order — Focus Position (CRITICAL)

Hungarian is technically SVO but word order is **driven by focus, not grammar**. The word **immediately before the verb** is emphasized.

| Sentence | Emphasis |
|---|---|
| **PÉTER** menti a fájlt | Péter (not someone else) is saving the file |
| Péter **A FÁJLT** menti | Péter is saving the file (not something else) |
| Péter menti **A FÁJLT** | (neutral / topic-comment) |

For UI strings:
- Use neutral SVO unless emphasis is required
- The word right before the verb is heard first — put the most important info there
- Imperatives default to verb-initial: "Mentsd el a fájlt"

## Question Structures — The `-e` Particle

Yes/no questions in formal Hungarian use the `-e` interrogative particle attached to the verb (or to the questioned element):

- "Látja-e a képernyőt?" (formal: do you see the screen?)
- "Működik-e a rendszer?" (does the system work?)
- Casual alternative: rising intonation only — "Látja a képernyőt?"

For UI, both work; `-e` adds formality.

## Terminology

| English | Preferred Hungarian | Avoid |
|---|---|---|
| Click | kattintani / kattintson | klikkelni |
| Settings | beállítások | |
| User | felhasználó | |
| Delete | törlés / törölni | deletálni |
| Save | mentés / menteni | save-olni |
| Upload | feltöltés / feltölteni | uploadolni |
| Download | letöltés / letölteni | downloadolni |
| Log in | bejelentkezés | login-olni |
| Log out | kijelentkezés | |
| Dashboard | irányítópult / vezérlőpult | dashboard |
| Account | fiók | account |
| Browser | böngésző | browser |
| Password | jelszó | |
| Search | keresés | |
| Folder | mappa | |
| Cancel | Mégse | |
| Email | email | |
| Online | online | |
| WiFi | wifi | |

**Proper noun abbreviations in UI:**
- ✅ "USA" / "az Egyesült Államok" (NOT "Amerikai Egyesült Államok" in cramped UI)
- ✅ "EU" (Európai Unió)
- ✅ "Nagy-Britannia" / "az Egyesült Királyság" (NOT the full official name)

**Brand names** stay in their original form (Apple, Google, Microsoft). Take suffixes via hyphen avoidance: "Google-tól" → restructure to "a Google szerint".

## Calque / Anti-Pattern Blocklist

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| csinálni értelmet | **van értelme / értelmes** | "to make sense" |
| a nap végén | **végül is / összességében** | "at the end of the day" |
| ugyanazon az oldalon lenni | **egyetérteni** | "be on the same page" |
| Lábtörést! (literal "break a leg") | **Sok sikert! / Kitartást!** | "break a leg" |
| Egy darab torta | **Gyerekjáték / Pofon egyszerű** | "piece of cake" |
| Nem igazán | **Valójában nem / Nem egészen** | "not really" |
| aktuális (for "actual") | **valódi / tényleges** | "actual" — aktuális means "current" in Hungarian! |
| vezérelt (hyphenated, X-vezérelt) | **X-alapú / X-vel működő** | "X-driven / X-powered" |
| AI-hajtott | **AI-alapú / mesterséges intelligenciával működő** | "AI-powered" |

**False friend warning:** `aktuális` ≠ "actual". `aktuális` means **current/up-to-date**. Use `valódi`, `tényleges`, or `igazi` for English "actual".

## "Per" vs "For" Distinction

Hungarian distinguishes carefully:

| English meaning | Hungarian | Example |
|---|---|---|
| Rate / unit ("per each") | **-ként** suffix or **-ra/-re vonatkozóan** | nyelv**enként** (per language) |
| Aggregate ("for X items") | **-hez/-hoz/-höz** or **-ra/-re** | 5 nyelv**hez** (for 5 languages) |

- ❌ "per nyelv" (when meaning total) → ✅ "**# nyelvhez**" / "**# nyelvre**"
- ❌ "# nyelvhez" (when meaning rate) → ✅ "**nyelvenként**"

## Self-Check Checklist

Run BEFORE finalizing each translation:

**Accuracy (critical):**
- [ ] **Case selection:** correct suffix from 18 (-ban/-ben for "in", -ba/-be for "into", -ra/-re for "onto", -nak/-nek for dative)
- [ ] **Vowel harmony:** suffix vowels match stem (back a/o/u vs front e/ö/ü)
- [ ] **Definite vs indefinite conjugation:** definite verb (-juk/-jük) with `a/az` objects; indefinite (-unk/-ünk) with `egy` or no article
- [ ] **Verbal prefix position:** separates with negation (`Ne mentse el`, not `Ne elmentse`)
- [ ] **Singular noun after numbers:** öt fájl (NOT öt fájlok); same for ICU `other`
- [ ] **Suffixes attach directly:** no spaces, no hyphens (fájlban, not fájl-ban)
- [ ] **No suffix on placeholders:** restructure ("A következő felhasználónak: {name}")
- [ ] **Verb-governed case:** segít+dat, bízik+ines, függ+abl, gondoskodik+del
- [ ] **Existential sentences:** noun phrases need `van/található`
- [ ] **Quotation marks:** „..." not "..."
- [ ] **Number format:** 1 234,56 (space + comma)
- [ ] **Date format:** YYYY. MM. DD. with periods (2024. 01. 15.)
- [ ] **Currency:** 1 234 Ft (Forint, space thousands, no decimals)
- [ ] **Conjunction commas:** no comma before vagy/és/meg/s; comma before hogy/ha/mert/amely
- [ ] **Placeholders preserved** exactly

**Naturalness:**
- [ ] **Ön/te consistency** — possessives AND verb forms match throughout
- [ ] **Adjective loanwords adapted:** global → globális, digital → digitális, special → speciális (MANDATORY when adapted form exists)
- [ ] **Native verbs:** kattintani not klikkelni, letölteni not downloadolni, törölni not deletálni
- [ ] **Buttons in NOUN form** (Mentés, Törlés — NOT Menteni)
- [ ] **Status messages in NOUN form** (Betöltés..., Mentés..., not Ment / Mentve)
- [ ] **Drag-and-drop:** húzd, engedd el (NOT Draggold, Droppolj)
- [ ] **Error messages:** direct predicate ("A fájl nem található"), not verbose nominal
- [ ] **Focus position:** important info before the verb when emphasizing
- [ ] **`aktuális` not used for "actual"** — use `valódi/tényleges`
- [ ] **Abbreviations in UI** (USA, EU — not full names)
- [ ] **Compound adjective restructure:** X-alapú, X-vel működő (not X-vezérelt)
- [ ] **"per" vs "for" distinct** (-ként for rate, -hez for aggregate)

## Worked Examples

### Example 1 — Save button + status

**Source:**
> Save  
> Saving your changes...  
> Changes saved.

**Wrong:**
> Menteni (infinitive)  
> Mentjük a változtatásokat... (1st person plural — too casual)  
> Mentve. (just past participle — incomplete)

**Correct:**
> **Mentés** (noun-form button)  
> **Mentés...** / **Mentés folyamatban...** (noun + ellipsis)  
> **A változtatások mentve.** (complete sentence with subject)

### Example 2 — Files counter with ICU

**Source:**
> {count, plural, one {# file} other {# files}}

**Correct Hungarian ICU:**
```
{count, plural,
  one {# fájl}
  other {# fájl}
}
```

Both branches use the SINGULAR. This is correct Hungarian.

### Example 3 — Drag-and-drop area

**Source:**
> Drag and drop files here, or click to browse

**Wrong:**
> Draggold a fájlokat ide, vagy kattints a tallózáshoz (anglicism + comma before vagy)

**Correct:**
> **Húzd ide a fájlokat vagy kattints a tallózáshoz** (native verb, no comma before vagy)

### Example 4 — Definite vs indefinite conjugation

**Source:**
> We saved the file. / We saved a file.

**Wrong:**
> Mentettünk a fájlt. (indefinite verb + definite object — broken)
> Mentettük egy fájlt. (definite verb + indefinite object — broken)

**Correct:**
> **Mentettük a fájlt.** (definite verb + definite object)
> **Mentettünk egy fájlt.** (indefinite verb + indefinite object)

### Example 5 — Verbal prefix with negation

**Source:**
> File not saved.

**Wrong:**
> A fájl nem elmentve. (prefix before negated)
> Nem elmentve a fájl. (broken word order)

**Correct:**
> **A fájl nincs elmentve.** (existential negation)
> **A fájl nincs mentve.** (with bare verb form)
> **Nem sikerült menteni a fájlt.** (alternative natural phrasing)

### Example 6 — Adjective loanword adaptation

**Source:**
> Global settings / Digital signature / Special offer

**Wrong:**
> Global beállítások / Digital aláírás / Special ajánlat (raw English)

**Correct:**
> **Globális beállítások** / **Digitális aláírás** / **Speciális ajánlat** (adapted)

### Example 7 — Number + noun (singular!)

**Source:**
> 5 users / 25 files / 100 languages

**Wrong:**
> 5 felhasználók / 25 fájlok / 100 nyelvek (plural after number — wrong!)

**Correct:**
> **5 felhasználó** / **25 fájl** / **100 nyelv** (singular after number)

### Example 8 — Placeholder + suffix (restructure)

**Source:**
> Sent to {name}

**Wrong:**
> {name}-nak küldve (suffix on placeholder with hyphen)

**Correct:**
> **A következő felhasználónak elküldve: {name}** (suffix on known word)
> **Címzett: {name}** (label-style)

### Example 9 — Verb-governed case

**Source:**
> Help the user / Trust the system / Depend on settings

**Wrong:**
> Segít a felhasználót / Bízik a rendszert / Függ a beállításoknak (all wrong cases)

**Correct:**
> **Segít a felhasználónak** (dative)
> **Bízik a rendszerben** (inessive)
> **Függ a beállításoktól** (ablative)

### Example 10 — Date and currency

**Source:**
> January 15, 2024 — Total: $1,234.56

**Wrong:**
> 01/15/2024 — 1,234.56 Ft (US date, English number format)

**Correct:**
> **2024. január 15.** vagy **2024. 01. 15.** — **Összesen: 1 234 Ft** (or whatever the USD-equivalent is, in whole forints)

## When in Doubt

1. **Vowel harmony unclear?** Look at the last vowel of the stem. Back (a, á, o, ó, u, ú) → -ban/-ba/-tól. Front (e, é, i, í, ö, ő, ü, ű) → -ben/-be/-től.
2. **Definite or indefinite verb?** Look at the object. Has `a/az`? → definite. Has `egy` or nothing? → indefinite. Pronouns (azt, ezt, ezeket) → definite.
3. **Case unclear?** Identify the meaning:
   - "in" (location) → -ban/-ben
   - "into" (motion) → -ba/-be
   - "out of" → -ból/-ből
   - "onto" → -ra/-re
   - "on" (location) → -on/-en/-ön
   - "to/for whom" → -nak/-nek
   - "with" → -val/-vel (consonant doubles: fájllal, fonnyal)
   - "about" → -ról/-ről
4. **Number + noun?** ALWAYS singular (öt fájl, 100 nyelv).
5. **Placeholder + suffix?** Restructure to put the suffix on a known word.
6. **Adjective from English?** Check if a -ális / -ikus / -ív form exists. Almost always yes for -al/-ic/-ive English originals.
7. **Verb from English?** Almost always wrong. Find the native Hungarian verb.
8. **Button label?** Use the NOUN form (Mentés, Törlés) — not infinitive, not imperative.
9. **Compound adjective with hyphen?** Almost always wrong. Restructure as -alapú or with -val/-vel.
10. **`aktuális`?** Means "current", not "actual". For English "actual" use `valódi/tényleges`.

Hungarian's agglutinative structure means most translation errors are at the **suffix level** (wrong case, broken harmony, wrong conjugation) rather than at the word-choice level. When the translation feels off, check vowel harmony, verb conjugation paradigm, and case selection first.
