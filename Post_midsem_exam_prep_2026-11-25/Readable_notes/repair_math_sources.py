"""Repair lost math mode and standardise source Markdown math delimiters.

This migration preserves source copies and records every restored formula.
"""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from build_readable_notes import MATH

OUT = Path(__file__).resolve().parent
BACKUP = OUT / 'reference/math_repair_originals_2026-11-25'


def restore_parenthesised_math(text: str, repairs: list[dict], page: int) -> str:
    """Restore only the demonstrably damaged refresher prose, outside math."""
    pieces = []
    position = 0
    while position < len(text):
        if text[position] != '(' or (position and text[position - 1] == '\\'):
            pieces.append(text[position])
            position += 1
            continue
        depth = 1
        end = position + 1
        while end < len(text) and depth:
            if text[end] == '(':
                depth += 1
            elif text[end] == ')':
                depth -= 1
            end += 1
        if depth:
            pieces.append(text[position:])
            break
        inner = text[position + 1:end - 1]
        mathematical = (bool(re.search(r'\\[A-Za-z]+|[=^_<>]', inner))
                        or bool(re.fullmatch(r'[A-Za-z]{1,3}|\d+|[A-Za-z](?:,[A-Za-z])+|P\([0-9A-Za-z]+\)', inner)))
        if mathematical and '\n' not in inner and not inner.startswith('PDF'):
            repaired = '$' + inner + '$'
            repairs.append({'pdf_page': page, 'before': text[position:end], 'after': repaired})
            pieces.append(repaired)
        else:
            pieces.append(text[position:end])
        position = end
    return ''.join(pieces)


def restore_refresher(text: str, repairs: list[dict]) -> str:
    page_pattern = re.compile(r'(<a id="pdf-page-(\d{3})"></a>)')
    matches = list(page_pattern.finditer(text))
    result = []
    previous = 0
    for index, page_match in enumerate(matches):
        start = page_match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result.append(text[previous:start])
        page = int(page_match.group(2))
        section = text[start:end]
        if 151 <= page <= 160:
            protected = []
            cursor = 0
            for expression in MATH.finditer(section):
                protected.append(restore_parenthesised_math(section[cursor:expression.start()], repairs, page))
                protected.append(expression.group(0))
                cursor = expression.end()
            protected.append(restore_parenthesised_math(section[cursor:], repairs, page))
            section = ''.join(protected)
        result.append(section)
        previous = end
    result.append(text[previous:])
    return ''.join(result)


def canonicalise(text: str, counts: dict) -> str:
    def replace(match: re.Match) -> str:
        groups = match.groups()
        if groups[0] is not None or groups[1] is not None:
            return match.group(0)
        if groups[2] is not None:
            counts['display_delimiters'] += 1
            return '\n\n$$\n' + groups[2].strip() + '\n$$\n\n'
        latex = groups[3].strip()
        counts['inline_delimiters'] += 1
        if '\n' in latex:
            counts['multiline_inline_promoted'] += 1
            return '\n\n$$\n' + latex + '\n$$\n\n'
        return '$' + latex + '$'
    text = MATH.sub(replace, text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    # A period following a promoted display should not become a paragraph.
    text = re.sub(r'(\$\$\n)\n\.\s*\n', r'\1\n', text)
    return text


if __name__ == '__main__':
    BACKUP.mkdir(parents=True, exist_ok=True)
    sources = sorted((OUT / 'parts').glob('Part_*.md'))
    for source in sources + [OUT / name for name in ['build_readable_notes.py', 'verify_reader.py',
                                                    'validate_math.cjs', 'MFOCS_Notes_Readable.md',
                                                    'Readable_notes.html', 'Page_index.md']]:
        target = BACKUP / source.relative_to(OUT)
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            shutil.copy2(source, target)
    report = {'files': [], 'restored_math': []}
    for source in sources:
        text = source.read_text(encoding='utf-8')
        counts = {'file': source.name, 'inline_delimiters': 0,
                  'display_delimiters': 0, 'multiline_inline_promoted': 0}
        if source.name.startswith('Part_03'):
            text = restore_refresher(text, report['restored_math'])
        repaired = canonicalise(text, counts)
        source.write_text(repaired, encoding='utf-8')
        report['files'].append(counts)
    path = OUT / 'reference/math_source_repairs.json'
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'restored_expressions': len(report['restored_math']), 'files': report['files']}, indent=2))
