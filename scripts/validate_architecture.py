#!/usr/bin/env python3
"""
Architecture Validation Script (CI Gate)
Repository: Khaittc/Agents-Web-Blog-Content
Validates JSON schemas, Canonical Taxonomy, Stable Source IDs, Required Contracts,
Human-only publishing compliance, and Two-Gate pipeline consistency.
Uses Python standard library only.
"""

import os
import sys
import json
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------
# Configuration & Constants
# -------------------------------------------------------------

CONTRACTS_DIR = ROOT_DIR / "02_AGENT_TEMPLATES" / "contracts"

REQUIRED_CONTRACTS = [
    "article_brief.schema.json",
    "research_plan.schema.json",
    "evidence.schema.json",
    "claim_source_map.schema.json",
    "audit.schema.json",
    "revision_request.schema.json",
    "article_manifest.schema.json",
]

CANONICAL_TAXONOMY = {
    "BLOG-T01": "Technical Explanation",
    "BLOG-T02": "How-to / Measurement",
    "BLOG-T03": "Troubleshooting",
    "BLOG-T04": "Comparison",
    "BLOG-T05": "Best Practice / Engineering Guide",
}

FORBIDDEN_TAXONOMY_MAPPINGS = [
    (r"BLOG-T02\s*[-–—:]\s*(Calculation|Case Study)", "BLOG-T02 must be 'How-to / Measurement'"),
    (r"BLOG-T04\s*[-–—:]\s*(Standard|Compliance)", "BLOG-T04 must be 'Comparison'"),
    (r"BLOG-T05\s*[-–—:]\s*Comparison", "BLOG-T05 must be 'Best Practice / Engineering Guide'"),
]

# Files to check for active taxonomy, human publishing, and two-gate pipeline
ACTIVE_DOC_PATHS = [
    ROOT_DIR / "README.md",
    ROOT_DIR / "AGENT_GUIDE.md",
    ROOT_DIR / "ROADMAP.md",
    ROOT_DIR / "00_SKILL" / "BLOG_CONTENT_STRUCTURE_STANDARD_v1.3.md",
    ROOT_DIR / "00_SKILL" / "BLOG_TAXONOMY_CANONICAL_v1.0.md",
]

# Add all markdown files in 02_AGENT_TEMPLATES/
for md_file in (ROOT_DIR / "02_AGENT_TEMPLATES").glob("*.md"):
    ACTIVE_DOC_PATHS.append(md_file)


# -------------------------------------------------------------
# Gate 1 & Gate 4: Contract Existence and JSON Schema Validation
# -------------------------------------------------------------

def validate_contracts():
    errors = []
    print("[Gate 1 & 4] Checking Required Contracts & JSON Schema validity...")

    for schema_name in REQUIRED_CONTRACTS:
        schema_path = CONTRACTS_DIR / schema_name
        if not schema_path.is_file():
            errors.append(f"Missing required contract schema: {schema_path}")
            continue

        try:
            with open(schema_path, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
        except Exception as e:
            errors.append(f"Invalid JSON syntax in {schema_name}: {e}")
            continue

        # Basic schema structural checks
        if "$schema" not in data:
            errors.append(f"{schema_name} is missing '$schema' field")
        if "title" not in data:
            errors.append(f"{schema_name} is missing 'title' field")
        if data.get("type") != "object":
            errors.append(f"{schema_name} root type should be 'object'")

        # Recursively check enum uniqueness and non-emptiness
        def check_node(node, path=""):
            if isinstance(node, dict):
                if "enum" in node:
                    enum_vals = node["enum"]
                    if not isinstance(enum_vals, list) or len(enum_vals) == 0:
                        errors.append(f"{schema_name} has invalid or empty enum at {path}")
                    elif len(enum_vals) != len(set(enum_vals)):
                        errors.append(f"{schema_name} has duplicate values in enum at {path}")
                if "required" in node:
                    req_vals = node["required"]
                    if not isinstance(req_vals, list):
                        errors.append(f"{schema_name} 'required' at {path} must be an array")
                for k, v in node.items():
                    check_node(v, f"{path}.{k}")
            elif isinstance(node, list):
                for idx, item in enumerate(node):
                    check_node(item, f"{path}[{idx}]")

        check_node(data)

    if errors:
        for err in errors:
            print(f"  [FAIL] {err}", file=sys.stderr)
        return False

    print(f"  [PASS] All {len(REQUIRED_CONTRACTS)} JSON schemas are valid and structurally sound.")
    return True


# -------------------------------------------------------------
# Gate 2: Canonical Blog Taxonomy
# -------------------------------------------------------------

def validate_canonical_taxonomy():
    errors = []
    print("[Gate 2] Validating Canonical Blog Taxonomy (BLOG-T01 .. BLOG-T05)...")

    for doc_path in ACTIVE_DOC_PATHS:
        if not doc_path.is_file():
            continue

        content = doc_path.read_text(encoding="utf-8", errors="replace")

        # Check for forbidden legacy mappings
        for pattern, msg in FORBIDDEN_TAXONOMY_MAPPINGS:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for m in matches:
                # Find line number
                line_no = content[:m.start()].count("\n") + 1
                errors.append(f"{doc_path.relative_to(ROOT_DIR)}:{line_no} - {msg} (matched '{m.group(0)}')")

    if errors:
        for err in errors:
            print(f"  [FAIL] {err}", file=sys.stderr)
        return False

    print("  [PASS] Canonical Blog Taxonomy verified across all active documentation.")
    return True


# -------------------------------------------------------------
# Gate 3: Stable Source ID Policy
# -------------------------------------------------------------

def validate_stable_source_id_policy():
    errors = []
    print("[Gate 3] Validating Stable Source ID Policy (SRC-xxx in Research)...")

    research_files = [
        ROOT_DIR / "02_AGENT_TEMPLATES" / "research_agent.md",
        ROOT_DIR / "02_AGENT_TEMPLATES" / "contracts" / "evidence.schema.json",
        ROOT_DIR / "00_SKILL" / "SOURCE_TIER_EVIDENCE_WORKFLOW_v1.0.md",
    ]

    # Pattern detecting assigning IEEE numbers [1], [2] as Source ID in research tables/registries
    forbidden_research_patterns = [
        (r"\|\s*\[\d+\]\s*\|\s*Tier\s*[123]", "Forbidden IEEE bracket used as Source ID in table row"),
        (r"Ref\s*ID\s*[:=]\s*\[\d+\]", "Forbidden 'Ref ID = [n]' in Research artifact"),
        (r"Source\s*ID\s*[:=]\s*\[\d+\]", "Forbidden 'Source ID = [n]' in Research artifact"),
        (r'\"source_id\"\s*:\s*\"\[\d+\]\"', "Forbidden 'source_id: \"[n]\"' in evidence schema/data"),
    ]

    for rf in research_files:
        if not rf.is_file():
            continue
        text = rf.read_text(encoding="utf-8", errors="replace")
        for pat, desc in forbidden_research_patterns:
            matches = re.finditer(pat, text, re.IGNORECASE)
            for m in matches:
                line_no = text[:m.start()].count("\n") + 1
                errors.append(f"{rf.relative_to(ROOT_DIR)}:{line_no} - {desc} (matched '{m.group(0)}')")

    # In evidence.schema.json, ensure source_id pattern requires SRC-
    evidence_schema_file = ROOT_DIR / "02_AGENT_TEMPLATES" / "contracts" / "evidence.schema.json"
    if evidence_schema_file.is_file():
        schema_data = json.loads(evidence_schema_file.read_text(encoding="utf-8"))
        src_pattern = (
            schema_data.get("properties", {})
            .get("sources", {})
            .get("items", {})
            .get("properties", {})
            .get("source_id", {})
            .get("pattern", "")
        )
        if "SRC-" not in src_pattern:
            errors.append("evidence.schema.json source_id pattern must enforce 'SRC-' prefix")

    if errors:
        for err in errors:
            print(f"  [FAIL] {err}", file=sys.stderr)
        return False

    print("  [PASS] Stable Source ID policy verified (SRC-xxx enforced, no IEEE numbers in Research).")
    return True


# -------------------------------------------------------------
# Gate 6: Human-Only Publishing Policy
# -------------------------------------------------------------

def validate_human_only_publishing():
    errors = []
    print("[Gate 6] Validating Human-Only Publishing Policy...")

    forbidden_autonomous_publish_patterns = [
        (r"agent\s+(?:tự\s+động\s+)?đăng\s+bài\s+lên\s+cms", "Agent cannot be described as publishing directly to CMS"),
        (r"agent\s+(?:will\s+)?publish(?:es)?\s+directly\s+to\s+cms", "Agent cannot publish directly to CMS"),
        (r"agent\s+tự\s+động\s+xuất\s+bản", "Agent cannot autonomously publish articles"),
        (r"agent\s+sets\s+status\s+to\s+published\s+autonomously", "Agent cannot set status to PUBLISHED autonomously"),
    ]

    for doc_path in ACTIVE_DOC_PATHS:
        if not doc_path.is_file():
            continue
        text = doc_path.read_text(encoding="utf-8", errors="replace")
        for pat, desc in forbidden_autonomous_publish_patterns:
            matches = re.finditer(pat, text, re.IGNORECASE)
            for m in matches:
                line_no = text[:m.start()].count("\n") + 1
                errors.append(f"{doc_path.relative_to(ROOT_DIR)}:{line_no} - {desc} (matched '{m.group(0)}')")

    if errors:
        for err in errors:
            print(f"  [FAIL] {err}", file=sys.stderr)
        return False

    print("  [PASS] Human-Only Publishing policy verified in all active documentation.")
    return True


# -------------------------------------------------------------
# Gate 7: Two-Gate Pipeline Consistency
# -------------------------------------------------------------

def validate_two_gate_pipeline():
    errors = []
    print("[Gate 7] Validating Two-Gate Pipeline Consistency...")

    key_pipeline_files = [
        ROOT_DIR / "README.md",
        ROOT_DIR / "AGENT_GUIDE.md",
        ROOT_DIR / "02_AGENT_TEMPLATES" / "README.md",
        ROOT_DIR / "02_AGENT_TEMPLATES" / "review_agent.md",
        ROOT_DIR / "02_AGENT_TEMPLATES" / "ARTICLE_LIFECYCLE_AND_APPROVAL_PROTOCOL.md",
    ]

    # In key pipeline files, check that both Technical Review Gate and Presentation Review Gate are mentioned
    for pf in key_pipeline_files:
        if not pf.is_file():
            continue
        text = pf.read_text(encoding="utf-8", errors="replace")
        has_gate1 = "Technical Review Gate" in text or "CỔNG 1" in text or "TECH_APPROVED" in text
        has_gate2 = "Presentation" in text or "CỔNG 2" in text or "Responsive Review" in text
        if not (has_gate1 and has_gate2):
            errors.append(f"{pf.relative_to(ROOT_DIR)} missing clear Two-Gate pipeline references (Gate 1 & Gate 2)")

    if errors:
        for err in errors:
            print(f"  [FAIL] {err}", file=sys.stderr)
        return False

    print("  [PASS] Two-Gate Pipeline consistency verified.")
    return True


# -------------------------------------------------------------
# Gate 8: Canonical Article Statuses
# -------------------------------------------------------------

CANONICAL_ARTICLE_STATUSES = {
    "DRAFT",
    "RESEARCHED",
    "TECH_REVIEW",
    "TECH_APPROVED",
    "VISUAL_READY",
    "PRESENTATION_REVIEW",
    "IN_REVIEW",
    "REVISION_REQUESTED",
    "APPROVED",
    "PUBLISHED",
}

def validate_canonical_article_statuses():
    errors = []
    print("[Gate 8] Validating Canonical Article Statuses across 03_Articles...")

    article_dirs = sorted((ROOT_DIR / "03_Articles").glob("BLOG_*"))
    for ad in article_dirs:
        status_file = ad / "article_status.json"
        if not status_file.is_file():
            continue
        try:
            data = json.loads(status_file.read_text(encoding="utf-8-sig"))
        except Exception as e:
            errors.append(f"{status_file.relative_to(ROOT_DIR)} failed to parse JSON: {e}")
            continue

        status = data.get("status")
        if not status:
            errors.append(f"{status_file.relative_to(ROOT_DIR)} missing 'status' field")
        elif status not in CANONICAL_ARTICLE_STATUSES:
            errors.append(
                f"{status_file.relative_to(ROOT_DIR)} has invalid non-canonical status '{status}'. "
                f"Must be one of: {sorted(CANONICAL_ARTICLE_STATUSES)}"
            )

    if errors:
        for err in errors:
            print(f"  [FAIL] {err}", file=sys.stderr)
        return False

    print("  [PASS] Canonical article statuses verified across all articles.")
    return True


# -------------------------------------------------------------
# Gate 9: Source Exception Consistency
# -------------------------------------------------------------

def validate_source_exception_consistency():
    errors = []
    print("[Gate 9] Validating Source Policy Exception Consistency...")

    evidence_files = sorted((ROOT_DIR / "03_Articles").glob("BLOG_*/evidence.json"))
    for ef in evidence_files:
        try:
            data = json.loads(ef.read_text(encoding="utf-8-sig"))
        except Exception as e:
            errors.append(f"{ef.relative_to(ROOT_DIR)} failed to parse JSON: {e}")
            continue

        spe = data.get("source_policy_exception")
        if not spe or not isinstance(spe, dict):
            errors.append(f"{ef.relative_to(ROOT_DIR)} missing 'source_policy_exception' object")
            continue

        is_exception = spe.get("source_policy_exception")
        exc_type = spe.get("exception_type")
        approved = spe.get("approved_by_review_gate")
        verdict = spe.get("review_verdict")

        if is_exception is False:
            if exc_type != "NONE":
                errors.append(
                    f"{ef.relative_to(ROOT_DIR)}: source_policy_exception is False but exception_type is '{exc_type}' (expected 'NONE')"
                )
            if approved is not False:
                errors.append(
                    f"{ef.relative_to(ROOT_DIR)}: source_policy_exception is False but approved_by_review_gate is {approved} (expected False)"
                )
            if verdict != "NOT_APPLICABLE":
                errors.append(
                    f"{ef.relative_to(ROOT_DIR)}: source_policy_exception is False but review_verdict is '{verdict}' (expected 'NOT_APPLICABLE')"
                )
        elif is_exception is True:
            if exc_type == "NONE":
                errors.append(
                    f"{ef.relative_to(ROOT_DIR)}: source_policy_exception is True but exception_type is 'NONE'"
                )
            if verdict not in ("PENDING", "APPROVE_EXCEPTION", "REJECT_EXCEPTION"):
                errors.append(
                    f"{ef.relative_to(ROOT_DIR)}: source_policy_exception is True but review_verdict '{verdict}' is invalid"
                )
            reason = spe.get("reason", "").strip()
            if not reason:
                errors.append(
                    f"{ef.relative_to(ROOT_DIR)}: source_policy_exception is True but reason is empty"
                )

    if errors:
        for err in errors:
            print(f"  [FAIL] {err}", file=sys.stderr)
        return False

    print("  [PASS] Source policy exception consistency verified.")
    return True


# -------------------------------------------------------------
# Main Runner
# -------------------------------------------------------------

def main():
    print("=" * 70)
    print("RUNNING ARCHITECTURE VALIDATION (PHASE 2.5.1 CI)")
    print("=" * 70)

    results = [
        validate_contracts(),
        validate_canonical_taxonomy(),
        validate_stable_source_id_policy(),
        validate_human_only_publishing(),
        validate_two_gate_pipeline(),
        validate_canonical_article_statuses(),
        validate_source_exception_consistency(),
    ]

    print("=" * 70)
    if all(results):
        print(">>> ALL ARCHITECTURE VALIDATION CHECKS PASSED (RESULT: PASS) <<<")
        print("=" * 70)
        sys.exit(0)
    else:
        print(">>> ARCHITECTURE VALIDATION FAILED (RESULT: FAIL) <<<", file=sys.stderr)
        print("=" * 70)
        sys.exit(1)


if __name__ == "__main__":
    main()
