# Expertenmeinungen zum Mitnehmen

Expertenmeinungen sortiert eine Debatte, statt sie zusammenzufassen: Welche Lager gibt es zu einem Thema, wer sind die wichtigsten Stimmen je Lager, wo sind sich alle einig und worüber wird gestritten? Jede Position ist mit einer Aussage und ihrer Fundstelle belegt. Der Skill läuft in einem KI-Assistenten mit Websuche.

Die Abgrenzung: Die [Themenrecherche](../themenrecherche/) fragt „Was ist belegt?“, Expertenmeinungen fragt „Wer sagt was?“. Den Text, den ihr daraus schreibt, prüft der [Faktencheck](../faktencheck/) oder [Moby](../../agent/moby/).

Diese Fassung beruht auf dem Skill „Expertenmeinungen“, den Florian in der Redaktion nutzt (Stand 15.10.2026), umgebaut für verschiedene Plattformen.

Stand: 03.11.2026

## Welche Datei wofür

| Datei | Länge | Wofür |
|---|---|---|
| `SKILL.md` | rund 3.000 Wörter, 22.000 Zeichen | in einen Chat einfügen, in ein Projekt legen oder als Skill hochladen |
| `Expertenmeinungen_kurz.md` | rund 4.100 Zeichen | Kurzfassung für Anweisungsfelder mit Zeichenlimit (GPT, Le-Chat-Agent) |
| [`../zum-hochladen/expertenmeinungen.zip`](../zum-hochladen/expertenmeinungen.zip) | – | Paket zum Hochladen in Claude und Gemini |

Wie ihr den Skill einsetzt, steht in der [Anleitung](../ANLEITUNG.md).

## Voraussetzung

Ein KI-Assistent mit **Websuche**, am besten einer, der Seiten auch **öffnen** kann. Nur dann darf er wörtlich zitieren. Kann er nur suchen, gibt er die Positionen mit eigenen Worten wieder und schreibt „Snippet-Basis“ dazu. Ohne Websuche nennt er keine Namen, sondern liefert einen Suchplan.

## So fragt ihr

- „Wie schätzen Fachleute KI in der Musikproduktion ein?“ (Themen-Dossier, Standard)
- „Welche Lager gibt es in der Debatte um die Rückgabe von Kolonialobjekten?“
- „Wen kann ich zur Förderung freier Theater in Bayern anfragen?“ (Expertenliste)
- „Was sagt [Name] zur Zukunft des Stadttheaters?“ (Kurzprofil einer Person)
- „Mach daraus ein Kompakt-Briefing“ oder „eine Zitat-Tabelle“

Gemeint sind öffentliche Stimmen und ihre öffentlichen Aussagen. Private Angaben über Personen gehören nicht in den Prompt (Spielregel 2).

## Das Ergebnis lesen

- Oben steht die **Kurzantwort**, darunter die **Lage**, dann die **Debattenstränge** mit den Stimmen.
- Jede Person hat eine Nummer (E01, E02 …). Damit könnt ihr nachfragen: „E03 vertiefen“.
- **„Snippet-Basis“** heißt: Der Assistent hat nur den Suchtreffer gesehen, nicht die Seite. Ein Zitat mit diesem Vermerk ist nicht wörtlich geprüft.
- Die **Einordnung** am Ende sagt, wessen Stimmen fehlen und welches Gespräch am meisten absichern würde.
- **Öffnet die Fundstelle**, bevor ihr jemanden zitiert. Prüft auch, ob die Funktion der Person noch stimmt.
- Eine Expertin, die etwas sagt, belegt nur, dass sie es sagt. Ob es stimmt, ist eine eigene Prüfung.

## Was anders ist als in der Redaktionsfassung

- **Drei Modi statt sechs:** Themen-Dossier, Expertenliste, Positions-Kurzprofil. Das Voll-Tracking einer Person über Jahre und der Faktencheck einer Position fallen weg. Sie brauchen viele geöffnete Seiten und ein Belegregister, das in Gratis-Tools selten durchhält.
- **Eine Datei statt sieben:** Die sechs Zusatzdateien der Redaktionsfassung stehen als Text im Skill.
- **Dieselben Quellenregeln** wie in den anderen Skills dieses Repos, ergänzt um Regeln für Zitate, Mediatheken und Interessen.
- **Kein Plattformbezug:** keine Werkzeugnamen. HTML-Dossier und CSV nur, wenn euer Tool Dateien erzeugen kann.
- **Neu:** der Check zu Beginn, ob Websuche, Seitenabruf und Datum verfügbar sind, Beispiele aus der Kultur, die Regel zu Personen ohne öffentliche Rolle.
