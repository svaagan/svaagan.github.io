# Milepæler: én fellesside for alle appene (arbeidsnavn «App Factory»)

## Status

| Milepæl | Status |
|---|---|
| M0 Undersøk de beste | ✅ `docs/KUNNSKAPSGRUNNLAG.md` |
| M1 Bygg fellessiden | ✅ |
| M2 Publiser | ✅ live på https://svaagan.github.io/ (2026-11-04) |
| M3 Lenker tilbake | ✅ TapTime, Pokerface (6 språk), Leyezer, Knips og runpace.no |
| M4 Pengeblokka | ✅ sidene er ute, `metadata.md` i appen peker hit |
| M5 Studionavn og domene | venter på at Stian velger navn |

## Avklart med Stian 2026-11-04 (før nattkjøringen)
- Publiser alt i natt: repoet `svaagan/svaagan.github.io`, fellessiden og lenkene på appsidene.
- NOCB vises ikke før App Review har godkjent den (den skriver om VG-overskrifter).
- Stian skal ikke nevnes ved navn på siden (endret 2026-11-06; først var det fullt navn). Bare studionavnet og e-posten kontakt@runpace.no inntil videre.

## Nattkjøringen 2026-11-04 – hva som ble gjort og hvorfor
- **Kortene har tekstlenke, ikke App Store-merket.** Apple tillater ett merke per side, og
  ingen av de beste studiosidene bruker merket på oversikten (`docs/KUNNSKAPSGRUNNLAG.md`).
  Hele kortet går til appens egen side.
- **Leyezer:** bare lenken ble publisert. `web/` hadde fra før seks commits med sider for 1.1
  (kjøp, varmesyn) som ikke er pushet med vilje, fordi 1.1 ikke er ute. Lenken ble lagt
  rett på den publiserte utgaven, og lokal `main` er slått sammen med den. 1.1-sidene
  venter fortsatt.
- **Knips:** de to ventende commitene (Smart App Banner og TestFlight-lenken) ble pushet
  sammen med lenken, siden statusen sa at de kunne pushes. QR-sida (`404.html`) fikk ikke
  lenken, så gjestene ikke ledes bort.
- **Pokerface:** tysk og fransk lenker til den engelske fellessiden, svensk og dansk til
  den norske.
- **Pengeblokka:** personvernsiden lå aldri på runpace.no (den svarte 404), så det var
  ingenting å la ligge igjen der.
- **NOCB** er ikke med, som avtalt.

**Når studionavnet bestemmes (M5):** «App Factory» står i `portefolje/_src/apps.py` og
`make_images.py` (kjør begge), `runpace/_src/chrome.py` (`STUDIO`), `Alfa/scripts/make_web.py`
(`STUDIO`), og som tekst i bunnen av sidene i `Pokerface/web`, `Leyezer/web` og `Knips/web`
(`grep -rl "App Factory"`). Knips og runpace.no lenker til `https://svaagan.github.io/`, som
sender videre av seg selv.

## Bakgrunn
I dag har hver app sin egen adresse:

| App | Adresse i dag | Status |
|---|---|---|
| RunPace | runpace.no (eget domene, 36 sider) | i App Store |
| Pokerface | svaagan.github.io/pokerface/ | i App Store |
| TapTime | svaagan.github.io/taptime/ | i App Store |
| Knips | knipspics.no (eget domene, QR-lenker og app-lenker) | TestFlight |
| Leyezer | svaagan.github.io/leyezer/ | TestFlight |
| NOCB | ingen nettside | TestFlight |
| Pengeblokka | personvernsiden ligger på runpace.no/pengeblokka/ | klar til innsending |

Målet er én porteføljeside som viser alle appene, slik at nye apper får en side der i
stedet for et eget domene. Studionavnet bestemmes senere; frem til da heter siden
«App Factory». Navnet står bare ett sted i koden, så det er raskt å bytte.

## Grepet som gjør dette enkelt
GitHub har en egen «brukerside» i repoet `svaagan/svaagan.github.io`. Den legges i rota
på `svaagan.github.io/`. Pokerface, TapTime og Leyezer ligger allerede på undersider av
den adressen, så de dukker opp under fellessiden av seg selv, uten å bli flyttet.

Når studionavnet og domenet er på plass, setter vi domenet på brukersiden. Da gjør GitHub
selv dette:
- fellessiden flytter til `studionavn.no/`
- appene flytter til `studionavn.no/pokerface/`, `/taptime/` og `/leyezer/`
- de gamle `svaagan.github.io/...`-adressene sender videre til de nye, så adressene som
  står i App Store Connect og i appene fortsetter å virke

Det betyr at fellessiden kan bygges nå, før domenet finnes.

## Fordeler og ulemper
**Fordeler**
- Ingen ny domeneavgift, DNS-oppsett eller HTTPS-jobb per app. En ny app trenger bare en
  ny underside og én linje i applista.
- Folk som finner én app, ser alle de andre. Det gir gratis reklame mellom appene.
- Det ser mer seriøst ut overfor App Review, presse og brukere når det står et studio bak.
- Google bygger opp tillit til ett domene, ikke sju små.
- Alle appene får samme mal for personvern og hjelp.

**Ulemper og risikoer**
- Alle eggene i én kurv. Går domenet ut, slutter personvern- og hjelpelenkene til alle
  appene å virke, og Apple kan da fjerne appene. Slå på automatisk fornyelse.
- Den enkelte appen får et svakere merke enn med et eget domene, og selger du en app
  senere, kan ikke adressen følge med.
- Sidene handler om alt fra løping til poker, så ingen app er så tett knyttet til
  domenet som runpace.no er til RunPace.
- Bytter du studionavn etter at domenet er tatt i bruk, flytter alt én gang til. Derfor
  venter vi med domenet til navnet er bestemt.

## Svar: blir søkemotorplasseringen (SEO) like god om RunPace flyttes inn?
Ja, på sikt er det mulig. Google lar plasseringen følge med når hver gammel adresse sender
permanent videre (301) til sin nye, og når flyttingen meldes i Search Console. Det koster
ofte noen uker til et par måneder med dårligere plassering. RunPace ligger dessuten bare
på plass 33, så det er ikke mye å miste.

Likevel anbefaler jeg å **beholde runpace.no og knipspics.no** og vise dem som kort på
fellessiden. Det er fordi flyttingen ikke sparer noe:
- runpace.no må uansett betales videre. `/support/` står i App Store Connect og kan ikke
  bytte adresse, appen lenker til runpace.no, og `app-ads.txt` må ligge der. GitHub Pages
  kan heller ikke sende videre side for side, så det krever i tillegg et videresendingsoppsett
  på hjemmeserveren.
- Knips har QR-kodene og lenkene som åpner appen (`/e/<kode>`) bakt inn i appen. Å flytte
  dem krever en ny appversjon, og koder som allerede er skrevet ut, må fortsatt virke.

Gevinsten av å samle ligger i alle appene som kommer. Spørsmålet kan tas opp igjen når
fellesdomenet har bygd seg opp.

## Gjennomføring

### M0 – Undersøk de beste (før design)
Studer 6–8 gode porteføljesider fra små appstudioer, med kilder. Se på oppsettet
(rutenett eller liste), hva hvert kort viser, hvor App Store-knappen står og hvordan
«kommer snart» vises. Skriv et kort notat med valgene og begrunnelsen, med valgmuligheter
der svaret er usikkert. *(Følger regelen om å designe etter de beste.)*

### M1 – Bygg fellessiden lokalt
En ny mappe `/Users/svaagan/Documents/Claude/portefolje/` med eget git-repo (blir
`svaagan/svaagan.github.io`). Den bygges som runpace.no, med generator og sjekk:
- `_src/apps.py`: applista med navn, kort tekst på norsk og engelsk, status (i App Store
  eller kommer snart), App Store-ID, lenke og ikon. Ingenting om appene skrives for hånd
  i HTML-en. Studionavnet står bare her, i én konstant.
- `_src/build.py` lager `index.html` (norsk) og `en/index.html` (engelsk), `404.html`
  og `.nojekyll`. Byggeren til runpace.no (`runpace/_src/build.py`, `chrome.py`) brukes
  som mønster.
- `_src/check.py` sjekker at alle lenker og ikoner finnes og at begge språkene har de
  samme appene.
- Ikonene hentes fra appenes egne `web/icon.png`, og App Store-ID-ene fra lenkene som
  allerede står i appenes nettsider. RunPace har 6789667868.
- Innhold: RunPace, Pokerface og TapTime med App Store-knapp og lenke til egen side.
  Knips, Leyezer, NOCB og Pengeblokka står som «kommer snart», uten knapp.
- Ingen mapper i rota får samme navn som et app-repo (`pokerface`, `taptime`, `leyezer`),
  ellers kolliderer adressene.

### M2 – Publiser
Opprett `svaagan/svaagan.github.io` i nettleseren (det finnes ingen `gh`), push over SSH og
slå på Pages. Sjekk at `svaagan.github.io/` svarer 200, og at `/pokerface/`, `/taptime/` og
`/leyezer/` fortsatt svarer 200.

### M3 – Lenker tilbake fra appsidene
Legg en lenke nederst på hver appside: «Flere apper fra App Factory».
- Pokerface og TapTime lages fra en mal i hvert sitt private app-repo. Det er malen som
  skal endres, ikke HTML-en.
- Leyezer og Knips: i `web/`.
- runpace.no: i `runpace/_src/chrome.py`, så `build.py` og `check.py`.

### M4 – Pengeblokka flytter til fellessiden
Legg personvern og hjelp for Pengeblokka på `svaagan.github.io/pengeblokka/`, og sett de nye
adressene i App Store Connect **før** innsending. Siden på runpace.no blir liggende, slik at
gamle lenker virker.

### M5 – Senere: studionavn og domene
Når navnet er bestemt:
1. Registrer domenet i ditt navn hos Domeneshop. Det kan Claude ikke gjøre for deg.
2. Legg `CNAME` i fellessiden og DNS-postene via Domeneshop-API-et, og slå på HTTPS.
3. Bytt navnekonstanten, bygg og push.
4. Oppdater adressene i App Store Connect og i appene når hver app får sin neste versjon.
   Fram til da sender de gamle adressene videre.
5. Legg domenet til i Google Search Console.

### Oppskrift for nye apper
Lag et repo med appens slug-navn (`web/`-mønsteret som Pokerface har), og legg til én linje i
`_src/apps.py`. Ferdig, og uten nytt domene.

## Inntekt
Siden selger ingenting selv. Verdien ligger i at appene viser fram hverandre: én bruker av
Pokerface som også laster ned TapTime eller kjøper Pro. Tallene kan følges i `/app-tall`
over tid (nedlastinger fra nettsider per app), men det lages ingen ny sporing nå.

## Verifisering
- `python3 _src/build.py && python3 _src/check.py` uten feil.
- Åpne siden i Chrome i bredde for mobil (390 px) og datamaskin. Klikk hver knapp og hvert
  kort, og sjekk at App Store-lenkene og lenkene til appsidene treffer. Bytt språk begge
  veier. Sjekk både lyst og mørkt tema.
- Etter publisering: `curl` gir 200 på fellessiden og på alle appsidene, og lenkene tilbake
  fra appsidene virker.
- Commit ved hver milepæl (M1–M4).

## Modell og innsats
**Sonnet 5.5, middels innsats.** Dette er en liten statisk side som følger et mønster vi
allerede har på runpace.no. Bytt til Opus 5.5 bare for designundersøkelsen i M0 hvis du
vil ha et grundigere smaksskjønn. Planen ligger i fil, så kjør gjerne `/clear` før vi
begynner å bygge.
