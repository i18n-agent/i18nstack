---
name: localize-ar
description: Use when translating or localizing source text into Arabic (ar / MSA / ar-SA / ar-EG / ar-AE / ar-LB / ar-MA). Covers RTL handling, ICU zero/one/two/few/many/other plurals, dual number, masculine/feminine gender, non-human plural = feminine singular, sun/moon letters, idafa construct, Arabic punctuation (؟ ، ؛), bidirectional text, religious/Islamic sensitivity, MSA vs regional dialects, and register auto-detection (formal أنت default, حضرتك for very formal).
---

# Translate to Arabic (ar) — High-Fidelity Skill

## Scope & Variants

Arabic is a **diglossic** language: written/formal = **MSA (الفصحى)**, spoken = **dialects (العامية)**. UI/product copy almost always uses **MSA**. Dialects are used only when the product explicitly targets a single region's spoken voice (rare for software).

If a translation target locale is given, follow its variant. Otherwise treat as **MSA** (the safe pan-regional default) and surface differences only where meaningful.

**Recognized variants:**

| Locale | Name | Use case | Default formality |
|--------|------|----------|-------------------|
| `ar` | MSA (Modern Standard Arabic) | Pan-regional UI, written, business, news | Formal (أنت + masdar) |
| `ar-SA` | Saudi MSA | Saudi-specific products; KSA-localized | Formal (أنت + masdar) |
| `ar-EG` | Egyptian (MSA-leaning or Masri) | Egyptian audience; can lean colloquial in marketing | Formal default, can soften |
| `ar-AE` | UAE/Gulf MSA | UAE/Gulf audience | Formal |
| `ar-LB` | Levantine (or LB MSA) | Lebanon/Syria/Jordan/Palestine | Formal default |
| `ar-MA` | Moroccan/Maghrebi | Morocco/Algeria/Tunisia; **Darija** spoken, MSA written | Formal MSA in writing |

**Critical principle:** When a translation must serve **multiple regions**, ALWAYS pick **MSA** with terminology choices that read naturally across regions. Never use dialect-specific vocabulary in MSA copy.

### When the target locale is unspecified

If the user requests "Arabic" without specifying region/variant, ask once with the option tool:

> Which Arabic variant should I target?
>
> - **MSA (`ar`)** — Recommended. Pan-regional, formal, used in software, news, books, business.
> - **Egyptian (`ar-EG`)** — Egypt-specific. Some loanwords (موبايل) differ from MSA (هاتف محمول).
> - **Saudi (`ar-SA`)** — Saudi/Gulf-leaning MSA; SAR currency; Hijri calendar friendly.
> - **Levantine (`ar-LB`)** — Lebanon/Syria/Jordan/Palestine MSA.
> - **Moroccan/Maghrebi (`ar-MA`)** — Morocco-region MSA; French loanwords may bleed in.
> - **UAE (`ar-AE`)** — UAE-specific MSA; AED currency.

Default to MSA if no answer.

---

## Register Auto-Detection (Apply Before Translating)

Arabic formality is set by **pronoun choice**, **imperative form**, and **lexical register**. Auto-detect from the source text:

| Source signal | Target register |
|---------------|-----------------|
| Contractions (`you're`, `don't`), exclamations, casual lexicon (`Hey!`, `Let's…`), emoji, marketing voice | **Soft formal** — أنت + direct imperative (اضغط, احفظ); allow short verbal phrases. Buttons stay masdar (حفظ). |
| Neutral product/UI prose (`Click to save`, `Your file was uploaded`) — DEFAULT | **Standard formal MSA** — أنت + masdar buttons; status uses تم/جارٍ; "Please" → الرجاء + masdar in modal/dialog confirmations only. |
| Legal/financial/government/very-formal business (`Kindly be advised`, terms of service, banking) | **Elevated formal** — حضرتك / حضرتكم for "you"; verbose courtesy (يُرجى التكرم بـ, نتشرف بـ); religious-respectful framings allowed; 3rd-person verb agreement with حضرتك. |

**Hard rule: never mix levels in the same string.** If the source mixes registers (rare), pick the higher one.

**Hard rule: never inject religious phrases (إن شاء الله, ما شاء الله, بإذن الله) into a translation unless the source text already invokes that semantic.** They are not generic politeness fillers in MSA software copy.

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. Non-human plural takes FEMININE SINGULAR adjective/verb (severity 2.5)

This is **the** most-failed Arabic grammar rule by AI systems and non-native speakers. **Memorize it.**

> Any plural noun that refers to non-human entities (files, settings, products, accounts, files, photos, items, computers, etc.) takes a **feminine SINGULAR** adjective AND a **feminine SINGULAR** verb.

| Wrong | Correct | Why |
|-------|---------|-----|
| ملفات جديدين | **ملفات جديدة** | Files (non-human pl.) → feminine sg. adjective |
| الأنظمة متقدمين | **الأنظمة متقدمة** | Systems (non-human pl.) → feminine sg. |
| المنصات الجدد | **المنصات الجديدة** | Platforms (non-human pl.) → feminine sg. |
| الملفات يتم حذفهم | **الملفات تُحذف / يتم حذف الملفات** | Verb agrees as fem. sg. with non-human pl. subject |
| الإعدادات حُفظوا | **الإعدادات حُفظت** | Settings (non-human pl.) → fem. sg. verb |

Human plurals follow normal m./f. plural rules (المستخدمون الجدد, المستخدمات الجديدات). Non-human plurals do NOT.

### 2. Number agreement (3–10 = reverse-gender + plural genitive) (severity 2.0)

| Count | Pattern | Example (masc. noun ملف) | Example (fem. noun منصة) |
|-------|---------|--------------------------|--------------------------|
| 1 | masdar/sg., agreeing gender | ملف واحد | منصة واحدة |
| 2 | **dual** (-ان nom. / -ين acc./gen.) | ملفان / ملفين | منصتان / منصتين |
| 3–10 | number takes **opposite** gender + **plural genitive** noun | **ثلاثة** ملفات (m. noun → fem. number form) | **ثلاث** منصات (f. noun → masc. number form) |
| 11–99 | number + **singular accusative tanween** noun | عشرون ملفًا | خمس وعشرون منصةً |
| 100+ | number + **singular genitive** noun | مئة ملف | مئة منصة |

Common errors: `ثلاث ملفات` (should be ثلاثة ملفات), `5 ملفين` (should be 5 ملفات), `2 ملفات` (should be ملفان).

### 3. Definiteness agreement: both definite or both indefinite (severity 2.0)

Noun + adjective MUST match in definiteness.

- `الملف الجديد` ✓ (both definite — "the new file")
- `ملف جديد` ✓ (both indefinite — "a new file")
- `الملف جديد` ✗ → this is a **sentence**, not a phrase: "The file is new." If you meant the noun phrase, fix to `الملف الجديد`.

### 4. RTL direction + bidirectional text (severity 2.0 — placeholders)

- Arabic flows **right-to-left**. Punctuation goes at the **end** of the sentence in logical order (which displays on the left visually): `تم الحفظ.` ✓ not `.تم الحفظ`.
- **Placeholders `{var}`, `{{name}}`, `<tag>`, URLs, emails, code identifiers, file names, numbers** must be preserved exactly as in source. Do NOT translate `file.txt`, `localhost:3000`, `<b>`, `npm`, `API`, `GitHub`, etc.
- For mixed Arabic/Latin text where bidi rendering can confuse the user (a Latin filename inside an Arabic sentence), surround the LTR run with **LRM (U+200E)** or wrap with explicit Unicode directional embeddings if the surface needs it. Most UI frameworks handle this automatically — do **not** sprinkle LRM/RLM characters into translation strings unless you know the framework does not auto-handle.
- Numerals: when the surrounding UI uses Eastern Arabic-Indic digits (٠-٩), use them. Otherwise use Western digits (0-9). **Be consistent within a string** — never mix `5 ملفات` and `٧ منصات` in the same screen.

### 5. Arabic punctuation, not Latin (severity 2.0)

| Latin (wrong in Arabic text) | Arabic (correct) | Unicode |
|------------------------------|------------------|---------|
| `?` | **`؟`** | U+061F |
| `,` | **`،`** | U+060C |
| `;` | **`؛`** | U+061B |
| `%` | `٪` (optional, U+066A) or `%` accepted | |

Period `.`, colon `:`, exclamation `!`, parentheses `( )`, square brackets `[ ]`, quotation marks `" "` or `« »` stay as-is (or use guillemets `« »` for style consistency).

### 6. Religious / Islamic sensitivity (severity 2.5)

Critical for **all Arabic content**, not just religious text. The Arabic-reading audience is overwhelmingly Muslim, and the language itself carries Islamic register.

**Idioms with Christian/biblical/pagan/secular-Western origins MUST be re-conceptualized, never literally translated:**

| English idiom | ✗ Literal calque | ✓ Culturally adapted |
|---------------|------------------|----------------------|
| cross to bear | صليب يحمله | عبء يتحمله / مسؤولية ثقيلة |
| holy grail | الكأس المقدسة | الهدف الأسمى / الغاية المنشودة |
| good Samaritan | السامري الصالح | شخص محسن / فاعل خير |
| blessing in disguise | (literal) | نعمة مقنّعة / خير في باطنه |
| act of God | عمل الله | قوة قاهرة / حدث طبيعي (legal term) |
| baptism of fire | معمودية النار | اختبار صعب / تجربة قاسية |
| Pandora's box | صندوق باندورا | فتح باب الشر / عواقب وخيمة |
| Achilles' heel | كعب أخيل | نقطة ضعف |
| knock on wood | (literal) | الله يحفظنا / بإذن الله |
| fingers crossed | (literal) | إن شاء الله / نتمنى |
| bring home the bacon | (literal — pork!) | يكسب رزقه / ينجح في المهمة |
| champagne problems | (literal) | مشاكل الرفاهية / مشاكل تافهة |
| Christmas miracle | معجزة عيد الميلاد | معجزة / شيء رائع |

**Halal sensitivity:** Avoid casual metaphors involving pork (lard, bacon, ham), alcohol (champagne, beer, wine), or gambling that are not the literal subject of the source text.

**Finance:** "Interest" → `فائدة` is ambiguous between halal (غير ربوية) and haram (ربوية). For neutral copy, `فائدة` is fine. For Islamic-banking products, explicitly disambiguate. Never market `ربا` (usury) positively.

**Calendar:** Don't assume Gregorian calendar / Western holidays are universal. For dates in Saudi/Gulf contexts, consider Hijri (التاريخ الهجري) — see Cultural Conventions below.

**Dating/relationships:** `dating app` → `تطبيق تعارف` or `تطبيق للزواج` (depending on context), not literal `تطبيق للمواعدة` (which carries inappropriate connotation in conservative regions).

**Gender:** Arabic has grammatical gender on EVERYTHING. The default audience-facing pronoun is masculine (`أنت / يمكنك`) when the audience is mixed/unknown. If the product is explicitly targeting women only, switch to feminine throughout (`أنتِ / يمكنكِ`). **Never mix** within a string.

**Imagery in copy** (if referenced verbally): mentions of "she wore [revealing item]" or "drink at the bar" carry sensitivity — translate the function, not the literal scene, where possible.

### 7. Verb-Subject-Object (VSO) preferred for new info; SVO for topicalization (severity 1.5)

- **VSO** is the most natural Arabic word order: `يفتح المستخدم الملف` ("Opens the user the file" → "The user opens the file").
- **SVO** is also grammatical and very common in modern Arabic, especially when the subject is topicalized: `المستخدم يفتح الملف`.
- **Never** put adjective before noun: `جديد ملف` ✗ → `ملف جديد` ✓.

### 8. Idafa (إضافة) construct — possessive/compound noun chain (severity 1.5)

When two nouns form a possessive/compound (`the manager of the files`, `the dashboard's settings`):

- **First** noun: drops `ال`, drops nunation (tanween). Just bare form.
- **Second** noun: takes `ال` if the whole phrase is definite; takes genitive ending.

| Wrong | Correct | Meaning |
|-------|---------|---------|
| المدير الملفات | **مدير الملفات** | the file manager |
| لوحة تحكم | **لوحة التحكم** | the control panel (idafa, definite) |
| لوحة التحكم الإعدادات | **إعدادات لوحة التحكم** | the control panel's settings |

### 9. ICU plurals — Arabic uses ALL SIX categories (severity 2.5)

This is **uniquely Arabic** and most translation tools get it wrong by treating Arabic like English (one/other).

```icu
{count, plural,
  zero {لا توجد ملفات}
  one {ملف واحد}
  two {ملفان}
  few {# ملفات}
  many {# ملفًا}
  other {# ملف}
}
```

**Category boundaries (CLDR official):**
- `zero`: n = 0
- `one`: n = 1
- `two`: n = 2
- `few`: n % 100 = 3..10
- `many`: n % 100 = 11..99
- `other`: everything else (including 100, 200, 1000, etc.)

For each ICU plural variable: if the source has only `{count, plural, one {...} other {...}}`, you MUST expand to all six Arabic categories — never leave categories out, even if the English source omits them.

---

## Pronouns, "You", and Possessives

### Personal pronouns

| English | Arabic (formal default — masc.) | Feminine variant | Very formal |
|---------|----------------------------------|------------------|-------------|
| you (sg.) | أنت | أنتِ | حضرتك (m.) / حضرتك (f.) |
| your (sg.) | -ك (masc. suffix) | -كِ (fem. suffix) | حضرتك / حضرتكم (pl. polite) |
| you (pl. courtesy) | أنتم | أنتن (all-women plural) | حضراتكم / سيادتكم |
| we | نحن | نحن | نحن (no change) |
| I | أنا | أنا | أنا |

### Verb endings (2nd-person sg.)

| Form | Masc. | Fem. |
|------|-------|------|
| present "you do X" | تفعل (tafʿalu) | تفعلين (tafʿalīna) |
| imperative "do X!" | افعل (ifʿal) | افعلي (ifʿalī) |
| past "you did X" | فعلتَ (faʿalta) | فعلتِ (faʿalti) |

**For software UI: default to masculine 2nd-person singular** (`يمكنك`, `اضغط`, `أنت`) unless the audience is clearly women-only.

### Possessive suffixes

English `your file` → Arabic `ملفك` (masc.) or `ملفكِ` (fem.). The pronoun is a suffix, not a separate word.

| English | Arabic |
|---------|--------|
| my account | حسابي |
| your account (m.) | حسابك |
| your account (f.) | حسابكِ |
| your account (pl.) | حسابكم |
| our account | حسابنا |
| their account | حسابهم |

---

## Grammar Reference

### Two genders (مذكر / مؤنث)

**Feminine markers** (almost always feminine):
- ends in `-ة` (taa marbuta): منصة, خدمة, شركة, لغة
- ends in `-اء`: صحراء (but check — some are masc.)
- ends in `-ى` (alif maqsura): ذكرى, شكوى

**Inherently feminine** without marker:
- Country names: مصر, السعودية, ألمانيا (use feminine adjective)
- Body parts in pairs: عين, يد, أذن
- Some specific nouns: شمس, نار, ريح, نفس

**Default masculine**: everything else.

### Adjective agreement table

| Subject | Adjective form |
|---------|---------------|
| Masculine singular (ملف) | masculine sg. (جديد) |
| Feminine singular (منصة) | feminine sg. (جديدة) |
| Human masculine plural (مستخدمون) | masculine plural (جُدُد / جديدون) |
| Human feminine plural (مستخدمات) | feminine plural (جديدات) |
| **Non-human plural** (ملفات, أنظمة) | **feminine SINGULAR (جديدة)** ⚠ |
| Dual masc. (ملفان) | dual masc. (جديدان) |
| Dual fem. (منصتان) | dual fem. (جديدتان) |

### Verb agreement

Verbs agree with subject in **gender + number**. For non-human plural subjects, verb is feminine singular: `الملفات حُفظت` (not حُفظوا).

### Sun and moon letters (definite article assimilation)

The `ال` (the) is pronounced differently depending on the next letter — but **written the same**. In writing, you never need to change spelling. Just be aware that in reading:
- **Sun letters** (ت ث د ذ ر ز س ش ص ض ط ظ ل ن): `ل` assimilates to next consonant (الشمس reads as "ash-shams").
- **Moon letters** (everything else): `ل` is pronounced normally (القمر = "al-qamar").

Practical impact in writing: **none**. The spelling stays `ال`.

### Cases (إعراب)

Three cases: nominative (مرفوع), accusative (منصوب), genitive (مجرور). In modern unvocalized text:
- **Sound masculine plural**: nom. `-ون` (مستخدمون), acc./gen. `-ين` (مستخدمين).
- **Dual**: nom. `-ان` (ملفان), acc./gen. `-ين` (ملفين).
- **Sound feminine plural**: nom. `-ات` (ملفات / ملفاتٌ), acc. `-ات` (ملفاتٍ — same letters), gen. `-ات` (ملفاتٍ).
- **Singular nouns**: case shows only in tanween (rarely written in UI). Drop tanween in headlines/buttons.

For UI copy: most case endings are unmarked. Focus on **dual vs plural** distinction and **definiteness agreement**.

### Common particles + governed case

| Particle | Meaning | Governs | Example |
|----------|---------|---------|---------|
| في | in | genitive | في الملف |
| على | on | genitive | على المنصة |
| إلى | to | genitive | إلى الإعدادات |
| من | from | genitive | من المستخدم |
| بـ | by/with | genitive | بكلمة المرور |
| لـ | for/to | genitive | للمستخدم |
| إنّ | indeed/that | accusative | إنّ الملفَ جديد |
| أنّ | that (sub.) | accusative | أعلم أنّ الملفَ جديد |
| كان | was | accusative on predicate | كان الملفُ جديدًا |

---

## UI Conventions

### Buttons → masdar (verbal noun)

Single-word action buttons use the **masdar** form, not imperative:

| English | ✓ Arabic (masdar) | ✗ Imperative (wrong for buttons) |
|---------|-------------------|----------------------------------|
| Save | حفظ | احفظ |
| Cancel | إلغاء | ألغِ |
| Delete | حذف | احذف |
| Send | إرسال | أرسل |
| Edit | تعديل | عدّل |
| Search | بحث | ابحث |
| Confirm | تأكيد | أكّد |
| Continue | متابعة | تابع |
| Submit | إرسال / تأكيد | — |
| Sign in | تسجيل الدخول | — |
| Sign out | تسجيل الخروج | — |
| Sign up | إنشاء حساب / التسجيل | — |
| Next | التالي | — |
| Back | رجوع / السابق | — |
| Done | تم / إنهاء | — |
| OK | موافق | — |
| Close | إغلاق | — |
| Upload | رفع | — |
| Download | تنزيل | — |
| Refresh | تحديث | — |
| Settings | الإعدادات | — |

**Multi-word action phrases** can use imperative: `اضغط هنا` (click here), `اختر ملفًا` (choose a file).

### Status messages (progressive / completion / empty)

**Progressive (in-flight):** `جارٍ + masdar` or `يتم + masdar`
- جارٍ التحميل... (Loading…)
- جارٍ الحفظ... (Saving…)
- يتم الإرسال... (Sending…)
- الرجاء الانتظار... (Please wait…)

**Completion:** `تم + masdar` or `اكتمل + noun`
- تم الحفظ بنجاح. (Saved successfully.)
- اكتمل التحميل. (Upload complete.)
- تم! (Done!)

**Failure:** `فشل + masdar` or `لم يتم + masdar` or `تعذّر + masdar`
- فشل الحفظ. (Save failed.)
- تعذّر الاتصال بالخادم. (Could not connect to server.)
- لم يتم العثور على الملف. (File not found.)

**Empty state:** `لا توجد X` / `لا يوجد X` (gender agreement!)
- لا توجد نتائج. (No results.)
- لا يوجد محتوى لعرضه. (No content to display.)
- لا توجد ملفات بعد. (No files yet.)
- لا توجد إشعارات. (No notifications.)

**Validation/Field errors:** nominal description
- هذا الحقل مطلوب. (This field is required.)
- الصيغة غير صالحة. (Invalid format.)
- كلمة المرور قصيرة جدًا. (Password too short.)

**Action instructions:** imperative
- أدخل كلمة المرور. (Enter your password.)
- اختر لغة واحدة على الأقل. (Choose at least one language.)
- حاول مرة أخرى. (Try again.)

### Drag-and-drop terminology

- drag → اسحب
- drop → أفلت (NOT حرر = "liberate" — wrong sense)
- release → حرّر / أفلت
- Combined: `اسحب وأفلت الملف هنا` (Drag and drop the file here).

### File picker

- file picker action → `اختر ملفًا` or `حدد ملفًا` (action-oriented, NOT تصفح which means "browse" for navigation).
- `Browse files` (when meaning "navigate through") → `تصفح الملفات`. But for an upload trigger, prefer `اختر ملفًا`.

### Quantities and "more"

- `+25 languages` → **`أكثر من 25 لغة`** or `ما يزيد عن 25 لغة` (not `+25 لغة` — looks unnatural).
- `+{count} more` → **`و{count} لغات أخرى`** or `والمزيد ({count})`.
- `25+` (when used as a count) → `أكثر من 25` or `25 أو أكثر`.

### Validation / error messages — include next steps

| Source | ✗ Bare | ✓ With next step |
|--------|--------|------------------|
| File not found. | لم يُعثر على الملف. | لم يُعثر على الملف. تحقق من المسار. |
| Network error. | خطأ في الشبكة. | خطأ في الشبكة. أعد المحاولة. |
| Invalid email. | بريد غير صالح. | البريد الإلكتروني غير صالح. تحقق من العنوان. |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation (locked)

| Mark | Arabic | Unicode | Notes |
|------|--------|---------|-------|
| Question mark | **؟** | U+061F | Always at end (RTL = appears on left visually) |
| Comma | **،** | U+060C | Replaces Latin comma in Arabic text |
| Semicolon | **؛** | U+061B | Replaces Latin semicolon |
| Period | `.` | U+002E | Same as Latin |
| Colon | `:` | U+003A | Same as Latin |
| Exclamation | `!` | U+0021 | Same as Latin |
| Quotation marks | `«…»` (preferred) or `"…"` | U+00AB/U+00BB | Either works; be consistent |
| Percent | `%` (or `٪` U+066A) | | Western `%` accepted in UI |

**No space before `؟ ، ؛ : !`** (unlike French).

**Bidi note:** Arabic punctuation displays at the end of the sentence in logical order. Editors and text engines handle visual placement.

### Numerals — two systems

| Western (Hindu-Arabic) | Eastern Arabic-Indic |
|------------------------|----------------------|
| 0 1 2 3 4 5 6 7 8 9 | ٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩ |

- **Western 0-9 is standard** for software UI, business, scientific contexts across all Arabic regions.
- **Eastern Arabic-Indic** numerals are used in some traditional/print/religious contexts and certain government docs (especially KSA, Egypt traditionally).
- **Choose ONE per locale and be consistent.** Most modern Arabic UI uses Western digits.

### Numbers, thousands, decimals

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | `,` (comma) or `٬` (Arabic thousands sep U+066C) | 1,234 / ١٬٢٣٤ |
| Decimal separator | `.` (period) or `٫` (Arabic decimal sep U+066B) | 1,234.56 / ١٬٢٣٤٫٥٦ |
| Negative numbers | `-25` (minus before number, LTR-protected) | -25 |
| Percentages | `25%` (or `٢٥٪`) | 25% |

### Currency — by region

| Locale | Currency | Symbol / Code | Format |
|--------|----------|---------------|--------|
| `ar-SA` | Saudi Riyal | ر.س / SAR | 99.99 ر.س |
| `ar-AE` | UAE Dirham | د.إ / AED | 99.99 د.إ |
| `ar-EG` | Egyptian Pound | ج.م / EGP / £ | 99.99 ج.م |
| `ar-MA` | Moroccan Dirham | د.م / MAD | 99.99 د.م |
| `ar-LB` | Lebanese Lira | ل.ل / LBP | 99.99 ل.ل |
| `ar` (MSA, no region) | USD or context | $ / USD | $99.99 — keep as in source |

Currency symbol typically **follows** the amount in Arabic. Three-letter code (USD, SAR) is always acceptable.

### Dates

| Format | Example | When to use |
|--------|---------|-------------|
| DD/MM/YYYY | 15/01/2024 | Default for all Arabic locales |
| Day + month name + year | 15 يناير 2024 (Gulf/Levant) / 15 جانفي 2024 (Maghreb) | Long form |
| Day + month name + year | 15 كانون الثاني 2024 | Levantine (Syrian-style month names) |
| Hijri | 1445/07/03 هـ / 3 محرم 1445 | KSA, religious, some Gulf gov |
| ISO 8601 | 2024-01-15 | Technical / API contexts only |

**Month names — three systems coexist:**

| # | Modern Arabic (Gulf, mainstream MSA) | Levantine (Syria/Lebanon/Iraq/Jordan) | Maghrebi (Morocco/Algeria/Tunisia) |
|---|--------------------------------------|----------------------------------------|------------------------------------|
| 1 | يناير | كانون الثاني | جانفي / يناير |
| 2 | فبراير | شباط | فيفري / فبراير |
| 3 | مارس | آذار | مارس |
| 4 | أبريل / إبريل | نيسان | أفريل / أبريل |
| 5 | مايو | أيار | ماي / مايو |
| 6 | يونيو | حزيران | جوان / يونيو |
| 7 | يوليو | تموز | جويلية / يوليو |
| 8 | أغسطس | آب | أوت / أغسطس |
| 9 | سبتمبر | أيلول | سبتمبر |
| 10 | أكتوبر | تشرين الأول | أكتوبر |
| 11 | نوفمبر | تشرين الثاني | نوفمبر |
| 12 | ديسمبر | كانون الأول | ديسمبر |

**For MSA pan-regional content:** use the Gulf/mainstream column (يناير, فبراير, مارس…). This is understood everywhere.

### Time

- 12-hour: `2:30 م` (PM) / `2:30 ص` (AM). Period is suffix.
- 24-hour: `14:30`.
- Time goes LTR within Arabic context (display protected).

### Weekdays

| English | Arabic | Notes |
|---------|--------|-------|
| Sunday | الأحد | First day of week in Arabic culture |
| Monday | الاثنين | |
| Tuesday | الثلاثاء | |
| Wednesday | الأربعاء | |
| Thursday | الخميس | |
| Friday | الجمعة | Holy day; weekend in most Arab countries |
| Saturday | السبت | Weekend |

**Week starts on Sunday** in Arabic calendar UI.

---

## Terminology — preferred Arabic terms (MSA-pan-regional)

| English | Arabic preferred | Avoid |
|---------|-------------------|-------|
| user | المستخدم | يوزر |
| account | حساب | أكاونت |
| password | كلمة المرور | باسوورد |
| settings | الإعدادات | السيتنغز |
| dashboard | لوحة التحكم | الداشبورد |
| email | البريد الإلكتروني | الإيميل (informal) |
| link | رابط | لينك |
| browser | المتصفح | البراوزر |
| website | موقع إلكتروني / موقع ويب | الويبسايت |
| folder | مجلد | الفولدر |
| file | ملف | فايل |
| device | جهاز | ديفايس |
| phone (mobile) | هاتف محمول / هاتف ذكي | موبايل (Gulf), محمول (Egypt) |
| computer | حاسوب (formal) / كمبيوتر (acceptable) | — |
| application / app | تطبيق | أبلكيشن |
| update (v.) | تحديث | أبديت |
| save | حفظ | سيف |
| delete | حذف | ديليت |
| upload | **رفع** | ❌ تحميل (ambiguous!) |
| download | **تنزيل** | ❌ تحميل (ambiguous!) |
| sign in / log in | تسجيل الدخول | لوغ إن |
| sign up | إنشاء حساب / التسجيل | ساين أب |
| search | بحث | سيرش |
| click | انقر / اضغط | كليك |
| share | مشاركة | شير |
| profile | الملف الشخصي | بروفايل |
| notifications | الإشعارات | نوتيفيكيشنز |
| privacy | الخصوصية | البرايفسي |
| terms | الشروط | تيرمز |
| support | الدعم / دعم العملاء | السبورت |
| help | المساعدة | الهلب |
| feedback | الملاحظات / الآراء | فيدباك |
| menu | قائمة | مينيو |
| home | الرئيسية | هوم |
| logout / sign out | تسجيل الخروج | لوغ آوت |

**Critical:** `تحميل` is **ambiguous** between upload and download in Arabic. Always use `رفع` (upload) and `تنزيل` (download) to disambiguate.

### Regional terminology drift (only matters for region-locked locales)

| Concept | MSA / KSA / AE | Egypt | Maghreb (informal) | Levant |
|---------|----------------|-------|---------------------|--------|
| mobile phone | هاتف محمول / هاتف ذكي / جوال (KSA) | موبايل / محمول | تيليفون / محمول | موبايل / خلوي |
| computer | حاسوب / كمبيوتر | كمبيوتر | حاسوب / كومبيوتر | كمبيوتر |
| car | سيارة | عربية / سيارة | طوموبيل / سيارة | سيارة |
| street | شارع | شارع | زنقة (informal) / شارع | شارع |
| good (adj.) | جيد / حسن | كويس / جيد | مزيان (Darija) | منيح (Levantine) |
| now | الآن | دلوقتي (colloquial) / الآن | دابا (Darija) / الآن | هلق (Levantine) / الآن |

**For MSA software UI: always use the MSA column** (الآن, جيد, سيارة, etc.). Dialect words are only acceptable when the product brand voice explicitly leans into one region.

### Software-specific terms

| English | Arabic | Notes |
|---------|--------|-------|
| build (software) | بناء / إنشاء / تطوير | "build" in tech context OK as بناء |
| deploy | نشر / إطلاق | نشر is standard |
| pipeline (CI/CD) | خط الإنتاج / مسار / pipeline (keep) | Tech-context-only |
| repository / repo | مستودع | |
| branch (git) | فرع | |
| commit (v.) | حفظ / commit (keep) | OK to keep English in dev tools |
| pull request | طلب سحب | OK to keep `pull request` in dev tools |
| merge | دمج | |
| API | واجهة برمجة التطبيقات (API) | Keep "API" abbreviation, full term parenthetically once |
| endpoint | نقطة نهاية / endpoint | |
| token | رمز / توكن | |
| cache | ذاكرة التخزين المؤقت | |
| log (n.) | سجل | |
| log (v.) — record | تسجيل | |
| sync | مزامنة | |
| webhook | webhook (keep) | |
| source of truth | المرجع الأساسي / المصدر الموثوق | NOT literal "مصدر الحقيقة" |
| listings (app store) | صفحة التطبيق / بطاقة التطبيق | NOT "القوائم" |

### Tech identifiers — keep in Latin script

These MUST stay in Latin script inside Arabic text:
- Programming languages: Python, JavaScript, Go, Rust, Java
- Frameworks: React, Vue, Angular, Next.js, Django
- Tools: Git, GitHub, GitLab, Docker, npm, pip, cargo
- Protocols: HTTP, HTTPS, FTP, SSH, TCP, REST, GraphQL
- File formats: JSON, XML, YAML, CSV, PDF, MP4
- Commands, file paths, URLs, code snippets

```text
✗ يمكنك استخدام جيت لإدارة الكود.
✓ يمكنك استخدام Git لإدارة الكود.

✗ خادم الإنترنت غير متاح.
✓ خادم HTTP غير متاح.
```

---

## Calque / Anti-Pattern List

| ✗ Wrong (calque) | ✓ Correct | Why |
|------------------|-----------|-----|
| الدفع ناجح | تم الدفع بنجاح / اكتمل الدفع | English "Payment Successful" adjective calque; Arabic uses verbal form |
| التحميل مكتمل | تم التحميل / اكتمل التحميل | Same — verbal preferred |
| العملية فاشلة | فشلت العملية / لم تنجح العملية | Verbal form preferred |
| صفر توقف | بدون توقف / بلا انقطاع | "Zero X" English marketing calque |
| صفر أخطاء | بدون أخطاء / خالٍ من الأخطاء | Same |
| على أساس يومي | يوميًا / كل يوم | "On a daily basis" — use adverb |
| من حيث الأداء | فيما يتعلق بالأداء / بخصوص الأداء | "In terms of" — use proper preposition |
| في حالة ما إذا | إذا / في حال | Verbose — simplify |
| من أجل أن نستطيع | لكي / حتى نستطيع | Verbose purpose clause |
| الملف لا يمكن أن يتم إيجاده | لم يُعثر على الملف / تعذّر إيجاد الملف | Passive calque; use direct passive |
| بشكل افتراضي القيمة | القيمة الافتراضية | Wrong word order |
| مدفوع بالذكاء الاصطناعي | مدعوم بالذكاء الاصطناعي / يعمل بالذكاء الاصطناعي | "X-powered" calque |
| واعٍ بالسياق | مدرك للسياق / يراعي السياق | "context-aware" calque |
| صديق للمستخدم | سهل الاستخدام / بديهي | "user-friendly" calque |
| قاعدة بيانات URLs | قاعدة بيانات الروابط / قاعدة بيانات عناوين URL | Mixed Arabic-English plural |
| نقطة نهاية الـAPI | نقطة نهاية API / نقطة نهاية واجهة برمجة التطبيقات | Use full Arabic or keep Latin "API" cleanly |
| يتم القيام بعملية الحذف | يُحذف | Over-verbalization; use direct passive |
| الولايات المتحدة الأمريكية | أمريكا / الولايات المتحدة | Use short form in UI |
| المملكة المتحدة لبريطانيا العظمى | المملكة المتحدة / بريطانيا | Short form |
| الكأس المقدسة (for "holy grail") | الهدف الأسمى | Religious-origin calque |
| كعب أخيل | نقطة ضعف | Pagan-origin calque |
| اكسر ساقك! (break a leg!) | بالتوفيق! / حظًا سعيدًا! | Idiom not literal |
| قطعة كعكة (piece of cake) | سهل جدًا / أسهل من شربة ماء | Idiom |
| اقتل عصفورين بحجر واحد | تحقيق هدفين بضربة واحدة | Idiom; literal exists but feels translated |

### Passive voice — be sparing

Arabic has a true passive (يُحفظ, يُحذف, يُرسل) with diacritics. In modern unvocalized text it looks identical to active voice and can confuse readers. The English calque `يتم + masdar` (`يتم الحفظ`) overuses this construction. Rule of thumb:

- **Prefer active voice** when possible: `نحفظ ملفك تلقائيًا.`
- **Use direct passive** for short statuses where actor is unimportant: `يُحفظ تلقائيًا.`
- **Reserve `يتم + masdar`** for cases where rephrasing is awkward, and limit to ~10% of strings.
- **Never stack** `يتم + يتم`: `يتم القيام بعملية الحذف` ✗ → `يُحذف` ✓.

### False friends

| Arabic | Means | Common English misuse |
|--------|-------|------------------------|
| أكيد | "certainly" / "of course" | NOT "actually" — for "actually" use **في الواقع / فعليًا** |
| في النهاية | "at the end" (temporal) | NOT "eventually" — for "eventually" use **في نهاية المطاف** |
| تحميل | ambiguous (up or down) | NOT for upload OR download alone — use **رفع** (up) or **تنزيل** (down) |
| لطيف | "nice/kind" (about a person) | NOT for "nice feature" — use **رائع / جميل** |

---

## Custom Sections

### Bidirectional (BiDi) text — when to add markers

Most rendering engines (browsers, mobile OSes) handle bidi correctly when:
- The Arabic text is in an RTL container (`dir="rtl"`).
- Numbers and Latin runs are short.

**Problem cases** that may need explicit markers:
- Arabic sentence containing a filename (`file.txt`) followed by Arabic punctuation — punctuation can stick to the wrong side.
- Arabic sentence ending with a parenthetical that contains Latin.
- Number with parenthetical unit: `(50 MB)` inside Arabic text.

**Markers** (use sparingly, only when surface confirms wrong rendering):
- LRM (U+200E) — Left-to-Right Mark
- RLM (U+200F) — Right-to-Left Mark
- LRE / RLE / PDF — directional embeddings (deprecated; use LRI/RLI/PDI in new code)

**Best practice in translation strings:** trust the framework. Only add markers when QA confirms a rendering bug.

### Hashtags, mentions, URLs in copy

- `#hashtag` (Latin) → `#وسم_عربي` (Arabic hashtag) where appropriate; Latin hashtags stay Latin.
- `@username` stays as-is.
- URLs stay LTR within RTL context — most engines handle this. Don't translate domain names.

### Politeness and "please"

- `الرجاء + masdar` for formal modals and requests: `الرجاء إدخال كلمة المرور.`
- `من فضلك + verb` is conversational/Egyptian-leaning and OK in UI: `من فضلك أدخل كلمة المرور.`
- `يُرجى + masdar` is more elevated/formal still: `يُرجى التحقق من البريد الإلكتروني.`

Pick one register and stay consistent.

### Names and addresses

- Personal names: transliterate respectfully. `John` → `جون`, `Maria` → `ماريا`. Don't translate.
- Country names: use common short forms in UI (أمريكا, ألمانيا, السعودية, مصر), full diplomatic name only for forms requiring it.
- Use `الإمارات` not `الإمارات العربية المتحدة` in UI unless legally required.

### Cost / quantity expression order

In RTL context, lead with the amount, not the unit:
- ✗ `# لغة 5 رصيد` (amount buried)
- ✓ `التكلفة: 5 رصيد لـ # لغة` (amount prominent)

### FOR vs PER — critical distinction

| Source | ✓ Translation | Meaning |
|--------|---------------|---------|
| for 25 languages (total) | لـ 25 لغة / 25 لغة | Total scope |
| per language (rate) | لكل لغة / للغة الواحدة | Per-unit rate |

`لكل` is **always** per-unit. Never use it for total scope. Pricing pages where this is mixed up are an auto-fail.

---

## Religious / Sensitive Topics — Decision Matrix

| Content type | Rule |
|--------------|------|
| Religious copy (Quran refs, prayer apps) | Stay close to source theological wording; consult subject experts |
| Generic UI / SaaS | Use neutral MSA; avoid Western religious idioms; default to halal-safe metaphors |
| Marketing/lifestyle | Adapt non-halal references (alcohol, pork); soften superstition; gender-respectful imagery |
| Dating / relationships | Frame as تعارف (acquaintance) or زواج (marriage), context-dependent |
| Banking / finance | Disambiguate ربا (usury) vs فائدة (interest); be explicit if product is Islamic-finance |
| News / journalism | Source register preserved; flag culturally loaded terms for review |
| Gaming / fantasy | Western mythology can stay (Greek gods, etc.) but reframe heavy Christian symbols |
| Holiday / celebration | Don't assume Gregorian holidays universal; recognize Islamic holidays (رمضان, العيد) |

---

## Self-Check Checklist (Run Before Returning Output)

### Accuracy (auto-fail on miss)

- [ ] **Non-human plural agreement**: every plural inanimate subject uses **feminine singular** adjective and verb.
- [ ] **Number agreement**: 1 (sg.), 2 (dual -ان/-ين), 3-10 (reverse gender + pl. gen.), 11-99 (sg. acc. tanween), 100+ (sg. gen.).
- [ ] **Definiteness**: noun and adjective both have ال or both don't (الملف الجديد ✓).
- [ ] **Gender**: feminine markers identified; agreement consistent on adj./verb/pronoun.
- [ ] **Idafa construct**: first noun bare (no ال), second noun definite if whole phrase is definite.
- [ ] **ICU plurals**: ALL SIX categories (zero/one/two/few/many/other) present when the source has plural variants.
- [ ] **Placeholders**: every `{var}`, `{{var}}`, `<tag>`, URL, email, identifier preserved exactly.
- [ ] **Latin tech identifiers**: Git, API, JSON, npm, React etc. stay in Latin script.
- [ ] **Punctuation**: `؟ ، ؛` not `? , ;`. No space before any punctuation.
- [ ] **Numerals consistent**: all Western (0-9) or all Eastern Arabic (٠-٩) within a string.
- [ ] **RTL direction**: punctuation at logical end of sentence (period after the last word).
- [ ] **No mixed dialect** in MSA copy.
- [ ] **FOR vs PER**: لـ for total, لكل for rate — never mixed.

### Register

- [ ] Source register detected and matched (soft formal / standard / elevated formal).
- [ ] No mid-string mixing of أنت / حضرتك / الرجاء + direct imperative.
- [ ] No religious phrase (إن شاء الله, ما شاء الله) injected unless source already invokes it.
- [ ] No casual non-halal metaphors (alcohol, pork, gambling) added.

### UI conventions

- [ ] Buttons use masdar (حفظ, إلغاء, حذف), not imperative.
- [ ] Progressive status uses جارٍ + masdar (جارٍ التحميل…).
- [ ] Completion uses تم + masdar (تم الحفظ بنجاح), not adjective (الحفظ ناجح ✗).
- [ ] Empty state uses لا توجد / لا يوجد + specific noun, not bare فارغ.
- [ ] Error messages include next-step instruction when applicable.
- [ ] File picker uses اختر/حدد, not تصفح.
- [ ] Drag-drop uses اسحب + أفلت (not حرر).
- [ ] Quantity expression: أكثر من 25 (not 25+); و{count} أخرى (not +{count}).

### Naturalness

- [ ] No English calques (صفر X, مدفوع بـ X, صديق للمستخدم, على أساس X).
- [ ] No `يتم + masdar` overuse — at most ~10% of statuses; prefer active or direct passive (يُحفظ).
- [ ] Idioms culturally adapted (no صليب يحمله, الكأس المقدسة, اكسر ساقك).
- [ ] رفع/تنزيل distinction respected (never ambiguous تحميل).
- [ ] Word order: VSO or SVO, adjective AFTER noun.
- [ ] Cost order: amount first, unit second.
- [ ] Proper noun short forms (أمريكا, بريطانيا, الإمارات), not diplomatic long forms.

### Regional (when locale-specific)

- [ ] Currency symbol matches locale (ر.س / د.إ / ج.م / etc.).
- [ ] Date format matches locale (DD/MM/YYYY default; Hijri only when context demands).
- [ ] Month names match regional convention (Gulf vs Levantine vs Maghrebi).
- [ ] No dialect words in MSA copy (دلوقتي, هلق, دابا, مزيان must NOT appear in MSA).

---

## Worked Example — Standard formal MSA (default)

**Source (English, neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Auto-detect register:** Standard product UI, exclamation OK, neutral lexicon → **Standard formal MSA**.

**Translation (MSA, masculine default):**

> أهلًا بعودتك! لديك 3 ملفات جديدة في حسابك. اضغط **متابعة** لمراجعتها أو **إلغاء** للبقاء هنا. جارٍ حفظ تغييراتك…

**Why this works:**
- `3 ملفات جديدة` — number agrees with masc. noun (3 = ثلاثة when written out, but as digit `3 + plural genitive ملفات`); adjective `جديدة` is fem. sg. (non-human plural rule).
- `لديك / حسابك / مراجعتها / تغييراتك` — possessive suffixes attach to nouns (no separate "your" word).
- Buttons in masdar: `متابعة`, `إلغاء`.
- Progressive status: `جارٍ + masdar` → `جارٍ حفظ تغييراتك`.
- Punctuation: Arabic comma `،`? Not needed here. Period at logical end ✓. Exclamation OK (Latin `!`).
- No religious filler injected. No calque. No English loanwords (`فايل / كانسل` would be wrong).

**Same string for women-only audience (e.g., women's health app):**

> أهلًا بعودتكِ! لديكِ 3 ملفات جديدة في حسابكِ. اضغطي **متابعة** لمراجعتها أو **إلغاء** للبقاء هنا. جارٍ حفظ تغييراتكِ…

(All 2nd-person suffixes/endings switched to feminine `-كِ` / `-ي`. Non-human plural agreement unchanged.)

**Elevated formal version (legal / banking):**

> نُرحب بعودتكم. يتوفر في حسابكم 3 ملفات جديدة. يُرجى الضغط على **متابعة** للمراجعة أو **إلغاء** للبقاء في هذه الصفحة. جارٍ حفظ التغييرات…

---

## Worked Example — ICU plural expansion

**Source:**

```icu
You have {count, plural, one {# new message} other {# new messages}}.
```

**Translation (full Arabic plural expansion required):**

```icu
لديك {count, plural,
  zero {لا توجد رسائل جديدة}
  one {رسالة جديدة واحدة}
  two {رسالتان جديدتان}
  few {# رسائل جديدة}
  many {# رسالةً جديدة}
  other {# رسالة جديدة}
}.
```

Notes:
- `زero`: rephrase as "no new messages" (لا توجد رسائل جديدة).
- `one`: singular `رسالة واحدة جديدة`.
- `two`: dual `رسالتان جديدتان` (fem. dual, both noun and adj.).
- `few` (3-10): plural genitive `رسائل` + adj. fem. sg. `جديدة` (non-human plural rule).
- `many` (11-99): sg. acc. tanween `رسالةً` + adj. fem. sg.
- `other` (100+): sg. gen. `رسالة` + adj. fem. sg.

---

## Worked Example — Date formatting across regional locales

**Source:** Last login: January 15, 2024 at 2:30 PM

| Locale | Translation |
|--------|-------------|
| `ar` (MSA pan-regional) | آخر تسجيل دخول: 15 يناير 2024 الساعة 2:30 م |
| `ar-SA` | آخر تسجيل دخول: 15 يناير 2024 الساعة 2:30 م (or Hijri context: 3 رجب 1445 هـ) |
| `ar-LB` (Levantine months) | آخر تسجيل دخول: 15 كانون الثاني 2024 الساعة 2:30 م |
| `ar-MA` (Maghrebi months) | آخر تسجيل دخول: 15 يناير 2024 على الساعة 2:30 م |

(Date format DD month YYYY is universally OK in Arabic UI.)

---

## When in Doubt

1. **Default to MSA, masculine, standard formal, Western digits.**
2. If unsure about regional variant → ask once, default MSA.
3. If unsure about religious/cultural framing → choose the **neutral, halal-safe** option.
4. If unsure about idiom → translate the **function**, not the literal words.
5. If a Latin tech term has no clean Arabic equivalent → **keep it Latin** rather than awkwardly transliterate.
6. If non-human plural agreement looks "wrong" to you because you learned English-Arabic informally → **trust the rule**: non-human plural = feminine singular. Always.
