# AGENTS.md

Conventions for AI agents working in this repository.

## Environment

- Jekyll 4.x: `jekyll` is on PATH. Run plain `jekyll` — there is no Gemfile, never use `bundle exec`.
- `jekyll build` outputs to `./_site`; do not use `--destination` (fails in this environment).
- `node` is not available — use Python for HTML/JS sanity checks.

## Structure

- `index.html` — front page. Liquid pins the `apie` post first, the rest newest-first; keep that ordering.
- `_layouts/default.html` — picks `content-area-full` on the front page and `content-area` elsewhere (conditional on `page.url == '/'`); keep the conditional.
- `_posts/` — posts named `YYYY-MM-DD-<slug>.md` (the date prefix is required by Jekyll; URLs are `/<slug>/` thanks to the `collections.posts` block in `_config.yml` — do not remove it).
- `duk/`, `peritonine-dialize/`, `pacientu-patirtys/` — static pages (Markdown).
- `assets/css/style.css` — theme.
- `assets/images/<theme>/` — images grouped by theme (`logo/`, `apie/`, `duk/`, `peritonine-dialize/`, `patirtys/`, `misc/` = unused WP leftovers). Never reintroduce dated WP-style dirs (e.g. `2019/02/`).

## Build & local development

```console
jekyll build               # rebuild into ./_site
jekyll serve --port 8742   # dev server, auto-rebuilds on change
```

then open http://127.0.0.1:8742/ in a browser. To preview the last build without a watcher: `python3 -m http.server 8742 --directory _site` (a running static server picks up rebuilds — no restart needed).

## Content conventions

- Markdown (kramdown) is the default. Keep HTML islands only where Markdown cannot express the construct — currently just the YouTube `<iframe>` on the peritonine-dialize page.
- FAQ/TOC pattern (see `duk/index.md`): one `## Turinys` section at the top with a (nested) list of anchor links; each question is a `###` heading with an explicit kramdown anchor: `### Klausimas? {#AnchorId}`.
- Kramdown gotchas: `{#id}` works only on headings (not on paragraphs); ids must not start with a digit — `{#1}` is silently ignored, use `BPD1`, `PD1`, ... Every TOC link must point at an explicit heading id.
- Images: standard Markdown `![alt](/assets/images/<theme>/file)`. Floated image: `![alt](/path){: width="330" height="209" class="float-left"}` (styled by `.entry-content img.float-left`).
- Images should have alternative text where possible — a short description of the image, never an empty `alt=""`.
- Post front matter: `layout: post`, `title`, `date`, `slug`, `description`, `image` (root-relative `/assets/images/...`).
- Page front matter: `layout: page`, `title`, `permalink: /<slug>/`, `description`.

## Verifying changes

`jekyll build` must succeed, then:

1. **Anchors** — every in-page `href="#x"` must match an `id="x"` in the same built page:

   ```python
   import re, glob
   for f in glob.glob('_site/**/index.html', recursive=True):
       html = open(f).read()
       missing = [a for a in re.findall(r'href="#([^"]+)"', html)
                  if a not in set(re.findall(r'id="([^"]+)"', html))]
       if missing: print(f, 'BROKEN:', missing)
   ```

2. **Assets** — every referenced image must exist:

   ```python
   import re, glob, os
   for f in glob.glob('_site/**/*.html', recursive=True):
       for src in re.findall(r'src="(/assets/[^"]+)"', open(f).read()):
           if not os.path.exists('_site' + src): print(f, 'MISSING', src)
   ```

3. **Visible text** — when restructuring a page, compare visible text before/after (strip `<script>`/`<style>` and all tags, `html.unescape`, collapse whitespace); only intentional diffs are acceptable.

## Commits

Commit messages are LKML style: terse, imperative subject line (≤ 50 chars), no boilerplate.

## Pull requests

PRs must be created in draft state initially.
