# -*- coding: utf-8 -*-
"""Alt fellessiden vet om studioet og appene.

Studionavnet står bare her. Når det endelige navnet og domenet er bestemt, endres
STUDIO["name"] og SITE, og så bygges siden på nytt (se MILEPÆLER.md, M5).

En ny app er én ny oppføring i APPS. Rekkefølgen i lista er rekkefølgen på siden:
appene som er ute først, så de som kommer.
"""

# Adressen siden ligger på. Brukes bare i canonical, hreflang og delebildet;
# alle lenker inne på siden starter med «/» og virker på begge adressene.
SITE = "https://svaagan.github.io"

STUDIO = {
    "name": "App Factory",
    "person": "Stian Gaare Vaagan",
    "email": "kontakt@runpace.no",
    # Utviklersiden i App Store, med alle appene som er ute.
    "appstore_developer": "https://apps.apple.com/developer/id6789667870",
}

# status:
#   "live"  – i App Store: App Store-merke og lenke til appens egen side.
#   "soon"  – ikke ute ennå: «Kommer snart», ingen merke.
# page: appens egen side. Starter den med «/», ligger den under fellessiden.
#       None betyr at appen ikke har noen side ennå.
# category: schema.org-kategorien for apper som ikke er spill.
# price: vises bare for apper som er ute. Aldri beløp, de varierer med land.
# page_en: den engelske siden, hvis den finnes et annet sted enn page + «en/».
APPS = [
    {
        "slug": "runpace",
        "name": "RunPace",
        "status": "live",
        "appstore_id": "6789667868",
        "page": "https://runpace.no/",
        "page_en": "https://runpace.no/en/",
        "kind": {"nb": "Løping", "en": "Running"},
        "category": "HealthApplication",
        "tagline": {
            "nb": "Løpekalkulator for tempo, fart, sluttider og mellomtider.",
            "en": "A running calculator for pace, speed, finish times and splits.",
        },
        "devices": {"nb": "iPhone", "en": "iPhone"},
        "price": {"nb": "Gratis, med Pro", "en": "Free, with Pro"},
    },
    {
        "slug": "pokerface",
        "name": "Pokerface",
        "status": "live",
        "appstore_id": "6825464919",
        "page": "/pokerface/",
        "page_en": "/pokerface/en/",
        "kind": {"nb": "Selskapsspill", "en": "Party game"},
        "tagline": {
            "nb": "Alle får det hemmelige ordet, bortsett fra bløffmakeren. Pek den ut før den skjønner hva ordet er.",
            "en": "Everyone gets the secret word except the bluffer. Call them out before they work it out.",
        },
        "devices": {"nb": "iPhone · 3–20 spillere", "en": "iPhone · 3–20 players"},
        "price": {"nb": "Gratis, med Pro", "en": "Free, with Pro"},
    },
    {
        "slug": "taptime",
        "name": "TapTime",
        "status": "live",
        "appstore_id": "6826379785",
        "page": "/taptime/",
        "page_en": "/taptime/en/",
        "kind": {"nb": "Selskapsspill", "en": "Party game"},
        "tagline": {
            "nb": "Si et ord i kategorien og trykk på en ledig bokstav før tiden går ut.",
            "en": "Say a word that fits the category and tap its first letter before time runs out.",
        },
        "devices": {"nb": "iPhone og iPad · 2–8 spillere", "en": "iPhone and iPad · 2–8 players"},
        "price": {"nb": "Gratis, med Pro", "en": "Free, with Pro"},
    },
    {
        "slug": "knips",
        "name": "Knips",
        "status": "soon",
        "appstore_id": None,
        "page": "https://knipspics.no/",
        "page_en": None,
        "kind": {"nb": "Kamera", "en": "Camera"},
        "tagline": {
            "nb": "Gjør gjestenes telefoner til engangskameraer. Alle bildene fremkalles samtidig, etter festen.",
            "en": "Turns your guests’ phones into disposable cameras. Every photo develops at once, after the party.",
        },
        "devices": {"nb": "iPhone", "en": "iPhone"},
    },
    {
        "slug": "leyezer",
        "name": "Leyezer",
        "status": "soon",
        "appstore_id": None,
        "page": "/leyezer/",
        "page_en": "/leyezer/en/",
        "kind": {"nb": "Spill", "en": "Game"},
        "tagline": {
            "nb": "Forsvar slottet ved å sikte med nesa. Laseren kommer fra dine egne øyne.",
            "en": "Defend the castle by aiming with your nose. The laser shoots from your own eyes.",
        },
        "devices": {"nb": "iPhone", "en": "iPhone"},
    },
    {
        "slug": "pengeblokka",
        "name": "Pengeblokka",
        "status": "soon",
        "appstore_id": None,
        "page": "/pengeblokka/",
        "page_en": None,
        "kind": {"nb": "Økonomi", "en": "Finance"},
        "category": "FinanceApplication",
        "tagline": {
            "nb": "Budsjett fra lønn til lønn. Du fører selv, og ingenting forlater telefonen.",
            "en": "A budget that runs from payday to payday. You keep the books, and nothing leaves your phone.",
        },
        "devices": {"nb": "iPhone", "en": "iPhone · Norwegian only"},
    },
]
