from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'index.html'
STYLES = ROOT / 'src' / 'styles.css'


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stylesheets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.stylesheets.append(attrs.get('href'))


html = INDEX.read_text(encoding='utf-8')
parser = LinkParser()
parser.feed(html)

assert '/src/styles.css' in parser.stylesheets, 'index.html must load the Open Props stylesheet'
css = STYLES.read_text(encoding='utf-8')
for import_url in (
    'https://unpkg.com/open-props',
    'https://unpkg.com/open-props/normalize.min.css',
    'https://unpkg.com/open-props/buttons.min.css',
):
    assert import_url in css, f'missing Open Props import: {import_url}'

for token in ('var(--radius-4)', 'var(--shadow-4)', 'var(--gradient-9)', 'var(--indigo-6)'):
    assert token in css, f'missing Open Props token example: {token}'

print('Static Open Props configuration checks passed.')
