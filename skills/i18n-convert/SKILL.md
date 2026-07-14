---
name: i18n-convert
description: "|"
---

# i18n-convert: localization file format converter

Cross-platform CLI (Rust) that converts between 32 localization file formats
with data-loss warnings when the target format can't represent something.

## Setup check

```bash
command -v i18n-convert || npm install -g @i18n-agent/i18n-convert
```

## Usage

```bash
i18n-convert <input-file> --to <format> [-o <output-file>]
```

| Flag | Meaning |
|------|---------|
| `--to <format>` | Target format (required) |
| `-o <file>` | Output file (default: stdout) |
| `--force` | Skip data-loss confirmation |
| `--dry-run` | Show warnings without writing |
| `--verbose` | Show conversion details |
| `--list-formats` | List all supported format slugs |

Input format is auto-detected from the file. Run `i18n-convert --list-formats`
to get the exact `--to` slugs — do not guess them.

## Examples

```bash
i18n-convert en.json --to android-xml -o strings.xml   # JSON → Android
i18n-convert Localizable.strings --to po -o messages.po # iOS → Gettext
i18n-convert translations.xliff --to yaml-rails -o en.yml
i18n-convert messages.po --to json                       # to stdout
```

## Agent guidance

- Always `--dry-run` first when converting to a less expressive format
  (e.g. plural-aware → CSV) and surface the warnings to the user.
- Batch conversions: loop over files in Bash; the CLI takes one input at a time.
- Round-trip check after risky conversions: convert back and diff key sets
  (or run `i18n-validate` on the result).
