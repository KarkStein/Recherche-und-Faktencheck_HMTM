# PDB-Helfer zum Mitnehmen

Der PDB-Helfer baut euch Suchstrings für Pressedatenbanken (PDB): zwei kopierfertige Strings, einen engen und einen weiten, und erklärt jeden Baustein. Standard ist das Archiv der Süddeutschen Zeitung über die Stabi (Bayerische Staatsbibliothek). Auf Wunsch schreibt er den String für F.A.Z., Genios/WISO oder LexisNexis um. Ihr kopiert den String in die Datenbank, meldet die Trefferzahl zurück, und er justiert nach.

Passt zu Kapitel 3 des Seminars. Zugänge und Syntax aller Datenbanken stehen in [Datenbanken: Zugänge und Suchsyntax](../../../suche/datenbanken.md).

Stand: 03.11.2026

## Welche Datei wofür

| Datei | Länge | Wofür |
|---|---|---|
| `SKILL.md` | rund 1.400 Wörter, 9.900 Zeichen | in einen Chat einfügen, in ein Projekt legen oder als Skill hochladen. Für GPTs mit 8.000 Zeichen Limit zu lang: dort als Datei hochladen |
| [`pdb-helfer.zip`](../zum-hochladen/pdb-helfer.zip) im Ordner `zum-hochladen` | – | Paket zum Hochladen in Claude und Gemini |

## Voraussetzung

Ein beliebiger KI-Chat. Websuche ist hilfreich, um Schreibweisen und passende Begriffe zu finden, aber nicht nötig. Ohne Websuche schreibt der Helfer dazu, dass ihr Schreibweisen selbst prüfen sollt. Wie ihr den Skill einsetzt, steht in der [Anleitung](../README.md).

Für die Datenbank selbst braucht ihr euren Ausweis der Stabi oder der Stadtbibliothek.

## So fragt ihr

- „Suchstring für Artikel über die Akustik der Isarphilharmonie“
- „Interviews mit Kirill Petrenko, nur die letzten zwei Jahre“
- „Das gleiche bitte für WISO“
- „Eng hatte 3 Treffer, weit 850“
- „Fehlermeldung: unerwartetes Suchelement“

## Das Ergebnis lesen

Ihr bekommt:

1. eine Zeile, was er zu Schreibweisen und Begriffen gefunden hat
2. **String eng** und **String weit**, jeweils zum Kopieren
3. eine kleine Tabelle: welcher Baustein was bewirkt
4. was ihr in der Suchmaske einstellen solltet (Zeitraum, Ressort, Artikeltyp)

Dann meldet ihr die Trefferzahlen. Ziel sind etwa 20 bis 100 Treffer. Der Helfer ändert pro Runde nur eine Stellschraube, damit ihr seht, was wirkt.

## Die wichtigsten Operatoren im SZ-Archiv

| Syntax | Bedeutung |
|---|---|
| `ATLEAST.5(Petrenko*)` | Wort kommt mindestens fünfmal vor |
| `NEAR.10(Petrenko, Philharmoniker)` | höchstens zehn Wörter Abstand |
| `ONEAR.3(Zauberflöte, Inszenierung)` | wie NEAR, in dieser Reihenfolge |
| `*philharmonie` | Linkstrunkierung, findet auch Isarphilharmonie |

Häufigster Fehler: mehrere Wörter in einer ATLEAST-Klammer. `ATLEAST.3(Oper* AND Intendant*)` geht nicht, richtig ist `ATLEAST.3(Oper*) AND ATLEAST.3(Intendant*)`.

## Grenzen

- **Er fragt die Datenbanken nicht selbst ab.** Die Suche macht ihr, er baut nur die Strings.

Nicht gesichert ist bisher:

- Ob `begriff#N` (F.A.Z., WISO) und `atleastN(…)` (LexisNexis) zusammen mit `*` funktionieren.
- Ob Linkstrunkierung außerhalb des SZ-Archivs geht.
- Ob die Suchmaske im SZ-Archiv einen Artikeltyp „Interview“ anbietet.

Testet das mit einer Suche, deren Treffer ihr ungefähr kennt. Mehr dazu in der [Anleitung](../README.md#erst-testen-dann-nutzen).

## Herkunft

Beruht auf dem Suchstring-Assistenten, den Florian in der Redaktion nutzt, umgebaut für den Bibliothekszugang. Er kennt nur die Operatoren von der Seminarfolie, Zeitraum, Ressort und Artikeltyp stellt ihr in der Suchmaske ein.
