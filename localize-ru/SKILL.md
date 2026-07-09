---
name: localize-ru
description: Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Russian (ru). Enforces the 6-case system, 3-gender agreement, ICU plural one/few/many (1/2-4/5+ pattern), perfective vs imperfective verb aspect, ты/Вы formality consistency (Вы always capitalized), «ёлочки» quotation marks, infinitive button labels, impersonal status messages, and preservation of Latin-script technical identifiers (Git, API, JSON) inside Cyrillic text.
---

# Russian Translation Rules (ru / русский язык)

Distilled from the production translation prompt. Follow these rules verbatim — they are model-agnostic and produce consistent native-quality Russian output.

## Mindset

> Вы — крайне требовательный носитель русского языка, который ненавидит неестественные русские формулировки, такие как буквальные переводы с английского.

Reject literal English calques and word-stacking calques. Russian is highly inflected — getting case, gender, or aspect wrong produces output that reads as obviously machine-translated. Common English tech loanwords (файл, браузер, аккаунт, сервер) are accepted; Russified verb anglicisms (`апдейтить`, `чекать`) are NOT.

## Pre-Translation Setup

Lock in before translating:

1. **Formality (Вы vs ты)** — Default to **Вы** (formal, ALWAYS capitalized: Вы / Ваш / Ваша / Ваше / Ваши / Вам / Вас) for B2B, government, banking, and most software UI. Use **ты** only for explicitly consumer-casual contexts. NEVER mix within a file.
2. **Three genders** — masculine (он), feminine (она), neuter (оно). Adjectives + past-tense verbs MUST agree with noun gender.
3. **Six cases** — Nominative, Genitive, Dative, Accusative, Instrumental, Prepositional. Selection depends on verb/preposition.
4. **No articles, no present-tense copula** — `Это книга` not `Это есть книга`; definiteness comes from context, not "the/a".
5. **Word order** — SVO default, but flexible for emphasis (`Это сделал Иван` for emphasis on who).
6. **Placeholders** — Preserve `{variables}` and ICU plural syntax (`one / few / many / other`) exactly.

## Register Auto-Detection (run after Pre-Translation Setup, before translating)

If the user has NOT specified Вы or ты, infer from source text register. Match output to source — formal source → Вы; informal source → ты.

### Formal source signals → output Вы / Ваш / Ваша / Ваше / Ваши (all capitalized)
- Hedging / polite modals: "please", "kindly", "we recommend", "could you", "would you mind"
- Passive / impersonal: "users are advised", "it is recommended", "applicants must"
- No contractions: "do not", "cannot", "we will"
- Domain vocabulary: legal, financial, healthcare, regulatory, enterprise B2B, government, insurance, banking
- Third-person / distance: "the user must", "customers should"
- Long sentences, formal connectors (тем не менее, кроме того, более того)
- Brand voice: bank, insurance, government, B2B SaaS, healthcare, legal tech
- No exclamations or emojis

### Informal source signals → output ты / твой / твоя / твоё / твои (lowercase)
- Contractions: "don't", "you'll", "it's", "we're"
- Casual greetings: "hey", "hi there", "yo", "hi 👋", "привет!"
- Second-person directness, exclamations, emoji (🎉 😎 🚀 ✨)
- Slang: "cool", "awesome", "no worries", "kinda"
- Consumer-app voice: gaming, social, lifestyle, dating, fitness, kids, casual e-commerce
- Sentence fragments and conversational filler

### Mixed / ambiguous source → default to Вы
Вы reads slightly distant but professional; ты can read as disrespectful in B2B/government contexts. When in doubt, stay formal — Russian B2B and many consumer brands still use Вы by default.

### Explicit user override
If the user says "use ты" / "use Вы" / "formal" / "casual", their instruction wins.

### Worked examples

| Source | Detected | Russian output |
|----------------|----------|----------------|
| "Please review the terms of service before proceeding." | formal | Перед продолжением ознакомьтесь, пожалуйста, с условиями использования. |
| "Hey! Tap here to get started — it's super quick 🚀" | informal | Привет! Нажми сюда, чтобы начать — это очень быстро 🚀 |
| "Submit your application by the deadline." | formal | Отправьте Вашу заявку до указанного срока. |
| "Don't forget to save your work!" | informal | Не забудь сохранить свою работу! |

After detection: keep the chosen form consistent. NEVER mix Вы/ты across pronouns, possessives, OR imperatives.

## ⚠️ Critical Rules — Russian Has Four Distinctive Patterns

These are the biggest sources of unnatural output. They have no direct analogue in English, so the model gets them wrong by default.

### A. Numeral-noun agreement — the 1 / 2-4 / 5+ pattern (severity 2.0)

Russian noun forms after numbers depend on the LAST digit:

| Ends in | Use | Example |
|---------|-----|---------|
| 1 (but NOT 11) — 1, 21, 31, 101 | **nominative singular** | `1 файл`, `21 файл`, `101 файл` |
| 2-4 (but NOT 12-14) — 2, 3, 4, 22, 23, 24 | **genitive singular** | `2 файла`, `23 файла`, `104 файла` |
| 0, 5-20, 25-30, 11-19, 100-120 | **genitive plural** | `5 файлов`, `12 файлов`, `100 файлов` |
| Fractions / decimals | **genitive singular** | `1,5 файла`, `2,7 файла` |

| Wrong | Correct |
|-------|---------|
| `5 файла` | **`5 файлов`** (5 → gen.pl) |
| `2 файлов` | **`2 файла`** (2 → gen.sg) |
| `21 файла` | **`21 файл`** (21 → nom.sg, ends in 1) |
| `11 файл` | **`11 файлов`** (11 is the exception — gen.pl, NOT nom.sg) |
| `13 файла` | **`13 файлов`** (13 is the exception — gen.pl) |

### B. ICU plural categories: `one / few / many / other` (CRITICAL)

Russian ICU plurals use FOUR categories, not two:

```icu
{count, plural,
  one {# файл}          // 1, 21, 31, 101 (ends in 1, not 11)
  few {# файла}         // 2-4, 22-24, 102-104 (ends in 2-4, not 12-14)
  many {# файлов}       // 0, 5-20, 100, 1000
  other {# файла}}      // fractional / decimal (1.5 файла)
```

| Wrong | Correct |
|-------|---------|
| `{count, plural, one {# файл} other {# файлы}}` (English-style binary) | **Use `one / few / many / other`** |
| `few {# файлов}` | **`few {# файла}`** (gen.sg, not gen.pl) |
| `many {# файла}` | **`many {# файлов}`** (gen.pl) |

Common ICU patterns:

```icu
{n, plural, one {# минута} few {# минуты} many {# минут} other {# минуты}}
{n, plural, one {# секунда} few {# секунды} many {# секунд} other {# секунды}}
{n, plural, one {# день} few {# дня} many {# дней} other {# дня}}
{n, plural, one {# пользователь} few {# пользователя} many {# пользователей} other {# пользователя}}
{n, plural, one {# крéдит} few {# крéдита} many {# крéдитов} other {# крéдита}}
```

### C. Verb aspect — perfective vs imperfective (CRITICAL, severity 2.0)

Every Russian verb pair encodes whether the action is **completed (perfective)** or **ongoing/repeated (imperfective)**. Get this wrong and the meaning shifts.

| Aspect | Use for | UI examples |
|--------|---------|-------------|
| **Perfective** | Single completed action; result-focused; buttons | сохранить, удалить, нажать, отправить, открыть |
| **Imperfective** | Ongoing; in-progress; repeated; status spinners | сохраняется, загружается, обрабатывается, выполняется |

**Buttons → perfective infinitive**: `Сохранить, Удалить, Отправить, Загрузить`. NOT `Сохранять, Удалять`.

**Status messages → imperfective reflexive (-ется / -ятся)** or `Идёт` + verbal noun:

| Wrong | Correct | Why |
|-------|---------|-----|
| `Загрузился...` | **`Загружается...` / `Идёт загрузка...`** | imperfective for ongoing |
| `Файл сохранился...` (as spinner) | **`Файл сохраняется...`** | imperfective for ongoing |
| `Вычисляю...` (first-person) | **`Идёт вычисление... / Вычисляется...`** | impersonal, NEVER 1st person |

**Completion messages → perfective neuter past participle**:

| Wrong | Correct |
|-------|---------|
| `Перевод завершился` | **`Перевод завершён / Переведено`** |
| `Файл сохранился` (as confirmation) | **`Файл сохранён / Сохранено`** |
| `Загрузка закончилась` | **`Загружено / Загрузка завершена`** |

**Failure messages → `Не удалось` + infinitive OR `Ошибка` + genitive verbal noun**:

| Wrong | Correct |
|-------|---------|
| `Перевод провалился` | **`Не удалось перевести / Ошибка перевода`** |
| `Загрузка провалилась` | **`Не удалось загрузить / Ошибка загрузки`** |
| `Сохранение неуспешно` | **`Не удалось сохранить / Ошибка сохранения`** |

### D. Word integrity — never split verbal prefixes (severity 3.0 — highest)

Russian verb prefixes (по-, пере-, вы-, на-, до-, под-, у-, etc.) are part of the verb, NOT separate words.

| Wrong (split) | Correct (joined) |
|---------------|-------------------|
| `по строить` | **`построить`** |
| `пере вести` | **`перевести`** |
| `вы полнить` | **`выполнить`** |
| `до бавить` | **`добавить`** |
| `на жать` | **`нажать`** |
| `у далить` | **`удалить`** |

**Exception:** the negation particle `не` STAYS SEPARATE from verbs (`не забудет`, `не сохранил`). But `не` attaches to ADJECTIVES (`невидимый`, `неактивный`, `непрочитанный`).

## The 6 Cases — Full Reference (severity 2.5)

Every noun, pronoun, and adjective takes one of 6 case forms. Wrong case is the biggest error surface.

| # | Case | Question | When to use | Example with `пользователь` |
|---|------|----------|-------------|------------------------------|
| 1 | Nominative | кто? что? | Subject of sentence | **пользователь** |
| 2 | Genitive | кого? чего? | Possession, "of", absence, after 5+, after negation | **пользователя** |
| 3 | Dative | кому? чему? | Indirect object, "to" | **пользователю** |
| 4 | Accusative | кого? что? | Direct object | **пользователя** (animate) / **файл** (inanimate masc) |
| 5 | Instrumental | кем? чем? | Means, "with", "by", agency | **пользователем** |
| 6 | Prepositional | о ком? о чём? | Location, "about", after в/на/о | **о пользователе** |

### Common preposition + case pairings

| Preposition | Case | Example |
|-------------|------|---------|
| с / со (with) | instrumental | `с пользователем, со списком` |
| без (without) | genitive | `без файла, без подписки` |
| для (for) | genitive | `для пользователя, для проекта` |
| у (at/by) | genitive | `у меня есть файл` |
| из (from) | genitive | `из папки, из архива` |
| от (from) | genitive | `от пользователя` |
| в (in/into) | accusative (motion) / prepositional (location) | `в папку (into)` / `в папке (in)` |
| на (on/onto) | accusative (motion) / prepositional (location) | `на сервер (onto)` / `на сервере (on)` |
| о / об (about) | prepositional | `о файле, об ошибке` |
| к (towards/to) | dative | `к пользователю` |
| по (along/by/per) | dative | `по умолчанию, по адресу` |
| за (behind/for/per) | instrumental (location/agent) / accusative (motion/exchange) | `за пользователем (after)` / `за неделю (in a week)` / `за файл (per file)` |
| перед (before/in front of) | instrumental | `перед пользователем, перед запуском` |
| через (through/in [time]) | accusative | `через {n} секунд` |
| между (between) | instrumental | `между пользователями` |

### Common case errors

| Wrong | Correct | Why |
|-------|---------|-----|
| `с новый пользователь` | **`с новым пользователем`** | instrumental after `с` |
| `для пользователь` | **`для пользователя`** | genitive after `для` |
| `в система` | **`в системе`** | prepositional after `в` (location) |
| `о файл` | **`о файле`** | prepositional after `о` |
| `из папка` | **`из папки`** | genitive after `из` |
| `через 5 секунд` | (correct) | accusative + gen.pl for time |

### Verb-governed case (CRITICAL — memorize)

Some Russian verbs require a specific case for their object, NOT the typical accusative.

| Verb | Governs | Wrong | Correct |
|------|---------|-------|---------|
| **помогать** (help) | dative | `помогать пользователя` | **`помогать пользователю`** |
| **звонить** (call) | dative | `звонить пользователя` | **`звонить пользователю`** |
| **управлять** (manage) | instrumental | `управлять система` | **`управлять системой`** |
| **пользоваться** (use) | instrumental | `пользоваться программой` | (correct) |
| **владеть** (own/master) | instrumental | `владеть язык` | **`владеть языком`** |
| **достичь** (achieve) | genitive | `достичь результат` | **`достичь результата`** |
| **избежать** (avoid) | genitive | `избежать ошибка` | **`избежать ошибки`** |
| **бояться** (fear) | genitive | `бояться ошибка` | **`бояться ошибок / бояться ошибки`** |
| **ждать** (wait for) | genitive (or accusative for definite/animate) | `ждать ответ` | **`ждать ответа`** |

## Past-tense gender agreement (severity 2.0)

Past-tense verbs MUST agree with subject gender. Endings: `-л` (masc), `-ла` (fem), `-ло` (neut), `-ли` (plural).

| Wrong | Correct | Why |
|-------|---------|-----|
| `Система работал` | **`Система работала`** | feminine subject |
| `Приложение запустился` | **`Приложение запустилось`** | neuter subject |
| `Файлы загрузился` | **`Файлы загрузились`** | plural subject |
| `Пользователь сохранила` | **`Пользователь сохранил`** (if male) / **`Пользователь сохранила`** (if female) — context-dependent |

For UI strings where gender is unknown, use **passive/impersonal**: `Файл сохранён` (neuter participle) NOT `Я сохранил` / `Я сохранила`.

## Adjective gender + case agreement (severity 2.0)

Adjectives agree with their noun in gender, number, AND case. Endings vary heavily.

| Gender (nominative) | Ending | Example |
|---------------------|--------|---------|
| Masculine | -ый / -ий / -ой | новый файл, последний раз, большой проект |
| Feminine | -ая / -яя | новая система, последняя версия |
| Neuter | -ое / -ее | новое приложение, последнее обновление |
| Plural (all genders) | -ые / -ие | новые файлы, последние данные |

| Wrong | Correct |
|-------|---------|
| `новый система` | **`новая система`** |
| `новый приложение` | **`новое приложение`** |
| `Простой настройка` | **`Простая настройка`** |
| `новые файла` (case error) | **`нового файла` (gen.sg)** or **`новые файлы` (nom.pl)** depending on context |

## Gender of common IT nouns (memorize)

| Masculine (он) | Feminine (она) | Neuter (оно) |
|----------------|-----------------|----------------|
| **файл** | **система** | **приложение** |
| **сайт** | **папка** | **сообщение** |
| **сервер** | **страница** | **окно** |
| **браузер** | **ссылка** | **обновление** |
| **компьютер** | **кнопка** | **поле** |
| **пользователь** | **версия** | **устройство** |
| **документ** | **программа** | **имя** |
| **проект** | **настройка** | **время** |
| **аккаунт** | **ошибка** | **значение** |
| **сервис** | **подписка** | **уведомление** |
| **отчёт** | **загрузка** | **разрешение** |
| **поиск** | **операция** | **завершение** |
| **выбор** | **корзина** | **сохранение** |
| **запрос** | **функция** | **состояние** |
| **результат** | **сеть** | **число** |
| **OneSky / Slack / Teams** (foreign tech, default masc) | **компания / платформа** (when brand = company) | |

### Acronym gender

| Acronym | Expansion | Gender |
|---------|-----------|--------|
| **ИИ** | Искусственный интеллект | masculine |
| **API** | (foreign abbreviation) | masculine (treated as foreign masc noun) |
| **URL** | (foreign abbreviation) | masculine |
| **PDF** | (Portable Document Format) | masculine |
| **CPU** | (Central Processing Unit) | masculine (центральный процессор) |
| **СМИ** | Средства массовой информации | neuter plural |
| **ООН** | Организация Объединённых Наций | feminine |

## UI Conventions

### Buttons — infinitive (perfective)

| Wrong | Correct |
|-------|---------|
| `Сохраните / Сохрани` (imperative) | **`Сохранить`** |
| `Удалите / Удали` | **`Удалить`** |
| `Отмените / Отмени` | **`Отменить`** |
| `Создайте / Создай` | **`Создать`** |
| `Закройте / Закрой` | **`Закрыть`** |
| `Войдите / Войди` | **`Войти`** |

Infinitive works for both ты and Вы contexts. Avoid the imperative on buttons.

### Status messages — impersonal voice

NEVER first-person (`Вычисляю...`). Use **imperfective reflexive** or **`Идёт` + verbal noun**.

| Wrong | Correct |
|-------|---------|
| `Загрузка...` (noun-only, OK but flat) | **`Загружается... / Идёт загрузка...`** |
| `Вычисляю` | **`Идёт вычисление... / Вычисляется...`** |
| `Анализирую` | **`Идёт анализ... / Анализируется...`** |
| `Сохраняю изменения...` | **`Изменения сохраняются... / Идёт сохранение...`** |

### Completion messages — short-form neuter perfective participle

| Wrong | Correct |
|-------|---------|
| `Готово! Ваш перевод теперь готов.` (verbose) | **`Перевод завершён`** or just **`Готово`** |
| `Отлично! Всё было сохранено.` (calque) | **`Всё сохранено`** |
| `Ваши файлы были успешно загружены!` (calque + redundant "успешно") | **`Файлы загружены`** |

Drop redundant `успешно` (success is implied by completion). Drop exclamation marks unless the source clearly warrants them.

### Failure messages

| Wrong | Correct |
|-------|---------|
| `Перевод провалился` | **`Не удалось перевести / Ошибка перевода`** |
| `Сохранение неуспешно` | **`Не удалось сохранить / Ошибка сохранения`** |
| `Загрузка фейлд` | **`Не удалось загрузить`** |

Patterns: `Не удалось` + perfective infinitive, OR `Ошибка` + genitive verbal noun.

### Empty state messages

| Wrong | Correct |
|-------|---------|
| `Не было найдено никаких результатов` | **`Нет результатов`** |
| `У вас пока нет никаких проектов` | **`Пока нет проектов`** |
| `Не найдено файлов, соответствующих вашему запросу` | **`Нет подходящих файлов`** |
| `Список пустой` | **`Список пуст`** (short-form adjective is more idiomatic) |
| `Сообщений нет` | **`Сообщений нет / Нет сообщений`** (genitive of absence) |

### Drag and drop

| English | Russian |
|---------|---------|
| drag | **перетащить** / **перетащите** (imperative for help text) |
| drop | **отпустить** |
| drag and drop | **перетащите сюда** (unified phrase) |
| release (let go) | **отпустите** |
| browse (file picker) | **выбрать файл** — NOT `просмотреть файлы` |

| Wrong | Correct |
|-------|---------|
| `Драгните файлы` | **`Перетащите файлы сюда`** |
| `Бросьте файлы сюда` | **`Перетащите файлы сюда`** (бросьте = throwing, not drag-drop) |
| `Уроните файлы` | **`Отпустите файлы`** (уроните = drop accidentally) |
| `Просмотреть файлы` (file picker) | **`Выбрать файлы`** |

### UI label completeness — complete noun phrases

| Wrong (bare adjective) | Correct |
|------------------------|---------|
| `Альтернативное` | **`Альтернативное обнаружение`** |
| `Автоматическое` | **`Автоматический режим`** |
| `Расширенные` | **`Расширенные настройки`** |

### Validation messages — distinct verb moods

| Type | Mood | Example |
|------|------|---------|
| Field validation | indicative | `Это поле обязательно для заполнения` / `Неверный формат` |
| Action instruction | imperative | `Введите корректное значение` / `Выберите хотя бы один язык` |
| State description | impersonal | `Не удалось подключиться` / `Произошла ошибка` |

Drop calques: `Поле отсутствует` (calque of "field missing") → `Это поле обязательно`.

### Other UI patterns

| Wrong | Correct |
|-------|---------|
| `25+ языков` | **`более 25 языков`** / `25 и более языков` |
| `+{count} ещё` | **`и ещё {count}`** |
| `пер файл` (per file) | **`за файл`** |
| `Добавить больше` | **`Добавить ещё`** (incremental "more") |
| `Показать больше` | **`Показать ещё`** |
| `Загрузить больше` | **`Загрузить ещё`** |
| `Отменить выбор всего` | **`Снять все / Отменить выбор`** |
| `Выбрать выбор всех` | **`Выбрать все`** |
| `Преференция языка` | **`Предпочтительный язык / Выбор языка`** |

## Punctuation and Typography

| Item | Russian |
|------|---------|
| Decimal separator | **`,`** (comma) |
| Thousands separator | **` `** (space, ideally NBSP) |
| Example number | `1 234,56` |
| Currency | `99,99 ₽` or `1 234,56 ₽` (number + space + symbol) |
| Date | **`15.01.2024`** (DD.MM.YYYY, period separators) or `15 января 2024 г.` |
| Time | **`14:30`** (24-hour, no AM/PM) |
| Primary quotation marks | **`«ёлочки»`** (chevrons/guillemets, NO inside spaces) |
| Nested quotation marks | **`„лапки"`** (German-style low-9 + high-6) |
| Em-dash | **`—`** with spaces — used heavily in Russian for ranges, attribution, copular sentences |
| Ellipsis | **`…`** (single character preferred) |

| Wrong | Correct |
|-------|---------|
| `"кнопка"` (English quotes) | **`«кнопка»`** |
| `1,234.56 ₽` (US format) | **`1 234,56 ₽`** |
| `01/15/2024` | **`15.01.2024`** |
| `2:30 PM` | **`14:30`** |

### Em-dash in copular and attribution sentences

Russian uses `—` (with spaces) where English uses "is":

| Russian | English |
|---------|---------|
| Москва — столица России. | Moscow is the capital of Russia. |
| Это — наш приоритет. | This is our priority. |
| OneSky — платформа для перевода. | OneSky is a translation platform. |

## Comma Rules — Russian is comma-heavy

| Before | Comma? |
|--------|--------|
| и / или / либо (coordinating) | **NO comma** |
| но / а / однако (contrasting) | **Comma required** |
| что / который / если / когда / потому что / так как (subordinating) | **Comma required always** |
| чтобы / так чтобы | **Comma required** |
| Parenthetical phrases (даже, кроме того, например) | **Surround with commas** |

| Wrong | Correct |
|-------|---------|
| `файл, или папку` | **`файл или папку`** |
| `Проверьте что файл существует` | **`Проверьте, что файл существует`** |
| `Попробуйте ещё раз или свяжитесь с поддержкой` | (correct — no comma before или) |
| `когда вы готовы нажмите кнопку` | **`когда Вы готовы, нажмите кнопку`** |
| `файл который вы загрузили` | **`файл, который Вы загрузили`** |

## No articles, no copula in present tense

Russian has NO equivalent to English "the/a" — context determines definiteness. Do NOT insert any.

Russian has NO `есть` ("is") in simple present-tense copular sentences. The English "is" disappears.

| Wrong (English calque) | Correct (Russian) |
|------------------------|---------------------|
| `Это есть книга.` | **`Это книга.`** |
| `Файл есть открытый.` | **`Файл открыт.`** (short-form participle) |
| `Система есть готовая.` | **`Система готова.`** |

Exception: `есть` is used for **possession** (`У меня есть файл` = "I have a file") and for emphasizing existence.

## Anglicism Avoidance

| Anglicism (avoid in formal/UI) | Native Russian |
|---------------------------------|------------------|
| юзер | **пользователь** |
| линк | **ссылка** |
| апдейт | **обновление** |
| фидбэк | **отзыв** / **обратная связь** |
| дашборд | **панель управления** |
| таргет | **цель** |
| репорт | **отчёт** |
| чекать | **проверять** |
| дилитнуть | **удалить** |
| мерджить | **объединять** / **слить** |
| коммитить | **зафиксировать** (formal) / **сделать коммит** (acceptable in dev contexts) |

But these English loanwords ARE accepted as established Russian tech terms:
- **браузер** (browser)
- **файл** (file)
- **аккаунт** (account) — though `учётная запись` is the formal Russian equivalent
- **сервер** (server)
- **сайт** (website)
- **чат** (chat)
- **бэкап** (backup, acceptable; alt: `резервная копия`)
- **интерфейс** (interface)

## False Friends

| Russian word | Actually means | NOT the English |
|--------------|----------------|-----------------|
| **актуальный** | current / relevant / topical | NOT "actual" — use **фактический** for "actual" |
| **реализовать** | to implement / accomplish | NOT "realize (understand)" — use **осознать** |
| **симпатия** | liking / fondness | NOT "sympathy (condolence)" — use **сочувствие** |
| **фабрика** | factory (manufacturing) | NOT "fabric (cloth)" — use **ткань** |
| **магазин** | store / shop | NOT "magazine" — use **журнал** |
| **резюме** | CV / résumé | NOT verb "resume (continue)" — use **продолжить** / **возобновить** |
| **аккуратный** | neat / careful | NOT "accurate" — use **точный** |
| **симулировать** | to fake / simulate (medical) | careful; for software simulation use **моделировать / имитировать** |
| **репетиция** | rehearsal | NOT "repetition" — use **повторение** |
| **прогрессивный** | progressive (political) | for "progressive" (gradual) use **постепенный** |

## Technical Identifiers — Keep Latin Script (CRITICAL)

Technical identifiers, code, API names, brand names MUST stay in Latin script even when surrounded by Cyrillic text. NEVER transliterate.

| Wrong (transliterated) | Correct |
|------------------------|---------|
| `Гит репозиторий` | **`Git репозиторий`** |
| `АПИ ключ` | **`API ключ`** |
| `ДЖСОН формат` | **`JSON формат`** |
| `УРЛ адрес` | **`URL адрес`** |
| `нпм пакет` | **`npm пакет`** |
| `НодДжс` | **`Node.js`** |
| `Реакт компонент` | **`React компонент`** |

**Keep Latin always:** Git, GitHub, npm, Node.js, React, Vue, Angular, Next.js, API, URL, HTTP, HTTPS, JSON, XML, CSS, HTML, SQL, OAuth, JWT, REST, GraphQL, WebSocket, IDE, CLI, GUI, MVP, SaaS, PaaS, IaaS, SDK, SLA, KPI, CRM, ERP.

## Software Terminology — Domain Accuracy

| English (software context) | Wrong (literal) | Correct |
|----------------------------|------------------|---------|
| build (software) | **строить** (= construct buildings) | **собрать / создать / разработать** |
| deploy | **развернуть** (also means "unfold") — OK in tech / **выложить** | **развернуть / развернуть в продакшен / выложить** |
| release (product) | **выпустить** / **релиз** | **выпустить / опубликовать** |
| commit (git) | **обязательство** | **коммит / зафиксировать** |
| pipeline (CI/CD) | **трубопровод** (= plumbing) | **пайплайн / конвейер** |
| architecture (software) | **архитектура (здания)** | **архитектура (программная/системная)** |
| source of truth | **источник правды** (literal) | **источник истины / эталонный источник данных** |
| bug (software) | **жук** (= insect) | **ошибка / баг** |
| scale (software) | **весы** (= weighing scale) | **масштабирование / масштабируемость** |
| support (feature) | **поддерживать (= hold up)** | **поддерживать / быть совместимым с** (verb works in both contexts) |
| listings (app store) | **списки** | **страница приложения / карточка приложения / витрина** |
| migrate (data) | **мигрировать** (informal accepted) | **перенести данные / выполнить миграцию** |

## Calques to Avoid

### Structural calques

| Wrong (literal English) | Correct (Russian) |
|--------------------------|---------------------|
| `Файл не может быть найден` (passive calque) | **`Файл не найден`** |
| `В случае если` | **`Если`** |
| `делать смысл` | **`иметь смысл`** |
| `взять место` | **`происходить / иметь место`** |
| `базируясь на` | **`на основе`** |
| `с целью` (overused) | **`чтобы`** |
| `Получите переведено за минуты` ("Get X done") | **`Перевод за считанные минуты`** |
| `Держите ваши проекты синхронизированными` | **`Поддерживайте синхронизацию проектов`** |
| `Сделайте ваш рабочий процесс быстрее` | **`Ускорьте рабочий процесс`** |
| `провести улучшение` | **`улучшить`** |
| `осуществить выбор` | **`выбрать`** |
| `предоставить ответ` | **`ответить`** |

### Noun-stacking calques (English compound nouns → Russian adjective/genitive)

| Wrong (noun-stacked) | Correct (adjective or genitive) |
|----------------------|------------------------------------|
| `проект папка` | **`папка проекта / проектная папка`** |
| `пользователь настройки` | **`настройки пользователя / пользовательские настройки`** |
| `опция языка` | **`языковые настройки / выбор языка`** |
| `предпочтение тона` | **`предпочтительный тон / выбор тона`** |

### Hyphenated `Авто-X` calques

| Wrong | Correct |
|-------|---------|
| `Авто-определено` | **`Автоматически определено`** |
| `авто-сохранение` | **`автосохранение`** (compound, NO hyphen) |
| `авто-заполнение` | **`автозаполнение`** |
| `авто-обнаружение` | **`автоматическое обнаружение / автообнаружение`** |

### Proper-noun calques

| Wrong | Correct |
|-------|---------|
| `Соединённые Штаты Америки` (in UI) | **`США`** |
| `Соединённое Королевство Великобритании и Северной Ирландии` | **`Великобритания`** |
| `английский язык Соединённых Штатов` | **`американский английский`** |

### Idiom calques

| Wrong (literal) | Natural Russian |
|-----------------|-----------------|
| Break a leg (literal) | **Ни пуха ни пера!** |
| Piece of cake (literal) | **Проще простого / Раз плюнуть** |
| It's raining cats and dogs | **Льёт как из ведра** |
| At the end of the day | **В конечном счёте / В итоге** |

## Marketing "Zero X" → "Без X / Никаких X"

| Wrong | Correct |
|-------|---------|
| `Ноль простоев / Zero downtime` | **`Без простоев / Без перерывов в работе / Непрерывная доступность`** |
| `Ноль ошибок` | **`Без ошибок / Никаких ошибок`** |
| `Ноль обслуживания` | **`Не требует обслуживания`** |
| `Ноль обязательств` | **`Без обязательств`** |

## Compound Adjectives — natural construction

| English pattern | Wrong (calque) | Correct |
|-----------------|----------------|---------|
| AI-powered | `ИИ-управляемый / ИИ-приведённый в действие` | **`на основе ИИ / с использованием ИИ / с ИИ`** |
| context-aware | `контекстно-осведомлённый` | **`контекстный / учитывающий контекст`** |
| user-friendly | `пользователь-дружественный` | **`удобный для пользователя / удобный в использовании`** |
| cloud-based | `облако-основанный` | **`облачный / на основе облака / размещённый в облаке`** |
| data-driven | `данные-управляемый` | **`основанный на данных / на базе данных`** |

## Compound Descriptive Nouns

| English | Wrong | Correct |
|---------|-------|---------|
| mom creators | мама создатели | **матери-создатели контента / мамы-блогеры** |
| niche creators | нишевые создатели | **создатели нишевого контента / специализированные авторы** |
| beauty influencers | бьюти-инфлюенсеры (acceptable in marketing) | **инфлюенсеры в сфере красоты** (formal) |

## Word-Sense Disambiguation (polysemy)

| English (context) | Wrong (first dictionary meaning) | Correct (contextual) |
|--------------------|----------------------------------|------------------------|
| copy (marketing context) | **копия** (= duplicate) | **текст / рекламный текст** |
| sauce (figurative) | **соус** | **секрет / суть** |
| bug (software) | **жук** | **ошибка / баг** |
| scale (marketing) | **весы** | **масштаб / масштабирование** |
| backstory | **предыстория** (literal — may work) | **предыстория / история создания / контекст** |
| resume (verb) | **резюме** | **возобновить / продолжить** |

## Brand Names

- Foreign tech brands default to **masculine** when gender is implied by `сервис` (service): `сервис OneSky` = masc.
- When the brand is the company itself, use **feminine** (implied `компания`): `компания Apple`, `компания Microsoft`.
- DO NOT decline brand names in cases — keep them in original Latin form: `с OneSky` (NOT `с OneSkyом`).
- Russian honorific naming convention does not extend to brands.

## Cultural Conventions

- **Communication style:** direct, professional. Formal Russian (B2B, legal, government) uses Вы, complex syntax, full sentences.
- **Date format:** `15.01.2024` (DD.MM.YYYY with periods) or `15 января 2024 г.` (with `г.` = "of the year").
- **Time format:** 24-hour `14:30`. AM/PM not used.
- **Currency:** Russian Ruble `99,99 ₽` (space before symbol, comma decimal). Symbol after amount.
- **Phone:** `+7 (XXX) XXX-XX-XX` international, `8 (XXX) XXX-XX-XX` domestic (8 prefix instead of +7).
- **Address ordering:** Russian addresses go from LARGEST to smallest (country, city, street, house, apartment).
- **Names:** Russian names follow the pattern `First + Patronymic + Last` (Иван Петрович Сидоров). In formal address, use `First + Patronymic` (Иван Петрович) WITHOUT the last name. In casual address, use first name alone (Иван). For UI, typically use first name only unless replicating formal correspondence.

## Greetings, Closings, and Email Conventions

### Greetings
- **Здравствуйте** — universal polite hello (formal, time-agnostic).
- **Добрый день** — good day (until ~18:00).
- **Доброе утро** — good morning.
- **Добрый вечер** — good evening.
- **Привет** — informal hello.
- **Приветствуем** — formal welcome (used in UI: "Приветствуем в OneSky").
- **Добро пожаловать** — welcome (UI standard).

### Goodbyes
- **До свидания** — formal goodbye (until next meeting).
- **Всего доброго / Всего хорошего** — formal warm goodbye.
- **Пока** — informal bye.

### Email salutations
- Formal: `Уважаемый Иван Петрович,` (m) / `Уважаемая Анна Сергеевна,` (f) — with patronymic. `Здравствуйте, Иван Петрович!` (slightly less formal).
- Semi-formal: `Здравствуйте, Иван!`
- Informal: `Привет, Иван!` / `Привет!`

### Email closings
- Formal: `С уважением,` (with respect — standard formal), `С наилучшими пожеланиями,` (with best wishes), `Искренне Ваш,` (sincerely yours).
- Semi-formal: `Всего доброго,` / `С уважением,`.
- Informal: `Пока!` / `До связи!` / `Удачи!`.

### Politeness particles
- **пожалуйста** — please (place mid-sentence after the verb: `Сохраните, пожалуйста, файл` — preferred placement).
- **будьте добры** — "kindly / would you" (formal request).
- **спасибо** — thank you (informal/neutral).
- **благодарю Вас** — formal thanks.

## Source-Structure Parsing (severity 2.5)

English compound noun phrases and modifier chains require careful restructuring.

| English | Wrong (English-structure) | Correct (Russian structure) |
|---------|---------------------------|------------------------------|
| `user-friendly interface` | дружественный пользователь интерфейса | **удобный для пользователя интерфейс** |
| `files selected for translation` | файлы выбранные перевод | **файлы, выбранные для перевода** (для + genitive) |
| `knowing German expands 30%` | Если Вы знаете немецкий, охват расширится (conditional misread) | **Учитывая, что знание немецкого расширяет охват на 30%** (factual) |

## Tense / Aspect Fidelity (severity 2.0)

Preserve English progressive ("we are building") with Russian imperfective; preserve simple past with Russian perfective.

| English | Wrong | Correct |
|---------|-------|---------|
| we are building (ongoing) | мы построили (perfective past) | **мы строим / мы создаём** (imperfective present) |
| costs are increasing (ongoing) | расходы выросли (perfective past) | **расходы растут** (imperfective present) |
| we built (completed) | мы строим (imperfective ongoing) | **мы построили / мы создали** (perfective past) |
| translating files (in progress) | перевести файлы (perfective infinitive) | **переводить файлы / перевод файлов** (imperfective) |

## Block Verb Mood Consistency

Child items must match the verb mood frame set by the parent title/heading.

| Title frame | Wrong child | Correct child |
|-------------|-------------|---------------|
| `Что Вы получите:` (declarative) | `Получите предложение...` (imperative) | `Вы получите предложение...` or `Предложение на следующий рабочий день...` (noun phrase) |
| `Шаги:` (instructional) | `Вы бы настроили аккаунт...` (conditional) | `Настройте свой аккаунт...` (imperative) or `Настроить аккаунт...` (infinitive) |

## Self-Check Checklist (run before finalizing)

### Critical accuracy (must all pass)
- [ ] **Case selection** correct for every noun (6-case system: nom/gen/dat/acc/instr/prep)
- [ ] **Verb-governed case** correct (помогать+dat, управлять+instr, достичь+gen)
- [ ] **Numeral-noun agreement** correct (1=nom.sg, 2-4=gen.sg, 5+=gen.pl, with 11-14 exception)
- [ ] **ICU plural categories**: `one / few / many / other` used (NOT just one/other)
- [ ] **Past-tense gender agreement** (Система работала, Приложение запустилось, Файлы загрузились)
- [ ] **Adjective gender + case agreement** correct (новая система, новое приложение)
- [ ] **Relative pronoun agreement** (который/которая/которое matches antecedent)
- [ ] **Verb aspect** correct (perfective for completed, imperfective for ongoing)
- [ ] **Вы/ты consistent** throughout (Вы always capitalized; matched possessives + imperatives)
- [ ] **Word integrity** — no split prefixes (`построить` NOT `по строить`)
- [ ] **Technical identifiers stay Latin** (`Git`, `API`, `JSON`, `npm`, `Node.js` — never transliterated)
- [ ] **No articles inserted** (no "the/a" calques)
- [ ] **No `есть` copula** in present tense (`Это книга`, NOT `Это есть книга`)
- [ ] All `{variables}` and ICU intact
- [ ] **Domain terminology** uses IT meaning (architecture=software, pipeline=CI/CD, bug=software defect)

### Naturalness
- [ ] **Buttons in infinitive perfective** (`Сохранить, Удалить, Войти`)
- [ ] **Status messages impersonal** (`Загружается... / Идёт загрузка...`) — NEVER first-person
- [ ] **Completion in neuter perfective participle** (`Перевод завершён, Сохранено`)
- [ ] **Failure** uses `Не удалось` + infinitive OR `Ошибка` + genitive
- [ ] **Empty state** uses `Нет X` or `Пока нет X` (NOT `Не было найдено никаких X`)
- [ ] **Drag-drop verbs** correct (`перетащить / отпустить`, NOT `бросить / уронить`)
- [ ] **File picker** uses `Выбрать` (NOT `Просмотреть`)
- [ ] **«ёлочки» quotes** (`«...»` primary, `„...""` nested) — NOT English `"..."`
- [ ] **Em-dash** with spaces for copular sentences and ranges
- [ ] **Comma rules**: comma before `что/который/если/потому что`; NO comma before `и/или/либо`
- [ ] **No verbed anglicisms** (`удалить` NOT `дилитнуть`; `проверить` NOT `чекать`)
- [ ] **Native preferred over loan** for non-established (`обновление` NOT `апдейт`; `отзыв` NOT `фидбэк`)
- [ ] **No noun-stacking calques** (`папка проекта` NOT `проект папка`)
- [ ] **No hyphenated `Авто-X`** — use full form or compound (`автосохранение`)
- [ ] **No `провести/осуществить/предоставить` + verbal noun** when direct verb works (`улучшить` NOT `провести улучшение`)
- [ ] **Marketing zero**: `Без X` (NOT `Ноль X`)
- [ ] **Compound adjectives natural** (`удобный для пользователя`, `на основе ИИ`)
- [ ] **No false friends** in wrong sense (актуальный ≠ actual, реализовать ≠ realize, резюме ≠ resume)
- [ ] **Currency** `99,99 ₽`; **date** `15.01.2024`; **numbers** `1 234,56`
- [ ] **Block verb mood** consistent between title and child items

## Worked Example

**Source:** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

### Russian (Вы, formal)

Добро пожаловать! Пожалуйста, выберите файл для загрузки. Мы поддерживаем более 25 форматов и переводим файл на 5 языков за {seconds} секунд. Не беспокойтесь — Вы можете отменить операцию в любой момент.

### Russian (ты, informal)

Привет! Выбери файл для загрузки. Мы поддерживаем более 25 форматов и переводим его на 5 языков за {seconds} секунд. Не волнуйся — отменить можно в любой момент.

### Common errors both would catch

- `25+ форматов` → `более 25 форматов` (Russian quantity).
- `за 5 языков` (calque) → `на 5 языков` (translating INTO languages takes `на` + accusative).
- `{seconds}` without unit/case agreement → `{seconds} секунд` (gen.pl for typical 5+ display values; ICU should provide `one/few/many/other` for accuracy).
- `Не имейте беспокойств` (calque of "don't worry") → `Не беспокойтесь / Не волнуйся`.
- `Сохраняться` on a button → `Сохранить` (perfective infinitive).
- `Файл сохранился` as confirmation → `Файл сохранён / Сохранено` (neuter participle).
- `Перевод провалился` → `Не удалось перевести / Ошибка перевода`.
- Mixed `Вы выберите свой файл` → either fully formal `Вы выберите Ваш файл` OR drop one to `Выберите файл` (imperative is acceptable in instructions).
- `Гит коммит` → `Git коммит` (Latin script preserved).
- `5 файла` → `5 файлов` (gen.pl after 5+).
- ICU `{n, plural, one {# файл} other {# файлов}}` → must be `{n, plural, one {# файл} few {# файла} many {# файлов} other {# файла}}`.
