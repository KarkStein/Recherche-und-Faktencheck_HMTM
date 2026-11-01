# Moby zum Mitnehmen

Moby ist ein Faktencheck-Assistent: ein langer Prompt mit Regeln, der in einem KI-Assistenten mit Websuche läuft. Er prüft einen Text in vier Schritten (Fakten herausziehen, in Aspekte zerlegen, prüfen, Bericht) und liefert einen Bericht mit Status, Quellen und Korrekturvorschlägen. Das ist dieselbe Methode wie im Seminar, Kapitel 5b.

Diese Fassung ist für euch zum Mitnehmen. Sie beruht auf dem Moby, den Florian in der Redaktion nutzt (Stand 27.10.2026), und ist so umgebaut, dass sie auf verschiedenen Plattformen läuft.

Stand: 01.11.2026

## Welche Datei wofür

| Datei | Länge | Wofür |
|---|---|---|
| `Moby_Faktencheck.md` | rund 3.200 Wörter, 24.000 Zeichen | Langfassung: in einen Chat einfügen oder als Datei in ein Projekt legen |
| `Moby_kurz.md` | rund 4.800 Zeichen | Kurzfassung für Anweisungsfelder mit Zeichenlimit |

Wenn ihr die Wahl habt, nehmt die Langfassung. Sie enthält die Quellenregeln und Beispiele, die Kurzfassung nur das Gerüst.

## Voraussetzung

Ein KI-Assistent, der **im Web suchen** kann. Ohne Websuche erfindet ein Modell im schlimmsten Fall Quellen. Moby ist so gebaut, dass er dann ablehnt und nur die Prüfliste liefert. Noch besser ist ein Tool, das gefundene Seiten auch **öffnen und lesen** kann, nicht nur die Suchtreffer.

Ein Konto anzulegen ist freiwillig. Ohne Konto: Langfassung in einen Chat kopieren, der eine Websuche hat (welche das sind, steht in der Testtabelle der [Anleitung](../ANLEITUNG.md#getestet-oder-noch-zu-prüfen)).

## So geht's

**Überall, ohne Einrichtung**
1. Neuen Chat öffnen, Websuche einschalten, falls es dafür einen Schalter gibt.
2. Den ganzen Inhalt von `Moby_Faktencheck.md` einfügen und abschicken.
3. In der nächsten Nachricht: „Prüfe diesen Text:“ und darunter euren Text.

**Als Projekt in Claude oder ChatGPT**
1. Neues Projekt anlegen.
2. `Moby_Faktencheck.md` als Datei hochladen, oder den Inhalt in die Projektanweisungen kopieren.
3. Falls ihr die Datei hochgeladen habt, in die Anweisungen schreiben: „Arbeite immer nach der Datei Moby_Faktencheck.md. Jede Nachricht ist der zu prüfende Text.“
4. Im Projekt einen Chat starten und den Text einfügen.

**Als Gem in Gemini**
1. Neues Gem anlegen.
2. Die Kurzfassung `Moby_kurz.md` in das Anweisungsfeld kopieren. Passt die Langfassung hinein, nehmt die.
3. Gem speichern und den Text einfügen.

**Als Agent in Le Chat**
1. Neuen Agenten anlegen.
2. Kurz- oder Langfassung in die Anweisungen kopieren, Websuche aktivieren.
3. Agent im Chat aufrufen und den Text einfügen.

**Als GPT in ChatGPT:** Das Anweisungsfeld ist auf 8.000 Zeichen begrenzt, also die Kurzfassung nehmen. Ob ihr ohne Abo eigene GPTs anlegen könnt, ist nicht geprüft.

## Den Bericht lesen

- Fangt bei den kritischen Befunden an.
- Öffnet die Links selbst. Steht „Snippet“ oder „Nur Snippet-Basis“ dabei, hat Moby nur den Suchtreffer gesehen, nicht die Seite.
- Ein ✅ heißt: zwei unabhängige Quellen gefunden. Es heißt nicht, dass ihr nicht mehr nachschauen müsst.
- Die Verantwortung für euren Text bleibt bei euch.

## Was anders ist als in der Redaktionsfassung

- **Kein Plattformbezug.** Die Redaktionsfassung ist auf eine bestimmte KI-Plattform und deren Werkzeuge eingestellt (etwa wie viele Seiten pro Antwort geöffnet werden dürfen). Hier steht stattdessen: Wenn du Seiten öffnen kannst, öffne zuerst die Quellen der wichtigsten Fakten.
- **Quellenregeln eingebaut.** In der Redaktion hängt ein eigenes Quellenregelwerk als Datei an. Hier steht eine Kurzfassung direkt im Prompt.
- **Keine Ausschlussliste mit Namen.** Das Regelwerk der Redaktion nennt Medien, die nie als Quelle zählen. In dieser Fassung stehen nur die Muster, nach denen eine Quelle ausgeschlossen wird.
- **Neu:** ein Check zu Beginn, ob Websuche und Datum verfügbar sind, und ein Hinweis zu Grauzonen und absoluten Aussagen.

## Das würde Moby noch besser machen

- **Eine eigene, gepflegte Quellenliste:** welche Quellen ihr zuerst nehmt, welche nie. Baut sie für euer Fachgebiet und hängt sie als Datei an.
- **Euer eigenes Material:** Rechercheordner, Protokolle, Gesprächsnotizen, Dokumente als Dateien ins Projekt. Moby prüft dann zuerst darin.
- **Pressedatenbanken und Archive:** Moby kommt nicht hinter Bezahlschranken. Was er nicht findet, sucht ihr in der Pressedatenbank eurer Bibliothek.
- **Daten direkt:** Über MCP (Model Context Protocol) lassen sich Datenbanken und Dienste an KI-Assistenten anbinden, etwa Statistik oder Open-Data-Portale. Dann prüft der Agent gegen Primärquellen statt gegen Suchtreffer.
- **Ein Workflow statt eines einzelnen Prompts:** feste Schritte mit je eigenem Auftrag, etwa wichtige Fakten gründlich und Nebensachen schnell prüfen. Das braucht eine Plattform für Workflows.

## Was noch zu prüfen ist

Der Test in den Tools steht noch aus (geplant beim Testlauf am 03./04.11.2026). Die Testtabelle für alle vier Skills steht in der [Anleitung](../ANLEITUNG.md#getestet-oder-noch-zu-prüfen).

## Belege für die Angaben zu den Tools

- Claude Free: Websuche und bis zu fünf Projekte, laut [claude.com/pricing](https://claude.com/pricing), geöffnet am 31.10.2026.
- ChatGPT-Projekte für Free-Nutzer seit September 2025, laut [promptoptimizer.tools, 23.07.2026](https://promptoptimizer.tools/blog/how-to-use-chatgpt-projects), Drittquelle, geöffnet am 01.11.2026.
- GPT-Anweisungen höchstens 8.000 Zeichen, laut [OpenAI Developer Community, 04.06.2024](https://community.openai.com/t/how-can-i-increase-the-ceiling-for-gpt-instructions-beyond-8000-characters/801867), geöffnet am 01.11.2026. Ein neuerer Stand ist zu prüfen.
- Gems für alle ohne Abo seit 26.03.2025, laut [GoogleWatchBlog](https://www.googlewatchblog.de/2025/03/gemini-neue-kostenlose-funktion-startet-jetzt-fuer-alle-nutzer-eigene-gems-agenten-erstellen-und-nutzen/), geöffnet am 01.11.2026.
- Agents in Le Chat ohne Abo, aber mit Konto, laut Mistral-Hilfe, geprüft am 31.10.2026.
- MCP: seit 09.12.2025 Projekt der Agentic AI Foundation unter dem Dach der Linux Foundation, laut [MCP-Blog](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/), geöffnet am 01.11.2026.
