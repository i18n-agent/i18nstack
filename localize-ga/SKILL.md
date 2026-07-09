---
name: localize-ga
description: Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Irish / Gaeilge for Ireland. Irish is a Celtic Goidelic language (sister to Scottish Gaelic and Manx — NOT same branch as Welsh, which is Brittonic). THE defining critical features are (1) two initial consonant mutation systems — séimhiú (lenition, marked by inserted h: b→bh, c→ch, d→dh, f→fh, g→gh, m→mh, p→ph, s→sh, t→th) and urú (eclipsis, marked by prepended consonant: b→mb, c→gc, d→nd, f→bhF, g→nG, p→bP, t→dT) — each triggered by specific particles, possessives, prepositions, and number ranges; (2) VSO word order (verb-first: "Shábháil an t-úsáideoir an comhad" not subject-first); (3) broad vs slender consonant orthography (caol le caol, leathan le leathan — surrounding vowels must match in front/back quality); (4) long vowels with fada (´): á é í ó ú are meaning-critical and NEVER optional. Other key features: copula `is` (identity/classification) vs substantive verb `tá` (state/location) — distinct verbs that mean different things; inflected prepositional pronouns (agam/agat/aige/aici/againn/agaibh/acu — preposition + pronoun fused into one word, NEVER `ag mé`); no verb "to have" (use `tá X ag Y` = "is X at Y"); singular noun after numbers 1-10 with mutation by range (1-6 = lenition, 7-10 = eclipsis); no indefinite article ("cat" = cat OR a cat; "an cat" = the cat); 2 genders with feminine lenition after `an` (an bhean) and adjective lenition after fem. nouns (bean mhór); genitive case (an tuiseal ginideach) after verbal nouns and compound prepositions (ag sábháil an chomhaid); no yes/no words — answer with the verb itself (Q: An bhfuil tú anseo? A: Tá / Níl); verbal noun (ainm briathartha) used for English gerund/infinitive (ag scríobh = writing); button labels use verbal noun form (Sábháil, Scrios — NOT autonomous); status messages use Ag + verbal noun (Ag sábháil…); EUR currency since 2002 with Anglo number format (€1,234.56 — period decimal, comma thousands — UNLIKE most of Europe); DD/MM/YYYY dates; Béarlachas (anglicism calque) is the named, well-known anti-pattern — direct word-for-word from English is the principal quality failure to avoid (Tá brón orm NOT Tá mé sorry; Conas atá tú NOT Conas tá tú); no comma before agus (and) / nó (or); comma before go/má/dá/mar/nuair/a in subordinating contexts. Irish is the FIRST official language of Ireland under the Constitution — UI for ga carries cultural weight even though only ~1-2% are native speakers. Reference authorities: An Caighdeán Oifigiúil (Official Standard), tearma.ie (national terminology database), teanglann.ie, focloir.ie.
---

# Localize: Irish / Gaeilge (ga → Gaeilge)

## Scope & Variants

Irish (Gaeilge) is the **first official language of the Republic of Ireland** under Article 8 of the Constitution (Bunreacht na hÉireann), with English as the second official language. It is also recognised in Northern Ireland (Identity & Language Act 2022) and is an official working language of the EU since 2007.

| Locale | Notes |
|--------|-------|
| `ga` / `ga-IE` | **An Caighdeán Oifigiúil** (the Official Standard) — Ireland. **Default and only UI target.** |

### Three native dialects (Na Canúintí)

Native Irish survives in **Gaeltacht** regions and has three traditional dialects:

| Dialect | Region | Notes |
|---------|--------|-------|
| **Cúige Mumhan** (Munster) | Kerry, Cork, Waterford | Strong stress on long syllables; preserves old `do` perfective particle. |
| **Cúige Chonnacht** (Connacht) | Galway (Conamara), Mayo | **Most-spoken dialect.** Distinctive pronunciation of broad/slender. |
| **Cúige Uladh** (Ulster) | Donegal | Closest to Scottish Gaelic; distinctive intonation; some unique lexis. |

**For UI translation, use An Caighdeán Oifigiúil (the Official Standard)** — the codified written norm used by the State, education, RTÉ, and TG4. Do NOT translate a UI string into a single dialect form; that excludes other Gaeltacht speakers and learners. Standard Irish is the supra-dialectal written norm.

### Demographic reality

- **~1–2%** of the population are daily native speakers (Gaeltacht communities, ~70,000 people).
- **~40%** of the Republic's population (Census 2022) claim some Irish — most being L2 learners through the school system.
- Irish is mandatory in Republic of Ireland primary and secondary schools, on State signage, in government documents, and in EU translation.
- **UI in Irish carries cultural and constitutional weight** even though most users will also have English available. Translate it WELL — sloppy Irish is more visibly wrong than sloppy German because the audience is small, motivated, and includes language activists.

> **Tír gan teanga, tír gan anam** — "A country without a language is a country without a soul." This proverb is the cultural premise of Irish localization.

---

## Identity Guardrail — Irish is Celtic Goidelic, NOT the same as Welsh

Irish is a **Celtic language**, but Celtic has two branches and Irish is in the **Goidelic** branch — together with **Scottish Gaelic (Gàidhlig)** and **Manx (Gaelg)**.

| Branch | Languages | Notes |
|--------|-----------|-------|
| **Goidelic (Q-Celtic)** | **Irish (Gaeilge)**, Scottish Gaelic, Manx | Sister languages, mutually partially intelligible in writing. |
| **Brittonic (P-Celtic)** | Welsh (Cymraeg), Breton (Brezhoneg), Cornish (Kernewek) | Separate branch — different mutations, orthography, vocabulary. |

**Practical implications:**
- Irish ≠ Welsh. They share the *concept* of initial consonant mutation, but **the specific mutation patterns differ** (Welsh has soft, nasal, aspirate; Irish has séimhiú and urú).
- Irish ≠ Scottish Gaelic. They share lenition, but **orthography differs**: Irish uses `séimhiú = h` (bh, ch, dh); Scottish Gaelic also uses `h` but spells some words differently (Irish `bóthar` = Scottish `rathad`). Do NOT cross-port translations.
- Irish ≠ Modern English even though both are spoken in Ireland. Irish has VSO word order, mutations, and a copula. It is a typologically distant language.

**If your source mentions "Gaelic" in a US/Canadian context**, it almost always means Scottish Gaelic, not Irish. In Ireland, "Gaelic" usually refers to Gaelic Football, not the language. The language is **Irish / Gaeilge**.

---

## Register: sibh vs tú (T–V distinction)

Irish has a T–V distinction:

| Pronoun | Use | Verb form (imperative 2nd person) | Possessive |
|---------|-----|-----------------------------------|------------|
| **tú** | Singular informal; default in casual contexts; Gaeltacht everyday speech | 2sg: `roghnaigh` (choose) | **do** (your-sg) — triggers **séimhiú** |
| **sibh** | (1) Plural "you all"; (2) Singular formal in some contexts | 2pl: `roghnaígí` (choose) | **bhur** (your-pl/formal) — triggers **urú** |

### Register choice for UI

Irish culture tends informal. Unlike German `Sie` or French `vous`, Irish does **not** have a strong T–V politeness asymmetry in modern usage. Two reasonable defaults:

| Context | Recommended register | Why |
|---------|----------------------|-----|
| Consumer apps, social, marketing, casual UI | **tú** (singular, informal) | Matches conversational Irish; warmer; closer to native Gaeltacht usage. |
| Government, banking, formal business UI | **sibh** (plural-as-formal) | Matches Irish State formal register; respectful distance. |
| Mass UI addressing "users" generically | **tú** (default) OR **sibh** | Pick ONE and stay consistent throughout the product. |

**Hard rule: never mix tú and sibh in the same surface** (or even the same product). Mixing them creates grammar errors because possessives differ:

| ✗ Mixed (wrong) | ✓ Consistent (tú) | ✓ Consistent (sibh) |
|-----------------|---------------------|----------------------|
| Roghnaigh do chomhad agus cliceáil oraibh | Roghnaigh do chomhad agus cliceáil ort | Roghnaígí bhur gcomhad agus cliceáil oraibh |

In the rest of this skill, **examples default to tú** unless explicitly noted, but the rules apply mirror-image to sibh.

> **Note on `sibh` triggering urú:** `bhur socruithe` → standard says `s` is not actually eclipsed in Irish (only b, c, d, f, g, p, t take a prefixed consonant). So `bhur socruithe` stays `bhur socruithe` (no visible mutation on s — eclipsis applies only to mutable consonants). But `bhur gcomhad` is correct (c → gc).

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. Initial consonant mutations — séimhiú (lenition) and urú (eclipsis) (severity 2.5)

This is THE defining feature of Irish grammar. Two parallel mutation systems trigger on the **first consonant** of a word based on what precedes it.

#### Séimhiú (lenition) — marked by inserted `h`

A small letter `h` is inserted **after** the initial consonant:

| Original | Lenited | Example |
|----------|---------|---------|
| **B** | **Bh** | `bean` (woman) → `an bhean` (the woman) |
| **C** | **Ch** | `cat` → `mo chat` (my cat) |
| **D** | **Dh** | `dán` (poem) → `do dhán` (your poem) |
| **F** | **Fh** (silent!) | `fear` (man) → `mo fhear` (my man) — Fh is silent in speech |
| **G** | **Gh** | `garda` → `do gharda` |
| **M** | **Mh** | `máthair` → `mo mháthair` |
| **P** | **Ph** | `post` (job) → `mo phost` |
| **S** | **Sh** | `siopa` (shop) → `an tsiopa`'s sister case — see below; in séimhiú: `sa siopa` → `sa shiopa` |
| **T** | **Th** | `teach` (house) → `mo theach` |

> **NOT lenited:** L, N, R, vowels — these never take séimhiú in standard modern Irish.

**Common triggers for séimhiú:**
- Possessives: **mo** (my), **do** (your-sg), **a** (his)
- Definite article + feminine singular noun: `an bhean`, `an chathair` (the city)
- Numbers 2–6: `dhá chomhad`, `trí chomhad`, `sé chomhad`
- After certain prepositions: **de**, **do** (to), **ó** (from), **roimh** (before), **mar** (as/like), **faoi** (under), **trí** (through), **um**, **ar** (on)
- Past tense particle: `do shábháil sé` (he saved) — `do` triggers séimhiú on past verbs
- Negative past `níor`: `níor shábháil sé`
- Vocative particle `a`: `a Sheáin!` (Seán!)
- After comparative `níos`: `níos fearr` (better) (s mutates contextually)

#### Urú (eclipsis) — marked by prepended consonant

A **new consonant is prepended** before the original, eclipsing its sound:

| Original | Eclipsed | Pronounced as |
|----------|----------|---------------|
| **B** | **mB** | /m/ — original b is silent |
| **C** | **gC** | /g/ |
| **D** | **nD** | /n/ |
| **F** | **bhF** | /v/ or /w/ |
| **G** | **nG** | /ŋ/ |
| **P** | **bP** | /b/ |
| **T** | **dT** | /d/ |
| Vowels | **n-** prefix | `n-` is added before the vowel: `a n-athair` (their father), `ár n-athair` (our father) |

> **NOT eclipsed:** L, M, N, R, S — only the 7 mutable consonants take urú.

**Common triggers for urú:**
- Possessives: **ár** (our), **bhur** (your-pl/formal), **a** (their)
- Preposition `i` (in): `i nGaillimh` (in Galway), `i mBaile Átha Cliath` (in Dublin)
- Preposition + article combinations: `ag an`, `leis an`, `ar an`, `as an`, `roimh an`, `ón`, `don` — many trigger urú on the following noun (depending on dialect/standard)
- Numbers 7–10: `seacht gcomhad`, `ocht gcomhad`, `naoi gcomhad`, `deich gcomhad`
- After interrogative/dependent particle `an` (used for questions): `An bhfuil tú?` (are you?) — `bhfuil` is `tá` eclipsed
- After the dependent verb particles `go`, `nach`, `mura`, `dá`, `cá`

#### Concrete examples (mutation by trigger)

| Trigger | Base form | After mutation | English |
|---------|-----------|----------------|---------|
| `mo` (my) + lenition | comhad | **mo chomhad** | my file |
| `do` (your-sg) + lenition | post | **do phost** | your job |
| `a` (his) + lenition | máthair | **a mháthair** | his mother |
| `a` (her) + NOTHING on consonant; h-prefix on vowels | máthair / athair | `a máthair` / **a hathair** | her mother / her father |
| `ár` (our) + eclipsis | comhad | **ár gcomhad** | our file |
| `bhur` (your-pl) + eclipsis | post | **bhur bpost** | your (pl) job |
| `a` (their) + eclipsis | tír | **a dtír** | their country |
| `an` + feminine sg + lenition | bean | **an bhean** | the woman |
| `an` + feminine sg starting with s (NOT sc, sm, sp, st) + `ts` | sráid | **an tsráid** | the street (special: s → ts after `an` for fem.) |
| `i` (in) + eclipsis | Gaillimh | **i nGaillimh** | in Galway |
| 3 + lenition | cat | **trí chat** | three cats |
| 8 + eclipsis | comhad | **ocht gcomhad** | eight files |

> **Critical UI rule:** If you write `mo comhad`, `do post`, `ár comhad`, `i Gaillimh`, `trí comhad`, or `ocht comhad` — they are **all wrong**. Mutations are obligatory, not stylistic.

#### Mutation cheat-sheet (memorize this)

```
Lenition (séimhiú) — add h to consonant:
  b→bh  c→ch  d→dh  f→fh  g→gh  m→mh  p→ph  s→sh  t→th
  Triggers: mo, do, a(his), an+fem.sg, prepositions (de/do/ó/faoi/ar/roimh/mar/trí/um), numbers 2–6,
            past-tense particle do/níor, vocative a, comparative níos

Eclipsis (urú) — prepend consonant:
  b→mb  c→gc  d→nd  f→bhf  g→ng  p→bp  t→dt   (vowels take n- prefix)
  Triggers: ár, bhur, a(their), i (in), preposition+an in many cases, numbers 7–10,
            interrogative an, dependent particles go/nach/mura/dá/cá

NOT mutated by either: l, n, r (and vowels are only h-prefixed/n-prefixed selectively)
```

### 2. Broad vs slender consonants (caol le caol, leathan le leathan) (severity 2.0)

Irish orthography enforces a rule about which vowels surround a consonant. Every consonant in Irish is either **broad** (velarized) or **slender** (palatalized) — this affects pronunciation. The orthography signals this through the **surrounding vowels**, and they MUST match in front/back quality.

| Vowel quality | Vowels |
|---------------|--------|
| **Slender (caol)** | e, é, i, í |
| **Broad (leathan)** | a, á, o, ó, u, ú |

The rule **"caol le caol, leathan le leathan"** (slender with slender, broad with broad) means: vowels on **both sides** of a consonant must be from the same quality group.

| ✗ Wrong | ✓ Correct | Why |
|---------|-----------|-----|
| `comhadanna` (looking inside) | `comhaid` (plural of comhad) | broad-broad inside, but the actual plural is formed by slenderizing |
| `cailín` ✓ | (correct) | c-aí-l-í-n: broad a-aí surrounds c (broad-broad), then slender í surrounds l-n (slender-slender). ✓ |
| `fearr` ✓ | (correct) | broad a around rr |
| `*cailear` ✗ | The vowels around `l` would be slender `i` and broad `e` — illegal. |

**Why this matters for UI translation:**
- When inflecting nouns (e.g., genitive, plural), Irish spelling changes to keep this rule satisfied:
  - `fear` (man, nom) → `fir` (man, gen — broadenend r becomes slender; spelling adjusts)
  - `bord` (table) → `boird` (gen sg — slender d, so an `i` is inserted)
  - `cat` (cat) → `cait` (plural — `a` becomes `ai` to keep `t` slender)
- When auto-generating UI text with placeholders, do NOT cross broad/slender boundaries.
- If you see an Irish word with adjacent vowels of different quality around a consonant, it's almost certainly misspelled.

**You don't have to compute this from scratch** — use established dictionary forms (teanglann.ie, focloir.ie, tearma.ie) rather than inventing inflections.

### 3. Long vowels with fada (´) are meaning-critical (severity 2.5)

Irish has 5 long vowels marked with the **fada** (acute accent): **á é í ó ú**. The fada is **NEVER optional decoration** — it changes meaning.

| With fada | Without fada | Difference |
|-----------|--------------|------------|
| `bán` (white) | `ban` (woman, gen. pl.) | Different words. |
| `cás` (case) | `cas` (twist, turn) | Different words. |
| `sí` (she) | `si` (no such word in standard) | Required. |
| `Seán` (proper name) | `Sean` (old) | Different. |
| `Éire` (Ireland) | `Eire` is just a stripped form, considered wrong | Required. |
| `saol` (world / life) | `saol` (correct — vowel cluster, not fada-bearing) | Note: also `saoil` = genitive |
| `fáilte` (welcome) | `failte` ✗ | Required. |

**Hard rule: NEVER strip fadas to ASCII.** `Eire`, `Failte`, `Caoga` (50, should be `caoga`) are signs of a broken pipeline. Restore them.

Five common Irish words you will encounter constantly:
- **Gaeilge** (Irish language) — note `ei` not `ée`
- **Éire** (Ireland) — capital É + fada
- **fáilte** (welcome)
- **sábháil** (save) — TWO fadas
- **íoslódáil** (download) — THREE fadas (i, o, a)

### 4. VSO word order — Verb–Subject–Object (severity 2.0)

Irish is a **VSO language** — the verb comes **FIRST** in declarative main clauses, then subject, then object/complement.

| ✗ Wrong (SVO calque from English) | ✓ Correct (VSO) | English |
|------------------------------------|-------------------|---------|
| An t-úsáideoir shábháil an comhad | **Shábháil an t-úsáideoir an comhad** | The user saved the file. |
| An cat ar an mbord | **Tá an cat ar an mbord** | The cat is on the table. (verb `tá` first) |
| Sibh is féidir socruithe a athrú | **Is féidir libh socruithe a athrú** | You can change settings. (copula `is` first) |
| Mé do shábháil é | **Shábháil mé é** | I saved it. |

**Question form:** prepend the interrogative particle **an** (which triggers urú on the verb):

| Statement | Question |
|-----------|----------|
| Tá tú anseo. (You are here.) | **An bhfuil tú anseo?** (Are you here?) — `tá` → `bhfuil` (eclipsed dependent form) |
| Sábhálann tú é. | **An sábhálann tú é?** |

**Past tense statement:** verb takes the past-tense `do`/`d'` particle (often elided) + séimhiú:

| Statement | Past |
|-----------|------|
| Sábhálann sé é (he saves it) | **Shábháil sé é** (he saved it) — `s` lenited to `sh` |

### 5. Copula `is` vs substantive verb `tá` — DO NOT CONFUSE (severity 2.5)

Irish has **two "to be" verbs** with completely different functions. This is one of the hardest features for English speakers and a frequent source of bad UI.

| Verb | Function | Example |
|------|----------|---------|
| **is** (copula) | **Identity / classification / permanent quality.** Used to link a noun to a noun, or to define what something IS. | **Is dochtúir é.** (He is a doctor.) `Is + [predicate noun] + [subject pronoun]` |
| **tá** (substantive verb) | **State / location / temporary condition / existence.** Used for where something is, how it is, what state it is in. | **Tá sé sa siopa.** (He is in the shop.) `Tá + [subject] + [state/location]` |

#### Worked contrasts

| English | ✗ Wrong | ✓ Correct | Why |
|---------|---------|-----------|-----|
| He is a doctor. | Tá sé dochtúir. | **Is dochtúir é.** | Classification → copula. |
| He is in the shop. | Is é sa siopa. | **Tá sé sa siopa.** | Location → tá. |
| The file is open. | Is oscailte an comhad. | **Tá an comhad oscailte.** | State → tá. |
| This is a directory. | Tá sé eolaireacht. | **Is eolaire é seo.** | Classification → copula. |
| It is possible. | Tá sé féidir. | **Is féidir.** / **Is féidir é.** | "Possible" is a classificatory predicate. |
| You can save (it is possible for you to save). | Tá tú in ann sábháil. (OK conversational) | **Is féidir leat sábháil.** | Standard idiom uses copula. |

> **Mnemonic:** "X is a Y" / "X is (description)" → **copula is**. "X is at/in/here/now/feeling/state" → **tá**.

### 6. No verb "to have" — use `tá X ag Y` construction (severity 2.0)

Irish has **no direct equivalent of "to have."** Instead, possession is expressed with `tá` + the thing + `ag` (at) + the possessor.

Literal: **"Is [thing] at [person]"** = "[Person] has [thing]"

| English | ✓ Irish | Literal |
|---------|---------|---------|
| I have a book. | **Tá leabhar agam.** | Is book at-me. |
| You have a file. | **Tá comhad agat.** | Is file at-you. |
| She has the password. | **Tá an pasfhocal aici.** | Is the password at-her. |
| We have three messages. | **Tá trí theachtaireacht againn.** | Is three messages at-us. |
| Do you have an account? | **An bhfuil cuntas agat?** | Q: is account at-you? |

**Note** the prepositional pronouns `agam, agat, aici, againn, agaibh, acu` — these are **fused forms** of `ag + pronoun` (see Rule 7).

> **Anti-pattern:** Do NOT invent `*tá mé leabhar` or `*tá mé ag leabhar` ("I have book") — these are not Irish. Use `Tá leabhar agam`.

### 7. Inflected prepositional pronouns (forainmneacha réamhfhoclacha) (severity 2.0)

In Irish, prepositions **fuse with pronouns** into single inflected forms. You must use the fused form. **Never write `ag mé`, `ar tú`, `le sibh`** — these are ungrammatical.

#### Most common prepositional pronoun paradigms

| Preposition (English) | mé (I) | tú (you-sg) | sé (he/it-m) | sí (she/it-f) | sinn (we) | sibh (you-pl) | siad (they) |
|------------------------|--------|-------------|---------------|---------------|-----------|---------------|--------------|
| **ag** (at) → "have" | **agam** | **agat** | **aige** | **aici** | **againn** | **agaibh** | **acu** |
| **ar** (on) | **orm** | **ort** | **air** | **uirthi** | **orainn** | **oraibh** | **orthu** |
| **as** (out of, from) | **asam** | **asat** | **as** | **aisti** | **asainn** | **asaibh** | **astu** |
| **chuig** (towards) | **chugam** | **chugat** | **chuige** | **chuici** | **chugainn** | **chugaibh** | **chucu** |
| **de** (off, of) | **díom** | **díot** | **de** | **di** | **dínn** | **díbh** | **díobh** |
| **do** (to, for) | **dom** | **duit** | **dó** | **di** | **dúinn** | **daoibh** | **dóibh** |
| **faoi** (under, about) | **fúm** | **fút** | **faoi** | **fúithi** | **fúinn** | **fúibh** | **fúthu** |
| **i** (in) | **ionam** | **ionat** | **ann** | **inti** | **ionainn** | **ionaibh** | **iontu** |
| **le** (with) | **liom** | **leat** | **leis** | **léi** | **linn** | **libh** | **leo** |
| **ó** (from) | **uaim** | **uait** | **uaidh** | **uaithi** | **uainn** | **uaibh** | **uathu** |
| **roimh** (before) | **romham** | **romhat** | **roimhe** | **roimpi** | **romhainn** | **romhaibh** | **rompu** |
| **trí** (through) | **tríom** | **tríot** | **tríd** | **tríthi** | **trínn** | **tríbh** | **tríothu** |

#### UI examples

| ✗ Wrong (separate) | ✓ Correct (fused) | English |
|---------------------|--------------------|---------|
| Tá leabhar ag mé. | **Tá leabhar agam.** | I have a book. |
| Cliceáil ar é. | **Cliceáil air.** | Click on it. |
| Le sibh: | **Libh:** / **Daoibh:** | For you (pl): |
| Theip ar an íoslódáil ar mé. | **Theip orm ar an íoslódáil.** / **Theip ar an íoslódáil orm.** | The download failed for me. |

### 8. Numbers + singular noun + mutation by range (severity 2.0)

Irish numbers behave **completely unlike English**. Three rules:

1. **The noun stays SINGULAR after numbers 1–10** (and often higher). Never `5 chomhaid` ; correct is `5 chomhad`.
2. **Numbers 1–6 trigger lenition (séimhiú).**
3. **Numbers 7–10 trigger eclipsis (urú).**
4. **Numbers 11+ generally take no mutation** and noun stays singular.
5. **0 takes the plural** noun form.

#### Cardinal numbers + comhad (file)

| Number | Word | Result | Why |
|--------|------|--------|-----|
| 0 | náid / a náid | **0 comhaid** (plural) | Plural form. |
| 1 | aon | **aon chomhad amháin** | Lenition + `amháin` ("one only"). |
| 2 | dhá | **dhá chomhad** | Lenition. (Note: `dhá` itself is `dá` lenited.) |
| 3 | trí | **trí chomhad** | Lenition. |
| 4 | ceithre | **ceithre chomhad** | Lenition. |
| 5 | cúig | **cúig chomhad** | Lenition. |
| 6 | sé | **sé chomhad** | Lenition. |
| 7 | seacht | **seacht gcomhad** | Eclipsis (c → gc). |
| 8 | ocht | **ocht gcomhad** | Eclipsis. |
| 9 | naoi | **naoi gcomhad** | Eclipsis. |
| 10 | deich | **deich gcomhad** | Eclipsis. |
| 11 | aon … déag | **aon chomhad déag** | Lenition (from 1), `déag` after. |
| 20 | fiche | **fiche comhad** | No mutation; singular. |
| 100 | céad | **céad comhad** | No mutation; singular. |

**ICU plural form mapping (Irish has 5 categories):**

| ICU category | Range | Form | Example |
|--------------|-------|------|---------|
| **one** | n = 1 | lenition, singular | `1 chomhad` (or `aon chomhad amháin`) |
| **two** | n = 2 | lenition, singular | `2 chomhad` |
| **few** | n = 3..6 | lenition, singular | `3 chomhad`, `6 chomhad` |
| **many** | n = 7..10 | eclipsis, singular | `7 gcomhad`, `10 gcomhad` |
| **other** | else (0, 11+) | no mutation, singular usually | `0 comhaid`, `11 comhad`, `20 comhad` |

> **For UI ICU plural keys, you usually need all 5 forms: `one / two / few / many / other`** because Irish distinguishes 2 (dual remnant), 3–6, and 7–10 with different mutations.

#### People counting (system of numbering people)

There is a **separate set of numbers** used for counting people (1–12), based on the old "personal" numerals: `duine, beirt, triúr, ceathrar, cúigear, seisear, seachtar, ochtar, naonúr, deichniúr, aon duine déag, dáréag`. These trigger **lenition** on the noun after them (`beirt fhear` = two men). For UI, you'll rarely need this — but DON'T use cardinal numbers for people contexts in marketing copy where it sounds natural to say `beirt úsáideoirí` (two users) idiomatically — though in software UI, generic cardinal `2 úsáideoir` is also accepted.

### 9. No indefinite article; definite article = `an` (sg) / `na` (pl) (severity 2.0)

Irish has **no indefinite article**. The bare noun does double duty:

| English | Irish | Notes |
|---------|-------|-------|
| a cat | **cat** | No "a" word in Irish. |
| the cat | **an cat** | Definite article `an`. |
| cats | **cait** | Bare plural. |
| the cats | **na cait** | Plural article `na`. |

#### Effects of `an` (singular definite article)

| Context | Mutation | Example |
|---------|----------|---------|
| Masculine noun, nom/acc | none | **an fear** (the man) |
| Feminine noun, nom/acc | **lenition** | **an bhean** (the woman) (`b → bh`) |
| Feminine noun starting with `s` + vowel (or s + l/n/r) | **`s → ts`** | **an tsráid** (the street); **an tsiopa**? No — `siopa` is masc. — better example: **an tseachtain** (the week, fem.) (Note: s + sc/sm/sp/st keeps `s`.) |
| Masculine noun starting with vowel | **`t-` prefix** | **an t-úsáideoir** (the user); **an t-ainm** (the name); **an t-uaslódáil** (the upload) |
| Feminine noun starting with vowel | **no mutation** | **an aiste** (the essay); **an oifig** (the office) |
| Singular genitive masculine (after the genitive `an`) | **lenition** | **leabhar an fhir** (the man's book) (`fear → fhir`) |
| Singular genitive feminine (after `na`) | varies | **carr na mná** (the woman's car) |

#### Effects of `na` (plural definite article)

| Context | Mutation | Example |
|---------|----------|---------|
| Nominative/accusative plural | none on noun | **na cait** (the cats); **na comhaid** (the files) |
| Genitive plural (all genders) | **eclipsis** | **leabhair na bhfear** (the men's books); **luach na gcomhad** (the value of the files) |
| Plural starting with vowel | **`h-` prefix** | **na hoifigí** (the offices); **na hainmneacha** (the names) |

> **Common UI errors:**
> - `úsáideoir` → "the user" must be **`an t-úsáideoir`** (masc. vowel → t-prefix), NOT `an úsáideoir`.
> - `bean` → "the woman" must be **`an bhean`** (fem. → lenition), NOT `an bean`.
> - `na úsáideoirí` → "the users" must be **`na húsáideoirí`** (plural vowel → h-prefix).

### 10. Genitive case (an tuiseal ginideach) — possession + verbal noun (severity 2.0)

Irish has 4 cases (nominative, vocative, genitive, dative — dative is mostly merged with nominative in modern Irish except in fixed phrases), but **the genitive is alive and load-bearing**.

The genitive is triggered by:
1. **Possession**: `leabhar an fhir` (the man's book) — `fear → fhir`.
2. **After a verbal noun (ainm briathartha)**: `ag sábháil an chomhaid` (saving the file) — `comhad → chomhaid`.
3. **After compound prepositions**: `i ndiaidh an chomhaid` (after the file), `os comhair an úsáideora` (in front of the user).
4. **After certain simple prepositions** in some dialects: `chun an chomhaid` (towards the file).

#### Genitive formation patterns (some examples)

| Nom. sg. | Gen. sg. | Pattern |
|----------|----------|---------|
| comhad (file) | **chomhaid** | broadening with séimhiú after article |
| fear (man) | **fhir** | slenderization + séimhiú |
| bean (woman) | **mná** | irregular |
| úsáideoir (user) | **úsáideora** | -oir → -ora |
| Éire (Ireland) | **na hÉireann** | irregular + h-prefix after `na` |
| teach (house) | **tí** | irregular |
| baile (town) | **bhaile** | séimhiú only |
| sábháil (saving, vbn) | **na sábhála** | -áil → -ála |

#### UI examples

| ✗ Wrong (nominative used after vbn) | ✓ Correct (genitive) | English |
|--------------------------------------|------------------------|---------|
| ag sábháil an comhad | **ag sábháil an chomhaid** | saving the file |
| ag íoslódáil an comhad | **ag íoslódáil an chomhaid** | downloading the file |
| ag scriosadh an úsáideoir | **ag scriosadh an úsáideora** | deleting the user |
| suíomh an úsáideoir | **suíomh an úsáideora** | the user's location |

> Genitive is one of the **most common UI errors** in machine-translated Irish — auto-translators often skip it. Always check verbal noun + noun pairs.

### 11. Two genders + adjective agreement (severity 2.0)

Irish has **two grammatical genders**: **firinscneach (masculine)** and **baininscneach (feminine)**. Neuter does not exist.

#### Rough heuristic (not absolute)

| Tendency | Ending suggests | Examples |
|----------|------------------|----------|
| Masculine | -ach, -aire, -aí, -ín, -úr, -óir | fear, úsáideoir, comhad, carr, leabhar, ríomhaire |
| Feminine | -acht, -íocht, -eog, -óg, -lann, -is, -áil (vbn) | bean, oifig, fuinneog, scoil, obair, Gaeilge, sábháil |

> **There are exceptions everywhere.** Use a dictionary. Native speakers also gender-correct each other on rare nouns.

#### Effects of gender

1. **Definite article `an` + feminine = lenition** (rule above).
2. **Adjective after feminine singular noun = lenition.**
3. **Adjective genitive form differs.**

| Gender | Pattern | Example |
|--------|---------|---------|
| Masculine | adj. unchanged after noun | **carr mór** (big car); **fear mór** (big man) |
| Feminine sg | adj. takes séimhiú | **bean mhór** (big woman); **oifig bheag** (small office) |
| Plural (any gender) | adj. agrees in number; pl. attributive adj has its own form | **fir mhóra** (big men); **carranna móra** (big cars) |

| ✗ Wrong | ✓ Correct | Why |
|---------|-----------|-----|
| bean beag | **bean bheag** | fem. → lenite adj. |
| an cat mhór | **an cat mór** | `cat` is masc. → no lenition. |
| oifig mór | **oifig mhór** | fem. → lenite. |
| carr mhór | **carr mór** | `carr` is masc. → no lenition. |

### 12. No yes/no — answer with the verb (severity 1.5)

Irish has **no words for "yes" and "no."** You answer a yes/no question by **repeating the verb** (in positive or negative form).

| Question | "Yes" answer | "No" answer |
|----------|---------------|--------------|
| **An bhfuil tú anseo?** (Are you here?) | **Tá.** (Am.) | **Níl.** (Am not.) |
| **An sábhálann tú é?** (Do you save it?) | **Sábhálann.** (Save.) | **Ní shábhálann.** (Don't save.) |
| **An bhfaca tú é?** (Did you see it?) | **Chonaic.** (Saw.) | **Ní fhaca.** (Didn't see.) |
| **An mian leat dul ar aghaidh?** (Do you wish to continue?) | **Is mian.** | **Ní mian.** |
| **An raibh tú ann?** (Were you there?) | **Bhí.** | **Ní raibh.** |

#### UI implications

- **Confirmation dialogs**: do NOT use `Sea / Ní hea` or `Tá / Níl` as universal yes/no buttons unless the dialog actually asks `An…?` with the matching verb.
- **Safe modern UI convention**: use action labels:
  - `Lean ar aghaidh` (Continue) / `Cealaigh` (Cancel)
  - `Sábháil` (Save) / `Caith amach` (Discard)
  - `Deimhnigh` (Confirm) / `Cealaigh` (Cancel)
- Where a literal "Yes / No" is forced (e.g., a generic dialog whose verb is unknown): **`Tá / Níl`** is the conventional fallback in modern Irish UI, but it is not universally correct grammar. Prefer action verbs.

> **Béarlachas alert:** `Sea` exists as a particle for emphasis/affirmation in some contexts (e.g., answering identity questions: `An tú Seán? — Is mé.` or in Munster `Sea`), but it is NOT the universal "yes" of English. Don't lean on it as a generic translation.

---

## UI Conventions

### Buttons — verbal noun (ainm briathartha) form

Irish UI buttons use the **verbal noun (ainm briathartha)** form, which is also the form used after `ag` for progressive aspect. This is the standard convention in Irish software localization, consistent with terminology from **tearma.ie** and established Microsoft/Apple/Google Irish localizations.

| English | ✓ Irish | Avoid |
|---------|---------|-------|
| Save | **Sábháil** | `Sábháiltear` (autonomous), `Sábháiligí` (sibh imperative — only if formal-sibh) |
| Cancel | **Cealaigh** | — |
| Delete | **Scrios** | `Scrios é` (redundant pronoun) |
| Send | **Seol** | — |
| Edit | **Cuir in eagar** / **Eagraigh** | — |
| Search | **Cuardaigh** | — |
| Confirm | **Deimhnigh** | — |
| Continue | **Lean ar aghaidh** | — |
| Submit | **Seol isteach** | — |
| Sign in / Log in | **Logáil isteach** | `Logála isteach` (wrong form) |
| Sign out / Log out | **Logáil amach** | — |
| Sign up | **Cláraigh** | — |
| Next | **Ar aghaidh** / **Ar Aghaidh** | — |
| Back | **Ar ais** | — |
| Done | **Críochnaithe** / **Réidh** | — |
| OK | **OK** / **Ceart go leor** | — |
| Close | **Dún** | — |
| Open | **Oscail** | `Oscail é` |
| Upload | **Uaslódáil** | `Uploadáil` (Béarlachas) |
| Download | **Íoslódáil** | `Downloadáil` (Béarlachas) |
| Refresh | **Athnuaigh** | — |
| Settings | **Socruithe** | — |
| Apply | **Cuir i bhfeidhm** | — |
| Reset | **Athshocraigh** | — |
| Select all | **Roghnaigh gach rud** | — |
| Add more | **Cuir tuilleadh leis** | `Cuir níos mó leis` (less natural) |
| Copy | **Cóipeáil** | — |
| Paste | **Greamaigh** | — |
| Choose / Pick file | **Roghnaigh comhad** | `Brabhsáil le haghaidh comhad` (browser-language for picker) |

### Status messages — `Ag` + verbal noun (ongoing) / autonomous past (completed)

Irish progressive aspect is **`ag + ainm briathartha`** (literally "at saving"). This is the natural Irish way to express ongoing actions.

| English | ✓ Irish | Notes |
|---------|---------|-------|
| Loading… | **Ag lódáil…** / **Ag luchtú…** | Either accepted; `ag luchtú` is more native. |
| Saving… | **Ag sábháil…** | |
| Sending… | **Ag seoladh…** | |
| Processing… | **Á phróiseáil…** (it being processed) | Or `Ag próiseáil…` |
| Connecting… | **Ag nascadh…** | |
| Searching… | **Ag cuardach…** | |
| Translating… | **Ag aistriú…** | |
| Uploading… | **Ag uaslódáil…** | |
| Downloading… | **Ag íoslódáil…** | |
| Please wait | **Fan nóiméad** / **Fanaigí nóiméad** (sibh) | "Wait a moment" |

### Completion messages — autonomous past or past participle

For **completed states**, Irish uses either the autonomous past form (`Sábháladh`) or the past participle / verbal adjective (`Sábháilte`):

| English | ✓ Irish |
|---------|---------|
| Saved | **Sábháilte** (adjective form) / **Sábháladh é** (autonomous past, "it was saved") |
| Done | **Críochnaithe** / **Déanta** |
| Translation complete | **Aistriúchán críochnaithe** / **Tá an t-aistriúchán réidh** |
| File uploaded | **Comhad uaslódáilte** |
| Sent | **Seolta** |
| Payment successful | **Íocaíocht éirithe** / **D'éirigh leis an íocaíocht** |

### Failure / error messages — `Theip ar` + noun

The idiomatic Irish for "X failed" is **`Theip ar X`** (literally "failed on X") — using the prepositional pronoun pattern.

| English | ✓ Irish |
|---------|---------|
| Upload failed. | **Theip ar an uaslódáil.** |
| Connection failed. | **Theip ar an nasc.** |
| Login failed. | **Theip ar an logáil isteach.** |
| Something went wrong. | **Chuaigh rud éigin amú.** / **Tharla earráid.** |
| File not found. | **Níor aimsíodh an comhad.** (autonomous past negative — Níor + lenition) |
| No results found. | **Níor aimsíodh aon torthaí.** |
| Try again. | **Bain triail eile as.** / **Triail arís.** |

### Empty states — `Níl aon` / `Gan`

| ✗ Wrong / weak | ✓ Native |
|----------------|----------|
| Níl torthaí | **Níl aon torthaí** ("There are no results") |
| Níl rud roghnaithe | **Níl aon rud roghnaithe** / **Gan aon rud roghnaithe** |
| Folamh | **Folamh** (OK) or **Gan ábhar** ("without content") |
| Tá tú gan teachtaireachtaí | **Níl aon teachtaireachtaí agat** ("you have no messages") |

### Drag-and-drop

- **drag** → `tarraing` (native verb)
- **drop / release** → `scaoil` (let go) / `lig` (let)
- **NOT** `dragáil` (Béarlachas), `saor` (= free/liberate, wrong sense)

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| Dragáil comhaid anseo | **Tarraing comhaid anseo** |
| Saor chun uaslódála | **Scaoil chun uaslódála** |

### File picker — `Roghnaigh`, not `Brabhsáil`

For file pickers, use the **action-oriented verb** `roghnaigh` (choose / select), NOT the navigation verb `brabhsáil` (browse). The user's goal is to choose, not to wander.

| ✗ Browse-language | ✓ Action-language |
|---------------------|---------------------|
| Brabhsáil le haghaidh comhad | **Roghnaigh comhad** |
| Cliceáil chun brabhsála | **Cliceáil chun roghnaithe** |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Irish | Notes |
|------|-------|-------|
| Question mark | `?` | Same as English. |
| Comma | `,` | Different conjunction rules — see below. |
| Period | `.` | Same as English. |
| Colon | `:` | Same. |
| Quotation marks | **`"…"`** | Standard. Some style guides use **`„…"`** (Germanic) but `"…"` is dominant in modern Irish UI. |
| Apostrophe | Used in elided forms: **d'éirigh, n'fheadar, b'fhéidir** | Mandatory in elisions. |
| En-dash | `–` | For ranges. |

### Comma rules

| Rule | Example |
|------|---------|
| **NO comma** before **`agus`** (and) / **`is`** (and, contraction) / **`nó`** (or) | Cliceáil **agus** oscail é. / Comhad **nó** fillteán. |
| **Comma** before **`go`** (that, subordinating) | Tá súil agam, **go** n-éireoidh leat. |
| **Comma** before **`má`** (if) / **`dá`** (if-hypothetical) | Sábháil é, **má** tá tú réidh. |
| **Comma** before **`nuair`** (when) | Cliceáil, **nuair** atá tú réidh. |
| **Comma** before **`mar`** (because, as) | Theip ar an uaslódáil, **mar** níl ceangal idirlín ann. |
| **Comma** before **`a`** (relative — non-restrictive) | An comhad, **a** sábháladh inné, … |

### Numbers — Anglo style (UNLIKE most of Europe)

Ireland follows **UK/Irish conventions**, which match English: **period (.) for decimals, comma (,) for thousands.** This is **different from continental Europe**.

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **comma (,)** | 1,234,567 |
| Decimal separator | **period (.)** | 3.14 / 99.99 |
| Negative | `-25` | |
| Percent | `25%` (no space, English-style) | |

| ✗ Wrong (European) | ✓ Correct (Irish/UK) |
|---------------------|------------------------|
| 3,14 | **3.14** |
| 1.000 | **1,000** |
| 1 234,56 | **1,234.56** |

### Dates — DD/MM/YYYY

| Format | Example | Use |
|--------|---------|-----|
| DD/MM/YYYY | **15/01/2024** | Default numeric. |
| D Month YYYY | **15 Eanáir 2024** | Long-form prose. |
| D Month, YYYY | **15 Eanáir, 2024** | Also acceptable with comma. |
| YYYY-MM-DD | 2024-01-15 | Technical / ISO only. |

**Irish month names (CAPITALIZED — months are capitalized in Irish, unlike English convention in some style guides):**

| # | Irish | English |
|---|-------|---------|
| 1 | **Eanáir** | January |
| 2 | **Feabhra** | February |
| 3 | **Márta** | March |
| 4 | **Aibreán** | April |
| 5 | **Bealtaine** | May |
| 6 | **Meitheamh** | June |
| 7 | **Iúil** | July |
| 8 | **Lúnasa** | August |
| 9 | **Meán Fómhair** | September ("middle of harvest") |
| 10 | **Deireadh Fómhair** | October ("end of harvest") |
| 11 | **Samhain** | November |
| 12 | **Nollaig** | December (also = Christmas) |

**Irish weekdays (with `Dé-` prefix for "day of"):**

| English | Irish |
|---------|-------|
| Monday | **Dé Luain** |
| Tuesday | **Dé Máirt** |
| Wednesday | **Dé Céadaoin** |
| Thursday | **Déardaoin** (irregular — historically `Dé Ardaoin`) |
| Friday | **Dé hAoine** (h-prefix because Aoine starts with vowel) |
| Saturday | **Dé Sathairn** |
| Sunday | **Dé Domhnaigh** |

Week starts **Monday** (ISO 8601, Irish convention).

### Time

- **24-hour** preferred: `14:30`.
- 12-hour acceptable with **`a.m.` / `i.n.`** (iarnóin = afternoon) or **`r.n.`** (roimh nóin = before-noon = morning):
  - `9.30 r.n.` = 9:30 AM
  - `2.30 i.n.` = 2:30 PM
- Use **period (.) between hours and minutes** in 12-hour format (Irish convention), but `:` is also accepted in modern UI.

### Currency — Euro (EUR / €) — Ireland is in the eurozone

Ireland adopted the **euro on 1 January 2002**, replacing the Irish pound (punt). Use EUR.

| Format | Pattern | Example |
|--------|---------|---------|
| Symbol before amount | `€` | **€1,234.56** |
| ISO code | EUR | **EUR 1,234.56** / **1,234.56 EUR** |

**Number format with euro: Anglo style** — period decimal, comma thousands.

- ✓ `€1,234.56`
- ✓ `€99.99`
- ✗ `€1.234,56` (continental style — wrong for Ireland)
- ✗ `€1 234,56` (French style — wrong for Ireland)

For "cent" subdivisions: `cent` is borrowed; `ceint` exists but `cent` is dominant. `€0.50` reads as "caoga cent" colloquially.

---

## Terminology — Preferred Irish Terms (Caighdeánach)

Use established Irish terminology from **An Caighdeán Oifigiúil** and the **tearma.ie** national terminology database. Reference also **teanglann.ie** (dictionary), **focloir.ie** (English–Irish dictionary), **abair.ie** (text-to-speech for pronunciation).

| English | ✓ Irish | Avoid (Béarlachas) |
|---------|---------|---------------------|
| user | **úsáideoir** | — |
| account | **cuntas** | akkúint |
| password | **pasfhocal** ("pass-word", calque) / **focal faire** ("watch-word", more native) | password |
| settings | **socruithe** | settings |
| dashboard | **deais** / **painéal** | dashboard |
| email | **ríomhphost** ("computer-mail") | email, mejl |
| link | **nasc** | link |
| website | **suíomh gréasáin** / **láithreán gréasáin** | website |
| folder | **fillteán** | folder |
| file | **comhad** | file |
| device | **gléas** | divice |
| phone | **fón** / **guthán** | telephone |
| computer | **ríomhaire** | kompúter |
| application / app | **feidhmchlár** / **app / aip** | applikéisean |
| update (v.) | **nuashonraigh** / **uasdátaigh** | updatáil |
| save | **sábháil** | seibheáil, saveáil |
| delete | **scrios** | delete-áil |
| upload | **uaslódáil** | uploadáil |
| download | **íoslódáil** | downloadáil |
| sign in / log in | **logáil isteach** / **sínigh isteach** | login |
| sign up | **cláraigh** | — |
| search | **cuardaigh** | search-áil |
| click | **cliceáil** / **clic** | klikáil |
| share | **comhroinn** / **roinn** | share-áil |
| profile | **próifíl** | — |
| notifications | **fógraí** | — |
| privacy | **príobháideacht** | privacy |
| terms | **téarmaí** / **coinníollacha** | — |
| support | **tacaíocht** | — |
| help | **cabhair** | — |
| feedback | **aiseolas** | feedback |
| menu | **roghchlár** ("choice-list") | menu |
| home | **baile** / **leathanach baile** | home |
| browser | **brabhsálaí** | browser |
| screen | **scáileán** | screen |
| keyboard | **méarchlár** ("finger-board") | keyboard |
| mouse | **luch** | mouse |
| software | **bogearraí** | software |
| hardware | **crua-earraí** | hardware |
| video | **físeán** / **fís-** | video |
| photo | **grianghraf** / **pictiúr** | foto |
| window | **fuinneog** | — |
| menu bar | **barra roghchláir** | — |
| search bar | **barra cuardaigh** | — |
| icon | **deilbhín** ("little-image") | icon |
| error | **earráid** | error |
| warning | **rabhadh** | warning |
| language | **teanga** | — |
| font | **cló** | font |
| size | **méid** | size |
| color | **dath** | colour |
| copy (v.) | **cóipeáil** | — |
| paste (v.) | **greamaigh** ("stick") | pasteáil |
| cut (v.) | **gearr** | — |
| open (v.) | **oscail** | — |
| close (v.) | **dún** | — |
| print (v.) | **priontáil** / **clóigh** | — |
| send (v.) | **seol** | — |
| select (v.) | **roghnaigh** | — |
| build (software) | **tóg** / **cruthaigh** | buildáil |
| deploy | **imscar** / **cuir i bhfeidhm** | deployáil |
| pipeline (CI/CD) | pipeline (keep) | — |
| commit (git) | commit (keep) | — |
| merge (git) | **cumaisc** / merge (keep in code contexts) | mergeáil |
| repository | **stór** / **stóras** / repository | — |
| sync | **sioncronaigh** / **comhshioncronaigh** | — |
| API | API (keep — Latin always) | — |
| cache | **taisce** | — |
| log (n.) | **logchomhad** / **loga** | — |
| URL | **URL** (keep) / **seoladh idirlín** | — |
| WiFi | **WiFi** / **gan sreang** ("without wire") | — |
| internet | **idirlíon** | — |

### Place names — Ireland uses Irish forms in Irish text

| English | Irish |
|---------|-------|
| Ireland | **Éire** |
| Republic of Ireland | **Poblacht na hÉireann** |
| Dublin | **Baile Átha Cliath** (BÁC) |
| Cork | **Corcaigh** |
| Galway | **Gaillimh** |
| Limerick | **Luimneach** |
| Belfast | **Béal Feirste** |
| Northern Ireland | **Tuaisceart Éireann** |
| United Kingdom | **An Ríocht Aontaithe** |
| United States | **Stáit Aontaithe Mheiriceá** (full) / **SAM** (abbreviated — preferred in UI) |
| European Union | **An tAontas Eorpach** (AE) |
| Europe | **An Eoraip** |

### Tech identifiers — keep in Latin

Inside Irish text, these stay as-is, even if they would mutate phonetically:
- **Brand names: Google, Microsoft, Apple, GitHub, iPhone, Android, Facebook, Twitter/X**
- **Protocols: HTTP, HTTPS, REST, GraphQL, OAuth, JWT, SSH, FTP**
- **Formats: JSON, XML, YAML, CSV, PDF, PNG, JPEG**
- **Tools: Git, Docker, npm, pip, yarn**
- **Commands, paths, URLs, code, placeholders**

> **Hard rule:** Do NOT lenite or eclipse brand names. `Google` stays `Google` even after `mo` (which would normally lenite). Write **`mo chuntas Google`** (my Google account), NOT `mo Ghoogle`.

---

## Calque / Anti-Pattern Blocklist — Béarlachas

**Béarlachas** (literally "English-ness") is the named, well-known anti-pattern in Irish: producing Irish text that is grammatical word-by-word but is actually just English with Irish words. It is the **#1 quality failure** in machine-translated Irish.

### Idiom calques

| ✗ Béarlachas (English-shaped) | ✓ Native Irish | Reason |
|--------------------------------|------------------|--------|
| Tá mé sorry. | **Tá brón orm.** ("Sorrow is on me.") | "I'm sorry" — never use English `sorry`. |
| Conas tá tú? | **Conas atá tú?** | Indirect relative — must include `atá`. |
| Bris cos! | **Go n-éirí leat!** / **Ádh mór ort!** | "Break a leg" — use Irish good-luck idiom. |
| Píosa cáca | **Furasta go leor** / **Is beag an rud é** | "Piece of cake" — calque. |
| Déanann sé ciall | **Tá ciall leis** / **Is réasúnta é** | "Makes sense" — calque. |
| Ag deireadh an lae | **Ar deireadh thiar thall** / **Sa deireadh** | "At the end of the day" — calque. |
| Ar an leathanach céanna | **Ar aon intinn** / **Ar aon fhocal** | "On the same page" — calque. |
| Tóg é go dtí an chéad leibhéal eile | **Téigh níos faide** / **Téigh chun cinn** | "Take to next level" — calque. |
| Tá mé ag súil chun tosaigh le | **Tá mé ag tnúth le** | "Look forward" — use `ag tnúth le`. |

### Vocabulary anglicisms

| ✗ Béarlachas | ✓ Native Irish |
|---------------|-----------------|
| jab (for job) | **post** / **obair** |
| brocáilte (for broken) | **briste** / **lochtach** |
| víosa (for visa — political, OK as is)  | **víosa** (loan, fine in tech) |
| seibheáil | **sábháil** |
| delete-áil | **scrios** |
| download-áil | **íoslódáil** |
| upload-áil | **uaslódáil** |
| update-áil | **nuashonraigh** |
| sín-áil (signáil) | **sínigh** |
| klikáil | **cliceáil** |
| dragáil | **tarraing** |
| search-áil | **cuardaigh** |
| share-áil | **comhroinn** / **roinn** |
| build-áil | **tóg** |
| email-áil | **seol ríomhphost** |

### Structural calques

| ✗ Calque structure | ✓ Native Irish | Reason |
|---------------------|------------------|--------|
| I n-ord le sábháil (in order to save) | **Chun sábháil** / **Le haghaidh sábhála** | `i n-ord le` is overly verbose / direct calque. |
| Ní féidir an comhad a bheith aimsithe | **Níor aimsíodh an comhad** / **Comhad gan aimsiú** | Passive calque → use autonomous past. |
| Tá sé á rá go… | (acceptable Irish) | — |
| Bunaithe ar | **De réir** / **Ar bhonn** | "Based on" as sentence opener — prefer concise prepositional. |
| Bain triail as é | **Bain triail as** | Pronoun `é` redundant — Irish already encodes object in `as`. |
| Cuir níos mó leis | **Cuir tuilleadh leis** | "Add more" — `tuilleadh` is the natural Irish word. |
| Taispeáin níos mó | **Taispeáin tuilleadh** | "Show more" — `tuilleadh` more natural. |

### Compound-adjective calques

English forms like "AI-powered", "X-driven", "X-aware" do NOT have direct Irish equivalents using hyphens. Restructure:

| ✗ Hyphen calque | ✓ Native Irish |
|------------------|------------------|
| AI-tiomáinte | **le cumhacht AI** / **ag úsáid AI** / **le cabhair AI** |
| Cumhachtaithe-AI | **le cumhacht AI** |
| X-tiomáinte | **bunaithe ar X** / **ag úsáid X** |
| Data-driven | **bunaithe ar shonraí** |
| User-friendly | **éasca le húsáid** / **so-úsáidte** |

### False friends (focail bhréige)

| Irish word | What it actually means | English looks like | Correct for the English |
|------------|--------------------------|---------------------|--------------------------|
| `actually` does NOT exist; `aktually` is wrong | — | "actually" | **i ndáiríre** / **go fíor** |
| `eventually` does NOT translate directly | — | "eventually" | **ar deireadh** / **sa deireadh** |
| `originally` does NOT translate directly | — | "originally" | **ó thús** / **i dtosach** |
| Béarla | the English language | "Béarla" looks borrowed | (means "English") |
| Sasanach | English person | — | (means "English person") |
| Cárta | card | (loan, fine) | — |

---

## Self-Check Checklist (Run Before Returning Output)

### Mutations (auto-fail on miss)

- [ ] **Séimhiú (lenition) applied** after `mo`, `do`, `a`(his), `an`+fem.sg, numbers 2–6, past particle, vocative `a`, prepositions de/do/ó/faoi/ar/roimh/mar/trí/um.
- [ ] **Urú (eclipsis) applied** after `ár`, `bhur`, `a`(their), `i` (in), numbers 7–10, interrogative `an`, dependent particles go/nach/mura/dá.
- [ ] **L, N, R, vowels NOT lenited** (no `lh`, `nh`, `rh`).
- [ ] **L, M, N, R, S NOT eclipsed.**
- [ ] **Vowel after eclipsis trigger gets `n-` prefix** (e.g., `ár n-úsáideoirí`, `i n-Albain`).
- [ ] **Fem. sg. starting with vowel takes NO mutation after `an`** (an oifig, NOT an hoifig).
- [ ] **Masc. sg. starting with vowel takes `t-` prefix after `an`** (an t-úsáideoir).
- [ ] **Fem. sg. starting with `s` + vowel/l/n/r takes `ts` after `an`** (an tseachtain, an tsráid).
- [ ] **Plural starting with vowel takes `h-` prefix after `na`** (na hoifigí).
- [ ] **Numbers 2–6 lenite the following SINGULAR noun** (trí chomhad).
- [ ] **Numbers 7–10 eclipse the following SINGULAR noun** (seacht gcomhad).

### Special characters (auto-fail)

- [ ] **Fadas (´) preserved** on long vowels: á é í ó ú. Never `Eire`, `failte`, `cead`. Always `Éire`, `fáilte`, `céad`.
- [ ] **Common UI words spelled correctly**: `Gaeilge`, `Éire`, `fáilte`, `sábháil`, `íoslódáil`, `uaslódáil`, `úsáideoir`, `comhad`, `socruithe`.

### Orthography

- [ ] **Caol le caol, leathan le leathan** preserved — surrounding vowels match in quality (slender e/i with consonant; broad a/o/u with consonant).

### Grammar (high-severity)

- [ ] **VSO word order** — verb first in declarative main clauses (Shábháil an t-úsáideoir an comhad, NOT An t-úsáideoir shábháil…).
- [ ] **Copula `is` vs substantive `tá`** correctly chosen — `Is dochtúir é` (classification) vs `Tá sé sa siopa` (location/state).
- [ ] **No verb "to have"** — use `tá X ag Y` (Tá leabhar agam, NOT Tá mé leabhar).
- [ ] **Prepositional pronouns used** — `agam/agat/aige/aici/againn/agaibh/acu`, etc. NEVER `ag mé`, `ar tú`, `le sibh`.
- [ ] **Singular noun after numbers 1–10** (5 chomhad, NOT 5 chomhaid).
- [ ] **Genitive case after verbal nouns** (ag sábháil an chomhaid, NOT ag sábháil an comhad).
- [ ] **Genitive case after compound prepositions** (os comhair an úsáideora, i ndiaidh an chomhaid).
- [ ] **Feminine sg. adj. lenited** (bean bheag, oifig mhór).
- [ ] **Masc. sg. adj. unchanged** (carr mór, fear mór).
- [ ] **Plural article `na` triggers eclipsis in genitive** (luach na gcomhad).

### UI conventions

- [ ] **Buttons use verbal noun (ainm briathartha)** form: Sábháil, Scrios, Cealaigh, Cóipeáil.
- [ ] **Status messages use `Ag + verbal noun`** for ongoing: `Ag sábháil…`, `Ag íoslódáil…`.
- [ ] **Completion uses past participle / autonomous past**: `Sábháilte`, `Sábháladh é`, `Seolta`.
- [ ] **Failures use `Theip ar`**: `Theip ar an uaslódáil`, `Theip ar an nasc`.
- [ ] **Empty states use `Níl aon`** or **`Gan`**: `Níl aon torthaí`, `Gan aon rud roghnaithe`.
- [ ] **Drag-drop uses `Tarraing` + `Scaoil`** — NOT `Dragáil` / `Saor`.
- [ ] **File picker uses `Roghnaigh`** — NOT `Brabhsáil`.
- [ ] **No yes/no buttons** unless dialog asks `An…?` with a matching verb. Prefer action labels (Sábháil/Cealaigh, Lean ar aghaidh/Cealaigh).

### Béarlachas (anti-calque)

- [ ] **No anglicism-verb hybrids**: NO `seibheáil`, `deleteáil`, `updateáil`, `downloadáil`, `uploadáil`, `klikáil`, `searcháil`, `shareáil`, `dragáil`, `signáil`.
- [ ] **No anglicism nouns** when native exists: NO `email`, `password`, `dashboard`, `software`, `browser`, `screen`, `mouse`, `keyboard`. Use ríomhphost, pasfhocal, deais, bogearraí, brabhsálaí, scáileán, luch, méarchlár.
- [ ] **No structural calques**: NO `i n-ord le` for "in order to"; use `chun`. NO `tá mé sorry`; use `tá brón orm`.
- [ ] **Idiomatic phrases use Irish forms**: `Conas atá tú?` (NOT `Conas tá tú?`); `Tá brón orm` (NOT `tá mé sorry`); `Ar aon intinn` (NOT `ar an leathanach céanna`).
- [ ] **Brand names not mutated**: `Google`, `Apple`, `Microsoft` stay as-is even after `mo`/`do`/`ár`.

### Formatting

- [ ] **Numbers: period for decimal, comma for thousands** (Anglo style — 1,234.56).
- [ ] **Dates: DD/MM/YYYY** (15/01/2024) or `15 Eanáir 2024`.
- [ ] **Months capitalized**: Eanáir, Feabhra, Márta…
- [ ] **Currency: EUR €** (Ireland is in eurozone since 2002) — `€1,234.56`.
- [ ] **No comma before `agus / nó / is`**.
- [ ] **Comma before `go / má / dá / nuair / mar / a (relative)`**.

### Register

- [ ] **tú or sibh consistent throughout** — never mixed within the same product.
- [ ] **Possessive matches register**: `do` + lenition (tú-form); `bhur` + eclipsis (sibh-form).
- [ ] **Verb endings match register**: `roghnaigh` (2sg imperative for tú); `roghnaígí` (2pl imperative for sibh).

---

## Worked Examples

### Example 1 — Standard UI (informal `tú`, native vocabulary)

**Source (English):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** Consumer product UI → casual `tú`, native Irish vocabulary, no Béarlachas.

**Translation:**

> Fáilte ar ais! Tá 3 chomhad nua agat i do chuntas. Cliceáil ar **Lean ar aghaidh** chun iad a athbhreithniú, nó ar **Cealaigh** chun fanacht anseo. Ag sábháil do chuid athruithe…

**Why this works:**
- `Fáilte ar ais!` — native greeting.
- `Tá 3 chomhad nua agat` — uses `tá + ag` for "have"; `3 chomhad` (number 3 + lenition + singular noun); `agat` (prepositional pronoun for "at you-sg" = "you have"); `nua` (adjective unchanged, since `comhad` is masc.).
- `i do chuntas` — `i` (in) + `do` (your-sg, lenites) + `cuntas` → `chuntas`. The preposition `i` would normally eclipse, but combined with possessive `do` we get lenition from `do`.
- Buttons: `Lean ar aghaidh`, `Cealaigh` (verbal noun / imperative form).
- `chun iad a athbhreithniú` — `chun` + obj. pronoun `iad` + particle `a` + verbal noun (purpose construction).
- `Ag sábháil do chuid athruithe…` — `ag` + verbal noun `sábháil` (progressive); `do chuid athruithe` (your changes — `do chuid` is the partitive possessive construction used for abstract/plural nouns).
- All fadas preserved.

### Example 2 — Anglicism rejection

**Source:** Click here to download the software update.

**✗ Béarlachas-heavy:**

> Clikeáil anseo chun an software update a downloadáil.

**✓ Native Irish:**

> Cliceáil anseo chun nuashonrú na mbogearraí a íoslódáil.

Notes:
- `Clikeáil` → `Cliceáil` (native verb form).
- `software update` → `nuashonrú na mbogearraí` (compound noun — "update of the software"). `na mbogearraí` is the genitive plural with `na` + eclipsis on `b` (`bogearraí` → `mbogearraí`).
- `downloadáil` → `íoslódáil` (native verb).
- Word order: VO with `a + verbal noun` infinitive construction (`chun X a íoslódáil` = "to download X").

### Example 3 — Mutations after possessives

**Source:** My file is in our folder, but their folder is empty.

**Translation:**

> Tá mo chomhad inár bhfillteán, ach tá a bhfillteán siúd folamh.

Notes:
- `mo chomhad` — `mo` (my) + lenition: `comhad` → `chomhad`.
- `inár bhfillteán` — `i` (in) + `ár` (our) contracts to `inár`; `ár` triggers eclipsis: `fillteán` → `bhfillteán`.
- `a bhfillteán siúd` — `a` (their) + eclipsis on `fillteán` → `bhfillteán`; `siúd` is emphatic ("their, that one over there").
- `folamh` (empty) — adjective; `fillteán` is masc., so no lenition on adj.
- VSO: `Tá` first in both clauses.

### Example 4 — VSO and copula vs `tá`

**Source:** The user is an administrator. The administrator is in the system.

**Translation:**

> Is riarthóir é an t-úsáideoir. Tá an riarthóir sa chóras.

Notes:
- Sentence 1: **classification** ("user is an administrator") → **copula `is`**. Structure: `Is [pred. noun] [subj. pron.] [subj.]` = `Is riarthóir é an t-úsáideoir`.
- Sentence 2: **location** ("administrator is in the system") → **substantive `tá`**. VSO.
- `an t-úsáideoir` — masc. noun starting with vowel → `t-` prefix after `an`.
- `sa chóras` — `sa` (in the) is contraction of `i + an` and triggers lenition: `córas` → `chóras`.

### Example 5 — Numbers + mutations

**Source:** You have 1 file, 3 files, 8 files, 12 files.

**Translation:**

> Tá 1 chomhad amháin agat. Tá 3 chomhad agat. Tá 8 gcomhad agat. Tá 12 chomhad agat.

Notes:
- `1` → lenition + `amháin`: `aon chomhad amháin` (or `1 chomhad amháin`).
- `3` → lenition (numbers 2–6): `3 chomhad`.
- `8` → eclipsis (numbers 7–10): `8 gcomhad`.
- `12` → no mutation in standard (numbers 11+ generally take no mutation, but some style guides still apply lenition with `déag` constructions). For UI ICU `other` form, `12 comhad` is also acceptable. Above we used `12 chomhad` reflecting the older convention; both are defensible.

### Example 6 — Genitive after verbal noun

**Source:** Saving the file… The file has been saved.

**Translation:**

> Ag sábháil an chomhaid… Sábháladh an comhad. / Tá an comhad sábháilte.

Notes:
- Ongoing: `Ag sábháil an chomhaid` — `ag` + verbal noun `sábháil` + **genitive** `an chomhaid` (`comhad` → `chomhaid` with lenition + slenderization). Wrong would be `ag sábháil an comhad`.
- Completion: `Sábháladh an comhad` (autonomous past — "it-was-saved the file") OR `Tá an comhad sábháilte` (state — "the file is saved").

### Example 7 — Failure message

**Source:** Upload failed. Please try again.

**Translation:**

> Theip ar an uaslódáil. Bain triail eile as, le do thoil.

Notes:
- `Theip ar` (failed on) + `an uaslódáil` — the idiomatic Irish for failure. `Theip` is the past tense of `teip` (fail).
- `Bain triail eile as` — "take another try out of [it]" — idiomatic for "try again". `as` is the preposition; no redundant `é`.
- `le do thoil` — "with your-sg will" = "please" (informal). For sibh: `le bhur dtoil`.

### Example 8 — Currency and dates

**Source:** Your subscription costs €9.99 per month. Next payment: 15/01/2024.

**Translation:**

> Cosnaíonn do shíntiús €9.99 in aghaidh na míosa. Chéad íocaíocht eile: 15/01/2024 (15 Eanáir 2024).

Notes:
- EUR with period decimal: `€9.99` (Anglo style — Ireland uses period decimals).
- `do shíntiús` — `do` (your-sg) + lenition on `síntiús` → `shíntiús`.
- `in aghaidh na míosa` — "per month" (literally "in face of the month"); `na míosa` is genitive sg. of `mí` (month).
- Date format: `15/01/2024` numeric or `15 Eanáir 2024` long-form. Month capitalized.

---

## When in Doubt

1. **Default to Irish (ga-IE), An Caighdeán Oifigiúil, informal `tú` form (unless explicitly formal sibh requested), native Irish vocabulary (no Béarlachas), DD/MM/YYYY dates, EUR with period decimals.**
2. If you wrote an anglicism-verb hybrid (`seibheáil`, `deleteáil`, `updateáil`, `downloadáil`, `klikáil`) → **fix to native Irish verb** (`sábháil`, `scrios`, `nuashonraigh`, `íoslódáil`, `cliceáil`).
3. If you stripped a fada (`Eire`, `failte`, `cead`) → **restore** (`Éire`, `fáilte`, `céad`).
4. If you used SVO word order (`An t-úsáideoir shábháil…`) → **fix to VSO** (`Shábháil an t-úsáideoir…`).
5. If you wrote `ag mé`, `ar tú`, `le sibh` → **use the prepositional pronoun** (`agam`, `ort`, `libh`).
6. If you confused `is` and `tá` (used `Tá sé dochtúir` for classification) → **switch to copula** (`Is dochtúir é`).
7. If you forgot the genitive after a verbal noun (`ag sábháil an comhad`) → **apply genitive** (`ag sábháil an chomhaid`).
8. If you applied mutation to a brand name (`mo Ghoogle`) → **leave brand names unchanged** (`mo chuntas Google`).
9. If you used English plural noun after a number (`5 chomhaid`) → **use singular with mutation by range** (`5 chomhad`, `8 gcomhad`).
10. If you mixed `tú` and `sibh` (or `do` and `bhur`) → **pick one and apply throughout**.
11. If a feminine singular noun is missing lenition after `an` (`an bean`) → **apply** (`an bhean`).
12. If you forgot the `t-` prefix on a masculine vowel-initial noun after `an` (`an úsáideoir`) → **apply** (`an t-úsáideoir`).
13. If you used `Sea / Ní hea` or `Tá / Níl` as universal yes/no without checking the question verb → **use action labels** (`Sábháil / Cealaigh`, `Lean ar aghaidh / Cealaigh`).
14. If currency uses European number format (`€1.234,56`) → **fix to Anglo style** (`€1,234.56`).
15. If the source has a "powered by X" or "X-driven" hyphenated calque → **restructure** to `le cumhacht X`, `bunaithe ar X`, `ag úsáid X`.
16. If you didn't apply eclipsis after `i` (in) on a place name (`i Gaillimh`) → **apply** (`i nGaillimh`).
17. If you broke broad/slender vowel harmony in an inflected form → **use the dictionary** (teanglann.ie, tearma.ie) rather than inventing the form.
18. If your translation reads like word-by-word English with Irish vocabulary → **stop and rewrite from the meaning**. This is Béarlachas, the named anti-pattern. Read the Irish out loud — would a Gaeltacht speaker say this?

> **Final reminder — Tír gan teanga, tír gan anam.** Irish UI is read by a small, motivated, language-conscious audience that includes the Government, RTÉ/TG4, language activists, Gaeltacht communities, and tens of thousands of L2 learners. The grammatical bar is high. The political bar (no Béarlachas, no English calques, no anglicism-verb-hybrids) is even higher. Translate it WELL.
