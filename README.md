# peritonine.lt

Jekyll svetainė apie peritoninę dializę.

## Struktūra

- `index.html` — pagrindinis puslapis (kortelės; „Apie" visada pirmas)
- `_layouts/`, `_includes/` — šablonai (antraštė, meniu, poraštė)
- `_posts/` — įrašai: `KKKK-MM-DD-<slug>.md` (data tik vardinimui, URL yra `/<slug>/`)
- `duk/`, `peritonine-dialize/`, `pacientu-patirtys/` — puslapiai (Markdown)
- `assets/css/style.css` — tema
- `assets/images/<tema>/` — paveikslėliai pagal temas (`logo/`, `apie/`, `duk/`, `peritonine-dialize/`, `patirtys/`, `misc/`)
- `_config.yml` — konfigūracija (`collections.posts` blokas lemia `/<slug>/` URL — jo nešalinti)
- nauji su svetaine nesusiję failai — į `_config.yml` `exclude` sąrašą (kitaip atsidurs `_site/`)

## Statymas

```console
jekyll build
```

Rezultatas — `_site/` kataloge.

## Peržiūra naršyklėje

```console
jekyll serve --port 8742
```

ir atidaryti <http://127.0.0.1:8742/>.
