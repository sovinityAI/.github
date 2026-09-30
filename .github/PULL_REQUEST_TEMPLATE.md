## Issue

Closes <!-- #123 oder owner/repository#123 -->

## Ergebnis

<!-- Was hat sich für Nutzende, Betrieb oder Produkt geändert? -->

## Verifikation

- [ ] Relevante automatisierte Tests oder Prüfungen sind erfolgreich
- [ ] Akzeptanzkriterien wurden anhand konkreter Nachweise geprüft
- [ ] Nutzerseitige oder Layout-Änderungen wurden, wo erforderlich, visuell geprüft
- [ ] Es sind keine Zugangsdaten, privaten Daten oder umgebungsspezifischen Geheimnisse enthalten

Nachweise:

<!-- Befehle, Ergebnisse, Screenshots oder andere prüfbare Nachweise. -->

## Umgebungsfreigabe

<!-- Für Repositories ohne getrennte Vorabnahme- und Produktionsumgebung jeweils „Nicht zutreffend“ mit kurzer Begründung eintragen. Keine Zugangsdaten oder privaten Testdaten angeben. -->

- [ ] Preview/Staging: Slot-Zuordnung, bereitgestellter Commit, erfolgreicher Lauf und live geprüfte URLs/Pfade sind nachgewiesen oder nicht zutreffend
- [ ] Der Preview-/Staging-Nachweis stammt vom letzten Code-Stand nach Rebase, Konfliktlösung oder sonstiger Änderung
- [ ] Bei einem geplanten Squash-Merge ist der Vergleich des freigegebenen und gemergten Git-Trees als Abschlussnachweis vorgesehen
- [ ] Produktion: Lauf und live geprüfte Pfade werden nach dem Merge im Issue oder Pull Request nachgetragen oder sind laut Scope nicht vorgesehen
- [ ] Preview/Staging wird anschließend mit Produktion synchronisiert oder die kontrollierte Übergabe an den nächsten Kandidaten wird dokumentiert

Nachweise oder Begründung:

<!-- Links auf Deployment-Läufe, Commit/Tree, geprüfte URLs/Pfade und verbleibende Freigaben. -->

## Scope und Risiko

<!-- Migrationen, Datenschutz-/Sicherheitsfolgen, Rückabwicklung und verbleibende Unsicherheit dokumentieren. -->

## Folgearbeit

<!-- Separate Issues für neu entdeckten Scope verknüpfen. „Keine“ schreiben, falls nichts folgt. -->

## Project-Übergabe

- [ ] Verknüpftes Issue und Project-Status bilden den aktuellen Stand ab
- [ ] Die Umsetzungszuweisung ist entfernt, sobald die Arbeit in die Prüfwarteschlange wechselt
- [ ] Die `Arbeitsart` beschreibt die Eignung, ohne die Prüfung jemandem zuzuweisen
- [ ] Bei einer Pause dokumentiert das Issue den exakt fehlenden Input oder die Abhängigkeit
