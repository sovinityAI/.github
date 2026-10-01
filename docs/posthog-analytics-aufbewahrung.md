# PostHog-Analytics: Aufbewahrung und Loeschung

Stand: 01.10.2026

Auftrag: [sovinityAI/.github#37](https://github.com/sovinityAI/.github/issues/37)

Produktentscheidungen: [product#14](https://github.com/sovinityAI/product/issues/14), [product#33](https://github.com/sovinityAI/product/issues/33)

## Zweck und Grenze

Sovinity speichert freiwillige, pseudonyme und inhaltsfreie Analytics-Einzelereignisse nur so lange, wie sie fuer die beschriebene Auswertung und Produktverbesserung erforderlich sind. Der Bestand wird regelmaessig geprueft. Nicht mehr benoetigte Ereignisse werden geloescht, in der Regel nach drei Monaten und spaetestens nach sechs Kalendermonaten.

PostHogs tarifgebundene Aufbewahrung ist laut Anbieter-API nur lesbar. Sie ersetzt diese Sovinity-Grenze nicht. Der Lauf nutzt deshalb die offizielle Vorschau und die selbstbediente Ereignisloeschung. Die Loeschung ist asynchron; ein angenommener Auftrag ist noch kein Abschlussnachweis.

## Positivliste

Der Client in `scripts/posthog_retention.py` waehlt nur Ereignisse aus, fuer die alle folgenden Bedingungen gelten:

- `environment=production`
- `synthetic=false`
- `surface=website` oder `surface=docs`
- Ereignisname in der versionierten Website-/Docs-Positivliste
- sechsmonatige Hoechstfrist endet innerhalb des 14-taegigen Sicherheitsfensters

Das Sicherheitsfenster beruecksichtigt, dass PostHog Loeschauftraege asynchron und gegebenenfalls erst in einem spaeteren Wartungsfenster abschliesst. Es verlaengert die Aufbewahrung nicht; Ereignisse duerfen dadurch etwas vor ihrer Hoechstfrist geloescht werden. Monatsenden werden kalendarisch begrenzt, nicht pauschal als 180 Tage berechnet.

Eine zweite Vorschau zaehlt unbekannte Sovinity-Produktionsereignisse im selben Zeitraum. Jeder Treffer bricht den Lauf ab. Neue Ereignisse muessen zuerst fachlich freigegeben und in die Positivliste aufgenommen werden.

## Zugang und Geheimnisse

Der GitHub-Secretname lautet `POSTHOG_RETENTION_API_KEY`. Das zugehoerige PostHog Personal API Token benoetigt ausschliesslich:

- `data_deletion:read`
- `data_deletion:write`

Der oeffentliche Projekt-Token `phc_...` ist dafuer ungeeignet. Ein persoenliches Token `phx_...` darf weder in Git, Issue, Pull Request, Workflow-Ausgabe noch Browser-Screenshot erscheinen. Nach Erzeugung wird es unmittelbar als Repository-Secret in `sovinityAI/.github` gespeichert. Bei vermuteter Offenlegung wird es zuerst in PostHog widerrufen, danach ersetzt und der Vorfall dokumentiert.

## Ablauf

1. Der taegliche Zeitplan prueft zuerst fruehere Loeschauftraege.
2. `failed` blockiert jeden neuen Auftrag und laesst den Workflow fehlschlagen.
3. `draft`, `pending`, `approved`, `in_progress` oder `queued` verhindert Doppelauftraege. Nach mehr als neun Tagen wird daraus ein sichtbarer Fehler.
4. Ohne offenen Auftrag prueft der Client unbekannte Ereignisse und danach die Positivliste.
5. Bei null Treffern endet der Lauf ohne Loeschauftrag.
6. Bei Treffern erzeugt `reconcile-submit` eine idempotente Tageskennung und reicht die unveraenderliche Einspaltenabfrage `SELECT uuid` ein.
7. Ein spaeterer Lauf muss den Status `completed` sehen. Bis dahin darf nur von einem eingereichten oder laufenden Auftrag gesprochen werden.

Der manuelle Workflow-Modus `dry-run` fuehrt beide Vorschauen aus, loescht aber nichts. `reconcile-submit` kann loeschen und darf erst nach dokumentierter Betriebsfreigabe verwendet werden. Der Zeitplan verwendet denselben Modus; ohne Secret scheitert er sicher und sichtbar.

## Protokollierung

Zulaessig sind nur:

- UTC-Grenzzeitpunkt und Sicherheitsfenster
- Anzahl der Vorschautreffer
- technischer Fingerabdruck der unveraenderten Abfrage
- technische Loeschauftragskennung und Status
- Anzahl bereits abgeschlossener Auftraege

Nicht protokolliert werden Ereignis-UUIDs, Besuchs-/App-Kennungen, Eigenschaften, Inhalte, API-Antworttexte oder das Token. HTTP-Fehler werden nur als Statuscode ausgegeben.

## Produktionsgate und Stoerung

Vor dem ersten echten Analytics-Ereignis muessen ein kontrollierter PostHog-EU-Dry-run, ein eingereichter synthetischer Testauftrag und dessen asynchroner Abschluss nachgewiesen sein. Jede tatsaechliche Loeschung benoetigt die im Issue dokumentierte Freigabe. Website und App bleiben bei einem Ausfall voll nutzbar; produktiver Analytics-Versand wird jedoch nicht neu freigegeben und bei einem dauerhaften Loeschfehler ueber die vorhandene Modulgrenze wieder ausgeschaltet.

Die Anbieter-Dokumentation, ein HTTP-2xx oder ein gespeicherter Insight sind allein kein Loeschnachweis. Der Abschlussstatus des konkreten Auftrags und eine anschliessende Null-Vorschau fuer denselben Bereich sind erforderlich.

## Lokale Pruefung

```bash
python -m unittest discover -s tests -p 'test_posthog_retention.py' -v
```

Die Tests verwenden ausschliesslich simulierte API-Antworten und loeschen keine Daten.
