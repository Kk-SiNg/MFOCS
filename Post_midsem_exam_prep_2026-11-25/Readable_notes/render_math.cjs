// Render mathematical expressions at build time, including when reader JS is disabled.
const fs = require('fs');
const katex = require('./vendor/katex/katex.min.js');
const expressions = JSON.parse(fs.readFileSync(0, 'utf8'));
const cache = new Map();
const errors = [];
const rendered = expressions.map((expression, index) => {
  const key = JSON.stringify([expression.display, expression.latex]);
  if (cache.has(key)) return cache.get(key);
  try {
    const result = katex.renderToString(expression.latex, {
      displayMode: expression.display, throwOnError: true, strict: 'ignore', trust: false,
      output: 'htmlAndMathml'
    });
    cache.set(key, result);
    return result;
  } catch (error) {
    errors.push({index, pdf_page: expression.pdf_page, latex: expression.latex, error: String(error)});
    return null;
  }
});
process.stdout.write(JSON.stringify({rendered, errors}));
if (errors.length) process.exitCode = 1;
