"""Baut aus jeder ki/skills/<name>/SKILL.md ein Paket zum Hochladen.

Das Paket ki/skills/zum-hochladen/<name>.zip enthält nur den Ordner <name>/
mit der Datei SKILL.md. So erwarten es Claude und Gemini: Der Ordner heißt
wie der Skill, darin liegt SKILL.md.

Aufruf aus dem Hauptordner des Repos:

    python3 wartung/skills_packen.py           # Pakete neu bauen
    python3 wartung/skills_packen.py --pruefen # nur prüfen, ob alles aktuell ist

Vorher prüft das Skript den Kopf jeder SKILL.md:
- name: klein, Ziffern und Bindestriche, höchstens 64 Zeichen, gleich dem Ordnernamen
- description: vorhanden, höchstens 1.024 Zeichen, keine spitzen Klammern

Nach jeder Änderung an einer SKILL.md das Skript laufen lassen und die
ZIP-Dateien mit committen.
"""

import re
import sys
import zipfile
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
SKILLS = WURZEL / "ki" / "skills"
ZIEL = SKILLS / "zum-hochladen"
NAME_MUSTER = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# Feste Zeit im ZIP, damit ein neuer Lauf ohne Änderung dieselbe Datei ergibt.
ZEITSTEMPEL = (2026, 1, 1, 0, 0, 0)


def kopf_lesen(text: str) -> dict:
    """Liest name und description aus dem Kopf zwischen den ersten beiden ---."""
    if not text.startswith("---\n"):
        raise ValueError("Die Datei beginnt nicht mit einem Kopf (---).")
    ende = text.find("\n---\n", 4)
    if ende == -1:
        raise ValueError("Der Kopf wird nicht mit --- abgeschlossen.")
    felder = {}
    for zeile in text[4:ende].splitlines():
        schluessel, _, wert = zeile.partition(":")
        wert = wert.strip()
        if len(wert) >= 2 and wert[0] == wert[-1] == '"':
            wert = wert[1:-1]
        felder[schluessel.strip()] = wert
    return felder


def pruefen(ordner: Path, kopf: dict) -> list:
    fehler = []
    name = kopf.get("name", "")
    beschreibung = kopf.get("description", "")
    if not NAME_MUSTER.match(name) or len(name) > 64:
        fehler.append(f"name „{name}“: nur Kleinbuchstaben, Ziffern und Bindestriche, höchstens 64 Zeichen")
    if name != ordner.name:
        fehler.append(f"name „{name}“ passt nicht zum Ordner „{ordner.name}“")
    if not beschreibung:
        fehler.append("description fehlt")
    if len(beschreibung) > 1024:
        fehler.append(f"description hat {len(beschreibung)} Zeichen, erlaubt sind 1.024")
    if "<" in beschreibung or ">" in beschreibung:
        fehler.append("description enthält spitze Klammern")
    return fehler


def zip_bauen(name: str, inhalt: bytes) -> bytes:
    from io import BytesIO

    puffer = BytesIO()
    with zipfile.ZipFile(puffer, "w", zipfile.ZIP_DEFLATED) as z:
        info = zipfile.ZipInfo(f"{name}/SKILL.md", date_time=ZEITSTEMPEL)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        z.writestr(info, inhalt)
    return puffer.getvalue()


def main() -> int:
    nur_pruefen = "--pruefen" in sys.argv
    probleme = 0
    erwartet = set()
    for skill_datei in sorted(SKILLS.glob("*/SKILL.md")):
        ordner = skill_datei.parent
        inhalt = skill_datei.read_bytes()
        try:
            kopf = kopf_lesen(inhalt.decode("utf-8"))
        except ValueError as e:
            print(f"FEHLER {ordner.name}: {e}")
            probleme += 1
            continue
        fehler = pruefen(ordner, kopf)
        for f in fehler:
            print(f"FEHLER {ordner.name}: {f}")
        probleme += len(fehler)
        if fehler:
            continue
        name = kopf["name"]
        ziel = ZIEL / f"{name}.zip"
        erwartet.add(ziel.name)
        neu = zip_bauen(name, inhalt)
        aktuell = ziel.exists() and ziel.read_bytes() == neu
        if nur_pruefen:
            if not aktuell:
                print(f"VERALTET {ziel.relative_to(WURZEL)}")
                probleme += 1
            else:
                print(f"ok {ziel.relative_to(WURZEL)}")
        else:
            ZIEL.mkdir(exist_ok=True)
            if not aktuell:
                ziel.write_bytes(neu)
            print(f"{'gebaut' if not aktuell else 'unverändert'} {ziel.relative_to(WURZEL)} "
                  f"({len(kopf['description'])} Zeichen Beschreibung)")
    for alt in sorted(ZIEL.glob("*.zip")) if ZIEL.exists() else []:
        if alt.name not in erwartet:
            print(f"ÜBERZÄHLIG {alt.relative_to(WURZEL)} (kein Skill-Ordner dazu)")
            probleme += 1
    return 1 if probleme else 0


if __name__ == "__main__":
    sys.exit(main())
