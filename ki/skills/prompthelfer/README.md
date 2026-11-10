# Prompthelfer zum Mitnehmen

Der Prompthelfer schreibt mit euch einen Prompt für ein Thema, das ihr euch selbst aussucht, egal welches. Er fragt nach, was ihr vorhabt, schlägt die passende Form vor und liefert einen fertigen Prompt zum Kopieren, dazu kurz, warum er so gebaut ist. Den Prompt setzt ihr dann in einem neuen Chat ein.

Stand: 05.11.2026

## Was er kann

| Ihr wollt … | Er liefert |
|---|---|
| einmal eine Antwort auf eine Frage | eine Einzelfrage: Zweck, Kontext, Frage, Quellen, Output |
| ein Tool selbst suchen lassen (Deep Research, Agent) | einen Agenten-Auftrag: Ziel, erst der Plan, Grenzen, Belege, Format |
| dieselbe Aufgabe öfter erledigen | einen eigenen Skill, kurz genug für jedes Anweisungsfeld |
| euren eigenen Prompt besser machen | eine Rückmeldung mit ✓ ~ ✗ und eine verbesserte Fassung |
| einen Skill aus dem Netz in eurem Chat nutzen | eine Fassung ohne Skripte und Befehle |

Habt ihr erst ein Thema und noch keine Frage, schlägt er euch drei mögliche Zugänge vor.

## Welche Datei wofür

| Datei | Länge | Wofür |
|---|---|---|
| `SKILL.md` | rund 2.700 Wörter, 17.000 Zeichen | Langfassung: in einen Chat einfügen, in ein Projekt legen oder als Skill hochladen |
| `Prompthelfer_kurz.md` | rund 5.200 Zeichen | Kurzfassung für Anweisungsfelder mit Zeichenlimit (GPT, Le-Chat-Agent) oder Chats, in die die Langfassung nicht passt |
| [`prompthelfer.zip`](../zum-hochladen/prompthelfer.zip) im Ordner `zum-hochladen` | – | Paket zum Hochladen in Claude und Gemini |
| `Vorlage_Skill.md` | rund 2.000 Zeichen | leeres Gerüst, um einen Skill ohne KI selbst zu schreiben |

## Voraussetzung

Ein KI-Chat, egal welcher. Der Prompthelfer braucht **keine Websuche**, weil er nur Prompts schreibt und nicht recherchiert. Er läuft also auch in Tools ohne Konto (siehe [Tool-Liste](../../tools/tools.md)). Wie ihr ihn einsetzt, steht in der [Anleitung](../README.md).

Den fertigen Prompt setzt ihr in einem **neuen** Chat ein. Geht es um Fakten, in einem mit Websuche.

## So fragt ihr

Nach dem Einfügen fragt er: „Was ist dein Thema, und was soll die KI für dich tun?“ Dann zum Beispiel:

- „Mein Thema: Dirigentinnen in Deutschland. Ich will einen Überblick für ein Referat.“
- „schnell: Ich brauche Interviewfragen für ein Gespräch mit einer Bühnenbildnerin.“
- „Verbessere meinen Prompt:“ und darunter euren Prompt
- „Ich will mit Deep Research herausfinden, wie sich die Förderung freier Theater in Bayern seit 2020 entwickelt hat.“
- „Ich schreibe jede Woche eine Konzertankündigung. Bau mir einen Skill dafür.“
- „Bau diesen Skill so um, dass er in Gemini läuft:“ und darunter den Text der Datei

Mit „schnell“ bekommt ihr sofort einen Entwurf. Ohne fragt er erst kurz nach, höchstens drei Fragen auf einmal.

## Das Ergebnis lesen

- **Der Prompt steht im Kasten.** Oben rechts am Kasten ist meist ein Kopier-Symbol.
- **[Eckige Klammern]** sind Platzhalter. Ersetzt sie, bevor ihr den Prompt abschickt.
- **„Warum so“** erklärt in zwei, drei Punkten, welcher Baustein was bewirkt. Das ist der Teil, aus dem ihr lernt, wie ihr es beim nächsten Mal selbst macht.
- **Passt die Antwort nicht,** bringt sie zurück: „Die Antwort war zu lang“ oder „Da sind keine Quellen drin“. Er sagt, welcher Baustein gefehlt hat, und schärft den Prompt nach.

## Grenzen

- **Ein guter Prompt macht gute Antworten wahrscheinlicher, nicht sicher.** Öffnet die Quellen selbst, bevor ihr etwas übernehmt. Wie, steht in [KI-Antworten prüfen](../../prompts/ki-antworten-pruefen.md).
- **Keine persönlichen Daten** in Prompts, nur öffentliches Material.
- **Der Prompthelfer ist selbst eine KI.** Was er über Funktionen einzelner Tools sagt, kann veraltet sein.

## Herkunft

Neu für dieses Seminar, nicht aus der Redaktion. Der Prompthelfer baut auf den Checklisten aus Kapitel 4 auf: [Von der Frage zum Auftrag](../../prompts/recherche-auftrag.md) und ROMANE.
