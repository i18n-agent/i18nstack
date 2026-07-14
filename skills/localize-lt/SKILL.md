---
name: localize-lt
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Lithuanian (Lietuvių kalba) for Lithuania. Covers 7-case grammar including vocative, 2-gender agreement (-as/-is/-us/-ys masc, -a/-ė fem), definite/indefinite adjectives (naujas vs naujasis), Jūs/tu formality, ogonek + dot preservation (ą č ę ė į š ų ū ž — ė is uniquely Lithuanian), accusative-of-duration (6 metus NOT 6 metų), prieš + padalyvis construction, German-style quotes „...\", ISO YYYY-MM-DD dates, EUR currency (since 2015), comma decimal + space thousands (1 234,56 €), ICU plurals (one=nom.sg failas / few=nom.pl failai / many=gen.pl failų / other=gen.sg failo), the kuris/kuri relative pronoun agreement, and Baltic-not-Slavic identity. Lithuanian is one of the most archaic Indo-European languages — close sibling of Latvian but distinctly NOT Slavic and NOT Latvian."
---

# Localize: Lithuanian (lt → Lietuvių)

You are translating source text into Lithuanian for Lithuania. This skill captures grammar, register, UI conventions, formatting, and Lithuanian-specific failure modes derived from a production translation prompt.

## Scope & Variants

**One standard:**
- **lt-LT** — Lithuanian as used in Lithuania. Official state language.

No widely-distinguished variants in software localization.

**Native name:** Lietuvių kalba (the language); lietuviškai (the adverb "in Lithuanian"). Use "lietuvių" for the language.

**Identity guardrail:**
- Lithuanian is **Baltic, NOT Slavic**. It is in the same family as Latvian (Baltic) — not Russian, Polish, or any Slavic language, despite geographic proximity and centuries of contact.
- Lithuanian is **NOT Latvian**. Sister languages, but distinct: Lithuanian has 7 cases (including active vocative), Latvian has 6. Lithuanian uses ogoneks (ą ę į ų) for long vowels and the unique letter `ė`; Latvian uses macrons (ā ē ī ū) and cedillas (ģ ķ ļ ņ). Different prepositional government, different ICU plural rules.
- Lithuanian is **one of the most archaic Indo-European languages still spoken** — its grammar preserves features lost in most other IE languages. Do NOT modernize/simplify by analogy to Slavic or Germanic.
- Never translate Lithuanian content via Russian, Polish, or Latvian intermediaries.

## Register

**Default level: FORMAL (Jūs-form)** for software UI, errors, documentation, marketing. This differs from Latvian's neutral default.

| Source signals | Target register |
|---|---|
| Product UI, error messages, documentation, customer support, marketing | **Jūs-form** (default) |
| Personal blog, casual narrative, dialog, kids' content | **tu-form** |
| Short rhetorical fragments, exclamations | Preserve the rhetorical device — do NOT expand to formal full sentence |

| | Jūs (formal) | tu (informal) |
|---|---|---|
| Subject pronoun | Jūs | tu |
| Possessive | jūsų | tavo |
| Verb ending (2pl) | -ate / -ite (galite) | -i (gali) |
| Imperative ending | **-kite** (Išsaugokite, Spustelėkite) | **-k** (Išsaugok, Spustelėk) |

**Within a file, ONE register only.** Mixing `Jūs gali` (formal pronoun + informal verb) or `Jūsų failas + Išsaugok` (formal possessive + informal imperative) is always wrong.

Examples:
- ❌ Jūs gali pakeisti nustatymus → ✅ **Jūs galite pakeisti nustatymus**
- ❌ Įkelkite jūsų failus + Naršyk → ✅ **Įkelkite jūsų failus + Naršykite**

## Critical Hard Rules

### Special Characters: ą č ę ė į š ų ū ž (severity 3.0)

These are **essential letters**, not optional diacritics. Stripping makes Lithuanian unreadable.

- **`ė`** is UNIQUE to Lithuanian (no other language uses it as a base letter) — represents a long mid-front vowel.
- **Ogonek letters** (ą, ę, į, ų) historically marked nasal vowels; modern pronunciation = long vowels. Stripping confuses cases (genitive plural `nustatymų` vs nominative `nustatymu` — different word).
- **`ū`** is a long u.
- **Háčeks** (č, š, ž) = post-alveolar fricatives/affricates.

| Wrong (stripped) | Correct | Word |
|---|---|---|
| ieskoti | **ieškoti** | to search (š essential) |
| zodynas | **žodynas** | dictionary (ž essential) |
| nustatymu | **nustatymų** | settings (ų essential — genitive plural) |
| ikelti | **įkelti** | upload (į essential) |
| cia | **čia** | here (č essential) |
| buti | **būti** | to be (ū essential) |
| del | **dėl** | because of (ė essential) |

The `ė` vs `e` distinction is meaning-critical (`mane` "me" vs `manė` "thought"). Never replace ė with e.

### Two-Gender Agreement (severity 2.0)

Lithuanian has 2 grammatical genders determined by noun ending:

| Ending | Gender | Examples |
|---|---|---|
| **-as, -is, -us, -ys** | masculine | vartotoj**as**, fail**as**, brol**is**, sūn**us**, mėnes**is** |
| **-a, -ė** | feminine | sistem**a**, platform**a**, mergait**ė**, paskyr**a** |

(A few -is nouns are feminine — e.g., `naktis` "night", `širdis` "heart" — but rare in tech UI.)

Adjectives agree in **gender + number + case** (3-way agreement):

| Wrong | Correct | Why |
|---|---|---|
| naujas sistema | nauj**a** sistema | sistema is fem |
| nauja failas | nauj**as** failas | failas is masc |
| geras platforma | ger**a** platforma | platforma is fem |
| nauja vartotojas | nauj**as** vartotojas | vartotojas is masc |

### Seven-Case System (severity 2.0)

Lithuanian has 7 cases (vocative is **active** — used in direct address, unlike Latvian):

| Case | Function | Example (failas — file, masc) |
|---|---|---|
| Nominative (vardininkas) | subject | failas yra atidarytas |
| Genitive (kilmininkas) | possession, after iš/nuo/dėl/be/iki | failo turinys |
| Dative (naudininkas) | indirect obj, "for whom" | failui |
| Accusative (galininkas) | direct obj, duration, after į/per/pro/apie/už | matau failą |
| Instrumental (įnagininkas) | means, after su | su failu |
| Locative (vietininkas) | location ("in"), no preposition needed | faile |
| Vocative (šauksmininkas) | direct address | (faile! — though rare in UI; common for names: Jonai!) |

**Key gotchas:**
- ❌ `su failas` → ✅ `su fail**u**` (su + instrumental)
- ❌ `į sistema` → ✅ `į sistem**ą**` (į + accusative for motion)
- ❌ `į sistemoje` → ✅ `į sistem**ą**` (motion) / `sistemoje` (location, no prep)
- ❌ `iš sistema` → ✅ `iš sistem**os**` (iš + genitive)
- ❌ `apie failas` → ✅ `apie fail**ą**` (apie + accusative)

### Accusative of Duration (severity 2.5)

**Time durations require ACCUSATIVE (galininkas), NOT genitive.** This is a Lithuanian-specific rule that frequently fails.

| Wrong (genitive) | Correct (accusative) | English |
|---|---|---|
| Praleidau 6 met**ų** | Praleidau 6 met**us** | I spent 6 years |
| Dirbau 3 valand**ų** | Dirbau 3 valand**as** | I worked 3 hours |
| Mokiausi 5 mėnesi**ų** | Mokiausi 5 mėnesi**us** | I studied 5 months |

**Exception** — verbs that govern genitive specifically (e.g., `laukti` "wait for") keep their genitive:
- ✅ Laukiau 20 minučių (laukti governs genitive — minučių is correct here)
- ✅ Bet: Mokiausi 20 minučių? Verify each verb's government.

Rule of thumb: if English uses "for X time/duration", the default Lithuanian case is accusative — unless the governing verb specifically demands a different case.

### Verb Construction Integrity (severity 2.0–2.5)

**"Before doing X"**: use `prieš + padalyvis` (half-participle/gerund) — NEVER `prieš + finite verb`.

| Wrong | Correct |
|---|---|
| prieš jūs sumokėjote (prieš + finite past) | **prieš sumokant** (padalyvis) / **prieš tai sumokėjus** (pusdalyvis) |

**Passive voice**: requires correct participle + case agreement.

**Person consistency in narrative**: if the narrator is the subject, use 1st person throughout. Do not drift to 3rd person.

- ❌ Padėjo valdyti (3rd person where narrator is subject) → ✅ Padėjau valdyti (1st person)

### Relative Pronoun Agreement: kuris/kuri (severity 2.5)

Relative pronouns must agree with antecedent in **gender + number**. Case is determined by the relative clause role.

| Wrong | Correct | Why |
|---|---|---|
| sistema, **kuris** veikia | sistema, **kuri** veikia | sistema is feminine → kuri |
| DI, **kuri** niekada nepamiršta | DI, **kuris** niekada nepamiršta | DI (dirbtinis intelektas) is masculine → kuris |
| platforma, **kuris** palaiko | platforma, **kuri** palaiko | platforma is feminine → kuri |

### Number+Case in Counted Nouns (severity 2.0)

Lithuanian has a sophisticated number-noun case pattern:

| Number | Case | Example (failas) |
|---|---|---|
| 1, 21, 31, 41... (ends in 1 except 11) | **nominative singular** | 1 failas, 21 failas |
| 2-9, 22-29... | **nominative plural** | 3 failai, 5 failai |
| 0, 10-20, multiples of 10 | **genitive plural** | 10 failų, 0 failų, 15 failų |

Adjectives match:
- ❌ trys naujas failai → ✅ trys **nauji** failai (nom.pl)
- ❌ dešimt nauji failų → ✅ dešimt **naujų** failų (gen.pl)

### ICU Plural Categories (severity 2.5)

Lithuanian has **4 CLDR plural categories**: **one / few / many / other**.

| Branch | Rule | Case required | Example |
|---|---|---|---|
| one | n mod 10 = 1 AND n mod 100 ≠ 11-19 | **nominative singular** | `one {# failas}` |
| few | n mod 10 = 2-9 AND n mod 100 ≠ 11-19 | **nominative plural** | `few {# failai}` |
| many | n is a non-integer (fraction/decimal) | **genitive singular** | `many {# failo}` |
| other | n = 0, 10-20, 30, 40... (also general fallback) | **genitive plural** | `other {# failų}` |

**Wait — verify the spec.** Lithuanian CLDR is:
- one: n % 10 = 1 and n % 100 ≠ 11 (integers ending in 1 except 11)
- few: n % 10 = 2..9 and n % 100 ≠ 11..19 (integers ending in 2-9 except 11-19)
- many: non-integer (decimal/fraction) → **genitive singular**
- other: everything else (including 0, 10-20) → **genitive plural**

```icu
{count, plural,
  one {# failas}
  few {# failai}
  many {# failo}
  other {# failų}
}
```

❌ `many {# failai}` → ✅ `many {# failo}` (gen.sg for fractions)
❌ `one {# failai}` (nom.pl in one branch) → ✅ `one {# failas}` (nom.sg)
❌ `other {# failas}` → ✅ `other {# failų}` (gen.pl)

### Ellipsis Completion (severity 2.0)

Lithuanian requires an explicit noun after numbers/quantifiers — bare numbers or dangling genitives are ungrammatical:

- ❌ "4 kitų" (bare genitive, no noun) → ✅ "**dar 4 modeliai**" / "**4 kiti modeliai**"
- ❌ "ir 3 daugiau" → ✅ "**ir dar 3 failai**" / "**ir 3 papildomi**"

### Definite vs Indefinite Adjectives

Lithuanian has two adjective forms:

| Form | Use | Example |
|---|---|---|
| Indefinite | general, non-specific | nauj**as** failas (a new file) |
| Definite (pronominal) | specific, already-mentioned | naujas**is** failas (the new file) |

UI usually uses **indefinite**:
- ❌ "naujasis failas" for general reference
- ✅ "naujas failas"

## Pronouns and Possessives

| English | Formal (Jūs) | Informal (tu) |
|---|---|---|
| you (subj) | Jūs | tu |
| your (poss) | jūsų | tavo |
| Imperative ending | -**kite** (Išsaugokite) | -**k** (Išsaugok) |
| Verb (2pl/sg) | -ate/-ite (galite) | -i (gali) |

`jūsų` and `tavo` are **invariable possessives** (do not decline). Possessive adjectives `mano`, `tavo`, `savo`, `jo`, `jos`, `mūsų`, `jūsų`, `jų` all stay in the same form regardless of the noun's case.

## UI Conventions

### Button Labels — Infinitive Form

Lithuanian buttons use the **infinitive**, NOT the imperative or nominalization:

| Wrong | Correct | English |
|---|---|---|
| Išsaugokite (imperative) | **Išsaugoti** | Save |
| Išsaugojimas (nominalization) | **Išsaugoti** | Save |
| Ištrinkite | **Ištrinti** | Delete |
| Atšaukite | **Atšaukti** | Cancel |
| Pasirinkite | **Pasirinkti** | Select |
| Spustelėkite | **Spustelėti** | Click |

### Status Messages — Impersonal / 3rd Person

Use **active 3rd person** or **impersonal passive** — NOT "Mes analizuojame...":

| Wrong | Correct | English |
|---|---|---|
| Mes analizuojame... | **Analizuoja... / Analizuojama...** | Analyzing... |
| Sistema krauna | **Krauna... / Kraunama...** | Loading... |
| Mes saugome jūsų darbą | **Saugoma... / Saugomas darbas...** | Saving... |

### Bulk Action Buttons — Use "viską" (accusative)

```
✅ Pasirinkti viską          (Select All)
✅ Atšaukti visą pasirinkimą (Deselect All)
✅ Išvalyti viską            (Clear All)
❌ Pasirinkti visus          (implies "all people")
```

Pattern: `[infinitive] + viską` OR `[infinitive] + visą + [noun.acc]`

### Drag-and-Drop Vocabulary

- **vilkti** = drag
- **numesti** = drop
- ❌ "paleisti" = release/liberate — **wrong meaning**

```
✅ Vilkite failus čia                     (drag files here)
✅ Vilkite ir numeskite failus čia        (drag and drop files here)
❌ Numeskite failus čia                    (drop-only — feels incomplete)
❌ Paleiskite failą čia                    (paleisti = release, not drop)
```

### File Picker / Placeholder Handling

Avoid putting placeholders in a case-marked position — restructure:

- ❌ "{name} failui" (case on placeholder) → ✅ "**Failui {name}**" / "**Failas pavadinimu {name}**"
- ❌ "Palaikymas {formatList} failams" → ✅ "**Palaikomi {formatList} failai / formatai**" (participle over noun+dative)

## Punctuation, Numbers, Dates, Currency

### Quotation Marks
- **Lithuanian uses German-style low-high quotes: `„..."`**
- ❌ "English quotes" → ✅ „Lietuviškos kabutės"

### Numbers
- Decimal separator: **comma** (1**,**5)
- Thousands separator: **space** (1 234,56)
- ❌ 1,234.56 → ✅ 1 234,56

### Dates
- **Numeric (ISO)**: YYYY-MM-DD → 2024-01-15
- **Long form**: "2024 m. sausio 15 d." (months **lowercase**, "m." = metai/year, "d." = diena/day)
- The "m." abbreviation always follows the year; "d." always follows the day number.

### Time
- 24-hour: 14:30 or `14 val. 30 min.` (val. = valanda = "hour")

### Currency: EUR (since 2015)
- **Lithuania adopted the euro on 2015-01-01.** Symbol after amount.
- Format: `99,99 €` / `1 234,56 €`
- Pre-2015 currency was litas (Lt) — should NOT appear in new UI.

### Comma Rules

**NO comma before coordinating conjunctions:**
- arba (or), ar (or — different nuance), ir (and), bei (and also)
- ❌ "Vilkite failus čia, arba spustelėkite" → ✅ "...čia arba spustelėkite"
- Exception: comma DOES precede `bet` / `tačiau` / `o` (but)

**ALWAYS comma before subordinating conjunctions:**
- kad (that): "Matau, kad failas atidarytas"
- kuris / kuri (which/who): "Failas, kurį pasirinkote"
- jei / jeigu (if): "Spustelėkite, jei norite tęsti"
- nes / kadangi (because): "Neveikia, nes failas nerastas"
- kai (when): "Pranešti, kai bus baigta"

## Terminology

| English | Preferred Lithuanian | Avoid |
|---|---|---|
| Click | spustelėti / paspausti | klikinti (anglicism) |
| Settings | nustatymai | — |
| User | vartotojas | — |
| Delete | ištrinti / pašalinti | — |
| Save | išsaugoti | — |
| Upload | įkelti | uploadinti |
| Download | atsisiųsti | downloadinti |
| Log in | prisijungti | — |
| Log out | atsijungti | — |
| File | failas (or rinkmena — pure Lithuanian, more formal) | — |
| Folder | aplankas | — |
| Dashboard | valdymo skydelis | — |
| Account | paskyra | — |
| Email | el. paštas | emailas |
| Browser | naršyklė | brauseris |
| Link | nuoroda | — |
| Password | slaptažodis | — |
| Search | paieška / ieškoti | — |

**Proper noun abbreviations in UI:**
- ✅ "JAV" (NOT "Jungtinės Amerikos Valstijos" in cramped UI)
- ✅ "JK" / "Didžioji Britanija" (NOT "Jungtinė Didžiosios Britanijos Karalystė")
- ✅ "ES" (Europos Sąjunga — European Union)
- ✅ "DI" (dirbtinis intelektas — AI; treat as masculine)

**Brand names** remain undeclined. Take gender of implied noun (OneSky platforma = fem, OneSky įrankis = masc) or default to masculine.

## Calque / Anti-Pattern Blocklist

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| Tai daro prasmę | **Tai logiška / Tai turi prasmę** | "makes sense" |
| daryti prasmę | **turėti prasmę / būti prasminga** | "make sense" |
| Dienos pabaigoje | **Galų gale / Iš esmės** | "at the end of the day" |
| Ne tikrai | **Iš tiesų ne / Ne visai** | "not really" |
| būti saugioje pusėje | **dėl visa ko / saugumo dėlei** | "be on the safe side" |
| Salaužk koją (literal) | **Sėkmės! / Lai sekasi!** | "break a leg" |
| Lengvas kaip pyragas | (literal calque acceptable but) **paprasta kaip du kartus du** | "piece of cake" |
| Lyja kates ir šunis | **Lyja kaip iš kibiro** | "raining cats and dogs" |
| vartotojo-draugiškas | **patogus vartotojui / intuityvus** | "user-friendly" |
| debesija-paremtas | **debesyje veikiantis / debesų paslauga** | "cloud-based" |
| konteksto suvokiantis | **kontekstą suprantantis / kontekstinis** | "context-aware" |
| DI-varomas | **su dirbtinio intelekto pagalba / paremtas dirbtiniu intelektu** | "AI-powered" |
| duomenų varomas | **paremtas duomenimis / duomenimis grįstas** | "data-driven" |
| downloadinti | **atsisiųsti** | direct anglicism |
| uploadinti | **įkelti** | direct anglicism |
| klikinti | **spustelėti / paspausti** | direct anglicism |
| emailas | **el. paštas** | direct anglicism |

## "per" vs "for" Distinction

Lithuanian has two distinct meanings for English "per/for" that must be clarified:

| English meaning | Lithuanian construction | Example |
|---|---|---|
| Rate / unit ("each") | **už** + accusative OR **kiekvienai** + dative | už kalbą (per language) / kiekvienai kalbai (for each language) |
| Aggregate / total ("for X items") | dative plural | "{credits} kreditų {count} kalboms" (credits for X languages) |

Clarify the relationship when English is ambiguous. Don't default to one construction.

## Tense and Aspect

Lithuanian preserves **present continuous** with present tense (no separate continuous form):

| English | Wrong | Correct |
|---|---|---|
| "we are building" | mes pastatėme (past perf) | **mes statome** (present) |
| "costs are increasing" | išlaidos padidėjo (past) | **išlaidos didėja** (present) |

## Polysemous Word Disambiguation

| English (domain) | Correct Lithuanian | Wrong sense |
|---|---|---|
| scale (IT scalability) | **mastelio keitimas / plėtimas** | mastelis (measurement) |
| deploy (software) | **įdiegti / paleisti į produkciją** | dislokuoti (military) |
| copy (marketing text) | **tekstas / reklamos tekstas** | kopija (photocopy) |
| bug (defect) | **klaida** | vabalas (insect) |
| pipeline (CI/CD) | **konvejeris / pipeline** | vamzdynas (plumbing) |
| architecture (software) | **architektūra (IT design)** | architektūra (building) — context disambiguates |

## Self-Check Checklist

Run BEFORE finalizing each translation:

**Accuracy (critical):**
- [ ] **Gender agreement:** -as/-is/-us/-ys = masc, -a/-ė = fem; adjectives match
- [ ] **Case correct:** 7 cases; locative for "in", accusative after į (motion)
- [ ] **Adjective agreement:** gender + number + case all three
- [ ] **Number-noun case:** 1=nom.sg, 2-9=nom.pl, 10-20=gen.pl
- [ ] **Accusative of duration:** 6 metus (NOT 6 metų), 3 valandas (NOT 3 valandų) — except where verb governs genitive (laukti)
- [ ] **Relative pronoun:** kuris (masc) / kuri (fem) matches antecedent
- [ ] **Preposition case:** su→instr, į→acc (motion) / loc (no prep), iš/nuo/dėl→gen, apie/už→acc
- [ ] **Diacritics preserved:** all ą č ę ė į š ų ū ž present
- [ ] **Verb construction:** prieš + padalyvis (NOT prieš + finite verb); narrative person consistent
- [ ] **Placeholders preserved** exactly
- [ ] **ICU plural cases:** one=nom.sg (failas), few=nom.pl (failai), many=gen.sg (failo, for fractions), other=gen.pl (failų)
- [ ] **Quotation marks:** „..." not "..."
- [ ] **Number format:** 1 234,56 (space + comma)
- [ ] **Conjunction commas:** no comma before arba/ar/ir; comma before kad/kuris/jei/nes
- [ ] **Date format:** YYYY-MM-DD or "2024 m. sausio 15 d."
- [ ] **Currency:** 99,99 € (comma decimal, € after amount)
- [ ] **Ellipsis completed:** explicit noun after numbers (dar 4 modeliai)

**Naturalness:**
- [ ] **Jūs/tu consistency** — possessives, verbs, imperatives all same level
- [ ] **Buttons in infinitive** (Išsaugoti, not Išsaugokite)
- [ ] **Status in 3rd person/impersonal** (Krauna / Kraunama, not Mes kraunam)
- [ ] **"viską" pattern for bulk actions** (Pasirinkti viską)
- [ ] **vilkti/numesti** for drag-and-drop (NOT paleisti)
- [ ] **Native vocabulary** (atsisiųsti, el. paštas — not downloadinti, emailas)
- [ ] **No hyphenated calques** (X-aware, X-powered, X-driven, user-friendly)
- [ ] **Abbreviations in UI** (JAV, ES, DI — not full forms in cramped space)
- [ ] **`ė` vs `e`** correctly distinguished (mane vs manė)

## Worked Examples

### Example 1 — Save button + status

**Source:**
> Save  
> Saving your changes...  
> Changes saved.

**Wrong:**
> Išsaugokite (imperative)  
> Mes saugome jūsų pakeitimus...  
> Pakeitimai išsaugotas. (wrong gender/number — pakeitimai is masc.pl)

**Correct:**
> **Išsaugoti** (infinitive button)  
> **Saugoma... / Saugomi pakeitimai...** (impersonal)  
> **Pakeitimai išsaugoti.** (masc.pl participle agreeing with pakeitimai)

### Example 2 — Files counter with ICU

**Source:**
> {count, plural, =0 {No files} one {# file} other {# files}}

**Correct Lithuanian ICU:**
```
{count, plural,
  one {# failas}
  few {# failai}
  many {# failo}
  other {# failų}
}
```

Reasoning:
- one (1, 21, 31...): nominative singular → failas
- few (2-9, 22-29...): nominative plural → failai
- many (fractions like 1.5): genitive singular → failo
- other (0, 10-20, etc.): genitive plural → failų

### Example 3 — Drag-and-drop area

**Source:**
> Drag and drop files here, or click to browse

**Wrong:**
> Numeskite failus čia, arba spustelėkite, kad naršytumėte (drop-only verb; comma before arba)

**Correct:**
> **Vilkite ir numeskite failus čia arba spustelėkite, kad naršytumėte** (no comma before arba; comma before kad-clause)

### Example 4 — Accusative of duration

**Source:**
> I worked here for 6 years.

**Wrong (genitive):**
> Dirbau čia 6 metų.

**Correct (accusative):**
> **Dirbau čia 6 metus.**

(`metai` "year" → accusative plural `metus` for duration)

### Example 5 — Relative pronoun gender

**Source:**
> The platform that supports multiple languages

**Wrong:**
> Platforma, kuris palaiko kelias kalbas (kuris is masc, platforma is fem)

**Correct:**
> **Platforma, kuri palaiko kelias kalbas** (kuri matches feminine platforma)

### Example 6 — Bulk action

**Source:**
> Select All

**Wrong:**
> Pasirinkti visus (implies "all people, not items")

**Correct:**
> **Pasirinkti viską** (compact accusative neuter)

### Example 7 — "Before" construction

**Source:**
> Before you pay, please review the order.

**Wrong:**
> Prieš jūs sumokėjote, peržiūrėkite užsakymą. (prieš + finite verb — ungrammatical)

**Correct:**
> **Prieš sumokant, peržiūrėkite užsakymą.** (prieš + padalyvis sumokant)
> OR: **Prieš tai sumokėjus, peržiūrėkite užsakymą.** (prieš + pusdalyvis)

### Example 8 — `ė` vs `e` (meaning-critical)

**Wrong:**
> "Sistema mane patikrino" (mane = "me" — correct usage)
> "Sistema manė patikrinti" (manė = "thought" — different word!)

The two are NOT interchangeable. ALWAYS preserve `ė`.

### Example 9 — Number+case with adjective

**Source:**
> 3 new files / 10 new files

**Correct:**
> **3 nauji failai** (nom.pl + nom.pl)  
> **10 naujų failų** (gen.pl + gen.pl)

## When in Doubt

1. **Diacritic uncertain?** Default to the form with diacritic — Lithuanian rarely has unmarked forms where marked exists. Especially never strip `ė` (changes meaning completely).
2. **Case unclear?** Re-read the preposition or verb governing the noun. Lookup:
   - su (with) → instrumental
   - į (into, motion) → accusative
   - per (through), pro (past), apie (about), už (for) → accusative
   - iš (from), nuo (off), dėl (because of), be (without), iki (until) → genitive
   - palaikyti (support), matyti (see), girdėti (hear) → accusative object
   - laukti (wait for), bijoti (fear), reikia (need) → genitive object
3. **Duration?** Use **accusative** (6 metus, 3 valandas) unless the verb specifically governs another case.
4. **ICU branch unclear?** Lithuanian has 4: one/few/many/other.
   - one = nom.sg (1, 21, 31...)
   - few = nom.pl (2-9, 22-29...)
   - many = gen.sg (1.5, 2.5 — fractions/decimals)
   - other = gen.pl (0, 10-20, 30...)
5. **Gender unclear?** -as/-is/-us/-ys → masc. -a/-ė → fem. (A few -is nouns are fem: naktis, širdis, dantis — rare in UI.)
6. **Register unclear?** Default to Jūs-form for UI/errors/marketing.
7. **Compound adjective with hyphen?** Almost always wrong. Restructure with preposition or participle.
8. **"prieš" with a verb?** Use padalyvis (sumokant), not finite verb (sumokėjote).
9. **Relative pronoun?** Check antecedent's gender first: failas → kuris, sistema → kuri.

Lithuanian is one of the most morphologically rich modern European languages. When the translation feels off, the cause is usually one of: wrong case (especially missed accusative-of-duration), wrong gender agreement on relative pronoun, stripped diacritic (especially `ė`), or finite-verb-after-prieš. Fix the structure, don't just swap synonyms.
