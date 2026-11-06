# -*- coding: utf-8 -*-
"""Bygger fellessiden med alle appene.

    python3 _src/build.py

Leser studioet og applista fra _src/apps.py og skriver ferdige, statiske HTML-filer.
GitHub Pages serverer rå filer; det finnes ikke noe byggsteg ved publisering.

Rediger ALDRI de genererte HTML-filene direkte; endringene blir overskrevet.
Tekst om appene står i _src/apps.py, tekst på sidene her, og utseendet i assets/site.css.
"""
import datetime, hashlib, html, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apps import SITE, STUDIO, APPS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_src")
YEAR = datetime.date.today().year
NAME = STUDIO["name"]
E = html.escape


# Ressursene merkes med innholdssummen sin. GitHub Pages setter max-age=600, så uten
# dette ser besøkende gammel CSS i inntil ti minutter etter en endring.
def asset(path):
    try:
        with open(os.path.join(ROOT, path.lstrip("/")), "rb") as f:
            return "%s?v=%s" % (path, hashlib.sha1(f.read()).hexdigest()[:8])
    except IOError:
        return path


def appstore_url(app, lang):
    country = "no" if lang == "nb" else "us"
    return "https://apps.apple.com/%s/app/id%s" % (country, app["appstore_id"])


def app_page(app, lang):
    """Lenken til appens egen side på riktig språk, eller None."""
    if lang == "en" and app.get("page_en"):
        return app["page_en"]
    return app.get("page")


# ── Tekster ─────────────────────────────────────────────────────────
T = {
    "nb": {
        "title": "%s – alle appene" % NAME,
        "description": ("Alle appene fra %s: RunPace, Pokerface, TapTime og flere som "
                        "kommer." % NAME),
        "skip": "Hopp til appene",
        "h1": "Alle appene fra %s" % NAME,
        "lead": "Trykk på en app for å lese mer om den.",
        "live_h": "I App Store",
        "soon_h": "Kommer snart",
        "soon_badge": "Kommer snart",
        "store_link": "Last ned i App Store",
        "about_h": "Kontakt",
        "contact": "Spørsmål, ros eller ris? Skriv til",
        "all_appstore": "Alle appene i App Store",
        "privacy_note": "Denne siden bruker ingen informasjonskapsler og samler ikke inn noe om deg.",
        "other_lang": ("English", "en", "/en/"),
        "home": "Til forsiden",
        "nf_title": "Fant ikke siden",
        "nf_text": "Adressen finnes ikke. Kanskje appen du lette etter, står på forsiden?",
    },
    "en": {
        "title": "%s – all the apps" % NAME,
        "description": ("All the apps from %s: RunPace, Pokerface, TapTime and more on "
                        "the way." % NAME),
        "skip": "Skip to the apps",
        "h1": "All the apps from %s" % NAME,
        "lead": "Tap an app to read more about it.",
        "live_h": "On the App Store",
        "soon_h": "Coming soon",
        "soon_badge": "Coming soon",
        "store_link": "Download on the App Store",
        "about_h": "Contact",
        "contact": "Questions or feedback? Write to",
        "all_appstore": "All the apps on the App Store",
        "privacy_note": "This page uses no cookies and collects nothing about you.",
        "other_lang": ("Norsk", "nb", "/"),
        "home": "Back to the front page",
        "nf_title": "Page not found",
        "nf_text": "That address doesn’t exist. Maybe the app you were looking for is on the front page?",
    },
}
HOME = {"nb": "/", "en": "/en/"}


# ── Ramme ───────────────────────────────────────────────────────────
def head(lang, title, description, path, alternates=True, schema=None, noindex=False):
    url = SITE + path
    L = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>%s</title>" % E(title),
        '<meta name="description" content="%s">' % E(description),
        '<meta name="color-scheme" content="light">',
        '<meta name="theme-color" content="#f5f5f7">',
    ]
    if noindex:
        L.append('<meta name="robots" content="noindex">')
    else:
        L.append('<link rel="canonical" href="%s">' % url)
    if alternates:
        L += ['<link rel="alternate" hreflang="nb" href="%s/">' % SITE,
              '<link rel="alternate" hreflang="en" href="%s/en/">' % SITE,
              '<link rel="alternate" hreflang="x-default" href="%s/en/">' % SITE]
    L += [
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="%s">' % E(NAME),
        '<meta property="og:title" content="%s">' % E(title),
        '<meta property="og:description" content="%s">' % E(description),
        '<meta property="og:url" content="%s">' % url,
        '<meta property="og:locale" content="%s">' % ("nb_NO" if lang == "nb" else "en_US"),
        '<meta property="og:image" content="%s/og.png">' % SITE,
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<link rel="icon" href="/favicon.png">',
        '<link rel="apple-touch-icon" href="/favicon.png">',
        '<link rel="stylesheet" href="%s">' % asset("/assets/site.css"),
    ]
    if schema:
        L.append('<script type="application/ld+json">%s</script>'
                 % json.dumps(schema, ensure_ascii=False, separators=(",", ":")))
    return "\n".join(L)


# Merket: fire avrundede ruter i fargene fra appikonene, én «app» i hver.
MARK = ('<svg viewBox="0 0 26 26" aria-hidden="true">'
        '<rect x="0" y="0" width="12" height="12" rx="3.2" fill="#F6C915"/>'
        '<rect x="14" y="0" width="12" height="12" rx="3.2" fill="#E0263A"/>'
        '<rect x="0" y="14" width="12" height="12" rx="3.2" fill="#C2491D"/>'
        '<rect x="14" y="14" width="12" height="12" rx="3.2" fill="#C8F03C"/></svg>')


def wordmark(lang):
    return '<a class="wordmark" href="%s">%s<span>%s</span></a>' % (HOME[lang], MARK, E(NAME))


def footer(lang, lang_href=None):
    t = T[lang]
    label, code, default_href = t["other_lang"]
    return f'''<footer class="site-footer">
  <div class="wrap">
    <p class="footer-main"><span>© {YEAR} {E(NAME)}</span>
      <a href="mailto:{STUDIO["email"]}">{STUDIO["email"]}</a>
      <a href="{STUDIO["appstore_developer"]}">{t["all_appstore"]}</a>
      <a href="{lang_href or default_href}" hreflang="{code}" lang="{code}">{label}</a></p>
    <p class="footer-note">{t["privacy_note"]}</p>
  </div>
</footer>'''


def document(lang, head_html, body, lang_href=None, narrow=False):
    return f'''<!doctype html>
<html lang="{lang}">
<head>
{head_html}
</head>
<body>
<a class="skip" href="#apper">{T[lang]["skip"]}</a>
<header class="site-header"><div class="wrap{" narrow" if narrow else ""}">{wordmark(lang)}</div></header>
{body}
{footer(lang, lang_href)}
</body>
</html>
'''


# ── Kortene ─────────────────────────────────────────────────────────
def icon(app, size):
    return ('<img class="icon" src="%s" width="%d" height="%d" alt="" loading="lazy" decoding="async">'
            % (asset("/icons/%s.png" % app["slug"]), size, size))


def card(app, lang):
    """Ett kort. Hele kortet er klikkbart via navnelenken (strukket over kortet med CSS),
    og App Store-lenken ligger over den. Apple vil ha ett App Store-merke per side,
    så oversikten bruker tekstlenker; merket hører hjemme på appens egen side."""
    t = T[lang]
    live = app["status"] == "live"
    page = app_page(app, lang) or (appstore_url(app, lang) if live else None)
    name = E(app["name"])
    title = ('<a class="stretch" href="%s">%s</a>' % (page, name)) if page else name
    meta = [app["kind"][lang], app["devices"][lang]]
    if live and app.get("price"):
        meta.append(app["price"][lang])
    if live:
        foot = ('<p class="actions"><a class="store" href="%s">%s</a></p>'
                % (appstore_url(app, lang), t["store_link"]))
        pill = ""
    else:
        foot = ""
        pill = ' <span class="pill">%s</span>' % t["soon_badge"]
    size = 88 if live else 64
    return f'''      <li class="card{"" if live else " soon"}" id="{app["slug"]}">
        {icon(app, size)}
        <div class="card-body">
          <h3>{title}{pill}</h3>
          <p class="meta">{" · ".join(E(m) for m in meta)}</p>
          <p class="tagline">{E(app["tagline"][lang])}</p>
          {foot}
        </div>
      </li>'''


def schema_home(lang):
    live = [a for a in APPS if a["status"] == "live"]
    org = {"@type": "Organization", "@id": SITE + "/#studio", "name": NAME,
           "url": SITE + "/", "email": STUDIO["email"]}
    items = []
    for i, a in enumerate(live, 1):
        page = app_page(a, lang) or appstore_url(a, lang)
        is_game = a["kind"]["en"].lower().endswith("game")
        items.append({"@type": "ListItem", "position": i, "item": {
            "@type": (["VideoGame", "MobileApplication"] if is_game
                      else "MobileApplication"),
            "name": a["name"], "operatingSystem": "iOS",
            "applicationCategory": "GameApplication" if is_game else a.get("category", "UtilitiesApplication"),
            "description": a["tagline"][lang],
            "url": page if page.startswith("http") else SITE + page,
            "installUrl": appstore_url(a, lang),
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "NOK"},
            "publisher": {"@id": SITE + "/#studio"},
        }})
    return {"@context": "https://schema.org", "@graph": [
        org,
        {"@type": "WebSite", "url": SITE + "/", "name": NAME, "inLanguage": lang,
         "publisher": {"@id": SITE + "/#studio"}},
        {"@type": "ItemList", "name": T[lang]["live_h"], "itemListElement": items},
    ]}


def home(lang):
    t = T[lang]
    live = "\n".join(card(a, lang) for a in APPS if a["status"] == "live")
    soon = "\n".join(card(a, lang) for a in APPS if a["status"] == "soon")
    body = f'''<main>
  <section class="hero wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
  </section>
  <section class="wrap" id="apper" aria-labelledby="live-h">
    <h2 id="live-h">{t["live_h"]}</h2>
    <ul class="grid live" role="list">
{live}
    </ul>
  </section>
  <section class="wrap" aria-labelledby="soon-h">
    <h2 id="soon-h">{t["soon_h"]}</h2>
    <ul class="grid soon-grid" role="list">
{soon}
    </ul>
  </section>
  <section class="wrap about" aria-labelledby="about-h">
    <h2 id="about-h">{t["about_h"]}</h2>
    <p>{t["contact"]} <a href="mailto:{STUDIO["email"]}">{STUDIO["email"]}</a>.</p>
  </section>
</main>'''
    path = HOME[lang]
    return document(lang, head(lang, t["title"], t["description"], path,
                               schema=schema_home(lang)), body)


def not_found():
    # 404 serveres for alle språk; den er på norsk med engelsk under.
    nb, en = T["nb"], T["en"]
    body = f'''<main class="wrap narrow">
  <h1>{nb["nf_title"]}</h1>
  <p>{nb["nf_text"]}</p>
  <p><a class="button" href="/">{nb["home"]}</a></p>
  <p lang="en" class="muted">{en["nf_text"]} <a href="/en/">{en["home"]}</a></p>
</main>'''
    return document("nb", head("nb", "%s – %s" % (nb["nf_title"], NAME), nb["nf_text"],
                               "/404.html", alternates=False, noindex=True), body, narrow=True)


# ── Undersider for apper som ligger på fellessiden ─────────────────
# Pengeblokka har ingen nettside fra før. Den får forside og hjelp her, og
# personvernerklæringen er en ferdig side fra appens repo (_src/body/).
def pengeblokka_pages():
    import pengeblokka as P
    out = {}
    app = next(a for a in APPS if a["slug"] == "pengeblokka")
    for key, (path, title, description, body) in P.pages(app, icon, E).items():
        h = head("nb", title, description, path, alternates=False)
        out[path] = document("nb", h, body, lang_href="/en/#pengeblokka", narrow=True)
    with open(os.path.join(SRC, "body", "pengeblokka-personvern.html"), encoding="utf-8") as f:
        out["/pengeblokka/personvern/"] = f.read().replace("{{STUDIO}}", E(NAME))
    return out


def write(path, text):
    rel = path.lstrip("/")
    if rel == "" or rel.endswith("/"):
        rel += "index.html"
    full = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)
    return rel


def main():
    written = []
    for lang in ("nb", "en"):
        written.append(write(HOME[lang], home(lang)))
    written.append(write("/404.html", not_found()))
    for path, text in pengeblokka_pages().items():
        written.append(write(path, text))
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    for w in written:
        print("skrev", w)


if __name__ == "__main__":
    main()
