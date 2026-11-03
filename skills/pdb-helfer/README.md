# PDB-Helfer zum Mitnehmen

Der PDB-Helfer baut euch Suchstrings für Pressedatenbanken (PDB): zwei kopierfertige Strings, einen engen und einen weiten, und erklärt jeden Baustein. Standard ist das Archiv der Süddeutschen Zeitung über die Stabi. Auf Wunsch schreibt er den String für F.A.Z., Genios/WISO oder LexisNexis um. Ihr kopiert den String in die Datenbank, meldet die Trefferzahl zurück, und er justiert nach.

Passt zu Kapitel 3 des Seminars. Zugänge und Syntax aller Datenbanken stehen in [suche/datenbanken.md](../../suche/datenbanken.md).

Diese Fassung beruht auf dem Suchstring-Assistenten, den Florian in der Redaktion nutzt (Stand 27.10.2026), umgebaut für den Bibliothekszugang.

Stand: 03.11.2026

## Welche Datei

| Datei | Länge | Wofür |
|---|---|---|
| `SKILL.md` | rund 1.400 Wörter, 9.900 Zeichen | in einen Chat einfügen, in ein Projekt legen oder als Skill hochladen. Für GPTs mit 8.000 Zeichen Limit zu lang: dort als Datei hochladen |
| [`../zum-hochladen/pdb-helfer.zip`](../zum-hochladen/pdb-helfer.zip) | – | Paket zum Hochladen in Claude und Gemini |

## Voraussetzung

Ein beliebiger KI-Chat. Websuche ist hilfreich, um Schreibweisen und passende Begriffe zu finden, aber nicht nötig. Ohne Websuche schreibt der Helfer dazu, dass ihr Schreibweisen selbst prüfen sollt. Wie ihr den Skill einsetzt, steht in der [Anleitung](../ANLEITUNG.md).

Für die Datenbank selbst braucht ihr euren Ausweis der Stabi oder der Stadtbibliothek.

## So fragt ihr

- „Suchstring für Artikel über die Akustik der Isarphilharmonie“
- „Interviews mit Kirill Petrenko, nur die letzten zwei Jahre“
- „Das gleiche bitte für WISO“
- „Eng hatte 3 Treffer, weit 850“
- „Fehlermeldung: unerwartetes Suchelement“

## Was ihr zurückbekommt

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

## Was anders ist als in der Redaktionsfassung

- **Nur die Operatoren von der Seminarfolie.** Die Redaktion arbeitet mit einem internen System und weiteren Feldcodes, etwa für Titel, Publikation oder Datum. Ob die im Bibliothekszugang funktionieren, ist nicht geprüft. Zeitraum, Ressort und Artikeltyp stellt ihr deshalb in der Suchmaske ein.
- **Keine Quellenlisten und Publikationscodes** der Redaktion.
- **Neu:** Umrechnung für F.A.Z., Genios/WISO und LexisNexis, Erklärung jedes Bausteins, funktioniert auch ohne Websuche.

## Was noch zu prüfen ist

- Ob `begriff#N` (F.A.Z., WISO) und `atleastN(…)` (LexisNexis) zusammen mit `*` funktionieren.
- Ob Linkstrunkierung außerhalb des SZ-Archivs geht.
- Ob die Suchmaske im SZ-Archiv einen Artikeltyp „Interview“ anbietet.

Geprüft wird beim Testlauf am 03./04.11.2026, Ergebnisse kommen in die [Testtabelle](../ANLEITUNG.md#getestet-oder-noch-zu-prüfen).
