---
name: localize-cy
description: Use when translating or localizing UI strings, marketing copy, documentation, error messages, or any source text into Welsh (cy / Cymraeg) for Wales. Welsh is a Celtic Brittonic language (sister to Cornish and Breton) — NOT Irish/Gaelic (Goidelic), and NOT English despite geographic proximity. THE defining critical feature is INITIAL CONSONANT MUTATIONS — three systems (soft / nasal / aspirate) that change the first letter of a word based on the grammatical environment (the trigger word that precedes it, gender of the noun, syntactic role). Mutations are not optional ornament; they are part of the spelling. Other key features: VSO word order (verb-first — "Cadwodd y defnyddiwr y ffeil"), Welsh 29-letter alphabet with 8 digraphs treated as single letters (ch, dd, ff, ng, ll, ph, rh, th — ng comes after g in dictionary order, NOT between n and o), w and y are vowels (Welsh has 7 vowels: a e i o u w y), to bach circumflex (â ê î ô û ŵ ŷ) marks long vowels and is meaning-critical, NO indefinite article (ci = "dog" OR "a dog"), definite article y/yr/'r changes form based on what follows, inflected prepositions (arnaf fi / arnat ti / arno fe — prepositions conjugate for person+number), predicative yn triggers soft mutation, periphrastic verb constructions with bod + yn + verbal noun (Mae'n cadw), 2-gender system (masculine/feminine) with feminine nouns triggering soft mutation after y, numbers 1-4 with gendered forms (dau/dwy, tri/tair, pedwar/pedair), 6-form ICU plural system (zero/one/two/few/many/other), singular noun after numbers 1-10 (5 ffeil NOT 5 ffeiliau), "o" + plural for numbers 11+ (15 o ffeiliau), chi (formal/plural) vs ti (informal/singular) T-V distinction, verbal-noun (berfenw) buttons (Cadw not Cadwch — UI convention from Microsoft/Apple/LibreOffice Welsh), periphrastic status with "Wrthi'n" (Wrthi'n cadw...), impersonal past for completion (Cadwyd / Wedi'i gadw), DD/MM/YYYY dates, GBP £ currency (Wales uses British pound), 1,234.56 number format (Anglo style — comma thousands, period decimal), and Cymraeg Clir (Plain Welsh) cultural movement for accessible language. Reference: BydTermCymru, Y Termiadur Addysg for official terminology.
---

# Localize: Welsh (cy → Cymraeg) — High-Fidelity Skill

## Scope & Variants

Welsh (Cymraeg) is the Celtic language of Wales. The default and primary target for product localization is **Welsh Standard Written** — the unified literary/professional written register used across Wales for government, education, broadcasting, and software UI.

| Locale | Notes |
|--------|-------|
| `cy` / `cy-GB` | Welsh (Wales). **Default and primary target.** Welsh Standard Written form covers all UI work. |
| Northern Welsh (Gogledd) | Colloquial spoken variant — does NOT diverge in written/UI contexts. |
| Southern Welsh (De) | Colloquial spoken variant — does NOT diverge in written/UI contexts. |

**Practical reality:** Welsh has a strong written standard (sometimes called *Cymraeg safonol* or *Cymraeg llenyddol*) that is used uniformly across Wales for UI, government, broadcasting, and education. Northern and Southern Welsh diverge in spoken pronunciation, lexicon (e.g., *llefrith* North vs *llaeth* South for "milk"), and some verb forms (e.g., *dwi'n* North vs *rwy'n* South for "I am"), but these regional differences are **largely absent from the written standard used in software localization**.

The defining quality concern in Welsh localization is **correct application of initial consonant mutations**. Mutations are not optional or stylistic — they are mandatory orthographic changes triggered by specific grammatical environments. A Welsh translation with missing or wrong mutations reads as fundamentally broken to a native speaker, even if the rest of the text is correct.

### Welsh is a Celtic Brittonic language

Welsh is one of the four surviving Celtic languages, in the **Brittonic (Brythonic, P-Celtic)** branch:

| Branch | Languages |
|--------|-----------|
| **Brittonic (P-Celtic)** — Welsh's family | **Welsh (Cymraeg)**, Cornish (Kernewek), Breton (Brezhoneg) |
| Goidelic (Q-Celtic) — DIFFERENT family | Irish (Gaeilge), Scottish Gaelic (Gàidhlig), Manx (Gaelg) |

Welsh shares structural features with Cornish and Breton (mutations, VSO word order, inflected prepositions) but is **NOT mutually intelligible with Irish or Scottish Gaelic**, despite popular conflation. Calling Welsh "Gaelic" is wrong.

Welsh is also **NOT English**. Despite Wales sharing the island of Great Britain with England and the deep historical contact between the two languages, Welsh is structurally unrelated to English. Welsh has VSO word order (not SVO), initial consonant mutations (not present in English), inflected prepositions (English has none), and no indefinite article (English has "a/an"). Treating Welsh as "English in disguise" is the most common source of bad Welsh translations.

---

## Identity Guardrail — Welsh is NOT Gaelic and NOT English

Auto-fail signals (translator is treating Welsh as the wrong language):

| Signal | Diagnosis | Fix |
|--------|-----------|-----|
| Output uses *Sláinte*, *Slán*, *Fáilte* | Translator wrote Irish, not Welsh | "Welcome" = **Croeso**; "Goodbye" = **Hwyl fawr** |
| Output uses Gaelic accent marks like *à è ì ò ù* | Irish/Scottish Gaelic uses grave accents | Welsh uses **circumflex (to bach): â ê î ô û ŵ ŷ** — never grave |
| Output is SVO (subject-verb-object) word order | Translator used English structure | Welsh is **VSO** — verb first: *Cadwodd y defnyddiwr y ffeil* |
| Output mutations missing or incorrect | Translator skipped Welsh-specific grammar | Apply soft/nasal/aspirate mutation per trigger |
| Output uses *the* before nouns mechanically | English calque | Welsh has only definite article (y/yr/'r) and NO indefinite article |
| Output uses *of* construction (*car o John*) | English calque | Welsh uses **juxtaposition for possession**: *car John* |
| Output reads like word-for-word English | English SVO retained | Restructure as VSO with periphrastic *bod + yn + verbal noun* |

**Cultural note:** Welsh has Equal Status with English in Wales under the Welsh Language (Wales) Measure 2011. The Welsh Government's strategy *Cymraeg 2050* aims for one million Welsh speakers by 2050. The **Cymraeg Clir (Plain Welsh)** movement promotes accessible, clear Welsh in public communications. Welsh-language-medium contexts (Welsh-medium schools, Welsh-language broadcasting, government bilingual services) are politically and culturally significant. Sloppy or anglicism-heavy Welsh is not just bad style — it is read as disrespect for the language.

---

## Register Auto-Detection (Apply Before Translating)

Welsh has a T-V distinction:

| Pronoun | Use | Possessive | Verb ending (imperative) |
|---------|-----|------------|--------------------------|
| **chi** | Formal singular OR plural (any number) | **eich** (no mutation) | **-wch** (Cadwch, Dewiswch) |
| **ti** | Informal singular only | **dy** (+ soft mutation) | **-a / -â** (Cadwa, Dewisa) |

**Auto-detect from source:**

| Source signal | Target register |
|---------------|-----------------|
| Professional product UI / business / government (DEFAULT) | **chi formal** — `eich`, `-wch` imperatives, native Welsh vocabulary |
| Casual app / social / children's software | **ti informal** — `dy + soft mutation`, `-a` imperatives |
| Marketing copy (warm but professional) | **chi formal** — Welsh marketing is typically formal/respectful |
| Legal / banking / official | **chi formal** — never `ti` for institutional voice |

**Hard rule: never mix chi and ti in the same text.**
- ✗ `Cadwch eich gwaith` + `Dewisa` — mixes chi imperative with ti imperative
- ✗ `Gallwch chi newid dy osodiadau` — chi verb form with ti possessive

**Special UI exception — verbal-noun buttons are register-neutral:**
Welsh UI buttons use the **berfenw (verbal noun)** form, which is neither chi nor ti — it's the bare verb form: `Cadw`, `Dileu`, `Copio`, `Agor`. This is the established Microsoft/Apple/LibreOffice/Welsh Government convention. Button labels do NOT change between chi and ti registers.

| Surface | chi form | ti form | Verbal-noun (buttons) |
|---------|----------|---------|-----------------------|
| Imperative ("Save!") | **Cadwch** | **Cadwa** | — |
| Button label | — | — | **Cadw** |
| Possessive ("your file") | **eich ffeil** | **dy ffeil** | — |
| Instruction in body text | **Dewiswch eich ffeil** | **Dewisa dy ffeil** | — |

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. Initial Consonant Mutations — THE defining Welsh feature (severity 2.5)

Welsh mutations change the first letter of a word based on the grammatical environment. There are **three mutation systems**: **soft (treiglad meddal)**, **nasal (treiglad trwynol)**, and **aspirate (treiglad llaes)**. Mutations are not optional; they are part of the word's spelling in that context.

#### 1a. Soft Mutation (Treiglad Meddal) — most common

The soft mutation softens stops to voiced/fricative equivalents:

| Original | Soft mutation | Example trigger | Example |
|----------|---------------|-----------------|---------|
| **c** | **g** | dy (your-ti) | dy **g**ar (your car) ← *car* |
| **p** | **b** | i (to) | i **B**aris ← *Paris* |
| **t** | **d** | o (from) | o **D**denmarc ← *Tdenmarc*... actually: o **D**enmarc ← *Denmarc* |
| **g** | (dropped — ∅) | dy (your-ti) | dy **a**rdd ← *gardd* (your garden) |
| **b** | **f** | dy (your-ti) | dy **f**rawd ← *brawd* (your brother) |
| **d** | **dd** | dy (your-ti) | dy **dd**rws ← *drws* (your door) |
| **m** | **f** | y (fem. art.) | y **f**erch ← *merch* (the girl) |
| **ll** | **l** | dy (your-ti) | dy **l**aw ← *llaw* (your hand) |
| **rh** | **r** | dy (your-ti) | dy **r**iant ← *rhiant* (your parent) |

**Soft mutation triggers (the most important set to memorize):**

| Trigger | Meaning | Example |
|---------|---------|---------|
| **dy** | your (ti, informal) | dy **g**ar (your car) |
| **ei** | his | ei **d**ad (his father) |
| **y / yr / 'r** | the (only before feminine singular nouns) | y **f**erch (the girl) |
| **i** | to | i **G**aerdydd (to Cardiff) |
| **o** | from / of | o **L**undain (from London) |
| **am** | about, at (time) | am **d**ri (at three) |
| **ar** | on | ar **g**adair (on a chair) |
| **at** | towards | at **D**di (to you-ti) |
| **gan** | by, with | gan **f**erch (by a girl) |
| **heb** | without | heb **g**arden (without a garden... actually *gardd*) |
| **tan / dan** | under, until | dan **f**wrdd (under a table) |
| **dros** | over, for | dros **b**onthwy (over a bridge... *pont*) |
| **drwy / trwy** | through | drwy **g**oeden (through a tree) |
| **wrth** | by, while | wrth **g**adw (while saving) |
| **hyd** | until | hyd **f**ory (until tomorrow) |
| **neu** | or (sometimes) | A **neu** B (or; usually no mutation in modern Welsh) |
| **yn** (predicative, before adj./noun) | "is" + complement | Mae'n **dd**iddorol ← *diddorol* (it is interesting) |
| **yn** (adverbial, before adj.) | -ly | yn **g**yflym ← *cyflym* (quickly) |
| **dau / dwy** | two (m./f.) | dau **g**i (two dogs); dwy **f**erch (two girls) |
| **tri / tair** | three (m./f.) | (note: *tri* takes aspirate, not soft — see below) |
| **prif** | main, chief (precedes noun) | y prif **b**eth (the main thing) ← *peth* |
| **hen** | old (precedes noun) | hen **d**ŷ (an old house) ← *tŷ* |
| **Feminine singular noun → adjective after it** | | merch **dd**al ← *tal* (a tall girl) |
| **Object of inflected (conjugated) verb** | direct object soft-mutates | Gwelais **g**i ← *ci* (I saw a dog) |

#### 1b. Nasal Mutation (Treiglad Trwynol)

The nasal mutation converts stops to their nasal equivalents:

| Original | Nasal mutation | Example trigger | Example |
|----------|----------------|-----------------|---------|
| **c** | **ngh** | fy (my) | fy **ngh**ar ← *car* (my car) |
| **p** | **mh** | fy (my) | fy **mh**en ← *pen* (my head) |
| **t** | **nh** | fy (my) | fy **nh**ad ← *tad* (my father) |
| **g** | **ng** | fy (my) | fy **ng**ardd ← *gardd* (my garden) |
| **b** | **m** | fy (my) | fy **m**rawd ← *brawd* (my brother) |
| **d** | **n** | fy (my) | fy **n**rws ← *drws* (my door) |

**Nasal mutation triggers (only two real triggers):**

| Trigger | Meaning | Example |
|---------|---------|---------|
| **fy** | my | fy **ngh**ar (my car) |
| **yn** (as locative preposition "in") | in [place] | yng **Ngh**aerdydd ← *Caerdydd* (in Cardiff). Note: `yn` itself becomes `ym` before m-/mh-, `yng` before ng-/ngh-. |

**Critical: `yn` has three different functions and mutations.** See §1d below.

#### 1c. Aspirate Mutation (Treiglad Llaes)

The aspirate mutation affects ONLY c, p, t, converting them to fricatives:

| Original | Aspirate mutation | Example trigger | Example |
|----------|-------------------|-----------------|---------|
| **c** | **ch** | ei (her) | ei **ch**ar ← *car* (her car) |
| **p** | **ph** | a (and) | a **ph**leser ← *pleser* (and pleasure) |
| **t** | **th** | ei (her) | ei **th**ad ← *tad* (her father) |

**Aspirate mutation triggers:**

| Trigger | Meaning | Example |
|---------|---------|---------|
| **ei** | her | ei **th**ad (her father) |
| **a** | and | bara **ch**aws ← *caws* (bread and cheese) |
| **â** | with (instrument) | â **ch**yllell ← *cyllell* (with a knife) |
| **gyda** | with | gyda **ph**leser (with pleasure) |
| **tri** | three (m.) | tri **ch**i ← *ci* (three dogs) |
| **chwe** | six | chwe **ph**unt ← *punt* (six pounds) |
| **tua** | about, approximately | tua **th**ri (about three) |

#### 1d. The Three Faces of `yn` — Critical Disambiguation

Welsh `yn` has three completely different uses, each triggering a different mutation (or none):

| Function | Mutation | Example |
|----------|----------|---------|
| **Progressive aspect** (before verbal noun) — "is doing" | **NO mutation** | Mae'n **c**adw (he/she is saving). NOT *Mae'n gadw*. |
| **Adverbial** (before adjective, makes -ly) | **Soft mutation** | yn **g**yflym (quickly) ← *cyflym* |
| **Predicative** (before adjective or noun complement) — "is X" | **Soft mutation** (but NOT on ll-/rh-) | Mae'n **dd**iddorol (it is interesting) |
| **Locative preposition** (= "in") | **Nasal mutation** + `yn → ym/yng` | yng **Ngh**aerdydd (in Cardiff) |

**Common mistake:** treating progressive `yn` as if it mutates. `Mae'n gadw` is WRONG; `Mae'n cadw` is right. Verbal nouns after progressive `yn` keep their dictionary form.

#### 1e. Possessive pronoun mutations (memorize this table)

| Possessive | Meaning | Mutation triggered |
|------------|---------|---------------------|
| **fy** | my | **Nasal** (fy nghar, fy mhen, fy nhad, fy ngardd, fy mrawd, fy nrws) |
| **dy** | your (ti, informal sg.) | **Soft** (dy gar, dy ben, dy dad, dy ardd, dy frawd, dy ddrws) |
| **ei** (masculine) | his | **Soft** (ei gar, ei ben, ei dad, ei ardd, ei frawd, ei ddrws) |
| **ei** (feminine) | her | **Aspirate** (ei char, ei phen, ei thad) — only c/p/t mutate |
| **ein** | our | **NO mutation** (ein car, ein pen, ein tad) — but often + "n" sandhi: ein **n**ardd? No: *ein gardd*. |
| **eich** | your (chi, formal/plural) | **NO mutation** (eich car, eich pen, eich tad) |
| **eu** | their | **NO mutation** (eu car, eu pen, eu tad) |

**UI impact:** Formal Welsh UI uses **eich** (no mutation) → simplifies translation. Informal UI uses **dy** + soft mutation → requires applying soft mutation to every possessed noun.

### 2. Welsh 29-Letter Alphabet — Digraphs Are Single Letters (severity 2.5)

The Welsh alphabet has **29 letters**, including 8 **digraphs** that are treated as **single letters** for sorting, hyphenation, and counting:

```
a, b, c, ch, d, dd, e, f, ff, g, ng, h, i, j, l, ll, m, n, o, p, ph, r, rh, s, t, th, u, w, y
```

**Critical: w and y are VOWELS** in Welsh, not consonants. Welsh has **7 vowels**: a, e, i, o, u, w, y. This is why words like *cwm* (valley), *crwth* (stringed instrument), *y* (the), *bryn* (hill) are valid — *w* and *y* are vowels carrying the syllable.

**Digraph alphabetical order:**

| Digraph | Position | Example |
|---------|----------|---------|
| **ch** | After **c** (NOT after h) | `cae, ci, ciuto, ch-...` |
| **dd** | After **d** | `da, dy, ddim` |
| **ff** | After **f** | `ffon, ffeil` |
| **ng** | After **g** (NOT between n and o!) | `gan, gardd, ng-...` |
| **ll** | After **l** | `lle, llyfr` |
| **ph** | After **p** | (rare outside mutations) |
| **rh** | After **r** | `rhad, rhif` |
| **th** | After **t** | `thri, thal` |

**Critical for sorting:** Welsh dictionary order places `ng` **after `g`**, not between `n` and `o`. So `nofio` (to swim) comes BEFORE `ngardd` (my-garden), not after. Modern Welsh dictionaries follow this convention.

**Critical for hyphenation:** Never split a digraph. *llygoden* hyphenates as *lly-go-den*, never *l-lygoden*. *anghofio* hyphenates as *ang-hof-io* — no, actually *an-gho-fio* — wait, since `ng` is one letter, it stays together: *a-ngho-fio*. (Welsh hyphenation is complex; the rule is "treat digraphs as one letter".)

**Critical for character counting:** *ffon* (stick) has **3 letters** (ff, o, n), not 4.

### 3. To Bach (Circumflex) — Long Vowels (severity 2.0)

The **to bach** ("little roof") is the circumflex accent that marks long vowels in Welsh. It appears on all 7 vowels: **â, ê, î, ô, û, ŵ, ŷ**.

**The to bach is meaning-critical** — it distinguishes minimal pairs:

| Without to bach | Meaning | With to bach | Meaning |
|-----------------|---------|--------------|---------|
| **tan** | until / fire | **tân** | fire (clarified) |
| **gem** | gem | **gêm** | game |
| **ty** | (no meaning alone) | **tŷ** | house |
| **dyn** | man | **dŷn** | (different sense) |
| **llan** | parish | **llân** | full |
| **gwn** | gun / I know (depends) | **gŵn** | gown / I know (different) |
| **cyn** | before | **cŷn** | chisel |

**Critical: ŵ and ŷ are uniquely Welsh letters.** The circumflex on w and y appears in no other major Latin-script language. NEVER strip these to plain `w` and `y` — they change meaning.

**Common UI words with to bach:**

| Welsh | Meaning |
|-------|---------|
| **tŷ** | house |
| **tân** | fire |
| **cŵn** | dogs (plural of ci) |
| **gwŷr** | husbands / men |
| **ŵy** | egg |
| **ŷd** | corn |
| **â** | with |
| **ê** | (interjection) |

### 4. VSO Word Order (severity 2.0)

Welsh is **strict VSO (verb-subject-object)** in affirmative main clauses with inflected verbs. The verb comes FIRST.

| ✗ Wrong (English SVO) | ✓ Correct (Welsh VSO) | Gloss |
|-----------------------|------------------------|-------|
| Y defnyddiwr cadwodd y ffeil | **Cadwodd y defnyddiwr y ffeil** | Saved-the-user-the-file (= The user saved the file) |
| Chi gallu newid gosodiadau | **Gallwch chi newid gosodiadau** | Can-you change settings |
| Y cyfrifiadur yn lawrlwytho | **Mae'r cyfrifiadur yn lawrlwytho** | Is-the-computer downloading |
| Y ci yn cysgu | **Mae'r ci yn cysgu** | Is-the-dog sleeping |

**Periphrastic constructions also follow VSO** — the auxiliary `bod` (to be) is the verb:

| English | Welsh |
|---------|-------|
| The user is saving the file. | **Mae'r defnyddiwr yn cadw'r ffeil.** (Is-the-user yn save-the-file) |
| The file has been saved. | **Mae'r ffeil wedi'i chadw.** (Is-the-file wedi-its saved [aspirate mutation on *cadw* → *chadw* because ffeil is feminine]) |
| You can save your work. | **Gallwch chi gadw eich gwaith.** (Can-you save your work [*cadw* soft-mutates after the inflected modal `gallwch`]) |

### 5. Periphrastic Verb Constructions (severity 2.0)

Modern Welsh primarily uses periphrastic (auxiliary) verb constructions with **bod** (to be) + **yn** (progressive particle) + **berfenw** (verbal noun):

| Tense | Pattern | Example |
|-------|---------|---------|
| **Present** | `Mae [subject] + yn + verbal noun` | *Mae e'n cadw* (He is saving / He saves) |
| **Past (continuous)** | `Roedd [subject] + yn + verbal noun` | *Roedd e'n cadw* (He was saving) |
| **Perfect** | `Mae [subject] + wedi + verbal noun` (note: `wedi` replaces `yn`) | *Mae e wedi cadw* (He has saved) |
| **Pluperfect** | `Roedd [subject] + wedi + verbal noun` | *Roedd e wedi cadw* (He had saved) |
| **Future** | `Bydd [subject] + yn + verbal noun` | *Bydd e'n cadw* (He will save) |
| **Conditional** | `Byddai [subject] + yn + verbal noun` | *Byddai e'n cadw* (He would save) |

**Hard rules:**
- ✗ `Mae'n yn cadw` — DOUBLE `yn`. `Mae'n` already contracts `Mae + yn`.
- ✗ `Mae e wedi yn cadw` — `wedi` REPLACES `yn`, not added to it.
- ✗ `Mae'n gadw` — progressive `yn` does NOT trigger mutation.
- ✓ `Mae'n cadw` — verbal noun stays in dictionary form after progressive `yn`.

### 6. Inflected Prepositions (severity 2.0)

Welsh prepositions **conjugate for person and number**. Unlike English (where prepositions are invariable: *on me, on you, on him* all use the same "on"), Welsh inflects the preposition itself.

**Example: `ar` (on)**

| Person | Form | Meaning |
|--------|------|---------|
| 1st sg. | **arnaf fi** / **arna i** | on me |
| 2nd sg. (ti) | **arnat ti** | on you (ti) |
| 3rd sg. m. | **arno fe** / **arno fo** | on him |
| 3rd sg. f. | **arni hi** | on her |
| 1st pl. | **arnon ni** | on us |
| 2nd pl. / formal | **arnoch chi** | on you (chi) |
| 3rd pl. | **arnyn nhw** | on them |

**Example: `i` (to)**

| Person | Form |
|--------|------|
| 1st sg. | **i mi / i fi** |
| 2nd sg. | **i ti** |
| 3rd sg. m. | **iddo fe** |
| 3rd sg. f. | **iddi hi** |
| 1st pl. | **i ni** |
| 2nd pl. | **i chi** |
| 3rd pl. | **iddyn nhw** |

**Example: `gan` (by / with possession)** — also used to express HAVE in Welsh

| Person | Form | Meaning |
|--------|------|---------|
| 1st sg. | **gen i** / **gennyf** | by me / I have |
| 2nd sg. | **gen ti** / **gennyt** | by you / you (ti) have |
| 3rd sg. m. | **ganddo fe** / **ganddo fo** | by him / he has |
| 3rd sg. f. | **ganddi hi** | by her / she has |
| 1st pl. | **gennyn ni** / **gennym ni** | by us / we have |
| 2nd pl. | **gennych chi** | by you (chi) / you have |
| 3rd pl. | **ganddyn nhw** | by them / they have |

**Critical for UI:**
- "You have 3 new files" = **Mae gennych chi 3 ffeil newydd** (formal) — NOT *Mae chi 3 ffeil newydd*.
- "Send it to me" = **Anfonwch ef ataf fi** — NOT *Anfonwch ef i fi*.
- "On your screen" = **Ar eich sgrin** — but "on me" pronouns require the inflected form *arnaf fi*.

### 7. Two-Gender System (severity 2.0)

Welsh has **two grammatical genders**: **masculine (gwrywaidd)** and **feminine (benywaidd)**. About 60% of nouns are masculine.

**Gender effects (the four things that change):**

| Effect | Masculine | Feminine |
|--------|-----------|----------|
| **After definite article `y`** | NO mutation: *y car* (the car) | SOFT mutation: *y **g**ath* (the cat) ← *cath* |
| **Adjective after singular noun** | NO mutation: *car mawr* (big car) | SOFT mutation: *cath **f**awr* ← *mawr* (big cat) |
| **Numeral form for 2** | **dau** + soft: *dau **g**ar* (two cars) | **dwy** + soft: *dwy **f**erch* (two girls) |
| **Numeral form for 3** | **tri** + aspirate: *tri **ch**i* (three dogs) | **tair** (NO mutation): *tair merch* (three girls) |
| **Numeral form for 4** | **pedwar** + no mutation: *pedwar ci* | **pedair** + no mutation: *pedair merch* |

**Common UI-relevant noun genders:**

| Noun | Gender | Notes |
|------|--------|-------|
| **ffeil** (file) | Feminine | y ffeil, dwy ffeil |
| **ffolder** (folder) | Masculine | y ffolder, dau ffolder |
| **cyfrifiadur** (computer) | Masculine | y cyfrifiadur |
| **gwefan** (website) | Feminine | y wefan ← soft mut. |
| **meddalwedd** (software) | Feminine | y feddalwedd ← soft mut. |
| **caledwedd** (hardware) | Feminine | y galedwedd ← soft mut. |
| **bysellfwrdd** (keyboard) | Masculine | y bysellfwrdd |
| **llygoden** (mouse) | Feminine | y lygoden ← soft mut. |
| **sgrin** (screen) | Feminine | y sgrin (s- doesn't mutate) |
| **gosodiad** (setting) | Masculine | y gosodiad (sg.) / y gosodiadau (pl.) |
| **defnyddiwr** (user) | Masculine | y defnyddiwr |
| **cyfrinair** (password) | Masculine | y cyfrinair |
| **cyfrif** (account) | Masculine | y cyfrif |
| **dolen** (link) | Feminine | y ddolen ← soft mut. |
| **iaith** (language) | Feminine | yr iaith (vowel start → yr); tair iaith |
| **dewis** (choice) | Masculine | y dewis |

**Critical errors:**

| ✗ Wrong | ✓ Correct | Reason |
|---------|-----------|--------|
| y cath | **y gath** | *cath* is feminine → soft mutation after *y* |
| y ffeil mawr | **y ffeil fawr** | *ffeil* is feminine → adj. soft-mutates |
| dau ffeil | **dwy ffeil** | *ffeil* is feminine → use *dwy* not *dau* |
| dau ffeil | **dwy ffeil** + soft mutation (already in *ffeil*) | f- doesn't mutate but *dwy* requires soft mutation context |
| tri iaith | **tair iaith** | *iaith* is feminine → use *tair* |
| pedwar gwefan | **pedair gwefan** | *gwefan* is feminine → use *pedair* |

### 8. Number System — Singular After Numerals 1-10 (severity 2.0)

Welsh uses **singular noun forms after numbers 1-10**, unlike English. For numbers 11+, the construction switches to **`o` + plural** (a partitive genitive structure).

| Count | Pattern | Example |
|-------|---------|---------|
| 1 | singular | **un ffeil** (one file) |
| 2 | `dau/dwy` + soft mut. + singular | **dwy ffeil** (two files) |
| 3 | `tri/tair` (+ aspirate for m.) + singular | **tair ffeil** (three files); **tri chi** (three dogs) |
| 4 | `pedwar/pedair` + singular | **pedair ffeil** (four files) |
| 5 | `pump` + singular | **pump ffeil** (five files) — sometimes *pum* (shortened form) before consonant |
| 6 | `chwech` + singular | **chwe ffeil** (six files) — *chwe* shortened; aspirate mut. on c/p/t |
| 7 | `saith` + singular | **saith ffeil** (seven files) |
| 8 | `wyth` + singular | **wyth ffeil** (eight files) |
| 9 | `naw` + singular | **naw ffeil** (nine files) |
| 10 | `deg` + singular | **deg ffeil** (ten files) |
| 11+ | numeral + `o` + plural | **15 o ffeiliau** (fifteen of files) |

| ✗ Wrong (English-style plural) | ✓ Correct (Welsh) |
|---------------------------------|-------------------|
| 5 ffeiliau | **5 ffeil** |
| dau ffeiliau | **dwy ffeil** |
| 3 ffeiliau | **3 ffeil** OR **tair ffeil** |
| 10 ffeiliau | **10 ffeil** |
| 15 ffeil | **15 o ffeiliau** |
| 100 ffeil | **100 o ffeiliau** |

**Note on traditional vs modern (decimal) number system:** Welsh historically uses a **vigesimal (base-20)** system: *un ar bymtheg* = 16 (one on fifteen), *deugain* = 40 (two-twenties), *trigain* = 60 (three-twenties). Modern Welsh, especially in UI and education, uses a **decimal** system: *un deg chwech* = 16 (one-ten-six), *pedwar deg* = 40. For UI work, **prefer the decimal system** — it's clearer and avoids confusion. Use Arabic numerals (`16`, `40`) wherever practical to sidestep the issue.

### 9. Plural Formation — Six ICU Categories (severity 2.0)

Welsh has one of the most complex plural systems among European languages. ICU plural categories:

| ICU category | Welsh count rule | Pattern | Example |
|--------------|------------------|---------|---------|
| **zero** (0) | `dim` + soft mutation + plural | dim + plural | **dim ffeiliau** (no files) |
| **one** (1) | singular, no mutation needed in many UI contexts | `un` + singular | **1 ffeil** / **un ffeil** |
| **two** (2) | `dau/dwy` + soft mut. + singular | dau/dwy + sg. | **2 ffeil** / **dwy ffeil** |
| **few** (3-6) | numeral + singular (gendered for 3,4) | tair/tri/pedair... + sg. | **3 ffeil** / **tair ffeil** |
| **many** (≥7 in some classes, often combined w/ "few") | numeral + singular | numeral + sg. | **7 ffeil** |
| **other** (11+, or default) | numeral + `o` + plural | `15 o ffeiliau` | **15 o ffeiliau** |

**Plural formation patterns (no single rule — each noun must be memorized):**

| Pattern | Singular | Plural |
|---------|----------|--------|
| **-au** (most common) | ffeil | ffeil**iau** |
| **-au** | gosodiad | gosodiad**au** |
| **-iau** | drws | dryss**iau** (also: drysau) |
| **-oedd** | iaith | iei**thoedd** |
| **-i** | llyfr | llyfr**i**au — actually *llyfrau* |
| **-od** | cath | cath**od** |
| **-ed/-iaid** | plentyn | plant (irreg.) |
| **Vowel change** | car | ceir |
| **Vowel change** | troed | traed |
| **Vowel change** | bachgen | bechgyn |
| **Irregular** | brawd | brodyr |
| **Irregular** | chwaer | chwiorydd |
| **Irregular** | dyn | dynion |

There is **no productive default plural ending** — every Welsh noun's plural must be looked up.

**UI plurals (memorize):**

| English | Singular | Plural |
|---------|----------|--------|
| file | **ffeil** | **ffeiliau** |
| folder | **ffolder** | **ffolderi** / **ffolderau** |
| setting | **gosodiad** | **gosodiadau** |
| user | **defnyddiwr** | **defnyddwyr** |
| password | **cyfrinair** | **cyfrineiriau** |
| account | **cyfrif** | **cyfrifon** |
| computer | **cyfrifiadur** | **cyfrifiaduron** |
| website | **gwefan** | **gwefannau** |
| language | **iaith** | **ieithoedd** |
| choice | **dewis** | **dewisiadau** |
| link | **dolen** | **dolenni** |
| email | **e-bost** | **e-byst** / **negeseuon e-bost** |

### 10. Adjective Placement — After the Noun (severity 1.5)

Most Welsh adjectives **follow the noun** (unlike English which puts them before):

| ✗ Wrong (English order) | ✓ Correct (Welsh order) | Gloss |
|------------------------|--------------------------|-------|
| newydd ffeil | **ffeil newydd** | file new |
| mawr cyfrifiadur | **cyfrifiadur mawr** | computer big |
| cyflym cysylltiad | **cysylltiad cyflym** | connection fast |

**Adjectives that PRECEDE the noun (small closed class — and they trigger soft mutation):**

| Adjective | Meaning | Example |
|-----------|---------|---------|
| **hen** | old | **hen** **d**ŷ (an old house) ← *tŷ* |
| **prif** | main, chief | y **prif** **b**eth (the main thing) ← *peth* |
| **unig** | only, sole | yr **unig** **dd**efnyddiwr (the only user) ← *defnyddiwr* |
| **holl** | all, whole | yr **holl** **d**defnyddwyr — actually *yr holl ddefnyddwyr* (all the users) |
| **ambell** | occasional, some | **ambell** **f**erch (some girl) ← *merch* |
| **prin** | scarce, rare | **prin** **g**i (a rare dog) ← *ci* |

**Feminine singular noun → adjective soft-mutates:**

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| merch tal | **merch dal** (← *tal*, soft mut. after fem. sg.) |
| cath mawr | **cath fawr** (← *mawr*) |
| ffeil newydd | **ffeil newydd** (*n* doesn't mutate, so no visible change) |
| gwefan da | **gwefan dda** (← *da*, soft mut.) |

### 11. Definite Article y / yr / 'r — Forms by Context (severity 1.5)

Welsh has only ONE article — the definite article — which has three contextual forms:

| Form | Use | Example |
|------|-----|---------|
| **y** | before consonants (default) | y **c**ar, y **ll**yfr |
| **yr** | before vowels (a, e, i, o, u, w, y) and silent *h* | yr **a**fon, yr **i**aith, yr **h**eddlu |
| **'r** | after a vowel (in connected speech/writing) | Mae'**r** ffeil; o'**r** cyfrifiadur |

**There is NO indefinite article.** *ci* means BOTH "dog" and "a dog" depending on context. *Mae ci yma* = "There is a dog here."

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| y afon | **yr afon** (vowel start) |
| y iaith | **yr iaith** (vowel start) |
| Mae y ffeil | **Mae'r ffeil** (after vowel) |
| Aeth e i y siop | **Aeth e i'r siop** (after vowel) |
| yr car | **y car** (consonant start) |

### 12. Possession by Juxtaposition (severity 2.0)

Welsh expresses possession by **juxtaposition** (placing nouns side by side), NOT with a preposition like English "of":

| English | ✗ Wrong (calque) | ✓ Correct (Welsh) |
|---------|------------------|--------------------|
| John's car | car o John | **car John** |
| the user's file | y ffeil o'r defnyddiwr | **ffeil y defnyddiwr** |
| the file's name | yr enw o'r ffeil | **enw'r ffeil** |
| the user's password | cyfrinair o'r defnyddiwr | **cyfrinair y defnyddiwr** |
| the company's website | gwefan o'r cwmni | **gwefan y cwmni** |
| Wales's capital | prifddinas o Gymru | **prifddinas Cymru** |

**Pattern:** `[possessed thing] + [possessor]`, with the definite article (if any) placed only before the possessor: *enw'r ffeil* = "name [of] the file."

### 13. Aspirate Mutation on "a" (and) — Easy to Forget (severity 1.5)

The conjunction **a** ("and") triggers **aspirate mutation** on c, p, t. This is one of the most commonly missed mutations in Welsh writing.

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| ffeil a cyfrif | **ffeil a chyfrif** (file and account) |
| dyn a plentyn | **dyn a phlentyn** (man and child) |
| coffi a tatws — *te*? | **coffi a the** (coffee and tea) ← well, *te* in Welsh; *te* + a = *a the* (aspirate) |
| Cymraeg a Saesneg | **Cymraeg a Saesneg** (s- doesn't mutate, OK) |
| llyfr a coffi | **llyfr a choffi** |

**Note:** `a` becomes **ac** before vowels (and silent h): *ffeil ac e-bost* (file and email).

### 14. Welsh Quotation Marks (severity 1.0)

Welsh uses **standard double quotes** `"..."` (same as English).

```
"Croeso", meddai. — "Welcome," he said.
```

Single quotes `'...'` are used for nested quotes:

```
"Dywedodd, 'Croeso'", meddai. — "He said, 'Welcome',"  she said.
```

Some traditional Welsh typography uses guillemets «...» but this is rare in modern UI.

---

## UI Conventions

### Buttons — Verbal Noun (Berfenw) — NOT Imperative

Welsh UI buttons use the **berfenw** (verbal noun) form — the dictionary form of the verb, functioning as an infinitive/gerund. This is the **established Microsoft / Apple / LibreOffice / Welsh Government convention**.

| English | ✓ Welsh button (berfenw) | ✗ Wrong (imperative) |
|---------|--------------------------|----------------------|
| Save | **Cadw** | Cadwch / Cadwa |
| Cancel | **Canslo** | Canslwch |
| Delete | **Dileu** | Dilewch |
| Copy | **Copïo** | Copïwch |
| Paste | **Gludo** | Gludwch |
| Open | **Agor** | Agorwch |
| Close | **Cau** | Caewch |
| Edit | **Golygu** | Golygwch |
| Search | **Chwilio** | Chwiliwch |
| Send | **Anfon** | Anfonwch |
| Print | **Argraffu** | Argraffwch |
| Select | **Dewis** | Dewiswch |
| Continue | **Parhau** | Parhewch |
| Next | **Nesaf** / **Ymlaen** | — |
| Back | **Yn ôl** | — |
| Submit | **Cyflwyno** | Cyflwynwch |
| Confirm | **Cadarnhau** | Cadarnhewch |
| Done | **Wedi gorffen** / **Gorffen** | — |
| OK | **Iawn** / **OK** | — |
| Upload | **Uwchlwytho** | Uwchlwythwch |
| Download | **Lawrlwytho** | Lawrlwythwch |
| Refresh | **Adnewyddu** | — |
| Settings | **Gosodiadau** | — |
| Apply | **Defnyddio** / **Cymhwyso** | — |
| Reset | **Ailosod** | — |
| Add | **Ychwanegu** | — |
| Remove | **Tynnu** | — |
| Sign in / Log in | **Mewngofnodi** | — |
| Sign out / Log out | **Allgofnodi** | — |
| Sign up / Register | **Cofrestru** | — |
| Add more | **Ychwanegu rhagor** | — (use *rhagor* not *mwy* for buttons) |
| Show more | **Dangos rhagor** | — |

**Rationale:** The berfenw (verbal noun) is register-neutral — it doesn't pick chi vs ti. This keeps button labels stable across formality levels.

### Status Messages — Periphrastic with "Wrthi'n" or "Yn"

For **in-progress** states, use periphrastic constructions with `bod` + `yn` + verbal noun. For UI status messages specifically, **`Wrthi'n + verbal noun`** is the established pattern:

| English | ✗ Wrong (bare verbal noun) | ✓ Correct (periphrastic) |
|---------|------------------------------|---------------------------|
| Loading... | Llwytho... | **Wrthi'n llwytho...** / **Yn llwytho...** |
| Saving... | Cadw... | **Wrthi'n cadw...** |
| Sending... | Anfon... | **Wrthi'n anfon...** |
| Processing... | Prosesu... | **Wrthi'n prosesu...** |
| Connecting... | Cysylltu... | **Wrthi'n cysylltu...** |
| Searching... | Chwilio... | **Wrthi'n chwilio...** |
| Translating... | Cyfieithu... | **Wrthi'n cyfieithu...** |
| Downloading... | Lawrlwytho... | **Wrthi'n lawrlwytho...** |
| Uploading... | Uwchlwytho... | **Wrthi'n uwchlwytho...** |
| Please wait | — | **Arhoswch / Os gwelwch yn dda, arhoswch** |

### Completion Messages — Impersonal Past or "Wedi'i" Construction

For **completed** states, use either the **impersonal past** (`-wyd` ending) or the **`wedi'i` + soft-mutated verbal noun** construction:

| English | ✗ Wrong | ✓ Correct |
|---------|---------|-----------|
| Saved | Cadw | **Cadwyd** / **Wedi'i gadw** (soft mut. — *cadw → gadw*) |
| Sent | Anfon | **Anfonwyd** / **Wedi'i anfon** |
| Deleted | Dileu | **Dilëwyd** / **Wedi'i ddileu** (soft mut.) |
| Done | Wedi gorffen | **Wedi gorffen** / **Wedi cwblhau** |
| Translation complete | Cwblhau cyfieithu | **Cyfieithiad wedi'i gwblhau** / **Cwblhawyd y cyfieithiad** |
| File uploaded | Uwchlwythwyd ffeil | **Uwchlwythwyd y ffeil** / **Ffeil wedi'i huwchlwytho** |
| Payment successful | Llwyddiant taliad | **Taliad llwyddiannus** / **Talwyd yn llwyddiannus** |

### Failure Messages — Impersonal Negative or "Heb"

For **failure / error** states:

| English | ✓ Welsh |
|---------|---------|
| Failed | **Methwyd** / **Ni lwyddwyd** |
| Could not save | **Ni lwyddwyd i gadw** (NOT *Methodd cadw*) |
| File not found | **Ni ddaethpwyd o hyd i'r ffeil** / **Ffeil heb ei chanfod** |
| Not saved | **Heb ei gadw** (without its-being-saved) |
| Connection lost | **Collwyd y cysylltiad** |

### Empty States — Dim or Heb

For **empty states**:

| English | ✓ Welsh |
|---------|---------|
| No results | **Dim canlyniadau** |
| No files | **Dim ffeiliau** |
| Nothing selected | **Dim wedi'i ddewis** / **Heb ddewis dim** |
| No notifications | **Dim hysbysiadau** |
| Empty | **Gwag** |

### Drag-and-Drop

- drag → **llusgo** (native Welsh — NOT *dragio*)
- drop / release → **gollwng** (native Welsh — NOT *rhyddhau* which means "liberate")

| English | ✓ Welsh |
|---------|---------|
| Drag files here | **Llusgwch ffeiliau yma** |
| Drop to upload | **Gollwng i uwchlwytho** |
| Release to upload | **Gollwng i uwchlwytho** (NOT *Rhyddhau i uwchlwytho*) |

### File Picker — `Dewis` not `Pori`

For **file selection**, use the action-oriented verb **dewis** (select/choose), NOT the navigation verb **pori** (browse):

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| Pori am ffeiliau | **Dewis ffeiliau** |
| Cliciwch i bori | **Cliciwch i ddewis** (note soft mut. on *dewis* after *i*) |
| Pori | **Dewis ffeil** / **Dewis** |

### "More" — `Rhagor` not `Mwy` (for buttons)

For button idioms expressing "more", **rhagor** is more natural and formal than **mwy** in UI:

| ✗ Less natural | ✓ More natural |
|----------------|----------------|
| Ychwanegu mwy | **Ychwanegu rhagor** |
| Dangos mwy | **Dangos rhagor** |
| Llwytho mwy | **Llwytho rhagor** |

### Error Messages — What + Next Step

Welsh UI errors follow the pattern *what went wrong* + *what to do next*:

| ✗ Bare | ✓ With next step |
|--------|-------------------|
| Ffeil heb ei chanfod. | **Ffeil heb ei chanfod. Gwiriwch y llwybr.** (File not found. Check the path.) |
| Gwall rhwydwaith. | **Gwall rhwydwaith. Rhowch gynnig arall.** (Network error. Try again.) |
| Cyfrinair anghywir. | **Cyfrinair anghywir. Ceisiwch eto.** (Wrong password. Try again.) |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Welsh | Notes |
|------|-------|-------|
| Question mark | `?` | Same as English |
| Comma | `,` | Different conjunction rules — see below |
| Period | `.` | Same |
| Colon | `:` | Same |
| Quotation marks | `"..."` (standard) | Same as English |
| Nested quotes | `'...'` | Single inside double |
| Apostrophe | `'` | Used in contractions (Mae'r, o'r, i'r) |

### Comma Rules

| Rule | Example |
|------|---------|
| **NO comma** before `a / ac` (and) | Llyfr **a** cherdyn (book and card) — NOT *Llyfr, a cherdyn*. |
| **NO comma** before `neu` (or) | Ffeil **neu** ffolder — NOT *Ffeil, neu ffolder*. |
| **Comma** before `bod` (that, subordinating) | Gwn**,** **bod** y ffeil yn gywir. |
| **Comma** before `os` (if) | Cadwch y ffeil**,** **os** ydych yn barod. |
| **Comma** before `pan` (when) | Anfonwch e-bost**,** **pan** fyddwch yn barod. |
| **Comma** before `achos` / `oherwydd` (because) | Methodd**,** **oherwydd** gwall rhwydwaith. |
| **Comma** before `ond` (but) | Cyflym**,** **ond** dibynadwy. |

### Numbers

Welsh follows **UK / Anglo number formatting** (not continental European):

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **comma (,)** | 1,234,567 |
| Decimal separator | **period (.)** | 3.14 / 99.99 |
| Negative | `-25` | |
| Percent | `25%` or `25 %` | |

| ✗ Wrong (continental) | ✓ Correct (Welsh/UK) |
|------------------------|----------------------|
| 1.234,56 | **1,234.56** |
| 3,14 | **3.14** |
| 1 234 | **1,234** |

### Dates

| Format | Example | Use |
|--------|---------|-----|
| **DD/MM/YYYY** | **15/01/2024** | Default Welsh format (UK convention) |
| D Month YYYY | **15 Ionawr 2024** | Long-form prose |
| D'ed/-fed Month YYYY | **15fed Ionawr 2024** | With ordinal suffix (more formal) |
| YYYY-MM-DD | 2024-01-15 | Technical/API only |

**Welsh month names (CAPITALIZED):**

| # | Welsh |
|---|-------|
| 1 | **Ionawr** |
| 2 | **Chwefror** |
| 3 | **Mawrth** |
| 4 | **Ebrill** |
| 5 | **Mai** |
| 6 | **Mehefin** |
| 7 | **Gorffennaf** |
| 8 | **Awst** |
| 9 | **Medi** |
| 10 | **Hydref** |
| 11 | **Tachwedd** |
| 12 | **Rhagfyr** |

**Welsh weekday names (lowercase in the format `dydd X`):**

| Day | Welsh |
|-----|-------|
| Monday | **dydd Llun** |
| Tuesday | **dydd Mawrth** |
| Wednesday | **dydd Mercher** |
| Thursday | **dydd Iau** |
| Friday | **dydd Gwener** |
| Saturday | **dydd Sadwrn** |
| Sunday | **dydd Sul** |

Note: `dydd` (day) is lowercase; the day name itself is capitalized (e.g., *dydd Llun*). Week starts **Monday**.

### Time

- 24-hour preferred: **14:30**.
- 12-hour with **y.b.** (yn y bore = a.m.) / **y.p.** (yn y prynhawn = p.m.) / **y.h.** (yn yr hwyr = evening): **2:30 y.p.**

### Currency — GBP (£) — Wales Uses British Pound

| Format | Pattern | Example |
|--------|---------|---------|
| Symbol before amount | `£` | **£99.99** |
| With pence | period decimal | **£99.99** (not £99,99) |
| ISO code | GBP | **99.99 GBP** |
| Large amounts | comma thousands | **£1,234.56** |

Wales is part of the United Kingdom and uses the **British pound sterling (£, GBP)**. Wales does NOT use the euro. Penny/pence are subdivisions: 100 pence = £1.

**Welsh words:**
- pound = **punt** (plural: **punnoedd / punt**)
- pence = **ceiniog** (plural: **ceiniogau**)
- £99.99 = "naw deg naw punt naw deg naw ceiniog" (literal) — but in UI just write **£99.99**.

---

## Terminology — Welsh Native Terms (Established UI Vocabulary)

Welsh has an active terminology coordination effort — primarily through **BydTermCymru** (the National Terminology Portal of the Welsh Government) and **Y Termiadur Addysg** (the educational terminology standard). For UI work, use established Welsh terms:

| English | ✓ Welsh (preferred) | ✗ Avoid (anglicism) | Notes |
|---------|---------------------|----------------------|-------|
| save | **cadw** | seifio | "to keep" — native verb |
| delete | **dileu** | deletio | native verb |
| copy | **copïo** | — | accepted Welsh form of borrowed verb |
| paste | **gludo** | pestio | "to stick" — native |
| cut | **torri** | cytio | "to cut/break" — native |
| open | **agor** | opnio | native |
| close | **cau** | clôsio | native |
| file | **ffeil** | — | borrowed but Welshified |
| folder | **ffolder** | — | borrowed but accepted |
| settings | **gosodiadau** | settings | native plural |
| upload | **uwchlwytho** | uploadio | "load upwards" — native compound |
| download | **lawrlwytho** | downloadio | "load downwards" — native compound |
| search | **chwilio** | sêrtsio | native |
| click | **clicio** | — | accepted borrowing |
| computer | **cyfrifiadur** | compiwtar | "calculator" — native coinage |
| software | **meddalwedd** | software | "soft-ware" calque, native |
| hardware | **caledwedd** | hardware | "hard-ware" calque, native |
| internet | **rhyngrwyd** | internet (also OK) | "inter-net" — native calque |
| browser | **porwr** | browser | "grazer" — native |
| website | **gwefan** | website | "web-place" — native |
| email | **e-bost** | email | "e-post" — native |
| password | **cyfrinair** | password | "secret-word" — native |
| user | **defnyddiwr** | user | native; pl. *defnyddwyr* |
| account | **cyfrif** | account | "calculation/count" — native |
| log in | **mewngofnodi** | logio | "log-in" — native compound |
| log out | **allgofnodi** | logio allan | "log-out" — native |
| cancel | **canslo** | — | accepted borrowing |
| print | **argraffu** | — | native |
| send | **anfon** | — | native |
| select | **dewis** | selectio | native (also "choice") |
| dashboard | **dangosfwrdd** | dashboard | "show-board" — native |
| app / application | **ap** (informal) / **rhaglen** (formal) | — | both accepted |
| link | **dolen** | link | "loop" — native |
| menu | **dewislen** | menu | "choice-page" — native |
| screen | **sgrin** | — | accepted borrowing |
| keyboard | **bysellfwrdd** | keyboard | "keys-board" — native |
| mouse | **llygoden** | mouse | "mouse" — native (same animal) |
| icon | **eicon** | — | accepted borrowing |
| error | **gwall** | error | native |
| warning | **rhybudd** | warning | native |
| help | **help** / **cymorth** | — | both used |
| support | **cefnogaeth** | support | native |
| feedback | **adborth** | feedback | "echo-talk" — native |
| privacy | **preifatrwydd** | privacy | native |
| terms | **telerau** | terms | native |
| language | **iaith** (sg.) / **ieithoedd** (pl.) | — | native |
| color | **lliw** | colour | native |
| size | **maint** | size | native |
| font | **ffont** | — | accepted borrowing |
| update (v.) | **diweddaru** | updatio | "to date-up" — native |
| share | **rhannu** | — | "to share/divide" — native |
| profile | **proffil** | — | accepted borrowing |
| notifications | **hysbysiadau** | notifications | "announcements" — native |
| home | **hafan** | home | "haven/home" — native |
| URL | **URL** / **gwe-gyfeiriad** | — | URL acceptable in tech contexts |
| WiFi | **WiFi** / **diwifr** | — | WiFi acceptable |
| device | **dyfais** | device | "invention" — native |
| video | **fideo** | — | accepted borrowing |
| photo | **llun** / **ffotograff** | — | both used |
| sync | **cysoni** | — | "to harmonize" — native |
| build (sw.) | **adeiladu** | — | native |
| deploy | **defnyddio** / **gosod** | — | native |
| log (n.) | **cofnod** / **cofnodion** | — | native |

### Brand Names and Tech Identifiers — Keep As-Is

Inside Welsh text, these stay in English / Latin:
- **Brand names**: Google, Microsoft, Apple, GitHub, Facebook, Twitter
- **Tech identifiers**: Git, Docker, npm, pip, HTTP, REST, JSON, XML, API, URL
- **Codes/commands/paths**: command names, file paths, code samples
- **Placeholders**: `{name}`, `{count}`, `%s`

**Critical: do NOT mutate brand names.** Even when grammatical context would normally trigger a mutation, brand names stay exactly as the brand spells them:

| ✗ Wrong (mutated) | ✓ Correct (preserved) |
|-------------------|------------------------|
| Gyda **G**oogle (should soft mut. *G* → ∅?) | **Gyda Google** |
| O **F**acebook | **O Facebook** |
| Yn **Ng**oogle | **Yn Google** |

---

## Calque / Anti-Pattern Blocklist (Avoid English Calques)

Welsh-language identity is culturally important. Calques (literal translations) from English read as lazy or anglicized. Replace them with native Welsh expressions:

| ✗ English calque | ✓ Native Welsh | Note |
|------------------|-----------------|------|
| **Ar ddiwedd y dydd** (at the end of the day) | **Yn y pen draw** / **Wedi'r cwbl** | English idiom calque |
| **Gwneud synnwyr** (makes sense) | **Bod yn synhwyrol** / **Mae'n gwneud sens** (colloquial OK) | "Makes sense" calque |
| **Ar yr un dudalen** (on the same page) | **Yn cytuno** / **O'r un farn** | "Same page" calque |
| **Torri coes** (break a leg) | **Pob lwc!** / **Dal ati!** | Use native good-luck idiom |
| **Darn o gacen** (piece of cake) | **Hawdd fel baw** / **Dim problem** | Use native easy idiom |
| **Mae'n cymryd lle** (it takes place) | **Mae'n digwydd** / **Mae'n cael ei gynnal** | "Take place" calque — use *digwydd* |
| **Mae e wedi mynd yn ôl ar ei air** (gone back on his word) | **Mae e wedi torri ei air** | Use native idiom |
| **Yn seiliedig ar** (based on — as sentence opener) | **Ar sail** / **Yn ôl** | Verbose calque |
| **Er mwyn i** (in order to) | **Er mwyn** / **I** | Verbose — short form suffices |
| **actwali** | **mewn gwirionedd** / **a dweud y gwir** | Anglicism — use native |
| **siŵr** (informal for "sure") | **sicr** / **pendant** (in formal UI) | *siŵr* is OK colloquially but use *sicr* in UI |
| **jyst** | **dim ond** / **yn unig** | Anglicism — use native |
| **rili** (really) | **mewn gwirionedd** / **iawn** | Anglicism |
| **OK** (in body text) | **Iawn** / **O'r gorau** | Use native (OK accepted in buttons) |
| **AI-yredig** ("AI-driven" calque) | **gyda chymorth AI** / **wedi'i bweru gan AI** | Compound-adjective calque |
| **X-bwerus** ("X-powered" suffix) | **wedi'i bweru gan X** | Compound suffix calque |
| **Gwneud cyfraniad** (make a contribution) | **Cyfrannu** | Use verb, not "make + noun" |
| **Gwneud penderfyniad** (make a decision) | **Penderfynu** | Use verb |
| **Cael profiad** (have an experience) | **Profi** | Use verb |
| **Y ffeil ddim gallu bod wedi'i ffeindio** | **Ni ddaethpwyd o hyd i'r ffeil** / **Ffeil heb ei chanfod** | Passive construction calque |
| **Unol Daleithiau America** (in UI body) | **UDA** | Use abbreviation in UI |

### Compound Adjective Calques (avoid)

English compound adjectives like *AI-powered*, *cloud-based*, *data-driven* do NOT calque well into Welsh. Restructure:

| ✗ Calque | ✓ Welsh natural |
|----------|-----------------|
| AI-yredig | **gyda chymorth AI** / **wedi'i bweru gan AI** / **yn defnyddio AI** |
| cloud-based | **yn seiliedig ar y cwmwl** / **wedi'i seilio ar y cwmwl** |
| data-driven | **wedi'i yrru gan ddata** / **yn seiliedig ar ddata** |
| user-friendly | **hawdd ei ddefnyddio** ("easy to use") |
| AI-powered | **wedi'i bweru gan AI** |

---

## Self-Check Checklist (Run Before Returning Output)

### Identity (auto-fail on miss)
- [ ] Output is **Welsh (Cymraeg)**, NOT Irish/Gaelic, NOT English.
- [ ] No Gaelic vocabulary (no *Sláinte*, *Fáilte*, *Slán*).
- [ ] Welsh letters used: **w, y, ŵ, ŷ, â, ê, î, ô, û**.
- [ ] No grave accents (Welsh uses circumflex, never grave).

### Mutations (auto-fail)
- [ ] **Soft mutation** applied after: dy, ei (his), y (before fem. sg.), i, o, am, ar, at, gan, dros, drwy, wrth, neu (sometimes), yn (adverbial/predicative), dau/dwy, prif/hen/unig/holl.
- [ ] **Nasal mutation** applied after: fy, yn (locative — "in" + place).
- [ ] **Aspirate mutation** applied after: ei (her), a (and), â (with), gyda, tri, chwe, tua.
- [ ] **No mutation** after: ein, eich, eu, yn (progressive — before verbal noun).
- [ ] Direct object of inflected (conjugated) verb is soft-mutated.
- [ ] Adjective after feminine singular noun is soft-mutated.

### Welsh Alphabet & Spelling (auto-fail)
- [ ] **Digraphs** (ch, dd, ff, ng, ll, ph, rh, th) treated as single letters — not split.
- [ ] **To bach (â ê î ô û ŵ ŷ)** preserved where meaning-critical (tŷ, cŵn, ŵy).
- [ ] **ŵ and ŷ** (uniquely Welsh) preserved — not stripped to plain w/y.
- [ ] No ASCII-stripping of accents.

### Word Order (auto-fail)
- [ ] **VSO** in main clauses — verb first (Cadwodd y defnyddiwr y ffeil).
- [ ] Periphrastic constructions use *bod + yn + berfenw* (Mae'n cadw).
- [ ] Subject does NOT precede the verb in main clauses.

### Articles & Possession
- [ ] Definite article correct: **y** (before consonants), **yr** (before vowels/h), **'r** (after vowel).
- [ ] No indefinite article (don't insert "a" or "an" calque).
- [ ] Possession by **juxtaposition** (car John, not car o John).

### Pronouns & Register
- [ ] **chi / ti consistent** throughout — never mix.
- [ ] If chi: **eich** (no mutation), `-wch` imperatives.
- [ ] If ti: **dy** (+ soft mutation), `-a` imperatives.
- [ ] Buttons use **berfenw** (Cadw, Dileu — register-neutral).
- [ ] **Inflected prepositions** used correctly (arnaf fi, iddi hi, ganddyn nhw).

### Gender & Number
- [ ] **Gender** correct on nouns (ffeil = f., cyfrifiadur = m., gwefan = f.).
- [ ] **Feminine sg. noun** soft-mutates after y AND triggers soft mutation on following adjective.
- [ ] **dau / dwy**, **tri / tair**, **pedwar / pedair** match noun gender.
- [ ] **Singular noun** after numerals 1-10 (5 ffeil, not 5 ffeiliau).
- [ ] **"o" + plural** for numerals 11+ (15 o ffeiliau).
- [ ] Plural form correct per noun (ffeil → ffeiliau, iaith → ieithoedd, dyn → dynion).

### Verbs
- [ ] Periphrastic *bod + yn + berfenw* for present/past continuous.
- [ ] `wedi` (perfect) REPLACES `yn`, not added to it.
- [ ] No double `yn` (Mae'n yn cadw ✗ → Mae'n cadw ✓).
- [ ] Impersonal past `-wyd` for completion (Cadwyd, Anfonwyd).
- [ ] "Wedi'i" + soft-mutated berfenw for completion alternative (Wedi'i gadw).
- [ ] "Heb" + soft-mutated berfenw for negation (Heb ei gadw).
- [ ] "Ni lwyddwyd i" + berfenw for failure (Ni lwyddwyd i gadw).

### UI Conventions
- [ ] Buttons in **berfenw** (Cadw, Dileu, Copïo, Agor).
- [ ] Status messages with **Wrthi'n + berfenw** (Wrthi'n cadw...).
- [ ] Completion with impersonal past or `Wedi'i` + soft-mut. berfenw.
- [ ] Drag-and-drop: **llusgo / gollwng** (not *dragio / rhyddhau*).
- [ ] File picker: **dewis** (not *pori*).
- [ ] "More" buttons: **rhagor** (not *mwy*).
- [ ] Empty states: **Dim X** / **Heb ddim**.
- [ ] Error messages include next step.

### Punctuation & Numbers
- [ ] **Decimal**: period (3.14).
- [ ] **Thousands**: comma (1,234).
- [ ] **NO comma** before *a / ac / neu*.
- [ ] **Comma** before *bod / os / pan / oherwydd / ond*.
- [ ] **Quotation marks**: "..." (standard, same as English).

### Dates & Currency
- [ ] **DD/MM/YYYY** date format (UK convention).
- [ ] Months capitalized: **Ionawr, Chwefror, Mawrth, Ebrill, Mai, Mehefin, Gorffennaf, Awst, Medi, Hydref, Tachwedd, Rhagfyr**.
- [ ] Days lowercase with `dydd`: **dydd Llun, dydd Mawrth...**.
- [ ] **GBP £** currency, NOT EUR (Wales uses British pound).
- [ ] **Period decimal** on currency: £99.99, not £99,99.

### Terminology
- [ ] Native Welsh terms used: **cadw, dileu, lawrlwytho, uwchlwytho, cyfrifiadur, meddalwedd, cyfrinair, defnyddiwr, gosodiadau**.
- [ ] No anglicism-verbs (no *seifio, deletio, downloadio, uploadio*).
- [ ] Brand names unchanged (Google, NOT mutated).
- [ ] No English plurals (no *ffeils*; use *ffeiliau*).

### Calques
- [ ] No "make + noun" calques (use the verb: *Cyfrannu*, not *Gwneud cyfraniad*).
- [ ] No "at the end of the day" calque (use *Yn y pen draw*).
- [ ] No "X-powered" compound-adj calques (use *wedi'i bweru gan X*).
- [ ] No passive-voice English calques (use Welsh impersonal *-wyd*).

---

## Worked Examples

### Example 1 — Standard cy UI (chi formal)

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** professional product UI → **chi formal**, native Welsh vocabulary, berfenw buttons.

**Translation:**

> Croeso 'nôl! Mae gennych chi 3 ffeil newydd yn eich cyfrif. Cliciwch ar **Parhau** i'w hadolygu neu **Canslo** i aros yma. Wrthi'n cadw eich newidiadau…

**Why this works:**
- **Croeso 'nôl** — "Welcome back" (native idiom; *'nôl* is contracted *yn ôl*).
- **Mae gennych chi** — "Have you" — uses inflected preposition *gennych* (`gan` conjugated for *chi*). Welsh expresses HAVE with `gan` + person.
- **3 ffeil newydd** — singular *ffeil* after numeral (per Welsh number rule); *newydd* follows the noun (post-nominal adjective). No mutation needed because *ffeil* is feminine but *newydd* starts with *n* which doesn't mutate.
- **yn eich cyfrif** — "in your account": *yn* here is the predicative/locative use (no mutation needed because we're treating it as connector with possessive *eich* which itself takes no mutation). *cyfrif* is masculine.
- **Cliciwch ar Parhau** — chi-form imperative *Cliciwch* (-wch ending); *ar* governs subsequent noun; *Parhau* is the button label (berfenw, register-neutral).
- **i'w hadolygu** — "to review them": *i* + *eu* (their) → *i'w*; *adolygu* takes *h-* before vowel-starting verbal noun when preceded by certain particles (specifically *ei/eu* in 3rd person object construction).
- **neu Canslo** — "or Cancel": *neu* (or) takes no mutation in modern Welsh.
- **i aros yma** — "to stay here": *aros* (to wait/stay) is the berfenw; *yma* (here).
- **Wrthi'n cadw eich newidiadau…** — status message in periphrastic form. *Wrthi'n* = "in the act of"; *cadw* = berfenw (no mutation after progressive *yn*); *eich newidiadau* = "your changes" (no mutation after *eich*).
- All to bach (none in this text) and digraphs (ch in *cliciwch*, *adolygu*) preserved.

### Example 2 — Mutation Showcase

**Source:** I saw my dog and her cat in Cardiff.

**Translation:**

> Gwelais fy nghi a'i chath yng Nghaerdydd.

**Mutation analysis:**
- **fy nghi** — "my dog": *fy* triggers **nasal mutation** on *ci* → *nghi*.
- **a'i** — "and her": *a* + *ei* (her) → *a'i* (contracted).
- **chath** — "cat" after *ei* (her) → **aspirate mutation** *cath* → *chath*.
- **yng Nghaerdydd** — "in Cardiff": *yn* (locative) triggers **nasal mutation** on *Caerdydd* → *Nghaerdydd*; *yn* itself becomes *yng* before *ng-/ngh-*.
- **Gwelais** — 1st sg. past of *gweld* (to see); inflected verb form (not periphrastic).

This single sentence demonstrates all three mutation systems and the *yn → yng* sandhi change.

### Example 3 — Periphrastic Verb Constructions

**Source:** The user is downloading the file. The file has been saved.

**Translation:**

> Mae'r defnyddiwr yn lawrlwytho'r ffeil. Mae'r ffeil wedi'i chadw.

**Analysis:**
- **Mae'r defnyddiwr** — "Is-the-user" — VSO with auxiliary *bod*; *Mae* + *yr* → *Mae'r*.
- **yn lawrlwytho** — progressive *yn* + verbal noun *lawrlwytho*; NO mutation (progressive *yn* never mutates).
- **'r ffeil** — "the file" (definite article *'r* after vowel of *lawrlwytho*).
- **Mae'r ffeil wedi'i chadw** — "Is-the-file having-its saved": perfect aspect uses *wedi* + *ei* (its, referring back to *ffeil* feminine) + soft-mutated verbal noun. *ffeil* is feminine, so *ei* (her/its-fem.) triggers **aspirate mutation** on *cadw* → *chadw*.

Wait — *ei* for feminine triggers aspirate, but for masculine triggers soft. *cadw* starts with *c*. Aspirate of *c* is *ch*. So *wedi'i chadw* is correct here (because *ffeil* is feminine).

If the subject were masculine (e.g., *cyfrif* = account, masc.): *Mae'r cyfrif wedi'i gadw* (soft mutation *c* → *g*).

### Example 4 — VSO with Inflected vs Periphrastic Verbs

**Source (with inflected verb — past):** The user saved the file.

> Cadwodd y defnyddiwr y ffeil.

- **Cadwodd** — 3rd sg. past of *cadw* (inflected). Comes FIRST (VSO).
- **y defnyddiwr** — subject (definite article + noun).
- **y ffeil** — direct object. Direct object after inflected verb takes **soft mutation** if the object starts with a mutable consonant — but *ffeil* starts with *ff* which doesn't soft-mutate (ff is already in the mutated form of *p*; ff doesn't further mutate to anything in soft mutation).

**Source (periphrastic — present continuous):** The user is saving the file.

> Mae'r defnyddiwr yn cadw'r ffeil.

- **Mae** — 3rd sg. of *bod* (to be).
- **'r defnyddiwr** — subject.
- **yn cadw** — progressive *yn* + berfenw *cadw* (no mutation).
- **'r ffeil** — direct object (no mutation in periphrastic — object mutation rule only applies to direct objects of INFLECTED verbs, not periphrastic).

### Example 5 — Anglicism Rejection

**Source:** Click here to download the software update.

**✗ Wrong (anglicism-heavy):**

> Clicia yma i downloadio'r software update.

**✓ Correct (native Welsh):**

> Cliciwch yma i lawrlwytho'r diweddariad meddalwedd.

**Notes:**
- *downloadio* → **lawrlwytho** ✓ (native)
- *software* → **meddalwedd** ✓ (native)
- *update* (n.) → **diweddariad** ✓ (native, from *diweddaru* = to update)
- **i lawrlwytho** — *i* (to) triggers soft mutation: *lawrlwytho* (no visible change because *l* → *l*, but mutation rule applies).
- **'r diweddariad meddalwedd** — possession by juxtaposition: "the update [of] software" → *diweddariad meddalwedd* (no preposition).

### Example 6 — Currency (GBP)

**Source:** Subscription: £9.99 / month.

**Translation:**

> Tanysgrifiad: £9.99 y mis.

- **Tanysgrifiad** — "subscription" (native).
- **£9.99** — UK number format (period decimal). Welsh follows Anglo convention.
- **y mis** — "the month" — Welsh uses *y* before the time unit for periodic charges.

### Example 7 — Inflected Prepositions in Action

**Source:** Send the file to me. Show it to her.

**Translation:**

> Anfonwch y ffeil ata i. Dangoswch hi iddi hi.

- **Anfonwch** — chi imperative of *anfon* (send).
- **ata i** — inflected form of *at* (towards) for 1st sg.: *at + fi → ata i*.
- **Dangoswch hi** — chi imperative + *hi* (it-fem., referring to *ffeil* which is feminine).
- **iddi hi** — inflected form of *i* (to) for 3rd sg. fem.: *i + hi → iddi hi*.

### Example 8 — Numbers with Gender

**Source:** 2 dogs, 2 cats, 3 files, 3 men.

**Translation:**

> dau gi, dwy gath, tair ffeil, tri dyn.

- **dau gi** — *ci* (dog) is masc. → *dau* + soft mut. *ci* → *gi*.
- **dwy gath** — *cath* (cat) is fem. → *dwy* + soft mut. *cath* → *gath*.
- **tair ffeil** — *ffeil* is fem. → *tair* (fem. form of three); *ff* doesn't aspirate-mutate.
- **tri dyn** — *dyn* (man) is masc. → *tri* (masc. form); *d* doesn't aspirate-mutate (only c/p/t aspirate-mutate, but *tri* triggers aspirate only on c/p/t — *d* is unaffected).

---

## When in Doubt

1. **Default to cy / Welsh standard written, chi formal register, native Welsh vocabulary, berfenw buttons, DD/MM/YYYY dates, GBP £ currency (1,234.56 format).**
2. **Check mutations first** — if the source has a word like *fy / dy / ei / y / a / yn / o / i / am / ar*, the next word probably mutates. Confirm: soft / nasal / aspirate?
3. **VSO** — if you wrote *Y defnyddiwr cadwodd*, restructure to *Cadwodd y defnyddiwr*.
4. **No indefinite article** — don't translate English "a/an" as a word; just omit.
5. **Possession by juxtaposition** — don't insert *o* between possessed and possessor: *car John*, not *car o John*.
6. **Inflected prepositions** — if pronoun follows preposition, use the conjugated form (*arnaf fi*, *iddi hi*, *ganddyn nhw*), not bare preposition + pronoun.
7. **Periphrastic verbs** — for present/past continuous, use *bod + yn + berfenw* (*Mae'n cadw*, *Roedd e'n cadw*). Never double *yn*. *wedi* replaces *yn* for perfect aspect.
8. **Numbers** — singular noun after 1-10, *o* + plural for 11+. *dau/dwy*, *tri/tair*, *pedwar/pedair* must match gender.
9. **Gender** — if you don't know a noun's gender, look it up. Get it wrong and adjectives + articles will be wrong too.
10. **chi/ti consistency** — pick one register and stick with it throughout. Buttons use berfenw (neutral).
11. **Buttons use berfenw**, NOT imperative — *Cadw*, not *Cadwch*. This is the established Welsh software convention.
12. **Status messages** — *Wrthi'n + berfenw* (in-progress), impersonal *-wyd* past (completed).
13. **Anglicisms** — if you wrote *seifio, deletio, downloadio, uploadio*, fix to *cadw, dileu, lawrlwytho, uwchlwytho*.
14. **To bach (circumflex)** — preserve on long vowels; *tŷ* (house), *cŵn* (dogs), *gŵr* (husband/man). Never strip to plain *ty, cwn, gwr*.
15. **Digraphs are single letters** — *ch, dd, ff, ng, ll, ph, rh, th*. Don't split them in hyphenation; don't sort them as two letters.
16. **Currency is £ GBP**, not € EUR — Wales uses British pound.
17. **Brand names don't mutate** — *gyda Google*, not *gyda Oogle*; *o Facebook*, not *o Vacebook*.
18. **If you're unsure about a mutation, ask: "what's the trigger word?"** — Then look up which mutation that trigger requires. The trigger determines the mutation, not the mutating word itself.
19. **Reference official terminology**: BydTermCymru (https://termau.cymru/) and Y Termiadur Addysg for established Welsh tech terms.
20. **Cymraeg Clir** — favor clear, accessible Welsh in UI. Avoid archaic or overly literary forms unless the context calls for them.
