"""Check local documentation links, strict JSON, and common publication hazards.

Uses the standard library and does not contact external services. The checks are
heuristics, not a substitute for a human review or a dedicated secret scanner.
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".publish", ".codex", ".agents", ".venv", "venv", "__pycache__", "dist", "node_modules"}
TEXT_SUFFIXES = {".md", ".py", ".json", ".yml", ".yaml", ".txt"}
SECRET_SUFFIXES = {".pem", ".key", ".pfx", ".p12"}
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
SECRET_PATTERNS = (
    ("private-key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("credential-like token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b")),
    ("local user path", re.compile(r"(?i)[a-z]:[\\/]Users[\\/][^\s]+")),
    ("private IPv4 address", re.compile(r"\b(?:10\.\d{1,3}|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b")),
)


def files():
    """List candidate publication files, excluding local/generated directories."""
    return sorted(
        path for path in ROOT.rglob("*")
        if path.is_file() and not set(path.relative_to(ROOT).parts) & SKIP_DIRS
        and path.suffix.lower() not in {".pyc", ".zip", ".log"}
    )


def strict_object(pairs):
    """Reject duplicate keys rather than silently retaining the last value."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def reject_constant(value):
    """Reject non-JSON numeric constants accepted by the default decoder."""
    raise ValueError("non-finite JSON constant: " + value)


def anchors(text):
    """Compute anchors for the simple ATX headings used in this repository."""
    result, counts = set(), {}
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if count == 0 else slug + "-" + str(count))
    return result


def main():
    """Return nonzero when a publication candidate needs correction."""
    errors, documents, json_files, checked_links = [], 0, 0, 0
    candidates = files()
    for path in candidates:
        relative = path.relative_to(ROOT).as_posix()
        if path.name == ".env" or path.name.startswith(".env.") or path.suffix.lower() in SECRET_SUFFIXES:
            errors.append(relative + ": sensitive configuration/key file")
            continue
        if path.suffix not in TEXT_SUFFIXES and path.name not in {".gitignore", ".gitattributes"}:
            errors.append(relative + ": unexpected publication file type; review explicitly")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            errors.append(relative + ": cannot read as UTF-8")
            continue
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(content):
                errors.append(relative + ": possible " + label + " (value omitted)")
        if path.suffix == ".json":
            json_files += 1
            try:
                json.loads(content, object_pairs_hook=strict_object, parse_constant=reject_constant)
            except (ValueError, TypeError) as exc:
                errors.append(relative + ": invalid strict JSON: " + str(exc))
        if path.suffix != ".md":
            continue
        documents += 1
        if not content.startswith("# "):
            errors.append(relative + ": missing document title")
        if content.count("```") % 2:
            errors.append(relative + ": unmatched fenced code block")
        prose = re.sub(r"```.*?```", "", content, flags=re.S)
        for raw in LINK.findall(prose):
            target = raw.strip().strip("<>")
            parts = urlsplit(target)
            if parts.scheme or parts.netloc:
                continue
            checked_links += 1
            destination = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            try:
                destination.relative_to(ROOT)
            except ValueError:
                errors.append(relative + ": link escapes repository: " + target)
                continue
            if not destination.exists():
                errors.append(relative + ": broken local link: " + target)
            elif parts.fragment and destination.suffix == ".md":
                if unquote(parts.fragment) not in anchors(destination.read_text(encoding="utf-8")):
                    errors.append(relative + ": unknown heading anchor: " + target)
    if errors:
        for error in errors:
            print("FAIL " + error)
        return 1
    print("PASS: {} files; {} Markdown documents; {} JSON files; {} local links.".format(
        len(candidates), documents, json_files, checked_links))
    print("No configured publication-hazard patterns matched. Human review still required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
