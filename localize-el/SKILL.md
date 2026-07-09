---
name: localize-el
description: Use when translating or localizing UI strings, marketing copy, blogs, documentation, error messages, or any product text into Greek (el / Ελληνικά). Enforces monotonic accent system (only acute ´ since 1982), final sigma ς only at word end, 3-gender × 4-case agreement (ο/η/το × nom/gen/acc/voc), Greek question mark ; (NOT ?) and ano teleia · (NOT period), εσείς/εσύ formality consistency, verb government (μετατρέπω+σε+acc, εξαρτώμαι+από+acc), article contractions (σε+τον=στον), «...» guillemet quotation marks, EUR currency 99,99 €, DD/MM/YYYY dates, ICU one/other plurals, and preservation of Latin-script technical identifiers (Git, API, JSON) inside Greek text.
---

# Localize: Greek (el → Ελληνικά)

Distilled from the production translation prompt. Follow these rules verbatim — they are model-agnostic and produce consistent native-quality Greek output for Greece and Cyprus.

## Scope & Variants

This skill covers **Modern Standard Greek (Νέα Ελληνικά / Δημοτική)** — the standard since 1976 when Katharevousa was officially abolished. Two regional variants both use the same standard:

| Code | Country | Standard | Differences |
|------|---------|----------|-------------|
| **el-GR** | Greece (Ελλάδα) | Demotic Greek | The reference standard. Default if unspecified. |
| **el-CY** | Cyprus (Κύπρος) | Standard Greek written form | Written language is identical to el-GR. Cyprus uses a Greek dialect (Κυπριακή) for speech, but formal writing — UI, docs, contracts — follows mainland Greek. A few lexical differences exist (e.g., **σιενίκι / σιεπί** in Cyprus speech) but these do NOT appear in formal Greek UI. |

**Decision policy:** Translate to el (standard Demotic). For Cyprus-specific products, ask the user if they want any localisms; otherwise output is identical to el-GR.

**What the skill does NOT cover:**
- **Katharevousa** (Καθαρεύουσα) — purist/archaic register, abolished 1976. Never use in modern UI.
- **Polytonic system** (πολυτονικό) — multiple accents (´ ` ῀) + breathing marks (᾿ ῾) + iota subscript (ᾳ ῃ ῳ). Used ONLY for ancient texts, ecclesiastical / Orthodox liturgy, classical scholarship. NEVER for modern UI/marketing/docs.
- **Cypriot Greek dialect** (Κυπριακή διάλεκτος) — spoken variety only.

## Identity Guardrail — Greek is its Own Family

Greek (Ελληνικά) is the sole living member of the **Hellenic** branch of Indo-European — it has NO close living relatives the way Romance, Slavic, or Germanic languages have siblings. Its alphabet is unique and ancestral to Latin and Cyrillic. Do NOT confuse Greek with:

| Confusable | Reality |
|------------|---------|
| Russian / Cyrillic | Different script, different language family. Greek letter Β = beta (B), Cyrillic В = ve (V). Do not mix scripts. |
| Coptic | Egyptian descendant that uses some Greek letters; different language. |
| Macedonian / Bulgarian | Slavic languages, Cyrillic script. NOT Greek despite geographic proximity. |
| Ancient Greek / Koine | Greek's own ancestors. Modern UI = Demotic only. |

Greek's defining features in this skill:
- **Unique alphabet** (24 letters, see below) — never transliterate technical identifiers (Git, API, JSON) into Greek; keep Latin.
- **Three genders, four cases** (no dative; vocative for direct address).
- **Monotonic system** — single acute accent ´ only, since 1982 reform.
- **Final sigma ς** — graphical variant of σ used ONLY at word end.
- **Greek question mark `;`** — looks like a Latin semicolon but is the ερωτηματικό.
- **Ano teleia `·`** — the raised dot, NOT a period, used like English semicolon.

## The Greek Alphabet (24 Letters)

| Upper | Lower | Name | Sound |
|-------|-------|------|-------|
| Α | α | άλφα | a |
| Β | β | βήτα | v (not b — that's μπ) |
| Γ | γ | γάμμα | gh / y (before ε/ι) |
| Δ | δ | δέλτα | ð (voiced th, as in "this") |
| Ε | ε | έψιλον | e |
| Ζ | ζ | ζήτα | z |
| Η | η | ήτα | i |
| Θ | θ | θήτα | θ (voiceless th, as in "thin") |
| Ι | ι | γιώτα | i |
| Κ | κ | κάππα | k |
| Λ | λ | λάμβδα | l |
| Μ | μ | μι | m |
| Ν | ν | νι | n |
| Ξ | ξ | ξι | ks |
| Ο | ο | όμικρον | o |
| Π | π | πι | p |
| Ρ | ρ | ρο | r |
| Σ | σ / **ς** | σίγμα | s (ς only at word end) |
| Τ | τ | ταυ | t |
| Υ | υ | ύψιλον | i |
| Φ | φ | φι | f |
| Χ | χ | χι | x / ç |
| Ψ | ψ | ψι | ps |
| Ω | ω | ωμέγα | o |

**Note**: ι, η, υ, ει, οι all sound /i/ (iotacism). Different spellings reflect ancient distinctions. Do not "simplify" — `υπηρεσία` ≠ `ιπιρεσία`.

## Mindset

> Είσαι ένας εξαιρετικά απαιτητικός Έλληνας συγγραφέας που μισεί τις αφύσικες ελληνικές κατασκευές, όπως οι κυριολεκτικές μεταφράσεις από τα αγγλικά ή οι αδέξιες διατυπώσεις.

Reject literal English calques. Greek is highly inflected — getting gender, case, or article contraction wrong reads as obviously machine-translated. Common English tech loanwords (`email`, `URL`, `API`) stay in Latin script; verbed anglicisms (`κλικάρω`, `σεβάρω`, `λινκάρω`, `απλοουντάρω`) are NOT acceptable.

## Pre-Translation Setup

Lock in before translating:

1. **Formality (εσείς vs εσύ)** — Default to **εσείς** (formal/plural — same verb form) for B2B, government, banking, and most software UI. Use **εσύ** only for explicitly consumer-casual contexts. NEVER mix within a file.
2. **Three genders** — αρσενικό (ο), θηλυκό (η), ουδέτερο (το). Articles, adjectives, past participles MUST agree.
3. **Four cases** — ονομαστική (nom), γενική (gen), αιτιατική (acc), κλητική (voc). Selection depends on verb/preposition. Dative is archaic (replaced by σε + acc or genitive).
4. **Monotonic accent only** — single acute ´ on stressed syllable. NEVER use polytonic ` ῀ ᾿ ῾.
5. **Final sigma rule** — `ς` only at the end of a word; `σ` everywhere else. Get this wrong and the text looks broken.
6. **No articles like English** — Greek HAS definite articles (ο/η/το) but they are used MORE than English "the". Abstract nouns, possessives, generic statements all need articles.
7. **Placeholders** — Preserve `{variables}` and ICU plural syntax (`one / other`) exactly.

## Register Auto-Detection (run after Pre-Translation Setup)

Greek formality is realized through verb conjugation and possessive pronouns:

| Register | Pronoun | Possessive | Imperative ending | Example |
|----------|---------|------------|---------------------|---------|
| Formal | εσείς | σας | -ετε / -είτε / -στε | Μπορείτε να αλλάξετε τις ρυθμίσεις σας |
| Informal | εσύ | σου | -ε | Μπορείς να αλλάξεις τις ρυθμίσεις σου |

**εσείς** = both formal 2-person AND genuine plural. In UI it serves as the formal address.

### Formal source signals → output εσείς / σας
- Hedging / polite modals: "please", "kindly", "we recommend"
- Passive / impersonal: "users are advised", "it is recommended"
- No contractions: "do not", "cannot", "we will"
- Domain vocabulary: legal, financial, healthcare, regulatory, B2B SaaS, banking
- Third-person / distance: "the user must", "customers should"
- Brand voice: bank, insurance, government, enterprise

### Informal source signals → output εσύ / σου
- Contractions: "don't", "you'll", "we're"
- Casual greetings: "hey", "hi there", "yo"
- Consumer-app voice: gaming, social, lifestyle, dating, fitness, kids
- Second-person directness, exclamations, emoji

### Mixed / ambiguous source → default to εσείς
εσείς reads slightly distant but professional; εσύ can read as too casual in B2B contexts.

### Explicit user override
If the user says "use εσύ" / "use εσείς" / "formal" / "casual", their instruction wins.

After detection: keep the chosen form consistent. NEVER mix εσείς/εσύ across verbs, possessives, OR imperatives in one file.

| Wrong (mixed) | Correct |
|---------------|---------|
| `Θέλετε να διαγράψεις` | **`Θέλετε να διαγράψετε`** (both formal) OR **`Θέλεις να διαγράψεις`** (both informal) |
| `Μεταφορτώστε + Αναζήτησε` | **`Μεταφορτώστε + Αναζητήστε`** (both formal) |
| `Τα αρχεία σου ... Αποθηκεύστε` | **`Τα αρχεία σας ... Αποθηκεύστε`** (possessive must match) |

## Critical Hard Rules

These have no English analogue. The model gets them wrong by default.

### A. Monotonic accent system (μονοτονικό) — severity 2.5

Since the 1982 reform, Modern Greek uses ONE accent only: the **acute ´**. The polytonic system (multiple accents, breathing marks) belongs to ancient/ecclesiastical texts.

| Wrong (polytonic) | Correct (monotonic) |
|-------------------|----------------------|
| `ἄνθρωπος` (smooth breathing + acute) | **`άνθρωπος`** |
| `Ἑλλάς` (rough breathing + acute) | **`Ελλάς`** |
| `οἶκος` (smooth breathing + circumflex) | **`οίκος`** |
| `αὐτός` (rough breathing) | **`αυτός`** |

**Acute placement is mandatory** on the stressed syllable of every word ≥ 2 syllables:

| Wrong (missing accent) | Correct |
|------------------------|---------|
| `αρχειο` | **`αρχείο`** (stress on -χεί-) |
| `συστημα` | **`σύστημα`** (stress on σύ-) |
| `πλατφορμα` | **`πλατφόρμα`** |
| `αποθηκευση` | **`αποθήκευση`** |

**Single-syllable words** generally take NO accent: `το`, `μου`, `σε`, `και`, `ή`, `δεν`, `μη`, `να`, `θα`. Exception: ή (or) keeps its accent to distinguish from η (the/she).

**Dialytika (¨)** — used over ι or υ to indicate it is pronounced as a separate syllable (NOT a diphthong):

| Word | Pronunciation |
|------|---------------|
| `άυπνος` | dipthong αυ → /afnos/ |
| `αϋπνία` | separate syllables α-ϋ-πνία → /aipnia/ |
| `προϊόν` | separate syllables προ-ϊ-όν |
| `Μαΐου` | μα-ΐ-ου |

When stress falls on the second vowel of what would be a diphthong, the dialytika is implicit in the acute accent on the second vowel (`Μαΐου` has both ¨ AND ´ combined).

### B. Final sigma — ς only at word end (severity 3.0 — HIGHEST)

Greek has two graphical forms of sigma:
- **σ** — used everywhere EXCEPT word-final position
- **ς** — used ONLY at the end of a word

NEVER mix them. This is the single most distinctive Greek typography rule.

| Wrong | Correct |
|-------|---------|
| `σπίτις` | **`σπίτι`** (no ς in this word — wrong character) |
| `θάλασςας` | **`θάλασσας`** (σ inside, ς only at end) |
| `χρηστης` (missing final ς) | **`χρήστης`** |
| `ςύστημα` | **`σύστημα`** (ς can NEVER start a word) |
| `έλληνας` | (correct — final ς) |
| `ελλήνeς` (mid-word ς) | **`Έλληνες`** (σ mid-word) |

Compound words: if a sigma falls at the END of the first component but INSIDE the full word, it depends on whether the compound is hyphenated. In standard Greek compounds without hyphen → use σ: `θάλασσα` not `θάλαςσα`.

### C. Greek question mark ` ; ` and ano teleia ` · ` (severity 2.5)

Greek punctuation looks confusing because of overlap with Latin:

| Mark | Greek name | Looks like | Function |
|------|------------|------------|----------|
| `;` | ερωτηματικό | Latin semicolon | **Greek question mark** |
| `·` | άνω τελεία (U+0387) | Raised dot | **Greek semicolon** (mid-sentence pause stronger than comma, weaker than period) |
| `.` | τελεία | period | Period / full stop |
| `,` | κόμμα | comma | Comma |
| `:` | διπλή τελεία | colon | Colon |

**Critical:**
- **NEVER use `?` in Greek text** — use `;`
- **NEVER use `;` as English semicolon** — use `·` (ano teleia)
- **The ano teleia `·` is NOT a question mark** — that's `;`

| Wrong | Correct |
|-------|---------|
| `Θέλετε να συνεχίσετε?` | **`Θέλετε να συνεχίσετε;`** |
| `Τι είναι αυτό?` | **`Τι είναι αυτό;`** |
| `Πατήστε εδώ; θα σας βοηθήσει` (question? mid-sentence) | **`Πατήστε εδώ· θα σας βοηθήσει`** (ano teleia for pause) |
| `Αρχείο; φάκελος; ή σύνδεσμος;` (multiple "questions") | **`Αρχείο, φάκελος ή σύνδεσμος;`** (one question mark only at the end) |

### D. Verb government — verbs require specific preposition + case (severity 2.5)

Many Greek verbs require a SPECIFIC preposition + case combination for their complement. Using the wrong one is a grammar error, not a stylistic choice.

| Verb | Requires | Wrong | Correct |
|------|----------|-------|---------|
| **μετατρέπω** (convert) | σε + acc | `μετατρέπω PDF` | **`μετατρέπω σε PDF`** |
| **αναφέρομαι** (refer) | σε + acc | `αναφέρεται το αρχείο` | **`αναφέρεται στο αρχείο`** |
| **εξαρτώμαι** (depend) | από + acc | `εξαρτάται τις ρυθμίσεις` | **`εξαρτάται από τις ρυθμίσεις`** |
| **αποτελούμαι** (consist) | από + acc | `αποτελείται τρία μέρη` | **`αποτελείται από τρία μέρη`** |
| **συνδέομαι** (connect) | με + acc | `συνδέεται τον διακομιστή` | **`συνδέεται με τον διακομιστή`** |
| **ενδιαφέρομαι** (be interested) | για + acc | `ενδιαφέρεται τα αποτελέσματα` | **`ενδιαφέρεται για τα αποτελέσματα`** |
| **βασίζομαι** (rely) | σε + acc | `βασίζεται τα δεδομένα` | **`βασίζεται στα δεδομένα`** (σε + τα → στα) |
| **πληροφορώ** (inform) | για + acc | `ενημέρωση τις αλλαγές` | **`ενημέρωση για τις αλλαγές`** |
| **χρειάζομαι** (need) | accusative (no preposition) | — | `χρειάζομαι βοήθεια` |
| **απαντώ** (answer/reply) | σε + acc | `απαντώ το μήνυμα` | **`απαντώ στο μήνυμα`** |

### E. Article contractions (σε + article) — severity 2.0

**ALWAYS contract** σε with definite articles. Never leave them as separate words.

| σε + article | Contracted form | Example |
|--------------|------------------|---------|
| σε + τον (masc acc sg) | **στον** | στον χρήστη |
| σε + την (fem acc sg) | **στην** | στην πλατφόρμα |
| σε + το (neut acc sg) | **στο** | στο αρχείο |
| σε + τους (masc acc pl) | **στους** | στους χρήστες |
| σε + τις (fem acc pl) | **στις** | στις ρυθμίσεις |
| σε + τα (neut acc pl) | **στα** | στα αρχεία |

| Wrong (uncontracted) | Correct (contracted) |
|----------------------|----------------------|
| `σε το σύστημα` | **`στο σύστημα`** |
| `σε την πλατφόρμα` | **`στην πλατφόρμα`** |
| `σε τον χρήστη` | **`στον χρήστη`** |
| `σε τα αρχεία` | **`στα αρχεία`** |

## The Three Genders

Three genders are visible in the definite article and the noun ending.

| Gender | Article (nom sg) | Indefinite | Common endings | Examples |
|--------|-------------------|------------|------------------|----------|
| Masculine (αρσενικό) | **ο** | ένας | -ος, -ης, -ας, -έας | χρήστης, φάκελος, λογαριασμός |
| Feminine (θηλυκό) | **η** | μία / μια | -α, -η, -ση | πλατφόρμα, υπηρεσία, αναζήτηση |
| Neuter (ουδέτερο) | **το** | ένα | -ο, -ι, -μα | αρχείο, παιδί, σύστημα |

### Gender of common IT nouns (memorize)

| Masculine (ο) | Feminine (η) | Neuter (το) |
|---------------|--------------|-------------|
| **ο χρήστης** | **η πλατφόρμα** | **το αρχείο** |
| **ο φάκελος** | **η υπηρεσία** | **το σύστημα** |
| **ο λογαριασμός** | **η εφαρμογή** | **το πρόγραμμα** |
| **ο σύνδεσμος** | **η βάση δεδομένων** | **το email** |
| **ο διακομιστής** | **η αναζήτηση** | **το μήνυμα** |
| **ο κωδικός** | **η σελίδα** | **το έγγραφο** |
| **ο υπολογιστής** | **η ρύθμιση** | **το URL** |
| **ο ιστότοπος** | **η ενημέρωση** | **το PDF** |
| **ο διαχειριστής** | **η γλώσσα** | **το όνομα** |
| **ο τομέας** | **η μετάφραση** | **το κουμπί** |

**Loanwords default to NEUTER**: `το email`, `το URL`, `το API`, `το Wi-Fi`, `το PDF`.

| Wrong | Correct | Why |
|-------|---------|-----|
| `ο πλατφόρμα` | **`η πλατφόρμα`** | πλατφόρμα is feminine |
| `η αρχείο` | **`το αρχείο`** | αρχείο is neuter |
| `το χρήστης` | **`ο χρήστης`** | χρήστης is masculine |
| `ο σύστημα` | **`το σύστημα`** | -μα ending → always neuter |
| `η πρόγραμμα` | **`το πρόγραμμα`** | -μα ending → always neuter |
| `ο email` | **`το email`** | Loanwords → neuter |

## The Four Cases

| # | Case | Greek | Question | When to use |
|---|------|-------|----------|-------------|
| 1 | Nominative | ονομαστική | ποιος; (who/what) | Subject of sentence |
| 2 | Genitive | γενική | ποιανού; (of whom/what) | Possession, "of", after some prepositions |
| 3 | Accusative | αιτιατική | ποιον; (whom/what) | Direct object, after most prepositions |
| 4 | Vocative | κλητική | — | Direct address only |

**Note:** Modern Greek has no productive dative case. Where ancient Greek used dative, modern Greek uses σε + accusative or genitive of possession.

### Definite article — full declension

| Case | Masc sg | Fem sg | Neut sg | Masc pl | Fem pl | Neut pl |
|------|---------|--------|---------|---------|--------|---------|
| Nom | **ο** | **η** | **το** | **οι** | **οι** | **τα** |
| Gen | **του** | **της** | **του** | **των** | **των** | **των** |
| Acc | **τον** (or το before vowel) | **την** (or τη) | **το** | **τους** | **τις** | **τα** |
| Voc | — | — | — | — | — | — |

Vocative has no article — direct address uses bare noun in vocative case: `Κύριε Παπαδόπουλε,` not `Ο κύριε Παπαδόπουλε,`.

### Common preposition + case pairings

| Preposition | Case | Example |
|-------------|------|---------|
| **σε** (to/in/at) | accusative | στο αρχείο, στον χρήστη |
| **για** (for/about) | accusative | για τον χρήστη, για το θέμα |
| **με** (with) | accusative | με τον φάκελο |
| **από** (from/by) | accusative | από τον διακομιστή |
| **κατά** (during/against) | accusative | κατά τη διάρκεια |
| **μετά** (after) | accusative | μετά την αποθήκευση |
| **πριν** (before) | accusative | πριν τη μετάφραση |
| **χωρίς** (without) | accusative | χωρίς λογαριασμό |
| **μέχρι** (until) | accusative | μέχρι την Παρασκευή |
| **παρά** (despite) | accusative | παρά τις προσπάθειες |
| **μεταξύ** (between/among) | genitive | μεταξύ των χρηστών |
| **λόγω** (due to) | genitive | λόγω σφάλματος |
| **εξαιτίας** (because of) | genitive | εξαιτίας της καθυστέρησης |
| **εκτός** (except) | genitive | εκτός των ενεργών |
| **χάριν** (for the sake of) | genitive | χάριν συντομίας |

### Common case errors

| Wrong | Correct | Why |
|-------|---------|-----|
| `για ο χρήστης` | **`για τον χρήστη`** | accusative after για |
| `από η πλατφόρμα` | **`από την πλατφόρμα`** | accusative after από |
| `του πλατφόρμα` | **`της πλατφόρμας`** | genitive must agree (fem) |
| `μεταξύ τους χρήστες` | **`μεταξύ των χρηστών`** | genitive after μεταξύ |
| `με ο φάκελος` | **`με τον φάκελο`** | accusative after με |
| `λόγω η καθυστέρηση` | **`λόγω της καθυστέρησης`** | genitive after λόγω |

## Adjective Agreement — gender + number + case (severity 2.0)

Adjectives MUST agree with the noun in gender, number, AND case. The order is **Article + Adjective + Noun**, and ALL THREE must match.

| Wrong | Correct | Why |
|-------|---------|-----|
| `η νέο υπηρεσία` | **`η νέα υπηρεσία`** | feminine noun → feminine adjective |
| `το νέος αρχείο` | **`το νέο αρχείο`** | neuter noun → neuter adjective |
| `οι νέος χρήστες` | **`οι νέοι χρήστες`** | plural noun → plural adjective |
| `νέο αρχείο` (no article) | **`το νέο αρχείο`** | include article |
| `η νέα φάκελος` | **`ο νέος φάκελος`** | φάκελος is masculine |
| `στο μεγάλο πλατφόρμα` | **`στη μεγάλη πλατφόρμα`** | fem acc sg agreement |

### Adjective endings (basic -ος / -η / -ο pattern)

| Case | Masc sg | Fem sg | Neut sg | Masc pl | Fem pl | Neut pl |
|------|---------|--------|---------|---------|--------|---------|
| Nom | νέος | νέα | νέο | νέοι | νέες | νέα |
| Gen | νέου | νέας | νέου | νέων | νέων | νέων |
| Acc | νέο | νέα | νέο | νέους | νέες | νέα |

## Plural Formation by Gender (severity 1.5)

Plural endings vary by gender and the noun's declension:

| Gender | Singular ending | Plural ending | Example |
|--------|------------------|----------------|---------|
| Masc | -ος | -οι | φάκελος → φάκελοι |
| Masc | -ης | -ες | χρήστης → χρήστες |
| Masc | -ας | -ες | άντρας → άντρες |
| Fem | -α | -ες | πλατφόρμα → πλατφόρμες |
| Fem | -η | -ες | υπηρεσία → υπηρεσίες |
| Fem | -ση | -σεις | ρύθμιση → ρυθμίσεις |
| Neut | -ο | -α | αρχείο → αρχεία |
| Neut | -ι | -ια | παιδί → παιδιά |
| Neut | **-μα** | **-ματα** | σύστημα → συστήματα |

| Wrong | Correct | Why |
|-------|---------|-----|
| `τα αρχείος` | **`τα αρχεία`** | -ο → -α (neuter) |
| `οι υπηρεσίας` | **`οι υπηρεσίες`** | -α → -ες (feminine) |
| `τα συστήμα` | **`τα συστήματα`** | -μα → -ματα (neuter) |
| `τα προγράμμα` | **`τα προγράμματα`** | -μα → -ματα |
| `οι φάκελες` | **`οι φάκελοι`** | -ος (masc) → -οι |

## Subject-Verb Agreement

Verbs agree with the subject in person AND number.

| Wrong | Correct | Why |
|-------|---------|-----|
| `Ο χρήστης αποθηκεύουν` | **`Ο χρήστης αποθηκεύει`** | singular subj → singular verb |
| `Οι χρήστες αποθηκεύει` | **`Οι χρήστες αποθηκεύουν`** | plural subj → plural verb |
| `Το σύστημα λειτουργούν` | **`Το σύστημα λειτουργεί`** | neuter singular → 3sg |
| `Τα αρχεία αποθηκεύεται` | **`Τα αρχεία αποθηκεύονται`** | neuter plural → 3pl passive |

## Verb Aspect — perfective vs imperfective

Greek verbs encode whether an action is **completed (συνοπτικό/τέλειο aspect)** or **ongoing/repeated (μη συνοπτικό/ατελές aspect)**.

| Aspect | Use for | UI examples |
|--------|---------|-------------|
| **Perfective** | Single completed action; buttons | αποθηκεύσετε, διαγράψετε, ολοκληρωθεί, σταλεί |
| **Imperfective** | Ongoing; in-progress; repeated; status | αποθηκεύεται, φορτώνεται, επεξεργάζεται |

**Status messages → imperfective + impersonal** or `Γίνεται` + verbal noun:

| Wrong (1st person) | Correct (impersonal) | Why |
|--------------------|----------------------|-----|
| `Αποθηκεύω...` | **`Αποθήκευση... / Γίνεται αποθήκευση...`** | impersonal — never first person |
| `Φορτώνω...` | **`Φόρτωση... / Γίνεται φόρτωση...`** | impersonal |
| `Αναζητώ...` | **`Αναζήτηση... / Γίνεται αναζήτηση...`** | impersonal |
| `Επεξεργάζομαι το αρχείο` | **`Γίνεται επεξεργασία του αρχείου`** | impersonal |

**Completion messages → passive aorist** (3rd person):

| Wrong | Correct |
|-------|---------|
| `Τέλεια! Η μετάφρασή σας ολοκληρώθηκε.` | **`Η μετάφραση ολοκληρώθηκε`** |
| `Ωραία! Όλα αποθηκεύτηκαν.` | **`Αποθηκεύτηκαν όλα`** |
| `Έγινε αποθήκευση επιτυχώς!` | **`Αποθηκεύτηκε`** |

**Failure messages → noun + verb OR `Αποτυχία` + genitive verbal noun**:

| Wrong | Correct |
|-------|---------|
| `Παρουσιάστηκε σφάλμα κατά την αποθήκευση` (verbose) | **`Η αποθήκευση απέτυχε / Αποτυχία αποθήκευσης`** |
| `Η μετάφραση δεν πέτυχε` | **`Η μετάφραση απέτυχε / Αποτυχία μετάφρασης`** |

## Clitic Pronoun Placement

Weak object pronouns (clitics) — με, σε, τον, την, το, μας, σας, τους — have fixed positions:

| Construction | Position | Example |
|--------------|----------|---------|
| Indicative / subjunctive | **BEFORE** verb | `Το αποθηκεύω` (I save it) |
| Negative | **BEFORE** verb (after δεν/μην) | `Δεν το αποθηκεύω` |
| Imperative | **AFTER** verb | `Αποθηκεύστε το` (Save it) |
| With να / θα / ας | **BEFORE** main verb | `Θα το αποθηκεύσω` (I will save it) |

| Wrong | Correct | Why |
|-------|---------|-----|
| `Αποθηκεύω το` | **`Το αποθηκεύω`** | clitic precedes indicative |
| `Το αποθηκεύστε` | **`Αποθηκεύστε το`** | clitic follows imperative |
| `Δεν αποθηκεύω το` | **`Δεν το αποθηκεύω`** | clitic between δεν and verb |
| `Θα αποθηκεύσω το` | **`Θα το αποθηκεύσω`** | clitic between θα and verb |

## ICU Plurals — `one / other` (severity 1.5)

Greek has only TWO plural categories — far simpler than Slavic languages.

```icu
{count, plural,
  one {# αρχείο}      // 1
  other {# αρχεία}}   // 0, 2, 3, 4, 5, 100, 1000, decimals
```

Common ICU patterns:

```icu
{n, plural, one {# λεπτό} other {# λεπτά}}
{n, plural, one {# δευτερόλεπτο} other {# δευτερόλεπτα}}
{n, plural, one {# μέρα} other {# μέρες}}
{n, plural, one {# χρήστης} other {# χρήστες}}
{n, plural, one {# μήνυμα} other {# μηνύματα}}
{n, plural, one {# πρόγραμμα} other {# προγράμματα}}
```

**Other branch must use the correct plural form** (matching gender's plural ending):

| Wrong | Correct |
|-------|---------|
| `other {# αρχείο}` (using singular) | **`other {# αρχεία}`** |
| `other {# υπηρεσία}` | **`other {# υπηρεσίες}`** |
| `other {# σύστημα}` | **`other {# συστήματα}`** |

## UI Conventions

### Buttons — noun OR formal imperative

Two acceptable styles. Pick ONE per file and stick with it:

| Noun (verbal noun) | Formal imperative |
|---------------------|----------------------|
| **Αποθήκευση** | **Αποθηκεύστε** |
| **Διαγραφή** | **Διαγράψτε** |
| **Μεταφόρτωση** | **Μεταφορτώστε** |
| **Λήψη** | **Κατεβάστε** (formal: Πραγματοποιήστε λήψη) |
| **Ακύρωση** | **Ακυρώστε** |
| **Αναζήτηση** | **Αναζητήστε** |
| **Σύνδεση** | **Συνδεθείτε** |

Verbal noun (Αποθήκευση) is preferred for compact UI — works with both εσείς and εσύ.

| Wrong | Correct |
|-------|---------|
| `Αποθηκεύσα` (1st person past) | **`Αποθήκευση / Αποθηκεύστε`** |
| `Σώσε` (informal singular) | **`Αποθήκευση / Αποθηκεύστε`** |
| `Διαγράφω` (1st person present) | **`Διαγραφή / Διαγράψτε`** |
| `Ανέβασμα` (colloquial) | **`Μεταφόρτωση`** |
| `Κατέβασμα` (colloquial) | **`Λήψη`** |

### Status messages — impersonal voice

NEVER first-person. Use **verbal noun** or **`Γίνεται` + verbal noun** or **3rd person passive**.

| Wrong | Correct |
|-------|---------|
| `Αποθηκεύω...` | **`Αποθήκευση... / Γίνεται αποθήκευση...`** |
| `Φορτώνω...` | **`Φόρτωση... / Γίνεται φόρτωση...`** |
| `Επεξεργάζομαι...` | **`Επεξεργασία... / Γίνεται επεξεργασία...`** |
| `Συνδέομαι στον διακομιστή` | **`Σύνδεση στον διακομιστή... / Γίνεται σύνδεση...`** |

### Completion messages — concise passive aorist

Drop interjections (`Τέλεια!`, `Ωραία!`). Drop redundant adverbs (`επιτυχώς`). Drop exclamations unless source warrants.

| Wrong | Correct |
|-------|---------|
| `Τέλεια! Η μετάφρασή σας ολοκληρώθηκε.` | **`Η μετάφραση ολοκληρώθηκε`** |
| `Ωραία! Όλα αποθηκεύτηκαν.` | **`Αποθηκεύτηκαν όλα`** |
| `Το αρχείο σας αποθηκεύτηκε με επιτυχία!` | **`Το αρχείο αποθηκεύτηκε`** |

### Empty state messages — concise

Use `Κανένα/Καμία/Κανένας` + noun OR `Δεν` + verb.

| Wrong | Correct |
|-------|---------|
| `Δεν βρέθηκαν αποτελέσματα στην αναζήτησή σας` | **`Κανένα αποτέλεσμα`** |
| `Δεν έχετε ακόμα κανένα αρχείο` | **`Κανένα αρχείο ακόμα`** |
| `Η λίστα είναι κενή προς το παρόν` | **`Κενή λίστα`** |

### Drag and drop

| English | Greek |
|---------|-------|
| drag | **σύρετε** |
| drop | **αφήστε** |
| release | **αφήστε** |
| browse (file picker) | **επιλέξτε** (action verb), NOT **περιηγηθείτε** (navigation) |

| Wrong | Correct |
|-------|---------|
| `κάντε drag` | **`σύρετε`** |
| `κάντε drop` | **`αφήστε`** |
| `Drag εδώ` | **`Σύρετε τα αρχεία εδώ`** |
| `Αφήστε για release` | **`Αφήστε για μεταφόρτωση`** |
| `Περιηγηθείτε στα αρχεία` (for file picker) | **`Επιλέξτε αρχεία`** |

### Validation messages — distinct verb moods

| Type | Mood | Example |
|------|------|---------|
| Field validation | indicative | `Το πεδίο είναι υποχρεωτικό / Μη έγκυρη μορφή` |
| Action instruction | imperative (formal) | `Εισαγάγετε μια έγκυρη τιμή / Επιλέξτε τουλάχιστον μία γλώσσα` |
| State description | impersonal | `Δεν ήταν δυνατή η σύνδεση / Προέκυψε σφάλμα` |

### Quantity expressions

| Wrong | Correct |
|-------|---------|
| `25+ γλώσσες` | **`πάνω από 25 γλώσσες`** |
| `+{count} ακόμα` | **`και {count} ακόμα`** |
| `25 ή περισσότερες γλώσσες` (literal) | **`πάνω από 25 γλώσσες / 25 ή και περισσότερες γλώσσες`** |

### Rate / "per" expressions

| Wrong | Correct |
|-------|---------|
| `περ μήνα` | **`ανά μήνα / το μήνα`** |
| `10 ευρώ/μήνα` | **`10 ευρώ ανά μήνα`** |
| `περ χρήστη` | **`ανά χρήστη`** |
| `για ένα αρχείο` (per file, literal) | **`ανά αρχείο`** |

### UI label completeness — complete noun phrases

| Wrong (bare adjective) | Correct |
|------------------------|---------|
| `Εναλλακτική` | **`Εναλλακτική ανίχνευση`** |
| `Αυτόματη` | **`Αυτόματη λειτουργία`** |
| `Προηγμένες` | **`Προηγμένες ρυθμίσεις`** |

### Definite article usage — Greek requires MORE articles than English

Greek includes definite articles in many places English drops them:

| Context | Wrong (no article) | Correct |
|---------|--------------------|---------|
| Abstract noun | `Ποιότητα είναι σημαντική` | **`Η ποιότητα είναι σημαντική`** |
| Possessive | `αρχείο μου` | **`το αρχείο μου`** (article + noun + possessive) |
| Generic statement | `Χρήστες χρειάζονται...` | **`Οι χρήστες χρειάζονται...`** |
| Adjective + noun | `Νέο αρχείο δημιουργήθηκε` | **`Το νέο αρχείο δημιουργήθηκε`** |
| Country names | `Ελλάδα είναι ωραία` | **`Η Ελλάδα είναι ωραία`** |
| Languages | `Μιλώ Ελληνικά` (sometimes OK) | **`Μιλώ τα Ελληνικά`** (more formal) |

**Possessive structure**: article + noun + possessive pronoun (`το αρχείο μου`, NOT `μου αρχείο`).

## Punctuation, Numbers, Dates, Currency

| Item | Greek |
|------|-------|
| Decimal separator | **`,`** (comma) |
| Thousands separator | **`.`** (period) |
| Example number | `1.234,56` |
| Currency | `99,99 €` or `1.234,56 €` (number + space + symbol) |
| Date (numeric) | **`15/01/2024`** (DD/MM/YYYY with slashes) — NEVER US format |
| Date (long) | `15 Ιανουαρίου 2024` (genitive of month name) |
| Time | **`14:30`** (24-hour) or `2:30 μ.μ.` (12-hour with π.μ./μ.μ.) |
| Question mark | **`;`** (Greek ερωτηματικό) |
| Greek semicolon | **`·`** (ano teleia, U+0387) |
| Quotation marks | **`«...»`** (guillemets, NO inside spaces) |
| Nested quotation marks | **`"..."`** (curly double) — but very rare; prefer rephrasing |
| Em-dash | **`—`** with spaces (lists, ranges, dialogue) |

| Wrong | Correct |
|-------|---------|
| `"Αποθήκευση"` (English quotes) | **`«Αποθήκευση»`** |
| `1,234.56` (US format) | **`1.234,56`** |
| `01/15/2024` | **`15/01/2024`** |
| `€99.99` | **`99,99 €`** |
| `99.99€` (no space, period decimal) | **`99,99 €`** |
| `2:30 PM` | **`14:30 / 2:30 μ.μ.`** |
| `15 Ιανουάριος 2024` (nominative of month) | **`15 Ιανουαρίου 2024`** (genitive — "of January") |

### Greek months — always GENITIVE in dates

When stating "the 15th of January", the month MUST be in genitive case. Months can be capitalized in formal contexts but lowercase is standard:

| Nominative | Genitive (used in dates) |
|------------|--------------------------|
| Ιανουάριος | **Ιανουαρίου** |
| Φεβρουάριος | **Φεβρουαρίου** |
| Μάρτιος | **Μαρτίου** |
| Απρίλιος | **Απριλίου** |
| Μάιος | **Μαΐου** (note dialytika on ΐ) |
| Ιούνιος | **Ιουνίου** |
| Ιούλιος | **Ιουλίου** |
| Αύγουστος | **Αυγούστου** |
| Σεπτέμβριος | **Σεπτεμβρίου** |
| Οκτώβριος | **Οκτωβρίου** |
| Νοέμβριος | **Νοεμβρίου** |
| Δεκέμβριος | **Δεκεμβρίου** |

### Greek days of week (lowercase in running text)

All meaningful: literally "second", "third", etc.

| Greek | Meaning | English |
|-------|---------|---------|
| Δευτέρα | "second [day]" | Monday |
| Τρίτη | "third [day]" | Tuesday |
| Τετάρτη | "fourth [day]" | Wednesday |
| Πέμπτη | "fifth [day]" | Thursday |
| Παρασκευή | "preparation" | Friday |
| Σάββατο | "Sabbath" | Saturday |
| Κυριακή | "Lord's day" | Sunday |

## Comma Rules — differ from English

| Before | Comma? |
|--------|--------|
| **και** (and) | **NO** |
| **ή** (or) | **NO** |
| **ούτε ... ούτε** (neither ... nor) | NO between, but separating commas elsewhere |
| **που** (that, relative) | depends — restrictive: NO; non-restrictive: YES |
| **ότι** (that, subordinating) | **YES** |
| **αν / εάν** (if) | **YES** |
| **γιατί / επειδή** (because) | **YES** |
| **όταν** (when) | **YES** |
| **ενώ** (while) | **YES** |
| **αλλά / όμως** (but) | **YES** |

| Wrong | Correct |
|-------|---------|
| `Επιλέξτε αρχείο, ή φάκελο` | **`Επιλέξτε αρχείο ή φάκελο`** |
| `Αποθηκεύστε, και κλείστε` | **`Αποθηκεύστε και κλείστε`** |
| `Ο χρήστης που είδαμε χθες είναι...` (restrictive — no commas) | (correct) |
| `Προσέξτε όταν αποθηκεύετε` | **`Προσέξτε, όταν αποθηκεύετε`** |
| `Δεν μπόρεσε γιατί έλειπε αρχείο` | **`Δεν μπόρεσε, γιατί έλειπε αρχείο`** |

## Terminology

### Preferred Greek terms for UI

| English | Preferred | Avoid (colloquial / anglicism) |
|---------|-----------|--------------------------------|
| Click | **κάντε κλικ / πατήστε** | κλικάρω, κλίκαρε |
| Save | **αποθήκευση / αποθηκεύστε** | σώσιμο, σεβάρω |
| Delete | **διαγραφή / διαγράψτε** | σβήσιμο |
| Upload | **μεταφόρτωση** | ανέβασμα, απλοουντάρω |
| Download | **λήψη** | κατέβασμα |
| Log in | **σύνδεση** | λογκίνω, λογκίν |
| Log out | **αποσύνδεση** | λογκάουτ |
| Search | **αναζήτηση / αναζητήστε** | σερτς |
| Cancel | **ακύρωση / ακυρώστε** | κάνσελ |
| Convert | **μετατροπή / μετατρέψτε** | κονβέρτω |
| Settings | **ρυθμίσεις** | σετίνγκς |
| User | **χρήστης** | γιούζερ |
| File | **αρχείο** | φάιλ |
| Folder | **φάκελος** | φόλντερ |
| Dashboard | **πίνακας ελέγχου** | ταμπλό, dashboard |
| Account | **λογαριασμός** | ακάουντ |
| Link | **σύνδεσμος** | λινκ |
| Browser | **πρόγραμμα περιήγησης** | μπράουζερ |
| Email | **email / ηλεκτρονικό ταχυδρομείο** | (email is accepted) |
| Forward | **προωθώ** | φορβαρντάρω |
| Connect | **συνδέω** | λινκάρω |

### Greek words ARE English words (etymological reclamation)

Many English tech terms ARE Greek loanwords. Use the Greek form, not the English transliteration:

| English (Greek origin) | Greek form | NOT |
|------------------------|------------|------|
| technology | **τεχνολογία** | τεκνόλοτζι |
| system | **σύστημα** | σίστεμ |
| program | **πρόγραμμα** | προγκράμ |
| problem | **πρόβλημα** | προμπλέμ |
| idea | **ιδέα** | αϊντία |
| philosophy | **φιλοσοφία** | φιλοσόφι |
| athlete | **αθλητής** | άθλητ |
| analysis | **ανάλυση** | ανάλισις |
| synthesis | **σύνθεση** | σίνθεσις |
| dialogue | **διάλογος** | ντάιαλογκ |
| democracy | **δημοκρατία** | ντεμοκράσι |
| crisis | **κρίση** | κράϊσις |
| dynamic | **δυναμικός** | ντάιναμικ |
| automatic | **αυτόματος** | οτομάτικ |
| chronological | **χρονολογικός** | κρονολότζικαλ |

### Brand names

- Foreign tech brands (`OneSky`, `Slack`, `Google`, `Microsoft`) stay in Latin script. NEVER decline them in cases.
- Gender assignment: take gender from implied Greek noun (`η πλατφόρμα OneSky` → fem from πλατφόρμα; `η εταιρεία Microsoft` → fem from εταιρεία; `το OneSky` → default neuter as standalone).
- `στο OneSky` (NOT `στον OneSky` — bare brand defaults to neuter).

## Calque / Anti-Pattern Blocklist

### A. Idiom calques

| Wrong (literal) | Correct (natural Greek) | Why |
|-----------------|--------------------------|-----|
| `Break a leg` → `Σπάσε ένα πόδι` | **`Καλή επιτυχία! / Να τα πας καλά!`** | Native Greek good luck |
| `Piece of cake` → `Κομμάτι κέικ` | **`Παιχνιδάκι / Πάρα πολύ εύκολο`** | Native idiom |
| `It's raining cats and dogs` → `Βρέχει γάτες και σκύλους` | **`Βρέχει καρεκλοπόδαρα`** | Greek heavy-rain idiom |
| `War stories` → `Ιστορίες πολέμου` | **`Εμπειρίες από δύσκολες καταστάσεις / Ιστορίες από τα χαρακώματα`** | Figurative — anecdotes about struggles |
| `Eating your own dogfood` → literal | **`Χρησιμοποιώ το δικό μου προϊόν`** | Translate the concept |
| `Low-hanging fruit` → literal | **`Εύκολη νίκη / Εύκολος στόχος`** | Translate the meaning |
| `At the end of the day` → `Στο τέλος της ημέρας` | **`Τελικά / Ουσιαστικά`** | Greek idiom |
| `Source of truth` → `πηγή αλήθειας` | **`αξιόπιστη πηγή δεδομένων`** | Industry term |
| `Game changer` → `αλλαγή παιχνιδιού` | **`καθοριστικός παράγοντας / ριζική αλλαγή`** | Translate the meaning |
| `Bottleneck` → `λαιμός μπουκαλιού` | **`σημείο συμφόρησης`** | Established term |
| `Pain point` → `σημείο πόνου` | **`πρόβλημα / δυσκολία`** | Translate the meaning |

### B. Structural calques (English sentence patterns)

| Wrong (literal English) | Correct (natural Greek) |
|--------------------------|---------------------------|
| `Πάρτε τη μετάφρασή σας σε λεπτά` ("Get your X done in minutes") | **`Μετάφραση σε λίγα λεπτά`** |
| `Κρατήστε τα αρχεία σας συγχρονισμένα` ("Keep X adj") | **`Διατηρήστε τον συγχρονισμό των αρχείων σας`** |
| `Κάντε τη ροή εργασίας σας πιο γρήγορη` ("Make X adj") | **`Επιταχύνετε τη ροή εργασίας σας`** |
| `Σε θέση να` ("able to") | **`μπορώ να`** |
| `Κάνω σίγουρος` ("make sure") | **`βεβαιώνομαι`** |

### C. Collocation calques (verbose noun phrases)

| Wrong | Correct (direct verb) |
|-------|------------------------|
| `κάνω μια βελτίωση` | **`βελτιώνω`** |
| `δίνω μια απάντηση` | **`απαντώ`** |
| `κάνω μια επιλογή` | **`επιλέγω`** |
| `παίρνω μια απόφαση` | **`αποφασίζω`** |
| `κάνω κλικ πάνω στο κουμπί` | **`πατήστε το κουμπί / κάντε κλικ στο κουμπί`** |
| `παίρνω ένα διάλειμμα` | **`κάνω διάλειμμα`** |

### D. Word-for-word calques

| Wrong | Correct |
|-------|---------|
| `κάνει νόημα` (calque of "makes sense") | **`έχει νόημα / βγάζει νόημα`** |
| `Πώς μπορώ να σε βοηθήσω;` (literal "how can I help") | **`Σε τι μπορώ να σε βοηθήσω;`** |
| `Όχι πραγματικά` ("not really") | **`Όχι ακριβώς / Μάλλον όχι`** |
| `Τι είδους...;` ("what kind of") | **`Τι λογής...;`** |

### E. Compound adjectives

| English pattern | Wrong (hyphenated calque) | Correct (Greek construction) |
|-----------------|----------------------------|--------------------------------|
| X-friendly | `X-φιλικός` | **`φιλικό προς τον X / εύκολο στη χρήση για X`** |
| long-term / short-term | `μακρύ-τερμ / κοντό-τερμ` | **`μακροπρόθεσμος / βραχυπρόθεσμος`** |
| X-powered / X-driven / X-based | `X-κινούμενος / X-βασισμένος` | **`με τεχνολογία X / βασισμένο σε X / με χρήση X`** |
| X-aware / context-aware | `X-ενήμερος` | **`που λαμβάνει υπόψη το X / με επίγνωση X`** |
| high-quality / low-cost | `υψηλός-ποιότητα / χαμηλός-κόστος` | **`υψηλής ποιότητας / χαμηλού κόστους`** |
| AI-powered | `AI-κινούμενος` | **`με τεχνολογία AI / βασισμένο σε AI`** |
| user-friendly | `χρήστης-φιλικός` | **`φιλικό προς τον χρήστη / εύχρηστο`** |
| cloud-based | `σύννεφο-βασισμένος` | **`στο cloud / βασισμένο σε cloud`** |

### F. Proper-noun calques

| Wrong (over-translated) | Correct |
|--------------------------|---------|
| `Ηνωμένες Πολιτείες της Αμερικής` (in UI) | **`ΗΠΑ / Ηνωμένες Πολιτείες`** |
| `Ηνωμένο Βασίλειο Μεγάλης Βρετανίας` | **`Ηνωμένο Βασίλειο / Βρετανία`** |
| `Παγκόσμιος Ιστός Ιστού` | **`Web / Παγκόσμιος Ιστός`** |

### G. False friends

| Greek word | Actually means | NOT the English |
|------------|------------------|-------------------|
| **συμπάθεια** | liking / fondness | NOT "sympathy" — use **συμπόνια** |
| **αποκαλύπτω** | to reveal | NOT "apologize" — use **ζητώ συγγνώμη** |
| **ακτουάλ** (loanword) | rare | "actual" = **πραγματικός / τρέχων** depending on sense |
| **εβεντουαλι** (loanword) | rare | "eventually" = **τελικά** |
| **σχολή** | school (high-ed / institution) | "school" (primary) = **σχολείο** |
| **φάρμα** | farm | not pharmacy — **φαρμακείο** is pharmacy |
| **εμπάθεια** | strong dislike / aversion | NOT "empathy" — use **ενσυναίσθηση** (false friend!) |
| **κάμερα** | camera | (correct, but plural is κάμερες not κάμεραι) |

### H. Marketing "Zero X" → "Χωρίς X / Καμία X"

| Wrong | Correct |
|-------|---------|
| `Μηδέν προβλήματα` | **`Χωρίς προβλήματα / Καμία ταλαιπωρία`** |
| `Μηδέν συμβόλαια` | **`Χωρίς συμβόλαιο / Χωρίς δεσμεύσεις`** |
| `Μηδέν συντήρηση` | **`Χωρίς συντήρηση / Δεν χρειάζεται συντήρηση`** |

### I. Word-sense disambiguation (polysemy)

| English (context) | Wrong (literal first sense) | Correct (contextual) |
|--------------------|-------------------------------|------------------------|
| copy (marketing) | **αντίγραφο** (= duplicate) | **κείμενο / διαφημιστικό κείμενο** |
| bug (software) | **έντομο** (= insect) | **σφάλμα / bug** |
| scale (software) | **ζυγαριά** (= weighing scale) | **κλιμάκωση / επεκτασιμότητα** |
| deploy (software) | **αναπτύσσω στρατιωτικά** | **αναπτύσσω / εγκαθιστώ** |
| build (software) | **κτίζω** (= construct buildings) | **κατασκευή / build / δημιουργία** |
| architecture (software) | **αρχιτεκτονική (κτιρίου)** | **αρχιτεκτονική συστήματος** |
| pipeline (CI/CD) | **σωλήνας** (= plumbing) | **pipeline / αγωγός CI/CD** |
| listings (app store) | **λίστες** | **σελίδα εφαρμογής / καρτέλα εφαρμογής** |
| migrate (data) | **μεταναστεύω** (= human migration) | **μεταφέρω δεδομένα / κάνω μετάβαση** |
| support (feature) | **υποστηρίζω (= hold up)** | **υποστηρίζει / είναι συμβατό με** |
| affiliates (marketing) | **συνεργάτες** (too generic) | **affiliates / συνεργάτες affiliate μάρκετινγκ** |

### J. Technical identifiers — Keep Latin Script (CRITICAL)

Code names, API names, brand names MUST stay in Latin script even when surrounded by Greek. NEVER transliterate.

| Wrong (transliterated) | Correct |
|------------------------|---------|
| `Γκιτ αποθετήριο` | **`Git αποθετήριο`** |
| `ΑΠΙ κλειδί` | **`API κλειδί`** |
| `ΤΖΣΟΝ μορφή` | **`JSON μορφή`** |
| `ΟΥΡΛ διεύθυνση` | **`URL διεύθυνση`** |
| `έν-πι-εμ πακέτο` | **`npm πακέτο`** |
| `Νοντ.τζες` | **`Node.js`** |
| `Ριάκτ στοιχείο` | **`React στοιχείο`** |
| `ΗΤΤΠ αίτημα` | **`HTTP αίτημα`** |

**Keep Latin always:** Git, GitHub, npm, Node.js, React, Vue, Angular, Next.js, API, URL, HTTP, HTTPS, JSON, XML, CSS, HTML, SQL, OAuth, JWT, REST, GraphQL, WebSocket, IDE, CLI, GUI, MVP, SaaS, PaaS, IaaS, SDK, SLA, KPI, CRM, ERP, AI, ML, NLP.

## Greetings, Closings, and Email Conventions

### Greetings
- **Γεια σας** — universal polite hello (formal, εσείς).
- **Γεια σου** — informal hello (εσύ).
- **Γεια** — neutral/casual hello.
- **Καλημέρα** — good morning (until noon).
- **Καλησπέρα** — good afternoon/evening.
- **Καλώς ήρθατε** (formal) / **Καλώς ήρθες** (informal) — welcome.
- **Καλώς ορίσατε / Καλώς ορίσετε** — formal welcome (UI).

### Goodbyes
- **Αντίο** — goodbye.
- **Γεια σας / γεια σου** — bye (same as hello).
- **Καληνύχτα** — good night.
- **Τα λέμε** — see you (informal).

### Email salutations
- Formal: `Αγαπητέ κύριε Παπαδόπουλε,` (m) / `Αγαπητή κυρία Παπαδοπούλου,` (f) — vocative case.
- Semi-formal: `Καλημέρα κύριε Παπαδόπουλε,`
- Informal: `Γεια σου Γιώργο,` / `Γεια σου!`

### Email closings
- Formal: `Με εκτίμηση,` (with esteem — standard), `Με τιμή,` (with honor — very formal), `Φιλικά,` (kindly).
- Semi-formal: `Με τους καλύτερους χαιρετισμούς,` / `Φιλικά,`
- Informal: `Φιλιά / Φιλάκια` (kisses — friends), `Τα λέμε,`

### Politeness particles
- **παρακαλώ** — please / you're welcome.
- **ευχαριστώ** — thank you.
- **ευχαριστώ πολύ** — thank you very much.
- **σας ευχαριστώ** — formal thanks (with σας).

## Self-Check Checklist (run before finalizing)

### Critical accuracy (must all pass)
- [ ] **Monotonic only** — single acute ´ on every word ≥ 2 syllables; NO polytonic ` ῀ ᾿ ῾
- [ ] **Final sigma** — ς only at word end; σ everywhere else
- [ ] **Three genders correct** (αρχείο=το, πλατφόρμα=η, χρήστης=ο, σύστημα=το)
- [ ] **Four cases correct** after prepositions (σε/για/με/από → acc, μεταξύ/λόγω → gen)
- [ ] **Verb government correct** (μετατρέπω σε + acc, εξαρτώμαι από + acc, βασίζομαι σε + acc, συνδέομαι με + acc)
- [ ] **Article contractions used** (σε + τον = στον, σε + την = στην, σε + το = στο) — NEVER `σε το`
- [ ] **Adjective agreement** (gender + number + case match noun: η νέα υπηρεσία, το νέο αρχείο)
- [ ] **Plural endings correct by gender** (-οι/-ες masc, -ες fem, -α/-ια/-ματα neut)
- [ ] **Subject-verb agreement** (singular subject → 3sg verb; plural subject → 3pl verb)
- [ ] **Greek question mark `;`** (NEVER `?`)
- [ ] **Ano teleia `·`** for mid-sentence pause (NEVER `;` for this)
- [ ] **Formality consistency** — εσείς/σας OR εσύ/σου throughout, NEVER mixed
- [ ] **Number format** — `1.234,56` (period thousands, comma decimal)
- [ ] **Date format** — `15/01/2024` DD/MM/YYYY (not US `01/15/2024`)
- [ ] **Long date format** — `15 Ιανουαρίου 2024` (genitive of month, NOT nominative)
- [ ] **Currency** — `99,99 €` (comma decimal, space, symbol after)
- [ ] **No comma before ή/και** (differs from English)
- [ ] **Comma before ότι/αν/γιατί/όταν/ενώ/αλλά**
- [ ] **Clitic pronouns** — BEFORE verb in indicative (Το αποθηκεύω), AFTER imperative (Αποθηκεύστε το)
- [ ] **All `{variables}` and ICU intact**
- [ ] **ICU plural categories** — `one / other` (Greek has only 2)
- [ ] **Definite articles included** for abstract nouns, possessives, generic statements, adj+noun
- [ ] **Latin script for tech identifiers** (Git, API, JSON, npm, Node.js — never transliterated)
- [ ] **Domain terminology** — software meaning, not literal (architecture=software, pipeline=CI/CD, bug=defect)

### Naturalness
- [ ] **Buttons** in noun form (Αποθήκευση) or formal imperative (Αποθηκεύστε) — never 1st person (Αποθηκεύω)
- [ ] **Status messages impersonal** (Φόρτωση... / Γίνεται φόρτωση... — NOT Φορτώνω)
- [ ] **Completion** = concise passive aorist (Η μετάφραση ολοκληρώθηκε — NO interjections)
- [ ] **Failure** = noun + verb OR Αποτυχία + genitive (Η αποθήκευση απέτυχε / Αποτυχία αποθήκευσης)
- [ ] **Empty state** = concise label (Κανένα αποτέλεσμα — NOT Δεν βρέθηκαν αποτελέσματα στην αναζήτησή σας)
- [ ] **Drag-drop verbs** (σύρετε, αφήστε — NOT drag, drop, κάντε drop)
- [ ] **File picker** = Επιλέξτε (action) — NOT Περιηγηθείτε (navigation)
- [ ] **«...» guillemet quotes** (NEVER `"..."`)
- [ ] **No verbed anglicisms** (αποθηκεύω NOT σεβάρω; συνδέω NOT λινκάρω; προωθώ NOT φορβαρντάρω)
- [ ] **Formal UI vocabulary** (Μεταφόρτωση NOT Ανέβασμα; Λήψη NOT Κατέβασμα)
- [ ] **No noun-stacking calques** (η ροή εργασίας NOT η εργασία ροή)
- [ ] **No compound adjective calques** (φιλικό προς τον χρήστη NOT χρήστης-φιλικός)
- [ ] **No collocation calques** (βελτιώνω NOT κάνω μια βελτίωση; απαντώ NOT δίνω μια απάντηση)
- [ ] **Marketing "Zero X"** → `Χωρίς X / Καμία X` (NOT `Μηδέν X`)
- [ ] **Greek origin words used** (τεχνολογία NOT τεκνόλοτζι; ιδέα NOT αϊντία)
- [ ] **No false friends in wrong sense** (συμπάθεια ≠ sympathy; εμπάθεια = aversion NOT empathy)
- [ ] **Quantity phrases** — `πάνω από 25` (NOT `25+`); `και {count} ακόμα` (NOT `+{count}`)
- [ ] **Rate phrases** — `ανά μήνα / το μήνα` (NOT `περ μήνα`)

## Worked Examples

### Example 1 — Welcome / upload flow

**Source:** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

#### Greek (εσείς, formal)

Καλώς ορίσατε! Παρακαλώ επιλέξτε το αρχείο σας για μεταφόρτωση — υποστηρίζουμε πάνω από 25 μορφές και το μεταφράζουμε σε 5 γλώσσες σε {seconds} δευτερόλεπτα. Μην ανησυχείτε — μπορείτε να ακυρώσετε ανά πάσα στιγμή.

#### Greek (εσύ, informal)

Καλώς ήρθες! Διάλεξε το αρχείο σου για μεταφόρτωση — υποστηρίζουμε πάνω από 25 μορφές και το μεταφράζουμε σε 5 γλώσσες σε {seconds} δευτερόλεπτα. Μην ανησυχείς — μπορείς να ακυρώσεις όποτε θέλεις.

#### Common errors both would catch

- `25+ μορφές` → **`πάνω από 25 μορφές`** (Greek quantity expression)
- `για 5 γλώσσες` (calque) → **`σε 5 γλώσσες`** (translating INTO languages uses σε + acc)
- `Μετατρέπω σας` (literal "convert your") → **`το μεταφράζουμε`** (natural Greek)
- `απλοουντάρω` or `αποστείλατε` → **`μεταφόρτωση`** (formal UI vocabulary)
- `Ανέβασμα` (colloquial) → **`Μεταφόρτωση`** (formal UI)
- `Αποθηκεύσα` (1st person past for a button) → **`Αποθήκευση / Αποθηκεύστε`**
- `?` in question → **`;`** (Greek question mark)
- `"αρχείο"` → **`«αρχείο»`** (guillemets)
- `01/15/2024` → **`15/01/2024`**

### Example 2 — Status, completion, failure

| English status | Wrong Greek | Correct Greek |
|----------------|-------------|----------------|
| Saving... | `Αποθηκεύω...` (1st person) | **`Αποθήκευση... / Γίνεται αποθήκευση...`** |
| Translation complete | `Τέλεια! Η μετάφρασή σας ολοκληρώθηκε!` | **`Η μετάφραση ολοκληρώθηκε`** |
| Upload failed | `Η μεταφόρτωση παρουσίασε σφάλμα κατά τη διάρκειά της` | **`Η μεταφόρτωση απέτυχε / Αποτυχία μεταφόρτωσης`** |
| No results | `Δεν βρέθηκαν αποτελέσματα στην αναζήτησή σας` | **`Κανένα αποτέλεσμα`** |
| Loading... | `Φορτώνω...` | **`Φόρτωση... / Γίνεται φόρτωση...`** |

### Example 3 — Verb government in a sentence

**Source:** "Convert your PDF to Word in one click. The result depends on the original file format."

| Wrong (verb government errors) | Correct |
|--------------------------------|---------|
| `Μετατρέψτε το PDF Word με ένα κλικ.` (missing σε) | **`Μετατρέψτε το PDF σε Word με ένα κλικ.`** |
| `Το αποτέλεσμα εξαρτάται τη μορφή του αρχικού αρχείου.` (missing από) | **`Το αποτέλεσμα εξαρτάται από τη μορφή του αρχικού αρχείου.`** |

Final correct: **`Μετατρέψτε το PDF σε Word με ένα κλικ. Το αποτέλεσμα εξαρτάται από τη μορφή του αρχικού αρχείου.`**

### Example 4 — Date/currency/number block

| English | Wrong | Correct Greek |
|---------|-------|---------------|
| `January 15, 2024` | `Ιανουάριος 15, 2024` (US format + nominative month) | **`15 Ιανουαρίου 2024`** (genitive) or **`15/01/2024`** |
| `$1,234.56` | `1,234.56 €` (US separators) | **`1.234,56 €`** |
| `Available 24/7` | `Διαθέσιμο 24/7` (acceptable) or `Διαθέσιμο όλο το 24ωρο` | **`Διαθέσιμο 24/7 / Διαθέσιμο όλο το 24ωρο, 7 ημέρες την εβδομάδα`** |
| `5 users` (in ICU) | `{n, plural, one {# χρήστης} other {# χρήστη}}` (wrong plural) | **`{n, plural, one {# χρήστης} other {# χρήστες}}`** |

### Example 5 — Article contractions and case

**Source:** "Save the file to your account and connect to the server."

| Wrong | Correct |
|-------|---------|
| `Αποθηκεύστε το αρχείο σε το λογαριασμό σας και συνδεθείτε σε τον διακομιστή.` (uncontracted + wrong case) | **`Αποθηκεύστε το αρχείο στον λογαριασμό σας και συνδεθείτε στον διακομιστή.`** |
| `σε το` → **`στο / στον`**, `λογαριασμό` here is accusative (after σε) | Final: contractions στον/στην/στο with appropriate gender |

## When in Doubt

1. **Monotonic vs polytonic** — when in doubt, use monotonic (single acute ´). Polytonic is reserved for ancient texts, ecclesiastical material, and explicit period pieces.
2. **εσείς vs εσύ** — when source register is unclear, default to **εσείς** (formal/plural). It is the safer default for B2B, UI, government, healthcare, finance.
3. **Article on possessives** — always include: `το αρχείο μου`, NOT `αρχείο μου`. Greek requires article + noun + possessive.
4. **σε + article** — ALWAYS contract: `στο` / `στον` / `στην` / `στους` / `στις` / `στα`. NEVER write `σε το` / `σε την`.
5. **Final sigma** — `ς` only at the absolute end of a word; everywhere else use `σ`. A single misplaced `ς` makes text look broken to a native reader.
6. **Question mark** — always `;`, never `?`. Even when copy-pasting from English, change it.
7. **Months in dates** — when written out with a day number, the month MUST be in genitive case: `15 Ιανουαρίου 2024` (not `Ιανουάριος`).
8. **Latin technical identifiers** — Git, API, JSON, npm, URL, HTTP — never transliterate to Greek letters.
9. **Anglicism vs native verb** — when unsure between `λινκάρω/κλικάρω` style and native form, choose native: `συνδέω`, `κάνω κλικ`, `αποθηκεύω`. Verbed anglicisms read as low-register / informal.
10. **Domain meaning of polysemous words** — software contexts use software senses: `architecture` = αρχιτεκτονική συστήματος (not κτιρίου), `bug` = σφάλμα (not έντομο), `deploy` = εγκαθιστώ (not military).
11. **Idioms** — translate the MEANING, not the words. "War stories" → εμπειρίες δυσκολιών; "game changer" → καθοριστικός παράγοντας. Never produce garbled literal calques.
12. **Cyprus localization** — unless the user explicitly requests Cypriot Greek lexical items, default output is standard Demotic and is fully acceptable for both el-GR and el-CY.
