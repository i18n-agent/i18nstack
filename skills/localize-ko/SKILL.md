---
name: localize-ko
description: "Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Korean (ko). Enforces 존댓말 speech-level consistency, 받침-based particle selection (including loanword pronunciation), SOV restructuring, Konglish false-friend avoidance, and native-Korean preference over transliterations."
---

# Korean Translation Rules (ko / 한국어)

Distilled from the production translation prompts. Follow these rules verbatim — they are model-agnostic and produce consistent native-quality Korean output.

## Mindset

> 당신은 한국어 원어민 작가로서 영어 직역체나 부자연스러운 한국어 표현을 매우 싫어합니다.

You are a strict Korean native writer who rejects English-style direct translation and Konglish. Preserve meaning, restructure ALL English SVO into SOV, and prefer native Korean over transliterated English when both exist.

## Pre-Translation Setup

Lock in before translating:

1. **Speech level (존댓말)** — Default to **해요체 (Polite)** for modern UI, or **하십시오체 (Formal)** for official docs. NEVER use **해체 (Casual)** in professional contexts. Never mix levels.
2. **SOV word order** — Restructure all English SVO sentences.
3. **Pro-drop language** — Omit 당신/너/저 when context is clear.
4. **Half-width punctuation** — Korean uses ASCII punctuation (unlike Japanese/Chinese).
5. **Placeholders** — Preserve `{variables}` and ICU plural syntax exactly.

## Register Auto-Detection (run after Pre-Translation Setup, before translating)

If the user has NOT explicitly specified the speech level, infer it from the source text register. Match the output to the source — formal source → 하십시오체, informal source → 해요체. NEVER use 해체 (casual) regardless of source informality — it is forbidden in professional UI.

### Formal source signals → output 하십시오체 (-습니다 / -ㅂ니다 / -십시오)
- Hedging / polite modals: "please", "kindly", "we recommend", "we kindly request", "could you", "would you mind"
- Passive / impersonal: "users are advised", "it is recommended", "applicants must"
- No contractions, full sentences, formal connectors
- Domain vocabulary: legal, financial, healthcare, regulatory, enterprise B2B, government, insurance
- Third-person / distance: "the user must", "customers should"
- Brand voice: bank, insurance, government, B2B SaaS, healthcare, legal tech
- No exclamations or emojis

### Informal source signals → output 해요체 (-어요 / -아요 / -세요)
- Contractions: "don't", "you'll", "it's", "we're"
- Casual greetings: "hey", "hi there", "yo", "what's up", "hi 👋"
- Second-person directness, exclamations, emoji presence (🎉 😎 🚀 ✨)
- Slang: "cool", "awesome", "no worries", "kinda"
- Consumer-app voice: gaming, social, lifestyle, dating, fitness, kids
- Sentence fragments and conversational filler

### Mixed / ambiguous source → default to 해요체
Modern Korean software defaults to 해요체 (polite but friendly). 하십시오체 reserved for explicitly formal / government / banking / very B2B.

### Explicit user override
If the user says "use formal speech" / "use 하십시오체" / "make it casual" — their instruction wins.

### Worked examples

| Source | Detected register | Korean output style |
|----------------|-------------------|---------------------|
| "Please review the terms of service before proceeding." | formal | 진행하기 전에 이용 약관을 확인하십시오. |
| "Hey! Tap here to get started — it's super quick 🚀" | informal (해요체) | 안녕하세요! 여기를 눌러 시작하세요. 정말 빨라요 🚀 |
| "Submit your application by the deadline." | formal | 기한 내에 신청서를 제출하십시오. |
| "Don't forget to save your work!" | informal (해요체) | 작업을 저장하는 것을 잊지 마세요! |

After detection: keep the chosen speech level consistent throughout the file. The no-mixing rule still applies.

## Critical Accuracy Rules (NEVER violate)

### 1. Particles by final sound (받침)

| Sound | Subject | Object | Topic | And |
|-------|---------|--------|-------|-----|
| Ends in **consonant** (받침 O) | 이 | 을 | 은 | 과 |
| Ends in **vowel** (받침 X) | 가 | 를 | 는 | 와 |

**Loanwords / abbreviations** — choose particle by KOREAN PRONUNCIATION of the final syllable:

| Loanword | Korean reading | Final | Particle |
|----------|----------------|-------|----------|
| Google | 구글 | 글 (받침 ㄹ) | 을 / 이 / 은 |
| API | 에이피아이 | 이 (vowel) | 를 / 가 / 는 |
| GPT-5 | 파이브 | 브 (vowel ㅡ) | 를 / 가 / 는 |
| RTL | 알티엘 | 엘 (받침 ㄹ) | 을 / 이 / 은 |
| USB | 유에스비 | 비 (vowel) | 를 / 가 / 는 |

**NEVER output both particles** like `RTL을(를)` or `이(가)` — that is a mechanical artifact. Always pick exactly one based on pronunciation.

### 2. Word vs Character — completely different

| English | Wrong | Correct |
|---------|-------|---------|
| word count | 글자 수 | **단어 수** |
| character count | 단어 수 | **글자 수** |

word = 단어 ; character = 글자.

### 3. FOR vs PER — total vs rate

| English | Wrong | Correct |
|---------|-------|---------|
| for # languages (total) | #언어당 | **#개 언어에 대해 / #개 언어 기준** |
| per language (rate) | 언어에 대해 | **언어당 / 각 언어마다** |

### 4. Measurement unit words after numeric placeholders

| Wrong | Correct |
|-------|---------|
| {seconds} 후 삭제 | {seconds}**초** 후 삭제 |
| {minutes} 후 재시도 | {minutes}**분** 후 재시도 |
| 남은 시간: {hours} | 남은 시간: {hours}**시간** |
| {days} 이내 완료 | {days}**일** 이내 완료 |

### 5. Temporal expression agreement

| Meaning | Use | Don't use |
|---------|-----|-----------|
| Countdown / future | ~후 (after) | ~중 (means "during") |
| Ongoing status | ~중 / ~하는 중 | ~후 |
| Deadline | ~이내 (within) | — |

`{days}일 중` is wrong — means "during the daytime". Use `{days}일 후`.

### 6. Placeholder type markers

| Wrong | Correct |
|-------|---------|
| {formatList} 파일 지원 | {formatList} **형식의** 파일 지원 |
| {languageList} 콘텐츠 | {languageList} **언어의** 콘텐츠 |

### 7. Measure words (분류사)

| Counter | Use for |
|---------|---------|
| 개 | General items, languages |
| 명 | People |
| 건 | Cases / records |
| 가지 | Types / kinds |
| 번 | Times / counts |

Wrong: `{count}언어` → Correct: `{count}**개** 언어`.
Wrong: `{count}명 언어` → 명 is for people, not items.

## Native vs Sino-Korean Numerals

Korean has **two number systems**, and the wrong system with a counter is immediately wrong to native ears.

### Two number systems

| # | Native Korean (고유어) | Sino-Korean (한자어) |
|---|------------------------|-----------------------|
| 1 | 하나 (하나/한) | 일 |
| 2 | 둘 (둘/두) | 이 |
| 3 | 셋 (셋/세) | 삼 |
| 4 | 넷 (넷/네) | 사 |
| 5 | 다섯 | 오 |
| 6 | 여섯 | 육 |
| 7 | 일곱 | 칠 |
| 8 | 여덟 | 팔 |
| 9 | 아홉 | 구 |
| 10 | 열 | 십 |
| 20 | 스물 (스무) | 이십 |
| 30 | 서른 | 삼십 |
| 40 | 마흔 | 사십 |
| 50 | 쉰 | 오십 |
| 60 | 예순 | 육십 |
| 70 | 일흔 | 칠십 |
| 80 | 여든 | 팔십 |
| 90 | 아흔 | 구십 |
| 100 | 백 (Sino-only past 99) | 백 |
| 1000 | — | 천 |
| 10000 | — | 만 |
| 100000000 | — | 억 |

Native numbers stop at 99; from 100 up, Korean uses Sino-Korean.

### Use NATIVE numbers with these counters

| Counter | Meaning | Example |
|---------|---------|---------|
| 개 | general items | 세 개 (3 items) |
| 명 | people | 다섯 명 (5 people) |
| 분 | people (honorific) | 두 분 (2 people, polite) |
| 살 | age in years | 스무 살 (20 years old) |
| 시 | clock hour | 열두 시 (12 o'clock) |
| 마리 | animals | 한 마리 (1 animal) |
| 권 | books | 세 권 (3 books) |
| 잔 | cups | 두 잔 (2 cups) |
| 병 | bottles | 한 병 (1 bottle) |
| 그릇 | bowls | 두 그릇 (2 bowls) |

Note attributive forms when modifying a counter: 하나 → 한, 둘 → 두, 셋 → 세, 넷 → 네, 스물 → 스무. (`한 개`, NOT `하나 개`.)

### Use SINO-KOREAN numbers with these counters

| Counter | Meaning | Example |
|---------|---------|---------|
| 분 | minutes | 삼십 분 (30 minutes) |
| 초 | seconds | 십 초 (10 seconds) |
| 일 | days | 오 일 (5 days) |
| 월 | months | 삼 월 (March) |
| 년 | years | 이천이십사 년 (year 2024) |
| 번 | number / ordinal | 일 번 (number 1) |
| 원 | won (currency) | 오천 원 (5,000 won) |
| 층 | floor | 오 층 (5th floor) |
| 호 | room/number | 삼백일 호 (room 301) |
| 차 | sequence / nth | 일 차 (1st round) |
| 인분 | servings | 이 인분 (2 servings) |

### Mixed pattern for time
- Hour = native, Minute = Sino-Korean: `세 시 삼십 분` (3:30)
- `오후 두 시 십오 분` (2:15 PM)
- In digital UI, prefer numerals + units: `14:30` or `오후 2시 30분` (where 2 reads as 두 [native] and 30 reads as 삼십 [Sino]).

### Common UI pitfalls

| Wrong | Correct |
|-------|---------|
| 일 개 (1 item) | **한 개** |
| 삼 명 (3 people) | **세 명** |
| 두 분 (2 minutes — time) | **이 분** |
| 다섯 원 (5 won) | **오 원** |
| 한 초 (1 second) | **일 초** |
| 이 살 (2 years old) | **두 살** |

### 8. Plural marker 들 — omit when number is present

Wrong: `{count}개 파일들` → Correct: `{count}개 파일`.

### 9. Domain terminology — use IT loanwords

| Source | Wrong (literal) | Correct (IT term) |
|--------|-----------------|---------------------|
| architecture | 건축 | **아키텍처** |
| pipeline (CI/CD) | 배관 | **파이프라인** |
| deploy | 배치하다 (military) | **배포하다** |
| source of truth | 진실의 원천 | **정보의 원천 / 기준점** |
| bug (software) | 벌레 | **버그** |

## UI Conventions

### Buttons — verb stem / noun form

| Wrong | Correct |
|-------|---------|
| 프로젝트를 생성합니다 | **프로젝트 생성** |
| 저장합니다 | **저장** |

### Status messages — ongoing → ~중

| Wrong | Correct |
|-------|---------|
| 번역하다 | **번역 중 / 번역하는 중** |
| 업로드하다 | **업로드 중...** |

### Completion messages — ~완료 / ~되었습니다

| Wrong | Correct |
|-------|---------|
| 저장하다 | **저장 완료 / 저장되었습니다** |
| 번역하다 | **번역이 완료되었습니다** |
| 업로드 중 (for completed) | **업로드 완료** |

### Empty state — negative existence

| Wrong | Correct |
|-------|---------|
| 결과가 비어 있습니다 | **결과가 없습니다 / 결과를 찾을 수 없습니다** |
| 선택 안 됨 | **선택된 항목이 없습니다** |

### Drag and drop

| English | Korean |
|---------|--------|
| drag | 드래그 |
| drop | 드롭 / 놓기 |
| **release** (let go) | **놓다 / 드롭하다** — NOT 허용 (permit) |
| **browse** (file picker) | **찾아보기 / 파일 선택** — NOT 브라우즈 |

### Validation messages

Connectors: 및 / 과 (and), 또는 (or), 만 / 뿐 (only).

- Wrong: `3-50자, 문자, 숫자, 하이픈만`
- Correct: `3-50자, 사용 가능: 영문자, 숫자, 하이픈`

### Other UI patterns

| Wrong | Correct | Reason |
|-------|---------|--------|
| 대체 감지 | **대체 감지 방법** | Labels need complete noun phrases |
| 자동 (bare) | **자동 모드 / 자동 감지** | Add completing noun |
| 25+언어 | **25개 이상의 언어** | "N+" → N개 이상의 ~ |
| +{count} 더 | **외 {count}개** | "+N more" pattern |

## Speech Level Consistency

NEVER mix levels in same context.

| Don't mix | Use |
|-----------|-----|
| 변경하세요 + 눌러 | 변경하세요 + 누르세요 (해요체) |
| 확인하십시오 + 저장했어요 | 확인하십시오 + 저장되었습니다 (하십시오체) |

UI labels (buttons/nouns) stay in stem/noun form regardless of speech level.

## Politeness Softeners

Korean has fine-grained politeness markers that soften requests, questions, and statements. Use sparingly — overuse sounds obsequious.

### Softening adverbs

| Marker | Romanization | Function | Example |
|--------|--------------|----------|---------|
| 좀 | jom | "a little" / "please" — conversational softener | `좀 기다려 주세요` (please wait) — softer than `잠시만 기다려 주세요` |
| 부디 | budi | "kindly" / "please earnestly" — formal | `부디 확인해 주시기 바랍니다` (we kindly request your confirmation) |
| 혹시 | hoksi | "by any chance" — softens questions / hedges | `혹시 시간이 있으신가요?` (do you happen to have time?) |
| 잠시 | jamsi | "for a moment" — buffers requests | `잠시만요` (one moment please) |
| 아무쪼록 | amujjorok | "in any case" / "above all" — earnest hope | `아무쪼록 양해 부탁드립니다` (we earnestly ask for your understanding) |

### ~주세요 ending (CRITICAL)

The `~주세요` ending is the standard polite request marker in 해요체. **Do NOT omit it** when making a request — bare imperatives sound rude.

| Wrong (bare) | Correct (with 주세요) |
|--------------|-----------------------|
| 확인해 | **확인해 주세요** |
| 기다려 | **기다려 주세요** |
| 입력해 | **입력해 주세요** |

### ~시- honorific infix (subject elevation)

The `~시~` infix elevates the **subject** of the verb (the person doing the action). It produces honorific verb stems.

| Plain verb | Honorific form | Meaning |
|------------|----------------|---------|
| 가다 (go) | 가시다 | (someone respected) goes |
| 먹다 (eat) | 잡수시다 | (someone respected) eats |
| 있다 (be / exist) | 계시다 | (someone respected) is present |
| 자다 (sleep) | 주무시다 | (someone respected) sleeps |
| 말하다 (say) | 말씀하시다 | (someone respected) speaks |

### 드리다 vs 주시다 (give — directionality matters)

| Form | Direction | Use |
|------|-----------|-----|
| 드리다 | I give → you (humble, lowering self) | `말씀 드리겠습니다` (I will tell you, humble) |
| 주시다 | You give → me (honorific, elevating other) | `알려 주세요` (please tell me) |

Mixing them up sounds reversed — 드리다 must elevate the receiver, 주시다 must elevate the giver.

## Punctuation — half-width (ASCII)

Korean is unlike Japanese/Chinese — use standard ASCII punctuation, no full-width.

| Wrong | Correct |
|-------|---------|
| 상태 : 완료 | 상태**:** 완료 |

- Decimal: `.`  Thousands: `,` Quotation: `"..."` or `'...'`

### Full-width brackets — title/quotation contexts only

While modern Korean UI uses Western punctuation (`"..."`), specific contexts DO use full-width brackets:

| Bracket | Use for | Example |
|---------|---------|---------|
| 『 』 | Book titles | 『나미야 잡화점의 기적』 |
| 「 」 | Chapter titles, short works, quoted titles within a work | 「제3장: 시작」 |
| 〈 〉 or 《 》 | Movies, albums, songs, exhibitions, performances | 〈기생충〉, 《BE》 (BTS album) |

For inline UI prose, prefer Western quotes `"..."` or `'...'`. Use full-width brackets only when explicitly citing media titles in editorial / marketing copy.

## Spacing (띄어쓰기)

- **Space** between Korean and Latin script/numbers: `API 설정` not `API설정`, `합계 10건` not `합계10건`.
- **No space** between a Korean stem and its suffix/particle: `저장하기` not `저장 하기`.

## Native vs Loanword — prefer native for UI

| Avoid (transliterated) | Use (native) |
|------------------------|--------------|
| 세이브 | 저장 |
| 세팅 | 설정 |
| 셀렉트 | 선택 |
| 캔슬 | 취소 |
| 딜리트 | 삭제 |
| 에딧 | 편집 |
| 서치 | 검색 |

**Spelling that natives expect** (revised orthography):

| Wrong | Correct |
|-------|---------|
| 컨텐츠 | **콘텐츠** |
| 메세지 | **메시지** |

## Konglish False Friends (콩글리시)

| Konglish | Korean meaning | Correct for English |
|----------|----------------|---------------------|
| 서비스 | free bonus / complimentary | 서비스 (only if literally "service") |
| 핸드폰 | hand phone (Konglish) | **휴대폰 / 스마트폰** |
| 미팅 | group blind date | **회의** (business meeting) |
| 원샷 | "drink in one gulp" | **한 번에 / 단번에** |

## Calques to avoid

| Literal (wrong) | Natural Korean |
|-----------------|-----------------|
| 말이 된다 | 이치에 맞다 / 합리적이다 |
| 하루의 끝에 | 결국 / 궁극적으로 |
| 테이블 위에 있다 (abstract) | 논의 중이다 |
| 공은 당신 코트에 | 당신에게 달렸습니다 |
| 정말로 아니다 ("not really") | 실제로는 아니다 / 그렇지 않다 |
| Break a leg | 화이팅! / 행운을 빕니다 |
| Piece of cake | 식은 죽 먹기 / 누워서 떡 먹기 |
| When pigs fly | 해가 서쪽에서 뜨면 |

## Compound Adjectives

| English | Wrong | Correct |
|---------|-------|---------|
| X-aware | 컨텍스트 어웨어 | **문맥을 인식하는** |
| AI-powered/driven | AI 구동형 | **AI 기반 / AI 활용** |

## Compound Descriptive Nouns

Decompose English compounds, rebuild naturally.

- "mom creators" → `엄마 크리에이터` or `육아 크리에이터` (NOT `어머니 창작자`)
- "niche creators" → `니치 크리에이터` or `틈새시장 크리에이터`
- "English-speaking customer service" → `영어 고객 서비스` (compound adjective, not relative clause)

## UI Element Reference in Prose

When referencing a UI label by name in prose, use quotes or brackets:

- Wrong: `이름의 필드` → Correct: `'이름' 필드` or `[이름] 필드`
- Wrong: `계정의 탭` → Correct: `'계정' 탭`
- Generic elements (`검색창`) need no quotes.

## Spatial Metaphor Prepositions

| English (figurative) | Use | Don't use |
|---------------------|-----|-----------|
| under [category] | ~에서 / ~ 중에서 | ~ 아래에 |
| on top of (in addition to) | ~에 더해 / ~외에도 | ~ 위에 |
| behind the scenes | 비하인드 / 무대 뒤 | (literal) |
| within [timeframe] | ~ 이내에 / ~ 안에 | ~ 내부에 |

## Temporal Simile Restructuring

| English | Wrong (literal) | Natural |
|---------|-----------------|---------|
| operating like it's 1995 | 1995년처럼 운영하고 있다 | **1995년에서 멈춰 있다 / 1995년 이후로 변한 게 없다** |
| stuck in [YEAR] | [YEAR]년 그대로 운영 중이다 | **[YEAR]년 이후로 발전이 없다 / 아직도 [YEAR]년 방식이다** |

## Polysemy — pick the right sense

| Word | Wrong (literal) | Correct (contextual) |
|------|-----------------|--------------------|
| copy (marketing) | 복사 | **문구 / 카피** |
| sauce (figurative) | 소스 (양념) | **비결 / 핵심 요소** |
| bug (software) | 벌레 | **버그** |
| resume (verb) | 이력서 | **재개하다** |

## Proper Nouns — use natural Korean forms

| Wrong | Correct |
|-------|---------|
| 오스트레일리아 | **호주** |
| 아메리카 합중국 | **미국** |
| 그레이트 브리튼 | **영국** |
| 미국 영어 | **미국식 영어** (use X식 for language variants) |

## Tense / Aspect Fidelity

Don't flatten ongoing/habitual into completed actions.

| English (ongoing) | Wrong (past) | Correct (progressive) |
|--------|--------------|------------------------|
| we are building | 우리가 구축했습니다 | **우리가 구축하고 있습니다** |
| costs are increasing | 비용이 증가했다 | **비용이 증가하고 있다** |
| announcing X (habitual) | 말했습니다 | **말하고 다닙니다 / 말하곤 합니다** |

## Question / Confirmation Phrasing

- Wrong: `당신은 확실합니까?` → Correct: `확실하신가요?`
- Wrong: `삭제할래?` → Correct: `삭제하시겠습니까?`
- Omit unnecessary subjects.

## Brand Name Rules

- Brand + Korean noun: space between them. `Airbnb 앱` or `에어비앤비 앱`.
- Technical abbreviations stay as-is: `API`, `URL`, `ID`.

## Honorific Suffix 님 / Name Forms

Korean uses the honorific suffix **님** attached to names and titles in formal address. Unlike Japanese `-san`, Korean does not have a standalone name suffix — instead `님` attaches to **titles** (job/role), and `title + 님` works similarly.

### Title + 님 (formal address)

| Form | Meaning | Context |
|------|---------|---------|
| 김 선생님 | Mr./Ms. Kim (teacher / respected) | School, formal address |
| 이 부장님 | Manager Lee | Office, hierarchy |
| 박 사장님 | President/CEO Park | Business |
| 최 교수님 | Professor Choi | Academic |
| 정 의사님 | Dr. Jung | Medical |

### UI honorific forms

| Form | Meaning | When to use |
|------|---------|-------------|
| 고객님 | Dear customer | Customer-facing copy, support, e-commerce |
| 회원님 | Dear member | Membership / subscription apps |
| 손님 | Guest | Hospitality, retail, restaurants |
| 사용자 | User | Technical UI — **no 님** in dev/admin/dashboards |
| 사용자님 | Dear user | Rare; only in very polite consumer copy |

### Email / greeting addressing

- `안녕하세요, 김철수 님` — Hello, Mr. Kim Chul-soo (space before 님 after a full name)
- `김철수 고객님` — Customer Kim Chul-soo
- `회원님께` — To dear member (with dative particle 께)

### Rules
- Attach `님` to **titles**, not bare given names in technical UI.
- Use space between full name and `님`: `김철수 님`, not `김철수님` (though both are seen; space form is more correct in formal copy).
- Drop `님` in technical/dev UI: `사용자 ID`, `사용자 권한` — never `사용자님 ID`.

## Greetings & Closing Protocols

| Phrase | Meaning | Context |
|--------|---------|---------|
| 안녕하세요 | Hello / Hi (universal polite) | Any UI greeting, opening, customer support |
| 안녕히 가세요 | Goodbye (to person LEAVING) | Said by the person staying |
| 안녕히 계세요 | Goodbye (to person STAYING) | Said by the person leaving |
| 좋은 아침입니다 | Good morning (polite) | Morning greetings, B2B |
| 반갑습니다 | Nice to meet you (formal) | First-time greetings |
| 환영합니다 | Welcome (formal) | Onboarding, landing, signup confirmation |
| 어서 오세요 | Welcome (warmer, retail/hospitality) | E-commerce, app entrance |
| 감사합니다 | Thank you (formal) | Default polite thanks |
| 고맙습니다 | Thank you (slightly warmer) | Friendly polite thanks |

### Direction rule for 가세요 vs 계세요

The departure direction determines which to use:
- The person who is **leaving** says `안녕히 계세요` (stay well).
- The person who is **staying** says `안녕히 가세요` (go well).

App goodbye screens default to `안녕히 가세요` since the app is "staying" and the user is "leaving".

## Empty State Alternatives

Different empty states need different phrasings. Don't use one for all.

| English | Korean | When |
|---------|--------|------|
| No results | **결과가 없습니다** | Search returned 0 hits |
| No items | **항목이 없습니다** | List/table empty |
| No data | **데이터가 없습니다** | Chart/dashboard empty |
| Nothing to show | **표시할 내용이 없습니다** | Generic placeholder |
| File not found | **파일을 찾을 수 없습니다** | 404 / missing resource |
| No notifications | **알림이 없습니다** | Notification panel |
| No messages | **메시지가 없습니다** | Inbox/chat empty |
| No history | **기록이 없습니다** | Activity log empty |

Avoid `비어 있습니다` (literally "is empty") for search/results — sounds odd. Reserve for explicit container states like 폴더가 비어 있습니다 (the folder is empty).

## Calendar / Time Conventions

| Item | Consumer apps | B2B / Technical |
|------|---------------|-----------------|
| Time of day | `오전 9시` / `오후 2시 30분` | `09:00` / `14:30` (24h) |
| Date | `2024년 1월 15일` | `2024-01-15` / `2024.01.15` |
| Day of week | `금요일` (Friday) | `(금)` (abbreviated) |
| Relative | `오늘`, `내일`, `어제`, `모레` (today, tomorrow, yesterday, day after) | — |

Prefer `오전 / 오후` over `AM / PM` in consumer-facing copy. Use 24-hour format in admin dashboards, schedule UI, and technical contexts.

## Cultural Conventions

| Item | Format |
|------|--------|
| Date | `2024년 1월 15일` or `2024.01.15` (NOT `01/15/2024`) |
| Time | `오후 2시 30분` or `14:30` |
| Currency | `1,000원` or `₩1,000` |

## Cost / Estimate Expression Ordering

- Pattern A (amount-first): `예상 비용: {credits} 크레딧 ({count}개 언어)`
- Pattern B (scope + 총): `{count}개 언어 총 {credits} 크레딧`
- Wrong (ambiguous): `{count}개 언어 {credits} 크레딧`.

## Redundant Modifiers — remove

| Wrong | Correct |
|-------|---------|
| 최소 {min}자 길이 | 최소 {min}자 / {min}자 이상 |
| 당신의 파일을 저장 | 파일 저장 (omit possessive) |

## UI Tone Vocabulary

| English | Wrong | Correct |
|---------|-------|---------|
| casual tone | 캐주얼한 톤 (=fashion) | **편안한 톤 / 격식 없는 톤** |
| formal | 격식 없음 | **격식체** |
| professional | (literal) | **전문적** |

## Self-Check Checklist (run before finalizing)

### Accuracy
- [ ] Particles correct for final 받침 (이/가, 을/를, 은/는, 과/와)
- [ ] Loanword particles chosen by Korean pronunciation (GPT-5[파이브]→가, RTL[알티엘]→은)
- [ ] No mechanical artifacts (`을(를)`, `이(가)` — pick one)
- [ ] Speech level consistent throughout (해요체 OR 하십시오체)
- [ ] UI buttons in stem/noun form; sentences in speech level
- [ ] Measure words appropriate (개/명/건/가지/번)
- [ ] Word vs character not confused (단어 vs 글자)
- [ ] FOR vs PER not confused (~에 대해 vs ~당)
- [ ] Unit words after numeric placeholders (초/분/시간/일)
- [ ] Temporal: ~후 for countdowns, ~중 for ongoing, ~이내 for deadlines
- [ ] Placeholder type markers (형식의, 언어의)
- [ ] Half-width (ASCII) punctuation
- [ ] No space before colon
- [ ] SOV word order
- [ ] Spacing: gap between Korean ⇄ Latin/numbers; no internal gap (저장하기)
- [ ] All `{variables}` and ICU intact
- [ ] Standard spelling (콘텐츠 not 컨텐츠, 메시지 not 메세지)
- [ ] Domain terminology uses IT loanwords (아키텍처, 배포, 파이프라인)

### Naturalness
- [ ] UI labels are complete noun phrases (대체 감지 방법)
- [ ] Cost expressions use amount-first or scope+총 pattern
- [ ] Tone vocabulary correct (편안한, NOT 캐주얼)
- [ ] No English calques
- [ ] Konglish false friends caught (서비스, 미팅, 핸드폰)
- [ ] Pronouns omitted when context clear (no 당신/너)
- [ ] Compound adjectives natural (AI 기반, NOT AI 구동형)
- [ ] Drag-drop verbs correct (놓다 for release, NOT 허용)
- [ ] Native term over transliteration (저장 > 세이브)
- [ ] Compound nouns restructured (엄마 크리에이터, NOT 어머니 창작자)
- [ ] UI labels in prose use quotes/brackets ('이름' 필드)
- [ ] Spatial metaphors adapted (인기 주제에서, NOT 인기 주제 아래에)
- [ ] Proper nouns naturalized (호주, 미국, 영국)
- [ ] Validation messages clear with 및/또는/만
- [ ] Tense/aspect preserved (~하고 있다 for ongoing)

## Worked Example

**Source:** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

**Wrong (literal):**
환영합니다! 업로드를 위해 당신의 파일을 브라우즈하세요 — 우리는 25+ 포맷을 서포트하고 5언어당 {seconds}에 그것을 번역합니다. 걱정 말아요, 언제든지 캔슬할 수 있어요.

**Issues:** `당신의` (redundant), `브라우즈` (Konglish), `서포트` (transliteration), `25+` (not natural), `5언어당` (FOR/PER confusion), `{seconds}` (missing 초), `캔슬` (use 취소), mixed speech levels (~해요 + ~합니다).

**Correct:**
환영합니다! 업로드할 파일을 선택해 주세요. 25개 이상의 형식을 지원하며, 5개 언어에 대해 {seconds}초 이내에 번역합니다. 언제든지 취소할 수 있습니다.
