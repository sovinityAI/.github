# Arbeitsregeln für das öffentliche Organisations-Repository

## Ergebnisregel und vollständiger Abschluss

Ein führendes Issue umfasst den vollständig erreichbaren Mehrwert einschließlich Analyse, Umsetzung, Integration, Tests, Review und erforderlicher Bereitstellung/Abnahme. Kleine Schritte werden als Checkliste geführt; Repositorygrenzen oder Arbeitsphasen erzeugen keine eigenen Erfolgstickets. Mehrere PRs in mehreren Repositories dürfen demselben Issue dienen.

Ein Produkt-Issue ist erst fertig, wenn der Mehrwert nachgewiesen und der integrierte Stand potenziell auslieferbar ist: im normalen nächsten Build beziehungsweise Dev-Start vorhanden und im vereinbarten Modus nutzbar. Erforderliche native, Integrations-, Deployment- und Live-Nachweise gehören zum selben Issue. Ein einzelner Merge, eine abgeschaltete Funktion oder ausgelagerte Abnahmereste genügen nicht. Betriebs-, Prozess- und Entscheidungsaufträge benötigen entsprechend einen vollständig wirksamen, nutzbaren Abschluss.

Notwendige Restschritte bleiben im Ergebnis-Issue; nur unabhängige zusätzliche Ergebnisse erhalten eigene Issues. Teil-PRs verwenden `Refs`; `Closes` erst, wenn der Merge sämtliche Abschlusskriterien erfüllt. Zusammenführungen erhalten alle offenen Kriterien und Nachweise; abgelöste Tickets werden als zusammengeführt (`not_planned`) geschlossen und im Project archiviert, nicht als erreichten Mehrwert gezählt. Aktive Zuständigkeiten und Übergaben bleiben erhalten. Maßgeblich ist die [gemeinsame Ergebnisregel](https://github.com/sovinityAI/.github-private/blob/main/WORKFLOW.md#ein-issue-ein-vollständig-erreichtes-ergebnis).

## Scope

- Dieses Repository ist öffentlich. Es enthält ausschließlich das öffentliche Organisationsprofil, öffentliche Hinweise und die von GitHub organisationsweit verwendeten Issue- und Pull-Request-Vorlagen.
- Interne Produktsteuerung, Kennzahlen, Verantwortlichkeiten, Betriebsdetails und ausführliche Workflow-Dokumentation gehören in das private Repository [`sovinityAI/.github-private`](https://github.com/sovinityAI/.github-private).
- Produktstrategie und Entscheidungen bleiben im privaten Repository [`sovinityAI/product`](https://github.com/sovinityAI/product).

## Änderungen

- Beginne Änderungen nur auf Grundlage eines offenen verknüpften Issues mit prüfbaren Akzeptanzkriterien. Wenn der vollständige Kontext nicht öffentlich sein soll, darf das koordinierende Issue in `.github-private` liegen.
- Lies Issue, Kommentare, Abhängigkeiten und Akzeptanzkriterien vollständig und halte die Änderung innerhalb des vereinbarten Scopes.
- Prüfe bei Issue-Erstellung und fachlicher Überarbeitung sowie vor **Bereit** und vor der Übernahme ausdrücklich Motivation und Mehrwert: welches Problem oder welche Chance besteht, wer oder was profitiert und was sich verbessert. Das gilt auch für CLI/API und freie Browser-Issues. Ergänze fehlende Begründungen aus belegtem Kontext; kläre unklaren Nutzen vor der Übernahme im Issue. Zielzustand und Akzeptanzkriterien ersetzen diese Prüfung nicht. Details und Unter-Issue-Regel: [gemeinsamer Workflow](https://github.com/sovinityAI/.github-private/blob/main/WORKFLOW.md#inhaltliche-prüfung-von-motivation-und-mehrwert).
- Verwende einen Branch nach dem Muster `<akteur>/<issue-nummer>-<kurzname>` und einen Pull Request auf Deutsch; unveränderliche technische Bezeichner dürfen englisch bleiben.
- Dokumentiere ausgeführte Prüfungen und verbleibende Risiken. Schließe ein Issue erst nach nachgewiesener Erfüllung der Akzeptanzkriterien.
- Veröffentliche niemals Zugangsdaten, personenbezogene Daten, private Testdaten, Kundendokumente, interne Betriebsdetails oder umgebungsspezifische Geheimnisse.

## Öffentliche Aussagen

- Trenne bestätigte Produktentscheidungen, verifizierte Umsetzungsfakten, Hypothesen und offene Fragen.
- Behaupte keine Veröffentlichung, Plattformunterstützung, Lizenzierung, Compliance, Sicherheitsgarantie oder Produkteigenschaft ohne aktuellen Nachweis.
- Das öffentliche Profil beschreibt Sovinity Docs als lokale Anwendung für eine Person. Teamnutzung, gemeinsame Arbeitsräume und Serverbetrieb sind keine aktuelle Produktzusage.
- Gemeinsame Vorlagen bleiben repositoryneutral und enthalten keine repositoryspezifischen Produktanforderungen.

Der vollständige interne Lebenszyklus und die Sprachregel liegen für Organisationsmitglieder in `.github-private`.
