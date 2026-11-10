# Prompten: von der Frage zum Auftrag

Aus Kapitel 4 des Seminars. Stand: 01.11.2026.

**Wichtigste Botschaft: Schreibt das, was ihr bekommen wollt.** Und übernehmt nur, was ihr in der Quelle selbst gesehen habt.

Hilfe beim Schreiben: Der [Prompthelfer](../skills/prompthelfer/) geht diese Checklisten mit euch durch und schreibt den Prompt für euer eigenes Thema.

## Zwei Arten zu fragen

| Einzelne Frage | Auftrag an einen Agenten oder Prozess |
|---|---|
| **Zweck:** wofür ihr die Antwort braucht | **Ziel:** Wann ist der Auftrag erledigt? |
| **Kontext:** was ihr schon wisst, für wen | **Erst der Plan:** zeigen lassen, dann starten |
| **Quellen:** welche zählen, mit Link und Zitat | **Grenzen:** welche Quellen, nichts senden, nichts kaufen |
| **Output:** Liste, Tabelle, Länge | **Belege:** Zwischenschritte und Quellen sichtbar |
| **Nachhaken** statt neu anfangen | **Format:** bei jedem Lauf gleich |

Links steht, was eine einzelne Frage an einen Chat besser macht. Rechts steht, was ein Tool zusätzlich braucht, das selbstständig in Schleifen sucht, etwa Deep Research: Es muss wissen, wann es fertig ist, was es nicht darf und wie das Ergebnis aussieht. Den Plan vorher anzusehen spart Fehlläufe.

## Vorlage: einzelne Frage

Ersetzt die eckigen Klammern. Das Beispiel ist erfunden und nicht geprüft.

```
Zweck: Ich schreibe [eine Meldung / ein Porträt / eine Vorrecherche] über [Thema].
Kontext: Ich weiß schon [was ihr wisst]. Der Text ist für [Publikum, Medium].
Frage: [eure Frage, so konkret wie möglich]
Quellen: Nutze vor allem [Primärquellen: Stadt, Ministerium, Veranstalter, Statistik]. Belege jede Zahl und jedes Zitat mit Link und dem wörtlichen Satz aus der Quelle. Wikipedia und KI-Zusammenfassungen sind keine Belege.
Output: [eine Tabelle mit Spalten ... / fünf Stichpunkte / höchstens 200 Wörter]. Markiere, was du nicht belegen kannst.
```

Beispiel:

```
Zweck: Ich schreibe eine kurze Meldung für ein Kulturmagazin.
Kontext: Ich weiß, dass die staatlichen Museen in Bayern ihre Eintrittspreise 2026 geändert haben sollen, kenne aber keine Details.
Frage: Was hat sich bei den Eintrittspreisen geändert, ab wann, und welche Häuser betrifft es?
Quellen: Nutze die Websites der Museen und des zuständigen Ministeriums zuerst. Belege jede Zahl mit Link und wörtlichem Satz.
Output: Tabelle mit Haus, Preis vorher, Preis nachher, gültig ab, Quelle. Darunter zwei Sätze zur Einordnung. Markiere, was du nicht belegen kannst.
```

**Nachhaken statt neu anfangen:** Im selben Chat weiterfragen. „Was spricht dagegen?“, „Welche Quelle davon hast du geöffnet?“, „Zeig mir den wörtlichen Satz zu Zahl 3.“

## Vorlage: Auftrag an einen Agenten

Für Deep Research, Claude Research oder andere Tools, die selbstständig suchen.

```
Ziel: Der Auftrag ist erledigt, wenn [die Frage beantwortet ist / jede der fünf Fragen einen Beleg hat / klar ist, was sich nicht belegen lässt].
Erst der Plan: Zeig mir zuerst deinen Suchplan in Stichpunkten und warte auf mein Okay.
Grenzen: Nutze nur [öffentliche Quellen / diese Websites / Quellen ab Jahr X]. Nichts senden, nichts kaufen, keine Formulare ausfüllen, keine Konten anlegen.
Belege: Nenne zu jeder Aussage die Quelle mit Link. Schreib dazu, ob du die Seite geöffnet hast oder nur den Suchtreffer kennst.
Format: [Gliederung, die bei jedem Lauf gleich bleibt, etwa: Kurzbefund, Tabelle der Fakten, offene Fragen, Quellenverzeichnis].
```

## Regeln einmal aufschreiben: das Projekt

Gebt ihr denselben Auftrag öfter, speichert die Regeln. In Claude heißt das Projekt, in ChatGPT ebenfalls Projekt, in Le Chat Agent. In Gemini hieß es Gem, an seine Stelle treten Skills. Ein Projekt bündelt Anweisungen und Dateien. Jeder neue Chat im Projekt kennt beide.

Vorlage für die Anweisungen eines Recherche-Projekts:

```
Belege jede Zahl mit Link und wörtlichem Zitat.
Primärquellen vor Presseberichten.
Markiere, was du nicht belegen kannst.
Nutze zuerst die Dateien in diesem Projekt, dann die Websuche.
Sag, wenn eine Frage mit den Dateien nicht zu beantworten ist.
```

Testet die dritte Regel mit einer Fangfrage, deren Antwort nicht in euren Dateien steht. Gute Antwort: „Dazu steht nichts in den Dokumenten.“

## Ein mögliches Regelwerk: ROMANE

Aus dem Seminar, als Gedächtnisstütze:

- **R**olle: in welcher Funktion, für wen
- **O**bjective: das Ziel
- **M**eta-Anweisungen: wie vorgehen, was beachten
- **A**nwendungsbeispiele: zeigen, wie das Ergebnis aussehen soll
- **N**icht zu lang
- **E**xperimentieren

„Schritt für Schritt denken“ müsst ihr Reasoning-Modellen nicht mehr sagen, sie tun es von selbst.
