#!/usr/bin/env python3
"""Check release hashes, unchanged source provenance, and local public links.

Standard library only. This checks packaging, not mathematical truth.
"""
from pathlib import Path
import hashlib
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def check_manifest(manifest, root):
    count = 0
    for line in manifest.read_text().splitlines():
        if not line.strip():
            continue
        expected, relative = line.split(maxsplit=1)
        path = root / relative.lstrip('*')
        if not path.is_file():
            raise ValueError(f'Missing manifest file: {path.relative_to(ROOT)}')
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f'Hash mismatch: {path.relative_to(ROOT)}')
        count += 1
    return count


def main():
    count = check_manifest(ROOT / 'SHA256SUMS', ROOT)
    original = check_manifest(ROOT / 'source/v2.4/SHA256SUMS', ROOT / 'source/v2.4')
    for path in (ROOT / 'source/v2.4/lean').glob('*.lean'):
        if path.name == 'lakefile.lean':
            continue
        if path.read_bytes() != (ROOT / 'formal' / path.name).read_bytes():
            raise ValueError(f'Original Lean module changed: {path.name}')
    links = 0
    for path in [ROOT / 'README.md', *sorted((ROOT / 'docs').glob('*.md'))]:
        text = path.read_text()
        if sum(line.strip() == '$$' for line in text.splitlines()) % 2:
            raise ValueError(f'Unpaired display math in {path.name}')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if '://' in target or target.startswith(('#', 'mailto:')):
                continue
            target = unquote(target.split('#')[0].strip('<>'))
            if not (path.parent / target).exists():
                raise ValueError(f'Broken link in {path.name}: {target}')
            links += 1
    print(f'PASS: {count} release hashes, {original} original source hashes, unchanged original Lean modules, {links} local links.')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        raise SystemExit(1)
