---
name: localize-vi
description: "Use when translating UI strings, marketing copy, blogs, docs, error messages, or any product text (originally in any source language) into Vietnamese (Tiếng Việt) for Vietnam. Vietnamese is an isolating language — NO grammatical gender, NO number agreement, NO case system, NO verb conjugation. Critical features include the SIX-TONE diacritic system (Cảm ơn bạn — never strip tone marks; severity 3.0), classifier system before counted nouns (một cái bàn, một con mèo, một người, một quyển sách), pronoun-based formality with bạn as the UI default (Quý khách for very formal, Anh/Chị for polite, bạn for standard, no casual pronouns in product UI), adjective-AFTER-noun word order (tệp mới NOT mới tệp — opposite of English), softening particles (nhé friendly, nhá gentle, ạ respectful — but NOT in buttons), progressive form with `đang` for status messages (Đang tải... NOT just Tải), active voice over `được` passive, DD/MM/YYYY dates, VND currency (100.000₫ with period thousands), no comma before hoặc/hay/và, and rejection of colloquial shortenings in professional UI (không not hông, rồi not rùi, này not nè, không not hổng)."
---

# Localize: Vietnamese (vi → Tiếng Việt)

You are translating source text into Vietnamese for Vietnam. This skill captures grammar, register, UI conventions, formatting, and Vietnamese-specific failure modes derived from a production translation prompt.

## Scope & Variants

**One standard with regional flavors:**
- **vi-VN** — Vietnamese as used in Vietnam. Official state language.

**Regional varieties:**
- **Northern (Hanoi)** — more formal, conservative vocabulary, standard pronunciation for media. **Use as default for UI.**
- **Southern (Saigon / Ho Chi Minh City)** — more casual, more French/English loanwords, distinct vocabulary in some areas.
- **Central** — distinct in spoken language; rarely a written-language target.

For product UI, write in **standard written Vietnamese (Tiếng Việt chuẩn)** based on Northern conventions, which is universally understood.

**Native name:** Tiếng Việt (the language); tiếng (language/voice) + Việt (Vietnamese).

**Identity guardrail:**
- Vietnamese is **Austroasiatic (Mon-Khmer family)**, NOT Chinese (Sino-Tibetan) and NOT Thai (Tai-Kadai). Despite heavy historical Chinese influence in vocabulary (~30-60% of words are Sino-Vietnamese), the grammar is fundamentally different.
- Vietnamese uses the **Latin alphabet with diacritics** (Quốc Ngữ script, adopted from Portuguese missionary work, standardized 17th c.). It does NOT use Chinese characters anymore (Chữ Hán/Nôm was phased out).
- Vietnamese is **isolating** — no inflections, no gender, no number. Words don't change form. Grammar is conveyed by word order, function words, and tones.

## Register

**Default level: `bạn` (standard polite)** for software UI, errors, documentation, marketing aimed at general consumers.

Vietnamese formality is expressed through **pronoun choice** (not verb conjugation, which doesn't exist):

| Level | Pronoun | Use case |
|---|---|---|
| Very formal | **Quý khách / Quý vị** | Banking, premium services, official announcements |
| Polite | **Anh / Chị** | Customer service to slightly older person, formal email |
| **Standard (UI default)** | **bạn** | Most product UI, peer-to-peer messages |
| Casual / familiar | (varies by age/relationship) | NOT for UI |
| Intimate | em / anh / chị / mày / tao | NEVER in UI |

**Rules:**
- Choose ONE pronoun level per file. Don't switch between `bạn` and `Quý khách`.
- Match softening particles to formality (`ạ` with formal, `nhé` with friendly).
- Avoid colloquial forms in professional UI: `hông` (= không, no), `rùi` (= rồi, already), `nè` (= này, this), `dzậy` (= vậy).

**Examples:**
- ❌ "Quý khách nhấn vào đây nhé" (very formal Quý khách + casual nhé) → ✅ "**Quý khách vui lòng nhấn vào đây**" (or use `bạn` throughout)
- ❌ "hông được" → ✅ "**không được**"
- ❌ "rùi" → ✅ "**rồi**"
- ❌ "nè" → ✅ "**này**"

## Critical Hard Rules

### Tone Marks (severity 3.0)

**Vietnamese has 6 tones, all marked by diacritics.** Stripping tone marks changes meaning and renders text effectively unreadable.

| Tone | Mark | Vietnamese | Example |
|---|---|---|---|
| Level (ngang) | (none) | ma | ghost |
| Falling (huyền) | ` (grave) | mà | but |
| Rising (sắc) | ´ (acute) | má | mother |
| Dipping-rising (hỏi) | ̉ (hook above) | mả | grave |
| Glottalized rising (ngã) | ˜ (tilde) | mã | code |
| Heavy/falling-short (nặng) | ̣ (dot below) | mạ | rice seedling |

**One word, 6 meanings.** Stripping is catastrophic.

**Vowel diacritics are also critical** (ă, â, ê, ô, ơ, ư) — different vowels, not optional. Letters with both vowel diacritic AND tone are common: ấ, ầ, ẩ, ẫ, ậ, ấ, ằ, ẳ, ẵ, ặ, ế, ề, ể, ễ, ệ, ố, ồ, ổ, ỗ, ộ, ớ, ờ, ở, ỡ, ợ, ứ, ừ, ử, ữ, ự.

| Wrong (stripped) | Correct | Meaning |
|---|---|---|
| Cam on ban | **Cảm ơn bạn** | Thank you |
| Luu y | **Lưu ý** | Note |
| Tai len | **Tải lên** | Upload |
| Mat khau | **Mật khẩu** | Password |
| Tieng Viet | **Tiếng Việt** | Vietnamese |

**NEVER omit diacritics in formal/UI text.** ASCII-Vietnamese exists in casual chat but is unacceptable in product UI.

### Classifier System (Loại từ) (severity 2.0)

**Vietnamese requires a classifier before a counted noun.** Bare numbers + nouns are ungrammatical (with some exceptions).

| Classifier | Used for | Example |
|---|---|---|
| **cái** | general objects, things | một **cái** bàn (a table), hai **cái** ghế (two chairs) |
| **con** | animals, some objects (knives, rivers, boats) | một **con** mèo (a cat), một **con** dao (a knife) |
| **người** | people | một **người** (a person), năm **người** (five people) |
| **quyển / cuốn** | books, magazines, notebooks | một **quyển** sách (a book) |
| **tờ** | flat objects, paper, newspapers | một **tờ** giấy (a sheet of paper), một **tờ** báo |
| **chiếc** | vehicles, some objects | một **chiếc** xe (a vehicle), một **chiếc** áo |
| **bộ** | sets, collections | một **bộ** quần áo (an outfit) |
| **cây** | trees, long objects | một **cây** bút (a pen) |
| **viên** | small round/lumpy objects | một **viên** đá (a stone), một **viên** thuốc (a pill) |
| **bức** | flat artworks | một **bức** tranh (a painting) |

**No classifier needed** for:
- Inherent counted nouns: `ngôn ngữ` (language), `tệp` (file), `phút` (minute), `nước` (country)
- `{count} ngôn ngữ` ✓ (no classifier needed)
- `{count} tệp` ✓ (no classifier needed for "file" in UI usage)

**Plural markers (`các`, `những`) are OMITTED with numbers:**
- ✅ "{count} tệp" (not "{count} các tệp")
- ✅ "5 ngôn ngữ" (not "5 các ngôn ngữ")
- ✅ "các tệp" (when no count: general "the files")

### Adjective-After-Noun Word Order (severity 2.0)

**Vietnamese places modifiers AFTER the head word**, opposite of English.

| Wrong (English order) | Correct (Vietnamese) | English |
|---|---|---|
| **mới** tệp | **tệp mới** | new file |
| **đẹp** nhà | **nhà đẹp** | beautiful house |
| **mới** tính năng | **tính năng mới** | new feature |
| **cao** tốc độ | **tốc độ cao** | high speed |
| **tốt** chất lượng | **chất lượng tốt** | good quality |
| **xanh** áo | **áo xanh** | blue shirt |

This applies to:
- Adjectives (tệp **mới**)
- Possessives (nhà **của tôi** — house of mine)
- Relative clauses (tệp **mà bạn đã chọn** — file that you selected)
- Demonstratives (tệp **này** — this file, tệp **đó** — that file)

### Active Voice over Passive (severity 1.5)

Vietnamese overuses `được` (passive marker) creates stiff, translation-y text. Prefer **active voice**.

| Wrong (passive) | Correct (active) |
|---|---|
| File **được lưu** bởi hệ thống | **Hệ thống đã lưu** file / **File đã lưu** |
| Tệp **được tải lên** bởi người dùng | **Người dùng đã tải lên** tệp |
| Email **được gửi** | **Đã gửi email** |
| Thông báo **được tạo** | **Đã tạo thông báo** |

`được` IS appropriate when:
- The agent is unknown / irrelevant
- Expressing positive permission: "Bạn **được phép** truy cập" (you are allowed to access)
- After verbs of allowance: cho phép, cấp

### Progressive Form with `đang` (severity 1.5)

For ongoing/loading actions, use **`đang` + verb** — not the bare verb.

| Wrong | Correct | English |
|---|---|---|
| Tải... | **Đang tải...** | Loading... |
| Lưu... | **Đang lưu...** | Saving... |
| Xử lý... | **Đang xử lý...** | Processing... |
| Kết nối... | **Đang kết nối...** | Connecting... |
| Tìm kiếm... | **Đang tìm kiếm...** | Searching... |

`đang` marks ongoing action (present continuous). Without it, the bare verb reads as imperative or generic.

### No-Plural-Marker Rule

Vietnamese has plural markers `các` (definite plural) and `những` (indefinite plural), but:
- They're **omitted with explicit numbers** (5 tệp, NOT 5 các tệp)
- They're **omitted in most counting/quantity contexts**
- They appear in general "the X" references: "**các** tệp đã chọn" (the selected files)

## UI Conventions

### Button Labels — Concise Imperative

Vietnamese buttons use **short imperatives** without polite prefixes:

| Wrong (with hãy/polite prefix) | Correct (concise) | English |
|---|---|---|
| Hãy lưu lại | **Lưu** | Save |
| Hãy xóa | **Xóa** | Delete |
| Hãy hủy bỏ | **Hủy** | Cancel |
| Hãy tải lên | **Tải lên** | Upload |
| Hãy chọn | **Chọn** | Select |
| Hãy đóng | **Đóng** | Close |

(`Hãy` is a polite imperative marker — appropriate in instructions or polite requests, but bloats buttons.)

### Status Messages — `Đang + verb...`

```
✅ Đang tải...           (Loading...)
✅ Đang lưu...           (Saving...)
✅ Đang xử lý dữ liệu... (Processing data...)
✅ Đã lưu                (Saved — past completion)
✅ Đã sẵn sàng           (Ready)
❌ Tải                    (just "load" — sounds imperative)
❌ Đang được tải         (passive + đang — too stiff)
```

### Drag-and-Drop Vocabulary

- **kéo** = drag
- **thả** = drop / release
- ❌ "drag" / "drop" (English) — wrong

```
✅ Kéo tệp vào đây            (drag files here)
✅ Kéo và thả vào đây         (drag and drop here)
✅ Kéo thả tệp                (drag-drop files — compact)
❌ Drag tệp / Drop tại đây
```

### Error Messages — Natural Phrasing

| Wrong (calque) | Correct (natural) |
|---|---|
| Thất bại khi tải | **Không thể tải / Lỗi tải** |
| Lỗi khi lưu | **Không thể lưu / Lưu không thành công** |
| Thất bại để kết nối | **Không thể kết nối** |
| Lỗi xảy ra | **Đã xảy ra lỗi** (if needed; usually omit entirely) |

Pattern: `Không thể + [verb]` is the canonical "failed to X" structure.

### File Picker / Placeholder Handling

Vietnamese can suffix-free with placeholders (unlike Hungarian or Finnish), but add **type markers** for clarity when placeholders represent types/formats:

| Less clear | Preferred (with type marker) |
|---|---|
| Hỗ trợ tệp {formatList} | **Hỗ trợ tệp định dạng {formatList}** |
| Nội dung {languageList} | **Nội dung bằng {languageList} ngôn ngữ** |

Exception: simple quantity ({count} tệp) and established compounds (tệp JSON, tệp PDF) don't need markers.

### Softening Particles

Vietnamese uses sentence-final particles to soften tone:

| Particle | Use | Example |
|---|---|---|
| **nhé** | friendly suggestion | "Nhấn vào đây nhé" (Click here, ok?) |
| **nhá** | gentle confirmation | "Đúng rồi nhá" (That's right) |
| **ạ** | respectful (formal) | "Cảm ơn bạn ạ" (Thank you) |
| **chứ** | reinforcement | "Tốt chứ" (It's good, right?) |
| **đi** | mild imperative | "Làm đi" (Just do it) |
| **với** | "too" / "along with" | "Tôi với" (Me too) |

**Match particle to register:**
- Formal (Quý khách) → `ạ`
- Standard (bạn) → no particle or mild `nhé` in friendly messages
- DO NOT add particles in buttons or terse UI labels — they bloat the UI

## Punctuation, Numbers, Dates, Currency

### Quotation Marks
- **Vietnamese uses standard double quotes** `"..."` or angle quotes `«...»`
- Less commonly, single quotes
- No special "Vietnamese quote marks" — straight or curly double quotes are standard

### Numbers
- Decimal separator: **comma** (3**,**14)
- Thousands separator: **period** (100**.**000)
- Format: `1.234.567,89`
- ❌ 1,234.56 (US) → ✅ 1.234,56

### Dates — DD/MM/YYYY
- Numeric: **15/01/2024** (slashes)
- Word form: **15 tháng 1, 2024** or **ngày 15 tháng 1 năm 2024** (day-month-year, "tháng" = month, "năm" = year)
- ❌ 01/15/2024 (US) → ✅ 15/01/2024
- ❌ 2024-01-15 (ISO; acceptable in technical contexts but not customer-facing UI)

### Time
- 24-hour: `14:30`
- Word form: `2 giờ 30 chiều` (2:30 PM, chiều = afternoon) or `14 giờ 30` or `2 rưỡi chiều` (half past two PM)
- AM/PM equivalents: `sáng` (morning), `trưa` (noon), `chiều` (afternoon), `tối` (evening), `đêm` (night)

### Currency: VND đồng
- **Vietnam uses the đồng (₫ or VND).** NOT in any monetary union.
- Format: `100.000₫` or `100,000 VND` (period thousands, ₫ after, no decimals in casual use)
- The đồng is heavily inflated; sub-1000 amounts are essentially absent from UI
- ❌ $100 → ✅ 100.000₫ (use VND, NOT dollars)
- ❌ 100.000 đồng (verbose in UI) — acceptable in body text but `100.000₫` for compact UI

### Comma Rules

**NO comma before coordinating conjunctions** (hoặc, hay, và, cũng như):
- ❌ "Kéo tệp vào đây, hoặc nhấp" → ✅ "Kéo tệp vào đây hoặc nhấp"
- ❌ "Lưu tệp, và đóng" → ✅ "Lưu tệp và đóng"

**Comma DOES go before subordinating clauses** (nếu, khi, vì, nhưng):
- "Nhấn vào đây, nếu bạn muốn tiếp tục"
- "Không hoạt động, vì tệp bị thiếu"
- "Đó là tệp nhỏ, nhưng quan trọng"

### Word Spacing

Vietnamese **DOES use spaces** between syllables (unlike Thai or Chinese). Each syllable is a separate "word" in writing:
- ✅ "Cảm ơn bạn" (three separated syllables)
- ❌ "Cảmơnbạn" (wrong)

**Compound words** are written as separated syllables: `máy tính` (computer), `điện thoại` (phone), `phần mềm` (software). Don't fuse them.

## Terminology

| English | Preferred Vietnamese | Avoid |
|---|---|---|
| Save | Lưu | |
| Delete | Xóa | |
| Cancel | Hủy | Hủy bỏ (verbose) |
| Upload | Tải lên | Upload (English) |
| Download | Tải xuống | Download |
| Settings | Cài đặt | Thiết lập (less common in modern UI) |
| Search | Tìm kiếm | |
| Edit | Chỉnh sửa | Edit |
| Copy | Sao chép | Copy (use in some contexts) |
| Paste | Dán | |
| Close | Đóng | |
| Open | Mở | |
| File | Tệp / tập tin / file | (file is also acceptable in tech context) |
| Folder | Thư mục | |
| User | Người dùng | |
| Password | Mật khẩu | |
| Email | Email / Thư điện tử | (Email is preferred in modern UI) |
| Username | Tên đăng nhập | |
| Log in | Đăng nhập | |
| Log out | Đăng xuất | |
| Dashboard | Bảng điều khiển | |
| Account | Tài khoản | |
| Browser | Trình duyệt | |
| Click | Nhấp / nhấn / bấm | |
| Submit | Gửi | |
| Loading | Đang tải | |

**Proper noun abbreviations in UI:**
- ✅ "Mỹ" / "Hoa Kỳ" (NOT "Hợp chúng quốc Hoa Kỳ" in cramped UI)
- ✅ "Anh" / "Vương quốc Anh" (NOT "Vương quốc Liên hiệp Anh và Bắc Ireland")
- ✅ "Úc" (NOT "Ô-xtrây-li-a" — old transliteration, sounds archaic)
- ✅ "Đức" (Germany), "Nhật" (Japan), "Hàn" (Korea), "Trung Quốc" (China)

**Tech English tolerance:** Modern Vietnamese tolerates well-established English tech terms (email, app, online, wifi, link, ID, OK). Don't over-translate these.

## Calque / Anti-Pattern Blocklist

| Wrong (calque) | Correct (idiomatic) | Source |
|---|---|---|
| Nó có nghĩa | **Điều này hợp lý / Có lý** | "it makes sense" |
| Vào cuối ngày | **Cuối cùng / Suy cho cùng** | "at the end of the day" |
| Không thực sự | **Thực ra không phải / Không hẳn** | "not really" |
| Lấy một nghỉ | **Nghỉ ngơi** | "take a break" |
| Gãy chân đi | **Chúc may mắn!** | "break a leg" |
| Miếng bánh | **Dễ như trở bàn tay / Dễ ợt** | "piece of cake" |
| 25+ ngôn ngữ | **hơn 25 ngôn ngữ / trên 25 ngôn ngữ** | "25+ languages" |
| +{count} thêm | **và {count} khác / thêm {count}** | "+{count} more" |
| {min} ký tự dài | **ít nhất {min} ký tự** | "{min} characters long" |
| 5 phút dài | **5 phút** | "5 minutes long" (length is implicit) |
| Thất bại khi tải | **Không thể tải / Lỗi tải** | "failed to load" |
| Lỗi khi lưu | **Không thể lưu** | "error saving" |
| File được lưu | **Đã lưu file / File đã lưu** | "the file was saved" (passive→active) |

## Question Particles

Vietnamese questions don't change word order. They use sentence-final particles or question words:

| Form | Pattern | Example |
|---|---|---|
| Yes/no question | sentence + **không?** | "Bạn có muốn lưu không?" (Do you want to save?) |
| Or-question | A + **hay** + B | "Lưu hay hủy?" (Save or cancel?) |
| Wh-question | WH-word in question position | "Tệp ở đâu?" (Where is the file?) |
| Tag question | sentence + **đúng không? / phải không?** | "Tệp đã lưu, đúng không?" |

## Self-Check Checklist

Run BEFORE finalizing each translation:

**Accuracy (critical):**
- [ ] **All tone marks present** (Cảm ơn bạn, not Cam on ban) — never strip
- [ ] **Vowel diacritics present** (ă, â, ê, ô, ơ, ư + combined with tones)
- [ ] **Classifier used** when counting nouns (một cái bàn, một con mèo, một quyển sách); BUT no classifier for inherent counts (5 ngôn ngữ, 3 tệp)
- [ ] **Adjective AFTER noun** (tệp mới, NOT mới tệp)
- [ ] **No plural marker with numbers** (5 tệp, NOT 5 các tệp)
- [ ] **Active voice** preferred over `được` passive
- [ ] **`đang` for ongoing actions** (Đang tải..., NOT just Tải)
- [ ] **Pronoun consistency** — same level throughout (bạn OR Quý khách, not both)
- [ ] **No colloquial shortenings** in UI (không not hông, rồi not rùi, này not nè)
- [ ] **Date format:** DD/MM/YYYY (15/01/2024)
- [ ] **Number format:** period thousands, comma decimal (1.234,56)
- [ ] **Currency:** VND đồng (100.000₫), NOT dollars
- [ ] **No comma before hoặc/hay/và**
- [ ] **Word spacing:** Vietnamese DOES space between syllables (Cảm ơn bạn, not Cảmơnbạn)
- [ ] **Placeholders preserved** exactly

**Naturalness:**
- [ ] **Buttons concise** (Lưu, Xóa, Hủy — not Hãy lưu lại)
- [ ] **Status with đang + ellipsis** (Đang tải...)
- [ ] **Drag-and-drop:** kéo, thả (NOT drag, drop)
- [ ] **Error messages:** Không thể + verb (NOT Thất bại khi)
- [ ] **Native verb preference** when standard equivalent exists
- [ ] **Tech English tolerated** (email, app, wifi, online, link)
- [ ] **No `được` overuse** — convert passive to active
- [ ] **Quantity expressions natural** (hơn 25, NOT 25+)
- [ ] **No redundant modifiers** (5 phút not 5 phút dài)
- [ ] **Softening particles match formality** (ạ formal, nhé friendly; none in buttons)
- [ ] **Abbreviations in UI** (Mỹ not Hoa Kỳ Hợp chúng quốc; Úc not Ô-xtrây-li-a)
- [ ] **`tháng 1` not `January`** in dates
- [ ] **Type markers when helpful** (tệp định dạng {formatList})

## Worked Examples

### Example 1 — Save button + status

**Source:**
> Save  
> Saving your changes...  
> Changes saved.

**Wrong:**
> Hãy lưu lại (verbose)  
> Lưu thay đổi của bạn... (bare verb — sounds imperative)  
> Thay đổi đã được lưu. (overused được passive)

**Correct:**
> **Lưu** (concise imperative button)  
> **Đang lưu thay đổi...** (đang + ellipsis)  
> **Đã lưu thay đổi.** (đã = past marker, active)

### Example 2 — Files counter

**Source:**
> 1 file / 5 files / 25 files

**Vietnamese has no plural agreement:**
> **1 tệp** / **5 tệp** / **25 tệp** (singular form used throughout — Vietnamese has no plural inflection)

ICU plural for Vietnamese is trivial — only `other`:
```icu
{count, plural,
  other {# tệp}
}
```

### Example 3 — Drag-and-drop area

**Source:**
> Drag and drop files here, or click to browse

**Wrong:**
> Drag và drop tệp vào đây, hoặc click để duyệt (anglicism + comma before hoặc)

**Correct:**
> **Kéo và thả tệp vào đây hoặc nhấp để duyệt** (native verbs, no comma before hoặc)

### Example 4 — Tone-mark catastrophe

**Source:**
> Welcome to your account

**Wrong:**
> Chao mung den tai khoan cua ban (stripped — looks like random Latin letters)

**Correct:**
> **Chào mừng đến tài khoản của bạn** (all tones present)

### Example 5 — Adjective order

**Source:**
> New feature / Beautiful design / High speed

**Wrong:**
> Mới tính năng / Đẹp thiết kế / Cao tốc độ (English order)

**Correct:**
> **Tính năng mới** / **Thiết kế đẹp** / **Tốc độ cao** (adjective after noun)

### Example 6 — Classifier

**Source:**
> Buy a table / Save a book / 3 cats

**Wrong:**
> Mua một bàn / Lưu một sách / 3 mèo (no classifier)

**Correct:**
> **Mua một cái bàn** / **Lưu một quyển sách** / **3 con mèo** (with classifier)

(But: "**5 ngôn ngữ**" with no classifier — inherent count.)

### Example 7 — Active over passive

**Source:**
> The file was saved by the system. / Email was sent.

**Wrong (passive):**
> File được lưu bởi hệ thống. / Email được gửi.

**Correct (active):**
> **Hệ thống đã lưu file.** / **Đã gửi email.** (more natural Vietnamese)

### Example 8 — Pronoun consistency

**Source:**
> Welcome! Click here to start. Need help?

**Wrong (mixed):**
> Chào Quý khách! Nhấp vào đây để bắt đầu nhé. Cần giúp đỡ không?

**Correct (consistent — using bạn):**
> **Chào bạn! Nhấp vào đây để bắt đầu. Cần giúp đỡ không?**

**Correct (consistent — using Quý khách):**
> **Chào Quý khách! Vui lòng nhấp vào đây để bắt đầu. Quý khách có cần hỗ trợ không?**

### Example 9 — Date and currency

**Source:**
> January 15, 2024 — Total: $99.99

**Wrong:**
> 01/15/2024 — $99.99 (US date, dollars)

**Correct:**
> **15/01/2024** (or **15 tháng 1, 2024**) — **Tổng: 2.500.000₫** (or whatever VND equivalent, using period thousands)

### Example 10 — Error message

**Source:**
> Failed to upload file.

**Wrong:**
> Thất bại khi tải lên tệp. (calque "failed when")

**Correct:**
> **Không thể tải lên tệp.** (Không thể + infinitive — natural)

## When in Doubt

1. **Tone uncertain?** Look up the word. Vietnamese is full of minimal pairs (ma/mà/má/mả/mã/mạ). NEVER guess.
2. **Vowel diacritic uncertain?** Check whether the vowel is ă/â/ê/ô/ơ/ư or the plain a/e/o/u. They are distinct phonemes, not stylistic.
3. **Classifier?** Identify the noun class (general object → cái, animal → con, person → người, book → quyển/cuốn, flat object → tờ). When counting "inherent count" nouns (ngôn ngữ, tệp, phút), no classifier needed.
4. **Pronoun?** Default to `bạn` for product UI. Upgrade to `Quý khách` only for premium/banking/very formal contexts. Stay consistent.
5. **Adjective placement?** Always AFTER the noun. Reverse English order.
6. **`đang` or not?** Use for ongoing action (status messages). Skip for completed (đã) or generic statements.
7. **`được` passive?** Almost always restructurable as active. Default to active unless the agent is genuinely unknown.
8. **Particle in UI label?** Almost never. Particles bloat. Keep buttons and status compact.
9. **Tech term — translate or keep English?** Established loans (email, app, online, wifi) stay. Native equivalents exist (lưu, xóa, tải) — use them for actions.
10. **Currency?** VND đồng, NEVER dollars. Use period thousands (100.000₫), not comma.
11. **Northern vs Southern?** Northern is the written standard. Use it unless explicitly targeting Southern audience.

Vietnamese's isolating grammar means almost all translation errors are at the **word-choice and word-order level**, not morphology. When the translation feels off, check: (a) tone marks present, (b) adjectives placed correctly, (c) classifier present, (d) active voice, and (e) pronoun consistency.
