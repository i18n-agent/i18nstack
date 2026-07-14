---
name: localize-lv
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Latvian (Latviešu valoda) for Latvia. Covers 6-case grammar (no vocative), 2-gender agreement (-s/-š/-is masc, -a/-e fem), definite/indefinite adjectives (jauns vs jaunais), Jūs/tu formality with register auto-detection from source tone, macron + cedilla preservation (ā č ē ģ ī ķ ļ ņ š ū ž), reflexive -ties verbs, German-style quotes „...\", DD.MM.YYYY dates, EUR currency (since 2014), comma decimal + space thousands (1 234,56 €), ICU plurals (zero=gen.pl failu / one=nom.sg fails / other=nom.pl faili), the colloquial \"priekš\" warning (use dative instead), and Baltic-not-Slavic identity. Latvian is a Baltic language — close sibling of Lithuanian but distinctly NOT Slavic and NOT Lithuanian."
---

# Localize: Latvian (lv → Latviešu)

You are translating source text into Latvian for Latvia. This skill captures grammar, register, UI conventions, formatting, and Latvian-specific failure modes derived from a production translation prompt.

## Scope & Variants

**One standard:**
- **lv-LV** — Latvian as used in Latvia. Official state language.

No widely-distinguished variants in software localization. Latvian outside Latvia (Latvian diaspora) uses the same standard.

**Native name:** Latviešu valoda (the language); latviski (the adverb "in Latvian"). Use "latviešu" for the language in UI, never the obsolete "lettish".

**Identity guardrail:**
- Latvian is **Baltic, NOT Slavic**. It is in the same family as Lithuanian (Baltic) — not Russian, Polish, or any Slavic language, despite geographic proximity.
- Latvian is **NOT Lithuanian**. Sister languages, but distinct: different cases (lv=6, lt=7), different special characters (lv uses macrons ā ē ī ū + cedillas ģ ķ ļ ņ; lt uses ogoneks ą ę į ų + unique ė), different plural patterns, different prepositional government.
- Never translate Latvian content via Lithuanian or Russian intermediaries.

## Register Auto-Detection (CRITICAL — severity 2.5)

**The default register is NEUTRAL, NOT formal. Latvian must determine register from source content tone.** Defaulting all content to Jūs-form is a quality failure.

Determine register from source signals BEFORE translating:

| Source signals | Target register |
|---|---|
| Casual blog, personal narrative, internet slang, dialog, rhetorical fragments, exclamations, sarcasm ("Fight me.", "Sorry, Kenji.", "Look, here's the thing—") | **tu-form** or neutral — preserve casualness |
| Product UI strings, error messages, system notifications, documentation, customer support | **Jūs-form** (formal/professional) |
| Marketing copy, landing pages, value props | **Jūs-form** UNLESS source uses deliberately casual/friendly tone — then match |
| Short punchy fragments | Preserve the rhetorical device — do NOT expand to full polite sentence |

**Register mismatch examples that MUST be caught:**
- ❌ "Fight me." → "Strīdieties ar mani." (formal Jūs for casual slang) → ✅ "Cīnies ar mani." (tu-form)
- ❌ "Sorry, Kenji." → "Atvainojiet, Kendži." (formal for casual aside) → ✅ "Piedod, Kendži."
- ❌ "Look, here's the thing—" → "Klausieties, lieta ir šāda —" (formal imperative for conversational opener) → ✅ "Klau, lieta ir tāda —"

When source is casual but you used Jūs-form, the result sounds stilted and unnatural. This is severity 2.5 — a quality failure, not a style preference.

**Within a file, ONE register only.** Mixing `Jūs vari...` (Jūs verb + tu form) or `jūsu fails + Saglabā` (formal possessive + informal imperative) is always wrong.

## Critical Hard Rules

### Special Characters: ā č ē ģ ī ķ ļ ņ š ū ž (severity 3.0)

These are **essential letters**, not optional diacritics. Stripping makes Latvian unreadable and is severity 3.0.

- **Macrons** (ā, ē, ī, ū) = long vowels. Changes meaning: `mājas` (home) vs `majas` (nonsense), `mīt` (live) vs `mit` (nonsense).
- **Cedillas** (ģ, ķ, ļ, ņ) = palatalized consonants. Distinct phonemes.
- **Háčeks** (č, š, ž) = post-alveolar fricatives/affricates.

| Wrong (stripped) | Correct | Word |
|---|---|---|
| iestatijumi | **iestatījumi** | settings (ī essential) |
| lietotajs | **lietotājs** | user (ā essential) |
| drosiba | **drošība** | security (š AND ī essential) |
| valoda | **valoda** | (already correct, no diacritic needed) |
| Latviesu | **Latviešu** | Latvian (š essential) |

Common required diacritics in UI: iestatījumi, lietotājs, drošība, sistēma, mainīt, saņemt, paroles, e-pasts, vārds, pārlūks.

### Two-Gender Agreement (severity 2.0)

Latvian has 2 grammatical genders determined by noun ending:

| Ending | Gender | Examples |
|---|---|---|
| **-s, -š, -is, -us** | masculine | lietotāj**s**, fail**s**, akmen**s**, mēnes**is**, ledu**s** |
| **-a, -e** | feminine | sistēm**a**, platform**a**, mape, parole, lieta |

Adjectives agree in **gender + number + case** (3-way agreement):

| Wrong | Correct | Why |
|---|---|---|
| jauns sistēma | jaun**a** sistēma | sistēma is fem |
| jauna fails | jaun**s** fails | fails is masc |
| labs platforma | lab**a** platforma | platforma is fem |
| jauna lietotājs | jaun**s** lietotājs | lietotājs is masc |

### Six-Case System (severity 2.0)

Latvian has 6 cases (vocative is rare and largely absent from modern UI):

| Case | Function | Example (fails — file, masc) |
|---|---|---|
| Nominative | subject | fails ir atvērts |
| Genitive | possession, after no/bez/dēļ/līdz/pie/pēc | faila saturs |
| Dative | indirect obj, after palīdzēt/pateikties; "for whom" | failam |
| Accusative | direct obj, after uz/caur/par/pret/ap/pa, after ar (instrumental sense) | redzu failu / ar failu |
| Locative | location ("in"), no preposition needed | failā |
| Instrumental | NO separate form — uses accusative with `ar` | ar failu |

**Key gotchas:**
- ❌ `ar fails` → ✅ `ar fail**u**` (ar + accusative form)
- ❌ `uz sistēmā` → ✅ `uz sistēm**u**` (uz + accusative) OR `sistēmā` (locative, no prep)
- ❌ `no sistēma` → ✅ `no sistēm**as**` (no + genitive)
- ❌ `par fails` → ✅ `par fail**u**` (par + accusative)

### Verb-Governed Case (severity 2.0)

Specific verbs require specific cases for their objects — do not confuse with preposition-governed case:

| Verb | Required case | Example |
|---|---|---|
| palīdzēt (help) | **dative** | palīdzēt lietotāj**am** ❌ palīdzēt lietotāj**u** |
| pateikties (thank) | **dative** | pateikties lietotāj**am** ❌ pateikties lietotāj**u** |
| vajadzēt (need) | **genitive** | vajadzēt fail**a** ❌ vajadzēt fail**s** |
| gaidīt (wait) | accusative | gaidīt fail**u** |
| meklēt (search for) | accusative | meklēt fail**u** |

### Relative Pronoun Agreement: kurš/kura (severity 2.5)

Relative pronouns must agree with antecedent in **gender + number**. Case is determined by the relative clause role.

| Wrong | Correct | Why |
|---|---|---|
| sistēma, **kurš** darbojas | sistēma, **kura** darbojas | sistēma is feminine → kura |
| fails, **kura** ir atvērts | fails, **kurš** ir atvērts | fails is masculine → kurš |
| platforma, **kurš** atbalsta | platforma, **kura** atbalsta | platforma is feminine → kura |

### Number+Case in Counted Nouns (severity 2.0)

Latvian quantified-noun phrases follow a specific case pattern:

| Number | Case | Example (fails) |
|---|---|---|
| 1, 21, 31... (ends in 1, except 11) | **nominative singular** | 1 fails, 21 fails |
| 2-9, 22-29... | **nominative plural** | 3 faili, 5 faili |
| 0, 10-20, multiples of 10 | **genitive plural** | 10 failu, 15 failu, 0 failu |

Adjectives match this pattern:
- ❌ trīs jauns faili → ✅ trīs **jauni** faili (nom.pl)
- ❌ desmit jauni failu → ✅ desmit **jaunu** failu (gen.pl)

### ICU Plural Categories (severity 2.5)

Latvian has 3 CLDR plural categories: **zero / one / other**.

| Branch | Rule | Case required | Example |
|---|---|---|---|
| zero | n = 0 | **genitive plural** | `zero {# failu}` |
| one | n mod 10 = 1 AND n mod 100 ≠ 11 | **nominative singular** | `one {# fails}` |
| other | everything else | **nominative plural** | `other {# faili}` |

```icu
{count, plural,
  zero {# failu}
  one {# fails}
  other {# faili}
}
```

❌ `zero {# fails}` (nom.sg in zero branch) → ✅ `zero {# failu}` (gen.pl)
❌ `one {# faili}` (nom.pl in one branch) → ✅ `one {# fails}` (nom.sg)

### Reflexive Verbs in -ties (severity 1.5)

Verbs ending in `-ties` keep the reflexive in conjugation. Common UI verbs:

| Infinitive | 1sg | 3sg/pl | Meaning |
|---|---|---|---|
| pieslēgties | pieslēdzos | pieslēdzas | log in |
| atslēgties | atslēdzos | atslēdzas | log out |
| reģistrēties | reģistrējos | reģistrējas | register |
| atgriezties | atgriežos | atgriežas | return |

❌ "Es pieslēdz**u**" (non-reflexive) → ✅ "Es pieslēdz**os**" (reflexive)

### Verb Construction Integrity (severity 2.0)

- **"Before doing X"**: use `pirms + verbal noun (gen)` or `pirms + gerund`, NOT `pirms + finite verb`
  - ❌ pirms jūs samaksājāt → ✅ pirms samaksāšanas / pirms maksājuma
- **Passive voice**: `tiek + past participle`
  - ❌ Fails ir saglabā (broken) → ✅ Fails **tiek saglabāts** / Fails **ir saglabāts**

### Ellipsis Completion (severity 2.0)

Latvian requires an explicit noun after numbers/quantifiers. English allows ellipsis ("4 others", "3 more") — Latvian does not.

- ❌ "4 citu" (bare genitive, no noun) → ✅ "vēl 4 modeļi" / "4 citi modeļi"
- ❌ "un 3 vairāk" → ✅ "un vēl 3 faili" / "un 3 papildu"

## Pronouns and Possessives

| English | Formal (Jūs) | Informal (tu) |
|---|---|---|
| you (subj) | Jūs | tu |
| your (poss) | jūsu | tavs (masc) / tava (fem) — declines like adjective |
| Imperative ending | -**iet** / -**jiet** (Saglabājiet, Noklikšķiniet) | base / -**i** (Saglabā, Noklikšķini) |

**Decline `tavs`:**
- Masc: tavs fails / tava faila / tavam failam / tavu failu / ar tavu failu / tavā failā
- Fem: tava lieta / tavas lietas / tavai lietai / tavu lietu / ar tavu lietu / tavā lietā

`jūsu` is invariable in form (does NOT decline).

## UI Conventions

### Button Labels — Infinitive Form

Latvian buttons use the **infinitive**, NOT the imperative or nominalization:

| Wrong | Correct | English |
|---|---|---|
| Saglabājiet (imperative) | **Saglabāt** | Save |
| Saglabāšana (nominalization) | **Saglabāt** | Save |
| Dzēsiet | **Dzēst** | Delete |
| Sūtiet | **Sūtīt** | Send |
| Atceliet | **Atcelt** | Cancel |
| Atlasiet | **Atlasīt** | Select |

### Status Messages — Impersonal / 3rd Person

Use **active 3rd person** or **impersonal passive** with `tiek + participle` — NOT "Mēs analizējam...":

| Wrong | Correct | English |
|---|---|---|
| Mēs analizējam... | **Analizē... / Tiek analizēts...** | Analyzing... |
| Sistēma ielādē | **Ielādē... / Tiek ielādēts...** | Loading... |
| Mēs saglabājam jūsu darbu | **Saglabā darbu... / Tiek saglabāts...** | Saving your work... |

### Bulk Action Buttons — Use "visu" (accusative)

```
✅ Atlasīt visu          (Select All)
✅ Noņemt visu atlasi    (Deselect All)
✅ Notīrīt visu          (Clear All)
❌ Atlasīt visus         (implies "all people", not "everything")
❌ Atlasīt visu atlasi   (redundant)
```

### Drag-and-Drop Vocabulary

- **vilkt** = drag
- **nomest** = drop
- ❌ "atlaist" = release/liberate — **wrong meaning**

```
✅ Velciet failus šurp                       (drag files here)
✅ Ievelciet un nometiet failus šeit         (drag and drop files here)
❌ Nometiet savus failus šeit                (drop-only — feels incomplete)
❌ Atlaidiet failu šeit                       (atlaist = release, not drop)
```

### File Picker / Placeholder Handling

Avoid putting the placeholder in a case-marked position — restructure:

- ❌ "{name} failam" (case on placeholder) → ✅ "**Failam {name}**" / "**Fails ar nosaukumu {name}**"
- ❌ "Atbalsts {formatList} failiem" → ✅ "**Atbalstīti {formatList} faili / formāti**" (participle over noun+dative)

### Definite vs Indefinite Adjective in UI

For non-specific general reference, use the **indefinite** form (jauns fails). The definite form (jaunais fails, ending -ais masc / -ā fem) is for specific/already-mentioned referents.

- General: "Saglabāt kā **jaunu** failu" (save as a new file)
- Specific: "Atvērt **jauno** failu" (open the new file [the specific one])

UI text predominantly uses indefinite.

## Punctuation, Numbers, Dates, Currency

### Quotation Marks
- **Latvian uses German-style low-high quotes: `„...."`** (the closing is high-right, like English close-quote)
- ❌ "English quotes" → ✅ „Latviešu pēdiņas"
- Severity 0.5 (cosmetic but expected in polished text)

### Numbers
- Decimal separator: **comma** (1**,**5)
- Thousands separator: **space** (1 234,56)
- ❌ 1,234.56 → ✅ 1 234,56

### Dates
- **Numeric**: DD.MM.YYYY → 15.01.2024
- **Long form**: "2024. gada 15. janvāris" (months **lowercase**)
- Year takes the construction: `2024. gada` (genitive: "of 2024")

### Time
- 24-hour: 14:30 or `plkst. 14:30` (plkst. = pulkstenis = "o'clock")

### Currency: EUR (since 2014)
- **Latvia adopted the euro on 2014-01-01.** Symbol after amount.
- Format: `99,99 €` / `1 234,56 €`
- Pre-2014 currency was lats (Ls) — should NOT appear in new UI.

### Comma Rules

**NO comma before coordinating conjunctions:**
- vai (or), un (and), un arī (and also)
- ❌ "Saglabājiet, un aizveriet" → ✅ "Saglabājiet un aizveriet"
- Exception: comma DOES precede `bet` / `taču` (but)

**ALWAYS comma before subordinating conjunctions:**
- ka (that): "Redzu, ka fails ir atvērts"
- kas / kurš / kura (which/who): "Fails, kuru izvēlējāties"
- ja (if): "Noklikšķiniet, ja vēlaties turpināt"
- jo / tāpēc ka (because): "Nedarbojas, jo fails nav atrasts"
- kad (when): "Sniegt paziņojumu, kad tiek pabeigts"

## Terminology

| English | Preferred Latvian | Avoid |
|---|---|---|
| Click | noklikšķināt | klikšķēt (anglicism) |
| Settings | iestatījumi | — |
| User | lietotājs | — |
| Delete | dzēst | — |
| Save | saglabāt | — |
| Upload | augšupielādēt | uploadēt |
| Download | lejupielādēt | downloadēt |
| Log in | pieslēgties | — |
| Log out | atslēgties | — |
| File | fails | — |
| Folder | mape | — |
| Dashboard | vadības panelis | — |
| Account | konts | — |
| Email | e-pasts | e-meils |
| Browser | pārlūkprogramma / pārlūks | brauzers |
| Link | saite | — |
| Password | parole | — |
| Search | meklēt / meklēšana | — |

**Proper noun abbreviations in UI:**
- ✅ "ASV" (NOT "Amerikas Savienotās Valstis" in cramped UI)
- ✅ "ES" (Eiropas Savienība — European Union)

**Brand names** remain undeclined. Take gender of implied noun (OneSky platforma = fem, OneSky rīks = masc) or default to masculine.

## Calque / Anti-Pattern Blocklist

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| Tas rada jēgu | **Tam ir jēga / Tas ir loģiski** | "makes sense" |
| darīt jēgu | **būt jēgai / ir loģiski** | "make sense" |
| Dienas beigās | **Galu galā / Kopumā** | "at the end of the day" |
| būt drošā pusē | **drošības pēc / lai būtu droši** | "be on the safe side" |
| mēri divreiz, griez vienreiz | **septiņreiz nomēri, vienreiz nogriez** | "measure twice, cut once" (Latvian uses 7, not 2) |
| Salauz kāju (literal) | **Lai veicas!** | "break a leg" |
| lietotāja-draudzīgs | **ērts lietotājam / lietotājam draudzīgs** | "user-friendly" |
| mākoņa-bāzēts | **mākonī bāzēts / mākoņpakalpojums** | "cloud-based" |
| konteksta apzināts | **kontekstu izprotošs / kontekstuāls** | "context-aware" |
| AI-darbināts | **ar mākslīgā intelekta atbalstu / izmantojot mākslīgo intelektu** | "AI-powered" |
| datu vadīts | **balstīts uz datiem / datu balstīts** | "data-driven" |
| downloadēt | **lejupielādēt** | direct anglicism |
| uploadēt | **augšupielādēt** | direct anglicism |
| e-meils | **e-pasts** | direct anglicism |

## "priekš" Colloquialism Warning (severity 1.5)

In professional/UI text, `priekš + genitive` (meaning "for whom/what") is **colloquial** and should be replaced with the **dative case** (no preposition):

| Colloquial (avoid) | Formal (preferred) |
|---|---|
| ❌ priekš lietotāja | ✅ **lietotājam** |
| ❌ priekš faila | ✅ **failam** |
| ❌ iestatījumi priekš konta | ✅ **konta iestatījumi** / iestatījumi kontam |
| ❌ priekš jums | ✅ **jums** |

`priekš` IS acceptable for:
- Temporal: `priekš vakariņām` (before dinner)
- Fixed idioms

## Tense and Aspect

Latvian preserves **present continuous** with present tense (no separate continuous form):

| English | Wrong | Correct |
|---|---|---|
| "we are building" | mēs uzbūvējām (past perf) | **mēs būvējam** (present) |
| "costs are increasing" | izmaksas pieauga (past) | **izmaksas pieaug** (present) |
| "I have been working here for 5 years" | Es strādāju šeit 5 gadus (just past) | **Es šeit strādāju jau 5 gadus** (ongoing marker `jau`) |

For "have been doing X for Y" use the ongoing marker `jau` (already) to convey continuity.

## Polysemous Word Disambiguation

| English (domain) | Correct Latvian | Wrong sense |
|---|---|---|
| scale (IT scalability) | **mērogošana / paplašināšana** | mērogs (measurement scale) |
| deploy (software) | **izvietot / nodot ekspluatācijā** | izvietot (military) |
| resume (verb, continue) | **atsākt / turpināt** | CV (only if document) |
| resume (noun, document) | **CV** | atsākt (only if verb) |
| copy (marketing text) | **teksts / reklāmas teksts** | kopija (photocopy) |
| bug (defect) | **kļūda** | kukainis (insect) |
| pipeline (CI/CD) | **konveijers / pipeline** | caurule (plumbing) |

Check domain context — first dictionary definition is often the wrong one.

## Self-Check Checklist

Run BEFORE finalizing each translation:

**Accuracy (critical):**
- [ ] **Gender agreement:** -s/-š/-is = masc, -a/-e = fem; adjectives match
- [ ] **Case correct:** 6 cases; locative for "in", accusative after uz/par/ar
- [ ] **Adjective agreement:** gender + number + case all three
- [ ] **Number-noun case:** 1=nom.sg, 2-9=nom.pl, 10-20=gen.pl
- [ ] **Relative pronoun:** kurš (masc) / kura (fem) matches antecedent
- [ ] **Verb-governed case:** palīdzēt→dat, vajadzēt→gen, gaidīt→acc
- [ ] **Preposition case:** ar→acc, no/bez→gen, uz→acc (motion) or loc (no prep, location)
- [ ] **Diacritics preserved:** all ā č ē ģ ī ķ ļ ņ š ū ž present
- [ ] **Reflexive -ties verbs** correctly conjugated (pieslēdzos, not pieslēdzu)
- [ ] **Placeholders preserved** exactly
- [ ] **ICU plural cases:** zero=gen.pl (failu), one=nom.sg (fails), other=nom.pl (faili)
- [ ] **Quotation marks:** „..." not "..."
- [ ] **Number format:** 1 234,56 (space + comma)
- [ ] **Conjunction commas:** no comma before vai/un; comma before ka/kas/kurš/ja/jo
- [ ] **Date format:** DD.MM.YYYY or "2024. gada 15. janvāris"
- [ ] **Currency:** 99,99 € (comma decimal, € after amount)

**Naturalness:**
- [ ] **Jūs/tu consistency** — possessives, verbs, imperatives all same level
- [ ] **Register matches source tone** — casual source → tu-form, not Jūs-form
- [ ] **No "priekš + gen"** for "for" — use dative
- [ ] **Buttons in infinitive** (Saglabāt, not Saglabājiet)
- [ ] **Status in 3rd person/impersonal** (Ielādē / Tiek ielādēts, not Mēs ielādējam)
- [ ] **"visu" pattern for bulk actions** (Atlasīt visu)
- [ ] **vilkt/nomest** for drag-and-drop (NOT atlaist)
- [ ] **Native vocabulary** (lejupielādēt, e-pasts — not downloadēt, e-meils)
- [ ] **No hyphenated calques** (X-aware, X-powered, X-driven, user-friendly)
- [ ] **Abbreviations in UI** (ASV, ES — not full forms in cramped space)
- [ ] **Ellipsis completed** — explicit noun after numbers (vēl 4 modeļi)

## Worked Examples

### Example 1 — Save button + status

**Source:**
> Save  
> Saving your changes...  
> Changes saved.

**Wrong:**
> Saglabājiet (imperative)  
> Mēs saglabājam jūsu izmaiņas...  
> Izmaiņas tika saglabājis. (wrong participle gender)

**Correct:**
> **Saglabāt** (infinitive button)  
> **Saglabā izmaiņas... / Tiek saglabātas izmaiņas...** (impersonal)  
> **Izmaiņas saglabātas.** (fem.pl participle agreeing with izmaiņas)

### Example 2 — Files counter with ICU

**Source:**
> {count, plural, =0 {No files} one {# file} other {# files}}

**Correct Latvian ICU:**
```
{count, plural,
  zero {# failu}
  one {# fails}
  other {# faili}
}
```

Reasoning: zero=genitive plural (failu), one=nominative singular (fails), other=nominative plural (faili).

### Example 3 — Drag-and-drop area

**Source:**
> Drag and drop files here, or click to browse

**Wrong:**
> Nometiet failus šeit, vai noklikšķiniet, lai pārlūkotu (drop-only; comma before vai)

**Correct:**
> **Ievelciet un nometiet failus šeit vai noklikšķiniet, lai pārlūkotu** (no comma before vai; comma before lai-clause)

### Example 4 — Casual register

**Source (casual blog):**
> "Look, here's the thing — my kids find this hilarious."

**Wrong (over-formal):**
> "Klausieties, lieta ir šāda — mani bērni to uzskata par ārkārtīgi smieklīgu." (formal imperative, formal noun construction)

**Correct (matching casual register):**
> **"Klau, lieta ir tāda — maniem bērniem tas šķiet neprātīgi smieklīgi."** (casual conversational opener, natural dative construction)

### Example 5 — "priekš" colloquialism

**Source:**
> Settings for your account

**Wrong (colloquial):**
> Iestatījumi priekš jūsu konta

**Correct (dative):**
> **Konta iestatījumi** / **Jūsu konta iestatījumi** / **Iestatījumi kontam**

### Example 6 — Bulk action

**Source:**
> Select All

**Wrong:**
> Atlasīt visus (implies "all people") / Atlasīt visu atlasi (redundant)

**Correct:**
> **Atlasīt visu** (compact accusative)

### Example 7 — Number+case in counted nouns

**Source:**
> 1 file uploaded  
> 5 files uploaded  
> 12 files uploaded

**Correct:**
> 1 fails augšupielādēts ← nom.sg + masc.sg participle  
> 5 faili augšupielādēti ← nom.pl + masc.pl participle  
> 12 failu augšupielādēti ← gen.pl + (participle still agrees with the nominal subject in the broader phrase, but for "12 files" the noun is gen.pl)

### Example 8 — Relative pronoun gender

**Source:**
> The system that supports multiple languages

**Wrong:**
> Sistēma, kurš atbalsta vairākas valodas (kurš is masculine; sistēma is feminine)

**Correct:**
> **Sistēma, kura atbalsta vairākas valodas** (kura matches feminine sistēma)

## When in Doubt

1. **Diacritic uncertain?** Default to the form with macron/cedilla/háček — Latvian rarely has unmarked forms where marked exists. Look up `iestatījumi`, not `iestatijumi`.
2. **Case unclear?** Re-read the preposition or verb governing the noun. Lookup table:
   - ar (with) → accusative
   - no, bez, dēļ, līdz, pie, pēc → genitive
   - uz, caur, par, pret, ap, pa → accusative
   - palīdzēt, pateikties → dative object
   - vajadzēt → genitive object
3. **Gender unclear?** Look at the ending. -s/-š/-is/-us → masc. -a/-e → fem. (A few -is nouns are feminine — sirds (heart), zivs (fish) — but rare in UI.)
4. **Register unclear?** Default to Jūs-form ONLY for product UI / errors / docs. For everything else, check source tone signals.
5. **Number+case unclear?** Use the table: 1/21/31 = nom.sg, 2-9/22-29 = nom.pl, 0/10-20 = gen.pl.
6. **ICU branch unclear?** zero=gen.pl, one=nom.sg, other=nom.pl. Memorize this.
7. **Want to use "priekš"?** Almost always wrong. Use dative instead.
8. **Compound adjective with hyphen?** Almost always wrong. Restructure with preposition or participle.

Latvian is a Baltic language with a rich case system. When the translation feels stiff, the cause is usually one of: wrong case, wrong gender agreement, calque from English, or `priekš` colloquialism. Fix the structure, don't just swap synonyms.
