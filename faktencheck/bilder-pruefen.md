# Bilder prüfen und Geolokation

Aus Kapitel 5 der Seminarfolien (Bild und Video). Stand: 07.11.2026.

**Prüfstufe:** geöffnet am 07.11.2026. Übernommen aus den Folien: Image Whisperer, Wolfram Alpha, das InVID-Plugin und die Angaben dazu, was die Werkzeuge können und kosten. Zu prüfen: Baidu und SynthID.

## Die Checkliste

Drei Schritte, nicht zwingend in dieser Reihenfolge:

1. **Originalquelle finden**
2. **Innere und äußere Logik prüfen**
3. **Technische Hinweise auf KI ausschließen**

Euer Bauchgefühl ist oft gar nicht schlecht. Verlassen solltet ihr euch nicht darauf.

## Welchen Fotoquellen vertraut ihr wie sehr?

| Quelle | Vertrauen |
|---|---|
| Soziale Medien, Beteiligte, Unternehmen, Stockagenturen | alles hinterfragen; Bildunterschriften können von einer KI übersetzt oder ergänzt sein |
| Nachrichtenagenturen wie dpa, AFP, AP, Reuters | nicht komplett zurücklehnen |
| selbst fotografiert oder von eigenen Fotografinnen und Fotografen | sicher |

## 1. Originalquelle finden: Rückwärtssuche

| Werkzeug | Wofür | Adresse |
|---|---|---|
| Google Lens | Standard, auch für einzelne Gebäude oder Objekte im Bild, ohne Konto | in der Google-Suche das Kamera-Symbol |
| Yandex | Bilder aus Russland, der Ukraine und Osteuropa | [yandex.com/images](https://yandex.com/images/) |
| Baidu | Bilder aus China, Oberfläche chinesisch | graph.baidu.com, zu prüfen |
| TinEye | sortiert die Treffer besser, etwa nach dem ältesten Fund | [tineye.com](https://tineye.com/) |
| Bing | warum nicht mal probieren? | in der Bing-Bildersuche das Kamera-Symbol |
| PimEyes, Lenso.ai | Gesichtersuche, meist kostenpflichtig | [pimeyes.com](https://pimeyes.com/), [lenso.ai](https://lenso.ai/) |

**Gesichter** sind besonders geschützte Daten. Die Gesichtersuche nur mit gutem Grund nutzen und den Datenschutz beachten.

**Tipp:** Das [InVID-WeVerify-Plugin](https://bellingcat.gitbook.io/toolkit/more/all-tools/invid) für Chrome bündelt alle Suchen und zerlegt Videos in Standbilder.

**Die Treffer lesen:**

- **Genaue Übereinstimmungen** zeigen dasselbe Bild. Wann und wo wurde es zuerst gepostet? Klickt immer auf die Links. Wie verlässlich ist die Quelle?
- **Visuelle Übereinstimmungen** zeigen ähnliche Bilder. Die helfen bei der Geolokation, etwa derselbe Ort aus einem anderen Blickwinkel.

## 2. Innere und äußere Logik

**Innere Logik:** Hektisch generierte Fakes sind immer noch voller Fehler.

- Personen: Schmuck, Haare und Bart, Finger und Hände, Pupillen, fehlende Hautunreinheiten (oft wachsige Haut)
- Text: vor allem im Hintergrund und in Videos
- Licht und Schatten: Wo sind die Lichtquellen? Stimmen die Spiegelungen?
- Schärfe und Unschärfe: Ergibt der Fokus Sinn? Ist er überhaupt möglich?
- Videos: Bild für Bild anschauen, etwa im VLC-Player oder mit dem InVID-Plugin

**Äußere Logik:** Ist das Foto plausibel?

- Wo wurde es aufgenommen? Satellitenbilder, etwa in [Google Earth](https://earth.google.com/).
- Stimmt das Wetter? Historische Wetterdaten, etwa in [Wolfram Alpha](https://www.wolframalpha.com/) mit einer Abfrage wie `weather Munich June 12 2026`. Kahle Bäume im Juni passen nicht.
- Wer hat es gepostet, mit welcher Absicht? Kann sein, was gezeigt wird? Soll es Wut oder Angst auslösen?

## 3. Technische Hinweise auf KI

| Werkzeug | Was es kann | Zugang |
|---|---|---|
| SynthID Detector | erkennt das Wasserzeichen, das Google, OpenAI, NVIDIA, Kakao und Apple selbst einbauen; Bild, Video, Audio | auf synthid.com oder in der Gemini-App, nur mit Anmeldung, etwa 10 Prüfungen am Tag; Adresse zu prüfen |
| [Content Credentials (C2PA)](https://verify.contentauthenticity.org/) | zeigt signierte Herkunftsangaben, die mit der Datei reisen: Aufnahme, Bearbeitung, Veröffentlichung | Datei hochladen oder Bildadresse einfügen |
| [Image Whisperer](https://www.imagewhisperer.org/) | führt viele Erkennungsmodelle zusammen und legt offen, wie es urteilt | laut Website 1 € für 2 Prüfungen; übernommen |
| Hive AI Detector | prüft Bild, Video, Text und Audio auf KI | kostenlos, ohne Konto, Erweiterung im Chrome Web Store |
| [Forensically](https://29a.ch/photo-forensics/) | findet Bearbeitungsspuren, keine KI-Erkennung | kostenlos im Browser, die Bilder bleiben auf eurem Rechner |

**Was die Ergebnisse heißen:**

- **SynthID:** Ein gefundenes Wasserzeichen heißt, dass KI im Spiel war. Kein Wasserzeichen heißt nicht, dass das Foto echt ist. Das Wasserzeichen übersteht Screenshots und Bearbeitungen, lässt sich aber entfernen. Bilder von Flux, Anthropic und chinesischen Modellen tragen es nicht.
- **C2PA:** Viele Plattformen löschen die Herkunftsdaten beim Hochladen. Meistens fehlen sie deshalb.
- **KI-Detektoren:** In Tests sind die Ergebnisse unzuverlässig. Sie geben einen Hinweis, nie das letzte Wort.

## Ein möglicher Ablauf

Eine Faustregel, kein Automatismus:

1. Originalquelle gefunden, und ihr vertraut ihr? Dann ist das Bild verwendbar.
2. Sonst: Zeigt SynthID oder C2PA KI? Dann ist es ein KI-Fake.
3. Sonst: Gibt es sichtbare Fehler, oder ist es nicht plausibel? Dann ist es ein KI-Fake.
4. Sonst: Zeigt ein Detektor wie Image Whisperer KI? Dann ist es ein KI-Fake.
5. Sonst: verwendbar, aber ein Restrisiko bleibt immer, etwa ein echtes Foto in falschem Zusammenhang. Im Zweifel mit der Bildredaktion sprechen.

## Verifikation mit Sprachmodellen?

Sprachmodelle können helfen, verlassen könnt ihr euch nie darauf. Ein schwacher Prompt fragt nur: „Ist dieses Video echt oder KI-generiert?“ Ein starker Prompt hat fünf Teile, wie der Auftrag in [Von der Frage zum Auftrag](../prompts/recherche-auftrag.md):

```
Rolle: Du bist eine erfahrene OSINT-Analystin.
Ziel: Dieses Foto soll [was, wo, wann] zeigen. Prüfe Ort und Zeitpunkt.
Quellen: Suche die früheste Veröffentlichung in sozialen Netzwerken und seriösen Quellen. Nenne direkte Links.
Grenzen: Trenne Beobachtung von Vermutung, sag klar, was du nicht prüfen konntest. Erfinde keine Belege, urteile nicht allein nach dem Aussehen.
Format: Tabelle mit Befund, Beleg mit Link, offen.
```

## Geolokation: Wo wurde das aufgenommen?

1. **Hinweise sammeln:** Schilder und Sprache, Architektur, Kennzeichen, Vegetation, markante Bauten.
2. **Grob eingrenzen:** Land, Stadt, Viertel.
3. **Abgleichen:** Satellitenbild, Street View, Fotos anderer vom selben Ort.
4. **Zeit prüfen:** Schatten, Wetter, Jahreszeit.

| Werkzeug | Was es kann | Adresse |
|---|---|---|
| Google Maps und Google Earth | Satellit, Street View, 3D-Ansicht | [earth.google.com](https://earth.google.com/) |
| OpenStreetMap | Karte, teils detailreicher als Google: Wege, Gebäude | [openstreetmap.org](https://www.openstreetmap.org/) |
| Mapillary | Straßenfotos von Nutzerinnen und Nutzern, auch wo Street View fehlt | [mapillary.com/app](https://www.mapillary.com/app) |
| Bellingcat OSM Search | Orte über Merkmale finden, etwa „Kirche neben Bahnlinie“ | [osm-search.bellingcat.com](https://osm-search.bellingcat.com/) |
| SunCalc, Sonnenverlauf | Sonnenstand und Schatten für Ort und Uhrzeit | [suncalc.org](https://www.suncalc.org/), [sonnenverlauf.de](https://www.sonnenverlauf.de/) |
| Wolfram Alpha | historisches Wetter an Ort und Tag | [wolframalpha.com](https://www.wolframalpha.com/) |
| Rückwärtssuche | visuelle Übereinstimmungen zeigen denselben Ort aus anderen Blickwinkeln | siehe oben |

