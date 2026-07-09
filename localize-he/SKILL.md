---
name: localize-he
description: Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Hebrew (he / iw). RTL Semitic language — enforces right-to-left direction with LTR-embedded Latin tech identifiers, two-gender agreement (-ה masculine vs feminine), construct state (סמיכות) over של compound forms, opposite-gender numerals 1-10, ICU one/two/other plurals, definiteness agreement (both noun and adjective need ה), gender-neutral UI patterns (infinitive ללחוץ or plural לחצו over gendered singular), and CRITICAL Jewish religious sensitivity (rewrite Christian/biblical idioms — cross to bear, holy grail, good Samaritan, act of God; adapt non-kosher metaphors — bacon, champagne; soften superstition; respect Shabbat / Hebrew calendar).
---

# Translate to Hebrew (he / iw) — High-Fidelity Skill

## Scope & Variants

Hebrew is essentially **a single standard target** — Modern Israeli Hebrew (`he` / legacy `iw`). There is no significant regional split for product localization:

| Locale | Name | Notes |
|--------|------|-------|
| `he` / `he-IL` | Modern Israeli Hebrew | Default and only meaningful variant for product UI |
| `iw` | Legacy ISO 639-1 code for Hebrew | Deprecated but still appears in some old systems; equivalent to `he` |

**Two register / vocabulary axes** (not regional):

- **Secular vs religious audience** — affects vocabulary (e.g., divine names, calendar references). Default to secular Israeli for general product UI; switch to religiously-aware register when target audience is observant.
- **Modern colloquial vs formal literary** — most UI uses neutral modern register; legal/government can shift to higher register.

**No script variant question to ask** — Hebrew uses the Hebrew alphabet exclusively. Latin script appears only for technical identifiers and brand names embedded in Hebrew text.

---

## Register Auto-Detection (Apply Before Translating)

Hebrew has **no formal/informal pronoun distinction** (no equivalent to vous/Sie/Vi). Both `אתה` (m. sg.) and `את` (f. sg.) are register-neutral. **Formality is expressed through vocabulary choice and sentence structure**, NOT through pronoun.

Auto-detect from source:

| Source signal | Target register |
|---------------|-----------------|
| Casual / conversational / personal (`Hey!`, contractions, emoji, marketing voice) | **Casual modern** — short sentences, modern vocabulary, allow English loans where natural (`אימייל`, `אפליקציה`, `סטטוס`). Use gender-neutral plural imperatives (`לחצו`, `שלחו`). |
| Neutral product UI / docs / consumer software (DEFAULT) | **Neutral modern** — gender-neutral imperatives via **plural** (`לחצו כאן`) or **infinitive** (`ללחוץ כאן`). Avoid mixing singular masculine + feminine imperatives. |
| Legal / banking / government / enterprise | **Formal literary** — longer constructions, native Hebrew over loanwords (`דואר אלקטרוני` over `אימייל`; `יישומון`/`יישום` over `אפליקציה`), use `נא ל...` for polite requests (`נא ללחוץ`). |

**Hard rule (gender-neutral UI): NEVER mix singular masculine and feminine imperatives in the same UI.** This is the most common Hebrew UI failure.

| ✗ Wrong (mixed) | ✓ Correct (consistent) |
|-----------------|------------------------|
| `לחץ כאן` (m.sg) + `שמרי שינויים` (f.sg) | **`לחצו כאן`** + **`שמרו שינויים`** (plural — neutral) |
| `הירשם` (m.sg) + `התנתקי` (f.sg) | **`להירשם`** + **`להתנתק`** (infinitive — neutral) |

**Default for software UI: gender-neutral via PLURAL imperative** (`לחצו, שמרו, שלחו`) OR **infinitive** (`ללחוץ, לשמור, לשלוח`). Pick one approach and stay consistent.

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. RTL direction + bidirectional text (severity 2.5)

- Hebrew flows **right-to-left**. Punctuation goes at the **logical end** of the sentence (displays on the left visually): `הקובץ נשמר.` ✓ — period at logical end, displays as ← `.רמשנ ץבוקה` ← reading right-to-left.
- **Placeholders `{var}`, `{{count}}`, `<tag>`, URLs, emails, code identifiers, file names, numbers, Latin brand names** MUST be preserved exactly and stay LTR within the RTL sentence.
- Most rendering engines (browsers, mobile OSes) handle bidi correctly in `dir="rtl"` containers. **Don't sprinkle LRM/RLM marks into translation strings** unless QA confirms a specific rendering bug.
- Unlike Arabic, Hebrew uses **standard Latin-style punctuation marks** (`?`, `,`, `;`, `.`, `!`) at the same positions — NOT mirrored RTL-specific marks.
- **Hebrew numerals are Latin digits (0-9)** for modern product use (the historical Hebrew gematria letters are only used for dates in religious contexts).

### 2. Two-gender agreement (m. / f.) — adjectives, verbs, possessives (severity 2.5)

Hebrew has TWO grammatical genders. Adjectives and verbs MUST agree with noun gender.

**Feminine markers (almost always feminine):**
- ends in `-ה` (`he`) → `פלטפורמה, אפליקציה, מערכת... wait, מערכת ends in ת`
- ends in `-ת` (`tav`) → `מערכת, תיקייה (also ת), טבלת`
- ends in `-ית` (`-it`) → `ספרייה (book + -iyah/-it)`, `אפשרות`
- ends in `-ות` (`-ut`) → `אפשרות`, `התחברות`
- inherently feminine without marker: paired body parts (`עין, יד, אוזן`), some country names

**Masculine markers (default):** consonant ending, no `-ה`/`-ת` feminine marker.

**Common IT nouns and their gender:**

| Masculine (זכר) | Feminine (נקבה) |
|------------------|------------------|
| קובץ (file) | פלטפורמה (platform) |
| משתמש (user) | אפליקציה (application) |
| שירות (service) | מערכת (system) |
| חשבון (account) | הגדרה (setting — sing.) |
| דפדפן (browser) | תיקייה (folder) |
| קישור (link) | תוכנה (software) |
| ניהול (management) | רשת (network) |
| מסך (screen) | אבטחה (security) |
| תפריט (menu) | התחברות (login) |
| לחצן / כפתור (button) | תקלה (error/fault) |
| שדה (field) | בקשה (request) |
| תהליך (process) | אפשרות (option) |
| מסמך (document) | תמונה (image) |
| נתון (datum) | סיסמה (password) |
| דוא"ל / אימייל (email) | עוגייה (cookie) |
| חיפוש (search) | תוצאה (result) |
| חיבור (connection) | פעולה (action) |

**Critical error patterns:**

| ✗ Wrong | ✓ Correct | Reason |
|---------|-----------|--------|
| פלטפורמה חדש | **פלטפורמה חדשה** | פלטפורמה is f., needs `-ה` adj |
| שירות חדשה | **שירות חדש** | שירות is m. |
| מערכת חדש | **מערכת חדשה** | מערכת is f. |
| קובץ חדשה | **קובץ חדש** | קובץ is m. |
| המערכת עובד | **המערכת עובדת** | Verb must agree f. with f. subject |
| המשתמש פעילה | **המשתמש פעיל** | m. subject takes m. adj |

### 3. Adjective position — AFTER noun (severity 2.0)

Hebrew adjectives FOLLOW the noun (unlike English).

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| חדש קובץ | **קובץ חדש** (a new file) |
| חכמה אפליקציה | **אפליקציה חכמה** (a smart app) |
| מהיר חיבור | **חיבור מהיר** (a fast connection) |

### 4. Definiteness agreement (severity 2.0)

When a noun is definite (carries `ה-`), the adjective ALSO needs `ה-`. When the noun is indefinite, neither has `ה-`.

| ✗ Wrong | ✓ Correct | Meaning |
|---------|-----------|---------|
| הקובץ חדש | **הקובץ החדש** ✓ phrase OR **הקובץ חדש** ✓ sentence | The new file (phrase) vs The file is new (sentence) |
| קובץ החדש | **קובץ חדש** OR **הקובץ החדש** | Match both or neither |
| המערכת חדשה | **המערכת החדשה** (the new system) OR sentence `המערכת חדשה` (the system is new) | |

This is the **same pattern as Arabic** definiteness — but easy to forget when translating from English (which uses `the` separately rather than attached).

### 5. Number agreement — **OPPOSITE gender for numbers 1-10** (severity 2.0)

Hebrew numbers 1-10 use the **opposite gender** of the noun they count. This is uniquely Hebrew and a notorious AI-translator failure.

| # | With masculine noun | With feminine noun |
|---|---------------------|---------------------|
| 1 | אחד | אחת |
| 2 | שניים / שני | שתיים / שתי |
| 3 | שלושה | שלוש |
| 4 | ארבעה | ארבע |
| 5 | חמישה | חמש |
| 6 | שישה | שש |
| 7 | שבעה | שבע |
| 8 | שמונה | שמונה |
| 9 | תשעה | תשע |
| 10 | עשרה | עשר |

**Examples:**

| ✗ Wrong | ✓ Correct | English |
|---------|-----------|---------|
| שלוש קבצים | **שלושה קבצים** | three files (קובץ is m., so number is fem.-looking שלושה) |
| שלושה פלטפורמות | **שלוש פלטפורמות** | three platforms (פלטפורמה is f., so number is masc.-looking שלוש) |
| חמש משתמשים | **חמישה משתמשים** | five users |
| חמישה מערכות | **חמש מערכות** | five systems |

**The "opposite gender" rule sounds backwards but is consistent**: masculine nouns take numbers that LOOK feminine (`-ה` ending), feminine nouns take numbers that LOOK masculine (no `-ה`).

**Numbers 11+** stop having gender opposition (mostly invariable in modern Hebrew UI).

### 6. ICU plurals — one / two / other (severity 2.0)

Hebrew CLDR recognizes a **dual category** (`two`) inherited from biblical Hebrew. In modern usage, it's mostly for genuine duals (eyes, hands, days), but CLDR Hebrew plural rules include:

```icu
{count, plural,
  one {קובץ אחד}
  two {שני קבצים}
  many {# קבצים}
  other {# קבצים}
}
```

**CLDR plural category boundaries** (modern Hebrew):

| Category | Rule | Examples |
|----------|------|----------|
| `one` | n = 1 | 1 |
| `two` | n = 2 | 2 |
| `many` | n = 0, or n = 10..10, 20..20, 30..30… and n ≠ 0,1,2 (rare in UI) | usually fold into `other` |
| `other` | everything else | 0, 3, 4, 5… |

In practice, **most product UI uses one/two/other** and folds `many` into `other`. For UI defaults:

```icu
{count, plural,
  one {קובץ אחד}
  two {שני קבצים}
  other {# קבצים}
}
```

### 7. Construct state (סמיכות) — preferred over `של` (severity 1.5)

Hebrew has a special **construct state** for compound nouns and possession, which is more natural than the `של` (of/possessive) construction.

| ✗ Long form with של | ✓ Construct state (סמיכות) |
|---------------------|----------------------------|
| קבצים של המערכת | **קבצי המערכת** (the system's files) |
| הגדרות של המערכת | **הגדרות המערכת** (system settings) |
| פלטפורמה של OneSky | **פלטפורמת OneSky** (OneSky platform) |
| מנהל של הקבצים | **מנהל הקבצים** (the file manager) |
| לוח של הבקרה | **לוח הבקרה** (the dashboard) |

**Form changes in construct:**
- Masculine plural `-ים` → `-י`: `קבצים` → `קבצי...` (the X's files: `קבצי המערכת`)
- Feminine singular `-ה` → `-ת`: `פלטפורמה` → `פלטפורמת...` (`פלטפורמת OneSky`)
- Feminine plural `-ות` → `-ות` (stays the same): `הגדרות` → `הגדרות המערכת`

The construct state reads more idiomatically than `של` chains. Use it for technical compounds.

### 8. Plural forms by gender (severity 1.5)

| Gender | Singular | Plural | Example |
|--------|----------|--------|---------|
| Masculine | קובץ | קבצים | קובץ → קבצים (files) |
| Feminine | פלטפורמה | פלטפורמות | פלטפורמה → פלטפורמות (platforms) |
| Some m. nouns take f. plural | אבא | אבות | (irregular) |
| Some f. nouns take m. plural | שנה (year) | שנים | (irregular) |

Adjective agreement extends to plural:
- m. pl. adj: `-ים` — `קבצים חדשים` (new files)
- f. pl. adj: `-ות` — `פלטפורמות חדשות` (new platforms)

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| פלטפורמות חדש | **פלטפורמות חדשות** |
| קבצים חדשות | **קבצים חדשים** |

### 9. Religious / Jewish cultural sensitivity (severity 2.5)

**CRITICAL for ALL Hebrew content**, not just religious. The Hebrew-reading audience includes secular Israelis (the majority) plus observant Jewish populations worldwide — and Hebrew itself carries strong religious-cultural associations because it is the language of Jewish scripture.

#### Divine names

- Use **`השם`** ("the Name") or **`ה'`** (abbreviated) instead of writing the full Tetragrammaton in non-sacred contexts.
- In casual / secular UI, generally avoid invoking divine names altogether.

#### Christian/biblical-origin idioms — MUST be rewritten, NOT literally translated

Many English idioms have Christian roots that are inappropriate to render literally in Hebrew. The Hebrew-speaking audience reads these literally as alien religious references.

| English idiom | ✗ Literal calque | ✓ Culturally adapted |
|---------------|------------------|----------------------|
| cross to bear | צלב לשאת | **נטל כבד** / **משא שיש לשאת** |
| holy grail | הגביע הקדוש | **המטרה העליונה** / **היעד הנכסף** |
| good Samaritan | שומרוני טוב | **אדם טוב לב** / **בעל חסד** (note: שומרוני is a real ancient Jewish group — the biblical parable framing is what's loaded) |
| blessing in disguise | ברכה במסווה | **ברכה בהסוואה** / **טוב שהוסתר** |
| act of God | מעשה אלוהים | **כוח עליון** / **אירוע טבעי** (legal: כוח עליון) |
| baptism of fire | טבילת אש | (acceptable as metaphor in modern Hebrew, but verify context) → **מבחן אש** |
| Pandora's box | תיבת פנדורה | (Greek myth, generally acceptable in secular Hebrew) — but consider **פתיחת מקור צרות** for plain prose |
| Achilles' heel | עקב אכילס | (Greek myth, fully naturalized in Hebrew) — **נקודת תורפה** as alternative |
| Christmas miracle | נס חג המולד | **נס** / **פלא** (neutralize) |

#### Luck / fate / superstition

| English | Adaptation |
|---------|------------|
| knock on wood | **בלי עין הרע** / **בעזרת השם** (religious-friendly) / context-dependent for secular |
| fingers crossed | **מקווה** / **בעזרת השם** / **בהצלחה** |
| lucky / unlucky | **בר מזל** / **חסר מזל** — fully acceptable in secular Hebrew |
| break a leg | **בהצלחה!** / **שיהיה בשעה טובה!** (NOT literal `שבור רגל`) |

#### Kashrut (kosher dietary law) — adapt non-kosher metaphors

| English | ✗ Non-kosher literal | ✓ Neutral adaptation |
|---------|---------------------|----------------------|
| bring home the bacon | להביא את הבייקון | **להביא את הלחם הביתה** / **להרוויח את הפרנסה** |
| champagne problems | בעיות שמפניה | **בעיות של עשירים** / **בעיות מותרות** |
| have your cake and eat it too | (cake itself is fine, but the idiom) | **לאכול את העוגה ולהשאיר אותה שלמה** (lit. translation works) |
| pork barrel (politics) | חבית חזיר | **אינטרסים פוליטיים צרים** / **תקציבי טובות הנאה** |

For mainstream product UI, avoid casual metaphors that imply consuming pork (חזיר), shellfish, or mixing meat+dairy. These read as awkward at minimum.

#### Calendar / holiday sensitivity

- Default: **Gregorian calendar** for product UI (dates in DD/MM/YYYY format).
- For observant audiences or Jewish-themed products: include **Hebrew calendar** dates (תשפ"ה for 5785, etc.).
- Hebrew months (תשרי, חשוון, כסלו, טבת, שבט, אדר, ניסן, אייר, סיוון, תמוז, אב, אלול) for religious context.
- Israeli-relevant holidays: ראש השנה (Rosh Hashanah), יום כיפור (Yom Kippur), פסח (Pesach/Passover), שבועות (Shavuot), סוכות (Sukkot), חנוכה (Hanukkah), פורים (Purim), יום העצמאות (Independence Day).
- **NEVER assume Christmas/Easter are universal** in Hebrew copy.

#### Shabbat (שבת) observance

- For observant audiences: respect that Shabbat (Friday sundown to Saturday sundown) is no-work time.
- Don't schedule notifications or marketing around Saturday as if it were a normal business day for orthodox audiences.
- Mention of Shabbat should be respectful: **`שבת`** (NOT `יום השבת` in religious contexts where it sounds patronizing).

#### Modesty (צניעות)

- For religious audiences, avoid imagery/wording that implies revealing dress, casual physical contact, or romantic content.
- Dating apps: use neutral phrasing — **`אפליקציית היכרויות`** (literally "acquaintance app") rather than language that emphasizes romance/sex.

#### Interest / financial concerns

- The Hebrew word `ריבית` (interest) is religiously loaded — Halakha has rules about interest between Jews.
- For Israeli mainstream finance: `ריבית` is fine.
- For observant-Jewish finance products: clarify (e.g., `היתר עיסקא` for halakhically-compliant interest structures).

**When in doubt, choose phrasing that respects Jewish values OR is religion-neutral for secular audiences. Never inject religious phrases (בעזרת השם, ברוך השם, אם ירצה השם) into a translation unless the source already invokes that semantic.**

### 10. Word integrity — prefixes attached (severity 2.0)

Hebrew prefixes are attached directly to the following word without space or hyphen:

- ה (the): `הקובץ` (the file), `המערכת` (the system)
- ו (and): `וגם` (and also), `והקובץ` (and the file)
- ב (in/at): `בקובץ` (in the file), `בכל` (in every)
- ל (to/for): `לקובץ` (to the file), `למשתמש` (to the user)
- מ (from): `מהקובץ` (from the file), `מהמערכת` (from the system)
- כ (as/like): `כקובץ` (as a file)
- ש (that/which): `שהקובץ` (that the file)

**Never insert a space** between prefix and word: `ה קובץ` ✗ → `הקובץ` ✓.

---

## Pronouns

### Personal pronouns (gendered in 2nd / 3rd person)

| English | Hebrew m. | Hebrew f. |
|---------|-----------|-----------|
| I | אני | אני (same) |
| you (sg.) | **אתה** | **את** |
| you (pl.) | **אתם** | **אתן** (or אתם for mixed group) |
| he | הוא | — |
| she | — | היא |
| we | אנחנו | אנחנו (same) |
| they | הם | הן (or הם for mixed) |

### Possessive (postposed, attached or with של)

| English | Hebrew (post-noun) | With של |
|---------|---------------------|---------|
| my X | הקובץ שלי | (same construction) |
| your X (m.) | הקובץ שלך | |
| your X (f.) | הקובץ שלך (spelling same; pronounced differently) | |
| his X | הקובץ שלו | |
| her X | הקובץ שלה | |
| our X | הקובץ שלנו | |
| your X (pl.) | הקובץ שלכם / שלכן | |
| their X | הקובץ שלהם / שלהן | |

Hebrew possession is almost always `noun + של + pronoun` in modern UI. Older / formal style uses attached suffixes (`קובצי` = "my file", `קובצך` = "your m. file") but these sound literary and are rare in product UI.

---

## UI Conventions

### Buttons — INFINITIVE or NOUN form (gender-neutral)

Hebrew imperatives are gendered (`לחץ` m., `לחצי` f., `לחצו` pl.). For UI buttons that all users see regardless of gender:

| English | ✓ Infinitive (preferred for buttons) | ✓ Noun form (also OK) | Plural imperative (for instructions) |
|---------|--------------------------------------|------------------------|---------------------------------------|
| Save | **לשמור** | **שמירה** | שמרו |
| Cancel | **לבטל** | **ביטול** | בטלו |
| Delete | **למחוק** | **מחיקה** | מחקו |
| Send | **לשלוח** | **שליחה** | שלחו |
| Edit | **לערוך** | **עריכה** | ערכו |
| Search | **לחפש** | **חיפוש** | חפשו |
| Confirm | **לאשר** | **אישור** | אשרו |
| Continue | **להמשיך** | **המשך** | המשיכו |
| Submit | **לשלוח** / **להגיש** | **שליחה** / **הגשה** | שלחו / הגישו |
| Sign in | **להתחבר** / **להיכנס** | **התחברות** / **כניסה** | התחברו / היכנסו |
| Sign out | **להתנתק** | **התנתקות** | התנתקו |
| Sign up | **להירשם** | **הרשמה** | הירשמו |
| Next | **הבא** | (same) | |
| Back | **חזרה** | | |
| Done | **סיום** / **בוצע** | | |
| OK | **אישור** / **OK** | | |
| Close | **לסגור** | **סגירה** | סגרו |
| Upload | **להעלות** | **העלאה** | העלו |
| Download | **להוריד** | **הורדה** | הורידו |
| Refresh | **לרענן** | **רענון** | רעננו |
| Settings | **הגדרות** | | |
| Apply | **להחיל** | **החלה** | החילו |
| Reset | **לאפס** | **איפוס** | אפסו |
| Select all | **לבחור הכל** | **בחירת הכל** | בחרו הכל |

**For action instructions / hints (not single button labels), use plural imperative:**

| English | ✓ Hebrew |
|---------|----------|
| Click here to continue | **לחצו כאן כדי להמשיך** |
| Enter your password | **הזינו את הסיסמה** |
| Choose at least one language | **בחרו לפחות שפה אחת** |
| Try again | **נסו שוב** |
| Please wait | **אנא המתינו** / **נא להמתין** |

### Status messages — present participle + …

Hebrew "present tense" verbs function as present participles. For loading/ongoing states:

| English | Hebrew |
|---------|--------|
| Loading… | **טוען…** / **טוענת…** depending on subject's gender; **`טעינה…`** is gender-safe |
| Saving… | **שומר…** / **שומרת…**; safer: **`שמירה…`** |
| Sending… | **שולח…** / **שולחת…**; safer: **`שליחה…`** |
| Uploading… | **מעלה…**; safer: **`העלאה…`** |
| Downloading… | **מוריד…**; safer: **`הורדה…`** |
| Connecting… | **מתחבר…**; safer: **`מתחבר…`** OR **`התחברות…`** |
| Processing… | **מעבד…**; safer: **`עיבוד…`** |
| Searching… | **מחפש…**; safer: **`חיפוש…`** |
| Please wait | **נא להמתין…** / **המתינו בבקשה…** |

**Best practice: use the noun form (gerund)** for status messages — it sidesteps the gender question entirely. `טעינה…` is unambiguous; `טוען…` defaults to masculine.

### Completion messages — past tense or short noun

| English | Hebrew |
|---------|--------|
| Saved | **נשמר** (m.) / **נשמרה** (f.) — depends on subject |
| Done | **בוצע** / **הושלם** |
| Translation complete | **התרגום הושלם** / **התרגום הסתיים** |
| File uploaded | **הקובץ הועלה** |
| Payment successful | **התשלום בוצע** / **תשלום בוצע בהצלחה** |
| Sent | **נשלח** / **ההודעה נשלחה** |

### Failed messages

| English | Hebrew |
|---------|--------|
| Save failed | **השמירה נכשלה** / **השמירה לא הצליחה** |
| Upload failed | **ההעלאה נכשלה** |
| Translation failed | **התרגום נכשל** |
| Connection failed | **החיבור נכשל** |
| File not found | **הקובץ לא נמצא** |

### Empty states — `אין X` / `לא נמצאו`

| ✗ Bare | ✓ Specific |
|--------|-----------|
| ריק | **אין תוצאות** / **לא נמצאו פריטים** |
| כלום כאן | **אין קבצים** / **אין נתונים זמינים** |
| ללא נתונים | **אין נתונים זמינים** |
| הרשימה ריקה | **אין פריטים ברשימה** |

### Drag-and-drop

- drag → **גרור** (m.sg) / **גררו** (pl., gender-neutral)
- drop (= place) → **שחרר** / **שחררו**
- release → **שחרר** / **שחררו**

Combined: **`גררו ושחררו קובץ לכאן`** (Drag and drop a file here) — using plural for gender neutrality.

### File picker — `בחר`/`בחרו` action verb

| ✓ Action-oriented (preferred) |
|-------------------------------|
| **בחרו קובץ** (Choose a file) |
| **לחצו לבחירת קובץ** (Click to choose a file) |
| **בחירת קובץ** (File selection — as label) |

Avoid `דפדף` (browse) for file picker — `בחר/בחירה` matches the user's actual goal.

### Quantity expressions

| ✗ Calque | ✓ Native Hebrew |
|----------|------------------|
| +25 שפות | **יותר מ-25 שפות** / **מעל 25 שפות** |
| +{count} עוד | **ועוד {count}** / **+{count}** (number formatting acceptable) |

### Error messages — what + next step

| ✗ Bare | ✓ With next step |
|--------|------------------|
| הקובץ לא נמצא. | **הקובץ לא נמצא. בדקו את הנתיב.** |
| שגיאת רשת. | **שגיאת רשת. נסו שוב.** |
| כתובת אימייל לא חוקית. | **כתובת האימייל לא חוקית. בדקו את הפורמט.** |
| ההתחברות נכשלה. | **ההתחברות נכשלה. בדקו את שם המשתמש והסיסמה.** |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Hebrew | Notes |
|------|--------|-------|
| Question mark | `?` (Latin) | Same as English — NOT mirrored (unlike Arabic ؟) |
| Comma | `,` | Same as English |
| Period | `.` | Same |
| Colon | `:` | Same |
| Quotation marks | `"…"` (modern UI, English-style) or **`„…"`** German style sometimes | English `"…"` is most common |
| Apostrophe-like | `'` (geresh) for foreign-name approximation | e.g., `ג'ון` (Jon), `צ'אט` (chat) — see below |

**Geresh (`׳`) and gershayim (`״`):**
- `'` (geresh, U+05F3) appears after letters to indicate foreign sounds: `ג'` (= /dʒ/) → `ג'ין` (gin), `ז'` (= /ʒ/), `צ'` (= /tʃ/) → `צ'אט` (chat), `ת'` (occasionally).
- `"` (gershayim, U+05F4) appears before the last letter of acronyms: `דוא"ל` (e-mail abbreviation = ד.ו.א.ל), `ארה"ב` (USA = ארצות הברית), `יום ו'` (Friday).

### Numbers

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **comma (,)** | 1,234,567 |
| Decimal separator | **period (.)** | 3.14 / 99.99 |
| Negative | `-25` (Latin minus before digits, LTR-protected) | |
| Percent | `25%` (no space typical) | |

Modern Hebrew uses **Western-style punctuation for numbers**: comma thousands, period decimal — **same as English**, opposite of Croatian/Serbian/German.

Hebrew **does** have its own letter-based numeral system (gematria: א=1, ב=2, ג=3…) but it's used only for traditional/religious dates and Bible verses, NOT for product UI.

### Dates

| Format | Example | Use |
|--------|---------|-----|
| DD/MM/YYYY | **15/01/2024** | Default Israeli format |
| DD.MM.YYYY | **15.01.2024** | Acceptable alternative |
| D mensa YYYY | **15 בינואר 2024** | Long-form Hebrew (note the `ב` prefix on month) |
| Hebrew calendar | **ה' בשבט תשפ"ד** | Religious contexts |

**Hebrew month names (Gregorian transliterations):**

| # | Hebrew |
|---|--------|
| 1 | ינואר |
| 2 | פברואר |
| 3 | מרץ |
| 4 | אפריל |
| 5 | מאי |
| 6 | יוני |
| 7 | יולי |
| 8 | אוגוסט |
| 9 | ספטמבר |
| 10 | אוקטובר |
| 11 | נובמבר |
| 12 | דצמבר |

**Hebrew calendar months** (used only for Jewish religious dates):

תשרי, חשוון, כסלו, טבת, שבט, אדר (and אדר ב' in leap years), ניסן, אייר, סיוון, תמוז, אב, אלול.

### Time

- 24-hour preferred: `14:30` or `בשעה 14:30` (at 14:30).
- 12-hour with AM/PM is uncommon in Israeli context.

### Weekdays — start Sunday in Israeli convention

| English | Hebrew |
|---------|--------|
| Sunday | יום ראשון (יום א') |
| Monday | יום שני (יום ב') |
| Tuesday | יום שלישי (יום ג') |
| Wednesday | יום רביעי (יום ד') |
| Thursday | יום חמישי (יום ה') |
| Friday | יום שישי (יום ו') |
| Saturday | שבת |

**Critical:** in Israel the **week starts on Sunday** (not Monday). The Israeli work week is Sunday-Thursday for most secular contexts; Friday-Saturday is the weekend (Shabbat).

### Currency — Israeli Shekel (NIS / ₪)

| Format | Pattern | Example |
|--------|---------|---------|
| Symbol | **₪** | **₪99.99** OR **99.99 ₪** |
| Abbreviation | **ש"ח** (= שקל חדש = "new shekel") | **99.99 ש"ח** |
| ISO code | NIS or ILS | 99.99 NIS |

For Israeli UI, currency symbol can appear before or after the number — both are common. `₪99.90` (before, US-style) and `99.90 ₪` (after) both used.

---

## Terminology — preferred Hebrew terms

| English | ✓ Hebrew preferred | Notes |
|---------|---------------------|-------|
| user | משתמש | |
| account | חשבון | |
| password | סיסמה | |
| settings | הגדרות | |
| dashboard | לוח בקרה | |
| email | אימייל (informal) / **דוא"ל** (formal) | `דוא"ל` = `דואר אלקטרוני` |
| link | קישור | |
| website | אתר / אתר אינטרנט | |
| folder | תיקייה | |
| file | קובץ | |
| device | מכשיר / התקן | |
| phone | טלפון / נייד (mobile) / סלולרי | |
| computer | מחשב | |
| application / app | אפליקציה (informal) / יישום / יישומון | |
| update (v.) | לעדכן / עדכון | |
| save | לשמור / שמירה | |
| delete | למחוק / מחיקה | |
| upload | להעלות / העלאה | |
| download | להוריד / הורדה | |
| sign in / log in | להתחבר / להיכנס / התחברות / כניסה | |
| sign up | להירשם / הרשמה | |
| search | לחפש / חיפוש | |
| click | ללחוץ / לחיצה | |
| share | לשתף / שיתוף | |
| profile | פרופיל | |
| notifications | התראות | |
| privacy | פרטיות | |
| terms | תנאים | |
| support | תמיכה | |
| help | עזרה | |
| feedback | משוב / חוות דעת | |
| menu | תפריט | |
| home | בית / דף הבית | |
| logout | התנתקות | |
| browser | דפדפן | |
| screen | מסך | |
| keyboard | מקלדת | |
| mouse | עכבר | |
| API | API (keep) | |
| build (software) | בנייה / יצירה | |
| deploy | פריסה / השקה | |
| pipeline | pipeline (keep) / צינור (acceptable) | |
| commit (git) | commit (keep) | |
| merge | מיזוג / merge | |
| repository | מאגר / repository | |
| branch (git) | branch (keep) / ענף | |
| token | אסימון / token | |
| cache | מטמון / cache | |
| log (n.) | יומן / log | |
| sync | סנכרון / לסנכרן | |
| webhook | webhook (keep) | |
| source of truth | מקור האמת / המקור המוסמך | |

### Tech identifiers — keep in Latin, stays LTR inside RTL text

These MUST stay in Latin/English inside Hebrew text:
- Programming languages: Python, JavaScript, Go, Rust, Java
- Frameworks: React, Vue, Angular, Next.js, Django
- Tools: Git, GitHub, Docker, npm, pip
- Protocols: HTTP, REST, GraphQL, OAuth, JWT
- File formats: JSON, XML, CSV, PDF
- Brands: Google, Microsoft, Apple, iPhone, Android
- Commands, file paths, URLs, code snippets, placeholders.

Example: `יש להתחבר אל GitHub כדי לסנכרן את הקבצים.` ("You need to connect to GitHub to sync the files.") — `GitHub` stays Latin, embedded LTR in the RTL sentence.

---

## False Friends — Critical

| Hebrew word | Actually means | NOT this | Correct for the English |
|-------------|----------------|----------|--------------------------|
| אקטואלי | current / topical (loanword) | "actual" | "actual" → **אמיתי** / **של ממש** |
| ריאלי | realistic | "real (genuine)" | "real (genuine)" → **אמיתי** |
| סולידי | conservative (financially) | "solid (in feel)" | "solid (object)" → **מוצק** |
| סנטימנטלי | sentimental in literary sense | (mostly OK) | — |
| אינדיבידואל | an individual (literary) | (OK in formal text) | — |
| גלובלי | global (scope) | (OK) | — |

Hebrew has relatively few false-friend traps compared to European languages, because Modern Hebrew was deliberately constructed with explicit terminology choices by the Academy of the Hebrew Language.

---

## Calque / Anti-Pattern List

| ✗ Calque | ✓ Native Hebrew | Reason |
|----------|------------------|--------|
| עושה הגיון | **הגיוני** / **מתאים** | "Makes sense" calque |
| באופן ברירת מחדל הערך | **ערך ברירת המחדל** | English structure with `באופן` is verbose |
| במקרה בו | **אם** | English "in the case where" calque; use simple `אם` |
| הקובץ לא יכול להימצא | **הקובץ לא נמצא** | "cannot be found" calque; use simple negation |
| על מנת ש- | **כדי ש-** | Verbose `על מנת` → simple `כדי` |
| על בסיס יומי / שבועי | **מדי יום** / **יומית** / **שבועית** | "On a daily/weekly basis" — use adverb |
| במונחים של | **מבחינת** / **לגבי** | "In terms of" calque |
| צלב לשאת | **נטל כבד** / **משא שיש לשאת** | Christian-origin idiom |
| הגביע הקדוש | **המטרה העליונה** | Christian-origin idiom |
| שומרוני טוב | **אדם טוב לב** / **בעל חסד** | Biblical reference, loaded |
| מעשה אלוהים | **כוח עליון** | Christian-flavored legal phrasing |
| ברכה במסווה | **ברכה בהסוואה** / **טוב שהוסתר** | Awkward calque |
| להביא את הבייקון | **להביא את הלחם הביתה** | Non-kosher food reference |
| חתיכת עוגה (= easy) | **קל כנוצה** / **פשוט מאוד** | Idiom; use Hebrew equivalent |
| שבור רגל (break a leg) | **בהצלחה!** / **שיהיה בשעה טובה!** | Idiom not literal |
| יורד גשם של חתולים וכלבים | **יורד גשם שוטף** / **גשם כמו מטר** | Idiom |
| ארצות הברית של אמריקה (in UI) | **ארה"ב** | UI short form |
| הממלכה המאוחדת של בריטניה הגדולה | **בריטניה** / **הממלכה המאוחדת** | UI short form |
| AI-מונע | **מבוסס בינה מלאכותית** / **מונע על ידי AI** | "AI-powered" calque |
| X-מודע | **מודע ל-X** / **המתחשב ב-X** | "X-aware" calque |
| ידידותי-משתמש | **ידידותי למשתמש** / **קל לשימוש** | "user-friendly" calque |
| אפס זמן השבתה | **ללא זמן השבתה** | "Zero X" English marketing calque |
| לחץ כאן + לחצי שם | **לחצו כאן + לחצו שם** | Mixed singular genders — use plural |

---

## Custom Sections

### Per vs total — semantic distinction

| Source | ✓ Hebrew | Meaning |
|--------|----------|---------|
| per language (rate) | **לכל שפה** | rate, per-unit |
| for 25 languages (total) | **עבור 25 שפות** | total scope |
| 5 USD per language | **5 USD לכל שפה** | rate |
| 5 USD for all languages | **5 USD עבור כל השפות** | total |

### Cost / estimate ordering

In RTL context, amount-first reads naturally:

| ✗ Awkward | ✓ Clear |
|-----------|---------|
| 5 שפות 25 קרדיט | **25 קרדיט עבור 5 שפות** |

### UI element references in prose

Use quotation marks for specific UI labels:

| ✗ Compound | ✓ Quoted label |
|------------|----------------|
| לחצו על שמירה-כפתור | **לחצו על הכפתור "שמירה"** |
| פתחו את הגדרות-לשונית | **פתחו את הלשונית "הגדרות"** |
| השתמשו בשם-שדה | **השתמשו בשדה "שם"** |

### Brand names + Hebrew gender

Foreign brands take **masculine gender by default** OR the gender of an implied noun:

- `OneSky` → masculine by default. But `פלטפורמת OneSky` (the OneSky platform) — feminine, because `פלטפורמה` is feminine.
- `Google` → masc.: `Google מציע...` ("Google offers..."). Or fem.-leaning if implied noun is `חברה` (company).
- `iPhone` → masc.: `ה-iPhone החדש`.

Brand names stay invariant (no Hebrew declension) but the surrounding text agrees with their assigned gender.

### Bidirectional rendering — when LRM/RLM helps

Most rendering engines handle bidi correctly in `dir="rtl"` containers. **Add LRM/RLM marks only when QA confirms a specific issue**:

- Hebrew sentence ending with a parenthetical that contains Latin — punctuation can stick wrong.
- Hebrew sentence with a placeholder `{var}` followed by Hebrew punctuation.
- Numbers immediately followed by Hebrew text causing visual jumps.

Marks:
- LRM (U+200E) — Left-to-Right Mark, forces LTR direction at insertion point.
- RLM (U+200F) — Right-to-Left Mark, forces RTL.

**Best practice in translation strings: trust the framework. Don't pre-litter strings with bidi marks.**

### Hebrew calendar dates (when needed)

Hebrew years use letters: ה (5) + תשפ"ה (785) = `ה'תשפ"ה` (5785). For products with religious-Jewish audiences:

- Convert Gregorian → Hebrew: `15 בינואר 2024` ↔ `ה' בשבט תשפ"ד`.
- Hebrew months listed above (תשרי through אלול).
- The current Hebrew year as of 2026-05-24 is 5786 / תשפ"ו.

For mainstream secular Israeli UI, **Gregorian-only is fine**. Hebrew calendar is opt-in for religious context.

---

## Self-Check Checklist (Run Before Returning Output)

### RTL & script (auto-fail on miss)

- [ ] **Hebrew script throughout** Hebrew text.
- [ ] **Latin tech identifiers preserved** (Git, API, JSON, URLs, `{var}`) — they stay LTR-embedded in RTL flow.
- [ ] **Punctuation at logical end** of sentence (not mirrored — Hebrew uses standard `? , ; . !`).
- [ ] **Latin digits 0-9** for numbers in product UI.

### Accuracy

- [ ] **Gender agreement** on every noun-adj-verb triple (פלטפורמה חדשה, שירות חדש, מערכת עובדת).
- [ ] **Adjective AFTER noun** (`קובץ חדש`, not `חדש קובץ`).
- [ ] **Definiteness agreement**: both noun and adj take `ה-` or neither (`הקובץ החדש` OR `קובץ חדש` — but not `הקובץ חדש` as a noun phrase).
- [ ] **Numbers 1-10 opposite gender** (`שלושה קבצים`, `שלוש פלטפורמות` — masculine noun = number with `-ה`, feminine noun = number without).
- [ ] **Plural forms**: masc. `-ים`, fem. `-ות`; adjectives agree (`קבצים חדשים`, `פלטפורמות חדשות`).
- [ ] **ICU plurals**: one / two / other (Hebrew dual recognized in CLDR).
- [ ] **Construct state (סמיכות)** used for compound nouns (`קבצי המערכת`, not `קבצים של המערכת`).
- [ ] **Prefix integrity**: `ה / ו / ב / ל / מ / כ / ש` attached without space.
- [ ] **Placeholders preserved**: `{var}`, `{{count}}`, `<tag>`, URLs.
- [ ] **Numbers**: comma thousands (1,234), period decimal (99.99). Same as English.
- [ ] **Dates**: DD/MM/YYYY default; `15 בינואר 2024` long form with `ב` prefix on month.
- [ ] **Week starts Sunday**.
- [ ] **Currency**: `₪` or `ש"ח` for Israeli shekel.

### Religious / cultural sensitivity (auto-fail on miss)

- [ ] **No literal Christian-origin idioms** (`צלב לשאת`, `הגביע הקדוש`, `שומרוני טוב`, `מעשה אלוהים`, `ברכה במסווה`).
- [ ] **Non-kosher food metaphors adapted** (no `להביא את הבייקון`, `בעיות שמפניה`).
- [ ] **Superstition softened** (`בלי עין הרע` / `בעזרת השם` / context-neutral for `knock on wood`, `fingers crossed`).
- [ ] **No religious filler injected** (`בעזרת השם`, `ברוך השם`) unless source already invokes it.
- [ ] **Calendar/holiday assumptions checked** — don't assume Christmas/Easter universal; use Hebrew calendar where religious context demands.
- [ ] **Shabbat respected** for observant-audience products.
- [ ] **Divine names not casually invoked** in non-sacred contexts (`השם` / `ה'` instead).

### Register

- [ ] **Gender-neutral imperatives** — plural (`לחצו`) OR infinitive (`ללחוץ`) — pick one approach and stay consistent.
- [ ] **No mixed singular m./f. imperatives** in same UI.
- [ ] **Vocabulary register matches source** (don't elevate casual English to literary Hebrew).

### UI conventions

- [ ] Buttons use **infinitive** (`לשמור`) or **noun** (`שמירה`) — gender-neutral.
- [ ] Status messages prefer **noun form** (`טעינה…`, `שמירה…`) over gendered participle, OR consistent m./f.
- [ ] Action instructions use **plural imperative** (`לחצו, הזינו, בחרו`).
- [ ] Completion: `נשמר` / `הושלם` / past-tense passive.
- [ ] Failed: `נכשל` / `לא הצליח`.
- [ ] Empty state: `אין X` / `לא נמצאו` with specific noun.
- [ ] File picker: `בחרו`, not `דפדפו`.
- [ ] Drag-drop: `גררו`, `שחררו`.
- [ ] Error messages include next step.

### Naturalness

- [ ] **No English calques** (no `עושה הגיון`, `במקרה בו`, `על מנת ש`, `במונחים של`, `על בסיס יומי`).
- [ ] **Construct state used** where idiomatic (`קבצי המערכת` over `קבצים של המערכת`).
- [ ] **`של`-chains avoided** when construct state works.
- [ ] **No marketing-zero calque** (`אפס X` → `ללא X` / `בלי X`).
- [ ] **No false friends** (`אקטואלי ≠ actual`).
- [ ] **Proper noun short forms** (`ארה"ב`, `בריטניה`).
- [ ] **Established Hebrew terms** preferred where they exist alongside loanwords (e.g., `דפדפן`, `מסך`, `תיקייה`, `קישור`).

---

## Worked Example — Standard he UI

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** neutral product UI → gender-neutral plural imperative, noun-form status.

**Translation:**

> ברוכים השבים! יש לכם 3 קבצים חדשים בחשבונכם. לחצו על **המשך** כדי לסקור אותם או על **ביטול** כדי להישאר כאן. שמירת השינויים…

**Why this works:**
- `ברוכים השבים` — gender-neutral plural greeting ("welcome back, [you all]").
- `יש לכם` — gender-neutral plural ("you have"). Singular forms would be `יש לך` (gender-ambiguous in writing but pronounced differently for m./f.).
- `3 קבצים חדשים` — `קובץ` is m., so `3` takes the feminine-looking form `שלושה` (opposite-gender rule); in numerals as digits this is implicit. Adjective `חדשים` (m. pl.) agrees with noun.
- `בחשבונכם` — `ב` (in) + `חשבון` + `כם` (your m. pl.) — prefix attached.
- Buttons noun-form: `המשך` (continuation) and `ביטול` (cancellation) — gender-neutral.
- `לחצו על ... כדי לסקור` — plural imperative + infinitive purpose clause.
- Status: `שמירת השינויים…` — construct state (`שמירה` → `שמירת`) + definite `השינויים`. Gender-safe noun form.
- Punctuation: standard `!`, `…`, period at logical end.

**Same string for a religious-Jewish audience product (e.g., kosher recipe app):**

(no special religious phrases needed for neutral UI string like this — the religious sensitivity rule kicks in mainly for IDIOMS and CULTURAL REFERENCES that mention religion. A neutral UI string remains the same.)

---

## Worked Example — Religious sensitivity adaptation

**Source (marketing copy):**

> Reaching net-zero emissions is the holy grail for sustainability — but it's a cross to bear for many companies. Don't worry, we'll be your good Samaritan.

**✗ Wrong (literal Christian idioms):**

> הגעה לאפס פליטות היא הגביע הקדוש של הקיימות — אך זהו צלב כבד שיש לשאת עבור חברות רבות. אל דאגה, אנחנו נהיה השומרוני הטוב שלכם.

**✓ Right (culturally adapted):**

> הגעה לאפס פליטות היא היעד הנכסף של הקיימות — אך מדובר בנטל כבד עבור חברות רבות. אל דאגה, אנחנו נסייע לכם בדרך.

(Adaptations: `הגביע הקדוש` → `היעד הנכסף`; `צלב כבד שיש לשאת` → `נטל כבד`; `השומרוני הטוב` → simple `נסייע לכם`.)

---

## Worked Example — Construct state

**Source:** Translation Service Settings

**✗ Awkward (של chain):**

> הגדרות של שירות של תרגום

**✓ Construct state:**

> הגדרות שירות התרגום

(Three nouns in construct: `הגדרות` (settings) — `שירות` (service of) — `התרגום` (the translation). Only the last carries the definite article; earlier nouns are bare construct-form.)

---

## Worked Example — Number-noun agreement (opposite gender)

| Source | ✓ Hebrew |
|--------|----------|
| 3 files | **3 קבצים** (m. noun → number `שלושה`) |
| 3 platforms | **3 פלטפורמות** (f. noun → number `שלוש`) |
| 5 users | **5 משתמשים** (m. → `חמישה`) |
| 5 systems | **5 מערכות** (f. → `חמש`) |
| 7 settings | **7 הגדרות** (f. → `שבע`) |
| 7 fields | **7 שדות** (m. → `שבעה`) |

When numbers appear as digits, the agreement is implicit; when spelled out, the form chosen MUST match the rule.

---

## Worked Example — ICU plural with Hebrew dual

```icu
You have {count, plural, one {# new message} other {# new messages}}.
```

**Hebrew expansion:**

```icu
יש לכם {count, plural,
  one {הודעה חדשה אחת}
  two {שתי הודעות חדשות}
  other {# הודעות חדשות}
}.
```

Notes:
- `one`: `הודעה חדשה אחת` — `הודעה` is f., adj. `חדשה` agrees, number `אחת` (f.).
- `two`: `שתי הודעות חדשות` — dual form `שתי` (f.), pl. noun + pl. adj.
- `other`: `# הודעות חדשות` — f. pl. noun + agreeing adj.

---

## When in Doubt

1. **Default to gender-neutral via plural imperative or infinitive.**
2. If unsure about gender agreement → **check noun ending** (-ה / -ת / -ית / -ות = feminine; consonant = masculine usually).
3. If you wrote `שלוש קבצים` or `שלושה פלטפורמות` → **flip the number** (opposite-gender rule).
4. If you wrote `קבצים של המערכת` → **use construct state**: `קבצי המערכת`.
5. If you translated a Christian-origin idiom literally (`צלב`, `שומרוני`, `גביע הקדוש`) → **stop and adapt to a neutral Hebrew equivalent**.
6. If you mention bacon / pork / champagne casually → **use a kosher-neutral metaphor**.
7. If you injected `בעזרת השם` / `ברוך השם` where the source didn't invoke religion → **remove it**.
8. If you mixed `לחץ` (m.) and `לחצי` (f.) in one UI → **switch all to `לחצו` (plural) or `ללחוץ` (infinitive)**.
9. If the noun is definite but the adjective lacks `ה-` (or vice versa) → **fix definiteness**.
10. If currency is USD/$ in Israeli context → **fix to ₪ or `ש"ח`**.
