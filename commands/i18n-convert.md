---
description: "Convert localization files between 32 formats safely: dry-run first, surface data-loss warnings, verify the result"
argument-hint: "<input-file(s)> --to <format> [-o output]"
allowed-tools: [Bash, Read, Glob, Grep]
---

# i18n-convert: $ARGUMENTS

Convert the given localization file(s) using the `i18n-convert` CLI.

## Step 1 — Setup check

```bash
command -v i18n-convert || npm install -g @i18n-agent/i18n-convert
```

## Step 2 — Resolve the target format slug

Never guess slugs. If the requested format isn't an exact slug, run:

```bash
i18n-convert --list-formats
```

and pick the matching slug (e.g. "Android" → `android-xml`, "Rails YAML" →
`yaml-rails`).

## Step 3 — Dry-run for data loss

```bash
i18n-convert <input> --to <slug> --dry-run
```

If it warns about data loss (plurals flattened, metadata dropped, comments
lost), STOP and show the warnings to the user before writing anything. Only
proceed with `--force` after they confirm (or if they already said to force).

## Step 4 — Convert

```bash
i18n-convert <input> --to <slug> -o <output>
```

If no output path was given, derive it from the input name and the target
format's conventional extension, in the same directory.
Multiple inputs: loop in Bash, one invocation per file.

## Step 5 — Verify

- Read the output file and confirm it parses / looks structurally sane.
- Key-count check: convert the output back to `json` on stdout and compare the
  key count with the input converted to `json`. A mismatch not explained by
  the dry-run warnings is a failure — report it, don't hide it.

Report: files converted, format, any data-loss warnings, verification result.
