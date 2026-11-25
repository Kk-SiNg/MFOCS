// Pre-render all .math-source blocks in a Final_rev HTML sheet using local KaTeX
// and verify zero unrendered math tags and valid relative links.
const fs = require('fs');
const path = require('path');

const targetArg = process.argv[2];
if (!targetArg || targetArg === '--help' || targetArg === '-h') {
  console.log('Usage: node prerender_katex.cjs <path-to-html>');
  process.exit(targetArg ? 0 : 1);
}

const htmlPath = path.resolve(targetArg);
const katexPath = path.resolve(
  path.dirname(htmlPath),
  '../Post_midsem_exam_prep_2026-11-25/Readable_notes/vendor/katex/katex.min.js'
);
const cssPath = path.resolve(
  path.dirname(htmlPath),
  '../Post_midsem_exam_prep_2026-11-25/Readable_notes/vendor/katex/katex.min.css'
);

const katex = require(katexPath);
let html = fs.readFileSync(htmlPath, 'utf8');
let count = 0;

const unescapeHtml = (s) =>
  s.replace(/&gt;/g, '>').replace(/&lt;/g, '<').replace(/&amp;/g, '&');

html = html.replace(
  /<(span|div) class="math-source" data-display="(true|false)">([\s\S]*?)<\/\1>/g,
  (_match, _tag, disp, raw) => {
    count++;
    const latex = unescapeHtml(raw.trim());
    return katex.renderToString(latex, {
      displayMode: disp === 'true',
      throwOnError: true,
      strict: 'ignore',
      trust: false,
      output: 'htmlAndMathml',
    });
  }
);

fs.writeFileSync(htmlPath, html, 'utf8');

const dir = path.dirname(htmlPath);
const hrefs = [...html.matchAll(/href="([^"#]+)(?:#[^"]*)?"/g)].map((m) => m[1]);
const brokenLinks = hrefs.filter((h) => !fs.existsSync(path.resolve(dir, h)));
const leftover = (html.match(/class="math-source"/g) || []).length;

console.log(
  JSON.stringify({
    file: htmlPath,
    rendered_expressions: count,
    leftover_math_source: leftover,
    css_exists: fs.existsSync(cssPath),
    broken_links: brokenLinks,
    bytes: fs.statSync(htmlPath).size,
  })
);

if (leftover > 0 || !fs.existsSync(cssPath) || brokenLinks.length > 0) {
  process.exitCode = 1;
}
