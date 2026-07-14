---
name: localize-et
description: "Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Estonian (et). Enforces the 14-case system (illative for motion, inessive for location, partitive for partial objects), verb-governed case (aitama+partitive, sõltuma+elative), partitive-singular with numbers 2+ (viis faili, NOT viis failid), ICU plural `other` = partitive singular, Teie/sina formality consistency, and native compound nouns (failisüsteem, NOT faili-süsteem) over English calques."
---

# Estonian Translation Rules (et / eesti keel)

Distilled from the production translation prompt. Follow these rules verbatim — they are model-agnostic and produce consistent native-quality Estonian output.

## Mindset

> Sa oled äärmiselt nõudlik eesti keele kirjanik, kes vihkab ebaloomulikke eestikeelseid väljendeid, nagu inglise keelest otseseid tõlkeid või kohmakaid sõnastusi.

Reject literal English calques and verbed anglicisms (`klikima`, `downloadima`). Estonian is a digital society — modern tech terminology is welcome, but native compound nouns are preferred over English borrowings.

## Pre-Translation Setup

Lock in before translating:

1. **Formality (sina vs Teie)** — Default to **sina** (informal) for modern software. Teie is acceptable but reads stiff in most consumer/B2B UI. NEVER mix within a file.
2. **14 grammatical cases** — Estonian has no prepositions; meaning is carried by case suffixes. Get the case wrong and the meaning shifts entirely.
3. **No grammatical gender** — `ta` = he / she / it. Adjectives agree in CASE and NUMBER only.
4. **Partitive singular with numbers 2+** — UNIQUE to Estonian/Finnish. `viis faili` (singular!) NOT `viis failid`.
5. **Placeholders** — Preserve `{variables}` and ICU plural syntax exactly.

## Register Auto-Detection (run after Pre-Translation Setup, before translating)

If the user has NOT specified sina or Teie, infer from source text register. Match output to source — formal source → Teie; informal source → sina. **Estonian calibration is UNIQUE: even moderately formal source defaults to sina in modern software UI; Teie reads as stiff or old-fashioned in most contexts.**

### Formal source signals → output Teie / teie / Teid
- Hedging / polite modals: "please", "kindly", "we recommend", "we kindly request", "could you"
- Passive / impersonal constructions: "users are advised", "it is recommended", "applicants must"
- No contractions: "do not", "cannot", "we will"
- Domain vocabulary: legal, financial, healthcare, regulatory, government, banking, insurance, formal contracts
- Third-person / distance: "the user must", "customers should"
- Long sentences, formal connectors
- Brand voice: bank, government, legal tech, insurance, healthcare formal correspondence
- No exclamations or emojis

### Informal source signals → output sina / sa / sinu / su (modern Estonian default)
- ANY of: contractions, casual greetings, emoji, exclamations, slang, consumer-app voice
- Lifestyle, gaming, social, e-commerce, productivity apps — all default to sina
- Marketing copy, newsletters, mobile UI — sina is the modern norm

### Mixed / ambiguous source → default to SINA
This is OPPOSITE of most other languages (where formal is the safe default). In Estonian:
- Modern software UI: sina almost always.
- Teie reads stiff and may signal "outdated/government/elderly target".
- Only escalate to Teie if source is explicitly legal/banking/government, OR the user requests it.

### Explicit user override
If the user says "use Teie" / "use formal" / "make it casual", their instruction wins.

### Worked examples

| Source | Detected | Estonian output |
|----------------|----------|------------------|
| "Please review the terms of service before proceeding." | formal | Palun tutvuge teenusetingimustega enne jätkamist. |
| "Hey! Tap here to get started — it's super quick 🚀" | informal | Tere! Puuduta siia, et alustada — see on imekiire 🚀 |
| "Submit your application by the deadline." | formal | Esitage oma avaldus enne tähtaega. |
| "Don't forget to save your work!" | informal | Ära unusta oma tööd salvestada! |

After detection: keep the chosen form consistent. NEVER mix sina/Teie across pronouns, possessives, OR imperatives.

## ⚠️ Critical Rules — Estonian Has Three Highly Distinctive Patterns

These three are the most common sources of unnatural output. They have no analogue in English/Romance/Germanic languages, so the model gets them wrong by default.

### A. Numbers 2+ take partitive SINGULAR (severity 2.0)

| Wrong (English-style plural) | Correct (partitive singular) |
|------------------------------|------------------------------|
| viis failid | **viis faili** |
| kolm kasutajad | **kolm kasutajat** |
| kakskümmend failid | **kakskümmend faili** |
| sada krediidid | **sada krediiti** |

Rule: only `1` takes nominative singular (`üks fail`). Every other number, including `0`, takes partitive singular. This applies recursively in ICU plurals (see below).

### B. ICU plural `other` = partitive singular (CRITICAL)

```icu
{count, plural, one {# fail} other {# faili}}
{count, plural, one {# krediit} other {# krediiti}}
{count, plural, one {# kasutaja} other {# kasutajat}}
```

| Wrong | Correct |
|-------|---------|
| `other {# failid}` | **`other {# faili}`** (partitive singular, not plural) |
| `other {# krediite}` | **`other {# krediiti}`** |

The `other` branch is the partitive SINGULAR form. Common pitfall: most translators reach for the partitive plural by analogy with English/Spanish/etc.

### C. Verb-governed case (severity 2.0)

Each Estonian verb dictates which case its object/complement takes. There's no general rule — these must be memorized.

| Verb | Governs | Example | Wrong (alt case) |
|------|---------|---------|------------------|
| aitama (help) | **partitive** | aitama kasutajat | aitama kasutajale |
| sõltuma (depend on) | **elative** | sõltuma seadetest | sõltuma seadetel |
| huvituma (be interested in) | **elative** | huvituma projektist | huvituma projekti |
| otsima (search for) | **partitive** | otsima faili | (genitive form looks identical for `fail`) |
| uskuma (believe) | **partitive** | uskuma teda | uskuma temale |
| meeldima (please / X likes Y) | **adessive** subj. + **nominative** obj. | mulle meeldib see | minule meeldib seda |
| vajama (need) | **partitive** | vajame faili | vajame failile |
| ootama (wait for) | **partitive** | ootame teie vastust | ootame teie vastusele |

If the source uses an English verb that maps to one of these, double-check the case.

## The 14 Cases — Full Reference

| # | Case | Question | Singular example (`fail`) | When to use |
|---|------|----------|---------------------------|-------------|
| 1 | Nominative | kes? mis? | **fail** | Subject of sentence |
| 2 | Genitive | kelle? mille? | **faili** | Possession; motion direction (often) |
| 3 | Partitive | keda? mida? | **faili** | Partial object; with numbers 2+; with certain verbs |
| 4 | Illative | kuhu? | **faili / failisse** | Motion INTO |
| 5 | Inessive | kus? | **failis** | Location IN |
| 6 | Elative | kust? | **failist** | Motion FROM inside |
| 7 | Allative | kellele? | **failile** | Motion ONTO; recipient |
| 8 | Adessive | kellel? | **failil** | Location ON |
| 9 | Ablative | kellelt? | **faililt** | Motion FROM surface |
| 10 | Translative | kelleks? | **failiks** | Becoming; transformation |
| 11 | Terminative | kelleni? | **failini** | UP TO (limit) |
| 12 | Essive | kellena? | **failina** | AS (role) |
| 13 | Abessive | kelleta? | **failita** | WITHOUT |
| 14 | Comitative | kellega? | **failiga** | WITH (accompaniment / instrument) |

**English preposition → Estonian case** quick map:

| English | Case | Example |
|---------|------|---------|
| in the file | inessive | `failis` |
| into the file | illative | `faili` (or `failisse`) |
| from inside the file | elative | `failist` |
| on the file | adessive | `failil` |
| onto the file | allative | `failile` |
| from the surface of the file | ablative | `faililt` |
| with the file | comitative | `failiga` |
| without the file | abessive | `failita` |
| up to the file | terminative | `failini` |
| as a file | essive | `failina` |
| (becoming) a file | translative | `failiks` |

### Common case errors (severity 2.0)

| Wrong | Correct | Why |
|-------|---------|-----|
| failis (for motion into) | **faili** | illative for "into" |
| süsteemist (for location in) | **süsteemis** | inessive for "in" |
| kasutaja (when partial object) | **kasutajat** | partitive for partial objects |
| failes | **failis** | wrong case form |

### Adjective agreement in case + number

Adjectives must agree with the noun in CASE and NUMBER. No gender to worry about.

| Wrong | Correct |
|-------|---------|
| uus faile (partitive plural) | **uusi faile** |
| uue failid (nominative plural) | **uued failid** |
| suur kasutajat | **suurt kasutajat** (partitive both) |

## Formality — sina vs Teie

| Form | Pronoun | Possessive | Example |
|------|---------|------------|---------|
| Informal (sina) | sina / sa | sinu / su | `Sa saad oma faili salvestada.` |
| Formal (Teie) | Teie / Te | Teie | `Te saate oma faili salvestada.` |

- **Default to sina** for modern software UI. Teie is for very formal/older contexts.
- NEVER mix pronouns, possessives, and imperatives within one file.
- Teie is capitalized when used as the formal address (`Te / Teie / Teid`); `te / teie` lowercase = "you all" (plural informal — rare in software UI).

**Imperative endings:**
- Informal sina: base form — `Salvesta, Logi sisse, Vali kõik`.
- Formal Teie: `-ge / -te` — `Salvestage, Logige sisse, Valige kõik`.

| Don't mix | Use |
|-----------|-----|
| Teie fail on salvestatud. Salvesta uuesti? | **Teie fail on salvestatud. Salvestage uuesti?** (formal) OR **Sinu fail on salvestatud. Salvesta uuesti?** (informal) |
| Laadige üles + Sirvi faile | Laadige üles + **Sirvige** faile (both formal) |

## Negation — invariant `ei` + same stem for all persons

| Wrong (conjugated after ei) | Correct (invariant stem) |
|-----------------------------|--------------------------|
| mina ei salvestan | **mina ei salvesta** |
| meie ei salvestame | **meie ei salvesta** |
| nad ei salvestavad | **nad ei salvesta** |

`ei` does the negation; the verb following is always the bare negative stem (looks like the present-tense `ta` form without ending).

## Word Order

- Default: SVO — `Kasutaja salvestab faili`.
- V2 tendency when an adverb is fronted — the verb stays in the 2nd position:

| Wrong | Correct |
|-------|---------|
| Täna kasutaja salvestab faili | **Täna salvestab kasutaja faili** |
| Pärast seda süsteem käivitub | **Pärast seda käivitub süsteem** |

## Compound Words — Estonian Writes Them TOGETHER

Estonian aggressively compounds nouns. Hyphens are wrong except for abbreviations.

| Wrong (hyphenated like English) | Correct (one word) |
|---------------------------------|---------------------|
| faili-süsteem | **failisüsteem** |
| andme-baas | **andmebaas** |
| kasutaja-sõbralik | **kasutajasõbralik** |
| pilve-põhine | **pilvepõhine** |
| veebi-leht | **veebileht** |

**Exception** — abbreviations DO take a hyphen: `XML-fail`, `e-post`, `IT-osakond`.

## Infinitives — Da vs Ma

Estonian has two infinitive forms; each verb selects the right one based on context.

| Trigger | Infinitive form | Example |
|---------|-----------------|---------|
| tahan, soovin, suudan, võin, oskan | **-da** | `Tahan salvestada` |
| hakkan, lähen, pean, jään | **-ma** | `Hakkan salvestama`, `Lähen ostma` |

| Wrong | Correct |
|-------|---------|
| Tahan salvestama | **Tahan salvestada** |
| Hakkan salvestada | **Hakkan salvestama** |

## Consonant Gradation (severity 1.5)

Strong/weak alternation across cases:

| Strong | Weak |
|--------|------|
| `pp → p` | `kapp → kapi` |
| `tt → t` | `kott → koti` |
| `kk → k` | `pakk → paki` |
| `p → v` | `leib → leiva` |
| `k → g / ∅` | `leping → lepingu` |

These shifts happen during inflection — important when generating case forms.

## Punctuation and Typography

| Item | Estonian |
|------|----------|
| Decimal separator | **`,`** (comma) |
| Thousands separator | **` `** (space) |
| Example number | `1 234,56` |
| Currency | `99,99 €` (symbol AFTER, with NBSP space) — Estonia is in the Eurozone |
| Date | `15.01.2024` (DD.MM.YYYY) or `15. jaanuar 2024` (lowercase months) |
| Time | `14:30` or `kell 14:30` (24-hour) |
| Quotation marks | **`„..."`** (German-style low-9 open + high-6 close), NOT English `"..."` |
| Ellipsis | `…` single character (NOT three periods) |
| Ampersand | `ja` (NOT `&`, except in brand names) |
| Space before unit symbol | yes (NBSP preferred): `10 MB`, `99,9 %` |

| Wrong | Correct |
|-------|---------|
| `1,234.56 €` | **`1 234,56 €`** |
| `"Estonian quotes"` | **`„Estonian quotes"`** |
| `01/15/2024` | **`15.01.2024`** |

## Comma Rules (Estonian is comma-heavy)

| Before | Comma? |
|--------|--------|
| või / ja / ning (or / and) | **No comma** |
| et / kui / sest / mis / kes / kuna (subordinating: that/if/because/which/who/since) | **Comma always required** |
| aga / kuid / ent (but) | **Comma required** |

| Wrong | Correct |
|-------|---------|
| Näen et fail on avatud | Näen**,** et fail on avatud |
| Lohistage siia, või klõpsake | Lohistage siia või klõpsake |
| See on lihtne aga tõhus | See on lihtne**,** aga tõhus |

## Preferred Terms (UI / SaaS vocabulary)

| English | Preferred Estonian | Avoid |
|---------|--------------------|-------|
| save | **salvestama** / button: `Salvesta` | — |
| settings | **seaded** | sätted |
| select | **valima** / `Vali` | — |
| upload | **üles laadima** | uploadima |
| download | **alla laadima** | downloadima |
| log in | **sisse logima** / `Logi sisse` | — |
| log out | **välja logima** / `Logi välja` | — |
| update | **uuendama** | updateima |
| cancel | **tühistama** / `Tühista` / `Loobu` | — |
| delete | **kustutama** / `Kustuta` | deleteima |
| search | **otsima** / `Otsi` | — |
| file | **fail** (accepted loanword, invariable concept; takes Estonian case suffixes) | — |
| folder | **kaust** | — |
| email | **e-post** (`e-kiri` for the message) | email |
| browser | **veebilehitseja** | brauser |
| click | **klõpsama** | klikima |
| dashboard | **töölaud** / `juhtpaneel` | — |
| notifications | **teavitused** | notifikatsioonid |
| native support | **sisseehitatud tugi** | loomulik tugi |
| login credentials | **sisselogimisandmed** | konto mandaadid |
| account | **konto** | — |
| user | **kasutaja** | — |
| Settings | `seaded` | sätted (older; both used but `seaded` more current) |
| Profile | `profiil` | — |
| Account | `konto` | — |
| Sign up / register | `registreeruma / loo konto` | `signupima` |
| Subscribe | `tellima / tellida` | `subscribima` |
| Unsubscribe | `tellimusest loobuma` | — |
| Submit | `esita` (button) / `esitama` | — |
| Apply | `rakenda` (e.g., apply filter) / `taotle` (apply for something) | — |
| Filter | `filter / filtreerima` | — |
| Sort | `sorteerima / järjesta` | — |
| Refresh | `värskenda / uuenda` | `refreshima` |
| Copy | `kopeeri / kopeerima` | — |
| Paste | `kleebi / kleepima` | — |
| Cut | `lõika / lõikama` | — |
| Undo | `võta tagasi` | `undoma` |
| Redo | `tee uuesti` | `redoma` |
| Confirm | `kinnita / kinnitama` | — |
| Continue | `jätka / jätkama` | — |
| Back | `tagasi` | — |
| Next | `edasi` | — |
| Skip | `jäta vahele` | `skipima` |
| Share | `jaga / jagama` | `sharima` |
| Help | `abi` | — |
| Welcome | `tere tulemast / tervitame` | — |
| Success | `õnnestumine / õnnestus` | — |
| Error | `viga` | — |
| Warning | `hoiatus` | — |
| Loading | `laadimine` | — |
| Saving | `salvestamine` | — |
| Required | `nõutav / kohustuslik` | — |
| Optional | `valikuline` | — |
| Free / no cost | `tasuta` | — |
| Paid | `tasuline` | — |
| Premium | `tasuline / premium` | — |
| Trial | `prooviperiood` | — |
| Subscription | `tellimus / tellimine` | — |
| Payment | `makse / maksmine` | — |
| Invoice | `arve` | — |
| Coupon | `kupong / sooduskood` | — |
| Discount | `allahindlus / soodustus` | — |

## Anglicism Verbs — Estonian Prefers Native

| Anglicism (avoid) | Native Estonian |
|-------------------|------------------|
| klikima | **klõpsama** |
| downloadima | **alla laadima** |
| uploadima | **üles laadima** |
| deleteima | **kustutama** |
| editima | **muutma** / `redigeerima` (loan but accepted) |
| checkima | **kontrollima** |

## Software Terminology

| English | Wrong | Correct |
|---------|-------|---------|
| build (software) | (no Estonian word for physical construction works here) | **arendama / koostama / looma** |
| deploy | (military sense) | **juurutama / paigaldama / käiku andma** |
| support (feature) | toetama (general sense) | **toetama** (accepted) / `olema ühilduv` / `ühildub X-iga` |
| pipeline (CI/CD) | toru (= physical pipe) | **konveier / pipeline** (loanword accepted in DevOps) |
| architecture (software) | (construction sense) | **arhitektuur** (context: software) |
| source of truth | (literal) | **ainus tõeallikas / autoriteetne andmeallikas** |
| commit (git) | `giti sisse laaditud` (= uploaded into git — wrong domain) | **committima / giti lisatud** |
| launch (product) | (military / spatial) | **avaldama / käivitama / turule tooma** |
| migrate (data) | (general "move") | **migreerima / üle viima** |

## UI Conventions

### Buttons — imperative (sina form)

| Wrong | Correct |
|-------|---------|
| Salvestage (formal -ge) | **Salvesta** |
| Salvestamine (noun) | **Salvesta** |
| Tühistamine (noun) | **Tühista** |

(If the file uses Teie throughout, buttons take `-ge` form: `Salvestage, Tühistage`. Match formality consistently.)

### Status messages — active 3rd person or impersonal passive

| Wrong | Correct |
|-------|---------|
| Laadimine (noun alone) | **Laeb... / Laetakse...** |
| Salvestamine (noun alone) | **Salvestab... / Salvestatakse...** |
| Analüüs (noun) | **Analüüsib...** |

### Drag and drop

| English | Estonian |
|---------|----------|
| drag | **lohistama** |
| drop | **kukutama** |
| release (let go) | **lahti laskma** |
| browse (file picker) | **sirvima** / action verb: `Vali fail` |

| Wrong | Correct |
|-------|---------|
| Kukutage failid siia | **Lohistage failid siia** (drag is the main action) |
| Vabastage failid siia | **Lohistage ja kukutage siia** |

### Empty state — `Ei ole X` / `Ühtegi X-i ei leitud` / `Tulemused puuduvad`

(The source file is light on explicit empty-state templates — use natural Estonian existential negation. See **Empty State Templates** section below for a full table.)

| Wrong | Correct |
|-------|---------|
| Tühi | **Pole midagi näidata** / `Tulemused puuduvad` |
| Mitte tulemusi | **Ühtegi tulemust ei leitud** / `Tulemused puuduvad` |

### Validation messages

| Type | Mood | Example |
|------|------|---------|
| Field validation | indicative | `See väli on kohustuslik` / `Formaat pole õige` |
| Action instruction | imperative | `Sisestage õige väärtus` (Teie) / `Sisesta õige väärtus` (sina) |
| State description | impersonal | `Ühendust ei õnnestunud luua` |

### Other UI patterns

| Wrong | Correct |
|-------|---------|
| Tugi {formatList} failidele | **Toetatud {formatList} failid** (participle) |
| {name}le (case suffix on placeholder) | **Failile {name}** (restructure to avoid suffix on placeholder) |
| Vali kõik üksused (verbose) | **Vali kõik** (compact bulk action) |
| Eemalda valik kõigilt | **Tühista kõik valikud** (idiomatic bulk deselect) |

## Question Structures

- Yes/no questions: use `Kas` at start. `Kas see töötab?` `Kas soovite jätkata?`
- Wh-questions: question word at start. `Mida sa arvad?` `Kuidas see töötab?`
- Word order can also signal a question (verb-first), but `kas` is the standard UI form.

| Wrong | Correct |
|-------|---------|
| See teeb mõtet? | **Kas sellel on mõtet?** |
| Sa oled kindel? | **Kas sa oled kindel?** / `Oled sa kindel?` |

## Ellipsis Completion

Quantified expressions need a head noun.

| Wrong (bare quantifier) | Correct (with head noun) |
|-------------------------|--------------------------|
| veel 4 muud | **veel 4 faili** / `veel 4 muud elementi` |
| ja 3 muud | **ja 3 muud elementi** |

## "Per" vs "For" Expressions

Estonian doesn't have a single equivalent — disambiguate with case/postposition.

- Rate / each: `kohta` (postposition) → `keele kohta`, `ühe keele eest`, `iga keele eest`
- Total: `{count} keele jaoks` → `{credits} krediiti {count} keele jaoks`, `kokku {count} keele jaoks`

| Wrong (ambiguous) | Correct |
|-------------------|---------|
| {count} keelt {credits} krediiti | **{credits} krediiti {count} keele jaoks** (total) OR **{credits} krediiti keele kohta** (rate) |

## Calques to Avoid

| Wrong (literal) | Natural Estonian |
|-----------------|-------------------|
| tegema mõtet ("make sense") | **on mõtet / on mõistlik** |
| olema kindlal poolel ("on the safe side") | **igaks juhuks / kindluse mõttes** |
| logima sisse (particle after verb — calque) | **sisse logima** (particle BEFORE verb) |
| Break a leg | **Edu! / Kõike head!** |
| Piece of cake | **Lihtne nagu alp / Kerge töö** |

## Russian-Influenced Calques to Avoid

Estonia's historical Russian/Soviet influence left some Russian-influenced expressions that survive in older Estonian. Modern Estonian software UI prefers native phrasings.

Avoid these Russian-influenced constructions:

| Russian-influenced (avoid) | Native Estonian | Reason |
|----------------------------|-----------------|--------|
| `proovid panna` (in sense of "you'll try to put") — Russian word order | natural Estonian SVO | Russian-style verb placement |
| `Ütle mulle, palun...` (overly direct Russian-style request) | `Palun ütle mulle...` | put `palun` at start, Estonian style |
| `igal juhul` (overused — calque of "v lyubom sluchae") | `igatahes / nagunii` | native equivalents are warmer |
| `mitte midagi` (literal "not nothing" — double negative Russian-style) | `midagi pole` / `pole midagi` | Estonian negation is `ei` + verb only |
| `tegema otsust` (Russian-influenced) | `otsustama` (single verb) | Estonian prefers verbed forms over noun + tegema |
| `pidama vajalikuks` (overformalism, Russian bureaucratic) | `arvama, et on vaja` / `pean vajalikuks` | native casual phrasing |
| Excessive `kolleeg` (Russian/Soviet workplace formality) | `kaastöötaja` / just name | use Estonian when natural |
| `külalisõpetaja` (calque from Russian compound) | `külalislektor` / `külaslektor` | use Estonian compound style |

Generally: when in doubt, prefer the native Estonian compound or simple verb over Russian-style noun phrase + dummy verb.

## Compound Adjective Calques

| English | Wrong (hyphenated) | Correct |
|---------|---------------------|---------|
| X-aware / context-aware | konteksti-teadlik / X-teadlik | **konteksti arvestav / X-põhine / X arvesse võttev** |
| X-powered / AI-powered | X-juhitud / IA-juhitud | **X abil / X-l põhinev / X kasutav** |
| X-based / cloud-based | nuvola-põhine / X-põhine (hyphenated) | **pilvepõhine / X-põhine** (one word) / `pilves töötav` |
| user-friendly | kasutaja-sõbralik | **kasutajasõbralik** (one word) / `mugav kasutajale` |

## Proper Nouns — short forms in UI

| Wrong | Correct |
|-------|---------|
| Ameerika Ühendriigid (full form in UI) | **USA** |
| Suurbritannia ja Põhja-Iiri Ühendkuningriik | **Suurbritannia** / `Ühendkuningriik` |

## Cultural Conventions

- Communication style: **direct, efficient, concise**. Estonians are low-context — avoid excessive hedging, apologies, or filler.
- Date: `15.01.2024` (DD.MM.YYYY, periods) or `15. jaanuar 2024` (lowercase months: `jaanuar, veebruar, märts, aprill, mai, juuni, juuli, august, september, oktoober, november, detsember`).
- Time: 24-hour `14:30` or `kell 14:30`.
- Currency: `99,99 €` (EUR, space before symbol).
- Number format: `1 234,56` (space thousands, comma decimal).

## Future Tense — Estonian Has None

Estonian does NOT have a dedicated future tense. Future meaning is expressed by:

1. **Present + adverb of time**: `Tulen homme.` (I will come tomorrow — literally "I come tomorrow"); `Avaldame uue funktsiooni järgmisel nädalal.` (We will release the new feature next week — literally "we release...").
2. **Modal verb `hakkama` + ma-infinitive** (incipient/about to start): `Hakkan tegema seda.` (I'm going to do this); `Süsteem hakkab käivituma.` (The system is about to start).
3. **`saama` (auxiliary)** in some constructions, though limited.

Translation rule: English "will + verb" → Estonian present tense + time adverb, OR `hakkama` + ma-inf for actions about to begin.

Wrong (calquing English): `Ma tahan saada salvestama` (literally "I want to be saving" — incorrect future) → Correct: `Ma salvestan kohe` (I'll save soon) or `Ma hakkan salvestama` (I'm about to save).

UI patterns:
- "Your file will be uploaded" → `Sinu fail laaditakse üles` (passive present, future-implied) OR `Sinu fail hakkab üles laadima` (about to start).
- "We will notify you" → `Me anname sulle teada` (present, future-implied with promise context) OR `Sulle teatatakse` (passive).
- "Loading will take a few moments" → `Laadimine võtab natuke aega` (present, future-implied).

## Gender-Neutral Pronoun `ta`

Estonian has NO grammatical gender. The pronoun `ta` (or `tema` emphatic) means **he / she / it** — all three.

This is a major translation advantage when source is gender-ambiguous: "When a user logs in, they see..." → `Kui kasutaja sisse logib, näeb ta...` (no gendered pronoun choice needed).

For business/formal source distinguishing he/she: just use `ta` — Estonian readers understand from context.

- Possessive: `tema oma` (his/her own) — same word.
- Plural: `nad` (they) for any group.
- Wrong (forcing gender): inventing male/female suffixes — Estonian has none.

This applies to UI references: "User profile" → `Kasutaja profiil` (gender-neutral by default). "Their preferences" → `Tema eelistused` or `Kasutaja eelistused`.

## Empty State Templates

Estonian empty-state phrasings, ranked by formality and context:

| Context | Preferred | Acceptable alternatives |
|---------|-----------|------------------------|
| No results found | `Tulemused puuduvad` | `Ühtegi tulemust ei leitud` / `Midagi ei leitud` |
| No items | `Ühtegi elementi pole` | `Loend on tühi` / `Üksusi pole` |
| No notifications | `Teavitusi pole` | `Uusi teavitusi ei ole` |
| No selection | `Midagi pole valitud` | `Valik puudub` / `Ühtegi üksust pole valitud` |
| Empty inbox | `Postkast on tühi` | `Sõnumeid pole` |
| No data | `Andmed puuduvad` | `Andmeid ei ole / Andmeid pole` |
| No connection | `Ühendus puudub` | `Internetiühendust pole` / `Pole ühendust` |
| File not found | `Faili ei leitud` | `Faili pole olemas` |
| No content | `Sisu puudub` | `Pole midagi näidata` |

- `puuduvad/puudub` (lacks/is missing) sounds neutral and professional.
- `pole / ei ole` (negation existence) sounds more conversational.
- AVOID `Tühi` (empty) by itself — too telegraphic. Always extend: `Postkast on tühi`.

## Greetings and Time-of-Day

- `Tere!` — universal hello (any time, neutral, polite).
- `Tere hommikust!` — good morning (until ~10:00).
- `Tere päevast!` — good day (10:00–17:00, formal).
- `Tere õhtust!` — good evening (17:00 onwards).
- `Head ööd!` — good night (when going to bed).
- `Hei!` / `Tšau!` — casual hello/goodbye (informal, mostly youth).
- `Tere tulemast!` — welcome (UI standard).
- `Nägemiseni!` — goodbye (literally "until seeing"; standard formal/neutral).
- `Head aega!` — goodbye (warmer).
- `Head päeva!` — have a good day (casual closing).
- `Aitäh!` / `Tänan!` — thank you (latter more formal/old-fashioned).
- `Palun!` — please / you're welcome.
- `Vabandust!` — sorry / excuse me.

## Loanword Inflection Patterns

English loanwords MUST take Estonian case suffixes when used in inflected positions.

- `fail` (file) → `faili` (genitive/partitive), `failis` (inessive), `faile` (partitive plural).
- `link` → `lingi` (genitive), `lingis` (inessive), `linke` (partitive plural).
- `app` → `äpp` (with Estonian -p doubling) → genitive `äpi`, inessive `äpis`.
- `klikk` → `kliki` (genitive). NOTE: prefer verb `klõpsama` over `klikkima`.
- `dashboard` → `dashboard'i` (genitive with apostrophe — foreign-word marker), `dashboard'is` (inessive). Or use native `töölaud` / `juhtpaneel`.
- `email` → `email'i` / use `e-post` for natural Estonian.
- For brand names: same apostrophe-suffix pattern: `Google'is` (in Google), `Facebook'i` (Facebook's, genitive).

## Domain Terminology — Preserve IT Meaning

The source explicitly flags this as severity 2.5 (highest tier). Domain-shift errors:

| Source (IT context) | Wrong (general meaning) | Correct |
|---------------------|-------------------------|---------|
| `pipeline` (CI/CD) | toru / torustik (plumbing) | **konveier / pipeline** |
| `architecture` (software) | (building/construction) | **arhitektuur** (IT context) |
| `commit` (git) | `giti sisse laaditud` (= uploaded into git) | **committima / giti lisatud** |
| `launch` (product) | (literal: launch a projectile) | **avaldama / käivitama / turule tooma** |
| `deploy` (code) | (military: deploy troops) | **juurutama / paigaldama / käiku andma** |
| `source of truth` | (literal "truth source") | **ainus tõeallikas / autoriteetne andmeallikas** |

## Placeholder Case-Suffix Issue (severity 1.5)

NEVER attach an Estonian case suffix directly to a placeholder — the placeholder value might already include a name with its own ending, and stacking suffixes produces garbage.

| Wrong | Correct |
|-------|---------|
| `Tere, {name}le!` (suffix on placeholder) | **`Tere, {name}!`** OR `Tere kasutajale {name}!` (move suffix to a host noun) |
| `Faili {name}st` | **`Failist {name}`** (restructure word order) |

## Self-Check Checklist (run before finalizing)

### Critical accuracy (must all pass)
- [ ] **Correct case** from 14 options (illative for motion into, inessive for location, partitive for partial object)
- [ ] **Verb-governed case correct** (aitama+partitive, sõltuma+elative, huvituma+elative, otsima+partitive)
- [ ] **Numbers 2+ take partitive SINGULAR** (`viis faili`, NOT `viis failid`)
- [ ] **ICU `other` branch uses partitive singular** (`other {# faili}`, NOT `# failid`)
- [ ] **Teie/sina consistent** throughout (pronouns, possessives, imperatives)
- [ ] **Adjective agreement** in case + number (no gender to worry about)
- [ ] **Negation** uses invariant `ei` + bare negative stem (`mina ei salvesta`)
- [ ] **Da vs ma infinitive** matches the trigger verb (`Tahan salvestada` / `Hakkan salvestama`)
- [ ] **Compound words** written together (`failisüsteem`, `kasutajasõbralik`, `pilvepõhine`) — hyphen only for abbreviations (`XML-fail`, `e-post`)
- [ ] **No suffix on placeholders** (restructure to put suffix on a host noun)
- [ ] **Punctuation:** `„..."` quotes, comma BEFORE et/kui/sest/aga, no comma before või/ja/ning
- [ ] **Number format** `1 234,56`; date `15.01.2024`; currency `99,99 €`
- [ ] All `{variables}` and ICU intact
- [ ] **Domain terminology** preserves IT meaning (architecture, pipeline, commit, deploy, source of truth)

### Naturalness
- [ ] Buttons in imperative matching formality (`Salvesta` / `Salvestage`)
- [ ] Status messages active/impersonal-passive (`Laeb... / Laetakse...`)
- [ ] Native verbs over anglicism verbs (`klõpsama` not `klikima`, `alla laadima` not `downloadima`, `kustutama` not `deleteima`)
- [ ] No `tegema mõtet` (use `on mõtet`)
- [ ] No hyphenated English-style compound adjectives (`kasutajasõbralik` not `kasutaja-sõbralik`)
- [ ] File picker / browse uses action verbs (`Vali fail`)
- [ ] Drag-drop: `lohistama / kukutama / lahti laskma`
- [ ] Questions use `Kas` for yes/no (`Kas sa oled kindel?`)
- [ ] Ellipsis with head noun (`veel 4 faili` not `veel 4 muud`)
- [ ] Direct, concise tone — no excessive hedging
- [ ] Compound nouns formed natively (`andmebaas`, `failisüsteem`, `töölaud`)
- [ ] Communicative intent preserved (declarative stays declarative, imperative stays imperative — don't swap moods)

## Worked Example

**Source:** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

### Estonian (sina, modern UI default)

Tere tulemast! Vali fail, mille soovid üles laadida. Toetame enam kui 25 formaati ja tõlgime selle 5 keelde {seconds} sekundi jooksul. Ära muretse — saad alati tühistada.

(Notes: `Vali` informal imperative; `mille soovid` relative clause; `üles laadida` da-infinitive after `soovid`; `formaati` partitive singular for `25 formaati` (partitive after enam kui + number); `5 keelde` illative for "into 5 languages"; `{seconds} sekundi jooksul` = "within {seconds} seconds" — restructured to avoid suffix on placeholder; `Ära muretse` informal negative imperative.)

### Estonian (Teie, formal alternative)

Tere tulemast! Valige fail, mille soovite üles laadida. Toetame enam kui 25 formaati ja tõlgime selle 5 keelde {seconds} sekundi jooksul. Ärge muretsege — saate alati tühistada.

(Notes: `Valige / Ärge muretsege` Teie imperative; `soovite` Teie verb form; rest unchanged.)

### Common errors both would catch

- `5 keelt` instead of `5 keelde` — wrong case (nominative vs illative for "into").
- `25 formaatid` — number 2+ takes partitive singular `formaati`.
- `fail-süsteem` → `failisüsteem` (compound together).
- `Vali fail-i {name}le` — never suffix on placeholder.
- `klikkige siia` → `klõpsake siia` (native verb).
- `Tahan salvestama` → `Tahan salvestada` (wrong infinitive after `tahan`).
- `Näen et fail on avatud` → `Näen, et fail on avatud` (missing comma before `et`).
- Mixed `Te valite + Salvesta` → pick one formality.
- `mina ei salvestan` → `mina ei salvesta` (negation invariant).
- `other {# failid}` in ICU → `other {# faili}` (partitive singular).
