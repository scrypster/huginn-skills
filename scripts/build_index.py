#!/usr/bin/env python3
"""
Build dist/index.json and dist/skills/{id}.json from registry YAML files.

index.json  — compact listing for browse/search (no long_description)
skills/     — one JSON per skill with full detail (for skill detail view)
"""

import json
import os
import sys
import yaml
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
REGISTRY_SKILLS = ROOT / "registry" / "skills"
REGISTRY_COLLECTIONS = ROOT / "registry" / "collections"
CONTENT_DIR = ROOT / "content"
DIST = ROOT / "dist"


def load_yaml(path: Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def validate_skill(data: dict, path: Path) -> list[str]:
    errors = []
    required = ["id", "name", "display_name", "author", "description", "version",
                 "category", "tags", "source_url"]
    for field in required:
        if field not in data:
            errors.append(f"  missing required field: {field}")
    if "id" in data:
        expected_id = f"{path.parent.name}/{path.stem}"
        if data["id"] != expected_id:
            errors.append(f"  id mismatch: got '{data['id']}', expected '{expected_id}'")
    return errors


def validate_collection(data: dict, path: Path) -> list[str]:
    errors = []
    required = ["id", "name", "display_name", "author", "description", "skills"]
    for field in required:
        if field not in data:
            errors.append(f"  missing required field: {field}")
    return errors


def build():
    errors_found = False

    # Load skills
    skills_full = []
    skills_index = []

    for yaml_path in sorted(REGISTRY_SKILLS.glob("**/*.yaml")):
        data = load_yaml(yaml_path)
        errs = validate_skill(data, yaml_path)
        if errs:
            print(f"ERROR in {yaml_path.relative_to(ROOT)}:")
            for e in errs:
                print(e)
            errors_found = True
            continue

        # Full record (for detail view)
        full = {
            "id": data["id"],
            "name": data["name"],
            "display_name": data["display_name"],
            "author": data["author"],
            "description": data["description"],
            "long_description": data.get("long_description", "").strip(),
            "version": data["version"],
            "category": data["category"],
            "tags": data.get("tags", []),
            "license": data.get("license", ""),
            "source_url": data["source_url"],
            "collection": data.get("collection"),
            "created_at": data.get("created_at", ""),
            "updated_at": data.get("updated_at", ""),
        }
        skills_full.append(full)

        # Compact record (for index)
        index_entry = {k: v for k, v in full.items() if k != "long_description"}
        skills_index.append(index_entry)

    # Load collections
    collections = []
    for yaml_path in sorted(REGISTRY_COLLECTIONS.glob("**/*.yaml")):
        data = load_yaml(yaml_path)
        errs = validate_collection(data, yaml_path)
        if errs:
            print(f"ERROR in {yaml_path.relative_to(ROOT)}:")
            for e in errs:
                print(e)
            errors_found = True
            continue

        collections.append({
            "id": data["id"],
            "name": data["name"],
            "display_name": data["display_name"],
            "author": data["author"],
            "description": data["description"],
            "long_description": data.get("long_description", "").strip(),
            "version": data.get("version", "1.0.0"),
            "tags": data.get("tags", []),
            "license": data.get("license", ""),
            "skills": data.get("skills", []),
            "source_repo": data.get("source_repo", ""),
            "created_at": data.get("created_at", ""),
            "updated_at": data.get("updated_at", ""),
        })

    if errors_found:
        print("\nBuild failed due to validation errors.")
        sys.exit(1)

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Write dist/index.json (compact — no long_description)
    DIST.mkdir(exist_ok=True)
    index = {
        "version": "1",
        "generated_at": generated_at,
        "skills": skills_index,
        "collections": [
            {k: v for k, v in c.items() if k != "long_description"}
            for c in collections
        ],
    }
    index_path = DIST / "index.json"
    with open(index_path, "w") as f:
        json.dump(index, f, indent=2)
    print(f"Wrote {index_path.relative_to(ROOT)}  ({index_path.stat().st_size} bytes)")

    # Write dist/skills/{author}/{name}.json (full detail)
    for skill in skills_full:
        author, name = skill["id"].split("/", 1)
        detail_dir = DIST / "skills" / author
        detail_dir.mkdir(parents=True, exist_ok=True)
        detail_path = detail_dir / f"{name}.json"
        with open(detail_path, "w") as f:
            json.dump(skill, f, indent=2)

    print(f"Wrote {len(skills_full)} skill detail files")

    # Write dist/collections/{author}/{name}.json
    for col in collections:
        author, name = col["id"].split("/", 1)
        col_dir = DIST / "collections" / author
        col_dir.mkdir(parents=True, exist_ok=True)
        col_path = col_dir / f"{name}.json"
        with open(col_path, "w") as f:
            json.dump(col, f, indent=2)

    print(f"Wrote {len(collections)} collection detail files")
    print(f"\nBuild complete: {len(skills_index)} skills, {len(collections)} collections")


if __name__ == "__main__":
    build()
