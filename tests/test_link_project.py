import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "link_project.py"
SPEC = importlib.util.spec_from_file_location("link_project", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ProjectLinkTests(unittest.TestCase):
    def test_preserves_existing_rules_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "DESIGN.md").write_text("# Existing visual system")
            (root / "AGENTS.md").write_text("# Engineering\nKeep the current library.\n")
            (root / "CLAUDE.md").write_text("# Existing Claude rules\n")
            changes = MODULE.plan(root, "DESIGN.md", True)
            for path, before, after in changes:
                self.assertIn(before, after)
                path.write_text(after)
            for _, before, after in MODULE.plan(root, "DESIGN.md", True):
                self.assertEqual(before, after)

    def test_rejects_bad_marker_without_altering_content(self):
        with self.assertRaises(ValueError):
            MODULE.merge_block(MODULE.START + "\nuser text", "replacement")

    def test_rejects_external_design_and_symlinked_instruction(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "project"
            project.mkdir()
            (root / "external.md").write_text("Private rules")
            with self.assertRaises(ValueError):
                MODULE.plan(project, "../external.md")
            (project / "DESIGN.md").write_text("Project visual rules")
            (project / "AGENTS.md").symlink_to(root / "external.md")
            with self.assertRaises(ValueError):
                MODULE.plan(project, "DESIGN.md")
            self.assertEqual((root / "external.md").read_text(), "Private rules")

    def test_cli_defaults_to_dry_run(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "DESIGN.md").write_text("Visual rules")
            result = subprocess.run([sys.executable, str(SCRIPT), "--project", directory,
                                     "--design", "DESIGN.md"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse((root / "AGENTS.md").exists())

    def test_existing_import_is_not_duplicated(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "DESIGN.md").write_text("Visual rules")
            (root / "CLAUDE.md").write_text("@AGENTS.md\n\nKeep other rules.\n")
            changes = MODULE.plan(root, "DESIGN.md", True)
            self.assertEqual(changes[1][1], changes[1][2])

    def test_code_examples_do_not_count_as_imports(self):
        examples = ("```markdown\n@AGENTS.md\n```\n",
                    "~~~\n@./AGENTS.md\n~~~\n", "    @AGENTS.md\n", "`@AGENTS.md`\n")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "DESIGN.md").write_text("Visual rules")
            for example in examples:
                with self.subTest(example=example):
                    (root / "CLAUDE.md").write_text(example)
                    changes = MODULE.plan(root, "DESIGN.md", True)
                    self.assertEqual(changes[1][2], "@AGENTS.md\n\n" + example)
                    self.assertTrue(MODULE.has_root_import(changes[1][2]))


if __name__ == "__main__":
    unittest.main()
