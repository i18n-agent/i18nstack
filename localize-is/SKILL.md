---
name: localize-is
description: Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Icelandic (is). Icelandic enforces EXTREME language purism — virtually every modern concept has a native-coined word (tölva for computer, sími for telephone, vafri for browser, tölvupóstur for email, hugbúnaður for software, lykilorð for password). The Icelandic Language Committee actively coins replacements; loanwords like "kompjúter / klikka / seiva / deleta / updatea" are strongly rejected. Also enforces ð/þ preservation (eth/thorn — never replace with d/th), æ/ö preservation, 4-case grammar (Nom/Acc/Dat/Gen) with preposition-governed case, 3-gender system with strong/weak adjective declension, suffixed definite articles that decline (hesturinn/hestinn/hestinum), V2 word order, verb conjugation by person (Icelandic conjugates by person unlike other Scandinavian), þú-only formality (þér archaic), CZK currency wait — no, ISK króna with NO decimals (9.999 kr.), DD.MM.YYYY dates, comma decimals, NO comma before eða/og.
---

# Translate to Icelandic (is) — High-Fidelity Skill

## Scope & Variants

Icelandic is a single standard target — Modern Icelandic (íslenska). There are no significant regional dialects, no diglossia. The Icelandic Language Committee (Íslensk málnefnd) actively coordinates national standardization.

| Locale | Notes |
|--------|-------|
| `is` / `is-IS` | Standard Icelandic (Iceland). Default and only target. |

**Practical reality:** Icelandic translation has one target. The defining quality concern is **extreme language purism** — Iceland actively coins native Icelandic words for new technological concepts and aggressively rejects loanwords. This is not a stylistic preference; it is national policy supported by both the government's Language Committee and a strong cultural consensus among speakers.

### Icelandic is a conservative North Germanic language

Icelandic is the closest modern descendant of Old Norse. It retains:
- The full **4-case system** (Nom/Acc/Dat/Gen) that other Scandinavian languages mostly lost.
- **Three genders** with strong/weak adjective declension.
- **Verb conjugation by person** (unlike Swedish/Norwegian/Danish where verbs have one form for all persons).
- **Suffixed definite articles** that decline by case (hesturinn → hestinn → hestinum → hestsins).
- Letters lost in most modern Latin-script languages: **ð (eth)** and **þ (thorn)**.

This means Icelandic translation requires substantially more grammatical precision than Norwegian/Swedish/Danish.

---

## Register Auto-Detection (Apply Before Translating)

Modern Icelandic uses **`þú` universally** — the formal `þér` is archaic and used only in ceremonial/legal contexts (less than 1% of usage). Even Iceland's president is addressed as `þú`.

Auto-detect from source:

| Source signal | Target register |
|---------------|-----------------|
| Casual / conversational / personal | **Casual þú** — direct verbs, short sentences. Possessive `þinn / þín / þitt` (lowercase). |
| Neutral product UI / docs (DEFAULT) | **Neutral þú** — þú throughout, imperative buttons, present-tense status. |
| Legal / banking / government | **Formal þú** — still `þú` (NEVER `þér` in modern UI), but use full constructions, prefer impersonal passives, careful native vocabulary. |

**Hard rule: NEVER use `þér` in modern Icelandic UI.** Even banking and government use `þú`.

**Hard rule: source register matching for vocabulary** — Icelandic has both common-register and literary-register vocabulary. Match the source — don't elevate a casual English `stay` to a literary Icelandic equivalent.

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. EXTREME language purism — anglicisms strongly rejected (severity 2.5)

Icelandic is **the most purist major European language** for IT terminology. The Icelandic Language Committee has coined native Icelandic words for every common tech concept, and these are the **expected and required** terms in Icelandic UI:

| English | ✓ Icelandic native (REQUIRED) | ✗ Anglicism / loanword (REJECTED) |
|---------|-------------------------------|-----------------------------------|
| computer | **tölva** ("number-prophetess" — Halldór Halldórsson's 1965 coinage) | kompjúter, computer |
| telephone | **sími** (from Old Norse "thread") | telefón |
| television | **sjónvarp** (literally "sight-throw") | televísjón, TV |
| email | **tölvupóstur** ("computer-mail") | email, emaila |
| software | **hugbúnaður** ("mind-equipment") | software |
| hardware | **vélbúnaður** ("machine-equipment") | hardware |
| browser | **vafri** ("wanderer") | browser |
| website | **vefsíða** ("web-page") OR **vefur** | website |
| internet | **internetið** OR **veraldarvefurinn** ("world-wide-web") | (internet acceptable) |
| keyboard | **lyklaborð** ("keys-board") | keyboard |
| mouse | **mús** (native word reused) | mouse |
| screen | **skjár** | screen |
| password | **lykilorð** ("key-word") | password |
| file | **skrá** | file |
| folder | **mappa** (from "map") | folder |
| user | **notandi** | user |
| settings | **stillingar** | settings |
| dashboard | **yfirlit** ("overview") | dashboard |
| account | **reikningur** | account |
| video | **myndband** ("picture-band") | video |
| photo | **mynd** | foto |
| download (v.) | **hlaða niður** ("load down") | downloada |
| upload (v.) | **hlaða upp** ("load up") | uploada |
| click (v.) | **smella** | klikka |
| save (v.) | **vista** | seiva |
| delete (v.) | **eyða** | deleta |
| update (v.) | **uppfæra** | updatea |
| log in | **skrá sig inn** | logga, logga inn |
| log out | **skrá sig út** | logga út |
| select (v.) | **velja** | selekta |
| cancel (v.) | **hætta við** ("stop with") | kansella |
| search (v.) | **leita** | sörtsa |
| share (v.) | **deila** | sjera |

**Hard rule: ALL "verb-with-Icelandic-suffix-on-English-root" forms are rejected** by Icelandic users. `klikka, deleta, seiva, updatea, uploada, downloada, sörtsa, sjera, logga` — all WRONG. Use the native verb.

A small set of established loanwords IS accepted:
- `app` (also `forrit`) — both used
- `internet` (alongside `internetið`)
- `wifi` (also `þráðlaust net`)
- `cookie` (in tech contexts; `vafrakaka` is the formal term)
- Brand names: Google, Microsoft, Apple, GitHub — stay as-is.

But for the COMMON verbs and nouns above, native Icelandic is required.

### 2. ð (eth) and þ (thorn) preservation (severity 2.5)

Icelandic uses two letters that no other major modern language uses:
- **ð** (eth, voiced /ð/ as in English "this") — appears in middle/end of words. NEVER replace with `d`.
- **þ** (thorn, unvoiced /θ/ as in English "thin") — appears at start of words. NEVER replace with `th`.

| ✗ Stripped to ASCII | ✓ Correct |
|---------------------|-----------|
| madur | **maður** (man) |
| tholinmaedi | **þolinmæði** (patience) |
| islenska | **íslenska** (Icelandic) |
| thessi | **þessi** (this) |
| hladu nidur | **hlaða niður** (download — `ð` in `hlaða`) |
| sidan | **síðan** (the page) |
| theta er | **þetta er** (this is) |
| vidmot | **viðmót** (interface) |

Note: **ð never appears at start of a word** (Old Norse phonotactic constraint). Word-initial `þ` ONLY. Mid/end words can have `ð`.

### 3. æ and ö preservation (severity 2.0)

In addition to ð and þ, Icelandic uses **æ** (the æ ligature, /ai/ sound) and **ö** (umlauted o, /œ/ sound):

| ✗ Stripped | ✓ Correct |
|------------|-----------|
| baeta | **bæta** |
| haetta | **hætta** |
| broker → broker | (loanword keeps brokering) |
| forrit / kerfid | (no æ/ö in this example, just illustrating) |
| sjonvarp | **sjónvarp** |
| toluvert | **töluvert** |

Other diacritics: `á é í ó ú ý` (acute-marked long vowels). All essential.

### 4. Word integrity — compound words written as one (severity 2.0)

Icelandic forms compound words by concatenation. Splitting them changes meaning or produces nonsense.

| ✗ Wrong (split) | ✓ Correct (joined) | English |
|-----------------|---------------------|---------|
| `gagna grunnur` | **`gagnagrunnur`** | database |
| `notanda viðmót` | **`notandaviðmót`** | user interface |
| `lykil orð` | **`lykilorð`** | password |
| `tölvu póstur` | **`tölvupóstur`** | email |
| `hug búnaður` | **`hugbúnaður`** | software |
| `vef síða` | **`vefsíða`** | website |
| `lykla borð` | **`lyklaborð`** | keyboard |

**Compound gender rule:** the gender of an Icelandic compound is the gender of the **LAST element**. `gagnagrunnur` is masculine (because `grunnur` = base is masculine), `tölvupóstur` is masculine, `notandaviðmót` is neuter (because `viðmót` is neuter).

### 5. Four-case system (severity 2.5)

Icelandic retains all 4 cases from Old Norse. Cases are: **nefnifall (Nom), þolfall (Acc), þágufall (Dat), eignarfall (Gen)**.

| Case | Question | Use | Example (m. "hestur" — horse) | Example (f. "skrá") |
|------|----------|-----|-------------------------------|---------------------|
| Nom | hver? hvað? | Subject | hestur | skrá |
| Acc | um hvern? hvað? | Direct object | hest | skrá |
| Dat | frá hverjum? hverju? | Indirect object, with many preps | hesti | skrá |
| Gen | til hvers? hvers? | Possession, with some preps | hests | skrár |

Definite forms add the suffixed article and continue to decline:
- Indef.: hestur — hest — hesti — hests
- Def.: hesturinn — hestinn — hestinum — hestsins

(That's 8 forms for one noun across 2 numbers × 4 cases × 2 (def/indef) = 16 forms total per noun. Icelandic is very inflected.)

### 6. Preposition-governed case (severity 2.5)

Each preposition governs a specific case. Wrong case = critical error.

**Accusative (Acc) prepositions:**
- um (about, around): `um kerfið`
- gegnum (through): `gegnum vafrann`
- kringum (around): —

**Dative (Dat) prepositions (most common):**
- frá (from): `frá notandanum` (dat. of "notandinn")
- með (with): `með kerfinu` (NOT `með kerfið`)
- af (off, from): `af síðunni`
- úr (out of): `úr möppunni`
- að (to/at): `að notandanum`

**Genitive (Gen) prepositions:**
- til (to): `til þess` (NOT `til það`)
- vegna (because of): `vegna villu`
- milli (between): `milli skrár og möppu`

**Two-case prepositions (Acc vs Dat by motion):**
- **í (in / into)**:
  - Motion INTO → ACC: `í kerfið` (into the system)
  - Location IN → DAT: `í kerfinu` (in the system)
- **á (on / onto)**:
  - Motion ONTO → ACC: `á skjáinn` (onto the screen)
  - Location ON → DAT: `á skjánum` (on the screen)

**Critical UI errors to avoid:**

| ✗ Wrong | ✓ Correct | Reason |
|---------|-----------|--------|
| með það kerfi | **með því kerfi** | dat. after `með` |
| frá það | **frá því** | dat. after `frá` |
| til það | **til þess** | gen. after `til` |
| í kerfinu (motion sense) | **í kerfið** | acc. for motion INTO |
| í kerfið (location sense) | **í kerfinu** | dat. for location IN |

### 7. Definite article suffixes that decline (severity 2.0)

Icelandic has **no separate definite article word** (unlike English "the"). Instead, the definite article is suffixed to the noun AND it declines by case.

| Gender | Indef. Nom | Def. Nom | Def. Acc | Def. Dat | Def. Gen |
|--------|------------|----------|----------|----------|----------|
| Masc. (hestur — horse) | hestur | hesturinn | hestinn | hestinum | hestsins |
| Fem. (kona — woman) | kona | konan | konuna | konunni | konunnar |
| Neut. (barn — child) | barn | barnið | barnið | barninu | barnsins |

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| hesturinn (in accusative) | **hestinn** |
| barnið (in dative) | **barninu** |
| konan (in genitive) | **konunnar** |

This is uniquely difficult among Western European languages — the article suffix isn't just a marker, it inflects.

### 8. Adjective declension — strong vs weak (severity 2.0)

Icelandic adjectives have **two declension classes**:
- **Strong** (indefinite, predicative): used when noun is indefinite or adj. is predicative.
  - `nýtt kerfi` (a new system) — strong neuter indef.
  - `kerfið er nýtt` (the system is new) — strong predicative.
- **Weak** (definite, with article): used when noun is definite.
  - `nýja kerfið` (the new system) — weak.

Wrong choice = critical error:

| ✗ Wrong | ✓ Correct | Why |
|---------|-----------|-----|
| stór vandamálið | **stóra vandamálið** | def. noun needs weak adj |
| nýtt kerfið | **nýja kerfið** | def. needs weak |
| nýja kerfi | **nýtt kerfi** | indef. needs strong |
| góður dagurinn | **góði dagurinn** | def. weak |

### 9. Verb conjugation by person (severity 2.0)

UNLIKE Swedish/Norwegian/Danish (where verbs have ONE form for all persons), Icelandic verbs **conjugate by person and number**.

Example: `vista` (to save)

| Person | Form (present) | Form (past) |
|--------|----------------|-------------|
| ég (I) | vista | vistaði |
| þú (you sg.) | vistar | vistaðir |
| hann/hún/það (he/she/it) | vistar | vistaði |
| við (we) | vistum | vistuðum |
| þið (you pl.) | vistið | vistuðuð |
| þeir/þær/þau (they) | vista | vistuðu |

**UI critical**: `ég vista` ✓ (NOT `ég vistar`); `þú vistar` ✓ (NOT `þú vista`); `þið vistið` ✓.

### 10. V2 word order (severity 2.0)

Like other Scandinavian languages, Icelandic is **strict V2** — finite verb in position 2 of declarative main clauses.

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| Í dag notandinn vistar skrána | **Í dag vistar notandinn skrána** |
| Núna kerfið hleður gögn | **Núna hleður kerfið gögn** |
| Þegar þú smellir, þú sérð... | **Þegar þú smellir, sérðu...** (V2 after subordinate clause) |

### 11. Three-gender system (severity 2.0)

| Gender | Endings | Example | Article suffixes |
|--------|---------|---------|------------------|
| Masculine (karlkyn) | typically -ur, -i, -ir | hestur, vafri | -inn |
| Feminine (kvenkyn) | typically -a, -ur (some), consonant | skrá, mappa, kona, brú | -in |
| Neuter (hvorugkyn) | typically -a (some), -i (some), consonant | barn, kerfi, hús, viðmót | -ið |

| ✗ Wrong | ✓ Correct | Reason |
|---------|-----------|--------|
| sú kerfi | **það kerfi** | kerfi = neuter |
| það vafri | **sá vafri** | vafri = masc. |
| hinn skrá | **hin skrá** | skrá = fem. |

### 12. Past participle agreement (severity 2.0)

Past participles agree with subject in gender + number:

| Subject | Participle (e.g., "vistaður" — saved) |
|---------|----------------------------------------|
| m. sg. (`hesturinn`) | vistaður (`hesturinn er vistaður`) |
| f. sg. (`skráin`) | vistuð (`skráin er vistuð`) |
| n. sg. (`kerfið`) | vistað (`kerfið er vistað`) |
| m. pl. (`hestarnir`) | vistaðir |
| f. pl. (`skrárnar`) | vistaðar |
| n. pl. (`kerfin`) | vistuð |

`Skráin er vistað` ✗ → `Skráin er vistuð` ✓.

---

## Pronouns and Possessives

### Personal pronouns (decline by case!)

| English | Nom | Acc | Dat | Gen |
|---------|-----|-----|-----|-----|
| I | ég | mig | mér | mín |
| you (sg.) | **þú** | þig | þér | þín |
| he | hann | hann | honum | hans |
| she | hún | hana | henni | hennar |
| it (m.) | hann | hann | honum | hans |
| it (f.) | hún | hana | henni | hennar |
| it (n.) | það | það | því | þess |
| we | við | okkur | okkur | okkar |
| you (pl.) | þið | ykkur | ykkur | ykkar |
| they (m.) | þeir | þá | þeim | þeirra |
| they (f.) | þær | þær | þeim | þeirra |
| they (n.) | þau | þau | þeim | þeirra |

**Critical: pronouns decline.** `með þú` ✗ → `með þér` ✓ (dat. after `með`).

### Possessive pronouns

| English | m. | f. | n. |
|---------|-----|-----|-----|
| my | minn | mín | mitt |
| your sg. | þinn | þín | þitt |
| his | hans (invariable) | hans | hans |
| her | hennar (invariable) | hennar | hennar |
| our | okkar (invariable, or okkar declined) | okkar | okkar |
| your pl. | ykkar | ykkar | ykkar |
| their | þeirra | þeirra | þeirra |
| reflexive (own) | sinn | sín | sitt |

---

## UI Conventions

### Buttons — imperative (concise)

| English | ✓ Icelandic |
|---------|-------------|
| Save | **Vista** |
| Cancel | **Hætta við** (NOT `Kansella`) |
| Delete | **Eyða** |
| Send | **Senda** |
| Edit | **Breyta** |
| Search | **Leita** |
| Confirm | **Staðfesta** |
| Continue | **Halda áfram** |
| Submit | **Senda inn** |
| Sign in / Log in | **Skrá sig inn** |
| Sign out | **Skrá sig út** |
| Sign up | **Skrá sig** / **Búa til reikning** |
| Next | **Næsta** / **Áfram** |
| Back | **Til baka** |
| Done | **Lokið** / **Búið** |
| OK | **OK** / **Í lagi** |
| Close | **Loka** |
| Upload | **Hlaða upp** |
| Download | **Hlaða niður** |
| Refresh | **Uppfæra** |
| Settings | **Stillingar** |
| Apply | **Beita** |
| Reset | **Endurstilla** |
| Select all | **Velja allt** |
| Add more | **Bæta við** |

### Status messages — present tense + ellipsis

| English | ✓ Icelandic |
|---------|-------------|
| Loading… | **Hleður…** (3rd person sg present) |
| Saving… | **Vistar…** |
| Sending… | **Sendir…** |
| Processing… | **Vinnur úr…** / **Vinnur…** |
| Connecting… | **Tengir…** |
| Searching… | **Leitar…** |
| Translating… | **Þýðir…** |
| Please wait | **Vinsamlegast bíddu** / **Bíddu aðeins** |

### Completion messages — concise

| English | ✓ Icelandic |
|---------|-------------|
| Saved | **Vistað** / **Vistuð** (gender depends on subject) |
| Done | **Lokið** / **Búið** |
| Translation complete | **Þýðingu lokið** ("translation-DAT completed") |
| File uploaded | **Skrá hlaðin upp** ("file loaded up") |
| Sent | **Sent** |
| Payment successful | **Greiðsla tókst** / **Greitt** |

### Empty states — `Engar X` / `Ekkert X`

| ✗ Verbose | ✓ Concise |
|-----------|-----------|
| Engar niðurstöður fundust | **Engar niðurstöður** |
| Þú hefur engin verkefni ennþá | **Engin verkefni ennþá** |
| Það er ekkert hér | **Ekkert hér** |

### Drag-and-drop

- drag → **draga** (or imperative `Dragðu`)
- drop → **sleppa** (or imperative `Slepptu`) — NOT `losa` (= release/loosen, wrong sense)
- Combined: **`Dragðu skrár hingað`** (Drag files here) / **`Slepptu til að hlaða upp`** (Release to upload).

### File picker — `Velja` (native action verb)

| ✓ Icelandic |
|-------------|
| **Velja skrá** (Choose a file) |
| **Velja skrár** (Choose files) |
| **Smelltu til að velja** (Click to choose) |

### Quantity expressions

| ✗ Calque | ✓ Native |
|----------|----------|
| 25+ tungumál | **meira en 25 tungumál** |
| +{count} til viðbótar | **og {count} til viðbótar** |

### Error messages — what + next step

| ✗ Bare | ✓ With next step |
|--------|------------------|
| Skrá fannst ekki. | **Skrá fannst ekki. Athugaðu slóðina.** |
| Netvilla. | **Netvilla. Reyndu aftur.** |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Icelandic | Notes |
|------|-----------|-------|
| Question mark | `?` | Same as English |
| Comma | `,` | Different conjunction rules |
| Period | `.` | Same |
| Colon | `:` | Same |
| Quotation marks | **`„…"`** (gæsalappir — low-9 / high-9) | Same as German style |
| Apostrophe | only in foreign names | |

### Comma rules

| Rule | Example |
|------|---------|
| **NO comma** before `og` (and) | Veldu skrá **og** smelltu. |
| **NO comma** before `eða` (or) | Veldu skrá **eða** möppu. |
| **Comma** before `að` (that, subordinating) | Ég sé, **að** skráin er opin. |
| **Comma** before `sem` (relative — non-restrictive) | Skráin, **sem** var vistuð… |
| **Comma** before `ef` (if) | Vistaðu, **ef** þú vilt. |
| **Comma** before `því` (because) | Hætt við, **því** það mistókst. |
| **Comma** before `vegna þess að` (because) | Hætt við, **vegna þess að** það mistókst. |
| **Comma** before `en` (but) | Hratt, **en** skilvirkt. |

### Numbers

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **period (.)** | 1.234.567 |
| Decimal separator | **comma (,)** | 3,14 / 99,99 (rare for ISK) |
| Negative | `-25` | |
| Percent | `25 %` (with space) | |

### Dates

| Format | Example | Use |
|--------|---------|-----|
| DD.MM.YYYY | **15.01.2024** | Default Icelandic format |
| D. mánuður YYYY | **15. janúar 2024** | Long-form prose |
| YYYY-MM-DD | 2024-01-15 | Technical/API only |

**Icelandic month names (lowercase):**

| # | Icelandic |
|---|-----------|
| 1 | janúar |
| 2 | febrúar |
| 3 | mars |
| 4 | apríl |
| 5 | maí |
| 6 | júní |
| 7 | júlí |
| 8 | ágúst |
| 9 | september |
| 10 | október |
| 11 | nóvember |
| 12 | desember |

**Weekdays (lowercase):** mánudagur, þriðjudagur, miðvikudagur, fimmtudagur, föstudagur, laugardagur, sunnudagur.

Week starts **Monday**.

### Time

- 24-hour preferred: `14:30` or `kl. 14:30` (kl. = klukkan).

### Currency — Icelandic króna (ISK / kr.) — NO DECIMALS

| Format | Pattern | Example |
|--------|---------|---------|
| Symbol after amount | `kr.` (with period) | **9.999 kr.** |
| ISO code | ISK | **9.999 ISK** |

**CRITICAL: Icelandic króna has NO decimal subdivisions** (aurar were abolished in 2002). Always use whole numbers.

- ✗ `99,99 kr.` (decimals)
- ✗ `99.99 kr.` (English-style)
- ✓ `100 kr.` (whole numbers)
- ✓ `1.234 kr.` (period as thousands separator)
- ✓ `9.999 kr.` (large amounts more common in Iceland — ISK has low purchasing power, ~140 ISK = 1 USD)

Iceland is NOT in the eurozone (not even an EU member — Iceland is EEA). Never use EUR for Icelandic localization.

---

## Terminology — preferred Icelandic terms (PURIST)

| English | ✓ Icelandic (REQUIRED) | ✗ Avoid (anglicism) |
|---------|------------------------|----------------------|
| user | **notandi** | user |
| account | **reikningur** | akkáunt |
| password | **lykilorð** ("key-word") | password |
| settings | **stillingar** | settings |
| dashboard | **yfirlit** | dashboard |
| email | **tölvupóstur** | email, mejl |
| link | **tengill** | link |
| website | **vefsíða** | website |
| folder | **mappa** | folder |
| file | **skrá** | file |
| device | **tæki** | device |
| phone | **sími** | telefón |
| computer | **tölva** | kompjúter |
| application / app | **forrit** / app (accepted) | applikation |
| update (v.) | **uppfæra** | updatea |
| save | **vista** | seiva |
| delete | **eyða** | deleta |
| upload | **hlaða upp** | uploada |
| download | **hlaða niður** | downloada |
| sign in / log in | **skrá sig inn** | logga inn |
| sign up | **skrá sig** | — |
| search | **leita** | sörtsa |
| click | **smella** | klikka |
| share | **deila** | sjera |
| profile | **prófíll** (accepted loanword) / **persónusíða** | — |
| notifications | **tilkynningar** | — |
| privacy | **persónuvernd** ("person-protection") | privacy |
| terms | **skilmálar** | — |
| support | **stuðningur** | — |
| help | **hjálp** / **aðstoð** | — |
| feedback | **endurgjöf** | feedback |
| menu | **valmynd** ("choice-picture") | menu |
| home | **heim** / **upphafssíða** | home |
| **browser** | **vafri** | browser |
| **screen** | **skjár** | screen |
| **keyboard** | **lyklaborð** | keyboard |
| **mouse** | **mús** | mouse |
| **software** | **hugbúnaður** | software |
| **hardware** | **vélbúnaður** | hardware |
| **video** | **myndband** | video |
| **photo** | **mynd** / **ljósmynd** | foto |
| **window** | **gluggi** | — |
| **menu bar** | **valmyndastika** | — |
| **search bar** | **leitarstika** | — |
| **icon** | **tákn** | ikon |
| **error** | **villa** | error |
| **warning** | **viðvörun** | warning |
| **language** | **tungumál** ("tongue-thing") | — |
| **font** | **letur** / **leturgerð** | font |
| **size** | **stærð** | size |
| **color** | **litur** | color |
| build (software) | **byggja** / **smíða** | builda |
| deploy | **dreifa** / **setja upp** | deploya |
| pipeline (CI/CD) | pipeline (keep) | — |
| commit (git) | commit (keep) | — |
| merge (git) | **sameina** / merge (keep in code) | mergea |
| repository | **vörusöfn** (formal) / repository | — |
| sync | **samstilla** | — |
| API | API (keep — Latin always) | — |
| cache | **skyndiminni** / cache | — |
| log (n.) | **annáll** / **skrá** | — |
| URL | **vefslóð** ("web-trail") | — |
| WiFi | **þráðlaust net** ("wireless net") / WiFi | — |

### Tech identifiers — keep in Latin

Inside Icelandic text (Latin alphabet anyway), these stay as-is:
- Git, GitHub, Docker, npm, pip
- HTTP, REST, GraphQL, OAuth, JWT
- JSON, XML, YAML, CSV, PDF
- Brand names: Google, Microsoft, Apple, iPhone, Android
- Commands, paths, URLs, code, placeholders

---

## False Friends — Critical

| Icelandic word | Actually means | NOT this | Correct for the English |
|----------------|----------------|----------|--------------------------|
| **gift** | **poison** OR "married" | "gift" (present) | "gift" → **gjöf** |
| **fart** | speed / pace | (English meaning unrelated) | — |
| **bjór** | beer | (OK loanword) | — |
| **fjall** | mountain | — | — |
| `aktuelt` (if it appears) | current | "actual" | "actual" → **raunverulegt** |
| `eventuelt` | possibly | "eventually" | "eventually" → **að lokum** / **á endanum** |
| **álit** | opinion | "elite" | "elite" → **úrvalslið** |
| **bók** | book | (OK) | — |

The `gift = poison` false friend is the classic Icelandic translation trap.

---

## Calque / Anti-Pattern List

| ✗ Calque | ✓ Native Icelandic | Reason |
|----------|---------------------|--------|
| gerir skilning / Það gerir vit | **er skynsamlegt** / **það meikar sens** (colloquial only) | "Makes sense" calque |
| í lok dags | **þegar allt kemur til alls** | "At the end of the day" calque |
| Taka það á næsta stig | **Fara lengra** | "Take to next level" calque |
| Á sama blaðsíðu | **Sammála** / **Á sama máli** | "On the same page" calque |
| gera úrbætur | **bæta** | "Make improvements" — use verb |
| gefa svar | **svara** | "Provide an answer" — use verb |
| Fáðu þýðingu á nokkrum mínútum | **Þýðing á nokkrum mínútum** | "Get X done" structural calque |
| Haltu verkefnunum þínum samstilltum | **Tryggðu samstillingu verkefna** | "Keep X synced" calque |
| AI-knúið | **byggt á AI** / **knúið af AI** | "X-powered" calque |
| **klikka** | **smella** | Anglicism — use native verb |
| **deleta** | **eyða** | Anglicism |
| **seiva** | **vista** | Anglicism |
| **uploada** | **hlaða upp** | Anglicism |
| **downloada** | **hlaða niður** | Anglicism |
| **updatea** | **uppfæra** | Anglicism |
| **kompjúter** | **tölva** | Anglicism — use Iceland's national coinage |
| **email** | **tölvupóstur** | Anglicism — use native |

---

## Self-Check Checklist (Run Before Returning Output)

### Language purism (auto-fail on miss)

- [ ] **Native Icelandic terms used** for IT vocabulary: `tölva`, `sími`, `vafri`, `tölvupóstur`, `hugbúnaður`, `lyklaborð`, `notandi`, `stillingar`, `skrá`, `mappa`, `lykilorð`.
- [ ] **No anglicism-verb hybrids**: no `klikka`, `deleta`, `seiva`, `uploada`, `downloada`, `updatea`, `sörtsa`, `sjera`.
- [ ] **No raw anglicism nouns**: no `kompjúter`, `email`, `password`, `dashboard`, `browser`, `software` (unless explicitly part of a brand/product name).

### Special characters (auto-fail)

- [ ] **ð (eth)** present where required — never `d`. Examples: `maður`, `viðmót`, `síðan`, `hlaða niður`.
- [ ] **þ (thorn)** present where required (word-initially) — never `th`. Examples: `þetta`, `þú`, `þannig`, `þýðing`.
- [ ] **æ** present where required — never `ae`. Examples: `bæta`, `hætta`.
- [ ] **ö** present where required — never `o` or `oe`. Examples: `tölva`, `sjónvarp`.
- [ ] **á é í ó ú ý** acute-marked vowels preserved.

### Accuracy

- [ ] **Compound words written as one word** — no `gagna grunnur`, `tölvu póstur`.
- [ ] **Four-case system** correct — preposition-governed case respected.
- [ ] **i / á two-case prepositions**: ACC for motion, DAT for location.
- [ ] **Definite article suffix declines** by case (`hesturinn / hestinn / hestinum / hestsins`).
- [ ] **Strong vs weak adjective** correctly chosen (strong for indef./predicative, weak for def.).
- [ ] **Verb conjugation by person** correct (`ég vista`, `þú vistar`, `við vistum`, `þið vistið`).
- [ ] **V2 word order** in main clauses.
- [ ] **Past participle agreement** with subject gender/number (`skráin er vistuð`).
- [ ] **Gender (m/f/n)** correct on every article and adjective.
- [ ] **Pronoun case** correct (pronouns decline! `með þér`, `frá honum`, `til þess`).
- [ ] **Compound gender = last element** rule applied.
- [ ] **ICU plurals**: standard `one / other` for Icelandic.
- [ ] **Placeholders preserved**.
- [ ] **Numbers**: comma decimal, period thousands.
- [ ] **Dates**: DD.MM.YYYY.
- [ ] **Currency: ISK króna, NO decimals** — `9.999 kr.` not `99,99 kr.`.

### Register

- [ ] **þú throughout** — never `þér` (archaic).
- [ ] **Possessive matches**: `þinn / þín / þitt` consistently.

### UI conventions

- [ ] Buttons use imperative (`Vista`, `Eyða`, `Hætta við`).
- [ ] Status uses present + ellipsis (`Hleður…`, `Vistar…`).
- [ ] Completion concise (`Vistað`, `Þýðingu lokið`).
- [ ] Empty states concise (`Engar niðurstöður`).
- [ ] Drag-drop uses `Dragðu` + `Slepptu`.
- [ ] No comma before `og / eða`.
- [ ] Error messages include next step.

### Currency / Region

- [ ] **ISK (kr.) for Icelandic locale** — NEVER EUR (Iceland is not in eurozone, not even EU).
- [ ] **No decimals on ISK** — `100 kr.`, `1.234 kr.`, never `99,99 kr.`.

---

## Worked Example — Standard is UI

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** neutral product UI → casual þú, present-tense status, native Icelandic vocabulary.

**Translation:**

> Velkomin/n aftur! Þú ert með 3 nýjar skrár á reikningnum þínum. Smelltu á **Halda áfram** til að skoða þær eða **Hætta við** til að vera áfram hér. Vistar breytingarnar þínar…

**Why this works:**
- `Velkomin/n` — adjective participle (fem./masc. with slash for gender-neutral; or use masc. `Velkominn` if gender-neutral plural isn't possible here).
- `Þú ert með` — `þú` + 2nd-person sg. verb `ert` + `með` (with). Idiomatic Icelandic for "you have".
- `3 nýjar skrár` — `nýjar` f. pl. adj agreeing with `skrár` (f. pl. of `skrá`).
- `á reikningnum þínum` — `á` + DAT (location); `reikningnum` masc. dat. sg. definite suffix; `þínum` masc. dat. sg. possessive.
- Buttons: `Halda áfram`, `Hætta við` (native — NOT `Continue` / `Kansella`).
- `Smelltu` — 2nd-person sg. imperative of `smella` (native verb, NOT `klikka`).
- `til að skoða þær / til að vera áfram` — `til að + infinitive` construction (purpose).
- Status: `Vistar breytingarnar þínar…` — present tense `vistar` (3rd person sg. — system is doing). `breytingarnar` is f. pl. def. ACC; `þínar` agrees.
- ð and þ preserved.

---

## Worked Example — Anglicism rejection

**Source:** Click here to download the software update.

**✗ Wrong (anglicism-heavy):**

> Klikkaðu hér til að downloada software updatea.

**✓ Correct (native Icelandic):**

> Smelltu hér til að hlaða niður hugbúnaðaruppfærslunni.

Notes:
- `klikka` → `smella` ✓
- `downloada` → `hlaða niður` ✓
- `software` → `hugbúnaður` ✓
- `update` → `uppfærsla` (here in compound `hugbúnaðaruppfærsla` = "software-update")
- `hugbúnaðaruppfærslunni` is dative (after `hlaða niður` which takes dat. object).

---

## Worked Example — Currency (NO decimals)

**Source:** Subscription: 9.99 EUR / month.

**✗ Wrong:**

> Áskrift: 1.480,00 kr. á mánuði.

**✓ Correct (no decimals on ISK):**

> Áskrift: 1.480 kr. á mánuði.

(Period for thousands; no comma-decimals on Icelandic króna.)

---

## Worked Example — Case-governed prepositions

| English | ✓ Icelandic |
|---------|-------------|
| from the user | **frá notandanum** (dat.) |
| with the system | **með kerfinu** (dat.) |
| to (toward) the page | **að síðunni** (dat.) |
| into the system (motion) | **í kerfið** (acc.) |
| in the system (location) | **í kerfinu** (dat.) |
| onto the screen (motion) | **á skjáinn** (acc.) |
| on the screen (location) | **á skjánum** (dat.) |
| to (purpose) the user | **til notandans** (gen.) |
| about the user | **um notandann** (acc.) |

---

## When in Doubt

1. **Default to is, þú-form, native Icelandic vocabulary (no anglicisms), DD.MM.YYYY dates, ISK with no decimals.**
2. If you see an anglicism (`klikka`, `deleta`, `seiva`, `uploada`, `kompjúter`, `email`, `software`, `browser`) → **fix to native Icelandic** (`smella`, `eyða`, `vista`, `hlaða upp`, `tölva`, `tölvupóstur`, `hugbúnaður`, `vafri`).
3. If you stripped `ð` to `d` → **restore** (`maður`, not `madur`).
4. If you stripped `þ` to `th` → **restore** (`þetta`, not `thetta`).
5. If you stripped `æ` or `ö` → **restore** (`bæta`, `tölva`).
6. If you used `þér` for formal singular → **switch to `þú`** (þér is archaic).
7. If currency is € / EUR → **fix to kr. / ISK** (Iceland is not in eurozone).
8. If currency has decimals (`9.99 kr.`) → **remove decimals** (`100 kr.` — ISK has no aurar).
9. If a preposition + wrong case → **fix to governed case** (`með` → dat., `til` → gen., `frá` → dat.).
10. If you used `klika kerfið` instead of `kerfið` (wrong gender) → **fix** (`kerfi` is neuter → `það kerfi`).
11. If you split a compound (`gagna grunnur`) → **join it** (`gagnagrunnur`).
12. If verb conjugation is wrong (`ég vistar`) → **fix** (`ég vista`).
13. If you used English-style plural with no Icelandic plural form → **decline noun for number AND case**.
14. If strong/weak adjective mismatch → **fix** (`nýtt kerfið` ✗ → `nýja kerfið` ✓).
