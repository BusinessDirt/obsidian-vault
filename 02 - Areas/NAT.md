---
date: 2025-07-24T15:55
tags:
  - Informatik
  - Rechnernetze
  - Internet
aliases:
  - Network Address Translation
---
> Ein Mechanismus, bei dem eine oder mehrere private IP-Adressen (z.B. im Heimnetz) in eine öffentliche IP-Adresse umgewandelt werden - und umgekehrt

## Warum gibt es NAT?
- Weil **IPv4 zu wenig Adressen bietet**
- NAT ermöglicht, dass viele Geräte **eine einzige öffentliche IPv4-Adresse teilen**

## Beispiel:
- Dein PC hat die private IP `192.168.0.2`
- Der Router übersetzt sie nach außen zu z.B. `85.214.50.1`
- Für Webseiten sieht es so aus, als käme der gesamte Datenverkehr von `85.214.50.1`

## Probleme:
- NAT macht direkte Verbindungen (z.B. für Online-Gaming oder VoIP) schwieriger
- Wird bei [[IP#IPv6|IPv6]] **nicht mehr benötigt**