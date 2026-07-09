---
name: localize-ur
description: Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Urdu (اردو) for Pakistan (ur-PK, national language) or Indian Muslim communities (ur-IN, one of India's 22 scheduled languages). Urdu is an Indo-Aryan language written in Perso-Arabic Nastaliq script (RTL) — NOT Arabic, NOT Persian, and CRITICALLY NOT Hindi despite ~75% spoken overlap. Urdu and Hindi share grammar but diverge SHARPLY in literary register: Urdu uses Perso-Arabic-derived formal vocabulary (شکریہ, مسئلہ, حکومت, تعلیم) and RTL Nastaliq script; Hindi uses Sanskrit-derived (तत्सम) formal vocabulary (धन्यवाद, समस्या, सरकार, शिक्षा) and Devanagari LTR script. Critical features: Nastaliq calligraphic style (NOT Arabic Naskh — native Urdu publishing uses Jameel Noori Nastaleeq / Noto Nastaliq Urdu fonts), the 4 Persian extras (پ چ ژ گ) PLUS Urdu-specific letters retroflex ٹ ڈ ڑ, nasalization ں (nūn ghunnā), do-chashmi ھ for aspirated consonants (کھ گھ چھ تھ ٹھ دھ ڈھ پھ بھ — these distinguish minimal pairs like کل/کھل), baṛī ye ے (final long ye), 2 grammatical genders (m/f) visible on nouns/adjectives/verbs, SOV word order, 3-tier honorific verb conjugation (تو tū intimate / تم tum peer / آپ āp formal — DEFAULT for UI), postpositions (نے ergative, کو dative, سے ablative, میں locative, پر on, کا/کی/کے genitive agreeing with possessed noun), ergative case marking نے with perfective transitive (میں نے فائل دیکھی — verb agrees with object), Urdu/Persian numerals ۰۱۲۳۴۵۶۷۸۹ in formal Urdu (Persian code points, NOT Arabic-Indic ٠١٢٣٤٥٦٧٨٩), Indian-style lakh/crore number grouping (۱,۲۳,۴۵۶), Urdu full stop ۔ (U+06D4, NOT Latin period), Arabic-style ؟ ، ؛ punctuation, DD/MM/YYYY dates, Gregorian months adapted (جنوری فروری مارچ…), Pakistani week starts Monday (پیر) with جمعہ as Islamic holy day, currency PKR ₨/Rs. for Pakistan vs INR ₹ for India, compound verb with کرنا for tech vocab (کلک کرنا, سیو کرنا), ہو رہا ہے continuous aspect for loading + ہو گیا/گئی for completion (gender agrees), براہ کرم for "please" (NOT کرپیا which is Hindi), and respect for Islamic values in Sunni-majority Pakistan (avoid pork/alcohol imagery, Friday is جمعہ holy day).
---

# Localize: Urdu (ur → اردو)

## Scope & Variants

Urdu is one of the great literary languages of the Indian subcontinent — the national language of Pakistan, one of 22 scheduled languages of the Republic of India, and a language of culture and prestige across the South Asian Muslim diaspora. It descends from the same Indo-Aryan vernacular base as Hindi (called "Hindustani" or "Khari Boli" before the 19th century), but acquired its literary identity at the Mughal court and in the qasbahs (small towns) of north India through extensive Persian and Arabic enrichment. Modern Urdu emerged with the great 18th-19th century poets of Delhi and Lucknow (Mir Taqi Mir, Mirza Ghalib, Mir Anis) and the prose stylists of Aligarh and Hyderabad.

| Locale | Name | Native name | Where | Default register |
|--------|------|-------------|-------|------------------|
| `ur` / `ur-PK` | Pakistani Urdu (standard) | اردو / پاکستانی اردو | Pakistan (~70M L1 + ~100M L2) | Formal آپ |
| `ur-IN` | Indian Urdu | اردو / ہندوستانی اردو | India (~50M, primarily UP, Bihar, Telangana, Maharashtra, Delhi, Kashmir) | Formal آپ |

**Default for general UI / international audiences: `ur-PK`** (Pakistan standard, Karachi/Lahore/Islamabad register). The written standard is essentially the **same in both countries** — Urdu in Pakistan and Urdu in India share orthography, grammar, and formal vocabulary almost identically. Differences are mostly:

- **Currency** (PKR in Pakistan vs INR in India)
- **Some everyday lexical items** that diverge from English (Pakistan has more English loans in tech; Indian Urdu sometimes uses Sanskrit-Hindi crossovers in everyday speech)
- **Religious/cultural framing** (Pakistan is overwhelmingly Muslim — UI can lean Islamic by default; India-Urdu serves a religious minority and may need more secular framing)

### ur-PK vs ur-IN — what actually differs in writing

The two are the **same written language** for ~98% of UI copy. Differences appear in:

| Concept | ur-PK (Pakistan) | ur-IN (India) |
|---------|------------------|---------------|
| Currency | ₨ / روپے (Pakistani Rupee, PKR) | ₹ / روپے (Indian Rupee, INR) |
| Phone country code | +92 | +91 |
| Capital | اسلام آباد | نئی دہلی |
| Cricket/news context | پاک-بھارت | ہند-پاک |
| "India" reference | بھارت (more formal/political), ہندوستان (cultural/historical) | بھارت (official), ہندوستان (everyday/cultural) |
| "Pakistan" reference | پاکستان | پاکستان |
| Tech loans tolerance | High (English freely mixed in urban UI) | Mixed; sometimes Hindi-tech crossovers seep in |
| Religious framing | Default Muslim/Islamic ambient | Sensitive: many Indian Urdu speakers are Muslim, but secular/cross-community framing safer |
| Weekend | جمعہ + اتوار (Pakistan officially Fri+Sun) | اتوار only (India: Sunday) |

**Default to ur-PK.** If the user requests ur-IN, switch currency to ₹ INR and tone down Pakistan-specific religious/political framing.

### When the target locale is unspecified

If the user requests "Urdu" without specifying region, ask once:

> Which Urdu variant should I target?
>
> - **`ur-PK` Pakistan Urdu** — Recommended. Default for international/general use. Currency: ₨ PKR. Week ends Fri+Sun.
> - **`ur-IN` Indian Urdu** — Currency: ₹ INR. Week ends Sun only. Often more secular/cross-community framing.

Default to `ur-PK` if no answer.

---

## Identity Guardrail — Urdu is NOT Hindi

This is the single most important section of this skill. Urdu and Hindi are mutually intelligible in everyday conversation — when two friends chat about food, weather, or cricket, an outsider cannot tell which language they are speaking. Linguists sometimes call the shared spoken base "Hindustani." But **as written languages, Urdu and Hindi are TWO DIFFERENT LANGUAGES**, with different scripts, different literary registers, and increasingly divergent formal vocabularies.

| Feature | Urdu (اردو) | Hindi (हिन्दी) |
|---------|-------------|---------------|
| **Script** | **Perso-Arabic Nastaliq (RTL)** — flowing diagonal calligraphic style | **Devanagari (LTR)** — angular block letters with top-bar (शिरोरेखा) |
| **Direction** | Right-to-left | Left-to-right |
| **Literary register vocabulary** | **Persian + Arabic** loanwords | **Sanskrit** loanwords (तत्सम tatsama "as-is") |
| **Everyday spoken overlap** | ~75% identical with Hindi | ~75% identical with Urdu |
| **Formal/written divergence** | High — formal Urdu uses Perso-Arabic terms | High — formal Hindi uses Sanskritic terms |
| **Grammar (syntax, morphology)** | **Identical to Hindi** (same SOV, same gender, same case, same ergative نے / ने) | **Identical to Urdu** |
| **Numerals** | Urdu/Persian ۰۱۲۳۴۵۶۷۸۹ (formal) or Western 0-9 | Devanagari ०१२३४५६७८९ or Western 0-9 |
| **Punctuation** | Arabic-style ؟ ، ؛ + Urdu full stop ۔ | Latin punctuation + Devanagari danda ।, double-danda ॥ |
| **Calendar** | Gregorian + Islamic Hijri for religious dates | Gregorian + Hindu Vikram Samvat / Shaka for religious dates |
| **Religious framing** | Muslim-default (Pakistan); Muslim-minority (India) | Hindu-default (India); secular for international |
| **Status** | National language of Pakistan; scheduled language of India | Official language of India (alongside English); not official in Pakistan |

**The Urdu-vs-Hindi formal vocabulary divergence — memorize this table:**

| English | Urdu (✓) | Hindi (✗ for Urdu UI) |
|---------|----------|------------------------|
| Please | **براہ کرم** (barāh-e-karam) | कृपया (kṛipayā) |
| Thank you | **شکریہ** (shukriyā) | धन्यवाद (dhanyavād) |
| Problem | **مسئلہ** (masʾalah) | समस्या (samasyā) |
| Government | **حکومت** (hukūmat) | सरकार (sarkār) |
| Education | **تعلیم** (taʿlīm) | शिक्षा (śikṣā) |
| Question | **سوال** (savāl) | प्रश्न (praśna) — Hindi formal; सवाल also exists everyday |
| Answer | **جواب** (javāb) | उत्तर (uttar) — Hindi formal; जवाब also exists |
| News | **خبر** (khabar) | समाचार (samāchār) — Hindi formal; ख़बर also exists |
| History | **تاریخ** (tārīkh) | इतिहास (itihās) |
| Country | **ملک** (mulk) | देश (deśa) |
| World | **دنیا** (dunyā) | संसार (saṃsār), विश्व (viśva) — Hindi formal; दुनिया everyday |
| God | **اللہ / خدا** (Allāh / Khudā) | ईश्वर (Īśvara), भगवान (Bhagavān), परमेश्वर (Parameśvara) |
| Marriage | **شادی / نکاح** (shādī / nikāh — Islamic contract) | विवाह (vivāha — Hindu rite); शादी also everyday |
| Hospital | **اسپتال / شفاخانہ** | अस्पताल (aspatāl); also चिकित्सालय (formal Sanskritic) |
| University | **جامعہ / یونیورسٹی** | विश्वविद्यालय (viśvavidyālaya) — Hindi formal; यूनिवर्सिटी also |
| Book | **کتاب** (kitāb) | पुस्तक (pustaka) formal; किताब everyday |
| Time | **وقت** (vaqt) | समय (samaya) formal; वक़्त everyday |
| Friend | دوست (dost — shared, both languages use this) | दोस्त (dost — everyday); मित्र (mitra) Hindi formal |
| Sunday | **اتوار** (itvār — Persian origin) | रविवार (ravivār — Sanskrit, day of Sun-god Ravi) |
| Monday | **پیر / سوموار** (pīr — Persian "elder/Monday" / somvār) | सोमवार (somvār) |

**The pattern:** the MORE FORMAL the context, the MORE the languages diverge. Casual SMS-style Hindi/Urdu can be nearly identical. Formal/written/religious/legal/scientific/government contexts diverge sharply because Urdu reaches into Perso-Arabic vocabulary while Hindi reaches into Sanskritic vocabulary.

**Concrete contrast — "Thank you for using our education service":**

| Language | Sentence | Script |
|----------|----------|--------|
| English | Thank you for using our education service. | Latin LTR |
| **Urdu** | ہماری تعلیمی خدمت استعمال کرنے کا شکریہ۔ | Perso-Arabic Nastaliq RTL |
| **Hindi** | हमारी शिक्षा सेवा का उपयोग करने के लिए धन्यवाद। | Devanagari LTR |

Same grammar (SOV, ergative system, gender), but **شکریہ vs धन्यवाद**, **تعلیمی vs शिक्षा**, **خدمت vs सेवा**, **استعمال vs उपयोग** — every formal word is a different lexical choice.

**Mistakes that auto-fail (Hindi creeping into Urdu UI):**

- Writing کرپیا instead of براہ کرم for "please" (`کرپیا` is a transliteration of Hindi कृपया and reads wrong in Urdu)
- Writing دھنیہ واد / دھنیواد instead of شکریہ for "thank you"
- Using سرکار instead of حکومت for "government" in formal text (سرکار in Urdu means "lord/master/sir", a respectful address — NOT "government")
- Using سمسیا instead of مسئلہ for "problem"
- Using شکشا instead of تعلیم for "education"
- Writing Urdu words with Devanagari script
- Importing Hindi/Sanskrit compound formations into Urdu (e.g., `بشواودیالیہ` for university — use جامعہ or یونیورسٹی)
- Calling Urdu "a dialect of Hindi" or "Hindi in Arabic script" (it is a literary language in its own right with a Mughal-court heritage)

**Urdu is NOT Arabic either.** Like Persian, Urdu uses the Perso-Arabic script and borrows Arabic vocabulary (especially religious terms), but Urdu is **Indo-Aryan**, not Semitic. Urdu has no Arabic feminine adjective agreement, no Arabic dual number, no Arabic VSO order, and no Arabic root-and-pattern morphology. Urdu grammar is identical to Hindi (Indo-Aryan).

**Urdu is NOT Persian either.** Urdu borrowed massively from Persian (and via Persian, from Arabic), but Urdu grammar is Indo-Aryan, not Iranian:

| Feature | Urdu (Indo-Aryan) | Persian (Iranian) |
|---------|-------------------|-------------------|
| Grammatical gender | **YES** — 2 genders (m/f), visible on nouns, adjectives, verbs | **NO** gender |
| Ergative case | **YES** — نے marks perfective transitive subject | **NO** ergative |
| Postpositions | **YES** — کو, سے, میں, پر follow noun | Persian uses prepositions (به، در، از، با) — opposite order |
| Retroflex consonants | **YES** — ٹ ڈ ڑ (Indo-Aryan feature) | **NO** retroflex |
| Aspirated consonants with do-chashmi he | **YES** — کھ گھ چھ تھ ٹھ دھ ڈھ پھ بھ | **NO** aspirated series |
| Compound verbs with کرنا | **YES** — Indo-Aryan pattern (Hindi करना cognate) | Persian uses کردن, but Urdu کرنا is Indo-Aryan native |
| Honorific levels | **3** — تو/تم/آپ | **2** — تو/شما |

**When in doubt: Urdu is Indo-Aryan, with Indo-Aryan grammar wrapped in Perso-Arabic script and enriched by Persian-Arabic vocabulary.** It is the sister language of Hindi, the cousin of Punjabi/Bengali/Marathi, and the literary heir of the Mughal court.

---

## Register — تو (intimate) / تم (peer) / آپ (formal)

Urdu distinguishes **three** honorific levels via the second-person pronoun. Each pronoun takes a different verb conjugation, so register affects every verb in a sentence. **Software UI default is formal آپ throughout.**

| Register | Pronoun | "You save" | "Your file" | "Please click" | Use case |
|----------|---------|-----------|-------------|----------------|----------|
| **آپ (formal/respectful — DEFAULT)** | آپ | محفوظ کرتے ہیں / کیجیے | آپ کی فائل | براہ کرم کلک کیجیے / کریں | UI, business, news, formal address, elders, strangers, any unknown audience |
| **تم (peer/familiar)** | تم | محفوظ کرتے ہو | تمہاری فائل | کلک کرو | Close friends, peers, family of same generation, casual chat apps |
| **تو (intimate/inferior)** | تو | محفوظ کرتا ہے | تیری فائل | کلک کر | Children, very close intimates, God in prayer, contempt; **NEVER in software UI** |

**Hard rules:**

1. **Software UI uses آپ — always.** This is non-negotiable for product copy aimed at general users.
2. **Never mix آپ, تم, and تو in the same file.** All verb endings, pronouns, and possessive forms must agree with one register.
3. **آپ is the polite plural too** — it can address one person formally or multiple people. It is the only safe default for unknown audience.
4. **تم is informal/familiar** — use only when the source text is explicitly casual peer-to-peer (chat app among friends, intimate marketing, children's product to older children).
5. **تو is intimate** — never use in software. It can sound insulting to an adult stranger.

### Verb ending table (present tense, "to do" کرنا)

| Person | آپ-form (formal) | تم-form (peer) | تو-form (intimate) |
|--------|-------------------|------------------|---------------------|
| I do (masc) | میں کرتا ہوں | میں کرتا ہوں | میں کرتا ہوں |
| I do (fem) | میں کرتی ہوں | میں کرتی ہوں | میں کرتی ہوں |
| You do (masc) | **آپ کرتے ہیں** | **تم کرتے ہو** | **تو کرتا ہے** |
| You do (fem) | **آپ کرتی ہیں** | **تم کرتی ہو** | **تو کرتی ہے** |
| He/she does | وہ کرتا/کرتی ہے | وہ کرتا/کرتی ہے | وہ کرتا/کرتی ہے |
| We do | ہم کرتے ہیں | ہم کرتے ہیں | ہم کرتے ہیں |
| You (pl.) do | آپ کرتے ہیں | تم لوگ کرتے ہو | (rare) |
| They do | وہ کرتے ہیں | وہ کرتے ہیں | وہ کرتے ہیں |

### Imperative table — the most important for UI

| Verb | آپ form (DEFAULT) | تم form (avoid) | تو form (never) |
|------|---------------------|-------------------|------------------|
| Do / make | **کریں** / **کیجیے** | کرو | کر |
| Save | **محفوظ کریں / محفوظ کیجیے** | محفوظ کرو | محفوظ کر |
| Delete | **حذف کریں / حذف کیجیے** | حذف کرو | حذف کر |
| Click | **کلک کریں** | کلک کرو | کلک کر |
| Enter | **درج کریں** | درج کرو | درج کر |
| Open | **کھولیں / کھولیے** | کھولو | کھول |
| Close | **بند کریں** | بند کرو | بند کر |
| See / view | **دیکھیں / دیکھیے** | دیکھو | دیکھ |
| Give | **دیں / دیجیے** | دو | دے |
| Take | **لیں / لیجیے** | لو | لے |
| Come | **آئیں / آئیے** | آؤ | آ |
| Go | **جائیں / جائیے** | جاؤ | جا |

**The two آپ-form imperative variants — کریں vs کیجیے:**

- **کریں** is the standard formal imperative. Shorter, more common in modern UI.
- **کیجیے** is more elevated/respectful, slightly more old-fashioned, common in printed publications and high-formal contexts.
- **For UI buttons:** use کریں (محفوظ کریں, حذف کریں). For long-form polite instructions in onboarding/help: کیجیے is also acceptable but be consistent.

### Possessive (genitive) table

The genitive postposition کا/کی/کے agrees with the **possessed noun's gender and number**, NOT the possessor's gender.

| English | آپ-form (UI default) | تم-form (informal) |
|---------|----------------------|---------------------|
| my (masc sg) file | میری فائل | میری فائل |
| your (masc sg) file | **آپ کی فائل** | **تمہاری فائل** |
| his/her file | اس کی فائل | اس کی فائل |
| our file | ہماری فائل | ہماری فائل |
| your (pl.) file | آپ کی فائل | تم لوگوں کی فائل |
| their file | ان کی فائل | ان کی فائل |
| my (masc sg) account | میرا اکاؤنٹ | میرا اکاؤنٹ |
| your account | **آپ کا اکاؤنٹ** | **تمہارا اکاؤنٹ** |
| your password | **آپ کا پاس ورڈ** | **تمہارا پاس ورڈ** |

**Note:** میرا/میری/میرے, ہمارا/ہماری/ہمارے, تمہارا/تمہاری/تمہارے follow the same گ گ ی pattern as کا/کی/کے.

### Register auto-detection from source

| Source signal | Target register |
|---------------|-----------------|
| Neutral product/UI prose (`Click to save`, `Your file was uploaded`) — **DEFAULT** | **آپ formal** — براہ کرم کلک کریں, آپ کی فائل اپ لوڈ ہو گئی |
| Contractions, exclamations, casual lexicon (`Hey!`, `Let's…`, emoji-heavy) | آپ formal still recommended, but soften — drop براہ کرم in buttons, allow short status forms |
| Legal/financial/very-formal (terms of service, banking, government) | آپ formal + elevated vocabulary (مہربانی فرما کر, نوازش کیجیے, آنجناب, جناب/محترمہ titles) |
| Children's product, chat-app personal voice between peers | تم informal — but be absolutely sure this is the brand voice |
| Prayer, religious text addressing God | تو (intimate-to-the-divine), but this is poetic, not UI |

**Hard rule: when in doubt, use آپ.** Defaulting to formal is always safe; defaulting to تم can offend an unknown audience; defaulting to تو can outright insult.

---

## Critical Hard Rules

### 1. Perso-Arabic Nastaliq script — RTL with Indo-Aryan extensions (severity 2.5)

Urdu is written in the **Perso-Arabic alphabet** extended with **additional Urdu-specific letters** for Indo-Aryan sounds (retroflex, aspirated, nasalized). The traditional and culturally-preferred calligraphic style is **Nastaliq (نستعلیق)** — a flowing diagonal style developed in 14th-century Persia and perfected for Urdu in Mughal India.

**Nastaliq vs Naskh — the visual style matters:**

- **Nastaliq (نستعلیق)** — flowing, diagonal, hand-written-feeling, letters cascade from upper-right to lower-left within each ligature. This is the traditional Urdu publishing style. Native Urdu speakers expect this for serious reading material.
- **Naskh (نسخ)** — upright, regular, horizontal — this is the standard Arabic print style. Persian also accepts Naskh. Urdu in **Naskh feels foreign or low-quality** to native readers, though it is increasingly accepted on screens due to font availability.

**Recommended Urdu fonts:**

- **Jameel Noori Nastaleeq** — gold-standard Urdu Nastaliq for print/screen.
- **Noto Nastaliq Urdu** — Google's open-source Nastaliq, well-supported across platforms.
- **Mehr Nastaliq Web** — web-optimized Nastaliq.
- **Avoid** plain Arabic Naskh fonts (Amiri, Scheherazade) for production Urdu UI — they read as "Arabic" to Urdu speakers.

When specifying CSS or design for Urdu UI:

```css
font-family: "Jameel Noori Nastaleeq", "Noto Nastaliq Urdu", "Mehr Nastaliq Web", serif;
direction: rtl;
text-align: right;
```

**RTL direction rules** — same as Arabic and Persian:

- Text flows right-to-left.
- UI elements (navigation, icons, scroll direction) mirror to RTL layout.
- Embedded Latin text (English brand names, code, URLs) stays LTR — bidi algorithm handles this when container is `dir="rtl"` or `dir="auto"`.
- Punctuation appears at the **visual left** but is **logically last** in the string. Type in logical order; editor displays correctly.

### 2. Urdu alphabet extensions beyond Arabic and Persian (severity 2.0)

Urdu's alphabet **extends both Arabic and Persian** with letters that capture Indo-Aryan sounds. These are non-negotiable: using Arabic-only letters for Indo-Aryan sounds in Urdu words is a fundamental error.

**Letters Urdu shares with Persian (NOT in Arabic):**

| Letter | Name | Unicode | Sound | Example |
|--------|------|---------|-------|---------|
| **پ** | pe | U+067E | /p/ | پاکستان (Pakistan), پانی (water) |
| **چ** | che | U+0686 | /tʃ/ | چاند (moon), چائے (tea) |
| **ژ** | zhe | U+0698 | /ʒ/ | ژالہ (hailstone), ژوب (place name) |
| **گ** | gāf | U+06AF | /g/ | گھر (house), گاؤں (village) |

**Letters unique to Urdu (NOT in standard Arabic or Persian):**

| Letter | Name | Unicode | Sound | Example |
|--------|------|---------|-------|---------|
| **ٹ** | ṭe (retroflex) | U+0679 | /ʈ/ | ٹماٹر (tomato), ٹھیک (correct) |
| **ڈ** | ḍāl (retroflex) | U+0688 | /ɖ/ | ڈاکٹر (doctor), ڈبہ (box) |
| **ڑ** | ṛe (retroflex flap) | U+0691 | /ɽ/ | بڑا (big), لڑکا (boy) |
| **ں** | nūn ghunna (nasalization) | U+06BA | nasal vowel | ہاں (yes), نہیں (no), میں (I/in) |
| **ھ** | dō-cašmī he (aspiration marker) | U+06BE | aspirated consonant | کھانا (food), گھر (house), بھائی (brother) |
| **ے** | baṛī ye (final/long ye) | U+06D2 | /e:/ or /ɛ:/ | ہے (is), میرے (my), چائے (tea) |

**The two ye letters in Urdu:**

- **ی** (U+06CC, choṭī ye / small ye) — used initially, medially, and for /i:/ sound in final position when joined: کتابی (booky)
- **ے** (U+06D2, baṛī ye / large ye) — used ONLY in final unjoined position for /e:/ /ɛ:/ sound: ہے (hai = is), کرے (kare = does), پے (pe = on)

**Using the wrong ye is a common error.** Final ـے vs ـی distinguishes:

- ہے (hai = "is") vs ہی (hī = "only/just")
- کرے (kare = "may do/does subjunctive") vs کری (karī = informal feminine past)

**Aspirated consonants — the do-cashmi he ھ (severity 2.0):**

Urdu uses **ھ** (do-cashmi he, "two-eyed he", U+06BE) specifically to mark aspiration AFTER a consonant. This distinguishes minimal pairs:

| Unaspirated | Aspirated | Meaning |
|-------------|-----------|---------|
| کل (kal) | **کھل** (khal) | "tomorrow/yesterday" vs "husk" |
| پل (pal) | **پھل** (phal) | "bridge/moment" vs "fruit" |
| تال (tāl) | **تھال** (thāl) | "rhythm" vs "platter" |
| ٹیک (ṭek) | **ٹھیک** (ṭhīk) | (name) vs "correct/OK" |
| جا (jā) | **جھا** (jhā) | "go" (imperative) vs (Indic surname) |
| ڈال (ḍāl) | **ڈھال** (ḍhāl) | "throw" vs "shield/slope" |
| بال (bāl) | **بھال** (bhāl) | "hair" vs (rare/poetic) |

**Aspirated series:** کھ، گھ، چھ، جھ، ٹھ، ڈھ، تھ، دھ، پھ، بھ، (less common: لھ، مھ، نھ، رھ، یھ)

**NEVER use** the regular Arabic-style **ہ** (he, U+06C1) for aspiration in Urdu. The aspirating ھ has TWO loops (two "eyes" — دو چشمی do-cashmi); the regular he has ONE loop (a single goal-shape).

| Wrong (regular he) | Correct (do-cashmi he) | Meaning |
|--------------------|--------------------------|---------|
| کہلانا | **کھلانا** | "to feed" — requires aspirated کھ |
| پہول | **پھول** | "flower" — requires aspirated پھ |
| گہر | **گھر** | "house" — requires aspirated گھ |

**Detection regex (for QA):**

```regex
# Look for likely aspirated-consonant errors (regular ہ following a consonant inside a word, where aspirating ھ was probably meant):
[کگچجٹڈتدپب]ہ
# These should usually be:
[کگچجٹڈتدپب]ھ  (U+06BE)
```

**Retroflex consonants ٹ ڈ ڑ — Indo-Aryan, NOT in Arabic or Persian (severity 2.0):**

Retroflex consonants are produced with the tongue curled back against the hard palate. They are a defining Indo-Aryan feature, present in Hindi, Punjabi, Bengali, Marathi, Tamil, etc. Arabic and Persian do not have them.

| Retroflex (Urdu) | Dental/regular (Urdu/Arabic/Persian) | Distinction matters |
|------------------|--------------------------------------|---------------------|
| ٹ (ṭe) — /ʈ/ | ت (te) — /t̪/ | ٹماٹر (tomato) ≠ تماشا (spectacle) |
| ڈ (ḍāl) — /ɖ/ | د (dāl) — /d̪/ | ڈاکٹر (doctor) ≠ دار (post/hanger) |
| ڑ (ṛe) — /ɽ/ | ر (re) — /r/ | لڑکا (boy) ≠ لرکا (rare/none) |

Using د instead of ڈ or ت instead of ٹ in Urdu words is a fundamental misspelling.

**Nasalization ں (nūn ghunna, U+06BA — severity 2.0):**

ں (nūn ghunna, literally "hidden nūn") marks nasalization of the preceding vowel WITHOUT pronouncing a full /n/ consonant. It appears WORD-FINAL and contrasts with regular ن (nūn, /n/).

| Regular ن (full nasal consonant) | Nasal ں (vowel nasalization only) |
|----------------------------------|------------------------------------|
| نون (nūn — name of letter) | نوں (rare) |
| ہاں (hāⁿ — "yes") — vowel nasalization | (no contrast pair) |
| نہیں (nahīⁿ — "no") | (no plain ن version) |
| میں (mein — "I" or "in") | مین (rare; main = "main" loanword) |

**Common Urdu words with ں:**

- ہاں (yes), نہیں (no), میں (I/in), ہم (we), کہاں (where), یہاں (here), وہاں (there), جہاں (where-relative), کیوں (why), کیسے (how), کہیں (somewhere/anywhere)

In medial position, nasalization is typically written with ن (followed by a consonant) rather than ں. ں is primarily a word-final phenomenon.

### 3. SOV word order — verb at the end (severity 2.5)

Urdu is rigidly **SOV** (Subject-Object-Verb). The verb almost always comes **last** in the clause.

| English (SVO) | Urdu (SOV) | Word-by-word |
|---------------|------------|--------------|
| I read a book. | میں کتاب پڑھتا ہوں۔ | I book read AUX. |
| The user saves the file. | صارف فائل محفوظ کرتا ہے۔ | user file save does. |
| You should click the button. | آپ کو بٹن پر کلک کرنا چاہیے۔ | you DAT button on click to-do should. |
| Please enter your password. | براہ کرم اپنا پاس ورڈ درج کریں۔ | please own password enter do. |

**Word order template (formal):**

```
[Time/Place] [Subject + erg/dat] [Indirect Obj + postposition] [Direct Obj (+ کو)] [Adverb] [Verb-complex]
```

**The verb complex** in Urdu can include: main verb + auxiliary (ہے، ہیں، تھا، تھے، گا، گے) + modal (سکنا، چاہنا، چاہیے، پڑنا). All of this stays at the **end**.

**Common errors (English-influenced SVO retention):**

| ✗ Wrong (SVO calque) | ✓ Correct (SOV) |
|----------------------|------------------|
| صارف محفوظ کرتا ہے فائل | **صارف فائل محفوظ کرتا ہے** |
| براہ کرم درج کریں پاس ورڈ | **براہ کرم پاس ورڈ درج کریں** |
| سسٹم ارسال کرتا ہے پیغام | **سسٹم پیغام ارسال کرتا ہے** |
| میں پڑھتا ہوں کتاب | **میں کتاب پڑھتا ہوں** |

**Important: passive voice also follows SOV** — the verb complex (including کیا جانا / کی جانا) stays at end:

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| کیا جا سکتا ہے استعمال | **استعمال کیا جا سکتا ہے** ("can be used") |
| فائل ہے محفوظ ہو رہی | **فائل محفوظ ہو رہی ہے** ("file is being saved") |

### 4. Postpositions, NOT prepositions (severity 2.0)

Urdu has **postpositions** that follow the noun (English uses prepositions that precede). The noun takes **oblique case** before most postpositions.

**Core postpositions:**

| Postposition | Function | Example |
|--------------|----------|---------|
| **نے** | Ergative (perfective transitive subject) | میں نے کتاب پڑھی (I-ERG book read) |
| **کو** | Dative / definite accusative | آپ کو پیغام آیا (to-you message came); فائل کو حذف کریں (delete THE file) |
| **سے** | Ablative / instrumental / "from", "with", "by" | گھر سے (from home); قلم سے لکھنا (to write with pen) |
| **میں** | Locative "in" | فولڈر میں (in folder); شہر میں (in city) |
| **پر** | Locative "on" / "at" | میز پر (on table); بٹن پر کلک (click on button) |
| **تک** | "up to" / "until" | کل تک (until tomorrow); گھر تک (up to home) |
| **سے پہلے** | "before" | کل سے پہلے (before tomorrow) |
| **کے بعد** | "after" | کام کے بعد (after work) |
| **کے لیے** | "for" | آپ کے لیے (for you) |
| **کے ساتھ** | "with" (accompaniment) | دوست کے ساتھ (with friend) |
| **کے بارے میں** | "about" | اس کے بارے میں (about it/him/her) |

**Genitive کا / کی / کے — agrees with the POSSESSED noun (severity 2.0):**

The genitive postposition takes three forms depending on the gender/number/case of the **possessed noun** (NOT the possessor):

| Possessed noun | Form | Example |
|----------------|------|---------|
| Masculine singular direct | **کا** | لڑکے کا گھر (boy's house — گھر is masc sg) |
| Masculine plural OR masculine oblique | **کے** | لڑکے کے گھر میں (in the boy's houses / in the boy's house OBL) |
| Feminine (sg or pl) | **کی** | لڑکے کی کتاب (boy's book — کتاب is fem) |

**Common error:** matching کا/کی/کے to the possessor's gender (wrong — it agrees with the possessed).

| ✗ Wrong | ✓ Correct | Why |
|---------|-----------|-----|
| فولڈر کا فائل | **فولڈر کی فائل** | فائل is feminine — use کی |
| فائل کی نام | **فائل کا نام** | نام is masculine — use کا |
| صارف کی پاس ورڈ | **صارف کا پاس ورڈ** | پاس ورڈ is masculine — use کا |
| لڑکی کا ماں | **لڑکی کی ماں** | ماں is feminine — use کی |

**Oblique case before postpositions (severity 1.5):**

Masculine nouns ending in -ا change to -ے before a postposition. Plural masculine nouns and feminine nouns end in -وں in oblique plural.

| Direct (nominative) | Oblique (before postposition) | Example |
|---------------------|-------------------------------|---------|
| لڑکا (boy) sg | لڑکے کو، لڑکے سے، لڑکے کا | (the boy's, to the boy) |
| لڑکے (boys) pl | لڑکوں کو، لڑکوں سے، لڑکوں کا | (to the boys) |
| لڑکی (girl) sg | لڑکی کو، لڑکی سے، لڑکی کی | (no change for fem -ی sg) |
| لڑکیاں (girls) pl | لڑکیوں کو، لڑکیوں سے، لڑکیوں کی | (to the girls) |
| بڑا (big) m sg | بڑے سسٹم میں | (in the big system) |
| نیا (new) m sg | نئے بٹن پر | (on the new button) |

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| بڑا سسٹم میں | **بڑے سسٹم میں** |
| نیا بٹن پر کلک | **نئے بٹن پر کلک** |
| فائل میں (when plural meant) | **فائلوں میں** |

### 5. Ergative case marking نے (severity 2.5)

This is the single hardest grammatical feature for non-Indo-Aryan speakers to acquire. Urdu (like Hindi, Punjabi, etc.) has a **split-ergative system**: in the perfective (completed) past tense with a transitive verb, the subject takes **نے** and the verb agrees with the **object** (not the subject).

**Rule:**

- **Transitive + perfective** → subject + **نے**, verb agrees with object's gender/number.
- **Intransitive + perfective** → no نے, verb agrees with subject normally.
- **Non-perfective** (present, future, habitual, progressive) → no نے, normal nominative-style agreement with subject.

| English | Urdu | Analysis |
|---------|------|----------|
| I read the book. (perf) | میں نے کتاب پڑھی۔ | نے on subject; verb پڑھی (fem sg) agrees with کتاب (fem sg) |
| I read the books. (perf) | میں نے کتابیں پڑھیں۔ | verb پڑھیں (fem pl) agrees with کتابیں |
| I read the file. (perf) | میں نے فائل پڑھی۔ | verb پڑھی (fem sg) agrees with فائل (fem) |
| I deleted the file. (perf) | **میں نے فائل حذف کی۔** | verb کی (fem sg) agrees with فائل (fem) |
| She deleted the files. (perf) | **اس نے فائلیں حذف کیں۔** | verb کیں (fem pl) agrees with فائلیں |
| He saved the password. (perf) | اس نے پاس ورڈ محفوظ کیا۔ | verb کیا (masc sg) agrees with پاس ورڈ (masc sg) |
| I will read the book. (future) | میں کتاب پڑھوں گا۔ | NO نے (future); verb agrees with subject (masc پڑھوں گا) |
| I am reading the book. (prog) | میں کتاب پڑھ رہا ہوں۔ | NO نے (progressive); verb agrees with subject |
| I went home. (intransitive perf) | میں گھر گیا۔ | NO نے (intransitive); verb agrees with subject |

**Common errors:**

| ✗ Wrong | ✓ Correct | Why |
|---------|-----------|-----|
| میں نے فائل حذف کیا | **میں نے فائل حذف کی** | فائل is fem → verb must be کی (fem) |
| اس نے فائلیں ڈاؤن لوڈ کیا | **اس نے فائلیں ڈاؤن لوڈ کیں** | فائلیں is fem pl → verb must be کیں |
| میں کتاب پڑھی | **میں نے کتاب پڑھی** | Perfective transitive needs نے |
| میں نے گیا | **میں گیا** | جانا (to go) is intransitive — no نے |
| اس نے فائل کو حذف کی | **اس نے فائل کو حذف کیا** | With کو-marked object, verb defaults to masc sg |

**The کو-marked object rule:** when the direct object takes کو (because it is definite/specific), the verb defaults to **masculine singular** regardless of the object's actual gender:

| Sentence | Why |
|----------|-----|
| اس نے فائل حذف کی۔ | object فائل (fem) bare → verb agrees: کی fem sg |
| اس نے فائل کو حذف کیا۔ | object فائل کو (with کو) → verb defaults to masc sg: کیا |

### 6. Grammatical gender (severity 2.5)

Urdu has **TWO genders**: masculine (مذکر mużakkar) and feminine (مؤنث muʾannas). Every noun has a fixed gender. Adjectives, verbs, and possessive postpositions must agree.

**Tech term genders — memorize:**

**Masculine (مذکر):**
- سسٹم (system), سرور (server), فولڈر (folder), بٹن (button), ڈیٹا (data), پاس ورڈ (password), پیغام (message), لنک (link), پروگرام (program), بلاگ (blog), یوزر (user — but صارف is also m), اکاؤنٹ (account), براؤزر (browser), ڈومین (domain), کوڈ (code), فنکشن (function)

**Feminine (مؤنث):**
- فائل (file), ویب سائٹ (website), سیٹنگ / سیٹنگز (setting/settings), ایپ / ایپلی کیشن (app), ای میل (email), ترتیبات (settings, native form), تصویر (picture), فہرست (list), زبان (language), ویڈیو (video — sometimes m), سکرین (screen — sometimes m), یونیورسٹی (university), ڈاؤن لوڈ (download — context-dependent)

**Adjective agreement table:**

| Adjective form | Masc sg direct | Masc pl / masc oblique sg | Feminine (sg or pl) |
|----------------|----------------|---------------------------|----------------------|
| نیا (new) | نیا فولڈر | نئے فولڈر، نئے بٹن میں | نئی فائل، نئی فائلیں |
| اچھا (good) | اچھا کام | اچھے کام، اچھے کام سے | اچھی فائل، اچھی فائلیں |
| بڑا (big) | بڑا سسٹم | بڑے سسٹم، بڑے سسٹم میں | بڑی فائل |
| پرانا (old) | پرانا اکاؤنٹ | پرانے اکاؤنٹ | پرانی فائل |
| چھوٹا (small) | چھوٹا بٹن | چھوٹے بٹن | چھوٹی فہرست |

**Adjectives ending in consonants (مستحکم adjectives like خوبصورت, اہم, مفید) DO NOT change** for gender or number.

| Form | Example |
|------|---------|
| خوبصورت فائل | (no change) |
| خوبصورت اکاؤنٹ | (no change) |
| خوبصورت فائلیں | (no change) |
| اہم پیغام | (no change) |
| اہم تنبیہ | (no change) |

**Common errors:**

| ✗ Wrong | ✓ Correct | Why |
|---------|-----------|-----|
| نیا فائل | **نئی فائل** | فائل is feminine |
| نیا ویب سائٹ | **نئی ویب سائٹ** | ویب سائٹ is feminine |
| اچھا سیٹنگ | **اچھی سیٹنگ** | سیٹنگ is feminine |
| نیا سیٹنگز | **نئی سیٹنگز** | سیٹنگز feminine (also plural) |
| نئی سسٹم | **نیا سسٹم** | سسٹم is masculine |
| نئی پاس ورڈ | **نیا پاس ورڈ** | پاس ورڈ is masculine |

### 7. Compound verbs with کرنا — the tech vocabulary pattern (severity 2.0)

Urdu (like Hindi) builds most loanword verbs using the pattern: **noun + کرنا** (to do). This is the standard for almost all tech/borrowed verbs.

**Pattern: [English noun in Urdu transliteration OR native noun] + کرنا**

| English verb | Urdu compound verb (infinitive) | Imperative (آپ form) |
|--------------|--------------------------------|------------------------|
| save | محفوظ کرنا | **محفوظ کریں** |
| delete | حذف کرنا | **حذف کریں** |
| click | کلک کرنا | **کلک کریں** |
| cancel | منسوخ کرنا | **منسوخ کریں** |
| edit | ترمیم کرنا / ایڈٹ کرنا | **ترمیم کریں / ایڈٹ کریں** |
| search | تلاش کرنا / سرچ کرنا | **تلاش کریں** |
| upload | اپ لوڈ کرنا | **اپ لوڈ کریں** |
| download | ڈاؤن لوڈ کرنا | **ڈاؤن لوڈ کریں** |
| login | لاگ ان کرنا / سائن ان کرنا | **لاگ ان کریں** |
| logout | لاگ آؤٹ کرنا | **لاگ آؤٹ کریں** |
| confirm | تصدیق کرنا / تأئید کرنا | **تصدیق کریں / تأئید کریں** |
| send | بھیجنا (native) / ارسال کرنا | **بھیجیں / ارسال کریں** |
| receive | وصول کرنا / حاصل کرنا | **وصول کریں** |
| submit | جمع کرنا / جمع کرانا | **جمع کریں / جمع کرائیں** |
| select | منتخب کرنا | **منتخب کریں** |
| share | شیئر کرنا / بانٹنا | **شیئر کریں** |
| copy | کاپی کرنا / نقل کرنا | **کاپی کریں / نقل کریں** |
| paste | پیسٹ کرنا / چسپاں کرنا | **پیسٹ کریں / چسپاں کریں** |
| close | بند کرنا | **بند کریں** |
| open | کھولنا (native) | **کھولیں** |

**Hard rule for UI: complete the compound verb.** Don't strand the noun without کرنا/کریں.

| ✗ Wrong (stranded noun) | ✓ Correct (compound complete) |
|--------------------------|--------------------------------|
| کلک | **کلک کریں** |
| محفوظ | **محفوظ کریں** |
| سیو | **محفوظ کریں** |
| ڈیلیٹ | **حذف کریں** |

**Note: some verbs are native (single-word, no کرنا needed):**

- کھولنا (to open) → کھولیں
- بند کرنا (to close) → بند کریں (though native form is بند ہونا for intransitive)
- پڑھنا (to read) → پڑھیں
- لکھنا (to write) → لکھیں
- دیکھنا (to see) → دیکھیں
- بھیجنا (to send) → بھیجیں
- پکڑنا (to grab) → پکڑیں
- چھوڑنا (to release/leave) → چھوڑیں

These don't take کرنا — they conjugate directly.

### 8. ICU plurals — Urdu uses one + other (severity 1.5)

Urdu CLDR plural categories: **one** + **other**. Both forms use the **plural noun form** (NOT singular like Persian — this is different from Persian!).

**Note: Urdu IS different from Persian here.** Persian keeps the noun singular after numbers (`پنج فایل`). Urdu **does pluralize** after counts in the ICU `other` branch.

```icu
{count, plural,
  one {# نئی فائل}
  other {# نئی فائلیں}
}
```

**Plural noun formation in Urdu:**

| Pattern | Singular | Plural | Example |
|---------|----------|--------|---------|
| Masc -ا → -ے | لڑکا | لڑکے | "boy" → "boys" |
| Masc consonant → no change | فولڈر | فولڈر (or فولڈرز Englishloan) | "folder" → "folders" |
| Fem -ی → -یاں | لڑکی | لڑکیاں | "girl" → "girls" |
| Fem consonant → -یں | فائل | فائلیں | "file" → "files" |
| Fem -ت → -تیں or -وں oblique | عورت | عورتیں | "woman" → "women" |
| Arabic-origin plural (sometimes preserved) | کتاب | کتابیں OR کتب (Arabic broken pl) | "book" → "books" |
| Oblique plural | فائلیں | فائلوں (before postposition) | "in the files" → فائلوں میں |

**ICU plural example:**

```icu
{count, plural,
  one {# نئی فائل}
  other {# نئی فائلیں}
}
```

**Common errors:**

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| `{count} نئی فائل` for plural counts | `{count} نئی فائلیں` |
| `{count} نیا فائلیں` | `{count} نئی فائلیں` (adjective agrees fem pl) |
| Importing Arabic six-category zero/one/two/few/many/other | Collapse to Urdu one + other |

**When the source has six Arabic categories:** collapse zero/two/few/many → other. Urdu needs only two.

### 9. Urdu punctuation (severity 2.0)

Urdu uses a **mix of Arabic punctuation and Latin punctuation**, with one important Urdu-specific mark.

| Mark | Urdu | Unicode | Notes |
|------|------|---------|-------|
| Question mark | **؟** | U+061F | Same as Arabic/Persian. Mirror of Latin ?. Visual position: LEFT (logical end). |
| Comma | **،** | U+060C | Same as Arabic/Persian. NOT Latin `,`. |
| Semicolon | **؛** | U+061B | Same as Arabic/Persian. NOT Latin `;`. |
| Full stop / period | **۔** | **U+06D4 (URDU FULL STOP)** | **CRITICAL: Urdu has its own full stop. NOT Latin `.`** — this is a small horizontal stroke, distinct from Arabic/Persian which use Latin `.` |
| Colon | `:` | U+003A | Same as Latin. |
| Exclamation | `!` | U+0021 | Same as Latin. |
| Quotation marks | **"..."** or **«...»** | U+201C/U+201D or U+00AB/U+00BB | Both accepted. Latin curly quotes "..." are most common in modern Urdu UI; guillemets «...» borrowed from Persian convention in formal contexts. |
| Hyphen | `-` | U+002D | Same as Latin. |
| Ellipsis | `…` | U+2026 | Same as Latin. |
| Percent | `%` or `٪` (U+066A) | | Western `%` widely accepted. |

**The Urdu full stop ۔ — critical (severity 2.0):**

Urdu's signature punctuation mark is the **Urdu full stop ۔** (Unicode U+06D4). It is a short horizontal stroke, distinct from the Latin period `.`.

| ✗ Wrong (Latin period) | ✓ Correct (Urdu full stop) |
|-------------------------|------------------------------|
| محفوظ ہو گیا. | **محفوظ ہو گیا۔** |
| فائل نہیں ملی. | **فائل نہیں ملی۔** |
| براہ کرم کلک کریں. | **براہ کرم کلک کریں۔** |

**When the Latin period IS acceptable:**

- Inside Latin-script tech identifiers preserved as English: `Next.js`, `Node.js`, `package.json` — the `.` here is part of the identifier.
- In dates with numeric format: `15.01.2024` (European-style) — though `/` is more common.
- In abbreviations of English origin: `e.g.`, `i.e.` — but in Urdu prose, prefer مثلاً (for example) and یعنی (that is).

**In Urdu sentences, the sentence-final punctuation should be ۔ — using `.` is a low-quality marker.**

**Other punctuation rules:**

1. Use `؟` not `?` at end of Urdu questions. ASCII `?` is wrong in Urdu prose.
2. Use `،` not `,` in Urdu sentences. ASCII `,` is wrong.
3. Use `؛` not `;` in Urdu sentences.
4. **No space before** `؟ ، ؛ : ! ۔` (unlike French).
5. **No comma before اور (and) / یا (or)** typically — Urdu list-comma rules align with Arabic/Persian:
   - `فائل، فولڈر اور دستاویز` ✓ (no comma before اور)
   - **Comma DOES appear** before subordinating conjunctions: کہ (that), اگر (if), کیونکہ (because), جب (when), جس کے بعد (after which)
6. **Bidirectional behavior:** punctuation in RTL displays at the visual left but logically last. Type in logical order; renderer handles display.

**Example:**

```
Logical (storage) order:  کیا آپ نے فائل محفوظ کی؟
Visual (display) order:   ؟کیا آپ نے فائل محفوظ کی
                          ↑ question mark appears at far left
```

### 10. ZWNJ (Zero-Width Non-Joiner, U+200C) — half-space in Urdu (severity 1.5)

Urdu uses ZWNJ (نیم فاصلہ nīm-fāṣila, "half-space") less aggressively than Persian, but still in certain contexts. Unlike Persian which REQUIRES ZWNJ with می‌- and ـها, Urdu compound verbs typically use a **full space** between components (محفوظ کریں, not محفوظ‌کریں).

**Urdu ZWNJ contexts (where it matters):**

| Context | ✗ Wrong | ✓ Correct |
|---------|---------|-----------|
| Borrowed Persian compound words | (varies) | Some words preserve Persian ZWNJ convention |
| Compound noun + suffix | (when full space breaks meaning) | Use ZWNJ for inseparable compounds |
| Plural ـیں on stems where ligature breaks | فائل یں | **فائلیں** (no space — no ZWNJ needed) |
| Aspiration ھ following consonant | کھ انا | **کھانا** (no space, no ZWNJ — write contiguous) |

**Hard rule for Urdu:** compound verbs use **full space**: `محفوظ کریں`, `حذف کریں`, `کلک کریں`. Do NOT join them as `محفوظکریں` (joined, looks wrong) or insert ZWNJ unnecessarily.

**When ZWNJ IS useful in Urdu:**

- In Persian-borrowed compound words preserved with Persian convention: نیم‌فاصلہ itself uses ZWNJ.
- In modern UI/web fonts where ligatures break across morpheme boundaries.

**Common QA bug:** translation tools that "normalize whitespace" can strip ZWNJ; verify your pipeline preserves U+200C if your Urdu source uses it.

### 11. Bidirectional text — preserving Latin tech identifiers (severity 1.5)

Urdu is RTL. Embedded Latin script (Git, API, JSON, URLs, file names, code identifiers) stays LTR. Most rendering engines handle this automatically when the container is `dir="rtl"` or `dir="auto"`.

**Hard rules:**

1. **Never translate code identifiers, file names, URLs, brand names.** They stay in Latin script exactly as in source.
2. **Latin runs inside Urdu sentences** should be preserved as Latin. The bidi algorithm handles visual flow.
3. **Add LRM (U+200E) or RLM (U+200F) markers only when QA confirms a rendering bug** — do not sprinkle them speculatively.

**Examples — Latin tech terms inside Urdu:**

```
✓ کوڈ مینجمنٹ کے لیے Git استعمال کریں۔
✓ API کال کرنے کے لیے، اپنا JWT ٹوکن Authorization ہیڈر میں رکھیں۔
✓ package.json فائل کو روٹ ڈائریکٹری میں رکھیں۔
✓ https://example.com کے ذریعے سائن ان کریں۔

✗ گٹ سے کوڈ مینج کریں۔  (transliteration when keep-Latin is better)
✗ ای پی آئی... (do not spell out API as Urdu letters)
```

**Tech terms typically kept in Latin in Urdu UI:**

- Languages: Python, JavaScript, Go, Rust, Java, C++, TypeScript, PHP, Ruby
- Frameworks: React, Vue, Angular, Next.js, Django, Spring Boot, Laravel
- Tools: Git, GitHub, GitLab, Docker, Kubernetes, npm, pip
- Protocols: HTTP, HTTPS, FTP, SSH, TCP, REST, GraphQL, gRPC
- Formats: JSON, XML, YAML, CSV, PDF, MP4, PNG, SVG
- Commands: ls, cd, git commit, npm install
- URLs, email addresses, file paths, IP addresses
- Brand names: Google, Apple, Microsoft, Facebook/Meta, Amazon, AWS, OpenAI

**Pakistani urban UI tolerates English code-switching** ("Urdu-English mix" or sometimes pejoratively "Urdish") — sentences like `براہ کرم اپنا email address enter کریں` are heard in casual contexts. **For formal UI, prefer pure Urdu.** Mixed Urdu-English is acceptable in casual chat/marketing contexts targeting urban Pakistanis but should not be the default.

### 12. Religious and cultural sensitivity (severity 2.0)

Pakistan is **~96% Muslim** (predominantly Sunni, with Shia minority ~10-15%, plus Ahmadiyya legally non-Muslim, Christian, Hindu, and Sikh minorities). Indian Urdu audiences are predominantly Muslim (the language carries Mughal/Islamic literary heritage and is associated with India's ~200M Muslim population). UI copy for Urdu should respect Islamic values **without alienating non-Muslim Urdu speakers in India** or assuming Arab-style framing.

**Hard rules:**

1. **Don't inject religious phrases** (ان شاء اللہ / الحمد للہ / ماشاء اللہ / بسم اللہ) into translations unless the source already invokes that semantic. They are not generic politeness fillers in software UI. **Exception:** بسم اللہ is sometimes seen at the start of very formal Urdu documents (especially in Pakistan religious-government contexts) — this is a cultural opening, not a UI string.

2. **Cultural Christian-origin idioms** must be re-conceptualized, not literally translated:

| English idiom | ✗ Literal calque | ✓ Urdu cultural equivalent |
|---------------|------------------|------------------------------|
| cross to bear | صلیب اٹھانا | بار سہنا / بھاری ذمہ داری |
| holy grail | جام مقدس | حتمی منزل / بڑی خواہش |
| good Samaritan | نیک سامری | نیک انسان / ہمدرد |
| blessing in disguise | (literal) | بظاہر مصیبت، حقیقت میں رحمت |
| baptism of fire | غسل تعمید کا آگ | کٹھن آزمائش / سخت تجربہ |
| Pandora's box | پنڈورا کا ڈبہ | فتنے کا دروازہ / مصیبت کا آغاز |
| Achilles' heel | اچلیس کی ایڑی | کمزوری کا نکتہ / کمزوری |
| knock on wood | لکڑی پر دستک | ان شاء اللہ / اللہ خیر کرے |
| fingers crossed | (literal) | ان شاء اللہ / امید ہے |
| break a leg | ٹانگ توڑو | کامیابی کی دعا! / اللہ کامیاب کرے! |
| piece of cake | کیک کا ٹکڑا | بائیں ہاتھ کا کھیل / بہت آسان |
| bring home the bacon | (literal — pork!) | حلال روزی کمانا / گھر چلانا |
| champagne problems | (literal — alcohol) | عیش کے مسائل / خوش حالوں کے مسائل |
| kill two birds with one stone | (literal violence) | ایک تیر سے دو شکار |

3. **Halal sensitivity:** Avoid casual metaphors involving pork (سور), alcohol (شراب), or gambling (جوا/قمار) unless they are the literal subject. Use neutral alternatives. Pakistani consumer UI should not normalize haram products.

4. **Interest (سود) framing:** Riba/interest is a sensitive financial topic in Islamic finance. Banks in Pakistan distinguish سودی (interest-bearing, conventional) vs غیر سودی / اسلامی (interest-free, Islamic banking). When translating "interest rate" for financial products, be aware which framing the product wants.

5. **Friday (جمعہ) is the Islamic holy day** — equivalent of Sunday in Christian-majority countries. Friday afternoons in Pakistan are for جمعہ prayer; many businesses close for the prayer hour. Government workdays in Pakistan are Mon–Sat with Fri+Sun typically off (varies by sector).

6. **Major Islamic holidays acknowledged in Urdu UI:**
   - رمضان (Ramadan) — month of fasting
   - عید الفطر (Eid ul-Fitr) — end of Ramadan
   - عید الاضحٰی (Eid ul-Adha) — sacrifice feast, ~70 days after Eid ul-Fitr
   - شب برأت (Shab-e-Barat) — night of forgiveness
   - شب معراج (Shab-e-Mi'raj) — night of ascension
   - یوم آشورا / محرم (Muharram/Ashura) — especially significant for Shia

7. **Dating/relationships:** "Dating app" in Pakistan typically translates as رشتے کی ایپ (matchmaking app) or تعارف کی ایپ (introduction app) rather than the Western "dating" framing which carries the wrong connotation. India-Urdu audiences may accept ڈیٹنگ ایپ more readily.

8. **National identity:**
   - **Pakistani Urdu UI** can lean into national pride: قائد اعظم (Jinnah), یوم آزادی (Independence Day, August 14), pakistan-specific cultural references.
   - **Indian Urdu UI** should be religiously sensitive: avoid framing Urdu as "Muslim-only" (it has Hindu, Sikh, and secular speakers historically), and avoid Pakistan-specific political framing.

9. **Avoid Arab-conflation:** Don't translate "the Arab world" assumptions into Urdu. Pakistanis and Indian Muslims are not Arabs. The Arab-style framing in Urdu sounds religious-political (ummah-style), not cultural.

10. **Bismillah (بسم اللہ):** "بسم اللہ الرحمٰن الرحیم" is sometimes seen at the start of formal documents in Pakistan — government, religious, formal business correspondence. NOT typical in modern app UI but acceptable for traditional/religious products.

---

## UI Conventions

### Button labels — formal imperative with آپ form

Urdu button labels prefer **formal imperative (آپ-form)**: noun + کریں.

**Standard button vocabulary:**

| English | ✓ Urdu (preferred) | ⚠ Alternative (English-loan) |
|---------|--------------------|-------------------------------|
| Save | **محفوظ کریں** | سیو کریں |
| Cancel | **منسوخ کریں** | کینسل کریں |
| Delete | **حذف کریں** | ڈیلیٹ کریں |
| Edit | **ترمیم کریں** | ایڈٹ کریں |
| Send | **بھیجیں / ارسال کریں** | سینڈ کریں |
| Confirm | **تصدیق کریں / تأئید کریں** | کنفرم کریں |
| Continue | **جاری رکھیں** | کنٹینیو کریں |
| Submit | **جمع کرائیں / جمع کریں** | سبمٹ کریں |
| Search | **تلاش کریں** | سرچ کریں |
| Settings | **ترتیبات** | سیٹنگز |
| Sign in / Log in | **سائن ان کریں / لاگ ان کریں** | (often kept English-loan) |
| Sign out / Log out | **سائن آؤٹ کریں / لاگ آؤٹ کریں** | (often English-loan) |
| Sign up | **سائن اپ کریں / رجسٹر کریں** | |
| Upload | **اپ لوڈ کریں** | |
| Download | **ڈاؤن لوڈ کریں** | |
| Refresh | **تازہ کریں / ریفریش کریں** | |
| Close | **بند کریں** | کلوز کریں |
| Open | **کھولیں** | اوپن کریں |
| Next | **اگلا / آگے** | نیکسٹ |
| Previous / Back | **پچھلا / واپس** | |
| Done | **مکمل / ہو گیا** | |
| OK | **ٹھیک ہے / تأئید** | اوکے |
| Copy | **کاپی کریں / نقل کریں** | |
| Paste | **پیسٹ کریں / چسپاں کریں** | |
| Share | **شیئر کریں / بانٹیں** | |
| Yes | **ہاں / جی ہاں** | (use جی for extra politeness) |
| No | **نہیں / جی نہیں** | |

**Picking کریں vs کیجیے:**

- **کریں** is the modern, standard formal imperative. Use this for most UI.
- **کیجیے** is more elevated/respectful — common in printed publications, government forms, and high-formal contexts. Acceptable but sounds slightly old-fashioned for tech UI.

**Pick ONE style per product** — don't mix محفوظ کریں in one button and محفوظ کیجیے in another.

**Never use تو-form or تم-form imperatives in formal UI:**

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| محفوظ کرو | **محفوظ کریں** |
| محفوظ کر | **محفوظ کریں** |
| حذف کرو | **حذف کریں** |
| کلک کر | **کلک کریں** |

### Status messages — progressive / completion / failure / empty

**Progressive (in-flight): use noun + ہو رہا ہے / ہو رہی ہے (gender agrees with subject noun)**

| English | Urdu | Why |
|---------|------|-----|
| Loading... | لوڈ ہو رہا ہے... | ambient/process subject — masc default |
| Saving... | محفوظ ہو رہا ہے... | masc default for process |
| Sending... | بھیجا جا رہا ہے... | passive progressive |
| Processing... | پراسیس ہو رہا ہے... | masc |
| Uploading... | اپ لوڈ ہو رہا ہے... | masc |
| Connecting... | منسلک ہو رہا ہے... | masc |
| Please wait... | براہ کرم انتظار کریں... | imperative |

**Gender agreement matters in completion:** the subject noun's gender determines ہو گیا (m) vs ہو گئی (f).

**Completion: use noun + ہو گیا / ہو گئی (past, with gender agreement)**

| English | Urdu | Subject gender |
|---------|------|----------------|
| Saved. | محفوظ ہو گیا۔ | implicit subject m (e.g., کام) |
| File saved. | فائل محفوظ ہو گئی۔ | فائل is fem → گئی |
| Account created. | اکاؤنٹ بن گیا۔ | اکاؤنٹ is masc → گیا |
| Message sent. | پیغام بھیج دیا گیا۔ / پیغام چلا گیا۔ | پیغام is masc → گیا |
| Email sent. | ای میل بھیج دی گئی۔ | ای میل is fem → گئی |
| Done. | ہو گیا۔ / مکمل ہو گیا۔ | masc default |
| Sent successfully. | کامیابی سے بھیج دیا گیا۔ | passive completion |

**Failure: use noun + نہیں ہوا / نہیں ہوئی / خرابی ہوئی**

| English | Urdu |
|---------|------|
| Save failed. | محفوظ نہیں ہو سکا۔ / محفوظ کرنے میں خرابی ہوئی۔ |
| File not found. | فائل نہیں ملی۔ |
| Could not connect to server. | سرور سے کنکشن نہیں ہو سکا۔ |
| Sending failed. | بھیجنے میں ناکامی ہوئی۔ / نہیں بھیجا جا سکا۔ |
| Error occurred. | خرابی پیش آئی۔ / خطا ہوئی۔ |
| Unable to perform operation. | عمل مکمل نہیں کیا جا سکا۔ |

**Empty state: کوئی [noun] نہیں**

| English | Urdu |
|---------|------|
| No files yet. | ابھی تک کوئی فائل نہیں۔ |
| No results found. | کوئی نتیجہ نہیں ملا۔ |
| No notifications. | کوئی اطلاع نہیں۔ |
| No content to display. | دکھانے کے لیے کوئی مواد نہیں۔ |
| No messages. | کوئی پیغام نہیں۔ |

**Validation / field errors:** noun + ہے copula pattern

| English | Urdu |
|---------|------|
| This field is required. | یہ فیلڈ لازمی ہے۔ |
| Invalid format. | غلط فارمیٹ۔ / فارمیٹ درست نہیں۔ |
| Password must be at least 8 characters. | پاس ورڈ کم از کم 8 حروف کا ہونا چاہیے۔ |
| Email is invalid. | ای میل درست نہیں۔ |

**Action instructions:** آپ-form imperative with براہ کرم

- پاس ورڈ درج کریں۔ (Enter your password.)
- کم از کم ایک آپشن منتخب کریں۔ (Choose at least one option.)
- دوبارہ کوشش کریں۔ (Try again.)
- براہ کرم معلومات کی تصدیق کریں۔ (Please verify the information.)

### Error messages — what happened + what to do

Urdu error messages should follow the two-part structure: **state the problem, then suggest a next step.**

| ✗ Bare (only what happened) | ✓ With next step |
|------------------------------|-------------------|
| فائل نہیں ملی۔ | **فائل نہیں ملی۔ براہ کرم راستہ چیک کریں۔** |
| نیٹ ورک خرابی۔ | **نیٹ ورک خرابی۔ براہ کرم اپنا انٹرنیٹ کنکشن چیک کریں اور دوبارہ کوشش کریں۔** |
| ای میل غلط۔ | **آپ نے جو ای میل درج کیا وہ درست نہیں۔ براہ کرم پتا چیک کریں۔** |
| پاس ورڈ غلط۔ | **پاس ورڈ غلط ہے۔ براہ کرم دوبارہ کوشش کریں یا "پاس ورڈ بھول گئے" آپشن استعمال کریں۔** |
| رسائی نہیں۔ | **رسائی مسترد ہو گئی۔ براہ کرم سائن ان کریں یا منتظم سے رابطہ کریں۔** |

### Drag-and-drop terminology

Use **native Urdu verbs**, NOT transliterations from English.

| English | ✓ Urdu (native) | ✗ Avoid (transliteration) |
|---------|-----------------|----------------------------|
| drag | کھینچیں | ڈریگ کریں |
| drop | چھوڑیں | ڈراپ کریں |
| release | چھوڑ دیں | ریلیز کریں |
| Drag and drop the file here | فائل کو یہاں کھینچ کر چھوڑیں | فائل کو یہاں ڈریگ اینڈ ڈراپ کریں |
| Drop file here to upload | اپ لوڈ کرنے کے لیے فائل کو یہاں چھوڑیں | (no English calque) |

### File picker

- "Choose a file" → **فائل منتخب کریں**
- "Browse files" → **فائلیں براؤز کریں** (when meaning navigation) or **فائل منتخب کریں** (when meaning upload trigger — prefer this)
- "Open" → **کھولیں**

Avoid `تلاش کریں` for file picker (تلاش = search, not browse).

### Quantities — "X+" / "more than X"

Urdu uses **X سے زیادہ** instead of `X+`.

- `+25 languages` → **25 سے زیادہ زبانیں** ✓ (NOT `+25 زبانیں` or `25+ زبانیں` ✗)
- `5+` → **5 یا زیادہ** or **5 سے زیادہ**
- `+{count} more` → **{count} مزید** or **اور {count} اضافی**

### FOR vs PER — critical distinction

| Source | ✓ Urdu | Meaning |
|--------|--------|---------|
| for 25 languages (total) | **25 زبانوں کے لیے** | Total scope |
| per language (rate) | **فی زبان** / **ہر زبان کے لیے** | Per-unit rate |
| per month | **فی ماہ** / **ہر ماہ** / **ماہانہ** | Per-time rate |
| per year | **فی سال** / **سالانہ** | Per-time rate |
| per user | **فی صارف** / **ہر صارف کے لیے** | Per-unit rate |

Pricing-page wording mixing these is an auto-fail.

### Hashtags, mentions, links in copy

- `#hashtag` (Latin) stays Latin: `#example`.
- `#اردو_ٹیگ` (Urdu hashtag) is also fine for Urdu-tagged content.
- `@username` stays as-is, never translated.
- URLs stay LTR within RTL — engines handle this; don't translate domain names.

---

## Punctuation, Numbers, Dates, Currency

### Numerals — two systems

Urdu has two acceptable numeral systems:

| System | Digits | Use case |
|--------|--------|----------|
| **Urdu/Persian (Extended Arabic-Indic)** | ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹ | Traditional, literary, formal Urdu text |
| **Western (Hindu-Arabic)** | 0 1 2 3 4 5 6 7 8 9 | Modern UI, technical, business, scientific |

**Important Unicode note:** Urdu uses the **same numeral code points as Persian** (U+06F0 to U+06F9), NOT the Arabic-Indic numerals (U+0660 to U+0669). The shapes are slightly different:

- **Persian/Urdu ۴ ۵ ۶** (U+06F4, U+06F5, U+06F6) — slightly different shapes
- **Arabic-Indic ٤ ٥ ٦** (U+0664, U+0665, U+0666) — different shapes
- **Western 4 5 6** (U+0034, U+0035, U+0036)

**Using Arabic-Indic ٤٥٦ in Urdu is wrong** — it should be Persian/Urdu ۴۵۶ if using extended-Arabic style.

**Rule for UI:**

- **Be consistent within a string/screen.** Never mix `5 فائل` with `۷ پیغام` in the same UI.
- **Modern Urdu software typically uses Western 0-9** for tech UI because most users have international keyboards and bidi handling is more reliable.
- **Urdu/Persian ۰-۹** is used in formal/literary contexts, government documents, religious texts, and traditionally-styled UIs (especially newspapers, books).
- **Default for software UI: Western 0-9** unless the brand explicitly leans Urdu-traditional.

### Number formatting — Indian-style lakh/crore grouping

Pakistan and India both use the **South Asian number grouping system**: groups of **3** for the first thousand, then groups of **2** for higher places.

| Number | South Asian | Western | Spoken Urdu |
|--------|-------------|---------|-------------|
| 1,000 | 1,000 | 1,000 | ایک ہزار |
| 10,000 | 10,000 | 10,000 | دس ہزار |
| 100,000 | **1,00,000** | 100,000 | **ایک لاکھ** |
| 1,000,000 | **10,00,000** | 1,000,000 | **دس لاکھ** |
| 10,000,000 | **1,00,00,000** | 10,000,000 | **ایک کروڑ** |
| 1,234,567 | **12,34,567** | 1,234,567 | بارہ لاکھ چونتیس ہزار پانچ سو سڑسٹھ |

In Urdu script with Urdu numerals:

| Number | Urdu numerals (South Asian grouping) |
|--------|----------------------------------------|
| 100 | ۱۰۰ |
| 1,000 | ۱,۰۰۰ |
| 1,00,000 | **۱,۰۰,۰۰۰** (= ایک لاکھ) |
| 1,00,00,000 | **۱,۰۰,۰۰,۰۰۰** (= ایک کروڑ) |

**Modern Pakistan increasingly uses Western grouping** (1,234,567 instead of 12,34,567), especially in international business and apps. Both conventions coexist. **For pure Urdu publications and formal Pakistani UI: use South Asian.** For international/tech contexts: Western is acceptable.

| Format | Urdu convention | Example |
|--------|------------------|---------|
| Thousands separator | `,` (Latin comma in number context — NOT Urdu ، which is sentence comma) | 1,234 or ۱,۲۳۴ |
| Decimal separator | `.` (period) | 1,234.56 |
| Negative | `-25` (minus before) | -25 / -۲۵ |
| Percentage | `25%` (after number) | ۲۵٪ |
| Phone numbers | (Pakistan) +92 3xx xxxxxxx | +92 300 1234567 |

### Dates — Gregorian with adapted month names

Urdu uses the **Gregorian calendar** as the everyday/civil calendar. The **Islamic Hijri (lunar) calendar** is used for religious dates. Pakistan does not use the Solar Hijri Jalali calendar (that's Iran/Afghanistan).

**Urdu month names — adapted from English/Persian:**

| # | Urdu | Pronunciation | Gregorian |
|---|------|---------------|-----------|
| 1 | **جنوری** | Janvarī | January |
| 2 | **فروری** | Farvarī | February |
| 3 | **مارچ** | Mārch | March |
| 4 | **اپریل** | Aprail | April |
| 5 | **مئی** | Maī | May |
| 6 | **جون** | Jūn | June |
| 7 | **جولائی** | Jūlāī | July |
| 8 | **اگست** | Agast | August |
| 9 | **ستمبر** | Sitambar | September |
| 10 | **اکتوبر** | Aktūbar | October |
| 11 | **نومبر** | Navambar | November |
| 12 | **دسمبر** | Disambar | December |

**Date formats:**

| Format | Example | When to use |
|--------|---------|-------------|
| DD/MM/YYYY | 15/01/2024 or ۱۵/۰۱/۲۰۲۴ | Pakistan/India default |
| DD-MM-YYYY | 15-01-2024 | Government forms |
| DD month-name YYYY | 15 جنوری 2024 / ۱۵ جنوری ۲۰۲۴ | Long form, formal/news |
| YYYY-MM-DD (ISO) | 2024-01-15 | Technical / API contexts only |
| Hijri lunar (قمری/ہجری) | 3 رجب 1445 ھ | Religious contexts, holidays (Ramadan, Eid, Muharram) |

**Hijri month names (Islamic calendar):**

محرم، صفر، ربیع الاول، ربیع الثانی، جمادی الاول، جمادی الثانی، رجب، شعبان، رمضان، شوال، ذی القعدہ، ذی الحجہ

**Calendar disambiguation suffixes:**

- **ء** (eesvī / Christian-era) — e.g., 2024ء (rare but seen in formal texts)
- **ھ** (Hijri lunar) — e.g., 1445ھ (used in religious dates)

**For UI:** Gregorian Urdu month names are standard. If your product uses Hijri dates for religious features (prayer times, Ramadan countdown), mark them explicitly.

### Days of week — Pakistan starts Monday (international standard)

Pakistan officially follows the **Monday-start week** (ISO 8601). Sunday is the weekend day, plus Friday (جمعہ) which is the Islamic holy day with shortened working hours.

| English | Urdu (standard) | Alternative | Notes |
|---------|-----------------|-------------|-------|
| Monday | **پیر** | سوموار (less common in Pakistan, more in India) | Workday; "pīr" means elder/Monday |
| Tuesday | **منگل** | (none) | Workday |
| Wednesday | **بدھ** | (none) | Workday |
| Thursday | **جمعرات** | (none) | Workday |
| Friday | **جمعہ** | (none) | Islamic holy day; shortened work / prayer break |
| Saturday | **ہفتہ** | سنیچر (urban Pakistani slang) | Workday (Pakistan, depending on sector); weekend in many private firms |
| Sunday | **اتوار** | (none) | Weekend day |

**Pakistani work week conventions:**

- **Government / banks:** Mon–Fri (full days) with Friday prayer break; Sat+Sun weekend in some sectors; Mon–Sat with Sun off in others.
- **Private sector:** Typically Mon–Fri 5-day, or Mon–Sat 6-day. Sun is always off; Fri prayer break universal.
- **Religious / traditional / rural:** Friday and Sunday both treated as half/full holidays.

**Indian Urdu UI:** Sun only as weekend; Mon–Sat workweek (with Sat half-day in many sectors).

### Time

| Format | Example | Use case |
|--------|---------|----------|
| 24-hour | 14:30 / ۱۴:۳۰ | Default, technical, international |
| 12-hour | 2:30 شام / 2:30 PM | Casual / verbal-spoken |

**Time-of-day periods (used colloquially with 12-hour time):**

- صبح (subah) — morning, ~5 AM to ~11 AM
- دوپہر (dopahar) — noon/midday, ~12 PM to ~3 PM
- سہ پہر (sih-pahar) — mid-afternoon
- شام (shām) — evening, ~4 PM to ~7 PM
- رات (rāt) — night, after sunset

Example: "صبح 10:30" or "شام 5:00 بجے".

### Currency

**Pakistan (ur-PK):**

| Aspect | Pakistani Rupee |
|--------|-----------------|
| Name | روپیہ (singular) / روپے (plural) |
| Symbol | ₨ or Rs. (Latin abbreviation) or PKR (ISO) |
| Subunit | پیسہ (paisā, 1/100 of a rupee — largely demonetized but conceptually used) |
| Example | Rs. 1,234 or ₨1,234 or ۱,۲۳۴ روپے or 1,234 PKR |
| Inflation note | Pakistani rupee has weakened considerably; prices are often in thousands/lakhs |

**Pakistani UI pricing examples:**

- 999 PKR / ماہ
- Rs. 9,999 / ماہ
- ۹,۹۹۹ روپے ماہانہ
- ₨1,500 / سال

**India (ur-IN):**

| Aspect | Indian Rupee |
|--------|--------------|
| Name | روپیہ / روپے (same word; different country) |
| Symbol | ₹ (Unicode U+20B9) or Rs. or INR |
| Subunit | پیسہ (paisā) |
| Example | ₹1,234 or Rs. 1,234 or ۱,۲۳۴ روپے or 1,234 INR |

**Currency placement:** amount + currency name → `1,234 روپے` / `Rs. 1,234` / `۱,۲۳۴ روپے`. Both orders accepted in Urdu UI.

**For international/global products:** USD `$99.99` is acceptable; specify the conversion to PKR/INR if pricing is for South Asian market.

---

## Terminology — Preferred Urdu Terms

### Common UI vocabulary

| English | ✓ Urdu (preferred) | ⚠ Avoid / English-loan alternative |
|---------|---------------------|--------------------------------------|
| user | **صارف** / یوزر | (یوزر widely accepted in casual Pakistani UI) |
| account | **اکاؤنٹ** / کھاتہ | (کھاتہ formal; اکاؤنٹ universal) |
| password | **پاس ورڈ** | (universal English-loan; no native equivalent in common use) |
| email | **ای میل** | (universal) |
| settings | **ترتیبات** / سیٹنگز | (ترتیبات native; سیٹنگز casual) |
| dashboard | **ڈیش بورڈ** | (English-loan, universal) |
| profile | **پروفائل** / تعارف | |
| link | **لنک** / ربط | (لنک casual; ربط formal) |
| browser | **براؤزر** | |
| website | **ویب سائٹ** | |
| folder | **فولڈر** | |
| file | **فائل** | (universal) |
| device | **ڈیوائس** / آلہ | (ڈیوائس tech; آلہ formal native) |
| phone (mobile) | **موبائل** / فون | |
| computer | **کمپیوٹر** / شمارندہ (rare) | |
| application / app | **ایپلی کیشن** / ایپ / درخواست | (درخواست means application-form formally too — ambiguous) |
| update (v.) | **اپ ڈیٹ کریں** / تازہ کریں | |
| save | **محفوظ کریں** | سیو کریں |
| delete | **حذف کریں** | ڈیلیٹ کریں |
| cancel | **منسوخ کریں** | کینسل کریں |
| upload | **اپ لوڈ کریں** | |
| download | **ڈاؤن لوڈ کریں** | |
| sign in / log in | **سائن ان کریں / لاگ ان کریں** | داخل ہوں (poetic) |
| sign out / log out | **سائن آؤٹ کریں / لاگ آؤٹ کریں** | |
| sign up | **سائن اپ کریں / رجسٹر کریں** | اندراج کریں (formal) |
| search | **تلاش کریں** | سرچ کریں |
| click | **کلک کریں** | (universal) |
| share | **شیئر کریں / بانٹیں** | |
| notifications | **اطلاعات / نوٹیفکیشنز** | اعلانات (more formal) |
| privacy | **رازداری / پرائیویسی** | |
| terms (of service) | **شرائط / شرائط استعمال** | |
| support | **سپورٹ / مدد / امداد** | |
| help | **مدد / امداد** | ہیلپ |
| feedback | **تبصرہ / فیڈ بیک / آرا** | |
| menu | **مینیو** / فہرست | |
| home | **ہوم / گھر / مرکزی صفحہ** | |
| copy | **کاپی کریں / نقل کریں** | |
| paste | **پیسٹ کریں / چسپاں کریں** | |
| cut | **کاٹیں / کٹ کریں** | |
| undo | **واپس / انڈو** / منسوخ | |
| redo | **دوبارہ / ری ڈو** | |
| open | **کھولیں** | اوپن کریں |
| close | **بند کریں** | کلوز کریں |
| edit | **ترمیم کریں** / ایڈٹ کریں | |
| view | **دیکھیں / مشاہدہ کریں** | |
| send | **بھیجیں / ارسال کریں** | سینڈ کریں |
| receive | **وصول کریں / حاصل کریں** | |
| invite | **مدعو کریں / دعوت دیں** | |
| follow | **فالو کریں** | |
| like | **لائک کریں / پسند کریں** | |
| comment | **تبصرہ / کامنٹ** | |
| Yes | **ہاں / جی ہاں** | |
| No | **نہیں / جی نہیں** | |
| Continue | **جاری رکھیں** | |
| Next | **اگلا / آگے** | |
| Previous | **پچھلا / واپس** | |
| Done | **مکمل / ہو گیا** | |
| OK | **ٹھیک ہے / تأئید** | اوکے |

### Tech / dev-specific terms

| English | ✓ Urdu | Notes |
|---------|--------|-------|
| build (v., software) | بلڈ / تعمیر | (بلڈ English-loan; تعمیر means "construction") |
| deploy | ڈپلائے / تعینات کرنا | (ڈپلائے English; تعینات formal) |
| pipeline (CI/CD) | pipeline / پائپ لائن | Keep Latin in dev contexts |
| repository / repo | repository / ریپو / مخزن | (ریپو casual; مخزن formal Arabic) |
| branch (git) | branch / شاخ | |
| commit (v., git) | commit / کمٹ / ثبت | (English-loan in dev; ثبت = "record/register") |
| pull request | pull request / PR | Often kept Latin |
| merge | merge / ضم / ملا دینا | |
| API | API | Keep Latin "API" |
| endpoint | endpoint / نقطہ اختتام | |
| token | token / ٹوکن | |
| cache | cache / کیش | |
| log (n.) | log / لاگ | |
| sync | sync / ہم آہنگی | |
| webhook | webhook | Keep Latin |
| backend | backend / بیک اینڈ | |
| frontend | frontend / فرنٹ اینڈ | |
| database | database / ڈیٹا بیس | |
| server | server / سرور | |
| client | client / کلائنٹ | |
| query | query / کوئری / استفسار | |
| index | index / انڈیکس / فہرست | |
| schema | schema / اسکیما | |
| migration | migration / منتقلی | |

### Native vs loanword preference

Urdu tolerates English loanwords more than some languages — Pakistani urban tech-savvy users freely mix English tech terms into Urdu speech and writing. This is more like Indonesian (loan-tolerant) than Icelandic (loan-resistant).

**Rule of thumb:**

- **Common UI actions with established native Urdu** (save → محفوظ کریں, delete → حذف کریں, settings → ترتیبات, search → تلاش کریں, password → پاس ورڈ) → **use the native form**.
- **Universal tech terms without good Urdu equivalents** (email, file, app, link, browser, click) → **use the Urduized loan** (ای میل, فائل, ایپ, لنک, براؤزر, کلک).
- **Developer-specific terms** (API, JSON, Git, deploy, build) → **keep in Latin script** in technical contexts.

**Three registers of Urdu:**

1. **Pure literary Urdu (ادبی اردو):** maximum Persian/Arabic vocabulary, avoids English. Used in newspapers (especially editorials), formal documents, literature. (ترتیبات, نقل, محفوظ, تلاش)
2. **Standard modern Urdu:** mix of native and accepted English-loan tech terms. Default for app UI. (سیٹنگز, کاپی, محفوظ, تلاش)
3. **Casual urban Urdish:** heavy English code-switching. Used in casual chat, social media, urban marketing. (settings, copy, save, search — often English directly)

**For app UI, default to (2) standard modern Urdu.** Switch to (1) for traditional/religious products; (3) only for explicitly casual brands.

### Place names — short forms in UI

| English | UI short form | Long/formal form (avoid in UI) |
|---------|---------------|--------------------------------|
| United States / USA | **امریکا** | ریاستہائے متحدہ امریکا |
| United Kingdom | **برطانیہ** / انگلستان | متحدہ سلطنت |
| Germany | **جرمنی** | جمہوریہ جرمنی |
| France | **فرانس** | جمہوریہ فرانس |
| China | **چین** | عوامی جمہوریہ چین |
| Japan | **جاپان** | (note: NOT ژاپن with ژ — Urdu uses جاپان with regular ج) |
| Russia | **روس** | روسی فیڈریشن |
| Saudi Arabia | **سعودی عرب** | مملکت سعودی عرب |
| UAE / Emirates | **متحدہ عرب امارات / امارات** | |
| Iran | **ایران** | اسلامی جمہوریہ ایران |
| Pakistan | **پاکستان** | اسلامی جمہوریہ پاکستان |
| India | **بھارت / ہندوستان** | جمہوریہ بھارت |
| Afghanistan | **افغانستان** | |
| Bangladesh | **بنگلہ دیش** | |
| Turkey | **ترکی / ترکیہ** | (ترکیہ official since 2022) |

---

## Calque / Anti-Pattern Blocklist

These calques (literal English translations) make Urdu text sound machine-translated. Replace with idiomatic Urdu.

| ✗ Wrong (English calque) | ✓ Correct (idiomatic Urdu) | Why |
|---------------------------|------------------------------|-----|
| سینس بناتا ہے (makes sense) | **سمجھ میں آتا ہے / معقول ہے** | English idiom calque |
| بریک لینا (take a break) | **وقفہ لینا / آرام کرنا** | English calque; Urdu uses وقفہ |
| ٹائم لینا (take time) | **وقت لینا / وقت لگنا** | OK in some contexts; وقت لگنا for "takes time" |
| کیئر لینا (take care) | **خیال رکھنا** | English calque; Urdu uses خیال رکھنا |
| یک تکہ کیک (piece of cake) | **بائیں ہاتھ کا کھیل** | Idiom — use Urdu equivalent |
| ٹانگ توڑو (break a leg) | **کامیابی کی دعا / اللہ کامیاب کرے** | Idiom — translate function, not literal |
| ایک پتھر سے دو پرندے (kill two birds with one stone) | **ایک تیر سے دو شکار** | Urdu native equivalent |
| بڑی تصویر دکھاؤ (paint the big picture) | **مجموعی منظر / تصویر پیش کرنا** | English business calque |
| دن کے آخر میں (at the end of the day) | **بالآخر / آخر کار / در اصل** | English filler calque |
| روزانہ کی بنیاد پر (on a daily basis) | **روزانہ / ہر روز** | Use adverb, not nominal |
| کارکردگی کے لحاظ سے (in terms of performance) | **کارکردگی کے اعتبار سے** | OK; or just simpler "کارکردگی میں" |
| اگر صورت میں اگر (in case if) | **اگر / اس صورت میں کہ** | Redundant double-conjunction |
| تاکہ ہم کر سکیں (in order that we can) | **تاکہ ہم کر سکیں / تاکہ ہم...** | OK; just avoid کے لیے کہ |
| فائل تلاش نہیں ہو سکتی | **فائل نہیں ملی / فائل دستیاب نہیں** | Passive "cannot be found" calque |
| ڈیفالٹ کی قیمت (default value) | **طے شدہ قیمت / پہلے سے طے شدہ** | English calque; use طے شدہ |
| AI سے چلایا گیا (AI-powered) | **AI پر مبنی / مصنوعی ذہانت سے چلنے والا** | "Powered by AI" calque |
| سیاق و سباق سے آگاہ (context-aware) | **سیاق و سباق کو سمجھنے والا / مدنظر رکھنے والا** | "Context-aware" calque |
| صارف دوست (user-friendly) | **استعمال میں آسان / صارف پسند** | "User-friendly" literal calque |
| URLs کا ڈیٹا بیس | **آدرس کا ڈیٹا بیس / URLs کا مجموعہ** | Mixed Urdu-English plural |
| API کا اختتامی نقطہ | **API endpoint / API کا نقطہ اختتام** | Keep API in Latin |
| حذف کا عمل انجام پایا | **حذف ہو گیا / حذف ہوا** | Over-nominalization |
| ریاستہائے متحدہ امریکا | **امریکا** (in UI) | Use short form |
| متحدہ سلطنت | **برطانیہ / انگلستان** | Use short form |
| جام مقدس (holy grail) | **حتمی منزل / بڑی خواہش** | Christian-origin idiom |
| صلیب اٹھانا (cross to bear) | **بھاری ذمہ داری / بار سہنا** | Christian-origin idiom |
| لکڑی پر دستک (knock on wood) | **ان شاء اللہ / اللہ خیر کرے** | Western superstition |
| انگلیاں صلیب نما (fingers crossed) | **ان شاء اللہ / امید ہے** | Western gesture-idiom |

### Hindi vocabulary creeping into Urdu — the BIG ONE

These are the most common Hindi-Urdu mistakes when translators don't distinguish the two languages carefully:

| ✗ Hindi calque (wrong for Urdu UI) | ✓ Urdu correct |
|------------------------------------|------------------|
| کرپیا (kṛipayā) | **براہ کرم** |
| دھنیہ واد / دھنیاواد | **شکریہ** |
| سمسیا | **مسئلہ** |
| شکشا (Hindi शिक्षा) | **تعلیم** |
| سرکار (used as "government" in Hindi sense) | **حکومت** (سرکار in Urdu = "lord/sir") |
| پرشن (Hindi formal "question") | **سوال** |
| اتر (Hindi formal "answer") | **جواب** |
| سماچار (Hindi formal "news") | **خبر / خبریں** |
| اتہاس (Hindi formal "history") | **تاریخ** |
| دیش (Hindi "country") | **ملک** |
| سنسار / وشو (Hindi "world") | **دنیا** |
| ایشور / بھگوان (Hindi "God") | **اللہ** (Islamic) / **خدا** (general; both Muslim/non-Muslim use خدا) |
| وواہ (Hindi "marriage") | **شادی / نکاح** (Islamic marriage = نکاح) |
| پُستک (Hindi formal "book") | **کتاب** |
| سمی (Hindi formal "time") | **وقت** |
| متر (Hindi formal "friend") | **دوست** |
| سہایتا / مدد (Hindi "help") | **مدد** (مدد is shared; سہایتا is Hindi-only) |
| پراری / پراری بھون (Hindi "settings") | **ترتیبات** |
| سچ ایکجن (Hindi "selection") | **انتخاب / منتخب** |

**Detection heuristic:** if a translation contains Sanskrit-derived words like ـیہ, ـت, کرپیا, دھنیہ, پرشن, اتر, سماچار, اتہاس, دیش, سنسار, ایشور, پُستک, سمی, متر, سہایتا — it's probably Hindi vocabulary creeping in. Replace with the Urdu equivalent.

### Passive voice — be sparing

Urdu has a passive (formed with جانا as auxiliary: `بھیجا گیا` = "was sent"). It is grammatically natural for short status messages.

However, **over-using passive in narrative copy** sounds awkward — Urdu prefers active voice with clear subjects when possible.

| ✗ Over-passive | ✓ Active or natural passive |
|----------------|-------------------------------|
| فائل سسٹم کے ذریعے محفوظ کی جاتی ہے۔ | **سسٹم فائل محفوظ کرتا ہے۔** |
| ای میل ہماری طرف سے آپ کو بھیجی گئی ہے۔ | **ہم نے آپ کو ای میل بھیجی ہے۔** |
| یہ عمل آپ کے ذریعے انجام نہیں دیا جا سکتا۔ | **آپ یہ عمل نہیں کر سکتے۔** |

**Short status passives are fine:** `محفوظ ہو گیا` ✓, `بھیج دیا گیا` ✓, `حذف ہو گئی` ✓.

### False friends and tricky vocabulary

| Urdu word | True meaning | Common misuse |
|-----------|--------------|----------------|
| سرکار | "lord, sir" (respectful address) — NOT "government" | Hindi uses सरकार for government; Urdu uses حکومت for government |
| واقعی | "really, truly" | NOT "actually" in factual sense — for that use **در حقیقت / حقیقتاً** |
| حال | "state, condition" | NOT "now/present" — for now use **اب / اس وقت / موجودہ** |
| پرسنل | NOT "personal" — it's English-loan but ambiguous; prefer **ذاتی / نجی** |
| لائبریری | code library OR book library (context-dependent) | Mostly tech contexts in UI |
| آرڈر | "order (commercial)" | NOT "order" in sense of arrangement — use **ترتیب** |
| پارٹی | political party / party (gathering) / contractual party | Multiple meanings; use **فریق** for legal contractual party |

---

## Self-Check Checklist

Run this before returning Urdu output. Items marked **(critical)** are auto-fail.

### Identity & script (critical)

- [ ] **(critical)** Output is in Perso-Arabic script, NOT Devanagari. (No हिन्दी characters.)
- [ ] **(critical)** No Hindi vocabulary creeping in: no کرپیا, دھنیہ واد, سمسیا, شکشا, پرشن — replaced with براہ کرم, شکریہ, مسئلہ, تعلیم, سوال.
- [ ] **(critical)** Urdu-specific letters used wherever needed: retroflex ٹ ڈ ڑ, nasalization ں, aspirated ھ, baṛī ye ے.
- [ ] **(critical)** Aspirated consonants use do-cashmi ھ (U+06BE) NOT regular ہ (U+06C1): کھانا (correct) NOT کہانا (wrong if meaning "to eat").
- [ ] Persian extra letters پ چ ژ گ used where Persian/Indo-Aryan word requires (پاکستان, چاند, ژالہ, گھر).
- [ ] Final ـے (baṛī ye) used in word-final /e:/ positions: ہے, کرے, میرے — not ـی.
- [ ] No Arabic-style grammar imported (no Arabic feminine adjective forms, no dual, no zero/two/few/many plural categories).

### Honorific register (critical)

- [ ] **(critical)** Consistent آپ-form throughout file (no mixing with تم-form or تو-form).
- [ ] All imperatives use کریں or کیجیے (not کرو from تم or کر from تو).
- [ ] Possessives use آپ کا/کی/کے (not تمہارا/تمہاری/تمہارے).
- [ ] براہ کرم used appropriately for "please" — at most once per dialog, not in every button.

### Grammar — gender, number, case (critical)

- [ ] **(critical)** Adjective gender agreement: نئی فائل (fem), نیا سسٹم (masc), نئی فائلیں (fem pl).
- [ ] **(critical)** Genitive کا/کی/کے agrees with POSSESSED noun: فولڈر کی فائل (فائل is fem), فائل کا نام (نام is masc).
- [ ] **(critical)** Ergative نے used with perfective transitive: میں نے فائل دیکھی (not میں فائل دیکھی).
- [ ] **(critical)** Verb in perfective transitive agrees with OBJECT gender: میں نے فائل حذف کی (fem), میں نے پیغام حذف کیا (masc).
- [ ] **(critical)** With کو-marked object, verb defaults to masc sg: اس نے فائل کو حذف کیا (not کی).
- [ ] No نے on intransitive verbs: میں گیا (not میں نے گیا).
- [ ] No نے on non-perfective: میں فائل دیکھتا ہوں (not میں نے فائل دیکھتا ہوں).
- [ ] Oblique case before postpositions: بڑے سسٹم میں, نئے بٹن پر, فائلوں میں.

### Word order (critical)

- [ ] **(critical)** SOV word order — verb at end of clause, not English SVO calque.
- [ ] Postpositions FOLLOW noun (میں فولڈر ✗ → فولڈر میں ✓).
- [ ] Adjectives PRECEDE noun (Urdu order — opposite of Arabic): نئی فائل ✓ not فائل نئی ✗.
- [ ] Verb complex (main + aux + modal) at end together.

### Compound verbs

- [ ] Tech verbs use complete compound: کلک کریں ✓ (not just کلک ✗); محفوظ کریں ✓ (not just محفوظ ✗).
- [ ] کرنا/کریں added to noun for borrowed-verb pattern.
- [ ] Native verbs conjugate directly without کرنا: کھولیں, پڑھیں, دیکھیں, بھیجیں.

### Punctuation

- [ ] **Urdu full stop ۔ (U+06D4)** at end of Urdu sentences, NOT Latin period.
- [ ] Question marks are `؟` (U+061F), not `?`.
- [ ] Commas are `،` (U+060C), not `,`, in Urdu text.
- [ ] Semicolons are `؛` (U+061B), not `;`, in Urdu text.
- [ ] No comma before اور (and) or یا (or) in standard lists.
- [ ] Comma DOES appear before کہ, اگر, کیونکہ, جب.
- [ ] No space before ؟ ، ؛ : ! ۔.
- [ ] Quotations use `"..."` or `«...»` consistently.

### Numbers, dates, currency

- [ ] Numerals consistent within string (all Urdu/Persian ۰-۹ U+06F0–U+06F9, or all Western 0-9 — never mixed).
- [ ] If using extended-Arabic numerals, they are Persian/Urdu code points (U+06F0+), NOT Arabic-Indic (U+0660+).
- [ ] Number grouping uses South Asian lakh/crore (۱,۲۳,۴۵۶) for traditional Pakistani UI, or Western (1,234,567) for modern/international.
- [ ] Dates use Gregorian Urdu month names (جنوری, فروری, مارچ…) — NOT Persian/Iranian Jalali (فروردین, اردیبہشت).
- [ ] Hijri (Islamic lunar) dates used only for religious contexts and explicitly marked with ھ.
- [ ] Currency: ₨/Rs./روپے for Pakistan (PKR); ₹/روپے for India (INR).
- [ ] Day-of-week names: پیر/منگل/بدھ/جمعرات/جمعہ/ہفتہ/اتوار.

### Bidirectional / Latin embedding

- [ ] Latin tech identifiers (Git, API, JSON, URLs, file names, brand names) preserved in Latin script.
- [ ] No accidental transliteration of code identifiers (don't write ای پی آئی for API).
- [ ] Bidi rendering not broken by missing LRM/RLM (test mixed Latin-Urdu sentences visually).

### Naturalness

- [ ] No English calques (`بریک لینا`, `روزانہ کی بنیاد پر`, `سینس بناتا ہے`, `یک تکہ کیک`).
- [ ] No transliteration when native Urdu exists (`سیو کریں` → `محفوظ کریں`; `ڈیلیٹ کریں` → `حذف کریں`).
- [ ] Buttons use آپ-form imperative (`محفوظ کریں`, `حذف کریں`) — not informal تم/تو-form.
- [ ] Status messages use `ہو رہا ہے` for loading/progressive, `ہو گیا/گئی` for completion (with gender agreement).
- [ ] Error messages include both what-happened AND next-step.
- [ ] Drag-drop uses native verbs (`کھینچیں` + `چھوڑیں`), not transliterations.
- [ ] `X سے زیادہ` instead of `X+` or `+X`.
- [ ] فی for rate (per unit), کے لیے for total (for N units) — never confused.
- [ ] Empty states use `کوئی [noun] نہیں` pattern.

### Religious/cultural sensitivity

- [ ] No Christian-origin idioms literally translated (no `جام مقدس`, `صلیب اٹھانا`, `لکڑی پر دستک`).
- [ ] No religious phrases injected unless source invokes them (no spontaneous `ان شاء اللہ` in neutral UI).
- [ ] No pork/alcohol/gambling metaphors unless they are the literal subject.
- [ ] Place names use UI short forms (`امریکا`, `برطانیہ`, `بھارت/ہندوستان`).
- [ ] Indian Urdu (ur-IN) framing kept secular if audience includes non-Muslim Urdu speakers.
- [ ] Pakistan-specific political/religious references not pushed onto Indian Urdu audience.

### Nastaliq script (recommendation, not a strict checklist gate)

- [ ] If specifying fonts/CSS for production: Nastaliq fonts (Jameel Noori Nastaleeq, Noto Nastaliq Urdu) preferred over Arabic Naskh.
- [ ] Text-direction set to RTL (`dir="rtl"` or `dir="auto"`).

---

## Worked Examples

### Example 1 — Standard formal UI (default register)

**Source (English):**

> Welcome back! You have 3 new messages in your inbox. Click **Continue** to read them, or **Cancel** to stay here. Saving your changes…

**Auto-detect register:** Standard product UI, neutral lexicon → **آپ formal**.

**Translation (ur-PK, آپ-form, default):**

> خوش آمدید! آپ کے انباکس میں 3 نئے پیغامات ہیں۔ انہیں پڑھنے کے لیے **جاری رکھیں** پر کلک کریں، یا یہاں رکنے کے لیے **منسوخ کریں** کا انتخاب کریں۔ آپ کی تبدیلیاں محفوظ ہو رہی ہیں…

**Why this works:**

- `خوش آمدید` — formal welcome.
- `آپ کے انباکس میں` — possessive کے (oblique masc — انباکس is masculine and follows postposition میں).
- `3 نئے پیغامات` — number followed by plural noun (Urdu DOES pluralize, unlike Persian). نئے is masc plural agreeing with پیغامات.
- `انہیں پڑھنے کے لیے` — "to read them" — کے لیے = "for/in order to".
- Buttons in imperative آپ-form: `جاری رکھیں`, `منسوخ کریں`.
- `پر کلک کریں` — SOV (verb کریں at end). پر = "on" postposition.
- Status: `محفوظ ہو رہی ہیں` — progressive form. ہو رہی ہیں because subject `تبدیلیاں` is feminine plural.
- Punctuation: Urdu `،` not `,`. Urdu full stop ۔ at end. Ellipsis `…`.
- Aspirated and retroflex letters used correctly throughout (نئے, تبدیلیاں).

### Example 2 — ICU plural

**Source:**

```icu
You have {count, plural, one {# new message} other {# new messages}}.
```

**Urdu translation:**

```icu
آپ کے پاس {count, plural,
  one {# نیا پیغام}
  other {# نئے پیغامات}
} ہیں۔
```

**Why:**

- Only `one` and `other` (Urdu needs only 2 CLDR categories).
- **`one`** uses singular noun + singular adjective: نیا پیغام (masc sg).
- **`other`** uses plural noun + plural adjective: نئے پیغامات (masc pl).
- پیغام is masculine; adjective نیا → نئے in plural.
- SOV: copula ہیں at end.
- (Note: a more polished version would handle count=0 separately with a کوئی پیغامات نہیں ہیں phrasing.)

### Example 3 — Error message with next-step

**Source:**

> File not found. Please check the path and try again.

**Urdu translation:**

> فائل نہیں ملی۔ براہ کرم راستہ چیک کریں اور دوبارہ کوشش کریں۔

**Why:**

- `فائل نہیں ملی` — feminine subject فائل + feminine past verb ملی.
- Two-part structure: what happened (`فائل نہیں ملی`) + what to do (`راستہ چیک کریں اور دوبارہ کوشش کریں`).
- `براہ کرم` once at start (politeness marker — Urdu native, NOT Hindi کرپیا).
- SOV: verbs `چیک کریں`, `کوشش کریں` at end.
- `اور` connecting clauses (no comma before اور).
- `دوبارہ` (again) before the verb.
- Urdu full stop ۔ at end (NOT Latin period).

### Example 4 — Marketing copy with Latin tech terms

**Source:**

> Built with Next.js and TypeScript. Deploy to AWS in seconds. Connect to GitHub, GitLab, or Bitbucket.

**Urdu translation:**

> Next.js اور TypeScript کے ساتھ بنایا گیا۔ سیکنڈز میں AWS پر deploy کریں۔ GitHub، GitLab، یا Bitbucket سے منسلک ہوں۔

**Why:**

- All tech brand names (Next.js, TypeScript, AWS, GitHub, GitLab, Bitbucket) stay in Latin script — bidi handles rendering.
- `deploy` kept in Latin (acceptable in Pakistani dev UI; alternative: تعینات کریں).
- `بنایا گیا` — passive completion (masc default subject "it was built").
- `سیکنڈز میں AWS پر deploy کریں` — SOV. روی AWS پر = "on AWS".
- `سے منسلک ہوں` — "connect to" using منسلک + ہونا. SOV with verb ہوں at end.
- Comma `،` between list items (Urdu comma, not Latin `,`).
- No comma before `یا` (or).
- Urdu full stop ۔ at end of each sentence.

### Example 5 — Date displayed in Pakistani context

**Source:** Last login: January 15, 2024 at 2:30 PM

**Urdu (ur-PK):**

> آخری سائن ان: 15 جنوری 2024، دوپہر 2:30 بجے

OR using Urdu numerals:

> آخری سائن ان: ۱۵ جنوری ۲۰۲۴، دوپہر ۲:۳۰ بجے

**Why:**

- `آخری سائن ان` — "last sign-in" (سائن ان is the borrowed compound noun, treated as a unit).
- Gregorian date with Urdu month name: `15 جنوری 2024`.
- Time-of-day: `دوپہر` (noon/afternoon) + 12-hour time + `بجے` ("o'clock").
- Urdu comma `،` separates date and time.
- Western numerals 15/2024/2:30 are standard for modern Pakistani UI; Urdu numerals ۱۵/۲۰۲۴/۲:۳۰ for traditional style.

**Urdu (ur-IN) — Indian context:**

> آخری لاگ ان: 15 جنوری 2024، دوپہر 2:30 بجے

(Same form; only difference is currency context if pricing is mentioned.)

### Example 6 — Pricing with Pakistani currency

**Source:**

> Pro plan: $9.99 per month, billed annually. Includes 100GB storage and unlimited users.

**Urdu translation (ur-PK, Pakistani market with PKR):**

> پرو پلان: 2,800 روپے فی ماہ، سالانہ بل۔ 100GB اسٹوریج اور لامحدود صارفین شامل ہیں۔

**Why:**

- Pricing converted to PKR (illustrative ≈ 2,800 PKR for $9.99 — actual exchange rate varies).
- `پرو پلان` — Pro plan (English-loan in Pakistani UI; alternative: پیشہ ورانہ پلان more formal).
- `فی ماہ` for "per month" — Urdu native rate expression.
- `سالانہ بل` — "annual billing".
- `شامل ہیں` — "are included" — copula at end (plural ہیں because subject is plural: اسٹوریج اور صارفین).
- `لامحدود صارفین` — "unlimited users" — adjective before noun, both Persian/Arabic-derived.
- `100GB` kept in Latin (universal tech notation).
- No comma before اور (and).
- Urdu full stop ۔ at end.

**For ur-IN (Indian market with INR):**

> پرو پلان: ₹830 فی ماہ، سالانہ بل۔ 100GB اسٹوریج اور لامحدود صارفین شامل ہیں۔

(Same text; only currency symbol/amount differs.)

### Example 7 — Sign-up form with validation

**Source form:**

```
Sign up
Email: [your@email.com]
Password: [at least 8 characters]
[I agree to the Terms of Service]
[Create account] [Cancel]

Errors:
- This field is required.
- Invalid email format.
- Password must be at least 8 characters.
```

**Urdu translation:**

```
سائن اپ کریں
ای میل: [your@email.com]
پاس ورڈ: [کم از کم 8 حروف]
[میں شرائط استعمال سے متفق ہوں]
[اکاؤنٹ بنائیں] [منسوخ کریں]

غلطیاں:
- یہ فیلڈ لازمی ہے۔
- ای میل کا فارمیٹ درست نہیں۔
- پاس ورڈ کم از کم 8 حروف کا ہونا چاہیے۔
```

**Why:**

- `سائن اپ کریں` — compound verb (English-loan + کریں).
- Email placeholder stays in Latin (`your@email.com`).
- Form labels are nouns (`ای میل`, `پاس ورڈ`).
- Checkbox label uses آپ-form-internal 1st-person: `میں ... متفق ہوں` (I agree).
- Buttons are formal imperatives: `اکاؤنٹ بنائیں`, `منسوخ کریں`.
- Errors: noun + copula ہے pattern. `یہ فیلڈ لازمی ہے` — SOV with copula at end.
- `ای میل کا فارمیٹ` — genitive کا (فارمیٹ is masc).
- `پاس ورڈ ... ہونا چاہیے` — modal construction (subjunctive with چاہیے) at end.

### Example 8 — Status messages with gender agreement

**Source (statuses for various subjects):**

```
Saving... → ✓ Saved
Sending email... → ✓ Email sent
Uploading file... → ✓ File uploaded
Creating account... → ✓ Account created
Deleting message... → ✓ Message deleted
```

**Urdu translation (with gender agreement):**

```
محفوظ ہو رہا ہے... → محفوظ ہو گیا۔
ای میل بھیجی جا رہی ہے... → ای میل بھیج دی گئی۔
فائل اپ لوڈ ہو رہی ہے... → فائل اپ لوڈ ہو گئی۔
اکاؤنٹ بن رہا ہے... → اکاؤنٹ بن گیا۔
پیغام حذف ہو رہا ہے... → پیغام حذف ہو گیا۔
```

**Why — gender agreement on every verb:**

- `محفوظ ہو رہا ہے` / `محفوظ ہو گیا` — masc default (subject implicit "the operation").
- `ای میل بھیجی جا رہی ہے` / `بھیج دی گئی` — ای میل is **feminine**, so رہی / دی / گئی all in feminine form.
- `فائل اپ لوڈ ہو رہی ہے` / `ہو گئی` — فائل is **feminine** → رہی / گئی.
- `اکاؤنٹ بن رہا ہے` / `بن گیا` — اکاؤنٹ is **masculine** → رہا / گیا.
- `پیغام حذف ہو رہا ہے` / `ہو گیا` — پیغام is **masculine** → رہا / گیا.

**This is the single most common source of Urdu UI errors** — using one fixed gender pattern instead of agreeing with each subject noun. Every status message must be reviewed for gender match.

### Example 9 — Numbers with Indian-style grouping and Urdu numerals

**Source:** Total revenue: $1,234,567

**Urdu (Pakistani context, traditional Urdu numerals + South Asian grouping):**

> کل آمدنی: ۱۲,۳۴,۵۶۷ روپے

(That reads "twelve lakh thirty-four thousand five hundred sixty-seven rupees" with South Asian grouping.)

**Urdu (modern Pakistani UI with Western numerals + Western grouping):**

> کل آمدنی: 1,234,567 روپے

(Both are acceptable; pick one and stay consistent.)

**Spoken form:** بارہ لاکھ چونتیس ہزار پانچ سو سڑسٹھ روپے

### Example 10 — Religious-sensitive UI (Pakistan vs India)

**Source:** "May your day be blessed."

**Urdu (ur-PK, Pakistan — Muslim-default ambient):**

> آپ کا دن مبارک ہو۔

OR more religious:

> اللہ آپ کا دن خیر و برکت سے بھرے۔

**Urdu (ur-IN, India — Muslim minority + cross-community):**

> آپ کا دن خوشگوار ہو۔

(Avoids overtly Islamic framing for cross-community Indian Urdu audience; alternative: مبارک is shared enough that it's also fine in India.)

**Source:** "Happy holidays!"

**Urdu (ur-PK during Eid season):**

> عید مبارک! (during Eid specifically)
> 
> Or generic: تہوار مبارک!

**Urdu (ur-IN, generic):**

> آپ کو چھٹیاں مبارک!

(چھٹی = holiday/leave; شب of festival = specific religious holiday)

---

## When in Doubt

1. **Default to آپ-form formal register, Western 0-9 digits, Gregorian Urdu month names, Pakistani currency (PKR).** This is the safe pan-ur-PK setting.

2. **If unsure about variant (ur-PK vs ur-IN)** → ask once; default to ur-PK.

3. **If you see Hindi vocabulary creeping in** (کرپیا, دھنیہ واد, سمسیا, شکشا, پرشن, سرکار-meaning-government) → replace with Urdu equivalent (براہ کرم, شکریہ, مسئلہ, تعلیم, سوال, حکومت).

4. **If you see Latin period `.` ending an Urdu sentence** → replace with Urdu full stop `۔` (U+06D4). This is the single most visible "low-quality Urdu" indicator.

5. **If an English idiom doesn't have a clear Urdu equivalent** → translate the **function**, not the literal words. Don't import the metaphor (especially Christian-origin idioms).

6. **If you're tempted to import Arabic grammar** (Arabic feminine adjective agreement, dual number, six-category plurals, VSO order) → STOP. Urdu is Indo-Aryan with SOV order, 2-gender system (m/f), ergative نے, and only one+other CLDR plurals.

7. **If you're tempted to import Hindi/Sanskrit vocabulary** at formal register → STOP. Urdu formal register uses Persian/Arabic derivations (تعلیم, حکومت, مسئلہ, شکریہ), not Sanskritic (शिक्षा, सरकार, समस्या, धन्यवाद).

8. **If a tech term has no clean Urdu equivalent** → keep it in Latin script (Git, API, JSON, React) rather than awkwardly transliterate. Pakistani urban tech UI tolerates this freely.

9. **If unsure about religious/cultural framing** → choose the neutral, secular option that respects Islamic values without alienating non-Muslim Urdu speakers (especially in India context).

10. **If the source mixes registers** → pick the higher register (آپ-form) and apply it consistently.

11. **If a placeholder `{variable}` appears in source** → preserve it byte-for-byte. Do not translate `{count}`, `{name}`, `{file}`. The interpolated value will arrive in Urdu (or as user data) at runtime.

12. **If gender of a placeholder noun is unknown** → restructure to avoid agreement ambiguity. Use passive voice (`{file} حذف ہو گیا` defaults to masc) or rephrase to avoid the agreement.

13. **If the source has Arabic-style six-category ICU plurals** → collapse to Urdu `one` + `other`, with singular noun in one branch and plural noun in other branch.

14. **If unsure whether to use ٹ vs ت or ڈ vs د or ڑ vs ر** → these are retroflex vs dental contrasts native to Urdu. Look up the word. Urdu speakers can hear the difference; using the wrong one is a misspelling.

15. **If unsure whether to use ھ (do-cashmi he) vs ہ (regular he)** → aspirated consonants (kh, gh, ch, th, ṭh, dh, ḍh, ph, bh) use ھ. Look at adjacent consonant: کھ گھ چھ تھ ٹھ دھ ڈھ پھ بھ all use ھ.

16. **If unsure about ـی vs ـے at word end** → ـے (baṛī ye) for /e:/ sounds at end (ہے, کرے, میرے, چائے); ـی for /i:/ sounds (کتابی, پاکستانی, اچھی).

Urdu is one of the world's great literary languages, with three centuries of continuous high-register tradition from the Mughal court to modern Pakistani journalism and Indian Urdu literature. It is the language of Ghalib, Iqbal, Faiz Ahmed Faiz, and Mir Taqi Mir. Modern Urdu UI should feel **clear, polite, and natively Urdu** — not like translated Hindi (different vocabulary, different script), not like translated Arabic (different grammar), not like translated Persian (different gender system, different ergative, different aspiration). When you get the script right (پ چ ژ گ ٹ ڈ ڑ ں ھ ے), the word order right (SOV with postpositions), the gender agreement right (m/f on every adjective and verb), the ergative right (نے with perfective transitive, verb agrees with object), the register right (آپ formal), and the cultural framing right (Islamic-respectful without imposing on Indian non-Muslim Urdu audiences), the translation will read naturally to an Urdu speaker — whether in Karachi, Lahore, Delhi, Hyderabad, or the worldwide Urdu diaspora.
