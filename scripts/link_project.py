#!/usr/bin/env python3
"""Link an existing visual standard into project instructions; dry-run by default."""

import argparse
import difflib
from pathlib import Path
import re
import sys

START = "<!-- ui-styles:start -->"
END = "<!-- ui-styles:end -->"


def merge_block(original, block):
    """Preserve all text outside one well-formed owned block."""
    starts, ends = original.count(START), original.count(END)
    if not starts and not ends:
        separator = "\n\n" if original and not original.endswith("\n") else "\n" if original else ""
        return original + separator + block + "\n"
    if starts != 1 or ends != 1 or original.index(END) < original.index(START):
        raise ValueError("Malformed or repeated ui-styles markers; inspect the instruction file.")
    first, last = original.index(START), original.index(END) + len(END)
    return original[:first] + block + original[last:]


def has_root_import(text):
    """Recognize a standalone import outside fenced/indented code examples."""
    fence_char, fence_length = None, 0
    for line in text.splitlines():
        marker = re.match(r"^[ \t]*(`{3,}|~{3,})(.*)$", line)
        if marker:
            run, suffix = marker.groups()
            if fence_char is None:
                fence_char, fence_length = run[0], len(run)
            elif run[0] == fence_char and len(run) >= fence_length and not suffix.strip():
                fence_char, fence_length = None, 0
            continue
        if fence_char is None and not line.startswith(("    ", "\t")):
            if line.strip() in ("@AGENTS.md", "@./AGENTS.md"):
                return True
    return False


def plan(project, design, claude=False):
    project = Path(project).expanduser().resolve(strict=True)
    if not project.is_dir():
        raise ValueError("Project must be a directory.")
    relative = Path(design)
    if relative.is_absolute() or ".." in relative.parts or any(x in str(relative) for x in "\n\r`"):
        raise ValueError("Design must be a safe project-relative path.")
    target = (project / relative).resolve(strict=True)
    if not target.is_relative_to(project) or not target.is_file():
        raise ValueError("Visual standard must be an existing file inside the project.")
    path_text = relative.as_posix()
    block = "\n".join([
        START, "## Product UI",
        f"Before building or visually changing product UI, read `{path_text}` and its linked theme sources.",
        "Use the installed ui-styles skill when available, including for demos, component states and UI-library choices.",
        "Preserve the project direction and library; extend missing states consistently before expanding the UI.",
        "Backend-only and nonvisual fixes do not require the design workflow.", END,
    ])
    changes = []
    for name in (["AGENTS.md", "CLAUDE.md"] if claude else ["AGENTS.md"]):
        path = project / name
        if path.is_symlink():
            raise ValueError(f"Instruction file is a symlink; inspect its owner first: {path}")
        before = path.read_text(encoding="utf-8") if path.exists() else ""
        if name == "AGENTS.md":
            after = merge_block(before, block)
        else:
            # Leave an existing exact root import alone. A prose mention is not an import.
            after = before if has_root_import(before) else "@AGENTS.md\n\n" + before
        changes.append((path, before, after))
    return changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True)
    parser.add_argument("--design", default="design/visual-system.md")
    parser.add_argument("--claude", action="store_true", help="Also preserve/add a CLAUDE.md import of AGENTS.md.")
    parser.add_argument("--write", action="store_true", help="Apply the displayed project-local changes.")
    args = parser.parse_args()
    try:
        changes = plan(args.project, args.design, args.claude)
        for path, before, after in changes:
            if before == after:
                continue
            print("".join(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                                             fromfile=str(path), tofile=str(path))), end="")
        if args.write:
            # Recheck all files before any write so ordinary concurrent edits are not lost.
            for path, before, _ in changes:
                if path.is_symlink() or (path.read_text(encoding="utf-8") if path.exists() else "") != before:
                    raise ValueError(f"Instruction file changed; rerun after inspecting: {path}")
            for path, before, after in changes:
                if before != after:
                    path.write_text(after, encoding="utf-8")
            print("Project instructions linked.")
        else:
            print("Dry run; no files written. Use --write to apply.")
        return 0
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
