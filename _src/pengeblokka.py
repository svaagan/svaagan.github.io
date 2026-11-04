# -*- coding: utf-8 -*-
"""Forside og hjelp for Pengeblokka, som ikke har noen nettside fra før.

Appen er bare på norsk, så sidene er det også. Personvernerklæringen er en ferdig
side fra appens repo (Apputvikling/Pengeblokka/AppStore/personvern.html), kopiert
til _src/body/pengeblokka-personvern.html. Endres den der, kopieres den hit igjen.

Når appen er ute: sett status «live» og appstore_id i apps.py, og legg App
Store-merket og Smart App Banner inn her.
"""

DESCRIPTION = ("Pengeblokka er et budsjett for iPhone som går fra lønn til lønn. Du fører "
               "selv, uten bankkobling og uten konto, og ingenting forlater telefonen.")

FEATURES = [
    ("Ett tall å forholde seg til",
     "«Igjen å bruke» står øverst og sier hva du har igjen, og hvor mye det blir per dag "
     "resten av perioden."),
    ("Fra lønn til lønn",
     "Perioden starter på lønnsdagen din, ikke den 1. Lander lønna på en helg eller en rød "
     "dag, flyttes den til siste virkedag før."),
    ("Faste poster som oppfører seg",
     "Husleie, strøm og abonnementer legges inn én gang og trekkes fra med én gang. En post "
     "kan settes på pause, og pausen tar slutt av seg selv."),
    ("Hva ting faktisk koster",
     "Del opp en handletur i varelinjer, så blir de til prishistorikk: hva melka har kostet "
     "det siste halvåret."),
    ("Dine tall, din telefon",
     "Ingen konto, ingen reklame og ingen sporing. Appen kobler seg ikke til nettet, og "
     "sikkerhetskopien går til din egen iCloud Drive."),
]

FAQ = [
    ("Må jeg koble til banken?",
     "Nei. Pengeblokka har ingen bankkobling. Du fører inntekter og utgifter selv, og bare "
     "beløpet må fylles ut."),
    ("Hvordan bytter jeg lønnsdag?",
     "Gå til Innstillinger og trykk «Endre lønnsdagen». Ingenting slettes, og du kan sette "
     "lønnsdagen tilbake når som helst."),
    ("Jeg førte en utgift feil. Kan den rettes?",
     "Ja. Trykk på utgiften, i perioden den hører til, og rett den. Det gjelder også "
     "perioder bakover i tid."),
    ("Hvorfor sier appen fra når jeg fører en fast post?",
     "Fører du en utgift med samme navn som en fast post, kan den bli trukket fra to ganger. "
     "Appen sier fra, men stopper deg ikke."),
    ("Hvor ligger sikkerhetskopien?",
     "I mappa «Pengeblokka» i din egen iCloud Drive, som du finner i Filer-appen. De ti siste "
     "kopiene beholdes. Under Sikkerhetskopi i Innstillinger kan du også trykke «Del en kopi» "
     "og lagre fila der du vil."),
    ("Jeg har fått ny telefon. Hvordan får jeg med tallene?",
     "Installer Pengeblokka og gå til Innstillinger → Sikkerhetskopi → «Gjenopprett fra fil». "
     "Velg den nyeste kopien i mappa «Pengeblokka» i iCloud Drive. Du får se hva kopien "
     "inneholder før noe byttes ut."),
    ("Kommer appen på engelsk eller til Android?",
     "Ikke foreløpig. Pengeblokka er laget for norske kroner, norsk lønnsdag og norske "
     "helligdager."),
]


def pages(app, icon, E):
    feat = "\n".join('      <li><h3>%s</h3><p>%s</p></li>' % (E(h), E(p)) for h, p in FEATURES)
    home_body = f'''<main class="wrap narrow app-page" style="--app-accent:#0f7a4f;--app-accent-dark:#34c88a">
  <div class="app-hero">
    {icon(app, 112)}
    <div>
      <h1>Pengeblokka</h1>
      <p class="meta">Budsjett · iPhone · bare på norsk</p>
    </div>
  </div>
  <p class="lead">Én oversikt fra lønn til lønn: hva du har igjen, hva som er fast, og hva ting
    koster. Du fører selv, og ingenting forlater telefonen.</p>
  <p><span class="pill">Kommer snart i App Store</span></p>
  <ul class="features" role="list">
{feat}
  </ul>
  <p class="links"><a href="support/">Hjelp</a> <a href="personvern/">Personvern</a></p>
</main>'''
    faq = "\n".join('    <details><summary>%s</summary><p>%s</p></details>' % (E(q), E(a))
                    for q, a in FAQ)
    support_body = f'''<main class="wrap narrow app-page" style="--app-accent:#0f7a4f;--app-accent-dark:#34c88a">
  <p class="crumb"><a href="../">Pengeblokka</a></p>
  <h1>Hjelp til Pengeblokka</h1>
  <p class="lead">Svar på det folk lurer mest på. Finner du ikke svaret, skriv til
    <a href="mailto:kontakt@runpace.no">kontakt@runpace.no</a>, så svarer jeg så fort jeg kan.</p>
  <div class="faq">
{faq}
  </div>
  <p class="links"><a href="../personvern/">Personvern</a></p>
</main>'''
    return {
        "home": ("/pengeblokka/", "Pengeblokka – budsjett fra lønn til lønn", DESCRIPTION, home_body),
        "support": ("/pengeblokka/support/", "Hjelp – Pengeblokka",
                    "Hjelp og svar på vanlige spørsmål om Pengeblokka, budsjettappen fra lønn til lønn.",
                    support_body),
    }
