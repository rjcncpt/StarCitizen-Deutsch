# [WIP] Star Citizen deutsche Lokalisierung (global.ini)

### Willkommen zu unserer deutschen Lokalisierung für Star Citizen (inkl. Umlaute)

**Diese Lokalisierung ist ein Gemeinschaftsprojekt und wird sich in vielen Bereichen unterscheiden. Es ist eine große Herausforderung, die englischen Begriffe ins verständliche Deutsch zu übertragen. Oft können wir keine 1:1-Übersetzung verwenden, da einige englische Begriffe in der deutschen Sprache mehrere Bedeutungen haben.**
<br/>

![Static Badge](https://img.shields.io/badge/Bereit-%2339cb75?label=3.21.1%20LIVE) <!--![Static Badge](https://img.shields.io/badge/Bereit-%2339cb75?label=3.21.1%20PTU)--> ![Static Badge](https://img.shields.io/badge/Kein%20Fokus-%23ff2f00?label=Preview%20Channel) 
![Static Badge](https://img.shields.io/badge/Work%20In%20Process-%23f3ac04?label=ini) [![Static Badge](https://img.shields.io/badge/%F0%9F%92%96-%23fff?label=Star%20Citizen)](https://robertsspaceindustries.com/)



<br/>

### Table of Content

- [Preview/Test Channels](#previewtest-channels)
- [Download als ZIP](#download)
- [Direktdownload der global.ini](#direktdownload-der-globalini)
- [Das Team](#das-team)
- [Troubleshooting](#troubleshooting)
  <br/><br/>

Die **`global.ini`** ist ein Work In Progress (WIP) Projekt. Unsere Veröffentlichungen werden stets im Spiel getestet, aber dennoch können wir keine 100%ige Funktionalität garantieren. Es wird eine beträchtliche Zeit dauern, bis wir alle Texte manuell von Zeile 1 bis etwa Zeile 62000 übersetzt und überprüft haben.
<br/><br/>
An manchen Stellen hat das Spiel Schwierigkeiten mit Umlauten, zum Beispiel bei Terminals oder MouseOver. Die Umlaute werden einfach weggelassen, und es entsteht eine Lücke. Dies ist keine Übersetzungspanne, sondern ein Spielfehler. Wir behalten diese Fehler absichtlich bei, damit CIG darauf reagieren kann, und wir selbst feststellen können, ob seitens CIG Fixes vorgenommen wurden.
<br/><br/><br/>

### Preview/Test Channels

Preview und Test-Kanäle werden von uns nicht unterstützt. Damit du an den Tests problemlos teilhaben kannst, füge ein **`;`** vor die Zeile **`g_language = german_(germany)`** in der **`user.cfg`** ein, um Star Citizen in engl. Sprache zu spielen.
<br/><br/><br/>

### Download

Täglich um 4 Uhr Nachts wird aus den Fixes des Vortags automatisch ein LIVE-Release erstellt. Lade dir **[die neuste ZIP Datei herunter](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/releases)** und entpacke diese im LIVE Ordner. (Nutzt du die INI Datei für LIVE im PTU, kann es zu Darstellungsfehlern kommen wenn sich die Versionsnummern unterscheiden.)<br/><br/>

In der ZIP Datei befindet sich die **`global.ini`** und die **`user.cfg`** Datei. Wenn du nicht möchtest das die **`user.cfg`** Datei deine eigene überschreibt, lade die **`global.ini`** **[als einzelne Datei herunter](#direktdownload-der-globalini)**. Diese findest du im **`live`** Ordner. Im **`ptu`** Ordner liegt die **`global.ini`** die für den aktuellen PTU gedacht ist. Bitte nutzt nur die Dateien, welche für den jeweiligen Channel ausgelegt sind.
<br/>

#### Installation

1. Lade dir die **`StarCitizen.Deutsch.zip`** herunter
2. Entpacke diese
3. Kopiere den Inhalt in den LIVE bzw. PTU Ordner
<br/><br/><br/><br/>

### Direktdownload der global.ini

Du kannst die **[global.ini auch direkt aus dem Verzeichnis laden](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/live/global.ini)**, wenn du nicht immer alles herunterladen möchtest. Der Vorteil ist, diese Datei ist immer auf einem aktuelleren Stand als die Release Datei.
<br/><br/>
![image](https://i.imgur.com/jTabj3V.png)
<br/>

#### Wohin muss die global.ini Datei?

1. **[Klicke hier](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/live/global.ini)** und öffne die `global.ini` Datei
2. Klicke im neuen Fenster auf den Downloadbutton oben rechts. Im Screenshot gelb markiert.
3. Erstelle die Ordner im Star Citizen Verzeichnis und füge die Datei ein. So muss der Dateipfad aussehen:<br/>
**`\ Roberts Space Industries \ StarCitizen \ LIVE \ data \ Localization \ german_(germany) \ global.ini`**
4. speichere ggf. die `user.cfg` in den LIVE oder PTU Ordner:<br/>
**`\ Roberts Space Industries \ StarCitizen \ LIVE \`**<br/>
**`\ Roberts Space Industries \ StarCitizen \ PTU \`**
<br/><br/><br/><br/>

### Das Team

| Team                                        | Fokus Position       | Beschreibung                               |
|:--------------------------------------------|:---------------------|:-------------------------------------------|
| [rjcncpt](https://github.com/rjcncpt)       | `Ansprechparter`     | Übersetzungen & GitHub                     |
| [MaxM1211](https://github.com/MaxM1211)     | `Dev & Bugfixing`    | Korrekturen, GitHub, Dev & Bugfixing       |
| [greluc](https://github.com/greluc)         | `Übersetzer`         | Übersetzungen (spez. militärisch) & GitHub |
| [Norinofu](https://github.com/Norinofu)     | `Dev & Bugfixing`    | Korrekturen, GitHub, Dev & Bugfixing       |
| [Drakonhawk](https://github.com/Drakonhawk) | `Dev & Bugfixing`    | GitHub, Dev & Bugfixing                    |
| Boy7                                        | `Dev & Bugfixing`    | Übersetzungen, Dev & Bugfixing             |
| Hikaruhoshi1                                | `Übersetzer`         | Übersetzungen                              |
| electron0                                   | `Dev & Bugfixing`    | GitHub, Dev & Bugfixing                    |
| APROVES                                     | `Übersetzer`         | Übersetzungen                              |
| Asaya87                                     | `Discord Management` | Übersetzungen & Discord Admin              |
| Fabi 18                                     | `Discord Management` | Discord Admin                              |

<br/>

| Dankeschön       | Position   | Beschreibung                                                                                                                       |
|:-----------------|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------|
| Claudia Fröhlich | `Lektorin` | © Einige Textblöcke werden von ihr für etwas Geld Korrektur gelesen.                                                               |
| Knebel Discord   |            | Ein großes Dankeschön geht an die vielen Einsender der **[Knebel Discord Community](https://discord.com/invite/knebel)** \*Invite-Link |

<br/><br/>

### Troubleshooting

<details>
<summary>[Klick] Fehler: Es werden kryptische Variablen mit @-Zeichen am Anfang angezeigt</summary>
<br/>

Unsere **`global.ini`** Datei liegt bereits im korrekten **`UTF-8-BOM`** im Format vor. Wenn bei dir Variablen angezeigt werden, die mit einem @-Zeichen beginnen, aber die Ordnerstuktur richtig ist, scheint deine Datei-Codierung falsch zu sein. Lade entweder **[unsere Datei erneut herunter](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/live/global.ini)** oder stelle die Codierung deiner Datei manuell um:
<br/><br/>

1. Öffne die **`global.ini`** in einem Texteditor wie Notepad++ (kostenlos)
2. Klicke anschließend in der Symbolleiste auf "Codierung"
3. Wähle **`UTF-8-BOM`**
4. Speichern
<br/><br/>

Das sollte das Problem beheben.
___________
</details>


<details>
<summary>[Klick] Fehler: Ich habe alles richtig gemacht, aber es werden immer noch englische Texte angezeigt</summary>
<br/>

Achte bei den beiden Dateien **`global.ini`** und **`user.cfg`** auf die richtigen Dateiendungen.
<br/><br/>

Kontrolliere ob es die richtige Dateiendung ist:

1. Öffne den Windows Dateiexplorer
2. Klicke auf Ansicht am oberen Fensterrand
3. Aktiviere im Bereich Ein-/ausblenden: **`Dateinamenerweiterungen`**
4. Sollten die beiden Dateien nun **`global.ini.ini`** oder **`user.txt.cfg`** oder ähnlich heißen, musst du sie zurück in **`global.ini`** und **`user.cfg`** umbennenen.
<br/><br/>

Das sollte das Problem beheben.
___________
</details>


<details>
<summary>[Klick] Fehler: Keine englische Sprachausgabe im Spiel</summary>
<br/>

Es gibt einen Fix für das Audio Problem. Du musst deiner **`user.cfg`** Datei diese folgende Zeile hinzufügen:<br/>
**`g_languageAudio = english`**<br/><br/>
Alternativ lade dir unsere **`user.cfg`** Datei herunter, in der wir das bereits für dich übernommen haben.
<br/><br/>

Das sollte das Problem beheben.
___________
</details>

<br/><br/>
Salut and stay tuned!

<br/><br/><br/><br/>
-------<br/>
**Note about lecturer**<br/>
The entire repository is licensed under a [CC-BY-4.0](http://creativecommons.org/licenses/by/4.0/) license. To provide the best possible quality, we commission a lecturer to proofread some of the text modules. The copyright is held by Claudia Fröhlich. You may use our global.ini file privately and commercially, but you must not identify yourself as the author of this global.ini.
<br/><br/>
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
