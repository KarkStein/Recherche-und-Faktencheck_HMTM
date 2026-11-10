# Datenbanken: Zugänge und Suchsyntax

Aus Kapitel 3 der Seminarfolien. Stand: 01.11.2026.

**Prüfstufe:** übernommen aus den Folien. Funktioniert ein Link nicht, findet ihr die Datenbank über [DBIS](#datenbanken-finden-dbis).

## Warum Datenbanken, wenn es Google gibt?

Datenbanken sind meist auf ein Thema spezialisiert. Ihre Inhalte sind ausgewählt und erschlossen, die Quellen durchlaufen zumindest eine gewisse Qualitätssicherung, und vieles davon findet keine Suchmaschine.

Manche Datenbanken sind kostenlos, manche Freemium, manche nur mit bezahltem Konto nutzbar. **Mit eurem Ausweis der Bayerischen Staatsbibliothek (Stabi) und der Münchner Stadtbibliothek kommt ihr kostenlos an viele Datenbanken, die sonst Geld kosten.** Die Links über `emedia1.bsb-muenchen.de/han/…` fragen nach dem Stabi-Login.

## Datenbanken finden: DBIS

[DBIS](https://dbis.ur.de/BSB/browse/subjects/), das Datenbank-Infosystem, ist ein Katalog von Datenbanken aus allen Fachgebieten, keineswegs nur wissenschaftlichen. Der Link führt zum Einstieg über die Stabi.

Ein Ampelsymbol zeigt den Zugang:

| Ampel | Zugang |
|---|---|
| grün | frei zugänglich |
| gelb | über den Stabi-Account |
| rot | nur kostenpflichtig oder mit besonderer Berechtigung |

## Pressedatenbanken

Die meisten Pressedatenbanken laufen intern in Verlagen und Sendern. F.A.Z. und SZ bieten auch externe Zugänge an, ebenso Genios, Munzinger, LexisNexis und Dow Jones Factiva. Über Stabi und Stadtbibliothek kommt ihr kostenlos an F.A.Z., SZ, Genios, Munzinger und LexisNexis.

### Überblick: Zugang und Syntax

| Datenbank | Zugang | Nähe | Mindestens N-mal | Besonderheit |
|---|---|---|---|---|
| SZ | [Stabi](http://emedia1.bsb-muenchen.de/han/sz) | `NEAR.N(a,b)` · in Reihenfolge `ONEAR.N(a,b)` | `ATLEAST.N(begriff)` | Linkstrunkierung `*philharmonie`, Artikeltypen und Dossiers |
| F.A.Z. | [Stabi](http://emedia1.bsb-muenchen.de/han/faz-bibliotheksportal/) | `"a b"~N` | `begriff#N` | bildet Wortstämme automatisch |
| Genios / WISO | [Stadtbibliothek](http://bib-muenchen.genios.de/), [Stabi](http://emedia1.bsb-muenchen.de/han/wiso/) | `"a b"~N` | `begriff#N` | Suche auf [genios.de](http://www.genios.de/) ohne Konto |
| LexisNexis (Nexis Uni) | [Stabi](http://emedia1.bsb-muenchen.de/han/nexisuni1) | `a near/N b` | `atleastN(begriff)` | internationale Presse; NOT heißt hier `AND NOT` |

In allen vier gehen `AND`, `OR`, `NOT`, `*` zum Trunkieren, `"Phrasensuche"` und `(Klammern)` zum Gruppieren.

Den Suchstring für SZ, F.A.Z. und WISO baut euch auf Wunsch der [PDB-Helfer](../skills/pdb-helfer/).

### Süddeutsche Zeitung

- Zugang über den Stabi-Account: [emedia1.bsb-muenchen.de/han/sz](http://emedia1.bsb-muenchen.de/han/sz)
- Weitgehend alle SZ-Ausgaben und die Inhalte von sz.de.
- Großes Plus: Ihr könnt die Erschließung der SZ-Dokumentation nutzen, also die Zuordnung von Artikeln zu Dossiers, und nach Artikeltypen filtern.
- Unter „Ganzseiten“ blättert ihr durch die Ausgaben wie im E-Paper.
- Zeitraum, Ressort, Artikeltyp und mehr könnt ihr vor der Suche einschränken oder danach filtern.

Operatoren und Syntax (unter anderem):

| Syntax | Bedeutung |
|---|---|
| `AND` / `OR` / `NOT` | beide, einer davon, nicht |
| `Philharmonie*` | Trunkierung rechts |
| `*philharmonie` | Trunkierung links, findet auch Isarphilharmonie |
| `"Phrasensuche"` | genau diese Wortfolge |
| `( … )` | Gruppieren |
| `NEAR.N(begriff1,begriff2,…)` | Begriffe höchstens N Wörter voneinander entfernt |
| `ONEAR.N(begriff1,begriff2,…)` | wie NEAR, aber in dieser Reihenfolge |
| `ATLEAST.N(begriff)` | Begriff kommt mindestens N-mal im Text vor |

### Frankfurter Allgemeine Zeitung

- Zugang über den Stabi-Account: [emedia1.bsb-muenchen.de/han/faz-bibliotheksportal/](http://emedia1.bsb-muenchen.de/han/faz-bibliotheksportal/)
- Die Suche bildet aus eurer Eingabe automatisch Wortstämme und Beugungsformen. Manchmal schießt sie dabei übers Ziel hinaus.
- Alle Operatoren erklärt die [Suchhilfe des F.A.Z.-Archivs](https://fazarchiv.faz.net/suchhilfe).

| Syntax | Bedeutung |
|---|---|
| `AND` / `OR` / `NOT`, `*`, `"Phrase"`, `( … )` | wie oben |
| `"suchbegriff1 suchbegriff2"~N` | Begriffe höchstens N Wörter voneinander entfernt |
| `suchbegriff#N` | Begriff kommt mindestens N-mal im Text vor |

### Genios und WISO

Genios vermarktet dieselbe Datenbank unter zwei Namen. Sie enthält Zeitungen und Zeitschriften vieler Verlage.

- Genios über die Stadtbibliothek: [bib-muenchen.genios.de](http://bib-muenchen.genios.de/)
- WISO über die Stabi: [emedia1.bsb-muenchen.de/han/wiso](http://emedia1.bsb-muenchen.de/han/wiso/)
- Auf [genios.de](http://www.genios.de/) könnt ihr ohne Konto und kostenlos suchen. Erst das Abrufen von Artikeln kostet.
- Syntax wie bei der F.A.Z.: `"a b"~N` für Nähe, `begriff#N` für mindestens N-mal. Alle Operatoren und Felder stehen in der [Genios-Hilfe](https://www.gbi-genios.de/de/hilfe/genios/operatoren-und-datenbank-felder).

### LexisNexis (Nexis Uni)

- Sehr viele internationale Publikationen, unter anderem Guardian, New York Times, Le Figaro, El País.
- Zugang über den Stabi-Account: [emedia1.bsb-muenchen.de/han/nexisuni1](http://emedia1.bsb-muenchen.de/han/nexisuni1)
- Alle Operatoren erklärt die [Hilfe von LexisNexis](https://www.lexisnexis.com/Casemapsuitesupport/xm/xm9.0/xm_search_operators_using.htm) (englisch).

| Syntax | Bedeutung |
|---|---|
| `AND` / `OR` / `AND NOT`, `*`, `"Phrase"`, `( … )` | wie oben, NOT heißt hier `AND NOT` |
| `begriff1 near/N begriff2` | Begriffe höchstens N Wörter voneinander entfernt |
| `atleastN(begriff)` | Begriff kommt mindestens N-mal im Text vor |

### Artikel hinter der Bezahlschranke lesen

- Viele „Plus“-Artikel stehen auch in Genios oder WISO. Gebt den Titel oder einen Halbsatz aus dem sichtbaren Teil in das Suchfeld ein. Ist der Artikel in der Datenbank, könnt ihr ihn lesen.
- Bei manchen Quellen dauert es ein paar Tage, bis Artikel in der Datenbank stehen. Manche bleiben dauerhaft exklusiv.
- Tipp: Das Browser-Plugin [BibBot](https://stefanw.github.io/bibbot/) sucht beim Aufruf eines Paywall-Artikels im Hintergrund in Genios oder WISO und blendet den Text ein, wenn es ihn findet. Dafür hinterlegt ihr eure Zugangsdaten von Stabi oder Stadtbibliothek; mit der Stadtbibliothek gibt es mehr Quellen. Nur für Text, nicht für Bilder oder Grafiken.

### Zeitschriften und E-Paper

| Angebot | Was | Zugang |
|---|---|---|
| [PressReader](https://online.munzinger.de/publikation/pressreader) | E-Paper von Zeitschriften und einzelnen Zeitungen | Stadtbibliothek, über Munzinger |
| [Onleihe München](https://www.onleihe.de/muenchen/frontend/welcome,51-0-0-100-0-0-1-0-0-0-0.html) | E-Paper von Zeitschriften suchen und digital ausleihen | Stadtbibliothek |
| [Elektronische Zeitschriftenbibliothek (EZB)](https://ezb.ur.de/searchres.phtml?bibid=BSB) | vor allem wissenschaftliche Zeitschriften, Ampel wie in DBIS | Stabi |

## Thematische Datenbanken

### Munzinger

Munzinger vereint unter anderem Biografien, Pop-Lexikon, Sport-Lexikon, Gedenktage und Chronik, Filmdienst-Kritiken, die Kritischen Lexika zur deutsch- und fremdsprachigen Gegenwartsliteratur und Duden Sprachwissen.

- über die Stabi: [Munzinger via DBIS](https://dbis.ur.de/warpto?ubr_id=BSB&resource_id=2109&license_type=2&license_form=22&access_type=1&access_form=15&access_id=61265)
- über die Stadtbibliothek: [online.munzinger.de](https://online.munzinger.de/)
- Die enthaltenen Module unterscheiden sich je nach Zugang etwas.

### Feltas

[Feltas](http://www.feltas.de/) ist eine Ereignis-Datenbank: Geburts- und Todestage bekannter Persönlichkeiten, Chronik politischer, kultureller und anderer Ereignisse. Eingeschränkt auch ohne Anmeldung nutzbar. Gut für Jahrestage als Anlass.

### MediathekViewWeb

[MediathekViewWeb](https://mediathekviewweb.de/) durchsucht an einer Stelle die Mediatheken der öffentlich-rechtlichen Sender aus Deutschland sowie ORF und SRF. Die Beiträge laufen direkt im Browser. Bei ORF und SRF nicht mehr direkt: Dort öffnet ihr die URL des M3U8-Streams im VLC-Player.

| Syntax | sucht in |
|---|---|
| `!sendername` | Sender |
| `#thema` | Thema, meist der Name der Sendung |
| `+titel` | Titel des Beitrags |
| `*begriff` | überall |
