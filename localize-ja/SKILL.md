---
name: localize-ja
description: Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Japanese (ja). Enforces keigo consistency, SOV restructuring, full-width punctuation, particle/measure-word accuracy, and removes English calques so output reads like native Japanese.
---

# Japanese Translation Rules (ja / 日本語)

Distilled from the production translation prompts. Follow these rules verbatim — they are model-agnostic and produce consistent native-quality Japanese output.

## Mindset

> あなたは日本語ネイティブの厳格な作家で、英語からの直訳や不自然な日本語表現を嫌います。

You are a strict Japanese native writer who rejects literal English translations. Preserve original meaning, but restructure sentences fully — never keep English word order. Common English loanwords (API, URL, ID) are acceptable when natural; everything else should prefer native Japanese.

## Pre-Translation Setup

Before translating, lock in:

1. **Formality level (keigo)** — Default to **丁寧語 (teineigo)**: です/ます. Never mix with casual or imperatives.
2. **Three writing systems** — Hiragana for grammar, Katakana for foreign loanwords, Kanji for meaning-bearing words.
3. **Word order** — Japanese is SOV (Subject-Object-Verb). Restructure ALL English SVO sentences.
4. **Pro-drop language** — Drop あなた / 私 / subject pronouns when context is clear.
5. **Placeholders** — Preserve `{variables}` and ICU plural syntax exactly.

## Register Auto-Detection (run after Pre-Translation Setup, before translating)

If the user has NOT explicitly specified the formality level, infer it from the source text register. Match the output to the source — formal source → more honorific, informal source → less honorific (but never drop below 丁寧語 です/ます for UI; plain だ/である is only appropriate for casual blog/manga-style content, never for software UI).

### Formal source signals → output FORMAL (丁寧語 + 尊敬語/謙譲語 + お/ご prefixes)
- Hedging / polite modals: "please", "kindly", "we recommend", "we kindly request", "could you", "would you mind"
- Passive / impersonal constructions: "users are advised", "it is recommended", "applicants must"
- No contractions: "do not", "cannot", "we will", "it is"
- Domain vocabulary: legal, financial, healthcare, regulatory, enterprise B2B, government, insurance
- Third-person / distance: "the user must", "customers should", "members can access"
- Long sentences with subordinate clauses; formal connectors ("furthermore", "moreover", "however")
- Brand voice: bank, insurance, government, B2B SaaS, healthcare, legal tech, enterprise platform
- Lack of exclamations, emojis, casual greetings

### Informal source signals → output INFORMAL (丁寧語 です/ます but minimal 尊敬語/お/ご prefixes; permissible to drop お/ご from non-essential nouns)
- Contractions: "don't", "you'll", "it's", "we're", "I'd"
- Casual greetings: "hey", "hi there", "yo", "what's up", "hi 👋"
- Second-person directness, exclamations, emoji presence (🎉 😎 🚀 ✨)
- Slang / colloquialisms: "cool", "awesome", "no worries", "kinda", "stuff"
- Consumer-app voice: gaming, social, lifestyle, dating, fitness, kids, casual e-commerce
- Sentence fragments and conversational filler

### Mixed / ambiguous source → default to FORMAL
Japanese over-politeness reads stiff but never offensive; under-politeness can read as disrespectful. When in doubt, stay formal.

### Explicit user override
If the user says "use polite form" / "drop the honorifics" / "make it casual", their instruction overrides auto-detection.

### Worked examples

| Source | Detected register | Japanese output style |
|----------------|-------------------|-----------------------|
| "Please review the terms of service before proceeding." | formal | お手続きを進める前に、利用規約をご確認ください。 |
| "Hey! Tap here to get started — it's super quick 🚀" | informal | こんにちは！ここをタップして始めましょう。すぐに完了します 🚀 |
| "Submit your application by the deadline." | formal (no contractions, directive) | 期限までに申請書を提出してください。 |
| "Don't forget to save your work!" | informal (contraction + exclamation) | 作業内容を保存するのを忘れずに！ |

After detection: keep the chosen register consistent throughout the file. The no-mixing rule still applies.

## Critical Accuracy Rules (NEVER violate)

### 1. Word vs Character — completely different meanings

| English | Wrong | Correct |
|---------|-------|---------|
| word count | 文字数 | **単語数** |
| character count | 単語数 | **文字数** |

word = 語/単語 ; character = 文字. Confusing these changes meaning entirely.

### 2. FOR vs PER — total vs rate

| English | Wrong | Correct |
|---------|-------|---------|
| for # languages (total) | #言語につき | **#言語で / #言語分** |
| per language (rate) | 言語で | **言語あたり / 1言語につき** |

### 3. Measurement unit words — required after numeric placeholders

English "{n}s/m/h/d" suffixes MUST become explicit Japanese unit words.

| Wrong | Correct |
|-------|---------|
| 削除まで{seconds} | 削除まで{seconds}**秒** |
| {minutes}後にリトライ | {minutes}**分**後にリトライ |
| 残り{hours} | 残り{hours}**時間** |
| {days}以内に完了 | {days}**日**以内に完了 |

### 4. Temporal expression agreement

| Meaning | Use | Don't use |
|---------|-----|-----------|
| Countdown / future event | 〜後に (after) | 〜中に (means "during") |
| Ongoing state | 〜中 / 〜しています | 〜後 |
| Deadline | 〜以内に (within) | — |

`{days}日中` literally means "during the daytime", NOT "in N days". Always use `{days}日後`.

### 5. Placeholder type markers

When a placeholder is a type/format/language, add explicit type marker.

| Wrong | Correct |
|-------|---------|
| {formatList}ファイルに対応 | {formatList}**形式の**ファイルに対応 |
| {languageList}コンテンツ | {languageList}**言語の**コンテンツ |

### 6. Particles (助詞)

| Particle | Use for | Example |
|----------|---------|---------|
| を | Direct object | ファイル**を**使用 |
| に | Direction/target | サーバー**に**送信 |
| で | Means/location of action | 5言語**で**翻訳 |
| の | Possession/attribution | 翻訳**の**文脈 |
| から | Source/origin | サーバー**から**取得 |

Wrong: `ファイルに使用` → Correct: `ファイルを使用` (使用する takes を).

### 7. Measure words (助数詞)

| Counter | Use for |
|---------|---------|
| 語 / 言語 | Languages |
| 件 | Cases / items / records |
| 個 | General objects |
| 人 | People |
| 枚 | Flat things (paper, photos) |

Wrong: `{count}個の言語` / `{count}件の言語` → Correct: `{count}言語`.

### 8. Domain terminology — use IT loanwords for software contexts

| Source | Wrong (literal) | Correct (IT term) |
|--------|-----------------|---------------------|
| architecture | 建築 | **アーキテクチャ** |
| pipeline (CI/CD) | 配管 | **パイプライン** |
| deploy | 展開する | **デプロイする** |
| source of truth | 真実の源 | **信頼できる情報源 / 正式なデータソース** |
| bug (software) | 虫 | **バグ** |

## UI Conventions

### Buttons — stem/noun form (NOT polite sentence)

| Wrong | Correct |
|-------|---------|
| 保存します | **保存** |
| 編集する | **編集** |
| 作成します | **作成** |

### Status messages — ongoing → 〜中

| Wrong | Correct |
|-------|---------|
| 翻訳する | **翻訳中** |
| 処理 | **処理中** |

### Completion messages — past/完了 form

| Wrong | Correct |
|-------|---------|
| 保存する | **保存しました / 保存完了** |
| 翻訳する | **翻訳が完了しました** |

### Empty state — negative existence

| Wrong | Correct |
|-------|---------|
| 結果は空です | **結果がありません / 結果が見つかりませんでした** |
| 選択されていない | **選択されていません** |

### Drag and drop

| English | Japanese |
|---------|----------|
| drag | ドラッグ |
| drop | ドロップ |
| **release** (let go) | **離す** — NOT リリース |
| **browse** (file picker) | **選択 / ファイルを選択** — NOT 参照 |

### Validation messages

Use connectors: および/と (and), または (or), のみ (only). Always polite form.

- Wrong: `3-50文字、文字、数字、ハイフンのみ`
- Correct: `3-50文字。使用可能：英字、数字、ハイフン`
- Wrong: `パスワードが短すぎる` → Correct: `パスワードが短すぎます`

### Other UI patterns

| Wrong | Correct | Reason |
|-------|---------|--------|
| 代替検出 | **代替検出方法** | Labels need complete noun phrases |
| 自動 | **自動モード** | Bare adjectives need completing nouns |
| 25+言語 | **25以上の言語** | "N+" → N以上の〜 |
| +N more items | **他{count}件 / 残り{count}件** | "+N more" pattern |

## Keigo Consistency

Maintain ONE level throughout. Mixing is the most common error.

| Don't mix | Use |
|-----------|-----|
| 変更してください + クリックしろ | 変更してください + クリックしてください |
| ご確認ください + 保存した | ご確認ください + 保存しました |

UI labels (buttons) stay in stem form regardless of keigo level used in sentences.

## Punctuation — full-width in Japanese text

Use `。、：「」！？（）`. Half-width for URLs, emails, code, English text.

| Wrong | Correct |
|-------|---------|
| ステータス: 完了 | ステータス**：**完了 |
| 確認してください,保存します | 確認してください**、**保存します |
| メール: user@example.com | メール**：**user@example.com (full-width colon, but email stays half-width) |

## Spacing (スペーシング)

- **Space** between Japanese and Latin script/numbers: `API 設定` not `API設定`, `合計 10 件` not `合計10件`.
- **No space** between Japanese characters: `保存する` not `保存 する`.

## Native vs Loanword — prefer native for UI

| Avoid (katakana) | Use (native) |
|------------------|--------------|
| セーブする | 保存する |
| セッティング | 設定 |
| セレクト | 選択 |
| ターゲットオーディエンス | 対象ユーザー |
| カジュアル (for speech tone) | くだけた / 気軽な |

`カジュアル` describes fashion. For communication register, use `くだけた` or `気軽な`. UI tone vocabulary: `フォーマル、くだけた、プロフェッショナル`.

Keep katakana ONLY for: established loanwords (アップロード, ダウンロード, キャンセル, ログイン), foreign brand names, technical abbreviations (API, URL, ID).

## Honorific Prefixes お (o-) / ご (go-)

Honorific prefixes attach to nouns to elevate the referent. Used in formal register; minimized in informal.

### Rule of thumb
- **お** attaches to native Japanese words (和語 / wago): お名前, お時間, お電話, お知らせ, お支払い, お申し込み, お問い合わせ
- **ご** attaches to Sino-Japanese words (漢語 / kango): ご連絡, ご利用, ご確認, ご質問, ご注文, ご登録, ご案内
- Test: native word → お ; Chinese-origin word → ご
- Exceptions exist (e.g., ご飯 is wago but takes ご; お電話 looks kango but takes お). Memorize the common UI ones below.

### Register usage
- Formal register: apply liberally to customer-facing nouns
- Informal register: drop from non-essential nouns (`登録` instead of `ご登録` is fine in casual UI)
- 謙譲語 (humble) contexts referring to ONE'S OWN action: do NOT attach お/ご to your own action. e.g., when YOU are applying, write `申し込む`, NOT `お申し込みする`. Reserve `お申し込み` for referring to the customer's action.

### Common UI examples

| Japanese | English |
|----------|---------|
| お名前 | name (customer's) |
| お時間 | time (customer's) |
| お支払い方法 | payment method |
| お知らせ | notification |
| お問い合わせ | inquiry / contact |
| ご利用規約 | terms of use |
| ご登録 | registration |
| ご確認 | confirmation |
| ご連絡 | contact / communication |
| ご注文 | order |
| ご案内 | guidance / information |
| ご質問 | question |

## False Friends (和製英語)

| Katakana | Means in Japanese | Correct for English meaning |
|----------|-------------------|---------------------------|
| マンション | apartment/condo | 大邸宅 (for "mansion") |
| バイキング | buffet | (Viking warrior - rarely needed) |
| スマート | slim/slender | 頭がいい (for "intelligent") |
| テンション | excitement/high energy | 緊張 (for "stress/tension") |

## Calques to avoid

| Literal (wrong) | Natural Japanese |
|-----------------|------------------|
| 意味をなす | 理にかなっている |
| 一日の終わりに | 結局のところ |
| テーブルの上に (abstract) | 議題として |
| ボールはあなたのコートに | あなた次第です |
| Break a leg | 頑張って！/ 幸運を祈ります |
| Piece of cake | 朝飯前 / 簡単 |
| When pigs fly | ありえない / 無理 |

## Compound Adjectives

| English pattern | Wrong | Correct |
|-----------------|-------|---------|
| X-aware | コンテキストアウェア | **文脈を考慮した** |
| AI-powered/driven | AI駆動型 | **AIを活用した / AI搭載** |

## Compound Descriptive Nouns

Decompose English compounds, rebuild with Japanese noun-modification syntax.

- "mom creators" → `ママクリエイター` or `子育て中のクリエイター` (NOT `母親作成者`)
- "niche creators" → `ニッチ分野のクリエイター` or `専門クリエイター`
- "English-speaking customer service" → `英語対応の顧客サービス` (compound adjective, NOT participial)

## Spatial Metaphor Prepositions (adapt, don't translate literally)

| English (figurative) | Use | Don't use |
|---------------------|-----|-----------|
| under [category] | 〜の中から / 〜にある | 〜の下に |
| on top of (in addition) | 〜に加えて | 〜の上に |
| behind the scenes | 舞台裏 / 裏側 | (literal) |
| within [timeframe] | 〜以内に | 〜の内部に |

## UI Element Reference in Prose

When referencing a UI label by name in running prose, bracket it:

- Wrong: `名前のフィールド` → Correct: `「名前」フィールド` or `［名前］フィールド`
- Wrong: `アカウントのタブ` → Correct: `「アカウント」タブ`
- Generic elements (`検索バー`) need no brackets.

## Temporal Simile Restructuring

English similes like "like it's [YEAR]" / "stuck in [YEAR]" imply "outdated / frozen in time". Literal `[YEAR]年のまま + 動詞` sounds unnatural.

| English | Wrong | Natural |
|---------|-------|---------|
| operating like it's 1995 | 1995年のまま動いています | **1995年から何も変わっていない / 1995年で時が止まったかのようだ** |
| stuck in [YEAR] | [YEAR]年に止まっている | **[YEAR]年から進歩していない / [YEAR]年代のままだ** |

## Polysemy — pick the right sense for the domain

| Word | Wrong (literal) | Correct (contextual) |
|------|-----------------|--------------------|
| copy (marketing) | コピー/複写 | **コピー(文案) / 文言** |
| sauce (figurative) | ソース | **秘訣 / 決め手** |
| bug (software) | 虫 | **バグ** |
| resume (verb) | 履歴書 | **再開する** |

## Proper Nouns — natural form in UI

| Formal/news | UI/casual |
|-------------|-----------|
| 米国 | **アメリカ** |
| 英国 | **イギリス** |
| アメリカ合衆国 | **アメリカ** |

## Name Suffixes (敬称)

Suffixes attach to a person's name to convey respect level. Choosing the wrong one is a noticeable formality error.

| Suffix | Formality | When to use in UI |
|--------|-----------|-------------------|
| 様 (sama) | Highest — customer-facing | Addressing the customer in messages: `田中様、ようこそ。` |
| さん (san) | Neutral polite | Internal references, casual customer touch, community apps |
| 殿 (dono) | Outdated / archaic | Avoid in modern UI; appears only on formal certificates |
| 先生 (sensei) | Profession-respect | Teachers, doctors, lawyers, authors |
| ちゃん / 君 (kun) | Diminutive / casual | Avoid in UI unless target audience is kids/casual community |

### Rules
- Do NOT attach a suffix to one's own name. The brand/sender never self-applies 様/さん.
- Personalized greetings address the recipient only: `田中様、ようこそ。` — NOT `田中様、私田中ようこそ。`
- When in doubt for customer-facing UI: use 様.
- For internal dashboards / team-facing UI: さん is more natural than 様.

## Question / Confirmation Phrasing

- Wrong: `あなたは確かですか？` → Correct: `よろしいですか？`
- Wrong: `これを本当に削除しますか？` → Correct: `この項目を削除してもよろしいですか？`
- End yes/no questions with `か` in polite form. Omit pronouns.

## Cultural Conventions

| Item | Format |
|------|--------|
| Date | `2024年1月15日` (NOT `01/15/2024`) |
| Time | `14時30分` or `14:30` |
| Currency | `¥1,000` or `1,000円` |

## Number Formatting

### Numerals
- **Thousands separator**: comma — `1,000`, `10,000`, `1,234,567`
- **Decimal point**: period — `3.14`, `0.5`
- **Large units** use kanji groupings (not Western thousands/millions/billions):

| Numeral | Japanese | Meaning |
|---------|----------|---------|
| 10,000 | `1万` | ten thousand |
| 100,000 | `10万` | hundred thousand |
| 1,000,000 | `100万` | one million |
| 10,000,000 | `1,000万` or `1千万` | ten million |
| 100,000,000 | `1億` | hundred million |
| 1,000,000,000,000 | `1兆` | trillion |

### Currency
- `¥1,000` (symbol-first, Western style)
- `1,000円` (number + 円, more native)
- Large amounts: `1万円`, `100万円`, `1億円`

### Date
| Format | Use case |
|--------|----------|
| `2024年1月15日` | Standard / full — preferred in UI body copy |
| `2024/01/15` | Slash form — tables, logs, compact UI |
| `2024-01-15` | ISO — technical / API contexts |
| `R6/01/15` or `令和6年1月15日` | Reiwa era — formal/government/legal only |

### Time
| Format | Use case |
|--------|----------|
| `14:30` | 24-hour, compact — preferred in UI |
| `14時30分` | 24-hour, native — body copy / formal |
| `午後2時30分` | 12-hour with 午前/午後 — casual / spoken style |

### Counters (助数詞) — expansion

| Counter | Use for |
|---------|---------|
| 人 (にん) | People (general) |
| 名 (めい) | People (formal, business — `5名様`) |
| 件 (けん) | Cases, records, inquiries, results |
| 個 (こ) | General small objects |
| 枚 (まい) | Flat things — paper, photos, tickets, cards |
| 冊 (さつ) | Bound items — books, magazines, notebooks |
| 台 (だい) | Machines, vehicles, devices |
| 本 (ほん) | Long thin objects — bottles, pencils, calls |
| 杯 (はい) | Cups, glasses, bowls of liquid |
| 匹 (ひき) | Small animals — cats, dogs, fish |
| 頭 (とう) | Large animals — cattle, horses |
| 階 (かい) | Floors of a building |
| 番 (ばん) | Number / turn / ranking |
| 語 / 言語 | Languages |

## Greeting and Closing Conventions

### Spoken / time-of-day greetings
| Japanese | Use |
|----------|-----|
| おはようございます | Morning |
| こんにちは | Daytime |
| こんばんは | Evening |
| お疲れ様です | Workplace standard — "thank you for your hard work" |
| はじめまして | First meeting introduction |

### UI welcome
- `ようこそ` — formal welcome (`ようこそ、田中様。`)
- `こんにちは` — neutral / informal welcome

### Email openings
| Japanese | Formality |
|----------|-----------|
| お世話になっております | Standard business |
| 平素より大変お世話になっております | More formal / first-touch enterprise |
| いつもありがとうございます | Warm / customer-facing |

### Email closings
| Japanese | Formality |
|----------|-----------|
| よろしくお願いいたします | Standard |
| 何卒よろしくお願い申し上げます | Very formal |
| 引き続きよろしくお願いいたします | Ongoing relationships |

## Cost / Estimate Expression Ordering

Be explicit about whether the amount is per-item or total.

- Pattern A (amount-first): `{credits}クレジット（{count}言語分）`
- Pattern B (scope + 合計): `{count}言語で合計{credits}クレジット`
- Ambiguous (wrong): `{count}言語{credits}クレジット` — could mean per-language OR total.

## Redundant Modifiers — remove

| Wrong | Correct |
|-------|---------|
| {min}文字の長さ | {min}文字以上 |
| 丸い形の | 丸い |
| あなたのファイルを保存 | ファイルを保存 (omit pronoun) |

## Self-Check Checklist (run before finalizing)

### Accuracy
- [ ] Particles correct (を/に/で/の/から)
- [ ] Measure words appropriate (言語/件/個/人/枚)
- [ ] Word vs character not confused (単語 vs 文字)
- [ ] FOR vs PER not confused (〜で/分 vs 〜あたり/につき)
- [ ] Unit words added after numeric placeholders (秒/分/時間/日)
- [ ] Temporal: 〜後 for countdowns, 〜中 for ongoing, 〜以内に for deadlines
- [ ] Placeholder type markers added (形式の, 言語の)
- [ ] Keigo level consistent throughout
- [ ] UI buttons in stem form; sentences in です/ます
- [ ] Full-width punctuation (。、：「」)
- [ ] SOV word order
- [ ] Script choice correct (hiragana=grammar, katakana=foreign, kanji=meaning)
- [ ] Spacing: gap between Japanese ⇄ Latin/numbers; none between Japanese characters
- [ ] All `{variables}` and ICU intact
- [ ] Domain terminology uses IT loanwords (アーキテクチャ, デプロイ, パイプライン)

### Naturalness
- [ ] UI labels are complete noun phrases (代替検出方法, NOT 代替検出)
- [ ] Cost expressions use amount-first or scope+合計 pattern
- [ ] Tone vocabulary correct (くだけた, NOT カジュアル for speech)
- [ ] No English idioms translated literally (calques)
- [ ] Pronouns omitted when context clear
- [ ] Compound adjectives natural (AIを活用した, NOT AI駆動型)
- [ ] Drag-drop verbs correct (離す for release, NOT リリース)
- [ ] Native term over loanword when both exist (保存 > セーブ)
- [ ] Compound nouns restructured (ママクリエイター, NOT 母親作成者)
- [ ] UI labels in prose use 「」brackets
- [ ] Spatial metaphors adapted (〜の中から, NOT 〜の下に)
- [ ] False friends not used in wrong sense (マンション ≠ mansion)
- [ ] Validation messages polite + clear structure

## Worked Example

**Source:** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

**Wrong (literal):**
あなたへようこそ！アップロードするためにあなたのファイルを参照してください — 私たちは25+のフォーマットをサポートし、5言語につき{seconds}でそれを翻訳します。心配しないで、いつでもキャンセルできます。

**Issues:** `あなたへ` (unnatural), `あなたの` (redundant), `参照` (wrong UI verb), `25+` (not natural quantity), `5言語につき` (FOR/PER confusion, says PER), `{seconds}` (missing unit), `心配しないで` (calque).

**Correct:**
ようこそ！アップロードするファイルを選択してください。25以上の形式に対応し、5言語で{seconds}秒以内に翻訳します。いつでもキャンセル可能です。
