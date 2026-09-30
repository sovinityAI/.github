# Sovinity-Produkt-Workflow für Menschen und KI

GitHub Issues sind der verbindliche Nachweis geplanter Arbeit für Sovinity. Das organisationsweite Project [Sovinity Product](https://github.com/orgs/sovinityAI/projects/1) bietet die repositoryübergreifende Übersicht; es ist kein zweites Backlog.

Sovinity ist eine Produktfamilie mit einem gemeinsamen Backlog. Repositories bestimmen, wo die Umsetzung stattfindet; sie begründen nicht automatisch ein eigenes Produkt, ein eigenes Backlog oder eigene Roadmaps und Priorisierungslisten. Das erste konkrete Produkt ist **Sovinity Docs**.

Dieser Vertrag ist werkzeugneutral und gilt gleichermaßen für Mario, Ludwig, Codex, andere KI-Agenten und zukünftige Mitwirkende. Sovinity verwendet ein Pull-System: Produktarbeit wird vorbereitet und eingeordnet, während Mitwirkende sie erst bei freier Kapazität übernehmen. Auch eine schnelle KI-Umsetzung durchläuft alle Zustände; der Status beschreibt die aktuelle Wahrheit und nicht die erwartete Dauer.

Für alle internen Texte gilt die [verbindliche Sprachregel](SPRACHE.md).

## Zuständiges Repository

- `sovinityAI/cloud`: gehostete Anwendung und private Arbeitsbereiche, Dienste, KI, Speicher, Konnektoren, Betrieb und Wiederherstellung
- `sovinityAI/SovinityDocs`: Desktop-Anwendung, lokale Laufzeit, Paketerstellung und Stores
- `sovinityAI/website`: öffentliche Website, Domains, Rechtstexte und Veröffentlichungsarbeit
- `sovinityAI/product`: repositoryübergreifende Vision, Strategie, Roadmap, Entscheidungen und Discovery
- `sovinityAI/.github`: organisationsweite Prozesse, gemeinsame Vorlagen und repositoryübergreifende Governance

Repositoryübergreifende Vorhaben verwenden ein Eltern-Issue mit repositoryspezifischen Unter-Issues. Abhängigkeiten werden als GitHub-Issue-Beziehungen erfasst und nicht nur im Fließtext beschrieben.

## Portabler Zugang für Menschen und KI

Sovinity verwendet vorhandene offene Formate statt eines herstellerspezifischen Agenten- oder Memory-Protokolls:

- [`AGENTS.md`](https://agents.md/) enthält Arbeitsanweisungen auf Repository-Ebene für Menschen und kompatible KI-Coding-Agenten.
- Kann ein Werkzeug `AGENTS.md` nicht direkt laden, darf sein kleinstmöglicher Adapter diese Datei importieren oder darauf verweisen. Gemeinsame Regeln dürfen nicht in eine konkurrierende werkzeugspezifische Quelle kopiert werden.
- [Agent Skills](https://agentskills.io/) (`SKILL.md`) dürfen wiederverwendbare Abläufe, Skripte, Referenzen und Vorlagen bündeln. Sie dürfen keine aktuelle Produktstrategie, Roadmap, Entscheidungen, Zugangsdaten oder personenbezogenen Daten enthalten.
- Das [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) darf Agenten mit externen Werkzeugen und Daten verbinden. Es ist eine Integrationsschnittstelle und kein Ersatz für dauerhafte Project-Nachweise.
- GitHub Issues, Pull Requests und versionierte Repository-Dokumente enthalten dauerhaften Auftrags- und Produktstand. Chatverläufe, lokale Notizen, Profile, Memory und Sitzungen beliebiger Werkzeuge dürfen einzelne Mitwirkende unterstützen, sind aber nicht kanonisch und können verworfen werden.

## Produktmeilensteine und Ansichten

Das Project-Feld **Produktmeilenstein** gruppiert Issues repositoryübergreifend nach Produktergebnis. Es ist das gemeinsame Meilensteinmodell; Repository-Meilensteine bleiben lokale Metadaten und dürfen es nicht ersetzen.

Das Project pflegt folgende Arbeitsansichten:

- **Produkt-Board**: kanonische Rangfolge aller Produktarbeit, gruppiert nach Status und in jeder Spalte manuell sortiert; Repository, Produktmeilenstein, Arbeitsart und Benötigter Input sind dort sichtbar, wo sie helfen
- **Team-Aufgaben**: tabellarische Übersicht der Zuweisungen und des aktuellen Arbeitsstands
- **Produkt-Roadmap**: zeitliche Planung über Startdatum und Zieldatum
- **Meine Aufgaben**: persönliche Ansicht mit dem Filter `assignee:@me`
- **Produktmeilensteine**: Produktarbeit gruppiert nach Produktmeilenstein, unabhängig vom Umsetzungs-Repository
- **Produktbetrieb**: Organisationsprozesse und Governance-Arbeit aus `sovinityAI/.github`

Ein Issue erscheint einmal im gemeinsamen Project. Sein Repository zeigt, wo es umgesetzt wird. Ein repositoryübergreifendes Ergebnis besitzt ein koordinierendes Eltern-Issue und verknüpfte Umsetzungs-Issues in den Repositories, denen die jeweiligen Änderungen gehören.

## Aufnahme neuer Issues

- Erstelle ein Issue vorzugsweise aus dem Project, wenn das Umsetzungs-Repository bereits bekannt ist.
- Verwende andernfalls das gemeinsame Formular **Produktaufgabe** oder **Fehlerbericht**. Die Formulare fügen das neue Issue über `projects: ["sovinityAI/1"]` zu **Sovinity Product** hinzu.
- Leere Issues sind für die normale Aufnahme deaktiviert, damit Motivation und Mehrwert, Zielzustand, Akzeptanzkriterien, Abhängigkeiten, Verifikation und Arbeitsart nicht fehlen.
- Die Project-Zuordnung ist ein verbindliches Aufnahme-Gate. Ein Issue gilt erst als aufgenommen, wenn seine Mitgliedschaft in `sovinityAI/projects/1` nach der Erstellung gelesen und bestätigt wurde.
- Wird ein Issue per CLI, API oder auf einem anderen Weg außerhalb der Formulare erstellt, füge es unmittelbar zum Project v2 hinzu und verifiziere die Zuordnung, bevor du es zuweist, einen Branch erstellst oder mit der Umsetzung beginnst. Schlägt die Zuordnung oder Verifikation fehl, stoppt die Arbeit an diesem Issue.
- Native repositoryspezifische Auto-add-Workflows dürfen vorübergehend als Sicherheitsnetz bestehen bleiben. Sie sind weder für jedes Repository erforderlich noch ersetzen sie gemeinsame Formulare oder die Erstellung aus dem Project.

Für die GitHub CLI benötigt die Anmeldung den OAuth-Scope `project`:

```sh
gh auth refresh -s project
```

Da `gh issue create --project` je nach GitHub-CLI-Version noch das veraltete Projects-classic-Modell abfragen kann, verwendet der belastbare Project-v2-Weg zwei ausdrücklich geprüfte Schritte:

```sh
issue_url="$(gh issue create --repo OWNER/REPOSITORY --title "TITEL" --body-file ISSUE_BODY.md)"
gh project item-add 1 --owner sovinityAI --url "$issue_url"
gh issue view "$issue_url" --json projectItems --jq '.projectItems'
```

Die letzte Ausgabe muss das Project `sovinity` enthalten. Erst danach werden Status, Arbeitsart und gegebenenfalls Zuweisung gesetzt.

Prüfe bei jeder repositoryübergreifenden Backlog-Sichtung zusätzlich, ob offene Issues außerhalb des Projects existieren:

```text
org:sovinityAI is:issue is:open no:project
```

Jeder Treffer wird vor der Auswahl neuer Arbeit zum Project hinzugefügt und eingeordnet.

**Motivation und Mehrwert** erklären die gewünschte Wirkung: welches heutige Problem oder welche Chance das Issue adressiert, wer oder was profitiert und was sich nach dem Abschluss für Nutzende, Produkt, Betrieb oder Zusammenarbeit verbessert. Der **Zielzustand** beschreibt davon getrennt, was konkret erreicht sein muss. Belastbare qualitative Aussagen genügen; Kennzahlen werden nur verwendet, wenn sie tatsächlich belegt oder als Ziel entschieden sind.

Ein eigenständiges Issue beschreibt seinen eigenen Mehrwert. Ein repositoryspezifisches Unter-Issue darf den Mehrwert aus seinem Eltern-Issue übernehmen, wenn es darauf verweist und seinen eigenen Beitrag zum übergeordneten Nutzen benennt. Reine Checkbox-Unteraufgaben innerhalb eines Issues benötigen keinen eigenen Abschnitt. Bestehende Issues werden nicht massenhaft umgeschrieben; Motivation und Mehrwert werden ergänzt, sobald ein Issue fachlich überarbeitet oder nach **Bereit** verschoben wird.

## Kriterien für Bereit

Ein Issue ist bereit, wenn es Folgendes besitzt:

- eine nachvollziehbare Motivation und einen verständlichen Mehrwert,
- einen konkreten Zielzustand,
- prüfbare Akzeptanzkriterien,
- eine verifizierte Zuordnung zu `sovinityAI/projects/1`,
- das richtige Repository und die vorgesehene Position von oben nach unten im Produkt-Board,
- bekannte Abhängigkeiten oder die ausdrückliche Angabe, dass keine bekannt sind,
- genügend Kontext, um ohne erfundene Produktentscheidungen zu beginnen,
- keinen ungelösten Blocker, der externe Zuständigkeit oder sensible Informationen erfordert,
- keine Zuweisung oder bestehende Übernahme.

## Project-Status

- **Backlog**: gültige Arbeit, die noch nicht bereit oder ausgewählt ist
- **Bereit**: ausreichend beschrieben, nicht blockiert, manuell eingeordnet, nicht zugewiesen und zur Übernahme verfügbar
- **In Arbeit**: von einem Menschen oder KI-Agenten übernommen und aktiv bearbeitet, auch wenn die Umsetzung nur wenige Minuten dauert
- **Benötigt Input**: pausiert wegen einer benannten Entscheidung, Abhängigkeit, sensiblen Information oder externen Zuständigkeit
- **In Prüfung**: Ein Ergebnis liegt vor und menschliche, rechtliche, visuelle oder technische Nachweise werden geprüft
- **Erledigt**: Die Akzeptanzkriterien sind verifiziert und das Issue ist geschlossen

Jedes Issue in **Benötigt Input** muss im Feld **Benötigter Input** kurz die fehlende Entscheidung, Information, Abhängigkeit oder das externe Ergebnis nennen. Lösche oder aktualisiere den Wert, wenn das Issue diesen Status verlässt.

## Arbeitsart

Das Project-Feld **Arbeitsart** hilft Mitwirkenden zu entscheiden, ob ein Issue zur Übernahme geeignet ist. Es ist eine Einordnung und niemals eine Zuweisung:

- **Alle Mitwirkenden**: keine besondere Einschränkung für die Ausführung
- **KI-geeignet**: ausreichend abgegrenzte Arbeit, die ein KI-Agent ausführen darf; Menschen dürfen sie ebenfalls übernehmen
- **Menschliche Entscheidung**: Eine Produkt-, Rechts-, Finanz-, Ethik- oder andere Entscheidung muss ein Mensch treffen
- **Gemeinsame Arbeit**: Die Arbeit sollte von zwei Menschen oder einem Menschen gemeinsam mit einem KI-Agenten ausgeführt werden
- **Extern**: Der Abschluss hängt von Kundschaft, Rechts- oder Steuerberatung, Sicherheitsprüfung oder einer anderen Partei außerhalb des aktiven Teams ab

Ein Issue in **Bereit** bleibt unabhängig von seiner Arbeitsart unzugewiesen. Die Arbeitsart reserviert keine Arbeit und begründet keine Verpflichtung.

## Manuelle Rangfolge

Die gespeicherte Reihenfolge von oben nach unten in jeder Statusspalte des **Produkt-Boards** ist das einzige Priorisierungsmodell. Es gibt keine Prioritätsstufen, Titelpräfixe, Prioritätslabels oder separaten Prioritätsfelder.

- **Backlog**: Der oberste Eintrag ist der nächste Kandidat zur Ausarbeitung und Vorbereitung.
- **Bereit**: Das oberste geeignete Issue ist als Nächstes zu übernehmen.
- **In Arbeit**: Der oberste Eintrag erhält zuerst Aufmerksamkeit, wenn aktive Arbeit konkurriert.
- **Benötigt Input**: Der oberste Eintrag ist der nächste zu lösende Blocker oder die nächste Entscheidung.
- **In Prüfung**: Der oberste Eintrag ist das nächste zu prüfende Ergebnis.
- **Erledigt**: Die manuelle Reihenfolge darf aus Konsistenzgründen erhalten bleiben, bestimmt aber keine zukünftige Arbeit.

Abhängigkeiten bleiben explizite Issue-Beziehungen. Verhindert eine Abhängigkeit die Umsetzung, ist das Issue nicht bereit und gehört nach **Benötigt Input**, statt weiter unten in **Bereit** zu stehen. Da GitHub die manuelle Reihenfolge in der Ansichtskonfiguration speichert, müssen Mitwirkende das Produkt-Board nach dem Verschieben von Karten speichern.

## Pull-Prinzip und Begrenzung paralleler Arbeit

- Mario und Ludwig pflegen Ergebnisse, Bereitschaft, Abhängigkeiten und die gespeicherte Reihenfolge von oben nach unten in jeder Statusspalte des **Produkt-Boards**.
- Mitwirkende mit freier Kapazität übernehmen das oberste geeignete Issue aus **Bereit**. Das Überspringen eines höheren Eintrags erfordert einen kurzen Issue-Kommentar mit dem Zugriffs- oder Eignungsgrund; ein blockiertes Issue muss **Bereit** verlassen.
- Lies das Issue vor der Übernahme erneut und prüfe, dass es weiterhin **Bereit**, unzugewiesen und ohne neueren Übernahmekommentar ist.
- Übernimm atomar: Weise das verantwortliche GitHub-Konto zu, ergänze bei einer KI ohne eigene GitHub-Identität einen Übernahmekommentar und verschiebe das Issue vor der Bearbeitung nach **In Arbeit**.
- Jede mitwirkende Person oder KI-Sitzung hat normalerweise höchstens ein Umsetzungs-Issue in **In Arbeit**. Eine Ausnahme muss in beiden betroffenen Issues begründet werden.
- Auch Prüfung wird übernommen. Ein Ergebnis nach **In Prüfung** zu verschieben, weist es keiner prüfenden Person zu; verfügbare qualifizierte Prüfende übernehmen die Prüfung.

Pull ist keine beliebige Auswahl. Die Produktverantwortung bestimmt, was bereit ist und an welcher Stelle es im Produkt-Board steht; die Kapazität der Mitwirkenden bestimmt, wann das nächste geeignete Issue beginnt.

## CI-Auslieferungsgate für `main`

Die verpflichtende Continuous Integration (CI) auf `main` ist das gemeinsame Signal, dass der integrierte Produktstand gebaut, geprüft und ausgeliefert werden kann. Schlägt ein verpflichtender Build, Test oder Paketierungsschritt auf dem aktuellen `main`-Stand fehl, hat die Wiederherstellung dieses Signals höchste operative Priorität. Ein nur auf einem Feature-Branch fehlgeschlagener Lauf fällt nicht unter dieses Gate; er wird vor dem Merge im zugehörigen Issue oder Pull Request behoben.

Während das Gate ausgelöst ist:

1. Verifiziere den Fehlschlag am aktuellen `main`-Commit und sichere einen datensparsamen Link oder Logauszug als Nachweis. Ein erneuter Lauf darf einen vermuteten Infrastruktur- oder Flake-Fehler prüfen, ersetzt aber nicht die Ursachenklärung, wenn der Fehler wiederkehrt.
2. Verwende ein passendes offenes Fehler-Issue im betroffenen Repository oder erstelle sofort eines. Bestätige die Project-Zuordnung, ordne es ein und übernimm es nach dem normalen Protokoll. Die manuelle Rangfolge regulärer Produktarbeit setzt diese betriebliche Vorrangregel nicht außer Kraft.
3. Unterbrich reguläre Umsetzungsarbeit im betroffenen Repository. Dokumentiere den sicheren Zwischenstand im bisherigen Issue, entferne dessen aktive Zuweisung und verschiebe es zurück nach **Bereit**. Gehört es wegen einer anderen benannten Abhängigkeit nach **Benötigt Input**, dokumentiere stattdessen genau diese Abhängigkeit. So bleibt die normale WIP-Grenze trotz der Sofortmaßnahme erhalten.
4. Setze reguläre Merges und Releases im betroffenen Repository aus. Zulässig sind nur Änderungen, die unmittelbar der Diagnose oder Wiederherstellung des Gates dienen.
5. Stelle die Lieferfähigkeit mit einer vorwärtsgerichteten Änderung wieder her:
   - Deaktiviere bevorzugt das verursachende Feature über ein vorhandenes Feature-Flag oder eine gleichwertige Modulgrenze und verwende dessen sicheren Standardzustand.
   - Ist eine getrennte Deaktivierung nicht sicher möglich oder liegt die Ursache außerhalb eines Features, korrigiere die Ursache mit dem kleinsten gezielten Fix, der den vollständigen Lieferpfad wiederherstellt.
   - Das Zurücksetzen bereits integrierter Commits ist in diesem Prozess kein regulärer Wiederherstellungsweg.
6. Deaktiviere keine verpflichtende Prüfung und schwäche kein Erfolgskriterium ab, nur um einen grünen Status zu erzeugen. Eine deaktivierte Produktfunktion darf den fehlerhaften Pfad nicht weiterhin beim Start, Build oder in der Auslieferung ausführen.
7. Führe die verpflichtenden Prüfungen für die Wiederherstellungsänderung aus und bestätige danach den erfolgreichen Lauf auf dem tatsächlich aktualisierten `main`-Commit. Erst dann werden reguläre Merges und Releases wieder aufgenommen.
8. Trenne Wiederherstellung und dauerhafte Ursachenbehebung: Hat eine Feature-Deaktivierung das Gate wieder geöffnet, dokumentiere die noch offene Ursache und die Bedingungen für eine erneute Aktivierung in einem verknüpften Folge-Issue. Das Feature bleibt bis zum nachgewiesenen Fix deaktiviert.

Diese Vorrangregel ersetzt die Nachweispflicht nicht. Issue, Pull Request und Project halten Ursache, gewählte Wiederherstellung, Prüfungen, verbleibendes Risiko und Folgearbeit dauerhaft fest.

### Modularität und sichere Deaktivierung

Neue Funktionen mit relevantem Integrations- oder Auslieferungsrisiko werden so zugeschnitten, dass ihr Fehler möglichst nicht den Kernpfad blockiert. Wo eine Funktion unabhängig aktiviert werden kann, besitzt sie ein Feature-Flag oder eine gleichwertige Modulgrenze. Der deaktivierte Zustand ist sicher, umgeht den Funktionspfad tatsächlich und wird ebenso geprüft wie der aktivierte Zustand. Eine Funktion wird nach einer störungsbedingten Deaktivierung erst wieder aktiviert, wenn Ursachenfix und verpflichtende Prüfungen nachgewiesen sind.

## Preview-, Staging- und Produktionsfreigabe

Dieser Abschnitt gilt für Repositories, die neben Produktion eine getrennte Preview-, Staging-, QA- oder Vorabnahmeumgebung betreiben. Repositoryspezifische Dokumentation legt Branches, Zielpfade, Deploymenttechnik und erlaubte Testdaten fest. Ein erfolgreicher Pull-Request-Check belegt nur den geprüften Quellstand; er ersetzt keinen Nachweis, dass derselbe Kandidat in der vorgesehenen Umgebung bereitgestellt und dort geprüft wurde.

1. Weise eine gemeinsam genutzte Vorabnahmeumgebung genau einem Issue beziehungsweise Freigabekandidaten zu. Issue oder Pull Request nennen den belegenden Auftrag, den bereitgestellten Git-Stand und offene Freigaben. Parallele Arbeit darf den Slot nicht stillschweigend überschreiben.
2. Stelle den aktuellen Kandidaten ausgehend vom aktuellen `main`-Stand bereit. Dokumentiere den erfolgreichen Deployment-Lauf, den Commit und die geprüften URLs oder Pfade. Zugangsdaten und andere Geheimnisse gehören nicht in Issue, Pull Request oder Logs.
3. Prüfe die Akzeptanzkriterien in der laufenden Vorabnahmeumgebung. Eine Freigabe gilt nur für den tatsächlich bereitgestellten Kandidaten. Jede nachfolgende Codeänderung, jeder Rebase und jede Konfliktauflösung macht den bisherigen Nachweis ungültig und erfordert eine erneute Bereitstellung und Prüfung.
4. Bei einem Squash-Merge darf die resultierende Commit-ID von der geprüften Commit-ID abweichen. In diesem Fall muss der Git-Tree des gemergten Stands dem freigegebenen Kandidaten entsprechen; eine gleiche Beschreibung oder ein nur ähnlich wirkender Inhalt genügt nicht.
5. Merge und Produktionsfreigabe bleiben getrennte Entscheidungen. Nach dem Merge werden der erfolgreiche Produktionslauf und die betroffenen produktiven Pfade geprüft und im Issue oder Pull Request festgehalten.
6. Synchronisiere den Preview-/Staging-Zeiger danach mit dem freigegebenen Produktionsstand. Ist der Slot bereits dokumentiert an den nächsten Kandidaten übergeben, bleibt dessen Stand bestehen und die Übergabe wird ausdrücklich genannt. Ein nicht vorwärtsgerichtetes Umsetzen eines reinen Deployment-Zeigers ist nur nach Prüfung des aktuellen Slot-Eigentümers, des exakten Zielstands und mit einem gegen parallele Änderungen abgesicherten Verfahren zulässig.
7. Schließe das Issue erst, wenn Produktionsnachweis und erwarteter Zustand der Vorabnahmeumgebung belegt sind. Bei ausdrücklich Preview-only angelegter Arbeit entfallen Merge und Produktionsnachweis; Scope, verbleibende Freigaben und der weiterhin belegte Preview-Slot müssen dann im offenen Issue sichtbar bleiben.

Wo Plattformfunktionen ein technisches Deployment- oder Merge-Gate erlauben, sollen sie diesen Ablauf zusätzlich absichern. Fehlt diese Möglichkeit, bleiben die dokumentierten Nachweise und die gemeinsame Pull-Request-Checkliste verbindlich. Der bei `sovinityAI/website#47` und `sovinityAI/website#49` sichtbar gewordene fehlende Preview-Abgleich ist der Anlass für diese Klarstellung; der historische Auftragsstand wird dadurch nicht rückwirkend verändert.

## Umsetzungsablauf

1. Beginne mit einem offenen Issue; erstelle zuerst eines, wenn Umsetzungsarbeit noch keines besitzt.
2. Füge das Issue zum Organisations-Project hinzu, lies die Project-Zuordnung zurück und bestätige Motivation und Mehrwert, Zielzustand, Scope, Akzeptanzkriterien, Abhängigkeiten, vorgesehene Position im Produkt-Board und **Arbeitsart**. Ohne bestätigte Project-Zuordnung endet der Ablauf hier.
3. Die Produktvorbereitung endet mit einem unzugewiesenen Issue in **Bereit**. Benenne keinen Menschen oder KI-Agenten für die Ausführung.
4. Übernimm bei freier Kapazität das oberste geeignete Issue aus **Bereit**: Prüfe, dass es nicht beansprucht ist, weise das verantwortliche GitHub-Konto zu, ergänze bei Bedarf einen KI-Übernahmekommentar und verschiebe es nach **In Arbeit**.
5. Arbeite auf einem Branch nach dem Muster `<akteur>/<issue-nummer>-<kurzname>`.
6. Halte dauerhaften Stand in GitHub fest. Chats, lokale Notizen und Agenten-Memory dürfen die Arbeit unterstützen, ersetzen aber niemals Issue-Kommentare oder Pull-Request-Nachweise.
7. Pausiert die Arbeit, kommentiere den erreichten Stand und den exakt fehlenden Input oder die Abhängigkeit; entferne die aktive Zuweisung und verschiebe das Issue nach **Benötigt Input**. Die Benennung einer Person, die Input geben kann, kennzeichnet eine Abhängigkeit und keine zugewiesene Verpflichtung.
8. Verknüpfe den Pull Request mit `Closes #<nummer>` oder der vollständigen repositoryübergreifenden Referenz.
9. Dokumentiere Tests, Prüfungen, Screenshots, Entscheidungen und verbleibende Unsicherheit im Pull Request.
10. Ist die Umsetzung bereit, entferne die Umsetzungszuweisung und verschiebe das Issue nach **In Prüfung**. Verfügbare qualifizierte Prüfende übernehmen die Prüfung.
11. Merge erst, wenn die Akzeptanzkriterien und gegebenenfalls die Preview-/Staging-Freigabe erfüllt sind. Schließe erst nach den erforderlichen Produktions- und Synchronisierungsnachweisen; verschiebe das Issue danach nach **Erledigt**.
12. Bereinige nach einem verifizierten Merge den zugehörigen Remote-Branch sowie nicht mehr benötigte lokale Branches und Worktrees. Prüfe vor dem Löschen, dass die aktuelle Branch-Spitze dem gemergten Pull-Request-Stand entspricht und keine späteren ungemergten Commits enthält. Branches mit offenen oder ohne Merge geschlossenen Pull Requests, aktive Worktrees und ausdrücklich aufbewahrte Backups bleiben bestehen, bis ihre Übernahme, Verwerfung oder weitere Aufbewahrung ausdrücklich entschieden und dokumentiert ist.

Ein KI-Agent muss das Project vor dem Ende seiner Arbeit abgleichen: Keine gestoppte Aufgabe darf in **In Arbeit** verbleiben und jede Pause muss die exakt nächste Aktion oder den fehlenden Input dokumentieren. KI-Agenten übernehmen Arbeit nicht stillschweigend, sondern nach demselben Protokoll wie Menschen.

Neu entdeckter Scope wird zu einem separaten verknüpften Issue. Er darf weder in einem Pull Request versteckt noch stillschweigend zum aktuellen Auftrag hinzugefügt werden.

## Issue als dauerhafte Übergabe

Das Issue oder der verknüpfte Pull Request muss es einem anderen Menschen oder KI-Agenten ermöglichen, ohne Rekonstruktion eines privaten Gesprächs weiterzuarbeiten. Halte fest:

- Motivation und Mehrwert sowie den aktuellen Zielzustand,
- geprüfte Akzeptanzkriterien,
- getroffene Entscheidungen und deren Verantwortliche,
- relevante Nachweise und Prüfergebnisse,
- ungelöste Risiken oder Blocker,
- die exakt nächste Aktion oder den fehlenden Input.

## Codex nach der nächsten Aufgabe fragen

Verwende diese Anfrage:

> Lies die offenen GitHub Issues und das Sovinity Product Project über alle Sovinity-Repositories hinweg. Gleiche veraltete Status, Zuweisungen und Arbeitsarten ab, bevor du Arbeit auswählst. Übernimm das oberste geeignete, unzugewiesene Issue aus der Bereit-Spalte des Produkt-Boards. Prüfe, dass es noch nicht beansprucht ist, beanspruche es, verschiebe es nach In Arbeit und halte Issue und Project synchron. Wenn du nur empfiehlst statt zu beginnen, empfehle genau ein Issue und nenne bis zu drei Folgeaufgaben, ohne sie zuzuweisen.

Die Sichtung umfasst den organisationsweiten Filter `org:sovinityAI is:issue is:open no:project`. Offene Treffer werden zuerst zum Project hinzugefügt und eingeordnet; sie dürfen nicht außerhalb des gemeinsamen Backlogs bearbeitet werden.
