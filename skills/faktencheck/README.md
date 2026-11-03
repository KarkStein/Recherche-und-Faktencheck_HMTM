# Faktencheck zum Mitnehmen

Der Faktencheck prüft einen Text oder eine einzelne Behauptung auf Faktentreue. Er zieht die prüfbaren Fakten heraus, sucht Belege und unterscheidet genau: **widerlegt** (❌) ist etwas anderes als **nicht belegt** (⭕) oder **nicht prüfbar** (❓). Bevor er „nicht belegt“ sagen darf, muss er sechs Rechercherouten durchlaufen. Jede Abweichung bewertet er mit dem Schadentest: Wie sehr schadet sie dem Text? Passt zu Kapitel 5b des Seminars.

Diese Fassung beruht auf dem Faktencheck-Skill, den Florian in der Redaktion nutzt (Version 3.0, Stand 15.10.2026), umgebaut für verschiedene Plattformen.

Stand: 03.11.2026

## Faktencheck oder Moby?

Beide prüfen nach derselben Methode wie im Seminar. Der Unterschied liegt darin, wie ihr sie einsetzt:

| | [Moby](../../agent/moby/) | Faktencheck |
|---|---|---|
| Was es ist | ein Assistent mit eigenem Raum: Projekt, GPT oder Le-Chat-Agent | ein Skill, der in einem normalen Chat von selbst startet, wenn ihr um eine Prüfung bittet |
| Was ihr schickt | jede Nachricht ist der Prüftext | „Prüfe diesen Text: …“ oder „Stimmt es, dass …?“ |
| Einzelne Behauptung | prüft sie wie einen Text | eigener Kurzcheck mit kompakter Antwort |
| Status | ❌ heißt falsch oder nicht belegt | ❌ widerlegt und ⭕ nicht belegt sind getrennt |
| Am besten in | Claude-Projekt, ChatGPT-Projekt, GPT, Le-Chat-Agent | Claude und Gemini als hochgeladener Skill, sonst überall zum Einfügen |

In Gemini gibt es ab dem 17.11.2026 keine neuen Gems mehr. Dort nehmt ihr den Faktencheck als Skill.

## Welche Datei wofür

| Datei | Länge | Wofür |
|---|---|---|
| `SKILL.md` | rund 2.800 Wörter, 20.500 Zeichen | in einen Chat einfügen, in ein Projekt legen oder als Skill hochladen |
| [`../zum-hochladen/faktencheck.zip`](../zum-hochladen/faktencheck.zip) | – | Paket zum Hochladen in Claude und Gemini |

Eine Kurzfassung gibt es nicht. Für Anweisungsfelder mit Zeichenlimit nehmt die [Kurzfassung von Moby](../../agent/moby/Moby_kurz.md). Wie ihr den Skill einsetzt, steht in der [Anleitung](../ANLEITUNG.md).

## Voraussetzung

Ein KI-Assistent, der **im Web suchen** kann, am besten auch Seiten **öffnen und lesen**. Ohne Websuche liefert der Faktencheck nur die Liste der Fakten, die zu prüfen wären, und vergibt keinen Status.

## So fragt ihr

- „Prüfe diesen Text:“ und darunter euer Text
- „Faktencheck für diesen Artikel“ und darunter der Link
- „Stimmt es, dass Theater in Deutschland mehr Zuschauer haben als die Fußball-Bundesliga?“ (Kurzcheck)

## Das Ergebnis lesen

| Symbol | heißt |
|---|---|
| ✅ | zwei unabhängige Quellen gefunden, bei wichtigen Fakten eine davon gelesen |
| ⚠️ | Abweichung im Detail |
| ❌ | widerlegt: Eine belastbare Quelle zeigt das Gegenteil |
| ⭕ | nicht belegt: kein Beleg und kein Gegenbeleg, nach allen Rechercherouten |
| ❓ | nicht prüfbar, etwa weil Fachwissen oder ein Archivzugang fehlt |
| ⏰ | veraltet: stimmte zum Textdatum, hat sich seither geändert |
| ⏸️ | noch nicht geprüft. Schreibt „weiter“ |
| 🔴S / 🟡N | schwerwiegend / nicht gravierend, laut Schadentest |

- Fangt bei den **kritischen Befunden** an.
- **Öffnet die Links selbst.** „Snippet-Basis“ heißt: Der Assistent hat nur den Suchtreffer gesehen, nicht die Seite.
- Ein ✅ heißt nicht, dass ihr nicht mehr nachschauen müsst. Die Verantwortung für euren Text bleibt bei euch.

## Was anders ist als in der Redaktionsfassung

- **Quellenregeln eingebaut** als Kurzfassung, wie bei Moby. In der Redaktion hängt ein eigenes Regelwerk als Datei an.
- **Kein Plattformbezug:** keine Werkzeugnamen, keine festen Abrufzahlen, keine Übergabe an andere Assistenten.
- **Neu:** der Check zu Beginn, ob Websuche, Seitenabruf und Datum verfügbar sind, die Hinweise zu Zuschreibungen, Bezugsgrößen und absoluten Aussagen aus Moby, Korrekturvorschläge und Zählprobe.
