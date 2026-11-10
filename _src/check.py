# -*- coding: utf-8 -*-
"""Kontrollerer den ferdig bygde fellessiden.

    python3 _src/check.py

Sjekker at interne lenker og bilder finnes, at hver side har nøyaktig én h1, at
begge språkene viser de samme appene, at strukturerte data er gyldig JSON, og at
ingen mappe i rota kolliderer med et app-repo (svaagan.github.io/<repo>/), og at
Stian ikke nevnes ved navn.
"""
import json, os, re, sys, html.parser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apps import APPS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
problems = []

# Disse adressene eies av egne repoer på GitHub Pages og må ikke finnes her.
PROJECT_REPOS = {"pokerface", "taptime", "leyezer", "rullo", "runpace"}
SKIP_DIRS = {".git", "_src", "docs"}

pages = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    pages += [os.path.join(dirpath, f) for f in filenames if f.endswith(".html")]
pages.sort()


def exists(url):
    u = url.split("#")[0].split("?")[0]
    if not u.startswith("/") or u.startswith("//"):
        return True
    first = u.strip("/").split("/")[0]
    if first in PROJECT_REPOS:
        return True       # ligger i et annet repo; sjekkes etter publisering med curl
    p = os.path.join(ROOT, u.lstrip("/"))
    if u.endswith("/"):
        return os.path.isfile(os.path.join(p, "index.html"))
    return os.path.isfile(p) or os.path.isfile(os.path.join(p, "index.html"))


def resolve(page, url):
    """Gjør en relativ lenke om til en absolutt sti fra rota."""
    if re.match(r"^[a-z]+:", url) or url.startswith(("/", "#")):
        return url
    base = "/" + os.path.relpath(os.path.dirname(page), ROOT).replace(".", "") + "/"
    base = base.replace("//", "/")
    parts = []
    for seg in (base + url).split("/"):
        if seg == "..":
            parts and parts.pop()
        elif seg != ".":
            parts.append(seg)
    return "/".join(parts)


class Scan(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.refs = []
        self.ld = []
        self._in_ld = False
        self.ids = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        if tag in ("a", "link") and a.get("href"):
            if tag == "link" and a.get("rel") in ("canonical", "alternate"):
                pass
            else:
                self.refs.append(a["href"])
        if tag in ("img", "script") and a.get("src"):
            self.refs.append(a["src"])
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld = True
        if tag == "li" and "card" in (a.get("class") or ""):
            self.ids.append(a.get("id"))

    def handle_endtag(self, tag):
        if tag == "script":
            self._in_ld = False

    def handle_data(self, data):
        if self._in_ld:
            self.ld.append(data)


cards = {}
for page in pages:
    rel = os.path.relpath(page, ROOT)
    with open(page, encoding="utf-8") as f:
        text = f.read()
    s = Scan()
    s.feed(text)
    if s.h1 != 1:
        problems.append("%s: %d h1 (skal være 1)" % (rel, s.h1))
    for ref in s.refs:
        if ref.startswith(("mailto:", "http://", "https://", "#")):
            continue
        if not exists(resolve(page, ref)):
            problems.append("%s: lenken %s finnes ikke" % (rel, ref))
    for block in s.ld:
        try:
            json.loads(block)
        except ValueError as e:
            problems.append("%s: ugyldig JSON-LD (%s)" % (rel, e))
    if re.search(r"stian|gaare", text, re.I):
        problems.append("%s: nevner Stian ved navn (skal ikke stå på siden)" % rel)
    if "{{" in text:
        problems.append("%s: plassholder som ikke er byttet ut" % rel)
    if rel in ("index.html", os.path.join("en", "index.html")):
        cards[rel] = s.ids

expected = [a["slug"] for a in APPS]
for rel, ids in cards.items():
    if ids != expected:
        problems.append("%s: appene %s, ventet %s" % (rel, ids, expected))
if len(cards) != 2:
    problems.append("fant ikke begge forsidene")

for app in APPS:
    if not os.path.isfile(os.path.join(ROOT, "icons", app["slug"] + ".png")):
        problems.append("ikonet til %s mangler" % app["slug"])
    if app["status"] == "live" and not app.get("appstore_id"):
        problems.append("%s er ute, men mangler App Store-ID" % app["slug"])

for name in os.listdir(ROOT):
    if name in PROJECT_REPOS:
        problems.append("mappa /%s/ kolliderer med app-repoet med samme navn" % name)

for f in (".nojekyll", "og.png", "favicon.png", "404.html"):
    if not os.path.exists(os.path.join(ROOT, f)):
        problems.append("%s mangler" % f)

print("Kontrollerte %d sider." % len(pages))
if problems:
    print("\n".join("  – " + p for p in problems))
    sys.exit(1)
print("Ingen problemer funnet.")
