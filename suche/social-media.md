# Social Media durchsuchen

Aus Kapitel 5 der Seminarfolien (Abschnitt Social Media). Stand: 05.11.2026.

**Prüfstufe:** übernommen aus den Folien.

## Bevor ihr sucht

- **Sucht mit einem Recherche-Konto,** getrennt vom privaten, mit eigener E-Mail-Adresse.
- **Ihr hinterlasst Spuren.** Wer eine Instagram-Story ansieht, steht in der Zuschauerliste. TikTok zeigt Profilbesuche, wenn beide Seiten den Profilverlauf eingeschaltet haben.
- **Wer Kontakt aufnimmt, gibt sich zu erkennen.** Verdeckt recherchieren geht nur ausnahmsweise, bei besonderem öffentlichem Interesse (Pressekodex, Ziffer 4).

## Wie sucht man wo?

Drei Suchwege gehen überall:

| Suche | Findet |
|---|---|
| `@Name` | Personen und Gruppen |
| `#Hashtag` | Themen und Kampagnen |
| Stichwort | Posts und Profile |

Dazu von außen, ohne Konto: Google mit `site:`, etwa `site:tiktok.com Kammerspiele`.

Jede Plattform hat außerdem eine Besonderheit:

| Plattform | Was nur hier geht |
|---|---|
| X | echte Suchoperatoren wie `from:` und `since:` (siehe unten); suchen nur mit Login |
| Facebook | Filter „Neueste Beiträge“ und „Datum“, beim Datum aber nur nach Jahr |
| Instagram | Ortsseiten; im Profil „Info zu diesem Konto“: Beitritt, Land, wie oft der Name geändert wurde |
| Telegram | öffentliche Kanäle ohne Konto im Browser lesen und durchsuchen |
| TikTok | Filter Datum (bis drei Monate) und Sortieren nach Likes |

## X: suchen mit Operatoren

| Operator | Wirkung |
|---|---|
| `"Münchner Kammerspiele"` | genau diese Wortfolge |
| `-Kino` | Wort ausschließen |
| `OR` | eins von beiden |
| `from:konto` | nur Posts dieses Kontos |
| `to:konto`, `@konto` | Antworten an das Konto, Posts, die es erwähnen |
| `since:2026-07-16` | ab diesem Tag |
| `until:2026-07-20` | bis vor diesem Tag |
| `min_faves:20` | mindestens 20 Likes (`min_retweets:`, `min_replies:` entsprechend) |
| `filter:images` | nur Posts mit Bildern (`filter:videos`, `filter:media`, `filter:links` entsprechend) |
| `lang:de` | nur Posts auf Deutsch |
| `url:muenchen.de` | Posts mit einem Link auf diese Seite |

Alle Operatoren gibt es auch als Formular: [x.com/search-advanced](https://x.com/search-advanced). Ortssuchen wie `near:` sind unzuverlässig, weil nur wenige Posts Ortsdaten haben. Dienste, die X ohne Konto zeigten, sind seit September 2026 offline.

## Die Adresse verrät mehr

Oft kommt ihr weiter, wenn ihr eine Adresse direkt eintippt, statt die Suche der Plattform zu nehmen.

| Plattform | Adresse | Was ihr bekommt |
|---|---|---|
| Instagram | `instagram.com/NAME/tagged/` | Posts anderer, in denen das Konto markiert ist |
| Facebook | [facebook.com/ads/library](https://www.facebook.com/ads/library) | alle Anzeigen einer Seite, ohne Login |
| Facebook | Seite, dann „Seitentransparenz“ | Erstelldatum, frühere Namen, Land der Verwalter |
| X | die lange Zahl am Ende von `x.com/NAME/status/…` | in [TweetedAt](https://oduwsdl.github.io/tweetedat/) eingefügt: Datum und Uhrzeit des Posts, auch wenn er gelöscht ist |
| X | `x.com/NAME/media` | nur Bilder und Videos des Kontos |
| Telegram | `t.me/s/KANAL` | die letzten Posts eines öffentlichen Kanals, ohne Konto |
| Telegram | `t.me/s/KANAL?q=Wort` | Suche im Kanal, auch nach Hashtags und Wortteilen |
| Telegram | `t.me/KANAL/123?embed=1` | ein einzelner Post mit Datum, ohne Konto |
| TikTok | `tiktok.com/tag/HASHTAG` | alle öffentlichen Videos zum Hashtag, ohne Login |
| TikTok | `tiktok.com/@NAME` | das Profil, ohne Login |

**Google als Umweg:**

- `site:` mit Pfad: `site:instagram.com/p/ "Kammerspiele"`, `site:facebook.com/groups "Kammerspiele"`, `site:tiktok.com/@ "Kammerspiele"`, `site:t.me/s/ "Wort"`.
- Zeitraum: `after:2026-07-01 before:2026-08-01`.
- Wo ein Konto anderswo verlinkt ist, auf Websites, in der Presse, auf anderen Plattformen: `"instagram.com/NAME" -site:instagram.com`.

Mehr zu den Google-Operatoren steht in [Suchen im Web](google-operatoren.md).

## Werkzeuge

| Werkzeug | Was es kann | Zugang |
|---|---|---|
| [InVID-WeVerify-Plugin](https://bellingcat.gitbook.io/toolkit/more/all-tools/invid) | zerlegt Videos aus Posts: Standbilder für die Rückwärtssuche, Metadaten, Lupe | kostenlos, Browser-Erweiterung für Chrome und Edge; die KI-Erkennung braucht eine Registrierung |
| [Who posted what?](https://bellingcat.gitbook.io/toolkit/more/all-tools/who-posted-what) | findet Facebook-Posts nach Stichwort und Tag, genauer als die Facebook-Suche | kostenlos, nur mit Facebook-Login |
| [TikTok Timestamp](https://bellingcat.github.io/tiktok-timestamp/) | Video-Adresse einfügen: Uploadzeit auf die Sekunde, auch bei gelöschten Videos | ohne Anmeldung |
| [Bellingcat-Toolkit](https://bellingcat.gitbook.io/toolkit) | Werkzeugsammlung nach Plattform, je Eintrag mit Kosten und Konto-Bedarf | ohne Anmeldung |

