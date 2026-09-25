# Sovinity-Arbeitsvereinbarung für Menschen und KI

## GitHub-Auftragsvertrag

- GitHub Issues sind die verbindliche Quelle für geplante Arbeit. Das organisationsweite Project ist [Sovinity Product](https://github.com/orgs/sovinityAI/projects/1).
- Sovinity hat ein gemeinsames Product Backlog über alle Repositories hinweg. Das Repository bestimmt den technischen Umsetzungsort; es begründet weder ein eigenes Produkt noch ein eigenes Backlog.
- Umsetzungsarbeit benötigt ein offenes Issue in dem Repository, dem das Ergebnis gehört. Organisationsweite Prozesse und Vorlagen gehören in `sovinityAI/.github`.
- Lies vor jeder Änderung das vollständige Issue einschließlich Kommentaren, Labels, Abhängigkeiten, verknüpften Pull Requests und Akzeptanzkriterien.
- Halte Änderungen innerhalb des Issue-Scopes. Neu entdeckte Arbeit wird als separates verknüpftes Issue erfasst, statt den Scope stillschweigend zu erweitern.
- Markiere ein Issue erst dann als abgeschlossen, wenn jedes Akzeptanzkriterium anhand konkreter Nachweise geprüft wurde.
- Chats, lokale Notizen und Agenten-Memory sind kein dauerhafter Auftragsstand. Halte Entscheidungen, Blocker, Übergaben und Abschlussnachweise im GitHub Issue oder im verknüpften Pull Request fest.
- Neue und wesentlich überarbeitete interne Arbeit wird nach [SPRACHE.md](SPRACHE.md) auf Deutsch geführt.

## Verbindliche Project-Synchronisierung

Menschen und KI-Agenten verwenden in [Sovinity Product](https://github.com/orgs/sovinityAI/projects/1) denselben Lebenszyklus:

- **Backlog**: gültige Arbeit, die noch nicht bereit oder ausgewählt ist.
- **Bereit**: ausreichend beschrieben, nicht blockiert, manuell eingeordnet, nicht zugewiesen und für geeignete Mitwirkende verfügbar.
- **In Arbeit**: Ein Mensch oder KI-Agent hat das Issue übernommen und arbeitet aktiv daran, auch wenn die Arbeit nur wenige Minuten dauert.
- **Benötigt Input**: Die Arbeit pausiert wegen einer benannten Entscheidung, Abhängigkeit, sensiblen Information oder externen Zuständigkeit.
- **In Prüfung**: Ein Ergebnis liegt vor und wartet auf menschliche, rechtliche, visuelle oder technische Prüfung.
- **Erledigt**: Die Akzeptanzkriterien sind nachgewiesen und das Issue ist geschlossen.

Halte das Project-Feld **Arbeitsart** aktuell: `Alle Mitwirkenden`, `KI-geeignet`, `Menschliche Entscheidung`, `Gemeinsame Arbeit` oder `Extern`. Es beschreibt die Arbeit und weist sie niemandem zu.

Halte bei Produktarbeit das Project-Feld **Produktmeilenstein** aktuell. Produktmeilensteine beschreiben repositoryübergreifende Ergebnisse. Repository-Meilensteine bleiben lokale Metadaten und dürfen nicht als gemeinsame Produkt-Roadmap dienen.

- Erstelle neue Arbeit aus dem Project oder über die gemeinsamen Issue-Formulare der Organisation. Beide Wege müssen das Issue zu **Sovinity Product** hinzufügen.
- Erstelle für normale Produktarbeit keine leeren Issues. Wird ausnahmsweise ein Wartungs-Issue ohne Formular angelegt, füge es sofort dem Project hinzu.
- Native Auto-add-Workflows des Projects sind optionale Sicherheitsnetze und nicht die verbindliche Quelle für die Aufnahme.
- Produktarbeit wird in **Bereit** vorbereitet und eingeordnet; sie wird keinem Menschen oder KI-Agenten zugewiesen.
- Bei Übernahme: Prüfe, dass das Issue weiterhin unzugewiesen und nicht übernommen ist, weise es dir oder dem verantwortlichen GitHub-Konto zu, ergänze bei einer KI ohne eigene GitHub-Identität einen kurzen Übernahmekommentar und verschiebe das Issue nach **In Arbeit**.
- Begrenze parallele Arbeit auf ein Umsetzungs-Issue pro mitwirkender Person oder KI-Sitzung, sofern keine dokumentierte Ausnahme erforderlich ist.
- Bei einer Pause: Ergänze einen knappen Issue-Kommentar mit dem erreichten Stand und dem exakt fehlenden Input oder der Abhängigkeit, entferne die aktive Zuweisung und verschiebe das Issue nach **Benötigt Input**.
- Nach Abschluss der Umsetzung: Dokumentiere die Prüfnachweise, entferne die Umsetzungszuweisung und verschiebe das Issue nach **In Prüfung**, damit verfügbare Prüfende es übernehmen können.
- Nach verifiziertem Abschluss: Schließe das Issue und verschiebe es nach **Erledigt**.
- Lasse ein Issue nie in **In Arbeit**, wenn die Arbeit gestoppt wurde oder eine Agenten-Sitzung ohne aktive Fortsetzung endet.

## Auswahl der nächsten Aufgabe

- Prüfe bei der Frage nach der nächsten Aufgabe die offenen Issues in `sovinityAI/cloud`, `sovinityAI/SovinityDesktop`, `sovinityAI/website`, `sovinityAI/product` und `sovinityAI/.github`.
- Schließe Epics, Arbeit in **Benötigt Input** und Issues aus, die bereits durch einen offenen Pull Request abgedeckt sind.
- Übernimm Arbeit aus **Bereit**, nicht aus bereits zugewiesener Arbeit anderer Mitwirkender. Verwende die gespeicherte Reihenfolge des Produkt-Boards von oben nach unten: Das oberste geeignete Issue in **Bereit** ist als Nächstes dran.
- Überspringe Arbeit, deren **Arbeitsart** für die verfügbaren Mitwirkenden ungeeignet ist. `KI-geeignet` bedeutet, dass eine KI die Arbeit ausführen darf; Menschen sind dadurch nicht ausgeschlossen.
- Empfiehl genau ein nächstes Issue und nenne getrennt davon bis zu drei Folgeaufgaben.

## Git und Pull Requests

- Verwende für Umsetzungsarbeit einen Branch nach dem Muster `<akteur>/<issue-nummer>-<kurzname>`, zum Beispiel `codex/12-fix-import` oder `ludwig/12-fix-import`.
- Referenziere das Issue in Commits und Pull Requests. Verwende `Closes #<nummer>` für Issues im selben Repository oder `Closes owner/repository#<nummer>` für repositoryübergreifende Issues.
- Pull Requests müssen die Änderung zusammenfassen, die ausgeführten Prüfungen nennen und verbleibende Risiken oder unerfüllte Akzeptanzkriterien offenlegen.
- Führe Pull Requests und Commits auf Deutsch; technische Präfixe und unveränderliche Bezeichner dürfen gemäß [SPRACHE.md](SPRACHE.md) bestehen bleiben.
- Merge oder schließe ein Issue nicht allein deshalb, weil Dateien geändert wurden; der Nachweis entscheidet über den Abschluss.

## Werkzeugneutrale Agentenregeln

- Verwende `AGENTS.md` im Repository als gemeinsame, werkzeugneutrale Anweisungsdatei. Ein werkzeugspezifischer Adapter darf sie bei Bedarf importieren oder darauf verweisen, aber keine abweichende Kopie der gemeinsamen Regeln pflegen.
- Halte dauerhaften Auftrags- und Produktstand in GitHub und versionierten Repository-Dokumenten fest. Chatverläufe, lokale Notizen, Profile, Memory und Sitzungen einzelner KI-Werkzeuge sind temporäre Hilfen und niemals gemeinsame Infrastruktur oder verbindliche Quelle.
- Verwende Agent Skills (`SKILL.md`) nur für wiederverwendbare Abläufe, Skripte, Referenzen und Vorlagen. Lege dort keine aktuelle Produktstrategie, Roadmap, Entscheidungen, Zugangsdaten oder personenbezogenen Daten ab.
- Verwende das Model Context Protocol (MCP) nur, wenn eine standardisierte Schnittstelle zu externen Werkzeugen oder Daten benötigt wird. MCP-Verbindungen ersetzen Issues, Pull Requests und Repository-Dokumente nicht als dauerhaften Nachweis.

## Scope des Organisations-Repositories

- Halte gemeinsame Issue-Formulare, Pull-Request-Vorlagen, Workflow-Dokumentation und das öffentliche Organisationsprofil sachlich und wiederverwendbar.
- Nimm keine repositoryspezifischen Produktanforderungen in gemeinsame Vorlagen auf.
- Füge niemals Geheimnisse, personenbezogene Daten, rein interne Betriebsdetails oder unbelegte öffentliche Aussagen hinzu.
