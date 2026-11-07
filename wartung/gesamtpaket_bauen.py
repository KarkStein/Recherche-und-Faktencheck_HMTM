"""Baut das Gesamtpaket: den ganzen Werkzeugkasten in einer ZIP-Datei.

Ziel: gesamtpaket/Werkzeugkasten_Recherche_Faktencheck.zip

Darin:
- Werkzeugkasten.html       alle Seiten in einer Datei, mit Inhaltsverzeichnis
                            und Kopier-Knöpfen, läuft ohne Internet
- Skills_zum_Kopieren/      jeder Skill und Moby als .txt
- Skills_zum_Hochladen/     die Pakete aus skills/zum-hochladen/
- Fuer_KI-Chats/            alle Seiten als eine Markdown-Datei, ohne Skill-Texte
- Spickzettel.pdf, LIESMICH.txt

Aufruf aus dem Hauptordner des Repos:

    python3 wartung/gesamtpaket_bauen.py           # Paket neu bauen
    python3 wartung/gesamtpaket_bauen.py --pruefen # nur prüfen, ob es aktuell ist

Braucht pandoc (Umwandlung von Markdown in HTML). Vorher
wartung/skills_packen.py laufen lassen, damit die Skill-Pakete aktuell sind.

Neue Seiten erscheinen im Paket erst, wenn sie unten in GRUPPEN, TEXTE,
UMLEITUNG oder NICHT_IM_PAKET stehen. Das Skript meldet vergessene Dateien.
"""

import html
import io
import posixpath
import re
import subprocess
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote

WURZEL = Path(__file__).resolve().parent.parent
ZIEL = WURZEL / "gesamtpaket" / "Werkzeugkasten_Recherche_Faktencheck.zip"
ORDNER = "Werkzeugkasten_Recherche_Faktencheck"
REPO_URL = "https://github.com/KarkStein/Recherche-und-Faktencheck_HMTM"
# Feste Zeit im ZIP, damit ein neuer Lauf ohne Änderung dieselbe Datei ergibt.
ZEITSTEMPEL = (2026, 1, 1, 0, 0, 0)

# Seiten der Leseversion in dieser Reihenfolge: Gruppe, dann (Datei, Titel im Inhaltsverzeichnis)
GRUPPEN = [
    ("Start", [("README.md", "Start")]),
    ("Skills", [
        ("skills/README.md", "Überblick und Anleitung"),
        ("skills/faktencheck/README.md", "Faktencheck"),
        ("skills/herkunftscheck/README.md", "Herkunftscheck"),
        ("skills/themenrecherche/README.md", "Themenrecherche"),
        ("skills/expertenmeinungen/README.md", "Expertenmeinungen"),
        ("skills/pdb-helfer/README.md", "PDB-Helfer"),
        ("skills/prompthelfer/README.md", "Prompthelfer"),
        ("skills/prompthelfer/Vorlage_Skill.md", "Vorlage für eigene Skills"),
        ("skills/zum-hochladen/README.md", "Pakete zum Hochladen"),
    ]),
    ("Assistent", [("agent/moby/README.md", "Moby")]),
    ("Prompten", [
        ("prompts/recherche-auftrag.md", "Von der Frage zum Auftrag"),
        ("prompts/ki-antworten-pruefen.md", "KI-Antworten prüfen"),
    ]),
    ("KI-Tools", [
        ("ki-tools/tools.md", "Alle Tools mit Link"),
        ("ki-tools/neue-tools-finden.md", "Neue KI-Tools finden"),
    ]),
    ("Suchen", [
        ("suche/google-operatoren.md", "Google"),
        ("suche/datenbanken.md", "Datenbanken"),
    ]),
    ("Links", [("links/kultur.md", "Kulturthemen")]),
]

# Texte zum Kopieren: (Quelle, Datei im Paket, Seite mit Kopier-Kasten oder None, Beschriftung)
TEXTE = [
    ("skills/faktencheck/SKILL.md", "Faktencheck.txt", "skills/faktencheck/README.md", "Langfassung"),
    ("skills/herkunftscheck/SKILL.md", "Herkunftscheck.txt", "skills/herkunftscheck/README.md", "Langfassung"),
    ("skills/herkunftscheck/Herkunftscheck_kurz.md", "Herkunftscheck_kurz.txt", "skills/herkunftscheck/README.md", "Kurzfassung"),
    ("skills/themenrecherche/SKILL.md", "Themenrecherche.txt", "skills/themenrecherche/README.md", "Langfassung"),
    ("skills/themenrecherche/Themenrecherche_kurz.md", "Themenrecherche_kurz.txt", "skills/themenrecherche/README.md", "Kurzfassung"),
    ("skills/expertenmeinungen/SKILL.md", "Expertenmeinungen.txt", "skills/expertenmeinungen/README.md", "Langfassung"),
    ("skills/expertenmeinungen/Expertenmeinungen_kurz.md", "Expertenmeinungen_kurz.txt", "skills/expertenmeinungen/README.md", "Kurzfassung"),
    ("skills/pdb-helfer/SKILL.md", "PDB-Helfer.txt", "skills/pdb-helfer/README.md", "Langfassung"),
    ("skills/prompthelfer/SKILL.md", "Prompthelfer.txt", "skills/prompthelfer/README.md", "Langfassung"),
    ("skills/prompthelfer/Prompthelfer_kurz.md", "Prompthelfer_kurz.txt", "skills/prompthelfer/README.md", "Kurzfassung"),
    ("skills/prompthelfer/Vorlage_Skill.md", "Vorlage_Skill.txt", None, "Vorlage"),
    ("agent/moby/Moby_Faktencheck.md", "Moby_Faktencheck.txt", "agent/moby/README.md", "Langfassung"),
    ("agent/moby/Moby_kurz.md", "Moby_kurz.txt", "agent/moby/README.md", "Kurzfassung"),
]

# Ordner-Seiten, die in der Leseversion keine eigene Seite haben: Links darauf führen hierhin
UMLEITUNG = {
    "agent/README.md": "agent/moby/README.md",
    "prompts/README.md": "prompts/recherche-auftrag.md",
    "ki-tools/README.md": "ki-tools/tools.md",
    "suche/README.md": "suche/google-operatoren.md",
    "links/README.md": "links/kultur.md",
    "gesamtpaket/README.md": "#ueber-diese-datei",
    "LICENSE": "README.md#lizenz",
}

# Seiten nur für die Pflege: Links darauf werden in der Leseversion zu normalem Text
NICHT_IM_PAKET = {"wartung/README.md"}

SPICKZETTEL = "ki-tools/spickzettel.pdf"


def seiten():
    for _, eintraege in GRUPPEN:
        for pfad, titel in eintraege:
            yield pfad, titel


def seiten_id(pfad: str) -> str:
    teile = pfad.split("/")
    if teile[-1] == "README.md":
        name = teile[-2] if len(teile) > 1 else "start"
    else:
        name = teile[-1].rsplit(".", 1)[0]
    return re.sub(r"[^a-z0-9-]", "-", name.lower())


def text_id(datei: str) -> str:
    return "t-" + re.sub(r"[^a-z0-9-]", "-", datei.rsplit(".", 1)[0].lower())


def lesen(pfad: str) -> str:
    return (WURZEL / pfad).read_text(encoding="utf-8")


def stand_ermitteln() -> str:
    """Das jüngste Datum aus allen Zeilen „Stand …: TT.MM.JJJJ“ der Seiten."""
    daten = []
    for pfad, _ in seiten():
        for t, m, j in re.findall(r"Stand[^0-9\n]{0,40}?(\d{2})\.(\d{2})\.(\d{4})", lesen(pfad)):
            daten.append((j, m, t))
    j, m, t = max(daten)
    return f"{t}.{m}.{j}"


def ziel_aufloesen(link: str, von: str, warnungen: list):
    """Ordnet einem Link aus einer Seite sein Ziel zu.

    Rückgabe: ("extern", url) | ("anker", "#id") | ("datei", pfad_im_paket) | ("text", None)
    """
    if re.match(r"^(https?:|mailto:)", link):
        return "extern", link
    pfad, _, anker = link.partition("#")
    anker = unquote(anker)
    if not pfad:
        return "anker", f"#{seiten_id(von)}--{anker}" if anker else f"#{seiten_id(von)}"
    pfad = unquote(pfad)
    voll = posixpath.normpath(posixpath.join(posixpath.dirname(von), pfad))
    if pfad.endswith("/") or (WURZEL / voll).is_dir():
        voll = posixpath.join(voll, "README.md")
    if voll in UMLEITUNG:
        umleitung = UMLEITUNG[voll]
        if umleitung.startswith("#"):
            return "anker", umleitung
        voll, _, neuer_anker = umleitung.partition("#")
        anker = anker or neuer_anker
    if voll in NICHT_IM_PAKET:
        return "text", None
    seitenpfade = {p for p, _ in seiten()}
    if voll in seitenpfade:
        return "anker", f"#{seiten_id(voll)}--{anker}" if anker else f"#{seiten_id(voll)}"
    for quelle, datei, kasten, _ in TEXTE:
        if voll == quelle:
            return "anker", f"#{text_id(datei)}"
    if voll == SPICKZETTEL:
        return "datei", "Spickzettel.pdf"
    if voll.startswith("skills/zum-hochladen/") and voll.endswith(".zip"):
        return "datei", "Skills_zum_Hochladen/" + posixpath.basename(voll)
    warnungen.append(f"Link ohne Ziel im Paket: {link} (in {von})")
    return "text", None


def pandoc(text: str) -> str:
    ergebnis = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html", "--wrap=none"],
        input=text.encode("utf-8"), capture_output=True, check=True,
    )
    return ergebnis.stdout.decode("utf-8")


def seite_html(pfad: str, warnungen: list) -> str:
    pid = seiten_id(pfad)
    rumpf = pandoc(lesen(pfad))
    rumpf = re.sub(r' id="([^"]+)"', lambda m: f' id="{pid}--{m.group(1)}"', rumpf)

    def link_ersetzen(m):
        inhalt, href = m.group(2), html.unescape(m.group(1))
        art, ziel = ziel_aufloesen(href, pfad, warnungen)
        if art == "extern":
            return f'<a href="{html.escape(ziel)}" target="_blank" rel="noopener">{inhalt}</a>'
        if art == "text":
            return inhalt
        return f'<a href="{html.escape(ziel)}">{inhalt}</a>'

    rumpf = re.sub(r'<a href="([^"]*)">(.*?)</a>', link_ersetzen, rumpf, flags=re.S)
    rumpf = rumpf.replace("<table>", '<div class="tabelle"><table>').replace("</table>", "</table></div>")
    # Erste Überschrift bekommt die Seiten-ID, damit Links auf die Seite oben landen
    rumpf = re.sub(r"<h1 id=\"[^\"]+\">", f'<h1 id="{pid}">', rumpf, count=1)

    kaesten = []
    for quelle, datei, kasten, beschriftung in TEXTE:
        if kasten != pfad:
            continue
        text = lesen(quelle)
        zeichen = f"{round(len(text) / 100) * 100:,}".replace(",", ".")
        kaesten.append(
            f'<details class="skilltext" id="{text_id(datei)}">'
            f"<summary><span class=\"titel\">{beschriftung} zum Kopieren</span>"
            f' <span class="info">{datei} · rund {zeichen} Zeichen</span></summary>'
            f'<div class="kastenkopf"><button type="button" class="kopieren" data-ziel="{text_id(datei)}-text">Text kopieren</button>'
            f"<span>Dieselbe Datei liegt im Ordner <code>Skills_zum_Kopieren</code>.</span></div>"
            f'<pre class="rohtext" id="{text_id(datei)}-text">{html.escape(text)}</pre></details>'
        )
    if kaesten:
        rumpf += '<div class="kaesten"><h2>Zum Kopieren</h2>' + "".join(kaesten) + "</div>"

    return (
        f'<section class="seite">{rumpf}'
        f'<p class="seitenfuss"><a href="#inhalt">Zum Inhaltsverzeichnis</a> · '
        f'<a href="{REPO_URL}/blob/main/{pfad}" target="_blank" rel="noopener">Diese Seite auf GitHub</a></p>'
        f"</section>"
    )


CSS = """
:root{--bg:#fbfaf7;--fl:#ffffff;--tx:#1d1d1b;--tx2:#5a5a55;--rand:#e2dfd6;--akz:#9b2c2c;--akz2:#f6e9e6;--code:#f2f0ea;--link:#1f5f8b}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#161615;--fl:#1f1f1d;--tx:#ecebe6;--tx2:#a9a8a1;--rand:#3a3935;--akz:#e08a7e;--akz2:#3a2522;--code:#262623;--link:#7fb8e0}}
:root[data-theme="dark"]{--bg:#161615;--fl:#1f1f1d;--tx:#ecebe6;--tx2:#a9a8a1;--rand:#3a3935;--akz:#e08a7e;--akz2:#3a2522;--code:#262623;--link:#7fb8e0}
*{box-sizing:border-box}
html{scroll-padding-top:1rem}
body{margin:0;background:var(--bg);color:var(--tx);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;-webkit-text-size-adjust:100%}
a{color:var(--link)}
.rahmen{display:grid;grid-template-columns:17rem minmax(0,1fr);max-width:76rem;margin:0 auto}
nav{position:sticky;top:0;align-self:start;max-height:100vh;overflow:auto;padding:1.5rem 1rem 2rem 1.25rem;border-right:1px solid var(--rand);font-size:.92rem}
nav summary{font-weight:700;cursor:pointer;margin-bottom:.5rem}
nav h3{font-size:.75rem;text-transform:uppercase;letter-spacing:.06em;color:var(--tx2);margin:1.1rem 0 .3rem}
nav ul{list-style:none;margin:0;padding:0}
nav li a{display:block;padding:.2rem .5rem;border-radius:.3rem;text-decoration:none;color:var(--tx)}
nav li a:hover{background:var(--akz2)}
main{padding:2rem 2.5rem 4rem;min-width:0}
header.kopf{border-bottom:3px solid var(--akz);padding-bottom:1rem;margin-bottom:1.5rem}
header.kopf h1{margin:0 0 .3rem;font-size:2rem;line-height:1.2}
header.kopf p{margin:.2rem 0;color:var(--tx2)}
.hinweis{background:var(--fl);border:1px solid var(--rand);border-left:4px solid var(--akz);border-radius:.4rem;padding:.8rem 1.1rem;margin:1rem 0 2rem}
.hinweis h2{font-size:1.05rem;margin:.2rem 0 .4rem}
.hinweis ul{margin:.3rem 0;padding-left:1.2rem}
.seite{border-top:1px solid var(--rand);padding-top:1.5rem;margin-top:2.5rem}
.seite h1{font-size:1.65rem;line-height:1.25;margin:.2rem 0 1rem}
.seite h2{font-size:1.25rem;margin:1.8rem 0 .6rem}
.seite h3{font-size:1.05rem;margin:1.4rem 0 .4rem}
.tabelle{overflow-x:auto;margin:1rem 0}
table{border-collapse:collapse;width:100%;font-size:.93rem;background:var(--fl)}
th,td{border:1px solid var(--rand);padding:.45rem .6rem;text-align:left;vertical-align:top}
th{background:var(--code)}
code{background:var(--code);padding:.08rem .3rem;border-radius:.25rem;font-size:.88em;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;overflow-wrap:anywhere}
pre{position:relative;background:var(--code);border:1px solid var(--rand);border-radius:.4rem;padding:2.4rem .9rem .9rem;overflow-x:auto;white-space:pre-wrap;word-break:break-word;font-size:.85rem;line-height:1.5}
pre code{background:none;padding:0;font-size:inherit}
button.kopieren{font:inherit;font-size:.82rem;cursor:pointer;border:1px solid var(--rand);background:var(--fl);color:var(--tx);border-radius:.3rem;padding:.25rem .65rem}
button.kopieren:hover{border-color:var(--akz)}
pre > button.kopieren{position:absolute;top:.45rem;right:.45rem}
.kaesten{margin-top:2rem}
details.skilltext{border:1px solid var(--rand);border-radius:.45rem;background:var(--fl);margin:.6rem 0}
details.skilltext summary{cursor:pointer;padding:.7rem 1rem;display:flex;flex-wrap:wrap;gap:.2rem .8rem;align-items:baseline}
details.skilltext summary .titel{font-weight:650}
details.skilltext summary .info{color:var(--tx2);font-size:.88rem}
details.skilltext[open] summary{border-bottom:1px solid var(--rand)}
.kastenkopf{display:flex;flex-wrap:wrap;gap:.5rem 1rem;align-items:center;padding:.7rem 1rem 0;color:var(--tx2);font-size:.88rem}
pre.rohtext{margin:.7rem 1rem 1rem;padding-top:.9rem;max-height:28rem;overflow:auto}
.seitenfuss{margin-top:2rem;font-size:.85rem;color:var(--tx2)}
@media (max-width:900px){
 .rahmen{display:block}
 nav{position:static;max-height:none;border-right:0;border-bottom:1px solid var(--rand);padding:1rem 16px}
 main{padding:1.2rem 16px 3rem}
 header.kopf h1{font-size:1.6rem}
}
@media print{nav,button.kopieren,.seitenfuss{display:none}.rahmen{display:block}main{padding:0}body{background:#fff;color:#000;font-size:11pt}a{color:#000}pre{white-space:pre-wrap}}
"""

JS = """
function altKopieren(text){var t=document.createElement('textarea');t.value=text;t.setAttribute('readonly','');t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();var ok=false;try{ok=document.execCommand('copy')}catch(e){}document.body.removeChild(t);return ok}
function kopieren(text,knopf){var alt=knopf.textContent;function fertig(ok){knopf.textContent=ok?'Kopiert ✓':'Bitte markieren und kopieren';setTimeout(function(){knopf.textContent=alt},1800)}
 if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(text).then(function(){fertig(true)},function(){fertig(altKopieren(text))})}else{fertig(altKopieren(text))}}
document.querySelectorAll('pre:not(.rohtext)').forEach(function(pre){var b=document.createElement('button');b.type='button';b.className='kopieren';b.textContent='Kopieren';b.addEventListener('click',function(){var c=pre.querySelector('code');kopieren((c||pre).textContent,b)});pre.appendChild(b)});
document.querySelectorAll('button.kopieren[data-ziel]').forEach(function(b){b.addEventListener('click',function(){kopieren(document.getElementById(b.dataset.ziel).textContent,b)})});
function zielOeffnen(){if(!location.hash)return;var el=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(el&&el.tagName==='DETAILS'){el.open=true;el.scrollIntoView()}}
window.addEventListener('hashchange',zielOeffnen);zielOeffnen();
var toc=document.getElementById('toc');function schmal(){return window.matchMedia('(max-width:900px)').matches}
if(schmal())toc.open=false;
toc.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){if(schmal())toc.open=false})});
"""


def html_bauen(stand: str, warnungen: list) -> str:
    nav = ['<details open id="toc"><summary>Inhalt</summary>']
    for gruppe, eintraege in GRUPPEN:
        nav.append(f"<h3>{html.escape(gruppe)}</h3><ul>")
        for pfad, titel in eintraege:
            nav.append(f'<li><a href="#{seiten_id(pfad)}">{html.escape(titel)}</a></li>')
        nav.append("</ul>")
    nav.append('<h3>Dateien</h3><ul><li><a href="Spickzettel.pdf">Spickzettel (PDF)</a></li></ul></details>')

    hinweis = f"""
<div class="hinweis" id="ueber-diese-datei">
<h2>So benutzt ihr diese Datei</h2>
<ul>
<li>Das <a href="#inhalt">Inhaltsverzeichnis</a> führt zu allen Seiten. Links nach außen öffnen sich in einem neuen Tab und brauchen Internet.</li>
<li>Unter der Beschreibung jedes Skills und von Moby stehen die Texte zum Kopieren: aufklappen, „Text kopieren“, in einen KI-Chat einfügen.</li>
<li>Wo im Text von GitHub die Rede ist (Kopier-Symbol, „Copy raw file“, Download), gilt hier: der Knopf am Kasten oder die Dateien in den Ordnern neben dieser Datei.</li>
<li>Die aktuelle Fassung liegt immer auf <a href="{REPO_URL}" target="_blank" rel="noopener">GitHub</a>.</li>
</ul>
</div>"""

    teile = [seite_html(pfad, warnungen) for pfad, _ in seiten()]
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Werkzeugkasten Recherche und Faktencheck</title>
<style>{CSS}</style>
</head>
<body>
<div class="rahmen">
<nav id="inhalt" aria-label="Inhalt">{''.join(nav)}</nav>
<main>
<header class="kopf">
<h1>Werkzeugkasten Recherche und Faktencheck</h1>
<p>Seminar „Recherche und Faktencheck“, Master Kulturjournalismus, Hochschule für Musik und Theater München, 05./06.11.2026</p>
<p>Stand: {stand} · Lizenz: CC BY 4.0</p>
</header>
{hinweis}
{''.join(teile)}
</main>
</div>
<script>{JS}</script>
</body>
</html>
"""


def ki_datei_bauen(stand: str, warnungen: list) -> str:
    titel_von = {}
    for pfad, _ in seiten():
        m = re.search(r"^# (.+)$", lesen(pfad), re.M)
        titel_von[pfad] = m.group(1).strip() if m else pfad

    def links_umschreiben(text: str, von: str) -> str:
        def ersetzen(m):
            inhalt, href = m.group(1), m.group(2)
            art, ziel = ziel_aufloesen(href, von, [])
            if art == "extern":
                return m.group(0)
            if art == "datei":
                return f"{inhalt} (Datei {ziel})"
            if art == "anker" and ziel.startswith("#t-"):
                datei = next(d for _, d, _, _ in TEXTE if text_id(d) == ziel[1:])
                return f"{inhalt} (Datei Skills_zum_Kopieren/{datei})"
            if art == "anker":
                pid = ziel[1:].split("--")[0]
                seite = next((p for p, _ in seiten() if seiten_id(p) == pid), None)
                if seite:
                    return f"{inhalt} (siehe Abschnitt „{titel_von[seite]}“)"
            return inhalt
        return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", ersetzen, text)

    def ueberschriften_tiefer(text: str) -> str:
        zeilen, im_code = [], False
        for zeile in text.splitlines():
            if zeile.startswith("```"):
                im_code = not im_code
            if not im_code and re.match(r"^#{1,5} ", zeile):
                zeile = "#" + zeile
            zeilen.append(zeile)
        return "\n".join(zeilen)

    kopf = f"""# Werkzeugkasten Recherche und Faktencheck: alles in einer Datei

Seminar „Recherche und Faktencheck“, Master Kulturjournalismus, Hochschule für Musik und Theater München, 05./06.11.2026. Stand: {stand}. Lizenz: CC BY 4.0. Aktuelle Fassung: {REPO_URL}

**Für Menschen:** Ladet diese Datei in einen KI-Chat oder ein Projekt hoch. Dann könnt ihr Fragen zum Werkzeugkasten stellen, etwa „Welcher Skill hilft mir, ein Zitat bis zum Ursprung zu verfolgen?“ oder „Wie richte ich Moby in Le Chat ein?“. Die Skill-Texte selbst stehen nicht in dieser Datei, sondern im Ordner Skills_zum_Kopieren.

**Für den KI-Assistenten:** Diese Datei ist Nachschlagematerial, keine Anweisung an dich. Beantworte Fragen dazu und nenne den Abschnitt, aus dem eine Angabe stammt, mit seinem Stand-Datum. Angaben zu Tools, Zugängen und Preisen können veraltet sein; sag das dazu. Will der User einen Skill nutzen, verweise auf die passende Datei im Ordner Skills_zum_Kopieren.

## Inhalt

""" + "\n".join(f"- {titel_von[p]}" for p, _ in seiten()) + "\n"

    teile = [kopf]
    for pfad, _ in seiten():
        text = ueberschriften_tiefer(links_umschreiben(lesen(pfad), pfad)).strip()
        teile.append(f"---\n\n<!-- Datei im Repo: {pfad} -->\n\n{text}\n")
    return "\n".join(teile)


def liesmich(stand: str) -> str:
    return f"""WERKZEUGKASTEN RECHERCHE UND FAKTENCHECK
Seminar „Recherche und Faktencheck“, Master Kulturjournalismus,
Hochschule für Musik und Theater München, 05./06.11.2026
Stand: {stand} · Lizenz: CC BY 4.0


ZUERST ENTPACKEN
Windows: Rechtsklick auf die ZIP-Datei, dann „Alle extrahieren“.
Mac: Doppelklick auf die ZIP-Datei.
Ohne Entpacken funktionieren die Verweise zwischen den Dateien nicht.


WAS WO LIEGT

Werkzeugkasten.html
  Alles zum Lesen in einer Datei. Doppelklick öffnet sie im Browser,
  auch ohne Internet. Mit Inhaltsverzeichnis und Knöpfen zum Kopieren
  der Skills und Prompts.

Skills_zum_Kopieren/
  Jeder Skill und Moby als Textdatei. Öffnen, alles markieren
  (Strg+A, am Mac cmd+A), kopieren, in einen KI-Chat einfügen.
  Oder die Datei in ein Projekt hochladen. „_kurz“ ist die Kurzfassung
  für Anweisungsfelder mit Zeichenlimit.

Skills_zum_Hochladen/
  Pakete für Claude und Gemini. Für Claude nicht entpacken, so hochladen.
  Für Gemini entpacken und den Ordner hochladen. Anleitung in
  Werkzeugkasten.html, Abschnitt „Skills: Überblick und Anleitung“.

Fuer_KI-Chats/
  Der ganze Werkzeugkasten als eine Textdatei, ohne die Skill-Texte.
  In einen KI-Chat hochladen, dann beantwortet er Fragen dazu.

Spickzettel.pdf
  Der Spickzettel zu KI-Tools aus dem Seminar.


IN ZWEI MINUTEN LOSLEGEN
1. Skills_zum_Kopieren/Moby_Faktencheck.txt öffnen, alles markieren, kopieren.
2. In einen KI-Chat mit Websuche einfügen und abschicken.
3. Nächste Nachricht: „Prüfe diesen Text:“ und darunter euer Text.
Eigenes Thema? Dasselbe mit Prompthelfer.txt.


SPIELREGELN FÜR KI
1. Ein Konto ist freiwillig. Jede Übung geht auch ohne.
2. Keine Namen, Telefonnummern oder anderen persönlichen Daten in Prompts.
3. Nur Dokumente hochladen, die schon öffentlich zugänglich sind.
4. Wo es geht: Verlauf aus, Training abwählen.
5. Jeder Link wird geöffnet. Was nicht geöffnet wurde, gilt als nicht verifiziert.
6. KI-Text, den ihr übernehmt, kennzeichnet ihr.


AKTUELLE FASSUNG
{REPO_URL}
"""


def vergessene_dateien() -> list:
    bekannt = {p for p, _ in seiten()} | {q for q, _, _, _ in TEXTE} | set(UMLEITUNG) | NICHT_IM_PAKET
    alle = {str(p.relative_to(WURZEL)) for p in WURZEL.rglob("*.md") if ".git" not in p.parts}
    return sorted(alle - bekannt)


def anker_pruefen(seite: str, warnungen: list):
    ids = set(re.findall(r' id="([^"]+)"', seite))
    for ziel in re.findall(r'href="#([^"]+)"', seite):
        if html.unescape(ziel) not in ids:
            warnungen.append(f"Sprungmarke fehlt: #{html.unescape(ziel)}")


def paket_bauen():
    warnungen = []
    stand = stand_ermitteln()
    leseversion = html_bauen(stand, warnungen)
    anker_pruefen(leseversion, warnungen)
    eintraege = [
        ("LIESMICH.txt", liesmich(stand).encode("utf-8")),
        ("Werkzeugkasten.html", leseversion.encode("utf-8")),
        ("Spickzettel.pdf", (WURZEL / SPICKZETTEL).read_bytes()),
        ("Fuer_KI-Chats/Werkzeugkasten_fuer_KI.md", ki_datei_bauen(stand, warnungen).encode("utf-8")),
    ]
    for quelle, datei, _, _ in TEXTE:
        eintraege.append((f"Skills_zum_Kopieren/{datei}", (WURZEL / quelle).read_bytes()))
    for paket in sorted((WURZEL / "skills" / "zum-hochladen").glob("*.zip")):
        eintraege.append((f"Skills_zum_Hochladen/{paket.name}", paket.read_bytes()))

    puffer = io.BytesIO()
    with zipfile.ZipFile(puffer, "w", zipfile.ZIP_DEFLATED) as z:
        for name, inhalt in eintraege:
            info = zipfile.ZipInfo(f"{ORDNER}/{name}", date_time=ZEITSTEMPEL)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, inhalt)
    return puffer.getvalue(), stand, warnungen, eintraege


def main() -> int:
    nur_pruefen = "--pruefen" in sys.argv
    probleme = 0
    for datei in vergessene_dateien():
        print(f"FEHLT IN DER LISTE {datei} (in GRUPPEN, TEXTE, UMLEITUNG oder NICHT_IM_PAKET eintragen)")
        probleme += 1
    neu, stand, warnungen, eintraege = paket_bauen()
    for w in warnungen:
        print(f"WARNUNG {w}")
    probleme += len(warnungen)
    aktuell = ZIEL.exists() and ZIEL.read_bytes() == neu
    rel = ZIEL.relative_to(WURZEL)
    if nur_pruefen:
        print(f"{'ok' if aktuell else 'VERALTET'} {rel}")
        probleme += 0 if aktuell else 1
    else:
        ZIEL.parent.mkdir(exist_ok=True)
        if not aktuell:
            ZIEL.write_bytes(neu)
        print(f"{'gebaut' if not aktuell else 'unverändert'} {rel} "
              f"(Stand {stand}, {len(eintraege)} Dateien, {len(neu) // 1024} KB)")
    return 1 if probleme else 0


if __name__ == "__main__":
    sys.exit(main())
