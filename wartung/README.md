# Wartung

Dieser Ordner ist für die Pflege des Repos. Zum Lesen und Nutzen des Werkzeugkastens braucht ihr ihn nicht.

| Datei | Was sie tut |
|---|---|
| [skills_packen.py](skills_packen.py) | baut aus jeder `SKILL.md` das Paket in `skills/zum-hochladen/` und prüft vorher den Kopf der Datei (`name`, `description`) |
| [gesamtpaket_bauen.py](gesamtpaket_bauen.py) | baut das [Gesamtpaket](../gesamtpaket/README.md): alle Seiten als eine HTML-Datei, die Skills als Textdateien, eine Datei für KI-Chats, die Pakete, die Folien und den Spickzettel, zusammen in einer ZIP-Datei |

## Nach jeder Änderung

Aus dem Hauptordner des Repos, in dieser Reihenfolge:

```
python3 wartung/skills_packen.py
python3 wartung/gesamtpaket_bauen.py
```

Danach die geänderten ZIP-Dateien mit committen. Mit `--pruefen` melden beide Skripte nur, ob etwas veraltet ist, und ändern nichts. Das Gesamtpaket braucht das Programm pandoc, das die Seiten in HTML umwandelt.

**Neue Fassung der Folien:** Das PDF in `folien/` entsteht aus der PowerPoint-Datei, ohne Sprechernotizen, ausgeblendete Folien fallen weg. In PowerPoint: Datei, Exportieren, PDF, unter Optionen „Folien“ wählen. Oder mit LibreOffice: `soffice --headless --convert-to pdf Datei.pptx`. Danach die Seitenzahlen der Kapitel in `folien/README.md` prüfen und das Gesamtpaket neu bauen.

**Neue Seite oder neuer Skill:** Im Gesamtpaket erscheinen sie erst, wenn sie in einer der Listen oben in `gesamtpaket_bauen.py` stehen. Das Skript meldet Dateien, die in keiner Liste stehen, und Links, die im Paket ins Leere führen.

## So sind die Seiten aufgebaut

Damit sich Leserinnen und Leser überall gleich zurechtfinden, folgen alle Seiten einem festen Muster. Geschrieben ist alles für kluge Leute ohne Technikkenntnisse: Fachwörter beim ersten Auftreten kurz erklären, sonst einfache Wörter.

**Ordner-Seite** (README.md in jedem Ordner)
1. Überschrift: Name des Ordners als Wort, etwa „Suchen“
2. Ein, zwei Sätze: wofür der Ordner da ist, zu welchem Kapitel er gehört
3. Tabelle: Datei, was drin ist, wann man sie braucht

**Skill-Seite** (README.md in jedem Skill-Ordner und bei Moby)
1. „[Name] zum Mitnehmen“, darunter zwei, drei Sätze: was er tut, wofür, Abgrenzung zu verwandten Skills, Kapitel
2. Stand: TT.MM.JJJJ
3. Abschnitte in dieser Reihenfolge: Welche Datei wofür · Voraussetzung · So fragt ihr · Das Ergebnis lesen · Grenzen · Herkunft
4. Erlaubt ist ein Zusatzabschnitt, wo er nötig ist, etwa „Faktencheck oder Moby?“
5. Wie man einen Skill einrichtet, steht nur in der [Anleitung](../skills/README.md), nicht auf jeder Skill-Seite. Ausnahme: Moby, der als Assistent anders eingerichtet wird.

**Inhaltsseite** (alle anderen Seiten)
1. Überschrift
2. Kopfzeile: „Aus Kapitel X des Seminars. Stand: TT.MM.JJJJ.“
3. Prüfstufe der Links, wenn die Seite Links enthält: geöffnet (mit Datum), übernommen, zu prüfen

**Stand** heißt: An diesem Tag wurden die Angaben auf der Seite zuletzt geprüft oder geändert. Wer nur umformuliert, lässt das Datum stehen.
