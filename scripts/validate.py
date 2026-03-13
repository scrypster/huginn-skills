#!/usr/bin/env python3
"""Validate registry YAML files without building output."""

import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
REGISTRY_SKILLS = ROOT / "registry" / "skills"
REGISTRY_COLLECTIONS = ROOT / "registry" / "collections"

VALID_CATEGORIES = {
    "workflow", "debugging", "testing", "git", "language", "security",
    "documentation", "ai", "data", "devops", "meta",
}

REQUIRED_SKILL_FIELDS = [
    "id", "name", "display_name", "author", "description",
    "version", "category", "tags", "source_url",
]

REQUIRED_COLLECTION_FIELDS = [
    "id", "name", "display_name", "author", "description", "skills",
]


def validate_skill(data: dict, path: Path) -> list[str]:
    errors = []
    for field in REQUIRED_SKILL_FIELDS:
        if field not in data:
            errors.append(f"missing required field: {field}")

    if "id" in data:
        expected = f"{path.parent.name}/{path.stem}"
        if data["id"] != expected:
            errors.append(f"id mismatch: got '{data['id']}', expected '{expected}'")

    if "category" in data and data["category"] not in VALID_CATEGORIES:
        errors.append(f"unknown category '{data['category']}' — valid: {sorted(VALID_CATEGORIES)}")

    if "tags" in data and not isinstance(data["tags"], list):
        errors.append("tags must be a list")

    if "source_url" in data and not data["source_url"].startswith("https://"):
        errors.append("source_url must start with https://")

    if "description" in data and len(data["description"]) > 120:
        errors.append(f"description too long ({len(data['description'])} chars, max 120)")

    return errors


def validate_collection(data: dict, path: Path) -> list[str]:
    errors = []
    for field in REQUIRED_COLLECTION_FIELDS:
        if field not in data:
            errors.append(f"missing required field: {field}")

    if "id" in data:
        expected = f"{path.parent.name}/{path.stem}"
        if data["id"] != expected:
            errors.append(f"id mismatch: got '{data['id']}', expected '{expected}'")

    if "skills" in data and not isinstance(data["skills"], list):
        errors.append("skills must be a list")

    return errors


def main():
    all_errors = []

    for yaml_path in sorted(REGISTRY_SKILLS.glob("**/*.yaml")):
        try:
            with open(yaml_path) as f:
                data = yaml.safe_load(f)
            errs = validate_skill(data, yaml_path)
        except Exception as e:
            errs = [f"parse error: {e}"]

        if errs:
            all_errors.append((yaml_path.relative_to(ROOT), errs))

    for yaml_path in sorted(REGISTRY_COLLECTIONS.glob("**/*.yaml")):
        try:
            with open(yaml_path) as f:
                data = yaml.safe_load(f)
            errs = validate_collection(data, yaml_path)
        except Exception as e:
            errs = [f"parse error: {e}"]

        if errs:
            all_errors.append((yaml_path.relative_to(ROOT), errs))

    if all_errors:
        for path, errs in all_errors:
            print(f"FAIL {path}")
            for e in errs:
                print(f"     {e}")
        print(f"\n{len(all_errors)} file(s) with errors")
        sys.exit(1)
    else:
        skill_count = len(list(REGISTRY_SKILLS.glob("**/*.yaml")))
        col_count = len(list(REGISTRY_COLLECTIONS.glob("**/*.yaml")))
        print(f"OK — {skill_count} skills, {col_count} collections validated")
