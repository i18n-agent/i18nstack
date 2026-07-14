---
name: localize-id
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Indonesian (Bahasa Indonesia) for Indonesia. CRITICAL — Indonesian is NOT Malaysian. Despite ~85% lexical overlap, the two have systematically different tech vocabulary (unggah NOT muat naik, unduh NOT muat turun, pengaturan NOT tetapan, perbarui NOT kemas kini, jendela NOT tetingkap, pesan NOT mesej, hapus NOT padam, tempel NOT tampal, jelajahi/telusuri NOT semak imbas, bisa NOT boleh as default \"can\"), different number formats (Indonesian uses 1.234,56 European-style — period thousands, comma decimal — like Dutch), different currency (Rp Rupiah NOT RM Ringgit), different day names (Senin/Kamis/Jumat/Minggu NOT Isnin/Khamis/Jumaat/Ahad), and different times-of-day (4 periods: pagi/siang/sore/malam NOT ms 3 periods). Other key features: extensive affix system (me-/di-/ber-/-kan/-i), nasal assimilation (p→m memadam, t→n menulis, k→ng mengirim, s→ny menyimpan), MANDATORY -kan suffix for transitive verbs (Pertimbangkan, Gunakan, Tambahkan), MANDATORY me- prefix after \"untuk\" (untuk mengunggah NOT untuk unggah), reduplication for plurality without numbers (file-file = files) but NOT with numbers (5 file), Anda/kamu formality with `kita` for inclusive warm tone, manner adverbs AFTER verb (mendeteksi secara otomatis NOT secara otomatis mendeteksi), formal vocabulary preference over slang (tidak NOT gak, sudah NOT udah, saja NOT aja, bagaimana NOT gimana), and religious/ethnic sensitivity (300+ ethnic groups, majority Muslim)."
---

# Localize: Indonesian (id → Bahasa Indonesia)

You are translating source text into Indonesian for Indonesia. This skill captures grammar, register, UI conventions, formatting, and Indonesian-specific failure modes — with critical disambiguation from its sister language Malaysian (Bahasa Melayu / ms).

## Scope & Variants

**One standard:**
- **id-ID** — Bahasa Indonesia as used in Indonesia. Official language of Indonesia.

No widely-distinguished regional variants in software localization. Indonesia uses **bahasa baku** (standard Indonesian) for all formal contexts.

**Native name:** Bahasa Indonesia (the language).

## Identity Guardrail — NOT Malaysian (CRITICAL)

**Indonesian (id) and Malaysian (ms / Bahasa Melayu) are sister languages with ~85% lexical overlap but distinct standards.** They are mutually intelligible to a degree but have **systematically different vocabulary in tech, UI, and modern domains** because they were standardized separately and drew loanwords from different sources:

- **Indonesian** — heavy Dutch colonial influence (kantor, sepatu, gratis, buncis, jendela, handuk, pulpen), some Javanese, Sanskrit, Arabic.
- **Malaysian** — heavy Arabic/Islamic and English influence; less Dutch.

**Mixing the two is a quality failure**, especially in tech UI. NEVER translate Indonesian content via Malaysian intermediaries or vice versa.

### Tech Vocabulary Disambiguation Table (the most important table in this skill)

| English | Indonesian (USE) | Malaysian (DO NOT USE for Indonesian) |
|---|---|---|
| Upload | **unggah** | muat naik |
| Download | **unduh** | muat turun |
| Settings | **pengaturan** / setelan | tetapan |
| Update | **perbarui** / mutakhirkan | kemas kini |
| Window | **jendela** | tetingkap |
| Message | **pesan** | mesej |
| Delete | **hapus** | padam |
| Paste | **tempel** | tampal |
| File | **file** / berkas | fail |
| Browse (files) | **jelajahi** / **telusuri** | semak imbas |
| Office | **kantor** | pejabat |
| Office (work for someone) | (use jabatan) | pejabat (Malaysian = office) |
| Can / able | **bisa** | boleh (Malaysian — in Indonesian "boleh" is informal "may") |

### False Friends with Malaysian (DANGER — different meanings, same spelling)

| Word | Indonesian meaning | Malaysian meaning |
|---|---|---|
| **kereta** | train (short for "kereta api") | car (the everyday car) |
| **butuh** | need (standard verb) | vulgar (genitalia) — DO NOT USE THIS WORD IN MALAYSIAN |
| **pusing** | dizzy / headache | to spin / to turn around |
| **punggung** | back (body part) | buttocks |
| **sulit** | difficult | confidential / secret |
| **comel** | (rare) | cute (common) |
| **abang** | older brother (informal) | older brother / boyfriend |

If you are writing Indonesian, you can use these freely in Indonesian senses. Just NEVER assume the meaning carries over to Malaysian.

### Day Names — DIFFER from Malaysian

| Day | Indonesian | Malaysian |
|---|---|---|
| Monday | **Senin** | Isnin |
| Tuesday | Selasa | Selasa (same) |
| Wednesday | Rabu | Rabu (same) |
| Thursday | **Kamis** | Khamis |
| Friday | **Jumat** | Jumaat |
| Saturday | Sabtu | Sabtu (same) |
| Sunday | **Minggu** | Ahad |

`Minggu` in Indonesian also means "week" — context disambiguates.

### Times of Day — 4 periods (NOT 3 like Malaysian)

| Period | Indonesian | Approximate time | Greeting |
|---|---|---|---|
| Morning | **pagi** | 04:00–11:00 | Selamat pagi |
| Midday | **siang** | 11:00–15:00 | Selamat siang |
| Afternoon | **sore** | 15:00–18:30 | Selamat sore |
| Evening / Night | **malam** | 18:30–04:00 | Selamat malam |

(Malaysian uses only 3: pagi / petang / malam — no "siang" or "sore" distinction.)

### Number Format — European (Dutch-influenced)

- **Decimal separator: comma** (3**,**14)
- **Thousands separator: period** (1**.**000.000)
- Format: `1.234.567,89`
- ❌ 1,234.56 (Anglo) → ✅ 1.234,56
- This is the **OPPOSITE** of Malaysian (which uses Anglo format).

### Currency: IDR Rupiah

- **Indonesia uses the rupiah (Rp / IDR).** NOT Malaysian ringgit (RM).
- Format: **`Rp 1.000.000`** or **`Rp1.000.000`** (period thousands, no decimals for small denominations — the rupiah is heavily inflated, sub-1000 amounts essentially nonexistent in UI)
- ❌ RM 1,000 (Malaysian) → ✅ Rp 1.000.000
- ❌ Rp 1,000,000 (Anglo format) → ✅ Rp 1.000.000

## Register

**Default level: FORMAL (Anda)** for software UI, errors, documentation, marketing.

| Level | Pronoun | Use case |
|---|---|---|
| Formal | **Anda** (capitalized) | Business UI, professional software, customer-facing |
| Informal | **kamu** | Consumer apps with casual brand voice, social, youth |
| Inclusive "we" | **kita** | Building connection — includes listener (use for warm, friendly tone) |
| Exclusive "we" | **kami** | Excludes listener (use for "we, the company") |

**Rules:**
- Choose ONE pronoun level (Anda OR kamu) per file.
- Use `kita` for warm/inclusive tone where the user is part of the action ("Mari kita mulai!" = Let's start!).
- Use `kami` when speaking AS the company TO the user ("Kami akan memberitahu Anda" = We will notify you).

**Examples:**
- ❌ "Anda mau hapus gak?" (formal Anda + slang `gak`) → ✅ "**Apakah Anda ingin menghapus file ini?**"
- ❌ "kamu yakin mau hapus?" (then `Anda` elsewhere in same file) → mix is wrong
- ✅ "Mari **kita** mulai perjalanan Anda" (inclusive warm tone using kita + Anda — acceptable in marketing)

### Formal vs Colloquial Vocabulary

Professional UI must use **bahasa baku (standard formal Indonesian)**:

| Colloquial (AVOID) | Formal (USE) | Meaning |
|---|---|---|
| gak / nggak | **tidak** | not / no |
| udah | **sudah** | already |
| aja / doang | **saja** | only / just |
| gimana | **bagaimana** | how |
| gini / gitu | **begini / begitu** | like this / that |
| emang | **memang** | indeed |
| banget | **sangat / sekali** | very |
| kayak / kaya | **seperti** | like / as |
| soalnya | **karena** | because |
| dong | (none — sentence particle) | (intensifier, omit in formal) |
| ya / iya | (acceptable in many contexts) | yes |

Colloquial is acceptable ONLY in: casual/youth-oriented apps with explicit informal tone, marketing content deliberately targeting informal register.

## Critical Hard Rules

### Affix System: me- / di- / ber- / -kan / -i (severity 2.0)

Indonesian's grammar runs on **affixation**. Roots become verbs with prefixes/suffixes:

| Affix | Function | Example |
|---|---|---|
| **me-** | active transitive verb | menulis (write), membaca (read), mengirim (send) |
| **di-** | passive | ditulis (was written), dibaca (was read) |
| **ber-** | intransitive / stative | berlari (run), berdiri (stand) |
| **ke-** | nominal | kebersihan (cleanliness), keadilan (justice) |
| **pe-** | agent noun | penulis (writer), pembaca (reader) |
| **-kan** | transitive / causative | menggunakan (use, with object), mempertimbangkan (consider) |
| **-i** | intensive / locative | memenuhi (fulfill), menulisi (write on) |
| **-an** | abstract noun | bulanan (monthly), tulisan (writing) |

### Nasal Assimilation with me- (severity 1.5)

The `me-` prefix changes form based on the **initial consonant of the root**:

| Root consonant | Becomes | Example (root → form) |
|---|---|---|
| **p, b, f** | mem- | padam → **mem**adam (extinguish), beli → **mem**beli (buy) |
| **t, d** | men- | tulis → **men**ulis (write), dorong → **men**dorong (push) |
| **k, g, h** | meng- | kirim → **meng**irim (send), gambar → **meng**gambar (draw) |
| **s** | meny- | simpan → **meny**impan (save), sapu → **meny**apu (sweep) |
| **vowels** | meng- | unggah → **meng**unggah (upload), ambil → **meng**ambil (take) |
| **l, m, n, r, w, y, ng, ny** | me- (no change) | larang → **me**larang (forbid), masuk → **me**masuki (enter) |

**Common errors:**
- ❌ mepadam → ✅ **memadam** (p → m)
- ❌ metulis → ✅ **menulis** (t → n)
- ❌ mekirim → ✅ **mengirim** (k → ng)
- ❌ mesimpan → ✅ **menyimpan** (s → ny)

The initial consonant is **assimilated/replaced** for p, t, k, s. For other consonants, the prefix simply attaches without modification.

### Transitive -kan Suffix (severity 2.0)

**Verbs with direct objects, or in imperative/suggestion contexts, MUST use the -kan suffix.**

| Wrong (intransitive) | Correct (transitive with -kan) |
|---|---|
| Pertimbang untuk memperbaiki | **Pertimbangkan** untuk memperbaiki (Consider improving) |
| Guna variabel | **Gunakan** variabel (Use the variable) |
| Tambah konten | **Tambahkan** konten (Add content) |
| Hilang file | **Hilangkan** file (Remove file) |
| Pikir tentang ini | **Pikirkan** tentang ini (Think about this) |

The bare root (Pertimbang, Guna, Tambah, Hilang) is grammatically incomplete when there's an object. `-kan` marks transitivity and is required.

### "untuk" + Verb Requires me- Prefix (severity 2.0)

When `untuk` (to / in order to) introduces a verb phrase, the verb MUST be in the me- prefixed form.

| Wrong | Correct |
|---|---|
| untuk **unggah** file | untuk **mengunggah** file |
| untuk **edit** dokumen | untuk **mengedit** dokumen |
| untuk **ubah** format | untuk **mengubah** format |
| untuk **simpan** perubahan | untuk **menyimpan** perubahan |
| untuk **kirim** email | untuk **mengirim** email |

This is one of the most-missed rules. Bare roots after `untuk` are a hallmark of bad translation.

### Reduplication for Plurality (severity 2.0)

Indonesian has **no grammatical number marker**. Plural is marked by **reduplication** — but ONLY when no number is present.

| Context | Form | Example |
|---|---|---|
| Plural, no number | **reduplication** | "Upload Files" → "Unggah **file-file**" |
| Plural, no number | **reduplication** | "View books" → "Lihat **buku-buku**" |
| With number/quantifier | **NO reduplication** | "5 files" → "5 **file**" (NOT "5 file-file") |
| With number/quantifier | **NO reduplication** | "{count} items" → "{count} **item**" |
| ICU with # | **NO reduplication** | `{count, plural, other {# file}}` |
| Generic / collective | **NO reduplication often** | "Semua file" (all files — collective, no reduplication needed) |

ICU pattern (Indonesian has only `other` effectively — no plural distinction needed):
```icu
{count, plural,
  other {# file}
}
```

The two branches of failure:
- ❌ "Unggah file" when meaning "Upload Files" (plural) — missing reduplication
- ❌ "5 file-file" when meaning "5 files" — wrong reduplication

### Adverb Placement — After the Verb (severity 1.5)

Manner adverbs (`secara X` / `dengan X`) follow the **main verb**, not the auxiliary.

| Wrong (adverb before verb) | Correct (adverb after verb) |
|---|---|
| akan **secara otomatis** mendeteksi | akan mendeteksi **secara otomatis** |
| Sistem **secara otomatis** akan mendeteksi | Sistem akan mendeteksi **secara otomatis** |
| **dengan cepat** menyelesaikan | menyelesaikan **dengan cepat** |

The adverb sits after the lexical verb, not between modal/auxiliary and verb.

## UI Conventions

### Button Labels — Short Imperative

Indonesian buttons use **short imperative verbs**, often bare roots that function as commands:

| English | Indonesian | Notes |
|---|---|---|
| Save | **Simpan** | |
| Delete | **Hapus** | NOT Padam (which is Malaysian) |
| Cancel | **Batal** / **Batalkan** | Both acceptable |
| Submit | **Kirim** | |
| Upload | **Unggah** | NOT Muat naik (Malaysian) |
| Download | **Unduh** | NOT Muat turun (Malaysian) |
| Search | **Cari** | |
| Edit | **Edit** / **Ubah** | |
| Copy | **Salin** | |
| Paste | **Tempel** | NOT Tampal (Malaysian) |
| Close | **Tutup** | |
| Open | **Buka** | |
| Browse | **Jelajahi** / **Telusuri** | NOT Semak imbas (Malaysian) |
| OK / Confirm | **OK** / **Konfirmasi** | |

❌ "Silakan klik di sini untuk menyimpan" (verbose) → ✅ "**Simpan**"

### Status Messages — Impersonal

Use **impersonal forms** (me- prefix with no subject, OR nominal). NEVER first person.

| Wrong (first person) | Correct (impersonal) |
|---|---|
| Saya sedang memuat... | **Memuat...** / **Sedang memuat...** |
| Kami menyimpan file Anda... | **Menyimpan...** / **Penyimpanan berhasil** |
| Saya memproses... | **Memproses...** |

The system speaks impersonally. "Saya" (I) for system messages sounds bizarre.

### Drag-and-Drop Vocabulary

- **seret** = drag
- **lepas** = drop / release
- ❌ "drag" / "drop" (English) — wrong

```
✅ Seret file ke sini                       (drag files here)
✅ Seret dan lepas file ke sini             (drag and drop files here)
✅ Pilih file atau seret ke sini            (select files or drag here — complete or clause)
❌ Pilih file atau seret                     (incomplete — finish the phrase)
❌ Drag file ke sini                         (English calque)
```

### Error Messages — Direct Predicate

Indonesian error messages favor direct predicate form over verbose nominal constructions:

- ❌ "Terjadi kesalahan saat menyimpan file" (verbose nominal "an error occurred when saving the file")
- ✅ "**File tidak dapat disimpan**" (File cannot be saved — direct predicate)
- ✅ "**Tidak dapat menghubungkan ke server**" (Cannot connect to server — direct predicate)

## Punctuation, Numbers, Dates, Currency

### Quotation Marks
- Standard double quotes `"..."` or single `'...'` — both common, be consistent
- No special "Indonesian quote marks"

### Numbers (European format — opposite of Malaysian)
- Decimal separator: **comma** (3**,**14)
- Thousands separator: **period** (1**.**000.000)
- Format: `1.234.567,89`
- ❌ 3.14 (Anglo decimal) → ✅ **3,14**
- ❌ 1,000,000 (Anglo thousands) → ✅ **1.000.000**

### Dates — DD/MM/YYYY
- Numeric: **15/01/2024** (slashes)
- Word form: **15 Januari 2024** (day + month name + year)
- Long form: **Senin, 15 Januari 2024** (with day name)
- ❌ 01/15/2024 (US) → ✅ 15/01/2024

Indonesian months (always capitalized in formal writing):
Januari, Februari, Maret, April, Mei, Juni, Juli, Agustus, September, Oktober, November, Desember.

### Time
- 24-hour: `14:30` or `14.30` (period as colon is also acceptable)
- Word form: `2 sore` (2 PM in afternoon period) or `pukul 14:30`
- "Jam" or "pukul" for "o'clock" (jam 2 = at 2 o'clock)

### Currency: IDR Rupiah
- Format: **`Rp 1.000.000`** or **`Rp1.000.000`** (period thousands, no decimal for round amounts)
- ❌ Rp 1,000,000 (Anglo) → ✅ **Rp 1.000.000**
- ❌ RM 1,000 (Malaysian) → ✅ **Rp ...**

### Comma Rules

**NO comma before coordinating conjunctions** (atau, dan):
- ❌ "Seret file ke sini, atau klik" → ✅ "Seret file ke sini atau klik"
- ❌ "Simpan file, dan tutup" → ✅ "Simpan file dan tutup"

**COMMA before subordinating conjunctions**:
- tetapi / namun (but): "Sederhana, tetapi efektif"
- yang (which / that): "File yang Anda pilih"
- jika (if): "Klik di sini, jika ingin melanjutkan"
- karena (because): "Tidak berfungsi, karena file tidak ditemukan"
- ketika / saat (when): "Tunggu, ketika proses selesai"
- supaya / agar (so that): "Simpan, supaya perubahan tersimpan"

## Terminology Quick Reference

| English | Indonesian | NOT (Malaysian) |
|---|---|---|
| Save | Simpan | (same) |
| Delete | **Hapus** | Padam |
| Cancel | Batal / Batalkan | (same) |
| Submit | Kirim | Hantar |
| Upload | **Unggah** | Muat naik |
| Download | **Unduh** | Muat turun |
| Settings | **Pengaturan** / Setelan | Tetapan |
| Update | **Perbarui** / Mutakhirkan | Kemas kini |
| Search | Cari | (same) |
| Edit | Edit / Ubah | (Sunting) |
| Copy | Salin | (same) |
| Paste | **Tempel** | Tampal |
| Close | Tutup | (same) |
| Open | Buka | (same) |
| Browse (files) | **Jelajahi / Telusuri** | Semak imbas |
| File | **File / Berkas** | Fail |
| Folder | Folder / Direktori | (same / Folder) |
| Window | **Jendela** | Tetingkap |
| Message | **Pesan** | Mesej |
| User | Pengguna | (same) |
| Password | Kata sandi / Password | Kata laluan |
| Username | Nama pengguna | (same) |
| Log in | **Masuk** / Login | Log masuk |
| Log out | **Keluar** / Logout | Log keluar |
| Dashboard | Dasbor / Dashboard | Papan pemuka |
| Account | Akun | Akaun |
| Email | Email / Surel | E-mel |
| Click | Klik | (same) |
| Loading | Memuat | Memuatkan |

**Proper noun abbreviations in UI:**
- ✅ **AS** / **Amerika Serikat** (NOT in cramped UI)
- ✅ **Inggris** / **Britania Raya** (NOT "Kerajaan Britania Raya dan Irlandia Utara")
- ✅ **UE** (Uni Eropa) for European Union
- ✅ **PBB** (Perserikatan Bangsa-Bangsa) for UN
- ✅ **Jepang** (Japan), **Tiongkok** (China — modern preferred form over Cina)

**Brand names** stay in original form. Technical terms (API, URL, token) acceptable as-is but be consistent.

## Calque / Anti-Pattern Blocklist

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| Membuat masuk akal | **Masuk akal / Logis** | "to make sense" |
| Itu masuk akal (very literal) | **Itu logis / Itu bisa dimengerti** | "that makes sense" |
| Di akhir hari | **Pada akhirnya / Intinya** | "at the end of the day" |
| Tidak benar-benar | **Sebenarnya tidak / Tidak juga** | "not really" |
| Mengambil istirahat | **Beristirahat** | "take a break" |
| Patahkan kaki | **Semoga sukses! / Semoga berhasil!** | "break a leg" |
| Sepotong kue | **Mudah sekali / Gampang banget** | "piece of cake" |
| 25+ bahasa | **lebih dari 25 bahasa / 25 bahasa atau lebih** | "25+ languages" |
| +{count} lagi | **dan {count} lainnya / {count} lagi** | "+{count} more" |
| minimal {min} karakter panjangnya | **minimal {min} karakter** | redundant "panjangnya" |
| pengguna-ramah | **ramah pengguna** | "user-friendly" (head-modifier order) |
| AI-digerakkan | **berbasis AI / didukung AI** | "AI-powered" |
| panjang-istilah | **jangka panjang** | "long-term" |

## Cultural Sensitivity

Indonesia has **300+ ethnic groups** and is the world's **largest Muslim-majority country**. UI text should:
- Use **inclusive, pan-Indonesian** expressions; avoid references specific to one ethnic group (Javanese-only, Sundanese-only, Balinese-only)
- Be **respectful of religious diversity** — Indonesia officially recognizes 6 religions (Islam, Protestantism, Catholicism, Hinduism, Buddhism, Confucianism)
- Avoid pork/alcohol imagery in marketing aimed at general consumers
- Use `kita` for warm inclusive tone where appropriate
- Use Sundanese / Javanese / Balinese / Batak / Bugis loanwords only when the audience is explicitly that region's

## Self-Check Checklist

Run BEFORE finalizing each translation:

**Identity (CRITICAL):**
- [ ] **Indonesian vocabulary, NOT Malaysian:** unggah/unduh/pengaturan/perbarui/jendela/pesan/hapus/tempel/jelajahi
- [ ] **Number format Indonesian:** 1.000.000 (period thousands), 3,14 (comma decimal) — NOT 1,000,000 / 3.14
- [ ] **Currency Rp (Rupiah), NOT RM** (Ringgit is Malaysian)
- [ ] **Day names Indonesian:** Senin/Kamis/Jumat/Minggu (NOT Isnin/Khamis/Jumaat/Ahad)
- [ ] **Times of day 4 periods:** pagi/siang/sore/malam (NOT Malaysian 3 periods)

**Accuracy:**
- [ ] **me- prefix used** for active verbs (menulis, mengirim, mengunggah)
- [ ] **Nasal assimilation correct** (p→m, t→n, k→ng, s→ny)
- [ ] **-kan suffix for transitive verbs** (Pertimbangkan, Gunakan, Tambahkan)
- [ ] **me- prefix after "untuk"** (untuk mengunggah, NOT untuk unggah)
- [ ] **Reduplication for plural** without numbers (file-file)
- [ ] **NO reduplication with numbers** (5 file, NOT 5 file-file)
- [ ] **Adverb after verb** (mendeteksi secara otomatis, NOT secara otomatis mendeteksi)
- [ ] **Conjunction commas:** no comma before atau/dan; comma before tetapi/yang/jika/karena/ketika
- [ ] **Placeholders preserved** exactly

**Naturalness:**
- [ ] **Anda/kamu consistency** — same level throughout
- [ ] **Formal vocabulary:** tidak (not gak), sudah (not udah), saja (not aja), bagaimana (not gimana)
- [ ] **Buttons concise** (Simpan, Hapus, Batal — not verbose)
- [ ] **Status impersonal** (Memuat..., NOT Saya sedang memuat)
- [ ] **Drag-and-drop:** seret, lepas (NOT drag, drop)
- [ ] **Error messages direct** (File tidak dapat disimpan, NOT Terjadi kesalahan saat menyimpan file)
- [ ] **`kita` for warm inclusive tone** where appropriate
- [ ] **Complete or-clauses** (atau seret ke sini, NOT just atau seret)
- [ ] **Active voice preferred** over excessive di- passive
- [ ] **Religious/ethnic sensitivity** — inclusive, no pork/alcohol in mass-market UI
- [ ] **No redundant modifiers** (karakter, NOT karakter panjangnya)
- [ ] **Compound adjective head-modifier order** (ramah pengguna, NOT pengguna-ramah)

## Worked Examples

### Example 1 — Save button + status

**Source:**
> Save  
> Saving your changes...  
> Changes saved.

**Wrong (mixing with English / first person):**
> Save (English on button)  
> Saya sedang menyimpan perubahan... (first person)  
> Perubahan telah di-save. (calque + di- with English root)

**Correct:**
> **Simpan**  
> **Menyimpan perubahan...** (impersonal me- prefix)  
> **Perubahan berhasil disimpan.** (di- passive — completion)

### Example 2 — Plural reduplication

**Source:**
> Upload Files (button label, plural)  
> 5 files uploaded  
> Files (general label, list header)

**Correct:**
> **Unggah File-file** (reduplication required for plural without number)  
> **5 file diunggah** (NO reduplication with number)  
> **File-file** (reduplication for general plural label)

### Example 3 — "untuk" + verb (me- mandatory)

**Source:**
> Click to upload / Click to edit / Click to change format

**Wrong:**
> Klik untuk unggah / Klik untuk edit / Klik untuk ubah format

**Correct:**
> **Klik untuk mengunggah** / **Klik untuk mengedit** / **Klik untuk mengubah format**

### Example 4 — Drag-and-drop area

**Source:**
> Drag and drop files here, or click to browse

**Wrong (Malaysian terms + English):**
> Muat naik file ke sini, atau click untuk semak imbas

**Correct (Indonesian terms):**
> **Seret dan lepas file ke sini atau klik untuk menjelajahi** (no comma before atau)

### Example 5 — Number/currency disambiguation

**Source:**
> Total: $1,234.56

**Wrong (Malaysian or Anglo format):**
> Total: Rp 1,234.56 (Anglo number format with Indonesian currency — broken)
> Total: RM 1.234,56 (Malaysian currency with Indonesian number — broken)

**Correct (Indonesian format + currency):**
> **Total: Rp 18.500.000** (or whatever IDR equivalent — period thousands, no decimals)

### Example 6 — Formal vs colloquial

**Source:**
> Are you sure you want to delete this file?

**Wrong (colloquial):**
> Lo yakin mau hapus file ini gak?

**Wrong (mixed):**
> Apakah Anda yakin mau hapus file ini? (Anda + casual `mau`)

**Correct (formal):**
> **Apakah Anda yakin ingin menghapus file ini?**

**Acceptable (consistent informal):**
> **Apakah kamu yakin ingin menghapus file ini?**

### Example 7 — Adverb placement

**Source:**
> The system will automatically detect changes.

**Wrong:**
> Sistem akan **secara otomatis** mendeteksi perubahan. (adverb before verb)

**Correct:**
> **Sistem akan mendeteksi perubahan secara otomatis.** (adverb after verb)

### Example 8 — Transitive -kan

**Source:**
> Consider improving this / Use this variable / Add content

**Wrong:**
> Pertimbang untuk memperbaiki / Guna variabel ini / Tambah konten

**Correct:**
> **Pertimbangkan** untuk memperbaiki / **Gunakan** variabel ini / **Tambahkan** konten

### Example 9 — Inclusive `kita`

**Source:**
> Let's start your journey

**Possible translations:**
> ✅ **Mari kita mulai perjalanan Anda** (inclusive `kita` for warmth, Anda for the user's journey)  
> ⚠️ "Mari mulai perjalanan Anda" (omits the warmth)  
> ❌ "Kami akan memulai perjalanan Anda" (exclusive `kami` — wrong; this isn't us doing it for you, this is us doing it together)

### Example 10 — Day names + date

**Source:**
> Monday, January 15, 2024

**Wrong (Malaysian day name):**
> Isnin, 15 Januari 2024

**Correct (Indonesian day name):**
> **Senin, 15 Januari 2024**

## When in Doubt

1. **Indonesian or Malaysian word?** Check the tech vocab disambiguation table. Indonesian uses: unggah/unduh/pengaturan/perbarui/jendela/pesan/hapus/tempel/jelajahi. Malaysian uses: muat naik/muat turun/tetapan/kemas kini/tetingkap/mesej/padam/tampal/semak imbas.
2. **Number format?** Period thousands, comma decimal (1.000.000 / 3,14). OPPOSITE of Anglo and OPPOSITE of Malaysian.
3. **Currency?** Rp (Rupiah), NEVER RM (Ringgit). Format: Rp 1.000.000 (no decimals, period thousands).
4. **Day of week?** Use Indonesian forms: Senin / Selasa / Rabu / Kamis / Jumat / Sabtu / Minggu.
5. **me- prefix form?** Look at root's first consonant. p/b/f → mem-, t/d → men-, k/g/h → meng-, s → meny-, vowels → meng-, others → me-.
6. **`bisa` or `boleh`?** Both exist in Indonesian. `bisa` = can/able (standard). `boleh` = may (asking permission — informal). Default to `bisa` for "can".
7. **Plural?** With number → no reduplication. Without number → reduplication. ICU `other` → no reduplication (the # provides count).
8. **`untuk` + verb?** Always with me- prefix. Never bare root.
9. **Formal or informal?** Default Anda for product UI; kamu only for casual brand voice.
10. **Avoid colloquial:** tidak (not gak), sudah (not udah), saja (not aja), bagaimana (not gimana).
11. **Active or passive?** Indonesian uses di- passive a lot. Acceptable but don't overdo it. Active voice is often clearer.
12. **Religious imagery?** Avoid pork, alcohol, gambling references in mass-market UI for the largest Muslim-majority country.

Indonesian's isolating + affixing grammar means most errors are at the **affix level** (missing me-, wrong nasal assimilation, missing -kan) or at the **vocabulary level** (Malaysian word slipping in). When the translation feels off, check the affix table and the disambiguation table first.
