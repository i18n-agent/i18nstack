---
name: localize-zh
description: "Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Chinese (zh). Asks the user to choose the regional variant (zh-CN Mainland Simplified, zh-Hant-TW Taiwan Traditional, or zh-Hant-HK Hong Kong Traditional) on first use, then enforces variant-specific script, vocabulary, formality, currency, AND politically-sensitive place-name conventions. Mistakes in place names, mainland terminology, country/region labels, and Simplified/Traditional script mixing can cause real customer escalation across all three markets."
---

# Chinese Translation Rules (zh / 中文)

Distilled from the production translation prompts (`zh.ts`, `zh-hant.ts`, `zh-hant-tw.ts`, `zh-hant-hk.ts`) AND domain knowledge of Chinese localization politics. Follow these rules verbatim — they are model-agnostic and produce consistent native-quality output without political missteps.

## ⚠️ READ FIRST — Political Red Lines

These rules apply across ALL variants. Violating any of them can cause **real customer escalation, public backlash, app store removal, or legal exposure** (especially in HK post-2020). They override every other rule in this skill.

1. **NEVER mix Simplified and Traditional characters in one output.** Mixing `软件設定` or `軟體设置` is the single most damaging error possible — perceived as lazy/AI-slop and sometimes politically careless. Particularly watchful pairs: 设/設, 体/體, 国/國, 个/個, 这/這, 们/們, 时/時, 后/後, 发/發, 会/會, 学/學, 实/實, 应/應, 当/當, 还/還, 关/關, 开/開, 听/聽, 见/見, 业/業, 处/處, 务/務. Validate the entire output is 100% one script.
2. **NEVER write `中國台灣 / 中国台湾`** in Taiwan-targeted content. Use `台灣` alone.
3. **NEVER write `祖國 / 祖国` (motherland)** in TW or HK content unless the source explicitly contains it and the user has confirmed the framing.
4. **NEVER use `內地` (inner land)** in TW content — `內地` is the PRC-framed term implying Taiwan is peripheral. Use `中國大陸` or `大陸` for TW.
5. **NEVER use `中華民國` (Republic of China)** in CN content unless quoting historical source.
6. **NEVER use bare `$`** for NTD or HKD — always `NT$` or `HK$` to disambiguate from USD/CNY.
7. **NEVER mix `民國` calendar with `公元/西元`** dates in the same document.
8. **DEFAULT to "Country/Region" labels** (`國家/地區` Traditional, `国家/地区` Simplified) instead of "Country" — universal safe choice for dropdowns containing Taiwan/HK/Macau.
9. **NEVER ship CCP, KMT, DPP, or leader names** unsolicited; treat as red-flag terms requiring user confirmation.
10. **In HK content (post-2020 NSL), AVOID restricted political phrases** (`光復香港`, `時代革命`, 2019 protest slogans) — these have legal implications under the National Security Law.

If the source text contains any of: `祖国/祖國`, `光復香港`, `時代革命`, `中華民國`, `Taiwan, Province of China`, `Taiwan, China`, `中國台灣`, or specific leader/party names — **STOP and confirm the user's intent** before translating.

## Mindset

> 你是一位極其挑剔的中文作家，痛恨從英文直譯而來的不自然表達。

Reject literal English calques. Restructure fully into natural Chinese. Common English terms (API, URL, AI, app) are acceptable when they're standard in the target variant — HK tolerates code-mixing; CN and TW prefer native terms.

## Variant Selection (run FIRST)

Chinese has three variants that **directly conflict on script, vocabulary, formality, currency, AND political framing**. Applying the wrong variant produces output that reads as foreign or — worse — politically tone-deaf.

**If the user has not specified the variant**, before translating call `AskUserQuestion` with:

- Question: `Which Chinese variant should I target?`
- Header: `ZH variant`
- Options:
  1. **Simplified Chinese — Mainland (zh-CN / zh-Hans)** — 简体字, 您/你 with 您 in B2B, `保存/设置/登录/视频/软件/网络`, RMB `¥`/`元`, `"..."` quotes.
  2. **Traditional Chinese — Taiwan (zh-Hant-TW)** — 繁體字 (TW forms 嘆/著/裡), defaults to `您`, `儲存/設定/登入/影片/軟體/網路`, NTD `NT$`, `「」` quotes, strict native-term preference.
  3. **Traditional Chinese — Hong Kong (zh-Hant-HK)** — 繁體字 (HK forms 歎/着/裏), defaults to `你`, `儲存/設定/登入/影片/軟件/網絡` (hybrid: Traditional script but selectively aligns with CN on hardware/networking terms), HKD `HK$`, `「」` quotes, English code-mixing acceptable.

**If unsure how to label the user request**: ask explicitly. The cost of mislabeling is much higher than the cost of one extra question.

**After confirmation**, apply: **Universal Chinese base** + the chosen variant's deltas. Do NOT cross-apply variant rules.

## Pre-Translation Setup

1. **Variant confirmed** above. Lock in script (Simplified vs Traditional) and character-form (TW vs HK).
2. **Formality (address form)** — pick `您` (formal) or `你` (neutral) and use it consistently throughout. Default by variant: CN business → `您`; TW → `您`; HK → `你`.
3. **Quotation marks** — `"..."` for CN; `「」` (with `『』` nested) for TW + HK.
4. **Currency** — `¥`/`元` (CN), `NT$`/`新台幣` (TW), `HK$`/`港幣` (HK). NEVER bare `$`.
5. **Placeholders** — Preserve `{variables}` and ICU plural syntax exactly.

## Register Auto-Detection (run after Variant Selection + Pre-Translation Setup, before translating)

If the user has NOT specified 您 or 你, infer from source text register. Match output to source — formal source → 您; informal source → 你. The default differs by variant (see below).

### Formal source signals → output 您 / 您的
- Hedging / polite modals: "please", "kindly", "we recommend", "could you", "would you mind"
- Passive / impersonal: "users are advised", "it is recommended", "applicants must"
- No contractions: "do not", "cannot", "we will"
- Domain vocabulary: legal, financial, healthcare, regulatory, enterprise B2B, government, insurance, banking
- Third-person / distance: "the user must", "customers should"
- Long sentences, formal connectors (然而, 此外, 而且)
- Brand voice: bank, insurance, government, B2B SaaS, healthcare, legal tech
- No exclamations or emojis

### Informal source signals → output 你 / 你的
- Contractions: "don't", "you'll", "it's", "we're"
- Casual greetings: "hey", "hi there", "yo", "hi 👋"
- Second-person directness, exclamations, emoji (🎉 😎 🚀 ✨)
- Slang: "cool", "awesome", "no worries", "kinda"
- Consumer-app voice: gaming, social, lifestyle, dating, fitness, kids
- Sentence fragments and conversational filler

### Mixed / ambiguous source → defaults differ by variant
- **zh-CN**: default to **您** for B2B/financial; **你** for general consumer. When ambiguous, prefer **您**.
- **zh-Hant-TW**: default to **您**. Reserve **你** for explicitly casual consumer apps.
- **zh-Hant-HK**: default to **你**. Reserve **您** for government/luxury/banking. HK is uniquely informal-default.

### Explicit user override
If the user says "use 您" / "use 你" / "formal" / "casual", their instruction wins.

### Worked examples (zh-CN; substitute Traditional + variant glyphs as needed)

| Source | Detected | Chinese output (zh-CN) |
|----------------|----------|------------------------|
| "Please review the terms of service before proceeding." | formal | 请在继续之前查看服务条款。 (uses 请 polite + impersonal) |
| "Hey! Tap here to get started — it's super quick 🚀" | informal | 你好！点击这里开始 — 超快 🚀 |
| "Submit your application by the deadline." | formal | 请在截止日期前提交您的申请。 |
| "Don't forget to save your work!" | informal | 别忘了保存你的工作！ |

After detection: keep the chosen form consistent. NEVER mix 您/你 across pronouns, possessives, OR imperatives.

### HK code-mixing interaction with register
- **HK informal**: English code-mixing fully acceptable in casual contexts: `按 Save 制儲存`, `check 你的 email`, `schedule 一個 meeting`.
- **HK formal**: minimize English mixing — use 儲存 not Save, 電郵 not email, 會議 not meeting.
- pt-CN/TW: do NOT code-mix even in informal contexts — keep Chinese throughout.

## Universal Chinese Base (apply to ALL three variants)

### 1. Full-width punctuation in Chinese text

Use full-width `。，：；！？（）`. Half-width allowed ONLY inside URLs, email addresses, code, English text, and currency-with-numbers.

| Wrong | Correct |
|-------|---------|
| `保存成功.` | **`保存成功。`** |
| `名称,邮箱,密码` | **`名称，邮箱，密码`** |
| `状态: 完成` | **`状态：完成`** |

Enumeration uses `、` for items: `蘋果、香蕉` (NOT `蘋果,香蕉`).

Note: quote-mark convention differs by variant — see variant deltas.

### 2. Measure words (量詞 / 量词) — required for countable nouns

| Wrong | Correct |
|-------|---------|
| `{count}语言 / {count}語言` | `{count}**种**语言 / {count}**種**語言` |
| `每语言成本 / 每語言成本` | `每**种**语言成本 / 每**種**語言成本` |
| `3文件 / 3檔案` | `3 **个** 文件 / 3 **個** 檔案` |

Common counters: 种/種 (kinds, languages), 个/個 (general items), 篇 (articles), 份 (copies), 件 (cases), 名 (people), 张/張 (sheets), 部 (vehicles, films).

### 3. Word vs character — semantic distinction (CRITICAL)

NEVER confuse — they are different concepts.

| Source | Wrong | Correct |
|--------|-------|---------|
| word count | `字数 / 字數` | **`词数 / 詞數`** or **`单词数 / 單詞數`** |
| character count | `词数 / 詞數` | **`字数 / 字數`** |

`字` = character. `词/詞` = word.

### 4. FOR vs PER — total vs rate (CRITICAL)

| English | Wrong | Correct |
|---------|-------|---------|
| for # languages (total) | `每种语言 / 每種語言` | **`{N}种语言共计... / {N}種語言共計...`** |
| per language (rate) | `共计 / 共計` | **`每种语言 / 每種語言`** |

### 5. Temporal preposition agreement (CRITICAL, severity 2.5)

| Meaning | Use | Don't use |
|---------|-----|-----------|
| Countdown / future completion | **`将在...后 / 將在...後`** (after) | `正在...中` (means "during", wrong tense) |
| Ongoing state | **`正在... / ...中`** | `...后/...後` |
| Deadline | **`...内/...內`** (within) | — |

| Wrong | Correct |
|-------|---------|
| `正在 {seconds} 秒中删除` | **`将在 {seconds} 秒后删除`** (CN) / **`將在 {seconds} 秒後刪除`** (TW/HK) |
| `{days}日中过期 / {days}日中過期` | **`{days}日后过期 / {days}日後過期`** |

### 6. Measurement unit words after numeric placeholders (severity 2.0)

English `{n}s/m/h/d` suffixes MUST become explicit Chinese unit words.

| Wrong | Correct |
|-------|---------|
| `{seconds}中删除 / {seconds}中刪除` | `{seconds} **秒**后删除 / {seconds} **秒**後刪除` |
| `{minutes}后重试 / {minutes}後重試` | `{minutes} **分钟**后重试 / {minutes} **分鐘**後重試` |
| `等待 {hours}` | `等待 {hours} **小时** / 等待 {hours} **小時**` |
| `{days}内完成 / {days}內完成` | `{days} **天**内完成 / {days} **天**內完成` |

### 7. CJK-Latin spacing (severity 1.5)

- **Space** between Chinese characters and English/numbers: `API 密钥` not `API密钥`; `合计 10 件` not `合计10件`.
- **No space** between Chinese characters: `保存设置` not `保存 设置`.

### 8. Passive + timestamp uses `于/於`, not `的/的` (severity 2.0)

| Wrong | Correct |
|-------|---------|
| `创建的 {date}` | **`创建于 {date}`** (CN) |
| `建立的 {date}` | **`建立於 {date}`** (TW/HK) |
| `更新的 {date}` | **`更新于 {date} / 更新於 {date}`** |

`于/於` = "at/on" (preposition). `的/的` = possessive — different meaning.

### 9. Avoid `被` passive when not needed

English passive should usually become Chinese active or `已`+verb:

| Wrong | Correct |
|-------|---------|
| `文件被保存了` | **`文件已保存`** (CN) / **`檔案已儲存`** (TW/HK) |
| `任务被完成了` | **`任务已完成 / 任務已完成`** |

`被` is correct when emphasizing victimization (`他被解雇了`). Avoid it for routine status reports.

### 10. UI button labels — imperative, no polite prefix

| Wrong | Correct |
|-------|---------|
| `创建一个项目 / 創建一個專案` | **`创建项目 / 建立專案`** (drop `一个/一個`) |
| `请编辑 / 請編輯` | **`编辑 / 編輯`** (drop `请/請`) |
| `请保存 / 請儲存` | **`保存 / 儲存`** |

### 11. Status messages — progressive with `正在` or `~中`

| Wrong | Correct |
|-------|---------|
| `翻译 / 翻譯` (as status) | **`正在翻译 / 翻译中`** (CN) / **`正在翻譯 / 翻譯中`** (TW/HK) |
| `上传文件 / 上傳檔案` (as spinner) | **`正在上传... / 上傳中...`** |

### 12. UI label completeness — no bare adjectives (CRITICAL)

Labels must be complete noun phrases.

| Wrong | Correct |
|-------|---------|
| `替代检测 / 替代檢測` | **`替代检测方式 / 替代檢測方式`** |
| `自动 / 自動` (bare) | **`自动模式 / 自動模式`** or `自动检测 / 自動檢測` |
| `高级 / 進階` (bare) | **`高级设置 / 進階設定`** |

### 13. Placeholder type markers (severity 2.5)

When a placeholder represents a type/format, add explicit type marker.

| Wrong | Correct |
|-------|---------|
| `支持 {formatList} 文件 / 支援 {formatList} 檔案` | `支持 {formatList} **格式的**文件 / 支援 {formatList} **格式的**檔案` |
| `{languageList} 内容 / {languageList} 內容` | `{languageList} **种语言的**内容 / {languageList} **種語言的**內容` |

### 14. Quantity expressions

| Wrong | Correct |
|-------|---------|
| `25+语言 / 25+語言` | **`25 种以上语言 / 25 種以上語言`** or `超过 25 种语言 / 超過 25 種語言` |
| `+{count}个更多 / +{count}個更多` | **`还有 {count} 种 / 還有 {count} 種`** or `另有 {count} 项 / 另有 {count} 項` |

### 15. Cost / estimate ordering — amount-first or scope+共计

- Pattern A (preferred): `预计费用：{credits} 积分（共 {count} 种语言）` (CN) / `預計費用：{credits} 點數（共 {count} 種語言）` (TW/HK)
- Pattern B: `{count} 种语言共计 {credits} 积分` (CN) / `{count} 種語言共計 {credits} 點數` (TW/HK)
- Wrong (ambiguous): `{count} 种语言 {credits} 积分` — could mean per-language OR total.

### 16. Temporal simile restructuring (severity 2.0)

English `like it's [YEAR]` / `stuck in [YEAR]` implies "outdated". Literal `像 [YEAR] 年一样` sounds unnatural.

| Wrong | Correct |
|-------|---------|
| `像 1995 年一样运营` (CN) / `像 1995 年一樣運營` (TW/HK) | **`还停留在 1995 年 / 從 1995 年以來就沒變過`** (CN) / **`還停留在 1995 年 / 自 1995 年以來毫無改變`** (TW/HK) |

### 17. Compound descriptive noun adaptation (severity 1.5)

Decompose English compounds and rebuild with Chinese noun-modification syntax.

| English | Wrong | Correct |
|---------|-------|---------|
| mom creators | `母亲创作者 / 母親創作者` | **`妈妈创作者 / 宝妈博主`** (CN) / **`媽媽創作者 / 育兒創作者`** (TW/HK) |
| niche creators | `小众创作者 / 小眾創作者` | **`小众领域创作者 / 垂直领域博主`** (CN) / **`小眾領域創作者 / 利基創作者`** (TW/HK) |

### 18. UI element reference in prose

Use Chinese-style brackets/quotes for UI labels:

| Wrong | Correct |
|-------|---------|
| `名称的字段 / 名稱的欄位` | **`"名称"字段`** (CN) / **`「名稱」欄位`** (TW/HK) |
| `账户的标签页 / 帳戶的分頁` | **`"账户"标签页`** (CN) / **`「帳戶」分頁`** (TW/HK) |

### 19. Spatial metaphor prepositions

| English (figurative) | CN | TW / HK |
|---------------------|-----|---------|
| under [category] | `在...中 / ...下的` | `在...中 / ...下的` |
| on top of (in addition) | `除了...之外` | `除了...之外` |
| behind the scenes | `幕后` | `幕後` |
| within [timeframe] | `...内 / 在...内` | `...內 / 在...內` |

### 20. Domain terminology — IT meaning for polysemous terms

| English | Wrong (literal) | Correct (CN) | Correct (TW) | Correct (HK) |
|---------|-----------------|---------------|---------------|---------------|
| architecture (software) | 建筑 / 建築 | **架构** | **架構** | **架構** |
| pipeline (CI/CD) | 管道 / 管道 (plumbing) | **流水线 / 管线** | **管線 / Pipeline** | **管線 / Pipeline** |
| source of truth | 真相之源 | **权威数据源 / 单一可信源** | **權威資料源 / 單一可信源** | **權威資料源 / 單一可信源** |
| deploy (software) | 部署 (military: deploy troops) is acceptable in IT | **部署** | **部署** | **部署** |
| bug (software) | 虫子 / 蟲子 | **bug / 缺陷** | **bug / 錯誤** | **bug / 錯誤** |

### 21. Drag and drop

| English | CN | TW | HK |
|---------|-----|-----|-----|
| drag | 拖动 / 拖拽 | 拖曳 / 拖動 | 拖曳 / 拖動 |
| drop | 放置 | 放置 | 放置 |
| release (let go) | **松开** | **放開 / 鬆開** | **釋放** |
| browse (file picker) | 选择文件 / 浏览 | 選擇檔案 / 瀏覽 | 選擇檔案 / 瀏覽 |

| Wrong | Correct |
|-------|---------|
| `释放以上传 / 釋放以上傳` (CN/TW) | `松开即可上传 / 放開即可上傳` |

### 22. Calques to avoid (universal)

| Wrong (literal) | Natural CN | Natural TW/HK |
|-----------------|------------|---------------|
| 这说得通 / 這說得通 ("makes sense") | **这有道理 / 这合理** | **這有道理 / 言之成理** |
| 在一天结束时 / 在一天結束時 ("at the end of the day") | **最终 / 归根结底** | **最終 / 歸根究柢** |
| 并不真正 / 並不真正 ("not really") | **其实不是 / 实际上不** | **其實不是 / 實際上不** |
| 球在你的场上 / 球在你的場上 ("ball in your court") | **由你决定 / 轮到你了** | **由你決定 / 輪到你了** |

---

## zh-CN (Mainland Simplified) Deltas

Apply ONLY when user picked Mainland Simplified.

### A. Script — Simplified only

100% Simplified characters. Any Traditional character is a defect (see Red Line #1).

### B. Quotation marks — Western curly quotes

CN uses `"..."` (双引号) and `'...'` (单引号) — NOT `「」`. This is the GB standard.

| Wrong | Correct |
|-------|---------|
| `「保存」按钮` | **`"保存"按钮`** |
| `「设置」选项卡` | **`"设置"选项卡`** |

### C. Formality — `您` for business, `你` for casual

- `defaultLevel: formal` → defaults to `您/您的` for B2B SaaS, financial, enterprise.
- Consumer apps targeting younger users may use `你/你的`.
- NEVER mix within one document. Possessives must also match (`您的设置` or `你的设置`).

### D. CN-preferred vocabulary

| English | CN preferred | Avoid |
|---------|--------------|-------|
| save | **保存** | — |
| settings | **设置** | 设定 |
| select | **选择** | — |
| upload | **上传** | — |
| download | **下载** | — |
| login | **登录** | — |
| logout | **注销** | — |
| cancel | **取消** | — |
| delete | **删除** | — |
| edit | **编辑** | — |
| document | **文档** | — |
| video | **视频** | — |
| link | **链接** | — |
| integration | **集成** | — |
| software | **软件** | — |
| network | **网络** | — |
| internet | **互联网** | — |
| computer | **计算机 / 电脑** | — |
| user | **用户** | — |
| default | **默认** | — |
| endpoint | **端点** | 接口 |
| header (HTTP) | **请求头** | 标头 |
| credits | **积分** | 额度, 信用 |
| dashboard | **控制台** | 仪表板 |

### E. Currency, date, time (CN)

- Currency: `¥1,000` or `1,000 元`. For international audiences alongside USD, use `CN¥` or `RMB` to disambiguate from JPY.
- Date: `2024年1月15日` or `2024-01-15`. NEVER `01/15/2024`.
- Time: `14:30` or `下午 2 点 30 分`.
- Calendar: Gregorian (公元/公元前). NEVER use `民國` calendar.
- Number format: `1,234,567.89` (Western thousands).

### F. CN proper nouns

| Wrong | Correct |
|-------|---------|
| `澳大利亚` (in casual UI) | **`澳洲`** (short form preferred) |
| `美国英语` | **`美式英语`** |
| `英国英语` | **`英式英语`** |

### G. CN UI tone vocabulary

| English | Wrong | Correct |
|---------|-------|---------|
| casual (tone) | `休闲` (= leisure activity) | **`随意 / 轻松`** |
| formal | (literal) | **`正式`** |
| professional | (literal) | **`专业`** |

### H. CN political conventions

- **`中国大陆 / 内地 / 大陆`** are all acceptable for "Mainland".
- Listing Taiwan in country dropdowns is sensitive. Common PRC framings: `中国台湾`, `中国台湾省`. For software shipping to Mainland China, omitting these framings can trigger app store removal. **Recommend labeling dropdown "国家/地区" (Country/Region)** and listing Taiwan as `中国台湾` only if explicitly required by PRC distribution.
- HK: `中国香港 / 香港特别行政区` (official). Bare `香港` is generally fine for commercial software.
- AVOID: `中华民国`, `Republic of China` (unless quoting historical source).
- AVOID: Taiwan-as-country implications.

---

## zh-Hant-TW (Taiwan Traditional) Deltas

Apply ONLY when user picked Taiwan Traditional.

### A. Script — Traditional with Taiwan character forms

100% Traditional. TW-specific glyphs:

| TW form (use) | HK form (avoid for TW) |
|---------------|------------------------|
| 嘆 | 歎 |
| 妝 | 粧 |
| 著 (particle) | 着 |
| 衛 (as in 衛生) | 衞 |
| 裡 (inside) | 裏 |

### B. Quotation marks — `「」` primary, `『』` nested

| Wrong | Correct |
|-------|---------|
| `"儲存"按鈕` | **`「儲存」按鈕`** |
| `'設定'分頁` | **`「設定」分頁`** |

Nested: `他說「她回答『好的』」`.

### C. Formality — `您` default

- `defaultLevel: formal` → defaults to **`您/您的`** in professional/SaaS contexts.
- Reserve `你` for casual consumer apps targeting young users.
- Possessives must match.

### D. TW-preferred vocabulary (CRITICAL — Mainland-term avoidance)

The TW prompt explicitly says: *"如果一個詞聽起來像是大陸網站或科技公司的用語，那就是錯的"* (if a word sounds like Mainland tech company terminology, it's wrong).

| English | TW preferred | CN form (AVOID in TW) |
|---------|--------------|------------------------|
| save | **儲存** | 保存 |
| settings | **設定** | 設置 |
| login | **登入** | 登錄 |
| logout | **登出** | 注銷 |
| link | **連結** | 鏈接 |
| video | **影片** | 視頻 |
| document | **文件** | 文檔 |
| file | **檔案** | 文件 (CN means file generically; TW disambiguates 文件=document, 檔案=file) |
| integration | **整合** | 集成 |
| checkout | **結帳** | 結賬 |
| credits | **點數** | 積分 |
| software | **軟體** | 軟件 / 软件 |
| hardware | **硬體** | 硬件 / 硬件 |
| network | **網路** | 網絡 / 网络 |
| internet | **網際網路** | 互聯網 / 互联网 |
| mobile (adj) | **行動** | 移動 / 移动 |
| privacy | **隱私** | (HK uses 私隱) |
| tips/hints | **提示** | (HK uses 貼士) |
| program (n) | **程式** | 程序 |
| computer | **電腦** | 計算機 / 计算机 |
| digital | **數位** | 數碼 / 数字 / 数码 |
| information | **資訊** | 信息 |
| message | **訊息** | 消息 / 信息 |
| server | **伺服器** | 服务器 |
| database | **資料庫** | 数据库 |
| data | **資料** | 数据 |
| default | **預設** | 默认 |
| optimization | **最佳化** | 优化 |
| quality | **品質** | (HK uses 質素; CN 质量) |
| AI | **人工智慧** | (CN: 人工智能; HK trends 人工智能) |
| cloud | **雲端** | (CN: 云) |
| user | **使用者** | (HK uses 使用者/用戶; CN 用户) |
| email | **電子郵件** | (HK: Email/電郵; CN 电子邮件/邮箱) |
| app | **應用程式** | (HK: App/應用程式; CN 应用/应用程序) |
| smartphone | **智慧型手機** | (HK: 智能手機; CN 智能手机) |
| memory/RAM | **記憶體** | 内存 |
| bus | **公車** | (HK: 巴士; CN: 公交车) |
| taxi | **計程車** | (HK: 的士; CN: 出租车) |

### E. TW currency, date, calendar

- Currency: `NT$1,000` or `新台幣 1,000 元`. **NEVER `$1,000` alone**; **NEVER `HK$1,000`** in TW content.
- Date: `2024年1月15日` or `2024-01-15` (Gregorian). Time: `14:30` or `下午 2 點 30 分`.
- Calendar: Default to Gregorian (`公元/西元`). ROC era (`民國`) ONLY in formal/government/tax contexts when source explicitly requires it: `民國 113 年 1 月 15 日` = 2024. Use `民國` not `中華民國` (less verbose).
- Number format: `1,234,567.89`.

### F. TW drag-drop

- release = **`放開 / 鬆開`** (colloquial, NOT `釋放` which is the HK form)
- Example: `釋放以上傳` → `放開即可上傳`.

### G. TW cultural / native-term preference

- Avoid excessive English mixing — TW prefers native Traditional Chinese.
- Communication style: more formal, polite, Mandarin-influenced.

### H. TW political conventions (CRITICAL)

- **Place names:**
  - Taiwan: **`台灣`** (most common). `臺灣` (formal, MOE-preferred). NEVER `中國台灣`.
  - Republic of China: `中華民國` — sensitive; use only if user explicitly wants ROC framing (e.g., government contexts).
  - Mainland China: **`中國大陸`** (preferred formal) or `大陸` (informal). **NEVER `內地`** — that's the PRC-framed term.
  - Hong Kong: `香港`. Macau: `澳門`.
  - China (the country): `中國`. In TW context, `中國` means PRC (foreign country), distinct from `中華民國/台灣`.
- **Avoid in TW content:**
  - `祖國` (motherland) — politically loaded.
  - `回歸` / `光復` used about Taiwan — implies Taiwan was lost and should return. (Note: `光復節` Oct 25 is a real ROC holiday — contextual exception.)
  - `內地` (used in HK/CN for Mainland) — PRC framing inappropriate for TW.
- **`國語` vs `普通話`:** `國語` is TW-standard (ROC framing for Mandarin); `普通話` is the PRC term. Use `國語` or just `中文` in TW content.
- **Country dropdown:** Label as **`國家/地區`** (Country/Region), not just `國家`. List Taiwan as `台灣` alone.

---

## zh-Hant-HK (Hong Kong Traditional) Deltas

Apply ONLY when user picked Hong Kong Traditional.

### A. Script — Traditional with Hong Kong character forms

100% Traditional. HK-specific glyphs (different from TW):

| HK form (use) | TW form (avoid for HK) |
|---------------|------------------------|
| 歎 | 嘆 |
| 粧 | 妝 |
| 着 (particle) | 著 |
| 衞 | 衛 |
| 裏 | 裡 |

The `着 / 著` distinction is the most visible — `着` appears very frequently in particle/aspect-marker usage.

### B. Quotation marks — `「」` primary, `『』` nested (same as TW)

| Wrong | Correct |
|-------|---------|
| `"儲存"按鈕` | **`「儲存」按鈕`** |

### C. Formality — `你` default

- `defaultLevel: neutral` → defaults to **`你/你的`** in most business/SaaS contexts.
- Reserve `您` for very formal contexts (government, luxury services).
- HK is more casual and direct than TW.

### D. HK-preferred vocabulary (HYBRID — Traditional script but selectively CN-aligned)

HK is a hybrid: Traditional characters but selectively aligns with Mainland on hardware/networking terms, with TW on UI/file terms, plus distinct Cantonese-influenced lexis.

**Aligns with TW (Traditional UI/file terms):**

| English | HK preferred | CN form (avoid) |
|---------|--------------|------------------|
| save | **儲存** | 保存 |
| settings | **設定** | 設置 |
| login | **登入** | 登錄 |
| logout | **登出** | 注銷 |
| link | **連結** | 鏈接 |
| video | **影片** | 視頻 |
| document | **文件** | 文檔 |
| file | **檔案** | 文件 (in CN sense) |
| integration | **整合** | 集成 |
| credits | **點數** | 積分 |
| program (n) | **程式** | 程序 |
| computer | **電腦** | 計算機 |

**Aligns with CN (hardware/networking terms — diverges from TW):**

| English | HK preferred | TW form (avoid in HK) |
|---------|--------------|------------------------|
| software | **軟件** | 軟體 |
| hardware | **硬件** | 硬體 |
| network | **網絡** | 網路 |
| internet | **互聯網** | 網際網路 |
| mobile (adj) | **流動** | 行動 |

**HK-distinct (Cantonese-influenced):**

| English | HK preferred | TW / CN form |
|---------|--------------|---------------|
| privacy | **私隱** | TW/CN: 隱私 / 隐私 |
| tips/hints | **貼士** | TW/CN: 提示 |
| quality | **質素 / 品質** | TW: 品質; CN: 质量 |
| message | **訊息 / 信息** | TW: 訊息; CN: 消息/信息 |
| bus | **巴士** | TW: 公車; CN: 公交车 |
| taxi | **的士** | TW: 計程車; CN: 出租车 |
| elevator | **升降機** | TW/CN: 電梯/电梯 |
| residential complex | **屋苑** | TW: 社區; CN: 小区 |
| AI | **人工智能 / 人工智慧** | (CN: 人工智能; TW: 人工智慧) |
| smartphone | **智能手機** | TW: 智慧型手機; CN: 智能手机 |
| email | **電郵 / Email** (code-mixing OK) | TW: 電子郵件; CN: 电子邮件 |
| app | **App / 應用程式** (code-mixing OK) | TW: 應用程式; CN: 应用 |

### E. HK code-mixing — ACCEPTABLE (and characteristic)

HK uniquely tolerates Chinese+English code-mixing in informal/business contexts. **Do NOT over-translate.**

- ✅ Acceptable: `請 check 你的 email` (casual)
- ✅ Acceptable: `我們需要 schedule 一個 meeting` (business)
- ✅ Acceptable: `按 Save 制儲存` (UI prose)
- Acceptable English words: `login`, `email`, `file`, `app`, `meeting`, `schedule`, `deadline`, `update`, `download`, `share`, `like`

But for formal documents and government-facing content, prefer native Traditional Chinese.

### F. HK currency, date, calendar

- Currency: `HK$500` or `港幣 500 元` / `港元 500`. **NEVER `$500` alone**; **NEVER `NT$500`** in HK content.
- Date: `2024年1月15日` or `2024-01-15`. Time: `14:30` or `下午 2 點 30 分`.
- Calendar: Gregorian (`公元/西元`). **NEVER use `民國`** calendar in HK content.
- Number format: `1,234,567.89`.

### G. HK drag-drop

- release = **`釋放`** (formal — NOT `放開/鬆開` which is the TW form)
- Example: `放開以上傳` (TW) → `釋放即可上傳` (HK)

### H. HK political conventions (CRITICAL — post-2020 NSL sensitivity)

- **Place names:**
  - Hong Kong: `香港` (default). `香港特別行政區` (formal/government). Mainland-facing distribution may require `中國香港` — confirm with user.
  - Mainland China: **`內地`** (preferred default, especially in commercial software post-1997) or `大陸` (more historical). Both are common; `內地` is the safer default for post-2020 commercial content.
  - Taiwan: `台灣` (bare). Avoid `中國台灣` unless Mainland-facing distribution requires it (confirm with user).
  - Macau: `澳門`.
- **Avoid in HK content (post-2020 NSL sensitivity):**
  - `光復香港` / `時代革命` — these specific phrases are restricted under the National Security Law; absolutely avoid in any commercial copy.
  - `黑暴` (PRC-official term for 2019 protests) — only if explicitly mirroring PRC framing.
  - Direct 2019 protest references in commercial copy.
  - `祖國` (motherland) — politically charged; avoid unsolicited use even though PRC-aligned media use it.
- **Sovereignty framing:**
  - `回歸祖國` is the PRC-official framing for 1997 handover.
  - `主權移交` is the more neutral/academic framing.
  - **Default to `主權移交` or `1997年` for commercial software** — neutral.
- **Country dropdown:** Label as **`國家/地區`**, not just `國家`. List `香港` and `中國` separately for international software; if shipping to Mainland with PRC distribution, may need `中國香港`.

### I. HK communication style

- More casual and direct than TW.
- Cantonese-influenced grammar/vocabulary acceptable in casual contexts.
- Code-mixing tolerated.
- Use `你` not `您` as default.

## HK 口語體 (Spoken Cantonese) vs 書面語 (Written Standard) Distinction

- **書面語 (written Standard Chinese)** uses Mandarin syntax + Traditional characters with HK glyphs. This is what 99% of HK software UI uses. Examples: `我是` (I am), `不是` (is not), `沒有` (do not have), `這個` (this one), `非常` (very).
- **口語體 (spoken Cantonese)** uses Cantonese-specific particles and characters that would never appear in formal writing. Examples: `我係` (I am), `唔係` (is not), `冇` (do not have), `呢個` (this one), `好` (very/good).
- **Critical rule for software UI**: ALWAYS use 書面語. NEVER use 口語體 unless the source is explicitly a casual messaging/social context (e.g., a quote from a user post, marketing copy mimicking conversation).
- Common Cantonese particles to AVOID in standard HK UI: `嘅` (possessive — use `的`), `嗰` (that — use `那`), `咗` (perfective marker — use 了), `緊` (progressive — use 正在/中), `啲` (some/a bit — use 一些), `喺` (at/in — use 在).
- Wrong (mixed Cantonese in formal UI): `你嘅檔案已經儲存咗` → Correct (書面語): `您的檔案已儲存`.
- Cantonese is fine in: marketing for very casual/local HK products, social/messaging apps, gaming, lifestyle apps targeting youth. Even then, prefer 書面語 for system messages.

## Name Honorifics and Address Forms

- Universal Chinese honorifics: `先生` (Mr.), `女士` (Ms./Mrs.), `小姐` (Miss — pt-CN/TW; less common in HK), `老師` (Teacher/Mr.-Ms., for educators + martial arts instructors), `醫生` (Dr., medical), `博士` (Dr., PhD), `教授` (Professor), `經理` (Manager), `董事長` (Chairman/Director).
- Order: Surname first, then title: `王先生` (Mr. Wang), `李醫生` (Dr. Li), `陳教授` (Prof. Chen).
- In zh-CN formal: `张先生`, `李女士`. In zh-Hant-TW: same. In zh-Hant-HK: same.
- For young/single women, zh-CN modern usage prefers `女士` over `小姐` (which has acquired ambiguous connotations in some contexts). TW/HK retain `小姐` more.
- Email salutations:
  - Formal (zh-CN): `尊敬的 王先生 您好：` or `张总 您好：` (with executive title).
  - Formal (TW): `敬啟者：` (general) or `王先生 您好：`.
  - Formal (HK): `敬啟者：` or `王先生：`.
  - Informal (all): `你好，王先生！` or `Hi 小王！` (HK code-mix).
- Email closings:
  - Formal: `此致敬礼` (very formal CN), `謹啟` (formal TW/HK), `誠摯地` (sincerely), `祝商祺` (business regards).
  - Informal: `祝好` (best wishes), `祝順利` (wishing you well), `Cheers` (HK code-mix).

## Empty State Phrasings (per variant)

| Context | zh-CN | zh-Hant-TW | zh-Hant-HK |
|---------|-------|-------------|-------------|
| No results | 暂无结果 / 没有结果 | 暫無結果 / 沒有結果 | 暫無結果 / 沒有結果 |
| No data | 暂无数据 | 暫無資料 | 暫無資料 |
| No notifications | 暂无通知 | 暫無通知 | 暫無通知 |
| No items selected | 未选择任何项 | 未選擇任何項目 | 未選擇任何項目 |
| Empty inbox | 收件箱为空 | 收件匣為空 | 收件匣為空 |
| No content | 暂无内容 | 暫無內容 | 暫無內容 |
| File not found | 未找到文件 | 找不到檔案 | 找不到檔案 |
| No connection | 无网络连接 | 無網路連線 | 無網絡連線 |

The `暫` / `暂` (temporarily / for now) pattern is preferred in Chinese empty states because it sounds less harsh than `没有` / `沒有`.

## Greeting Protocols

| Greeting | zh-CN | zh-Hant-TW | zh-Hant-HK |
|----------|-------|-------------|-------------|
| Universal hello | 你好 / 您好 | 你好 / 您好 | 你好 |
| Good morning | 早上好 / 早安 | 早安 / 早上好 | 早晨 (HK colloquial) / 早上好 |
| Good afternoon | 下午好 | 午安 / 下午好 | 午安 / 下午好 |
| Good evening | 晚上好 / 晚安 | 晚安 / 晚上好 | 晚上好 |
| Goodbye (formal) | 再见 | 再見 | 再見 |
| Goodbye (casual) | 拜拜 / 拜了 | 掰掰 | Bye / 拜拜 |
| Welcome (UI) | 欢迎 | 歡迎 | 歡迎 |
| Thanks (universal) | 谢谢 | 謝謝 | 多謝 (HK) / 謝謝 |
| Thanks (formal) | 非常感谢 / 感激不尽 | 非常感謝 / 感激不盡 | 非常感謝 |
| You're welcome | 不客气 / 不用谢 | 不客氣 / 不會 | 唔使客氣 (spoken) / 不用客氣 |

## Punctuation Deep Dive — Full-Width Specifics + URL Handling

- Full-width characters list: 。 (period), ， (comma), ： (colon), ； (semicolon), ！ (exclamation), ？ (question), 、 (enumeration comma), （） (parens), 「」 / 『』 / 《》 (quotes TW/HK), "..." / '...' (quotes CN).
- The enumeration comma 、 is used between list items: `蘋果、香蕉、橘子` NOT `蘋果，香蕉，橘子`.
- Em-dash 破折號 — Chinese uses double `——` (two characters wide): `這是答案——簡單明瞭`.
- Ellipsis 省略號 — Chinese uses `……` (six dots, two characters wide): `稍等……` NOT `稍等...`.
- Half-width contexts (KEEP these in their original form):
  - URLs: `https://example.com/path?key=value`
  - Email: `user@example.com`
  - Code: `function() { return true; }`
  - English in mixed text: `使用 API 來處理` (space + half-width API + space + Chinese)
  - Math: `2 + 2 = 4`
  - Currency in numbers: `¥99.99`, `NT$1,500`, `HK$500`
- Space between Chinese and Latin/numbers: required. `API密鑰` → `API 密鑰`.

---

## Cross-Variant Vocabulary Cheat Sheet

Quick comparison for the most error-prone tech terms:

| English | zh-CN | zh-Hant-TW | zh-Hant-HK |
|---------|--------|--------------|--------------|
| software | 软件 | **軟體** | **軟件** |
| hardware | 硬件 | **硬體** | **硬件** |
| network | 网络 | **網路** | **網絡** |
| internet | 互联网 | **網際網路** | **互聯網** |
| mobile (adj) | 移动 | **行動** | **流動** |
| privacy | 隐私 | **隱私** | **私隱** |
| tips | 提示 | **提示** | **貼士** |
| quality | 质量 | **品質** | **質素 / 品質** |
| video | 视频 | **影片** | **影片** |
| document | 文档 | **文件** | **文件** |
| file | 文件 | **檔案** | **檔案** |
| save | 保存 | **儲存** | **儲存** |
| settings | 设置 | **設定** | **設定** |
| login | 登录 | **登入** | **登入** |
| link | 链接 | **連結** | **連結** |
| integration | 集成 | **整合** | **整合** |
| computer | 计算机 / 电脑 | **電腦** | **電腦** |
| program | 程序 | **程式** | **程式** |
| digital | 数字 / 数码 | **數位** | **數碼** |
| information | 信息 | **資訊** | **資訊** |
| message | 消息 / 信息 | **訊息** | **訊息 / 信息** |
| server | 服务器 | **伺服器** | **伺服器** |
| database | 数据库 | **資料庫** | **資料庫** |
| data | 数据 | **資料** | **資料** |
| default | 默认 | **預設** | **預設** |
| optimization | 优化 | **最佳化** | **優化 / 最佳化** |
| AI | 人工智能 | **人工智慧** | **人工智能 / 人工智慧** |
| cloud | 云 | **雲端** | **雲端** |
| user | 用户 | **使用者** | **使用者 / 用戶** |
| email | 电子邮件 / 邮箱 | **電子郵件** | **電郵 / Email** |
| app | 应用 / 应用程序 | **應用程式** | **應用程式 / App** |
| memory/RAM | 内存 | **記憶體** | **記憶體** |
| bus | 公交车 | **公車** | **巴士** |
| taxi | 出租车 | **計程車** | **的士** |
| smartphone | 智能手机 | **智慧型手機** | **智能手機** |
| upload | 上传 | **上傳** | **上傳** |
| download | 下载 | **下載** | **下載** |
| cancel | 取消 | **取消** | **取消** |
| delete | 删除 | **刪除** | **刪除** |
| edit | 编辑 | **編輯** | **編輯** |
| drag-release verb | **松开** | **放開 / 鬆開** | **釋放** |
| quotation marks | `"..."` | `「」` | `「」` |
| address default | 您 (B2B) / 你 (consumer) | **您** | **你** |
| currency | `¥` / `元` | `NT$` / `新台幣` | `HK$` / `港幣` |
| Mainland (term) | 中国大陆 / 内地 / 大陆 | **中國大陸 / 大陸** (NOT 內地) | **內地 / 大陸** |

---

## Self-Check Checklist (run before finalizing)

### Red lines (universal — must ALL pass)
- [ ] **100% one script** — no mixed Simplified+Traditional anywhere in output
- [ ] No `中國台灣 / 中国台湾` in TW content
- [ ] No `祖國 / 祖国` in TW or HK content (unless source explicitly contains it and user approved)
- [ ] No `內地` in TW content (use `中國大陸` or `大陸`)
- [ ] No `中華民國` in CN content
- [ ] No bare `$` for NTD or HKD (always `NT$`, `HK$`)
- [ ] No `民國` calendar mixed with Gregorian in same document
- [ ] Country dropdown labeled `國家/地區` or `国家/地区` (not bare `國家/国家`)
- [ ] No CCP/KMT/DPP/leader names unsolicited
- [ ] No HK NSL-restricted phrases (`光復香港`, `時代革命`)

### Universal accuracy (all variants)
- [ ] Full-width punctuation in Chinese text (half-width only in URLs/code/email)
- [ ] Measure words present on countable nouns (種/种, 個/个, 篇, 件, 名, 張/张)
- [ ] Word vs character not confused (詞/词 vs 字)
- [ ] FOR vs PER: `共計/共计` (total) vs `每種/每种` (rate)
- [ ] Temporal preposition: `後/后` for countdown, `中` for ongoing, `內/内` for deadline
- [ ] Unit words after numeric placeholders (秒, 分鐘/分钟, 小時/小时, 天)
- [ ] Passive + timestamp uses `於/于` (NOT `的`)
- [ ] CJK-Latin spacing (space between Chinese ⇄ English/numbers)
- [ ] Placeholder type markers added (`格式的/種語言的`)
- [ ] All `{variables}` and ICU intact
- [ ] Domain terminology uses IT meaning (架構/架构, 流水線/流水线, 權威數據源/权威数据源)

### Universal naturalness
- [ ] UI labels are complete noun phrases (`替代檢測方式 / 替代检测方式`)
- [ ] Buttons use imperative without `请/請` or `一個/一个` prefix
- [ ] Status messages use `正在.../...中`
- [ ] No `被` passive when `已`+verb works
- [ ] No literal English idiom translations
- [ ] Spatial metaphors adapted (`在...中`, `除了...之外`, `幕後/幕后`)
- [ ] Compound nouns restructured (NOT `母親作成者/母亲作成者`)
- [ ] Cost ordering uses amount-first or scope+共計
- [ ] UI labels in prose use brackets/quotes for the variant

### zh-CN (Mainland) specific
- [ ] **100% Simplified characters** — zero Traditional forms
- [ ] Quotation marks `"..."` (NOT `「」`)
- [ ] Address form consistent (您 for B2B, 你 for consumer)
- [ ] CN vocab: 保存, 设置, 登录, 视频, 软件, 网络, 互联网, 默认, 优化, 用户
- [ ] Currency `¥1,000` or `1,000 元` (use `RMB` or `CN¥` if disambiguating from JPY)
- [ ] Date `2024年1月15日` or `2024-01-15`
- [ ] Gregorian calendar only
- [ ] `中国大陆 / 内地 / 大陆` all acceptable for Mainland
- [ ] Avoid `中华民国` and Taiwan-as-country implications

### zh-Hant-TW (Taiwan) specific
- [ ] **100% Traditional characters with TW glyphs** (嘆, 妝, 著, 衛, 裡) — NOT HK forms
- [ ] Quotation marks `「」` (primary), `『』` (nested)
- [ ] Address default `您` (in formal/B2B); `你` only for very casual consumer
- [ ] TW vocab: 儲存, 設定, 登入, 影片, 軟體, 網路, 網際網路, 預設, 最佳化, 使用者, 行動, 隱私, 提示, 程式, 電腦, 數位, 資訊, 訊息, 伺服器, 資料庫, 資料, 記憶體
- [ ] NO Mainland terms (軟件→軟體, 網絡→網路, 視頻→影片, 默認→預設, 用戶→使用者)
- [ ] Currency `NT$1,000` or `新台幣 1,000 元` (NEVER bare `$`)
- [ ] Date: Gregorian default; `民國` ONLY if source requires
- [ ] Drag release: `放開 / 鬆開` (NOT `釋放`)
- [ ] Place names: `台灣` alone (NEVER `中國台灣`); `中國大陸` or `大陸` for Mainland (NEVER `內地`)
- [ ] Country dropdown labeled `國家/地區`

### zh-Hant-HK (Hong Kong) specific
- [ ] **100% Traditional characters with HK glyphs** (歎, 粧, 着, 衞, 裏) — NOT TW forms
- [ ] Quotation marks `「」`
- [ ] Address default `你` (NOT `您`)
- [ ] HK vocab aligning with TW: 儲存, 設定, 登入, 影片, 文件, 檔案, 整合, 程式, 電腦
- [ ] HK vocab aligning with CN (hardware/networking): 軟件, 硬件, 網絡, 互聯網, 流動
- [ ] HK-distinct vocab: 私隱, 貼士, 質素, 巴士, 的士, 升降機, 屋苑
- [ ] Cantonese-influenced lexis OK in casual/business
- [ ] Code-mixing acceptable (`check 你的 email`, `schedule 一個 meeting`)
- [ ] Currency `HK$500` or `港幣 500 元` (NEVER bare `$`)
- [ ] Gregorian calendar only
- [ ] Drag release: `釋放` (NOT `放開/鬆開`)
- [ ] Place names: Mainland = `內地` (default post-2020) or `大陸`; `香港` (bare) or `香港特別行政區` formal
- [ ] No NSL-restricted phrases (`光復香港`, `時代革命`)
- [ ] Default to `主權移交 / 1997年` for handover references (NOT `回歸祖國`)
- [ ] Country dropdown labeled `國家/地區`

---

## Worked Example (same source, three variants)

**Source:** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

### zh-CN (Simplified, Mainland)

欢迎！请选择要上传的文件。我们支持 25 种以上格式，可在 {seconds} 秒内将其翻译为 5 种语言。请放心，您可以随时取消。

(Notes: Simplified throughout; `"..."` would be used if quoting; `25+` → `25 种以上`; `for 5 languages` → `5 种语言` with measure word; `{seconds}` followed by `秒`; `您` formal; `中国大陆`-friendly terms.)

### zh-Hant-TW (Traditional, Taiwan)

歡迎！請選擇要上傳的檔案。我們支援 25 種以上格式，可在 {seconds} 秒內將其翻譯成 5 種語言。請放心，您隨時都可以取消。

(Notes: TW Traditional glyphs (`歡`, `請`, `檔`, `傳`, `語`); `檔案` not `文件`; `支援` not `支持` (TW preference for software support); `語言` correct; `您` formal; same measure-word and unit-word rules. Quotation marks would be `「」` if needed.)

### zh-Hant-HK (Traditional, Hong Kong)

歡迎！請選擇你要上傳嘅檔案 (formal: 您要上傳的檔案)。我哋支援超過 25 種格式，可喺 {seconds} 秒內將佢翻譯成 5 種語言。放心，你隨時可以 cancel。

(More natural formal HK version, avoiding spoken Cantonese particles:)

歡迎！請選擇要上傳的檔案。我們支援超過 25 種格式，可於 {seconds} 秒內將其翻譯成 5 種語言。放心，你隨時可以取消。

(Notes: HK Traditional glyphs (`着` would appear if particle; here mostly shared with TW); `你` default not `您`; `軟件/網絡`-style alignment with CN doesn't show in this string but would matter for hardware/networking content; code-mixing `cancel` is acceptable in casual HK but `取消` is safer for formal UI; `於` formal preposition.)

### Common errors all three would catch

- Mixed script: `软体設定` (Simplified 软 + Traditional 體 + Simplified 设) — catastrophic.
- Wrong country reference: `中國台灣` in TW UI — political escalation risk.
- Bare `$25.99` — ambiguous between USD/NTD/HKD/CNY; always disambiguate.
- `25+ 种语言 / 25+ 種語言` — use `25 种以上语言 / 25 種以上語言`.
- `{seconds}` without `秒` — bare placeholder reads as raw number.
- `每种语言 / 每種語言` for `for 5 languages` (total) — FOR/PER inverted, should be `5 种语言共计 / 5 種語言共計`.
- `创建的 {date} / 建立的 {date}` — should be `创建于 {date} / 建立於 {date}`.
- Mixed `您/你` in same document.
- HK content with `民國` calendar reference — never appropriate.
- TW content using `內地` — wrong framing, use `中國大陸`.
- CN content using `中華民國` — politically inappropriate for PRC distribution.
