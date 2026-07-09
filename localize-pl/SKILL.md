---
name: localize-pl
description: Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Polish (pl). Enforces 7-case grammar including active vocative (Aniu!, użytkowniku!), 3-gender system with FIVE gender forms in plural (masculine-personal vs non-masculine-personal split — known as "męskoosobowy" vs "niemęskoosobowy"), ICU one/few/many/other plurals (1/2-4 ends 2-4 not 12-14/5+ with 11-14 going to many), perfective/imperfective verb aspect, formal address via Pan/Pani + 3rd person verb (NOT a 2nd-person "Vy" form — uniquely Polish T-V system), Polish diacritics ą ć ę ł ń ó ś ź ż (ł is essential — never replace with l), impersonal voice for status (Przetwarzanie / Trwa obliczanie / Oblicza się, NEVER first-person Obliczam), neuter perfective participle for completion (Zapisano, Wczytano), "Nie udało się" + infinitive for failure, infinitive buttons (Zapisz wait — actually imperative Zapisz), comma rules (no comma before lub/i/oraz), PLN złoty currency (99,99 zł — Poland did NOT adopt euro).
---

# Translate to Polish (pl) — High-Fidelity Skill

## Scope & Variants

Polish is a single standard target — Modern Standard Polish (język polski literacki). No regional split for product UI:

| Locale | Notes |
|--------|-------|
| `pl` / `pl-PL` | Standard Polish (Poland). Default and only target. |

Polish has dialect variations (Silesian, Kashubian) but these have their own ISO codes (`szl`, `csb`) and are NOT covered by `pl`.

---

## Register Auto-Detection (Apply Before Translating) — POLISH IS DIFFERENT

Polish formality is **structurally unique** among Slavic languages. Unlike Russian/Ukrainian/Czech/Slovak/Croatian/Serbian which use a `Vy/ty` 2nd-person split, Polish uses **`Pan` (Mr. / sir) and `Pani` (Mrs. / madam)** + **3rd-person verb forms** for formal address.

| Register | Form | Verb agreement | Example |
|----------|------|----------------|---------|
| Informal (ty) | `ty` + 2nd-person sg. | -sz ending | `Możesz to zrobić.` (You can do it.) |
| Formal (Pan / Pani) | `Pan` (m.) / `Pani` (f.) + **3rd-person sg.** | -e ending | `Może Pan to zrobić.` / `Może Pani to zrobić.` |
| Formal (mixed group) | `Państwo` + 3rd-person pl. | — | `Mogą Państwo to zrobić.` |

**This is the most distinctive feature of Polish formality and trips up most AI translators.** They often produce "Polish Vy-form" by analogy with Czech/Russian — but Polish has no `Vy` form for formal singular. The formal form is `Pan/Pani + 3rd person verb`.

Auto-detect from source:

| Source signal | Target register |
|---------------|-----------------|
| Casual / conversational / personal (`Hey!`, contractions, emoji, marketing voice) | **Informal (ty)** — `ty` lowercase, 2nd-person sg. verb endings (-sz: możesz, widzisz), familiar imperative (singular: wybierz, kliknij, otwórz). |
| Neutral product UI / docs / consumer software (DEFAULT) | **Inclusive impersonal** — UI often avoids both ty and Pan/Pani by using **impersonal/infinitive constructions**. E.g., `Kliknij, aby kontynuować` (informal-leaning but neutral) OR `Aby kontynuować, należy kliknąć` (formal impersonal). |
| Legal / banking / government / enterprise | **Formal (Pan / Pani / Państwo)** — capitalized in direct address, 3rd-person verb, possessive `Pana / Pani / Państwa`. |

**Hard rule: NEVER use `Wy` as a singular formal pronoun** — `Wy` is plural informal "you all" only. Using it as formal singular is a critical error (and politically loaded — was associated with the communist period when official documents used it formal-Russianized style).

**Capitalization of Pan/Pani:** in direct address (letters, UI greetings), capitalize: `Drogi Panie`, `Szanowna Pani`, `dla Pani`. In general references (talking ABOUT a person), lowercase: `Pan Nowak jest tutaj`.

**Default for software UI: impersonal / infinitive-based** (sidesteps the ty/Pan question) OR ty-form (for consumer apps) OR Pan/Pani (for B2B/banking/government).

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. Word integrity — verb prefixes NEVER split (severity 3.0)

Polish verbs with prefixes are **single words**. Splitting is a critical error.

| ✗ Wrong (split) | ✓ Correct (joined) |
|-----------------|---------------------|
| `prze tłumaczyć` | **`przetłumaczyć`** (to translate) |
| `wy konać` | **`wykonać`** (to execute) |
| `prze nieść` | **`przenieść`** (to transfer) |
| `na pisać` | **`napisać`** (to write) |
| `za pisać` | **`zapisać`** (to save / record) |
| `od pisać` | **`odpisać`** (to reply) |
| `przy jąć` | **`przyjąć`** (to accept) |
| `roz począć` | **`rozpocząć`** (to begin) |
| `po brać` | **`pobrać`** (to download) |

**Reflexive `się` is a SEPARATE clitic** — not attached to verb. `zalogować się`, `zarejestrować się`, `zajmować się`. Writing `zalogowaćsię` is wrong.

### 2. Polish diacritics — preserve all, especially ł (severity 2.5)

Polish uses: `ą ć ę ł ń ó ś ź ż`. Stripping any is a critical readability failure. Especially:

- **ł** (slashed L, /w/ sound — "łańcuch" pronounced "wanchooh") — easily confused with `l` but it's a distinct letter. NEVER replace with `l`.
- **ó** (kreska o, /u/ sound) — distinct from `o`. NEVER replace with `o` or `u`.
- **ę** and **ą** (nasal vowels) — distinct from `e` and `a`.
- **ś ć ź ń** (acute-marked palatalized consonants) — distinct from `s c z n`.
- **ż** (dotted z) — distinct from `ź` (acute-z) which is itself distinct from `z`.

| ✗ Stripped | ✓ Correct |
|------------|-----------|
| uzytkownik | **użytkownik** |
| ustawienia | **ustawienia** ✓ (no diacritics here, illustrating that not all words need them) |
| zaloguj sie | **zaloguj się** |
| pobrac | **pobrać** |
| polaczenie | **połączenie** (note the ł!) |
| skonczyc | **skończyć** |
| zrodlo | **źródło** |
| jezyk | **język** |
| wybierz | **wybierz** ✓ |
| przeglad | **przegląd** |

### 3. Seven-case system — Polish retains active vocative (severity 2.5)

Polish uses **all 7 Slavic cases**, INCLUDING an active vocative (like Czech/Ukrainian, unlike Slovak/Russian).

| Case | Question | Use | Example (m. anim. "użytkownik") | Example (f. "aplikacja") |
|------|----------|-----|--------------------------------|--------------------------|
| Mianownik (NOM) | kto? co? | Subject | użytkownik | aplikacja |
| Dopełniacz (GEN) | kogo? czego? | Possession, "of", absence, 5+ count | użytkownika | aplikacji |
| Celownik (DAT) | komu? czemu? | Indirect object, "to" | użytkownikowi | aplikacji |
| Biernik (ACC) | kogo? co? | Direct object | użytkownika (animate=GEN) / plik (inanimate=NOM) | aplikację |
| Narzędnik (INS) | kim? czym? | "With", means | użytkownikiem | aplikacją |
| Miejscownik (LOC) | o kim? o czym? | Location (always w/ prep) | o użytkowniku | o aplikacji |
| **Wołacz (VOC)** | — | **Direct address — ACTIVE in Polish** | użytkowniku! | aplikacjo! |

**Critical: animate masculine accusative = genitive form.** `widzę użytkownika`, NOT `widzę użytkownik`.

**Vocative usage** — Polish ACTIVELY uses vocative for direct address. Common vocative endings: m. `-u/-e/-ie` (Krzysztof → Krzysztofie, Adam → Adamie, syn → synu), f. `-o/-u` (Ania → Aniu, Anna → Anno, mama → mamo).

| ✗ Wrong (nominative) | ✓ Correct (vocative) |
|----------------------|----------------------|
| Cześć, Anna! | **Cześć, Anno!** |
| Witaj, Krzysztof! | **Witaj, Krzysztofie!** |
| Drogi użytkownik! | **Drogi użytkowniku!** |
| Drogi Pan Nowak! | **Drogi Panie Nowak!** (or formally `Szanowny Panie Nowak!`) |

For UI greetings using user's first name, vocative is REQUIRED in formal/respectful tone.

### 4. **CRITICAL: Polish has 5 gender forms in plural — męskoosobowy vs niemęskoosobowy** (severity 3.0)

This is **uniquely Polish**. While other Slavic languages have 3 genders (m/f/n) in plural with various splits, Polish has the strongest grammatical split:

**Plural gender categories (Polish has 2 plural gender forms — split from the 3 singular genders):**

| Category | Polish term | Members | Example noun (pl.) |
|----------|-------------|---------|---------------------|
| **Masculine-personal** | męskoosobowy | Male humans ONLY | mężczyźni, użytkownicy, programiści |
| **Non-masculine-personal** | niemęskoosobowy | Everything else — women, children, animals, objects | kobiety, dzieci, koty, pliki, systemy, aplikacje, ustawienia |

**Verb past-tense agreement plural:**
- m.-personal: `-li` ending (oni byli, oni pracowali, użytkownicy zalogowali się)
- non-m.-personal: `-ły` ending (one były, one pracowały, pliki zostały zapisane)

**Adjective agreement plural:**
- m.-personal: `-i / -y` ending (nowi użytkownicy, dobrzy ludzie)
- non-m.-personal: `-e` ending (nowe pliki, dobre kobiety, nowe systemy)

**Examples of how this breaks naïve translation:**

| ✗ Wrong (treating all as one) | ✓ Correct (m-personal vs non-m-personal) |
|-------------------------------|------------------------------------------|
| Pliki zostali zapisani (using m-personal -li for files) | **Pliki zostały zapisane** (files are not male humans → non-m-personal -ły / -e) |
| Użytkowniki zalogowały się | **Użytkownicy zalogowali się** (users include male humans → m-personal -li) |
| Nowi pliki | **Nowe pliki** (files → non-m-personal -e) |
| Nowe użytkownicy | **Nowi użytkownicy** (male users → m-personal -i) |
| Kobiety zalogowali się | **Kobiety zalogowały się** (women only → non-m-personal -ły) |

**Mixed groups containing at least one male human take m-personal forms.** A group of one man and ten women is m-personal. A group of all women is non-m-personal.

**Most UI items (pliki, systemy, ustawienia, aplikacje, użytkownicy, klienci):**
- `pliki, systemy, ustawienia, aplikacje, opcje` → **non-m-personal** (`zostały zapisane`, `nowe pliki`)
- `użytkownicy, klienci, programiści, administratorzy` (mixed/male) → **m-personal** (`zalogowali się`, `nowi użytkownicy`)
- `użytkowniczki, klientki` (women-only forms) → **non-m-personal** (`zalogowały się`, `nowe użytkowniczki`)

This is the single most-mocked Polish translation error by native speakers when AI gets it wrong.

### 5. Preposition + governed case (severity 2.5)

| Preposition | Case | Example |
|-------------|------|---------|
| w / we (in) | LOC (location) | w systemie |
| do (into / to) | GEN | do systemu |
| na (on/onto) | LOC / ACC | na ekranie / na ekran |
| z / ze (with) | INS | z użytkownikiem |
| bez (without) | GEN | bez błędów |
| dla (for) | GEN | dla użytkownika |
| od (from) | GEN | od użytkownika |
| do (to/until) | GEN | do końca |
| o (about) | LOC | o użytkowniku |
| po (after) | LOC | po zalogowaniu |
| przed (before) | INS | przed zapisaniem |
| za (per / behind) | ACC / INS | za plik / za stołem |
| u (at, with) | GEN | u użytkownika |
| przy (at, by) | LOC | przy zapisywaniu |

**"per" in Polish:** use `za + ACC` for rate (`za plik`), `na + ACC` for distribution (`na użytkownika`), `dziennie` for "per day". Never `per plik` (English calque).

### 6. ICU plurals — one / few / many / other (1 / 2-4 ends in 2-4 not 12-14 / 5+ with 11-14 going to many / other for fractions) (severity 2.5)

```icu
{count, plural,
  one {# plik}
  few {# pliki}
  many {# plików}
  other {# pliku}
}
```

**CLDR plural category boundaries** (Polish):

| Category | Rule | Examples | Noun form |
|----------|------|----------|-----------|
| `one` | n = 1 | 1 | **NOM singular** (plik) |
| `few` | n % 10 ∈ {2,3,4}, n % 100 ∉ {12,13,14} | 2, 3, 4, 22, 23, 24, 102, 103 | **NOM plural** (pliki) |
| `many` | n = 0, n % 10 ∈ {0,1,5-9}, n % 100 ∈ {11-14} | 0, 5-20, 25-30, 100, 11, 12, 13, 14, 21 (yes 21!) | **GEN plural** (plików) |
| `other` | fractions | 1.5, 2.5 | **GEN singular** (pliku) |

**Critical note:** Polish's `many` category includes 11-14 (like Russian/Ukrainian/Croatian) AND also includes **21, 31, 41**, etc. Polish uses `one` ONLY for the integer 1 itself — NOT for 21, 31, 41 like Russian does. Polish `21 plików` (GEN pl) not `21 plik` (NOM sg).

### 7. Numeral-noun agreement (severity 2.0)

| Count | Pattern | Example |
|-------|---------|---------|
| 1 | NOM sg | 1 plik |
| 2, 3, 4 (ends in 2-4, NOT 12-14) | NOM pl | 2 pliki, 3 użytkownicy (m-pers), 22 pliki |
| 5+ AND 11-14 AND 21, 31, 41… | GEN pl | 5 plików, 11 plików, 21 plików, 100 plików |
| Fractions | GEN sg | 2,5 pliku |

### 8. Three-gender singular + masculine animate/inanimate (severity 2.0)

In SINGULAR, Polish distinguishes:
- **Masc. personal/animate** (male humans, named animals) → genitive form for accusative: `widzę użytkownika`
- **Masc. inanimate** (objects, abstracts) → accusative = nominative: `widzę plik`
- **Feminine** (-a ending mostly): `aplikacja`, `użytkowniczka`
- **Neuter** (-o/-e/-ie ending): `ustawienie`, `okno`, `narzędzie`

Wrong gender adjective is auto-fail: `nowa system` ✗, `nowy aplikacja` ✗, `nowa ustawienie` ✗.

### 9. Past-tense gender agreement + m-personal/non-m-personal in plural (severity 2.5)

(Documented in rule #4 above; restating here as a checklist item.)

| Subject | L-participle | Example |
|---------|--------------|---------|
| m. sg. | -ł | on pracował |
| f. sg. | -ła | ona pracowała |
| n. sg. | -ło | ono pracowało |
| **m-personal pl.** | **-li** | **oni pracowali** (mixed/male group) |
| **non-m-personal pl.** | **-ły** | **one pracowały** (women/objects/animals) |

### 10. Verb aspect — perfective vs imperfective (severity 2.0)

| Imperfective (process, ongoing) | Perfective (single completed event) | English |
|--------------------------------|--------------------------------------|---------|
| zapisywać | zapisać | save |
| usuwać | usunąć | delete |
| pobierać | pobrać | download |
| wysyłać | wysłać | send |
| otwierać | otworzyć | open |
| zamykać | zamknąć | close |
| tworzyć | utworzyć | create |
| edytować | zedytować | edit |
| zmieniać | zmienić | change |
| pisać | napisać | write |
| czytać | przeczytać | read |
| wybierać | wybrać | choose / select |
| tłumaczyć | przetłumaczyć | translate |
| logować się | zalogować się | log in |

**UI patterns by aspect:**
- Buttons (single action) → **perfective imperative**: `Zapisz`, `Usuń`, `Wyślij`, `Wybierz`. Polish UI convention is IMPERATIVE (not infinitive).
- Ongoing status → **imperfective verbal noun** (`Zapisywanie…`, `Wczytywanie…`) or **`Trwa + verbal noun`**.
- Completed → **impersonal neuter perfective participle (-no/-to)** (`Zapisano`, `Wczytano`, `Wysłano`).

### 11. Verb-construction integrity — no stacked finite verbs (severity 2.0)

English `-ing` (gerund as adverbial) MUST be rendered with **imiesłów przysłówkowy współczesny** (Polish adverbial participle in `-ąc`) OR restructure with `przy + verbal noun`.

| ✗ Stacked finite | ✓ Adverbial participle / przy + noun | English |
|------------------|--------------------------------------|---------|
| `Spędziłem 6 lat budowałem firmę` | **`Spędziłem 6 lat budując firmę`** OR **`Spędziłem 6 lat na budowaniu firmy`** | I spent 6 years building the business |
| `Pracowałem podczas gdy pisałem raport` | **`Pracowałem pisząc raport`** OR **`Pracowałem przy pisaniu raportu`** | I worked while writing the report |

**Common -ąc forms (imperfective verbs only):**
- pisać → pisząc (writing)
- budować → budując (building)
- czekać → czekając (waiting)
- używać → używając (using)
- pracować → pracując (working)

---

## Pronouns and Possessives

### Personal pronouns

| English | Polish | Notes |
|---------|--------|-------|
| I | ja | |
| you (sg. informal) | ty | |
| **you (sg. formal — masc.)** | **Pan** (+ 3rd-person verb) | Capitalized in direct address |
| **you (sg. formal — fem.)** | **Pani** (+ 3rd-person verb) | Capitalized in direct address |
| **you (pl. formal)** | **Państwo** (+ 3rd-person pl. verb) | Capitalized |
| you (pl. informal — all male/mixed) | wy / panowie | wy informal, panowie formal-pl |
| you (pl. informal — all female) | wy / panie | |
| he | on | |
| she | ona | |
| it | ono | |
| we | my | |
| they (m-personal) | oni | |
| they (non-m-personal) | one | |

### Possessive pronouns

| Person | m. sg. | f. sg. | n. sg. |
|--------|--------|--------|--------|
| mój (my) | mój | moja | moje |
| twój (your sg. informal) | twój | twoja | twoje |
| **Pana (your formal m. — invariable)** | **Pana** | **Pana** | **Pana** |
| **Pani (your formal f. — invariable)** | **Pani** | **Pani** | **Pani** |
| **Państwa (your formal pl. — invariable)** | **Państwa** | **Państwa** | **Państwa** |
| jego (his — invariable) | jego | jego | jego |
| jej (her — invariable) | jej | jej | jej |
| swój (reflexive — own) | swój | swoja | swoje |
| nasz (our) | nasz | nasza | nasze |
| ich (their — invariable) | ich | ich | ich |

**Reflexive `swój`** is required when possessor = subject of same clause.

---

## UI Conventions

### Buttons — perfective IMPERATIVE

Polish platform UIs (Windows PL, Chrome PL, macOS PL) use **imperative** for buttons (NOT infinitive like Czech/Slovak). This is a deliberate convention choice.

| English | ✓ Polish imperative |
|---------|---------------------|
| Save | **Zapisz** |
| Cancel | **Anuluj** |
| Delete | **Usuń** |
| Send | **Wyślij** |
| Edit | **Edytuj** |
| Search | **Szukaj** / **Wyszukaj** |
| Confirm | **Potwierdź** |
| Continue | **Kontynuuj** / **Dalej** |
| Submit | **Wyślij** / **Prześlij** |
| Sign in / Log in | **Zaloguj się** |
| Sign out | **Wyloguj się** |
| Sign up | **Zarejestruj się** |
| Next | **Dalej** / **Następny** |
| Back | **Wstecz** / **Powrót** |
| Done | **Gotowe** / **Zakończ** |
| OK | **OK** |
| Close | **Zamknij** |
| Upload | **Prześlij** / **Wgraj** |
| Download | **Pobierz** |
| Refresh | **Odśwież** |
| Settings | **Ustawienia** |
| Apply | **Zastosuj** |
| Reset | **Resetuj** / **Zresetuj** |
| Select all | **Zaznacz wszystko** |
| Add more | **Dodaj więcej** ✓ (or `Dodaj kolejne`) |

For **formal Pan/Pani register**, you might use polite forms like `Proszę zapisać` (please save) — but for button labels, the bare imperative is standard regardless of register.

### Status messages — three distinct patterns

**Ongoing (in-flight)** → **imperfective verbal noun** OR **`Trwa` + verbal noun** (NEVER first-person)

| English | ✓ Polish |
|---------|----------|
| Loading… | **Wczytywanie…** / **Trwa wczytywanie…** |
| Saving… | **Zapisywanie…** / **Trwa zapisywanie…** |
| Sending… | **Wysyłanie…** / **Trwa wysyłanie…** |
| Processing… | **Przetwarzanie…** / **Trwa przetwarzanie…** |
| Connecting… | **Łączenie…** / **Trwa łączenie…** |
| Searching… | **Wyszukiwanie…** / **Trwa wyszukiwanie…** |
| Translating… | **Tłumaczenie…** / **Trwa tłumaczenie…** |
| Please wait | **Proszę czekać** |

**Critical impersonal voice rule:** NEVER first-person (`Obliczam…`, `Analizuję…`, `Przetwarzam…`) — sounds awkward.

**Completed** → **Impersonal neuter perfective participle (`-no/-to`)**

| English | ✓ Polish |
|---------|----------|
| Saved | **Zapisano** |
| Done | **Gotowe** / **Zakończono** |
| Translation complete | **Przetłumaczono** / **Tłumaczenie zakończone** |
| File uploaded | **Plik przesłano** / **Przesłano** |
| Sent | **Wysłano** |
| Payment successful | **Płatność zrealizowana** / **Opłacono** |

**Critical**: Use the impersonal `-no/-to` form, NOT personal past:
- ✗ `Plik został zapisany` (passive — OK but verbose)
- ✓ **`Zapisano`** (impersonal — preferred for status)
- ✗ `Plik zapisał się` (reflexive past — awkward as status)
- ✓ **`Zapisano`** ✓

**Failed** → **`Nie udało się` + infinitive** OR **`Błąd` + GEN of verbal noun**

| English | ✓ Polish |
|---------|----------|
| Save failed | **Nie udało się zapisać** / **Błąd zapisywania** |
| Upload failed | **Nie udało się przesłać** / **Błąd przesyłania** |
| Translation failed | **Nie udało się przetłumaczyć** / **Błąd tłumaczenia** |
| Connection failed | **Nie udało się połączyć** / **Błąd połączenia** |
| File not found | **Nie znaleziono pliku** |

NEVER use:
- ✗ `Tłumaczenie nie powiodło się` (verbose)
- ✗ `Zapis nieudany` (calque)

### Empty states — `Brak X` / `Nie znaleziono`

| ✗ Verbose | ✓ Concise |
|-----------|-----------|
| Nie znaleziono żadnych wyników | **Brak wyników** |
| Nie masz jeszcze żadnych projektów | **Brak projektów** |
| Nie ma żadnych plików | **Brak plików** |

### Drag-and-drop

- drag → **przeciągnij** (informal) / **proszę przeciągnąć** (formal)
- drop → **upuść** (NOT `zrzuć` = dump/throw down — wrong sense)
- Combined: **`Przeciągnij pliki tutaj`** (Drag files here).

### File picker — `Wybierz` (action verb)

| ✓ Polish |
|----------|
| **Wybierz pliki** (Choose files) |
| **Wybierz plik** (Choose a file) |
| **Kliknij, aby wybrać** (Click to choose) |

### Quantity expressions

| ✗ Calque | ✓ Native |
|----------|----------|
| 25+ języków | **ponad 25 języków** / **więcej niż 25 języków** |
| +{count} więcej | **i {count} więcej** / **jeszcze {count}** |

### Error messages — what + next step

| ✗ Bare | ✓ With next step |
|--------|------------------|
| Nie znaleziono pliku. | **Nie znaleziono pliku. Sprawdź ścieżkę.** |
| Błąd sieci. | **Błąd sieci. Spróbuj ponownie.** |
| Nieprawidłowy e-mail. | **Adres e-mail jest nieprawidłowy. Sprawdź format.** |

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Polish | Notes |
|------|--------|-------|
| Question mark | `?` | Same as English |
| Comma | `,` | Different conjunction rules |
| Period | `.` | Same |
| Colon | `:` | Same |
| Quotation marks | **`„…"`** (low-9 / high-9) primary, **`«…»`** for nested or alternative | Same as German style |
| Em-dash | `—` | Used for parenthetical breaks |

### Comma rules

Polish has **strict comma rules** (more so than English). Key principles:

| Rule | Example |
|------|---------|
| **NO comma** before `i` (and) | Wybierz plik **i** kliknij. |
| **NO comma** before `oraz` (and, formal) | rzetelnie **oraz** szybko. |
| **NO comma** before `lub / albo` (or) | Wybierz plik **lub** folder. |
| **NO comma** before `ani` (nor — when in sequence) | Nie jest to błąd **ani** problem. |
| **Comma** before `że` (that, subordinating) | Widzę, **że** plik jest otwarty. |
| **Comma** before `który / która / które` (relative) | Plik, **który** wybrałeś… |
| **Comma** before `aby / żeby` (in order to) | Kliknij, **aby** kontynuować. |
| **Comma** before `gdy / kiedy` (when) | Zapisz, **gdy** skończysz. |
| **Comma** before `jeśli / jeżeli` (if) | Zapisz, **jeśli** chcesz. |
| **Comma** before `ponieważ / bo` (because) | Anulowano, **ponieważ** nie powiodło się. |
| **Comma** before `ale / a / lecz` (but / and-contrast) | Szybko, **ale** skutecznie. |

**Critical**: Polish uses commas more strictly than English in subordinate clauses. Missing a comma before `że` is a common error.

### Numbers

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **space** (or no separator for 4-digit) | 1 234 567 (or 1234 for 4-digit) |
| Decimal separator | **comma (,)** | 3,14 / 99,99 |
| Negative | `-25` | |
| Percent | `25%` (no space typical, or `25 %` formal) | |

**Critical:** Polish uses **space for thousands, comma for decimal** — opposite of English.

### Dates

| Format | Example | Use |
|--------|---------|-----|
| DD.MM.YYYY | **15.01.2024** | Default for UI / business |
| D miesiąc YYYY | **15 stycznia 2024** | Long-form prose (month in genitive!) |
| D miesiąc YYYY r. | **15 stycznia 2024 r.** | Formal documents (`r.` = `roku`) |
| YYYY-MM-DD | 2024-01-15 | Technical/API only |

**Polish month names (lowercase always, declines — Slavic-rooted!):**

| Nominative | Genitive (used in dates) |
|------------|---------------------------|
| styczeń | stycznia |
| luty | lutego |
| marzec | marca |
| kwiecień | kwietnia |
| maj | maja |
| czerwiec | czerwca |
| lipiec | lipca |
| sierpień | sierpnia |
| wrzesień | września |
| październik | października |
| listopad | listopada |
| grudzień | grudnia |

**Critical: in long-form dates, month is in genitive** — `15 stycznia 2024` not `15 styczeń 2024`. Polish months are Slavic-rooted (like Czech, Croatian, Ukrainian).

**Weekdays (lowercase):** poniedziałek, wtorek, środa, czwartek, piątek, sobota, niedziela.

Week starts **Monday**.

### Time

- 24-hour preferred: `14:30` or `godz. 14:30` (godz. = godzina).
- 12-hour rarely used.

### Currency — Polish złoty (PLN / zł) — Poland did NOT adopt the euro

| Format | Pattern | Example |
|--------|---------|---------|
| Symbol after amount | `zł` | **99,99 zł** OR **1 234,56 zł** |
| ISO code | PLN | **99,99 PLN** |

**Critical: Poland is NOT in the eurozone.** Despite being an EU member, Poland retains the złoty and has no immediate plan to adopt the euro. NEVER use `€ / EUR` for Polish localization.

---

## Terminology — preferred Polish terms

| English | ✓ Polish preferred | ✗ Avoid |
|---------|---------------------|---------|
| user | **użytkownik** | user, juzer |
| account | konto | akkaunt |
| password | hasło | password |
| settings | **ustawienia** | settings |
| dashboard | panel sterowania / pulpit | dashboard |
| email | e-mail / poczta elektroniczna (formal) | mejl |
| link | link / odnośnik | — |
| website | strona internetowa / witryna | website |
| folder | **folder** / katalog | — |
| file | **plik** | fajl |
| device | urządzenie | device |
| phone | telefon / komórka (mobile) | — |
| computer | komputer | komputer (same — loanword integrated) |
| application / app | aplikacja | — |
| update (v.) | aktualizować / zaktualizować | apdejtować |
| save | zapisać / zapisywać | sejwować |
| delete | usunąć | deletować |
| upload | przesłać / wgrać | uploadować |
| download | pobrać | downloadować |
| sign in / log in | zalogować się | — |
| sign up | zarejestrować się | — |
| search | szukać / wyszukiwać | — |
| click | kliknąć | — |
| share | udostępnić | szerować |
| profile | profil | — |
| notifications | powiadomienia | — |
| privacy | prywatność | — |
| terms | warunki / regulamin | — |
| support | wsparcie / pomoc techniczna | support |
| help | pomoc | — |
| feedback | opinia / informacja zwrotna | feedback |
| menu | menu | — |
| home | strona główna | — |
| browser | przeglądarka | browser |
| screen | ekran | — |
| keyboard | klawiatura | — |
| mouse | mysz | — |
| build (software) | zbudować / utworzyć | budować (= construction) |
| deploy | wdrożyć / publikować | deployować |
| pipeline (CI/CD) | pipeline (keep) | — |
| commit (git) | commit (keep) / zatwierdzić | — |
| merge (git) | scalić / merge | — |
| repository | repozytorium | — |
| sync | synchronizacja / synchronizować | — |
| API | API (keep — Latin always) | — |
| endpoint | endpoint (keep) | — |
| token | token | — |
| cache | pamięć podręczna / cache | — |

### Tech identifiers — keep in Latin script

Inside Polish text (Latin alphabet anyway), these stay exactly as-is:
- Git, GitHub, Docker, npm, pip
- HTTP, REST, GraphQL, OAuth, JWT
- JSON, XML, YAML, CSV, PDF
- Brand names: Google, Microsoft, Apple, iPhone, Android
- Commands, paths, URLs, code, placeholders

---

## False Friends — Critical

| Polish word | Actually means | NOT this | Correct for the English |
|-------------|----------------|----------|--------------------------|
| **podniecony** | aroused (sexual) / excited (tense context) | "excited (looking forward)" | "excited" → **podekscytowany** / **z niecierpliwością czekam** |
| aktualny | current / topical | "actual" | "actual" → **rzeczywisty** / **prawdziwy** |
| realizować | to implement / carry out | "to realize (understand)" | "realize" → **uświadomić sobie** / **zrozumieć** |
| eventualnie | possibly / perhaps | "eventually" | "eventually" → **w końcu** / **ostatecznie** |
| kontrolować | to check / verify | "to control (manage)" | "control (manage)" → **zarządzać** / **sterować** |
| sympatyczny | likeable / pleasant | "sympathetic (compassionate)" | "sympathetic" → **współczujący** |
| rezultat | result | (OK in modern usage) | — |
| ordynarny | vulgar / common | "ordinary" | "ordinary" → **zwykły** / **zwyczajny** |
| garderoba | wardrobe | "garderobe" | — |

---

## Calque / Anti-Pattern List

| ✗ Calque | ✓ Native Polish | Reason |
|----------|------------------|--------|
| robić sens | **mieć sens** | "Makes sense" calque |
| na koniec dnia | **ostatecznie** / **w końcu** | "At the end of the day" calque |
| zająć miejsce | **odbyć się** / **mieć miejsce** | "Take place" calque (note: `mieć miejsce` is OK Polish though) |
| oparte na | **na podstawie** / **w oparciu o** | "Based on" calque |
| na dziennej bazie | **dziennie** / **codziennie** | "On a daily basis" calque |
| w terminach | **w kwestii** / **odnośnie** | "In terms of" calque |
| **Auto-wykryto** | **Wykryto automatycznie** | "Auto-X" — use full adverb |
| **Auto-zapis** | **Automatyczny zapis** | "Auto-X" |
| **Auto-uzupełnianie** | **Automatyczne uzupełnianie** / **autouzupełnianie** | "Auto-X" |
| **Przetłumaczone wyniki** (header) | **Wyniki tłumaczenia** | English Past-Participle + Noun → Polish Noun + Genitive of verbal noun |
| **Przesłane pliki** (header) | **Pliki do przesłania** | Same pattern for actionable context |
| **Wybrane opcje** (header) | **Wybór opcji** | Use noun form |
| **opcja języka** (N+N) | **opcje językowe** / **ustawienia języka** | Use adj+N or genitive |
| **projekt folder** | **folder projektu** / **folder projektowy** | Use genitive or adjective |
| **użytkownik ustawienia** | **ustawienia użytkownika** / **ustawienia użytkowników** | Use genitive |
| **dokonać poprawy** | **poprawić** / **ulepszyć** | Use direct verb |
| **udzielić odpowiedzi** | **odpowiedzieć** | Use direct verb |
| **per plik** | **za plik** | "per X" calque |
| **per użytkownik** | **na użytkownika** | "per X" |
| **AI-napędzany** | **oparty na AI** / **wykorzystujący AI** | "X-powered" calque |
| **Tłumaczenie nie powiodło się** | **Nie udało się przetłumaczyć** / **Błąd tłumaczenia** | Verbose → impersonal |
| **Plik został zapisany** (as status) | **Zapisano** | Personal passive → impersonal -no/-to |
| **Plik zapisał się** | **Zapisano** | Reflexive past → impersonal |
| **Stany Zjednoczone Ameryki** (UI) | **USA** | UI short form |

---

## Self-Check Checklist (Run Before Returning Output)

### Polish gender split (auto-fail on miss)

- [ ] **Plural verb/adjective agreement**: m-personal `-li`/`-i` for male humans (or mixed); non-m-personal `-ły`/`-e` for everything else.
- [ ] `Pliki zostały zapisane` ✓ (non-m-personal for "files") — NOT `Pliki zostali zapisani` ✗.
- [ ] `Użytkownicy zalogowali się` ✓ (m-personal for "users") — NOT `Użytkownicy zalogowały się` ✗.
- [ ] Mixed group containing male humans → m-personal.

### Accuracy

- [ ] **Diacritics intact** — `ą ć ę ł ń ó ś ź ż` never stripped. Especially `ł` (NOT `l`) and `ó` (NOT `o` or `u`).
- [ ] **Word integrity** — prefixes joined (`przetłumaczyć`, `wykonać`, `przenieść`, `pobrać`). Reflexive `się` separate (`zalogować się`).
- [ ] **Seven cases** correct, including **active vocative** for direct address (`Anno!`, `użytkowniku!`).
- [ ] **Animate masc. accusative = genitive** (`widzę użytkownika`).
- [ ] **Verb-governed case**: pomagać+DAT, zajmować się+INS, osiągnąć+GEN.
- [ ] **Relative pronoun agreement** (który/która/które/którzy).
- [ ] **ICU plurals**: `one / few / many / other` (1 / 2-4 ends in 2-4 / 0+5-20+ AND 11-14 AND 21,31… / fractions). Polish's `many` includes 11-14 AND 21+.
- [ ] **Numeral-noun**: 1=NOM.sg, 2-4 (ends 2-4)=NOM.pl, 5+ AND 11-14 AND 21+=GEN.pl.
- [ ] **Verb aspect** correct.
- [ ] **No stacked finite verbs** from English -ing — use `-ąc` participle or `przy + verbal noun`.
- [ ] **Placeholders preserved**.
- [ ] **Latin tech identifiers** intact.
- [ ] **Numbers**: comma decimal (3,14), space thousands (1 234), `zł` after amount.
- [ ] **Dates**: `15.01.2024` (digit form) or `15 stycznia 2024` (long form, month in **genitive**).
- [ ] **Time**: 24-hour, `godz. 14:30`.
- [ ] **per**: `za + ACC` for rate, `na + ACC` for distribution, `dziennie` for "per day".

### Register

- [ ] **Formality form chosen and applied consistently**:
  - Informal: `ty + 2nd-person verb`.
  - Formal: `Pan / Pani / Państwo + 3rd-person verb` (CAPITALIZED in direct address).
  - **NEVER use `Wy` as formal singular** (politically loaded calque from Russian).
- [ ] **`Pan / Pani / Państwo / Pana / Pani / Państwa` capitalized** in direct address.
- [ ] **Vocative used** when addressing user by name (`Aniu!`, `Krzysztofie!`, `użytkowniku!`).

### UI conventions

- [ ] Buttons use **perfective imperative** (`Zapisz`, `Usuń`, `Anuluj`).
- [ ] Reflexive `się` present where required (`zalogować się`, `zarejestrować się`).
- [ ] Status ongoing: **imperfective verbal noun** (`Zapisywanie…`) or `Trwa + noun` — NEVER first-person (`Zapisuję…` ✗).
- [ ] Status completed: **impersonal `-no/-to`** participle (`Zapisano`, `Przetłumaczono`), NOT personal past (`Plik się zapisał` ✗).
- [ ] Status failed: **`Nie udało się + infinitive`** OR **`Błąd + GEN`**.
- [ ] Empty state: `Brak + GEN` / `Nie znaleziono` with specific noun.
- [ ] File picker: `Wybierz`, not `Przeglądaj`.
- [ ] Drag-drop: `Przeciągnij` + `Upuść` (NOT `zrzuć`).
- [ ] Quantity: `ponad 25` / `więcej niż 25`, NOT `25+`.
- [ ] No comma before `i / oraz / lub / albo`.
- [ ] Comma before `że / który / aby / gdy / jeśli / ponieważ / ale`.
- [ ] Error messages include next step.

### Naturalness

- [ ] **No English calques** (`robić sens`, `na koniec dnia`, `oparte na`, `na dziennej bazie`).
- [ ] **Past-Participle + Noun headers** → **Noun + Genitive of verbal noun** (`Wyniki tłumaczenia`).
- [ ] **Auto-X prefix** → full adverb (`Wykryto automatycznie`) or compound (`autozapis`).
- [ ] **N+N compounds** → adj+N or genitive.
- [ ] **No verbose collocations** (`dokonać poprawy` → `poprawić`).
- [ ] **No false friends**: `podniecony ≠ excited (positive)`, `aktualny ≠ actual`, `realizować ≠ realize`, `eventualnie ≠ eventually`, `ordynarny ≠ ordinary`.
- [ ] **Polish months in genitive** in date prose (`15 stycznia 2024`).
- [ ] **`„…"`** Polish quotation marks (low-9/high-9), NOT English `"…"`.

### Currency / Region

- [ ] **PLN (zł) for Polish locale** — **NEVER EUR** (Poland did not adopt euro).

---

## Worked Example — Standard pl UI (informal ty)

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** neutral product UI → casual/informal ty (typical for consumer software), perfective imperative buttons.

**Translation:**

> Witaj ponownie! W Twoim koncie są 3 nowe pliki. Kliknij **Kontynuuj**, aby je sprawdzić, lub **Anuluj**, aby tu pozostać. Zapisywanie zmian…

**Why this works:**
- `Witaj ponownie` — informal singular imperative-greeting (or use `Witamy ponownie` for plural/inclusive).
- `W Twoim koncie` — `w` + LOC; `koncie` n. LOC sg.; `Twoim` — possessive (capitalized as direct address even in ty-form — Polish convention).
- `są 3 nowe pliki` — `pliki` is non-m-personal pl; `nowe` is non-m-personal pl. adjective; `są` is 3rd-pers. pl.
- `kliknij` — informal ty imperative.
- Buttons: `Kontynuuj`, `Anuluj` (perfective imperative).
- `aby je sprawdzić / aby tu pozostać` — `aby + infinitive` (purpose construction — correct Polish).
- Status: `Zapisywanie zmian…` — imperfective verbal noun (impersonal, NOT first-person `Zapisuję…`). `zmian` is GEN pl.
- No comma before `lub` ✓.
- Comma before `aby` ✓.

**Same string for FORMAL (Pan/Pani) register:**

> Witamy ponownie! W Pani/Pana koncie są 3 nowe pliki. Proszę kliknąć **Kontynuuj**, aby je sprawdzić, lub **Anuluj**, aby tu pozostać. Trwa zapisywanie zmian…

(`Pani/Pana` instead of `Twoim`; `Proszę kliknąć` instead of `kliknij`; `Trwa zapisywanie` more formal status.)

---

## Worked Example — Masculine-personal vs non-masculine-personal split

**Source:** 3 files were saved. 5 users logged in. 7 women joined.

**Translation:**

> **3 pliki zostały zapisane.** **5 użytkowników się zalogowało.** **7 kobiet dołączyło.**

Wait — let me redo with correct plural form:

> **Zapisano 3 pliki.** OR **3 pliki zostały zapisane.** (non-m-personal: pliki → zostały/zapisane with -e)
> **5 użytkowników zalogowało się.** (m-personal subject, but with "5" → GEN.pl noun + sg verb; for nominative: `Użytkownicy zalogowali się.`)
> **7 kobiet dołączyło.** (non-m-personal subject "7 women", with 5+ count takes GEN.pl + sg verb)

**Plural-form examples:**

| Subject | English | ✓ Polish |
|---------|---------|----------|
| Files were saved. | The files were saved. | **Pliki zostały zapisane.** (non-m-pers `-ły`/`-e`) |
| Users logged in. | The users logged in. | **Użytkownicy się zalogowali.** (m-pers `-li`) |
| Women logged in. | The women logged in. | **Użytkowniczki się zalogowały.** OR **Kobiety się zalogowały.** (non-m-pers `-ły`) |
| Systems are running. | The systems are running. | **Systemy działają.** (non-m-pers — neuter "działają" with non-m-pers subject `-e` for adj if needed) |
| Children are playing. | The children are playing. | **Dzieci się bawią.** (non-m-pers — "children" treated as non-m-personal in plural) |

---

## Worked Example — Vocative for direct address

**Source:** Hello, Anna! Welcome back, Krzysztof.

**✗ Wrong (Slovak/Russian-style nominative):**

> Cześć, Anna! Witaj ponownie, Krzysztof.

**✓ Correct (Polish vocative):**

> Cześć, Anno! Witaj ponownie, Krzysztofie.

Other vocative examples:
- Adam → Adamie
- Marek → Marku
- Tomek → Tomku
- Maria → Mario
- Ania → Aniu
- pan → panie (`Panie Nowak!`)
- pani → pani (vocative = nominative for fem.)
- użytkownik → użytkowniku

---

## Worked Example — ICU plurals (Polish four-category expansion)

**Source:**

```icu
You have {count, plural, one {# new message} other {# new messages}}.
```

**Translation (full Polish four-category expansion):**

```icu
Masz {count, plural,
  one {# nową wiadomość}
  few {# nowe wiadomości}
  many {# nowych wiadomości}
  other {# nowej wiadomości}
}.
```

Notes:
- `one` (1): `1 nową wiadomość` — f. ACC sg.
- `few` (2-4 not 12-14): `2 nowe wiadomości` — f. NOM pl.
- `many` (0, 5-20, 21+, 11-14): `5 nowych wiadomości` — f. GEN pl.
- `other` (fractions): `2,5 nowej wiadomości` — f. GEN sg.

**Critical**: Polish's `many` covers 11-14 AND 21+ (not `one` for 21). 5+ = GEN pl.

---

## Worked Example — Date with genitive month

**Source:** Last login: January 15, 2024 at 2:30 PM. Subscription: 99 PLN/month.

**Translation:**

> Ostatnie logowanie: 15 stycznia 2024 r. o godz. 14:30. Abonament: 99 zł miesięcznie.

Note: `stycznia` (genitive of `styczeń`). Polish dates use month in **genitive**. `r.` is `roku` (year, gen.). `zł` for złoty — NEVER euro.

---

## Worked Example — Status messages

| State | English | ✓ Polish |
|-------|---------|----------|
| Ongoing | Saving… | **Zapisywanie…** / **Trwa zapisywanie…** (NOT `Zapisuję…` first-person) |
| Completed | Saved | **Zapisano** (NOT `Plik został zapisany` verbose, NOT `Plik się zapisał` reflexive past) |
| Failed | Save failed | **Nie udało się zapisać** / **Błąd zapisywania** (NOT `Zapis się nie powiódł` verbose, NOT `Zapis nieudany` calque) |

---

## When in Doubt

1. **Default to pl, informal ty for consumer apps OR formal Pan/Pani for B2B/banking, perfective imperative buttons.**
2. **NEVER use `Wy` as singular formal pronoun** — Polish formal singular is `Pan/Pani + 3rd person verb`.
3. If `ł` was stripped to `l` (or `polski` → `polski` is fine, but `łańcuch` → `lancuch` ✗) → **restore `ł`**.
4. If `ó` was stripped/replaced → **restore `ó`** (`źródło` not `zrodlo`).
5. If `ś / ź / ć / ń / ą / ę / ż` were stripped → **restore all diacritics**.
6. If a verb prefix has a space (`prze tłumaczyć`) → **join it**: `przetłumaczyć`.
7. If `się` is attached to a verb (`zalogowaćsię`) → **separate it**: `zalogować się`.
8. If you used m-personal `-li` for non-m-personal subject (`Pliki zostali zapisani`) → **fix to `-ły`/`-e`**: `Pliki zostały zapisane`.
9. If you used non-m-personal for m-personal users (`Użytkownicy zalogowały się`) → **fix to `-li`**: `Użytkownicy zalogowali się`.
10. If you wrote `Plik został zapisany` as a status → **use impersonal `Zapisano`**.
11. If you wrote `Tłumaczenie się nie powiodło` → **use `Nie udało się przetłumaczyć`**.
12. If you used first-person status (`Zapisuję…`) → **switch to impersonal `Zapisywanie…` / `Trwa zapisywanie…`**.
13. If you addressed someone by name in nominative (`Anna!`) → **use vocative** (`Anno!`).
14. If a date is `15 styczeń 2024` → **fix month to genitive**: `15 stycznia 2024 r.`.
15. If you used `Auto-` prefix → **expand to `Automatycznie / Automatyczny`** or compound (`autozapis`).
16. If you used `per plik` → **fix to `za plik` / `na plik`**.
17. If currency is € / EUR → **fix to zł / PLN** (Poland is NOT in eurozone).
18. If `21 plik` → **fix to `21 plików`** (Polish 5+ AND 21+ AND 11-14 all use GEN.pl).
