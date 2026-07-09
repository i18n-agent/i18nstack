---
name: localize-sv
description: Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Swedish (sv / sv-SE / sv-FI). Enforces två genus (en/ett) agreement, V2 word order with subordinate-clause inversion, double definiteness (den stora filen), compound-word integrity (särskrivning is a critical error), du-form universality post-du-reform (ni is archaic), fler/mer countable/uncountable distinction, s-passive, ISO 8601 dates (YYYY-MM-DD), comma decimals with space thousands, å/ä/ö preservation, hybrid-compound verb rejection (no avlinka, avsynca), and register auto-detection from source.
---

# Translate to Swedish (sv) — High-Fidelity Skill

## Scope & Variants

Swedish has two recognized written variants for product localization:

| Locale | Name | Speakers | Use case | Currency |
|--------|------|----------|----------|----------|
| `sv` / `sv-SE` | Sweden Swedish (default) | ~10M | Pan-Swedish UI, default for `sv` | SEK (kr) |
| `sv-FI` | Finland Swedish (finlandssvenska) | ~290k (Swedish-speaking Finns; official minority lang) | Products targeting Finland's Swedish-speaking population | EUR (€) |

**Practical reality:** ~95% of Swedish translation work is `sv-SE` and the differences from `sv-FI` are mostly currency, a handful of vocabulary items (e.g., `tvättstuga` vs `tvättinrättning`), and Finnish-administrative loanwords. For pan-Nordic products, **always default to `sv-SE`** unless the audience is specifically Finland-Swedish.

### When the target locale is unspecified

If the user requests "Swedish" without specifying:

> Which Swedish variant should I target?
>
> - **sv-SE (Sweden Swedish, Recommended)** — Default. SEK currency, Stockholm-norm.
> - **sv-FI (Finland Swedish)** — Finland's Swedish-speaking minority. EUR currency, some Finnish-administrative vocabulary.

Default to `sv-SE` if no answer.

---

## Register Auto-Detection (Apply Before Translating)

Modern Swedish is famously informal — the **du-reform of the late 1960s** abolished hierarchical pronouns. `Ni` (formal "you") survives only as an archaism, in some service-industry attempts at "old-school politeness" (poorly received), or in poetry/legal forms. **All modern software uses `du` universally** — banking, government services, healthcare apps, everything.

Auto-detect from source:

| Source signal | Target register |
|---------------|-----------------|
| Casual / conversational / playful (`Hey!`, contractions, exclamations, emoji) | **Casual du** — direct verbs, contractions where natural (`nån` for `någon` in some apps), short sentences. Avoid literary verbs (`förbli` → `vara kvar`). |
| Neutral product UI / documentation (DEFAULT) | **Neutral du** — du throughout, present tense status, imperative buttons, no literary vocabulary. |
| Legal / financial / formal corporate (terms of service, banking statements, government forms) | **Formal du** — still `du` (never `ni`!), but use full forms (`ska` over `kommer att`, `inte` over `nån`), avoid colloquialisms, prefer s-passive for impersonal statements. |

**Hard rule: NEVER use `ni` in modern Swedish UI.** Even for legal/banking. It will be read as either archaic (irritating) or wrong (especially since `ni` is also the plural "you" in Swedish — using it as singular formal is ambiguous and dated).

**Hard rule: source register matching for vocabulary** — if the source uses casual English (`stay`, `countless`, `ship`), do NOT elevate to literary Swedish (`förbli`, `otaliga`, `levereras`). Match the register, not the dictionary's first hit.

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. Compound words written as ONE word — särskrivning is a critical error (severity 2.5)

Swedish forms compounds by **concatenation**, not spacing or hyphens. Separating a compound into two words (`särskrivning`) changes meaning catastrophically — it's the most-mocked Swedish error.

| ✗ Wrong (split) | ✓ Correct (joined) | Meaning of the split version |
|-----------------|--------------------|-----------------------------|
| `sjuk sköterska` | **`sjuksköterska`** | "sick nurse" (the nurse is sick!) vs "nurse" |
| `kassa biträde` | **`kassabiträde`** | "shitty assistant" vs "cashier" |
| `brun hårig flicka` | **`brunhårig flicka`** | "brown hairy girl" vs "brown-haired girl" |
| `data bas` | **`databas`** | nonsense vs "database" |
| `bil förare` | **`bilförare`** | nonsense vs "car driver" |
| `användar gränssnitt` | **`användargränssnitt`** | nonsense vs "user interface" |
| `lösen ord` | **`lösenord`** | nonsense vs "password" |

**Rule of thumb:** if two nouns together describe a single concept in English (`user interface`, `database`, `password`), they form a single Swedish word.

**Hyphens** are used only for:
- Compound where first element is an acronym or number: `IT-företag`, `25-årig`.
- Brand names: `Google-konto`.
- Avoiding three identical consonants in writing: `tax-xa` style edge cases (very rare).
- Avoiding ambiguity in long compounds (rare; ask if uncertain).

When unsure, write it as one word. Native readers expect compounds joined.

### 2. Hybrid-compound verb anti-pattern (Swedish prefix + English stem) — REJECT (severity 2.5)

A common AI-translation failure mode: bolt a Swedish verbal prefix (`av-`, `från-`, `ur-`, `upp-`, `in-`) onto a raw English root (`link`, `sync`, `share`, `stream`, `pair`, `merge`, `push`, `pull`) and produce a non-word.

| ✗ Wrong (hybrid) | ✓ Correct (native attested) | English |
|------------------|------------------------------|---------|
| `avlinka` / `avlänkad` | **`koppla bort`** / **`frånkopplad`** | unlink / disconnected |
| `avsynca` | **`synkronisera`** / **`avsynkronisera`** | sync / desync |
| `delea` | **`dela`** | share (dela exists; delea doesn't) |
| `pairea` | **`para ihop`** / **`koppla samman`** | pair |
| `uppgrade` / `uppgreja` | **`uppgradera`** | upgrade |
| `mergea` | **`slå ihop`** / **`sammanfoga`** | merge |
| `pushea` | **`skicka in`** / **`pusha`** (git context only) | push |
| `streama` | **`streama`** ✓ (this one is attested) | stream |
| `downloada` | **`ladda ner`** | download |
| `uploada` | **`ladda upp`** | upload |
| `deleta` | **`radera`** / **`ta bort`** | delete |
| `cancella` | **`avbryta`** | cancel |
| `updatea` | **`uppdatera`** | update |
| `supportera` | **`stödja`** / **`stöder`** | support |
| `deployera` | **`driftsätta`** / **`rulla ut`** / **`publicera`** | deploy |

**Verification test:** before accepting any verb formed with a Swedish prefix + English-looking root, ask "would this appear in SAOL (Svenska Akademiens ordlista)?" If you're not sure, use the attested native verb. Standard Swedish has native forms for almost every IT verb concept.

A few English loans that ARE attested and acceptable: `streama`, `tweeta`, `chatta`, `mejla`, `googla`, `pusha` (git-context only), `bloga`, `dejta`. These have entered the language. Hybrid prefixed forms of them generally have not.

### 3. Gender — `en` vs `ett` (severity 2.0)

Swedish has two genders: **common (en, ~75%)** and **neuter (ett, ~25%)**. There is no reliable phonological rule — you must know the gender per noun.

**Common IT nouns and their genders (memorize for tech UI):**

| en (common) | ett (neuter) |
|-------------|--------------|
| en fil (file) | ett system (system) |
| en mapp (folder) | ett konto (account) |
| en plattform (platform) | ett problem (problem) |
| en app (app) | ett lösenord (password) |
| en sida (page/side) | ett meddelande (message) |
| en knapp (button) | ett dokument (document) |
| en inställning (setting) | ett nätverk (network) |
| en användare (user) | ett objekt (object) |
| en flik (tab) | ett gränssnitt (interface) |
| en länk (link) | ett alternativ (option) |
| en bild (image) | ett verktyg (tool) |
| en uppdatering (update) | ett resultat (result) |
| en sökning (search) | ett fält (field) |
| en webbplats (website) | ett namn (name) |
| en e-post (email — but `mail` is `ett`) | ett kort (card) |
| en webbsida (web page) | ett tema (theme) |
| en kommentar (comment) | ett ämne (subject/topic) |
| en notis (notification) | ett konto (account) |

**Indefinite article**: en/ett before the noun.
**Definite (without adjective)**: suffix `-en` (common) or `-et` (neuter). `filen`, `systemet`.
**Definite (with adjective)**: free article `den/det` + adjective + noun + definite suffix = **DOUBLE DEFINITENESS**. `den stora filen`, `det nya systemet`.

### 4. Double definiteness — both article AND suffix (severity 2.0)

When a definite noun has a preceding adjective, Swedish requires **both** the free article `den/det/de` AND the definite suffix on the noun. This is unusual among Germanic languages.

| ✗ Wrong | ✓ Correct | English |
|---------|-----------|---------|
| `stora filen` (no article) | **`den stora filen`** | the large file |
| `den stora fil` (no suffix) | **`den stora filen`** | the large file |
| `nya systemet` (no article) | **`det nya systemet`** | the new system |
| `det nya system` (no suffix) | **`det nya systemet`** | the new system |
| `nya filerna` (no article) | **`de nya filerna`** | the new files |

**Exception**: certain fixed expressions and proper-noun-like compounds skip the article (`Svenska Akademien`, `Sista versen`). For UI, always use both.

### 5. V2 word order (verb in second position in main clauses) (severity 2.0)

Swedish, like all mainland Scandinavian languages and German, is **strict V2**: in any declarative main clause, the **finite verb** must come in **position 2**, regardless of what fills position 1.

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| `Idag användaren sparar filen` | **`Idag sparar användaren filen`** (Today saves the user the file) |
| `Nu systemet laddar data` | **`Nu laddar systemet data`** |
| `Efter inloggningen du kan ändra...` | **`Efter inloggningen kan du ändra...`** |
| `Snart vi kommer att lansera` | **`Snart kommer vi att lansera`** |

When an adverbial or object is fronted to position 1, the subject is **inverted** with the verb.

### 6. Subordinate clause word order — DIFFERENT from main clauses (severity 1.5)

In subordinate clauses (introduced by `att`, `som`, `eftersom`, `när`, `om`, `medan`, `innan`, `efter att`), the **subject comes BEFORE the verb**, and adverbs like `inte`, `alltid`, `aldrig` go between subject and verb.

| Clause type | Word order | Example |
|-------------|-----------|---------|
| Main (V2) | Subject — Verb — Adverb — Object | `Användaren sparar inte filen.` |
| Subordinate (SVx) | Subject — Adverb — Verb — Object | `…eftersom användaren inte sparar filen.` |

### 7. Negation placement (severity 2.0)

`Inte` (not) follows the V2/subordinate split above. The classic native-speaker test:

| Context | Pattern | Example |
|---------|---------|---------|
| Main clause | Verb + inte | `Filen sparas inte.` (The file is not saved.) |
| Main clause with object | Verb + Subject + inte + Object | `Sparar filen inte automatiskt?` (no) — actually: `Sparas filen inte automatiskt?` |
| Subordinate clause | inte + Verb | `…eftersom filen inte sparas.` |

### 8. Compound-quantifier distinction: `fler` (countable) vs `mer` (uncountable) (severity 2.0)

| Countable (use fler/färre) | Uncountable (use mer/mindre) |
|----------------------------|-------------------------------|
| `fler filer` (more files) | `mer minne` (more memory) |
| `fler alternativ` (more options) | `mer information` (more information) |
| `fler språk` (more languages) | `mer plats` (more space) |
| `färre fel` (fewer errors) | `mindre data` (less data) |
| `färre klick` (fewer clicks) | `mindre brus` (less noise) |

**Button labels**: `Visa fler` ✓ (show more — countable items), NOT `Visa mer` for a list.
**Body text**: `Lägg till fler språk` ✓, NOT `Lägg till mer språk`.

### 9. Comma rules — `eller`, `och` vs `men`, `för` (severity 1.0)

- **No comma** before coordinating conjunctions `eller` (or) and `och` (and).
- **Comma** before contrastive conjunctions `men` (but), `för` (because/for).
- Comma before subordinating conjunctions: `Han kom hem, eftersom det började regna.`

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| `Spara, och stäng.` | `Spara och stäng.` |
| `Dra hit, eller klicka.` | `Dra hit eller klicka.` |
| `Det är enkelt men effektivt.` | `Det är enkelt, men effektivt.` |
| `Vi kan inte det för det är låst.` | `Vi kan inte det, för det är låst.` |

### 10. Special characters `å ä ö` are essential — NEVER strip (severity 3.0)

Replacing `å ä ö` with `a a o` or `aa ae oe` is the single highest-severity character-level error in Swedish translation. They are letters, not diacritics — `år` (year) and `år` are different words from `ar` (would-be nonsense).

A Swedish-localized product with `Sprak` instead of `Språk`, `Andra` instead of `Ändra`, `Lasenord` instead of `Lösenord` is broken on its face.

### 11. ICU plurals — `one` + `other` is enough for Swedish (severity 1.5)

Swedish has only two CLDR plural categories: `one` (n = 1) and `other` (everything else). Unlike Arabic/Russian, no extra categories needed.

```icu
{count, plural,
  one {# fil}
  other {# filer}
}
```

But: the definite plural form differs (`# filer` indefinite vs `de # filerna` definite), and **adjective agreement** must be checked separately (see Grammar Reference).

---

## Pronouns and Possessives

### Personal pronouns

| English | Swedish | Notes |
|---------|---------|-------|
| I | jag | |
| you (sg.) | **du** (always, modern) | NEVER `ni` for singular formal |
| you (pl.) | **ni** | This is the only modern use of `ni` |
| he / she / they (sg., gender-neutral) | han / hon / **hen** | `hen` is gender-neutral, increasingly common |
| we | vi | |
| they | de (subject) / dem (object) — in spoken Swedish often `dom` for both | UI: write `de` / `dem` for written register |
| it (common) | den | |
| it (neuter) | det | |

### Possessive pronouns (agree with the POSSESSED noun's gender/number)

| Person | en-noun | ett-noun | plural |
|--------|---------|----------|--------|
| min (my) | min fil | mitt system | mina filer |
| din (your sg.) | din fil | ditt system | dina filer |
| hans (his — invariable) | hans fil | hans system | hans filer |
| hennes (her — invariable) | hennes fil | hennes system | hennes filer |
| sin / sitt / sina (reflexive — own) | sin fil | sitt system | sina filer |
| vår (our) | vår fil | vårt system | våra filer |
| er (your pl.) | er fil | ert system | era filer |
| deras (their — invariable) | deras fil | deras system | deras filer |

**Reflexive `sin/sitt/sina`** is critical: used when the possessor is the subject of the same clause.
- `Hon sparar sin fil.` (She saves her own file.) ← reflexive
- `Hon sparar hennes fil.` (She saves her [someone else's] file.) ← non-reflexive

---

## Grammar Reference

### Adjective agreement

Three forms: **base / -t / -a**.

| Subject | Form | Example |
|---------|------|---------|
| en-noun, indefinite singular | base | en **stor** fil |
| ett-noun, indefinite singular | -t | ett **stort** system |
| plural (indefinite) | -a | **stora** filer |
| definite (sg./pl., either gender) | -a | den **stora** filen, det **stora** systemet, de **stora** filerna |

Irregular: `liten` (small) → `litet` (neuter) / `små` (plural).
Irregular: `gammal` (old) → `gammalt` / `gamla`.
Mass nouns (en svår tid → den svåra tiden) follow the same pattern.

### Verb conjugation — present tense uses ONE form for all persons

Swedish verbs do **not** conjugate by person. The same form serves I/you/we/they.

| Group | Infinitive | Present (all persons) | Past | Supine | Past participle |
|-------|-----------|-----------------------|------|--------|-----------------|
| 1 (-ar) | tala | tal**ar** | tal**ade** | tal**at** | tal**ad/at/ade** |
| 2a (-er) | ringa | ring**er** | ring**de** | ring**t** | ring**d/t/da** |
| 2b (-er) | läsa | läs**er** | läs**te** | läs**t** | läs**t/ta** |
| 3 (-r) | bo | bo**r** | bo**dde** | bo**tt** | bo**dd/tt/dda** |
| 4 (strong) | skriva | skriv**er** | skrev | skriv**it** | skriv**en/et/na** |

For UI work, the key forms are present (status messages) and past/supine (completion).

### S-passive — Swedish's elegant passive voice

Form: stem + **-s** (from older `-st`). The s-passive is the preferred passive in technical and impersonal contexts.

| Active | S-passive | Past s-passive |
|--------|-----------|----------------|
| Systemet sparar filen. | **Filen sparas.** (The file is saved / is being saved.) | **Filen sparades.** |
| Användaren raderar kontot. | **Kontot raderas.** | **Kontot raderades.** |
| Vi laddar data. | **Data laddas.** | **Data laddades.** |

Avoid the periphrastic `bli + past participle` (`Filen blir sparad`) in UI — it sounds bureaucratic.

### Definite forms summary

| Indefinite sg. | Definite sg. | Indef. pl. | Def. pl. |
|----------------|--------------|------------|----------|
| en fil | filen | filer | filerna |
| en mapp | mappen | mappar | mapparna |
| ett system | systemet | system | systemen |
| ett konto | kontot | konton | kontona |
| en användare | användaren | användare | användarna |
| en plattform | plattformen | plattformar | plattformarna |

---

## UI Conventions

### Buttons — imperative (preferred) or infinitive

| English | ✓ Imperative (preferred) | ✓ Infinitive (also OK) |
|---------|--------------------------|-----------------------|
| Save | **Spara** | Spara |
| Cancel | **Avbryt** | Avbryta |
| Delete | **Radera** / **Ta bort** | — |
| Send | **Skicka** | — |
| Edit | **Redigera** | — |
| Search | **Sök** | Söka |
| Confirm | **Bekräfta** | — |
| Continue | **Fortsätt** | Fortsätta |
| Submit | **Skicka in** / **Bekräfta** | — |
| Sign in / Log in | **Logga in** | — |
| Sign out / Log out | **Logga ut** | — |
| Sign up | **Skapa konto** / **Registrera dig** | — |
| Next | **Nästa** | — |
| Back | **Tillbaka** | — |
| Done | **Klar** | — |
| OK | **OK** | — |
| Close | **Stäng** | — |
| Upload | **Ladda upp** | — |
| Download | **Ladda ner** | — |
| Refresh | **Uppdatera** | — |
| Settings | **Inställningar** | — |
| Apply | **Använd** / **Tillämpa** | — |
| Reset | **Återställ** | — |

Standard Swedish platform localization (Windows, macOS, iOS, Android) uses **imperative** — follow this convention.

### Status messages — present tense + ellipsis

| English | ✓ Swedish |
|---------|-----------|
| Loading… | **Laddar…** |
| Saving… | **Sparar…** |
| Sending… | **Skickar…** |
| Connecting… | **Ansluter…** |
| Processing… | **Bearbetar…** |
| Uploading… | **Laddar upp…** |
| Searching… | **Söker…** |
| Please wait | **Vänligen vänta** / **Vänta…** |

### Completion messages — concise, often nominal + past participle

| English | ✓ Swedish |
|---------|-----------|
| Saved | **Sparat** / **Allt sparat** |
| Done! | **Klar** (NOT `Klar!` — drop exclamation in product UI) |
| Translation complete | **Översättning klar** |
| File uploaded | **Filen uppladdad** |
| Sent | **Skickat** |
| Payment successful | **Betalningen genomförd** |

### Empty states — concise label, drop pronouns

| ✗ Verbose | ✓ Concise |
|-----------|-----------|
| Inga resultat hittades | **Inga resultat** |
| Du har inga projekt ännu | **Inga projekt ännu** |
| Det finns ingenting här | **Inget att visa** |
| Inga filer tillgängliga | **Inga filer** |

### Drag-and-drop terminology

- drag → **dra**
- drop → **släpp** (NOT `frigör` = "liberate" — wrong sense)
- release → **släpp**
- Combined: **`Dra och släpp filer här`** (Drag and drop files here).

### File picker — `välj` not `bladdra`

Action-oriented `välj` (choose) or `välj filer` is the modern Swedish platform standard (Chrome, Windows-SV, macOS-SV). `Bladdra` (browse) is older/literal-calque feel.

| ✗ Older | ✓ Modern |
|---------|---------|
| Bladdra efter filer | **Välj filer** |
| Klicka för att bladdra | **Klicka för att välja** |
| Sök efter filer | (only for actual search) |

### "Support" expressions — verb form, not noun

| ✗ Calque | ✓ Native |
|----------|----------|
| Stöd för X-filer | **Stöder X-filer** |
| Stöd för flera språk | **Stöder flera språk** / **Flera språk stöds** |
| Stöd för {formatList} | **Stöder {formatList}** |

### Quantity expressions

| ✗ Calque | ✓ Native |
|----------|----------|
| 25+ språk | **fler än 25 språk** / **över 25 språk** |
| +{count} fler | **och {count} till** |
| +25 nya funktioner | **över 25 nya funktioner** |

### Error messages — what + next step

| ✗ Bare | ✓ With next step |
|--------|------------------|
| Filen hittades inte. | **Filen hittades inte. Kontrollera sökvägen.** |
| Nätverksfel. | **Nätverksfel. Försök igen.** |
| Ogiltig e-post. | **Ogiltig e-postadress. Kontrollera formatet.** |
| Inloggning misslyckades. | **Inloggning misslyckades. Kontrollera dina uppgifter.** |

### Validation — clear structure

| ✗ Comma soup | ✓ Structured |
|--------------|--------------|
| 3-50 tecken, bokstäver, siffror, bindestreck | **3-50 tecken. Tillåtet: bokstäver, siffror, bindestreck** |
| Fält saknas | **Detta fält är obligatoriskt** |
| Fel format | **Ogiltigt format** |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Swedish | Notes |
|------|---------|-------|
| Question mark | `?` | Same as English |
| Comma | `,` | Same as English; rules about conjunctions differ |
| Period | `.` | Same |
| Colon | `:` | Same; used in brand-suffix attachments (`OneSky:et`) |
| Quotation marks | `"…"` (common in modern Swedish) or `»…»` (rare, dated) | Either works; prefer plain `"…"`. Smart quotes `"…"` if typography allows. |
| Apostrophe | only in foreign names (`Joe's`) | Swedish genitive uses bare `-s`: `Annas bok` (NOT `Anna's bok`) |
| Ellipsis | `…` (one character) or `...` (three dots) | Either |

### Numbers

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **space** (or no separator) | 1 234 567 |
| Decimal separator | **comma** | 3,14 — `99,99 kr` |
| Negative | `-25` | |
| Percent | `25 %` (with space) OR `25%` (acceptable in UI) | |
| Negative percent | `-25 %` | |

**Critical:** Swedish uses **space** for thousands, NOT comma. `1,000` reads as "one comma zero zero zero" (= one) in Swedish — very confusing.

### Dates — ISO 8601 default

Swedish strongly prefers **YYYY-MM-DD** (ISO 8601). This is the official standard and most familiar to Swedish users in business/government/UI contexts.

| Format | Example | Use |
|--------|---------|-----|
| YYYY-MM-DD | **2024-01-15** | Default, all UI/business contexts |
| D mån. YYYY | 15 jan. 2024 | Casual prose, marketing |
| D månadnamn YYYY | 15 januari 2024 | Long-form prose |

**Months (lowercase always, no period for full names):**

| 1 | januari | 7 | juli |
| 2 | februari | 8 | augusti |
| 3 | mars | 9 | september |
| 4 | april | 10 | oktober |
| 5 | maj | 11 | november |
| 6 | juni | 12 | december |

**Weekdays (lowercase):** måndag, tisdag, onsdag, torsdag, fredag, lördag, söndag.
**Week starts Monday** in Swedish calendar.

### Time

- 24-hour preferred: `14:30` or `kl. 14:30` (kl. = klockan).
- 12-hour rarely used in Sweden. If shown: `2:30 e.m.` (eftermiddag) / `2:30 f.m.` (förmiddag) — but stick to 24-hour.

### Currency

| Locale | Currency | Format |
|--------|----------|--------|
| `sv-SE` | Swedish krona | `99,99 kr` or `99,99 SEK` (kr after amount, with space) |
| `sv-FI` | Euro | `99,99 €` or `99,99 EUR` (€ after amount, with space) |

Never `kr 99,99` or `$99,99` style in Swedish UI.

---

## Terminology — preferred Swedish terms

| English | ✓ Swedish | Avoid |
|---------|-----------|-------|
| user | användare | brukare |
| account | konto | account |
| password | lösenord | passord |
| settings | inställningar | settings |
| dashboard | instrumentpanel / översikt | dashboard |
| email | e-post | mail (rare for verb: mejla) |
| link | länk | link |
| browser | webbläsare | browser |
| website | webbplats | website |
| folder | mapp | folder |
| file | fil | — |
| device | enhet | device |
| phone | telefon / mobiltelefon / mobil | — |
| computer | dator | komputer |
| application / app | applikation / app | — |
| update (v.) | uppdatera | updatea |
| save | spara | — |
| delete | radera / ta bort | deleta |
| upload | ladda upp | uploada |
| download | ladda ner | downloada |
| sign in / log in | logga in | sign in |
| sign up | skapa konto / registrera | sign up |
| search | sök / söka | search |
| click | klicka | — |
| share | dela | sharea |
| profile | profil | — |
| notifications | aviseringar / notiser | notifications |
| privacy | integritet / sekretess | privacy |
| terms | villkor | terms |
| support | support (noun, OK) / **stödja** (verb) | supportera (verb form is wrong) |
| help | hjälp | — |
| feedback | feedback (OK) / återkoppling | — |
| menu | meny | — |
| home | hem / startsida | — |
| build (software) | bygga / skapa / utveckla | builda |
| deploy | driftsätta / rulla ut / publicera | deployera |
| commit (git) | committa (informal, attested) / spara | — |
| merge | slå ihop / sammanfoga / merga (informal git) | mergea |
| repository | repository / arkiv | — |
| branch (git) | gren / branch | — |
| pipeline | pipeline / processkedja | — |
| API | API (keep) | — |
| endpoint | endpoint / slutpunkt | — |
| cache | cache (keep) / mellanlagring | — |
| log (n.) | logg | — |
| sync | synkronisera / synka (informal) | — |
| webhook | webhook (keep) | — |
| source of truth | enda källa / källa till sanning (calque — avoid) | — |

### Tech identifiers — keep in Latin/English

These MUST stay in English inside Swedish text:
- Programming languages: Python, JavaScript, Go, Rust, Java.
- Frameworks: React, Vue, Next.js, Django, Spring.
- Tools: Git, GitHub, Docker, npm, pip.
- Protocols: HTTP, HTTPS, REST, GraphQL, TCP, SSH.
- File formats: JSON, XML, CSV, PDF.
- Commands, file paths, URLs, code identifiers.

---

## False Friends — Critical

Swedish has many words that look like English but mean something else. These are common AI-translation errors.

| Swedish word | Actually means | NOT this | Correct for the English |
|--------------|----------------|----------|--------------------------|
| aktuell | current / relevant | "actual" | "actual" → **faktisk / verklig** |
| eventuellt | possibly / perhaps | "eventually" | "eventually" → **till slut / så småningom** |
| semester | vacation | "academic semester" | "semester" → **termin** |
| sensibel | sensitive | "sensible" | "sensible" → **förnuftig / vettig** |
| kontrollera | to check / verify | "to control" | "control (v.)" → **styra / hantera** |
| engelsk | English (Englishman's) | "Anglican" | "Anglican" → **anglikansk** |
| receipt | a recipe | "receipt" (proof of payment) | "receipt" → **kvitto** |
| chef | boss / manager | "chef" (cook) | "chef (cook)" → **kock** |
| smaka | to taste | "to smack" | |
| barn | child(ren) | "barn" | "barn" → **lada** |
| gift | married OR poison | "gift" (present) | "gift" → **present / gåva** |
| rolig | funny / amusing | "rolling" | — |
| kock | a cook | "cock" | — |

---

## Calque / Anti-Pattern List

| ✗ Calque | ✓ Native | Reason |
|----------|----------|--------|
| Det ger mening | **Det är vettigt** / **Det är logiskt** | "makes sense" calque |
| ta plats | **äga rum** (events) / **finnas plats** (space) | "take place" calque |
| i slutet av dagen | **i slutändan** / **när allt kommer omkring** | "at the end of the day" calque |
| på en daglig basis | **dagligen** / **varje dag** | "on a daily basis" |
| i termer av | **när det gäller** / **vad gäller** | "in terms of" |
| göra en förbättring | **förbättra** | "make an improvement" — use verb |
| ge ett svar | **svara** | "provide an answer" — use verb |
| Få din översättning klar på minuter | **Översättning på bara minuter** | "Get X done" |
| Håll dina projekt synkroniserade | **Se till att projekten är synkroniserade** | "Keep X synced" |
| Gör ditt arbetsflöde snabbare | **Effektivisera ditt arbetsflöde** | "Make X faster" |
| Noll stillestånd / Zero downtime | **Utan avbrott** / **Inga avbrott** | "Zero X" calque |
| Noll engagemang | **Utan förpliktelser** / **Helt fritt** | "Zero commitment" |
| AI-driven | **AI-baserad** / **drivs av AI** / **med AI** | "X-driven" awkward |
| AI-medveten | **AI-anpassad** / **med AI-stöd** / **stödjer AI** | "X-aware" calque |
| användarvänlig | **lätt att använda** / **intuitiv** | "user-friendly" (this one is borderline OK in marketing but flagged in technical UI) |
| det sparas av systemet | **systemet sparar** | English-style agentless passive |
| Det är 5 år sedan jag (when "2019 me" / "[year] me") | **mitt 2019-jag** / **den jag var 2019** | year-vs-age confusion |
| Amerikas förenta stater | **USA** | UI short form |
| Förenade kungariket | **Storbritannien** / **UK** | UI short form |

---

## Custom Sections

### Time / duration — `återstår` and unit abbreviations

| English | ✓ Swedish |
|---------|-----------|
| 30 seconds remaining | **30 s återstår** |
| 5 minutes remaining | **5 min återstår** (NOT `5 m`) |
| 2 hours remaining | **2 tim återstår** or **2 h återstår** |
| 3 days remaining | **3 d återstår** or **3 dagar återstår** |

- `återstår` (preferred for UI) > `kvarstår` (more formal/bureaucratic).
- Always space between number and unit: `5 min` ✓, `5min` ✗.
- `min` for minutes, NOT `m` (which is meters).

### Per vs för (rate vs total) — CRITICAL semantic distinction

| Source | ✓ Swedish | Meaning |
|--------|-----------|---------|
| per language (rate) | **per språk** / **per språk** | rate, per-unit |
| for 25 languages (total) | **för 25 språk** / **till 25 språk** | total scope |
| $5 per language | **5 USD per språk** | rate |
| $5 for all languages | **5 USD för alla språk** | total |

Mixing these in pricing copy is an auto-fail.

### Cost / estimate ordering

Prefer **amount first**, then scope:

| ✗ Ambiguous | ✓ Clear |
|-------------|---------|
| 5 språk 25 krediter | **25 krediter för 5 språk** |
| 5 språk: 25 krediter | **5 språk: totalt 25 krediter** (acceptable variant) |

### Compound descriptive nouns — restructure don't stack

English allows long noun-compound chains (`mom creators`, `niche AI writers`). Swedish doesn't stack compounds 3+ deep gracefully — restructure with `som` clauses or prepositional phrases:

| ✗ Calque | ✓ Restructured |
|----------|----------------|
| mamma-skapare | **mammor som skapar innehåll** |
| nisch-skapare | **skapare inom nischområden** / **nischade innehållsskapare** |
| AI-skribent-verktyg | **AI-verktyg för skribenter** |

### "Lagom" cultural tone

Swedish culture values **lagom** — "just right, balanced, not too much". This translates into UI copy as:
- No superlatives or hype ("Bästa någonsin!" → just `Förbättrad`).
- No emoji overload.
- Practical, calm, understated.
- Don't be flashy or boastful.

For marketing copy especially, soften American-style hyperbole.

### UI element references in prose

When prose refers to a specific named UI element, use quotation marks around the label, not a compound:

| ✗ Compound | ✓ Quoted label |
|------------|----------------|
| Klicka på Spara-knappen | **Klicka på knappen "Spara"** |
| Öppna Inställningar-fliken | **Öppna fliken "Inställningar"** |
| Använd Namn-fältet | **Använd fältet "Namn"** |

(`Sparaknappen` would also be one word but reads as a generic concept; the quoted form clearly references a specific labelled element.)

### Brand names + Swedish suffixes — use colon

Foreign brand names take Swedish definite/possessive endings via colon:

- `OneSky` (en/ett brand) → `OneSky:et` (def. neuter), `OneSky:s` (possessive)
- `Google:s` (Google's)
- `GitHub:s` (GitHub's)
- `iPhone:n` (the iPhone)

---

## sv-FI Delta (Finland-Swedish)

If target is `sv-FI`, apply these overrides:

| Domain | sv-SE | sv-FI |
|--------|-------|-------|
| Currency | SEK (kr) | EUR (€) |
| Date | YYYY-MM-DD (ISO) | DD.MM.YYYY (Finnish style) or YYYY-MM-DD |
| Phone | Swedish format (+46) | Finnish format (+358) |
| ID number | personnummer (10/12 digits) | personbeteckning / HETU |
| postcode → city | 12345 Stockholm | 00100 Helsingfors |
| `kommun` | kommun | kommun (same) but local council = `stadsfullmäktige` |
| `landstinget` | regionen | landskapet (region in Finland) |
| `kärnkraftverk` | (same) | — |
| `tvättstuga` | tvättstuga | tvättinrättning (in some contexts) |
| `kaffepaus` | fika | — (no Finnish-Swedish equivalent of `fika`; use `kafferast`) |
| `roligt` | roligt (fun) | rolig + ng for "calm/peaceful" can confuse; use `kul / trevligt` |
| `prick` | (period) | (also period; but `prick` vs `punkt` varies) |

**Most product UI doesn't need sv-FI-specific treatment** beyond currency and possibly date format. When in doubt, sv-SE is understood perfectly by Finland-Swedish speakers.

---

## Self-Check Checklist (Run Before Returning Output)

### Accuracy (auto-fail on miss)

- [ ] **Compound words written as ONE word** — no särskrivning (`databas` not `data bas`).
- [ ] **Hybrid-compound verbs rejected** — no `avlinka`, `avsynca`, `cancella`, `deleta`, `downloada`.
- [ ] **Gender (en/ett)** correct on every article and definite suffix.
- [ ] **Double definiteness** present when noun has adjective: `den stora filen`.
- [ ] **Adjective agreement**: -t for ett-noun indefinite singular, -a for plural/definite.
- [ ] **V2 word order** in every main clause (verb in position 2).
- [ ] **Subordinate clause word order**: subject before verb, `inte` between them.
- [ ] **Negation placement**: after verb (main), before verb (subordinate).
- [ ] **fler vs mer**: countable uses fler/färre, uncountable uses mer/mindre.
- [ ] **No comma before `och` / `eller`**; comma before `men` / `för`.
- [ ] **Special chars å ä ö** preserved — never replaced with a/a/o.
- [ ] **ICU plurals**: `one` and `other` categories present.
- [ ] **Placeholders** {var}, {{var}}, <tag>, URLs, code identifiers preserved exactly.
- [ ] **Latin tech identifiers**: Git, API, JSON, React, etc. stay in Latin.
- [ ] **Numbers**: comma decimal (3,14), space thousands (1 000), `kr` after amount (99,99 kr).
- [ ] **Dates**: ISO 8601 (YYYY-MM-DD) default.
- [ ] **per vs för**: rate vs total — never mixed.
- [ ] **Time format**: 24-hour, `kl. 14:30`.

### Register

- [ ] **Du throughout** — never `ni` for singular formal.
- [ ] **No literary register elevation** when source is casual (no `förbli`, `otaliga`, `levereras` for casual `stay`, `countless`, `ship`).
- [ ] **Possessive forms** match: `din/ditt/dina` (du-form), not mixed with `er/ert/era` (ni-form).

### UI conventions

- [ ] Buttons use imperative (`Spara`, `Avbryt`, `Radera`).
- [ ] Status uses present + ellipsis (`Laddar…`, `Sparar…`).
- [ ] Completion is concise (`Klar`, `Översättning klar`, NOT `Klar! Översättningen är nu klar!`).
- [ ] Empty states are concise (`Inga resultat`, NOT `Inga resultat hittades`).
- [ ] File picker uses `välj`, not `bladdra`.
- [ ] Drag-drop uses `dra` and `släpp`.
- [ ] `Stöder X` not `Stöd för X`.
- [ ] Quantity: `fler än 25` not `25+`; `och {count} till` not `+{count}`.
- [ ] Error messages include next step.

### Naturalness

- [ ] No English calques (`ta plats`, `det ger mening`, `på en daglig basis`, `i termer av`, `göra en förbättring`).
- [ ] No marketing-zero calque (`Noll X` → `Utan X` / `Inga X`).
- [ ] No anglicism-verb formations (`supportera`, `deployera`, `downloada`).
- [ ] False-friend check: `aktuell ≠ actual`, `eventuellt ≠ eventually`, `semester ≠ academic term`, `kontrollera ≠ to control`.
- [ ] `återstår` not `kvarstår` for time-remaining.
- [ ] `min` not `m` for minutes; space before unit.
- [ ] Proper nouns use short forms (`USA`, `Storbritannien`).
- [ ] Lagom tone — no hype, no exclamations stacked.

### Regional (when sv-FI)

- [ ] Currency: € not kr.
- [ ] Date: DD.MM.YYYY acceptable alongside ISO.
- [ ] Phone format / postal codes appropriate to Finland.

---

## Worked Example — Standard sv-SE UI

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** neutral product UI with exclamation → casual du, present-tense status.

**Translation (sv-SE):**

> Välkommen tillbaka! Du har 3 nya filer i ditt konto. Klicka på **Fortsätt** för att granska dem eller **Avbryt** för att stanna kvar här. Sparar dina ändringar…

**Why this works:**
- `Välkommen tillbaka` — standard greeting, no `Hej!` injected.
- `Du har` — du-form throughout.
- `3 nya filer` — adjective `nya` (plural -a), noun `filer` (plural). No double-def needed since indefinite.
- `i ditt konto` — `ditt` matches neuter `konto`.
- Buttons imperative: `Fortsätt`, `Avbryt`.
- `för att granska dem / för att stanna kvar` — V2 not at play (subordinate `att`-clause: subject before verb implicit).
- Status: `Sparar dina ändringar…` (present + ellipsis).
- Possessive `dina ändringar` — plural form of din.
- Punctuation: Latin `.`, `!`, `…` all fine. Comma NOT used before `eller`.

**Same string in formal sv-SE (legal/banking):**

> Välkommen tillbaka. Du har 3 nya filer i ditt konto. Klicka på **Fortsätt** för att granska filerna eller på **Avbryt** för att avbryta. Ändringarna sparas…

(Drop `!`, switch to s-passive `sparas`, use definite `filerna` to reinforce specificity.)

**Same string for sv-FI:**

> Välkommen tillbaka! Du har 3 nya filer i ditt konto. Klicka på **Fortsätt** för att granska dem eller **Avbryt** för att stanna kvar här. Sparar dina ändringar…

(No vocabulary difference here — the source doesn't trigger any sv-FI delta. If a price were included: `5 € per språk` instead of `5 kr per språk`.)

---

## Worked Example — Compound word + V2

**Source:** Today, the system saves your file automatically every five minutes.

**Translation:**

> Idag **sparar systemet** din fil **automatiskt** var femte minut.

**Notes:**
- `Idag` fronted → V2 inversion → `sparar systemet` (verb in position 2).
- `automatiskt` adjective form for neuter context (here adverb).
- `var femte minut` — Swedish idiom for "every five minutes" (NOT `varje fem minuter`).
- No särskrivning issues; `systemet` is one word.

---

## Worked Example — ICU plurals + countable

**Source:**

```icu
{count, plural, one {# new file} other {# new files}}
```

**Translation:**

```icu
{count, plural,
  one {# ny fil}
  other {# nya filer}
}
```

Notes:
- `one`: `ny` (base form, en-noun indef. sg.).
- `other`: `nya filer` (plural adjective -a, plural noun).
- If embedded in `Lägg till X mer`, switch to `fler` since `filer` is countable: `Lägg till {count, plural, one {# fler fil} other {# fler filer}}`.

---

## When in Doubt

1. **Default to sv-SE, du-form, ISO dates, ett-or-en checked per noun.**
2. If unsure about variant → ask once, default sv-SE.
3. If a word looks like an English root with av- / upp- / in- prefixed → **stop and look up the native verb**; almost certainly `koppla bort`, `synkronisera`, `radera`, etc. exists.
4. If you typed two nouns with a space and they describe one concept → **join them**.
5. If you used `mer` with countable things → switch to `fler`.
6. If you put `ni` in singular formal → switch to `du`. Always.
