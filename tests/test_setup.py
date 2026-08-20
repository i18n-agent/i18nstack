import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[1]


class SetupTests(unittest.TestCase):
    def _copy_checkout(self, home: Path, relative_path: Path) -> Path:
        checkout = home / relative_path
        checkout.mkdir(parents=True)

        shutil.copy2(REPOSITORY / "setup", checkout / "setup")
        (checkout / "setup").chmod(0o755)

        for relative_file in (
            Path("scripts/register-codex.py"),
            Path("scripts/sync-skills-catalog.sh"),
            Path("i18nstack/SKILL.md"),
            Path("i18n-convert/SKILL.md"),
        ):
            destination = checkout / relative_file
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPOSITORY / relative_file, destination)

        (checkout / "scripts/sync-skills-catalog.sh").chmod(0o755)
        return checkout

    def _fake_cli_tools(self, home: Path) -> Path:
        bin_dir = home / "bin"
        bin_dir.mkdir()
        for tool in ("i18n-convert", "i18n-pseudo", "i18n-validate"):
            executable = bin_dir / tool
            executable.write_text(f"#!/bin/sh\necho '{tool} test'\n", encoding="utf-8")
            executable.chmod(0o755)
        return bin_dir

    def _run_setup_twice(self, checkout: Path, home: Path, bin_dir: Path) -> None:
        environment = os.environ.copy()
        environment["HOME"] = str(home)
        environment["PATH"] = f"{bin_dir}{os.pathsep}{environment['PATH']}"

        for _ in range(2):
            subprocess.run(
                [str(checkout / "setup")],
                check=True,
                cwd=checkout,
                env=environment,
                capture_output=True,
                text=True,
            )

    def test_agent_anchors_remain_valid_and_idempotent(self) -> None:
        install_locations = (
            Path(".claude/skills/i18nstack"),
            Path(".grok/skills/i18nstack"),
            Path(".codex/i18nstack"),
        )

        for install_location in install_locations:
            with self.subTest(install_location=install_location):
                with tempfile.TemporaryDirectory() as temporary_directory:
                    home = Path(temporary_directory)
                    for agent_directory in (".claude", ".grok", ".codex", ".agents"):
                        (home / agent_directory).mkdir()

                    checkout = self._copy_checkout(home, install_location)
                    bin_dir = self._fake_cli_tools(home)

                    if install_location != Path(".grok/skills/i18nstack"):
                        grok_skills = home / ".grok/skills"
                        grok_skills.mkdir()
                        (grok_skills / "i18nstack").symlink_to(
                            "i18nstack/i18nstack"
                        )

                    self._run_setup_twice(checkout, home, bin_dir)

                    root_skill = checkout / "SKILL.md"
                    self.assertTrue(root_skill.is_symlink())
                    self.assertEqual(os.readlink(root_skill), "i18nstack/SKILL.md")
                    self.assertIn("name: i18nstack", root_skill.read_text(encoding="utf-8"))

                    for agent in (".claude", ".grok"):
                        anchor = home / agent / "skills/i18nstack"
                        self.assertTrue(anchor.exists())
                        self.assertTrue(os.path.samefile(anchor, checkout))
                        self.assertIn(
                            "name: i18nstack",
                            (anchor / "SKILL.md").read_text(encoding="utf-8"),
                        )

                        tool_skill = home / agent / "skills/i18n-convert"
                        self.assertTrue(tool_skill.exists())
                        self.assertTrue(
                            os.path.samefile(tool_skill, checkout / "i18n-convert")
                        )

                    codex_adapter = home / ".agents/skills/i18nstack/SKILL.md"
                    codex_adapter_text = codex_adapter.read_text(encoding="utf-8")
                    self.assertIn(
                        str(checkout / "i18nstack/SKILL.md"),
                        codex_adapter_text,
                    )
                    self.assertIn(
                        "Complete i18n/localization toolkit for AI coding agents",
                        codex_adapter_text,
                    )
                    self.assertNotIn("tasks requiring: |", codex_adapter_text)

                    catalog_skill = checkout / "skills/i18nstack/SKILL.md"
                    catalog_text = catalog_skill.read_text(encoding="utf-8")
                    self.assertIn(
                        'description: "Complete i18n/localization toolkit',
                        catalog_text,
                    )
                    self.assertNotIn('description: "|"', catalog_text)


if __name__ == "__main__":
    unittest.main()
