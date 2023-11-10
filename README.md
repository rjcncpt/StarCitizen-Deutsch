# [WIP] StarCitizen Deutsch global.ini

### Willkommen zu unserer deutschen Lokalisierung für Star Citizen (inkl. Umlaute)

**Diese Lokalisierung ist ein Gemeinschaftsprojekt und wird sich in vielen Bereichen unterscheiden. Es ist eine große Herausforderung, die englischen Begriffe ins verständliche Deutsch zu übertragen. Oft können wir keine 1:1-Übersetzung verwenden, da einige englische Begriffe in der deutschen Sprache mehrere Bedeutungen haben.**
<br/>

![Static Badge](https://img.shields.io/badge/Bereit-%2339cb75?label=3.21.0%20LIVE) ![Static Badge](https://img.shields.io/badge/Bereit-%2339cb75?label=3.21.1%20PTU) ![Static Badge](https://img.shields.io/badge/Kein%20Fokus-%23ff2f00?label=Preview%20Channel) 
![Static Badge](https://img.shields.io/badge/Work%20In%20Process-%23f3ac04?label=ini) [![Static Badge](https://img.shields.io/badge/%F0%9F%92%96-%23fff?label=Star%20Citizen)](https://robertsspaceindustries.com/)



<br/>

### Table of Content

- [Preview/Test Channels](#previewtest-channels)
- [Das Team](#das-team)
- [Download als ZIP](#download)
- [Direktdownload der global.ini](#direktdownload-der-globalini)
- [AUDIO FIX](#audio-fix)
- [Troubleshooting](#troubleshooting)
  <br/><br/>

Die `global.ini` ist ein Work In Progress (WIP) Projekt. Unsere Veröffentlichungen werden stets im Spiel getestet, aber dennoch können wir keine 100%ige Funktionalität garantieren. Es wird eine beträchtliche Zeit dauern, bis wir alle Texte manuell von Zeile 1 bis etwa Zeile 62000 übersetzt und überprüft haben.
<br/><br/>
An manchen Stellen hat das Spiel Schwierigkeiten mit Umlauten, zum Beispiel bei Terminals oder MouseOver. Die Umlaute werden einfach weggelassen, und es entsteht eine Lücke. Dies ist keine Übersetzungspanne, sondern ein Spielfehler. Wir behalten diese Fehler absichtlich bei, damit CIG darauf reagieren kann, und wir selbst feststellen können, ob seitens CIG Fixes vorgenommen wurden.
<br/><br/><br/>

### Preview/Test Channels

Preview und Test-Kanäle werden von uns nicht priorisiert übersetzt. Damit du an den Tests problemlos teilhaben kannst, füge ein **`;`** vor die Zeile `g_language = german_(germany)` in der `user.cfg` ein.
<br/><br/><br/>

### Das Team

| Team                                        | Fokus Position       | Beschreibung                               |
|:--------------------------------------------|:---------------------|:-------------------------------------------|
| [rjcncpt](https://github.com/rjcncpt)       | `Ansprechparter`     | Übersetzungen & GitHub                     |
| [MaxM1211](https://github.com/MaxM1211)     | `Dev & Bugfixing`    | Korrekturen, GitHub, Dev & Bugfixing       |
| [Norinofu](https://github.com/Norinofu)     | `Dev & Bugfixing`    | Korrekturen, GitHub, Dev & Bugfixing       |
| [Drakonhawk](https://github.com/Drakonhawk) | `Dev & Bugfixing`    | GitHub, Dev & Bugfixing                    |
| view                                        | `Dev & Bugfixing`    | Übersetzungen, Dev & Bugfixing             |
| Boy7                                        | `Dev & Bugfixing`    | Übersetzungen, Dev & Bugfixing             |
| electron0                                   | `Dev & Bugfixing`    | GitHub, Dev & Bugfixing                    |
| DerOrga                                     | `Dev & Bugfixing`    | Dev & Bugfixing                            |
| blazingUnknown                              | `Übersetzer`         | Übersetzungen                              |
| Hikaruhoshi1                                | `Übersetzer`         | Übersetzungen                              |
| [greluc](https://github.com/greluc)         | `Übersetzer`         | Übersetzungen (spez. militärisch) & GitHub |
| 0schinator                                  | `Übersetzer`         | Übersetzungen                              |
| APROVES                                     | `Übersetzer`         | Übersetzungen                              |
| Asaya87                                     | `Discord Management` | Übersetzungen & Discord Admin              |
| Fabi 18                                     | `Discord Management` | Discord Admin                              |

<br/>

| Dankeschön       | Position   | Beschreibung                                                                                                                       |
|:-----------------|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------|
| Claudia Fröhlich | `Lektorin` | © Einige Textblöcke werden von ihr für etwas Geld Korrektur gelesen.                                                               |
| Knebel Discord   |            | Ein großes Dankeschön geht an die vielen Einsender der [Knebel Discord Community](https://discord.com/invite/knebel) \*Invite-Link |

<br/><br/>

### Download

Lade dir [die ZIP Datei herunter](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/releases) und entpacke diese im LIVE bzw. PTU Ordner. In der ZIP Datei ist die `global.ini` und die `user.cfg` Datei enthalten. Wenn du nicht möchtest das die `user.cfg` Datei deine eigene überschreibt, lade die `global.ini` als einzelne Datei herunter.
<br/><br/>

### Installation

1. Lade dir die `StarCitizen.Deutsch.zip` herunter
2. entpacke diese
3. kopiere den Inhalt in den LIVE bzw. PTU Ordner

Im ZIP ist bereits die user.cfg enthalten.
<br/><br/><br/><br/>

### Direktdownload der global.ini

Du kannst die [global.ini auch direkt aus dem Verzeichnis laden](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/global.ini), wenn du nicht immer alles herunterladen möchtest.
<br/><br/>
![image](https://i.imgur.com/jTabj3V.png)
<br/>

### Wohin muss die global.ini Datei?

1. [Klicke hier](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/global.ini) und öffne die `global.ini` Datei
2. klicke im neuen Fenster auf den Downloadbutton oben rechts. Im Screenshot gelb markiert.
3. Erstelle die Ordner im Star Citizen Verzeichnis und füge die Datei ein. So muss der Dateipfad aussehen:<br/>
`\ Roberts Space Industries \ StarCitizen \ LIVE \ data \ Localization \ german_(germany) \ global.ini`
4. speichere ggf. die `user.cfg` in den LIVE oder PTU Ordner:<br/>
`\ Roberts Space Industries \ StarCitizen \ LIVE \`<br/>
`\ Roberts Space Industries \ StarCitizen \ PTU \`
<br/><br/><br/><br/>

### AUDIO FIX

Es gibt einen Fix für das Audio Problem. Du musst deiner `user.cfg` Datei diese folgende Zeile hinzufügen:<br/>
`g_languageAudio = english`<br/><br/>
Alternativ lade dir unsere `user.cfg` Datei herunter.

<br/><br/>

### Troubleshooting

Die `global.ini` liegt im Format `UTF-8-BOM` vor. Das ist eigentlich unnötig, und `UTF-8` würde ausreichen. Aus unerklärlichen Gründen führt dies bei einigen zu Problemen, bei denen statt der Übersetzung kryptische Variablen, die mit einem @-Zeichen beginnen, angezeigt werden. Wenn du alles richtig gemacht hast und die Datei sich im korrekten Ordner befindet, musst du wahrscheinlich die Codierung der Datei von `UTF-8` auf `UTF-8-BOM` ändern.
<br/><br/>

1. öffne die `global.ini` in einem Texteditor wie Notepad++ (kostenlos)
2. klicke anschließend in der Symbolleiste auf "Codierung"
3. wähle `UTF-8-BOM`
4. speichern
<br/><br/>

Das sollte das Problem beheben.
<br/><br/>

Salut and stay tuned!

<br/><br/><br/><br/>
-------<br/>
### Disclaimer
The entire repository is licensed under a [CC-BY-4.0](http://creativecommons.org/licenses/by/4.0/) license. To provide the best possible quality, we commission a lecturer to proofread some of the text modules. The copyright is held by Claudia Fröhlich (representing René Jansen). You may use our global.ini file privately and commercially, but you must not identify yourself as the author of this global.ini.
<br/><br/>
Our German localisation is an unofficial Star Citizen fan project and is not associated with the Cloud Imperium Games group of companies.
<br/><br/>
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
