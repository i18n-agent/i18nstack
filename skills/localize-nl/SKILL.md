---
name: localize-nl
description: "Use when translating or localizing UI strings, marketing copy, blogs, documentation, error messages, or any product text into Dutch (nl / Nederlands) for the Netherlands (nl-NL — DEFAULT), Belgium (nl-BE / Flemish / Vlaams), or Suriname / Aruba / Curaçao / Sint Maarten. Dutch is West Germanic — sister language to German and Frisian, parent of Afrikaans — but with its OWN gender system (2 genders de/het, NOT 3 like German), its OWN word order (V2 like German but less rigid), and its OWN spelling conventions (ij as a single letter, lowercase months, no noun capitalization). Enforces de/het article correctness (the single biggest source of bugs — \"het probleem\" not \"de probleem\", \"de map\" not \"het map\"), strong vs weak adjective endings (definite + adjective always -e; indefinite het-word = NO -e), V2 word order with verb-final subordinate clauses, separable verbs splitting in main clauses, je vs u formality with full possessive consistency (u+uw, je+jouw — NEVER mix), Dutch number format (1.234,56 — period thousands, comma decimal), DD-MM-YYYY dates with HYPHENS, EUR currency, lowercase months/days (NOT capitalized like German nouns), the productive diminutive system (always neuter het), and Dutch-specific UI calques to avoid (verwijderen not deleten, annuleren not cancelen, \"het is logisch\" not \"het maakt zin\")."
---

# Localize: Dutch (nl → Nederlands)

Distilled from the production translation prompts and the West Germanic localization stack. Follow these rules verbatim — they produce consistent, native-quality Dutch output across `nl-NL`, `nl-BE`, and Caribbean Dutch contexts.

## Mindset

> Je bent een uiterst veeleisende Nederlandse schrijver die een hekel heeft aan onnatuurlijke constructies, zoals letterlijke vertalingen uit het Engels of onhandige formuleringen.

You are a demanding Dutch native who rejects literal English calques and stiff phrasing. Preserve meaning, but restructure for natural Dutch. Well-established English loanwords (account, dashboard, app, email, download, upload) are acceptable when conjugated/integrated into Dutch (downloaden, geüpload, gemaild) — but Dutch verbs are preferred where they exist (verwijderen over deleten, opslaan over saven).

## Scope & Variants

This skill covers **Standard Dutch (nl / Nederlands / ABN — Algemeen Beschaafd Nederlands)** as written and spoken in:

| Variant | Region | Notes |
|---------|--------|-------|
| **nl-NL** | Netherlands | **DEFAULT for this skill.** ~17M speakers. Modern, direct, "je" is overwhelmingly the UI default. |
| **nl-BE** | Belgium (Flanders / Vlaanderen) | ~6.5M speakers. Same written standard but distinct lexical preferences (gsm/mobiel, aanmelden/inloggen). More formal register — "u" is more common in business than in NL. |
| **nl-SR** | Suriname | Dutch is the official language. Closer to nl-NL than nl-BE, with Surinamese loanwords. |
| **nl-CW / nl-AW / nl-SX** | Curaçao / Aruba / Sint Maarten | Dutch is co-official alongside Papiamento/English. Use nl-NL standard. |

### Variant Selection (run FIRST if user mentions BE/Flemish)

**Default behaviour:** assume `nl-NL` unless the source text or user mentions Belgium, Flanders, Vlaanderen, Brussels, België, or shows BE-specific cues (gsm, aanmelden, microgolfoven).

**If the user explicitly mentions Belgium or Flanders**, call `AskUserQuestion` before translating:

- Question: `Which Dutch variant should I target?`
- Header: `NL variant`
- Options:
  1. **Netherlands Standard Dutch (nl-NL)** — Default. "je/jij" register, inloggen, mobiel, magnetron. (Recommended for most software/marketing.)
  2. **Belgian Dutch / Flemish (nl-BE)** — "u" more common, aanmelden, gsm, microgolfoven. More formal default register.

**If the user picks nl-BE**, apply these deltas on top of the standard rules:

- **Register default:** lean toward **u** rather than **je** for business/professional UI. "je" is still acceptable for consumer apps but feels less common than in NL.
- **Vocabulary deltas** (use Flemish form in BE context):

  | English | nl-NL | nl-BE (Flemish) |
  |---------|-------|-----------------|
  | log in | **inloggen** | **aanmelden** |
  | log out | **uitloggen** | **afmelden** |
  | mobile phone | **mobiel / mobieltje** | **gsm** |
  | microwave | **magnetron** | **microgolfoven** |
  | bag | **tas** | **zak / tas** |
  | sandwich (filled) | **boterham / broodje** | **boterham / tartine** |
  | French fries | **frieten / patat** | **frieten / friet** |
  | "you" (plural informal) | **jullie** | **jullie / gij** (colloq.) |
  | downstairs / ground floor | **begane grond** | **gelijkvloers** |
  | breakfast | **ontbijt** | **ontbijt** (same) |
  | dishwasher | **vaatwasser / afwasmachine** | **vaatwas / afwasmachine** |
  | wallet | **portemonnee** | **portefeuille** |

- **Spelling:** identical to nl-NL — same Taalunie orthography rules apply since the 1995 spelling reform.
- **Number / date / currency formats:** identical to nl-NL (1.234,56 — EUR — DD-MM-YYYY).
- **Quotes, comma rules, V2 word order, de/het genders, diminutive system:** unchanged.
- **Time:** BE more often uses `14u30` colloquially, but `14:30` and `14.30` are both standard written forms in both variants.

Everything else — 2 genders, V2 word order, separable verbs, comma rules, diminutives, lowercase months — applies unchanged from nl-NL.

If the user picks nl-NL (or didn't mention BE/Flanders), skip the deltas and use the full skill below as-is.

## Identity Guardrail

Dutch is **West Germanic** — closest living relatives are Frisian, Low German dialects, and **German**. Despite the proximity, Dutch is NOT a German dialect and NOT Afrikaans:

| Feature | Dutch | German | Afrikaans |
|---------|-------|--------|-----------|
| Genders | **2** (de / het) | 3 (der / die / das) | **0** (no gender) |
| Cases | **0** (lost) | 4 (Nom/Acc/Dat/Gen) | 0 |
| Verb conjugation | -t/-en endings, simple | -e/-st/-t/-en/-t/-en | invariable (loop loop loop) |
| V2 word order | Yes (less rigid than DE) | Yes (strict) | Yes |
| Definite article | de / het | der / die / das | die (only) |
| Past participle prefix | ge- (with exceptions) | ge- (with exceptions) | ge- (with exceptions) |
| Verb-final in subord. | Yes | Yes (stricter) | No (SVO) |
| Spelling: ice | **ijs** | Eis | ys |
| Spelling: out | **uit** | aus | uit |
| Spelling: time | **tijd** | Zeit | tyd |
| Noun capitalization | NO (only proper nouns) | YES (all nouns) | NO |
| Double negation | NO | NO | YES (Afrikaans: "nie ... nie") |

**Common cross-language errors to avoid:**

- ❌ Capitalizing nouns like German: `het Huis`, `de Computer` → ✅ `het huis`, `de computer`
- ❌ Three genders: introducing `*den` or `*dem` articles (don't exist in Dutch)
- ❌ German spelling drift: `*zeit`, `*ein` (for "a"), `*haus` → ✅ `tijd`, `een`, `huis`
- ❌ Afrikaans simplification: `*ek loop` (Afrikaans for "I walk") → ✅ `ik loop`
- ❌ Treating Dutch as just "easier German" — different gender system, different word distribution, no case marking

Dutch has its OWN ~1500 years of evolution from Low Franconian. Respect it.

## Pre-Translation Setup

Lock in before translating:

1. **Variant** — nl-NL (default) or nl-BE (if user signalled Flanders).
2. **Formality (je vs u)** — Default to **je / jij** for modern Dutch UI (`nl-NL`). Default to **u** for `nl-BE` or formal/financial/legal contexts. NEVER mix within a file.
3. **Two genders** — Every noun is either **de-word** (common — historical masc + fem merged) or **het-word** (neuter). Diminutives (-je, -tje, -pje, -kje) are ALWAYS het. Plurals are ALWAYS de.
4. **V2 word order** in main clauses, **verb-final** in subordinate clauses (dat, omdat, wanneer, als, terwijl, hoewel, zodat).
5. **No cases** — Unlike German, no Nominative/Accusative/Dative declension on nouns or articles. (A few fossilized expressions remain: "in naam der wet", "ter beschikking", but these are not productive.)
6. **Placeholders** — Preserve `{variables}` and ICU plural syntax exactly. Restructure around them if needed to avoid de/het ambiguity.

## Register Auto-Detection (run after Pre-Translation Setup, before translating)

If the user has NOT explicitly specified je or u, infer from source register. Match output to source.

### Formal source signals → output u / uw / u (object)
- Polite modals: "please", "kindly", "we recommend", "could you", "would you mind"
- Passive / impersonal constructions: "users are advised", "applicants must", "it is recommended"
- No contractions: "do not", "cannot", "we will"
- Domain vocabulary: legal, financial, healthcare, insurance, government, enterprise B2B, automotive
- Third-person distance: "the user must", "customers should", "members can"
- Brand voice: bank, insurance, government, B2B SaaS, healthcare, premium retail
- Belgian/Flemish source (default lean toward u)

### Informal source signals → output je / jij / jouw
- Contractions: "don't", "you'll", "it's", "we're", "I'd"
- Casual greetings: "hey", "hi there", "what's up", "hi 👋"
- Exclamations and emoji (🎉 😎 🚀 ✨)
- Slang: "cool", "awesome", "no worries"
- Consumer-app voice: gaming, social, lifestyle, dating, fitness, food delivery, kids
- Sentence fragments, conversational filler
- Dutch consumer apps (Bol.com, Coolblue tone — all use je)

### Mixed / ambiguous source → default to **je** for nl-NL, **u** for nl-BE
For nl-NL: "je" is the modern default in 80% of Dutch software. Reads warm but professional. Most B2B SaaS in NL uses je (Mollie, Adyen marketing UI, Booking.com).
For nl-BE: "u" reads as default-professional and "je" can read as slightly casual in business contexts.

### Explicit user override
If the user says "use je" / "use u" / "formal" / "informal", their instruction overrides auto-detection.

### Worked examples

| Source | Detected | Dutch output (nl-NL) | Dutch output (nl-BE) |
|--------|----------|----------------------|----------------------|
| "Please review the terms of service before proceeding." | formal | Lees de algemene voorwaarden door voordat u verdergaat. | Lees de algemene voorwaarden door voordat u verdergaat. |
| "Hey! Tap here to get started — it's super quick 🚀" | informal | Hey! Tik hier om te beginnen — gaat supersnel 🚀 | Hey! Tik hier om te beginnen — gaat supersnel 🚀 |
| "Submit your application by the deadline." | formal | Dien je sollicitatie in vóór de deadline. *(consumer-job NL)* / Dien uw aanvraag in vóór de deadline. *(formal)* | Dien uw aanvraag in vóór de deadline. |
| "Don't forget to save your work!" | informal | Vergeet niet je werk op te slaan! | Vergeet niet uw werk op te slaan! |

After detection: keep the chosen form consistent. NEVER mix pronouns, possessives, OR imperatives.

## Register (je / jij / u — full forms)

### je-form (informal) — DEFAULT for nl-NL UI

| Function | Form |
|----------|------|
| Subject pronoun (unstressed) | **je** |
| Subject pronoun (stressed/emphatic) | **jij** |
| Object pronoun (unstressed) | **je** |
| Object pronoun (stressed) | **jou** |
| Possessive (unstressed) | **je** |
| Possessive (stressed) | **jouw** |
| Reflexive | **je** |
| Plural ("you all") | **jullie** (subject + possessive + object) |

Examples:
- `Je kunt je instellingen wijzigen.` (You can change your settings.)
- `Heb jij jouw bestand opgeslagen?` (Did YOU save YOUR file? — emphatic)
- `Welkom! Voer je e-mailadres in.` (Welcome! Enter your email.)
- `Jullie kunnen je werk delen.` (You all can share your work.)

### u-form (formal) — DEFAULT for nl-BE, formal contexts in nl-NL

| Function | Form |
|----------|------|
| Subject pronoun | **u** |
| Object pronoun | **u** |
| Possessive | **uw** |
| Reflexive | **u / zich** (both accepted; "zich" feels more formal-written) |
| Plural ("you all") | **u** (or restructure with "iedereen") |

Examples:
- `U kunt uw instellingen wijzigen.` (You can change your settings.)
- `Welkom! Voer uw e-mailadres in.`
- `Heeft u uw bestand opgeslagen?` (Note: u takes 3rd-person verb conjugation — `heeft`, not `hebt`. Both are accepted, but `heeft` is more formal.)

### Jij Inversion Rule — t-drop

When `jij` (or `je`) appears AFTER the verb (in inversion or questions), the -t ending DROPS:

| Statement | Inversion / Question |
|-----------|----------------------|
| Jij werkt hier. | **Werk** jij hier? *(NOT Werkt jij)* |
| Je slaat het bestand op. | **Sla** je het bestand op? *(NOT Slaat je)* |
| Je kunt verdergaan. | **Kun** je verdergaan? *(or "Kan je"; both accepted)* |

This rule applies ONLY to jij/je. Other pronouns keep -t (`Werkt hij?` `Werkt u?`).

### Mixed-register errors (CRITICAL — auto-fail)

| Wrong | Correct |
|-------|---------|
| U kunt **je** instellingen wijzigen. | U kunt **uw** instellingen wijzigen. |
| Voer je e-mailadres in. ... Klik vervolgens op de knop om door te gaan, **uw** wachtwoord ... | Voer **je** e-mailadres in. ... Klik vervolgens op de knop om door te gaan, **je** wachtwoord ... |
| Upload uw bestanden + **Klik hier** + Vergeet niet **je werk** op te slaan | Pick ONE register and apply throughout |

**Infinitive button forms** (`Opslaan`, `Verwijderen`, `Annuleren`) work with EITHER register — that's why they're the safest UI default.

## Critical Hard Rules

### 1. de / het — the #1 source of bugs (severity 2.0)

Dutch has TWO grammatical genders that determine the article:

- **de-words** (common gender, ~75% of nouns): historical masculine + feminine merged. Article: `de` in singular, `de` in plural.
- **het-words** (neuter, ~25% of nouns): Article: `het` in singular, `de` in plural.
- **All plurals use `de`** regardless of singular gender. `het bestand` → `de bestanden`. `het kind` → `de kinderen`.

You CANNOT reliably predict gender from the noun's meaning — you have to memorize. The most common errors in software UI:

#### High-frequency het-words (memorize)

| het-word | English | Common error |
|----------|---------|--------------|
| **het bestand** | the file | ❌ *de bestand* |
| **het systeem** | the system | ❌ *de systeem* |
| **het probleem** | the problem | ❌ *de probleem* |
| **het account** | the account *(usually het; "de account" exists in some BE usage)* | ❌ *de account* (in nl-NL) |
| **het wachtwoord** | the password | ❌ *de wachtwoord* |
| **het scherm** | the screen | ❌ *de scherm* |
| **het venster** | the window | ❌ *de venster* |
| **het veld** | the field | ❌ *de veld* |
| **het overzicht** | the overview / dashboard | ❌ *de overzicht* |
| **het netwerk** | the network | ❌ *de netwerk* |
| **het apparaat** | the device | ❌ *de apparaat* |
| **het pictogram** | the icon | ❌ *de pictogram* |
| **het menu** | the menu | ❌ *de menu* |
| **het formulier** | the form | ❌ *de formulier* |
| **het rapport** | the report | ❌ *de rapport* |
| **het tabblad** | the tab | ❌ *de tabblad* |
| **het bericht** | the message | ❌ *de bericht* |
| **het project** | the project | ❌ *de project* |
| **het document** | the document | ❌ *de document* |
| **het wachtwoord** | the password | ❌ *de wachtwoord* |
| **het beeld / het plaatje** | the image | ❌ *de beeld* |
| **het pad** | the path | ❌ *de pad* |
| **het abonnement** | the subscription | ❌ *de abonnement* |
| **het profiel** | the profile | ❌ *de profiel* |
| **het kind** | the child | ❌ *de kind* (`de kinderen` plural!) |
| **het meisje** | the girl *(diminutive → het)* | ❌ *de meisje* |

#### High-frequency de-words (memorize)

| de-word | English | Common error |
|---------|---------|--------------|
| **de map** | the folder | ❌ *het map* |
| **de gebruiker** | the user | ❌ *het gebruiker* |
| **de computer** | the computer | ❌ *het computer* |
| **de service** | the service | ❌ *het service* |
| **de server** | the server | ❌ *het server* |
| **de pagina** | the page | ❌ *het pagina* |
| **de link** | the link | ❌ *het link* |
| **de URL** | the URL | ❌ *het URL* |
| **de app** | the app | ❌ *het app* |
| **de plug-in** | the plug-in | ❌ *het plug-in* |
| **de website** | the website | ❌ *het website* |
| **de browser** | the browser | ❌ *het browser* |
| **de instelling** | the setting | ❌ *het instelling* |
| **de e-mail** | the email | ❌ *het e-mail* |
| **de melding / de notificatie** | the notification | ❌ *het melding* |
| **de knop** | the button | ❌ *het knop* |
| **de balk** | the bar (toolbar etc.) | ❌ *het balk* |
| **de tekst** | the text | ❌ *het tekst* |
| **de vraag** | the question | ❌ *het vraag* |
| **de fout / de foutmelding** | the error | ❌ *het fout* |
| **de gebruikersnaam** | the username | ❌ *het gebruikersnaam* |
| **de naam** | the name | ❌ *het naam* |
| **de taal** | the language | ❌ *het taal* |
| **de status** | the status | ❌ *het status* |
| **de versie** | the version | ❌ *het versie* |
| **de tabel** | the table | ❌ *het tabel* |
| **de afbeelding** | the image | ❌ *het afbeelding* |
| **de datum** | the date | ❌ *het datum* (yes, even though it ends like a het-word) |

#### Heuristics (not perfect — verify each noun)

- Diminutives (-je, -tje, -pje, -kje) → **always het**. Even when the base noun is de-: `de tafel → het tafeltje`, `de computer → het computertje`, `de man → het mannetje`.
- Verbal nouns ending in -en used as noun → **het**: `het lopen` (walking), `het opslaan` (saving — when used as noun).
- Most loanwords from Latin/Greek ending in -isme, -ment, -aat, -eum, -ium → **het**: `het racisme`, `het document`, `het apparaat`, `het museum`, `het stadium`.
- Most nouns ending in -ing, -heid, -ij, -teit, -ie, -tie, -nis, -st (after stem) → **de**: `de werking`, `de mogelijkheid`, `de bakkerij`, `de kwaliteit`, `de natie`, `de informatie`, `de geschiedenis`, `de winst`.
- When in doubt, look it up. Don't guess.

### 2. Adjective endings — strong vs weak (-e or no -e)

Dutch adjective endings depend on **definiteness + gender + plurality**.

| Context | Pattern | Example |
|---------|---------|---------|
| **Definite (de/het) + adjective** — both genders | adjective + **-e** | de **grote** computer, het **grote** systeem, de **grote** systemen |
| **Indefinite (een) + de-word + adjective** | adjective + **-e** | een **grote** computer |
| **Indefinite (een) + het-word + adjective** | adjective + **NO -e** | een **groot** systeem ⚠ |
| **No article + plural** | adjective + **-e** | **grote** systemen |
| **No article + het-word singular** | adjective + **NO -e** (predicative-ish) | **groot** systeem (rare in UI; predicative `Het systeem is groot`) |
| **Predicative** (`is X`) | adjective + **NO -e** | Het systeem is **groot**. De computer is **groot**. |

| Wrong | Correct | Reason |
|-------|---------|--------|
| een **grote** probleem | een **groot** probleem | indef + het-word → no -e |
| een **groot** computer | een **grote** computer | indef + de-word → -e |
| het **groot** systeem | het **grote** systeem | definite → always -e |
| de **belangrijk** instellingen | de **belangrijke** instellingen | plural → always -e |
| nieuw **ervaring** | **nieuwe** ervaring | (after de implied) — `de nieuwe ervaring` / `een nieuwe ervaring` |
| een **nieuw** account *(het-word)* | een **nieuw** account | (correct — indef + het = no -e) |

Materials adjectives (`gouden`, `houten`, `glazen`, `zilveren`) and ordinal numerals (`eerste`, `tweede`) always end in -e/-en and don't follow the strong/weak rule.

### 3. V2 Word Order — finite verb is the SECOND element in main clauses

Like German, Dutch is V2: the finite (conjugated) verb is the **second constituent** in a main clause. The "first constituent" can be the subject, an adverb, a time expression, an object — anything — but exactly ONE thing before the verb.

| Pattern | Example |
|---------|---------|
| Subject first | **Ik** **koop** een boek. *(I buy a book.)* |
| Time-adverb first → subject moves after verb | **Vandaag** **koop** ik een boek. *(Today buy I a book = Today I buy a book.)* |
| Object first (emphatic) | **Een boek** **koop** ik vandaag. *(A book I'm buying today.)* |
| Prepositional phrase first | **In de map** **vind** je het bestand. *(In the folder you find the file.)* |

| Wrong | Correct |
|-------|---------|
| Vandaag de gebruiker slaat op het bestand. | Vandaag **slaat** de gebruiker het bestand op. |
| Daarna je klikt op de knop. | Daarna **klik** je op de knop. |
| Eerst het systeem laadt. | Eerst **laadt** het systeem. |
| In dit menu je kunt opslaan. | In dit menu **kun** je opslaan. |

### 4. Verb-final in subordinate clauses

After subordinating conjunctions — **dat, omdat, wanneer, als, terwijl, hoewel, zodat, voordat, nadat, sinds, zodra, totdat, of (whether)** — the conjugated verb goes to the END of the clause.

| Wrong | Correct |
|-------|---------|
| ...omdat de gebruiker **slaat** op het bestand. | ...omdat de gebruiker het bestand **opslaat**. |
| ...dat het systeem **heeft** geladen. | ...dat het systeem **geladen heeft / heeft geladen**. *(both orders accepted; "geladen heeft" is more traditional, "heeft geladen" is the auxiliary-first variant — both fine)* |
| ...als je **klikt** hier. | ...als je hier **klikt**. |
| ...terwijl het bestand **wordt** geüpload. | ...terwijl het bestand **geüpload wordt / wordt geüpload**. |

This is the SINGLE most common Dutch grammar error from English speakers — keep the verb at the end in subordinate clauses.

### 5. Separable verbs — prefix splits in main clauses

Dutch has many separable verbs: a prefix + main verb that LOOK like one word in the infinitive but SPLIT in main clauses (the prefix goes to the END).

| Infinitive | Main clause (split) | Subordinate (rejoined) | English |
|-----------|---------------------|------------------------|---------|
| **opslaan** | Ik **sla** het bestand **op**. | ...omdat ik het bestand **opsla**. | to save |
| **uitloggen** | Je **logt** **uit**. | ...als je **uitlogt**. | to log out |
| **inloggen** | Ik **log** **in**. | ...wanneer ik **inlog**. | to log in |
| **opladen** | De telefoon **laadt** **op**. | ...terwijl de telefoon **oplaadt**. | to charge |
| **uitschakelen** | Schakel het **uit**. | ...zodat je het **uitschakelt**. | to turn off |
| **terugkomen** | Ik **kom** zo **terug**. | ...wanneer ik **terugkom**. | to come back |
| **doorgaan** | Ga je **door**? | ...als je **doorgaat**. | to continue |
| **uitloggen** | Je **logt** je nu **uit**. | ...nadat je je **uitlogt**. | to log out |
| **afmelden** | Meld je **af**. | ...als je je **afmeldt**. | to unsubscribe / log out |
| **bijwerken** | Werk de app **bij**. | ...wanneer je de app **bijwerkt**. | to update |
| **downloaden** *(NOT separable!)* | Ik **download** het bestand. | ...omdat ik het bestand **download**. | to download |
| **uploaden** *(NOT separable!)* | Ik **upload** het bestand. | ...omdat ik het bestand **upload**. | to upload |

⚠ **English-origin verbs (downloaden, uploaden, updaten, googlen, mailen, appen) are NOT separable** — they don't split. They conjugate as single units. This is a frequent error.

| Wrong | Correct |
|-------|---------|
| Ik **opsla** het bestand. | Ik **sla** het bestand **op**. |
| Je **uitlogt** nu. | Je **logt** nu **uit**. |
| Ik **download** **uit** het bestand. *(nonsense — not separable)* | Ik **download** het bestand. |
| Ik **upload** **op** het bestand. | Ik **upload** het bestand. |
| ...omdat hij **sla** het bestand **op**. *(splitting in subord clause — wrong)* | ...omdat hij het bestand **opslaat**. |

### 6. Past participle — ge- prefix and its exceptions

Standard past participle pattern: **ge-** + stem + **-d/-t/-en**.

| Verb | Past participle |
|------|----------------|
| werken (weak) | **gewerkt** |
| maken (weak) | **gemaakt** |
| opslaan (strong, separable) | **opgeslagen** *(ge- inserted between prefix and stem)* |
| uitloggen (weak, separable) | **uitgelogd** |
| downloaden (weak, English origin) | **gedownload** *(ge- + stem; final -d not double)* |
| uploaden | **geüpload** *(trema on ü — see spelling section)* |
| updaten | **geüpdatet** |
| mailen | **gemaild** |
| googlen | **gegoogeld** |
| appen | **geappt** |

**Exception — NO ge- prefix when the verb starts with these unstressed prefixes:**

- **be-** (begrijpen → **begrepen** NOT *begregrepen, *gebegrepen)
- **ge-** (gebeuren → **gebeurd** — the ge- is already there)
- **ver-** (verkopen → **verkocht**, verbergen → **verborgen**)
- **ont-** (ontdekken → **ontdekt**, ontvangen → **ontvangen**)
- **er-** (ervaren → **ervaren**, erkennen → **erkend**)
- **her-** (herhalen → **herhaald**, herstellen → **hersteld**)

| Wrong | Correct |
|-------|---------|
| **gebegrepen** | **begrepen** |
| **geverkocht** | **verkocht** |
| **geontdekt** | **ontdekt** |
| **geherhaald** | **herhaald** |
| **geupload** *(no trema)* | **geüpload** |

### 7. IJ — ONE letter, capitalized as IJ

Dutch `ij` (yes the digraph) is treated as a single letter in:
- **Capitalization**: at the start of a sentence or proper noun, BOTH letters capitalize: **IJsland** (Iceland), **IJ** (the river in Amsterdam), **IJmuiden** (city). NOT *Ijsland.
- **Sorting**: traditionally sorted as if it were "y", but modern dictionaries sort as `i` + `j` separately.
- **Hyphenation**: never break between i and j.

Common ij words in UI/tech: tijd, schrijven, vrij, bijvoorbeeld (bv.), bijwerken, mijn, zijn, krijgen, blijven, kijken, vergelijken, beschikbaar, gelijk, terwijl, mogelijk.

| Wrong | Correct |
|-------|---------|
| **Ijsland** | **IJsland** |
| **Ij-rivier** | **IJ-rivier** |
| breken tussen `wij-d` → wi-jd | hyphenate `wijd` only between syllables, never split ij |

### 8. Diminutive system — productive, always neuter (het)

Dutch has a hyper-productive diminutive suffix that:
1. Makes a noun smaller, cuter, or less formal
2. Sometimes changes meaning entirely (`het meisje` "girl" is the diminutive of `de meid`)
3. **ALWAYS makes the resulting noun het-neuter**, regardless of base gender
4. **ALWAYS has a plural in -s**, NEVER -en: `het huisje → de huisjes`

| Base noun | Diminutive | Plural |
|-----------|-----------|--------|
| de tafel (table) | **het tafeltje** | de tafeltjes |
| het huis (house) | **het huisje** | de huisjes |
| de computer | **het computertje** | de computertjes |
| de man (man) | **het mannetje** | de mannetjes |
| de boek → het boek (book) | **het boekje** *(booklet)* | de boekjes |
| de kop (cup) | **het kopje** *(little cup)* | de kopjes |
| de mobiel | **het mobieltje** *(=cellphone, common in nl-NL!)* | de mobieltjes |
| de bel (bell) | **het belletje** *(also: a quick phone call)* | de belletjes |
| de week | **het weekje** *(a little week, ~1 week)* | de weekjes |

**Suffix variants** (depend on the final sound of the base):
- **-je** (after most consonants ending in voiceless or sibilant): boek → boekje, fiets → fietsje, zak → zakje
- **-tje** (after long vowels, diphthongs, /l/, /n/, /r/, /w/): tafel → tafeltje, schoen → schoentje, deur → deurtje, bui → buitje
- **-pje** (after /m/): boom → boompje, bezem → bezempje, arm → armpje
- **-kje** (after /ŋ/ — words ending in -ing): koning → koninkje, woning → woninkje
- **-etje** (after short vowel + /l/, /n/, /r/, /m/, /ŋ/ where consonant doubles): bal → balletje, kar → karretje, man → mannetje, kam → kammetje

Even in formal UI, diminutives carry connotation. `Een berichtje` (a little message) is warmer than `een bericht`. Use sparingly in business UI; use freely in consumer warmth.

### 9. No noun capitalization (UNLIKE German)

This is the #1 cross-language error from German speakers. In Dutch:

- **Only proper nouns and sentence-initial words** are capitalized.
- Common nouns are **lowercase**: het huis, de computer, de gebruiker, het bestand.
- Days, months, languages, nationalities (adjective form) → **lowercase**.
- BUT nationalities used as nouns referring to people → some style guides capitalize: `een Nederlander` (a Dutch person) — Taalunie allows both `Nederlander` and `nederlander`; the capitalized form is more common.

| Wrong (German-influenced) | Correct |
|---------------------------|---------|
| Het Huis is groot. | Het **huis** is groot. |
| De Gebruiker logt in. | De **gebruiker** logt in. |
| Op Maandag | op **maandag** |
| in Januari | in **januari** |
| Ik spreek Engels en Frans. | Ik spreek **Engels** en **Frans**. *(languages: cap — they ARE proper nouns)* |
| een Nederlandse computer | een **Nederlandse** computer *(nationality adjective: cap, because derived from country name Nederland)* |

⚠ Nuance: **Languages and nationality-derived adjectives ARE capitalized** (`Nederlands`, `Engels`, `Frans`, `Duits`, `Spaans`) because they derive from country/people names. But days (`maandag`), months (`januari`), and common nouns are NOT.

### 10. Compound nouns — write as ONE word

Dutch, like German, builds compound nouns by glueing nouns together. Always one word (or with a linking element). Use a hyphen only for clarity in specific cases (see below).

| Wrong (split) | Correct (compound) |
|---------------|---------------------|
| data base | **database** *(de database)* |
| gebruikers interface | **gebruikersinterface** *(linking -s-, de gebruikersinterface)* |
| project ordner | **projectmap** *(de projectmap)* |
| huis deur | **huisdeur** *(de huisdeur)* |
| veiligheids instellingen | **veiligheidsinstellingen** *(linking -s-)* |
| zoek resultaten | **zoekresultaten** *(de zoekresultaten)* |
| log bestand | **logbestand** *(het logbestand)* |
| inkomst belasting | **inkomstenbelasting** *(linking -en-)* |

**Linking elements** (-s- or -en-) appear between the parts in many compounds. Some rules:
- **-s-** when first noun naturally has -s- in its genitive feel: dorpsschool, jeugdsraad, gebruikersinterface, projectsmanagement *(rare)*
- **-en-** when first noun has plural in -en that makes sense in compound: pannenkoek, boekenkast, mannenkleding, vrouwenkleding
- **No linking element** for many compounds: huisdeur, autosleutel, computerprobleem

**Use a hyphen when**:
- The compound has 3+ parts and would be unclear: `wifi-wachtwoord-reset`
- The first part ends in a vowel and joining would create an ambiguous reading: `auto-industrie`, `radio-uitzending`
- Compounding a proper noun: `OneSky-API`, `Google-zoekopdracht`
- One element is an acronym/initialism: `API-sleutel`, `URL-balk`, `pdf-bestand` (note: pdf is lowercased; `pdf-bestand` is preferred over `PDF-bestand`)
- Two of the same vowel meet across a join: `na-apen`, `zee-eend`

**Gender of compounds** follows the LAST element: `de map + het bestand` → `het mapbestand`? No, the compound is `het bestand uit de map` → in compounds, the gender follows the LAST noun: `huisdeur` ends in `deur` (de) → `de huisdeur`. `logbestand` ends in `bestand` (het) → `het logbestand`.

### 11. FOR vs PER — distinct words, different uses

| English | Dutch | Use |
|---------|-------|-----|
| for 5 languages (total / for the benefit of) | **voor 5 talen** | total scope |
| per language (rate) | **per taal** | per-unit rate |
| per month | **per maand** | rate |
| for 30 days (duration) | **gedurende 30 dagen / 30 dagen lang** | duration |

| Wrong | Correct |
|-------|---------|
| `pro Sprache` (German calque) | **per taal** |
| `voor taal` (when meaning "per taal") | **per taal** |
| **5 talen voor maand** | **5 talen per maand** |

### 12. Domain terminology — use IT/software meanings

| Source | Wrong (general meaning) | Correct (IT meaning) |
|--------|-------------------------|----------------------|
| architecture (software) | bouwkunst, gebouw | **architectuur (software-architectuur)** |
| pipeline (CI/CD) | leiding, buis | **pipeline / CI/CD-pipeline** |
| source of truth | bron van waarheid *(too literal)* | **gezaghebbende databron / single source of truth** *(English term often accepted in tech)* |
| build (software) | bouw, constructie | **bouwen / maken / compileren** |
| deploy (software) | uitrollen *(this one works)* | **uitrollen / implementeren / deployen** *(English form accepted in tech)* |
| support (feature) | ondersteunen *(this one works — natural Dutch)* | **ondersteunen** ✓ |
| commit (git) | toezeggen *(wrong domain)* | **committen / een commit doen** |
| branch (git) | tak *(works) / branch (English form)* | **branch / vertakking** |
| repository (git) | opslagplaats / repo | **repository / repo** |
| dashboard | bedieningspaneel *(too literal)* | **dashboard / overzicht** ✓ |
| backend / frontend | achterkant / voorkant *(too literal)* | **backend / frontend** ✓ |

Software jargon is increasingly accepted in Dutch as-is. When the source is technical, the English term is often more natural than a forced Dutch calque.

## UI Conventions

### Buttons — INFINITIVE form

Like German, Dutch UI buttons use the infinitive (the -en form), NOT the imperative.

| Wrong | Correct |
|-------|---------|
| Sla op *(imperative)* | **Opslaan** |
| Slaat op *(present-tense)* | **Opslaan** |
| Opslag *(nominalization)* | **Opslaan** |
| Verwijder *(imperative)* | **Verwijderen** |
| Klik *(imperative)* | **Klikken** *(or restructure to action)* |
| Annuleer *(imperative)* | **Annuleren** |
| Doorgaan ✓ | (correct — infinitive of doorgaan) |

Standard infinitive buttons:

| English | Dutch button |
|---------|--------------|
| Save | **Opslaan** |
| Cancel | **Annuleren** |
| Delete | **Verwijderen** |
| Edit | **Bewerken** |
| Add | **Toevoegen** |
| Remove | **Verwijderen** |
| Upload | **Uploaden** |
| Download | **Downloaden** |
| Submit | **Verzenden** |
| Send | **Verzenden** |
| Continue / Next | **Doorgaan / Volgende** |
| Back / Previous | **Terug / Vorige** |
| Close | **Sluiten** |
| Open | **Openen** |
| Confirm | **Bevestigen** |
| Search | **Zoeken** |
| Sign in / Log in | **Inloggen** (nl-NL) / **Aanmelden** (nl-BE) |
| Sign up / Register | **Registreren / Aanmelden** |
| Log out | **Uitloggen** (nl-NL) / **Afmelden** (nl-BE) |
| Refresh / Reload | **Vernieuwen / Opnieuw laden** |
| Settings | **Instellingen** |
| Try again / Retry | **Opnieuw proberen** |
| Skip | **Overslaan** |
| Reset | **Resetten / Opnieuw instellen** |

### Status messages

| State | Form | Example |
|-------|------|---------|
| Ongoing | `Wordt X...` *(passive present)* or `Bezig met X...` or `X...` *(English-style)* | `Wordt geladen...`, `Bezig met opslaan...`, `Laden...`, `Bezig met uploaden...` |
| Completed | Past participle | `Opgeslagen`, `Geüpload`, `Verzonden`, `Succesvol opgeslagen` |
| Failed | `Fout bij X` or `X mislukt` | `Fout bij opslaan`, `Opslaan mislukt`, `Uploaden mislukt` |

Avoid:
- ❌ `Ik laad...` (first-person — wrong register for UI)
- ❌ `We laden...` (also reads off — use passive)
- ❌ `Opslaan heeft gefaald` *(English-style calque)*
- ❌ `Bezig...` bare without specifying *(unclear)*

### Completion / success

| Wrong | Correct |
|-------|---------|
| Upload Succes | **Upload voltooid / Succesvol geüpload** |
| Proces compleet | **Proces voltooid / Voltooid** |
| Betaling succesvol | **Betaling voltooid / Betaling bevestigd** |
| Klaar | **Voltooid / Gereed** *("Klaar" is OK informally, but "Voltooid" is the standard in business UI)* |

### Empty states

| Wrong | Correct |
|-------|---------|
| Niet resultaten | **Geen resultaten / Geen resultaten gevonden** |
| Geen Bestand geselecteerd | **Geen bestand geselecteerd** *(lowercase!)* |
| Leeg | **Geen items / Geen items beschikbaar** |
| 0 berichten | **Nog geen berichten / Geen berichten** |

The negation `geen` is used with nouns; `niet` is used with verbs/adjectives. UI empty states almost always need `geen`.

### Drag and drop

| English | Dutch |
|---------|-------|
| drag | **slepen** |
| drop | **neerzetten / loslaten / plaatsen** |
| release | **loslaten** |
| drop here | **hier loslaten / hier neerzetten** |
| browse (file picker) | **bladeren / kiezen / selecteren** |
| select files | **bestanden selecteren / bestanden kiezen** |

| Wrong (anglicism) | Correct |
|-------------------|---------|
| Drag bestanden | **Sleep bestanden hierheen** |
| Drop hier | **Hier loslaten / Hier neerzetten** |
| Browse bestand | **Bestand selecteren / Bladeren** |
| Releasen | **Loslaten** |

### Validation messages

- Clear structure: `3-50 tekens. Toegestaan: letters, cijfers, koppeltekens.`
- Required field: `Dit veld is verplicht.` (NOT `Veld ontbreekt` — calque)
- Invalid format: `Ongeldige indeling / Ongeldig formaat.`
- Imperative for instructions in je-form: `Vul een geldige waarde in.`
- Imperative for instructions in u-form: `Vul een geldige waarde in.` *(same — infinitive imperative for both)*

### Error messages — what + next step

| Wrong (bare) | Correct (actionable) |
|--------------|----------------------|
| Bestand niet gevonden. | **Bestand niet gevonden. Controleer het pad.** |
| Fout opgetreden. | **Er is een fout opgetreden. Probeer het opnieuw.** |
| Verbinding mislukt. | **Verbinding mislukt. Controleer je internetverbinding.** |

### Other UI patterns

| Wrong | Correct |
|-------|---------|
| Geavanceerd *(bare)* | **Geavanceerde instellingen** *(complete noun phrase — also note: de geavanceerde — definite -e ending)* |
| Automatisch *(bare)* | **Automatische modus** |
| Alternatief *(bare)* | **Alternatieve detectie / Alternatieve methode** |
| 25+ talen | **meer dan 25 talen** |
| +{count} meer | **en {count} andere / nog {count} andere** |
| Meer toevoegen | **Nog meer toevoegen / Meer toevoegen** (both OK; "nog meer" is warmer) |
| Ondersteuning voor X-bestanden *(noun-focused)* | **Ondersteunt X-bestanden** *(capability-focused, active)* |
| Ondersteuning van meerdere talen | **Ondersteunt meerdere talen** |

### Placeholder gender ambiguity

When a placeholder might be a de-word OR a het-word, restructure to avoid `de/het {name}`:

| Wrong | Correct |
|-------|---------|
| Verwijder de/het {item}? | **{item} verwijderen?** *(use as proper-noun-style, no article)* |
| Verwijder de {item}? *(when {item} could be het-word)* | **Wil je {item} verwijderen?** *(no article)* |
| Welkom, de gebruiker {name}! | **Welkom, {name}!** |

## Punctuation, Numbers, Dates, Currency

### Numbers

- **Decimal separator: comma** — `3,14`, `0,5`, `99,99`
- **Thousands separator: period** — `1.000`, `10.000`, `1.234.567`
- Combined: `€ 1.234,56`, `€ 1.000.000,00`
- Negative: `-5,00` or `−5,00` *(true minus is rare; hyphen-minus is fine)*

| Wrong (English style) | Correct (Dutch) |
|----------------------|-----------------|
| 1,000.50 | **1.000,50** |
| 3.14 | **3,14** |
| 99.99 € | **€ 99,99** *(symbol before, space optional but common; also `€99,99` accepted)* |

### Dates

Dutch uses **hyphens** as the primary date separator, though slashes and dots are also accepted:

- **Numeric (preferred): DD-MM-YYYY** — `15-01-2024`, `01-12-2024`
- Numeric (also accepted): `15/01/2024`, `15.01.2024`
- **Long form: D maand YYYY** *(lowercase month!)* — `15 januari 2024`, `1 december 2024`
- Day of week: `maandag 15 januari 2024` *(lowercase day!)*
- Time: `14:30` or `14.30` *(both used; "uur" appended in formal: `14:30 uur` or `14 uur 30`)*

| Wrong | Correct |
|-------|---------|
| 01/15/2024 *(US format MDY)* | **15-01-2024** *(DMY)* |
| January 15, 2024 | **15 januari 2024** |
| Maandag 15 Januari 2024 *(capitalized day/month)* | **maandag 15 januari 2024** |
| 2:30 PM | **14:30 / 14.30** *(24-hour)* |
| 15-Jan-2024 | **15-01-2024 / 15 januari 2024** |

**Dutch months (LOWERCASE):**
januari, februari, maart, april, mei, juni, juli, augustus, september, oktober, november, december

**Dutch days (LOWERCASE):**
maandag, dinsdag, woensdag, donderdag, vrijdag, zaterdag, zondag

Week starts on **Monday** (maandag), as in most European countries.

### Currency

- **EUR (€)** since 2002, used in NL, BE, and most of the EU.
- **Format:** `€ 99,99` (symbol before with optional space) or `€99,99` (no space). Both accepted; space form is more traditional.
- Suriname: SRD (Surinamese dollar) — `SRD 99,99`. Caribbean Netherlands: USD (`US$ 99,99` or `$ 99,99`).
- ABN AMRO and most NL/BE banks display: `€ 1.234,56`
- No currency-after pattern (unlike German `99,99 €` — Dutch consistently puts symbol before, though `99,99 €` is sometimes seen in print)

| Wrong | Correct |
|-------|---------|
| €99.99 *(English decimal)* | **€ 99,99** |
| 99,99 EUR *(text after)* | **€ 99,99** *(symbol before)* |
| EUR 99,99 *(text first)* | **€ 99,99** *(or "99,99 euro" in prose)* |

### Quotation marks

- **Modern Dutch increasingly uses straight ASCII** `"..."` for software, web, and many publications.
- Traditional Dutch uses **`„..."`** (low-9 opening + high-6 closing — same as German) OR **`'...'`** (single curly quotes for nested/short quotes).
- All three are accepted; pick ONE per file and be consistent.
- Avoid `«...»` (French/Swiss style — not standard Dutch).
- Avoid `''...''` (English double-curly — not standard Dutch).

| Wrong | Correct |
|-------|---------|
| Hij zei: "Hallo." *(English curly)* | Hij zei: "Hallo." *(straight)* or Hij zei: „Hallo." |
| Klik op «Opslaan». | Klik op "Opslaan" / Klik op 'Opslaan'. |

### Apostrophes

- Used in possessives: `Anna's auto`, `Eva's project`, `de baby's` *(also for plurals ending in vowel)*
- Used in plurals after vowel: `baby's`, `taxi's`, `foto's`, `auto's`, `paragraaf 's avonds` *(time of day)*
- Used in elisions: `'s ochtends`, `'s avonds`, `'s middags`, `'s nachts`, `'t = het` (informal), `d'r = haar` (very informal)

### Comma rules

| Before | Comma? |
|--------|--------|
| **en / of** *(coordinating)* | **No comma** in standard Dutch usage |
| **maar / want** *(coordinating)* | **Comma** *(common but not strictly mandatory — strongly recommended)* |
| **dat / omdat / wanneer / als / hoewel / terwijl / zodat** *(subordinating — always start a subordinate clause)* | **Always comma** before |
| Between two main clauses joined by **en / of** with two distinct subjects | **Comma optional** (more common in longer sentences) |
| Listing items | **Comma between**, NO Oxford comma: `appels, peren en bananen` (NOT `appels, peren, en bananen`) |
| **omdat**, **want** when they introduce a reason | **Comma before omdat/want** *(want = coordinating, omdat = subordinating — both get comma)* |

| Wrong | Correct |
|-------|---------|
| Opslaan**,** en sluiten | Opslaan en sluiten |
| Ik werk hier maar het is moeilijk. | Ik werk hier**,** maar het is moeilijk. |
| Ik zie dat de datei groot is. | Ik zie**,** dat de datei groot is. *(Note: Dutch comma before subordinate is required in formal/written prose — the Taalunie official rule. Informal writing sometimes omits it.)* |
| appels**,** peren**,** en bananen *(Oxford comma)* | appels, peren en bananen |

### Punctuation around abbreviations

- Common abbreviations: bv. (bijvoorbeeld), nl. (namelijk), enz. (enzovoort), m.a.w. (met andere woorden), o.a. (onder andere), m.b.t. (met betrekking tot), t.o.v. (ten opzichte van).
- US/UK style of avoiding periods (eg → e.g.) is NOT Dutch; Dutch keeps the periods: **bv.**, **enz.**, **t.o.v.**

## Terminology

### Standard UI vocabulary

| English | Dutch (nl-NL) | Variant (nl-BE) |
|---------|---------------|-----------------|
| file | het bestand | het bestand |
| folder | de map | de map |
| save | opslaan | opslaan |
| delete | verwijderen | verwijderen |
| cancel | annuleren | annuleren |
| upload | uploaden | uploaden |
| download | downloaden | downloaden |
| settings | de instellingen | de instellingen |
| search | zoeken | zoeken |
| edit | bewerken | bewerken |
| copy | kopiëren | kopiëren |
| paste | plakken | plakken |
| close | sluiten | sluiten |
| open | openen | openen |
| log in | inloggen | **aanmelden** |
| log out | uitloggen | **afmelden** |
| sign up | aanmelden / registreren | registreren |
| user | de gebruiker | de gebruiker |
| account | het account | het account / de account (BE) |
| password | het wachtwoord | het wachtwoord |
| email | de e-mail | de e-mail |
| URL | de URL | de URL |
| link | de link | de link |
| message | het bericht | het bericht |
| notification | de melding / de notificatie | de melding / de notificatie |
| error | de fout / de foutmelding | de fout |
| dashboard | het dashboard / het overzicht | het dashboard |
| update | bijwerken / updaten | bijwerken / updaten |
| refresh | vernieuwen / opnieuw laden | vernieuwen |
| device | het apparaat | het toestel / het apparaat |
| screen | het scherm | het scherm |
| window | het venster | het venster |
| menu | het menu | het menu |
| icon | het pictogram / het icoon | het icoon |
| tab | het tabblad | het tabblad |
| browser | de browser | de browser |
| mobile | de mobiel / het mobieltje | de gsm |
| computer | de computer | de computer |
| keyboard | het toetsenbord | het toetsenbord / het klavier |
| mouse (computer) | de muis | de muis |
| support (feature) | ondersteunen / ondersteuning | ondersteunen |
| help | de hulp | de hulp |
| feedback | de feedback / de terugkoppeling | de feedback |

### Anglicism integration — Dutch loves English loans

Unlike French or German purists, Dutch readily integrates English loanwords. They get Dutch conjugation:

| English | Dutch verb | Past participle | Example |
|---------|-----------|----------------|---------|
| to download | downloaden | gedownload | Ik download het. / Ik heb het gedownload. |
| to upload | uploaden | geüpload | Ik upload het. / Ik heb het geüpload. |
| to update | updaten | geüpdatet | Ik update de app. / Ik heb de app geüpdatet. |
| to mail | mailen | gemaild | Ik mail je. / Ik heb je gemaild. |
| to google | googelen / googlen | gegoogeld | Ik google het. / Ik heb het gegoogeld. |
| to app (WhatsApp) | appen | geappt | Ik app je later. / Ik heb je geappt. |
| to like (social) | liken | geliket | Ik like het. / Ik heb het geliket. |
| to chatten | chatten | gechat | Ik chat met haar. / Ik heb gechat. |
| to scrollen | scrollen | gescrold | Ik scroll. / Ik heb gescrold. |
| to swipen | swipen | geswiped | Ik swipe. / Ik heb geswiped. |
| to printen | printen | geprint | Ik print het. / Ik heb het geprint. |

**BUT** — prefer Dutch verbs when they exist:

| Anglicism | Prefer Dutch |
|-----------|--------------|
| **deleten** | **verwijderen** |
| **cancelen** | **annuleren** |
| **saven** | **opslaan** |
| **editeren** | **bewerken** |

Some anglicisms have become so standard they're acceptable: `downloaden`, `uploaden`, `googlen`, `mailen`, `chatten`, `liken`, `appen`. These are fine in UI.

### Brand names

Foreign brand names typically take **het** for products/platforms or **de** for services/companies:

- het Google account *(or "je Google-account")*
- de OneSky-service / het OneSky-platform
- het WhatsApp-bericht / de WhatsApp-melding
- Genitive with `'s` for many foreign names: `Google's API`, `OneSky's instellingen`
- For Dutch genitives: just use a `van`-construction: `de API van Google`, `de instellingen van OneSky`.

### Proper nouns — short forms in UI

| Wrong (verbose) | Correct (UI) |
|-----------------|--------------|
| Verenigde Staten van Amerika | **VS / de VS / de Verenigde Staten** |
| Groot-Brittannië en Noord-Ierland | **het VK / Groot-Brittannië / VK** |
| Volksrepubliek China | **China** |
| Bondsrepubliek Duitsland | **Duitsland** |

| Country | Dutch name | Adjective | Language |
|---------|-----------|-----------|----------|
| Nederland | het Nederlands | Nederlands |
| België | het Belgisch | Belgisch *(but the language is Nederlands or Frans)* |
| Duitsland | het Duits | Duits |
| Frankrijk | het Frans | Frans |
| Verenigd Koninkrijk / VK | het Engels / Brits | Engels |
| Verenigde Staten / VS | het Amerikaans | Amerikaans (Engels) |
| Spanje | het Spaans | Spaans |
| Italië | het Italiaans | Italiaans |
| Japan | het Japans | Japans |
| China | het Chinees | Chinees |

## Calque / Anti-Pattern Blocklist

### Word-for-word English → Dutch traps

| English | Wrong (literal) | Correct (natural Dutch) |
|---------|-----------------|--------------------------|
| It makes sense | het maakt zin | **het is logisch / het slaat ergens op / het is zinvol / het is begrijpelijk** |
| At the end of the day | aan het einde van de dag | **uiteindelijk / per saldo / al met al** |
| Not really | niet echt | **eigenlijk niet / niet bepaald** *("niet echt" is borderline OK in casual speech but "eigenlijk niet" is more idiomatic)* |
| Take a look | neem een kijkje | **kijk eens / werp een blik** |
| Future-proof | toekomst-proof | **toekomstbestendig / klaar voor de toekomst** |
| Take advantage of | voordeel nemen van | **gebruikmaken van / profiteren van / benutten** |
| Based on | gebaseerd op *(this one's fine!)* | gebaseerd op ✓ |
| On a daily basis | op een dagelijkse basis | **dagelijks / elke dag** |
| In terms of (overused) | in termen van | **wat ... betreft / op het gebied van / qua** |
| Going forward | gaande voorwaarts | **voortaan / vanaf nu / in het vervolg** |
| Reach out (to contact) | bereik uit | **contact opnemen / contact zoeken** |
| Address (an issue) | adresseren *(rare and stiff)* | **aanpakken / behandelen** |
| Leverage (verb) | hefbomen *(absurd literal)* | **benutten / gebruikmaken van / inzetten** |
| Onboarding | aanboarding *(no)* | **onboarding** *(accepted English term)* or **introductie / inwerktraject** |
| Out of the box | uit de doos | **kant-en-klaar / standaard** |
| Streamline | stroomlijnen *(this one works!)* | stroomlijnen ✓ |
| Game changer | spel veranderaar | **doorbraak / keerpunt / gamechanger** |
| Low-hanging fruit | laag hangend fruit *(literal calque; spreading but stiff)* | **eenvoudige winst / makkelijke wins** |
| Best practice | beste praktijk | **beste werkwijze / best practice** *(English term accepted)* |
| Stakeholder | belanghebbende *(works)* | belanghebbende / stakeholder *(both fine)* |
| Deep dive | diepe duik | **uitgebreide analyse / diepgaande verkenning** |

### False friends — Dutch words that look like English but mean something else

| Dutch word | Actual meaning | NOT the English |
|-----------|---------------|------------------|
| **actueel** | **current / up-to-date** | NOT "actual" → use **eigenlijk / daadwerkelijk / werkelijk** |
| **eventueel** | **possibly / potentially** | NOT "eventually" → use **uiteindelijk / op den duur** |
| **sympathiek** | **likeable / nice** | NOT "sympathetic" → use **meelevend / begrijpend** |
| **brutaal** | **rude / cheeky** | NOT "brutal" → use **wreed / hardvochtig** |
| **slim** | **clever / smart** | NOT "slim" → use **slank / dun** |
| **boos** | **angry** | NOT "boss-like" → use **woedend** for stronger |
| **gift** *(de gift)* | **donation / gift** | sometimes ALSO "poison" *(het gif / het gift = poison)* — context-dependent! `de gift` = donation, `het gif/gift` = poison |
| **rare** *(adj)* | **strange / weird** | NOT "rare" → use **zeldzaam** for rare |
| **groot** | **big / large / great** | "great" in the "excellent" sense → use **geweldig / fantastisch** |
| **doof** | **deaf** | NOT "doofus" (no such Dutch word) |
| **klimaat** | **climate** ✓ | (same; no false friend) |
| **fabriek** | **factory** | NOT "fabric" → use **stof / weefsel** for fabric |
| **mist** | **fog** | NOT "mist" → also OK; missed = gemist |
| **vlug** | **fast / quick** | NOT "flu" → flu is **griep** |
| **stoel** | **chair** | NOT "stool" → stool is **kruk** |

### Idioms — translate the MEANING, not the words

| English idiom | Wrong (literal) | Natural Dutch |
|---------------|-----------------|---------------|
| Break a leg! | breek een been | **Succes! / Veel succes! / Zet 'm op!** |
| Piece of cake | stuk taart | **Een eitje / Appeltje, eitje / Fluitje van een cent** |
| It's raining cats and dogs | het regent katten en honden | **Het regent pijpenstelen / Het giet** |
| Spill the beans | morsen de bonen | **De waarheid opbiechten / Doorslaan** |
| Cost an arm and a leg | kost een arm en een been | **Een rib uit het lijf kosten / Handenvol geld kosten** |
| Hit the nail on the head | sla de spijker op de kop *(this one IS natural Dutch!)* | **De spijker op zijn kop slaan** ✓ |
| Once in a blue moon | eens in een blauwe maan | **Eens in de zoveel tijd / Eens in de honderd jaar** |
| Beat around the bush | sla rond de bos | **Eromheen draaien / Om de hete brij heen draaien** |
| Burn the midnight oil | brand de middernacht olie | **Nachtwerk verrichten / Tot diep in de nacht doorwerken** |

### Structural calques — restructure for V2 / verb-final

- ❌ English passive overuse: "The file was saved by the user." → ✅ Dutch active or "er-passive": **De gebruiker heeft het bestand opgeslagen** / **Het bestand is opgeslagen**.
- ❌ English noun stacking: "Project Folder Settings" → ✅ Dutch compound: **Projectmapinstellingen** / restructure: **Instellingen voor de projectmap**.
- ❌ English "of"-genitive overload: "settings of the project of the user" → ✅ Dutch genitive or van-chain: **gebruikersprojectinstellingen** / **de instellingen van het project van de gebruiker** (when natural) / restructure.
- ❌ Mid-sentence pronoun ambiguity: "If you click here, you see..." → ✅ Subordinate clause word order: **Als je hier klikt, zie je...**

### Marketing "zero X" patterns

| Wrong | Correct |
|-------|---------|
| Zero downtime | **Geen downtime / Zonder downtime** |
| Null fouten | **Foutloos / Geen fouten** |
| Nul verplichting | **Zonder verplichting / Geheel vrijblijvend** |
| Zero hassle | **Geen gedoe / Moeiteloos** |

### Compound adjectives — restructure

| English | Wrong (literal) | Correct |
|---------|-----------------|---------|
| X-aware | X-bewust | **met X-ondersteuning / X-geschikt / met X compatibel** |
| X-powered | X-aangedreven *(stiff)* | **op basis van X / met X / aangedreven door X** *(the last one is becoming OK)* |
| X-driven | X-gedreven | **op basis van X / gebaseerd op X / gestuurd door X** |
| AI-powered | AI-aangedreven | **met AI / op basis van AI / AI-gestuurd** |
| Data-driven | data-gedreven | **op basis van data / data-gestuurd** |
| Mobile-first | mobiel-eerst | **mobielvriendelijk / mobile-first** *(accepted)* |

## Self-Check Checklist

Run before finalizing.

### Accuracy

- [ ] **de / het correct** for every noun (het bestand, het systeem, het probleem, het account, het wachtwoord, het scherm; de map, de gebruiker, de service, de e-mail, de pagina)
- [ ] **Adjective endings**: definite = -e; indef + de-word = -e; indef + het-word = NO -e; plural = -e; predicative = no ending
- [ ] **V2 word order** in main clauses (verb is the 2nd constituent)
- [ ] **Verb-final** in subordinate clauses (after dat, omdat, wanneer, als, terwijl, hoewel, zodat)
- [ ] **Separable verbs split** in main clauses (sla...op, log...uit, schakel...uit) and **rejoined** in subordinate clauses
- [ ] **English-origin verbs** (downloaden, uploaden, updaten) are NOT separable — conjugate as single units
- [ ] **jij inversion**: -t drops after the verb (`Werk jij?` not `Werkt jij?`)
- [ ] **Past participles**: ge- prefix except after be-/ge-/ver-/ont-/er-/her-; correct trema where needed (geüpload, geüpdatet)
- [ ] **IJ** capitalized as IJ (both letters), not Ij. ij stays one letter, never hyphenated mid-digraph.
- [ ] **No noun capitalization** — only proper nouns and sentence-initial words. Lowercase: huis, computer, maandag, januari.
- [ ] **Languages and nationality adjectives ARE capitalized**: Nederlands, Engels, Frans (because derived from country names).
- [ ] **Compound nouns written as one word** (database, gebruikersinterface, projectmap, veiligheidsinstellingen) with correct linking elements (-s-, -en-).
- [ ] **Gender of compounds** follows the LAST element (huisdeur = de huisdeur because deur is de-).
- [ ] **Plural forms** correct (-en for most, -s for many loanwords, -s with apostrophe after vowel: baby's, foto's). All plurals take `de`.
- [ ] **Diminutives** are always `het` and pluralize in -s: het tafeltje → de tafeltjes.
- [ ] **Quotation marks**: straight `"..."` or `„..."` consistently; not English curly `"..."`.
- [ ] **Numbers**: `3,14` and `1.000`; `€ 99,99`
- [ ] **Date**: DD-MM-YYYY (`15-01-2024`) or `15 januari 2024` *(lowercase month)*
- [ ] **Time**: `14:30` or `14.30` (24-hour)
- [ ] **Comma rules**: NO comma before en/of; comma before maar/want; ALWAYS comma before dat/omdat/wanneer/als/terwijl/hoewel; no Oxford comma in lists.
- [ ] **No grammatical case errors** — Dutch has no case system, so reject any introduction of *den / *dem / *des forms.
- [ ] **All `{variables}` and ICU plural syntax preserved exactly.**
- [ ] **FOR vs PER**: `voor 5 talen` (total) vs `per taal` (rate).
- [ ] **Domain terminology** uses IT meaning (software-architectuur, CI/CD-pipeline, database, deployen).

### Naturalness

- [ ] **je/u consistency** — pronouns, possessives, and imperatives all match (je+je/jouw OR u+uw; never u+je or u+jouw).
- [ ] **Buttons in infinitive form** (Opslaan, Verwijderen, Annuleren — NOT imperative "Sla op").
- [ ] **Status ongoing**: `Wordt geladen...` or `Bezig met X...` or `X...` — NOT `Ik laad...`.
- [ ] **Completion in past participle**: `Opgeslagen`, `Geüpload`, `Voltooid`.
- [ ] **Failure**: `Fout bij X` or `X mislukt` — NOT `X heeft gefaald` *(calque)*.
- [ ] **Empty states use `geen`**: `Geen resultaten`, `Geen bestand geselecteerd` — NOT `niet bestand` or `nul resultaten`.
- [ ] **Drag-drop vocabulary**: slepen, neerzetten/loslaten, bladeren/selecteren — NOT draggen/droppen/browsen.
- [ ] **Anglicism avoidance** where Dutch verb exists: verwijderen (NOT deleten), annuleren (NOT cancelen), opslaan (NOT saven), bewerken (NOT editeren).
- [ ] **False friends avoided**: uiteindelijk (NOT eventueel for "eventually"), eigenlijk/daadwerkelijk (NOT actueel for "actual"), meelevend (NOT sympathiek for "sympathetic").
- [ ] **Calques eliminated**: "het is logisch" NOT "het maakt zin"; "uiteindelijk" NOT "aan het einde van de dag"; "kijk eens" NOT "neem een kijkje".
- [ ] **Compound adjectives restructured**: "op basis van AI" / "AI-gestuurd" NOT "AI-aangedreven"; "met X-ondersteuning" NOT "X-bewust".
- [ ] **Marketing zero patterns**: "geen X" / "zonder X" — NOT "nul X" / "zero X".
- [ ] **No English noun stacking**: use compounds (projectmap) or van-construction.
- [ ] **Capability-focused over noun-focused**: "Ondersteunt X" NOT "Ondersteuning voor X".
- [ ] **`er`-construction used where natural**: "Er staat een bestand op het bureaublad", "Er zijn geen resultaten".
- [ ] **Variant consistency** — nl-NL throughout, OR nl-BE throughout; don't mix inloggen with aanmelden, or mobiel with gsm.
- [ ] **Proper nouns use short forms** (VS not Verenigde Staten van Amerika; VK or Groot-Brittannië not Verenigd Koninkrijk en Noord-Ierland).
- [ ] **Tone matches source register** — formal source → formal Dutch (u), informal → je. No mid-string register switch.

## Worked Examples

### Example 1 — Stuffed with errors, then corrected

**Source (English):**
> "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

**Wrong (literal, German-influenced, anglicism-heavy):**
> Welkom! Bitte selecteer Uw File om te uploaden — wij supporten 25+ Formaten en vertalen het pro 5 Talen in {seconds}. Maak je niet druk, jij kunt op elk moment cancellen.

**Issues:**
- `selecteer` → not infinitive (UI button form); also `selecteer` is OK as imperative but the source structure asks for instruction-style
- `Uw / File / Formaten` — German-style noun capitalization
- `supporten` — anglicism; use `ondersteunen`
- `25+` — should be `meer dan 25`
- `pro 5 Talen` — German calque; should be `voor 5 talen` (FOR not PER here)
- `{seconds}` — needs unit word `seconden`
- Mixed register: `Uw` (formal) then `jij` (informal) then `je`
- `cancellen` → use `annuleren`
- `Maak je niet druk` is OK but `Geen zorgen` reads more natural in UI

**Correct (je-form, nl-NL):**
> Welkom! Selecteer het bestand dat je wilt uploaden — we ondersteunen meer dan 25 formaten en vertalen het in {seconds} seconden voor 5 talen. Geen zorgen, je kunt op elk moment annuleren.

**Correct (u-form, nl-NL formal or nl-BE):**
> Welkom! Selecteer het bestand dat u wilt uploaden — we ondersteunen meer dan 25 formaten en vertalen het in {seconds} seconden voor 5 talen. Geen zorgen, u kunt op elk moment annuleren.

### Example 2 — V2 word order under stress

**Source:**
> "Today, the system saves all files automatically. If you click here, you can disable it."

**Wrong (English word order):**
> Vandaag, het systeem slaat automatisch alle bestanden op. Als je klikt hier, je kunt het uitschakelen.

**Issues:**
- After fronted time-adverb `Vandaag`, verb must come BEFORE subject (V2)
- After subordinate `Als je klikt hier` — `hier` and `klikt` are misordered; in subord clause, verb at END: `Als je hier klikt`
- Main clause after the comma needs V2: `kun je`, NOT `je kunt` *(verb-2 inversion with the comma-fronted subord clause counting as "first element")*

**Correct:**
> Vandaag slaat het systeem automatisch alle bestanden op. Als je hier klikt, kun je het uitschakelen.

### Example 3 — Separable verb in main and subordinate

**Source:**
> "Save the file before you log out, because the system will close it."

**Wrong (verb not split / not reunited correctly):**
> Opslaan het bestand voordat je uitlogt, omdat het systeem zal het sluiten.

**Issues:**
- Imperative for instruction → in Dutch instructional prose, use imperative `Sla ... op` (split!) — OR restructure
- `voordat je uitlogt` — subordinate, so `uitlogt` (rejoined) ✓ correct
- `omdat het systeem zal het sluiten` — subordinate, verb at end: `omdat het systeem het zal sluiten`

**Correct:**
> Sla het bestand op voordat je uitlogt, omdat het systeem het zal sluiten.

### Example 4 — de/het with adjective endings

**Source:**
> "A new project, the new user, a big problem, the big problems."

**Wrong:**
> Een nieuw project *(actually correct — `project` is het-word, indef het-word = no -e ✓)*, de nieuw gebruiker *(wrong — definite always -e)*, een grote probleem *(wrong — indef het-word = no -e)*, de grote problemen *(correct)*.

**Correct:**
> Een nieuw project, de nieuwe gebruiker, een groot probleem, de grote problemen.

### Example 5 — Diminutive register

**Source:**
> "Hey! Got a sec? Quick question about your file."

**Wrong (over-formal, no warmth):**
> Hallo. Heeft u een moment? Een korte vraag over uw bestand.

**Correct (informal with diminutive warmth — nl-NL consumer):**
> Hey! Heb je een seconde? Een vraagje over je bestandje.

(Note the diminutives `seconde → seconde` — actually here `seconde` is the form; `secondje` exists colloquially. `vraagje` and `bestandje` add casual warmth — appropriate for matched casual register.)

### Example 6 — Marketing copy with calques

**Source:**
> "Our AI-powered platform makes sense for any team. At the end of the day, you save time and effort. Zero hassle, future-proof."

**Wrong (calques everywhere):**
> Ons AI-aangedreven platform maakt zin voor elk team. Aan het einde van de dag bespaar je tijd en moeite. Nul gedoe, toekomst-proof.

**Issues:**
- `AI-aangedreven` — stiff compound adjective; use "met AI" or "op basis van AI" or "AI-gestuurd"
- `maakt zin` — calque; use "is logisch" or "slaat ergens op"
- `Aan het einde van de dag` — calque; use "uiteindelijk" or "per saldo"
- `Nul gedoe` — calque; use "Geen gedoe"
- `toekomst-proof` — calque; use "toekomstbestendig"

**Correct:**
> Ons AI-gestuurde platform is logisch voor elk team. Uiteindelijk bespaar je tijd en moeite. Geen gedoe, toekomstbestendig.

### Example 7 — nl-NL vs nl-BE divergence

**Source:**
> "Log in with your mobile number. Open the microwave settings."

**nl-NL:**
> Log in met je mobiele nummer. Open de magnetroninstellingen.

**nl-BE (Flemish):**
> Meld u aan met uw gsm-nummer. Open de microgolfoveninstellingen.

(Note: BE shifts to `u`+`uw` register by default, swaps `inloggen` → `aanmelden`, `mobiel` → `gsm`, `magnetron` → `microgolfoven`.)

### Example 8 — er-construction

**Source:**
> "There are no files in this folder. There's a problem with the connection."

**Wrong (no er):**
> Geen bestanden zijn in deze map. Een probleem is met de verbinding.

**Correct (er-construction is the natural Dutch existential):**
> Er staan geen bestanden in deze map. Er is een probleem met de verbinding.

### Example 9 — ICU plural in Dutch

```
{count, plural, one {# bestand verwijderd} other {# bestanden verwijderd}}
```

- `one` branch: singular noun (`bestand`), verb agrees with singular subject.
- `other` branch: plural noun (`bestanden`), plural verb if needed.
- Numbers in the ICU branches use `#` which interpolates the count — formatted as Dutch number (`1.000` thousands).
- For zero, you can add a `zero` branch in some ICU dialects, but standard Dutch has no zero/few/many/dual — only one/other (CLDR `one` covers 1; `other` covers 0 and 2+).

Worked plural strings:

| English | Dutch |
|---------|-------|
| 1 file | 1 bestand |
| 0 files | 0 bestanden |
| 5 files | 5 bestanden |
| 1,000 files | 1.000 bestanden |
| 1 user | 1 gebruiker |
| 1 language | 1 taal |
| 5 languages | 5 talen *(taal pluralizes irregularly: taal → talen)* |
| 1 child | 1 kind |
| 5 children | 5 kinderen *(kind pluralizes irregularly: kind → kinderen)* |

### Example 10 — Email salutations and closings

**Formal:**
- Salutation: `Geachte heer Jansen,` / `Geachte mevrouw Jansen,` / `Geachte heer/mevrouw,` *(when unknown)* / `Geachte heer of mevrouw,`
- Body opens lowercase: `Geachte heer Jansen,\n\nhartelijk dank voor uw bericht...`
- Closing: `Met vriendelijke groet,` / `Met hartelijke groet,` / `Hoogachtend,` *(very formal)*
- Sign-off line breaks before name.

**Informal:**
- Salutation: `Hoi Anna,` / `Hi Max,` / `Hé Sam,` / `Beste Anna,` *(slightly more formal informal)*
- Closing: `Groet,` / `Groetjes,` / `Vriendelijke groet,` / `Tot snel,` / `Tot ziens,` / `Liefs,` *(intimate)*

**Business neutral (mixed):**
- Salutation: `Beste {naam},`
- Closing: `Met vriendelijke groet,` / `MVG` *(abbreviation in email signatures)*

## When in Doubt

1. **de or het?** Look it up. Don't guess. The Van Dale, Woordenlijst Nederlandse Taal (Groene Boekje), or any modern dictionary has it. If a noun is both (some loanwords have both: "de/het web", "de/het advies" in old usage — though "het advies" is now standard), pick the more common form. Diminutives → always `het`. Plurals → always `de`.

2. **je or u?** Default to **je** for nl-NL software/marketing UI. Default to **u** for nl-BE, financial, legal, healthcare, government, insurance, premium brands. Match source register. Never mix within a file.

3. **V2 or verb-final?** If the clause starts with a subordinating conjunction (dat, omdat, als, wanneer, hoewel, terwijl, zodat, voordat, nadat), verb at END. Otherwise, V2 — verb is the 2nd constituent.

4. **Separable verb?** Check the infinitive. If it has an unstressed prefix like `op-`, `uit-`, `in-`, `aan-`, `af-`, `door-`, `mee-`, `terug-`, `bij-`, `over-` AND the stress falls on that prefix, it splits in main clauses. `downloaden`, `uploaden`, `googlen`, `updaten` (English-origin) are NOT separable.

5. **Spelling reform questions?** Follow the Taalunie's Groene Boekje (Woordenlijst Nederlandse Taal — official spelling dictionary). 1995 + 2005 + 2015 reforms unified spelling across NL and BE. Use modern forms: `pannenkoek` (not pannekoek since 1995), `tussen-n` rules apply.

6. **Capitalize or not?** Lowercase: common nouns, days, months. Capitalize: sentence-initial, proper nouns, languages (`Nederlands`, `Engels`), nationality adjectives derived from country names (`Nederlandse`, `Engelse`), brand names. IJ at start of word → BOTH letters cap.

7. **Variant ambiguous?** If you can't tell whether the audience is nl-NL or nl-BE, use neutral forms: infinitive buttons (`Opslaan`), neutral verbs (`registreren` for sign-up), avoid clear BE-only terms (`gsm`, `microgolfoven`) unless explicitly requested.

8. **Anglicism or Dutch verb?** Prefer the Dutch verb where it exists naturally: `verwijderen` over `deleten`, `opslaan` over `saven`. Accept the anglicism when it's the de-facto standard: `downloaden`, `uploaden`, `googlen`, `mailen`, `liken`, `chatten`. Conjugate them with Dutch endings.

9. **Diminutive or base form?** Diminutives carry warmth/casualness — use sparingly in business UI, freely in consumer warmth. `een vraagje` is friendlier than `een vraag`; `bestandje` is casual; `momentje` (one moment) is universally accepted.

10. **Stuck on a phrase?** Read it back in English. If the English source has a clear, idiomatic meaning, find the Dutch idiom that conveys the SAME meaning — not the same words. "Break a leg" is `Succes!`, not `Breek een been`.

When all else fails: prefer **direct, clear, lowercased, comma-disciplined, V2-ordered, gender-correct** Dutch. That alone clears 90% of common errors.
