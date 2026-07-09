---
name: localize-sw
description: Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Swahili (Kiswahili) for East Africa — Tanzania (sw-TZ), Kenya (sw-KE), Uganda, the eastern DRC, Rwanda, Burundi, and as a lingua franca across the African Great Lakes region. Swahili is a **Bantu (Niger-Congo)** language — NOT Arabic, despite ~20% of vocabulary being Arabic loanwords, and NOT closely related to other major African languages (Hausa is Afro-Asiatic, Yoruba is Niger-Congo Volta-Niger, both grammatically very different from Bantu). THE defining feature is the **NOUN CLASS SYSTEM** — 15-18 noun classes (commonly grouped into 9 singular/plural pairs) each with its own prefix that spreads through the entire sentence via concord (every adjective, verb, possessive, demonstrative that refers to the noun must carry a matching prefix). Other critical features: agglutinative verb morphology (SM-TAM-OM-root-extension-FV, e.g. a-li-ki-pik-i-a = "he/she-PAST-it-cook-applied-FINAL"), tense markers -na- (present) / -li- (past) / -ta- (future) / -me- (perfect) / -ki- (while/conditional) / -nge- (would), subject prefixes ni-/u-/a-/tu-/m-/wa- for persons plus class-specific prefixes for noun-class subjects, **no grammatical gender** (noun classes are NOT gendered male/female), SVO word order but flexible due to verb morphology marking subject and object, adjectives AFTER the noun with concord prefixes (faili kubwa, kitufe kipya, mifumo mipya), no articles (a/the inferred from context), possessives that agree with the possessed noun's class (kitabu changu, vitabu vyangu, watu wangu), Latin alphabet with **ng' (with apostrophe)** as a distinct letter (velar nasal) separate from ng, NO tones (Swahili lost the Bantu tone system), stress on penultimate syllable, ICU plurals **one/other** (plural is morphological via class prefix), numbers 1-5 take noun-class concord (mtu mmoja, vitu vitatu) but 6+ do not, currency varies by country (TZS Tanzanian Shilling TSh /=, KES Kenyan Shilling KSh, UGX Ugandan Shilling USh, CDF Congolese Franc Fr), DD/MM/YYYY dates, English-derived month names (Januari, Februari, Machi...), Arabic-derived day names (Alhamisi Thursday, Ijumaa Friday), comma thousands + period decimal (Anglo-style 1,234.56), Arabic loanwords integrated into native phonology (kitabu, salama, shule, saa), English loanwords for tech (kompyuta, programu, faili, folda), imperative buttons (Hifadhi, Futa, Tuma — NOT Kuhifadhi infinitive), impersonal system voice with class-prefix + -na-/-me- (Inapakia..., Imehifadhiwa), Kiswahili sanifu (standard Swahili) as the UI register — NOT Sheng (Nairobi urban mix) or kiswahili cha mtaani (street Swahili), and cross-EAC regional respect (don't favor Tanzanian or Kenyan terminology in a way that excludes the other; East Africa is religiously mixed Muslim/Christian/indigenous — keep UI religiously neutral).
---

# Localize: Swahili (sw → Kiswahili)

You are translating source text into Swahili for East Africa. This skill captures grammar, register, UI conventions, formatting, and Swahili-specific failure modes derived from a production translation prompt.

## Scope & Variants

Swahili has two primary localization targets used in software, both based on the same literary standard (Kiswahili sanifu) but with minor lexical preferences:

- **sw-TZ** — Tanzanian Swahili. Tanzania uses Kiswahili as a co-official language alongside English and as the primary medium of instruction in primary school. **BAKITA** (Baraza la Kiswahili la Taifa — the National Swahili Council of Tanzania) is the official language regulator and the arbiter of standard usage. Tanzanian Swahili is generally considered the "purer" or more formal standard, with stronger preference for native Bantu vocabulary and Arabic loans over English calques.
- **sw-KE** — Kenyan Swahili. Kenya uses Kiswahili as a co-official language alongside English. Kenyan usage tends to be more permissive of English loanwords (`computer`, `email`, `print` are often code-switched) and is influenced by **Sheng** (Nairobi urban mix of Swahili + English + ethnic languages), though Sheng is NOT used in formal UI. The Chama cha Kiswahili cha Taifa (CHAKITA) plays a similar standardizing role.

**Also significant:**
- **sw-UG** — Uganda. Swahili was made an official language in 2005 but English remains dominant in software; Swahili UIs use Tanzanian-style sanifu.
- **sw-CD** — DR Congo. Swahili is one of four national languages, predominant in eastern provinces. Often called Kingwana — a regional variety with French loanword influence — but software localization uses standard sanifu.
- **sw-RW, sw-BI** — Rwanda, Burundi. Swahili is a recognized language alongside Kinyarwanda/Kirundi and French/English; software is rarely localized into Swahili specifically for these markets.

**Default UI register: Tanzanian-style Kiswahili sanifu**, which Kenya largely follows. This is the safest choice for pan-East-African software because:
1. Tanzania has the largest Swahili-as-first-language population (~15M L1 speakers, ~50M total).
2. BAKITA-aligned vocabulary is universally understood in Kenya, Uganda, and beyond.
3. It avoids Sheng-flavored Kenyan colloquialisms that Tanzanians or formal Kenyans may find unprofessional.

**Native name:** Kiswahili (the language — note the **Ki-** prefix from class 7, which is the noun class used for languages). Use "Kiswahili" in UI when naming the language itself.

## Identity Guardrail

Swahili is **Bantu (Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern Bantoid, Narrow Bantu, Sabaki)**. Closest sister languages: other Sabaki languages (Comorian Shikomori, Mwani, Pokomo). Wider family: ~500 Bantu languages across sub-Saharan Africa (Zulu, Xhosa, Shona, Kikuyu, Luganda, Lingala, Kinyarwanda, etc.) — all share the noun-class system, agglutinative verb morphology, and concord.

**Swahili is NOT:**
- **NOT Arabic** — despite ~20% of vocabulary being Arabic loanwords (kitabu from kitāb, salama from salām, shule from school via German/Arabic, dunia from dunyā), Swahili grammar is **fundamentally Bantu**. Arabic is Afro-Asiatic, has root-and-pattern morphology, three-letter consonantal roots, masculine/feminine gender, dual number, and VSO order. Swahili has none of these — it has noun classes, agglutinative prefix-stacking verbs, no gender, no dual, and SVO. Do **NOT** treat Swahili as "African Arabic." The Arabic vocabulary layer is comparable to French loanwords in English: lexical influence, zero grammatical influence.
- **NOT closely related to Hausa, Yoruba, Igbo, Zulu/Xhosa, Amharic, Somali, etc.** — Hausa is Afro-Asiatic (Chadic). Yoruba and Igbo are Niger-Congo but Volta-Niger branch, NOT Bantu. Zulu/Xhosa ARE Bantu but South Bantu (very distant cousins, ~3000+ years diverged from Swahili — about as related as English to Hindi). Amharic and Somali are Afro-Asiatic Semitic and Cushitic respectively. Do NOT translate Swahili by analogy with any of these.
- **NOT Sheng.** Sheng is a Nairobi-origin urban mix of Swahili grammar with English, Kikuyu, Luo, and Dholuo vocabulary. It is heavily slang-based, age-marked (teen/young-adult), and used in informal conversation, music (genge, gengetone), and street advertising. Sheng is **inappropriate for software UI**, formal writing, or any text intended to be understood across age groups and regions. UI uses Kiswahili sanifu.
- **NOT historically Arabic-script.** Swahili was indeed historically written in **Ajami** (a modified Arabic script) on the coast of East Africa from roughly the 13th century onward, but since the 19th century the standard script has been Latin (adopted under European colonial education and standardized at the 1928 Mombasa conference). All modern UI, books, newspapers, and digital content use Latin script. Do NOT output Arabic script.

**Closest practical neighbors:**
- Comorian (Shikomori) — same Sabaki subgroup, ~50% mutually intelligible to literate Swahili speakers.
- Mijikenda languages (Giriama, Digo) — coastal Kenya, Sabaki cousins.
- Other Bantu languages share the noun-class concept but with different class numbers, prefixes, and vocabulary — a Zulu speaker would recognize the system but not the words.

## Register

**Default level: Polite-standard sanifu** for software UI, errors, documentation, marketing.

Swahili does **NOT have a strict T-V distinction** like French tu/vous, German du/Sie, or Hungarian te/Ön. Politeness is achieved through:

| Mechanism | Casual | Polite-standard (UI) |
|---|---|---|
| Pronoun | wewe (you sg), nyinyi/ninyi (you pl) | same — wewe is universal |
| Vocabulary | colloquial | formal Bantu / Arabic loans |
| Verb form | bare imperative | subjunctive (-e final), or imperative + tafadhali |
| Sentence shape | terse | structured |

| | wewe (you, sg) | ninyi (you, pl) |
|---|---|---|
| Subject prefix | u- | m- |
| Object prefix | -ku- | -wa-/-eni |
| Imperative | Hifadhi! Soma! | Hifadhini! Someni! (with -ni suffix) |
| Subjunctive | uhifadhi, usome | mhifadhi, msome |
| Possessive | -ako (kitabu chako) | -enu (kitabu chenu) |

**The critical insight:** Politeness in Swahili comes from **word choice and structure**, not from a separate formal pronoun. A button labeled `Hifadhi` (Save — bare imperative) is not impolite; it is the norm. Adding `Tafadhali hifadhi` ("please save") on every button would be **excessively polite** and feel non-native.

**Examples of register calibration:**
- UI button: `Hifadhi` (correct — direct imperative, polite-standard)
- Polite request: `Tafadhali ingiza nenosiri lako` (please enter your password — `tafadhali` reserved for high-stakes prompts)
- Casual/Sheng (WRONG for UI): `Hifadhi maze` (save dude), `Hebu save` (let me save), `Sasa unataka kufanya nini?` (what do you wanna do now — colloquial conversational opener)

**Within a file, ONE register only.** Mixing sanifu with Sheng terms (e.g. `mzee` for "old version", `noma` for "great") is always wrong in UI.

**Pronouns of address:**
- `wewe` — singular "you", default for UI addressed to a single user. Not impolite.
- `ninyi`/`nyinyi` — plural "you", for messages addressed to multiple users (e.g. team mentions).
- `Bwana` (Mr.), `Bibi` (Mrs.), `Mwalimu` (Teacher), `Daktari` (Doctor) — honorifics for direct address, used in customer-service messaging but rarely in pure UI.

Do not use `Heshima` ("respect" / royal we) or archaic forms. They sound formal-stilted.

## Critical Hard Rules

### Noun Class System (severity 3.0 — THE single most important Swahili rule)

Swahili has **15–18 noun classes**, traditionally numbered 1–18 (some classes are rare or merged in modern usage). Each noun belongs to a class indicated by its prefix; the class governs the prefixes of every agreeing word in the sentence (adjectives, verbs, possessives, demonstratives, relative pronouns). This is **concord**, and getting it wrong is the most common and most jarring translation error.

The 9 core class pairs (singular/plural) plus standalone classes:

| # | Sg/Pl | Noun prefix | Subject prefix | Adj prefix | Possessive prefix | Demonstrative | Typical content | Examples |
|---|---|---|---|---|---|---|---|---|
| 1/2 | M-/Wa- | m-/wa- | a-/wa- | m-/wa- | wangu/wetu... | huyu/hawa | **People** | mtu/watu (person/people), mtoto/watoto (child/children), mwalimu/walimu (teacher/teachers), mtumiaji/watumiaji (user/users) |
| 3/4 | M-/Mi- | m-/mi- | u-/i- | m-/mi- | wangu/yangu... | huu/hii | **Plants, body parts, abstract, natural forces** | mti/miti (tree/trees), mkono/mikono (hand/hands), mlima/milima (mountain/mountains), mfumo/mifumo (system/systems) |
| 5/6 | Ji-/Ma- | (Ø)/ma- | li-/ya- | (Ø)/ma- | langu/yangu... | hili/haya | **Augmentatives, collectives, paired body parts, fruits** | jicho/macho (eye/eyes), jiwe/mawe (stone/stones), jina/majina (name/names), tunda/matunda (fruit/fruits), tokeo/matokeo (result/results) |
| 7/8 | Ki-/Vi- | ki-/vi- | ki-/vi- | ki-/vi- | changu/vyangu... | hiki/hivi | **Things, manner, instruments, languages, diminutives** | kitu/vitu (thing/things), kiti/viti (chair/chairs), kitabu/vitabu (book/books), kitufe/vitufe (button/buttons), **Kiswahili (language names are class 7)** |
| 9/10 | N-/N- | (Ø)/(Ø) | i-/zi- | (Ø)/(Ø) | yangu/zangu... | hii/hizi | **Animals, abstract nouns, loanwords (including most English/Arabic tech terms)** | mbwa/mbwa (dog/dogs, same), ndege/ndege (bird/birds, same), nyumba/nyumba (house/houses), **faili/faili** (file/files), **kompyuta/kompyuta** (computer/computers), barua/barua (letter/letters) |
| 11/(10) | U- | u- | u-/zi- | wangu/zangu | huu/hizi | **Abstracts, mass nouns, long thin things** (plural shifts to class 10) | uhuru (freedom — usually no plural), upendo (love — no plural), wakati/nyakati (time/times — irregular pl) |
| 14 | U- | u- | u- | wangu | huu | **Abstract nouns** (often no plural) | ujamaa (family/community/socialism), ukweli (truth), umoja (unity) |
| 15 | Ku- | ku- | ku- | (—) | (—) | (—) | **Verbal infinitives, gerunds** (verb-nouns) | kufanya (to do / doing), kusoma (to read / reading), kuhifadhi (to save / saving) |
| 16 | Pa- (locative) | pa- | pa- | — | — | hapa | **Specific location** (formed with -ni suffix on a noun) | nyumbani (at home), shuleni (at school), faili**ni** (in the file) |
| 17 | Ku- (locative) | ku- | ku- | — | — | huku | **General/indefinite location, direction** | kule (over there), kwenye (at/in — preposition) |
| 18 | Mu-/Mw- (locative) | m(u)- | mu- | — | — | humu | **Inside (enclosed)** | ndani (inside), mwituni (in the forest) |

**Concord example — a complete sentence with class agreement spreading:**

> `Mtumiaji huyu mzuri anasoma kitabu chake kipya.`
> = "This good user is reading their new book."

Breaking it down:
- `mtumiaji` (user) — class 1 (M-Wa)
- `huyu` (this) — class 1 demonstrative
- `mzuri` (good) — class 1 adjective prefix m-
- `a-na-soma` (he/she-PRES-read) — class 1 subject prefix a-
- `kitabu` (book) — class 7 (Ki-Vi)
- `chake` (his/her) — class 7 possessive prefix ch- (a phonological variant of ki-)
- `kipya` (new) — class 7 adjective prefix ki-

The class of `mtumiaji` (class 1) controls `huyu`, `mzuri`, and the verb prefix `a-`. The class of `kitabu` (class 7) controls `chake` and `kipya`. The two classes do NOT cross over.

**Concord in plural:**

> `Watumiaji hawa wazuri wanasoma vitabu vyao vipya.`

- `watumiaji` (users) — class 2
- `hawa` (these) — class 2 demonstrative
- `wazuri` (good, pl) — class 2 adjective prefix wa-
- `wa-na-soma` — class 2 subject prefix wa-
- `vitabu` (books) — class 8
- `vyao` (their) — class 8 possessive prefix vy-
- `vipya` (new, pl) — class 8 adjective prefix vi-

**The most common concord errors in UI translation:**

| Wrong | Correct | Why |
|---|---|---|
| `faili mpya` (with class-9 prefix on adj) | `faili jipya` (often) OR `faili mpya` (acceptable — see note) | Class 9 N-class typically has Ø prefix on adjectives, so adjectives starting with vowel get N- or the bare form; the rule is complicated by whether the adjective is Bantu (takes prefix) or Arabic (no prefix). `mpya` happens to be invariant here. |
| `kitufe mpya` | `kitufe kipya` | Class 7 button needs class-7 prefix ki- on the adjective |
| `mifumo mpya` | `mifumo mipya` | Class 4 plural systems need class-4 prefix mi- on the adjective |
| `matokeo nzuri` | `matokeo mazuri` | Class 6 results need class-6 prefix ma- on the adjective |
| `watumiaji wengi` | `watumiaji wengi` (correct) | Class 2 users with class-2 wa- prefix (here `w-` because of vowel sandhi) |

**Subject-prefix-on-verb errors:**

| Wrong | Correct | Why |
|---|---|---|
| `Faili **a**nahifadhiwa` | `Faili **i**nahifadhiwa` | Class 9 (faili) takes i-, not a- (class 1) |
| `Mfumo **i**nafanya kazi` | `Mfumo **u**nafanya kazi` | Class 3 (mfumo) takes u-, not i- (class 9) |
| `Vitufe **i**nafanya kazi` | `Vitufe **vi**nafanya kazi` | Class 8 (vitufe) takes vi-, not i- |
| `Matokeo **i**meonekana` | `Matokeo **ya**meonekana` | Class 6 (matokeo) takes ya-, not i- |
| `Watumiaji **a**meingia` | `Watumiaji **wa**meingia` | Class 2 (watumiaji) takes wa-, not a- |

**Quick lookup table for UI nouns and their classes:**

| English | Swahili | Class (sg/pl) | Subject prefix (sg/pl) | Adjective prefix (sg/pl) |
|---|---|---|---|---|
| user | mtumiaji / watumiaji | 1/2 | a-/wa- | m-/wa- |
| system | mfumo / mifumo | 3/4 | u-/i- | m-/mi- |
| setting | mpangilio / mipangilio | 3/4 | u-/i- | m-/mi- |
| button | kitufe / vitufe | 7/8 | ki-/vi- | ki-/vi- |
| file | faili / faili | 9/10 | i-/zi- | (no prefix) |
| folder | folda / folda | 9/10 | i-/zi- | (no prefix) |
| password | nenosiri / manenosiri (or nywila) | 5/6 (or 9/10) | li-/ya- | (Ø/ma-) |
| message | ujumbe / jumbe | 11/10 | u-/zi- | (varies) |
| result | tokeo / matokeo | 5/6 | li-/ya- | (Ø/ma-) |
| document | hati / hati | 9/10 | i-/zi- | (no prefix) |
| account | akaunti / akaunti | 9/10 | i-/zi- | (no prefix) |
| email | barua pepe / barua pepe | 9/10 | i-/zi- | (no prefix) |
| link | kiungo / viungo | 7/8 | ki-/vi- | ki-/vi- |
| browser | kivinjari / vivinjari | 7/8 | ki-/vi- | ki-/vi- |
| window | dirisha / madirisha | 5/6 | li-/ya- | (Ø/ma-) |
| computer | kompyuta / kompyuta | 9/10 | i-/zi- | (no prefix) |
| network | mtandao / mitandao | 3/4 | u-/i- | m-/mi- |
| server | seva / seva | 9/10 | i-/zi- | (no prefix) |
| screen | skrini / skrini | 9/10 | i-/zi- | (no prefix) |
| language | lugha / lugha | 9/10 | i-/zi- | (no prefix) |

**Memorization shortcut:** Most English tech loanwords land in **class 9/10 (N-class)** — same form for singular and plural, takes `i-/zi-` subject prefixes, and adjectives generally appear in their bare form. This is why `faili imehifadhiwa` works the same for one file or many files (you'd add a number to disambiguate).

### Verb Morphology — Agglutinative Stacking (severity 2.5)

Swahili verbs are built by stacking morphemes in a fixed order:

```
Subject prefix (SM) + Tense/Aspect (TAM) + (Object prefix OM) + Verb root + (Extension) + Final vowel (FV)
```

Worked example:
- `a-li-ki-pik-i-a` = "he/she-PAST-it-cook-applied-FINAL"
- Translation: "he/she cooked it for [someone]"
- Morpheme by morpheme:
  - `a-` = 3rd person singular subject (class 1)
  - `-li-` = past tense marker
  - `-ki-` = object marker (class 7 "it")
  - `-pik-` = verb root "cook"
  - `-i-` = applicative extension ("for/to")
  - `-a` = final vowel (indicative)

**Subject prefixes (personal):**

| Person | Subject prefix | Example with -soma (read) |
|---|---|---|
| 1sg (I) | ni- | ninasoma (I read) |
| 2sg (you) | u- | unasoma (you read) |
| 3sg (he/she) | a- | anasoma (he/she reads) |
| 1pl (we) | tu- | tunasoma (we read) |
| 2pl (you all) | m- | mnasoma (you all read) |
| 3pl (they, people) | wa- | wanasoma (they read) |

For non-person subjects, the subject prefix matches the noun class (see noun class table above).

**Tense/Aspect markers (TAM):**

| Marker | Meaning | Example (a- subject) | Translation |
|---|---|---|---|
| -na- | present (general/progressive) | anasoma | he/she reads / is reading |
| -li- | past (simple) | alisoma | he/she read |
| -ta- | future | atasoma | he/she will read |
| -me- | perfect (completed, result-state) | amesoma | he/she has read |
| -ki- | conditional / "while" / "if" | akisoma | if/while he/she reads |
| -nge- | hypothetical "would" | angesoma | he/she would read |
| -ngali- | counterfactual "would have" | angalisoma | he/she would have read |
| -ja- | "not yet" (negative perfect) | hajasoma | he/she hasn't read yet |
| hu- | habitual (no subject prefix) | husoma | he/she usually reads |
| -∅- | subjunctive (bare, final vowel -e) | asome | he/she should read |
| -ka- | consecutive ("and then") | akasoma | and then he/she read |

**Extensions (verb-final suffixes that modify meaning):**

| Suffix | Function | Example |
|---|---|---|
| -i- / -e- | applicative ("for/to") | piki**a** = cook for; somea (read to) |
| -ish- / -esh- | causative ("make X happen") | somesha = teach (make read); pikisha = make cook |
| -ek- / -ik- | stative / potential ("be Xable") | someka = be readable; pikika = be cookable |
| -w- (before final -a) | passive | somwa = be read; pikwa = be cooked; hifadhiwa = be saved |
| -an- | reciprocal ("each other") | somana = read each other; saidiana = help each other |

**Common UI verb patterns:**

| English UI form | Swahili | Morpheme breakdown |
|---|---|---|
| Saving... (system status) | Inahifadhi... | i- (class 9 SM) -na- (PRES) hifadhi (root) |
| Saved | Imehifadhiwa | i- (class 9) -me- (PERF) hifadhi (root) -w- (PASS) -a (FV) |
| Save (button) | Hifadhi | bare imperative — verb root as command |
| Will save (future status) | Itahifadhiwa | i- (class 9) -ta- (FUT) hifadhi -w- -a |
| Not saved yet | Haijahifadhiwa | ha- (NEG) -i- (class 9 SM) -ja- (not yet) hifadhi -w- -a |
| Loading... | Inapakia... | i- -na- pakia |
| Loaded | Imepakia (intrans) / Imepakiwa (passive) | i- -me- pakia (-w-) -a |
| Click here | Bofya hapa | bofya imperative + hapa "here" |
| Please click | Tafadhali bofya | tafadhali (Arabic loan, "please") + bofya |
| You should save | Uhifadhi | u- (2sg SM) hifadhi -i (subjunctive FV — i replaces final -i but irregular here, often written uhifadhi) |
| Don't save | Usihifadhi | u- (2sg) -si- (negative subjunctive) hifadhi |

**The status-vs-command distinction:**

- **System status messages** use the impersonal class-9 prefix `i-` (or the appropriate class for the subject noun) + tense marker:
  - `Inapakia...` = it/the-file is loading
  - `Imehifadhiwa` = it has been saved
- **Commands/buttons** use the bare imperative (just the verb root with final vowel):
  - `Hifadhi` = Save!
  - `Futa` = Delete!
  - `Tuma` = Send!
- **DO NOT** mix first/second person into system status: ❌ `Ninapakia faili yako...` ("I am loading your file") — too personal. ✅ `Inapakia...`

### Concord on Adjectives — The "kitufe mpya" Trap (severity 2.5)

Adjectives in Swahili come **AFTER the noun** and **take a concord prefix** that matches the noun's class. This is one of the most error-prone areas because:

1. Many English-derived loan adjectives (in class 9) appear unchanged.
2. Bantu-origin adjectives almost always change.
3. The prefix form sometimes drops or assimilates phonologically.

**Bantu adjective stems that take concord:**

| Stem | Meaning | Class 1 sg | Class 2 pl | Class 3 sg | Class 4 pl | Class 7 sg | Class 8 pl | Class 9 sg | Class 10 pl |
|---|---|---|---|---|---|---|---|---|---|
| -pya | new | mpya | wapya | mpya | mipya | kipya | vipya | mpya | mpya |
| -zuri | good/beautiful | mzuri | wazuri | mzuri | mizuri | kizuri | vizuri | nzuri | nzuri |
| -baya | bad | mbaya | wabaya | mbaya | mibaya | kibaya | vibaya | mbaya | mbaya |
| -dogo | small | mdogo | wadogo | mdogo | midogo | kidogo | vidogo | ndogo | ndogo |
| -kubwa | big | mkubwa | wakubwa | mkubwa | mikubwa | kikubwa | vikubwa | kubwa | kubwa |
| -refu | long/tall | mrefu | warefu | mrefu | mirefu | kirefu | virefu | ndefu | ndefu |
| -eupe | white/clear | mweupe | weupe | mweupe | myeupe | cheupe | vyeupe | nyeupe | nyeupe |

**Loan adjectives (mostly Arabic, English) — INVARIANT (no concord):**

| Adjective | Meaning |
|---|---|
| bora | best/excellent |
| safi | clean/fine |
| ghali | expensive |
| rahisi | easy/cheap |
| tayari | ready |
| hodari | skilled/capable |
| muhimu | important |
| salama | safe/peaceful |

These are used as-is regardless of noun class: `kitufe rahisi`, `mfumo rahisi`, `matokeo rahisi`, `watumiaji rahisi` (though semantics may force a different word).

**Worked examples:**

| Wrong | Correct | Class explanation |
|---|---|---|
| `kitufe mpya` ❌ | `kitufe kipya` ✅ | Class 7 → ki- prefix on -pya |
| `mfumo kipya` ❌ | `mfumo mpya` ✅ | Class 3 → m- prefix on -pya (mpya, identical to class 1) |
| `mifumo mpya` ❌ | `mifumo mipya` ✅ | Class 4 plural → mi- prefix on -pya |
| `vitufe mpya` ❌ | `vitufe vipya` ✅ | Class 8 plural → vi- prefix on -pya |
| `matokeo mazuri` ✅ | `matokeo mazuri` ✅ | Class 6 → ma- prefix on -zuri (correct) |
| `faili kubwa` ✅ | `faili kubwa` ✅ | Class 9 → bare/Ø prefix on -kubwa (correct as-is) |
| `nyumba kubwa` ✅ | `nyumba kubwa` ✅ | Class 9 → bare prefix (correct) |
| `watu wengi` ✅ | `watu wengi` ✅ | Class 2 → wa- prefix on -ingi → wengi (vowel sandhi) |
| `vitabu vingi` ✅ | `vitabu vingi` ✅ | Class 8 → vi- + -ingi → vingi |

### Possessives — Agree with the POSSESSED, Not the Possessor (severity 2.0)

Possessive pronouns in Swahili agree with the **possessed noun's class**, not the possessor's gender or number. The stem is the person/number of the possessor, the prefix is the class of the possessed thing.

**Possessor stems:**

| Possessor | Stem |
|---|---|
| my (1sg) | -angu |
| your sg (2sg) | -ako |
| his/her (3sg) | -ake |
| our (1pl) | -etu |
| your pl (2pl) | -enu |
| their (3pl) | -ao |

**Concord prefix on possessive by class:**

| Class | Prefix | "my" | "your sg" | "his/her" | "our" | "your pl" | "their" |
|---|---|---|---|---|---|---|---|
| 1 (mtu) | w- | wangu | wako | wake | wetu | wenu | wao |
| 2 (watu) | w- | wangu | wako | wake | wetu | wenu | wao |
| 3 (mfumo) | w- | wangu | wako | wake | wetu | wenu | wao |
| 4 (mifumo) | y- | yangu | yako | yake | yetu | yenu | yao |
| 5 (tokeo) | l- | langu | lako | lake | letu | lenu | lao |
| 6 (matokeo) | y- | yangu | yako | yake | yetu | yenu | yao |
| 7 (kitabu) | ch- | changu | chako | chake | chetu | chenu | chao |
| 8 (vitabu) | vy- | vyangu | vyako | vyake | vyetu | vyenu | vyao |
| 9 (faili) | y- | yangu | yako | yake | yetu | yenu | yao |
| 10 (faili pl) | z- | zangu | zako | zake | zetu | zenu | zao |
| 11 (uhuru) | w- | wangu | wako | wake | wetu | wenu | wao |
| 14 (ujamaa) | w- | wangu | wako | wake | wetu | wenu | wao |

Worked examples:

| English | Swahili | Class |
|---|---|---|
| my book | kitabu **changu** | 7 |
| my books | vitabu **vyangu** | 8 |
| my people | watu **wangu** | 2 |
| my file | faili **yangu** | 9 |
| my files | faili **zangu** | 10 (same noun, possessive differs!) |
| my system | mfumo **wangu** | 3 |
| my systems | mifumo **yangu** | 4 |
| my result | tokeo **langu** | 5 |
| my results | matokeo **yangu** | 6 |
| your account | akaunti **yako** | 9 |
| your accounts | akaunti **zako** | 10 |
| our settings | mipangilio **yetu** | 4 |
| their messages | jumbe **zao** | 10 |

### Subject Pronouns are PRO-DROP (severity 1.5)

Because the verb prefix already encodes the subject, the standalone subject pronouns (`mimi`, `wewe`, `yeye`, `sisi`, `ninyi`, `wao`) are **omitted** in most contexts. They appear only for emphasis or contrast.

| Wrong (overuses pronoun) | Correct (pro-drop) |
|---|---|
| Wewe unaweza kuhifadhi faili. | Unaweza kuhifadhi faili. ✅ |
| Mimi ninapakia... | Inapakia... ✅ (impersonal system voice) |
| Sisi tunapakia faili yako | Inapakia... ✅ |

For UI imperatives, drop pronouns entirely: `Hifadhi`, `Futa`, `Bofya hapa` — never `Wewe hifadhi`, `Wewe futa`, `Wewe bofya hapa`.

### SVO Word Order (severity 1.5)

Neutral declarative sentences follow Subject-Verb-Object. Word order is flexible because the verb morphology marks subject (via SM) and object (via OM), but UI strings should stick to SVO for clarity.

| Wrong | Correct | Why |
|---|---|---|
| `Faili mpya alifungua mtumiaji` ❌ | `Mtumiaji alifungua faili mpya` ✅ | SVO: user-opened-new-file |
| `Imehifadhiwa faili` ❌ (VS, marked) | `Faili imehifadhiwa` ✅ | Neutral statements put subject first |

VSO order **is grammatical** but signals emphasis/contrast — inappropriate for plain UI status messages.

### No Articles — Definiteness from Context (severity 1.0)

Swahili has **no a/the articles**. Definiteness is inferred from context, demonstratives (`huyu`, `hii`, `hiki`), or the object marker on the verb. Do NOT translate English "the" or "a/an" with anything; just drop them.

| English | Swahili |
|---|---|
| Save **a** file | Hifadhi faili |
| Save **the** file | Hifadhi faili (context decides) |
| Save **this** file | Hifadhi faili **hili** (demonstrative class 5/9 in some uses) — use `hii` for class 9: Hifadhi faili **hii** |

If you need to make definiteness explicit, use a **demonstrative** (`huyu`, `hawa`, `huu`, `hii`, `hiki`, `hivi`, `lile`, `yale`, `kile`, `vile`) or an **object marker** on the verb (`-ki-` for class 7, `-i-` for class 9, etc.).

### Negation (severity 2.0)

Swahili negates verbs by changing the subject prefix and (sometimes) adding a tense-specific suffix.

| Affirmative | Negative present | Negative past | Negative perfect (not yet) | Negative future |
|---|---|---|---|---|
| Ninasoma (I read) | Sisomi | Sikusoma | Sijasoma | Sitasoma |
| Unasoma | Husomi | Hukusoma | Hujasoma | Hutasoma |
| Anasoma | Hasomi | Hakusoma | Hajasoma | Hatasoma |
| Tunasoma | Hatusomi | Hatukusoma | Hatujasoma | Hatutasoma |
| Mnasoma | Hamsomi | Hamkusoma | Hamjasoma | Hamtasoma |
| Wanasoma | Hawasomi | Hawakusoma | Hawajasoma | Hawatasoma |

Pattern:
- Present negative: subject-prefix replaced by `ha-` (`hu-`, `ha-`, etc.) + verb root with final **-i** (not -a)
- Past negative: subject-prefix replaced by `ha-` + `-ku-` + verb root + final -a
- Perfect negative ("not yet"): `ha-` subject + `-ja-` + verb root + final -a — **NOT just adding "si"**

For non-person subjects, use the class negative form:

| Class | Affirmative | Negative present | Negative perfect |
|---|---|---|---|
| 9 (faili) | Inahifadhiwa | Haihifadhiwi | Haijahifadhiwa |
| 3 (mfumo) | Unafanya kazi | Haufanyi kazi | Haujafanya kazi |
| 7 (kitufe) | Kinabofyeka | Hakibofyeki | Hakijabofyeka |

| Wrong | Correct | Why |
|---|---|---|
| `Faili si imehifadhiwa` ❌ | `Faili haijahifadhiwa` ✅ | Use ha-...-ja- for negative perfect, not "si imehifadhiwa" |
| `Si inafanya kazi` ❌ | `Haifanyi kazi` ✅ | Class 9 negative present is hai-...-i |
| `Hawakuwa wameingia` ⚠ | `Hawakuingia` / `Hawajaingia` ✅ | Don't stack negatives; use the right negative tense |

### Numbers and Counting Concord (severity 2.0)

Cardinal numbers **1–5 agree with noun class** (taking a concord prefix). Numbers **6 and above are invariant** (no concord — they appear as bare numerals or in their Arabic-derived form).

| Numeral | Class 1/2 (mtu) | Class 3/4 (mfumo) | Class 7/8 (kitabu) | Class 9/10 (faili) |
|---|---|---|---|---|
| 1 | mtu **mmoja** | mfumo **mmoja** | kitabu **kimoja** | faili **moja** |
| 2 | watu **wawili** | mifumo **miwili** | vitabu **viwili** | faili **mbili** |
| 3 | watu **watatu** | mifumo **mitatu** | vitabu **vitatu** | faili **tatu** |
| 4 | watu **wanne** | mifumo **minne** | vitabu **vinne** | faili **nne** |
| 5 | watu **watano** | mifumo **mitano** | vitabu **vitano** | faili **tano** |
| 6 | watu **sita** | mifumo **sita** | vitabu **sita** | faili **sita** |
| 7+ | watu saba, nane, tisa, kumi... | (all invariant) | | |

**Critical rule:** Numbers 6 and above are Arabic loans (sita, saba, nane, tisa, ishirini, hamsini, mia, elfu) and they do not take noun-class concord.

| English | Swahili |
|---|---|
| 1 user | mtumiaji mmoja |
| 2 users | watumiaji wawili |
| 5 users | watumiaji watano |
| 6 users | watumiaji sita (no concord) |
| 10 users | watumiaji kumi |
| 25 users | watumiaji ishirini na watano (← `watano` concords because of "5" inside "25") |
| 100 users | watumiaji mia moja (or `watumiaji 100`) |
| 1 file | faili moja |
| 5 files | faili tano |
| 100 files | faili 100 (or faili mia moja) |

**ICU plurals** — Swahili has two CLDR categories: `one` and `other`. Both render with the morphological plural form via the noun's class prefix; the number agreement is encoded in the noun's class itself, not in extra plural forms.

```icu
{count, plural,
  one {faili # / # faili}
  other {faili # / # faili}
}
```

Note: Because class 9/10 nouns (faili, kompyuta, akaunti) don't change form between singular and plural, only the verb agreement changes. For class 7/8 (kitufe/vitufe), 3/4 (mfumo/mifumo), 1/2 (mtumiaji/watumiaji) etc., the noun form MUST switch:

```icu
{count, plural,
  one {mtumiaji #}
  other {watumiaji #}
}

{count, plural,
  one {kitufe kimoja}
  other {vitufe #}
}
```

### Passive Voice (severity 1.5)

Swahili passives are formed by inserting `-w-` before the final vowel of the verb root. Used heavily in UI status messages.

| Active (root) | Passive | Meaning |
|---|---|---|
| hifadhi | hifadhi**w**a | be saved |
| futa | fut**w**a | be deleted |
| tuma | tum**w**a | be sent |
| pakia | paki**w**a | be loaded/uploaded |
| pakua | pakuli**w**a | be downloaded |
| ona | on**ek**ana / on**w**a | be seen |
| chagua | chagu**li**wa | be chosen |

Full passive form in UI status (class 9 subject, perfect tense):

| Active concept | Passive UI form |
|---|---|
| Saved | Imehifadhi**w**a |
| Deleted | Imefut**w**a |
| Sent | Imetum**w**a |
| Uploaded | Imepaki**w**a |
| Downloaded | Imepaku**li**wa |
| Selected | Imechagu**li**wa |

### The "Fanya + Noun" Calque (severity 1.5)

English often uses **make/do + noun** ("make a decision", "do a search", "make changes"). Swahili usually has a **single-verb equivalent** that sounds more natural.

| Wrong (fanya + noun) | Correct (single verb) | Meaning |
|---|---|---|
| fanya mabadiliko | **badilisha** | make changes / change |
| fanya uamuzi | **amua** | make a decision / decide |
| fanya uchaguzi | **chagua** | make a selection / choose |
| fanya utafiti | **tafuta** | do a search / search |
| fanya usasishaji | **sasisha** | do an update / update |
| fanya uhifadhi | **hifadhi** | do a save / save |
| fanya usafishaji | **safisha** | do cleaning / clean |
| fanya marekebisho | **rekebisha** | make corrections / correct |
| fanya muunganisho | **unganisha** | make a connection / connect |

**When `fanya` IS appropriate:**
- Abstract or culturally-loaded actions: `fanya kazi` (work — literally "do work"), `fanya hesabu` (do math), `fanya mazoezi` (do exercise).
- When the noun is the specific point: `fanya mtihani` (sit an exam).

### Latin Alphabet with `ng'` (severity 1.5)

Swahili uses standard Latin script with these letters: `a, b, c, ch, d, dh, e, f, g, gh, h, i, j, k, l, m, n, ng, ng', ny, o, p, r, s, sh, t, th, u, v, w, y, z`.

Key points:
- **`ng'` with an apostrophe** is a **distinct letter** (velar nasal /ŋ/), separate from the digraph **`ng`** (nasal+stop /ŋg/). They are NOT interchangeable.
  - `ng'ombe` = cow (/ŋombe/)
  - `nguo` = cloth (/ŋguo/)
  - `ng'ang'ania` = cling to (note the repeated `ng'`)
- **`dh`, `gh`, `th`** appear in Arabic loanwords: `dhambi` (sin), `ghali` (expensive), `thelathini` (thirty). These represent the original Arabic sounds /ð/, /ɣ/, /θ/, though many speakers pronounce them as /z/, /g/, /s/.
- **`c`** alone is rare; mostly appears in proper nouns or as part of `ch`.
- **No tones, no accents.** Swahili lost the Bantu tone system entirely. Pronunciation is predictable from spelling.
- **Stress on penultimate syllable** (the second-to-last). Affects UI reading rhythm: `ki-TA-bu`, `mtu-MIA-ji`, `Kis-wa-HI-li`.

### Time — Two Systems (severity 1.0)

Swahili has a traditional time-keeping system that differs from Western time by 6 hours:

**Traditional Swahili time (Saa za Kiswahili):** Day starts at 6 AM = `saa moja asubuhi` (hour 1 morning). So:
- 6:00 AM = saa kumi na mbili usiku / saa moja asubuhi
- 9:00 AM = saa tatu asubuhi (hour 3 morning)
- 12:00 noon = saa sita mchana (hour 6 midday)
- 3:00 PM = saa tisa mchana (hour 9 afternoon)
- 6:00 PM = saa kumi na mbili jioni (hour 12 evening)
- 9:00 PM = saa tatu usiku (hour 3 night)

**Standard / international time (Saa za kimagharibi):** Used in all modern UI, schedules, transport, broadcasting:
- 9:00 (am/asubuhi), 14:30, 21:00

**UI rule:** Use 24-hour international format (`14:30`) or 12-hour with `asubuhi/mchana/jioni/usiku` (morning/midday/afternoon/night) for AM/PM. Avoid traditional saa-based time in software UIs unless culturally targeted.

| Wrong | Correct |
|---|---|
| `saa 3 asubuhi` (for 9 AM, in tech UI) | `9:00` or `9:00 asubuhi` |
| `saa kumi mchana` (for 4 PM) | `16:00` or `4:00 mchana` |

### Currency — Country-Specific (severity 1.0)

| Country | Code | Symbol | Format | Notes |
|---|---|---|---|---|
| Tanzania | TZS | TSh or **/=** | `TSh 1,000` or `1,000/=` | The `/=` is traditional Tanzanian currency notation (equivalent to "shillings flat"). Both are widely understood. |
| Kenya | KES | KSh or Ksh. | `KSh 1,000` or `Ksh. 1,000` | KSh is standard; Ksh. is older formal style. |
| Uganda | UGX | USh | `USh 1,000` | |
| DRC | CDF | Fr or FC | `Fr 1,000` or `1,000 FC` | French-derived "franc congolais"; US dollars also widely used in commerce. |
| Rwanda | RWF | RF or FRw | `RF 1,000` | |
| Burundi | BIF | FBu | `FBu 1,000` | |

**For pan-EAC or cross-country UI:**
- Show the amount in figures with no specific symbol, or use the ISO code (`TZS 1,000`) for clarity.
- Avoid hardcoding a single country's currency in shared UI.

### Numbers and Decimal Format (severity 1.0)

Swahili (under English colonial-era influence) follows the **Anglo-style numeric convention**:
- **Comma** for thousands: `1,234`, `1,234,567`
- **Period** for decimals: `3.14`, `0.5`

(Contrast with European-style `1.234,56` which is NOT used.)

| Wrong | Correct |
|---|---|
| `3,14` | `3.14` |
| `1.000` (for one thousand) | `1,000` |
| `1 000` (space thousands, French-style) | `1,000` |

Very large numbers can use words:
- `mia moja` = 100
- `elfu moja` = 1,000
- `milioni moja` = 1,000,000
- `bilioni moja` = 1,000,000,000

### Dates (severity 1.0)

**Numeric format:** `DD/MM/YYYY` (day-first, slash-separated). Example: `15/01/2024`.

**Long form (formal/written):** `15 Januari 2024` or `Tarehe 15 mwezi wa Januari mwaka 2024` (date 15 month-of January year 2024).

**Month names** (capitalized, English-derived):

| # | Swahili | English |
|---|---|---|
| 1 | Januari | January |
| 2 | Februari | February |
| 3 | Machi | March |
| 4 | Aprili | April |
| 5 | Mei | May |
| 6 | Juni | June |
| 7 | Julai | July |
| 8 | Agosti | August |
| 9 | Septemba | September |
| 10 | Oktoba | October |
| 11 | Novemba | November |
| 12 | Desemba | December |

**Days of the week** (Swahili days mix Bantu numerical counting with Arabic religious tradition):

| Swahili | English | Etymology |
|---|---|---|
| Jumatatu | Monday | "first gathering day" |
| Jumanne | Tuesday | "second gathering" |
| Jumatano | Wednesday | "third gathering" |
| Alhamisi | Thursday | Arabic al-khamīs ("the fifth") |
| Ijumaa | Friday | Arabic al-jumʿa ("congregation" — Muslim prayer day) |
| Jumamosi | Saturday | "Moses day" (from Arabic) |
| Jumapili | Sunday | "Apollo day" / "first" |

**Wrong/Right:**

| Wrong | Correct |
|---|---|
| `01/15/2024` (US format) | `15/01/2024` |
| `2024-01-15` (ISO — acceptable but unusual in pure-Swahili UI) | `15/01/2024` or `15 Januari 2024` |
| `january` (lowercase) | `Januari` (capitalized) |

### Comma and Punctuation Rules (severity 1.0)

- **NO comma before** `na` (and), `au` (or), `wala` (nor): `Hifadhi faili au funga dirisha` (NOT `Hifadhi faili, au funga dirisha`).
- **COMMA before** `lakini` (but), `kwa sababu` (because), `ingawa` (although), `ili` (so that), `kwamba` (that), `kama` (if), `wakati` (when): `Imeshindikana, kwa sababu seva haijibu.`
- **Quotation marks:** standard double quotes `"..."`. Single quotes `'...'` for nested.

### Religious and Cultural Neutrality (severity 1.0)

East Africa is religiously diverse:
- Tanzania: ~60% Christian, ~35% Muslim (Zanzibar is 99% Muslim).
- Kenya: ~85% Christian, ~10% Muslim, indigenous religions present.
- Uganda: ~85% Christian, ~12% Muslim.
- Coastal regions (Swahili coast): historically Muslim majority.

UI guidelines:
- **Avoid religious salutations** (`Asalaam aleikum` — Muslim greeting; `Bwana asifiwe` — Christian "praise the Lord") in default UI.
- Default greeting: `Habari` (hello — neutral, lit. "news") or `Karibu` (welcome).
- Holiday names should be religion-neutral or country-specific: `Sikukuu ya Idi` (Eid), `Krismasi` (Christmas), `Pasaka` (Easter), `Mwaka Mpya` (New Year).
- Default date references use Gregorian calendar.

### Cross-EAC Terminology Respect (severity 1.0)

Tanzanian and Kenyan Swahili sometimes prefer different terms for the same concept. UI for pan-East-African use should:
- Prefer the term that is **mutually understood** in both countries.
- Avoid heavily Kenya-specific or Tanzania-specific colloquialisms.

| Concept | Tanzanian-leaning | Kenyan-leaning | Pan-EAC safe |
|---|---|---|---|
| Computer | kompyuta | kompyuta / computer | **kompyuta** |
| Phone | simu | simu | **simu** |
| Money | pesa | pesa / hela / doh (Sheng) | **pesa** |
| OK / yes | sawa / ndiyo | sawa / sawa-sawa / poa (Sheng) | **sawa / ndiyo** |
| Friend | rafiki | rafiki / jamaa | **rafiki** |
| Now | sasa | sasa / saa hii | **sasa** |
| Cool/great | nzuri / vizuri | poa (Sheng) / safi | **nzuri / vizuri** |

## UI Conventions

### Button Labels — Bare Imperative

Swahili buttons use the **imperative stem** — the verb root with its final vowel (`-a` for most, `-i` for Arabic loans). NOT the infinitive (`ku-`), NOT present-tense `ina-/una-`, NOT subjunctive (`-e` final).

| Wrong | Correct | Notes |
|---|---|---|
| `Kuhifadhi` (infinitive) | **Hifadhi** | Drop ku- |
| `Unahifadhi` (present 2sg) | **Hifadhi** | Drop subject + tense |
| `Uhifadhi` (subjunctive — overly polite) | **Hifadhi** | Subjunctive is for embedded clauses |
| `Bonyeza hapa ili kuhifadhi` (verbose) | **Hifadhi** | Be concise |
| `Tafadhali hifadhi` (please save) | **Hifadhi** | `Tafadhali` only for high-stakes prompts |

| English | Swahili button |
|---|---|
| Save | Hifadhi |
| Delete | Futa |
| Cancel | Ghairi / Sitisha |
| OK | Sawa |
| Submit | Wasilisha |
| Send | Tuma |
| Upload | Pakia |
| Download | Pakua |
| Select | Chagua |
| Edit | Hariri |
| Copy | Nakili |
| Paste | Bandika |
| Cut | Kata |
| Close | Funga |
| Open | Fungua |
| Sign in / Log in | Ingia |
| Sign out / Log out | Toka |
| Sign up / Register | Jisajili |
| Search | Tafuta |
| Next | Endelea / Inayofuata |
| Previous | Rudi / Iliyopita |
| Back | Rudi |
| Continue | Endelea |
| Update | Sasisha |
| Refresh | Onyesha upya |
| Confirm | Thibitisha |
| Apply | Tumia |
| Print | Chapisha |

### Status Messages — Impersonal Voice

Status messages use the **class prefix + tense marker** structure, never first/second person.

| Message type | Pattern | Example |
|---|---|---|
| Ongoing | class-prefix + `-na-` + verb (+ trailing ellipsis) | `Inapakia...` (Loading...) `Inahifadhi...` (Saving...) `Inatuma...` (Sending...) |
| Completed | class-prefix + `-me-` + verb (passive `-w-`) | `Imehifadhiwa` (Saved) `Imefutwa` (Deleted) `Imekamilika` (Completed) |
| Failed | `Imeshindikana` or class + `-me-` + verb of failure | `Imeshindikana` (Failed) `Imeshindwa kupakia` (Failed to load) |
| Not yet | class-prefix + `ha-...-ja-` | `Haijahifadhiwa` (Not saved yet) |

| Wrong | Correct |
|---|---|
| `Ninahifadhi faili yako` (1st person) | `Inahifadhi...` |
| `Tunapakia...` (we-form) | `Inapakia...` |
| `Mimi nimekamilisha` | `Imekamilika` |
| `Faili imehifadhiwa kwa mafanikio` (verbose) | `Faili imehifadhiwa` (concise) |

### Drag-and-Drop Vocabulary

| English | Swahili | Notes |
|---|---|---|
| drag | **buruta** | native Bantu verb |
| drop | **dondosha** | causative of -dondoka (to drip/fall) |
| release / let go | **achia** | from -acha (leave) |

| Wrong | Correct |
|---|---|
| `Drag faili hapa` ❌ | `Buruta faili hapa` ✅ |
| `Drop hapa kupakia` ❌ | `Dondosha hapa ili kupakia` ✅ |
| `Release ili kupakia` ❌ | `Achia ili kupakia` ✅ |

### File Picker

| Wrong | Correct | Notes |
|---|---|---|
| `Browse faili` ❌ | `Chagua faili` ✅ | "browse" → "chagua" (choose) for file pickers, NOT "vinjari" (which is for web browsing) |
| `Bofya hapa kuchagua faili` (verbose) | `Chagua faili` ✅ | Concise label |
| `Browse kwa faili` ❌ | `Tafuta faili` or `Chagua faili` ✅ | "browse for files" — use search or select |

### Empty States

Pattern: `Hakuna + noun/relative clause` (there is no / none).

| Wrong | Correct |
|---|---|
| `Hakuna kitu kilichochaguliwa` (verbose) | `Hakuna kilichochaguliwa` ✅ |
| `Bado hakuna matokeo` (not yet no results) | `Hakuna matokeo` ✅ |
| `Hakuna data ya kuonyesha` | `Hakuna data` ✅ (concise) |

### Error Messages — Concrete Predicate

| Wrong | Correct |
|---|---|
| `Hitilafu: X` (English-style label) | `Imeshindikana kuhifadhi faili. Jaribu tena.` (direct predicate + actionable advice) |
| `Hitilafu imetokea wakati wa kuhifadhi` (verbose) | `Imeshindikana kuhifadhi.` |
| `Je, una uhakika unataka kufuta?` (English calque) | `Ungependa kufuta?` ✅ (idiomatic Swahili) |

### Confirmation Dialogs

| English source | Idiomatic Swahili |
|---|---|
| Are you sure you want to delete? | `Ungependa kufuta?` (Would you like to delete?) |
| Confirm | `Thibitisha` |
| Cancel | `Ghairi` |
| OK | `Sawa` |

## Punctuation, Numbers, Dates, Currency

### Quotation Marks
- **Standard double quotes `"..."`**.
- Inner quotes: `'...'`.
- ❌ Hungarian-style `„..."` or French `« »` — not used in Swahili.

### Numbers
- **Decimal:** period (`3.14`)
- **Thousands:** comma (`1,234,567`)
- ❌ `3,14` or `1.000` — European-style, wrong for Swahili.

### Dates
- **DD/MM/YYYY** in numeric form (`15/01/2024`)
- Long: `15 Januari 2024` or `Tarehe 15 mwezi wa Januari mwaka 2024` (very formal)
- Months capitalized: `Januari, Februari, Machi, Aprili, Mei, Juni, Julai, Agosti, Septemba, Oktoba, Novemba, Desemba`

### Time
- **24-hour `14:30`** (modern UI default)
- 12-hour with period markers: `2:30 mchana` (afternoon), `8:00 asubuhi` (morning), `9:00 usiku` (night)
- ❌ Traditional Swahili saa-time (`saa nane mchana` = 2 PM) — only for cultural/lifestyle apps; not for tech UI.

### Currency
- See "Currency — Country-Specific" above.
- Default for pan-EAC: omit symbol or use ISO code.

### Comma Rules
- NO comma before `na, au, wala`.
- COMMA before `lakini, kwa sababu, ingawa, ili, kwamba, kama, wakati`.

## Terminology

| English | Preferred Swahili | Avoid | Notes |
|---|---|---|---|
| Save | hifadhi | save-isha, save-i | Native Bantu verb |
| Delete | futa | delete-isha | Native Bantu verb |
| Cancel | ghairi / sitisha | cancel-isha | Both common; `ghairi` is Arabic-loan |
| Submit | wasilisha | submit-i | |
| Send | tuma | | |
| Upload | pakia | upload-i | |
| Download | pakua / teremsha | download-i | `teremsha` (cause to descend) is more Tanzanian |
| Settings | mipangilio | settings | |
| Search | tafuta | search-i | |
| Edit | hariri | edit-i | |
| Copy | nakili | copy-i | |
| Paste | bandika | paste-i | |
| Cut | kata | cut-i | |
| Close | funga | close-i | |
| Open | fungua | open-i | |
| Sign in / Log in | ingia | login-i | |
| Sign out / Log out | toka | logout-i | |
| Register / Sign up | jisajili | sign-up-i | reflexive -ji- + sajili |
| File | faili | | English loan, class 9/10 |
| Folder | folda / kabrasha | | folda is common loan; kabrasha is Arabic-origin formal |
| Send | tuma | | |
| Select | chagua | select-i | |
| Print | chapisha | print-i | |
| Password | nenosiri / nywila | password | Both common; `nenosiri` is literal "secret word" |
| Email | barua pepe | email (acceptable code-switch) | Literally "lightning letter" |
| Link | kiungo | link (acceptable in dev contexts) | Class 7/8 |
| Update | sasisha | update-i | |
| Refresh | onyesha upya | refresh-i | "show anew" |
| Account | akaunti | | English loan, class 9/10 |
| Message | ujumbe / jumbe (pl) | message-i | Class 11 sg, class 10 pl |
| Browser | kivinjari | browser | Class 7/8 |
| Window | dirisha / madirisha (pl) | window | Class 5/6 |
| Computer | kompyuta | | English loan, class 9/10 |
| Internet | intaneti / mtandao | internet | `mtandao` is preferred Bantu term ("the web/network") |
| Network | mtandao / mitandao (pl) | network-i | Class 3/4 |
| Server | seva | server-i | Class 9/10 |
| Username | jina la mtumiaji | username | "name of the user" |
| Profile | wasifu | profile | |
| Notification | arifa / taarifa | notification-i | |
| Subscription | usajili | subscription-i | |
| Payment | malipo | payment-i | Class 6 (plural mass noun) |
| Free (no cost) | bure | free | |
| Free (liberty) | huru | | Different word from "no cost" |
| Premium | premium / hali ya juu | | |
| Help | msaada | help-i | |
| Support | usaidizi | support-i | |
| Privacy | faragha | privacy | |
| Security | usalama | security-i | |
| Terms of service | masharti ya huduma | terms-i | |
| Welcome | karibu / karibuni (pl) | welcome | Standard greeting |
| Hello | habari / hujambo | hello | |
| Yes | ndiyo | yes | |
| No | hapana / la | no | |
| OK | sawa | OK (acceptable) | |
| Please | tafadhali | please | Use sparingly |
| Thank you | asante / asanteni (pl) | thanks | |
| Sorry | samahani / pole | sorry | |

### Compound Adjective Constructions

English compound adjectives with hyphens (AI-powered, user-friendly, context-aware) do NOT translate as hyphenated forms in Swahili. Restructure with **relative clauses** or **possessive constructions**.

| English | Wrong (hyphenated calque) | Correct (restructured) |
|---|---|---|
| AI-powered | AI-iendesha | **inayotumia AI** (which uses AI) / **yenye AI** (with AI) |
| user-friendly | mtumiaji-rafiki | **rahisi kutumia** (easy to use) / **rafiki kwa mtumiaji** (friendly to the user) |
| context-aware | muktadha-fahamu | **inayozingatia muktadha** (which considers context) |
| cloud-based | mawingu-msingi | **inayotumia teknolojia ya wingu** (which uses cloud technology) / **ya wingu** |
| data-driven | data-endesha | **inayoendeshwa na data** (which is driven by data) |
| open-source | chanzo-wazi | **chanzo huru** (free source) / **chanzo wazi** (open source — two words) |

### Brand Names and Technical Identifiers

- **Brand names** remain in their original form: Apple, Google, Microsoft, Anthropic, Claude, Slack, GitHub.
- **Technical identifiers** (API, URL, JSON, XML, HTTP, REST) stay as-is.
- **No need to add Swahili morphology** to brand names or technical IDs.
- For ambiguity, can clarify: `tovuti ya Google` (Google's website), `programu ya Microsoft Word` (the Microsoft Word program).

### Country Names — Swahili Conventions

| English | Preferred Swahili | Avoid |
|---|---|---|
| USA / America | Marekani | Muungano wa Madola ya Amerika (too formal/long) |
| United Kingdom | Uingereza | Ufalme wa Muungano (technical) |
| Germany | Ujerumani | |
| France | Ufaransa | |
| China | Uchina / China | |
| Japan | Japani | |
| India | Uhindi / India | |
| South Africa | Afrika Kusini | |
| Egypt | Misri | |
| Saudi Arabia | Saudia / Saudi Arabia | |
| Tanzania | Tanzania | |
| Kenya | Kenya | |
| Uganda | Uganda | |

Note the **U-** prefix on many country names (Uingereza, Ujerumani, Ufaransa, Uchina, Uhindi) — this is class 14 (abstract noun class), used historically for "land of X." Modern usage retains it for European/Asian countries; newer countries (Tanzania, Kenya) keep their international form.

## Calque / Anti-Pattern Blocklist

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| Vunja mguu | **Kila la heri! / Bahati njema!** | "break a leg" (good luck) |
| Kipande cha keki | **Ni rahisi sana / Ni jambo dogo** | "piece of cake" |
| Mwishoni mwa siku | **Hatimaye / Kwa ujumla** | "at the end of the day" |
| Inafanya hisia | **Inaeleweka / Ina mantiki** | "makes sense" |
| Chukua mapumziko | **Pumzika** | "take a break" — use single verb |
| Toa jicho | **Angalia / Chunguza** | "keep an eye on" |
| Fanya uamuzi | **Amua** | "make a decision" — single verb |
| Fanya mabadiliko | **Badilisha** | "make changes" — single verb |
| Fanya uchaguzi | **Chagua** | "make a selection" — single verb |
| 25+ lugha | **zaidi ya lugha 25 / lugha 25 au zaidi** | "+N" unnatural in Swahili |
| +{count} zaidi | **na {count} zaidi / {count} nyingine** | "+N" unnatural |
| herufi {min} za urefu | **herufi {min} au zaidi** | "za urefu" (of length) redundant |
| Zero usumbufu / Sifuri muda wa kufa | **Bila usumbufu / Bila kukatika** | "zero X" — use "bila" (without) |
| Faili imehifadhiwa kwa mafanikio | **Faili imehifadhiwa** | "successfully" — often unnecessary |
| Je, una uhakika unataka kufuta? | **Ungependa kufuta?** | Verbose English confirmation calque |
| Muungano wa Madola ya Amerika | **Marekani** | Use short form in UI |
| Save-isha | **Hifadhi** | English-Swahili hybrid verb |
| Delete-isha | **Futa** | English-Swahili hybrid verb |
| Click-ia | **Bofya** | English-Swahili hybrid verb |
| mtumiaji-rafiki (hyphenated) | **rahisi kutumia / rafiki kwa mtumiaji** | "user-friendly" — restructure |
| AI-iendesha (hyphenated) | **inayotumia AI / yenye AI** | "AI-powered" — relative clause |

## "Per" vs "For" Distinction (severity 2.0)

Swahili distinguishes carefully between **kwa** (for, aggregate/total) and **kwa kila** (per, rate/unit). Mixing them changes the meaning.

| English meaning | Swahili | Example |
|---|---|---|
| For X items (total/aggregate) | **kwa + N** | "kwa lugha 5" = for 5 languages [in total] |
| Per X (rate per unit) | **kwa kila + N** | "kwa kila lugha" = per language |

| Wrong | Correct | Why |
|---|---|---|
| `kwa kila lugha 5` (meaning "for 5 total") | `kwa lugha 5` | `kwa` for total |
| `kwa lugha` (meaning "per language") | `kwa kila lugha` | `kwa kila` for rate |
| `$10 kwa mtumiaji` (ambiguous) | `$10 kwa kila mtumiaji` (per user) OR `$10 kwa watumiaji 10` (for 10 users) | Disambiguate |

## Loanword Integration Rules

Swahili has two large loanword layers and a smaller modern English-tech layer:

**Arabic loans** (deeply integrated, ~20% of vocabulary, often unrecognizable as foreign to modern speakers):
- kitabu (book), salama (peace/safe), shule (school), saa (clock/hour), dunia (world), habari (news), karibu (welcome), tafadhali (please), asante (thanks), samahani (sorry), kahawa (coffee), sukari (sugar), Alhamisi/Ijumaa (Thursday/Friday).

**English loans** (modern tech, integrated phonologically):
- kompyuta, programu, tovuti (← website, but mostly Tanzanian; Kenyans often say `website`), seva, intaneti, faili, folda, redio, televisheni, simu (phone, though originally Arabic via Indian languages), benki, namba (number).

**Portuguese loans** (older, smaller, coastal):
- meza (table — Portuguese mesa), bandera (flag — Portuguese bandeira), leso (handkerchief).

**Rules for integrating new English tech terms:**
1. **Prefer established Swahili term if it exists:** Don't say `save-i` when `hifadhi` works.
2. **Use the English loan if it's already widely accepted:** `faili`, `kompyuta`, `programu`, `intaneti`.
3. **Avoid creating new -isha/-ia hybrid verbs:** ❌ `save-isha`, ❌ `delete-isha`, ❌ `click-ia`, ❌ `update-i`. Use native verbs.
4. **For untranslatable technical IDs (API, URL, JSON, token, SDK, IDE), use English as-is.** No Swahili morphology needed.

| Wrong (hybrid) | Correct |
|---|---|
| save-isha | hifadhi |
| delete-isha | futa |
| click-ia | bofya |
| update-i | sasisha |
| Imesaveiwa | Imehifadhiwa |

## Self-Check Checklist

Run BEFORE finalizing each translation:

**Accuracy — concord and grammar (critical):**
- [ ] **Noun class identified** for every noun in the string
- [ ] **Adjective concord:** prefix matches noun class (kitufe **ki**pya, mifumo **mi**pya, watumiaji **wa**zuri)
- [ ] **Verb subject prefix:** matches noun class (faili **i**nahifadhiwa, mfumo **u**nafanya, vitufe **vi**nafanya)
- [ ] **Possessive prefix:** matches class of possessed noun (kitabu **ch**angu, faili **y**angu, vitabu **vy**angu, mifumo **y**angu)
- [ ] **Demonstrative concord:** correct class form (mtu **huyu**, kitabu **hiki**, faili **hii**, mifumo **hii**)
- [ ] **Tense markers correct:** `-na-` for ongoing, `-li-` for past, `-me-` for completed, `-ta-` for future
- [ ] **Negation correct form:** `ha-...-i` present, `ha-...-ku-` past, `ha-...-ja-` perfect-not-yet
- [ ] **Passive form:** `-w-` inserted before final vowel (hifadhi**w**a, fut**w**a, tum**w**a)
- [ ] **Plural via class prefix:** NOT English -s (mifumo not mfumos, vitufe not kitufes, faili stays faili)
- [ ] **Number concord 1-5:** numbers 1-5 take class prefix (mtu **m**moja, vitu **vi**tatu, watumiaji **wa**tano); 6+ invariant
- [ ] **Adjectives AFTER noun:** faili kubwa (not kubwa faili)
- [ ] **SVO word order** for neutral statements
- [ ] **Pro-drop:** no unnecessary `mimi/wewe/sisi` pronouns
- [ ] **Placeholders preserved exactly** ({count}, {name}, {date} unchanged)

**Accuracy — formatting:**
- [ ] **No comma** before `na` / `au` / `wala`
- [ ] **Comma** before `lakini` / `kwa sababu` / `kwamba` / `kama` / `wakati`
- [ ] **Decimal point** (3.14) not comma (3,14)
- [ ] **Thousands comma** (1,234) not period (1.234)
- [ ] **DD/MM/YYYY** date format
- [ ] **24-hour time** (14:30) for tech UI, not traditional Swahili saa-time
- [ ] **Currency symbol** correct for target country (TSh, KSh, USh, Fr) OR generic for pan-EAC
- [ ] **Quotation marks** `"..."` (double quotes)
- [ ] **`ng'` vs `ng`** distinction preserved in writing

**Accuracy — semantics:**
- [ ] **`kwa` vs `kwa kila`:** "for total" vs "per unit" — never confused
- [ ] **Domain terminology** preserves precise IT meaning (architecture = system design, NOT building; pipeline = CI/CD, NOT plumbing)

**Naturalness — UI patterns:**
- [ ] **Buttons in imperative stem** (Hifadhi, Futa, Tuma) — NOT infinitive `Kuhifadhi`, NOT subjunctive `Uhifadhi`
- [ ] **Status messages impersonal** (Inapakia..., Imehifadhiwa) — NOT first/second person
- [ ] **File picker:** `Chagua faili` NOT `Browse faili`
- [ ] **Drag-and-drop:** `buruta/dondosha/achia` NOT `drag/drop/release`
- [ ] **Empty states:** `Hakuna...` construction
- [ ] **Confirmations:** `Ungependa kufuta?` NOT verbose calque
- [ ] **Marketing absence:** `Bila X` NOT `Sifuri X / Zero X`

**Naturalness — word choice:**
- [ ] **Native Swahili verbs:** hifadhi/futa/tafuta/pakia, NOT save-isha/delete-isha/click-ia
- [ ] **`fanya + noun` avoided** when single verb exists (badilisha not fanya mabadiliko)
- [ ] **Compound adjectives restructured** with relative clauses (inayotumia AI not AI-iendesha)
- [ ] **No calques:** hatimaye (not mwishoni mwa siku), inaeleweka (not inafanya hisia)
- [ ] **`tafadhali` used sparingly** (not on every button)
- [ ] **Country names short** (Marekani not Muungano wa Madola ya Amerika)
- [ ] **No Sheng** (no `poa, noma, sasa hivi, doh, jamaa` as slang)
- [ ] **Religiously neutral** (no `Asalaam aleikum` or `Bwana asifiwe` in default UI)

**Naturalness — flow:**
- [ ] **Reads naturally** when spoken aloud
- [ ] **Cross-EAC understandable** (a user in Dar es Salaam OR Nairobi would get it immediately)
- [ ] **Concord makes sense** — every adjective and verb pulls from the same noun's class
- [ ] **Matches East African software conventions** (Microsoft, Google, Mozilla Swahili UIs use similar patterns)

## Worked Examples

### Example 1 — Save button + status sequence

**Source:**
> Save
> Saving your changes...
> Changes saved.

**Wrong:**
> Kuhifadhi (infinitive, wrong for button)
> Mimi ninahifadhi mabadiliko yako... (1st person, too personal)
> Mabadiliko yamehifadhiwa kwa mafanikio. (redundant "successfully")

**Correct:**
> **Hifadhi** (imperative stem)
> **Inahifadhi...** OR **Inahifadhi mabadiliko...** (impersonal, class-9 i- prefix)
> **Mabadiliko yamehifadhiwa.** (class-6 ya- prefix for matokeo-style plural; complete sentence)

### Example 2 — File count with concord

**Source:**
> 1 file uploaded
> 5 files uploaded
> 25 files uploaded

**Wrong:**
> Faili 1 imepakia
> Failis 5 zimepakia (English -s plural is wrong)
> 25 failis zimepakiwa

**Correct (class 9/10 — faili is invariant):**
> **Faili moja limepakiwa** (1 file uploaded — class 5 li- because of mass/aggregate framing) OR **Faili 1 imepakiwa** (class 9 i-)
> **Faili tano zimepakiwa** (5 files — class 10 zi- because plural)
> **Faili 25 zimepakiwa**

(Note: faili in singular often takes class 5/9 ambiguity; modern Swahili usage trends toward class 9 i- for singular, class 10 zi- for plural with numeric quantifier. The form `zimepakiwa` indicates plural unambiguously.)

### Example 3 — Counter with concord across multiple classes

**Source:**
> 1 user, 3 buttons, 5 files

**Wrong:**
> 1 mtumiajis, 3 kitufes, 5 failis (English -s plural)
> Mtumiaji 1, kitufes 3, failis 5

**Correct:**
> **Mtumiaji mmoja, vitufe vitatu, faili tano** (singular noun class 1 + plural class 8 + class 10)

### Example 4 — Possessive across classes

**Source:**
> My account, my files, my settings, my password

**Wrong:**
> Akaunti changu (wrong possessive prefix — `changu` is class 7/8, akaunti is class 9)
> Faili changu (same error)

**Correct:**
> **Akaunti yangu** (class 9 — y- prefix)
> **Faili zangu** (class 10 plural — z- prefix; or `Faili yangu` for singular)
> **Mipangilio yangu** (class 4 — y- prefix)
> **Nenosiri langu** (class 5 — l- prefix)

### Example 5 — Drag-and-drop area

**Source:**
> Drag and drop files here, or click to browse

**Wrong:**
> Drag na drop faili hapa, au bofya kuvinjari (anglicism + wrong "browse")
> Buruta na dondosha faili hapa, au bofya (comma before au — wrong)

**Correct:**
> **Buruta na dondosha faili hapa au bofya kuchagua faili** (native verbs, no comma before `au`, `chagua` for file selection not `vinjari`)

### Example 6 — Concord chain in a confirmation

**Source:**
> This new file has been saved successfully.

**Wrong:**
> Hii faili mpya imehifadhiwa kwa mafanikio. (demonstrative before noun — wrong order; verbose "kwa mafanikio")
> Faili huyu mpya imehifadhiwa. (wrong demonstrative class — huyu is class 1)

**Correct:**
> **Faili hii mpya imehifadhiwa.** (demonstrative `hii` after noun, class 9 concord; drop "kwa mafanikio")

For class 7 (kitufe):
> **Kitufe hiki kipya kimebofyeka.** (button-this-new has been clicked — every word ki-)

For class 4 (mifumo):
> **Mifumo hii mipya imeshawekwa.** (systems-these-new have been set — concord across the chain)

### Example 7 — Verb-prefix on negation

**Source:**
> File not saved.

**Wrong:**
> Faili si imehifadhiwa. (using `si` standalone — ungrammatical)
> Faili hai imehifadhiwa. (broken concatenation)

**Correct:**
> **Faili haijahifadhiwa.** (class 9 + ha-...-ja- = "not yet saved")
> **Imeshindikana kuhifadhi faili.** (alternative: "failed to save the file")

### Example 8 — Plural across noun classes

**Source:**
> Settings have been updated.

**Wrong:**
> Mipangilio imebadilishwa (class 9 i- prefix — wrong; mipangilio is class 4)
> Settings imeupdate-iwa (English hybrid — wrong)

**Correct:**
> **Mipangilio imesasishwa.** (class 4 i- subject prefix for plural mipangilio, + `me-` perfect, + `sasishwa` passive of sasisha)

### Example 9 — Number + noun (concord 1-5, invariant 6+)

**Source:**
> 2 users, 5 buttons, 7 files, 100 messages

**Correct:**
> **Watumiaji wawili** (class 2, 2 takes wa-)
> **Vitufe vitano** (class 8, 5 takes vi-)
> **Faili saba** (class 10, 7 invariant)
> **Jumbe 100** (class 10, 100 invariant — or **jumbe mia moja**)

### Example 10 — Compound adjective restructured

**Source:**
> AI-powered translation, user-friendly interface, cloud-based storage

**Wrong:**
> Tafsiri AI-iendeshwa, kiolesura mtumiaji-rafiki, hifadhi mawingu-msingi (hyphenated calques — all wrong)

**Correct:**
> **Tafsiri inayotumia AI** (translation which uses AI)
> **Kiolesura kilicho rahisi kutumia** (interface that is easy to use) OR **Kiolesura rafiki kwa mtumiaji** (interface friendly to the user)
> **Hifadhi inayotumia teknolojia ya wingu** (storage which uses cloud technology) OR shorter: **Hifadhi ya wingu**

### Example 11 — Date and currency

**Source:**
> January 15, 2024 — Total: TSh 1,234.50

**Wrong:**
> 01/15/2024 — Jumla: 1.234,50 TSh (US date + European number format)
> Januari 15, 2024 — Jumla: TSh 1,234.50 (date format wrong-ish — needs day first)

**Correct:**
> **15 Januari 2024** OR **15/01/2024** — **Jumla: TSh 1,234.50** OR **1,234.50/=**

(Day first, period decimal, comma thousands, currency symbol before amount, or the traditional Tanzanian `/=` after the amount.)

### Example 12 — Religious/regional neutrality

**Source:**
> Hello! Welcome to our service.

**Wrong (overly religious):**
> Asalaam aleikum! Karibu kwenye huduma yetu. (Muslim-specific greeting)
> Bwana asifiwe! Karibu... (Christian-specific greeting)

**Correct (neutral):**
> **Habari! Karibu kwenye huduma yetu.** (neutral, friendly, cross-religious)
> **Karibu! Tunafurahi kukuona.** (Welcome! We're glad to see you.)

### Example 13 — Empty state

**Source:**
> No results found. Try a different search.

**Wrong:**
> Hakuna matokeo yameonekana. Jaribu utafutaji tofauti. (verbose, wrong concord — `matokeo yameonekana`)
> Bado hakuna matokeo. Jaribu utafutaji tofauti. (literal "not yet no results" — redundant)

**Correct:**
> **Hakuna matokeo. Jaribu utafutaji mwingine.** (concise + native idiom)
> OR **Hakuna kilichopatikana. Jaribu tena.** (nothing was found, try again)

### Example 14 — Confirmation dialog

**Source:**
> Are you sure you want to delete this file? This action cannot be undone.

**Wrong:**
> Je, una uhakika unataka kufuta faili hii? Kitendo hiki hakiwezi kubatilishwa. (verbose English calque)

**Correct:**
> **Ungependa kufuta faili hii? Kitendo hiki hakitaweza kubatilishwa.** (idiomatic Swahili question + future negative)

OR more concise:
> **Una uhakika? Kufuta hakuwezi kubatilishwa.** (Are you sure? Deletion cannot be undone.)

## When in Doubt

1. **Noun class unclear?** Look at the noun's prefix:
   - `m-` + person → class 1 (sg, takes a- on verb, wa- in plural to class 2)
   - `mi-` (or `m-` + non-person) → class 3 (sg, takes u- on verb, mi- in plural to class 4)
   - `ki-` → class 7 (sg, takes ki- on verb, vi- in plural to class 8)
   - `ma-` → class 6 plural (takes ya- on verb; sg is class 5 with Ø or ji-)
   - Loanword with no prefix (faili, kompyuta, akaunti) → almost always class 9/10 (takes i-/zi-)
   - `u-` + abstract → class 11/14 (often no plural)
   - `ku-` + verb stem → class 15 (gerund/infinitive)

2. **Adjective concord unclear?**
   - Bantu-stem adjective (-pya, -zuri, -baya, -dogo, -kubwa) → adds the class prefix
   - Loan adjective (bora, safi, rahisi, muhimu) → invariant, no concord

3. **Verb subject prefix unclear?** Match the subject noun's class:
   - Person sg → a- (3sg) or ni-/u-/tu-/m- (1/2/1pl/2pl)
   - Person pl → wa-
   - mfumo (class 3) → u-
   - mifumo (class 4) → i-
   - kitufe (class 7) → ki-
   - vitufe (class 8) → vi-
   - faili sg (class 9) → i-
   - faili pl (class 10) → zi-
   - tokeo (class 5) → li-
   - matokeo (class 6) → ya-

4. **Possessive prefix unclear?** Use the prefix of the **possessed** noun's class (not the possessor):
   - kitabu (class 7) → -changu, -chako, -chake, -chetu, -chenu, -chao
   - vitabu (class 8) → -vyangu, -vyako, -vyake, -vyetu, -vyenu, -vyao
   - faili (class 9) → -yangu, -yako, -yake, -yetu, -yenu, -yao
   - faili pl (class 10) → -zangu, -zako, -zake, -zetu, -zenu, -zao
   - mfumo (class 3) → -wangu, -wako, -wake, -wetu, -wenu, -wao

5. **Plural form unclear?** Apply the class-pair plural prefix:
   - 1→2: mtu→watu, mtoto→watoto
   - 3→4: mfumo→mifumo, mti→miti
   - 5→6: jicho→macho, jiwe→mawe, tokeo→matokeo
   - 7→8: kitabu→vitabu, kiti→viti
   - 9→10: faili→faili (no change), kompyuta→kompyuta
   - 11→10: ujumbe→jumbe (n-class)

6. **Number + noun?** Use class concord for 1-5; invariant for 6+:
   - vitu vitatu (3 things, class 8)
   - vitu sita (6 things — no concord)
   - watu wawili (2 people, class 2)
   - watu kumi (10 people — no concord)

7. **Tense unclear?**
   - Ongoing/progressive → `-na-` (Inapakia... = It is loading...)
   - Completed → `-me-` (Imehifadhiwa = It has been saved)
   - Past simple → `-li-` (Alipakia = He/she loaded)
   - Future → `-ta-` (Itahifadhiwa = It will be saved)
   - Not-yet → `ha-...-ja-` (Haijahifadhiwa = It has not yet been saved)

8. **Button label?** Use the bare imperative (verb stem): Hifadhi, Futa, Tuma, Bofya, Chagua. NOT infinitive (Kuhifadhi) or subjunctive (Uhifadhi) or full sentence (Bofya hapa kuhifadhi).

9. **Status message?** Use impersonal class-9 + tense: Inapakia... / Imehifadhiwa / Imeshindikana. NOT first-person (Ninapakia...) or second-person (Unapakia...).

10. **Compound adjective with hyphen in English?** Restructure with a relative clause: AI-powered → inayotumia AI, user-friendly → rahisi kutumia, cloud-based → ya wingu / inayotumia teknolojia ya wingu.

11. **`fanya + noun`?** Almost always wrong. Find the single verb: fanya mabadiliko → badilisha, fanya uamuzi → amua, fanya uchaguzi → chagua.

12. **English-Swahili hybrid verb (-isha, -ia)?** Always wrong. Use the native Swahili verb: save-isha → hifadhi, delete-isha → futa, click-ia → bofya.

13. **Country name in UI?** Use the short Swahili form: USA → Marekani, UK → Uingereza, China → Uchina, Germany → Ujerumani. Not the full official name.

14. **Religious greeting in default UI?** Avoid. Use neutral: Habari / Karibu. Reserve religious salutations for explicitly religious apps.

15. **Sheng or colloquial term?** Avoid in UI. Use Kiswahili sanifu (standard): poa → nzuri/sawa, noma → nzuri sana, mzee → mtu / mtumiaji, jamaa → rafiki, doh → pesa, sasa hivi (Sheng intensifier) → sasa.

Swahili's noun-class concord is the single most error-prone area. When a translation feels "off," check first whether every adjective, verb prefix, and possessive in the sentence matches the class of its head noun. The second most common error is using English-style verb hybrids (save-isha, click-ia) instead of native Bantu verbs (hifadhi, bofya). Fix those two, and most other issues fall into place.
