#!/usr/bin/env python3
"""Check the built site in _site/: in-page anchors and referenced assets."""
import glob
import os
import re
import sys

SITE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_site')


def main():
    if not os.path.isdir(SITE):
        sys.exit('error: _site/ not found, run `jekyll build` first')
    ok = True
    for path in sorted(glob.glob(os.path.join(SITE, '**', '*.html'), recursive=True)):
        with open(path, encoding='utf-8') as f:
            html = f.read()
        rel = os.path.relpath(path, SITE)
        ids = set(re.findall(r'id="([^"]+)"', html))
        for anchor in re.findall(r'href="#([^"]+)"', html):
            if anchor not in ids:
                print(f'{rel}: broken anchor #{anchor}')
                ok = False
        for src in re.findall(r'src="(/assets/[^"]+)"', html):
            if not os.path.exists(os.path.join(SITE, src.lstrip('/'))):
                print(f'{rel}: missing asset {src}')
                ok = False
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
