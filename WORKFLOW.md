# Sovinity-Produkt-Workflow für Menschen und KI

GitHub Issues sind der verbindliche Nachweis geplanter Arbeit für Sovinity. Das organisationsweite Project [Sovinity Product](https://github.com/orgs/sovinityAI/projects/1) bietet die repositoryübergreifende Übersicht; es ist kein zweites Backlog.

Sovinity ist ein Produkt mit einem Backlog. Repositories bestimmen, wo die Umsetzung stattfindet; sie begründen weder getrennte Produkte noch eigene Roadmaps oder Priorisierungslisten.

Dieser Vertrag ist werkzeugneutral und gilt gleichermaßen für Mario, Ludwig, Codex, andere KI-Agenten und zukünftige Mitwirkende. Sovinity verwendet ein Pull-System: Produktarbeit wird vorbereitet und eingeordnet, während Mitwirkende sie erst bei freier Kapazität übernehmen. Auch eine schnelle KI-Umsetzung durchläuft alle Zustände; der Status beschreibt die aktuelle Wahrheit und nicht die erwartete Dauer.

Für alle internen Texte gilt die [verbindliche Sprachregel](SPRACHE.md).

## Zuständiges Repository

- `sovinityAI/cloud`: gehostete Anwendung und private Arbeitsbereiche, Dienste, KI, Speicher, Konnektoren, Betrieb und Wiederherstellung
- `sovinityAI/SovinityDesktop`: Desktop-Anwendung, lokale Laufzeit, Paketerstellung und Stores
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
- Leere Issues sind für die normale Aufnahme deaktiviert, damit Ergebnis, Akzeptanzkriterien, Abhängigkeiten, Verifikation und Arbeitsart nicht fehlen.
- Erstellende Personen benötigen die Berechtigung, Einträge zum Organisations-Project hinzuzufügen. Wird ein Issue auf anderem Weg erstellt, füge es bei der Triage zum Project hinzu.
- Native repositoryspezifische Auto-add-Workflows dürfen vorübergehend als Sicherheitsnetz bestehen bleiben. Sie sind weder für jedes Repository erforderlich noch ersetzen sie gemeinsame Formulare oder die Erstellung aus dem Project.

## Kriterien für Bereit

Ein Issue ist bereit, wenn es Folgendes besitzt:

- ein konkretes Ergebnis,
- prüfbare Akzeptanzkriterien,
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

## Umsetzungsablauf

1. Beginne mit einem offenen Issue; erstelle zuerst eines, wenn Umsetzungsarbeit noch keines besitzt.
2. Füge das Issue zum Organisations-Project hinzu und bestätige Scope, Akzeptanzkriterien, Abhängigkeiten, vorgesehene Position im Produkt-Board und **Arbeitsart**.
3. Die Produktvorbereitung endet mit einem unzugewiesenen Issue in **Bereit**. Benenne keinen Menschen oder KI-Agenten für die Ausführung.
4. Übernimm bei freier Kapazität das oberste geeignete Issue aus **Bereit**: Prüfe, dass es nicht beansprucht ist, weise das verantwortliche GitHub-Konto zu, ergänze bei Bedarf einen KI-Übernahmekommentar und verschiebe es nach **In Arbeit**.
5. Arbeite auf einem Branch nach dem Muster `<akteur>/<issue-nummer>-<kurzname>`.
6. Halte dauerhaften Stand in GitHub fest. Chats, lokale Notizen und Agenten-Memory dürfen die Arbeit unterstützen, ersetzen aber niemals Issue-Kommentare oder Pull-Request-Nachweise.
7. Pausiert die Arbeit, kommentiere den erreichten Stand und den exakt fehlenden Input oder die Abhängigkeit; entferne die aktive Zuweisung und verschiebe das Issue nach **Benötigt Input**. Die Benennung einer Person, die Input geben kann, kennzeichnet eine Abhängigkeit und keine zugewiesene Verpflichtung.
8. Verknüpfe den Pull Request mit `Closes #<nummer>` oder der vollständigen repositoryübergreifenden Referenz.
9. Dokumentiere Tests, Prüfungen, Screenshots, Entscheidungen und verbleibende Unsicherheit im Pull Request.
10. Ist die Umsetzung bereit, entferne die Umsetzungszuweisung und verschiebe das Issue nach **In Prüfung**. Verfügbare qualifizierte Prüfende übernehmen die Prüfung.
11. Merge und schließe erst, wenn die Akzeptanzkriterien erfüllt sind; verschiebe das Issue danach nach **Erledigt**.

Ein KI-Agent muss das Project vor dem Ende seiner Arbeit abgleichen: Keine gestoppte Aufgabe darf in **In Arbeit** verbleiben und jede Pause muss die exakt nächste Aktion oder den fehlenden Input dokumentieren. KI-Agenten übernehmen Arbeit nicht stillschweigend, sondern nach demselben Protokoll wie Menschen.

Neu entdeckter Scope wird zu einem separaten verknüpften Issue. Er darf weder in einem Pull Request versteckt noch stillschweigend zum aktuellen Auftrag hinzugefügt werden.

## Issue als dauerhafte Übergabe

Das Issue oder der verknüpfte Pull Request muss es einem anderen Menschen oder KI-Agenten ermöglichen, ohne Rekonstruktion eines privaten Gesprächs weiterzuarbeiten. Halte fest:

- das aktuelle Ergebnis und geprüfte Akzeptanzkriterien,
- getroffene Entscheidungen und deren Verantwortliche,
- relevante Nachweise und Prüfergebnisse,
- ungelöste Risiken oder Blocker,
- die exakt nächste Aktion oder den fehlenden Input.

## Codex nach der nächsten Aufgabe fragen

Verwende diese Anfrage:

> Lies die offenen GitHub Issues und das Sovinity Product Project über alle Sovinity-Repositories hinweg. Gleiche veraltete Status, Zuweisungen und Arbeitsarten ab, bevor du Arbeit auswählst. Übernimm das oberste geeignete, unzugewiesene Issue aus der Bereit-Spalte des Produkt-Boards. Prüfe, dass es noch nicht beansprucht ist, beanspruche es, verschiebe es nach In Arbeit und halte Issue und Project synchron. Wenn du nur empfiehlst statt zu beginnen, empfehle genau ein Issue und nenne bis zu drei Folgeaufgaben, ohne sie zuzuweisen.
