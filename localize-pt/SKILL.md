---
name: localize-pt
description: Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Portuguese (pt). Asks the user to choose between Brazilian (pt-BR) and European (pt-PT) on first use, then enforces variant-specific verb construction (gerund vs a+infinitivo), pronoun placement (proclisis vs enclisis), article+possessive rules, vocabulary, AO90 orthography, and currency.
---

# Portuguese Translation Rules (pt / Português)

Distilled from the production translation prompts (`pt.ts`, `pt-br.ts`, `pt-pt.ts`). Follow these rules verbatim — they are model-agnostic and produce consistent native-quality Portuguese output.

## Mindset

> Você é um escritor nativo extremamente exigente que detesta traduções literais do inglês e construções pouco naturais.

Reject literal English calques. Restructure fully into natural Portuguese. Brazilian Portuguese is more tolerant of anglicisms (mouse, link, deploy); European Portuguese is stricter (rato, ligação, implementar).

## Variant Selection (run FIRST)

Brazilian (pt-BR) and European (pt-PT) Portuguese **directly conflict** on many fundamental things — verb construction (`está fazendo` vs `está a fazer`), pronoun placement (`Me diga` vs `Diga-me`), article+possessive (`seu arquivo` vs `o seu ficheiro`), most everyday vocabulary, currency, and register defaults. Applying the wrong variant produces output that reads as foreign to native speakers of the other.

**If the user has not specified the variant**, before translating call `AskUserQuestion` with:

- Question: `Which Portuguese variant should I target?`
- Header: `PT variant`
- Options:
  1. **Brazilian (pt-BR)** — `você` standard, gerund (`está fazendo`), proclisis (`Me diga`), no article with possessive (`seu arquivo`), `arquivo/salvar/usuário/celular`, R$, warmer tone. ~210M speakers — the default for most consumer products.
  2. **European (pt-PT)** — `tu/você/o senhor`, `a + infinitivo` (`está a fazer`), enclitic (`Diga-me`), article with possessive (`o seu ficheiro`), `ficheiro/guardar/utilizador/telemóvel`, €, formal default, AO90 spelling. ~10M speakers in Portugal + Lusophone Africa.

**If the user picks pt-BR**, apply the **Universal Portuguese base** + **pt-BR Deltas**. Do NOT apply European rules.

**If the user picks pt-PT**, apply the **Universal Portuguese base** + **pt-PT Deltas**. Do NOT apply Brazilian rules.

## Pre-Translation Setup

Lock in before translating:

1. **Variant** — confirmed above.
2. **Formality** — depends on variant. pt-BR: `você` is the standard for all professional contexts. pt-PT: choose from `tu` (informal), `você` (semi-formal), `o senhor/a senhora` (very formal). NEVER mix within a file.
3. **Two genders** — o (masc), a (fem). Articles, adjectives, participles all agree.
4. **Word order** — SVO; most adjectives follow the noun.
5. **Placeholders** — Preserve `{variables}` and ICU plural syntax exactly.

## Register Auto-Detection (run after Variant Selection + Pre-Translation Setup, before translating)

If the user has NOT specified formality, infer from source text register. The formality systems differ DRAMATICALLY by variant:

- **pt-BR**: `você` works as both formal and informal. Register signaled by contractions, exclamations, slang, NOT by pronoun choice. Informal pt-BR may use `pra` (= para), `tá` (= está), `tô` (= estou), `né` (= não é). Formal pt-BR keeps full forms.
- **pt-PT**: three-level system (tu / você / o senhor). Formal source → você or o senhor; informal source → tu.

### Formal source signals → pt-PT: você/o senhor + article+possessive (`o seu ficheiro`); pt-BR: `você` + full forms (no `pra/tá/tô`)
- Hedging / polite modals: "please", "kindly", "we recommend", "could you"
- Passive / impersonal: "users are advised", "it is recommended", "applicants must"
- No contractions: "do not", "cannot", "we will"
- Domain vocabulary: legal, financial, healthcare, regulatory, enterprise B2B, government, insurance
- Third-person / distance, long sentences, formal connectors
- Brand voice: bank, insurance, government, B2B SaaS, healthcare, legal tech
- No exclamations or emojis

### Informal source signals → pt-PT: `tu` + verb conjugation; pt-BR: `você` + permitted contractions (`pra/tá/tô`) + warmer tone
- Contractions: "don't", "you'll", "it's", "we're"
- Casual greetings: "hey", "hi there", "yo", "hi 👋"
- Second-person directness, exclamations, emoji (🎉 😎 🚀 ✨)
- Slang: "cool", "awesome", "no worries", "kinda"
- Consumer-app voice: gaming, social, lifestyle, dating, fitness, kids
- Sentence fragments and conversational filler

### Mixed / ambiguous source → default to FORMAL
- pt-PT: default to **você** (semi-formal) — safest mid-ground; reserve `tu` for clearly casual / `o senhor` for clearly very formal.
- pt-BR: default to **você** with full forms (no contractions like `pra/tá`).

### pt-BR informal contraction markers (register, NOT a separate pronoun system)
| Formal pt-BR | Informal pt-BR |
|--------------|----------------|
| `para` | `pra` |
| `está / estás` | `tá / tás` |
| `estou` | `tô` |
| `não é?` | `né?` |
| `você` | `cê` (very casual, avoid in software UI) |

USE informal forms ONLY when source register clearly warrants it (consumer-app gaming/social/casual voice). NEVER use in B2B/government/banking.

### Explicit user override
If the user says "use tu" / "use o senhor" / "formal" / "casual", their instruction wins.

### Worked examples

| Source | Detected | pt-BR output | pt-PT output |
|----------------|----------|---------------|---------------|
| "Please review the terms of service before proceeding." | formal | Por favor, revise os termos de serviço antes de continuar. | Por favor, leia os termos do serviço antes de continuar. |
| "Hey! Tap here to get started — it's super quick 🚀" | informal | Oi! Toque aqui pra começar — é super rápido 🚀 | Olá! Toca aqui para começares — é super rápido 🚀 |
| "Submit your application by the deadline." | formal | Envie sua candidatura até o prazo. | Submeta a sua candidatura até ao prazo. |
| "Don't forget to save your work!" | informal | Não esqueça de salvar seu trabalho! | Não te esqueças de guardar o teu trabalho! |

After detection: keep the chosen form consistent. NEVER mix register markers across pronouns, possessives, OR imperatives.

## Universal Portuguese Base (apply to BOTH variants)

### 1. Gender of common IT nouns (memorize)

| Masculine (o) | Feminine (a) |
|---------------|--------------|
| **o** problema | **a** solução |
| **o** sistema | **a** plataforma |
| **o** programa | **a** aplicação |
| **o** tema | **a** página |
| **o** idioma | **a** conexão / ligação |
| **o** mapa | **a** rede |
| **o** dia | **a** interface |
| **o** arquivo / ficheiro | **a** tabela |
| **o** software | **a** consulta |
| **o** servidor | **a** API |
| **o** navegador | **a** IA |
| **o** PDF | **a** CPU |
| **o** URL | **a** Apple (company) |
| **o** OneSky / Slack / Teams (foreign tech) | **a** tela / ecrã |

**Patterns:**
- `-ção / -são / -dade` → always feminine
- `-ma` (Greek origin) → usually masculine (problema, sistema, tema, idioma)
- **Acronyms inherit gender from expanded form** (CRITICAL): `a IA` (Inteligência Artificial), `a API` (Interface de Programação), `o PDF` (Formato), `o URL` (Localizador), `a CPU` (Unidade).

Common errors: `a problema` → `o problema`; `o plataforma` → `a plataforma`; `nosso IA` → `nossa IA`.

### 2. Article contractions (mandatory)

| Combine | → |
|---------|---|
| de + o | **do** |
| de + a | **da** |
| em + o | **no** |
| em + a | **na** |
| a + a | **à** |

`de o sistema` → `do sistema`. `em a plataforma` → `na plataforma`.

### 3. Article completeness in noun phrases (CRITICAL)

Specific known nouns require contracted articles in prepositional phrases. Exception: generic classifiers (`erro de sistema` = type of error, vs `erro do sistema` = error of THE system).

| Wrong | Correct |
|-------|---------|
| Erro de aplicação | **Erro da aplicação** |
| Configuração de conta | **Configuração da conta** |
| Estado de conexão (br) / Estado de ligação (pt) | **Estado da conexão / Estado da ligação** |
| Detalhes de transação | **Detalhes da transação** |

### 4. FOR vs PER — never confuse (CRITICAL)

| English | Wrong | Correct |
|---------|-------|---------|
| for 5 languages (total) | por idioma | **para 5 idiomas** |
| per language (rate) | para idioma | **por idioma** |

### 5. Translate English acronyms

| Wrong | Correct |
|-------|---------|
| AI translation | **tradução com IA** |
| nosso AI | **nossa IA** (IA = Inteligência Artificial, fem) |

### 6. UI button labels — infinitive form

| Wrong (imperative) | Correct (infinitive) |
|--------------------|----------------------|
| Salve / Guarde | **Salvar / Guardar** |
| Cancele | **Cancelar** |
| Exclua / Elimine | **Excluir / Eliminar** |

### 7. Completion messages — participial (NOT "bem-sucedido")

`bem-sucedido` is an adjectival calque of "successful". Use participial forms.

| Wrong | Correct (pt-BR) | Correct (pt-PT) |
|-------|------------------|------------------|
| Pagamento bem-sucedido | **Pagamento realizado** | **Pagamento efetuado / Pronto!** |
| Upload bem-sucedido | **Upload concluído / Arquivo enviado** | **Carregamento concluído / Ficheiro carregado** |
| Download completo | **Download concluído / Download finalizado** | **Transferência concluída** |
| Operação completa | **Operação concluída / Pronto!** | **Operação concluída** |

### 8. Empty state — `Não há X` or `Nenhum(a) X`

| Wrong | Correct |
|-------|---------|
| Não foram selecionados idiomas | **Não há idiomas selecionados / Nenhum idioma selecionado** |
| Não foram encontrados resultados | **Não há resultados / Nenhum resultado** |
| Sem dados | **Nenhum dado disponível / Não há dados disponíveis** |
| Vazio | **Nenhum item encontrado** |

### 9. Calques to avoid (universal)

| Wrong (literal) | Natural Portuguese |
|-----------------|---------------------|
| `faz sentido` (overused) | **`tem sentido / é lógico`** |
| `não realmente` | **`na verdade não / não exatamente`** (br) / `não propriamente` (pt) |
| `a nível de` | **`em termos de / quanto a`** |
| `numa base diária/semanal` | **`diariamente / semanalmente / todos os dias`** |
| `em termos de` | **`quanto a / no que diz respeito a / relativamente a`** |
| `[Subject] é necessário/obrigatório para [Purpose]` | **`É necessário [Subject] para [Purpose]`** |

### 10. False friends (universal)

| Wrong (English meaning) | Actual Portuguese meaning | Correct |
|--------------------------|---------------------------|---------|
| `atualmente` (for "actually") | currently | **na verdade / de fato (br) / efetivamente (pt)** |
| `eventualmente` (for "eventually") | possibly | **finalmente** |
| `realizar` (for "to realize") | to carry out | **perceber / aperceber-se (pt) / dar-se conta (br)** |
| `pretender` (for "pretend") | to intend | **fingir** |
| `suportar` (for "to tolerate") | to tolerate | **apoiar / dar suporte** (in tech context, `suportar` is accepted for "support a feature") |

### 11. Marketing "Zero X" → "Sem X"

| Wrong | Correct |
|-------|---------|
| Zero tempo de inatividade / Zero downtime | **Sem tempo de inatividade / Sem interrupções / Disponibilidade contínua** |
| Zero erros | **Sem erros / Livre de erros / Nenhum erro** |
| Zero manutenção | **Sem manutenção / Não requer manutenção** |
| Zero compromisso | **Sem compromisso / Sem obrigação** |

### 12. Adjective order — postnominal for abstract qualities

| Wrong | Correct |
|-------|---------|
| com perfeita coerência | **com uma coerência perfeita / de forma perfeitamente coerente** |
| de superior qualidade | **de qualidade superior / de alta qualidade** |
| qualidade humana (tech) | **qualidade ao nível humano / qualidade de nível humano / qualidade profissional** |

### 13. Compound adjectives — natural construction

| English pattern | Wrong | Correct |
|-----------------|-------|---------|
| AI-powered / X-powered | `IA-alimentado`, `tradução de IA` | **`com IA / inteligente / alimentado por IA / baseado em IA / tradução com IA`** |
| context-aware / X-aware | `contexto-consciente` | **`contextual / sensível ao contexto / inteligente`** |
| user-friendly | `utilizador-amigável` (pt) / `usuário-amigável` (br) | **`intuitivo / amigável / fácil de usar`** |
| cloud-based | `nuvem-baseado` | **`na nuvem / baseado na nuvem`** |
| supported formats | `formatos suportados` | **`formatos compatíveis`** (br rejects `suportados` for features) |

### 14. Software terminology — IT meaning

| English | Wrong | Correct |
|---------|-------|---------|
| build (software) | construção | **desenvolver / criar / implementar** |
| deploy | desdobrar | **implementar / colocar em produção / lançar** (pt) / **implantar / fazer deploy** (br accepts loanword) |
| support (feature) | (only `apoiar`) | **suportar / ser compatível com / incluir suporte para** (tech `suportar` is accepted) |
| sync seamlessly | sincronizar facilmente | **sincronizar automaticamente / manter sincronizado** |
| listings (app store) | listagens | **fichas da aplicação (pt) / fichas do aplicativo (br) / páginas da aplicação** |
| architecture (software) | arquitetura (construção) | **arquitetura de software** |
| pipeline (CI/CD) | canalização | **pipeline (CI/CD)** |
| source of truth | fonte da verdade | **fonte de referência / fonte autoritativa** |

### 15. Brand names — no article for platform destinations

| Wrong | Correct |
|-------|---------|
| sincronizar com a Apple App Store | **sincronizar com Apple App Store** |
| em a App Store | **em Apple App Store / em App Store** |
| publicar no o Google Play | **publicar em Google Play** |

When brand IS the subject: `A App Store oferece...` (with article OK when modified). Foreign tech brands default to masculine: `o OneSky, o Slack, o Teams`. Exception: `a Apple` (company name).

### 16. Punctuation rules (universal)

- Decimal separator: **`,`** (comma)
- Thousands separator: **`.`** (period)
- Wrong: `1,234.56` → Correct: **`1.234,56`**
- No space before colon: `Nota: isto` not `Nota : isto`
- **NO comma** before `e` / `ou`: `Salvar e fechar`
- **Comma BEFORE** `mas / porém / contudo / porque`: `simples**,** mas eficaz`

### 17. Sentence case (not Title Case)

Wrong: `Conteúdo de Texto` → Correct: **`Conteúdo do texto`** (Portuguese uses sentence case for UI strings — only first word and proper nouns capitalized).

### 17b. Orthography (Acordo Ortográfico 1990 — AO90)

AO90 applies to **BOTH** pt-BR and pt-PT — it was adopted in Brazil starting in 2009 and obligatory since 2016, and in Portugal obligatory since 2015. Do not produce pre-AO90 spellings in either variant.

Common AO90 spellings (apply universally):

| Pre-AO90 (wrong) | AO90 (correct) |
|------------------|----------------|
| projecto | **projeto** |
| acção | **ação** |
| actual | **atual** |
| óptimo | **ótimo** |

Pairs that legitimately differ between BR and PT post-AO90 (silent-consonant divergence):

| Concept | pt-BR | pt-PT |
|---------|-------|-------|
| reception | **recepção** (BR kept the `p`) | **receção** (PT dropped silent `p`) |
| fact / suit | **fato** (also means "suit") | **facto** (PT kept `c` to distinguish from `fato` = suit) |

Hyphenation under AO90 (universal):

| Old | New |
|-----|-----|
| re-escrever | **reescrever** |
| co-autor | **coautor** |
| auto-retrato | **autorretrato** |

### 18. Quantity expressions

| Wrong | Correct |
|-------|---------|
| 25+ idiomas | **mais de 25 idiomas** |
| +{count} mais (pt) / +{count} a mais (br) | **e mais {count}** (pt) / **e {count} outros / outros {count}** (br) |

### 19. Prepositional-chain simplification (max 2)

- Wrong: `produtos de cuidados da pele à noite`
- Correct: **`produtos de cuidados noturnos / cuidados noturnos da pele`**

### 20. Drag-drop (UNIVERSAL terms; variants differ on `drop`)

- drag = **`arrastar`**
- drop = **`soltar` (pt-BR)** / **`largar` (pt-PT)** — see variant deltas
- "Standard phrase": `Arrastar e soltar` (br) / `Arrastar e largar` (pt)

### 21. Block verb mood consistency

Child items must match the verb mood frame set by the parent title/heading.

| Title frame | Wrong child | Correct child |
|-------------|-------------|---------------|
| `O que você obteria:` (conditional) | `Receba uma proposta...` (imperative) | `Você receberia...` (conditional) or `Proposta no próximo dia útil...` (noun phrase) |
| `Passos a seguir:` (instructional) | `Você configuraria sua conta...` (conditional) | `Configure sua conta...` (imperative) or `Configurar sua conta...` (infinitive) |

## Diminutives (-inho / -inha) Register Impact

Brazilian Portuguese loves diminutives for warmth — they soften, add affection, or make small. European Portuguese uses them far less and perceives heavy use as overtly Brazilian.

Examples (pt-BR):

| Form | Meaning / use |
|------|----------------|
| `cafezinho` | small / friendly coffee |
| `momentinho` | "just a sec" |
| `obrigadinho` | warmer thanks |
| `tchauzinho` | cute goodbye |
| `pertinho` | very close (warm) |
| `rapidinho` | quick (informal) |

ACCEPTABLE in pt-BR consumer/marketing copy when matching warm tone, e.g.:

> `Aguarde só um momentinho...`
> `Quase pronto! Só mais um momentinho...`

AVOID diminutives in:
- **pt-PT** — perceived as overly Brazilian; use neutral forms (`um momento`, `obrigado`, `adeus`).
- **B2B / government / banking / legal / healthcare** (both variants) — sounds infantilizing and undermines authority.
- **Error messages and system status** — undermines authority; `Aguarde um momento...` not `Aguarde um momentinho...` in an error.

## Calling Forms and Titles

Honorifics, abbreviations, and email salutation/closing conventions:

| Abbrev | Expansion | Use |
|--------|-----------|-----|
| `Sr.` | Senhor | Mr. — with surname or full name: `Sr. Silva`, `Sr. João Silva`. Plural: `Srs.` |
| `Sra.` | Senhora | Mrs. / Ms. — same usage: `Sra. Santos`. Plural: `Sras.` |
| `Sr.ª / Sra.ª` | Senhora (formal abbreviated) | Common in pt-PT formal writing |
| `Srta.` | Senhorita | Miss — dated in pt-PT, still used in pt-BR for unmarried / young |
| `Dr. / Dra.` | Doutor / Doutora | PhD holders, medical doctors, AND in Brazil broadly for educated professionals (lawyers, dentists) |
| `Prof. / Prof.ª` | Professor / Professora | Teachers, professors |
| `Eng. / Eng.ª` | Engenheiro / Engenheira | Engineer — used with surname in formal Portugal context |

Email salutations:

| Register | Form |
|----------|------|
| Formal | `Caro/a Sr./Sra. [Apellido],` or `Prezado/a Sr./Sra. [Apellido]:` |
| Informal (pt-BR) | `Olá, [Nome]!` `Oi [Nome]!` |
| Informal (pt-PT) | `Olá [Nome],` |

Email closings:

| Register | pt-BR | pt-PT |
|----------|-------|-------|
| Formal | `Atenciosamente,` `Cordialmente,` | `Com os melhores cumprimentos,` `Cordialmente,` |
| Informal | `Abraços,` `Um abraço,` `Beijos,` (warm) | `Até breve,` `Cumprimentos,` |

## Greetings and Time-of-Day

| Greeting | When | Notes |
|----------|------|-------|
| `Bom dia` | morning, until ~noon | universal polite |
| `Boa tarde` | afternoon, ~noon-evening | universal polite |
| `Boa noite` | evening / night (also "goodnight") | universal polite |
| `Olá!` | any time | neutral hello |

Casual greetings:

| pt-BR | pt-PT |
|-------|-------|
| `Oi!` | `Olá!` |
| `E aí?` (what's up) | `Tudo bem?` |
| `Tudo bem?` | `Como vais?` |

UI welcome:

| Register | Form |
|----------|------|
| Formal | `Bem-vindo / Bem-vinda` (with gender agreement) |
| Informal (pt-BR) | `Olá!` or `Oi!` |
| Informal (pt-PT) | `Olá!` |

Goodbyes:

| Form | Notes |
|------|-------|
| `Tchau` | informal, both variants |
| `Adeus` | formal, more pt-PT |
| `Até logo` | see you later |
| `Até breve` | see you soon |

---

## pt-BR (Brazilian Portuguese) Deltas

Apply ONLY when the user picked Brazilian.

### A. Formality — `você` is universal

`você` is the standard pronoun for all contexts (formal and informal). `tu` exists in some regions (Rio Grande do Sul, parts of NE) but is NOT used in standard professional Brazilian UI. **NEVER use `o senhor/a senhora` in software UI** unless explicitly customer service to elderly users.

| Don't mix | Use |
|-----------|-----|
| Você pode modificar tuas configurações | **Você pode modificar suas configurações** (você + suas) |

### B. NO article with possessive (CRITICAL)

| Wrong (PT-PT style) | Correct (pt-BR) |
|---------------------|------------------|
| o seu arquivo | **seu arquivo** |
| a sua pasta | **sua pasta** |
| os seus dados | **seus dados** |

### C. Proclisis — pronoun BEFORE verb (CRITICAL)

Brazilian Portuguese places pronouns before the verb in most contexts.

| Wrong (enclitic, PT-PT) | Correct (proclisis, pt-BR) |
|--------------------------|----------------------------|
| Diga-me | **Me diga** |
| Mostre-lhe | **Mostre a ele / Mostre pra ele** |
| Dizem-se | **Se dizem** |
| Faça-o agora | **Faça isso agora** |

### D. Verb construction — gerund (CRITICAL, severity 2.0)

Brazil uses **gerund** (-ando / -endo / -indo) for ongoing actions. NEVER use `a + infinitivo`.

| Wrong (PT-PT) | Correct (pt-BR) |
|----------------|------------------|
| está a fazer | **está fazendo** |
| estou a trabalhar | **estou trabalhando** |
| está a carregar | **está carregando** |
| está a processar | **está processando** |
| está a ser atualizado (passive) | **está sendo atualizado** |
| está-se a preparar (reflexive) | **está se preparando** |

Status messages:

| Wrong (PT) | Correct (BR) |
|-----------|---------------|
| A guardar... | **Salvando...** |
| A enviar... | **Enviando...** |
| A eliminar... | **Excluindo...** |
| A carregar... | **Carregando...** |
| A processar... | **Processando...** |

### E. Brazilian preferred vocabulary

| English | Brazilian (USE) | European (AVOID in Brazil) |
|---------|------------------|----------------------------|
| file | **arquivo** | ficheiro |
| save | **salvar** | guardar |
| delete | **excluir** (avoid `eliminar/apagar/deletar`) | eliminar / apagar |
| user | **usuário** | utilizador |
| settings | **configurações** | definições |
| phone | **celular** | telemóvel |
| bus | **ônibus** | autocarro |
| train | **trem** | comboio |
| mouse | **mouse** (Brazil keeps English) | rato |
| screen | **tela** | ecrã |
| breakfast | **café da manhã** | pequeno-almoço |
| bathroom | **banheiro** | casa de banho |
| upload | **enviar / fazer upload** | carregar |
| download | **baixar / fazer download** | transferir |
| log in | **fazer login / entrar** | iniciar sessão |
| log out | **sair / fazer logout** | terminar sessão |
| email | **email / e-mail** | e-mail / correio eletrónico |
| dashboard | **painel** | painel de controlo |
| account | **conta** | conta |
| search | **pesquisar / buscar** | pesquisar |
| fix (bug) | **corrigir / resolver** (avoid `fixar`) | corrigir |

### F. Professional register — avoid casual gírias

Brazil's defaultLevel is "neutral" — warm but professional. Avoid slang in UI:

| Casual (avoid) | Professional (use) |
|----------------|---------------------|
| show de bola | **excelente** |
| que mara / top / arrasou | **ótimo / excelente** |
| tranquilo / beleza / moleza | **ok / certo / fácil** |
| minutinhos / rapidinha | **minutos / rápido** |
| pra | **para** (full form in professional contexts) |

### G. Anglicism avoidance (Brazilian, but more relaxed than PT)

| Wrong (anglicism) | Correct |
|--------------------|---------|
| deletar | **excluir** |
| checar / checkar | **verificar / conferir** |
| startar | **iniciar** |
| fixar (a bug) | **corrigir** |
| linkar | **vincular / conectar** |

(But Brazil keeps these English terms in tech: `mouse`, `link`, `dashboard`, `email`, `deploy`, `feedback` — all accepted.)

### H. Drag-drop convention (Brazilian)

- drop = **`soltar`**, release = **`soltar`**
- Wrong: `Largue aqui` (European) → Correct: **`Solte aqui`**
- `Arrastar e soltar`

### I. Currency / date / number (Brazilian)

- Currency: **`R$ 99,99`** (Brazilian Real, symbol BEFORE amount)
- Date: **DD/MM/YYYY** (`15/01/2024`) or `15 de janeiro de 2024`
- Time: 24-hour (`14h30`) or 12-hour informal
- Numbers: `1.234,56` (period thousands, comma decimal)

### J. Brazilian-specific calques and rules

- **Subjunctive (severity 1.5):** `É possível que o arquivo é corrompido` → `É possível que o arquivo esteja corrompido`. After expressions of doubt/desire/emotion/necessity.
- **Accents (severity 1.5):** `voce` → `você`; `tambem` → `também`; `e importante` → `é importante` (é=is, e=and).
- **Temporal expression "[YEAR] me" (severity 2.0–2.5):**
  - "2014 me" → `eu em 2014 / o eu de 2014` (NOT `há 2014 anos`)
  - "90s me" → `eu nos anos 90 / o eu dos anos 90`
  - "teenage me" → `eu aos 14 anos / eu na adolescência`
- **Error ownership:** `da nossa parte` (error) → `do nosso lado / por nossa parte`. `do nosso fim / da nossa ponta` (literal "on our end") → `do nosso lado`.
- **UI status calque:** `Operação falhada` → `Erro ao [verbo] / Não foi possível concluir [Noun]`.
- **Business terminology:** `tradução para empresas` → `tradução empresarial / tradução profissional`.
- **Word-sense:** `escalabilidade` in marketing → `escala / crescimento` (keep `escalabilidade` only for technical infra). `história` for "backstory" → `bastidores / a história por trás`.
- **Loanword agreement (CRITICAL, severity 2.0):** English loanwords need agreement with Portuguese adjectives.
  - `Services tradicional` → `Services tradicionais`
  - `os plugins atualizado` → `os plugins atualizados`
  - `as features novo` → `as features novas`
  - `o dashboard atualizada` → `o dashboard atualizado`

### K. Compound descriptive nouns (Brazilian)

- "mom creators" → `mamães criadoras de conteúdo` (NOT `criadoras mães`)
- "niche creators" → `criadores de nicho / criadores especializados`

### L. Spatial metaphor prepositions (Brazilian)

| English | Wrong (literal) | Correct (figurative) |
|---------|------------------|----------------------|
| under [category] (browsing) | sob / debaixo de | **entre / nos** |
| on top of (in addition to) | em cima de | **além de / junto com** |
| behind the scenes | (literal) | **nos bastidores** |
| within [timeframe] | no interior de | **em / dentro de** |

### M. UI element reference in prose (Brazilian)

- Wrong: `o campo de nome` → Correct: **`o campo 'Nome'`** or `o campo Nome`
- Wrong: `Navegar arquivos` (file picker) → Correct: **`Selecionar arquivo / Escolher arquivo`**

### N. Error message convention (Brazilian)

- Wrong: `Arquivo não encontrado.` → Correct: **`Arquivo não encontrado. Verifique o caminho.`** (include next steps)

### O. Cost ordering (Brazilian)

- Amount-first with `para`: **`R$ 99,99 para 5 idiomas`** (NOT `para 5 idiomas, R$ 99,99`)
- Wrong: `{count} idiomas {credits} créditos` → Correct: `{credits} créditos para {count} idiomas`

### P. Validation messages (Brazilian)

| Type | Mood | Example |
|------|------|---------|
| Field validation | indicative | `Este campo é obrigatório` / `Uma descrição é necessária` |
| Action instruction | imperative | `Insira um valor válido` / `Selecione pelo menos um idioma` |
| State description | impersonal | `Não foi possível conectar` / `Ocorreu um erro` |

Wrong: `Campo faltando` (calque of "missing") → `Este campo é obrigatório`. Wrong: `Inserir um valor` (infinitive in error) → `Insira um valor válido`.

---

## pt-PT (European Portuguese) Deltas

Apply ONLY when the user picked European.

### A. Formality — three levels

| Level | Pronoun | Possessive | Verb form |
|-------|---------|------------|-----------|
| Informal | **tu** | teu / tua | podes |
| Semi-formal (standard UI) | **você** | seu / sua | pode |
| Very formal (business / older) | **o senhor / a senhora** | seu / sua | pode |

NEVER mix. Consumer UI typically uses `tu`; B2B and most software defaults to `você`.

### B. Article WITH possessive (CRITICAL)

In European Portuguese, the article precedes the possessive — opposite of Brazil.

| Wrong (BR style) | Correct (pt-PT) |
|------------------|------------------|
| seu ficheiro | **o seu ficheiro** |
| sua pasta | **a sua pasta** |
| seus dados | **os seus dados** |

### C. Enclitic pronouns — pronoun AFTER verb with hyphen (CRITICAL)

| Wrong (proclisis, BR) | Correct (enclitic, pt-PT) |
|------------------------|---------------------------|
| Me diga | **Diga-me** |
| Se dizem | **Dizem-se** |
| Lhe mostre | **Mostre-lhe** |
| Pode me ajudar? | **Pode ajudar-me?** |

Exceptions when proclisis is required even in PT-PT: after negatives (`não me digas`), after question words (`quem te disse?`), after some adverbs (`já se foram`).

### D. Verb construction — "a + infinitivo" (CRITICAL, severity 2.0)

Portugal uses `estar a + infinitivo` for ongoing actions. NEVER use gerund.

| Wrong (gerund, BR) | Correct (a + inf, pt-PT) |
|---------------------|---------------------------|
| está fazendo | **está a fazer** |
| estou trabalhando | **estou a trabalhar** |
| está carregando | **está a carregar** |
| está sendo atualizado (passive) | **está a ser atualizado** |
| está se preparando (reflexive) | **está-se a preparar** |

Status messages:

| Wrong (BR) | Correct (pt-PT) |
|------------|------------------|
| Salvando... | **A guardar...** |
| Enviando... | **A enviar...** |
| Excluindo... | **A eliminar...** |
| Carregando... | **A carregar...** |
| Processando... | **A processar...** |

### E. European preferred vocabulary

| English | European (USE) | Brazilian (AVOID in Portugal) |
|---------|-----------------|--------------------------------|
| file | **ficheiro** | arquivo |
| save | **guardar** | salvar |
| delete | **eliminar / apagar** (avoid `excluir` and `deletar`) | excluir |
| user | **utilizador** | usuário |
| settings | **definições** | configurações |
| phone | **telemóvel** | celular |
| bus | **autocarro** | ônibus |
| train | **comboio** | trem |
| mouse | **rato** | mouse |
| screen | **ecrã** | tela |
| breakfast | **pequeno-almoço** | café da manhã |
| bathroom | **casa de banho** | banheiro |
| upload | **carregar** | enviar / fazer upload |
| download | **transferir** (avoid `baixar`) | baixar / fazer download |
| log in | **iniciar sessão** (avoid `fazer login`) | fazer login / entrar |
| log out | **terminar sessão** | sair / fazer logout |
| email | **e-mail / correio eletrónico** | email |
| dashboard | **painel de controlo** | painel |
| feedback | **comentários / opinião** | feedback (BR accepts) |
| analytics | **análises / estatísticas** | analytics (BR accepts) |
| workflow | **fluxo de trabalho** | workflow |
| template | **modelo** | template |

### F. AO90 (Acordo Ortográfico 1990) — modern spelling required

| Pre-AO90 (wrong) | AO90 (correct) |
|------------------|----------------|
| projecto | **projeto** |
| acção | **ação** |
| actual | **atual** |
| óptimo | **ótimo** |
| recepção | **receção** |
| colecção | **coleção** |
| excepção | **exceção** |

Hyphenation:

| Old | New |
|-----|-----|
| re-escrever | **reescrever** |
| co-autor | **coautor** |
| auto-retrato | **autorretrato** |

### G. Personal infinitive (inflected infinitive — PT-PT only feature)

Portuguese has an inflected infinitive that agrees with subject:

| Wrong | Correct |
|-------|---------|
| É importante fazer isto (nós) | **É importante fazermos isto** |
| Espero ver-vos amanhã (vós) | **Espero ver-vos amanhã** |

### G2. Pretérito perfeito composto vs simple past (PT-PT only)

In pt-PT, `tenho feito` (present perfect compound) means "I have been doing repeatedly" — an action in progress over time, NOT a single completed past action. This is the opposite of English's "have done".

| pt-PT form | Meaning |
|-----------|---------|
| `Tenho trabalhado muito ultimamente.` | I have been working a lot lately (repeated / ongoing). |
| `Fiz o trabalho ontem.` (pretérito perfeito simples) | I did the work yesterday (single completed action). |

pt-BR uses `pretérito perfeito simples` more broadly: `Fiz o trabalho hoje.` covers both "I did the work today" and contexts where pt-PT might use `tenho feito`.

Common pt-PT error (mixing perfeito composto with a specific past time marker):

| Wrong | Correct |
|-------|---------|
| `Eu tenho feito o ginásio ontem.` | **`Eu fui ao ginásio ontem.`** |
| `Tenho terminado o relatório na semana passada.` | **`Terminei o relatório na semana passada.`** |

Rule of thumb (pt-PT): if the sentence has a specific past-time anchor (`ontem`, `na semana passada`, `às 14h`), use `pretérito perfeito simples`. If the action is repeated / habitual over a recent stretch, use `tenho/tens/tem + particípio`.

### H. PT-PT-specific false friends

| Wrong (English meaning) | Actual PT meaning | Correct |
|--------------------------|-------------------|---------|
| `livraria` (for "library") | bookstore | **biblioteca** |
| `assistir` (for "assist") | to watch / attend | **ajudar** |
| `checar` | (anglicism) | **verificar** |
| `startar` | (anglicism) | **iniciar** |

### I. Drag-drop convention (European)

- drop = **`largar`**, release = **`largar`**
- Wrong: `Solte aqui` (Brazilian) → Correct: **`Largue aqui`**
- Wrong: `Permitir upload` → Correct: **`Largue para carregar`**
- `Arrastar e largar`

### J. Imperative for instructions (PT-PT convention)

Use imperative (not infinitive) for UI instructions in pt-PT:

| Wrong (infinitive) | Correct (imperative) |
|---------------------|----------------------|
| Arrastar e largar os ficheiros | **Arraste e largue os ficheiros** |
| Largar namespace aqui | **Largue o namespace aqui** |

Buttons still use infinitive: `Guardar`, `Cancelar`. Instructions use imperative.

### K. Error message patterns (PT-PT)

Action-focused:

| Wrong | Correct |
|-------|---------|
| Movimento falhou | **Falha ao mover** / **Não foi possível mover o namespace** |

### L. Stricter anglicism handling

European Portuguese rejects more anglicisms than Brazilian:

| Wrong (anglicism) | Correct |
|--------------------|---------|
| deletar | **eliminar** |
| feedback | **comentários / opinião** |
| dashboard | **painel de controlo** |
| analytics | **análises / estatísticas** |
| workflow | **fluxo de trabalho** |
| template | **modelo** |
| upload | **carregar** |
| download | **transferir** |
| login | **iniciar sessão** |

### M. Currency / date / number (European)

- Currency: **`99,99 €`** (Euro, symbol AFTER with space) or `€ 99,99`
- Date: **DD/MM/YYYY** (`15/01/2024`) or `15 de janeiro de 2024` (lowercase months)
- Time: 24-hour (`14h30` or `14:30`, `às 14h30`)
- Numbers: `1.234,56` (period thousands, comma decimal)
- Quotation marks: `«Aspas angulares»` (traditional/formal) or `"..."` (digital)

### N. PT-PT communication style

Formal default, polite, slightly more reserved than Brazil. `Faz favor`, `obrigado/a`. Stricter about anglicisms in formal contexts.

---

## Direct conflict cheat sheet (pt-BR ↔ pt-PT)

Quick reference for the most-common variant divergences:

| Feature | pt-BR | pt-PT |
|---------|-------|-------|
| Ongoing action | `está fazendo` (gerund) | `está a fazer` (a + inf) |
| Pronoun placement | `Me diga` (proclisis) | `Diga-me` (enclitic) |
| Possessive article | `seu arquivo` (no article) | `o seu ficheiro` (with article) |
| Default formality | você (universal) | tu / você / o senhor (3 levels) |
| File | **arquivo** | **ficheiro** |
| Save | **salvar** | **guardar** |
| Delete | **excluir** | **eliminar / apagar** |
| User | **usuário** | **utilizador** |
| Settings | **configurações** | **definições** |
| Phone | **celular** | **telemóvel** |
| Bus | **ônibus** | **autocarro** |
| Train | **trem** | **comboio** |
| Mouse | **mouse** | **rato** |
| Screen | **tela** | **ecrã** |
| Breakfast | **café da manhã** | **pequeno-almoço** |
| Bathroom | **banheiro** | **casa de banho** |
| Upload | **enviar / fazer upload** | **carregar** |
| Download | **baixar / fazer download** | **transferir** |
| Log in | **fazer login / entrar** | **iniciar sessão** |
| Dashboard | **painel** | **painel de controlo** |
| Drop (DnD) | **soltar** | **largar** |
| Currency | **R$ 99,99** (before) | **99,99 €** (after) |
| Status spinner | **Salvando...** | **A guardar...** |
| Anglicism tolerance | more tolerant | stricter |

---

## Self-Check Checklist (run before finalizing)

### Universal accuracy (BOTH variants)
- [ ] Gender correct (o problema, o sistema, a plataforma, a IA, a API, o PDF)
- [ ] Acronym gender from expansion (`a IA`, `nossa IA`, NOT `nosso AI`)
- [ ] English acronyms translated (AI → IA)
- [ ] Article contractions applied (do, da, no, na, à)
- [ ] Articles included in noun phrases with specific nouns (`Erro da aplicação`)
- [ ] Adjective + participle agreement in gender AND number
- [ ] FOR vs PER: `para` (total) vs `por` (rate)
- [ ] All `{variables}` and ICU intact
- [ ] Formality consistent throughout file
- [ ] Domain terminology uses IT meaning (arquitetura de software, pipeline CI/CD, fonte de referência)
- [ ] Sentence case (not Title Case)
- [ ] No comma before `e`/`ou`; comma before `mas/porém/contudo/porque`
- [ ] Date `DD/MM/YYYY`; numbers `1.234,56`

### Universal naturalness
- [ ] Buttons in infinitive
- [ ] Completion participial (NOT `bem-sucedido`)
- [ ] Empty state uses `Não há X / Nenhum(a) X`
- [ ] No `faz sentido` overuse (use `tem sentido / é lógico`)
- [ ] No false friends in wrong sense (`atualmente` ≠ actually, `realizar` ≠ realize, `pretender` ≠ pretend)
- [ ] Compound adjectives natural (`com IA`, `contextual`, `intuitivo`, `na nuvem`)
- [ ] Marketing zero: `Sem X` (NOT `Zero X`)
- [ ] Postnominal adjectives for abstract qualities
- [ ] Software vocab: `desenvolver/criar` for "build"; `implementar` for "deploy"
- [ ] Brand-name articles omitted on platform destinations
- [ ] Block verb mood consistent
- [ ] Prepositional chains simplified (max 2 prepositions)
- [ ] Quantity: `mais de 25` (NOT `25+`)

### pt-BR specific
- [ ] **Você** standard (no `o senhor` in software UI)
- [ ] NO article with possessive (`seu arquivo` NOT `o seu arquivo`)
- [ ] Proclisis (`Me diga` NOT `Diga-me`)
- [ ] Gerund for ongoing (`está fazendo` NOT `está a fazer`)
- [ ] Status spinner: `Salvando...` `Carregando...` `Excluindo...`
- [ ] Brazilian vocab: `arquivo`, `salvar`, `usuário`, `celular`, `excluir`, `configurações`, `ônibus`, `trem`, `mouse`, `tela`
- [ ] Currency `R$ 99,99` (symbol BEFORE)
- [ ] Drop = `soltar` (NOT `largar`)
- [ ] No European terms (`ficheiro/guardar/utilizador/telemóvel/ecrã`)
- [ ] Accents preserved (`você`, `também`, `é importante`)
- [ ] Loanword agreement (`Services tradicionais`, `os plugins atualizados`)
- [ ] No casual gírias in professional UI
- [ ] Subjunctive after doubt/necessity (`É possível que esteja corrompido`)

### pt-PT specific
- [ ] **Article WITH possessive** (`o seu ficheiro` NOT `seu ficheiro`)
- [ ] Enclitic pronouns (`Diga-me` NOT `Me diga`)
- [ ] `a + infinitivo` for ongoing (`está a fazer` NOT `está fazendo`)
- [ ] Status spinner: `A guardar...` `A carregar...` `A eliminar...`
- [ ] European vocab: `ficheiro`, `guardar`, `utilizador`, `telemóvel`, `eliminar/apagar`, `definições`, `autocarro`, `comboio`, `rato`, `ecrã`
- [ ] Currency `99,99 €` (symbol AFTER)
- [ ] Drop = `largar` (NOT `soltar`)
- [ ] AO90 spelling (`projeto`, `ação`, `atual`, `ótimo`, `receção`)
- [ ] Personal infinitive used where natural (`É importante fazermos`)
- [ ] Stricter anglicism rejection (`painel de controlo` not `dashboard`, `iniciar sessão` not `login`)
- [ ] No Brazilian terms (`arquivo/salvar/usuário/celular/excluir`)
- [ ] Instructions in imperative (`Arraste e largue`)
- [ ] Formality consistent (tu vs você vs o senhor — pick one)

---

## Worked Example (same source, both variants)

**Source:** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

### pt-BR (Brazilian, você)

Bem-vindo! Selecione seu arquivo para fazer upload. Suportamos mais de 25 formatos e traduzimos o arquivo para 5 idiomas em {seconds} segundos. Não se preocupe, você pode cancelar a qualquer momento.

(Note: `seu arquivo` no article; `fazer upload` accepted in BR; `suportamos` accepted in tech contexts; `traduzimos` simple present; `para` not `por` for 5 idiomas; `{seconds} segundos` not bare `{seconds}`.)

### pt-PT (European, você)

Bem-vindo! Selecione o seu ficheiro a carregar. Suportamos mais de 25 formatos e traduzimo-lo para 5 idiomas em {seconds} segundos. Não se preocupe, pode cancelar a qualquer momento.

(Note: `o seu ficheiro` WITH article; `carregar` not `fazer upload`; `traduzimo-lo` enclitic pronoun with verb-ending elision; `pode cancelar` formal you; same `para 5 idiomas` and unit-word `segundos`.)

### Common errors both would catch

- `Bem-vindo! Por favor selecione tu arquivo` → mixed formality
- `Sem opções` → should be `Não há opções` (empty state)
- `Pagamento bem-sucedido` → `Pagamento realizado` (BR) / `Pagamento efetuado` (PT)
- `Soportamos 25+ formatos` → `Suportamos mais de 25 formatos`
- `por 5 idiomas` → `para 5 idiomas` (FOR vs PER)
- `{seconds}` without unit → `{seconds} segundos`
- BR-only error: `está a carregar` → should be `está carregando` in pt-BR
- PT-only error: `seu ficheiro` → should be `o seu ficheiro` in pt-PT
