---
name: localize-da
description: Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Danish (da). Enforces to genus (en/et) agreement, V2 word order with subordinate-clause inversion, double definiteness with adjective (det store hus), compound-word integrity (skrive sammen — separation is særskrivning error), du-form universality (De archaic), hybrid-compound verb rejection (no aflinke, afsynce — use frakoble, synkronisere), comma rules (no comma before eller/og, comma before men/at/når/fordi), present-tense status messages (Gemmer..., Indlæser...), æ/ø/å preservation, DKK currency (99,99 kr.), DD-MM-YYYY dates, and source-register matching.
---

# Translate to Danish (da) — High-Fidelity Skill

## Scope & Variants

Danish is a **single standard target** — Modern Standard Danish (rigsdansk). No significant regional split for product UI:

| Locale | Notes |
|--------|-------|
| `da` / `da-DK` | Standard Danish (Denmark). Default. |
| `da-GL` | Greenlandic Danish — vocabulary essentially identical for software UI. |
| `da-FO` | Faroese Danish — same. |

Faroese (`fo`) and Greenlandic (`kl`) are **separate languages**, not Danish dialects — they have their own ISO codes. Don't confuse them with Danish.

**Practical reality:** Danish translation has **one target**. Treat `da` as the universal target.

### Danish vs Norwegian Bokmål — distinct languages, often confused

Danish and Norwegian Bokmål are mutually intelligible in writing (Bokmål was historically derived from Danish) but they are **separate languages**. AI translators sometimes mix them. Key distinguishing features of Danish vs Bokmål:

| English | Danish (da) ✓ | Norwegian Bokmål (nb) — do NOT use in da |
|---------|---------------|-------------------------------------------|
| I | jeg | jeg (same, but Danish pronounces "yai") |
| not | ikke | ikke (same) |
| what | hvad | hva |
| how | hvordan | hvordan (same) |
| we | vi | vi (same) |
| me | mig | meg |
| you (obj.) | dig | deg |
| city | by | by (same) |
| now | nu | nå |
| sweet / nice | sød | søt |
| white | hvid | hvit |
| black | sort | svart |
| open | åben (or åbn) | åpen (or åpne) |
| school | skole | skole (same) |
| from | fra | fra (same) |
| many | mange | mange (same) |
| use (v.) | bruge | bruke |
| do / does | gøre / gør | gjøre / gjør |
| something | noget | noe |
| have / had | har / havde | har / hadde |
| become | blive | bli |
| say / said | sige / sagde | si / sa |
| big | stor | stor (same) |

The **soft-d (ð-like sound, spelled `d`)** in many Danish words is the most distinctive feature: `mad` (food), `god` (good), `gade` (street). Norwegian Bokmål has hard-d or no-d in equivalent positions.

**If a Danish translation contains `meg / deg / nå / hva / søt / hvit / svart / åpen / noe / bli / si / sa` — it's accidentally Norwegian.**

---

## Register Auto-Detection (Apply Before Translating)

Modern Danish, like Swedish and Norwegian, abandoned the formal `De` form. **`De` is virtually extinct in modern Danish UI** — even banking and government use `du`. Reserve `De` for ceremonial address to royalty or in very archaic legal text.

Auto-detect from source:

| Source signal | Target register |
|---------------|-----------------|
| Casual / conversational (`Hey!`, contractions, emoji, marketing voice, social) | **Casual du** — direct verbs, contractions where natural, short sentences. Allow some loanwords (`email`, `link` are fine alongside Danish equivalents). |
| Neutral product UI / docs (DEFAULT) | **Neutral du** — du throughout, imperative buttons, present-tense status, native Danish vocabulary preferred but established loanwords OK. |
| Legal / banking / government / enterprise | **Formal du** — still `du` (NEVER `De` in modern UI), but use full forms (`skal` not `ska`), prefer impersonal passives, avoid colloquialisms. |

**Hard rule: NEVER use `De` in modern Danish UI.** It's archaic. Even formal Danish government communication uses `du`.

**Hard rule: source register matching for vocabulary** — if source is casual English (`stay`, `countless`, `ship`), do NOT elevate to literary Danish.

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. Compound words written as ONE word — særskrivning is wrong (severity 2.5)

Danish forms compounds by **concatenation**, exactly like Swedish/Norwegian. Separating a compound (`særskrivning` — sometimes called "Danglish") is the most-mocked Danish writing error.

| ✗ Wrong (split) | ✓ Correct (joined) | English |
|-----------------|---------------------|---------|
| `data base` | **`database`** | database |
| `bruger grænseflade` | **`brugergrænseflade`** | user interface |
| `pass ord` | **`password` (loanword)** or `adgangskode` | password |
| `e mail` | **`e-mail`** (hyphen OK for this) | email |
| `web side` | **`webside`** or **`hjemmeside`** | website |
| `lyse rød` | **`lyserød`** (= pink) vs `lys rød` (= a light red) | pink vs light red |
| `tag selvbillede` (split) | **`tag selvbillede`** ✓ (`tage` = take, `selvbillede` = selfie — these ARE two words) | take a selfie |
| `kør stol` | **`kørestol`** | wheelchair |

**Hyphens** appear only in:
- Acronym + Danish word: `IT-firma`, `25-årig`.
- Compounds with brand/foreign words: `Google-konto`, `iPhone-en`.
- `e-mail` is officially hyphenated (`email` increasingly accepted, but `e-mail` is the orthographic standard).

### 2. Hybrid-compound verb anti-pattern — REJECT (severity 2.5)

Danish prefixes (`af-`, `fra-`, `ud-`, `op-`, `ind-`) onto English roots create non-words. **Always** find the dictionary-attested native form.

| ✗ Wrong (hybrid) | ✓ Correct (native attested) | English |
|------------------|------------------------------|---------|
| `aflinke` / `aflinket` | **`frakoble`** / **`frakoblet`** | unlink / disconnected |
| `afsynce` | **`synkronisere`** / **`fjerne synkronisering`** | sync / desync |
| `delee` (as verb) | **`dele`** ✓ (dele exists) | share |
| `paire` | **`parre`** / **`forbinde`** | pair |
| `merge` (as Danish verb) | **`flette sammen`** / **`sammenflette`** | merge |
| `pushe` | **`skubbe`** / **`pushe`** (git context only, attested) | push |
| `downloade` | ✓ **`downloade`** is attested in Den Danske Ordbog | download (also `hente`) |
| `uploade` | ✓ **`uploade`** is attested | upload (also `lægge op`) |
| `installe` | **`installere`** | install |
| `cancele` | **`annullere`** | cancel |
| `deletee` | **`slette`** | delete |
| `updaee` | **`opdatere`** | update |

**Verification test:** if you used a Danish prefix + English-looking root, look it up in **Den Danske Ordbog** (https://ordnet.dk/ddo) or **Retskrivningsordbogen** (Danish official orthography). If not found, replace with the native verb.

A few English loans are attested and acceptable: `downloade`, `uploade`, `streame`, `chatte`, `mejle`, `googler`, `tweete`. Their **hybrid prefixed forms generally are NOT** (no `afmejle`, `udchatte`, etc.).

### 3. Two-gender system — en (common) vs et (neuter) (severity 2.0)

Danish has two genders: **common (en, ~75%)** and **neuter (et, ~25%)**. There's no reliable phonological rule — gender must be memorized.

**Common IT nouns and their genders:**

| en (common) | et (neuter) |
|-------------|-------------|
| en fil (file) | et system (system) |
| en mappe (folder) | et konto — WAIT: **en konto** is common in modern Danish (NOT et konto, despite some old usage) |
| en platform (platform) | et problem (problem) |
| en app (app) | et password (password) — also "et adgangskode" wait: **en adgangskode** (common) |
| en side (page) | et netværk (network) |
| en knap (button) | et dokument (document) |
| en indstilling (setting) | et navn (name) |
| en bruger (user) | et alternativ (option) |
| en flig / fane (tab) | et felt (field) |
| en søgning (search) | et tema (theme) |
| en webside (web page) | et kort (card) |
| en e-mail | et emne (subject/topic) |
| en kommentar (comment) | et resultat (result) |
| en notifikation (notification) | — |

**Indefinite article**: en/et before the noun.
**Definite (without adjective)**: suffix `-en` (common) or `-et` (neuter). `filen`, `systemet`.
**Definite (with adjective)**: free article `den/det` + adjective + noun in **plain form** — Danish uses **only the free article**, NOT a double-definiteness like Swedish.

### 4. Double-definiteness DIFFERENCE from Swedish (severity 2.0)

This is a critical Danish-specific rule. Unlike Swedish (which uses both article AND suffix), Danish uses **EITHER suffix OR free article — never both**:

| ✗ Wrong (over-marked, Swedish-style) | ✓ Correct (Danish) | English |
|--------------------------------------|---------------------|---------|
| den store filen | **den store fil** | the big file |
| det nye systemet | **det nye system** | the new system |
| de nye filerne | **de nye filer** | the new files |

**Pattern:**
- No adjective → use suffix only: `filen`, `systemet`, `filerne`.
- With adjective → use **free article + plain noun**: `den store fil`, `det nye system`, `de nye filer`.

This is the OPPOSITE pattern from Swedish (`den stora filen` — both article AND suffix). Don't confuse them.

### 5. V2 word order (verb in position 2 of main clauses) (severity 2.0)

Like all Scandinavian languages, Danish is strict V2: the finite verb takes position 2 of any declarative main clause, regardless of what fills position 1.

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| I dag brugeren gemmer filen | **I dag gemmer brugeren filen** (Today saves the user the file) |
| Nu systemet indlæser data | **Nu indlæser systemet data** |
| Efter login du kan ændre... | **Efter login kan du ændre...** |
| Snart vi lancerer | **Snart lancerer vi** |

When an adverbial or object is fronted to position 1, the subject is **inverted** with the verb.

**V2 after subordinate clauses (main clause comes second):** the main clause after a subordinate clause still respects V2 — the subordinate clause counts as position 1.

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| Hvis du klikker her, du vil se... | **Hvis du klikker her, vil du se...** |
| Når filen gemmes, du får besked | **Når filen gemmes, får du besked** |

### 6. Subordinate clause word order — subject before verb (severity 1.5)

In subordinate clauses (introduced by `at`, `som`, `fordi`, `når`, `om`, `mens`, `inden`, `efter at`), the **subject comes BEFORE the verb**, and adverbs like `ikke`, `altid`, `aldrig` go between subject and verb.

| Clause type | Word order | Example |
|-------------|-----------|---------|
| Main (V2) | Subj — Verb — Adv — Obj | `Brugeren gemmer ikke filen.` |
| Subordinate (SVx) | Subj — Adv — Verb — Obj | `…fordi brugeren ikke gemmer filen.` |

### 7. Negation placement (severity 1.5)

| Context | Pattern | Example |
|---------|---------|---------|
| Main clause | Verb + ikke | `Filen gemmes ikke.` (The file is not saved.) |
| Subordinate clause | ikke + Verb | `…fordi filen ikke gemmes.` |

### 8. Adjective agreement (severity 1.5)

Three forms: **base / -t / -e**.

| Subject | Form | Example |
|---------|------|---------|
| en-noun (common) indefinite sg. | base | en **stor** fil |
| et-noun (neuter) indefinite sg. | -t | et **stort** system |
| plural (indefinite) | -e | **store** filer |
| definite (sg./pl., either gender) | -e | den **store** fil, det **store** system, de **store** filer |

Irregular: `lille` (small) → `lille` (neuter same) / `små` (plural).

### 9. Comma rules — `eller` / `og` vs `men` / `for` (severity 1.0)

Same pattern as Swedish/Norwegian:

| Rule | Example |
|------|---------|
| **NO comma** before `og` (and) | Træk hertil **og** klik. |
| **NO comma** before `eller` (or) | Træk hertil **eller** klik. |
| **NO comma** before `eller` (or, second use) | Vælg fil **eller** mappe. |
| **Comma** before `men` (but) | Hurtig, **men** effektiv. |
| **Comma** before `for` (because) | Annulleret, **for** det fejlede. |
| **Comma** before `at` (subordinating "that") | Jeg ser, **at** filen er åben. |
| **Comma** before `når / hvis / fordi / hvorfor` | Gem, **når** du er klar. |
| **Comma** before relative `som / der` (with care — see below) | Filen, **som** er gemt, ... |

**Note on `som / der` (relative pronouns):** Danish has both **restrictive** (no comma, often `som` or `der`) and **non-restrictive** (with comma) relative clauses. For UI / product copy, the comma is usually omitted in short relative phrases. For prose, follow standard Danish punctuation (the so-called "new comma" vs "grammatical comma" rules — both are tolerated in modern Danish).

### 10. Special characters æ ø å — NEVER strip (severity 3.0)

Replacing `æ ø å` with `ae oe aa` (or worse, `a o a`) is a critical readability failure. These are letters, not diacritics. `Gem` vs `Gem` is fine but `Vælg` → `Vaelg` and `Søg` → `Soeg` are broken.

A Danish product UI with `Adgangskode` → `Adgangskode` ✓ but `Søg` → `Sog` ✗.

### 11. ICU plurals — one / other (severity 1.5)

Danish has two CLDR plural categories: `one` (n = 1) and `other` (everything else).

```icu
{count, plural,
  one {# fil}
  other {# filer}
}
```

---

## Pronouns and Possessives

### Personal pronouns

| English | Danish | Notes |
|---------|--------|-------|
| I | jeg | |
| you (sg.) | **du** | NEVER `De` for singular formal (archaic) |
| you (pl.) | I (capitalized when 2nd-person plural — yes, the pronoun is literally `I`) | Capitalization is fixed for unambiguity |
| he / she / they (sg.) | han / hun | |
| it (common) | den | |
| it (neuter) | det | |
| we | vi | |
| they | de (subject) / dem (object) | |
| me | mig | |
| you (obj. sg.) | dig | |
| us | os | |
| them | dem | |

### Possessive (agree with possessed noun's gender/number)

| Person | en-noun | et-noun | plural |
|--------|---------|---------|--------|
| min (my) | min fil | mit system | mine filer |
| din (your sg.) | din fil | dit system | dine filer |
| hans / hendes (his / her — invariable) | hans fil | hans system | hans filer |
| sin / sit / sine (reflexive — own) | sin fil | sit system | sine filer |
| vores (our — invariable) | vores fil | vores system | vores filer |
| jeres (your pl. — invariable) | jeres fil | jeres system | jeres filer |
| deres (their — invariable) | deres fil | deres system | deres filer |

**Reflexive `sin / sit / sine`** is required when the possessor is the subject of the same clause:
- `Hun gemmer sin fil.` (She saves her own file.) ← reflexive
- `Hun gemmer hendes fil.` (She saves [someone else's] file.) ← non-reflexive

---

## UI Conventions

### Buttons — imperative (preferred)

| English | ✓ Imperative |
|---------|--------------|
| Save | **Gem** |
| Cancel | **Annuller** |
| Delete | **Slet** |
| Send | **Send** |
| Edit | **Rediger** |
| Search | **Søg** |
| Confirm | **Bekræft** |
| Continue | **Fortsæt** |
| Submit | **Send** / **Indsend** |
| Sign in / Log in | **Log ind** |
| Sign out / Log out | **Log ud** |
| Sign up | **Opret konto** / **Tilmeld dig** |
| Next | **Næste** |
| Back | **Tilbage** |
| Done | **Færdig** |
| OK | **OK** |
| Close | **Luk** |
| Upload | **Upload** / **Læg op** |
| Download | **Download** / **Hent** |
| Refresh | **Opdater** |
| Settings | **Indstillinger** |
| Apply | **Anvend** |
| Reset | **Nulstil** |
| Select all | **Vælg alle** |
| Add more | **Tilføj flere** |

### Status messages — present tense + ellipsis

| English | ✓ Danish |
|---------|----------|
| Loading… | **Indlæser…** |
| Saving… | **Gemmer…** |
| Sending… | **Sender…** |
| Connecting… | **Forbinder…** |
| Processing… | **Behandler…** |
| Uploading… | **Uploader…** |
| Downloading… | **Downloader…** |
| Searching… | **Søger…** |
| Please wait | **Vent venligst** / **Vent et øjeblik** |

### Completion messages — concise

| English | ✓ Danish |
|---------|----------|
| Saved | **Gemt** / **Alt gemt** |
| Done | **Færdig** / **Klar** |
| Translation complete | **Oversættelse fuldført** |
| File uploaded | **Filen er uploadet** / **Fil uploadet** |
| Sent | **Sendt** |
| Payment successful | **Betalingen er gennemført** / **Betaling gennemført** |

### Empty states — concise, drop pronouns

| ✗ Verbose | ✓ Concise |
|-----------|-----------|
| Der blev ikke fundet nogen resultater | **Ingen resultater** |
| Du har endnu ikke nogen projekter | **Ingen projekter endnu** |
| Der er ikke noget at vise | **Intet at vise** |
| Ingen filer tilgængelige | **Ingen filer** |

### Drag-and-drop

- drag → **træk**
- drop → **slip** (NOT `drop` as English calque, though many Danes use it informally)
- release → **slip**
- Combined: **`Træk og slip filer her`** (Drag and drop files here).

### Quantity expressions

| ✗ Calque | ✓ Native |
|----------|----------|
| 25+ sprog | **mere end 25 sprog** / **over 25 sprog** |
| +{count} mere | **og {count} mere** |
| +25 nye funktioner | **over 25 nye funktioner** |

### Error messages — what + next step

| ✗ Bare | ✓ With next step |
|--------|------------------|
| Filen blev ikke fundet. | **Filen blev ikke fundet. Tjek stien.** |
| Netværksfejl. | **Netværksfejl. Prøv igen.** |
| Ugyldig e-mail. | **Ugyldig e-mailadresse. Tjek formatet.** |
| Login mislykkedes. | **Login mislykkedes. Tjek brugernavn og adgangskode.** |

### Support expressions

| ✗ Calque | ✓ Native |
|----------|----------|
| Understøttelse af X-filer | **Understøtter X-filer** / **X-filer understøttes** |
| Understøttelse af flere sprog | **Understøtter flere sprog** |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Danish | Notes |
|------|--------|-------|
| Question mark | `?` | Same as English |
| Comma | `,` | Different conjunction rules |
| Period | `.` | Same |
| Colon | `:` | NO space before |
| Quotation marks | **`„…"`** German-style OR **`»…«`** French-style (inward-pointing — opposite of Norwegian) | Either acceptable; `"…"` increasingly common in modern UI |
| Apostrophe | only in foreign names (`Joe's`) | Danish genitive: bare `-s` |
| Em-dash | `—` | Used for parenthetical breaks |

**Critical: Danish guillemets point INWARD `»…«`** — opposite of Norwegian's outward `«…»`. If using guillemets, get the direction right.

### Numbers

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **period (.)** or space | 1.234.567 or 1 234 567 |
| Decimal separator | **comma (,)** | 3,14 / 99,99 |
| Negative | `-25` | |
| Percent | `25 %` (with space) or `25%` (acceptable in UI) | |

**Critical:** Danish uses **period OR space for thousands, comma for decimal** — same as Norwegian, different from Swedish (space-only). Never `1,234.56` (English) in Danish UI.

### Dates

| Format | Example | Use |
|--------|---------|-----|
| DD-MM-YYYY | **15-01-2024** | Default Danish format (hyphens) |
| DD.MM.YYYY | **15.01.2024** | Acceptable alternative (periods) |
| D. måned YYYY | **15. januar 2024** | Long-form prose |
| YYYY-MM-DD | 2024-01-15 | Technical/API only |

**Critical: Danish prefers HYPHEN-separated dates** (`15-01-2024`), unlike Norwegian's period (`15.01.2024`) and Swedish's ISO (`2024-01-15`). All three are mutually understood, but hyphen is the Danish-specific default.

**Months (lowercase always, no period for full names):**

| 1 | januar | 7 | juli |
| 2 | februar | 8 | august |
| 3 | marts | 9 | september |
| 4 | april | 10 | oktober |
| 5 | maj | 11 | november |
| 6 | juni | 12 | december |

**Weekdays (lowercase):** mandag, tirsdag, onsdag, torsdag, fredag, lørdag, søndag.

Week starts **Monday**.

### Time

- 24-hour preferred: `14:30` or `kl. 14:30` (kl. = klokken).
- 12-hour rarely used.

### Currency — Danish krone (DKK / kr.)

| Format | Pattern | Example |
|--------|---------|---------|
| Symbol | `kr.` after amount with space (period after kr is standard) | **99,99 kr.** |
| ISO code | DKK | **99,99 DKK** / **DKK 99,99** |

Never `kr.99,99` (no space) or `$99.99` style. Danish krone is `kr.` with period after — Norwegian uses `kr` without period.

Denmark is in the EU but uses krone, NOT euro. Don't switch to EUR in Danish localization (Denmark opted out of the euro).

---

## Terminology — preferred Danish terms

| English | ✓ Danish preferred | ✗ Avoid |
|---------|---------------------|---------|
| user | bruger | user |
| account | konto | akkaunt |
| password | adgangskode (formal) / password (acceptable loanword) | — |
| settings | indstillinger | opsætning (= setup, different) |
| dashboard | dashboard (loanword OK) / kontrolpanel | — |
| email | e-mail | mejl (very informal) |
| link | link / hyperlink | — |
| website | hjemmeside / website | — |
| folder | mappe | — |
| file | fil | — |
| device | enhed | device |
| phone | telefon / mobil | — |
| computer | computer | komputer |
| application / app | applikation / app / program | — |
| update (v.) | opdatere | update |
| save | gemme | sejve |
| delete | slette | delete |
| upload | uploade / lægge op | — both common |
| download | downloade / hente | — both common |
| sign in / log in | logge ind | sign in |
| sign up | oprette konto / tilmelde sig | — |
| search | søge / søgning | search |
| click | klikke | — |
| share | dele | share |
| profile | profil | — |
| notifications | notifikationer / underretninger | — |
| privacy | privatliv / privatlivspolitik | — |
| terms | vilkår / betingelser | — |
| support | support | — |
| help | hjælp | — |
| feedback | feedback (OK) / tilbagemelding | — |
| menu | menu | — |
| home | hjem / startside | — |
| logout | logge ud | — |
| browser | browser (loanword OK) | — |
| screen | skærm | — |
| keyboard | tastatur | tipkovnica (that's Croatian!) |
| mouse | mus | — |
| build (software) | bygge / udvikle | — |
| deploy | udrulle / installere / deploye (informal) | — |
| pipeline | pipeline (keep) | — |
| commit (git) | committe (informal, attested) / gemme ændringer | — |
| merge (git) | flette / sammenflette | mergee |
| repository | repository / arkiv | — |
| branch (git) | gren / branch | — |
| API | API (keep — Latin always) | — |
| endpoint | endpoint (keep) | — |
| cache | cache (keep) / mellemlager | — |
| log (n.) | log | — |
| sync | synkronisere / synke (informal) | — |
| webhook | webhook (keep) | — |
| source of truth | sandhedskilde / kanonisk datakilde | — |

Danish is **slightly more open to English loanwords** than Swedish or (especially) Croatian/Icelandic. Many anglicisms are fully naturalized: `computer`, `email`, `download`, `upload`, `browser`, `cookie`. Don't over-purify.

### Tech identifiers — keep in Latin/English

These MUST stay in English inside Danish text:
- Programming languages, frameworks, tools (Git, GitHub, Docker, npm, pip).
- Protocols (HTTP, REST, GraphQL).
- File formats (JSON, XML, CSV, PDF).
- Commands, paths, URLs, code.

---

## False Friends — Critical

| Danish word | Actually means | NOT this | Correct for the English |
|-------------|----------------|----------|--------------------------|
| aktuel | current / relevant | "actual" | "actual" → **faktisk** / **egentlig** |
| eventuelt | possibly / perhaps | "eventually" | "eventually" → **til sidst** / **med tiden** |
| sympatisk | likeable / pleasant | "sympathetic (compassionate)" | "sympathetic" → **medfølende** |
| sensitiv | sensitive | "sensible" | "sensible" → **fornuftig** |
| kontrollere | to check / verify | "to control (manage)" | "control (manage)" → **styre** / **lede** |
| receptur | recipe (formal) | "receipt" | "receipt" → **kvittering** |
| barn | child | "barn" (building) | "barn" → **lade** |
| chef | boss / manager | "chef" (cook) | "chef" → **kok** |
| gift | married OR poison | "gift" (present) | "gift" → **gave** |
| rolig | calm / quiet | (also OK) | — |
| præsentation | presentation (slides, performance) | (mostly OK) | — |
| event | event (party) — attested loanword | (OK in casual) | "event (formal)" → **begivenhed** |

---

## Calque / Anti-Pattern List

| ✗ Calque | ✓ Native | Reason |
|----------|----------|--------|
| tage plads | **finde sted** | "Take place" calque |
| i slutningen af dagen | **i sidste ende** / **når alt kommer til alt** | "At the end of the day" calque |
| på en daglig basis | **dagligt** / **hver dag** | "On a daily basis" calque |
| ikke rigtig | **ikke ligefrem** / **ikke helt** | "Not really" — more natural form |
| foretage en forbedring | **forbedre** | "Make an improvement" — use verb |
| give et svar | **svare** | "Provide an answer" — use verb |
| Få det oversat på minutter | **Oversættelse på få minutter** | "Get X done" structural calque |
| Hold dine projekter synkroniserede | **Sørg for synkronisering af projekterne** | "Keep X synced" calque |
| Gør din arbejdsgang hurtigere | **Effektiviser din arbejdsgang** | "Make X faster" calque |
| Hurtig oversættelse. Sikker. Pålidelig. (telegram) | **Hurtige, sikre og pålidelige oversættelser** | Telegram fragments → complete noun phrase |
| Det giver mening | **Det giver mening** ✓ (this is actually correct Danish) | (Note: `det giver mening` IS native Danish — leave it) |
| AI-drevet | **AI-baseret** / **drevet af AI** / **med AI** | "X-driven" awkward |
| AI-bevidst | **AI-klar** / **understøtter AI** / **med AI-understøttelse** | "X-aware" calque |
| brugervenlig | (this IS standard Danish, not a calque — leave it) | — |
| Amerikas Forenede Stater | **USA** | UI short form |
| Det Forenede Kongerige | **Storbritannien** / **UK** | UI short form |
| Drag here | **Træk hertil** | English verb → native |
| Drop here | **Slip her** | English → native |
| Færdig! Din oversættelse er nu klar. | **Oversættelse fuldført** | Verbose completion → concise |
| Fantastisk! Alt er blevet gemt. | **Alt gemt** | Verbose with interjection → concise |

---

## Custom Sections

### Time / duration — `tilbage` and unit abbreviations

| English | ✓ Danish |
|---------|----------|
| 30 seconds remaining | **30 sek tilbage** / **30 s tilbage** |
| 5 minutes remaining | **5 min tilbage** (NOT `5 m`) |
| 2 hours remaining | **2 t tilbage** (NOT `2 h` — `h` is English) |
| 3 days remaining | **3 d tilbage** / **3 dage tilbage** |

- `tilbage` is the standard Danish UI form for "remaining".
- Always **space** between number and unit: `5 min` ✓, `5min` ✗.
- `min` for minutes (NOT `m` — ambiguous with meters).
- `t` for timer (NOT English `h`).

### Per vs for (rate vs total)

| Source | ✓ Danish | Meaning |
|--------|----------|---------|
| per language (rate) | **pr. sprog** / **per sprog** | rate, per-unit |
| for 25 languages (total) | **for 25 sprog** / **til 25 sprog** | total scope |
| 5 USD per language | **5 USD pr. sprog** | rate |
| 5 USD for all languages | **5 USD for alle sprog** | total |

Danish uses **`pr.`** (abbreviation of Latin `per`) as the standard form, optionally `per` written out. Never use English `per` style without the period.

### Cost / estimate ordering

Amount-first:

| ✗ Ambiguous | ✓ Clear |
|-------------|---------|
| 5 sprog 25 kreditter | **25 kreditter for 5 sprog** |

### "Hygge" cultural tone

Danish culture values **hygge** — cozy, warm, low-key. UI copy in Danish should:
- Be **direct but warm** (Janteloven-style modesty — no boasting).
- Avoid superlatives and hype ("BEDST!" → just `Forbedret` or `Bedre`).
- Use friendly but not overly enthusiastic tone.
- Prefer practical, solution-oriented language.

For marketing copy, **soften American-style hyperbole**.

### UI element references in prose

When prose refers to a specific named UI element, use quotation marks:

| ✗ Compound | ✓ Quoted label |
|------------|----------------|
| Klik på Gem-knappen | **Klik på knappen "Gem"** |
| Åbn Indstillinger-fanen | **Åbn fanen "Indstillinger"** |
| Brug Navn-feltet | **Brug feltet "Navn"** |

### Brand names + Danish suffixes — use apostrophe + s for genitive

Foreign brand names take Danish definite/possessive endings via apostrophe or hyphen:

- `OneSky` → `OneSky'et` (def. neuter, with apostrophe) or `OneSky-en` (def. common).
- `Google's` (Google's) — Danish genitive can use English-style `'s` for foreign brands.
- `iPhone-en` (the iPhone).
- `GitHub-en` (the GitHub).

---

## Self-Check Checklist (Run Before Returning Output)

### Accuracy (auto-fail on miss)

- [ ] **Compound words written as ONE word** — no særskrivning (`database`, `brugergrænseflade`).
- [ ] **Hybrid-compound verbs rejected** — no `aflinke`, `afsynce`, `cancele`, `deletee`, `installe`.
- [ ] **Gender (en/et)** correct on every article and definite suffix.
- [ ] **No double-definiteness** (Swedish-style) — Danish uses EITHER suffix OR free article: `den store fil` ✓ NOT `den store filen`.
- [ ] **Adjective agreement**: -t for et-noun indefinite singular, -e for plural/definite.
- [ ] **V2 word order** in every main clause (verb in position 2).
- [ ] **Subordinate clause word order**: subject before verb, `ikke` between them.
- [ ] **Negation placement**: after verb (main), before verb (subordinate).
- [ ] **No comma before `og` / `eller`**; comma before `men` / `for` / `at` / subordinating conjunctions.
- [ ] **Special chars `æ ø å`** preserved — never replaced.
- [ ] **ICU plurals**: `one` and `other` categories.
- [ ] **Placeholders** preserved.
- [ ] **Latin tech identifiers**: Git, API, JSON, React, etc. stay in Latin.
- [ ] **Numbers**: comma decimal (3,14), period/space thousands (1.234 / 1 234), `kr.` after amount.
- [ ] **Dates**: DD-MM-YYYY (hyphen — Danish default).
- [ ] **Time**: 24-hour, `kl. 14:30`.
- [ ] **per vs for**: `pr. sprog` for rate, `for X sprog` for total.

### Register

- [ ] **du throughout** — never `De` (archaic).
- [ ] **No literary register elevation** when source is casual.
- [ ] **Possessive forms** match the du-form (`din / dit / dine`), never `Deres`.

### UI conventions

- [ ] Buttons use imperative (`Gem`, `Annuller`, `Slet`).
- [ ] Status uses present + ellipsis (`Indlæser…`, `Gemmer…`).
- [ ] Completion concise (`Gemt`, `Oversættelse fuldført`, NOT `Fantastisk! Alt er blevet gemt!`).
- [ ] Empty states concise (`Ingen resultater`, NOT `Der blev ikke fundet nogen resultater`).
- [ ] Drag-drop uses `træk` and `slip`.
- [ ] `Understøtter X` not `Understøttelse af X`.
- [ ] Quantity: `mere end 25` not `25+`; `og {count} mere` not `+{count}`.
- [ ] Error messages include next step.

### Naturalness

- [ ] No English calques (`tage plads`, `i slutningen af dagen`, `på en daglig basis`, `foretage en forbedring`).
- [ ] No anglicism-verb hybrid forms (`aflinke`, `afsynce`).
- [ ] False-friend check: `aktuel ≠ actual`, `eventuelt ≠ eventually`, `kontrollere = check (not manage)`, `gift = married OR poison (not present)`.
- [ ] `tilbage` for time-remaining; `min` not `m`; `t` not `h`; space before unit.
- [ ] Proper nouns short forms (`USA`, `Storbritannien`).
- [ ] Hygge tone — no hype, modest, warm.
- [ ] Currency `kr.` (with period) after amount.
- [ ] No accidental Norwegian forms (`meg`, `deg`, `nå`, `hva`, `søt`, `hvit`, `noe`, `bli`, `si`).

---

## Worked Example — Standard da UI

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** neutral product UI → casual du, present-tense status.

**Translation:**

> Velkommen tilbage! Du har 3 nye filer på din konto. Klik på **Fortsæt** for at gennemgå dem eller **Annuller** for at blive her. Gemmer dine ændringer…

**Why this works:**
- `Velkommen tilbage` — standard greeting.
- `Du har` — du-form throughout.
- `3 nye filer` — plural adj `nye` (-e suffix for plural), plural noun `filer`. Indefinite, no article.
- `på din konto` — `på` + plain noun (no double-def with possessive). `konto` is en-noun (modern Danish), `din` agrees.
- Buttons imperative: `Fortsæt`, `Annuller`.
- `for at gennemgå dem / for at blive her` — purpose `for at + infinitive`.
- Status: `Gemmer dine ændringer…` (present + ellipsis, possessive plural `dine`).
- No comma before `eller` ✓.
- Punctuation: Latin `!`, `…` standard.
- æ ø å preserved.

**Same string with formal/banking register (still du):**

> Velkommen tilbage. Du har 3 nye filer på din konto. Klik på **Fortsæt** for at gennemgå filerne, eller klik på **Annuller** for at afbryde. Ændringerne gemmes…

(Drop `!`, switch to passive `gemmes` instead of `Gemmer`, use definite `filerne` to reinforce specificity, still `du` throughout.)

---

## Worked Example — Compound word + V2

**Source:** Today, the system saves your file automatically every five minutes.

**Translation:**

> I dag **gemmer systemet** din fil **automatisk** hvert femte minut.

**Notes:**
- `I dag` fronted → V2 inversion → `gemmer systemet`.
- `systemet` — definite suffix on et-noun.
- `din fil` — possessive, en-noun.
- `hvert femte minut` — "every fifth minute" (Danish idiom for "every X minutes"). NOT `hver fem minutter`.
- No særskrivning issues; `systemet` is single word.

---

## Worked Example — Date and currency

**Source:** Last login: January 15, 2024 at 2:30 PM. Subscription: $99.99/month.

**Translation:**

> Sidste login: 15-01-2024 kl. 14:30. Abonnement: 99,99 kr. pr. måned.

(Hyphen-separated date — Danish default. `kl. 14:30` for 24-hour time. `99,99 kr.` for currency. `pr. måned` for "per month".)

---

## Worked Example — ICU plurals

**Source:**

```icu
{count, plural, one {# new file} other {# new files}}
```

**Translation:**

```icu
{count, plural,
  one {# ny fil}
  other {# nye filer}
}
```

Notes:
- `one`: `ny` (base form, en-noun indef. sg.).
- `other`: `nye filer` (plural adjective -e, plural noun).

---

## Worked Example — Reflexive possessive

**Source:** She saves her [own] file. She saves her [Anna's] file.

**Translation:**

> Hun gemmer **sin** fil. (her own)
> Hun gemmer **hendes** fil. (Anna's = someone else's)

Reflexive `sin` when possessor = subject; `hendes` when referring to a different person.

---

## When in Doubt

1. **Default to da, du-form, hyphen-separated dates, two-gender (en/et) checked per noun.**
2. If you typed `meg / deg / nå / hva / søt / hvit / noe / bli` → **switch to Danish equivalents** (`mig / dig / nu / hvad / sød / hvid / noget / blive`). You accidentally wrote Norwegian.
3. If a word looks like an English root with `af- / op- / ud-` prefixed → **stop and find the native verb** (`frakoble`, `synkronisere`, `slette`).
4. If you typed two nouns with a space (`data base`, `bruger grænseflade`) → **join them**.
5. If you put both article AND suffix (Swedish-style `den store filen`) → **remove the suffix**: `den store fil`.
6. If you used `De / Deres` for formal singular → **switch to `du / din`**. Always.
7. If currency is `kr` (no period) → **add the period**: `kr.` Danish convention.
8. If currency is EUR for a Danish locale → **switch to DKK** (Denmark opted out of euro).
9. If date is `2024-01-15` or `15.01.2024` → **prefer Danish default `15-01-2024`** (hyphens).
10. If you over-claim with marketing hype → **soften with hygge tone**.
