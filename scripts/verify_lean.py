#!/usr/bin/env python3
"""Fresh-build the research proofs and audit every theorem's printed axioms.

Python standard library only. Prepare the pinned Lake dependencies/cache first.
Only the project's generated .lake/build directory is removed for a fresh build.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time

ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def code_only(text: str) -> str:
    """Blank Lean comments (including nested blocks) and string literals."""
    out, i, depth, quoted = [], 0, 0, False
    while i < len(text):
        pair, char = text[i:i + 2], text[i]
        if depth:
            if pair == "/-":
                depth += 1
                out.extend("  ")
                i += 2
                continue
            if pair == "-/":
                depth -= 1
                out.extend("  ")
                i += 2
                continue
            out.append("\n" if char == "\n" else " ")
        elif quoted:
            if char == "\\" and i + 1 < len(text):
                out.extend("  ")
                i += 2
                continue
            if char == '"':
                quoted = False
            out.append("\n" if char == "\n" else " ")
        elif pair == "/-":
            depth = 1
            out.extend("  ")
            i += 2
            continue
        elif pair == "--":
            end = text.find("\n", i)
            if end == -1:
                end = len(text)
            out.extend(" " * (end - i))
            i = end
            continue
        elif char == '"':
            quoted = True
            out.append(" ")
        else:
            out.append(char)
        i += 1
    if depth or quoted:
        raise ValueError("Unclosed Lean comment or string")
    return "".join(out)


def run(command: list[str], project: Path, output: Path, name: str,
        timeout: int) -> dict:
    start = time.monotonic()
    log = output / f"{name}.log"
    with log.open("w") as handle:
        proc = subprocess.Popen(command, cwd=project, stdout=handle,
                                stderr=subprocess.STDOUT, start_new_session=True)
        try:
            exit_code = proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                proc.wait()
            exit_code = 124
    return {"command": command, "exit_code": exit_code,
            "elapsed_seconds": round(time.monotonic() - start, 3),
            "timeout_seconds": timeout, "log": log.name,
            "log_sha256": digest(log)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--timeout", type=int, default=300)
    args = parser.parse_args()
    project, output = args.project.resolve(), args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    receipt = {"schema": "voss.portable-lean-verification.v1",
               "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
               "status": "failed", "verifier_sha256": digest(Path(__file__)),
               "allowed_axioms": sorted(ALLOWED), "commands": []}
    try:
        if args.timeout < 1:
            raise ValueError("Timeout must be positive")
        config = (project / "lakefile.lean").read_text()
        if 'moreLeanArgs := #["-DwarningAsError=true"]' not in config:
            raise ValueError("Project must enforce warningAsError in moreLeanArgs")
        match = re.search(r"roots\s*:=\s*#\[(.*?)\]", config, re.S)
        if not match:
            raise ValueError("Explicit Lake proof roots are required")
        roots = re.findall(r"`([A-Za-z0-9_.]+)", match.group(1))
        sources = sorted(p for p in project.glob("*.lean") if p.name != "lakefile.lean")
        if set(roots) != {p.stem for p in sources} or len(roots) != len(sources):
            raise ValueError("Lake roots and proof-source inventory differ")
        inventory = []
        for source in sources:
            text = source.read_text()
            code = code_only(text)
            forbidden = re.findall(r"\b(?:sorry|admit|axiom|unsafe|native_decide|implemented_by|extern)\b", code)
            if forbidden or re.search(r"warningAsError\s+false", code):
                raise ValueError(f"Forbidden proof/trust override in {source.name}: {forbidden}")
            namespaces = re.findall(r"^namespace\s+([\w.]+)\s*$", code, re.M)
            if len(namespaces) != 1:
                raise ValueError(f"Expected one explicit namespace in {source.name}")
            names = re.findall(r"^theorem\s+(\w+)\b", code, re.M)
            prints = re.findall(r"^#print\s+axioms\s+(\w+)\s*$", code, re.M)
            if set(names) != set(prints) or len(names) != len(prints):
                raise ValueError(f"Missing or duplicate axiom reports in {source.name}")
            inventory.extend({"module": source.name, "name": namespaces[0] + "." + name}
                             for name in names)
        expected = {item["name"] for item in inventory}
        if not expected or len(expected) != len(inventory):
            raise ValueError("Empty or duplicate theorem inventory")
        receipt.update(module_count=len(sources), theorem_count=len(expected),
                       theorem_inventory=inventory, warnings_as_errors=True,
                       source_sha256={p.name: digest(p) for p in sources},
                       configuration_sha256={n: digest(project / n) for n in
                                             ["lakefile.lean", "lean-toolchain", "lake-manifest.json"]})
        version = run(["lake", "env", "lean", "--version"], project, output,
                      "version", args.timeout)
        receipt["commands"].append(version)
        if version["exit_code"]:
            raise RuntimeError("Pinned Lean is unavailable; see version.log")
        receipt["lean_version"] = (output / "version.log").read_text().strip()
        if "version 4.19.0," not in receipt["lean_version"]:
            raise RuntimeError("Expected Lean 4.19.0")
        manifest = json.loads((project / "lake-manifest.json").read_text())
        revisions = {}
        for package in manifest["packages"]:
            actual = subprocess.run(["git", "rev-parse", "HEAD"],
                                    cwd=project / manifest["packagesDir"] / package["name"],
                                    check=True, capture_output=True, text=True).stdout.strip()
            if actual != package["rev"]:
                raise RuntimeError(f"Dependency revision differs: {package['name']}")
            revisions[package["name"]] = actual
        receipt["dependency_revisions"] = revisions
        generated = project / ".lake" / "build"
        if output == generated or generated in output.parents:
            raise ValueError("Output cannot be inside the generated build directory")
        if generated.exists():
            shutil.rmtree(generated)
        receipt["clean_project_build"] = True
        build = run(["lake", "build"], project, output, "build", args.timeout)
        receipt["commands"].append(build)
        if build["exit_code"]:
            raise RuntimeError("Fresh Lean build failed; see build.log")
        build_text = (output / "build.log").read_text()
        receipt["build_warning_count"] = len(re.findall(r"\bwarning:", build_text))
        receipt["build_error_count"] = len(re.findall(r"\berror:", build_text))
        if receipt["build_warning_count"] or receipt["build_error_count"]:
            raise RuntimeError("The proof build must contain zero warnings and zero errors")
        reports = re.findall(r"'([^']+)' depends on axioms:\s*\[([^]]*)\]", build_text, re.S)
        deps = {name: [a.strip() for a in ax.split(",") if a.strip()] for name, ax in reports}
        if set(deps) != expected or len(reports) != len(expected):
            raise RuntimeError("Build axiom reports do not exactly match all source theorems")
        if any(set(axioms) - ALLOWED for axioms in deps.values()):
            raise RuntimeError("Unexpected axiom dependency")
        receipt.update(axiom_dependencies=deps, axiom_report_count=len(deps))
        controls = output / "controls"
        controls.mkdir(exist_ok=True)
        positive = controls / "AcceptedTrue.lean"
        negative = controls / "RejectedFalse.lean"
        positive.write_text("example : (0 : Nat) = 0 := by decide\n")
        negative.write_text("example : (0 : Nat) = 1 := by decide\n")
        for name, path in [("positive_control", positive), ("negative_control", negative)]:
            result = run(["lake", "env", "lean", "-DwarningAsError=true", os.path.relpath(path, project)],
                         project, output, name, args.timeout)
            receipt["commands"].append(result)
            receipt[name] = result
        if receipt["positive_control"]["exit_code"] != 0:
            raise RuntimeError("True-proposition control failed")
        negative_text = (output / "negative_control.log").read_text()
        if (receipt["negative_control"]["exit_code"] != 1 or
                "error:" not in negative_text or "decide" not in negative_text or
                "is false" not in negative_text):
            raise RuntimeError("False proposition was not rejected by the expected proof error")
        receipt["compiled_sha256"] = {
            root + ".olean": digest(generated / "lib" / "lean" / (root + ".olean"))
            for root in roots}
        receipt["status"] = "passed"
        receipt["negative_control_rejected"] = True
    except Exception as exc:
        receipt["failure"] = str(exc)
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k: receipt[k] for k in ["status", "module_count", "theorem_count",
                                            "axiom_report_count", "negative_control_rejected",
                                            "failure"] if k in receipt}, indent=2))
    return 0 if receipt["status"] == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())
