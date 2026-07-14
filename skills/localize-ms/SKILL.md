---
name: localize-ms
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Malaysian / Malay (Bahasa Melayu / Bahasa Malaysia) for Malaysia, Brunei, and Singapore Malay speakers. CRITICAL — Malaysian is NOT Indonesian. Despite ~85% lexical overlap, the two have systematically different tech vocabulary (muat naik NOT unggah, muat turun NOT unduh, tetapan NOT pengaturan, kemas kini NOT perbarui, tetingkap NOT jendela, mesej NOT pesan, padam NOT hapus, tampal NOT tempel, fail NOT file/berkas, semak imbas NOT jelajahi/telusuri for file browsing — and \"melayari\" means WEB-surf, NOT file-browse), different number formats (Malaysian uses 1,234.56 Anglo/English-style — comma thousands, period decimal — NOT Indonesian European-style), different currency (RM Ringgit NOT Rp Rupiah), different day names (Isnin/Khamis/Jumaat/Ahad NOT Senin/Kamis/Jumat/Minggu), and only 3 times-of-day (pagi/petang/malam — NO siang/sore distinction). DANGEROUS FALSE FRIENDS with Indonesian: \"butuh\" is vulgar/genitalia (use \"perlu\"), \"pusing\" means to spin/turn (NOT dizzy — use \"pening\"), \"punggung\" means buttocks (NOT back — use \"belakang\"), \"sulit\" means confidential (NOT difficult — use \"susah\"). Other features: extensive affix system (me-/di-/ber-/-kan/-i), nasal assimilation, MANDATORY -kan suffix for transitive verbs, MANDATORY me- prefix after \"untuk\", reduplication for plurality without numbers but NOT with numbers, Anda/awak formality with \"Sila\" for politeness, manner adverbs AFTER verb, formal bahasa baku vocabulary preference over slang (tidak NOT tak, hendak NOT nak, sahaja NOT je, sudah NOT dah, di/pada NOT kat, ini/itu NOT ni/tu, sedikit NOT sikit, seperti NOT macam, kerana NOT sebab), Islamic/multiracial cultural sensitivity, and the file-browse vs web-surf terminology split (semak imbas for files, melayari for web)."
---

# Localize: Malaysian / Malay (ms → Bahasa Melayu)

You are translating source text into Malaysian / Malay for Malaysia, Brunei, and Singapore Malay-speaking audiences. This skill captures grammar, register, UI conventions, formatting, and Malaysian-specific failure modes — with critical disambiguation from its sister language Indonesian (Bahasa Indonesia / id).

## Scope & Variants

**Primary standards:**
- **ms-MY** — Bahasa Melayu / Bahasa Malaysia as used in Malaysia. Official language of Malaysia.
- **ms-BN** — Malay as used in Brunei. Closely follows Malaysian standard with minor differences.
- **ms-SG** — Malay as a co-official language of Singapore. Also closely follows Malaysian standard.

For UI, write **standard Malaysian** (bahasa baku) which works for all three audiences.

**Native names:**
- **Bahasa Melayu** — the language (older / general / pan-Malay name)
- **Bahasa Malaysia** — the language as defined by Malaysia (post-1969, emphasizes national identity)

In modern Malaysian usage, both terms are interchangeable in practice. Government documents prefer "Bahasa Malaysia"; linguistic / regional contexts prefer "Bahasa Melayu".

## Identity Guardrail — NOT Indonesian (CRITICAL)

**Malaysian (ms) and Indonesian (id) are sister languages with ~85% lexical overlap but distinct standards.** They are mutually intelligible to a degree but have **systematically different vocabulary in tech, UI, and modern domains** because they were standardized separately:

- **Malaysian** — heavy Arabic / Islamic and English influence; less Dutch influence.
- **Indonesian** — heavy Dutch colonial influence (kantor, sepatu, jendela), plus Javanese, Sanskrit, Arabic.

**Mixing the two is a quality failure**, especially in tech UI. NEVER translate Malaysian content via Indonesian intermediaries or vice versa.

### Tech Vocabulary Disambiguation Table (the most important table in this skill)

| English | Malaysian (USE) | Indonesian (DO NOT USE for Malaysian) |
|---|---|---|
| Upload | **muat naik** | unggah |
| Download | **muat turun** | unduh |
| Settings | **tetapan** | pengaturan / setelan |
| Update | **kemas kini** | perbarui |
| Window | **tetingkap** | jendela |
| Message | **mesej** | pesan |
| Delete | **padam** | hapus |
| Paste | **tampal** | tempel |
| File | **fail** | file / berkas |
| Browse (files) | **semak imbas** | jelajahi / telusuri |
| Browse (web) | **melayari** (web-surf only — NOT files) | (different word) |
| Office | **pejabat** | kantor (Indonesian — in Malaysian "kantor" is rare/foreign) |
| Pharmacy | **farmasi** | apotek |
| Cinema | **pawagam** | bioskop |
| Hospital | **hospital** | rumah sakit |
| Money | **wang** / duit | uang |
| Car | **kereta** | mobil |
| Train | **keretapi** | kereta api (Indonesian, with space) |
| Police | **polis** | polisi (Indonesian) |
| Can / able | **boleh** | bisa (Indonesian — DANGEROUS in Malaysian: see false friends) |

### File Browse vs Web Surf — A Critical Malaysian Distinction (severity 1.5)

Malaysian has **TWO distinct words** for English "browse":

| Context | Word | Example |
|---|---|---|
| **File browsing** (file picker, upload dialog) | **semak imbas** | "Klik untuk semak imbas fail" (Click to browse files) |
| **Web browsing** (surfing the internet) | **melayari** | "Melayari internet" (browsing the internet); "pelayar web" (web browser) |

- ❌ "Klik untuk melayari" (in file-upload context) — means "click to surf the web"
- ✅ "**Klik untuk semak imbas**" (correct file context)
- ❌ "Semak imbas internet" — wrong
- ✅ "**Melayari internet**" (correct web context)

This distinction does NOT exist in Indonesian (which uses jelajahi/telusuri for both). Malaysian translators get this wrong constantly.

### DANGEROUS False Friends with Indonesian (severity 2.5)

**These words exist in BOTH languages but mean different things.** Using the Indonesian sense in Malaysian text is a serious error.

| Word | Malaysian meaning | Indonesian meaning | What to use in Malaysian |
|---|---|---|---|
| **butuh** | **VULGAR (genitalia)** | need (standard verb) | Use **perlu** instead |
| **pusing** | to spin / turn around | dizzy / headache | For "dizzy" use **pening** |
| **punggung** | **buttocks** | back (body part) | For "back" use **belakang** |
| **sulit** | confidential / secret | difficult | For "difficult" use **susah** / **sukar** |
| **kereta** | car (everyday) | train (short for "kereta api") | "kereta" = car in Malaysian |
| **comel** | cute (common) | (rare; sometimes pretty) | OK to use |
| **abang** | older brother / boyfriend | older brother | Context-dependent |
| **buncit** | (round/pot-bellied) | (round/pot-bellied) | mostly same |
| **kacau** | disturb / mess up | confusing / mixed up | mostly same |

**Critical takeaway:** NEVER use `butuh` in Malaysian text — it's vulgar. Use `perlu` (need) or `memerlukan` (to need).

### Day Names — DIFFER from Indonesian

| Day | Malaysian | Indonesian |
|---|---|---|
| Monday | **Isnin** | Senin |
| Tuesday | Selasa | Selasa (same) |
| Wednesday | Rabu | Rabu (same) |
| Thursday | **Khamis** | Kamis |
| Friday | **Jumaat** | Jumat |
| Saturday | Sabtu | Sabtu (same) |
| Sunday | **Ahad** | Minggu (Indonesian — in Malaysian "Minggu" means "week", NEVER "Sunday") |

`Minggu` in Malaysian = week only. `Ahad` = Sunday. Confusing them is a quality failure.

### Times of Day — 3 periods (NOT 4 like Indonesian)

| Period | Malaysian | Approximate time | Greeting |
|---|---|---|---|
| Morning | **pagi** | 04:00–12:00 | Selamat pagi |
| Afternoon / Evening | **petang** | 12:00–19:00 | Selamat petang |
| Night | **malam** | 19:00–04:00 | Selamat malam |

(Indonesian uses 4: pagi / siang / sore / malam. Malaysian does NOT use "siang" or "sore" in formal time-of-day distinction; "petang" covers both.)

### Number Format — Anglo / English-influenced

- **Decimal separator: period** (3**.**14)
- **Thousands separator: comma** (1**,**000**,**000)
- Format: `1,234,567.89`
- ❌ 3,14 (European) → ✅ **3.14**
- ❌ 1.000.000 (Indonesian) → ✅ **1,000,000**
- This is the **OPPOSITE** of Indonesian.

### Currency: MYR Ringgit

- **Malaysia uses the ringgit (RM / MYR).** NOT Indonesian rupiah.
- Format: **`RM 1,000`** or **`RM1,000`** or **`RM 1,234.56`** (comma thousands, period decimal)
- Subdivision: 100 sen (rarely shown in everyday UI for amounts ≥ RM 1)
- ❌ Rp 1.000.000 (Indonesian) → ✅ **RM ...** (different currency entirely)
- ❌ RM 1.000,00 (Indonesian format) → ✅ **RM 1,000.00**

Brunei: BND (Brunei dollar, B$ or BND); equivalent to SGD 1:1 by peg.
Singapore Malay: SGD (S$). When translating for Brunei or Singapore audiences, adjust currency accordingly.

## Register

**Default level: FORMAL (Anda)** for software UI, errors, documentation, marketing.

| Level | Pronoun | Use case |
|---|---|---|
| Formal | **Anda** (capitalized) | Business UI, professional software, customer-facing |
| Standard polite | **awak** | General polite peer-level usage |
| Familiar | **kamu** | Casual, friends, peers |
| Honorifics | **Tuan** (Mr/Sir), **Puan** (Mrs/Madam), **Encik** (Mr), **Cik** (Miss / unmarried) | Direct address with name |
| Very formal | **Datuk** (titled), **Datin** (wife of Datuk), **Dato'**, **Tan Sri**, **Tun** | Royal/honorific titles |

**Politeness marker:** `Sila` (please) — used frequently for polite requests.

- "**Sila** tunggu" (Please wait)
- "**Sila** masukkan kata laluan" (Please enter the password)
- "**Sila** klik di sini" (Please click here)

**Rules:**
- Choose ONE pronoun level per file.
- Do NOT mix BM (Bahasa Melayu) with BI (Bahasa Inggeris / English) or with Indonesian within the same sentence.
- Use `Sila` liberally for polite UI requests.

**Examples:**
- ❌ "Anda nak delete tak?" (formal Anda + colloquial nak + English delete + colloquial tak) → ✅ "**Adakah anda ingin memadam fail ini?**"
- ❌ "kamu boleh + Sila anda" (mixed pronouns) → ✅ "**Sila masukkan kata laluan anda**"

### Formal vs Colloquial Vocabulary (severity 1.5)

Professional UI must use **bahasa baku (standard formal Malay)**:

| Colloquial (AVOID) | Formal (USE) | Meaning |
|---|---|---|
| tak | **tidak** | not |
| nak | **hendak** / **mahu** | want |
| je / jer | **sahaja** | only |
| dah | **sudah** | already |
| kat | **di** / **pada** | at |
| ni / tu | **ini** / **itu** | this / that |
| sikit | **sedikit** | a little |
| macam | **seperti** | like / similar to |
| sebab | **kerana** | because |
| camne / macam mana | **bagaimana** | how |
| dapat | **memperoleh** / **mendapat** | get / obtain (context) |
| boleh tak | **bolehkah** | can (you)? |

## Critical Hard Rules

### Affix System: me- / di- / ber- / -kan / -i (severity 2.0)

Malaysian grammar runs on **affixation** — same system as Indonesian:

| Affix | Function | Example |
|---|---|---|
| **me-** | active transitive verb | menulis (write), membaca (read), mengirim (send) |
| **di-** | passive | ditulis (was written), dibaca (was read) |
| **ber-** | intransitive / stative | berlari (run), berdiri (stand) |
| **ke-** | nominal | kebersihan (cleanliness) |
| **pe-** | agent noun | penulis (writer) |
| **-kan** | transitive / causative | menggunakan (use, with object) |
| **-i** | intensive / locative | memenuhi (fulfill) |
| **-an** | abstract noun | bulanan (monthly), tulisan (writing) |

### Nasal Assimilation with me- (severity 1.5)

The `me-` prefix changes form based on the **initial consonant of the root**:

| Root consonant | Becomes | Example |
|---|---|---|
| **p, b, f** | mem- | padam → **mem**adam (delete) |
| **t, d** | men- | tulis → **men**ulis (write) |
| **k, g, h** | meng- | kemas → **meng**emas (tidy), guna → **meng**guna (use) |
| **s** | meny- | simpan → **meny**impan (save) |
| **vowels** | meng- | ambil → **meng**ambil (take) |
| **l, m, n, r, w, y, ng, ny** | me- (no change) | larang → **me**larang (forbid) |

**Common errors:**
- ❌ mepadam → ✅ **memadam** (p → m)
- ❌ metulis → ✅ **menulis** (t → n)
- ❌ mekemas → ✅ **mengemas** (k → ng)
- ❌ mesimpan → ✅ **menyimpan** (s → ny)

### Transitive -kan Suffix (severity 2.0)

**Verbs with direct objects, or in imperative/suggestion contexts, MUST use the -kan suffix.**

| Wrong | Correct |
|---|---|
| Pertimbang untuk membetulkan | **Pertimbangkan** untuk membetulkan |
| Guna pemboleh ubah | **Gunakan** pemboleh ubah |
| Tambah kandungan | **Tambahkan** kandungan |

### "untuk" + Verb Requires me- Prefix (severity 2.0)

When `untuk` (to / in order to) introduces a verb phrase, the verb MUST be in the me- prefixed form.

| Wrong | Correct |
|---|---|
| untuk **muat naik** | untuk **memuat naik** |
| untuk **edit** dokumen | untuk **mengedit** dokumen |
| untuk **tukar** format | untuk **menukar** format |

Note: `muat naik` (upload) takes me- → `memuat naik`. The compound stays intact; only the first verb takes the prefix.

### Reduplication for Plurality (severity 2.0)

Malaysian has **no grammatical number marker**. Plural is marked by **reduplication** — but ONLY when no number is present.

| Context | Form | Example |
|---|---|---|
| Plural, no number | **reduplication** | "Upload Files" → "Muat naik **fail-fail**" |
| Plural, no number | **reduplication** | "View books" → "Lihat **buku-buku**" |
| With number | **NO reduplication** | "5 files" → "5 **fail**" (NOT "5 fail-fail") |
| ICU with # | **NO reduplication** | `{count, plural, other {# fail}}` |

ICU pattern (Malaysian has only `other` effectively):
```icu
{count, plural,
  other {# fail}
}
```

### Adverb Placement — After the Verb (severity 1.5)

Manner adverbs (`secara X` / `dengan X`) follow the **main verb**:

| Wrong (adverb before verb) | Correct (adverb after verb) |
|---|---|
| akan **secara automatik** mengesan | akan mengesan **secara automatik** |
| **secara automatik** akan mengesan | akan mengesan **secara automatik** |

## UI Conventions

### Button Labels — Short Imperative

| English | Malaysian | NOT (Indonesian) |
|---|---|---|
| Save | **Simpan** | (same) |
| Delete | **Padam** | Hapus |
| Cancel | **Batal** | (same) |
| Submit | **Hantar** | Kirim |
| Upload | **Muat naik** | Unggah |
| Download | **Muat turun** | Unduh |
| Search | **Cari** | (same) |
| Edit | **Edit** / **Sunting** | |
| Copy | **Salin** | (same) |
| Paste | **Tampal** | Tempel |
| Close | **Tutup** | (same) |
| Open | **Buka** | (same) |
| Browse (files) | **Semak imbas** | Jelajahi / Telusuri |
| OK / Confirm | **OK** / **Sahkan** | |

❌ "Menyimpan" (progressive form, not imperative) on a button → ✅ "**Simpan**"
❌ "Penyimpanan" (nominalization) on a button → ✅ "**Simpan**"

### Status Messages — Impersonal Progressive

Use **me- prefix** or **sedang + verb** for ongoing status:

| Wrong (first person) | Correct (impersonal) |
|---|---|
| Saya sedang memuatkan... | **Memuatkan...** / **Sedang memuatkan...** |
| Kami menyimpan... | **Menyimpan...** |

### Drag-and-Drop Vocabulary

- **seret** = drag (same as Indonesian — one of the few shared tech terms)
- **lepas** / **lepaskan** = drop / release
- ❌ "drag" / "drop" (English) — wrong

```
✅ Seret fail ke sini                       (drag files here)
✅ Seret dan lepas fail ke sini             (drag and drop files here)
✅ Lepaskan untuk memuat naik               (release to upload)
❌ Drag fail ke sini
❌ Release untuk muat naik
```

### Error Messages — Polite, Direct

- ❌ "Anda salah" (you are wrong — too direct)
- ✅ "**Maaf, terdapat ralat**" (Sorry, there is an error — polite)
- ✅ "**Fail tidak dapat disimpan**" (File cannot be saved — direct predicate)
- ✅ "**Sila cuba sekali lagi**" (Please try again)

Malaysian culture values harmony and indirect communication. Add `Sila` (please) and `Maaf` (sorry) liberally in error/instruction text.

### Redundant Word Patterns

| Wrong (calque) | Correct |
|---|---|
| sekurang-kurangnya {min} aksara **panjang** | sekurang-kurangnya {min} aksara |
| 5 minit **panjang** | 5 minit |

`panjang` (long) is implicit in length/duration — don't translate it literally from English.

## Punctuation, Numbers, Dates, Currency

### Quotation Marks
- Standard double quotes `"..."` — most common
- Single quotes `'...'` for nested

### Numbers (Anglo format — opposite of Indonesian)
- Decimal separator: **period** (3.14)
- Thousands separator: **comma** (1,000,000)
- Format: `1,234,567.89`
- ❌ 3,14 → ✅ **3.14**
- ❌ 1.000.000 → ✅ **1,000,000**

### Dates — DD/MM/YYYY
- Numeric: **15/01/2024**
- Word form: **15 Januari 2024** or **15hb Januari 2024** (`hb` = haribulan = "day-of-month", optional)
- Long form: **Isnin, 15 Januari 2024**

Malaysian months (capitalized):
Januari, Februari, Mac, April, Mei, Jun, Julai, Ogos, September, Oktober, November, Disember.

**Note month spelling differences from Indonesian:**

| Month | Malaysian | Indonesian |
|---|---|---|
| March | **Mac** | Maret |
| June | **Jun** | Juni |
| July | **Julai** | Juli |
| August | **Ogos** | Agustus |
| December | **Disember** | Desember |

### Time
- 24-hour: `14:30`
- 12-hour common in spoken: `2:30 petang` (2:30 PM in afternoon period)
- AM/PM equivalents: pagi (AM), petang (PM afternoon), malam (PM night)

### Currency: MYR Ringgit
- Format: **`RM 1,000`** or **`RM1,000`** or **`RM 1,234.56`**
- ❌ Rp ... → ✅ **RM ...**

### Comma Rules

**NO comma before coordinating conjunctions** (atau, dan):
- ❌ "Seret fail ke sini, atau klik untuk semak imbas" → ✅ "Seret fail ke sini atau klik untuk semak imbas"

**COMMA before subordinating conjunctions:**
- tetapi / namun (but): "Mudah, tetapi berkesan"
- yang (which / that): "Fail yang anda pilih"
- jika (if): "Klik di sini, jika anda ingin meneruskan"
- kerana (because): "Tidak berfungsi, kerana fail tidak dijumpai"
- apabila (when): "Tunggu, apabila proses selesai"
- supaya / agar (so that): "Simpan, supaya perubahan tersimpan"

## Terminology Quick Reference

| English | Malaysian | NOT (Indonesian) |
|---|---|---|
| Save | Simpan | (same) |
| Delete | **Padam** | Hapus |
| Cancel | Batal | (same) |
| Submit | Hantar | Kirim |
| Upload | **Muat naik** | Unggah |
| Download | **Muat turun** | Unduh |
| Settings | **Tetapan** | Pengaturan |
| Update | **Kemas kini** | Perbarui |
| Search | Cari | (same) |
| Edit | Edit / Sunting | (same) |
| Copy | Salin | (same) |
| Paste | **Tampal** | Tempel |
| Close | Tutup | (same) |
| Open | Buka | (same) |
| Browse (files) | **Semak imbas** | Jelajahi |
| Browse (web) | **Melayari** | (different word — Indonesian uses same `melayari`/`menjelajah`) |
| File | **Fail** | File / Berkas |
| Folder | Folder / Direktori | (same) |
| Window | **Tetingkap** | Jendela |
| Message | **Mesej** | Pesan |
| User | Pengguna | (same) |
| Password | **Kata laluan** | Kata sandi / Password |
| Username | **Nama pengguna** | (same) |
| Log in | **Log masuk** | Masuk / Login |
| Log out | **Log keluar** | Keluar / Logout |
| Dashboard | **Papan pemuka** | Dasbor / Dashboard |
| Account | **Akaun** | Akun |
| Email | **E-mel** | Email / Surel |
| Click | Klik | (same) |
| Loading | **Memuatkan** | Memuat |

**Proper noun abbreviations in UI:**
- ✅ **AS** / **Amerika Syarikat** (NOT "Amerika Serikat" — that's Indonesian spelling!)
- ✅ **UK** / **Britain** (NOT the full official name)
- ✅ **EU** for European Union (or "Kesatuan Eropah")
- ✅ **PBB** for UN (Pertubuhan Bangsa-Bangsa Bersatu)

Country names: Many differ from Indonesian:
| Country | Malaysian | Indonesian |
|---|---|---|
| USA | **Amerika Syarikat** / AS | Amerika Serikat / AS |
| UK | **United Kingdom** / Britain / UK | Inggris / Britania Raya |
| Japan | **Jepun** | Jepang |
| China | **China** / Tiongkok | Tiongkok / Cina |
| Korea | **Korea** | (same) |
| Russia | **Rusia** | (same) |
| Germany | **Jerman** | (same) |
| France | **Perancis** | Prancis |

**Brand names** stay in original form. Technical terms (API, URL, token) acceptable as-is.

## Calque / Anti-Pattern Blocklist

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| Ia masuk akal (literal) | **Ia logik / Ia boleh difahami** | "it makes sense" |
| Di penghujung hari | **Akhirnya / Kesimpulannya** | "at the end of the day" |
| Tidak benar-benar | **Sebenarnya tidak / Tidak juga** | "not really" |
| Mengambil rehat | **Berehat** | "take a break" |
| Patahkan kaki | **Semoga berjaya! / Selamat maju jaya!** | "break a leg" |
| Sekeping kek | **Senang macam ABC / Mudah sahaja** | "piece of cake" |
| Bila babi terbang | **Bila kera pandai menari** | "when pigs fly" (Malay equivalent uses monkey) |
| pengguna-mesra | **mesra pengguna** | "user-friendly" (head-modifier order) |
| multi-fungsi | **pelbagai fungsi** | "multi-functional" |
| panjang-jangka | **jangka panjang** | "long-term" |
| AI-dipacu | **berasaskan AI / dikuasakan AI** | "AI-powered" |

## Cultural Sensitivity

Malaysia is a **multiracial, multireligious society** — Malay (majority, Muslim), Chinese, Indian, indigenous (Orang Asli, Iban, Kadazan, etc.) with strong Islamic constitutional position alongside official multireligious recognition.

- Use **inclusive language** that doesn't exclude non-Malay Malaysians
- Be **respectful of Islamic values** (Malaysia's official religion) without alienating non-Muslims
- Avoid pork/alcohol/gambling imagery in mass-market UI
- Halal certification awareness in food/health domains
- Royalty (Sultans, Agong) — show respect in any reference; never irreverent
- Friday is a special day (Jumaat) — Muslim Friday prayers; avoid scheduling implying everyone works through it
- Ramadan / Hari Raya Aidilfitri / Aidiladha — important cultural moments to acknowledge in marketing

## Self-Check Checklist

Run BEFORE finalizing each translation:

**Identity (CRITICAL):**
- [ ] **Malaysian vocabulary, NOT Indonesian:** muat naik/muat turun/tetapan/kemas kini/tetingkap/mesej/padam/tampal/fail/semak imbas
- [ ] **No DANGEROUS false friends from Indonesian:** never use "butuh" (vulgar in MS — use perlu), "pusing" (means spin not dizzy — use pening), "punggung" (buttocks — use belakang for body-back), "sulit" (confidential not difficult — use susah for difficult)
- [ ] **Number format Anglo:** 1,234.56 (comma thousands, period decimal) — NOT 1.234,56 Indonesian
- [ ] **Currency RM (Ringgit), NOT Rp** (Rupiah is Indonesian)
- [ ] **Day names Malaysian:** Isnin/Khamis/Jumaat/Ahad (NOT Senin/Kamis/Jumat/Minggu)
- [ ] **Minggu = week (NOT Sunday)** — Sunday is Ahad
- [ ] **Month spelling Malaysian:** Mac (not Maret), Jun (not Juni), Julai (not Juli), Ogos (not Agustus), Disember (not Desember)
- [ ] **Times of day 3 periods:** pagi/petang/malam (NOT 4 periods like Indonesian)
- [ ] **Country names Malaysian:** Amerika Syarikat (NOT Amerika Serikat), Jepun (NOT Jepang)
- [ ] **"semak imbas" for file browsing** — NEVER "melayari" (which means web-surf)

**Accuracy:**
- [ ] **me- prefix used** for active verbs (menulis, mengemas)
- [ ] **Nasal assimilation correct** (p→m, t→n, k→ng, s→ny)
- [ ] **-kan suffix for transitive verbs** (Pertimbangkan, Gunakan, Tambahkan)
- [ ] **me- prefix after "untuk"** (untuk memuat naik, NOT untuk muat naik)
- [ ] **Reduplication for plural** without numbers (fail-fail)
- [ ] **NO reduplication with numbers** (5 fail, NOT 5 fail-fail)
- [ ] **Adverb after verb** (mengesan secara automatik, NOT secara automatik mengesan)
- [ ] **Conjunction commas:** no comma before atau/dan; comma before yang/jika/kerana/apabila
- [ ] **Placeholders preserved** exactly

**Naturalness:**
- [ ] **Anda/awak consistency** — same level throughout
- [ ] **Formal vocabulary:** tidak (not tak), hendak/mahu (not nak), sahaja (not je), sudah (not dah), di/pada (not kat)
- [ ] **Buttons concise** (Simpan, Padam, Batal)
- [ ] **Status impersonal** (Memuatkan..., NOT Saya sedang memuatkan)
- [ ] **Drag-and-drop:** seret, lepas (NOT drag, drop)
- [ ] **Error messages polite** with `Sila` and `Maaf` where appropriate
- [ ] **No mixing BM with English or Indonesian** in same sentence
- [ ] **Complete or-clauses** (atau klik untuk semak imbas — full)
- [ ] **Islamic/multiracial sensitivity** — avoid pork/alcohol/gambling in mass-market
- [ ] **`Sila` used appropriately** for polite requests
- [ ] **Compound adjective head-modifier order** (mesra pengguna, NOT pengguna-mesra)
- [ ] **No redundant "panjang"** (aksara, NOT aksara panjang)

## Worked Examples

### Example 1 — Save button + status

**Source:**
> Save  
> Saving your changes...  
> Changes saved.

**Wrong (Indonesian terms + first person):**
> Simpan / Saya sedang menyimpan perubahan / Perubahan tersimpan

**Correct (Malaysian):**
> **Simpan**  
> **Menyimpan perubahan...** (impersonal, me- prefix)  
> **Perubahan telah disimpan.** (di- passive — completion; `telah` = already/completed)

### Example 2 — Plural reduplication

**Source:**
> Upload Files / 5 files uploaded

**Correct:**
> **Muat naik fail-fail** (reduplication for plural without number)  
> **5 fail dimuat naik** (NO reduplication with number)

### Example 3 — File browse (the Malaysian-specific trap)

**Source:**
> Click here to browse files

**Wrong (uses web-surf word):**
> Klik di sini untuk melayari fail (melayari = web-surf, not file-browse!)

**Correct:**
> **Klik di sini untuk semak imbas fail** (semak imbas = file-browse)

### Example 4 — "untuk" + verb (me- mandatory)

**Source:**
> Click to upload / Click to edit / Click to change format

**Wrong:**
> Klik untuk muat naik / Klik untuk edit / Klik untuk tukar format

**Correct:**
> **Klik untuk memuat naik** / **Klik untuk mengedit** / **Klik untuk menukar format**

### Example 5 — Drag-and-drop with file (Malaysian)

**Source:**
> Drag and drop files here, or click to browse

**Wrong (Indonesian terms):**
> Seret dan lepas file ke sini atau klik untuk menjelajahi

**Correct (Malaysian):**
> **Seret dan lepas fail ke sini atau klik untuk semak imbas** (no comma before atau)

### Example 6 — Number/currency disambiguation

**Source:**
> Total: $1,234.56

**Wrong (Indonesian format):**
> Jumlah: RM 1.234,56 (Indonesian number format with Malaysian currency — broken)

**Correct (Malaysian format + currency):**
> **Jumlah: RM 5,250.00** (or whatever MYR equivalent — comma thousands, period decimal)

### Example 7 — Day name + date

**Source:**
> Monday, January 15, 2024

**Wrong (Indonesian day name):**
> Senin, 15 Januari 2024

**Correct (Malaysian):**
> **Isnin, 15 Januari 2024**

### Example 8 — Country name

**Source:**
> United States of America / Japan / December

**Wrong (Indonesian spellings):**
> Amerika Serikat / Jepang / Desember

**Correct (Malaysian):**
> **Amerika Syarikat** (or AS) / **Jepun** / **Disember**

### Example 9 — DANGEROUS false friend

**Source:**
> "I need this file."

**Wrong (Indonesian `butuh` — VULGAR in Malaysian):**
> Saya butuh fail ini.

**Correct (Malaysian):**
> **Saya perlu fail ini.** / **Saya memerlukan fail ini.**

### Example 10 — Polite request with Sila

**Source:**
> Please enter your password.

**Wrong (no politeness marker):**
> Masukkan kata laluan anda.

**Correct (with Sila):**
> **Sila masukkan kata laluan anda.**

### Example 11 — Formal vs colloquial

**Source:**
> Are you sure you want to delete this file?

**Wrong (colloquial mix):**
> Anda nak padam fail ni tak? (formal Anda + colloquial nak + colloquial ni + colloquial tak)

**Correct (formal):**
> **Adakah anda pasti ingin memadam fail ini?**

### Example 12 — Transitive -kan

**Source:**
> Consider improving this / Use this variable / Add content

**Correct (Malaysian):**
> **Pertimbangkan** untuk membetulkan / **Gunakan** pemboleh ubah / **Tambahkan** kandungan

## When in Doubt

1. **Malaysian or Indonesian word?** Check the disambiguation table. Malaysian: muat naik / muat turun / tetapan / kemas kini / tetingkap / mesej / padam / tampal / fail / semak imbas.
2. **Browse — files or web?** Files → **semak imbas**. Web → **melayari**. Never confuse them.
3. **Number format?** Comma thousands, period decimal (1,234.56). Anglo-style. OPPOSITE of Indonesian.
4. **Currency?** RM (Ringgit), NEVER Rp (Rupiah). Format: RM 1,000.00.
5. **Day of week?** Use Malaysian forms: Isnin / Selasa / Rabu / Khamis / Jumaat / Sabtu / Ahad. Remember: `Minggu` = week, NOT Sunday.
6. **Month?** Watch the spelling: Mac/Jun/Julai/Ogos/Disember (Malaysian) vs Maret/Juni/Juli/Agustus/Desember (Indonesian).
7. **DANGER words from Indonesian?** Avoid `butuh` (vulgar in MS — use `perlu`). Avoid `pusing` for "dizzy" (means spin — use `pening`). Avoid `punggung` for "back" (means buttocks — use `belakang`). Avoid `sulit` for "difficult" (means confidential — use `susah`).
8. **me- prefix form?** Same as Indonesian: p/b/f → mem-, t/d → men-, k/g/h → meng-, s → meny-, vowels → meng-, others → me-.
9. **`boleh` or `bisa`?** Malaysian uses `boleh` for "can/able". Do NOT use `bisa` in Malaysian — in Malay it means "poison/venom" and is misleading.
10. **Plural?** With number → no reduplication. Without number → reduplication. ICU `other` → no reduplication.
11. **`untuk` + verb?** Always with me- prefix.
12. **Formal or informal?** Default Anda for product UI; awak for peer-level; use `Sila` for politeness liberally.
13. **Country name?** Malaysian spellings differ: Amerika Syarikat (not Serikat), Jepun (not Jepang), Disember (not Desember).
14. **Brand vs translated tech term?** Brand names stay. Tech terms (API, URL) acceptable as-is but consistent.

Malaysian's challenge isn't grammar — it's avoiding **vocabulary slippage from Indonesian** and avoiding the file-browse / web-surf confusion. When the translation feels off, check the disambiguation table first, then the false-friend list.
