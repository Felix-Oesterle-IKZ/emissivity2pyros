# emissivity2pyros

## Beschreibung
Emissivity2pyros baut auf dem Skript exp-T-control-v3 und seinen Vorgängern auf. Das Skript wurde so angepasst, dass zusätzlich ein Ratiopyrometer  angesteuert werden kann. Damit kann die Vergleichstemperatur ermittelt werden, ohne PT-Sensor.

---
## Veränderungen zu exp-T-control-v3 und multilog.

### Messreihe_Rezept.txt
In Messreihe_Rezept.txt wurde ein zusätzlicher Parameter eingeführt, um das Messgerät auszuwählen. "pyro" wählt das Ratiopyrometer als Vergleichssensor aus. "pt" wählt den PT-Sensor in der Probe aus als Vergleichssensor

### pyrometer_lumasense.py und config_Parameter.yml
Bei den Lummasenses Pyrometer (Z.B. IGA-6-23 or IGAR-6-adv) kann jetzt zusätzlich in der .yml Datei eingestellt werden das Verhältnis k (0.8 <= k <= 1.2) und der Operationsmodus (0: metal, 1: mono, 2: ratio, 3: smart). Zusätzlich wurden einige Funktionen pyrometer_lumasense.py implementiert, um die Handhabung des Hauptprogramms zu vereinfachen.

---
## Weitere Informationen
Für eine detailliertere Anleitung siehe:
https://github.com/nemocrys/exp-T-control-v3
https://github.com/nemocrys/exp-T-control-v2
https://github.com/nemocrys/exp-T-control