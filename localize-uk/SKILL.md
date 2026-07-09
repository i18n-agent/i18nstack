---
name: localize-uk
description: Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Ukrainian (uk). Ukrainian is NOT Russian — enforces Ukrainian identity (letters і/ї/є/ґ, vocabulary наразі/також/власний/друкувати, NOT Russian сейчас/тоже/собственный/печатать), 7-case grammar with active vocative (Олександре!, користувачу!), 3-gender agreement, ICU one/few/many/other plurals (1/2-4/5-20+ with 11-14 exception), perfective/imperfective verb aspect, Ви/ти formality consistency (Ви capitalized), apostrophe usage (комп'ютер, об'єкт, п'ять), Latin tech identifiers (Git, API, JSON) inside Cyrillic, diiepryslivnyk (-чи) for simultaneous actions, false-friend awareness (збуджений has sexual connotation — use захоплений / в захваті for "excited"), and «ялинки» quotation marks.
---

# Translate to Ukrainian (uk) — High-Fidelity Skill

## Scope & Variants

Ukrainian is a single standard target — Modern Standard Ukrainian (літературна українська мова). No regional split for product UI:

| Locale | Notes |
|--------|-------|
| `uk` / `uk-UA` | Standard Ukrainian (Ukraine). Default and only target. |

**Critical context for this skill: Ukrainian is NOT Russian.** Many AI translators conflate them because they share Cyrillic script and Slavic structure, but they are distinct languages with distinct vocabulary, distinct letters, and (especially since 2022) strong political/cultural reasons NOT to mix them. Avoiding Russianisms is a top-tier quality concern.

### Ukrainian vs Russian — letter and vocabulary identity

**Ukrainian uses 4 letters Russian doesn't:**

| Ukrainian | Used for | Russian equivalent |
|-----------|----------|---------------------|
| **і** | /i/ sound (most common Ukrainian vowel) | и (different sound) |
| **ї** | /ji/ sound | doesn't exist |
| **є** | /je/ sound | е (different) |
| **ґ** | /g/ hard sound (used in foreign words) | г |

**Russian uses 4 letters Ukrainian doesn't:** `ы`, `э`, `ъ`, `ё`. Any of these appearing in Ukrainian text means a Russian word leaked in.

**Common Ukrainian vs Russian vocabulary** (the surface markers a translation must NOT mix):

| English | ✓ Ukrainian | ✗ Russian (do NOT use in uk) |
|---------|-------------|------------------------------|
| currently / now | наразі / зараз | сейчас |
| also | також | тоже |
| own (adj.) | власний | собственный |
| print (v.) | друкувати | печатать |
| ok / fine | гаразд / добре | хорошо / ладно |
| thank you | дякую | спасибо |
| please | будь ласка | пожалуйста |
| city | місто | город |
| only | лише / тільки | только |
| almost | майже | почти |
| together | разом | вместе |
| year | рік | год |
| month | місяць | месяц |
| Tuesday | вівторок | вторник |
| Monday | понеділок | понедельник |
| green | зелений | зелёный |
| who | хто | кто |
| what | що | что |
| where | де | где |
| when | коли | когда |
| if | якщо | если |
| because | тому що / адже | потому что |
| user | користувач | пользователь |
| computer | комп'ютер | компьютер (note: no apostrophe in Russian) |
| settings | налаштування | настройки |
| password | пароль | пароль (same) |
| account | обліковий запис / акаунт | учётная запись |
| file | файл | файл (same) |
| folder | папка / тека | папка (same) |
| email | електронна пошта / ел. пошта | электронная почта |
| download (v.) | завантажити | загрузить / скачать |
| save (v.) | зберегти | сохранить |
| delete (v.) | видалити | удалить |

**If a Ukrainian translation contains `сейчас`, `тоже`, `пожалуйста`, `сохранить`, `удалить`, `пользователь`, `настройки`, `только`, `почти`, `вместе` — IT'S WRONG.** Fix to the Ukrainian equivalents.

---

## Register Auto-Detection (Apply Before Translating)

Ukrainian has a strong T-V distinction (Ви/ти). Auto-detect from source:

| Source signal | Target register |
|---------------|-----------------|
| Casual / conversational / personal (`Hey!`, contractions, emoji, marketing voice, gaming, social) | **Informal (ти)** — `ти` lowercase, 2nd-person sg. verb endings (`-еш/-иш`: можеш, бачиш), familiar imperative (singular form: вибери, натисни, відкрий). |
| Neutral product UI / docs / consumer software (DEFAULT) | **Formal (Ви)** — `Ви` capitalized for direct address, 2nd-person pl. verb endings (`-ете/-іте`: можете, бачите), polite imperative (`-ть/-іть`: виберіть, натисніть, відкрийте). Possessive `Ваш/Ваша/Ваше` also capitalized. |
| Legal / banking / government / enterprise B2B | **Formal (Ви) elevated** — same `Ви` form but full constructions, no contractions, prefer reflexive impersonal (`Виконується`), use formal vocabulary (`обліковий запис` over `акаунт`; `електронна пошта` over `імейл`). |

**Hard rule: never mix levels in one text.** A string with `Ви можете` (formal verb) and `твої налаштування` (informal possessive) is broken.

**Capitalization rule for Ви:** `Ви / Ваш / Ваша / Ваше / Ваші / Вам / Вас` are capitalized in direct second-person address. Failing to capitalize is read as informal even if the verb forms are formal.

**Default for software UI: Ви (formal)** unless brand voice is explicitly youth/casual.

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. Ukrainian identity — NOT Russian (severity 2.5)

Documented above. **The single most important Ukrainian rule.** Check for Russian letters (`ы`, `э`, `ъ`, `ё`) and Russian vocabulary in your translation. Replace with Ukrainian equivalents.

### 2. Word integrity — verb prefixes NEVER split (severity 3.0)

Ukrainian verbs with prefixes are **single words**. Splitting them is a critical error.

| ✗ Wrong (split) | ✓ Correct (joined) |
|-----------------|---------------------|
| `по будувати` | **`побудувати`** (to build) |
| `пере класти` | **`перекласти`** (to translate) |
| `ви конати` | **`виконати`** (to execute) |
| `на діслати` | **`надіслати`** (to send) |
| `за вантажити` | **`завантажити`** (to load/upload) |
| `від крити` | **`відкрити`** (to open) |
| `при йняти` | **`прийняти`** (to accept) |
| `роз почати` | **`розпочати`** (to begin) |

**Reflexive `-ся / -сь` is ATTACHED** (different from West/South Slavic) — it's a suffix, NOT a separate word in Ukrainian.
- `завантажується` ✓ (loads) — not `завантажує ся` and not `завантажуєся` (missing letter).
- `реєструватися` ✓ / `реєструватись` ✓ (both forms acceptable in infinitive).

**Negation `не` rule:**
- `не` + verb → **separate word**: `не забуду`, `не знаю`, `не натискайте`.
- `не` + adjective/noun (forming a word) → **prefix attached**: `невидимий`, `неуспіх`, `неможливо`, `неправда`.

### 3. Apostrophe usage (severity 2.0)

Ukrainian uses an **apostrophe** (`'`) after labials (`б / п / в / м / ф`) and `р` before iotated vowels (`я / ю / є / ї`). This is mandatory — missing apostrophes are wrong.

| ✗ Wrong | ✓ Correct | English |
|---------|-----------|---------|
| компютер | **комп'ютер** | computer |
| обєкт | **об'єкт** | object |
| субєкт | **суб'єкт** | subject |
| пять | **п'ять** | five |
| память | **пам'ять** | memory |
| імя | **ім'я** | name |
| сімя | **сім'я** | family |
| Кєв | **К'єв** would be wrong; the actual word is **Київ** (Kyiv, no apostrophe needed because к isn't a labial) | Kyiv |
| розязати | **розв'язати** | to solve |

The Unicode apostrophe `'` (U+2019, RIGHT SINGLE QUOTATION MARK) is preferred over the ASCII `'` (U+0027) in published text, but ASCII `'` is acceptable in UI strings where typography is not curated.

### 4. Seven-case system (severity 2.5)

Ukrainian uses **all 7 Slavic cases**, including an **active vocative** (used much more than in Russian). Every noun, adjective, and pronoun declines.

| Case | Question | Use | Example (m. sg. "користувач" — user) | Example (f. sg. "система" — system) |
|------|----------|-----|--------------------------------------|---------------------------------------|
| Називний (NOM) | хто? що? | Subject | користувач | система |
| Родовий (GEN) | кого? чого? | Possession, "of", absence, 5+ count | користувача | системи |
| Давальний (DAT) | кому? чому? | Indirect object, "to" | користувачу / користувачеві | системі |
| Знахідний (ACC) | кого? що? | Direct object | користувача (animate=GEN) / файл (inanimate=NOM) | систему |
| Орудний (INS) | ким? чим? | "With", means | користувачем | системою |
| Місцевий (LOC) | на/у кому? чому? | Location (always w/ prep) | користувачі (на користувачеві) | системі (у системі) |
| Кличний (VOC) | — | **Direct address — ACTIVE in Ukrainian** | користувачу! | системо! |

**Critical: animate masculine accusative = genitive form.** `бачу користувача`, NOT `бачу користувач`.

**Vocative usage is REQUIRED** for direct address (unlike Russian where it's archaic). When a Ukrainian product UI greets the user by name or addresses a role, use vocative:

| ✗ Russian-style (nominative for address) | ✓ Ukrainian (vocative) |
|------------------------------------------|------------------------|
| Привіт, Олександр! | **Привіт, Олександре!** |
| Шановний користувач! | **Шановний користувачу!** |
| Дякуємо, Марія! | **Дякуємо, Маріє!** |

### 5. Preposition + governed case (severity 2.5)

| Preposition | Case | Example |
|-------------|------|---------|
| у / в (in/into) | LOC (location) / ACC (motion) | у системі / у систему |
| на (on/onto) | LOC / ACC | на сервері / на сервер |
| з / зі / із (with/from) | INS ("with") / GEN ("from") | з користувачем / з папки |
| без (without) | GEN | без помилок |
| для (for) | GEN | для користувача |
| від (from) | GEN | від користувача |
| до (until/to) | GEN | до кінця |
| про (about) | ACC | про користувача |
| по (per / along) | LOC / DAT (with rate) | на день |
| перед (before) | INS | перед збереженням |
| після (after) | GEN | після входу |
| за (per / behind) | INS / ACC | за день |

**"per" in Ukrainian:** use preposition + case, **NOT** the calque `пер`.
- per day → **на день** / **щодня**
- per file → **за файл** / **на файл**
- per user → **на користувача** / **за користувача**

### 6. Verb-governed case (severity 2.0)

Specific verbs require specific cases. Wrong case = critical error.

| Verb | Governs | Example |
|------|---------|---------|
| допомагати (help) | **dative** | допомагати **користувачу** (NOT користувача) |
| дякувати (thank) | dative | дякую **Вам** |
| керувати (manage/control) | **instrumental** | керувати **системою** (NOT систему) |
| користуватися (use) | instrumental | користуватися **сервісом** |
| володіти (own) | instrumental | володіти **знаннями** |
| досягти (achieve) | **genitive** | досягти **результату** (NOT результат) |
| уникнути (avoid) | genitive | уникнути **помилки** |
| потребувати (need) | genitive | потребувати **допомоги** |
| зустрічатися (meet) | INS with з- | зустрічатися **з користувачем** |

### 7. Relative pronoun agreement (який / яка / яке / які) (severity 2.5)

The relative pronoun MUST agree with its antecedent in gender and number:

| Antecedent | Pronoun |
|------------|---------|
| Masc. sg. (`додаток`) | **який** |
| Fem. sg. (`система`) | **яка** |
| Neut. sg. (`налаштування`) | **яке** |
| Pl. (`файли`) | **які** |

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| система, **який** працює | **система, яка працює** |
| додаток, **яка** запущений | **додаток, який запущений** |
| файли, **яке** завантажені | **файли, які завантажені** |

### 8. ICU plurals — one / few / many / other (1 / 2-4 / 5-20+ pattern) (severity 2.5)

```icu
{count, plural,
  one {# файл}
  few {# файли}
  many {# файлів}
  other {# файла}
}
```

**CLDR plural category boundaries:**

| Category | Rule | Examples | Noun form |
|----------|------|----------|-----------|
| `one` | n % 10 = 1, n % 100 ≠ 11 | 1, 21, 31, 41, 101, 121 | **NOM singular** (файл) |
| `few` | n % 10 ∈ {2,3,4}, n % 100 ∉ {12,13,14} | 2, 3, 4, 22, 23, 24, 102, 103 | **NOM plural** (файли) |
| `many` | n % 10 = 0 OR n % 10 ∈ {5-9} OR n % 100 ∈ {11-14} | 0, 5-20, 25-30, 100, 1000 | **GEN plural** (файлів) |
| `other` | fractions | 1.5, 2.5 | **GEN singular** (файла) |

**Critical:** 11/12/13/14 use `many` (exceptions to the otherwise simple "ends in 1/2-4" pattern). Same pattern as Russian.

### 9. Numeral-noun agreement (severity 2.0)

The plural-form rule manifests directly in numeral constructions:

| Count | Pattern | Example |
|-------|---------|---------|
| 1 | NOM sg | 1 файл, 1 користувач |
| 2, 3, 4 | NOM pl (NOT GEN sg like Croatian/Russian-Slavic-style!) | 2 файли, 3 користувачі |
| 5+ | GEN pl | 5 файлів, 10 користувачів |
| 11-14 | GEN pl (exception) | 11 файлів, 12 систем |
| 21 | NOM sg (back to "one") | 21 файл |
| 22-24 | NOM pl | 22 файли |
| 25+ | GEN pl | 25 файлів |

**Note vs other Slavic languages:** Ukrainian uses **nominative plural** for 2-4 (like Russian), NOT genitive singular (which is Croatian/Bosnian). Don't apply Croatian/Serbian patterns here.

### 10. Three-gender adjective agreement (severity 2.0)

| Gender | Indef. example | Adjective ending (sg.) |
|--------|---------------|------------------------|
| Masculine (consonant ending) | користувач, файл | новий користувач, новий файл |
| Feminine (-а/-я ending) | система, інформація | нова система, нова інформація |
| Neuter (-о/-е ending) | налаштування, вікно | нове налаштування, нове вікно |

Wrong gender adjective is auto-fail: `нова файл` ✗, `новий система` ✗, `нова налаштування` ✗.

### 11. Past-tense gender agreement (severity 1.5)

Past tense in Ukrainian is the AUX-less L-participle (the AUX `бути` is dropped in present-day Ukrainian past), which agrees with subject in gender + number:

| Subject | L-participle | Example |
|---------|--------------|---------|
| m. sg. | -в | він працював |
| f. sg. | -ла | вона працювала |
| n. sg. | -ло | воно працювало |
| pl. | -ли | вони працювали |

`вона працював` ✗ → `вона працювала` ✓.

### 12. Verb-construction integrity — no stacked finite verbs (severity 2.0)

English `-ing` (gerund as adverbial: "I spent 6 years building...") MUST be rendered with **dieprislivnyk** (дієприслівник, verbal adverb in `-чи / -ючи / -ачи`), NOT a second finite clause.

| ✗ Stacked finite | ✓ Verbal adverb (-чи) | English |
|------------------|------------------------|---------|
| `Провів 6 років будував бізнес` | **`Провів 6 років будуючи бізнес`** | I spent 6 years building the business |
| `Працював поки писав звіт` | **`Працював пишучи звіт`** | I worked while writing the report |
| `Вона провела час чекала результати` | **`Вона провела час чекаючи результати`** | She spent time waiting for results |

**Common -чи forms (imperfective verbs only):**

| Infinitive | -чи form | English |
|------------|----------|---------|
| чекати | чекаючи | waiting |
| писати | пишучи | writing |
| будувати | будуючи | building |
| читати | читаючи | reading |
| думати / розмірковувати | розмірковуючи | thinking |
| використовувати | використовуючи | using |
| приходити | приходячи | coming |
| працювати | працюючи | working |
| говорити | говорячи | speaking |
| перекладати | перекладаючи | translating |

### 13. Complex constructions — щоб and перед (severity 2.0)

- `щоб` (so that / in order to) requires **infinitive** or **past tense**, NOT present indicative:
  - ✗ `щоб ви зберігаєте` → ✓ **`щоб зберегти`** / **`щоб ви зберегли`**
- `перед` (before) requires **instrumental verbal noun**, OR use `перш ніж` + infinitive:
  - ✗ `перед зберігаєте` → ✓ **`перед збереженням`** / **`перш ніж зберегти`**

### 14. Ellipsis completion — explicit nouns after numbers (severity 1.5)

Ukrainian requires explicit nouns after numbers and quantifiers; bare "5 others" sounds incomplete.

| ✗ Bare | ✓ Explicit |
|--------|-----------|
| 4 інших | **ще 4 елементи** / **4 інші файли** |
| і 3 більше | **і ще 3 файли** / **і 3 додаткові** |

### 15. False-friend: збуджений has sexual connotation (severity 2.0)

The Ukrainian word `збуджений` literally means "excited" but in modern usage carries a strong sexual/arousal connotation. **NEVER** use it as the casual "I'm excited (looking forward)" translation.

| ✗ Wrong (awkward / sexual) | ✓ Correct |
|----------------------------|-----------|
| Я збуджений! | **Я в захваті!** / **З нетерпінням чекаю!** / **Я радий/рада!** |
| Збуджуючий продукт | **Захоплюючий продукт** / **Цікавий продукт** |
| Збуджена аудиторія | **Захоплена аудиторія** / **Зацікавлена аудиторія** |

### 16. Diacritics and special letters — preserve (severity 2.5)

Ukrainian uses **і, ї, є, ґ, ʼ (apostrophe)**. Never strip them. Stripping the apostrophe in `комп'ютер` to `компютер` is a critical readability failure.

---

## Pronouns and Possessives

### Personal pronouns

| English | Ukrainian | Notes |
|---------|-----------|-------|
| I | я | |
| you (sg. informal) | ти | |
| you (sg./pl. formal — capitalize) | Ви | Always capitalized in direct address |
| you (pl. informal) | ви | lowercase when truly plural informal |
| he | він | |
| she | вона | |
| it | воно | |
| we | ми | |
| they | вони | |

### Possessive pronouns (agree with possessed noun's gender/number/case)

| Person | m. sg. | f. sg. | n. sg. |
|--------|--------|--------|--------|
| мій (my) | мій | моя | моє |
| твій (your sg. informal) | твій | твоя | твоє |
| **Ваш (your formal — capitalize)** | **Ваш** | **Ваша** | **Ваше** |
| його (his — invariable) | його | його | його |
| її (her — invariable) | її | її | її |
| свій (reflexive — own) | свій | своя | своє |
| наш (our) | наш | наша | наше |
| їхній (their) | їхній | їхня | їхнє |

**Reflexive `свій`** is used when the possessor is the subject of the same clause:
- `Він зберігає свій файл.` (He saves his own file.) ← reflexive
- `Він зберігає його файл.` (He saves someone else's file.) ← different referent

---

## UI Conventions

### Buttons — INFINITIVE (the Ukrainian UI convention)

Unlike Croatian/Serbian/Russian where buttons take imperative, **Ukrainian platform UIs (Windows UA, Android UA, Chrome UA) use INFINITIVE for buttons**. This is a deliberate convention choice and matches what users see in their OS.

| English | ✓ Infinitive (button) | (Imperative — for instruction prose) |
|---------|------------------------|---------------------------------------|
| Save | **Зберегти** | Збережіть |
| Cancel | **Скасувати** | Скасуйте |
| Delete | **Видалити** | Видаліть |
| Send | **Надіслати** | Надішліть |
| Edit | **Редагувати** / **Змінити** | Редагуйте |
| Search | **Шукати** | Шукайте |
| Confirm | **Підтвердити** | Підтвердіть |
| Continue | **Продовжити** | Продовжіть |
| Submit | **Надіслати** / **Підтвердити** | — |
| Sign in / Log in | **Увійти** | Увійдіть |
| Sign out | **Вийти** | Вийдіть |
| Sign up | **Зареєструватися** | Зареєструйтесь |
| Next | **Далі** / **Наступне** | — |
| Back | **Назад** | — |
| Done | **Готово** / **Завершено** | — |
| OK | **OK** / **Гаразд** | — |
| Close | **Закрити** | Закрийте |
| Upload | **Завантажити** | — |
| Download | **Завантажити** | — |
| Refresh | **Оновити** | Оновіть |
| Settings | **Налаштування** | — |
| Apply | **Застосувати** | — |
| Reset | **Скинути** | — |
| Select all | **Вибрати все** | — |
| Deselect all | **Скасувати все** | — |
| Add more | **Додати ще** (NOT `Додати більше`) | — |

**Note: upload and download are both `завантажити`** in modern Ukrainian — context disambiguates (`завантажити на сервер` = upload, `завантажити з сервера` = download). For UI buttons, the bare `Завантажити` is standard.

**For action instructions / longer hints, use imperative** (formal `-ть/-іть` or informal `-ь/-и`):
- ✓ `Натисніть, щоб продовжити` (Click to continue)
- ✓ `Введіть свій пароль` (Enter your password)

### Status messages — three distinct patterns

**Ongoing (in-flight)** → **imperfective reflexive (-ється)** OR **Триває + verbal noun** (NEVER first-person)

| English | ✓ Ukrainian |
|---------|-------------|
| Loading… | **Завантажується…** / **Триває завантаження…** |
| Saving… | **Зберігається…** / **Триває збереження…** |
| Sending… | **Надсилається…** / **Триває надсилання…** |
| Processing… | **Обробляється…** / **Триває обробка…** |
| Connecting… | **Підключення…** / **Триває підключення…** |
| Searching… | **Триває пошук…** / **Шукається…** |
| Translating… | **Перекладається…** / **Триває переклад…** |
| Please wait | **Зачекайте, будь ласка** / **Зачекайте…** |

**Critical impersonal voice rule:** NEVER use first-person (`Обчислюю…`, `Аналізую…`, `Обробляю…`) — sounds awkward and unnatural in Ukrainian UI status. Always impersonal.

**Completed** → **Neuter perfective participle (`-но / -то`)** — impersonal completion form

| English | ✓ Ukrainian |
|---------|-------------|
| Saved | **Збережено** |
| Done | **Готово** / **Завершено** |
| Translation complete | **Переклад завершено** / **Перекладено** |
| File uploaded | **Файл завантажено** |
| Sent | **Надіслано** |
| Payment successful | **Платіж здійснено** / **Оплачено** |

**Critical**: Use the **`-но/-то` impersonal neuter participle**, NOT personal past tense:
- ✗ `Переклад завершився` → ✓ **`Переклад завершено`**
- ✗ `Файл збережений` → ✓ **`Файл збережено`**
- ✗ `Завантаження закінчилось` → ✓ **`Завантажено`** / **`Завантаження завершено`**

**Failed** → **`Не вдалося` + infinitive** OR **`Помилка` + GEN of verbal noun**

| English | ✓ Ukrainian |
|---------|-------------|
| Save failed | **Не вдалося зберегти** / **Помилка збереження** |
| Upload failed | **Не вдалося завантажити** / **Помилка завантаження** |
| Translation failed | **Не вдалося перекласти** / **Помилка перекладу** |
| Connection failed | **Не вдалося підключитися** / **Помилка підключення** |
| File not found | **Файл не знайдено** |

NEVER use:
- ✗ `Переклад провалився` (too informal/slangy)
- ✗ `Збереження неуспішне` (calque)
- ✗ `Завантаження провалилось` (slangy)

### Empty states — `Немає + GEN` / `Не знайдено`

| ✗ Verbose | ✓ Concise |
|-----------|-----------|
| Не було знайдено жодних результатів | **Немає результатів** |
| У вас поки немає жодних проєктів | **Поки немає проєктів** |
| Не знайдено файлів, що відповідають запиту | **Немає відповідних файлів** |
| Без даних | **Немає даних** |

### Drag-and-drop

- drag → **перетягніть** (Vi) / **перетягни** (ти)
- drop (= place files) → **сюди** (use the verb `перетягніть` + сюди)
- release → **відпустіть** (Vi) / **відпусти** (ти)
- Combined: **`Перетягніть файли сюди`** (Drag files here) / **`Відпустіть для завантаження`** (Release to upload).

`Звільніть` ✗ (means "liberate"/"set free" — wrong sense for DnD).
`Упустіть` / `Кинути` ✗ (means accidentally drop/throw — wrong for intentional file placement).

### File picker — `Вибрати` not `Переглянути`

Standard in Chrome UA / Windows UA / macOS UA:

| ✗ Older / navigation | ✓ Modern / action-oriented |
|----------------------|----------------------------|
| Переглянути файли | **Вибрати файли** |
| Переглянути файл | **Вибрати файл** |
| натисніть, щоб переглянути | **натисніть, щоб вибрати** |

### Quantity expressions

| ✗ Calque | ✓ Native Ukrainian |
|----------|---------------------|
| 25+ мов | **понад 25 мов** |
| +{count} ще | **та ще {count}** |
| +25 нових функцій | **понад 25 нових функцій** / **більше 25 нових функцій** |

`Додати більше` ✗ (literal "add more") → `Додати ще` ✓ (idiomatic).

### Error messages — what + next step

| ✗ Bare | ✓ With next step |
|--------|------------------|
| Файл не знайдено. | **Файл не знайдено. Перевірте шлях.** |
| Помилка мережі. | **Помилка мережі. Спробуйте ще раз.** |
| Невірна електронна пошта. | **Електронна адреса невірна. Перевірте формат.** |
| Не вдалося увійти. | **Не вдалося увійти. Перевірте ім'я користувача та пароль.** |

**No comma before `або`**: `Спробуйте ще раз або зверніться до підтримки.` ✓ (NOT `Спробуйте ще раз, або зверніться…`).

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Ukrainian | Notes |
|------|-----------|-------|
| Question mark | `?` | Same as English |
| Comma | `,` | Different conjunction rules |
| Period | `.` | Same |
| Colon | `:` | Same |
| Quotation marks | **«…»** (ялинки/guillemets) primary, `„…"` nested | Same as Russian primary; never use English `"…"` in editorial copy |
| Apostrophe | `'` (curly) preferred; `'` ASCII acceptable | Used inside words: комп'ютер |
| Em-dash | `—` | Used for copular sentences: `Київ — столиця України` |

### Comma rules

| Rule | Example |
|------|---------|
| **NO comma** before `і / й` (and) | Виберіть файл **і** натисніть. |
| **NO comma** before `або / чи` (or) | Виберіть файл **або** папку. |
| **NO comma** before `та` (and, formal) | швидко **та** ефективно. |
| **Comma** before `що` (that, subordinating) | Бачу, **що** файл відкритий. |
| **Comma** before `який / яка / яке / які` (relative) | Файл, **який** збережено… |
| **Comma** before `щоб` (in order to) | Натисніть, **щоб** продовжити. |
| **Comma** before `якщо` (if) | Збережіть, **якщо** бажаєте. |
| **Comma** before `коли` (when) | Зачекайте, **коли** завантажиться. |
| **Comma** before `але / а / проте` (but/contrast) | Швидко, **але** ефективно. |

### Numbers

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **space** | 1 234 567 |
| Decimal separator | **comma (,)** | 3,14 / 99,99 |
| Negative | `-25` | |
| Percent | `25%` | |

**Critical:** Ukrainian uses **space for thousands, comma for decimal**. Never `1,234.56`.

### Dates

| Format | Example | Use |
|--------|---------|-----|
| DD.MM.YYYY | **15.01.2024** | Default for UI / business |
| D MMMM YYYY р. | **15 січня 2024 р.** | Long-form prose (month in genitive, `р.` = `року` = "of the year") |
| D MMMM YYYY року | **15 січня 2024 року** | Formal documents |
| YYYY-MM-DD | 2024-01-15 | Technical/API only |

**Ukrainian month names (lowercase always, declines):**

| # | Nominative | Genitive (used in dates!) |
|---|------------|---------------------------|
| 1 | січень | січня |
| 2 | лютий | лютого |
| 3 | березень | березня |
| 4 | квітень | квітня |
| 5 | травень | травня |
| 6 | червень | червня |
| 7 | липень | липня |
| 8 | серпень | серпня |
| 9 | вересень | вересня |
| 10 | жовтень | жовтня |
| 11 | листопад | листопада |
| 12 | грудень | грудня |

**Critical: in dates, the month is in genitive** — `15 січня 2024 р.` not `15 січень 2024 р.`. Like Croatian, unlike Russian where the form is the same.

**Weekdays (lowercase):** понеділок, вівторок, середа, четвер, п'ятниця, субота, неділя.

Week starts **Monday**.

### Time

- 24-hour preferred: `14:30` or `о 14:30` (at 14:30).
- 12-hour rarely used.

### Currency — Ukrainian Hryvnia (UAH / ₴ / грн)

| Format | Pattern | Example |
|--------|---------|---------|
| Symbol | `₴` or `грн` after amount with space | **99,99 ₴** / **99,99 грн** |
| ISO code | UAH | **99,99 UAH** |

For USD/EUR context: `99,99 $` or `99,99 €` (after amount).

---

## Terminology — preferred Ukrainian terms

| English | ✓ Ukrainian preferred | ✗ Avoid (Russian / anglicism) |
|---------|------------------------|--------------------------------|
| user | **користувач** | юзер, пользователь |
| account | обліковий запис (formal) / акаунт (acceptable) | учётная запись |
| password | пароль | — |
| settings | **налаштування** | сетінги, настройки |
| dashboard | **панель керування** | дашборд |
| email | **електронна пошта** / **ел. пошта** (formal) / **імейл** (acceptable casual) | электронная почта |
| link | **посилання** | лінк |
| website | веб-сайт / сайт | — |
| folder | **папка** / **тека** | — |
| file | **файл** | — |
| device | пристрій | девайс |
| phone | телефон / мобільний | — |
| computer | **комп'ютер** (with apostrophe!) | компьютер |
| application / app | застосунок / додаток / аплікація | аплікейшн |
| update (v.) | оновити | апдейтити |
| save | **зберегти** | сейвити |
| delete | **видалити** | удалити |
| upload | **завантажити (на сервер)** | даунлоадити |
| download | **завантажити (з сервера)** | скачати |
| sign in / log in | **увійти** | залогінитись |
| sign up | **зареєструватися** | зарегаться |
| search | **шукати** / **пошук** | — |
| click | **натиснути** (preferred) / клікнути (acceptable) | — |
| share | **поділитися** | шерити |
| profile | профіль | — |
| notifications | **сповіщення** | нотифікації |
| privacy | конфіденційність / приватність | — |
| terms | умови | — |
| support | підтримка | — |
| help | допомога | — |
| feedback | відгук / зворотний зв'язок | — |
| menu | меню | — |
| home | головна / домашня | — |
| logout | вийти | — |
| **browser** | **браузер** / **переглядач** | — |
| **screen** | екран | — |
| **keyboard** | клавіатура | — |
| **mouse** | мишка / миша | — |
| **token** | токен | жетон |
| **endpoint** | ендпоінт / кінцева точка | — |
| **authentication** | автентифікація | — |
| **authorization** | авторизація | — |
| API | API (keep — Latin always) | — |
| build (software) | створити / зібрати | будувати (= construction) |
| deploy | розгорнути / опублікувати | — |
| pipeline (CI/CD) | pipeline (keep) | — |
| commit (git) | commit (keep) / зберегти зміни | — |
| merge (git) | об'єднати / merge | — |
| repository | репозиторій | — |
| sync | синхронізація / синхронізувати | — |

### Tech identifiers — keep in Latin script even inside Cyrillic text

Inside Ukrainian Cyrillic text, the following ALWAYS stay in Latin:

- Programming languages: Python, JavaScript, Go, Rust, Java
- Frameworks: React, Vue, Angular, Next.js, Django
- Tools: Git, GitHub, GitLab, Docker, npm, pip, cargo
- Protocols: HTTP, HTTPS, REST, GraphQL, OAuth, JWT
- File formats: JSON, XML, YAML, CSV, PDF
- Brands: Google, Microsoft, Apple, iPhone, Android
- Commands, file paths, URLs, code snippets
- Placeholders: `{variableName}`, `{{count}}`, `<tag>`

✓ Correct: `Git репозиторій синхронізовано.` (Cyrillic prose, Latin `Git`)
✓ Correct: `API ключ недійсний.` (Cyrillic prose, Latin `API`)
✓ Correct: `Дані у форматі JSON.` (Cyrillic prose, Latin `JSON`)
✗ Wrong: `Ґіт репозиторій` (transliterating `Git` to Cyrillic)
✗ Wrong: `АПІ ключ` (transliterating `API`)
✗ Wrong: `ДЖСОН формат` (transliterating `JSON`)

---

## False Friends — Critical

| Ukrainian word | Actually means | NOT this | Correct for the English |
|----------------|----------------|----------|--------------------------|
| **збуджений** | aroused (sexual) / excited (in tense context) | "excited (looking forward)" | "excited" → **в захваті** / **радий/рада** / **з нетерпінням чекаю** |
| актуальний | current / topical / relevant | "actual" | "actual" → **фактичний** / **справжній** |
| реалізувати | to implement / carry out | "to realize (understand)" | "realize (understand)" → **усвідомити** |
| контролювати | to check / monitor / verify | "to control (manage)" | "control (manage)" → **керувати** |
| еventуально / еventualnoэ | (this isn't even a word — but `можливо` is "possibly") | "eventually" | "eventually" → **зрештою** / **врешті-решт** / **з часом** |
| симпатичний | likeable / pleasant | "sympathetic (compassionate)" | "sympathetic" → **співчутливий** |
| рутина | routine (as a procedure, often pejorative) | (mostly OK in tech: "рутинні задачі") | — |
| фабрика | factory (industrial only) | "factory" in software (e.g., factory pattern) | "factory pattern" → keep as `фабрика (патерн)` for clarity |

---

## Calque / Anti-Pattern List

| ✗ Calque | ✓ Native Ukrainian | Reason |
|----------|---------------------|--------|
| робити сенс | **мати сенс** / **бути логічним** | "Makes sense" calque |
| в кінці дня | **зрештою** / **врешті-решт** | "At the end of the day" calque |
| взяти місце | **відбутися** / **мати місце** | "Take place" calque |
| базуючись на | **на основі** | "Based on" calque |
| в порядку, щоб | **щоб** / **аби** | "In order to" calque |
| Це є... | **Це...** | "This is..." — `є` is redundant |
| Файл не може бути знайдений | **Файл не знайдено** | Passive calque; use impersonal `-но` |
| В разі якщо | **Якщо** | "In case if" — verbose |
| По замовчуванню значення | **Значення за замовчуванням** | Wrong word order |
| **Авто-виявлено** | **Автоматично виявлено** | "Auto-X" — use full adverb |
| **Перекладені результати** (header) | **Результати перекладу** | English Past-Participle + Noun → Ukrainian Noun + Genitive of verbal noun |
| **Завантажені файли** (header) | **Файли для завантаження** | Same pattern |
| **опція мови** (N + N compound) | **мовні налаштування** / **вибір мови** | English N+N → Ukrainian adj+N or genitive |
| **проект папка** | **папка проекту** / **проектна папка** | English N+N → genitive or adjective |
| **користувач налаштування** | **налаштування користувача** / **персональні налаштування** | English N+N → adj or genitive |
| **преференція тону** | **бажаний тон** / **вибір тону** | Anglicism noun → native adj |
| **провести покращення** | **покращити** | "Make improvements" — use verb |
| **надати відповідь** | **відповісти** | "Provide an answer" — use verb |
| **здійснити вибір** | **вибрати** | "Make a selection" — use verb |
| на дневній базі | **щодня** / **дневно** | "On a daily basis" calque |
| **пер файл** | **за файл** / **на файл** | "per X" calque — use preposition+case |
| **Швидкий переклад. Безпечний. Надійний.** | **Швидкі, безпечні та надійні переклади** | English telegram-style fragments → complete Ukrainian noun phrase with agreement |
| **Простий налаштування** | **Просте налаштування** | Gender disagreement — `налаштування` is neuter |
| **Сполучені Штати Америки** (in UI) | **США** | UI short form |
| **Об'єднане Королівство** (full in UI) | **Великобританія** / **Велика Британія** / **UK** | UI short form |
| **Драгніть файли** | **Перетягніть файли** | English verb → native |
| **Звільніть для завантаження** | **Відпустіть для завантаження** | "release" = `відпустити`, not `звільнити` (= liberate) |
| **Упустіть файли сюди** | **Перетягніть файли сюди** | `упустити` = drop accidentally — wrong sense |
| **Переклад провалився** | **Не вдалося перекласти** / **Помилка перекладу** | Slangy → impersonal failure construction |
| **Файл збережений** | **Файл збережено** | Personal passive → impersonal -но form |
| **Переклад завершився** | **Переклад завершено** / **Перекладено** | Personal → impersonal |
| **Скасувати вибір усього** | **Скасувати все** / **Зняти вибір** | Button brevity |
| **Вибрати вибір усіх** | **Вибрати все** | Button brevity / redundancy |
| **Додати більше** | **Додати ще** | "Add more" — use idiomatic `ще` |
| **AI-керований** | **на основі ШІ** / **з використанням ШІ** | "X-powered" calque |
| **даними-орієнтований** | **на основі даних** / **орієнтований на дані** | "X-driven" calque |

---

## Custom Sections

### Per/for/rate — semantic distinction

| Source | ✓ Ukrainian | Meaning |
|--------|-------------|---------|
| per language (rate) | **за мову** / **на мову** | rate, per-unit |
| for 25 languages (total) | **для 25 мов** | total scope |
| 5 USD per language | **5 USD за мову** | rate |
| 5 USD for all languages | **5 USD для всіх мов** | total |
| per day | **на день** / **щодня** | per-day |
| per user | **на користувача** / **за користувача** | per-user |

### Cost / estimate ordering

Amount-first:

| ✗ Ambiguous | ✓ Clear |
|-------------|---------|
| 5 мов 25 кредитів | **25 кредитів для 5 мов** |

### Time / duration

| English | ✓ Ukrainian |
|---------|-------------|
| 30 seconds remaining | **30 с залишилося** |
| 5 minutes remaining | **5 хв залишилося** |
| 2 hours remaining | **2 год залишилося** |
| 3 days remaining | **3 дні залишилося** |

`залишилося` is the preferred form for "remaining". Always space between number and unit.

### UI element references in prose

Use quotation marks for specific UI labels:

| ✗ Compound | ✓ Quoted label |
|------------|----------------|
| Натисніть Зберегти-кнопку | **Натисніть кнопку «Зберегти»** |
| Відкрийте Налаштування-вкладку | **Відкрийте вкладку «Налаштування»** |
| Використовуйте Ім'я-поле | **Використовуйте поле «Ім'я»** |

### Brand names + Ukrainian declension

Foreign brand names CAN be declined with Latin + hyphen + Ukrainian ending (informal), OR stay invariant (formal/UI default):

- `Google` → `Google-а` (gen.), `Google-у` (dat./loc.), `Google-ом` (ins.) — informal/conversational
- For formal UI, prefer prepositional phrases: `на платформі Google`.
- `iPhone` → `iPhone-а`, `iPhone-у`
- `GitHub` → `GitHub-а`, `GitHub-у`

---

## Self-Check Checklist (Run Before Returning Output)

### Ukrainian identity (auto-fail on miss)

- [ ] **Ukrainian letters used**: і / ї / є / ґ where appropriate.
- [ ] **No Russian letters**: no `ы / э / ъ / ё`.
- [ ] **No Russian vocabulary**: no `сейчас / тоже / собственный / печатать / спасибо / пожалуйста / хорошо / сохранить / удалить / пользователь / настройки / только / почти / вместе / город / месяц / вторник / понедельник / что / где / когда / если / потому что`.
- [ ] **Apostrophes present** where required: `комп'ютер`, `об'єкт`, `п'ять`, `пам'ять`, `ім'я`, `сім'я`.

### Accuracy

- [ ] **Word integrity** — prefixes joined (`перекласти`, `виконати`, `надіслати`, `завантажити`). Reflexive `-ся / -сь` attached as suffix (`завантажується`).
- [ ] **`не` separation rule**: separate with verbs (`не натискайте`), attached as prefix with adjectives/nouns (`невидимий`, `неможливо`).
- [ ] **Gender agreement** on every noun-adj pair (новий файл / нова система / нове налаштування).
- [ ] **Seven cases** correct, especially:
  - Animate masc. accusative = genitive (`бачу користувача`).
  - Instrumental after `з / зі` (`з користувачем`, `з Вами`).
  - Locative after `у / на / о / по` (`у системі`, `на сервері`).
  - Genitive after `без / для / від / до / з (=from)` (`без помилок`).
  - **Vocative for direct address** (`Олександре!`, `користувачу!`).
- [ ] **Verb-governed case**: допомагати+dat, керувати+ins, досягти+gen.
- [ ] **Relative pronoun agreement** (який/яка/яке/які matches antecedent).
- [ ] **Complex constructions**: щоб + infinitive/past, перед + INS noun, перш ніж + infinitive.
- [ ] **ICU plurals**: `one / few / many / other` categories present (1 / 2-4 / 5-20+ / fractions). 11-14 use `many`.
- [ ] **Numeral-noun agreement** matches plural pattern (Ukrainian: 2-4 = NOM pl, NOT GEN sg like Croatian!).
- [ ] **Verb aspect** correct: perfective for completed (buttons via infinitive use perfective; completion uses -но/-то), imperfective for ongoing (status uses reflexive imperfective).
- [ ] **Past-tense gender agreement** on L-participle (працював / працювала / працювало).
- [ ] **No stacked finite verbs** from English -ing — use `-чи` diiepryslivnyk.
- [ ] **Ellipsis completion**: explicit noun after numbers (`ще 4 елементи`, not bare `4 інших`).
- [ ] **Placeholders preserved** (`{var}`, `{{count}}`, `<tag>`, URLs, code identifiers).
- [ ] **Latin tech identifiers**: Git, API, JSON, npm, etc. stay in Latin.
- [ ] **Numbers**: comma decimal (3,14), space thousands (1 234), `грн` or `₴` after amount.
- [ ] **Dates**: DD.MM.YYYY default; `15 січня 2024 р.` long form with month in **genitive**.
- [ ] **Time**: 24-hour, `14:30` or `о 14:30`.
- [ ] **per** with rate uses preposition + case (`за мову`, `на день`), NEVER `пер`.

### Register

- [ ] **Ви/ти chosen and applied consistently** — pronouns, possessives, verb endings, imperatives all match.
- [ ] **`Ви / Ваш / Ваша / Ваше` capitalized** in direct address.
- [ ] **No mixing** of formal verb ending with informal possessive within one text.

### UI conventions

- [ ] Buttons use **INFINITIVE** (`Зберегти`, `Видалити`, `Скасувати`), the Ukrainian platform convention.
- [ ] Status ongoing: **imperfective reflexive (-ється)** or `Триває` + verbal noun (NEVER first-person `Обчислюю`).
- [ ] Status completed: **neuter perfective participle `-но / -то`** (`Перекладено`, `Файл збережено`), NOT personal past (`Файл збережений`).
- [ ] Status failed: **`Не вдалося + infinitive`** OR **`Помилка + GEN`**, NEVER `провалився` (slangy) or `неуспішне` (calque).
- [ ] Empty state: `Немає + GEN` with specific noun.
- [ ] File picker: `Вибрати`, not `Переглянути`.
- [ ] Drag-drop: `Перетягніть` + `Відпустіть` (NOT `звільніть`, `упустіть`).
- [ ] Quantity: `понад 25`, `та ще {count}`, NOT `25+`, `+{count}`.
- [ ] Error messages include next step.

### Naturalness

- [ ] **No English calques** (`робити сенс`, `в кінці дня`, `базуючись на`, `в порядку, щоб`, `Це є`, `на дневній базі`).
- [ ] **Past-Participle + Noun headers** → **Noun + Genitive of verbal noun** (`Результати перекладу`).
- [ ] **Auto-X prefix** → full adverb (`Автоматично виявлено`).
- [ ] **English N + N compounds** → Ukrainian adj + N or genitive.
- [ ] **No verbose collocations** (`провести покращення` → `покращити`).
- [ ] **No false friends**: `збуджений ≠ excited`, `актуальний ≠ actual`, `реалізувати ≠ realize`, `контролювати ≠ control (manage)`.
- [ ] **Ukrainian months in genitive** in date prose (`15 січня 2024`).
- [ ] **«…»** Ukrainian quotation marks (NOT English `"…"`).
- [ ] No comma before `і / й / або / чи / та`.
- [ ] Comma before `що / який / щоб / якщо / коли / але / а / проте`.

---

## Worked Example — Standard uk formal UI

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** neutral product UI, exclamation → **Ви (formal)**, infinitive buttons.

**Translation:**

> Вітаємо знову! У Вас 3 нові файли на Вашому обліковому записі. Натисніть **Продовжити**, щоб переглянути їх, або **Скасувати**, щоб залишитися тут. Зберігається…

**Why this works:**
- `Вітаємо знову` — standard greeting, plural verb form (impersonal "we welcome").
- `У Вас` — formal Ви, capitalized.
- `3 нові файли` — `3` triggers `few` (NOM pl); `файл` is m.; `нові` is m. pl. agreeing.
- `на Вашому обліковому записі` — `на` + LOC; `записі` is m. LOC sg.; `Вашому` agreeing in LOC; `обліковому` agreeing.
- Buttons in infinitive: `Продовжити`, `Скасувати`.
- `щоб переглянути / щоб залишитися` — `щоб` + perfective infinitive (correct construction).
- Status: `Зберігається…` — imperfective reflexive (impersonal, not first-person `Зберігаю…`).
- Comma before `щоб` ✓; no comma before `або` ✓.
- No Russian vocabulary.

**Same string informal (ти):**

> Вітаємо знову! У тебе 3 нові файли на твоєму обліковому записі. Натисни **Продовжити**, щоб переглянути їх, або **Скасувати**, щоб залишитися тут. Зберігається…

(`У Вас` → `У тебе`, `Ваш` → `твій`, `Натисніть` → `Натисни`.)

---

## Worked Example — Vocative for direct address

**Source:** Hello, Alexander! Welcome back.

**✗ Wrong (Russian-style nominative):**

> Привіт, Олександр! Ласкаво просимо назад.

**✓ Correct (Ukrainian vocative):**

> Привіт, Олександре! Ласкаво просимо назад.

Other vocative examples:
- Mark → Марку (Марк → Марку)
- Maria → Маріє (Марія → Маріє)
- Olena → Олено (Олена → Олено)
- User (formal) → користувачу
- Friend (formal) → друже (друг → друже)

---

## Worked Example — ICU plural expansion

**Source:**

```icu
You have {count, plural, one {# new message} other {# new messages}}.
```

**Translation (full Ukrainian four-category expansion):**

```icu
У Вас {count, plural,
  one {# нове повідомлення}
  few {# нові повідомлення}
  many {# нових повідомлень}
  other {# нового повідомлення}
}.
```

Notes:
- `one`: `1 нове повідомлення` — n.sg. NOM (повідомлення is neuter, ends in `-я`).
- `few` (2-4): `2 нові повідомлення` — n. NOM pl.
- `many` (5+, 11-14, 0): `5 нових повідомлень` — n. GEN pl.
- `other` (fractions): `2.5 нового повідомлення` — n. GEN sg.

---

## Worked Example — Date with genitive month

**Source:** Last login: January 15, 2024 at 2:30 PM

**Translation:**

> Останній вхід: 15 січня 2024 р. о 14:30.

Note: `січня` (genitive of `січень`). Ukrainian dates use **month in genitive**, like Croatian (unlike Russian where month form is the same).

---

## Worked Example — Verb-construction integrity (-чи)

**Source:** I spent 6 years building this business while learning from mistakes.

**✗ Wrong (stacked finite verbs):**

> Я провів 6 років будував цей бізнес поки навчався на помилках.

**✓ Right (verbal adverb -чи for simultaneous actions):**

> Я провів 6 років, будуючи цей бізнес і навчаючись на помилках.

---

## Worked Example — Status messages (three patterns)

| State | English | ✓ Ukrainian |
|-------|---------|-------------|
| Ongoing | Saving… | **Зберігається…** / **Триває збереження…** (NOT `Зберігаю…` first-person) |
| Completed | Saved | **Збережено** (NOT `Файл збережений` personal) |
| Failed | Save failed | **Не вдалося зберегти** / **Помилка збереження** (NOT `Збереження провалилось` slangy) |

---

## When in Doubt

1. **Default to uk, Ви (formal), Ukrainian identity (NOT Russian).**
2. If you see Russian letters (`ы / э / ъ / ё`) → **fix to Ukrainian equivalents**.
3. If you see Russian vocabulary (`сейчас`, `тоже`, `пользователь`, `настройки`, `сохранить`, `удалить`) → **fix to Ukrainian** (`наразі`, `також`, `користувач`, `налаштування`, `зберегти`, `видалити`).
4. If `комп'ютер` is missing the apostrophe → **add it**.
5. If a verb prefix has a space (`пере класти`) → **join it**: `перекласти`.
6. If reflexive `-ся` is wrong: missing letter (`завантажуєся`) → fix to `завантажується`.
7. If you used `збуджений` for "excited" → **fix to `в захваті` / `радий` / `з нетерпінням чекаю`**.
8. If you wrote `Файл збережений` → **use impersonal `Файл збережено`**.
9. If you wrote `Переклад провалився` → **use `Не вдалося перекласти` / `Помилка перекладу`**.
10. If you used first-person status (`Обчислюю…`) → **switch to impersonal `Триває обчислення…` / `Обчислюється…`**.
11. If you stacked two finite verbs from English -ing → **rewrite with -чи**.
12. If you used `пер файл` → **fix to `за файл` / `на файл`**.
13. If you didn't use vocative when addressing someone by name → **fix** (Олександр → Олександре!).
14. If a date is `15 січень 2024` → **fix month to genitive**: `15 січня 2024 р.`.

Slava Ukraini.
