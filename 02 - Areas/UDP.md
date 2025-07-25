---
date: 2025-07-24T15:11
tags:
  - Informatik
  - Rechnernetze
  - Internet
  - OSI-Schicht-4
  - Protocol
aliases:
  - User Datagram Protocol
---
## Eigenschaften
- **Verbindungslos**: Keine vorherige Verbindung nötig.
- **Unzuverlässig**: Es gibt keine Garantie, dass Pakete ankommen oder in der richtigen Reihenfolge
- **Keine Fehlerkorrektur**: Wenn ein Paket verloren geht, wird es nicht automatisch neu gesendet.
- **Schnell & leichtgewichtig**: Geringer Overhead, gut für Echtzeit-Anwendungen

## Anwendungsbeispiele
- Videstreaming
- Online-Spiele
- VoIP (Telefonie über Internet)
- [[DNS]] (Domain Name System)

## Funktion
1. Sender schickt einfach Datenpakete los - “Fire and Forget”
2. Empfänger nimmt ankommende Pakete, ohne Rückmeldung.