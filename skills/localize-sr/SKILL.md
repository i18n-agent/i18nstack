---
name: localize-sr
description: "Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Serbian (sr / sr-Cyrl / sr-Latn). Asks the user to choose Cyrillic (ћирилица) vs Latin (latinica) on first use — both are official, equal, fully interchangeable, but MUST NOT mix within one text. Enforces ekavian forms (vreme not vrijeme), 7-case grammar, 3-gender agreement, ICU one/few/other plurals (1/2-4/5+ pattern), perfective/imperfective verb aspect, Vi/ti formality, clitic second-position (Wackernagel's law), `da + present` construction, technical-identifier Latin preservation inside Cyrillic text, glagolski prilog sadašnji (-ći) for simultaneous actions, and verb-construction integrity (no stacked finite verbs from English -ing calques)."
---

# Translate to Serbian (sr) — High-Fidelity Skill

## Scope & Variants — CRITICAL

Serbian has **TWO officially equal writing systems**, mandated by Article 10 of the Serbian Constitution: **Cyrillic (ћирилица)** and **Latin (латиница)**. They are NOT regional dialects or formality registers — they are **alternate scripts for the same language**, fully interchangeable letter-by-letter via a 1:1 mapping.

| Locale | Script | Usage | Preference signal |
|--------|--------|-------|-------------------|
| `sr-Cyrl` / `sr` (default in many CLDR contexts) | Ћирилица (Cyrillic) | Official documents, government, schools, traditional press, religious texts, formal institutional copy | Older audiences, conservative branding, state institutions, Republika Srpska |
| `sr-Latn` | Latinica (Latin) | Internet, business, IT, advertising, modern UI, international-facing material | Younger audiences, tech products, web/mobile UI, globally-facing brands |

**Practical reality:**
- The Serbian government promotes Cyrillic as primary by law (2021 Law on Use of Serbian Language).
- In **digital products** the Latin script dominates ~70-80% of real-world use because keyboards default to it and URL/email systems handle it without ambiguity.
- **Most software localization targets Latin first**, then Cyrillic if the product needs institutional credibility.

### Hard rule — NEVER mix scripts within one text (severity 3.0)

The single most-failed Serbian rule by AI translators: **producing one string with both scripts**. This is unambiguously wrong.

✓ Correct: `Кликните на дугме „Сачувај"` (all Cyrillic)
✓ Correct: `Kliknite na dugme „Sačuvaj"` (all Latin)
✗ Wrong: `Кликните na dugme „Сачувај"` (mixed — auto-fail)
✗ Wrong: `Kliknite на dugme "Sačuvaj"` (mixed — auto-fail)

**The only exception:** technical identifiers (Git, API, JSON, npm, React, URLs, placeholders `{var}`, file paths) stay in Latin script **even inside Cyrillic text**. This is the standard convention, not a violation. See "Technical identifiers" below.

### When the target locale is unspecified

**Always ask** on first use if the user requests just "Serbian":

> Serbian has two official writing systems — both equal, fully interchangeable, but never mixed within one text. Which one should I target?
>
> - **Latin (`sr-Latn`, Recommended for software)** — Dominant in IT, web, business, advertising. Default for most product UI. Modern feel.
> - **Cyrillic (`sr-Cyrl`)** — Officially primary per Serbian Constitution. Used in government, traditional press, schools, religious texts. Required for state-facing and institutional products.
> - **Both (parity localization)** — Some products legally require both. I'll deliver Latin + Cyrillic side-by-side.

Default to **`sr-Latn`** if no answer (software default).

### Cyrillic ↔ Latin 1:1 mapping table (for self-conversion verification)

| Cyrillic | Latin | Cyrillic | Latin | Cyrillic | Latin |
|----------|-------|----------|-------|----------|-------|
| А а | A a | К к | K k | Т т | T t |
| Б б | B b | Л л | L l | Ћ ћ | Ć ć |
| В в | V v | Љ љ | **Lj lj** | У у | U u |
| Г г | G g | М м | M m | Ф ф | F f |
| Д д | D d | Н н | N n | Х х | H h |
| Ђ ђ | Đ đ | Њ њ | **Nj nj** | Ц ц | C c |
| Е е | E e | О о | O o | Ч ч | Č č |
| Ж ж | Ž ž | П п | P p | Џ џ | **Dž dž** |
| З з | Z z | Р р | R r | Ш ш | Š š |
| И и | I i | С с | S s | | |
| Ј ј | J j | | | | |

**Critical: three Cyrillic digraphs (Љ Њ Џ) become TWO-letter Latin sequences (Lj Nj Dž).** Case-sensitive — `Љубав` → `Ljubav`, `ЉУБАВ` → `LJUBAV`.

**Diacritics are essential in Latin script** — Č Ć Ž Š Đ. Replacing them with C, Z, S, Dj is a critical readability failure (`crna` and `crna` are nonsense for "crna" → blackness; but `Sacuvaj` for `Sačuvaj` is genuinely broken text, even though some legacy systems strip them).

### BCMS continuum note (NOT mutual locales)

Serbian, Croatian, Bosnian, and Montenegrin are mutually intelligible South Slavic varieties (collectively "BCMS"), but they are **politically and orthographically distinct languages** with their own ISO codes (sr / hr / bs / cnr). Do NOT treat them as variants of each other. Critical differences vs Croatian (`hr`):

| Concept | Serbian (sr) — ekavian | Croatian (hr) — ijekavian |
|---------|------------------------|---------------------------|
| time | vreme | vrijeme |
| nice | lepo | lijepo |
| milk | mleko | mlijeko |
| child | dete | dijete |
| children | deca | djeca |
| river | reka | rijeka |
| world | svet | svijet |
| beautiful | lep | lijep |

If a string contains `vrijeme / lijepo / mlijeko / dijete`, **it is Croatian, not Serbian** — flag and fix to ekavian (`vreme / lepo / mleko / dete`).

Other BCMS giveaways that mean "not Serbian":
- `tjedan` (Croatian) vs `nedelja` (Serbian) — week
- `siječanj/veljača/ožujak` (Croatian month names) vs `januar/februar/mart` (Serbian)
- `kruh` (Croatian) vs `hleb` (Serbian) — bread
- `tisuća` (Croatian) vs `hiljada` (Serbian) — thousand
- `tko` (Croatian) vs `ko` (Serbian) — who
- `što` (Croatian) vs `šta` (Serbian) — what
- `nogomet` (Croatian) vs `fudbal` (Serbian) — football

---

## Register Auto-Detection (Apply Before Translating)

Serbian formality is set by **pronoun + verb-ending** choice, with capitalization conventions for the formal form. Auto-detect from source:

| Source signal | Target register |
|---------------|-----------------|
| Casual / conversational / personal (`Hey!`, contractions, emoji, marketing voice, social) | **Informal (ti)** — `ti` pronoun, lowercase, 2nd-person sg. verb endings (-š), familiar imperative (`Sačuvaj`, `Klikni`). Allow short forms, allow established loanwords (`klipbord`, `link`, `imejl`). |
| Neutral product UI / docs / consumer software (DEFAULT) | **Formal (Vi)** — `Vi` capitalized for direct address, 2nd-person pl. verb endings (-te), polite imperative (`Sačuvajte`, `Kliknite`). Possessive `Vaš/Vaša/Vaše` also capitalized. |
| Legal / banking / government / enterprise B2B | **Formal (Vi) elevated** — same `Vi` form but full constructions, no contractions, prefer reflexive impersonal (`Vrši se / Obavlja se`), avoid casual loanwords (use `elektronska pošta` over `imejl` in legal text). |

**Hard rule: never mix levels in one text.** A string with `Možete da promenite` (formal) and `tvoja podešavanja` (informal possessive) is broken.

**Capitalization rule for Vi:** `Vi / Vaš / Vaša / Vaše / Vaši / Vam / Vas` are capitalized in direct second-person address (whether you're writing to one person or many). This signals respect — failing to capitalize is read as informal even if the verb forms are formal.

**Default for software UI: Vi (formal)** unless brand voice is explicitly youth/casual.

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. Script consistency — never mix Cyrillic + Latin (severity 3.0)

Documented above. The only exception is Latin technical identifiers inside Cyrillic text.

### 2. Word integrity — verb prefixes NEVER split (severity 3.0)

Serbian verbs with prefixes are **single words**. Splitting them by a space changes meaning catastrophically or produces gibberish.

| ✗ Wrong (split) | ✓ Correct (joined) | What the split means |
|-----------------|--------------------|-----------------------|
| `pre vesti` / `пре вести` | **`prevesti`** / **`превести`** | "pre" (prefix alone) + "vesti" (news) — nonsense |
| `iz vršiti` / `из вршити` | **`izvršiti`** / **`извршити`** | nonsense |
| `pre nositi` / `пре носити` | **`prenositi`** / **`преносити`** | nonsense |
| `na praviti` / **`направити`** | nonsense |
| `sa čuvati` / `са чувати` | **`sačuvati`** / **`сачувати`** | nonsense |
| `pre uzmi` / `пре узми` | **`preuzmi`** / **`преузми`** | nonsense |
| `o pozovi` / `о позови` | **`opozovi`** / **`опозови`** | nonsense |

**Reflexive `se` is the OPPOSITE pattern** — `se` is a **separate clitic word**, NEVER attached. `prijavi se`, `registruj se`, `odjavi se`. Writing `prijavise` or `registrujse` is wrong.

### 3. Ekavian forms — never ijekavian (severity 2.0)

Serbian standard is **ekavian** (the historical "yat" → `e`). Croatian and Bosnian use **ijekavian** (yat → `ije` / `je`). Any ijekavian form in a Serbian translation is wrong.

Full ekavian/ijekavian table:

| English | Serbian (ekavian) | Croatian/Bosnian (ijekavian) — DO NOT USE |
|---------|---------------------|--------------------------------------------|
| time | vreme / време | vrijeme |
| nice | lepo / лепо | lijepo |
| milk | mleko / млеко | mlijeko |
| child | dete / дете | dijete |
| children | deca / деца | djeca |
| river | reka / река | rijeka |
| world | svet / свет | svijet |
| light | svetlost / светлост | svjetlost |
| flower | cvet / цвет | cvijet |
| star | zvezda / звезда | zvijezda |
| song | pesma / песма | pjesma |
| place | mesto / место | mjesto |
| beautiful | lep / леп | lijep |
| bread (formal poetic) | hleb / хлеб | hljeb |
| arrow | strela / стрела | strijela |
| left | levi / леви | lijevi |
| measure | mera / мера | mjera |
| change (n.) | promena / промена | promjena |
| section | odeljak / одељак | odjeljak |

### 4. Seven-case system (severity 2.5)

Serbian uses **all 7 Slavic cases**, including the vocative (used for direct address — `korisniče!` "user!"). Every noun, adjective, and pronoun declines.

| Case | Question | Use | Example (m. sg. "korisnik" — user) | Example (f. sg. "datoteka" — file) |
|------|----------|-----|------------------------------------|-------------------------------------|
| Nominativ (NOM) | ko? šta? | Subject | korisnik | datoteka |
| Genitiv (GEN) | koga? čega? | Possession, "of", absence, 5+ count | korisnika | datoteke |
| Dativ (DAT) | kome? čemu? | Indirect object, "to" | korisniku | datoteci |
| Akuzativ (ACC) | koga? šta? | Direct object | korisnika (animate=GEN) / sistem (inanimate=NOM) | datoteku |
| Vokativ (VOC) | — | Direct address | korisniče! | datoteko! |
| Instrumental (INS) | s kim? čim? | "With", means | korisnikom | datotekom |
| Lokativ (LOC) | o kome? čemu? | Location (always w/ prep) | korisniku (o korisniku) | datoteci (o datoteci) |

**Critical: animate masculine accusative = genitive form.** `vidim korisnika` ("I see [the] user"), NOT `vidim korisnik`. Inanimate masculines keep ACC = NOM: `vidim sistem`.

### 5. Preposition + governed case (severity 2.5)

| Preposition | Case | Example |
|-------------|------|---------|
| u (in/into) | LOC (location) / ACC (motion) | u sistemu (in system) / u sistem (into system) |
| na (on/onto) | LOC / ACC | na ekranu (on screen) / na ekran (onto screen) |
| s / sa (with) | INS | s korisnikom, sa Vama |
| bez (without) | GEN | bez sistema, bez greške |
| za (for) | ACC | za korisnika, za sistem |
| od (from) | GEN | od korisnika |
| do (until/to) | GEN | do kraja |
| iz (out of) | GEN | iz mape |
| o (about) | LOC | o korisniku, o sistemu |
| po (per / along) | LOC | po korisniku, po datoteci |
| pre (before) | GEN | pre vremena |
| posle (after) | GEN | posle prijave |
| prema (toward) | DAT | prema korisniku |
| sa (down from) | GEN | sa stranice (depending on sense; sa = with takes INS) |
| kroz (through) | ACC | kroz aplikaciju |

`po` for "per" with rate: `po datoteci` (per file), `po korisniku` (per user), `dnevno` / `na dan` (per day).

### 6. ICU plurals — one / few / other (1 / 2-4 / 5+ pattern) (severity 2.5)

```icu
{count, plural,
  one {# datoteka}
  few {# datoteke}
  other {# datoteka}
}
```

**CLDR plural category boundaries** (memorize):

| Category | Rule | Examples | Noun form |
|----------|------|----------|-----------|
| `one` | n % 10 = 1, n % 100 ≠ 11 | 1, 21, 31, 41, 101, 121 | **NOM singular** (datoteka) |
| `few` | n % 10 ∈ {2,3,4}, n % 100 ∉ {12,13,14} | 2, 3, 4, 22, 23, 24, 102, 103 | **GEN singular** (datoteke) |
| `other` | everything else | 0, 5-20, 25-30, 100, 1000 | **GEN plural** (datoteka) |

**Critical:** 11/12/13/14 use `other` (they are exceptions to the otherwise simple "ends in 1/2-4" pattern). Same for 111, 112, 113, 114. This is identical to Russian but different from Croatian (some details vary).

### 7. Numeral-noun agreement (severity 2.0)

The plural-form rule manifests directly in number constructions:

| Count | Pattern | Example |
|-------|---------|---------|
| 1 | NOM sg | 1 datoteka, 1 korisnik, 1 sistem |
| 2, 3, 4 | GEN sg | 2 datoteke, 3 korisnika, 4 sistema |
| 5+ | GEN pl | 5 datoteka, 10 korisnika, 20 sistema |
| 11-14 | GEN pl (exception) | 11 datoteka (NOT datoteke), 12 sistema |
| 21 | NOM sg (back to "one") | 21 datoteka |
| 22-24 | GEN sg | 22 datoteke |
| 25+ | GEN pl | 25 datoteka |

### 8. Verb aspect — perfective vs imperfective (severity 2.0)

Every Serbian verb has aspect — most concepts have a perfective/imperfective **pair**. Choosing the wrong aspect changes meaning from "doing X" to "having done X" (or vice versa).

| Imperfective (process, ongoing) | Perfective (single completed event) | English |
|--------------------------------|--------------------------------------|---------|
| čuvati | sačuvati | save |
| brisati | obrisati | delete |
| otpremati | otpremiti | upload |
| preuzimati | preuzeti | download |
| otvarati | otvoriti | open |
| zatvarati | zatvoriti | close |
| stvarati | stvoriti / napraviti | create |
| uređivati | urediti | edit |
| menjati | promeniti | change |
| pisati | napisati | write |
| čitati | pročitati | read |
| slati | poslati | send |
| birati | izabrati | choose / select |
| prijavljivati se | prijaviti se | log in (process / single act) |

**UI patterns by aspect:**

- **Buttons (single action)** → **perfective imperative**: `Sačuvaj`, `Obriši`, `Pošalji`, `Izaberi`. (NOT `Čuvaj`, which implies "keep saving repeatedly".)
- **Ongoing status messages** → **imperfective verbal noun + …**: `Čuvanje…`, `Otpremanje…`, `Učitavanje…`, `Slanje…`.
- **Completed status** → **perfective past participle** + **je**: `Datoteka je sačuvana`, `Otpremanje je završeno`.
- **Failed status** → **perfective past + nije**: `Otpremanje nije uspelo`, `Datoteka nije sačuvana`.

### 9. Clitic second-position rule (Wackernagel's law) (severity 2.0)

Serbian clitics (`je`, `se`, `mi`, `ti`, `mu`, `joj`, `nam`, `vam`, `im`, `bi`, `li`) MUST go in the **second position** of their clause (after the first stressed word).

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| `Se meni to ne sviđa` | **`To mi se ne sviđa`** (clitics in 2nd position) |
| `Datoteka se mu prikazuje` | **`Datoteka mu se prikazuje`** (dative `mu` before reflexive `se`) |
| `Mi se to dopada` (in narrative) | **`Meni se to dopada`** (when emphatic, use full pronoun) |

**Clitic order within the cluster** (when multiple clitics stack):
1. `li` (question particle)
2. AUX `je/sam/si/smo/ste/su/bi/bih`
3. DAT (`mi/ti/mu/joj/nam/vam/im`)
4. ACC (`me/te/ga/je/nas/vas/ih`)
5. Reflexive `se`

Example: `Da li mu se to dopada?` (Q-AUX-DAT-REFL — does he like it?)

### 10. Three-gender adjective agreement (severity 2.0)

| Gender | Indef. example | Adjective ending (sg.) |
|--------|---------------|------------------------|
| Masculine (consonant ending) | sistem | novi sistem (anim/inanim sg. NOM same) |
| Feminine (-a ending) | aplikacija | nova aplikacija |
| Neuter (-o/-e ending) | podešavanje | novo podešavanje |

Wrong gender adjective is auto-fail: `nova sistem` ✗, `novi aplikacija` ✗.

### 11. Past-tense gender agreement (severity 1.5)

Past tense in Serbian = AUX (`sam/si/je/smo/ste/su`) + L-participle, which agrees with subject in gender + number:

| Subject | L-participle | Example |
|---------|--------------|---------|
| m. sg. | -o | on je radio (he worked) |
| f. sg. | -la | ona je radila (she worked) |
| n. sg. | -lo | ono je radilo (it worked) |
| m. pl. | -li | oni su radili |
| f. pl. | -le | one su radile |
| n. pl. | -la | ona su radila |

`ona je radio` ✗ (gender mismatch) → `ona je radila` ✓.

### 12. Verb-construction integrity — no stacked finite verbs (severity 2.0)

English `-ing` forms (gerund as adverbial: "I spent 6 years building...") MUST be rendered with **glagolski prilog sadašnji** (verbal adverb, -ći form), NOT with a second finite clause stacked on the first.

| ✗ Stacked finite | ✓ Verbal adverb (-ći) | English |
|------------------|------------------------|---------|
| `Proveo sam 6 godina gradio sam posao` | **`Proveo sam 6 godina gradeći posao`** | I spent 6 years building the business |
| `Radio sam dok sam pisao izveštaj` | **`Radio sam pišući izveštaj`** | I worked while writing the report |
| `Provela je vreme čekala je rezultate` | **`Provela je vreme čekajući rezultate`** | She spent time waiting for results |

**Common -ći forms (imperfective verbs only):**

| Infinitive | -ći form | English |
|------------|----------|---------|
| čekati | čekajući | waiting |
| pisati | pišući | writing |
| graditi | gradeći | building |
| čitati | čitajući | reading |
| razmišljati | razmišljajući | thinking |
| koristiti | koristeći | using |
| dolaziti | dolazeći | coming |
| radeći | radeći | working |
| govoreći | govoreći | speaking |

**Also flag verb-root monotony**: if the same root appears 3+ times in one string (`radi na radu radnog procesa`), restructure with synonyms (`obavlja posao`, `razvija radni proces`).

### 13. Diacritics — Č Ć Ž Š Đ are essential (severity 2.5)

In Latin script, never strip diacritics. `Sacuvaj` for `Sačuvaj`, `Obrisi` for `Obriši`, `Sifra` for `Šifra` is broken text. Some legacy SMS-era systems stripped them; modern UI does not.

In Cyrillic this is a non-issue (the script doesn't use Latin diacritics).

---

## Pronouns and Possessives

### Personal pronouns

| English | Latin | Cyrillic | Notes |
|---------|-------|----------|-------|
| I | ja | ја | |
| you (sg. informal) | ti | ти | |
| you (sg./pl. formal — capitalize) | Vi | Ви | Always capitalized in direct address |
| you (pl. informal) | vi | ви | lowercase when truly plural informal |
| he | on | он | |
| she | ona | она | |
| it | ono | оно | |
| we | mi | ми | |
| they (m./mixed) | oni | они | |
| they (f.) | one | оне | |
| they (n.) | ona | она | |

### Possessive pronouns (agree with possessed noun's gender/number/case)

| Person | m. sg. | f. sg. | n. sg. | pl. (all) |
|--------|--------|--------|--------|-----------|
| moj (my) | moj | moja | moje | moji/moje/moja |
| tvoj (your sg. informal) | tvoj | tvoja | tvoje | tvoji/tvoje/tvoja |
| **Vaš (your formal — capitalize)** | **Vaš** | **Vaša** | **Vaše** | **Vaši/Vaše/Vaša** |
| njegov (his) | njegov | njegova | njegovo | njegovi/njegove/njegova |
| njen (her) | njen | njena | njeno | njeni/njene/njena |
| svoj (reflexive — own) | svoj | svoja | svoje | svoji/svoje/svoja |
| naš (our) | naš | naša | naše | naši/naše/naša |
| njihov (their) | njihov | njihova | njihovo | njihovi/njihove/njihova |

**Reflexive `svoj`**: used when possessor = subject of same clause.
- `On čuva svoj fajl.` (He saves his own file.) ← reflexive
- `On čuva njegov fajl.` (He saves someone else's file.) ← non-reflexive — different referent

---

## UI Conventions

### Buttons — IMPERATIVE (perfective for single action)

Single-word action buttons take the **imperative** — informal `Sačuvaj` / formal `Sačuvajte`. NEVER infinitive (`Sačuvati`) — that reads as an instruction manual.

Both informal (ti) and formal (Vi) forms shown; pick one per project and stay consistent.

| English | ti (informal) | Vi (formal) |
|---------|---------------|-------------|
| Save | **Sačuvaj** | **Sačuvajte** |
| Cancel | **Otkaži** | **Otkažite** |
| Delete | **Obriši** | **Obrišite** |
| Send | **Pošalji** | **Pošaljite** |
| Edit | **Izmeni** | **Izmenite** |
| Search | **Pretraži** | **Pretražite** |
| Confirm | **Potvrdi** | **Potvrdite** |
| Continue | **Nastavi** | **Nastavite** |
| Submit | **Pošalji** | **Pošaljite** |
| Sign in | **Prijavi se** | **Prijavite se** |
| Sign out | **Odjavi se** | **Odjavite se** |
| Sign up | **Registruj se** | **Registrujte se** |
| Next | **Sledeće** | (same) |
| Back | **Nazad** | (same) |
| Done | **Gotovo** / **Završeno** | (same) |
| OK | **U redu** / **OK** | (same) |
| Close | **Zatvori** | **Zatvorite** |
| Upload | **Otpremi** | **Otpremite** |
| Download | **Preuzmi** | **Preuzmite** |
| Refresh | **Osveži** | **Osvežite** |
| Settings | **Podešavanja** | (same) |
| Apply | **Primeni** | **Primenite** |
| Reset | **Vrati na podrazumevano** / **Resetuj** | **Resetujte** |
| Select all | **Izaberi sve** | **Izaberite sve** |
| Deselect all | **Poništi sve** | **Poništite sve** |
| Add more | **Dodaj još** (NOT `Dodaj više`) | **Dodajte još** |
| Show more | **Prikaži još** | **Prikažite još** |

**Tabs and navigation labels also use imperative**, not infinitive:
- ✗ `Otpremiti datoteke` (inf., instruction-manual tone)
- ✓ `Otpremite datoteke` (Vi imp.) / `Otpremi datoteke` (ti imp.)

### Status messages — three distinct patterns

**Ongoing (in-flight)** → **imperfective verbal noun + …**

| English | Serbian |
|---------|---------|
| Loading… | **Učitavanje…** |
| Saving… | **Čuvanje…** |
| Sending… | **Slanje…** |
| Uploading… | **Otpremanje…** |
| Downloading… | **Preuzimanje…** |
| Translating… | **Prevođenje…** |
| Connecting… | **Povezivanje…** |
| Processing… | **Obrada…** |
| Searching… | **Pretraga…** |
| Please wait | **Sačekajte, molim Vas** / **Molimo sačekajte** |

**Completed** → **Subject + je + perfective past participle** (full construction with auxiliary `je`)

| English | Serbian |
|---------|---------|
| Saved | **Sačuvano** (n. participle, subject-less) / **Datoteka je sačuvana** |
| Done | **Gotovo** / **Završeno** |
| Translation complete | **Prevod je završen** |
| File uploaded | **Datoteka je otpremljena** |
| Payment successful | **Plaćanje je uspelo** / **Uspešno plaćanje** |
| Sent | **Poslato** / **Poruka je poslata** |

**Critical**: NEVER drop the `je` auxiliary in completion messages. `Prevod završen` ✗ (sounds incomplete) → `Prevod je završen` ✓.

**Failed** → **Subject + nije + perfective past participle**

| English | Serbian |
|---------|---------|
| Save failed | **Čuvanje nije uspelo** |
| Upload failed | **Otpremanje nije uspelo** |
| Translation failed | **Prevod nije uspeo** |
| Connection failed | **Povezivanje nije uspelo** |
| File not found | **Datoteka nije pronađena** |

NEVER use short forms like `Prevod neuspeo` — they sound unnatural and bureaucratic.

**Validation / field errors** → nominal description

| English | Serbian |
|---------|---------|
| This field is required | **Ovo polje je obavezno** |
| Invalid format | **Neispravan format** |
| Password too short | **Lozinka je prekratka** |
| Email already in use | **Imejl adresa je već u upotrebi** |

**Action instructions** → imperative

| English | Serbian |
|---------|---------|
| Enter your password | **Unesite Vašu lozinku** (Vi) / **Unesi lozinku** (ti) |
| Choose at least one language | **Izaberite najmanje jedan jezik** |
| Try again | **Pokušajte ponovo** |

### Empty states — `Nema X` / `Nije pronađeno`

| ✗ Bare | ✓ Specific |
|--------|-----------|
| Prazno | **Nema rezultata** / **Nema pronađenih stavki** |
| Ništa ovde | **Nema datoteka** / **Nema dostupnih podataka** |
| Bez podataka | **Nema dostupnih podataka** |
| Lista je prazna | **Nema stavki na listi** |

### Drag-and-drop

- drag → **prevucite** (Vi) / **prevuci** (ti)
- drop (= place files) → **pustite** (Vi) / **pusti** (ti) — NOT `ispustite` (= accidentally drop)
- release → **otpustite** (Vi) / **otpusti** (ti)
- Combined: **`Prevucite datoteke ovde`** (Drag files here) / **`Pustite za otpremanje`** (Release to upload).

`Ispustite svoje datoteke` ✗ (literal "drop your files [by accident]") → `Prevucite svoje datoteke ovde` ✓.

### File picker — `Izaberi` not `Pregledaj`

| ✗ Older / navigation-oriented | ✓ Modern / action-oriented |
|-------------------------------|-----------------------------|
| Pregledaj datoteke | **Izaberi datoteke** (ti) / **Izaberite datoteke** (Vi) |
| Klikni za pregled | **Klikni za izbor** / **Kliknite za izbor** |
| Za pregledanje datoteka | **Za izbor datoteka** |

### Quantity expressions

| ✗ Calque | ✓ Native |
|----------|----------|
| 25+ jezika | **više od 25 jezika** |
| +{count} više | **i {count} drugih** / **još {count}** |
| +25 funkcija | **preko 25 funkcija** / **više od 25 funkcija** |

`Dodaj više` ✗ (literal "add more") → `Dodaj još` ✓ (idiomatic "add more").

### Error messages — what + next step

| ✗ Bare | ✓ With next step |
|--------|------------------|
| Datoteka nije pronađena. | **Datoteka nije pronađena. Proverite putanju.** |
| Greška mreže. | **Greška mreže. Pokušajte ponovo.** |
| Neispravan imejl. | **Imejl adresa nije ispravna. Proverite format.** |
| Prijava nije uspela. | **Prijava nije uspela. Proverite korisničko ime i lozinku.** |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Serbian | Notes |
|------|---------|-------|
| Question mark | `?` | Same as English |
| Comma | `,` | Different conjunction rules (see below) |
| Period | `.` | Same |
| Colon | `:` | Same |
| Quotation marks | **„…"** (German-style: low opening, high closing) — preferred | OR `"…"` Latin straight quotes; `«…»` rarely used |
| Nested quotes | `'…'` | Single quotes inside primary |
| Apostrophe | only in foreign names | Possessive uses `-ov/-ev` or genitive, not English-style `'s` |

**Quote style:** `Klikni na dugme „Sačuvaj"` (low-9 opening, high-9 closing). NOT `"Sačuvaj"` (English style) or `«Sačuvaj»` (French/Russian style) in formal Serbian text.

### Comma rules

| Rule | Example |
|------|---------|
| **NO comma** before `i` (and) | Prevucite ovde **i** kliknite. |
| **NO comma** before `ili` (or) | Prevucite ovde **ili** kliknite. |
| **NO comma** before `niti` (nor) | Niti znam **niti** mi je važno. |
| **Comma** before `da` (that, subordinating) | Vidim, **da** je datoteka otvorena. |
| **Comma** before `koji/koja/koje` (relative) | Datoteka, **koja** je sačuvana… |
| **Comma** before `ako` (if) | Sačuvajte, **ako** želite. |
| **Comma** before `jer` (because) | Otkazano, **jer** nije uspelo. |
| **Comma** before `ali` (but) | Brzo, **ali** efikasno. |
| **Comma** before `a` (and/but contrast) | Ja sam pisao, **a** ti si čekao. |

### Numbers

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **period (.)** | 1.234.567 |
| Decimal separator | **comma (,)** | 3,14 / 99,99 |
| Negative | `-25` | |
| Percent | `25%` (no space typical) | |

**Critical:** Serbian uses **period for thousands, comma for decimal** — opposite of English. `1,234.56` is wrong; write `1.234,56`.

### Dates

| Format | Example | Use |
|--------|---------|-----|
| D. M. YYYY. | **15. 1. 2024.** | Default — note the period AFTER the year |
| D. mesec YYYY. | **15. januar 2024.** | Long-form prose |
| D. mesec YYYY. godine | **15. januar 2024. godine** | Formal documents |
| YYYY-MM-DD | 2024-01-15 | Technical/API only |

**Month names (lowercase always, no period for full names):**

| 1 | januar | 7 | jul |
| 2 | februar | 8 | avgust |
| 3 | mart | 9 | septembar |
| 4 | april | 10 | oktobar |
| 5 | maj | 11 | novembar |
| 6 | jun | 12 | decembar |

(These are the Serbian months — note `jul/avgust` vs Croatian `srpanj/kolovoz`.)

**Weekdays (lowercase):** ponedeljak, utorak, sreda, četvrtak, petak, subota, **nedelja** (NOT Croatian `nedjelja` ijekavian).

Week starts **Monday**.

### Time

- 24-hour preferred: `14:30` or `14.30` (period acceptable as separator).
- 12-hour rarely used.

### Currency — Serbian Dinar (RSD)

| Format | Pattern | Example |
|--------|---------|---------|
| Local symbol | `din.` after amount | **99,99 din.** |
| ISO code | RSD before/after | **99,99 RSD** / **RSD 99,99** |

For EUR (sometimes shown for context in Serbia): `99,99 €` or `99,99 EUR`.

Never `$99.99` in Serbian UI — currency-symbol-before-amount with period decimal is American English style.

---

## Terminology — preferred Serbian terms (with notes on established loanwords)

Serbian has a more relaxed attitude toward IT loanwords than Croatian — many Latinized terms (`klipbord`, `imejl`, `link`, `onlajn`) are fully established. Croatian "purist" terms (`međumemorija`, `e-pošta`, `poveznica`, `na mreži`) sound either foreign-Croatian or overly formal in Serbian.

| English | ✓ Serbian preferred | ✗ Avoid |
|---------|---------------------|---------|
| user | korisnik | user |
| account | nalog | akaunt |
| password | lozinka / šifra | password |
| settings | podešavanja | setings |
| dashboard | kontrolna tabla | dashboard |
| email | **imejl** | e-pošta (Croatian-leaning), mejl |
| link | **link** | veza (overly formal) |
| website | sajt / veb-sajt | website |
| folder | **fascikla** (formal) / **folder** (informal) | — |
| file | **datoteka** (formal) / **fajl** (informal) | — |
| device | uređaj | device |
| phone | telefon | — |
| computer | **računar** | kompjuter |
| application / app | aplikacija | aplikejšn |
| update (v.) | ažurirati / nadograditi | apdejtovati (informal) |
| save | sačuvati | sejvovati |
| delete | obrisati / izbrisati | deletovati |
| upload | **otpremiti** | uploadovati (informal but acceptable in casual) |
| download | **preuzeti** | downloadovati (informal but acceptable) |
| sign in / log in | prijaviti se | login-ovati se |
| sign up / register | registrovati se | — |
| search | pretraga / pretraživati | — |
| click | kliknuti / klikni | — |
| share | podeliti / deli | šerovati (informal) |
| profile | profil | — |
| notifications | obaveštenja | notifikacije (acceptable) |
| privacy | privatnost | — |
| terms | uslovi | — |
| support | podrška | — |
| help | pomoć | — |
| feedback | povratne informacije / fidbek (informal) | — |
| menu | meni | — |
| home | početna | — |
| logout | odjaviti se | logout-ovati se |
| **clipboard** | **klipbord** | međumemorija (Croatian purist) |
| **online** | **onlajn** | na mreži (Croatian purist) |
| **offline** | **oflajn** | van mreže (Croatian purist) |
| detection (in UI) | otkrivanje | detekcija (technical OK) |
| validation (in UI) | provera | validacija (technical OK) |
| configuration (in UI) | podešavanje | konfiguracija (technical OK) |
| build (software) | napraviti / razviti / build (keep in code contexts) | graditi (= construction) |
| deploy | postaviti / izdati / objaviti / deploy-ovati (informal) | — |
| pipeline (CI/CD) | pipeline (keep) / procesna linija | cevovod (= literal pipe) |
| commit (git) | commit (keep) / sačuvati izmene | — |
| merge (git) | spojiti / merge (keep in code) | — |
| repository | repozitorijum | — |
| branch (git) | grana / branch (keep) | — |
| API | API (keep — Latin always) | — |
| endpoint | endpoint (keep) / krajnja tačka | — |
| token | token (keep) | — |
| cache | keš (memorija) | — |
| log (n.) | dnevnik / log | — |
| sync | sinhronizacija / sinhronizovati | — |
| webhook | webhook (keep) | — |
| source of truth | izvor istine / kanonski izvor | — |

### Technical identifiers — keep in Latin script even inside Cyrillic text

This is the **only legitimate script-mixing case**. Inside Cyrillic Serbian text, the following ALWAYS stay in Latin:

- Programming languages: Python, JavaScript, Go, Rust, Java
- Frameworks: React, Vue, Angular, Next.js, Django
- Tools: Git, GitHub, GitLab, Docker, npm, pip, cargo
- Protocols: HTTP, HTTPS, FTP, SSH, TCP, REST, GraphQL, OAuth, JWT
- File formats: JSON, XML, YAML, CSV, PDF, MP4
- Brands: Google, Microsoft, Apple, AWS, iPhone, Android
- Commands, file paths, URLs, code snippets
- Placeholders: `{variableName}`, `{{count}}`, `<tag>`

✓ Correct: `Git репозиторијум је синхронизован.` (Cyrillic prose, Latin `Git`)
✓ Correct: `API кључ је неисправан.` (Cyrillic prose, Latin `API`)
✓ Correct: `Подаци у JSON формату.` (Cyrillic prose, Latin `JSON`)
✗ Wrong: `Гит репозиторијум је синхронизован.` (transliterating `Git` to Cyrillic)
✗ Wrong: `АПИ кључ` (transliterating `API`)
✗ Wrong: `ЈСОН формат` (transliterating `JSON`)

---

## False Friends — Critical

| Serbian word | Actually means | NOT this (common AI error) | Correct for the English |
|--------------|----------------|-----------------------------|--------------------------|
| aktuelan | current / topical | "actual" | "actual" → **stvaran / pravi** |
| realizovati | to implement / carry out | "to realize (understand)" | "realize (understand)" → **shvatiti** |
| eventualno | possibly | "eventually" | "eventually" → **na kraju** / **konačno** |
| uzbuđen | excited (sometimes ambiguous, can be sexual) | safer "excited" | "excited (looking forward)" → **radujem se** / **uzbudljiv** for adj. |
| sympatičan | likeable / pleasant | "sympathetic (compassionate)" | "sympathetic" → **saosećajan** |
| simpatija | a crush / affection | "sympathy (condolence)" | "sympathy" → **saučešće** |
| transparentan | clear / see-through | (mostly OK) | political "transparent" also `transparentan` is OK |
| receptura | recipe (formal) | "receipt" | "receipt" → **račun** / **priznanica** |
| dirigovati | to conduct (music) | "to direct (manage)" | "direct (manage)" → **upravljati** / **rukovoditi** |
| inženjering | engineering | (OK) | — |
| efektan | effective in producing visual effect | "effective" | "effective" → **delotvoran** / **efikasan** |

---

## Calque / Anti-Pattern List

| ✗ Calque | ✓ Native | Reason |
|----------|----------|--------|
| **Auto-otkriveno / Auto-sačuvaj** | **Automatski otkriveno / Automatski sačuvaj** | "Auto-X" — use full adjective form |
| **Prevedeni rezultati** (as header) | **Rezultati prevođenja** | English Past-Participle + Noun → Serbian Noun + Genitive verbal noun |
| **Otpremljeni fajlovi** (as header) | **Datoteke za otpremanje** | Same pattern; or use noun for purpose |
| **Izabrane opcije** (as header) | **Izbor opcija** | Same pattern; use noun form |
| **opcija jezika** (noun + noun) | **jezičke opcije** / **izbor jezika** | English N+N → Serbian adj+N or genitive |
| **projekat folder** | **folder projekta** / **projektni folder** | English N+N → Serbian genitive or adjective |
| **korisnik podešavanja** | **korisnička podešavanja** | English N+N → Serbian adjective |
| **preference tona** | **željeni ton** / **izbor tona** | Anglicism noun → native adjective + noun |
| **praviti smisao** | **imati smisla** | "Makes sense" calque |
| **na kraju dana** | **na kraju krajeva** | "At the end of the day" calque |
| **uzeti mesto** | **održati se** | "Take place" calque |
| **bazirano na** | **na osnovu** | "Based on" calque; use native preposition |
| **u redu da** | **da bi** / **kako bi** | "In order to" calque |
| **na dnevnoj bazi / nedeljnoj bazi** | **svakodnevno** / **dnevno** / **nedeljno** | "On a daily/weekly basis" calque; use adverb |
| **u smislu (overused)** | **što se tiče** / **u pogledu** | "In terms of" calque |
| **izvršiti poboljšanje** | **poboljšati** | "Make improvements" — use direct verb |
| **pružiti odgovor** | **odgovoriti** | "Provide an answer" — use verb |
| **izvršiti izbor** | **izabrati** | "Make a selection" — use verb |
| **Nulti zastoj / Nula zastoja** | **Bez zastoja** / **Bez grešaka** | "Zero X" English marketing calque |
| **AI-pokretan** | **zasnovan na AI** / **uz pomoć AI** | "X-powered" calque |
| **podaci-orijentisan** | **orijentisan na podatke** / **zasnovan na podacima** | "X-driven" calque |
| **pretpostavka-prijateljski** | **korisnički prilagođen** / **lako za korišćenje** | "user-friendly" calque |
| **Sjedinjene Američke Države** | **SAD** | UI short form |
| **Ujedinjeno Kraljevstvo Velike Britanije** | **Velika Britanija** / **UK** | UI short form |
| **[Subject] je potreban za [Purpose]** | **Potreban je [Subject] za [Purpose]** | English subject-first → Serbian verb-first |
| **Dragujte** / **Drag-ujte** | **Prevucite** | English verb → native |
| **Ispustite datoteke ovde** | **Prevucite datoteke ovde** / **Pustite za otpremanje** | "ispustite" = accidentally drop; use idiomatic phrasing |
| **Prevod neuspeo / Plaćanje neuspelo** | **Prevod nije uspeo** / **Plaćanje nije uspelo** | Missing auxiliary — sounds incomplete |
| **Prevod završen** (no je) | **Prevod je završen** | Missing auxiliary in completion message |
| **Poništi izbor svega** | **Poništi sve** | Button brevity |
| **Izaberi izbor svih** | **Izaberi sve** | Button brevity / redundancy |
| **Dodaj više** | **Dodaj još** | "Add more" — use idiomatic `još` |
| **per datoteka** | **po datoteci** | "per X" → `po` + locative |

### Past Participle + Noun → Noun + Genitive (header pattern)

This is a uniquely Serbian-natural restructure. English likes adjectival past participles in headers; Serbian prefers nominalization.

| English | ✗ Calque (Participle + N) | ✓ Native (N + Genitive of verbal noun) |
|---------|----------------------------|-----------------------------------------|
| Translated Results | Prevedeni rezultati | **Rezultati prevođenja** |
| Selected Options | Izabrane opcije | **Izbor opcija** |
| Uploaded Files | Otpremljeni fajlovi | **Otpremljene datoteke** (when finished, OK) / **Datoteke za otpremanje** (when pending) |
| Saved Items | Sačuvane stavke | **Sačuvane stavke** (OK as result), or **Lista sačuvanog** |

---

## Custom Sections

### Verbification suffixes are VALID — don't over-correct

Serbian forms verbs from English loans via `-ovati` / `-irati` suffixes. These are **legitimate** Serbian verbs once formed:

| English | Serbian verbified | Status |
|---------|---------------------|--------|
| upload | uploadovati / otpremiti | both OK; native `otpremiti` preferred |
| download | downloadovati / preuzeti | native preferred |
| install | instalirati | fully naturalized, no native alternative needed |
| log in | ulogovati se / prijaviti se | native `prijaviti se` preferred for UI |
| post | postovati | acceptable; native `objaviti` preferred in formal contexts |
| share | šerovati / podeliti | native `podeliti` preferred |
| like (social) | lajkovati | fully accepted in social-media contexts |
| sync | sinhronizovati | fully naturalized |
| reset | resetovati | fully naturalized |
| commit (git) | commit-ovati / sačuvati izmene | code-context only |

Don't flag `instalirati` or `sinhronizovati` as errors — they're standard. The flag is for **hybrid forms with native verbs already available**: `čistati` (no, use `čistiti`), `sejvovati` (no, use `sačuvati`), `deletovati` (no, use `obrisati`).

### Per vs for — CRITICAL semantic distinction

| Source | ✓ Serbian | Meaning |
|--------|-----------|---------|
| per language (rate) | **po jeziku** (loc.) | rate, per-unit |
| for 25 languages (total) | **za 25 jezika** (acc.) | total scope |
| 5 USD per language | **5 USD po jeziku** | rate |
| 5 USD for all languages | **5 USD za sve jezike** | total |

Mixing these in pricing copy is auto-fail.

### Cost / estimate ordering

Prefer amount-first:

| ✗ Ambiguous | ✓ Clear |
|-------------|---------|
| 5 jezika 25 kredita | **25 kredita za 5 jezika** |
| 5 jezika: 25 kredita | (acceptable variant) |

### UI element references in prose

Use quotation marks for specific UI labels:

| ✗ Compound | ✓ Quoted label |
|------------|----------------|
| Kliknite Sačuvaj-dugme | **Kliknite na dugme „Sačuvaj"** |
| Otvorite Podešavanja-karticu | **Otvorite karticu „Podešavanja"** |
| Koristite Ime-polje | **Koristite polje „Ime"** |

### Brand names + Serbian declension

Foreign brand names CAN be declined Serbian-style with a hyphen + Serbian ending (informal), OR stay invariant (formal/UI default):

- `Google` → `Google-a` (gen.), `Google-u` (loc.), `Google-om` (ins.) — informal/conversational
- For formal UI, prefer prepositional phrases: `na Google-u` or restructure to keep brand invariant: `na platformi Google`.
- `iPhone` → `iPhone-a`, `iPhone-u` (gen. / loc.)
- `GitHub` → `GitHub-a`, `GitHub-u`

### "Da + present" as alternative to infinitive

A natural Serbian feature — `da + present-tense` often replaces the infinitive, sounding more conversational:

| ✗ Stiff infinitive | ✓ Natural `da + present` |
|--------------------|--------------------------|
| Želim sačuvati datoteku | **Želim da sačuvam datoteku** |
| Moram napisati izveštaj | **Moram da napišem izveštaj** |
| Mogu pomoći | **Mogu da pomognem** |

Both are grammatical. `Da + present` is preferred in modern Serbian especially in spoken / informal / UI contexts. Use infinitive sparingly (formal/legal).

---

## Self-Check Checklist (Run Before Returning Output)

### Script (auto-fail on miss)

- [ ] **One script throughout** — never Cyrillic mixed with Latin within a single string (or set of related strings for the same locale).
- [ ] **Latin technical identifiers** preserved inside Cyrillic text (Git, API, JSON, npm, URLs, `{var}`).
- [ ] **Diacritics intact** in Latin: Č, Ć, Ž, Š, Đ never stripped.
- [ ] **Digraphs correct** when converting: Љ↔Lj, Њ↔Nj, Џ↔Dž (case-aware).

### Accuracy

- [ ] **Ekavian forms** — `vreme/lepo/mleko/dete/reka` (NEVER `vrijeme/lijepo/mlijeko/dijete/rijeka`).
- [ ] **Word integrity** — prefixes joined (`prevesti`, `izvršiti`, `sačuvati`), no spaces. Reflexive `se` separate (`prijavi se`, `registruj se`).
- [ ] **Gender agreement** on every noun-adj pair (novi sistem / nova aplikacija / novo podešavanje).
- [ ] **Seven cases** correct, especially:
  - Animate masc. accusative = genitive (`vidim korisnika`).
  - Instrumental after `s/sa` (`s korisnikom`, `sa Vama`).
  - Locative after `u/na/o/po` (`u sistemu`, `o korisniku`, `po datoteci`).
  - Genitive after `bez/od/do/iz/pre/posle` (`bez sistema`).
- [ ] **ICU plurals**: `one` / `few` / `other` categories present (1 = nom.sg, 2-4 = gen.sg, 5+ = gen.pl).
- [ ] **Numeral-noun agreement** matches plural-form pattern.
- [ ] **Verb aspect** correct: perfective for completed (buttons, completion), imperfective for ongoing (status, process).
- [ ] **Clitics in 2nd position** (Wackernagel): `To mi se ne sviđa`, not `Se mi to ne sviđa`.
- [ ] **Clitic order**: li → AUX → DAT → ACC → se (`Da li mu se to dopada?`).
- [ ] **Past-tense gender agreement** on L-participle (radio/radila/radilo).
- [ ] **No stacked finite verbs** from English -ing — use `-ći` verbal adverb (gradeći, čekajući, pišući).
- [ ] **Placeholders preserved** (`{var}`, `{{count}}`, `<tag>`, URLs, code identifiers).
- [ ] **Numbers**: comma decimal (3,14), period thousands (1.234), `din.` after amount.
- [ ] **Dates**: D. M. YYYY. (with period after year), Serbian month names (januar, avgust — NOT siječanj, kolovoz).
- [ ] **Time**: 24-hour, `14:30` or `14.30`.
- [ ] **per vs za**: `po + LOC` for rate, `za + ACC` for total.

### Register

- [ ] **Vi/ti chosen and applied consistently** — pronouns, possessives, verb endings all match.
- [ ] **`Vi/Vaš/Vaša` capitalized** in direct second-person address.
- [ ] **No mixing** of Vi-form verb ending with ti-form possessive (or vice versa) within one text.

### UI conventions

- [ ] Buttons use **perfective imperative** (`Sačuvaj`/`Sačuvajte`), not infinitive (`Sačuvati`).
- [ ] Tabs/navigation also use imperative, not infinitive.
- [ ] Reflexive `se` present where required (`prijavi se`, `registruj se`).
- [ ] Status ongoing: **imperfective verbal noun + …** (`Učitavanje…`, `Slanje…`).
- [ ] Status completed: **Subject + je + perfective past participle** (`Prevod je završen`), not bare `Prevod završen`.
- [ ] Status failed: **Subject + nije + perfective past participle** (`Otpremanje nije uspelo`), not bare `Otpremanje neuspelo`.
- [ ] Empty state: `Nema X` / `Nije pronađeno` with specific noun.
- [ ] File picker: `Izaberi`, not `Pregledaj`.
- [ ] Drag-drop: `Prevucite`, `Pustite` (NOT `Ispustite`).
- [ ] Quantity: `više od 25`, `još {count}`, NOT `25+`, `+{count}`.
- [ ] Quotes: `„X"` low-9/high-9 style.

### Naturalness

- [ ] **Past Participle + Noun** headers → **Noun + Genitive of verbal noun** (`Rezultati prevođenja`, not `Prevedeni rezultati`).
- [ ] **Auto-X prefix** → full adjective `Automatski X`.
- [ ] **Marketing "Zero X"** → `Bez X`.
- [ ] **English N + N compounds** → Serbian adj + N or genitive (`jezičke opcije`, not `opcija jezika` calque; `željeni ton`, not `preference tona`).
- [ ] **No verbose collocations** (`izvršiti poboljšanje` → `poboljšati`; `pružiti odgovor` → `odgovoriti`).
- [ ] **No false friends**: `aktuelan ≠ actual`, `realizovati ≠ realize`, `eventualno ≠ eventually`.
- [ ] **No verb-root monotony** (same root 3+ times in one string).
- [ ] **No accidental Croatian forms** (no `tjedan`, `kruh`, `tko`, `što`, `siječanj`).
- [ ] **Proper-noun short forms**: `SAD`, `UK`, `EU`.
- [ ] **Established loanwords accepted**: `klipbord`, `link`, `imejl`, `onlajn` — don't over-purify with `međumemorija`, `e-pošta`, `na mreži`.

---

## Worked Example — Standard sr-Latn formal UI

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** neutral product UI, exclamation → **Vi (formal)**, neutral lexicon, Latin script (software default).

**Translation (sr-Latn):**

> Dobro došli nazad! Imate 3 nove datoteke na Vašem nalogu. Kliknite na **Nastavi** da ih pregledate ili **Otkaži** da ostanete ovde. Čuvanje Vaših izmena…

**Why this works:**
- `Dobro došli nazad` — standard greeting with plural participle (formal Vi → -i plural form).
- `Imate` — Vi-form verb (2nd person plural).
- `3 nove datoteke` — `3` triggers `few` (gen.sg.); `datoteka` is fem.; `nove` is fem. plural adjective in gen.sg. form (matches noun).
- `na Vašem nalogu` — `na` + LOC; `nalogu` is masc. LOC sg.; `Vašem` capitalized formal possessive in LOC.
- `Kliknite na Nastavi / Otkaži` — Vi imperative, button labels in perfective imperative themselves.
- `da ih pregledate` / `da ostanete ovde` — `da + present` construction (natural Serbian), `ih` is ACC pl. clitic ("them"), `pregledate` Vi-form perfective verb.
- `Čuvanje Vaših izmena…` — imperfective verbal noun for ongoing status; `Vaših izmena` gen.pl. (object of verbal noun).
- Punctuation: Latin `!`, `…` OK. No comma before `ili` (correct).
- No religious / cultural filler injected.

**Same string in sr-Cyrl:**

> Добро дошли назад! Имате 3 нове датотеке на Вашем налогу. Кликните на **Настави** да их прегледате или **Откажи** да останете овде. Чување Ваших измена…

(1:1 Cyrillic conversion. No content changes. `Lj/Nj/Dž` would need careful handling — but none in this sentence.)

**Same string informal (ti):**

> Dobro došao/došla nazad! Imaš 3 nove datoteke na svom nalogu. Klikni na **Nastavi** da ih pregledaš ili **Otkaži** da ostaneš ovde. Čuvanje tvojih izmena…

(Note `Dobro došao/došla` — past participle now agrees with addressee's gender; in real UI you'd pick one or use a gender-neutral phrasing.)

---

## Worked Example — ICU plural expansion

**Source:**

```icu
You have {count, plural, one {# new message} other {# new messages}}.
```

**Translation (full Serbian three-category expansion):**

```icu
Imate {count, plural,
  one {# novu poruku}
  few {# nove poruke}
  other {# novih poruka}
}.
```

Notes:
- `one`: `1 nova poruka` → in ACC (object of `Imate`), `1 novu poruku`. The form chosen here is direct accusative singular feminine.
- `few`: `2/3/4 nove poruke` — `nove` is f. pl. NOM/ACC (used as gen.sg. surface form here because of the 2-4 rule), `poruke` is f. gen.sg.
- `other`: `5+ novih poruka` — `novih` is f. gen.pl. adjective, `poruka` is f. gen.pl. noun.

(English source has only `one/other`; Serbian MUST expand to `one/few/other`.)

---

## Worked Example — Date and currency in both scripts

**Source:** Your subscription expires on January 15, 2024. Total: $99.99.

**sr-Latn:**

> Vaša pretplata ističe 15. januar 2024. Ukupno: 99,99 RSD.

**sr-Cyrl:**

> Ваша претплата истиче 15. јануар 2024. Укупно: 99,99 РСД.

(If RSD doesn't apply and the price is genuinely USD, keep `99,99 USD` or `99,99 $` after amount. Never `$99.99` in Serbian.)

---

## Worked Example — Verb-construction integrity (-ći)

**Source:** I spent 6 years building this business while learning from mistakes.

**✗ Wrong (stacked finite verbs):**

> Proveo sam 6 godina gradio sam ovaj posao dok sam učio iz grešaka.

**✓ Right (verbal adverb -ći for simultaneous actions):**

> Proveo sam 6 godina gradeći ovaj posao i učeći iz grešaka.

OR in Cyrillic:

> Провео сам 6 година градећи овај посао и учећи из грешака.

---

## When in Doubt

1. **Default to sr-Latn, Vi (formal), ekavian, single script throughout.**
2. If unsure about script → ask once; default Latin for software UI.
3. If a word looks ijekavian (`vrijeme`, `lijepo`, `mlijeko`, `dijete`) → **fix to ekavian** (`vreme`, `lepo`, `mleko`, `dete`).
4. If a word looks Croatian (`tjedan`, `siječanj`, `kruh`, `tko`, `što`) → **fix to Serbian** (`nedelja`, `januar`, `hleb`, `ko`, `šta`).
5. If a verb prefix has a space (`pre vesti`, `iz vršiti`) → **join it**: `prevesti`, `izvršiti`.
6. If `se` is attached to a verb (`prijavise`, `registrujse`) → **separate it**: `prijavi se`, `registruj se`.
7. If you wrote `Prevod završen` or `Otpremanje neuspelo` → **add the auxiliary**: `Prevod je završen`, `Otpremanje nije uspelo`.
8. If a string has both Cyrillic AND Latin (other than tech identifiers) → **pick one and convert the rest**.
9. If you used `infinitive + da` for a button → **switch to imperative**: `Sačuvati` ✗ → `Sačuvaj/Sačuvajte` ✓.
10. If you stacked two finite verbs from an English -ing construction → **rewrite with -ći** (gradeći, pišući, čekajući).
