---
date: 2025-07-24T15:55
tags:
  - Informatik
  - Rechnernetze
  - Internet
aliases:
  - Stateless Address Autoconfiguration
---
> Ein Mechanismus bei **[[IP#IPv6|IPv6]]**, mit dem ein Gerät **automatisch** eine eigene IP-Adresse erhält - **ohne [[DHCP|DHCP-Server]]**

## Funktion
1. Das Gerät lauscht im Netzwerk auf [[Router#Router Advertisement (RA)|Router-Advertisements (RA)]]
2. Es erzeugt selbstständig eine **globale IPv6-Adresse**, z.B. aus Präfix + [[MAC|MAC-Adresse]] 
	- Der Präfix stammt vom [[Router]] (z.B. `2001:db8:abcd:1234::/64`)
	- Rest wird aus der [[MAC|MAC-Adresse]] generiert `2001:db8:abcd:1234:xxxx:xxxx:xxxx:xxxx`
3. Kein Zustand wird gespeichert, daher: “Stateless”
## Vorteile
- Einfach und schnell
- Kein zentraler Adressserver nötig
## Alternativen:
- **[[DHCP#DHCPv6|DHCPv6]]** (stateful, zentraler Server)
- **Manuelle Konfiguration**