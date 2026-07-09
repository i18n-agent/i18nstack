---
name: localize-it
description: Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Italian (it). Enforces Lei/tu consistency, le/la/lo gender + number agreement, article contractions (al, del, nel), conjunction `e → ed` before vowels starting with `e`, subjunctive after doubt/necessity, postnominal adjectives, anglicism-verb avoidance (caricare not uploadare), and `Senza X` marketing patterns over English `Zero X` calques.
---

# Italian Translation Rules (it / italiano)

Distilled from the production translation prompts. Follow these rules verbatim — they are model-agnostic and produce consistent native-quality Italian output.

## Mindset

> Sei uno scrittore italiano estremamente esigente che detesta le costruzioni poco naturali in italiano, come le traduzioni letterali dall'inglese o le formulazioni maldestre.

Reject literal English calques and verbed anglicisms. Restructure fully into natural Italian. Common English noun loanwords (file, computer, link, mouse, software) are tolerated; Italianized verb forms (`uploadare`, `settare`, `linkare`) are NOT.

## Pre-Translation Setup

Lock in before translating:

1. **Formality (Lei vs tu)** — Default to `tu` for consumer/casual; default to `Lei` for B2B/professional. NEVER mix within a file. (`voi` plural formal is out-of-scope — stick to Lei or tu.)
2. **Two genders** — il/lo/la/l' (singular), i/gli/le (plural). Article choice depends on what follows.
3. **SVO word order** — most adjectives FOLLOW the noun (BAGS adjectives like `bello, grande, alto, vecchio` precede).
4. **No French-style NBSP** — Italian uses standard ASCII spacing around `: ; ? !` (don't apply French rules).
5. **Placeholders** — Preserve `{variables}` and ICU plural syntax exactly.

## Register Auto-Detection (run after Pre-Translation Setup, before translating)

If the user has NOT specified Lei or tu, infer from source text register. Match output to source — formal source → Lei; informal source → tu.

### Formal source signals → output Lei / La / Le / Suo / Sua / Suoi / Sue (all capitalized)
- Hedging / polite modals: "please", "kindly", "we recommend", "could you", "would you mind"
- Passive / impersonal: "users are advised", "it is recommended", "applicants must"
- No contractions: "do not", "cannot", "we will"
- Domain vocabulary: legal, financial, healthcare, regulatory, enterprise B2B, government, insurance, luxury, automotive
- Third-person / distance: "the user must", "customers should"
- Long sentences, formal connectors ("inoltre", "tuttavia", "pertanto")
- Brand voice: bank, insurance, government, B2B SaaS, healthcare, legal tech, luxury retail
- No exclamations or emojis

### Informal source signals → output tu / tuo / tua / tuoi / tue (lowercase)
- Contractions: "don't", "you'll", "it's", "we're"
- Casual greetings: "hey", "hi there", "yo", "hi 👋", "ciao!"
- Second-person directness, exclamations, emoji (🎉 😎 🚀 ✨)
- Slang: "cool", "awesome", "no worries", "kinda"
- Consumer-app voice: gaming, social, lifestyle, dating, fitness, kids, casual e-commerce, food delivery
- Sentence fragments and conversational filler

### Mixed / ambiguous source → default to Lei
Lei reads slightly distant but professional; tu can read as overly familiar in B2B/government/luxury contexts. When in doubt, stay formal — most Italian B2B and many consumer brands still use Lei. Italian consumer-app trend toward tu is more recent than in other Romance languages.

### Explicit user override
If the user says "use tu" / "use Lei" / "formal" / "casual" / "give me the dài-form" (rare), their instruction wins.

### Worked examples

| Source | Detected | Italian output |
|----------------|----------|----------------|
| "Please review the terms of service before proceeding." | formal | La preghiamo di leggere i termini di servizio prima di procedere. |
| "Hey! Tap here to get started — it's super quick 🚀" | informal | Ciao! Tocca qui per iniziare — è super veloce 🚀 |
| "Submit your application by the deadline." | formal | Invii la Sua candidatura entro la scadenza. |
| "Don't forget to save your work!" | informal | Non dimenticare di salvare il tuo lavoro! |

After detection: keep the chosen form consistent. NEVER mix Lei/tu across pronouns, possessives, OR imperatives.

### Voi (plural formal) — out-of-scope
`voi` as 2nd-person plural formal is historical/southern Italian usage (still common in Naples, parts of Sicily, older formal correspondence). For modern standard Italian software UI, **stick to Lei (singular formal) and tu (singular informal)**. Plural is rendered as `voi` (informal plural) or `Loro` (very formal plural, archaic — avoid). For UI strings addressing multiple users, prefer recasting to singular or using neutral infinitives (`Salvare`, `Eliminare`).

## Critical Accuracy Rules

### 1. Gender of common IT nouns (memorize)

| Masculine | Feminine |
|-----------|----------|
| **il** problema | **la** soluzione |
| **il** sistema | **la** piattaforma |
| **il** programma | **l'**applicazione |
| **il** tema | **l'**interfaccia |
| **il** file | **la** pagina |
| **il** software | **la** rete |
| **il** server | **la** connessione |
| **il** browser | **la** configurazione |
| **il** link | **la** validazione |
| **il** plugin | **la** versione |
| **il** database | **la** cartella |
| **il** documento | **l'**email (also `la mail`) |
| **il** messaggio | **la** password |

**-ma Greek-origin nouns are MASCULINE** (despite ending in -a): `il problema, il sistema, il programma, il tema, lo schema`.
**-zione / -sione / -tà / -tù → ALWAYS feminine**: `la soluzione, la connessione, la qualità, la gioventù`.

**Foreign tech brands default to MASCULINE**: `il OneSky, il Slack, il Teams`. Exception: `l'Apple` (company, fem implied by "ditta/azienda").

Common errors: `la problema` → `il problema`; `il soluzione` → `la soluzione`; `la sistema` → `il sistema`.

### 2. Acronym gender inheritance (CRITICAL, severity 2.0)

Acronyms inherit gender from the expanded form. Translate English acronyms too.

| Acronym | Expansion | Gender |
|---------|-----------|--------|
| **l'IA** | Intelligenza Artificiale | feminine |
| **l'API** | Interfaccia di Programmazione | feminine |
| **la CPU** | Unità Centrale | feminine |
| **l'URL** | Localizzatore | masculine |
| **il PDF** | Formato Documento | masculine |

| Wrong | Correct |
|-------|---------|
| il nostro AI | **la nostra IA** (translate + correct gender) |
| il nostro IA | **la nostra IA** |

### 3. Article selection — `il / lo / la / l'`

| Use | Before |
|-----|--------|
| `il` | masc + consonant: `il file`, `il computer` |
| `lo` | masc before **s+consonant, z, gn, ps, x, y**: `lo spirito`, `lo psicologo`, `lo zaino`, `lo gnomo`, `lo xilofono` |
| `la` | fem + consonant: `la pagina` |
| `l'` | any vowel: `l'utente` (m), `l'applicazione` (f) |

Plurals: `i` (masc + cons) / `gli` (masc + vowel/s+cons/z/etc.) / `le` (fem all).

| Wrong | Correct |
|-------|---------|
| il utente | **l'utente** |
| il psicologo | **lo psicologo** |
| il spirito | **lo spirito** |

### 4. Apostrophe / elision — `un'` is FEMININE ONLY

| Wrong | Correct |
|-------|---------|
| un'utente (masc) | **un utente** (no apostrophe for masc) |
| una applicazione | **un'applicazione** (fem: apostrophe) |
| il utente | **l'utente** |
| dell utente | **dell'utente** |
| nell applicazione | **nell'applicazione** |

`un'` ONLY for feminine before vowel. Masculine before vowel = `un` with no apostrophe.

### 5. Preposition contractions (mandatory, severity 1.0)

| Combine | → |
|---------|---|
| a + il | **al** |
| a + la | alla |
| a + l' | all' |
| a + i | ai |
| a + gli | agli |
| a + le | alle |
| di + il | **del** |
| di + la | della |
| in + il | **nel** |
| in + la | nella |
| su + il | **sul** |
| da + il | **dal** |

| Wrong | Correct |
|-------|---------|
| di il progetto | **del progetto** |
| a la piattaforma | **alla piattaforma** |
| in il sistema | **nel sistema** |

### 6. Article completeness in noun phrases (CRITICAL, severity 1.5)

Specific known nouns require articulated prepositions. Exception: generic classifiers (`errore di sistema` = type of error).

| Wrong | Correct |
|-------|---------|
| Errore di applicazione | **Errore dell'applicazione** |
| Configurazione di account | **Configurazione dell'account** |
| Stato di connessione | **Stato della connessione** |
| Dettagli di transazione | **Dettagli della transazione** |
| variabile di ambiente manca | **la variabile di ambiente manca** / `manca la variabile di ambiente` |

### 7. Conjunction `e → ed` (euphonic rule, CRITICAL, severity 1.5)

Use `ed` ONLY before a word starting with `e`. Use `e` everywhere else (including before other vowels).

| Wrong | Correct |
|-------|---------|
| e ecco | **ed ecco** |
| e elegante | **ed elegante** |
| ed API (starts with /a/) | **e API** |
| ed italiano (starts with /i/) | **e italiano** |

Modern Italian uses `ed` only before `e-` (older usage extended to all vowels — avoid it).

### 8. Accents — distinguish meaning

| Wrong | Correct | Why |
|-------|---------|-----|
| perche | **perché** | acute on closed `e` |
| citta | **città** | grave on stressed final |
| caffe | **caffè** | grave on open `e` |
| e importante | **è importante** | `è` = is; `e` = and |
| pero (= pear tree) | **però** (= but) | accent disambiguates |
| pò | **po'** (= a bit) | uses apostrophe, NOT accent |
| si (reflexive) | **sì** (= yes) | accent on "yes" |
| da (preposition) | **dà** (= gives) | accent on the verb |

### 9. Double consonants (severity 1.5)

| Wrong | Correct |
|-------|---------|
| applicatione | **applicazione** |
| conessione | **connessione** |
| programare | **programmare** |
| comunicazione (this is correct) | comunicazione |
| professionale (correct) | professionale |

### 10. Subjunctive (congiuntivo) — required after doubt / necessity / emotion

Triggers: `È necessario che`, `È possibile che`, `Bisogna che`, `Sembra che`, `Credo che`, `Penso che`, `Spero che`, and conjunctions: `sebbene, nonostante, affinché, benché, purché, prima che, senza che`.

| Wrong (indicative) | Correct (subjunctive) |
|--------------------|----------------------|
| È possibile che il file è corrotto | **È possibile che il file sia corrotto** |
| Bisogna che l'utente salva | **Bisogna che l'utente salvi** |
| nonostante il sistema funziona | **nonostante il sistema funzioni** |
| È necessario che il campo è compilato | **È necessario che il campo sia compilato** |

### 11. Past participle agreement (severity 2.0)

- With **essere**: agrees with subject (gender + number).
- With **avere**: agrees with preceding direct object.

| Wrong | Correct |
|-------|---------|
| Le opzioni sono stato attivato | **Le opzioni sono state attivate** (fem plural) |
| I file sono stato salvato | **I file sono stati salvati** (masc plural) |

### 12. Number / loanword agreement (CRITICAL, severity 2.0)

English loanwords are typically invariable (no plural -s in Italian), but Italian adjectives must still agree in gender/number.

| Wrong | Correct |
|-------|---------|
| i file nuovo | **i file nuovi** |
| il software aggiornata | **il software aggiornato** (software is masc) |
| le feature nuovo | **le feature nuove** |
| i plugin aggiornato | **i plugin aggiornati** |
| le soluzione | **le soluzioni** |

### 13. Adjective position

- Most adjectives FOLLOW the noun: `coerenza perfetta`, `qualità superiore`, `servizio personalizzato`.
- BAGS adjectives (Beauty, Age, Goodness, Size) PRECEDE: `un bell'esempio, un grande progetto, una nuova versione, una piccola azienda`.
- Position can change meaning: `un uomo grande` (tall) vs `un grand'uomo` (great).

| Wrong | Correct |
|-------|---------|
| con perfetta coerenza | **con una coerenza perfetta** / `in modo perfettamente coerente` |
| di superiore qualità | **di qualità superiore** / `di alta qualità` |
| qualità umana (in tech) | **qualità a livello umano** / `qualità professionale` |

## BAGS Adjectives (prenominal)

Most Italian adjectives FOLLOW the noun. BAGS adjectives PRECEDE the noun.

- **B**eauty: `bello, bellissimo, brutto, carino`
- **A**ge: `giovane, vecchio, antico, nuovo, anziano`
- **G**oodness/quality: `buono, ottimo, cattivo, pessimo, grande, grandioso`
- **S**ize: `grande, piccolo, lungo, breve, alto, basso, vasto`

These adjectives can ALSO follow the noun, but the meaning shifts:
- `un grand'uomo` (a great man) vs `un uomo grande` (a tall man)
- `un vecchio amico` (a long-time friend) vs `un amico vecchio` (an elderly friend)
- `un povero ragazzo` (poor / unfortunate) vs `un ragazzo povero` (poor / financially)
- `un caro amico` (dear friend) vs `un amico caro` (expensive friend — rare meaning)
- `un certo modo` (a certain way) vs `un modo certo` (a sure way)

Article elision before BAGS: `un bel film` (NOT `un bello film`); `un buon caffè` (NOT `un buono caffè`); `un gran lavoro` (NOT `un grande lavoro`).

Reference table:

| Adjective | Before noun (idiomatic) | After noun (literal) |
|-----------|--------------------------|----------------------|
| grande | un grand'uomo (great) | un uomo grande (tall) |
| vecchio | un vecchio amico (long-time) | un amico vecchio (elderly) |
| povero | un povero ragazzo (unfortunate) | un ragazzo povero (poor) |
| caro | un caro amico (dear) | un caro amico (also OK) |
| certo | un certo libro (some) | un libro certo (certain) |
| diverso | diverse opinioni (various) | opinioni diverse (different) |
| nuovo | un nuovo modello (new release) | un modello nuovo (brand-new condition) |

### 14. FOR vs PER (CRITICAL, severity 2.0)

Both use `per` — disambiguate with quantifier placement.

| English | Wrong | Correct |
|---------|-------|---------|
| for 5 languages (total) | per lingua | **per 5 lingue** |
| per language (rate) | per 5 lingue | **per lingua** / `a lingua` |

### 15. Domain terminology — IT meaning

| English | Wrong | Correct |
|---------|-------|---------|
| build (software) | costruzione | **sviluppare / creare / realizzare** |
| deploy | dispiegare (military) | **distribuire / rilasciare / mettere in produzione** |
| support (feature) | (ambiguous `supportare`) | **supportare** (accepted in tech) / `essere compatibile con` / `includere il supporto per` |
| sync with [Platform] | sincronizzare con il/la Platform | **sincronizzare con [Platform]** (no article for destinations) |
| listings (app store) | liste, elenchi | **schede dell'app / pagine dell'applicazione** |
| architecture (software) | architettura (costruzione) | **architettura (software)** |
| pipeline (CI/CD) | tubatura | **pipeline (CI/CD)** |
| source of truth | fonte della verità | **fonte di riferimento / fonte autoritativa** |

## UI Conventions

### Buttons — infinitive form (neutral, works with Lei AND tu)

| Wrong | Correct |
|-------|---------|
| Fare il salvataggio | **Salvare** / `Salva` (tu) |
| Effettuare l'eliminazione | **Eliminare** / `Elimina` |
| Salvi (Lei imperative) | **Salvare** (avoids formality complexity) |

### Status messages — nominalized noun form

| Wrong | Correct |
|-------|---------|
| Sta salvando... | **Salvataggio...** |
| Sta caricando... | **Caricamento...** |
| Sta elaborando... | **Elaborazione in corso...** |

### Completion messages — participial (NOT `riuscito`)

| Wrong (calque) | Correct |
|----------------|---------|
| Pagamento riuscito | **Pagamento effettuato** / `Pagamento completato` |
| Caricamento riuscito | **Caricamento completato** / `File caricato` / `Fatto!` |
| Download completo | **Download completato** / `Download terminato` |
| Operazione riuscita | **Operazione completata** / `Fatto!` |

For failures:

| Wrong | Correct |
|-------|---------|
| Operazione fallita | **Errore durante [Noun]** / `Non è stato possibile completare [Noun]` |

### Empty state — `Nessun(o/a) X` or `Non ci sono X`

| Wrong | Correct |
|-------|---------|
| Niente risultati | **Nessun risultato** / `Non ci sono risultati` |
| Niente file selezionato | **Nessun file selezionato** |
| Senza dati | **Nessun dato disponibile** / `Non ci sono dati disponibili` |
| Vuoto | **Nessun elemento presente** |

`Nessun/Nessuno/Nessuna` requires gender agreement.

### Drag and drop

| English | Italian |
|---------|---------|
| drag | trascinare |
| drop | rilasciare |
| **release** (let go) | **rilasciare** — NOT `permettere` (= permit) |
| **browse** (file picker) | **selezionare / scegliere** — NOT `sfogliare` |

| Wrong | Correct |
|-------|---------|
| Drag i file qui | **Trascina i file qui** |
| Permettere il caricamento | **Rilascia per caricare** |
| Sfoglia file | **Seleziona file / Scegli file** |

### Validation messages — three patterns

| Type | Mood | Example |
|------|------|---------|
| Field validation | indicative | `Questo campo è obbligatorio` / `Il formato non è valido` |
| Action instruction | imperative | `Inserisci un valore valido` / `Seleziona almeno una lingua` |
| State description | impersonal | `Non è stato possibile connettersi` / `Si è verificato un errore` |

| Wrong | Correct |
|-------|---------|
| Campo mancante | **Questo campo è obbligatorio** (`mancante` is calque of "missing") |
| Inserire un valore (infinitive in error) | **Inserisci un valore valido** (imperative) |

### Error messages — what happened + what to do

| Wrong (bare) | Correct |
|--------------|---------|
| File non trovato. | **File non trovato. Verificare il percorso.** |

### UI label completeness — complete noun phrases

| Wrong (bare adjective) | Correct |
|------------------------|---------|
| Alternativo | **Rilevamento alternativo** |
| Automatico | **Modalità automatica** |
| Avanzato | **Impostazioni avanzate** |

### Other UI patterns

| Wrong | Correct |
|-------|---------|
| Supporto per formati X | **Supporta formati X** / `Compatibile con formati X` (verb-focused) |
| Contenuto di Testo | **Contenuto del testo** (articulated preposition) |
| 25+ lingue | **più di 25 lingue** / `oltre 25 lingue` |
| +{count} in più | **e {count} altri** / `altri {count}` |

## Lei / tu Consistency

NEVER mix. ALL pronouns, possessives, AND imperatives must match.

| Don't mix | Use |
|-----------|-----|
| Lei può modificare le tue impostazioni | Lei può modificare **le Sue impostazioni** |
| Carichi i Suoi file + Sfoglia | Carichi i Suoi file + **Sfogli** |

**Capitalization:**
- Formal: capitalize `Lei, La, Le, Suo, Sua, Suoi, Sue` (third-person courtesy forms).
- Informal: lowercase `tuo, tua, tuoi, tue`.

**Imperative forms:**
- Formal Lei: third-person form — `Faccia, Salvi, Selezioni, Inserisca`
- Informal tu: second-person form — `Fai, Salva, Seleziona, Inserisci`
- Buttons: prefer **infinitive** (`Salvare`) — works with either level.

## Punctuation and Typography

| Item | Italian |
|------|---------|
| Decimal separator | **`,`** (comma) |
| Thousands separator | **`.`** (period) |
| Example number | `1.234,56` |
| Currency | `99,99 €` (symbol AFTER, with space) |
| Date | `15/01/2024` (DD/MM/YYYY) or `15 gennaio 2024` (lowercase months) |
| Time | `14:30` or `ore 14:30` (24-hour) |
| Quotation marks | `« »` or `"..."` (consistent within text) |
| Spacing around `: ; ? !` | **No NBSP** (unlike French) — standard ASCII spacing |
| Ellipsis | `…` (single char) preferred |

**Common conversions:**

| Wrong | Correct |
|-------|---------|
| `1,234.56 €` | **`1.234,56 €`** |
| `€99.99` | **`99,99 €`** |
| `01/15/2024` | **`15/01/2024`** |

## Comma Rules

| Before | Comma? |
|--------|--------|
| e / ed / o / oppure / né | **No comma** |
| ma / però / bensì | **Comma required** |
| che (relative) | comma usually required |
| se / perché | comma required |

| Wrong | Correct |
|-------|---------|
| Salva, e chiudi | Salva e chiudi |
| semplice ma efficace | semplice**,** ma efficace |

## Calques to Avoid

| Wrong (literal) | Natural Italian |
|-----------------|------------------|
| fa senso | **ha senso** |
| alla fine del giorno / della giornata | **in fin dei conti / in definitiva** |
| in ordine a | **per** |
| applicare per (un lavoro) | **candidarsi per** |
| e molto di più | **e molto altro / e molto altro ancora** |
| su una base giornaliera | **quotidianamente / ogni giorno** |
| in termini di | **per quanto riguarda / quanto a** |
| non veramente | **non proprio / non esattamente** |
| prendere vantaggio di | **trarre vantaggio da / approfittare di** |
| Break a leg | **In bocca al lupo!** |
| Piece of cake | **È un gioco da ragazzi** |
| It's raining cats and dogs | **Piove a catinelle** |

## Error Ownership Phrasing

| Wrong | Correct |
|-------|---------|
| dalla nostra parte (in error — ambiguous, can mean "on our side in a dispute") | **da parte nostra / dal nostro lato** |
| dalla nostra fine / dal nostro estremo (literal "on our end") | **da parte nostra / dal nostro lato** |
| nella nostra parte | **da parte nostra** |

## Anglicism Avoidance — Italianized VERBS

Italian tolerates **noun loanwords** (file, software, computer, link, mouse). Italian rejects **Italianized verb loanwords**.

| Anglicism (avoid) | Native verb |
|-------------------|-------------|
| uploadare | **caricare** |
| downloadare | **scaricare** |
| settare | **impostare** |
| linkare | **collegare** |
| deletare | **eliminare** |
| checkare / ceccare | **verificare / controllare** |
| fixare | **correggere / risolvere** |
| loggarsi | **accedere** |
| forwardare | **inoltrare** |

## False Friends

| Italian word | Means | NOT the English |
|--------------|-------|------------------|
| `attualmente` | currently | NOT "actually" — use `in realtà` |
| `eventualmente` | possibly | NOT "eventually" — use `alla fine / infine` |
| `realizzare` | to create / accomplish | NOT "realize (understand)" — use `rendersi conto` |
| `supportare` | to tolerate (general) / support a feature (tech, accepted) | careful in general contexts; use `sostenere` for emotional support |
| `libreria` | bookstore | NOT "library" — use `biblioteca` |
| `sensibile` | sensitive | NOT "sensible" — use `ragionevole` |
| `assistere` | to attend | NOT "assist" — use `aiutare` |
| `eccitato` (sexual connotation!) | aroused | NOT "excited" — use **`entusiasta`** (severity 2.0 — avoid this mistake) |

## Compound Adjectives — natural construction

| English pattern | Wrong | Correct |
|-----------------|-------|---------|
| AI-powered / X-powered | `IA-alimentato`, `traduzione di IA`, `impulsato dall'IA` | **`con IA / basato sull'IA / traduzione con IA`** |
| context-aware / X-aware | `X-consapevole` | **`contestuale / sensibile al contesto`** |
| user-friendly | `utente-amichevole` | **`intuitivo / facile da usare`** |
| cloud-based / X-based | `nuvola-basato` | **`basato su cloud / in cloud`** |
| supported formats | `formati supportati` (general usage), `X supportati` | **`formati compatibili / compatibile con X`** |

## Compound Descriptive Nouns

Decompose English compounds and rebuild with Italian noun-modification syntax.

| English | Wrong | Correct |
|---------|-------|---------|
| mom creators | creatrici mamme | **creatrici che sono mamme / mamme creatrici di contenuti** |
| niche creators | (literal) | **creatori di nicchia / creatori specializzati** |
| beauty influencers | (literal) | **influencer del settore beauty / influencer di bellezza** |

## Business Terminology

| English compound | Wrong (prepositional) | Correct (adjective) |
|------------------|------------------------|---------------------|
| enterprise translation | traduzione per aziende / traduzione di azienda | **traduzione aziendale** / `traduzione professionale` |
| enterprise solution | soluzione per imprese | **soluzione aziendale** / `soluzione professionale` |
| business service | servizio di impresa | **servizio aziendale / servizio commerciale** |
| business level | livello per imprese | **livello aziendale** |

## Marketing "Zero X" → "Senza X" / "Nessun(o/a) X"

| Wrong | Correct |
|-------|---------|
| Zero tempi di inattività / Zero downtime | **Senza interruzioni / Disponibilità continua** |
| Zero errori | **Senza errori / Nessun errore** |
| Zero manutenzione | **Senza manutenzione / Non richiede manutenzione** |
| Zero impegno | **Senza impegno** |

## Prepositional Chain Simplification

Limit to 2 prepositions max. Use adjectives or apposition.

| Wrong (3+ `di`) | Correct (simplified) |
|-----------------|----------------------|
| prodotti per la cura della pelle di notte | **cura notturna della pelle / prodotti per la cura notturna** |
| strumento di gestione di progetti di software | **strumento di gestione progetti software** |

## Technical Source Preposition

| Wrong (physical sense) | Correct (data provenance) |
|------------------------|---------------------------|
| dall'API | **dell'API** |
| dal server | **del server** |
| dal database | **del database** |
| risposta dal sistema | **risposta del sistema** |

`di` = source/belonging; `da` = physical origin/starting point.

## Spatial Metaphor Prepositions

| English (figurative) | Use | Don't use |
|---------------------|-----|-----------|
| under [category] (browsing) | **tra / nei** | sotto |
| on top of (in addition to) | **oltre a / in aggiunta a** | sopra |
| behind the scenes | **dietro le quinte** | (literal) |
| within [timeframe] | **entro / in** | all'interno di |

## Temporal Expression — "[YEAR] me" idiom (HIGHEST severity 2.5)

English "[YEAR] me" / "[DECADE]s me" / "[AGE] me" = "myself at that time", NOT "X years ago".

| Wrong | Correct |
|-------|---------|
| 2014 anni fa (for "2014 me") | **io nel 2014 / il me del 2014 / chi ero nel 2014** |
| 90 anni fa (for "90s me") | **io negli anni 90 / il me degli anni 90** |
| 14 anni io (for "teenage me") | **io a 14 anni / io da adolescente** |

## UI Element Reference in Prose

| Wrong | Correct |
|-------|---------|
| il campo di nome | **il campo «Nome»** or `il campo Nome` |
| la scheda degli account | **la scheda «Account»** |
| la barra di ricerca | (generic — no quotes needed) |

## Cost / Estimate Expression Ordering

- Amount-first with `per`: `99,99 € per 5 lingue` (preferred)
- Scope + `in totale`: `Costo totale: 499,99 €`
- Per-unit: `1.500 parole per lingua` / `99,99 € al mese`
- Wrong (ambiguous): `{count} lingue {credits} crediti` — needs a connector (`per`, `in totale`).

## Block Verb Mood Consistency

Child items must match the verb mood of the parent title/heading.

| Title frame | Wrong child | Correct child |
|-------------|-------------|---------------|
| `Cosa otterresti:` (conditional) | `Ricevi una proposta...` (imperative) | `Riceveresti una proposta...` (conditional) or `Proposta entro il giorno successivo...` (noun phrase) |
| `Passi da seguire:` (instructional) | `Configureresti il tuo account...` (conditional) | `Configura il tuo account...` (imperative) or `Configurare il tuo account...` (infinitive) |

## Brand Names — no article for platform destinations

| Wrong | Correct |
|-------|---------|
| sincronizzare con l'Apple App Store | **sincronizzare con Apple App Store** |
| pubblicare sul Google Play | **pubblicare su Google Play** |

When brand IS the subject: `L'App Store offre...` (article when modified) or `Google Play permette...` (no article for proper noun subject).

## Proper Nouns — short forms in UI

| Wrong | Correct |
|-------|---------|
| Stati Uniti d'America | **Stati Uniti / USA** |
| Regno Unito di Gran Bretagna e Irlanda del Nord | **Regno Unito** |
| inglese degli Stati Uniti | **inglese americano** |

## Cultural Conventions

- Communication style: expressive, formal in business; clarity valued alongside elegance.
- Date: `15/01/2024` or `15 gennaio 2024` (lowercase month names — `gennaio, febbraio, marzo, aprile, maggio, giugno, luglio, agosto, settembre, ottobre, novembre, dicembre`).
- Time: 24-hour `14:30` or `ore 14:30`.
- Currency: `99,99 €` (EUR, space before symbol, symbol after amount).

## Greetings, Time-of-Day, and Email Closings

- Greetings: `Buongiorno` (until ~14:00 or so), `Buon pomeriggio` (afternoon, less common, often skipped), `Buonasera` (evening, from ~17:00), `Buonanotte` (good night, when going to bed), `Salve` (universal polite, time-agnostic, slightly formal), `Ciao!` (informal, both hello and goodbye), `Arrivederci` (formal goodbye), `Arrivederla` (very formal singular goodbye — Lei context).
- UI welcome: `Benvenuto/a` (gender agreement with user — fallback `Benvenuti` plural), `Salve!`, `Ciao!` (informal).
- Email salutations formal: `Egregio Signor [Cognome],` (very formal, masculine), `Gentile Signora [Cognome],` (formal feminine), `Gentile Cliente,` (gender-neutral business), `Spettabile [Azienda],` (formal to a company).
- Email salutations informal: `Ciao [Nome],` `Cara/o [Nome],` `Salve [Nome],`.
- Email closings formal: `Cordiali saluti,` (standard), `Distinti saluti,` (more formal), `Le porgo i miei migliori saluti,` (very formal), `In attesa di un Suo riscontro, La saluto cordialmente.`.
- Email closings informal: `Saluti,` `Un saluto,` `A presto,` `Un caro saluto,` `Cari saluti,` `Ciao,`.
- "Thank you" formal: `La ringrazio della Sua attenzione.` / `Grazie mille.`. Informal: `Grazie!` `Grazie mille!` `Mille grazie!`.

## Standard Italian vs Regional Variants

- This skill targets **Standard Italian (italiano standard / lingua italiana)** as defined by Accademia della Crusca, used in education, media, and software UI nationwide.
- **AVOID mixing in regional/dialectal forms**:
  - Northern: `ho da fare` (Lombard influence) — standard is `devo fare`.
  - Tuscan: `gorgia toscana` aspiration is spoken-only, doesn't affect writing.
  - Southern: `voi` plural formal (Naples), `tenere` for "to have" (Sicily — standard is `avere`).
  - Romanesco / Romaneschismo: `ner` for `nel`, dropped final vowels — spoken-only, never in UI.
- Some "Italian English" loanwords are universal and accepted: `il computer`, `il mouse`, `il file`, `la mail`, `il link`, `lo smartphone`. These are not regional.
- For Switzerland-Italian (Ticino) content: very minor differences (some German loanwords like `il Natel` for phone). The production prompt does NOT have a separate it-CH variant — treat as standard Italian unless user specifies.

## Pronoun Objects and Clitic Placement

Italian object pronouns: `mi, ti, lo, la, ci, vi, li, le, ne` (direct/indirect/partitive).

- **Pre-verbal** for conjugated verbs: `Lo vedo` (I see it), `Te lo dico` (I tell it to you), `Glielo dò` (I give it to him/her).
- **Post-verbal** (attached) for: infinitives, gerunds, imperatives (informal): `Voglio vederlo` (I want to see it), `Dammelo!` (Give it to me!), `Dicendolo, ...` (saying it, ...).
- **Formal Lei imperatives** keep pronoun pre-verbal: `Me lo dia.` (Give it to me, formal).

Double object pronouns: indirect + direct, with `i → e` shift before `lo/la/li/le/ne`:
- `mi + lo = me lo`
- `ti + lo = te lo`
- `gli/le + lo = glielo` (single word!)
- `ci + lo = ce lo`
- `vi + lo = ve lo`

Wrong: `Gli lo dò` → Correct: `Glielo dò` (always combined into one word).

## Tu vs Lei Imperative Forms

Buttons in **infinitive** work for both Lei and tu: `Salvare, Cancellare, Eliminare, Confermare`. PREFERRED for UI consistency.

Imperative for instructions (in help text, errors, dialogs):

| Action | Lei (formal) | tu (informal) |
|--------|--------------|---------------|
| Save | Salvi | Salva |
| Cancel | Cancelli | Cancella |
| Delete | Elimini | Elimina |
| Click | Clicchi | Clicca |
| Confirm | Confermi | Conferma |
| Try again | Riprovi | Riprova |
| Enter | Inserisca | Inserisci |
| Select | Selezioni | Seleziona |
| Open | Apra | Apri |
| Close | Chiuda | Chiudi |

Irregular imperatives — Lei vs tu often differ in stem:
- andare (go): tu `vai`, Lei `vada`
- fare (do): tu `fa'` or `fai`, Lei `faccia`
- dire (say): tu `di'` or `dì`, Lei `dica`
- dare (give): tu `da'` or `dai`, Lei `dia`
- stare (stay): tu `sta'` or `stai`, Lei `stia`
- essere (be): tu `sii`, Lei `sia`
- avere (have): tu `abbi`, Lei `abbia`

## Self-Check Checklist (run before finalizing)

### Accuracy
- [ ] Gender correct (`il problema, il sistema, la soluzione, la piattaforma, l'IA, l'API, il PDF`)
- [ ] Acronym gender from expansion (`la nostra IA`, NOT `il nostro AI`)
- [ ] Adjective + participle agreement in gender AND number
- [ ] Loanword agreement (`i file nuovi`, `il software aggiornato`, `le feature nuove`)
- [ ] Article selection correct (`lo` before s+cons/z/gn/ps/x; `l'` before vowel)
- [ ] `un` (masc) vs `un'` (fem) before vowels
- [ ] Preposition contractions applied (`al, del, nel, sul, dal, alla, della...`)
- [ ] Articulated prepositions in noun phrases with specific nouns (`Errore dell'applicazione`)
- [ ] Conjunction `ed` ONLY before words starting with `e`
- [ ] Subjunctive after `è necessario che / è possibile che / nonostante / sebbene / bisogna che`
- [ ] Accents correct (`è ≠ e`, `città`, `perché`, `po'` not `pò`)
- [ ] FOR vs PER: `per N lingue` (total) vs `per lingua` (rate)
- [ ] All `{variables}` and ICU intact
- [ ] Formality consistent (Lei OR tu) throughout file
- [ ] Domain terminology uses IT meaning (`architettura software, pipeline CI/CD, fonte di riferimento`)
- [ ] No NBSP before `: ; ? !` (Italian uses standard ASCII spacing)

### Naturalness
- [ ] Buttons in infinitive (`Salvare, Eliminare, Annullare`)
- [ ] Status messages nominalized (`Salvataggio..., Caricamento...`)
- [ ] Completion participial (`Pagamento effettuato`, NOT `Pagamento riuscito`)
- [ ] Empty state `Nessun(o/a) X` or `Non ci sono X` (NOT `Niente X` or bare `Vuoto`)
- [ ] Drag-drop verbs: `trascinare / rilasciare` (NOT `permettere` for release)
- [ ] File picker: `seleziona / scegli` (NOT `sfoglia`)
- [ ] No `fa senso` (use `ha senso`)
- [ ] No verbed anglicisms (`caricare` not `uploadare`, `impostare` not `settare`, `eliminare` not `deletare`)
- [ ] False friends in correct sense (`attualmente ≠ actually`, `realizzare ≠ realize`, `libreria ≠ library`)
- [ ] `eccitato` NEVER for "excited" — use `entusiasta`
- [ ] Compound adjectives natural (`con IA`, `contestuale`, `intuitivo`)
- [ ] Business terms adjective form (`traduzione aziendale`)
- [ ] Marketing zero: `Senza X` (NOT `Zero X`)
- [ ] Postnominal adjectives for abstract qualities
- [ ] Compound nouns restructured (`mamme creatrici di contenuti`, NOT `creatrici mamme`)
- [ ] Spatial metaphors adapted (`tra, oltre a, dietro le quinte, entro`)
- [ ] Error ownership: `da parte nostra` (NOT `dalla nostra parte`)
- [ ] Cascading `di` chains simplified (max 2 prepositions)
- [ ] UI labels in prose use `«...»` or capitalization
- [ ] Brand articles omitted on platform destinations
- [ ] Block verb mood consistent
- [ ] Temporal "[YEAR] me" rendered as `io nel YYYY` (NOT `YYYY anni fa`)

## Worked Example

**Source:** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

### Italian (Lei, formal)

Benvenuto! Selezioni il Suo file da caricare. Supportiamo più di 25 formati e lo traduciamo in 5 lingue in {seconds} secondi. Non si preoccupi, può annullare in qualsiasi momento.

### Italian (tu, informal)

Benvenuto! Seleziona il tuo file da caricare. Supportiamo più di 25 formati e lo traduciamo in 5 lingue in {seconds} secondi. Non preoccuparti, puoi annullare in qualsiasi momento.

### Common errors both would catch

- `Per favore seleziona il Suo file` → mixed formality.
- `Sfoglia il file` → use `seleziona / scegli`.
- `25+ formati` → `più di 25 formati`.
- `per 5 lingue` is correct here (FOR/total); `per lingua` would be wrong (PER/rate).
- `{seconds}` without unit → `{seconds} secondi`.
- `un'utente` (if it appeared) → `un utente` (masc, no apostrophe).
- `e elegante` somewhere → `ed elegante` (euphonic ed before `e-`).
- `Pagamento riuscito` somewhere → `Pagamento effettuato`.
