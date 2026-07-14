---
name: localize-hi
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Hindi (हिन्दी) for India. Hindi is an Indo-Aryan language written in Devanagari (देवनागरी) — NOT Latin, NOT Urdu/Nastaliq (though Hindi and Urdu are mutually intelligible when spoken, the scripts differ). Critical features: SOV word order (Subject-Object-Verb — verb ALWAYS at the END: यूज़र फ़ाइल सेव करता है, NOT यूज़र सेव करता है फ़ाइल); 2-gender system (masculine/feminine — फ़ाइल is masc, वेबसाइट is fem, सेटिंग्स is fem); THREE politeness levels with आप as the universal UI default (आप formal, तुम informal, तू intimate — NEVER use तू or तुम in software UI); ergative ने construction in perfective transitive (मैंने फ़ाइल सेव की — verb agrees with OBJECT not subject); postpositions following nouns (में, पर, को, से, का/के/की, के लिए) which require oblique case on the preceding noun (लड़का → लड़के को); compound verbs noun+करना (क्लिक करना, सेव करना, डाउनलोड करना — THE standard tech verb pattern); INDIAN number grouping with lakhs/crores (₹1,23,456.78 — groups of 2 after first 3, NEVER Western ₹123,456.78); nukta dots for borrowed sounds (फ़ for f, ज़ for z, ड़ for ɽ); का/के/की agreement with the POSSESSED noun (NOT the possessor); tech-loanword-friendly (फ़ाइल, क्लिक, डाउनलोड preferred over Sanskritic संचिका, चटकाएँ); DD/MM/YYYY dates; ₹ Rupee with Indian grouping; कृपया (please) for polite requests."
---

# Localize: Hindi (hi → हिन्दी)

You are translating source text into Hindi for India. This skill captures grammar, register, UI conventions, formatting, and Hindi-specific failure modes derived from a production translation prompt.

## Scope & Variants

**One standard:**
- **hi-IN** — Modern Standard Hindi (मानक हिन्दी) as used in India. The official language of the Government of India (alongside English).

**Native name:** हिन्दी (the language); हिन्दी में (in Hindi).

**Identity guardrail:**
- Hindi is **Indo-Aryan** (Indo-European family), descended from Sanskrit via Prakrit and Apabhraṃśa. NOT Dravidian (Tamil, Telugu, Kannada, Malayalam are unrelated southern languages).
- Hindi is written in **Devanagari** (देवनागरी). It is NOT written in Latin script for formal/UI contexts (Hinglish transliteration is for chat only).
- **Hindi vs Urdu:** Spoken Hindi and Urdu are largely the same language (Hindustani) but:
  - Hindi uses Devanagari script and prefers Sanskritic vocabulary in formal contexts
  - Urdu uses Nastaliq (Perso-Arabic) script and prefers Perso-Arabic vocabulary
  - This skill is for Hindi (Devanagari). For Urdu, use a separate ur skill.
- Hindi tolerates **English loanwords in tech contexts more than purist Hindi-नवलेखन (neo-script) would prefer**. Modern tech Hindi uses फ़ाइल, क्लिक, डाउनलोड freely — NOT obscure Sanskritic terms like संचिका or चटकाएँ.

## Register

**Default level: FORMAL (आप-form)** for ALL software UI. This is non-negotiable.

Hindi has THREE politeness levels:

| Level | Pronoun | Verb form | Use case |
|---|---|---|---|
| **Formal (आप)** | आप | करें / करते हैं / करिए / कीजिए | **ALWAYS USE FOR SOFTWARE** |
| Informal (तुम) | तुम | करो / करते हो | Familiar peer; casual apps; rarely for UI |
| Intimate (तू) | तू | कर / करता है | Family, close friends, deity prayers; **NEVER in software** (sounds disrespectful) |

**Examples:**
- ❌ "तुम यहाँ क्लिक करो" (informal) → ✅ "**कृपया यहाँ क्लिक करें**" (formal with कृपया = "please")
- ❌ "तू यहाँ क्लिक कर" (intimate) → ✅ "**कृपया यहाँ क्लिक करें**"
- ❌ "अपना फ़ाइल खोलो" → ✅ "**अपनी फ़ाइल खोलें**" (use formal imperative)

**`कृपया`** ("please") is the universal polite request marker — use liberally in instructions:
- "कृपया प्रतीक्षा करें" (Please wait)
- "कृपया विवरण भरें" (Please fill in details)

**Within a file, ONE register only.** Mixing आप and तुम imperatives is severity 2.0.

## Critical Hard Rules

### SOV Word Order (severity 2.0)

**Hindi is strictly SOV (Subject-Object-Verb) — the verb is ALWAYS at the END.**

| Wrong (English-style SVO) | Correct (Hindi SOV) | English |
|---|---|---|
| यूज़र **सेव करता है** फ़ाइल | यूज़र फ़ाइल **सेव करता है** | User saves the file |
| मैं **खोलता हूँ** दरवाज़ा | मैं दरवाज़ा **खोलता हूँ** | I open the door |
| हम **देखते हैं** टीवी | हम टीवी **देखते हैं** | We watch TV |
| **में फ़ोल्डर** | **फ़ोल्डर में** | in the folder |

Even with question words, the verb goes last:
- "आप क्या **करते हैं**?" (What do you do?) — कर "do" is at end
- "फ़ाइल कहाँ **है**?" (Where is the file?) — है "is" at end

### Two-Gender Agreement (severity 2.0)

**Hindi has 2 grammatical genders** — every noun is either masculine (पुल्लिंग) or feminine (स्त्रीलिंग). There is no neuter.

**Common tech-term genders (MEMORIZE):**

| Masculine (पुल्लिंग) | Feminine (स्त्रीलिंग) |
|---|---|
| फ़ाइल (file) | वेबसाइट (website) |
| सिस्टम (system) | सेटिंग्स (settings) |
| सर्वर (server) | ईमेल (email) |
| फ़ोल्डर (folder) | एप्लिकेशन (application) |
| बटन (button) | जानकारी (information) |
| डेटा (data) | भाषा (language) |
| पासवर्ड (password) | किताब (book) |
| कंप्यूटर (computer) | खिड़की (window — in UI: window) |
| कोड (code) | तस्वीर (picture) |
| यूज़र (user — though often gender-neutral) | सूचना (notification) |

**Adjective agreement (-ा / -ी / -े endings):**

| Form | Masc sg | Masc pl | Fem sg/pl |
|---|---|---|---|
| Direct | **-ा** (नया) | **-े** (नए) | **-ी** (नई) |
| Oblique (before postposition) | **-े** (नए) | **-े** (नए) | **-ी** (नई) |

Examples:
- **नई फ़ाइल** (correct: fem sg + fem adj) ❌ **नया फ़ाइल** (masc adj + fem noun — wait, actually फ़ाइल IS masc, so correct is **नया फ़ाइल**)
- Wait — `फ़ाइल` is officially masculine in standard Hindi tech vocabulary. So:
  - ✅ **नया फ़ाइल** (masc sg) → **नए फ़ाइल** (masc pl is same as oblique)
  - But many speakers naturally say **नई फ़ाइल** (treating it as feminine) — this is a common gender-uncertainty case. Standard tech Hindi uses masculine.
- ✅ **नई वेबसाइट** (fem sg + fem adj)
- ✅ **अच्छी सेटिंग** (fem sg + fem adj)
- ❌ अच्छा सेटिंग → ✅ **अच्छी सेटिंग** (सेटिंग is fem)
- ❌ नया वेबसाइट → ✅ **नई वेबसाइट** (वेबसाइट is fem)

**Adjectives ending in consonants** (e.g., खूबसूरत, सुंदर, important, अच्छा-not-but-something-else): do NOT decline. They stay the same regardless of gender/number.

### Postpositions + Oblique Case (severity 1.5)

**Hindi postpositions follow the noun** (NOT prepositions before). The noun changes to **oblique case** before any postposition.

**Common postpositions:**

| Postposition | Meaning | Example |
|---|---|---|
| **में** | in | फ़ोल्डर **में** (in the folder) |
| **पर** | on | टेबल **पर** (on the table) |
| **को** | to / accusative marker | यूज़र **को** (to the user) |
| **से** | from / with / by | सर्वर **से** (from the server) |
| **का / के / की** | of (possessive) | यूज़र **का** अकाउंट (user's account) |
| **के लिए** | for | आप **के लिए** (for you) |
| **के बारे में** | about | इस **के बारे में** (about this) |
| **तक** | until / up to | अब **तक** (until now) |
| **के पास** | near / has | मेरे **के पास** (I have) |
| **के साथ** | with | टीम **के साथ** (with the team) |

**Oblique case formation:**

| Direct form | Oblique form | Trigger |
|---|---|---|
| लड़का (boy) | लड़**के** को | masc -ा → -े before postposition |
| लड़के (boys) | लड़**कों** को | masc pl direct → -ों oblique pl |
| लड़की (girl) | लड़की को | fem -ी → no change |
| लड़कियाँ (girls) | लड़कि**यों** को | fem pl → -ियों |
| फ़ाइल | फ़ाइल में | masc consonant ending → no change |
| फ़ाइलें | फ़ाइलों में | masc pl with -ें → -ों |

- ❌ "लड़का को बुलाओ" → ✅ "**लड़के** को बुलाओ"
- ❌ "में फ़ोल्डर" → ✅ "**फ़ोल्डर में**" (postposition follows)
- ❌ "नया फ़ोल्डर में" → ✅ "**नए फ़ोल्डर में**" (adjective also in oblique)

### का/के/की Possessive — Agrees with the POSSESSED Noun (severity 1.5)

The possessive postposition **का/के/की** agrees with the **POSSESSED noun**, NOT the possessor (counterintuitive for English speakers).

| Possessor | Possessed | Form | Example |
|---|---|---|---|
| (any) | masc sg | **का** | यूज़र **का** अकाउंट (user's account — अकाउंट is masc sg) |
| (any) | masc pl / oblique | **के** | यूज़र **के** अकाउंट्स (user's accounts — masc pl) |
| (any) | fem (any) | **की** | यूज़र **की** फ़ाइल (user's file) — wait, फ़ाइल is masc, so should be **का**. |
| (any) | fem (any) | **की** | यूज़र **की** सेटिंग्स (user's settings — fem) |

Examples:
- ❌ फ़ोल्डर **का** सेटिंग्स (masc form with fem possessed) → ✅ फ़ोल्डर **की** सेटिंग्स (सेटिंग्स is fem → की)
- ❌ ऐप **की** डेटा (fem form with masc possessed) → ✅ ऐप **का** डेटा (डेटा is masc → का)

### Ergative Construction with ने (severity 2.0)

**In perfective transitive sentences**, Hindi uses an **ergative construction**: the subject takes the ergative marker **ने**, and **the verb agrees with the OBJECT** (NOT the subject — opposite of English).

| Tense | Construction | Verb agreement |
|---|---|---|
| Imperfective (present, imperfect past, future) | Subject (no marker) + verb | Verb agrees with **subject** |
| Perfective transitive | Subject **+ ने** + Object + verb | Verb agrees with **object** |
| Perfective intransitive | Subject (no ने) + verb | Verb agrees with **subject** |

Examples:
- Imperfective: "यूज़र फ़ाइल सेव करता है" (verb agrees with यूज़र — masc sg)
- Perfective ergative: "यूज़र **ने** फ़ाइल **सेव की**" (verb agrees with फ़ाइल — masc sg, but actually फ़ाइल is masc so it should be `सेव किया`. Let me re-check. Actually, the source has "फ़ाइल" treated as masculine here.)

**Examples from the source:**
- ❌ मैंने फ़ाइल सेव **किये** (plural verb with sg object) → ✅ मैंने फ़ाइल सेव **किया** (फ़ाइल = masc sg)
- ❌ यूज़र ने फ़ाइलें डाउनलोड **किया** (sg masc verb with fem pl object) → ✅ यूज़र ने फ़ाइलें डाउनलोड **कीं** (fem pl)

**Special case — object marked with को:** If the object is marked with `को` (definite/specific), the verb defaults to **masculine singular** regardless of actual object gender/number:
- "यूज़र ने उस फ़ाइल **को** डिलीट **किया**" (फ़ाइल marked with को → verb defaults to masc sg किया)

### Compound Verbs (noun + करना pattern) (severity 1.0)

**Hindi tech vocabulary heavily uses the noun + करना ("to do") pattern:**

| English verb | Hindi compound |
|---|---|
| to click | क्लिक **करना** |
| to save | सेव **करना** |
| to download | डाउनलोड **करना** |
| to upload | अपलोड **करना** |
| to delete | डिलीट **करना** (or हटाना) |
| to log in | लॉगिन **करना** |
| to log out | लॉगआउट **करना** |
| to copy | कॉपी **करना** |
| to paste | पेस्ट **करना** |
| to start | शुरू **करना** |
| to stop | बंद **करना** |
| to open | खोलना (single verb) |
| to close | बंद करना / बंद होना |

The English noun stays as-is (often borrowed); `करना` ("to do") is conjugated for tense/person/gender.

- Imperative formal: क्लिक **करें**, सेव **करें**, डाउनलोड **करें**
- Imperfective: यूज़र क्लिक **करता है**
- Perfective ergative: यूज़र ने क्लिक **किया**

### Nukta Dots for Borrowed Sounds (severity 0.5–1.0)

Hindi uses **nukta** (a dot below a letter) to mark borrowed Perso-Arabic / English sounds:

| With nukta | Without (incorrect for these sounds) | Sound |
|---|---|---|
| **फ़** | फ | /f/ (as in फ़ाइल "file", फ़ोन "phone") |
| **ज़** | ज | /z/ (as in ज़िप "zip", ज़ोन "zone") |
| **ड़** | ड | retroflex flap /ɽ/ (as in बड़ा "big") |
| **ढ़** | ढ | aspirated retroflex flap (as in पढ़ना "to read") |
| **क़** | क | /q/ (Arabic uvular — rare; usually written क) |
| **ख़** | ख | /x/ (Persian — rare) |
| **ग़** | ग | /ɣ/ (Persian — rare) |

**Critical for tech vocabulary:**
- ✅ **फ़ाइल** (with nukta — file) — NOT फाइल
- ✅ **फ़ोल्डर** (with nukta — folder)
- ✅ **फ़ोन** (with nukta — phone)
- ✅ **ज़िप** (with nukta — zip)

Many writers OMIT nukta in casual writing, but PROFESSIONAL Hindi UI should preserve them. Severity 0.5 (cosmetic but expected).

### Plural Formation

| Pattern | Singular | Plural | Notes |
|---|---|---|---|
| Masc ending in -ा | लड़**का** (boy) | लड़**के** (boys) | direct pl |
| Masc ending in consonant | फ़ोल्डर | फ़ोल्डर | no change in direct pl |
| Fem ending in -ी | लड़**की** (girl) | लड़**कियाँ** (girls) | nasalized -ियाँ |
| Fem ending in consonant | फ़ाइल | फ़ाइल**ें** (when treated as fem) | -ें pl |
| Oblique pl (all) | — | -**ों** | फ़ाइलों में |

In tech vocabulary, masculine borrowings (फ़ाइल, सिस्टम, फ़ोल्डर) often DON'T change in plural direct form:
- "एक फ़ाइल" (one file) → "कई फ़ाइलें" or "कई फ़ाइल" (many files — both seen; "फ़ाइलें" is more formal)
- "एक सिस्टम" → "कई सिस्टम" (no change)

### ICU Plurals (severity 1.5)

**Hindi has 2 plural categories: `one` and `other`.**

```icu
{count, plural,
  one {# फ़ाइल}
  other {# फ़ाइलें}
}
```

- one: n = 1
- other: 0, 2, 3, 4, ...

(Hindi's plural system is morphologically rich but CLDR groups it into 2 categories for ICU purposes.)

### Indian Number Grouping — Lakhs and Crores (severity 1.0)

**Indian number formatting uses lakhs (100,000) and crores (10,000,000)** — groups of 2 digits after the first group of 3 (counting from the right).

| Number | Indian grouping | Western grouping |
|---|---|---|
| One lakh (100,000) | **1,00,000** | 100,000 |
| Ten lakh / one million (1,000,000) | **10,00,000** | 1,000,000 |
| One crore (10,000,000) | **1,00,00,000** | 10,000,000 |
| 123,456 | **1,23,456** | 123,456 |
| ₹50,00,000 | ✅ **₹50,00,000** | ❌ ₹5,000,000 |

**Critical:**
- ❌ ₹123,456 (Western — wrong for Indian context) → ✅ **₹1,23,456**
- ❌ 5,000,000 → ✅ **50,00,000** (50 lakh)
- ❌ 10,000,000 → ✅ **1,00,00,000** (1 crore)

This applies to **all currency and numeric displays in Indian-context apps**. International products targeting India MUST use Indian grouping.

## UI Conventions

### Button Labels — आप Imperative

Hindi buttons use the **आप imperative** (-ें or -इए ending). Never use तुम (-ओ) or तू (bare verb) forms.

| Wrong (तुम form) | Wrong (तू form) | Correct (आप form) | English |
|---|---|---|---|
| सेव करो | सेव कर | **सेव करें** / **सहेजें** | Save |
| रद्द करो | रद्द कर | **रद्द करें** / **रद्द कीजिए** | Cancel |
| डिलीट करो | डिलीट कर | **डिलीट करें** / **हटाएँ** | Delete |
| अपलोड करो | अपलोड कर | **अपलोड करें** | Upload |
| डाउनलोड करो | डाउनलोड कर | **डाउनलोड करें** | Download |
| क्लिक करो | क्लिक कर | **क्लिक करें** | Click |
| खोलो | खोल | **खोलें** | Open |
| बंद करो | बंद कर | **बंद करें** | Close |

Both `-ें` (करें) and `-इए` (कीजिए) are formal imperative — `-ें` is more common in modern UI; `-इए` slightly more formal/older.

### Status Messages — Present Continuous with हो रहा है

For ongoing actions, use **`X हो रहा है`** (X is happening — present continuous) or **`X किया जा रहा है`** (X is being done):

| Wrong (bare verb) | Correct (progressive) | English |
|---|---|---|
| लोड | **लोड हो रहा है...** | Loading... |
| सेव | **सेव हो रहा है...** | Saving... |
| प्रोसेस | **प्रोसेस हो रहा है...** | Processing... |
| कनेक्ट | **कनेक्ट हो रहा है...** | Connecting... |
| (waiting) | **कृपया प्रतीक्षा करें...** | Please wait... |

Use **हो रहा है** for masculine subjects, **हो रही है** for feminine subjects:
- सेव हो रहा है (सेव is treated as masc abstract noun)
- फ़ाइल अपलोड हो रही है (if फ़ाइल treated as fem) or हो रहा है (if masc — standard)

For completion: **`X हो गया`** (X is done — masc) or **`X हो गई`** (fem):
- **सेव हो गया** (Saved)
- **डाउनलोड पूरा हुआ** (Download complete)
- **त्रुटि हो गई** (Error occurred — त्रुटि is fem)

### Drag-and-Drop Vocabulary

- **खींचें** = drag (formal imperative)
- **छोड़ें** = drop / release (formal imperative)
- **यहाँ** = here

```
✅ यहाँ खींचें                       (drag here)
✅ फ़ाइल यहाँ खींचें और छोड़ें       (drag and drop file here)
✅ अपलोड करने के लिए छोड़ें          (drop to upload)
❌ drag फ़ाइल / drop here            (English — wrong)
❌ छोड़ दें (release/let go — too literal)
```

### Error Messages — What + What to do

Hindi error messages should state **what went wrong + what to do**:

| Wrong (incomplete) | Correct (what + action) | English |
|---|---|---|
| फ़ाइल नहीं मिली। | **फ़ाइल नहीं मिली। कृपया पथ जाँचें।** | File not found. Please check the path. |
| त्रुटि हुई। | **त्रुटि हुई। कृपया पुनः प्रयास करें।** | Error occurred. Please try again. |
| गलत पासवर्ड। | **पासवर्ड गलत है। कृपया पुनः प्रयास करें।** | Wrong password. Please try again. |

### Empty State Messages

- "**कोई X नहीं**" (no X) or "**अभी तक कोई X नहीं**" (no X yet):
  - "कोई फ़ाइल नहीं" (No files)
  - "कोई परिणाम नहीं मिला" (No results found)
  - "अभी तक कोई संदेश नहीं" (No messages yet)

### Bulk Actions

| English | Hindi |
|---|---|
| Select All | **सभी चुनें** |
| Deselect All | **सभी चयन हटाएँ** |
| Clear All | **सभी साफ़ करें** |
| Got it / OK | **ठीक है** (gender-neutral) |

**Note on "Got it":** Avoid **समझ गया** (masc) / **समझ गई** (fem) unless user gender is known. **ठीक है** ("OK / alright") is gender-neutral.

## Punctuation, Numbers, Dates, Currency

### Quotation Marks
- Hindi uses standard double quotes `"..."` or single quotes `'...'`
- Curly or straight are both acceptable
- No special "Hindi quote marks"

### Numbers
- Decimal separator: **period** (3**.**14)
- Thousands separator: **comma** with **Indian grouping** (1**,**23**,**456)
- See Indian grouping section above for details

### Dates — DD/MM/YYYY
- **Numeric**: `15/01/2024` (slashes) — most common
- Alternative: `15.01.2024` (periods — also seen)
- **Word form**: `15 जनवरी 2024` (no comma; day-month-year)
- ❌ 01/15/2024 (US) → ✅ **15/01/2024**

Months (Hindi names — all from Sanskrit):
| English | Hindi |
|---|---|
| January | जनवरी |
| February | फ़रवरी |
| March | मार्च |
| April | अप्रैल |
| May | मई |
| June | जून |
| July | जुलाई |
| August | अगस्त |
| September | सितंबर |
| October | अक्तूबर |
| November | नवंबर |
| December | दिसंबर |

### Time
- 12-hour common: **2:30 PM** or **दोपहर 2:30** (afternoon)
- 24-hour also used: **14:30**
- Time-of-day markers: सुबह (morning), दोपहर (noon/afternoon), शाम (evening), रात (night)

### Currency: INR Rupee with Indian grouping
- **India uses the Indian Rupee (₹ / INR).**
- Format: `₹1,23,456.78` (₹ before amount, Indian grouping, period decimal)
- Subdivision: 100 paise (पैसा), rarely used in everyday UI
- ❌ ₹123,456.78 (Western grouping) → ✅ **₹1,23,456.78**
- ❌ $100 → ✅ **₹8,500** (or whatever INR equivalent — use ₹ for Indian users)

## Terminology

| English | Preferred Hindi | Avoid |
|---|---|---|
| Click | क्लिक करें | चटकाएँ (rarely used in tech) |
| Settings | सेटिंग्स | विन्यास (rare in modern tech) |
| User | यूज़र / उपयोगकर्ता | उपयोक्ता (rare) |
| Delete | डिलीट करें / हटाएँ | |
| Save | सेव करें / सहेजें | |
| Upload | अपलोड करें | |
| Download | डाउनलोड करें | |
| Log in | लॉगिन करें | |
| Log out | लॉगआउट करें | |
| File | फ़ाइल | संचिका (Sanskritic, rare) |
| Folder | फ़ोल्डर | |
| Dashboard | डैशबोर्ड | |
| Email | ईमेल | |
| Password | पासवर्ड | |
| Search | खोजें / सर्च करें | |
| Workflow | कार्य-प्रवाह | वर्कफ़्लो (transliteration; "कार्य-प्रवाह" preferred) |
| Feature | सुविधा / विशेषता | फ़ीचर (transliteration; native preferred for marketing) |
| Submit | जमा करें / सबमिट करें | |
| Cancel | रद्द करें | |
| OK / Confirm | ठीक है / पुष्टि करें | |
| Help | मदद / सहायता | |
| About | हमारे बारे में | (use "हमारे बारे में" for "About us" — not just "के बारे में") |
| Pricing | मूल्य निर्धारण | |
| Sign In | साइन इन करें | |

**Tech English tolerance:** Modern Hindi tech UI is **loanword-friendly**. क्लिक, फ़ाइल, डाउनलोड, सिस्टम, यूज़र, पासवर्ड, ईमेल are STANDARD — don't replace them with obscure Sanskritic terms unless the audience specifically requires high-purity Hindi (government/literary contexts).

**Proper noun abbreviations in UI:**
- ✅ **अमेरिका** / **अमरीका** (NOT "संयुक्त राज्य अमेरिका" in cramped UI)
- ✅ **ब्रिटेन** / **यूके** (NOT the full official name)
- ✅ **ऑस्ट्रेलिया** (NOT "ऑस्ट्रेलिया राष्ट्रमंडल")
- ✅ **भारत** for India

**Brand names** remain unchanged (Apple, Google, Microsoft, Facebook). They typically take **masculine gender** in Hindi grammar contexts.

## Compound Adjective Anti-Patterns

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| X-संचालित | **X आधारित / X द्वारा संचालित / X तकनीक से** | "X-powered" |
| AI-संचालित | **AI आधारित** / **एआई आधारित** | "AI-powered" |
| X-जागरूक | **X के प्रति जागरूक / X को ध्यान में रखते हुए** | "X-aware" |
| यूज़र-अनुकूल (compound) | **यूज़र के अनुकूल / उपयोग में आसान** | "user-friendly" |

## Calque / Anti-Pattern Blocklist

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| अर्थ बनाता है | **समझ में आता है / यह तर्कसंगत है** | "makes sense" |
| दिन के अंत में | **अंततः / मूल रूप से** | "at the end of the day" |
| वास्तव में नहीं | **असल में नहीं / ठीक नहीं** | "not really" |
| यह समझ में आता है (overly literal) | **यह तर्कसंगत है / यह उचित है** | "this makes sense" |
| टांग तोड़ो | **शुभकामनाएँ! / कामयाबी मिले!** | "break a leg" |
| केक का टुकड़ा | **बाएँ हाथ का खेल / बच्चों का खेल** | "piece of cake" |
| जब सूअर उड़ें | **जब तक सूरज पश्चिम से न निकले** | "when pigs fly" |
| दो पक्षियों को एक पत्थर से मारना | **एक पंथ दो काज / एक तीर से दो शिकार** | "kill two birds with one stone" |
| सिर पर कील मारी | **बिलकुल सही कहा / मुद्दे की बात कही** | "hit the nail on the head" |

## Hindi Idioms to Use

| English idiom | Hindi equivalent | Literal Hindi meaning |
|---|---|---|
| break a leg | **शुभकामनाएँ! / कामयाबी मिले!** | "Best wishes! / May you succeed!" |
| piece of cake | **बाएँ हाथ का खेल** | "left hand's game (i.e., trivially easy)" |
| when pigs fly | **जब तक सूरज पश्चिम से न निकले** | "when the sun rises from the west" |
| kill two birds with one stone | **एक पंथ दो काज / एक तीर से दो शिकार** | "two tasks in one journey / two hunts with one arrow" |
| hit the nail on the head | **बिलकुल सही कहा / मुद्दे की बात कही** | "said exactly right / spoke to the point" |
| good luck | **शुभकामनाएँ / कामयाबी मिले** | |
| never mind | **कोई बात नहीं** | "no problem" |
| no problem | **कोई बात नहीं / कोई दिक्कत नहीं** | |

## Self-Check Checklist

Run BEFORE finalizing each translation:

**Accuracy (critical):**
- [ ] **SOV word order** — verb at END (यूज़र फ़ाइल सेव करता है)
- [ ] **Gender agreement:** masc/fem (फ़ाइल = masc, वेबसाइट = fem, सेटिंग्स = fem)
- [ ] **Adjective agreement:** -ा/-े/-ी match noun gender + number + case
- [ ] **Postpositions follow nouns** (फ़ोल्डर में, NOT में फ़ोल्डर)
- [ ] **Oblique case before postposition** (लड़के को, NOT लड़का को)
- [ ] **का/के/की agrees with possessed noun** (यूज़र की सेटिंग्स — सेटिंग्स is fem → की)
- [ ] **Ergative ने** in perfective transitive (यूज़र ने फ़ाइल सेव की)
- [ ] **Verb agrees with OBJECT** under ने (मैंने फ़ाइल सेव की — fem object → की)
- [ ] **Compound verbs noun+करना** (क्लिक करें, सेव करें)
- [ ] **Nukta dots preserved** (फ़ाइल, ज़िप — NOT फाइल, जिप)
- [ ] **Indian number grouping** (₹1,23,456 NOT ₹123,456)
- [ ] **Date format:** DD/MM/YYYY (15/01/2024)
- [ ] **Currency:** ₹ Rupee with Indian grouping
- [ ] **Placeholders preserved** exactly (Roman script for tech identifiers)

**Naturalness:**
- [ ] **ALWAYS आप form** — NEVER तुम/तू in UI (करें not करो; pursue with कृपया)
- [ ] **`कृपया` for polite requests** in instructions
- [ ] **Imperative buttons** in आप form (सेव करें, हटाएँ, रद्द करें)
- [ ] **Present continuous status** with हो रहा है (लोड हो रहा है...)
- [ ] **Completion with हो गया/गई** (सेव हो गया, त्रुटि हो गई)
- [ ] **Drag-and-drop:** खींचें, छोड़ें (NOT drag, drop)
- [ ] **Tech loanwords standard** (फ़ाइल, क्लिक, डाउनलोड — NOT obscure Sanskritic terms)
- [ ] **Hindi idioms** for English idioms (शुभकामनाएँ for "break a leg")
- [ ] **No literal calques** (समझ में आता है, NOT अर्थ बनाता है)
- [ ] **Error messages: what + advice** (फ़ाइल नहीं मिली। कृपया पथ जाँचें।)
- [ ] **Abbreviations in UI** (अमेरिका not संयुक्त राज्य अमेरिका; ब्रिटेन not full title)
- [ ] **"ठीक है" not gendered "समझ गया/गई"** for "Got it"
- [ ] **Gender-neutral when possible** — restructure to avoid agreement on user's name/role
- [ ] **`हमारे बारे में`** for "About us" (NOT just "के बारे में")

## Worked Examples

### Example 1 — Save button + status

**Source:**
> Save  
> Saving your changes...  
> Changes saved successfully.

**Wrong:**
> सेव करो (तुम form)  
> सेव कर रहा है तुम्हारे बदलाव... (English word order + तुम)  
> बदलाव सफलतापूर्वक सेव किए गए। (passive, OK but stiff)

**Correct:**
> **सेव करें** (आप formal imperative)  
> **आपके बदलाव सेव हो रहे हैं...** (SOV + progressive)  
> **बदलाव सेव हो गए।** / **बदलाव सहेजे गए।** (completion with हो गए)

### Example 2 — Files counter

**Source:**
> 1 file / 5 files

**Correct Hindi ICU:**
```
{count, plural,
  one {# फ़ाइल}
  other {# फ़ाइलें}
}
```

(फ़ाइल pluralizes to फ़ाइलें in formal Hindi tech vocabulary.)

### Example 3 — Drag-and-drop area

**Source:**
> Drag and drop files here, or click to browse

**Wrong:**
> Drag and drop फ़ाइल यहाँ, या क्लिक करो ब्राउज़ करने के लिए (English verbs + तुम + English-style word order)

**Correct (SOV + आप + native verbs):**
> **फ़ाइलें यहाँ खींचें और छोड़ें, या ब्राउज़ करने के लिए क्लिक करें**

### Example 4 — SOV word order

**Source:**
> The user saves the file in the folder.

**Wrong (SVO):**
> यूज़र सेव करता है फ़ाइल को में फ़ोल्डर (English order + wrong postposition order)

**Correct (SOV):**
> **यूज़र फ़ोल्डर में फ़ाइल सेव करता है।** (S-O-V; postposition follows folder)

### Example 5 — Ergative with ने

**Source:**
> The user saved the file. / I downloaded the files.

**Wrong:**
> यूज़र ने फ़ाइल सेव किये (pl verb with sg object)
> मैंने फ़ाइलें डाउनलोड किया (sg masc verb with fem pl object)

**Correct:**
> **यूज़र ने फ़ाइल सेव की।** (फ़ाइल taken as fem here, agreeing) — or **यूज़र ने फ़ाइल सेव किया।** (फ़ाइल as masc — standard) 
> **मैंने फ़ाइलें डाउनलोड कीं।** (verb agrees with fem pl object)

### Example 6 — Adjective + noun gender

**Source:**
> New file / New website / Good settings

**Wrong:**
> नई फ़ाइल (treating फ़ाइल as fem — common error, but standard tech vocabulary says masc)
> नया वेबसाइट (treating वेबसाइट as masc — wrong)
> अच्छा सेटिंग्स (masc with fem)

**Correct (standard):**
> **नया फ़ाइल / नई फ़ाइल** (mixed practice — both seen; "नया फ़ाइल" formally correct)
> **नई वेबसाइट** (fem)
> **अच्छी सेटिंग्स** (fem pl)

### Example 7 — Postposition + oblique

**Source:**
> Save to the new folder.

**Wrong:**
> नया फ़ोल्डर में सेव करें (direct case before में)

**Correct:**
> **नए फ़ोल्डर में सेव करें।** (oblique नए before में)

### Example 8 — का/के/की with possessed noun

**Source:**
> User's settings / User's account / User's file

**Wrong:**
> यूज़र का सेटिंग्स (masc form with fem possessed)
> यूज़र की अकाउंट (fem form with masc possessed)

**Correct (agrees with possessed noun):**
> **यूज़र की सेटिंग्स** (सेटिंग्स = fem → की)
> **यूज़र का अकाउंट** (अकाउंट = masc → का)
> **यूज़र की फ़ाइल** OR **यूज़र का फ़ाइल** (depending on which gender treatment)

### Example 9 — Indian number grouping

**Source:**
> Total: $50,000 / Premium plan: ₹100,000/year

**Wrong (Western grouping):**
> कुल: $50,000 / प्रीमियम योजना: ₹100,000/वर्ष

**Correct (Indian grouping, INR for Indian users):**
> **कुल: ₹40,00,000** (rounded equivalent — also note: Indian grouping puts comma after first 3, then groups of 2)
> **प्रीमियम योजना: ₹1,00,000/वर्ष** (1 lakh per year)

### Example 10 — Nukta preservation

**Source:**
> File / Phone / Zip code

**Wrong (no nukta):**
> फाइल / फोन / जिप कोड

**Correct (with nukta):**
> **फ़ाइल** / **फ़ोन** / **ज़िप कोड**

### Example 11 — Formal आप imperative + कृपया

**Source:**
> Please click here to continue.

**Wrong (तुम form):**
> कृपया यहाँ क्लिक करो जारी रखने के लिए। (mixed कृपया-formal + तुम-informal — wrong)

**Correct (consistent आप):**
> **जारी रखने के लिए कृपया यहाँ क्लिक करें।** (SOV + आप + कृपया)

### Example 12 — Idiom adaptation

**Source:**
> It's a piece of cake. / Break a leg!

**Wrong (literal):**
> यह केक का टुकड़ा है। / टांग तोड़ो!

**Correct (Hindi idioms):**
> **यह बाएँ हाथ का खेल है।** / **यह बहुत आसान है।** (piece of cake = left hand's game / very easy)
> **शुभकामनाएँ!** / **कामयाबी मिले!** (break a leg = best wishes / may you succeed)

## When in Doubt

1. **Verb position?** Always at the END. Hindi is strictly SOV.
2. **Politeness level?** ALWAYS आप form in software UI. Never तुम, never तू. Use `कृपया` for polite requests.
3. **Gender unclear?**
   - Most tech terms ending in consonants → check standard usage (फ़ाइल = masc, सेटिंग्स = fem, ईमेल = fem, वेबसाइट = fem)
   - Masc patterns: -ा (लड़का), consonant (फ़ोल्डर, सिस्टम)
   - Fem patterns: -ी (लड़की), -इन (मालकिन), abstract -ता (मित्रता)
   - When uncertain, default to masculine and restructure if it sounds wrong
4. **Postposition unclear?**
   - "in" → में
   - "on" → पर
   - "to / for" → को OR के लिए
   - "from / with / by" → से
   - "of" → का/के/की (agrees with possessed!)
5. **Oblique case?** Required before any postposition. Masc -ा nouns → -े (लड़का → लड़के), pl forms → -ों (लड़कों, फ़ोल्डरों).
6. **का/के/की unclear?** Look at the POSSESSED noun (the thing being possessed). Its gender determines which form to use.
7. **ने needed?** Yes if: (a) verb is transitive AND (b) tense is perfective. In ने constructions, verb agrees with OBJECT.
8. **Compound verb or single?** Most tech actions use noun+करना. Single verbs exist (खोलना to open, बंद करना to close, देखना to see).
9. **Sanskritic vs English loanword?** Default to English loanword (फ़ाइल, क्लिक, डाउनलोड) for tech contexts unless audience requires high-purity Hindi.
10. **Number formatting?** Always Indian grouping (1,23,456 not 123,456) for Indian users.
11. **Nukta dot?** Always preserve for /f/, /z/, /ɽ/ sounds (फ़ाइल not फाइल; ज़िप not जिप).
12. **Idiom?** Use Hindi equivalent (शुभकामनाएँ, बाएँ हाथ का खेल), not literal translation.

Hindi's SOV order, ergative ने construction, and possessor-vs-possessed agreement in का/के/की are the three structural features that English-trained translators MOST commonly miss. When the translation feels off, check first: (a) is the verb at the end? (b) is ने present in perfective transitive? (c) does का/के/की agree with the possessed noun?
