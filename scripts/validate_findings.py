"""Validate agent-reviewed sitemap audit records; does not infer SEO results."""
import argparse
import datetime
import json
from pathlib import Path
from urllib.parse import urlsplit

RESULTS = {"√", "X", "N/A", "Human check"}
IDS = {f"11.{n}" for n in range(1, 10)}


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["Root must be an object"]
    for key in ("site_name", "site_url", "audit_date"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            errors.append(f"{key}: nonempty string required")
    def is_url(value):
        if not isinstance(value, str):
            return False
        try:
            parsed = urlsplit(value)
            return parsed.scheme in {"http", "https"} and bool(parsed.hostname)
        except ValueError:
            return False
    if not is_url(data.get("site_url")):
        errors.append("site_url: absolute HTTP(S) URL required")
    try:
        date = data.get("audit_date", "")
        if datetime.date.fromisoformat(date).isoformat() != date:
            raise ValueError()
    except (ValueError, TypeError):
        errors.append("audit_date: YYYY-MM-DD required")
    checks = data.get("checks")
    if not isinstance(checks, list):
        return errors + ["checks: list required"]
    seen = []
    for index, check in enumerate(checks):
        if not isinstance(check, dict):
            errors.append(f"row {index}: object required")
            continue
        ident = check.get("id")
        seen.append(ident if isinstance(ident, str) else "invalid")
        prefix = f"row {index} ({ident})"
        if not isinstance(check.get("result"), str) or check["result"] not in RESULTS:
            errors.append(f"{prefix}: invalid result")
        for key in ("item_name", "finding", "coverage"):
            if not isinstance(check.get(key), str) or not check[key].strip():
                errors.append(f"{prefix}: {key} required")
        action = check.get("action")
        if not isinstance(action, str):
            errors.append(f"{prefix}: action must be string")
        elif check.get("result") in ("X", "Human check") and not action.strip():
            errors.append(f"{prefix}: action required for this result")
        for key in ("urls", "evidence", "screenshots"):
            value = check.get(key)
            if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
                errors.append(f"{prefix}: {key} must be a list of nonempty strings")
        if isinstance(check.get("urls"), list) and any(not is_url(x) for x in check["urls"]):
            errors.append(f"{prefix}: urls must be absolute HTTP(S) URLs")
    if len(seen) != 9 or set(seen) != IDS:
        errors.append("checks must contain 11.1–11.9 exactly once")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("findings", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.findings.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Cannot read findings: {exc}\n")
    errors = validate(data)
    if errors:
        parser.exit(1, "\n".join(errors) + "\n")
    print("Valid findings structure: all nine sitemap checks present.")


if __name__ == "__main__":
    main()
