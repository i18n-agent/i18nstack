---
name: localize-cs
description: Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Czech (cs). Czech is NOT Slovak — enforces Czech-specific vocabulary (soubor not súbor, uživatel not používateľ, složka not zložka, nastavení not nastavenia, prohlížeč not prehliadač), Czech letters ě ř ů, 7-case grammar (with vocative — unlike Slovak's 6), 3-gender system with masculine animate/inanimate split, ICU one/few/other plurals (1/2-4/0+5+ with 11-14 going to other), perfective/imperfective verb aspect, Vy/ty formality (Vy capitalized), clitic second-position rule, impersonal voice for status (Probíhá výpočet / Počítá se, NEVER first-person Počítám), neuter perfective participle for completion (Uloženo, Načteno), "Nepodařilo se" + infinitive for failure, infinitive buttons (Uložit), and CZK koruna currency (1 234,56 Kč — Czechia did NOT adopt euro).
---

# Translate to Czech (cs) — High-Fidelity Skill

## Scope & Variants

Czech is a single standard target — Modern Standard Czech (spisovná čeština). No regional split for product UI:

| Locale | Notes |
|--------|-------|
| `cs` / `cs-CZ` | Standard Czech (Czechia). Default and only target. |

**Note on "Czech Republic" vs "Czechia":** the country's official short name is now **Česko / Czechia** (adopted 2016). Use the short form in UI; reserve `Česká republika` for formal/legal contexts.

**Practical reality:** Czech translation has one target. The defining quality concern is **disambiguating from Slovak**, which is structurally similar but lexically distinct.

### Czech vs Slovak — distinct West Slavic languages, often confused

Czech and Slovak are mutually intelligible (especially in writing) but they are **separate languages** with distinct vocabulary, distinct alphabets, and distinct grammar in places. This skill is the mirror partner to `localize-sk`.

**Czech has 3 letters Slovak doesn't:**

| Czech | Used for | Slovak equivalent |
|-------|----------|-------------------|
| **ě** | /je/ or palatalizing previous consonant | not used (Slovak uses `e` or different forms) |
| **ř** | /rž/ (uniquely Czech phoneme) | not used (Slovak has plain `r`) |
| **ů** | long /u:/ (alternant of `ó` from morphological change) | uses `ú` instead |

**Slovak has 5 letters Czech doesn't:** `ľ ĺ ŕ ô ä`. Any of these appearing in Czech text means a Slovak word leaked in.

**Common Czech vs Slovak vocabulary** (the surface markers a translation must NOT mix):

| English | ✓ Czech | ✗ Slovak (do NOT use in cs) |
|---------|---------|-----------------------------|
| file | soubor | súbor |
| folder | složka | zložka / priečinok |
| user | uživatel | používateľ |
| settings | nastavení | nastavenia |
| browser | prohlížeč | prehliadač |
| but | ale | ale (same) |
| because | protože | pretože |
| yes | ano | áno (with diacritic) |
| no | ne | nie |
| month | měsíc | mesiac |
| Monday | pondělí | pondelok |
| Tuesday | úterý | utorok |
| only | jen / pouze | len / iba |
| also | také / taky | tiež / aj |
| can | moci / moct | môcť |
| want | chtít | chcieť |
| see | vidět | vidieť |
| do | dělat | robiť |
| big | velký | veľký |

**If a Czech translation contains `súbor`, `používateľ`, `nastavenia`, `prehliadač`, `áno`, `mesiac`, `pondelok`, `robiť`, `vidieť`, or any of the letters `ľ ĺ ŕ ô ä`** — IT'S WRONG (Slovak leaked in). Fix to the Czech equivalents.

---

## Register Auto-Detection (Apply Before Translating)

Czech has a strong T-V distinction (Vy/ty — called "vykání" vs "tykání"). Auto-detect from source:

| Source signal | Target register |
|---------------|-----------------|
| Casual / conversational / personal (`Hey!`, contractions, emoji, marketing voice, gaming, social) | **Informal (ty / tykání)** — `ty` lowercase, 2nd-person sg. verb endings (`-š`: můžeš, vidíš), familiar imperative (singular: vyber, klikni, otevři). |
| Neutral product UI / docs / consumer software (DEFAULT) | **Formal (Vy / vykání)** — `Vy` capitalized for direct address, 2nd-person pl. verb endings (`-te`: můžete, vidíte), polite imperative (`-te/-ete`: vyberte, klikněte, otevřete). Possessive `Váš/Vaše` capitalized. |
| Legal / banking / government / enterprise B2B | **Formal (Vy) elevated** — same `Vy` form but full constructions, no contractions, prefer impersonal reflexive (`Provádí se`), native vocabulary. |

**Hard rule: never mix levels in one text.** A string with `Vy můžete` (formal verb) and `tvoje nastavení` (informal possessive) is broken.

**Capitalization rule for Vy:** `Vy / Váš / Vaše / Vám / Vás` are capitalized in direct second-person address.

**Default for software UI: Vy (formal)** unless brand voice is explicitly youth/casual.

---

## Critical Hard Rules (Severity ≥ 2.0 — Auto-Fail If Wrong)

### 1. Czech identity — NOT Slovak (severity 2.5)

Documented above. Check for Slovak letters (`ľ ĺ ŕ ô ä`) and Slovak vocabulary.

### 2. Word integrity — verb prefixes NEVER split (severity 3.0)

Czech verbs with prefixes are **single words**. Splitting them is a critical error.

| ✗ Wrong (split) | ✓ Correct (joined) |
|-----------------|---------------------|
| `pře vést` | **`převést`** (to transfer) |
| `pro vést` | **`provést`** (to execute) |
| `vy konat` | **`vykonat`** (to perform) |
| `na hrát` | **`nahrát`** (to upload / record) |
| `pře nést` | **`přenést`** (to transfer) |
| `od eslat` | **`odeslat`** (to send out) |
| `při jmout` | **`přijmout`** (to accept) |
| `za hájit` | **`zahájit`** (to begin) |

**Reflexive `se / si` is SEPARATE clitic** — not attached to verb in writing. `přihlásit se`, `registrovat se`, `zabývat se`. Writing `přihlásitse` is wrong.

### 3. Czech diacritics — preserve all (severity 2.5)

Czech uses: `á č ď é ě í ň ó ř š ť ú ů ý ž`. Stripping any is a critical readability failure. Especially:
- **ě** (`mě`, `tě`, `pět`, `dělat`) — palatalizing e.
- **ř** (`říjen`, `řeka`, `řekl`) — uniquely Czech sound.
- **ů** (`dům`, `stůl`, `obrátit`) — long u with marker.

| ✗ Stripped | ✓ Correct |
|------------|-----------|
| uzivatel | **uživatel** |
| nastaveni | **nastavení** |
| prohlizec | **prohlížeč** |
| reka | **řeka** |
| dum | **dům** |

### 4. Seven-case system — Czech retains active vocative (severity 2.5)

Czech uses **all 7 Slavic cases**, INCLUDING the vocative (unlike Slovak which merged it into nominative). Every noun, adjective, and pronoun declines.

| Case | Question | Use | Example (m. anim. "uživatel") | Example (f. "aplikace") |
|------|----------|-----|-------------------------------|--------------------------|
| Nominativ (NOM) | kdo? co? | Subject | uživatel | aplikace |
| Genitiv (GEN) | koho? čeho? | Possession, "of", absence, 5+ count | uživatele | aplikace |
| Dativ (DAT) | komu? čemu? | Indirect object, "to" | uživateli | aplikaci |
| Akuzativ (ACC) | koho? co? | Direct object | uživatele (animate=GEN) / soubor (inanimate=NOM) | aplikaci |
| **Vokativ (VOC)** | — | **Direct address — ACTIVE in Czech** | uživateli! | aplikace! |
| Lokál (LOK) | o kom? čem? | Location (always w/ prep) | o uživateli | o aplikaci |
| Instrumentál (INS) | s kým? čím? | "With", means | s uživatelem | s aplikací |

**Critical: animate masculine accusative = genitive form.** `vidím uživatele`, NOT `vidím uživatel`.

**Vocative usage** — Czech ACTIVELY uses vocative for direct address (unlike Slovak/Russian where it's archaic/merged). When a Czech product UI greets the user by name or addresses a role:

| ✗ Wrong (nominative) | ✓ Correct (vocative) |
|----------------------|----------------------|
| Ahoj, Petr! | **Ahoj, Petře!** |
| Vážený uživatel! | **Vážený uživateli!** |
| Děkujeme, Pavel! | **Děkujeme, Pavle!** |
| Karel! | **Karle!** |

Common vocative endings: m.anim. `-e/-i` (Petr → Petře, Karel → Karle, učitel → učiteli), f. usually = nominative (Marie → Marie), n. = nominative.

### 5. Preposition + governed case (severity 2.5)

| Preposition | Case | Example |
|-------------|------|---------|
| v / ve (in) | LOK (location) | v systému |
| do (into) | GEN | do systému |
| na (on/onto) | LOK / ACC | na obrazovce / na obrazovku |
| s / se (with) | INS | s uživatelem |
| bez (without) | GEN | bez chyb |
| pro (for) | ACC | pro uživatele |
| od (from) | GEN | od uživatele |
| k / ke (to/toward) | DAT | k uživateli |
| o (about) | LOK | o uživateli |
| po (after) | LOK | po přihlášení |
| před (before) | INS / ACC | před uložením |
| za (per / behind) | ACC / INS | za soubor / za stolem |
| u (at, by) | GEN | u uživatele |
| z / ze (from) | GEN | z aplikace |

**"per" in Czech:** use `za + ACC` for rate (`za soubor`), `na + ACC` for distribution (`na uživatele`), `denně` for "per day". Never `per soubor` (English calque).

### 6. ICU plurals — one / few / other (1 / 2-4 / 0+5+ with 11-14 going to other) (severity 2.5)

```icu
{count, plural,
  one {# soubor}
  few {# soubory}
  other {# souborů}
}
```

**CLDR plural category boundaries:**

| Category | Rule | Examples | Noun form |
|----------|------|----------|-----------|
| `one` | n = 1 | 1 | **NOM singular** (soubor) |
| `few` | n ∈ {2, 3, 4} | 2, 3, 4 | **NOM plural** (soubory) |
| `other` | n = 0 OR n ≥ 5 OR fractions | 0, 5-100, 1.5, 11, 12, 13, 14 | **GEN plural** (souborů) |

**Note vs other Slavic:** Czech is **simpler than Russian/Ukrainian/Croatian/Slovak** here — only `one / few / other` (3 categories), no `many` category. 11-14 fall into `other`, NOT `few`.

### 7. Numeral-noun agreement (severity 2.0)

| Count | Pattern | Example |
|-------|---------|---------|
| 1 | NOM sg | 1 soubor |
| 2, 3, 4 | NOM pl | 2 soubory, 3 systémy |
| 5+ | GEN pl | 5 souborů, 10 uživatelů |
| 11-14 | GEN pl (same as other 5+) | 11 souborů, 12 systémů |
| 21 | NOM sg (back to "one") | 21 souborů — WAIT, actually Czech is different from Russian here |
| 22-24 | varies by interpretation — commonly NOM pl when "21 = 1+20" interpretation isn't applied | (Czech generally treats 21+ as `other` = gen.pl. in modern usage) |

**Modern Czech tends to use GEN pl for everything 5+** including 21, 22, etc., though strict prescriptive grammar sometimes calls for NOM sg with 21, 22 etc. For UI, GEN pl is the safer default for 5+.

### 8. Three-gender + masculine animate/inanimate (severity 2.0)

Czech distinguishes **masculine animate** vs **masculine inanimate** (matters for accusative case):

| Gender | Example | Adjective NOM sg. |
|--------|---------|-------------------|
| Masc. animate (humans, named animals) | uživatel, programátor | nový uživatel |
| Masc. inanimate (objects, abstracts) | soubor, systém, počítač | nový soubor |
| Feminine (-a ending mostly) | aplikace, složka, databáze | nová aplikace |
| Neuter (-o/-e/-í ending) | nastavení, okno, zařízení | nové nastavení |

Wrong gender adjective is auto-fail: `nová soubor` ✗, `nový aplikace` ✗, `nová nastavení` ✗.

### 9. Past-tense gender agreement (severity 1.5)

| Subject | L-participle | Example |
|---------|--------------|---------|
| m. sg. | -l | on pracoval |
| f. sg. | -la | ona pracovala |
| n. sg. | -lo | ono pracovalo |
| m. anim. pl. | -li | oni pracovali |
| f. pl. / m. inan. pl. | -ly | ony pracovaly / soubory se uložily |
| n. pl. | -la | okna se otevřela |

### 10. Clitic second-position rule (severity 2.0)

Czech clitics (`se`, `si`, `by`, `bych`, `bys`, `jsem`, `jsi`, `mi`, `ti`, `mu`, `jí`, `ho`, `tě`, etc.) MUST go in the **second position** of their clause (Wackernagel's law), same as other Slavic languages.

| ✗ Wrong | ✓ Correct |
|---------|-----------|
| `Se mi to nelíbí` | **`To se mi nelíbí`** |
| `Soubor se mu zobrazuje` | **`Soubor se mu zobrazuje`** ✓ — wait, this is correct because `se mu` cluster is in position 2. The issue would be: `Soubor mu se zobrazuje` ✗ → `Soubor se mu zobrazuje` ✓ (clitic order: refl. `se` after AUX, before DAT) — actually Czech clitic order is: AUX → DAT → ACC → SE. So `se mu` is wrong; correct is `mu se`. Let me revise: |
| `Soubor se mu zobrazuje` (if mu comes first lexically) | Actually `Soubor mu se zobrazuje` ← but in Czech `se` typically comes after dative? Let me use a clear example. |

**Clitic cluster order in Czech:**
1. AUX (`jsem / jsi / je / jsme / jste / jsou / bych / bys / by / bychom / byste`)
2. SE / SI (reflexive)
3. DAT (`mi / ti / mu / nám / vám / jim`)
4. ACC (`mě / tě / ho / nás / vás / je`)

Example: `Já bych se mu byl zeptal.` (AUX bych — SE se — DAT mu — past). For UI status messages this complex cluster is rare; the main rule is: **`se / si` stays in 2nd position of the clause**.

### 11. Verb aspect — perfective vs imperfective (severity 2.0)

Standard UI verb aspect pairs:

| Imperfective (process, ongoing) | Perfective (single completed event) | English |
|--------------------------------|--------------------------------------|---------|
| ukládat | uložit | save |
| mazat | smazat | delete |
| nahrávat | nahrát | upload / record |
| stahovat | stáhnout | download |
| otevírat | otevřít | open |
| zavírat | zavřít | close |
| vytvářet | vytvořit | create |
| upravovat | upravit | edit |
| měnit | změnit | change |
| posílat | poslat | send |
| psát | napsat | write |
| číst | přečíst | read |
| vybírat | vybrat | choose / select |
| překládat | přeložit | translate |
| přihlašovat se | přihlásit se | log in |

**UI patterns by aspect:**
- Buttons (single action) → **perfective infinitive**: `Uložit`, `Smazat`, `Poslat`, `Vybrat`. The Czech UI convention is INFINITIVE (not imperative).
- Ongoing status → **imperfective verbal noun** (`Ukládání…`, `Načítání…`) or **`Probíhá + verbal noun`**.
- Completed → **perfective neuter participle** (`Uloženo`, `Načteno`, `Přeloženo`).

### 12. Verb-construction integrity — no stacked finite verbs (severity 2.0)

English `-ing` (gerund as adverbial) MUST be rendered with **přechodník** (Czech verbal adverb in `-ouc/-íc/-e`) OR restructure with `při + verbal noun`. Note: the přechodník is somewhat literary/archaic in modern Czech — `při + verbal noun` is more common in product copy.

| ✗ Stacked finite | ✓ Restructured | English |
|------------------|-----------------|---------|
| `Strávil jsem 6 let stavěl jsem firmu` | **`Strávil jsem 6 let stavbou firmy`** OR **`Strávil jsem 6 let při budování firmy`** | I spent 6 years building the business |
| `Pracoval jsem dokud jsem psal zprávu` | **`Pracoval jsem při psaní zprávy`** | I worked while writing the report |

---

## Pronouns and Possessives

### Personal pronouns

| English | Czech | Notes |
|---------|-------|-------|
| I | já | |
| you (sg. informal) | ty | |
| you (sg./pl. formal — capitalize) | Vy | Always capitalized in direct address |
| you (pl. informal) | vy | lowercase when truly plural informal |
| he | on | |
| she | ona | |
| it | ono | |
| we | my | |
| they (m. anim.) | oni | |
| they (m. inan. / f.) | ony | |
| they (n.) | ona | |

### Possessive pronouns

| Person | m. sg. | f. sg. | n. sg. |
|--------|--------|--------|--------|
| můj (my) | můj | moje / má | moje / mé |
| tvůj (your sg.) | tvůj | tvoje / tvá | tvoje / tvé |
| **Váš (your formal — capitalize)** | **Váš** | **Vaše / Vaše** | **Vaše** |
| jeho (his — invariable) | jeho | jeho | jeho |
| její (her) | její | její | její |
| svůj (reflexive — own) | svůj | svoje / svá | svoje / své |
| náš (our) | náš | naše | naše |
| jejich (their — invariable) | jejich | jejich | jejich |

**Reflexive `svůj`** is required when possessor = subject of same clause.

---

## UI Conventions

### Buttons — INFINITIVE (the Czech UI convention)

Czech platform UIs (Windows CZ, Chrome CZ, macOS CZ) use **infinitive** for buttons — NOT imperative. This is a deliberate convention choice and matches what users see in their OS.

| English | ✓ Infinitive (button) | (Vy-imperative — for instruction prose) |
|---------|------------------------|------------------------------------------|
| Save | **Uložit** | Uložte |
| Cancel | **Zrušit** / **Storno** | Zrušte |
| Delete | **Smazat** / **Odstranit** | Smažte / Odstraňte |
| Send | **Odeslat** | Odešlete |
| Edit | **Upravit** | Upravte |
| Search | **Hledat** | Hledejte |
| Confirm | **Potvrdit** | Potvrďte |
| Continue | **Pokračovat** | Pokračujte |
| Submit | **Odeslat** | Odešlete |
| Sign in / Log in | **Přihlásit se** | Přihlaste se |
| Sign out | **Odhlásit se** | Odhlaste se |
| Sign up | **Zaregistrovat se** | Zaregistrujte se |
| Next | **Další** / **Pokračovat** | (same) |
| Back | **Zpět** | (same) |
| Done | **Hotovo** / **Dokončeno** | (same) |
| OK | **OK** / **Souhlasím** | (same) |
| Close | **Zavřít** | Zavřete |
| Upload | **Nahrát** | Nahrajte |
| Download | **Stáhnout** | Stáhněte |
| Refresh | **Aktualizovat** / **Obnovit** | Aktualizujte |
| Settings | **Nastavení** | (same) |
| Apply | **Použít** | Použijte |
| Reset | **Resetovat** / **Obnovit původní** | — |
| Select all | **Vybrat vše** | Vyberte vše |
| Deselect all | **Odznačit vše** / **Zrušit vše** | — |
| Add more | **Přidat další** (NOT `Přidat více`) | Přidejte další |

**For action instructions in prose**, use Vy-imperative: `Klikněte pro pokračování`, `Zadejte heslo`.

### Status messages — three distinct patterns

**Ongoing (in-flight)** → **imperfective verbal noun** OR **`Probíhá` + verbal noun** (NEVER first-person)

| English | ✓ Czech |
|---------|---------|
| Loading… | **Načítání…** / **Probíhá načítání…** |
| Saving… | **Ukládání…** / **Probíhá ukládání…** |
| Sending… | **Odesílání…** / **Probíhá odesílání…** |
| Processing… | **Zpracovává se…** / **Probíhá zpracování…** |
| Connecting… | **Připojování…** |
| Searching… | **Hledání…** / **Probíhá vyhledávání…** |
| Translating… | **Překládání…** / **Probíhá překlad…** |
| Please wait | **Počkejte, prosím** / **Prosím, počkejte** |

**Critical impersonal voice rule:** NEVER first-person (`Počítám…`, `Analyzuji…`, `Zpracovávám…`) — sounds awkward. Always impersonal.

**Completed** → **Neuter perfective participle (`-no/-to`)** — impersonal

| English | ✓ Czech |
|---------|---------|
| Saved | **Uloženo** |
| Done | **Hotovo** / **Dokončeno** |
| Translation complete | **Přeloženo** / **Překlad dokončen** |
| File uploaded | **Soubor nahrán** / **Nahráno** |
| Sent | **Odesláno** |
| Payment successful | **Platba úspěšná** / **Zaplaceno** |

**Failed** → **`Nepodařilo se` + infinitive** OR **`Chyba` + GEN of verbal noun**

| English | ✓ Czech |
|---------|---------|
| Save failed | **Nepodařilo se uložit** / **Chyba ukládání** |
| Upload failed | **Nepodařilo se nahrát** / **Chyba nahrávání** |
| Translation failed | **Nepodařilo se přeložit** / **Chyba překladu** |
| Connection failed | **Nepodařilo se připojit** / **Chyba připojení** |
| File not found | **Soubor nebyl nalezen** |

NEVER use:
- ✗ `Překlad selhal` (too slangy)
- ✗ `Uložení neúspěšné` (calque)

### Empty states — `Žádné X` / `Nic nenalezeno`

| ✗ Verbose | ✓ Concise |
|-----------|-----------|
| Nebyly nalezeny žádné výsledky | **Žádné výsledky** |
| Zatím tu nemáte žádné projekty | **Zatím žádné projekty** |
| Nebyly nalezeny žádné soubory | **Žádné odpovídající soubory** |

### Drag-and-drop

- drag → **přetáhněte** (Vy) / **přetáhni** (ty)
- drop → **pusťte** (Vy) / **pusť** (ty) — NOT `uvolněte` (= liberate)
- Combined: **`Přetáhněte soubory sem`** (Drag files here) / **`Pusťte pro nahrání`** (Release to upload).

### File picker — `Vybrat` not `Procházet`

Standard in Chrome CZ / Windows CZ:

| ✗ Older / navigation | ✓ Modern / action-oriented |
|----------------------|----------------------------|
| Procházet soubory | **Vybrat soubory** |
| Procházet soubor | **Vybrat soubor** |
| klikněte pro procházení | **klikněte pro výběr** |

### Quantity expressions

| ✗ Calque | ✓ Native |
|----------|----------|
| 25+ jazyků | **více než 25 jazyků** |
| +{count} dalších | **a dalších {count}** / **dalších {count}** |

`Přidat více` ✗ (literal "add more") → `Přidat další` ✓ (idiomatic).

### Error messages — what + next step

| ✗ Bare | ✓ With next step |
|--------|------------------|
| Soubor nebyl nalezen. | **Soubor nebyl nalezen. Zkontrolujte cestu.** |
| Chyba sítě. | **Chyba sítě. Zkuste to znovu.** |
| Neplatný e-mail. | **E-mailová adresa je neplatná. Zkontrolujte formát.** |

**No comma before `nebo`** in Czech: `Zkuste to znovu nebo kontaktujte podporu.` ✓.

---

## Punctuation, Numbers, Dates, Currency

### Punctuation

| Mark | Czech | Notes |
|------|-------|-------|
| Question mark | `?` | Same as English |
| Comma | `,` | Different conjunction rules |
| Period | `.` | Same |
| Colon | `:` | Same |
| Quotation marks | **`„…"`** (low-9 / high-9) primary, **`‚…'`** nested | Same as German style |
| Em-dash | `—` | Used for parenthetical breaks |

### Comma rules

| Rule | Example |
|------|---------|
| **NO comma** before `a` (and) | Vyberte soubor **a** klikněte. |
| **NO comma** before `i` (also, archaic) | — |
| **NO comma** before `nebo / či` (or) | Vyberte soubor **nebo** složku. |
| **NO comma** before `ani` (nor) | Není to chyba **ani** problém. |
| **Comma** before `že` (that, subordinating) | Vidím, **že** soubor je otevřený. |
| **Comma** before `který / která / které` (relative) | Soubor, **který** jste vybrali… |
| **Comma** before `aby` (in order to) | Klikněte, **abyste** pokračovali. |
| **Comma** before `kdyby` (if conditional) | Uložte, **kdybyste** chtěli. |
| **Comma** before `protože` (because) | Zrušeno, **protože** selhalo. |
| **Comma** before `ale` (but) | Rychle, **ale** efektivně. |

### Numbers

| Format | Pattern | Example |
|--------|---------|---------|
| Thousands separator | **space** | 1 234 567 |
| Decimal separator | **comma (,)** | 3,14 / 99,99 |
| Negative | `-25` | |
| Percent | `25 %` (with space, official) or `25%` (common in UI) | |

**Critical:** Czech uses **space for thousands, comma for decimal** — opposite of English.

### Dates

| Format | Example | Use |
|--------|---------|-----|
| D. M. YYYY | **15. 1. 2024** | Default — spaces around periods |
| D. měsíc YYYY | **15. ledna 2024** | Long-form prose (month in genitive!) |
| YYYY-MM-DD | 2024-01-15 | Technical/API only |

**Czech month names (lowercase, declines — Slavic-rooted like Croatian!):**

| Nominative | Genitive (used in dates) |
|------------|---------------------------|
| leden | ledna |
| únor | února |
| březen | března |
| duben | dubna |
| květen | května |
| červen | června |
| červenec | července |
| srpen | srpna |
| září | září (indeclinable) |
| říjen | října |
| listopad | listopadu |
| prosinec | prosince |

**Critical: in long-form dates, month is in genitive** — `15. ledna 2024` not `15. leden 2024`. Czech is one of the few Slavic languages with native Slavic-rooted month names (alongside Croatian, Polish, Ukrainian, Belarusian).

**Weekdays (lowercase):** pondělí, úterý, středa, čtvrtek, pátek, sobota, neděle.

Week starts **Monday**.

### Time

- 24-hour preferred: `14:30` or `14.30` (period acceptable).
- 12-hour rarely used.

### Currency — Czech koruna (CZK / Kč) — Czechia did NOT adopt the euro

| Format | Pattern | Example |
|--------|---------|---------|
| Symbol after amount | `Kč` | **99,99 Kč** OR **1 234,56 Kč** |
| ISO code | CZK | **99,99 CZK** |

**Critical: Czechia is NOT in the eurozone.** Despite being an EU member, Czechia retains the koruna and has no formal plan to adopt the euro. NEVER use `€ / EUR` for Czech localization (would be a critical error for any pricing/payment UI).

---

## Terminology — preferred Czech terms

| English | ✓ Czech preferred | ✗ Avoid |
|---------|--------------------|---------|
| user | **uživatel** | user, používateľ (Slovak) |
| account | účet | akaunt |
| password | heslo | password |
| settings | **nastavení** | nastavenia (Slovak) |
| dashboard | přehled / hlavní panel | dashboard |
| email | e-mail | mejl |
| link | odkaz | link |
| website | webová stránka / web | website |
| folder | **složka** | folder, zložka (Slovak), priečinok (Slovak) |
| file | **soubor** | súbor (Slovak), fajl |
| device | zařízení | device |
| phone | telefon / mobil | — |
| computer | počítač | komputer |
| application / app | aplikace | — |
| update (v.) | aktualizovat | apdejtovat |
| save | uložit | sejvovat |
| delete | smazat / odstranit | deletovat |
| upload | **nahrát** | uploadovat |
| download | **stáhnout** | downloadovat |
| sign in / log in | přihlásit se | logovat se |
| sign up | zaregistrovat se | — |
| search | hledat | search |
| click | kliknout | — |
| share | sdílet | šerovat |
| profile | profil | — |
| notifications | upozornění / notifikace | — |
| privacy | soukromí | — |
| terms | podmínky | — |
| support | podpora | — |
| help | nápověda | — |
| feedback | zpětná vazba | — |
| menu | menu / nabídka | — |
| home | domů / domovská stránka | — |
| **browser** | **prohlížeč** | browser, prehliadač (Slovak) |
| **screen** | obrazovka | — |
| **keyboard** | klávesnice | tastatura (Slovak) |
| **mouse** | myš | — |
| build (software) | sestavit / vytvořit | — |
| deploy | nasadit / publikovat | deployovat |
| pipeline (CI/CD) | pipeline (keep) | — |
| commit (git) | commit (keep) / uložit změny | — |
| merge (git) | sloučit / merge | — |
| repository | repozitář | — |
| sync | synchronizovat | — |
| API | API (keep — Latin always) | — |
| endpoint | endpoint (keep) | — |
| cache | mezipaměť / cache | — |
| token | token | — |

### Tech identifiers — keep in Latin script

Inside Czech text (Latin alphabet anyway), these stay exactly as-is:
- Git, GitHub, GitLab, Docker, npm, pip
- HTTP, REST, GraphQL, OAuth, JWT
- JSON, XML, YAML, CSV, PDF
- Brand names: Google, Microsoft, Apple, iPhone, Android
- Commands, paths, URLs, code snippets
- Placeholders `{variableName}`, `{{count}}`, `<tag>`

---

## False Friends — Critical

| Czech word | Actually means | NOT this | Correct for the English |
|------------|----------------|----------|--------------------------|
| **vzrušený** | aroused (sexual) / excited (tense context) | "excited (looking forward)" | "excited" → **těším se** / **nadšený** |
| aktuální | current / topical | "actual" | "actual" → **skutečný** |
| realizovat | to implement / carry out | "to realize (understand)" | "realize" → **uvědomit si** |
| eventuálně | possibly / perhaps | "eventually" | "eventually" → **nakonec** |
| kontrolovat | to check / verify | "to control (manage)" | "control" → **ovládat** / **řídit** |
| sympatický | likeable / pleasant | "sympathetic (compassionate)" | "sympathetic" → **soucitný** |

---

## Calque / Anti-Pattern List

| ✗ Calque | ✓ Native Czech | Reason |
|----------|------------------|--------|
| dělat smysl | **dávat smysl** / **mít smysl** | "Makes sense" calque |
| na konci dne | **nakonec** / **v konečném důsledku** | "At the end of the day" calque |
| vzít místo | **konat se** / **proběhnout** | "Take place" calque |
| založeno na | **na základě** | "Based on" calque |
| na denní bázi | **denně** / **každý den** | "On a daily basis" calque |
| v termínech | **pokud jde o** / **ohledně** | "In terms of" calque |
| **Auto-detekováno** | **Automaticky detekováno** | "Auto-X" — use full adverb |
| **Auto-uložení** | **Automatické uložení** / **autouložení** | "Auto-X" |
| **Auto-doplnění** | **Automatické doplnění** / **autodoplnění** | "Auto-X" |
| **Přeložené výsledky** (header) | **Výsledky překladu** | English Past-Participle + Noun → Czech Noun + Genitive of verbal noun |
| **Nahrané soubory** (header) | **Soubory k nahrání** | Same pattern for actionable context |
| **Vybrané možnosti** (header) | **Výběr možností** | Use noun form |
| **volba jazyka** (N+N) | **jazykové možnosti** / **nastavení jazyka** | Use adj+N or genitive |
| **projekt složka** | **složka projektu** / **projektová složka** | Use genitive or adjective |
| **uživatel nastavení** | **uživatelské nastavení** / **nastavení uživatele** | Use adj or genitive |
| **preference tónu** | **preferovaný tón** / **volba tónu** | Anglicism noun → native adj |
| **provést vylepšení** | **vylepšit** | Use direct verb |
| **poskytnout odpověď** | **odpovědět** | Use direct verb |
| **AI-poháněný** | **založený na AI** / **s využitím AI** | "X-powered" calque |
| **datově-orientovaný** | **založený na datech** / **datově řízený** | "X-driven" calque |
| **per soubor** | **za soubor** | "per X" calque |
| **per uživatel** | **na uživatele** | "per X" calque |
| **Spojené státy americké** (UI) | **USA** | UI short form |
| **Spojené království Velké Británie** | **Velká Británie** / **UK** | UI short form |
| **Překlad selhal** | **Nepodařilo se přeložit** / **Chyba překladu** | Slangy → impersonal failure |
| **Uložení neúspěšné** | **Nepodařilo se uložit** / **Chyba ukladání** | Calque → impersonal |
| **Soubor se uložil** | **Uloženo** / **Soubor uložen** | Reflexive past → impersonal participle |
| **Přidat více** | **Přidat další** | "Add more" — use idiomatic `další` |
| **Rychlý překlad. Bezpečný. Spolehlivý.** | **Rychlé, bezpečné a spolehlivé překlady** | Telegram fragments → complete noun phrase |

---

## Self-Check Checklist (Run Before Returning Output)

### Czech identity (auto-fail on miss)

- [ ] **No Slovak letters**: no `ľ ĺ ŕ ô ä` in the text.
- [ ] **No Slovak vocabulary**: no `súbor / používateľ / nastavenia / prehliadač / pretože / mesiac / pondelok / robiť / vidieť / áno / nie`.
- [ ] **Czech letters present**: `ě ř ů` appear where required (`měsíc`, `říjen`, `dům`, `pět`).

### Accuracy

- [ ] **Word integrity** — prefixes joined (`převést`, `vykonat`, `nahrát`, `přijmout`). Reflexive `se/si` separate.
- [ ] **Diacritics intact** — `á č ď é ě í ň ó ř š ť ú ů ý ž` never stripped.
- [ ] **Gender agreement** + masc. animate/inanimate distinction.
- [ ] **Seven cases** correct, including **active vocative** for direct address (`Petře!`, `uživateli!`).
- [ ] **Animate masc. accusative = genitive** (`vidím uživatele`).
- [ ] **Verb-governed case**: pomáhat+DAT, zabývat se+INS, dosáhnout+GEN.
- [ ] **Relative pronoun agreement** (který/která/které/kteří).
- [ ] **ICU plurals**: `one / few / other` (1 / 2-4 / 0+5+). Note: NO `many` category. 11-14 use `other`.
- [ ] **Numeral-noun**: 1=NOM.sg, 2-4=NOM.pl, 5+=GEN.pl.
- [ ] **Verb aspect** correct.
- [ ] **Past-tense gender agreement** on L-participle.
- [ ] **Clitic second position** (`se / si` in 2nd slot of clause).
- [ ] **No stacked finite verbs** from English -ing — use `při + verbal noun`.
- [ ] **Placeholders preserved**.
- [ ] **Latin tech identifiers** intact.
- [ ] **Numbers**: comma decimal (3,14), space thousands (1 234), `Kč` after amount.
- [ ] **Dates**: `15. 1. 2024` (with spaces!) or `15. ledna 2024` (month in **genitive**).
- [ ] **Time**: 24-hour.
- [ ] **per**: `za + ACC` for rate, `na + ACC` for distribution.

### Register

- [ ] **Vy/ty chosen and applied consistently**.
- [ ] **`Vy/Váš/Vaše` capitalized** in direct address.
- [ ] **Vocative used** when addressing user by name in greetings/direct address.

### UI conventions

- [ ] Buttons use **INFINITIVE** (`Uložit`, `Smazat`, `Zrušit`), the Czech platform convention.
- [ ] Reflexive `se` present where required (`přihlásit se`, `zaregistrovat se`).
- [ ] Status ongoing: **imperfective verbal noun** (`Ukládání…`) or `Probíhá + noun` — NEVER first-person (`Počítám…` ✗).
- [ ] Status completed: **neuter perfective participle** (`Uloženo`, `Přeloženo`), NOT reflexive past (`Soubor se uložil` ✗).
- [ ] Status failed: **`Nepodařilo se + infinitive`** OR **`Chyba + GEN`**, never `selhal` (slangy) or `neúspěšné` (calque).
- [ ] Empty state: `Žádné + GEN` / `Nic nenalezeno` with specific noun.
- [ ] File picker: `Vybrat`, not `Procházet`.
- [ ] Drag-drop: `Přetáhněte` + `Pusťte` (NOT `uvolněte`).
- [ ] Quantity: `více než 25`, `dalších {count}`, NOT `25+`, `+{count}`.
- [ ] No comma before `nebo / a / či`.
- [ ] Error messages include next step.

### Naturalness

- [ ] **No English calques** (`dělat smysl`, `na konci dne`, `vzít místo`, `na denní bázi`, `založeno na`).
- [ ] **Past-Participle + Noun headers** → **Noun + Genitive of verbal noun** (`Výsledky překladu`).
- [ ] **Auto-X prefix** → full adverb (`Automaticky detekováno`).
- [ ] **N+N compounds** → adj+N or genitive (`uživatelské nastavení`).
- [ ] **No verbose collocations** (`provést vylepšení` → `vylepšit`).
- [ ] **No false friends**: `vzrušený ≠ excited (positive)`, `aktuální ≠ actual`, `realizovat ≠ realize`, `kontrolovat ≠ control (manage)`, `eventuálně ≠ eventually`.
- [ ] **Czech months in genitive** in date prose (`15. ledna 2024`).
- [ ] **`„…"`** Czech quotation marks (low-9/high-9), NOT English `"…"`.
- [ ] **No accidental Slovak forms**.

### Currency / Region

- [ ] **CZK (Kč)** for Czech locale — **NEVER EUR** (Czechia did not adopt euro).

---

## Worked Example — Standard cs formal UI

**Source (neutral product UI):**

> Welcome back! You have 3 new files in your account. Click **Continue** to review them or **Cancel** to stay here. Saving your changes…

**Register check:** neutral product UI → **Vy (formal)**, infinitive buttons.

**Translation:**

> Vítejte zpět! Ve svém účtu máte 3 nové soubory. Klikněte na **Pokračovat**, abyste si je prohlédli, nebo na **Zrušit**, abyste zůstali zde. Probíhá ukládání Vašich změn…

**Why this works:**
- `Vítejte zpět` — Vy-form greeting (formal plural participle).
- `Ve svém účtu` — `ve` + LOK; `účtu` masc. inan. LOK sg.; `svém` reflexive possessive.
- `máte 3 nové soubory` — Vy-form verb; `3` triggers `few` (NOM pl); `soubor` is m. inan.; `nové` is m. inan. pl. adjective.
- Buttons: `Pokračovat`, `Zrušit` (infinitive — Czech platform convention).
- `abyste si je prohlédli / abyste zůstali` — `aby + past tense (conditional)` construction — correct Czech (NOT `aby prohlížíte`).
- Status: `Probíhá ukládání Vašich změn…` — `Probíhá + verbal noun` (impersonal — not first-person `Ukládám…`). `Vašich změn` is gen. pl., agreeing with `Vašich` capitalized formal possessive.
- No comma before `nebo` ✓.
- Comma before `abyste` ✓.
- No Slovak vocabulary.

---

## Worked Example — Vocative for direct address

**Source:** Hi, Pavel! Welcome back, Karel.

**✗ Wrong (Slovak/Russian-style nominative):**

> Ahoj, Pavel! Vítejte zpět, Karel.

**✓ Correct (Czech vocative):**

> Ahoj, Pavle! Vítejte zpět, Karle.

Other vocative examples:
- Petr → Petře
- Marek → Marku
- Tomáš → Tomáši
- pan učitel → pane učiteli
- pán → pane
- (Marie → Marie, fem. usually same as nom.)

---

## Worked Example — ICU plurals

**Source:**

```icu
You have {count, plural, one {# new message} other {# new messages}}.
```

**Translation (full Czech three-category expansion):**

```icu
Máte {count, plural,
  one {# novou zprávu}
  few {# nové zprávy}
  other {# nových zpráv}
}.
```

Notes:
- `one`: `1 novou zprávu` — f. ACC sg.
- `few` (2-4): `2 nové zprávy` — f. NOM pl.
- `other` (0, 5+, 11-14, fractions): `5 nových zpráv` — f. GEN pl.

(No `many` category in Czech.)

---

## Worked Example — Date with genitive month

**Source:** Last login: January 15, 2024 at 2:30 PM. Subscription: 99 CZK/month.

**Translation:**

> Poslední přihlášení: 15. ledna 2024 v 14:30. Předplatné: 99 Kč měsíčně.

Note: `ledna` (genitive of `leden`). Czech dates use month in **genitive**, like Croatian/Slovak. `Kč` Czech koruna with NO euro (Czechia did not adopt euro).

---

## Worked Example — Status messages

| State | English | ✓ Czech |
|-------|---------|---------|
| Ongoing | Saving… | **Ukládání…** / **Probíhá ukládání…** (NOT `Ukládám…` first-person) |
| Completed | Saved | **Uloženo** (NOT `Soubor se uložil` reflexive past) |
| Failed | Save failed | **Nepodařilo se uložit** / **Chyba ukladání** (NOT `Uložení selhalo` slangy or `Uložení neúspěšné` calque) |

---

## When in Doubt

1. **Default to cs, Vy (formal), Czech identity (NOT Slovak), infinitive buttons.**
2. If you see Slovak letters (`ľ ĺ ŕ ô ä`) → **strip and convert** to Czech forms.
3. If you see Slovak vocabulary (`súbor`, `používateľ`, `nastavenia`, `prehliadač`) → **fix to Czech** (`soubor`, `uživatel`, `nastavení`, `prohlížeč`).
4. If a verb prefix has a space (`pře vést`) → **join it**: `převést`.
5. If `se` is attached to a verb (`přihlásitse`) → **separate it**: `přihlásit se`.
6. If you used `vzrušený` for "excited" → **fix to `těším se` / `nadšený`**.
7. If you wrote `Soubor se uložil` → **use impersonal `Uloženo`**.
8. If you wrote `Překlad selhal` → **use `Nepodařilo se přeložit` / `Chyba překladu`**.
9. If you used first-person status (`Počítám…`) → **switch to impersonal `Probíhá výpočet…` / `Počítá se…`**.
10. If you used `per soubor` → **fix to `za soubor` / `na soubor`**.
11. If you addressed someone by name in nominative (`Pavel!`) → **use vocative** (`Pavle!`).
12. If a date is `15. leden 2024` → **fix month to genitive**: `15. ledna 2024`.
13. If you used `Auto-` prefix → **expand to `Automaticky`** (adverb) or `Automatické` (adjective).
14. If currency is € / EUR → **fix to Kč / CZK** (Czechia is NOT in eurozone).
