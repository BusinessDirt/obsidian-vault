---
date: 2025-07-24T17:24
tags:
  - Rechnernetze
  - Internet
  - Informatik
aliases:
  - CRC
---
Der **CRC** ist ein Verfahren zur **Fehlererkennung** bei der Datenübertragung oder -speicherung.  
Er hilft zu prüfen, ob Daten unterwegs beschädigt wurden.

# Funktion
1. **Daten werden als Bitfolge interpretiert** (z. B. `1101011011`)
2. Es gibt einen vorgegebenen **Generatorpolynom** (auch "Divisor" genannt), z. B. `1101`
3. Die Datenbits werden durch dieses Polynom **modulo 2** (XOR-Verknüpfung statt normale Division) dividiert
4. Der **Rest der Division** ist der CRC-Wert (eine kurze Prüfsumme)
5. Dieser CRC-Wert wird **an die Daten angehängt** und übertragen