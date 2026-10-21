import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "skills/ui-style-creator/scripts/profiles.py"
SPEC = importlib.util.spec_from_file_location("style_profiles", SCRIPT)
profiles = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(profiles)


def tokens():
    return {
        "schemaVersion": 1, "name": "test-design",
        "modes": {"light": {key: "#234567" for key in profiles.COLORS}},
        "typography": {"fontFamily": "system-ui, sans-serif", "fontSize": 16, "lineHeight": 1.5},
        "shape": {"borderRadius": 0}, "spacing": {"unit": 4},
        "control": {"height": 40}, "motion": {"duration": 0, "reducedMotion": True},
    }


class ProfileTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "project"
        self.project.mkdir()
        self.design = Path(self.temp.name) / "design.md"
        self.design.write_text("# Test design\nReadable data tables and visible keyboard focus.\n")
        self.token_path = Path(self.temp.name) / "tokens.json"
        self.token_path.write_text(json.dumps(tokens()))

    def create(self, **kwargs):
        options = dict(name="test-style", scope="project", project=self.project, design=self.design)
        options.update(kwargs)
        return profiles.create_profile(**options)

    def test_create_list_and_no_activation(self):
        result = self.create(tokens=self.token_path, source="User brief")
        saved = Path(result["path"])
        self.assertEqual((saved / "DESIGN.md").read_text(), self.design.read_text())
        self.assertEqual(json.loads((saved / "tokens.json").read_text()), tokens())
        self.assertEqual(profiles.list_profiles("project", self.project)["profiles"][0]["name"], "test-style")
        self.assertFalse(result["activated"])
        self.assertFalse((self.project / "AGENTS.md").exists())
        self.assertFalse((self.project / "design").exists())

    def test_existing_profile_is_never_overwritten(self):
        result = self.create()
        path = Path(result["path"]) / "DESIGN.md"
        original = path.read_bytes()
        self.design.write_text("replacement")
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.create()
        self.assertEqual(path.read_bytes(), original)

    def test_dry_run_does_not_create_storage(self):
        result = self.create(tokens=self.token_path, dry_run=True)
        self.assertTrue(result["dryRun"])
        self.assertFalse((self.project / ".ui-styles").exists())

    def test_invalid_slug_never_escapes_project(self):
        for name in ("../escape", "a/b", "a\\b", ".", "a--b", "-a", "Upper", "x" * 65):
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.create(name=name)
        self.assertFalse((self.project / ".ui-styles").exists())

    def test_reject_symlink_storage_and_target(self):
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        (self.project / ".ui-styles").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            self.create()
        self.assertEqual(list(outside.iterdir()), [])
        (self.project / ".ui-styles").unlink()
        root = self.project / ".ui-styles/profiles"
        root.mkdir(parents=True)
        (root / "test-style").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.create()

    def test_user_scope_is_explicit_and_isolated(self):
        config = Path(self.temp.name) / "config"
        with patch.dict(os.environ, {"XDG_CONFIG_HOME": str(config)}):
            result = self.create(scope="user", project=None)
            self.assertEqual(Path(result["path"]), config.resolve() / "ui-styles/profiles/test-style")
            self.assertEqual(len(profiles.list_profiles("user")["profiles"]), 1)
        self.assertFalse((self.project / ".ui-styles").exists())

    def test_missing_scope_context_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "--project is required"):
            self.create(project=None)
        with self.assertRaisesRegex(ValueError, "cannot be used"):
            self.create(scope="user")
        with patch.dict(os.environ, {"XDG_CONFIG_HOME": "relative"}):
            with self.assertRaisesRegex(ValueError, "absolute"):
                self.create(scope="user", project=None)

    def test_invalid_tokens_fail_before_writing(self):
        invalid = tokens()
        invalid["modes"]["dark"] = {"background": "#000000"}
        self.token_path.write_text(json.dumps(invalid))
        with self.assertRaisesRegex(ValueError, "dark.surface"):
            self.create(tokens=self.token_path)
        self.assertFalse((self.project / ".ui-styles").exists())
        for value in (float("nan"), float("inf"), -1, True):
            invalid = tokens()
            invalid["control"]["height"] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                profiles.validate_tokens(invalid)

    def test_blank_design_rejected_and_missing_tokens_allowed(self):
        self.design.write_text("  \n")
        with self.assertRaisesRegex(ValueError, "nonempty"):
            self.create()
        self.assertFalse((self.project / ".ui-styles").exists())
        self.design.write_text("# Qualitative style\nA readable editorial design.\n")
        result = self.create()
        self.assertNotIn("tokens.json", result["files"])

    def test_unknown_token_fields_rejected_before_save(self):
        for group in (None, "typography", "shape", "spacing", "control", "motion", "light"):
            invalid = tokens()
            target = invalid if group is None else invalid["modes"]["light"] if group == "light" else invalid[group]
            target["extraState"] = "#111111"
            self.token_path.write_text(json.dumps(invalid))
            with self.subTest(group=group), self.assertRaisesRegex(ValueError, "unknown keys"):
                self.create(tokens=self.token_path)
            self.assertFalse((self.project / ".ui-styles").exists())

    def test_saved_profile_can_be_exported(self):
        saved = Path(self.create(tokens=self.token_path)["path"])
        exporter = SCRIPT.parents[3] / "scripts" / "export_theme.py"
        for library in ("css", "semi", "antd", "mui"):
            result = subprocess.run([sys.executable, str(exporter), str(saved / "tokens.json"),
                                     "--library", library], capture_output=True, text=True)
            with self.subTest(library=library):
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue(result.stdout)

    def test_listing_identifies_incomplete_profile(self):
        saved = Path(self.create()["path"])
        (saved / "DESIGN.md").unlink()
        result = profiles.list_profiles("project", self.project)
        self.assertEqual(result["profiles"], [])
        self.assertEqual(result["invalid"][0]["name"], "test-style")
        (saved / "DESIGN.md").write_text("Valid design")
        metadata_path = saved / "profile.json"
        metadata = json.loads(metadata_path.read_text())
        metadata.pop("version")
        metadata_path.write_text(json.dumps(metadata))
        result = profiles.list_profiles("project", self.project)
        self.assertEqual(result["profiles"], [])
        self.assertIn("version", result["invalid"][0]["error"])

    def test_listing_reports_invalid_profile_without_hiding_valid_one(self):
        self.create()
        broken = self.project / ".ui-styles/profiles/broken"
        broken.mkdir()
        (broken / "profile.json").write_text("invalid json")
        result = profiles.list_profiles("project", self.project)
        self.assertEqual(len(result["profiles"]), 1)
        self.assertEqual(result["invalid"][0]["name"], "broken")

    def test_cli_round_trip_and_failure_status(self):
        base = [sys.executable, str(SCRIPT), "create", "cli-style", "--project", str(self.project), "--design", str(self.design)]
        first = subprocess.run(base, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertFalse(json.loads(first.stdout)["activated"])
        second = subprocess.run(base, capture_output=True, text=True)
        self.assertEqual(second.returncode, 1)
        self.assertIn("already exists", json.loads(second.stderr)["error"])


if __name__ == "__main__":
    unittest.main()
