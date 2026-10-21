#!/usr/bin/env python3
"""Save/list local UI style recipes without activating or overwriting them."""

import argparse
import json
import math
import os
from pathlib import Path
import re
import sys


COLORS = (
    "background", "surface", "text", "mutedText", "border", "primary",
    "onPrimary", "success", "warning", "danger", "focus",
)
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def nonempty_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty string")


def reject_unknown_keys(value, allowed, label):
    extra = set(value) - set(allowed)
    if extra:
        raise ValueError(f"{label} has unknown keys: {sorted(extra)}; keep component states in the specification")


def validate_tokens(data):
    """Validate portable contract shape; theme adapters validate CSS semantics."""
    if not isinstance(data, dict) or type(data.get("schemaVersion")) is not int or data["schemaVersion"] != 1:
        raise ValueError("tokens.schemaVersion must be integer 1")
    nonempty_text(data.get("name"), "tokens.name")
    modes = data.get("modes")
    if not isinstance(modes, dict) or "light" not in modes or set(modes) - {"light", "dark"}:
        raise ValueError("tokens.modes must contain light and optionally dark")
    for mode, colors in modes.items():
        if not isinstance(colors, dict):
            raise ValueError(f"tokens.modes.{mode} must be an object")
        for key in COLORS:
            nonempty_text(colors.get(key), f"tokens.modes.{mode}.{key}")
    typography = data.get("typography")
    if not isinstance(typography, dict):
        raise ValueError("tokens.typography must be an object")
    nonempty_text(typography.get("fontFamily"), "tokens.typography.fontFamily")
    for section, key, allow_zero in (
        ("typography", "fontSize", False), ("typography", "lineHeight", False),
        ("shape", "borderRadius", True), ("spacing", "unit", False),
        ("control", "height", False), ("motion", "duration", True),
    ):
        group = data.get(section)
        number = group.get(key) if isinstance(group, dict) else None
        if type(number) not in (int, float) or not math.isfinite(number) or number < 0 or (number == 0 and not allow_zero):
            qualifier = "nonnegative" if allow_zero else "positive"
            raise ValueError(f"tokens.{section}.{key} must be a finite {qualifier} number")
    if type(data["motion"].get("reducedMotion")) is not bool:
        raise ValueError("tokens.motion.reducedMotion must be a boolean")
    reject_unknown_keys(data, ("schemaVersion", "name", "modes", "typography", "shape", "spacing", "control", "motion"), "tokens")
    for mode, colors in modes.items():
        reject_unknown_keys(colors, COLORS, f"tokens.modes.{mode}")
    for group, keys in (
        ("typography", ("fontFamily", "fontSize", "lineHeight")),
        ("shape", ("borderRadius",)), ("spacing", ("unit",)),
        ("control", ("height",)), ("motion", ("duration", "reducedMotion")),
    ):
        reject_unknown_keys(data[group], keys, f"tokens.{group}")


def profile_root(scope, project=None):
    if scope == "project":
        if project is None:
            raise ValueError("--project is required for project scope")
        anchor = Path(project).expanduser().resolve()
        if not anchor.is_dir():
            raise ValueError("--project must be an existing directory")
        segments = (".ui-styles", "profiles")
    elif scope == "user":
        if project is not None:
            raise ValueError("--project cannot be used with user scope")
        configured = os.environ.get("XDG_CONFIG_HOME")
        anchor = Path(configured).expanduser() if configured else Path.home() / ".config"
        if not anchor.is_absolute():
            raise ValueError("XDG_CONFIG_HOME must be an absolute path")
        anchor = anchor.resolve()
        segments = ("ui-styles", "profiles")
    else:
        raise ValueError("scope must be project or user")
    root = anchor
    for segment in segments:
        root = root / segment
        if root.is_symlink():
            raise ValueError(f"profile storage cannot traverse a symlink: {root}")
        if root.exists() and not root.is_dir():
            raise ValueError(f"profile storage must be a directory: {root}")
    return root


def create_profile(name, scope, project, design, tokens=None, description="", source="custom", dry_run=False):
    if not isinstance(name, str) or len(name) > 64 or not SLUG.fullmatch(name):
        raise ValueError("name must be 1–64 lowercase letters/digits with single hyphens")
    root = profile_root(scope, project)
    target = root / name
    if target.exists() or target.is_symlink():
        raise ValueError(f"profile already exists; inspect it or choose another name: {target}")
    design_text = Path(design).expanduser().read_text(encoding="utf-8")
    nonempty_text(design_text, "design specification")
    token_data = None
    if tokens is not None:
        token_data = json.loads(Path(tokens).expanduser().read_text(encoding="utf-8"))
        validate_tokens(token_data)
    metadata = {
        "schemaVersion": 1, "version": 1, "name": name, "scope": scope,
        "description": description, "source": source,
    }
    files = {"profile.json": json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", "DESIGN.md": design_text}
    if token_data is not None:
        files["tokens.json"] = json.dumps(token_data, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    receipt = {"path": str(target), "scope": scope, "name": name, "files": list(files), "dryRun": dry_run, "activated": False}
    if dry_run:
        return receipt
    root.mkdir(parents=True, exist_ok=True)
    target.mkdir(exist_ok=False)
    for filename, content in files.items():
        with (target / filename).open("x", encoding="utf-8") as output:
            output.write(content)
    return receipt


def list_profiles(scope, project=None):
    root = profile_root(scope, project)
    result = {"root": str(root), "scope": scope, "profiles": [], "invalid": []}
    if not root.exists():
        return result
    for item in sorted(root.iterdir()):
        if item.is_symlink() or not item.is_dir():
            continue
        try:
            for filename in ("profile.json", "DESIGN.md", "tokens.json"):
                if (item / filename).is_symlink():
                    raise ValueError(f"profile files cannot be symlinks: {filename}")
            metadata = json.loads((item / "profile.json").read_text(encoding="utf-8"))
            if not isinstance(metadata, dict) or type(metadata.get("schemaVersion")) is not int or metadata["schemaVersion"] != 1 or metadata.get("name") != item.name or metadata.get("scope") != scope:
                raise ValueError("metadata does not match profile directory/scope")
            if type(metadata.get("version")) is not int or metadata["version"] < 1:
                raise ValueError("profile version must be a positive integer")
            nonempty_text((item / "DESIGN.md").read_text(encoding="utf-8"), "design specification")
            token_path = item / "tokens.json"
            if token_path.exists():
                validate_tokens(json.loads(token_path.read_text(encoding="utf-8")))
            result["profiles"].append({**metadata, "path": str(item), "hasTokens": (item / "tokens.json").is_file()})
        except (OSError, ValueError) as error:
            result["invalid"].append({"name": item.name, "error": str(error)})
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("create", "list"):
        child = commands.add_parser(command)
        child.add_argument("--scope", choices=("project", "user"), default="project")
        child.add_argument("--project", type=Path)
        if command == "create":
            child.add_argument("name")
            child.add_argument("--design", required=True, type=Path)
            child.add_argument("--tokens", type=Path)
            child.add_argument("--description", default="")
            child.add_argument("--source", default="custom")
            child.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command == "create":
            result = create_profile(args.name, args.scope, args.project, args.design, args.tokens, args.description, args.source, args.dry_run)
        else:
            result = list_profiles(args.scope, args.project)
    except (OSError, ValueError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
