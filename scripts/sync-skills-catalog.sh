#!/usr/bin/env bash
# Build skills/ catalog for skills.sh / npx skills add discovery.
set -euo pipefail

STACK_DIR="$(cd "$(dirname "$0")/.." && pwd)"
CATALOG="$STACK_DIR/skills"
SKIP_DIRS=(commands scripts skills .git)
WORKFLOW_CMDS=(i18n-convert i18n-pseudo i18n-validate)
UNIQUE_CMDS=(i18n-wrap i18n-review)

should_skip() {
  local name="$1"
  for skip in "${SKIP_DIRS[@]}"; do
    [[ "$name" == "$skip" ]] && return 0
  done
  return 1
}

rm -rf "$CATALOG"
mkdir -p "$CATALOG"

python3 - "$STACK_DIR" "$CATALOG" <<'PY'
import json
import re
import sys
from pathlib import Path

stack_dir = Path(sys.argv[1])
catalog = Path(sys.argv[2])
skip_dirs = {"commands", "scripts", "skills", ".git"}
workflow_cmds = ["i18n-convert", "i18n-pseudo", "i18n-validate"]
unique_cmds = ["i18n-wrap", "i18n-review"]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        if key in {"name", "description", "argument-hint"}:
            meta[key] = value
    return meta, text[match.end() :]


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def write_skill_md(target: Path, name: str, description: str, body: str) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    front = f"---\nname: {name}\ndescription: {yaml_quote(description)}\n---\n\n"
    target.write_text(front + body.lstrip("\n"), encoding="utf-8")


def catalog_from_source(source: Path, skill_name: str) -> None:
    text = source.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    name = meta.get("name") or skill_name
    description = meta.get("description") or f"i18nstack skill: {skill_name}"
    write_skill_md(catalog / skill_name / "SKILL.md", name, description, body)


count = 0

for skill_dir in sorted(stack_dir.iterdir()):
    if not skill_dir.is_dir() or skill_dir.name in skip_dirs:
        continue
    source = skill_dir / "SKILL.md"
    if not source.is_file():
        continue
    catalog_from_source(source, skill_dir.name)
    count += 1

for cmd in unique_cmds:
    source = stack_dir / "commands" / f"{cmd}.md"
    if source.is_file():
        catalog_from_source(source, cmd)
        count += 1

for cmd in workflow_cmds:
    source = stack_dir / "commands" / f"{cmd}.md"
    if not source.is_file():
        continue
    skill_name = f"{cmd}-workflow"
    text = source.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    description = meta.get("description") or f"i18nstack workflow: {cmd}"
    write_skill_md(catalog / skill_name / "SKILL.md", skill_name, description, body)
    count += 1

print(f"skills/ catalog ready: {count} skills")
PY