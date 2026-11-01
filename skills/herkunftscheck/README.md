# Herkunftscheck zum Mitnehmen

Der Herkunftscheck verfolgt **ein** Zitat, **eine** Zahl oder **eine** Behauptung rückwärts bis zum Ursprung: Wer hat das zuerst gesagt oder veröffentlicht, wann, wo und in welchem Wortlaut? Er läuft als Prompt in einem KI-Assistenten mit Websuche und liefert eine Herkunftskette mit Belegen und einer Konfidenz.

Die Abgrenzung zu Moby: Moby prüft einen ganzen Text, der Herkunftscheck geht bei einer einzelnen Aussage in die Tiefe. Passt zu Kapitel 5b des Seminars.

Diese Fassung beruht auf dem Herkunftscheck, den Florian in der Redaktion nutzt (Stand 27.10.2026), umgebaut für verschiedene Plattformen.

Stand: 01.11.2026

## Welche Datei wofür

| Datei | Länge | Wofür |
|---|---|---|
| `Herkunftscheck.md` | rund 2.100 Wörter, 16.100 Zeichen | Langfassung: in einen Chat einfügen oder als Datei in ein Projekt legen |
| `Herkunftscheck_kurz.md` | rund 3.600 Zeichen | Kurzfassung für Anweisungsfelder mit Zeichenlimit (Gem, GPT) |

## Voraussetzung

Ein KI-Assistent mit **Websuche**, der Seiten auch **öffnen** kann. Nur dann kann er die Primärquelle selbst lesen und 🟢 vergeben. Kann er nur suchen, bittet er euch, die Quelle zu öffnen und den Absatz einzufügen. Wie ihr den Prompt einsetzt, steht in der [Anleitung](../ANLEITUNG.md).

## So fragt ihr

Nach dem Einfügen der Anweisungen das Item möglichst wortgenau eingeben, mit der angeblichen Herkunft, wenn ihr sie kennt:

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

## Was anders ist als in der Redaktionsfassung

- **Kein Plattformbezug.** „Seite öffnen“ statt eines bestimmten Werkzeugs, keine Verweise auf andere Skills.
- **Quellenregeln eingebaut** als Kurzfassung, ohne Ausschlussliste mit Namen.
- **Neu:** der Check zu Beginn, ob Websuche, Seitenabruf und Datum verfügbar sind. Beispiele ohne Redaktionsbezug.
