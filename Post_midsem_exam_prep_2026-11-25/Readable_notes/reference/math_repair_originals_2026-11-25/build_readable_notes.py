"""Assemble the visually transcribed notes and a local, offline math reader."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from pathlib import Path

import markdown

OUT = Path(__file__).resolve().parent
PAGE = re.compile(r'<a id="pdf-page-(\d{3})"></a>\s*\n## PDF page \1\s*[—–-]\s*([^\n]+)\n')
MATH = re.compile(r'\$\$(.*?)\$\$|(?<!\\)\$(?!\$)([^\n$]*?)(?<!\\)\$|\\\[(.*?)\\\]|\\\((.*?)\\\)', re.S)


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            value.update(chunk)
    return value.hexdigest()


def collect() -> list[dict]:
    result = []
    for part in sorted((OUT / 'parts').glob('Part_*.md')):
        source = part.read_text(encoding='utf-8')
        matches = list(PAGE.finditer(source))
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(source)
            body = source[match.end():end].strip()
            reference = next((line.strip() for line in body.splitlines()
                              if re.search(r'textbook.*(?:reference|§|chapter|Ch\.)', line, re.I)), '')
            qualifiers = [line.strip() for line in body.splitlines()
                          if re.search(r'unclear in source|source (?:qualification|correction|issue|error)|textbook clarification|unfinished|incomplete', line, re.I)]
            result.append({'pdf_page': int(match.group(1)), 'title': match.group(2).strip(),
                           'body': body, 'part': part.name, 'textbook_reference': reference,
                           'qualifications': qualifiers})
    return sorted(result, key=lambda item: item['pdf_page'])


def math_html(source: str, expressions: list[dict], page: int) -> str:
    replacements = {}

    def stash(match: re.Match) -> str:
        groups = match.groups()
        display = groups[0] is not None or groups[2] is not None
        latex = next(value for value in groups if value is not None).strip()
        index = len(expressions)
        expressions.append({'pdf_page': page, 'latex': latex, 'display': display})
        tag = 'div' if display else 'span'
        slot = f'<{tag} id="math-slot-{index}"></{tag}>'
        replacements[slot] = (f'<{tag} class="math-source" data-display="{str(display).lower()}">'
                              f'{html.escape(latex)}</{tag}>')
        return '\n\n' + slot + '\n\n' if display else slot

    protected = MATH.sub(stash, source)
    rendered = markdown.markdown(protected, extensions=['extra', 'sane_lists'])
    for slot, replacement in replacements.items():
        rendered = rendered.replace(slot, replacement)
    return rendered


CSS = """
:root{font-family:system-ui,-apple-system,Segoe UI,sans-serif;color:#18212b;background:#f5f7fa;font-size:17px}
*{box-sizing:border-box}body{margin:0}header{background:#163147;color:white;padding:24px 30px}
header h1{font-size:1.5rem;margin:0 0 8px}header p{margin:0;color:#dce7ef}a{color:#176289}
.layout{display:grid;grid-template-columns:300px minmax(0,1fr);max-width:1600px;margin:auto}
aside{position:sticky;top:0;height:100vh;overflow:auto;padding:20px;border-right:1px solid #d8e0e8;background:white}
aside input{width:100%;padding:10px;margin:4px 0 12px;border:1px solid #bccbd6;border-radius:6px;font:inherit}
aside label{font-size:.85rem;font-weight:600}nav a{display:block;padding:8px 4px;font-size:.86rem;text-decoration:none;border-bottom:1px solid #edf1f5}
nav a:hover{background:#edf5fa}.tools{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:14px}
button{padding:8px 10px;background:#e8f0f5;border:1px solid #b5c9d8;border-radius:5px;color:#183d56;cursor:pointer}
button.active{background:#163147;color:white}.count{font-size:.8rem;color:#546b7d;margin:8px 0 16px}
main{min-width:0;padding:24px 35px}.intro{background:#eaf3f9;padding:18px;border-radius:8px;margin-bottom:24px}
article{background:white;padding:28px 32px;margin:0 0 24px;border:1px solid #dce4eb;border-radius:8px;scroll-margin-top:14px}
article h2{font-size:1.22rem;margin-top:0;color:#173d58}.source{font-size:.84rem;margin-bottom:20px;color:#60798d}
p,li{line-height:1.65}li{margin:5px 0}table{border-collapse:collapse;width:100%;font-size:.92rem;display:block;overflow:auto}
th,td{border:1px solid #d7e0e8;padding:9px 12px;text-align:left}th{background:#edf3f7}
blockquote{border-left:4px solid #8eb4cd;margin-left:0;padding-left:18px;color:#415767}
pre{white-space:pre-wrap;background:#f1f5f8;padding:14px;border-radius:4px;overflow:auto}
.math-source[data-display=true],.katex-display{overflow-x:auto;overflow-y:hidden;padding:5px 0}
.katex{font-size:1.05em}.math-error{color:#a12727;white-space:pre-wrap}.hidden{display:none!important}
.footer{font-size:.85rem;color:#546b7d;padding:12px 0 24px}
@media(max-width:900px){.layout{grid-template-columns:1fr}aside{position:relative;height:auto;border-right:0;border-bottom:1px solid #d8e0e8}nav{max-height:220px}main{padding:15px}article{padding:20px}header{padding:20px}}
@media print{aside,header,.intro,.footer{display:none}.layout{display:block}main{padding:0}article{border:0;padding:0;margin-bottom:30px;break-before:page}.hidden{display:block!important}.source{font-size:10pt}body{background:white;font-size:11pt}.katex-display{overflow:visible}a{color:inherit}}
"""

SCRIPT = """
document.querySelectorAll('.math-source').forEach(el=>{
 const latex=el.textContent;
 try{katex.render(latex,el,{displayMode:el.dataset.display==='true',throwOnError:true,strict:'ignore',trust:false})}
 catch(e){el.classList.add('math-error');el.title=e.message;el.textContent=latex}
});
const pages=[...document.querySelectorAll('article[data-page]')], links=[...document.querySelectorAll('nav a')];
let minimum=1;
function filter(){const q=document.getElementById('search').value.trim().toLowerCase();let shown=0;
 pages.forEach((page,i)=>{const keep=Number(page.dataset.page)>=minimum&&(!q||page.textContent.toLowerCase().includes(q));
 page.classList.toggle('hidden',!keep);links[i].classList.toggle('hidden',!keep);if(keep)shown++});
 document.getElementById('count').textContent=shown+' of '+pages.length+' transcribed pages shown';}
document.getElementById('search').addEventListener('input',filter);
document.getElementById('all').onclick=()=>{minimum=1;document.getElementById('all').classList.add('active');document.getElementById('late').classList.remove('active');filter()};
document.getElementById('late').onclick=()=>{minimum=161;document.getElementById('late').classList.add('active');document.getElementById('all').classList.remove('active');filter()};
document.getElementById('jump').addEventListener('change',event=>{const n=Number(event.target.value);const target=document.getElementById('pdf-page-'+String(n).padStart(3,'0'));
 if(target){minimum=1;document.getElementById('search').value='';filter();target.scrollIntoView();location.hash=target.id}});
filter();
"""


def build(allow_partial: bool) -> None:
    pages = collect()
    numbers = [entry['pdf_page'] for entry in pages]
    missing = sorted(set(range(1, 222)) - set(numbers))
    duplicate = sorted({n for n in numbers if numbers.count(n) > 1})
    if duplicate or (missing and not allow_partial):
        raise SystemExit(f'Cannot assemble complete notes: missing={missing}, duplicate={duplicate}')
    complete = not missing
    status = 'All 221 PDF pages transcribed' if complete else f'Working draft: {len(pages)} of 221 PDF pages transcribed'
    heading = ('# CS208 MFOCS — Readable handwritten notes\n\n'
               f'**Coverage:** {status}.\n\n'
               'Sources: [handwritten notes PDF](../../Study_material_after_mid_sems/MFOCS_Notes_Aug-Nov_2026.pdf) '
               'and [Lehman–Leighton–Meyer textbook](../../Study_material_after_mid_sems/MCS_Textbook_Lehman_Leighton_Meyer.pdf).\n\n'
               'Use [the browser reader](Readable_notes.html) for rendered formulas and page search, '
               'or [the page index](Page_index.md) for navigation. PDF page numbers refer to the notes. '
               'Textbook PDF page number equals printed Arabic page number plus 8.\n\n'
               'This is a visual transcription into readable prose and LaTeX. Definitions, examples, proof steps '
               'and meaningful diagram information are retained. Unfinished source exercises remain unfinished. '
               'Unclear handwriting and source qualifications are identified in place. Explicit textbook clarifications '
               'are distinguished from the handwritten content. Administrative annotations are retained without guessing their meaning.\n\n')
    blocks = []
    articles = []
    nav = []
    expressions = []
    index_rows = []
    for entry in pages:
        n = entry['pdf_page']
        title = entry['title']
        anchor = f'pdf-page-{n:03}'
        scan = f'source_pages/page_{n:03}.png'
        blocks.append(f'<a id="{anchor}"></a>\n## PDF page {n:03} — {title}\n\n'
                      f'[Original scan]({scan})\n\n{entry["body"]}')
        rendered = math_html(entry['body'], expressions, n)
        articles.append(f'<article id="{anchor}" data-page="{n}"><h2>PDF page {n:03} — {html.escape(title)}</h2>'
                        f'<div class="source"><a href="{scan}">Original scanned page</a> · '
                        '<a href="../../Study_material_after_mid_sems/MCS_Textbook_Lehman_Leighton_Meyer.pdf">Textbook PDF</a></div>'
                        f'{rendered}</article>')
        nav.append(f'<a href="#{anchor}">{n:03} · {html.escape(title)}</a>')
        ref = entry['textbook_reference'].replace('|', '\\|').replace('**', '')
        ref = ref.replace('](#pdf-page-', '](MFOCS_Notes_Readable.md#pdf-page-')
        index_rows.append(f'| [{n:03}](MFOCS_Notes_Readable.md#{anchor}) | {title.replace("|", "/")} | {ref} |')
    (OUT / 'MFOCS_Notes_Readable.md').write_text(heading + '\n\n'.join(blocks) + '\n', encoding='utf-8')
    (OUT / 'Page_index.md').write_text('# Notes page index\n\n'
        '[Open the browser reader](Readable_notes.html) or [the full Markdown notes](MFOCS_Notes_Readable.md).\n\n'
        '| Notes PDF page | Topic | Textbook reference / qualification |\n|---|---|---|\n'
        + '\n'.join(index_rows) + '\n', encoding='utf-8')
    reader = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
              '<title>CS208 — Readable notes</title><link rel="stylesheet" href="vendor/katex/katex.min.css">'
              f'<style>{CSS}</style></head><body><header><h1>CS208 — Readable handwritten notes</h1><p>{status}</p></header>'
              '<div class="layout"><aside><label for="search">Search the transcribed pages</label><input id="search" type="search" placeholder="e.g. induction, bijection, Fibonacci">'
              '<div class="tools"><button id="all" class="active">All pages</button><button id="late">Pages 161–221</button></div>'
              '<label for="jump">Jump to notes PDF page</label><input id="jump" type="number" min="1" max="221" placeholder="1–221">'
              '<div id="count" class="count"></div><nav>' + ''.join(nav) + '</nav></aside><main>'
              '<div class="intro"><strong>Readable transcription with textbook references.</strong><p>Original examples and proof steps are retained. '
              'Unclear handwriting and textbook clarifications are labelled in place. Textbook PDF pages are printed page + 8. '
              '<a href="MFOCS_Notes_Readable.md">Markdown version</a> · <a href="Page_index.md">Page index</a></p></div>'
              + ''.join(articles) + '<div class="footer">Source scans and references remain beside this reader. The math renderer and fonts are bundled locally; no network is needed to read these notes.</div>'
              '</main></div><script src="vendor/katex/katex.min.js"></script>' + f'<script>{SCRIPT}</script></body></html>')
    (OUT / 'Readable_notes.html').write_text(reader, encoding='utf-8')
    reference = OUT / 'reference'
    reference.mkdir(exist_ok=True)
    (reference / 'math_expressions.json').write_text(json.dumps(expressions, ensure_ascii=False, indent=2), encoding='utf-8')
    manifest = [{key: value for key, value in entry.items() if key != 'body'} for entry in pages]
    (reference / 'page_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    report = {'complete': complete, 'source_pages': 221, 'transcribed_pages': len(pages),
              'missing_pages': missing, 'duplicate_pages': duplicate, 'math_expressions': len(expressions),
              'pages_with_qualifications': [entry['pdf_page'] for entry in pages if entry['qualifications']]}
    (reference / 'coverage_report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    (OUT / 'README.md').write_text(
        '# Readable CS208 handwritten notes\n\n'
        f'**{status}.**\n\n'
        '- [Open the browser reader](Readable_notes.html): rendered mathematics, search, page navigation and a pages 161–221 filter. The reader works offline.\n'
        '- [Full Markdown transcription](MFOCS_Notes_Readable.md): searchable text with LaTeX formulas and the original PDF page numbers.\n'
        '- [Page index and textbook references](Page_index.md): jump to a topic or source page.\n\n'
        'The transcription retains definitions, examples, equations, proof steps, meaningful diagram information, unfinished exercises and administrative notes. '
        'Diagrams are explained in words when their layout is not essential; each page links to its original scan. '
        'The textbook is used to resolve notation and verify matching definitions/results. Added or restored reasoning is labelled **Textbook clarification**. '
        'Unclear handwriting and source issues remain explicitly marked. Topics without a matching section, including the convex-geometry material, are identified as course-specific.\n\n'
        'Textbook references use printed Arabic page numbers; add 8 to obtain the textbook PDF page number.\n\n'
        'For smaller files: [pages 001–075](parts/Part_01_pages_001-075.md), '
        '[076–150](parts/Part_02_pages_076-150.md), '
        '[151–205](parts/Part_03_pages_151-205.md), '
        '[206–221](parts/Part_04_pages_206-221.md).\n\n'
        'The `source_pages/` directory contains source renders, including overlapping crops for long scanned pages. '
        'The `reference/` directory contains the searchable textbook extract, page manifest and validation records. '
        'The source PDFs remain unchanged.\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--allow-partial', action='store_true')
    args = parser.parse_args()
    build(args.allow_partial)
