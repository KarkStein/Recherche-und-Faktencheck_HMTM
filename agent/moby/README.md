# Moby zum Mitnehmen

Moby ist ein Faktencheck-Assistent. Er prüft einen Text in vier Schritten (Fakten herausziehen, in Aspekte zerlegen, prüfen, Bericht) und liefert einen Bericht mit Status, Quellen und Korrekturvorschlägen. Das ist dieselbe Methode wie im Seminar, Kapitel 5.

Moby ist kein Skill, sondern ein Assistent mit eigenem Raum. Ihr richtet ihn einmal als Projekt, GPT oder Le-Chat-Agent ein, und dort ist jede Nachricht ein Text zum Prüfen. Dieselbe Prüfung für einen normalen Chat ist der Skill Faktencheck. Was ihn von Moby unterscheidet, steht [beim Faktencheck](../../skills/faktencheck/README.md#faktencheck-oder-moby).

Stand: 03.11.2026

## Welche Datei wofür

| Datei | Länge | Wofür |
|---|---|---|
| `Moby_Faktencheck.md` | rund 3.200 Wörter, 23.100 Zeichen | Langfassung: in einen Chat einfügen oder als Datei in ein Projekt legen |
| `Moby_kurz.md` | rund 4.600 Zeichen | Kurzfassung für Anweisungsfelder mit Zeichenlimit |

Wenn ihr die Wahl habt, nehmt die Langfassung. Sie enthält die Quellenregeln und Beispiele, die Kurzfassung nur das Gerüst.

## Voraussetzung

Ein KI-Assistent, der **im Web suchen** kann. Ohne Websuche erfindet ein Modell im schlimmsten Fall Quellen. Moby ist so gebaut, dass er dann ablehnt und nur die Prüfliste liefert. Noch besser ist ein Tool, das gefundene Seiten auch **öffnen und lesen** kann, nicht nur die Suchtreffer.

Ein Konto anzulegen ist freiwillig. Ohne Konto: Langfassung in einen Chat kopieren, der eine Websuche hat (welche das sind, steht in der [Tool-Liste](../../ki-tools/tools.md)).

## So richtet ihr Moby ein

**Überall, ohne Einrichtung**
1. Neuen Chat öffnen, Websuche einschalten, falls es dafür einen Schalter gibt.
2. Den ganzen Inhalt von `Moby_Faktencheck.md` einfügen und abschicken.
3. In der nächsten Nachricht: „Prüfe diesen Text:“ und darunter euren Text.

**Als Projekt in Claude oder ChatGPT**
1. Neues Projekt anlegen.
2. `Moby_Faktencheck.md` als Datei hochladen, oder den Inhalt in die Projektanweisungen kopieren.
3. Falls ihr die Datei hochgeladen habt, in die Anweisungen schreiben: „Arbeite immer nach der Datei Moby_Faktencheck.md. Jede Nachricht ist der zu prüfende Text.“
4. Im Projekt einen Chat starten und den Text einfügen.

**Als Agent in Le Chat**
1. Neuen Agenten anlegen.
2. Kurz- oder Langfassung in die Anweisungen kopieren, Websuche aktivieren.
3. Agent im Chat aufrufen und den Text einfügen.

**Als GPT in ChatGPT:** Das Anweisungsfeld ist auf 8.000 Zeichen begrenzt, also die Kurzfassung nehmen. Ob ihr ohne Abo eigene GPTs anlegen könnt, ist nicht geprüft.

**In Gemini:** Gems laufen aus, einen festen Raum wie dort gibt es dann nicht mehr. Nehmt in Gemini den Skill Faktencheck.

## Das Ergebnis lesen

- Fangt bei den kritischen Befunden an.
- Öffnet die Links selbst. Steht „Snippet“ oder „Nur Snippet-Basis“ dabei, hat Moby nur den Suchtreffer gesehen, nicht die Seite.
- Ein ✅ heißt: zwei unabhängige Quellen gefunden. Es heißt nicht, dass ihr nicht mehr nachschauen müsst.
- Die Verantwortung für euren Text bleibt bei euch.

## Grenzen

- **Erst testen:** Moby läuft nicht in jedem Tool gleich gut. Probiert ihn zuerst mit einem Text aus, dessen Fehler ihr kennt, etwa dem Übungstext aus Kapitel 5. Mehr dazu unter [Erst testen, dann nutzen](../../skills/README.md#erst-testen-dann-nutzen).
- **Ein Status für zwei Fälle:** ❌ heißt bei Moby falsch oder nicht belegt. Wer das getrennt braucht, nimmt den Faktencheck.
- **Keine Bezahlschranken:** Moby umgeht sie nicht. Was er nicht findet, sucht ihr in den [Pressedatenbanken](../../suche/datenbanken.md) eurer Bibliothek.
- **Besser machen:** mit einer eigenen Quellenliste, eurem Material als Dateien im Projekt oder angebundenen Datenbanken. Wie, steht unter [Das würde die Skills noch besser machen](../../skills/README.md#das-würde-die-skills-noch-besser-machen).

## Herkunft

Beruht auf dem Moby, den Florian in der Redaktion nutzt, für verschiedene Plattformen umgebaut.
