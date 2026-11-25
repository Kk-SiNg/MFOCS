"""Check the reader's local math rendering and page/search controls in Edge."""
from pathlib import Path
import json

from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent
executables = [Path('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'),
               Path('C:/Program Files/Microsoft/Edge/Application/msedge.exe'),
               Path('C:/Program Files/Google/Chrome/Application/chrome.exe')]
executable = next(path for path in executables if path.is_file())

with sync_playwright() as playwright:
    context = playwright.chromium.launch_persistent_context(
        str(OUT / 'reference/browser_profile'), executable_path=str(executable),
        headless=True, viewport={'width': 1440, 'height': 1000})
    context.set_offline(True)
    page = context.new_page()
    page.goto((OUT / 'Readable_notes.html').as_uri(), wait_until='load')
    page.wait_for_function('typeof katex !== "undefined"')
    report = page.evaluate('''() => ({
        articles: document.querySelectorAll('article[data-page]').length,
        rendered_math: document.querySelectorAll('.math-source .katex').length,
        math_errors: document.querySelectorAll('.math-error').length,
        title: document.querySelector('header p').textContent,
        local_renderer: document.querySelector('script[src]').getAttribute('src')
    })''')
    page.screenshot(path=str(OUT / 'reference/reader_preview.png'))
    page.locator('#late').click()
    report['late_filter_pages'] = page.locator('article:not(.hidden)').count()
    page.locator('#all').click()
    page.locator('#search').fill('Fibonacci')
    report['fibonacci_search_pages'] = page.locator('article:not(.hidden)').count()
    page.locator('#search').fill('')
    page.locator('#jump').fill('218')
    page.locator('#jump').press('Tab')
    report['jump_fragment'] = page.evaluate('location.hash')
    context.close()

(OUT / 'reference/reader_validation.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report, indent=2))
if report['math_errors'] or report['articles'] != 221 or report['late_filter_pages'] != 61 or report['jump_fragment'] != '#pdf-page-218':
    raise SystemExit('Reader validation failed')
