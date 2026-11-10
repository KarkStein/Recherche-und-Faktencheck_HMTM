# KI-Tools für die Recherche: alle mit Link

Dieselben Tools wie auf dem [Spickzettel](spickzettel.pdf) (Kapitel 4 und 6), hier als Linkliste. Stand der Angaben zu Zugang und Preisen: 01.11.2026, ohne Gewähr.

**Prüfstufe:** übernommen vom Spickzettel, dessen Angaben zu Zugang und Preisen am 31.10.2026 geprüft wurden. Offenes steht als „zu prüfen“ dabei.

° Zugang ändert sich gerade, vor Ort ausprobieren.

## Welches Tool wofür

| Aufgabe | ohne Konto | mit Konto |
|---|---|---|
| schnell nachschlagen, mit Quellen | Perplexity, KI-Modus der Google-Suche°, Ask Brave | – |
| Überblick über ein Thema | – | Gemini Deep Research, Claude Research (Pro) |
| eigene Dokumente befragen | – | Gemini Notebook, Claude-Projekt |
| große Dokumentenstapel durchsuchen | öffentliche Pinpoint-Sammlungen° | Pinpoint |
| Interviews transkribieren | noScribe (läuft lokal), Whisper im Browser° | TurboScribe, Pinpoint |
| Studien finden | – | Scholar Labs, Consensus |
| fremdsprachige Quellen lesen | DeepL (mit Limit) | DeepL mit mehr Umfang |
| Gegenargumente, Interviewfragen | Duck.ai, Lumo | Claude, Le Chat, Euria |
| veröffentlichte Faktenchecks finden | Fact Check Explorer° | – |
| vertrauliches Material | noScribe, sonst nichts hochladen | – |

## Vier Fragen an jedes KI-Tool

Das Pult aus Kapitel 4: Mit diesen vier Fragen ordnet ihr jedes Tool ein, auch neue.

1. **Modell und Denkzeit:** Wie stark ist das Modell, wie lange denkt es nach?
2. **Zugriff:** Welche Quellen sind offen? Gedächtnis, offenes Web, eure Dateien, eure Dienste.
3. **Auftrag:** Wie strukturiert ist euer Input? Frage, Prompt oder Skill.
4. **Selbstständigkeit:** Wer bestimmt den nächsten Schritt, und verändert die KI etwas? Wenn sie handelt, nur mit eurer Freigabe.

## Eigene Daten: hochladen oder verbinden

Aus Kapitel 4 der Seminarfolien, Prüfstufe **übernommen**.

- **Hochladen:** Eine Kopie geht an den Anbieter, etwa eine PDF im Chat, im Projekt oder im Gemini Notebook. Das Modell liest nur, was ihr hineingebt.
- **Verbinden:** Integrationen geben dem Modell Zugriff auf einen Dienst wie Google Drive, Mail, Kalender oder GitHub. Bei Claude heißen sie Konnektoren, bei ChatGPT Apps. Das geht schon im normalen Chat und braucht immer ein Konto. Vorsicht vor versteckten Anweisungen in Mails.
- **Für beides gilt:** Nur hochladen und verbinden, was auch öffentlich sein dürfte.

**MCP, der Stecker für KI:** ein offener Standard, mit dem KI-Anwendungen Daten, Werkzeuge und Abläufe anderer Systeme anschließen. Ein Dienst baut einmal einen MCP-Server, dann passt er in Claude, ChatGPT, Gemini, Copilot und andere. Im November 2024 von Anthropic vorgestellt, seit Dezember 2025 bei der Linux Foundation. Ein Beispiel: Mit einem MCP-Server für das Guardian-Archiv durchsucht ein KI-Modell 1,9 Millionen Artikel, ein Prototyp, nicht vom Guardian selbst ([Nieman Lab, 01.07.2025](https://www.niemanlab.org/2025/07/a-new-tool-lets-your-favorite-ai-model-talk-with-1-9-million-articles-in-the-guardian/)). **Vorsicht:** Ein MCP-Server ist fremder Code mit Zugang zu euren Daten, und in seinen Beschreibungen lassen sich Anweisungen verstecken. Wie gefälschte Server auftauchen, steht in [Neue KI-Tools finden](neue-tools-finden.md).

**Website-Chatbots** bei Onlineshops, Banken oder Behörden suchen oft wie ein Notebook in einem festen Bestand: FAQ, Hilfeseiten, Merkblätter. Den Bestand wählt aber der Betreiber aus, nicht ihr. Ihr seht die Quellen meist nicht, und der Bot vertritt die Interessen des Betreibers.

## Alle Tools

### Suchen mit KI-Antwort

| Tool | Was es kann | Zugang | Adresse |
|---|---|---|---|
| KI-Modus (Google) | Antwort mit Fußnoten in der Google-Suche | ohne Konto°; ob ein Login nötig ist, zu prüfen | [google.com](https://www.google.com/), Reiter „KI-Modus“ |
| Perplexity | Suchmaschine, die mit nummerierten Quellen antwortet | Basissuche ohne Konto | [perplexity.ai](https://www.perplexity.ai/) |
| Ask Brave | KI-Antworten aus Braves eigenem Suchindex | kostenlos | [search.brave.com](https://search.brave.com/) |
| Ecosia | KI-Übersicht über den Treffern und KI-Chat | ohne Konto | [ecosia.org](https://www.ecosia.org/) |

### Chat-Assistenten

| Tool | Was es kann | Zugang | Adresse |
|---|---|---|---|
| Duck.ai | mehrere Sprachmodelle im Vergleich, Verlauf nur im Browser | ohne Konto; ob mit Websuche, zu prüfen | [duck.ai](https://duck.ai/) |
| Lumo (Proton) | Chat mit Websuche, wirbt mit Datenschutz | ohne Konto | [lumo.proton.me](https://lumo.proton.me/) |
| Le Chat (Mistral) | französischer Anbieter, Daten in der EU, auch Deep Research | Konto für mehr Funktionen° | [chat.mistral.ai](https://chat.mistral.ai/) |
| Euria (Infomaniak) | Assistent aus der Schweiz, laut Anbieter kein Training mit euren Daten | kostenloses Konto | [infomaniak.com/de/euria](https://www.infomaniak.com/de/euria) |
| Claude | lange Dokumente, Projekte mit festen Regeln | Konto mit E-Mail; Pro 17–20 $ im Monat | [claude.ai](https://claude.ai/) |
| ChatGPT | Multitool mit Websuche | Konto; gratis mit Werbung | [chatgpt.com](https://chatgpt.com/) |
| Copilot | in Bing, Edge, Windows und Office eingebaut | nur mit Login | [copilot.microsoft.com](https://copilot.microsoft.com/) |

### Recherche im Auftrag

| Tool | Was es kann | Zugang | Adresse |
|---|---|---|---|
| Gemini Deep Research | plant, sucht in Schleifen, schreibt einen Bericht mit Quellen | Google-Konto ab 18, mit Limit | [gemini.google.com](https://gemini.google.com/) |
| Claude Research | viele Suchen, ein Bericht mit Quellen | nur Pro | [claude.ai](https://claude.ai/), über „+“ |

### Eigene Dokumente befragen

| Tool | Was es kann | Zugang | Adresse |
|---|---|---|---|
| Gemini Notebook (früher NotebookLM) | Gespräch mit wenigen Quellen, zeigt die Belegstelle | Google-Konto, 50 Quellen je Notebook | [notebooklm.google.com](https://notebooklm.google.com/) |
| Pinpoint | Archiv mit Suchmaschine für große Stapel, Index von Personen und Orten, transkribiert Audio | öffentliche Sammlungen ohne Konto°; eigene mit Google-Konto ab 18 | [journaliststudio.google.com/pinpoint](https://journaliststudio.google.com/pinpoint) |
| Claude-Projekt | Anweisungen und Dateien, die jeder Chat im Projekt kennt | Konto, 5 Projekte gratis | [claude.ai](https://claude.ai/) |

### Transkription

| Tool | Was es kann | Zugang | Adresse |
|---|---|---|---|
| noScribe | transkribiert auf dem eigenen Rechner, offline, Open Source | kostenlos, installieren | [github.com/kaixxx/noScribe](https://github.com/kaixxx/noScribe) |
| Whisper im Browser | transkribiert im Browser, Datei oder Mikrofon; eine Demo der webml-community auf Hugging Face. Ob lokal, ist ungeprüft: Vertrauliches nur mit noScribe | ohne Konto° | [huggingface.co/spaces/webml-community/whisper-large-v3-turbo-webgpu](https://huggingface.co/spaces/webml-community/whisper-large-v3-turbo-webgpu) |
| TurboScribe | Transkription im Browser, Freemium | Konto, kostenlos mit Limit | [turboscribe.ai](https://turboscribe.ai/) |

**Whisper im Browser:** Die Seite (geöffnet am 01.11.2026) sagt, die Spracherkennung laufe „directly in your browser“. Ob die Aufnahme dabei sicher auf eurem Rechner bleibt, steht dort nicht ausdrücklich: zu prüfen. Der Name verweist auf WebGPU, also braucht ihr vermutlich einen aktuellen Browser mit WebGPU-Unterstützung. Für vertrauliches Material bleibt noScribe die sichere Wahl.

**Achtung bei noScribe:** Die Seite noscribe.ai gehört nicht zum Projekt. Laut README des Projekts (geöffnet am 01.11.2026) ist die neue offizielle Website noscribe.de, die Downloads verlinkt die README. Ladet das Programm nur über diese Wege.

### Studien und Übersetzen

| Tool | Was es kann | Zugang | Adresse |
|---|---|---|---|
| Scholar Labs | KI-Suche in Google Scholar, sagt, warum ein Aufsatz passt | Google-Konto, experimentell | [scholar.google.com](https://scholar.google.com/) |
| Consensus | fasst den Forschungsstand aus über 220 Mio. Fachartikeln zusammen | Konto, 10 Analysen im Monat | [consensus.app](https://consensus.app/) |
| DeepL | Übersetzer für fremdsprachige Quellen | ohne Konto mit Limit | [deepl.com](https://www.deepl.com/) |

### Faktenchecks finden

| Tool | Was es kann | Zugang | Adresse |
|---|---|---|---|
| Fact Check Explorer (Google) | durchsucht veröffentlichte Faktenchecks vieler Redaktionen | Suche ohne Konto°, geöffnet am 01.11.2026 | [toolbox.google.com/factcheck/explorer](https://toolbox.google.com/factcheck/explorer) |

### Vorsicht

| Tool | Was es kann | Zugang | Hinweis |
|---|---|---|---|
| DeepSeek | starke Modelle aus China; die Berliner Datenschutzbeauftragte hält die App für rechtswidrig | nur unkritische Fragen | chat.deepseek.com |
| KI-Browser (Comet, ChatGPT Atlas) | ein Agent klickt für euch; versteckte Anweisungen auf Webseiten können ihn fremdsteuern | nicht mit euren Konten | nur ansehen |

Auch eine Download-Adresse ist eine Quelle: Programme nur von der Seite des Projekts laden. Wie ihr neue Tools findet und prüft, steht in [Neue KI-Tools finden](neue-tools-finden.md).
