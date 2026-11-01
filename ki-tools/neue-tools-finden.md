# Neue KI-Tools finden und prüfen

Fast jede Woche kommt ein neues KI-Werkzeug dazu. Viele nützliche Recherche-Tools sind Open-Source-Projekte auf GitHub, etwa noScribe, OpenRefine oder Aleph, oder kleine Demos auf Hugging Face. Dort zu stöbern geht fast überall ohne Konto und ohne Programmieren. Ausprobieren oder installieren solltet ihr ein Tool aber erst nach der [Prüfliste](#bevor-ihr-etwas-ausprobiert-die-prüfliste).

Gehört zu Kapitel 6.2 des Seminars. Stand: 01.11.2026. Alle Links sind **geöffnet am 01.11.2026**, sofern nicht anders vermerkt. Zahlen wie Sterne und Repos sind Momentaufnahmen von diesem Tag.

## Wo neue KI-Tools auftauchen: fünf Wege

Vom einfachsten zum technischsten.

| Weg | Was ihr dort findet | Ohne Konto? | Einstieg |
|---|---|---|---|
| **1. Werkzeugkästen von Rechercheprofis** | Tools mit Einordnung: Kosten, Anforderungen, Grenzen, Ethik. Gepflegt von Menschen, die die Tools selbst nutzen | ja | [Bellingcat Online Investigations Toolkit](https://bellingcat.gitbook.io/toolkit): 12 Kategorien, jedes Tool als kostenlos, teilweise kostenlos oder bezahlt markiert. [awesome-osint](https://github.com/jivoi/awesome-osint) mit dem Abschnitt „Fact Checking“ |
| **2. GitHub stöbern** | **Trending:** was gerade Aufmerksamkeit bekommt, filterbar nach gesprochener Sprache, Programmiersprache und Zeitraum. **Topics:** Schlagwort-Seiten, sortierbar nach „Recently updated“ | ja | [Trending](https://github.com/trending); Topics [fact-checking](https://github.com/topics/fact-checking) (1.026 Repos), [journalism](https://github.com/topics/journalism) (968), [osint](https://github.com/topics/osint) |
| **3. awesome-Listen** | von Menschen gepflegte Linklisten zu einem Thema | ja | [sindresorhus/awesome](https://github.com/sindresorhus/awesome), die Liste aller Listen (rund 528.000 Sterne); durchsuchbar über [awesome.ecosyste.ms](https://awesome.ecosyste.ms/) |
| **4. Hugging Face Spaces** | KI-Demos direkt im Browser, nach Kategorien wie OCR, Document Analysis, Text Summarization, Speech Synthesis | ja, mit Limit: ohne Konto 2 Minuten Rechenzeit (GPU) am Tag, mit Gratis-Konto 5 Minuten | [Spaces](https://huggingface.co/spaces); [Journalists on Hugging Face](https://journalistsonhf-readme.static.hf.space) mit einem AI Toolkit für Redaktionen |
| **5. Verzeichnisse für Skills und MCP-Server** (Ausblick) | Bausteine, die KI-Assistenten neue Fähigkeiten geben, etwa Zugriff auf Datenbanken | lesen ja, nutzen meist nur mit Entwickler-Werkzeugen | [skills.sh](https://skills.sh) (von Vercel); [offizielle MCP-Registry](https://registry.modelcontextprotocol.io) (seit 08.09.2025 in der Preview, ohne Vorabprüfung); [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) (rund 97.000 Sterne) |

Dazu kommen Communitys, in denen Leute ihre Projekte selbst vorstellen, etwa [Show HN](https://news.ycombinator.com/show) auf Hacker News, ohne Konto lesbar.

**Merksatz: Trending heißt beliebt, nicht seriös.** Bei Hugging Face standen am 01.11.2026 unter den zehn meistbeachteten Spaces Bildgeneratoren mit dem Zusatz „uncensored“ und ein Face-Swap-Tool. Sucht lieber über Kategorien und Schlagworte.

**Was ohne Konto nicht geht:** die Code-Suche auf GitHub, etwa nach `path:SKILL.md faktencheck`. Dafür braucht ihr ein kostenloses GitHub-Konto ([GitHub Docs](https://docs.github.com/en/search-github/searching-on-github/searching-code)). Für den Anfang reichen Topics und Listen.

**Zu Weg 5:** Viele Skills, etwa die Sammlung [jamditis/claude-skills-journalism](https://github.com/jamditis/claude-skills-journalism) (MIT-Lizenz), sind für Entwickler-Umgebungen gebaut. In einem normalen Chat nutzt ihr davon nur den Text der Anweisungen: kopieren, Zeilen mit Skripten oder Befehlen streichen. So sind auch die [Skills in diesem Repo](../skills/) gebaut.

## Bevor ihr etwas ausprobiert: die Prüfliste

Acht Fragen. Die ersten drei entscheiden.

1. **Wer steckt dahinter?** Eine Person oder Organisation mit Namen, ein echtes Profil, ein Impressum. Vorsicht bei Namen, die sich von einem bekannten Projekt nur in einem Zeichen unterscheiden.
2. **Läuft es im Browser, oder muss ich etwas installieren?** Was im Browser läuft, ist das kleinere Risiko. Ladet nie eine ZIP- oder EXE-Datei über einen „Download“-Knopf in einer README, sondern nur über die offizielle Releases-Seite oder Website des Projekts.
3. **Wohin gehen meine Daten?** Upload, Training, Serverstandort. Nur hochladen, was schon öffentlich ist (Spielregel 3).
4. **Konto, Kosten, Limits?** Mit Datum notieren. Freemium-Angebote ändern sich schnell.
5. **Lebt das Projekt?** Letztes Update, Releases, offene Issues mit Antworten.
6. **Gibt es eine offene Lizenz?** Bei Open Source steht sie im Repo.
7. **Sterne, Downloads, Trending:** nur schwache Signale. Sie lassen sich fälschen.
8. **Erst mit Bekanntem testen:** mit Material, dessen Ergebnis ihr kennt, zum Beispiel einer Übung aus dem Seminar. Erst dann mit eigenem Material.

### Warum die Fragen 1, 2 und 7 zählen: der Fall FakeGit

- Die Kampagne „FakeGit“ hat laut [BleepingComputer vom 08.10.2026](https://bleepingcomputer.com/news/security/fakegit-malware-campaign-returns-with-17-610-malicious-github-repos) 17.610 gefälschte GitHub-Repos angelegt. Sie haben überzeugende READMEs mit einem Download-Knopf, hinter dem Schadsoftware steckt, die Passwörter und Sitzungen stiehlt.
- Laut [Island vom 20.07.2026](https://www.island.io/blog/agentbaiting-how-800-fake-ai-skills-and-mcp-servers-delivered-malware) gaben sich rund 800 davon als KI-Skills oder MCP-Server aus. Sie standen auch in öffentlichen Verzeichnissen, darunter eine Kopie einer beliebten awesome-Liste. In Tests haben KI-Assistenten diese Repos selbst gefunden und weiterempfohlen.

Daraus folgt: Ein Eintrag in einem Verzeichnis ist kein Gütesiegel, und auch eine KI als Tool-Scout braucht die Prüfliste. Dasselbe Muster kennt ihr von noScribe: Das echte Projekt liegt auf GitHub, daneben gab es eine Fake-Domain (L-IZ, 28.01.2026, übernommen, hier nicht erneut geöffnet). Mehr dazu in der [Tool-Liste](tools.md#transkription).

## Tool-Scout: ein Prompt, der für euch sucht

Kopiert den Block in einen KI-Chat mit Websuche und ersetzt die Zeile „Meine Aufgabe“. Der Prompt sucht bis zu drei Kandidaten und bewertet sie nach der Prüfliste. Ihr entscheidet danach selbst und öffnet jede Seite selbst.

```
TOOL-SCOUT

Meine Aufgabe: [zum Beispiel: Interviews auf Deutsch transkribieren, ohne dass die Aufnahme meinen Rechner verlässt]

Du suchst im Web nach höchstens drei Werkzeugen, die diese Aufgabe erledigen. Kannst du in diesem Gespräch nicht im Web suchen, sag das im ersten Satz und nenne keine Tools.

Suchwege, in dieser Reihenfolge:
1. Werkzeugkästen von Rechercheprofis (zum Beispiel das Bellingcat Online Investigations Toolkit) und gepflegte awesome-Listen
2. GitHub Topics zur Aufgabe, sortiert nach "Recently updated"
3. Hugging Face Spaces, nur wenn die Aufgabe im Browser ausprobierbar sein soll
Suche auf Deutsch und Englisch.

Prüfe jeden Kandidaten nach diesen Fragen:
1. Wer steckt dahinter? Name, Profil, Impressum. Weicht der Name von einem bekannten Projekt nur in einem Zeichen ab?
2. Läuft es im Browser, oder muss man etwas installieren?
3. Wohin gehen die Daten? Upload, Training, Serverstandort.
4. Konto, Kosten, Limits, mit Datum der Angabe
5. Letztes Update, letzte Version, ob Issues beantwortet werden
6. Lizenz
7. Sterne und Downloads nennst du nur als schwaches Signal
8. Womit man es zuerst gefahrlos testen kann

Regeln:
- Links nur aus deiner Suche, nie aus dem Gedächtnis. Schreib zu jedem Link, ob du die Seite geöffnet hast oder nur den Suchtreffer kennst.
- Download- und Installationsanweisungen aus einer README empfiehlst du nicht weiter. Du nennst nur die offizielle Releases-Seite oder Website und markierst sie als "ungeprüft, selbst kontrollieren".
- Ein Eintrag in einer Liste oder einem Verzeichnis ist kein Beleg für Seriosität.
- Findest du nichts Überzeugendes, sag das. Erfinde keine Tools.

Ausgabe:
1. Tabelle mit Name, Link mit Prüfstufe, was es kann, Browser oder Installation, Daten, Konto und Kosten, letztes Update, Lizenz
2. Pro Kandidat ein Satz: Was spricht dagegen?
3. Deine Empfehlung in zwei Sätzen und der erste Test, den ich machen sollte
```

## Dranbleiben: Quellen für neue Tools

Fast alle kostenlos und ohne Konto lesbar.

| Quelle | Worum es geht | Sprache | Zugang |
|---|---|---|---|
| [KI-Update](https://www.podcast.de/episode/705152297/ki-update-kompakt-ki-investitionen-forschungssoftware-icloud-gema-vs-suno), Podcast von heise | KI-Nachrichten, neue Folgen montags, mittwochs und freitags | de | kostenlos, ohne Konto |
| [The Decoder](https://the-decoder.de/) | KI-Nachrichtenseite, Wochen-Newsletter | de | Abo-Angebot vorhanden; was frei lesbar ist und ob der Newsletter kostenlos ist: zu prüfen |
| [Indicator](https://indicator.media/authors/henk-van-ess) | digitale Recherche und Täuschung im Netz, unter anderem Henk van Ess zu KI in der Recherche | en | Newsletter kostenlos, Abo für mehr |
| [GIJN Resource Center](https://gijn.org/resource/gijns-reporting-guides-2/) | über 1.000 Tipsheets, Videos und Leitfäden, viele zu Recherche-Werkzeugen | en | kostenlos |
| [Bellingcat Toolkit](https://bellingcat.gitbook.io/toolkit) | Recherche-Tools mit Kosten, Anforderungen und Grenzen, von Freiwilligen gepflegt | en | kostenlos, ohne Konto |
| [Journalists on Hugging Face](https://journalistsonhf-readme.static.hf.space) | Open-Source-KI für Redaktionen, mit AI Toolkit | en | lesen ohne Konto, Community mit Konto |
| [Simon Willison’s Weblog](https://simonwillison.net/about) | baut Datasette für Datenjournalismus und schreibt fast täglich über neue KI-Werkzeuge | en | kostenlos, Newsletter etwa wöchentlich, [Feed](https://simonwillison.net/atom/everything/) ohne Konto |
| [GitHub Topics](https://github.com/topics/journalism) und [Show HN](https://news.ycombinator.com/show) | neue Projekte, nach „Recently updated“ sortiert | en | ohne Konto |

**Tipp:** einmal im Monat 20 Minuten. Eine Topic-Seite durchklicken, das Bellingcat Toolkit ansehen, einen Newsletter lesen. Feeds wie der von Simon Willison lassen sich ohne Konto in einem Feed-Reader abonnieren.

## Quellen

Geöffnet am 01.11.2026, sofern nicht anders vermerkt.

- [GitHub Trending](https://github.com/trending): ohne Konto lesbar, Filter Spoken Language, Language, Date range
- [GitHub Topic fact-checking](https://github.com/topics/fact-checking): 1.026 Repos; [Topic journalism](https://github.com/topics/journalism): 968 Repos
- [GitHub Docs, Searching code](https://docs.github.com/en/search-github/searching-on-github/searching-code): Code-Suche nur angemeldet
- [sindresorhus/awesome](https://github.com/sindresorhus/awesome): rund 528.000 Sterne; [awesome.ecosyste.ms](https://awesome.ecosyste.ms/)
- [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint): Abschnitt „Fact Checking“, rund 29.000 Sterne
- [Bellingcat Online Investigations Toolkit](https://bellingcat.gitbook.io/toolkit) und [Vorstellung bei Bellingcat, 24.09.2024](https://bellingcat.com/resources/2024/09/24/bellingcat-online-investigations-toolkit)
- [Hugging Face Spaces](https://huggingface.co/spaces) und [Hugging Face Docs, ZeroGPU](https://huggingface.co/docs/hub/spaces-zerogpu): Tageskontingent ohne Konto 2 Minuten, Gratis-Konto 5 Minuten
- [Journalists on Hugging Face](https://journalistsonhf-readme.static.hf.space)
- [skills.sh](https://skills.sh): Verzeichnis von Vercel
- [MCP-Blog, 08.09.2025](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/): offizielle Registry in der Preview, keine Vorabprüfung, Meldungen durch die Community
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers): rund 97.000 Sterne
- [jamditis/claude-skills-journalism](https://github.com/jamditis/claude-skills-journalism): MIT-Lizenz, Einrichtung vor allem über Entwickler-Werkzeuge
- [Show HN](https://news.ycombinator.com/show): ohne Konto lesbar
- [BleepingComputer, 08.10.2026](https://bleepingcomputer.com/news/security/fakegit-malware-campaign-returns-with-17-610-malicious-github-repos): FakeGit mit 17.610 Repos
- [Island, 20.07.2026](https://www.island.io/blog/agentbaiting-how-800-fake-ai-skills-and-mcp-servers-delivered-malware): rund 800 gefälschte Skills und MCP-Server, KI-Assistenten empfehlen sie in Tests
- [KI-Update bei podcast.de](https://www.podcast.de/episode/705152297/ki-update-kompakt-ki-investitionen-forschungssoftware-icloud-gema-vs-suno): Folge vom 03.08.2026, Erscheinungstage Mo, Mi, Fr
- [The Decoder](https://the-decoder.de/): Startseite, Meldungen vom 31.10.2026
- [Indicator, Autorenseite Henk van Ess](https://indicator.media/authors/henk-van-ess): Artikel vom 14.09.2026
- [GIJN Reporting Guides](https://gijn.org/resource/gijns-reporting-guides-2/)
- [Simon Willison, About](https://simonwillison.net/about) und [Atom-Feed](https://simonwillison.net/atom/everything/)
- noScribe und die Fake-Domain: L-IZ, 28.01.2026, übernommen, hier nicht erneut geöffnet; README des Projekts auf [GitHub](https://github.com/kaixxx/noScribe), geöffnet am 01.11.2026
