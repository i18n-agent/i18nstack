---
name: localize-hr
description: "Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Croatian (hr). Enforces IJEKAVIAN forms (vrijeme, lijepo, mlijeko — NEVER Serbian ekavian), 7-case grammar, 3-gender agreement, ICU one/few/other plurals (1/2-4/5+ with 11-14 exception), perfective/imperfective verb aspect, Vi/ti formality consistency (Vaš capitalized), Latin script ONLY (Croatian never uses Cyrillic), Croatian-specific terminology (računalo, tipkovnica, zaslon, mapa) over Serbian/anglicism alternatives, clitic second-position (Wackernagel's law), verb-construction integrity with glagolski prilog sadašnji (-ći), and EUR currency since 2023 (formerly HRK)."
---

# Translate to Croatian (hr) — High-Fidelity Skill

## Scope & Variants

Croatian (`hr`) is a single standard written language using only **Latin script with Croatian diacritics** (Č Ć Đ Š Ž). Unlike Serbian, there is no Cyrillic variant — Croatian is Latin-only.

| Locale | Name | Notes |
|--------|------|-------|
| `hr` / `hr-HR` | Standard Croatian (Republic of Croatia) | Default and only meaningful variant for software |
| `hr-BA` | Croatian as used in Bosnia & Herzegovina | Practically identical to `hr` for product UI |

**Practical reality:** Croatian translation has essentially **one target**. There is no equivalent to the Spanish es-ES/es-419 split or the Norwegian Bokmål/Nynorsk split. Treat `hr` as the universal target.

### BCMS continuum — Croatian is NOT Serbian / Bosnian / Montenegrin

Croatian, Serbian, Bosnian, and Montenegrin are mutually intelligible South Slavic varieties — but they are **politically, orthographically, and lexically distinct languages** with their own ISO codes (`hr`, `sr`, `bs`, `cnr`). Mixing them is a critical failure.

**The biggest single tell that distinguishes Croatian from Serbian: ijekavian vs ekavian.**

| English | Croatian (ijekavian) ✓ | Serbian (ekavian) ✗ |
|---------|------------------------|----------------------|
| time | vrijeme | vreme |
| nice | lijepo | lepo |
| milk | mlijeko | mleko |
| child | dijete | dete |
| children | djeca | deca |
| river | rijeka | reka |
| world | svijet | svet |
| light | svjetlost | svetlost |
| flower | cvijet | cvet |
| star | zvijezda | zvezda |
| song | pjesma | pesma |
| place | mjesto | mesto |
| beautiful | lijep | lep |
| arrow | strijela | strela |
| left | lijevi | levi |
| measure | mjera | mera |
| change (n.) | promjena | promena |
| section | odjeljak | odeljak |

If any `vreme / lepo / mleko / dete / reka` slips into a Croatian translation, **fix it** — that's Serbian.

**Other Croatian-specific vocabulary** (where Serbian uses different roots):

| English | Croatian ✓ | Serbian (do not use in hr) |
|---------|-----------|-----------------------------|
| week | tjedan | nedelja (note: nedjelja in Croatian means "Sunday"!) |
| thousand | tisuća | hiljada |
| who | tko | ko |
| what | što | šta |
| football | nogomet | fudbal |
| bread | kruh | hleb |
| computer | računalo | računar |
| keyboard | tipkovnica | tastatura |
| screen | zaslon | ekran |
| browser | preglednik | pregledač |
| company | tvrtka (also poduzeće) | preduzeće / firma |
| office | ured | kancelarija |
| coffee | kava | kafa |
| airport | zračna luka | aerodrom |
| station | postaja / kolodvor | stanica |
| theatre | kazalište | pozorište |
| factory | tvornica | fabrika |
| sport | šport (or sport) | sport |
| family | obitelj | porodica |
| address | adresa | adresa (same) |
| university | sveučilište | univerzitet |
| million | milijun | milion |

**Croatian months are Slavic-rooted** (Croatia is one of only 5 Slavic countries to keep them — Czech, Polish, Ukrainian, Belarusian being the others):

| # | Croatian ✓ | Serbian (do not use) |
|---|-----------|----------------------|
| 1 | siječanj | januar |
| 2 | veljača | februar |
| 3 | ožujak | mart |
| 4 | travanj | april |
| 5 | svibanj | maj |
| 6 | lipanj | jun |
| 7 | srpanj | jul |
| 8 | kolovoz | avgust |
| 9 | rujan | septembar |
| 10 | listopad | oktobar |
| 11 | studeni | novembar |
| 12 | prosinac | decembar |

Croatian months are also adjectival in form (siječanj declines: `siječnja`, `siječnju`, etc.).

---

## Register Auto-Detection (Apply Before Translating)

Croatian formality is set by **pronoun + verb-ending** choice with capitalization conventions. Auto-detect from source:

| Source signal | Target register |
|---------------|-----------------|
| Casual / conversational / personal (`Hey!`, contractions, emoji, marketing voice, social) | **Informal (ti)** — `ti` pronoun lowercase, 2nd-person sg. verb endings (-š), familiar imperative (`Spremi`, `Klikni`). Allow some loanwords. |
| Neutral product UI / docs / consumer software (DEFAULT) | **Formal (Vi)** — `Vi` capitalized for direct address, 2nd-person pl. verb endings (-te), polite imperative (`Spremite`, `Kliknite`). Possessive `Vaš/Vaša/Vaše` also capitalized. |
| Legal / banking / government / enterprise B2B | **Formal (Vi) elevated** — same `Vi` form but full constructions, no contractions, prefer reflexive impersonal (`Vrši se`), avoid casual loanwords. |

**Hard rule: never mix levels in one text.** A string with `Možete promijeniti` (formal verb) and `tvoje postavke` (informal possessive) is broken.

**Capitalization rule for Vi:** `Vi / Vaš / Vaša / Vaše / Vaši / Vam / Vas` are capitalized in direct second-person address. This signals respect — failing to capitalize is read as informal even if verb forms are formal.

**Default for software UI: Vi (formal)** unless brand voice is explicitly youth/casual. Croatian business culture is more formal than e.g. Norwegian or Swedish — `Vi` is the safe default.

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. IJEKAVIAN forms only — never ekavian (severity 2.5)

Documented above. **The single defining feature of Croatian vs Serbian.** Every `vrijeme/lijepo/mlijeko/dijete/rijeka/svijet/lijep/cvijet/zvijezda/pjesma/mjesto`.

### 2. Word integrity — verb prefixes NEVER split (severity 3.0)

Croatian verbs with prefixes are **single words**. Splitting them is a critical error.

| ✗ Wrong (split) | ✓ Correct (joined) |
|-----------------|---------------------|
| `pre voditi` | **`prevoditi`** (to translate) |
| `iz vršiti` | **`izvršiti`** |
| `pre nijeti` | **`prenijeti`** (to transfer) |
| `na praviti` | **`napraviti`** |
| `sa čuvati` (rare in hr) / `spremati` | (use Croatian native `spremiti`) |
| `pre uzeti` | **`preuzeti`** (to download / take over) |
| `pro voditi` | **`provoditi`** |
| `ne uspjelo` (when meaning "didn't succeed") | use full construction `nije uspjelo` instead of writing the negation as a compound |

**Reflexive `se`/`si` is the OPPOSITE pattern** — `se` is a **separate clitic word**, NEVER attached. `prijavi se`, `registriraj se`, `odjavi se`. Writing `prijavise` or `registrirajse` is wrong.

### 3. Seven-case system (severity 2.5)

Croatian uses **all 7 Slavic cases**, including the vocative. Every noun, adjective, and pronoun declines.

| Case | Question | Use | Example (m. sg. "korisnik" — user) | Example (f. sg. "datoteka" — file) |
|------|----------|-----|------------------------------------|-------------------------------------|
| Nominativ (NOM) | tko? što? | Subject | korisnik | datoteka |
| Genitiv (GEN) | koga? čega? | Possession, "of", absence, 5+ count | korisnika | datoteke |
| Dativ (DAT) | komu? čemu? | Indirect object, "to" | korisniku | datoteci |
| Akuzativ (ACC) | koga? što? | Direct object | korisnika (animate=GEN) / sustav (inanimate=NOM) | datoteku |
| Vokativ (VOC) | — | Direct address | korisniče! | datoteko! |
| Lokativ (LOK) | o komu? čemu? | Location (always w/ prep) | korisniku (o korisniku) | datoteci (o datoteci) |
| Instrumental (INS) | s kim? čim? | "With", means | korisnikom | datotekom |

**Critical: animate masculine accusative = genitive form.** `vidim korisnika` ("I see [the] user"), NOT `vidim korisnik`. Inanimate masculines keep ACC = NOM: `vidim sustav`.

### 4. Preposition + governed case (severity 2.5)

| Preposition | Case | Example |
|-------------|------|---------|
| u (in/into) | LOK (location) / ACC (motion) | u sustavu (in system) / u sustav (into system) |
| na (on/onto) | LOK / ACC | na zaslonu / na zaslon |
| s / sa (with) | INS | s korisnikom, sa Vama |
| bez (without) | GEN | bez sustava, bez greške |
| za (for) | ACC | za korisnika, za sustav |
| od (from) | GEN | od korisnika |
| do (until/to) | GEN | do kraja |
| iz (out of) | GEN | iz mape |
| o (about) | LOK | o korisniku, o sustavu |
| po (per / along) | LOK | po datoteci, po korisniku |
| prije (before) | GEN | prije početka |
| nakon / poslije (after) | GEN | nakon prijave |
| prema (toward) | DAT | prema korisniku |
| kroz (through) | ACC | kroz aplikaciju |

`po + LOK` for "per" with rate: `po datoteci`, `po korisniku`. `dnevno` / `na dan` for "per day".

### 5. ICU plurals — one / few / other (1 / 2-4 / 5+ pattern) (severity 2.5)

```icu
{count, plural,
  one {# datoteka}
  few {# datoteke}
  other {# datoteka}
}
```

**CLDR plural category boundaries**:

| Category | Rule | Examples | Noun form |
|----------|------|----------|-----------|
| `one` | n % 10 = 1, n % 100 ≠ 11 | 1, 21, 31, 41, 101, 121 | **NOM singular** (datoteka) |
| `few` | n % 10 ∈ {2,3,4}, n % 100 ∉ {12,13,14} | 2, 3, 4, 22, 23, 24, 102, 103 | **GEN singular** (datoteke) |
| `other` | everything else | 0, 5-20, 25-30, 100, 1000 | **GEN plural** (datoteka) |

**Critical:** 11/12/13/14 use `other` (exceptions to the otherwise simple "ends in 1/2-4" pattern). Same for 111, 112, 113, 114.

### 6. Numeral-noun agreement (severity 2.0)

| Count | Pattern | Example |
|-------|---------|---------|
| 1 | NOM sg | 1 datoteka |
| 2, 3, 4 | GEN sg (with paucal adjective form) | 2 nove datoteke, 3 nova računala |
| 5+ | GEN pl | 5 datoteka, 10 korisnika |
| 11-14 | GEN pl (exception) | 11 datoteka, 12 sustava |
| 21 | NOM sg (back to "one") | 21 datoteka |
| 22-24 | GEN sg | 22 datoteke |
| 25+ | GEN pl | 25 datoteka |

### 7. Verb aspect — perfective vs imperfective (severity 2.0)

Every Croatian verb has aspect. UI patterns by aspect:

| Imperfective (process, ongoing) | Perfective (single completed event) | English |
|--------------------------------|--------------------------------------|---------|
| spremati | spremiti | save |
| brisati | obrisati / izbrisati | delete |
| prenositi / učitavati | prenijeti / učitati | upload / load |
| preuzimati | preuzeti | download |
| otvarati | otvoriti | open |
| zatvarati | zatvoriti | close |
| stvarati | stvoriti / napraviti | create |
| uređivati | urediti | edit |
| mijenjati | promijeniti | change |
| pisati | napisati | write |
| čitati | pročitati | read |
| slati | poslati | send |
| birati | odabrati / izabrati | choose / select |
| prevoditi | prevesti | translate |
| prijavljivati se | prijaviti se | log in |

**UI patterns by aspect:**

- **Buttons (single action)** → **perfective imperative**: `Spremi`, `Obriši`, `Pošalji`, `Odaberi`. (NOT `Spremaj`, which means "keep saving repeatedly".)
- **Ongoing status messages** → **imperfective verbal noun + …**: `Spremanje…`, `Učitavanje…`, `Prenošenje…`, `Slanje…`.
- **Completed status** → **perfective past participle** + **je**: `Datoteka je spremljena`, `Prijenos je završen`.
- **Failed status** → **perfective past + nije**: `Prijenos nije uspio`, `Datoteka nije spremljena`.

### 8. Clitic second-position rule (Wackernagel's law) (severity 2.0)

Croatian clitics (`je`, `se`, `si`, `mi`, `ti`, `mu`, `joj`, `nam`, `vam`, `im`, `bi`, `li`) MUST go in the **second position** of their clause.

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| `Se meni to ne sviđa` | **`To mi se ne sviđa`** |
| `Datoteka se mu prikazuje` | **`Datoteka mu se prikazuje`** (DAT `mu` before reflexive `se`) |

**Clitic order within the cluster**:
1. `li` (question particle)
2. AUX `je / sam / si / smo / ste / su / bi / bih`
3. DAT (`mi / ti / mu / joj / nam / vam / im`)
4. ACC (`me / te / ga / je / nas / vas / ih`)
5. Reflexive `se / si`

Example: `Da li mu se to sviđa?` (Q-AUX-DAT-REFL — does he like it?) — note: modern Croatian increasingly drops the `Da` opener for `Sviđa li mu se to?` style.

### 9. Three-gender adjective agreement (severity 2.0)

| Gender | Indef. example | Adjective ending (sg.) |
|--------|---------------|------------------------|
| Masculine (consonant ending) | sustav | novi sustav |
| Feminine (-a ending) | aplikacija | nova aplikacija |
| Neuter (-o/-e ending) | računalo | novo računalo |

Wrong gender adjective is auto-fail: `nova sustav` ✗, `novi aplikacija` ✗.

### 10. Past-tense gender agreement (severity 1.5)

Past tense = AUX + L-participle which agrees with subject in gender + number:

| Subject | L-participle | Example |
|---------|--------------|---------|
| m. sg. | -o | on je radio |
| f. sg. | -la | ona je radila |
| n. sg. | -lo | ono je radilo |
| m. pl. | -li | oni su radili |
| f. pl. | -le | one su radile |
| n. pl. | -la | ona su radila |

### 11. Verb-construction integrity — no stacked finite verbs (severity 2.0)

English `-ing` (gerund as adverbial: "I spent 6 years building...") MUST be rendered with **glagolski prilog sadašnji** (verbal adverb, -ći form), NOT a second finite clause.

| ✗ Stacked finite | ✓ Verbal adverb (-ći) | English |
|------------------|------------------------|---------|
| `Proveo sam 6 godina gradio sam posao` | **`Proveo sam 6 godina gradeći posao`** | I spent 6 years building the business |
| `Radio sam dok sam pisao izvješće` | **`Radio sam pišući izvješće`** | I worked while writing the report |
| `Provela je vrijeme čekala je rezultate` | **`Provela je vrijeme čekajući rezultate`** | She spent time waiting for results |

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
| raditi | radeći | working |
| govoriti | govoreći | speaking |
| prevoditi | prevodeći | translating |

**Also flag verb-root monotony**: if the same root appears 3+ times in one string (`radi na radu radnog procesa`), restructure with synonyms (`obavlja posao`, `razvija radni proces`).

### 12. Diacritics — Č Ć Đ Š Ž are essential (severity 2.5)

Never strip diacritics. `Spremi` is fine but `Pošalji` written as `Posalji` is broken; `Obriši` → `Obrisi` is broken; `Odaberite` → `Odaberite` is correct but `Učitavanje` → `Ucitavanje` is broken.

### 13. Latin script ONLY (severity 3.0)

Croatian is written **exclusively in Latin script**. Never use Cyrillic. (Croatia historically used Glagolitic, and briefly Cyrillic in certain dialects, but modern standard Croatian is unambiguously Latin.)

If a translation contains any Cyrillic letters except in tech identifiers/URLs (which would themselves be Latin anyway), something is wrong — most likely an accidental Serbian conversion.

---

## Pronouns and Possessives

### Personal pronouns

| English | Croatian | Notes |
|---------|----------|-------|
| I | ja | |
| you (sg. informal) | ti | |
| you (sg./pl. formal — capitalize) | Vi | Always capitalized in direct address |
| you (pl. informal) | vi | lowercase when truly plural informal |
| he | on | |
| she | ona | |
| it | ono | |
| we | mi | |
| they (m./mixed) | oni | |
| they (f.) | one | |
| they (n.) | ona | |

### Possessive pronouns (agree with possessed noun's gender/number/case)

| Person | m. sg. | f. sg. | n. sg. |
|--------|--------|--------|--------|
| moj (my) | moj | moja | moje |
| tvoj (your sg. informal) | tvoj | tvoja | tvoje |
| **Vaš (your formal — capitalize)** | **Vaš** | **Vaša** | **Vaše** |
| njegov (his) | njegov | njegova | njegovo |
| njezin / njen (her) | njezin | njezina | njezino |
| svoj (reflexive — own) | svoj | svoja | svoje |
| naš (our) | naš | naša | naše |
| njihov (their) | njihov | njihova | njihovo |

**Reflexive `svoj`**: used when possessor = subject of same clause.
- `On sprema svoju datoteku.` (He saves his own file.) ← reflexive
- `On sprema njegovu datoteku.` (He saves someone else's file.) ← non-reflexive — different referent

---

## UI Conventions

### Buttons — PERFECTIVE imperative (never infinitive)

Single-word action buttons take the **perfective imperative** — informal `Spremi` / formal `Spremite`. NEVER infinitive (`Spremiti`) — that reads as a manual instruction.

| English | ti (informal) | Vi (formal) |
|---------|---------------|-------------|
| Save | **Spremi** | **Spremite** |
| Cancel | **Odustani** / **Otkaži** | **Odustanite** / **Otkažite** |
| Delete | **Obriši** / **Izbriši** | **Obrišite** / **Izbrišite** |
| Send | **Pošalji** | **Pošaljite** |
| Edit | **Uredi** | **Uredite** |
| Search | **Pretraži** | **Pretražite** |
| Confirm | **Potvrdi** | **Potvrdite** |
| Continue | **Nastavi** | **Nastavite** |
| Submit | **Pošalji** | **Pošaljite** |
| Sign in | **Prijavi se** | **Prijavite se** |
| Sign out | **Odjavi se** | **Odjavite se** |
| Sign up | **Registriraj se** | **Registrirajte se** |
| Next | **Sljedeće** / **Dalje** | (same) |
| Back | **Natrag** | (same) |
| Done | **Gotovo** / **Završeno** | (same) |
| OK | **U redu** / **OK** | (same) |
| Close | **Zatvori** | **Zatvorite** |
| Upload | **Prenesi** | **Prenesite** |
| Download | **Preuzmi** | **Preuzmite** |
| Refresh | **Osvježi** | **Osvježite** |
| Settings | **Postavke** | (same) |
| Apply | **Primijeni** | **Primijenite** |
| Reset | **Vrati na zadano** / **Resetiraj** | **Resetirajte** |
| Select all | **Odaberi sve** | **Odaberite sve** |
| Deselect all | **Poništi sve** / **Odznači sve** | **Poništite sve** |
| Add more | **Dodaj još** (NOT `Dodaj više`) | **Dodajte još** |
| Show more | **Prikaži još** | **Prikažite još** |

**Tabs and navigation labels also use imperative**, not infinitive:
- ✗ `Prenijeti datoteke` (inf., instruction-manual tone)
- ✓ `Prenesite datoteke` (Vi imp.) / `Prenesi datoteke` (ti imp.)

### Status messages — three distinct patterns

**Ongoing (in-flight)** → **imperfective verbal noun + …**

| English | Croatian |
|---------|---------|
| Loading… | **Učitavanje…** |
| Saving… | **Spremanje…** |
| Sending… | **Slanje…** |
| Uploading… | **Prenošenje…** / **Učitavanje…** |
| Downloading… | **Preuzimanje…** |
| Translating… | **Prevođenje…** |
| Connecting… | **Povezivanje…** |
| Processing… | **Obrada…** |
| Searching… | **Pretraživanje…** |
| Please wait | **Pričekajte, molim** / **Molimo pričekajte** |

**Completed** → **Subject + je + perfective past participle** (full construction with auxiliary `je`)

| English | Croatian |
|---------|---------|
| Saved | **Spremljeno** / **Datoteka je spremljena** |
| Done | **Gotovo** / **Završeno** |
| Translation complete | **Prijevod je završen** |
| File uploaded | **Datoteka je prenesena** |
| Payment successful | **Plaćanje je uspjelo** / **Uspješno plaćanje** |
| Sent | **Poslano** / **Poruka je poslana** |

**Critical**: NEVER drop the `je` auxiliary. `Prijevod završen` ✗ (sounds incomplete) → `Prijevod je završen` ✓.

**Failed** → **Subject + nije + perfective past participle**

| English | Croatian |
|---------|---------|
| Save failed | **Spremanje nije uspjelo** |
| Upload failed | **Prijenos nije uspio** |
| Translation failed | **Prijevod nije uspio** |
| Connection failed | **Povezivanje nije uspjelo** |
| File not found | **Datoteka nije pronađena** |

NEVER use short forms like `Prijevod neuspjelo` — they sound unnatural.

**Validation / field errors** → nominal description

| English | Croatian |
|---------|---------|
| This field is required | **Ovo polje je obavezno** |
| Invalid format | **Neispravan format** |
| Password too short | **Lozinka je prekratka** |
| Email already in use | **E-mail adresa je već u upotrebi** |

**Action instructions** → imperative

| English | Croatian |
|---------|---------|
| Enter your password | **Unesite Vašu lozinku** (Vi) / **Unesi lozinku** (ti) |
| Choose at least one language | **Odaberite barem jedan jezik** |
| Try again | **Pokušajte ponovno** |

### Empty states — `Nema X` / `Nije pronađeno`

| ✗ Bare | ✓ Specific |
|--------|-----------|
| Prazno | **Nema rezultata** / **Nema pronađenih stavki** |
| Ništa ovdje | **Nema datoteka** / **Nema dostupnih podataka** |
| Bez podataka | **Nema dostupnih podataka** |
| Lista je prazna | **Nema stavki na popisu** |

### Drag-and-drop

- drag → **povucite** (Vi) / **povuci** (ti)
- drop (= place files) → **pustite** (Vi) / **ispustite** as fallback
- release → **ispustite** / **pustite**
- Combined: **`Povucite datoteke ovdje`** (Drag files here) / **`Pustite za prijenos`** (Release to upload).

`Ispustite datoteke ovdje` is borderline acceptable but `Povucite` reads as the unified drag-and-drop idiom.

### File picker — `Odaberi` not `Pregledaj`

Standard in Chrome HR / Windows HR / macOS HR:

| ✗ Older / navigation-oriented | ✓ Modern / action-oriented |
|-------------------------------|-----------------------------|
| Pregledaj datoteke | **Odaberi datoteke** (ti) / **Odaberite datoteke** (Vi) |
| Pregledaj datoteku | **Odaberi datoteku** / **Odaberite datoteku** |
| Kliknite za pregledavanje | **Kliknite za odabir** |
| Za pregledanje datoteka | **Za odabir datoteka** |

### Quantity expressions

| ✗ Calque | ✓ Native |
|----------|----------|
| 25+ jezika | **više od 25 jezika** |
| +{count} više | **i {count} drugih** / **još {count}** |
| +25 funkcija | **preko 25 funkcija** / **više od 25 funkcija** |

`Dodaj više` ✗ (literal "add more") → `Dodaj još` ✓ (idiomatic).

### Error messages — what + next step

| ✗ Bare | ✓ With next step |
|--------|------------------|
| Datoteka nije pronađena. | **Datoteka nije pronađena. Provjerite putanju.** |
| Greška mreže. | **Greška mreže. Pokušajte ponovno.** |
| Neispravan e-mail. | **E-mail adresa nije ispravna. Provjerite format.** |
| Prijava nije uspjela. | **Prijava nije uspjela. Provjerite korisničko ime i lozinku.** |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Croatian | Notes |
|------|----------|-------|
| Question mark | `?` | Same as English |
| Comma | `,` | Different conjunction rules (see below) |
| Period | `.` | Same |
| Colon | `:` | Same |
| Quotation marks | **„…"** (German low-9/high-9) — preferred, OR **»…«** (French-style, also acceptable) | Both standard in Croatian typography |
| Nested quotes | `'…'` | |
| Apostrophe | only in foreign names | Croatian genitive uses bare case ending, not English `'s` |

### Comma rules

| Rule | Example |
|------|---------|
| **NO comma** before `i` (and) | Povucite ovdje **i** kliknite. |
| **NO comma** before `ili` (or) | Povucite ovdje **ili** kliknite. |
| **NO comma** before `niti` (nor) | Niti znam **niti** mi je važno. |
| **Comma** before `da` (that, subordinating) | Vidim, **da** je datoteka otvorena. (Note: optional in modern style) |
| **Comma** before `koji/koja/koje` (relative) | Datoteka, **koja** je spremljena… |
| **Comma** before `ako` (if) | Spremite, **ako** želite. |
| **Comma** before `jer` (because) | Otkazano, **jer** nije uspjelo. |
| **Comma** before `ali` (but) | Brzo, **ali** učinkovito. |
| **Comma** before `nego` (but / rather) | Nije sporo, **nego** brzo. |
| **Comma** before `a` (and/but contrast) | Ja sam pisao, **a** ti si čekao. |

### Numbers

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **period (.)** | 1.234.567 |
| Decimal separator | **comma (,)** | 3,14 / 99,99 |
| Negative | `-25` | |
| Percent | `25%` (no space typical) | |

**Critical:** Croatian uses **period for thousands, comma for decimal** — opposite of English.

### Dates

| Format | Example | Use |
|--------|---------|-----|
| D. M. YYYY. | **15. 1. 2024.** | Default — note the period AFTER the year |
| D. mjesec YYYY. | **15. siječnja 2024.** | Long-form prose — month in genitive! |
| D. mjesec YYYY. godine | **15. siječnja 2024. godine** | Formal documents |
| YYYY-MM-DD | 2024-01-15 | Technical/API only |

**Croatian month names (Slavic-rooted, declines!):**

| Nominative | Genitive (used in dates) |
|------------|---------------------------|
| siječanj | siječnja |
| veljača | veljače |
| ožujak | ožujka |
| travanj | travnja |
| svibanj | svibnja |
| lipanj | lipnja |
| srpanj | srpnja |
| kolovoz | kolovoza |
| rujan | rujna |
| listopad | listopada |
| studeni | studenoga (or studenog) |
| prosinac | prosinca |

**Critical: in dates, the month is in genitive** — `15. siječnja 2024.` not `15. siječanj 2024.`.

**Weekdays (lowercase):** ponedjeljak, utorak, srijeda, četvrtak, petak, subota, **nedjelja** (= Sunday in Croatian; cf. Serbian `nedelja` = week).

Week starts **Monday**.

### Time

- 24-hour preferred: `14:30` or `14.30` (period acceptable as separator), or `14:30 sati`.
- 12-hour rarely used.

### Currency — EUR since 1 January 2023

Croatia adopted **the euro on 1 January 2023**, replacing the Croatian kuna (HRK). All modern Croatian UI uses EUR.

| Format | Pattern | Example |
|--------|---------|---------|
| Euro after amount | `€` after amount with space | **99,99 €** |
| ISO code | EUR | **99,99 EUR** |

**Do NOT** use HRK in modern UI — it was withdrawn. Historical references to HRK should explicitly say `kuna` if needed.

Never `$99.99` style in Croatian.

---

## Terminology — preferred Croatian terms

Croatian has a **stronger purist tradition** than Serbian — Croatian institutions actively promote native equivalents over loanwords. When in doubt, prefer the native form.

| English | ✓ Croatian preferred | ✗ Avoid (Serbian / loanword) |
|---------|---------------------|-------------------------------|
| user | korisnik | user |
| account | račun (banking) / korisnički račun (account) | akaunt |
| password | lozinka / zaporka | password |
| settings | postavke | postavke (same) |
| dashboard | nadzorna ploča | dashboard |
| email | e-mail / e-pošta | mejl, imejl |
| link | poveznica / link | — both acceptable |
| website | web-stranica / mrežna stranica | website |
| folder | mapa | folder |
| file | datoteka | fajl |
| device | uređaj | device |
| phone | telefon / mobilni telefon / mobitel | — |
| computer | **računalo** | kompjuter, **računar** (Serbian) |
| keyboard | **tipkovnica** | tastatura (Serbian) |
| screen | **zaslon** | ekran, monitor |
| application / app | aplikacija | — |
| update (v.) | ažurirati / nadograditi | apdejtati |
| save | spremiti / pohraniti | sejvati |
| delete | obrisati / izbrisati | — |
| upload | **prenijeti** / učitati | uploadati |
| download | **preuzeti** | downloadati |
| sign in / log in | prijaviti se | ulogirati se |
| sign up / register | registrirati se | — |
| search | pretraživati / tražiti | — |
| click | kliknuti / pritisnuti | — |
| share | podijeliti | šerati |
| profile | profil | — |
| notifications | obavijesti | notifikacije (acceptable, but `obavijesti` preferred) |
| privacy | privatnost | — |
| terms | uvjeti | — |
| support | podrška | — |
| help | pomoć | — |
| feedback | povratne informacije | feedback |
| menu | izbornik | meni |
| home | početna / početna stranica | — |
| logout | odjaviti se | — |
| **browser** | **preglednik** | browser, pregledač (Serbian) |
| **glossary** | **pojmovnik** | rječnik, glosar |
| **namespace** | **prostor imena** | namespace |
| build (software) | izgraditi / izraditi / stvoriti | builda (avoid) |
| deploy | postaviti / objaviti / pokrenuti u produkciju | deplojati |
| pipeline (CI/CD) | pipeline (keep) / proces izgradnje | cjevovod (= literal pipe) |
| commit (git) | commit (keep) / spremiti izmjene | — |
| merge (git) | spojiti / merge (keep in code) | — |
| repository | repozitorij | — |
| branch (git) | grana / branch (keep) | — |
| API | API (keep — Latin always) | — |
| endpoint | endpoint (keep) / krajnja točka | — |
| token | token (keep) | — |
| cache | predmemorija / cache | — |
| log (n.) | dnevnik / log | — |
| sync | sinkronizacija / sinkronizirati | — |
| webhook | webhook (keep) | — |
| **company** | **tvrtka** / poduzeće | firma, **preduzeće** (Serbian) |
| **office** | **ured** | kancelarija (Serbian) |

### Tech identifiers — keep in Latin

(Since Croatian is Latin-only this is less of a special rule, but still: keep brand names and identifiers as-is.)

- Programming languages: Python, JavaScript, Go, Rust, Java
- Frameworks: React, Vue, Angular, Next.js, Django
- Tools: Git, GitHub, GitLab, Docker, npm, pip, cargo
- Protocols: HTTP, REST, GraphQL, OAuth, JWT
- File formats: JSON, XML, YAML, CSV, PDF
- Brands: Google, Microsoft, Apple, iPhone, Android
- Commands, file paths, URLs, code snippets
- Placeholders: `{variableName}`, `{{count}}`, `<tag>`

---

## False Friends — Critical

| Croatian word | Actually means | NOT this (common AI error) | Correct for the English |
|---------------|----------------|-----------------------------|--------------------------|
| aktualan | current / topical | "actual" | "actual" → **stvaran / pravi** |
| realizirati | to implement / carry out | "to realize (understand)" | "realize (understand)" → **shvatiti** |
| eventualno | possibly | "eventually" | "eventually" → **na kraju** / **konačno** |
| uzbuđen | excited (sometimes ambiguous) | safer "excited" | "excited (looking forward)" → **veselim se** / **radujem se** |
| simpatičan | likeable / pleasant | "sympathetic (compassionate)" | "sympathetic" → **suosjećajan** |
| simpatija | a crush / affection | "sympathy (condolence)" | "sympathy" → **suosjećanje** |
| receptura | recipe (formal) | "receipt" | "receipt" → **račun** / **potvrda** |
| dirigirati | to conduct (music) | "to direct (manage)" | "direct (manage)" → **voditi** / **upravljati** |
| efektan | producing visual effect | "effective" | "effective" → **učinkovit** / **djelotvoran** |
| pretendirati | to claim / aspire to | "to pretend" | "pretend" → **pretvarati se** |
| nedjelja | Sunday (!) | "week" | "week" → **tjedan** (NOT `nedjelja`) |

The `nedjelja` (Sunday) vs Serbian `nedelja` (week) is a famous trap.

---

## Calque / Anti-Pattern List

| ✗ Calque | ✓ Native | Reason |
|----------|----------|--------|
| **Auto-otkriveno / Auto-spremi** | **Automatski otkriveno / Automatski spremi** | "Auto-X" — use full adjective form |
| **Prevedeni rezultati** (as header) | **Rezultati prevođenja** | English Past-Participle + Noun → Croatian Noun + Genitive verbal noun |
| **Ažurirane postavke** (as header) | **Postavke ažuriranja** / **Promjene postavki** | Same pattern |
| **Uvezene datoteke** (as header) | **Datoteke uvoza** / **Uvezeni dokumenti** | Same pattern |
| **opcija jezika** (noun + noun) | **jezične opcije** / **izbor jezika** | English N+N → Croatian adj+N or genitive |
| **projekt mapa** | **mapa projekta** / **projektna mapa** | English N+N → genitive or adjective |
| **korisnik postavke** | **korisničke postavke** / **postavke korisnika** | English N+N → adjective or genitive |
| **preferencija tona** | **željeni ton** / **odabir tona** | Anglicism noun → native adjective + noun |
| **To čini smisao** | **To ima smisla** / **To je logično** | "Makes sense" calque |
| **Na kraju dana** | **U konačnici** / **Na kraju krajeva** | "At the end of the day" calque |
| **uzeti mjesto** | **održati se** / **dogoditi se** | "Take place" calque |
| **bazirano na** | **na temelju** / **temeljeno na** | "Based on" calque |
| **u redu da** | **kako bi** / **da bi** | "In order to" calque |
| **na dnevnoj bazi** | **svakodnevno** / **dnevno** | "On a daily basis" calque |
| **u smislu (overused)** | **što se tiče** / **u pogledu** | "In terms of" calque |
| **izvršiti poboljšanje** | **poboljšati** | Use direct verb |
| **dati odgovor** | **odgovoriti** | Use direct verb |
| **izvršiti odabir** | **odabrati** | Use direct verb |
| **Nulta zastoja / Nula grešaka** | **Bez zastoja** / **Bez grešaka** | "Zero X" English marketing calque |
| **AI-pogonjen** | **temeljen na AI** / **uz pomoć AI** / **mrežno učenje** | "X-powered" calque |
| **podaci-orijentiran** | **temeljen na podacima** / **vođen podacima** | "X-driven" calque |
| **korisnik-prijateljski** | **korisniku prilagođen** / **lako za korištenje** | "user-friendly" calque |
| **Sjedinjene Američke Države** | **SAD** | UI short form |
| **Ujedinjeno Kraljevstvo Velike Britanije** | **Velika Britanija** / **UK** | UI short form |
| **[Subject] je potreban za [Purpose]** | **Potreban je [Subject]** | English subject-first → Croatian verb-first |
| **Draggajte** / **Drag-ajte** | **Povucite** | English verb → native |
| **Prijevod neuspjelo / Plaćanje neuspjelo** | **Prijevod nije uspio** / **Plaćanje nije uspjelo** | Missing auxiliary — sounds incomplete |
| **Prijevod završen** (no je) | **Prijevod je završen** | Missing auxiliary in completion message |
| **Poništi odabir svega** | **Poništi sve** / **Odznači sve** | Button brevity |
| **Odaberi odabir svih** | **Odaberi sve** | Button brevity / redundancy |
| **Dodaj više** | **Dodaj još** | "Add more" — use idiomatic `još` |
| **per datoteka** | **po datoteci** | "per X" → `po` + locative |

### Past Participle + Noun → Noun + Genitive (header pattern)

This is a uniquely natural Croatian restructure. English likes adjectival past participles in headers; Croatian prefers nominalization.

| English | ✗ Calque (Participle + N) | ✓ Native (N + Genitive of verbal noun) |
|---------|----------------------------|-----------------------------------------|
| Translated Results | Prevedeni rezultati | **Rezultati prevođenja** |
| Updated Settings | Ažurirane postavke | **Postavke ažuriranja** / **Promjene postavki** |
| Imported Files | Uvezene datoteke | **Datoteke uvoza** (or `Uvezeni dokumenti` if listing finished items is the intent) |
| Selected Options | Odabrane opcije | **Odabir opcija** |

---

## Custom Sections

### Verbification suffixes are VALID — don't over-correct

Croatian forms verbs from English loans via `-irati` / `-ati` suffixes. These are **legitimate** Croatian verbs once formed:

| English | Croatian verbified | Status |
|---------|---------------------|--------|
| install | instalirati | fully naturalized |
| sync | sinkronizirati | fully naturalized |
| reset | resetirati | fully naturalized |
| register | registrirati se | fully naturalized |
| reagirati | (reagirati) | OK |
| upload | uploadati / prenijeti | native `prenijeti` preferred for UI |
| download | downloadati / preuzeti | native `preuzeti` preferred |
| log in | ulogirati se / prijaviti se | native `prijaviti se` preferred |
| share | šerati / podijeliti | native `podijeliti` preferred |
| like (social) | lajkati | acceptable in social-media contexts |
| commit (git) | commitati / spremiti izmjene | code-context only |

Don't flag `instalirati` or `sinkronizirati` as errors — they're standard. The flag is for **hybrid forms with native verbs already available** (e.g., prefer `spremiti` over `sejvati`, `obrisati` over `deletirati`).

### Per vs za — CRITICAL semantic distinction

| Source | ✓ Croatian | Meaning |
|--------|-----------|---------|
| per language (rate) | **po jeziku** (lok.) | rate, per-unit |
| for 25 languages (total) | **za 25 jezika** (acc.) | total scope |
| 5 USD per language | **5 USD po jeziku** | rate |
| 5 USD for all languages | **5 USD za sve jezike** | total |

### Cost / estimate ordering

Prefer amount-first:

| ✗ Ambiguous | ✓ Clear |
|-------------|---------|
| 5 jezika 25 kredita | **25 kredita za 5 jezika** |

### UI element references in prose

Use quotation marks for specific UI labels:

| ✗ Compound | ✓ Quoted label |
|------------|----------------|
| Kliknite Spremi-gumb | **Kliknite na gumb „Spremi"** |
| Otvorite Postavke-karticu | **Otvorite karticu „Postavke"** |
| Koristite Ime-polje | **Koristite polje „Ime"** |

### Brand names + Croatian declension

Foreign brand names CAN be declined Croatian-style with a hyphen + Croatian ending (informal), OR stay invariant (formal/UI default):

- `Google` → `Google-a` (gen.), `Google-u` (lok.), `Google-om` (ins.) — informal/conversational
- For formal UI, prefer prepositional phrases: `na Google-u` or restructure: `na platformi Google`.
- `iPhone` → `iPhone-a`, `iPhone-u` (gen. / lok.)

---

## Self-Check Checklist (Run Before Returning Output)

### Croatian language identity (auto-fail on miss)

- [ ] **IJEKAVIAN forms** — `vrijeme/lijepo/mlijeko/dijete/rijeka/svijet/lijep/cvijet/zvijezda/pjesma/mjesto` (NEVER ekavian `vreme/lepo/mleko/dete/reka/svet/lep/cvet/zvezda/pesma/mesto`).
- [ ] **Croatian months**: siječanj, veljača, ožujak, travanj, svibanj, lipanj, srpanj, kolovoz, rujan, listopad, studeni, prosinac (NOT januar, februar, etc.).
- [ ] **Croatian-distinct vocabulary**: tjedan (not nedelja), tisuća (not hiljada), tko (not ko), što (not šta), nogomet (not fudbal), kruh (not hleb), računalo (not računar), tipkovnica (not tastatura), zaslon (not ekran), tvrtka (not preduzeće).
- [ ] **Latin script only** — no Cyrillic anywhere.

### Accuracy

- [ ] **Word integrity** — prefixes joined (`prevoditi`, `izvršiti`, `spremiti`), no spaces. Reflexive `se`/`si` separate (`prijavi se`, `registriraj se`).
- [ ] **Gender agreement** on every noun-adj pair (novi sustav / nova aplikacija / novo računalo).
- [ ] **Seven cases** correct, especially:
  - Animate masc. accusative = genitive (`vidim korisnika`).
  - Instrumental after `s/sa` (`s korisnikom`).
  - Locative after `u/na/o/po` (`u sustavu`, `o korisniku`, `po datoteci`).
  - Genitive after `bez/od/do/iz/prije/nakon` (`bez sustava`).
- [ ] **ICU plurals**: `one` / `few` / `other` categories present (1 = nom.sg, 2-4 = gen.sg, 5+ = gen.pl). 11-14 use `other`.
- [ ] **Numeral-noun agreement** matches plural pattern.
- [ ] **Verb aspect** correct: perfective for completed (buttons, completion), imperfective for ongoing (status, process).
- [ ] **Clitics in 2nd position** (Wackernagel): `To mi se ne sviđa`, not `Se mi to ne sviđa`.
- [ ] **Past-tense gender agreement** on L-participle (radio/radila/radilo).
- [ ] **No stacked finite verbs** from English -ing — use `-ći` verbal adverb.
- [ ] **Diacritics intact** — Č Ć Đ Š Ž never stripped.
- [ ] **Placeholders preserved** (`{var}`, `{{count}}`, `<tag>`, URLs, code identifiers).
- [ ] **Numbers**: comma decimal (3,14), period thousands (1.234), `€` after amount.
- [ ] **Dates**: `15. siječnja 2024.` (month in genitive!), period after year.
- [ ] **Time**: 24-hour, `14:30`.
- [ ] **Currency: EUR** (not HRK — kuna withdrawn 2023).
- [ ] **per vs za**: `po + LOK` for rate, `za + ACC` for total.

### Register

- [ ] **Vi/ti chosen and applied consistently** — pronouns, possessives, verb endings all match.
- [ ] **`Vi/Vaš/Vaša` capitalized** in direct second-person address.
- [ ] **No mixing** of Vi-form verb ending with ti-form possessive within one text.

### UI conventions

- [ ] Buttons use **perfective imperative** (`Spremi`/`Spremite`), not infinitive (`Spremiti`).
- [ ] Tabs/navigation also use imperative, not infinitive.
- [ ] Reflexive `se` present where required (`prijavi se`, `registriraj se`).
- [ ] Status ongoing: **imperfective verbal noun + …** (`Učitavanje…`, `Spremanje…`).
- [ ] Status completed: **Subject + je + perfective past participle** (`Prijevod je završen`), not bare `Prijevod završen`.
- [ ] Status failed: **Subject + nije + perfective past participle** (`Prijenos nije uspio`), not bare `Prijenos neuspio`.
- [ ] Empty state: `Nema X` / `Nije pronađeno` with specific noun.
- [ ] File picker: `Odaberi`, not `Pregledaj`.
- [ ] Drag-drop: `Povucite`, `Pustite/Ispustite`.
- [ ] Quantity: `više od 25`, `još {count}`, NOT `25+`, `+{count}`.
- [ ] Quotes: `„X"` (low-9/high-9) OR `»X«` (French-style).

### Naturalness

- [ ] **Past Participle + Noun headers** → **Noun + Genitive of verbal noun** (`Rezultati prevođenja`).
- [ ] **Auto-X prefix** → full adjective `Automatski X`.
- [ ] **Marketing "Zero X"** → `Bez X`.
- [ ] **English N + N compounds** → Croatian adj + N or genitive.
- [ ] **No verbose collocations** (`izvršiti poboljšanje` → `poboljšati`).
- [ ] **No false friends**: `aktualan ≠ actual`, `realizirati ≠ realize`, `eventualno ≠ eventually`, `nedjelja ≠ week (it means Sunday)`.
- [ ] **No verb-root monotony** (same root 3+ times).
- [ ] **No accidental Serbian forms** (no `vreme`, `lepo`, `mleko`, `tastatura`, `ekran`, `kompjuter`, `kafa`, `aerodrom`).
- [ ] **Croatian months in genitive** in date prose (`15. siječnja 2024.`).

---

## Worked Example — Standard hr formal UI

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** neutral product UI, exclamation → **Vi (formal)**, Croatian language identity.

**Translation:**

> Dobrodošli natrag! Imate 3 nove datoteke na svojem računu. Kliknite **Nastavi** da biste ih pregledali ili **Odustani** da biste ostali ovdje. Spremanje Vaših izmjena…

**Why this works:**
- `Dobrodošli natrag` — standard greeting, plural participle (formal Vi → -i plural).
- `Imate` — Vi-form verb (2nd-person plural present).
- `3 nove datoteke` — `3` triggers `few` (gen.sg.); `datoteka` is fem.; `nove` is fem. paucal adjective.
- `na svojem računu` — `na` + LOK; `računu` is masc. LOK; `svojem` is reflexive possessive.
- Buttons imperative: `Nastavi`, `Odustani` (both ti? actually here `Kliknite` is Vi but button labels are short imperatives — pick a style and be consistent; using `Nastavite/Odustanite` would also be valid Vi-form).
- `da biste ih pregledali` / `da biste ostali` — Vi-form `da + present` construction (natural Croatian).
- `Spremanje Vaših izmjena…` — imperfective verbal noun for ongoing status; `Vaših izmjena` gen.pl.
- No comma before `ili` ✓.
- No religious / cultural filler injected.

**Same string informal (ti):**

> Dobrodošao/dobrodošla natrag! Imaš 3 nove datoteke na svojem računu. Klikni **Nastavi** da bi ih pregledao/la ili **Odustani** da bi ostao/la ovdje. Spremanje tvojih izmjena…

(Past participles `dobrodošao/dobrodošla`, `pregledao/pregledala`, `ostao/ostala` agree with addressee's gender; in real UI pick a gender-neutral phrasing.)

---

## Worked Example — ICU plural expansion

**Source:**

```icu
You have {count, plural, one {# new file} other {# new files}}.
```

**Translation (full Croatian three-category expansion):**

```icu
Imate {count, plural,
  one {# novu datoteku}
  few {# nove datoteke}
  other {# novih datoteka}
}.
```

Notes:
- `one`: ACC sg (object of `Imate`) — `1 novu datoteku`.
- `few`: paucal genitive sg — `2 nove datoteke` (note: in 2-4 with adjective, the form looks like NOM/ACC plural but is technically GEN sg + paucal adj agreement).
- `other`: GEN pl — `5 novih datoteka`.

---

## Worked Example — Date with genitive month

**Source:** Last login: January 15, 2024 at 2:30 PM

**Translation:**

> Posljednja prijava: 15. siječnja 2024. u 14:30.

Note: `siječnja` (genitive of `siječanj`) — Croatian dates use month in genitive. NOT `15. siječanj 2024.`.

---

## Worked Example — Verb-construction integrity (-ći)

**Source:** I spent 6 years building this business while learning from mistakes.

**✗ Wrong (stacked finite verbs):**

> Proveo sam 6 godina gradio sam ovaj posao dok sam učio iz pogrešaka.

**✓ Right (verbal adverb -ći for simultaneous actions):**

> Proveo sam 6 godina gradeći ovaj posao i učeći iz pogrešaka.

---

## When in Doubt

1. **Default to hr, Vi (formal), ijekavian, Latin script.**
2. If a word looks ekavian (`vreme`, `lepo`, `mleko`, `dete`) → **fix to ijekavian** (`vrijeme`, `lijepo`, `mlijeko`, `dijete`).
3. If you used a Serbian-flavored word (`računar`, `tastatura`, `ekran`, `nedelja` for "week", `januar`) → **fix to Croatian** (`računalo`, `tipkovnica`, `zaslon`, `tjedan`, `siječanj`).
4. If a verb prefix has a space (`pre voditi`) → **join it**: `prevoditi`.
5. If `se` is attached to a verb → **separate it**: `prijavi se`, NOT `prijavise`.
6. If you wrote `Prijevod završen` or `Prijenos neuspio` → **add the auxiliary**: `Prijevod je završen`, `Prijenos nije uspio`.
7. If you used `infinitive` for a button → **switch to imperative**: `Spremiti` ✗ → `Spremi/Spremite` ✓.
8. If you stacked two finite verbs from an English -ing → **rewrite with -ći**.
9. If currency is HRK → **fix to EUR** (kuna withdrawn 2023).
10. If a date is `15. siječanj 2024.` → **fix month to genitive**: `15. siječnja 2024.`.
