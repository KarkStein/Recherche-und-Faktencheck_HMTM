# Skills und Moby: Überblick und Anleitung

Ein Skill ist ein Text mit Anweisungen und Regeln für eine Aufgabe, die immer wiederkommt, etwa einen Text auf Fakten prüfen. Jeder Skill liegt in einem eigenen Ordner, in der Datei `SKILL.md`. Oben in der Datei steht, wofür der Skill zuständig ist. Tools, die Skills kennen, laden ihn dann von selbst, sobald eure Frage passt. Alle anderen Tools bekommen denselben Text zum Einfügen. Programmieren müsst ihr dafür nichts.

## Die sechs Skills und Moby

| | Was er tut | Braucht Websuche? | Kapitel |
|---|---|---|---|
| [Faktencheck](faktencheck/) | prüft einen Text oder eine einzelne Behauptung, trennt widerlegt und nicht belegt | ja | 5 |
| [Herkunftscheck](herkunftscheck/) | verfolgt ein Zitat, eine Zahl oder Behauptung bis zum Ursprung | ja, am besten mit Seitenabruf | 5 |
| [Themenrecherche](themenrecherche/) | recherchiert ein Thema mit Belegen, Gegenprobe und Quellenkritik | ja | 2, 4 |
| [Expertenmeinungen](expertenmeinungen/) | sortiert eine Debatte: Lager, Stimmen, Konsens und Streit, jede Position belegt | ja, am besten mit Seitenabruf | 4 |
| [PDB-Helfer](pdb-helfer/) | baut Suchstrings für SZ, F.A.Z., Genios/WISO und LexisNexis | hilfreich, nicht nötig | 3 |
| [Prompthelfer](prompthelfer/) | schreibt mit euch Prompts, Agenten-Aufträge und eigene Skills für ein selbst gewähltes Thema | nein | 4 |
| [Moby](../agent/moby/) (Assistent) | prüft einen ganzen Text, in einem eigenen Projekt, GPT oder Agenten | ja | 5 |

Faktencheck und Moby prüfen nach derselben Methode. Den Unterschied erklärt die [Seite zum Faktencheck](faktencheck/README.md#faktencheck-oder-moby).

## Welche Datei wofür

In jedem Skill-Ordner liegen die `SKILL.md` und eine README, die erklärt, was der Skill kann und wie ihr ihn fragt. Die Pakete zum Hochladen liegen gesammelt im Ordner [`zum-hochladen`](zum-hochladen/).

Die `SKILL.md` ist die Langfassung: zum Einfügen in einen Chat, als Datei für ein Projekt und als Inhalt des Pakets zum Hochladen. Der Kopf oben mit `name` und `description` stört beim Einfügen nicht.

| | Langfassung | Kurzfassung | Paket zum Hochladen |
|---|---|---|---|
| Faktencheck | [`SKILL.md`](faktencheck/SKILL.md), 20.500 Zeichen | – (nehmt [Moby kurz](../agent/moby/Moby_kurz.md)) | [`faktencheck.zip`](zum-hochladen/faktencheck.zip) |
| Herkunftscheck | [`SKILL.md`](herkunftscheck/SKILL.md), 16.700 Zeichen | [3.600 Zeichen](herkunftscheck/Herkunftscheck_kurz.md) | [`herkunftscheck.zip`](zum-hochladen/herkunftscheck.zip) |
| Themenrecherche | [`SKILL.md`](themenrecherche/SKILL.md), 16.000 Zeichen | [3.600 Zeichen](themenrecherche/Themenrecherche_kurz.md) | [`themenrecherche.zip`](zum-hochladen/themenrecherche.zip) |
| Expertenmeinungen | [`SKILL.md`](expertenmeinungen/SKILL.md), 22.000 Zeichen | [4.100 Zeichen](expertenmeinungen/Expertenmeinungen_kurz.md) | [`expertenmeinungen.zip`](zum-hochladen/expertenmeinungen.zip) |
| PDB-Helfer | [`SKILL.md`](pdb-helfer/SKILL.md), 9.900 Zeichen | – | [`pdb-helfer.zip`](zum-hochladen/pdb-helfer.zip) |
| Prompthelfer | [`SKILL.md`](prompthelfer/SKILL.md), 17.000 Zeichen | [5.200 Zeichen](prompthelfer/Prompthelfer_kurz.md) | [`prompthelfer.zip`](zum-hochladen/prompthelfer.zip) |
| Moby | [`Moby_Faktencheck.md`](../agent/moby/Moby_Faktencheck.md), 23.100 Zeichen | [4.600 Zeichen](../agent/moby/Moby_kurz.md) | – |

Nehmt, wenn möglich, die Langfassung: Nur sie enthält die Quellenregeln mit Beispielen und alle Sonderfälle. Die Kurzfassung ist für Anweisungsfelder mit Zeichenlimit.

## Kopieren und herunterladen ohne GitHub-Konto

1. Datei anklicken, etwa `herkunftscheck/SKILL.md`.
2. Oben rechts über dem Text auf das Symbol mit den zwei Rechtecken klicken („Copy raw file“). Der ganze Text liegt jetzt in der Zwischenablage.
3. Alternativ „Raw“ klicken, dann alles markieren und kopieren.

Ein Paket herunterladen: im Ordner [`zum-hochladen/`](zum-hochladen/) die ZIP-Datei anklicken, dann oben rechts auf den Pfeil nach unten („Download raw file“).

Alles auf einmal: auf der Startseite des Repos grüner Knopf „Code“, dann „Download ZIP“.

## So geht's

**Überall, ohne Einrichtung**
1. Neuen Chat öffnen, Websuche einschalten, falls es dafür einen Schalter gibt.
2. Den ganzen Inhalt der `SKILL.md` einfügen und abschicken.
3. In der nächsten Nachricht euren Auftrag: den Text zum Prüfen, das Thema, das Zitat oder die Suchanfrage.

Der Skill gilt nur in diesem Chat. Für den nächsten Auftrag öffnet ihr einen neuen Chat und fügt ihn wieder ein, oder ihr richtet ihn dauerhaft ein (siehe unten).

**Als Skill in Claude** (Konto nötig, geht auch gratis)
1. Code-Ausführung einschalten: in den Einstellungen unter „Capabilities“. Skills brauchen sie, auch wenn diese Skills selbst keinen Code ausführen.
2. Das Paket herunterladen, etwa `herkunftscheck.zip`. Nicht entpacken.
3. In Claude: „Customize“, dann „Skills“, auf „+“ klicken, „Create skill“, „Upload a skill“, die ZIP-Datei wählen.
4. Den Skill eingeschaltet lassen. Ab jetzt startet er in jedem Chat von selbst, wenn eure Frage passt. Ihr könnt ihn auch beim Namen rufen: „Nutze den Herkunftscheck.“

**Als Skill in Gemini** (Google-Konto ab 18, in der Web-App oder der Mac-App)

Gems werden am 17.11.2026 schreibgeschützt und am 17.12.2026 gelöscht. An ihre Stelle treten Skills.
1. In Gemini in der Seitenleiste „Customize“, dann „Skills“, dann „Create“ und „Create manually“.
2. Name: der `name` aus dem Kopf der `SKILL.md`, etwa `herkunftscheck`. Beschreibung: der Text hinter `description`. Anweisungen: alles unter dem Kopf.
3. Speichern und im Chat loslegen.

Statt von Hand könnt ihr den Skill auch hochladen: Paket herunterladen und entpacken, dann bei einem angelegten Skill über „More options“ und „Replace skill“ den entpackten Ordner wählen. Der Ordner muss genauso heißen wie der Skill. Die Menünamen stammen aus der englischen Google-Hilfe, in der deutschen Oberfläche können sie anders heißen.

**Als Projekt in Claude oder ChatGPT**
1. Neues Projekt anlegen, etwa „Herkunftscheck“.
2. Die `SKILL.md` als Datei hochladen oder den Inhalt in die Projektanweisungen kopieren.
3. Falls ihr die Datei hochgeladen habt, in die Anweisungen schreiben: „Arbeite immer nach der Datei SKILL.md. Jede Nachricht ist ein neuer Auftrag.“
4. Im Projekt einen Chat starten und loslegen. Jeder neue Chat im Projekt kennt die Regeln.

**Als Agent in Le Chat**
1. Neuen Agenten anlegen.
2. Kurz- oder Langfassung in die Anweisungen kopieren, Websuche aktivieren.
3. Agent im Chat aufrufen und loslegen.

**Als GPT in ChatGPT:** Das Anweisungsfeld ist auf 8.000 Zeichen begrenzt, also die Kurzfassung nehmen, beim Faktencheck und beim PDB-Helfer die Datei hochladen. Ob ihr ohne Abo eigene GPTs anlegen könnt, ist nicht geprüft. Skills zum Hochladen gibt es in ChatGPT laut OpenAI bisher nur in Business, Enterprise und Edu.

**In Programmier-Werkzeugen** wie Claude Code, Gemini CLI oder GitHub Copilot: Diese Werkzeuge lesen Skill-Ordner mit `SKILL.md` direkt. Den entpackten Ordner in den Skill-Ordner des Werkzeugs legen.

Für Claude, ChatGPT, Gemini und Le Chat braucht ihr ein Konto. Ein Konto ist freiwillig. Welche Tools ohne Konto eine Websuche haben, steht in der [Tool-Liste](../tools/tools.md).

## Skills sind Text: erst lesen, dann hochladen

- Die Skills in diesem Repo sind reiner Text, ohne Skripte oder Programme. In jeder ZIP-Datei liegt nur die `SKILL.md`, die ihr hier lesen könnt.
- Fremde Skills lest ihr vor dem Hochladen. Ein Skill kann Anweisungen und Skripte enthalten, die euer Assistent dann befolgt oder ausführt. Im Juli 2026 zählte die Sicherheitsfirma Island über 800 gefälschte GitHub-Repos, die sich als KI-Skills oder MCP-Server tarnten und Schadsoftware verbreiteten. Mehr dazu in [Neue KI-Tools finden](../tools/neue-tools-finden.md).

## Für alle Skills gilt

- **Öffnet die Links selbst.** Steht „Snippet“ oder „Snippet-Basis“ dabei, hat der Assistent nur den Suchtreffer gesehen, nicht die Seite.
- **Ein ✅ oder 🟢 heißt nicht, dass ihr nicht mehr nachschauen müsst.** Es heißt, dass der Assistent Belege gefunden hat.
- **Keine persönlichen Daten** und nur öffentliches Material in die Prompts.
- **Die Verantwortung für euren Text bleibt bei euch.**

## Das würde die Skills noch besser machen

- **Eine eigene Quellenliste:** welche Quellen ihr zuerst nehmt, welche nie. Baut sie für euer Fachgebiet und hängt sie als Datei an.
- **Euer eigenes Material:** Rechercheordner, Protokolle, Dokumente als Dateien ins Projekt.
- **Pressedatenbanken:** Was die Skills hinter Bezahlschranken nicht finden, sucht ihr mit dem PDB-Helfer in den Datenbanken eurer Bibliothek.
- **Daten direkt:** Über MCP (Model Context Protocol) lassen sich Datenbanken und Dienste an KI-Assistenten anbinden. Mehr dazu in [Neue KI-Tools finden](../tools/neue-tools-finden.md).
- **Ein Ablauf statt eines einzelnen Prompts:** feste Schritte mit je eigenem Auftrag, etwa wichtige Fakten gründlich und Nebensachen schnell prüfen. Das braucht eine Plattform für solche Abläufe (Workflows).
- **Euer eigener Skill:** Was ihr zum zweiten Mal genauso macht, ist ein Skill. Ordner anlegen, darin eine `SKILL.md` mit `name` und `description` im Kopf und euren Regeln darunter. Die Skills hier sind Vorlagen dafür, ein leeres Gerüst liegt beim [Prompthelfer](prompthelfer/Vorlage_Skill.md), und der Prompthelfer baut einen Skill auch mit euch.

## Erst testen, dann nutzen

Nicht jeder Skill läuft in jedem Tool gleich gut. Probiert einen Skill zuerst mit einer Aufgabe aus, deren Ergebnis ihr kennt, etwa aus dem Seminar:

- **Moby und Faktencheck:** der Übungstext aus Kapitel 5. Finden sie alle Fehler, und wo kommen sie ohne PDF nicht weiter?
- **Herkunftscheck:** die zentrale Zahl aus dem Übungstext. Kommt er bis zum Originaldokument?
- **Themenrecherche:** die Leitfrage aus Kapitel 4. Nennt er Primärquellen und markiert Unbelegtes?
- **Expertenmeinungen:** eine Kulturdebatte, etwa KI in der Musikproduktion. Leitet er die Lager aus den Treffern ab, hat jede Stimme eine Fundstelle, sind Snippets markiert?
- **PDB-Helfer:** eine Suche nach Interviews mit einer Person im SZ-Archiv und dieselbe Suche für WISO. Läuft der String ohne Fehlermeldung?
- **Prompthelfer:** ein selbst gewähltes Thema. Fragt er nach, bevor er schreibt? Steht der Prompt kopierfertig im Kasten, und läuft er in einem neuen Chat?
- **Hochladen:** Nimmt euer Tool das Paket an, und startet der Skill von selbst, ohne dass ihr ihn nennt?

Notiert euch pro Tool: läuft, läuft mit Einschränkung oder läuft nicht, und ein Stichwort, warum.

Ob Skills in Gemini den gespeicherten Verlauf voraussetzen, ist nicht geklärt. Ein Blog behauptet es, die Google-Hilfe sagt dazu nichts.

## Belege für die Angaben zu den Tools

- Claude Free: Websuche und bis zu fünf Projekte, laut [claude.com/pricing](https://claude.com/pricing), geöffnet am 31.10.2026.
- Skills in Claude für Free, Pro, Max, Ultra, Team und Enterprise, Code-Ausführung nötig, Hochladen als ZIP unter Customize > Skills, laut [Claude-Hilfe](https://support.claude.com/en/articles/12512180-use-skills-in-claude), geöffnet am 03.11.2026.
- Gems ab 17.11.2026 schreibgeschützt, ab 17.12.2026 entfernt; Skills für Personen ab 18 mit privatem Google-Konto; Hochladen nur in der Web-App und der Mac-App; Ordnername gleich Skillname, klein mit Bindestrich; höchstens 100 MB, laut [Gemini-Hilfe](https://support.google.com/gemini/answer/18560919?hl=en), geöffnet am 03.11.2026.
- Skills in ChatGPT für Business, Enterprise, Healthcare und Edu, laut [OpenAI-Hilfe](https://help.openai.com/en/articles/20001066-skills-in-chatgpt), übernommen aus dem Suchtreffer; die Seite war am 03.11.2026 nicht abrufbar.
- ChatGPT-Projekte für Free-Nutzer seit September 2025, laut [promptoptimizer.tools, 23.07.2026](https://promptoptimizer.tools/blog/how-to-use-chatgpt-projects), Drittquelle, geöffnet am 01.11.2026.
- GPT-Anweisungen höchstens 8.000 Zeichen, laut [OpenAI Developer Community, 04.06.2024](https://community.openai.com/t/how-can-i-increase-the-ceiling-for-gpt-instructions-beyond-8000-characters/801867), geöffnet am 01.11.2026. Ein neuerer Stand ist zu prüfen.
- Agents in Le Chat ohne Abo, aber mit Konto, laut Mistral-Hilfe, geprüft am 31.10.2026. Skills im Ordnerformat: in einer Websuche am 03.11.2026 kein Beleg gefunden.
- Programmier-Werkzeuge mit Skill-Ordnern, etwa die [Gemini CLI](https://geminicli.com/docs/cli/skills): übernommen, nicht geöffnet.
