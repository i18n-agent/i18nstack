---
name: localize-fi
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Finnish (Suomi) for Finland. Finnish is a Finno-Ugric (Uralic) language, NOT Indo-European and NOT Scandinavian. Sister language to Estonian (Finnish 15 cases vs Estonian 14; both have consonant gradation but differ). Enforces the 15-case system with the defining PARTITIVE case (-a/-ä/-ta/-tä for partial objects, counted nouns 2+, negative direct objects), STRICT vowel harmony (front ä/ö/y vs back a/o/u — never mix in a word), consonant gradation (kk→k, pp→p, tt→t, t→d, p→v, k→Ø/v), NO grammatical gender (hän = he/she), agglutinative possessive suffixes (taloni \"my house\"), partitive-singular with numbers 2+ (viisi kissaa NOT viisi kissat — UNIQUE to Finnish/Estonian), ICU plural `other` = partitive singular, sinä (informal — default for Finnish UI) vs Te (formal) consistency, impersonal passive for status (Tallennetaan...), kirjakieli (written form, not puhekieli mä/sä/oon), connecting vowel \"i\" for consonant-final brand names (Agent:ia, React:issa), reverse guillemets »...«, DD.MM.YYYY dates, EUR currency (1 234,56 €), 24-hour time with period (14.30), and Finnish-specific identity (not Swedish, not Russian, not Hungarian)."
---

# Localize: Finnish (fi → Suomi)

Distilled from the production translation prompt at `service-mcp/src/prompts/language-rules/fi.ts`. Follow these rules verbatim — they are model-agnostic and produce consistent native-quality Finnish output.

## Mindset

> Olet äärimmäisen vaativa suomenkielinen kirjoittaja, joka vihaa luonnottomia suomenkielisiä ilmauksia, kuten englannista suoria käännöksiä tai kömpelöitä muotoiluja. Sinun on nyt muokattava tätä tekstiä, kunnes se saavuttaa täysin tyydyttävän sujuvuuden ja luonnollisuuden tason säilyttäen alkuperäisen merkityksen.

Translation: You are an extremely demanding Finnish writer who hates unnatural Finnish expressions — direct translations from English, clumsy phrasings. Your job is to refine the text until it reaches complete fluency and naturalness while preserving the original meaning. Casual use of common English words is fine when it sounds natural.

Reject literal English calques and verbed anglicisms (`klikata`, `deletoida`, `dauntloudaata`, `seivaata`, `aploudaata`). Finnish is a digital society — modern tech terminology is welcome where well-established (`sähköposti` for email, `selain` for browser), but native compound nouns and verbs are preferred over English borrowings.

---

## Scope & Variants

This skill targets **fi-FI** — Standard Finnish for Finland.

- **Written standard (kirjakieli)** is universal across Finland and is the **only** form used in UI, marketing, and documentation.
- **Spoken Finnish (puhekieli)** has heavy contractions (mä, sä, oon, kaa, niinku) and regional variation. **NEVER use puhekieli in product text** — it reads as unprofessional or chat-app casual.
- Finland is officially **bilingual** (Finnish ~87% / Swedish ~5%). UI for Finnish audiences is Finnish only. Swedish-speaking Finns (Finlandssvenskar) use the `sv-FI` locale, which is handled by the separate `localize-sv` skill — do NOT route Swedish-Finnish content here.

There are no regional variants of Finnish to disambiguate. One standard form fits all of Finland.

---

## Identity Guardrail — Finnish Is NOT Swedish, NOT Russian, NOT Hungarian

Finnish belongs to the **Finno-Ugric (Uralic)** language family, NOT Indo-European. This single fact reshapes everything:

| Misconception | Reality |
|---------------|---------|
| "Finnish is Scandinavian" | **FALSE.** Finnish is Uralic. Swedish, Norwegian, Danish, Icelandic are Germanic (Indo-European). Finland's geographic proximity to Sweden does NOT make Finnish a Scandinavian language. |
| "Finnish is similar to Russian" | **FALSE.** Russian is East Slavic (Indo-European). Russian and Finnish share no genetic relationship despite the long shared border. |
| "Finnish is like Hungarian" | **PARTIALLY TRUE but distant.** Hungarian is also Uralic, but in the Ugric branch. Finnish and Hungarian diverged ~6000 years ago — they share grammatical structure (agglutination, case system, no gender) but are NOT mutually intelligible. About as close as English is to Persian. |
| "Finnish is similar to Estonian" | **TRUE — sister language.** Finnish and Estonian are in the Finnic branch of Uralic. They share ~50% mutually intelligible cognates and very similar grammar. |

### Finnish vs Estonian (sister-language disambiguation)

These two languages are the closest pair in the family. Get them straight:

| Feature | Finnish | Estonian |
|---------|---------|----------|
| Cases | **15** | **14** (no instructive) |
| Consonant gradation | Yes (kk→k, pp→p, tt→t, t→d, p→v, k→Ø/v) | Yes, but different patterns (kk→k, k→g, etc.) |
| Vowel harmony | **YES, strict** (front ä/ö/y vs back a/o/u) | **NO** — Estonian lost vowel harmony |
| Long vowels/consonants | Distinct (tuli/tuuli/tulli are 3 different words) | Three-grade quantity system (different from Finnish) |
| Word "file" | **tiedosto** | **fail** |
| Word "save" | **tallenna** | **salvesta** |
| Word "user" | **käyttäjä** | **kasutaja** |
| Word "settings" | **asetukset** | **seaded** |
| Word "yes" | **kyllä / joo** | **jah** |
| Letter ä | Used heavily | Used heavily |
| Letter ö | Used | Used |
| Letter õ | NOT in Finnish | Used heavily — diagnostic for Estonian |
| Letter ü | NOT in Finnish (only in foreign names) | Used |

**Diagnostic letters**: If you see **õ** (o-tilde) in source text claiming to be Finnish, it's actually Estonian. Finnish never uses õ. Conversely, the Finnish letter combinations like **-ssa/-ssä**, **-ksi**, doubled vowels (**uu, ii, aa, oo**) are typical Finnish markers absent in Estonian.

### Finnish vs Swedish (Finland's other official language)

Finland is bilingual but the languages are unrelated:

- "Hello" — Finnish `Hei` / Swedish `Hej`
- "Thank you" — Finnish `Kiitos` / Swedish `Tack`
- "File" — Finnish `tiedosto` / Swedish `fil`
- "Save" — Finnish `Tallenna` / Swedish `Spara`

If a customer is in Finland but their content uses Swedish vocabulary (fil, spara, hej, tack), they want `sv-FI`, NOT this skill. Route to `localize-sv`.

### Cultural identity notes

- Finland is a **Nordic country** (one of five: Finland, Sweden, Norway, Denmark, Iceland). "Nordic" is a regional/political identifier, not a linguistic one.
- "Scandinavian" strictly means Sweden + Norway + Denmark + sometimes Iceland. Finland is Nordic but NOT Scandinavian in the strict linguistic sense.
- Finns are sensitive to being miscategorized as Russian or Swedish. Identity matters.
- Finland has been independent since 1917. Soviet/Russian influence is a historical fact (Karelia, Winter War) but Finland is **not** a former Soviet state.

---

## Register (Sinä informal — default / Te formal)

Finnish has two address forms. Unlike German/French/Spanish where formal is the safe default, **Finnish UI defaults to INFORMAL (sinä)** — Finnish culture is famously informal in business and tech.

| Form | Pronoun | Possessive suffix | Verb (2sg) | Imperative |
|------|---------|--------------------|------------|------------|
| Informal (sinä) | sinä / sä (puhekieli only) | -si | tallennat | **Tallenna** |
| Formal (Te) | Te / te | -nne | tallennatte | **Tallentakaa** |
| Impersonal passive | — | — | tallennetaan | (rarely imperative) |

### Register Auto-Detection — DEFAULTS DIFFER FROM MOST LANGUAGES

If the user hasn't specified, infer from source register. **Finnish calibration is UNIQUE: even moderately formal source defaults to sinä in modern software UI.** Te reads as old-fashioned, bureaucratic, or condescending in most consumer/B2B contexts.

#### Formal source signals → output Te / teitä / Teidän

- Hedging / polite modals: "please", "kindly", "we recommend", "we kindly request"
- Domain vocabulary: legal, financial, healthcare, regulatory, government, banking, insurance, formal contracts
- Third-person / distance: "the user must", "customers should"
- Long sentences, formal connectors, no contractions
- Brand voice: bank, government, legal tech, insurance, formal correspondence
- Older target demographic (retirement/health products)
- No exclamations or emojis

#### Informal source signals → output sinä / sinun / sinua (Finnish default)

- ANY of: contractions in source, casual greetings, emoji, exclamations, slang
- Lifestyle, gaming, social, e-commerce, productivity apps — all default to sinä
- Marketing copy, newsletters, mobile UI — sinä is the modern norm
- B2B SaaS — almost always sinä in Finnish (different from German/French B2B)

#### Mixed / ambiguous → default to SINÄ

This is OPPOSITE of most other languages. In Finnish:
- Modern software UI: sinä almost always.
- Te reads stiff and signals "outdated / government / elderly target".
- Only escalate to Te if source is explicitly legal/banking/government, OR user requests it.

#### Explicit user override

If the user says "use Te" / "use formal" / "make it casual", their instruction wins.

#### Worked examples

| Source | Detected | Finnish output |
|--------|----------|----------------|
| "Please review the terms of service before proceeding." | formal | Tutustukaa käyttöehtoihin ennen jatkamista. |
| "Hey! Tap here to get started — it's super quick 🚀" | informal | Hei! Napauta tästä ja aloita — sujuu nopeasti 🚀 |
| "Submit your application by the deadline." | formal | Lähettäkää hakemuksenne ennen määräaikaa. |
| "Don't forget to save your work!" | informal | Älä unohda tallentaa työtäsi! |
| "Update your profile information." | informal (B2B SaaS) | Päivitä profiilitietosi. |

After detection: keep the chosen form consistent. **NEVER mix sinä/Te** across pronouns, possessives, OR imperatives. The most common error is a verb in one form + possessive suffix in the other:

- ❌ `Voitte muuttaa asetuksiasi.` (Te verb + sinä possessive)
- ✅ `Voitte muuttaa asetuksianne.` (Te throughout)
- ✅ `Voit muuttaa asetuksiasi.` (sinä throughout)

---

## ⚠️ Critical Hard Rules — Finnish Has Several Highly Distinctive Patterns

These rules have no analogue in English/Romance/Germanic languages, so models get them wrong by default.

### A. Numbers 2+ take PARTITIVE SINGULAR (severity 2.0 — CRITICAL)

This is shared only with Estonian. Every other major European language uses plural after numbers.

| Wrong (English-style plural) | Correct (partitive singular) |
|------------------------------|------------------------------|
| viisi tiedostot | **viisi tiedostoa** |
| viisi tiedostoja (partitive PLURAL) | **viisi tiedostoa** (partitive SINGULAR) |
| kolme käyttäjät | **kolme käyttäjää** |
| kaksikymmentä tiedostot | **kaksikymmentä tiedostoa** |
| sata krediittit | **sata krediittiä** |
| nolla tiedostot | **nolla tiedostoa** |

Rule: only `1` (yksi) takes nominative singular (`yksi tiedosto`). Every other number — **including 0 and any number ≥2** — takes **partitive singular**. This applies recursively in ICU plurals (see B).

Common pitfall: Translators reach for partitive plural (`tiedostoja`) by analogy with English/Spanish/German. WRONG. The correct form is partitive **singular** (`tiedostoa`).

### B. ICU plural `other` = partitive singular (CRITICAL, severity 2.0)

Because Finnish only distinguishes 1 vs everything-else (via partitive singular), ICU has only two categories: `one` and `other`. The `other` branch must be partitive SINGULAR.

```icu
{count, plural, one {# tiedosto} other {# tiedostoa}}
{count, plural, one {# käyttäjä} other {# käyttäjää}}
{count, plural, one {# kieli} other {# kieltä}}
{count, plural, one {# krediitti} other {# krediittiä}}
```

| Wrong | Correct |
|-------|---------|
| `other {# tiedostot}` | **`other {# tiedostoa}`** (partitive singular, not nominative plural) |
| `other {# tiedostoja}` | **`other {# tiedostoa}`** (partitive SINGULAR, not partitive plural) |
| `other {# krediittejä}` | **`other {# krediittiä}`** |

### C. STRICT vowel harmony (severity 1.5)

Finnish vowels split into three classes that interact rigidly within a single word stem:

| Class | Vowels |
|-------|--------|
| Front | ä, ö, y |
| Back | a, o, u |
| Neutral | e, i |

**Rule**: Within a single word stem, front and back vowels NEVER mix. Suffixes have front/back variants and must match the stem:

| Stem | Suffix (inessive "in") | Result |
|------|-----------------------|--------|
| talo (back vowels) | -ssa | **talossa** "in the house" |
| metsä (front vowels) | -ssä | **metsässä** "in the forest" |
| työ (front vowels) | -ssä | **työssä** "at work" |
| pöytä (front vowels) | -ssä | **pöydässä** "on the table" (with gradation) |

Suffix pairs with front/back variants:

| Back | Front | Meaning |
|------|-------|---------|
| -ssa | -ssä | inessive (in) |
| -sta | -stä | elative (out of) |
| -lla | -llä | adessive (at/on) |
| -lta | -ltä | ablative (from) |
| -a | -ä | partitive |
| -na | -nä | essive |
| -tta | -ttä | abessive |

Neutral vowels (e, i) don't determine harmony — they can coexist with either class. But if a word has ONLY neutral vowels (`televisio`, `tie`, `kieli`), it takes **front** suffixes by default (`televisiossa`, `tiellä`, `kielessä`).

| Wrong | Correct | Reason |
|-------|---------|--------|
| järjestelmassa | **järjestelmässä** | front-vowel stem → front suffix |
| kansiössä | **kansiossa** | back-vowel stem → back suffix |
| työssä (correct) | työssä | front vowels ö, e → front suffix |
| autolla (correct) | autolla | back vowels a, o → back suffix |

Compound words: each part of a compound keeps its own harmony. `työ-paikka` is fine because each component is internally harmonic, but suffixes attach to the LAST component: `työpaikalla` (adessive based on `-paikka` back vowels — wait, both have neutral; but `paikka` is back-vowel-dominant → `-lla`).

### D. Partitive case — the defining Finnish feature (severity 2.5)

Partitive (-a/-ä/-ta/-tä/-ja/-jä) is used for:

1. **Partial / indefinite quantities**: `kahvia` "some coffee", `vettä` "some water"
2. **Counted nouns ≥2** (see rule A): `viisi tiedostoa` "five files"
3. **Negative direct objects**: `En näe taloa` "I don't see a/the house" (NOT `taloa` → `talon`)
4. **Incomplete / ongoing actions**: `Luen kirjaa` "I'm reading a book (ongoing)" vs `Luin kirjan` "I read the book (completed)"
5. **Object of certain verbs** (verb-governed — see rule F below): `auttaa käyttäjää`, `etsiä tiedostoa`, `rakastaa sinua`
6. **After certain numerals and quantifiers**: `paljon ihmisiä` "many people", `vähän aikaa` "little time"
7. **In existential sentences with mass/indef quantity**: `Maitoa on jääkaapissa` "There's milk in the fridge"

Partitive vs accusative (genitive) for direct object — the **completeness** distinction:

| Sentence | Object case | Meaning |
|----------|-------------|---------|
| Söin omenan. | accusative (= genitive form) | I ate the/an apple (completely). |
| Söin omenaa. | partitive | I was eating the/an apple (ongoing/partial). |
| Luin kirjan. | accusative | I read the book (finished). |
| Luin kirjaa. | partitive | I was reading the book (ongoing). |

This is one of the hardest features for non-Finns — aspect/completeness is grammaticalized.

### E. Consonant gradation (astevaihtelu) (severity 1.5)

When adding case suffixes, certain root consonants alternate between **strong** and **weak** grade. This happens in many but not all case forms.

#### Quantitative gradation (doubled → single):

| Strong | Weak | Example |
|--------|------|---------|
| **kk** | **k** | sukka → sukan (sock), tukki → tukin |
| **pp** | **p** | kuppi → kupin (cup), kauppa → kaupan |
| **tt** | **t** | matto → maton (carpet), katti → katin |

#### Qualitative gradation (single → other or zero):

| Strong | Weak | Example |
|--------|------|---------|
| **k** | **Ø** or **v** | jalka → jalan (foot), aika → ajan, luku → luvun |
| **t** | **d** | katu → kadun (street), pata → padan |
| **p** | **v** | apu → avun (help), tapa → tavan |
| **mp** | **mm** | lampi → lammen (pond) |
| **nt** | **nn** | kanta → kannan (heel) |
| **lt** | **ll** | kulta → kullan (gold) |
| **rt** | **rr** | kerta → kerran (time/instance) |
| **nk** | **ng** | Helsinki → Helsingin (note: spelled ng in weak grade) |

Gradation triggers: closed-syllable cases (genitive -n, inessive -ssa, etc.) typically use the **weak** grade. Open-syllable cases (illative, partitive, essive) often keep the **strong** grade. Plurals and certain endings reverse this.

**Worked example with `tiedosto` (file):**

| Case | Form | Note |
|------|------|------|
| Nominative | tiedosto | no gradation (no consonant cluster to gradate) |
| Genitive | tiedoston | (no gradation here, only suffixation) |
| Partitive | tiedostoa | strong stem |
| Inessive | tiedostossa | |
| Illative | tiedostoon | |

**Worked example with `kauppa` (shop) — has gradation:**

| Case | Form | Grade |
|------|------|-------|
| Nominative | **kauppa** | strong (pp) |
| Genitive | **kaupan** | weak (p) |
| Partitive | **kauppaa** | strong (pp) |
| Inessive | **kaupassa** | weak (p) |
| Illative | **kauppaan** | strong (pp) |

### F. Verb-governed case (severity 2.0)

Each Finnish verb dictates which case its object/complement takes. There's no general rule — these must be memorized.

| Verb | Governs | Example | Wrong (alt case) |
|------|---------|---------|------------------|
| auttaa (help) | **partitive** | auttaa käyttäjää | auttaa käyttäjälle / auttaa käyttäjän |
| pitää (like) | **elative** | pidän musiikista | pidän musiikkia (= "I'm holding music") |
| pitää (must) | **infinitive** | minun pitää tehdä | — |
| luottaa (trust) | **illative** | luottaa järjestelmään | luottaa järjestelmässä |
| etsiä (search for) | **partitive** | etsiä tiedostoa | etsiä tiedoston |
| tarvita (need) | **partitive** | tarvitsen apua | tarvitsen apu |
| odottaa (wait for) | **partitive** | odotamme vastaustanne | odotamme vastaustanne (acc) |
| rakastaa (love) | **partitive** | rakastaa sinua | rakastaa sinun |
| vihata (hate) | **partitive** | vihata epäonnistumista | vihata epäonnistuminen |
| käyttää (use) | **partitive** (often) | käyttää järjestelmää | käyttää järjestelmän (= "use up the system") |
| muistaa (remember) | **partitive** | muistaa nimeä (ongoing) / muistaa nimen (completed) | — |
| ymmärtää (understand) | **partitive** | ymmärrän sinua | — |
| ajatella (think of) | **partitive** | ajattelen sinua | — |
| kaivata (long for) | **partitive** | kaipaan kotia | — |
| pyytää (ask for) | **partitive** | pyytää apua | — |

If the source uses an English verb that maps to one of these, double-check the case.

### G. NO grammatical gender — `hän` covers he/she (UNIQUE)

Finnish has NO grammatical gender. The pronoun `hän` means **he, she, and (in formal use) it**. Animals and inanimate objects use `se`.

This is a major translation **advantage** when source is gender-ambiguous: "When a user logs in, they see..." → `Kun käyttäjä kirjautuu sisään, hän näkee...` (no gendered pronoun choice needed).

| Pronoun | Meaning |
|---------|---------|
| hän | he / she |
| se | it (animals, things; colloquially also he/she) |
| he | they (people) |
| ne | they (things, animals) |

UI implication: gender-neutral by default. "User profile" → `Käyttäjän profiili`. "Their preferences" → `Hänen asetuksensa` or `Käyttäjän asetukset`.

Don't invent gendered forms — Finnish has none. Adjectives don't agree in gender either, only in case and number.

### H. Possessive suffixes — agglutinated, not separate words

Finnish marks possession with **suffixes that attach to the noun**, not separate possessive pronouns. These suffixes attach AFTER case suffixes.

| Person | Suffix | Example (talo "house") |
|--------|--------|------------------------|
| 1sg | -ni | talo**ni** "my house" |
| 2sg | -si | talo**si** "your house" (sinä) |
| 3sg | -nsa / -nsä | talo**nsa** "his/her house" |
| 1pl | -mme | talo**mme** "our house" |
| 2pl / formal | -nne | talo**nne** "your house" (Te or plural) |
| 3pl | -nsa / -nsä | talo**nsa** "their house" |

With case suffixes — order: stem + case + possessive:

| Form | Breakdown | Meaning |
|------|-----------|---------|
| talossani | talo + ssa (ines) + ni (1sg) | "in my house" |
| autollasi | auto + lla (ades) + si (2sg) | "on/with your car" |
| asetuksissamme | asetuksissa + mme | "in our settings" |
| tiedostostanne | tiedosto + sta (elat) + nne | "from your file" (formal) |

Common UI patterns:

| English | Finnish (sinä) | Finnish (Te) |
|---------|----------------|--------------|
| Your file | Tiedostosi | Tiedostonne |
| Your account | Tilisi | Tilinne |
| Your settings | Asetuksesi | Asetuksenne |
| Your work | Työsi | Työnne |
| Your profile | Profiilisi | Profiilinne |

Standalone possessive pronouns (sinun, hänen, meidän) exist but are often used WITH the suffix for emphasis: `sinun tiedostosi` "your file (yours)". In neutral UI text, just the suffix is enough: `tiedostosi`.

### I. Long vowels and consonants — meaning-critical (severity 2.5)

Finnish distinguishes **short** vs **long** vowels/consonants by doubling letters. This is NOT optional — it changes meaning:

| Short | Long | Difference |
|-------|------|------------|
| tuli (fire) | tuuli (wind) — also tulli (customs) | 3 different words |
| tapa (way/habit) | tappaa (to kill) | |
| muta (mud) | mutta (but) | |
| kuka (who) | kukka (flower) | |
| pala (piece) | palaa (returns / burns) | |
| sinä (you) | sinää (no such word) | |
| valita (to choose) | välittää (to care) | also vowel-harmony difference |

**Translation implication**: do NOT carelessly add or drop a doubled letter. If you write `tulli` instead of `tuli`, you've changed "fire" to "customs". This is one of the highest-frequency Finnish proofreading errors.

### J. Agglutinative morphology — suffixes stack

Finnish is highly agglutinative. A single word can carry stem + plural marker + case + possessive + clitic particle:

| Word | Breakdown | Translation |
|------|-----------|-------------|
| taloissani | talo + i + ssa + ni | "in my houses" |
| taloissanikin | talo + i + ssa + ni + kin | "also in my houses" |
| epäjärjestelmällistyttämättömyydellänsäkäänkö | (notorious example, 1 word) | "even without his/her ability to make something unsystematic?" |

Translation implication: where English uses 4-5 small words, Finnish often uses 1 long word. Don't try to break it up unnaturally.

### K. Sentence completeness — predicates required (severity 1.5)

Finnish requires complete predicates. Noun phrases alone are often grammatically incomplete.

| Wrong (English-style fragment) | Correct (with predicate) |
|-------------------------------|--------------------------|
| Tiimissäsi 5 olemassa olevaa | **Tiimissäsi on 5 olemassa olevaa** "There are 5 existing in your team" |
| Vain 3–50 merkkiä | **Vain 3–50 merkkiä sallittu** "Only 3–50 characters allowed" |
| Käännös valmis | (acceptable as label, but in full sentence:) **Käännös on valmis.** |

Status-message labels (e.g., "Loading...", "Saved") can use participle-only forms (`Tallennettu`), but full sentences need a verb (`olla` = "to be" — most common).

### L. Active vs Passive Voice — strict rule (severity 2.0)

Finnish passive (impersonal) has NO agent/subject. When a nominative subject is present, the verb MUST be in active form. Passive is for impersonal/agentless statements (status messages, generic actions).

| Wrong (passive + subject) | Correct (active when subject present) |
|---------------------------|---------------------------------------|
| Teknologiapinonne ei merkitä | **Teknologiapinonne ei merkitse** (active 3sg) |
| Järjestelmä päivitetään | **Järjestelmä päivittää itsensä** (active) OR drop subject: **Päivitetään...** |

| Wrong (active when subject absent) | Correct (passive for agentless) |
|-----------------------------------|---------------------------------|
| (Subject) lataa... | **Ladataan...** "Loading..." (no subject) |
| (Subject) tallentaa... | **Tallennetaan...** "Saving..." |

**Rule of thumb**: status messages without explicit subject → passive (Ladataan, Tallennetaan, Käsitellään). Statements with subject → active (Käyttäjä lataa, Järjestelmä tallentaa).

### M. Verb Tense and Aspect — pluperfect requires PRIOR event (severity 2.0)

Finnish has four tenses:
- **Present** (preesens): `tallennan` "I save / am saving"
- **Imperfect / simple past** (imperfekti): `tallensin` "I saved"
- **Perfect** (perfekti): `olen tallentanut` "I have saved"
- **Pluperfect** (pluskvamperfekti): `olin tallentanut` "I had saved"

**CRITICAL RULE**: Pluperfect (olin + NUT-participle) REQUIRES a prior completed action before another past event. Don't use it for standalone past events or immediate emotional reactions.

| Wrong | Correct | Reason |
|-------|---------|--------|
| olin melkein itkenyt (immediate reaction) | **melkein itkin** | Simple past for emotional reactions |
| olin nähnyt sen eilen (no prior event) | **näin sen eilen** | Standalone past = imperfekti |
| tein sen koska halusin (prior cause as state) | **tein sen koska olin halunnut** | Pluperfect when one past preceded another |

---

## UI Conventions

### Buttons — imperative (sinä form by default)

| Wrong | Correct |
|-------|---------|
| Tallentaa (infinitive) | **Tallenna** (sinä imperative) |
| Tallentakaa (Te imperative — only if file is Te throughout) | **Tallenna** (default sinä) |
| Poistaminen (verbal noun) | **Poista** |
| Peruuttamaan (3rd infinitive) | **Peruuta** |

Common button labels:

| English | Finnish (sinä) | Finnish (Te) |
|---------|----------------|--------------|
| Save | Tallenna | Tallentakaa |
| Cancel | Peruuta | Peruuttakaa |
| Delete | Poista | Poistakaa |
| Edit | Muokkaa | Muokatkaa |
| Open | Avaa | Avatkaa |
| Close | Sulje | Sulkekaa |
| Send | Lähetä | Lähettäkää |
| Search | Etsi | Etsikää |
| Confirm | Vahvista | Vahvistakaa |
| Continue | Jatka | Jatkakaa |
| Back | Takaisin | Takaisin |
| Next | Seuraava | Seuraava |
| Skip | Ohita | Ohittakaa |
| Submit | Lähetä | Lähettäkää |
| Apply | Käytä | Käyttäkää |
| Reset | Palauta | Palauttakaa |
| Copy | Kopioi | Kopioikaa |
| Paste | Liitä | Liittäkää |
| Cut | Leikkaa | Leikatkaa |
| Undo | Kumoa | Kumotkaa |
| Redo | Tee uudelleen | Tehkää uudelleen |
| Share | Jaa | Jakakaa |
| Help | Apua / Ohje | — |

### Status messages — IMPERSONAL PASSIVE

Use the Finnish impersonal passive (-taan/-tään). This is the idiomatic form for loading/processing/saving states.

| Wrong | Correct |
|-------|---------|
| Tallennan... (1sg active) | **Tallennetaan...** "Saving..." |
| Lataan... (1sg active) | **Ladataan...** "Loading..." |
| Käsittelen... (1sg active) | **Käsitellään...** "Processing..." |
| Etsin... (1sg active) | **Etsitään...** "Searching..." |
| Yhdistän... | **Yhdistetään...** "Connecting..." |

| English status | Finnish |
|----------------|---------|
| Loading... | Ladataan... |
| Saving... | Tallennetaan... |
| Processing... | Käsitellään... |
| Connecting... | Yhdistetään... |
| Searching... | Etsitään... |
| Uploading... | Ladataan ylös... |
| Downloading... | Ladataan alas... |
| Updating... | Päivitetään... |
| Deleting... | Poistetaan... |

### Completion messages — concise, no exclamations

Finns dislike effusive feedback. Drop the "Great!", "Awesome!" tone.

| Wrong | Correct |
|-------|---------|
| Valmista! Käännöksesi on nyt valmis. | **Käännös valmis** |
| Hienoa! Kaikki on tallennettu. | **Kaikki tallennettu** |
| Onnistui! Tiedosto on ladattu. | **Tiedosto ladattu** |
| Mahtavaa! Päivitys onnistui. | **Päivitys valmis** |

Use **past participle (NUT/TU forms)** for completion: `Tallennettu`, `Ladattu`, `Poistettu`, `Lähetetty`, `Päivitetty`.

### Empty state — concise, descriptive

| Wrong | Correct |
|-------|---------|
| Hakutuloksia ei löytynyt | **Ei tuloksia** |
| Sinulla ei ole vielä yhtään projektia | **Ei vielä projekteja** |
| Sähköpostilaatikko on tyhjä | **Postilaatikko tyhjä** (label) / **Postilaatikko on tyhjä** (sentence) |
| Tyhjä | (avoid alone) — extend: **Ei sisältöä** / **Ei mitään näytettävää** |

| English | Finnish |
|---------|---------|
| No results | Ei tuloksia |
| No items | Ei kohteita |
| No notifications | Ei ilmoituksia |
| No selection | Ei valintaa |
| No data | Ei tietoja |
| No connection | Ei yhteyttä |
| File not found | Tiedostoa ei löytynyt |
| No content | Ei sisältöä |

### Error messages — direct, with guidance

| Wrong | Correct |
|-------|---------|
| Epäonnistunut lataus | **Lataus epäonnistui** (verb form, not nominal calque) |
| Tiedostoa ei voida löytää | **Tiedostoa ei löydy** (avoid passive calque) |
| Tiedostoa ei löytynyt | **Tiedostoa ei löytynyt. Tarkista polku.** (error + guidance) |
| Virhe! Kokeile uudelleen. | **Toiminto epäonnistui. Yritä uudelleen.** |

### Drag and drop

| English | Finnish verb | Imperative |
|---------|--------------|------------|
| drag | **vetää** | Vedä |
| drop | **pudottaa** | Pudota |
| release (let go) | **vapauttaa** | Vapauta |
| browse (file picker) | **selata** — BUT prefer action: **valita** | Valitse |

| Wrong | Correct |
|-------|---------|
| Drägää tänne | **Vedä tähän** (native verb) |
| Dropaa tiedostot | **Pudota tiedostot** (native verb) |
| Selaa tiedostoja (browse) | **Valitse tiedostoja** (action-oriented "select" preferred for file picker) |

### Validation messages

| Type | Mood | Example |
|------|------|---------|
| Field validation | indicative | `Tämä kenttä on pakollinen` / `Muoto ei ole oikea` |
| Action instruction | imperative (matching formality) | `Syötä oikea arvo` (sinä) / `Syöttäkää oikea arvo` (Te) |
| State description | impersonal | `Yhteyttä ei voitu muodostaa` |

### Placeholder restructuring

NEVER attach a Finnish case suffix directly to a placeholder — the value might already include a name with its own ending, and stacking suffixes produces garbage.

| Wrong | Correct |
|-------|---------|
| `{name}:n asetukset` (suffix on placeholder) | **`Käyttäjän {name} asetukset`** (move to host noun) |
| `Tiedoston {name}sta` | **`Tiedostosta {name}`** (restructure word order) |
| `Hei {name}lle!` | **`Hei, {name}!`** OR `Tervehdys käyttäjälle {name}!` |

### Quantity expressions

| Wrong | Correct |
|-------|---------|
| 25+ kieltä | **yli 25 kieltä** (Finnish spells out "more than") |
| +{count} lisää | **ja {count} lisää** OR **{count} lisää** |
| noin ~10 merkkiä | **~10 merkkiä** OR **noin 10 merkkiä** (NEVER both — symbol already means "noin") |
| yli +5 tiedostoa | **+5 tiedostoa** OR **yli 5 tiedostoa** (symbol already means "yli") |

### Ellipsis completion — head noun required

| Wrong (bare quantifier) | Correct (with head noun) |
|-------------------------|--------------------------|
| ja 4 muuta | **ja 4 muuta tiedostoa** / **ja 4 muuta kohdetta** |
| veel 3 muuta | **vielä 3 muuta kohdetta** |

---

## Punctuation, Numbers, Dates, Currency

| Item | Finnish |
|------|---------|
| Decimal separator | **`,`** (comma) |
| Thousands separator | **` `** (non-breaking space) |
| Example number | `1 234,56` |
| Currency | `99,99 €` (symbol AFTER, with NBSP space) — Finland is in the Eurozone since 2002 |
| Range with EUR | `5–50 €` (en-dash, not hyphen) |
| Date (numeric) | `15.1.2024` (DD.MM.YYYY, periods, no leading zeros required) or `15.01.2024` |
| Date (long) | `15. tammikuuta 2024` (day-ordinal + month-partitive, lowercase month) |
| Time | `14.30` or `klo 14.30` (24-hour, period separator; colon `14:30` also accepted) |
| Quotation marks | **`»...«`** (reverse guillemets — traditional Finnish) OR **`"..."`** (curly modern) — NOT English `"..."` |
| Ellipsis | `…` single character (NOT three periods `...`) |
| Ampersand | `ja` (NOT `&`, except in brand names) |
| Space before unit symbol | yes (NBSP preferred): `10 MB`, `99,9 %` |
| Percent | `99,9 %` (comma decimal, space before %) |

| Wrong | Correct |
|-------|---------|
| `1,234.56 €` (English format) | **`1 234,56 €`** |
| `99.9 %` (period decimal) | **`99,9 %`** |
| `"Finnish quotes"` (English) | **`»Finnish quotes«`** or **`"Finnish quotes"`** |
| `01/15/2024` (US format) | **`15.1.2024`** |
| `5-50€` (no space, no en-dash) | **`5–50 €`** |
| `14:30` (acceptable but...) | **`14.30`** (period is traditional Finnish) |

### Months (always lowercase)

| Month | Finnish | Etymology |
|-------|---------|-----------|
| January | tammikuu | "oak month" |
| February | helmikuu | "pearl month" |
| March | maaliskuu | "earth month" |
| April | huhtikuu | "burn-clearing month" |
| May | toukokuu | "spring sowing month" |
| June | kesäkuu | "summer month" |
| July | heinäkuu | "hay month" |
| August | elokuu | "harvest month" |
| September | syyskuu | "autumn month" |
| October | lokakuu | "muddy month" |
| November | marraskuu | "death/dead month" |
| December | joulukuu | "Christmas month" |

In dates: **partitive form** (`tammikuuta`, `helmikuuta`, etc.). Always lowercase in running text.

### Days (always lowercase)

| Day | Finnish |
|-----|---------|
| Monday | maanantai |
| Tuesday | tiistai |
| Wednesday | keskiviikko |
| Thursday | torstai |
| Friday | perjantai |
| Saturday | lauantai |
| Sunday | sunnuntai |

Always lowercase in running text.

### Comma rules

Finnish is comma-heavy in subordinating clauses, comma-free in coordinating conjunctions:

| Before | Comma? |
|--------|--------|
| ja / tai / vai (and / or) | **No comma** |
| että / kun / jos / koska / joka / mikä / kuka (subordinating) | **Comma always required** |
| mutta / vaan (but) | **Comma required** |

| Wrong | Correct |
|-------|---------|
| Vedä tiedostot tähän, tai napsauta | **Vedä tiedostot tähän tai napsauta** (no comma before tai) |
| Näen että tiedosto on avoinna | **Näen, että tiedosto on avoinna** (comma before että) |
| Tämä on helppoa mutta tehokasta | **Tämä on helppoa, mutta tehokasta** |
| Jos haluat tallentaa napsauta tästä | **Jos haluat tallentaa, napsauta tästä** (comma after if-clause) |

### Word order

- Default: **SVO** — `Käyttäjä tallentaa tiedoston`.
- Flexible due to case marking — topicalization is common: `Tiedoston käyttäjä tallentaa` (emphasis on file).
- **Yes/no questions**: verb takes `-ko/-kö` suffix and moves to front: `Tallentaako käyttäjä?` "Does the user save?"
- **Wh-questions**: question word first: `Mitä tallennat?` "What are you saving?"

| Wrong | Correct |
|-------|---------|
| Sinä haluatko tallentaa? | **Haluatko tallentaa?** (-ko on verb, verb-first) |
| Tämä on järkevä | (correct) | This is sensible |
| Tämä on... (English filler "This is...") | **Tämä...** (often the verb is unnecessary) |

### Negation — invariant `ei` conjugates, main verb in stem

The negative auxiliary `ei` conjugates by person; the main verb stays in the bare negative stem form (looks like 1sg without `-n`).

| Person | Negation | Verb form |
|--------|----------|-----------|
| 1sg | en | tallenna |
| 2sg | et | tallenna |
| 3sg | ei | tallenna |
| 1pl | emme | tallenna |
| 2pl / formal | ette | tallenna |
| 3pl | eivät | tallenna |

| Wrong | Correct |
|-------|---------|
| en tallennan | **en tallenna** (verb stem after negation) |
| ei tallennetaan (passive) | **ei tallenneta** (passive negative form) |
| emme tallennamme | **emme tallenna** |

---

## Terminology

### Preferred UI terms

| English | Preferred Finnish | Avoid |
|---------|-------------------|-------|
| Click | **napsauttaa** / `napsauta` (button) | klikata, klikkailla |
| Save | **tallentaa** / `Tallenna` | seivaata |
| Open | **avata** / `Avaa` | — |
| Close | **sulkea** / `Sulje` | — |
| Download | **ladata (alas)** / `Lataa` | dauntloudaata |
| Upload | **ladata (ylös)** / `Lataa ylös` | aploudaata |
| Delete | **poistaa** / `Poista` | deletoida |
| Edit | **muokata** / `Muokkaa` | editoida |
| Cancel | **peruuttaa** / `Peruuta` | — |
| Email | **sähköposti** | email, mail |
| Browser | **selain** | brauseri |
| Dashboard | **koontinäyttö** / **kojelauta** | — |
| Settings | **asetukset** | — |
| Search | **haku** (noun) / **etsiä** (verb) / `Etsi` | searchata |
| Folder | **kansio** | — |
| File | **tiedosto** | — |
| Login / Log in | **kirjautuminen** (noun) / **kirjautua sisään** (verb) / `Kirjaudu sisään` | — |
| Logout | **kirjautua ulos** / `Kirjaudu ulos` | — |
| Account | **tili** | — |
| User | **käyttäjä** | — |
| Profile | **profiili** | — |
| Password | **salasana** | — |
| Username | **käyttäjänimi** | — |
| Notification | **ilmoitus** | notifikaatio |
| Sign up / register | **rekisteröityä** / `Rekisteröidy` | — |
| Subscribe | **tilata** | — |
| Filter | **suodatin** (noun) / **suodattaa** (verb) | filtteri |
| Sort | **lajitella** / `Lajittele` | — |
| Refresh | **päivittää** / `Päivitä` | refreshata |
| Copy | **kopioida** / `Kopioi` | — |
| Paste | **liittää** / `Liitä` | — |
| Cut | **leikata** / `Leikkaa` | — |
| Undo | **kumota** / `Kumoa` | — |
| Redo | **tehdä uudelleen** / `Tee uudelleen` | — |
| Share | **jakaa** / `Jaa` | sharetä |
| Help | **apu** / **ohje** | — |
| Welcome | **tervetuloa** | — |
| Success | **onnistui** | — |
| Error | **virhe** | — |
| Warning | **varoitus** | — |
| Loading | **lataaminen** / **ladataan** | — |
| Saving | **tallentaminen** / **tallennetaan** | — |
| Required | **pakollinen** | — |
| Optional | **valinnainen** | — |
| Free | **ilmainen** / **maksuton** | — |
| Paid | **maksullinen** | — |
| Premium | **premium** (accepted) | — |
| Trial | **kokeilujakso** | — |
| Subscription | **tilaus** | — |
| Payment | **maksu** | — |
| Invoice | **lasku** | — |
| Coupon | **alennuskoodi** | — |
| Discount | **alennus** | — |

### Software domain terminology — preserve IT meaning (severity 2.5)

Polysemous words MUST use their IT-domain meaning in software contexts:

| English (IT) | Wrong (general/wrong domain) | Correct (IT meaning) |
|--------------|-----------------------------|----------------------|
| pipeline (CI/CD) | putki (plumbing) | **liukuhihna / putki** (DevOps context — pipeline accepted) |
| architecture (software) | (building/construction) | **arkkitehtuuri** (IT context) |
| commit (git) | `ladattu gitiin` (= uploaded into git) | **commitata / lisätä gitiin** |
| launch (product) | (military / spatial) | **julkaista / tuoda markkinoille / lanseerata** |
| deploy (code) | (military) | **ottaa käyttöön / julkaista / asentaa tuotantoon** |
| migrate (data) | (general "move") | **migroida / siirtää** |
| source of truth | (literal "truth source") | **autoritatiivinen tietolähde / yksi totuuden lähde** |
| build (software) | (construction) | **rakentaa / koota** |

### Brand name inflection — connecting vowel "i" for consonant-final stems

Finnish requires brand names to take case suffixes. The rules differ for vowel-final vs consonant-final stems:

- **Uppercase abbreviations**: colon + case ending. `API:ssa`, `EU:ssa`, `HTML:ää`, `USB:ta`, `USA:ssa`.
- **Consonant-final brand names**: colon + **connecting vowel `i`** (liitevokaali) + case ending. The `i` is required before case suffixes on consonant-final stems.
  - `Agent:ia` (partitive), `Agent:issa` (inessive)
  - `React:ia` (partitive), `React:issa` (inessive), `React:ista` (elative)
  - `Figment:iin` (illative), `Slack:in` (genitive)
- **Vowel-final brand names**: colon + case ending directly (no connecting vowel needed).
  - `Google:sta` (elative)
  - `Vercel:issä` (inessive — note vowel harmony, `Vercel` ends in `e/l` → front)
  - `Notion:issa`, `Figma:ssa`

| Wrong | Correct |
|-------|---------|
| Agent:a (missing connecting vowel) | **Agent:ia** |
| Agent:ssa | **Agent:issa** |
| React:a | **React:ia** |
| Figment:ssa | **Figment:issä** (front harmony) |
| Slack:n | **Slack:in** |

### File-format compounds

File formats attach to `tiedosto` with a hyphen:
- `JSON-tiedosto`, `YAML-tiedosto`, `CSV-tiedosto`, `XML-tiedosto`, `PDF-tiedosto`, `Properties-tiedosto`

### API terms

- `API-avain` (singular), `API-avaimet` (plural)
- `API-kutsu` (API call)
- `API-piste / päätepiste` (endpoint)

---

## Calque / Anti-Pattern Blocklist

### Idiom calques

| Wrong (literal) | Natural Finnish | Reason |
|-----------------|-----------------|--------|
| Se tekee järkeä | **Se on järkevää** / **Siinä on järkeä** | "makes sense" calque |
| Päivän lopussa | **Loppujen lopuksi** / **Pohjimmiltaan** | "at end of day" calque |
| olla samalla sivulla | **olla samaa mieltä** | "on the same page" calque |
| ottaa se helppona | **ottaa rennosti** | "take it easy" calque |
| Murra jalka! (literal "Break a leg") | **Onnea matkaan! / Tsemppiä!** | Use Finnish good-luck idiom |
| Pala kakkua (literal "piece of cake") | **Helppo nakki / Ei ole rakettitiedettä** | Use Finnish "easy" idiom |
| Kun siat lentävät (literal) | **Kun lehmät lentää** | Finnish "never" idiom (cows fly, not pigs) |
| Tappaa kaksi lintua | **Lyödä kaksi kärpästä yhdellä iskulla** | Two flies with one strike, not birds |

### Word-for-word calques

| Wrong | Correct | Reason |
|-------|---------|--------|
| Tämä on... (English "This is...") | **Tämä...** (often verb unnecessary) | Unnecessary "on" — calque |
| Oletusarvona arvo | **Oletusarvo** | Redundant construction |
| Tiedostoa ei voida löytää | **Tiedostoa ei löydy** | Avoid passive-modal calque |
| Jos siinä tapauksessa, että | **Jos** | "In case if" — verbose |
| Tehdä parannus | **parantaa** | Direct verb, not noun+verb |
| Antaa vastaus | **vastata** | Direct verb |
| Tehdä päätös | **päättää** | Direct verb |

### Structural calques

| Wrong (English-style) | Correct (natural Finnish) |
|----------------------|---------------------------|
| Saa käännös valmiiksi minuuteissa | **Käännös muutamassa minuutissa** ("Get X done" → nominal construction) |
| Pidä projektisi synkronoituina | **Varmista projektien synkronointi** ("Keep X adj" → "varmista" construction) |
| Tee työnkulustasi nopeampi | **Nopeuta työnkulkuasi** ("Make X adj" → direct verb) |

### Marketing telegram-style fragments

English marketing often uses period-separated fragments. Finnish prefers complete noun phrases:

| Wrong | Correct |
|-------|---------|
| Nopea käännös. Turvallinen. Luotettava. | **Nopeat, turvalliset ja luotettavat käännökset** |
| Helppo. Nopea. Tehokas. | **Helppoja, nopeita ja tehokkaita** |

### Compound adjective calques

Finnish forms compound adjectives differently from English:

| English | Wrong | Correct |
|---------|-------|---------|
| X-powered / X-driven | X-käyttöinen / X-vetävä | **X-pohjainen / X:n avulla toimiva / X-teknologialla** |
| AI-powered | AI-vetävä | **tekoälypohjainen / tekoälyn avulla toimiva** |
| X-aware / context-aware | konteksti-tietoinen | **kontekstin huomioiva / X-yhteensopiva** |
| X-friendly / user-friendly | käyttäjä-ystävällinen | **helppokäyttöinen / käyttäjälle sopiva** |
| X-based / cloud-based | pilvi-pohjainen (hyphen wrong) | **pilvipohjainen** (one word) |

### Proper noun calques

| Wrong (full form in UI) | Correct (short form) |
|-------------------------|----------------------|
| Amerikan yhdysvallat | **Yhdysvallat** / **USA** |
| Ison-Britannian ja Pohjois-Irlannin yhdistynyt kuningaskunta | **Iso-Britannia** / **Britannia** |
| Saksan liittotasavalta | **Saksa** |

### Anglicism verbs — Finnish prefers native

| Anglicism (avoid) | Native Finnish |
|-------------------|----------------|
| klikata | **napsauttaa** |
| deletoida | **poistaa** |
| editoida | **muokata** |
| seivaata | **tallentaa** |
| dauntloudaata | **ladata (alas)** |
| aploudaata | **ladata (ylös)** |
| sharetä | **jakaa** |
| filtteröidä | **suodattaa** |
| refreshata | **päivittää** |
| checkata | **tarkistaa** |

### PER vs FOR distinction (severity 1.5)

| English | Finnish | Meaning |
|---------|---------|---------|
| per (rate) | **kohden / kohti** | `kieltä kohden` "per language" (rate per unit) |
| for (total) | **-lle / -ään** (allative) | `kielelle` "for the language" (total recipient) |

These are NOT interchangeable. "per" is rate; "for" is total.

| Wrong (confusion) | Correct |
|------------------|---------|
| `kielelle` (meaning "per language") | **kieltä kohden** ("per language" rate) |
| `kieltä kohden` (meaning "for the language") | **kielelle** ("for the language" total) |

### Russian-influenced calques — rare in Finland but watch for

Finland has historical Russian/Soviet influence (Karelia, Winter War), and some Russian-influenced constructions exist in older Finnish texts. Modern Finnish UI prefers native:

| Russian-influenced (avoid) | Native Finnish |
|----------------------------|----------------|
| `joka tapauksessa` (overused) | `kaikessa tapauksessa / ainakin` |
| `ei mitään` (literal "not nothing" — double-negative Russian-style) | `ei ole mitään` (Finnish: `ei` + verb only) |
| `tehdä päätös` (Russian-influenced noun+verb) | `päättää` (single verb) |

### Symbol + word redundancy

| Wrong | Correct |
|-------|---------|
| noin ~10 merkkiä | **~10 merkkiä** OR **noin 10 merkkiä** (~ already means "noin") |
| yli +5 tiedostoa | **+5 tiedostoa** OR **yli 5 tiedostoa** (+ already means "yli") |
| alle <3 | **<3** OR **alle 3** |

### Puhekieli (spoken) forms — NEVER in UI

| Puhekieli (avoid in UI) | Kirjakieli (UI form) |
|-------------------------|----------------------|
| mä, sä, mun, sun | minä, sinä, minun, sinun |
| oon, oot, oo | olen, olet, on |
| kaa | kanssa |
| niinku, semmonen | niin kuin, sellainen |
| kyllähän, oonha | kyllähän → fine; oonhan → olenhan |
| tiiän, tuun | tiedän, tulen |
| käyttäjän kaa | **käyttäjän kanssa** |

---

## Self-Check Checklist (run before finalizing)

### Critical accuracy (must all pass)

- [ ] **Correct case** from 15 options (illative -Vn for motion into, inessive -ssa/-ssä for location, partitive -a/-ä/-ta/-tä for partial/counted object, etc.)
- [ ] **Vowel harmony** observed throughout — front (ä/ö/y) suffixes on front-vowel stems, back (a/o/u) suffixes on back-vowel stems
- [ ] **Consonant gradation** correct (kk→k, pp→p, tt→t, t→d, p→v, k→Ø/v) when adding case suffixes
- [ ] **Verb-governed case correct** (auttaa+partitive, pitää+elative, luottaa+illative, etsiä+partitive, tarvita+partitive, odottaa+partitive)
- [ ] **Numbers 2+ take partitive SINGULAR** (`viisi tiedostoa`, NOT `viisi tiedostot` or `viisi tiedostoja`)
- [ ] **ICU `other` branch uses partitive singular** (`other {# tiedostoa}`, NOT `# tiedostot` or `# tiedostoja`)
- [ ] **Sinä/Te consistent** throughout (pronouns, possessive suffixes -si/-nne, imperatives Tallenna/Tallentakaa)
- [ ] **Adjective agreement** in case + number (NO gender — `uudet tiedostot` nom pl, `uusia tiedostoja` part pl)
- [ ] **Negation** uses conjugated `ei/en/et` + bare negative stem (`en tallenna`, `ei tallenneta`)
- [ ] **Active vs passive voice** correct — active with nominative subject (`Stack ei merkitse`), passive only for impersonal (`Tallennetaan...`)
- [ ] **Possessive suffixes** correctly attached after case (talossani, asetuksissasi)
- [ ] **Verb tense correct** — imperfekti for standalone past (`tallensin`), pluskvamperfekti ONLY when prior action preceded another past event (`olin tallentanut, kun...`)
- [ ] **Long vs short** vowels/consonants preserved (tuli vs tuuli vs tulli are 3 different words)
- [ ] **No suffix on placeholders** (restructure to put suffix on host noun — `Käyttäjän {name} asetukset`, NOT `{name}:n asetukset`)
- [ ] **Foreign name inflection** — consonant-final brand stems take connecting vowel `i` before case (`Agent:ia`, `React:issa`)
- [ ] **Quotation marks** `»...«` or `"..."`, NOT English `"..."`
- [ ] **Comma rules**: comma before että/jos/kun/koska/joka/mutta; NO comma before ja/tai/vai
- [ ] **Number format** `1 234,56`; date `15.1.2024`; currency `99,99 €`; time `14.30` or `klo 14.30`
- [ ] All `{variables}` and ICU intact
- [ ] **Domain terminology** preserves IT meaning (arkkitehtuuri = IT design, liukuhihna/pipeline = CI/CD, ottaa käyttöön = deploy)

### Naturalness

- [ ] Buttons in imperative matching formality (`Tallenna` sinä / `Tallentakaa` Te)
- [ ] Status messages use **impersonal passive** (`Tallennetaan...`, `Ladataan...`, `Käsitellään...`) — NOT 1sg active
- [ ] Completion messages concise, no exclamations (`Käännös valmis`, NOT `Hienoa! Käännöksesi on nyt valmis.`)
- [ ] Empty states concise (`Ei tuloksia`, NOT `Hakutuloksia ei löytynyt`)
- [ ] Native verbs over anglicism verbs (`napsauttaa` not `klikata`, `poistaa` not `deletoida`, `tallentaa` not `seivaata`)
- [ ] No literal idiom calques (`on järkevää` not `tekee järkeä`)
- [ ] No telegram-style fragment marketing — use complete noun phrases
- [ ] File picker uses action verb (`Valitse tiedostoja`, NOT `Selaa tiedostoja`)
- [ ] Drag-drop: `vetää / pudottaa / vapauttaa` (native Finnish verbs)
- [ ] Quantity expressions: `yli 25 kieltä` not `25+ kieltä`; `ja {count} lisää` not `+{count} lisää`
- [ ] No symbol+word redundancy (`~10` or `noin 10`, never `noin ~10`)
- [ ] Written kirjakieli only — NO puhekieli (minä not mä, kanssa not kaa, olen not oon)
- [ ] Compound adjectives natural Finnish (X-pohjainen, X:n avulla)
- [ ] Proper nouns short form (USA not Amerikan yhdysvallat)
- [ ] Direct, concise tone — Finns value straightforward communication, no excessive hedging
- [ ] Communicative intent preserved (declarative stays declarative, imperative stays imperative)
- [ ] Existence statements have predicate (`Tiimissäsi on 5 jäsentä`, NOT `Tiimissäsi 5 jäsentä`)

---

## Worked Examples

### Example 1: Onboarding welcome

**Source:** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

#### Finnish (sinä, default modern UI)

> Tervetuloa! Valitse tiedosto, jonka haluat ladata — tuemme yli 25 tiedostomuotoa ja käännämme sen 5 kielelle {seconds} sekunnissa. Älä huoli, voit peruuttaa milloin tahansa.

**Notes:**
- `Valitse` (sinä imperative, not Te `Valitkaa`)
- `Valitse` not `Selaa` (action-oriented file picker)
- `jonka haluat ladata` relative clause with -da infinitive after `haluat`
- `yli 25 tiedostomuotoa` — partitive singular after partitive-governing quantifier (yli + number); also `yli` not `25+`
- `5 kielelle` allative for "for 5 languages" (total recipient)
- `{seconds} sekunnissa` — restructured to put case suffix on host noun, not placeholder
- `peruuttaa` not `kanselloida` (native verb)

#### Finnish (Te, formal alternative)

> Tervetuloa! Valitkaa tiedosto, jonka haluatte ladata — tuemme yli 25 tiedostomuotoa ja käännämme sen 5 kielelle {seconds} sekunnissa. Älkää huoliko, voitte peruuttaa milloin tahansa.

**Notes:**
- `Valitkaa / Älkää huoliko / voitte` all Te-form
- Everything else identical (case, vowel harmony, etc.)

### Example 2: Status / error / completion messages

| English | Finnish |
|---------|---------|
| Loading... | Ladataan... |
| Saving your work... | Tallennetaan työtäsi... |
| Processing 5 files... | Käsitellään 5 tiedostoa... |
| Upload failed. Try again. | Lataus epäonnistui. Yritä uudelleen. |
| File not found. Check the path. | Tiedostoa ei löytynyt. Tarkista polku. |
| Saved | Tallennettu |
| 5 files uploaded | 5 tiedostoa ladattu |
| Translation complete | Käännös valmis |
| No results | Ei tuloksia |
| No notifications yet | Ei vielä ilmoituksia |

### Example 3: Settings form

**Source:** "Settings — Update your profile information. Your changes will be saved automatically."

#### Finnish (sinä)

> Asetukset — Päivitä profiilitietosi. Muutoksesi tallennetaan automaattisesti.

**Notes:**
- `Päivitä` sinä imperative
- `profiilitietosi` = profiili + tieto-plural + -si (2sg possessive)
- `tallennetaan` impersonal passive (no agent — system saves automatically)
- `automaattisesti` (Finnish adverb form, not `automaattisesti`)

#### Finnish (Te)

> Asetukset — Päivittäkää profiilitietonne. Muutoksenne tallennetaan automaattisesti.

### Example 4: ICU plural with partitive

**Source:** `{count, plural, one {You have # unread message} other {You have # unread messages}}`

#### Finnish (sinä)

```icu
{count, plural, one {Sinulla on # lukematon viesti} other {Sinulla on # lukematonta viestiä}}
```

**Notes:**
- `one`: `# lukematon viesti` nominative singular (with adjective agreeing in nominative)
- `other`: `# lukematonta viestiä` partitive SINGULAR (adjective also partitive singular)
- NOT `# lukemattomia viestejä` (partitive PLURAL — wrong for ICU other branch with numerals)

### Example 5: Common errors caught by the checklist

- ❌ `5 tiedostot` → ✅ `5 tiedostoa` (partitive singular with 5+)
- ❌ `5 tiedostoja` → ✅ `5 tiedostoa` (partitive SINGULAR, not plural)
- ❌ `järjestelmassa` → ✅ `järjestelmässä` (vowel harmony — front vowel stem needs front suffix)
- ❌ `kansiössä` → ✅ `kansiossa` (vowel harmony — back vowel stem needs back suffix)
- ❌ `auttaa käyttäjälle` → ✅ `auttaa käyttäjää` (auttaa governs partitive)
- ❌ `pidän musiikkia` → ✅ `pidän musiikista` (pitää "to like" governs elative)
- ❌ `luottaa järjestelmässä` → ✅ `luottaa järjestelmään` (luottaa governs illative)
- ❌ `Stack:nne ei merkitä` → ✅ `Stack:nne ei merkitse` (active with nominative subject)
- ❌ `Tallennan...` → ✅ `Tallennetaan...` (impersonal passive for status)
- ❌ `olin melkein itkenyt` (reaction) → ✅ `melkein itkin` (imperfekti for emotional reactions)
- ❌ `Voitte muuttaa asetuksiasi` → ✅ `Voitte muuttaa asetuksianne` (verb+possessive must match formality)
- ❌ `mä tallennan` → ✅ `minä tallennan` / `tallennan` (kirjakieli, no puhekieli in UI)
- ❌ `Se tekee järkeä` → ✅ `Se on järkevää` (idiom calque)
- ❌ `Selaa tiedostoja` → ✅ `Valitse tiedostoja` (file picker convention)
- ❌ `25+ kieltä` → ✅ `yli 25 kieltä` (Finnish spells out "more than")
- ❌ `noin ~10` → ✅ `~10` or `noin 10` (symbol+word redundancy)
- ❌ `Agent:a` → ✅ `Agent:ia` (consonant-final stem needs connecting vowel i)
- ❌ `Näen että tiedosto on avoinna` → ✅ `Näen, että tiedosto on avoinna` (comma before että)
- ❌ `Vedä tähän, tai napsauta` → ✅ `Vedä tähän tai napsauta` (no comma before tai)
- ❌ `1,234.56 €` → ✅ `1 234,56 €` (Finnish number format)
- ❌ `01/15/2024` → ✅ `15.1.2024` (DD.MM.YYYY)
- ❌ `other {# tiedostot}` → ✅ `other {# tiedostoa}` (ICU other = partitive singular)
- ❌ `klikata, deletoida, seivaata` → ✅ `napsauttaa, poistaa, tallentaa` (native verbs)

---

## When in Doubt

1. **Check sister-language Estonian rules** — many patterns transfer, but watch for the differences (Finnish 15 cases vs Estonian 14, Finnish strict vowel harmony vs Estonian none, different lexicon).
2. **Default to sinä** — Finnish UI culture is informal; only escalate to Te for legal/banking/government.
3. **Default to partitive** — when counting (2+), negating, or expressing partial/ongoing action, you almost always need partitive.
4. **Default to impersonal passive** for status messages — `-taan/-tään` form.
5. **Default to native verb** when an anglicism verb is available — `napsauttaa` not `klikata`.
6. **Default to concise** — Finns prefer direct, unadorned communication. Drop hedging, drop exclamations, drop fluff.
7. **Default to compound words written together** — `työpaikka`, `tiedostomuoto`, `käyttäjänimi`, NOT hyphenated like English.
8. **Default to kirjakieli** — never use puhekieli (mä, sä, oon, kaa) in product text, even casual marketing.
9. **Vowel harmony check** — before finalizing any suffix, scan the stem: front-vowel stem (ä/ö/y) → front suffix (-ssä, -ä, -llä); back-vowel stem (a/o/u) → back suffix (-ssa, -a, -lla); neutral-only stem (e/i) → front suffix by default.
10. **Length check** — doubled vowels and consonants are meaning-critical. `tuli` (fire) ≠ `tuuli` (wind) ≠ `tulli` (customs). Proofread carefully.

When fundamentally unsure between two correct-looking options, the answer is almost always the one that is **(a) shorter**, **(b) uses a native Finnish verb**, **(c) uses the impersonal passive for agentless action**, and **(d) preserves vowel harmony**. Finnish rewards economy and structural correctness.
