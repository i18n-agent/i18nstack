---
name: localize-bn
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Bengali (বাংলা / Bāṅlā) for Bangladesh (bn-BD) and Indian Bengali speakers in West Bengal / Tripura (bn-IN). Bengali is Indo-Aryan, written in Eastern Nagari script (LTR), with NO grammatical gender, SOV word order, 3-tier honorific verb conjugation (তুই tui intimate / তুমি tumi peer / আপনি apni respectful — DEFAULT for UI), mandatory classifiers with numbers (একটি ফাইল not এক ফাইল, পাঁচজন ইউজার not পাঁচ ইউজার), animate vs inanimate plural marking (-রা for humans, -গুলো for things), case-marking postpositions attached without space or hyphen (ফাইলে not ফাইল এ, ইউজারের not ইউজার এর), compound verbs with করা (ক্লিক করুন, সেভ করুন), completive compounds (সেভ হয়ে গেছে for \"saved\"), conjunct consonants (যুক্তাক্ষর — ক্ষ, জ্ঞ, ন্ত, ত্র etc), chandrabindu (ঁ) vs anusvara (ং) nasal distinction, Indian-style number grouping with lakhs/crores (১,২৩,৪৫৬), DD/MM/YYYY dates, BDT (৳/Tk) for Bangladesh vs INR (₹) for India — DIFFERENT CURRENCIES, religious neutrality between Muslim-majority Bangladesh and Hindu-majority West Bengal, bn-BD vs bn-IN lexical preferences (Arabic/Persian loans in BD vs Sanskrit/English loans in IN), and Latin tech identifiers (Git, API, JSON) embedded inside Bengali script. CRITICAL: Bengali is NOT Hindi (different script, different language family branch from Indo-Aryan but distinct grammar, NO gender unlike Hindi); closest sister language is Assamese (~70% mutual intelligibility) — Bengali and Assamese share script with two letter differences (র vs ৰ, য় vs য়)."
---

# Translate to Bengali (bn → বাংলা) — High-Fidelity Skill

## Scope & Variants

Bengali (বাংলা / Bāṅlā) is the official language of Bangladesh and the second-most-spoken language in India (West Bengal, Tripura, parts of Assam). It is written in the **Eastern Nagari script** (also called Bengali-Assamese script), an LTR abugida derived from Brahmi.

**~270 million speakers worldwide** (~170M Bangladesh + ~100M India + diaspora). The 7th most-spoken language in the world.

| Locale | Name | Speakers | Notes |
|--------|------|----------|-------|
| `bn-BD` | Bangladesh Standard | ~170M | Official language of Bangladesh. Heavier Arabic/Persian loanword influence. Currency: BDT (৳ / Tk). |
| `bn-IN` | Indian Bengali (West Bengal / Tripura) | ~100M | One of India's 22 scheduled languages. Heavier Sanskrit/English loanword influence. Currency: INR (₹). |

**Both write THE SAME Bengali language in THE SAME script** — fully mutually intelligible — but have systematic differences in:

| Axis | bn-BD (Bangladesh) | bn-IN (India / West Bengal) |
|------|--------------------|------------------------------|
| **Loanword bias** | Arabic / Persian / Urdu (esp. for everyday concepts) | Sanskrit (তৎসম) / English |
| **"Water"** | পানি (pani — Persian-origin, dominant in BD) | জল (jol — Sanskrit-origin, dominant in WB) |
| **"Salt"** | নুন / লবণ | নুন (more common) |
| **"Invitation"** | দাওয়াত (Arabic-origin) | নিমন্ত্রণ (Sanskrit) |
| **Greeting** | আসসালামু আলাইকুম (Muslim) / নমস্কার (rare) | নমস্কার (default) / সালাম (Muslim minority) |
| **"Bath / shower"** | গোসল (gosol — Arabic) | স্নান (snan — Sanskrit) |
| **"Help"** | মদদ (madad — Persian) / সাহায্য | সাহায্য (default) |
| **Spelling reforms** | More phonetic, fewer silent letters retained | More etymological / Sanskritic spellings |
| **Currency** | **৳ / Tk / টাকা** (BDT taka) | **₹ / টাকা** (INR rupee) |
| **Date** | DD/MM/YYYY (both) | DD/MM/YYYY (both) |
| **Religious calendar overlay** | Bengali calendar (বঙ্গাব্দ) + Islamic Hijri sometimes | Bengali calendar (বঙ্গাব্দ) + Hindu Saka/Vikram |
| **Phone** | +880 country code | +91 country code |
| **Time-of-day greetings** | শুভ সকাল / শুভ দুপুর | Same |

**On first use, ASK the user:**

> Which Bengali variant should I target?
> - **bn-BD** (Bangladesh — Muslim-majority context, BDT taka, পানি/দাওয়াত vocabulary)
> - **bn-IN** (West Bengal / Tripura, India — secular/Hindu-majority context, INR rupee, জল/নিমন্ত্রণ vocabulary)
> - **Pan-Bengali neutral** (technical content for both audiences — minimize region-specific lexical choices, use English loanwords as common ground)

**For TECH PRODUCT UI** (the most common case): the lexical drift between bn-BD and bn-IN is much smaller because both share English loanwords for technical concepts (ক্লিক, সেভ, ডাউনলোড, লগইন, ফাইল). **English tech loans serve as common ground**. The differences mostly surface in marketing copy, idioms, religious framing, and currency. If the surface is just buttons/labels/errors, **pan-Bengali neutral** is usually safe.

---

## Identity Guardrail — Bengali Is NOT Hindi (and NOT Assamese either, though close)

Bengali is **Indo-Aryan** (a daughter branch of Indo-European), descended from Magadhi Prakrit through Eastern Apabhraṃśa. Its **closest living sister language is Assamese (অসমীয়া)** — they share a writing system (Eastern Nagari) with only two letter differences and are roughly 70% mutually intelligible. **Bishnupriya Manipuri**, **Chittagonian**, **Sylheti**, **Rohingya**, and **Rangpuri/Rajbanshi** are close relatives often classified as dialects or sister languages.

| Often-confused with | Why it's NOT Bengali |
|---------------------|------------------------|
| **Hindi (हिन्दी)** | DIFFERENT script (Devanagari देवनागरी vs Bengali বাংলা), DIFFERENT grammar (Hindi HAS grammatical gender — masculine/feminine — Bengali does NOT), different verb conjugation patterns, different number system look. Sister branch within Indo-Aryan but **not mutually intelligible** in writing. Many Bengalis read/understand spoken Hindi via Bollywood exposure but they are not the same language. |
| **Urdu (اردو)** | Different script entirely (Perso-Arabic, RTL). Linguistically sister to Hindi. Bengali has zero structural overlap with Urdu beyond shared Persian/Arabic loans in bn-BD. |
| **Assamese (অসমীয়া)** | THE closest relative. Same script family (Eastern Nagari), ~70% mutual intelligibility. Distinguishing letters: Assamese has **ৰ** (different from Bengali র) and **ৱ** (Bengali uses ব). Different verb agreement patterns. **Do NOT confuse a Bengali translation with an Assamese one** — they look almost identical but are distinct standards. |
| **Sanskrit (संस्कृत)** | Bengali borrows heavily from Sanskrit (তৎসম "same as that" loanwords), but Sanskrit is the ancient liturgical ancestor, not modern Bengali. Sanskritic spelling preserved in formal Bengali but pronunciation drifted significantly. |
| **Odia / Oriya (ଓଡ଼ିଆ)** | Different script (Odia uses curvilinear forms). Geographic neighbor (Odisha state, India). Related but distinct Indo-Aryan language. |

**Critical identity markers — Bengali has these, Hindi/Urdu do not:**

1. **NO grammatical gender** — `ছেলেটি লম্বা` (the boy is tall) and `মেয়েটি লম্বা` (the girl is tall) use the SAME adjective form `লম্বা`. Hindi would require `लंबा` (m.) vs `लंबी` (f.).
2. **Honorific verb conjugation, NOT gender conjugation** — verbs change for তুই / তুমি / আপনি honorific level, not for subject's gender.
3. **Single 3rd-person pronoun for all humans** — `সে` (she/he, no gender) and `তিনি` (formal s/he, no gender). Hindi distinguishes `वह` (with verb agreement gendered).
4. **Bengali script (Eastern Nagari)** — distinct from Devanagari. The Bengali letter অ resembles a different glyph from Devanagari अ.
5. **Inherent vowel ô (অ)** — pronounced as /ɔ/ in Bengali, NOT /ə/ as in Hindi.
6. **3 sibilants merge to one** — Bengali script preserves শ, ষ, স but all pronounced /ʃ/ (sh-sound), unlike Hindi which distinguishes them.
7. **No retroflex /ʈ/-vs-/ʈʰ/-vs-/ɖ/-vs-/ɖʱ/ contrast in pronunciation** for many speakers (script preserves the contrast).

**When the source mentions "translate to Indian languages" or "South Asian languages," confirm with user which language — DO NOT assume Bengali = Hindi.**

---

## Register — Three-Tier Honorific System

Bengali has **THREE honorific levels** baked into verb conjugation. Unlike European T/V distinctions (just 2), Bengali distinguishes:

| Pronoun | Register | When used | Example verb "to do" (present) | Example verb "to do" (imperative) |
|---------|----------|-----------|--------------------------------|-----------------------------------|
| **তুই** (tui) | Intimate / very informal | Close childhood friends, siblings (in some families), children, God in prayer, animals | তুই করিস (kôris) | তুই কর (kôr) — abrupt |
| **তুমি** (tumi) | Familiar / peer | Friends, peers, younger relatives, spouse, children (in some families) | তুমি কর (kôro) | তুমি কর / করো (kôro) |
| **আপনি** (apni) | Respectful / polite | Strangers, elders, professionals, ALL SOFTWARE UI | আপনি করেন (kôren) | আপনি করুন (kôrun) |

**Possessives match the register:**

| English | তুই (intimate) | তুমি (peer) | আপনি (polite — DEFAULT) |
|---------|----------------|--------------|---------------------------|
| your | তোর (tor) | তোমার (tomar) | আপনার (apnar) |

**Default for ALL product UI, marketing, docs: আপনি (apni) — respectful register.** Using তুমি or তুই in software UI is rude, condescending, or alien — sometimes intentionally for hyper-casual brands targeting Gen Z, but generally avoided.

### Imperative endings — the most common UI form

| English | আপনি form (DEFAULT for UI) | তুমি form (avoid in UI) | তুই form (NEVER in UI) |
|---------|------------------------------|--------------------------|--------------------------|
| Click | **ক্লিক করুন** (klik korun) | ক্লিক কর / করো | ক্লিক কর |
| Save | **সেভ করুন** | সেভ কর / করো | সেভ কর |
| Delete | **মুছুন** (muchhun) / মুছে ফেলুন | মোছ / মুছে ফেল | মোছ |
| Open | **খুলুন** (khulun) | খোল / খুলো | খোল |
| Close | **বন্ধ করুন** (bondho korun) | বন্ধ কর | বন্ধ কর |
| Submit | **জমা দিন** (jôma din) | জমা দাও | জমা দে |
| Send | **পাঠান** (pathan) | পাঠাও | পাঠা |
| Cancel | **বাতিল করুন** (batil korun) | বাতিল কর | বাতিল কর |
| Continue | **চালিয়ে যান** (chaliye jan) | চালিয়ে যাও | চালিয়ে যা |
| Try again | **আবার চেষ্টা করুন** | আবার চেষ্টা কর | আবার চেষ্টা কর |
| Sign in | **সাইন ইন করুন** / **লগইন করুন** | সাইন ইন কর | সাইন ইন কর |

### Hard rule: NEVER mix registers in the same UI

Mixing আপনি verbs with তুমি possessives (or vice versa) is the **#1 Bengali UI failure**.

| ✗ Wrong (mixed) | ✓ Correct (consistent আপনি) | Issue |
|------------------|------------------------------|-------|
| `আপনি ক্লিক কর` | **`আপনি ক্লিক করুন`** | আপনি pronoun + তুমি verb |
| `তোমার পাসওয়ার্ড দিন` | **`আপনার পাসওয়ার্ড দিন`** | তুমি possessive + আপনি verb |
| `তোমার অ্যাকাউন্ট সেভ করুন` | **`আপনার অ্যাকাউন্ট সেভ করুন`** | Mixed possessive |
| `আপনার ফাইল মুছে ফেল` | **`আপনার ফাইল মুছে ফেলুন`** | আপনি possessive + তুমি verb |

**Check EVERY verb, EVERY possessive, EVERY pronoun for consistency.**

### Register auto-detect from source

| Source signal | Target register |
|---------------|-----------------|
| Banking, legal, government, healthcare, enterprise, default product UI | **আপনি (apni)** — respectful, imperative -ুন/-ান |
| Marketing aimed at Gen Z, casual social apps, gaming, friend-to-friend chat | **তুমি (tumi)** — explicit user decision, document it |
| Religious texts (addressing the Divine), poetry, literary translation | তুই (intimate) — only when source matches |

**When in doubt: pick আপনি. It is NEVER wrong for UI.**

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. Script integrity — Bengali script (Eastern Nagari) throughout (severity 2.5)

- All Bengali text in **Bengali script**, NOT romanization, NOT Devanagari (Hindi), NOT Assamese (which differs by two letters).
- **Latin tech identifiers** (Git, API, JSON, URLs, code, file names, placeholders `{var}`, `{{count}}`) MUST stay in Latin script, embedded LTR within LTR Bengali (no bidi complexity since Bengali is also LTR).
- **Conjunct consonants (যুক্তাক্ষর)** must be correct:
  - ক + ষ = **ক্ষ** (kkh / kṣ) — as in পরীক্ষা (exam), লক্ষ্য (goal)
  - জ + ঞ = **জ্ঞ** (gg / jñ) — as in জ্ঞান (knowledge), বিজ্ঞান (science)
  - ন + ত = **ন্ত** — as in অনন্ত (eternal)
  - ত + র = **ত্র** — as in ত্রিভুজ (triangle)
  - ষ + ণ = **ষ্ণ** — as in কৃষ্ণ (Krishna)
  - হ + ম = **হ্ম** — as in ব্রহ্ম (Brahma)
  - শ + চ = **শ্চ** — as in নিশ্চয় (certainly)
  - শ + র = **শ্র** — as in শ্রী, আশ্রয়
  - Common typing errors: writing the conjunct as two separate letters with halant (e.g., ক্‌ষ instead of ক্ষ). Always render as the proper conjunct glyph.
- **Halant / hôshonto (্)** suppresses the inherent vowel — used when a consonant is final or part of a conjunct.
- **Inherent vowel অ (ô)** — every Bengali consonant carries an inherent /ɔ/ sound unless suppressed. So ক alone = "kô," not just "k."
- **Vowel signs (কার চিহ্ন)** attach to consonants in specific positions (some before: ি, কি; some after: া, কা; some above: ে, কে; some below: ু, কু; some around: ো, কো, ৌ, কৌ).

### 2. Chandrabindu (ঁ) vs Anusvara (ং) — different sounds (severity 2.0)

These two nasal markers are NOT interchangeable.

| Marker | Name | Sound | Example |
|--------|------|-------|---------|
| **ঁ** | চন্দ্রবিন্দু (chandrabindu, "moon-dot") | Nasalizes the preceding vowel (~), no /n/ or /ŋ/ consonant | চাঁদ (chãd — moon), কাঁচা (kãcha — raw) |
| **ং** | অনুস্বার (anusvara) | /ŋ/ velar nasal consonant | বাংলা (Baŋla — Bengali), সংগীত (sôŋgit — music) |
| **ঃ** | বিসর্গ (bisarga) | /h/ aspiration, rare in modern Bengali | দুঃখ (duḥkho — sorrow) |

| ✗ Wrong | ✓ Correct | Reason |
|---------|-----------|--------|
| বাংলা spelled বাঁলা | **বাংলা** | "Bengali" uses anusvara (ŋ-sound), not chandrabindu |
| চাঁদ spelled চাংদ | **চাঁদ** | "Moon" has nasalized vowel, not /ŋ/ |
| ইংরেজি spelled ইঁরেজি | **ইংরেজি** | "English (language)" uses anusvara |

### 3. SOV word order — verb at the end (severity 2.0)

Bengali is **Subject-Object-Verb**, unlike English's SVO.

| English (SVO) | ✗ SVO calque | ✓ Bengali SOV |
|---------------|--------------|------------------|
| The user saves the file | ইউজার সেভ করে ফাইল | **ইউজার ফাইল সেভ করে** |
| Click the button to continue | ক্লিক করুন বোতামে চালিয়ে যেতে | **চালিয়ে যেতে বোতামে ক্লিক করুন** OR **চালিয়ে যেতে বোতামটি ক্লিক করুন** |
| I download the file from the server | আমি ডাউনলোড করি ফাইল সার্ভার থেকে | **আমি সার্ভার থেকে ফাইল ডাউনলোড করি** |
| Open settings to change your password | খুলুন সেটিংস পাসওয়ার্ড পরিবর্তন করতে | **পাসওয়ার্ড পরিবর্তন করতে সেটিংস খুলুন** |

**Modifiers and adjuncts (time, place, manner) come BEFORE the verb.** Adjectives come BEFORE the noun (`নতুন ফাইল` — new file).

### 4. Case-marking postpositions — attached WITHOUT space or hyphen (severity 2.5)

Bengali expresses case relations via postpositional suffixes attached directly to nouns. NO space, NO hyphen between noun and postposition.

| Case | Postposition | Example |
|------|--------------|---------|
| Nominative | (none) | ফাইল (file) — subject |
| Accusative / Dative | **-কে** (-ke) | ইউজারকে (to the user), ফাইলটিকে (to the file) |
| Genitive | **-র / -এর** (-r / -er) | ইউজারের (user's), ফাইলের (file's), আমার (my) |
| Locative | **-তে / -এ** (-te / -e) | ফাইলে (in the file), ঘরে (in the room), টেবিলে (on the table) |
| Ablative | **থেকে** (theke — separate word) | সার্ভার থেকে (from the server) |
| Instrumental | **দিয়ে / দ্বারা** (diye / dwara) | চাবি দিয়ে (with the key) |

| ✗ Wrong (space/hyphen) | ✓ Correct (attached) | Issue |
|------------------------|----------------------|-------|
| ফাইল এ | **ফাইলে** | Locative -এ attaches directly |
| ইউজার এর | **ইউজারের** | Genitive -এর attaches directly |
| সিস্টেম-এর | **সিস্টেমের** | NO hyphen for native postposition |
| ফাইল কে | **ফাইলকে** | Accusative -কে attaches directly |
| ফোল্ডার -তে | **ফোল্ডারে** OR **ফোল্ডারেতে** | -তে / -এ attaches without hyphen |
| অ্যাকাউন্ট এ লগইন করুন | **অ্যাকাউন্টে লগইন করুন** | Sign in to the account |

**Exception**: When the noun ends in an English-script word (e.g., `Git`, `API`), insert a hyphen for readability:

| ✓ Acceptable |
|--------------|
| Git-এ পুশ করুন (push to Git) |
| API-তে অনুরোধ পাঠান (send a request to the API) |
| GitHub-এর মাধ্যমে (via GitHub) |

### 5. Classifiers REQUIRED with numbers (severity 2.0)

Bengali requires a **classifier (পরিমাণবাচক / শ্রেণীবাচক)** between numbers and the noun being counted. This is similar to Chinese/Japanese measure words. **Numbers without a classifier sound broken.**

| Classifier | Used for | Example |
|------------|----------|---------|
| **-টি / -টা** | General objects (most common; -টি slightly more formal, -টা more colloquial) | একটি ফাইল (one file), পাঁচটি ফোল্ডার (five folders), দুটো বই (two books — colloquial) |
| **-জন** | Humans (only for people) | একজন ইউজার (one user), পাঁচজন সদস্য (five members) |
| **-খানা / -খানি** | Flat objects, certain household items, sheets of paper, books | একখানা চিঠি (one letter), দুখানা বই (two books — slightly old-fashioned) |
| **-গাছা / -গাছি** | Long thin objects (sticks, ropes, hairs) | একগাছা চুল (one strand of hair) |
| **-টুকু / -টুকুনি** | Small amount, abstract quantity | একটুকু জল (a little water) |
| **-পাটি** | Pairs | একপাটি জুতা (a pair of shoes) |

| ✗ Wrong (missing classifier) | ✓ Correct (with classifier) |
|-------------------------------|------------------------------|
| তিন ফাইল | **তিনটি ফাইল** |
| পাঁচ ইউজার | **পাঁচজন ইউজার** |
| ১০ ভাষা | **১০টি ভাষা** OR **দশটি ভাষা** |
| দুই ফোল্ডার | **দুটি ফোল্ডার** OR **দুটো ফোল্ডার** |
| ৭ সদস্য | **৭ জন সদস্য** |

**Number 1 has a special classifier-fused form**: `এক + টি = একটি` (e-k-ti) is the standard "one [thing]."

**Special: in ICU plural `one` branch, write the noun WITH classifier**: `একটি ফাইল` not `১ ফাইল`.

### 6. Animate vs Inanimate plural marking (severity 2.0)

Bengali distinguishes plural endings by animacy.

| Type | Plural suffix | Example |
|------|---------------|---------|
| **Animate (humans, sometimes higher animals)** | **-রা** (-ra), **-গণ** (-gôn formal), **-বৃন্দ** (-brindo very formal) | ইউজাররা (users), ছাত্ররা (students), নাগরিকগণ (citizens — formal) |
| **Inanimate (objects, things, abstract)** | **-গুলো / -গুলি** (-gulo / -guli; -গুলো colloquial, -গুলি slightly formal) | ফাইলগুলো (files), বইগুলো (books), সমস্যাগুলি (problems) |

| ✗ Wrong | ✓ Correct | Reason |
|---------|-----------|--------|
| ফাইলরা | **ফাইলগুলো** | Files are inanimate → -গুলো |
| ইউজারগুলো | **ইউজাররা** | Users are people → -রা |
| ছাত্রগুলো | **ছাত্ররা** | Students are humans → -রা |
| বইরা | **বইগুলো** | Books are inanimate → -গুলো |
| ত্রুটিরা | **ত্রুটিগুলো** | Errors are inanimate → -গুলো |
| ফোল্ডাররা | **ফোল্ডারগুলো** | Folders are inanimate → -গুলো |

**Note**: For organizations of people personified as collective actors (companies, teams, governments), -রা can be used: `কোম্পানিগুলো` (companies as inanimate orgs) vs `কোম্পানির লোকেরা` (the people at the company).

### 7. Verb agreement — by PERSON and HONORIFIC, not gender (severity 2.0)

Bengali verbs conjugate for:
1. **Person** (1st, 2nd, 3rd)
2. **Honorific level** (intimate, familiar, polite)
3. **Tense / aspect**

But NOT for gender. The same verb form works whether the subject is a man, woman, or neuter object.

**Present tense of করা (to do):**

| Subject | Form | Example |
|---------|------|---------|
| আমি (I, 1st sg) | করি (kôri) | আমি কাজ করি (I work) |
| তুই (you intimate) | করিস (kôris) | তুই কাজ করিস |
| তুমি (you familiar) | কর (kôro) | তুমি কাজ কর |
| আপনি (you polite) | **করেন** (kôren) | আপনি কাজ করেন |
| সে (he/she 3rd) | করে (kôre) | সে কাজ করে |
| তিনি (he/she 3rd polite) | **করেন** (kôren) | তিনি কাজ করেন |
| আমরা (we) | করি (kôri) | আমরা কাজ করি |
| তোমরা (you fam pl) | কর / করো | তোমরা কাজ কর |
| আপনারা (you pol pl) | করেন (kôren) | আপনারা কাজ করেন |
| তারা (they) | করে (kôre) | তারা কাজ করে |
| তাঁরা (they polite) | করেন (kôren) | তাঁরা কাজ করেন |

**Imperative (most common in UI):**

| Subject | Imperative form | Example |
|---------|------------------|---------|
| তুই | কর (kôr) — abrupt | কর! (Do it!) |
| তুমি | কর / করো (kôro) | কর / করো |
| **আপনি (UI DEFAULT)** | **করুন (kôrun)** | **ক্লিক করুন** (Please click) |
| আপনারা | করুন (kôrun) | আপনারা ক্লিক করুন |

| ✗ Wrong (register mismatch) | ✓ Correct | Reason |
|------------------------------|-----------|--------|
| আপনি ক্লিক করো | **আপনি ক্লিক করুন** | আপনি requires -ুন imperative |
| তুমি ক্লিক করুন | **তুমি ক্লিক কর / করো** | তুমি takes -ো not -ুন |
| আপনি কাজ কর | **আপনি কাজ করেন** OR **আপনি কাজ করুন** (imperative) | Present tense for আপনি is -েন |

### 8. Compound verbs with করা (kôra) — most verbs come this way (severity 1.5)

Bengali extensively uses **compound verbs**: a noun (often borrowed English/Sanskrit/Persian) + a "light verb" (করা, হওয়া, দেওয়া, নেওয়া, ফেলা, পড়া, etc.).

| English source | Bengali compound | Light verb |
|----------------|------------------|-------------|
| click | ক্লিক **করা** | করা (to do) |
| save | সেভ **করা** / সংরক্ষণ **করা** | করা |
| delete | ডিলিট **করা** / মুছে **ফেলা** | করা / ফেলা (to complete) |
| upload | আপলোড **করা** | করা |
| download | ডাউনলোড **করা** | করা |
| login | লগইন **করা** | করা |
| be saved | সেভ **হওয়া** | হওয়া (to become / be) |
| be deleted | ডিলিট **হওয়া** | হওয়া |

**Critical rule**: a borrowed noun like "click" alone is incomplete. **You must append the light verb.**

| ✗ Wrong (bare noun) | ✓ Correct (compound) |
|----------------------|----------------------|
| ক্লিক (as a button) | **ক্লিক করুন** |
| সেভ (as a button) | **সেভ করুন** |
| ডাউনলোড | **ডাউনলোড করুন** |

### 9. Completive compound verbs — "done"-ness (severity 1.5)

Bengali distinguishes ongoing action from **completed** action using completive compounds:

| Light verb | Meaning added | Example |
|------------|----------------|---------|
| **করে ফেলা** (kôre phela) | Complete it (decisively, fully done) | সেভ করে ফেলেছি (I've fully saved it), মুছে ফেলেছি (I've deleted it for good) |
| **করে নেওয়া** (kôre neya) | Do it for self / take care of it | পড়ে নিয়েছি (I've read it through), করে নিয়েছি (I've handled it) |
| **করে দেওয়া** (kôre deya) | Do it for someone else | পাঠিয়ে দিয়েছি (I've sent it [to them]), লিখে দিয়েছি (I've written it out [for them]) |
| **হয়ে যাওয়া** (hôye jaôa) | Has become (completion of state change) | সেভ হয়ে গেছে (it's saved [now]), ডাউনলোড হয়ে গেছে (it's downloaded) |

**Critical for UI status messages**: "Saved" / "Done" / "Completed" should use a completive compound, NOT bare past tense.

| ✗ Bare past | ✓ Completive (natural) |
|-------------|------------------------|
| সেভ হয়েছে | **সেভ হয়ে গেছে** (more natural "got saved") |
| মুছে দিয়েছি | **মুছে ফেলেছি** (with completion emphasis) |
| পাঠিয়েছি | **পাঠিয়ে দিয়েছি** (sent it off to someone) |
| ডাউনলোড হয়েছে | **ডাউনলোড হয়ে গেছে** (it's now downloaded) |

For "now in progress" → use continuous **-চ্ছে** form: সেভ **হচ্ছে...** (saving...), লোড **হচ্ছে...** (loading...), পাঠানো **হচ্ছে...** (sending...).

### 10. Religious / regional sensitivity — Bangladesh vs West Bengal (severity 2.0)

Bengali is read by both **Muslim-majority Bangladesh** (~89% Muslim, ~10% Hindu) and **Hindu-majority West Bengal** (~70% Hindu, ~27% Muslim — India's second-largest Muslim state population). The same text must work for both unless explicitly targeting one variant.

**Default for product UI: religion-neutral.** Do NOT inject:

- Islamic phrases (ইনশাল্লাহ "God willing", আলহামদুলিল্লাহ "Praise be to God", মাশাল্লাহ "What God has willed") unless the source already invokes them.
- Hindu phrases (রাম রাম, জয় হিন্দ, ভগবানের কৃপায়) unless the source invokes them.
- Christian phrases (ঈশ্বরের ইচ্ছায়, যিশুর নামে) unless the source invokes them.
- Festival assumptions: Don't say "ঈদের সময়" (during Eid) if you mean "during the holiday season"; don't say "পূজার সময়" (during Durga Puja) if you mean "during the festival." Use **ছুটির সময়** (during holidays) for neutrality.

**Greetings — default neutral:**

| Context | bn-BD natural | bn-IN natural | Pan-Bengali neutral |
|---------|---------------|---------------|---------------------|
| Hello (formal) | আসসালামু আলাইকুম (Muslim) / নমস্কার | নমস্কার | **স্বাগতম** (Welcome) / **হ্যালো** |
| Good morning | শুভ সকাল | শুভ সকাল | শুভ সকাল |
| Welcome back | আবার স্বাগতম | আবার স্বাগতম | আবার স্বাগতম |

**Food metaphors — avoid pork (শূকর) references in bn-BD (haram in Islam) and beef (গরুর মাংস) references for Hindu bn-IN audiences.** Use chicken (মুরগি), fish (মাছ), or vegetarian neutral alternatives in metaphors.

**Christian-origin idioms** (English imports) need to be REWRITTEN, not literally calqued:

| English idiom | ✗ Literal calque | ✓ Culturally adapted Bengali |
|---------------|------------------|-------------------------------|
| holy grail | পবিত্র গ্রেইল | **চূড়ান্ত লক্ষ্য** (ultimate goal) / **পরম প্রাপ্য** |
| cross to bear | বহন করার ক্রুশ | **কষ্টের বোঝা** / **দায়িত্বের ভার** |
| good Samaritan | ভালো শমরীয় | **সহৃদয় ব্যক্তি** / **মহৎ মানুষ** |
| act of God | ঈশ্বরের কাজ | **প্রাকৃতিক দুর্যোগ** (natural disaster — legal) / **দৈব ঘটনা** |
| baptism of fire | আগুনের দীক্ষা | **কঠিন পরীক্ষা** (difficult trial) / **অগ্নিপরীক্ষা** (Bengali equivalent — pure of Sanskrit origin, secular-acceptable) |
| Pandora's box | প্যান্ডোরার বাক্স | (Greek myth, naturalized in formal Bengali) — or **সমস্যার আঁধার** |
| break a leg (theatrical good luck) | পা ভাঙো | **শুভকামনা!** (best wishes!) / **সাফল্য কামনা করি** |
| kill two birds with one stone | এক ঢিলে দুই পাখি (this is already a Bengali idiom) ✓ | **এক ঢিলে দুই পাখি** — works! |

Note: **এক ঢিলে দুই পাখি** is genuinely a Bengali idiom and a good case of where a literal English-Bengali parallel happens to align.

---

## UI Conventions

### Buttons — imperative form (আপনি default)

Bengali buttons use the **imperative -ুন/-ান form** for আপনি. Most are **compound verbs** (noun + করুন).

| English | ✓ Bengali button |
|---------|------------------|
| Save | **সেভ করুন** / সংরক্ষণ করুন |
| Cancel | **বাতিল করুন** |
| Delete | **মুছুন** / **মুছে ফেলুন** / **ডিলিট করুন** |
| Send | **পাঠান** |
| Edit | **সম্পাদনা করুন** / **এডিট করুন** |
| Search | **অনুসন্ধান করুন** / **সার্চ করুন** / **খুঁজুন** |
| Confirm | **নিশ্চিত করুন** |
| Continue | **চালিয়ে যান** / **এগিয়ে যান** |
| Submit | **জমা দিন** |
| Sign in / Log in | **লগইন করুন** / **সাইন ইন করুন** |
| Sign out / Log out | **লগআউট করুন** / **সাইন আউট করুন** |
| Sign up / Register | **সাইন আপ করুন** / **নিবন্ধন করুন** / **রেজিস্ট্রেশন করুন** |
| Next | **পরবর্তী** (next [one]) / **এগিয়ে যান** (move forward) |
| Back | **পিছনে যান** / **ফিরে যান** / **পূর্ববর্তী** |
| Done | **সম্পন্ন** / **হয়ে গেছে** |
| OK | **ঠিক আছে** (literally "it's right") / **OK** |
| Close | **বন্ধ করুন** |
| Open | **খুলুন** |
| Upload | **আপলোড করুন** |
| Download | **ডাউনলোড করুন** |
| Refresh | **রিফ্রেশ করুন** / **রিলোড করুন** |
| Settings | **সেটিংস** |
| Apply | **প্রয়োগ করুন** |
| Reset | **রিসেট করুন** / **পুনরায় সেট করুন** |
| Select all | **সব নির্বাচন করুন** / **সবগুলো বাছুন** |
| Copy | **কপি করুন** / **অনুলিপি করুন** |
| Paste | **পেস্ট করুন** / **আটকান** |
| Cut | **কাট করুন** / **কাটুন** |
| Add | **যোগ করুন** |
| Remove | **সরান** / **সরিয়ে ফেলুন** |
| Help | **সাহায্য** |
| Cancel | **বাতিল করুন** |

### Status messages — continuous aspect (হচ্ছে)

For "in progress" / "loading" states, use the **continuous suffix -চ্ছে** attached to verb stem (3rd person).

| English | ✓ Bengali (continuous) |
|---------|------------------------|
| Loading… | **লোড হচ্ছে…** |
| Saving… | **সেভ হচ্ছে…** / **সংরক্ষণ করা হচ্ছে…** |
| Sending… | **পাঠানো হচ্ছে…** |
| Uploading… | **আপলোড হচ্ছে…** |
| Downloading… | **ডাউনলোড হচ্ছে…** |
| Connecting… | **সংযোগ করা হচ্ছে…** / **কানেক্ট হচ্ছে…** |
| Processing… | **প্রক্রিয়া চলছে…** / **প্রসেস হচ্ছে…** |
| Searching… | **খোঁজা হচ্ছে…** / **সার্চ হচ্ছে…** |
| Please wait | **অনুগ্রহ করে অপেক্ষা করুন** / **দয়া করে অপেক্ষা করুন** |
| Authenticating… | **প্রমাণীকরণ হচ্ছে…** / **অথেন্টিকেট হচ্ছে…** |
| Verifying… | **যাচাই করা হচ্ছে…** |
| Updating… | **আপডেট হচ্ছে…** |
| Syncing… | **সিঙ্ক হচ্ছে…** |

### Completion messages — completive compound (হয়ে গেছে / হয়েছে)

| English | ✓ Bengali |
|---------|-----------|
| Saved | **সেভ হয়ে গেছে** / **সংরক্ষিত হয়েছে** |
| Done | **সম্পন্ন হয়েছে** / **হয়ে গেছে** |
| Translation complete | **অনুবাদ সম্পন্ন হয়েছে** / **অনুবাদ হয়ে গেছে** |
| File uploaded | **ফাইল আপলোড হয়েছে** / **ফাইল আপলোড হয়ে গেছে** |
| Payment successful | **পেমেন্ট সফল হয়েছে** / **পেমেন্ট সম্পন্ন হয়েছে** |
| Sent | **পাঠানো হয়েছে** / **বার্তা পাঠানো হয়েছে** |
| Account created | **অ্যাকাউন্ট তৈরি হয়েছে** |
| Settings updated | **সেটিংস আপডেট হয়েছে** |

### Failed messages — passive with "নি"/"যায়নি"/"ব্যর্থ"

| English | ✓ Bengali |
|---------|-----------|
| Save failed | **সেভ করা যায়নি** / **সংরক্ষণ ব্যর্থ হয়েছে** |
| Upload failed | **আপলোড করা যায়নি** / **আপলোড ব্যর্থ হয়েছে** |
| Translation failed | **অনুবাদ ব্যর্থ হয়েছে** |
| Connection failed | **সংযোগ ব্যর্থ হয়েছে** / **সংযোগ করা যায়নি** |
| File not found | **ফাইল খুঁজে পাওয়া যায়নি** / **ফাইল পাওয়া যায়নি** |
| Login failed | **লগইন ব্যর্থ হয়েছে** / **লগইন করা যায়নি** |
| Network error | **নেটওয়ার্ক ত্রুটি** / **নেটওয়ার্ক সমস্যা** |
| Something went wrong | **কিছু একটা ভুল হয়েছে** / **একটি ত্রুটি ঘটেছে** |

### Empty states — `কোনো X নেই`

| ✗ Bare | ✓ Specific Bengali |
|--------|---------------------|
| খালি | **কোনো ফলাফল পাওয়া যায়নি** (no results found) |
| কিছু নেই | **কোনো ডেটা নেই** / **কোনো তথ্য পাওয়া যায়নি** |
| তালিকা খালি | **তালিকায় কোনো আইটেম নেই** / **তালিকা খালি রয়েছে** |
| ফাইল নেই | **কোনো ফাইল পাওয়া যায়নি** |

### Drag-and-drop — native Bengali verbs preferred

| Action | Native Bengali | Transliteration (less preferred) |
|--------|----------------|----------------------------------|
| drag | **টানুন** (tanun — pull) / **টেনে আনুন** (drag-bring) | ড্র্যাগ করুন |
| drop | **ছাড়ুন** (chharun — release) / **ছেড়ে দিন** | ড্রপ করুন |
| release | **ছেড়ে দিন** | রিলিজ করুন |

Combined: **`ফাইল এখানে টেনে এনে ছাড়ুন`** (Drag the file here and release) — natural Bengali DnD.

### File picker — action-oriented over navigation

| ✗ Calque ("browse") | ✓ Action-oriented |
|----------------------|--------------------|
| ব্রাউজ করুন | **ফাইল বাছাই করুন** (Choose a file) / **ফাইল নির্বাচন করুন** |
| ফাইল ব্রাউজ করুন | **ফাইল বাছুন** / **ফাইল নির্বাচন করুন** |

### Rate / per expressions — প্রতি (not "পার")

| ✗ Calque | ✓ Native Bengali |
|----------|--------------------|
| পার মাস ($10) | **প্রতি মাসে** ($10) / **মাসে $10** |
| পার ইউজার | **প্রতি ইউজার** / **ইউজার প্রতি** / **প্রতি ব্যবহারকারী** |
| পার ফাইল | **প্রতি ফাইল** / **ফাইল প্রতি** |
| পার লাইসেন্স | **প্রতি লাইসেন্স** |

### Quantity expressions

| ✗ Calque | ✓ Native Bengali |
|----------|--------------------|
| +25 ভাষা | **২৫টির বেশি ভাষা** / **২৫টিরও বেশি ভাষা** |
| {count}+ আরো | **আরো {count}টি** / **+{count}** (numeric format OK) |
| উপরে 100 ফাইল | **১০০টির বেশি ফাইল** |

### Error messages — what + next step

Bengali error messages should state **what happened** and **what to do next**.

| ✗ Bare | ✓ With next step |
|--------|------------------|
| ফাইল পাওয়া যায়নি। | **ফাইল পাওয়া যায়নি। অনুগ্রহ করে পথটি যাচাই করুন।** |
| নেটওয়ার্ক ত্রুটি। | **নেটওয়ার্ক ত্রুটি। আবার চেষ্টা করুন।** |
| ইমেইল ঠিকানা অবৈধ। | **ইমেইল ঠিকানাটি অবৈধ। ফরম্যাট যাচাই করুন।** |
| লগইন ব্যর্থ। | **লগইন ব্যর্থ হয়েছে। ইউজারনেম এবং পাসওয়ার্ড যাচাই করুন।** |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Bengali | Notes |
|------|---------|-------|
| Sentence end | **।** (দাঁড়ি / dāṛi — Bengali period) OR `.` (Western period) | Traditional Bengali uses ।; modern UI freely mixes with `.`. Pick one and be consistent within a document. |
| Question mark | **?** | Same as English |
| Exclamation | **!** | Same as English |
| Comma | **,** | Same as English |
| Colon | **:** | Same as English |
| Semicolon | **;** | Same as English |
| Quotation marks | **"..."** (straight, most common) OR **"..."** (curly typographic) | Both used; straight more common in tech. |
| Ellipsis | **...** OR **…** | Either |
| Apostrophe | **'** OR **'** | For transliterating English words |

**দাঁড়ি (।)** is the traditional Bengali full stop. In tech UI and modern writing, both `।` and `.` are acceptable. **Be consistent within a document.**

**No comma before এবং (and) / ও (and) / বা (or)** — same as German rule (and unlike English Oxford comma).

| ✗ With comma | ✓ No comma |
|--------------|------------|
| ফাইল, ফোল্ডার, এবং সেটিংস | **ফাইল, ফোল্ডার এবং সেটিংস** |
| ইংরেজি, বাংলা, বা হিন্দি | **ইংরেজি, বাংলা বা হিন্দি** |

**Comma IS used before যে (that), যদি (if), কারণ (because), কিন্তু (but)** in complex sentences:

| ✓ With comma |
|--------------|
| আমি জানি, যে আপনি ব্যস্ত। |
| ফাইল সেভ করুন, যদি পরিবর্তন থাকে। |
| লগইন ব্যর্থ, কারণ পাসওয়ার্ড ভুল। |

### Numbers — Indian grouping (lakhs / crores)

**Bengali script numerals:** ০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮ ৯ (0-9)

In modern Bengali UI, **Arabic-Indic numerals (0-9) are STANDARD**. Bengali numerals (০-৯) appear in:
- Formal literary text
- Traditional / cultural content
- Educational materials for children
- Government documents (sometimes)
- Religious texts

**For tech product UI: Arabic-Indic numerals (0-9) are the default.** Be **consistent** within a document — never mix `১২৩` and `123` in the same string.

| Context | Preferred numeral |
|---------|--------------------|
| Modern tech UI, app interface | **0-9 (Arabic-Indic)** — default |
| Marketing copy targeting cultural audience | Either, pick one and stay consistent |
| Formal literary / poetic content | **০-৯ (Bengali script)** |
| Mixed Bengali + English text | **0-9 (Arabic-Indic)** for cleaner LTR flow |

**Indian-style number grouping (lakhs and crores) — used in BOTH bn-BD and bn-IN:**

| Number | ✗ Western grouping | ✓ Indian grouping |
|--------|---------------------|---------------------|
| 100,000 | 100,000 | **1,00,000** (one lakh — এক লক্ষ) |
| 1,000,000 | 1,000,000 | **10,00,000** (ten lakh — দশ লক্ষ) |
| 10,000,000 | 10,000,000 | **1,00,00,000** (one crore — এক কোটি) |
| 123,456,789 | 123,456,789 | **12,34,56,789** |

The pattern: first comma after **3 digits** from the right, then every **2 digits** after that. So thousands have a 3-digit group on the right, then lakhs (2-digit groups), then crores (still 2-digit).

**Bengali word for lakhs/crores in copy:**

| Number | Bengali word |
|--------|---------------|
| 1,00,000 | **১ লক্ষ** (eng: 1 lakh) / এক লক্ষ |
| 10,00,000 | **১০ লক্ষ** / দশ লক্ষ |
| 1,00,00,000 | **১ কোটি** / এক কোটি |
| 100 | একশো / একশত |
| 1,000 | এক হাজার |
| 10,000 | দশ হাজার |

**Decimal separator: period (.)** — `3.14`, `99.99`.
**Thousands separator: comma (,)** — using Indian grouping.

### Dates — DD/MM/YYYY

**Standard format**: DD/MM/YYYY (used in both Bangladesh and India)

| Format | Example | Use |
|--------|---------|-----|
| DD/MM/YYYY | **15/01/2024** | Default tech UI |
| DD-MM-YYYY | **15-01-2024** | Acceptable alternative |
| DD MonthName YYYY | **১৫ জানুয়ারি ২০২৪** OR **15 জানুয়ারি 2024** | Long form |
| Bengali calendar (বঙ্গাব্দ) | **১ বৈশাখ ১৪৩১** | Cultural / festival context |

**Bengali month names (Gregorian calendar transliterations):**

| # | English | Bengali |
|---|---------|---------|
| 1 | January | জানুয়ারি |
| 2 | February | ফেব্রুয়ারি |
| 3 | March | মার্চ |
| 4 | April | এপ্রিল |
| 5 | May | মে |
| 6 | June | জুন |
| 7 | July | জুলাই |
| 8 | August | আগস্ট |
| 9 | September | সেপ্টেম্বর |
| 10 | October | অক্টোবর |
| 11 | November | নভেম্বর |
| 12 | December | ডিসেম্বর |

**Bengali calendar (বঙ্গাব্দ / Bāṅlā śôn)** — used alongside Gregorian, especially for cultural events:

| # | Bengali month | Approx Gregorian |
|---|---------------|------------------|
| 1 | বৈশাখ (Boishakh) | mid-Apr to mid-May (Bengali New Year — পহেলা বৈশাখ) |
| 2 | জ্যৈষ্ঠ (Joishtho) | mid-May to mid-Jun |
| 3 | আষাঢ় (Ashaṛh) | mid-Jun to mid-Jul |
| 4 | শ্রাবণ (Shrabôn) | mid-Jul to mid-Aug |
| 5 | ভাদ্র (Bhadrô) | mid-Aug to mid-Sep |
| 6 | আশ্বিন (Ashbin) | mid-Sep to mid-Oct |
| 7 | কার্তিক (Kartik) | mid-Oct to mid-Nov |
| 8 | অগ্রহায়ণ (Ôgrôhayôn) | mid-Nov to mid-Dec |
| 9 | পৌষ (Poush) | mid-Dec to mid-Jan |
| 10 | মাঘ (Magh) | mid-Jan to mid-Feb |
| 11 | ফাল্গুন (Phalgun) | mid-Feb to mid-Mar |
| 12 | চৈত্র (Choitrô) | mid-Mar to mid-Apr |

**Current Bengali year (as of 2026 CE) ≈ 1432-1433 BS (বঙ্গাব্দ)**.

For mainstream tech UI: Gregorian-only is fine. Bengali calendar is opt-in for festival/cultural content.

### Time

- **12-hour with time-of-day words** is most natural in Bengali. 24-hour is acceptable in formal/technical context (e.g., schedules, transit).
- **Time-of-day words** divide the day:

| Period | Bengali | Approx range |
|--------|---------|--------------|
| Morning | **সকাল** (shôkal) | 5 AM - 11 AM |
| Noon / Midday | **দুপুর** (dupur) | 11 AM - 3 PM |
| Afternoon | **বিকাল / বিকেল** (bikal/bikel) | 3 PM - 5 PM |
| Evening | **সন্ধ্যা** (shondhya) | 5 PM - 7 PM |
| Night | **রাত** (rat) | 7 PM - 4 AM |
| Late night / Pre-dawn | **ভোর** (bhor) | 4 AM - 5 AM (also "early morning") |

| English | Bengali |
|---------|---------|
| 9:30 AM | **সকাল ৯:৩০** / **সকাল ৯টা ৩০ মিনিট** |
| 2:00 PM | **দুপুর ২:০০** / **দুপুর ২টা** |
| 6:00 PM | **সন্ধ্যা ৬:০০** |
| 11:00 PM | **রাত ১১:০০** |

### Weekdays — week starts Sunday or Monday (varies)

**Bangladesh**: official work week is **Sunday-Thursday** (Friday-Saturday weekend, Islamic convention). **Week typically starts রবিবার (Sunday).**

**India / West Bengal**: official work week is **Monday-Friday** (Saturday-Sunday weekend, Western convention). **Week can start either রবিবার (Sunday) or সোমবার (Monday) depending on calendar product.**

| English | Bengali | Short form |
|---------|---------|-------------|
| Sunday | **রবিবার** (Robibar) | রবি |
| Monday | **সোমবার** (Sombar) | সোম |
| Tuesday | **মঙ্গলবার** (Môŋgolbar) | মঙ্গল |
| Wednesday | **বুধবার** (Budhbar) | বুধ |
| Thursday | **বৃহস্পতিবার** (Brihôshpotibar) | বৃহস্পতি / বেস্পতি (colloquial) |
| Friday | **শুক্রবার** (Shukrôbar) | শুক্র |
| Saturday | **শনিবার** (Shônibar) | শনি |

### Currency — DIFFERENT in Bangladesh vs India

**THIS IS THE BIGGEST PITFALL when localizing for "Bengali" as a single market.** Bangladesh and India use **different currencies**. Always confirm the target before writing currency symbols.

| Country | Currency | Symbol | Code | Bengali word |
|---------|----------|--------|------|---------------|
| Bangladesh | Bangladeshi Taka | **৳** or **Tk** | **BDT** | **টাকা** (taka) |
| India (West Bengal, Tripura) | Indian Rupee | **₹** | **INR** | **টাকা** (taka — colloquially) or **রুপি** (rupee) |

**Note**: In Bengali colloquial speech in BOTH countries, money is often just called "টাকা" — but the **symbol and ISO code differ**. ALWAYS use the correct symbol matching the target audience's country.

**Currency formatting:**

| Locale | Format | Example |
|--------|--------|---------|
| bn-BD | ৳ before number OR Tk before number | **৳ 1,000** / **Tk 1,000** / **১,০০০ টাকা** |
| bn-IN | ₹ before number | **₹ 1,000** / **₹1,000** / **১,০০০ টাকা** |
| Pan-Bengali tech | Use ISO code | **BDT 1,000** for Bangladesh, **INR 1,000** for India, **USD 10** for international pricing |

**With Indian-grouping (lakhs/crores):**

| Amount | bn-BD | bn-IN |
|--------|-------|-------|
| 1 lakh | **৳ 1,00,000** | **₹ 1,00,000** |
| 1 crore | **৳ 1,00,00,000** | **₹ 1,00,00,000** |

**Subdivision**:
- 1 Taka (টাকা) = 100 পয়সা (poisha) [Bangladesh]
- 1 Rupee (রুপি / টাকা) = 100 পয়সা (poisha) [India]

(Poisha is barely used in practice anymore; both countries have inflation that makes the subunit functionally obsolete.)

### Phone numbers

| Country | Format | Example |
|---------|--------|---------|
| Bangladesh | +880 followed by 10 digits | +880 1234 567890 |
| India | +91 followed by 10 digits | +91 98765 43210 |

---

## Terminology — Core Bengali UI Vocabulary

| English | ✓ Bengali preferred | Notes |
|---------|---------------------|-------|
| user | **ইউজার** (loanword, common) / **ব্যবহারকারী** (native, more formal) | Both acceptable |
| account | **অ্যাকাউন্ট** (common) / **হিসাব** (older, "account/calculation") | অ্যাকাউন্ট for tech UI |
| password | **পাসওয়ার্ড** (loanword) / **গুপ্ত শব্দ** (native, rare) | পাসওয়ার্ড standard |
| settings | **সেটিংস** (loanword) / **সেটিং** (sing.) / **বিন্যাস** (native) | সেটিংস standard |
| dashboard | **ড্যাশবোর্ড** (loanword) / **নিয়ন্ত্রণ ফলক** (native) | ড্যাশবোর্ড most natural |
| email | **ইমেইল** (loanword) / **ই-মেইল** / **ইমেল** | ইমেইল most common |
| link | **লিংক** (loanword) / **সংযোগ** (native) | লিংক standard |
| website | **ওয়েবসাইট** (loanword) | Universal |
| URL | **URL** (keep Latin) / **ওয়েব ঠিকানা** | URL standard |
| folder | **ফোল্ডার** (loanword) | Universal |
| file | **ফাইল** (loanword) | Universal |
| device | **ডিভাইস** (loanword) / **যন্ত্র** (native) | ডিভাইস standard |
| phone | **ফোন** / **মোবাইল** | Both |
| computer | **কম্পিউটার** | Universal |
| application / app | **অ্যাপ্লিকেশন** / **অ্যাপ** | Universal |
| update | **আপডেট করুন** | Loanword standard |
| save | **সেভ করুন** / **সংরক্ষণ করুন** (more formal) | Both acceptable |
| delete | **মুছুন** / **ডিলিট করুন** | Both acceptable |
| upload | **আপলোড করুন** | Loanword standard |
| download | **ডাউনলোড করুন** | Loanword standard |
| sign in / log in | **লগইন করুন** / **সাইন ইন করুন** / **প্রবেশ করুন** (native) | লগইন most common |
| sign up | **সাইন আপ করুন** / **নিবন্ধন করুন** / **রেজিস্ট্রেশন করুন** | সাইন আপ casual, নিবন্ধন formal |
| search | **অনুসন্ধান করুন** / **সার্চ করুন** / **খুঁজুন** | All three acceptable |
| click | **ক্লিক করুন** | Universal |
| share | **শেয়ার করুন** | Loanword standard |
| profile | **প্রোফাইল** | Universal |
| notifications | **নোটিফিকেশন** / **বিজ্ঞপ্তি** (native, formal) | নোটিফিকেশন common |
| privacy | **গোপনীয়তা** (native, preferred) / **প্রাইভেসি** | গোপনীয়তা |
| terms | **শর্তাবলী** / **নিয়মাবলী** | Native |
| support | **সাপোর্ট** / **সহায়তা** (native) | Both |
| help | **সাহায্য** (native, preferred) / **হেল্প** | সাহায্য |
| feedback | **মতামত** (native) / **ফিডব্যাক** | মতামত preferred |
| menu | **মেনু** | Universal |
| home | **হোম** / **প্রথম পাতা** (front page) / **মূল পাতা** | All work |
| logout | **লগআউট করুন** / **সাইন আউট করুন** | লগআউট common |
| browser | **ব্রাউজার** | Universal |
| screen | **স্ক্রিন** / **পর্দা** (native, "screen/curtain") | স্ক্রিন most common |
| keyboard | **কীবোর্ড** | Universal |
| mouse | **মাউস** | Universal |
| API | **API** (keep Latin) | |
| build (software) | **বিল্ড** / **নির্মাণ** | |
| deploy | **ডিপ্লয়** / **স্থাপন** | |
| pipeline | **পাইপলাইন** (keep) | |
| commit (git) | **commit** (keep Latin) | |
| merge | **মার্জ** / **একত্রীকরণ** | |
| repository | **রিপোজিটরি** / **রেপো** | |
| branch (git) | **ব্রাঞ্চ** / **শাখা** | |
| token | **টোকেন** | |
| cache | **ক্যাশ** | |
| log (n.) | **লগ** / **নথি** | |
| sync | **সিঙ্ক** / **সমন্বয়** | |
| webhook | **webhook** (keep Latin) | |
| source of truth | **মূল তথ্যের উৎস** / **প্রামাণিক উৎস** | |

### Native vs loanword — when to prefer which

**Modern Bengali tech UI freely uses English loanwords.** Native Sanskritic alternatives exist for almost every English term but often sound:
- Overly formal (`সংরক্ষণ` for "save" — works in banking, sounds stiff in a chat app)
- Government-document-like (`বিজ্ঞপ্তি` for "notification" — official tone)
- Educational-textbook-like (`ব্যবহারকারী` for "user" — works but academic)

**Rule of thumb**: For consumer / casual tech UI, prefer **loanwords** (ইউজার, সেভ, ডিলিট). For formal/banking/government UI, prefer **native Bengali** (ব্যবহারকারী, সংরক্ষণ, মুছে ফেলুন).

### Tech identifiers — keep in Latin

These MUST stay in Latin/English inside Bengali text:
- Programming languages: Python, JavaScript, Go, Rust, Java
- Frameworks: React, Vue, Angular, Next.js, Django
- Tools: Git, GitHub, Docker, npm, pip
- Protocols: HTTP, REST, GraphQL, OAuth, JWT
- File formats: JSON, XML, CSV, PDF
- Brands: Google, Microsoft, Apple, iPhone, Android
- Commands, file paths, URLs, code snippets, placeholders.

Example: **`আপনার ফাইল সিঙ্ক করতে GitHub-এ লগইন করুন।`** ("Log in to GitHub to sync your files.") — `GitHub` stays Latin, embedded LTR inside LTR Bengali (no bidi issue since Bengali is also LTR).

---

## Calque / Anti-Pattern Blocklist

| ✗ Calque (English-flavored Bengali) | ✓ Native Bengali | Reason |
|--------------------------------------|--------------------|--------|
| এটা সেন্স মেক করে | **এটা যুক্তিসঙ্গত** / **এটা বোধগম্য** | "Makes sense" calque |
| দিনের শেষে | **শেষ পর্যন্ত** / **সব মিলিয়ে** | "At the end of the day" calque |
| ব্রেক নেওয়া (literal "break taking") | **বিরতি নেওয়া** | English borrowing where Bengali word exists |
| টাইম নেওয়া | **সময় নেওয়া** / **সময় লাগা** | English borrowing where Bengali word exists |
| প্লেস করা (literal "place doing") | **রাখা** / **স্থাপন করা** | English calque |
| ইউজার-ফ্রেন্ডলি | **ব্যবহারকারী-বান্ধব** / **সহজবোধ্য** | Compound adjective calque |
| AI-চালিত (with hyphen + suffix) | **AI দ্বারা চালিত** / **কৃত্রিম বুদ্ধিমত্তা চালিত** | Anglicized compound adjective |
| জিরো ডাউনটাইম (zero X marketing calque) | **কোনো ডাউনটাইম ছাড়াই** / **সম্পূর্ণ অবিচ্ছিন্ন** | "Zero X" English marketing pattern |
| পার মাস | **প্রতি মাসে** / **মাসে** | "Per X" calque |
| পার ইউজার | **প্রতি ইউজার** / **ইউজার প্রতি** | "Per X" calque |
| মার্কিন যুক্তরাষ্ট্র (full form in UI) | **আমেরিকা** / **মার্কিন** | Verbose for UI |
| ব্রাউজ করুন (for file picker) | **ফাইল বাছাই করুন** / **ফাইল নির্বাচন করুন** | Action-oriented over navigation |
| ড্র্যাগ করুন | **টানুন** / **টেনে আনুন** | Native verb available |
| ড্রপ করুন | **ছাড়ুন** / **ছেড়ে দিন** | Native verb available |
| মুক্ত করুন (for "release file") | **ছেড়ে দিন** | "Liberate" calque for "release" |
| ফাইল এ (with space before postposition) | **ফাইলে** | Postpositions attach without space |
| সিস্টেম-এর (with hyphen before postposition) | **সিস্টেমের** | Postpositions attach without hyphen |
| বিরতি ছাড়া (for "uninterrupted") | **অবিচ্ছিন্ন** / **অবিরাম** | Native word more compact |
| গবেষণার মতে (literal "according to research") | **গবেষণায়** / **গবেষণা অনুযায়ী** | More natural Bengali |
| খুবই ভালো (intensifier doubled) | **চমৎকার** / **অসাধারণ** | Use Bengali equivalent intensifier |

### Religious-origin idioms (English source) — adapt for Bengali audience

| ✗ Literal Christian idiom | ✓ Bengali-neutral |
|-----------------------------|---------------------|
| ক্রুশ বহন করা (cross to bear) | **কষ্টের বোঝা** / **দায়িত্বের ভার** |
| পবিত্র গ্রেইল (holy grail) | **চূড়ান্ত লক্ষ্য** / **পরম প্রাপ্য** |
| ভালো শমরীয় (good Samaritan) | **সহৃদয় ব্যক্তি** / **মহৎ মানুষ** |
| ঈশ্বরের কাজ (act of God) | **প্রাকৃতিক দুর্যোগ** (legal) / **দৈব ঘটনা** |
| আশীর্বাদ ছদ্মবেশে (blessing in disguise) | **প্রচ্ছন্ন আশীর্বাদ** / **অপ্রত্যাশিত ভালো** |

### Region-flavored idioms — adapt for the OTHER region

| Bangladesh-specific (avoid for bn-IN) | India-specific (avoid for bn-BD) | Pan-Bengali neutral |
|------------------------------------------|-----------------------------------|----------------------|
| পানি | জল | use whichever matches target; pan-neutral: prefer পানি for BD audiences, জল for IN audiences |
| দাওয়াত | নিমন্ত্রণ | নিমন্ত্রণ (more universally understood) |
| গোসল | স্নান | স্নান or be specific |
| মদদ | সাহায্য | **সাহায্য** (universal) |

---

## False Friends — Critical

| Bengali word | Actually means | NOT this | Correct for the English |
|--------------|----------------|----------|--------------------------|
| বিকাল (bikal) | afternoon (3-5 PM specifically) | "evening" generally | "evening" → **সন্ধ্যা** (shondhya) |
| সকাল (shôkal) | morning (5-11 AM) | "early morning" | "early morning / dawn" → **ভোর** (bhor) |
| বছর (bôchhor) | year (calendar/age) | "year" of education program | "academic year" → **শিক্ষাবর্ষ** |
| সম্পাদনা (shômpadôna) | editing (text/file) | "publishing" | "publishing" → **প্রকাশনা** |
| সংকেত (shôŋket) | signal / sign | "code" (computer code) | "code" → **কোড** (kod) |
| পত্রিকা (pôtrika) | newspaper / magazine | "post" (blog post) | "blog post" → **ব্লগ পোস্ট** |
| অভিধান (ôbhidhan) | dictionary | "directory" (filesystem) | "directory" → **ডিরেক্টরি** / **ফোল্ডার** |
| বুদ্ধি (buddhi) | intelligence / wit | "wisdom" alone | "wisdom" → **প্রজ্ঞা** |
| ক্ষমতা (kṣômôta) | power / ability / capacity | "permission" | "permission" → **অনুমতি** |
| পরিষেবা (pôriśeba) | service (formal, often govt) | "service" (informal) | "service" (informal tech) → **সার্ভিস** |
| জিনিস (jinis) | thing / item | "issue" | "issue" → **সমস্যা** / **ইস্যু** |
| কাজ (kaj) | work / job / task | "career" | "career" → **পেশা** / **ক্যারিয়ার** |

Bengali has relatively few false-friend traps with English compared to European languages because most tech vocabulary is openly borrowed rather than mis-mapped.

---

## Custom Sections

### Reduplication for emphasis / distributive meaning

Bengali uses **reduplication** to express emphasis, plurality of variety, or distribution. This is a unique feature absent in English.

| Pattern | Meaning | Example |
|---------|---------|---------|
| Adjective doubled | "various / many of" | **ছোট ছোট ফাইল** (lots of small files / small files of various kinds) |
| Adjective doubled | intensification | **বড় বড় বিল্ডিং** (very large buildings / many big buildings) |
| Noun doubled (with গুলো-) | "all of every kind" | **জায়গায় জায়গায়** (in many places / from place to place) |
| Verb stem doubled | "going on continuously" | **হাসতে হাসতে** (laughing and laughing / while laughing) |
| Color doubled | "of various shades" | **নীল নীল ফুল** (many blue flowers, varied shades) |

**For UI**: reduplication is sparing and contextual. Useful for:

| English | Bengali with reduplication |
|---------|------------------------------|
| various files | **বিভিন্ন ফাইল** / **নানা ধরনের ফাইল** (more standard than ফাইল ফাইল) |
| different settings | **বিভিন্ন সেটিংস** |
| Many small icons | **ছোট ছোট আইকন** |

Reduplication should match a source nuance — don't add it arbitrarily.

### Per vs total — semantic distinction

| Source | ✓ Bengali | Meaning |
|--------|-----------|---------|
| per language (rate) | **প্রতি ভাষায়** / **ভাষা প্রতি** | rate, per-unit |
| for 25 languages (total) | **২৫টি ভাষার জন্য** / **২৫টি ভাষায়** | total scope |
| $5 USD per language | **প্রতি ভাষায় $5** / **ভাষা প্রতি $5** | rate |
| $5 USD for all languages | **সব ভাষার জন্য $5** | total |

### Cost / estimate ordering

Bengali commonly puts **amount first** in price displays:

| ✗ Awkward | ✓ Natural Bengali |
|-----------|---------------------|
| ৫টি ভাষা ২৫ ক্রেডিট | **৫টি ভাষার জন্য ২৫ ক্রেডিট** |
| ১০ ইউজার ৫০ টাকা | **১০ ইউজারের জন্য ৫০ টাকা** |

### UI element references in prose

Use quotation marks for specific UI labels:

| ✗ Compound | ✓ Quoted label |
|------------|-----------------|
| সেভ বোতাম ক্লিক করুন | **"সেভ" বোতামে ক্লিক করুন** |
| সেটিংস ট্যাব খুলুন | **"সেটিংস" ট্যাবটি খুলুন** |
| নাম ফিল্ডে লিখুন | **"নাম" ফিল্ডে লিখুন** |

### Brand names — keep in Latin, no Bengali declension

Foreign brands stay invariant. Postpositions attach via hyphen for readability:

| Construction | Bengali |
|--------------|---------|
| at Google | **Google-এ** / **Google-তে** |
| from GitHub | **GitHub থেকে** |
| via Microsoft | **Microsoft-এর মাধ্যমে** |
| using Slack | **Slack ব্যবহার করে** |

Brand names DO NOT take animate/inanimate plural suffixes (no `Googleগুলো`).

### ICU plural — one / other

Bengali plural system is **simple**: one vs other (no dual, no zero special).

```icu
{count, plural,
  one {একটি ফাইল}
  other {# টি ফাইল}
}
```

Notes:
- `one` (count = 1): use classifier-fused একটি (or একজন for humans).
- `other` (count = 0, 2, 3, ...): use number + classifier.
- ALWAYS include the classifier in both branches.
- For humans, use -জন: `{count, plural, one {একজন ইউজার} other {# জন ইউজার}}`.

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| `{count, plural, one {1 ফাইল} other {# ফাইল}}` | **`{count, plural, one {একটি ফাইল} other {#টি ফাইল}}`** |
| `{count, plural, one {ইউজার} other {ইউজাররা}}` | **`{count, plural, one {একজন ইউজার} other {#জন ইউজার}}`** |

### Honorific 3rd person — তিনি for revered people

For mentioning revered third parties (the boss, the founder, a customer being addressed politely in admin notes), use **তিনি** (3rd person honorific) instead of **সে**.

| English | Familiar | Honorific |
|---------|----------|-----------|
| He/she said | **সে বলেছে** | **তিনি বলেছেন** |
| He/she is here | **সে এখানে আছে** | **তিনি এখানে আছেন** |
| His/her email | **তার ইমেইল** | **তাঁর ইমেইল** (with chandrabindu on possessive) |

The chandrabindu on `তাঁর` (her/his honorific) distinguishes it from `তার` (her/his familiar).

### Bengali numerals (০-৯) vs Arabic-Indic (0-9) — be consistent

| ✗ Mixed | ✓ Consistent |
|---------|---------------|
| ১২ ফাইল আজ 15 জানুয়ারি | **১২টি ফাইল আজ ১৫ জানুয়ারি** OR **12 ফাইল আজ 15 জানুয়ারি** |

Pick one numeral system per document/UI surface and stay consistent. **For mainstream tech UI: Arabic-Indic (0-9) is standard.**

---

## Self-Check Checklist (Run Before Returning Output)

### Script & glyph integrity (auto-fail on miss)

- [ ] **Bengali script throughout** Bengali text (not Devanagari, not Assamese-specific letters ৰ ৱ).
- [ ] **Conjunct consonants (যুক্তাক্ষর) correctly formed** (ক্ষ, জ্ঞ, ন্ত, ত্র, ষ্ণ — not split with halant).
- [ ] **Chandrabindu (ঁ) vs anusvara (ং) correctly chosen** — চাঁদ NOT চাংদ; বাংলা NOT বাঁলা.
- [ ] **Latin tech identifiers preserved** (Git, API, JSON, URLs, `{var}`).
- [ ] **Placeholders intact** (`{var}`, `{{count}}`, `<tag>`) — never translated.

### Grammar (auto-fail on miss)

- [ ] **Register consistency**: all verbs and possessives at SAME honorific level (আপনি throughout for UI).
- [ ] **NO mixed registers** (আপনি + কর is wrong; should be আপনি + করুন).
- [ ] **Postpositions attached without space or hyphen** (ফাইলে not ফাইল এ; ইউজারের not ইউজার এর; ফাইলকে not ফাইল কে).
- [ ] **Exception**: hyphen OK after Latin-script word (Git-এ, API-তে).
- [ ] **Classifiers present with numbers** (একটি ফাইল, পাঁচজন ইউজার — NOT তিন ফাইল, পাঁচ ইউজার).
- [ ] **Animate plural -রা for humans, -গুলো for inanimate** (ইউজাররা, ফাইলগুলো — NOT ইউজারগুলো, ফাইলরা).
- [ ] **Verb agreement matches subject's honorific level** (আপনি → করুন/করেন, NOT কর).
- [ ] **SOV word order** — verb at the end of clause.
- [ ] **Adjective BEFORE noun** (নতুন ফাইল, NOT ফাইল নতুন in attributive use).
- [ ] **Compound verbs complete** (ক্লিক করুন, NOT bare ক্লিক).
- [ ] **Completive compounds for "done" status** (সেভ হয়ে গেছে rather than just সেভ হয়েছে).
- [ ] **Continuous -চ্ছে for "in progress"** (লোড হচ্ছে...).

### Numbers, dates, currency

- [ ] **Numerals consistent** — either all Arabic-Indic (0-9) or all Bengali (০-৯), not mixed.
- [ ] **Indian grouping** for large numbers (1,00,000 not 100,000).
- [ ] **Date format DD/MM/YYYY** (15/01/2024 or ১৫/০১/২০২৪).
- [ ] **Decimal = period, thousands = comma** (Indian grouping).
- [ ] **Currency matches target**: BDT/৳/Tk for Bangladesh, INR/₹ for India.
- [ ] **NEVER use ₹ for Bangladesh or ৳ for India** without explicit pricing-table reason.
- [ ] **Time-of-day word matches the hour** (সকাল 9:00, দুপুর 1:00, বিকাল 4:00, সন্ধ্যা 6:00, রাত 10:00).

### Regional / religious sensitivity (auto-fail on miss)

- [ ] **No religious phrases injected** that aren't in source (no ইনশাল্লাহ, নমস্কার, ঈশ্বরের ইচ্ছায় unless source invokes).
- [ ] **No Christian-origin idioms literally translated** (no পবিত্র গ্রেইল, ক্রুশ বহন করা).
- [ ] **Greetings religion-neutral by default** (স্বাগতম, হ্যালো — not Muslim-only or Hindu-only).
- [ ] **Food metaphors region-safe** (no casual pork references for bn-BD; no casual beef references for Hindu bn-IN context).
- [ ] **Festival assumptions check** — don't assume Eid or Durga Puja universal; use **ছুটি** (holiday) generic.
- [ ] **Variant-specific vocabulary** matches target: পানি/দাওয়াত for bn-BD vs জল/নিমন্ত্রণ for bn-IN — OR explicit pan-neutral.

### UI conventions

- [ ] Buttons use **imperative -ুন/-ান form** (সেভ করুন, পাঠান) — gender-neutral by design (Bengali has no gender).
- [ ] Status messages use **continuous হচ্ছে** form (লোড হচ্ছে...).
- [ ] Completion uses **completive compound** (সেভ হয়ে গেছে).
- [ ] Failed uses **passive negative** (সেভ করা যায়নি / ব্যর্থ হয়েছে).
- [ ] Empty state: **কোনো X নেই** / **কোনো X পাওয়া যায়নি**.
- [ ] File picker: **বাছাই করুন** / **নির্বাচন করুন** — not ব্রাউজ করুন.
- [ ] Drag-drop: **টানুন** / **ছাড়ুন** — native verbs preferred over ড্র্যাগ / ড্রপ.
- [ ] Rate expressions use **প্রতি** (not পার): প্রতি মাসে, প্রতি ইউজার.
- [ ] Error messages include **next step** (what + what to do).

### Naturalness

- [ ] **No English calques** (no এটা সেন্স মেক করে, দিনের শেষে, পার মাস).
- [ ] **No bare ICU `one` branch without classifier** (একটি ফাইল not just 1 ফাইল).
- [ ] **No animate/inanimate confusion** (ইউজাররা for users, ফাইলগুলো for files).
- [ ] **Loanword vs native balance** matches register (loanwords for casual UI, native for formal).
- [ ] **Comma rules**: no comma before এবং / ও / বা; YES comma before যদি / কারণ / যে / কিন্তু.
- [ ] **Period choice consistent** (। OR . throughout, not mixed).
- [ ] **Established Bengali term used** where it exists (সাহায্য for help, ব্রাউজার for browser).
- [ ] **NO Hindi-isms** (no Devanagari letters mistakenly used; no Hindi-grammar gender agreement).

---

## Worked Example 1 — Standard UI (pan-Bengali neutral, tech product)

**Source:**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register**: neutral product UI → **আপনি** (apni respectful).

**Variant**: pan-Bengali neutral (English loanwords for tech terms).

**Translation:**

> আবার স্বাগতম! আপনার অ্যাকাউন্টে ৩টি নতুন ফাইল রয়েছে। সেগুলো পর্যালোচনা করতে **চালিয়ে যান** ক্লিক করুন অথবা এখানে থাকতে **বাতিল করুন** ক্লিক করুন। আপনার পরিবর্তনগুলো সেভ হচ্ছে…

**Why this works:**
- `আবার স্বাগতম` — "welcome again" (religion-neutral; works for both Muslim BD and Hindu/secular IN audiences).
- `আপনার অ্যাকাউন্টে` — আপনি possessive + locative postposition attached without space (অ্যাকাউন্ট + -এ = অ্যাকাউন্টে).
- `৩টি নতুন ফাইল` — **classifier টি included**; adjective নতুন BEFORE noun; SOV friendly.
- `রয়েছে` — formal "exists/has" for আপনি register (rather than আছে which would also be acceptable).
- `সেগুলো পর্যালোচনা করতে` — inanimate plural -গুলো on demonstrative; infinitive purpose clause -তে.
- `চালিয়ে যান` — imperative for আপনি (-ান ending).
- `বাতিল করুন` — compound verb (বাতিল + করুন).
- `পরিবর্তনগুলো` — inanimate plural -গুলো.
- `সেভ হচ্ছে…` — continuous aspect (হচ্ছে) for "saving in progress."
- Numerals all Bengali (৩) consistent — could also be all 3, but mixing must not happen.
- Punctuation: period at end, `…` for ongoing action.

---

## Worked Example 2 — Religion-sensitive marketing copy

**Source:**

> Reaching zero emissions is the holy grail for sustainability — but it's a cross to bear for many companies. Don't worry, we'll be your good Samaritan.

**✗ Wrong (literal Christian idioms):**

> জিরো এমিশনে পৌঁছানো হলো স্থায়িত্বের পবিত্র গ্রেইল — কিন্তু এটি অনেক কোম্পানির জন্য বহন করার ক্রুশ। চিন্তা করবেন না, আমরা আপনার ভালো শমরীয় হব।

**✓ Right (culturally adapted, religion-neutral):**

> জিরো এমিশনে পৌঁছানো হলো স্থায়িত্বের চূড়ান্ত লক্ষ্য — কিন্তু এটি অনেক কোম্পানির জন্য কঠিন দায়িত্ব। চিন্তা করবেন না, আমরা আপনাকে এই পথে সাহায্য করব।

**Adaptations:**
- `পবিত্র গ্রেইল` → `চূড়ান্ত লক্ষ্য` (ultimate goal — religion-neutral).
- `বহন করার ক্রুশ` → `কঠিন দায়িত্ব` (a difficult responsibility — neutral).
- `ভালো শমরীয়` → `এই পথে সাহায্য করব` ("we will help you on this path" — drops the biblical reference entirely).
- `চিন্তা করবেন না` — আপনি register, "don't worry" plain.
- Note: avoided injecting `ইনশাল্লাহ` (Muslim) or any Hindu deity reference to stay neutral.

---

## Worked Example 3 — Bangladesh vs India variant choice

**Source:**

> Add ₹100 to your wallet to unlock premium features. Need help? Contact our support team.

**If bn-BD target (Bangladesh):**

> প্রিমিয়াম ফিচার আনলক করতে আপনার ওয়ালেটে ৳১০০ যোগ করুন। সাহায্য প্রয়োজন? আমাদের সাপোর্ট টিমের সাথে যোগাযোগ করুন।

**If bn-IN target (India):**

> প্রিমিয়াম ফিচার আনলক করতে আপনার ওয়ালেটে ₹১০০ যোগ করুন। সাহায্য প্রয়োজন? আমাদের সাপোর্ট টিমের সাথে যোগাযোগ করুন।

**Notice:**
- **The text body is identical.** The pan-Bengali shared vocabulary handles both.
- **Only the currency symbol differs**: ৳ for BD, ₹ for IN.
- Both use Bengali numerals consistently.
- `যোগাযোগ করুন` (contact, lit. "make connection") — same in both.

---

## Worked Example 4 — Status, classifier, and animacy

**Source:**

> 5 users are uploading 12 files. Please wait.

**Translation:**

> ৫ জন ইউজার ১২টি ফাইল আপলোড করছেন। অনুগ্রহ করে অপেক্ষা করুন।

**Why:**
- `৫ জন ইউজার` — **-জন classifier for humans** (5 users).
- `১২টি ফাইল` — **-টি classifier for general objects** (12 files).
- `আপলোড করছেন` — continuous aspect (-ছেন) + আপনি/আপনারা register suffix (-েন) for the plural human subject "users."
- `অনুগ্রহ করে অপেক্ষা করুন` — polite "please wait" for আপনি register (অনুগ্রহ করে = please; অপেক্ষা করুন = wait).
- SOV: subject (৫ জন ইউজার) → object (১২টি ফাইল) → verb (আপলোড করছেন).

---

## Worked Example 5 — ICU plural with classifier

**Source ICU:**

```icu
You have {count, plural, one {# new message} other {# new messages}}.
```

**Bengali expansion:**

```icu
আপনার {count, plural,
  one {একটি নতুন বার্তা}
  other {#টি নতুন বার্তা}
} রয়েছে।
```

**Notes:**
- `one`: `একটি নতুন বার্তা` — **classifier-fused একটি** for "one [item]"; adjective নতুন before noun; বার্তা (inanimate, no plural marker because count=1).
- `other`: `#টি নতুন বার্তা` — number + classifier -টি; adjective বার্তা stays singular **because Bengali tends to omit plural marker after explicit numeric count** (the classifier already signals the count). This is unlike English where "5 messages" requires plural -s.
- `আপনার ... রয়েছে` — আপনি possessive + formal "has/exists."
- Period at end with traditional `।` (could also be `.`).

---

## Worked Example 6 — Date and currency, Bengali calendar overlay

**Source (cultural / festival context, bn-BD):**

> Order before 15 January 2026 to receive your Pohela Boishakh gift box. Total: ₹500 (free shipping).

**bn-BD translation (with Bengali calendar reference):**

> পহেলা বৈশাখের উপহার বাক্স পেতে ১৫ জানুয়ারি ২০২৬ (২ মাঘ ১৪৩২) এর আগে অর্ডার করুন। মোট: ৳৫০০ (ফ্রি শিপিং)।

**Notes:**
- `পহেলা বৈশাখ` (Pohela Boishakh — Bengali New Year, mid-April) is universally recognized in both bn-BD and bn-IN as a cultural festival.
- Gregorian date `১৫ জানুয়ারি ২০২৬` with Bengali numerals; Bengali calendar `২ মাঘ ১৪৩২` in parentheses (১০ মাঘ ১৪৩২ is approximate — adjust if precise calendar lookup matters).
- **Currency corrected from ₹ in source to ৳** because this is bn-BD. If keeping ₹ (e.g., the source was for India and we're translating for Indian Bengalis), use ₹.
- `অর্ডার করুন` — compound verb imperative for আপনি.
- `ফ্রি শিপিং` — loanword OK for casual e-commerce; native would be `বিনামূল্য পরিবহন`.

---

## When in Doubt

1. **Default to আপনি (apni) register.** It's never wrong for UI.
2. **If you wrote a verb without an explicit classifier-fused একটি or counter -টি/-জন,** add one — Bengali requires classifiers with numbers.
3. **If you used -গুলো for humans or -রা for objects,** flip them — animate vs inanimate is critical.
4. **If you wrote `ফাইল এ` or `ইউজার এর` with a space,** delete the space — postpositions attach directly.
5. **If you mixed আপনি with তুমি verbs/possessives,** unify to আপনি throughout.
6. **If you used ₹ for a Bangladesh audience or ৳ for an Indian audience,** flip the currency — Bangladesh = BDT/৳, India = INR/₹.
7. **If you injected religious phrasing (ইনশাল্লাহ, নমস্কার, ঈশ্বরের ইচ্ছায়) that wasn't in source,** remove it — default neutral.
8. **If you translated a Christian-origin idiom literally (পবিত্র গ্রেইল, ক্রুশ বহন),** rewrite it culturally — adapt to a religion-neutral Bengali expression.
9. **If you wrote `চাংদ` or `বাঁলা` (wrong nasal markers),** fix to `চাঁদ` / `বাংলা` — chandrabindu (ঁ) vs anusvara (ং) are different sounds.
10. **If you mixed Bengali (১২৩) and Arabic-Indic (123) numerals in the same string,** pick one and standardize.
11. **If a sentence reads SVO (English word order),** flip to SOV — verb at the end.
12. **If you bare-translated "click" or "save" without the light verb,** add করুন — Bengali compound verbs are mandatory.
13. **If you used `পার মাস` or `পার ইউজার`,** flip to `প্রতি মাসে` / `প্রতি ইউজার` — native rate expression.
14. **If you confused Bengali with Hindi or Assamese,** check the script: Bengali script has no ৰ (Assamese r); Bengali has no Devanagari letters (Hindi); Bengali পানি vs Hindi पानी (different scripts entirely).
15. **If the user said "Bengali" without specifying variant,** ask **bn-BD or bn-IN or pan-Bengali neutral** — the lexical and currency differences matter.
