---
date: 2025-07-24T15:01
tags:
  - Informatik
  - Rechnernetze
  - Internet
  - OSI-Schicht-3
aliases:
  - Internet Protocol
---
> IP (Internet Protocol) ist grundlegend für die Kommunikation im Internet.
> Es sorgt dafür, dass Datenpakete den richtigen Weg von einem Absender zu einem Empfänger finden - ähnlich wie eine Postadresse bei einem Brief
> Jedes Gerät im Netzwerk braucht eine eindeutige IP-Adresse, um erreichbar zu sein

## Aufgaben
1. **Adressierung**: Jedes Gerät erhält eine IP-Adresse
2. **Paketvermittlung**: Daten werden in Pakete zerlegt und weitergeleitet
3. **Routing**: Bestimmung des besten Weges durch das Netzwerk
4. **Fragmentierung**: Große Pakete werden ggf. in kleinere aufgeteilt

## IPv4

> **32-Bit-Adresse** (z.B. `192.168.0.1`)
> $2^{32} \approx 4,3\text{ Mrd Adressen}$
> Nicht mehr ausreichend auf Grund der zunehmenden Gerätezahl

### Aufbau eines Pakets
- Header (mit Absender, Empfänger, TTL, usw.)
- Nutzdaten (z.B. eine HTTP-Anfrage)


## IPv6

> **128-Bit-Adresse** (z.B. `2001:0db8:85a3:0000:0000:8a2e:0370:7334`)
> $2^{128} \approx 340\text{ Sextillionen Adressen}$
> Genug Adressen für jedes Sandkorn auf der Erde

### Vorteile gegenüber IPv4
- **Mehr Adressen**
- **Besseres Routing** (hierarchische Struktur)
- **Sicherheitsfunktionen** ([[IPsec]] ist Pflicht)
- **Kein [[NAT]] mehr nötig** (jedes Gerät kann global adressierbar sein)
- **Einfachere Konfiguration mit [[SLAAC]]** (automatische Adresszuweisung)

### Kurzschreibweise
- Führende Nullen dürfen weggelassen werden
- Mehrere aufeinanderfolgende `0000` können zu `::` zusammengefasst werden