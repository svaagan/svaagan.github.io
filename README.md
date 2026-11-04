# Fellessiden – alle appene på ett sted

Porteføljesiden til studioet (arbeidsnavn **App Factory**), servert av GitHub Pages fra
repoet `svaagan/svaagan.github.io` på https://svaagan.github.io/. Statiske filer, ingen byggsteg
ved publisering.

## Slik henger det sammen

- Dette er GitHub-«brukersiden». Appsidene i egne repoer (`svaagan/pokerface`, `svaagan/taptime`,
  `svaagan/leyezer`) ligger automatisk under den, på `/pokerface/`, `/taptime/` og `/leyezer/`.
  Ingen mappe her kan derfor hete det samme som et app-repo; `check.py` passer på det.
- runpace.no og knipspics.no har egne domener og vises bare som kort.
- Pengeblokka har ingen egen nettside, så sidene ligger her: `/pengeblokka/`, `support/` og
  `personvern/`.
- Når studiodomenet kommer, legges `CNAME` her. Da flytter GitHub både fellessiden og
  appsidene i de andre repoene til domenet, og de gamle github.io-adressene sender videre.

## Filer

- `_src/apps.py` – studioet (navn, person, e-post) og applista. **Studionavnet står bare her.**
- `_src/build.py` – lager forsidene (`/`, `/en/`), `404.html` og Pengeblokka-sidene.
- `_src/pengeblokka.py` – tekstene til Pengeblokka-sidene.
- `_src/body/pengeblokka-personvern.html` – personvernerklæringen, kopiert fra appens repo.
- `_src/check.py` – lenker, bilder, én h1 per side, like apper på begge språk, gyldig JSON-LD.
- `_src/make_images.py` – delebildet `og.png` og `favicon.png`. Kjøres når navnet eller applista endres.
- `assets/site.css` – utseendet. `icons/` – appikonene i 256 px, hentet fra appenes asset-kataloger.

Rediger aldri HTML-filene direkte; de overskrives.

```sh
python3 _src/build.py && python3 _src/check.py
```

## Ny app

1. Lag appens nettside i `web/` i appmappa, som et eget repo med appens navn (mønsteret i Pokerface).
2. Legg ikonet i `icons/<slug>.png` (256 px) og én oppføring i `APPS` i `_src/apps.py`.
3. Kjør `make_images.py`, `build.py` og `check.py`, commit og push.

Når en app kommer i App Store: sett `status` til `"live"`, fyll inn `appstore_id` og `price`.

## Valg

Kortene, merket og strukturerte data følger undersøkelsen i `docs/KUNNSKAPSGRUNNLAG.md`.
