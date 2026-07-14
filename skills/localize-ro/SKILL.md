---
name: localize-ro
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Romanian (Română) for Romania (and Moldova where applicable). Romanian is the only Romance language in the Balkans and the only major Romance language with a THREE-GENDER system — masculine + feminine + NEUTER (where neuter = masc.sg + fem.pl: un sistem → sistemele, un fișier → fișierele). Other unique features: postposed definite article attached to the noun (utilizator → utilizator**ul**, pagină → pagin**a**, fișier → fișier**ele**), genitive-dative case with `-ului/-ei/-elor` endings (folderul proiectului NOT folder proiect — bare juxtaposition fails), the five mandatory diacritics ă/â/î/ș/ț (and CRITICAL: ș/ț are comma-below NOT cedilla ş/ţ which is Turkish), ICU one/few/other plurals with \"de\" inserted before the noun for 20+ (1 fișier / 5 fișiere / 20 **de** fișiere — the \"de\" rule is the headline Romanian plural feature), Dumneavoastră/tu formality with verb agreement (Dumneavoastră + puteți + Salvați, NOT Dumneavoastră poți), „99-66\" quotation marks, comma decimal + period thousands (1.234,56), DD.MM.YYYY dates, Lei (RON) currency (NOT in eurozone), false-friend avoidance (actual=current NOT actual; eventual=possible NOT eventually; a realiza=achieve NOT realize; a suporta=tolerate NOT support; librărie=bookstore NOT library), native-verb preference (a șterge not a deleta, a încărca not a uploada, a extinde not a scala, a personaliza not a customiza, a prelucra not a procesa), \"Nu există X\" / \"Niciun X\" for empty states, \"Plată finalizată\" participles over \"Plată de succes\" adjective calques, and the \"per X\" → \"pe X\" rule (pe limbă, pe utilizator — NEVER per limbă)."
---

# Localize: Romanian (ro → Română)

You are translating source text into Romanian for Romania (and Moldova, where the same standard Romanian applies — Moldovan is Romanian with a different name post-2013 constitutional change). This skill captures grammar, register, UI conventions, formatting, and Romanian-specific failure modes derived from a production translation prompt.

## Scope & Variants

**One standard, two countries:**
- **ro-RO** — Romanian as used in Romania. Official language.
- **ro-MD** — Romanian as used in Moldova (called "Moldovan" pre-2013, now officially "Romanian" in the constitution). Same standard, minor lexical differences negligible for UI.

For product UI, **ro-RO is the universal default**.

**Native name:** Limba română (the language); românește (the adverb "in Romanian"). Use "română" for the language in UI.

**Identity guardrail:**
- Romanian is a **Romance language** (Latin-derived), NOT Slavic. Despite being surrounded by Slavic languages (Bulgarian, Serbian, Ukrainian, etc.) and having a Slavic vocabulary layer (~15%), the grammar is fundamentally Latin: Romance verbs, Romance articles, Romance case marking.
- Romanian is the **only major Romance language with**:
  - A productive neuter gender
  - Postposed definite article (Latin-style fused suffix)
  - A retained morphological case system (others lost it; Spanish/French/Italian use prepositions)
- Romanian uses the **Latin alphabet with 5 diacritics** (ă, â, î, ș, ț), NOT Cyrillic. (Moldovan was written in Cyrillic during Soviet era — that's obsolete since 1989.)
- Do NOT translate Romanian by analogy with Italian/Spanish/French — its grammar diverged early.

## Register

**Default level: FORMAL (Dumneavoastră-form)** for software UI, errors, documentation, marketing aimed at business users. Consumer-app marketing may use informal `tu`.

| | Dumneavoastră (formal) | Tu (informal) |
|---|---|---|
| Pronoun | Dumneavoastră (often abbreviated `Dvs.` in writing) | tu |
| Verb form | **2nd person plural** (puteți, sunteți, aveți) | 2nd person singular (poți, ești, ai) |
| Imperative | Salvați, Selectați, Ștergeți | Salvează, Selectează, Șterge |
| Possessive | dumneavoastră (invariable) | tău/ta/tăi/tale (agrees) |

**Critical:** Dumneavoastră uses **2nd-person plural verbs** (like French vous). Mixing is severity 2.0.

**Examples:**
- ❌ Dumneavoastră **poți** modifica (2sg verb with formal pronoun) → ✅ Dumneavoastră **puteți** modifica
- ❌ fișierele dumneavoastră + **Selectează** (formal possessive + informal imperative) → ✅ fișierele dumneavoastră + **Selectați**
- ❌ Salvați-vă **a ta** muncă (formal verb + informal possessive) → ✅ Salvați-vă munca dumneavoastră

**Within a file, ONE register only.** Mixing dumneavoastră and tu in possessives, verbs, or imperatives is always wrong.

## Critical Hard Rules

### Three-Gender System with NEUTER (severity 2.0 — defining Romanian feature)

**Romanian has THREE grammatical genders.** The neuter is unique: it behaves as **masculine in singular and feminine in plural**.

| Gender | Indef art | Singular | Plural | Examples |
|---|---|---|---|---|
| Masculine | **un** | -∅ / -e / -u | -i | un utilizator → utilizator**ii** |
| Feminine | **o** | -ă / -e / -a | -e / -i | o pagină → pagin**ile** |
| Neuter | **un** | (like masc) | (like fem) | un fișier → fișier**ele** |

**Most modern tech terms are neuter:**
- un sistem → sistemele
- un fișier → fișierele
- un computer → computerele
- un program → programele
- un cont → conturile
- un mesaj → mesajele
- un buton → butoanele
- un cod → codurile
- un fond → fondurile

**Common errors:**
- ❌ **o** sistem (using fem article with neuter) → ✅ **un** sistem
- ❌ sistem**ii** (using masc plural with neuter) → ✅ sistem**ele**
- ❌ **un** soluție (using masc article with feminine) → ✅ **o** soluție
- ❌ **o** computer → ✅ **un** computer

**Adjective agreement follows the neuter pattern:**
- un sistem **nou** (masc sg adj) → sisteme **noi** (fem pl adj)
- un fișier **important** → fișiere **importante**
- un program **rapid** → programe **rapide**

### Postposed Definite Article (severity 2.0)

**Romanian attaches the definite article to the END of the noun**, fused with the stem. This is unique among major modern languages (only Albanian, Bulgarian, and Macedonian share it).

| Gender | Indefinite | Definite (fused) |
|---|---|---|
| Masculine | un utilizator (a user) | utilizator**ul** (the user) |
| Feminine | o pagină (a page) | pagin**a** (the page) |
| Neuter sg | un fișier (a file) | fișier**ul** (the file) — like masc |
| Neuter pl | fișiere | fișier**ele** (the files) — like fem |

**Common errors:**
- ❌ "utilizator a fost șters" → ✅ "**utilizatorul** a fost șters"
- ❌ "fișier salvat" (as standalone sentence) → ✅ "**Fișierul** a fost salvat" / "**Fișierul** salvat"
- ❌ "pagină principală" (as the page title) → ✅ "**Pagina** principală"

When the noun is generic/uncountable, no article: "Eroare de sistem" (a type of error) vs "Eroarea sistemului" (the error of THE system).

### Genitive-Dative Case (severity 1.5)

Romanian retains a morphological case system, simplified to:
- **Nominative-accusative** (subject and direct object — same form)
- **Genitive-dative** (possession and indirect object — same form, marked by `-ului` / `-ei` / `-elor`)
- **Vocative** (direct address — `-ule!` / `-o!` — rare in UI)

**The genitive-dative is REQUIRED between two specific nouns** (where English uses "of" or apostrophe-s):

| Wrong (bare juxtaposition) | Correct (genitive) | English |
|---|---|---|
| folder proiect | **folderul proiectului** | the folder of the project |
| nume director | **numele directorului** | the name of the directory |
| pagina utilizator | **pagina utilizatorului** | the user's page |
| configurații sistem | **configurațiile sistemului** | the system's settings |
| eroare aplicație | **eroarea aplicației** | the application's error |
| stare conexiune | **starea conexiunii** | connection status |
| detalii tranzacție | **detaliile tranzacției** | transaction details |

**Genitive endings:**
- Masc/neuter sg: `-ul` → `-ului` (utilizator**ul** → utilizator**ului**, sistem**ul** → sistem**ului**)
- Fem sg: `-a` → `-ei` (pagin**a** → pagin**ei**, aplicați**a** → aplicați**ei**)
- Plural: `-le` → `-lor` (utilizator**ii** → utilizator**ilor**, fișier**ele** → fișier**elor**)

**Exception** — when the modifier is generic/classificatory (not a specific entity), bare juxtaposition with `de` is correct: "eroare **de** sistem" (a system-error type), "fișier **de** configurare" (a config-type file). These are stable compounds.

### Five Mandatory Diacritics: ă â î ș ț (severity 2.0)

**Romanian has 5 essential diacritics.** Omitting any is a hard error.

| Letter | Name | Where used | Examples |
|---|---|---|---|
| **Ă/ă** | a-breve | reduced/schwa vowel | băiat, fără, două |
| **Â/â** | a-circumflex | within words (high-back vowel) | în, pâine, român, încă |
| **Î/î** | i-circumflex | word-initial/final (same sound as â) | început, își, înăuntru |
| **Ș/ș** | s-with-comma-below | "sh" sound | și, ștergere, configurații |
| **Ț/ț** | t-with-comma-below | "ts" sound | țară, configurații, conține |

**CRITICAL — Comma vs Cedilla:**

Romanian uses **`Ș` / `ș` and `Ț` / `ț` with comma-below**, NOT `Ş` / `ş` and `Ţ` / `ţ` with cedilla (Turkish style). They look similar but are DIFFERENT Unicode characters.

- ✅ Romanian: `Ș ș Ț ț` (U+0218, U+0219, U+021A, U+021B)
- ❌ Turkish: `Ş ş Ţ ţ` (U+015E, U+015F, U+0162, U+0163)

Older Romanian texts and broken Unicode fonts use cedilla — but modern Unicode-compliant Romanian uses comma-below. Always use comma-below for new content.

**Common stripping errors:**
- ❌ configuratii → ✅ **configurații** (ț required)
- ❌ stergere → ✅ **ștergere** (ș required)
- ❌ inceput → ✅ **început** (î required)
- ❌ fara → ✅ **fără** (ă required)
- ❌ pâine → kept correctly (â within word)
- ❌ Romana → ✅ **Română** (ă required)

### ICU Plurals: one / few / other — the "de" rule (severity 2.0)

**Romanian has THREE plural categories**, and uses the **preposition `de` before nouns when count ≥ 20** (technically: numbers ending in 00 or 01-19 in the last two digits use `few`; everything else uses `other` with `de`).

| Branch | Rule | Example (fișier — neuter) |
|---|---|---|
| **one** | n = 1 | 1 fișier |
| **few** | n = 0, 2-19, or n % 100 = 1-19 | 0 fișiere, 5 fișiere, 19 fișiere, 101 fișiere, 119 fișiere |
| **other** | n = 20+ to 100, then 120+ etc. | **20 de fișiere**, **50 de fișiere**, **100 de fișiere**, **120 de fișiere** |

```icu
{count, plural,
  one {# fișier}
  few {# fișiere}
  other {# de fișiere}
}
```

The **"de" before the noun in the `other` branch is non-optional Romanian grammar** when counting ≥ 20.

- ❌ "25 limbi" → ✅ "**25 de limbi**"
- ❌ "100 utilizatori" → ✅ "**100 de utilizatori**"
- ✅ "5 fișiere" (no `de` — n is in `few`)
- ✅ "115 fișiere" (no `de` — last two digits 1-19)
- ❌ "25+ limbi" (English-style) → ✅ "**peste 25 de limbi**"

### Adjective Agreement (severity 1.5)

Adjectives agree with noun in **gender + number** (case is mostly identical to noun's). Most adjectives FOLLOW the noun.

| Noun | Adjective | Form |
|---|---|---|
| un sistem **nou** | masc sg | -∅ |
| o pagină **nouă** | fem sg | -ă |
| un fișier **important** | neuter sg = masc sg | -∅ |
| fișiere **importante** | neuter pl = fem pl | -e |
| sisteme **noi** | masc pl OR neuter pl | -i |
| pagini **noi** | fem pl | -i |

- ❌ sisteme nou (sg adj with pl noun) → ✅ sisteme **noi**
- ❌ platforma inteligent (masc adj with fem noun) → ✅ platforma **inteligentă**

A few high-frequency adjectives precede the noun: `bun`, `mare`, `mic`, `frumos`. "O bună soluție" / "un mare succes" — these add stylistic emphasis.

## Pronouns and Possessives

| English | Formal | Informal |
|---|---|---|
| you (subj) | **Dumneavoastră** / Dvs. | tu |
| you (obj) | vă / pe dumneavoastră | te / pe tine |
| your (poss) | **dumneavoastră** (invariable) | tău / ta / tăi / tale (agrees) |
| Imperative (sg) | Salvați (2pl form) | Salvează (2sg) |

`dumneavoastră` does NOT inflect — it's the same form regardless of gender/number of the noun it modifies.

## UI Conventions

### Button Labels — Imperative (formal preferred) or Infinitive

Romanian buttons use **imperative formal** (Salvați, Ștergeți) OR **infinitive** (Salvare, Ștergere) — both are acceptable, but **imperative is preferred for clear actions**.

| Wrong | Correct (preferred) | Alternative | English |
|---|---|---|---|
| Salvați (infinitive only — context: needs action) | **Salvați** (imperative) | Salvare (infinitive) | Save |
| Ștergeți | **Ștergeți** (imperative) | Ștergere | Delete |
| Anulați | **Anulați** | Anulare | Cancel |
| Încărcați | **Încărcați** | Încărcare | Upload |
| Descărcați | **Descărcați** | Descărcare | Download |
| Conectați-vă | **Conectați-vă** | Conectare | Log in |
| Selectați | **Selectați** | Selectare | Select |
| Editați | **Editați** | Editare | Edit |

Use imperative for direct action; infinitive for menu labels / option lists.

### Status Messages — Reflexive Passive or `În curs de...`

For ongoing actions, use **reflexive passive (`se` + verb)** or **`În curs de...`**:

| Wrong (past) | Correct | English |
|---|---|---|
| Salvat... | **Se salvează... / În curs de salvare...** | Saving... |
| Încărcat... | **Se încarcă... / Se procesează...** | Loading... |
| Trimis... | **Se trimite... / În curs de trimitere...** | Sending... |
| Verificat... | **Se verifică...** | Checking... |

For completion, use **participial form** (see next section).

### Completion Messages — Participial Form (NOT "de succes")

Romanian completion states use **participial forms** (`finalizată`, `efectuată`, `salvat`), NOT adjective calques like "de succes" (= "of success", a literal calque of English "successful"):

| Wrong (calque) | Correct (participial) | English |
|---|---|---|
| Plată **de succes** | **Plată efectuată / Plată finalizată / Gata!** | Payment successful |
| Încărcare **reușită** | **Încărcare finalizată / Fișier încărcat** | Upload successful |
| Operațiune **completă** | **Operațiune finalizată / Gata!** | Operation complete |
| Salvare **cu succes** | **Salvat / Salvare finalizată** | Saved successfully |
| Conectare **de succes** | **Conectare reușită / Conectat** | Connected (Login OK) |

Note: `reușită` is acceptable for "successful" in some contexts (especially "Conectare reușită") but `finalizată`/`efectuată` is preferred as a default.

### Empty State Messages — `Nu există X` / `Niciun X`

For empty states (no items, no results), Romanian uses **existential negation** (`Nu există X`) or **negative determiner** (`Niciun X` / `Nicio X`), NOT passive constructions:

| Wrong (passive calque) | Correct (existential) | English |
|---|---|---|
| Nu au fost selectate limbi | **Nu există limbi selectate / Nicio limbă selectată** | No languages selected |
| Nu au fost găsite rezultate | **Nu există rezultate / Niciun rezultat** | No results found |
| Nu au fost încărcate fișiere | **Nu există fișiere încărcate / Niciun fișier încărcat** | No files uploaded |

`Niciun` (masc/neuter) / `Nicio` (fem) is the **negative singular determiner**. It is written as ONE word (NOT `nici un`).

### Drag-and-Drop Vocabulary

- **a trage** = to drag
- **a plasa** / **a elibera** = to drop / release
- **trageți și plasați** = "drag and drop" (compound action)

```
✅ Trageți fișierele aici          (drag files here)
✅ Trageți și plasați aici          (drag and drop here)
✅ Eliberați pentru a încărca       (release to upload)
❌ a permite încărcarea             (vague — "to allow upload")
❌ drag and drop                    (English — unchanged)
```

### Error Messages — Direct Predicate + Actionable Advice

| Wrong (verbose nominal) | Correct (predicate + advice) |
|---|---|
| Eroare la procesarea fișierului | **Fișierul nu a putut fi procesat. Verificați formatul.** |
| Eroare de conexiune | **Nu există conexiune. Verificați rețeaua.** |
| Eroare de validare | **Datele nu sunt valide. Verificați câmpurile.** |

### Article Completeness in Subjects

Subject nouns in sentences need the definite article:

- ❌ "variabilă de mediu lipsește" → ✅ "**variabila** de mediu lipsește" / "**lipsește variabila** de mediu" (verb-first also natural)
- ❌ "utilizator nu a fost găsit" → ✅ "**utilizatorul** nu a fost găsit"

## Punctuation, Numbers, Dates, Currency

### Quotation Marks
- **Romanian uses "99-66" style quotes: `„..."`** — low opening (like comma), high-right closing
- Secondary: `«...»` (Russian/French guillemets — used in older typography)
- ❌ "English quotes" → ✅ „Ghilimele românești"

### Numbers
- Decimal separator: **comma** (3**,**14)
- Thousands separator: **period** (1**.**234)
- Format: `1.234.567,89`
- ❌ 1,234.56 (US) → ✅ 1.234,56

### Dates — DD.MM.YYYY (or word form)
- **Numeric**: `15.01.2024` (with periods) — most common in UI
- Alternative: `15/01/2024` (with slashes — also common)
- **Word form**: `15 ianuarie 2024` (months **lowercase**, day-month-year, no comma)
- ❌ 01/15/2024 (US) → ✅ **15.01.2024**

Months (always lowercase):
| English | Romanian |
|---|---|
| January | ianuarie |
| February | februarie |
| March | martie |
| April | aprilie |
| May | mai |
| June | iunie |
| July | iulie |
| August | august |
| September | septembrie |
| October | octombrie |
| November | noiembrie |
| December | decembrie |

### Time
- 24-hour: `14:30` (standard) or `la ora 14:30` (more formal)
- 12-hour: rare in formal contexts

### Currency: RON Leu (NOT in eurozone)
- **Romania uses the leu (RON / lei).** Romania has NOT yet adopted the euro.
- Format: `99,99 lei` (lowercase "lei", after amount, with space) or `99,99 RON`
- Plural: `un leu` / `doi lei` / `20 de lei` (the `de` rule applies to currency too!)
- ❌ €99.99 → ✅ **99,99 €** for euro contexts, or **99,99 lei** for Romanian currency

### Comma Rules

**NO comma before coordinating conjunctions** (și, sau, ori, fie):
- ❌ "Salvați fișierul, și închideți-l" → ✅ "Salvați fișierul și închideți-l"
- ❌ "Selectați limba, sau apăsați butonul" → ✅ "Selectați limba sau apăsați butonul"
- Exception: comma DOES precede `dar`, `însă`, `iar` (but/and-contrastive)

**ALWAYS comma before subordinating conjunctions:**
- că (that): "Am observat, că funcționează" — actually Romanian here is split; check style guide. Modern Romanian often DOES omit this comma. The safer rule is the one below:
- care / pe care (which / whom): "Fișierul, pe care l-ați selectat"
- dacă (if): "Apăsați aici, dacă doriți să continuați"
- pentru că / fiindcă (because): "Nu funcționează, fiindcă fișierul lipsește"
- când (when): "Notificați, când este gata"

## Terminology

| English | Preferred Romanian | Avoid (anglicism) |
|---|---|---|
| Click | clic / a face clic | click |
| Settings | setări / configurări | |
| User | utilizator | |
| Delete | a șterge | a deleta |
| Save | a salva | |
| Upload | a încărca | a uploada |
| Download | a descărca | a downloada |
| Log in | a se conecta / autentificare | a se logina |
| Log out | a se deconecta | |
| File | fișier | |
| Folder | dosar / folder (both acceptable) | |
| Dashboard | panou de control / tablou de bord | dashboard (acceptable) |
| Account | cont | account |
| Email | e-mail / email | |
| Browser | navigator / browser | |
| Link | legătură / link (both acceptable) | |
| Computer | calculator | |
| Screen | ecran | |
| Forward | a redirecționa | a forwarda |
| Scale | a extinde / a crește | a scala |
| Customize | a personaliza | a customiza |
| Process | a prelucra | a procesa |
| Implement | a pune în aplicare / a aplica | a implementa (acceptable in IT context) |
| Run (program) | a executa | a rula |

**False friends — CRITICAL (severity 2.0):**

| English | Wrong (false friend) | Correct Romanian | Romanian "false friend" means |
|---|---|---|---|
| actual | actual | **real / curent** | "actual" = current |
| eventually | eventual | **în final / în cele din urmă** | "eventual" = possible |
| to realize | a realiza | **a-și da seama** | "a realiza" = to achieve |
| to support | a suporta | **a oferi asistență / a sprijini** | "a suporta" = to tolerate |
| library | librărie | **bibliotecă** | "librărie" = bookstore |
| to assist (help) | a asista | **a ajuta** | "a asista" = to attend |
| sensible | sensibil | **rezonabil / sensat** | "sensibil" = sensitive |
| pretend | a pretinde | **a se preface** | "a pretinde" = to claim/demand |

**"per X" → "pe X" (severity 1.5):**

- ❌ "per limbă" (English calque) → ✅ "**pe limbă**" (per language)
- ❌ "per utilizator" → ✅ "**pe utilizator**" (per user)
- ❌ "per zi" → ✅ "**pe zi**" (per day) or "**zilnic**" (daily)

**Proper noun abbreviations in UI:**
- ✅ **SUA** / **Statele Unite** (NOT "Statele Unite ale Americii" in cramped UI)
- ✅ **Regatul Unit** / **Marea Britanie** (NOT the full official name)
- ✅ **UE** (Uniunea Europeană)

**Brand names with article suffix via hyphen:**
- ✅ "site-ul" (the site), "email-ul" (the email), "OneSky-ul" (the OneSky)
- ✅ "Google-ul" (rare; usually just "Google")

**Acronym plurals via hyphen:**
- ✅ URL-uri, API-uri, ID-uri (NOT URLs, APIs, IDs)

## Compound Adjective Anti-Patterns

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| IA-alimentat / AI-powered | **alimentat de IA / bazat pe IA** | "AI-powered" |
| context-conștient | **sensibil la context / contextual** | "context-aware" |
| utilizator-prietenos | **ușor de utilizat / intuitiv** | "user-friendly" |
| cloud-bazat | **bazat pe cloud / în cloud** | "cloud-based" |
| date-condus | **bazat pe date / orientat spre date** | "data-driven" |

## Calque / Anti-Pattern Blocklist

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| face sens | **are sens / este logic** | "makes sense" |
| la sfârșitul zilei | **în definitiv / în cele din urmă** | "at the end of the day" |
| a lua avantaj de | **a profita de** | "take advantage of" |
| a rula un program | **a executa un program** | "run a program" |
| pe o bază zilnică | **zilnic / în fiecare zi** | "on a daily basis" |
| în termeni de | **în ceea ce privește / din punct de vedere al** | "in terms of" |
| și mult mai mult | **și multe altele / și nu numai** | "and a lot more" |
| Plată de succes | **Plată finalizată / Plată efectuată** | "Payment successful" (calque) |
| Te rog rupe un picior | **Noroc! / Să-ți meargă bine!** | "break a leg" |
| O bucată de prăjitură | **E floare la ureche! / E simplu ca bună ziua** | "piece of cake" |
| 25+ limbi | **peste 25 de limbi** | "25+ languages" |
| +{count} mai multe | **și încă {count}** | "+{count} more" |

## Block Verb Mood Consistency (severity 2.0)

When a heading/title sets a verb mood, child items must match:

| Title mood | Item mood | Example |
|---|---|---|
| Conditional ("Ce ați obține:") | Conditional or noun phrase | "Ați primi o propunere..." or "Propunere..." |
| Instructional ("Pași de urmat:") | Imperative or infinitive | "Configurați contul..." or "Configurarea contului..." |
| Question ("Ce vreți să faceți?") | Infinitive options | "Salvare", "Anulare" |

- ❌ Title: "Ce ați obține:" (conditional) + Item: "Primiți o propunere..." (imperative) — mood mismatch
- ✅ Title: "Ce ați obține:" + Item: "**Ați primi** o propunere..." (matching conditional)

## Self-Check Checklist

Run BEFORE finalizing each translation:

**Accuracy (critical):**
- [ ] **Three-gender system:** masc / fem / NEUTER (un sistem → sistemele; un fișier → fișierele)
- [ ] **Postposed definite article:** utilizatorul, pagina, fișierele (not bare utilizator/pagină/fișiere as subject)
- [ ] **Genitive-dative:** folderul proiectului, pagina utilizatorului (NOT folder proiect)
- [ ] **Article completeness:** Eroarea aplicației (NOT Eroare de aplicație) for specific entities
- [ ] **Adjective agreement:** gender + number (sisteme noi, pagini noi, fișiere importante)
- [ ] **All 5 diacritics:** ă â î ș ț preserved
- [ ] **Comma-below (Ș/Ț) not cedilla (Ş/Ţ):** Unicode-correct characters
- [ ] **ICU plurals:** one / few / other with **"de"** before noun for 20+ (20 de fișiere, NOT 20 fișiere)
- [ ] **Quotation marks:** „..." not "..."
- [ ] **Number format:** 1.234,56 (period thousands, comma decimal)
- [ ] **Date format:** DD.MM.YYYY or 15 ianuarie 2024
- [ ] **Currency:** 99,99 lei (RON, NOT in eurozone)
- [ ] **Conjunction commas:** no comma before și/sau/ori; comma before dar/care/dacă/fiindcă
- [ ] **Placeholders preserved** exactly

**Naturalness:**
- [ ] **Dumneavoastră/tu consistency** — possessives, verbs, imperatives all same level
- [ ] **2nd-plural verbs with Dumneavoastră** (puteți, NOT poți)
- [ ] **Imperative buttons** (Salvați, Ștergeți) — or infinitive (Salvare, Ștergere) for menu labels
- [ ] **Reflexive passive for status** (Se salvează..., NOT Salvat...)
- [ ] **Participial completion** (Plată finalizată, NOT Plată de succes)
- [ ] **Existential empty states** (Nu există X, Niciun X — NOT Nu au fost selectate X)
- [ ] **False friends avoided** (real not actual; în final not eventual; a-și da seama not a realiza; a oferi asistență not a suporta)
- [ ] **Native verbs** (a șterge, a încărca, a descărca, a extinde, a personaliza, a prelucra — NOT a deleta, a uploada, a downloada, a scala, a customiza, a procesa)
- [ ] **"pe X" not "per X"** (pe limbă, pe utilizator)
- [ ] **Compound adjectives natural** (bazat pe IA, sensibil la context, ușor de utilizat — NOT IA-alimentat, context-conștient, utilizator-prietenos)
- [ ] **Drag-and-drop:** trageți, plasați, eliberați (NOT drag, drop)
- [ ] **Abbreviations in UI** (SUA, UE, Regatul Unit — not full names)
- [ ] **Block verb mood matches** title/heading
- [ ] **No redundant "de" chains** ("produse de îngrijire de noapte" — restructure with adjective "îngrijire nocturnă")
- [ ] **"peste 25 de limbi" not "25+ limbi"**

## Worked Examples

### Example 1 — Save button + status

**Source:**
> Save  
> Saving your changes...  
> Changes saved successfully.

**Wrong:**
> Salvare (infinitive — OK but imperative preferred for action button)  
> Salvat... (past — wrong tense)  
> Modificările au fost salvate cu succes. (verbose "cu succes" calque)

**Correct:**
> **Salvați** (imperative button — or `Salvare` for menu/option)  
> **Se salvează modificările...** (reflexive passive for ongoing)  
> **Modificările au fost salvate.** / **Modificări salvate.** (participle, no "de succes")

### Example 2 — Files counter with ICU and the "de" rule

**Source:**
> {count, plural, one {# file} other {# files}}

**Correct Romanian ICU (3 branches):**
```
{count, plural,
  one {# fișier}
  few {# fișiere}
  other {# de fișiere}
}
```

Examples:
- 1 fișier (one branch)
- 5 fișiere (few branch — no `de`)
- 20 **de** fișiere (other branch — `de` mandatory)
- 100 **de** fișiere (other branch)
- 115 fișiere (few branch — last two digits 1-19, no `de`)

### Example 3 — Neuter gender catastrophe

**Source:**
> The system is new. The systems are new.

**Wrong:**
> O sistem este nouă. Sistemii sunt noi. (fem article + fem adj for singular; masc plural for neuter — both broken)

**Correct:**
> **Un sistem nou** (un = masc/neuter sg article + masc/neuter sg adj) — but if "the":  
> **Sistemul este nou.** (sg with neuter article = masc-like)  
> **Sistemele sunt noi.** (pl with neuter article = fem-like; adj "noi" is the pl form)

### Example 4 — Postposed article

**Source:**
> The user was deleted. / The page is not available.

**Wrong:**
> Utilizator a fost șters. / Pagină nu este disponibilă. (bare nouns)

**Correct:**
> **Utilizatorul** a fost șters. / **Pagina** nu este disponibilă. (with postposed article)

### Example 5 — Genitive between nouns

**Source:**
> User's page / Application error / Connection status

**Wrong:**
> Pagina utilizator / Eroare aplicație / Stare conexiune (bare juxtaposition)

**Correct:**
> **Pagina utilizatorului** / **Eroarea aplicației** / **Starea conexiunii** (with genitive)

### Example 6 — Drag-and-drop area

**Source:**
> Drag and drop files here, or click to browse

**Wrong:**
> Drag and drop fișiere aici, sau click pentru a naviga (English verbs + comma before sau)

**Correct:**
> **Trageți și plasați fișierele aici sau apăsați pentru a naviga** (native verbs, no comma before sau)

### Example 7 — Empty state

**Source:**
> No languages selected / No results found

**Wrong (passive calque):**
> Nu au fost selectate limbi / Nu au fost găsite rezultate

**Correct (existential):**
> **Nu există limbi selectate** / **Nicio limbă selectată**
> **Nu există rezultate** / **Niciun rezultat**

### Example 8 — False friend

**Source:**
> The actual file is not available. We will eventually fix this.

**Wrong (false friends):**
> Fișierul actual nu este disponibil. Vom remedia eventual aceasta. (= "current file is unavailable. We may possibly fix this")

**Correct:**
> **Fișierul real nu este disponibil. Vom remedia aceasta în final.** (real = "actual"; în final = "eventually")

### Example 9 — Native verb preference

**Source:**
> Scale your operations / Customize the dashboard / Process the data

**Wrong (anglicisms):**
> Scalați operațiunile / Customizați tabloul de bord / Procesați datele

**Correct:**
> **Extindeți operațiunile / Creșteți operațiunile** / **Personalizați tabloul de bord** / **Prelucrați datele**

### Example 10 — "per X" → "pe X"

**Source:**
> Price per user / Limit per language

**Wrong:**
> Preț per utilizator / Limită per limbă (English calque)

**Correct:**
> **Preț pe utilizator** / **Limită pe limbă**

### Example 11 — Completion participle

**Source:**
> Payment successful / Upload complete / Login successful

**Wrong (calque):**
> Plată de succes / Încărcare completă / Conectare de succes

**Correct (participial):**
> **Plată efectuată** / **Plată finalizată** / **Încărcare finalizată** / **Conectare reușită** / **Conectat**

### Example 12 — Comma-below not cedilla

**Source / Wrong (cedilla — Turkish characters):**
> Ştergere configuraţii (Ş and ţ with cedilla — Unicode wrong)

**Correct (comma-below):**
> **Ștergere configurații** (Ș and ț with comma-below)

## When in Doubt

1. **Gender unclear?** Check the noun ending:
   - `-or`, `-or`, `-u` (and most consonant-final masculine animates) → masculine: un utilizator
   - `-ă`, `-e` → feminine: o pagină, o cheie
   - Most tech terms with no specific ending → **neuter** (un sistem, un fișier, un computer)
2. **Plural form unclear?**
   - Masc: usually `-i` (utilizator → utilizator**ii**)
   - Fem: `-e` or `-i` depending on stem (pagină → pagin**i**; aplicație → aplicați**i**)
   - Neuter: take fem-like `-e` or `-uri` (fișier → fișier**e** → fișier**ele**)
3. **Definite article unclear?**
   - Masc/Neuter sg: `-ul` (utilizator → utilizatorul)
   - Fem sg: `-a` (pagină → pagina)
   - Masc pl: `-i` (utilizatori → utilizatorii)
   - Fem/Neuter pl: `-le` (pagini → paginile; fișiere → fișierele)
4. **Genitive unclear?**
   - Take the definite form, swap article: `-ul` → `-ului`; `-a` → `-ei`; `-le` → `-lor`
5. **`de` in plural?** Insert before noun when number is 20+ (or generally outside 1-19 last digits).
6. **`actual`?** Means "current". For English "actual" use **real** or **curent**.
7. **`eventual`?** Means "possible". For English "eventually" use **în final** or **în cele din urmă**.
8. **`per X`?** Use **`pe X`**. Always.
9. **`a` + English verb stem + `-a`?** Almost always wrong (a deleta, a uploada, a downloada, a scala, a customiza, a procesa). Find the native Romanian verb.
10. **`Ș`/`Ț` with cedilla?** Use **comma-below** Unicode characters (U+0218–U+021B). Cedilla forms (U+015E, U+015F, U+0162, U+0163) are Turkish.
11. **Diacritic uncertain?** Look up the word. Romanian rarely has unmarked variants where marked exists.
12. **"de succes"?** Almost always a calque. Use participial form (finalizată, efectuată).
13. **Empty state?** Use **Nu există X** or **Niciun X / Nicio X** (one word, not nici un).

Romanian's distinctive features (postposed article, neuter, genitive case, `de` plural) mean that surface-level word swaps produce broken Romanian. When the translation feels off, check first: gender assignment, postposed article on subjects, genitive between nouns, ICU plural with `de`.
