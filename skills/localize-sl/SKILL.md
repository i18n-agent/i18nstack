---
name: localize-sl
description: "Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Slovenian (sl). Slovenian's defining feature is the DUAL number — exactly 2 items takes a third grammatical number distinct from singular and plural (2 datoteki, NOT 2 datoteke; sta delala, NOT so delali). Enforces dual + ICU one/two/few/other plurals (1 / 2 dual / 3-4 / 0+5+), 6-case grammar, 3-gender agreement, Vi/ti formality (Vi capitalized), perfective/imperfective verb aspect, impersonal voice for status (Poteka analiza / se izračunava, NOT first-person Računam), neuter perfective participle for completion (Shranjeno, Naloženo), \"Ni uspelo\" + infinitive for failure, \"Samodejno\" not \"Avto-\" prefix, native Slovenian terminology (uporabnik, datoteka, mapa, brskalnik), and EUR currency with `1.234,56 €`."
---

# Translate to Slovenian (sl) — High-Fidelity Skill

## Scope & Variants

Slovenian is a single standard target — Modern Standard Slovenian (knjižna slovenščina). No regional split for product UI:

| Locale | Notes |
|--------|-------|
| `sl` / `sl-SI` | Standard Slovenian (Slovenia). Default and only target. |

**Practical reality:** Slovenian translation has **one target**. The defining quality concern is the **dual number** — a feature unique to Slovenian among major modern European languages (Sorbian also has it but is much smaller). Failing to use dual is the most-mocked Slovenian translation error.

### Slovenian is its own South Slavic language

Slovenian is mutually intelligible with Croatian and Serbian to some degree but is **structurally distinct**. Don't conflate them. Key distinguishing features:

- **Dual number** (Slovenian has it; Croatian/Serbian don't — they merged dual into plural).
- Different vocabulary: `datoteka` (sl/hr/sr same), `mapa` (sl/hr same — sr uses `fascikla/folder`), but `okno` (sl) vs `prozor` (hr/sr) for "window".
- `prihrniti` vs Croatian `spremiti` for "save" — Slovenian uses `shraniti`.
- Slovenian doesn't have ekavian/ijekavian distinction — it has its own yat reflexes.

---

## Register Auto-Detection (Apply Before Translating)

Slovenian has a strong T-V distinction (Vi/ti — called "vikanje" vs "tikanje"). Auto-detect from source:

| Source signal | Target register |
|---------------|-----------------|
| Casual / conversational / personal (`Hey!`, contractions, emoji, marketing voice, gaming) | **Informal (ti / tikanje)** — `ti` lowercase, 2nd-person sg. verb endings (`-š`: lahko, vidiš), familiar imperative (singular: izberi, klikni, odpri). |
| Neutral product UI / docs / consumer software (DEFAULT) | **Formal (Vi / vikanje)** — `Vi` capitalized for direct address, 2nd-person pl. verb endings (`-te`: lahko, vidite), polite imperative (`-te/-ite`: izberite, kliknite, odprite). Possessive `Vaš/Vaša/Vaše` capitalized. |
| Legal / banking / government / enterprise | **Formal (Vi) elevated** — same `Vi` form but full constructions, no contractions, prefer impersonal `se` constructions, native Slovenian vocabulary. |

**Hard rule: never mix levels in one text.** A string with `Lahko spremenite` (formal verb) and `tvoje nastavitve` (informal possessive) is broken.

**Capitalization rule for Vi:** `Vi / Vaš / Vaša / Vaše / Vam / Vas` are capitalized in direct second-person address.

**Default for software UI: Vi (vikanje, formal)** unless brand voice is explicitly youth/casual.

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. DUAL NUMBER — exactly 2 items takes a separate grammatical number (severity 3.0)

**THE DEFINING FEATURE OF SLOVENIAN.** Slovenian is one of the very few modern Indo-European languages that **actively preserves the dual** as a productive grammatical number distinct from plural.

For exactly 2 of anything: noun, adjective, verb auxiliary, pronoun, and past participle ALL take dedicated dual forms.

| Number | Form (with "datoteka" — file, fem.) | Adj. + Noun | Verb (past) |
|--------|------------------------------------|--------------|-------------|
| **1** (singular) | datoteka | nova datoteka | je delala |
| **2** (DUAL) | **datoteki** | **novi datoteki** | **sta delali** |
| **3, 4** (plural) | datoteke | nove datoteke | so delale |
| **5+** (gen.pl.) | datotek | novih datotek | so delale |

Same for masculine:

| Number | "sistem" (m.) | Adj. + Noun | Verb (past) |
|--------|---------------|--------------|-------------|
| 1 | sistem | nov sistem | je deloval |
| **2** | **sistema** | **nova sistema** | **sta delovala** |
| 3-4 | sistemi | novi sistemi | so delovali |
| 5+ | sistemov | novih sistemov | so delovali |

And neuter:

| Number | "okno" (n.) | Adj. + Noun | Verb (past) |
|--------|-------------|--------------|-------------|
| 1 | okno | novo okno | je delovalo |
| **2** | **okni** | **novi okni** | **sta delovali** |
| 3-4 | okna | nova okna | so delovala |
| 5+ | oken | novih oken | so delovala |

**Critical UI examples:**

| ✗ Wrong (treating 2 as plural) | ✓ Correct (using dual) | English |
|-------------------------------|------------------------|---------|
| 2 datoteke | **2 datoteki** | 2 files |
| 2 sistemi | **2 sistema** | 2 systems |
| 2 sporočila | **2 sporočili** | 2 messages (neuter dual) |
| dva nova računalniki | **dva nova računalnika** | two new computers |
| dve novi datoteke | **dve novi datoteki** | two new files |
| so delali (for 2 people) | **sta delala** (or `sta delali` if fem.) | they (two) worked |

### 2. Word integrity — verb prefixes NEVER split (severity 3.0)

Slovenian verbs with prefixes are **single words**. Splitting them is a critical error.

| ✗ Wrong (split) | ✓ Correct (joined) |
|-----------------|---------------------|
| `pre vesti` | **`prevesti`** (to translate) |
| `iz vesti` | **`izvesti`** (to execute) |
| `na ložiti` | **`naložiti`** (to upload / load) |
| `od dati` | **`oddati`** (to submit) |
| `pri javiti se` | **`prijaviti se`** (to log in) |
| `pre nesti` | **`prenesti`** (to download / transfer) |
| `za pisati` | **`zapisati`** (to write) |

**Reflexive `se / si` is SEPARATE clitic** — not attached to verb in writing. `prijaviti se`, `zaregistrirati se`, `nahajati se`. Writing `prijavitise` is wrong.

### 3. Six-case system (severity 2.5)

Slovenian uses **6 cases** (same as Slovak — no separate vocative; direct address uses nominative).

| Case | Question | Use | Example (m. "uporabnik") | Example (f. "aplikacija") |
|------|----------|-----|--------------------------|---------------------------|
| Imenovalnik (NOM) | kdo? kaj? | Subject (and direct address) | uporabnik | aplikacija |
| Rodilnik (GEN) | koga? česa? | Possession, "of", absence, 5+ count | uporabnika | aplikacije |
| Dajalnik (DAT) | komu? čemu? | Indirect object, "to" | uporabniku | aplikaciji |
| Tožilnik (ACC) | koga? kaj? | Direct object | uporabnika (animate=GEN) / sistem (inanimate=NOM) | aplikacijo |
| Mestnik (MES) | o kom? čem? | Location (always w/ prep) | o uporabniku | o aplikaciji |
| Orodnik (ORO) | s kom? čim? | "With", means | z uporabnikom | z aplikacijo |

**Critical: animate masculine accusative = genitive form.** `vidim uporabnika`, NOT `vidim uporabnik`.

### 4. Preposition + governed case (severity 2.5)

| Preposition | Case | Example |
|-------------|------|---------|
| v (in/into) | MES (location) / ACC (motion) | v sistemu / v sistem |
| na (on/onto) | MES / ACC | na zaslonu / na zaslon |
| z / s (with) | ORO | z uporabnikom, s sistemom |
| brez (without) | GEN | brez napak |
| za (for) | ACC | za uporabnika |
| od (from) | GEN | od uporabnika |
| do (until/to) | GEN | do konca |
| o (about) | MES | o uporabniku |
| po (after / per / along) | MES (after) / DAT (rate) | po prijavi / na datoteko (per file) |
| pred (before) | ORO / ACC | pred shranjevanjem / pred sistem |
| pri (at, near) | MES | pri shranjevanju |
| med (between, during) | ORO / ACC | med datotekami |
| k (to/toward) | DAT | k uporabniku |

**"per" in Slovenian:** use `na + ACC` (`na datoteko`, `na uporabnika`), `dnevno` for "per day".

### 5. ICU plurals — one / two / few / other (severity 3.0)

Slovenian's ICU plural categories are **unique** because they include the `two` category for the dual:

```icu
{count, plural,
  one {# datoteka}
  two {# datoteki}
  few {# datoteke}
  other {# datotek}
}
```

**CLDR plural category boundaries:**

| Category | Rule | Examples | Noun form |
|----------|------|----------|-----------|
| `one` | n % 100 = 1 | 1, 101, 201, 301 | **NOM singular** (datoteka) |
| `two` | n % 100 = 2 | 2, 102, 202, 302 | **DUAL** (datoteki) |
| `few` | n % 100 ∈ {3, 4} | 3, 4, 103, 104 | **NOM plural** (datoteke) |
| `other` | everything else | 0, 5-100, 105+ | **GEN plural** (datotek) |

**Critical: ICU MUST include the `two` category** for Slovenian. Falling back to just `one/other` (English-style) is a critical error — speakers will immediately notice the missing dual.

### 6. Numeral-noun agreement (severity 2.5)

| Count | Pattern | Example |
|-------|---------|---------|
| 1 | NOM sg | 1 datoteka, 1 sistem |
| **2** | **DUAL** | **2 datoteki, 2 sistema, 2 okni** |
| 3, 4 | NOM pl | 3 datoteke, 4 sistemi |
| 5+ | GEN pl | 5 datotek, 10 sistemov |
| 0 | GEN pl | 0 datotek |
| 101 | NOM sg (back to "one") | 101 datoteka |
| 102 | DUAL (back to "two") | 102 datoteki |

### 7. Three-gender adjective agreement (severity 2.0)

| Gender | Example | Adjective NOM sg. |
|--------|---------|-------------------|
| Masculine (consonant ending) | sistem, uporabnik, računalnik | **nov** sistem (NO `-i` ending on indefinite!) |
| Feminine (-a ending) | aplikacija, mapa | **nova** aplikacija |
| Neuter (-o/-e ending) | okno, sporočilo | **novo** okno |

**Note vs other Slavic:** Slovenian masculine **indefinite** adjective is `nov` (bare consonant ending) — NOT `novi`. The `-i` ending marks **definite** (only in certain syntactic positions). This is a Slovenian-specific feature different from Croatian/Serbian/Czech/Slovak.

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| novi sistem (when indefinite) | **nov sistem** (a new system) |
| novi uporabnik (when indefinite) | **nov uporabnik** |
| nova okno | **novo okno** |
| nov aplikacija | **nova aplikacija** |

### 8. Past-tense gender + number agreement (severity 2.0)

Past participles agree with subject in gender AND number (INCLUDING dual!):

| Subject | L-participle | Example |
|---------|--------------|---------|
| m. sg. | -l | on je delal |
| f. sg. | -la | ona je delala |
| n. sg. | -lo | ono je delalo |
| **m. dual** | **-la** | **onadva sta delala** |
| **f. dual** | **-li** | **onidve sta delali** |
| **n. dual** | **-li** | **onidve sta delali** (neuter dual takes f.-dual form in modern Slovenian) |
| m. pl. | -li | oni so delali |
| f. pl. | -le | one so delale |
| n. pl. | -la | ona so delala |

Dual forms with auxiliary `sta` (for 2 people) — NOT `so` (which is plural for 3+).

### 9. Verb aspect — perfective vs imperfective (severity 2.0)

| Imperfective (process, ongoing) | Perfective (single completed event) | English |
|--------------------------------|--------------------------------------|---------|
| shranjevati | shraniti | save |
| brisati | izbrisati | delete |
| nalagati | naložiti | upload / load |
| prenašati | prenesti | download / transfer |
| odpirati | odpreti | open |
| zapirati | zapreti | close |
| ustvarjati | ustvariti | create |
| urejati | urediti | edit |
| prevajati | prevesti | translate |
| prijavljati se | prijaviti se | log in |

**UI patterns by aspect:**
- Buttons (single action) → **perfective imperative**: `Shrani`, `Izbriši`, `Pošlji`, `Izberi`.
- Ongoing status → **imperfective verbal noun** (`Shranjevanje…`, `Nalaganje…`) or **reflexive imperfective** (`se shranjuje`).
- Completed → **perfective neuter participle** (`Shranjeno`, `Naloženo`).

### 10. Verb-construction integrity — no stacked finite verbs (severity 2.0)

English `-ing` (gerund as adverbial) MUST be rendered with **deležje na -č** (present adverbial participle: `gradeč`, `delajoč`, `pišoč`) OR **`med` + verbal noun**, NOT a second finite clause.

Note: the adverbial participle in modern Slovenian is somewhat literary; the **`med` + verbal noun** construction is more common in product copy.

| ✗ Stacked finite | ✓ Adverbial participle / med + noun | English |
|------------------|--------------------------------------|---------|
| `Preživel sem 6 let gradil sem podjetje` | **`Preživel sem 6 let z gradnjo podjetja`** OR **`Preživel sem 6 let gradeč podjetje`** | I spent 6 years building the business |
| `Delal sem medtem ko sem pisal poročilo` | **`Delal sem med pisanjem poročila`** OR **`Delal sem pišoč poročilo`** | I worked while writing the report |

### 11. Diacritics — Č Š Ž essential (severity 2.5)

Slovenian uses three special letters: **č š ž**. Never strip them.

| ✗ Stripped | ✓ Correct |
|------------|-----------|
| sirina | **širina** |
| nacin | **način** |
| zelo | **želo** (or `zelo` = "very" — they're different words!) |
| krizisce | **križišče** |
| druzba | **družba** |

Slovenian does NOT use `ć / đ` (those are Croatian/Serbian/Bosnian markers — if you see them in a Slovenian translation, something is wrong).

---

## Pronouns and Possessives

### Personal pronouns

| English | Slovenian | Notes |
|---------|-----------|-------|
| I | jaz | |
| you (sg. informal) | ti | |
| you (sg./pl. formal — capitalize) | Vi | Always capitalized in direct address |
| you (pl. informal) | vi | lowercase when truly plural informal |
| he | on | |
| she | ona | |
| it | ono | |
| **we (two)** | **midva (m.) / midve (f.)** | DUAL pronoun |
| **you (two)** | **vidva (m.) / vidve (f.)** | DUAL pronoun |
| **they (two)** | **onadva (m.) / onidve (f.)** | DUAL pronoun |
| we (3+) | mi | |
| you (3+) | vi | |
| they (m. 3+) | oni | |
| they (f. 3+) | one | |
| they (n. 3+) | ona | |

### Possessive pronouns

| Person | m. sg. | f. sg. | n. sg. |
|--------|--------|--------|--------|
| moj (my) | moj | moja | moje |
| tvoj (your sg.) | tvoj | tvoja | tvoje |
| **Vaš (your formal — capitalize)** | **Vaš** | **Vaša** | **Vaše** |
| njegov (his) | njegov | njegova | njegovo |
| njen (her) | njen | njena | njeno |
| svoj (reflexive — own) | svoj | svoja | svoje |
| naš (our) | naš | naša | naše |
| njihov (their) | njihov | njihova | njihovo |

**Reflexive `svoj`** is required when possessor = subject of same clause.

---

## UI Conventions

### Buttons — perfective imperative

| English | ✓ Slovenian (Vi formal) | (ti informal) |
|---------|--------------------------|---------------|
| Save | **Shranite** | **Shrani** |
| Cancel | **Prekličite** | **Prekliči** |
| Delete | **Izbrišite** | **Izbriši** |
| Send | **Pošljite** | **Pošlji** |
| Edit | **Uredite** | **Uredi** |
| Search | **Iščite** | **Išči** |
| Confirm | **Potrdite** | **Potrdi** |
| Continue | **Nadaljujte** | **Nadaljuj** |
| Submit | **Pošljite** / **Oddajte** | **Pošlji** / **Oddaj** |
| Sign in / Log in | **Prijavite se** | **Prijavi se** |
| Sign out | **Odjavite se** | **Odjavi se** |
| Sign up | **Registrirajte se** | **Registriraj se** |
| Next | **Naprej** / **Naslednje** | (same) |
| Back | **Nazaj** | (same) |
| Done | **Končano** / **Opravljeno** | (same) |
| OK | **V redu** / **OK** | (same) |
| Close | **Zaprite** | **Zapri** |
| Upload | **Naložite** | **Naloži** |
| Download | **Prenesite** | **Prenesi** |
| Refresh | **Osvežite** | **Osveži** |
| Settings | **Nastavitve** | (same) |
| Apply | **Uporabite** | **Uporabi** |
| Reset | **Ponastavite** | **Ponastavi** |
| Select all | **Izberite vse** | **Izberi vse** |
| Add more | **Dodajte še** (NOT `Dodaj več`) | **Dodaj še** |

### Status messages — three distinct patterns

**Ongoing (in-flight)** → **verbal noun** (`Nalaganje…`) OR **reflexive imperfective** (`se nalaga…`) OR **`Poteka` + verbal noun** (NEVER first-person)

| English | ✓ Slovenian |
|---------|-------------|
| Loading… | **Nalaganje…** / **Datoteka se nalaga…** / **Poteka nalaganje…** |
| Saving… | **Shranjevanje…** / **se shranjuje…** |
| Sending… | **Pošiljanje…** / **se pošilja…** |
| Processing… | **Obdelava…** / **se obdeluje…** / **Poteka obdelava…** |
| Connecting… | **Povezovanje…** |
| Searching… | **Iskanje…** / **se išče…** |
| Translating… | **Prevajanje…** / **Poteka prevod…** |
| Please wait | **Prosimo, počakajte** / **Počakajte…** |

**Critical impersonal voice rule:** NEVER first-person (`Računam…`, `Analiziram…`, `Obdelujem…`) — sounds awkward. Always impersonal.

**Completed** → **Neuter perfective participle** (impersonal)

| English | ✓ Slovenian |
|---------|-------------|
| Saved | **Shranjeno** |
| Done | **Končano** / **Opravljeno** |
| Translation complete | **Prevedeno** / **Prevod končan** |
| File uploaded | **Naloženo** / **Datoteka naložena** |
| Sent | **Poslano** |
| Payment successful | **Plačilo uspešno** / **Plačano** |

**Failed** → **`Ni uspelo` + infinitive** OR **`Napaka pri` + verbal noun**

| English | ✓ Slovenian |
|---------|-------------|
| Save failed | **Ni uspelo shraniti** / **Napaka pri shranjevanju** |
| Upload failed | **Ni uspelo naložiti** / **Napaka pri nalaganju** |
| Translation failed | **Ni uspelo prevesti** / **Napaka pri prevajanju** |
| File not found | **Datoteka ni najdena** / **Datoteka ne obstaja** |

NEVER use:
- ✗ `Prevod ni uspel` (sounds like "the translation didn't succeed" — flat narrative tone)
- ✗ `Shranjevanje neuspešno` (calque)

### Empty states — `Ni X` / `Ni izbrano`

| ✗ Verbose / bare | ✓ Concise |
|------------------|-----------|
| Prazno | **Ni rezultatov** / **Ni najdenih elementov** |
| Nič tukaj | **Ni datotek** / **Ni razpoložljivih podatkov** |

### Drag-and-drop

- drag → **povlecite** (Vi) / **povleci** (ti)
- drop → **spustite** (Vi) / **spusti** (ti)
- Combined: **`Povlecite datoteke sem`** (Drag files here).

### File picker — `Izberi` not `Prebrskaj`

Standard in Chrome SL / Windows SL:

| ✗ Older / navigation | ✓ Modern / action-oriented |
|----------------------|----------------------------|
| Prebrskaj datoteke | **Izberi datoteke** |
| Prebrskaj datoteko | **Izberi datoteko** |
| kliknite za brskanje | **kliknite za izbiro** |

### Quantity expressions

| ✗ Calque | ✓ Native |
|----------|----------|
| 25+ jezikov | **več kot 25 jezikov** |
| +{count} več | **in {count} drugih** / **še {count}** |

`Dodaj več` ✗ → `Dodaj še` ✓ (idiomatic).

### Error messages — what + next step

| ✗ Bare | ✓ With next step |
|--------|------------------|
| Datoteka ni najdena. | **Datoteka ni najdena. Preverite pot.** |
| Napaka omrežja. | **Napaka omrežja. Poskusite znova.** |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Slovenian | Notes |
|------|-----------|-------|
| Question mark | `?` | Same as English |
| Comma | `,` | Different conjunction rules |
| Period | `.` | Same |
| Colon | `:` | Same |
| Quotation marks | **`„…"`** (low-9/high-9) OR **`»…«`** (French-style, inward) | Both standard in Slovenian |
| Nested quotes | `‚…'` or `›…‹` | |

### Comma rules

| Rule | Example |
|------|---------|
| **NO comma** before `in` (and) | Izberite datoteko **in** kliknite. |
| **NO comma** before `ter` (and, formal) | hitro **ter** učinkovito. |
| **NO comma** before `ali` (or) | Izberite datoteko **ali** mapo. |
| **NO comma** before `pa` (but/and contrast) | (depends on emphasis) |
| **Comma** before `da` (that, subordinating) | Vidim, **da** je datoteka odprta. |
| **Comma** before `ki` (relative — non-restrictive) | Datoteka, **ki** je shranjena… |
| **Comma** before `če` (if) | Shranite, **če** želite. |
| **Comma** before `ker` (because) | Preklicano, **ker** ni uspelo. |
| **Comma** before `ko` (when) | Počakajte, **ko** bo končano. |
| **Comma** before `a / ampak / toda` (but/contrast) | Hitro, **ampak** učinkovito. |

### Numbers

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **period (.)** OR space | 1.234.567 OR 1 234 567 |
| Decimal separator | **comma (,)** | 3,14 / 99,99 |
| Negative | `−25` or `-25` | |
| Percent | `25 %` (with space) or `25%` | |

### Dates

| Format | Example | Use |
|--------|---------|-----|
| D. M. YYYY | **15. 1. 2024** | Default — spaces around periods |
| D. mesec YYYY | **15. januar 2024** | Long-form prose (month NOT in genitive — unlike Croatian/Slovak) |
| YYYY-MM-DD | 2024-01-15 | Technical/API only |

**Slovenian month names (lowercase, declines in some forms):**

| # | Slovenian |
|---|-----------|
| 1 | januar |
| 2 | februar |
| 3 | marec |
| 4 | april |
| 5 | maj |
| 6 | junij |
| 7 | julij |
| 8 | avgust |
| 9 | september |
| 10 | oktober |
| 11 | november |
| 12 | december |

**Note: in Slovenian long-form dates, the month is in NOMINATIVE** (`15. januar 2024`) — different from Croatian (genitive: `15. siječnja 2024`) and Slovak (genitive: `15. januára 2024`). The figure-only form uses periods with spaces (`15. 1. 2024`).

**Weekdays (lowercase):** ponedeljek, torek, sreda, četrtek, petek, sobota, nedelja.

Week starts **Monday**.

### Time

- 24-hour preferred: `14:30` or `14.30`.
- 12-hour rarely used.

### Currency — Euro (EUR / €)

| Format | Pattern | Example |
|--------|---------|---------|
| Symbol after amount | `€` | **99,99 €** |
| ISO code | EUR | **99,99 EUR** |

Slovenia adopted the euro on 1 January 2007 (previously: Slovenian tolar).

---

## Terminology — preferred Slovenian terms

| English | ✓ Slovenian preferred | ✗ Avoid |
|---------|------------------------|---------|
| user | **uporabnik** | user |
| account | račun (banking) / uporabniški račun (account) | akaunt |
| password | geslo | password |
| settings | **nastavitve** | setingi |
| dashboard | **nadzorna plošča** | dashboard |
| email | e-pošta / e-poštni naslov | mejl |
| link | povezava | link |
| website | spletno mesto / spletna stran | website |
| folder | mapa | folder |
| file | **datoteka** | fajl |
| device | naprava | device |
| phone | telefon / mobilni telefon | — |
| computer | **računalnik** | kompjuter |
| application / app | aplikacija | — |
| update (v.) | posodobiti | apdejtovati |
| save | shraniti | sejvati |
| delete | izbrisati | deletovati |
| upload | **naložiti** | uploadati |
| download | **prenesti** | downloadati |
| sign in / log in | prijaviti se | logirati se |
| sign up | registrirati se | — |
| search | iskati / iskanje | search |
| click | klikniti / pritisniti | — |
| share | deliti | šerati |
| profile | profil | — |
| notifications | obvestila | notifikacije |
| privacy | zasebnost | — |
| terms | pogoji | — |
| support | podpora | — |
| help | pomoč | — |
| feedback | povratne informacije | — |
| menu | meni | — |
| home | domov / domača stran | — |
| **browser** | **brskalnik** | browser |
| **screen** | zaslon | — |
| **keyboard** | tipkovnica | — |
| **mouse** | miška | — |
| **software** | programska oprema | — |
| build (software) | ustvariti / zgraditi | graditi (= construction) |
| deploy | namestiti / objaviti | deployati |
| pipeline (CI/CD) | pipeline (keep) | — |
| commit (git) | commit (keep) | — |
| merge | združiti / spojiti | — |
| repository | repozitorij | — |
| sync | sinhronizirati | — |
| API | API (keep — Latin always) | — |
| endpoint | končna točka / endpoint | — |
| token | žeton / token | — |
| cache | predpomnilnik / cache | — |
| log (n.) | dnevnik / log | — |

### Tech identifiers — keep in Latin script

Inside Slovenian text (Latin alphabet anyway), these stay as-is:
- Git, GitHub, Docker, npm, pip
- HTTP, REST, GraphQL, OAuth, JWT
- JSON, XML, YAML, CSV, PDF
- Brand names: Google, Microsoft, Apple, iPhone, Android
- Commands, paths, URLs, code, placeholders

---

## False Friends — Critical

| Slovenian word | Actually means | NOT this | Correct for the English |
|----------------|----------------|----------|--------------------------|
| **vznemirjen** | agitated / disturbed (can be negative) | safer "excited" | "excited (looking forward)" → **veselim se** / **navdušen** |
| aktualen | current / topical | "actual" | "actual" → **dejanski** / **resničen** |
| realizirati | to implement / carry out | "to realize (understand)" | "realize" → **spoznati** / **uvideti** |
| eventualno | possibly / perhaps | "eventually" | "eventually" → **končno** / **na koncu** |
| kontrolirati | to check / verify | "to control (manage)" | "control" → **upravljati** / **voditi** |
| simpatičen | likeable / pleasant | "sympathetic (compassionate)" | "sympathetic" → **sočuten** |

---

## Calque / Anti-Pattern List

| ✗ Calque | ✓ Native Slovenian | Reason |
|----------|---------------------|--------|
| To naredi smisel | **To je smiselno** / **To je logično** | "Makes sense" calque |
| na koncu dneva | **konec koncev** / **navsezadnje** | "At the end of the day" calque |
| vzeti mesto | **potekati** / **odvijati se** | "Take place" calque |
| bazirano na | **na podlagi** / **temelječ na** | "Based on" calque |
| v redu da | **da bi** / **zato da** | "In order to" calque |
| na dnevni bazi | **dnevno** / **vsak dan** | "On a daily basis" calque |
| v smislu | **glede** / **kar zadeva** | "In terms of" calque (when overused) |
| **Avto-zaznano** | **Samodejno zaznano** | "Auto-X" — use full adverb `samodejno` |
| **Avto-shranjeno** | **Samodejno shranjeno** | "Auto-X" |
| **Avto-popravek** | **Samodejni popravek** | Use full adjective |
| **Avto-dopolnjevanje** | **Samodejno dopolnjevanje** | Use full adjective (neuter) |
| **Prevedeni rezultati** (header) | **Rezultati prevajanja** | English Past-Participle + Noun → Slovenian Noun + Genitive of verbal noun |
| **Posodobljene nastavitve** (header) | **Nastavitve posodobitve** / **Spremembe nastavitev** | Same pattern |
| **Uvožene datoteke** (header) | **Datoteke uvoza** / **Uvoženi dokumenti** | Same pattern |
| **opcija jezika** (N+N) | **jezikovne možnosti** / **izbira jezika** | Use adj+N or genitive |
| **projekt mapa** | **mapa projekta** / **projektna mapa** | Use genitive or adjective |
| **uporabnik nastavitve** | **uporabniške nastavitve** / **nastavitve uporabnika** | Use adj or genitive |
| **preferenca tona** | **želeni ton** / **izbira tona** | Anglicism noun → native adj |
| **Nič izpadov** / **Nič napak** | **Brez izpadov** / **Brez napak** | "Zero X" marketing calque |
| **AI-poganjan** | **temelječ na AI** / **s pomočjo AI** | "X-powered" calque |
| **podatki-usmerjen** | **podatkovno usmerjen** / **temelječ na podatkih** | "X-driven" calque |
| **per datoteka** | **na datoteko** | "per X" calque |
| **per uporabnik** | **na uporabnika** | "per X" |
| **per dan** | **dnevno** / **na dan** | "per X" |
| **Prevod ni uspel** | **Ni uspelo prevesti** / **Napaka pri prevajanju** | Personal "didn't succeed" → impersonal |
| **Shranjevanje neuspešno** | **Ni uspelo shraniti** / **Napaka pri shranjevanju** | Calque → impersonal |
| **Datoteka se je shranila** | **Shranjeno** / **Datoteka shranjena** | Reflexive past → impersonal participle |
| **Prekliči izbiro vsega** | **Prekliči vse** / **Odznači vse** | Button brevity |
| **Izberi izbiro vseh** | **Izberi vse** | Button brevity / redundancy |
| **Dodaj več** | **Dodaj še** | "Add more" — use idiomatic `še` |
| **Združene države Amerike** (UI) | **ZDA** | UI short form |
| **2 datoteke** (treating as plural) | **2 datoteki** (DUAL!) | THE Slovenian rule |
| **so delali** (for 2) | **sta delala/delali** (DUAL!) | THE Slovenian rule |

---

## Self-Check Checklist (Run Before Returning Output)

### DUAL — auto-fail on miss (severity 3.0)

- [ ] **Every count of exactly 2** uses dual form on noun, adjective, AND verb auxiliary.
- [ ] **ICU plurals include `two` category** (NOT just one/other or one/few/other).
- [ ] **Dual past tense**: `sta delala` (m. dual) / `sta delali` (f. dual / n. dual) — NOT `so delali` (which is plural for 3+).
- [ ] **Dual adjective**: `dva nova računalnika` (m.), `dve novi datoteki` (f.), `dve novi okni` (n.).
- [ ] **Dual pronouns**: midva/midve (we two), vidva/vidve (you two), onadva/onidve (they two).

### Accuracy

- [ ] **Word integrity** — prefixes joined (`prevesti`, `naložiti`, `odpreti`, `prijaviti`). Reflexive `se` separate.
- [ ] **Six-case system** correct (no separate vocative — direct address uses NOM).
- [ ] **Animate masc. accusative = genitive** (`vidim uporabnika`).
- [ ] **Masculine indefinite adjective is bare**: `nov sistem` (NOT `novi sistem` when indefinite).
- [ ] **Gender agreement** on every noun-adj-verb triple.
- [ ] **ICU plurals**: `one / two / few / other` (1 / 2 / 3-4 / 0+5+). All four categories present.
- [ ] **Numeral-noun**: 1=NOM.sg, 2=DUAL, 3-4=NOM.pl, 5+=GEN.pl.
- [ ] **Verb aspect** correct.
- [ ] **Past-tense gender + number agreement** including dual.
- [ ] **No stacked finite verbs** from English -ing — use `med + verbal noun` or `-č` participle.
- [ ] **Placeholders preserved**.
- [ ] **Latin tech identifiers** intact.
- [ ] **Numbers**: comma decimal (3,14), period or space thousands (1.234), `€` after amount.
- [ ] **Dates**: `15. 1. 2024` (spaces!) or `15. januar 2024` (month in **nominative** — unlike Croatian/Slovak).
- [ ] **Time**: 24-hour.
- [ ] **per**: `na + ACC` for rate, `dnevno` for "per day".
- [ ] **Diacritics**: `č š ž` preserved. No `ć / đ / dj` (those are Croatian).

### Register

- [ ] **Vi/ti chosen and applied consistently**.
- [ ] **`Vi / Vaš / Vaša / Vaše` capitalized** in direct address.

### UI conventions

- [ ] Buttons use **perfective imperative** (Vi `Shranite` or ti `Shrani`).
- [ ] Status ongoing: **verbal noun** (`Nalaganje…`) OR **reflexive `se`** (`se nalaga…`) OR **`Poteka` + noun**. NEVER first-person.
- [ ] Status completed: **neuter perfective participle** (`Shranjeno`, `Prevedeno`).
- [ ] Status failed: **`Ni uspelo + infinitive`** OR **`Napaka pri + verbal noun`**.
- [ ] Empty state: `Ni + GEN` (`Ni rezultatov`).
- [ ] File picker: `Izberi`, not `Prebrskaj`.
- [ ] Drag-drop: `Povlecite` + `Spustite`.
- [ ] Quantity: `več kot 25`, `še {count}`.
- [ ] Error messages include next step.

### Naturalness

- [ ] No English calques (`To naredi smisel`, `na koncu dneva`, `vzeti mesto`, `bazirano na`).
- [ ] **Past-Participle + Noun headers** → **Noun + Genitive of verbal noun** (`Rezultati prevajanja`).
- [ ] **Auto-X prefix** → full adverb `Samodejno`.
- [ ] **N+N compounds** → adj+N or genitive.
- [ ] **No verbose collocations** (use direct verbs).
- [ ] **No false friends**: `vznemirjen ≠ excited (positive)`, `aktualen ≠ actual`, `realizirati ≠ realize`, `eventualno ≠ eventually`.
- [ ] **Proper-noun short forms** (`ZDA`, `ZK`).

---

## Worked Example — Standard sl formal UI

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** neutral product UI → **Vi (formal)**, perfective imperative buttons.

**Translation:**

> Dobrodošli nazaj! V svojem računu imate 3 nove datoteke. Kliknite **Nadaljuj**, če jih želite pregledati, ali **Prekliči**, če želite ostati tukaj. Vaše spremembe se shranjujejo…

**Why this works:**
- `Dobrodošli nazaj` — formal plural greeting.
- `V svojem računu` — `v` + MES; `računu` masc. MES sg.; `svojem` reflexive possessive.
- `Imate` — Vi-form verb.
- `3 nove datoteke` — `3` triggers `few` (NOM pl); `datoteka` is f.; `nove` is f. pl. adjective. (If it were 2: `2 novi datoteki` — DUAL.)
- Buttons: `Nadaljuj`, `Prekliči` (perfective imperative, ti-form — for Vi alternative would be `Nadaljujte`, `Prekličite`).
- `če jih želite pregledati / če želite ostati` — `če` + present (correct Slovenian construction).
- Status: `Vaše spremembe se shranjujejo…` — imperfective reflexive (impersonal). `Vaše` capitalized formal. `spremembe` is f. pl., `shranjujejo` is 3rd-person plural reflexive.
- Comma before `če` ✓; no comma before `ali` ✓.

---

## Worked Example — DUAL in action

**Source:** 2 files saved. They (the two files) are uploaded.

**Translation:**

> Shranjeni sta 2 datoteki. Datoteki sta naloženi.

**Why this works:**
- `2 datoteki` — DUAL form (NOT `2 datoteke`).
- `Shranjeni sta` — `sta` is the dual auxiliary (NOT `so` which is plural for 3+).
- `Shranjeni` is the dual past participle (f. dual = -i ending).
- `naloženi sta` — same pattern.

**Compare with 3 files:**

> Shranjene so 3 datoteke. Datoteke so naložene.

(`so` is plural, `datoteke` is plural noun, `Shranjene` is plural participle.)

**And with 5 files:**

> Shranjenih je 5 datotek. Datoteke so naložene.

(`5` triggers `other` = GEN pl; `5 datotek` GEN pl. Note: for the 2nd sentence using "the files" as definite plural, `datoteke so naložene` uses pl.)

---

## Worked Example — ICU plurals (the FOUR-category expansion)

**Source:**

```icu
You have {count, plural, one {# new message} other {# new messages}}.
```

**Translation (full Slovenian four-category expansion — critical to include `two`):**

```icu
Imate {count, plural,
  one {# novo sporočilo}
  two {# novi sporočili}
  few {# nova sporočila}
  other {# novih sporočil}
}.
```

Notes:
- `one` (1, 101, 201…): `1 novo sporočilo` — n. NOM sg.
- **`two` (2, 102, 202…): `2 novi sporočili` — n. DUAL.** (DON'T skip this!)
- `few` (3, 4, 103, 104…): `3 nova sporočila` — n. NOM pl.
- `other` (0, 5+, 105+): `5 novih sporočil` — n. GEN pl.

---

## Worked Example — Status messages

| State | English | ✓ Slovenian |
|-------|---------|-------------|
| Ongoing | Saving… | **Shranjevanje…** / **Datoteka se shranjuje…** / **Poteka shranjevanje…** (NOT `Shranjujem…` first-person) |
| Completed | Saved | **Shranjeno** (NOT `Datoteka se je shranila` reflexive past) |
| Failed | Save failed | **Ni uspelo shraniti** / **Napaka pri shranjevanju** (NOT `Shranjevanje ni uspelo` flat or `Shranjevanje neuspešno` calque) |

---

## When in Doubt

1. **Default to sl, Vi (formal), perfective imperative buttons, dual where count = 2.**
2. **If you see `2 X-e/-i/-a` in plural form → switch to DUAL** (`2 datoteki`, `2 sistema`, `2 okni`).
3. **If you see `so delali` for 2 people → switch to `sta delala/delali`**.
4. **If ICU plural skips `two` category → add it**.
5. If you wrote `novi sistem` when indefinite → switch to bare `nov sistem`.
6. If a verb prefix has a space (`pre vesti`) → join it: `prevesti`.
7. If `se` is attached to a verb (`prijavitise`) → separate it: `prijaviti se`.
8. If you used `vznemirjen` for positive "excited" → switch to `veselim se` / `navdušen`.
9. If you wrote `Datoteka se je shranila` → use impersonal `Shranjeno`.
10. If you wrote `Shranjevanje neuspešno` → use `Ni uspelo shraniti` / `Napaka pri shranjevanju`.
11. If you used first-person status (`Računam…`) → switch to impersonal `Poteka izračun…` / `se izračunava…`.
12. If you used `Avto-` prefix → expand to `Samodejno` / `Samodejna` / `Samodejno` (adjective form per gender).
13. If you used `ć / đ` letters → those are Croatian/Serbian, not Slovenian — replace with `č / d`.
14. If a date is `15. januarja 2024` → use **nominative** `15. januar 2024` (Slovenian nominative, NOT genitive like Croatian/Slovak).
15. If currency is SIT or tolar → fix to `€` / `EUR` (Slovenia adopted euro 2007).
