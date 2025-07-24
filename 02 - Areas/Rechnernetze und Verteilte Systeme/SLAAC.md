---
date: 2025-07-24T15:55
tags:
  - Informatik
  - Rechnernetze
  - Internet
aliases:
  - Stateless Address Autoconfiguration
---
> Ein Mechanismus bei **[[IP#IPv6|IPv6]]**, mit dem ein Gerät **automatisch** eine eigene IP-Adresse erhält - **ohne [[DHCP]]-Server**

## Funktion
1. Das Gerät lauscht im Netzwerk auf Router-Advertisements.
2. Es erzeugt selbstständig eine **globale IPv6-Adresse**, z.B. aus Präfix + [[MAC|MAC-Adresse]] 
	- Der Präfix stammt vom Router (z.B. ``)
	- ``
3. Kein Zustand (Stateless) wird gespeichert, daher: “Stateless”

## Vorteile
- Einfach und schnell
- Kein zentraler Adressserver nötig

## Alternativen:
- **[[DHCP#DHCPv6|DHCPv6]]** (stateful, zentraler Server)
- **Manuelle Konfiguration**