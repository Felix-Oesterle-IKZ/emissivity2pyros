# emissivity2pyros

## Beschreibung
Emissivity2pyros baut auf dem Skript exp-T-control-v3 und seinen Vorg�ngern auf. Das Skript wurde so angepasst, dass zus�tzlich ein Ratiopyrometer  angesteuert werden kann. Damit kann die Vergleichstemperatur ermittelt werden, ohne PT-Sensor.

---
## Ver�nderungen zu exp-T-control-v3 und multilog.

### Messreihe_Rezept.txt
In Messreihe_Rezept.txt wurde ein zus�tzlicher Parameter eingef�hrt, um das Messger�t auszuw�hlen. "pyro" w�hlt das Ratiopyrometer als Vergleichssensor aus. "pt" w�hlt den PT-Sensor in der Probe aus als Vergleichssensor

### pyrometer_lumasense.py und config_Parameter.yml
Bei den Lummasenses Pyrometer (Z.B. IGA-6-23 or IGAR-6-adv) kann jetzt zus�tzlich in der .yml Datei eingestellt werden das Verh�ltnis k (0.8 <= k <= 1.2) und der Operationsmodus (0: metal, 1: mono, 2: ratio, 3: smart). Zus�tzlich wurden einige Funktionen pyrometer_lumasense.py implementiert, um die Handhabung des Hauptprogramms zu vereinfachen.

---
## Weitere Informationen
F�r eine detailliertere Anleitung siehe:
https://github.com/nemocrys/exp-T-control-v3
https://github.com/nemocrys/exp-T-control-v2
https://github.com/nemocrys/exp-T-control