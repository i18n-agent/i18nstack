---
name: localize-fa
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Persian / Farsi (فارسی) for Iran (fa-IR) or Afghanistan as Dari (fa-AF). Persian is an Iranian Indo-European language — NOT Arabic. Despite using the Perso-Arabic script and many Arabic loanwords, Persian has SOV word order (Arabic is VSO), NO grammatical gender (Arabic has masc/fem on everything), NO dual number (Arabic has dual), simple two-form CLDR plurals one/other (Arabic has zero/one/two/few/many/other), and the defining EZAFE construction (-e linker, کتابِ من = book-of-mine = my book) which Arabic does not have. Critical features: 4 extra letters NOT in Arabic (پ چ ژ گ), Persian ی (U+06CC) NOT Arabic ي (U+064A), Persian ک (U+06A9) NOT Arabic ك (U+0643), ZWNJ U+200C inside compound words (می‌رود NOT می رود and NOT میرود — half-space matters), Persian numerals ۰۱۲۳۴۵۶۷۸۹ preferred over Arabic-Indic ٠١٢٣٤٥٦٧٨٩, Solar Hijri Jalali calendar (1402-1403 SH ≈ 2024 CE) with month names فروردین/اردیبهشت/خرداد/…, week starts on شنبه (Saturday), Toman تومان in everyday use (officially Rial ریال), شما formal vs تو informal register, Persian punctuation ؟ ، ؛ but with «...» guillemets (no spaces inside), را definite-direct-object marker, singular noun after numbers (پنج فایل = five file, NOT پنج فایل‌ها), native verb preference (بکشید NOT دراگ کنید, ذخیره NOT سیو). Iran is Shia-majority — religious sensitivity matters but constitutional minorities (Christians, Jews, Zoroastrians) exist; Western Christian-origin idioms must be culturally re-conceptualized. Tajik (fa-TJ Cyrillic script) is OUT OF SCOPE for this skill."
---

# Localize: Persian / Farsi (fa → فارسی)

## Scope & Variants

Persian is the heritage language of a continuous civilization stretching from western China to the Caucasus. It is one of the world's oldest continuously-attested literary languages (Old Persian → Middle Persian / Pahlavi → New Persian since the 9th century CE). Today it is spoken by ~110 million people across Iran, Afghanistan, and Tajikistan, with significant diaspora in the Gulf, Europe, and North America.

**This skill covers the Perso-Arabic-script written language.** Tajik (which writes Persian in modified Cyrillic) is **out of scope**.

| Locale | Name | Native name | Where | Default register |
|--------|------|-------------|-------|------------------|
| `fa` / `fa-IR` | Iranian Persian (standard) | فارسی / فارسی ایران | Iran (~85M speakers) | Formal شما |
| `fa-AF` | Dari | دری / فارسی دری | Afghanistan (~15M speakers) | Formal شما (slightly more conservative) |
| `fa-TJ` | Tajik | тоҷикӣ / تاجیکی | Tajikistan (Cyrillic script) | **Out of scope** |

**Default for general UI / international audiences: `fa-IR`** (Iranian Persian standard, Tehran-based modern register). It is mutually intelligible with Dari in written form; most differences are in pronunciation and a few lexical items.

### fa-IR vs fa-AF (Dari) — what actually differs in writing

The two are the **same written language** for ~95% of UI copy. Differences appear mainly in:

| Concept | fa-IR (Iran) | fa-AF (Dari, Afghanistan) |
|---------|--------------|--------------------------|
| Currency | تومان / ریال | افغانی (afghani) |
| University | دانشگاه | پوهنتون |
| Faculty/college | دانشکده | پوهنځی |
| Hospital | بیمارستان | شفاخانه |
| Bicycle | دوچرخه | بایسکل |
| Airport | فرودگاه | میدان هوایی |
| Office | دفتر / اداره | دفتر / دفترکار |
| Calendar | Solar Hijri (Jalali) — Persian-named months فروردین… | Solar Hijri — but month names use **Arabic-origin** zodiac names (حمل، ثور، جوزا، سرطان، اسد، سنبله، میزان، عقرب، قوس، جدی، دلو، حوت) |
| Weekend | جمعه (Friday only) — شنبه is workday | پنج‌شنبه + جمعه |
| Lexical loanwords | More French/English loans (سیمان، آپارتمان، تاکسی) | More Pashto/Arabic loans alongside Persian |
| Verb endings (spoken) | -ad (می‌رود = miravad in Iran often miravad → "mire" colloquially) | More conservative, closer to written form |

**Default to fa-IR.** If the user requests fa-AF/Dari, switch the lexical items above and use Dari month names.

### When the target locale is unspecified

If the user requests "Persian" or "Farsi" without specifying region, ask once:

> Which Persian variant should I target?
>
> - **`fa-IR` Iranian Persian** — Recommended. Default for international/general use. Months: فروردین، اردیبهشت… Currency: تومان/ریال.
> - **`fa-AF` Dari (Afghanistan)** — Pohantoon/shafakhana vocabulary, Arabic-zodiac month names (حمل، ثور…), afghani currency.

Default to `fa-IR` if no answer.

---

## Identity Guardrail — Persian is NOT Arabic

This is the single most important section of this skill. Persian is an **Iranian Indo-European** language. Arabic is an **Afro-Asiatic Semitic** language. They are as related as English and Hindi — distant cousins in the global Indo-European family vs an entirely different family.

The two languages **share script and vocabulary** (Persian adopted the Perso-Arabic script in the 9th century and absorbed ~30-40% Arabic loanwords for religion, law, and high culture), but their **grammars are completely different**:

| Feature | Persian (Indo-European, Iranian) | Arabic (Afro-Asiatic, Semitic) |
|---------|----------------------------------|--------------------------------|
| **Word order** | **SOV** (Subject-Object-Verb) — verb at end | **VSO** (Verb-Subject-Object) preferred |
| **Grammatical gender** | **NONE** — no masculine/feminine on nouns or verbs | Masculine + feminine on every noun, adjective, verb, pronoun |
| **Number system** | Singular + plural | Singular + **dual** + plural (3 numbers) |
| **CLDR plural categories** | **2** — one/other (and `one` and `other` often look identical) | **6** — zero/one/two/few/many/other |
| **Noun-after-number** | **Stays singular** (پنج فایل = "five file") | Changes by count band (3-10 plural genitive, 11-99 sg. accusative tanween, 100+ sg. genitive) |
| **Defining grammar feature** | **EZAFE** (-e linker connecting noun + modifier) | **IDAFA** (construct state, opposite direction: possessor follows possessed) |
| **Verb morphology** | Conjugates for person + number (NOT gender). Compound verbs (noun + کردن) extremely common | Conjugates for person + number + **gender** + case (nom/acc/gen). Root-and-pattern morphology |
| **Definite article** | NONE (definiteness shown by context, را marker, or demonstratives) | ال prefix |
| **Letters specific to language** | **پ چ ژ گ** (4 letters NOT in Arabic) | ث ح خ ذ ض ظ ع (kept in Persian for Arabic loanwords but pronounced differently) |
| **Letter ی** | U+06CC (no dots beneath in any form) | ي U+064A (dots beneath in initial/medial/isolated) |
| **Letter ک** | U+06A9 (no hamza-like tail) | ك U+0643 (with tail in isolated form) |
| **Numerals** | ۰۱۲۳۴۵۶۷۸۹ (Persian) preferred | ٠١٢٣٤٥٦٧٨٩ (Arabic-Indic) traditional, or Western 0-9 |
| **Religious framing** | Shia-majority Iran (~90%) + Sunni Afghanistan; significant Zoroastrian heritage and minority Christians/Jews/Baha'is | Sunni-majority overall; some Shia regions (Iraq, Lebanon, Bahrain) |

**Concrete contrast — "The new files were saved":**

| Language | Sentence | Word-by-word |
|----------|----------|--------------|
| English | The new files were saved. | The new files were saved. |
| Persian | فایل‌های جدید ذخیره شدند. | files-the new saved became (SOV, no gender, ezafe ‍-e‍ connects فایل‌ها + جدید). |
| Arabic | حُفِظت الملفات الجديدة. | was-saved-fem.sg the-files the-new-fem.sg (VSO, non-human plural takes fem. sg. agreement). |

**Mistakes that auto-fail:**

- Writing Arabic ي where Persian ی belongs (`ميكنيد` instead of `می‌کنید`)
- Writing Arabic ك where Persian ک belongs (`كتاب` instead of `کتاب`)
- Forgetting ZWNJ in compound forms (`میکنید` or `می کنید` instead of `می‌کنید`)
- Putting adjective before noun, Arabic-IDAFA-style or English-style (`جدید فایل` instead of `فایل جدید`)
- Adding Arabic-style gender agreement (`فایل جدیده` instead of `فایل جدید` — Persian has no feminine adjective form)
- Using Arabic-style dual (`دو فایلان` — Persian has no dual; just `دو فایل`)
- Importing Arabic ICU six-category plurals into Persian (Persian needs only `one` + `other`)
- Calling Persian "a dialect of Arabic" (it is not — it predates Arabic literature by centuries and belongs to a different language family)

When in doubt: **Persian is Iranian; Arabic is Semitic. They share a script, not a grammar.**

---

## Register — شما (formal) vs تو (informal)

Persian distinguishes two registers via second-person pronoun + verb ending. **Software UI default is formal شما** throughout.

| Register | Pronoun | "You save" | "Your file" | "Please click" | Use case |
|----------|---------|-----------|-------------|----------------|----------|
| **شما (formal/plural — DEFAULT)** | شما | ذخیره می‌کنید | فایل شما / فایلتان | لطفاً کلیک کنید | UI, business, news, formal address, any unknown audience |
| **تو (informal singular)** | تو | ذخیره می‌کنی | فایلت | کلیک کن | Close friends, family, children, casual chat apps, intimate marketing |

**Hard rules:**

1. **Software UI uses شما — always.** This is non-negotiable for product copy aimed at general users.
2. **Never mix شما and تو in the same file.** All verb endings, pronouns, and possessive suffixes must agree.
3. **شما is also the polite plural** (used to address multiple people). It is the only safe default for unknown audience.
4. **تو is intimate** — use only when the source text is explicitly casual (informal tone of voice, "Hey!", chat-app messaging, children's product, dating app personal voice).

### Verb ending table (present tense, "do/does")

| Person | شما-form (formal) | تو-form (informal) |
|--------|-------------------|---------------------|
| I do | می‌کنم (mikonam) | می‌کنم (same) |
| You do | **می‌کنید** (mikonid) | **می‌کنی** (mikoni) |
| He/she/it does | می‌کند (mikonad) | می‌کند (same) |
| We do | می‌کنیم (mikonim) | می‌کنیم (same) |
| You (pl.) do | می‌کنید (mikonid) | می‌کنید (same — also formal sg.) |
| They do | می‌کنند (mikonand) | می‌کنند (same) |

### Possessive suffix table

| English | شما-form (UI default) | تو-form (informal) |
|---------|-----------------------|---------------------|
| my file | فایل من / فایلم | فایل من / فایلم |
| your file | **فایل شما / فایلتان** | **فایلت** |
| his/her file | فایل او / فایلش | فایل او / فایلش |
| our file | فایل ما / فایلمان | فایل ما / فایلمان |
| your (pl.) file | فایل شما / فایلتان | فایل شما / فایلتان |
| their file | فایل آن‌ها / فایلشان | فایل آن‌ها / فایلشان |

### Register auto-detection from source

| Source signal | Target register |
|---------------|-----------------|
| Neutral product/UI prose (`Click to save`, `Your file was uploaded`) — **DEFAULT** | **شما formal** — لطفاً کلیک کنید, فایل شما بارگذاری شد |
| Contractions, exclamations, casual lexicon (`Hey!`, `Let's…`, emoji-heavy) | شما formal still recommended, but soften — drop لطفاً in buttons, allow short status forms |
| Legal/financial/very-formal (terms of service, banking, government) | شما formal + elevated vocabulary (یُرجی, خواهشمندیم, با احترام, جناب/خانم titles) |
| Children's product, chat-app personal voice, intimate marketing | **تو informal** — but be absolutely sure this is the brand voice |

**Hard rule: when in doubt, use شما.** Defaulting to formal is always safe; defaulting to informal can offend.

---

## Critical Hard Rules

### 1. EZAFE construction — the defining Persian grammatical feature (severity 2.5)

Ezafe (اضافه, literally "addition") is a short unstressed vowel **-e** (or **-ye** after a vowel) that links a noun to its modifier, possessor, or descriptor. It is the single most distinctive feature of Persian grammar.

**Form:**

- After a consonant: pronounced **-e**, often unwritten (sometimes shown with کسره ◌ِ for clarity).
- After a vowel (especially ـه silent or ـا or ـو): pronounced **-ye**, written explicitly as **ـۀ** or **ـه‌ی** or **ی** depending on convention.

**Word order: head noun FIRST, then modifier — opposite of English.**

| Pattern | Example | Pronunciation | Meaning |
|---------|---------|---------------|---------|
| noun + adjective | فایل جدید | fâyl-**e** jadid | (file-**of** new =) new file |
| noun + possessor noun | تنظیمات کاربر | tanzimât-**e** kâr-bar | (settings-**of** user =) user settings |
| noun + possessor pronoun | کتاب من | ketâb-**e** man | (book-**of** me =) my book |
| noun ending in vowel + modifier | خانهٔ بزرگ / خانه‌ی بزرگ | khâne-**ye** bozorg | (house-**of** big =) big house |
| chain | اسم کاربر جدید | esm-**e** kâr-bar-**e** jadid | (name-of user-of new =) new user's name |

**Critical contrasts:**

| ✗ Wrong (English/Arabic order) | ✓ Correct (Persian ezafe order) | Why |
|--------------------------------|---------------------------------|-----|
| جدید فایل | **فایل جدید** | Noun must come FIRST |
| کاربر تنظیمات | **تنظیمات کاربر** | Possessed (settings) FIRST, possessor (user) SECOND |
| من کتاب | **کتاب من** | Possessed FIRST |
| نو خانه | **خانهٔ نو** | Vowel-ending noun → write ـۀ or ـه‌ی, not just space |

**ezafe vs Arabic idafa — opposite direction:**

In **Arabic idafa**, `كتاب الرجل` = "book the-man" = "the man's book" — possessed first, possessor second WITHOUT a linker, and the first noun drops `ال`.

In **Persian ezafe**, `کتابِ مرد` = "book-e-man" = "the man's book" — possessed first, possessor second WITH the linker -e.

The order is the same, but Persian REQUIRES the linker (audibly), and Persian does NOT drop the article (Persian has no article).

**When the ezafe is sometimes written:**

- For clarity in formal/educational text: explicit kasra ◌ِ on the head noun (`کتابِ من`).
- After ـه silent: **ـۀ** (one character, with hamza-like mark) or **ـه‌ی** (two-character with ZWNJ + ی). Both are accepted; ـۀ is more traditional, ـه‌ی is more modern/common in software.
- After ـی or vowels: just **ی** appended (`دانشجویی بزرگ` → ezafe is implicit in pronunciation).

**For UI translation: write the words in correct head-first order. Do NOT add diacritics (kasra) to UI strings unless the source explicitly uses them.** Modern Persian software omits the kasra and lets the reader infer ezafe from context.

### 2. ZWNJ (Zero-Width Non-Joiner, U+200C) — the half-space (severity 2.5)

Persian uses a special invisible character — the **half-space** or **نیم‌فاصله** (nim-fâsele) — between certain morphemes to:

- Prevent letter ligature (so two adjacent letters don't visually connect).
- Mark a compound boundary inside what is conceptually one word.
- Distinguish prefixed verbs from separate words.

**ZWNJ is REQUIRED in these contexts (auto-fail if missing or replaced by full space):**

| Context | ✗ Wrong (no space) | ✗ Wrong (full space) | ✓ Correct (ZWNJ) |
|---------|--------------------|-----------------------|------------------|
| می- present-tense prefix | میرود | می رود | **می‌رود** (is going) |
| می- with negation | نمیخواهم | نمی خواهم | **نمی‌خواهم** (I don't want) |
| ها plural suffix | فایلها | فایل ها | **فایل‌ها** (files) |
| ها on consonant-ending nouns | کتابها | کتاب ها | **کتاب‌ها** (books) |
| تر comparative | بزرگتر | بزرگ تر | **بزرگ‌تر** (bigger) |
| ترین superlative | بزرگترین | بزرگ ترین | **بزرگ‌ترین** (biggest) |
| ای indefinite suffix | فایلای | فایل ای | **فایل‌ای** (a file) — rare, usually فایلی |
| Compound words | خوشحال | (varies) | خوش‌حال or خوشحال (both accepted) |
| Numbered compound | پنجشنبه | پنج شنبه | **پنج‌شنبه** (Thursday) |

**Why this matters technically:**

- Without ZWNJ, `می` + `رود` written as `میرود` looks visually different — the م + ی would attempt to ligate with the next ر, producing an awkward shape.
- With a full space, `می رود` would treat می and رود as **separate words**, which is grammatically wrong (می- is a verbal prefix, not an independent word).
- The ZWNJ produces the correct visual rendering AND the correct semantic word boundary.

**Producing ZWNJ in software:**

- Unicode U+200C
- HTML entity: `&zwnj;`
- Persian keyboards: Shift+Space (Iranian standard layout) or Ctrl+Shift+2 (some layouts)
- Often invisible in source code — use a Persian-aware editor (VSCode renders it as a narrow dotted box).

**Common QA bug:** translation tools that "normalize whitespace" can strip ZWNJ, breaking every present-tense verb in the file. Always check that your translation pipeline preserves U+200C.

### 3. Direct Object Marker را (severity 2.0)

When a direct object is **definite** (specific, known), Persian marks it with the postposition **را** placed AFTER the noun phrase.

**Rule:** definite direct object → add را; indefinite direct object → no را.

| English | Persian | را used? | Why |
|---------|---------|----------|-----|
| Save **the file**. | فایل را ذخیره کنید. | ✓ | Specific file |
| Save **a file**. | فایلی ذخیره کنید. | ✗ | Indefinite (suffix ـی marks indefinite) |
| Delete **this account**. | این حساب را حذف کنید. | ✓ | Demonstrative → definite |
| Delete **an account**. | حسابی حذف کنید. | ✗ | Indefinite |
| Click **the button**. | روی دکمه کلیک کنید. | ✗ (with روی) | Indirect object via preposition روی |
| Click **the button** (transitive). | دکمه را فشار دهید. | ✓ | Direct object |

**Critical context — را goes AFTER the entire noun phrase, including ezafe modifiers:**

| ✗ Wrong placement | ✓ Correct placement |
|--------------------|---------------------|
| فایل را جدید ذخیره کنید | **فایل جدید را ذخیره کنید** |
| تنظیمات را کاربر تغییر دهید | **تنظیمات کاربر را تغییر دهید** |
| نام را کاربر جدید وارد کنید | **نام کاربر جدید را وارد کنید** |

**Common error: omitting را with definite objects.** Translators with English-source intuition forget را because English has no equivalent marker. `فایل ذخیره کنید` is grammatically marked — it means "save A file" (indefinite), not "save THE file." For UI where the file is clearly the current/specific file, write `فایل را ذخیره کنید`.

### 4. Singular noun after numbers (severity 2.0)

In Persian, nouns following a numeral **stay singular**. This is the opposite of English (`five files`) and Arabic (`خمسة ملفات` plural).

| ✗ Wrong (English-style plural) | ✓ Correct (singular after number) |
|--------------------------------|-----------------------------------|
| دو فایل‌ها | **دو فایل** (two file) |
| پنج کاربران | **پنج کاربر** (five user) |
| ۱۰۰ نتیجه‌ها | **۱۰۰ نتیجه** (100 result) |
| سه پیام‌ها | **سه پیام** (three message) |

**ICU plurals — Persian needs only `one` + `other`:**

CLDR official Persian plural rules:

- `one`: n = 0 or n = 1 (yes, Persian groups zero with one in CLDR — but in UI you usually still want a "no files" empty state phrasing)
- `other`: everything else

```icu
{count, plural,
  one {# فایل جدید}
  other {# فایل جدید}
}
```

**Both forms use the SINGULAR noun** (فایل, not فایل‌ها). The plural is encoded by the number itself, not by the noun.

**Common errors:**

```icu
✗ Wrong:
{count, plural,
  one {# فایل}
  other {# فایل‌ها}     // ← WRONG: don't pluralize after number
}

✓ Correct:
{count, plural,
  one {# فایل}
  other {# فایل}
}

✗ Wrong (Arabic-style six categories):
{count, plural,
  zero {...} one {...} two {...} few {...} many {...} other {...}
}

✓ Correct (Persian needs only two):
{count, plural,
  one {...}
  other {...}
}
```

**When the source has zero/few/many categories from Arabic:** collapse them all into Persian `other`. Persian does NOT have those categories.

**Plural without numbers — use ـها:**

When there's NO number ("the files" generally), use plural suffix ـها (with ZWNJ):

- "the files" → **فایل‌ها** ✓
- "users" → **کاربران** (animate -ان plural — see below) or **کاربرها** (regular)

**Two plural suffixes:**

- **-ها** (-hâ): regular plural, works for all nouns. Written with ZWNJ: فایل‌ها, کاربر‌ها, پیام‌ها.
- **-ان** (-ân): animate-only plural, more literary/elegant. کاربر → کاربران, مرد → مردان, دانشجو → دانشجویان. For UI, -ها is safer and universal.

### 5. Persian-specific letters and code points (severity 2.0)

Persian uses the Perso-Arabic script with **4 letters NOT in Arabic** and **2 letters that look identical to Arabic but have different Unicode code points**.

**Letters unique to Persian (must use these for Persian words):**

| Letter | Name | Unicode | Sound | Example |
|--------|------|---------|-------|---------|
| **پ** | pe | U+067E | /p/ | پدر (pedar = father), پنج (panj = five), پرسنل |
| **چ** | che | U+0686 | /tʃ/ | چه (che = what), چهار (chahâr = four), چای (chây = tea) |
| **ژ** | zhe | U+0698 | /ʒ/ | ژاپن (zhâpon = Japan), پروژه (proje = project) |
| **گ** | gâf | U+06AF | /g/ | گربه (gorbe = cat), گفتن (goftan = to say), گزارش (gozâresh = report) |

These letters do NOT exist in standard Arabic. Arabic borrowing of `p` uses ب; Arabic `g` uses ج or غ. Using ب or ج for Persian `p`/`g` words is a fundamental error.

**Letters that LOOK like Arabic but use different Unicode code points:**

| Letter | Persian Unicode | Arabic Unicode | Visual difference |
|--------|------------------|------------------|---------------------|
| **یـ / ـیـ / ـی / ی** | U+06CC (Arabic letter farsi yeh) | **ي** U+064A (Arabic letter yeh) | Persian ی has NO dots beneath in any form. Arabic ي has TWO dots beneath in initial/medial/isolated forms. |
| **کـ / ـکـ / ـک / ک** | U+06A9 (Arabic letter keheh) | **ك** U+0643 (Arabic letter kaf) | Persian ک has a flat top in isolated/final forms. Arabic ك has a small hamza-like mark on top in isolated form. |

**Why this matters:**

- Text rendered with Arabic ي in a Persian font may display correctly but is **wrong code-point-wise**. Searches, sorting, regex, and font fallback all break.
- Many keyboards default to Arabic ي / ك. Persian users on Iranian-standard keyboards type the correct Persian forms.
- Translation memory tools often confuse the two — always validate output uses U+06CC and U+06A9.

**Detection regex (for QA):**

```regex
# Find Arabic yeh/kaf in supposedly Persian text:
[يك]
# These should be replaced with:
ي → ی  (U+064A → U+06CC)
ك → ک  (U+0643 → U+06A9)
```

**Common Persian words spelled with these letters:**

| Wrong (Arabic chars) | Correct (Persian chars) | Meaning |
|----------------------|--------------------------|---------|
| كتاب | **کتاب** | book |
| ميكنيد | **می‌کنید** | you do (formal) |
| يك | **یک** | one |
| ايران | **ایران** | Iran |
| فارسي | **فارسی** | Persian |
| كاربر | **کاربر** | user |
| كليك | **کلیک** | click |
| كپي | **کپی** | copy |

### 6. SOV word order — verb at the end (severity 2.0)

Persian is **SOV** (Subject-Object-Verb). The verb almost always comes **last** in the clause.

| English (SVO) | Persian (SOV) | Word-by-word |
|---------------|---------------|--------------|
| I read a book. | من کتابی می‌خوانم. | I book-a read. |
| The user saves the file. | کاربر فایل را ذخیره می‌کند. | user file ACC saves. |
| You should click the button. | باید روی دکمه کلیک کنید. | should on button click. |
| Please enter your password. | لطفاً گذرواژه خود را وارد کنید. | please password yours ACC enter. |

**Word order template (formal):**

```
[Time] [Subject] [Indirect Obj + preposition] [Direct Obj + را] [Adverb] [Verb]
```

**Common errors (English-influenced SVO retention):**

| ✗ Wrong (SVO calque) | ✓ Correct (SOV) |
|----------------------|------------------|
| کاربر ذخیره می‌کند فایل را | **کاربر فایل را ذخیره می‌کند** |
| لطفاً وارد کنید گذرواژه را | **لطفاً گذرواژه را وارد کنید** |
| سیستم ارسال می‌کند پیام | **سیستم پیام را ارسال می‌کند** |
| من می‌خوانم کتاب | **من کتاب می‌خوانم** |

**For UI imperative buttons + status messages:** see the UI Conventions section. Short status forms can use SOV-like patterns: `در حال بارگذاری...` (literally "in state-of loading...").

### 7. Persian punctuation (severity 1.5)

Persian uses the same RTL-mirror punctuation as Arabic for some marks, but with French-style quotation guillemets.

| Mark | Persian | Unicode | Notes |
|------|---------|---------|-------|
| Question mark | **؟** | U+061F | Same as Arabic. Visually mirror of Latin ? — appears on LEFT side visually (logical end of sentence). |
| Comma | **،** | U+060C | Same as Arabic. |
| Semicolon | **؛** | U+061B | Same as Arabic. |
| Period | `.` | U+002E | Same as Latin. |
| Colon | `:` | U+003A | Same as Latin. |
| Exclamation | `!` | U+0021 | Same as Latin. |
| Quotation marks | **«…»** | U+00AB / U+00BB | **Persian uses French-style guillemets**, borrowed via 19th-c. French influence. NO spaces inside: `«فایل»` not `« فایل »`. |
| Hyphen | `-` | U+002D | Same as Latin. |
| Ellipsis | `…` | U+2026 | Same as Latin. |
| Percent | `%` or `٪` (U+066A) | | Western `%` accepted; Persian `٪` traditional. |

**Hard rules:**

1. Use `؟` not `?` in Persian sentences. ASCII `?` is wrong.
2. Use `،` not `,` in Persian sentences. ASCII `,` is wrong.
3. Use `«...»` not `"..."` for Persian quotations. Straight quotes are acceptable in technical/API contexts but guillemets are the formal standard.
4. **No space inside guillemets**: `«فایل»` ✓ not `« فایل »` ✗.
5. **No space before** `؟ ، ؛ : !` (unlike French).

**Bidirectional punctuation behavior:**

In RTL text, punctuation displays at the **visual left** but is **logically last** in the string (after the last word). Editors handle this — never manually reverse punctuation. Type it in logical order.

**Example:**

```
Logical (storage) order:  چرا فایل را ذخیره نمی‌کنید؟
Visual (display) order:   ؟چرا فایل را ذخیره نمی‌کنید
                          ↑ question mark appears at far left
```

### 8. Bidirectional text — preserving Latin tech identifiers (severity 1.5)

Persian text is RTL. Embedded Latin script (Git, API, JSON, URLs, file names, code identifiers) stays LTR. Most rendering engines handle this automatically when the container is `dir="rtl"` or `dir="auto"`.

**Hard rules:**

1. **Never translate code identifiers, file names, URLs, brand names.** They stay in Latin script exactly as in source.
2. **Latin runs inside Persian sentences** should be preserved as Latin. The bidi algorithm handles visual flow.
3. **Add LRM (U+200E) or RLM (U+200F) markers only when QA confirms a rendering bug** — do not sprinkle them speculatively.

**Examples — Latin tech terms inside Persian:**

```
✓ از Git برای مدیریت کد استفاده کنید.
✓ برای فراخوانی API، توکن JWT خود را در هدر Authorization قرار دهید.
✓ فایل package.json را در دایرکتوری ریشه قرار دهید.
✓ از طریق https://example.com وارد شوید.

✗ از جیت برای مدیریت کد استفاده کنید.  (transliteration when keep-Latin is better)
✗ از Api برای... (wrong capitalization — keep as source: API)
```

**Tech terms typically kept in Latin:**

- Languages: Python, JavaScript, Go, Rust, Java, C++, TypeScript
- Frameworks: React, Vue, Angular, Next.js, Django, Spring Boot
- Tools: Git, GitHub, GitLab, Docker, Kubernetes, npm, pip, cargo
- Protocols: HTTP, HTTPS, FTP, SSH, TCP, REST, GraphQL, gRPC
- Formats: JSON, XML, YAML, CSV, PDF, MP4, PNG, SVG
- Commands: ls, cd, mkdir, git commit, npm install
- URLs, email addresses, file paths, IP addresses

**Brand names:** Keep in Latin script where the brand is internationally recognized: Google, Apple, Microsoft, Facebook/Meta, Amazon, AWS, OpenAI. If a brand has an official Persian rendering (e.g., اینستاگرام is sometimes used alongside Instagram), check the brand's official Persian site.

### 9. Religious and cultural sensitivity (severity 2.0)

Iran is **~90% Shia Muslim** with constitutional minorities including Sunni Muslims (~9%), Christians (Armenian + Assyrian), Jews, and Zoroastrians (the indigenous pre-Islamic religion). Afghanistan is **~85% Sunni Muslim** with Shia minority. UI copy should respect Islamic values **without alienating non-Muslim Iranians** or assuming Arab-Sunni framing.

**Hard rules:**

1. **Don't inject religious phrases** (ان‌شاءالله / به امید خدا / الحمدلله) into translations unless the source already invokes that semantic. They are not generic politeness fillers in software UI.
2. **Cultural Christian-origin idioms** must be re-conceptualized, not literally translated:

| English idiom | ✗ Literal calque | ✓ Persian cultural equivalent |
|---------------|------------------|-------------------------------|
| cross to bear | صلیب حمل کردن | بار سنگین / مسئولیت سنگین |
| holy grail | جام مقدس | هدف نهایی / آرزوی بزرگ |
| good Samaritan | سامری نیک | فاعل خیر / آدم خیر |
| blessing in disguise | (literal) | نعمتی پنهان / در باطنش خیر است |
| baptism of fire | غسل تعمید آتش | آزمون سخت / تجربه‌ی دشوار |
| Pandora's box | جعبهٔ پاندورا | باب فتنه / آغاز مصیبت |
| Achilles' heel | پاشنهٔ آشیل | نقطهٔ ضعف |
| knock on wood | چوب بزن | به امید خدا / خدا نکند |
| fingers crossed | (literal) | ان‌شاءالله / امیدوارم |
| break a leg | پا شکستن | موفق باشی! / موفق باشید! |
| piece of cake | یک تکه کیک | مثل آب خوردن / خیلی آسان |
| bring home the bacon | (literal — pork!) | نان‌آور بودن / روزی حلال آوردن |
| champagne problems | (literal — alcohol) | مشکلات لوکس / مشکلات تجملاتی |

3. **Halal sensitivity:** Avoid casual metaphors involving pork (خوک), alcohol (شراب, الکل, بیر), or gambling (قمار) unless they are the literal subject. Use neutral alternatives.

4. **Iranian national identity:** Persians have a strong pre-Islamic Zoroastrian heritage (Cyrus, Darius, Nowruz). UI for Iranian audiences should respect both Islamic and pre-Islamic cultural framings. **Nowruz (نوروز, Persian New Year, ~March 20-21)** is the single most important Iranian holiday — bigger than Eid for many Iranians.

5. **Avoid Arab-vs-Persian conflation:** Don't translate "the Arab world" assumptions into Persian. Iranians are not Arabs. Don't write `العالم العربی` references for an Iranian audience.

6. **Calendar:** Iran officially uses **Solar Hijri (Jalali)** calendar — current year ≈ 1402-1403 SH for 2024 CE. Gregorian dates are also acceptable but Solar Hijri is the standard for Iranian audiences. (See Currency/Dates section below.)

7. **Politeness (تعارف):** Iranian culture has elaborate politeness conventions (تعارف). UI politeness is signaled with لطفاً (please) before requests and softer phrasings. Don't overuse — once per dialog/modal is plenty.

8. **Dating/relationships:** "Dating app" in conservative contexts → `اپلیکیشن آشنایی` or `اپلیکیشن همسریابی` (matchmaking) rather than literal `قرار ملاقات` which carries the wrong connotation.

---

## UI Conventions

### Button labels — noun (masdar) or formal imperative

Persian button labels have two acceptable styles. **Be consistent within a product.**

**Style 1: Noun-style (more concise, common in modern Iranian software):**

| English | Persian (noun) |
|---------|----------------|
| Save | ذخیره |
| Cancel | لغو |
| Delete | حذف |
| Edit | ویرایش |
| Send | ارسال |
| Confirm | تأیید |
| Continue | ادامه |
| Submit | ارسال / ثبت |
| Search | جستجو |
| Settings | تنظیمات |
| Login / Sign in | ورود |
| Logout / Sign out | خروج |
| Sign up | ثبت‌نام |
| Upload | بارگذاری |
| Download | بارگیری / دانلود |
| Refresh | به‌روزرسانی |
| Close | بستن |
| Next | بعدی |
| Previous / Back | قبلی / بازگشت |
| Done | انجام شد / تمام |
| OK | تأیید / باشد |

**Style 2: Formal imperative with کنید (more polite, common in traditional/formal UI):**

| English | Persian (imperative + کنید) |
|---------|------------------------------|
| Save | ذخیره کنید |
| Cancel | لغو کنید |
| Delete | حذف کنید |
| Edit | ویرایش کنید |
| Send | ارسال کنید |
| Login | وارد شوید |
| Logout | خارج شوید |

**Picking a style:**

- **Buttons (single action, short label)** → noun style preferred (ذخیره, حذف, لغو). Modern Iranian software follows this.
- **Sentence-style CTAs ("Please click here to continue")** → imperative + کنید (لطفاً برای ادامه اینجا کلیک کنید).
- **Confirmation modals** ("Are you sure you want to delete?") → imperative + کنید (آیا مطمئنید می‌خواهید حذف کنید؟).

**Never use تو-form imperatives** (`ذخیره کن`, `حذف کن`) in formal UI. Those are intimate/casual.

### Status messages — progressive / completion / failure / empty

**Progressive (in-flight):** Use `در حال + masdar` or present-progressive verb

- در حال بارگذاری... (Loading...)
- در حال ذخیره... (Saving...)
- در حال ارسال... (Sending...)
- در حال پردازش... (Processing...)
- در حال اتصال... (Connecting...)
- لطفاً صبر کنید... (Please wait...)

**Completion:** Use past-tense passive `... شد` or `با موفقیت ...`

- ذخیره شد. (Saved.)
- با موفقیت ذخیره شد. (Saved successfully.)
- فایل با موفقیت بارگذاری شد. (File uploaded successfully.)
- ارسال شد. (Sent.)
- تمام شد. (Done.)
- انجام شد. (Done.)

**Failure:** Use `... نشد` / `خطا در ...` / `قادر به ... نیستیم`

- ذخیره نشد. (Not saved. / Save failed.)
- خطا در بارگذاری فایل. (Error uploading file.)
- ارسال با خطا مواجه شد. (Sending failed.)
- اتصال به سرور برقرار نشد. (Could not connect to server.)
- فایل یافت نشد. (File not found.)
- قادر به انجام عملیات نیستیم. (Unable to perform the operation.)

**Empty state:** Use `هنوز ... وجود ندارد` / `... یافت نشد`

- هنوز فایلی وجود ندارد. (No files yet.)
- نتیجه‌ای یافت نشد. (No results found.)
- اعلانی وجود ندارد. (No notifications.)
- محتوایی برای نمایش وجود ندارد. (No content to display.)

**Validation / field errors:** nominal description + what to do

- این فیلد الزامی است. (This field is required.)
- قالب نامعتبر است. (Invalid format.)
- گذرواژه باید حداقل ۸ کاراکتر باشد. (Password must be at least 8 characters.)
- ایمیل وارد شده معتبر نیست. (The email entered is not valid.)

**Action instructions (in dialogs/forms):** formal imperative

- گذرواژه خود را وارد کنید. (Enter your password.)
- حداقل یک گزینه را انتخاب کنید. (Choose at least one option.)
- دوباره امتحان کنید. (Try again.)
- لطفاً اطلاعات را بررسی کنید. (Please check the information.)

### Error messages — what happened + what to do

Persian error messages should follow the same two-part structure as Arabic and English: **state the problem, then suggest a next step.**

| ✗ Bare (only what happened) | ✓ With next step |
|------------------------------|-------------------|
| فایل یافت نشد. | **فایل یافت نشد. لطفاً مسیر را بررسی کنید.** |
| خطای شبکه. | **خطای شبکه. لطفاً اتصال اینترنت خود را بررسی کنید و دوباره امتحان کنید.** |
| ایمیل نامعتبر. | **ایمیل وارد شده نامعتبر است. لطفاً آدرس را بررسی کنید.** |
| رمز عبور اشتباه. | **گذرواژه اشتباه است. لطفاً دوباره امتحان کنید یا از گزینهٔ "فراموشی گذرواژه" استفاده کنید.** |
| دسترسی رد شد. | **دسترسی رد شد. لطفاً وارد شوید یا با مدیر سیستم تماس بگیرید.** |

### Drag-and-drop terminology

Use **native Persian verbs**, NOT transliterations from English.

| English | ✓ Persian (native) | ✗ Avoid (transliteration) |
|---------|---------------------|----------------------------|
| drag | بکشید / بکشانید | دراگ کنید |
| drop | رها کنید / بیندازید | دراپ کنید |
| release | رها کنید | ریلیز کنید |
| Drag and drop the file here | فایل را به اینجا بکشید و رها کنید | فایل را اینجا دراگ اند دراپ کنید |
| Drop file here to upload | برای بارگذاری، فایل را اینجا رها کنید | (no English calque) |

### File picker

- "Choose a file" → **فایلی انتخاب کنید** or **انتخاب فایل** (noun form).
- "Browse files" → **مرور فایل‌ها** (when meaning navigation) or **انتخاب فایل** (when meaning upload trigger).
- "Open" → **باز کردن** or **بازکردن**.

Avoid `جستجو` for file picker (جستجو = search, not browse).

### Quantities — "X+" / "more than X"

Persian uses **بیش از X** or **بیشتر از X** instead of `X+`.

- `+25 languages` → **بیش از ۲۵ زبان** ✓ (NOT `+۲۵ زبان` ✗)
- `5+` → **۵ یا بیشتر** or **بیش از ۵** ✓
- `+{count} more` → **و {count} مورد دیگر** or **{count} مورد دیگر**

### FOR vs PER — critical distinction

| Source | ✓ Persian | Meaning |
|--------|-----------|---------|
| for 25 languages (total) | **برای ۲۵ زبان** | Total scope |
| per language (rate) | **به ازای هر زبان** / **برای هر زبان** | Per-unit rate |
| per month | **در ماه** / **ماهانه** | Per-time rate |
| per year | **در سال** / **سالانه** | Per-time rate |
| per user | **به ازای هر کاربر** | Per-unit rate |

Pricing-page wording mixing these is an auto-fail.

### Hashtags, mentions, links in copy

- `#hashtag` (Latin) stays Latin: `#example`.
- `#هشتگ_فارسی` (Persian hashtag) is also fine for Persian-tagged content.
- `@username` stays as-is, never translated.
- URLs stay LTR within RTL — engines handle this; don't translate domain names.

---

## Punctuation, Numbers, Dates, Currency

### Numerals — two systems

Persian has two acceptable numeral systems:

| System | Digits | Use case |
|--------|--------|----------|
| **Persian (Eastern Arabic-Indic, but specifically Persian)** | ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹ | Traditional, literary, formal Persian text |
| **Western (Hindu-Arabic)** | 0 1 2 3 4 5 6 7 8 9 | Modern UI, technical, business, scientific |

**Note:** Persian digits ۴ ۵ ۶ have subtly different shapes from Arabic-Indic ٤ ٥ ٦. The Unicode code points are:

- Persian ۰-۹: U+06F0 to U+06F9 (extended Arabic-Indic)
- Arabic ٠-٩: U+0660 to U+0669 (Arabic-Indic)
- Western 0-9: U+0030 to U+0039

**Rule for UI:**

- **Be consistent within a string/screen.** Never mix `5 فایل` with `۷ پیام` in the same UI.
- **Modern Iranian software typically uses Western 0-9** because most users have international keyboards and the bidi handling is more reliable.
- **Persian ۰-۹** is used in formal/literary contexts, government documents, and traditionally-styled UIs.
- **Default for software UI: Western 0-9** unless the brand explicitly leans Persian-traditional.

### Number formatting

| Format | Persian/Iranian convention | Example |
|--------|----------------------------|---------|
| Thousands separator | `٬` (Arabic thousands sep U+066C) or `,` (comma) | ۱٬۲۳۴ or 1,234 |
| Decimal separator | `٫` (Arabic decimal sep U+066B) or `.` (period) | ۱٬۲۳۴٫۵۶ or 1,234.56 |
| Negative numbers | `-25` (minus before number, LTR-protected) | -25 / -۲۵ |
| Percentages | `25%` or `٪۲۵` (Persian convention puts ٪ before number) | ۲۵٪ |
| Phone numbers | `0912-345-6789` (Iran mobile prefix 09) | +98 912 345 6789 |

**For software UI: Western `1,234.56` is the safest and most common.** Persian `۱٬۲۳۴٫۵۶` is correct for traditional/formal contexts.

### Dates — Solar Hijri (Jalali) is OFFICIAL in Iran

Iran officially uses the **Solar Hijri calendar** (also called Jalali), which has been the national civil calendar since the 1925 standardization (based on the older 1079 CE Jalali calendar of Omar Khayyam).

**Conversion:** Current Iranian year ≈ Gregorian year − 621 (or − 622 between January 1 and ~March 20).

- 2024 CE = 1402 SH (Jan-Mar) / 1403 SH (Mar-Dec)
- 2025 CE = 1403 SH (Jan-Mar) / 1404 SH (Mar-Dec)
- 2026 CE = 1404 SH (Jan-Mar) / 1405 SH (Mar-Dec)

**The Persian year starts on Nowruz (~March 21)** — the vernal equinox. This is also the Iranian New Year, the most important cultural holiday.

**Persian (Jalali) month names — fa-IR (Iran):**

| # | Name | Transliteration | Gregorian approx | Days |
|---|------|-----------------|------------------|------|
| 1 | **فروردین** | Farvardin | Mar 21 – Apr 20 | 31 |
| 2 | **اردیبهشت** | Ordibehesht | Apr 21 – May 21 | 31 |
| 3 | **خرداد** | Khordâd | May 22 – Jun 21 | 31 |
| 4 | **تیر** | Tir | Jun 22 – Jul 22 | 31 |
| 5 | **مرداد** | Mordâd | Jul 23 – Aug 22 | 31 |
| 6 | **شهریور** | Shahrivar | Aug 23 – Sep 22 | 31 |
| 7 | **مهر** | Mehr | Sep 23 – Oct 22 | 30 |
| 8 | **آبان** | Âbân | Oct 23 – Nov 21 | 30 |
| 9 | **آذر** | Âzar | Nov 22 – Dec 21 | 30 |
| 10 | **دی** | Dey | Dec 22 – Jan 20 | 30 |
| 11 | **بهمن** | Bahman | Jan 21 – Feb 19 | 30 |
| 12 | **اسفند** | Esfand | Feb 20 – Mar 20 | 29 (30 leap) |

**Dari (fa-AF, Afghanistan) — Solar Hijri but with Arabic-zodiac month names:**

| # | Persian/Iran (fa-IR) | Dari/Afghanistan (fa-AF) |
|---|----------------------|---------------------------|
| 1 | فروردین | **حمل** (Hamal — Aries) |
| 2 | اردیبهشت | **ثور** (Sawr — Taurus) |
| 3 | خرداد | **جوزا** (Jawzâ — Gemini) |
| 4 | تیر | **سرطان** (Saratân — Cancer) |
| 5 | مرداد | **اسد** (Asad — Leo) |
| 6 | شهریور | **سنبله** (Sonbola — Virgo) |
| 7 | مهر | **میزان** (Mizân — Libra) |
| 8 | آبان | **عقرب** (Aqrab — Scorpio) |
| 9 | آذر | **قوس** (Qaws — Sagittarius) |
| 10 | دی | **جدی** (Jadi — Capricorn) |
| 11 | بهمن | **دلو** (Dalv — Aquarius) |
| 12 | اسفند | **حوت** (Hut — Pisces) |

**Date formats:**

| Format | Example | When to use |
|--------|---------|-------------|
| YYYY/MM/DD (Jalali) | 1402/10/25 or ۱۴۰۲/۱۰/۲۵ | Default for Iranian audiences. Often written without "هـ.ش" suffix in computing |
| DD month-name YYYY (Jalali) | 25 دی 1402 / ۲۵ دی ۱۴۰۲ | Long form, formal |
| YYYY/MM/DD (Gregorian) | 2024/01/15 | Computing/international/dual-cal context |
| DD/MM/YYYY (Gregorian) | 15/01/2024 | International formal |
| ISO 8601 | 2024-01-15 | Technical / API contexts only |
| Hijri lunar (قمری) | 3 رجب 1445 هـ.ق | Religious contexts, holidays (Ramadan, Ashura, etc.) |

**Calendar disambiguation suffixes:**

- **هـ.ش** (Hijri Shamsi / Solar Hijri) — e.g., 1402 هـ.ش
- **هـ.ق** (Hijri Qamari / Lunar Hijri) — e.g., 1445 هـ.ق, used for religious dates
- **م** or **میلادی** (Gregorian / Christian-era) — e.g., 2024 م

**For UI:** If your product uses Gregorian dates, that's fine, but **always be explicit** in formal/legal documents. For Iranian audiences a Jalali date is more readable. Most Iranian sites show both: `۱۴۰۲/۱۰/۲۵ - ۱۵ ژانویه ۲۰۲۴`.

### Days of week — week starts on Saturday

In Iran, the week starts on **شنبه (Saturday)** and **Friday (جمعه) is the weekly holy day / weekend**. Government, banks, and schools close Friday; Thursday is a half-day. (Afghanistan: Thursday + Friday weekend.)

| English | Persian | Pronunciation | Notes |
|---------|---------|---------------|-------|
| Saturday | **شنبه** | Shanbe | First day of week, full workday |
| Sunday | **یکشنبه** | Yek-shanbe | Workday |
| Monday | **دوشنبه** | Do-shanbe | Workday |
| Tuesday | **سه‌شنبه** | Se-shanbe | Workday (ZWNJ between سه and شنبه) |
| Wednesday | **چهارشنبه** | Chahâr-shanbe | Workday |
| Thursday | **پنج‌شنبه** | Panj-shanbe | Half-day (Iran) / Weekend day (Afghanistan); ZWNJ inside |
| Friday | **جمعه** | Jom'e | Weekly holiday, weekend |

**Note the ZWNJ in سه‌شنبه and پنج‌شنبه** — without the half-space, the letters would form incorrect ligatures.

### Time

| Format | Example | Use case |
|--------|---------|----------|
| 24-hour | 14:30 / ۱۴:۳۰ | Default, technical, international |
| 12-hour | 2:30 ب.ظ / ۲:۳۰ ب.ظ | Casual (ب.ظ = بعد از ظهر = PM; ق.ظ = قبل از ظهر = AM) |

`صبح / بعدازظهر / عصر / شب` (morning / afternoon / evening / night) are also common in copy.

### Currency

**Iran (fa-IR):**

| Aspect | Rial (official) | Toman (everyday) |
|--------|-----------------|-------------------|
| Name | ریال | تومان |
| Conversion | 10 ریال = 1 تومان | (1 toman = 10 rials) |
| Used in | Government, banking, official prices | Everyday speech, shop prices, casual writing |
| ISO code | IRR | (no ISO — toman is informal) |
| Example | ۱۰٬۰۰۰ ریال | ۱٬۰۰۰ تومان |

**Iranian currency context:**

- Iran has had years of currency reform discussion. The country uses **toman in everyday life** but rials officially.
- A "100 toman" price tag = 1,000 rials officially.
- For UI: **default to toman (تومان)** for consumer-facing pricing — that's what users mentally calculate in. For banking/official UIs, use rials.
- Currency placement: amount + currency name → `۱٬۰۰۰ تومان` / `۱۰٬۰۰۰ ریال`.
- For international/global products: USD `$99.99` is acceptable; specify the conversion to toman if pricing is for Iranian market.

**Afghanistan (fa-AF):**

- **افغانی** (afghani, AFN) — Afghan unit of currency.
- Example: ۱٬۰۰۰ افغانی or 1,000 AFN.

---

## Terminology — Preferred Persian Terms

### Common UI vocabulary

| English | ✓ Persian (preferred) | ⚠ Avoid (transliteration) |
|---------|------------------------|----------------------------|
| user | کاربر | یوزر |
| account | حساب کاربری / حساب | اکانت |
| password | گذرواژه / رمز عبور | پسورد |
| email | ایمیل / پست الکترونیک | (ایمیل accepted) |
| settings | تنظیمات | ستینگز |
| dashboard | داشبورد / پیشخوان | (داشبورد accepted) |
| profile | پروفایل / نمایه | (پروفایل accepted) |
| link | لینک / پیوند | (لینک accepted) |
| browser | مرورگر | براوزر |
| website | وب‌سایت / سایت / تارنما | (سایت accepted) |
| folder | پوشه | فولدر |
| file | فایل | (فایل accepted) |
| device | دستگاه | دیوایس |
| phone (mobile) | موبایل / تلفن همراه / گوشی | (موبایل accepted) |
| computer | کامپیوتر / رایانه | (کامپیوتر accepted) |
| application / app | برنامه / اپلیکیشن / اپ | (اپلیکیشن accepted) |
| update (v.) | به‌روزرسانی / آپدیت | (آپدیت accepted) |
| save | ذخیره | سیو |
| delete | حذف / پاک کردن | دیلیت |
| cancel | لغو | کنسل |
| upload | بارگذاری / آپلود | (آپلود accepted) |
| download | بارگیری / دانلود | (دانلود accepted) |
| sign in / log in | ورود / وارد شدن | لاگین |
| sign out / log out | خروج / خارج شدن | لاگ‌اوت |
| sign up | ثبت‌نام | ساین‌آپ |
| search | جستجو | سرچ |
| click | کلیک / کلیک کردن | (کلیک accepted) |
| share | اشتراک‌گذاری / به اشتراک گذاشتن | شیر |
| notifications | اعلان‌ها / اطلاع‌رسانی | نوتیفیکیشن |
| privacy | حریم خصوصی | پرایوسی |
| terms (of service) | شرایط (استفاده) | ترمز |
| support | پشتیبانی | سپورت |
| help | راهنما / کمک | هلپ |
| feedback | بازخورد / نظرات | فیدبک |
| menu | منو / فهرست | (منو accepted) |
| home | خانه / صفحهٔ اصلی | هوم |
| copy | کپی / رونوشت | (کپی accepted) |
| paste | چسباندن | پیست |
| cut | برش | کات |
| undo | برگرداندن / لغو | آندو |
| redo | تکرار / انجام دوباره | ریدو |
| open | باز کردن | (no calque) |
| close | بستن | (no calque) |
| edit | ویرایش | ادیت |
| view | مشاهده / دیدن | (no calque) |
| send | ارسال | سند |
| receive | دریافت | (no calque) |
| invite | دعوت | (no calque) |
| follow | دنبال کردن | فالو |
| like | پسندیدن / لایک | (لایک accepted) |
| comment | نظر / کامنت | (کامنت accepted) |

### Tech/dev-specific terms

| English | ✓ Persian | Notes |
|---------|-----------|-------|
| build (v., software) | ساخت / بیلد | (بیلد accepted in dev contexts) |
| deploy | استقرار / دیپلوی | (دیپلوی accepted in dev) |
| pipeline (CI/CD) | خط لوله / pipeline | Keep Latin in dev contexts |
| repository / repo | مخزن / ریپازیتوری | (ریپو accepted) |
| branch (git) | شاخه / branch | |
| commit (v., git) | کامیت / ثبت | (کامیت accepted in dev) |
| pull request | درخواست ادغام / pull request | Often kept Latin |
| merge | ادغام / merge | |
| API | API / واسط برنامه‌نویسی | Keep Latin "API" |
| endpoint | endpoint / نقطهٔ پایانی | |
| token | توکن / نشانه | |
| cache | کش / حافظهٔ موقت | (کش accepted) |
| log (n.) | لاگ / گزارش / سیاهه | |
| sync | همگام‌سازی | |
| webhook | webhook | Keep Latin |
| backend | بک‌اند / پشت‌خانه | (بک‌اند accepted) |
| frontend | فرانت‌اند / پیش‌خانه | (فرانت‌اند accepted) |
| database | پایگاه داده / دیتابیس | |
| server | سرور | |
| client | کلاینت / مشتری | |
| query | کوئری / پرس‌وجو | |
| index | ایندکس / نمایه / فهرست | |
| schema | شِما / طرح | |
| migration | مهاجرت / migration | |

### Native vs loanword preference

Persian tolerates technical loanwords more than some languages (more than Icelandic, less than Indonesian). The **Iranian Academy of Persian Language and Literature (فرهنگستان زبان و ادب فارسی)** coins native Persian replacements for foreign terms (similar to Iceland's language committee), but adoption is partial.

**Rule of thumb:**

- **Tech terms users know well in English** (file, click, link, system, code, server, database) → keep familiar Persianized form (فایل، کلیک، لینک، سیستم، کد، سرور، دیتابیس).
- **Concepts with established native Persian** (settings → تنظیمات, search → جستجو, save → ذخیره, delete → حذف, settings → تنظیمات, browser → مرورگر, folder → پوشه, password → گذرواژه, browser → مرورگر) → use the native form.
- **Verbose Academy coinages** (e.g., "رایانامه" for email) are technically correct but feel stilted in modern UI. Use them only if the brand voice is explicitly traditional.

### Place names — short forms in UI

| English | UI short form | Long/diplomatic form (avoid in UI) |
|---------|---------------|------------------------------------|
| United States / USA | **آمریکا** | ایالات متحدهٔ آمریکا |
| United Kingdom | **بریتانیا** / **انگلیس** | پادشاهی متحدهٔ بریتانیا کبیر |
| Germany | **آلمان** | جمهوری فدرال آلمان |
| France | **فرانسه** | جمهوری فرانسه |
| China | **چین** | جمهوری خلق چین |
| Japan | **ژاپن** | (note ژ — Persian-specific letter) |
| Russia | **روسیه** | فدراسیون روسیه |
| Saudi Arabia | **عربستان (سعودی)** | پادشاهی عربستان سعودی |
| UAE | **امارات** | امارات متحدهٔ عربی |
| Iran | **ایران** | جمهوری اسلامی ایران |
| Afghanistan | **افغانستان** | (no different long form needed) |

---

## Calque / Anti-Pattern Blocklist

These calques (literal English translations) make Persian text sound machine-translated. Replace with idiomatic Persian.

| ✗ Wrong (English calque) | ✓ Correct (idiomatic Persian) | Why |
|---------------------------|-------------------------------|-----|
| حس می‌کند (makes sense) | **منطقی است / معنا دارد** | "Makes sense" is English idiom; Persian uses منطقی است |
| استراحت گرفتن (take a break) | **استراحت کردن** | "Take a break" — Persian uses کردن, not گرفتن with استراحت |
| وقت گرفتن (take time) | **وقت بردن / زمان‌بر بودن** | "Take time" — Persian says "carries time" بردن |
| مراقبت گرفتن (take care) | **مراقب بودن** | "Take care" — Persian uses بودن, not گرفتن |
| دراگ کنید (drag) | **بکشید** | Use native Persian verb |
| دراپ کنید (drop) | **رها کنید** | Use native Persian verb |
| یک تکه کیک (piece of cake) | **مثل آب خوردن / خیلی آسان** | Idiom — use Persian equivalent |
| پا شکستن (break a leg) | **موفق باشی / موفق باشید** | Idiom — translate function, not literal |
| ضربه با یک سنگ به دو پرنده (kill two birds with one stone) | **با یک تیر دو نشان زدن** | Persian native equivalent |
| نقاش تصویر بزرگ (paint the big picture) | **نگاه کلی / تصویر کلی ارائه دادن** | English business-speak calque |
| در نهایت روز (at the end of the day) | **در نهایت / در آخر / در پایان** | English filler calque |
| بر اساس روزانه (on a daily basis) | **روزانه / هر روز** | Use adverb, not nominal |
| از نظر عملکرد (in terms of performance) | **از لحاظ عملکرد / در زمینهٔ عملکرد** | Use natural Persian preposition |
| در صورتی که اگر (in case if) | **در صورتی که / اگر** | Redundant double-conjunction |
| به منظور اینکه بتوانیم (in order that we can) | **برای اینکه بتوانیم / تا بتوانیم** | Verbose purpose clause |
| فایل نمی‌تواند یافت شود | **فایل یافت نشد / فایل پیدا نشد** | Passive "cannot be found" calque |
| به صورت پیش‌فرض مقدار | **مقدار پیش‌فرض** | Wrong word order — adjective after noun |
| قدرت گرفته از هوش مصنوعی | **مبتنی بر هوش مصنوعی / با پشتیبانی هوش مصنوعی** | "Powered by AI" calque |
| آگاه از زمینه | **آگاه به زمینه / مبتنی بر زمینه** | "Context-aware" calque |
| دوستانه با کاربر | **کاربرپسند / آسان برای استفاده** | "User-friendly" calque |
| پایگاه دادهٔ URL ها | **پایگاه دادهٔ آدرس‌ها / URLs** | Mixed Persian-English plural |
| نقطهٔ پایانی API | **نقطهٔ پایانی API / endpoint** | Keep API in Latin, or use full Persian |
| عملیات حذف انجام می‌گیرد | **حذف انجام می‌شود / حذف می‌شود** | Over-nominalization |
| ایالات متحدهٔ آمریکا | **آمریکا** (in UI) | Use short form |
| پادشاهی متحده | **بریتانیا / انگلیس** | Use short form |
| جام مقدس (holy grail) | **هدف نهایی / آرزوی بزرگ** | Christian-origin idiom |
| صلیب حمل کردن (cross to bear) | **بار سنگین / مسئولیت سنگین** | Christian-origin idiom |
| چوب بزن (knock on wood) | **ان‌شاءالله / خدا نکند / به امید خدا** | Western superstition |
| انگشتانم را روی هم گذاشتم (fingers crossed) | **امیدوارم / ان‌شاءالله** | Western gesture-idiom |

### Passive voice — be sparing

Persian has a passive (formed with **شدن** as auxiliary: `ذخیره شد` = "became saved"). It is grammatically natural for short status messages.

However, **over-using passive in narrative copy** sounds awkward — Persian prefers active voice with clear subjects when possible.

| ✗ Over-passive | ✓ Active or natural passive |
|----------------|-------------------------------|
| فایل توسط سیستم ذخیره می‌شود. | **سیستم فایل را ذخیره می‌کند.** |
| ایمیل به شما توسط ما ارسال شده است. | **ایمیل را برای شما ارسال کرده‌ایم.** |
| این عملیات نمی‌تواند توسط شما انجام شود. | **شما نمی‌توانید این عملیات را انجام دهید.** |

**Short status passives are fine:** `ذخیره شد` ✓, `ارسال شد` ✓, `حذف شد` ✓.

### False friends and tricky vocabulary

| Persian | True meaning | Common misuse |
|---------|--------------|---------------|
| واقعاً | "really / truly" | NOT "actually" in the sense of "in fact" — for that use **در واقع** |
| در نهایت | "at the end / eventually" | OK for "eventually" but check tense |
| ممکن است | "it is possible" | NOT "may" in the sense of permission — use **اجازه دارید** for permission |
| دانلود vs آپلود | down vs up | Don't confuse — بارگیری (download) vs بارگذاری (upload) |
| نکته | "point / note" | NOT "tip" in the sense of money tip — use **انعام** |
| سفارش | "order (commercial)" | NOT "order" in the sense of arrangement — use **ترتیب** |
| رفیق | "friend / pal" (informal) | NOT "comrade" in political sense (which is Soviet-era usage) |

---

## Self-Check Checklist

Run this before returning Persian output. Items marked **(critical)** are auto-fail.

### Identity & script (critical)

- [ ] **(critical)** All ی letters are U+06CC (Persian), not Arabic ي (U+064A). Check: no dots beneath ی in initial/medial forms.
- [ ] **(critical)** All ک letters are U+06A9 (Persian), not Arabic ك (U+0643). Check: ک has flat top in isolated form.
- [ ] **(critical)** Persian-specific letters (پ چ ژ گ) used wherever the Persian word requires them — NOT substituted with Arabic ب ج ز ج/غ.
- [ ] No Arabic grammar imported (no feminine adjective forms, no dual, no zero/two/few/many plural categories).

### ZWNJ / half-space (critical)

- [ ] **(critical)** می- present-tense prefix written with ZWNJ: `می‌کنید`, `می‌رود`, `نمی‌خواهم` — never `میکنید` (joined) or `می کنید` (full space).
- [ ] **(critical)** ها plural suffix written with ZWNJ: `فایل‌ها`, `کاربر‌ها`, `پیام‌ها` — never `فایلها` or `فایل ها`.
- [ ] Compound words use ZWNJ where conventional: `پنج‌شنبه`, `سه‌شنبه`, `به‌روزرسانی`, `بزرگ‌تر`.
- [ ] Translation pipeline preserves U+200C (test for whitespace-normalization bugs).

### Ezafe & word order

- [ ] Noun-modifier pairs in **head-first order**: `فایل جدید` ✓ not `جدید فایل` ✗.
- [ ] Possessive chains in head-first order: `تنظیمات کاربر` ✓ not `کاربر تنظیمات` ✗.
- [ ] Vowel-ending nouns + modifier use ـۀ or ـه‌ی correctly: `خانهٔ بزرگ` or `خانه‌ی بزرگ`.
- [ ] **SOV word order** — verbs at the end of clauses (not English SVO calque).

### Grammar & morphology

- [ ] **(critical)** Singular noun after numbers: `پنج فایل` ✓ not `پنج فایل‌ها` ✗.
- [ ] **(critical)** ICU plurals use only `one` + `other`, both with singular noun. No Arabic-style six categories.
- [ ] را present after definite direct objects: `فایل را ذخیره کنید` ✓ not `فایل ذخیره کنید` ✗ (when "the" file is meant).
- [ ] Verb conjugations match register (شما-form: کنید, کنند, کنم — not تو-form کن).
- [ ] Negative verbs use ن- prefix: `نمی‌کنید`, `نخواهید کرد`, `نباشد`.

### Register (critical)

- [ ] **(critical)** Consistent شما-form throughout file (no mixing with تو-form).
- [ ] Possessives use formal pattern (`فایل شما` / `فایلتان`), not informal `فایلت`.
- [ ] Politeness markers (لطفاً) used appropriately — at most once per dialog, not in every button.

### Punctuation

- [ ] Question marks are `؟` (U+061F), not `?`.
- [ ] Commas are `،` (U+060C), not `,`, in Persian text.
- [ ] Semicolons are `؛` (U+061B), not `;`, in Persian text.
- [ ] Quotations use `«...»` guillemets with no spaces inside.
- [ ] Period at logical end of sentence (RTL renders it at visual left).
- [ ] No space before `؟ ، ؛ : !`.

### Numbers, dates, currency

- [ ] Numerals consistent within string (all Persian ۰-۹ or all Western 0-9 — never mixed).
- [ ] Dates use Solar Hijri (Jalali) with Persian month names for Iranian audience, or Gregorian explicitly marked.
- [ ] Dari/fa-AF uses Arabic-zodiac month names (حمل، ثور…) not Persian month names.
- [ ] Week starts Saturday (شنبه); جمعه is the weekend.
- [ ] Currency: تومان for everyday Iranian context, ریال for official/banking, افغانی for Afghanistan.

### Bidirectional / Latin embedding

- [ ] Latin tech identifiers (Git, API, JSON, URLs, file names, brand names) preserved in Latin script.
- [ ] No accidental transliteration of code identifiers.
- [ ] Bidi rendering not broken by missing LRM/RLM (test mixed Latin-Persian sentences visually).

### Naturalness

- [ ] No English calques (`بر اساس روزانه`, `از نظر`, `حس می‌کند`, `یک تکه کیک`).
- [ ] No transliteration when native Persian exists (`دراگ کنید` → `بکشید`; `سیو` → `ذخیره`).
- [ ] Buttons use noun form (`ذخیره`, `حذف`) or formal imperative (`ذخیره کنید`) — not informal تو-form (`ذخیره کن`).
- [ ] Status messages use `در حال + masdar` for progressive, `... شد` for completion, `... نشد` for failure.
- [ ] Error messages include both what-happened AND next-step.
- [ ] Drag-drop uses native verbs (`بکشید` + `رها کنید`).
- [ ] `بیش از X` instead of `+X`.

### Religious/cultural sensitivity

- [ ] No Christian-origin idioms literally translated (no `جام مقدس`, `صلیب حمل کردن`, `چوب بزن`).
- [ ] No religious phrases injected unless source invokes them (no spontaneous `ان‌شاءالله` in neutral UI).
- [ ] No pork/alcohol/gambling metaphors unless they are the literal subject.
- [ ] Place names use UI short forms (`آمریکا`, `بریتانیا`, `امارات`).
- [ ] Persian/Iranian cultural framing respected (Nowruz acknowledged when relevant; not Arab-conflated).

---

## Worked Examples

### Example 1 — Standard formal UI (default register)

**Source (English):**

> Welcome back! You have 3 new messages in your inbox. Click **Continue** to read them, or **Cancel** to stay here. Saving your changes…

**Auto-detect register:** Standard product UI, neutral lexicon → **شما formal**.

**Translation (fa-IR, شما-form, default):**

> خوش آمدید! شما ۳ پیام جدید در صندوق ورودی خود دارید. برای خواندن آن‌ها روی **ادامه** کلیک کنید، یا برای ماندن در اینجا **لغو** را انتخاب کنید. در حال ذخیرهٔ تغییرات شما…

**Why this works:**

- `خوش آمدید` — formal welcome (شما-form ending ـید).
- `شما ۳ پیام جدید` — number followed by singular noun (پیام, not پیام‌ها). Adjective جدید after noun (ezafe order).
- `صندوق ورودی خود` — possessive `خود` (formal reflexive). `خود` is the polite/formal "your own".
- `روی ... کلیک کنید` — SOV order (verb کنید at end). Note روی for "on" (clicking on).
- Buttons in noun form: `ادامه`, `لغو`.
- `را انتخاب کنید` — را marks definite direct object.
- Status: `در حال ذخیرهٔ تغییرات شما...` — progressive form. Ezafe ـۀ in ذخیرهٔ (noun ending in vowel ـه).
- Punctuation: Persian `،` not `,`. Ellipsis `…` at logical end (visually appears on left in RTL).
- Persian ی and ک throughout (شما uses Persian ی; کلیک uses Persian ک).
- ZWNJ in `آن‌ها` and `ذخیرهٔ`.

### Example 2 — Same string with formal imperative buttons

> خوش آمدید! ۳ پیام جدید در صندوق ورودی خود دارید. برای خواندن آن‌ها روی **ادامه دهید** کلیک کنید، یا برای ماندن در اینجا **لغو کنید** را بزنید. تغییرات شما در حال ذخیره است…

(Note: button labels switched from noun `ادامه/لغو` to verbal `ادامه دهید/لغو کنید`. Both styles are acceptable; pick one per product.)

### Example 3 — ICU plural

**Source:**

```icu
You have {count, plural, one {# new message} other {# new messages}}.
```

**Persian translation:**

```icu
شما {count, plural,
  one {# پیام جدید}
  other {# پیام جدید}
} دارید.
```

**Why:**

- Only `one` and `other` (Persian needs only 2 CLDR categories).
- **Both branches use singular noun** `پیام` (Persian nouns stay singular after numbers).
- Adjective `جدید` (no gender, no plural change).
- SOV: verb `دارید` at end.
- (If count = 0, you may want a separate empty-state phrasing handled outside ICU: `هیچ پیام جدیدی ندارید.`)

### Example 4 — Error message with next-step

**Source:**

> File not found. Please check the path and try again.

**Persian translation:**

> فایل یافت نشد. لطفاً مسیر را بررسی کنید و دوباره امتحان کنید.

**Why:**

- `فایل یافت نشد` — short passive completion form.
- Two-part structure: what happened (`فایل یافت نشد`) + what to do (`مسیر را بررسی کنید و دوباره امتحان کنید`).
- `مسیر را` — را marks definite direct object.
- `لطفاً` once at start (politeness marker).
- SOV: verbs `بررسی کنید`, `امتحان کنید` at end.
- `و` connecting clauses (no comma before و).
- `دوباره` (again) before the verb.

### Example 5 — Marketing copy with Latin tech terms

**Source:**

> Built with Next.js and TypeScript. Deploy to AWS in seconds. Connect to GitHub, GitLab, or Bitbucket.

**Persian translation:**

> ساخته‌شده با Next.js و TypeScript. در عرض چند ثانیه روی AWS مستقر کنید. به GitHub، GitLab یا Bitbucket متصل شوید.

**Why:**

- All tech brand names (Next.js, TypeScript, AWS, GitHub, GitLab, Bitbucket) stay in Latin script — bidi handles rendering.
- `ساخته‌شده` — passive participle, ZWNJ between ساخته and شده.
- `در عرض چند ثانیه روی AWS مستقر کنید` — SOV. `روی AWS` (on AWS).
- `به ... متصل شوید` — "connect to" using متصل + شدن. SOV with verb at end.
- Comma `،` between list items (Persian comma, not `,`).
- No comma before `یا` (or).

### Example 6 — Date displayed in Iranian context

**Source:** Last login: January 15, 2024 at 2:30 PM

**Persian (fa-IR) — Jalali + Gregorian dual:**

> آخرین ورود: ۲۵ دی ۱۴۰۲ - ۱۵ ژانویه ۲۰۲۴، ساعت ۱۴:۳۰

**Why:**

- Jalali date listed first (primary for Iranian audience): `۲۵ دی ۱۴۰۲`.
- Gregorian date shown after en-dash for clarity: `۱۵ ژانویه ۲۰۲۴`.
- Time in 24-hour: `۱۴:۳۰`.
- Persian numerals ۰-۹ throughout (formal/traditional style; Western 0-9 also acceptable in modern UI).
- Persian month name `دی` (10th Jalali month, late Dec–late Jan).
- Persian comma `،`.

**Persian (fa-AF) — Dari with Arabic-zodiac month names:**

> آخرین ورود: ۲۵ جدی ۱۴۰۲ - ۱۵ جنوری ۲۰۲۴، ساعت ۱۴:۳۰

(`جدی` is the Dari name for the 10th solar month; `جنوری` is the Dari spelling of January.)

### Example 7 — Pricing with toman currency

**Source:**

> Pro plan: $9.99 per month, billed annually. Includes 100GB storage and unlimited users.

**Persian translation (fa-IR, Iranian market with toman):**

> طرح حرفه‌ای: ۵۹۰٬۰۰۰ تومان در ماه، صورت‌حساب سالانه. شامل ۱۰۰ گیگابایت فضای ذخیره‌سازی و تعداد نامحدود کاربر.

**Why:**

- Pricing converted to toman (the everyday Iranian unit). $9.99 ≈ 590,000 toman at illustrative exchange rate.
- `طرح حرفه‌ای` — `Pro plan` (ezafe between طرح and حرفه‌ای).
- `در ماه` for "per month" (NOT `به ازای هر ماه` which is verbose).
- `صورت‌حساب سالانه` — annual billing.
- `شامل ... و ...` — list connector و, no comma before و.
- `فضای ذخیره‌سازی` — ezafe phrase for "storage space".
- `تعداد نامحدود کاربر` — "unlimited number of user" (singular کاربر, Persian rule).

### Example 8 — Sign-up form with validation

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

**Persian translation:**

```
ثبت‌نام
ایمیل: [your@email.com]
گذرواژه: [حداقل ۸ کاراکتر]
[با شرایط استفاده موافقم]
[ایجاد حساب] [لغو]

خطاها:
- این فیلد الزامی است.
- قالب ایمیل نامعتبر است.
- گذرواژه باید حداقل ۸ کاراکتر باشد.
```

**Why:**

- `ثبت‌نام` (ZWNJ between ثبت and نام) — sign up.
- Email placeholder stays in Latin (`your@email.com`).
- Form labels are nouns (`ایمیل`, `گذرواژه`).
- Checkbox label uses 1st-person شما-form: `موافقم` (I agree).
- Buttons are nouns: `ایجاد حساب`, `لغو`.
- Errors: nominal description + است copula. `این فیلد الزامی است` SOV with copula at end.
- `قالب ایمیل` — ezafe (format of email).

---

## When in Doubt

1. **Default to شما-form formal register, Western 0-9 digits, Solar Hijri calendar, modern Iranian terminology.** This is the safe pan-fa-IR setting.

2. **If unsure about variant (fa-IR vs fa-AF)** → ask once; default to fa-IR.

3. **If you see ي or ك in the output** → it's Arabic, replace with Persian ی (U+06CC) and ک (U+06A9). Always.

4. **If you see میکنید or می کنید** → fix to می‌کنید with ZWNJ.

5. **If an English idiom doesn't have a clear Persian equivalent** → translate the **function**, not the literal words. Don't import the metaphor.

6. **If you're tempted to import Arabic grammar** (dual, feminine agreement, six-category plurals) → STOP. Persian is Indo-European with SOV order, no gender, no dual, two CLDR plurals.

7. **If a tech term has no clean Persian equivalent** → keep it in Latin script (Git, API, JSON, React) rather than awkwardly transliterate.

8. **If unsure about religious/cultural framing** → choose the neutral, secular option that respects Islamic values without injecting religious phrasing.

9. **If the source mixes registers** → pick the higher register and apply it consistently.

10. **If a placeholder `{variable}` appears in source** → preserve it byte-for-byte. Do not translate `{count}`, `{name}`, `{file}`. The interpolated value will arrive in Persian (or as the user's data) at runtime.

11. **If ezafe creates ambiguity** (e.g., چند noun chains in a row) → consider restructuring with a comma or relative clause for clarity.

12. **If the source has Arabic-style six-category ICU plurals** → collapse to Persian `one` + `other`, both with singular noun.

Persian is one of the world's great literary languages, with over a thousand years of continuous high-register tradition. Modern Persian UI should feel **clear, polite, and natively Persian** — not like translated Arabic, not like word-for-word English, and never like the awkward calques that betray machine translation. When you get the script right (پ چ ژ گ, Persian ی and ک, ZWNJ), the word order right (SOV with ezafe), the register right (شما formal), and the cultural framing right (Iranian/Shia-respectful without being Arabic), the translation will read naturally to a Persian speaker.
