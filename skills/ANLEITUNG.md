# Anleitung: Skills einsetzen

Ein Skill ist hier ein langer Prompt mit Regeln für eine wiederkehrende Aufgabe. Ihr kopiert ihn in einen KI-Assistenten, und der arbeitet danach nach diesen Regeln. Programmieren müsst ihr dafür nichts. Stand: 01.11.2026.

## Die vier Skills

| Skill | Was er tut | Braucht Websuche? | Kapitel |
|---|---|---|---|
| [Moby](moby-faktencheck/) | prüft einen ganzen Text auf Fakten, mit Status, Quellen und Korrekturvorschlägen | ja | 5b |
| [Herkunftscheck](herkunftscheck/) | verfolgt ein Zitat, eine Zahl oder Behauptung bis zum Ursprung | ja, am besten mit Seitenabruf | 5b |
| [Themenrecherche](themenrecherche/) | recherchiert ein Thema mit Belegen, Gegenprobe und Quellenkritik | ja | 2, 4 |
| [PDB-Helfer](pdb-helfer/) | baut Suchstrings für SZ, F.A.Z., Genios/WISO und LexisNexis | hilfreich, nicht nötig | 3 |

## Welche Datei wofür

Zu Moby, Herkunftscheck und Themenrecherche gibt es eine **Langfassung** und eine **Kurzfassung** (`…_kurz.md`). Nehmt, wenn möglich, die Langfassung: Nur sie enthält die Quellenregeln mit Beispielen und alle Sonderfälle. Die Kurzfassung ist für Anweisungsfelder mit Zeichenlimit.

| Skill | Langfassung | Kurzfassung |
|---|---|---|
| Moby | 23.100 Zeichen | 4.600 Zeichen |
| Herkunftscheck | 16.100 Zeichen | 3.600 Zeichen |
| Themenrecherche | 15.400 Zeichen | 3.600 Zeichen |
| PDB-Helfer | 9.300 Zeichen | – |

## Kopieren ohne GitHub-Konto

1. Datei anklicken, etwa `moby-faktencheck/Moby_Faktencheck.md`.
2. Oben rechts über dem Text auf das Symbol mit den zwei Rechtecken klicken („Copy raw file“). Der ganze Text liegt jetzt in der Zwischenablage.
3. Alternativ „Raw“ klicken, dann alles markieren und kopieren.

Alles auf einmal: auf der Startseite des Repos grüner Knopf „Code“, dann „Download ZIP“.

## So geht's

**Überall, ohne Einrichtung**
1. Neuen Chat öffnen, Websuche einschalten, falls es dafür einen Schalter gibt.
2. Den ganzen Inhalt der Langfassung einfügen und abschicken.
3. In der nächsten Nachricht euren Auftrag: den Text zum Prüfen, das Thema, das Zitat oder die Suchanfrage.

Der Skill gilt nur in diesem Chat. Für den nächsten Auftrag öffnet ihr einen neuen Chat und fügt ihn wieder ein, oder ihr richtet ein Projekt ein.

**Als Projekt in Claude oder ChatGPT**
1. Neues Projekt anlegen, etwa „Herkunftscheck“.
2. Die Langfassung als Datei hochladen oder den Inhalt in die Projektanweisungen kopieren.
3. Falls ihr die Datei hochgeladen habt, in die Anweisungen schreiben: „Arbeite immer nach der Datei [Dateiname]. Jede Nachricht ist ein neuer Auftrag.“
4. Im Projekt einen Chat starten und loslegen. Jeder neue Chat im Projekt kennt die Regeln.

**Als Gem in Gemini**
1. Neues Gem anlegen.
2. Die Kurzfassung in das Anweisungsfeld kopieren. Passt die Langfassung hinein, nehmt die.
3. Gem speichern und loslegen.

**Als Agent in Le Chat**
1. Neuen Agenten anlegen.
2. Kurz- oder Langfassung in die Anweisungen kopieren, Websuche aktivieren.
3. Agent im Chat aufrufen und loslegen.

**Als GPT in ChatGPT:** Das Anweisungsfeld ist auf 8.000 Zeichen begrenzt, also die Kurzfassung nehmen, beim PDB-Helfer die Datei hochladen. Ob ihr ohne Abo eigene GPTs anlegen könnt, ist nicht geprüft.

Für Claude, ChatGPT, Gemini und Le Chat braucht ihr ein Konto. Ein Konto ist freiwillig. Welche Tools ohne Konto eine Websuche haben, steht in der [Tool-Liste](../ki-tools/tools.md).

## Für alle Skills gilt

- **Öffnet die Links selbst.** Steht „Snippet“ oder „Snippet-Basis“ dabei, hat der Assistent nur den Suchtreffer gesehen, nicht die Seite.
- **Ein ✅ oder 🟢 heißt nicht, dass ihr nicht mehr nachschauen müsst.** Es heißt, dass der Assistent Belege gefunden hat.
- **Keine persönlichen Daten** und nur öffentliches Material in die Prompts (Spielregeln 2 und 3).
- **Die Verantwortung für euren Text bleibt bei euch.**

## Das würde die Skills noch besser machen

- **Eine eigene Quellenliste:** welche Quellen ihr zuerst nehmt, welche nie. Baut sie für euer Fachgebiet und hängt sie als Datei an.
- **Euer eigenes Material:** Rechercheordner, Protokolle, Dokumente als Dateien ins Projekt.
- **Pressedatenbanken:** Was die Skills hinter Bezahlschranken nicht finden, sucht ihr mit dem PDB-Helfer in den Datenbanken eurer Bibliothek.
- **Daten direkt:** Über MCP (Model Context Protocol) lassen sich Datenbanken und Dienste an KI-Assistenten anbinden. Mehr dazu in [Neue KI-Tools finden](../ki-tools/neue-tools-finden.md).

## Getestet oder noch zu prüfen

Der Test in den Tools steht noch aus, geplant beim Testlauf am 03./04.11.2026. Getestet wird mit Aufgaben aus dem Seminar:

- **Moby:** der Übungstext aus Kapitel 5b. Findet er die sechs Stellen?
- **Herkunftscheck:** die zentrale Zahl aus dem Übungstext. Kommt er bis zum Originaldokument?
- **Themenrecherche:** die Leitfrage aus Kapitel 4. Nennt er Primärquellen und markiert Unbelegtes?
- **PDB-Helfer:** eine Suche nach Interviews mit einer Person im SZ-Archiv und dieselbe Suche für WISO. Läuft der String ohne Fehlermeldung?

| Tool | Zugang | Websuche | Moby | Herkunftscheck | Themenrecherche | PDB-Helfer |
|---|---|---|---|---|---|---|
| Claude (Free, mit Konto) | zu prüfen | zu prüfen | | | | |
| ChatGPT ohne Konto | zu prüfen | zu prüfen | | | | |
| ChatGPT-Projekt (Free, mit Konto) | zu prüfen | zu prüfen | | | | |
| Gemini-Gem (mit Konto) | zu prüfen | zu prüfen | | | | |
| Le Chat-Agent (mit Konto) | zu prüfen | zu prüfen | | | | |
| Perplexity ohne Konto | zu prüfen | zu prüfen | | | | |
| Lumo als Gast | zu prüfen | zu prüfen | | | | |

Pro Zelle: läuft / läuft mit Einschränkung / läuft nicht, und ein Stichwort.

## Belege für die Angaben zu den Tools

- Claude Free: Websuche und bis zu fünf Projekte, laut [claude.com/pricing](https://claude.com/pricing), geöffnet am 31.10.2026.
- ChatGPT-Projekte für Free-Nutzer seit September 2025, laut [promptoptimizer.tools, 23.07.2026](https://promptoptimizer.tools/blog/how-to-use-chatgpt-projects), Drittquelle, geöffnet am 01.11.2026.
- GPT-Anweisungen höchstens 8.000 Zeichen, laut [OpenAI Developer Community, 04.06.2024](https://community.openai.com/t/how-can-i-increase-the-ceiling-for-gpt-instructions-beyond-8000-characters/801867), geöffnet am 01.11.2026. Ein neuerer Stand ist zu prüfen.
- Gems für alle ohne Abo seit 26.03.2025, laut [GoogleWatchBlog](https://www.googlewatchblog.de/2025/03/gemini-neue-kostenlose-funktion-startet-jetzt-fuer-alle-nutzer-eigene-gems-agenten-erstellen-und-nutzen/), geöffnet am 01.11.2026.
- Agents in Le Chat ohne Abo, aber mit Konto, laut Mistral-Hilfe, geprüft am 31.10.2026.
