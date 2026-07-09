---
name: localize-th
description: Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Thai (ภาษาไทย) for Thailand. Thai is an isolating Tai-Kadai language with NO grammatical gender, NO number agreement, NO case system, NO verb conjugation. THE defining critical feature is NO SPACES between Thai words (ยินดีต้อนรับ NOT ยินดี ต้อนรับ — spaces ONLY at clause/sentence breaks, but spaces ARE required around colons). Other key features: 5-tone system with mandatory tone marks (combination of consonant class + vowel length + tone mark determines tone), rich classifier system (คน for people, ตัว for animals, อัน for objects, แผ่น for flat, ภาษา for languages, ลูก for round, เล่ม for books, คัน for vehicles), three formality registers (ทางการ formal / สุภาพ polite — DEFAULT for UI / พูด colloquial), polite particles ครับ/ค่ะ in conversation but NEVER in UI buttons/labels, คุณ pronoun for UI (NOT เธอ which is intimate), modifier-AFTER-head word order (ไฟล์ใหม่ NOT ใหม่ไฟล์), Buddhist Era dates option (2567 = 2024 CE), Baht currency (฿1,000), rejection of colloquial shortenings (ไม่ได้ not มะได้, อะไร not ไร), tech-friendly loanword tolerance (อีเมล, อัปเดต, เว็บไซต์ preferred over verbose calques), and list parallelism (all language names in a list must use the same form — either all "ภาษาเยอรมัน, ภาษาฟินแลนด์" or all bare).
---

# Localize: Thai (th → ภาษาไทย)

You are translating source text into Thai for Thailand. This skill captures grammar, register, UI conventions, formatting, and Thai-specific failure modes derived from a production translation prompt.

## Scope & Variants

**One standard:**
- **th-TH** — Central Thai (ภาษาไทยกลาง) as used in Bangkok. The national standard.

**Regional varieties** (Northern/Isaan/Southern) exist as spoken languages but are NEVER used in written/UI contexts. Always write standard Central Thai.

**Native name:** ภาษาไทย (the language).

**Identity guardrail:**
- Thai is **Tai-Kadai (Kra-Dai)**, NOT Chinese (Sino-Tibetan), NOT Vietnamese (Austroasiatic), NOT Cambodian (Austroasiatic), NOT Burmese (Sino-Tibetan). Closest relative is Lao (mutually intelligible to ~70%).
- Thai uses the **Thai script** (อักษรไทย), derived from Khmer/Brahmi. 44 consonants, 32 vowels (including combinations), 4 tone marks. NOT Latin script.
- Thai is **isolating** — no inflections, no gender, no number. Grammar is conveyed by word order, particles, and tones.
- Thai has heavy Sanskrit/Pali influence in formal vocabulary (especially religious, royal, legal). UI generally uses everyday Thai vocabulary.

## Register

**Default level: ภาษาสุภาพ (polite standard)** for software UI, errors, documentation, marketing.

Thai has three main formality registers:

| Register | Use case | Example |
|---|---|---|
| **ภาษาทางการ (formal)** | Royal/legal/official documents | กราบเรียน ท่าน |
| **ภาษาสุภาพ (polite — UI default)** | Business, UI, customer service, public | คุณสามารถ, กรุณา |
| **ภาษาพูด (colloquial)** | Casual conversation, social media | ไร, มะได้, รึป่าว |

**Within a file, ONE register only.** Don't mix formal and colloquial.

**Colloquial shortenings to AVOID in UI:**

| Wrong (colloquial) | Correct (polite written) | Meaning |
|---|---|---|
| มะได้ | **ไม่ได้** | cannot |
| ไร | **อะไร** | what |
| แค่นั้น | **เท่านั้น** | only that |
| งั้น | **เช่นนั้น / ถ้าอย่างนั้น** | so / in that case |
| รึ | **หรือ** | or |
| ป่าว | **หรือเปล่า** | or not |
| ก็ได้ | (acceptable in casual UI; varies) | also possible |
| หนิ | **นี้** | this |
| เนี่ย | (intensifier — avoid in UI) | this/here |

## Critical Hard Rules

### NO SPACES Between Thai Words (severity 2.0 — THE defining Thai rule)

**Thai does NOT use spaces between words.** Words run continuously. Spaces are ONLY used at clause/sentence boundaries.

| Wrong (English-style spacing) | Correct (Thai run-together) |
|---|---|
| ยินดี ต้อนรับ | **ยินดีต้อนรับ** (welcome) |
| สวัสดี ตอน เช้า | **สวัสดีตอนเช้า** (good morning) |
| คุณ สามารถ ลบ ไฟล์ ได้ | **คุณสามารถลบไฟล์ได้** (you can delete the file) |
| ผม กำลัง ทำ | **ผมกำลังทำ** (I am doing) |
| ภาษา ไทย | **ภาษาไทย** (Thai language) |
| ใหม่ ๆ | **ใหม่ ๆ** (multiple new — repetition mark `ๆ` does take adjacent space-like behavior) |

**This is the #1 Thai translation error.** Machine translators and non-native writers add English-style spaces that completely break Thai readability.

**Spaces ARE used at:**
- Clause breaks (where English would use a comma or period)
- Before and after Latin/Arabic numerals embedded in Thai text: "อายุ 25 ปี" (age 25 years)
- Before and after Latin script embedded: "เปิด Microsoft Word"
- **Before and after the colon (:)** — see below

**Spaces are NOT used:**
- Between Thai words
- Within compound words: "เครื่องบิน" (airplane), "ห้องน้ำ" (bathroom)

### Colon Spacing (severity 1.5)

Thai requires a **space before AND after the colon** (unlike English which has only space after):

- ❌ "อีเมล:user@example.com" (no spaces) → ✅ "**อีเมล : user@example.com**"
- ❌ "ชื่อ: สมชาย" → ✅ "**ชื่อ : สมชาย**"
- ❌ "เวลา:14:30" → ✅ "**เวลา : 14:30**" (but the time itself has no space around the colon)

This is part of standard Thai typographic convention.

### Tone Marks and Vowels (essential — meaning-critical)

Thai has 5 tones determined by a combination of:
1. **Consonant class** (high/mid/low — three classes)
2. **Vowel length** (long/short)
3. **Live/dead syllable** (final consonant or vowel ending)
4. **Tone mark** (◌่ ◌้ ◌๊ ◌๋ — mai ek, mai tho, mai tri, mai chattawa)

The tone determines meaning:
- มา (mā, mid tone) = to come
- ม่า (mà, low tone) = (rare)
- ม้า (má, high tone) = horse
- หม้า / หมา (hmǎ, rising tone) = dog (with high-class consonant cluster)

**NEVER omit tone marks or vowel marks.** All Thai diacritics are meaning-critical.

**Vowel marks that go above, below, before, after, or around the consonant:**
- เ-, แ-, โ-, ใ-, ไ- (before)
- -ะ, -า (after)
- -ิ, -ี, -ึ, -ื, -ุ, -ู (above/below)
- เ-า, เ-ือ (around)

Get them all right.

### Classifier System (ลักษณนาม) (severity 1.5)

Thai requires **a classifier (ลักษณนาม) when counting nouns**. The pattern is:

**NOUN + NUMBER + CLASSIFIER** (most common)
or **NUMBER + CLASSIFIER + NOUN** (less common, archaic)

| Classifier | Used for | Example |
|---|---|---|
| **คน** | people | คน 5 คน (five people), ผู้ใช้ 3 คน (3 users) |
| **ตัว** | animals, some objects (clothing items, characters) | แมว 2 ตัว (2 cats), เสื้อ 1 ตัว (1 shirt) |
| **อัน** | general small objects | ปากกา 3 อัน (3 pens) |
| **ชิ้น** | pieces, items | เค้ก 5 ชิ้น (5 pieces of cake) |
| **แผ่น** | flat objects, sheets, discs | กระดาษ 10 แผ่น (10 sheets) |
| **ใบ** | flat-roundish (paper, leaves, hats, faces) | ใบไม้ 3 ใบ (3 leaves), หมวก 1 ใบ |
| **ลูก** | round objects, fruits, children (informal) | ลูกบอล 1 ลูก (1 ball) |
| **เล่ม** | books, knives | หนังสือ 3 เล่ม (3 books) |
| **คัน** | vehicles, umbrellas, fishing rods | รถ 1 คัน (1 car) |
| **หลัง** | buildings | บ้าน 2 หลัง (2 houses) |
| **แห่ง / ที่** | places, locations | สถานที่ 5 แห่ง |
| **รายการ** | items in a list | 10 รายการ (10 items) |
| **ภาษา** | languages (the noun IS the classifier) | 5 ภาษา (5 languages) |
| **ไฟล์** | files (the noun IS the classifier in modern usage) | 10 ไฟล์ (10 files) |

**Self-classifying nouns** (don't need an additional classifier): ภาษา, ไฟล์, นาที, วินาที, ชั่วโมง, รายการ. The noun itself acts as classifier.

- ❌ 5 คน ภาษา (cannot use "person" classifier for language)
- ✅ **5 ภาษา** (language is its own classifier)
- ✅ **5 ไฟล์** (file is its own classifier in modern usage)

### Modifier-After-Head Word Order (severity 1.5)

Thai modifiers FOLLOW the head word (like Vietnamese, opposite of English):

| Wrong (English order) | Correct (Thai) | English |
|---|---|---|
| ใหม่ไฟล์ | **ไฟล์ใหม่** | new file |
| ดีระบบ | **ระบบดี** | good system |
| ใหญ่ห้อง | **ห้องใหญ่** | big room |
| สวยหญิง | **หญิงสวย** | beautiful woman |

Applies to:
- Adjectives (ไฟล์ **ใหม่**)
- Demonstratives (ไฟล์ **นี้** this, ไฟล์ **นั้น** that)
- Possessives via ของ (ไฟล์ **ของฉัน** my file)
- Relative clauses (ไฟล์ **ที่ฉันเลือก** the file that I selected)

### Pronoun Choice for UI

Thai has dozens of pronouns. For UI:

| Pronoun | Use | Note |
|---|---|---|
| **คุณ** | "you" — polite standard | **DEFAULT for UI** |
| ท่าน | "you" — formal/honorific | For premium/banking |
| เธอ | "you" — intimate | **NEVER in UI** (sounds romantic/familial) |
| คุณท่าน | "you" — formal | Less common |
| ผม / ดิฉัน | "I" — polite (m / f) | For first-person if needed (rare in UI) |
| พวกเรา | "we" — inclusive | For "we" |

- ❌ "เธอสามารถ..." (intimate) → ✅ "**คุณสามารถ...**"

### Active Voice over Passive (severity 1.5)

Thai prefers active voice. The passive marker `ถูก` (suggests negative experience) or `โดย` (formal) creates stiff translations:

| Wrong (passive) | Correct (active) | English |
|---|---|---|
| ไฟล์**ถูกบันทึก**โดยระบบ | **ระบบบันทึก**ไฟล์แล้ว / **บันทึก**ไฟล์**แล้ว** | The file was saved by the system |
| ผู้ใช้**ถูกตัดออก** | **ตัด**ผู้ใช้**ออกแล้ว** | The user was removed |
| ข้อความ**ถูกส่ง** | **ส่ง**ข้อความ**แล้ว** | The message was sent |

`ถูก` is fine when expressing genuinely passive/negative scenarios ("ถูกแฮ็ก" = was hacked) but should not pad UI status messages.

### Progressive Form with `กำลัง` (for status messages)

Thai uses **`กำลัง + verb`** for ongoing actions:

| Wrong | Correct | English |
|---|---|---|
| โหลด... | **กำลังโหลด...** | Loading... |
| บันทึก... | **กำลังบันทึก...** | Saving... |
| ประมวลผล... | **กำลังประมวลผล...** | Processing... |
| ส่ง... | **กำลังส่ง...** | Sending... |

For completed: **`แล้ว`** marker — "บันทึกแล้ว" (saved), "เสร็จแล้ว" (done).

## UI Conventions

### Button Labels — No Polite Particles

Thai buttons use **bare verbs/imperatives without polite particles**. The polite particles ครับ (male) and ค่ะ (female) are for spoken/conversational use and bloat UI:

| Wrong (with particle) | Correct (clean) | English |
|---|---|---|
| กรุณาบันทึกครับ | **บันทึก** | Save |
| กรุณายกเลิกค่ะ | **ยกเลิก** | Cancel |
| กรุณาลบครับ | **ลบ** | Delete |
| กรุณาอัปโหลดค่ะ | **อัปโหลด** | Upload |
| กรุณาดาวน์โหลด | **ดาวน์โหลด** | Download |
| กรุณาเลือก | **เลือก** | Select |
| กรุณาตกลง | **ตกลง** | OK / Confirm |

`กรุณา` (please) is sometimes used in instructions or polite system messages but not on action buttons.

### Status Messages — No Polite Particles

```
✅ กำลังโหลด...        (Loading...)
✅ กำลังบันทึก...       (Saving...)
✅ บันทึกแล้ว           (Saved)
✅ เสร็จสิ้น             (Complete)
❌ กำลังโหลดครับ        (with polite particle — wrong for UI)
❌ บันทึกแล้วค่ะ         (with polite particle)
```

### Drag-and-Drop Vocabulary

- **ลาก** = drag
- **วาง** = place/drop (the standard term)
- **ปล่อย** = release
- ❌ "drag" / "drop" (English) — wrong, except in casual tech speak

```
✅ ลากไฟล์มาที่นี่               (drag files here)
✅ ลากและวางที่นี่                (drag and drop here)
✅ เลือกไฟล์หรือลากและวางที่นี่   (select file or drag and drop here)
❌ Drag ไฟล์
❌ เลือกไฟล์หรือลาก  (incomplete — must complete the phrase)
```

### Error Messages — Polite, Indirect

Thai culture values face-saving. Direct accusations are softened:

| Wrong (direct) | Correct (indirect/polite) |
|---|---|
| คุณผิด | **ขออภัย อาจมีข้อผิดพลาด** (Apologies, there may be an error) |
| ทำไม่ถูก | **กรุณาลองอีกครั้ง** (Please try again) |
| รหัสผ่านผิด | **รหัสผ่านไม่ถูกต้อง** (Password incorrect — less accusatory) |

### UI Label Completeness (severity 1.0)

Thai UI labels should be COMPLETE descriptive phrases, not abbreviated nominal heads:

| Wrong (incomplete) | Correct (complete) | English |
|---|---|---|
| การตรวจจับทางเลือก | **วิธีการตรวจจับทางเลือก** | Alternative detection method |
| การบันทึกอัตโนมัติ | **การตั้งค่าการบันทึกอัตโนมัติ** | Auto-save settings |

## Punctuation, Numbers, Dates, Currency

### Quotation Marks
- Thai uses standard double quotes `"..."` or sometimes angle quotes `«...»`
- No special "Thai quote marks"
- Curly or straight double quotes are both acceptable

### Numbers
- Decimal separator: **period** (3.14)
- Thousands separator: **comma** (100,000)
- Format: `1,234,567.89`
- ❌ 1.234.567,89 (European) → ✅ 1,234,567.89

Thai numerals (๐, ๑, ๒, ๓, ๔, ๕, ๖, ๗, ๘, ๙) exist but are rarely used in modern UI. Latin/Arabic numerals are standard.

### Dates — DD/MM/YYYY (with Buddhist Era option)

**Buddhist Era (BE / พ.ศ.)** is +543 years from CE/AD:
- CE 2024 = BE 2567
- CE 2025 = BE 2568

| Form | Example | Meaning |
|---|---|---|
| Numeric BE | **15/01/2567** | 15 Jan 2024 BE format |
| Numeric CE | **15/01/2024** | 15 Jan 2024 CE format (international) |
| Word form BE | **15 มกราคม 2567** | 15 January BE |
| Long BE | **วันที่ 15 มกราคม พ.ศ. 2567** | Date 15 January B.E. 2567 |
| Word form CE | **15 มกราคม 2024 / ค.ศ. 2024** | (CE marked explicitly) |

**For international products / tech UI: use CE (2024)**. For traditional/government-facing Thai contexts: BE (2567). When in doubt, **state which era explicitly** if the year could be ambiguous.

Months (always lowercase):
| English | Thai (full) | Thai (abbrev) |
|---|---|---|
| January | มกราคม | ม.ค. |
| February | กุมภาพันธ์ | ก.พ. |
| March | มีนาคม | มี.ค. |
| April | เมษายน | เม.ย. |
| May | พฤษภาคม | พ.ค. |
| June | มิถุนายน | มิ.ย. |
| July | กรกฎาคม | ก.ค. |
| August | สิงหาคม | ส.ค. |
| September | กันยายน | ก.ย. |
| October | ตุลาคม | ต.ค. |
| November | พฤศจิกายน | พ.ย. |
| December | ธันวาคม | ธ.ค. |

### Time
- 24-hour: `14:30 น.` (น. = นาฬิกา = o'clock marker; optional in tech UI)
- Word form: `บ่ายสองโมงครึ่ง` (2:30 PM in traditional Thai 6-hour cycle)
- For UI, prefer **`14:30`** (international 24-hour, no marker needed)

### Currency: THB Baht
- **Thailand uses the baht (฿ / THB).** Symbol BEFORE amount.
- Format: `฿1,000` or `1,000 บาท`
- Subdivision: 100 satang (สตางค์) — rarely used in everyday UI
- ❌ 1.000,00 ฿ → ✅ 1,000.00 ฿ or **฿1,000**
- ❌ $100 → ✅ **฿3,500** (or whatever THB equivalent — use Baht for Thai users)

### Comma in Sentences

Thai sentences typically **do NOT use commas internally** the way English does. Clause boundaries are marked by:
- **Spaces** (where English uses commas)
- Particles like `แล้ว` (then), `และ` (and), `หรือ` (or), `แต่` (but)

Don't insert commas mid-sentence in Thai.

## Terminology

| English | Preferred Thai | Avoid |
|---|---|---|
| Email | อีเมล | จดหมายอิเล็กทรอนิกส์ (verbose) |
| Update | อัปเดต | ปรับปรุง (in modern tech contexts) |
| Website | เว็บไซต์ | |
| Privacy | ความเป็นส่วนตัว | |
| Contact | ติดต่อ | |
| Save | บันทึก | |
| Delete | ลบ | |
| Cancel | ยกเลิก | |
| Upload | อัปโหลด | |
| Download | ดาวน์โหลด | |
| Settings | การตั้งค่า / ตั้งค่า | |
| Search | ค้นหา | |
| Edit | แก้ไข | |
| Copy | คัดลอก | |
| Paste | วาง | |
| Close | ปิด | |
| Open | เปิด | |
| File | ไฟล์ | |
| Folder | โฟลเดอร์ | |
| User | ผู้ใช้ | |
| Password | รหัสผ่าน | |
| Username | ชื่อผู้ใช้ | |
| Log in | เข้าสู่ระบบ / ล็อกอิน | |
| Log out | ออกจากระบบ / ล็อกเอาต์ | |
| Dashboard | แดชบอร์ด | |
| Account | บัญชี | |
| Click | คลิก | |
| Submit | ส่ง | |
| Loading | กำลังโหลด | |

**Modern Thai is loanword-friendly for tech.** Anglicism transliterations like `อีเมล`, `อัปเดต`, `แดชบอร์ด`, `ดาวน์โหลด`, `อัปโหลด`, `คลิก` are PREFERRED over native calques like `จดหมายอิเล็กทรอนิกส์`. Don't over-translate.

**Proper noun abbreviations in UI:**
- ✅ **สหรัฐฯ** (with mai yamok `ฯ`) / **อเมริกา** (NOT "สหรัฐอเมริกา" in cramped UI)
- ✅ **สหราชอาณาจักร** / **อังกฤษ** (NOT the full official name)
- ✅ **ไทย** for Thailand in informal UI
- ✅ **ญี่ปุ่น** (Japan), **เกาหลี** (Korea), **จีน** (China), **เยอรมัน** / **เยอรมนี** (Germany)

**Brand names**: Keep in original form for global brands (Apple, Google, Microsoft, Facebook). Don't transliterate established global brand names.

## List Parallelism (severity 1.5)

When a list contains multiple items of the same semantic category (language names, file types, country names), **ALL items must use the same grammatical form**:

| Wrong (mixed) | Correct (parallel) | Reason |
|---|---|---|
| แปลเป็นภาษาเยอรมัน ฟินแลนด์ หรือไทย | **แปลเป็นภาษาเยอรมัน ภาษาฟินแลนด์ หรือภาษาไทย** | Either all use "ภาษา" prefix... |
| | **แปลเป็นเยอรมัน ฟินแลนด์ หรือไทย** | ...or none does. Don't mix. |
| ไฟล์ PDF, เวิร์ด, หรือ excel | **ไฟล์ PDF, Word, หรือ Excel** | Don't mix transliteration with original |

Apply this rule wherever list items share a category.

## Calque / Anti-Pattern Blocklist

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| มันสมเหตุสมผล | **เข้าใจได้ / มีเหตุผล** | "it makes sense" |
| ตอนท้ายวัน | **ในที่สุด / สรุปแล้ว** | "at the end of the day" |
| ไม่จริงๆ | **จริงๆ แล้วไม่ใช่ / ไม่ใช่เลย** | "not really" |
| 25+ ภาษา | **มากกว่า 25 ภาษา / กว่า 25 ภาษา** | "25+ languages" |
| +{count} เพิ่มเติม | **และอีก {count} ภาษา** | "+{count} more" |
| {min} ตัวอักษรยาว | **อย่างน้อย {min} ตัวอักษร** | "{min} characters long" |
| 5 นาทียาว | **5 นาที** | "5 minutes long" (length implicit) |
| ใหม่ไฟล์ | **ไฟล์ใหม่** | English adjective-first order |
| ถูกบันทึกโดยระบบ | **ระบบบันทึก / บันทึกแล้ว** | "was saved by the system" |
| ทำให้ดีที่สุด | **ทำให้ดีที่สุด** (acceptable) | "make best" |
| ออฟฟิศ | **ที่ทำงาน / สำนักงาน** | Optional — borrowed but native is also fine |

## Self-Check Checklist

Run BEFORE finalizing each translation:

**Accuracy (critical):**
- [ ] **NO spaces between Thai words** (ยินดีต้อนรับ, NOT ยินดี ต้อนรับ)
- [ ] **Space around colon** (อีเมล : user@example.com)
- [ ] **All tone marks present** (◌่ ◌้ ◌๊ ◌๋)
- [ ] **All vowel marks present** (เ-, แ-, โ-, -ิ, -ี, -ึ, -ื, etc.)
- [ ] **Classifier used** when counting (5 คน, 3 ไฟล์, 10 รายการ)
- [ ] **Self-classifying nouns** correctly handled (5 ภาษา, NOT 5 คน ภาษา)
- [ ] **Modifier AFTER head word** (ไฟล์ใหม่, NOT ใหม่ไฟล์)
- [ ] **No colloquial shortenings** (ไม่ได้ not มะได้, อะไร not ไร, เท่านั้น not แค่นั้น)
- [ ] **Date format consistent** (DD/MM/YYYY; specify BE/CE when ambiguous)
- [ ] **Number format:** comma thousands, period decimal (1,000.00)
- [ ] **Currency:** ฿ baht (NOT dollars)
- [ ] **List parallelism:** all items same form (all "ภาษา X" or none)
- [ ] **Placeholders preserved** exactly

**Naturalness:**
- [ ] **No ครับ/ค่ะ in UI buttons or labels** (only in conversational text)
- [ ] **Pronoun คุณ for UI** (NOT เธอ which is intimate)
- [ ] **Buttons concise** (บันทึก, ยกเลิก, ลบ — NOT กรุณาบันทึกครับ)
- [ ] **Status with กำลัง + ellipsis** (กำลังโหลด...)
- [ ] **Completion marked with แล้ว** (บันทึกแล้ว, เสร็จแล้ว)
- [ ] **Active voice** preferred over ถูก passive
- [ ] **Drag-and-drop:** ลาก, วาง (NOT drag, drop)
- [ ] **Phrase completeness:** complete or-clauses (หรือลากและวางที่นี่)
- [ ] **Error messages face-saving:** indirect language (ขออภัย อาจมีข้อผิดพลาด)
- [ ] **Tech loanwords preferred** for modern tech (อีเมล, อัปเดต, แดชบอร์ด)
- [ ] **UI labels complete** (วิธีการตรวจจับทางเลือก, not just การตรวจจับ)
- [ ] **Abbreviations in UI** (สหรัฐฯ not สหรัฐอเมริกา)
- [ ] **Brand names in original** (Apple, Google — not transliterated)
- [ ] **No redundant modifiers** (5 นาที not 5 นาทียาว)

## Worked Examples

### Example 1 — Save button + status

**Source:**
> Save  
> Saving your changes...  
> Changes saved.

**Wrong:**
> กรุณาบันทึกครับ (polite particle on button)  
> โหลด การเปลี่ยนแปลง ของ คุณ (English-style spacing — broken)  
> การเปลี่ยนแปลง ถูก บันทึก แล้ว (passive + spacing)

**Correct:**
> **บันทึก** (clean button — no particle)  
> **กำลังบันทึกการเปลี่ยนแปลง...** (กำลัง + ongoing, no spaces between Thai words)  
> **บันทึกการเปลี่ยนแปลงแล้ว** (active + แล้ว completion)

### Example 2 — Spacing catastrophe

**Source:**
> You can delete the file from settings.

**Wrong (English-style spacing — broken):**
> คุณ สามารถ ลบ ไฟล์ ได้ จาก การ ตั้ง ค่า

**Correct (no spaces between Thai words):**
> **คุณสามารถลบไฟล์ได้จากการตั้งค่า**

### Example 3 — Drag-and-drop area

**Source:**
> Drag and drop files here, or click to browse

**Wrong:**
> Drag files ที่นี่ หรือ click เพื่อ browse (anglicism + English spacing)

**Correct:**
> **ลากและวางไฟล์ที่นี่หรือคลิกเพื่อเรียกดู** (native verbs, no internal spaces)

### Example 4 — Adjective order

**Source:**
> New feature / Good quality / Easy interface

**Wrong:**
> ใหม่ฟีเจอร์ / ดีคุณภาพ / ง่ายอินเทอร์เฟซ (English order)

**Correct:**
> **ฟีเจอร์ใหม่** / **คุณภาพดี** / **อินเทอร์เฟซง่าย** (modifier after head)

### Example 5 — Classifier

**Source:**
> 5 users / 10 files / 3 languages / 2 cars

**Wrong:**
> 5 ผู้ใช้ / 10 / 3 คน ภาษา / 2 รถ (no classifier; wrong classifier for language)

**Correct:**
> **ผู้ใช้ 5 คน** / **10 ไฟล์** (self-classifying) / **3 ภาษา** (self-classifying) / **รถ 2 คัน**

### Example 6 — Active over passive

**Source:**
> The file was saved by the system.

**Wrong (passive):**
> ไฟล์ถูกบันทึกโดยระบบ

**Correct (active):**
> **ระบบบันทึกไฟล์แล้ว** (system saved file)
> **บันทึกไฟล์แล้ว** (saved the file — agent dropped)

### Example 7 — Buttons without particles

**Source:**
> Save / Cancel / Delete

**Wrong:**
> กรุณาบันทึกครับ / กรุณายกเลิกค่ะ / กรุณาลบครับ

**Correct:**
> **บันทึก** / **ยกเลิก** / **ลบ**

### Example 8 — Colon spacing

**Source:**
> Email: user@example.com

**Wrong (no spaces around colon):**
> อีเมล:user@example.com

**Correct (spaces around colon):**
> **อีเมล : user@example.com**

### Example 9 — List parallelism

**Source:**
> Translate to German, Finnish, or Thai

**Wrong (mixed forms):**
> แปลเป็นภาษาเยอรมัน ฟินแลนด์ หรือไทย (first uses ภาษา prefix; others bare)

**Correct (all with ภาษา prefix):**
> **แปลเป็นภาษาเยอรมัน ภาษาฟินแลนด์ หรือภาษาไทย**

**Or (all without prefix):**
> **แปลเป็นเยอรมัน ฟินแลนด์ หรือไทย**

### Example 10 — Date and currency

**Source:**
> January 15, 2024 — Total: $100

**Wrong:**
> 01/15/2024 — $100 (US date + dollars)

**Correct (CE for international product):**
> **15/01/2024** — **ยอดรวม: ฿3,500** (or whatever THB equivalent)

**Correct (BE for traditional Thai context):**
> **15 มกราคม 2567** — **ยอดรวม: ฿3,500**

### Example 11 — Polite pronoun

**Source:**
> You can change your settings.

**Wrong (intimate pronoun):**
> เธอสามารถเปลี่ยนการตั้งค่าได้

**Correct (polite pronoun):**
> **คุณสามารถเปลี่ยนการตั้งค่าได้**

### Example 12 — UI label completeness

**Source:**
> Alternative detection (menu label for a sub-options screen)

**Wrong (incomplete):**
> การตรวจจับทางเลือก (just "alternative detection" — sounds like a fragment)

**Correct (complete):**
> **วิธีการตรวจจับทางเลือก** (alternative detection method — complete noun phrase)

## When in Doubt

1. **Spacing between Thai words?** NEVER. Run them together. Use spaces only at clause/sentence breaks.
2. **Space around colon?** YES — both sides (อีเมล : x@y.com).
3. **Tone mark uncertain?** Look up the word. NEVER guess — Thai is full of minimal pairs distinguished only by tone.
4. **Classifier?** Identify the noun class:
   - People → คน
   - Animals → ตัว
   - Vehicles → คัน
   - Books → เล่ม
   - Flat → แผ่น, ใบ
   - General objects → อัน
   - Languages, files, items → self-classifying (no extra classifier needed)
5. **Adjective placement?** Always AFTER the noun.
6. **Pronoun?** Default to คุณ for product UI. ท่าน for premium/banking. NEVER เธอ.
7. **Buttons with ครับ/ค่ะ?** No. Polite particles are for conversation, not UI controls.
8. **Status message?** Use กำลัง + verb + ellipsis (กำลังโหลด...). Completion → แล้ว (บันทึกแล้ว).
9. **Date — BE or CE?** International product or modern tech → CE (2024). Government / traditional / older audience → BE (2567). When ambiguous, label explicitly.
10. **Translate or transliterate tech term?** Modern Thai prefers transliterations for tech (อีเมล, อัปโหลด, ดาวน์โหลด, แดชบอร์ด, คลิก). Don't over-translate.
11. **Currency?** ฿ baht for Thai users. Never dollars.
12. **List parallelism?** Audit lists for consistent grammatical form. Either all items use "ภาษา X" or none do.

Thai's isolating grammar means almost all translation errors are at the **typographic and word-choice level**, not morphology. When the translation feels off, check: (a) no spaces between Thai words, (b) space around colon, (c) all tone/vowel marks present, (d) classifier present, (e) modifier after head, (f) pronoun is คุณ not เธอ, (g) no polite particle on buttons.
