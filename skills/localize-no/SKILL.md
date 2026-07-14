---
name: localize-no
description: "Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Norwegian (no / nb Bokmål / nn Nynorsk). Asks the user to choose between Bokmål (~85% of users, default for `no`) and Nynorsk (~15%, structurally distinct written standard) on first use, then enforces variant-specific vocabulary (jeg/eg, ikke/ikkje, hva/kva, hvordan/korleis), 3-gender system (en/ei/et) with feminine-optional rule, V2 word order, outward guillemets «...», DD.MM.YYYY dates, comma decimals with space thousands, du-form universality (De is archaic), hybrid-compound verb rejection (no avlinke), and source-register matching."
---

# Translate to Norwegian (no) — High-Fidelity Skill

## Scope & Variants — CRITICAL

Norway has **TWO official written standards**, both required by law to be supported by government:

| Locale | Name | Speakers using daily | Use case | Closest cousin |
|--------|------|----------------------|----------|----------------|
| `nb` / `no` | **Bokmål** ("book language") | ~85-90% | Default for software, business, news, mainstream media | Danish (historical) |
| `nn` | **Nynorsk** ("new Norwegian") | ~10-15% | Western Norway counties, education in some regions, mandated government parity | Western dialects + Old Norse |

**These are not dialects — they are two distinct written standards.** Words, spellings, grammar, and idioms differ. Mixing them within a single text is a **critical error**.

**`no` locale code is conventionally Bokmål** (since Bokmål is the dominant variant), but to be explicit, prefer `nb` for Bokmål and `nn` for Nynorsk.

### When the target locale is unspecified

**Always ask** on first use if the user requests just "Norwegian":

> Norwegian has two official written standards. Which one should I target?
>
> - **Bokmål (`nb` / `no`, Recommended)** — Used by ~85-90% of Norwegians. Standard for software, business, mainstream media. Closer to Danish historically.
> - **Nynorsk (`nn`)** — Used by ~10-15%. Mandated for some government and education contexts. Structurally distinct (jeg→eg, ikke→ikkje, hva→kva).
> - **Both (parity localization)** — Some products legally require both. I'll deliver Bokmål + Nynorsk side-by-side.

Default to **Bokmål** if no answer.

### Bokmål vs Nynorsk — core lexical/grammatical differences

The Bokmål-vs-Nynorsk delta is **everywhere**, not just a few cosmetic word swaps. Below is the high-frequency core. If you've been asked for Nynorsk, you MUST apply ALL of these — not just some:

| English | Bokmål | Nynorsk |
|---------|--------|---------|
| I | jeg | eg |
| not | ikke | ikkje |
| what | hva | kva |
| how | hvordan | korleis |
| who | hvem | kven |
| where | hvor | kvar |
| why | hvorfor | kvifor |
| when | når | når (same) |
| some / someone | noen / noen | nokon / nokon |
| something | noe | noko |
| nothing | ingenting | ingenting / inkje |
| we | vi | vi (same) |
| me / us | meg / oss | meg / oss (same) |
| you (sg.) | du | du (same) |
| your | din/ditt/dine | din/ditt/dine (same) |
| have / had | har / hadde | har / hadde (same) |
| be / was | er / var | er / var (same) |
| to do / does | å gjøre / gjør | å gjere / gjer |
| from | fra | frå |
| their | deres | deira |
| many | mange | mange (same) |
| use / uses | bruke / bruker | bruke / brukar |
| save / saves | lagre / lagrer | lagre / lagrar |
| open / opens | åpne / åpner | opne / opnar |
| close / closes | lukke / lukker | lukke / lukkar (or stengje) |
| would | ville | ville / skulle |
| can / could | kan / kunne | kan / kunne (same) |
| -tion suffix | -sjon (informasjon) | -sjon (informasjon) (mostly same) |
| present tense ending | -er (lagrer, åpner) | **-ar / -er** (lagrar, kjem) — verb-class dependent |

**Verb endings are the biggest tell:** Bokmål's `-er` ending on most present-tense verbs becomes Nynorsk's `-ar` for `a-class` verbs (`lagrar`, `klikkar`, `brukar`). For `e-class` verbs, both stay `-er` (`kjem`, `gjer`).

### Whole-sentence Bokmål vs Nynorsk comparison

| English | Bokmål | Nynorsk |
|---------|--------|---------|
| I don't know what to do. | **Jeg vet ikke hva jeg skal gjøre.** | **Eg veit ikkje kva eg skal gjere.** |
| Save your changes. | **Lagre endringene dine.** | **Lagre endringane dine.** |
| The file was not found. | **Filen ble ikke funnet.** | **Fila vart ikkje funnen.** |
| Click here to continue. | **Klikk her for å fortsette.** | **Klikk her for å halde fram.** |
| How do I sign in? | **Hvordan logger jeg inn?** | **Korleis loggar eg inn?** |
| We can help you. | **Vi kan hjelpe deg.** | **Vi kan hjelpe deg.** (same) |
| Are you sure? | **Er du sikker?** | **Er du sikker?** (same) |

**Notice:** even when whole sentences look similar, every short word (jeg/eg, ikke/ikkje, hva/kva, hvordan/korleis) shifts. Mixing is immediately visible to native speakers.

---

## Register Auto-Detection (Apply Before Translating)

Norwegian is **extremely informal by default**. The `De` form (formal singular "you") is so archaic that even royalty are addressed as `du` in modern contexts. Norwegian society is famously egalitarian, and this is enforced in software UI.

Auto-detect from source:

| Source signal | Target register (Bokmål or Nynorsk — same principle) |
|---------------|------------------------------------------------------|
| Casual / conversational (`Hey!`, contractions, emoji, marketing voice) | **Casual du** — direct verbs, short sentences, avoid literary vocabulary (`forbli` → `bli værende`). |
| Neutral product UI / docs (DEFAULT) | **Neutral du** — du throughout, imperative buttons, present-tense status. |
| Legal / banking / government | **Formal du** — still `du`, but use full forms, prefer s-passive or impersonal `man`, no contractions. |

**Hard rule: NEVER use `De` / `Deres` in modern Norwegian UI.** It is virtually extinct. Even formal Norwegian government communication uses `du` today.

**Hard rule: source register matching for vocabulary** — if source is casual English (`stay`, `countless`, `ship`), do NOT elevate to literary Norwegian (`forbli`, `utallige`, `leveres`). Match the register.

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. NEVER mix Bokmål and Nynorsk (severity 2.5)

Pick one written standard and stay consistent throughout the entire string set. A single `eg` in a Bokmål translation, or a single `jeg` in Nynorsk, is an immediate quality failure.

**Detection test:** if your translation contains BOTH `jeg/eg` or BOTH `ikke/ikkje` or BOTH `hva/kva`, you've mixed. Pick one column.

### 2. Hybrid-compound verb anti-pattern (Norwegian prefix + English stem) — REJECT (severity 2.5)

A common AI translation failure: bolt a Norwegian verbal prefix (`av-`, `fra-`, `ut-`, `opp-`, `inn-`) onto a raw English root (`link`, `sync`, `share`, `stream`, `pair`, `merge`, `push`) to produce a non-word.

| ✗ Wrong (hybrid) | ✓ Correct (Bokmål) | ✓ Correct (Nynorsk) |
|------------------|---------------------|---------------------|
| `avlinke` / `avlinket` | **koble fra** / **frakoblet** | **kople frå** / **frakopla** |
| `avsynce` | **synkronisere** / **fjerne synkronisering** | **synkronisere** |
| `delee` / `delete` (as Norwegian verb) | **slette** | **slette** |
| `pairee` | **pare sammen** / **koble sammen** | **para saman** / **kople saman** |
| `mergee` | **slå sammen** | **slå saman** |
| `pushee` | **sende inn** / **pushe** (git context only) | **sende inn** |
| `downloade` | **laste ned** | **laste ned** |
| `uploade` | **laste opp** | **laste opp** |
| `cancele` | **avbryte** | **avbryte** |
| `updatee` | **oppdatere** | **oppdatere** |

**Verification test:** if you used a Norwegian prefix + an English-looking stem, check Norwegian dictionaries (Bokmålsordboka or Nynorskordboka) before accepting it. Standard Norwegian has native forms for virtually every IT concept.

A few attested loans that are acceptable: `streame`, `chatte`, `mejle` (rare; usually `e-poste` or just `sende e-post`), `googler`, `tweete`. These have entered the language. **Their hybrid prefixed forms generally have not.**

### 3. Gender — `en` / `ei` / `et` (3 genders, feminine often optional) (severity 2.0)

Norwegian Bokmål has three grammatical genders, but **feminine is optional** — feminine nouns can usually be inflected as masculine:

| Gender | Indefinite | Definite | Bokmål example |
|--------|-----------|----------|----------------|
| Masculine (en) | en bil | bilen | en bil → bilen |
| Feminine (ei) | ei bok | boka | ei bok → boka |
| Feminine treated as masculine (acceptable) | en bok | boken | en bok → boken |
| Neuter (et) | et hus | huset | et hus → huset |

**Common IT nouns and their gender (Bokmål):**

| en (masc.) | et (neuter) |
|------------|-------------|
| en fil (file) | et system (system) |
| en mappe (folder) | et konto (account) — wait: konto is `et`, account |
| en plattform (platform) | et problem (problem) |
| en app (app) | et passord (password) |
| en knapp (button) | et nettverk (network) |
| en innstilling (setting) | et dokument (document) |
| en bruker (user) | et alternativ (option) |
| en lenke (link) | et navn (name) |
| en side (page) | et tema (theme) |
| en oppdatering (update) | et kort (card) |
| en feil (error) | et felt (field) |
| en e-post (email) | et nettsted (website) |
| en konto — WAIT: it's `en konto` in some, `et konto` in others; ATTESTED: **en konto** is common in Bokmål too, but **et konto** is the older norm. Modern Bokmål dictionaries list **both en konto and et konto**. Default to **en konto** for consistency with sv. | |

Two-gender system (masculine + neuter only, no feminine) is **acceptable** in Bokmål UI. Many modern Norwegian UI uses two-gender for simplicity. Choose one approach and stay consistent within the translation.

**Nynorsk uses three genders strictly** — feminine is NOT optional in Nynorsk. `ei bok → boka` always (not `en bok → boken`).

### 4. Adjective agreement — indefinite + definite forms (severity 1.5)

| Subject | Form | Bokmål example | Nynorsk example |
|---------|------|----------------|-----------------|
| en-noun (masc.) indef. sg. | base | en **stor** fil | ei **stor** fil (fem.) / ein **stor** fil (masc.) |
| et-noun (neuter) indef. sg. | -t | et **stort** system | eit **stort** system |
| Plural (indef.) | -e | **store** filer | **store** filer (same) |
| Definite (sg./pl., either gender) | -e | den **store** filen / det **store** systemet | den **store** fila / det **store** systemet |

Irregular: `liten` (small) → `lite` (neuter) / `små` (plural). Same in both standards.
Irregular: `gammel` → `gammelt` / `gamle` (Bokmål); `gammal` → `gammalt` / `gamle` (Nynorsk).

### 5. Definite article — suffix vs free article (severity 1.5)

When a definite noun has a preceding adjective, Norwegian uses **double definiteness** (like Swedish, but slightly looser).

| ✗ Wrong | ✓ Correct (Bokmål) | ✓ Correct (Nynorsk) |
|---------|---------------------|---------------------|
| store filen | **den store filen** | **den store fila** |
| nye systemet | **det nye systemet** | **det nye systemet** |
| ny filer | **nye filer** | **nye filer** |

### 6. V2 word order (verb in position 2 of main clauses) (severity 2.0)

Same as Swedish/German/Danish.

| ✗ Wrong | ✓ Correct (Bokmål) | ✓ Correct (Nynorsk) |
|---------|---------------------|---------------------|
| I dag brukeren lagrer filen | **I dag lagrer brukeren filen** | **I dag lagrar brukaren fila** |
| Nå systemet laster data | **Nå laster systemet data** | **No lastar systemet data** |
| Etter innlogging du kan endre | **Etter innlogging kan du endre** | **Etter innlogging kan du endre** |

### 7. Subordinate clause word order — subject before verb (severity 1.5)

Like Swedish, subordinate clauses (introduced by `at`/`som`/`fordi`/`når`/`om`/`mens`) have **subject before verb**, and adverbs like `ikke`/`ikkje` go between them.

| Clause type | Pattern | Bokmål example |
|-------------|---------|----------------|
| Main (V2) | Subj + Verb + Adv + Obj | `Brukeren lagrer ikke filen.` |
| Subordinate | Subj + Adv + Verb + Obj | `…fordi brukeren ikke lagrer filen.` |

### 8. Negation placement (severity 1.5)

| Context | Pattern | Bokmål | Nynorsk |
|---------|---------|--------|---------|
| Main clause | Verb + ikke/ikkje | `Filen lagres ikke.` | `Fila vert ikkje lagra.` |
| Subordinate clause | ikke/ikkje + Verb | `…fordi filen ikke lagres.` | `…fordi fila ikkje vert lagra.` |

### 9. Compound words — write as ONE word (severity 1.5)

Same principle as Swedish, but generally less politically charged. Still required.

| ✗ Wrong (split) | ✓ Correct (joined) | English |
|-----------------|--------------------|---------|
| `data base` | **`database`** | database |
| `bruker grensesnitt` | **`brukergrensesnitt`** | user interface |
| `pass ord` | **`passord`** | password |
| `bok hylle` | **`bokhylle`** | bookshelf |
| `bilde kvalitet` | **`bildekvalitet`** | image quality |

**Hyphens** only for:
- Acronym + Norwegian word: `IT-firma`, `25-årig`.
- Compounds with foreign words/brands: `Google-konto`, `iPhone-en`.

Gender of compound = gender of the **LAST** element.

### 10. Comma rules — `og` / `eller` vs `men` / `for` (severity 1.0)

- **No comma** before coordinating `og` (and), `eller` (or).
- **Comma** before contrastive `men` (but), `for` (because).
- Comma before subordinating conjunctions.

### 11. Special characters `æ ø å` (Bokmål/Nynorsk) — NEVER strip (severity 3.0)

These are letters, not diacritics. Stripping or replacing them with `ae oe aa` is a critical failure.

`år` (year), `øy` (island), `æsj` (interjection) — replacing these makes the words unrecognizable to native readers.

### 12. ICU plurals — `one` + `other` (severity 1.5)

Norwegian has two CLDR plural categories.

```icu
{count, plural,
  one {# fil}
  other {# filer}
}
```

Nynorsk version:

```icu
{count, plural,
  one {# fil}
  other {# filer}
}
```

(Same forms here — `fil/filer` is consistent. For verbs and definite plurals, Bokmål/Nynorsk diverge: see delta table.)

---

## Pronouns

### Personal pronouns

| English | Bokmål | Nynorsk |
|---------|--------|---------|
| I | **jeg** | **eg** |
| you (sg.) | **du** | **du** |
| he | han | han |
| she | hun | ho |
| it (masc./fem.) | den | den / ho (fem.) |
| it (neuter) | det | det |
| gender-neutral 3rd person (rare) | hen (rising) | (less established in Nynorsk) |
| we | vi | vi |
| you (pl.) | dere | de |
| they | de / dem | dei |
| reflexive | seg | seg |

### Possessive (agrees with possessed noun)

| Person | masc. (en) | neut. (et) | plural |
|--------|------------|------------|--------|
| min (my) — Bokmål | min | mitt | mine |
| min (my) — Nynorsk | min | mitt | mine (same) |
| din (your sg.) — Bokmål | din | ditt | dine |
| din (your sg.) — Nynorsk | din | ditt | dine (same) |
| hans (his) | hans (invariable) | hans | hans |
| hennes (her) — Bokmål | hennes (invariable) | hennes | hennes |
| hennar (her) — Nynorsk | hennar | hennar | hennar |
| sin/sitt/sine (reflexive) | sin | sitt | sine |
| vår (our) | vår | vårt | våre |
| deres (their) — Bokmål | deres (invariable) | deres | deres |
| deira (their) — Nynorsk | deira (invariable) | deira | deira |

**Reflexive `sin/sitt/sine`**: used when the possessor is the subject of the same clause (same as Swedish, German, etc.).

---

## UI Conventions

### Buttons — imperative

| English | ✓ Bokmål | ✓ Nynorsk |
|---------|----------|-----------|
| Save | **Lagre** | **Lagre** |
| Cancel | **Avbryt** | **Avbryt** |
| Delete | **Slett** | **Slett** |
| Send | **Send** | **Send** |
| Edit | **Rediger** | **Rediger** |
| Search | **Søk** | **Søk** |
| Confirm | **Bekreft** | **Stadfest** |
| Continue | **Fortsett** | **Hald fram** |
| Submit | **Send inn** | **Send inn** |
| Sign in | **Logg inn** | **Logg inn** |
| Sign out | **Logg ut** | **Logg ut** |
| Sign up | **Opprett konto** / **Registrer deg** | **Opprett konto** / **Registrer deg** |
| Next | **Neste** | **Neste** |
| Back | **Tilbake** | **Tilbake** |
| Done | **Ferdig** | **Ferdig** |
| OK | **OK** | **OK** |
| Close | **Lukk** | **Lukk** |
| Upload | **Last opp** | **Last opp** |
| Download | **Last ned** | **Last ned** |
| Refresh | **Oppdater** | **Oppdater** |
| Settings | **Innstillinger** | **Innstillingar** |
| Apply | **Bruk** | **Bruk** |
| Reset | **Tilbakestill** | **Tilbakestill** |

### Status messages — present tense + ellipsis

| English | ✓ Bokmål | ✓ Nynorsk |
|---------|----------|-----------|
| Loading… | **Laster…** | **Lastar…** |
| Saving… | **Lagrer…** | **Lagrar…** |
| Sending… | **Sender…** | **Sender…** |
| Connecting… | **Kobler til…** | **Koplar til…** |
| Processing… | **Behandler…** | **Handsamar…** |
| Uploading… | **Laster opp…** | **Lastar opp…** |
| Searching… | **Søker…** | **Søkjer…** |
| Please wait | **Vennligst vent** | **Vent litt** |

### Completion messages — concise

| English | ✓ Bokmål | ✓ Nynorsk |
|---------|----------|-----------|
| Saved | **Lagret** | **Lagra** |
| Done | **Ferdig** | **Ferdig** |
| Translation complete | **Oversettelse fullført** | **Omsetjing fullført** |
| File uploaded | **Fil lastet opp** | **Fil lasta opp** |
| Sent | **Sendt** | **Sendt** |
| Payment successful | **Betaling fullført** | **Betaling fullført** |

### Empty states — concise, drop pronouns

| ✗ Verbose | ✓ Bokmål | ✓ Nynorsk |
|-----------|----------|-----------|
| Det ble ikke funnet noen resultater | **Ingen resultater** | **Ingen resultat** |
| Du har ingen prosjekter ennå | **Ingen prosjekter ennå** | **Ingen prosjekt enno** |

### Drag-and-drop

- drag → **dra**
- drop → **slipp** (NOT `slipp` ≠ `frigjør` which means "liberate")
- Combined: **`Dra og slipp filer her`**.

### Quantity expressions

| ✗ Calque | ✓ Bokmål | ✓ Nynorsk |
|----------|----------|-----------|
| 25+ språk | **mer enn 25 språk** | **meir enn 25 språk** |
| +{count} til | **og {count} til** | **og {count} til** |
| +25 nye funksjoner | **over 25 nye funksjoner** | **over 25 nye funksjonar** |

### Support expressions

| ✗ Calque | ✓ Bokmål | ✓ Nynorsk |
|----------|----------|-----------|
| Støtte for X-filer | **Støtter X-filer** / **X-filer støttes** | **Støttar X-filer** / **X-filer vert støtta** |
| Støtte for flere språk | **Støtter flere språk** | **Støttar fleire språk** |

### Error messages — what + next step

| ✗ Bare | ✓ Bokmål |
|--------|----------|
| Filen ble ikke funnet. | **Filen ble ikke funnet. Kontroller filbanen.** |
| Nettverksfeil. | **Nettverksfeil. Prøv igjen.** |
| Ugyldig e-post. | **Ugyldig e-postadresse. Sjekk formatet.** |
| Innlogging mislyktes. | **Innlogging mislyktes. Sjekk brukernavn og passord.** |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Norwegian | Notes |
|------|-----------|-------|
| Question | `?` | Same as English |
| Comma | `,` | Same as English; rules about conjunctions differ |
| Period | `.` | Same |
| Colon | `:` | Same |
| Quotation marks | **«…»** (outward-pointing guillemets) — preferred | Norwegian official typography; same as French but with no NBSP. Plain `"…"` also acceptable in UI. |
| Apostrophe | only in foreign names (`Joe's`) | Norwegian genitive: bare `-s` (`Annas bok`) |

**`«...»` are OUTWARD-pointing** in Norwegian (the angles point AWAY from the quoted text), unlike German's `»...«` (inward).

### Numbers

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **space** | 1 234 567 |
| Decimal separator | **comma** | 3,14 — `99,99 kr` |
| Negative | `-25` | |
| Percent | `25 %` (with space, preferred) or `25%` | |

### Dates

| Format | Example | Use |
|--------|---------|-----|
| DD.MM.YYYY | **15.01.2024** | Default for UI / business / casual |
| YYYY-MM-DD | 2024-01-15 | Technical / API / sortable contexts |
| D. månad YYYY | 15. januar 2024 | Long-form prose |

**Months (lowercase, no period) — same in Bokmål and Nynorsk:**

| 1 | januar | 7 | juli |
| 2 | februar | 8 | august |
| 3 | mars | 9 | september |
| 4 | april | 10 | oktober |
| 5 | mai | 11 | november |
| 6 | juni | 12 | desember |

**Weekdays (Bokmål / Nynorsk):**

| Eng | Bokmål | Nynorsk |
|-----|--------|---------|
| Monday | mandag | måndag |
| Tuesday | tirsdag | tysdag |
| Wednesday | onsdag | onsdag |
| Thursday | torsdag | torsdag |
| Friday | fredag | fredag |
| Saturday | lørdag | laurdag |
| Sunday | søndag | sundag |

**Week starts Monday.**

### Time

- 24-hour preferred: `14:30` or `kl. 14:30` (kl. = klokken / klokka).
- 12-hour rarely used.

### Currency — NOK

| Currency | Format |
|----------|--------|
| Norwegian krone | **99,99 kr** or **NOK 99,99** (kr after amount, with space) |

Never `kr 99,99` in modern Norwegian style. ISO-3-letter `NOK` before amount is acceptable in business/banking contexts.

---

## Terminology — preferred Norwegian terms (Bokmål default)

| English | ✓ Bokmål | ✓ Nynorsk | Avoid |
|---------|----------|-----------|-------|
| user | bruker | brukar | user |
| account | konto | konto | account |
| password | passord | passord | password |
| settings | innstillinger | innstillingar | — |
| dashboard | dashbord / kontrollpanel | kontrollpanel | — |
| email | e-post | e-post | mail |
| link | lenke | lenkje | link |
| browser | nettleser | nettlesar | browser |
| website | nettsted / nettside | nettstad / nettside | — |
| folder | mappe | mappe | folder |
| file | fil | fil | — |
| device | enhet | eining | device |
| phone | telefon / mobil | telefon / mobil | — |
| computer | datamaskin / PC | datamaskin / PC | komputer |
| app | app / applikasjon | app / applikasjon | — |
| update (v.) | oppdatere | oppdatere | updatee |
| save | lagre | lagre | — |
| delete | slette | slette | delete |
| upload | laste opp | laste opp | uploade |
| download | laste ned | laste ned | downloade |
| log in | logge inn | logge inn | sign in |
| sign up | opprette konto / registrere seg | opprette konto / registrere seg | — |
| search | søke | søkje | search |
| click | klikke | klikke | — |
| share | dele | dele | sharee |
| profile | profil | profil | — |
| notifications | varsler / notifikasjoner | varsel | — |
| privacy | personvern | personvern | privacy |
| terms | vilkår | vilkår | terms |
| help | hjelp | hjelp | — |
| feedback | tilbakemelding | tilbakemelding | feedback (also acceptable in dev contexts) |
| menu | meny | meny | — |
| home | hjem / startside | heim / startside | — |
| build (software) | bygge / utvikle | byggje / utvikle | builde |
| deploy | driftsette / rulle ut / publisere | driftsetje / rulle ut | deployere |
| commit (git) | commit (keep) / lagre | commit (keep) | — |
| merge | slå sammen | slå saman | mergee |
| repository | repository / arkiv | repository / arkiv | — |
| branch (git) | branch (keep) / gren | branch (keep) / grein | — |
| pipeline | pipeline / prosesskjede | pipeline | — |
| API | API (keep) | API (keep) | — |
| sync | synkronisere | synkronisere | — |
| webhook | webhook (keep) | webhook (keep) | — |
| support (feature) | støtte / **støtter** (verb) | støtte / **støttar** (verb) | supportere |

### Tech identifiers — keep in Latin/English

These MUST stay in Latin/English inside Norwegian text:
- Programming languages, frameworks, tools (Git, GitHub, Docker, npm, pip).
- Protocols (HTTP, REST, GraphQL).
- File formats (JSON, XML, CSV, PDF).
- Commands, paths, URLs, code.

---

## False Friends — Critical

| Norwegian | Actually means | NOT this | Correct for the English |
|-----------|----------------|----------|--------------------------|
| aktuell | current / relevant | "actual" | "actual" → **faktisk / egentlig** |
| eventuelt | possibly / perhaps | "eventually" | "eventually" → **til slutt / etter hvert** |
| engasjert | committed / involved / engaged-in-cause | "engaged" (to be married) | "engaged to marry" → **forlovet** |
| sensitiv | sensitive | "sensible" | "sensible" → **fornuftig / vettig** |
| kontrollere | to check / verify | "to control" | "control (v.)" → **styre / kontrollere** (note: kontrollere does cover some "control" senses, but check-sense is primary) |
| seriøs | reliable / trustworthy | "serious" (as in grave) | "serious (grave)" → **alvorlig** |
| gift | married OR poison | "gift" (present) | "gift" → **gave / present** |
| barn | child(ren) | "barn" (building) | "barn" → **låve** |
| smell | a bang / loud noise | "smell" (odor) | "smell" → **lukt** |

---

## Calque / Anti-Pattern List

| ✗ Calque | ✓ Bokmål |
|----------|----------|
| Ta plass (for events) | **Finne sted** / **Skje** |
| På slutten av dagen | **Til syvende og sist** / **I bunn og grunn** |
| Ikke egentlig | **Egentlig ikke** / **Ikke akkurat** |
| Gjøre en forbedring | **Forbedre** |
| Gi et svar | **Svare** |
| På en daglig basis | **Daglig** / **Hver dag** |
| I termer av | **Når det gjelder** / **Med tanke på** |
| Få oversettelsen din klar på minutter | **Oversettelse på noen få minutter** |
| Hold prosjektene dine synkroniserte | **Sørg for synkronisering av prosjektene** |
| Gjør arbeidsflyten din raskere | **Effektiviser arbeidsflyten din** |
| Null nedetid / Zero downtime | **Uten nedetid** / **Ingen nedetid** |
| Null forpliktelser | **Uten forpliktelser** / **Helt fritt** |
| AI-drevet | **AI-basert** / **drevet av AI** / **med AI** |
| AI-bevisst | **AI-tilpasset** / **støtter AI** / **med AI-støtte** |
| brukervennlig | **lett å bruke** / **intuitiv** (calque OK in some marketing; avoid in technical UI) |
| De forente stater | **USA** |
| Det forente kongerike | **Storbritannia** / **UK** |
| 5 år siden (when source means "2019 me") | **mitt 2019-jeg** / **den jeg var i 2019** |

---

## Custom Sections

### Time / duration — `igjen` and unit abbreviations

| English | ✓ Bokmål | ✓ Nynorsk |
|---------|----------|-----------|
| 30 seconds remaining | **30 s igjen** | **30 s att** |
| 5 minutes remaining | **5 min igjen** (NOT `5 m`) | **5 min att** |
| 2 hours remaining | **2 t igjen** (NOT `2 h`) | **2 t att** |
| 3 days remaining | **3 d igjen** | **3 d att** |

Always a **space** between number and unit. `min` not `m`. `t` not `h` for hours.

### Per vs for — CRITICAL semantic distinction

| Source | ✓ Bokmål | Meaning |
|--------|----------|---------|
| per language (rate) | **per språk** | rate, per-unit |
| for 25 languages (total) | **for 25 språk** | total scope |
| 5 USD per language | **5 USD per språk** | rate |
| 5 USD for all languages | **5 USD for alle språk** | total |

### Cost / estimate ordering

Amount first:

| ✗ Ambiguous | ✓ Clear |
|-------------|---------|
| 5 språk 25 kreditter | **25 kreditter for 5 språk** |

### Janteloven cultural tone

Norwegian culture values **Janteloven** (the Law of Jante — anti-bragging, humility). UI copy should be:
- Modest, not boastful or flashy.
- Direct, practical, solution-oriented.
- No superlatives or hype ("Best ever!" → just `Forbedret`).
- Outdoor / nature metaphors are well-received (`friluftsliv`, hiking, skiing).

This makes Norwegian marketing copy **substantially more understated** than English marketing copy. Soften American-style hype.

### UI element references in prose

| ✗ Compound | ✓ Quoted label |
|------------|----------------|
| Klikk Lagre-knappen | **Klikk på knappen "Lagre"** |
| Åpne Innstillinger-fanen | **Åpne fanen "Innstillinger"** |
| Bruk Navn-feltet | **Bruk feltet "Navn"** |

### Brand names + Norwegian suffixes — use hyphen

Foreign brand names take Norwegian definite/possessive endings via hyphen:

- `OneSky` → `OneSky-en` (masc. definite) / `OneSky-et` (neut. definite) / `OneSky-s` (possessive).
- `Google-konto`, `iPhone-en`, `GitHub-en`.

### Feminine optional in Bokmål — pick a strategy and stay consistent

Bokmål allows both `ei bok → boka` (feminine) and `en bok → boken` (treated as masculine). For UI:

- **Two-gender approach** (en/et only): simpler, broader appeal, slightly more "conservative Bokmål" feel. `en bok → boken`.
- **Three-gender approach** (en/ei/et): more colloquial, more Eastern-Norwegian dialect-aligned. `ei bok → boka`.

**Choose ONE per translation set and stay consistent.** Most modern Norwegian UI uses **two-gender** for simplicity.

**Nynorsk does NOT have this option** — feminine is always feminine.

---

## Self-Check Checklist (Run Before Returning Output)

### Bokmål vs Nynorsk integrity (auto-fail on miss)

- [ ] **Consistent variant** — no mixing of jeg/eg, ikke/ikkje, hva/kva, hvordan/korleis.
- [ ] If Nynorsk: verb endings -ar where applicable (`lagrar`, `brukar`), `frå` not `fra`, `kvar` not `hvor`, `dei` not `de` for plural they.
- [ ] If Bokmål: classic Bokmål forms throughout.

### Accuracy

- [ ] **Hybrid-compound verbs rejected** — no `avlinke`, `avsynce`, `downloade`, `cancele`, `delete` (as Norwegian verb).
- [ ] **Gender (en/ei/et)** correct on every article and definite suffix. Two-gender or three-gender approach consistent.
- [ ] **Adjective agreement**: -t for et-noun indef. sg., -e for plural/definite.
- [ ] **Definite suffix** present (filen, systemet, fila in Nynorsk).
- [ ] **Double definiteness** when noun has adjective (den store filen).
- [ ] **V2 word order** in every main clause.
- [ ] **Subordinate clause word order**: subject before verb, ikke/ikkje between.
- [ ] **Negation placement**: after verb (main), before verb (subordinate).
- [ ] **Compound words written as one word** (no `data base`, `bruker grensesnitt`).
- [ ] **Comma**: no comma before `og`/`eller`; comma before `men`/`for`.
- [ ] **Special chars `æ ø å`** preserved — never `ae oe aa`.
- [ ] **ICU plurals**: one and other categories present.
- [ ] **Placeholders** {var}, {{var}}, <tag>, URLs preserved.
- [ ] **Latin tech identifiers**: Git, API, JSON, etc. stay in Latin.
- [ ] **Numbers**: comma decimal, space thousands, `kr` after amount.
- [ ] **Dates**: DD.MM.YYYY default; ISO 8601 for technical contexts.
- [ ] **Time**: 24-hour, `kl. 14:30`.
- [ ] **per vs for**: rate vs total — never mixed.

### Register

- [ ] **du throughout** — never `De/Deres` in modern Norwegian UI.
- [ ] **No literary register elevation** when source is casual (no `forbli`, `utallige`, `leveres` for casual `stay`, `countless`, `ship`).

### UI conventions

- [ ] Buttons imperative (`Lagre`, `Avbryt`, `Slett`).
- [ ] Status uses present + ellipsis (`Laster…`, `Lagrer…`).
- [ ] Completion concise (`Lagret`, `Oversettelse fullført`).
- [ ] Empty states concise (`Ingen resultater`, NOT `Det ble ikke funnet noen resultater`).
- [ ] Drag-drop uses `dra` and `slipp`.
- [ ] `Støtter X` not `Støtte for X`.
- [ ] Quantity: `mer enn 25` not `25+`; `og {count} til` not `+{count}`.
- [ ] Error messages include next step.

### Naturalness

- [ ] No English calques (`ta plass`, `på slutten av dagen`, `gjøre en forbedring`, `på en daglig basis`).
- [ ] No marketing-zero calque (`Null X` → `Uten X` / `Ingen X`).
- [ ] No anglicism-verb formations (`supportere`, `deployere`, `downloade`).
- [ ] False-friend check: `aktuell ≠ actual`, `eventuelt ≠ eventually`, `engasjert ≠ engaged-to-marry`.
- [ ] `igjen` (Bokmål) / `att` (Nynorsk) for time-remaining; `min` not `m`; space before unit.
- [ ] Proper nouns short forms (`USA`, `Storbritannia`).
- [ ] Janteloven tone — no hype, modest.
- [ ] Quotation marks «...» (outward) when typography matters.

### Quotation marks

- [ ] Use `«...»` outward-pointing guillemets in editorial/marketing copy.
- [ ] Plain `"..."` acceptable in UI/technical contexts.

---

## Worked Example — Standard Bokmål UI

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** neutral product UI → casual du, present-tense status.

**Translation (Bokmål):**

> Velkommen tilbake! Du har 3 nye filer i kontoen din. Klikk på **Fortsett** for å gjennomgå dem eller **Avbryt** for å bli her. Lagrer endringene dine…

**Notes:**
- `Velkommen tilbake` — standard greeting.
- `Du har` — du throughout.
- `3 nye filer` — plural adj `nye`, plural noun `filer`. Indefinite, so no double-def.
- `i kontoen din` — possessive `din` (en-noun) attached. Alternative: `i din konto` (more formal).
- Buttons imperative: `Fortsett`, `Avbryt`.
- Status: `Lagrer endringene dine…` (present + ellipsis).
- `endringene` — definite plural ("the changes").
- `dine` — possessive plural agreement.

---

## Worked Example — Same string in Nynorsk

**Translation (Nynorsk):**

> Velkomen tilbake! Du har 3 nye filer i kontoen din. Klikk på **Hald fram** for å gå gjennom dei eller **Avbryt** for å bli her. Lagrar endringane dine…

**Notes — what changed from Bokmål:**
- `Velkommen` → **`Velkomen`** (one m).
- `Fortsett` → **`Hald fram`** (continue).
- `gjennomgå dem` → **`gå gjennom dei`** (`dei` is Nynorsk for "them").
- `Lagrer` → **`Lagrar`** (a-class verb ending).
- `endringene` → **`endringane`** (Nynorsk definite plural).

Every short word checked. No `jeg` / `ikke` / `hva` would survive a Nynorsk pass — but this particular sentence happens not to use them.

---

## Worked Example — Sentence with full vocabulary delta

**Source:** I don't know what to do when I can't sign in.

**Bokmål:** **Jeg vet ikke hva jeg skal gjøre når jeg ikke kan logge inn.**

**Nynorsk:** **Eg veit ikkje kva eg skal gjere når eg ikkje kan logge inn.**

Every italicized word is different:
- jeg / eg
- vet / veit
- ikke / ikkje
- hva / kva
- gjøre / gjere
- (logge stays the same — borrowed verb)
- ikke / ikkje (second occurrence)

---

## Worked Example — Compound word + V2

**Source:** Today, the system saves your file automatically every five minutes.

**Bokmål:** I dag **lagrer systemet** filen din **automatisk** hvert femte minutt.

**Nynorsk:** I dag **lagrar systemet** fila di **automatisk** kvart femte minutt.

Notes:
- `I dag` fronted → V2 → `lagrer/lagrar` in position 2.
- `systemet` — neuter definite suffix.
- `filen din` / `fila di` — Bokmål masc.-treatment vs Nynorsk fem.-treatment.
- `hvert femte minutt` / `kvart femte minutt` — idiom for "every five minutes".

---

## When in Doubt

1. **Default to Bokmål, du-form, two-gender (en/et).**
2. If unsure about variant → ask once; default Bokmål.
3. If you typed `eg` `ikkje` `kva` and the rest is Bokmål → **regress all to one variant**.
4. If a word looks like an English root with av-/fra-/opp- prefixed → **stop and find the native verb** (`koble fra`, `slette`, `synkronisere`).
5. If you typed two nouns with a space (e.g., `data base`) and they describe one concept → **join them**.
6. If you used `De/Deres` for formal singular → **switch to `du`**. Always.
7. If your translation feels boastful or hyped → **Janteloven**: tone it down.
