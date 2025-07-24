---
date: 2025-07-24T16:43
tags:
  - Rechnernetze
  - Informatik
  - Internet
  - Protocol
aliases:
  - Neighbor Discovery Protocol
---
> [[IP#IPv6|IPv6]]-Protokoll, das Endgeräte und Router dabei unterstützt, Informationen über andere Geräte im Netzwerk zu erlangen

## Funktionen
|           Aufgabe           |                         Was macht NDP                          | Entsprechung in [[IP#IPv4\|IPv4]] |
| :-------------------------: | :------------------------------------------------------------: | :-------------------------------: |
|       Adressauflösung       | Findet [[MAC\|MAC-Adresse]] zu einer [[IP#IPv6\|IPv6-Adresse]] |              [[ARP]]              |
|      Router-Entdeckung      |               Findet den zuständigen [[Router]]                |  Manuelle Gateway-Konfiguration   |
|      Präfix-Entdeckung      |           Liefert Netzwerkinformation für [[SLAAC]]            |             [[DHCP]]              |
|   Erreichbarkeitsprüfung    |              Prüft, ob ein Nachbar erreichbar ist              |         [[ARP]]-Ping/ICMP         |
| Duplicate Address Detection |       Prüft, ob die eigene Adresse bereits vergeben ist        |           [[ARP]] Probe           |
| Automatische Adressvergabe  |                           [[SLAAC]]                            |             [[DHCP]]              |
