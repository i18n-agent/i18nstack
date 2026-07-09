---
name: localize-ca
description: Use when translating or localizing UI strings, marketing copy, blogs, docs, error messages, or any product text into Catalan (Català) for Catalonia, Valencia (as Valencià), the Balearic Islands, or Andorra. Catalan is NOT Spanish — it is a distinct Romance language closer to Occitan and Old Provençal. Enforces the unique geminated L (l·l with INTERPUNCT), ç (c-cedilla) before a/o/u, mandatory apostrophe elision (l'aigua, d'ahir), open/closed accent direction (à/è/é/í/ò/ó/ú), the periphrastic past (vaig + infinitive — unique to Catalan), the weak pronoun system with partitive `en` and locative `hi`, vostè/tu formality consistency, EUR currency with European 1.234,56 € format, DD/MM/YYYY dates with lowercase Catalan months (gener, febrer, març…), Latin quotation marks «...», NO inverted ¿¡ at sentence start (UNLIKE Spanish), no comma before i/o, infinitive button labels (Desar, Cancel·lar), and — most critically — heavy anti-Spanish-calque discipline (desar NOT guardar, arxiu/fitxer NOT archivo, ordinador NOT ordenador, llavors NOT entonces, però NOT pero, dimecres NOT miércoles, treball/feina NOT trabajo, ratolí NOT ratón, parlar NOT hablar, cercar/buscar NOT buscar-as-Spanish, menjar NOT comer, oblidar NOT olvidar, tarda NOT tarde). Catalan has a political identity dimension — clean Catalan without Spanish slippage is a respect signal.
---

# Localize: Catalan (ca → Català)

Distilled from the production translation prompt (`ca.ts`). Catalan is a co-official language of Spain (Catalonia, Valencia, Balearic Islands), the sole official language of **Andorra** (the only sovereign state where Catalan is the official language), and is also spoken in Alghero (Sardinia), Roussillon (southern France), and the Franja in Aragon. ~10 million speakers.

Catalan looks superficially Spanish at first glance, but it is genealogically and structurally distinct — closer to Occitan than to Spanish. Treating it as "Spanish with funny letters" is the single most common quality failure.

## Mindset

> Ets un escriptor català natiu extremadament exigent que odia les construccions poc naturals en català, com ara traduccions literals de l'anglès o el castellà, o formulacions maldestres.

Reject literal English calques. Reject literal Spanish calques (which are subtle and far more common because Catalan speakers are bilingual and constantly exposed to Spanish). Preserve original meaning while restructuring fully into natural Catalan. Common English terms (API, token, software) are acceptable when no native Catalan equivalent exists.

---

## Scope & Variants

Catalan has multiple regional standards. For UI/SaaS/business content, **use general Catalan (IEC standard, Barcelona-based)** unless the user requests otherwise.

| Variant | Code | Region | Standard | Notes |
|---------|------|--------|----------|-------|
| **General Catalan / Central** | `ca` / `ca-ES` | Catalonia (Barcelona) | IEC (Institut d'Estudis Catalans) | DEFAULT. Used for software, news, business, education. |
| **Valencian** | `ca-valencia` / `ca-ES-valencia` | Valencia | AVL (Acadèmia Valenciana de la Llengua) | Same language linguistically; some vocabulary and accent direction differences. |
| **Balearic** | `ca-ES-balear` | Mallorca, Menorca, Eivissa | IEC, with dialectal forms | Uses `salat` article forms (es, sa, ses) colloquially; standard IEC in writing. |
| **Andorran** | `ca-AD` | Andorra | IEC | Andorra is the only sovereign state where Catalan is the sole official language. Euro currency. |

**Default behavior:** Unless the user specifies, target **general Catalan (IEC standard)**. This is what works for Catalonia, Andorra, and most pan-Catalan business/SaaS audiences. Avoid excessive valencianismes or balearismes.

**When the user requests Valencian (ca-valencia):**
- Use `meua/teua/seua` (Valencian) instead of `meva/teva/seva` (Central) — both forms are correct IEC, but the Valencian forms are characteristic.
- Vocabulary: `eixir` (Valencian) vs `sortir` (Central) — both mean "to exit/leave".
- `vore` (Valencian colloquial) vs `veure` (standard) — prefer standard `veure` even in Valencian unless the tone is conversational.
- Verb endings: 1st-person present `parle` (Valencian) vs `parlo` (Central). For UI buttons (infinitive), this doesn't matter.
- AVL accepts certain spellings IEC also accepts; do not introduce divergent orthography.

**When the user requests Balearic:**
- In FORMAL/UI writing, use the same IEC standard as Central Catalan.
- Avoid the colloquial `salat` article (`es/sa/ses` instead of `el/la/els/les`) — it is conversational, not written-register.
- Vocabulary: `al·lot/al·lota` (boy/girl), `bunyol` etc. — only in cultural/regional content.

**When in doubt: use general Catalan (IEC) — it is mutually intelligible across all regions and is what the Catalan Wikipedia, Vilaweb, TV3, and major SaaS products use.**

---

## Identity Guardrail — Catalan is NOT Spanish

This is the most important section of this skill. Catalan speakers are bilingual with Spanish, and Spanish-language influence constantly bleeds into spoken Catalan. **Native Catalan readers immediately spot Spanish calques, and they read as either uneducated or — in some political contexts — as actively disrespectful of the language.**

Catalan is a **Western Romance language**, sister to Occitan, descended from Vulgar Latin spoken in the Marca Hispànica (the buffer zone between the Carolingian Empire and Al-Andalus). It is **NOT** a dialect of Spanish, **NOT** descended from Spanish, and **NOT** "Spanish with some French mixed in".

### Genealogy

```
                    Vulgar Latin
                        |
        +---------------+----------------+
        |               |                |
   Gallo-Romance    Ibero-Romance    Italo-Romance
        |               |
   Occitan         Spanish (Castilian)
        |               |
   CATALAN ----- (areal contact, not descent)
        |
   Valencian, Balearic, Andorran, Algherese
```

Catalan and Occitan were nearly the same language in the 12th-13th century (troubadour literature). The Catalan-Spanish split is geographical (Pyrenees / Crown of Aragon vs Crown of Castile), not genealogical.

### Visual disambiguation

| Feature | Catalan | Spanish |
|---------|---------|---------|
| Geminated L | **`l·l`** (interpunct) | not used |
| Opening punctuation | `?` `!` at END only | **`¿`** `¡` at start AND end |
| "the" before vowel | **`l'aigua`** (apostrophe) | `el agua` |
| "of the" | **`del`** / **`dels`** / **`de la`** | `del` / `de la` |
| Future-tense periphrasis | `vaig + infinitive` = PAST | `voy a + infinitive` = FUTURE (!) |
| Word for "save (file)" | **`desar`** | `guardar` |
| Word for "file" | **`arxiu`** / **`fitxer`** | `archivo` |
| Word for "computer" | **`ordinador`** | `ordenador` (Spain) / `computadora` (LATAM) |
| Word for "mouse" | **`ratolí`** | `ratón` |
| Word for "but" | **`però`** | `pero` |
| Word for "then" | **`llavors`** / **`aleshores`** | `entonces` |
| Word for "something" | **`alguna cosa`** | `algo` |
| Word for "work" | **`treball`** / **`feina`** | `trabajo` |
| Word for "to speak" | **`parlar`** | `hablar` |
| Word for "to eat" | **`menjar`** | `comer` |
| Word for "Wednesday" | **`dimecres`** | `miércoles` |
| Word for "afternoon" | **`tarda`** | `tarde` |

### The CRITICAL false-friend trap: `vaig`

`vaig anar` in Catalan = "I went" (past).
`voy a ir` in Spanish = "I am going to go" (future).

If you confuse these you will mistranslate the entire tense of the sentence. This is the #1 trap for Spanish speakers learning Catalan.

### Political dimension (be aware)

Catalan has a strong political-identity dimension because of the independence movement and historical suppression under Franco (1939-1975, when public use of Catalan was banned). Many users perceive Spanish slippage in Catalan UI as either:
- **At best:** lazy / Google-Translate-from-Spanish
- **At worst:** politically dismissive of the language

**Clean Catalan without Spanish slippage is a respect signal.** Do not see this as optional polish — it is core to passing the native-speaker test.

---

## Register (vostè / tu)

Catalan uses a two-level formality system. Choose ONE and stay consistent throughout the file.

### vostè (formal — defaults for B2B / admin / business)

- **Pronoun:** `vostè` (singular), `vostès` (plural)
- **Verb conjugation:** 3rd person (LIKE SPANISH `usted`, NOT like French `vous`). `Vostè pot...`, `Vostè ha de...`
- **Possessives:** `el seu` / `la seva` / `els seus` / `les seves`
- **Imperatives:** 3rd person subjunctive form. `Desi`, `Cancel·li`, `Faci clic`, `Esperi`, `Enviï`
- **Direct address pronoun:** `el/la` ("you"): `L'ajudarem.` (We will help you.)

### tu (informal — defaults for consumer apps / modern tech)

- **Pronoun:** `tu` (singular), `vosaltres` (plural)
- **Verb conjugation:** 2nd person. `Pots...`, `Has de...`
- **Possessives:** `el teu` / `la teva` / `els teus` / `les teves`
- **Imperatives:** 2nd person. `Desa`, `Cancel·la`, `Fes clic`, `Espera`, `Envia`
- **Direct address pronoun:** `et` ("you"): `T'ajudarem.`

### Mixing is the #1 native-test failure

```
❌ Vostè pot modificar les teves configuracions
   (formal pronoun + informal possessive)

✅ Vostè pot modificar les seves configuracions
✅ Tu pots modificar les teves configuracions
```

### Register Auto-Detection

If the user has NOT specified `tu` or `vostè`, infer from source register.

**Formal source signals → `vostè`:**
- "please", "kindly", "we recommend", hedged modals
- Banking, legal, government, B2B SaaS, healthcare, insurance, enterprise
- No contractions, no exclamations, no emoji
- Third-person distance ("the user must", "applicants should")

**Informal source signals → `tu`:**
- Contractions: "don't", "you'll", "we're"
- "hey", "hi there", emoji (🎉 🚀 ✨)
- Consumer apps, gaming, social, lifestyle, fitness
- Sentence fragments, conversational filler

**Mixed/ambiguous → default to `vostè`.** Vostè reads professional and safe; `tu` can read as disrespectful in business or government contexts.

**Buttons stay infinitive regardless of register** — `Desar` works for both `tu` and `vostè`, sidestepping the formality choice entirely. Use imperative ONLY in instructional/help text where the choice is locked.

---

## Critical Hard Rules

### 1. Geminated L: **`l·l`** with INTERPUNCT (mid-dot, U+00B7)

This is **unique to Catalan among major Romance languages** and the single strongest "native" marker. Severity 2.5.

| Wrong | Correct |
|-------|---------|
| `intelligent` (looks English) | **`intel·ligent`** |
| `colaborar` (looks Spanish) | **`col·laborar`** |
| `paralel` | **`paral·lel`** |
| `il.lustració` (PERIOD instead of interpunct) | **`il·lustració`** |
| `colegi` | **`col·legi`** |
| `instal.lar` | **`instal·lar`** |
| `excel.lent` | **`excel·lent`** |
| `pel.lícula` | **`pel·lícula`** |
| `nul-la` (hyphen) | **`nul·la`** |

**The interpunct character is `·` (U+00B7, MIDDLE DOT), NOT a period (`.`), NOT a hyphen (`-`), NOT a katakana dot (`・`).** Many writing systems will autocorrect to a period — DO NOT accept that.

Common words requiring `l·l`: `intel·ligent`, `col·laborar`, `col·lecció`, `col·lectiu`, `col·legi`, `excel·lent`, `il·lustració`, `il·lusió`, `il·legal`, `il·limitat`, `instal·lació`, `instal·lar`, `mil·lenni`, `mil·límetre`, `nul·la`, `paral·lel`, `pel·lícula`, `síl·laba`, `tranquil·litat`.

### 2. ç (c-cedilla) before a, o, u

Catalan uses **`ç`** to mark a `/s/` sound before `a`, `o`, `u`. Without the cedilla, the letter `c` before those vowels would be `/k/`.

| Wrong | Correct | Meaning |
|-------|---------|---------|
| `forca` | **`força`** | force, strength |
| `placa` | **`plaça`** | square (place) |
| `faca` | **`faça`** | face (Valencian) |
| `comenca` | **`comença`** | begins |
| `lliconaria` | **`lliçó`** | lesson |

**Note:** Before `e` and `i`, plain `c` is already `/s/`, so no cedilla is needed (`cel`, `cinc`).

End-of-word `-ç` is also common: `feliç`, `dolç`, `audaç`, `vidriós`, `peix` (no — that's a different sound; `peix` uses `x`).

### 3. Apostrophe elision (mandatory)

Definite articles, prepositions, and weak pronouns elide before vowels and silent `h-`.

| Combination | Becomes | Example |
|-------------|---------|---------|
| `el` / `la` + vowel/`h-` | **`l'`** | `el aigua` → **`l'aigua`** (water); `la història` → **`l'història`** WAIT — see below |
| `de` + vowel/`h-` | **`d'`** | `de ahir` → **`d'ahir`** (of yesterday) |
| `que` + vowel | **`qu'`** | rarely written; mostly oral |
| `em / et / es / el / la / ens / us / els / les` + vowel | **`m' / t' / s' / l' / l'`** | `em ajuda` → **`m'ajuda`** |
| `ho` (weak pronoun) — no elision | stays `ho` | `que ho` stays `que ho` |

**Feminine `la` elision exception (CRITICAL):** Feminine `la` does **NOT** elide before unstressed `i-` or `u-` (because the resulting sequence would be ambiguous). So:
- `la història` → **`la història`** (stays — unstressed `i-`)
- `la universitat` → **`la universitat`** (stays — unstressed `u-`)
- `la idea` → **`la idea`** (stays — unstressed `i-`)
- `la àvia` → **`l'àvia`** (elides — stressed `à-`)
- `la hora` → **`l'hora`** (elides — `h-` is silent, the underlying vowel `o-` is stressed)
- `la imatge` → **`la imatge`** (stays — unstressed `i-`)

Masculine `el` ALWAYS elides before vowel or silent `h-`: `l'arxiu`, `l'usuari`, `l'home`, `l'objecte`.

### 4. Article contractions: `al`, `del`, `pel`

| Combine | → | Example |
|---------|---|---------|
| `a` + `el` | **`al`** | `anar al sistema` |
| `a` + `els` | **`als`** | `als usuaris` |
| `de` + `el` | **`del`** | `del sistema` |
| `de` + `els` | **`dels`** | `dels arxius` |
| `per` + `el` | **`pel`** | `pel sistema` |
| `per` + `els` | **`pels`** | `pels usuaris` |

**No contraction with elided `l'`:**
- `a` + `l'` → **`a l'`** (NOT `al`'): `a l'usuari`, `a l'arxiu`
- `de` + `l'` → **`de l'`** (NOT `del`'): `de l'aplicació`, `de l'usuari`
- `per` + `l'` → **`per l'`**

### 5. Open vs closed accents — direction matters

Catalan distinguishes open (low, `\` grave) and closed (high, `/` acute) vowels in stressed syllables. Wrong accent direction is a **literacy marker** — native readers spot it immediately.

| Vowel | Open (grave `\`) | Closed (acute `/`) |
|-------|------------------|---------------------|
| **a** | `à` (always open) | — |
| **e** | `è` | `é` |
| **i** | — | `í` (always closed) |
| **o** | `ò` | `ó` |
| **u** | — | `ú` (always closed) |

**Rules of thumb:**
- `à` and `í` and `ú` always go grave/acute respectively — no ambiguity.
- `è` vs `é`: open `è` in `cafè`, `però`, `èxit`, `mèrit`, `àlgebra`. Closed `é` in `també`, `francés` (Valencian) / `francès` (Central — note: `francès` is grave in Central).
- `ò` vs `ó`: open `ò` in `història`, `memòria`, `pròxim`. Closed `ó` in `només`, `cançó`, `acció`, `informació`.

**Common mistakes to catch:**
- ❌ `cafè` written as `café` (that's Spanish; Catalan needs grave)
- ❌ `història` written as `história` (closed accent is Spanish; Catalan is open `ò`)
- ❌ `però` written as `pero` (no accent = Spanish "but"; Catalan needs grave `ò`)

### 6. Periphrastic past with `vaig` + infinitive (UNIQUE TO CATALAN)

Catalan's standard past tense for completed actions is the **periphrastic perfective**: `vaig` + infinitive.

| English | Wrong (archaic / Spanish-calque) | Correct (periphrastic) |
|---------|----------------------------------|------------------------|
| I saved | `desí` (archaic — exists but not used) | **`vaig desar`** |
| You saved | `desares` / `guardaste` (Spanish) | **`vas desar`** |
| He/she/it saved | `desà` (archaic) | **`va desar`** |
| We saved | `desàrem` (archaic) | **`vam desar`** / **`vàrem desar`** |
| You (pl) saved | `desàreu` (archaic) | **`vau desar`** / **`vàreu desar`** |
| They saved | `desaren` (archaic) | **`van desar`** / **`varen desar`** |

The simple preterite (`desí`, `desàrem`, etc.) exists in formal/literary writing but **virtually all modern Catalan uses the periphrastic form**. This periphrastic past is **unique to Catalan** among Romance languages — no other Romance language uses an auxiliary + infinitive for the perfective past.

**The trap for Spanish speakers:** `vaig + inf` looks identical in form to Spanish `voy a + inf` ("I am going to..." = FUTURE). It is the OPPOSITE tense. Watch for this constantly.

### 7. Weak pronoun system (em / et / es / el / la / li / els / les / ho / en / hi)

Catalan has a rich set of weak (clitic) pronouns. They attach to verbs in specific patterns. The two that don't exist in Spanish and are signature-Catalan:

#### Partitive `en` (replaces de + noun, or quantified noun)

| Long form | With `en` | Meaning |
|-----------|-----------|---------|
| Tinc dos llibres | **En tinc dos** | I have two (of them) |
| He comprat pa | **N'he comprat** | I bought some |
| Parla de feina | **En parla** | He/she talks about it |

#### Locative `hi` (replaces a/en + place, or ablative)

| Long form | With `hi` | Meaning |
|-----------|-----------|---------|
| Vaig a Barcelona | **Hi vaig** | I'm going there |
| He pensat en això | **Hi he pensat** | I've thought about it |
| Visc a Catalunya | **Hi visc** | I live there |

These are not optional — omitting them sounds Spanish-influenced. `Vaig (sense `hi`)` for "I go (there)" is calque from Spanish "Voy".

#### Elision in weak pronouns

Same as articles: `em` → `m'`, `et` → `t'`, `es` → `s'`, `el` → `l'`, `la` → `l'`, `ens` → `'ns`, `us` → `us` (stays), `els` → `'ls`, `en` → `n'`, `hi` → no elision.

Position depends on verb form:
- Conjugated finite verb: pronoun goes BEFORE — `El veig`, `Ho sé`, `M'agrada`.
- Imperative / infinitive / gerund: pronoun goes AFTER, attached with hyphen — `Veure'l`, `Sabent-ho`, `Mira'm`.

### 8. NO inverted `¿` or `¡` at sentence start (UNLIKE Spanish)

Catalan uses only the closing `?` and `!` — like English, French, and Italian.

| Wrong (Spanish-style) | Correct (Catalan) |
|-----------------------|-------------------|
| `¿Voleu continuar?` | **`Voleu continuar?`** |
| `¡Error!` | **`Error!`** |
| `¿Quina hora és?` | **`Quina hora és?`** |
| `¡Compte!` | **`Compte!`** |

This is the **single most visible Spanish-calque error** to a Catalan reader. The inverted marks are diagnostic of "this person ran a Spanish translation through find-replace".

### 9. Comma rules

| Rule | Wrong | Correct |
|------|-------|---------|
| NO comma before `i` (and) | `Arrossegueu aquí, i feu clic` | **`Arrossegueu aquí i feu clic`** |
| NO comma before `o` (or) | `Arrossegueu, o feu clic` | **`Arrossegueu o feu clic`** |
| NO comma before `ni` (nor) | `No vull, ni puc` | **`No vull ni puc`** |
| Comma BEFORE `però` (but) | `És senzill però eficaç` | **`És senzill, però eficaç`** |
| Comma BEFORE `sinó` (but rather) | `No feu clic sinó arrossegueu` | **`No feu clic, sinó arrossegueu`** |
| Comma BEFORE subord. `que` (when introducing a clause) | context-dependent | `Crec, que vindrà` is wrong → **`Crec que vindrà`** (no comma); but `Tan ràpid, que no ho vaig veure` (consecutive) has comma |
| Comma BEFORE `perquè` (because), `si` (if), `quan` (when) | when subord. clause is preposed | `Si plou no vindrem` → **`Si plou, no vindrem`** |

---

## UI Conventions

### Buttons — infinitive form (industry standard)

| Wrong | Correct |
|-------|---------|
| `Deseu` (imperative — implies vostè) | **`Desar`** |
| `Desa` (imperative — implies tu) | **`Desar`** |
| `Cancel·leu` | **`Cancel·lar`** |
| `Eliminar el Projecte` (Title Case) | **`Eliminar el projecte`** (sentence case) |
| `Confirma` | **`Confirmar`** |
| `Registreu-vos` | **`Registrar-se`** / **`Crear compte`** |

Infinitive sidesteps the `tu`/`vostè` choice entirely. **Sentence case** (only first word capitalized) is standard — NOT Title Case.

### Status messages — gerund (-ant / -ent / -int)

| Wrong | Correct |
|-------|---------|
| `Desar...` (infinitive doesn't mean "in progress") | **`Desant...`** |
| `Carrega...` | **`Carregant...`** |
| `Processa...` | **`Processant...`** |
| `Enviar...` | **`Enviant...`** |
| `S'ha creat {date}` (full sentence in label) | **`Creat el {date}`** (concise label) |

### Completion messages — participial / verbal (NOT `exitós`)

`Exitós` is a calque from English "successful". Catalan prefers participial completion forms.

| Wrong | Correct |
|-------|---------|
| `Pagament exitós` | **`Pagament completat`** / **`Pagament realitzat`** / **`Fet!`** |
| `Càrrega exitosa` | **`Càrrega completada`** / **`Fitxer pujat`** / **`Llest!`** |
| `Operació exitosa` | **`Operació completada`** / **`Llest!`** |
| `Descàrrega completa` | **`Descàrrega completada`** / **`Descàrrega finalitzada`** |
| `Operació completa` (adjective) | **`Operació completada`** (participle) |

### Empty state — `No hi ha X` (existential)

Catalan prefers the existential `No hi ha` construction over passive `No s'han...`.

| Wrong (passive calque) | Correct (existential) |
|------------------------|------------------------|
| `No s'han seleccionat idiomes` | **`No hi ha idiomes seleccionats`** |
| `No s'han trobat resultats` | **`No hi ha resultats`** |
| `No s'han carregat fitxers` | **`No hi ha fitxers carregats`** |
| `Sense dades disponibles` | **`No hi ha dades disponibles`** |
| `No s'ha seleccionat cap arxiu` (double negative OK) | **`No hi ha cap arxiu seleccionat`** |

### Drag and drop

| English | Catalan |
|---------|---------|
| drag | **`arrossegar`** |
| drop / release (let go) | **`deixar anar`** (NOT `alliberar`, which means "to liberate") |
| browse (file picker) | **`Seleccionar fitxer`** / **`Triar fitxer`** (NOT `Explorar`) |
| Standard phrase | **`Arrossegueu i deixeu anar`** |

```
❌ Arrossegueu i dropeu (calque)
✅ Arrossegueu i deixeu anar

❌ Alliberar per pujar (alliberar = liberate, wrong sense)
✅ Deixeu anar per pujar
```

### FOR vs PER — `per` vs `per a`

This is one of the most disputed points in modern Catalan orthography. Two camps:

- **Fabrian / IEC traditional:** distinguish `per` (cause / rate / agent) vs `per a` (purpose / destination / time period). `Servei per a empreses`, `Tres minuts per idioma`.
- **Coromines / Solà reform:** use `per` everywhere before infinitives. `Servei per empreses`, `Per arribar a temps`.

**Default behavior:** Follow IEC traditional (use `per a` for purpose/destination/recipient). This matches major publications (TV3, Vilaweb) and is the safer choice for formal/business content.

| Sense | Use | Example |
|-------|-----|---------|
| Rate ("per X") | `per` | **`per idioma`** (per language) |
| Cause / agent | `per` | `causat per l'usuari` |
| Total / recipient ("for X") | `per a` | **`per a 5 idiomes`** |
| Purpose (before infinitive) | `per` (Fabra) or `per a` (Coromines) | `per traduir` or `per a traduir` — IEC accepts both |
| Time period | `per a` | `tancat per a la nit` |

### Quantity expressions

| Wrong (calque) | Correct |
|----------------|---------|
| `25+ idiomes` | **`més de 25 idiomes`** |
| `+{count} més` | **`i {count} més`** |
| `25 idiomes o més` (works, but `més de` more natural) | **`més de 25 idiomes`** |

### Capitalization

- **Sentence case** in buttons, headings, labels: `Eliminar el projecte`, `Configuració del compte`.
- Months and days: **lowercase** — `gener`, `dilluns` (see Dates section).
- Languages: **lowercase** — `català`, `castellà`, `anglès`, `francès`.
- Nationality nouns: **lowercase** — `un català`, `una catalana`.
- Proper nouns and place names: capitalized — `Catalunya`, `Barcelona`, `Andorra`, `País Valencià`.

### UI labels in prose

| Wrong | Correct |
|-------|---------|
| `el camp de nom` | **`el camp «Nom»`** or `el camp Nom` |
| `la pestanya dels comptes` | **`la pestanya «Comptes»**` |

---

## Punctuation, Numbers, Dates, Currency

### Quotation marks

- **Primary (traditional / formal):** `«...»` (Latin guillemets / cometes llatines): `«hola»`
- **Digital / casual:** straight `"..."` is acceptable but less native
- **Inner quotes:** "..." inside «...» or vice versa
- **Avoid** curly English quotes `"..."` `'...'` in formal Catalan writing

### Numbers

- **Decimal separator:** comma `,` — `3,14`
- **Thousands separator:** period `.` — `1.234`
- **Combined:** `1.234,56`
- **No separator** for years (`2026`, NOT `2.026`) or invoice numbers
- **Space-separated** for 5+ digit numbers is also acceptable: `12 345` — but `12.345` is more common

| Wrong | Correct |
|-------|---------|
| `1,234.56` (English format) | **`1.234,56`** |
| `99.99 €` | **`99,99 €`** |
| `3.14` | **`3,14`** |

### Dates

- **Numeric:** `DD/MM/YYYY` — `15/01/2024`, `25/05/2026`
- **Long form:** `15 de gener de 2024` (note: `de` before month, `de` before year — the second `de` becomes `d'` before vowel-starting year: `d'aquest any`)
- **Months are LOWERCASE:** gener, febrer, març, abril, maig, juny, juliol, agost, setembre, octubre, novembre, desembre

| Month | English | Notes |
|-------|---------|-------|
| **gener** | January | from Latin Ianuarius |
| **febrer** | February | |
| **març** | March | NOTE: `ç` |
| **abril** | April | |
| **maig** | May | |
| **juny** | June | |
| **juliol** | July | |
| **agost** | August | |
| **setembre** | September | NOTE: no `p` (unlike Spanish `septiembre`) |
| **octubre** | October | |
| **novembre** | November | |
| **desembre** | December | NOTE: `desembre` with `s`, not `decembre` |

### Days of week (lowercase)

All start with `di-` (literally "day of-"):

| Day | English |
|-----|---------|
| **dilluns** | Monday (`di-` + Luna = day of the Moon) |
| **dimarts** | Tuesday (Mars) |
| **dimecres** | Wednesday (Mercurius) — NOT Spanish `miércoles` |
| **dijous** | Thursday (Jovis) |
| **divendres** | Friday (Veneris) |
| **dissabte** | Saturday (Sabbath) |
| **diumenge** | Sunday (Dominica) |

### Time

- **24-hour standard:** `14:30` or `14.30` (period also accepted)
- **12-hour informal:** `2:30 de la tarda`
- **Traditional Catalan time:** `dos quarts de tres` = 2:30 (lit. "two quarters of three"). Used in cultural/colloquial contexts, NOT in UI digital clocks.

### Currency: EUR

**Catalonia, Valencia, Balearic Islands, Andorra ALL use the euro** (since 1999/2002 for Spain, and Andorra adopted the euro by monetary agreement with the EU in 2011 — before that, it used Spanish peseta and French franc).

- **Format:** `99,99 €` (amount + space + symbol)
- **Symbol position:** AFTER the amount, with a space
- **Decimal:** comma `,`
- **Thousands:** period `.`
- **ISO code:** EUR — `EUR 1.234,56` in financial/banking contexts

| Wrong | Correct |
|-------|---------|
| `€99.99` (US format) | **`99,99 €`** |
| `99,99€` (no space) | **`99,99 €`** |
| `€ 99,99` (symbol first — accepted but less natural) | **`99,99 €`** |
| `99.99 €` (period decimal) | **`99,99 €`** |

---

## Terminology

### Native vs Spanish vs Anglicism — preferred Catalan

| English | ✅ Catalan | ❌ Avoid (Spanish) | ❌ Avoid (English calque) |
|---------|-----------|---------------------|----------------------------|
| save (file) | **desar** | guardar | salvar |
| file | **arxiu** / **fitxer** | archivo | file |
| computer | **ordinador** | ordenador | computer |
| mouse | **ratolí** | ratón | mouse |
| keyboard | **teclat** | teclado | keyboard |
| screen | **pantalla** | pantalla (also Spanish — OK) | screen |
| folder | **carpeta** | carpeta (also Spanish — OK) | folder |
| upload | **pujar** | subir | upload / uploadejar |
| download | **baixar** / **descarregar** | bajar / descargar | download |
| delete | **eliminar** / **esborrar** | borrar | deletar / delete |
| log in | **iniciar sessió** | iniciar sesión | loguejar-se |
| log out | **tancar sessió** | cerrar sesión | desloguejar-se |
| click | **fer clic** | hacer clic (OK as influence) | clicar (OK informal) |
| user | **usuari** | usuario | user |
| settings | **configuració** / **paràmetres** | ajustes | settings |
| dashboard | **tauler de control** / **panell** | tablero | dashboard |
| feedback | **comentaris** / **valoracions** | feedback | feedback |
| analytics | **anàlisis** / **estadístiques** | analíticas | analytics |
| workflow | **flux de treball** | flujo de trabajo | workflow |
| template | **plantilla** | plantilla (OK) | template |
| link (verb) | **enllaçar** | enlazar | linkar / linkejar |
| forward (email) | **reenviar** | reenviar (OK) | forwardejar |
| check / verify | **verificar** / **comprovar** | chequear | chequejar |
| log (record) | **registre** | registro | log |
| log (verb, record) | **registrar** | registrar | logar |
| update | **actualitzar** | actualizar (OK as influence) | updatejar |
| support (tech feature) | **admetre** / **ser compatible amb** | soportar | suportar |
| run (program) | **executar** | ejecutar (OK) | córrer (Spanish calque "correr un programa") |

### Common day-to-day vocabulary (Spanish-disambiguation table)

| English | ✅ Catalan | ❌ Spanish |
|---------|-----------|-----------|
| afternoon | **tarda** | tarde |
| morning | **matí** | mañana |
| evening / night | **vespre** / **nit** | tarde-noche / noche |
| to speak | **parlar** | hablar |
| to look for / search | **cercar** / **buscar** (both OK, `cercar` is more Catalan) | buscar |
| to eat | **menjar** | comer |
| to forget | **oblidar** | olvidar |
| to find | **trobar** | encontrar |
| to leave / exit | **sortir** (Central) / **eixir** (Valencian) | salir |
| work | **treball** / **feina** | trabajo |
| but | **però** | pero |
| then / so | **llavors** / **aleshores** | entonces |
| something | **alguna cosa** | algo |
| nothing | **res** | nada |
| someone | **algú** | alguien |
| nobody | **ningú** | nadie |
| also | **també** | también |
| very | **molt** | muy |
| more | **més** | más |
| less | **menys** | menos |
| now | **ara** | ahora |
| yesterday | **ahir** | ayer |
| today | **avui** | hoy |
| tomorrow | **demà** | mañana |
| this morning | **aquest matí** | esta mañana |
| close (verb) | **tancar** | cerrar |
| open (verb) | **obrir** | abrir |
| put | **posar** | poner |
| take | **agafar** / **prendre** | coger / tomar |
| give | **donar** | dar |

### Acronym gender (CRITICAL — inherited from expanded form)

Acronyms take the gender of the **first noun** of their full expansion in Catalan, NOT the apparent ending.

| Acronym | Expansion | Gender |
|---------|-----------|--------|
| **IA** | **I**ntel·ligència Artificial | feminine — `la IA`, `la nostra IA` |
| **API** | (Application Programming) **I**nterface = `Interfície` | feminine — `l'API` |
| **URL** | **U**niform Resource Locator = `Localitzador` | masculine — `el URL` (some sources also fem: `la URL`; IEC accepts both) |
| **PDF** | **F**ormat de Document Portàtil — actually the acronym is English, but `format` is masc | masculine — `el PDF` |
| **HTML** | `Llenguatge` (masc) | masculine — `el HTML` |
| **SQL** | `Llenguatge` (masc) | masculine — `el SQL` |
| **CPU** | `Unitat` (fem) | feminine — `la CPU` |
| **RAM** | `Memòria` (fem) | feminine — `la RAM` |

```
❌ el nostre IA      → ✅ la nostra IA
❌ el API            → ✅ l'API (fem)
❌ la PDF            → ✅ el PDF
```

### Brand names

Foreign tech brands default to **masculine**: `el Google`, `el Slack`, `el OneSky`, `el GitHub`. When the brand is treated as the company (`l'empresa`), feminine: `Apple ha anunciat...`.

For platform destinations, omit articles: `publicar a Google Play`, `disponible a App Store`. NOT `publicar al Google Play`.

### Gender of common IT nouns

| Masculine (el / l') | Feminine (la / l') |
|---------------------|---------------------|
| el problema | la solució |
| el sistema | la plataforma |
| el programa | l'aplicació |
| el tema | la pàgina |
| l'idioma | la connexió |
| el mapa | la integritat |
| el dia | la xarxa |
| l'arxiu / el fitxer | la pantalla |
| el software | la interfície |
| el servidor | la taula |
| el navegador | la consulta |
| el PDF | l'API |
| el URL | la IA |

**Patterns:**
- `-ció` / `-sió` / `-tat` / `-dat` → always feminine
- `-ma` (Greek origin) → usually masculine (problema, sistema, programa, idioma, tema, clima, drama)

Common errors: `una problema` → `un problema`; `la sistema` → `el sistema`; `el solució` → `la solució`.

---

## Calque / Anti-Pattern Blocklist

This is the section that most distinguishes Catalan quality from "translated-from-Spanish" quality.

### Anti-Spanish calques (HIGHEST PRIORITY — severity 2.0)

| Spanish-influenced (WRONG) | Catalan (CORRECT) | Notes |
|----------------------------|--------------------|-------|
| `guardar` | **`desar`** | "to save" — guardar exists in Catalan but means "to keep/store" generally; `desar` is the specific save action |
| `archivo` | **`arxiu`** / **`fitxer`** | "file" |
| `ordenador` | **`ordinador`** | "computer" |
| `ratón` | **`ratolí`** | "mouse" |
| `entonces` | **`llavors`** / **`aleshores`** | "then" |
| `pero` | **`però`** | "but" — note grave accent |
| `algo` | **`alguna cosa`** | "something" |
| `ajustes` | **`paràmetres`** / **`configuració`** | "settings" |
| `borrar` | **`esborrar`** / **`eliminar`** | "delete" — `borrar` exists but `esborrar` is more Catalan |
| `actualmente` (Spanish form) | **`actualment`** | "currently" |
| `realizar` (Spanish form) | **`realitzar`** / **`dur a terme`** | "to perform" |
| `intelligent` (English/looks Spanish) | **`intel·ligent`** | needs gem ela |
| `colaborar` (Spanish) | **`col·laborar`** | needs gem ela |

### Anti-English calques

| English-calque (WRONG) | Catalan (CORRECT) |
|------------------------|--------------------|
| `fa sentit` | **`té sentit`** / **`és lògic`** ("makes sense") |
| `en base a` | **`basant-se en`** / **`segons`** |
| `a nivell de` | **`pel que fa a`** / **`quant a`** |
| `al final del dia` | **`en definitiva`** / **`al cap i a la fi`** |
| `córrer un programa` | **`executar un programa`** ("run a program") |
| `prendre avantatge` | **`aprofitar`** ("take advantage") |
| `en termes de` | **`pel que fa a`** / **`quant a`** ("in terms of") |
| `Zero temps d'inactivitat` | **`Sense temps d'inactivitat`** ("Zero downtime") |
| `Zero errors` | **`Sense errors`** / **`Cap error`** |
| `i molt més` | **`i molt més encara`** / **`i moltes coses més`** ("and a lot more") |
| `productes de cura de la pell de nit` | **`productes de cura nocturna de la pell`** (avoid de-chains) |
| `Pagament exitós` | **`Pagament completat`** / **`Pagament realitzat`** |
| `usuari-amigable` | **`fàcil d'usar`** / **`intuïtiu`** |
| `núvol-basat` | **`basat en el núvol`** / **`al núvol`** |
| `IA-alimentat` / `impulsat per IA` (acceptable but `amb IA` smoother) | **`amb tecnologia d'IA`** / **`amb IA`** |
| `context-conscient` | **`sensible al context`** / **`contextual`** |
| `dades-impulsat` | **`basat en dades`** / **`orientat a dades`** |

### Structural calques

| English subject-first passive (WRONG calque) | Verb-first / impersonal Catalan |
|----------------------------------------------|-----------------------------------|
| `[X] és necessari per a [Y]` | **`Cal [X] per a [Y]`** / **`Es requereix [X] per a [Y]`** |
| `[X] és obligatori` | **`Cal [X]`** / **`És obligatori [X]`** (with verb-first or impersonal) |
| `variable d'entorn falta` | **`la variable d'entorn falta`** / **`falta la variable d'entorn`** |

### Article completeness in noun phrases (CRITICAL)

Specific known nouns require definite articles in prepositional phrases.

| Wrong (missing article) | Correct |
|-------------------------|---------|
| `Error d'aplicació` | **`Error de l'aplicació`** |
| `Configuració de compte` | **`Configuració del compte`** |
| `Estat de connexió` | **`Estat de la connexió`** |
| `Detalls de transacció` | **`Detalls de la transacció`** |

Exception: generic classifier vs specific:
- `error de sistema` = a type of error (generic)
- `error del sistema` = error of THE system (specific)

### Adjective order

| Wrong | Correct |
|-------|---------|
| `servei complet nou` | **`servei nou complet`** (descriptive adj. after noun) |
| `bona servei` | **`bon servei`** (`bon/mal/gran` before noun, but `bon` not `bona`) |

`Bo/Bon/Bons/Bons` — masc.: `bon` apocopated before masculine singular nouns starting with consonant (`bon dia`, `bon servei`, `bon usuari`). Full `bo` after the noun or in predicate position.

### Idioms

| English idiom | Catalan equivalent |
|---------------|---------------------|
| Break a leg! | **Molta merda!** / **Molta sort!** |
| Piece of cake | **És bufar i fer ampolles** / **És coser i cantar** |
| It's raining cats and dogs | **Plou a bots i barrals** / **Cau un diluvi** |
| John Doe (placeholder name) | **Pere Català** / **Fulano de Tal** (the latter is also Spanish-origin) |
| at the end of the day | **al cap i a la fi** / **en definitiva** |

---

## Self-Check Checklist (run before finalizing)

### Identity / anti-Spanish-calque (CRITICAL)
- [ ] No `guardar` (use `desar`)
- [ ] No `archivo` (use `arxiu` or `fitxer`)
- [ ] No `ordenador` (use `ordinador`)
- [ ] No `ratón` (use `ratolí`)
- [ ] No `entonces` (use `llavors` or `aleshores`)
- [ ] No `pero` (use `però` with grave accent)
- [ ] No `algo` (use `alguna cosa`)
- [ ] No `ajustes` (use `paràmetres` or `configuració`)
- [ ] No `tarde`, `hablar`, `comer`, `olvidar`, `miércoles`, `trabajo` etc. — use Catalan equivalents

### Orthography (CRITICAL)
- [ ] Geminated L written as `l·l` with INTERPUNCT (not `.` or `-`): `intel·ligent`, `col·laborar`, `instal·lació`, `paral·lel`, `excel·lent`, `il·lusió`
- [ ] `ç` (c-cedilla) before `a/o/u`: `força`, `plaça`, `comença`, `març`
- [ ] Apostrophe elision: `l'aigua`, `d'ahir`, `l'usuari`, `m'agrada`
- [ ] Article contractions: `al`, `del`, `pel`, `als`, `dels`, `pels` (BUT `a l'usuari`, `de l'aplicació`)
- [ ] Open vs closed accents correct: `cafè`, `però`, `història` (open `è/ò`), `també`, `només`, `informació` (closed `é/ó`)
- [ ] NO inverted `¿` or `¡` at sentence start

### Grammar
- [ ] Gender correct (problema=masc, sistema=masc, solució=fem, plataforma=fem)
- [ ] Acronym gender from expanded form: `la IA` (Intel·ligència), `l'API` (Interfície), `el PDF`
- [ ] Adjective gender + number agreement (plataformes intel·ligents NOT plataformes intel·ligent)
- [ ] Periphrastic past `vaig + infinitive` (NOT archaic simple preterite, NOT Spanish-style)
- [ ] Weak pronoun `en` for partitive ("en tinc dos")
- [ ] Weak pronoun `hi` for locative ("hi vaig")
- [ ] Formality consistent: `vostè / el seu / les seves / desi` ALL formal, OR `tu / el teu / les teves / desa` ALL informal — no mixing
- [ ] Article completeness in noun phrases (`Error de l'aplicació` NOT `Error d'aplicació`)
- [ ] Subjunctive after `cal que`, `és possible que`, `vull que`

### Punctuation, numbers, dates
- [ ] No comma before `i`, `o`, `ni`
- [ ] Comma before `però`, `sinó`
- [ ] Numbers: `1.234,56` (period thousands, comma decimal)
- [ ] Currency: `99,99 €` (amount, space, symbol)
- [ ] Date: `15/01/2024` or `15 de gener de 2024` (months lowercase)
- [ ] Days lowercase: `dilluns`, `dimecres`, `divendres`
- [ ] Quotation marks: `«...»` (formal) or `"..."` (digital)

### UI conventions
- [ ] Buttons in infinitive: `Desar`, `Cancel·lar`, `Eliminar`, `Confirmar`
- [ ] Status in gerund: `Desant...`, `Carregant...`, `Processant...`
- [ ] Completion participial: `Pagament completat` NOT `Pagament exitós`
- [ ] Empty state: `No hi ha X` NOT `No s'han X`
- [ ] Drag and drop: `arrossegar i deixar anar` (NOT `dropejar`, NOT `alliberar`)
- [ ] File picker: `Seleccionar fitxer` / `Triar fitxer` NOT `Explorar`
- [ ] Sentence case in buttons and headings
- [ ] Quantity: `més de 25 idiomes` NOT `25+ idiomes`
- [ ] `per` (rate) vs `per a` (total / recipient / purpose) — follow IEC

### Naturalness
- [ ] No calque `fa sentit` (use `té sentit`)
- [ ] No calque `en base a` (use `segons` / `basant-se en`)
- [ ] No calque `en termes de` (use `pel que fa a` / `quant a`)
- [ ] No Spanish-influenced anglicisms: `linkar`, `deletar`, `forwardejar`, `chequejar`
- [ ] Block verb mood consistent (conditional title → conditional or noun-phrase items; imperative title → imperative items)
- [ ] All `{variables}` and ICU plurals preserved
- [ ] Reads aloud naturally — not "Google Translate from Spanish"

---

## Worked Examples

### Example 1 — Welcome / upload UI (vostè register)

**Source:** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

**❌ Bad (Spanish-influenced, with multiple errors):**

```
¡Bienvenido! Por favor seleccioni el seu archivo para subir — suportamos 25+ formatos
y lo traducimos por 5 idiomas en {seconds}s. No se preocupi, pot cancel·larlo en
qualsevol moment.
```

Errors: inverted `¡` (Spanish), `archivo` (Spanish), `subir` (Spanish), `suportamos` (Spanish/English calque + Spanish verb form), `25+` (calque), `por 5 idiomas` (FOR/PER confusion), mixed formality.

**✅ Good (clean Catalan, vostè formal):**

```
Benvingut! Seleccioni el seu fitxer per pujar-lo. Admetem més de 25 formats i el
traduïm a 5 idiomes en {seconds} segons. No es preocupi, el pot cancel·lar en
qualsevol moment.
```

Note: `Benvingut` (no inverted `¡`), `fitxer` (not archivo), `pujar` (not subir), `Admetem` (not suportar), `més de 25` (not `25+`), `a 5 idiomes` (correct preposition), `cancel·lar` (with interpunct), consistent `vostè` throughout.

**✅ Good (clean Catalan, tu informal — for consumer apps):**

```
Benvingut! Selecciona el teu fitxer per pujar-lo. Admetem més de 25 formats i
el traduïm a 5 idiomes en {seconds} segons. No et preocupis, el pots cancel·lar
en qualsevol moment.
```

### Example 2 — Status & completion messages

| English | ❌ Bad | ✅ Good |
|---------|-------|---------|
| Saving... | `Desar...` | **`Desant...`** |
| File uploaded successfully | `Fitxer pujat exitosament` | **`Fitxer pujat`** / **`Càrrega completada`** |
| Payment successful | `Pagament exitós` | **`Pagament completat`** / **`Pagament realitzat`** |
| No results found | `No s'han trobat resultats` | **`No hi ha resultats`** |
| Loading... | `Carregar...` | **`Carregant...`** |
| Processing... | `Procesar...` (Spanish) | **`Processant...`** |

### Example 3 — Error message with periphrastic past

**Source:** "Your file failed to upload. Please try again."

**❌ Bad:** `El seu archivo falló al subir. Por favor, intenti de nuevo.`
(Multiple Spanish calques)

**✅ Good (vostè):** `No s'ha pogut pujar el seu fitxer. Si us plau, torni-ho a provar.`
(Impersonal voice with `no s'ha pogut` is most natural for system-side failures)

**✅ Good (tu):** `No s'ha pogut pujar el teu fitxer. Si us plau, torna-ho a provar.`

### Example 4 — Date and price

**Source:** "Your subscription costs €99.99/month, billed on January 15, 2026."

**❌ Bad:** `La seva subscripció costa €99.99/mes, facturada el January 15, 2026.`
(English currency format, English month, English date order)

**✅ Good:** `La seva subscripció costa 99,99 € al mes, facturada el 15 de gener de 2026.`

Or fully numeric: `...facturada el 15/01/2026.`

### Example 5 — Geminated L showcase

**Source:** "Our intelligent collaboration platform offers an excellent illustrated experience with installable parallel modules."

**❌ Bad:** `La nostra plataforma de colaboració intelligent ofereix una experiència ilustrada excelente amb mòduls parallels instalables.`
(All missing the interpunct + Spanish `excelente`)

**✅ Good:** `La nostra plataforma de col·laboració intel·ligent ofereix una experiència il·lustrada excel·lent amb mòduls paral·lels instal·lables.`

Count of `l·l`: 6 in one sentence. This is what native Catalan written text looks like — the interpunct is everywhere.

### Example 6 — Periphrastic past trap

**Source:** "Yesterday I saved the file, but today I forgot the password."

**❌ Bad (Spanish-calque-style with simple preterite):** `Ahir vaig guardar el archivo, però avui vaig olvidar la contrasenya.`
(Multiple Spanish words AND `vaig guardar` should be `vaig desar`)

**❌ Bad (using future-looking Spanish `voy a`):** `Ahir voy a desar el fitxer...`
(Catastrophic — `voy a` does not exist in Catalan; would be misread)

**✅ Good:** `Ahir vaig desar el fitxer, però avui vaig oblidar la contrasenya.`

Note: `vaig desar` = "I saved" (Catalan past); a Spanish speaker who sees `vaig` thinks "I'm going to..." (future) — but that is wrong for Catalan.

### Example 7 — `en` and `hi` (signature Catalan pronouns)

**Source:** "I have three files. Do you want me to send them to you? I'll go to the office to get them."

**❌ Bad (no weak pronouns — sounds Spanish-influenced):**
`Tinc tres fitxers. Vols que te'ls enviï els fitxers? Vaig a l'oficina a buscar els fitxers.`
(Verbose, redundant noun repetition)

**✅ Good (natural Catalan with `en`, `hi`, and clitic `els`):**
`Tinc tres fitxers. Vols que te'ls enviï? Hi vaig a buscar-los a l'oficina.`

Or more idiomatic restructuring:
`En tinc tres. Te'ls envio? Vaig a l'oficina a buscar-los.`

### Example 8 — Block verb mood

**❌ Bad:**
```
El que obtindríeu:
- Rebeu una proposta detallada
- Reviseu els terminis
- Confirmeu l'acord
```
(Conditional title `obtindríeu` + imperative items `rebeu/reviseu/confirmeu` — mood mismatch.)

**✅ Good (option A — conditional items match conditional title):**
```
El que obtindríeu:
- Rebríeu una proposta detallada
- Revisaríeu els terminis
- Confirmaríeu l'acord
```

**✅ Good (option B — noun-phrase items, neutral):**
```
El que obtindríeu:
- Una proposta detallada
- Revisió de terminis
- Confirmació de l'acord
```

### Example 9 — Empty state

**Source:** "No files have been uploaded yet."

**❌ Bad (passive calque):** `No s'han pujat fitxers encara.`

**✅ Good (existential):** `Encara no hi ha cap fitxer pujat.` or `No hi ha fitxers pujats.`

---

## When in Doubt

1. **If you're unsure whether a word is Spanish or Catalan, assume it's a Spanish calque** and look up the Catalan equivalent. The bias is strong — Catalan speakers are bilingual and constantly hear Spanish, so Spanish vocabulary feels "fine" when in fact it's a calque.

2. **If you see a geminated double-L in the source language**, the Catalan equivalent almost certainly needs `l·l` with interpunct. Build a habit of checking: `intelligent → intel·ligent`, `collaborate → col·laborar`, `install → instal·lar`, `parallel → paral·lel`, `excellent → excel·lent`.

3. **If you see Spanish inverted `¿` or `¡` in the source**, REMOVE them. Catalan does not use them.

4. **If you can't decide between `desar/guardar`, `arxiu/archivo`, `ordinador/ordenador`** — choose the Catalan form. Always. The Spanish form is always wrong in Catalan UI.

5. **If the source has a past tense, use `vaig + infinitive`**, not the archaic simple preterite (`desí`, `vaig`, `vaig anar`). The simple preterite reads as 19th-century literary Catalan, not modern UI.

6. **If a sentence has a definite-noun prepositional phrase**, check for the article: `Error de l'aplicació`, NOT `Error d'aplicació`. The missing article is a signature Catalan error in machine translation.

7. **If you're translating from Spanish into Catalan** (very common — many companies localize ES first, then auto-translate to CA), treat the Spanish source as suspect for every single word. Re-translate from English if available. ES → CA is the highest-risk direction because it bakes in every Spanish calque.

8. **For Valencian / Balearic content**, use the IEC standard (general Catalan) unless the user explicitly requests dialect-flavored output. AVL and IEC are mutually compatible for 99% of UI vocabulary.

9. **When in doubt about register**, default to `vostè` — it is professional and safe. `tu` can read as disrespectful in B2B, banking, government, or healthcare.

10. **Cultural respect**: clean Catalan without Spanish slippage is a respect signal. Catalan readers will notice. Native-quality Catalan signals that your product takes the language seriously — and given the political and cultural weight of language in Catalonia, Valencia, and Andorra, this matters more than it does for most other localizations.

---

## Summary — the Catalan distinctness checklist

If you can answer YES to all of these, your Catalan is native-quality:

1. **Does every double-L use the interpunct `l·l`?** (`intel·ligent`, `col·laborar`)
2. **Does every `c` before `a/o/u` that should be `/s/` have the cedilla `ç`?** (`força`, `plaça`, `març`)
3. **Are there ZERO inverted `¿` or `¡` at sentence starts?**
4. **Is `vaig + infinitive` used for past tense** (not the archaic preterite, not Spanish `he/has + participio` style)?
5. **Are `en` (partitive) and `hi` (locative) used where natural Catalan would use them?**
6. **Is the file vocabulary Catalan, not Spanish?** (`desar`, `arxiu/fitxer`, `ordinador`, `ratolí`, `paràmetres`, `pujar`, `baixar`)
7. **Are the connectors Catalan?** (`però`, `llavors`, `alguna cosa`, `també`, `també`)
8. **Are dates lowercase?** (`gener`, `dimecres`)
9. **Is currency `99,99 €` with comma decimal, space, symbol-after?**
10. **Is formality consistent (vostè OR tu, never mixed)?**

If all ten check, you have native-quality Catalan that respects the language as distinct from Spanish.
