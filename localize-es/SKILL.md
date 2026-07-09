---
name: localize-es
description: Use when translating or localizing UI strings, marketing copy, documentation, or any source text into Spanish (es). Asks the user to choose the regional variant (es-ES Spain, es-419 Latin American neutral, or es-MX Mexico) on first use, then enforces variant-specific formality (vosotros vs ustedes), vocabulary (ordenador vs computadora), tense system (pretérito perfecto vs indefinido), currency, and idiom rules.
---

# Spanish Translation Rules (es / Español)

Distilled from the production translation prompts (`es.ts`, `es-es.ts`, `es-419.ts`, `es-mx.ts`). Follow these rules verbatim — they are model-agnostic and produce consistent native-quality Spanish output.

## Mindset

> Eres un escritor nativo extremadamente exigente que detesta las traducciones literales del inglés y las construcciones poco naturales.

Reject literal English calques. Preserve original meaning while restructuring fully into natural Spanish. Common English terms (API, token, cloud) are acceptable when no native equivalent exists.

## Variant Selection (run FIRST)

Spanish has multiple variants with **directly conflicting rules** (vosotros vs ustedes, ordenador vs computadora, EUR vs USD/MXN, pretérito perfecto vs indefinido, `coger` vulgarity). Applying the wrong variant produces visibly wrong output.

**If the user has not specified the variant**, before translating call `AskUserQuestion` with:

- Question: `Which Spanish variant should I target?`
- Header: `ES variant`
- Options:
  1. **European Spanish (es-ES / Spain)** — vosotros, ordenador/móvil/coche, EUR, pretérito perfecto for recent past, ¡Venga!/Vale.
  2. **Latin American neutral (es-419)** — ustedes only, computadora/celular/auto, pretérito indefinido, no regional slang, avoids `ahorita/orale/che`. Recommended for any pan-LatAm product.
  3. **Mexican (es-MX)** — ustedes, Mexico vocab (`camión` for bus, `chamaco`, `platicar`), MXN ($ with disambiguation), warm tone, diminutives OK, `¡Ándale!/¡Órale!`.

**If the user picks es-ES**, apply the **Universal Spanish base** + **es-ES Deltas** section. Do NOT apply LATAM deltas.

**If the user picks es-419**, apply the **Universal Spanish base** + **es-419 Deltas** section. Do NOT apply Spain or Mexico-specific deltas.

**If the user picks es-MX**, apply the **Universal Spanish base** + **es-419 Deltas** (as foundation) + **es-MX additional deltas** on top.

## Pre-Translation Setup

Lock in before translating:

1. **Variant** — confirmed above.
2. **Formality** — tú (informal) vs usted (formal). Default to usted for B2B/professional UI; tú for consumer apps. NEVER mix within a file.
3. **Two genders** — el (masc), la (fem). Articles, adjectives, participles all agree.
4. **Word order** — SVO; most adjectives FOLLOW the noun.
5. **Opening punctuation marks** — `¿` and `¡` are MANDATORY (universal Spanish, not optional).
6. **Placeholders** — Preserve `{variables}` and ICU plural syntax exactly.

## Register Auto-Detection (run after Variant Selection + Pre-Translation Setup, before translating)

If the user has NOT specified tú or usted, infer from source text register. Match output to source — formal source → usted; informal source → tú. The plural form is ALREADY locked by variant (vosotros = Spain only; ustedes = all other variants).

### Formal source signals → output usted / su / sus
- Hedging / polite modals: "please", "kindly", "we recommend", "could you", "would you mind"
- Passive / impersonal: "users are advised", "it is recommended", "applicants must"
- No contractions: "do not", "cannot", "we will"
- Domain vocabulary: legal, financial, healthcare, regulatory, enterprise B2B, government, insurance
- Third-person / distance: "the user must", "customers should"
- Long sentences, formal connectors
- Brand voice: bank, insurance, government, B2B SaaS, healthcare, legal tech
- No exclamations or emojis

### Informal source signals → output tú / tu / tus
- Contractions: "don't", "you'll", "it's", "we're"
- Casual greetings: "hey", "hi there", "yo", "hi 👋"
- Second-person directness, exclamations, emoji (🎉 😎 🚀 ✨)
- Slang: "cool", "awesome", "no worries", "kinda"
- Consumer-app voice: gaming, social, lifestyle, dating, fitness, kids
- Sentence fragments and conversational filler

### Mixed / ambiguous source → default to usted (formal)
Usted reads slightly distant but professional; tú can read as disrespectful in B2B/government contexts. When in doubt, stay formal.

### Variant interaction
- **es-ES** + informal plural: uses **vosotros**. e.g., `vosotros podéis cambiar vuestras configuraciones`. Buttons stay infinitive — `Guardar` works for both tú and vosotros.
- **es-419 / es-MX** + plural (any formality): uses **ustedes**. e.g., `ustedes pueden cambiar sus configuraciones`. vosotros is forbidden.
- **es-MX informal-tú**: warmer tone allowed (diminutives `cafecito`, expressions `¡Ándale!`), but stay professional in B2B.

### Explicit user override
If the user says "use tú" / "use usted" / "formal" / "casual" / "voseo for Argentina", their instruction wins.

### Worked examples (all using es-419 as the default; substitute per variant)

| Source | Detected | Spanish output |
|----------------|----------|----------------|
| "Please review the terms of service before proceeding." | formal | Por favor, revise los términos del servicio antes de continuar. |
| "Hey! Tap here to get started — it's super quick 🚀" | informal | ¡Hola! Toca aquí para empezar — es súper rápido 🚀 |
| "Submit your application by the deadline." | formal | Envíe su solicitud antes de la fecha límite. |
| "Don't forget to save your work!" | informal | ¡No olvides guardar tu trabajo! |

After detection: keep the chosen form consistent. NEVER mix tú/usted across pronouns, possessives, AND imperatives.

## Universal Spanish Base (apply to ALL variants)

### 1. Gender of common IT nouns (memorize)

| Masculine (el) | Feminine (la) |
|----------------|---------------|
| **el** problema | **la** solución |
| **el** sistema | **la** plataforma |
| **el** programa | **la** aplicación |
| **el** tema | **la** página |
| **el** idioma | **la** conexión |
| **el** mapa | **la** integridad |
| **el** día | **la** red |
| **el** archivo / fichero | **la** pantalla / ecrã |
| **el** software | **la** interfaz |
| **el** servidor | **la** tabla |
| **el** navegador | **la** consulta |
| **el** PDF | **la** API |
| **el** URL | **la** IA |
| **el** OneSky / Slack / Teams (foreign tech) | **la** Apple (company) |

**Patterns:**
- `-ción / -sión / -dad / -tad` → always feminine
- `-ma` (Greek origin) → usually masculine
- **Acronyms inherit gender from expanded form** (CRITICAL): `la IA` (Inteligencia Artificial), `la API` (Interfaz), `el PDF` (Formato).

Common errors: `una problema` → `un problema`; `el plataforma` → `la plataforma`; `la sistema` → `el sistema`; `nuestro IA` → `nuestra IA`.

### 2. Opening punctuation marks (MANDATORY)

| Wrong | Correct |
|-------|---------|
| `Desea continuar?` | **`¿Desea continuar?`** |
| `Error!` | **`¡Error!`** |

The opening `¿` and `¡` are NOT optional and NOT errors to be removed.

### 3. Conjunction y → e (euphonic rule, CRITICAL)

Use `e` instead of `y` before words starting with `i-` or `hi-` sound. Use `y` everywhere else.

| Wrong | Correct |
|-------|---------|
| `padre y hijo` | `padre **e** hijo` |
| `Francia y Italia` | `Francia **e** Italia` |
| `gestión y integración` | `gestión **e** integración` |
| `e almacenamiento` | `**y** almacenamiento` (starts with `a`) |
| `e API` | `**y** API` (starts with /a/ sound) |

Same rule for `o → u` before `o-` or `ho-` sound: `siete u ocho`, not `siete o ocho`.

### 4. Article contractions (mandatory)

| Combine | → |
|---------|---|
| a + el | **al** |
| de + el | **del** |

`ir a el sistema` → `ir al sistema`. `cerca de el servidor` → `cerca del servidor`.

### 5. Article completeness in noun phrases (CRITICAL)

Specific known nouns require definite articles in prepositional phrases. Exception: generic classifiers (`error de sistema` = type, vs `error del sistema` = specific).

| Wrong | Correct |
|-------|---------|
| Error de aplicación | **Error de la aplicación** |
| Configuración de cuenta | **Configuración de la cuenta** |
| Estado de conexión | **Estado de la conexión** |
| Detalles de transacción | **Detalles de la transacción** |
| variable de entorno falta | **la variable de entorno falta** / `falta la variable de entorno` |

### 6. FOR vs PER — never confuse (CRITICAL)

| English | Wrong | Correct |
|---------|-------|---------|
| for 5 languages (total) | por idioma | **para 5 idiomas** |
| per language (rate) | para idioma | **por idioma** |

### 7. Loanword adjective agreement (CRITICAL)

English loanwords in Spanish text: adjectives still agree in gender + number (foreign nouns default to perceived gender or masculine).

| Wrong | Correct |
|-------|---------|
| Services tradicional | **Services tradicionales** |
| los plugins actualizado | **los plugins actualizados** |
| las features nuevo | **las features nuevas** |
| el dashboard actualizada | **el dashboard actualizado** |

### 8. UI button labels — infinitive form (industry standard)

| Wrong (imperative) | Correct (infinitive) |
|--------------------|----------------------|
| Guarda / Guarde | **Guardar** |
| Cancela / Cancele | **Cancelar** |
| Elimina / Elimine | **Eliminar** |
| Regístrate / Regístrese | **Registrarse** |

Avoids tú/usted complexity in buttons.

### 9. Status messages — gerund

| Wrong | Correct |
|-------|---------|
| Guardar... | **Guardando...** |
| Cargar... | **Cargando...** |
| Procesar... | **Procesando...** |

### 10. Completion messages — participial / verbal (NOT "exitoso")

| Wrong (calque) | Correct |
|----------------|---------|
| Pago exitoso | **Pago realizado / Pago completado / ¡Listo!** |
| Carga exitosa | **Carga completada / Archivo subido / ¡Hecho!** |
| Descarga completa | **Descarga completada / Descarga finalizada** |
| Operación exitosa | **Operación completada / ¡Listo!** |

`exitoso` is severity 1.5 in Spain (sounds clearly imported), 0.5 in LATAM (more tolerated) — but participial forms are universally better.

### 11. Empty state — `No hay X` (existential)

| Wrong | Correct |
|-------|---------|
| No se han seleccionado idiomas | **No hay idiomas seleccionados** |
| No se han encontrado resultados | **No hay resultados** |
| Sin datos disponibles | **No hay datos disponibles** |
| Sin conexión | **No hay conexión** |
| No se ha seleccionado ningún archivo | **No hay archivos seleccionados** (avoid double negative) |

### 12. Drag and drop

| English | Spanish |
|---------|---------|
| drag | arrastrar |
| drop / release (let go) | **soltar** — NOT `permitir` |
| browse (file picker) | **Seleccionar archivo / Elegir archivo** — NOT `Explorar` |
| Standard phrase | `Arrastrar y soltar` |

### 13. Calques to avoid (universal)

| Wrong (literal) | Natural Spanish |
|-----------------|------------------|
| `hace sentido` / `hacer sentido` | **`tiene sentido`** |
| `aplicar para` (a job) | `solicitar / postularse / presentar solicitud` |
| `Estar siendo + participio` (overused) | active voice or simple passive |
| `tomar ventaja de` | `aprovechar / sacar provecho de` |
| `en una base diaria/semanal` | `a diario / cada semana / diariamente` |
| `en términos de` | `en cuanto a / respecto a` |
| `desde la API / desde el servidor` (abstract source) | `de la API / del servidor` (de = origin/belonging; desde = physical movement) |

### 14. False friends (universal)

| Wrong (English meaning) | Actual Spanish meaning | Correct Spanish |
|--------------------------|------------------------|------------------|
| `actualmente` (for "actually") | currently | **en realidad** |
| `eventualmente` (for "eventually") | possibly | **finalmente** |
| `realizar` (for "to realize") | to carry out | **darse cuenta** |
| `soportar` (for "to support") | to tolerate | **dar soporte / apoyar** (tech "support" = `admitir / ser compatible con`) |
| `remover` (for "to remove") | to stir | **eliminar / quitar** |

### 15. Marketing "Zero X" → "Sin X"

| Wrong | Correct |
|-------|---------|
| Cero tiempo de inactividad / Cero downtime | **Sin tiempo de inactividad / Sin interrupciones** |
| Cero errores | **Sin errores / Libre de errores** |
| Cero mantenimiento | **Sin mantenimiento / No requiere mantenimiento** |
| Cero compromiso | **Sin compromiso** |

### 16. Adjective order — postnominal for abstract qualities

| Wrong | Correct |
|-------|---------|
| con perfecta coherencia | **con una coherencia perfecta / de manera perfectamente coherente** |
| con completa confianza | **con total confianza / con confianza total** |
| con absoluta precisión | **con una precisión absoluta** |
| de superior calidad | **de calidad superior** |
| calidad humana (tech) | **calidad a nivel humano / calidad profesional** |

### 17. Compound adjectives — natural construction

| English pattern | Wrong | Correct |
|-----------------|-------|---------|
| AI-powered / X-powered | `IA-potenciado`, `impulsado por IA`, `traducción de IA` | **`con IA / con tecnología de IA / potenciado con IA / traducción con IA`** |
| context-aware / X-aware | `contexto-consciente` | **`contextual / sensible al contexto`** |
| user-friendly | `usuario-amigable` | **`intuitivo / fácil de usar`** |
| cloud-based | `nube-basado / basado en nube` | **`en la nube / basado en la nube`** |
| supported formats | `formatos soportados` | **`formatos compatibles / formatos admitidos`** |

### 18. Business terminology — adjective forms

| Wrong (prepositional) | Correct (adjective) |
|-----------------------|---------------------|
| traducción para empresas | **traducción empresarial** |
| solución para empresas | **solución empresarial** |
| cliente para empresas | **cliente empresarial** |
| traducción para negocios | **traducción comercial / traducción empresarial** |

### 19. Software terminology — IT meaning

| English | Wrong | Correct |
|---------|-------|---------|
| build (software) | construcción | **desarrollar / crear / implementar** |
| deploy | despliegue (military) | **implementar / poner en producción / lanzar** |
| support (feature) | soportar | **admitir / ser compatible con / incluir soporte para** |
| sync seamlessly | sincronizar fácilmente | **sincronizar automáticamente / mantener sincronizado** |
| listings (app store) | listados | **fichas de la aplicación / fichas de app** |
| architecture (software) | arquitectura (construcción) | **arquitectura de software** |
| pipeline (CI/CD) | tubería | **pipeline (CI/CD)** |
| source of truth | fuente de la verdad | **fuente de referencia / fuente autoritativa** |

### 20. Structural calques — verb-first / impersonal SE

| Wrong (English subject-first passive) | Correct (Spanish verb-first / SE) |
|---------------------------------------|------------------------------------|
| [Subject] es necesario/requerido para [Purpose] | **Se requiere [Subject] para [Purpose]** |
| [Subject] es obligatorio | **Se requiere [Subject] / Es obligatorio [Subject]** |

### 21. Prepositional-chain simplification (max 2 prepositions)

- Wrong: `productos de cuidado de la piel de noche`
- Correct: **`productos de cuidado nocturno / cuidado nocturno de la piel`**

Use adjective forms or merge concepts.

### 22. Compound descriptive nouns

| English | Wrong | Correct |
|---------|-------|---------|
| mom creators | creadoras madres | **creadoras que son madres / mamás creadoras de contenido** |
| niche creators | (literal) | **creadores de nicho / creadores especializados** |

### 23. UI element reference in prose

| Wrong | Correct |
|-------|---------|
| el campo de nombre | **el campo «Nombre»** or `el campo Nombre` |
| la pestaña de las cuentas | **la pestaña «Cuentas»** |
| la barra de búsqueda | (generic — no quotes needed) |

### 24. Spatial metaphor prepositions

| English (figurative) | Use | Don't use |
|---------------------|-----|-----------|
| under [category] (browsing) | **entre / en** | debajo de |
| on top of (in addition to) | **además de** | encima de |
| behind the scenes | **entre bastidores / detrás de escena** | (literal) |
| within [timeframe] | **en / dentro de** | (literal) |

### 25. Brand names — no article for platform destinations

| Wrong | Correct |
|-------|---------|
| sincronizar con la Apple App Store | **sincronizar con Apple App Store** |
| en la App Store | **en Apple App Store / en App Store** |
| publicar en el Google Play | **publicar en Google Play** |

When brand IS the subject: `Apple ha anunciado...` (no article preferred) or `La empresa Apple...` (with article when modified).

### 26. Block verb mood consistency

Child items must match the verb mood frame set by the parent title/heading.

| Title frame | Wrong child | Correct child |
|-------------|-------------|---------------|
| `Lo que obtendrías:` (conditional) | `Recibe una propuesta...` (imperative) | `Recibirías una propuesta...` or `Propuesta al siguiente día hábil...` (noun phrase) |
| `Pasos a seguir:` (instructional) | `Configurarías tu cuenta...` (conditional) | `Configura tu cuenta...` (imperative) or `Configurar tu cuenta...` (infinitive) |

### 27. Subjunctive after doubt / desire / necessity

| Wrong | Correct |
|-------|---------|
| Es posible que el archivo es corrupto | **Es posible que el archivo esté corrupto** |
| Necesitamos que usted puede acceder | **Necesitamos que usted pueda acceder** |

### 28. Temporal expression — "[YEAR] me" idiom

| English | Wrong | Correct |
|---------|-------|---------|
| 2014 me | hace 2014 años | **yo en 2014 / mi yo de 2014** |
| 90s me | hace 90s años | **yo en los 90 / mi yo de los 90** |
| teenage me | (literal) | **yo de adolescente / mi yo adolescente** |

### 29. Validation messages — match verb form to message type

| Type | Verb mood | Example |
|------|-----------|---------|
| Field validation | indicative | `Este campo es obligatorio` |
| Action instruction | imperative | `Introduce un valor válido` |
| State description | impersonal | `No se ha podido conectar` |

### 30. Cost / estimate expression ordering

- Amount-first with `para` (PREFERRED): `99,99 € para 5 idiomas`
- Per-unit: `1.500 palabras por idioma`, `por palabra`, `al mes`
- Total: `Coste total: 499,99 €`

---

## es-ES (Spain) Deltas

Apply ONLY when the user picked Spain.

### A. Vosotros for informal plural (CRITICAL, severity 2.0)

| Context | Use |
|---------|-----|
| Informal plural pronoun | **`vosotros / vosotras`** |
| "You all have" | `Vosotros tenéis` |
| "I tell you (pl)" | `Os digo` |
| Possessive (pl) | `vuestro / vuestra` |
| Imperative (pl) | `Hablad`, `Decidme` |

Wrong: `Ustedes tenéis` → Correct: `Vosotros tenéis`. (Exception: Canary Islands use ustedes for informal plural — usually NOT relevant for software UI.)

### B. Peninsular vocabulary (severity 1.5)

| Concept | Spain (USE) | Avoid (LATAM term) |
|---------|-------------|---------------------|
| computer | **ordenador** | computadora |
| mobile / phone | **móvil** | celular |
| car | **coche** | carro, auto |
| to drive | **conducir** | manejar |
| apartment | **piso** | departamento, apartamento |
| bus | **autobús** | camión (MX), colectivo (AR) |
| OK / confirmation | **vale** | ok / está bien |
| to chat | **hablar / charlar** | platicar |

### C. Pretérito perfecto compuesto for recent past

Spain uses pretérito perfecto for same-day/recent events. (LATAM uses pretérito indefinido.)

| Wrong (LATAM style) | Correct (Spain) |
|---------------------|------------------|
| Hoy comí | **Hoy he comido** |
| Esta semana fui | **Esta semana he ido** |
| Llegué hace un momento | **He llegado hace un momento** |

### D. "A por" construction (Spain-specific)

- `voy por el pan` → **`voy a por el pan`**

### E. Costes vs costos

Spain uses `costes`; LATAM uses `costos`. `Cero costos ocultos` → **`Sin costes ocultos / Sin cargos ocultos`** in Spain.

### F. Spain typography / cultural notes

- Currency: **EUR (€)**, format `99,99 €` or `€ 99,99`
- Decimal: **`,`** (comma); Thousands: **`.`** (period); example: `1.234,56 €`
- Date: **DD/MM/YYYY** (`15/01/2024`) or `15 de enero de 2024`
- Time: 24-hour (`14:30`) or 12-hour (`2:30 p.m.`)
- Quotation marks: `«...»` (traditional) or `"..."` (digital)

### G. Spain interjections (characteristic but optional)

`¡Venga!`, `¡Anda!`, `¡Hombre!`, `Vale` for confirmation. Use sparingly in software UI; they signal Spain authenticity.

### H. Spain status-message tolerance is LOWER

`exitoso` reads as a clear anglicism in Spain (severity 1.5 vs 0.5 in LATAM). Always prefer participial: `Pago realizado` not `Pago exitoso`.

### I. Spain-specific calque additions

- `Comenzar con la traducción` → **`Comenzar a traducir`** ("Get started with X" → `a + infinitive`)
- `para revisión / descarga / edición` → **`para revisar / descargar / editar`** (prefer infinitive after `para` in UI actions)

---

## es-419 (Latin American — neutral) Deltas

Apply when the user picked Latin American (use as foundation for es-MX too).

### A. Ustedes for ALL plural (CRITICAL, severity 2.0)

NEVER use vosotros. `ustedes` covers both formal and informal plural in all of Latin America.

| Wrong (Spain style) | Correct (LATAM) |
|---------------------|------------------|
| Vosotros tenéis | **Ustedes tienen** |
| os digo | **les digo** |
| vuestro / vuestra | **su / sus** |
| Hablad, Decidme | **Hablen, Díganme** |

### B. CRITICAL — `coger` is vulgar in Latin America (severity 3.0 — highest)

NEVER use `coger`. Always replace with `tomar` or `agarrar`.

| Wrong | Correct |
|-------|---------|
| Coger el autobús | **Tomar el autobús** |
| Coge esto | **Toma esto / Agarra esto** |
| Coger una cita | **Tomar / Sacar una cita** |
| Coger una llamada | **Recibir / Atender una llamada** |

This is the single highest-severity rule in the LATAM prompts.

### C. Pan-LatAm neutral vocabulary

Use terms understood across MX, AR, CO, CL, PE. Avoid single-country regionalisms.

| Concept | Neutral LATAM (USE) | Avoid (Spain) | Avoid (regional) |
|---------|---------------------|---------------|------------------|
| computer | **computadora** | ordenador | — |
| mobile / phone | **celular** | móvil | — |
| car | **carro / auto** | coche | — |
| to drive | **manejar** | conducir | — |
| bus | **autobús** | — | camión (MX), colectivo (AR) |
| grab / take | **tomar / agarrar** | (coger — vulgar!) | — |
| apartment | **departamento / apartamento** | piso | — |
| OK / Alright | **de acuerdo / está bien** | vale | órale (MX), dale (AR), bacano/chévere (CO) |
| right now | **ahora / en este momento** | — | ahorita (MX diminutive) |

### D. Pretérito indefinido for recent past (CRITICAL — applies to passive + reflexive SE too)

LATAM uses simple past for recently completed events. This applies to ALL constructions: active, passive, reflexive SE, impersonal SE.

| Wrong (Spain perfecto) | Correct (LATAM indefinido) |
|------------------------|-----------------------------|
| Hoy he comido | **Hoy comí** |
| El usuario ha iniciado sesión | **El usuario inició sesión** |
| Ha sido eliminado (passive) | **Fue eliminado** |
| Ha sido actualizado | **Fue actualizado** |
| Se ha eliminado de la lista (reflexive) | **Se eliminó de la lista** |
| Se ha guardado correctamente | **Se guardó correctamente** |
| Se ha enviado el mensaje | **Se envió el mensaje** |
| Se ha completado la operación | **Se completó la operación** |
| Se han procesado los datos | **Se procesaron los datos** |

The reflexive-SE and impersonal-SE cases are the most commonly missed.

### E. NO regional slang in LATAM-neutral

Avoid single-country expressions when targeting pan-LatAm:

| Country | Avoid |
|---------|-------|
| Mexico | `órale`, `ándale`, `ahorita`, `chamaco`, `chido` |
| Argentina | `che`, `boludo`, `laburo`, `pibe` |
| Colombia | `bacano`, `chévere`, `parce` |
| Chile | `cachái`, `po`, `fome` |
| Venezuela | `chamo`, `pana`, `arrecho` |

Use neutral alternatives. AVOID diminutives like `ahorita`, `ratito`, `momentito` — use `ahora`, `momento`.

### F. LATAM currency / number / date format

- Decimal separator: **`.`** (period) — `1,234.56`
- Thousands separator: **`,`** (comma)
- Currency varies by country — use generic format or specify ISO code (USD, MXN, ARS, COP, CLP, PEN)
- Date: **DD/MM/YYYY** standard across LatAm
- Time: 12-hour with a.m./p.m. common, 24-hour acceptable

### G. LATAM-specific calque differences

- `En base a` → **`Con base en / Basándose en`** (LATAM allows `con base en`; Spain rejects it)
- `Aplicar para` (job) → **`Solicitar / Postularse`** (preferred in LATAM; `Presentar solicitud` more Spain)
- `Comenzar con la traducción` → **`Comenzar a traducir`**
- `para revisión / descarga / edición` → **`para revisar / descargar / editar`**
- `contactar al soporte / contactar a soporte` → **`contactar con soporte / contactar con el equipo de soporte`** (always with `con`)
- `comunicarse a soporte` → **`comunicarse con soporte`**

### H. LATAM file picker & error patterns

- `Explorar archivos / Buscar archivos` → **`Seleccionar archivo / Elegir archivo`** (action verb, not navigation)
- `Archivo no encontrado.` → **`Archivo no encontrado. Verifique la ruta.`** (include next steps)

### I. LATAM communication style

Professional, clear, courteous, direct but respectful. Default to **usted** for business contexts; `tú` acceptable for consumer/casual.

---

## es-MX (Mexican) Additional Deltas

Apply ON TOP of the es-419 deltas (don't replace them — the `coger` rule, ustedes, and pretérito indefinido all still apply).

### A. Mexico-specific vocabulary

| Concept | Mexico (USE) | es-419 neutral |
|---------|--------------|-----------------|
| **bus** (city) | **`camión`** | autobús (more formal) |
| car | `carro` | carro / auto |
| computer | `computadora` | computadora |
| phone | `celular` | celular |
| to drive | `manejar` | manejar |
| to chat | `platicar` | (avoided in es-419) |
| kid / young | `chamaco/a` (regional) | (avoided in es-419) |
| OK / Alright | `ok / está bien / sale` | de acuerdo / está bien |
| download | `descargar / bajar` | descargar |

Note: Mexico's `camión` for bus is the OPPOSITE of es-419's `autobús` — only use in Mexico-specific content. For pan-LatAm, stay with `autobús`.

### B. Mexican currency

- Currency: **MXN** — `$99.99 MXN` or `MX$99.99` (disambiguate because `$` is ambiguous with USD)
- Example: `99,99 €` → `$99.99 MXN`

### C. Mexican warmth — diminutives + interjections allowed (with restraint)

Mexico's tone is warm, relationship-focused, respectful. Diminutives are characteristic but should be USED WITH RESTRAINT in software UI.

**OK in casual/marketing contexts:**
- Diminutives: `cafecito`, `ratito`, `momentito`, `tantito`, `ahorita`
- `¿Mande?` instead of `¿Qué?` (more polite)
- `¡Ándale!` (encouragement), `¡Sale!` (OK), `¡Órale!` (OK / surprise)
- `¡Échale ganas!` (encouragement, like "Break a leg")
- `¡Qué padre! / ¡Está chido!` ("That's cool")

**AVOID in professional/enterprise software UI:**
- Overuse of `ahorita` (use `ahora`)
- `chamaco` (too regional)
- `chido / padrísimo` (too casual for B2B)
- The MX prompt says: "Warm AND professional are NOT mutually exclusive — but don't OVERUSE diminutives."

### D. Mexican date format flexibility

Both **DD/MM/YYYY** and **MM/DD/YYYY** are tolerated in Mexico due to US proximity. Default to DD/MM/YYYY in software.

### E. Mexican brand-name rules

- MASCULINE default for foreign tech brands: `el OneSky, el Slack, el Teams`
- `el App Store ofrece...` when store is grammatical subject

### F. Mexican-specific cultural notes

- Frequent `por favor`, `disculpe`, `con permiso` — politeness is highly valued
- Personal approach even in business contexts
- `¡Que te vaya bien!` for casual goodbye / well-wishes

---

## Voseo (Argentina / Uruguay / Central America) — Out of Scope Note

- Voseo is the use of `vos` instead of `tú` as the 2nd-person informal singular pronoun.
- Geography: standard in Argentina, Uruguay, Paraguay; common in Costa Rica, Nicaragua, parts of Honduras, El Salvador, Guatemala, Bolivia, Chile (some regions).
- Argentine voseo conjugation: `vos sos` (vs `tú eres`), `vos tenés` (vs `tú tienes`), `vos podés` (vs `tú puedes`), `vos querés` (vs `tú quieres`), `vení` (vs `ven`), `tomá` (vs `toma`), `decí` (vs `di`).
- **This skill does NOT have full voseo rules.** The es-419 prompt explicitly avoids voseo for pan-LatAm neutrality. If the user wants Argentine-targeted content with voseo, treat as out-of-scope and ASK the user to confirm; provide best-effort with the known conjugation pairs above.
- For Argentina-targeted commercial software, the production approach is to use es-419 with `tú` (or `usted` formal), NOT voseo, even though it sounds slightly non-native.

---

## Diminutives (-ito / -ita) Register Impact

- Diminutives carry warmth and informality, NOT just literal smallness.
- Common in Mexican Spanish: `cafecito` (coffee, warm), `ratito` (a moment), `momentito` (just a sec), `tantito` (a bit), `ahorita` (right now).
- Acceptable in Mexican consumer UI when matching warm tone (`Espera tantito mientras procesamos...`).
- AVOID diminutives in:
  - es-419 neutral content — too regional (Mexican-flavored).
  - es-ES formal/B2B — sounds infantilizing.
  - Any government/banking/legal context — undermines authority.
- For Spain, diminutives `-ito/-ita` exist but are less frequent in UI. The Spanish-language equivalent of warmth tends to use `por favor`, `gracias`, exclamations.

---

## Gerundio (-ndo) and English Progressive Overuse

- Spanish gerundio (`-ando, -iendo`) describes simultaneous action: `Estoy guardando` = "I am saving (right now)".
- English overuses progressive forms; Spanish often prefers simple present.
- Wrong: `Estoy queriendo aprender` (calque of "I am wanting to learn") → Correct: `Quiero aprender`.
- Wrong: `Te estoy escribiendo para...` (calque of "I am writing to...") → Correct: `Te escribo para...` (simple present is more natural).
- Wrong: `Necesitando ayuda?` → Correct: `¿Necesitas ayuda?`.
- ICU/status patterns use gerundio correctly: `Cargando...`, `Guardando...`, `Procesando...`.
- Wrong: `Has estado iniciando sesión.` → Correct: `Has iniciado sesión.` (English "have been -ing" usually maps to Spanish perfect, not perfect progressive).

---

## Timing Adverbs (ya / aún / todavía)

- `ya` = "already" / "now" / depending on context "right away": `Ya está listo` (it's ready), `Ya voy` (I'm on my way), `¿Ya guardaste?` (have you saved yet?).
- `aún` and `todavía` both mean "still" / "yet" — largely interchangeable. `Aún no he terminado` = `Todavía no he terminado`. `Aún` slightly more formal/literary.
- Common UI: `Aún no hay resultados.` / `Todavía no hay resultados.` (no results yet) — both natural.
- Wrong: `Aún ya guardaste?` (contradictory).
- `ya no` = "no longer" / "not anymore": `Ya no está disponible.`

---

## Greetings and Email Closings

- Greetings: `Buenos días` (morning), `Buenas tardes` (afternoon), `Buenas noches` (evening/night), `Hola` (any time, neutral), `¿Qué tal?` (informal "how's it going?"), `¡Hola!` (warm UI welcome).
- Mexican-only warm: `¿Qué onda?` / `¿Cómo estás?` (consumer apps).
- Spain-only: `¡Hola!` and `Buenas` (very casual).
- Email salutations formal: `Estimado/a Sr./Sra. [Apellido]:` (with colon, Spanish convention), `Apreciado/a:`.
- Email salutations informal: `Hola, [Nombre]:` `Hola [Nombre]:` (most common).
- Email closings formal: `Atentamente,` (standard), `Cordialmente,` (warmer), `Saludos cordiales,` (warm/professional), `Quedo a su disposición,` (very formal).
- Email closings informal: `Saludos,` `Un saludo,` `Un abrazo,` (warmer), `Hasta pronto,`.

---

## Self-Check Checklist (run before finalizing)

### Universal accuracy (ALL variants)
- [ ] Gender correct (problema=masc, sistema=masc, plataforma=fem, IA=fem, API=fem, PDF=masc)
- [ ] Opening `¿` and `¡` present on all questions and exclamations
- [ ] Conjunction `y → e` before i-/hi- (padre e hijo, gestión e integración)
- [ ] Article contractions applied (al, del)
- [ ] Articles included in noun phrases with specific nouns (`Error de la aplicación`)
- [ ] Adjective + participle agreement in gender AND number
- [ ] Loanword adjective agreement (`Services tradicionales`, `los plugins actualizados`)
- [ ] FOR vs PER: `para` (total) vs `por` (rate)
- [ ] Subjunctive after doubt / necessity / desire
- [ ] All `{variables}` and ICU intact
- [ ] Formality consistent (tú or usted) throughout file
- [ ] Domain terminology uses IT meaning (arquitectura de software, pipeline CI/CD, fuente de referencia)

### Universal naturalness
- [ ] Buttons in infinitive (Guardar, Cancelar, Eliminar)
- [ ] Status messages in gerund (Guardando, Cargando)
- [ ] Completion participial (Pago realizado NOT Pago exitoso)
- [ ] Empty state uses `No hay X`
- [ ] Drag-drop: `arrastrar / soltar` (NOT permitir)
- [ ] No `hacer sentido` calque (use `tener sentido`)
- [ ] No false friends in wrong sense (`actualmente` ≠ actually, `realizar` ≠ realize)
- [ ] Compound adjectives natural (`con IA`, `contextual`, `intuitivo`, `en la nube`)
- [ ] Business terms in adjective form (`traducción empresarial`)
- [ ] Marketing zero: `Sin X` (NOT `Cero X`)
- [ ] Postnominal adjectives for abstract qualities (`con una coherencia perfecta`)
- [ ] Software vocab: `desarrollar/crear` for "build", `implementar` for "deploy", `admitir / ser compatible con` for "support"
- [ ] Brand-name articles omitted on platform destinations
- [ ] UI labels in prose use «...» or capitalization
- [ ] Block verb mood consistent
- [ ] Compound nouns restructured (`creadoras que son madres` NOT `creadoras madres`)
- [ ] Spatial metaphors adapted (`entre / además de / entre bastidores`)
- [ ] Validation: field=indicative, action=imperative, state=impersonal

### Spain (es-ES) specific
- [ ] `vosotros` for informal plural (NOT `ustedes`)
- [ ] Peninsular vocab (`ordenador`, `móvil`, `coche`, `vale`, `piso`, `autobús`)
- [ ] Pretérito perfecto for recent past (`Hoy he comido`)
- [ ] `a por` for "to fetch" (`voy a por el pan`)
- [ ] `costes` (not `costos`)
- [ ] Currency `99,99 €`; date `15/01/2024`; numbers `1.234,56`

### Latin America (es-419) specific
- [ ] `ustedes` for plural (NEVER `vosotros`)
- [ ] **NO `coger`** (use `tomar / agarrar`) — highest severity
- [ ] Pretérito indefinido for recent past (`comí` NOT `he comido`)
- [ ] Indefinido applies to passive + reflexive SE (`Se guardó` NOT `Se ha guardado`)
- [ ] Neutral vocab (`computadora`, `celular`, `carro/auto`, `manejar`, `autobús`)
- [ ] No regional slang (`ahorita`, `che`, `bacano`, `cachái`, etc.)
- [ ] No diminutives in professional UI
- [ ] Numbers `1,234.56`; date `15/01/2024`
- [ ] File picker uses action verbs (`Seleccionar archivo`)
- [ ] Error messages include next steps (`Verifique la ruta`)

### Mexico (es-MX) specific
- [ ] Mexico vocab (`camión` for city bus, `platicar`, `descargar/bajar`, `sale`)
- [ ] Currency `$99.99 MXN` (disambiguate from USD)
- [ ] Warmth markers acceptable (`por favor`, `disculpe`, `¿Mande?`)
- [ ] Diminutives used sparingly (`ahorita`, `cafecito` only in casual contexts)
- [ ] No `coger`; ustedes only; pretérito indefinido (all es-419 rules still apply)

---

## Worked Example (same source, three variants)

**Source:** "Welcome! Please select your file to upload — we support 25+ formats and translate it for 5 languages in {seconds}s. Don't worry, you can cancel at any time."

### es-ES (Spain, usted)

¡Bienvenido! Seleccione su archivo para subirlo. Admitimos más de 25 formatos y lo traducimos a 5 idiomas en {seconds} segundos. No se preocupe, puede cancelarlo en cualquier momento.

(Or with `vosotros` if plural informal context: `¡Bienvenidos! Seleccionad vuestro archivo...`)

### es-419 (Latin American, usted)

¡Bienvenido! Seleccione su archivo para subirlo. Admitimos más de 25 formatos y lo traducimos a 5 idiomas en {seconds} segundos. No se preocupe, puede cancelar en cualquier momento.

(Differences from Spain: no `vosotros` is even possible; "computadora/celular" don't apply here but would if the source had them; pretérito indefinido would matter if source had "we have launched" → `lanzamos` not `hemos lanzado`.)

### es-MX (Mexican, tú warm)

¡Bienvenido! Selecciona tu archivo para subirlo. Soportamos más de 25 formatos y lo traducimos a 5 idiomas en {seconds} segundos. No te preocupes, puedes cancelarlo en cualquier momento.

(Note: `tú` chosen for the warmer Mexican consumer-app register; `subirlo` works for upload; no diminutives forced; if the source mentioned a price, it would be `$99.99 MXN`.)

### Common errors all three would catch

- `Por favor seleccione tu archivo` → mixed formality (use `su` with usted or `tu` with tú throughout)
- `Sin las opciones` → should be `No hay opciones` for empty state
- `Pago exitoso` → `Pago realizado` (universally preferred, severity higher in Spain)
- `Soportamos 25+ formatos` → `Admitimos más de 25 formatos`
- `por 5 idiomas` → `para 5 idiomas` (FOR vs PER)
- `{seconds}` without unit → `{seconds} segundos`
