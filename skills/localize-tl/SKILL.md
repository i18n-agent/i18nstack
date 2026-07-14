---
name: localize-tl
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Tagalog / Filipino (Wikang Filipino) for the Philippines. CRITICAL — Tagalog/Filipino is Austronesian (Malayo-Polynesian), NOT Spanish despite ~30% Spanish loanwords (silya, kotse, kwento, libro, pera) and NOT Chinese despite Chinese loanwords. Loanwords don't change the grammar — the Austronesian core (verb-initial word order, focus/trigger system, agglutinative affixes) remains. THE defining critical feature is the FOCUS / TRIGGER SYSTEM — verbs select a \"focus\" via affix that determines which argument the ang-phrase refers to (Bumili ang lalaki ng tinapay = The MAN bought bread, agent focus; Binili ng lalaki ang tinapay = The man bought the BREAD, object focus). Affixes encode focus + aspect: -um- and mag- (actor focus), -in and i- (object focus), -an (locative/beneficiary focus). Aspect (NOT tense) is encoded by reduplication of first CV: kumain (ate, completed) / kumakain (is eating, imperfective) / kakain (will eat, contemplated). Other key features: verb-initial (V1) word order (\"Kumakain ako\" = Am-eating I), three case markers (ang topic/focus, ng non-topic, sa oblique), mga plural marker placed BEFORE the noun (mga tao = people) but OMITTED with numbers (limang tao NOT limang mga tao), na/-ng ligature linking modifier to noun (malaking bahay big-LIG house, magandang kotse beautiful-LIG car — ligature attaches to FIRST word of modifier phrase), reduplication for plural/intensity/ongoing aspect (tao→tao-tao, maganda→maganda-ganda), NO grammatical gender (siya = he/she/they singular), NO articles a/the (definiteness via ang/ng/sa case markers), Filipino 28-letter alphabet (adds Ñ for Spanish heritage and NG as one letter for the velar nasal), po/opo politeness particles INSERTED to mark respect (Salamat → Salamat po, Oo → Opo), inclusive vs exclusive \"we\" distinction (kami excludes listener / tayo includes listener — critical for UI tone), i- prefix is the productive way to verbalize English roots (i-save, i-click, i-upload, i-delete — respected practice not bad calque), Spanish-derived month and day names (Enero/Pebrero/Marso, Lunes/Martes/Miyerkules), PHP Philippine Peso ₱ with Anglo number format (₱1,234.56 — comma thousands, period decimal, American colonial influence), MM/DD/YYYY or DD/MM/YYYY dates both acceptable, Taglish (Tagalog-English code-switching) normal in colloquial speech but formal UI uses pure Filipino, religious sensitivity for predominantly Roman Catholic (~80%) Philippines with Muslim minority in Mindanao, and cultural concepts of pakikisama (smooth relations) and hiya (face) shaping polite UI tone."
---

# Localize: Tagalog / Filipino (tl → Tagalog / Wikang Filipino)

You are translating source text into Tagalog / Filipino for the Philippines. This skill captures grammar, register, UI conventions, formatting, and Tagalog-specific failure modes — including the famously complex **focus / trigger system** that distinguishes Tagalog from every Indo-European language.

## Scope & Variants

**One UI standard, two names for it:**

- **tl-PH** — Tagalog as the regional Luzon language (the historical basis for the national language).
- **fil-PH** — Filipino, since the **1987 Constitution**, is the **national language** of the Philippines. It is based on Tagalog but officially incorporates vocabulary from other Philippine languages (Cebuano, Hiligaynon, Ilocano, Bikol, Waray, etc.) and from Spanish/English.

**For UI work, use the Filipino register** since Filipino is the official national variant and the form taught in schools, used in government, and used in mass media. In practice, ~95% of Filipino UI text is identical to Tagalog UI text — the differences are mostly in formal/literary registers and in some vocabulary expansion.

**ISO codes:** `tl` (Tagalog) and `fil` (Filipino) are both used. CLDR uses `fil` for the national language; `tl` is the older code. Many software systems still use `tl` as the locale code. Treat them as effectively interchangeable for UI purposes.

**Native names:**
- **Tagalog** — Tagalog (the language as spoken historically in Luzon)
- **Filipino / Wikang Filipino** — the national language

**Co-official language:** English (since the 1935 Constitution). Most Filipinos are bilingual; **Taglish** (Tagalog-English code-switching) is normal in everyday speech, advertising, and casual media. Formal UI should default to pure Filipino, but tech terms borrowed from English are widely accepted.

## Identity Guardrail — Austronesian, NOT Spanish, NOT Chinese (CRITICAL)

Tagalog/Filipino is an **Austronesian (Malayo-Polynesian) language**. Its closest distant relatives are Indonesian, Malay, Javanese, Hawaiian, Maori, Malagasy. Like all Austronesian languages it has:

- Verb-initial / predicate-initial word order (V1)
- Focus / trigger system with case markers
- Agglutinative affixes (prefix, infix, suffix, circumfix, reduplication)
- No grammatical gender
- No articles in the European sense

**Despite ~30% Spanish loanwords** (silya from silla "chair", kotse from coche "car", kwento from cuento "story", libro "book", pera "money", mesa "table", bintana "window", kusina "kitchen", banyo "bathroom"), **Tagalog is NOT a Romance language and shares no grammatical structure with Spanish.** Loanwords adapted Tagalog phonotactics — they don't bring Spanish grammar with them.

**Despite Chinese loanwords** (mostly from Hokkien — bihon "rice noodles", siopao, ate "older sister", kuya "older brother", lola "grandmother", lolo "grandfather", pansit), **Tagalog is NOT a Chinese language** and shares no grammatical structure with Mandarin or Hokkien.

**Despite English co-official status and heavy Taglish in daily life**, the Tagalog grammar — focus system, V1 word order, ang/ng/sa case markers, mga plural, na/-ng ligature — is fully intact and what makes Filipino "Filipino".

**Common identity errors to avoid:**
- ❌ Translating as if it were Spanish ("La mga file" — using Spanish article la with Tagalog mga is nonsensical)
- ❌ Translating as if it were English with substituted words (SVO Anglo word order, no ligature, no case markers)
- ❌ Treating it as a "simple" or "broken" language because it lacks gender/articles — the focus system is grammatically richer than most European languages
- ❌ Confusing with **Cebuano (Bisaya)** — a different Philippine Austronesian language with ~20M speakers, NOT mutually intelligible with Tagalog. Cebuano uses "ang" similarly but vocabulary differs widely (Cebuano: unsa, asa, kanus-a / Tagalog: ano, saan, kailan)
- ❌ Confusing with **Ilocano, Hiligaynon, Bikol, Waray** — other major Philippine languages, all distinct

## Register

Tagalog/Filipino formality is signaled primarily by:

1. **Pronoun choice** (kayo plural/formal vs ikaw/ka singular informal)
2. **Politeness particles** (po/opo — inserted to mark respect)
3. **Vocabulary register** (formal/literary vs colloquial)

| Level | Form | Use case |
|---|---|---|
| Formal w/ po | `kayo` + `po`/`opo` | Speaking to elders, customers, respect contexts; "Salamat po" |
| Formal w/o po | `kayo` | Business UI, professional software (DEFAULT FOR UI) |
| Informal | `ikaw` / `ka` | Casual, peer-to-peer, friend-to-friend |
| Inclusive "we" | `tayo` | Includes listener — warm, inclusive UI tone |
| Exclusive "we" | `kami` | Excludes listener — "we, the company" |

### po and opo — Politeness Particles

`po` and `opo` are **inserted** into utterances to mark respect/politeness. They have no direct English equivalent — closest analogy is the deferential softening of "sir/ma'am" but particles, not nouns.

| Plain | With po (polite) |
|---|---|
| Salamat (Thanks) | **Salamat po.** (Thank you, sir/ma'am) |
| Oo (Yes, informal) | **Opo.** (Yes, polite) |
| Hindi (No) | **Hindi po.** (No, polite) |
| Anong oras na? (What time is it?) | **Anong oras na po?** |
| Pwede ba? (May I?) | **Pwede po ba?** (May I, please?) |

**Default for product UI: NO po/opo.** Po/opo is reserved for spoken interpersonal contexts and direct customer-service tone. UI buttons, status messages, and labels should be **neutral imperative** — adding "po" to "I-save" sounds weirdly conversational for a button.

| Wrong (po in UI) | Correct (neutral UI) |
|---|---|
| I-save po | **I-save** |
| Mag-log in po | **Mag-log in** |
| Salamat po sa paggamit | (acceptable in marketing/welcome screens) **Salamat sa paggamit** is more neutral |

**Use po/opo sparingly** — only in: customer-service prompts ("Paano po kami makakatulong?" = How may we help you?), thank-you screens, formal error messages where extra deference is warranted.

### kayo vs ikaw

- **kayo** — plural "you" AND formal singular "you" (like Spanish "usted" or French "vous"). DEFAULT for UI.
- **ikaw** / **ka** — informal singular "you". Use for casual brand voice, youth apps.

`ka` is a clitic that attaches to the previous word; `ikaw` is the full form. Both informal.

| Form | Example |
|---|---|
| Formal | "Maligayang pagdating sa inyong bagong account." (Welcome to your new account — formal `inyong`) |
| Informal | "Maligayang pagdating sa iyong bagong account." (informal `iyong`) |

### tayo vs kami (Inclusive vs Exclusive "We")

This is critical for UI tone:

- **tayo** — inclusive "we" — includes the listener/reader. Use when the action involves both system+user.
- **kami** — exclusive "we" — excludes the listener. Use when speaking AS the company/system TO the user.

| Wrong | Correct | Reason |
|---|---|---|
| "Magse-save kami ng file mo" | **"Magse-save tayo ng file mo"** | The user IS doing the saving with us — use inclusive tayo |
| "Tayo ay magpapadala ng email" | **"Magpapadala kami ng email"** | The company sends the email TO the user — use exclusive kami |
| "Mag-start na tayo!" (Let's start) | ✅ correct — inclusive tayo for shared action |
| "Sasabihan namin kayo." (We will notify you) | ✅ correct — exclusive kami because the system notifies, the user receives |

### Formal vs Colloquial Vocabulary

Professional UI must use **standard Filipino**, not colloquial shortenings:

| Colloquial (AVOID in UI) | Formal (USE in UI) | Meaning |
|---|---|---|
| di / 'di | **hindi** | not / no |
| 'yung / yun | **iyon / ang** | the / that |
| 'to / 'yan | **ito / iyan** | this / that |
| lang | **lamang** | only / just (lang is widely used informally but formal text prefers lamang) |
| 'wag | **huwag** | don't |
| kasi | **dahil / sapagkat** | because |
| pano | **paano** | how |
| san | **saan** | where |
| kelan | **kailan** | when |
| sino | sino (same) | who |
| meron / 'meron | **mayroon** | there is / has |

Colloquial forms are acceptable in: casual/youth-oriented apps with explicit informal tone, social/chat features, marketing targeting Gen-Z.

## Critical Hard Rules

### 1. Verb-Initial Word Order (V1) — severity 2.0

Tagalog is **verb-initial / predicate-initial**. The predicate (verb or adjective) comes FIRST. This is the opposite of English SVO and the opposite of Spanish SVO. Trying to translate by preserving English word order is a hallmark of bad MT output.

| English (SVO) | Tagalog (V1) | Gloss |
|---|---|---|
| I am eating. | **Kumakain ako.** | Am-eating I |
| The user saved the file. | **Nag-save ng file ang user.** | Saved NG file ANG user |
| The system is loading. | **Naglo-load ang system.** | Is-loading ANG system |
| You are welcome. | **Walang anuman.** | Lit. "(There is) nothing" |
| The file is large. | **Malaki ang file.** | Big ANG file (predicate-adjective first) |
| The file is being saved. | **Sine-save ang file.** | Being-saved ANG file |

**Pronoun and ang-phrase order after the verb:**
- Verb + clitic pronouns + ang-phrase + ng-phrase + sa-phrase

```
Verb        Clitic    Topic(ANG)       Object(NG)       Location(SA)
Binili      mo        ang libro        —                sa tindahan.
You-bought  ang book                                     at the store.
```

**Common errors:**
- ❌ "Ako ay kumakain." (I am eating — using `ay` inversion) — grammatically valid but stilted/literary. Default V1 is "Kumakain ako."
- ❌ "Ang user nag-save ng file." — wrong order; verb must come first
- ✅ "Nag-save ang user ng file." or "Nag-save ng file ang user." — verb first

**Inverted form with `ay`:** Tagalog allows SVO-ish reordering via the linker `ay` ("Si Maria ay kumakain"), but this is **formal/literary** and not the default UI register. Use V1 unless you have a specific reason (e.g., emphatic, formal speech writing).

### 2. The Focus / Trigger System (Pokus) — severity 3.0

**This is THE defining feature of Tagalog grammar.** Every Tagalog verb is conjugated for **focus** (which argument is "topical" / marked by ang) AND for **aspect** (completed / incompleted / contemplated). There is no straight English equivalent — closest analogy is **active vs passive vs locative voice** but extended to more roles.

#### The Three Case Markers

| Marker | Role | Description |
|---|---|---|
| **ang** (or `si` for personal names) | Topic / focused argument | Definite, salient — what the sentence is "about" |
| **ng** (pronounced "nang") (or `ni` for personal names) | Non-topic agent / patient / possessor | The other argument |
| **sa** (or `kay` for personal names) | Oblique | Location, direction, recipient, beneficiary |

#### The Same Event, Different Focus

The same action "bought" can be expressed multiple ways depending on which argument is in focus:

| Sentence | Focus | Gloss |
|---|---|---|
| **Bumili** ang lalaki ng tinapay. | **Actor focus** | "The MAN bought bread." (focus on who did it) |
| **Binili** ng lalaki ang tinapay. | **Object focus** | "The man bought the BREAD." (focus on what was bought) |
| **Binilhan** ng lalaki ng tinapay ang tindahan. | **Locative focus** | "The man bought bread AT THE STORE." (focus on where) |
| **Ibinili** ng lalaki ng tinapay ang anak. | **Beneficiary focus** | "The man bought bread FOR THE CHILD." (focus on for whom) |

Notice: the verb **affix changes** to match the focus, AND the case markers (ang/ng) shift accordingly.

#### Focus Affixes Summary

| Focus | Affixes | Example (root: kain = eat) |
|---|---|---|
| **Actor** | -um-, mag-, mang- | **kumain** (ate — actor focus), **nagluto** (cooked — actor focus, more deliberate) |
| **Object** (patient) | -in, i- | **kainin** (to eat it), **kinain** (was eaten — object focus), **ibigay** (to give it) |
| **Locative** (location/goal) | -an | **kainan** (eating place / eat at), **buksan** (open it / open at) |
| **Beneficiary** | ipag-, i- | **ipagluto** (cook for someone) |
| **Instrumental** | ipang- | **ipanghiwa** (cut with) |
| **Potentive** (ability/accidental) | maka-, ma- | **nakakain** (was able to eat / accidentally ate) |

**For UI commands** the most common are:
- **i-** prefix (object focus, attaches to English/foreign roots) — i-save, i-delete, i-click, i-upload
- **-in** suffix (object focus, often native roots) — kainin (eat it), buksan (open it — note: -an for buksan because it's locative)
- **mag-** prefix (actor focus, intentional action) — mag-log in, mag-upload (as "to perform the act of uploading")
- **-um-** infix (actor focus) — kumain, sumulat

#### i- vs mag- vs -in for UI Buttons

This is the most practically important distinction:

| Pattern | When to use | Examples |
|---|---|---|
| **i-** + root | **Object focus** on an English/foreign root — when the button acts ON an object (file, item) | I-save, I-delete, I-upload, I-edit, I-cancel, I-publish, I-sync |
| **mag-** + root | **Actor focus** — when the user performs an action (less about acting on an object) | Mag-log in, Mag-sign up, Mag-search (Maghanap), Mag-print |
| **-in** suffix | **Object focus** on a native root | Buksan (open), Kanselahin (cancel — native), Burahin (delete — native), Tanggalin (remove), Hanapin (search — native) |
| **-an** suffix | **Locative focus** on a native root | Buksan (open — locative because "open AT something"), Lagyan (put on) |

**Both forms often coexist** in modern Filipino UI:
- I-save / Mag-save → both used
- I-delete / Burahin → both used (I-delete uses English root, Burahin uses native)
- I-cancel / Kanselahin → both used (Kanselahin uses Spanish-derived native form)

### 3. Aspect (NOT Tense) — severity 2.5

Tagalog verbs encode **aspect**, not tense. There are three aspects:

| Aspect | Meaning | Encoding |
|---|---|---|
| **Perfective** (completed) | Action completed | Affix only, no reduplication |
| **Imperfective** (incompleted) | Action in progress or habitual | Reduplication of first CV of root/affix |
| **Contemplated** (not yet started) | Future-like, planned | Reduplication WITHOUT the realis marker |
| **Infinitive** | Citation form | Plain affix |

**Example: kain (eat) — actor focus with -um-**

| Aspect | Form | English approximation |
|---|---|---|
| Infinitive | **kumain** | to eat |
| Perfective (completed) | **kumain** | ate |
| Imperfective (ongoing) | **kumakain** | is eating / eats (habitually) |
| Contemplated (future) | **kakain** | will eat |

Note: the infinitive and the perfective have the same form for -um- verbs. Context disambiguates.

**Example: save (foreign root) — object focus with i-**

| Aspect | Form | English approximation |
|---|---|---|
| Infinitive | **i-save** | to save |
| Perfective | **i-save / na-save / sini-save (completed: nai-save)** | saved |
| Imperfective | **sine-save / sini-save** | saving |
| Contemplated | **ise-save / ise-save** | will save |

**Reduplication is critical for "loading" states in UI:**
- ❌ "I-save..." (with ellipsis but no reduplication — looks like infinitive, not "saving")
- ✅ "**Sine-save**..." / "**Sini-save**..." (imperfective — actually means "saving")
- ✅ "**Naglo-load**..." (loading — actor focus imperfective of "load")
- ✅ "**Ina-upload**..." (being uploaded — imperfective object focus)
- ✅ "**Dina-download**..." (being downloaded)

### 4. mga (Plural Marker) — severity 1.5

**`mga`** (pronounced "manga") is the plural/collective marker. It goes **BEFORE the noun**.

| Singular | Plural |
|---|---|
| tao (person) | **mga tao** (people) |
| libro (book) | **mga libro** (books) |
| file | **mga file** |
| user | **mga user** |
| bata (child) | **mga bata** (children) |

**Critical rules for when to use mga:**

#### Rule 1: REQUIRED for plural nouns in plain text

- ❌ "Mag-upload ng File" (when source is "Upload Files" — plural) → ✅ "**Mag-upload ng mga file**"
- ❌ "Pumili ng item" (when source is "Select items") → ✅ "**Pumili ng mga item**"
- ❌ Removing mga from a plural translation CHANGES THE MEANING from plural to singular

#### Rule 2: OMITTED with numbers / quantifiers

When a number directly precedes the noun (or via ligature), `mga` is omitted:

- ❌ "limang mga tao" → ✅ "**limang tao**" (five people)
- ❌ "5 mga proyekto" → ✅ "**5 proyekto**" (5 projects)
- ❌ "3 mga file" → ✅ "**3 file**" (3 files — or "tatlong file" with native number)

**Note:** Native Tagalog numbers use the ligature: isang (one), dalawang (two), tatlong (three), apat na (four — `na` after consonant), limang (five), animan/anim na (six), pitong (seven), walong (eight), siyam na (nine), sampung (ten). With ligature, no mga needed.

#### Rule 3: OMITTED with ICU plural `#` substitution

ICU patterns where `#` substitutes the count number — no `mga`:

```icu
{count, plural,
  one {# proyekto}
  other {# proyekto}
}
```

NOT:
```icu
{count, plural,
  other {# mga proyekto}  // WRONG — # is a number, so no mga
}
```

#### Rule 4: OMITTED in zero/empty states with "Wala pang"

Empty-state messages typically omit `mga`:

- ❌ "Wala pang mga proyekto" → ✅ "**Wala pang proyekto**" (No projects yet)
- ❌ "Wala pang mga gumagamit" → ✅ "**Wala pang gumagamit**" (No users yet)

The zero state is treated as generic/collective rather than countable plural.

#### Rule 5: OPTIONAL for collective / generic references

- "Lahat ng file" (all files — collective, no mga needed) vs "Lahat ng mga file" (both acceptable, slightly different connotation)
- "May mga problema" (there are problems) — `mga` emphasizes plural
- "May problema" (there is a/are problems) — number left ambiguous

### 5. na / -ng Ligature — severity 1.5

The **ligature** (na or -ng) links a modifier to its noun. It is **mandatory** in most attributive constructions.

- **-ng** attaches to words ending in a **vowel** (or in the consonant **n** which merges)
- **na** is used after words ending in any other consonant

| Wrong (no ligature) | Correct (with ligature) | Gloss |
|---|---|---|
| bago file | **bagong file** | new file (bago + -ng) |
| malaki bahay | **malaking bahay** | big house (malaki + -ng) |
| maganda kotse | **magandang kotse** | beautiful car (maganda + -ng) |
| mataas kalidad | **mataas na kalidad** | high quality (mataas + na — consonant) |
| mahirap problema | **mahirap na problema** | difficult problem (mahirap + na) |
| limang tao | ✅ correct | five people (lima + -ng) |
| apat tao | **apat na tao** | four people (apat + na) |

**The ligature attaches to the FIRST WORD of the modifier phrase** (the modifier, not the noun):
- ✅ **"bagong file"** — bago + -ng + file
- ✅ **"isang malaking file"** — isa + -ng + malaki + -ng + file (two ligatures: between numeral and adj, and between adj and noun)
- ✅ **"mahirap na bagong problema"** — mahirap + na + bago + -ng + problema

**Common errors:**
- ❌ "bago file" / "malaki bahay" — missing ligature entirely
- ❌ "filebago" — fusing without ligature
- ❌ "mataasng kalidad" — using -ng after consonant (should be na)
- ❌ "magandana kotse" — confusing na/-ng placement

### 6. Reduplication — severity 1.5

Reduplication is a productive morphological process in Tagalog. It does multiple jobs:

| Function | Pattern | Example |
|---|---|---|
| Plural / variety | Full root reduplication | tao → tao-tao (various people, every-person — colloquial); halaman → halaman-halaman |
| Diminutive / intensity | Full reduplication of adjective | maganda → maganda-ganda (somewhat beautiful), maliit → maliit-liit (somewhat small) |
| Verb imperfective aspect | First CV of root | save → sini-save; bili → bumibili |
| Contemplated aspect | First CV of root (without realis) | save → ise-save; bili → bibili |
| Plurality of action | First CV of root | tumakbo → tumakbo-takbo (kept running, ran repeatedly) |

For UI, reduplication mainly matters for **aspect marking** on verbs (loading states) and occasionally for nouns where mga is awkward.

### 7. Spanish-Derived Loanwords (Integrated, Not Code-Switched)

Tagalog has **deeply integrated Spanish loanwords** from 350+ years of Spanish colonization. These are NOT code-switching — they are fully Tagalogized:

| Spanish source | Tagalog (current spelling) | Meaning |
|---|---|---|
| silla | **silya** | chair |
| coche | **kotse** | car |
| cuento | **kwento** | story |
| libro | **libro** | book |
| (peso → ) pera | **pera** | money |
| mesa | **mesa** | table |
| ventana | **bintana** | window |
| cocina | **kusina** | kitchen |
| baño | **banyo** | bathroom |
| zapatos | **sapatos** | shoes |
| oración | **orasyon / panalangin** | prayer |
| medio | **medyo** | somewhat / kinda |
| pero | **pero** | but |
| porque | **porke** | because (colloquial) |
| siempre | **siyempre** | of course |
| trabajo | **trabaho** | work / job |
| escuela | **eskwela / paaralan** | school |
| iglesia | **iglesya / simbahan** | church |
| fiesta | **pista / piyesta** | feast / party |

**Spanish-derived numbers** (uno, dos, tres, etc.) are used for **time, currency, and counting**:
- Time: "alas dos" (2 o'clock), "alas singko y media" (5:30)
- Money: "singkwenta pesos" (50 pesos), "isang daan" (also Native: 100)
- Native numbers (isa, dalawa, tatlo, apat, lima) for general counting

**Filipino spelling reform (1987, then 2001)** simplified the orthography:
- c, f, j, ñ, q, v, x, z previously borrowed → mostly nativized as k, p, h, ny, k, b, ks, s
- Old spelling "cuento" → modern "kwento"; old "español" → modern "espanyol" or "Espanyol"
- The 28-letter Filipino alphabet **does include** F, J, Ñ, Q, V, X, Z for proper nouns and modern loanwords (foundation = pundasyon, but Facebook stays Facebook; jeep stays jeep; quiz can be kwis or quiz)

## UI Conventions

### Button Labels — Short Imperative with Focus Affix

Tagalog UI buttons typically use **imperative forms** with focus affixes:

| English | Filipino UI | Notes |
|---|---|---|
| Save | **I-save** | i- prefix for object focus on English root |
| Delete | **I-delete** / **Burahin** | Both common; Burahin is native object focus |
| Cancel | **Kanselahin** / **I-cancel** | Native Kanselahin (Spanish-derived root) preferred for formality |
| Submit | **Isumite** / **I-submit** | |
| Upload | **Mag-upload** / **I-upload** | mag- for actor focus, i- for object focus |
| Download | **Mag-download** / **I-download** | |
| Search | **Maghanap** / Hanapin | Native preferred — avoid "I-search" |
| Edit | **I-edit** / **Baguhin** | |
| Copy | **Kopyahin** / **I-copy** | |
| Paste | **I-paste** / **Idikit** | |
| Close | **Isara** | Native — avoid "I-close" |
| Open | **Buksan** | Native — locative focus -an |
| Browse | **Mag-browse** / **Tingnan** | |
| OK / Confirm | **OK** / **Kumpirmahin** | OK widely used |
| Sign in / Log in | **Mag-sign in** / **Mag-log in** | |
| Sign up | **Mag-sign up** / **Mag-rehistro** | |
| Yes | **Oo** (informal) / **Opo** (polite) | Use Oo in neutral UI buttons |
| No | **Hindi** | Use Hindi in neutral UI buttons |
| Back | **Bumalik** | |
| Next | **Susunod** | |
| Previous | **Nakaraan** / **Nakaraang Pahina** | |
| Send | **Ipadala** | i- object focus |
| Share | **Ibahagi** / **I-share** | |
| Reply | **Sumagot** / **Tumugon** | |
| Done | **Tapos** / **Tapos na** | |

❌ "Mangyaring i-click ang pindutan upang i-save ang file" (verbose) → ✅ "**I-save**"

### Status Messages — Imperfective Aspect

Use **imperfective (CV-reduplicated) aspect** with appropriate focus affix and ellipsis:

| English | Filipino | Notes |
|---|---|---|
| Loading... | **Naglo-load...** / **Naglolod...** | Imperfective actor focus of "load" |
| Saving... | **Sine-save...** / **Sini-save...** | Imperfective object focus of "save" |
| Uploading... | **Ina-upload...** / **Nag-uupload...** | |
| Downloading... | **Dina-download...** | |
| Processing... | **Pinoproseso...** | Imperfective object focus |
| Deleting... | **Binubura...** / **Dini-delete...** | |
| Connecting... | **Kumokonekta...** | Imperfective actor focus |
| Sending... | **Ipinapadala...** | Imperfective object focus |
| Searching... | **Naghahanap...** | Imperfective actor focus |
| Updating... | **Ina-update...** / **Ino-update...** | |

**Common errors:**
- ❌ "I-save..." (with ellipsis but plain infinitive — means "to save" not "saving")
- ✅ "**Sine-save...**" / "**Sini-save...**" (actually means "saving" via imperfective aspect)
- ❌ "Tapos na ang pag-save" (verbose past) → ✅ "**Naka-save na.**" / "**Na-save na.**" (saved — completed aspect)

### Drag-and-Drop Vocabulary

Filipino UI typically uses **i-drag** and **i-drop** with the i- prefix (English roots adapted):

- **i-drag** = drag
- **i-drop** = drop
- **bitawan** = release / let go (native verb)
- **i-hila** = pull (more native, sometimes used for drag)

```
✅ I-drag ang mga file dito             (Drag files here)
✅ I-drag at i-drop ang file            (Drag and drop the file)
✅ I-drag ang mga file dito o mag-click (Drag files here or click)
❌ I-drag dito lang                     (incomplete — finish the phrase: "...ang mga file")
❌ Drag dito                            (English without prefix — wrong)
```

### Error Messages — Polite Direct Predicate

Filipino UI prefers **direct predicate** error forms, often softened with "Hindi maaari" (cannot) or "Hindi nagawa" (was not done):

| Wrong (verbose / blame-y) | Correct (direct predicate) |
|---|---|
| Nagkaroon ng problema sa pag-save | **Hindi na-save ang file.** (File was not saved) |
| Hindi mo magawa ito | **Hindi maaaring gawin ito.** (This cannot be done — softer, no blame) |
| Pumalpak ang pag-load | **Nabigo ang pag-load.** / **Hindi ma-load.** (Load failed / Cannot load) |
| Mali ang ginawa mo | **May error sa input.** (There is an error in the input — depersonalize) |

**Cultural note:** Filipino communication avoids direct confrontation/blame (concept of **hiya** — shame/face). Error messages should avoid "you did this wrong" and prefer "this couldn't be done" or "an error occurred".

### Loading / Empty State Conventions

| Context | Pattern | Example |
|---|---|---|
| Loading | imperfective + ellipsis | Naglo-load... / Sine-save... |
| Empty state | Wala pang + noun (no mga) | Wala pang proyekto / Wala pang mensahe |
| Zero count | 0 + bare noun | 0 mensahe / 0 file |
| Saved confirmation | Naka-/Na- + verb | Na-save na. / Naka-save na. |
| Failure | Hindi + na- + verb / Nabigo | Hindi na-save. / Nabigo ang pag-save. |

## Punctuation, Numbers, Dates, Currency

### Quotation Marks

- Standard `"..."` double quotes (US English influence)
- Single `'...'` for nested quotes
- Filipino does NOT use guillemets `«»` or German `„..."`

### Ellipsis

- Use single character `…` (U+2026) rather than three periods `...`
- Common in loading states: "Naglo-load…"

### Comma Rules

Filipino has fewer mandatory commas than English:

**NO comma before coordinating conjunctions** (at, o):
- ❌ "I-drag ang file dito, o mag-click" → ✅ "**I-drag ang file dito o mag-click**" (no comma before o)
- ❌ "I-save ang file, at isara" → ✅ "**I-save ang file at isara**" (no comma before at)

**COMMA before subordinating conjunctions / clauses:**
- na (that): "Sinabi niya, na hindi siya pupunta" (Said he, that he won't go) — comma optional
- kung (if): "Mag-click sa link, kung gusto mong magpatuloy"
- dahil / sapagkat (because): "Hindi gumana, dahil hindi na-save"
- kapag (when): "Tumawag, kapag handa ka na"

**COMMA before tag questions / appositives:**
- "Si Maria, ang manager namin, ay nasa labas." (Maria, our manager, is outside)
- "Nasaan ka, ate?" (Where are you, sister?)

### Numbers — Anglo Format (American Influence)

Filipino uses **Anglo-style** number formatting due to American colonial influence (1898-1946) and continued American economic/cultural influence:

- **Decimal separator: period** (3**.**14)
- **Thousands separator: comma** (1**,**000**,**000)
- Format: `1,234,567.89`
- ❌ 1.234,56 (European) → ✅ **1,234.56**

This is **opposite to Spain** (despite Spanish heritage in vocabulary), opposite to Indonesia, opposite to most of continental Europe — Filipino follows the American convention.

### Dates — MM/DD/YYYY or DD/MM/YYYY (both acceptable)

The Philippines is unusual in accepting BOTH American MM/DD/YYYY and International DD/MM/YYYY date formats:

- **American format (common in government and US-influenced business):** 01/15/2024 = January 15, 2024
- **International format (common in modern apps, scientific contexts):** 15/01/2024 = January 15, 2024
- **Word form:** "Enero 15, 2024" or "15 ng Enero, 2024" or "Ika-15 ng Enero, 2024"

**For UI:** prefer ISO 8601 (YYYY-MM-DD) when machine-readable; use the user's locale preference when ambiguous. For display, MM/DD/YYYY is more common in older systems, DD/MM/YYYY in newer.

### Filipino Months (Spanish-derived, capitalized)

| English | Filipino |
|---|---|
| January | **Enero** |
| February | **Pebrero** |
| March | **Marso** |
| April | **Abril** |
| May | **Mayo** |
| June | **Hunyo** |
| July | **Hulyo** |
| August | **Agosto** |
| September | **Setyembre** |
| October | **Oktubre** |
| November | **Nobyembre** |
| December | **Disyembre** |

### Days of the Week (Spanish-derived, capitalized)

| English | Filipino |
|---|---|
| Monday | **Lunes** |
| Tuesday | **Martes** |
| Wednesday | **Miyerkules** |
| Thursday | **Huwebes** |
| Friday | **Biyernes** |
| Saturday | **Sabado** |
| Sunday | **Linggo** (or formally **Domingo**) |

Week starts on Monday in business contexts; Linggo means both "Sunday" and "week" — context disambiguates.

### Time

Filipino uses both 12-hour (everyday speech) and 24-hour (formal/military/transit) formats:

- 12-hour: `2:30 PM` or `2:30 ng hapon`
- 24-hour: `14:30`

**Time-of-day periods:**

| Period | Filipino | Approx. time |
|---|---|---|
| Morning | **umaga** | dawn–11am ("ng umaga" = AM) |
| Noon | **tanghali** | 11am–1pm |
| Afternoon | **hapon** | 1pm–6pm ("ng hapon" = PM afternoon) |
| Evening / Night | **gabi** | 6pm–midnight ("ng gabi" = PM evening) |
| Late night / dawn | **madaling-araw** | 12am–4am |

Spanish-derived time expressions are common: "alas dos" (2 o'clock), "alas singko y media" (5:30), "alas siyete" (7:00).

### Currency: PHP Philippine Peso (₱)

- **Symbol:** `₱` (U+20B1) or `PHP`
- **Format:** `₱1,234.56` (Anglo format — comma thousands, period decimal)
- Examples: `₱100`, `₱1,500`, `₱25,000`, `₱1,000,000.00`
- The peso is divided into 100 centavos but centavos rarely appear in modern UI (small denominations)
- ❌ Rp 1,000 (Indonesian rupiah) → ✅ **₱1,000**
- ❌ ₱1.234,56 (European number format) → ✅ **₱1,234.56**

**Spelling:** peso (singular), piso (Tagalog variant), pesos (plural in English contexts), salapi (formal/literary "money").

## Terminology Quick Reference

| English | Filipino UI Term | Alternative / Native |
|---|---|---|
| Save | **I-save** | (no common native — i- + English root) |
| Delete | **I-delete** / **Burahin** | Burahin = native |
| Cancel | **Kanselahin** / **I-cancel** | Kanselahin = Spanish-derived nativized |
| Submit | **Isumite** / **I-submit** | |
| Upload | **Mag-upload** / **I-upload** | |
| Download | **Mag-download** / **I-download** | |
| Settings | **Mga Setting** / **Mga Setting** | Native: **Mga Kaayusan** (less common) |
| Update | **I-update** / **Mag-update** | |
| Search | **Maghanap** / **Hanapin** | Native preferred over I-search |
| Edit | **I-edit** / **Baguhin** | Baguhin = native (change) |
| Copy | **Kopyahin** / **I-copy** | |
| Paste | **I-paste** / **Idikit** | Idikit = native (stick/attach) |
| Close | **Isara** | Isara = native |
| Open | **Buksan** | Buksan = native |
| File | **File** / **Talaksan** | Talaksan = native (rarely used in casual UI) |
| Folder | **Folder** / **Kahon** | Folder more common |
| Window | **Window** / **Bintana** | Bintana = native window |
| Message | **Mensahe** | (Spanish-derived nativized) |
| User | **User** / **Gumagamit** | Gumagamit = native (one who uses) |
| Password | **Password** / **Kontrasenyas** | Password far more common |
| Username | **Username** | |
| Log in | **Mag-log in** / **Mag-sign in** | |
| Log out | **Mag-log out** / **Mag-sign out** | |
| Dashboard | **Dashboard** | |
| Account | **Account** / **Kuwenta** | Kuwenta exists but less common |
| Email | **Email** / **Liham elektroniko** | Liham elektroniko = literary |
| Click | **Mag-click** / **I-click** | |
| Loading | **Naglo-load** | (imperfective) |
| Cancel (button) | **Kanselahin** / **Bumalik** | |
| Confirm | **Kumpirmahin** | |
| Continue | **Magpatuloy** | |
| Next | **Susunod** | |
| Previous | **Nakaraan** | |
| Back | **Bumalik** | |
| Yes | **Oo** | |
| No | **Hindi** | |
| Welcome | **Maligayang pagdating** | |
| Thank you | **Salamat** | (add po for politeness: Salamat po) |
| Profile | **Profile** / **Tala** | Profile far more common |
| Notification | **Abiso** / **Notification** | |
| Help | **Tulong** | |
| Settings | **Mga Setting** | |
| Search results | **Mga resulta ng paghahanap** | |
| No results | **Walang resulta** | |
| More | **Pa** / **Higit pa** | |
| Show more | **Magpakita pa** | |
| Show less | **Magpakita ng kaunti** | |

### Brand & Proper Names

- Keep brand names in original form: Apple, Google, Facebook, Microsoft, Webflow
- Country names: **Pilipinas** (Philippines), **Estados Unidos** or just **US** (United States — "Estados Unidos ng Amerika" is overly formal/literary for UI), **Hapon** (Japan), **Tsina** or **Intsik** is dated (use **Tsina** or **China**), **Inglatera** (England — old) or **United Kingdom** in modern usage
- Acronyms acceptable: **PNB** (Philippine National Bank), **BIR** (Bureau of Internal Revenue), **DTI** (Department of Trade and Industry), **DOH** (Department of Health), **SSS** (Social Security System)

### English Loanwords in Tech (Taglish-Acceptable)

The following English words are **fully acceptable** in formal Filipino UI — coining native equivalents would feel forced:

- file, folder, server, browser, app, link, click, scroll, swipe, button, tab, menu, login, logout, password, username, email, internet, website, online, offline, video, audio, download, upload, save, delete, copy, paste, edit, share, post, comment, like, follow, friend, search, profile, account, message, chat, notification, settings, account, dashboard, refresh, sync, backup, update, install, uninstall

When attaching these to Tagalog grammar, use **i-** prefix (object focus) or **mag-** prefix (actor focus):
- **i-** + English root: i-save, i-delete, i-click, i-upload, i-edit, i-cancel
- **mag-** + English root: mag-upload, mag-login, mag-search, mag-print, mag-share

### Native Equivalents That Are Preferred (When Available)

For some common UI verbs, the **native Filipino form is strongly preferred**:

| English (calque) | Native (preferred) |
|---|---|
| I-search | **Maghanap** / **Hanapin** |
| I-open | **Buksan** |
| I-close | **Isara** |
| I-delete (formal) | **Burahin** / **Tanggalin** |
| I-cancel (formal) | **Kanselahin** |
| I-confirm | **Kumpirmahin** |
| I-print | **Mag-print** (acceptable) / **Maglimbag** (formal) |

## Calque / Anti-Pattern Blocklist

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| Nagkakaroon ng kahulugan | **May katuturan / Makatuwiran** | "makes sense" (literal) |
| Sa dulo ng araw | **Sa bandang huli / Sa kabuuan** | "at the end of the day" |
| Kumuha ng pahinga | **Magpahinga** | "take a break" — Filipino has a single verb |
| Mag-sync nang walang putol | **I-sync nang tuluy-tuloy** | unnatural Tagalog construction |
| Kapag maging available na | **Kapag naging available na / Kapag magagamit na** | wrong verb form |
| {min} na character ang haba | **hindi bababa sa {min} character** | redundant "ang haba" (the length) |
| 5 minuto ang haba | **5 minuto** | duration doesn't need "length" modifier |
| Estados Unidos ng Amerika (in UI) | **US / Estados Unidos** | overly formal |
| Pumalpak ang pag-load | **Nabigo ang pag-load** | "pumalpak" is too colloquial/informal for UI |
| {count} mga proyekto | **{count} proyekto** | mga redundant with number |
| Wala pang mga proyekto | **Wala pang proyekto** | zero state omits mga |
| 25+ na wika | **higit sa 25 wika / 25 wika o higit pa** | "25+" English calque |
| User-friendly | **madaling gamitin / friendly sa user** | English compound calque |
| AI-powered | **pinapatakbo ng AI / batay sa AI** | English compound calque |
| Long-term | **pangmatagalan / matagal-tagal** | English compound calque |
| Bago file (no ligature) | **Bagong file** | missing -ng ligature |
| 5 mga file | **5 file** | mga redundant with number |
| Mag-upload ng File (for plural) | **Mag-upload ng mga file** | missing mga for plural |
| Patahakin (misspelling) | **Patakbuhin** (run it) | check root verb |

## Cultural Sensitivity

### Religious Diversity

The Philippines is the **only majority-Christian country in Asia**:
- **Roman Catholic** — ~80% of population. Holy Week (Mahal na Araw), Christmas (Pasko), All Saints/Souls Day (Undas) are major.
- **Other Christian denominations** — ~10% (Iglesia ni Cristo, Born Again, Aglipayan, etc.)
- **Muslim** — ~5%, concentrated in Mindanao (Maranao, Maguindanao, Tausug, Sama, Yakan). Eid al-Fitr is a national holiday.
- **Indigenous animist traditions** — small but culturally significant in highland regions.

**UI guidance:**
- Avoid making assumptions about religion in mass-market UI
- Use neutral greetings: "Maligayang pagdating" (Welcome) rather than religious salutations
- For Christmas: "Maligayang Pasko" (Merry Christmas) is universal and acceptable
- For Eid: "Eid Mubarak" is used by Muslim Filipinos
- Don't equate "Filipino" with "Catholic" — there are millions of Muslim Filipinos and they are equally Filipino

### Pakikisama, Hiya, Utang na Loob

Filipino culture has nuanced concepts that affect communication style:

- **Pakikisama** — smooth interpersonal relations, going along with the group
- **Hiya** — sense of shame / face; preserving dignity for self and others
- **Utang na loob** — debt of gratitude / inner debt for kindness received
- **Po / opo** — respect particles, especially to elders/superiors

**Translation implications for UI:**
- Avoid blame-language in errors ("Mali ang ginawa mo" → "May problema sa input")
- Use indirect/softened constructions ("Hindi maaaring gawin" rather than "Hindi mo magawa")
- Express gratitude generously ("Salamat sa paggamit" = thanks for using)
- Avoid abrasive imperatives — soften with `paki-` prefix when appropriate ("Pakitingnan" = please look at)

### Regional Languages and "Filipino"

Filipino is the **national language**, but the Philippines has **170+ languages**. Tagalog/Filipino is the lingua franca, but speakers of Cebuano, Hiligaynon, Ilocano, Bikol, Waray, Kapampangan, Pangasinan, Tausug, Maranao, etc. may use Filipino as a second language.

**For UI:**
- Default to standard Filipino (Tagalog-based)
- For very specific regional markets, consider Cebuano (ceb) as a separate locale
- Avoid Manila-centric idioms when the audience is national

### Family and Social Address

Filipino has rich kinship vocabulary used as polite forms of address:

| Term | Meaning |
|---|---|
| **Kuya** | Older brother / older male (polite to slightly-older man) |
| **Ate** | Older sister / older female |
| **Lolo** | Grandfather (also: old man) |
| **Lola** | Grandmother (also: old woman) |
| **Tito** | Uncle (also: family friend, older man) |
| **Tita** | Aunt (also: family friend, older woman) |
| **Manong / Manang** | Polite "sir/ma'am" for older blue-collar / Ilocano-influenced |

These are **rarely used in UI** but appear in marketing copy that wants to evoke warmth/family.

## Self-Check Checklist

Run BEFORE finalizing each translation:

**Identity (CRITICAL):**
- [ ] **Austronesian grammar, NOT Spanish/English calque:** verb-initial, focus system, ang/ng/sa markers
- [ ] **Verb is first** (V1 word order — predicate before subject)
- [ ] **Filipino vocabulary, not Cebuano/Ilocano:** ano (what), saan (where), kailan (when), bakit (why)
- [ ] **Number format Anglo:** 1,234.56 (comma thousands, period decimal) — NOT 1.234,56
- [ ] **Currency ₱ (Peso),** NOT Rp or other
- [ ] **Day names Filipino:** Lunes/Martes/Miyerkules/Huwebes/Biyernes/Sabado/Linggo

**Focus System & Verb Affixes:**
- [ ] **Correct focus affix** for the intended argument (i- for object focus, mag-/-um- for actor focus, -an for locative)
- [ ] **Aspect marked correctly** (reduplication for imperfective — "Sine-save..." not "I-save...")
- [ ] **i- prefix used for English-root commands** (i-save, i-delete, i-upload)
- [ ] **Native verbs preferred where established:** Maghanap (not I-search), Buksan (not I-open), Isara (not I-close)
- [ ] **Aspect matches context:** infinitive for buttons (I-save), imperfective for loading (Sine-save...), completed for status (Na-save na)

**Plurality (mga):**
- [ ] **mga REQUIRED** for plural nouns in plain text (mga file, mga tao, mga proyekto)
- [ ] **mga OMITTED with numbers** (5 file NOT 5 mga file; limang tao NOT limang mga tao)
- [ ] **mga OMITTED in ICU `#` patterns** (`{count, plural, other {# proyekto}}` — no mga)
- [ ] **mga OMITTED in "Wala pang" zero states** (Wala pang proyekto)
- [ ] **Never remove mga from a plural** — changes meaning to singular

**Ligature (na/-ng):**
- [ ] **-ng after vowels** (bagong file, malaking bahay, limang tao)
- [ ] **na after consonants** (mataas na kalidad, apat na tao, mahirap na problema)
- [ ] **Ligature attached to first word of modifier phrase**
- [ ] **No missing ligatures** (bago file → bagong file)

**Register & Politeness:**
- [ ] **kayo for formal singular/plural** OR **ikaw/ka for informal singular** — consistent throughout
- [ ] **No po/opo in UI buttons** (I-save NOT I-save po)
- [ ] **po/opo only in customer-service tone** or polite messages where deference is warranted
- [ ] **Formal vocabulary:** hindi (not 'di), lamang (not lang for formal contexts), huwag (not 'wag), iyon (not 'yung), bagaimana paano (not pano)
- [ ] **kami vs tayo correct:** kami when company speaks to user; tayo when action is shared

**Punctuation & Formatting:**
- [ ] **No comma before at / o** (Filipino doesn't comma before coordinating conjunctions)
- [ ] **Comma before subordinating** dahil/kung/kapag/sapagkat
- [ ] **Single ellipsis character …** not three periods
- [ ] **₱ symbol** for Philippine Peso
- [ ] **Anglo number format** (₱1,234.56)
- [ ] **Filipino month and day names** (Enero, Pebrero, Lunes, Martes)

**Naturalness:**
- [ ] **No SVO calque** — verbs come first
- [ ] **No bare-root verbs** where focus affix required (I-save not just Save; Buksan not just Open)
- [ ] **Reduplication on loading states** (Sine-save... not I-save...)
- [ ] **Error messages depersonalized** (Hindi maaaring gawin, not Hindi mo magawa)
- [ ] **Taglish balance appropriate** — English tech terms OK, but follow Tagalog grammar
- [ ] **Religious neutrality** — no Catholic-specific assumptions in mass-market UI
- [ ] **Brand names preserved** in original form
- [ ] **Placeholders preserved exactly** ({name}, {count}, {{url}})

## Worked Examples

### Example 1 — Save button + loading + completed

**Source:**
> Save
> Saving your changes...
> Changes saved.

**Wrong (no reduplication for loading; calque-y completion):**
> I-save
> I-save ang iyong mga pagbabago... (infinitive — means "to save", not "saving")
> Ang iyong mga pagbabago ay na-save na. (overly literal SVO with `ay` inversion)

**Correct:**
> **I-save**  (object focus infinitive — button)
> **Sine-save ang iyong mga pagbabago...**  (imperfective object focus — actually means "saving")
> **Na-save na ang iyong mga pagbabago.**  (completed aspect, V1 — "(Have been) saved already, your changes")

### Example 2 — Plural mga + number combinations

**Source:**
> Upload Files (button — plural)
> 5 files uploaded
> Files (general label)
> No files yet (empty state)

**Wrong:**
> Mag-upload ng File  (missing mga for plural)
> 5 mga file na-upload  (mga redundant with number)
> File-file  (wrong — full reduplication isn't standard for nouns)
> Wala pang mga file  (mga should be omitted in zero state)

**Correct:**
> **Mag-upload ng mga file**  (mga required for plural)
> **5 file ang na-upload**  (no mga with number; V1 with focus)
> **Mga file**  (mga for general plural label)
> **Wala pang file**  (no mga in zero state)

### Example 3 — Focus system: same event, different focus

**Source:**
> The user bought the book.

Three ways to express it, depending on what's in focus:

> **Bumili ang user ng libro.**  (Actor focus — emphasizes WHO did it: "The USER bought a book.")
> **Binili ng user ang libro.**  (Object focus — emphasizes WHAT was bought: "The user bought the BOOK.")
> **Binilhan ng user ng libro ang tindahan.**  (Locative focus — emphasizes WHERE: "The user bought a book AT THE STORE.")

For UI: use **actor focus (mag-/-um-)** when describing what the user does ("Nag-save ang user ng file"). Use **object focus (i-/-in)** for imperatives acting on items ("I-save ang file").

### Example 4 — Ligature na/-ng

**Source:**
> A new file / a big house / high quality / a difficult problem

**Wrong (missing or wrong ligature):**
> Bago file (no ligature)
> Malaki bahay (no ligature)
> Mataasng kalidad (wrong: -ng after consonant)
> Mahirapng problema (wrong: -ng after consonant)

**Correct:**
> **Bagong file** (bago + -ng — vowel ending)
> **Malaking bahay** (malaki + -ng — vowel ending)
> **Mataas na kalidad** (mataas + na — consonant ending)
> **Mahirap na problema** (mahirap + na — consonant ending)

### Example 5 — Drag and drop (complete the phrase)

**Source:**
> Drag and drop files here, or click to browse

**Wrong (English calque + incomplete):**
> Drag and drop files dito, or click to browse  (mostly English)
> I-drag at i-drop dito, o mag-click  (incomplete — what is dragged?)

**Correct:**
> **I-drag at i-drop ang mga file dito o mag-click upang mag-browse**  (complete phrase, no comma before o, mga for plural)

### Example 6 — Formal vs informal register

**Source:**
> Are you sure you want to delete this file?

**Wrong (colloquial in formal UI):**
> Sigurado ka bang gusto mong burahin 'tong file na 'to?  ('tong/'to colloquial)

**Wrong (po/opo in plain UI):**
> Sigurado po ba kayong gustong burahin ang file na ito?  (po doesn't belong in confirmation dialogs)

**Correct (formal, neutral, no po):**
> **Sigurado ka bang gusto mong burahin ang file na ito?**  (informal ka — for casual brand)
> **Sigurado ba kayong gustong burahin ang file na ito?**  (formal kayo — for business UI)

### Example 7 — Loading state with aspect

**Source:**
> Loading... / Saving... / Uploading...

**Wrong (no imperfective marking — looks like infinitive):**
> I-load...  (means "to load", not "loading")
> I-save...  (means "to save", not "saving")
> I-upload...  (means "to upload", not "uploading")

**Correct (imperfective with CV reduplication):**
> **Naglo-load...**  (actor focus imperfective)
> **Sine-save...**  (object focus imperfective)
> **Ina-upload...**  /  **Nag-uupload...**  (object focus / actor focus imperfective)
> **Pinoproseso...**  (Processing — object focus imperfective)

### Example 8 — Error messages (depersonalized)

**Source:**
> You can't do that. / The file failed to save. / Invalid input.

**Wrong (blame-y / verbose):**
> Hindi mo magawa iyan.  (direct "you can't" — too confrontational for Filipino tone)
> Nagkaroon ng problema sa pag-save ng file.  (verbose nominal construction)
> Mali ang ginawa mo.  (blame-y)

**Correct (depersonalized, direct predicate):**
> **Hindi maaaring gawin iyan.**  (That cannot be done — soft, depersonalized)
> **Hindi na-save ang file.**  (File was not saved — direct predicate, V1)
> **May error sa input.**  (There is an error in the input — depersonalized)

### Example 9 — Inclusive tayo vs Exclusive kami

**Source:**
> Let's get started! / We will send you an email.

**Wrong:**
> Magsimula tayo! (acceptable but missing the warmth)
> Kami magpapadala ng email sa'yo. (English-ish word order)
> Magpapadala tayo ng email. (wrong — implies user is also sending)

**Correct:**
> **Magsimula na tayo!**  (Let's start — inclusive tayo for shared action)
> **Magpapadala kami ng email sa iyo.**  (We will send you email — exclusive kami, company speaks to user)

### Example 10 — Date and currency

**Source:**
> Due: January 15, 2024. Amount: $1,234.56 = ₱70,000

**Wrong (European number format):**
> Due: Enero 15, 2024. Halaga: ₱70.000  (Indonesian-style period thousands — wrong for Filipino)
> Due: 15/01/2024. Halaga: ₱70,000.00  (DD/MM/YYYY acceptable but inconsistent with American format)

**Correct:**
> **Takdang petsa: Enero 15, 2024. Halaga: ₱70,000.00**  (American MM word DD, YYYY; Anglo number format)
> or
> **Takdang petsa: 15 ng Enero, 2024. Halaga: ₱70,000.00**  (Filipino word-form date)
> or (machine-readable)
> **Takdang petsa: 2024-01-15. Halaga: ₱70,000.00**

### Example 11 — Welcome message with politeness

**Source:**
> Welcome! Thank you for signing up.

**Wrong (mixed register):**
> Maligayang pagdating po! Salamat sa pag-sign up.  (po+plain mixed)
> Welcome ka! Thanks for nag-sign up ka.  (Taglish overload)

**Correct (formal, consistent):**
> **Maligayang pagdating! Salamat sa pag-sign up.**  (neutral formal)
> **Maligayang pagdating po! Salamat po sa pag-sign up.**  (full polite register — for customer-service tone)
> **Welcome! Salamat sa pag-sign up.**  (mild Taglish, common in modern Filipino apps)

### Example 12 — Search results

**Source:**
> Searching... / Found 5 results / No results found / Showing 1-10 of 234 results

**Correct:**
> **Naghahanap...**  (imperfective actor focus)
> **5 resulta ang natagpuan.**  (V1, focus marker; no mga because numbered)
> **Walang resulta.**  / **Walang nakitang resulta.**  (no results found)
> **Ipinapakita ang 1-10 sa 234 resulta.**  (V1, imperfective object focus, no mga because numbered)

## When in Doubt

1. **Tagalog or Filipino?** For UI purposes, they're effectively the same. Use the term "Filipino" in metadata if the project audience is national; "Tagalog" if focused on Luzon or older systems. ISO code `tl` or `fil` are interchangeable in practice.

2. **Verb-initial or SVO?** Always verb-initial (V1) unless you have a specific literary/emphatic reason for the `ay` inversion. Default: **Kumakain ako** (Eat I) not **Ako ay kumakain**.

3. **Which focus affix?**
   - Acting ON an object (English root) → **i-**: i-save, i-delete, i-click, i-upload
   - Acting ON an object (native root) → **-in**: kainin, burahin, kanselahin
   - Locative ("at"/"on" something) → **-an**: buksan, lagyan
   - Actor performs an action → **mag-** or **-um-**: mag-upload, kumain, sumulat
   - Default for English-root UI buttons: **i-**

4. **Aspect for loading states?** Always reduplicate the first CV → **Sine-save...** not **I-save...** for "Saving..."

5. **mga or no mga?**
   - Plural noun, no number → **YES mga**: mga file, mga tao
   - Plural noun, with number → **NO mga**: 5 file, limang tao
   - ICU `# noun` → **NO mga**: `{count, plural, other {# file}}`
   - "Wala pang X" zero state → **NO mga**: Wala pang file

6. **na or -ng ligature?**
   - After vowel (or n) → **-ng**: bagong file, malaking bahay, limang tao
   - After other consonant → **na**: mataas na kalidad, apat na file

7. **kayo or ikaw?** Default **kayo** for business UI (formal). Use **ikaw/ka** only for explicit casual brand voice.

8. **kami or tayo?** **kami** when the company speaks TO the user (excludes user). **tayo** when the action is shared (includes user). "Let's start" = "Magsimula na tayo!" "We will email you" = "Magpapadala kami ng email."

9. **po or no po?** **No po in UI buttons.** Use po only for explicit customer-service/respectful tones, welcome screens, or marketing copy where deference is desired.

10. **Native verb or i-+English?** Use the **native verb where it's established** (Maghanap, Buksan, Isara, Burahin, Kanselahin). Use **i-+English root** when the English term is the standard tech term (I-save, I-upload, I-click, I-paste).

11. **English loanword OK?** Tech terms (file, folder, server, app, login, upload, click) are fully acceptable in Filipino UI and follow Tagalog grammar via affixes. Don't force unnatural calques (don't translate "server" as "tagapagsilbi" — server is fine).

12. **Number format?** Anglo style (American influence): comma thousands, period decimal. ₱1,234.56. NOT European.

13. **Date format?** Both MM/DD/YYYY and DD/MM/YYYY acceptable. Word form: "Enero 15, 2024" (Spanish-derived month, capitalized).

14. **Currency?** ₱ Peso. Format: ₱1,000 (no decimals for round amounts) or ₱1,234.56.

15. **Religious sensitivity?** Default to religiously neutral language. Don't assume Catholic context in mass-market UI. Filipino Muslims, Protestants, Iglesia ni Cristo members, and others are all equally Filipino.

16. **Avoid colloquial in formal UI:** hindi (not 'di), lamang or lang (in casual), huwag (not 'wag), iyon (not 'yung), paano (not pano), saan (not san), kailan (not kelan).

Tagalog/Filipino's Austronesian grammar means most translation errors are at the **focus/affix level** (wrong focus marker, missing aspect reduplication, missing ligature, wrong mga usage) or at the **register level** (po where it doesn't belong, colloquial shortenings in formal UI). When the translation feels off, check the focus affix first, then the aspect, then the ligature, then mga. Trust the V1 word order — don't force English SVO.
