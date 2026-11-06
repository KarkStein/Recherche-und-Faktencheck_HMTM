# Suchen mit Google: Operatoren, erweiterte Suche, Web-Archiv

Aus Kapitel 2 der Seminarfolien, ergänzt um den Stand, welche Operatoren heute noch wirken. Stand: 01.11.2026.

Links aus den Folien haben die Prüfstufe **übernommen** (für dieses Repo nicht erneut geöffnet). Die beiden Quellen zum Operator-Stand sind **geöffnet am 01.11.2026**.

## Die Standardsuche

- Google ist nicht für objektive Recherche gebaut. Es rät, was für euch relevant sein könnte, und nutzt dafür auch Daten, die nicht in eurer Anfrage stehen, etwa Standort und frühere Suchen.
- Über der Trefferliste versucht Google, die Frage selbst zu beantworten, mit Inhalten aus Wikipedia und anderen Seiten. Wollt ihr nur die Trefferliste, klickt auf **Mehr**, dann **Web**.
- Gebt Schlüsselbegriffe ein statt ganzer Fragen: `Bergson Eröffnung` statt „Wann wurde das Bergson eröffnet?“
- Google sucht automatisch nach Wortstämmen und toleriert Tippfehler. Wollt ihr das nicht: **Suchfilter**, **Alle Ergebnisse**, **Wortwörtlich**.
- In den Suchfiltern legt ihr auch den Zeitraum fest (Format MM/DD/YYYY).
- Für Presse und Rundfunk: Reiter **News**, dann in den Suchfiltern Zeitraum wählen und von „Nach Relevanz sortiert“ auf „Nach Datum sortiert“ umstellen.

## Die erweiterte Suche

Direkt aufrufen: [google.com/advanced_search](https://www.google.com/advanced_search), oder auf der Startseite **Einstellungen**, dann **Erweiterte Suche**.

| Feld | Was es tut | Beispiel aus den Folien |
|---|---|---|
| genau dieses Wort oder diese Wortgruppe | genau diese Wörter in dieser Reihenfolge | „Wer reitet so spät durch Nacht und Wind“ |
| keines der folgenden Wörter | diese Wörter dürfen nicht vorkommen | „Oktoberfest“, aber ohne „München“ |
| Webseite oder Domain | nur Treffer auf dieser Website | „Frank Sinatra“ nur auf zeit.de |
| Dateityp | nur Dateien in diesem Format, keine Webseiten | nur PDF |

## Operatoren: was heute noch wirkt

Google dokumentiert offiziell nur sechs Operatoren. Andere wirken trotzdem, manche gar nicht mehr. Die Spalte „Stand“ folgt einem Test von SEOmator vom 13.07.2026 (Google USA, Englisch, Desktop). Ergebnisse können je nach Land, Sprache und Zeitpunkt abweichen.

| Operator | Was er tut | Beispiel | Stand |
|---|---|---|---|
| `"…"` | genau diese Wortfolge | `"Wer reitet so spät durch Nacht und Wind"` | offiziell |
| `-wort` | Wort darf nicht vorkommen, ohne Leerzeichen | `Bach -Vivaldi` | offiziell |
| `site:` | nur diese Website | `site:zeit.de "Rolling Stones"` | offiziell |
| `filetype:` | nur dieser Dateityp | `filetype:pdf Spielzeit Programmheft` | offiziell |
| `after:` / `before:` | zuletzt aktualisiert nach oder vor einem Datum | `Documenta after:2022-06-01 before:2022-09-30` | offiziell, siehe Hinweis |
| `intitle:` / `allintitle:` | Wort oder alle Wörter im Titel der Seite | `intitle:Uraufführung Oper` | wirkt, nicht offiziell |
| `intext:` / `allintext:` | Wort oder alle Wörter im Seitentext | `intext:Intendanz Theater` | wirkt, nicht offiziell |
| `AROUND(N)` | Begriffe höchstens N Wörter voneinander entfernt | `Brecht AROUND(5) Weill` | wirkt, nicht offiziell |
| `OR` | einer der Begriffe genügt, großschreiben | `Bach OR Vivaldi` | unklar |
| `*` | Platzhalter für ein beliebiges Wort | `"Wer * so * durch * und *"` | unklar |
| `inurl:` / `allinurl:` | Wort in der Internetadresse | `inurl:pressemitteilung` | gelockert, filtert nicht mehr streng |
| `cache:`, `related:`, `info:`, `link:`, `+`, `~` | | | wirken nicht mehr |

**Hinweis zu `after:` und `before:`:** Sie filtern nach dem Datum der letzten Aktualisierung, nicht nach dem Erscheinungsdatum. Ein alter Text, der gestern geändert wurde, taucht also auch bei `after:gestern` auf. Prüft das Datum immer auf der Seite selbst.

**Hinweis zu `*`:** Bei Google ist das Sternchen ein Platzhalter für ein ganzes Wort. Wortteile abschneiden („trunkieren“, etwa `Erlk*`) geht bei Google nicht, wohl aber in den [Pressedatenbanken](datenbanken.md).

**Kein Leerzeichen** zwischen Operator und Suchbegriff: `site:zeit.de`, nicht `site: zeit.de`.

### Kombinieren

Operatoren lassen sich verbinden. Ein paar Muster zum Abwandeln (Beispiele, nicht für jedes Thema getestet):

| Ziel | Suchstring |
|---|---|
| Interviews einer Person auf einer Sender-Website | `site:br.de intitle:Interview "Anne-Sophie Mutter"` |
| Dokumente einer Stadt zu einem Thema | `site:berlin.de filetype:pdf Atelierförderung` |
| Berichte ohne Wikipedia und Online-Lexika | `"Gärtnerplatztheater" Sanierung -site:wikipedia.org` |
| eine Person, aber nicht eine gleichnamige | `"Thomas Mann" -Heinrich` |
| Pressemitteilungen eines Hauses | `site:pinakothek.de intitle:Pressemitteilung` |

Mehr Operatoren mit Beispielen: [ahrefs, Google Advanced Search Operators](https://ahrefs.com/blog/google-advanced-search-operators/) und [eine Sammlung als Google-Dokument](https://docs.google.com/document/d/1ydVaJJeL1EYbWtlfj9TPfBTE5IBADkQfZrQaBZxqXGs) (beide übernommen aus den Folien). Ob ein Operator noch wirkt, prüft ihr am besten selbst mit einer Suche, deren Ergebnis ihr kennt.

## Suche im Web-Archiv

Was tun, wenn eine Seite verschwunden ist oder sich verändert hat?

- Das [Internet Archive (Wayback Machine)](https://web.archive.org/) speichert Webseiten in Kopien mit Datum, sofern die Betreiber das nicht verhindern oder eine Löschung beantragen.
- Den Cache von Google gibt es nicht mehr. Andere Archive gibt es, zum Beispiel bei Bing.
- Archiv-Metasuche über mehrere Archive: [echo.archivarix.net](https://echo.archivarix.net/)
- Browser-Erweiterung für den direkten Zugriff auf viele Archive: [Web Archives](https://github.com/dessant/web-archives)
- Die Deutsche Nationalbibliothek archiviert das deutschsprachige Web: [Sammlung Websites der DNB](https://www.dnb.de/DE/Professionell/Sammeln/Sammlung_Websites/sammlung_websites_node.html)

Eine archivierte Seite belegt, was zu diesem Zeitpunkt dort stand. Gebt in eurem Text das Datum der Archivkopie an.

## Wikipedia

Wikipedia hat rund drei Millionen Artikel auf Deutsch, geschrieben von Freiwilligen. Sie gilt nicht als zitierfähige Quelle, weil die Autor:innen meist anonym sind und ihre Sachkenntnis nicht belegt ist. Nutzt sie als Sprungbrett: Die Einzelnachweise unten im Artikel führen zu Originalquellen, die ihr selbst öffnet und zitiert.

## Quellen

- Folien „Recherche im Web“, Seminar Recherche und Faktencheck, Stand 31.10.2026
- [Google-Suchhilfe, Refine Google searches](https://support.google.com/websearch/answer/2466433?hl=en): dokumentiert `"…"`, `site:`, `-`, `before:`, `after:`, `filetype:`; geöffnet am 01.11.2026
- [SEOmator, Google Search Operators Cheat Sheet](https://seomator.com/de/blog/google-search-operators-cheat-sheet-tabelle): Test aller Operatoren am 13.07.2026, aktualisiert 21.07.2026; geöffnet am 01.11.2026
