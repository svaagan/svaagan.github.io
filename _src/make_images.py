# -*- coding: utf-8 -*-
"""Lager delebildet (og.png, 1200x630) og nettsideikonet (favicon.png, 180x180).

    python3 _src/make_images.py

Kjøres når studionavnet, merket eller applista endres. Resultatet committes.
Krever Pillow og systemfonten SF (følger med macOS).
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apps import STUDIO, APPS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = "/System/Library/Fonts/SFNS.ttf"
MARK = ["#F6C915", "#E0263A", "#C2491D", "#C8F03C"]   # samme som MARK i build.py
S = 2  # tegnes i dobbel størrelse og skaleres ned, for glatte kanter


def font(size, weight):
    f = ImageFont.truetype(FONT, size * S)
    try:
        f.set_variation_by_axes([100, min(96, size), 400, weight])  # bredde, optisk størrelse, GRAD, vekt
    except Exception:
        pass
    return f


def mark(draw, x, y, cell, gap, radius):
    for i, colour in enumerate(MARK):
        cx = x + (i % 2) * (cell + gap)
        cy = y + (i // 2) * (cell + gap)
        draw.rounded_rectangle([cx * S, cy * S, (cx + cell) * S, (cy + cell) * S],
                               radius=radius * S, fill=colour)


def rounded_icon(path, size):
    im = Image.open(path).convert("RGBA").resize((size * S, size * S), Image.LANCZOS)
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, im.size[0] - 1, im.size[1] - 1],
                                        radius=int(size * S * .225), fill=255)
    im.putalpha(m)
    return im


def og():
    W, H = 1200, 630
    im = Image.new("RGB", (W * S, H * S), "#f5f5f7")
    d = ImageDraw.Draw(im)
    mark(d, 80, 80, 26, 6, 7)
    d.text((80 * S + 74 * S, 80 * S + 4 * S), STUDIO["name"], fill="#1d1d1f", font=font(44, 680))
    d.text((80 * S, 190 * S), "Alle appene,", fill="#1d1d1f", font=font(76, 700))
    d.text((80 * S, 280 * S), "på ett sted.", fill="#1d1d1f", font=font(76, 700))
    size, gap = 132, 26
    x = 80
    for app in APPS:
        ic = rounded_icon(os.path.join(ROOT, "icons", app["slug"] + ".png"), size)
        im.paste(ic, (x * S, 420 * S), ic)
        x += size + gap
    im = im.resize((W, H), Image.LANCZOS)
    im.save(os.path.join(ROOT, "og.png"), optimize=True)


def favicon():
    N = 180
    im = Image.new("RGBA", (N * S, N * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, N * S - 1, N * S - 1], radius=40 * S, fill="#1d1d1f")
    mark(d, 34, 34, 52, 8, 13)
    im.resize((N, N), Image.LANCZOS).save(os.path.join(ROOT, "favicon.png"), optimize=True)


if __name__ == "__main__":
    og()
    favicon()
    print("skrev og.png og favicon.png")
