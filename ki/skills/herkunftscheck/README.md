# Herkunftscheck zum Mitnehmen

Der Herkunftscheck verfolgt **ein** Zitat, **eine** Zahl oder **eine** Behauptung rückwärts bis zum Ursprung: Wer hat das zuerst gesagt oder veröffentlicht, wann, wo und in welchem Wortlaut? Er läuft als Skill in einem KI-Assistenten mit Websuche und liefert eine Herkunftskette mit Belegen und einer Konfidenz.

Die Abgrenzung zum [Faktencheck](../faktencheck/) und zu [Moby](../../agent/moby/): Die prüfen, ob etwas stimmt, der Herkunftscheck fragt, woher es stammt, und geht bei einer einzelnen Aussage in die Tiefe. Passt zu Kapitel 5 des Seminars.

Stand: 03.11.2026

## Welche Datei wofür

| Datei | Länge | Wofür |
|---|---|---|
| `SKILL.md` | rund 2.200 Wörter, 16.700 Zeichen | Langfassung: in einen Chat einfügen, in ein Projekt legen oder als Skill hochladen |
| `Herkunftscheck_kurz.md` | rund 3.600 Zeichen | Kurzfassung für Anweisungsfelder mit Zeichenlimit (GPT, Le-Chat-Agent) |
| [`herkunftscheck.zip`](../zum-hochladen/herkunftscheck.zip) im Ordner `zum-hochladen` | – | Paket zum Hochladen in Claude und Gemini |

## Voraussetzung

Ein KI-Assistent mit **Websuche**, der Seiten auch **öffnen** kann. Nur dann kann er die Primärquelle selbst lesen und 🟢 vergeben. Kann er nur suchen, bittet er euch, die Quelle zu öffnen und den Absatz einzufügen. Wie ihr den Skill einsetzt, steht in der [Anleitung](../README.md).

## So fragt ihr

Das Item möglichst wortgenau eingeben, mit der angeblichen Herkunft, wenn ihr sie kennt:

- „Woher stammt das Zitat ‚Kunst ist schön, macht aber viel Arbeit‘? Angeblich Karl Valentin.“
- „Woher kommt die Zahl, dass jede dritte Bühne in Deutschland Besucher verloren hat?“
- „In diesem Artikel steht eine Zahl zu den Besucherzahlen. Woher stammt sie?“ und darunter den Link

## Das Ergebnis lesen

| Symbol | heißt |
|---|---|
| 🟢 | Original im Volltext gelesen, Wortlaut oder Wert stimmt |
| 🟡 | stimmige Kette, aber das Original war nicht lesbar |
| 🟡ˢ | wie 🟡, nur aus Suchtreffer-Ausschnitten |
| 🟠 | widersprüchliche Zuschreibungen oder Wortlaute |
| 🔴 | Ursprung nicht belegbar |
| ⏸️ | unfertig: Primärquelle gefunden, aber noch nicht geöffnet. Schreibt „weiter“ |

- Die **Herkunftskette** steht mit dem jüngsten Beleg oben und dem Erstbeleg unten.
- Öffnet mindestens die unterste Station selbst. Erst dann zitiert ihr.
- Viele Treffer heißen nicht viele Belege: Medien, die sich aufeinander beziehen, sind eine Quelle.

## Grenzen

- **Ein Item pro Auftrag:** ein Zitat, eine Zahl oder eine Behauptung. Einen ganzen Text prüft der [Faktencheck](../faktencheck/).
- **Keine Bilder:** Woher ein Foto stammt, klärt eine Bild-Rückwärtssuche, nicht dieser Skill.
- **Keine Bezahlschranken:** Er umgeht sie nicht, sondern sucht frei zugängliche Fassungen oder bittet euch, die Quelle zu öffnen und den Absatz einzufügen.

## Herkunft

Beruht auf dem Herkunftscheck, den Florian in der Redaktion nutzt, für verschiedene Plattformen umgebaut.
