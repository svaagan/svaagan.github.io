# Kunnskapsgrunnlag – fellessiden

Undersøkt 2026-11-04, før designet ble valgt. Sidene ble hentet og lest samme dag.

## Hva de beste studiosidene gjør

| Side | Oppsett | Kortet | App Store | Kommer snart |
|---|---|---|---|---|
| sindresorhus.com/apps | Rutenett med 60+ apper og filtre | Ikon, navn, én linje, plattform og «Free/Paid» | Kortet går til appens egen side; merket ligger der | Bare «New»-merke |
| iconfactory.com | Lange seksjoner | Tre skjermbilder per app | Tekstlenke | Nei |
| panic.com | Én lang side, gruppert etter type | Navn, én linje, plattform | Tekstlenke til produktsiden | Nei |
| Triple Glazed (Mercury) | Store rader | Kategori, navn, stort skjermbilde, sitat | «View on the App Store →» | Nei |
| Tapbots | Kort liste | Lite ikon, navn, én linje | Tekstlenker | Nei |
| Rogue Amoeba | Liste | 256 px ikon, navn, én linje, knapper | Knapper (selges direkte) | Nei |
| Snowman | Fliser | Navn, plattform, kunst | Lenke til spillets side | Nei |
| Lucas Pope | Én kolonne, nyeste først | Bilde, navn, linje | Tekstlenke | Nei |

Fellestrekk: ingen bruker det offisielle merket på oversikten, alle har én linje om hver app,
og «om»-delen er kort.

## Apples regler for merket

Fra [Apples markedsføringsregler](https://developer.apple.com/app-store/marketing/guidelines/):
- Minst 40 px høyt, luft på en firedel av høyden rundt, bare Apples egen tegning.
- **Ett merke per oppsett.** Et rutenett med merke på hvert kort bryter regelen.
- Bare for apper som er ute. Kommende apper får aldri merket (unntatt det offisielle
  «Pre-order»-merket).
- Norsk merke på norske sider, engelsk på engelske; «App Store» oversettes aldri.

## Søkemotorer

- Forside med `ItemList` som peker til hver app, og egen side per app
  ([Google om programvareapper](https://developers.google.com/search/docs/appearance/structured-data/software-app)).
- Spill merkes `["VideoGame","MobileApplication"]`; `VideoGame` alene gir ingenting.
- Stjerner krever egne vurderinger på siden. Vurderinger hentet fra App Store er ikke lov
  ([Googles regler for vurderinger](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)),
  så fellessiden har ingen stjerner.
- Smart App Banner (`apple-itunes-app`) gjelder én app og hører hjemme på appsidene, aldri her.

## Avgjørelsene

- **Hele kortet er klikkbart** og går til appens egen side. Under står tekstlenken
  «Last ned i App Store ↗». Dermed ingen merker på oversikten, som Apple krever.
- **Ikon, ikke skjermbilder.** Det finnes ingen gode tall for hva som gir flest klikk på en
  porteføljeside. Skjermbilder passer for to–tre apper, men gjør seks apper til en lang side.
  Ikonene er stilt opp i 88 px på datamaskin og 68 px på mobil.
- **Pris uten beløp:** «Gratis, med Pro», som Sindre Sorhus. Beløpene varierer med land.
- **«Kommer snart» vises**, som Stian valgte. De står for seg selv, dempet, uten lenke til App Store.
  Fare: står en app der lenge, ser det uferdig ut. Flytt den opp når den er ute, eller fjern den.
- **Rammen er nøytral** (systemfonten, grått og hvitt), så ikonene står for fargen. **Bare lyst tema**, også når telefonen står i mørk modus (Stian, 2026-11-04).
  Merket er fire ruter i fargene fra appikonene.
- **Ingen føringer for hva slags apper studioet lager** (Stian, 2026-11-04): forsiden sier bare at dette er alle appene, og «om» er én setning med navnet pluss e-post. Hver app beskrives på sin egen side.
