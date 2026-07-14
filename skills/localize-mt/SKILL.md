---
name: localize-mt
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Maltese (Malti) for Malta. Maltese is the ONLY Semitic language in the EU AND the only Semitic language written in Latin script — descended from Siculo-Arabic with massive Italian/Sicilian/English overlay. Critical features: special letters Ċ ċ Ġ ġ Ħ ħ Ż ż (overdots and bars are PART OF the letter, NEVER strip), digraphs GĦ and IE treated as single units, definite article il- with sun-letter assimilation (id-/it-/ir-/in-/is-/iż-/iċ-/ix-/iz-) parallel to Arabic al-, Semitic root-and-pattern morphology (kiteb/kitba/kittieb/miktub from k-t-b) coexisting with Italian-borrowed conjugation, 2 genders (masc/fem) with adjective agreement, 5-form ICU plural system (one/two/few/many/other) with broken plurals (ktieb→kotba) AND sound plurals AND English -s, SVO word order with adjectives FOLLOWING the noun (Semitic pattern), ma...x double negation (ma ssejvjax NOT ma ssejvja), Anglo-style numbers (1,234.56 — comma thousands, period decimal — due to British influence), EUR currency (€1,234.56) since 2008, DD/MM/YYYY dates or \"15 ta' Jannar 2024\" with \"ta'\" linker, Catholic cultural baseline, and bilingual code-switching with English being normal in everyday Maltese. CRITICAL identity: Maltese is NOT Arabic (Arabic speakers cannot read or fully understand Maltese without learning), NOT Italian (different family), and NOT a dialect of anything — it is its own EU official language."
---

# Localize: Maltese (mt → Malti)

Distilled from production translation prompts for Maltese. Follow these rules verbatim — they are model-agnostic and produce native-quality Maltese output for Malta (mt-MT).

## Mindset

> Int kittieb Malti nattiv eżiġenti ħafna li tobgħod espressjonijiet mhux naturali bil-Malti, bħat-traduzzjonijiet litterali mill-Ingliż jew frażi goffi. Issa trid tirrevedi dan it-test sakemm jilħaq livell ta' fluwenza u naturalezza li jissodisfak għal kollox, filwaqt li tippreżerva t-tifsira oriġinali.

Reject literal English calques and forced neologisms. Restructure fully into natural Maltese. Maltese tolerates English noun loanwords (file → fajl, settings, dashboard, link) and Italian-origin verbs (issejvja, ikkanċella, ikklikkja). Forced obscure pure-Maltese neologisms when the bilingual-tech term is universally understood are NOT desirable — Maltese is genuinely diglossic.

## Scope & Variants

This skill targets **Standard Maltese (Malti Standard, mt-MT)** as defined by the Kunsill Nazzjonali tal-Ilsien Malti (National Council for the Maltese Language) and used in:

- Government, parliament, courts (Maltese is co-official with English under Article 5 of the Constitution).
- Education and media (TVM, l-Orizzont, Times of Malta Maltese edition).
- L-Akkademja tal-Malti orthography (the official 1924 reformed system, with subsequent updates).
- Software UI, formal correspondence, and product copy.

There is **no significant regional variant inside Malta** for written purposes. Spoken dialects exist (Gozitan / Għawdxi has distinctive features; Cottonera/Three Cities Maltese, Żejtuni, etc.) but written Standard Maltese is unified. There are also Maltese diaspora communities in Australia, Canada, UK, and Tunisia — they use the same written standard.

**NOT in scope:**
- Vernacular spoken forms with heavy code-switching ("Maltenglish" / "Manglish") — fine in conversation, NOT in product UI.
- Archaic/literary forms (e.g., Dun Karm's poetic register).
- Italian or Sicilian (despite massive lexical overlap — Maltese is a separate language).
- Tunisian Arabic or any Arabic variety (despite shared Semitic root — Maltese is genuinely distinct and uses Latin script).

## Identity Guardrail (CRITICAL — read every translation start)

**Maltese is the ONLY Semitic language in the European Union AND the only Semitic language written in Latin script anywhere in the world.** It is a unique linguistic identity:

- **Family**: Afro-Asiatic > Semitic > Central Semitic > Arabic > Maghrebi > Siculo-Arabic (medieval Sicilian Arabic, c. 870–1249 CE) → Maltese. Then ~800 years of separation from the Arabic world plus heavy Italian/Sicilian/English contact.
- **Script**: Latin alphabet with diacritics (Ċ Ġ Ħ Ż), not Arabic abjad. Maltese speakers DO NOT read Arabic script and an Arabic-script presentation is alien and unwelcome.
- **Mutual intelligibility with Arabic**: ASYMMETRIC and limited. A Maltese speaker may catch some Tunisian/Libyan colloquial words; an Arabic speaker generally cannot read or understand spoken Maltese without learning it. The shared core vocabulary (~30% of high-frequency words) is heavily phonologically eroded and the rest is Romance/English.
- **Mutual intelligibility with Italian**: ZERO at the grammar level. Maltese verbs conjugate Semitically (root-and-pattern). Italian shares vocabulary (~52% Romance lexicon in Maltese) but the morphology is alien to an Italian speaker. Maltese is NOT a dialect of Italian.
- **EU status**: Official EU language since 2004. All EU documents are translated into Maltese. Malta is a full EU member, Eurozone member (since 2008), Schengen member.
- **Religion**: Overwhelmingly Roman Catholic (~95%). Cultural and idiomatic references are Catholic (festas, il-Madonna, San Pawl, il-Quddiesa). Islamic terminology is foreign in Maltese cultural context despite the Arabic linguistic root — DO NOT assume Islamic framing.
- **Population**: ~500,000 speakers in Malta + Maltese diaspora.

**Do NOT:**
- Render Maltese in Arabic script.
- Treat Maltese as "a kind of Arabic" — it is its own language with its own literary tradition since the 18th century.
- Treat Maltese as "Italian-ish" — the grammar core is Semitic.
- Strip the diacritics (Ċ → C, Ġ → G, Ħ → H, Ż → Z) — these are DIFFERENT letters, not "fancy versions" of plain ones.
- Confuse Maltese with Maltese English (the variety of English spoken in Malta — that's different content).
- Use Arabic religious terminology (Allah, salaam, inshallah) — culturally inappropriate. Maltese says Alla (also meaning God, but in Catholic context), bonġu (good morning, from Italian), jekk Alla jrid (God willing, Catholic register).

## Maltese Alphabet (30 letters)

The Maltese alphabet has **30 letters** in this official order:

```
A B Ċ D E F Ġ G GĦ H Ħ I IE J K L M N O P Q R S T U V W X Ż Z
```

Note: **GĦ** (digraph) and **IE** (digraph) are listed as single letters. **H** (plain h) and **Ħ** (h-bar) are separate letters. **G** (plain g) and **Ġ** (g-overdot) are separate letters. **Z** (plain z) and **Ż** (z-overdot) are separate letters.

### Special letters — exact Unicode and sound

| Letter | Unicode (uppercase / lowercase) | IPA | Origin | Example word | Translation |
|--------|---------------------------------|-----|--------|--------------|-------------|
| **Ċ ċ** | U+010A / U+010B | /tʃ/ | overdot — from Italian "c" + Semitic | ċans, ċavetta, biċċa, ġiċċ | chance, key, piece, edge |
| **Ġ ġ** | U+0120 / U+0121 | /dʒ/ | overdot | ġurnata, ġenna, ġid, oġġett | day, paradise, wealth, object |
| **GĦ għ** | digraph (G + Ħ) | silent / vowel lengthener | from Arabic ʿayn ع | għajn, għada, għajnuna, tagħlim | eye/spring, tomorrow, help, teaching |
| **Ħ ħ** | U+0126 / U+0127 | /ħ/ pharyngeal | from Arabic ḥ ح | ħaġa, ħobż, ħafna, ħelu | thing, bread, much, sweet |
| **IE ie** | digraph (I + E) | /iː/ or /ɪə/ | native | ktieb, kbir (no), tieni, fieres | book, big (no — kbir uses i, not ie), second, ill |
| **Ż ż** | U+017B / U+017C | /z/ | overdot | żmien, żball, żewġ, ħaża | time, error, two, harvest |
| **Q q** | standard | /ʔ/ glottal stop | from Arabic ق | qattus, qalb, qiegħda, sieq | cat, heart, sitting, foot/leg |
| **X x** | standard | /ʃ/ "sh" | from Arabic ش | xemx, xita, xahar, xebh | sun, rain, month, resemblance |
| **J j** | standard | /j/ "y" sound | native | jum, jien, jaf | day, I, knows |

### Critical: NEVER strip diacritics or substitute plain letters

These are NOT "decoration" — they distinguish meaning:

| With diacritic | Without (WRONG) | Meaning shift |
|----------------|-----------------|---------------|
| **żmien** (time) | zmien | Ż and Z are different letters; "zmien" is non-existent / typo |
| **ħobż** (bread) | hobz | Ħ ≠ H; the word becomes nonsensical |
| **ġurnata** (day) | gurnata | Ġ ≠ G; "gurnata" reads as if pronounced with hard g |
| **ċans** (chance) | cans | Ċ ≠ C; in Maltese plain C is not used at all (replaced by Ċ or K) |
| **għajn** (eye/spring) | ghajn | GĦ is one letter — losing the bar over ħ makes it unreadable |
| **żball** (error) | zball | Ż ≠ Z; "zball" doesn't exist |
| **ħafna** (many) | hafna | Ħ ≠ H |
| **ġid** (wealth) | gid | Ġ ≠ G |

**Severity 3.0 — stripping diacritics is a critical error.** Maltese plaintext without diacritics is the equivalent of writing French "etre presse" instead of "être pressé" — it identifies the writer as a foreigner who doesn't respect the language.

**Note on plain C:** Maltese alphabet has **no plain C**. The phoneme /k/ is written **K** (kelb = dog, ktieb = book) and /tʃ/ is written **Ċ**. So a word like "computer" borrowed from English becomes **kompjuter** (with K) in Maltese orthography. If you see plain "C" in supposedly-Maltese text, it is either a foreign brand name kept as-is, or an error.

## Register

Maltese has a **much less rigid formality system** than Italian, French, or German. There is no clear T-V (tu/Lei) distinction in modern usage.

### The three address forms

| Form | Use | Verb form | UI default? |
|------|-----|-----------|-------------|
| **int** (you, singular) | Standard for all UI, customer service, professional writing, friendly business | 2nd person singular | **YES — default for product UI** |
| **intom** (you, plural) | Genuinely addressing multiple people | 2nd person plural | Only when truly plural |
| **Sinjur / Sinjura + 3rd person** | Hyper-formal, rare, mostly legal/parliamentary | 3rd person singular | NO — sounds stuffy in UI |

**Bottom line**: Use **int** consistently for software UI. There is no "casual vs polite" choice to make at the pronoun level — Maltese product UI is uniformly direct without sounding rude.

### What changes register in Maltese (NOT pronouns)

Since pronouns don't shift, register is signalled by:

- **Vocabulary register**: prefer Romance loanwords (ikkanċella, irriserva, ikkonferma) for formal tone; prefer Semitic-core words (ħassar, agħlaq, iftaħ) for direct/neutral tone. Mixing is fine and natural.
- **Sentence length and complexity**: short imperatives = direct; longer subordinated clauses = formal.
- **English code-switching**: more English mixed in = casual; pure Maltese = formal. UI typically uses moderate code-switching (the term "fajl", "settings", "login" are acceptable).
- **Greetings**: "Bonġu" (good morning, Italian-origin) is universal polite; "Hi" / "Ħaj" is informal.

### Consistency rules

- Pick a register at the start of a file and hold it for the entire file.
- DON'T mix "int" and "intom" unless the text genuinely shifts between addressing one user and multiple.
- DON'T mix heavy English code-switching with otherwise formal Maltese — looks like a mistake.
- Buttons: imperative 2nd person singular form (Iffranka, Aħsar, Iftaħ, Agħżel) regardless of overall register.

## Critical Hard Rules

### 1. Definite article il- and sun-letter assimilation (CRITICAL, severity 2.5)

The definite article **il-** assimilates to **9 sun consonants** (ittri tax-xemx). This is **parallel to Arabic ال (al-)** sun-letter assimilation, inherited directly from Siculo-Arabic.

**Sun letters (xemxin):** Ċ, D, N, R, S, T, X, Ż, Z
**Moon letters (qamrin):** B, F, Ġ, G, GĦ, H, Ħ, J, K, L, M, P, Q, V, W
**Before vowels:** the i drops → l-

| Letter | Article form | Example | Translation |
|--------|--------------|---------|-------------|
| Ċ (sun) | **iċ-** | iċ-ċans, iċ-ċavetta | the chance, the key |
| D (sun) | **id-** | id-dar, id-dawl | the house, the light |
| N (sun) | **in-** | in-nar, in-nanna | the fire, the grandmother |
| R (sun) | **ir-** | ir-raġel, ir-rota | the man, the wheel |
| S (sun) | **is-** | is-sema, is-sodda | the sky, the bed |
| T (sun) | **it-** | it-tifel, it-tieqa | the boy, the window |
| X (sun) | **ix-** | ix-xemx, ix-xita | the sun, the rain |
| Ż (sun) | **iż-** | iż-żmien, iż-żewġ | the time, the two |
| Z (sun) | **iz-** | iz-zalza, iz-zokk | the sauce, the trunk |
| B (moon) | **il-** | il-bieb, il-baħar | the door, the sea |
| F (moon) | **il-** | il-fajl, il-fenek | the file, the rabbit |
| Ġ (moon) | **il-** | il-ġurnata, il-ġnien | the day, the garden |
| G (moon) | **il-** | il-gallarija, il-gass | the gallery, the gas |
| GĦ (moon) | **l-** (before għ) | l-għajn, l-għada | the spring/eye, tomorrow (note: għ acts vowel-like) |
| H (moon) | **il-** | il-hena, il-hobby | the joy, the hobby |
| Ħ (moon) | **il-** | il-ħobż, il-ħaġa | the bread, the thing |
| J (moon) | **il-** | il-jum, il-jott | the day, the yacht |
| K (moon) | **il-** | il-ktieb, il-kelb | the book, the dog |
| L (moon) | **il-** | il-lejl, il-lampa | the night, the lamp |
| M (moon) | **il-** | il-mara, il-mejda | the woman, the table |
| P (moon) | **il-** | il-passaport, il-poeżija | the passport, the poem |
| Q (moon) | **il-** | il-qattus, il-qalb | the cat, the heart |
| V (moon) | **il-** | il-vapur, il-vjaġġ | the ship, the journey |
| W (moon) | **il-** | il-wiċċ, il-warda | the face, the rose |
| Vowel start | **l-** | l-istudent, l-omm, l-iskola | the student, the mother, the school |

**Wrong → Correct examples:**

| Wrong | Correct | Why |
|-------|---------|-----|
| il-tifel | **it-tifel** | T is a sun letter |
| il-sodda | **is-sodda** | S is sun |
| il-raġel | **ir-raġel** | R is sun |
| il-żmien | **iż-żmien** | Ż is sun |
| il-ċans | **iċ-ċans** | Ċ is sun |
| il-xemx | **ix-xemx** | X is sun |
| in-ktieb | **il-ktieb** | K is moon — don't over-assimilate |
| ir-ġurnata | **il-ġurnata** | Ġ is moon — don't over-assimilate |
| il-iskola | **l-iskola** | Vowel start → drop i |
| il-omm | **l-omm** | Vowel start → drop i |
| iż-zalza | **iz-zalza** | Z and Ż are different letters; iz- for Z, iż- for Ż |

**Why severity 2.5**: native speakers will catch this immediately. It is the most visible "is this writer actually Maltese?" test.

### 2. Maltese days of the week — definite article in action

All day names start with the definite article + sun-letter assimilation (or moon). This is a great mini-quiz on whether you understand the system:

| Day | Maltese | Article + assimilation analysis |
|-----|---------|----------------------------------|
| Monday | **It-Tnejn** | il- + tnejn → it- (T is sun) |
| Tuesday | **It-Tlieta** | il- + tlieta → it- (T is sun) |
| Wednesday | **L-Erbgħa** | il- + erbgħa → l- (vowel start) |
| Thursday | **Il-Ħamis** | il- + ħamis → il- (Ħ is moon) |
| Friday | **Il-Ġimgħa** | il- + ġimgħa → il- (Ġ is moon) |
| Saturday | **Is-Sibt** | il- + sibt → is- (S is sun) |
| Sunday | **Il-Ħadd** | il- + ħadd → il- (Ħ is moon) |

Day names are **always capitalised**.

### 3. Maltese months (always capitalised)

| Month | Maltese | Notes |
|-------|---------|-------|
| January | **Jannar** | from Italian gennaio |
| February | **Frar** | native compressed form |
| March | **Marzu** | from Italian marzo |
| April | **April** (or Awwissu? — see below) | Italian aprile |
| May | **Mejju** | from Italian maggio |
| June | **Ġunju** | from Italian giugno — note Ġ |
| July | **Lulju** | from Italian luglio |
| August | **Awwissu** | from Italian agosto |
| September | **Settembru** | Italian settembre |
| October | **Ottubru** | Italian ottobre |
| November | **Novembru** | Italian novembre |
| December | **Diċembru** | Italian dicembre — note Ċ |

**Date construction with "ta'"** (= "of"):
- `15 ta' Jannar 2024` (long form, the most natural in prose)
- `15/01/2024` (numeric, in UI date pickers)

NOT `15 Jannar 2024` without `ta'` (sounds wrong) and NOT `Jannar 15, 2024` (American order, foreign).

### 4. Semitic root-and-pattern morphology (severity 1.5)

Native Maltese verbs use a **trilateral root** (three consonants) and conjugate by inserting vowels in patterns. Italian-origin verbs use a different system. Both coexist.

**Example root: k-t-b (writing)**

| Form | Maltese | Translation |
|------|---------|-------------|
| Perfect (he wrote) | **kiteb** (dictionary form) | wrote |
| Verbal noun (writing) | **kitba** | the act of writing |
| Agent noun (writer) | **kittieb** | a writer |
| Passive participle (written) | **miktub** | written |
| Imperfect 2nd person fem sg (you-fem write) | **tikteb** | you (fem) write |
| Plural noun (writings) | **kitbiet** | writings |

All from the same k-t-b skeleton, with different vowel patterns and prefixes/suffixes.

**Example root: f-t-ħ (opening)**

| Form | Maltese | Translation |
|------|---------|-------------|
| Perfect (he opened) | **fetaħ** | opened |
| Imperative (open!) | **iftaħ** | open! — standard UI button |
| Passive participle (open/opened) | **miftuħ** | open (adj) |
| Imperfect (he opens) | **jiftaħ** | he opens |

**Example: Italian-borrowed verb "iffranka" (to save money/file)**

- Perfect: iffranka (he saved)
- Imperative: iffranka (save!)
- Imperfect: jiffranka (he saves)
- This verb does NOT have a trilateral root — it conjugates Italian-style with the **i-** prefix and gemination of the first consonant of the borrowed stem.

**Implication for translators**: don't try to "regularise" — accept that some verbs follow Semitic patterns and others Italian patterns. Use established forms.

### 5. The ma...x double negation (CRITICAL, severity 2.0)

Maltese verb negation **requires both ma- before and -x after** the verb. Single negation is incorrect.

| Wrong | Correct | Translation |
|-------|---------|-------------|
| Ma issejvja | **Ma issejvjax** | Doesn't save / didn't save |
| Ma niftaħ | **Ma niftaħx** | I don't open |
| Ma jaf | **Ma jafx** | He doesn't know |
| Ma ktibt | **Ma ktibtx** | I didn't write |
| Ma nstab | **Ma nstabx** | Not found (passive form, common in error messages) |

**Use "mhux" for noun/adjective negation, NOT verbs:**

| Wrong | Correct | Why |
|-------|---------|-----|
| Mhux issejvja (= "not save") | **Ma issejvjax** | verbs use ma...x |
| Ma kbir (= "not big") | **Mhux kbir** | adjectives use mhux |
| Ma utent (= "not a user") | **Mhux utent** | nouns use mhux |

**Why severity 2.0**: error messages and validation strings are full of negation. Getting this wrong sounds immediately broken to native speakers.

### 6. Two genders + adjective agreement (severity 2.0)

Maltese has **masculine** and **feminine** for nouns AND adjectives. Adjectives follow the noun and agree.

**Default rules:**
- Nouns ending in **-a** → usually **feminine** (sistema, lingwa, problema, mara, kelma, ħaġa).
- Nouns ending in **consonant** → usually **masculine** (fajl, kompjuter, ktieb, ragħal, raġel, ħobż).
- **Exceptions** exist: papa (the Pope, masculine despite -a), id (hand, feminine despite consonant ending), dar (house, feminine despite consonant ending), triq (street, feminine).

**Adjective endings (typical):**

| Form | Masculine sg | Feminine sg | Plural (often same for both genders) |
|------|--------------|-------------|---------------------------------------|
| big | **kbir** | **kbira** | kbar |
| new | **ġdid** | **ġdida** | ġodda |
| beautiful | **sabiħ** | **sabiħa** | sbieħ |
| good | **tajjeb** | **tajba** | tajbin |
| open | **miftuħ** | **miftuħa** | miftuħin |

**Wrong → Correct:**

| Wrong | Correct | Why |
|-------|---------|-----|
| sistema ġdid | **sistema ġdida** | sistema is fem (ends -a) |
| lingwa kbir | **lingwa kbira** | lingwa is fem |
| fajl ġdida | **fajl ġdid** | fajl is masc |
| problema kbir | **problema kbira** | problema is fem in Maltese (unlike Italian where *il problema* is masc) |
| mara tajjeb | **mara tajba** | mara is fem |
| ktieb kbira | **ktieb kbir** | ktieb is masc |

### 7. Plurals: broken + sound + English -s coexist (severity 2.0)

Maltese has **multiple plural systems**, depending on word origin:

#### a) Broken plurals (Semitic-origin words) — internal vowel change

| Singular | Plural | Translation |
|----------|--------|-------------|
| ktieb | **kotba** | book → books |
| kelb | **klieb** | dog → dogs |
| tifel | **tfal** | boy → children |
| raġel | **rġiel** | man → men |
| dar | **djar** | house → houses |
| kelma | **kliem** | word → words |
| qalb | **qlub** | heart → hearts |
| ħuta | **ħut** | fish → fish (collective) |

#### b) Sound plurals (masculine) — add -in / -ijiet

| Singular | Plural | Translation |
|----------|--------|-------------|
| ħaddiem | **ħaddiema / ħaddiemin** | worker → workers |
| kittieb | **kittieba** | writer → writers |

#### c) Sound plurals (feminine) — add -i / -iet / -ijiet

| Singular | Plural | Translation |
|----------|--------|-------------|
| lingwa | **lingwi** | language → languages |
| sistema | **sistemi** | system → systems |
| applikazzjoni | **applikazzjonijiet** | application → applications |
| informazzjoni | **informazzjonijiet** | piece of info → information items |

#### d) English-loan plurals — add -s

| Singular | Plural | Translation |
|----------|--------|-------------|
| fajl | **fajls** | file → files (also "fajls" is widespread; some prefer "files") |
| kompjuter | **kompjuters** | computer → computers |
| dashboard | **dashboards** | dashboard → dashboards |

#### e) Dual number (Semitic relic) — for natural pairs

Dual is rare in modern Maltese but appears for naturally paired or counted things:

| Singular | Dual | Translation |
|----------|------|-------------|
| jum (day) | **jumejn** | two days |
| sena (year) | **sentejn** | two years |
| xahar (month) | **xahrejn** | two months |
| siegħa (hour) | **sagħtejn** | two hours |

After dual, the noun is in the dual form, NOT plural. So "two days" = `jumejn`, NOT `żewġ jiem`. For "3 days" or more, use plural: `tlett ijiem` (three days).

### 8. ICU plural system (5 forms: one/two/few/many/other)

Maltese has a **CLDR/ICU 5-form plural** (more complex than English):

| Category | Applies to | Example noun: ktieb (book) | Example with number |
|----------|-----------|-----------------------------|---------------------|
| **one** | n = 1 | ktieb wieħed | 1 ktieb |
| **two** | n = 2 | żewġ kotba (or dual jumejn for days) | 2 kotba |
| **few** | n = 0 or n%100 in 3-10 | kotba | 5 kotba |
| **many** | n%100 in 11-19 | -il ktieb | 15-il ktieb |
| **other** | everything else (20+, fractions) | ktieb (singular!) | 20 ktieb, 100 ktieb |

**Key trap — 20+ uses SINGULAR**:

| Wrong | Correct | Why |
|-------|---------|-----|
| 20 kotba | **20 ktieb** | 20+ uses singular (true other category) |
| 100 lingwi | **100 lingwa** | 100 uses singular |
| 5 ktieb | **5 kotba** | 3-10 uses few-plural |
| 11 ktieb (without -il) | **11-il ktieb** | 11-19 uses "many" form with -il- suffix |
| 2 kotba | **żewġ kotba** | 2 uses "two" category + dual word `żewġ` |

ICU example:
```
{count, plural, =0 {ebda fajl} one {fajl wieħed} two {żewġ fajls} few {# fajls} many {#-il fajl} other {# fajl}}
```

### 9. Word order (SVO, adjectives follow noun)

Maltese is **SVO** (subject-verb-object), more like Romance languages than Arabic VSO. But unlike English/Italian, **adjectives FOLLOW the noun** (Semitic pattern, also Italian standard pattern).

| Wrong | Correct | Translation |
|-------|---------|-------------|
| ġdid fajl | **fajl ġdid** | new file |
| L-utent fetaħ ġdid il-fajl | **L-utent fetaħ il-fajl il-ġdid** | The user opened the new file |
| il-kbir tifel | **it-tifel il-kbir** | the big boy (both noun and adj take definite article) |

**Note: when noun is definite, the adjective ALSO takes the article:**
- `tifel kbir` (a big boy — indefinite)
- `it-tifel il-kbir` (the big boy — both get il-/it-)

### 10. Numbers: Anglo-style separators (severity 1.5)

Due to British colonial influence (1814–1964), Maltese uses **English-style number formatting**, NOT continental European:

| Format | Maltese | Italian (for contrast) |
|--------|---------|------------------------|
| Decimal | `3.14` (period) | `3,14` (comma) |
| Thousands | `1,234` (comma) | `1.234` (period) |
| Combined | `1,234.56` | `1.234,56` |
| Currency | `€1,234.56` or `€1,234.56` | `1.234,56 €` |
| Percentage | `45.5%` (no space) | `45,5%` |

**Wrong → Correct:**

| Wrong (continental) | Correct (Maltese) |
|---------------------|-------------------|
| 3,14 | **3.14** |
| 1.000 | **1,000** |
| 1.234,56 € | **€1,234.56** |
| 45,5% | **45.5%** |

This is one of the few areas where Maltese aligns with English/Irish conventions rather than continental European EU conventions. **Do not "fix" to continental style** — this is correct Maltese.

### 11. Currency: EUR (since 2008)

Malta adopted the Euro on **1 January 2008**, replacing the Maltese Lira (Lm). Format follows Anglo conventions:

| Form | Example |
|------|---------|
| Numeric | `€1,234.56` or `EUR 1,234.56` |
| Spelled out | `elf mitejn u erbgħa u tletin ewro u sitta u ħamsin ċenteżmu` (rare in UI) |
| Abbreviated in prose | `€100`, `€1.50`, `€0.50` |
| Plural | `ewro` (invariable for euro) / `ċenteżmi` (cents, plural of ċenteżmu) |

**Word "euro"**: officially spelled **ewro** in Maltese (note the W). Common forms: 1 ewro, żewġ ewro, 5 ewro, 100 ewro (number is what changes, not the noun).

Don't use Lm (Lira Maltija) — it has been demonetised since 2008.

### 12. Date and time

**Date formats:**
- Numeric: **`DD/MM/YYYY`** → `15/01/2024`, `28/02/2024`
- Long: **`DD ta' MONTH YYYY`** → `15 ta' Jannar 2024`
- The word **`ta'`** (= "of") with apostrophe-curly is the standard linker. Don't use plain "ta" without apostrophe.

**Time formats:**
- Standard: **24-hour** → `14:30`, `09:05`, `23:59`
- Optional 12-hour with: `ta' filgħodu` (AM, morning), `ta' wara nofsinhar` (PM, afternoon), `tal-għaxija` (evening)
- Examples: `2:30 ta' filgħodu` (2:30 AM), `2:30 ta' wara nofsinhar` (2:30 PM)

**Day + date in prose:**
- `Il-Ħamis, 15 ta' Jannar 2024` (Thursday, 15 January 2024)
- Note: day name has its article (Il-Ħamis), separated by comma from the date.

### 13. The "ta'" linker (genitive/of-construction)

**ta'** (= "of") with apostrophe is the most common Maltese linker. It connects nouns in a genitive-like relation:

| Maltese | English |
|---------|---------|
| il-fajl **ta'** Joe | Joe's file |
| il-bidu **tal-**ġurnata | the start of the day (note: ta' + il- → tal-) |
| **għal-**ħabta **ta'** nofsinhar | around noon |
| 15 **ta'** Jannar | 15th of January |
| **ta'** filgħodu | of the morning (= AM) |

**Contractions with definite article:**
- ta' + il- = **tal-** (`tal-ġurnata`, `tal-fajl`)
- ta' + l- (before vowel) = **tal-** (`tal-utent` — same form, just different surface)
- ta' + iż- (sun-letter case) = **taż-** (`taż-żmien`)
- ta' + it- = **tat-** (`tat-tifel`)
- ta' + is- = **tas-** (`tas-sodda`)

Same pattern as Italian "di + il = del" — Maltese contracts ta' + article.

### 14. Other prepositions and their article contractions

| Preposition | Meaning | + il- contraction | Example |
|-------------|---------|-------------------|---------|
| **fi / f'** | in | **fil-** | fil-fajl, fil-kompjuter |
| **bi / b'** | with/by | **bil-** | bil-Malti (in Maltese), bil-ħlas |
| **ġo / ġol-** | inside | **ġol-** | ġol-kaxxa |
| **għal / għall-** | for | **għall-** | għall-utent, għall-applikazzjoni |
| **ma' / mal-** | with | **mal-** | mal-utent |
| **mill-** | from | **mill-** | mill-fajl |
| **mal-** | with/by | **mal-** | mal-ġurnata |
| **fuq** | on/about | **fuq il-** (no contraction, often) | fuq il-mejda |
| **taħt** | under | **taħt il-** | taħt il-mejda |

These all assimilate with sun letters: `fis-sema` (in the sky), `bit-tifel` (with the boy), `mar-raġel` (with the man).

## UI Conventions

### Buttons — imperative 2nd person singular

Maltese buttons use the **imperative** form. Concise, direct.

| Action | Maltese button | English |
|--------|----------------|---------|
| Save | **Iffranka** or **Issejvja** or **Salva** | Save |
| Cancel | **Ikkanċella** | Cancel |
| Delete | **Ħassar** | Delete |
| Open | **Iftaħ** | Open |
| Close | **Agħlaq** | Close |
| Edit | **Editja** or **Immodifika** | Edit |
| Copy | **Ikkopja** | Copy |
| Paste | **Waħħal** | Paste |
| Search | **Fittex** | Search |
| Select | **Agħżel** | Select |
| Click | **Ikklikkja** | Click |
| Upload | **Tella'** or **Ittellgħa** | Upload |
| Download | **Niżżel** or **Inżel** | Download |
| Send | **Ibgħat** | Send |
| Login | **Idħol** or just **Login** | Login |
| Logout | **Oħroġ** or **Logout** | Logout |
| Confirm | **Ikkonferma** | Confirm |
| Try again | **Erġa' pprova** | Try again |
| Continue | **Kompli** | Continue |
| Back | **Lura** | Back |
| Next | **Li jmiss** or **Sussegwenti** | Next |
| Yes | **Iva** | Yes |
| No | **Le** | No |
| OK | **OK** or **Tajjeb** | OK |

**Note on "Iffranka" vs "Issejvja"**: both are used. **Iffranka** comes from Italian "affrancare" (to free/dispatch); **Issejvja** is from English "save". For modern software UI, **Issejvja** or **Salva** are more common. Pick one and stay consistent in a file.

### Status messages — "Qed" + present (ongoing), past participle (completed)

Maltese has a progressive aspect marker **"qed"** (= "is/are doing"). Use it for ongoing actions.

| State | Pattern | Example |
|-------|---------|---------|
| Ongoing | **Qed + imperfect verb** | `Qed jissejvja...` (saving...), `Qed jittella'...` (uploading...) |
| Completed (verb) | **past participle** | `Ssejvjat` (saved), `Ittellgħa` (uploaded), `Tlesta` (completed) |
| Completed (state) | **Tlesta / Sar / Lest** | `Tlesta!` (done!), `Lest` (ready) |
| Failed | **Ma rnexxiex / Ma rnexxix** | `Ma rnexxiex jissejvja` (couldn't save) |

| Wrong | Correct | Why |
|-------|---------|-----|
| Issejvjat (for ongoing) | **Qed jissejvja...** | Use "qed" for ongoing |
| Qed ittella' (for completed) | **Ittellgħa** or **Tlesta** | Past participle for done |
| Falla | **Ma rnexxiex** or **Kien hemm problema** | More natural failure phrasing |

### Drag and drop

| Action | Maltese | Notes |
|--------|---------|-------|
| **drag** | **ikkaxkar** | (lit. "to drag, pull along") |
| **drop** | **itfa'** or **erħi** | itfa' = throw/place; erħi = let go |
| **release** | **erħi** | NOT heles (= liberate, wrong sense) |
| **browse files** | **Agħżel il-fajls** | NOT "Browse fajls" — use "agħżel" |

| Wrong | Correct |
|-------|---------|
| Draggja l-fajls hawn | **Ikkaxkar il-fajls hawn** |
| Ħeles għall-upload | **Erħi biex ittella'** |
| Browse fajls | **Agħżel il-fajls** |

### Empty states — Ebda + noun

| English | Wrong | Correct |
|---------|-------|---------|
| No files | xejn fajls | **Ebda fajl** or **L-ebda fajl** |
| No results | xejn riżultati | **Ebda riżultat** |
| No data | xejn data | **Ebda data** or **L-ebda data disponibbli** |
| Empty | Vojt | **Ebda element** or **L-ebda kontenut** |

`Ebda` (= "no, not any") + singular noun is the formal pattern. **Bla** (= "without") works in marketing.

### Error and validation messages

| Type | Pattern | Example |
|------|---------|---------|
| Field validation | indicative or impersonal | `Dan il-qasam huwa obbligatorju` (This field is required) |
| Action instruction | imperative | `Daħħal valur validu` (Enter a valid value) |
| State description | impersonal/passive | `Ma rnexxiex jingħaqad mas-server` (Couldn't connect to the server) |

| Wrong | Correct |
|-------|---------|
| Qasam nieqes | **Dan il-qasam huwa obbligatorju** (the calque "missing" is unnatural) |
| Daħħal valur (infinitive in error) | **Daħħal valur validu** (imperative + complement) |
| Il-fajl ma jistax jinstab | **Il-fajl ma nstabx** (use passive verb form, not English calque) |

### Marketing "Zero X" → "Bla X" or "Ebda X"

| Wrong (English calque) | Correct (Maltese) |
|------------------------|--------------------|
| Zero downtime | **Bla interruzzjoni** or **Disponibbiltà kontinwa** |
| Zero errors | **Bla żbalji** or **Ebda żball** |
| Zero maintenance | **Bla manutenzjoni** or **Ma jeħtieġx manutenzjoni** |
| Zero commitment | **Bla impenn** |

### Quantity expressions: "iktar minn N" NOT "N+"

| Wrong | Correct |
|-------|---------|
| +25 lingwi | **Iktar minn 25 lingwa** |
| 25+ formati | **Iktar minn 25 format** or **'l fuq minn 25 format** |

Note the singular `lingwa` / `format` after numbers in `iktar minn N` (matching the "other" plural category for 20+).

### UI label completeness — complete noun phrases

| Wrong (bare adjective) | Correct |
|------------------------|---------|
| Awtomatiku | **Modalità awtomatika** (Automatic mode) |
| Avvanzat | **Settings avvanzati** or **Impostazzjonijiet avvanzati** |
| Alternattiv | **Detezzjoni alternattiva** |

## Punctuation, Numbers, Dates, Currency

| Item | Maltese |
|------|---------|
| Decimal separator | **`.`** (period — Anglo style) |
| Thousands separator | **`,`** (comma — Anglo style) |
| Example number | `1,234.56` |
| Currency | `€1,234.56` (symbol before, no space) — or `1,234.56 €` is also accepted |
| Date numeric | `DD/MM/YYYY` → `15/01/2024` |
| Date long | `15 ta' Jannar 2024` (with "ta'" linker, month capitalised) |
| Time | 24-hour `14:30` standard; 12-hour `2:30 ta' filgħodu` (AM) / `ta' wara nofsinhar` (PM) |
| Quotation marks | `"..."` (standard double quotes, like English) |
| Spacing around `: ; ? !` | **No NBSP** — standard ASCII spacing (NOT French rules) |
| Ellipsis | `…` (single char) preferred over `...` |
| Apostrophe | `'` curly preferred; in `ta'`, `m'`, `b'`, `f'` it is essential |

**Common conversions from continental EU style:**

| Wrong (Italian/German style) | Correct (Maltese) |
|------------------------------|-------------------|
| `3,14` | **`3.14`** |
| `1.000` | **`1,000`** |
| `1.234,56 €` | **`€1,234.56`** |
| `01/15/2024` (American) | **`15/01/2024`** |

## Terminology

### Preferred UI translations

| English | Preferred Maltese | Alternative | Notes |
|---------|-------------------|-------------|-------|
| file | **fajl** | (no real native equivalent) | English loan, fully integrated |
| folder | **kartella** | fowlder | from Italian "cartella" |
| save | **issejvja** / **iffranka** / **salva** | (pick one per file) | salva from Italian |
| delete | **ħassar** | elimina | ħassar = native Semitic |
| cancel | **ikkanċella** | ħassar | from Italian "cancellare" |
| upload | **tella'** / **ittellgħa** | upowdjat | tella' is native (lit. "raise") |
| download | **niżżel** / **inżel** | downlowdjat | niżżel is native (lit. "lower") |
| click | **ikklikkja** | (no native alternative) | English-origin verb |
| search | **fittex** | sib | native Semitic |
| select | **agħżel** | għażel | imperative form |
| open | **iftaħ** | — | from f-t-ħ root |
| close | **agħlaq** | — | imperative |
| edit | **editja** / **immodifika** | — | editja is English loan |
| copy | **ikkopja** | — | from Italian "copiare" |
| paste | **waħħal** | inkolla | waħħal = native (lit. "stick") |
| send | **ibgħat** | — | native |
| user | **utent** | — | from Italian "utente" |
| account | **kont** | — | from Italian "conto" |
| email | **email** | posta elettronika | email is universal |
| password | **password** | kelma sigrieta | password is universal |
| settings | **settings** / **impostazzjonijiet** | konfigurazzjoni | English term very common |
| dashboard | **dashboard** / **pannell** | — | English usually retained |
| browser | **brawżer** | — | Maltese-spelled English |
| link | **link** / **ħolqa** | — | both forms used |
| login | **idħol** / **login** | — | both common |
| logout | **oħroġ** / **logout** | — | both common |
| help | **għajnuna** | — | native |
| about | **dwar** | — | native |
| home | **dar** / **paġna prinċipali** | — | dar = "house" |
| share | **aqsam** | — | imperative |
| confirm | **ikkonferma** | — | Italian-origin |
| try again | **erġa' pprova** | — | with apostrophe in erġa' |
| done | **lest** / **tlesta** | — | lest = ready; tlesta = is completed |
| loading | **qed jagħbi** / **qed itella'** | — | "qed" + verb |
| error | **żball** | erro | native |
| warning | **twissija** | — | native |
| success | **suċċess** | — | Italian-origin |

### Italian-origin verbs (the i- prefix + double consonant pattern)

A productive Maltese pattern: take an Italian verb stem, drop the infinitive ending, prefix with **i-** (or **ikk-** if stem starts with c/k), gemminate the first consonant.

| Italian | Maltese verb |
|---------|--------------|
| salvare | **issejvja** (also **salva**) |
| cancellare | **ikkanċella** |
| copiare | **ikkopja** |
| confermare | **ikkonferma** |
| caricare | **ikkarika** |
| comunicare | **ikkomunika** |
| consultare | **ikkonsulta** |
| controllare | **ikkontrolla** |
| eliminare | **ielimina** (rare; native ħassar more common) |
| modificare | **immodifika** |
| organizzare | **organizza** |
| programmare | **ipprogramma** |
| stampare | **istampa** (print) |
| telefonare | **iċempel** (native!) or **ittelefona** |

### English-origin verbs (recent, often clearly anglicism)

| English | Maltese verb form | Notes |
|---------|-------------------|-------|
| save | **issejvja** | gemmination + i- prefix |
| update | **iggajdja** / **aġġorna** | aġġorna (Italian-origin) preferred in formal context |
| login | **illoggja** | informal |
| logout | **illogjawt** | informal |
| post (verb) | **ippostja** | informal |
| share | **issjerja** (rare) or **aqsam** (native) | aqsam preferred |
| edit | **editja** | well-established |
| upload | **upowdjat** (rare) or **tella'** (native) | tella' preferred |
| download | **downlowdjat** (rare) or **niżżel** (native) | niżżel preferred |

**Rule of thumb**: prefer native or Italian-origin verb when it exists and is established (tella', niżżel, aqsam, fittex, iftaħ). Use English-loan verb when no clear native equivalent exists (ikklikkja, editja).

### False friends to watch (Italian → Maltese)

| Maltese | Means | NOT the Italian |
|---------|-------|------------------|
| attwalment | currently | NOT "actually" — use `fil-fatt` for actually |
| eventwalment | possibly | NOT "eventually" — use `fl-aħħar` for eventually |
| sensibbli | sensitive | NOT "sensible" — use `raġonevoli` for sensible |
| libreriija | bookstore / library (both!) | context-dependent |
| simpatiku | nice / friendly | NOT "sympathetic" — use `tal-għajn` for sympathetic |
| eduwkat | educated / polite | broader than English "educated" |

### Brand names

Foreign brand names (Apple, Google, Microsoft, Facebook, OneSky) remain **unchanged**. When the definite article is needed:

- Sun letter at start → assimilate: `it-Twitter` (T is sun)
- Moon letter at start → keep il-: `il-Facebook`, `il-Google`
- Vowel start → l-: `l-Apple`, `l-Instagram`

### Religious / cultural sensitivity

Malta is overwhelmingly Roman Catholic. The following is fine and culturally apt:

- **Alla** (God, in Catholic Christian sense — same word root as Arabic Allah but Catholic meaning in Maltese)
- **il-Madonna** (Our Lady, Virgin Mary)
- **San Pawl** (Saint Paul — Malta's patron, important national identity)
- **il-festa** (feast day — every village has its patron saint's festa)
- **il-Quddiesa** (Mass)
- **Il-Milied** (Christmas)
- **L-Għid** (Easter)

DO NOT use Arabic/Islamic framings (salaam, inshallah verbatim, ramadan references, mosque-related vocabulary) as the default cultural baseline. They are intelligible (Malta has Muslim minority + ties to North Africa) but culturally not the norm.

**Inclusive option for non-religious contexts**: avoid religious idioms entirely. Use neutral business language.

## Calque / Anti-Pattern Blocklist

| Wrong (literal calque) | Natural Maltese |
|------------------------|------------------|
| Jagħmel sens (lit. "makes sense") | **Għandu sens** or **Huwa loġiku** |
| Fl-aħħar tal-ġurnata (lit. "at the end of the day") | **Fl-aħħar mill-aħħar** or **Wara kollox** |
| Aqta' siek (lit. "break a leg") | **Il-hena!** or **Awguri!** |
| Biċċa kejk (lit. "piece of cake") | **Faċli daqs tnejn** or **Mhux diffiċli** |
| Ħa tieħu post (lit. "is going to take place") | **Isir** or **Iseħħ** |
| Ibbażat fuq (overuse) | **Skont** when possible |
| Sabiex (= "in order to", verbose) | **Biex** |
| Fil-każ li (= "in case", verbose) | **Jekk** |
| Zero żbalji | **Bla żbalji** or **Ebda żball** |
| Zero downtime | **Bla interruzzjoni** or **Disponibbiltà kontinwa** |
| AI-ibbażat | **B'appoġġ tal-AI** or **Bbażat fuq l-AI** |
| Utent-ħabib (lit. "user-friend") | **Faċli għall-użu** or **Intuwittiv** |
| X-konxju (calque of X-aware) | **Li jqis il-X** or **Sensittiv għall-X** |
| L-Istati Uniti tal-Amerika (in UI) | **l-USA** or **l-Istati Uniti** |

### "Inżel/erħi" confusions

| Wrong | Correct | Why |
|-------|---------|-----|
| Ħeles għall-upload | **Erħi biex ittella'** | "Heles" = liberate/free a prisoner — wrong sense for "release/let go" |
| Permettja l-upload | **Erħi biex ittella'** | "Permettja" = permit — different semantic |

### Conjunction commas

| Conjunction | Comma? |
|-------------|--------|
| **u** (and) | **No comma before** |
| **jew** (or) | **No comma before** |
| **jew inkella** (or else) | **No comma before** |
| **iżda / imma / però** (but) | **Comma before** |
| **li** (that — relative/subordinating) | **Comma before** (usually) |
| **meta** (when) | **Comma before** |
| **jekk** (if) | **Comma before** |
| **għax** (because) | **Comma before** |
| **biex** (so that, in order to) | **Comma before** |

| Wrong | Correct |
|-------|---------|
| Agħżel fajl, jew fowlder | **Agħżel fajl jew fowlder** |
| Ikklikkja, u issejvja | **Ikklikkja u issejvja** |
| Ikklikkja biex tissokta | **Ikklikkja, biex tissokta** |

## Self-Check Checklist

### Accuracy
- [ ] All special letters preserved: **Ċ ċ Ġ ġ Ħ ħ Ż ż** (NEVER stripped or replaced with C G H Z)
- [ ] Digraphs intact: **GĦ** and **IE** treated as units (not split)
- [ ] Definite article assimilates correctly: sun letters (Ċ D N R S T X Ż Z) → iċ-/id-/in-/ir-/is-/it-/ix-/iż-/iz-; moon letters → il-; vowels → l-
- [ ] Day names with article (It-Tnejn, It-Tlieta, L-Erbgħa, Il-Ħamis, Il-Ġimgħa, Is-Sibt, Il-Ħadd)
- [ ] Month names capitalised (Jannar, Frar, Marzu, April, Mejju, Ġunju, Lulju, Awwissu, Settembru, Ottubru, Novembru, Diċembru)
- [ ] Date format: `DD/MM/YYYY` or `DD ta' MONTH YYYY` (with `ta'`)
- [ ] Gender agreement: masc/fem on adjectives (sistema ġdida NOT sistema ġdid; fajl ġdid NOT fajl ġdida)
- [ ] Plural form correct: broken (kotba, klieb, tfal), sound (-iet/-ijiet, -in), or English -s (fajls, kompjuters), depending on word origin
- [ ] 20+ uses SINGULAR (20 ktieb, NOT 20 kotba); 11-19 uses singular + -il- (15-il ktieb); 2 uses dual or żewġ
- [ ] ma...x double negation used for verbs (ma issejvjax NOT ma issejvja)
- [ ] mhux for noun/adjective negation, NOT verbs
- [ ] Word order SVO; adjectives FOLLOW noun (fajl ġdid, NOT ġdid fajl)
- [ ] Both noun and adjective take article when definite (it-tifel il-kbir)
- [ ] Numbers: comma thousands, period decimal (1,234.56 — Anglo style)
- [ ] Currency: € before number, no space (€1,234.56)
- [ ] Time: 24-hour standard
- [ ] Quotes: standard `"..."`
- [ ] No NBSP before `: ; ? !` (Maltese uses ASCII spacing)
- [ ] All `{variables}` and ICU plural syntax intact
- [ ] FOR (total) vs PER (rate): `għal 5 lingwi` (for 5 languages total) vs `kull lingwa` (per language) — never confuse

### Naturalness
- [ ] Buttons imperative form (Issejvja, Iftaħ, Ħassar, Agħżel, Ikkonferma)
- [ ] Status messages use `Qed + imperfect` for ongoing (Qed jissejvja...) and past participle for completed (Issejvjat / Tlesta)
- [ ] Failure: "Ma rnexxiex" + verb, not "Falla"
- [ ] Drag-drop: ikkaxkar / itfa' / erħi (NOT draggja, ħeles)
- [ ] File picker: "Agħżel" (NOT "Browse")
- [ ] Empty state: "Ebda X" or "L-ebda X" (NOT "Xejn X" or bare "Vojt")
- [ ] Marketing "Zero X" → "Bla X" or "Ebda X"
- [ ] Quantity: "Iktar minn 25" (NOT "+25" or "25+")
- [ ] Calques avoided (no "jagħmel sens", no "fl-aħħar tal-ġurnata", no "ħa tieħu post")
- [ ] False friends in correct sense (attwalment = currently NOT actually; eventwalment = possibly NOT eventually)
- [ ] Code-switching with English is bounded — use established Maltese terms where they exist (tella' not upowdjat; niżżel not downlowdjat; aqsam not issjerja)
- [ ] No forced obscure neologisms when bilingual tech term is universal (fajl is fine; "dokument elettroniku" is overkill)
- [ ] Domain terminology in IT sense (arkitettura = software architecture, not building; pipeline = CI/CD, not plumbing)
- [ ] Compound adjectives natural (b'appoġġ tal-AI, faċli għall-użu — not AI-ibbażat, utent-ħabib)
- [ ] Religious framing Catholic where present (Alla, il-Madonna, San Pawl, il-festa — not Islamic vocabulary as default)
- [ ] No comma before `u` (and) or `jew` (or); comma before `li`, `meta`, `jekk`, `biex`, `iżda`
- [ ] Register consistent throughout file (int / intom usage stable; vocabulary register stable)

## Worked Examples

### Example 1: UI welcome with file upload

**Source (English):** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

**Maltese:**

> Merħba! Agħżel il-fajl tiegħek biex ittellgħa — aħna ngħinu b'iktar minn 25 format u nittraduċuh għal 5 lingwi f'{seconds} sekondi. Tinkwetax, tista' tikkanċella f'kull ħin.

**What this demonstrates:**
- `Merħba!` (welcome — native Semitic word)
- `Agħżel` (select — imperative, NOT "browse")
- `il-fajl` (the file — moon letter F, article stays il-)
- `tiegħek` (your, sg. — possessive suffix, "int" register)
- `biex` (so that — not "sabiex")
- `ittellgħa` (be uploaded — passive form of `tella'`)
- `iktar minn 25` (more than 25 — NOT "25+")
- `format` (singular after iktar minn N — correct CLDR "other" form for 25)
- `lingwi` (languages — sound feminine plural of `lingwa`)
- `għal 5 lingwi` (for 5 languages — `għal` for total, not `kull`)
- `f'{seconds} sekondi` (in {seconds} seconds — `fi` contracted to `f'` before vowel of placeholder)
- `Tinkwetax` (Don't worry — note the `-x` suffix of ma...x negation, even with the imperative prefix `tin-`)
- `tista'` (you can — apostrophe is essential)
- `tikkanċella` (cancel — Italian-origin verb with i- prefix)
- `f'kull ħin` (at any time — `fi` → `f'` + Ħ moon letter)

### Example 2: Error message

**Source:** "The file could not be found. Please verify the path and try again."

**Maltese:**

> Il-fajl ma nstabx. Jekk jogħġbok ivverifika l-path u erġa' pprova.

**What this demonstrates:**
- `Il-fajl` (the file — il- with F moon letter)
- `ma nstabx` (was not found — passive verb form `instab` + ma...x double negation; NOT "ma jistax jinstab" calque)
- `Jekk jogħġbok` (please — lit. "if it pleases you")
- `ivverifika` (verify — Italian-origin verb)
- `l-path` (the path — English loan kept; `il-` → `l-` because vowel/h-like silent start; some writers use `il-path`)
- `erġa' pprova` (try again — with apostrophe in `erġa'`)

### Example 3: Confirmation dialog

**Source:** "Are you sure you want to delete 15 files? This action cannot be undone."

**Maltese:**

> Żgur li trid tħassar 15-il fajl? Din l-azzjoni ma tistax titreġġa' lura.

**What this demonstrates:**
- `Żgur li` (sure that — `li` introduces subordinate clause)
- `trid tħassar` (you want to delete — int-form, no infinitive in Maltese, just bare imperfect)
- `15-il fajl` (15 files — note `-il-` suffix mandatory for 11-19; SINGULAR `fajl` after, matching "many" CLDR category)
- `Din l-azzjoni` (this action — `azzjoni` is feminine, hence `din` not `dan`; `l-` before vowel a)
- `ma tistax` (cannot — ma...x with imperfect 3rd-fem-sg of `seta'` matching `l-azzjoni`)
- `titreġġa' lura` (be reversed — passive verb form + `lura` = back)

### Example 4: Pricing card

**Source:** "Starter plan — €9.99 per month for 5 languages and 10,000 words. No commitment."

**Maltese:**

> Pjan Starter — €9.99 fix-xahar għal 5 lingwi u 10,000 kelma. Bla impenn.

**What this demonstrates:**
- `Pjan Starter` (Starter plan — English brand-like term kept)
- `€9.99` (Anglo number format: period decimal; € before, no space)
- `fix-xahar` (per month — `fi` + `il-` → `fil-`; sun letter X → `fix-`; lit. "in the month")
- `għal 5 lingwi` (for 5 languages — `għal` = for/total)
- `10,000 kelma` (10,000 words — Anglo comma thousands; `kelma` singular because 10,000 falls in "other" CLDR category for 20+; literally "10,000 word")
- `Bla impenn` (No commitment — "Bla X" pattern, NOT "Zero X")

### Example 5: Pluralisation across categories (ICU example)

**Source frame:** "{count} files selected"

**Maltese forms (CLDR 5-form):**

| count | Maltese | Analysis |
|-------|---------|----------|
| 0 | `Ebda fajl magħżul` | "no" category — `ebda` + singular |
| 1 | `Fajl wieħed magħżul` | one — `wieħed` (one, masc) follows masc noun |
| 2 | `Żewġ fajls magħżula` | two — `żewġ` + plural |
| 5 | `5 fajls magħżula` | few (3-10) — plural form, agreeing in adj |
| 15 | `15-il fajl magħżul` | many (11-19) — singular + `-il-` infix, singular adj agreement |
| 25 | `25 fajl magħżul` | other (20+) — SINGULAR form |
| 100 | `100 fajl magħżul` | other — SINGULAR |

Note: this example uses English loan `fajl/fajls` plural with -s. If you used a Semitic-root noun, the broken-plural form would replace the -s form in the `few` and `two` categories.

### Example 6: Status spinner messages

**Source:** "Uploading file... | Processing... | Done! | Failed to save."

**Maltese:**

> Qed jittella' l-fajl... | Qed jiġi pproċessat... | Tlesta! | Ma rnexxiex jissejvja.

**What this demonstrates:**
- `Qed jittella'` (is being uploaded — `qed` + passive imperfect of `tella'`)
- `Qed jiġi pproċessat` (is being processed — `qed jiġi` + past participle)
- `Tlesta!` (done — perfective form, complete state)
- `Ma rnexxiex jissejvja` (failed to save — `ma rnexxiex` = didn't succeed + bare verb; NOT "Falla")

### Example 7: Code-switching sweet spot

**Source (mixed input):** "Click the Dashboard tab, then go to Settings > Notifications."

**Maltese (showing acceptable code-switching):**

> Ikklikkja t-tab Dashboard, mbagħad mur fis-Settings > Notifications.

**Alternative pure Maltese:**

> Ikklikkja l-paġna Dashboard, mbagħad mur fl-Impostazzjonijiet > Notifiki.

**Why both work:** Maltese is genuinely bilingual in tech contexts. The first version (with English UI terms) matches how Maltese tech professionals actually speak and write. The second version (pure Maltese) is appropriate for formal documentation. Pick one approach per document and stay consistent.

**What NOT to do:**

> *Ikklikkja t-tab id-dashboard...* (mixing definite article with English term inconsistently)
> *Klikkja* (English bare verb without Maltese morphology)

## When in Doubt

1. **Special characters** — If in doubt about Ċ Ġ Ħ Ż, **assume you need them**. They are not optional. Verify with a Maltese-Italian dictionary or the Akkademja tal-Malti reference.

2. **Definite article** — If unsure about sun vs moon letter, recite the sun consonants: **Ċ D N R S T X Ż Z**. Everything else is moon. Vowels and silent għ → use `l-`.

3. **Plural form** — When in doubt about broken vs sound plural, check a dictionary. For English loanwords, `-s` is normally fine (fajls, kompjuters). For Semitic-root nouns, the broken plural is required (klieb not kelbs; kotba not ktiebs).

4. **20+ singular trap** — Always: 1 → one form, 2 → dual or żewġ, 3-10 → plural, 11-19 → -il- + singular, 20+ → singular. The 20+ singular is the most-missed rule.

5. **ma...x** — If you write a negated verb, **always end with -x**. If you find yourself wanting to use `mhux` with a verb, you probably need ma...x instead.

6. **Gender** — Default rule: -a ending → feminine, consonant ending → masculine. When in doubt, consult a dictionary. Note that adjective agreement is mandatory (sistema ġdida, fajl ġdid).

7. **Code-switching with English** — If a term is universally understood in English (file, settings, dashboard, login), it is fine to use as a Maltese loanword. If a clear Maltese term exists and is established (tella', niżżel, aqsam, fittex), prefer it. Don't force obscure neologisms ("dokument elettroniku" for "file" is overkill).

8. **Religious tone** — Default to neutral. If a Catholic framing fits naturally (Christmas messaging, festa references), use it confidently. Do NOT default to Islamic vocabulary because of the Arabic roots — culturally Malta is Catholic.

9. **Number formats** — When the source is European (1.234,56), **invert** to Anglo (1,234.56). Maltese aligns with English here.

10. **"Ta'" linker** — Almost any "X of Y" construction in English wants `Y ta' X` or `Y tal-X` in Maltese. The apostrophe in `ta'` is essential.

11. **Identity check** — Before finalising, ask: "Would a native Maltese speaker recognise this as natural Maltese — not Arabic in Latin script, not awkwardly literal Italian, not English-with-Maltese-decoration?" If you're unsure, simplify and use more established vocabulary.

12. **Sanity check the diacritics** — Final pass: search the output for plain `c h z g` (lowercase) and verify that every instance is either (a) part of a digraph (għ, ie), (b) a foreign brand name, or (c) a genuinely native form. Otherwise you probably need `ċ ħ ż ġ`.
