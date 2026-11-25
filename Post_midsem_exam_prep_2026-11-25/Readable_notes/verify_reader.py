"""Verify static formulas, uncaptured LaTeX, layout and reader controls."""
from pathlib import Path
import json, re

from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent
expected = len(json.loads((OUT / 'reference/math_expressions.json').read_text(encoding='utf-8')))
executables = [Path('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'),
               Path('C:/Program Files/Microsoft/Edge/Application/msedge.exe'),
               Path('C:/Program Files/Google/Chrome/Application/chrome.exe')]
executable = next(path for path in executables if path.is_file())

with sync_playwright() as playwright:
    context = playwright.chromium.launch_persistent_context(
        str(OUT / 'reference/browser_profile_math_repair'), executable_path=str(executable),
        headless=True, viewport={'width': 1440, 'height': 1000})
    context.set_offline(True)
    page = context.new_page()
    page.goto((OUT / 'Readable_notes.html').as_uri(), wait_until='load')
    page.evaluate('document.fonts.ready')
    report = page.evaluate('''() => ({
        articles: document.querySelectorAll('article[data-page]').length,
        rendered_math: document.querySelectorAll('.math-source .katex').length,
        math_errors: document.querySelectorAll('.math-error').length,
        title: document.querySelector('header p').textContent,
        external_scripts: document.querySelectorAll('script[src]').length,
        external_stylesheets: document.querySelectorAll('link[rel="stylesheet"]').length,
        loaded_math_fonts: [...new Set([...document.fonts].filter(font=>font.status==='loaded')
          .map(font=>font.family.replace(/["']/g,'')))],
        font_loading_errors: [...document.fonts].filter(font=>font.status==='error').map(font=>font.family)
    })''')
    leftovers = page.evaluate(r'''() => {
        const found = [], walker = document.createTreeWalker(document.querySelector('main'), NodeFilter.SHOW_TEXT);
        while(walker.nextNode()) {
            const node = walker.currentNode;
            if(node.parentElement.closest('.math-source,script,style')) continue;
            if(/\\[a-zA-Z]+|\\[()[\]]|\$/.test(node.textContent)) {
                found.push({page: node.parentElement.closest('article')?.dataset.page, text: node.textContent.trim()});
            }
        }
        return found;
    }''')
    report['unrendered_math_text'] = leftovers
    report['expected_math'] = expected
    report['desktop_formula_overflow'] = page.evaluate('''() => [...document.querySelectorAll('article .math-source[data-display=false]')]
        .filter(el=>el.getBoundingClientRect().right>el.closest('article').getBoundingClientRect().right)
        .map(el=>({page:el.closest('article').dataset.page,index:el.dataset.mathIndex}))''')
    page.locator('#late').click()
    report['late_filter_pages'] = page.locator('article:not(.hidden)').count()
    page.locator('#all').click()
    page.locator('#search').fill('Fibonacci')
    report['fibonacci_search_pages'] = page.locator('article:not(.hidden)').count()
    page.locator('#search').fill('')
    page.locator('#jump').fill('218')
    page.locator('#jump').press('Tab')
    report['jump_fragment'] = page.evaluate('location.hash')
    page.locator('#pdf-page-151').screenshot(path=str(OUT / 'reference/math_fixed_page_151.png'))
    page.locator('#pdf-page-205').screenshot(path=str(OUT / 'reference/math_fixed_page_205.png'))
    # The reader must show complete mathematics even when previewers block JavaScript.
    static_context = context.browser.new_context(java_script_enabled=False, offline=True,
                                                viewport={'width': 1440, 'height': 1000})
    static_page = static_context.new_page()
    static_page.goto((OUT / 'Readable_notes.html').as_uri(), wait_until='load')
    report['math_with_scripts_disabled'] = static_page.locator('.math-source .katex').count()
    report['articles_with_scripts_disabled'] = static_page.locator('article[data-page]').count()
    static_page.evaluate('document.fonts.ready')
    report['font_errors_with_scripts_disabled'] = static_page.evaluate(
        '() => [...document.fonts].filter(font=>font.status==="error").map(font=>font.family)')
    static_context.close()
    context.close()

(OUT / 'reference/reader_validation.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report, indent=2))
if (report['math_errors'] or report['articles'] != 221 or report['late_filter_pages'] != 61
        or report['jump_fragment'] != '#pdf-page-218' or report['unrendered_math_text']
        or report['rendered_math'] != expected or report['math_with_scripts_disabled'] != expected
        or report['desktop_formula_overflow'] or report['font_loading_errors']
        or report['font_errors_with_scripts_disabled']
        or not all(font in report['loaded_math_fonts'] for font in ['KaTeX_Main','KaTeX_Math','KaTeX_AMS'])):
    raise SystemExit('Reader validation failed')
