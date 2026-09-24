#!/usr/bin/env python3
"""
Locked Article Content Integrity Verification Script (CI Gate)
Repository: Khaittc/Agents-Web-Blog-Content
Validates that all approved/locked articles (BLOG_01, BLOG_02, BLOG_03, etc.)
have not been modified by comparing actual HTML content SHA-256 against approved_content_sha256.
Uses Python standard library only.
"""

import sys
import json
import hashlib
import re
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT_DIR / "03_Articles"

HEX_64_PATTERN = re.compile(r"^[0-9A-Fa-f]{64}$")
GIT_COMMIT_SHA_PATTERN = re.compile(r"^[0-9a-fA-F]{7,40}$")


def verify_git_commit_exists(commit_sha: str) -> bool:
    """Checks whether the specified commit exists in local git history if git is available."""
    try:
        result = subprocess.run(
            ["git", "cat-file", "-t", commit_sha],
            cwd=str(ROOT_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        return result.returncode == 0 and result.stdout.strip() == "commit"
    except Exception:
        # If git executable is not available or outside repo, do not hard-fail provenance check
        return True


def verify_article(status_file: Path) -> dict:
    """Verifies a single article status file and its corresponding HTML content hash."""
    article_dir = status_file.parent
    rel_path = status_file.relative_to(ROOT_DIR)

    try:
        with open(status_file, "r", encoding="utf-8-sig") as f:
            status_data = json.load(f)
    except Exception as e:
        return {
            "status_file": str(rel_path),
            "is_locked": False,
            "passed": False,
            "error": f"Failed to read/parse JSON: {e}",
        }

    status = status_data.get("status")
    is_locked = status_data.get("is_locked", False)
    article_id = status_data.get("article_id", article_dir.name)

    # Only verify approved or locked articles
    if status != "APPROVED" and not is_locked:
        return {
            "status_file": str(rel_path),
            "article_id": article_id,
            "is_locked": False,
            "passed": True,
            "message": "Article is in progress (not approved/locked), skipped.",
        }

    # Locked/Approved article must have approved_content_sha256
    expected_sha256 = status_data.get("approved_content_sha256", "").strip()
    if not expected_sha256:
        return {
            "status_file": str(rel_path),
            "article_id": article_id,
            "is_locked": True,
            "passed": False,
            "error": "Missing 'approved_content_sha256' in article_status.json",
        }

    if not HEX_64_PATTERN.match(expected_sha256):
        return {
            "status_file": str(rel_path),
            "article_id": article_id,
            "is_locked": True,
            "passed": False,
            "error": f"Invalid 'approved_content_sha256' format: '{expected_sha256}' (must be 64-char hex)",
        }

    # Locate HTML file
    html_filename = status_data.get("html_file")
    if not html_filename:
        return {
            "status_file": str(rel_path),
            "article_id": article_id,
            "is_locked": True,
            "passed": False,
            "error": "Missing 'html_file' property in article_status.json",
        }

    html_path = article_dir / html_filename
    if not html_path.is_file():
        return {
            "status_file": str(rel_path),
            "article_id": article_id,
            "is_locked": True,
            "passed": False,
            "error": f"Referenced HTML file does not exist: {html_path.relative_to(ROOT_DIR)}",
        }

    # Calculate actual SHA-256
    try:
        content_bytes = html_path.read_bytes()
        actual_sha256 = hashlib.sha256(content_bytes).hexdigest().upper()
    except Exception as e:
        return {
            "status_file": str(rel_path),
            "article_id": article_id,
            "is_locked": True,
            "passed": False,
            "error": f"Failed reading HTML file bytes: {e}",
        }

    if actual_sha256 != expected_sha256.upper():
        return {
            "status_file": str(rel_path),
            "article_id": article_id,
            "is_locked": True,
            "passed": False,
            "error": (
                f"INTEGRITY VIOLATION / MISMATCH in {article_id}!\n"
                f"  Actual SHA-256:   {actual_sha256}\n"
                f"  Approved SHA-256: {expected_sha256.upper()}"
            ),
        }

    # Check commit provenance format
    commit_sha = status_data.get("approved_commit_sha", "").strip()
    if commit_sha:
        if not GIT_COMMIT_SHA_PATTERN.match(commit_sha):
            return {
                "status_file": str(rel_path),
                "article_id": article_id,
                "is_locked": True,
                "passed": False,
                "error": f"Invalid 'approved_commit_sha' format: '{commit_sha}'",
            }
        if not verify_git_commit_exists(commit_sha):
            # Non-fatal warning if shallow clone or external, but logged
            print(f"  [WARN] {article_id} approved_commit_sha '{commit_sha}' not found in current git history.")

    return {
        "status_file": str(rel_path),
        "article_id": article_id,
        "is_locked": True,
        "passed": True,
        "sha256": actual_sha256,
        "commit_sha": commit_sha or "N/A",
    }


def main():
    print("=" * 70)
    print("RUNNING LOCKED ARTICLE INTEGRITY VERIFICATION (PHASE 2.5.1 CI)")
    print("=" * 70)

    if not ARTICLES_DIR.is_dir():
        print(f"Articles directory not found: {ARTICLES_DIR}", file=sys.stderr)
        sys.exit(1)

    status_files = sorted(ARTICLES_DIR.glob("*/article_status.json"))
    if not status_files:
        print("No article_status.json files found. Nothing to verify.")
        sys.exit(0)

    all_passed = True
    verified_count = 0

    for status_file in status_files:
        res = verify_article(status_file)
        art_id = res.get("article_id", status_file.parent.name)

        if not res["passed"]:
            all_passed = False
            print(f"  [FAIL] {art_id}: {res['error']}", file=sys.stderr)
        elif res.get("is_locked"):
            verified_count += 1
            print(f"  [PASS] {art_id} (LOCKED / APPROVED)")
            print(f"         Content SHA-256: {res['sha256']}")
            print(f"         Provenance Commit: {res['commit_sha']}")
        else:
            print(f"  [SKIP] {art_id}: {res.get('message', 'Not locked')}")

    print("=" * 70)
    if all_passed:
        print(f">>> ALL {verified_count} LOCKED ARTICLES PASSED INTEGRITY VERIFICATION <<<")
        print("=" * 70)
        sys.exit(0)
    else:
        print(">>> LOCKED ARTICLE INTEGRITY VERIFICATION FAILED <<<", file=sys.stderr)
        print("=" * 70)
        sys.exit(1)


if __name__ == "__main__":
    main()
