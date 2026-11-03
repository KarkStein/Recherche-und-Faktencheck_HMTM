# Themenrecherche zum Mitnehmen

Die Themenrecherche ist ein Recherche-Skill, der in einem KI-Assistenten mit Websuche läuft. Ihr gebt ein Thema oder eine Frage ein, er sucht zuerst bei Primärquellen, belegt jeden Fakt mit Link, macht bei Streitthemen die Gegenprobe und schließt mit Quellenverzeichnis und Quellenkritik. Das ist die Arbeitsweise aus den Kapiteln 2 und 4 des Seminars.

Diese Fassung beruht auf dem Recherche-Assistenten, den Florian in der Redaktion nutzt (Stand 27.10.2026), umgebaut für verschiedene Plattformen.

Stand: 03.11.2026

## Welche Datei wofür

| Datei | Länge | Wofür |
|---|---|---|
| `SKILL.md` | rund 2.100 Wörter, 16.000 Zeichen | Langfassung: in einen Chat einfügen, in ein Projekt legen oder als Skill hochladen |
| `Themenrecherche_kurz.md` | rund 3.600 Zeichen | Kurzfassung für Anweisungsfelder mit Zeichenlimit (GPT, Le-Chat-Agent) |
| [`../zum-hochladen/themenrecherche.zip`](../zum-hochladen/themenrecherche.zip) | – | Paket zum Hochladen in Claude und Gemini |

Wenn ihr die Wahl habt, nehmt die Langfassung.

## Voraussetzung

Ein KI-Assistent, der **im Web suchen** kann, am besten auch Seiten **öffnen und lesen**. Ohne Websuche liefert der Assistent nur einen Rechercheplan und keine Fakten. Wie ihr den Skill in Chat, Projekt, als hochgeladenen Skill oder als Agent einsetzt, steht in der [Anleitung](../ANLEITUNG.md).

## So fragt ihr

Einfach das Thema oder die Frage schreiben. Beispiele:

- „Recherchiere: Wie werden freie Theater in Bayern gefördert?“
- „Kurz: Wer leitet ab 2027 das Filmfest München?“
- „Deep Dive zur Debatte um Rückgaben von Kolonialobjekten aus Münchner Museen“
- „Was ist gerade los bei [Ereignis]?“ (News-Modus)
- „Gib mir eine kommentierte Quellenliste zu [Thema]“

„Kurz“ heißt 2–3 Suchen, „Deep Dive“ 8–15, ohne Angabe 4–7.

## Das Ergebnis lesen

- Der **Kernbefund** steht oben. Darunter steht, wie belastbar er ist.
- „Eingeschränkt belegt“ heißt: nur ein Quellentyp. Das ist eine Spur, kein Fakt.
- **Öffnet die Links selbst**, vor allem bei Zahlen und Zitaten. „Snippet-Basis“ heißt: Der Assistent hat nur den Suchtreffer gesehen, nicht die Seite.
- Die **Quellenkritik** am Ende sagt, wo die Lücken sind und was ihr als Nächstes prüfen solltet.
- ⏸️ heißt: unfertig. Schreibt „weiter“, dann recherchiert er die offenen Punkte.

## Was anders ist als in der Redaktionsfassung

- **Kein Plattformbezug** und keine Verweise auf andere Skills oder Zusatzdateien.
- **Quellenregeln eingebaut**, als Kurzfassung wie bei Moby, ohne Ausschlussliste mit Namen und ohne politische Einordnung einzelner Medien.
- **Neu:** der Check zu Beginn, ob Websuche und Datum verfügbar sind, und der Hinweis auf die Pressedatenbanken der Bibliothek bei Bezahlschranken.

## Was die Themenrecherche nicht kann

- Sie kommt nicht hinter Bezahlschranken und nicht in Pressedatenbanken. Dafür gibt es den [PDB-Helfer](../pdb-helfer/) und eure Bibliothekszugänge.
- Sie ersetzt keinen Anruf. Die Quellenkritik sagt euch, welcher Anruf am meisten absichert.
- Sie prüft keinen fertigen Text. Dafür gibt es den [Faktencheck](../faktencheck/) und [Moby](../../agent/moby/).
- Sie sortiert keine Debatte nach Stimmen und Lagern. Dafür gibt es [Expertenmeinungen](../expertenmeinungen/).
