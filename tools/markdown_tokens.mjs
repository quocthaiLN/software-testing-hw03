// Read-only Markdown lexer for the PDF exporter. Uses bundled marked.
import {readFileSync} from 'node:fs';
import {marked} from 'marked';
if(process.argv.length!==3)throw Error('Usage: node markdown_tokens.mjs SOURCE.md');
process.stdout.write(JSON.stringify(marked.lexer(readFileSync(process.argv[2],'utf8'))));
