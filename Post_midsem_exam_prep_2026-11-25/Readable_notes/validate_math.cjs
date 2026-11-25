const fs = require('fs');
const path = require('path');
const katex = require('./vendor/katex/katex.min.js');
const expressions = JSON.parse(fs.readFileSync(path.join(__dirname, 'reference/math_expressions.json'), 'utf8'));
const errors = [];
for (const [index, expression] of expressions.entries()) {
  try {
    katex.renderToString(expression.latex, {displayMode: expression.display, throwOnError: true, strict: 'ignore', trust: false});
  } catch (error) {
    errors.push({index, pdf_page: expression.pdf_page, latex: expression.latex, error: String(error)});
  }
}
const report = {checked: expressions.length, errors};
fs.writeFileSync(path.join(__dirname, 'reference/math_validation.json'), JSON.stringify(report, null, 2));
process.stdout.write(JSON.stringify({checked: expressions.length, error_count: errors.length, errors: errors.slice(0, 20)}, null, 2) + '\n');
if (errors.length) process.exitCode = 1;
